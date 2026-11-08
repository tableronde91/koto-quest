import { describe, expect, it } from 'vitest';
import { DUEL_RULES, DUEL_TIERS, botAnswer, createRng, duelDamage, duelOutcome, duelRank, eloDelta, planDuelQuestions, type EngineItem } from './index';

const items: EngineItem[] = [
  ['水', 'みず', 'eau'], ['火', 'ひ', 'feu'], ['山', 'やま', 'montagne'], ['川', 'かわ', 'rivière'], ['先生', 'せんせい', 'professeur'],
  ['学生', 'がくせい', 'étudiant'], ['猫', 'ねこ', 'chat'], ['犬', 'いぬ', 'chien'], ['本', 'ほん', 'livre'], ['車', 'くるま', 'voiture'],
].map(([front, reading, meaning], i) => ({ id: `v${i}`, kind: 'vocabulary' as const, front, reading, meaning }));

describe('duel', () => {
  it('plus on répond vite, plus on frappe fort', () => {
    const fast = duelDamage(true, 1500).damage;
    const mid = duelDamage(true, 5000).damage;
    const slow = duelDamage(true, 9800).damage;
    expect(fast).toBeGreaterThan(mid);
    expect(mid).toBeGreaterThan(slow);
    expect(slow).toBeGreaterThanOrEqual(DUEL_RULES.minDamage);
    expect(duelDamage(true, 1500).critical).toBe(true);
    expect(duelDamage(false, 500).damage).toBe(0);
    expect(duelDamage(true, DUEL_RULES.roundMs + DUEL_RULES.graceMs + 1).damage).toBe(0);
  });

  it('les bonnes réponses enchaînées ajoutent un combo plafonné', () => {
    expect(duelDamage(true, 5000, 2).damage - duelDamage(true, 5000, 0).damage).toBe(4);
    expect(duelDamage(true, 5000, 20).damage - duelDamage(true, 5000, 0).damage).toBe(DUEL_RULES.comboMax);
  });

  it('fin de duel par K.-O. ou aux points', () => {
    expect(duelOutcome(40, 0, 5)).toBe('p1');
    expect(duelOutcome(0, 0, 5)).toBe('draw');
    expect(duelOutcome(40, 30, 5)).toBeNull();
    expect(duelOutcome(40, 30, DUEL_RULES.rounds)).toBe('p1');
    expect(duelOutcome(30, 30, DUEL_RULES.rounds)).toBe('draw');
  });

  it('Elo : battre plus fort que soi rapporte plus', () => {
    const [even] = eloDelta(1000, 1000, 1);
    const [upset] = eloDelta(1000, 1300, 1);
    expect(even).toBe(16);
    expect(upset).toBeGreaterThan(even);
    expect(eloDelta(1300, 1000, 1)[0]).toBeGreaterThanOrEqual(4);
    expect(eloDelta(1000, 1000, 0)).toEqual([-16, 16]);
  });

  it('rangs et divisions', () => {
    expect(duelRank(1000).label).toBe('Ashigaru III');
    expect(duelRank(1080).label).toBe('Ashigaru I');
    expect(duelRank(1100).tier.id).toBe('samurai');
    expect(duelRank(1249).label).toBe('Samouraï I');
    expect(duelRank(1800)).toMatchObject({ division: null, next: null });
    expect(duelRank(700).label).toBe('Ashigaru III');
    for (let i = 1; i < DUEL_TIERS.length; i++) expect(DUEL_TIERS[i].min).toBeGreaterThan(DUEL_TIERS[i - 1].min);
  });

  it('questions de duel : QCM, sans écoute', () => {
    const qs = planDuelQuestions(items, items, createRng('d'));
    expect(qs).toHaveLength(DUEL_RULES.rounds);
    for (const q of qs) {
      expect(q.choices!.length).toBeGreaterThanOrEqual(3);
      expect(q.type).not.toBe('listening_choice');
      expect(q.choices).toContain(q.answer);
    }
  });

  it('adversaire simulé : déterministe, plus fort quand mieux classé', () => {
    expect(botAnswer('x', 1, 1000)).toEqual(botAnswer('x', 1, 1000));
    const rate = (r: number) => Array.from({ length: 400 }, (_, i) => botAnswer(`s${i}`, 1, r)).filter((a) => a.correct).length;
    expect(rate(1600)).toBeGreaterThan(rate(900));
  });
});
