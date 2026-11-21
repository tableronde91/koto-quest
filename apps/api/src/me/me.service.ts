import { BadRequestException, ForbiddenException, Injectable } from '@nestjs/common';
import { isValidTimeZone } from '@koto/learning-engine';
import { applyStudyChoice, languageOfLevel, type JlptCode, type MeDto, type StudyChoice, type StudyLanguage } from '@koto/shared';
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
        studyLanguage: languageOfLevel(p.targetLevel),
      },
    };
  }

  private checkTz(tz?: string) {
    if (tz && !isValidTimeZone(tz)) throw new BadRequestException('Fuseau horaire inconnu.');
  }

  /** Langue et niveau visé, en gardant en mémoire le dernier niveau de chaque langue. */
  private async studyChoice(userId: string, patch: { studyLanguage?: string; targetLevel?: string }) {
    const p = await this.prisma.userPreferences.findUnique({ where: { userId } });
    const current: StudyChoice = {
      studyLanguage: (p?.studyLanguage as StudyLanguage) ?? 'ja',
      targetLevel: (p?.targetLevel as JlptCode) ?? 'N5',
      levelByLanguage: (p?.levelByLanguage as StudyChoice['levelByLanguage']) ?? {},
    };
    return applyStudyChoice(current, { studyLanguage: patch.studyLanguage as StudyLanguage | undefined, targetLevel: patch.targetLevel as JlptCode | undefined });
  }

  async onboarding(userId: string, dto: OnboardingDto) {
    this.checkTz(dto.timezone);
    const choice = await this.studyChoice(userId, { studyLanguage: dto.studyLanguage, targetLevel: dto.targetLevel });
    const data = {
      selfLevel: dto.selfLevel,
      targetLevel: choice.targetLevel,
      studyLanguage: choice.studyLanguage,
      levelByLanguage: choice.levelByLanguage,
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
    const { displayName, examDate, locale, studyLanguage, targetLevel, ...rest } = dto;
    const study = studyLanguage || targetLevel ? await this.studyChoice(userId, { studyLanguage, targetLevel }) : null;
    await this.prisma.userPreferences.update({
      where: { userId },
      data: {
        ...rest,
        ...(study ? { studyLanguage: study.studyLanguage, targetLevel: study.targetLevel, levelByLanguage: study.levelByLanguage } : {}),
        ...(locale ? { uiLanguage: locale } : {}),
        ...(examDate !== undefined ? { examDate: examDate ? new Date(examDate) : null } : {}),
      },
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
        achievements: true,
        examAttempts: true,
        gameResults: true,
        readingLogs: { select: { chapter: true, dateKey: true, correct: true, total: true, seconds: true, createdAt: true } },
        duelProfile: true,
        friendsAsked: { select: { status: true, createdAt: true, acceptedAt: true } },
        friendsAsking: { select: { status: true, createdAt: true, acceptedAt: true } },
        duelsAsP1: { select: { id: true, kind: true, status: true, outcome: true, endReason: true, hp1: true, hp2: true, delta1: true, createdAt: true, endedAt: true, botName: true } },
        duelsAsP2: { select: { id: true, kind: true, status: true, outcome: true, endReason: true, hp1: true, hp2: true, delta2: true, createdAt: true, endedAt: true } },
        pushSubscriptions: { select: { id: true, createdAt: true } },
        sessions: { select: { id: true, createdAt: true, expiresAt: true, userAgent: true } },
      },
    });
    const { passwordHash: _omit, ...safe } = user;
    return { exportedAt: this.clock.now().toISOString(), format: 'koto-quest-export/2', data: safe };
  }

  /** Suppression définitive du compte et de toutes ses données (cascade). */
  async deleteAccount(userId: string, password: string) {
    if (!(await this.auth.verifyPassword(userId, password))) throw new ForbiddenException('Mot de passe incorrect.');
    await this.prisma.user.delete({ where: { id: userId } });
  }
}
