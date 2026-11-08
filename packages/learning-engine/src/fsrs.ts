/**
 * Planificateur de répétition espacée inspiré de FSRS‑4.5
 * (Free Spaced Repetition Scheduler, J. Ye et al., open-spaced-repetition).
 *
 * Modèle « DSR » : chaque carte possède
 *  - une difficulté D (1..10),
 *  - une stabilité S (en jours : durée pour que la probabilité de rappel tombe à 90 %),
 *  - une récupérabilité R(t) = probabilité de se souvenir après t jours.
 *
 * Les intervalles ne sont donc jamais fixes : ils dépendent de l'historique propre
 * à chaque utilisateur et à chaque carte.
 *
 * Les nouvelles cartes passent d'abord par de courtes « étapes d'apprentissage »
 * (10 min puis 4 h) : c'est ce qui permet au mini-défi « quelques heures plus tard »
 * d'arriver au bon moment.
 */

export type Rating = 1 | 2 | 3 | 4; // Again, Hard, Good, Easy
export const Rating = { Again: 1, Hard: 2, Good: 3, Easy: 4 } as const;

export type CardStateName = 'new' | 'learning' | 'review' | 'relearning';

export interface CardState {
  state: CardStateName;
  /** Stabilité en jours (0 tant que la carte est neuve). */
  stability: number;
  /** Difficulté 1..10 (0 tant que la carte est neuve). */
  difficulty: number;
  due: Date;
  lastReview: Date | null;
  reps: number;
  lapses: number;
  /** Index de l'étape d'apprentissage courante. */
  step: number;
}

export interface SchedulerOptions {
  /** Rétention visée (0.7–0.97). 0.9 = 90 % de chances de se souvenir à l'échéance. */
  desiredRetention: number;
  learningStepsMinutes: number[];
  relearningStepsMinutes: number[];
  maximumIntervalDays: number;
}

export const DEFAULT_OPTIONS: SchedulerOptions = {
  desiredRetention: 0.9,
  learningStepsMinutes: [10, 240],
  relearningStepsMinutes: [15],
  maximumIntervalDays: 365 * 3,
};

/** Paramètres par défaut publiés de FSRS‑4.5. */
export const W = [
  0.4872, 1.4003, 3.7145, 13.8206, 5.1618, 1.2298, 0.8975, 0.031, 1.6474, 0.1367, 1.0461, 2.1072,
  0.0793, 0.3246, 1.587, 0.2272, 2.8755,
] as const;
/** Paramètres de mise à jour à court terme (révisions le même jour), repris de FSRS‑5. */
const W_SHORT_A = 0.5425;
const W_SHORT_B = 0.0912;

const DECAY = -0.5;
const FACTOR = 19 / 81; // garantit R(S, S) = 0.9
const MINUTE = 60_000;
const DAY = 86_400_000;

const clamp = (x: number, lo: number, hi: number) => Math.min(hi, Math.max(lo, x));

export function newCard(now: Date): CardState {
  return { state: 'new', stability: 0, difficulty: 0, due: now, lastReview: null, reps: 0, lapses: 0, step: 0 };
}

/** Probabilité de rappel après `elapsedDays` jours pour une stabilité S. */
export function retrievability(elapsedDays: number, stability: number): number {
  if (stability <= 0) return 0;
  return Math.pow(1 + (FACTOR * Math.max(0, elapsedDays)) / stability, DECAY);
}

/** Récupérabilité actuelle d'une carte (1 si jamais révisée en mode long terme). */
export function currentRetrievability(card: CardState, now: Date): number {
  if (card.state === 'new' || !card.lastReview) return 0;
  return retrievability((now.getTime() - card.lastReview.getTime()) / DAY, card.stability);
}

/** Intervalle (jours) pour que R tombe à la rétention visée. */
export function intervalForStability(stability: number, retention: number): number {
  return (stability / FACTOR) * (Math.pow(retention, 1 / DECAY) - 1);
}

const initStability = (r: Rating) => Math.max(W[r - 1], 0.1);
const initDifficulty = (r: Rating) => clamp(W[4] - (r - 3) * W[5], 1, 10);

function nextDifficulty(d: number, r: Rating): number {
  const delta = d - W[6] * (r - 3);
  // Retour vers la moyenne : évite qu'une carte reste « bloquée » très difficile.
  return clamp(W[7] * initDifficulty(3) + (1 - W[7]) * delta, 1, 10);
}

function recallStability(d: number, s: number, r: number, rating: Rating): number {
  const hardPenalty = rating === 2 ? W[15] : 1;
  const easyBonus = rating === 4 ? W[16] : 1;
  return (
    s *
    (1 + Math.exp(W[8]) * (11 - d) * Math.pow(s, -W[9]) * (Math.exp((1 - r) * W[10]) - 1) * hardPenalty * easyBonus)
  );
}

