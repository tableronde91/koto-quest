import { BadRequestException, ConflictException, ForbiddenException, Injectable, NotFoundException } from '@nestjs/common';
import { randomInt } from 'node:crypto';
import type { Duel, DuelAnswer, DuelProfile, Prisma } from '@prisma/client';
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
  type Question,
} from '@koto/learning-engine';
import type {
  DuelHistoryDto,
  DuelInviteDto,
  DuelKind,
  DuelLeaderboardDto,
  DuelLobbyDto,
  DuelPlayerDto,
  DuelPlayerSearchDto,
  DuelQueueDto,
  DuelQuestionDto,
  DuelRankDto,
  DuelSideResultDto,
  DuelStateDto,
  DuelStatus,
} from '@koto/shared';
import { PrismaService } from '../common/prisma.service';
import { ClockService } from '../common/clock.service';
import { ContentService, toEngineItem } from '../content/content.service';
import { ActivityService } from '../learning/activity.service';

type Tx = Prisma.TransactionClient;
type Side = 1 | 2;

const CODE_ALPHABET = 'ABCDEFGHJKLMNPQRSTUVWXYZ23456789';
const BOT_NAMES = ['Rōnin Kenta', 'Rōnin Aiko', 'Rōnin Haru', 'Rōnin Mei', 'Rōnin Sora', 'Rōnin Yuki', 'Rōnin Daichi', 'Rōnin Hana'];
/** Un joueur est « en ligne » s'il a donné signe de vie récemment. */
const ONLINE_MS = 6_000;

export function rankDto(rating: number): DuelRankDto {
  const r = duelRank(rating);
  return { tierId: r.tier.id, jp: r.tier.jp, label: r.label, color: r.tier.color, next: r.next, progress: r.progress };
}

const sideOf = (d: Pick<Duel, 'p1Id' | 'p2Id'>, userId: string): Side | null => (d.p1Id === userId ? 1 : d.p2Id === userId ? 2 : null);
const other = (s: Side): Side => (s === 1 ? 2 : 1);

/**
 * Duels : le serveur est l'unique arbitre. Il distribue les questions au même instant aux deux joueurs,
 * mesure lui-même le temps de réponse, corrige et applique les dégâts. Les clients se contentent
 * d'interroger l'état du duel à intervalles courts.
 */
@Injectable()
export class DuelService {
  constructor(
    private prisma: PrismaService,
    private clock: ClockService,
    private content: ContentService,
    private activity: ActivityService,
  ) {}

  // ───────────── Profils ─────────────

  async profile(userId: string, tx: Tx = this.prisma): Promise<DuelProfile> {
    const existing = await tx.duelProfile.findUnique({ where: { userId } });
    if (existing) return existing;
    for (let attempt = 0; attempt < 5; attempt++) {
      const code = `KQ-${Array.from({ length: 6 }, () => CODE_ALPHABET[randomInt(CODE_ALPHABET.length)]).join('')}`;
      try {
        return await tx.duelProfile.upsert({ where: { userId }, create: { userId, code }, update: {} });
      } catch (e: any) {
        if (e?.code !== 'P2002') throw e;
      }
    }
    throw new ConflictException('Impossible de créer le profil de duelliste.');
  }

  private async player(userId: string, tx: Tx = this.prisma): Promise<DuelPlayerDto> {
    const [user, p] = await Promise.all([tx.user.findUniqueOrThrow({ where: { id: userId }, select: { displayName: true, avatar: true } }), this.profile(userId, tx)]);
    return { userId, name: user.displayName, avatar: (user.avatar as AvatarConfig | null) ?? null, rating: p.rating, rank: rankDto(p.rating), isBot: false };
  }

  private botPlayer(d: Duel): DuelPlayerDto {
    const rating = d.botRating ?? DUEL_START_RATING;
    return { userId: null, name: d.botName ?? 'Rōnin', avatar: null, rating, rank: rankDto(rating), isBot: true };
  }

  // ───────────── Verrou par duel ─────────────

  /** Toutes les modifications d'un duel passent par un verrou : une seule correction par question. */
  private locked<T>(key: string, fn: (tx: Tx) => Promise<T>): Promise<T> {
    return this.prisma.$transaction(
      async (tx) => {
        await tx.$queryRaw`SELECT 1 AS ok FROM (SELECT pg_advisory_xact_lock(hashtext(${key}))) AS l`;
        return fn(tx);
      },
      { timeout: 15_000, maxWait: 10_000 },
    );
  }

  // ───────────── Questions ─────────────

