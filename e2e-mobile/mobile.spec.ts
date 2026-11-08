import { Page, expect, test } from '@playwright/test';

async function answerUntil(page: Page, end: RegExp) {
  for (let guard = 0; guard < 80; guard++) {
    if (await page.getByRole('heading', { name: end }).isVisible().catch(() => false)) return;
    const q = page.getByTestId('question').last();
    if (!(await q.isVisible().catch(() => false))) {
      await page.waitForTimeout(250);
      continue;
    }
    const verify = q.getByRole('button', { name: 'Vérifier' });
    // Remise en ordre : on pose les morceaux dans l'ordre affiché ; association : on remplit ligne à ligne.
    // Repère d'étape : l'intitulé de la barre de progression (« Question n sur m ») et le titre de la séance.
    const stepOf = async () => `${await page.getByRole('progressbar').first().getAttribute('aria-label').catch(() => '')}|${await page.getByText('Mini-révision').count()}`;
    const before = await stepOf();
    const right = q.getByTestId('match-right');
    if ((await right.count()) > 0) {
      for (let k = 0; k < (await right.count()); k++) await right.nth(k).click();
      await verify.click();
    } else if (await verify.isVisible().catch(() => false)) {
      for (let k = 0; k < 12 && (await verify.isDisabled().catch(() => false)); k++) {
        const chips = q.getByRole('button').filter({ hasNotText: /Vérifier|Continuer|Terminer|Écouter/ });
        await chips.nth(Math.min(k, (await chips.count()) - 1)).click();
      }
      await verify.click();
    } else {
      await q.getByRole('button').filter({ hasNotText: /Écouter|🔊/ }).first().click();
    }
    const next = page.getByRole('button', { name: /^(Continuer|Terminer)$/ });
    await expect(next).toBeVisible();
    await next.click();
    await expect.poll(async () => (await page.getByRole('heading', { name: end }).isVisible().catch(() => false)) || (await stepOf()) !== before).toBe(true);
  }
  throw new Error('séance non terminée');
}

test('appli mobile : inscription, profil, leçon complète, révisions, rappels, déconnexion', async ({ page }) => {
  const email = `mobile${Date.now()}@test.local`;
  await page.goto('/');
  await expect(page.getByRole('heading', { name: 'Koto Quest' })).toBeVisible();
  await page.getByRole('tab', { name: 'Créer un compte' }).click();
  await page.getByLabel('Pseudo').fill('Mobile');
  await page.getByLabel('Adresse e-mail').fill(email);
  await page.getByLabel('Mot de passe').fill('motdepasse123');
  await page.getByRole('button', { name: 'Créer mon compte' }).click();

  await expect(page.getByRole('heading', { name: 'Bienvenue dans l’archipel !' })).toBeVisible();
  await page.getByRole('button', { name: 'Commencer l’aventure' }).click();

  await expect(page.getByRole('heading', { name: 'Prêt·e pour la suite ?' })).toBeVisible();
  // Le jeton est dans le stockage de l'appli, jamais dans un cookie
  expect((await page.context().cookies()).filter((c) => c.name.includes('koto'))).toHaveLength(0);

  await page.getByRole('button', { name: 'Commencer la leçon' }).click();
  await expect(page.getByRole('heading', { name: 'Les voyelles あいうえお' })).toBeVisible();
  await page.getByRole('button', { name: 'Passer aux exercices' }).click();
  await answerUntil(page, /Sans faute|Leçon terminée/);
  await expect(page.getByText(/\+\d+ XP/).filter({ visible: true }).first()).toBeVisible();
  await page.getByRole('button', { name: 'Retour à l’accueil' }).click();

  // Parcours : la leçon est terminée, la suivante est ouverte
  await page.getByRole('tab', { name: /Parcours/ }).click();
  await expect(page.getByRole('button', { name: 'Les voyelles あいうえお, terminée' })).toBeVisible();
  await page.getByRole('tab', { name: /N4/ }).click();
  await expect(page.getByRole('heading', { name: /N4 : Archipel des voyageurs/ })).toBeVisible();

  // Révisions et réglages
  await page.getByRole('tab', { name: /Révisions/ }).click();
  await expect(page.getByRole('heading', { name: 'Révisions' })).toBeVisible();
  await page.getByRole('tab', { name: /Réglages/ }).click();
  await page.getByRole('switch', { name: 'Recevoir les rappels' }).click();
  await expect(page.getByText(/Rappels enregistrés/).filter({ visible: true })).toBeVisible();
  await expect(page.getByText(/Créneaux du jour/).filter({ visible: true })).toBeVisible();

  // Session conservée au rechargement, puis déconnexion
  await page.reload();
  await expect(page.getByRole('heading', { name: 'Réglages' })).toBeVisible();
  await page.getByRole('button', { name: 'Se déconnecter' }).click();
  await expect(page.getByRole('heading', { name: 'Koto Quest' })).toBeVisible();
});
