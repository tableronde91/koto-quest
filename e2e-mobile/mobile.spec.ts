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
  test.setTimeout(200_000);
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
  // Mode histoire : saga du niveau, chapitre de l'île, et les cinq niveaux
  await expect(page.getByRole('heading', { name: 'N5 : La Voie du samouraï' })).toBeVisible();
  await expect(page.getByRole('heading', { name: /Chapitre 1 · Le premier pinceau/ })).toBeVisible();
  await expect(page.getByText(/Le Kappa garde le gué/).first()).toBeVisible();
  await page.getByRole('tab', { name: /^N4/ }).click();
  await expect(page.getByRole('heading', { name: 'N4 : L’Ombre du ninja' })).toBeVisible();
  await page.getByRole('tab', { name: /^N1/ }).click();
  await expect(page.getByRole('heading', { name: 'N1 : Le Règne du shōgun' })).toBeVisible();

  // Examen blanc depuis l'île finale : chronomètre, réponse, copie rendue, résultat par compétence
  await page.getByRole('button', { name: /Examen blanc : Simulation JLPT N1/ }).click();
  await page.getByRole('button', { name: 'Commencer l’examen' }).click();
  await expect(page.getByRole('timer')).toBeVisible();
  await expect(page.getByText(/45:00|44:5\d/)).toBeVisible();
  await page.getByTestId('exam-question').getByRole('radio').first().click();
  await expect(page.getByText('1 réponse sur 44.')).toBeVisible();
  await page.getByRole('button', { name: 'Rendre ma copie maintenant' }).click();
  await page.getByRole('button', { name: 'Confirmer : rendre ma copie' }).click();
  await expect(page.getByRole('heading', { name: 'Pas encore le seuil' })).toBeVisible();
  await expect(page.getByRole('heading', { name: 'Par compétence' })).toBeVisible();
  await page.getByRole('button', { name: 'Retour au parcours' }).click();
  await expect(page.getByText(/Meilleur score : \d+ %/).first()).toBeVisible();
  // Gardien pas encore accessible tant que les leçons de l'île ne sont pas finies
  await expect(page.getByRole('button', { name: /Gardien : Le Sceau Animé, termine les leçons/ })).toBeDisabled();

  // Caractères : grille des hiragana (les voyelles sont vues), fiche d'un caractère, pratique d'un groupe
  await page.getByRole('tab', { name: /Kana/ }).click();
  await expect(page.getByRole('heading', { name: 'Caractères' })).toBeVisible();
  await page.getByRole('button', { name: /^あ, a, / }).click();
  await expect(page.getByTestId('char-sheet')).toBeVisible();
  await page.getByRole('button', { name: 'Fermer' }).click();
  await expect(page.getByTestId('char-sheet')).toHaveCount(0);
  await page.getByRole('button', { name: /^Pratiquer : / }).first().click();
  await answerUntil(page, /Séance terminée/);
  await expect(page.getByText(/bonnes réponses · \+\d+ XP/)).toBeVisible();
  await page.getByRole('button', { name: 'Retour aux caractères' }).click();
  await page.getByRole('tab', { name: 'Kanji' }).click();
  await expect(page.getByTestId('char-group').filter({ visible: true }).first()).toBeVisible();
  // Expressions : recherche, puis un thème à pratiquer (on quitte après la première question)
  await page.getByRole('tab', { name: 'Expressions' }).click();
  await page.getByLabel('Rechercher une expression').fill('merci');
  await expect(page.getByText(/expression\(s\) trouvée\(s\)/)).toBeVisible();
  await expect(page.getByTestId('expression').filter({ visible: true }).first()).toBeVisible();
  await page.getByLabel('Rechercher une expression').fill('');
  await page.getByRole('button', { name: 'Apprendre ces expressions' }).click();
  await expect(page.getByTestId('question').last()).toBeVisible({ timeout: 10_000 });
  await page.getByRole('button', { name: 'Quitter la session' }).click();
  await expect(page.getByRole('heading', { name: 'Caractères' })).toBeVisible();

  // Lecture : tout est ouvert, liseuse avec traduction au toucher, compréhension
  await page.getByRole('tab', { name: /Lecture/ }).click();
  await expect(page.getByRole('heading', { name: 'Lecture', exact: true })).toBeVisible();
  await expect(page.getByText('Conseillé aujourd’hui')).toBeVisible();
  await page.getByRole('button', { name: 'Lire le chapitre du jour' }).click();
  await expect(page.getByTestId('reader')).toBeVisible();
  await page.getByTestId('reader').getByRole('button').first().click();
  await expect(page.getByText(/Il était une fois|Autrefois/).first()).toBeVisible();
  for (let k = 0; k < 8; k++) {
    const first = page.getByRole('radio').nth(k * 3);
    if (!(await first.isVisible().catch(() => false))) break;
    await first.click();
  }
  await page.getByRole('button', { name: 'Valider mes réponses' }).click();
  await expect(page.getByText(/bonnes réponses/)).toBeVisible();
  await expect(page.getByText(/\+\d+ XP/).filter({ visible: true }).first()).toBeVisible();
  await page.getByRole('button', { name: 'Tous les contes' }).last().click();
  await expect(page.getByText('Lu aujourd’hui')).toBeVisible();
  // Un chapitre éloigné s'ouvre directement
  await page.getByTestId('story').last().getByRole('link').last().click();
  await expect(page.getByTestId('reader')).toBeVisible();
  await page.getByRole('link', { name: '← Tous les contes' }).click();

  // Mini-jeux : les jeux de kana sont débloqués après la première leçon ; une partie complète d'une minute
  await page.getByRole('tab', { name: /Jeux/ }).click();
  await expect(page.getByRole('heading', { name: 'Mini-jeux' })).toBeVisible();
  await expect(page.getByTestId('game-card')).toHaveCount(3);
  const playable = page.getByRole('button', { name: /^Jouer à / });
  await expect(playable.first()).toBeVisible();
  await playable.first().click();
  await page.getByRole('button', { name: 'C’est parti' }).click();
  await expect(page.getByRole('timer')).toBeVisible({ timeout: 5000 });
  for (let k = 0; k < 6; k++) {
    await page.getByLabel('Réponses').getByRole('button').first().click();
    await page.waitForTimeout(800);
  }
  await expect(page.getByRole('heading', { name: /Nouveau record|Partie terminée/ })).toBeVisible({ timeout: 75_000 });
  await expect(page.getByTestId('final-score')).toBeVisible();
  await page.getByRole('button', { name: 'Autres mini-jeux' }).click();
  await expect(page.getByText(/Record : \d+, 1 partie/)).toBeVisible();

  // Duels : entraînement contre un rōnin, une réponse puis abandon
  await page.getByRole('button', { name: 'Entrer dans le dojo' }).click();
  await expect(page.getByText('TON RANG')).toBeVisible();
  await expect(page.getByTestId('duel-friends').filter({ visible: true })).toBeVisible();
  await page.getByTestId('duel-practice').click();
  await expect(page.getByTestId('duel-arena').filter({ visible: true })).toBeVisible();
  await expect(page.getByTestId('duel-question').filter({ visible: true })).toBeVisible({ timeout: 15_000 });
  await page.getByTestId('duel-choice').filter({ visible: true }).first().click();
  await expect(page.getByText(/Juste ! Coup de|Raté…|pas de réponse|juste en|faux/).filter({ visible: true }).first()).toBeVisible({ timeout: 15_000 });
  await page.getByRole('button', { name: 'Abandonner' }).filter({ visible: true }).first().click();
  await page.getByRole('button', { name: 'Abandonner' }).filter({ visible: true }).last().click();
  await expect(page.getByText('Tu as abandonné.').filter({ visible: true })).toBeVisible({ timeout: 10_000 });
  await page.getByRole('button', { name: 'Retour au dojo' }).filter({ visible: true }).click();
  await page.getByRole('tab', { name: 'Mes duels' }).filter({ visible: true }).click();
  await expect(page.getByText('Défaite').filter({ visible: true }).first()).toBeVisible();
  await page.getByRole('button', { name: 'Retour' }).filter({ visible: true }).click();

  // Révisions, profil et réglages
  await page.getByRole('tab', { name: /Révisions/ }).click();
  await expect(page.getByRole('heading', { name: 'Révisions' })).toBeVisible();
  await page.getByRole('tab', { name: /Profil/ }).click();
  await expect(page.getByRole('heading', { name: 'Profil' }).filter({ visible: true })).toBeVisible();
  await expect(page.getByText(/^Niveau \d+ · objectif JLPT N5$/).filter({ visible: true })).toBeVisible();
  await expect(page.getByTestId('my-code').filter({ visible: true })).toHaveText(/^KQ-/);
  // Niveau visé modifié depuis le profil, enregistré sur le compte
  await page.getByRole('radiogroup', { name: 'Niveau visé' }).filter({ visible: true }).getByRole('radio', { name: 'N4' }).click();
  await expect(page.getByText(/objectif JLPT N4$/).filter({ visible: true })).toBeVisible();
  await page.getByRole('radiogroup', { name: 'Niveau visé' }).filter({ visible: true }).getByRole('radio', { name: 'N5' }).click();
  await expect(page.getByText(/objectif JLPT N5$/).filter({ visible: true })).toBeVisible();
  await page.getByRole('button', { name: 'Réglages' }).filter({ visible: true }).click();
  await expect(page.getByRole('heading', { name: 'Réglages' }).filter({ visible: true })).toBeVisible();
  await page.getByRole('switch', { name: 'Recevoir les rappels' }).click();
  await expect(page.getByText(/Rappels enregistrés/).filter({ visible: true })).toBeVisible();
  await expect(page.getByText(/Créneaux du jour/).filter({ visible: true })).toBeVisible();

  // Anglais : interface, données de l'API et récit traduits ; retour au français
  await page.getByRole('radio', { name: 'English' }).click();
  await expect(page.getByRole('heading', { name: 'Settings' }).filter({ visible: true })).toBeVisible();
  await page.getByRole('button', { name: 'Back' }).filter({ visible: true }).click();
  await expect(page.getByRole('heading', { name: 'Profile' }).filter({ visible: true })).toBeVisible();
  await page.getByRole('tab', { name: /Path/ }).click();
  await expect(page.getByText(/STORY MODE/).filter({ visible: true }).first()).toBeVisible();
  await expect(page.getByText(/^Chapter 1 · /).filter({ visible: true }).first()).toBeVisible();
  await page.getByRole('tab', { name: /Home/ }).click();
  await expect(page.getByText('Daily quests').filter({ visible: true })).toBeVisible();
  await page.getByRole('tab', { name: /Profile/ }).click();
  await page.getByRole('button', { name: 'Settings' }).filter({ visible: true }).click();
  await page.getByRole('radio', { name: 'Français' }).click();
  await expect(page.getByRole('heading', { name: 'Réglages' }).filter({ visible: true })).toBeVisible();

  // Session conservée au rechargement, puis déconnexion
  await page.reload();
  await expect(page.getByRole('heading', { name: 'Réglages' })).toBeVisible();
  await page.getByRole('button', { name: 'Se déconnecter' }).click();
  await expect(page.getByRole('heading', { name: 'Koto Quest' })).toBeVisible();
});
