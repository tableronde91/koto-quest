# Koto Quest

Application web (PWA) d'apprentissage du japonais, du JLPT N5 au N1 : leçons courtes, répétition espacée FSRS et petits défis envoyés au fil de la journée.

> **État : phase 1 (MVP web).** Le parcours N5 complet (43 leçons alignées sur l'examen, examen blanc au format officiel) et le N4 (21 leçons et son examen blanc), le moteur de révision, les rappels et les statistiques sont fonctionnels. La gamification avancée (avatar, boss, mini-jeux), les niveaux N4 à N1 et les niveaux N3 à N1 correspondent aux phases suivantes : voir [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md).

## Démarrage rapide

Prérequis : Node.js 20 ou plus récent, et PostgreSQL 16 (via Docker ou installé localement).

```bash
docker compose up -d        # PostgreSQL (crée aussi la base de test koto_test)
npm run setup               # dépendances, .env + clés VAPID, client Prisma, migrations, contenu N5
npm run dev                 # API sur :3000 et web sur :5173
```

Ouvrir http://localhost:5173, créer un compte et suivre l'onboarding.

- Documentation de l'API (OpenAPI) : http://localhost:3000/api/docs
- E-mails (réinitialisation de mot de passe) : affichés dans la console de l'API en développement.

Sans Docker, créez les bases `koto` et `koto_test` (utilisateur `koto`, mot de passe `koto`) ou adaptez `DATABASE_URL` dans `apps/api/.env`.

## Version hors ligne (sans serveur ni base de données)

Pour s'entraîner seul sur son ordinateur : ouvrir **`KotoQuest.html`** d'un double-clic (Chrome, Edge ou Firefox). Rien à installer.

- La progression est enregistrée dans le navigateur (localStorage). Réglages > « Télécharger une sauvegarde » pour la conserver ou la transférer.
- Les défis de la journée arrivent tant que l'onglet est ouvert (même en arrière-plan), avec notification système facultative.
- Même moteur pédagogique et même contenu que la version serveur. Le compte, la réinitialisation par e-mail et le Web Push n'existent pas dans cette version.
- Régénérer le fichier : `npm run build:offline`. Tester : `npm run test:offline`.

## Commandes

| Commande | Rôle |
|---|---|
| `npm run dev` | API (rechargement auto) + front Vite |
| `npm test` | Tests unitaires du moteur (Vitest) puis tests d'intégration de l'API (Jest + Supertest, base `koto_test`) |
| `npm run test:e2e` | Tests de bout en bout Playwright, desktop et mobile (lance l'API et le front si besoin). Exécutez `npx playwright install chromium` une fois, ou `PW_CHANNEL=chrome` pour utiliser votre Chrome |
| `npm run db:seed` | Réimporte le contenu de `content/` (idempotent, la progression est conservée) |
| `npm run db:migrate` | Applique les migrations Prisma |
| `npm run build` | Build de production (packages, API, web) |

## Organisation

```
apps/api                 NestJS + Prisma (PostgreSQL) — REST /api, OpenAPI /api/docs
apps/web                 React + Vite + Tailwind + TanStack Query + Motion — PWA
packages/learning-engine Moteur pédagogique pur TypeScript (FSRS, maîtrise, exercices, rappels, séries, quêtes)
packages/shared          Types des contrats d'API (partagés avec le futur mobile)
content/n5               Contenu pédagogique en JSON (voir content/README.md)
e2e                      Tests Playwright
docs/ARCHITECTURE.md     Architecture, écrans, modèle de données, API, plan par phases
```

## Ce que fait le MVP

- **Comptes** : inscription, connexion, sessions en cookie `httpOnly` révocables, réinitialisation du mot de passe, limitation de débit, export JSON et suppression définitive des données (RGPD).
- **Onboarding** : les 6 questions du cahier des charges. Le niveau déclaré fixe le monde de départ (les mondes précédents restent ouverts pour réviser).
- **Onglet Caractères** (ouvert à tous, sans déblocage) : grilles complètes des hiragana et katakana (de base, (han)dakuten, combinaisons) et 60 kanji N5 avec lectures on/kun. Chaque caractère a sa barre de maîtrise, partagée avec le parcours. « Apprendre » fait pratiquer en priorité les caractères dus, puis quelques nouveaux, puis les plus fragiles ; chaque ligne peut aussi être pratiquée seule. Le catalogue est dans `content/characters/characters.json`.
- **Boss de fin de monde** (début de la phase 2) : chaque monde terminé débloque un gardien (kappa, tanuki, kitsune, oni…). 12 questions de difficulté croissante, 9 coups pour le vaincre, 3 cœurs. Résultat recalculé côté serveur à partir des réponses enregistrées ; 120 XP et 30 pièces à la première victoire, récompense symbolique ensuite.
- **Personnage et boutique** : avatar original à composer (teint, coiffure, couleur, yeux) et 23 cosmétiques (tenues, couvre-chefs, accessoires, décors). Les objets s'achètent avec des pièces ; 8 trophées se débloquent en battant les gardiens. Achats et équipement validés côté serveur (débit conditionnel, jamais de solde négatif ni de double achat). Catalogue : `content/cosmetics/catalog.json`.
- **Économie de pièces** : 10 pièces à la première validation d'une leçon (+5 sans faute), 5 par quête du jour, 30 par première victoire sur un gardien. Les quêtes du jour rapportent désormais réellement leur XP, une seule fois chacune.
- **Mini-jeux** (onglet Jeux) : Kanji Rush, Speed Challenge et Listening Ninja, une minute chrono sur les notions déjà rencontrées. Score recalculé côté serveur à partir de l'heure de chaque réponse ; meilleurs scores enregistrés ; 1 pièce toutes les 5 bonnes réponses, plafonnées à 15 par jour. Les mini-jeux ne modifient pas la planification des révisions.
- **Carte des mondes** en haut du Parcours : route animée, personnage posé sur le monde en cours, gardiens indiqués ; toucher une étape fait défiler jusqu'à ses leçons.
- **Test de positionnement** (phase 3) : adaptatif, 3 questions par monde dans l'ordre du parcours ; un monde réussi (2/3) est validé et le test continue, il s'arrête au premier monde à travailler. Les leçons validées sont marquées terminées et leurs notions entrent en révision espacée (vérification quelques jours plus tard).
- **Examen blanc JLPT N5** (dernier monde) : 30 questions en 25 minutes, en trois sections (文字・語彙, 文法・読解, 聴解), sans correction pendant l'épreuve. Copie corrigée côté serveur, score par compétence, seuil indicatif (60 % au total, 40 % par section), recommandations, détail des erreurs ; les notions ratées repartent en révision. Historique et courbe dans Progrès. Examen non officiel.
- **Parcours N5** : mondes, chapitres et leçons avec déblocage progressif. Mondes livrés : hiragana, premiers katakana, se présenter, premières phrases, nombres/heures/jours, verbes en 〜ます (négation, passé, déplacements), premiers kanji, conversations (restaurant, magasin, chemin) : 27 leçons. Le dernier monde accueille l'examen blanc N5.
- **Leçons** : objectif, explication, notions (audio, furigana commutables, lectures on/kun des kanji), exemples, puis exercices et mini-révision.
- **10 types d’exercices**, tous corrigés **côté serveur** (le client ne reçoit jamais la réponse) : sens, traduction inverse, lecture, écoute, vrai/faux, association, particule, phrase à trous, remise en ordre, dialogue.
- **Exercices ratés repris en fin de séance** (au plus deux fois chacun), comme sur Duolingo. Le score de la leçon compte le premier essai, et la reprise ne replanifie pas la notion une seconde fois.
- **Phrase complète prononcée** après une bonne réponse (phrase à trou, remise en ordre, dialogue), avec le mot choisi à sa place. La phrase à trou n'est jamais lue avant la réponse.
- **Répétition espacée FSRS‑4.5** : difficulté, stabilité et échéance propres à chaque notion et à chaque utilisateur. Une notion réussie revient environ 4 h plus tard, puis à des intervalles croissants ; une erreur la fait revenir sous 10 à 15 minutes. Statuts : découverte, en apprentissage, fragile, maîtrisée, à réviser vite.
- **Charge quotidienne adaptative** : en cas de retard, les révisions sont plafonnées et les nouveautés ralenties au lieu de s'accumuler.
- **Défis dans la journée** : consentement explicite, 4 modes de fréquence, horaires personnalisés, heures silencieuses, pause. Un défi n'est envoyé que s'il y a une notion pertinente à réviser et jamais pendant une session d'étude. Il arrive en notification Web Push si le navigateur l'autorise, sinon en popup interactive dans l'application. La notification ouvre directement le mini-quiz.
- **Tableau de bord et statistiques** : série bienveillante (un jour manqué pardonné par semaine), XP et niveau, temps du jour, mots et kanji maîtrisés, révisions dues, leçon recommandée, 3 quêtes du jour, estimation prudente de préparation, graphiques et détail de chaque notion.
- **Interface** : responsive (barre d'onglets en bas sur mobile), modes clair et sombre, navigation clavier (touches 1 à 4 pour répondre), lecteurs d'écran, animations réduites sur demande, PWA installable.

### Examen blanc JLPT N5 au format officiel
- Banque de 130 questions rédigées en japonais (`content/exams/n5-jlpt.json`), dans les 11 épreuves du JLPT N5 : 漢字読み, 表記, 文脈規定, 言い換え類義 ; 文法形式の判断, 文の組み立て (★), 読解 ; 聴解 (課題理解, ポイント理解, 発話表現, 即時応答). Chaque examen tire 67 questions (70 minutes), choix mélangés.
- Écoute réaliste : dialogues à deux voix (hauteur de voix différente homme/femme), 2 écoutes au maximum, réponses à entendre pour 発話表現 et 即時応答 ; transcription donnée à la correction.
- Barème du JLPT : langue et lecture sur 120, écoute sur 60 ; réussite à 80/180 avec au moins 38 et 19. L'ancien examen (généré à partir des leçons) reste disponible comme version d'entraînement (`/exam/n5-mock`).

### Préparation à l'examen : cours alignés et format JLPT
- **Contenu aligné** : 16 leçons N5 ajoutées dans les îles existantes (famille, adjectifs en い et en な, calendrier, compteurs, forme en て de base, avant/après/pendant, gestes du quotidien, ville, points cardinaux, météo et santé, école, transports et téléphone, mots interrogatifs, invitations et comparaisons) : 43 leçons, 304 notions. Quelques mots de niveau N5 (電車, 電話, 借ります, 貸します, 開けます, 閉めます, 時計) sont passés du N4 au N5. Un test (`coverage.test.ts`) vérifie que chaque mot testé à l'examen blanc (lecture des kanji, orthographe, vocabulaire en contexte) est enseigné.
- **Difficulté progressive au format de l'examen** (`packages/learning-engine/src/jlpt.ts`) : 漢字読み (mot souligné dans une phrase des leçons, pièges de lecture : voyelle longue, ten-ten, petit っ, ゃゅょ) et 表記 (kanji sosies, okurigana fautifs), consignes en japonais. Dès la leçon pour la lecture des mots en kanji ; en révision, de plus en plus souvent à mesure que la notion est maîtrisée (une fois sur deux quand elle est bien installée) ; aussi dans la dernière phase des combats.
- **Atelier JLPT** (`/prepa`, `GET /api/jlpt/drills`, `POST /api/jlpt/drills/:part`) : séries de 10 questions par épreuve (漢字読み, 表記, 文法, ★, 聴解), construites uniquement avec les notions apprises et les exercices des leçons terminées ; les phrases à reconstituer deviennent des questions ★, les dialogues des questions d'écoute.

### Chrono des combats de gardiens
- 10 à 30 s par question selon l'exercice (`BOSS_TIME_LIMITS` dans le moteur). À zéro, la question est perdue et le gardien riposte.
- Contrôle côté serveur : l'affichage de la question est enregistré (`POST /questions/:id/shown`) ; une réponse arrivée après la limite (+2,5 s de marge) compte comme une erreur. Sans déclaration d'affichage, le chrono part de la réponse précédente : impossible de gagner du temps en trichant.

### Succès
- 29 succès en 5 catégories (étude, régularité, maîtrise, aventure, jeux et collection), de rareté courante, rare ou épique : 10, 25 ou 50 pièces et de l'XP, une seule fois.
- Catalogue et règles dans le moteur (`packages/learning-engine/src/achievements.ts`), testés. Le serveur recalcule les statistiques depuis la base (`GET /api/achievements`, `POST /api/achievements/check`) ; la clé primaire (utilisateur, succès) empêche toute double récompense, même en appels simultanés.
- L'application vérifie après chaque étape (fin de leçon, gardien, mini-jeu, examen, achat) et à chaque changement de page ; la notification attend la fin de l'exercice en cours. Collection dans « Succès » (depuis l'accueil ou Progrès).

### Parcours N4
- `content/n4/n4.json` : 7 îles, 21 leçons, 129 notions — forme en て (groupes 1, 2, irréguliers), 〜てください, 〜てもいいです, 〜てはいけません, forme en ない et 〜ないでください, forme en た et 〜たことがあります, 〜たいです, forme du dictionnaire et 〜つもりです, comparaisons (より, どちら/のほうが, いちばん), 〜と思います, raisons avec から et ので, あげる/もらう/くれる et services (〜てあげる…), 〜たら, forme potentielle, 〜とき. Un gardien par île.
- Examen blanc JLPT N4 (île 8) : 34 questions en 30 minutes, tirées du contenu N4, conseils de révision propres au niveau.
- Sélecteur de niveau dans Parcours (choix mémorisé). Le N4 s'ouvre au premier monde pour tout le monde ; une fois le N5 terminé, la prochaine leçon conseillée passe automatiquement au N4.
- Le seed refuse une notion présente dans deux niveaux (elle serait sinon déplacée silencieusement).

### Progrès : « Mon aventure »
- Fiche du héros (rang selon le niveau, anneau d'XP, série, pièces, leçons, temps d'étude), compétences façon RPG (kana, vocabulaire, kanji, grammaire : un niveau tous les 10 éléments maîtrisés), jardin de la mémoire (graines, pousses, fleurs, feuilles fragiles), carnet de route des 14 derniers jours, vitrine des gardiens vaincus, succès et tableau d'honneur.
- Le grimoire des notions et les graphiques détaillés restent disponibles (graphiques repliés).

### Carte en archipel
- Chaque niveau est un archipel (`components/WorldMap.tsx`, SVG original) : une île par monde avec son repère (torii, pagode, mont Fuji, phare, bambouseraie, lanternes, cascade, sanctuaire pour l'examen), sceau rouge du gardien, plaque de bois avec le nom, ponts de bois entre les îles proches et chemins lumineux sur l'eau.
- Océan animé (vagues, bateaux, nuages, pétales), soleil couchant, halo sur l'île en cours où se tient le personnage ; les îles pas encore publiées apparaissent dans la brume. Animations coupées par « Réduire les animations ».

### Illustrations et animations
- Illustrations originales en SVG (`apps/web/src/components/Illustrations.tsx`) : scène d'accueil, vignette de chaque monde, chat endormi et pousse pour les écrans vides. Aucune image externe, couleurs issues du thème (mode sombre compris).
- Animations (`components/Celebrate.tsx`, Motion) : transitions de page, choix qui apparaissent un à un, secousse sur une erreur, « +XP » qui s'envole, tampon du résultat, confettis (leçon, gardien vaincu, record, examen réussi, positionnement), compteurs, flamme de série, personnage-compagnon qui parle, saute et cligne des yeux.
- Toutes les animations décoratives sont coupées par le réglage « Réduire les animations » ou par la préférence du système.

### Duels en ligne

Page **Duels** (`/duel`) : deux joueurs reçoivent la même question au même instant. Une bonne réponse inflige 8 à 26 dégâts selon la vitesse. Sous 2 s, c'est un coup critique (+6), et les bonnes réponses enchaînées ajoutent un combo (jusqu'à +6). 100 PV chacun, 12 questions de 10 s au plus : le K.-O. ou le plus de PV l'emporte.

- **Duel classé** : matchmaking aléatoire (adversaire au classement le plus proche dans la file d'attente).
- **Défi** : par code de duelliste (`KQ-XXXXXX`) ou recherche par nom. Le défi expire au bout de 2 min et le joueur défié reçoit une alerte partout dans l'application. Ces duels sont amicaux et ne comptent pas pour le classement.
- **Entraînement** contre un rōnin (IA), sans effet sur le classement. Il est proposé quand personne n'est en ligne.
- **Classement Elo** (départ à 1000 points). Rangs avec trois divisions chacun : Ashigaru (足軽), Samouraï (侍), Kengō (剣豪), Daimyō (大名), Shōgun (将軍), Tenkabito (天下人). Le tableau se trie par points ou par victoires. L'historique garde les 10 derniers duels.
- **Le serveur est le seul arbitre.** Il distribue les questions sans la réponse, mesure lui-même le temps de réponse, corrige, applique les dégâts sous verrou (un verrou consultatif PostgreSQL par duel) et déclare forfait un joueur silencieux pendant 25 s. Les clients interrogent l'état toutes les 600 ms.
- **Hors ligne**, les adversaires et le classement sont simulés, avec les mêmes règles (`packages/learning-engine/src/duel.ts`).

### Expressions utiles

L'onglet **Expressions** (`/expressions`) rassemble 84 expressions courantes en 10 thèmes :

- politesse ;
- rencontres ;
- se faire comprendre ;
- restaurant ;
- magasins ;
- transports ;
- réactions ;
- urgences et santé ;
- entre amis (familier) ;
- travail (formel).

Chaque fiche donne le japonais, la lecture en kana, le romaji, le sens et une note d'usage (quand et à qui le dire). Elle indique aussi le registre (poli, neutre, familier, formel) et propose un exemple, avec écoute de l'expression et de l'exemple.

- **Recherche** en français, en anglais, en kana ou en romaji.
- **Entraînement par thème** : QCM, écoute, retrouver le japonais et associations. Une fois vues, les expressions entrent dans les révisions espacées, comme le vocabulaire des leçons.
- **Contenu** dans `content/expressions/expressions.json`, importé par le seed (notions `expr-*`). Traductions anglaises dans `content/i18n/en/content.json`.
- **Sur mobile**, le menu du bas affiche des libellés courts (« Kana », « Phrases »).

### Langues : français et anglais

L'application existe en **français** (langue source) et en **anglais**. On choisit sa langue sur la page d'accueil, au début de l'onboarding ou dans les Réglages. Par défaut, c'est le français pour un navigateur en français et l'anglais sinon. Une fois connecté, le choix est enregistré sur le compte (`preferences.locale`) et suit le joueur d'un appareil à l'autre.

- **Dictionnaires** dans `content/i18n/en/` : `ui.json` (interface), `engine.json` (consignes générées, succès, épreuves), `api.json` (messages du serveur) et `content.json` (cours N5/N4, examen blanc, caractères, boutique). Chaque clé est le texte français ; les variables s'écrivent `{0}` ou `{nom}`.
- **Interface** : chaque texte passe par `T('Texte français', [variables])` (`apps/web/src/i18n.ts`).
- **Données** : le client HTTP traduit toutes les réponses de l'API, motifs à variables compris (« Que signifie « 水 » ? » → « What does “水” mean? »). Les réponses du joueur sont renvoyées en VO au serveur, d'après les traductions réellement affichées : la correction reste inchangée côté serveur.
- **Côté serveur**, seuls les notifications push et l'e-mail de mot de passe sont traduits (`apps/api/src/common/i18n.ts`).
- **Ajouter un texte** : écrire la phrase en français dans `T(…)` puis ajouter sa traduction au dictionnaire. Le test `apps/api/test/i18n.spec.ts` échoue si un texte de cours ou un exercice généré n'est pas traduit, ou si deux sens deviennent identiques en anglais.
- **Limite** : l'application mobile (Expo) est encore en français uniquement.

## Application mobile (Expo, phase 4)

`apps/mobile` : application iOS / Android en React Native (Expo SDK 58, expo-router), qui réutilise `@koto/shared` (contrats d'API) et `@koto/learning-engine`.

- **Écrans** : connexion / inscription, profil en un écran, accueil (action du moment, série, niveau, quêtes), parcours N5 / N4 par îles, leçon (notions avec prononciation, exemples, exercices de tous les types, reprise des erreurs, mini-révision), révisions, réglages.
- **Rappels natifs** : `expo-notifications` programme chaque jour des notifications locales aux créneaux calculés par le serveur (mêmes réglages que le web) ; toucher la notification ouvre une séance de révision.
- **Session** : l'API renvoie un jeton au client mobile (en-tête `X-Koto-Client: mobile`), rangé dans le coffre sécurisé du téléphone (`expo-secure-store`) et envoyé en `Authorization: Bearer`. Le web garde son cookie httpOnly, jamais exposé au JavaScript.
- Combats de gardiens, mini-jeux et examens blancs restent pour l'instant sur la version web (indiqué dans l'appli).

Lancer sur un téléphone (application Expo Go) :

```bash
npm run dev:api                                   # l'API doit être joignable depuis le téléphone
cd apps/mobile
EXPO_PUBLIC_API_URL=http://<IP-de-ton-PC>:3000 npx expo start   # puis scanner le QR code avec Expo Go
```

Sans variable, l'appli vise `http://10.0.2.2:3000` (émulateur Android) ou `http://localhost:3000`. Pour l'aperçu web de l'appli, ajoute son origine à l'API : `WEB_ORIGIN=http://localhost:5173,http://localhost:8081`.

Tests : `npx playwright test -c playwright.mobile.config.ts` (après `EXPO_PUBLIC_API_URL=http://localhost:3000 npm run export:web -w @koto/mobile`) déroule inscription → leçon complète → parcours → révisions → rappels → déconnexion sur un téléphone émulé, contre la vraie API.

## Mise en production

Comptes, duels en ligne et classement nécessitent le serveur (API + PostgreSQL) ; la page `KotoQuest.html` n'est que la version hors ligne. Deux guides pas à pas : `docs/DEPLOIEMENT-RENDER.md` (gratuit : Render + base Neon, fichier `render.yaml`) et `docs/DEPLOIEMENT.md` (serveur/VPS avec Docker) : `Dockerfile`, `docker-compose.prod.yml` (PostgreSQL + application + Caddy pour le HTTPS automatique), `.env.prod.example`. En production, l'API sert aussi le site compilé (`WEB_DIST`) sur le même domaine.

## Limites connues

- **Audio** : synthèse vocale du navigateur (`ja-JP`). Si aucune voix japonaise n'est installée, l'exercice d'écoute affiche le mot à la place.
- **Web Push sur iPhone** : nécessite d'installer l'application sur l'écran d'accueil (iOS 16.4 ou plus récent).
- **Planificateur** : cron en mémoire dans le processus API (une seule instance). Passer à BullMQ + Redis avant de lancer plusieurs instances.
- **E-mails** : envoyés par SMTP si `SMTP_URL` est renseigné ; sinon, les liens sont écrits dans la console de l'API.
- **Contenu** : N5 partiel. Pas encore de test de positionnement (l'onboarding fixe le point de départ) ni d'examen blanc.
- **Migration initiale** : générée depuis le schéma Prisma dans un environnement sans accès aux moteurs Prisma. Après `npm run setup`, lancez `npm run db:migrate:dev -w @koto/api` une fois : si Prisma détecte un écart avec `schema.prisma`, il proposera une migration corrective.

## Variables d'environnement

Voir `apps/api/.env.example`. `npm run setup` crée `apps/api/.env` et génère des clés VAPID ; aucun secret n'est versionné.
