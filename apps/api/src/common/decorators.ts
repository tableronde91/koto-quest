import { ExecutionContext, SetMetadata, createParamDecorator } from '@nestjs/common';

export const IS_PUBLIC = 'isPublic';
/** Route accessible sans session. */
export const Public = () => SetMetadata(IS_PUBLIC, true);

export interface AuthUser {
  id: string;
  email: string;
  sessionId: string;
}

/** Utilisateur authentifié (injecté par AuthGuard). */
export const CurrentUser = createParamDecorator((_: unknown, ctx: ExecutionContext): AuthUser => {
  return ctx.switchToHttp().getRequest().user;
});
