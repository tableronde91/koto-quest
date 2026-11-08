import { defineConfig, devices } from '@playwright/test';
import base from './playwright.config';

/**
 * Mêmes parcours que playwright.config.ts, mais contre la version de production
 * (site compilé servi par l'API sur un seul port) : PROD_URL=http://localhost:3000 par défaut.
 */
export default defineConfig({
  ...base,
  use: { ...base.use, baseURL: process.env.PROD_URL ?? 'http://localhost:3000' },
  projects: [{ name: 'desktop', use: { ...devices['Desktop Chrome'] } }],
  webServer: undefined,
});
