import { addDays } from './time';

/**
 * Lecture : tous les contes et tous leurs chapitres sont ouverts dès le départ, le lecteur lit ce qu'il veut,
 * quand il veut. On lui propose simplement un chapitre du jour (le premier pas encore lu) pour garder l'habitude.
 */
export type ReadingState = 'read' | 'available';

export interface ReadingLogLite {
  chapter: string;
  dateKey: string;
}

/** État de chaque chapitre, dans l'ordre du catalogue : lu, ou disponible (jamais verrouillé). */
export function readingStates(order: readonly string[], logs: readonly ReadingLogLite[]): Map<string, ReadingState> {
  const read = new Set(logs.map((l) => l.chapter));
  return new Map(order.map((slug) => [slug, read.has(slug) ? 'read' : 'available'] as const));
}

/** Chapitre conseillé : le premier pas encore lu, dans l'ordre du catalogue (null quand tout est lu). */
export function readingSuggestion(order: readonly string[], logs: readonly ReadingLogLite[]): string | null {
  const read = new Set(logs.map((l) => l.chapter));
  return order.find((slug) => !read.has(slug)) ?? null;
}

/** Jours de lecture consécutifs (la série tient tant que la lecture d'hier ou d'aujourd'hui est faite). */
export function readingStreak(dateKeys: readonly string[], todayKey: string): { current: number; best: number } {
  const days = new Set(dateKeys);
  let cursor = days.has(todayKey) ? todayKey : addDays(todayKey, -1);
  let current = 0;
  while (days.has(cursor)) {
    current++;
    cursor = addDays(cursor, -1);
  }
  let best = 0;
  for (const k of days) {
    if (days.has(addDays(k, -1))) continue;
    let n = 1;
    let c = k;
    while (days.has((c = addDays(c, 1)))) n++;
    best = Math.max(best, n);
  }
  return { current, best: Math.max(best, current) };
}

/** Récompense de la première lecture d'un chapitre (les relectures ne rapportent rien). */
export function readingReward(correct: number, total: number): { xp: number; coins: number } {
  return { xp: 15 + 5 * correct, coins: total > 0 && correct === total ? 10 : 5 };
}

/** Texte japonais sans la notation des furigana {漢字|かな}. */
export function stripRuby(text: string): string {
  return text.replace(/\{([^|{}]+)\|[^|{}]+\}/g, '$1');
}

/** Découpe {漢字|かな} en segments pour l'affichage (ruby). */
export function rubySegments(text: string): { text: string; ruby?: string }[] {
  const out: { text: string; ruby?: string }[] = [];
  const re = /\{([^|{}]+)\|([^|{}]+)\}/g;
  let last = 0;
  let m: RegExpExecArray | null;
  while ((m = re.exec(text))) {
    if (m.index > last) out.push({ text: text.slice(last, m.index) });
    out.push({ text: m[1], ruby: m[2] });
    last = m.index + m[0].length;
  }
  if (last < text.length) out.push({ text: text.slice(last) });
  return out;
}