  /**
   * Questions communes : d'abord les notions que les deux joueurs ont déjà apprises,
   * sinon celles de l'un ou de l'autre, sinon les kana du premier monde.
   */
  private async plan(seed: string, userIds: string[], tx: Tx): Promise<Question[]> {
    const cards = await tx.reviewCard.findMany({ where: { userId: { in: userIds } }, select: { userId: true, itemId: true } });
    const byUser = userIds.map((u) => new Set(cards.filter((c) => c.userId === u).map((c) => c.itemId)));
    const common = [...byUser[0]].filter((id) => byUser.every((s) => s.has(id)));
    const union = [...new Set(cards.map((c) => c.itemId))];
    let ids = common.length >= 8 ? common : union.length >= 8 ? union : [];
    let rows = ids.length ? await tx.learningItem.findMany({ where: { id: { in: ids } } }) : [];
    if (rows.length < 8) {
      rows = await tx.learningItem.findMany({ where: { lessons: { some: { lesson: { chapter: { world: { slug: 'n5-w1' } } } } } } });
      ids = rows.map((r) => r.id);
    }
    const items = rows.map(toEngineItem);
    const levels = [...new Set(rows.map((r) => r.levelCode))];
    const full = (await Promise.all(levels.map((l) => this.content.enginePool(l)))).flat();
    return planDuelQuestions(items, focusedPool(items, full), createRng(seed));
  }

  private publicQuestion(q: Question, index: number): DuelQuestionDto {
    const d = q.display ?? {};
    return { index, type: q.type, prompt: q.prompt, display: { jp: d.jp, reading: d.reading, text: d.text }, choices: q.choices ?? [] };
  }

  // ───────────── Déroulement ─────────────

  /** Fait avancer le duel jusqu'à l'instant présent (expiration, abandon, correction des questions). */
  private async advance(tx: Tx, d: Duel, now: Date): Promise<{ duel: Duel; finished: boolean }> {
    if (d.status === 'pending' && now.getTime() - d.createdAt.getTime() > DUEL_RULES.inviteTtlMs) {
      return { duel: await tx.duel.update({ where: { id: d.id }, data: { status: 'expired', endedAt: now } }), finished: false };
    }
    if (d.status !== 'active') return { duel: d, finished: false };

    // Abandon : un joueur humain qui ne donne plus de nouvelles perd le duel.
    const stale = (seen: Date | null) => !seen || now.getTime() - seen.getTime() > DUEL_RULES.afkMs;
    const gone1 = stale(d.seen1);
    const gone2 = d.p2Id ? stale(d.seen2) : false;
    if (gone1 || gone2) {
      const outcome = gone1 && gone2 ? 'draw' : gone1 ? 'p2' : 'p1';
      return { duel: await this.finish(tx, d, outcome, 'forfeit', now), finished: true };
    }

    const questions = d.questions as unknown as Question[];
    const total = Math.min(DUEL_RULES.rounds, questions.length);
    let duel = d;
    for (let guard = 0; guard < total + 1; guard++) {
      if (!duel.roundStartsAt || now < duel.roundStartsAt || duel.round >= total) break;
      const r = duel.round;
      const start = duel.roundStartsAt.getTime();
      const deadline = start + DUEL_RULES.roundMs + DUEL_RULES.graceMs;
      const answers = await tx.duelAnswer.findMany({ where: { duelId: duel.id, round: r } });
      const bot = duel.p2Id ? null : botAnswer(duel.id, r, duel.botRating ?? DUEL_START_RATING);
      const has = (s: Side) => answers.some((a) => a.side === s) || (s === 2 && !!bot && now.getTime() >= start + bot.ms);
      const complete = has(1) && has(2);
      if (!complete && now.getTime() < deadline) break;

      // Réponse de l'adversaire simulé
      if (bot && !answers.some((a) => a.side === 2) && now.getTime() >= start + bot.ms) {
        const q = questions[r];
        const given = bot.correct ? String(q.answer) : (q.choices ?? []).find((c) => c !== q.answer) ?? '';
        const hit = duelDamage(bot.correct, bot.ms, duel.streak2);
        answers.push(await tx.duelAnswer.create({ data: { duelId: duel.id, round: r, side: 2, answer: given, correct: bot.correct, ms: bot.ms, damage: hit.damage, critical: hit.critical } }));
      }
      const a1 = answers.find((a) => a.side === 1);
      const a2 = answers.find((a) => a.side === 2);
      const hp1 = Math.max(0, duel.hp1 - (a2?.damage ?? 0));
      const hp2 = Math.max(0, duel.hp2 - (a1?.damage ?? 0));
      const resolvedAt = complete ? now.getTime() : deadline;
      duel = await tx.duel.update({
        where: { id: duel.id },
        data: {
          hp1,
          hp2,
          streak1: a1?.correct ? duel.streak1 + 1 : 0,
          streak2: a2?.correct ? duel.streak2 + 1 : 0,
          round: r + 1,
          roundStartsAt: new Date(resolvedAt + DUEL_RULES.revealMs),
        },
      });
      const outcome = duelOutcome(hp1, hp2, r + 1) ?? (r + 1 >= total ? (hp1 === hp2 ? 'draw' : hp1 > hp2 ? 'p1' : 'p2') : null);
      if (outcome) return { duel: await this.finish(tx, duel, outcome, hp1 <= 0 || hp2 <= 0 ? 'ko' : 'points', new Date(resolvedAt)), finished: true };
    }
    return { duel, finished: false };
  }

