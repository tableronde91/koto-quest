/**
 * Contrats d'API partagés entre l'API, le web et (phase 4) l'application mobile.
 * Aucun code d'exécution lourd ici : uniquement des types et constantes.
 */
import type { AvatarConfig, CosmeticItem, CosmeticSlot, Mastery, PublicQuestion, QuestStatus, ReadinessEstimate, ReminderMode } from '@koto/learning-engine';

export type { AvatarConfig, CosmeticItem, CosmeticSlot, Mastery, PublicQuestion, QuestStatus, ReadinessEstimate, ReminderMode };

export type JlptCode = 'N5' | 'N4' | 'N3' | 'N2' | 'N1';
export const JLPT_LEVELS: JlptCode[] = ['N5', 'N4', 'N3', 'N2', 'N1'];

export type SelfLevel = 'beginner' | 'kana' | 'basics' | 'n5' | 'n4plus';
export const DIFFICULT_AREAS = ['kana', 'vocabulary', 'kanji', 'grammar', 'listening', 'reading'] as const;
export type DifficultArea = (typeof DIFFICULT_AREAS)[number];

export interface MeDto {
  id: string;
  email: string;
  displayName: string;
  onboarded: boolean;
  xp: number;
  coins: number;
  avatar: AvatarConfig;
  preferences: {
    selfLevel: SelfLevel;
    targetLevel: JlptCode;
    examDate: string | null;
    minutesPerDay: number;
    difficultAreas: DifficultArea[];
    timezone: string;
    showFurigana: boolean;
    theme: 'system' | 'light' | 'dark';
    reducedMotion: boolean;
    locale: 'fr' | 'en';
  };
}

export interface OnboardingInput {
  selfLevel: SelfLevel;
  targetLevel: JlptCode;
  examDate?: string | null;
  minutesPerDay: number;
  difficultAreas: DifficultArea[];
  reminderMode: ReminderMode | 'off';
  timezone?: string;
  locale?: 'fr' | 'en';
}

export type LessonStatus = 'locked' | 'available' | 'in_progress' | 'completed';

export interface PathLessonDto {
  slug: string;
  title: string;
  objective: string;
  minutes: number;
  status: LessonStatus;
  itemCount: number;
}
export interface PathChapterDto {
  slug: string;
  title: string;
  lessons: PathLessonDto[];
}
export interface PathWorldDto {
  slug: string;
  order: number;
  title: string;
  description: string;
  comingSoon: boolean;
  /** Monde antérieur au point de départ choisi lors de l'onboarding. */
  optional: boolean;
  progress: { completed: number; total: number };
  chapters: PathChapterDto[];
  /** Gardien de fin de monde, s'il y en a un. */
  boss: WorldBossDto | null;
  /** Examen blanc proposé dans ce monde. */
  exam: { slug: string; title: string; attempts: number; bestPercent: number | null; passed: boolean } | null;
}

export interface WorldBossDto {
  name: string;
  glyph: string;
  intro: string;
  /** Toutes les leçons du monde sont terminées. */
  available: boolean;
  defeated: boolean;
  attempts: number;
}

export interface BossFightDto {
  sessionId: string;
  world: { slug: string; title: string };
  boss: { name: string; glyph: string; intro: string };
  rules: { hp: number; hearts: number };
  questions: IssuedQuestionDto[];
}

export interface BossOutcomeDto {
  state: 'won' | 'lost';
  hits: number;
  heartsLeft: number;
  firstVictory: boolean;
  xpGained: number;
  coinsGained: number;
}
export interface PathDto {
  level: { code: JlptCode; title: string; region: string; notice: string | null };
  /** Niveaux disponibles (N5 d'abord) avec la progression de l'utilisateur */
  levels: { code: JlptCode; title: string; lessons: number; completed: number }[];
  worlds: PathWorldDto[];
}

export interface LessonItemDto {
  id: string;
  kind: 'kana' | 'vocabulary' | 'kanji' | 'grammar';
  front: string;
  reading: string | null;
  romaji: string | null;
  meaning: string;
  kanji?: { onyomi: string[]; kunyomi: string[]; strokes: number | null } | null;
  mastery: Mastery | null;
}

export interface LessonDto {
  slug: string;
  title: string;
  objective: string;
  minutes: number;
  explanation: string[];
  items: LessonItemDto[];
  examples: { jp: string; reading: string | null; fr: string }[];
  status: LessonStatus;
  world: { slug: string; title: string };
  chapter: { slug: string; title: string };
}

