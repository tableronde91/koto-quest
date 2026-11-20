import type { ReactNode } from 'react';
import { Link, useLocation } from 'react-router';
import site from '../../../../content/legal/site.json';
import { LOCAL } from '../api/client';
import { DATE_LOCALE, T, locale } from '../i18n';

/**
 * Pages légales : mentions légales, confidentialité, cookies, conditions d'utilisation.
 * Les textes longs sont rédigés dans chaque langue (et non passés par le dictionnaire).
 * Les informations de l'éditeur viennent de content/legal/site.json.
 */

type Block = { h: string; p?: ReactNode[]; list?: ReactNode[]; table?: { head: string[]; rows: ReactNode[][] } };

const E = site.editor;
const en = locale === 'en';
const contact = E.email ? <a href={`mailto:${E.email}`}>{E.email}</a> : null;
const updated = new Date(site.updatedAt).toLocaleDateString(DATE_LOCALE, { day: 'numeric', month: 'long', year: 'numeric' });
const ext = (href: string, label?: string) => (
  <a href={href} target="_blank" rel="noopener noreferrer">
    {label ?? href.replace(/^https?:\/\//, '')}
  </a>
);
/** Lignes « libellé : valeur », sans les valeurs vides. */
const lines = (rows: [string, ReactNode][]) => rows.filter(([, v]) => v !== '' && v !== null && v !== undefined).map(([k, v]) => <><strong>{k}</strong> {v}</>);

export const LEGAL_PAGES = [
  { path: '/mentions-legales', label: () => T('Mentions légales') },
  { path: '/confidentialite', label: () => T('Confidentialité') },
  { path: '/cookies', label: () => T('Cookies') },
  { path: '/conditions', label: () => T('Conditions d’utilisation') },
] as const;

// ───────────────────────── Mentions légales ─────────────────────────

function notice(): Block[] {
  if (en)
    return [
      {
        h: 'Publisher',
        list: lines([
          ['Publisher:', `${E.owner}, sole trader (EI)`],
          ['Trading name:', E.name],
          ['Status:', E.status.en],
          ['Business address:', E.address],
          ['SIREN:', E.siren],
          ['SIRET:', E.siret],
          ['Activity code (NAF):', E.naf.en],
          ['Registration:', E.register.en],
          ['VAT:', E.vat.en],
          ['Publication director:', E.director],
          ['Contact:', contact],
          ['Phone:', E.phone],
        ]),
      },
      {
        h: 'Hosting',
        list: [
          <><strong>Website and application:</strong> {site.host.name}, {site.host.address}, {ext(site.host.website)}</>,
          <><strong>Database:</strong> {site.database.name}, servers in {site.database.region.split(' / ')[1] ?? site.database.region}, {ext(site.database.website)}</>,
          <><strong>Domain name:</strong> {site.domain.name}, {site.domain.address}, {site.domain.phone}, {ext(site.domain.website)}</>,
        ],
      },
      {
        h: 'Intellectual property',
        p: [
          `The ${site.siteName} name, design, illustrations, characters, lessons, exercises and texts are the property of ${E.owner} (${E.name}), unless stated otherwise. Any reproduction or reuse without permission is prohibited.`,
          'Fonts: Atkinson Hyperlegible (Braille Institute of America) and Zen Maru Gothic (Yoshimichi Ohira), both under the SIL Open Font License 1.1.',
          'JLPT (Japanese-Language Proficiency Test) is run by the Japan Foundation and Japan Educational Exchanges and Services. Koto Quest is not affiliated with them: its mock exams and lists are unofficial and do not guarantee any result.',
        ],
      },
    ];
  return [
    {
      h: 'Éditeur du site',
      list: lines([
        ['Éditeur :', `${E.owner}, entrepreneur individuel (EI)`],
        ['Nom commercial :', E.name],
        ['Statut :', E.status.fr],
        ['Adresse professionnelle :', E.address],
        ['SIREN :', E.siren],
        ['SIRET :', E.siret],
        ['Code NAF :', E.naf.fr],
        ['Immatriculation :', E.register.fr],
        ['TVA :', E.vat.fr],
        ['Directeur de la publication :', E.director],
        ['Contact :', contact],
        ['Téléphone :', E.phone],
      ]),
    },
    {
      h: 'Hébergement',
      list: [
        <><strong>Site et application :</strong> {site.host.name}, {site.host.address}, {ext(site.host.website)}</>,
        <><strong>Base de données :</strong> {site.database.name}, serveurs situés à {site.database.region.split(' / ')[0]}, {ext(site.database.website)}</>,
        <><strong>Nom de domaine :</strong> {site.domain.name}, {site.domain.address}, {site.domain.phone}, {ext(site.domain.website)}</>,
      ],
    },
    {
      h: 'Propriété intellectuelle',
      p: [
        `Le nom ${site.siteName}, le design, les illustrations, les personnages, les leçons, les exercices et les textes sont la propriété de ${E.owner} (${E.name}), sauf mention contraire. Toute reproduction ou réutilisation sans autorisation est interdite.`,
        'Polices de caractères : Atkinson Hyperlegible (Braille Institute of America) et Zen Maru Gothic (Yoshimichi Ohira), sous licence SIL Open Font License 1.1.',
        'Le JLPT (Japanese-Language Proficiency Test) est organisé par la Japan Foundation et Japan Educational Exchanges and Services. Koto Quest n’est pas affilié à ces organismes : ses examens blancs et ses listes ne sont pas officiels et ne garantissent aucun résultat.',
      ],
    },
  ];
}

// ───────────────────────── Confidentialité ─────────────────────────

function privacy(): Block[] {
  const who = `${E.owner} (${E.name})`;
  if (en)
    return [
      {
        h: 'Who is responsible?',
        p: [
          <>The data controller is {who}{E.address ? `, ${E.address}` : ''}. For any question about your data or to exercise your rights: {contact ?? 'see the legal notice'}.</>,
          'Koto Quest only collects what is needed to run the learning service. No advertising, no audience-measurement tools, no sale or rental of data, no commercial profiling.',
        ],
      },
      {
        h: 'What data, why, and for how long?',
        table: {
          head: ['Data', 'Purpose', 'Legal basis', 'Retention'],
          rows: [
            ['Email address, username, password (stored only as an irreversible hash)', 'Create and secure your account, log in, reset a forgotten password', 'Performance of the service (contract)', 'As long as the account exists; deleted after 3 years without a visit'],
            ['Learning data: lessons, answers, reviews, scores, XP, coins, achievements, exams, mini-games, character', 'Run the course, spaced repetition, progress tracking', 'Performance of the service', 'As long as the account exists'],
            ['Duels and friends: duellist profile and code, ranking points, wins/losses, duel history, friend list and requests, last time online', 'Online duels, leaderboard, friends and challenges between players', 'Performance of the service', 'As long as the account exists'],
            ['Preferences: level, goals, exam date, language, theme, time zone', 'Adapt the programme and display', 'Performance of the service', 'As long as the account exists'],
            ['Login sessions (session identifier, browser type, dates)', 'Keep you logged in securely', 'Performance of the service', '30 days, then deleted'],
            ['Notification subscription and reminder settings', 'Send review challenges during the day', 'Your consent (can be withdrawn at any time)', 'Until you turn reminders off or delete the account'],
            ['IP address and technical logs', 'Security, anti-abuse protection, troubleshooting', 'Legitimate interest (service security)', 'A few minutes for anti-abuse counters; host’s technical logs for a limited period'],
            ['Date of last visit', 'Delete inactive accounts', 'Legitimate interest (data minimisation)', 'Updated once a day'],
          ],
        },
      },
      {
        h: 'What other players can see',
        p: ['In duels and on the leaderboard, other players can see your username, character, rank, ranking points, number of wins and your duellist code. Your friends also see whether you are online (or when you were last seen) and the record of your duels together; you can remove a friend at any time. Your email address is never shown. Choose a username that does not reveal your identity if you prefer to stay discreet.'],
      },
      {
        h: 'Recipients and processors',
        list: [
          <><strong>{site.host.name}</strong> (hosting of the application, United States). Transfers to the United States are covered by the EU–US Data Privacy Framework, under which Render is certified.</>,
          <><strong>{site.database.name}</strong> (database hosting, servers in Frankfurt, European Union).</>,
          <><strong>IONOS</strong> (domain name and, where applicable, sending of emails such as password resets).</>,
          'Browser push services (Google, Mozilla, Apple…), only if you turn on notifications: they relay an encrypted message to your device.',
          'Read-aloud: Japanese is read by your browser’s speech synthesis. Depending on the browser, it may use an online service from its publisher (for example Google for Chrome); only the Japanese text to be read is concerned.',
        ],
      },
      {
        h: 'Security',
        p: ['HTTPS connection, passwords hashed with bcrypt, session cookie inaccessible to scripts (httpOnly), limits on login attempts per account and per address, data access restricted to the service.'],
      },
      {
        h: 'Your rights',
        p: [
          'Under the GDPR and the French Data Protection Act, you have the right to access, rectify, erase and port your data, to restrict or object to its processing, to withdraw your consent at any time, and to give instructions about your data after your death.',
          <>Directly in the app: <Link to="/settings">Settings</Link> → “Download my data” (export) and “Delete my account” (immediate, permanent erasure). Your username and goals can be edited in your <Link to="/profile">Profile</Link>, other preferences in Settings. For any other request: {contact ?? 'see the legal notice'}. We reply within one month.</>,
          <>If you believe your rights are not respected, you can lodge a complaint with the CNIL ({ext('https://www.cnil.fr/fr/plaintes')}).</>,
        ],
      },
      {
        h: 'Minors',
        p: ['Koto Quest is open to all learners. Under 15, the agreement of a parent or legal guardian is required to create an account and to turn on notifications.'],
      },
      {
        h: 'Offline version',
        p: ['The offline version (single HTML file) sends no data: your progress stays in your browser’s local storage, on your device.'],
      },
      { h: 'Changes', p: ['This policy may change; the date of the last update is shown at the top of the page.'] },
    ];
  return [
    {
      h: 'Qui est responsable ?',
      p: [
        <>Le responsable du traitement est {who}{E.address ? `, ${E.address}` : ''}. Pour toute question sur vos données ou pour exercer vos droits : {contact ?? 'voir les mentions légales'}.</>,
        'Koto Quest ne collecte que ce qui est nécessaire au service d’apprentissage. Pas de publicité, pas d’outil de mesure d’audience, ni vente ni location de données, pas de profilage commercial.',
      ],
    },
    {
      h: 'Quelles données, pourquoi, combien de temps ?',
      table: {
        head: ['Données', 'Finalité', 'Base légale', 'Conservation'],
        rows: [
          ['Adresse e-mail, pseudo, mot de passe (conservé uniquement sous forme d’empreinte irréversible)', 'Créer et sécuriser le compte, se connecter, réinitialiser un mot de passe oublié', 'Exécution du service (contrat)', 'Tant que le compte existe ; suppression après 3 ans sans visite'],
          ['Données d’apprentissage : leçons, réponses, révisions, scores, XP, pièces, succès, examens, mini-jeux, personnage', 'Faire fonctionner le cours, la répétition espacée, le suivi des progrès', 'Exécution du service', 'Tant que le compte existe'],
          ['Duels et amis : profil et code de duelliste, points de classement, victoires/défaites, historique, liste d’amis et demandes, dernière présence en ligne', 'Duels en ligne, classement, amis et défis entre joueurs', 'Exécution du service', 'Tant que le compte existe'],
          ['Préférences : niveau, objectifs, date d’examen, langue, thème, fuseau horaire', 'Adapter le programme et l’affichage', 'Exécution du service', 'Tant que le compte existe'],
          ['Sessions de connexion (identifiant de session, type de navigateur, dates)', 'Rester connecté en sécurité', 'Exécution du service', '30 jours, puis suppression'],
          ['Abonnement aux notifications et réglages des rappels', 'Envoyer des défis de révision dans la journée', 'Votre consentement (retirable à tout moment)', 'Jusqu’à la désactivation des rappels ou la suppression du compte'],
          ['Adresse IP et journaux techniques', 'Sécurité, protection contre les abus, résolution des pannes', 'Intérêt légitime (sécurité du service)', 'Quelques minutes pour les compteurs anti-abus ; journaux techniques de l’hébergeur pour une durée limitée'],
          ['Date de dernière visite', 'Supprimer les comptes inactifs', 'Intérêt légitime (minimisation des données)', 'Mise à jour une fois par jour'],
        ],
      },
    },
    {
      h: 'Ce que voient les autres joueurs',
      p: ['Dans les duels et le classement, les autres joueurs voient votre pseudo, votre personnage, votre rang, vos points de classement, votre nombre de victoires et votre code de duelliste. Vos amis voient aussi si vous êtes en ligne (ou depuis quand vous ne l’êtes plus) et le bilan de vos duels communs ; vous pouvez retirer un ami à tout moment. Votre adresse e-mail n’est jamais affichée. Choisissez un pseudo qui ne révèle pas votre identité si vous préférez rester discret.'],
    },
    {
      h: 'Destinataires et sous-traitants',
      list: [
        <><strong>{site.host.name}</strong> (hébergement de l’application, États-Unis). Les transferts vers les États-Unis sont encadrés par le cadre de protection des données UE–États-Unis (Data Privacy Framework), auquel Render est certifié.</>,
        <><strong>{site.database.name}</strong> (hébergement de la base de données, serveurs à Francfort, Union européenne).</>,
        <><strong>IONOS</strong> (nom de domaine et, le cas échéant, envoi des e-mails, comme la réinitialisation du mot de passe).</>,
        'Services de notification des navigateurs (Google, Mozilla, Apple…), uniquement si vous activez les notifications : ils relaient un message chiffré jusqu’à votre appareil.',
        'Lecture audio : le japonais est lu par la synthèse vocale de votre navigateur. Selon le navigateur, elle peut s’appuyer sur un service en ligne de son éditeur (par exemple Google pour Chrome) ; seul le texte japonais à prononcer est concerné.',
      ],
    },
    {
      h: 'Sécurité',
      p: ['Connexion HTTPS, mots de passe chiffrés avec bcrypt, cookie de session inaccessible aux scripts (httpOnly), limitation des tentatives de connexion par compte et par adresse, accès aux données réservé au service.'],
    },
    {
      h: 'Vos droits',
      p: [
        'Conformément au RGPD et à la loi Informatique et Libertés, vous disposez d’un droit d’accès, de rectification, d’effacement et de portabilité de vos données, d’un droit à la limitation et d’opposition, du droit de retirer votre consentement à tout moment, et du droit de définir des directives sur le sort de vos données après votre décès.',
        <>Directement dans l’application : <Link to="/settings">Réglages</Link> → « Télécharger mes données » (export) et « Supprimer mon compte » (effacement immédiat et définitif). Le pseudo et les objectifs se modifient dans le <Link to="/profile">Profil</Link>, les autres préférences dans les Réglages. Pour toute autre demande : {contact ?? 'voir les mentions légales'}. Réponse sous un mois.</>,
        <>Si vous estimez que vos droits ne sont pas respectés, vous pouvez adresser une réclamation à la CNIL ({ext('https://www.cnil.fr/fr/plaintes')}).</>,
      ],
    },
    {
      h: 'Mineurs',
      p: ['Koto Quest est ouvert à tous les apprenants. Avant 15 ans, l’accord d’un parent ou du titulaire de l’autorité parentale est nécessaire pour créer un compte et pour activer les notifications.'],
    },
    {
      h: 'Version hors ligne',
      p: ['La version hors ligne (fichier HTML unique) n’envoie aucune donnée : votre progression reste dans le stockage local de votre navigateur, sur votre appareil.'],
    },
    { h: 'Modifications', p: ['Cette politique peut évoluer ; la date de dernière mise à jour figure en haut de la page.'] },
  ];
}

// ───────────────────────── Cookies ─────────────────────────

function cookies(): Block[] {
  if (en)
    return [
      {
        h: 'In short',
        p: ['Koto Quest uses no advertising cookies, no audience-measurement cookies and no third-party cookies. It only uses what is strictly necessary for the service to work or what keeps the settings you choose. These trackers are exempt from consent under the rules of the CNIL (article 82 of the French Data Protection Act), which is why no cookie banner is shown.'],
      },
      {
        h: 'What is stored on your device',
        table: {
          head: ['Name', 'Type', 'Purpose', 'Lifetime'],
          rows: [
            ['koto_session', 'Cookie (httpOnly, secure)', 'Keeps you logged in', '30 days, or until logout'],
            ['koto-locale', 'Local storage', 'Remembers the language you chose', 'Until you clear it'],
            ['koto-locale-sync', 'Session storage', 'Avoids reloading the language several times', 'Until the tab is closed'],
            ['koto-path-level', 'Local storage', 'Remembers the level shown on the path', 'Until you clear it'],
            ['koto-quest-local-v1', 'Local storage', 'Offline version only: your progress', 'Until you clear it'],
            ['Notification subscription', 'Browser (service worker)', 'Receive review challenges, only if you turn them on', 'Until you turn them off'],
          ],
        },
      },
      {
        h: 'How to delete them',
        p: ['Logging out deletes the session cookie. You can delete all these elements at any time from your browser settings (site data for this address). Fonts are served by Koto Quest itself: no request is made to Google Fonts.'],
      },
    ];
  return [
    {
      h: 'En bref',
      p: ['Koto Quest n’utilise aucun cookie publicitaire, aucun cookie de mesure d’audience et aucun cookie tiers. Seuls sont utilisés les éléments strictement nécessaires au fonctionnement du service ou à la conservation des réglages que vous choisissez. Ces traceurs sont exemptés de consentement selon les règles de la CNIL (article 82 de la loi Informatique et Libertés) : c’est pourquoi aucun bandeau cookies n’est affiché.'],
    },
    {
      h: 'Ce qui est enregistré sur votre appareil',
      table: {
        head: ['Nom', 'Type', 'Rôle', 'Durée'],
        rows: [
          ['koto_session', 'Cookie (httpOnly, sécurisé)', 'Vous garder connecté', '30 jours, ou jusqu’à la déconnexion'],
          ['koto-locale', 'Stockage local', 'Retenir la langue choisie', 'Jusqu’à effacement'],
          ['koto-locale-sync', 'Stockage de session', 'Éviter de recharger plusieurs fois la langue', 'Jusqu’à la fermeture de l’onglet'],
          ['koto-path-level', 'Stockage local', 'Retenir le niveau affiché sur le parcours', 'Jusqu’à effacement'],
          ['koto-quest-local-v1', 'Stockage local', 'Version hors ligne uniquement : votre progression', 'Jusqu’à effacement'],
          ['Abonnement aux notifications', 'Navigateur (service worker)', 'Recevoir les défis de révision, seulement si vous les activez', 'Jusqu’à désactivation'],
        ],
      },
    },
    {
      h: 'Comment les supprimer',
      p: ['La déconnexion supprime le cookie de session. Vous pouvez effacer tous ces éléments à tout moment depuis les réglages de votre navigateur (données de site pour cette adresse). Les polices de caractères sont servies par Koto Quest lui-même : aucune requête n’est envoyée à Google Fonts.'],
    },
  ];
}

// ───────────────────────── Conditions d'utilisation ─────────────────────────

function terms(): Block[] {
  if (en)
    return [
      { h: 'Purpose', p: [`These terms govern the use of ${site.siteName} (${site.siteUrl}), a free application for learning Japanese published by ${E.owner} (${E.name}). Creating an account means accepting them.`] },
      { h: 'Account', p: ['You must provide a valid email address and keep your password confidential. One account per person. You are responsible for the activity on your account; report any suspected misuse to us.'] },
      {
        h: 'Rules of conduct',
        list: [
          'Choose a respectful username: no insults, hateful, discriminatory or sexual content, no impersonation, no advertising.',
          'Duels and leaderboard: play fair. Automated tools, scripts, multiple accounts or arranged matches to manipulate rankings are prohibited.',
          'Do not try to disrupt the service, access other people’s data or bypass security measures.',
        ],
      },
      { h: 'Moderation', p: ['In case of breach, we may reset a username, cancel ranking points, or suspend or delete the account concerned, after prior notice except in serious cases.'] },
      { h: 'Educational content', p: ['Lessons, exercises and mock exams are written with care but may contain errors. They are unofficial and do not guarantee success in the JLPT or any other exam. Please let us know of any error.'] },
      { h: 'Availability', p: ['The service is provided free of charge, “as is”. It may be interrupted for maintenance, updates or events beyond our control, and may take a few moments to start after a period without visitors. Features may change.'] },
      { h: 'Liability', p: [`The publisher cannot be held liable for indirect damage arising from the use of the service, nor for temporary unavailability. Nothing in these terms limits your statutory rights as a consumer.`] },
      { h: 'End of use', p: ['You can delete your account at any time from Settings; your data is then erased immediately. Accounts unused for 3 years are deleted automatically.'] },
      { h: 'Personal data', p: [<>See the <Link to="/confidentialite">privacy policy</Link> and the <Link to="/cookies">cookie policy</Link>.</>] },
      { h: 'Changes and applicable law', p: ['These terms may be updated; the date is shown at the top of the page. They are governed by French law. In the event of a dispute, an amicable solution will be sought first; you may also use a consumer mediator.'] },
    ];
  return [
    { h: 'Objet', p: [`Ces conditions encadrent l’utilisation de ${site.siteName} (${site.siteUrl}), application gratuite d’apprentissage du japonais éditée par ${E.owner} (${E.name}). Créer un compte vaut acceptation de ces conditions.`] },
    { h: 'Compte', p: ['Vous devez fournir une adresse e-mail valide et garder votre mot de passe confidentiel. Un compte par personne. Vous êtes responsable de l’activité de votre compte ; signalez-nous toute utilisation frauduleuse.'] },
    {
      h: 'Règles de conduite',
      list: [
        'Choisissez un pseudo respectueux : pas d’insulte, de contenu haineux, discriminatoire ou sexuel, pas d’usurpation d’identité, pas de publicité.',
        'Duels et classement : jouez loyalement. Outils automatiques, scripts, comptes multiples ou parties arrangées pour manipuler le classement sont interdits.',
        'N’essayez pas de perturber le service, d’accéder aux données d’autrui ou de contourner les mesures de sécurité.',
      ],
    },
    { h: 'Modération', p: ['En cas de manquement, nous pouvons réinitialiser un pseudo, annuler des points de classement, suspendre ou supprimer le compte concerné, après avertissement sauf en cas de faute grave.'] },
    { h: 'Contenus pédagogiques', p: ['Les leçons, exercices et examens blancs sont rédigés avec soin mais peuvent comporter des erreurs. Ils ne sont pas officiels et ne garantissent pas la réussite au JLPT ou à tout autre examen. Signalez-nous toute erreur.'] },
    { h: 'Disponibilité', p: ['Le service est fourni gratuitement, « en l’état ». Il peut être interrompu pour maintenance, mise à jour ou pour des raisons indépendantes de notre volonté, et peut mettre quelques instants à démarrer après une période sans visite. Les fonctionnalités peuvent évoluer.'] },
    { h: 'Responsabilité', p: [`L’éditeur ne saurait être tenu responsable des dommages indirects liés à l’utilisation du service, ni de ses indisponibilités temporaires. Rien dans ces conditions ne limite les droits que vous tenez de la loi en tant que consommateur.`] },
    { h: 'Fin d’utilisation', p: ['Vous pouvez supprimer votre compte à tout moment depuis les Réglages ; vos données sont alors effacées immédiatement. Les comptes inutilisés depuis 3 ans sont supprimés automatiquement.'] },
    { h: 'Données personnelles', p: [<>Voir la <Link to="/confidentialite">politique de confidentialité</Link> et la <Link to="/cookies">politique cookies</Link>.</>] },
    { h: 'Modifications et droit applicable', p: ['Ces conditions peuvent être mises à jour ; la date figure en haut de la page. Elles sont soumises au droit français. En cas de litige, une solution amiable sera recherchée en priorité ; vous pouvez aussi recourir à un médiateur de la consommation.'] },
  ];
}

// ───────────────────────── Affichage ─────────────────────────

const PAGES: Record<string, { title: () => string; blocks: () => Block[] }> = {
  '/mentions-legales': { title: () => T('Mentions légales'), blocks: notice },
  '/confidentialite': { title: () => T('Politique de confidentialité'), blocks: privacy },
  '/cookies': { title: () => T('Cookies et stockage local'), blocks: cookies },
  '/conditions': { title: () => T('Conditions d’utilisation'), blocks: terms },
};

export function LegalPage() {
  const { pathname } = useLocation();
  const page = PAGES[pathname] ?? PAGES['/mentions-legales'];
  return (
    <article className="legal mx-auto flex w-full max-w-3xl flex-col gap-6 py-4">
      <header className="flex flex-col gap-2">
        <h1 className="text-3xl sm:text-4xl">{page.title()}</h1>
        <p className="text-sm text-ink-soft">{T('{0} · dernière mise à jour : {1}', [site.siteName, updated])}</p>
      </header>
      {page.blocks().map((b) => (
        <section key={b.h} className="flex flex-col gap-2">
          <h2 className="text-xl">{b.h}</h2>
          {b.p?.map((x, i) => <p key={i} className="leading-relaxed">{x}</p>)}
          {b.list && (
            <ul className="flex list-disc flex-col gap-1.5 pl-5 leading-relaxed">
              {b.list.map((x, i) => <li key={i}>{x}</li>)}
            </ul>
          )}
          {b.table && (
            <>
            {/* Mobile : une fiche par ligne */}
            <div className="flex flex-col gap-3 sm:hidden">
              {b.table.rows.map((r, i) => (
                <dl key={i} className="rounded-2xl border border-line p-3 text-sm">
                  <dt className="sr-only">{b.table!.head[0]}</dt>
                  <dd className="font-bold">{r[0]}</dd>
                  {r.slice(1).map((c, j) => (
                    <div key={j} className="mt-1.5">
                      <dt className="inline text-ink-soft">{b.table!.head[j + 1]}{en ? ': ' : ' : '}</dt>
                      <dd className="inline">{c}</dd>
                    </div>
                  ))}
                </dl>
              ))}
            </div>
            <div className="hidden overflow-x-auto rounded-2xl border border-line sm:block">
              <table className="w-full min-w-[36rem] text-left text-sm">
                <thead className="bg-surface-2">
                  <tr>{b.table.head.map((h) => <th key={h} className="p-3 font-bold">{h}</th>)}</tr>
                </thead>
                <tbody>
                  {b.table.rows.map((r, i) => (
                    <tr key={i} className="border-t border-line align-top">
                      {r.map((c, j) => <td key={j} className={`p-3 ${j === 0 ? 'font-bold' : ''}`}>{c}</td>)}
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>
            </>
          )}
        </section>
      ))}
      <nav aria-label={T('Informations légales')} className="flex flex-wrap gap-3 border-t border-line pt-4 text-sm">
        {LEGAL_PAGES.filter((p) => p.path !== pathname).map((p) => (
          <Link key={p.path} to={p.path} className="underline">{p.label()}</Link>
        ))}
      </nav>
    </article>
  );
}

/** Page légale hors application (visiteur non connecté, accueil du compte). */
export function LegalStandalone({ back = '/welcome' }: { back?: string }) {
  return (
    <div className="mx-auto flex min-h-dvh max-w-3xl flex-col px-5 py-8">
      <div className="flex flex-wrap items-center gap-3">
        <img src="/icons/icon.svg" alt="" className="h-10 w-10" />
        <p className="font-display text-lg">{site.siteName}</p>
        <Link to={back} className="ml-auto underline">{T("Retour")}</Link>
      </div>
      <div className="flex-1"><LegalPage /></div>
      <SiteFooter />
    </div>
  );
}

/** Pied de page présent partout (connecté ou non). */
export function SiteFooter({ className = '' }: { className?: string }) {
  const year = new Date().getFullYear();
  return (
    <footer className={`mt-10 border-t border-line pt-5 pb-2 text-sm text-ink-soft ${className}`}>
      <nav aria-label={T('Informations légales')} className="flex flex-wrap items-center gap-x-4 gap-y-2">
        {LEGAL_PAGES.map((p) => (
          <Link key={p.path} to={p.path} className="hover:text-ink hover:underline">{p.label()}</Link>
        ))}
        {E.email && !LOCAL && <a href={`mailto:${E.email}`} className="hover:text-ink hover:underline">{T('Contact')}</a>}
      </nav>
      <p className="mt-2">© {year} {E.name} · {site.siteName}</p>
    </footer>
  );
}
