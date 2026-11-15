import { Injectable, Logger } from '@nestjs/common';
import { Cron, CronExpression } from '@nestjs/schedule';
import { config } from '../config';
import { PrismaService } from './prisma.service';
import { ClockService } from './clock.service';

/** Comptes supprimés après 3 ans sans visite (durée annoncée dans la politique de confidentialité). */
export const INACTIVE_ACCOUNT_DAYS = 3 * 365;

/**
 * Durées de conservation : chaque nuit, suppression des comptes inactifs depuis 3 ans
 * (avec toutes leurs données, en cascade), des sessions expirées et des liens de
 * réinitialisation périmés.
 */
@Injectable()
export class RetentionService {
  private readonly logger = new Logger('Conservation');

  constructor(private prisma: PrismaService, private clock: ClockService) {}

  @Cron(CronExpression.EVERY_DAY_AT_3AM)
  async nightly() {
    if (!config.schedulerEnabled) return;
    await this.purge().catch((e) => this.logger.error(`Purge impossible : ${(e as Error).message}`));
  }

  async purge() {
    const now = this.clock.now();
    const limit = new Date(now.getTime() - INACTIVE_ACCOUNT_DAYS * 86_400_000);
    const users = await this.prisma.user.deleteMany({ where: { OR: [{ lastSeenAt: { lt: limit } }, { lastSeenAt: null, createdAt: { lt: limit } }] } });
    const sessions = await this.prisma.session.deleteMany({ where: { expiresAt: { lt: now } } });
    const resets = await this.prisma.passwordResetToken.deleteMany({ where: { OR: [{ expiresAt: { lt: now } }, { usedAt: { not: null } }] } });
    if (users.count || sessions.count || resets.count)
      this.logger.log(`Comptes inactifs supprimés : ${users.count} · sessions expirées : ${sessions.count} · liens de réinitialisation : ${resets.count}`);
    return { users: users.count, sessions: sessions.count, resets: resets.count };
  }
}