export interface IssuedQuestionDto extends PublicQuestion {
  id: string;
  phase: 'lesson' | 'mini_review' | 'review' | 'quiz' | 'practice' | 'boss' | 'game' | 'exam' | 'placement';
  /** Section d'examen (vocabulaire, grammaire, écoute). */
  section?: 'vocab' | 'grammar' | 'listening';
  /** Identifiant de l'exercice raté que celui-ci reprend. */
  retryOf?: string | null;
}

export interface SessionDto {
  sessionId: string;
  questions: IssuedQuestionDto[];
}

export interface AnswerResultDto {
  correct: boolean;
  correctAnswer: string | string[];
  explanation: string;
  xpGained: number;
  mastery: Mastery | null;
  nextReviewAt: string | null;
  /** Quêtes du jour accomplies grâce à cette réponse (déjà récompensées). */
  questsCompleted?: { title: string; xp: number }[];
  /** Combat de gardien : réponse arrivée après la fin du chrono (comptée comme une erreur). */
  timedOut?: boolean;
}

export interface LessonCompletionDto {
  score: number;
  correct: number;
  total: number;
  xpGained: number;
  coinsGained: number;
  perfect: boolean;
  miniReview: IssuedQuestionDto[];
  nextLessonSlug: string | null;
}

export interface DashboardDto {
  displayName: string;
  targetLevel: JlptCode;
  examDate: string | null;
  progress: { completedLessons: number; totalLessons: number; percent: number };
  xp: { total: number; level: number; intoLevel: number; forNext: number };
  coins: number;
  avatar: AvatarConfig;
  streak: { current: number; todayDone: boolean; graceDaysUsed: number };
  today: { seconds: number; answers: number; accuracy: number | null };
  mastered: { words: number; kanji: number; kana: number; grammar: number };
  reviews: { due: number; learningSoon: number };
  plan: { reviewLimit: number; newItemLimit: number; lessonsSuggested: number; catchUpMode: boolean; estimatedMinutes: number };
  nextLesson: { slug: string; title: string; worldTitle: string } | null;
  quests: QuestStatus[];
  readiness: ReadinessEstimate;
  /** Proposer le test de positionnement (jamais fait, aucune leçon terminée). */
  suggestPlacement: boolean;
  notifications: { consent: boolean; enabled: boolean };
}

export interface StatsDto {
  days: { date: string; seconds: number; answers: number; correct: number; xp: number }[];
  weeks: { weekStart: string; minutes: number }[];
  accuracy: number | null;
  masteryDistribution: Record<Mastery, number>;
  byKind: Record<'kana' | 'vocabulary' | 'kanji' | 'grammar', { learned: number; mastered: number }>;
  growth: { date: string; learned: number; mastered: number }[];
  totals: { answers: number; reviews: number; lessonsCompleted: number; studySeconds: number };
  exams: { date: string; title: string; percent: number; passed: boolean; sections: { id: string; title: string; percent: number }[] }[];
  items: { id: string; front: string; reading: string | null; meaning: string; kind: string; mastery: Mastery; due: string; lapses: number }[];
}

export interface NotificationPrefsDto {
  consent: boolean;
  enabled: boolean;
  mode: ReminderMode;
  customTimes: number[];
  windowStart: number;
  windowEnd: number;
  quietStart: number | null;
  quietEnd: number | null;
  pausedUntil: string | null;
  slots: number[];
  pushSubscribed: boolean;
  vapidPublicKey: string | null;
}

export interface InboxItemDto {
  id: string;
  title: string;
  body: string;
  questionId: string | null;
  createdAt: string;
}

export interface ApiErrorDto {
  statusCode: number;
  message: string | string[];
}

// ───────── Onglet Caractères ─────────

export interface CharacterDto {
  id: string;
  kind: 'kana' | 'kanji';
  front: string;
  reading: string | null;
  romaji: string | null;
  meaning: string;
  kanji?: { onyomi: string[]; kunyomi: string[]; strokes: number | null } | null;
  mastery: Mastery | null;
  /** 0..100 : barre de maîtrise sous le caractère. */
  score: number;
}

export interface CharacterGroupDto {
  slug: string;
  title: string;
  items: CharacterDto[];
}

