/**
 * Mode « hors ligne » : réimplémente l'API Koto Quest directement dans le navigateur.
 * Aucune base de données ni serveur : l'état est stocké dans le localStorage,
 * le contenu N5 est embarqué, et la logique pédagogique vient du même moteur
 * (@koto/learning-engine) que la version serveur.
 */
import { localDuels, type LocalDuelState } from './duel';
import { locale } from '../i18n';
import {
  AuthoredExercise,
  CardState,
  DEFAULT_OPTIONS,
  EngineItem,
  ItemKind,
  MASTERED_STABILITY_DAYS,
  Mastery,
  Question,
  QuestionType,
  ReminderMode,
  ReminderPrefs,
  addDays,
  authoredToQuestion,
  checkAnswer,
  chooseQuestionType,
  masteryScore,
  planCharacterPractice,
  focusedPool,
  COINS,
  ACQUIRE_ERRORS_FR,
  AvatarConfig,
  CosmeticCatalog,
  checkAcquire,
  normalizeAvatar,
  ownedSkus,
  validateAvatar,
  DAILY_GAME_COIN_CAP,
  GAMES,
  GAME_IDS,
  GameDef,
  GameId,
  eligibleItems,
  gameReward,
  planTimedGame,
  scoreTimedGame,
  EXAMS,
  ExamSectionId,
  examRecommendations,
  gradeExam,
  placementBlockPassed,
  planExam,
  planPlacementBlock,
  BOSS_RULES,
  JLPT_DRILLS,
  JlptDrillPart,
  planJlptDrill,
  exampleIndex,
  ExamBank,
  JLPT_SCALE,
  planBankExam,
  TIMEOUT_ANSWER,
  bossAnswerTooLate,
  bossTimeLimitSec,
  bossReward,
  planBossFight,
  simulateBoss,
  computeStreak,
  createRng,
  dailyQuests,
  decideReminder,
  estimateReadiness,
  generateMatching,
  generateQuestion,
  hashSeed,
  levelFromXp,
  localParts,
  masteryOf,
  newCard,
  orderReviewQueue,
  planDailyLoad,
  ratingFromAnswer,
  reminderMessage,
  reminderSlots,
  schedule,
  shuffle,
  toPublic,
  reshuffleForRetry,
  PublicQuestion,
  xpForAnswer,
  xpForLessonCompletion,
  ACHIEVEMENT_COINS,
  AchievementDef,
  AchievementStats,
  achievementProgress,
  achievementReward,
  longestStreak,
  newlyUnlocked,
} from '@koto/learning-engine';
import type {
  JlptDrillsDto,
  AchievementCheckDto,
  AchievementDto,
  AchievementsDto,
  AnswerResultDto,
  CharacterDto,
  CharactersDto,
  ExpressionDto,
  ExpressionRegister,
  ExpressionsDto,
  BossFightDto,
  BossOutcomeDto,
  ShopDto,
  GameInfoDto,
  GameResultDto,
  GameStartDto,
  GamesDto,
  ExamResultDto,
  ExamStartDto,
  PlacementStepDto,
  DashboardDto,
  InboxItemDto,
  IssuedQuestionDto,
  JlptCode,
  LessonCompletionDto,
  LessonDto,
  LessonStatus,
  MeDto,
  NotificationPrefsDto,
  PathDto,
  SessionDto,
  StatsDto,
} from '@koto/shared';
import content from '../../../../content/n5/n5.json';
import contentN4 from '../../../../content/n4/n4.json';
import charactersContent from '../../../../content/characters/characters.json';
import expressionsContent from '../../../../content/expressions/expressions.json';
import cosmeticsCatalog from '../../../../content/cosmetics/catalog.json';
import bankN5 from '../../../../content/exams/n5-jlpt.json';

/** Banques de questions au format officiel (examens blancs). */
const BANKS: Record<string, ExamBank> = { 'n5-jlpt': bankN5 as unknown as ExamBank };

const CATALOG = cosmeticsCatalog as unknown as CosmeticCatalog;

// ───────────────────────── Contenu embarqué ─────────────────────────

interface ItemJson { slug: string; kind: ItemKind; front: string; reading?: string; romaji?: string; meaning: string; kanji?: { onyomi: string[]; kunyomi: string[]; strokes?: number } }
interface LessonJson { slug: string; title: string; objective: string; minutes: number; explanation: string[]; items: ItemJson[]; examples: { jp: string; reading?: string; fr: string }[]; exercises: AuthoredExercise[] }
interface LessonEntry extends LessonJson { level: JlptCode; worldOrder: number; worldSlug: string; worldTitle: string; chapterSlug: string; chapterTitle: string }

type WorldJson = { slug: string; title: string; region: string; description: string; boss?: { name: string; glyph: string; intro: string }; exam?: string; chapters: { slug: string; title: string; lessons: LessonJson[] }[] };
/** Niveaux embarqués, du plus facile au plus difficile. */
const LEVELS = [content, contentN4].map((c) => ({
  code: c.level.code as JlptCode,
  title: c.level.title,
  region: c.level.region,
  notice: (c as { notice?: string }).notice ?? null,
  worlds: (c.worlds as unknown as WorldJson[]).map((w, i) => ({ ...w, order: i + 1, level: c.level.code as JlptCode })),
}));
const WORLDS = LEVELS.flatMap((l) => l.worlds);
const LESSONS: LessonEntry[] = WORLDS.flatMap((w) => w.chapters.flatMap((c) => c.lessons.map((l) => ({ ...l, level: w.level, worldOrder: w.order, worldSlug: w.slug, worldTitle: w.title, chapterSlug: c.slug, chapterTitle: c.title }))));
const lessonsOf = (code: string) => LESSONS.filter((l) => l.level === code);
/** Contenu N5 (examen blanc et test de positionnement). */
const N5_WORLDS = WORLDS.filter((w) => w.level === 'N5');
const ITEMS = new Map<string, ItemJson>();
LESSONS.forEach((l) => l.items.forEach((it) => ITEMS.set(it.slug, it)));
// Onglet Caractères : mêmes slugs que le parcours, donc maîtrise partagée.
const CHARACTERS = charactersContent as unknown as { notice?: string; sections: { slug: 'hiragana' | 'katakana' | 'kanji'; title: string; description: string; groups: { slug: string; title: string; items: ItemJson[] }[] }[] };
CHARACTERS.sections.forEach((s) => s.groups.forEach((g) => g.items.forEach((it) => ITEMS.set(it.slug, it))));
type ExpressionJson = ItemJson & { note: string; register: ExpressionRegister; example?: { jp: string; fr: string } };
const EXPRESSIONS = expressionsContent as unknown as { notice?: string; themes: { slug: string; glyph: string; title: string; description: string; expressions: ExpressionJson[] }[] };
EXPRESSIONS.themes.forEach((t) => t.expressions.forEach((it) => ITEMS.set(it.slug, it)));
const POOL: EngineItem[] = [...ITEMS.values()].map(toEngine);
/** Distracteurs centrés sur le monde de la leçon (voir focusedPool). */
const WORLD_POOL = new Map(WORLDS.map((w) => [w.slug, focusedPool([...new Map(w.chapters.flatMap((c) => c.lessons.flatMap((l) => l.items.map((it) => [it.slug, toEngine(it)] as const)))).values()], POOL)]));
const poolFor = (worldSlug: string) => WORLD_POOL.get(worldSlug) ?? POOL;
/** Phrase d'exemple des leçons pour chaque mot en kanji (questions au format JLPT). */
const EXAMPLES = exampleIndex(POOL, LESSONS.flatMap((l) => l.examples.map((e) => e.jp)));

function toEngine(it: ItemJson): EngineItem {
  return { id: it.slug, kind: it.kind, front: it.front, reading: it.reading ?? null, romaji: it.romaji ?? null, meaning: it.meaning };
}

// ───────────────────────── État persistant ─────────────────────────

interface StoredCard { state: CardState['state']; stability: number; difficulty: number; due: string; lastReview: string | null; reps: number; lapses: number; step: number; createdAt: string }
interface StoredQuestion { id: string; sessionId: string | null; itemId: string | null; type: QuestionType; phase: IssuedQuestionDto['phase']; order: number; payload: object; answer: string | string[]; explanation: string; guessable: boolean; correct: boolean | null; answeredAt: string | null; createdAt: string; retryOf?: string | null; shownAt?: string | null }
interface Daily { seconds: number; total: number; correct: number; reviews: number; kanjiReviews: number; newItems: number; currentCombo: number; bestCombo: number; perfectLessons: number; listeningCorrect: number; xp: number; questsClaimed?: string[]; gameCoins?: number }
interface State {
  version: 1;
  user: { displayName: string; xp: number; onboardedAt: string | null; createdAt: string };
  prefs: Omit<MeDto['preferences'], 'locale'> & { desiredRetention: number };
  notif: { consent: boolean; enabled: boolean; mode: ReminderMode; customTimes: number[]; windowStart: number; windowEnd: number; quietStart: number | null; quietEnd: number | null; pausedUntil: string | null; lastSlotKey: string | null };
  cards: Record<string, StoredCard>;
  history: { itemId: string; sessionId: string | null; rating: number; stabilityAfter: number; reviewedAt: string }[];
  progress: Record<string, { status: 'in_progress' | 'completed'; attempts: number; bestScore: number; completedAt: string | null }>;
  sessions: Record<string, { kind: 'lesson' | 'review' | 'boss' | 'game' | 'exam' | 'placement'; lessonSlug: string | null; endedAt: string | null; createdAt: string; scope?: string; state?: { index: number; passed: string[] } }>;
  bosses: Record<string, { attempts: number; victories: number; bestHits: number; firstVictoryAt: string | null }>;
  coins: number;
  avatar: Partial<AvatarConfig> | null;
  inventory: string[];
  games: Record<string, { plays: number; bestScore: number; lastScore: number }>;
  exams: { slug: string; title: string; date: string; percent: number; passed: boolean; sections: { id: string; title: string; percent: number }[] }[];
  placementAt: string | null;
  /** Succès débloqués : slug → date */
  achievements: Record<string, string>;
  /** Duels contre des adversaires simulés */
  duel?: LocalDuelState;
  questions: Record<string, StoredQuestion>;
  notifications: { id: string; title: string; body: string; questionId: string; status: 'pending' | 'opened' | 'answered' | 'expired'; createdAt: string; expiresAt: string }[];
  daily: Record<string, Daily>;
  lastActivityAt: string | null;
}

