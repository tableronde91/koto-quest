/**
 * Duels en mode hors ligne : pas d'autres joueurs joignables, les adversaires sont donc simulés
 * (même moteur de règles que le serveur : dégâts selon la vitesse, combo, Elo et rangs).
 */
import {
  DUEL_RULES,
  DUEL_START_RATING,
  botAnswer,
  checkAnswer,
  createRng,
  duelDamage,
  duelOutcome,
  duelRank,
  duelReward,
  eloDelta,
  focusedPool,
  planDuelQuestions,
  type AvatarConfig,
  type EngineItem,
  type Question,
} from '@koto/learning-engine';
import type { DuelKind, DuelLeaderboardDto, DuelLobbyDto, DuelPlayerDto, DuelQuestionDto, DuelRankDto, DuelSideResultDto, DuelStateDto } from '@koto/shared';

interface LocalAnswer { round: number; side: 1 | 2; answer: string; correct: boolean; ms: number; damage: number; critical: boolean }
interface LocalDuel {
  id: string;
  kind: DuelKind;
  status: 'active' | 'finished';
  botName: string;
  botRating: number;
  hp1: number;
  hp2: number;
  streak1: number;
  streak2: number;
  round: number;
  roundStartsAt: string;
  questions: Question[];
  answers: LocalAnswer[];
  outcome: 'p1' | 'p2' | 'draw' | null;
  endReason: 'ko' | 'points' | 'forfeit' | null;
  rating1: number | null;
  delta1: number | null;
  createdAt: string;
  endedAt: string | null;
}
export interface LocalDuelState {
  profile: { code: string; rating: number; peakRating: number; wins: number; losses: number; draws: number; streak: number; bestStreak: number; damageDealt: number };
  queuedAt: string | null;
  duels: Record<string, LocalDuel>;
}

export interface DuelDeps {
  duelState: () => LocalDuelState | undefined;
  setDuelState: (s: LocalDuelState) => void;
  save: () => void;
  reward: (xp: number, coins: number) => void;
  me: () => { displayName: string; avatar: AvatarConfig };
  seenItems: () => EngineItem[];
  starterItems: () => EngineItem[];
  pool: EngineItem[];
  fail: (status: number, message: string) => never;
}

const GHOSTS: [string, number, number][] = [
  ['Hana', 1690, 61], ['Kaito', 1612, 54], ['Rin', 1548, 47], ['Sōta', 1475, 40], ['Mio', 1402, 35], ['Yūto', 1330, 28],
  ['Aoi', 1262, 22], ['Ren', 1196, 17], ['Sakura', 1130, 12], ['Haruto', 1074, 8], ['Yui', 1031, 5], ['Daiki', 1008, 3],
];
/** Délai avant de « trouver » un adversaire simulé */
const MATCH_DELAY_MS = 2600;

function rankDto(rating: number): DuelRankDto {
  const r = duelRank(rating);
  return { tierId: r.tier.id, jp: r.tier.jp, label: r.label, color: r.tier.color, next: r.next, progress: r.progress };
}

const uid = () => `d-${Date.now().toString(36)}-${Math.random().toString(36).slice(2, 10)}`;

