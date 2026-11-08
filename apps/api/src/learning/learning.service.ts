import { BadRequestException, ConflictException, Injectable, NotFoundException } from '@nestjs/common';
import {
  AuthoredExercise,
  EngineItem,
  Question,
  QuestionType,
  authoredToQuestion,
  checkAnswer,
  chooseQuestionType,
  createRng,
  generateMatching,
  generateQuestion,
  masteryOf,
  newCard,
  orderReviewQueue,
  planDailyLoad,
  ratingFromAnswer,
  schedule,
  shuffle,
  toPublic,
  reshuffleForRetry,
  PublicQuestion,
  COINS,
  xpForAnswer,
  xpForLessonCompletion,
  DEFAULT_OPTIONS,
  TIMEOUT_ANSWER,
  bossAnswerTooLate,
  bossTimeLimitSec,
  exampleIndex,
} from '@koto/learning-engine';
import type { AnswerResultDto, IssuedQuestionDto, LessonCompletionDto, SessionDto } from '@koto/shared';
import { Prisma } from '@prisma/client';
import { PrismaService } from '../common/prisma.service';
import { ClockService } from '../common/clock.service';
import { ContentService, toEngineItem } from '../content/content.service';
import { ActivityService } from './activity.service';
import { fromCardState, toCardState } from './card-mapper';

type Phase = IssuedQuestionDto['phase'];
const MAX_REVIEWS_PER_SESSION = 20;
const MAX_RESPONSE_MS = 120_000;

@Injectable()
export class LearningService {
  constructor(
    private prisma: PrismaService,
    private clock: ClockService,
    private content: ContentService,
    private activity: ActivityService,
  ) {}

  // ─────────────── Émission des questions ───────────────

  async issue(userId: string, sessionId: string | null, phase: Phase, questions: Question[], startOrder = 0): Promise<IssuedQuestionDto[]> {
    const rows = await this.prisma.issuedQuestion.createManyAndReturn({
      data: questions.map((q, i) => ({
        userId,
        sessionId,
        itemId: q.itemId ?? null,
        type: q.type,
        phase,
        order: startOrder + i,
        payload: toPublic(q) as unknown as Prisma.InputJsonValue,
        answer: q.answer as Prisma.InputJsonValue,
        explanation: q.explanation,
        guessable: q.guessable,
      })),
    });
    return rows.sort((a, b) => a.order - b.order).map((r) => this.toDto(r));
  }

  private toDto(r: { id: string; phase: string; payload: Prisma.JsonValue; retryOf?: string | null }): IssuedQuestionDto {
    return { ...(r.payload as object), id: r.id, phase: r.phase as Phase, retryOf: r.retryOf ?? null } as IssuedQuestionDto;
  }

  /**
   * Reprise d'un exercice raté, à refaire en fin de séance. Idempotent : redemander la reprise
   * d'une même question renvoie la même copie. Au plus 2 reprises successives d'un même exercice.
   */
  async retry(userId: string, questionId: string): Promise<IssuedQuestionDto> {
    const q = await this.prisma.issuedQuestion.findFirst({ where: { id: questionId, userId } });
    if (!q) throw new NotFoundException('Question introuvable.');
    if (!q.answeredAt || q.correct !== false) throw new BadRequestException('Seul un exercice raté peut être repris.');
    if (['boss', 'quiz', 'game', 'exam', 'placement'].includes(q.phase)) throw new BadRequestException('Cet exercice ne peut pas être repris.');
    const existing = await this.prisma.issuedQuestion.findFirst({ where: { retryOf: q.id, userId } });
    if (existing) return this.toDto(existing);
    let depth = 0;
    for (let parent = q.retryOf; parent && depth < 5; depth++) {
      parent = (await this.prisma.issuedQuestion.findUnique({ where: { id: parent }, select: { retryOf: true } }))?.retryOf ?? null;
    }
    if (depth >= 2) throw new ConflictException('Cet exercice a déjà été repris deux fois : il reviendra dans tes révisions.');
    const payload = reshuffleForRetry(q.payload as unknown as PublicQuestion, q.answer as string | string[], createRng(`${q.id}:retry`));
    const copy = await this.prisma.issuedQuestion.create({
      data: {
        userId,
        sessionId: q.sessionId,
        itemId: q.itemId,
        type: q.type,
        phase: q.phase,
        order: q.order + 10_000,
        payload: payload as unknown as Prisma.InputJsonValue,
        answer: q.answer as Prisma.InputJsonValue,
        explanation: q.explanation,
        guessable: q.guessable,
        retryOf: q.id,
      },
    });
    return this.toDto(copy);
  }

