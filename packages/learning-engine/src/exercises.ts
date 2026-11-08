import { jlptReadingQuestion, jlptWritingQuestion } from './jlpt';
import { Rng, pick, shuffle } from './random';

export type ItemKind = 'kana' | 'vocabulary' | 'kanji' | 'grammar';

/** Représentation minimale d'une notion, indépendante de la base de données. */
export interface EngineItem {
  id: string;
  kind: ItemKind;
  /** Forme japonaise affichée (猫, あ, 水, 〜は〜です). */
  front: string;
  /** Lecture en kana (ねこ). Pour un kana : le kana lui-même. */
  reading?: string | null;
  /** Romanisation Hepburn (neko, a). */
  romaji?: string | null;
  /** Sens en français. Pour un kana : sa romanisation. */
  meaning: string;
}

export type QuestionType =
  | 'meaning_choice'
  | 'reverse_choice'
  | 'reading_choice'
  | 'listening_choice'
  | 'true_false'
  | 'matching'
  | 'particle_choice'
  | 'fill_blank'
  | 'sentence_order'
  | 'dialogue_choice'
  /** Format JLPT : lecture d'un mot en kanji (漢字読み) */
  | 'jlpt_reading'
  /** Format JLPT : écriture en kanji d'un mot en hiragana (表記) */
  | 'jlpt_writing';

export interface Question {
  type: QuestionType;
  itemId?: string;
  /** Consigne en français. */
  prompt: string;
  /** Contenu principal à afficher (texte japonais ou phrase). */
  display?: {
    jp?: string;
    reading?: string;
    text?: string;
    lines?: { speaker: string; jp: string; reading?: string }[];
    /** Examen : texte à lire (lecture) */
    passage?: string;
    /** Examen : les réponses s'écoutent au lieu de se lire */
    audioChoices?: boolean;
    /** Examen : intitulé de l'épreuve (ex. « もんだい１　漢字読み ») */
    part?: string;
    /** Examen : nombre maximal d'écoutes du document */
    maxPlays?: number;
  };
  /** Texte japonais prononçable avant de répondre (ne doit jamais révéler la réponse). */
  audio?: string;
  /**
   * Phrase complète à prononcer après une bonne réponse. « ＿ » y est remplacé par la
   * réponse donnée (voir fillBlank) : la réponse elle-même n'est donc pas exposée.
   */
  answerAudio?: string;
  choices?: string[];
  tokens?: string[];
  pairs?: { left: string[]; right: string[] };
  /** Bonne réponse : jamais envoyée au client avant correction. */
  answer: string | string[];
  explanation: string;
  /** Vrai si le hasard aide beaucoup (vrai/faux) : on ne donne alors jamais « Facile ». */
  guessable: boolean;
}

export type PublicQuestion = Omit<Question, 'answer' | 'explanation'>;

export function toPublic(q: Question): PublicQuestion {
  const { answer: _a, explanation: _e, ...rest } = q;
  return rest;
}

export function normalizeAnswer(s: string): string {
  return s.normalize('NFKC').trim().toLowerCase().replace(/\s+/g, ' ');
}

export function checkAnswer(q: Pick<Question, 'answer' | 'type'>, given: unknown): boolean {
  if (Array.isArray(q.answer)) {
    if (!Array.isArray(given) || given.length !== q.answer.length) return false;
    return q.answer.every((a, i) => typeof given[i] === 'string' && normalizeAnswer(given[i]) === normalizeAnswer(a));
  }
  return typeof given === 'string' && normalizeAnswer(given) === normalizeAnswer(q.answer);
}

/** Types de questions générables automatiquement pour une notion. */
export function questionTypesFor(item: EngineItem): QuestionType[] {
  switch (item.kind) {
    case 'kana':
      return ['meaning_choice', 'reverse_choice', 'listening_choice', 'true_false'];
    case 'vocabulary': {
      const types: QuestionType[] = ['meaning_choice', 'reverse_choice', 'listening_choice', 'true_false'];
      if (item.reading && item.reading !== item.front) types.push('reading_choice');
      return types;
    }
    case 'kanji':
      return ['meaning_choice', 'reverse_choice', 'reading_choice', 'true_false'];
    case 'grammar':
      return ['meaning_choice', 'reverse_choice'];
  }
}

/** Choisit un type adapté : reconnaissance d'abord, rappel actif et écoute ensuite. */
/**
 * Type d'exercice selon la familiarité avec la notion. Plus elle est connue, plus l'exercice ressemble à
 * l'examen : consignes en japonais, lecture et écriture des kanji avec les pièges du JLPT.
 */