export interface CharacterSectionDto {
  slug: 'hiragana' | 'katakana' | 'kanji';
  title: string;
  description: string;
  learned: number;
  mastered: number;
  total: number;
  due: number;
  groups: CharacterGroupDto[];
}

export interface CharactersDto {
  notice: string | null;
  sections: CharacterSectionDto[];
}

// ───────── Personnage et boutique ─────────

export interface ShopItemDto extends CosmeticItem {
  owned: boolean;
  equipped: boolean;
  /** Trophée pas encore débloqué : nom du gardien à vaincre. */
  lockedBy: string | null;
}

export interface ShopDto {
  coins: number;
  avatar: AvatarConfig;
  slots: { slot: CosmeticSlot; label: string }[];
  items: ShopItemDto[];
}

// ───────── Mini-jeux ─────────

export interface GameInfoDto {
  id: 'kanji-rush' | 'speed' | 'listening';
  title: string;
  description: string;
  durationSec: number;
  minItems: number;
  /** Notions vues utilisables dans ce jeu. */
  seenItems: number;
  available: boolean;
  bestScore: number;
  plays: number;
}

export interface GamesDto {
  games: GameInfoDto[];
  coinsLeftToday: number;
}

export interface GameStartDto {
  sessionId: string;
  game: GameInfoDto;
  questions: IssuedQuestionDto[];
}

export interface GameResultDto {
  score: number;
  answered: number;
  bestScore: number;
  newBest: boolean;
  xpGained: number;
  coinsGained: number;
}

// ───────── Examen blanc ─────────

export interface ExamSectionDto {
  id: 'vocab' | 'grammar' | 'listening';
  title: string;
  jpTitle: string;
  count: number;
}

export interface ExamStartDto {
  sessionId: string;
  exam: { slug: string; title: string; durationMin: number; sections: ExamSectionDto[]; passPercent: number; sectionMinPercent: number };
  questions: IssuedQuestionDto[];
}

export interface ExamResultDto {
  percent: number;
  correct: number;
  total: number;
  passed: boolean;
  late: boolean;
  sections: { id: string; title: string; jpTitle: string; correct: number; total: number; percent: number }[];
  recommendations: string[];
  mistakes: { section: string; prompt: string; jp: string | null; text: string | null; given: string | null; correctAnswer: string; explanation: string }[];
  xpGained: number;
  coinsGained: number;
  passPercent: number;
  sectionMinPercent: number;
  /** Barème du JLPT (examen au format officiel) : points obtenus et maximums/seuils */
  scaled?: { language: number; listening: number; total: number; max: { language: number; listening: number; total: number; passTotal: number; passLanguage: number; passListening: number } } | null;
}

// ───────── Test de positionnement ─────────

export interface PlacementBlockDto {
  sessionId: string;
  world: { slug: string; title: string; order: number };
  index: number;
  totalWorlds: number;
  questions: IssuedQuestionDto[];
}

export type PlacementStepDto =
  | { done: false; block: PlacementBlockDto; lastPassed: boolean | null }
  | { done: true; validated: { slug: string; title: string }[]; stoppedAt: { slug: string; title: string } | null; nextLesson: { slug: string; title: string } | null };

// ───────────── Succès ─────────────

export interface AchievementDto {
  slug: string;
  title: string;
  description: string;
  glyph: string;
  category: 'study' | 'streak' | 'mastery' | 'adventure' | 'play';
  rarity: 'common' | 'rare' | 'epic';
  value: number;
  target: number;
  unlocked: boolean;
  unlockedAt: string | null;
  coins: number;
}

export interface AchievementsDto {
  unlocked: number;
  total: number;
  achievements: AchievementDto[];
}

/** Réponse de la vérification : succès débloqués à l'instant (avec récompenses déjà créditées). */
export interface AchievementCheckDto {
  unlocked: AchievementDto[];
  coinsGained: number;
  xpGained: number;
}

// ───────────── Atelier JLPT ─────────────

export interface JlptDrillsDto {
  /** Nombre minimal de questions pour lancer une série */
  minQuestions: number;
  drills: { part: 'kanji' | 'writing' | 'grammar' | 'star' | 'listening'; title: string; jpTitle: string; description: string; available: number }[];
}

// ───────────── Duels ─────────────

export type DuelKind = 'ranked' | 'friendly' | 'practice';
export type DuelStatus = 'pending' | 'active' | 'finished' | 'declined' | 'cancelled' | 'expired';