const KEY = 'koto-quest-local-v1';

function fresh(): State {
  return {
    version: 1,
    user: { displayName: locale === 'en' ? 'Apprentice' : 'Apprenti·e', xp: 0, onboardedAt: null, createdAt: new Date().toISOString() },
    prefs: { selfLevel: 'beginner', targetLevel: 'N5', examDate: null, minutesPerDay: 15, difficultAreas: [], timezone: Intl.DateTimeFormat().resolvedOptions().timeZone || 'Europe/Paris', showFurigana: true, theme: 'system', reducedMotion: false, desiredRetention: 0.9 },
    notif: { consent: false, enabled: false, mode: 'normal', customTimes: [], windowStart: 540, windowEnd: 1260, quietStart: 1320, quietEnd: 480, pausedUntil: null, lastSlotKey: null },
    cards: {}, history: [], progress: {}, sessions: {}, questions: {}, notifications: [], daily: {}, lastActivityAt: null, bosses: {}, coins: 0, avatar: null, inventory: [], games: {}, exams: [], placementAt: null, achievements: {},
  };
}

let cache: State | null = null;
function load(): State {
  if (cache) return cache;
  try {
    const raw = localStorage.getItem(KEY);
    cache = raw ? { ...fresh(), ...JSON.parse(raw) } : fresh();
  } catch {
    cache = fresh();
  }
  return cache!;
}
function save() {
  const s = load();
  // Garde la sauvegarde compacte : on oublie les questions anciennes déjà traitées.
  const cutoff = Date.now() - 3 * 86_400_000;
  for (const [id, q] of Object.entries(s.questions)) if (Date.parse(q.createdAt) < cutoff) delete s.questions[id];
  for (const [id, se] of Object.entries(s.sessions)) if (Date.parse(se.createdAt) < cutoff) delete s.sessions[id];
  s.notifications = s.notifications.filter((n) => Date.parse(n.createdAt) >= cutoff);
  if (s.history.length > 20_000) s.history = s.history.slice(-20_000);
  try {
    localStorage.setItem(KEY, JSON.stringify(s));
  } catch {
    throw new HttpError(507, 'Le stockage du navigateur est plein : exporte ta sauvegarde puis réinitialise.');
  }
}

export class HttpError extends Error {
  constructor(public status: number, message: string) {
    super(message);
  }
}

const uid = () => `${Date.now().toString(36)}-${Math.random().toString(36).slice(2, 10)}-${Math.random().toString(36).slice(2, 10)}`;
const now = () => new Date();
const toCard = (c: StoredCard): CardState => ({ state: c.state, stability: c.stability, difficulty: c.difficulty, due: new Date(c.due), lastReview: c.lastReview ? new Date(c.lastReview) : null, reps: c.reps, lapses: c.lapses, step: c.step });
const fromCard = (c: CardState, createdAt: string): StoredCard => ({ state: c.state, stability: c.stability, difficulty: c.difficulty, due: c.due.toISOString(), lastReview: c.lastReview?.toISOString() ?? null, reps: c.reps, lapses: c.lapses, step: c.step, createdAt });
const todayKey = () => localParts(now(), load().prefs.timezone).dateKey;

function daily(key = todayKey()): Daily {
  const s = load();
  return (s.daily[key] ??= { seconds: 0, total: 0, correct: 0, reviews: 0, kanjiReviews: 0, newItems: 0, currentCombo: 0, bestCombo: 0, perfectLessons: 0, listeningCorrect: 0, xp: 0 });
}
function addXp(n: number) {
  load().user.xp += n;
  daily().xp += n;
}

// ───────────────────────── Parcours ─────────────────────────

/** Seul le N5 commence par les kana : les autres niveaux s'ouvrent au premier monde. */
const startWorld = (code: string = 'N5') => (code === 'N5' && ['kana', 'basics', 'n5', 'n4plus'].includes(load().prefs.selfLevel) ? 3 : 1);

/** Déblocage séquentiel, niveau par niveau. */
function statuses(): Map<string, LessonStatus> {
  const s = load();
  const out = new Map<string, LessonStatus>();
  for (const lvl of LEVELS) {
    const seq = lessonsOf(lvl.code);
    const start = startWorld(lvl.code);
    let startIdx = seq.findIndex((l) => l.worldOrder >= start);
    if (startIdx < 0) startIdx = 0;
    seq.forEach((l, i) => {
      const p = s.progress[l.slug]?.status;
      if (p) out.set(l.slug, p);
      else if (i <= startIdx || s.progress[seq[i - 1]?.slug]?.status === 'completed') out.set(l.slug, 'available');
      else out.set(l.slug, 'locked');
    });
  }
  return out;
}

/** Prochaine leçon : niveau visé d'abord, puis les niveaux suivants (N5 → N4…), puis les plus faciles. */
function nextLesson(preferred: string = load().prefs.targetLevel) {
  const st = statuses();
  const idx = Math.max(0, LEVELS.findIndex((l) => l.code === preferred));
  const order = [...LEVELS.slice(idx), ...LEVELS.slice(0, idx).reverse()];
  for (const lvl of order) {
    const seq = lessonsOf(lvl.code);
    const start = startWorld(lvl.code);
    const ordered = [...seq.filter((l) => l.worldOrder >= start), ...seq.filter((l) => l.worldOrder < start)];
    const found = ordered.find((l) => ['available', 'in_progress'].includes(st.get(l.slug)!));
    if (found) return found;
  }
  return null;
}

function lessonOrThrow(slug: string) {
  const l = LESSONS.find((x) => x.slug === slug);
  if (!l) throw new HttpError(404, 'Leçon introuvable.');
  if (statuses().get(slug) === 'locked') throw new HttpError(403, 'Cette leçon est encore verrouillée : termine d’abord la précédente.');
  return l;
}

function path(code: string): PathDto {
  const lvl = LEVELS.find((l) => l.code === code);
  if (!lvl) throw new HttpError(404, `Le niveau ${code} n’est pas encore disponible.`);
  const st = statuses();
  const start = startWorld(code);
  return {
    level: { code: lvl.code, title: lvl.title, region: lvl.region, notice: lvl.notice },
    levels: LEVELS.map((l) => ({ code: l.code, title: l.title, lessons: lessonsOf(l.code).length, completed: lessonsOf(l.code).filter((x) => st.get(x.slug) === 'completed').length })),
    worlds: lvl.worlds.map((w) => {
      const lessons = w.chapters.flatMap((c) => c.lessons);
      return {
        slug: w.slug, order: w.order, title: w.title, description: w.description,
        comingSoon: lessons.length === 0 && !w.exam, optional: w.order < start,
        progress: { completed: lessons.filter((l) => st.get(l.slug) === 'completed').length, total: lessons.length },
        exam: w.exam
          ? (() => {
              const att = (load().exams ?? []).filter((e) => e.slug === w.exam);
              return { slug: w.exam, title: EXAMS[w.exam]?.title ?? 'Examen blanc', attempts: att.length, bestPercent: att.length ? Math.max(...att.map((a) => a.percent)) : null, passed: att.some((a) => a.passed) };
            })()
          : null,
        boss: w.boss
          ? {
              ...w.boss,
              available: lessons.length > 0 && lessons.every((l) => st.get(l.slug) === 'completed'),
              defeated: !!load().bosses[w.slug]?.firstVictoryAt,
              attempts: load().bosses[w.slug]?.attempts ?? 0,
            }
          : null,
        chapters: w.chapters.map((c) => ({
          slug: c.slug, title: c.title,
          lessons: c.lessons.map((l) => ({ slug: l.slug, title: l.title, objective: l.objective, minutes: l.minutes, status: st.get(l.slug) ?? 'locked', itemCount: l.items.length })),
        })),
      };
    }),
  };
}

function lessonDto(slug: string): LessonDto {
  const l = lessonOrThrow(slug);
  const s = load();
  const t = now();
  return {
    slug: l.slug, title: l.title, objective: l.objective, minutes: l.minutes, explanation: l.explanation,
    status: statuses().get(slug)!,
    world: { slug: l.worldSlug, title: l.worldTitle },
    chapter: { slug: l.chapterSlug, title: l.chapterTitle },
    examples: l.examples.map((e) => ({ jp: e.jp, reading: e.reading ?? null, fr: e.fr })),
    items: l.items.map((it) => ({
      id: it.slug, kind: it.kind, front: it.front, reading: it.reading ?? null, romaji: it.romaji ?? null, meaning: it.meaning,
      kanji: it.kanji ? { onyomi: it.kanji.onyomi, kunyomi: it.kanji.kunyomi, strokes: it.kanji.strokes ?? null } : null,
      mastery: s.cards[it.slug] ? masteryOf(toCard(s.cards[it.slug]), t) : null,
    })),
  };
}