  /** Clôture : classement (duels classés uniquement), palmarès et récompenses. */
  private async finish(tx: Tx, d: Duel, outcome: 'p1' | 'p2' | 'draw', reason: 'ko' | 'points' | 'forfeit', now: Date): Promise<Duel> {
    const humans: { side: Side; userId: string }[] = [{ side: 1, userId: d.p1Id }, ...(d.p2Id ? [{ side: 2 as Side, userId: d.p2Id }] : [])];
    const profiles = new Map<string, DuelProfile>();
    for (const h of humans) profiles.set(h.userId, await this.profile(h.userId, tx));
    const r1 = profiles.get(d.p1Id)!.rating;
    const r2 = d.p2Id ? profiles.get(d.p2Id)!.rating : (d.botRating ?? DUEL_START_RATING);
    const score: 0 | 0.5 | 1 = outcome === 'p1' ? 1 : outcome === 'p2' ? 0 : 0.5;
    const [delta1, delta2] = d.kind === 'ranked' ? eloDelta(r1, r2, score) : [0, 0];
    const dealt = await tx.duelAnswer.groupBy({ by: ['side'], where: { duelId: d.id }, _sum: { damage: true } });

    for (const h of humans) {
      const p = profiles.get(h.userId)!;
      const result = this.resultFor(outcome, h.side);
      const delta = h.side === 1 ? delta1 : delta2;
      if (d.kind === 'ranked') {
        const streak = result === 'win' ? p.streak + 1 : result === 'draw' ? p.streak : 0;
        await tx.duelProfile.update({
          where: { userId: h.userId },
          data: {
            rating: p.rating + delta,
            peakRating: Math.max(p.peakRating, p.rating + delta),
            wins: { increment: result === 'win' ? 1 : 0 },
            losses: { increment: result === 'loss' ? 1 : 0 },
            draws: { increment: result === 'draw' ? 1 : 0 },
            streak,
            bestStreak: Math.max(p.bestStreak, streak),
            damageDealt: { increment: dealt.find((x) => x.side === h.side)?._sum.damage ?? 0 },
            lastDuelAt: now,
          },
        });
      } else {
        await tx.duelProfile.update({ where: { userId: h.userId }, data: { lastDuelAt: now } });
      }
      const reward = this.reward(d.kind as DuelKind, result, reason, h.side, outcome);
      if (reward.xp > 0 || reward.coins > 0) {
        await tx.user.update({ where: { id: h.userId }, data: { xp: { increment: reward.xp }, coins: { increment: reward.coins } } });
        if (reward.xp > 0) await tx.xpEvent.create({ data: { userId: h.userId, amount: reward.xp, reason: 'duel', refId: d.id } });
      }
    }
    return tx.duel.update({ where: { id: d.id }, data: { status: 'finished', outcome, endReason: reason, endedAt: now, rating1: r1, rating2: r2, delta1, delta2 } });
  }

  private resultFor(outcome: string | null, side: Side): 'win' | 'loss' | 'draw' {
    return outcome === 'draw' ? 'draw' : outcome === `p${side}` ? 'win' : 'loss';
  }

  /** Abandonner ne rapporte rien ; l'entraînement contre l'IA rapporte moitié moins. */
  private reward(kind: DuelKind, result: 'win' | 'loss' | 'draw', reason: string | null, side: Side, outcome: string | null) {
    if (reason === 'forfeit' && outcome !== `p${side}`) return { xp: 0, coins: 0 };
    const r = duelReward(result);
    return kind === 'practice' ? { xp: Math.floor(r.xp / 2), coins: Math.floor(r.coins / 2) } : r;
  }