export interface DuelRankDto {
  tierId: string;
  jp: string;
  label: string;
  color: string;
  /** Points requis pour la division suivante (null au sommet) */
  next: number | null;
  progress: number;
}

export interface DuelPlayerDto {
  userId: string | null;
  name: string;
  avatar: AvatarConfig | null;
  rating: number;
  rank: DuelRankDto;
  isBot: boolean;
}

export interface DuelProfileDto {
  code: string;
  rating: number;
  peakRating: number;
  rank: DuelRankDto;
  wins: number;
  losses: number;
  draws: number;
  streak: number;
  bestStreak: number;
  damageDealt: number;
  /** Place au classement (par points) */
  position: number;
  players: number;
}

export interface DuelInviteDto {
  id: string;
  player: DuelPlayerDto;
  expiresAt: string;
}

export interface DuelHistoryDto {
  id: string;
  kind: DuelKind;
  opponent: string;
  result: 'win' | 'loss' | 'draw' | 'cancelled';
  delta: number | null;
  myHp: number;
  oppHp: number;
  endReason: string | null;
  endedAt: string | null;
}

export interface DuelLobbyDto {
  profile: DuelProfileDto;
  activeDuelId: string | null;
  searching: { since: string } | null;
  invites: DuelInviteDto[];
  sent: DuelInviteDto[];
  history: DuelHistoryDto[];
  online: boolean;
  rules: { hp: number; rounds: number; roundMs: number };
}

export interface DuelQueueDto {
  status: 'searching' | 'matched' | 'idle';
  duelId?: string;
  since?: string;
}

export interface DuelSideResultDto {
  answer: string | null;
  correct: boolean;
  ms: number | null;
  damage: number;
  critical: boolean;
  combo: number;
}

export interface DuelQuestionDto {
  index: number;
  type: string;
  prompt: string;
  display?: { jp?: string; reading?: string; text?: string };
  choices: string[];
}

export interface DuelStateDto {
  id: string;
  kind: DuelKind;
  status: DuelStatus;
  /** Horloge du serveur au moment de la réponse (synchronisation des chronos) */
  serverNow: string;
  rules: { hp: number; rounds: number; roundMs: number; revealMs: number };
  me: DuelPlayerDto & { hp: number; side: 1 | 2; combo: number };
  opponent: DuelPlayerDto & { hp: number; online: boolean; combo: number };
  round: number;
  roundStartsAt: string | null;
  question: DuelQuestionDto | null;
  /** Ma réponse à la question en cours (correction immédiate) et si l'adversaire a déjà répondu */
  mine: DuelSideResultDto | null;
  opponentAnswered: boolean;
  /** Correction de la question précédente (pendant l'entracte) */
  last: { question: DuelQuestionDto; answer: string; me: DuelSideResultDto; opponent: DuelSideResultDto } | null;
  /** Défi en attente */
  expiresAt: string | null;
  result: {
    outcome: 'win' | 'loss' | 'draw';
    endReason: string | null;
    ratingBefore: number;
    ratingAfter: number;
    delta: number;
    rankBefore: DuelRankDto;
    rankAfter: DuelRankDto;
    xp: number;
    coins: number;
  } | null;
}

export interface DuelLeaderboardDto {
  sort: 'rating' | 'wins';
  entries: { position: number; userId: string; name: string; avatar: AvatarConfig | null; rating: number; rank: DuelRankDto; wins: number; losses: number; me: boolean }[];
  me: { position: number; rating: number; wins: number } | null;
}

export interface DuelPlayerSearchDto {
  players: (DuelPlayerDto & { code: string })[];
}
export * from './i18n';

// ───────────── Expressions ─────────────

export type ExpressionRegister = 'polite' | 'neutral' | 'casual' | 'formal';

export interface ExpressionDto {
  id: string;
  front: string;
  reading: string | null;
  romaji: string | null;
  meaning: string;
  /** Quand et comment l'employer */
  note: string;
  register: ExpressionRegister;
  example: { jp: string; fr: string } | null;
  mastery: Mastery | null;
  score: number;
}

export interface ExpressionThemeDto {
  slug: string;
  glyph: string;
  title: string;
  description: string;
  learned: number;
  mastered: number;
  due: number;
  total: number;
  expressions: ExpressionDto[];
}

export interface ExpressionsDto {
  notice: string | null;
  themes: ExpressionThemeDto[];
}