// ───────────────────────── Questions ─────────────────────────

function issue(sessionId: string | null, phase: StoredQuestion['phase'], qs: Question[], startOrder = 0): IssuedQuestionDto[] {
  const s = load();
  const created = now().toISOString();
  return qs.map((q, i) => {
    const id = uid();
    const payload = toPublic(q);
    s.questions[id] = { id, sessionId, itemId: q.itemId ?? null, type: q.type, phase, order: startOrder + i, payload, answer: q.answer, explanation: q.explanation, guessable: q.guessable, correct: null, answeredAt: null, createdAt: created };
    return { ...payload, id, phase } as IssuedQuestionDto;
  });
}

const toDto = (q: StoredQuestion) => ({ ...q.payload, id: q.id, phase: q.phase, retryOf: q.retryOf ?? null }) as IssuedQuestionDto;

/** Exercice raté repris en fin de séance (même logique que l'API). */
function retry(id: string): IssuedQuestionDto {
  const s = load();
  const q = s.questions[id];
  if (!q) throw new HttpError(404, 'Question introuvable.');
  if (!q.answeredAt || q.correct !== false) throw new HttpError(400, 'Seul un exercice raté peut être repris.');
  if (['boss', 'quiz', 'game', 'exam', 'placement'].includes(q.phase)) throw new HttpError(400, 'Cet exercice ne peut pas être repris.');
  const existing = Object.values(s.questions).find((x) => x.retryOf === id);
  if (existing) return toDto(existing);
  let depth = 0;
  for (let parent = q.retryOf; parent && depth < 5; depth++) parent = s.questions[parent]?.retryOf ?? null;
  if (depth >= 2) throw new HttpError(409, 'Cet exercice a déjà été repris deux fois : il reviendra dans tes révisions.');
  const copy: StoredQuestion = {
    ...q,
    id: uid(),
    order: q.order + 10_000,
    payload: reshuffleForRetry(q.payload as PublicQuestion, q.answer, createRng(`${q.id}:retry`)),
    correct: null,
    answeredAt: null,
    createdAt: now().toISOString(),
    retryOf: q.id,
  };
  s.questions[copy.id] = copy;
  save();
  return toDto(copy);
}

function startLesson(slug: string): SessionDto {
  const l = lessonOrThrow(slug);
  const items = l.items.map(toEngine);
  const rng = createRng(`${slug}:${Date.now()}`);
  const pool = poolFor(l.worldSlug);
  const recognition = items.map((it) => generateQuestion(it, pool, 'meaning_choice', rng)).filter(Boolean) as Question[];
  const authored = l.exercises.map((e) => authoredToQuestion(e, rng));
  // Les mots en kanji se lisent au format de l'examen (漢字読み, dans une phrase de la leçon).
  const examples = exampleIndex(items, l.examples.map((e) => e.jp));
  const recall = shuffle(items, rng)
    .map((it) => {
      // Mot en kanji : lecture au format JLPT ; kanji isolé : lecture classique.
      const readingType: QuestionType = it.kind === 'vocabulary' ? 'jlpt_reading' : 'reading_choice';
      const types = (['reverse_choice', 'listening_choice', readingType] as QuestionType[]).filter((t) =>
        it.kind === 'grammar' ? t === 'reverse_choice' : t !== readingType || (it.reading && it.reading !== it.front && (t === 'reading_choice' || /[一-龯々]/.test(it.front))),
      );
      return generateQuestion(it, pool, types[Math.floor(rng() * types.length)], rng, examples.get(it.id)) ?? generateQuestion(it, pool, 'reverse_choice', rng);
    })
    .filter(Boolean) as Question[];
  const vocab = items.filter((i) => i.kind !== 'grammar');
  const matching = vocab.length >= 3 ? generateMatching(vocab, rng) : null;

  const s = load();
  const sessionId = uid();
  s.sessions[sessionId] = { kind: 'lesson', lessonSlug: slug, endedAt: null, createdAt: now().toISOString() };
  const p = (s.progress[slug] ??= { status: 'in_progress', attempts: 0, bestScore: 0, completedAt: null });
  p.attempts++;
  const questions = issue(sessionId, 'lesson', [...recognition, ...authored, ...recall, ...(matching ? [matching] : [])]);
  save();
  return { sessionId, questions };
}

function completeLesson(slug: string, sessionId: string): LessonCompletionDto {
  const s = load();
  const se = s.sessions[sessionId];
  if (!se || se.lessonSlug !== slug) throw new HttpError(404, 'Session de leçon introuvable.');
  if (se.endedAt) throw new HttpError(409, 'Cette leçon a déjà été validée.');
  const qs = Object.values(s.questions).filter((q) => q.sessionId === sessionId && q.phase === 'lesson' && !q.retryOf);
  if (qs.some((q) => !q.answeredAt)) throw new HttpError(400, 'Réponds à toutes les questions avant de valider la leçon.');
  const correct = qs.filter((q) => q.correct).length;
  const total = qs.length;
  const errors = total - correct;
  const score = total ? Math.round((correct / total) * 100) : 100;
  const p = s.progress[slug];
  const first = p.status !== 'completed';
  const xp = first ? xpForLessonCompletion(errors) : 5;
  p.status = 'completed';
  p.completedAt ??= now().toISOString();
  p.bestScore = Math.max(p.bestScore, score);
  addXp(xp);
  if (errors === 0) daily().perfectLessons++;
  // Pièces : seulement à la première validation.
  const lessonCoins = first ? COINS.lessonFirstCompletion + (errors === 0 ? COINS.perfectLessonBonus : 0) : 0;
  s.coins = (s.coins ?? 0) + lessonCoins;
  claimQuests();

  const l = LESSONS.find((x) => x.slug === slug)!;
  const items = l.items.map(toEngine);
  const missed = new Set(qs.filter((q) => !q.correct && q.itemId).map((q) => q.itemId!));
  const rng = createRng(`${sessionId}:mini`);
  const ordered = [...items.filter((i) => missed.has(i.id)), ...shuffle(items.filter((i) => !missed.has(i.id)), rng)];
  const mini = ordered
    .slice(0, 4)
    .map((it) => generateQuestion(it, poolFor(l.worldSlug), it.kind === 'grammar' ? 'reverse_choice' : rng() < 0.5 ? 'true_false' : 'reverse_choice', rng))
    .filter(Boolean) as Question[];
  const miniReview = issue(sessionId, 'mini_review', mini, 1000);
  se.endedAt = now().toISOString();
  save();
  return { score, correct, total, xpGained: xp, coinsGained: lessonCoins, perfect: errors === 0, miniReview, nextLessonSlug: nextLesson(l.level)?.slug ?? null };
}

function getQuestion(id: string) {
  const q = load().questions[id];
  if (!q) throw new HttpError(404, 'Ce défi a expiré ou n’existe plus.');
  return { question: toDto(q), answered: !!q.answeredAt, result: q.answeredAt ? { correct: !!q.correct, correctAnswer: q.answer, explanation: q.explanation } : null };
}

function answer(id: string, given: unknown, responseMsRaw: number): AnswerResultDto {
  const s = load();
  const q = s.questions[id];
  if (!q) throw new HttpError(404, 'Question introuvable.');
  if (q.phase === 'exam' || q.phase === 'placement') throw new HttpError(400, 'Cette question se corrige avec la copie entière.');
  if (q.answeredAt) throw new HttpError(409, 'Cette question a déjà reçu une réponse.');
  const t = now();
  const responseMs = Math.max(0, Math.min(120_000, Math.round(responseMsRaw || 0)));
  let correct = checkAnswer({ type: q.type, answer: q.answer }, given);
  // Combat de gardien : chrono (départ = affichage, sinon réponse précédente ou début du combat).
  let timedOut = false;
  if (q.phase === 'boss') {
    const prev = Object.values(s.questions).filter((x) => x.sessionId === q.sessionId && x.answeredAt).map((x) => x.answeredAt!).sort().pop();
    const start = q.shownAt ?? prev ?? (q.sessionId ? s.sessions[q.sessionId]?.createdAt : null) ?? q.createdAt;
    timedOut = given === TIMEOUT_ANSWER || bossAnswerTooLate(q.type, new Date(start), t);
    if (timedOut) correct = false;
  }
  q.correct = correct;
  q.answeredAt = t.toISOString();
  s.lastActivityAt = t.toISOString();

  let mastery: Mastery | null = null;
  let nextReviewAt: string | null = null;
  let created = false;
  let kind: ItemKind | null = null;
  // Mini-jeux : entraînement uniquement, pas de replanification des révisions.
  const isGame = q.phase === 'game';
  if (q.itemId && ITEMS.has(q.itemId) && !isGame) {
    kind = ITEMS.get(q.itemId)!.kind;
    const existing = s.cards[q.itemId];
    const card = existing ? toCard(existing) : newCard(t);
    let apply = true;
    if (existing && q.sessionId) {
      const inSession = s.history.filter((h) => h.itemId === q.itemId && h.sessionId === q.sessionId);
      if (inSession.length > 0) apply = !correct && !inSession.some((h) => h.rating === 1);
    }
    if (apply) {
      const rating = ratingFromAnswer({ correct, responseMs, reps: card.reps, guessable: q.guessable });
      const next = schedule(card, rating, t, { ...DEFAULT_OPTIONS, desiredRetention: s.prefs.desiredRetention });
      s.cards[q.itemId] = fromCard(next, existing?.createdAt ?? t.toISOString());
      s.history.push({ itemId: q.itemId, sessionId: q.sessionId, rating, stabilityAfter: next.stability, reviewedAt: t.toISOString() });
      created = !existing;
      mastery = masteryOf(next, t);
      nextReviewAt = next.due.toISOString();
    } else {
      mastery = masteryOf(card, t);
      nextReviewAt = card.due.toISOString();
    }
  }

  const xp = isGame ? 0 : xpForAnswer(correct, q.phase === 'lesson' || q.phase === 'boss' ? 'lesson' : q.phase === 'quiz' ? 'quiz' : 'review');
  addXp(xp);
  const d = daily();
  const isReview = q.phase !== 'lesson';
  d.seconds += Math.round(Math.min(responseMs, 60_000) / 1000);
  d.total++;
  if (correct) d.correct++;
  if (isReview) d.reviews++;
  if (created) d.newItems++;
  if (isReview && kind === 'kanji') d.kanjiReviews++;
  if (correct && q.type === 'listening_choice') d.listeningCorrect++;
  d.currentCombo = correct ? d.currentCombo + 1 : 0;
  d.bestCombo = Math.max(d.bestCombo, d.currentCombo);
  const questsCompleted = claimQuests().map((x) => ({ title: x.title, xp: x.xp }));
  s.notifications.forEach((n) => n.questionId === id && (n.status = 'answered'));
  save();
  return { correct, correctAnswer: q.answer, explanation: q.explanation, xpGained: xp, mastery, nextReviewAt, questsCompleted, timedOut };
}

