import { describe, expect, it } from 'vitest';
import { existsSync, readFileSync, readdirSync } from 'fs';
import { createRng, generateQuestion, normalizeAnswer, questionTypesFor, soundKey, type EngineItem, type QuestionType } from '../src';

/**
 * Passe en revue les questions générées pour toutes les notions de tous les niveaux (cinq langues) :
 * une seule bonne réponse possible, y compris à l'oreille, et une consigne dans la bonne langue.
 */
const root = new URL('../../../content/', import.meta.url);
const load = (p: string) => JSON.parse(readFileSync(new URL(p, root), 'utf8'));

function itemsOf(o: unknown, out: EngineItem[] = [], seen = new Set<string>()): EngineItem[] {
  if (Array.isArray(o)) o.forEach((x) => itemsOf(x, out, seen));
  else if (o && typeof o === 'object') {
    const r = o as Record<string, unknown>;
    if (typeof r.slug === 'string' && typeof r.kind === 'string' && typeof r.front === 'string' && !seen.has(r.slug)) {
      seen.add(r.slug);
      out.push({ id: r.slug, kind: r.kind as EngineItem['kind'], front: r.front, reading: r.reading as string | null, romaji: r.romaji as string | null, meaning: r.meaning as string });
    }
    Object.values(r).forEach((x) => itemsOf(x, out, seen));
  }
  return out;
}

const LEVELS = readdirSync(root).filter((d) => existsSync(new URL(`${d}/${d}.json`, root)) && Array.isArray(load(`${d}/${d}.json`).worlds));
const SOURCES = [...LEVELS.map((d) => `${d}/${d}.json`), 'characters/characters.json', 'characters/hangul.json', 'characters/hanzi.json'];
const japanese = (file: string) => /^n\d\//.test(file) || file === 'characters/characters.json';

describe('questions générées sur tout le contenu', () => {
  it('couvre les six langues', () => {
    expect(LEVELS.length).toBe(30);
  });

  it('une seule bonne réponse, même à l’oreille, et la consigne nomme la bonne langue', { timeout: 120_000 }, () => {
    const problems: string[] = [];
    for (const file of SOURCES) {
      const items = itemsOf(load(file));
      for (const item of items) {
        const types: QuestionType[] = [...questionTypesFor(item), 'jlpt_reading', 'jlpt_writing'];
        for (const type of types) {
          for (let s = 0; s < 4; s++) {
            const q = generateQuestion(item, items, type, createRng(`${item.id}-${type}-${s}`));
            if (!q) continue;
            const ch = q.choices ?? [];
            const answer = String(q.answer);
            const at = `${file} ${item.front} ${q.type}`;
            if (!ch.includes(answer)) problems.push(`${at} : réponse absente des choix`);
            if (new Set(ch.map(normalizeAnswer)).size !== ch.length) problems.push(`${at} : choix en double`);
            if (!japanese(file) && /kanji|japonais|\bkana\b/i.test(q.prompt + q.explanation)) problems.push(`${at} : consigne japonaise « ${q.prompt} »`);
            if (q.type === 'listening_choice') {
              // Un autre choix se prononce comme la bonne réponse (他 / 她, 来ます / 着ます, ㅐ / ㅔ, お / を)
              const key = item.kind === 'kana' ? 'front' : 'meaning';
              const twin = items.find((o) => o.id !== item.id && soundKey(o) === soundKey(item) && o[key] !== answer && ch.includes(o[key]));
              if (twin) problems.push(`${at} : ${twin.front} se prononce pareil`);
            }
            if (q.type === 'jlpt_writing') {
              const twin = items.find((o) => o.id !== item.id && o.reading === item.reading && o.front !== answer && ch.includes(o.front));
              if (twin) problems.push(`${at} : ${twin.front} s’écrit aussi ${item.reading}`);
            }
          }
        }
      }
    }
    expect(problems.slice(0, 20)).toEqual([]);
  });

  it('homophones : 他 et 她 (tā), 来ます et 着ます (きます), ㅐ et ㅔ, お et を ont la même clé sonore', () => {
    const k = (kind: EngineItem['kind'], front: string, reading: string | null = null) => soundKey({ kind, front, reading });
    expect(k('vocabulary', '他', 'tā')).toBe(k('vocabulary', '她', 'tā'));
    expect(k('vocabulary', '来ます', 'きます')).toBe(k('vocabulary', '着ます', 'きます'));
    expect(k('kana', 'ㅔ', '에')).toBe(k('kana', 'ㅐ', '애'));
    expect(k('kana', 'を', 'を')).toBe(k('kana', 'お', 'お'));
    expect(k('kanji', '長', 'なが(い)')).toBe(k('vocabulary', '長い', 'ながい'));
    expect(k('vocabulary', '他', 'tā')).not.toBe(k('vocabulary', '大', 'dà'));
  });
});
