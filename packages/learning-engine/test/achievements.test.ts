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
