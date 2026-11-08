import { CardState, currentRetrievability } from './fsrs';
import { EngineItem, Question, QuestionType, chooseQuestionType, generateMatching, generateQuestion } from './exercises';
import { masteryScore } from './mastery';
import { Rng, shuffle } from './random';

export interface CharacterEntry {
  item: EngineItem;
  /** null si le caractère n'a jamais été vu. */
  card: CardState | null;
}

export interface CharacterPracticeOptions {
  /** Nombre maximal de caractères travaillés dans la séance. */
  maxItems?: number;
  /** Nombre maximal de nouveaux caractères introduits. */
  maxNew?: number;
}

export interface CharacterPracticePlan {
  questions: Question[];
  /** Caractères introduits pour la première fois. */
  newItemIds: string[];
}

/**
 * Prépare une séance « Caractères » (comme l'onglet Caractères de Duolingo) :
 *  1. d'abord les caractères dont la révision est due (les plus oubliés en premier),
 *  2. puis quelques nouveaux, dans l'ordre du tableau (あいうえお…),
 *  3. puis les plus fragiles pour compléter.
 * Les nouveaux sont vus deux fois (reconnaissance puis rappel) et la séance se termine par une association.
 *
 * `entries` est dans l'ordre d'affichage ; `pool` limite les distracteurs à la même écriture
 * (on ne mélange pas hiragana et katakana dans les choix).
 */
export function planCharacterPractice(
  entries: CharacterEntry[],
  pool: EngineItem[],
  now: Date,
  rng: Rng,
  opts: CharacterPracticeOptions = {},
): CharacterPracticePlan {
  const maxItems = opts.maxItems ?? 10;
  const maxNew = opts.maxNew ?? 5;

  const due = entries
    .filter((e) => e.card && e.card.state !== 'new' && e.card.due.getTime() <= now.getTime())
    .sort((a, b) => retr(a.card!, now) - retr(b.card!, now));
  const unseen = entries.filter((e) => !e.card || e.card.state === 'new');
  const weak = entries
    .filter((e) => e.card && e.card.state !== 'new' && e.card.due.getTime() > now.getTime())
    .sort((a, b) => masteryScore(a.card!, now) - masteryScore(b.card!, now));

  const chosen: CharacterEntry[] = due.slice(0, maxItems);
  const fresh = unseen.slice(0, Math.max(0, Math.min(maxNew, maxItems - chosen.length)));
  chosen.push(...fresh);
  for (const w of weak) {
    if (chosen.length >= maxItems) break;
    chosen.push(w);
  }

  const freshIds = new Set(fresh.map((e) => e.item.id));
  const first: Question[] = [];
  const second: Question[] = [];
  for (const e of chosen) {
    const isNew = freshIds.has(e.item.id);
    const type: QuestionType = isNew ? 'meaning_choice' : chooseQuestionType(e.item, e.card?.reps ?? 0, rng);
    const q = generateQuestion(e.item, pool, type, rng) ?? generateQuestion(e.item, pool, 'meaning_choice', rng);
    if (q) first.push(q);
    if (isNew) {
      const recall: QuestionType = e.item.kind === 'kana' ? (rng() < 0.5 ? 'reverse_choice' : 'listening_choice') : 'reverse_choice';
      const q2 = generateQuestion(e.item, pool, recall, rng);
      if (q2) second.push(q2);
    }
  }
  const questions = [...first, ...shuffle(second, rng)];
  const matchingItems = chosen.map((e) => e.item);
  if (matchingItems.length >= 4) {
    const m = generateMatching(matchingItems, rng);
    if (m) questions.push(m);
  }
  return { questions, newItemIds: [...freshIds] };
}

function retr(card: CardState, now: Date) {
  return card.state === 'review' ? currentRetrievability(card, now) : 0.5;
}
