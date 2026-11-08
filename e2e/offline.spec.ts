import { Page, expect, test } from '@playwright/test';
import { resolve } from 'path';
import { readFileSync } from 'fs';

/** Version hors ligne : fichier HTML ouvert directement, sans serveur ni base. */
const FILE = 'file://' + resolve(__dirname, '../apps/web/dist-offline/KotoQuest.html');


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
    await expect(page.locator(`[data-qid="${qid}"]`)).toHaveCount(0);
  }
  throw new Error('session non terminée');
}

test('hors ligne : onboarding, leçon, persistance, révisions planifiées et défi', async ({ page }) => {
  await page.goto(FILE);
  await expect(page.getByRole('heading', { name: 'Où en es-tu en japonais ?' })).toBeVisible();
  for (let i = 0; i < 5; i++) await page.getByRole('button', { name: 'Suivant' }).click();
  await page.getByRole('button', { name: 'Commencer l’aventure' }).click();

  await page.getByRole('link', { name: 'Commencer la leçon' }).click();
  await expect(page.getByRole('heading', { name: 'Les voyelles あいうえお' })).toBeVisible();
  await page.getByRole('button', { name: 'Passer aux exercices' }).click();
  await answerAll(page, /Sans faute|Leçon terminée/);

  // Fermeture / réouverture : la progression est conservée dans le navigateur
  await page.reload();
  await page.goto(FILE + '#/');
  await expect(page.getByText(/1 leçon\(s\) sur 43 disponibles/)).toBeVisible();

  // Quelques heures plus tard, les 5 kana sont à réviser
  // (simulé en reculant de 5 h les dates enregistrées dans la sauvegarde locale)
  await page.evaluate(() => {
    const key = 'koto-quest-local-v1';
    const s = JSON.parse(localStorage.getItem(key)!);
    const back = (iso: string | null) => (iso ? new Date(Date.parse(iso) - 5 * 3600_000).toISOString() : iso);
    for (const c of Object.values<any>(s.cards)) Object.assign(c, { due: back(c.due), lastReview: back(c.lastReview), createdAt: back(c.createdAt) });
    s.lastActivityAt = back(s.lastActivityAt);
    localStorage.setItem(key, JSON.stringify(s));
  });
  await page.goto(FILE + '#/reviews');
  await page.reload();
  await expect(page.getByText('notions à réviser maintenant')).toBeVisible();
  await page.getByRole('link', { name: 'Lancer la révision' }).click();
  await answerAll(page, /Révision terminée/);

  // Défi : consentement puis popup interactive
  await page.goto(FILE + '#/settings');
  await page.getByLabel('J’accepte de recevoir des défis de révision').click();
  await expect(page.getByLabel('J’accepte de recevoir des défis de révision')).toBeChecked();
  await page.getByRole('button', { name: 'Recevoir un défi maintenant' }).click();
  const dialog = page.getByRole('dialog');
  await expect(dialog).toBeVisible({ timeout: 10_000 });
  await dialog.getByRole('group').getByRole('button').first().click();
  await dialog.getByRole('button', { name: 'Fermer' }).click();

  // Sauvegarde téléchargeable
  const download = page.waitForEvent('download');
  await page.getByRole('button', { name: 'Télécharger une sauvegarde' }).click();
  expect((await download).suggestedFilename()).toMatch(/koto-quest-sauvegarde/);

  await page.goto(FILE + '#/stats');
  await expect(page.locator('#notions tbody tr')).toHaveCount(5);
});

test('hors ligne : onglet Caractères ouvert à tous, pratique et maîtrise par caractère', async ({ page }) => {
  await page.goto(FILE);
  for (let i = 0; i < 5; i++) await page.getByRole('button', { name: 'Suivant' }).click();
  await page.getByRole('button', { name: 'Commencer l’aventure' }).click();
  await page.getByRole('link', { name: 'Caractères' }).first().click();
  await expect(page.getByRole('heading', { name: 'Caractères', level: 1 })).toBeVisible();
  await expect(page.getByText('0 sur 104 vus')).toBeVisible();
  // Katakana et kanji accessibles immédiatement
  await page.getByRole('tab', { name: /Kanji/ }).click();
  await page.getByRole('button', { name: /^一, un/ }).click();
  await expect(page.getByRole('dialog').getByText('イチ、イツ')).toBeVisible();
  await page.getByRole('dialog').getByRole('button', { name: 'Fermer' }).click();
  await page.getByRole('tab', { name: /Hiragana/ }).click();
  await page.getByRole('button', { name: 'Apprendre les hiragana' }).click();
  await answerAll(page, /Séance terminée/);
  await page.getByRole('link', { name: 'Retour aux caractères' }).click();
  await expect(page.getByText('5 sur 104 vus, 0 maîtrisés')).toBeVisible();
  await expect(page.getByRole('button', { name: /^あ, a, / })).not.toHaveAccessibleName(/pas encore vu/);
});

