import { readFileSync, readdirSync } from 'fs';
import { resolve } from 'path';
import { Translator } from '@koto/shared';
import { authoredToQuestion, createRng, generateQuestion, questionTypesFor, type AuthoredExercise, type EngineItem, type Question } from '@koto/learning-engine';

/**
 * Version anglaise : tout le texte français des contenus et des exercices générés doit avoir
 * une traduction, et chaque réponse traduite doit redevenir la valeur attendue par le serveur.
 */
const ROOT = resolve(__dirname, '../../..');
const json = (p: string) => JSON.parse(readFileSync(resolve(ROOT, p), 'utf8'));
const en = new Translator(['ui', 'engine', 'api', 'content'].map((f) => json(`content/i18n/en/${f}.json`)));
const FRENCH = /[àâçéèêëîïôûùœ«»]|\b(le|la|les|des|du|une|est|et|pour|avec|ce|cette|signifie|quel|quelle|que|comment)\b/i;
const JP_ONLY = /^[\s　-ヿ一-鿿＀-￯0-9０-９.,!?()「」『』…〜・ー/★＿:：;]+$/;

const levels = ['content/n5/n5.json', 'content/n4/n4.json', 'content/n3/n3.json', 'content/n2/n2.json', 'content/n1/n1.json', 'content/topik1/topik1.json', 'content/topik2/topik2.json', 'content/topik3/topik3.json', 'content/topik4/topik4.json', 'content/topik5/topik5.json', 'content/topik6/topik6.json', 'content/a1/a1.json', 'content/a2/a2.json', 'content/b1/b1.json', 'content/b2/b2.json', 'content/c1/c1.json', 'content/hsk1/hsk1.json', 'content/hsk2/hsk2.json', 'content/hsk3/hsk3.json', 'content/hsk4/hsk4.json', 'content/hsk5/hsk5.json', 'content/hsk6/hsk6.json', 'content/delea1/delea1.json', 'content/delea2/delea2.json', 'content/deleb1/deleb1.json', 'content/deleb2/deleb2.json'].map(json);
const items: EngineItem[] = [];
const authored: AuthoredExercise[] = [];
for (const lvl of levels)
  for (const w of lvl.worlds)
    for (const c of w.chapters)
      for (const l of c.lessons) {
        for (const it of l.items) items.push({ id: it.slug, kind: it.kind, front: it.front, reading: it.reading ?? null, romaji: it.romaji ?? null, meaning: it.meaning });
        for (const ex of l.exercises ?? []) authored.push(ex);
      }
for (const t of [...json('content/expressions/expressions.json').themes, ...json('content/expressions/expressions-ko.json').themes, ...json('content/expressions/expressions-en.json').themes, ...json('content/expressions/expressions-zh.json', 'content/expressions/expressions-es.json').themes])
  for (const it of t.expressions) items.push({ id: it.slug, kind: it.kind, front: it.front, reading: it.reading ?? null, romaji: it.romaji ?? null, meaning: it.meaning });

// Espagnol : mots et choix des exercices du DELE, en espagnol (jamais traduits, même s'ils contiennent « la » ou « que »).
const SPANISH = new Set<string>();
for (const it of items) if (/^(es-|gram-es-|esx-)/.test(it.id)) SPANISH.add(it.front);
for (const w of [...json('content/delea1/delea1.json').worlds, ...json('content/delea2/delea2.json').worlds, ...json('content/deleb1/deleb1.json').worlds, ...json('content/deleb2/deleb2.json').worlds])
  for (const c of w.chapters) for (const l of c.lessons) for (const ex of l.exercises ?? []) [...(ex.choices ?? []), ...(Array.isArray(ex.answer) ? ex.answer : [ex.answer])].forEach((x: string) => SPANISH.add(x));

