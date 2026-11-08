import { Injectable, OnModuleInit } from '@nestjs/common';
import {
  ACHIEVEMENTS,
  ACHIEVEMENT_COINS,
  AchievementDef,
  AchievementStats,
  achievementProgress,
  achievementReward,
  longestStreak,
  masteryOf,
  newlyUnlocked,
} from '@koto/learning-engine';
import type { AchievementCheckDto, AchievementDto, AchievementsDto } from '@koto/shared';
import { Prisma } from '@prisma/client';
import { PrismaService } from '../common/prisma.service';
import { ClockService } from '../common/clock.service';
import { toCardState } from '../learning/card-mapper';

@Injectable()
export class AchievementsService implements OnModuleInit {
  constructor(private prisma: PrismaService, private clock: ClockService) {}

  /** Le catalogue vit dans le moteur ; la table sert de référence pour les clés étrangères. */
  async onModuleInit() {
    try {
      for (const d of ACHIEVEMENTS) {
        await this.prisma.achievement.upsert({
          where: { slug: d.slug },
          create: { slug: d.slug, title: d.title, description: d.description, rarity: d.rarity },
          update: { title: d.title, description: d.description, rarity: d.rarity },
        });
      }
    } catch {
      // Base indisponible au démarrage : la synchronisation sera refaite à la première vérification.
    }
  }

  /** Statistiques agrégées, toutes recalculées depuis la base (aucune valeur fournie par le client). */
  async stats(userId: string): Promise<AchievementStats> {
    const now = this.clock.now();
    const [lessons, activity, cards, bosses, examsTaken, examsPassed, games, items, placement] = await Promise.all([
      this.prisma.userLessonProgress.count({ where: { userId, status: 'completed' } }),
      this.prisma.dailyActivity.findMany({ where: { userId }, select: { dateKey: true, total: true, correct: true, reviews: true, bestCombo: true, perfectLessons: true } }),
      this.prisma.reviewCard.findMany({ where: { userId }, include: { item: { select: { kind: true } } } }),
      this.prisma.bossResult.count({ where: { userId, firstVictoryAt: { not: null } } }),
      this.prisma.examAttempt.count({ where: { userId, finishedAt: { not: null } } }),
      this.prisma.examAttempt.count({ where: { userId, passed: true } }),
      this.prisma.gameResult.findMany({ where: { userId }, select: { plays: true, bestScore: true } }),
      this.prisma.inventoryItem.count({ where: { userId } }),
      this.prisma.learningSession.count({ where: { userId, kind: 'placement', endedAt: { not: null } } }),
    ]);
    let masteredItems = 0;
    let masteredKanji = 0;
    for (const c of cards) {
      if (masteryOf(toCardState(c), now) !== 'mastered') continue;
      masteredItems++;
      if (c.item.kind === 'kanji') masteredKanji++;
    }
    return {
      lessonsCompleted: lessons,
      perfectLessons: activity.reduce((n, d) => n + d.perfectLessons, 0),
      bestStreak: longestStreak(activity.filter((d) => d.total > 0).map((d) => d.dateKey)),
      correctAnswers: activity.reduce((n, d) => n + d.correct, 0),
      reviewsDone: activity.reduce((n, d) => n + d.reviews, 0),
      bestCombo: activity.reduce((n, d) => Math.max(n, d.bestCombo), 0),
      masteredItems,
      masteredKanji,
      bossesDefeated: bosses,
      examsTaken,
      examsPassed,
      gamesPlayed: games.reduce((n, g) => n + g.plays, 0),
      bestGameScore: games.reduce((n, g) => Math.max(n, g.bestScore), 0),
      itemsCollected: items,
      placementDone: placement > 0 ? 1 : 0,
    };
  }

  private async unlockedMap(userId: string) {
    const rows = await this.prisma.userAchievement.findMany({ where: { userId }, include: { achievement: { select: { slug: true } } } });
    return new Map(rows.map((r) => [r.achievement.slug, r.unlockedAt]));
  }

  private toDto(def: AchievementDef, value: number, unlocked: boolean, at: Date | null): AchievementDto {
    return {
      slug: def.slug, title: def.title, description: def.description, glyph: def.glyph, category: def.category, rarity: def.rarity,
      value, target: def.target, unlocked, unlockedAt: at?.toISOString() ?? null, coins: ACHIEVEMENT_COINS[def.rarity],
    };
  }

  async list(userId: string): Promise<AchievementsDto> {
    const [stats, done] = await Promise.all([this.stats(userId), this.unlockedMap(userId)]);
    const progress = achievementProgress(stats, done.keys());
    return {
      unlocked: progress.filter((p) => p.unlocked).length,
      total: progress.length,
      achievements: progress.map((p) => this.toDto(p.def, p.value, p.unlocked, done.get(p.def.slug) ?? null)),
    };
  }

  /**
   * Enregistre les succès nouvellement atteints et crédite leur récompense une seule fois :
   * la clé primaire (utilisateur, succès) bloque une double attribution, même en cas d'appels simultanés.
   */
  async check(userId: string): Promise<AchievementCheckDto> {
    const [stats, done] = await Promise.all([this.stats(userId), this.unlockedMap(userId)]);
    const candidates = newlyUnlocked(stats, done.keys());
    const granted: AchievementDef[] = [];
    for (const def of candidates) {
      try {
        await this.prisma.$transaction(async (tx) => {
          const row = await tx.achievement.upsert({ where: { slug: def.slug }, create: { slug: def.slug, title: def.title, description: def.description, rarity: def.rarity }, update: {} });
          await tx.userAchievement.create({ data: { userId, achievementId: row.id } });
          const r = achievementReward([def]);
          await tx.user.update({ where: { id: userId }, data: { coins: { increment: r.coins }, xp: { increment: r.xp } } });
          await tx.xpEvent.create({ data: { userId, amount: r.xp, reason: 'achievement', refId: def.slug } });
        });
        granted.push(def);
      } catch (e) {
        if (!(e instanceof Prisma.PrismaClientKnownRequestError && e.code === 'P2002')) throw e;
      }
    }
    const reward = achievementReward(granted);
    const at = this.clock.now();
    return { unlocked: granted.map((d) => this.toDto(d, d.target, true, at)), coinsGained: reward.coins, xpGained: reward.xp };
  }
}