  private async userRetention(userId: string) {
    const p = await this.prisma.userPreferences.findUnique({ where: { userId }, select: { desiredRetention: true } });
    return { ...DEFAULT_OPTIONS, desiredRetention: p?.desiredRetention ?? 0.9 };
  }

  // ─────────────── Leçons ───────────────

  async startLesson(userId: string, slug: string): Promise<SessionDto> {
    const lesson = await this.content.lessonBySlug(slug);
    const levelCode = lesson.chapter.world.levelCode;
    await this.content.assertUnlocked(userId, lesson.id, levelCode);
    const pool = await this.content.worldPool(lesson.chapter.worldId, levelCode);
    const items = lesson.items.map((li) => toEngineItem(li.item));
    const rng = createRng(`${userId}:${slug}:${this.clock.now().getTime()}`);

    // 1) Reconnaissance de chaque nouvelle notion
    const recognition = items.map((it) => generateQuestion(it, pool, 'meaning_choice', rng)).filter(Boolean) as Question[];
    // 2) Exercices rédigés (grammaire, phrases, dialogues)
    const authored = lesson.exercises.map((e) => authoredToQuestion(e.payload as unknown as AuthoredExercise, rng));
    // 3) Rappel actif / écoute sur chaque notion, dans un ordre mélangé.
    //    Les mots en kanji se lisent au format de l'examen (漢字読み, dans une phrase de la leçon).
    const examples = exampleIndex(items, lesson.examples.map((e) => e.jp));
    const recall = shuffle(items, rng)
      .map((it) => {
        // Mot en kanji : lecture au format JLPT ; kanji isolé : lecture classique.
        const readingType: QuestionType = it.kind === 'vocabulary' ? 'jlpt_reading' : 'reading_choice';
        const types = (['reverse_choice', 'listening_choice', readingType] as QuestionType[]).filter((t) =>
          it.kind === 'grammar' ? t === 'reverse_choice' : t !== readingType || (it.reading && it.reading !== it.front && (t === 'reading_choice' || /[一-龯々]/.test(it.front))),
        );
        const t = types[Math.floor(rng() * types.length)];
        return generateQuestion(it, pool, t, rng, examples.get(it.id)) ?? generateQuestion(it, pool, 'reverse_choice', rng);
      })
      .filter(Boolean) as Question[];
    // 4) Association de mots pour conclure
    const matching = items.filter((i) => i.kind !== 'grammar').length >= 3 ? generateMatching(items.filter((i) => i.kind !== 'grammar'), rng) : null;

    const questions = [...recognition, ...authored, ...recall, ...(matching ? [matching] : [])];
    const session = await this.prisma.learningSession.create({ data: { userId, kind: 'lesson', lessonId: lesson.id } });
    await this.prisma.userLessonProgress.upsert({
      where: { userId_lessonId: { userId, lessonId: lesson.id } },
      create: { userId, lessonId: lesson.id, status: 'in_progress', attempts: 1 },
      update: { attempts: { increment: 1 } },
    });
    return { sessionId: session.id, questions: await this.issue(userId, session.id, 'lesson', questions) };
  }

