import { Injectable } from '@nestjs/common';
import {
  Mastery,
  MASTERED_STABILITY_DAYS,
  addDays,
  computeStreak,
  dailyQuests,
  estimateReadiness,
  levelFromXp,
  localParts,
  masteryOf,
  normalizeAvatar,
  AvatarConfig,
} from '@koto/learning-engine';
import type { DashboardDto, JlptCode, StatsDto } from '@koto/shared';
import { PrismaService } from '../common/prisma.service';
import { ClockService } from '../common/clock.service';
import { ContentService } from '../content/content.service';
import { LearningService } from '../learning/learning.service';
import { toCardState } from '../learning/card-mapper';

type Kind = 'kana' | 'vocabulary' | 'kanji' | 'grammar';

@Injectable()
export class DashboardService {
  constructor(
    private prisma: PrismaService,
    private clock: ClockService,
    private content: ContentService,
    private learning: LearningService,
  ) {}

  async dashboard(userId: string): Promise<DashboardDto> {
    const now = this.clock.now();
    const user = await this.prisma.user.findUniqueOrThrow({ where: { id: userId }, include: { preferences: true, notificationPrefs: true } });
    const tz = user.preferences?.timezone ?? 'Europe/Paris';
    const level = (user.preferences?.targetLevel ?? 'N5') as JlptCode;
    const todayKey = localParts(now, tz).dateKey;

    const [{ seq, status }, activity, cards, summary, next, levelItemCount] = await Promise.all([
      this.content.lessonStatuses(userId, level),
      this.prisma.dailyActivity.findMany({ where: { userId, dateKey: { gte: addDays(todayKey, -400) } } }),
      this.prisma.reviewCard.findMany({ where: { userId }, include: { item: { select: { kind: true, levelCode: true } } } }),
      this.learning.reviewSummary(userId),
      this.content.nextLessonAnyLevel(userId, level),
      this.prisma.learningItem.count({ where: { levelCode: level } }),
    ]);

    const completed = seq.filter((s) => status.get(s.lessonId) === 'completed').length;
    const today = activity.find((a) => a.dateKey === todayKey);
    const mastered = { words: 0, kanji: 0, kana: 0, grammar: 0 };
    for (const c of cards) {
      if (masteryOf(toCardState(c), now) !== 'mastered') continue;
      if (c.item.kind === 'vocabulary') mastered.words++;
      else mastered[c.item.kind as 'kanji' | 'kana' | 'grammar']++;
    }
    const lv = levelFromXp(user.xp);

    return {
      displayName: user.displayName,
      targetLevel: level,
      examDate: user.preferences?.examDate?.toISOString().slice(0, 10) ?? null,
      progress: { completedLessons: completed, totalLessons: seq.length, percent: seq.length ? Math.round((completed / seq.length) * 100) : 0 },
      xp: { total: user.xp, ...lv },
      coins: user.coins,
      avatar: normalizeAvatar(user.avatar as Partial<AvatarConfig> | null),
      streak: computeStreak(activity.filter((a) => a.total > 0).map((a) => a.dateKey), todayKey),
      today: { seconds: today?.seconds ?? 0, answers: today?.total ?? 0, accuracy: today?.total ? Math.round((today.correct / today.total) * 100) : null },
      mastered,
      reviews: { due: summary.due, learningSoon: summary.learningSoon },
      plan: summary.plan,
      nextLesson: next ? { slug: next.slug, title: next.title, worldTitle: next.worldTitle } : null,
      quests: dailyQuests(todayKey, {
        newItems: today?.newItems ?? 0,
        reviews: today?.reviews ?? 0,
        kanjiReviews: today?.kanjiReviews ?? 0,
        bestCombo: today?.bestCombo ?? 0,
        perfectLessons: today?.perfectLessons ?? 0,
        listeningCorrect: today?.listeningCorrect ?? 0,
      }),
      readiness: estimateReadiness(cards.filter((c) => c.item.levelCode === level).map(toCardState), levelItemCount, now),
      suggestPlacement: !user.preferences?.placementAt && completed === 0,
      notifications: { consent: !!user.notificationPrefs?.consent, enabled: !!user.notificationPrefs?.enabled },
    };
  }

