import { defineConfig, devices } from '@playwright/test';

/**
 * Tests de bout en bout des parcours essentiels.
 * Prérequis : base PostgreSQL migrée et seedée (npm run setup).
 * Lancement : npm run test:e2e  (PW_CHANNEL=chrome pour utiliser le Chrome installé)
 */
export default defineConfig({
  testDir: 'e2e',
  testIgnore: 'offline.spec.ts',
  timeout: 120_000,
  fullyParallel: false,
  workers: 1,
  reporter: [['list']],
  use: {
    baseURL: 'http://localhost:5173',
    channel: process.env.PW_CHANNEL || undefined,
    locale: 'fr-FR',
    timezoneId: 'Europe/Paris',
    trace: 'retain-on-failure',
  },
  projects: [
    { name: 'desktop', use: { ...devices['Desktop Chrome'], channel: process.env.PW_CHANNEL || undefined } },
    { name: 'mobile', use: { ...devices['Pixel 7'], channel: process.env.PW_CHANNEL || undefined } },
  ],
  webServer: [
    { command: 'npm run build -w @koto/api && npm run start -w @koto/api', url: 'http://localhost:3000/api/health', reuseExistingServer: true, timeout: 120_000 },
    { command: 'npm run dev -w @koto/web', url: 'http://localhost:5173', reuseExistingServer: true, timeout: 60_000 },
  ],
});