  /** Après la clôture : l'XP compte aussi pour la journée (série, quêtes). */
  private async afterFinish(d: Duel) {
    for (const [side, userId] of [[1, d.p1Id], [2, d.p2Id]] as [Side, string | null][]) {
      if (!userId) continue;
      const reward = this.reward(d.kind as DuelKind, this.resultFor(d.outcome, side), d.endReason, side, d.outcome);
      if (reward.xp > 0) await this.activity.record(userId, { xp: reward.xp }).catch(() => undefined);
    }
  }

  private async activeDuelOf(userId: string, tx: Tx = this.prisma) {
    return tx.duel.findFirst({ where: { status: 'active', OR: [{ p1Id: userId }, { p2Id: userId }] }, orderBy: { createdAt: 'desc' } });
  }

  /** Lance un duel entre deux joueurs (ou contre l'IA) : compte à rebours puis première question. */
  private async startDuel(tx: Tx, data: { id?: string; kind: DuelKind; p1Id: string; p2Id: string | null; botName?: string; botRating?: number }, now: Date) {
    const ids = [data.p1Id, ...(data.p2Id ? [data.p2Id] : [])];
    const questions = await this.plan(`${ids.join(':')}:${now.getTime()}`, ids, tx);
    if (questions.length < 3) throw new BadRequestException('Pas assez de notions pour un duel.');
    const fields = {
      status: 'active',
      questions: questions as unknown as Prisma.InputJsonValue,
      startedAt: now,
      roundStartsAt: new Date(now.getTime() + DUEL_RULES.countdownMs),
      seen1: now,
      seen2: data.p2Id ? now : null,
      hp1: DUEL_RULES.hp,
      hp2: DUEL_RULES.hp,
    };
    if (data.id) return tx.duel.update({ where: { id: data.id }, data: fields });
    return tx.duel.create({ data: { kind: data.kind, p1Id: data.p1Id, p2Id: data.p2Id, botName: data.botName, botRating: data.botRating, ...fields } });
  }

  // ───────────── Matchmaking ─────────────

  async joinQueue(userId: string): Promise<DuelQueueDto> {
    const now = this.clock.now();
    await this.profile(userId);
    const active = await this.activeDuelOf(userId);
    if (active) return { status: 'matched', duelId: active.id };
    await this.prisma.duelProfile.update({ where: { userId }, data: { queuedAt: now, queueSeenAt: now } });
    return this.tryMatch(userId);
  }

  async pollQueue(userId: string): Promise<DuelQueueDto> {
    const active = await this.activeDuelOf(userId);
    if (active) return { status: 'matched', duelId: active.id };
    const p = await this.profile(userId);
    if (!p.queuedAt) return { status: 'idle' };
    await this.prisma.duelProfile.update({ where: { userId }, data: { queueSeenAt: this.clock.now() } });
    return this.tryMatch(userId);
  }

  async leaveQueue(userId: string): Promise<DuelQueueDto> {
    await this.profile(userId);
    await this.prisma.duelProfile.update({ where: { userId }, data: { queuedAt: null, queueSeenAt: null } });
    return { status: 'idle' };
  }

  /** Associe le joueur au plus proche en classement parmi ceux qui cherchent (verrou global de file). */
  private async tryMatch(userId: string): Promise<DuelQueueDto> {
    const now = this.clock.now();
    return this.locked('duel-queue', async (tx) => {
      const active = await this.activeDuelOf(userId, tx);
      if (active) return { status: 'matched' as const, duelId: active.id };
      const me = await tx.duelProfile.findUniqueOrThrow({ where: { userId } });
      if (!me.queuedAt) return { status: 'idle' as const };
      const others = await tx.duelProfile.findMany({
        where: { userId: { not: userId }, queuedAt: { not: null }, queueSeenAt: { gte: new Date(now.getTime() - DUEL_RULES.queueTtlMs) } },
        orderBy: { queuedAt: 'asc' },
        take: 50,
      });
      if (others.length === 0) return { status: 'searching' as const, since: me.queuedAt.toISOString() };
      const opp = others.reduce((best, o) => (Math.abs(o.rating - me.rating) < Math.abs(best.rating - me.rating) ? o : best));
      const [p1, p2] = opp.queuedAt! <= me.queuedAt ? [opp.userId, userId] : [userId, opp.userId];
      const duel = await this.startDuel(tx, { kind: 'ranked', p1Id: p1, p2Id: p2 }, now);
      await tx.duelProfile.updateMany({ where: { userId: { in: [userId, opp.userId] } }, data: { queuedAt: null, queueSeenAt: null } });
      return { status: 'matched' as const, duelId: duel.id };
    });
  }

