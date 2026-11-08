import { Injectable, Logger } from '@nestjs/common';
import { createTransport, type Transporter } from 'nodemailer';
import { config } from '../config';

/**
 * Envoi d'e-mails (réinitialisation du mot de passe).
 * Avec SMTP_URL, les messages partent réellement ; sinon, ils sont écrits dans les logs du serveur.
 */
@Injectable()
export class MailService {
  private readonly logger = new Logger('Mail');
  private readonly transport: Transporter | null = config.smtpUrl ? createTransport(config.smtpUrl) : null;
  readonly outbox: { to: string; subject: string; body: string }[] = [];

  async send(to: string, subject: string, body: string) {
    this.outbox.push({ to, subject, body });
    if (this.outbox.length > 50) this.outbox.shift();
    if (!this.transport) {
      this.logger.log(`✉️  À ${to} — ${subject}\n${body}`);
      return;
    }
    try {
      await this.transport.sendMail({ from: config.mailFrom, to, subject, text: body });
      this.logger.log(`✉️  E-mail envoyé à ${to} — ${subject}`);
    } catch (e) {
      // Un échec d'envoi ne doit ni bloquer la requête ni révéler si le compte existe.
      this.logger.error(`Échec d'envoi de l'e-mail à ${to} : ${(e as Error).message}`);
    }
  }
}
