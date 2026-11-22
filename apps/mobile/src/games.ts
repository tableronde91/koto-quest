import type { GameInfoDto } from '@koto/shared';

export const GAME_GLYPH: Record<GameInfoDto['id'], string> = { 'word-rush': 'W', 'kana-rush': 'あ', 'kanji-rush': '速', 'hangul-rush': '한', speed: '走', listening: '耳' };
/** Traduit à l'affichage avec T(). */
export const KIND_HINT: Record<GameInfoDto['id'], string> = { 'word-rush': 'mots', 'kana-rush': 'kana', 'kanji-rush': 'kanji', 'hangul-rush': 'lettres du hangeul', speed: 'notions', listening: 'kana ou mots' };
