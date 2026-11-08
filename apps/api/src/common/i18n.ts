import { readFileSync } from 'fs';
import { resolve } from 'path';
import { Translator, interpolate, type Locale } from '@koto/shared';

/** Dictionnaires partagés avec l'application (content/i18n). Le français reste la langue source. */
const DIR = resolve(__dirname, '../../../../content/i18n/en');
let en: Translator | null = null;

function english(): Translator {
  en ??= new Translator(['ui', 'engine', 'api', 'content'].map((f) => JSON.parse(readFileSync(resolve(DIR, `${f}.json`), 'utf8')) as Record<string, string>));
  return en;
}

export const asLocale = (v: unknown): Locale => (typeof v === 'string' && v.toLowerCase().startsWith('en') ? 'en' : 'fr');

/** Traduit un texte destiné à sortir du serveur sans passer par l'application (push, e-mail). */
export function serverText(text: string, locale: Locale): string {
  return locale === 'en' ? english().tr(text) : text;
}

/** Texte à variables écrit côté serveur (clé = gabarit français). */
export function serverT(key: string, vars: Record<string, unknown> | unknown[], locale: Locale): string {
  return locale === 'en' ? english().t(key, vars) : interpolate(key, vars);
}
