import { describe, expect, it } from 'vitest';
import {
  CardState,
  DEFAULT_OPTIONS,
  intervalForStability,
  masteryOf,
  newCard,
  ratingFromAnswer,
  retrievability,
  schedule,
} from '../src';

const T0 = new Date('2026-01-05T09:00:00Z');
const MIN = 60_000;
const DAY = 86_400_000;
const at = (base: Date, ms: number) => new Date(base.getTime() + ms);
const daysUntilDue = (c: CardState, from: Date) => (c.due.getTime() - from.getTime()) / DAY;

/** Fait réussir une carte jusqu'à sa sortie de la phase d'apprentissage. */
function graduate(rating: 3 | 4 = 3): { card: CardState; now: Date } {
  let card = schedule(newCard(T0), rating, T0);
  let now = T0;
  while (card.state === 'learning') {
    now = card.due;
    card = schedule(card, 3, now);
  }
  return { card, now };
}

describe('formules FSRS', () => {
  it('R vaut 90 % quand le temps écoulé égale la stabilité', () => {
    expect(retrievability(10, 10)).toBeCloseTo(0.9, 5);
    expect(retrievability(0, 10)).toBe(1);
  });

  it('l’intervalle à 90 % de rétention est égal à la stabilité', () => {
    expect(intervalForStability(7, 0.9)).toBeCloseTo(7, 5);
    expect(intervalForStability(7, 0.8)).toBeGreaterThan(7);
    expect(intervalForStability(7, 0.95)).toBeLessThan(7);
  });
});

describe('cartes neuves et étapes d’apprentissage', () => {
  it('une première bonne réponse programme une révision quelques heures plus tard', () => {
    const c = schedule(newCard(T0), 3, T0);
    expect(c.state).toBe('learning');
    expect(c.due.getTime() - T0.getTime()).toBe(240 * MIN);
    expect(c.reps).toBe(1);
    expect(c.lastReview).toEqual(T0);
  });

  it('une erreur ramène la carte 10 minutes plus tard', () => {
    const c = schedule(newCard(T0), 1, T0);
    expect(c.state).toBe('learning');
    expect(c.due.getTime() - T0.getTime()).toBe(10 * MIN);
  });

  it('« Facile » sur une carte neuve la fait passer directement en révision', () => {
    const c = schedule(newCard(T0), 4, T0);
    expect(c.state).toBe('review');
    expect(daysUntilDue(c, T0)).toBeGreaterThanOrEqual(2);
  });

  it('une carte réussie à chaque étape gradue avec un intervalle d’au moins un jour', () => {
    const { card, now } = graduate();
    expect(card.state).toBe('review');
    expect(daysUntilDue(card, now)).toBeGreaterThanOrEqual(1);
  });

  it('la difficulté initiale dépend de la première évaluation', () => {
    const again = schedule(newCard(T0), 1, T0);
    const easy = schedule(newCard(T0), 4, T0);
    expect(again.difficulty).toBeGreaterThan(easy.difficulty);
    expect(again.difficulty).toBeLessThanOrEqual(10);
    expect(easy.difficulty).toBeGreaterThanOrEqual(1);
  });
});