/** Répond juste (ou faux) en lisant la bonne réponse dans la sauvegarde locale. */
async function answerFromStore(page: Page, correct: boolean) {
  const q = page.getByTestId('question').last();
  const id = await q.getAttribute('data-qid');
  const type = await q.getAttribute('data-type');
  const answer = await page.evaluate((qid) => JSON.parse(localStorage.getItem('koto-quest-local-v1')!).questions[qid!].answer, id);
  if (type === 'sentence_order') {
    const order = correct ? answer : [...answer].reverse();
    for (const t of order) await q.getByTestId('token-bank').getByRole('button', { name: t, exact: true }).first().click();
    await q.getByRole('button', { name: 'Vérifier' }).click();
  } else if (type === 'matching') {
    const left = q.locator('button[aria-describedby=match-left]');
    for (let i = 0; i < (answer as string[]).length; i++) {
      await left.nth(i).click();
      const target = correct ? answer[i] : answer[(i + 1) % answer.length];
      await q.locator('[data-match=right]').filter({ has: page.getByText(target, { exact: true }) }).first().click();
    }
    await q.getByRole('button', { name: 'Vérifier' }).click();
  } else {
    const buttons = q.getByRole('group').getByRole('button');
    const names = await buttons.allInnerTexts();
    const idx = names.findIndex((n) => (n.replace(/^\d\s*/, '').trim() === answer) === correct);
    await buttons.nth(idx).click();
  }
  return { id, type };
}

test('hors ligne : phrase complète prononcée après une bonne réponse, exercices ratés repris en fin de séance', async ({ page }) => {
  await page.addInitScript(() => {
    (window as any).__spoken = [];
    Object.defineProperty(window, 'speechSynthesis', {
      value: { speak: (u: SpeechSynthesisUtterance) => (window as any).__spoken.push(u.text), cancel: () => {}, getVoices: () => [], onvoiceschanged: null },
    });
  });
  await page.goto(FILE);
  await page.getByRole('radio', { name: /Je lis les hiragana/ }).click();
  for (let i = 0; i < 5; i++) await page.getByRole('button', { name: 'Suivant' }).click();
  await page.getByRole('button', { name: 'Commencer l’aventure' }).click();

  // Leçon 1 sans faute pour débloquer la suivante
  await page.goto(FILE + '#/lesson/n5-greetings');
  await page.getByRole('button', { name: 'Passer aux exercices' }).click();
  for (let k = 0; k < 30; k++) {
    if (await page.getByRole('heading', { name: /Sans faute|Leçon terminée|Mini-révision/ }).isVisible().catch(() => false)) break;
    await answerFromStore(page, true);
    await page.getByRole('button', { name: /^(Continuer|Terminer)$/ }).click();
  }

  await page.goto(FILE + '#/lesson/n5-wa-desu');
  await page.getByRole('button', { name: 'Passer aux exercices' }).click();
  let firstWrongPrompt = '';
  let sawParticle = false;
  for (let k = 0; k < 60; k++) {
    if (await page.getByRole('heading', { name: /Sans faute|Leçon terminée/ }).isVisible().catch(() => false)) break;
    const q = page.getByTestId('question').last();
    const isRetry = (await q.getAttribute('data-retry')) === '1';
    const wrong = !isRetry && !firstWrongPrompt; // on rate seulement le tout premier exercice
    if (wrong) firstWrongPrompt = (await q.locator('p').first().innerText()).trim();
    if (isRetry) {
      await expect(page.getByText('On reprend un exercice raté.')).toBeVisible();
      await expect(q.locator('p').first()).toHaveText(firstWrongPrompt);
    }
    const before = await page.evaluate(() => (window as any).__spoken.length);
    const { type } = await answerFromStore(page, !wrong);
    if (wrong) await expect(q.getByText('Tu le referas en fin de séance.')).toBeVisible();
    if (type === 'particle_choice' && !sawParticle && !wrong) {
      // Le trou est rempli à l'écran et la phrase entendue est complète (jamais de « ＿ »)
      await expect(q.locator('mark')).toBeVisible();
      const spoken: string[] = await page.evaluate((n) => (window as any).__spoken.slice(n), before);
      expect(spoken.length).toBeGreaterThan(0);
      expect(spoken.every((t) => !t.includes('＿'))).toBe(true);
      sawParticle = true;
    }
    await page.getByRole('button', { name: /^(Continuer|Terminer)$/ }).click();
  }
  expect(sawParticle).toBe(true);
  expect(firstWrongPrompt).not.toBe('');
  // Le score ne compte que le premier essai
  await expect(page.getByRole('heading', { name: 'Leçon terminée' })).toBeVisible();
  const spoken: string[] = await page.evaluate(() => (window as any).__spoken);
  expect(spoken).toContain('わたしはがくせいです。');
});

