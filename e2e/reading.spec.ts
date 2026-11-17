import { Page, expect, test } from '@playwright/test';

async function registerAndOnboard(page: Page) {
  const email = `e2e_read_${Date.now()}_${Math.floor(Math.random() * 1e6)}@test.local`;
  await page.goto('/');
  await page.getByLabel('Pseudo').fill('Yomi');
  await page.getByLabel('Adresse e-mail').fill(email);
  await page.getByLabel('Mot de passe').fill('motdepasse-e2e');
  await page.getByRole('button', { name: 'Créer mon compte' }).click();
  await expect(page.getByRole('heading', { name: 'Où en es-tu en japonais ?' })).toBeVisible();
  await page.getByRole('radio', { name: /Je pars de zéro/ }).click();
  for (let i = 0; i < 5; i++) await page.getByRole('button', { name: 'Suivant' }).click();
  await page.getByRole('button', { name: 'Commencer l’aventure' }).click();
}

test('lecture : chapitre du jour, furigana, traduction au toucher, compréhension, suite ouverte tout de suite', async ({ page }) => {
  await registerAndOnboard(page);
  // Carte de lecture sur l'accueil
  await page.getByTestId('reading-today').click();
  await expect(page.getByTestId('reader')).toBeVisible();
  await expect(page.getByRole('heading', { level: 1 })).toContainText('大');

  // Furigana affichés par défaut, masquables
  const first = page.getByTestId('sentence').first();
  await expect(first.locator('rt').first()).toBeVisible();
  await page.getByRole('button', { name: /ふりがな/ }).click();
  await expect(first.locator('rt')).toHaveCount(0);

  // Traduction au toucher
  await expect(page.getByTestId('translation')).toHaveCount(0);
  await first.getByRole('button').first().click();
  await expect(first.getByTestId('translation')).toContainText('Il était une fois');
  await page.getByRole('radio', { name: 'tout', exact: true }).click();
  expect(await page.getByTestId('translation').count()).toBe(await page.getByTestId('sentence').count());

  // Compréhension
  const validate = page.getByRole('button', { name: 'Valider mes réponses' });
  await expect(validate).toBeDisabled();
  await page.getByRole('radio', { name: 'À la rivière' }).check();
  await page.getByRole('radio', { name: 'Une grosse pêche' }).check();
  await validate.click();
  await expect(page.getByText('2/2 bonnes réponses')).toBeVisible();
  await expect(page.getByText(/\+25 XP · \+10 pièces/)).toBeVisible();
  await expect(page.getByRole('link', { name: 'Chapitre suivant' }).first()).toBeVisible();

  // Bibliothèque : chapitre 1 lu, chapitre 2 conseillé, et tous les contes ouverts sans attendre
  await page.getByRole('link', { name: 'Tous les contes' }).first().click();
  await expect(page.getByText('Lu aujourd’hui')).toBeVisible();
  await expect(page.getByText(/Envie de continuer \? La suite, « Un garçon dans la pêche », t’attend/)).toBeVisible();
  await expect(page.getByRole('button', { name: 'Relire' })).toBeVisible();
  await expect(page.getByRole('link', { name: /Chapitre 2 : Un garçon dans la pêche \(conseillé\)/ })).toBeVisible();
  const chapters = page.getByTestId('story').getByRole('listitem');
  expect(await chapters.count()).toBeGreaterThanOrEqual(28);
  expect(await page.getByTestId('story').getByRole('listitem').getByRole('link').count()).toBe(await chapters.count());

  // On ouvre directement le dernier chapitre du dernier conte
  await page.getByTestId('story').last().getByRole('link').last().click();
  await expect(page.getByTestId('reader')).toBeVisible();
  await expect(page.getByRole('button', { name: 'Valider mes réponses' })).toBeVisible();

  // « Continuer la lecture » mène au chapitre conseillé
  await page.goBack();
  await page.getByRole('button', { name: 'Continuer la lecture' }).click();
  await expect(page.getByRole('heading', { level: 1 })).toContainText('もも');
});