  async stats(userId: string): Promise<StatsDto> {
    const now = this.clock.now();
    const prefs = await this.prisma.userPreferences.findUnique({ where: { userId } });
    const tz = prefs?.timezone ?? 'Europe/Paris';
    const todayKey = localParts(now, tz).dateKey;
    const from = addDays(todayKey, -29);
    const [activity, cards, history, lessonsCompleted, examAttempts] = await Promise.all([
      this.prisma.dailyActivity.findMany({ where: { userId } }),
      this.prisma.reviewCard.findMany({ where: { userId }, include: { item: true } }),
      this.prisma.reviewHistory.findMany({ where: { userId }, select: { cardId: true, stabilityAfter: true, reviewedAt: true }, orderBy: { reviewedAt: 'asc' } }),
      this.prisma.userLessonProgress.count({ where: { userId, status: 'completed' } }),
      this.prisma.examAttempt.findMany({ where: { userId, finishedAt: { not: null } }, orderBy: { finishedAt: 'asc' }, include: { exam: { select: { title: true } } } }),
    ]);
    const byDate = new Map(activity.map((a) => [a.dateKey, a]));

    const days = Array.from({ length: 30 }, (_, i) => {
      const date = addDays(from, i);
      const a = byDate.get(date);
      return { date, seconds: a?.seconds ?? 0, answers: a?.total ?? 0, correct: a?.correct ?? 0, xp: a?.xp ?? 0 };
    });

    // Semaines (lundi) sur 8 semaines
    const dow = (new Date(`${todayKey}T00:00:00Z`).getUTCDay() + 6) % 7;
    const thisMonday = addDays(todayKey, -dow);
    const weeks = Array.from({ length: 8 }, (_, i) => {
      const weekStart = addDays(thisMonday, -7 * (7 - i));
      let seconds = 0;
      for (let d = 0; d < 7; d++) seconds += byDate.get(addDays(weekStart, d))?.seconds ?? 0;
      return { weekStart, minutes: Math.round(seconds / 60) };
    });

    const totals = activity.reduce(
      (t, a) => ({ answers: t.answers + a.total, correct: t.correct + a.correct, reviews: t.reviews + a.reviews, seconds: t.seconds + a.seconds }),
      { answers: 0, correct: 0, reviews: 0, seconds: 0 },
    );

    const masteryDistribution: Record<Mastery, number> = { discovered: 0, learning: 0, fragile: 0, mastered: 0, urgent: 0 };
    const byKind: StatsDto['byKind'] = { kana: { learned: 0, mastered: 0 }, vocabulary: { learned: 0, mastered: 0 }, kanji: { learned: 0, mastered: 0 }, grammar: { learned: 0, mastered: 0 } };
    const items: StatsDto['items'] = [];
    for (const c of cards) {
      const m = masteryOf(toCardState(c), now);
      masteryDistribution[m]++;
      const k = c.item.kind as Kind;
      byKind[k].learned++;
      if (m === 'mastered') byKind[k].mastered++;
      items.push({ id: c.item.id, front: c.item.front, reading: c.item.reading, meaning: c.item.meaning, kind: c.item.kind, mastery: m, due: c.due.toISOString(), lapses: c.lapses });
    }
    const urgency: Record<Mastery, number> = { urgent: 0, fragile: 1, learning: 2, discovered: 3, mastered: 4 };
    items.sort((a, b) => urgency[a.mastery] - urgency[b.mastery] || a.due.localeCompare(b.due));

    // Croissance : notions découvertes et premières fois où une notion atteint le seuil de maîtrise.
    const learnedOn = new Map<string, number>();
    const masteredOn = new Map<string, number>();
    const seenMastered = new Set<string>();
    for (const c of cards) {
      const k = localParts(c.createdAt, tz).dateKey;
      learnedOn.set(k, (learnedOn.get(k) ?? 0) + 1);
    }
    for (const h of history) {
      if (h.stabilityAfter >= MASTERED_STABILITY_DAYS && !seenMastered.has(h.cardId)) {
        seenMastered.add(h.cardId);
        const k = localParts(h.reviewedAt, tz).dateKey;
        masteredOn.set(k, (masteredOn.get(k) ?? 0) + 1);
      }
    }
    let learned = [...learnedOn.entries()].filter(([k]) => k < from).reduce((s, [, v]) => s + v, 0);
    let masteredCum = [...masteredOn.entries()].filter(([k]) => k < from).reduce((s, [, v]) => s + v, 0);
    const growth = days.map(({ date }) => {
      learned += learnedOn.get(date) ?? 0;
      masteredCum += masteredOn.get(date) ?? 0;
      return { date, learned, mastered: masteredCum };
    });

    return {
      days,
      weeks,
      accuracy: totals.answers ? Math.round((totals.correct / totals.answers) * 100) : null,
      masteryDistribution,
      byKind,
      growth,
      totals: { answers: totals.answers, reviews: totals.reviews, lessonsCompleted, studySeconds: totals.seconds },
      items: items.slice(0, 300),
      exams: examAttempts.map((a) => ({
        date: a.finishedAt!.toISOString(),
        title: a.exam.title,
        percent: a.percent ?? 0,
        passed: !!a.passed,
        sections: ((a.scores as { sections?: { id: string; title: string; percent: number }[] } | null)?.sections ?? []).map((x) => ({ id: x.id, title: x.title, percent: x.percent })),
      })),
    };
  }
}