  async completeLesson(userId: string, slug: string, sessionId: string): Promise<LessonCompletionDto> {
    const session = await this.prisma.learningSession.findFirst({
      where: { id: sessionId, userId, kind: 'lesson' },
      include: { lesson: true, questions: true },
    });
    if (!session || session.lesson?.slug !== slug) throw new NotFoundException('Session de leçon introuvable.');
    if (session.endedAt) throw new ConflictException('Cette leçon a déjà été validée.');
    // Le score porte sur le premier essai ; les reprises servent à retravailler, pas à se rattraper.
    const lessonQuestions = session.questions.filter((q) => q.phase === 'lesson' && !q.retryOf);
    if (lessonQuestions.some((q) => !q.answeredAt)) throw new BadRequestException('Réponds à toutes les questions avant de valider la leçon.');

    const correct = lessonQuestions.filter((q) => q.correct).length;
    const total = lessonQuestions.length;
    const errors = total - correct;
    const score = total ? Math.round((correct / total) * 100) : 100;
    const lessonId = session.lessonId!;
    const previous = await this.prisma.userLessonProgress.findUnique({ where: { userId_lessonId: { userId, lessonId } } });
    const firstCompletion = previous?.status !== 'completed';

    // Récompense calculée par le serveur ; une leçon rejouée rapporte peu (pas de « farm »).
    const xp = firstCompletion ? xpForLessonCompletion(errors) : 5;
    await this.prisma.userLessonProgress.update({
      where: { userId_lessonId: { userId, lessonId } },
      data: { status: 'completed', completedAt: previous?.completedAt ?? this.clock.now(), bestScore: Math.max(previous?.bestScore ?? 0, score) },
    });
    await this.activity.addXp(userId, xp, 'lesson_complete', lessonId);
    // Pièces : seulement à la première validation (pas de « farm » en rejouant la leçon).
    const coins = firstCompletion ? COINS.lessonFirstCompletion + (errors === 0 ? COINS.perfectLessonBonus : 0) : 0;
    if (coins) await this.prisma.user.update({ where: { id: userId }, data: { coins: { increment: coins } } });
    await this.activity.record(userId, { xp, perfectLesson: errors === 0 });

    // Mini-révision : d'abord les notions ratées, puis d'autres notions de la leçon, sous une autre forme.
    const lesson = await this.content.lessonBySlug(slug);
    const pool = await this.content.worldPool(lesson.chapter.worldId, lesson.chapter.world.levelCode);
    const items = lesson.items.map((li) => toEngineItem(li.item));
    const missed = new Set(lessonQuestions.filter((q) => !q.correct && q.itemId).map((q) => q.itemId!));
    const rng = createRng(`${sessionId}:mini`);
    const ordered = [...items.filter((i) => missed.has(i.id)), ...shuffle(items.filter((i) => !missed.has(i.id)), rng)];
    const mini = ordered
      .slice(0, 4)
      .map((it) => generateQuestion(it, pool, it.kind === 'grammar' ? 'reverse_choice' : rng() < 0.5 ? 'true_false' : 'reverse_choice', rng))
      .filter(Boolean) as Question[];
    const miniReview = await this.issue(userId, sessionId, 'mini_review', mini, 1000);

    await this.prisma.learningSession.update({ where: { id: sessionId }, data: { endedAt: this.clock.now(), xpEarned: { increment: xp } } });
    const next = await this.content.nextLessonAnyLevel(userId, lesson.chapter.world.levelCode);
    return { score, correct, total, xpGained: xp, coinsGained: coins, perfect: errors === 0, miniReview, nextLessonSlug: next?.slug ?? null };
  }

  // ─────────────── Correction ───────────────

  async getQuestion(userId: string, id: string) {
    const q = await this.prisma.issuedQuestion.findFirst({ where: { id, userId } });
    if (!q) throw new NotFoundException('Question introuvable.');
    return {
      question: this.toDto(q),
      answered: !!q.answeredAt,
      result: q.answeredAt ? { correct: !!q.correct, correctAnswer: q.answer as string | string[], explanation: q.explanation } : null,
    };
  }

  /** Combat de gardien : la question vient d'être affichée, le chrono démarre (une seule fois). */
  async shown(userId: string, questionId: string) {
    const q = await this.prisma.issuedQuestion.findFirst({ where: { id: questionId, userId }, select: { id: true, phase: true, type: true } });
    if (!q) throw new NotFoundException('Question introuvable.');
    if (q.phase !== 'boss') return { timeLimitSec: null };
    await this.prisma.issuedQuestion.updateMany({ where: { id: q.id, shownAt: null, answeredAt: null }, data: { shownAt: this.clock.now() } });
    return { timeLimitSec: bossTimeLimitSec(q.type as QuestionType) };
  }

