import type { GameInfoDto } from '@koto/shared';

export const GAME_GLYPH: Record<GameInfoDto['id'], string> = { 'word-rush': 'W', 'kana-rush': 'あ', 'kanji-rush': '速', 'hangul-rush': '한', 'hanzi-rush': '字', speed: '走', listening: '耳' };
/** Traduit à l'affichage avec T(). */
export const KIND_HINT: Record<GameInfoDto['id'], string> = { 'word-rush': 'mots', 'kana-rush': 'kana', 'kanji-rush': 'kanji', 'hangul-rush': 'lettres du hangeul', 'hanzi-rush': 'caractères', speed: 'notions', listening: 'kana ou mots' };