  /** Entraînement contre un rōnin (IA) d'un niveau proche : sans effet sur le classement. */
  async practice(userId: string): Promise<{ duelId: string }> {
    const now = this.clock.now();
    const p = await this.profile(userId);
    return this.locked(`duel-user:${userId}`, async (tx) => {
      const active = await this.activeDuelOf(userId, tx);
      if (active) return { duelId: active.id };
      await tx.duelProfile.update({ where: { userId }, data: { queuedAt: null, queueSeenAt: null } });
      const botRating = Math.max(900, p.rating + randomInt(-60, 61));
      const duel = await this.startDuel(tx, { kind: 'practice', p1Id: userId, p2Id: null, botName: BOT_NAMES[randomInt(BOT_NAMES.length)], botRating }, now);
      return { duelId: duel.id };
    });
  }

  // ───────────── Défis ─────────────

  async challenge(userId: string, target: { code?: string; userId?: string }): Promise<{ duelId: string }> {
    await this.profile(userId);
    const code = target.code?.trim().toUpperCase().replace(/^(KQ)?-?/, 'KQ-');
    const opp = target.userId
      ? await this.prisma.duelProfile.findUnique({ where: { userId: target.userId } })
      : code
        ? await this.prisma.duelProfile.findUnique({ where: { code } })
        : null;
    if (!opp) throw new NotFoundException('Aucun duelliste avec ce code.');
    if (opp.userId === userId) throw new BadRequestException('Tu ne peux pas te défier toi-même.');
    const now = this.clock.now();
    const since = new Date(now.getTime() - DUEL_RULES.inviteTtlMs);
    const existing = await this.prisma.duel.findFirst({ where: { status: 'pending', createdAt: { gte: since }, OR: [{ p1Id: userId, p2Id: opp.userId }, { p1Id: opp.userId, p2Id: userId }] } });
    if (existing) return { duelId: existing.id };
    const pendingForTarget = await this.prisma.duel.count({ where: { status: 'pending', p2Id: opp.userId, createdAt: { gte: since } } });
    if (pendingForTarget >= 5) throw new ConflictException('Ce joueur a déjà trop de défis en attente.');
    const duel = await this.prisma.duel.create({ data: { kind: 'friendly', status: 'pending', p1Id: userId, p2Id: opp.userId, questions: [], seen1: now } });
    return { duelId: duel.id };
  }

  async accept(userId: string, id: string): Promise<{ duelId: string }> {
    const now = this.clock.now();
    const res = await this.locked(id, async (tx) => {
      const found = await tx.duel.findUnique({ where: { id } });
      if (!found || found.p2Id !== userId) throw new NotFoundException('Défi introuvable.');
      const { duel: d } = await this.advance(tx, found, now);
      if (d.status !== 'pending') throw new ConflictException(d.status === 'expired' ? 'Ce défi a expiré.' : 'Ce défi n’est plus disponible.');
      for (const u of [d.p1Id, userId]) if (await this.activeDuelOf(u, tx)) throw new ConflictException(u === userId ? 'Tu as déjà un duel en cours.' : 'Ton adversaire est déjà en duel.');
      await tx.duelProfile.updateMany({ where: { userId: { in: [d.p1Id, userId] } }, data: { queuedAt: null, queueSeenAt: null } });
      return this.startDuel(tx, { id: d.id, kind: 'friendly', p1Id: d.p1Id, p2Id: userId }, now);
    });
    return { duelId: res.id };
  }

  async decline(userId: string, id: string) {
    const d = await this.prisma.duel.findUnique({ where: { id } });
    if (!d || d.status !== 'pending' || (d.p1Id !== userId && d.p2Id !== userId)) throw new NotFoundException('Défi introuvable.');
    await this.prisma.duel.updateMany({ where: { id, status: 'pending' }, data: { status: d.p1Id === userId ? 'cancelled' : 'declined', endedAt: this.clock.now() } });
    return { ok: true };
  }

  async forfeit(userId: string, id: string): Promise<DuelStateDto> {
    const now = this.clock.now();
    let finished: Duel | null = null;
    await this.locked(id, async (tx) => {
      const d = await tx.duel.findUnique({ where: { id } });
      const side = d && sideOf(d, userId);
      if (!d || !side) throw new NotFoundException('Duel introuvable.');
      const adv = await this.advance(tx, d, now);
      if (adv.finished) finished = adv.duel;
      if (adv.duel.status !== 'active') return;
      finished = await this.finish(tx, adv.duel, `p${other(side)}` as 'p1' | 'p2', 'forfeit', now);
    });
    if (finished) await this.afterFinish(finished);
    return this.state(userId, id);
  }

