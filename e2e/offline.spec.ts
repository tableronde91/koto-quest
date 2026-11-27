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
  await expect(page.getByText(/1 leçon\(s\) sur 50 disponibles/)).toBeVisible();

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

test('hors ligne : audio fiable (voix chargées en retard, voix installée préférée, dernière demande seule jouée)', async ({ page }) => {
  // Synthèse simulée : la liste des voix n'arrive que plus tard (au signal du test), une voix en ligne est listée avant la voix installée,
  // et le moteur reste « occupé » le temps de lire une phrase.
  await page.addInitScript(() => {
    const w = window as any;
    w.__log = [];
    const voices = [
      { lang: 'ja-JP', name: 'Google 日本語', localService: false, default: false },
      { lang: 'ja-JP', name: 'Kyoko', localService: true, default: false },
    ];
    let loaded = false;
    const listeners: (() => void)[] = [];
    const synth: any = {
      speaking: false,
      pending: false,
      getVoices: () => (loaded ? voices : []),
      addEventListener: (_: string, f: () => void) => listeners.push(f),
      removeEventListener: () => {},
      resume: () => w.__log.push('resume'),
      cancel: () => { synth.speaking = false; w.__log.push('cancel'); },
      speak: (u: any) => {
        w.__log.push({ text: u.text, voice: u.__voice?.name ?? null, at: Date.now() });
        synth.speaking = true;
        setTimeout(() => { synth.speaking = false; u.onend?.(); }, 300);
      },
    };
    // Le navigateur refuse un objet « voix » maison : on mémorise celle qui a été choisie
    Object.defineProperty(SpeechSynthesisUtterance.prototype, 'voice', { set(v) { this.__voice = v; }, get() { return this.__voice ?? null; }, configurable: true });
    Object.defineProperty(window, 'speechSynthesis', { value: synth });
    w.__loadVoices = () => { loaded = true; listeners.forEach((f) => f()); };
  });
  await page.goto(FILE);
  for (let i = 0; i < 5; i++) await page.getByRole('button', { name: 'Suivant' }).click();
  await page.getByRole('button', { name: 'Commencer l’aventure' }).click();
  await page.goto(FILE + '#/lesson/n5-hira-a');
  const listen = page.getByRole('button', { name: 'Écouter あ' });
  await expect(listen).toBeVisible();
  // Trois clics rapprochés pendant que les voix ne sont pas encore là : une seule lecture, avec la voix installée
  await page.evaluate(() => ((window as any).__log = []));
  await listen.click();
  await listen.click();
  await listen.click();
  // Rien n'est lu avec une voix inconnue : on attend la liste des voix
  expect(await page.evaluate(() => (window as any).__log.filter((x: any) => typeof x === 'object').length)).toBe(0);
  await page.evaluate(() => (window as any).__loadVoices());
  await expect.poll(() => page.evaluate(() => (window as any).__log.filter((x: any) => typeof x === 'object').length)).toBe(1);
  await page.waitForTimeout(600);
  const log = await page.evaluate(() => (window as any).__log);
  const spoken = log.filter((x: any) => typeof x === 'object');
  expect(spoken).toHaveLength(1);
  expect(spoken[0].voice).toBe('Kyoko');
  expect(log).toContain('resume');
  // Relance pendant une lecture : arrêt, court délai, puis la nouvelle phrase (jamais avalée)
  await page.evaluate(() => ((window as any).__log = []));
  await listen.click();
  await page.waitForTimeout(50);
  await listen.click();
  await expect.poll(() => page.evaluate(() => (window as any).__log.filter((x: any) => typeof x === 'object').length)).toBe(2);
  const log2 = await page.evaluate(() => (window as any).__log);
  const [a, b] = log2.filter((x: any) => typeof x === 'object');
  expect(b.at - a.at).toBeGreaterThanOrEqual(100);
});

