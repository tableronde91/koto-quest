import { Browser, expect, test } from '@playwright/test';

async function player(browser: Browser, name: string, baseURL: string) {
  const ctx = await browser.newContext({ baseURL, locale: 'fr-FR', timezoneId: 'Europe/Paris' });
  const page = await ctx.newPage();
  await page.goto('/');
  await page.getByLabel('Pseudo').fill(name);
  await page.getByLabel('Adresse e-mail').fill(`friend_${name}_${Date.now()}_${Math.floor(Math.random() * 1e6)}@test.local`);
  await page.getByLabel('Mot de passe').fill('motdepasse-e2e');
  await page.getByRole('button', { name: 'Créer mon compte' }).click();
  await page.getByRole('radio', { name: /Je pars de zéro/ }).click();
  for (let i = 0; i < 5; i++) await page.getByRole('button', { name: 'Suivant' }).click();
  await page.getByRole('button', { name: 'Commencer l’aventure' }).click();
  await expect(page.getByRole('link', { name: /Duels/ }).first()).toBeVisible();
  return page;
}

test('amis : ajout par code, alerte et acceptation, présence en ligne, défi en un clic', async ({ browser, baseURL }, info) => {
  test.skip(info.project.name !== 'desktop', 'un seul passage suffit');
  test.setTimeout(120_000);
  const a = await player(browser, 'Ren', baseURL!);
  const b = await player(browser, 'Yui', baseURL!);

  await b.goto('/profile');
  const code = (await b.getByTestId('my-code').textContent())!.trim();
  await b.goto('/');

  // Ren ajoute Yui avec son code, depuis son profil
  await a.goto('/profile');
  await a.getByLabel('Code ou nom du joueur').fill(code);
  await a.getByRole('button', { name: 'Ajouter en ami' }).click();
  await expect(a.getByText('Demande envoyée à Yui.')).toBeVisible();
  await expect(a.getByText('Demandes d’ami envoyées')).toBeVisible();

  // Yui reçoit l'alerte n'importe où dans l'application et accepte
  const toast = b.getByTestId('friend-toast');
  await b.reload();
  await expect(toast).toContainText('Ren veut devenir ton ami.', { timeout: 35_000 });
  await toast.getByRole('button', { name: 'Accepter' }).click();
  await expect(toast).toBeHidden();

  // Ren voit Yui en ligne dans son profil, puis la défie en un clic depuis le dojo
  await a.reload();
  await expect(a.getByTestId('friend').filter({ hasText: 'Yui' })).toContainText('En ligne', { timeout: 20_000 });
  await a.goto('/duel');
  const friend = a.getByTestId('friend-quick').filter({ hasText: 'Yui' });
  await expect(friend).toContainText('En ligne', { timeout: 20_000 });
  await friend.getByRole('button', { name: 'Défier Yui' }).click();
  await expect(a.getByRole('heading', { name: /Défi envoyé à Yui/ })).toBeVisible();
  await expect(b.getByText(/Ren.*te défie en duel/)).toBeVisible({ timeout: 15_000 });

  // Côté Yui, Ren apparaît dans la liste d'amis ; retrait avec confirmation
  await b.goto('/profile');
  const ren = b.getByTestId('friend').filter({ hasText: 'Ren' });
  await expect(ren).toBeVisible();
  await ren.getByRole('button', { name: 'Retirer Ren de mes amis' }).click();
  await ren.getByRole('button', { name: 'Retirer ?' }).click();
  await expect(b.getByTestId('friend')).toHaveCount(0);
});