  // ───────────── En duel ─────────────

  async state(userId: string, id: string): Promise<DuelStateDto> {
    const now = this.clock.now();
    const { duel, finished } = await this.locked(id, async (tx) => {
      const d = await tx.duel.findUnique({ where: { id } });
      const side = d && sideOf(d, userId);
      if (!d || !side) throw new NotFoundException('Duel introuvable.');
      if (d.status === 'active') await tx.duel.update({ where: { id }, data: side === 1 ? { seen1: now } : { seen2: now } });
      return this.advance(tx, { ...d, ...(side === 1 ? { seen1: now } : { seen2: now }) }, now);
    });
    if (finished) await this.afterFinish(duel);
    return this.toState(userId, duel, now);
  }

  async answer(userId: string, id: string, round: number, given: string): Promise<DuelStateDto> {
    const now = this.clock.now();
    const { duel, finished } = await this.locked(id, async (tx) => {
      const d = await tx.duel.findUnique({ where: { id } });
      const side = d && sideOf(d, userId);
      if (!d || !side) throw new NotFoundException('Duel introuvable.');
      const seen = side === 1 ? { seen1: now } : { seen2: now };
      if (d.status === 'active') await tx.duel.update({ where: { id }, data: seen });
      const adv = await this.advance(tx, { ...d, ...seen }, now);
      const cur = adv.duel;
      if (adv.finished || cur.status !== 'active') return adv;
      if (cur.round !== round || !cur.roundStartsAt || now < cur.roundStartsAt) throw new ConflictException('Cette question n’est plus en jeu.');
      const ms = now.getTime() - cur.roundStartsAt.getTime();
      if (ms > DUEL_RULES.roundMs + DUEL_RULES.graceMs) throw new ConflictException('Temps écoulé.');
      const exists = await tx.duelAnswer.findUnique({ where: { duelId_round_side: { duelId: id, round, side } } });
      if (exists) throw new ConflictException('Tu as déjà répondu.');
      const q = (cur.questions as unknown as Question[])[round];
      const correct = checkAnswer(q, given);
      const hit = duelDamage(correct, ms, side === 1 ? cur.streak1 : cur.streak2);
      await tx.duelAnswer.create({ data: { duelId: id, round, side, answer: given.slice(0, 200), correct, ms, damage: hit.damage, critical: hit.critical } });
      return this.advance(tx, cur, now);
    });
    if (finished) await this.afterFinish(duel);
    return this.toState(userId, duel, now);
  }

  private sideResult(a: DuelAnswer | undefined, streakBefore: number): DuelSideResultDto {
    if (!a) return { answer: null, correct: false, ms: null, damage: 0, critical: false, combo: 0 };
    return { answer: a.answer, correct: a.correct, ms: a.ms, damage: a.damage, critical: a.critical, combo: a.correct ? streakBefore + 1 : 0 };
  }

