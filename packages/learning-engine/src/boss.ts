import { AuthoredExercise, EngineItem, Question, QuestionType, authoredToQuestion, generateQuestion } from './exercises';
import { Rng, shuffle } from './random';

/**
 * Combats de boss (fin de monde).
 *  - Le boss a des points de vie (HP) : chaque bonne réponse lui retire 1 point.
 *  - Le joueur a des cœurs : chaque erreur en coûte un (et affiche l'explication).
 *  - La difficulté monte : reconnaissance → rappel actif → écoute et phrases rédigées.
 */
export const BOSS_RULES = { questions: 12, hp: 9, hearts: 3 } as const;

export interface BossRules {
  questions: number;
  hp: number;
  hearts: number;
}

export type BossState = 'ongoing' | 'won' | 'lost';

export interface BossProgress {
  state: BossState;
  hits: number;
  heartsLeft: number;
  /** Nombre de réponses prises en compte (les réponses données après la fin du combat sont ignorées). */
  counted: number;
}

/** Rejoue une suite de réponses (dans l'ordre) : utilisé à l'identique par le serveur et l'interface. */
export function simulateBoss(results: boolean[], rules: Pick<BossRules, 'hp' | 'hearts'> = BOSS_RULES): BossProgress {
  let hits = 0;
  let heartsLeft = rules.hearts;
  let counted = 0;
  for (const ok of results) {
    if (hits >= rules.hp || heartsLeft <= 0) break;
    counted++;
    if (ok) hits++;
    else heartsLeft--;
  }
  const state: BossState = hits >= rules.hp ? 'won' : heartsLeft <= 0 ? 'lost' : 'ongoing';
  return { state, hits, heartsLeft, counted };
}

/**
 * Prépare les questions du combat à partir des notions et exercices du monde.
 * Les questions sont ordonnées par difficulté croissante.
 */
export function planBossFight(items: EngineItem[], authored: AuthoredExercise[], pool: EngineItem[], rng: Rng, rules: BossRules = BOSS_RULES): Question[] {
  const total = rules.questions;
  const nAuthored = Math.min(authored.length, Math.round(total / 4));
  const nItems = total - nAuthored;
  const picked = shuffle(items, rng);
  // Si le monde a peu de notions, on les réutilise sous une autre forme.
  while (picked.length < nItems && items.length > 0) picked.push(...shuffle(items, rng));
  const chosen = picked.slice(0, nItems);

  const tiers: QuestionType[][] = [
    ['meaning_choice'],
    ['reverse_choice', 'reading_choice'],
    ['listening_choice', 'reverse_choice', 'jlpt_reading', 'jlpt_writing'],
  ];
  const questions: Question[] = chosen
    .map((item, i) => {
      const tier = tiers[Math.min(tiers.length - 1, Math.floor((i / Math.max(1, nItems)) * tiers.length))];
      const kanjiWord = !!item.reading && item.reading !== item.front && /[一-龯々]/.test(item.front);
      const allowed = tier.filter((t) => (t !== 'reading_choice' && !t.startsWith('jlpt_')) || (kanjiWord && (t === 'reading_choice' ? item.kind !== 'kana' : item.kind === 'vocabulary')));
      const usable = item.kind === 'grammar' ? (['meaning_choice', 'reverse_choice'] as QuestionType[]) : allowed;
      const type = usable[Math.floor(rng() * usable.length)] ?? 'meaning_choice';
      return generateQuestion(item, pool, type, rng) ?? generateQuestion(item, pool, 'meaning_choice', rng);
    })
    .filter((q): q is Question => !!q);
  // Les exercices rédigés (phrases, dialogues) arrivent en fin de combat : ce sont les plus exigeants.
  const finale = shuffle(authored, rng).slice(0, nAuthored).map((ex) => authoredToQuestion(ex, rng));
  return [...questions, ...finale];
}

/**
 * Chrono : temps maximal pour répondre à une question de combat, selon l'effort demandé.
 * Au-delà (plus une petite marge réseau côté serveur), la réponse compte comme une erreur.
 */
export const BOSS_TIME_LIMITS: Partial<Record<QuestionType, number>> & { default: number } = {
  default: 12,
  true_false: 10,
  listening_choice: 15,
  particle_choice: 15,
  fill_blank: 18,
  dialogue_choice: 18,
  sentence_order: 25,
  matching: 30,
};
/** Marge tolérée par le serveur (latence réseau, affichage). */
export const BOSS_TIME_GRACE_MS = 2500;
/** Réponse envoyée par l'interface quand le temps est écoulé (toujours fausse). */
export const TIMEOUT_ANSWER = '⏱';

export function bossTimeLimitSec(type: QuestionType): number {
  return BOSS_TIME_LIMITS[type] ?? BOSS_TIME_LIMITS.default;
}

/** Vrai si la réponse arrive trop tard (au-delà de la limite et de la marge). */
export function bossAnswerTooLate(type: QuestionType, shownAt: Date, answeredAt: Date): boolean {
  return answeredAt.getTime() - shownAt.getTime() > bossTimeLimitSec(type) * 1000 + BOSS_TIME_GRACE_MS;
}

/** Récompenses : généreuses la première fois, symboliques ensuite (pas de « farm »). */
export function bossReward(won: boolean, firstVictory: boolean): { xp: number; coins: number } {
  if (!won) return { xp: 5, coins: 0 };
  return firstVictory ? { xp: 120, coins: 30 } : { xp: 15, coins: 3 };
}