// ───────────────────────── Révisions ─────────────────────────

function dueEntries() {
  const s = load();
  const t = now();
  return orderReviewQueue(
    Object.entries(s.cards).filter(([id]) => ITEMS.has(id)).map(([id, c]) => ({ id, card: toCard(c) })),
    t,
  );
}

function reviewSummary() {
  const s = load();
  const t = now().getTime();
  const due = dueEntries().length;
  const learningSoon = Object.values(s.cards).filter((c) => Date.parse(c.due) > t && Date.parse(c.due) <= t + 3600_000).length;
  const d = daily();
  const plan = planDailyLoad({
    minutesPerDay: s.prefs.minutesPerDay,
    dueCount: due + d.reviews,
    newItemsAvailable: Math.max(0, ITEMS.size - Object.keys(s.cards).length) + d.newItems,
    reviewsDoneToday: d.reviews,
    newItemsDoneToday: d.newItems,
  });
  return { due, learningSoon, plan };
}

function questionFor(id: string, reps: number, rng: () => number) {
  const item = toEngine(ITEMS.get(id)!);
  return generateQuestion(item, POOL, chooseQuestionType(item, reps, rng), rng, EXAMPLES.get(id)) ?? generateQuestion(item, POOL, 'meaning_choice', rng);
}

function reviewSession(): SessionDto {
  const queue = dueEntries().slice(0, 20);
  if (!queue.length) return { sessionId: '', questions: [] };
  const rng = createRng(`review:${Date.now()}`);
  const qs = queue.map((e) => questionFor(e.id, e.card.reps, rng)).filter(Boolean) as Question[];
  const sessionId = uid();
  load().sessions[sessionId] = { kind: 'review', lessonSlug: null, endedAt: null, createdAt: now().toISOString() };
  const questions = issue(sessionId, 'review', qs);
  save();
  return { sessionId, questions };
}

function issueQuiz(allowNotDue: boolean): IssuedQuestionDto | null {
  const s = load();
  let target = dueEntries()[0];
  if (!target && allowNotDue) {
    const soonest = Object.entries(s.cards).filter(([id]) => ITEMS.has(id)).sort((a, b) => a[1].due.localeCompare(b[1].due))[0];
    if (soonest) target = { id: soonest[0], card: toCard(soonest[1]) };
  }
  if (!target) return null;
  const q = questionFor(target.id, target.card.reps, createRng(`quiz:${Date.now()}`));
  return q ? issue(null, 'quiz', [q])[0] : null;
}

// ───────────────────────── Rappels (dans l'onglet ouvert) ─────────────────────────

function enginePrefs(): ReminderPrefs {
  const { notif, prefs } = load();
  return { ...notif, pausedUntil: notif.pausedUntil ? new Date(notif.pausedUntil) : null, timezone: prefs.timezone };
}

function notifPrefs(): NotificationPrefsDto {
  const n = load().notif;
  return { consent: n.consent, enabled: n.enabled, mode: n.mode, customTimes: n.customTimes, windowStart: n.windowStart, windowEnd: n.windowEnd, quietStart: n.quietStart, quietEnd: n.quietEnd, pausedUntil: n.pausedUntil, slots: reminderSlots(enginePrefs()), pushSubscribed: false, vapidPublicKey: null };
}

function updateNotifPrefs(body: Partial<NotificationPrefsDto>) {
  const n = load().notif;
  const consent = body.consent ?? n.consent;
  if (body.enabled && !consent) throw new HttpError(400, 'Active d’abord ton consentement aux rappels.');
  Object.assign(n, body, { consent, enabled: consent ? (body.enabled ?? n.enabled) : false });
  save();
  return notifPrefs();
}

function createChallenge(allowNotDue = false) {
  const q = issueQuiz(allowNotDue);
  if (!q) return null;
  const t = now();
  const notif = { id: uid(), title: 'Koto Quest', body: reminderMessage(hashSeed(q.id)), questionId: q.id, status: 'pending' as const, createdAt: t.toISOString(), expiresAt: new Date(t.getTime() + 12 * 3600_000).toISOString() };
  load().notifications.push(notif);
  save();
  return { notificationId: notif.id, questionId: q.id, pushed: false, title: notif.title, body: notif.body };
}

/** Appelé chaque minute tant que l'application est ouverte. Renvoie le défi créé, le cas échéant. */
export function tickReminders() {
  const s = load();
  if (!s.user.onboardedAt) return null;
  const decision = decideReminder({
    now: now(),
    prefs: enginePrefs(),
    relevantItems: dueEntries().length,
    lastSlotKey: s.notif.lastSlotKey,
    lastActivityAt: s.lastActivityAt ? new Date(s.lastActivityAt) : null,
  });
  if (decision.slotKey && decision.slotKey !== s.notif.lastSlotKey) {
    s.notif.lastSlotKey = decision.slotKey;
    save();
  }
  // Pas d'empilement : un seul défi en attente à la fois.
  if (!decision.send || inbox().length > 0) return null;
  return createChallenge();
}

function inbox(): InboxItemDto[] {
  const s = load();
  const t = Date.now();
  s.notifications.forEach((n) => n.status === 'pending' && Date.parse(n.expiresAt) <= t && (n.status = 'expired'));
  return s.notifications.filter((n) => n.status === 'pending').reverse().slice(0, 5).map((n) => ({ id: n.id, title: n.title, body: n.body, questionId: n.questionId, createdAt: n.createdAt }));
}

// ───────────────────────── Compte, tableau de bord, statistiques ─────────────────────────

function me(): MeDto {
  const s = load();
  const { desiredRetention: _r, ...prefs } = s.prefs;
  const preferences = { ...prefs, locale };
  return { id: 'local', email: 'local', displayName: s.user.displayName, onboarded: !!s.user.onboardedAt, xp: s.user.xp, coins: s.coins ?? 0, avatar: normalizeAvatar(s.avatar), preferences };
}

function onboarding(b: Record<string, unknown>) {
  const s = load();
  Object.assign(s.prefs, {
    selfLevel: b.selfLevel, targetLevel: b.targetLevel, examDate: (b.examDate as string) || null,
    minutesPerDay: b.minutesPerDay, difficultAreas: b.difficultAreas,
    ...(typeof b.timezone === 'string' ? { timezone: b.timezone } : {}),
  });
  if (b.reminderMode && b.reminderMode !== 'off') s.notif.mode = b.reminderMode as ReminderMode;
  s.user.onboardedAt = now().toISOString();
  save();
  return me();
}

function updatePrefs(b: Record<string, unknown>) {
  const s = load();
  const { displayName, locale: _locale, ...rest } = b;
  if (typeof displayName === 'string' && displayName.trim()) s.user.displayName = displayName.trim().slice(0, 40);
  Object.assign(s.prefs, rest);
  save();
  return me();
}

