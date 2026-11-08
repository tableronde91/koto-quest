import { BadRequestException, ConflictException, Injectable, NotFoundException } from '@nestjs/common';
import {
  AuthoredExercise,
  EXAMS,
  ExamDef,
  ExamSectionId,
  PLACEMENT_BLOCK,
  Question,
  createRng,
  examRecommendations,
  gradeExam,
  newCard,
  placementBlockPassed,
  planExam,
  planPlacementBlock,
  schedule,
  ExamBank,
  JLPT_SCALE,
  planBankExam,
} from '@koto/learning-engine';
import type { ExamResultDto, ExamStartDto, PlacementStepDto } from '@koto/shared';
import { readFileSync } from 'fs';
import { resolve } from 'path';
import { Prisma } from '@prisma/client';
import { PrismaService } from '../common/prisma.service';
import { ClockService } from '../common/clock.service';
import { ContentService, toEngineItem } from '../content/content.service';
import { LearningService } from '../learning/learning.service';
import { ActivityService } from '../learning/activity.service';
import { fromCardState } from '../learning/card-mapper';

/** Marge après la fin du temps imparti (latence, envoi automatique). */
const EXAM_GRACE_MS = 2 * 60_000;

@Injectable()
export class ExamService {
  constructor(
    private prisma: PrismaService,
    private clock: ClockService,
    private content: ContentService,
    private learning: LearningService,
    private activity: ActivityService,
  ) {}

  private def(slug: string): ExamDef {
    const def = EXAMS[slug];
    if (!def) throw new NotFoundException('Examen inconnu.');
    return def;
  }

  private async levelContent(levelCode: string) {
    const worlds = await this.prisma.world.findMany({
      where: { levelCode },
      orderBy: { order: 'asc' },
      include: { chapters: { orderBy: { order: 'asc' }, include: { lessons: { orderBy: { order: 'asc' }, include: { items: { include: { item: true } }, exercises: true } } } } },
    });
    return worlds.map((w) => {
      const lessons = w.chapters.flatMap((c) => c.lessons);
      return {
        world: w,
        lessons,
        items: [...new Map(lessons.flatMap((l) => l.items.map((li) => [li.item.id, toEngineItem(li.item)]))).values()],
        authored: lessons.flatMap((l) => l.exercises.map((e) => e.payload as unknown as AuthoredExercise)),
      };
    });
  }

  // ───────── Examen blanc ─────────

  /** Banques de questions rédigées au format officiel (content/exams). */
  private banks = new Map<string, ExamBank>();
  private bank(slug: string): ExamBank {
    if (!this.banks.has(slug)) this.banks.set(slug, JSON.parse(readFileSync(resolve(__dirname, `../../../../content/exams/${slug}.json`), 'utf8')) as ExamBank);
    return this.banks.get(slug)!;
  }

  async start(userId: string, slug: string): Promise<ExamStartDto> {
    const def = this.def(slug);
    const rng = createRng(`${userId}:${slug}:${this.clock.now().getTime()}`);
    let planned;
    if (def.bank) {
      planned = planBankExam(this.bank(def.bank), rng);
    } else {
      const worlds = await this.levelContent(def.level);
      const items = [...new Map(worlds.flatMap((w) => w.items.map((i) => [i.id, i]))).values()];
      const authored = worlds.flatMap((w) => w.authored);
      const pool = await this.content.enginePool(def.level);
      planned = planExam(def, items, authored, pool, rng);
    }
    const session = await this.prisma.learningSession.create({ data: { userId, kind: 'exam', scope: slug, startedAt: this.clock.now() } });
    const questions = planned.map((p) => Object.assign(p.question, { section: p.section }) as Question);
    return {
      sessionId: session.id,
      exam: { slug, title: def.title, durationMin: def.durationMin, sections: def.sections, passPercent: def.passPercent, sectionMinPercent: def.sectionMinPercent },
      questions: await this.learning.issue(userId, session.id, 'exam', questions),
    };
  }

