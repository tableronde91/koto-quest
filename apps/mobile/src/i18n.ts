import { useSyncExternalStore } from 'react';
import { Platform } from 'react-native';
import * as SecureStore from 'expo-secure-store';
import { LOCALES, Translator, interpolate, type Locale, type Vars } from '@koto/shared';
import ui from '../../../content/i18n/en/ui.json';
import engine from '../../../content/i18n/en/engine.json';
import api from '../../../content/i18n/en/api.json';
import content from '../../../content/i18n/en/content.json';
import mobile from '../../../content/i18n/en/mobile.json';

/**
 * Langue de l'appli mobile, comme sur le web : le français est la langue source, `T("…")`
 * renvoie sa traduction. Les dictionnaires sont ceux du web (content/i18n/en), plus
 * `mobile.json` pour les textes propres au téléphone. Changer de langue redessine l'appli.
 */
const KEY = 'koto-locale';
let current: Locale = 'fr';
let english: Translator | null = null;
/** Langue choisie explicitement sur ce téléphone (sinon, elle suit celle du compte). */
let chosen = false;
/** Écran à rouvrir après le changement de langue (l'appli est redessinée). */
let returnTo: string | null = null;
const listeners = new Set<() => void>();

export { LOCALES };
export type { Locale };

function deviceLocale(): Locale {
  let tag = 'fr';
  try {
    tag = (Platform.OS === 'web' ? globalThis.navigator?.language : Intl.DateTimeFormat().resolvedOptions().locale) ?? 'fr';
  } catch {
    /* langue inconnue : français */
  }
  return tag.toLowerCase().startsWith('fr') ? 'fr' : 'en';
}

async function readSaved(): Promise<Locale | null> {
  try {
    const v = Platform.OS === 'web' ? globalThis.localStorage?.getItem(KEY) : await SecureStore.getItemAsync(KEY);
    return v === 'fr' || v === 'en' ? v : null;
  } catch {
    return null;
  }
}

async function save(l: Locale) {
  try {
    if (Platform.OS === 'web') globalThis.localStorage?.setItem(KEY, l);
    else await SecureStore.setItemAsync(KEY, l);
  } catch {
    /* stockage indisponible : le choix vaut pour cette utilisation */
  }
}

function apply(l: Locale) {
  current = l;
  if (l === 'en') english ??= new Translator([ui, engine, api, content, mobile] as Record<string, string>[]);
  listeners.forEach((f) => f());
}

/** Au démarrage : choix enregistré sur le téléphone, sinon langue du téléphone. Renvoie true si un choix existait. */
export async function initLocale(): Promise<boolean> {
  const saved = await readSaved();
  chosen = saved !== null;
  apply(saved ?? deviceLocale());
  return chosen;
}

export async function setLocale(l: Locale, from?: string) {
  chosen = true;
  await save(l);
  if (l !== current) {
    returnTo = from ?? null;
    apply(l);
  }
}

/** Connecté : sans choix fait sur ce téléphone, on adopte la langue enregistrée sur le compte. */
export function followAccount(l: Locale | undefined) {
  if (!l || chosen || l === current) return;
  chosen = true;
  apply(l);
}

/** Écran où l'on était au moment du changement de langue (lu une seule fois). */
export function takeReturnPath(): string | null {
  const p = returnTo;
  returnTo = null;
  return p;
}

export const getLocale = () => current;
export const translator = () => (current === 'en' ? english : null);
export const dateLocale = () => (current === 'en' ? 'en-GB' : 'fr-FR');

export function useLocale(): Locale {
  return useSyncExternalStore(
    (f) => {
      listeners.add(f);
      return () => listeners.delete(f);
    },
    () => current,
  );
}

/** Texte d'interface (clé = texte français), avec variables `{0}` ou `{nom}`. */
export function T(key: string, vars?: Vars): string {
  const t = translator();
  return t ? t.t(key, vars) : interpolate(key, vars);
}

/** Texte venu des données (cours, récit). */
export function tr(text: string): string {
  const t = translator();
  return t ? t.tr(text) : text;
}

/** Choisit la version d'un texte rédigé dans les deux langues. */
export const bi = (v: { fr: string; en: string }) => (current === 'en' ? v.en || v.fr : v.fr);

/** Accord simple : « 1 pièce », « 3 pièces » ; en anglais via la traduction de chaque forme. */
export const plural = (n: number, one: string, many: string, vars?: Vars) => T((current === 'en' ? n !== 1 : n > 1) ? many : one, vars ?? [n]);
