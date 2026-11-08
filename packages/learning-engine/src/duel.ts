import { generateQuestion, type EngineItem, type Question, type QuestionType } from './exercises';
import { createRng, shuffle, type Rng } from './random';

/**
 * Duel : deux joueurs reçoivent la même question au même moment.
 * Une bonne réponse inflige des dégâts d'autant plus forts qu'elle est rapide.
 */
export const DUEL_RULES = {
  hp: 100,
  rounds: 12,
  /** Temps pour répondre à une question */
  roundMs: 10_000,
  /** Marge réseau tolérée après la fin du chrono */
  graceMs: 1_500,
  /** Affichage de la correction entre deux questions */
  revealMs: 2_800,
  /** Compte à rebours avant la première question */
  countdownMs: 3_500,
  minDamage: 8,
  maxDamage: 26,
  /** Réponse très rapide : coup critique */
  criticalMs: 2_000,
  criticalBonus: 6,
  /** Bonus par bonne réponse consécutive (à partir de la 2e), plafonné */
  comboBonus: 2,
  comboMax: 6,
  /** Un défi non accepté expire */
  inviteTtlMs: 120_000,
  /** Un joueur qui ne donne plus signe de vie perd par abandon */
  afkMs: 25_000,
  /** Une recherche d'adversaire sans nouvelles du joueur est annulée */
  queueTtlMs: 12_000,
} as const;

export const DUEL_START_RATING = 1000;

export interface DuelHit {
  damage: number;
  critical: boolean;
  combo: number;
}

/**
 * Dégâts d'une réponse. `streak` = nombre de bonnes réponses consécutives AVANT celle-ci.
 * Mauvaise réponse ou hors délai : aucun dégât (et le combo retombe).
 */
export function duelDamage(correct: boolean, ms: number, streak = 0): DuelHit {
  if (!correct || ms > DUEL_RULES.roundMs + DUEL_RULES.graceMs) return { damage: 0, critical: false, combo: 0 };
  const t = Math.min(1, Math.max(0, ms / DUEL_RULES.roundMs));
  const speed = Math.round(DUEL_RULES.minDamage + (DUEL_RULES.maxDamage - DUEL_RULES.minDamage) * (1 - t));
  const critical = ms <= DUEL_RULES.criticalMs;
  const combo = streak + 1;
  const comboBonus = Math.min(DUEL_RULES.comboMax, Math.max(0, combo - 1) * DUEL_RULES.comboBonus);
  return { damage: speed + (critical ? DUEL_RULES.criticalBonus : 0) + comboBonus, critical, combo };
}

export type DuelOutcome = 'p1' | 'p2' | 'draw' | null;

/** Fin de duel : K.-O., ou à l'issue de la dernière question (le plus de PV l'emporte). */
export function duelOutcome(hp1: number, hp2: number, roundsPlayed: number): DuelOutcome {
  if (hp1 <= 0 && hp2 <= 0) return 'draw';
  if (hp2 <= 0) return 'p1';
  if (hp1 <= 0) return 'p2';
  if (roundsPlayed >= DUEL_RULES.rounds) return hp1 === hp2 ? 'draw' : hp1 > hp2 ? 'p1' : 'p2';
  return null;
}

/** Classement Elo. `score` = 1 victoire, 0.5 nul, 0 défaite (du point de vue du joueur 1). */
export function eloDelta(r1: number, r2: number, score: 0 | 0.5 | 1, k = 32): [number, number] {
  const expected = 1 / (1 + 10 ** ((r2 - r1) / 400));
  let d = Math.round(k * (score - expected));
  // Une victoire rapporte toujours un peu, une défaite coûte toujours un peu.
  if (score === 1) d = Math.max(4, d);
  if (score === 0) d = Math.min(-4, d);
  return [d, -d];
}

export interface DuelTier {
  id: string;
  jp: string;
  name: string;
  min: number;
  color: string;
}

/** Rangs, du fantassin au maître du pays. Chaque rang a trois divisions (III → I). */
export const DUEL_TIERS: DuelTier[] = [
  { id: 'ashigaru', jp: '足軽', name: 'Ashigaru', min: 0, color: '#9C6B3E' },
  { id: 'samurai', jp: '侍', name: 'Samouraï', min: 1100, color: '#8E9AA6' },
  { id: 'kengo', jp: '剣豪', name: 'Kengō', min: 1250, color: '#D4A537' },
  { id: 'daimyo', jp: '大名', name: 'Daimyō', min: 1400, color: '#3FA7A0' },
  { id: 'shogun', jp: '将軍', name: 'Shōgun', min: 1550, color: '#7B5BD6' },
  { id: 'tenka', jp: '天下人', name: 'Tenkabito', min: 1700, color: '#C8323F' },
];

