import { BadRequestException, Injectable, Logger, NotFoundException } from '@nestjs/common';
import { Cron, CronExpression } from '@nestjs/schedule';
import { ReminderMode, ReminderPrefs, decideReminder, hashSeed, reminderMessage, reminderSlots } from '@koto/learning-engine';
import type { InboxItemDto, NotificationPrefsDto } from '@koto/shared';
import type { NotificationPreferences } from '@prisma/client';
import { PrismaService } from '../common/prisma.service';
import { ClockService } from '../common/clock.service';
import { config } from '../config';
import { LearningService } from '../learning/learning.service';
import { PushService } from './push.service';
import { NotificationPrefsInput, PushSubscriptionInput } from './dto';
import { asLocale, serverText } from '../common/i18n';

const NOTIFICATION_TTL_MS = 12 * 3600_000;

@Injectable()
export class NotificationsService {
  private readonly logger = new Logger('Rappels');
  private running = false;

  constructor(
    private prisma: PrismaService,
    private clock: ClockService,
    private learning: LearningService,
    private push: PushService,
  ) {}

  private toEnginePrefs(p: NotificationPreferences, timezone: string): ReminderPrefs {
    return {
      enabled: p.enabled,
      consent: p.consent,
      mode: p.mode as ReminderMode,
      customTimes: p.customTimes,
      windowStart: p.windowStart,
      windowEnd: p.windowEnd,
      quietStart: p.quietStart,
      quietEnd: p.quietEnd,
      pausedUntil: p.pausedUntil,
      timezone,
    };
  }

  async getPrefs(userId: string): Promise<NotificationPrefsDto> {
    const [p, prefs, subs] = await Promise.all([
      this.prisma.notificationPreferences.upsert({ where: { userId }, create: { userId }, update: {} }),
      this.prisma.userPreferences.findUnique({ where: { userId } }),
      this.prisma.pushSubscription.count({ where: { userId } }),
    ]);
    return {
      consent: p.consent,
      enabled: p.enabled,
      mode: p.mode as ReminderMode,
      customTimes: p.customTimes,
      windowStart: p.windowStart,
      windowEnd: p.windowEnd,
      quietStart: p.quietStart,
      quietEnd: p.quietEnd,
      pausedUntil: p.pausedUntil?.toISOString() ?? null,
      slots: reminderSlots(this.toEnginePrefs(p, prefs?.timezone ?? 'Europe/Paris')),
      pushSubscribed: subs > 0,
      vapidPublicKey: this.push.enabled ? config.vapid.publicKey : null,
    };
  }

  async updatePrefs(userId: string, dto: NotificationPrefsInput) {
    const current = await this.prisma.notificationPreferences.upsert({ where: { userId }, create: { userId }, update: {} });
    const consent = dto.consent ?? current.consent;
    let enabled = dto.enabled ?? current.enabled;
    if (dto.enabled && !consent) throw new BadRequestException('Active d’abord ton consentement aux rappels.');
    if (!consent) enabled = false; // retirer son consentement coupe tout envoi
    const { pausedUntil, ...rest } = dto;
    await this.prisma.notificationPreferences.update({
      where: { userId },
      data: {
        ...rest,
        consent,
        enabled,
        consentAt: consent && !current.consent ? this.clock.now() : consent ? current.consentAt : null,
        ...(pausedUntil !== undefined ? { pausedUntil: pausedUntil ? new Date(pausedUntil) : null } : {}),
      },
    });
    if (!consent) await this.prisma.pushSubscription.deleteMany({ where: { userId } });
    return this.getPrefs(userId);
  }

  async subscribe(userId: string, dto: PushSubscriptionInput) {
    const prefs = await this.prisma.notificationPreferences.findUnique({ where: { userId } });
    if (!prefs?.consent) throw new BadRequestException('Consentement requis avant l’abonnement aux notifications.');
    await this.prisma.pushSubscription.upsert({
      where: { endpoint: dto.endpoint },
      create: { userId, endpoint: dto.endpoint, p256dh: dto.keys.p256dh, auth: dto.keys.auth },
      update: { userId, p256dh: dto.keys.p256dh, auth: dto.keys.auth, failedCount: 0 },
    });
    return this.getPrefs(userId);
  }

  async unsubscribe(userId: string, endpoint: string) {
    await this.prisma.pushSubscription.deleteMany({ where: { userId, endpoint } });
    return this.getPrefs(userId);
  }

