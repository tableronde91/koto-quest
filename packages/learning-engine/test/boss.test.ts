import { describe, expect, it } from 'vitest';
import { AuthoredExercise, BOSS_RULES, EngineItem, bossReward, createRng, planBossFight, simulateBoss } from '../src';

const v = (id: string, front: string, reading: string, meaning: string): EngineItem => ({ id, kind: 'vocabulary', front, reading, meaning });
const ITEMS = [v('a', '猫', 'ねこ', 'chat'), v('b', '犬', 'いぬ', 'chien'), v('c', '鳥', 'とり', 'oiseau'), v('d', '魚', 'さかな', 'poisson'), v('e', '馬', 'うま', 'cheval'), v('f', '本', 'ほん', 'livre')];
const EX: AuthoredExercise[] = [
  { type: 'particle_choice', prompt: '?', sentence: 'わたし＿がくせいです。', choices: ['は', 'を'], answer: 'は', explanation: '…' },
  { type: 'sentence_order', prompt: '?', answer: ['わたしは', 'がくせい', 'です。'], explanation: '…' },
  { type: 'fill_blank', prompt: '?', sentence: 'ねこ', choices: ['neko', 'inu'], answer: 'neko', explanation: '…' },
];

describe('combats de boss', () => {
  it('gagne quand les HP du boss tombent à zéro, perd après 3 erreurs', () => {
    expect(simulateBoss(Array(9).fill(true))).toMatchObject({ state: 'won', hits: 9, heartsLeft: 3 });
    expect(simulateBoss([true, false, false, true, false])).toMatchObject({ state: 'lost', hits: 2, heartsLeft: 0, counted: 5 });
    expect(simulateBoss([true, false, true])).toMatchObject({ state: 'ongoing', hits: 2, heartsLeft: 2 });
  });

  it('ignore les réponses données après la fin du combat', () => {
    const r = simulateBoss([false, false, false, true, true]);
    expect(r).toMatchObject({ state: 'lost', hits: 0, counted: 3 });
  });

  it('assez de questions pour gagner même avec 2 erreurs, difficulté croissante', () => {
    const qs = planBossFight(ITEMS, EX, ITEMS, createRng(1));
    expect(qs).toHaveLength(BOSS_RULES.questions);
    expect(BOSS_RULES.questions).toBeGreaterThanOrEqual(BOSS_RULES.hp + BOSS_RULES.hearts - 1);
    expect(qs[0].type).toBe('meaning_choice');
    // Les exercices rédigés arrivent à la fin
    const lastTypes = qs.slice(-3).map((q) => q.type);
    expect(lastTypes.some((t) => ['particle_choice', 'sentence_order', 'fill_blank'].includes(t))).toBe(true);
  });

  it('récompense surtout la première victoire', () => {
    expect(bossReward(true, true).xp).toBeGreaterThan(bossReward(true, false).xp * 5);
    expect(bossReward(false, false).coins).toBe(0);
  });
});