  private async toState(userId: string, d: Duel, now: Date): Promise<DuelStateDto> {
    const side = sideOf(d, userId)!;
    const oppSide = other(side);
    const oppId = side === 1 ? d.p2Id : d.p1Id;
    const [mePlayer, oppPlayer] = await Promise.all([this.player(userId), oppId ? this.player(oppId) : Promise.resolve(this.botPlayer(d))]);
    const questions = d.questions as unknown as Question[];
    const total = Math.min(DUEL_RULES.rounds, questions.length);
    const live = d.status === 'active' && !!d.roundStartsAt && now >= d.roundStartsAt && d.round < total;
    const rounds = d.round > 0 ? [d.round - 1, d.round] : [d.round];
    const answers = d.status === 'pending' ? [] : await this.prisma.duelAnswer.findMany({ where: { duelId: d.id, round: { in: rounds } } });
    const hp = (s: Side) => (s === 1 ? d.hp1 : d.hp2);
    const streak = (s: Side) => (s === 1 ? d.streak1 : d.streak2);
    const mineNow = live ? answers.find((a) => a.round === d.round && a.side === side) : undefined;
    const oppNow = live ? answers.find((a) => a.round === d.round && a.side === oppSide) : undefined;
    const bot = !d.p2Id && live ? botAnswer(d.id, d.round, d.botRating ?? DUEL_START_RATING) : null;

    let last: DuelStateDto['last'] = null;
    if (d.round > 0 && questions[d.round - 1]) {
      const r = d.round - 1;
      const a = (s: Side) => answers.find((x) => x.round === r && x.side === s);
      // Combo avant cette question : on le déduit du combo actuel
      const before = (s: Side) => (a(s)?.correct ? Math.max(0, streak(s) - 1) : 0);
      last = {
        question: this.publicQuestion(questions[r], r),
        answer: String(questions[r].answer),
        me: this.sideResult(a(side), before(side)),
        opponent: this.sideResult(a(oppSide), before(oppSide)),
      };
    }

    let result: DuelStateDto['result'] = null;
    if (d.status === 'finished') {
      const outcome = this.resultFor(d.outcome, side);
      const before = (side === 1 ? d.rating1 : d.rating2) ?? mePlayer.rating;
      const delta = (side === 1 ? d.delta1 : d.delta2) ?? 0;
      const reward = this.reward(d.kind as DuelKind, outcome, d.endReason, side, d.outcome);
      result = { outcome, endReason: d.endReason, ratingBefore: before, ratingAfter: before + delta, delta, rankBefore: rankDto(before), rankAfter: rankDto(before + delta), xp: reward.xp, coins: reward.coins };
    }
    const oppSeen = oppSide === 1 ? d.seen1 : d.seen2;
    return {
      id: d.id,
      kind: d.kind as DuelKind,
      status: d.status as DuelStatus,
      serverNow: now.toISOString(),
      rules: { hp: DUEL_RULES.hp, rounds: total || DUEL_RULES.rounds, roundMs: DUEL_RULES.roundMs, revealMs: DUEL_RULES.revealMs },
      me: { ...mePlayer, hp: hp(side), side, combo: streak(side) },
      opponent: { ...oppPlayer, hp: hp(oppSide), combo: streak(oppSide), online: !oppId || (!!oppSeen && now.getTime() - oppSeen.getTime() < ONLINE_MS) },
      round: d.round,
      roundStartsAt: d.roundStartsAt?.toISOString() ?? null,
      question: live ? this.publicQuestion(questions[d.round], d.round) : null,
      mine: mineNow ? this.sideResult(mineNow, streak(side)) : null,
      opponentAnswered: !!oppNow || (!!bot && !!d.roundStartsAt && now.getTime() >= d.roundStartsAt.getTime() + bot.ms),
      last,
      expiresAt: d.status === 'pending' ? new Date(d.createdAt.getTime() + DUEL_RULES.inviteTtlMs).toISOString() : null,
      result,
    };
  }

  // ───────────── Hall, classement, recherche ─────────────

  async lobby(userId: string): Promise<DuelLobbyDto> {
    const now = this.clock.now();
    const p = await this.profile(userId);
    const since = new Date(now.getTime() - DUEL_RULES.inviteTtlMs);
    // Les défis trop anciens expirent
    await this.prisma.duel.updateMany({ where: { status: 'pending', createdAt: { lt: since }, OR: [{ p1Id: userId }, { p2Id: userId }] }, data: { status: 'expired', endedAt: now } });
    const [active, incoming, outgoing, history, above, players] = await Promise.all([
      this.activeDuelOf(userId),
      this.prisma.duel.findMany({ where: { status: 'pending', p2Id: userId }, orderBy: { createdAt: 'desc' } }),
      this.prisma.duel.findMany({ where: { status: 'pending', p1Id: userId }, orderBy: { createdAt: 'desc' } }),
      this.prisma.duel.findMany({
        where: { status: { in: ['finished'] }, OR: [{ p1Id: userId }, { p2Id: userId }] },
        orderBy: { endedAt: 'desc' },
        take: 10,
        include: { p1: { select: { displayName: true } }, p2: { select: { displayName: true } } },
      }),
      this.prisma.duelProfile.count({ where: { rating: { gt: p.rating }, OR: [{ wins: { gt: 0 } }, { losses: { gt: 0 } }, { draws: { gt: 0 } }] } }),
      this.prisma.duelProfile.count({ where: { OR: [{ wins: { gt: 0 } }, { losses: { gt: 0 } }, { draws: { gt: 0 } }] } }),
    ]);
    const invite = async (d: Duel, who: string): Promise<DuelInviteDto> => ({ id: d.id, player: await this.player(who), expiresAt: new Date(d.createdAt.getTime() + DUEL_RULES.inviteTtlMs).toISOString() });
    const queued = p.queuedAt && p.queueSeenAt && now.getTime() - p.queueSeenAt.getTime() < DUEL_RULES.queueTtlMs;
    return {
      profile: {
        code: p.code,
        rating: p.rating,
        peakRating: p.peakRating,
        rank: rankDto(p.rating),
        wins: p.wins,
        losses: p.losses,
        draws: p.draws,
        streak: p.streak,
        bestStreak: p.bestStreak,
        damageDealt: p.damageDealt,
        position: above + 1,
        players: Math.max(players, above + 1),
      },
      activeDuelId: active?.id ?? null,
      searching: queued ? { since: p.queuedAt!.toISOString() } : null,
      invites: await Promise.all(incoming.map((d) => invite(d, d.p1Id))),
      sent: await Promise.all(outgoing.map((d) => invite(d, d.p2Id!))),
      history: history.map((d): DuelHistoryDto => {
        const side = sideOf(d, userId)!;
        return {
          id: d.id,
          kind: d.kind as DuelKind,
          opponent: side === 1 ? (d.p2?.displayName ?? d.botName ?? 'Rōnin') : d.p1.displayName,
          result: this.resultFor(d.outcome, side),
          delta: d.kind === 'ranked' ? ((side === 1 ? d.delta1 : d.delta2) ?? 0) : null,
          myHp: side === 1 ? d.hp1 : d.hp2,
          oppHp: side === 1 ? d.hp2 : d.hp1,
          endReason: d.endReason,
          endedAt: d.endedAt?.toISOString() ?? null,
        };
      }),
      online: true,
      rules: { hp: DUEL_RULES.hp, rounds: DUEL_RULES.rounds, roundMs: DUEL_RULES.roundMs },
    };
  }