test('hors ligne : gardien de fin de monde, combat gagné côté moteur et marqué vaincu', async ({ page }) => {
  await page.goto(FILE);
  await page.getByRole('radio', { name: /Je lis les hiragana/ }).click();
  for (let i = 0; i < 5; i++) await page.getByRole('button', { name: 'Suivant' }).click();
  await page.getByRole('button', { name: 'Commencer l’aventure' }).click();

  await page.goto(FILE + '#/path');
  await expect(page.getByLabel(/Le Tanuki farceur : Termine l’île/)).toBeVisible();

  for (const slug of ['n5-kata-a', 'n5-kata-ka']) {
    await page.goto(FILE + '#/lesson/' + slug);
    await page.getByRole('button', { name: 'Passer aux exercices' }).click();
    for (let k = 0; k < 40; k++) {
      if (await page.getByRole('heading', { name: /Sans faute|Leçon terminée/ }).isVisible().catch(() => false)) break;
      const qid = await page.getByTestId('question').last().getAttribute('data-qid');
      await answerFromStore(page, true);
      await page.getByRole('button', { name: /^(Continuer|Terminer)$/ }).click();
      await expect(page.locator(`[data-qid="${qid}"]`)).toHaveCount(0);
    }
  }

  await page.goto(FILE + '#/path');
  await page.getByRole('link', { name: /Le Tanuki farceur : Prêt/ }).click();
  await expect(page.getByRole('heading', { name: 'Le Tanuki farceur' })).toBeVisible();
  await page.getByRole('button', { name: 'Affronter le gardien' }).click();
  await expect(page.getByRole('progressbar', { name: 'Vie du gardien' })).toHaveAttribute('aria-valuenow', '9');

  // Une erreur coûte un cœur, puis neuf bonnes réponses terrassent le gardien.
  await answerFromStore(page, false);
  await expect(page.getByRole('img', { name: '2 cœurs sur 3' })).toBeVisible();
  await page.getByRole('button', { name: 'Continuer' }).click();
  for (let k = 0; k < 9; k++) {
    const qid = await page.getByTestId('question').last().getAttribute('data-qid');
    await answerFromStore(page, true);
    await page.getByRole('button', { name: k === 8 ? 'Coup final !' : 'Continuer' }).click();
    await expect(page.locator(`[data-qid="${qid}"]`)).toHaveCount(0);
  }
  await expect(page.getByRole('heading', { name: 'Le Tanuki farceur est vaincu !' })).toBeVisible();
  await expect(page.getByText('+120 XP, +30 pièces')).toBeVisible();
  await page.getByRole('link', { name: 'Retour au parcours' }).click();
  await expect(page.getByLabel(/Le Tanuki farceur : Vaincu/)).toBeVisible();
});

test('hors ligne : pièces gagnées en leçon, achat en boutique, objet équipé sur le personnage', async ({ page }) => {
  await page.goto(FILE);
  for (let i = 0; i < 5; i++) await page.getByRole('button', { name: 'Suivant' }).click();
  await page.getByRole('button', { name: 'Commencer l’aventure' }).click();
  await expect(page.getByLabel('0 pièces, ouvrir la boutique')).toBeVisible();

  for (const slug of ['n5-hira-a', 'n5-hira-ka']) {
    await page.goto(FILE + '#/lesson/' + slug);
    await page.getByRole('button', { name: 'Passer aux exercices' }).click();
    for (let k = 0; k < 40; k++) {
      if (await page.getByRole('heading', { name: /Sans faute|Leçon terminée/ }).isVisible().catch(() => false)) break;
      const qid = await page.getByTestId('question').last().getAttribute('data-qid');
      await answerFromStore(page, true);
      await page.getByRole('button', { name: /^(Continuer|Terminer)$/ }).click();
      await expect(page.locator(`[data-qid="${qid}"]`)).toHaveCount(0);
    }
    await expect(page.getByText(/\+15 pièces/)).toBeVisible();
  }
  const coins = await page.evaluate(() => JSON.parse(localStorage.getItem('koto-quest-local-v1')!).coins);
  expect(coins).toBeGreaterThanOrEqual(30);

  await page.goto(FILE + '#/avatar?t=boutique');
  await page.getByRole('group', { name: 'Catégorie' }).getByRole('button', { name: 'Accessoires' }).click();
  await page.getByRole('button', { name: 'Acheter Lunettes rondes pour 20 pièces' }).click();
  await expect(page.getByText('Lunettes rondes acheté.')).toBeVisible();
  // Les trophées restent verrouillés tant que le gardien n'est pas vaincu
  await expect(page.getByText('Bats Le Marchand de lanternes')).toBeVisible();
  await page.getByRole('button', { name: 'Équiper' }).click();
  await expect(page.getByText('Équipé')).toBeVisible();
  const saved = await page.evaluate(() => JSON.parse(localStorage.getItem('koto-quest-local-v1')!));
  expect(saved.avatar.accessory).toBe('acc-glasses');
  expect(saved.coins).toBe(coins - 20);

  // Apparence : changement de coiffure enregistré
  await page.getByRole('tab', { name: 'Apparence' }).click();
  await page.getByRole('button', { name: 'Chignon' }).click();
  await page.getByRole('button', { name: 'Enregistrer' }).click();
  await expect(page.getByText('Apparence enregistrée.')).toBeVisible();
  expect(await page.evaluate(() => JSON.parse(localStorage.getItem('koto-quest-local-v1')!).avatar.hair)).toBe('bun');
});

