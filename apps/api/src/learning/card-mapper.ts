import { CardState, CardStateName } from '@koto/learning-engine';
import type { ReviewCard } from '@prisma/client';

export function toCardState(c: Pick<ReviewCard, 'state' | 'stability' | 'difficulty' | 'due' | 'lastReview' | 'reps' | 'lapses' | 'step'>): CardState {
  return {
    state: c.state as CardStateName,
    stability: c.stability,
    difficulty: c.difficulty,
    due: c.due,
    lastReview: c.lastReview,
    reps: c.reps,
    lapses: c.lapses,
    step: c.step,
  };
}

export function fromCardState(s: CardState) {
  return {
    state: s.state,
    stability: s.stability,
    difficulty: s.difficulty,
    due: s.due,
    lastReview: s.lastReview,
    reps: s.reps,
    lapses: s.lapses,
    step: s.step,
  };
}