  async invites(userId: string): Promise<DuelInviteDto[]> {
    const since = new Date(this.clock.now().getTime() - DUEL_RULES.inviteTtlMs);
    const rows = await this.prisma.duel.findMany({ where: { status: 'pending', p2Id: userId, createdAt: { gte: since } }, orderBy: { createdAt: 'desc' }, take: 5 });
    return Promise.all(rows.map(async (d) => ({ id: d.id, player: await this.player(d.p1Id), expiresAt: new Date(d.createdAt.getTime() + DUEL_RULES.inviteTtlMs).toISOString() })));
  }

  async leaderboard(userId: string, sort: 'rating' | 'wins'): Promise<DuelLeaderboardDto> {
    const me = await this.profile(userId);
    const played = { OR: [{ wins: { gt: 0 } }, { losses: { gt: 0 } }, { draws: { gt: 0 } }] };
    const orderBy: Prisma.DuelProfileOrderByWithRelationInput[] = sort === 'wins' ? [{ wins: 'desc' }, { rating: 'desc' }] : [{ rating: 'desc' }, { wins: 'desc' }];
    const rows = await this.prisma.duelProfile.findMany({ where: played, orderBy, take: 50, include: { user: { select: { displayName: true, avatar: true } } } });
    const hasPlayed = me.wins + me.losses + me.draws > 0;
    const position = hasPlayed
      ? (await this.prisma.duelProfile.count({
          where: { ...played, ...(sort === 'wins' ? { OR: [{ wins: { gt: me.wins } }, { wins: me.wins, rating: { gt: me.rating } }] } : { OR: [{ rating: { gt: me.rating } }, { rating: me.rating, wins: { gt: me.wins } }] }) },
        })) + 1
      : 0;
    return {
      sort,
      entries: rows.map((r, i) => ({ position: i + 1, userId: r.userId, name: r.user.displayName, avatar: (r.user.avatar as AvatarConfig | null) ?? null, rating: r.rating, rank: rankDto(r.rating), wins: r.wins, losses: r.losses, me: r.userId === userId })),
      me: hasPlayed ? { position, rating: me.rating, wins: me.wins } : null,
    };
  }

  /** Recherche d'un duelliste par son code (KQ-XXXXXX) ou son nom. */
  async search(userId: string, q: string): Promise<DuelPlayerSearchDto> {
    const term = q.trim();
    if (term.length < 2) return { players: [] };
    const code = term.toUpperCase().replace(/^(KQ)?-?/, 'KQ-');
    const rows = await this.prisma.duelProfile.findMany({
      where: { userId: { not: userId }, OR: [{ code }, { user: { displayName: { contains: term, mode: 'insensitive' } } }] },
      include: { user: { select: { displayName: true, avatar: true } } },
      orderBy: { rating: 'desc' },
      take: 10,
    });
    return { players: rows.map((r) => ({ userId: r.userId, code: r.code, name: r.user.displayName, avatar: (r.user.avatar as AvatarConfig | null) ?? null, rating: r.rating, rank: rankDto(r.rating), isBot: false })) };
  }
}
