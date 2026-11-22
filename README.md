# Koto Quest

Application web (PWA) d'apprentissage du japonais (JLPT N5 à N1) et du coréen (TOPIK) : leçons courtes, répétition espacée FSRS et petits défis envoyés au fil de la journée.

> **État : phase 1 (MVP web).** Les parcours N5 (43 leçons), N4 (39 leçons), N3, N2 et N1 (24 leçons chacun) sont complets, chacun avec son examen blanc. Mode histoire, moteur de révision, lecture, duels, rappels et statistiques sont fonctionnels. L'application mobile correspond à la phase suivante : voir [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md).

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
- **Personnage et boutique** : avatar original à composer (teint, coiffure, couleur, yeux) et 35 cosmétiques (tenues, couvre-chefs, accessoires, décors), dont 12 coréens : hanbok, durumagi, épingle binyeo, éventail de danse, palais de Joseon, village hanok, et 6 trophées des gardiens du TOPIK 1 (corne de dokkaebi, chapeau gat, haetae, perle du renard, kakis séchés, mer de l’Est). Les objets s'achètent avec des pièces ; 14 trophées se débloquent en battant les gardiens. Achats et équipement validés côté serveur (débit conditionnel, jamais de solde négatif ni de double achat). Catalogue : `content/cosmetics/catalog.json`.
- **Économie de pièces** : 10 pièces à la première validation d'une leçon (+5 sans faute), 5 par quête du jour, 30 par première victoire sur un gardien. Les quêtes du jour rapportent désormais réellement leur XP, une seule fois chacune.
- **Mini-jeux** (onglet Jeux) : Kanji Rush (Hangeul Rush pour qui étudie le coréen), Speed Challenge et Listening Ninja, une minute chrono sur les notions déjà rencontrées. Score recalculé côté serveur à partir de l'heure de chaque réponse ; meilleurs scores enregistrés ; 1 pièce toutes les 5 bonnes réponses, plafonnées à 15 par jour. Les mini-jeux ne modifient pas la planification des révisions.
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
- **Audio** : synthèse vocale du navigateur (`apps/web/src/lib/speech.ts`) ; on attend que les voix soient chargées, on préfère une voix japonaise installée sur l'appareil (les voix en ligne démarrent avec du retard ou restent muettes), on laisse au moteur un court instant pour s'arrêter avant d'enchaîner, et seule la dernière demande est jouée. Même logique dans l'appli mobile (`apps/mobile/src/speech.ts`).
- **Interface** : responsive (barre d'onglets en bas sur mobile), modes clair et sombre, navigation clavier (touches 1 à 4 pour répondre), lecteurs d'écran, animations réduites sur demande, PWA installable.

### Plusieurs langues : japonais et coréen (TOPIK)
- **Langue étudiée** (`studyLanguage`, `ja` ou `ko`) choisie à l'onboarding, changeable à tout moment (barre latérale, Accueil, Parcours, Profil, Réglages). Le niveau visé appartient toujours à la langue étudiée ; chaque langue retrouve son dernier niveau (`levelByLanguage`). Logique commune : `packages/shared/src/languages.ts` (`applyStudyChoice`, `languageOfLevel`, `levelsOfLanguage`).
- Tout suit la langue : parcours et niveaux proposés, révisions et défis, statistiques, mini-jeux, atelier d'examen, caractères, expressions, contes. Les duels classés n'associent que des joueurs de la même langue. La progression de l'autre langue est conservée.
- **TOPIK 1** (`content/topik1/topik1.json`, généré par `scripts/topik1-level.py`) : 8 îles, 28 leçons, 185 notions — hangeul (voyelles, consonnes, aspirées, doubles, voyelles composées, batchim), se présenter, nombres sino-coréens et natifs, prix et heure, présent poli, 을/를, 에/에서, passé, négation, futur, -고 싶어요, -(으)세요, -(으)ㄹ까요, -고/-지만, transports, météo, restaurant. Romanisation révisée ; pas de « lecture » pour le vocabulaire coréen.
- **TOPIK 2** (`content/topik2/topik2.json`, `scripts/topik2-level.py`) : 8 îles, 24 leçons, 160 notions — raisons (-아서/-어서, -(으)니까, 때문에), capacité et permissions (-(으)ㄹ 수 있다, -아도 되다, -(으)면 안 되다, -아야 하다), -고 있다, -아/어 보다, -(으)ㄴ 적이 있다, propositions relatives (-는, -(으)ㄴ, -(으)ㄹ), -기 전에, -(으)ㄴ 후에, -(으)ㄹ 때, -(으)면서, -(으)면, -(으)려고, -(으)ㄹ게요, -기로 하다, honorifiques (-(으)시-, 께서, 드시다, 주무시다, 계시다, 께 드리다), comparaisons, -(으)ㄹ 것 같다, irréguliers ㄷ, 르, ㅡ.
- **TOPIK 3** (`content/topik3/topik3.json`, `scripts/topik3-level.py`), premier niveau du TOPIK II : 8 îles, 24 leçons, 163 notions — discours indirect (-다고, -냐고, -자고, -(으)라고, -대요/-래요), -는데, -거든요, -잖아요, -게 되다, -아/어지다, -게 하다, -기 위해서, -도록, -(으)려면, -(으)ㄹ 정도로, -는 대로, 처럼/만큼, passif et causatif, -아/어 있다, -(으)ㄹ걸 그랬다, -았/었으면 좋겠다, -아/어야겠다, -자마자, -는 동안, -(으)ㄴ 지.
- **TOPIK 4** (`content/topik4/topik4.json`, `scripts/topik4-level.py`) : 8 îles, 24 leçons, 166 notions — -다면서요, -더라고요, -던데요, -는 모양이다, -나 보다, -(으)ㄹ 텐데, -다면, -았/었더라면, -거든, -더라도, -는데도, -아/어 봤자, -는 바람에, -는 탓에, -느라고, -(으)ㄹ 뿐만 아니라, -는 데다가, -기도 하다, -(으)ㄹ까 하다, -는 김에, -(으)ㄹ 겸, -아/어 버리다, -고 말다, -아/어 놓다/두다 ; vocabulaire de société et de presse.
- **TOPIK 5** (`content/topik5/topik5.json`, `scripts/topik5-level.py`) : 8 îles, 24 leçons — -(으)ㄹ 뿐이다, -기 마련이다, -는 법이다, -는 반면에, -는가 하면, -는 데 반해, -(으)ㄹ 만하다, -(으)ㄹ 법하다, -(으)ㄹ 리가 없다, -는 한, -기에, -(으)므로, -(으)ㄴ 셈이다, -는 척하다, -(으)ㄹ 뻔하다, -(으)ㄹ수록, -다 보면, -다가는, -기는커녕, 조차, 마저, -는 대신에, -거니와, -(으)ㄴ 이상 ; mythes, chamanisme et débats de société.
- **TOPIK 6** (`content/topik6/topik6.json`, `scripts/topik6-level.py`) : 8 îles, 24 leçons — style écrit soutenu, connecteurs académiques, -는 데 그치지 않고, proverbes (속담) et expressions en quatre caractères (사자성어).
- **Mode histoire coréen** : TOPIK 6 « La Légende de Dangun » (Royaume de Gojoseon) : Hwanung, Ungnyeo, Jumong, Bak Hyeokgeose, esprit de la cloche d'Emille, Manpasikjeok, Cheoyong, Dangun ; carte de l'aube dorée. TOPIK 5 « Le Chant de la princesse Bari » (Terres des mythes) : Femme-escargot, Yeono et Seo-nyeo, Enfant général ailé, Garçon-arbre, Oneuri, Jacheongbi, Grand-mère Mago, Mujangseung ; carte du crépuscule des esprits (lueurs d'âmes). TOPIK 4 « L'Historien des Annales » (사관, Annales de Joseon) : Serpent gardien du grenier, Yagwanggwi, Jowangsin, Grand-mère Samsin, Dueoksini, Gangcheori, Chiens de feu, Hyeonmu ; carte d'hiver (neige). TOPIK 3 « L'Inspecteur royal secret » (암행어사, d'après le récit de Chunhyang) : Jangsanbeom, Eoduksini, Grand Arbre du village, Cheval céleste, Cerf de longévité, Mulgwisin, Janghwa et Hongryeon, Préfet Byeon ; carte d'été (rizières, lucioles). TOPIK 2 « Le Conteur du tigre blanc » (jeongisu de l'époque Joseon) : Jangseung, Crapaud d'or, Pie messagère, Samjogo, Grand-mère Seolmundae, masque de Hahoe, Phénix Bonghwang, Tigre blanc ; carte au printemps (azalées, forsythias). TOPIK 1 « La Voie du hwarang » (Silla), gardiens du folklore (Dokkaebi, Haetae, Gumiho, le Tigre et le kaki séché, Imugi, Bulgasari, Jeoseung saja, Dragon de la mer de l'Est), carte aux couleurs du dancheong et décors coréens (`components/KoreanScenes.tsx`).
- **Onglet Hangeul** (`content/characters/hangul.json`) : 70 lettres et syllabes, mêmes notions que les îles 1 et 2. **Expressions coréennes** (`content/expressions/expressions-ko.json`, `scripts/ko-expressions.py`) : 10 thèmes, 67 expressions, dont la **révision des proverbes** : « Proverbes du quotidien », « Proverbes des contes et des animaux » (속담) et « Expressions en quatre caractères » (사자성어), chacun avec son entraînement.
- **Contes coréens** (`scripts/ko-reading.py`) : 해님 달님, 흥부와 놀부, 견우와 직녀, 금도끼 은도끼 (TOPIK 1), 토끼와 자라, 선녀와 나무꾼, 혹부리 영감 et 콩쥐팥쥐 (TOPIK 2), 춘향전 et 심청전 (TOPIK 3), 홍길동전 (TOPIK 4), 바리공주 (TOPIK 5), 단군 신화 (TOPIK 6), 54 chapitres.
- **Examen blanc TOPIK I au format officiel** (`content/exams/topik1.json`, `scripts/topik1-exam.py`) : banque de 95 questions en coréen, 30 en écoute (듣기) et 40 en lecture (읽기), 100 minutes, noté sur 200 (niveau 1 à 80, niveau 2 à 140). Entraînement généré à partir des leçons (`topik1-mock`) et **Atelier TOPIK** (grammaire, écoute).
- **Examen blanc TOPIK I — niveau 2** (`content/exams/topik2.json`, `scripts/topik2-exam.py`, après `topik1-exam.py`) : même épreuve (le TOPIK I couvre les niveaux 1 et 2), banque enrichie de 37 questions plus difficiles (132 en tout) ; l'examen n'est validé qu'au niveau 2, 140/200 (`passLevel: 2`). Entraînement `topik2-mock`.
- **Examen blanc TOPIK II** (`content/exams/topik3.json`, `scripts/topik3-exam.py`) : version abrégée du format officiel, 25 questions d'écoute (듣기), 5 d'écriture (쓰기) et 25 de lecture (읽기) en 90 minutes, tirées d'une banque de 76 questions ; noté sur 300 (100 par épreuve), niveau 3 à 120, 4 à 150, 5 à 190, 6 à 230 (`scoring: 'topik2'`, section `writing`). L'écriture est adaptée en questions à choix (compléter un texte, décrire un graphique) : elle ne remplace pas la rédaction du vrai examen. Validé au niveau 3. Entraînement `topik3-mock`.
- **Examen blanc TOPIK II — niveau 4** (`content/exams/topik4.json`, `scripts/topik4-exam.py`, après `topik3-exam.py`) : même format, banque enrichie de 30 questions plus difficiles (106 en tout) ; validé seulement au niveau 4, 150/300. Entraînement `topik4-mock`.
- **Examens blancs TOPIK II — niveaux 5 et 6** (`content/exams/topik5.json`, `topik6.json`, `scripts/topik56-exam.py`, après `topik4-exam.py`) : même format, banques de 119 et 131 questions ; validés seulement au niveau 5 (190/300) ou 6 (230/300). Entraînements `topik5-mock` et `topik6-mock`.
- Synthèse vocale coréenne (voix `ko-KR` choisie selon le texte), police Gowun Dodum. Les six niveaux du TOPIK sont prêts.

### Examen blanc JLPT N5 au format officiel
- Banque de 130 questions rédigées en japonais (`content/exams/n5-jlpt.json`), dans les 11 épreuves du JLPT N5 : 漢字読み, 表記, 文脈規定, 言い換え類義 ; 文法形式の判断, 文の組み立て (★), 読解 ; 聴解 (課題理解, ポイント理解, 発話表現, 即時応答). Chaque examen tire 67 questions (70 minutes), choix mélangés.
- Écoute réaliste : dialogues à deux voix (hauteur de voix différente homme/femme), 2 écoutes au maximum, réponses à entendre pour 発話表現 et 即時応答 ; transcription donnée à la correction.
- Barème du JLPT : langue et lecture sur 120, écoute sur 60 ; réussite à 80/180 avec au moins 38 et 19. L'ancien examen (généré à partir des leçons) reste disponible comme version d'entraînement (`/exam/n5-mock`).

### Examens blancs JLPT N4 à N1 au format officiel (abrégé)
- Banques `content/exams/n4-jlpt.json` … `n1-jlpt.json`, générées par `scripts/jlpt-exams.py` : 漢字読み (lectures voisines comme distracteurs), 表記 (sauf au N1), 文脈規定, 言い換え類義, 文法形式の判断, 文の組み立て (★), 読解, 聴解 (課題理解, ポイント理解, 即時応答). Le vocabulaire, la grammaire, la phrase à reconstituer et les réponses orales viennent des mots, exemples et exercices du niveau ; la reformulation, la lecture et l'écoute (tâche, points essentiels) sont rédigées à part.
- 40 questions au N4, N3 et N2 (60, 70 et 75 minutes), 35 au N1 (80 minutes). C'est l'examen de l'île finale de chaque niveau ; l'ancien examen généré à partir des leçons reste la version d'entraînement (`/exam/nX-mock`).
- Barème du JLPT : au N4, langue et lecture sur 120 et écoute sur 60, réussite à 90/180 (38 et 19 au minimum) ; du N3 au N1, connaissances de la langue, lecture et écoute sur 60 chacune, 19 au minimum dans chaque partie, réussite à 95 (N3), 90 (N2) ou 100 (N1).

### Préparation à l'examen : cours alignés et format JLPT
- **Contenu aligné** : 16 leçons N5 ajoutées dans les îles existantes (famille, adjectifs en い et en な, calendrier, compteurs, forme en て de base, avant/après/pendant, gestes du quotidien, ville, points cardinaux, météo et santé, école, transports et téléphone, mots interrogatifs, invitations et comparaisons) : 43 leçons, 304 notions. Quelques mots de niveau N5 (電車, 電話, 借ります, 貸します, 開けます, 閉めます, 時計) sont passés du N4 au N5. Un test (`coverage.test.ts`) vérifie que chaque mot testé à l'examen blanc (lecture des kanji, orthographe, vocabulaire en contexte) est enseigné.
- **Difficulté progressive au format de l'examen** (`packages/learning-engine/src/jlpt.ts`) : 漢字読み (mot souligné dans une phrase des leçons, pièges de lecture : voyelle longue, ten-ten, petit っ, ゃゅょ) et 表記 (kanji sosies, okurigana fautifs), consignes en japonais. Dès la leçon pour la lecture des mots en kanji ; en révision, de plus en plus souvent à mesure que la notion est maîtrisée (une fois sur deux quand elle est bien installée) ; aussi dans la dernière phase des combats.
- **Atelier JLPT** (`/prepa`, `GET /api/jlpt/drills`, `POST /api/jlpt/drills/:part`) : séries de 10 questions par épreuve (漢字読み, 表記, 文法, ★, 聴解), construites uniquement avec les notions apprises et les exercices des leçons terminées ; les phrases à reconstituer deviennent des questions ★, les dialogues des questions d'écoute.

### Chrono des combats de gardiens
- 10 à 30 s par question selon l'exercice (`BOSS_TIME_LIMITS` dans le moteur). À zéro, la question est perdue et le gardien riposte.
- Contrôle côté serveur : l'affichage de la question est enregistré (`POST /questions/:id/shown`) ; une réponse arrivée après la limite (+2,5 s de marge) compte comme une erreur. Sans déclaration d'affichage, le chrono part de la réponse précédente : impossible de gagner du temps en trichant.

### Succès
- 41 succès en 5 catégories (étude, régularité, maîtrise, aventure, jeux et collection), de rareté courante, rare ou épique : 10, 25 ou 50 pièces et de l'XP, une seule fois.
- Succès propres à une langue : pour le japonais, les kanji, les kana (20 puis 92), les gardiens japonais (8 puis 24), un examen blanc JLPT validé et 10 chapitres de contes japonais ; pour le coréen, le hangeul (10 puis 40 lettres et syllabes), les gardiens coréens (8 puis 24), un examen blanc TOPIK validé et 10 chapitres de contes coréens. Chacun ne voit que ceux de sa langue (plus ceux déjà débloqués).
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

### Mode histoire
- Chaque niveau est une saga (`content/story/story.json`, français et anglais, régénéré par `scripts/gen-story.py`) : N5 « La Voie du samouraï » (侍), N4 « L'Ombre du ninja » (忍), N3 « Le Voyage de l'esprit » (霊), N2 « La Capitale de l'onmyōji » (陽), N1 « Le Règne du shōgun » (将). Les récits s'enchaînent.
- Un chapitre par île : titre, introduction qui relie la notion étudiée au gardien, et dénouement affiché une fois le gardien vaincu (ou l'examen réussi). Prologue en tête du parcours, épilogue quand le niveau est terminé.
- Sur la carte : bannière et sceau de la saga, emblème du héros sur le personnage, et un décor par île qui illustre son chapitre (`components/StoryScenes.tsx` : gué du Kappa, porte du château, pont de l'Oni, village caché, marché de nuit, palais sous l'orage, auberge aux horloges, forge de l'Oni, nid du corbeau…). La même île sert de vignette au chapitre dans la liste.
- Ambiance par saga : N5 de jour sur les routes du Japon féodal (pins, bannières, châteaux à l'horizon) ; N4 de nuit (fenêtres éclairées, lune, étoiles de ninja, ombre qui bondit, éclairs) ; N3 nuit de neige chez les esprits (mer indigo, voiles de lumière, feux follets, lanternes sur l'eau, lueur de l'aube près de la dernière île) ; N2 soir d'été dans la capitale (eau de jade, hortensias, lotus, lucioles, feux d'artifice) ; N1 aube du Nouvel An (ciel violet qui s'embrase d'or, mont Fuji, grues, pruniers en fleur, paillettes d'or).
- `apps/api/test/story.spec.ts` vérifie qu'aucune île n'est sans chapitre.

### Carte en archipel
- Chaque niveau est un archipel (`components/WorldMap.tsx`, SVG original) : une île par monde avec son repère (torii, pagode, mont Fuji, phare, bambouseraie, lanternes, cascade, sanctuaire pour l'examen), sceau rouge du gardien, plaque de bois avec le nom, ponts de bois entre les îles proches et chemins lumineux sur l'eau.
- Océan animé (vagues, bateaux, nuages, pétales), soleil couchant, halo sur l'île en cours où se tient le personnage ; les îles pas encore publiées apparaissent dans la brume. Animations coupées par « Réduire les animations ».

### Illustrations et animations
- Illustrations originales en SVG (`apps/web/src/components/Illustrations.tsx`) : scène d'accueil, vignette de chaque monde, chat endormi et pousse pour les écrans vides. Aucune image externe, couleurs issues du thème (mode sombre compris).
- Animations (`components/Celebrate.tsx`, Motion) : transitions de page, choix qui apparaissent un à un, secousse sur une erreur, « +XP » qui s'envole, tampon du résultat, confettis (leçon, gardien vaincu, record, examen réussi, positionnement), compteurs, flamme de série, personnage-compagnon qui parle, saute et cligne des yeux.
- Toutes les animations décoratives sont coupées par le réglage « Réduire les animations » ou par la préférence du système.

### Duels en ligne

Page **Duels** (`/duel`) : deux joueurs reçoivent la même question au même instant. Une bonne réponse inflige 6 à 16 dégâts selon la vitesse. Sous 2 s, c'est un coup critique (+3), et les bonnes réponses enchaînées ajoutent un combo (jusqu'à +4). 250 PV chacun, 30 questions de 10 s au plus : le K.-O. ou le plus de PV l'emporte. Un duel dure de 1 min 30 environ (joueurs rapides) à 5 min au plus.

- **Duel classé** : matchmaking aléatoire (adversaire au classement le plus proche dans la file d'attente).
- **Défi** : par code de duelliste (`KQ-XXXXXX`) ou recherche par nom. Le défi expire au bout de 2 min et le joueur défié reçoit une alerte partout dans l'application. Ces duels sont amicaux et ne comptent pas pour le classement.
- **Entraînement** contre un rōnin (IA), sans effet sur le classement. Il est proposé quand personne n'est en ligne.
- **Classement Elo** (départ à 1000 points). Rangs avec trois divisions chacun : Ashigaru (足軽), Samouraï (侍), Kengō (剣豪), Daimyō (大名), Shōgun (将軍), Tenkabito (天下人). Le tableau se trie par points ou par victoires. L'historique garde les 10 derniers duels.
- **Le serveur est le seul arbitre.** Il distribue les questions sans la réponse, mesure lui-même le temps de réponse, corrige, applique les dégâts sous verrou (un verrou consultatif PostgreSQL par duel) et déclare forfait un joueur silencieux pendant 25 s. Les clients interrogent l'état toutes les 600 ms.
- **Hors ligne**, les adversaires et le classement sont simulés, avec les mêmes règles (`packages/learning-engine/src/duel.ts`).

### Expressions utiles

L'onglet **Expressions** (`/expressions`) rassemble 104 expressions en 12 thèmes :

- politesse ;
- rencontres ;
- se faire comprendre ;
- restaurant ;
- magasins ;
- transports ;
- réactions ;
- urgences et santé ;
- entre amis (familier) ;
- travail (formel) ;
- **révision des proverbes** : ことわざ (猿も木から落ちる, 石の上にも三年, 急がば回れ…) et 四字熟語 (一期一会, 温故知新, 三日坊主…), générés par `scripts/ja-proverbs.py`. Plusieurs ont leur jumeau coréen (우물 안 개구리, 이심전심, 대기만성…).

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
- **Appli mobile** : mêmes dictionnaires que le web, plus `content/i18n/en/mobile.json` pour les textes propres au téléphone (`apps/mobile/src/i18n.ts`). Langue du téléphone par défaut, choix FR/EN à l'accueil et dans les Réglages (enregistré sur le compte) ; sans choix sur le téléphone, la langue suit celle du compte. `python3 scripts/mobile-i18n-keys.py` liste les textes encore sans traduction, et un test le vérifie.

## Profil

- Page **Profil** (`/profile`, menu « Profil », ou carte du personnage en bas du menu) : carte d'identité (personnage, pseudo, niveau et XP, objectif JLPT, rang de duelliste, boutons « Personnaliser » et « Mes succès »), « Identité et objectifs » (pseudo, niveau visé N5 à N1, temps d'étude par jour, date d'examen) et gestion des amis.
- Les **Réglages** gardent ce qui concerne l'application : défis dans la journée, langue et affichage, compte et données.
- Appli mobile : onglet **Profil** (人) à la place de Réglages ; les réglages s'ouvrent depuis le bouton « 設 Réglages » du profil.

## Amis

- Dans **Profil → Mes amis** : ajout par code de duelliste (`KQ-XXXXXX`) ou par nom, demande à accepter (alerte « X veut devenir ton ami » partout dans l'application), demandes croisées acceptées automatiquement.
- Liste d'amis avec **présence en ligne** (signe de vie toutes les 10 s quand l'application est ouverte, « vu il y a… » sinon), rang, bilan de vos duels communs, bouton **Défier** en un clic, retrait avec confirmation. La page **Duels** garde un encart « Défier un ami » (amis en ligne en premier, défi en un clic) avec un lien vers la gestion des amis.
- Après un duel contre un vrai joueur : bouton « Ajouter en ami ».
- Limites : 200 amis, 30 demandes envoyées en attente. API : `GET /friends`, `GET /friends/requests`, `POST /friends` (`code` ou `userId`), `POST /friends/:id/accept`, `DELETE /friends/:id`.
- Version hors ligne : non disponible (pas d'autres joueurs).

## Lecture

- Menu **Lecture** (`/lecture`) : douze contes traditionnels japonais réécrits en japonais simple, du N5 au N1 — N5 (Momotarō, Kasa Jizō, la grue reconnaissante, Hanasaka jiisan), N4 (Urashima Tarō, Issun-bōshi, Kaguya-hime, Shitakiri suzume), N3 (Yuki-onna, Warashibe Chōja), N2 (Mimi-nashi Hōichi) et N1 (Hachikazuki) — découpés en 51 chapitres de plus en plus longs (au N2 et au N1, des phrases plus longues et plus littéraires).
- **Tout est ouvert dès le départ** : le lecteur lit le conte et le chapitre qu'il veut, dans l'ordre qu'il veut, autant de chapitres par jour qu'il veut. Le « chapitre du jour » n'est qu'un conseil (le premier pas encore lu) ; une fois la lecture du jour faite, « Continuer la lecture » propose la suite. Série de jours de lecture, caractères lus, carte « Lecture du jour » sur l'accueil.
- Liseuse : furigana affichables, traduction FR/EN phrase par phrase (au toucher, tout, aucune), écoute phrase par phrase ou du chapitre entier, vocabulaire du chapitre, questions de compréhension (XP et pièces à la première lecture seulement).
- Contenu : `content/reading/stories.json` (furigana notés `{漢字|かな}`) ; logique commune serveur / hors ligne dans `packages/shared/src/reading.ts` ; API `GET /reading`, `GET /reading/chapters/:slug`, `POST /reading/chapters/:slug/complete`.

## Application mobile (Expo, phase 4)

`apps/mobile` : application iOS / Android en React Native (Expo SDK 58, expo-router), qui réutilise `@koto/shared` (contrats d'API) et `@koto/learning-engine`.

- **Écrans** : connexion / inscription, profil en un écran, accueil (action du moment, série, niveau, quêtes), parcours en mode histoire sur les cinq niveaux (saga du héros, chapitre et récit de chaque île), leçon (notions avec prononciation, exemples, exercices de tous les types, reprise des erreurs, mini-révision), onglet Kana (hiragana, katakana, kanji et expressions), lecture, révisions, profil (identité, objectifs, amis) et réglages.
- **Lecture** : les mêmes contes que sur le web, tous ouverts ; furigana à la demande (placés au-dessus des kanji, `src/Ruby.tsx`), traduction et prononciation au toucher d'une phrase, vocabulaire, questions de compréhension, série et récompenses communes au compte.
- **Rappels natifs** : `expo-notifications` programme chaque jour des notifications locales aux créneaux calculés par le serveur (mêmes réglages que le web) ; toucher la notification ouvre une séance de révision.
- **Session** : l'API renvoie un jeton au client mobile (en-tête `X-Koto-Client: mobile`), rangé dans le coffre sécurisé du téléphone (`expo-secure-store`) et envoyé en `Authorization: Bearer`. Le web garde son cookie httpOnly, jamais exposé au JavaScript.
- **Combats de gardiens** (`app/boss/[slug].tsx`) : vie du gardien, cœurs, coup final ; le résultat est recalculé par le serveur ; le dénouement du chapitre s'affiche à la victoire.
- **Examens blancs** (`app/exam/[slug].tsx`) : chronomètre, navigation entre les questions, écoute avec nombre d'écoutes limité, copie rendue automatiquement à la fin du temps, résultat par compétence, conseils et erreurs corrigées.
- **Kana** (onglet あ, `app/(tabs)/kana.tsx`) : grilles hiragana / katakana / kanji avec maîtrise par caractère, fiche au toucher (lectures on/kun, traits, écoute normale et lente), pratique d'un groupe ou d'une écriture entière ; expressions par thème avec recherche, registre, exemple et écoute, entraînement par thème (`app/practice.tsx`).
- **Navigation** : cinq onglets (Accueil, Parcours, Apprendre, Jouer, Profil). « Apprendre » (`app/(tabs)/learn.tsx`) regroupe, chacun expliqué en une phrase : Révisions, Lecture, Kana et kanji, Atelier JLPT, Examen blanc du niveau visé et Test de niveau. Chaque écran ouvert de là a un bouton retour (`TitleBar` dans `src/ui.tsx`).
- **Accueil** : test de niveau proposé aux nouveaux, guide « Comment ça marche ? » pendant les premières leçons, raccourcis (Apprendre, Jouer, Mon aventure, Mon personnage).
- **Atelier JLPT** (`app/prepa.tsx`) et **test de niveau** (`app/placement.tsx`), comme sur le web.
- **Personnage** (`app/character.tsx`, depuis le profil ou les pièces de l'accueil) : même dessin que le web (`src/Avatar.tsx`, react-native-svg), apparence, garde-robe et boutique (achats en pièces, trophées des gardiens).
- **Succès** (`app/achievements.tsx`) : médailles par catégorie ; vérifiés à chaque changement d'écran (hors séance en cours), avec une bannière « Succès débloqué » (`src/Achievements.tsx`).
- **Mon aventure** (`app/progress.tsx`, depuis l'accueil ou le profil) : fiche du héros, compétences, jardin de la mémoire, carnet des 14 derniers jours, examens blancs.
- **Mini-jeux** (onglet Jeux, `app/games/[id].tsx`) : Kanji Rush, Speed Challenge et Listening Ninja, avec compte à rebours, minute chronométrée, série, correction instantanée, score validé par le serveur, record et pièces communs au compte.
- **Langues** : français et anglais, comme le web (interface, cours, récit, contes, messages du serveur et rappels).
- **Japonais ou coréen** : la langue étudiée se choisit à l'inscription (`app/onboarding.tsx`) et se change dans le profil. En coréen : parcours TOPIK 1 à 6 et leurs sagas, onglet Hangeul (voyelles, consonnes, syllabes, expressions et proverbes), Atelier TOPIK, examens blancs TOPIK (barème sur 200 ou 300, niveau obtenu), contes coréens, Hangeul Rush et voix coréenne (`src/study.ts`, `src/speech.ts`).
- **Duels** (onglet Jeux → dojo, `app/duel/index.tsx` et `app/duel/[id].tsx`) : rang et palmarès, duel classé avec recherche d'adversaire, entraînement contre un rōnin, défi d'un ami en un geste (ajout et gestion dans le profil), invitations reçues, historique et classement. Dans l'arène, le chrono est calé sur l'horloge du serveur ; points de vie, combo, correction de chaque échange, abandon et revanche.

Lancer sur un téléphone (application Expo Go) :

```bash
npm run dev:api                                   # l'API doit être joignable depuis le téléphone
cd apps/mobile
EXPO_PUBLIC_API_URL=http://<IP-de-ton-PC>:3000 npx expo start   # puis scanner le QR code avec Expo Go
```

Sans variable, l'appli vise `http://10.0.2.2:3000` (émulateur Android) ou `http://localhost:3000`. Pour l'aperçu web de l'appli, ajoute son origine à l'API : `WEB_ORIGIN=http://localhost:5173,http://localhost:8081`.

Tests : `npx playwright test -c playwright.mobile.config.ts` (après `EXPO_PUBLIC_API_URL=http://localhost:3000 npm run export:web -w @koto/mobile`) déroule inscription → leçon complète → parcours → kana et expressions → lecture → mini-jeu → duel d’entraînement → révisions → atelier JLPT → test de niveau → profil → personnage et boutique → succès → mon aventure → rappels → déconnexion sur un téléphone émulé, contre la vraie API.

## Mise en production

Comptes, duels en ligne et classement nécessitent le serveur (API + PostgreSQL) ; la page `KotoQuest.html` n'est que la version hors ligne. Deux guides pas à pas : `docs/DEPLOIEMENT-RENDER.md` (gratuit : Render + base Neon, fichier `render.yaml`) et `docs/DEPLOIEMENT.md` (serveur/VPS avec Docker) : `Dockerfile`, `docker-compose.prod.yml` (PostgreSQL + application + Caddy pour le HTTPS automatique), `.env.prod.example`. En production, l'API sert aussi le site compilé (`WEB_DIST`) sur le même domaine.

## Informations légales (RGPD, cookies)

- Pied de page sur toutes les pages : **Mentions légales**, **Confidentialité**, **Cookies**, **Conditions d’utilisation** (`/mentions-legales`, `/confidentialite`, `/cookies`, `/conditions`), en français et en anglais (`apps/web/src/pages/Legal.tsx`).
- Les informations de l’éditeur et des hébergeurs sont dans `content/legal/site.json` : un champ vide n’est pas affiché. **À compléter** : forme juridique, capital, siège, SIREN/RCS, TVA, directeur de la publication, e-mail de contact. Mettre à jour `updatedAt` à chaque modification des textes.
- Pas de bandeau cookies : seul le cookie de session (strictement nécessaire) et des préférences en stockage local sont utilisés, sans mesure d’audience ni publicité (exemption CNIL).
- Polices auto-hébergées (`@fontsource`) : plus aucune requête vers Google Fonts.
- Comptes inactifs depuis 3 ans supprimés automatiquement chaque nuit (`RetentionService`), ainsi que les sessions et liens de réinitialisation expirés.
- Export complet des données (Réglages → Télécharger mes données) et suppression immédiate du compte.

## Limites connues

- **Audio** : synthèse vocale du navigateur (`ja-JP`). Si aucune voix japonaise n'est installée, l'exercice d'écoute affiche le mot à la place.
- **Web Push sur iPhone** : nécessite d'installer l'application sur l'écran d'accueil (iOS 16.4 ou plus récent).
- **Planificateur** : cron en mémoire dans le processus API (une seule instance). Passer à BullMQ + Redis avant de lancer plusieurs instances.
- **E-mails** : envoyés par SMTP si `SMTP_URL` est renseigné ; sinon, les liens sont écrits dans la console de l'API.
- **Contenu** : N5 complet (9 îles, 43 leçons) et N4 (9 îles, 39 leçons, 239 notions) ; N3 (9 îles, 24 leçons, 171 notions, examens blancs `n3-jlpt` et `n3-mock`, généré par `scripts/n3-level.py`) ; N2 (9 îles, 24 leçons, 192 notions, examens blancs `n2-jlpt` et `n2-mock`, généré par `scripts/n2-level.py`) ; N1 (9 îles, 24 leçons, 192 notions, examens blancs `n1-jlpt` et `n1-mock`, généré par `scripts/n1-level.py`). Le contenu N4 ajouté le 10/11/2026 est généré par `scripts/n4-extension.py` (français + anglais).
- **Migration initiale** : générée depuis le schéma Prisma dans un environnement sans accès aux moteurs Prisma. Après `npm run setup`, lancez `npm run db:migrate:dev -w @koto/api` une fois : si Prisma détecte un écart avec `schema.prisma`, il proposera une migration corrective.

## Variables d'environnement

Voir `apps/api/.env.example`. `npm run setup` crée `apps/api/.env` et génère des clés VAPID ; aucun secret n'est versionné.
