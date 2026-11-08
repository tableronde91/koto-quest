import { BadRequestException, ConflictException, ForbiddenException, Injectable, NotFoundException } from '@nestjs/common';
import { readFileSync } from 'fs';
import { resolve } from 'path';
import { ACQUIRE_ERRORS_FR, AvatarConfig, CosmeticCatalog, checkAcquire, normalizeAvatar, ownedSkus, validateAvatar } from '@koto/learning-engine';
import type { ShopDto } from '@koto/shared';
import { Prisma } from '@prisma/client';
import { PrismaService } from '../common/prisma.service';

const CATALOG_PATH = resolve(__dirname, '../../../../content/cosmetics/catalog.json');

@Injectable()
export class ShopService {
  private catalog: CosmeticCatalog | null = null;

  constructor(private prisma: PrismaService) {}

  load(): CosmeticCatalog {
    this.catalog ??= JSON.parse(readFileSync(CATALOG_PATH, 'utf8')) as CosmeticCatalog;
    return this.catalog;
  }

  private async state(userId: string) {
    const [user, inventory, bosses, worlds] = await Promise.all([
      this.prisma.user.findUniqueOrThrow({ where: { id: userId }, select: { coins: true, avatar: true } }),
      this.prisma.inventoryItem.findMany({ where: { userId }, select: { sku: true } }),
      this.prisma.bossResult.findMany({ where: { userId, firstVictoryAt: { not: null } }, select: { worldSlug: true } }),
      this.prisma.world.findMany({ where: { bossName: { not: null } }, select: { slug: true, bossName: true } }),
    ]);
    const catalog = this.load();
    return {
      catalog,
      coins: user.coins,
      avatar: normalizeAvatar(user.avatar as Partial<AvatarConfig> | null),
      owned: ownedSkus(catalog, inventory.map((i) => i.sku)),
      defeated: new Set(bosses.map((b) => b.worldSlug)),
      bossNames: new Map(worlds.map((w) => [w.slug, w.bossName!])),
    };
  }

  async avatarOf(userId: string): Promise<AvatarConfig> {
    const u = await this.prisma.user.findUniqueOrThrow({ where: { id: userId }, select: { avatar: true } });
    return normalizeAvatar(u.avatar as Partial<AvatarConfig> | null);
  }

  async shop(userId: string): Promise<ShopDto> {
    const st = await this.state(userId);
    const equipped = new Set([st.avatar.outfit, st.avatar.hat, st.avatar.accessory, st.avatar.background].filter(Boolean));
    return {
      coins: st.coins,
      avatar: st.avatar,
      slots: st.catalog.slots,
      items: st.catalog.items.map((i) => ({
        ...i,
        owned: st.owned.has(i.sku),
        equipped: equipped.has(i.sku),
        lockedBy: i.unlockBoss && !st.defeated.has(i.unlockBoss) ? (st.bossNames.get(i.unlockBoss) ?? 'un gardien') : null,
      })),
    };
  }

  /** Achat (pièces) ou réclamation d'un trophée. Le débit est conditionnel : jamais de solde négatif. */
  async acquire(userId: string, sku: string): Promise<ShopDto> {
    const st = await this.state(userId);
    const check = checkAcquire(st.catalog, sku, { coins: st.coins, owned: st.owned, defeatedBosses: st.defeated });
    if (!check.ok) {
      const msg = ACQUIRE_ERRORS_FR[check.error];
      if (check.error === 'unknown_item') throw new NotFoundException(msg);
      if (check.error === 'already_owned') throw new ConflictException(msg);
      if (check.error === 'boss_required') throw new ForbiddenException(msg);
      throw new BadRequestException(msg);
    }
    try {
      await this.prisma.$transaction(async (tx) => {
        // 1) On réserve l'objet : la contrainte d'unicité bloque un second achat simultané du même objet.
        await tx.inventoryItem.create({ data: { userId, sku } });
        // 2) Débit conditionnel : jamais de solde négatif ; en cas d'échec, la réservation est annulée.
        if (check.cost > 0) {
          const debit = await tx.user.updateMany({ where: { id: userId, coins: { gte: check.cost } }, data: { coins: { decrement: check.cost } } });
          if (debit.count === 0) throw new BadRequestException(ACQUIRE_ERRORS_FR.not_enough_coins);
        }
      });
    } catch (e) {
      const unique = (e instanceof Prisma.PrismaClientKnownRequestError && e.code === 'P2002') || /unique constraint/i.test(String((e as Error)?.message));
      if (unique) throw new ConflictException(ACQUIRE_ERRORS_FR.already_owned);
      throw e;
    }
    return this.shop(userId);
  }

  async saveAvatar(userId: string, config: unknown): Promise<AvatarConfig> {
    const st = await this.state(userId);
    const errors = validateAvatar(config, st.catalog, st.owned);
    if (errors.length) throw new BadRequestException(errors);
    const c = config as AvatarConfig;
    const avatar: AvatarConfig = { skin: c.skin, hair: c.hair, hairColor: c.hairColor, eyes: c.eyes, outfit: c.outfit ?? null, hat: c.hat ?? null, accessory: c.accessory ?? null, background: c.background ?? null };
    await this.prisma.user.update({ where: { id: userId }, data: { avatar: avatar as unknown as Prisma.InputJsonValue } });
    return avatar;
  }
}
