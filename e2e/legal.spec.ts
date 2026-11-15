import { expect, test } from '@playwright/test';

test('pied de page et pages légales accessibles sans compte, en français et en anglais', async ({ page }) => {
  await page.goto('/');
  await expect(page).toHaveURL(/\/welcome/);
  const footer = page.getByRole('contentinfo');
  await expect(footer).toContainText('AG SOFTWARE SOLUTION');
  // Aucune police chargée depuis Google
  const google: string[] = [];
  page.on('request', (r) => { if (/fonts\.(googleapis|gstatic)\.com/.test(r.url())) google.push(r.url()); });

  for (const [link, heading] of [
    ['Mentions légales', 'Mentions légales'],
    ['Confidentialité', 'Politique de confidentialité'],
    ['Cookies', 'Cookies et stockage local'],
    ['Conditions d’utilisation', 'Conditions d’utilisation'],
  ] as const) {
    await page.getByRole('contentinfo').getByRole('link', { name: link, exact: true }).click();
    await expect(page.getByRole('heading', { level: 1, name: heading })).toBeVisible();
  }
  await page.goto('/cookies');
  await expect(page.getByText('koto_session', { exact: true }).locator('visible=true').first()).toBeVisible();
  await page.goto('/confidentialite');
  await expect(page.getByText('Render Services, Inc.').first()).toBeVisible();
  expect(google).toEqual([]);

  await page.evaluate(() => localStorage.setItem('koto-locale', 'en'));
  await page.reload();
  await expect(page.getByRole('heading', { level: 1, name: 'Privacy policy' })).toBeVisible();
  await expect(page.getByRole('heading', { name: 'Your rights' })).toBeVisible();
  await page.evaluate(() => localStorage.removeItem('koto-locale'));
});