test('hors ligne : phrase complète prononcée après une bonne réponse, exercices ratés repris en fin de séance', async ({ page }) => {
  await page.addInitScript(() => {
    (window as any).__spoken = [];
    Object.defineProperty(window, 'speechSynthesis', {
      value: { speak: (u: SpeechSynthesisUtterance) => (window as any).__spoken.push(u.text), cancel: () => {}, resume: () => {}, speaking: false, pending: false, getVoices: () => [{ lang: 'ja-JP', name: 'Kyoko', localService: true, default: false }], addEventListener: () => {}, removeEventListener: () => {} },
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
  // Les 9 leçons de katakana (46 caractères) avant le gardien
  test.setTimeout(240_000);
  await page.goto(FILE);
  await page.getByRole('radio', { name: /Je lis les hiragana/ }).click();
  for (let i = 0; i < 5; i++) await page.getByRole('button', { name: 'Suivant' }).click();
  await page.getByRole('button', { name: 'Commencer l’aventure' }).click();

  await page.goto(FILE + '#/path');
  await expect(page.getByLabel(/Le Tanuki farceur : Termine l’île/)).toBeVisible();

  for (const slug of ['n5-kata-a', 'n5-kata-ka', 'n5-kata-sa', 'n5-kata-ta', 'n5-kata-na', 'n5-kata-ha', 'n5-kata-ma', 'n5-kata-ya', 'n5-kata-ra']) {
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
  expect(await page.evaluate(() => JSON.parse(localStorage.getItem('koto-quest-local-v1')!).coins)).toBeGreaterThanOrEqual(30);

  await page.goto(FILE + '#/avatar?t=boutique');
  await page.getByRole('group', { name: 'Catégorie' }).getByRole('button', { name: 'Accessoires' }).click();
  // Les succès des leçons sont vérifiés (et récompensés) en arrivant sur la page : on compte les pièces après
  await page.waitForTimeout(1500);
  const coins = await page.evaluate(() => JSON.parse(localStorage.getItem('koto-quest-local-v1')!).coins);
  await page.getByRole('button', { name: 'Acheter Lunettes rondes pour 20 pièces' }).click();
  await expect(page.getByText('Lunettes rondes acheté.')).toBeVisible();
  // Les trophées restent verrouillés tant que le gardien n'est pas vaincu
  await expect(page.getByText('Bats Le Marchand de lanternes')).toBeVisible();
  await page.getByRole('button', { name: 'Équiper' }).click();
  await expect(page.getByText('Équipé')).toBeVisible();
  const saved = await page.evaluate(() => JSON.parse(localStorage.getItem('koto-quest-local-v1')!));
  expect(saved.avatar.accessory).toBe('acc-glasses');
  // − 20 pour l'achat (+ 10 si le succès « Collectionneur » du premier objet est déjà crédité)
  expect([coins - 20, coins - 10]).toContain(saved.coins);

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
  await expect(page.getByRole('heading', { name: /N5 : La Voie du samouraï/ })).toBeVisible();
  await expect(page.getByRole('heading', { name: /Chapitre 1 Le premier pinceau/ })).toBeVisible();
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

  // En japonais : Kana Rush et Kanji Rush, pas Hangeul Rush
  await page.goto(FILE + '#/games');
  await expect(page.getByRole('heading', { name: 'Kana Rush' })).toBeVisible();
  await expect(page.getByRole('heading', { name: 'Kanji Rush' })).toBeVisible();
  await expect(page.getByRole('heading', { name: 'Hangeul Rush' })).toHaveCount(0);

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
  await expect(page.getByRole('heading', { name: /N4 : L’Ombre du ninja/ })).toBeVisible();
  await expect(page.getByRole('heading', { name: /Chapitre 1 L’entraînement de l’ombre/ })).toBeVisible();
  await expect(page.getByText(/Le Tengu pressé ne te laissera aucun répit/)).toBeVisible();
  await expect(page.getByRole('heading', { name: /La forme en て/ })).toBeVisible();
  await page.getByRole('link', { name: /Forme en て : verbes en る/ }).click();
  await expect(page.getByRole('heading', { name: 'Forme en て : verbes en る et irréguliers' })).toBeVisible();
  await page.getByRole('button', { name: 'Passer aux exercices' }).click();
  await answerAll(page, /Sans faute|Leçon terminée/);
  // Le choix du niveau est mémorisé
  await page.goto(FILE + '#/path');
  await expect(page.getByRole('tab', { name: /N4/ })).toHaveAttribute('aria-selected', 'true');
  await expect(page.getByRole('tab', { name: /N4/ })).toContainText('1/39 leçons');
  await expect(page.getByRole('button', { name: /Île 9 : Simulation JLPT N4, examen blanc/ })).toBeVisible();

  // N2 : carte d'été, une leçon de bout en bout, île de l'examen blanc
  await page.getByRole('tab', { name: /N2/ }).click();
  await expect(page.getByRole('heading', { name: /N2 : La Capitale de l’onmyōji/ })).toBeVisible();
  await expect(page.locator('[data-theme-map="summer"]')).toBeVisible();
  await expect(page.getByRole('tab', { name: /N2/ })).toContainText('0/24 leçons');
  await expect(page.getByRole('button', { name: /Île 9 : Simulation JLPT N2, examen blanc/ })).toBeVisible();
  await expect(page.getByText('75 minutes, 40 questions, non officiel')).toBeVisible(); // format officiel abrégé
  await expect(page.getByRole('heading', { name: /Chapitre 1 L’observatoire des présages/ })).toBeVisible();
  await page.getByRole('link', { name: /Du point de vue de…/ }).click();
  await expect(page.getByRole('heading', { name: /Du point de vue de… : 〜からすると・〜から見ると/ })).toBeVisible();
  await page.getByRole('button', { name: 'Passer aux exercices' }).click();
  await answerAll(page, /Sans faute|Leçon terminée/);
  await page.goto(FILE + '#/path');
  await expect(page.getByRole('tab', { name: /N2/ })).toContainText('1/24 leçons');
  // N1 : saga du shōgun, carte de l'aube du Nouvel An
  await page.getByRole('tab', { name: /N1/ }).click();
  await expect(page.getByRole('heading', { name: /N1 : Le Règne du shōgun/ })).toBeVisible();
  await expect(page.locator('[data-theme-map="newyear"]')).toBeVisible();
  await expect(page.getByRole('tab', { name: /N1/ })).toContainText('0/24 leçons');
  await expect(page.getByRole('button', { name: /Île 9 : Simulation JLPT N1, examen blanc/ })).toBeVisible();
  await expect(page.getByText('80 minutes, 35 questions, non officiel')).toBeVisible(); // format officiel abrégé
  await expect(page.getByRole('heading', { name: /Chapitre 1 La cérémonie de succession/ })).toBeVisible();
  await page.getByRole('tab', { name: /N4/ }).click();

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

test('hors ligne : examens blancs N4 à N1 au format officiel, barème en trois parties à partir du N3', async ({ page }) => {
  await page.goto(FILE);
  for (let i = 0; i < 5; i++) await page.getByRole('button', { name: 'Suivant' }).click();
  await page.getByRole('button', { name: 'Commencer l’aventure' }).click();
  await page.goto(FILE + '#/exam/n2-jlpt');
  await expect(page.getByRole('heading', { name: 'Examen blanc JLPT N2 — format officiel (abrégé)' })).toBeVisible();
  await expect(page.getByText(/40 questions en 75 minutes/)).toBeVisible();
  await expect(page.getByText(/réussite à 90, avec au moins 19\/60 dans chacune des trois parties/)).toBeVisible();
  await page.getByRole('button', { name: 'Commencer l’examen' }).click();
  await expect(page.getByText('問題１　漢字読み')).toBeVisible();
  await expect(page.getByTestId('exam-question').locator('u')).toHaveCount(1);
  await page.getByRole('button', { name: 'Rendre ma copie' }).first().click();
  await page.getByRole('alertdialog').getByRole('button', { name: 'Rendre ma copie' }).click();
  await expect(page.getByText('/ 180')).toBeVisible();
  await expect(page.getByRole('heading', { name: 'Pas encore le seuil' })).toBeVisible();
  for (const part of ['言語知識', '読解', '聴解']) await expect(page.getByText(part, { exact: true }).first()).toBeVisible();
  // Au N4, le barème reste en deux parties (langue et lecture sur 120, écoute sur 60), réussite à 90
  await page.goto(FILE + '#/exam/n4-jlpt');
  await expect(page.getByText(/réussite à 90, avec au moins 38\/120 et 19\/60/)).toBeVisible();
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
  // Le tirage des formats est aléatoire : on rejoue la leçon (jusqu'à 3 fois) tant qu'aucune question 漢字読み n'est sortie
  let sawJlpt = false;
  for (let attempt = 0; attempt < 3 && !sawJlpt; attempt++) {
  await page.goto(FILE + '#/lesson/n5-calendar');
  await expect(page.getByRole('heading', { name: 'Chaque jour, la semaine prochaine' })).toBeVisible();
  await page.getByRole('button', { name: 'Passer aux exercices' }).click();
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
  test.setTimeout(300_000);
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
  for (let i = 0; i < 30; i++) {
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
  // Révision des proverbes japonais
  await page.getByRole('button', { name: /Expressions en quatre caractères/ }).click();
  await expect(page.getByText('一期一会', { exact: true })).toBeVisible();
  await page.getByRole('button', { name: /Proverbes/ }).click();
  await expect(page.getByText('猿も木から落ちる', { exact: true })).toBeVisible();
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

test('hors ligne : lecture du jour, tous les chapitres ouverts, progression enregistrée', async ({ page }) => {
  await page.goto(FILE);
  for (let i = 0; i < 5; i++) await page.getByRole('button', { name: 'Suivant' }).click();
  await page.getByRole('button', { name: 'Commencer l’aventure' }).click();
  await page.getByRole('link', { name: 'Lecture' }).first().click();
  await expect(page.getByRole('heading', { name: 'Lecture', level: 1 })).toBeVisible();
  await page.getByRole('button', { name: 'Lire le chapitre du jour' }).click();
  await expect(page.getByTestId('sentence').first()).toContainText('むかしむかし');
  await page.getByRole('radio', { name: 'À la rivière' }).check();
  await page.getByRole('radio', { name: 'Une grosse pêche' }).check();
  await page.getByRole('button', { name: 'Valider mes réponses' }).click();
  await expect(page.getByText('2/2 bonnes réponses')).toBeVisible();
  const stored = await page.evaluate(() => JSON.parse(localStorage.getItem('koto-quest-local-v1')!).reading);
  expect(stored).toHaveLength(1);
  expect(stored[0]).toMatchObject({ chapter: 'momotaro-1', correct: 2 });
  await page.getByRole('link', { name: 'Tous les contes' }).first().click();
  await expect(page.getByText('Lu aujourd’hui')).toBeVisible();
  // Rien n'est verrouillé : chaque chapitre de chaque conte est un lien
  const chapters = page.getByTestId('story').getByRole('listitem');
  expect(await chapters.getByRole('link').count()).toBe(await chapters.count());
  await page.getByTestId('story').last().getByRole('link').last().click();
  await expect(page.getByTestId('reader')).toBeVisible();
  await page.goBack();
  // Le lendemain : on simule une lecture datée d'hier, le chapitre conseillé est le suivant
  await page.evaluate(() => {
    const s = JSON.parse(localStorage.getItem('koto-quest-local-v1')!);
    s.reading[0].dateKey = '2000-01-01';
    localStorage.setItem('koto-quest-local-v1', JSON.stringify(s));
  });
  await page.reload();
  await expect(page.getByText('Conseillé aujourd’hui')).toBeVisible();
  await expect(page.getByRole('heading', { name: /Un garçon dans la pêche/ })).toBeVisible();
});

test('hors ligne : apprendre le coréen (hangeul, saga du hwarang, contes, retour au japonais)', async ({ page }) => {
  await page.goto(FILE);
  await expect(page.getByRole('heading', { name: 'Quelle langue veux-tu apprendre ?' })).toBeVisible();
  await page.getByRole('radio', { name: /Coréen/ }).click();
  await expect(page.getByRole('heading', { name: 'Où en es-tu en coréen ?' })).toBeVisible();
  await page.getByRole('radio', { name: /Je pars de zéro/ }).click();
  await page.getByRole('button', { name: 'Suivant' }).click();
  await expect(page.getByRole('heading', { name: 'Quel niveau TOPIK vises-tu ?' })).toBeVisible();
  await expect(page.getByRole('radio', { name: /TOPIK 1 — débutant/ })).toHaveAttribute('aria-checked', 'true');
  await expect(page.getByRole('radio', { name: /TOPIK 2 — élémentaire/ })).toBeEnabled();
  await expect(page.getByRole('radio', { name: /TOPIK 3 — intermédiaire/ })).toBeEnabled();
  await expect(page.getByRole('radio', { name: /TOPIK 4 — intermédiaire avancé/ })).toBeEnabled();
  await expect(page.getByRole('radio', { name: /TOPIK 5 — avancé/ })).toBeEnabled();
  await expect(page.getByRole('radio', { name: /TOPIK 6 — maîtrise/ })).toBeEnabled();
  for (let i = 0; i < 4; i++) await page.getByRole('button', { name: 'Suivant' }).click();
  await page.getByRole('button', { name: 'Commencer l’aventure' }).click();

  // Première leçon : les voyelles du hangeul
  await page.getByRole('link', { name: 'Commencer la leçon' }).click();
  await expect(page.getByRole('heading', { name: 'Les voyelles ㅏ ㅓ ㅗ ㅜ ㅡ ㅣ' })).toBeVisible();
  // Une lettre coréenne est du hangeul, pas un kana
  await expect(page.locator('#items-title + ul li').first()).toContainText('Hangeul');
  await expect(page.locator('#items-title + ul')).not.toContainText('Kana');
  await page.getByRole('button', { name: 'Passer aux exercices' }).click();
  await answerAll(page, /Sans faute|Leçon terminée/);

  // Parcours : la saga coréenne et son archipel
  await page.goto(FILE + '#/path');
  await expect(page.getByRole('heading', { name: 'TOPIK 1 : La Voie du hwarang' })).toBeVisible();
  await expect(page.getByRole('heading', { name: /Les lettres du roi Sejong/ })).toBeVisible();
  await expect(page.locator('[data-theme-map="korea"]')).toBeVisible();
  await page.getByRole('tab', { name: /TOPIK 2/ }).click();
  await expect(page.getByRole('heading', { name: 'TOPIK 2 : Le Conteur du tigre blanc' })).toBeVisible();
  await expect(page.getByRole('heading', { name: /Le village de Jeonju/ })).toBeVisible();
  await page.getByRole('tab', { name: /TOPIK 3/ }).click();
  await expect(page.getByRole('heading', { name: 'TOPIK 3 : L’Inspecteur royal secret' })).toBeVisible();
  await expect(page.getByRole('heading', { name: /Le marché aux rumeurs/ })).toBeVisible();
  await page.getByRole('tab', { name: /TOPIK 4/ }).click();
  await expect(page.getByRole('heading', { name: 'TOPIK 4 : L’Historien des Annales' })).toBeVisible();
  await page.getByRole('tab', { name: /TOPIK 5/ }).click();
  await expect(page.getByRole('heading', { name: 'TOPIK 5 : Le Chant de la princesse Bari' })).toBeVisible();
  await page.getByRole('tab', { name: /TOPIK 6/ }).click();
  await expect(page.getByRole('heading', { name: 'TOPIK 6 : La Légende de Dangun' })).toBeVisible();
  await page.getByRole('tab', { name: /TOPIK 1/ }).click();

  // Onglet Hangeul
  await page.goto(FILE + '#/characters');
  await expect(page.getByRole('heading', { name: 'Hangeul', level: 1 })).toBeVisible();
  await expect(page.getByRole('tab', { name: /Voyelles/ })).toBeVisible();
  await page.getByRole('tab', { name: /Consonnes/ }).click();
  await expect(page.getByRole('button', { name: /^ㄱ, g \/ k/ })).toBeVisible();

  // Mini-jeux : Hangeul Rush remplace Kanji Rush
  await page.goto(FILE + '#/games');
  await expect(page.getByRole('heading', { name: 'Hangeul Rush' })).toBeVisible();
  await expect(page.getByRole('heading', { name: 'Kanji Rush' })).toHaveCount(0);
  await expect(page.getByRole('heading', { name: 'Kana Rush' })).toHaveCount(0);

  // Succès : ceux du coréen remplacent ceux des kanji
  await page.goto(FILE + '#/achievements');
  await expect(page.getByText('Héritier·e du roi Sejong').first()).toBeVisible();
  await expect(page.getByText('Calligraphe')).toHaveCount(0);

  // Expressions : la révision des proverbes
  await page.goto(FILE + '#/expressions');
  await page.getByRole('button', { name: /Expressions en quatre caractères/ }).click();
  await expect(page.getByText('작심삼일', { exact: true })).toBeVisible();
  await page.getByRole('button', { name: /Proverbes des contes/ }).click();
  await expect(page.getByText('누워서 떡 먹기', { exact: true })).toBeVisible();

  // Lecture : les contes coréens
  await page.goto(FILE + '#/lecture');
  await expect(page.getByText('해님 달님').first()).toBeVisible();
  await expect(page.getByText('선녀와 나무꾼').first()).toBeVisible();
  await expect(page.getByText('춘향전').first()).toBeVisible();
  await expect(page.getByText('홍길동전').first()).toBeVisible();
  await expect(page.getByText('바리공주').first()).toBeVisible();
  await expect(page.getByText('금도끼 은도끼').first()).toBeVisible();
  await expect(page.getByText('콩쥐팥쥐').first()).toBeVisible();
  await expect(page.getByText('심청전').first()).toBeVisible();
  await expect(page.getByText('단군 신화').first()).toBeVisible();
  await expect(page.getByText('ももたろう')).toHaveCount(0);

  // Retour au japonais : le parcours N5 et les contes japonais reviennent, la progression coréenne reste
  // La langue étudiée ne se change plus que dans les réglages
  await page.goto(FILE + '#/path');
  await expect(page.getByTestId('study-language')).toHaveCount(0);
  await page.goto(FILE + '#/settings');
  await page.getByTestId('study-language').getByRole('radio', { name: /日本語/ }).click();
  await expect(page.getByTestId('study-language').getByRole('radio', { name: /日本語/ })).toHaveAttribute('aria-checked', 'true');
  await page.goto(FILE + '#/path');
  await expect(page.getByRole('heading', { name: /N5 : La Voie du samouraï/ })).toBeVisible();
  // Contes japonais du N5 au N1, dont les nouveaux
  await page.goto(FILE + '#/lecture');
  await expect(page.getByText('はなさかじいさん').first()).toBeVisible();
  await expect(page.getByText('Hōichi sans oreilles').first()).toBeVisible();
  await expect(page.getByText('La Jeune Fille au bol').first()).toBeVisible();
  await expect(page.getByText('해님 달님')).toHaveCount(0);
  await page.goto(FILE + '#/settings');
  await page.getByTestId('study-language').getByRole('radio', { name: /한국어/ }).click();
  await expect(page.getByTestId('study-language').getByRole('radio', { name: /한국어/ })).toHaveAttribute('aria-checked', 'true');
  await page.goto(FILE + '#/path');
  await expect(page.getByRole('heading', { name: 'TOPIK 1 : La Voie du hwarang' })).toBeVisible();
  await expect(page.getByText('1/4').first()).toBeVisible();
});

test('hors ligne : apprendre l’anglais pour le TOEIC (saga de Merlin, expressions, contes, examen sur 990)', async ({ page }) => {
  await page.goto(FILE);
  await page.getByRole('radio', { name: /Anglais/ }).click();
  await expect(page.getByRole('heading', { name: 'Où en es-tu en anglais ?' })).toBeVisible();
  await page.getByRole('radio', { name: /Je pars de zéro ou presque/ }).click();
  await page.getByRole('button', { name: 'Suivant' }).click();
  await expect(page.getByRole('heading', { name: 'Quel niveau TOEIC vises-tu ?' })).toBeVisible();
  await expect(page.getByRole('radio', { name: /A1 — découverte/ })).toHaveAttribute('aria-checked', 'true');
  await expect(page.getByRole('radio', { name: /C1 — autonome/ })).toBeEnabled();
  for (let i = 0; i < 3; i++) await page.getByRole('button', { name: 'Suivant' }).click();
  // Pas de kana ni de kanji parmi les difficultés proposées
  await expect(page.getByRole('button', { name: 'Les kanji' })).toHaveCount(0);
  await page.getByRole('button', { name: 'Suivant' }).click();
  await page.getByRole('button', { name: 'Commencer l’aventure' }).click();

  // Première leçon : saluer
  await page.getByRole('link', { name: 'Commencer la leçon' }).click();
  await expect(page.getByRole('heading', { name: 'Bonjour ! Saluer et prendre congé' })).toBeVisible();
  await page.getByRole('button', { name: 'Passer aux exercices' }).click();
  await answerAll(page, /Sans faute|Leçon terminée/);

  // Parcours : la saga de Merlin dans le royaume d'Albion
  await page.goto(FILE + '#/path');
  await expect(page.getByRole('heading', { name: 'A1 : L’Épée dans le bureau' })).toBeVisible();
  await expect(page.getByRole('heading', { name: /Hello, London/ })).toBeVisible();
  await expect(page.locator('[data-theme-map="albion"]')).toBeVisible();

  // Pas d'onglet d'écriture : la page Caractères mène aux expressions
  await page.goto(FILE + '#/characters');
  await expect(page).toHaveURL(/#\/expressions/);
  await page.getByRole('button', { name: /Idiomes imagés/ }).click();
  await expect(page.getByText('a piece of cake', { exact: true })).toBeVisible();

  // Mini-jeux : Word Rush
  await page.goto(FILE + '#/games');
  await expect(page.getByRole('heading', { name: 'Word Rush' })).toBeVisible();
  await expect(page.getByRole('heading', { name: 'Kana Rush' })).toHaveCount(0);

  // Lecture : les contes anglais
  await page.goto(FILE + '#/lecture');
  await expect(page.getByText('Goldilocks and the Three Bears').first()).toBeVisible();
  await expect(page.getByText('The Sword in the Stone').first()).toBeVisible();
  await expect(page.getByText('ももたろう')).toHaveCount(0);

  // Atelier TOEIC et examen blanc noté sur 990
  await page.goto(FILE + '#/prepa');
  await expect(page.getByRole('heading', { name: 'Atelier TOEIC' })).toBeVisible();
  await page.goto(FILE + '#/exam/a1-toeic');
  await expect(page.getByRole('heading', { name: 'Examen blanc TOEIC A1 — format officiel (abrégé)' })).toBeVisible();
  await expect(page.getByText('Barème du TOEIC')).toBeVisible();
  await page.getByRole('button', { name: 'Commencer l’examen' }).click();
  // Partie 1 : une photo, quatre phrases lues (pas de texte ni d'écoute séparée des réponses)
  await expect(page.getByText('Part 1 — Photographs').first()).toBeVisible();
  await expect(page.getByTestId('exam-photo')).toBeVisible();
  await expect(page.getByRole('radio', { name: 'Réponse 4' })).toBeVisible();
  await expect(page.getByRole('button', { name: /Écouter la réponse/ })).toHaveCount(0);
  await page.getByRole('button', { name: 'Suivante' }).click();
  await page.getByRole('button', { name: 'Suivante' }).click();
  await expect(page.getByText('Part 2 — Question-Response').first()).toBeVisible();
});

test('hors ligne : apprendre le chinois pour le HSK (pinyin, saga du messager, hanzi, fables, examen sur 200)', async ({ page }) => {
  await page.goto(FILE);
  await page.getByRole('radio', { name: /Chinois/ }).click();
  await expect(page.getByRole('heading', { name: 'Où en es-tu en chinois ?' })).toBeVisible();
  await page.getByRole('radio', { name: /Je pars de zéro/ }).click();
  await page.getByRole('button', { name: 'Suivant' }).click();
  await expect(page.getByRole('heading', { name: 'Quel niveau HSK vises-tu ?' })).toBeVisible();
  await expect(page.getByRole('radio', { name: /HSK 1 — débutant/ })).toHaveAttribute('aria-checked', 'true');
  for (let i = 0; i < 3; i++) await page.getByRole('button', { name: 'Suivant' }).click();
  // Pas de kana parmi les difficultés proposées, mais les caractères (hanzi)
  await expect(page.getByRole('button', { name: 'Les kana' })).toHaveCount(0);
  await expect(page.getByRole('button', { name: 'Les caractères (hanzi)' })).toBeVisible();
  await page.getByRole('button', { name: 'Suivant' }).click();
  await page.getByRole('button', { name: 'Commencer l’aventure' }).click();

  // Première leçon : le pinyin et les quatre tons, le pinyin au-dessus des caractères
  await page.getByRole('link', { name: 'Commencer la leçon' }).click();
  await expect(page.getByRole('heading', { name: 'Le pinyin et les quatre tons' })).toBeVisible();
  await expect(page.locator('ruby[lang="zh"]').filter({ hasText: 'bā' }).first()).toBeVisible();
  // Les caractères prennent les formes du chinois simplifié dans toute l'appli (polices, voir index.css)
  await expect(page.locator('html')).toHaveAttribute('data-study', 'zh');
  await page.getByRole('button', { name: 'Passer aux exercices' }).click();
  await answerAll(page, /Sans faute|Leçon terminée/);

  // Parcours : la saga du messager dans la plaine du Fleuve jaune
  await page.goto(FILE + '#/path');
  await expect(page.getByRole('heading', { name: 'HSK 1 : le messager des Royaumes' })).toBeVisible();
  await expect(page.locator('[data-theme-map="china"]')).toBeVisible();

  // Onglet Hanzi : caractères du HSK 1, lus en pinyin
  await page.goto(FILE + '#/characters');
  await expect(page.getByText('人', { exact: true }).first()).toBeVisible();

  // Mini-jeux : Hanzi Rush
  await page.goto(FILE + '#/games');
  await expect(page.getByRole('heading', { name: 'Hanzi Rush' })).toBeVisible();
  await expect(page.getByRole('heading', { name: 'Kana Rush' })).toHaveCount(0);

  // Lecture : les fables des Royaumes combattants
  await page.goto(FILE + '#/lecture');
  await expect(page.getByText('Le paysan qui attendait le lièvre').first()).toBeVisible();
  await expect(page.getByText('ももたろう')).toHaveCount(0);

  // Atelier HSK et examen blanc noté sur 200
  await page.goto(FILE + '#/prepa');
  await expect(page.getByRole('heading', { name: 'Atelier HSK' })).toBeVisible();
  await page.goto(FILE + '#/exam/hsk1-official');
  await expect(page.getByRole('heading', { name: 'Examen blanc HSK 1 — format officiel' })).toBeVisible();
  await expect(page.getByText('Tout en chinois')).toBeVisible();
  await page.getByRole('button', { name: 'Commencer l’examen' }).click();
  await expect(page.getByText('听力 第一部分（1～5）').first()).toBeVisible();

  // HSK 2 : la saga du général Sun et son examen de 55 minutes
  await page.goto(FILE + '#/path');
  await page.getByRole('tab', { name: /HSK 2/ }).click();
  await expect(page.getByRole('heading', { name: 'HSK 2 : l’art de la guerre' })).toBeVisible();
  await page.goto(FILE + '#/exam/hsk2-official');
  await expect(page.getByRole('heading', { name: 'Examen blanc HSK 2 — format officiel' })).toBeVisible();
  await expect(page.getByText(/60 questions en 55 minutes/)).toBeVisible();

  // HSK 3 : les Cent Écoles, examen avec écriture (书写) sur 300 points
  await page.goto(FILE + '#/path');
  await page.getByRole('tab', { name: /HSK 3/ }).click();
  await expect(page.getByRole('heading', { name: 'HSK 3 : les Cent Écoles' })).toBeVisible();
  await page.goto(FILE + '#/exam/hsk3-official');
  await expect(page.getByRole('heading', { name: 'Examen blanc HSK 3 — format officiel' })).toBeVisible();
  await expect(page.getByText(/80 questions en 90 minutes/)).toBeVisible();
  await page.getByRole('button', { name: 'Commencer l’examen' }).click();
  await expect(page.getByText('听力 第一部分（1～10）').first()).toBeVisible();

  // HSK 4 : l'empire unifié, 100 questions en 100 minutes
  await page.goto(FILE + '#/path');
  await page.getByRole('tab', { name: /HSK 4/ }).click();
  await expect(page.getByRole('heading', { name: 'HSK 4 : l’empire unifié' })).toBeVisible();
  await page.goto(FILE + '#/exam/hsk4-official');
  await expect(page.getByRole('heading', { name: 'Examen blanc HSK 4 — format officiel' })).toBeVisible();
  await expect(page.getByText(/100 questions en 100 minutes/)).toBeVisible();

  // HSK 5 : la quête de l'immortalité, 100 questions en 120 minutes
  await page.goto(FILE + '#/path');
  await page.getByRole('tab', { name: /HSK 5/ }).click();
  await expect(page.getByRole('heading', { name: 'HSK 5 : la quête de l’immortalité' })).toBeVisible();
  await page.goto(FILE + '#/exam/hsk5-official');
  await expect(page.getByRole('heading', { name: 'Examen blanc HSK 5 — format officiel' })).toBeVisible();
  await expect(page.getByText(/100 questions en 120 minutes/)).toBeVisible();

  // HSK 6 : la route de la soie, 103 questions en 135 minutes
  await page.goto(FILE + '#/path');
  await page.getByRole('tab', { name: /HSK 6/ }).click();
  await expect(page.getByRole('heading', { name: 'HSK 6 : la route de la soie' })).toBeVisible();
  await page.goto(FILE + '#/exam/hsk6-official');
  await expect(page.getByRole('heading', { name: 'Examen blanc HSK 6 — format officiel' })).toBeVisible();
  await expect(page.getByText(/103 questions en 135 minutes/)).toBeVisible();
});

test('hors ligne : apprendre l’espagnol pour le DELE (saga de Don Quichotte, expressions, contes, examen sur 100)', async ({ page }) => {
  await page.goto(FILE);
  await page.getByRole('radio', { name: /Espagnol/ }).click();
  await expect(page.getByRole('heading', { name: 'Où en es-tu en espagnol ?' })).toBeVisible();
  await page.getByRole('radio', { name: /Je pars de zéro ou presque/ }).click();
  await page.getByRole('button', { name: 'Suivant' }).click();
  await expect(page.getByRole('heading', { name: 'Quel niveau DELE vises-tu ?' })).toBeVisible();
  await expect(page.getByRole('radio', { name: /DELE A1 — découverte/ })).toHaveAttribute('aria-checked', 'true');
  for (let i = 0; i < 3; i++) await page.getByRole('button', { name: 'Suivant' }).click();
  // Pas de kana ni de kanji parmi les difficultés proposées
  await expect(page.getByRole('button', { name: 'Les kanji' })).toHaveCount(0);
  await page.getByRole('button', { name: 'Suivant' }).click();
  await page.getByRole('button', { name: 'Commencer l’aventure' }).click();

  // Première leçon : saluer
  await page.getByRole('link', { name: 'Commencer la leçon' }).click();
  await expect(page.getByRole('heading', { name: '¡Hola! Saluer et prendre congé' })).toBeVisible();
  await page.getByRole('button', { name: 'Passer aux exercices' }).click();
  await answerAll(page, /Sans faute|Leçon terminée/);

  // Parcours : la saga de Don Quichotte sur les chemins de la Manche, sans japonais
  await page.goto(FILE + '#/path');
  await expect(page.getByRole('heading', { name: 'DELE A1 : Le chevalier de la Manche' })).toBeVisible();
  await expect(page.locator('[data-theme-map="spain"]')).toBeVisible();
  await expect(page.getByText(/[぀-ヿ一-鿿]/)).toHaveCount(0);

  // Pas d'onglet d'écriture : la page Caractères mène aux expressions
  await page.goto(FILE + '#/characters');
  await expect(page).toHaveURL(/#\/expressions/);
  await page.getByRole('button', { name: /Au quotidien/ }).click();
  await expect(page.getByText('¡Vale!', { exact: true })).toBeVisible();

  // Mini-jeux : Word Rush
  await page.goto(FILE + '#/games');
  await expect(page.getByRole('heading', { name: 'Word Rush' })).toBeVisible();
  await expect(page.getByRole('heading', { name: 'Kana Rush' })).toHaveCount(0);

  // Lecture : les contes espagnols
  await page.goto(FILE + '#/lecture');
  await expect(page.getByText('El medio pollito').first()).toBeVisible();
  await expect(page.getByText('Los molinos de viento').first()).toBeVisible();
  await expect(page.getByText('Juan sin Miedo').first()).toBeVisible();
  await expect(page.getByText('El gallo de Santo Domingo').first()).toBeVisible();
  await expect(page.getByText('La leyenda de El Dorado').first()).toBeVisible();
  await expect(page.getByText('Don Illán, el mago de Toledo').first()).toBeVisible();
  await expect(page.getByText('La tortuga gigante').first()).toBeVisible();
  await expect(page.getByText('Goldilocks and the Three Bears')).toHaveCount(0);

  // Atelier DELE et examen blanc noté sur 100
  await page.goto(FILE + '#/prepa');
  await expect(page.getByRole('heading', { name: 'Atelier DELE' })).toBeVisible();
  await page.goto(FILE + '#/exam/delea2-official');
  await expect(page.getByRole('heading', { name: 'Examen blanc DELE A2 — format officiel' })).toBeVisible();
  await expect(page.getByText(/60 questions en 110 minutes/)).toBeVisible();
  await page.goto(FILE + '#/exam/deleb1-official');
  await expect(page.getByRole('heading', { name: 'Examen blanc DELE B1 — format officiel' })).toBeVisible();
  await expect(page.getByText(/65 questions en 130 minutes/)).toBeVisible();
  await page.goto(FILE + '#/exam/deleb2-official');
  await expect(page.getByRole('heading', { name: 'Examen blanc DELE B2 — format officiel' })).toBeVisible();
  await expect(page.getByText(/71 questions en 150 minutes/)).toBeVisible();
  await page.goto(FILE + '#/exam/delec1-official');
  await expect(page.getByRole('heading', { name: 'Examen blanc DELE C1 — format officiel' })).toBeVisible();
  await expect(page.getByText(/75 questions en 170 minutes/)).toBeVisible();
  await page.goto(FILE + '#/exam/delec2-official');
  await expect(page.getByRole('heading', { name: 'Examen blanc DELE C2 — format officiel' })).toBeVisible();
  await expect(page.getByText(/80 questions en 190 minutes/)).toBeVisible();
  await page.goto(FILE + '#/exam/delea1-official');
  await expect(page.getByRole('heading', { name: 'Examen blanc DELE A1 — format officiel' })).toBeVisible();
  await expect(page.getByText(/55 questions en 90 minutes/)).toBeVisible();
  await expect(page.getByText('Barème du DELE')).toBeVisible();
  await page.getByRole('button', { name: 'Commencer l’examen' }).click();
  await expect(page.getByText('Comprensión de lectura — Tarea 1').first()).toBeVisible();
});

test('hors ligne : apprendre l’allemand pour le Goethe-Zertifikat (saga des frères Grimm, expressions, contes, examen sur 100)', async ({ page }) => {
  await page.goto(FILE);
  await page.getByRole('radio', { name: /Allemand/ }).click();
  await expect(page.getByRole('heading', { name: 'Où en es-tu en allemand ?' })).toBeVisible();
  await page.getByRole('radio', { name: /Je pars de zéro ou presque/ }).click();
  await page.getByRole('button', { name: 'Suivant' }).click();
  await expect(page.getByRole('heading', { name: 'Quel niveau Goethe vises-tu ?' })).toBeVisible();
  await expect(page.getByRole('radio', { name: /Goethe A1 — découverte/ })).toHaveAttribute('aria-checked', 'true');
  // Les niveaux suivants sont annoncés mais pas encore ouverts
  await expect(page.getByRole('radio', { name: /Goethe C2 — maîtrise/ })).toBeDisabled();
  await expect(page.getByRole('radio', { name: /Goethe C1 — autonome/ })).toBeEnabled();
  for (let i = 0; i < 3; i++) await page.getByRole('button', { name: 'Suivant' }).click();
  await expect(page.getByRole('button', { name: 'Les kanji' })).toHaveCount(0);
  await page.getByRole('button', { name: 'Suivant' }).click();
  await page.getByRole('button', { name: 'Commencer l’aventure' }).click();

  // Première leçon : saluer
  await page.getByRole('link', { name: 'Commencer la leçon' }).click();
  await expect(page.getByRole('heading', { name: 'Hallo! Saluer et prendre congé' })).toBeVisible();
  await page.getByRole('button', { name: 'Passer aux exercices' }).click();
  await answerAll(page, /Sans faute|Leçon terminée/);

  // Parcours : la Route des contes, sans japonais ni autre langue
  await page.goto(FILE + '#/path');
  await expect(page.getByRole('heading', { name: 'Goethe A1 : La Route des contes' })).toBeVisible();
  await expect(page.locator('[data-theme-map="germany"]')).toBeVisible();
  await expect(page.getByText(/[぀-ヿ一-鿿]/)).toHaveCount(0);
  await expect(page.getByText('Le Rumpelstilzchen').first()).toBeVisible();

  // Pas d'onglet d'écriture : la page Caractères mène aux expressions
  await page.goto(FILE + '#/characters');
  await expect(page).toHaveURL(/#\/expressions/);
  await page.getByRole('button', { name: /Au quotidien/ }).click();
  await expect(page.getByText('Genau!', { exact: true })).toBeVisible();

  // Mini-jeux : Word Rush
  await page.goto(FILE + '#/games');
  await expect(page.getByRole('heading', { name: 'Word Rush' })).toBeVisible();
  await expect(page.getByRole('heading', { name: 'Kana Rush' })).toHaveCount(0);

  // Lecture : les contes des frères Grimm
  await page.goto(FILE + '#/lecture');
  await expect(page.getByText('Die Bremer Stadtmusikanten').first()).toBeVisible();
  await expect(page.getByText('Der süße Brei').first()).toBeVisible();
  await expect(page.getByText('Die Sterntaler').first()).toBeVisible();
  await expect(page.getByText('Der Froschkönig').first()).toBeVisible();
  await expect(page.getByText('Der Zauberlehrling').first()).toBeVisible();
  await expect(page.getByText('Der Erlkönig').first()).toBeVisible();
  await expect(page.getByText('Siegfried und der Drache').first()).toBeVisible();
  await expect(page.getByText('El medio pollito')).toHaveCount(0);

  // Atelier Goethe et examen blanc noté sur 100
  await page.goto(FILE + '#/prepa');
  await expect(page.getByRole('heading', { name: 'Atelier Goethe' })).toBeVisible();
  await page.goto(FILE + '#/path');
  await page.getByRole('tab', { name: /Goethe A2/ }).click();
  await expect(page.getByRole('heading', { name: 'Goethe A2 : Du Rhin à la Forêt-Noire' })).toBeVisible();
  await expect(page.getByText('Le Roi Grenouille').first()).toBeVisible();
  await page.goto(FILE + '#/exam/goethea2-official');
  await expect(page.getByRole('heading', { name: 'Examen blanc Goethe-Zertifikat A2 — format officiel' })).toBeVisible();
  await expect(page.getByText(/45 questions en 90 minutes/)).toBeVisible();
  await page.goto(FILE + '#/exam/goetheb1-official');
  await expect(page.getByText(/65 questions en 165 minutes/)).toBeVisible();
  await expect(page.getByText(/se valide séparément à 60 points/)).toBeVisible();
  await page.goto(FILE + '#/exam/goetheb2-official');
  await expect(page.getByRole('heading', { name: 'Examen blanc Goethe-Zertifikat B2 — format officiel' })).toBeVisible();
  await expect(page.getByText(/65 questions en 180 minutes/)).toBeVisible();
  await page.goto(FILE + '#/exam/goethec1-official');
  await expect(page.getByRole('heading', { name: 'Examen blanc Goethe-Zertifikat C1 — format officiel' })).toBeVisible();
  await page.goto(FILE + '#/exam/goethea1-official');
  await expect(page.getByRole('heading', { name: 'Examen blanc Goethe-Zertifikat A1 — format officiel' })).toBeVisible();
  await expect(page.getByText(/35 questions en 65 minutes/)).toBeVisible();
  await expect(page.getByText('Barème du Goethe-Zertifikat')).toBeVisible();
  await page.getByRole('button', { name: 'Commencer l’examen' }).click();
  await expect(page.getByText('Hören — Teil 1').first()).toBeVisible();
});
