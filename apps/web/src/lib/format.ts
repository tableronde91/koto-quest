import type { Mastery } from '@koto/shared';
import { T } from '../i18n';

export const MASTERY_LABEL: Record<Mastery, string> = {
  discovered: T("Découverte"),
  learning: T("En apprentissage"),
  fragile: T("Fragile"),
  mastered: T("Maîtrisée"),
  urgent: T("À réviser vite"),
};

export const MASTERY_COLOR: Record<Mastery, string> = {
  discovered: 'var(--ink-soft)',
  learning: 'var(--focus)',
  fragile: 'var(--gold)',
  mastered: 'var(--ok)',
  urgent: 'var(--ko)',
};

export const minutesToHHMM = (m: number) => `${String(Math.floor(m / 60)).padStart(2, '0')}:${String(m % 60).padStart(2, '0')}`;
export const hhmmToMinutes = (s: string) => {
  const [h, m] = s.split(':').map(Number);
  return h * 60 + (m || 0);
};

export function formatDuration(seconds: number) {
  const m = Math.round(seconds / 60);
  if (m < 1) return seconds > 0 ? T("moins d’une minute") : '0 min';
  if (m < 60) return T("{0} min", [m]);
  return `${Math.floor(m / 60)} h ${String(m % 60).padStart(2, '0')}`;
}

export const KIND_LABEL: Record<string, string> = { kana: T("Kana"), vocabulary: T("Vocabulaire"), kanji: T("Kanji"), grammar: T("Grammaire") };
