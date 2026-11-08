import { describe, expect, it } from 'vitest';
import { DAILY_GAME_COIN_CAP, EngineItem, GAMES, createRng, gameReward, planTimedGame, scoreTimedGame } from '../src';

const k = (id: string, front: string, reading: string, meaning: string): EngineItem => ({ id, kind: 'kanji', front, reading, meaning });
const KANJI = [k('1', '一', 'いち', 'un'), k('2', '二', 'に', 'deux'), k('3', '三', 'さん', 'trois'), k('4', '山', 'やま', 'montagne'), k('5', '川', 'かわ', 'rivière'), k('6', '日', 'ひ', 'jour'), k('7', '月', 'つき', 'lune')];

describe('mini-jeux', () => {
  it('exige assez de notions vues', () => {
    expect(planTimedGame(GAMES['kanji-rush'], KANJI.slice(0, 3), KANJI, createRng(1))).toEqual([]);
  });

  it('prépare une minute de questions sans répéter deux fois de suite la même notion', () => {
    const qs = planTimedGame(GAMES['kanji-rush'], KANJI, KANJI, createRng(2));
    expect(qs.length).toBe(60);
    for (let i = 1; i < qs.length; i++) expect(qs[i].itemId).not.toBe(qs[i - 1].itemId);
    expect(new Set(qs.map((q) => q.type)).size).toBeGreaterThan(1);
  });

  it('ne compte que les bonnes réponses données dans le temps', () => {
    const r = scoreTimedGame(GAMES.speed, [
      { correct: true, atMs: 1000 },
      { correct: false, atMs: 2000 },
      { correct: true, atMs: 61_000 },
      { correct: true, atMs: 70_000 },
    ]);
    expect(r).toEqual({ score: 2, answered: 3 });
  });

  it('plafonne les pièces gagnées en jeu chaque jour', () => {
    expect(gameReward(20, 0)).toEqual({ xp: 40, coins: 4 });
    expect(gameReward(100, 0).xp).toBe(60);
    expect(gameReward(50, DAILY_GAME_COIN_CAP - 2).coins).toBe(2);
    expect(gameReward(50, DAILY_GAME_COIN_CAP).coins).toBe(0);
  });
});