export function localDuels(deps: DuelDeps) {
  function state(): LocalDuelState {
    let s = deps.duelState();
    if (!s) {
      const code = `KQ-${Array.from({ length: 6 }, () => 'ABCDEFGHJKLMNPQRSTUVWXYZ23456789'[Math.floor(Math.random() * 32)]).join('')}`;
      s = { profile: { code, rating: DUEL_START_RATING, peakRating: DUEL_START_RATING, wins: 0, losses: 0, draws: 0, streak: 0, bestStreak: 0, damageDealt: 0 }, queuedAt: null, duels: {} };
      deps.setDuelState(s);
    }
    return s;
  }

  function active(): LocalDuel | null {
    return Object.values(state().duels).find((d) => d.status === 'active') ?? null;
  }

  function create(kind: DuelKind, botName: string, botRating: number): LocalDuel {
    const seen = deps.seenItems();
    const items = seen.length >= 8 ? seen : deps.starterItems();
    const now = Date.now();
    const d: LocalDuel = {
      id: uid(),
      kind,
      status: 'active',
      botName,
      botRating,
      hp1: DUEL_RULES.hp,
      hp2: DUEL_RULES.hp,
      streak1: 0,
      streak2: 0,
      round: 0,
      roundStartsAt: new Date(now + DUEL_RULES.countdownMs).toISOString(),
      questions: planDuelQuestions(items, focusedPool(items, deps.pool), createRng(`${now}:${botName}`)),
      answers: [],
      outcome: null,
      endReason: null,
      rating1: null,
      delta1: null,
      createdAt: new Date(now).toISOString(),
      endedAt: null,
    };
    const s = state();
    // On ne garde que les derniers duels
    const old = Object.values(s.duels).filter((x) => x.status === 'finished').sort((a, b) => b.createdAt.localeCompare(a.createdAt)).slice(20);
    for (const o of old) delete s.duels[o.id];
    s.duels[d.id] = d;
    return d;
  }

  function finish(d: LocalDuel, outcome: 'p1' | 'p2' | 'draw', reason: 'ko' | 'points' | 'forfeit', at: number) {
    const p = state().profile;
    const score: 0 | 0.5 | 1 = outcome === 'p1' ? 1 : outcome === 'p2' ? 0 : 0.5;
    const [delta] = d.kind === 'ranked' ? eloDelta(p.rating, d.botRating, score) : [0];
    const result = outcome === 'draw' ? 'draw' : outcome === 'p1' ? 'win' : 'loss';
    d.status = 'finished';
    d.outcome = outcome;
    d.endReason = reason;
    d.endedAt = new Date(at).toISOString();
    d.rating1 = p.rating;
    d.delta1 = delta;
    if (d.kind === 'ranked') {
      p.rating += delta;
      p.peakRating = Math.max(p.peakRating, p.rating);
      if (result === 'win') p.wins++;
      else if (result === 'loss') p.losses++;
      else p.draws++;
      p.streak = result === 'win' ? p.streak + 1 : result === 'draw' ? p.streak : 0;
      p.bestStreak = Math.max(p.bestStreak, p.streak);
      p.damageDealt += d.answers.filter((a) => a.side === 1).reduce((n, a) => n + a.damage, 0);
    }
    const r = rewardFor(d);
    deps.reward(r.xp, r.coins);
  }

  function rewardFor(d: LocalDuel) {
    const result = d.outcome === 'draw' ? 'draw' : d.outcome === 'p1' ? 'win' : 'loss';
    if (d.endReason === 'forfeit' && result !== 'win') return { xp: 0, coins: 0 };
    const r = duelReward(result);
    return d.kind === 'practice' ? { xp: Math.floor(r.xp / 2), coins: Math.floor(r.coins / 2) } : r;
  }

  /** Fait avancer le duel jusqu'à maintenant (réponses de l'adversaire simulé, corrections). */
  function advance(d: LocalDuel, now: number) {
    const total = Math.min(DUEL_RULES.rounds, d.questions.length);
    for (let guard = 0; guard <= total && d.status === 'active'; guard++) {
      const start = Date.parse(d.roundStartsAt);
      if (now < start || d.round >= total) break;
      const r = d.round;
      const deadline = start + DUEL_RULES.roundMs + DUEL_RULES.graceMs;
      const bot = botAnswer(d.id, r, d.botRating);
      const mine = d.answers.find((a) => a.round === r && a.side === 1);
      const botDone = now >= start + bot.ms;
      const complete = !!mine && botDone;
      if (!complete && now < deadline) break;
      if (botDone && !d.answers.some((a) => a.round === r && a.side === 2)) {
        const q = d.questions[r];
        const hit = duelDamage(bot.correct, bot.ms, d.streak2);
        d.answers.push({ round: r, side: 2, answer: bot.correct ? String(q.answer) : (q.choices ?? []).find((c) => c !== q.answer) ?? '', correct: bot.correct, ms: bot.ms, damage: hit.damage, critical: hit.critical });
      }
      const a1 = d.answers.find((a) => a.round === r && a.side === 1);
      const a2 = d.answers.find((a) => a.round === r && a.side === 2);
      d.hp1 = Math.max(0, d.hp1 - (a2?.damage ?? 0));
      d.hp2 = Math.max(0, d.hp2 - (a1?.damage ?? 0));
      d.streak1 = a1?.correct ? d.streak1 + 1 : 0;
      d.streak2 = a2?.correct ? d.streak2 + 1 : 0;
      d.round = r + 1;
      const resolvedAt = complete ? now : deadline;
      d.roundStartsAt = new Date(resolvedAt + DUEL_RULES.revealMs).toISOString();
      const outcome = duelOutcome(d.hp1, d.hp2, r + 1) ?? (r + 1 >= total ? (d.hp1 === d.hp2 ? 'draw' : d.hp1 > d.hp2 ? 'p1' : 'p2') : null);
      if (outcome) finish(d, outcome, d.hp1 <= 0 || d.hp2 <= 0 ? 'ko' : 'points', resolvedAt);
    }
  }

  const publicQ = (q: Question, index: number): DuelQuestionDto => ({ index, type: q.type, prompt: q.prompt, display: { jp: q.display?.jp, reading: q.display?.reading, text: q.display?.text }, choices: q.choices ?? [] });
  const side = (a: LocalAnswer | undefined, before: number): DuelSideResultDto =>
    a ? { answer: a.answer, correct: a.correct, ms: a.ms, damage: a.damage, critical: a.critical, combo: a.correct ? before + 1 : 0 } : { answer: null, correct: false, ms: null, damage: 0, critical: false, combo: 0 };

  function toState(d: LocalDuel, now: number): DuelStateDto {
    const p = state().profile;
    const me = deps.me();
    const total = Math.min(DUEL_RULES.rounds, d.questions.length);
    const start = Date.parse(d.roundStartsAt);
    const live = d.status === 'active' && now >= start && d.round < total;
    const bot = live ? botAnswer(d.id, d.round, d.botRating) : null;
    const myRating = d.rating1 ?? p.rating;
    let last: DuelStateDto['last'] = null;
    if (d.round > 0) {
      const r = d.round - 1;
      const a = (s: 1 | 2) => d.answers.find((x) => x.round === r && x.side === s);
      const before = (s: 1 | 2) => (a(s)?.correct ? Math.max(0, (s === 1 ? d.streak1 : d.streak2) - 1) : 0);
      last = { question: publicQ(d.questions[r], r), answer: String(d.questions[r].answer), me: side(a(1), before(1)), opponent: side(a(2), before(2)) };
    }
    const mine = live ? d.answers.find((x) => x.round === d.round && x.side === 1) : undefined;
    const outcome = d.outcome === 'draw' ? 'draw' : d.outcome === 'p1' ? 'win' : 'loss';
    const reward = rewardFor(d);
    const mePlayer: DuelPlayerDto = { userId: 'local', name: me.displayName, avatar: me.avatar, rating: myRating, rank: rankDto(myRating), isBot: false };
    const opp: DuelPlayerDto = { userId: null, name: d.botName, avatar: null, rating: d.botRating, rank: rankDto(d.botRating), isBot: true };
    return {
      id: d.id,
      kind: d.kind,
      status: d.status,
      serverNow: new Date(now).toISOString(),
      rules: { hp: DUEL_RULES.hp, rounds: total, roundMs: DUEL_RULES.roundMs, revealMs: DUEL_RULES.revealMs },
      me: { ...mePlayer, rating: d.status === 'finished' ? myRating + (d.delta1 ?? 0) : myRating, rank: rankDto(d.status === 'finished' ? myRating + (d.delta1 ?? 0) : myRating), hp: d.hp1, side: 1, combo: d.streak1 },
      opponent: { ...opp, hp: d.hp2, online: true, combo: d.streak2 },
      round: d.round,
      roundStartsAt: d.roundStartsAt,
      question: live ? publicQ(d.questions[d.round], d.round) : null,
      mine: mine ? side(mine, d.streak1) : null,
      opponentAnswered: !!bot && now >= start + bot.ms,
      last,
      expiresAt: null,
      result:
        d.status === 'finished'
          ? { outcome, endReason: d.endReason, ratingBefore: myRating, ratingAfter: myRating + (d.delta1 ?? 0), delta: d.delta1 ?? 0, rankBefore: rankDto(myRating), rankAfter: rankDto(myRating + (d.delta1 ?? 0)), xp: reward.xp, coins: reward.coins }
          : null,
    };
  }

  function get(id: string): LocalDuel {
    const d = state().duels[id];
    if (!d) deps.fail(404, 'Duel introuvable.');
    return d!;
  }

  function lobby(): DuelLobbyDto {
    const s = state();
    const p = s.profile;
    const now = Date.now();
    const searching = s.queuedAt && now - Date.parse(s.queuedAt) < 60_000 ? { since: s.queuedAt } : null;
    const above = GHOSTS.filter(([, r]) => r > p.rating).length;
    const finished = Object.values(s.duels).filter((d) => d.status === 'finished').sort((a, b) => (b.endedAt ?? '').localeCompare(a.endedAt ?? '')).slice(0, 10);
    return {
      profile: { code: p.code, rating: p.rating, peakRating: p.peakRating, rank: rankDto(p.rating), wins: p.wins, losses: p.losses, draws: p.draws, streak: p.streak, bestStreak: p.bestStreak, damageDealt: p.damageDealt, position: above + 1, players: GHOSTS.length + 1 },
      activeDuelId: active()?.id ?? null,
      searching,
      invites: [],
      sent: [],
      history: finished.map((d) => ({
        id: d.id,
        kind: d.kind,
        opponent: d.botName,
        result: d.outcome === 'draw' ? 'draw' : d.outcome === 'p1' ? 'win' : 'loss',
        delta: d.kind === 'ranked' ? (d.delta1 ?? 0) : null,
        myHp: d.hp1,
        oppHp: d.hp2,
        endReason: d.endReason,
        endedAt: d.endedAt,
      })),
      online: false,
      rules: { hp: DUEL_RULES.hp, rounds: DUEL_RULES.rounds, roundMs: DUEL_RULES.roundMs },
    };
  }

  function leaderboard(sort: 'rating' | 'wins'): DuelLeaderboardDto {
    const p = state().profile;
    const me = deps.me();
    const rows = [
      ...GHOSTS.map(([name, rating, wins]) => ({ userId: `ghost-${name}`, name, avatar: null, rating, wins, losses: Math.round(wins * 0.8), me: false })),
      ...(p.wins + p.losses + p.draws > 0 ? [{ userId: 'local', name: me.displayName, avatar: me.avatar, rating: p.rating, wins: p.wins, losses: p.losses, me: true }] : []),
    ].sort((a, b) => (sort === 'wins' ? b.wins - a.wins || b.rating - a.rating : b.rating - a.rating || b.wins - a.wins));
    const entries = rows.map((r, i) => ({ ...r, position: i + 1, rank: rankDto(r.rating) }));
    const mine = entries.find((e) => e.me);
    return { sort, entries, me: mine ? { position: mine.position, rating: mine.rating, wins: mine.wins } : null };
  }

  function queuePoll() {
    const s = state();
    const a = active();
    if (a) return { status: 'matched', duelId: a.id };
    if (!s.queuedAt) return { status: 'idle' };
    if (Date.now() - Date.parse(s.queuedAt) < MATCH_DELAY_MS) return { status: 'searching', since: s.queuedAt };
    // Adversaire simulé de niveau proche
    const near = [...GHOSTS].sort((x, y) => Math.abs(x[1] - s.profile.rating) - Math.abs(y[1] - s.profile.rating))[Math.floor(Math.random() * 3)];
    const rating = Math.max(950, s.profile.rating + Math.round((Math.random() - 0.5) * 120));
    const d = create('ranked', near[0], rating);
    s.queuedAt = null;
    deps.save();
    return { status: 'matched', duelId: d.id };
  }

  return function handle(method: string, path: string, query: URLSearchParams, b: Record<string, unknown>): unknown {
    const route = `${method} ${path}`;
    const now = Date.now();
    let m: RegExpMatchArray | null;
    if (route === 'GET /duels') {
      const l = lobby();
      deps.save();
      return l;
    }
    if (route === 'GET /duels/leaderboard') return leaderboard(query.get('sort') === 'wins' ? 'wins' : 'rating');
    if (route === 'GET /duels/players') return { players: [] };
    if (route === 'GET /duels/invites') return [];
    if (route === 'POST /duels/queue') {
      const a = active();
      if (a) return { status: 'matched', duelId: a.id };
      state().queuedAt = new Date(now).toISOString();
      deps.save();
      return { status: 'searching', since: state().queuedAt };
    }
    if (route === 'GET /duels/queue') return queuePoll();
    if (route === 'DELETE /duels/queue') {
      state().queuedAt = null;
      deps.save();
      return { status: 'idle' };
    }
    if (route === 'POST /duels/practice') {
      const a = active() ?? create('practice', `Rōnin ${['Kenta', 'Aiko', 'Haru', 'Mei', 'Sora'][Math.floor(Math.random() * 5)]}`, Math.max(900, state().profile.rating + Math.round((Math.random() - 0.5) * 120)));
      state().queuedAt = null;
      deps.save();
      return { duelId: a.id };
    }
    if (route === 'POST /duels/challenges') deps.fail(503, 'Défier un ami nécessite la version en ligne de Koto Quest.');
    if ((m = route.match(/^GET \/duels\/([\w-]+)$/))) {
      const d = get(m[1]);
      advance(d, now);
      deps.save();
      return toState(d, now);
    }
    if ((m = route.match(/^POST \/duels\/([\w-]+)\/answer$/))) {
      const d = get(m[1]);
      advance(d, now);
      if (d.status !== 'active') return toState(d, now);
      const round = Number(b.round);
      const start = Date.parse(d.roundStartsAt);
      if (round !== d.round || now < start) deps.fail(409, 'Cette question n’est plus en jeu.');
      const ms = now - start;
      if (ms > DUEL_RULES.roundMs + DUEL_RULES.graceMs) deps.fail(409, 'Temps écoulé.');
      if (d.answers.some((a) => a.round === round && a.side === 1)) deps.fail(409, 'Tu as déjà répondu.');
      const q = d.questions[round];
      const correct = checkAnswer(q, String(b.answer));
      const hit = duelDamage(correct, ms, d.streak1);
      d.answers.push({ round, side: 1, answer: String(b.answer), correct, ms, damage: hit.damage, critical: hit.critical });
      advance(d, now);
      deps.save();
      return toState(d, now);
    }
    if ((m = route.match(/^POST \/duels\/([\w-]+)\/forfeit$/))) {
      const d = get(m[1]);
      advance(d, now);
      if (d.status === 'active') finish(d, 'p2', 'forfeit', now);
      deps.save();
      return toState(d, now);
    }
    if ((m = route.match(/^POST \/duels\/([\w-]+)\/(accept|decline)$/))) deps.fail(404, 'Défi introuvable.');
    return deps.fail(404, `Fonction indisponible en mode hors ligne (${route}).`);
  };
}
