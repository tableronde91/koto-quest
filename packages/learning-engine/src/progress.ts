import { addDays } from './time';
import { CardState, currentRetrievability } from './fsrs';

// ---------------------------------------------------------------------------
// Séries de jours (bienveillantes)
// ---------------------------------------------------------------------------

export interface StreakResult {
  current: number;
  todayDone: boolean;
  /** Jours manqués « pardonnés » dans la série actuelle. */
  graceDaysUsed: number;
}

/**
 * Série de jours d'étude. Pour éviter les pénalités excessives, un jour manqué
 * est pardonné au plus une fois par période de 7 jours.
 * Si l'utilisateur n'a pas encore étudié aujourd'hui, la série reste intacte.
 */
export function computeStreak(activeDateKeys: Iterable<string>, todayKey: string): StreakResult {
  const active = new Set(activeDateKeys);
  const todayDone = active.has(todayKey);
  let cursor = todayDone ? todayKey : addDays(todayKey, -1);
  let current = 0;
  let graceDaysUsed = 0;
  let daysSinceGrace = Infinity;
  for (let guard = 0; guard < 3650; guard++) {
    if (active.has(cursor)) {
      current++;
      daysSinceGrace++;
    } else if (daysSinceGrace >= 7 && active.has(addDays(cursor, -1))) {
      graceDaysUsed++;
      daysSinceGrace = 0;
    } else {
      break;
    }
    cursor = addDays(cursor, -1);
  }
  return { current, todayDone, graceDaysUsed };
}

// ---------------------------------------------------------------------------
// Expérience et niveaux
// ---------------------------------------------------------------------------

export type XpContext = 'lesson' | 'review' | 'quiz';

export const XP = {
  lessonAnswer: 10,
  reviewAnswer: 5,
  quizAnswer: 8,
  wrongAnswer: 1, // l'effort compte un peu, la maîtrise compte beaucoup plus
  lessonComplete: 30,
  perfectLessonBonus: 20,
} as const;

export function xpForAnswer(correct: boolean, ctx: XpContext): number {
  if (!correct) return XP.wrongAnswer;
  return ctx === 'lesson' ? XP.lessonAnswer : ctx === 'quiz' ? XP.quizAnswer : XP.reviewAnswer;
}

export function xpForLessonCompletion(errors: number): number {
  return XP.lessonComplete + (errors === 0 ? XP.perfectLessonBonus : 0);
}

/** Niveau de personnage : chaque niveau demande 100 XP de plus que le précédent. */
export function levelFromXp(xp: number): { level: number; intoLevel: number; forNext: number } {
  let level = 1;
  let remaining = Math.max(0, Math.floor(xp));
  while (remaining >= level * 100) {
    remaining -= level * 100;
    level++;
  }
  return { level, intoLevel: remaining, forNext: level * 100 };
}

// ---------------------------------------------------------------------------
// Quêtes quotidiennes (calculées à partir de l'activité du jour)
// ---------------------------------------------------------------------------

export interface DailyActivityStats {
  newItems: number;
  reviews: number;
  kanjiReviews: number;
  bestCombo: number;
  perfectLessons: number;
  listeningCorrect: number;
}

export interface QuestStatus {
  id: string;
  title: string;
  progress: number;
  target: number;
  done: boolean;
  xp: number;
}

const QUEST_DEFS: { id: string; title: string; target: number; xp: number; value: (s: DailyActivityStats) => number }[] = [
  { id: 'learn-5', title: 'Apprendre 5 nouvelles notions', target: 5, xp: 20, value: (s) => s.newItems },
  { id: 'review-10', title: 'Faire 10 révisions', target: 10, xp: 20, value: (s) => s.reviews },
  { id: 'combo-5', title: 'Réussir 5 questions d’affilée', target: 5, xp: 15, value: (s) => s.bestCombo },
  { id: 'perfect-lesson', title: 'Terminer une leçon sans erreur', target: 1, xp: 25, value: (s) => s.perfectLessons },
  { id: 'listening-3', title: 'Réussir 3 questions d’écoute', target: 3, xp: 15, value: (s) => s.listeningCorrect },
];

/** Sélectionne 3 quêtes du jour de façon déterministe (même liste toute la journée). */
export function dailyQuests(dateKey: string, stats: DailyActivityStats): QuestStatus[] {
  const day = Number(dateKey.replace(/-/g, '')) % QUEST_DEFS.length;
  const chosen = [0, 1, 2].map((k) => QUEST_DEFS[(day + k) % QUEST_DEFS.length]);
  return chosen.map((q) => {
    const progress = Math.min(q.target, q.value(stats));
    return { id: q.id, title: q.title, progress, target: q.target, done: progress >= q.target, xp: q.xp };
  });
}

// ---------------------------------------------------------------------------
// Estimation prudente de préparation
// ---------------------------------------------------------------------------

export interface ReadinessEstimate {
  /** 0..100 — volontairement prudent, plafonné à 90. */
  percent: number;
  label: string;
  /** Nombre de notions de référence utilisées pour le calcul. */
  basis: number;
}

/**
 * Probabilité moyenne de se souvenir des notions du niveau (non vues = 0),
 * minorée de 10 % et plafonnée : ce n'est qu'un indicateur, pas une prédiction de réussite.
 */
export function estimateReadiness(cards: CardState[], referenceItemCount: number, now: Date): ReadinessEstimate {
  const basis = Math.max(referenceItemCount, cards.length, 1);
  const recall = cards.reduce((sum, c) => sum + (c.state === 'review' ? currentRetrievability(c, now) : 0), 0);
  const percent = Math.min(90, Math.round((recall / basis) * 100 * 0.9));
  const label =
    percent < 15 ? 'Début du parcours' : percent < 40 ? 'Bases en construction' : percent < 70 ? 'En bonne voie' : 'Solide sur le contenu étudié';
  return { percent, label, basis };
}
