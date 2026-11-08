/**
 * Langue de l'interface. Le français est la langue source : `T('Texte en français')` renvoie
 * la traduction dans la langue choisie. Changer de langue recharge l'application.
 */
import { LOCALES, Translator, interpolate, type Locale, type Vars } from '@koto/shared';
import ui from '../../../content/i18n/en/ui.json';
import engine from '../../../content/i18n/en/engine.json';
import api from '../../../content/i18n/en/api.json';
import content from '../../../content/i18n/en/content.json';

const KEY = 'koto-locale';

function detect(): Locale {
  try {
    const saved = localStorage.getItem(KEY);
    if (saved === 'fr' || saved === 'en') return saved;
  } catch {
    /* stockage indisponible */
  }
  const nav = typeof navigator !== 'undefined' ? navigator.language?.toLowerCase() ?? 'fr' : 'fr';
  return nav.startsWith('fr') ? 'fr' : 'en';
}

export const locale: Locale = detect();
export const DATE_LOCALE = locale === 'en' ? 'en-GB' : 'fr-FR';
export { LOCALES };

export const translator: Translator | null = locale === 'en' ? new Translator([ui, engine, api, content] as Record<string, string>[]) : null;

if (typeof document !== 'undefined') document.documentElement.lang = locale;

/** Texte d'interface (clé = texte français), avec variables `{0}` ou `{nom}`. */
export function T(key: string, vars?: Vars): string {
  return translator ? translator.t(key, vars) : interpolate(key, vars);
}

/** Texte venu des données (cours, messages du serveur). */
export function tr(text: string): string {
  return translator ? translator.tr(text) : text;
}

/** Change de langue et recharge l'application. */
export function setLocale(next: Locale, reload = true) {
  try {
    localStorage.setItem(KEY, next);
  } catch {
    /* stockage indisponible */
  }
  if (reload && next !== locale) window.location.reload();
}
