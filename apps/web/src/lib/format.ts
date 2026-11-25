import { textLanguage } from '@koto/shared';
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

/**
 * Nature d'une notion dans la langue étudiée : une lettre coréenne est du hangeul (pas un kana)
 * et un caractère chinois lu en pinyin est un hanzi (pas un kanji).
 */
export function kindLabelOf(item: { kind: string; front: string; reading?: string | null }): string {
  if (item.kind === 'kana' && /[\u1100-\u11ff\u3130-\u318f\uac00-\ud7af]/.test(item.front)) return T("Hangeul");
  if (item.kind === 'kanji' && /[a-zA-Zāáǎàēéěèīíǐìōóǒòūúǔùǖǘǚǜü]/.test(item.reading ?? '')) return T("Hanzi");
  return KIND_LABEL[item.kind] ?? item.kind;
}

/** Attribut lang d'un texte dans la langue étudiée : coréen (hangeul), japonais (kana, kanji), chinois (caractères seuls, quand on étudie le chinois) ou anglais (alphabet latin). */
export function langOf(text: unknown): 'ja' | 'ko' | 'en' | 'zh' | 'es' {
  return typeof text === 'string' ? textLanguage(text) : 'ja';
}
