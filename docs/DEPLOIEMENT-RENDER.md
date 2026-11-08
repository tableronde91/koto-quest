# Mettre Koto Quest en ligne gratuitement : Render + Neon

- **Neon** héberge la base PostgreSQL (gratuit, 1 Go).
- **Render** fait tourner l'application (API + site) à partir du `Dockerfile` et du fichier `render.yaml`.
- **IONOS** garde le nom de domaine : on change juste un enregistrement DNS.

Il faut compter environ 45 minutes la première fois. Tout se fait dans le navigateur, avec PowerShell pour envoyer le code sur GitHub.

---

## Étape 0 — Créer les comptes (gratuits)

1. **GitHub** : <https://github.com/signup> (pour héberger le code, en dépôt privé).
2. **Neon** : <https://neon.com> → *Sign up* (le plus simple : « Continue with GitHub »).
3. **Render** : <https://render.com> → *Get Started* → « GitHub ».
4. Sur ton PC : **Git pour Windows**, depuis <https://git-scm.com/download/win> (options par défaut).

---

## Étape 1 — Envoyer le code sur GitHub

1. Sur GitHub : **+** (en haut à droite) → *New repository*.
   - Nom : `koto-quest`
   - Coche **Private**.
   - Ne coche rien d'autre (pas de README, pas de .gitignore).
   - *Create repository*.
2. Dézippe `koto-quest.zip`, par exemple dans `C:\Projets\koto-quest`.
3. Ouvre **PowerShell**, puis :

```powershell
cd C:\Projets\koto-quest
git init
git add .
git commit -m "Koto Quest"
git branch -M main
git remote add origin https://github.com/TON-PSEUDO/koto-quest.git
git push -u origin main
```

Si Git demande ton nom et ton e-mail, lance une seule fois :

```powershell
git config --global user.name "Ton Nom"
git config --global user.email "ton@email.fr"
```

Puis refais le `git commit`. Au `git push`, une fenêtre GitHub s'ouvre pour te connecter.

Vérifie sur GitHub que les fichiers sont là, notamment `Dockerfile` et `render.yaml`. Aucun mot de passe n'est dans le zip : les fichiers `.env` en sont exclus.

---

## Étape 2 — Créer la base sur Neon

1. *Create project*.
   - Nom : `koto-quest`.
   - Version de Postgres : celle proposée par défaut.
   - Région : **AWS Europe Central 1 (Frankfurt)**, la même que Render pour la rapidité.
2. Sur le tableau de bord du projet, clique sur **Connect**.
   - **Désactive « Connection pooling »**. C'est important : il faut la connexion directe, sans `-pooler` dans l'adresse.
   - Copie la chaîne de connexion. Elle ressemble à :
     `postgresql://neondb_owner:xxxxx@ep-xxxx-xxxx.eu-central-1.aws.neon.tech/neondb?sslmode=require&channel_binding=require`
3. **Retire `&channel_binding=require`** à la fin, et garde `?sslmode=require`.
4. Garde cette chaîne de côté : c'est ton `DATABASE_URL`. Elle contient un mot de passe, ne la partage pas.

Il n'y a rien d'autre à faire dans Neon : les tables sont créées automatiquement au premier démarrage.

---

## Étape 3 — Déployer l'application sur Render

1. Sur Render : **New +** → **Blueprint**.
2. Connecte ton compte GitHub si besoin, puis choisis le dépôt `koto-quest`.
3. Render lit `render.yaml` et affiche le service `koto-quest` (offre **Free**, région Frankfurt). Remplis les valeurs demandées :

| Variable | Valeur |
|---|---|
| `DATABASE_URL` | La chaîne Neon de l'étape 2 |
| `WEB_ORIGIN` | `https://koto-quest.ananda-garapati.fr,https://koto-quest.onrender.com` |
| `VAPID_PUBLIC_KEY` / `VAPID_PRIVATE_KEY` | Laisse vide pour l'instant (facultatif, voir plus bas) |
| `SMTP_URL` | Laisse vide pour l'instant (facultatif, voir plus bas) |

Si Render donne un autre nom que `koto-quest.onrender.com` (par exemple `koto-quest-ab12.onrender.com`), mets ce nom-là dans `WEB_ORIGIN`.

4. **Apply**. La première construction prend 5 à 10 minutes. Dans **Logs**, tu dois voir défiler :
   - `→ Migrations de la base de données`
   - `→ Contenus … import`
   - puis `API prête`.
5. Teste l'adresse Render (en haut de la page du service, `https://koto-quest….onrender.com`) :
   - `…onrender.com/api/health` doit répondre `{"status":"ok"}` ;
   - la page d'accueil doit proposer **Créer un compte**.

