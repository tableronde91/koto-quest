import { Page, expect, test } from '@playwright/test';

const password = 'motdepasse-e2e';

async function register(page: Page) {
  const email = `e2e_${Date.now()}_${Math.floor(Math.random() * 1e6)}@test.local`;
  await page.goto('/');
  await expect(page).toHaveURL(/\/welcome/);
  await page.getByLabel('Pseudo').fill('Hana');
  await page.getByLabel('Adresse e-mail').fill(email);
  await page.getByLabel('Mot de passe').fill(password);
  await page.getByRole('button', { name: 'Créer mon compte' }).click();
  return email;
}

async function onboard(page: Page, level = 'Je pars de zéro') {
  await expect(page.getByRole('heading', { name: 'Où en es-tu en japonais ?' })).toBeVisible();
  await page.getByRole('radio', { name: new RegExp(level) }).click();
  for (let i = 0; i < 5; i++) await page.getByRole('button', { name: 'Suivant' }).click();
  await page.getByRole('button', { name: 'Commencer l’aventure' }).click();
}

/** Répond à toutes les questions affichées (sans connaître la réponse : on veut tester le parcours, pas le score). */
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
      // Associe chaque ligne à la case « sens » de la même ligne (sans chercher la bonne réponse).
      const right = q.locator('[data-match=right]');
      const n = await right.count();
      for (let i = 0; i < n; i++) await right.nth(i).click();
      await q.getByRole('button', { name: 'Vérifier' }).click();
    } else {
      await q.getByRole('group').getByRole('button').first().click();
    }
    const qid = await q.getAttribute('data-qid');
    await page.getByRole('button', { name: /^(Continuer|Terminer)$/ }).click();
    // Attend que la question suivante (ou l'écran de fin) remplace celle-ci.
    await expect(page.locator(`[data-qid="${qid}"]`)).toHaveCount(0);
  }
  throw new Error('La session ne s’est pas terminée');
}

test('inscription, onboarding, première leçon, mini-révision et progression persistante', async ({ page }) => {
  const email = await register(page);
  await onboard(page);

  // Tableau de bord : la première leçon est recommandée
  await expect(page.getByRole('heading', { name: 'Prêt·e pour la suite ?' })).toBeVisible();
  await page.getByRole('link', { name: 'Commencer la leçon' }).click();

  // Leçon : objectif, notions, puis exercices
  await expect(page.getByRole('heading', { name: 'Les voyelles あいうえお' })).toBeVisible();
  await expect(page.getByText('Objectif :')).toBeVisible();
  await page.getByRole('button', { name: 'Passer aux exercices' }).click();
  await expect(page.getByRole('progressbar').first()).toBeVisible();
  await answerAll(page, /Sans faute|Leçon terminée/);
  await expect(page.getByText(/XP de fin de leçon/)).toBeVisible();

  // Déconnexion puis reconnexion : la progression est conservée
  await page.goto('/settings');
  await page.getByRole('button', { name: 'Se déconnecter' }).click();
  await expect(page).toHaveURL(/\/welcome/);
  await page.getByRole('tab', { name: 'Se connecter' }).click();
  await page.getByLabel('Adresse e-mail').fill(email);
  await page.getByLabel('Mot de passe').fill(password);
  await page.getByRole('button', { name: 'Me connecter' }).click();
  await expect(page.getByText(/1 leçon\(s\) sur \d+ disponibles/)).toBeVisible();

  // Parcours : leçon terminée et suivante débloquée
  await page.goto('/path');
  await expect(page.getByRole('link', { name: /Les voyelles あいうえお.*Terminée/ })).toBeVisible();
  await expect(page.getByRole('link', { name: /La ligne K.*Disponible/ })).toBeVisible();

  // Statistiques : les 5 kana sont suivis individuellement
  await page.goto('/stats');
  await expect(page.getByRole('heading', { name: 'Grimoire des notions' })).toBeVisible();
  await expect(page.locator('#notions tbody tr')).toHaveCount(5);
});

