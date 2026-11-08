import { Browser, Page, expect, test } from '@playwright/test';

/** Duel en ligne entre deux vrais comptes (deux navigateurs isolés). */
async function player(browser: Browser, name: string, baseURL: string) {
  const ctx = await browser.newContext({ baseURL, locale: 'fr-FR', timezoneId: 'Europe/Paris' });
  const page = await ctx.newPage();
  await page.goto('/');
  await page.getByLabel('Pseudo').fill(name);
  await page.getByLabel('Adresse e-mail').fill(`duel_${name}_${Date.now()}_${Math.floor(Math.random() * 1e6)}@test.local`);
  await page.getByLabel('Mot de passe').fill('motdepasse-e2e');
  await page.getByRole('button', { name: 'Créer mon compte' }).click();
  await page.getByRole('radio', { name: /Je pars de zéro/ }).click();
  for (let i = 0; i < 5; i++) await page.getByRole('button', { name: 'Suivant' }).click();
  await page.getByRole('button', { name: 'Commencer l’aventure' }).click();
  await expect(page.getByRole('link', { name: /Duels/ }).first()).toBeVisible();
  return page;
}

async function playRound(page: Page) {
  const q = page.getByRole('region', { name: /^Question \d+/ });
  if (!(await q.isVisible().catch(() => false))) return;
  const first = q.getByRole('button').first();
  if (await first.isEnabled().catch(() => false)) await first.click({ timeout: 2000 }).catch(() => undefined);
}

test('duel en ligne : défi par code, combat simultané, résultat et classement', async ({ browser, baseURL }, info) => {
  test.skip(info.project.name !== 'desktop', 'un seul passage suffit');
  test.setTimeout(240_000);
  const a = await player(browser, 'Kenji', baseURL!);
  const b = await player(browser, 'Mio', baseURL!);

  await a.goto('/duel');
  await expect(a.getByRole('heading', { name: 'Duels', level: 1 })).toBeVisible();
  await b.goto('/duel');
  const code = (await b.locator('code').first().textContent())!.trim();
  expect(code).toMatch(/^KQ-[A-Z0-9]{6}$/);

  // Kenji défie Mio avec son code
  await a.getByLabel('Code ou nom du joueur').fill(code);
  await a.getByRole('button', { name: 'Défier ce code' }).click();
  await expect(a.getByRole('heading', { name: /Défi envoyé à Mio/ })).toBeVisible();

  // Mio reçoit le défi et l'accepte
  await expect(b.getByText(/Kenji.*te défie en duel/)).toBeVisible({ timeout: 15_000 });
  await b.getByRole('button', { name: 'Accepter' }).first().click();
  await expect(b.getByRole('region', { name: 'Arène du duel' })).toBeVisible();
  await expect(a.getByRole('region', { name: 'Arène du duel' })).toBeVisible({ timeout: 10_000 });

  // Les deux répondent jusqu'à la fin du duel
  const end = /^(Victoire !|Défaite|Égalité)$/;
  for (let i = 0; i < 1200; i++) {
    const doneA = await a.getByRole('heading', { name: end }).isVisible().catch(() => false);
    const doneB = await b.getByRole('heading', { name: end }).isVisible().catch(() => false);
    if (doneA && doneB) break;
    await playRound(a);
    await playRound(b);
    await a.waitForTimeout(150);
  }
  const ra = (await a.getByRole('heading', { name: end }).textContent())!;
  const rb = (await b.getByRole('heading', { name: end }).textContent())!;
  const opposite: Record<string, string> = { 'Victoire !': 'Défaite', Défaite: 'Victoire !', Égalité: 'Égalité' };
  expect(rb).toBe(opposite[ra]);
  await expect(a.getByText('Duel amical : sans effet sur le classement.')).toBeVisible();

  // Retour au dojo : l'historique garde la trace du duel
  await a.getByRole('link', { name: 'Retour au dojo' }).click();
  await a.getByRole('tab', { name: 'Mes duels' }).click();
  await expect(a.getByText(/contre Mio/)).toBeVisible();
  await a.context().close();
  await b.context().close();
});
