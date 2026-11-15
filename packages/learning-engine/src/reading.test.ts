import { describe, expect, it } from 'vitest';
import { readingReward, readingStates, readingStreak, rubySegments, stripRuby } from './reading';

describe('lecture quotidienne', () => {
  const order = ['a-1', 'a-2', 'b-1', 'b-2'];

  it('un seul nouveau chapitre par jour, dans l’ordre', () => {
    expect([...readingStates(order, [], '2026-11-10').values()]).toEqual(['available', 'locked', 'locked', 'locked']);
    const today = [{ chapter: 'a-1', dateKey: '2026-11-10' }];
    expect([...readingStates(order, today, '2026-11-10').values()]).toEqual(['read', 'locked', 'locked', 'locked']);
    expect([...readingStates(order, today, '2026-11-11').values()]).toEqual(['read', 'available', 'locked', 'locked']);
    // Après plusieurs jours d'absence, on reprend simplement au chapitre suivant
    expect([...readingStates(order, today, '2026-12-01').values()]).toEqual(['read', 'available', 'locked', 'locked']);
  });

  it('série de jours de lecture', () => {
    const keys = ['2026-11-07', '2026-11-08', '2026-11-09'];
    expect(readingStreak(keys, '2026-11-10')).toEqual({ current: 3, best: 3 });
    expect(readingStreak([...keys, '2026-11-10'], '2026-11-10').current).toBe(4);
    expect(readingStreak(keys, '2026-11-11')).toEqual({ current: 0, best: 3 });
    expect(readingStreak([], '2026-11-11')).toEqual({ current: 0, best: 0 });
  });

  it('récompense et furigana', () => {
    expect(readingReward(2, 2)).toEqual({ xp: 25, coins: 10 });
    expect(readingReward(1, 3)).toEqual({ xp: 20, coins: 5 });
    expect(stripRuby('{大|おお}きなもも')).toBe('大きなもも');
    expect(rubySegments('{山|やま}へ{行|い}く')).toEqual([{ text: '山', ruby: 'やま' }, { text: 'へ' }, { text: '行', ruby: 'い' }, { text: 'く' }]);
  });
});
