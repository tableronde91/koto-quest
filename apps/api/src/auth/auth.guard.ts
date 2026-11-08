import { CanActivate, ExecutionContext, Injectable, UnauthorizedException } from '@nestjs/common';
import { Reflector } from '@nestjs/core';
import { IS_PUBLIC } from '../common/decorators';
import { SESSION_COOKIE } from '../config';
import { AuthService } from './auth.service';

/** Garde globale : toute route est protégée sauf si elle est marquée @Public(). */
@Injectable()
export class AuthGuard implements CanActivate {
  constructor(private readonly reflector: Reflector, private readonly auth: AuthService) {}

  async canActivate(ctx: ExecutionContext): Promise<boolean> {
    const req = ctx.switchToHttp().getRequest();
    const isPublic = this.reflector.getAllAndOverride<boolean>(IS_PUBLIC, [ctx.getHandler(), ctx.getClass()]);
    // Cookie (navigateur) ou jeton « Bearer » (application mobile).
    const header: string | undefined = req.headers?.authorization;
    const bearer = header?.startsWith('Bearer ') ? header.slice(7).trim() : undefined;
    const token: string | undefined = req.cookies?.[SESSION_COOKIE] ?? bearer;
    const user = token ? await this.auth.validateSession(token) : null;
    if (user) req.user = user;
    if (isPublic) return true;
    if (!user) throw new UnauthorizedException('Session expirée ou absente. Merci de vous reconnecter.');
    return true;
  }
}
