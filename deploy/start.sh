#!/bin/sh
# Démarrage en production : migrations de la base, mise à jour des contenus (sans toucher aux joueurs), puis l'API.
set -e
cd /app/apps/api
echo "→ Migrations de la base de données"
npx prisma migrate deploy
echo "→ Contenus (cours, caractères, expressions) : import s'ils ont changé"
node dist-seed/seed.js --if-changed
echo "→ Démarrage de Koto Quest"
exec node dist/main.js
