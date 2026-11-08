import { ConflictException, Injectable, UnauthorizedException, BadRequestException } from '@nestjs/common';
import * as bcrypt from 'bcryptjs';
import { PrismaService } from '../common/prisma.service';
import { ClockService } from '../common/clock.service';
import { hashToken, newToken } from '../common/crypto';
import { AuthUser } from '../common/decorators';
import { config } from '../config';
import { MailService } from './mail.service';
import { serverT, serverText } from '../common/i18n';
import type { Locale } from '@koto/shared';

const BCRYPT_ROUNDS = process.env.NODE_ENV === 'test' ? 4 : 12;
// Hash factice pour que la durée de réponse ne révèle pas si un compte existe.
const DUMMY_HASH = bcrypt.hashSync('dummy-password-koto', 4);

@Injectable()
export class AuthService {
  constructor(private prisma: PrismaService, private clock: ClockService, private mail: MailService) {}

  async register(email: string, password: string, displayName: string, timezone?: string) {
    const existing = await this.prisma.user.findUnique({ where: { email } });
    if (existing) throw new ConflictException('Un compte existe déjà avec cette adresse e-mail.');
    const passwordHash = await bcrypt.hash(password, BCRYPT_ROUNDS);
    return this.prisma.user.create({
      data: {
        email,
        passwordHash,
        displayName: displayName.trim(),
        preferences: { create: timezone ? { timezone } : {} },
        notificationPrefs: { create: {} },
      },
    });
  }

  async login(email: string, password: string) {
    const user = await this.prisma.user.findUnique({ where: { email } });
    const ok = await bcrypt.compare(password, user?.passwordHash ?? DUMMY_HASH);
    if (!user || !ok) throw new UnauthorizedException('E-mail ou mot de passe incorrect.');
    return user;
  }

  async verifyPassword(userId: string, password: string) {
    const user = await this.prisma.user.findUniqueOrThrow({ where: { id: userId } });
    return bcrypt.compare(password, user.passwordHash);
  }

  async createSession(userId: string, userAgent?: string) {
    const token = newToken();
    const expiresAt = new Date(this.clock.now().getTime() + config.sessionTtlDays * 86_400_000);
    await this.prisma.session.create({ data: { userId, tokenHash: hashToken(token), expiresAt, userAgent: userAgent?.slice(0, 200) } });
    return { token, expiresAt };
  }

  async validateSession(token: string): Promise<AuthUser | null> {
    const session = await this.prisma.session.findUnique({ where: { tokenHash: hashToken(token) }, include: { user: true } });
    if (!session || session.expiresAt <= this.clock.now()) return null;
    return { id: session.user.id, email: session.user.email, sessionId: session.id };
  }

  async logout(sessionId: string) {
    await this.prisma.session.deleteMany({ where: { id: sessionId } });
  }

  /** Répond toujours de la même façon pour ne pas révéler l'existence d'un compte. */
  async forgotPassword(email: string, locale: Locale = 'fr') {
    const user = await this.prisma.user.findUnique({ where: { email } });
    if (!user) return;
    const token = newToken();
    await this.prisma.passwordResetToken.create({
      data: { userId: user.id, tokenHash: hashToken(token), expiresAt: new Date(this.clock.now().getTime() + 3600_000) },
    });
    await this.mail.send(
      email,
      serverText('Koto Quest — réinitialisation du mot de passe', locale),
      serverT('Pour choisir un nouveau mot de passe (lien valable 1 heure) :\n{0}/reset-password?token={1}', [config.webOrigin.split(',')[0].trim(), token], locale),
    );
  }

  async resetPassword(token: string, password: string) {
    const row = await this.prisma.passwordResetToken.findUnique({ where: { tokenHash: hashToken(token) } });
    if (!row || row.usedAt || row.expiresAt <= this.clock.now()) throw new BadRequestException('Lien invalide ou expiré.');
    const passwordHash = await bcrypt.hash(password, BCRYPT_ROUNDS);
    await this.prisma.$transaction([
      this.prisma.user.update({ where: { id: row.userId }, data: { passwordHash } }),
      this.prisma.passwordResetToken.update({ where: { id: row.id }, data: { usedAt: this.clock.now() } }),
      // Toutes les sessions existantes sont révoquées.
      this.prisma.session.deleteMany({ where: { userId: row.userId } }),
    ]);
  }
}