  async inbox(userId: string): Promise<InboxItemDto[]> {
    const now = this.clock.now();
    await this.prisma.notification.updateMany({ where: { userId, status: { in: ['pending', 'sent'] }, expiresAt: { lte: now } }, data: { status: 'expired' } });
    const rows = await this.prisma.notification.findMany({
      where: { userId, status: { in: ['pending', 'sent'] } },
      orderBy: { createdAt: 'desc' },
      take: 5,
    });
    return rows.map((n) => ({ id: n.id, title: n.title, body: n.body, questionId: n.questionId, createdAt: n.createdAt.toISOString() }));
  }

  async open(userId: string, id: string) {
    const res = await this.prisma.notification.updateMany({ where: { id, userId }, data: { status: 'opened', openedAt: this.clock.now() } });
    if (!res.count) throw new NotFoundException('Notification introuvable.');
    return { ok: true };
  }

  /**
   * Crée un mini-défi : une question ciblée + une notification in-app,
   * et un push si l'utilisateur a consenti et s'est abonné.
   */
  async createChallenge(userId: string, opts: { allowNotDue?: boolean } = {}): Promise<{ notificationId: string; questionId: string; pushed: boolean } | null> {
    const question = await this.learning.issueQuiz(userId, opts);
    if (!question) return null;
    const now = this.clock.now();
    const body = reminderMessage(hashSeed(question.id));
    const notif = await this.prisma.notification.create({
      data: { userId, title: 'Koto Quest', body, questionId: question.id, expiresAt: new Date(now.getTime() + NOTIFICATION_TTL_MS) },
    });
    const prefs = await this.prisma.notificationPreferences.findUnique({ where: { userId } });
    let pushed = false;
    if (prefs?.consent) {
      const subs = await this.prisma.pushSubscription.findMany({ where: { userId } });
      const lang = asLocale((await this.prisma.userPreferences.findUnique({ where: { userId }, select: { uiLanguage: true } }))?.uiLanguage);
      for (const sub of subs) {
        const r = await this.push.send(sub, { title: notif.title, body: serverText(body, lang), url: `/quiz/${question.id}?n=${notif.id}`, notificationId: notif.id });
        if (r === 'ok') pushed = true;
        else if (r === 'gone') await this.prisma.pushSubscription.delete({ where: { id: sub.id } }).catch(() => undefined);
        else if (r === 'error') {
          const s = await this.prisma.pushSubscription.update({ where: { id: sub.id }, data: { failedCount: { increment: 1 } } });
          if (s.failedCount > 5) await this.prisma.pushSubscription.delete({ where: { id: sub.id } });
        }
      }
      if (pushed) await this.prisma.notification.update({ where: { id: notif.id }, data: { pushed: true, status: 'sent' } });
    }
    return { notificationId: notif.id, questionId: question.id, pushed };
  }

  @Cron(CronExpression.EVERY_MINUTE)
  async tick() {
    if (!config.schedulerEnabled || this.running) return;
    this.running = true;
    try {
      await this.runScheduler();
    } catch (e) {
      this.logger.error('Échec du planificateur de rappels', e as Error);
    } finally {
      this.running = false;
    }
  }

  /** Une passe du planificateur. Exposée pour les tests. */
  async runScheduler(): Promise<{ sent: number; checked: number }> {
    const now = this.clock.now();
    const candidates = await this.prisma.notificationPreferences.findMany({
      where: { consent: true, enabled: true },
      include: { user: { select: { preferences: { select: { timezone: true } } } } },
    });
    let sent = 0;
    for (const p of candidates) {
      const userId = p.userId;
      const [relevantItems, lastAnswer] = await Promise.all([
        this.prisma.reviewCard.count({ where: { userId, due: { lte: now }, state: { not: 'new' } } }),
        this.prisma.exerciseAnswer.findFirst({ where: { userId }, orderBy: { createdAt: 'desc' }, select: { createdAt: true } }),
      ]);
      const decision = decideReminder({
        now,
        prefs: this.toEnginePrefs(p, p.user.preferences?.timezone ?? 'Europe/Paris'),
        relevantItems,
        lastSlotKey: p.lastSlotKey,
        lastActivityAt: lastAnswer?.createdAt ?? null,
      });
      if (decision.slotKey && decision.slotKey !== p.lastSlotKey) {
        await this.prisma.notificationPreferences.update({ where: { userId }, data: { lastSlotKey: decision.slotKey } });
      }
      if (decision.send && (await this.createChallenge(userId))) sent++;
    }
    return { sent, checked: candidates.length };
  }
}
