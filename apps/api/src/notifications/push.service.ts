import { Injectable, Logger } from '@nestjs/common';
import * as webpush from 'web-push';
import { config } from '../config';

export interface PushPayload {
  title: string;
  body: string;
  url: string;
  notificationId: string;
}
export type PushResult = 'ok' | 'gone' | 'error' | 'disabled';

/** Envoi Web Push (VAPID). Remplaçable dans les tests. */
@Injectable()
export class PushService {
  private readonly logger = new Logger('Push');
  readonly enabled = !!(config.vapid.publicKey && config.vapid.privateKey);

  constructor() {
    if (this.enabled) webpush.setVapidDetails(config.vapid.subject, config.vapid.publicKey, config.vapid.privateKey);
    else this.logger.warn('Clés VAPID absentes : les notifications push sont désactivées (popups in-app uniquement).');
  }

  async send(sub: { endpoint: string; p256dh: string; auth: string }, payload: PushPayload): Promise<PushResult> {
    if (!this.enabled) return 'disabled';
    try {
      await webpush.sendNotification({ endpoint: sub.endpoint, keys: { p256dh: sub.p256dh, auth: sub.auth } }, JSON.stringify(payload), { TTL: 6 * 3600 });
      return 'ok';
    } catch (e) {
      const status = (e as { statusCode?: number }).statusCode;
      if (status === 404 || status === 410) return 'gone';
      this.logger.warn(`Échec d'envoi push (${status ?? 'réseau'})`);
      return 'error';
    }
  }
}
