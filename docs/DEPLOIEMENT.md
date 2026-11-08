# Mettre Koto Quest en ligne avec les comptes et les duels

La page `KotoQuest.html` est la **version hors ligne** : tout reste dans le navigateur du joueur, sans compte ni adversaire réel. Pour les comptes, les duels en ligne, le classement et les défis entre amis, il faut faire tourner **le serveur** : l'API Node.js et une base PostgreSQL. Le serveur sert aussi le site web.

```
Navigateur ──HTTPS──▶ Caddy (ou votre Nginx/Apache) ──▶ app :3000 (API + site) ──▶ PostgreSQL
```

## Ce qu'il faut

- Un serveur capable de faire tourner **Docker** : VPS chez OVH, Scaleway, Hetzner, o2switch Cloud… 1 vCPU et 1 à 2 Go de RAM suffisent pour démarrer.
  Un hébergement mutualisé classique (PHP uniquement) **ne convient pas**.
- Le nom de domaine `koto-quest.ananda-garapati.fr` pointé (enregistrement DNS A/AAAA) vers l'IP de ce serveur.
- Facultatif : un compte SMTP (celui de votre hébergeur e-mail, Brevo, Mailjet…) pour les e-mails « mot de passe oublié ».

## Installation (première fois)

```bash
# 1. Sur le serveur : Docker
curl -fsSL https://get.docker.com | sh

# 2. Le code
git clone <votre dépôt> koto-quest && cd koto-quest
#    (ou copier le contenu du zip dans un dossier koto-quest)

# 3. La configuration
cp .env.prod.example .env
nano .env        # DOMAIN, POSTGRES_PASSWORD (openssl rand -hex 24), SMTP_URL…

# 4. Les clés des notifications push (à copier dans .env)
docker compose -f docker-compose.prod.yml build app
docker compose -f docker-compose.prod.yml run --rm --no-deps app node -e "console.log(require('web-push').generateVAPIDKeys())"

# 5. Lancement
docker compose -f docker-compose.prod.yml up -d --build
docker compose -f docker-compose.prod.yml logs -f app   # « API prête » puis Ctrl+C
```

Au démarrage, l'application applique les migrations de la base et importe les contenus (cours, caractères, expressions), puis démarre. Caddy obtient le certificat HTTPS tout seul.

Vérifications :

- `https://votre-domaine/api/health` doit répondre `{"status":"ok"}`.
- Créez un compte, puis ouvrez une fenêtre de navigation privée avec un second compte et lancez **Duels → Duel classé** sur les deux.

## Si le serveur a déjà un Nginx ou un Apache

Lancez sans Caddy :

```bash
docker compose -f docker-compose.prod.yml up -d --build db app
```

Exemple Nginx (le certificat est géré comme pour vos autres sites, par exemple avec certbot) :

```nginx
server {
    server_name koto-quest.ananda-garapati.fr;
    listen 443 ssl http2;
    # ssl_certificate … ; ssl_certificate_key … ;
    client_max_body_size 5m;
    location / {
        proxy_pass http://127.0.0.1:3000;
        proxy_set_header Host $host;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
```

Gardez `TRUST_PROXY=1` (déjà fixé dans `docker-compose.prod.yml`) : sans lui, tous les joueurs partageraient la même limite anti-abus, et les connexions seraient bloquées dès 10 essais par minute sur tout le site.

## Mettre à jour

```bash
git pull            # ou remplacer les fichiers par le nouveau zip
docker compose -f docker-compose.prod.yml up -d --build
```

Les données des joueurs sont conservées : les migrations ne font qu'ajouter, et l'import des contenus ne touche ni aux comptes ni aux progressions.

## Sauvegarder la base

```bash
docker compose -f docker-compose.prod.yml exec -T db pg_dump -U koto koto | gzip > koto-$(date +%F).sql.gz
```

À planifier chaque jour (cron) et à copier hors du serveur.

## À savoir

- **Une seule instance** de l'application, à cause du planificateur de rappels en mémoire. C'est largement suffisant pour démarrer.
- **La progression faite dans la version hors ligne** (`KotoQuest.html`) ne se transfère pas vers un compte.
- **Garder la version hors ligne** reste possible : vous pouvez la publier à une autre adresse (ex. `/hors-ligne.html`), comme démonstration sans compte.
- **Tester la version de production en local** : `npm run build`, puis lancer l'API avec `WEB_DIST=apps/web/dist`, puis `npx playwright test -c playwright.prod.config.ts`.
