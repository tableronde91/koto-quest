import type { GameInfoDto } from '@koto/shared';

export const GAME_GLYPH: Record<GameInfoDto['id'], string> = { 'kanji-rush': '速', speed: '走', listening: '耳' };
/** Traduit à l'affichage avec T(). */
export const KIND_HINT: Record<GameInfoDto['id'], string> = { 'kanji-rush': 'kanji', speed: 'notions', listening: 'kana ou mots' };