function dashboard(): DashboardDto {
  const s = load();
  const t = now();
  const st = statuses();
  const targetLessons = lessonsOf(s.prefs.targetLevel).length ? lessonsOf(s.prefs.targetLevel) : lessonsOf('N5');
  const completed = targetLessons.filter((l) => st.get(l.slug) === 'completed').length;
  const key = todayKey();
  const today = s.daily[key];
  const mastered = { words: 0, kanji: 0, kana: 0, grammar: 0 };
  for (const [id, c] of Object.entries(s.cards)) {
    const it = ITEMS.get(id);
    if (!it || masteryOf(toCard(c), t) !== 'mastered') continue;
    if (it.kind === 'vocabulary') mastered.words++;
    else mastered[it.kind]++;
  }
  const summary = reviewSummary();
  const nl = nextLesson();
  return {
    displayName: s.user.displayName,
    targetLevel: s.prefs.targetLevel,
    examDate: s.prefs.examDate,
    progress: { completedLessons: completed, totalLessons: targetLessons.length, percent: Math.round((completed / targetLessons.length) * 100) },
    xp: { total: s.user.xp, ...levelFromXp(s.user.xp) },
    coins: s.coins ?? 0,
    avatar: normalizeAvatar(s.avatar),
    streak: computeStreak(Object.entries(s.daily).filter(([, d]) => d.total > 0).map(([k]) => k), key),
    today: { seconds: today?.seconds ?? 0, answers: today?.total ?? 0, accuracy: today?.total ? Math.round((today.correct / today.total) * 100) : null },
    mastered,
    reviews: { due: summary.due, learningSoon: summary.learningSoon },
    plan: summary.plan,
    nextLesson: nl ? { slug: nl.slug, title: nl.title, worldTitle: nl.worldTitle } : null,
    quests: dailyQuests(key, { newItems: today?.newItems ?? 0, reviews: today?.reviews ?? 0, kanjiReviews: today?.kanjiReviews ?? 0, bestCombo: today?.bestCombo ?? 0, perfectLessons: today?.perfectLessons ?? 0, listeningCorrect: today?.listeningCorrect ?? 0 }),
    readiness: estimateReadiness(Object.values(s.cards).map(toCard), ITEMS.size, t),
    suggestPlacement: !s.placementAt && completed === 0,
    notifications: { consent: s.notif.consent, enabled: s.notif.enabled },
  };
}

function stats(): StatsDto {
  const s = load();
  const t = now();
  const tz = s.prefs.timezone;
  const key = todayKey();
  const from = addDays(key, -29);
  const days = Array.from({ length: 30 }, (_, i) => {
    const date = addDays(from, i);
    const a = s.daily[date];
    return { date, seconds: a?.seconds ?? 0, answers: a?.total ?? 0, correct: a?.correct ?? 0, xp: a?.xp ?? 0 };
  });
  const dow = (new Date(`${key}T00:00:00Z`).getUTCDay() + 6) % 7;
  const monday = addDays(key, -dow);
  const weeks = Array.from({ length: 8 }, (_, i) => {
    const weekStart = addDays(monday, -7 * (7 - i));
    let sec = 0;
    for (let d = 0; d < 7; d++) sec += s.daily[addDays(weekStart, d)]?.seconds ?? 0;
    return { weekStart, minutes: Math.round(sec / 60) };
  });
  const totals = Object.values(s.daily).reduce((a, d) => ({ answers: a.answers + d.total, correct: a.correct + d.correct, reviews: a.reviews + d.reviews, seconds: a.seconds + d.seconds }), { answers: 0, correct: 0, reviews: 0, seconds: 0 });
  const masteryDistribution: Record<Mastery, number> = { discovered: 0, learning: 0, fragile: 0, mastered: 0, urgent: 0 };
  const byKind: StatsDto['byKind'] = { kana: { learned: 0, mastered: 0 }, vocabulary: { learned: 0, mastered: 0 }, kanji: { learned: 0, mastered: 0 }, grammar: { learned: 0, mastered: 0 } };
  const items: StatsDto['items'] = [];
  for (const [id, c] of Object.entries(s.cards)) {
    const it = ITEMS.get(id);
    if (!it) continue;
    const m = masteryOf(toCard(c), t);
    masteryDistribution[m]++;
    byKind[it.kind].learned++;
    if (m === 'mastered') byKind[it.kind].mastered++;
    items.push({ id, front: it.front, reading: it.reading ?? null, meaning: it.meaning, kind: it.kind, mastery: m, due: c.due, lapses: c.lapses });
  }
  const urgency: Record<Mastery, number> = { urgent: 0, fragile: 1, learning: 2, discovered: 3, mastered: 4 };
  items.sort((a, b) => urgency[a.mastery] - urgency[b.mastery] || a.due.localeCompare(b.due));

  const learnedOn = new Map<string, number>();
  const masteredOn = new Map<string, number>();
  const seen = new Set<string>();
  Object.values(s.cards).forEach((c) => {
    const k = localParts(new Date(c.createdAt), tz).dateKey;
    learnedOn.set(k, (learnedOn.get(k) ?? 0) + 1);
  });
  s.history.forEach((h) => {
    if (h.stabilityAfter >= MASTERED_STABILITY_DAYS && !seen.has(h.itemId)) {
      seen.add(h.itemId);
      const k = localParts(new Date(h.reviewedAt), tz).dateKey;
      masteredOn.set(k, (masteredOn.get(k) ?? 0) + 1);
    }
  });
  let learned = [...learnedOn].filter(([k]) => k < from).reduce((n, [, v]) => n + v, 0);
  let mast = [...masteredOn].filter(([k]) => k < from).reduce((n, [, v]) => n + v, 0);
  const growth = days.map(({ date }) => {
    learned += learnedOn.get(date) ?? 0;
    mast += masteredOn.get(date) ?? 0;
    return { date, learned, mastered: mast };
  });
  return {
    days, weeks, growth, masteryDistribution, byKind, items,
    accuracy: totals.answers ? Math.round((totals.correct / totals.answers) * 100) : null,
    exams: (s.exams ?? []).map(({ slug: _slug, ...e }) => e),
    totals: { answers: totals.answers, reviews: totals.reviews, lessonsCompleted: Object.values(s.progress).filter((p) => p.status === 'completed').length, studySeconds: totals.seconds },
  };
}

/** Sauvegarde : export / import / réinitialisation. */
export function exportBackup(): string {
  return JSON.stringify({ format: 'koto-quest-local/1', exportedAt: new Date().toISOString(), data: load() }, null, 2);
}
export function importBackup(text: string) {
  const parsed = JSON.parse(text);
  if (parsed?.format !== 'koto-quest-local/1' || !parsed.data?.user) throw new Error('Ce fichier n’est pas une sauvegarde Koto Quest.');
  cache = { ...fresh(), ...parsed.data };
  save();
}
export function resetAll() {
  cache = fresh();
  save();
}

// ───────────────────────── Caractères ─────────────────────────

function characters(): CharactersDto {
  const s = load();
  const t = now();
  return {
    notice: CHARACTERS.notice ?? null,
    sections: CHARACTERS.sections.map((sec) => {
      let learned = 0, mastered = 0, due = 0, total = 0;
      const groups = sec.groups.map((g) => ({
        slug: g.slug,
        title: g.title,
        items: g.items.map((it): CharacterDto => {
          const stored = s.cards[it.slug];
          const card = stored ? toCard(stored) : null;
          const m = card ? masteryOf(card, t) : null;
          total++;
          if (card) learned++;
          if (m === 'mastered') mastered++;
          if (card && card.state !== 'new' && card.due <= t) due++;
          return {
            id: it.slug, kind: it.kind as 'kana' | 'kanji', front: it.front, reading: it.reading ?? null, romaji: it.romaji ?? null, meaning: it.meaning,
            kanji: it.kanji ? { onyomi: it.kanji.onyomi, kunyomi: it.kanji.kunyomi, strokes: it.kanji.strokes ?? null } : null,
            mastery: m, score: card ? masteryScore(card, t) : 0,
          };
        }),
      }));
      return { slug: sec.slug, title: sec.title, description: sec.description, learned, mastered, due, total, groups };
    }),
  };
}

function characterPractice(scope: string): SessionDto {
  const section = CHARACTERS.sections.find((x) => x.slug === scope || x.groups.some((g) => g.slug === scope));
  if (!section) throw new HttpError(404, 'Ensemble de caractères inconnu.');
  const groups = section.slug === scope ? section.groups : section.groups.filter((g) => g.slug === scope);
  const s = load();
  const pool = section.groups.flatMap((g) => g.items.map(toEngine));
  const entries = groups.flatMap((g) => g.items.map((it) => ({ item: toEngine(it), card: s.cards[it.slug] ? toCard(s.cards[it.slug]) : null })));
  const plan = planCharacterPractice(entries, pool, now(), createRng(`${scope}:${Date.now()}`));
  if (!plan.questions.length) return { sessionId: '', questions: [] };
  const sessionId = uid();
  s.sessions[sessionId] = { kind: 'review', lessonSlug: null, endedAt: null, createdAt: now().toISOString() };
  const questions = issue(sessionId, 'practice', plan.questions);
  save();
  return { sessionId, questions };
}

// ───────────────────────── Expressions ─────────────────────────

function expressions(): ExpressionsDto {
  const s = load();
  const t = now();
  return {
    notice: EXPRESSIONS.notice ?? null,
    themes: EXPRESSIONS.themes.map((th) => {
      let learned = 0, mastered = 0, due = 0, total = 0;
      const list = th.expressions.map((it): ExpressionDto => {
        const stored = s.cards[it.slug];
        const card = stored ? toCard(stored) : null;
        const m = card ? masteryOf(card, t) : null;
        total++;
        if (card) learned++;
        if (m === 'mastered') mastered++;
        if (card && card.state !== 'new' && card.due <= t) due++;
        return { id: it.slug, front: it.front, reading: it.reading ?? null, romaji: it.romaji ?? null, meaning: it.meaning, note: it.note, register: it.register, example: it.example ?? null, mastery: m, score: card ? masteryScore(card, t) : 0 };
      });
      return { slug: th.slug, glyph: th.glyph, title: th.title, description: th.description, learned, mastered, due, total, expressions: list };
    }),
  };
}

