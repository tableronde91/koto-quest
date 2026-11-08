import { BadRequestException, ForbiddenException, Injectable } from '@nestjs/common';
import { isValidTimeZone } from '@koto/learning-engine';
import type { MeDto } from '@koto/shared';
import { PrismaService } from '../common/prisma.service';
import { ClockService } from '../common/clock.service';
import { AuthService } from '../auth/auth.service';
import { AvatarConfig, normalizeAvatar } from '@koto/learning-engine';
import { OnboardingDto, PreferencesDto } from './dto';

@Injectable()
export class MeService {
  constructor(private prisma: PrismaService, private clock: ClockService, private auth: AuthService) {}

  async me(userId: string): Promise<MeDto> {
    const u = await this.prisma.user.findUniqueOrThrow({ where: { id: userId }, include: { preferences: true } });
    const p = u.preferences ?? (await this.prisma.userPreferences.create({ data: { userId } }));
    return {
      id: u.id,
      email: u.email,
      displayName: u.displayName,
      onboarded: !!u.onboardedAt,
      xp: u.xp,
      coins: u.coins,
      avatar: normalizeAvatar(u.avatar as Partial<AvatarConfig> | null),
      preferences: {
        selfLevel: p.selfLevel as MeDto['preferences']['selfLevel'],
        targetLevel: p.targetLevel as MeDto['preferences']['targetLevel'],
        examDate: p.examDate?.toISOString().slice(0, 10) ?? null,
        minutesPerDay: p.minutesPerDay,
        difficultAreas: p.difficultAreas as MeDto['preferences']['difficultAreas'],
        timezone: p.timezone,
        showFurigana: p.showFurigana,
        theme: p.theme as MeDto['preferences']['theme'],
        reducedMotion: p.reducedMotion,
        locale: p.uiLanguage === 'en' ? 'en' : 'fr',
      },
    };
  }

  private checkTz(tz?: string) {
    if (tz && !isValidTimeZone(tz)) throw new BadRequestException('Fuseau horaire inconnu.');
  }

  async onboarding(userId: string, dto: OnboardingDto) {
    this.checkTz(dto.timezone);
    const data = {
      selfLevel: dto.selfLevel,
      targetLevel: dto.targetLevel,
      examDate: dto.examDate ? new Date(dto.examDate) : null,
      minutesPerDay: dto.minutesPerDay,
      difficultAreas: dto.difficultAreas,
      ...(dto.timezone ? { timezone: dto.timezone } : {}),
      ...(dto.locale ? { uiLanguage: dto.locale } : {}),
    };
    await this.prisma.userPreferences.upsert({ where: { userId }, create: { userId, ...data }, update: data });
    // Le choix du rythme est enregistré ; l'envoi ne démarrera qu'après consentement explicite.
    const mode = dto.reminderMode === 'off' ? 'normal' : dto.reminderMode;
    await this.prisma.notificationPreferences.upsert({
      where: { userId },
      create: { userId, mode, enabled: false },
      update: { mode },
    });
    await this.prisma.user.update({ where: { id: userId }, data: { onboardedAt: this.clock.now() } });
    return this.me(userId);
  }

  async updatePreferences(userId: string, dto: PreferencesDto) {
    this.checkTz(dto.timezone);
    const { displayName, examDate, locale, ...rest } = dto;
    await this.prisma.userPreferences.update({
      where: { userId },
      data: { ...rest, ...(locale ? { uiLanguage: locale } : {}), ...(examDate !== undefined ? { examDate: examDate ? new Date(examDate) : null } : {}) },
    });
    if (displayName) await this.prisma.user.update({ where: { id: userId }, data: { displayName: displayName.trim() } });
    return this.me(userId);
  }

  /** Export RGPD : toutes les données personnelles, au format JSON lisible. */
  async export(userId: string) {
    const user = await this.prisma.user.findUniqueOrThrow({
      where: { id: userId },
      include: {
        preferences: true,
        notificationPrefs: true,
        lessonProgress: { include: { lesson: { select: { slug: true, title: true } } } },
        reviewCards: { include: { item: { select: { slug: true, front: true, meaning: true } } } },
        reviewHistory: true,
        learningSessions: true,
        answers: true,
        notifications: true,
        dailyActivity: true,
        xpEvents: true,
        inventory: true,
        bossResults: true,
        pushSubscriptions: { select: { id: true, createdAt: true } },
        sessions: { select: { id: true, createdAt: true, expiresAt: true, userAgent: true } },
      },
    });
    const { passwordHash: _omit, ...safe } = user;
    return { exportedAt: this.clock.now().toISOString(), format: 'koto-quest-export/1', data: safe };
  }

  /** Suppression définitive du compte et de toutes ses données (cascade). */
  async deleteAccount(userId: string, password: string) {
    if (!(await this.auth.verifyPassword(userId, password))) throw new ForbiddenException('Mot de passe incorrect.');
    await this.prisma.user.delete({ where: { id: userId } });
  }
}
