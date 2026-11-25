import { describe, expect, it } from 'vitest';
import { readFileSync } from 'fs';

/**
 * Cohérence cours ↔ examen : chaque mot testé à l'examen blanc N5 (lecture des kanji, orthographe,
 * vocabulaire en contexte) doit être enseigné dans le parcours N5 ou dans l'onglet Caractères.
 */
const load = (p: string) => JSON.parse(readFileSync(new URL(`../../../content/${p}`, import.meta.url), 'utf8'));

function taught(): Set<string> {
  const out = new Set<string>();
  const walk = (o: unknown) => {
    if (Array.isArray(o)) o.forEach(walk);
    else if (o && typeof o === 'object') {
      const r = o as Record<string, unknown>;
      if (typeof r.slug === 'string' && typeof r.kind === 'string') {
        out.add(String(r.front));
        if (r.reading) out.add(String(r.reading));
      }
      Object.values(r).forEach(walk);
    }
  };
  walk(load('n5/n5.json'));
  walk(load('characters/characters.json'));
  return out;
}

/** Forme conjuguée de l'examen → forme enseignée (dictionnaire poli en 〜ます). */
const LEMMA: Record<string, string> = { 飲みました: '飲みます', しめて: 'しめます', ぬいで: 'ぬぎます', かりました: 'かります', まい: '〜枚（まい）', えん: '円' };

describe('cours alignés sur l’examen blanc N5', () => {
  const words = taught();
  const bank = load('exams/n5-jlpt.json') as { parts: { id: string; questions: { jp?: string; answer: string }[] }[] };
  const part = (id: string) => bank.parts.find((p) => p.id === id)!.questions;

  it('chaque mot de 漢字読み est enseigné', () => {
    const missing = part('kanji_reading').map((q) => /\{\{(.*?)\}\}/.exec(q.jp!)![1]).filter((w) => !words.has(LEMMA[w] ?? w));
    expect(missing).toEqual([]);
  });

  it('chaque mot de 表記 est enseigné', () => {
    const missing = part('orthography').map((q) => LEMMA[q.answer] ?? q.answer).filter((w) => !words.has(w));
    expect(missing).toEqual([]);
  });

  it('chaque réponse de 文脈規定 est enseignée', () => {
    const missing = part('context').map((q) => LEMMA[q.answer] ?? q.answer).filter((w) => !words.has(w));
    expect(missing).toEqual([]);
  });
});

describe('parcours N5 : kana et kanji', () => {
  const n5 = load('n5/n5.json');
  const lessons = (slug: string) => n5.worlds.find((w: { slug: string }) => w.slug === slug).chapters.flatMap((c: { lessons: unknown[] }) => c.lessons);
  const fronts = (slug: string) => lessons(slug).flatMap((l: { items: { kind: string; front: string }[] }) => l.items.filter((i) => i.kind === 'kana').map((i) => i.front));

  it('l’île des katakana couvre les 46 katakana de base, comme celle des hiragana', () => {
    expect(new Set(fronts('n5-w1')).size).toBe(46);
    expect(new Set(fronts('n5-w2')).size).toBe(46);
    expect(fronts('n5-w2').every((k: string) => /^[ァ-ヶ]$/.test(k))).toBe(true);
  });

  it('un kanji seul note son okurigana entre parenthèses (長 : なが(い)), il ne répète pas la lecture du mot', () => {
    const items = lessons('n5-w4').concat(lessons('n5-w7')).flatMap((l: { items: { slug: string; reading: string; romaji: string }[] }) => l.items);
    expect(items.find((i: { slug: string }) => i.slug === 'kanji-nagai')).toMatchObject({ reading: 'なが(い)', romaji: 'naga(i)' });
    for (const p of ['n5/n5.json', 'n4/n4.json', 'n3/n3.json', 'n2/n2.json', 'n1/n1.json', 'characters/characters.json']) {
      const walk = (o: unknown): void => {
        if (Array.isArray(o)) o.forEach(walk);
        else if (o && typeof o === 'object') {
          const r = o as { kind?: string; reading?: string; romaji?: string; kanji?: { kunyomi: string[] } };
          if (r.kind === 'kanji' && r.kanji) {
            // La lecture d'un kanji n'est jamais un kun'yomi dont on aurait fondu l'okurigana.
            expect(r.kanji.kunyomi.some((k) => k.includes('(') && k.replace(/[()]/g, '') === r.reading)).toBe(false);
            expect(r.romaji ?? '').not.toMatch(/^[a-z]+-[a-z]+$/);
          }
          Object.values(r).forEach(walk);
        }
      };
      walk(load(p));
    }
  });
});
