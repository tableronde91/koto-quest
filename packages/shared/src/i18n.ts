/**
 * Traductions de Koto Quest.
 *
 * Le français est la langue source : chaque texte sert lui-même de clé (à la gettext).
 * Un dictionnaire associe le texte français à sa traduction ; les clés peuvent contenir
 * des variables `{nom}` ou `{0}`, ce qui permet aussi de traduire des phrases générées
 * (« Que signifie « 水 » ? » → « What does "水" mean? »). Un texte sans traduction reste en français.
 */

export type Locale = 'fr' | 'en';

export const LOCALES: { code: Locale; label: string; short: string }[] = [
  { code: 'fr', label: 'Français', short: 'FR' },
  { code: 'en', label: 'English', short: 'EN' },
];

export type Dictionary = Record<string, string>;
export type Vars = Record<string, unknown> | unknown[];

const PLACEHOLDER = /\{(\w+)\}/g;
const HAS_PLACEHOLDER = /\{\w+\}/;
const LETTERS = /[A-Za-zÀ-ÿ]/;

export function interpolate(template: string, vars?: Vars): string {
  if (!vars) return template;
  return template.replace(PLACEHOLDER, (m, k: string) => {
    if (!Array.isArray(vars) && !(k in vars)) return m;
    const v = Array.isArray(vars) ? vars[Number(k)] : (vars as Record<string, unknown>)[k];
    // Comme React : false, null et undefined n'affichent rien
    return v === undefined || v === null || v === false ? '' : String(v);
  });
}

interface Pattern {
  re: RegExp;
  names: string[];
  out: string;
  weight: number;
}

const escapeRe = (s: string) => s.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');

/** Clés et valeurs ignorées lors de la traduction d'une réponse de l'API (identifiants, saisies des joueurs…). */
const SKIP_KEYS = new Set(['id', 'slug', 'code', 'email', 'displayName', 'userId', 'sessionId', 'duelId', 'qid', 'itemId', 'retryOf', 'url', 'href', 'path', 'audio', 'tokens', 'front', 'reading', 'romaji', 'jp', 'kanji', 'kana', 'lang', 'locale', 'theme', 'status', 'type', 'kind', 'tierId', 'sku', 'slot', 'levelCode', 'worldSlug', 'lessonSlug', 'serverNow', 'createdAt', 'updatedAt', 'expiresAt', 'unlockedAt', 'date', 'due']);
/** Champs d'une requête qui portent la réponse d'un joueur : on les renvoie en VO au serveur. */
const ANSWER_KEYS = new Set(['answer', 'answers']);

export class Translator {
  readonly size: number;
  private exact = new Map<string, string>();
  private reverse = new Map<string, string>();
  private patterns: Pattern[] = [];
  /** Traductions réellement affichées (anglais → français) : sert à renvoyer les réponses en VO. */
  private shown = new Map<string, string>();

  constructor(dictionaries: Dictionary[]) {
    for (const dict of dictionaries)
      for (const [k, v] of Object.entries(dict)) {
        if (!v || k.startsWith('//')) continue;
        if (!this.exact.has(k)) this.exact.set(k, v);
        if (!this.reverse.has(v)) this.reverse.set(v, k);
        if (HAS_PLACEHOLDER.test(k)) {
          const names: string[] = [];
          const parts = k.split(PLACEHOLDER);
          let re = '^';
          parts.forEach((p, i) => {
            if (i % 2 === 0) re += escapeRe(p);
            else {
              names.push(p);
              re += '([\\s\\S]+?)';
            }
          });
          const literal = parts.filter((_, i) => i % 2 === 0).join('');
          // Un motif réduit à des variables (« {0} {1} ») traduirait n'importe quoi : on l'écarte.
          if (literal.replace(/\s/g, '').length >= 2) this.patterns.push({ re: new RegExp(`${re}$`), names, out: v, weight: literal.length });
        }
      }
    this.patterns.sort((a, b) => b.weight - a.weight);
    this.size = this.exact.size;
  }

  has(key: string): boolean {
    return this.exact.has(key);
  }

  /** Texte d'interface : clé française + variables. */
  t(key: string, vars?: Vars): string {
    return interpolate(this.exact.get(key) ?? key, vars);
  }

  /** Texte venu des données (cours, réponses de l'API) : correspondance exacte, puis par motif. */
  tr(text: string, depth = 0): string {
    const hit = this.exact.get(text);
    if (hit !== undefined) return hit;
    if ((!LETTERS.test(text) && !text.includes('«')) || depth > 4) return text;
    const trimmed = text.trim();
    if (trimmed !== text) {
      if (!trimmed) return text;
      const inner = this.tr(trimmed, depth);
      return inner === trimmed ? text : text.replace(trimmed, inner);
    }
    if (text.includes('\n')) {
      const lines = text.split('\n');
      const out = lines.map((l) => this.tr(l, depth + 1));
      return out.join('\n');
    }
    for (const p of this.patterns) {
      const m = p.re.exec(text);
      if (!m) continue;
      const vals: Record<string, string> = {};
      p.names.forEach((n, i) => (vals[n] = this.tr(m[i + 1], depth + 1)));
      return interpolate(p.out, vals);
    }
    return text;
  }

  /**
   * Traduction inverse (réponse affichée en anglais → valeur d'origine attendue par le serveur).
   * Seules les traductions effectivement affichées comptent : un texte resté tel quel
   * (romaji « no », nom propre…) n'est jamais converti par erreur.
   */
  back(text: string): string {
    return this.shown.get(text) ?? text;
  }

  /** Traduction inverse d'après le dictionnaire seul (outils, tests). */
  reverseOf(text: string): string | undefined {
    return this.reverse.get(text);
  }

  /** Traduit toutes les chaînes d'une réponse de l'API. */
  deep<T>(value: T, key?: string): T {
    if (typeof value === 'string') {
      if (key && SKIP_KEYS.has(key)) return value as T;
      const out = this.tr(value);
      if (out !== value && !this.shown.has(out)) this.shown.set(out, value);
      return out as T;
    }
    if (Array.isArray(value)) return value.map((v) => this.deep(v, key)) as T;
    if (value && typeof value === 'object') {
      const out: Record<string, unknown> = {};
      for (const [k, v] of Object.entries(value as Record<string, unknown>)) out[k] = SKIP_KEYS.has(k) ? v : this.deep(v, k);
      return out as T;
    }
    return value;
  }

  /** Remet en VO les réponses du joueur contenues dans une requête. */
  answersBack<T>(body: T, inAnswer = false): T {
    if (typeof body === 'string') return (inAnswer ? this.back(body) : body) as T;
    if (Array.isArray(body)) return body.map((v) => this.answersBack(v, inAnswer)) as T;
    if (body && typeof body === 'object') {
      const out: Record<string, unknown> = {};
      for (const [k, v] of Object.entries(body as Record<string, unknown>)) out[k] = this.answersBack(v, inAnswer || ANSWER_KEYS.has(k));
      return out as T;
    }
    return body;
  }
}