export function chooseQuestionType(item: EngineItem, reps: number, rng: Rng): QuestionType {
  const types = questionTypesFor(item);
  if (reps < 1) return 'meaning_choice';
  const withKanji = item.kind === 'vocabulary' && !!item.reading && /[一-龯々]/.test(item.front);
  const jlpt: QuestionType[] = withKanji ? ['jlpt_reading', ...(item.reading !== item.front ? (['jlpt_writing'] as QuestionType[]) : [])] : [];
  if (reps < 2) return pick(types.filter((t) => t !== 'true_false'), rng);
  if (reps < 4) return pick([...types.filter((t) => t !== 'true_false'), ...jlpt], rng);
  // Notion bien installée : une fois sur deux au format exact de l'examen.
  if (jlpt.length && rng() < 0.5) return pick(jlpt, rng);
  return pick(types, rng);
}

const field = (item: EngineItem, key: 'meaning' | 'front' | 'reading') =>
  key === 'reading' ? (item.reading ?? item.front) : item[key];

/**
 * Choisit des distracteurs non ambigus : même type de notion, valeur différente
 * de la bonne réponse et sans doublon (ex. じ/ぢ se lisent tous deux « ji »).
 */
export function pickDistractors(
  item: EngineItem,
  pool: readonly EngineItem[],
  key: 'meaning' | 'front' | 'reading',
  count: number,
  rng: Rng,
): string[] {
  const correct = normalizeAnswer(field(item, key));
  const seen = new Set([correct]);
  // Pour les kana, les choix restent dans la même écriture (hiragana ou katakana) : sinon la réponse saute aux yeux.
  const script = item.kind === 'kana' ? kanaScript(item.front) : null;
  const sameKind = shuffle(pool.filter((p) => p.id !== item.id && p.kind === item.kind && (!script || kanaScript(p.front) === script)), rng);
  const others = shuffle(pool.filter((p) => p.id !== item.id && p.kind !== item.kind && p.kind !== 'grammar'), rng);
  const out: string[] = [];
  for (const cand of [...sameKind, ...(item.kind === 'grammar' ? [] : others)]) {
    if (out.length >= count) break;
    // Un mot de vocabulaire ne doit pas proposer un kana isolé (et inversement) si possible.
    if (cand.kind !== item.kind && sameKind.length >= count) continue;
    // Écarte aussi les notions partageant le même sens ou la même graphie (réponses ambiguës).
    if (normalizeAnswer(cand.meaning) === normalizeAnswer(item.meaning)) continue;
    if (normalizeAnswer(cand.front) === normalizeAnswer(item.front)) continue;
    const v = normalizeAnswer(field(cand, key));
    if (seen.has(v)) continue;
    seen.add(v);
    out.push(field(cand, key));
  }
  return out;
}

function kanaScript(s: string): 'hiragana' | 'katakana' | 'other' {
  const c = s.codePointAt(0) ?? 0;
  if (c >= 0x3040 && c <= 0x309f) return 'hiragana';
  if (c >= 0x30a0 && c <= 0x30ff) return 'katakana';
  return 'other';
}

const kindLabel: Record<ItemKind, string> = {
  kana: 'ce caractère',
  vocabulary: 'ce mot',
  kanji: 'ce kanji',
  grammar: 'cette construction',
};

function describe(item: EngineItem): string {
  const reading = item.reading && item.reading !== item.front ? ` (${item.reading})` : '';
  if (item.kind === 'kana') return `${item.front} se lit « ${item.meaning} ».`;
  return `${item.front}${reading} signifie « ${item.meaning} ».`;
}

/**
 * Génère une question à choix pour une notion. Renvoie `null` s'il n'y a pas
 * assez de distracteurs pour une question non ambiguë.
 */
