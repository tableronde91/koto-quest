import { EngineItem, Question, QuestionType, generateQuestion } from './exercises';
import { Rng, shuffle } from './random';

/**
 * Mini-jeux chronométrés (phase 2). Ils se jouent sur les notions déjà rencontrées :
 * c'est de l'entraînement, ils ne modifient pas la planification des révisions.
 */
export type GameId = 'kanji-rush' | 'speed' | 'listening';

export interface GameDef {
  id: GameId;
  title: string;
  description: string;
  durationSec: number;
  /** Nombre minimal de notions vues pour débloquer le jeu. */
  minItems: number;
  /** Types de notions utilisées. */
  kinds: EngineItem['kind'][];
  questionTypes: QuestionType[];
}

export const GAMES: Record<GameId, GameDef> = {
  'kanji-rush': {
    id: 'kanji-rush',
    title: 'Kanji Rush',
    description: 'Identifie un maximum de kanji en une minute.',
    durationSec: 60,
    minItems: 6,
    kinds: ['kanji'],
    questionTypes: ['meaning_choice', 'reverse_choice', 'reading_choice'],
  },
  speed: {
    id: 'speed',
    title: 'Speed Challenge',
    description: 'Une minute, toutes les notions vues : réponds le plus vite possible.',
    durationSec: 60,
    minItems: 8,
    kinds: ['kana', 'vocabulary', 'kanji'],
    questionTypes: ['meaning_choice', 'reverse_choice'],
  },
  listening: {
    id: 'listening',
    title: 'Listening Ninja',
    description: 'Écoute et reconnais les mots prononcés.',
    durationSec: 60,
    minItems: 6,
    kinds: ['kana', 'vocabulary'],
    questionTypes: ['listening_choice'],
  },
};

export const GAME_IDS = Object.keys(GAMES) as GameId[];

/** Marge accordée pour la latence réseau entre la fin du chrono et la dernière réponse. */
export const GAME_GRACE_MS = 3000;
/** Pièces gagnables en mini-jeux par jour (évite d'« acheter » la boutique en jouant en boucle). */
export const DAILY_GAME_COIN_CAP = 15;

export const eligibleItems = (game: GameDef, seen: EngineItem[]) => seen.filter((i) => game.kinds.includes(i.kind));

/** Prépare assez de questions pour une minute de jeu rapide, en réutilisant les notions si besoin. */
export function planTimedGame(game: GameDef, seen: EngineItem[], pool: EngineItem[], rng: Rng, count = 60): Question[] {
  const items = eligibleItems(game, seen);
  if (items.length < game.minItems) return [];
  const out: Question[] = [];
  let bag: EngineItem[] = [];
  for (let guard = 0; out.length < count && guard < count * 4; guard++) {
    if (!bag.length) bag = shuffle(items, rng);
    const item = bag.pop()!;
    const types = game.questionTypes.filter((t) => t !== 'reading_choice' || (item.reading && item.reading !== item.front));
    const q = generateQuestion(item, pool, types[Math.floor(rng() * types.length)], rng);
    // Pas deux fois la même notion d'affilée
    if (q && out[out.length - 1]?.itemId !== q.itemId) out.push(q);
  }
  return out;
}

export interface TimedAnswer {
  correct: boolean;
  /** Millisecondes écoulées depuis le début de la partie. */
  atMs: number;
}

/** Score : bonnes réponses données avant la fin du chrono (plus la marge). */
export function scoreTimedGame(game: GameDef, answers: TimedAnswer[]): { score: number; answered: number } {
  const limit = game.durationSec * 1000 + GAME_GRACE_MS;
  const inTime = answers.filter((a) => a.atMs >= 0 && a.atMs <= limit);
  return { score: inTime.filter((a) => a.correct).length, answered: inTime.length };
}

export function gameReward(score: number, coinsEarnedToday: number): { xp: number; coins: number } {
  const xp = Math.min(60, score * 2);
  const coins = Math.max(0, Math.min(Math.floor(score / 5), DAILY_GAME_COIN_CAP - coinsEarnedToday));
  return { xp, coins };
}
