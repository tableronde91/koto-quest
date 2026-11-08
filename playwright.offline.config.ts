import { defineConfig } from '@playwright/test';

/** Tests de la version hors ligne : aucun serveur à démarrer. Lancer après `npm run build:offline`. */
export default defineConfig({
  testDir: 'e2e',
  testMatch: 'offline.spec.ts',
  timeout: 120_000,
  reporter: [['list']],
  use: { channel: process.env.PW_CHANNEL || undefined, locale: 'fr-FR', timezoneId: 'Europe/Paris' },
});
