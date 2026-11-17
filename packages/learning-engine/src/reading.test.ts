import { describe, expect, it } from 'vitest';
import { readingReward, readingStates, readingStreak, readingSuggestion, rubySegments, stripRuby } from './reading';

describe('lecture quotidienne', () => {
  const order = ['a-1', 'a-2', 'b-1', 'b-2'];

  it('tous les chapitres sont ouverts dès le départ ; le premier non lu est conseillé', () => {
    expect([...readingStates(order, []).values()]).toEqual(['available', 'available', 'available', 'available']);
    expect(readingSuggestion(order, [])).toBe('a-1');
    // On peut lire dans le désordre : le conseil reste le premier chapitre non lu
    const logs = [{ chapter: 'b-1', dateKey: '2026-11-10' }];
    expect([...readingStates(order, logs).values()]).toEqual(['available', 'available', 'read', 'available']);
    expect(readingSuggestion(order, logs)).toBe('a-1');
    expect(readingSuggestion(order, [...logs, { chapter: 'a-1', dateKey: '2026-11-10' }])).toBe('a-2');
    expect(readingSuggestion(order, order.map((chapter) => ({ chapter, dateKey: '2026-11-10' })))).toBeNull();
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