function expressionPractice(theme: string): SessionDto {
  const th = EXPRESSIONS.themes.find((x) => x.slug === theme);
  if (!th) throw new HttpError(404, 'Thème d’expressions inconnu.');
  const s = load();
  const pool = EXPRESSIONS.themes.flatMap((x) => x.expressions.map(toEngine));
  const entries = th.expressions.map((it) => ({ item: toEngine(it), card: s.cards[it.slug] ? toCard(s.cards[it.slug]) : null }));
  const plan = planCharacterPractice(entries, pool, now(), createRng(`expr:${theme}:${Date.now()}`), { maxItems: 8, maxNew: 5 });
  if (!plan.questions.length) return { sessionId: '', questions: [] };
  const sessionId = uid();
  s.sessions[sessionId] = { kind: 'review', lessonSlug: null, endedAt: null, createdAt: now().toISOString() };
  const questions = issue(sessionId, 'practice', plan.questions);
  save();
  return { sessionId, questions };
}

// ───────────────────────── Boss de fin de monde ─────────────────────────

function bossWorld(slug: string) {
  const w = WORLDS.find((x) => x.slug === slug);
  if (!w || !w.boss) throw new HttpError(404, 'Ce monde n’a pas de gardien.');
  const st = statuses();
  const lessons = w.chapters.flatMap((c) => c.lessons);
  if (!lessons.length || !lessons.every((l) => st.get(l.slug) === 'completed')) throw new HttpError(403, 'Termine toutes les leçons de ce monde pour affronter son gardien.');
  return { w, lessons, boss: w.boss };
}

function bossStart(slug: string): BossFightDto {
  const { w, lessons, boss } = bossWorld(slug);
  const items = [...new Map(lessons.flatMap((l) => l.items.map((it) => [it.slug, toEngine(it)]))).values()];
  const authored = lessons.flatMap((l) => l.exercises);
  const questions = planBossFight(items, authored, poolFor(slug), createRng(`${slug}:${Date.now()}`));
  const s = load();
  const sessionId = uid();
  s.sessions[sessionId] = { kind: 'boss', lessonSlug: null, endedAt: null, createdAt: now().toISOString(), scope: slug };
  const r = (s.bosses[slug] ??= { attempts: 0, victories: 0, bestHits: 0, firstVictoryAt: null });
  r.attempts++;
  const issued = issue(sessionId, 'boss', questions);
  save();
  return { sessionId, world: { slug: w.slug, title: w.title }, boss, rules: { hp: BOSS_RULES.hp, hearts: BOSS_RULES.hearts }, questions: issued };
}

function bossFinish(slug: string, sessionId: string): BossOutcomeDto {
  const s = load();
  const se = s.sessions[sessionId];
  if (!se || se.kind !== 'boss' || se.scope !== slug) throw new HttpError(404, 'Combat introuvable.');
  if (se.endedAt) throw new HttpError(409, 'Ce combat est déjà terminé.');
  const answered = Object.values(s.questions)
    .filter((q) => q.sessionId === sessionId && q.answeredAt)
    .sort((a, b) => a.answeredAt!.localeCompare(b.answeredAt!) || a.order - b.order);
  const progress = simulateBoss(answered.map((q) => !!q.correct));
  if (progress.state === 'ongoing') throw new HttpError(400, 'Le combat n’est pas terminé.');
  const won = progress.state === 'won';
  const r = (s.bosses[slug] ??= { attempts: 1, victories: 0, bestHits: 0, firstVictoryAt: null });
  const firstVictory = won && !r.firstVictoryAt;
  const reward = bossReward(won, firstVictory);
  if (won) r.victories++;
  r.bestHits = Math.max(r.bestHits, progress.hits);
  if (firstVictory) r.firstVictoryAt = now().toISOString();
  se.endedAt = now().toISOString();
  addXp(reward.xp);
  s.coins = (s.coins ?? 0) + reward.coins;
  save();
  return { state: progress.state, hits: progress.hits, heartsLeft: progress.heartsLeft, firstVictory, xpGained: reward.xp, coinsGained: reward.coins };
}

// ───────────────────────── Quêtes, personnage, boutique ─────────────────────────

/** Récompense chaque quête du jour une seule fois (XP + pièces). */
function claimQuests() {
  const s = load();
  const key = todayKey();
  const d = daily(key);
  const claimed = (d.questsClaimed ??= []);
  const done = dailyQuests(key, d).filter((q) => q.done && !claimed.includes(q.id));
  for (const q of done) {
    claimed.push(q.id);
    addXp(q.xp);
    s.coins = (s.coins ?? 0) + COINS.questCompleted;
  }
  return done;
}

function shopState() {
  const s = load();
  const defeated = new Set(Object.entries(s.bosses ?? {}).filter(([, b]) => b.firstVictoryAt).map(([k]) => k));
  return { s, owned: ownedSkus(CATALOG, s.inventory ?? []), defeated, avatar: normalizeAvatar(s.avatar) };
}

function shop(): ShopDto {
  const { s, owned, defeated, avatar } = shopState();
  const equipped = new Set([avatar.outfit, avatar.hat, avatar.accessory, avatar.background].filter(Boolean));
  const bossName = (slug: string) => WORLDS.find((w) => w.slug === slug)?.boss?.name ?? 'un gardien';
  return {
    coins: s.coins ?? 0,
    avatar,
    slots: CATALOG.slots,
    items: CATALOG.items.map((i) => ({ ...i, owned: owned.has(i.sku), equipped: equipped.has(i.sku), lockedBy: i.unlockBoss && !defeated.has(i.unlockBoss) ? bossName(i.unlockBoss) : null })),
  };
}

function acquire(sku: string): ShopDto {
  const { s, owned, defeated } = shopState();
  const check = checkAcquire(CATALOG, sku, { coins: s.coins ?? 0, owned, defeatedBosses: defeated });
  if (!check.ok) {
    const status = { unknown_item: 404, already_owned: 409, boss_required: 403, not_enough_coins: 400, not_for_sale: 400 }[check.error];
    throw new HttpError(status, ACQUIRE_ERRORS_FR[check.error]);
  }
  s.coins = (s.coins ?? 0) - check.cost;
  (s.inventory ??= []).push(sku);
  save();
  return shop();
}

function saveAvatar(config: unknown): AvatarConfig {
  const { s, owned } = shopState();
  const errors = validateAvatar(config, CATALOG, owned);
  if (errors.length) throw new HttpError(400, errors[0]);
  const c = config as AvatarConfig;
  s.avatar = { skin: c.skin, hair: c.hair, hairColor: c.hairColor, eyes: c.eyes, outfit: c.outfit ?? null, hat: c.hat ?? null, accessory: c.accessory ?? null, background: c.background ?? null };
  save();
  return normalizeAvatar(s.avatar);
}

// ───────────────────────── Mini-jeux ─────────────────────────

const seenItems = () => Object.entries(load().cards).filter(([id, c]) => ITEMS.has(id) && c.state !== 'new').map(([id]) => toEngine(ITEMS.get(id)!));

function gameInfo(def: GameDef, seen: EngineItem[]): GameInfoDto {
  const r = load().games?.[def.id];
  const n = eligibleItems(def, seen).length;
  return { id: def.id, title: def.title, description: def.description, durationSec: def.durationSec, minItems: def.minItems, seenItems: n, available: n >= def.minItems, bestScore: r?.bestScore ?? 0, plays: r?.plays ?? 0 };
}

function gameDef(id: string) {
  if (!GAME_IDS.includes(id as GameId)) throw new HttpError(404, 'Mini-jeu inconnu.');
  return GAMES[id as GameId];
}

function games(): GamesDto {
  const seen = seenItems();
  return { games: GAME_IDS.map((id) => gameInfo(GAMES[id], seen)), coinsLeftToday: Math.max(0, DAILY_GAME_COIN_CAP - (daily().gameCoins ?? 0)) };
}

function gameStart(id: string): GameStartDto {
  const def = gameDef(id);
  const seen = seenItems();
  const info = gameInfo(def, seen);
  if (!info.available) throw new HttpError(403, `Rencontre au moins ${def.minItems} notions adaptées dans tes leçons pour débloquer ${def.title}.`);
  const questions = planTimedGame(def, seen, focusedPool(seen, POOL), createRng(`${id}:${Date.now()}`));
  const s = load();
  const sessionId = uid();
  s.sessions[sessionId] = { kind: 'game', lessonSlug: null, endedAt: null, createdAt: now().toISOString(), scope: id };
  const issued = issue(sessionId, 'game', questions);
  save();
  return { sessionId, game: info, questions: issued };
}

function gameFinish(id: string, sessionId: string): GameResultDto {
  const def = gameDef(id);
  const s = load();
  const se = s.sessions[sessionId];
  if (!se || se.kind !== 'game' || se.scope !== id) throw new HttpError(404, 'Partie introuvable.');
  if (se.endedAt) throw new HttpError(409, 'Cette partie est déjà terminée.');
  const started = Date.parse(se.createdAt);
  const qs = Object.values(s.questions).filter((q) => q.sessionId === sessionId);
  if (Date.now() - started < def.durationSec * 1000 - 2000 && !qs.every((q) => q.answeredAt)) throw new HttpError(400, 'La partie n’est pas terminée.');
  const { score, answered } = scoreTimedGame(def, qs.filter((q) => q.answeredAt).map((q) => ({ correct: !!q.correct, atMs: Date.parse(q.answeredAt!) - started })));
  const d = daily();
  const reward = gameReward(score, d.gameCoins ?? 0);
  const prev = (s.games ??= {})[id];
  const bestScore = Math.max(prev?.bestScore ?? 0, score);
  s.games[id] = { plays: (prev?.plays ?? 0) + 1, bestScore, lastScore: score };
  d.gameCoins = (d.gameCoins ?? 0) + reward.coins;
  s.coins = (s.coins ?? 0) + reward.coins;
  addXp(reward.xp);
  se.endedAt = now().toISOString();
  save();
  return { score, answered, bestScore, newBest: score > 0 && score > (prev?.bestScore ?? 0), xpGained: reward.xp, coinsGained: reward.coins };
}

