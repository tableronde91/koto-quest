import { CardState, currentRetrievability } from './fsrs';

/** Temps moyen estimé par activité (secondes). */
export const SECONDS_PER_REVIEW = 10;
export const SECONDS_PER_NEW_ITEM = 60; // explication + exercices de leçon
export const ITEMS_PER_LESSON = 6;

export interface DailyPlanInput {
  minutesPerDay: number;
  dueCount: number;
  newItemsAvailable: number;
  /** Révisions et nouvelles notions déjà faites aujourd'hui. */
  reviewsDoneToday?: number;
  newItemsDoneToday?: number;
}

export interface DailyPlan {
  reviewLimit: number;
  newItemLimit: number;
  lessonsSuggested: number;
  /** Vrai si l'utilisateur a pris du retard : on réduit les nouveautés au lieu d'empiler. */
  catchUpMode: boolean;
  estimatedMinutes: number;
}

/**
 * Répartit le temps disponible entre révisions et nouvelles notions.
 * En cas de retard, on plafonne les révisions du jour (70 % du temps) et on
 * ralentit les nouveautés : le retard se résorbe sur plusieurs jours au lieu
 * d'imposer une montagne d'exercices.
 */
export function planDailyLoad(input: DailyPlanInput): DailyPlan {
  const budget = Math.max(5, input.minutesPerDay) * 60;
  const maxReviewSec = budget * 0.7;
  const reviewSec = Math.min(input.dueCount * SECONDS_PER_REVIEW, maxReviewSec);
  const reviewLimit = Math.floor(reviewSec / SECONDS_PER_REVIEW);
  const catchUpMode = input.dueCount > reviewLimit;

  let newItems = Math.floor((budget - reviewSec) / SECONDS_PER_NEW_ITEM);
  if (catchUpMode) newItems = Math.floor(newItems / 2);
  newItems = Math.min(newItems, 30, input.newItemsAvailable);
  newItems = Math.max(0, newItems - (input.newItemsDoneToday ?? 0));
  const remainingReviews = Math.max(0, reviewLimit - (input.reviewsDoneToday ?? 0));

  return {
    reviewLimit: remainingReviews,
    newItemLimit: newItems,
    lessonsSuggested: newItems > 0 ? Math.max(1, Math.round(newItems / ITEMS_PER_LESSON)) : 0,
    catchUpMode,
    estimatedMinutes: Math.round((remainingReviews * SECONDS_PER_REVIEW + newItems * SECONDS_PER_NEW_ITEM) / 60),
  };
}

/**
 * Ordonne la file de révision : d'abord ce qui est le plus en train d'être oublié
 * (récupérabilité la plus basse), puis les cartes en apprentissage court.
 */
export function orderReviewQueue<T extends { card: CardState }>(entries: T[], now: Date): T[] {
  const due = entries.filter((e) => e.card.state !== 'new' && e.card.due.getTime() <= now.getTime());
  return due
    .map((e) => ({
      e,
      r: e.card.state === 'review' ? currentRetrievability(e.card, now) : 0.5,
    }))
    .sort((a, b) => a.r - b.r || a.e.card.due.getTime() - b.e.card.due.getTime())
    .map((x) => x.e);
}