// Pinyin (chinois romanisé avec les tons) : jamais traduit, même s'il contient des voyelles accentuées.
const SYL = '(?:[bpmfdtnlgkhjqxrzcsyw]|zh|ch|sh)?[aeiouüāáǎàēéěèīíǐìōóǒòūúǔùǖǘǚǜ]{1,4}(?:ng|n)?r?';
const PINYIN_WORD = new RegExp(`^(?:${SYL})+$`, 'i');
const isPinyin = (s: string) =>
  /[āáǎàēéěèīíǐìōóǒòūúǔùǖǘǚǜ]/.test(s) && s.replace(/[\p{Script=Han}＿?!.,，。？！:：’'"“”…✓✗-]/gu, ' ').trim().split(/\s+/).every((w) => !w || PINYIN_WORD.test(w));
const untranslated = (s: string) => !JP_ONLY.test(s) && !isPinyin(s) && FRENCH.test(s) && en.tr(s) === s;

describe('Traduction anglaise', () => {
  it('traduit tous les textes des cours (titres, explications, sens, exemples)', () => {
    const missing = new Set<string>();
    const SKIP = new Set(['slug', 'kind', 'front', 'reading', 'romaji', 'jp', 'audio', 'tokens', 'answer', 'choices', 'type']);
    const walk = (o: unknown, k?: string): void => {
      if (Array.isArray(o)) o.forEach((v) => walk(v, k));
      else if (o && typeof o === 'object') for (const [kk, v] of Object.entries(o)) !SKIP.has(kk) && walk(v, kk);
      else if (typeof o === 'string' && untranslated(o)) missing.add(o);
    };
    for (const f of ['content/n5/n5.json', 'content/n4/n4.json', 'content/n3/n3.json', 'content/n2/n2.json', 'content/n1/n1.json', 'content/exams/n5-jlpt.json', 'content/exams/n4-jlpt.json', 'content/exams/n3-jlpt.json', 'content/exams/n2-jlpt.json', 'content/exams/n1-jlpt.json', 'content/characters/characters.json', 'content/cosmetics/catalog.json', 'content/expressions/expressions.json', 'content/topik1/topik1.json', 'content/topik2/topik2.json', 'content/topik3/topik3.json', 'content/topik4/topik4.json', 'content/topik5/topik5.json', 'content/topik6/topik6.json', 'content/exams/topik1.json', 'content/exams/topik2.json', 'content/exams/topik3.json', 'content/exams/topik4.json', 'content/exams/topik5.json', 'content/exams/topik6.json', 'content/characters/hangul.json', 'content/expressions/expressions-ko.json', 'content/a1/a1.json', 'content/exams/a1-toeic.json', 'content/a2/a2.json', 'content/exams/a2-toeic.json', 'content/b1/b1.json', 'content/exams/b1-toeic.json', 'content/b2/b2.json', 'content/exams/b2-toeic.json', 'content/c1/c1.json', 'content/exams/c1-toeic.json', 'content/expressions/expressions-en.json', 'content/hsk1/hsk1.json', 'content/exams/hsk1.json', 'content/hsk2/hsk2.json', 'content/hsk3/hsk3.json', 'content/hsk4/hsk4.json', 'content/hsk5/hsk5.json', 'content/hsk6/hsk6.json', 'content/exams/hsk2.json', 'content/exams/hsk3.json', 'content/exams/hsk4.json', 'content/exams/hsk5.json', 'content/exams/hsk6.json', 'content/characters/hanzi.json', 'content/expressions/expressions-zh.json', 'content/expressions/expressions-es.json']) walk(json(f));
    // Espagnol : les phrases, textes et consignes du DELE sont en espagnol (non traduits) ; seuls les textes français le sont.
    const SKIP_ES = new Set([...SKIP, 'sentence', 'passage', 'text', 'glyph']);
    const walkEs = (o: unknown, skip: Set<string>): void => {
      if (Array.isArray(o)) o.forEach((v) => walkEs(v, skip));
      else if (o && typeof o === 'object') for (const [kk, v] of Object.entries(o)) !skip.has(kk) && walkEs(v, skip);
      else if (typeof o === 'string' && untranslated(o)) missing.add(o);
    };
    walkEs(json('content/delea1/delea1.json'), SKIP_ES);
    walkEs(json('content/exams/delea1.json'), new Set([...SKIP_ES, 'prompt']));
    walkEs(json('content/delea2/delea2.json'), SKIP_ES);
    walkEs(json('content/exams/delea2.json'), new Set([...SKIP_ES, 'prompt']));
    walkEs(json('content/deleb1/deleb1.json'), SKIP_ES);
    walkEs(json('content/exams/deleb1.json'), new Set([...SKIP_ES, 'prompt']));
    walkEs(json('content/deleb2/deleb2.json'), SKIP_ES);
    walkEs(json('content/exams/deleb2.json'), new Set([...SKIP_ES, 'prompt']));
    expect([...missing]).toEqual([]);
  });

  it('les sens des notions restent distincts une fois traduits', () => {
    const byEn = new Map<string, Set<string>>();
    // Un sens traduit ne doit pas non plus coïncider avec un sens laissé tel quel (romaji des kana…)
    for (const it of items) {
      const t = en.tr(it.meaning);
      if (!byEn.has(t)) byEn.set(t, new Set());
      byEn.get(t)!.add(it.meaning);
    }
    const clashes = [...byEn].filter(([, fr]) => fr.size > 1).map(([e, fr]) => `${e} ← ${[...fr].join(' | ')}`);
    expect(clashes).toEqual([]);
  });

  it('exercices générés : consignes et choix traduits, réponses retrouvées après traduction', () => {
    const rng = createRng('i18n');
    const problems: string[] = [];
    const check = (q: Question) => {
      const shown = en.deep(q);
      if (untranslated(q.prompt)) problems.push(`consigne : ${q.prompt}`);
      for (const c of q.choices ?? []) if (untranslated(c) && !SPANISH.has(c)) problems.push(`choix : ${c}`);
      if (q.choices) {
        if (new Set(shown.choices).size !== q.choices.length) problems.push(`choix en double après traduction : ${shown.choices!.join(' / ')}`);
        const picked = shown.choices![q.choices.indexOf(String(q.answer))];
        if (en.answersBack({ answer: picked }).answer !== q.answer) problems.push(`réponse non retrouvée : ${picked} → ${q.answer}`);
      }
      if (q.type === 'matching' && Array.isArray(q.answer)) {
        const back = en.answersBack({ answer: (q.answer as string[]).map((a) => en.tr(a)) }).answer;
        // (les sens affichés des paires viennent de shown.pairs)
        if (JSON.stringify(back) !== JSON.stringify(q.answer)) problems.push(`association non retrouvée : ${q.answer}`);
      }
    };
    for (const it of items) for (const type of questionTypesFor(it)) {
      const q = generateQuestion(it, items, type, rng);
      if (q) check(q);
    }
    for (const ex of authored) check(authoredToQuestion(ex, rng));
    expect(problems.slice(0, 30)).toEqual([]);
  });

  it('motifs : une consigne générée est traduite avec ses variables', () => {
    expect(en.tr('Que signifie « 水 » ?')).toBe('What does “水” mean?');
    expect(en.tr('Comment dit-on « eau » en japonais ?')).toBe('How do you say “water” in Japanese?');
    expect(en.t('Encore {0} points pour la division suivante', [12])).toBe('12 more points to the next division');
    expect(en.t('Plan du jour : jusqu’à {0} révisions et {1} nouvelles notions, environ {2} min.{3}', [5, 3, 10, false])).toBe('Today’s plan: up to 5 reviews and 3 new items, about 10 min.');
  });

  it('appli mobile : chaque texte passé à T() ou plural() a sa traduction anglaise', () => {
    const dict = new Translator(['ui', 'engine', 'api', 'content', 'mobile'].map((f) => json(`content/i18n/en/${f}.json`)));
    const files = (dir: string): string[] =>
      readdirSync(dir, { withFileTypes: true }).flatMap((e) => (e.isDirectory() ? files(resolve(dir, e.name)) : /\.tsx?$/.test(e.name) ? [resolve(dir, e.name)] : []));
    const keys = new Set<string>();
    for (const f of [...files(resolve(ROOT, 'apps/mobile/app')), ...files(resolve(ROOT, 'apps/mobile/src'))]) {
      const src = readFileSync(f, 'utf8').replace(/^\s*(\/\/|\*|\/\*).*$/gm, '');
      for (const m of src.matchAll(/\b(?:T|plural)\(\s*'((?:[^'\\]|\\.)*)'(?:\s*,\s*'((?:[^'\\]|\\.)*)')?(?:\s*,\s*'((?:[^'\\]|\\.)*)')?/g))
        for (const k of m.slice(1)) if (k && /[A-Za-zÀ-ÿ]/.test(k)) keys.add(k);
    }
    // Libellés passés à T() par une table (onglet Caractères, maîtrise, registres)
    for (const k of ['Hiragana', 'Katakana', 'Kanji', 'Expressions', 'Découverte', 'En apprentissage', 'Fragile', 'Maîtrisée', 'À réviser vite', 'Poli', 'Neutre', 'Familier', 'Formel', 'Courant', 'Rare', 'Épique', 'Courts', 'Longs', 'Chignon', 'En pétard', 'Carré', 'Rasés', 'Ronds', 'Rieurs', 'Sereins', 'Noir', 'Châtain', 'Roux', 'Blond', 'Gris', 'Bleu', 'Étude', 'Régularité', 'Maîtrise', 'Aventure', 'Jeux et collection', 'Maître du Koto', 'Sensei en herbe', 'Gardien·ne des kanji', 'Lame des kana', 'Voyageur·se des îles', 'Apprenti·e du dojo', 'Vocabulaire', 'Grammaire', 'En fleur', 'En pousse', 'Graines', 'Feuilles fragiles', 'À arroser vite']) keys.add(k);
    expect(keys.size).toBeGreaterThan(150);
    expect([...keys].filter((k) => !dict.has(k))).toEqual([]);
  });
});