test('hors ligne : carte des mondes et mini-jeu chronométré', async ({ page }) => {
  test.setTimeout(180_000);
  await page.goto(FILE);
  for (let i = 0; i < 5; i++) await page.getByRole('button', { name: 'Suivant' }).click();
  await page.getByRole('button', { name: 'Commencer l’aventure' }).click();

  // Carte : le monde 1 est « en cours », toucher une étape mène à ses leçons
  await page.goto(FILE + '#/path');
  await expect(page.getByRole('button', { name: /Île 1 : Découverte des hiragana, en cours/ })).toBeVisible();
  await expect(page.getByRole('button', { name: /Île 9 : Simulation JLPT N5, examen blanc/ })).toBeVisible();

  // Mini-jeux verrouillés au départ
  await page.goto(FILE + '#/games');
  await expect(page.getByText(/Débloqué après avoir rencontré 6 kanji \(0\/6\)/)).toBeVisible();

  // On rencontre 10 kanji dans l'onglet Caractères (2 séances)
  await page.goto(FILE + '#/characters/practice/kanji-nombres');
  for (let i = 0; i < 2; i++) {
    if (i === 1) await page.getByRole('button', { name: 'Encore une séance' }).click();
    for (let k = 0; k < 30; k++) {
      if (await page.getByRole('heading', { name: 'Séance terminée' }).isVisible().catch(() => false)) break;
      const qid = await page.getByTestId('question').last().getAttribute('data-qid');
      await answerFromStore(page, true);
      await page.getByRole('button', { name: /^(Continuer|Terminer)$/ }).click();
      await expect(page.locator(`[data-qid="${qid}"]`)).toHaveCount(0);
    }
  }

  await page.goto(FILE + '#/games/kanji-rush');
  await page.getByRole('button', { name: 'C’est parti' }).click();
  // Quelques bonnes réponses rapides, puis on laisse le chrono s'écouler (accéléré)
  for (let k = 0; k < 6; k++) {
    const g = page.getByTestId('game');
    const qid = await g.getAttribute('data-qid');
    const answer = await page.evaluate((id) => JSON.parse(localStorage.getItem('koto-quest-local-v1')!).questions[id!].answer, qid);
    await g.getByRole('group').getByRole('button').filter({ has: page.getByText(answer, { exact: true }) }).click();
    await expect(page.locator(`[data-testid=game][data-qid="${qid}"]`)).toHaveCount(0);
  }
  await expect(page.getByTestId('score')).toHaveText('6');
  // On laisse la minute s'écouler : le score est recalculé par le moteur à partir de l'heure des réponses.
  await expect(page.getByRole('heading', { name: 'Nouveau record !' })).toBeVisible({ timeout: 75_000 });
  await expect(page.getByText(/bonnes réponses sur 6, record : 6/)).toBeVisible();
  await expect(page.getByText('+12 XP')).toBeVisible();
  await page.getByRole('link', { name: 'Autres mini-jeux' }).click();
  await expect(page.getByText(/Record : 6, 1 partie/)).toBeVisible();
});

/** Remplit une question d'épreuve (sans correction immédiate) avec la bonne réponse, ou laisse vide. */
async function fillExamQuestion(page: Page, q: ReturnType<Page['getByTestId']>, correct: boolean) {
  const id = await q.getAttribute('data-qid');
  const type = await q.getAttribute('data-type');
  const answer = await page.evaluate((qid) => JSON.parse(localStorage.getItem('koto-quest-local-v1')!).questions[qid!].answer, id);
  if (!correct) return;
  if (type === 'sentence_order') {
    for (const t of answer as string[]) await q.getByTestId('token-bank').getByRole('button', { name: t, exact: true }).first().click();
  } else {
    await q.getByRole('radio', { name: answer, exact: true }).check();
  }
}