export function generateQuestion(
  item: EngineItem,
  pool: readonly EngineItem[],
  type: QuestionType,
  rng: Rng,
  /** Phrase d'exemple contenant le mot (format JLPT) */
  example?: string,
): Question | null {
  if (type === 'jlpt_reading') return jlptReadingQuestion(item, pool, rng, example);
  if (type === 'jlpt_writing') return jlptWritingQuestion(item, pool, rng, example);
  const base = { itemId: item.id, explanation: describe(item), guessable: false };
  const audio = item.kind === 'grammar' ? undefined : (item.reading ?? item.front);
  const choiceQuestion = (key: 'meaning' | 'front' | 'reading', prompt: string, display: Question['display'], extra: Partial<Question> = {}): Question | null => {
    const distractors = pickDistractors(item, pool, key, 3, rng);
    if (distractors.length < 2) return null;
    const answer = field(item, key);
    return { ...base, type, prompt, display, choices: shuffle([answer, ...distractors], rng), answer, ...extra };
  };

  switch (type) {
    case 'meaning_choice':
      return choiceQuestion(
        'meaning',
        item.kind === 'kana' ? 'Comment se lit ce caractère ?' : `Que signifie ${kindLabel[item.kind]} ?`,
        { jp: item.front, reading: item.kind === 'kana' ? undefined : (item.reading ?? undefined) },
        { audio },
      );
    case 'reverse_choice':
      return choiceQuestion(
        'front',
        item.kind === 'kana' ? `Quel caractère se lit « ${item.meaning} » ?` : `Comment dit-on « ${item.meaning} » en japonais ?`,
        { text: item.meaning },
      );
    case 'reading_choice':
      return choiceQuestion('reading', `Quelle est la lecture de ${kindLabel[item.kind]} ?`, { jp: item.front }, { audio });
    case 'listening_choice':
      if (item.kind === 'kana') {
        return choiceQuestion('front', 'Écoute : quel caractère entends-tu ?', {}, { audio });
      }
      return choiceQuestion('meaning', 'Écoute : que signifie le mot prononcé ?', {}, { audio });
    case 'true_false': {
      const [distractor] = pickDistractors(item, pool, 'meaning', 1, rng);
      const truthful = !distractor || rng() < 0.5;
      const shown = truthful ? item.meaning : distractor;
      const statement = item.kind === 'kana' ? `${item.front} se lit « ${shown} »` : `${item.front} signifie « ${shown} »`;
      return {
        ...base,
        type,
        guessable: true,
        prompt: 'Vrai ou faux ?',
        display: { text: statement, jp: item.front },
        audio,
        choices: ['Vrai', 'Faux'],
        answer: truthful ? 'Vrai' : 'Faux',
      };
    }
    default:
      return null;
  }
}

/**
 * Réserve de distracteurs centrée sur le monde en cours : on propose d'abord des notions
 * déjà rencontrées dans ce monde (plus crédibles que des caractères jamais vus).
 * Pour chaque type de notion trop peu représenté (< 4), on complète avec la réserve du niveau.
 */
export function focusedPool(focus: readonly EngineItem[], full: readonly EngineItem[]): EngineItem[] {
  const out = [...focus];
  const ids = new Set(focus.map((i) => i.id));
  const kinds: ItemKind[] = ['kana', 'vocabulary', 'kanji', 'grammar'];
  for (const k of kinds) {
    if (focus.filter((i) => i.kind === k).length >= 4) continue;
    out.push(...full.filter((i) => i.kind === k && !ids.has(i.id)));
  }
  return out;
}

/** Association de mots : 3 à 5 notions à relier à leur sens. */
export function generateMatching(items: readonly EngineItem[], rng: Rng): Question | null {
  const unique = items.filter(
    (it, i) => items.findIndex((o) => normalizeAnswer(o.meaning) === normalizeAnswer(it.meaning)) === i,
  );
  if (unique.length < 3) return null;
  const chosen = shuffle(unique, rng).slice(0, 5);
  return {
    type: 'matching',
    prompt: 'Associe chaque élément japonais à son sens.',
    pairs: { left: chosen.map((i) => i.front), right: shuffle(chosen.map((i) => i.meaning), rng) },
    answer: chosen.map((i) => i.meaning),
    explanation: chosen.map(describe).join(' '),
    guessable: false,
  };
}

/** Exercice rédigé dans le contenu pédagogique (grammaire, phrases, dialogues). */
export interface AuthoredExercise {
  type: 'particle_choice' | 'fill_blank' | 'sentence_order' | 'dialogue_choice' | 'true_false';
  prompt: string;
  sentence?: string;
  reading?: string;
  translation?: string;
  lines?: { speaker: string; jp: string; reading?: string }[];
  choices?: string[];
  tokens?: string[];
  answer: string | string[];
  explanation: string;
}

