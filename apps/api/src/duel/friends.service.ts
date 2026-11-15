import { BadRequestException, ConflictException, ForbiddenException, Injectable, NotFoundException } from '@nestjs/common';
import type { DuelProfile, Friendship, Prisma } from '@prisma/client';
import { DUEL_RULES } from '@koto/learning-engine';
import type { AvatarConfig, FriendActionDto, FriendDto, FriendPlayerDto, FriendRelation, FriendRequestDto, FriendsDto } from '@koto/shared';
import { PrismaService } from '../common/prisma.service';
import { ClockService } from '../common/clock.service';
import { DuelService, rankDto } from './duel.service';

type Tx = Prisma.TransactionClient;

export const FRIEND_LIMITS = {
  /** Amis au plus */
  friends: 200,
  /** Demandes envoyées en attente au plus */
  pendingOut: 30,
  /** Un joueur est « en ligne » s'il a donné signe de vie il y a moins de… */
  onlineMs: 45_000,
  /** Fréquence maximale d'écriture du signe de vie */
  heartbeatMs: 20_000,
};

/** Amis : demandes par code de duelliste ou depuis la recherche, présence en ligne, défis simplifiés. */
@Injectable()
export class FriendsService {
  constructor(private prisma: PrismaService, private clock: ClockService, private duels: DuelService) {}

  /** Une seule opération à la fois par paire de joueurs (évite les doublons A→B et B→A simultanés). */
  private pairLocked<T>(a: string, b: string, fn: (tx: Tx) => Promise<T>): Promise<T> {
    const key = `friend:${[a, b].sort().join(':')}`;
    return this.prisma.$transaction(async (tx) => {
      await tx.$executeRaw`SELECT pg_advisory_xact_lock(hashtext(${key}))`;
      return fn(tx);
    });
  }

  private between(a: string, b: string, tx: Tx = this.prisma) {
    return tx.friendship.findFirst({ where: { OR: [{ requesterId: a, addresseeId: b }, { requesterId: b, addresseeId: a }] } });
  }

  private async players(ids: string[]): Promise<Map<string, FriendPlayerDto & { seenAt: Date | null }>> {
    if (!ids.length) return new Map();
    for (const id of ids) await this.duels.profile(id); // profil créé au besoin
    const rows = await this.prisma.duelProfile.findMany({ where: { userId: { in: ids } }, include: { user: { select: { displayName: true, avatar: true } } } });
    return new Map(
      rows.map((r) => [
        r.userId,
        { userId: r.userId, code: r.code, name: r.user.displayName, avatar: (r.user.avatar as AvatarConfig | null) ?? null, rating: r.rating, rank: rankDto(r.rating), isBot: false, seenAt: r.seenAt },
      ]),
    );
  }

  private strip(p: FriendPlayerDto & { seenAt?: Date | null }): FriendPlayerDto {
    const { seenAt: _seen, ...rest } = p;
    return rest;
  }

  /** Signe de vie (appelé par le sondage des défis, toutes les 10 s quand l'application est ouverte). */
  async heartbeat(userId: string, profile?: DuelProfile) {
    const now = this.clock.now();
    const p = profile ?? (await this.duels.profile(userId));
    if (p.seenAt && now.getTime() - p.seenAt.getTime() < FRIEND_LIMITS.heartbeatMs) return;
    await this.prisma.duelProfile.update({ where: { userId }, data: { seenAt: now } });
  }