// ───────────────────────── Examen blanc et positionnement ─────────────────────────

/** Applique un résultat à la carte d'une notion (même règles que le serveur). */
function applyCard(itemId: string, sessionId: string, correct: boolean, t: Date, opts: { rating?: 1 | 2 | 3 | 4 } = {}) {
  const s = load();
  const existing = s.cards[itemId];
  const card = existing ? toCard(existing) : newCard(t);
  const rating = opts.rating ?? (correct ? 3 : 1);
  const next = schedule(card, rating, t, { ...DEFAULT_OPTIONS, desiredRetention: s.prefs.desiredRetention });
  s.cards[itemId] = fromCard(next, existing?.createdAt ?? t.toISOString());
  s.history.push({ itemId, sessionId, rating, stabilityAfter: next.stability, reviewedAt: t.toISOString() });
}

function examStart(slug: string): ExamStartDto {
  const def = EXAMS[slug];
  if (!def) throw new HttpError(404, 'Examen inconnu.');
  const rng = createRng(`${slug}:${Date.now()}`);
  let planned;
  if (def.bank) {
    const bank = BANKS[def.bank];
    if (!bank) throw new HttpError(404, 'Banque de questions introuvable.');
    planned = planBankExam(bank, rng);
  } else {
    const lessons = lessonsOf(def.level);
    const items = [...new Map(lessons.flatMap((l) => l.items.map((it) => [it.slug, toEngine(it)]))).values()];
    const authored = lessons.flatMap((l) => l.exercises);
    planned = planExam(def, items, authored, POOL, rng);
  }
  const s = load();
  const sessionId = uid();
  s.sessions[sessionId] = { kind: 'exam', lessonSlug: null, endedAt: null, createdAt: now().toISOString(), scope: slug };
  const issued = issue(sessionId, 'exam', planned.map((p) => Object.assign(p.question, { section: p.section }) as Question));
  save();
  return { sessionId, exam: { slug, title: def.title, durationMin: def.durationMin, sections: def.sections, passPercent: def.passPercent, sectionMinPercent: def.sectionMinPercent }, questions: issued };
}

function examSubmit(slug: string, sessionId: string, answers: Record<string, unknown>): ExamResultDto {
  const def = EXAMS[slug];
  const s = load();
  const se = s.sessions[sessionId];
  if (!def || !se || se.kind !== 'exam' || se.scope !== slug) throw new HttpError(404, 'Examen introuvable.');
  if (se.endedAt) throw new HttpError(409, 'Cette copie a déjà été rendue.');
  const t = now();
  const late = t.getTime() - Date.parse(se.createdAt) > def.durationMin * 60_000 + 120_000;
  const qs = Object.values(s.questions).filter((q) => q.sessionId === sessionId).sort((a, b) => a.order - b.order);
  const section = (q: StoredQuestion) => ((q.payload as { section?: ExamSectionId }).section ?? 'vocab');
  const grade = gradeExam(def, qs.map((q) => ({ section: section(q), type: q.type, answer: q.answer })), qs.map((q) => answers[q.id]));
  const seen = new Set<string>();
  qs.forEach((q, i) => {
    q.answeredAt = t.toISOString();
    q.correct = grade.results[i];
    if (!q.itemId || !ITEMS.has(q.itemId) || seen.has(q.itemId)) return;
    seen.add(q.itemId);
    if (!s.cards[q.itemId] && grade.results[i]) return;
    applyCard(q.itemId, sessionId, grade.results[i], t);
  });
  const previousPass = (s.exams ?? []).some((e) => e.slug === slug && e.passed);
  const xp = grade.correct * 2 + (grade.passed && !previousPass ? 30 : 0);
  const coins = grade.passed && !previousPass ? 20 : 0;
  addXp(xp);
  s.coins = (s.coins ?? 0) + coins;
  (s.exams ??= []).push({ slug, title: def.title, date: t.toISOString(), percent: grade.percent, passed: grade.passed, sections: grade.sections.map((x) => ({ id: x.id, title: x.title, percent: x.percent })) });
  se.endedAt = t.toISOString();
  save();
  const show = (v: unknown) => (v === undefined || v === null ? null : Array.isArray(v) ? v.join(' ') : String(v));
  return {
    percent: grade.percent, correct: grade.correct, total: grade.total, passed: grade.passed, late,
    sections: grade.sections, recommendations: examRecommendations(grade, def.level),
    mistakes: qs
      .map((q, i) => ({ q, i }))
      .filter(({ i }) => !grade.results[i])
      .map(({ q }) => {
        const p = q.payload as { prompt: string; display?: { jp?: string; text?: string }; audio?: string };
        return { section: section(q), prompt: p.prompt, jp: p.display?.jp ?? (q.type === 'listening_choice' ? p.audio ?? null : null), text: p.display?.text ?? null, given: show(answers[q.id]), correctAnswer: show(q.answer)!, explanation: q.explanation };
      }),
    xpGained: xp, coinsGained: coins, passPercent: def.passPercent, sectionMinPercent: def.sectionMinPercent, scaled: grade.scaled ? { ...grade.scaled, max: JLPT_SCALE } : null,
  };
}

const PLACEMENT_WORLDS = N5_WORLDS.filter((w) => w.chapters.some((c) => c.lessons.length));

function placementBlock(sessionId: string, index: number): PlacementStepDto {
  const w = PLACEMENT_WORLDS[index];
  const lessons = w.chapters.flatMap((c) => c.lessons);
  const items = [...new Map(lessons.flatMap((l) => l.items.map((it) => [it.slug, toEngine(it)]))).values()];
  const questions = planPlacementBlock(items, lessons.flatMap((l) => l.exercises), poolFor(w.slug), createRng(`${sessionId}:${index}`));
  const issued = issue(sessionId, 'placement', questions, index * 10);
  save();
  return { done: false, lastPassed: null, block: { sessionId, world: { slug: w.slug, title: w.title, order: w.order }, index, totalWorlds: PLACEMENT_WORLDS.length, questions: issued } };
}

function placementStart(): PlacementStepDto {
  const s = load();
  const sessionId = uid();
  s.sessions[sessionId] = { kind: 'placement', lessonSlug: null, endedAt: null, createdAt: now().toISOString(), state: { index: 0, passed: [] } };
  return placementBlock(sessionId, 0);
}

function placementAnswer(sessionId: string, answers: Record<string, unknown>): PlacementStepDto {
  const s = load();
  const se = s.sessions[sessionId];
  if (!se || se.kind !== 'placement' || !se.state) throw new HttpError(404, 'Test introuvable.');
  if (se.endedAt) throw new HttpError(409, 'Ce test est déjà terminé.');
  const t = now();
  const { index, passed } = se.state;
  const block = Object.values(s.questions).filter((q) => q.sessionId === sessionId && !q.answeredAt && q.order >= index * 10 && q.order < index * 10 + 10);
  let correct = 0;
  for (const q of block) {
    const ok = checkAnswer({ type: q.type, answer: q.answer }, answers[q.id]);
    q.correct = ok;
    q.answeredAt = t.toISOString();
    if (ok) correct++;
  }
  const world = PLACEMENT_WORLDS[index];
  const ok = placementBlockPassed(correct);
  const nextPassed = ok ? [...passed, world.slug] : passed;
  if (ok && index + 1 < PLACEMENT_WORLDS.length) {
    se.state = { index: index + 1, passed: nextPassed };
    return { ...(placementBlock(sessionId, index + 1) as Extract<PlacementStepDto, { done: false }>), lastPassed: true };
  }
  // Validation des mondes réussis
  const validated = PLACEMENT_WORLDS.filter((w) => nextPassed.includes(w.slug));
  for (const w of validated) {
    for (const l of w.chapters.flatMap((c) => c.lessons)) {
      const p = (s.progress[l.slug] ??= { status: 'completed', attempts: 0, bestScore: 0, completedAt: t.toISOString() });
      p.status = 'completed';
      p.completedAt ??= t.toISOString();
      for (const it of l.items) if (!s.cards[it.slug]) applyCard(it.slug, sessionId, true, t, { rating: 4 });
    }
  }
  se.endedAt = t.toISOString();
  s.placementAt = t.toISOString();
  save();
  const next = nextLesson();
  return {
    done: true,
    validated: validated.map((w) => ({ slug: w.slug, title: w.title })),
    stoppedAt: ok ? null : { slug: world.slug, title: world.title },
    nextLesson: next ? { slug: next.slug, title: next.title } : null,
  };
}

// ───────────────────────── Atelier JLPT ─────────────────────────

function jlptMaterial() {
  const s = load();
  const learned = Object.keys(s.cards).filter((id) => ITEMS.has(id)).map((id) => toEngine(ITEMS.get(id)!));
  const authored = LESSONS.filter((l) => s.progress[l.slug]?.status === 'completed').flatMap((l) => l.exercises);
  return { learned, authored };
}

function jlptDrills(): JlptDrillsDto {
  const m = jlptMaterial();
  const rng = createRng('jlpt-count');
  return {
    minQuestions: 3,
    drills: (Object.keys(JLPT_DRILLS) as JlptDrillPart[]).map((part) => ({ part, ...JLPT_DRILLS[part], available: planJlptDrill(part, m.learned, m.authored, POOL, rng, EXAMPLES).length })),
  };
}

