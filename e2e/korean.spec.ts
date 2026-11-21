import { Page, expect, test } from '@playwright/test';

/** Version en ligne : un compte qui apprend le coréen (TOPIK), puis passe au japonais et revient. */
async function answerAll(page: Page, endHeading: RegExp) {
  for (let guard = 0; guard < 150; guard++) {
    if (await page.getByRole('heading', { name: endHeading }).isVisible().catch(() => false)) return;
    const q = page.getByTestId('question').last();
    if (!(await q.isVisible().catch(() => false))) {
      await page.waitForTimeout(200);
      continue;
    }
    const type = await q.getAttribute('data-type');
    if (type === 'sentence_order') {
      const bank = q.getByTestId('token-bank');
      while ((await bank.getByRole('button').count()) > 0) await bank.getByRole('button').first().click();
      await q.getByRole('button', { name: 'Vérifier' }).click();
    } else if (type === 'matching') {
      const right = q.locator('[data-match=right]');
      const n = await right.count();
      for (let i = 0; i < n; i++) await right.nth(i).click();
      await q.getByRole('button', { name: 'Vérifier' }).click();
    } else {
      await q.getByRole('group').getByRole('button').first().click();
    }
    const qid = await q.getAttribute('data-qid');
    await page.getByRole('button', { name: /^(Continuer|Terminer)$/ }).click();
    await expect(page.locator(`[data-qid="${qid}"]`)).toHaveCount(0);
  }
  throw new Error('La session ne s’est pas terminée');
}

test('coréen : inscription, choix du coréen, leçon de hangeul, saga du hwarang, examen TOPIK, retour au japonais', async ({ page }) => {
  await page.goto('/');
  await page.getByLabel('Pseudo').fill('Minji');
  await page.getByLabel('Adresse e-mail').fill(`ko_${Date.now()}_${Math.floor(Math.random() * 1e6)}@test.local`);
  await page.getByLabel('Mot de passe').fill('motdepasse-e2e');
  await page.getByRole('button', { name: 'Créer mon compte' }).click();

  await expect(page.getByRole('heading', { name: 'Quelle langue veux-tu apprendre ?' })).toBeVisible();
  await page.getByRole('radio', { name: /Coréen/ }).click();
  await page.getByRole('radio', { name: /Je pars de zéro/ }).click();
  for (let i = 0; i < 5; i++) await page.getByRole('button', { name: 'Suivant' }).click();
  await page.getByRole('button', { name: 'Commencer l’aventure' }).click();

  await expect(page.getByText('Minji 님, 안녕하세요')).toBeVisible();
  await page.getByRole('link', { name: 'Commencer la leçon' }).click();
  await expect(page.getByRole('heading', { name: 'Les voyelles ㅏ ㅓ ㅗ ㅜ ㅡ ㅣ' })).toBeVisible();
  await page.getByRole('button', { name: 'Passer aux exercices' }).click();
  await answerAll(page, /Sans faute|Leçon terminée/);

  await page.goto('/path');
  await expect(page.getByRole('heading', { name: 'TOPIK 1 : La Voie du hwarang' })).toBeVisible();
  await expect(page.locator('[data-theme-map="korea"]')).toBeVisible();
  // Deuxième niveau coréen : la saga du conteur
  await page.getByRole('tab', { name: /TOPIK 2/ }).click();
  await expect(page.getByRole('heading', { name: 'TOPIK 2 : Le Conteur du tigre blanc' })).toBeVisible();
  await expect(page.getByRole('heading', { name: /Le village de Jeonju/ })).toBeVisible();
  await page.getByRole('tab', { name: /TOPIK 3/ }).click();
  await expect(page.getByRole('heading', { name: 'TOPIK 3 : L’Inspecteur royal secret' })).toBeVisible();
  await page.getByRole('tab', { name: /TOPIK 4/ }).click();
  await expect(page.getByRole('heading', { name: 'TOPIK 4 : L’Historien des Annales' })).toBeVisible();
  await page.getByRole('tab', { name: /TOPIK 5/ }).click();
  await expect(page.getByRole('heading', { name: 'TOPIK 5 : Le Chant de la princesse Bari' })).toBeVisible();
  await page.getByRole('tab', { name: /TOPIK 6/ }).click();
  await expect(page.getByRole('heading', { name: 'TOPIK 6 : La Légende de Dangun' })).toBeVisible();
  await page.getByRole('tab', { name: /TOPIK 1/ }).click();
  await expect(page.getByRole('heading', { name: 'TOPIK 1 : La Voie du hwarang' })).toBeVisible();

  // Examen blanc TOPIK I : consignes en coréen
  await page.goto('/exam/topik1-official');
  await expect(page.getByRole('heading', { name: 'Examen blanc TOPIK I — format officiel' })).toBeVisible();
  await page.getByRole('button', { name: 'Commencer l’examen' }).click();
  await expect(page.getByText('다음을 듣고 물음에 맞는 대답을 고르십시오.').first()).toBeVisible();

  // Passage au japonais depuis le parcours, puis retour au coréen
  await page.goto('/path');
  await page.getByTestId('study-language').filter({ visible: true }).first().getByRole('radio', { name: /日本語/ }).click();
  await expect(page.getByRole('heading', { name: /N5 : La Voie du samouraï/ })).toBeVisible();
  await page.goto('/characters');
  await expect(page.getByRole('tab', { name: /Hiragana/ })).toBeVisible();
  await page.goto('/path');
  await page.getByTestId('study-language').filter({ visible: true }).first().getByRole('radio', { name: /한국어/ }).click();
  await expect(page.getByRole('heading', { name: 'TOPIK 1 : La Voie du hwarang' })).toBeVisible();
  await page.goto('/characters');
  await expect(page.getByRole('tab', { name: /Consonnes/ })).toBeVisible();
});