  /** Correction de la copie entière, côté serveur. Les notions ratées repartent en révision. */
  async submit(userId: string, slug: string, sessionId: string, answers: Record<string, unknown>): Promise<ExamResultDto> {
    const def = this.def(slug);
    const session = await this.prisma.learningSession.findFirst({ where: { id: sessionId, userId, kind: 'exam', scope: slug }, include: { questions: { orderBy: { order: 'asc' } } } });
    if (!session) throw new NotFoundException('Examen introuvable.');
    if (session.endedAt) throw new ConflictException('Cette copie a déjà été rendue.');
    const now = this.clock.now();
    const late = now.getTime() - session.startedAt.getTime() > def.durationMin * 60_000 + EXAM_GRACE_MS;

    const qs = session.questions;
    const section = (q: (typeof qs)[number]) => (q.payload as { section?: ExamSectionId }).section ?? 'vocab';
    const grade = gradeExam(def, qs.map((q) => ({ section: section(q), type: q.type, answer: q.answer as string | string[] })), qs.map((q) => answers[q.id]));

    // Enregistre la copie
    await this.prisma.$transaction(qs.map((q, i) => this.prisma.issuedQuestion.update({ where: { id: q.id }, data: { answeredAt: now, correct: grade.results[i] } })));

    // Effet sur les révisions : une notion ratée repart en apprentissage ; une notion réussie déjà connue est consolidée.
    const seen = new Set<string>();
    for (const [i, q] of qs.entries()) {
      if (!q.itemId || seen.has(q.itemId)) continue;
      seen.add(q.itemId);
      const exists = await this.prisma.reviewCard.findUnique({ where: { userId_itemId: { userId, itemId: q.itemId } } });
      if (!exists && grade.results[i]) continue;
      await this.learning.updateCard(userId, q.itemId, session.id, 'exam', grade.results[i], 8000, q.guessable, now);
    }

    const previousPass = await this.prisma.examAttempt.findFirst({ where: { userId, passed: true, exam: { slug } } });
    const xp = grade.correct * 2 + (grade.passed && !previousPass ? 30 : 0);
    const coins = grade.passed && !previousPass ? 20 : 0;
    const exam = await this.prisma.exam.findUniqueOrThrow({ where: { slug } });
    const scores = { sections: grade.sections, correct: grade.correct, total: grade.total, late };
    await this.prisma.$transaction([
      this.prisma.learningSession.update({ where: { id: session.id }, data: { endedAt: now, total: grade.total, correct: grade.correct, xpEarned: xp } }),
      this.prisma.examAttempt.create({ data: { userId, examId: exam.id, startedAt: session.startedAt, finishedAt: now, sessionId: session.id, percent: grade.percent, passed: grade.passed, scores: scores as unknown as Prisma.InputJsonValue } }),
      this.prisma.user.update({ where: { id: userId }, data: { coins: { increment: coins } } }),
    ]);
    await this.activity.addXp(userId, xp, 'exam', session.id);
    await this.activity.record(userId, { xp, seconds: Math.min(def.durationMin * 60, (now.getTime() - session.startedAt.getTime()) / 1000) });

    const show = (v: unknown) => (v === undefined || v === null ? null : Array.isArray(v) ? v.join(' ') : String(v));
    return {
      percent: grade.percent,
      correct: grade.correct,
      total: grade.total,
      passed: grade.passed,
      late,
      sections: grade.sections,
      recommendations: examRecommendations(grade, def.level),
      mistakes: qs
        .map((q, i) => ({ q, i }))
        .filter(({ i }) => !grade.results[i])
        .map(({ q }) => {
          const p = q.payload as { prompt: string; display?: { jp?: string; text?: string }; audio?: string };
          return { section: section(q), prompt: p.prompt, jp: p.display?.jp ?? (q.type === 'listening_choice' ? p.audio ?? null : null), text: p.display?.text ?? null, given: show(answers[q.id]), correctAnswer: show(q.answer)!, explanation: q.explanation };
        }),
      xpGained: xp,
      coinsGained: coins,
      passPercent: def.passPercent,
      sectionMinPercent: def.sectionMinPercent,
      scaled: grade.scaled ? { ...grade.scaled, max: JLPT_SCALE } : null,
    };
  }

  // ───────── Test de positionnement ─────────

  private async placementWorlds(levelCode: string) {
    return (await this.levelContent(levelCode)).filter((w) => w.lessons.length > 0);
  }

  private async block(userId: string, sessionId: string, levelCode: string, index: number): Promise<PlacementStepDto> {
    const worlds = await this.placementWorlds(levelCode);
    const w = worlds[index];
    const pool = await this.content.worldPool(w.world.id, levelCode);
    const questions = planPlacementBlock(w.items, w.authored, pool, createRng(`${sessionId}:${index}`));
    return {
      done: false,
      lastPassed: null,
      block: { sessionId, world: { slug: w.world.slug, title: w.world.title, order: w.world.order }, index, totalWorlds: worlds.length, questions: await this.learning.issue(userId, sessionId, 'placement', questions, index * 10) },
    };
  }