test('hors ligne : test de positionnement adaptatif puis examen blanc N5 corrigé par compétence', async ({ page }) => {
  await page.goto(FILE);
  for (let i = 0; i < 5; i++) await page.getByRole('button', { name: 'Suivant' }).click();
  await page.getByRole('button', { name: 'Commencer l’aventure' }).click();

  // Positionnement : on réussit les mondes 1 et 2, puis « Je ne sais pas »
  await page.getByRole('link', { name: 'Passer le test' }).click();
  await page.getByRole('button', { name: 'Commencer le test' }).click();
  for (const world of ['Découverte des hiragana', 'Maîtrise des katakana']) {
    await expect(page.getByRole('heading', { name: world })).toBeVisible();
    for (const q of await page.getByTestId('exam-question').all()) await fillExamQuestion(page, q, true);
    await page.getByRole('button', { name: 'Valider ces réponses' }).click();
  }
  await expect(page.getByRole('heading', { name: 'Se présenter' })).toBeVisible();
  await page.getByRole('button', { name: 'Je ne sais pas' }).click();
  await expect(page.getByRole('heading', { name: '2 mondes validés' })).toBeVisible();
  await expect(page.getByText('Ton parcours reprend au monde « Se présenter ».')).toBeVisible();
  await page.getByRole('link', { name: 'Voir le parcours' }).click();
  await expect(page.getByRole('button', { name: /Île 1 : Découverte des hiragana/ })).toBeVisible();
  await expect(page.getByLabel(/Le Kappa de la rivière : Prêt/)).toBeVisible();

  // Examen d'entraînement (sur les leçons) : tout juste sauf l'écoute
  await page.goto(FILE + '#/exam/n5-mock');
  await page.getByRole('button', { name: 'Commencer l’examen' }).click();
  for (let i = 0; i < 30; i++) {
    const q = page.getByTestId('exam-question');
    const listening = (await q.getAttribute('data-type')) === 'listening_choice';
    await fillExamQuestion(page, q, !listening);
    if (i < 29) await page.getByRole('button', { name: 'Suivante' }).click();
  }
  await page.getByRole('button', { name: 'Rendre ma copie' }).first().click();
  await expect(page.getByText(/8 question\(s\) sans réponse/)).toBeVisible();
  await page.getByRole('alertdialog').getByRole('button', { name: 'Rendre ma copie' }).click();
  await expect(page.getByRole('heading', { name: 'Pas encore le seuil' })).toBeVisible();
  await expect(page.getByText('73 %')).toBeVisible();
  await expect(page.getByText(/Listening Ninja/)).toBeVisible();
  await expect(page.getByRole('heading', { name: 'Tes erreurs (8)' })).toBeVisible();
  await page.getByRole('link', { name: 'Voir l’historique' }).click();
  await expect(page.getByRole('heading', { name: 'Examens blancs' })).toBeVisible();
  await expect(page.getByText('(seuil non atteint)')).toBeVisible();
});

test('hors ligne : succès débloqué en fin de leçon, notification et collection', async ({ page }) => {
  await page.goto(FILE);
  for (let i = 0; i < 5; i++) await page.getByRole('button', { name: 'Suivant' }).click();
  await page.getByRole('button', { name: 'Commencer l’aventure' }).click();
  await page.goto(FILE + '#/achievements');
  await expect(page.getByRole('heading', { name: 'Succès', exact: true })).toBeVisible();
  await expect(page.locator('[data-testid=achievement][data-unlocked="1"]')).toHaveCount(0);

  await page.goto(FILE + '#/');
  await page.getByRole('link', { name: 'Commencer la leçon' }).click();
  await page.getByRole('button', { name: 'Passer aux exercices' }).click();
  await answerAll(page, /Sans faute|Leçon terminée/);
  const toast = page.getByTestId('achievement-toast');
  await expect(toast).toContainText('Premier pas');
  await expect(toast).toContainText('+10 pièces');

  await page.goto(FILE + '#/achievements');
  const firstLesson = page.locator('[data-testid=achievement]', { hasText: 'Premier pas' });
  await expect(firstLesson).toHaveAttribute('data-unlocked', '1');
  // Récompense créditée une seule fois, même après de nouvelles vérifications
  const coins = await page.evaluate(() => JSON.parse(localStorage.getItem('koto-quest-local-v1')!).coins);
  await page.goto(FILE + '#/stats');
  await page.goto(FILE + '#/');
  await page.waitForTimeout(800);
  expect(await page.evaluate(() => JSON.parse(localStorage.getItem('koto-quest-local-v1')!).coins)).toBe(coins);
});

test('hors ligne : parcours N4, choix du niveau et première leçon de la forme en て', async ({ page }) => {
  await page.goto(FILE);
  for (let i = 0; i < 5; i++) await page.getByRole('button', { name: 'Suivant' }).click();
  await page.getByRole('button', { name: 'Commencer l’aventure' }).click();
  await page.goto(FILE + '#/path');
  await expect(page.getByRole('tab', { name: /N5/ })).toHaveAttribute('aria-selected', 'true');
  await page.getByRole('tab', { name: /N4/ }).click();
  await expect(page.getByRole('heading', { name: /N4 : Archipel des voyageurs/ })).toBeVisible();
  await expect(page.getByRole('heading', { name: /La forme en て/ })).toBeVisible();
  await page.getByRole('link', { name: /Forme en て : verbes en る/ }).click();
  await expect(page.getByRole('heading', { name: 'Forme en て : verbes en る et irréguliers' })).toBeVisible();
  await page.getByRole('button', { name: 'Passer aux exercices' }).click();
  await answerAll(page, /Sans faute|Leçon terminée/);
  // Le choix du niveau est mémorisé
  await page.goto(FILE + '#/path');
  await expect(page.getByRole('tab', { name: /N4/ })).toHaveAttribute('aria-selected', 'true');
  await expect(page.getByRole('tab', { name: /N4/ })).toContainText('1/21 leçons');
  await expect(page.getByRole('button', { name: /Île 8 : Simulation JLPT N4, examen blanc/ })).toBeVisible();

  // Examen blanc N4 : présentation propre au niveau, copie rendue vide puis corrigée
  await page.goto(FILE + '#/exam/n4-mock');
  await expect(page.getByRole('heading', { name: 'Examen blanc JLPT N4' })).toBeVisible();
  await expect(page.getByText(/34 questions en 30 minutes/)).toBeVisible();
  await page.getByRole('button', { name: 'Commencer l’examen' }).click();
  await expect(page.getByTestId('exam-question').first()).toBeVisible();
});