export interface DuelRank {
  tier: DuelTier;
  /** 3, 2 ou 1 (le dernier rang n'a pas de division) */
  division: number | null;
  label: string;
  /** Points de classement du palier suivant (null au sommet) */
  next: number | null;
  /** Avancement vers le palier suivant, 0..1 */
  progress: number;
}

export function duelRank(rating: number): DuelRank {
  let i = 0;
  while (i + 1 < DUEL_TIERS.length && rating >= DUEL_TIERS[i + 1].min) i++;
  const tier = DUEL_TIERS[i];
  if (i === DUEL_TIERS.length - 1) return { tier, division: null, label: tier.name, next: null, progress: 1 };
  const top = DUEL_TIERS[i + 1].min;
  // Les divisions du premier rang se comptent à partir du classement de départ.
  const floor = i === 0 ? DUEL_START_RATING : tier.min;
  const step = (top - floor) / 3;
  const pos = Math.max(0, rating - floor);
  const div = Math.max(1, 3 - Math.min(2, Math.floor(pos / step)));
  const lo = floor + (3 - div) * step;
  const hi = lo + step;
  return {
    tier,
    division: div,
    label: `${tier.name} ${['', 'I', 'II', 'III'][div]}`,
    next: Math.round(hi),
    progress: Math.min(1, Math.max(0, (rating - lo) / step)),
  };
}

/** Récompenses d'un duel (XP et pièces). */
export function duelReward(result: 'win' | 'loss' | 'draw'): { xp: number; coins: number } {
  return result === 'win' ? { xp: 30, coins: 15 } : result === 'draw' ? { xp: 18, coins: 8 } : { xp: 10, coins: 3 };
}

const DUEL_TYPES: QuestionType[] = ['meaning_choice', 'reverse_choice', 'reading_choice', 'jlpt_reading'];

/**
 * Questions du duel : uniquement des QCM lisibles en un coup d'œil (pas d'écoute :
 * les deux joueurs doivent être à égalité), du plus simple au plus exigeant.
 */
export function planDuelQuestions(items: readonly EngineItem[], pool: readonly EngineItem[], rng: Rng, count: number = DUEL_RULES.rounds): Question[] {
  const usable = items.filter((i) => i.kind !== 'grammar');
  const source = usable.length >= 4 ? usable : [...items];
  if (source.length === 0) return [];
  const picked = shuffle(source, rng);
  while (picked.length < count + 4) picked.push(...shuffle(source, rng));
  const out: Question[] = [];
  const seen = new Set<string>();
  for (const item of picked) {
    if (out.length >= count) break;
    const stage = out.length / count;
    const kanjiWord = !!item.reading && item.reading !== item.front && /[一-龯々]/.test(item.front);
    const types = DUEL_TYPES.filter((t) =>
      t === 'meaning_choice' ? true : t === 'reverse_choice' ? stage >= 0.25 : t === 'reading_choice' ? stage >= 0.4 && kanjiWord : stage >= 0.6 && kanjiWord && item.kind === 'vocabulary',
    );
    const type = types[Math.floor(rng() * types.length)] ?? 'meaning_choice';
    const q = generateQuestion(item, pool, type, rng) ?? generateQuestion(item, pool, 'meaning_choice', rng);
    if (!q || !q.choices || q.choices.length < 3) continue;
    const key = `${q.type}:${q.itemId}`;
    if (seen.has(key) && out.length < picked.length - count) continue;
    seen.add(key);
    out.push(q);
  }
  return out;
}

/**
 * Adversaire simulé (entraînement, ou mode hors-ligne) : sa précision et sa vitesse
 * dépendent de son classement. Déterministe pour un duel et une question donnés.
 */
export function botAnswer(seed: string, round: number, botRating: number): { correct: boolean; ms: number } {
  const rng = createRng(`${seed}:bot:${round}`);
  const skill = Math.min(1, Math.max(0, (botRating - 850) / 900));
  const correct = rng() < 0.55 + 0.35 * skill;
  const base = 6200 - 3400 * skill;
  const ms = Math.round(Math.min(DUEL_RULES.roundMs - 300, Math.max(1100, base + (rng() - 0.5) * 3600)));
  return { correct, ms };
}
