import { readFileSync } from 'fs';
import { resolve } from 'path';

/** Mode histoire : chaque île de chaque niveau a son chapitre, en français et en anglais. */
const ROOT = resolve(__dirname, '../../..');
const json = (p: string) => JSON.parse(readFileSync(resolve(ROOT, p), 'utf8'));
const story = json('content/story/story.json');
const LEVELS = ['n5', 'n4', 'n3', 'n2', 'n1', 'topik1', 'topik2', 'topik3', 'topik4', 'topik5', 'topik6', 'a1', 'a2', 'b1', 'b2', 'c1', 'hsk1', 'hsk2', 'hsk3', 'hsk4', 'hsk5', 'hsk6', 'delea1', 'delea2', 'deleb1'];
const filled = (b: { fr?: string; en?: string }) => !!b?.fr?.trim() && !!b?.en?.trim() && b.fr !== b.en;

describe('mode histoire', () => {
  it('une saga par niveau publié, avec héros, prologue et épilogue', () => {
    expect(Object.keys(story.levels)).toEqual(LEVELS.map((l) => l.toUpperCase()));
    for (const saga of Object.values<any>(story.levels)) {
      expect(saga.glyph).toHaveLength(1);
      expect(saga.jp.length).toBeGreaterThan(1);
      expect(saga.color).toMatch(/^#[0-9A-F]{6}$/i);
      for (const k of ['saga', 'hero', 'short', 'prologue', 'epilogue']) expect(filled(saga[k])).toBe(true);
    }
    expect(Object.values<any>(story.levels).map((s) => s.glyph)).toEqual(['侍', '忍', '霊', '陽', '将', '화', '이', '어', '사', '바', '단', 'M', 'R', 'G', 'K', 'E', '信', '兵', '学', '秦', '仙', '丝', 'Ñ', '¡', '¿']);
  });

  it.each(LEVELS)('%s : un chapitre par île, ni plus ni moins', (code) => {
    const level = json(`content/${code}/${code}.json`);
    const chapters = story.levels[code.toUpperCase()].chapters;
    const slugs = level.worlds.map((w: { slug: string }) => w.slug);
    expect(Object.keys(chapters)).toEqual(slugs);
    const titles = new Set<string>();
    for (const slug of slugs) {
      const c = chapters[slug];
      for (const k of ['title', 'intro', 'outro']) expect(filled(c[k])).toBe(true);
      titles.add(c.title.fr);
    }
    expect(titles.size).toBe(slugs.length);
  });

  it('le gardien de chaque île apparaît dans son chapitre', () => {
    for (const code of LEVELS) {
      const level = json(`content/${code}/${code}.json`);
      for (const w of level.worlds) {
        if (!w.boss) continue;
        // Dernier mot du nom du gardien (« Le Kappa de la rivière » → Kappa, « La Grue rivale » → Grue…)
        const key = w.boss.name.split(/[\s’']/).find((word: string) => /^[A-ZÉ]/.test(word) && !/^(Le|La|Les|L)$/.test(word));
        expect({ slug: w.slug, ok: story.levels[code.toUpperCase()].chapters[w.slug].intro.fr.includes(key) }).toEqual({ slug: w.slug, ok: true });
      }
    }
  });
});
