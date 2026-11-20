import type { Mastery } from '@koto/shared';
import { C } from './theme';

/** Libellés traduits à l'affichage avec T(). */
export const MASTERY_LABEL: Record<Mastery, string> = {
  discovered: 'Découverte',
  learning: 'En apprentissage',
  fragile: 'Fragile',
  mastered: 'Maîtrisée',
  urgent: 'À réviser vite',
};

export const MASTERY_COLOR: Record<Mastery, string> = {
  discovered: C.inkSoft,
  learning: '#3A6FD8',
  fragile: C.gold,
  mastered: C.ok,
  urgent: C.ko,
};
