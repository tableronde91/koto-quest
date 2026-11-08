import { defineConfig, devices } from '@playwright/test';

/**
 * Application mobile, testée via son export web (React Native Web) dans un téléphone émulé,
 * contre la vraie API. Préalable : npm run export:web -w @koto/mobile (avec EXPO_PUBLIC_API_URL=http://localhost:3000).
 */
export default defineConfig({
  testDir: './e2e-mobile',
  timeout: 120_000,
  workers: 1,
  use: { ...devices['Pixel 7'], baseURL: 'http://localhost:8090', locale: 'fr-FR', timezoneId: 'Europe/Paris', channel: process.env.PW_CHANNEL || undefined },
  webServer: [
    { command: 'npm run build -w @koto/api && WEB_ORIGIN=http://localhost:5173,http://localhost:8090 npm run start -w @koto/api', url: 'http://localhost:3000/api/health', reuseExistingServer: true, timeout: 120_000 },
    { command: 'node e2e-mobile/serve.cjs', url: 'http://localhost:8090', reuseExistingServer: true },
  ],
});