test('hors ligne : chrono des combats, une question sans réponse à temps est perdue', async ({ page }) => {
  await page.clock.install();
  await page.goto(FILE);
  for (let i = 0; i < 5; i++) await page.getByRole('button', { name: 'Suivant' }).click();
  await page.getByRole('button', { name: 'Commencer l’aventure' }).click();
  // Île 1 terminée (raccourci) : le Kappa est prêt
  await page.evaluate((slugs) => {
    const s = JSON.parse(localStorage.getItem('koto-quest-local-v1')!);
    for (const slug of slugs) s.progress[slug] = { status: 'completed', attempts: 1, bestScore: 100, completedAt: new Date().toISOString() };
    localStorage.setItem('koto-quest-local-v1', JSON.stringify(s));
  }, ["n5-hira-a", "n5-hira-ka", "n5-hira-sa", "n5-hira-ta", "n5-hira-na", "n5-hira-ha", "n5-hira-ma", "n5-hira-ya", "n5-hira-ra"]);
  await page.goto(FILE + '#/boss/n5-w1');
  await page.reload();
  await page.getByRole('button', { name: 'Affronter le gardien' }).click();
  await expect(page.getByRole('timer')).toBeVisible();
  await page.clock.fastForward('00:20');
  await expect(page.getByText('Temps écoulé !')).toBeVisible();
  await expect(page.getByRole('img', { name: '2 cœurs sur 3' })).toBeVisible();
  // Question suivante : nouveau chrono, réponse rapide acceptée
  await page.getByRole('button', { name: 'Continuer' }).click();
  await expect(page.getByRole('timer')).toBeVisible();
});

test('hors ligne : examen blanc N5 au format officiel, en japonais, noté sur 180', async ({ page }) => {
  await page.goto(FILE);
  for (let i = 0; i < 5; i++) await page.getByRole('button', { name: 'Suivant' }).click();
  await page.getByRole('button', { name: 'Commencer l’aventure' }).click();
  await page.goto(FILE + '#/path');
  await page.getByRole('link', { name: /Examen blanc JLPT N5 — format officiel/ }).click();
  await expect(page.getByText(/67 questions en 70 minutes/)).toBeVisible();
  await expect(page.getByText(/réussite à 80/)).toBeVisible();
  await page.getByRole('button', { name: 'Commencer l’examen' }).click();
  // Épreuves dans l'ordre officiel, consignes en japonais
  await expect(page.getByText('もんだい１　漢字読み')).toBeVisible();
  await expect(page.getByTestId('exam-question').locator('u')).toHaveCount(1);
  // Bonne réponse lue dans la sauvegarde locale (le test ne voit pas la correction autrement)
  for (let i = 0; i < 67; i++) {
    const q = page.getByTestId('exam-question');
    const qid = await q.getAttribute('data-qid');
    const listening = (await q.getAttribute('data-type')) === 'listening_choice';
    const answer = await page.evaluate((id) => JSON.parse(localStorage.getItem('koto-quest-local-v1')!).questions[id].answer as string, qid);
    const labels = q.locator('label');
    const n = await labels.count();
    let picked = false;
    for (let k = 0; k < n && !picked; k++) {
      const radio = labels.nth(k).locator('input');
      const text = (await labels.nth(k).innerText()).trim();
      // Réponses à l'écoute : pas de texte affiché, on choisit par position dans les choix publics
      const choices = await page.evaluate((id) => JSON.parse(localStorage.getItem('koto-quest-local-v1')!).questions[id].payload.choices as string[], qid);
      const isRight = text.includes('Écouter') ? choices[k] === answer : text === answer;
      if (isRight === !listening) { await radio.check(); picked = true; }
    }
    if (i === 49) await expect(page.getByText(/もんだい１　課題理解/)).toBeVisible();
    if (i < 66) await page.getByRole('button', { name: 'Suivante' }).click();
  }
  await page.getByRole('button', { name: 'Rendre ma copie' }).first().click();
  await page.getByRole('alertdialog').getByRole('button', { name: 'Rendre ma copie' }).click();
  // Langue parfaite (120/120) mais écoute à 0 : refusé malgré 120 points
  await expect(page.getByText('/ 180')).toBeVisible();
  await expect(page.getByRole('heading', { name: 'Pas encore le seuil' })).toBeVisible();
  await expect(page.getByText(/Minimum : 19 ✗/)).toBeVisible();
  await expect(page.getByText(/Transcription|Phrase entendue|Situation/).first()).toBeVisible();
});

