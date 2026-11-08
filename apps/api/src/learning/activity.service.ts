import { Injectable } from '@nestjs/common';
import { COINS, QuestStatus, dailyQuests, localParts } from '@koto/learning-engine';
import type { DailyActivity } from '@prisma/client';
import { PrismaService } from '../common/prisma.service';
import { ClockService } from '../common/clock.service';

export interface ActivityDelta {
  seconds?: number;
  answered?: boolean;
  correct?: boolean;
  review?: boolean;
  newItem?: boolean;
  kanjiReview?: boolean;
  listeningCorrect?: boolean;
  perfectLesson?: boolean;
  xp?: number;
}

/** Agrège l'activité du jour (date locale de l'utilisateur) : base des séries, quêtes et statistiques. */
@Injectable()
export class ActivityService {
  constructor(private prisma: PrismaService, private clock: ClockService) {}

  async timezone(userId: string): Promise<string> {
    const p = await this.prisma.userPreferences.findUnique({ where: { userId }, select: { timezone: true } });
    return p?.timezone ?? 'Europe/Paris';
  }

  async todayKey(userId: string): Promise<string> {
    return localParts(this.clock.now(), await this.timezone(userId)).dateKey;
  }

  async record(userId: string, d: ActivityDelta) {
    const dateKey = await this.todayKey(userId);
    const key = { userId_dateKey: { userId, dateKey } };
    const current = await this.prisma.dailyActivity.upsert({ where: key, create: { userId, dateKey }, update: {} });
    let combo = current.currentCombo;
    if (d.answered) combo = d.correct ? combo + 1 : 0;
    const updated = await this.prisma.dailyActivity.update({
      where: key,
      data: {
        seconds: { increment: Math.round(d.seconds ?? 0) },
        total: { increment: d.answered ? 1 : 0 },
        correct: { increment: d.answered && d.correct ? 1 : 0 },
        reviews: { increment: d.review ? 1 : 0 },
        newItems: { increment: d.newItem ? 1 : 0 },
        kanjiReviews: { increment: d.kanjiReview ? 1 : 0 },
        listeningCorrect: { increment: d.listeningCorrect ? 1 : 0 },
        perfectLessons: { increment: d.perfectLesson ? 1 : 0 },
        xp: { increment: d.xp ?? 0 },
        currentCombo: combo,
        bestCombo: Math.max(current.bestCombo, combo),
      },
    });
    return this.claimQuests(userId, updated);
  }

  /**
   * Récompense chaque quête du jour une seule fois (XP + pièces). La revendication est atomique :
   * deux réponses simultanées ne peuvent pas toucher deux fois la même quête.
   */
  async claimQuests(userId: string, day: DailyActivity): Promise<QuestStatus[]> {
    const quests = dailyQuests(day.dateKey, day);
    const claimed: QuestStatus[] = [];
    for (const q of quests) {
      if (!q.done || day.questsClaimed.includes(q.id)) continue;
      const res = await this.prisma.dailyActivity.updateMany({
        where: { userId, dateKey: day.dateKey, NOT: { questsClaimed: { has: q.id } } },
        data: { questsClaimed: { push: q.id }, xp: { increment: q.xp } },
      });
      if (res.count === 0) continue;
      await this.addXp(userId, q.xp, 'quest', `${day.dateKey}:${q.id}`);
      await this.prisma.user.update({ where: { id: userId }, data: { coins: { increment: COINS.questCompleted } } });
      claimed.push(q);
    }
    return claimed;
  }

  /** Seul point d'attribution d'XP : toujours calculé côté serveur. */
  async addXp(userId: string, amount: number, reason: string, refId?: string) {
    if (amount <= 0) return;
    await this.prisma.$transaction([
      this.prisma.xpEvent.create({ data: { userId, amount, reason, refId } }),
      this.prisma.user.update({ where: { id: userId }, data: { xp: { increment: amount } } }),
    ]);
  }
}