  async list(userId: string): Promise<FriendsDto> {
    await this.heartbeat(userId);
    const now = this.clock.now();
    const rows = await this.prisma.friendship.findMany({ where: { OR: [{ requesterId: userId }, { addresseeId: userId }] }, orderBy: { createdAt: 'desc' } });
    const otherOf = (f: Friendship) => (f.requesterId === userId ? f.addresseeId : f.requesterId);
    const players = await this.players(rows.map(otherOf));
    const accepted = rows.filter((f) => f.status === 'accepted');
    const friendIds = accepted.map(otherOf);

    // Bilan des duels terminés et défis en attente avec chaque ami
    const [finished, pending] = friendIds.length
      ? await Promise.all([
          this.prisma.duel.findMany({
            where: { status: 'finished', kind: { in: ['friendly', 'ranked'] }, OR: [{ p1Id: userId, p2Id: { in: friendIds } }, { p2Id: userId, p1Id: { in: friendIds } }] },
            select: { p1Id: true, p2Id: true, outcome: true },
          }),
          this.prisma.duel.findMany({
            where: { status: 'pending', createdAt: { gte: new Date(now.getTime() - DUEL_RULES.inviteTtlMs) }, OR: [{ p1Id: userId, p2Id: { in: friendIds } }, { p2Id: userId, p1Id: { in: friendIds } }] },
            select: { id: true, p1Id: true, p2Id: true },
          }),
        ])
      : [[], []];

    const friends = accepted
      .map((f): FriendDto => {
        const other = otherOf(f);
        const p = players.get(other)!;
        const record = { wins: 0, losses: 0, draws: 0 };
        for (const d of finished) {
          if (!((d.p1Id === userId && d.p2Id === other) || (d.p2Id === userId && d.p1Id === other))) continue;
          const mine = d.p1Id === userId ? 'p1' : 'p2';
          if (d.outcome === 'draw') record.draws++;
          else if (d.outcome === mine) record.wins++;
          else record.losses++;
        }
        const pend = pending.find((d) => (d.p1Id === userId && d.p2Id === other) || (d.p2Id === userId && d.p1Id === other));
        return {
          id: f.id,
          player: this.strip(p),
          online: !!p.seenAt && now.getTime() - p.seenAt.getTime() < FRIEND_LIMITS.onlineMs,
          lastSeenAt: p.seenAt?.toISOString() ?? null,
          since: (f.acceptedAt ?? f.createdAt).toISOString(),
          record,
          pendingDuelId: pend?.id ?? null,
        };
      })
      .sort((a, b) => Number(b.online) - Number(a.online) || (b.lastSeenAt ?? '').localeCompare(a.lastSeenAt ?? '') || a.player.name.localeCompare(b.player.name));

    const request = (f: Friendship): FriendRequestDto => ({ id: f.id, player: this.strip(players.get(otherOf(f))!), createdAt: f.createdAt.toISOString() });
    return {
      friends,
      incoming: rows.filter((f) => f.status === 'pending' && f.addresseeId === userId).map(request),
      outgoing: rows.filter((f) => f.status === 'pending' && f.requesterId === userId).map(request),
      limits: { friends: FRIEND_LIMITS.friends },
    };
  }

  /** Demandes reçues (sondées par l'application pour afficher une alerte). */
  async requests(userId: string): Promise<FriendRequestDto[]> {
    const rows = await this.prisma.friendship.findMany({ where: { addresseeId: userId, status: 'pending' }, orderBy: { createdAt: 'desc' }, take: 5 });
    const players = await this.players(rows.map((r) => r.requesterId));
    return rows.map((f) => ({ id: f.id, player: this.strip(players.get(f.requesterId)!), createdAt: f.createdAt.toISOString() }));
  }

  /** Lien d'amitié avec chacun des joueurs donnés (pour la recherche). */
  async relations(userId: string, ids: string[]): Promise<Map<string, { relation: FriendRelation; id: string }>> {
    if (!ids.length) return new Map();
    const rows = await this.prisma.friendship.findMany({ where: { OR: [{ requesterId: userId, addresseeId: { in: ids } }, { addresseeId: userId, requesterId: { in: ids } }] } });
    return new Map(
      rows.map((f) => {
        const other = f.requesterId === userId ? f.addresseeId : f.requesterId;
        const relation: FriendRelation = f.status === 'accepted' ? 'friend' : f.requesterId === userId ? 'outgoing' : 'incoming';
        return [other, { relation, id: f.id }];
      }),
    );
  }

  private async countFriends(userId: string, tx: Tx) {
    return tx.friendship.count({ where: { status: 'accepted', OR: [{ requesterId: userId }, { addresseeId: userId }] } });
  }