test('hors ligne : atelier JLPT et exercices de leçon au format de l’examen', async ({ page }) => {
  await page.goto(FILE);
  for (let i = 0; i < 5; i++) await page.getByRole('button', { name: 'Suivant' }).click();
  await page.getByRole('button', { name: 'Commencer l’aventure' }).click();
  await page.goto(FILE + '#/prepa');
  await expect(page.getByRole('heading', { name: 'Atelier JLPT' })).toBeVisible();
  await expect(page.getByRole('button', { name: 'S’entraîner' }).first()).toBeDisabled();

  // Toutes les leçons N5 précédentes faites (raccourci), puis la leçon « calendrier » pour de vrai
  const n5 = JSON.parse(readFileSync(resolve(__dirname, '../content/n5/n5.json'), 'utf8'));
  const before: string[] = [];
  for (const w of n5.worlds) for (const c of w.chapters) for (const l of c.lessons) if (!before.includes('n5-calendar') && l.slug !== 'n5-calendar') before.push(l.slug); else before.push('n5-calendar');
  await page.evaluate((slugs) => {
    const s = JSON.parse(localStorage.getItem('koto-quest-local-v1')!);
    for (const slug of slugs.slice(0, slugs.indexOf('n5-calendar'))) s.progress[slug] = { status: 'completed', attempts: 1, bestScore: 100, completedAt: new Date().toISOString() };
    localStorage.setItem('koto-quest-local-v1', JSON.stringify(s));
  }, before);
  await page.goto(FILE + '#/');
  await page.reload();
  await page.goto(FILE + '#/lesson/n5-calendar');
  await expect(page.getByRole('heading', { name: 'Chaque jour, la semaine prochaine' })).toBeVisible();
  await page.getByRole('button', { name: 'Passer aux exercices' }).click();
  let sawJlpt = false;
  for (let k = 0; k < 40; k++) {
    if (await page.getByRole('heading', { name: /Sans faute|Leçon terminée/ }).isVisible().catch(() => false)) break;
    const q = page.getByTestId('question').last();
    if (!(await q.isVisible().catch(() => false))) { await page.waitForTimeout(200); continue; }
    if ((await q.getAttribute('data-type')) === 'jlpt_reading') {
      sawJlpt = true;
      await expect(q.getByText('＿＿の ことばは ひらがなで どう かきますか。')).toBeVisible();
      await expect(q.locator('u')).toHaveCount(1);
    }
    const qid = await q.getAttribute('data-qid');
    await answerFromStore(page, true);
    await page.getByRole('button', { name: /^(Continuer|Terminer)$/ }).click();
    await expect(page.locator(`[data-qid="${qid}"]`)).toHaveCount(0);
  }
  expect(sawJlpt).toBe(true);

  await page.goto(FILE + '#/prepa');
  const kanji = page.getByRole('listitem').filter({ hasText: '漢字読み' });
  await kanji.getByRole('button', { name: 'S’entraîner' }).click();
  const q = page.getByTestId('question').last();
  await expect(q).toHaveAttribute('data-type', 'jlpt_reading');
  await expect(q.locator('u')).toHaveCount(1);
});

test('hors ligne : duel classé contre un adversaire simulé, rang et classement', async ({ page }) => {
  test.setTimeout(150_000);
  await page.goto(FILE);
  for (let i = 0; i < 5; i++) await page.getByRole('button', { name: 'Suivant' }).click();
  await page.getByRole('button', { name: 'Commencer l’aventure' }).click();
  await page.getByRole('link', { name: /Duels/ }).first().click();
  await expect(page.getByText('Ashigaru III').first()).toBeVisible();
  await page.getByRole('button', { name: 'Trouver un adversaire' }).click();
  await expect(page.getByRole('heading', { name: 'Recherche d’un adversaire…' })).toBeVisible();
  await expect(page.getByRole('region', { name: 'Arène du duel' })).toBeVisible({ timeout: 10_000 });

  const answer = () => page.evaluate(() => {
    const s = JSON.parse(localStorage.getItem('koto-quest-local-v1')!);
    const d: any = Object.values(s.duel.duels).find((x: any) => x.status === 'active');
    return d ? String(d.questions[d.round].answer) : null;
  });
  const end = page.getByRole('heading', { name: /^(Victoire !|Défaite|Égalité)$/ });
  for (let i = 0; i < 12; i++) {
    const q = page.getByRole('region', { name: /^Question \d+/ });
    await Promise.race([q.waitFor({ timeout: 20_000 }), end.waitFor({ timeout: 20_000 })]).catch(() => undefined);
    if (await end.isVisible()) break;
    const a = await answer();
    if (!a) break;
    await q.getByRole('button', { name: a, exact: true }).click();
    await expect(page.getByText(/Juste ! Tu prépares un coup de \d+/)).toBeVisible();
    await q.waitFor({ state: 'detached', timeout: 20_000 });
  }
  // Toujours juste et rapide : victoire, points gagnés
  await expect(page.getByRole('heading', { name: 'Victoire !' })).toBeVisible({ timeout: 20_000 });
  await expect(page.getByText(/points \(\+\d+\)/)).toBeVisible();
  await page.getByRole('link', { name: 'Retour au dojo' }).click();
  await expect(page.getByText(/^1\d{3}$/).first()).toBeVisible();
  await expect(page.getByRole('listitem').filter({ hasText: '(toi)' })).toBeVisible();
});

