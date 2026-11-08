import { BadRequestException, ConflictException, ForbiddenException, Injectable, NotFoundException } from '@nestjs/common';
import { AuthoredExercise, BOSS_RULES, bossReward, createRng, planBossFight, simulateBoss } from '@koto/learning-engine';
import type { BossFightDto, BossOutcomeDto } from '@koto/shared';
import { PrismaService } from '../common/prisma.service';
import { ClockService } from '../common/clock.service';
import { ContentService, toEngineItem } from '../content/content.service';
import { LearningService } from '../learning/learning.service';
import { ActivityService } from '../learning/activity.service';

@Injectable()
export class BossService {
  constructor(
    private prisma: PrismaService,
    private clock: ClockService,
    private content: ContentService,
    private learning: LearningService,
    private activity: ActivityService,
  ) {}

  private async world(slug: string) {
    const world = await this.prisma.world.findUnique({
      where: { slug },
      include: { chapters: { include: { lessons: { include: { items: { include: { item: true } }, exercises: true } } } } },
    });
    if (!world || !world.bossName) throw new NotFoundException('Ce monde n’a pas de gardien.');
    return world;
  }

  /** Le gardien n'apparaît qu'une fois toutes les leçons du monde terminées. */
  private async assertAvailable(userId: string, world: Awaited<ReturnType<BossService['world']>>) {
    const lessonIds = world.chapters.flatMap((c) => c.lessons.map((l) => l.id));
    const done = await this.prisma.userLessonProgress.count({ where: { userId, lessonId: { in: lessonIds }, status: 'completed' } });
    if (lessonIds.length === 0 || done < lessonIds.length) throw new ForbiddenException('Termine toutes les leçons de ce monde pour affronter son gardien.');
  }

  async start(userId: string, slug: string): Promise<BossFightDto> {
    const world = await this.world(slug);
    await this.assertAvailable(userId, world);
    const lessons = world.chapters.flatMap((c) => c.lessons);
    const items = [...new Map(lessons.flatMap((l) => l.items.map((li) => [li.item.id, toEngineItem(li.item)]))).values()];
    const authored = lessons.flatMap((l) => l.exercises.map((e) => e.payload as unknown as AuthoredExercise));
    const pool = await this.content.worldPool(world.id, world.levelCode);
    const now = this.clock.now();
    const questions = planBossFight(items, authored, pool, createRng(`${userId}:${slug}:${now.getTime()}`));
    const session = await this.prisma.learningSession.create({ data: { userId, kind: 'boss', scope: slug } });
    await this.prisma.bossResult.upsert({
      where: { userId_worldSlug: { userId, worldSlug: slug } },
      create: { userId, worldSlug: slug, attempts: 1 },
      update: { attempts: { increment: 1 } },
    });
    return {
      sessionId: session.id,
      world: { slug: world.slug, title: world.title },
      boss: { name: world.bossName!, glyph: world.bossGlyph ?? '鬼', intro: world.bossIntro ?? '' },
      rules: { hp: BOSS_RULES.hp, hearts: BOSS_RULES.hearts },
      questions: await this.learning.issue(userId, session.id, 'boss', questions),
    };
  }

  /** Le résultat est recalculé par le serveur à partir des réponses enregistrées, dans l'ordre. */
  async finish(userId: string, slug: string, sessionId: string): Promise<BossOutcomeDto> {
    const session = await this.prisma.learningSession.findFirst({
      where: { id: sessionId, userId, kind: 'boss', scope: slug },
      include: { questions: { orderBy: { order: 'asc' } } },
    });
    if (!session) throw new NotFoundException('Combat introuvable.');
    if (session.endedAt) throw new ConflictException('Ce combat est déjà terminé.');
    const answered = session.questions.filter((q) => q.answeredAt).sort((a, b) => a.answeredAt!.getTime() - b.answeredAt!.getTime() || a.order - b.order);
    const progress = simulateBoss(answered.map((q) => !!q.correct));
    if (progress.state === 'ongoing') throw new BadRequestException('Le combat n’est pas terminé.');

    const won = progress.state === 'won';
    const previous = await this.prisma.bossResult.findUnique({ where: { userId_worldSlug: { userId, worldSlug: slug } } });
    const firstVictory = won && !previous?.firstVictoryAt;
    const reward = bossReward(won, firstVictory);
    const now = this.clock.now();
    await this.prisma.$transaction([
      this.prisma.learningSession.update({ where: { id: session.id }, data: { endedAt: now, xpEarned: { increment: reward.xp } } }),
      this.prisma.bossResult.upsert({
        where: { userId_worldSlug: { userId, worldSlug: slug } },
        create: { userId, worldSlug: slug, attempts: 1, victories: won ? 1 : 0, bestHits: progress.hits, firstVictoryAt: won ? now : null },
        update: {
          victories: { increment: won ? 1 : 0 },
          bestHits: Math.max(previous?.bestHits ?? 0, progress.hits),
          ...(firstVictory ? { firstVictoryAt: now } : {}),
        },
      }),
      this.prisma.user.update({ where: { id: userId }, data: { coins: { increment: reward.coins } } }),
    ]);
    await this.activity.addXp(userId, reward.xp, won ? 'boss_victory' : 'boss_attempt', session.id);
    await this.activity.record(userId, { xp: reward.xp });
    return { state: progress.state, hits: progress.hits, heartsLeft: progress.heartsLeft, firstVictory, xpGained: reward.xp, coinsGained: reward.coins };
  }
}
