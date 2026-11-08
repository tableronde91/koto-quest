import { Injectable } from '@nestjs/common';
import { ThrottlerGuard } from '@nestjs/throttler';

/**
 * Limitation de débit.
 * - Inscription, connexion et mot de passe : comptées par adresse e-mail visée, en plus de l'IP.
 *   Le forçage d'un compte reste bloqué même si l'IP vue par le serveur est imprécise ou falsifiée
 *   (plusieurs relais devant l'application chez certains hébergeurs).
 * - Le reste : par IP.
 */
@Injectable()
export class KotoThrottlerGuard extends ThrottlerGuard {
  protected async getTracker(req: Record<string, any>): Promise<string> {
    const email = typeof req.body?.email === 'string' ? req.body.email.trim().toLowerCase() : '';
    const path: string = req.originalUrl ?? req.url ?? '';
    if (email && req.method === 'POST' && /\/api\/auth\//.test(path)) return `email:${email}`;
    return req.ip ?? req.socket?.remoteAddress ?? 'unknown';
  }
}