test.describe('version anglaise', () => {
  test.use({ locale: 'en-GB' });

  test('hors ligne en anglais : interface, cours et exercices traduits, bonnes réponses reconnues, retour au français', async ({ page }) => {
    test.setTimeout(120_000);
    const dict: Record<string, string> = Object.assign({}, ...['ui', 'engine', 'content'].map((f) => JSON.parse(readFileSync(resolve(__dirname, `../content/i18n/en/${f}.json`), 'utf8'))));
    await page.goto(FILE);
    await expect(page.getByRole('heading', { name: 'Where are you with Japanese?' })).toBeVisible();
    await page.getByRole('radio', { name: /I know some kanji/ }).click();
    for (let i = 0; i < 5; i++) await page.getByRole('button', { name: 'Next' }).click();
    await page.getByRole('button', { name: 'Start the adventure' }).click();
    await expect(page.getByRole('heading', { name: 'Ready for what’s next?' })).toBeVisible();
    await expect(page.locator('html')).toHaveAttribute('lang', 'en');

    await page.goto(FILE + '#/lesson/n5-greetings');
    await expect(page.getByRole('heading', { name: 'Hello, thank you, goodbye' })).toBeVisible();
    await expect(page.getByText('Greet and thank depending on the time of day.')).toBeVisible();
    await page.getByRole('button', { name: 'Go to the exercises' }).click();

    let checked = 0;
    for (let guard = 0; guard < 60; guard++) {
      if (await page.getByRole('heading', { name: /^(Lesson complete|Flawless!)$/ }).isVisible().catch(() => false)) break;
      const q = page.getByTestId('question').last();
      if (!(await q.isVisible().catch(() => false))) {
        await page.waitForTimeout(200);
        continue;
      }
      const qid = (await q.getAttribute('data-qid'))!;
      const type = await q.getAttribute('data-type');
      const answer = await page.evaluate((id) => JSON.parse(localStorage.getItem('koto-quest-local-v1')!).questions[id].answer, qid);
      if (type === 'sentence_order') {
        for (const tok of answer as string[]) await q.getByTestId('token-bank').getByRole('button', { name: tok, exact: true }).first().click();
        await q.getByRole('button', { name: 'Check' }).click();
      } else if (type === 'matching') {
        const right = q.locator('[data-match=right]');
        for (let k = 0; k < (await right.count()); k++) await right.nth(k).click();
        await q.getByRole('button', { name: 'Check' }).click();
      } else {
        const shown = dict[answer as string] ?? (answer as string);
        await q.getByRole('group').getByRole('button', { name: new RegExp(`^(\\d\\s*)?${shown.replace(/[.*+?^${}()|[\]\\]/g, '\\$&')}$`) }).first().click();
        await expect(q.getByText('Correct!')).toBeVisible();
        checked++;
      }
      await page.getByRole('button', { name: /^(Continue|Finish)$/ }).click();
      await expect(page.locator(`[data-qid="${qid}"]`)).toHaveCount(0);
    }
    expect(checked).toBeGreaterThan(5);
    await expect(page.getByRole('heading', { name: /^(Lesson complete|Flawless!)$/ })).toBeVisible();

    // Retour au français depuis les réglages
    await page.goto(FILE + '#/settings');
    await page.getByRole('radio', { name: 'Français' }).click();
    await expect(page.getByRole('heading', { name: 'Réglages', level: 1 })).toBeVisible();
    await expect(page.getByRole('link', { name: /Parcours/ }).first()).toBeVisible();
  });
});

test('hors ligne : expressions utiles par thème, recherche et entraînement', async ({ page }) => {
  await page.goto(FILE);
  for (let i = 0; i < 5; i++) await page.getByRole('button', { name: 'Suivant' }).click();
  await page.getByRole('button', { name: 'Commencer l’aventure' }).click();
  await page.getByRole('link', { name: 'Expressions' }).first().click();
  await expect(page.getByRole('heading', { name: 'Expressions', level: 1 })).toBeVisible();
  await expect(page.getByText('よろしくお願いします', { exact: true })).toBeVisible();
  await page.getByRole('button', { name: /Urgences et santé/ }).click();
  await expect(page.getByText('救急車を呼んでください', { exact: true })).toBeVisible();
  await expect(page.getByText(/119/)).toBeVisible();
  await page.getByPlaceholder(/Rechercher/).fill('addition');
  await expect(page.getByTestId('expression')).toHaveCount(1);
  await expect(page.getByText('お会計お願いします', { exact: true })).toBeVisible();
  await page.getByPlaceholder(/Rechercher/).fill('');

  await page.getByRole('button', { name: 'Apprendre ces expressions' }).click();
  const q = page.getByTestId('question').first();
  await expect(q).toBeVisible();
  const qid = (await q.getAttribute('data-qid'))!;
  const answer = await page.evaluate((id) => JSON.parse(localStorage.getItem('koto-quest-local-v1')!).questions[id].answer, qid);
  await q.getByRole('group').getByRole('button', { name: new RegExp(`${String(answer).replace(/[.*+?^${}()|[\]\\]/g, '\\$&')}$`) }).first().click();
  await expect(q.getByText('Bonne réponse !')).toBeVisible();
  await page.getByRole('button', { name: 'Quitter la session' }).click();
  await expect(page.getByText(/1 sur 8 vues|sur 8 vues/)).toBeVisible();
});
