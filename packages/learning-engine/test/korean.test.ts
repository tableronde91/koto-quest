import { readFileSync } from 'fs';
import { describe, expect, it } from 'vitest';
import {
  EXAM_TOPIK1,
  EXAM_TOPIK1_MOCK,
  EXAM_TOPIK2,
  EXAM_TOPIK2_MOCK,
  EXAM_TOPIK3,
  EXAM_TOPIK3_MOCK,
  EXAM_TOPIK4,
  EXAM_TOPIK4_MOCK,
  EXAM_TOPIK5,
  EXAM_TOPIK5_MOCK,
  EXAM_TOPIK6,
  EXAM_TOPIK6_MOCK,
  authoredToQuestion,
  bankSections,
  createRng,
  examScale,
  fillBlank,
  generateMatching,
  generateQuestion,
  gradeExam,
  isKorean,
  joinTokens,
  pickDistractors,
  planBankExam,
  planExam,
  planJlptDrill,
  reminderMessage,
  validateAuthoredExercise,
  type AuthoredExercise,
  type EngineItem,
} from '../src';

const json = (p: string) => JSON.parse(readFileSync(new URL(`../../../content/${p}`, import.meta.url), 'utf8'));
const topik1 = json('topik1/topik1.json');
const lessons = topik1.worlds.flatMap((w: { chapters: { lessons: unknown[] }[] }) => w.chapters.flatMap((c) => c.lessons)) as {
  slug: string;
  items: { slug: string; kind: EngineItem['kind']; front: string; reading?: string | null; romaji?: string | null; meaning: string }[];
  exercises: AuthoredExercise[];
}[];
const items: EngineItem[] = lessons.flatMap((l) => l.items).map((it) => ({ id: it.slug, kind: it.kind, front: it.front, reading: it.reading ?? null, romaji: it.romaji ?? null, meaning: it.meaning }));
const authored = lessons.flatMap((l) => l.exercises);

describe('coréen : contenu du TOPIK 1', () => {
  it('chaque exercice rédigé est valide et chaque leçon de grammaire a des exercices', () => {
    for (const ex of authored) expect(validateAuthoredExercise(ex)).toEqual([]);
    const grammarLessons = lessons.filter((l) => l.items.some((i) => i.kind === 'grammar'));
    expect(grammarLessons.length).toBeGreaterThan(15);
    for (const l of grammarLessons) expect(l.exercises.length).toBeGreaterThanOrEqual(4);
  });

  it('le vocabulaire coréen n’a pas de lecture (pas de question « lecture ») mais une romanisation', () => {
    for (const it of items.filter((i) => i.kind === 'vocabulary')) {
      expect(it.reading).toBeNull();
      expect(it.romaji).toBeTruthy();
      expect(isKorean(it.front)).toBe(true);
    }
  });

  it('les lettres du hangeul ont un son prononçable (syllabe) et une romanisation', () => {
    const letters = items.filter((i) => i.kind === 'kana');
    expect(letters.length).toBeGreaterThanOrEqual(40);
    for (const l of letters) {
      expect(isKorean(l.front)).toBe(true);
      expect(l.reading && /[가-힯]/.test(l.reading)).toBe(true);
    }
  });
});

describe('coréen : exercices générés', () => {
  const rng = createRng('ko');
  it('consigne « en coréen » et association « éléments coréens »', () => {
    const word = items.find((i) => i.id === 'ko-hakgyo')!;
    const q = generateQuestion(word, items, 'reverse_choice', rng)!;
    expect(q.prompt).toBe('Comment dit-on « école » en coréen ?');
    expect(q.choices).toContain('학교');
    const m = generateMatching(items.filter((i) => i.kind === 'vocabulary').slice(0, 5), rng)!;
    expect(m.prompt).toBe('Associe chaque élément coréen à son sens.');
  });

  it('les distracteurs d’une lettre restent du même type (voyelle, consonne, syllabe)', () => {
    const a = items.find((i) => i.front === 'ㅏ')!;
    for (let k = 0; k < 10; k++) {
      const d = pickDistractors(a, items, 'front', 3, createRng(`d${k}`));
      expect(d.every((x) => x.codePointAt(0)! >= 0x314f && x.codePointAt(0)! <= 0x3163)).toBe(true);
    }
  });

  it('phrase à remettre dans l’ordre : les segments coréens sont séparés par des espaces', () => {
    expect(joinTokens(['저는', '학교에', '가요.'])).toBe('저는 학교에 가요.');
    expect(joinTokens(['私は', '学校に', '行きます。'])).toBe('私は学校に行きます。');
    const so = authored.find((e) => e.type === 'sentence_order')!;
    const q = authoredToQuestion(so, rng);
    expect(fillBlank(q.answerAudio!, so.answer)).toContain(' ');
  });

  it('phrase à trou : la réponse coréenne est prononcée dans la phrase complète', () => {
    const fb = authored.find((e) => e.type === 'fill_blank' && typeof e.answer === 'string' && isKorean(e.answer))!;
    const q = authoredToQuestion(fb, rng);
    expect(q.answerAudio).toContain('＿');
    expect(fillBlank(q.answerAudio!, fb.answer)).toContain(fb.answer as string);
  });

  it('rappels en coréen', () => {
    const msgs = new Set(Array.from({ length: 10 }, (_, i) => reminderMessage(i, 'ko')));
    expect([...msgs].some((m) => m.includes('coréen') || m.includes('안녕하세요'))).toBe(true);
    expect([...msgs].some((m) => m.includes('japonais') || m.includes('こんにちは'))).toBe(false);
  });
});