describe('révisions long terme', () => {
  it('les intervalles s’allongent quand l’utilisateur réussit', () => {
    let { card, now } = graduate();
    const intervals: number[] = [];
    for (let i = 0; i < 5; i++) {
      now = card.due;
      card = schedule(card, 3, now);
      intervals.push(Math.round(daysUntilDue(card, now)));
    }
    for (let i = 1; i < intervals.length; i++) expect(intervals[i]).toBeGreaterThan(intervals[i - 1]);
  });

  it('une notion mal maîtrisée revient plus vite qu’une notion bien maîtrisée', () => {
    const { card, now } = graduate();
    const later = card.due;
    const hard = schedule(card, 2, later);
    const good = schedule(card, 3, later);
    const easy = schedule(card, 4, later);
    expect(hard.due.getTime()).toBeLessThan(good.due.getTime());
    expect(good.due.getTime()).toBeLessThan(easy.due.getTime());
    expect(now.getTime()).toBeLessThan(later.getTime());
  });

  it('un oubli fait repasser la carte en réapprentissage, réduit la stabilité et compte un oubli', () => {
    let { card } = graduate();
    for (let i = 0; i < 3; i++) card = schedule(card, 3, card.due);
    const before = card.stability;
    const now = card.due;
    const lapsed = schedule(card, 1, now);
    expect(lapsed.state).toBe('relearning');
    expect(lapsed.lapses).toBe(1);
    expect(lapsed.stability).toBeLessThan(before);
    expect(lapsed.due.getTime() - now.getTime()).toBe(DEFAULT_OPTIONS.relearningStepsMinutes[0] * MIN);
  });

  it('une révision tardive réussie augmente davantage la stabilité (effet d’espacement)', () => {
    const { card } = graduate();
    const onTime = schedule(card, 3, card.due);
    const late = schedule(card, 3, at(card.due, 3 * DAY));
    expect(late.stability).toBeGreaterThan(onTime.stability);
  });

  it('respecte l’intervalle maximum', () => {
    let { card } = graduate(4);
    for (let i = 0; i < 30; i++) card = schedule(card, 4, card.due);
    expect(daysUntilDue(card, card.lastReview!)).toBeLessThanOrEqual(DEFAULT_OPTIONS.maximumIntervalDays);
  });

  it('est une fonction pure (n’altère pas la carte d’origine)', () => {
    const c = newCard(T0);
    const copy = JSON.parse(JSON.stringify(c));
    schedule(c, 3, T0);
    expect(JSON.parse(JSON.stringify(c))).toEqual(copy);
  });

  it('deux utilisateurs avec des performances différentes obtiennent des plannings différents', () => {
    const alice = graduate().card; // réussit tout
    let bob = schedule(newCard(T0), 1, T0); // se trompe souvent
    bob = schedule(bob, 1, bob.due);
    while (bob.state !== 'review') bob = schedule(bob, 3, bob.due);
    expect(bob.difficulty).toBeGreaterThan(alice.difficulty);
    const aliceNext = schedule(alice, 3, alice.due);
    const bobNext = schedule(bob, 3, bob.due);
    expect(daysUntilDue(bobNext, bob.due)).toBeLessThan(daysUntilDue(aliceNext, alice.due));
  });
});

describe('évaluation déduite d’une réponse', () => {
  it('erreur → Again ; lent → Hard ; rapide et connu → Easy ; vrai/faux jamais Easy', () => {
    expect(ratingFromAnswer({ correct: false, responseMs: 1000, reps: 5 })).toBe(1);
    expect(ratingFromAnswer({ correct: true, responseMs: 20_000, reps: 5 })).toBe(2);
    expect(ratingFromAnswer({ correct: true, responseMs: 6000, reps: 5 })).toBe(3);
    expect(ratingFromAnswer({ correct: true, responseMs: 2000, reps: 5 })).toBe(4);
    expect(ratingFromAnswer({ correct: true, responseMs: 2000, reps: 0 })).toBe(3);
    expect(ratingFromAnswer({ correct: true, responseMs: 2000, reps: 5, guessable: true })).toBe(3);
  });
});

describe('statut de maîtrise', () => {
  it('suit le cycle découverte → apprentissage → maîtrisée', () => {
    expect(masteryOf(newCard(T0), T0)).toBe('discovered');
    const first = schedule(newCard(T0), 3, T0);
    expect(masteryOf(first, T0)).toBe('discovered');
    let { card } = graduate();
    expect(['learning', 'mastered']).toContain(masteryOf(card, card.lastReview!));
    while (card.stability < 21) card = schedule(card, 3, card.due);
    expect(masteryOf(card, card.lastReview!)).toBe('mastered');
  });

  it('une carte très en retard devient urgente', () => {
    const { card } = graduate();
    expect(masteryOf(card, at(card.due, 60 * DAY))).toBe('urgent');
  });

  it('une carte souvent oubliée est fragile', () => {
    let { card } = graduate();
    for (let i = 0; i < 2; i++) {
      card = schedule(card, 1, card.due);
      while (card.state !== 'review') card = schedule(card, 3, card.due);
    }
    expect(masteryOf(card, card.lastReview!)).toBe('fragile');
  });
});