function forgetStability(d: number, s: number, r: number): number {
  const sf = W[11] * Math.pow(d, -W[12]) * (Math.pow(s + 1, W[13]) - 1) * Math.exp((1 - r) * W[14]);
  return Math.min(sf, s);
}

function shortTermStability(s: number, rating: Rating): number {
  return Math.max(0.1, s * Math.exp(W_SHORT_A * (rating - 3 + W_SHORT_B)));
}

function graduate(card: CardState, now: Date, opts: SchedulerOptions, rating: Rating): CardState {
  let days = Math.round(intervalForStability(card.stability, opts.desiredRetention));
  if (rating === 4) days = Math.max(days, 2);
  days = clamp(days, 1, opts.maximumIntervalDays);
  return { ...card, state: 'review', step: 0, due: new Date(now.getTime() + days * DAY) };
}

function stepTransition(
  card: CardState,
  rating: Rating,
  now: Date,
  steps: number[],
  opts: SchedulerOptions,
): CardState {
  const at = (minutes: number) => new Date(now.getTime() + minutes * MINUTE);
  if (steps.length === 0 || rating === 4) return graduate(card, now, opts, rating);
  switch (rating) {
    case 1:
      return { ...card, step: 0, due: at(steps[0]) };
    case 2: {
      const cur = steps[Math.min(card.step, steps.length - 1)];
      return { ...card, due: at(Math.round(cur * 1.5)) };
    }
    case 3: {
      const next = card.step + 1;
      if (next >= steps.length) return graduate(card, now, opts, rating);
      return { ...card, step: next, due: at(steps[next]) };
    }
  }
  return card;
}

/**
 * Applique une évaluation à une carte et renvoie le nouvel état (fonction pure).
 */
export function schedule(
  card: CardState,
  rating: Rating,
  now: Date,
  opts: SchedulerOptions = DEFAULT_OPTIONS,
): CardState {
  const elapsedDays = card.lastReview ? Math.max(0, (now.getTime() - card.lastReview.getTime()) / DAY) : 0;
  const base = { ...card, reps: card.reps + 1, lastReview: now };

  if (card.state === 'new') {
    const c: CardState = {
      ...base,
      state: 'learning',
      stability: initStability(rating),
      difficulty: initDifficulty(rating),
      step: 0,
    };
    // Une carte neuve réussie démarre à l'étape 0 puis avance comme une carte en apprentissage.
    if (rating === 1) return stepTransition(c, 1, now, opts.learningStepsMinutes, opts);
    if (rating === 2) return stepTransition(c, 2, now, opts.learningStepsMinutes, opts);
    return stepTransition(c, rating, now, opts.learningStepsMinutes, opts);
  }

  if (card.state === 'learning' || card.state === 'relearning') {
    const steps = card.state === 'learning' ? opts.learningStepsMinutes : opts.relearningStepsMinutes;
    const c: CardState = {
      ...base,
      difficulty: nextDifficulty(card.difficulty, rating),
      stability: elapsedDays >= 1
        ? (rating === 1
            ? forgetStability(card.difficulty, card.stability, retrievability(elapsedDays, card.stability))
            : recallStability(card.difficulty, card.stability, retrievability(elapsedDays, card.stability), rating))
        : shortTermStability(card.stability, rating),
    };
    return stepTransition(c, rating, now, steps, opts);
  }

  // Révision « long terme »
  const r = retrievability(elapsedDays, card.stability);
  const difficulty = nextDifficulty(card.difficulty, rating);
  if (rating === 1) {
    const c: CardState = {
      ...base,
      state: 'relearning',
      lapses: card.lapses + 1,
      difficulty,
      stability: Math.max(0.1, forgetStability(card.difficulty, card.stability, r)),
      step: 0,
    };
    return stepTransition(c, 1, now, opts.relearningStepsMinutes, opts);
  }
  const stability = recallStability(card.difficulty, card.stability, r, rating);
  let days = Math.round(intervalForStability(stability, opts.desiredRetention));
  const previous = card.lastReview ? Math.round(elapsedDays) : 0;
  // Ordre logique des boutons : un « bien » ou « facile » ne raccourcit jamais l'intervalle.
  if (rating >= 3) days = Math.max(days, previous + 1);
  days = clamp(days, 1, opts.maximumIntervalDays);
  return { ...base, difficulty, stability, due: new Date(now.getTime() + days * DAY) };
}

/**
 * Convertit une réponse à une question en évaluation FSRS.
 * - erreur → Again
 * - réponse correcte mais très lente → Hard
 * - réponse correcte et rapide sur une carte déjà connue → Easy
 *   (sauf pour les questions où le hasard aide beaucoup, ex. vrai/faux)
 */
export function ratingFromAnswer(input: {
  correct: boolean;
  responseMs: number;
  reps: number;
  guessable?: boolean;
}): Rating {
  if (!input.correct) return 1;
  if (input.responseMs > 15_000) return 2;
  if (!input.guessable && input.reps >= 2 && input.responseMs < 4_000) return 4;
  return 3;
}