describe('Atelier TOPIK', () => {
  it('ne propose que la grammaire et l’écoute, avec des consignes en coréen', () => {
    const grammar = planJlptDrill('grammar', items, authored, items, createRng('g'), new Map(), 'ko');
    expect(grammar.length).toBe(10);
    expect(grammar.every((q) => isKorean(q.prompt))).toBe(true);
    const listening = planJlptDrill('listening', items, authored, items, createRng('l'), new Map(), 'ko');
    expect(listening.length).toBeGreaterThan(3);
    expect(listening.every((q) => q.type === 'listening_choice' && q.audio)).toBe(true);
    expect(planJlptDrill('kanji', items, authored, items, createRng('k'), new Map(), 'ko')).toEqual([]);
  });
});

describe('Examen blanc TOPIK I', () => {
  const bank = json('exams/topik1.json');

  it('tire 30 questions d’écoute et 40 de lecture, en coréen, réponse parmi les choix', () => {
    const planned = planBankExam(bank, createRng('topik'));
    expect(planned).toHaveLength(70);
    expect(bankSections(bank)).toEqual({ listening: 30, reading: 40 });
    expect(EXAM_TOPIK1.sections.map((s) => [s.id, s.count])).toEqual([['listening', 30], ['reading', 40]]);
    for (const { question: q } of planned) {
      expect(q.choices).toContain(q.answer);
      expect(q.choices).toHaveLength(4);
      expect(isKorean(q.prompt)).toBe(true);
    }
    const listening = planned.filter((p) => p.section === 'listening');
    expect(listening).toHaveLength(30);
    expect(listening.every((p) => p.question.type === 'listening_choice' && isKorean(p.question.audio) && p.question.display?.maxPlays === 2)).toBe(true);
    expect(new Set(planned.map((p) => JSON.stringify(p.question.display) + p.question.audio)).size).toBe(70);
  });

  it('note sur 200 comme le TOPIK I : niveau 1 à 80, niveau 2 à 140, sans minimum par épreuve', () => {
    const qs = [
      ...Array.from({ length: 30 }, () => ({ section: 'listening' as const, type: 'listening_choice', answer: 'a' })),
      ...Array.from({ length: 40 }, () => ({ section: 'reading' as const, type: 'particle_choice', answer: 'a' })),
    ];
    const answer = (listening: number, reading: number) => qs.map((q, i) => (q.section === 'listening' ? (i < listening ? 'a' : 'b') : i - 30 < reading ? 'a' : 'b'));
    const none = gradeExam(EXAM_TOPIK1, qs, answer(0, 0));
    expect(none.scaled).toEqual({ language: 0, listening: 0, total: 0, level: 0 });
    expect(none.passed).toBe(false);
    // Lecture parfaite, aucune écoute : 100 points, niveau 1 (pas de minimum par épreuve au TOPIK)
    const readOnly = gradeExam(EXAM_TOPIK1, qs, answer(0, 40));
    expect(readOnly.scaled).toEqual({ language: 100, listening: 0, total: 100, level: 1 });
    expect(readOnly.passed).toBe(true);
    const level2 = gradeExam(EXAM_TOPIK1, qs, answer(24, 32));
    expect(level2.scaled).toMatchObject({ listening: 80, language: 80, total: 160, level: 2 });
    expect(level2.percent).toBe(80);
    expect(examScale(EXAM_TOPIK1)).toMatchObject({ system: 'topik', total: 200, passTotal: 80, levels: [{ level: 1, min: 80 }, { level: 2, min: 140 }] });
    expect(examScale(EXAM_TOPIK1_MOCK)).toBeNull();
  });

  it('l’entraînement TOPIK 1 se compose à partir des leçons', () => {
    const planned = planExam(EXAM_TOPIK1_MOCK, items, authored, items, createRng('mock'));
    expect(planned.filter((p) => p.section === 'vocab')).toHaveLength(12);
    expect(planned.filter((p) => p.section === 'listening')).toHaveLength(8);
    expect(planned.length).toBeGreaterThanOrEqual(28);
  });
});

