import { describe, expect, it } from 'vitest';
import { CharacterEntry, EngineItem, createRng, newCard, planCharacterPractice, schedule } from '../src';

const kana = (r: string, ch: string): EngineItem => ({ id: `hira-${r}`, kind: 'kana', front: ch, reading: ch, romaji: r, meaning: r });
const ITEMS = [kana('a', 'あ'), kana('i', 'い'), kana('u', 'う'), kana('e', 'え'), kana('o', 'お'), kana('ka', 'か'), kana('ki', 'き'), kana('ku', 'く')];
const NOW = new Date('2026-05-01T10:00:00Z');

describe('pratique des caractères', () => {
  it('introduit les nouveaux caractères dans l’ordre du tableau, deux fois chacun', () => {
    const entries: CharacterEntry[] = ITEMS.map((item) => ({ item, card: null }));
    const plan = planCharacterPractice(entries, ITEMS, NOW, createRng(1), { maxNew: 3 });
    expect(plan.newItemIds).toEqual(['hira-a', 'hira-i', 'hira-u']);
    for (const id of plan.newItemIds) expect(plan.questions.filter((q) => q.itemId === id).length).toBe(2);
    expect(plan.questions[0]).toMatchObject({ itemId: 'hira-a', type: 'meaning_choice' });
  });

  it('fait passer les révisions dues avant les nouveautés', () => {
    const dueCard = schedule(newCard(new Date('2026-04-01T10:00:00Z')), 3, new Date('2026-04-01T10:00:00Z'));
    const entries: CharacterEntry[] = ITEMS.map((item) => ({ item, card: item.id === 'hira-ka' ? dueCard : null }));
    const plan = planCharacterPractice(entries, ITEMS, NOW, createRng(2), { maxItems: 4, maxNew: 3 });
    expect(plan.questions[0].itemId).toBe('hira-ka');
    expect(plan.newItemIds).toHaveLength(3);
  });

  it('n’utilise que le pool fourni pour les distracteurs (pas de mélange d’écritures)', () => {
    const kata: EngineItem = { id: 'kata-a', kind: 'kana', front: 'ア', reading: 'ア', romaji: 'a', meaning: 'a' };
    const plan = planCharacterPractice(ITEMS.map((item) => ({ item, card: null })), ITEMS, NOW, createRng(3));
    const shown = plan.questions.flatMap((q) => q.choices ?? []);
    expect(shown).not.toContain(kata.front);
  });

  it('termine par une association quand il y a assez de caractères', () => {
    const plan = planCharacterPractice(ITEMS.map((item) => ({ item, card: null })), ITEMS, NOW, createRng(4));
    expect(plan.questions.at(-1)?.type).toBe('matching');
  });
});