---

## Étape 4 — Brancher ton domaine IONOS

1. Sur Render, dans le service, ouvre **Settings** → **Custom Domains** → **Add Custom Domain** → `koto-quest.ananda-garapati.fr`.
   Render affiche une cible **CNAME**, du type `koto-quest.onrender.com`. Garde la page ouverte.
2. Dans l'espace client IONOS : **Domaines & SSL** → `ananda-garapati.fr` → onglet **DNS**.
   - Supprime les enregistrements **A** et **AAAA** existants du sous-domaine `koto-quest`. Ce sont eux qui pointent vers la version hors ligne actuelle.
   - IONOS refuse parfois un CNAME tant que le sous-domaine est rattaché à l'hébergement web. Dans ce cas, va dans **Utilisation du domaine** et choisis « Utiliser mes propres enregistrements DNS » (le libellé varie un peu selon l'interface).
   - **Ajouter un enregistrement** → **CNAME** :
     - Nom d'hôte : `koto-quest`
     - Pointe vers : la cible donnée par Render
     - TTL : 1 heure (ou la valeur par défaut)
3. Retourne sur Render et clique sur **Verify**. Au bout de quelques minutes (parfois jusqu'à une heure), le domaine passe en vert et Render installe le certificat HTTPS tout seul.
4. Ouvre <https://koto-quest.ananda-garapati.fr> : c'est la version en ligne, avec les comptes.

---

## Étape 5 — Vérifier avec deux comptes

1. Crée un compte sur le site.
2. Ouvre une **fenêtre de navigation privée** et crée un second compte.
3. Sur les deux : **Duels** → **Duel classé** → **Trouver un adversaire**. Le duel démarre.
4. Ou bien, depuis un compte, défie l'autre avec son code `KQ-…` (onglet Duels).

---

## Bon à savoir (offre gratuite)

- **Mise en veille** : après 15 minutes sans visite, Render met le site en veille. Le visiteur suivant attend environ une minute le temps du réveil. C'est normal.
- **Ne pas maintenir le site éveillé artificiellement**, par exemple avec un service qui l'interroge toutes les 10 minutes. L'application interroge alors la base en continu, et le quota gratuit de Neon (environ 400 heures de calcul par mois) serait épuisé avant la fin du mois. Pour un site toujours disponible, il faudra passer à une offre payante (Render « Starter » ou un VPS).
- **Rappels du jour** : ils ne partent que lorsque le site est éveillé.
- **Mises à jour** : chaque `git push` sur `main` redéploie automatiquement :

  ```powershell
  cd C:\Projets\koto-quest
  # (remplacer les fichiers par la nouvelle version)
  git add .
  git commit -m "Mise à jour"
  git push
  ```

  Les comptes et les progressions sont conservés.
- **Sauvegardes** : Neon garde un historique court (offre gratuite). Pour une copie de sécurité, utilise *Branches* → *Create branch* dans Neon, ou un `pg_dump` depuis ton PC.

### Facultatif — notifications push

Sur un PC qui a Node.js :

```powershell
npx web-push generate-vapid-keys
```

Copie les deux clés dans Render : **Environment** → `VAPID_PUBLIC_KEY` et `VAPID_PRIVATE_KEY`, puis **Save changes**. Le service redémarre tout seul.

### Facultatif — e-mails « mot de passe oublié »

Avec une adresse e-mail IONOS, mets dans `SMTP_URL` :

```
smtps://adresse%40ananda-garapati.fr:MOT_DE_PASSE@smtp.ionos.fr:465
```

Dans l'adresse, `@` s'écrit `%40`. Mets aussi `MAIL_FROM` à `Koto Quest <adresse@ananda-garapati.fr>`. Sans SMTP, le site fonctionne, mais le lien de réinitialisation n'apparaît que dans les logs Render.

---

## En cas de problème

| Symptôme | Cause probable |
|---|---|
| Logs : `P1001 Can't reach database` | `DATABASE_URL` mal copiée, ou connexion « pooling » au lieu de directe. |
| Logs : erreur sur `channel_binding` | Retirer `&channel_binding=require` de `DATABASE_URL`. |
| Le site affiche encore l'ancienne version | Le DNS n'est pas encore propagé, ou les A/AAAA du sous-domaine n'ont pas été supprimés chez IONOS. Vider le cache du navigateur. |
| Inscription OK mais « Session expirée » en boucle | Le site n'est pas ouvert en `https://`. Utiliser l'adresse https. |
| Build qui échoue sur Render | Ouvrir **Logs** du déploiement et m'envoyer les dernières lignes. |