describe('TOPIK 2 : parcours et examen du niveau 2', () => {
  const topik2 = json('topik2/topik2.json');
  const lessons2 = topik2.worlds.flatMap((w: { chapters: { lessons: unknown[] }[] }) => w.chapters.flatMap((c) => c.lessons)) as typeof lessons;
  const items2: EngineItem[] = lessons2.flatMap((l) => l.items).map((it) => ({ id: it.slug, kind: it.kind, front: it.front, reading: it.reading ?? null, romaji: it.romaji ?? null, meaning: it.meaning }));
  const authored2 = lessons2.flatMap((l) => l.exercises);

  it('8 îles de 3 leçons, chacune avec de la grammaire, des exercices valides et des mots romanisés', () => {
    expect(topik2.level.code).toBe('TOPIK2');
    expect(topik2.worlds.filter((w: { boss?: unknown }) => w.boss)).toHaveLength(8);
    expect(lessons2).toHaveLength(24);
    for (const l of lessons2) {
      expect(l.items.some((i) => i.kind === 'grammar')).toBe(true);
      expect(l.exercises.length).toBeGreaterThanOrEqual(4);
      for (const it of l.items) {
        expect(isKorean(it.front)).toBe(true);
        expect(it.reading ?? null).toBeNull();
        expect(it.romaji).toBeTruthy();
      }
    }
    for (const ex of authored2) expect(validateAuthoredExercise(ex)).toEqual([]);
    // Aucune notion déjà vue au TOPIK 1
    const known = new Set(items.filter((i) => i.kind === 'vocabulary').map((i) => i.front));
    expect(items2.filter((i) => i.kind === 'vocabulary' && known.has(i.front))).toEqual([]);
    expect(topik2.worlds.at(-1)).toMatchObject({ slug: 'topik2-final', exam: EXAM_TOPIK2.slug });
  });

  it('banque du niveau 2 : celle du TOPIK 1 enrichie, même format de 70 questions', () => {
    const bank1 = json('exams/topik1.json');
    const bank2 = json('exams/topik2.json');
    expect(bankSections(bank2)).toEqual({ listening: 30, reading: 40 });
    const count = (b: { parts: { questions: unknown[] }[] }) => b.parts.reduce((n, p) => n + p.questions.length, 0);
    expect(count(bank2)).toBeGreaterThan(count(bank1) + 30);
    const planned = planBankExam(bank2, createRng('topik2'));
    expect(planned).toHaveLength(70);
    for (const { question: q } of planned) expect(q.choices).toContain(q.answer);
  });

  it('l’examen du niveau 2 ne se valide qu’à 140 points', () => {
    const qs = [
      ...Array.from({ length: 30 }, () => ({ section: 'listening' as const, type: 'listening_choice', answer: 'a' })),
      ...Array.from({ length: 40 }, () => ({ section: 'reading' as const, type: 'particle_choice', answer: 'a' })),
    ];
    const answer = (listening: number, reading: number) => qs.map((q, i) => (q.section === 'listening' ? (i < listening ? 'a' : 'b') : i - 30 < reading ? 'a' : 'b'));
    const level1 = gradeExam(EXAM_TOPIK2, qs, answer(15, 20));
    expect(level1.scaled).toMatchObject({ total: 100, level: 1 });
    expect(level1.passed).toBe(false);
    expect(gradeExam(EXAM_TOPIK1, qs, answer(15, 20)).passed).toBe(true);
    const level2 = gradeExam(EXAM_TOPIK2, qs, answer(21, 28));
    expect(level2.scaled).toMatchObject({ total: 140, level: 2 });
    expect(level2.passed).toBe(true);
    expect(examScale(EXAM_TOPIK2)).toMatchObject({ system: 'topik', passLevel: 2 });
    expect(examScale(EXAM_TOPIK1)).toMatchObject({ passLevel: 1 });
    const mock = planExam(EXAM_TOPIK2_MOCK, items2, authored2, items2, createRng('mock2'));
    expect(mock.length).toBeGreaterThanOrEqual(28);
  });
});

