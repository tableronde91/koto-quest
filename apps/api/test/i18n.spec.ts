import { readFileSync } from 'fs';
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

const levels = ['content/n5/n5.json', 'content/n4/n4.json'].map(json);
const items: EngineItem[] = [];
const authored: AuthoredExercise[] = [];
for (const lvl of levels)
  for (const w of lvl.worlds)
    for (const c of w.chapters)
      for (const l of c.lessons) {
        for (const it of l.items) items.push({ id: it.slug, kind: it.kind, front: it.front, reading: it.reading ?? null, romaji: it.romaji ?? null, meaning: it.meaning });
        for (const ex of l.exercises ?? []) authored.push(ex);
      }
for (const t of json('content/expressions/expressions.json').themes)
  for (const it of t.expressions) items.push({ id: it.slug, kind: it.kind, front: it.front, reading: it.reading ?? null, romaji: it.romaji ?? null, meaning: it.meaning });

const untranslated = (s: string) => !JP_ONLY.test(s) && FRENCH.test(s) && en.tr(s) === s;

describe('Traduction anglaise', () => {
  it('traduit tous les textes des cours (titres, explications, sens, exemples)', () => {
    const missing = new Set<string>();
    const SKIP = new Set(['slug', 'kind', 'front', 'reading', 'romaji', 'jp', 'audio', 'tokens', 'answer', 'choices', 'type']);
    const walk = (o: unknown, k?: string): void => {
      if (Array.isArray(o)) o.forEach((v) => walk(v, k));
      else if (o && typeof o === 'object') for (const [kk, v] of Object.entries(o)) !SKIP.has(kk) && walk(v, kk);
      else if (typeof o === 'string' && untranslated(o)) missing.add(o);
    };
    for (const f of ['content/n5/n5.json', 'content/n4/n4.json', 'content/exams/n5-jlpt.json', 'content/characters/characters.json', 'content/cosmetics/catalog.json', 'content/expressions/expressions.json']) walk(json(f));
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
      for (const c of q.choices ?? []) if (untranslated(c)) problems.push(`choix : ${c}`);
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
});