export function validateAuthoredExercise(ex: AuthoredExercise): string[] {
  const errors: string[] = [];
  if (ex.type === 'sentence_order') {
    if (!Array.isArray(ex.answer) || ex.answer.length < 2) errors.push('sentence_order: answer doit être une liste de 2 segments ou plus');
  } else {
    if (typeof ex.answer !== 'string') errors.push(`${ex.type}: answer doit être une chaîne`);
    if (!ex.choices || ex.choices.length < 2) errors.push(`${ex.type}: au moins 2 choix`);
    else {
      const norm = ex.choices.map(normalizeAnswer);
      if (new Set(norm).size !== norm.length) errors.push(`${ex.type}: choix en double`);
      if (typeof ex.answer === 'string' && norm.filter((c) => c === normalizeAnswer(ex.answer as string)).length !== 1)
        errors.push(`${ex.type}: la réponse doit figurer exactement une fois parmi les choix`);
    }
  }
  if (!ex.explanation?.trim()) errors.push(`${ex.type}: explication manquante`);
  return errors;
}

/** Marque du trou dans une phrase à compléter. */
export const BLANK = '＿';
const BLANK_RE = /＿+|_+/g;

export const hasBlank = (s: string | null | undefined) => !!s && /＿|_/.test(s);

/** Remplace le trou par la réponse (une liste de segments est recollée). Sans trou, renvoie le texte tel quel. */
export function fillBlank(template: string, answer: string | string[]): string {
  const value = Array.isArray(answer) ? answer.join('') : answer;
  return hasBlank(template) ? template.replace(BLANK_RE, value) : template;
}

/** Les réponses en romaji (« neko ») ne se prononcent pas : on lit alors la phrase seule. */
const isJapanese = (s: string) => /[\u3040-\u30ff\u4e00-\u9faf]/.test(s);

export function authoredToQuestion(ex: AuthoredExercise, rng: Rng, itemId?: string): Question {
  const display: Question['display'] = ex.lines
    ? { lines: ex.lines, text: ex.translation }
    : { jp: ex.sentence?.replace(BLANK_RE, BLANK), reading: ex.reading?.replace(BLANK_RE, BLANK), text: ex.translation };
  const spoken = ex.sentence ? (ex.reading ?? ex.sentence).replace(BLANK_RE, BLANK) : undefined;
  const answerIsJp = typeof ex.answer === 'string' && isJapanese(ex.answer);
  let answerAudio: string | undefined;
  if (ex.type === 'dialogue_choice') answerAudio = [...(ex.lines ?? []).map((l) => l.reading ?? l.jp), BLANK].join('　');
  else if (spoken && hasBlank(spoken)) answerAudio = answerIsJp ? spoken : spoken.replace(BLANK_RE, '');
  else if (spoken) answerAudio = spoken;

  const base: Question = {
    type: ex.type,
    itemId,
    prompt: ex.prompt,
    display,
    answer: ex.answer,
    explanation: ex.explanation,
    guessable: ex.type === 'true_false',
    // Avant de répondre, on ne lit jamais une phrase à trou (le trou serait « sauté » et dénaturerait la phrase).
    audio: spoken && !hasBlank(spoken) && ex.type !== 'fill_blank' ? spoken : undefined,
    answerAudio,
  };
  if (ex.type === 'sentence_order') {
    const answer = ex.answer as string[];
    let tokens = shuffle(answer, rng);
    // Évite de proposer les segments déjà dans le bon ordre.
    for (let i = 0; i < 5 && tokens.join('|') === answer.join('|'); i++) tokens = shuffle(answer, rng);
    return { ...base, tokens, audio: undefined, answerAudio: BLANK };
  }
  return { ...base, choices: shuffle(ex.choices ?? [], rng) };
}

/**
 * Prépare la même question pour une nouvelle tentative (exercice raté repris en fin de séance) :
 * même contenu, mais choix, segments et colonnes remélangés pour ne pas répondre « de mémoire de position ».
 */
export function reshuffleForRetry(pub: PublicQuestion, answer: string | string[], rng: Rng): PublicQuestion {
  const differentOrder = <T>(items: T[], avoid: T[]) => {
    let out = shuffle(items, rng);
    for (let i = 0; i < 6 && items.length > 1 && out.join('|') === avoid.join('|'); i++) out = shuffle(items, rng);
    return out;
  };
  const next: PublicQuestion = { ...pub };
  if (pub.choices) next.choices = differentOrder(pub.choices, pub.choices);
  if (pub.tokens) next.tokens = differentOrder(pub.tokens, Array.isArray(answer) ? answer : pub.tokens);
  // La colonne de gauche garde son ordre : la réponse attendue (liste des sens) en dépend.
  if (pub.pairs) next.pairs = { left: pub.pairs.left, right: differentOrder(pub.pairs.right, pub.pairs.right) };
  return next;
}