  async answer(userId: string, questionId: string, given: unknown, responseMsRaw: number): Promise<AnswerResultDto> {
    // Le filtre sur userId garantit l'isolation des comptes : une question d'un autre utilisateur est « introuvable ».
    const q = await this.prisma.issuedQuestion.findFirst({ where: { id: questionId, userId } });
    if (!q) throw new NotFoundException('Question introuvable.');
    if (q.phase === 'exam' || q.phase === 'placement') throw new BadRequestException('Cette question se corrige avec la copie entière.');
    const now = this.clock.now();
    const responseMs = Math.max(0, Math.min(MAX_RESPONSE_MS, Math.round(responseMsRaw || 0)));
    let correct = checkAnswer({ type: q.type as QuestionType, answer: q.answer as string | string[] }, given);
    // Combat de gardien : chrono contrôlé côté serveur. Départ = affichage déclaré, sinon la réponse précédente
    // (ou le début du combat) : ne pas déclarer l'affichage ne donne donc aucun temps supplémentaire.
    let timedOut = false;
    if (q.phase === 'boss') {
      let start = q.shownAt;
      if (!start) {
        const prev = await this.prisma.issuedQuestion.findFirst({ where: { sessionId: q.sessionId, userId, answeredAt: { not: null } }, orderBy: { answeredAt: 'desc' }, select: { answeredAt: true } });
        const session = q.sessionId ? await this.prisma.learningSession.findUnique({ where: { id: q.sessionId }, select: { startedAt: true } }) : null;
        start = prev?.answeredAt ?? session?.startedAt ?? q.createdAt;
      }
      timedOut = given === TIMEOUT_ANSWER || bossAnswerTooLate(q.type as QuestionType, start, now);
      if (timedOut) correct = false;
    }

    // Verrou optimiste : une question ne peut être corrigée qu'une seule fois.
    const locked = await this.prisma.issuedQuestion.updateMany({ where: { id: q.id, answeredAt: null }, data: { answeredAt: now, correct } });
    if (locked.count === 0) throw new ConflictException('Cette question a déjà reçu une réponse.');
    await this.prisma.exerciseAnswer.create({
      data: { questionId: q.id, userId, given: (given ?? null) as Prisma.InputJsonValue, correct, responseMs },
    });

    let mastery: AnswerResultDto['mastery'] = null;
    let nextReviewAt: string | null = null;
    let createdCard = false;
    let itemKind: string | null = null;
    // Mini-jeux : simple entraînement, la planification des révisions n'est pas modifiée.
    const isGame = q.phase === 'game';
    if (q.itemId && !isGame) {
      const r = await this.updateCard(userId, q.itemId, q.sessionId, q.phase, correct, responseMs, q.guessable, now);
      mastery = r.mastery;
      nextReviewAt = r.due.toISOString();
      createdCard = r.created;
      itemKind = r.kind;
    }

    const ctx = q.phase === 'lesson' || q.phase === 'boss' ? 'lesson' : q.phase === 'quiz' ? 'quiz' : 'review';
    const xp = isGame ? 0 : xpForAnswer(correct, ctx);
    await this.activity.addXp(userId, xp, `answer_${q.phase}`, q.id);
    const isReview = q.phase !== 'lesson';
    const quests = await this.activity.record(userId, {
      seconds: Math.min(responseMs, 60_000) / 1000,
      answered: true,
      correct,
      review: isReview,
      newItem: createdCard,
      kanjiReview: isReview && itemKind === 'kanji',
      listeningCorrect: correct && q.type === 'listening_choice',
      xp,
    });
    if (q.sessionId) {
      await this.prisma.learningSession.update({
        where: { id: q.sessionId },
        data: { total: { increment: 1 }, correct: { increment: correct ? 1 : 0 }, xpEarned: { increment: xp } },
      });
    }
    await this.prisma.notification.updateMany({ where: { questionId: q.id, userId }, data: { status: 'answered' } });

    return { correct, correctAnswer: q.answer as string | string[], explanation: q.explanation, xpGained: xp, mastery, nextReviewAt, questsCompleted: quests.map((x) => ({ title: x.title, xp: x.xp })),
      timedOut,
    };
  }

  /**
   * Met à jour la carte FSRS. Dans une même session (leçon + mini-révision), seule la
   * première réponse planifie la carte ; une erreur ultérieure la fait revenir plus vite.
   * Cela évite qu'une notion vue 3 fois en 5 minutes soit considérée comme acquise.
   */
  async updateCard(userId: string, itemId: string, sessionId: string | null, phase: string, correct: boolean, responseMs: number, guessable: boolean, now: Date) {
    const item = await this.prisma.learningItem.findUniqueOrThrow({ where: { id: itemId }, select: { kind: true } });
    const existing = await this.prisma.reviewCard.findUnique({ where: { userId_itemId: { userId, itemId } } });
    const card = existing ? toCardState(existing) : newCard(now);
    let apply = true;
    if (existing && sessionId) {
      const inSession = await this.prisma.reviewHistory.findMany({ where: { cardId: existing.id, sessionId }, select: { rating: true } });
      if (inSession.length > 0) apply = !correct && !inSession.some((h) => h.rating === 1);
    }
    if (!apply) return { mastery: masteryOf(card, now), due: card.due, created: false, kind: item.kind };

    const rating = ratingFromAnswer({ correct, responseMs, reps: card.reps, guessable });
    const next = schedule(card, rating, now, await this.userRetention(userId));
    const saved = await this.prisma.reviewCard.upsert({
      where: { userId_itemId: { userId, itemId } },
      create: { userId, itemId, ...fromCardState(next) },
      update: fromCardState(next),
    });
    await this.prisma.reviewHistory.create({
      data: {
        cardId: saved.id,
        userId,
        sessionId,
        rating,
        stateBefore: card.state,
        stabilityAfter: next.stability,
        difficultyAfter: next.difficulty,
        dueAfter: next.due,
        responseMs,
        context: phase,
      },
    });
    return { mastery: masteryOf(next, now), due: next.due, created: !existing, kind: item.kind };
  }