describe('TOPIK 3 : premier niveau du TOPIK II', () => {
  const topik3 = json('topik3/topik3.json');
  const lessons3 = topik3.worlds.flatMap((w: { chapters: { lessons: unknown[] }[] }) => w.chapters.flatMap((c) => c.lessons)) as typeof lessons;
  const items3: EngineItem[] = lessons3.flatMap((l) => l.items).map((it) => ({ id: it.slug, kind: it.kind, front: it.front, reading: it.reading ?? null, romaji: it.romaji ?? null, meaning: it.meaning }));

  it('8 îles de 3 leçons, grammaire, exercices valides, vocabulaire nouveau', () => {
    expect(topik3.level).toMatchObject({ code: 'TOPIK3', order: 14 });
    expect(lessons3).toHaveLength(24);
    for (const l of lessons3) {
      expect(l.items.some((i) => i.kind === 'grammar')).toBe(true);
      expect(l.exercises.length).toBeGreaterThanOrEqual(4);
      for (const ex of l.exercises) expect(validateAuthoredExercise(ex)).toEqual([]);
      for (const it of l.items) expect(it.romaji).toBeTruthy();
    }
    const before = new Set([...items, ...json('topik2/topik2.json').worlds.flatMap((w: any) => w.chapters.flatMap((c: any) => c.lessons.flatMap((l: any) => l.items)))].filter((i: any) => i.kind === 'vocabulary').map((i: any) => i.front));
    expect(items3.filter((i) => i.kind === 'vocabulary' && before.has(i.front))).toEqual([]);
    expect(topik3.worlds.at(-1)).toMatchObject({ slug: 'topik3-final', exam: EXAM_TOPIK3.slug });
  });

  it('examen TOPIK II : écoute, écriture et lecture, 25 + 5 + 25 questions en coréen', () => {
    const bank = json('exams/topik3.json');
    expect(bankSections(bank)).toEqual({ listening: 25, writing: 5, reading: 25 });
    expect(EXAM_TOPIK3.sections.map((s) => [s.id, s.count])).toEqual([['listening', 25], ['writing', 5], ['reading', 25]]);
    const planned = planBankExam(bank, createRng('topik3'));
    expect(planned).toHaveLength(55);
    for (const { question: q } of planned) {
      expect(q.choices).toContain(q.answer);
      expect(isKorean(q.prompt)).toBe(true);
    }
  });

  it('noté sur 300 comme le TOPIK II : niveau 3 à 120, 4 à 150, 5 à 190, 6 à 230', () => {
    const qs = [
      ...Array.from({ length: 25 }, () => ({ section: 'listening' as const, type: 'listening_choice', answer: 'a' })),
      ...Array.from({ length: 5 }, () => ({ section: 'writing' as const, type: 'particle_choice', answer: 'a' })),
      ...Array.from({ length: 25 }, () => ({ section: 'reading' as const, type: 'particle_choice', answer: 'a' })),
    ];
    const answer = (l: number, w: number, r: number) => qs.map((q, i) => (q.section === 'listening' ? (i < l ? 'a' : 'b') : q.section === 'writing' ? (i - 25 < w ? 'a' : 'b') : i - 30 < r ? 'a' : 'b'));
    const zero = gradeExam(EXAM_TOPIK3, qs, answer(0, 0, 0));
    expect(zero.scaled).toMatchObject({ total: 0, level: 0 });
    const l3 = gradeExam(EXAM_TOPIK3, qs, answer(10, 2, 10));
    expect(l3.scaled).toMatchObject({ listening: 40, writing: 40, language: 40, total: 120, level: 3 });
    expect(l3.passed).toBe(true);
    const below = gradeExam(EXAM_TOPIK3, qs, answer(10, 1, 10));
    expect(below.scaled).toMatchObject({ total: 100, level: 0 });
    expect(below.passed).toBe(false);
    expect(gradeExam(EXAM_TOPIK3, qs, answer(20, 4, 20)).scaled).toMatchObject({ total: 240, level: 6 });
    expect(examScale(EXAM_TOPIK3)).toMatchObject({ system: 'topik', total: 300, writing: 100, passLevel: 3, levels: [{ level: 3, min: 120 }, { level: 4, min: 150 }, { level: 5, min: 190 }, { level: 6, min: 230 }] });
    const authored3 = lessons3.flatMap((l) => l.exercises);
    expect(planExam(EXAM_TOPIK3_MOCK, items3, authored3, items3, createRng('mock3')).length).toBeGreaterThanOrEqual(28);
  });
});

