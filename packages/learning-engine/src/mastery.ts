import { CardState, currentRetrievability } from './fsrs';

/**
 * Statut pédagogique d'une notion, tel qu'affiché à l'apprenant.
 *  - discovered : vue pour la première fois
 *  - learning   : en cours de consolidation
 *  - fragile    : souvent oubliée ou jugée difficile
 *  - mastered   : stable sur plusieurs semaines
 *  - urgent     : échéance dépassée et probabilité de rappel faible
 */
export type Mastery = 'discovered' | 'learning' | 'fragile' | 'mastered' | 'urgent';

export const MASTERED_STABILITY_DAYS = 21;
const URGENT_RETRIEVABILITY = 0.75;

export function masteryOf(card: CardState, now: Date): Mastery {
  if (card.state === 'new') return 'discovered';
  if (card.state === 'learning') return card.reps <= 1 ? 'discovered' : 'learning';
  const r = currentRetrievability(card, now);
  if (card.due.getTime() <= now.getTime() && r < URGENT_RETRIEVABILITY) return 'urgent';
  if (card.state === 'relearning') return 'fragile';
  if (card.lapses >= 2 || card.difficulty >= 8) return 'fragile';
  if (card.stability >= MASTERED_STABILITY_DAYS) return 'mastered';
  return 'learning';
}

/** Score de maîtrise 0..100 combinant stabilité (long terme) et récupérabilité (aujourd'hui). */
export function masteryScore(card: CardState, now: Date): number {
  if (card.state === 'new') return 0;
  const longTerm = Math.min(1, Math.log1p(card.stability) / Math.log1p(90));
  const r = card.state === 'review' ? currentRetrievability(card, now) : 0.6;
  return Math.round(100 * longTerm * r);
}

export const MASTERY_LABELS_FR: Record<Mastery, string> = {
  discovered: 'Découverte',
  learning: 'En apprentissage',
  fragile: 'Fragile',
  mastered: 'Maîtrisée',
  urgent: 'Révision urgente',
};