  /** Envoie une demande (ou accepte directement si l'autre joueur nous l'avait déjà demandé). */
  async request(userId: string, target: { code?: string; userId?: string }): Promise<FriendActionDto> {
    await this.duels.profile(userId);
    const code = target.code?.trim().toUpperCase().replace(/^(KQ)?-?/, 'KQ-');
    const opp = target.userId
      ? await this.prisma.duelProfile.findUnique({ where: { userId: target.userId } })
      : code
        ? await this.prisma.duelProfile.findUnique({ where: { code } })
        : null;
    if (!opp) throw new NotFoundException('Aucun duelliste avec ce code.');
    if (opp.userId === userId) throw new BadRequestException('Tu ne peux pas t’ajouter toi-même.');
    const now = this.clock.now();
    const f = await this.pairLocked(userId, opp.userId, async (tx) => {
      const existing = await this.between(userId, opp.userId, tx);
      if (existing?.status === 'accepted') throw new ConflictException('Vous êtes déjà amis.');
      if (existing && existing.requesterId === userId) return existing;
      if ((await this.countFriends(userId, tx)) >= FRIEND_LIMITS.friends) throw new ConflictException(`Tu as atteint la limite de ${FRIEND_LIMITS.friends} amis.`);
      if (existing) {
        // L'autre joueur nous avait déjà envoyé une demande : on l'accepte.
        if ((await this.countFriends(opp.userId, tx)) >= FRIEND_LIMITS.friends) throw new ConflictException('Ce joueur a atteint sa limite d’amis.');
        return tx.friendship.update({ where: { id: existing.id }, data: { status: 'accepted', acceptedAt: now } });
      }
      const pendingOut = await tx.friendship.count({ where: { requesterId: userId, status: 'pending' } });
      if (pendingOut >= FRIEND_LIMITS.pendingOut) throw new ConflictException('Trop de demandes en attente : attends qu’on te réponde.');
      return tx.friendship.create({ data: { requesterId: userId, addresseeId: opp.userId, status: 'pending' } });
    });
    const p = (await this.players([opp.userId])).get(opp.userId)!;
    return { id: f.id, status: f.status as 'pending' | 'accepted', player: this.strip(p) };
  }

  async accept(userId: string, id: string): Promise<FriendActionDto> {
    const f = await this.prisma.friendship.findUnique({ where: { id } });
    if (!f || (f.addresseeId !== userId && f.requesterId !== userId)) throw new NotFoundException('Demande introuvable.');
    if (f.status === 'pending' && f.addresseeId !== userId) throw new ForbiddenException('Seul le joueur invité peut accepter la demande.');
    const updated = await this.pairLocked(f.requesterId, f.addresseeId, async (tx) => {
      const cur = await tx.friendship.findUnique({ where: { id } });
      if (!cur) throw new NotFoundException('Demande introuvable.');
      if (cur.status === 'accepted') return cur;
      if ((await this.countFriends(userId, tx)) >= FRIEND_LIMITS.friends) throw new ConflictException(`Tu as atteint la limite de ${FRIEND_LIMITS.friends} amis.`);
      if ((await this.countFriends(cur.requesterId, tx)) >= FRIEND_LIMITS.friends) throw new ConflictException('Ce joueur a atteint sa limite d’amis.');
      return tx.friendship.update({ where: { id }, data: { status: 'accepted', acceptedAt: this.clock.now() } });
    });
    const p = (await this.players([updated.requesterId])).get(updated.requesterId)!;
    return { id: updated.id, status: 'accepted', player: this.strip(p) };
  }

  /** Refuser, annuler une demande ou retirer un ami : la ligne disparaît (sans prévenir l'autre joueur). */
  async remove(userId: string, id: string) {
    const res = await this.prisma.friendship.deleteMany({ where: { id, OR: [{ requesterId: userId }, { addresseeId: userId }] } });
    if (res.count === 0) throw new NotFoundException('Ami ou demande introuvable.');
    return { ok: true };
  }
}