test('rappels : consentement explicite, défi en popup in-app et mini-quiz', async ({ page }) => {
  await register(page);
  await onboard(page, 'Je lis les hiragana');
  await page.getByRole('link', { name: 'Commencer la leçon' }).click();
  await page.getByRole('button', { name: 'Passer aux exercices' }).click();
  await answerAll(page, /Sans faute|Leçon terminée/);

  await page.goto('/settings#rappels');
  await expect(page.getByRole('button', { name: 'Recevoir un défi maintenant' })).toHaveCount(0); // rien sans consentement
  await page.getByLabel('J’accepte de recevoir des défis de révision').click();
  await expect(page.getByLabel('J’accepte de recevoir des défis de révision')).toBeChecked();
  await page.getByRole('button', { name: /Tranquille/ }).click();
  await expect(page.getByText(/Créneaux prévus : \d\d:\d\d, \d\d:\d\d\./)).toBeVisible();
  await page.getByRole('button', { name: 'Recevoir un défi maintenant' }).click();

  const dialog = page.getByRole('dialog');
  await expect(dialog).toBeVisible({ timeout: 15_000 });
  await dialog.getByRole('group').getByRole('button').first().click();
  await expect(dialog.getByText(/Bonne réponse|Pas tout à fait/)).toBeVisible();
  await dialog.getByRole('button', { name: 'Fermer' }).click();
  await expect(dialog).toBeHidden();

  // Retrait du consentement : plus aucun réglage d'envoi
  await page.getByLabel('J’accepte de recevoir des défis de révision').click();
  await expect(page.getByLabel('J’accepte de recevoir des défis de révision')).not.toBeChecked();
  await expect(page.getByRole('button', { name: 'Recevoir un défi maintenant' })).toHaveCount(0);
});

test.describe('version anglaise', () => {
  test.use({ locale: 'en-GB' });

  test('en ligne : inscription en anglais, langue enregistrée sur le compte, erreurs du serveur traduites', async ({ page }, info) => {
    test.skip(info.project.name !== 'desktop', 'un seul passage suffit');
    await page.goto('/');
    await expect(page.getByRole('heading', { name: 'A word in the morning, a challenge in the afternoon.' })).toBeVisible();
    // Erreur renvoyée par l'API en français, affichée en anglais
    await page.getByRole('tab', { name: 'Log in' }).click();
    await page.getByLabel('Email address').fill('nobody@test.local');
    await page.getByLabel('Password').fill('wrong-password');
    await page.getByRole('button', { name: 'Log me in' }).click();
    await expect(page.getByText('Incorrect email or password.')).toBeVisible();

    await page.getByRole('tab', { name: 'Create an account' }).click();
    await page.getByLabel('Username').fill('Emma');
    await page.getByLabel('Email address').fill(`en_${Date.now()}_${Math.floor(Math.random() * 1e6)}@test.local`);
    await page.getByLabel('Password').fill('password-e2e');
    await page.getByRole('button', { name: 'Create my account' }).click();
    await expect(page.getByRole('heading', { name: 'Where are you with Japanese?' })).toBeVisible();
    for (let i = 0; i < 5; i++) await page.getByRole('button', { name: 'Next' }).click();
    await page.getByRole('button', { name: 'Start the adventure' }).click();
    await expect(page.getByRole('heading', { name: 'Ready for what’s next?' })).toBeVisible();
    const me = await (await page.request.get('/api/me')).json();
    expect(me.preferences.locale).toBe('en');

    await page.getByRole('link', { name: /^Path/ }).first().click();
    await expect(page.getByRole('heading', { name: /N5: Beginners’ Archipelago/ })).toBeVisible();
    await expect(page.getByRole('button', { name: /Island 1: Discovering hiragana, in progress/ })).toBeVisible();

    // Passage au français : enregistré sur le compte
    await page.getByRole('link', { name: /^Settings/ }).first().click();
    await page.getByRole('radio', { name: 'Français' }).click();
    await expect(page.getByRole('heading', { name: 'Réglages', level: 1 })).toBeVisible();
    expect((await (await page.request.get('/api/me')).json()).preferences.locale).toBe('fr');
  });
});
