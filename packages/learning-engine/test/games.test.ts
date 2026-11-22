import { describe, expect, it } from 'vitest';
import { DAILY_GAME_COIN_CAP, EngineItem, GAMES, createRng, gameIdsFor, gameReward, planTimedGame, scoreTimedGame } from '../src';

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

  it('Hangeul Rush remplace Kanji Rush pour qui étudie le coréen', () => {
    expect(gameIdsFor('ja')).toEqual(['kana-rush', 'kanji-rush', 'speed', 'listening']);
    expect(gameIdsFor('ko')).toEqual(['hangul-rush', 'speed', 'listening']);
    const h = (id: string, front: string, reading: string, meaning: string): EngineItem => ({ id, kind: 'kana', front, reading, meaning });
    const HANGUL = [h('a', 'ㅏ', '아', 'a'), h('eo', 'ㅓ', '어', 'eo'), h('o', 'ㅗ', '오', 'o'), h('u', 'ㅜ', '우', 'u'), h('eu', 'ㅡ', '으', 'eu'), h('i', 'ㅣ', '이', 'i'), h('ga', '가', '가', 'ga')];
    const qs = planTimedGame(GAMES['hangul-rush'], HANGUL, HANGUL, createRng(3));
    expect(qs.length).toBe(60);
    expect(qs.every((q) => ['meaning_choice', 'reverse_choice'].includes(q.type))).toBe(true);
  });

  it('Kana Rush entraîne les hiragana et katakana dès les premières leçons de japonais', () => {
    const kn = (id: string, front: string, romaji: string): EngineItem => ({ id, kind: 'kana', front, reading: front, meaning: romaji });
    const KANA = [kn('a', 'あ', 'a'), kn('i', 'い', 'i'), kn('u', 'う', 'u'), kn('ka', 'カ', 'ka'), kn('ki', 'キ', 'ki'), kn('ku', 'ク', 'ku'), kn('sa', 'さ', 'sa')];
    expect(planTimedGame(GAMES['kana-rush'], [...KANA, ...KANJI], KANA, createRng(4)).every((q) => KANA.some((x) => x.id === q.itemId))).toBe(true);
    expect(planTimedGame(GAMES['kana-rush'], KANJI, KANJI, createRng(5))).toEqual([]);
  });
});
