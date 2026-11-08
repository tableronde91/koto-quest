import { describe, expect, it } from 'vitest';
import { EngineItem, chooseQuestionType, createRng, generateQuestion, jlptReadingQuestion, jlptWritingQuestion, planJlptDrill, readingTraps, starQuestion, writingTraps, exampleIndex } from '../src';

const v = (id: string, front: string, reading: string, meaning: string): EngineItem => ({ id, kind: 'vocabulary', front, reading, meaning });
const POOL = [v('sensei', '先生', 'せんせい', 'professeur'), v('gakkou', '学校', 'がっこう', 'école'), v('tenki', '天気', 'てんき', 'temps'), v('atarashii', '新しい', 'あたらしい', 'nouveau'), v('yasumi', '休み', 'やすみ', 'congé'), v('kaisha', '会社', 'かいしゃ', 'entreprise')];

describe('format JLPT', () => {
  it('pièges de lecture : voyelle longue, ten-ten, petit っ, ゃゅょ', () => {
    expect(readingTraps('せんせい')).toEqual(expect.arrayContaining(['せんせ', 'ぜんせい']));
    expect(readingTraps('がっこう')).toEqual(expect.arrayContaining(['がこう', 'かっこう', 'がっこ']));
    expect(readingTraps('かいしゃ')).toEqual(expect.arrayContaining(['かいしや', 'がいしゃ']));
    expect(readingTraps('てんき')).toContain('でんき');
    expect(readingTraps('てんき')).not.toContain('てんき');
  });

  it('pièges d’écriture : kanji sosies et okurigana', () => {
    expect(writingTraps('休み', 'やすみ')).toEqual(expect.arrayContaining(['体み', '休すみ']));
    expect(writingTraps('新しい', 'あたらしい')).toEqual(expect.arrayContaining(['親しい', '新い', '新らしい']));
    expect(writingTraps('天気', 'てんき')).toEqual(expect.arrayContaining(['夫気', '天汽']));
  });

  it('漢字読み dans une phrase d’exemple, consigne en japonais, 4 choix uniques', () => {
    const q = jlptReadingQuestion(POOL[2], POOL, createRng('r'), 'きょうは 天気が いいです。')!;
    expect(q.prompt).toBe('＿＿の ことばは ひらがなで どう かきますか。');
    expect(q.display?.jp).toBe('きょうは {{天気}}が いいです。');
    expect(q.choices).toHaveLength(4);
    expect(new Set(q.choices).size).toBe(4);
    expect(q.choices).toContain('てんき');
  });

  it('表記 : le mot est donné en hiragana, la réponse est en kanji', () => {
    const q = jlptWritingQuestion(POOL[3], POOL, createRng('w'))!;
    expect(q.display?.jp).toBe('{{あたらしい}}');
    expect(q.answer).toBe('新しい');
    expect(q.choices!.every((c) => /[一-龯]/.test(c))).toBe(true);
    // Pas de kanji pour un mot en kana
    expect(jlptWritingQuestion(v('x', 'ごはん', 'ごはん', 'repas'), POOL, createRng('w'))).toBeNull();
  });

  it('★ à partir d’une phrase à reconstituer', () => {
    const q = starQuestion({ type: 'sentence_order', prompt: "Remets dans l'ordre : « Je bois du thé. »", answer: ['わたしは', 'おちゃを', 'あつい', 'のみます。'], explanation: 'x' }, createRng('s'))!;
    expect(q.display?.jp).toBe('＿＿ ＿＿ ★ ＿＿');
    expect(q.answer).toBe('あつい');
    expect(q.choices).toHaveLength(4);
  });

  it('progression : jamais de format JLPT à la découverte, souvent une fois la notion installée', () => {
    expect(chooseQuestionType(POOL[0], 0, createRng('a'))).toBe('meaning_choice');
    const rng = createRng('b');
    const types = Array.from({ length: 200 }, () => chooseQuestionType(POOL[0], 6, rng));
    const share = types.filter((t) => t.startsWith('jlpt_')).length / types.length;
    expect(share).toBeGreaterThan(0.4);
    expect(generateQuestion(POOL[0], POOL, 'jlpt_reading', createRng('c'))?.type).toBe('jlpt_reading');
  });

  it('séries de l’atelier JLPT : uniquement à partir de ce qui est appris', () => {
    const ex = exampleIndex(POOL, ['きょうは 天気が いいです。', '先生に ききます。']);
    expect(ex.get('tenki')).toBe('きょうは 天気が いいです。');
    const kanji = planJlptDrill('kanji', POOL, [], POOL, createRng('d'), ex);
    expect(kanji.length).toBe(6);
    expect(kanji.every((q) => q.type === 'jlpt_reading')).toBe(true);
    expect(planJlptDrill('star', POOL, [], POOL, createRng('e'))).toEqual([]);
  });
});