  // ─────────────── Révisions ───────────────

  async dueCards(userId: string) {
    const now = this.clock.now();
    const cards = await this.prisma.reviewCard.findMany({ where: { userId, due: { lte: now }, state: { not: 'new' } }, include: { item: true } });
    return orderReviewQueue(cards.map((c) => ({ row: c, card: toCardState(c) })), now);
  }

  async reviewSummary(userId: string) {
    const now = this.clock.now();
    const prefs = await this.prisma.userPreferences.findUnique({ where: { userId } });
    const levelCode = prefs?.targetLevel ?? 'N5';
    const [due, soon, learnedCount, totalItems] = await Promise.all([
      this.prisma.reviewCard.count({ where: { userId, due: { lte: now } } }),
      this.prisma.reviewCard.count({ where: { userId, due: { gt: now, lte: new Date(now.getTime() + 3600_000) } } }),
      this.prisma.reviewCard.count({ where: { userId, item: { levelCode } } }),
      this.prisma.learningItem.count({ where: { levelCode } }),
    ]);
    const today = await this.prisma.dailyActivity.findUnique({ where: { userId_dateKey: { userId, dateKey: await this.activity.todayKey(userId) } } });
    const plan = planDailyLoad({
      minutesPerDay: prefs?.minutesPerDay ?? 15,
      dueCount: due + (today?.reviews ?? 0),
      newItemsAvailable: Math.max(0, totalItems - learnedCount) + (today?.newItems ?? 0),
      reviewsDoneToday: today?.reviews ?? 0,
      newItemsDoneToday: today?.newItems ?? 0,
    });
    return { due, learningSoon: soon, plan };
  }

  async startReviewSession(userId: string): Promise<SessionDto> {
    const queue = (await this.dueCards(userId)).slice(0, MAX_REVIEWS_PER_SESSION);
    if (queue.length === 0) return { sessionId: '', questions: [] };
    const rng = createRng(`${userId}:review:${this.clock.now().getTime()}`);
    const pools = new Map<string, EngineItem[]>();
    const examples = new Map<string, Map<string, string>>();
    const questions: Question[] = [];
    for (const { row, card } of queue) {
      if (!pools.has(row.item.levelCode)) pools.set(row.item.levelCode, await this.content.enginePool(row.item.levelCode));
      if (!examples.has(row.item.levelCode)) examples.set(row.item.levelCode, await this.content.examples(row.item.levelCode));
      const q = this.questionForItem(toEngineItem(row.item), pools.get(row.item.levelCode)!, card.reps, rng, examples.get(row.item.levelCode)!.get(row.item.id));
      if (q) questions.push(q);
    }
    const session = await this.prisma.learningSession.create({ data: { userId, kind: 'review' } });
    return { sessionId: session.id, questions: await this.issue(userId, session.id, 'review', questions) };
  }

  private questionForItem(item: EngineItem, pool: EngineItem[], reps: number, rng: () => number, example?: string): Question | null {
    return generateQuestion(item, pool, chooseQuestionType(item, reps, rng), rng, example) ?? generateQuestion(item, pool, 'meaning_choice', rng);
  }

  /** Question unique pour un mini-défi (notification ou popup). Renvoie null si rien n'est pertinent. */
  async issueQuiz(userId: string, opts: { allowNotDue?: boolean } = {}): Promise<IssuedQuestionDto | null> {
    let [first] = await this.dueCards(userId);
    if (!first && opts.allowNotDue) {
      // Demande explicite de l'utilisateur : on prend la notion dont la révision est la plus proche.
      const soonest = await this.prisma.reviewCard.findFirst({ where: { userId, state: { not: 'new' } }, orderBy: { due: 'asc' }, include: { item: true } });
      if (soonest) first = { row: soonest, card: toCardState(soonest) };
    }
    if (!first) return null;
    const pool = await this.content.enginePool(first.row.item.levelCode);
    const example = (await this.content.examples(first.row.item.levelCode)).get(first.row.item.id);
    const q = this.questionForItem(toEngineItem(first.row.item), pool, first.card.reps, createRng(`${userId}:quiz:${this.clock.now().getTime()}`), example);
    if (!q) return null;
    const [dto] = await this.issue(userId, null, 'quiz', [q]);
    return dto;
  }
}
