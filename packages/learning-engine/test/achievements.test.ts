import { describe, expect, it } from 'vitest';
import { ACHIEVEMENTS, EMPTY_ACHIEVEMENT_STATS, achievementProgress, achievementReward, longestStreak, newlyUnlocked } from '../src';

describe('succès', () => {
  it('catalogue cohérent : slugs uniques, cibles positives', () => {
    const slugs = ACHIEVEMENTS.map((a) => a.slug);
    expect(new Set(slugs).size).toBe(slugs.length);
    for (const a of ACHIEVEMENTS) {
      expect(a.target).toBeGreaterThan(0);
      expect(a.glyph.length).toBe(1);
      expect(Object.keys(EMPTY_ACHIEVEMENT_STATS)).toContain(a.metric);
    }
  });

  it('rien au départ, puis débloque uniquement ce qui est atteint et pas encore enregistré', () => {
    expect(newlyUnlocked(EMPTY_ACHIEVEMENT_STATS, [])).toEqual([]);
    const s = { ...EMPTY_ACHIEVEMENT_STATS, lessonsCompleted: 10, perfectLessons: 1 };
    expect(newlyUnlocked(s, []).map((a) => a.slug)).toEqual(['first-lesson', 'ten-lessons', 'first-perfect']);
    expect(newlyUnlocked(s, ['first-lesson', 'first-perfect']).map((a) => a.slug)).toEqual(['ten-lessons']);
  });

  it('un succès débloqué le reste même si la statistique redescend', () => {
    const p = achievementProgress({ ...EMPTY_ACHIEVEMENT_STATS, masteredItems: 3 }, ['mastered-25']);
    const m = p.find((x) => x.def.slug === 'mastered-25')!;
    expect(m.unlocked).toBe(true);
    expect(m.value).toBe(25);
    const k = p.find((x) => x.def.slug === 'mastered-100')!;
    expect(k).toMatchObject({ unlocked: false, value: 3 });
  });

  it('succès propres à chaque langue : hangeul, gardiens coréens, TOPIK et contes pour le coréen', () => {
    const slugs = (lang: 'ja' | 'ko', done: string[] = []) => achievementProgress(EMPTY_ACHIEVEMENT_STATS, done, lang).map((p) => p.def.slug);
    expect(slugs('ja')).toContain('kanji-10');
    expect(slugs('ja')).not.toContain('hangul-10');
    expect(slugs('ko')).toEqual(expect.arrayContaining(['hangul-10', 'hangul-40', 'ko-bosses-8', 'ko-bosses-24', 'topik-passed', 'ko-tales-10']));
    expect(slugs('ko')).not.toContain('kanji-10');
    // Un succès déjà débloqué reste affiché après un changement de langue
    expect(slugs('ko', ['kanji-10'])).toContain('kanji-10');
    const s = { ...EMPTY_ACHIEVEMENT_STATS, masteredHangul: 12, koreanBosses: 8, topikPassed: 1, koreanChapters: 10 };
    expect(newlyUnlocked(s, []).map((a) => a.slug)).toEqual(['hangul-10', 'ko-bosses-8', 'topik-passed', 'ko-tales-10']);
  });

  it('succès propres au japonais : kana, gardiens japonais, JLPT et contes japonais', () => {
    const ja = achievementProgress(EMPTY_ACHIEVEMENT_STATS, [], 'ja').map((p) => p.def.slug);
    expect(ja).toEqual(expect.arrayContaining(['kana-20', 'kana-92', 'ja-bosses-8', 'ja-bosses-24', 'jlpt-passed', 'ja-tales-10', 'kanji-10']));
    expect(achievementProgress(EMPTY_ACHIEVEMENT_STATS, [], 'ko').map((p) => p.def.slug)).not.toContain('kana-20');
    // Autant de succès propres à chaque langue (équilibre japonais / coréen)
    const own = (l: string) => ACHIEVEMENTS.filter((x) => x.language === l).length;
    expect(Math.abs(own('ja') - own('ko'))).toBeLessThanOrEqual(2);
    const s = { ...EMPTY_ACHIEVEMENT_STATS, masteredKana: 25, japaneseBosses: 8, jlptPassed: 1, japaneseChapters: 10 };
    expect(newlyUnlocked(s, []).map((a) => a.slug)).toEqual(['kana-20', 'ja-bosses-8', 'jlpt-passed', 'ja-tales-10']);
  });

  it('récompense selon la rareté', () => {
    const defs = ACHIEVEMENTS.filter((a) => ['first-lesson', 'ten-lessons', 'all-n5-lessons'].includes(a.slug));
    expect(achievementReward(defs)).toEqual({ coins: 10 + 25 + 50, xp: 10 + 30 + 60 });
  });

  it('plus longue série de jours consécutifs (y compris changement de mois)', () => {
    expect(longestStreak([])).toBe(0);
    expect(longestStreak(['2026-01-30', '2026-01-31', '2026-02-01', '2026-02-03', '2026-02-04'])).toBe(3);
    expect(longestStreak(['2026-03-01'])).toBe(1);
  });
});