describe('TOPIK 4 : parcours et examen validé au niveau 4', () => {
  const topik4 = json('topik4/topik4.json');
  const lessons4 = topik4.worlds.flatMap((w: { chapters: { lessons: unknown[] }[] }) => w.chapters.flatMap((c) => c.lessons)) as typeof lessons;
  const items4: EngineItem[] = lessons4.flatMap((l) => l.items).map((it) => ({ id: it.slug, kind: it.kind, front: it.front, reading: it.reading ?? null, romaji: it.romaji ?? null, meaning: it.meaning }));

  it('8 îles de 3 leçons, exercices valides, vocabulaire jamais vu aux niveaux précédents', () => {
    expect(topik4.level).toMatchObject({ code: 'TOPIK4', order: 13 });
    expect(lessons4).toHaveLength(24);
    for (const l of lessons4) {
      expect(l.items.some((i) => i.kind === 'grammar')).toBe(true);
      for (const ex of l.exercises) expect(validateAuthoredExercise(ex)).toEqual([]);
    }
    const levels = ['topik1/topik1.json', 'topik2/topik2.json', 'topik3/topik3.json'].map(json);
    const before = new Set(levels.flatMap((lv: any) => lv.worlds.flatMap((w: any) => w.chapters.flatMap((c: any) => c.lessons.flatMap((l: any) => l.items)))).filter((i: any) => i.kind === 'vocabulary').map((i: any) => i.front));
    expect(items4.filter((i) => i.kind === 'vocabulary' && before.has(i.front))).toEqual([]);
    expect(topik4.worlds.at(-1)).toMatchObject({ slug: 'topik4-final', exam: EXAM_TOPIK4.slug });
  });

  it('banque du TOPIK II enrichie ; 150 points pour valider le niveau 4', () => {
    const bank3 = json('exams/topik3.json');
    const bank4 = json('exams/topik4.json');
    const count = (b: { parts: { questions: unknown[] }[] }) => b.parts.reduce((n, p) => n + p.questions.length, 0);
    expect(count(bank4)).toBeGreaterThanOrEqual(count(bank3) + 30);
    expect(bankSections(bank4)).toEqual({ listening: 25, writing: 5, reading: 25 });
    const qs = [
      ...Array.from({ length: 25 }, () => ({ section: 'listening' as const, type: 'listening_choice', answer: 'a' })),
      ...Array.from({ length: 5 }, () => ({ section: 'writing' as const, type: 'particle_choice', answer: 'a' })),
      ...Array.from({ length: 25 }, () => ({ section: 'reading' as const, type: 'particle_choice', answer: 'a' })),
    ];
    const answer = (l: number, w: number, r: number) => qs.map((q, i) => (q.section === 'listening' ? (i < l ? 'a' : 'b') : q.section === 'writing' ? (i - 25 < w ? 'a' : 'b') : i - 30 < r ? 'a' : 'b'));
    const level3 = gradeExam(EXAM_TOPIK4, qs, answer(10, 2, 10));
    expect(level3.scaled).toMatchObject({ total: 120, level: 3 });
    expect(level3.passed).toBe(false);
    const level4 = gradeExam(EXAM_TOPIK4, qs, answer(13, 2, 12));
    expect(level4.scaled).toMatchObject({ total: 140, level: 3 });
    const pass = gradeExam(EXAM_TOPIK4, qs, answer(15, 2, 12));
    expect(pass.scaled).toMatchObject({ total: 148 });
    const ok = gradeExam(EXAM_TOPIK4, qs, answer(15, 3, 12));
    expect(ok.scaled).toMatchObject({ total: 168, level: 4 });
    expect(ok.passed).toBe(true);
    expect(examScale(EXAM_TOPIK4)).toMatchObject({ total: 300, passLevel: 4 });
    expect(planExam(EXAM_TOPIK4_MOCK, items4, lessons4.flatMap((l) => l.exercises), items4, createRng('mock4')).length).toBeGreaterThanOrEqual(28);
  });
});

