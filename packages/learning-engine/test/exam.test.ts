import { describe, expect, it } from 'vitest';
import { AuthoredExercise, EXAM_N5, EngineItem, createRng, examRecommendations, gradeExam, planExam, planPlacementBlock, placementBlockPassed } from '../src';

const v = (id: string, front: string, reading: string, meaning: string, kind: EngineItem['kind'] = 'vocabulary'): EngineItem => ({ id, kind, front, reading, meaning });
const ITEMS: EngineItem[] = [
  v('a', '猫', 'ねこ', 'chat'), v('b', '犬', 'いぬ', 'chien'), v('c', '鳥', 'とり', 'oiseau'), v('d', '魚', 'さかな', 'poisson'), v('e', '馬', 'うま', 'cheval'),
  v('f', '本', 'ほん', 'livre'), v('g', '水', 'みず', 'eau'), v('h', '駅', 'えき', 'gare'), v('i', '学校', 'がっこう', 'école'), v('j', '今日', 'きょう', 'aujourd’hui'),
  v('k', '山', 'やま', 'montagne', 'kanji'), v('l', '川', 'かわ', 'rivière', 'kanji'), v('m', '日', 'ひ', 'jour', 'kanji'), v('n', '月', 'つき', 'lune', 'kanji'),
  v('o', 'あ', 'あ', 'a', 'kana'), v('p', 'い', 'い', 'i', 'kana'), v('q', 'う', 'う', 'u', 'kana'),
  v('g1', '〜は〜です', '〜は〜です', 'A est B', 'grammar'), v('g2', '〜を〜ます', '〜を〜ます', 'objet', 'grammar'), v('g3', '〜ません', '〜ません', 'négation', 'grammar'),
];
const EX: AuthoredExercise[] = Array.from({ length: 8 }, (_, i) => ({ type: 'particle_choice', prompt: `p${i}`, sentence: 'わたし＿がくせいです。', choices: ['は', 'を', 'に'], answer: 'は', explanation: '…' }));

describe('examen blanc', () => {
  const planned = planExam(EXAM_N5, ITEMS, EX, ITEMS, createRng(1));

  it('respecte la structure en sections', () => {
    const count = (s: string) => planned.filter((p) => p.section === s).length;
    expect(count('vocab')).toBe(12);
    expect(count('grammar')).toBe(10);
    expect(count('listening')).toBe(8);
    expect(planned.every((p) => p.question.type !== 'matching')).toBe(true);
    expect(planned.filter((p) => p.section === 'listening').every((p) => p.question.type === 'listening_choice')).toBe(true);
  });

  it('corrige par section, avec seuil global et seuil par section', () => {
    const qs = planned.map((p) => ({ section: p.section, type: p.question.type, answer: p.question.answer }));
    const perfect = gradeExam(EXAM_N5, qs, qs.map((q) => q.answer));
    expect(perfect).toMatchObject({ percent: 100, passed: true });
    // Tout juste en vocabulaire et grammaire, rien en écoute : 22/30 = 73 % mais section écoute à 0 % → échec
    const noListening = gradeExam(EXAM_N5, qs, qs.map((q) => (q.section === 'listening' ? undefined : q.answer)));
    expect(noListening.percent).toBe(73);
    expect(noListening.passed).toBe(false);
    expect(noListening.weakest).toBe('listening');
    expect(examRecommendations(noListening)[0]).toMatch(/Listening Ninja/);
  });
});

describe('test de positionnement', () => {
  it('propose 3 questions par monde et valide à partir de 2 bonnes réponses', () => {
    const block = planPlacementBlock(ITEMS.slice(0, 6), EX.slice(0, 1), ITEMS, createRng(2));
    expect(block).toHaveLength(3);
    expect(placementBlockPassed(2)).toBe(true);
    expect(placementBlockPassed(1)).toBe(false);
  });
});

describe('examen blanc N4', () => {
  it('est déclaré pour le N4, avec ses propres conseils', async () => {
    const { EXAM_N4, EXAMS, examRecommendations } = await import('../src');
    expect(EXAMS['n4-mock']).toBe(EXAM_N4);
    expect(EXAM_N4.level).toBe('N4');
    const grade = { sections: [{ id: 'grammar' as const, title: '', jpTitle: '', correct: 1, total: 10, percent: 10 }], correct: 1, total: 10, percent: 10, passed: false, weakest: 'grammar' as const };
    expect(examRecommendations(grade, 'N4')[0]).toMatch(/îles 1 à 3/);
    expect(examRecommendations(grade)[0]).toMatch(/mondes 3, 4 et 6/);
  });
});

describe('examen blanc N5 au format officiel (banque)', () => {
  it('tire 67 questions dans les 11 épreuves, toutes en japonais, réponse parmi les choix', async () => {
    const { planBankExam, EXAM_N5_JLPT, bankSections, createRng } = await import('../src');
    const { readFileSync } = await import('fs');
    const bank = JSON.parse(readFileSync(new URL('../../../content/exams/n5-jlpt.json', import.meta.url), 'utf8'));
    const planned = planBankExam(bank, createRng('banque'));
    expect(planned).toHaveLength(67);
    expect(bankSections(bank)).toEqual(Object.fromEntries(EXAM_N5_JLPT.sections.map((s) => [s.id, s.count])));
    for (const { question: q } of planned) {
      expect(q.choices).toContain(q.answer);
      expect(/[぀-ヿ一-龯]/.test(q.prompt)).toBe(true);
    }
    const listening = planned.filter((p) => p.section === 'listening');
    expect(listening.every((p) => p.question.type === 'listening_choice' && p.question.audio && p.question.display?.maxPlays === 2)).toBe(true);
    // Pas deux fois la même question
    expect(new Set(planned.map((p) => JSON.stringify(p.question.display) + p.question.audio)).size).toBe(67);
  });

  it('note sur 180 comme le JLPT : 80 points et minimums par section', async () => {
    const { gradeExam, EXAM_N5_JLPT } = await import('../src');
    const qs = [
      ...Array.from({ length: 49 }, () => ({ section: 'vocab' as const, type: 'particle_choice', answer: 'a' })),
      ...Array.from({ length: 18 }, () => ({ section: 'listening' as const, type: 'listening_choice', answer: 'a' })),
    ];
    // Langue parfaite, écoute nulle : 120/180 mais minimum d'écoute non atteint
    const g1 = gradeExam(EXAM_N5_JLPT, qs, qs.map((q) => (q.section === 'vocab' ? 'a' : 'b')));
    expect(g1.scaled).toEqual({ language: 120, listening: 0, total: 120 });
    expect(g1.passed).toBe(false);
    // 50 % partout : 60 + 30 = 90 → réussi
    const g2 = gradeExam(EXAM_N5_JLPT, qs, qs.map((_, i) => (i % 2 === 0 ? 'a' : 'b')));
    expect(g2.scaled!.total).toBeGreaterThanOrEqual(80);
    expect(g2.passed).toBe(true);
    // 40 % : sous les 80 points
    const g3 = gradeExam(EXAM_N5_JLPT, qs, qs.map((_, i) => (i % 5 < 2 ? 'a' : 'b')));
    expect(g3.passed).toBe(false);
  });
});