function jlptStart(part: string): SessionDto {
  if (!(part in JLPT_DRILLS)) throw new HttpError(404, 'Épreuve inconnue.');
  const m = jlptMaterial();
  const qs = planJlptDrill(part as JlptDrillPart, m.learned, m.authored, POOL, createRng(`jlpt:${part}:${Date.now()}`), EXAMPLES);
  if (qs.length < 3) throw new HttpError(409, 'Pas encore assez de notions pour cette épreuve : termine quelques leçons de plus.');
  const s = load();
  const sessionId = uid();
  s.sessions[sessionId] = { kind: 'lesson', lessonSlug: null, endedAt: null, createdAt: now().toISOString(), scope: `jlpt:${part}` };
  const issued = issue(sessionId, 'practice', qs);
  save();
  return { sessionId, questions: issued };
}

// ───────────────────────── Succès ─────────────────────────

function achievementStats(): AchievementStats {
  const s = load();
  const t = now();
  const days = Object.entries(s.daily);
  let masteredItems = 0;
  let masteredKanji = 0;
  for (const [id, c] of Object.entries(s.cards)) {
    if (masteryOf(toCard(c), t) !== 'mastered') continue;
    masteredItems++;
    if (ITEMS.get(id)?.kind === 'kanji') masteredKanji++;
  }
  const games = Object.values(s.games ?? {});
  return {
    lessonsCompleted: Object.values(s.progress).filter((p) => p.status === 'completed').length,
    perfectLessons: days.reduce((n, [, d]) => n + d.perfectLessons, 0),
    bestStreak: longestStreak(days.filter(([, d]) => d.total > 0).map(([k]) => k)),
    correctAnswers: days.reduce((n, [, d]) => n + d.correct, 0),
    reviewsDone: days.reduce((n, [, d]) => n + d.reviews, 0),
    bestCombo: days.reduce((n, [, d]) => Math.max(n, d.bestCombo), 0),
    masteredItems,
    masteredKanji,
    bossesDefeated: Object.values(s.bosses ?? {}).filter((b) => b.firstVictoryAt).length,
    examsTaken: (s.exams ?? []).length,
    examsPassed: (s.exams ?? []).filter((e) => e.passed).length,
    gamesPlayed: games.reduce((n, g) => n + g.plays, 0),
    bestGameScore: games.reduce((n, g) => Math.max(n, g.bestScore), 0),
    itemsCollected: (s.inventory ?? []).length,
    placementDone: s.placementAt ? 1 : 0,
  };
}

const achievementDto = (def: AchievementDef, value: number, unlocked: boolean, at: string | null): AchievementDto => ({
  slug: def.slug, title: def.title, description: def.description, glyph: def.glyph, category: def.category, rarity: def.rarity,
  value, target: def.target, unlocked, unlockedAt: at, coins: ACHIEVEMENT_COINS[def.rarity],
});

function achievements(): AchievementsDto {
  const done = load().achievements ?? {};
  const progress = achievementProgress(achievementStats(), Object.keys(done));
  return { unlocked: progress.filter((p) => p.unlocked).length, total: progress.length, achievements: progress.map((p) => achievementDto(p.def, p.value, p.unlocked, done[p.def.slug] ?? null)) };
}

function checkAchievements(): AchievementCheckDto {
  const s = load();
  s.achievements ??= {};
  const granted = newlyUnlocked(achievementStats(), Object.keys(s.achievements));
  const at = now().toISOString();
  for (const d of granted) s.achievements[d.slug] = at;
  const r = achievementReward(granted);
  s.coins = (s.coins ?? 0) + r.coins;
  s.user.xp += r.xp;
  if (granted.length) save();
  return { unlocked: granted.map((d) => achievementDto(d, d.target, true, at)), coinsGained: r.coins, xpGained: r.xp };
}

// ───────────────────────── Routeur ─────────────────────────

/** Traduit un appel « HTTP » de l'application en appel local. */
const duels = localDuels({
  duelState: () => load().duel,
  setDuelState: (d) => {
    load().duel = d;
  },
  save,
  reward: (xp, coins) => {
    addXp(xp);
    const s = load();
    s.coins = (s.coins ?? 0) + coins;
  },
  me: () => ({ displayName: load().user.displayName, avatar: normalizeAvatar(load().avatar) }),
  seenItems: () => seenItems(),
  starterItems: () => [...(WORLD_POOL.get('n5-w1') ?? [])].filter((i) => i.kind === 'kana'),
  pool: POOL,
  fail: (status, message) => {
    throw new HttpError(status, message);
  },
});

export async function handle(method: string, fullPath: string, body: unknown): Promise<unknown> {
  const p = fullPath.split('?')[0];
  const b = (body ?? {}) as Record<string, unknown>;
  let m: RegExpMatchArray | null;
  const route = `${method} ${p}`;

  if (route === 'GET /me') return me();
  if (route === 'PUT /me/onboarding') return onboarding(b);
  if (route === 'PUT /me/preferences') return updatePrefs(b);
  if (route === 'GET /dashboard') return dashboard();
  if (route === 'GET /stats') return stats();
  if ((m = route.match(/^GET \/path\/(\w+)$/))) return path(m[1]);
  if ((m = route.match(/^GET \/lessons\/([\w-]+)$/))) return lessonDto(m[1]);
  if ((m = route.match(/^POST \/lessons\/([\w-]+)\/start$/))) return startLesson(m[1]);
  if ((m = route.match(/^POST \/lessons\/([\w-]+)\/complete$/))) return completeLesson(m[1], String(b.sessionId));
  if ((m = route.match(/^GET \/questions\/([\w-]+)$/))) return getQuestion(m[1]);
  if ((m = route.match(/^POST \/questions\/([\w-]+)\/answer$/))) return answer(m[1], b.answer, Number(b.responseMs));
  if ((m = route.match(/^POST \/questions\/([\w-]+)\/retry$/))) return retry(m[1]);
  if ((m = route.match(/^POST \/questions\/([\w-]+)\/shown$/))) {
    const q = load().questions[m[1]];
    if (!q) throw new HttpError(404, 'Question introuvable.');
    if (q.phase !== 'boss') return { timeLimitSec: null };
    if (!q.shownAt && !q.answeredAt) q.shownAt = now().toISOString();
    save();
    return { timeLimitSec: bossTimeLimitSec(q.type) };
  }
  if ((m = route.match(/^POST \/worlds\/([\w-]+)\/boss\/start$/))) return bossStart(m[1]);
  if ((m = route.match(/^POST \/worlds\/([\w-]+)\/boss\/finish$/))) return bossFinish(m[1], String(b.sessionId));
  if ((m = route.match(/^POST \/exams\/([\w-]+)\/start$/))) return examStart(m[1]);
  if ((m = route.match(/^POST \/exams\/([\w-]+)\/submit$/))) return examSubmit(m[1], String(b.sessionId), (b.answers ?? {}) as Record<string, unknown>);
  if (route === 'POST /placement/start') return placementStart();
  if (route === 'POST /placement/answer') return placementAnswer(String(b.sessionId), (b.answers ?? {}) as Record<string, unknown>);
  if (route === 'GET /games') return games();
  if ((m = route.match(/^POST \/games\/([\w-]+)\/start$/))) return gameStart(m[1]);
  if ((m = route.match(/^POST \/games\/([\w-]+)\/finish$/))) return gameFinish(m[1], String(b.sessionId));
  if (route === 'GET /jlpt/drills') return jlptDrills();
  if ((m = route.match(/^POST \/jlpt\/drills\/(\w+)$/))) return jlptStart(m[1]);
  if (route === 'GET /achievements') return achievements();
  if (route === 'POST /achievements/check') return checkAchievements();
  if (route === 'GET /shop') return shop();
  if (route === 'POST /shop/acquire') return acquire(String(b.sku));
  if (route === 'PUT /me/avatar') return saveAvatar(b.avatar);
  if (route === 'GET /expressions') return expressions();
  if (route === 'POST /expressions/practice') return expressionPractice(String(b.theme));
  if (route === 'GET /characters') return characters();
  if (route === 'POST /characters/practice') return characterPractice(String(b.scope));
  if (route === 'GET /reviews/summary') return reviewSummary();
  if (route === 'POST /reviews/session') return reviewSession();
  if (route === 'GET /notifications/preferences') return notifPrefs();
  if (route === 'PUT /notifications/preferences') return updateNotifPrefs(b as Partial<NotificationPrefsDto>);
  if (route === 'GET /notifications/inbox') return inbox();
  if ((m = route.match(/^POST \/notifications\/([\w-]+)\/open$/)) && m[1] !== 'test') {
    const n = load().notifications.find((x) => x.id === m![1]);
    if (n && n.status === 'pending') n.status = 'opened';
    save();
    return { ok: true };
  }
  if (route === 'POST /notifications/test') {
    const r = createChallenge(true);
    if (!r) throw new HttpError(409, 'Aucune notion à réviser pour le moment : apprends d’abord une leçon !');
    return r;
  }
  if (p === '/duels' || p.startsWith('/duels/')) return duels(method, p, new URLSearchParams(fullPath.split('?')[1] ?? ''), b);
  if (route === 'POST /auth/logout') return undefined;
  throw new HttpError(404, `Fonction indisponible en mode hors ligne (${route}).`);
}
