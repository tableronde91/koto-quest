import 'dotenv/config';

function bool(v: string | undefined, d: boolean) {
  return v === undefined || v === '' ? d : ['1', 'true', 'yes'].includes(v.toLowerCase());
}

/** Configuration lue depuis l'environnement (aucun secret en dur dans le code). */
export const config = {
  port: Number(process.env.PORT ?? 3000),
  databaseUrl: process.env.DATABASE_URL ?? '',
  webOrigin: process.env.WEB_ORIGIN ?? 'http://localhost:5173',
  cookieSecure: bool(process.env.COOKIE_SECURE, false),
  sessionTtlDays: Number(process.env.SESSION_TTL_DAYS ?? 30),
  schedulerEnabled: bool(process.env.SCHEDULER_ENABLED, true),
  vapid: {
    publicKey: process.env.VAPID_PUBLIC_KEY ?? '',
    privateKey: process.env.VAPID_PRIVATE_KEY ?? '',
    subject: process.env.VAPID_SUBJECT ?? 'mailto:contact@koto-quest.local',
  },
  /**
   * Derrière un proxy inverse (Caddy, Nginx, hébergeur…) : nombre de proxys de confiance,
   * pour que la limitation de débit voie l'IP réelle des joueurs et non celle du proxy.
   */
  trustProxy: process.env.TRUST_PROXY ?? '',
  /** Dossier du site web compilé (apps/web/dist) : l'API le sert elle-même en production. */
  webDist: process.env.WEB_DIST ?? '',
  /** Envoi réel des e-mails (ex. smtps://utilisateur:motdepasse@smtp.exemple.fr:465). Vide = e-mails écrits dans les logs. */
  smtpUrl: process.env.SMTP_URL ?? '',
  mailFrom: process.env.MAIL_FROM ?? 'Koto Quest <no-reply@koto-quest.local>',
  /** Plafond de limitation de débit des routes d'authentification (requêtes / minute / IP). */
  authRateLimit: Number(process.env.AUTH_RATE_LIMIT ?? 10),
};

export const SESSION_COOKIE = 'koto_session';
