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
