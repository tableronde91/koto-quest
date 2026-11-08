import { Body, Controller, HttpCode, Post, Req, Res, Headers } from '@nestjs/common';
import { ApiTags } from '@nestjs/swagger';
import { Throttle } from '@nestjs/throttler';
import type { Request, Response } from 'express';
import { CurrentUser, Public, AuthUser } from '../common/decorators';
import { SESSION_COOKIE, config } from '../config';
import { AuthService } from './auth.service';
import { ForgotPasswordDto, LoginDto, RegisterDto, ResetPasswordDto } from './dto';
import { asLocale } from '../common/i18n';

const authLimit = { default: { limit: config.authRateLimit, ttl: 60_000 } };

@ApiTags('auth')
@Controller('auth')
export class AuthController {
  constructor(private auth: AuthService) {}

  /**
   * Ouvre une session. Navigateur : cookie httpOnly (le jeton n'est jamais lisible par le JavaScript).
   * Application mobile (en-tête X-Koto-Client: mobile) : le jeton est renvoyé dans la réponse pour être
   * rangé dans le coffre sécurisé du téléphone, puis envoyé en « Authorization: Bearer ».
   */
  private async startSession(res: Response, req: Request, userId: string): Promise<{ token?: string; expiresAt?: string }> {
    const { token, expiresAt } = await this.auth.createSession(userId, req.headers['user-agent']);
    if (req.headers['x-koto-client'] === 'mobile') return { token, expiresAt: expiresAt.toISOString() };
    res.cookie(SESSION_COOKIE, token, {
      httpOnly: true,
      sameSite: 'lax',
      secure: config.cookieSecure,
      expires: expiresAt,
      path: '/',
    });
    return {};
  }

  @Public() @Throttle(authLimit) @Post('register')
  async register(@Body() dto: RegisterDto, @Req() req: Request, @Res({ passthrough: true }) res: Response) {
    const tz = typeof req.headers['x-timezone'] === 'string' ? req.headers['x-timezone'] : undefined;
    const valid = tz && (() => { try { new Intl.DateTimeFormat('en', { timeZone: tz }); return true; } catch { return false; } })();
    const user = await this.auth.register(dto.email, dto.password, dto.displayName, valid ? tz : undefined);
    return { id: user.id, ...(await this.startSession(res, req, user.id)) };
  }

  @Public() @Throttle(authLimit) @Post('login') @HttpCode(200)
  async login(@Body() dto: LoginDto, @Req() req: Request, @Res({ passthrough: true }) res: Response) {
    const user = await this.auth.login(dto.email, dto.password);
    return { id: user.id, ...(await this.startSession(res, req, user.id)) };
  }

  @Post('logout') @HttpCode(204)
  async logout(@CurrentUser() user: AuthUser, @Res({ passthrough: true }) res: Response) {
    await this.auth.logout(user.sessionId);
    res.clearCookie(SESSION_COOKIE, { path: '/' });
  }

  @Public() @Throttle(authLimit) @Post('forgot-password') @HttpCode(200)
  async forgot(@Body() dto: ForgotPasswordDto, @Headers('accept-language') lang?: string) {
    await this.auth.forgotPassword(dto.email, asLocale(lang));
    return { message: 'Si un compte existe pour cette adresse, un e-mail vient d’être envoyé.' };
  }

  @Public() @Throttle(authLimit) @Post('reset-password') @HttpCode(200)
  async reset(@Body() dto: ResetPasswordDto) {
    await this.auth.resetPassword(dto.token, dto.password);
    return { message: 'Mot de passe modifié. Vous pouvez vous connecter.' };
  }
}