describe('TOPIK 5 et 6 : mythes coréens, examens validés aux niveaux 5 et 6', () => {
  const lv = (code: number) => json(`topik${code}/topik${code}.json`);
  const lessonsOf = (l: any) => l.worlds.flatMap((w: any) => w.chapters.flatMap((c: any) => c.lessons)) as typeof lessons;
  const itemsOf = (ls: typeof lessons): EngineItem[] => ls.flatMap((l) => l.items).map((it) => ({ id: it.slug, kind: it.kind, front: it.front, reading: it.reading ?? null, romaji: it.romaji ?? null, meaning: it.meaning }));

  it.each([
    [5, 12, EXAM_TOPIK5],
    [6, 11, EXAM_TOPIK6],
  ])('TOPIK %i : 8 îles de 3 leçons, exercices valides, vocabulaire nouveau', (n, order, exam) => {
    const level = lv(n);
    const ls = lessonsOf(level);
    expect(level.level).toMatchObject({ code: `TOPIK${n}`, order });
    expect(ls).toHaveLength(24);
    for (const l of ls) {
      expect(l.items.some((i) => i.kind === 'grammar')).toBe(true);
      for (const ex of l.exercises) expect(validateAuthoredExercise(ex)).toEqual([]);
    }
    const before = new Set(Array.from({ length: n - 1 }, (_, i) => lv(i + 1)).flatMap((l: any) => lessonsOf(l).flatMap((x) => x.items)).filter((i: any) => i.kind === 'vocabulary').map((i: any) => i.front));
    expect(itemsOf(ls).filter((i) => i.kind === 'vocabulary' && before.has(i.front))).toEqual([]);
    expect(level.worlds.at(-1)).toMatchObject({ slug: `topik${n}-final`, exam: exam.slug });
  });

  it('banques enrichies ; 190 points pour le niveau 5, 230 pour le niveau 6', () => {
    const count = (b: { parts: { questions: unknown[] }[] }) => b.parts.reduce((k, p) => k + p.questions.length, 0);
    const [b4, b5, b6] = [4, 5, 6].map((n) => json(`exams/topik${n}.json`));
    expect(count(b5)).toBeGreaterThan(count(b4));
    expect(count(b6)).toBeGreaterThan(count(b5));
    for (const b of [b5, b6]) expect(bankSections(b)).toEqual({ listening: 25, writing: 5, reading: 25 });
    const qs = [
      ...Array.from({ length: 25 }, () => ({ section: 'listening' as const, type: 'listening_choice', answer: 'a' })),
      ...Array.from({ length: 5 }, () => ({ section: 'writing' as const, type: 'particle_choice', answer: 'a' })),
      ...Array.from({ length: 25 }, () => ({ section: 'reading' as const, type: 'particle_choice', answer: 'a' })),
    ];
    const answer = (l: number, w: number, r: number) => qs.map((q, i) => (q.section === 'listening' ? (i < l ? 'a' : 'b') : q.section === 'writing' ? (i - 25 < w ? 'a' : 'b') : i - 30 < r ? 'a' : 'b'));
    // 168/300 : niveau 4, insuffisant pour le TOPIK 5
    expect(gradeExam(EXAM_TOPIK5, qs, answer(15, 3, 12))).toMatchObject({ passed: false, scaled: { total: 168, level: 4 } });
    const five = gradeExam(EXAM_TOPIK5, qs, answer(20, 3, 20));
    expect(five).toMatchObject({ passed: true, scaled: { total: 220, level: 5 } });
    expect(gradeExam(EXAM_TOPIK6, qs, answer(20, 3, 20))).toMatchObject({ passed: false, scaled: { level: 5 } });
    expect(gradeExam(EXAM_TOPIK6, qs, answer(22, 4, 22))).toMatchObject({ passed: true, scaled: { total: 256, level: 6 } });
    expect(examScale(EXAM_TOPIK5)).toMatchObject({ total: 300, passLevel: 5 });
    expect(examScale(EXAM_TOPIK6)).toMatchObject({ total: 300, passLevel: 6 });
    for (const [n, mock] of [[5, EXAM_TOPIK5_MOCK], [6, EXAM_TOPIK6_MOCK]] as const) {
      const ls = lessonsOf(lv(n));
      const its = itemsOf(ls);
      expect(planExam(mock, its, ls.flatMap((l) => l.exercises), its, createRng(`mock${n}`)).length).toBeGreaterThanOrEqual(28);
    }
  });
});
