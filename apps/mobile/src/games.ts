import { decor, type StudyLanguage } from '@koto/shared';
import type { GameInfoDto } from '@koto/shared';

export const GAME_GLYPH: Record<GameInfoDto['id'], string> = { 'word-rush': 'W', 'kana-rush': 'あ', 'kanji-rush': '速', 'hangul-rush': '한', 'hanzi-rush': '字', speed: '走', listening: '耳' };

/** Glyphe d'un mini-jeu dans la langue étudiée (les jeux communs n'affichent pas de japonais hors japonais). */
export function gameGlyph(id: GameInfoDto['id'], lang: StudyLanguage): string {
  return id === 'speed' || id === 'listening' ? decor(id, lang) : GAME_GLYPH[id];
}
/** Traduit à l'affichage avec T(). */
export const KIND_HINT: Record<GameInfoDto['id'], string> = { 'word-rush': 'mots', 'kana-rush': 'kana', 'kanji-rush': 'kanji', 'hangul-rush': 'lettres du hangeul', 'hanzi-rush': 'caractères', speed: 'notions', listening: 'kana ou mots' };
/** Ce qu'il faut avoir rencontré pour débloquer un jeu ; l'écoute porte sur des kana en japonais, des lettres en coréen, des mots ailleurs. */
export const gameHint = (id: GameInfoDto['id'], lang: string | null | undefined): string =>
  id !== 'listening' ? KIND_HINT[id] : lang === 'ko' ? 'lettres ou mots' : lang === 'en' || lang === 'zh' || lang === 'es' || lang === 'de' ? 'mots' : KIND_HINT.listening;