  async placementStart(userId: string): Promise<PlacementStepDto> {
    const prefs = await this.prisma.userPreferences.findUnique({ where: { userId } });
    const level = prefs?.targetLevel ?? 'N5';
    const session = await this.prisma.learningSession.create({ data: { userId, kind: 'placement', scope: level, state: { index: 0, passed: [] } } });
    return this.block(userId, session.id, level, 0);
  }

  async placementAnswer(userId: string, sessionId: string, answers: Record<string, unknown>): Promise<PlacementStepDto> {
    const session = await this.prisma.learningSession.findFirst({ where: { id: sessionId, userId, kind: 'placement' } });
    if (!session) throw new NotFoundException('Test introuvable.');
    if (session.endedAt) throw new ConflictException('Ce test est déjà terminé.');
    const state = session.state as { index: number; passed: string[] };
    const level = session.scope ?? 'N5';
    const worlds = await this.placementWorlds(level);
    const current = worlds[state.index];
    const blockQs = await this.prisma.issuedQuestion.findMany({ where: { sessionId, userId, phase: 'placement', answeredAt: null, order: { gte: state.index * 10, lt: state.index * 10 + PLACEMENT_BLOCK + 1 } } });
    if (!blockQs.length) throw new BadRequestException('Aucune question en attente.');
    const now = this.clock.now();
    let correct = 0;
    for (const q of blockQs) {
      const ok = gradeExam({ ...EXAMS['n5-mock'], sections: [{ id: 'vocab', title: '', jpTitle: '', count: 1 }] }, [{ section: 'vocab', type: q.type, answer: q.answer as string | string[] }], [answers[q.id]]).correct === 1;
      if (ok) correct++;
      await this.prisma.issuedQuestion.update({ where: { id: q.id }, data: { answeredAt: now, correct: ok } });
    }
    const passed = placementBlockPassed(correct);
    const nextState = { index: state.index + 1, passed: passed ? [...state.passed, current.world.slug] : state.passed };
    if (passed && nextState.index < worlds.length) {
      await this.prisma.learningSession.update({ where: { id: sessionId }, data: { state: nextState } });
      const step = await this.block(userId, sessionId, level, nextState.index);
      return { ...step, lastPassed: true } as PlacementStepDto;
    }
    return this.placementFinish(userId, sessionId, worlds, nextState.passed, passed ? null : current.world);
  }

  /** Valide les mondes réussis : leçons terminées et notions mises en révision espacée (à vérifier dans quelques jours). */
  private async placementFinish(
    userId: string,
    sessionId: string,
    worlds: Awaited<ReturnType<ExamService['placementWorlds']>>,
    passedSlugs: string[],
    stoppedAt: { slug: string; title: string } | null,
  ): Promise<PlacementStepDto> {
    const now = this.clock.now();
    const validated = worlds.filter((w) => passedSlugs.includes(w.world.slug));
    for (const w of validated) {
      for (const l of w.lessons) {
        await this.prisma.userLessonProgress.upsert({
          where: { userId_lessonId: { userId, lessonId: l.id } },
          create: { userId, lessonId: l.id, status: 'completed', completedAt: now },
          update: { status: 'completed', completedAt: now },
        });
      }
      for (const it of w.items) {
        const exists = await this.prisma.reviewCard.findUnique({ where: { userId_itemId: { userId, itemId: it.id } } });
        if (exists) continue;
        await this.prisma.reviewCard.create({ data: { userId, itemId: it.id, ...fromCardState(schedule(newCard(now), 4, now)) } });
      }
    }
    await this.prisma.learningSession.update({ where: { id: sessionId }, data: { endedAt: now, state: { passed: passedSlugs } } });
    await this.prisma.userPreferences.update({ where: { userId }, data: { placementAt: now, placedWorlds: validated.length } });
    const next = await this.content.nextRecommendedLesson(userId, 'N5');
    return {
      done: true,
      validated: validated.map((w) => ({ slug: w.world.slug, title: w.world.title })),
      stoppedAt: stoppedAt ? { slug: stoppedAt.slug, title: stoppedAt.title } : null,
      nextLesson: next ? { slug: next.slug, title: next.title } : null,
    };
  }
}
