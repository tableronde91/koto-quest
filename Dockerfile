# Image de production de Koto Quest : API NestJS + site web compilé, servis par le même processus.
#   docker compose -f docker-compose.prod.yml up -d --build
FROM node:20-bookworm-slim AS build
WORKDIR /app
RUN apt-get update && apt-get install -y --no-install-recommends openssl ca-certificates && rm -rf /var/lib/apt/lists/*

# Dépendances (l'application mobile Expo n'est pas installée sur le serveur)
COPY package.json package-lock.json ./
COPY apps/api/package.json apps/api/
COPY apps/web/package.json apps/web/
COPY apps/mobile/package.json apps/mobile/
COPY packages/shared/package.json packages/shared/
COPY packages/learning-engine/package.json packages/learning-engine/
RUN npm ci --workspace=@koto/api --workspace=@koto/web --workspace=@koto/shared --workspace=@koto/learning-engine --include-workspace-root --no-audit --no-fund

# Code et contenus, puis compilation
COPY tsconfig.base.json ./
COPY packages packages
COPY apps/api apps/api
COPY apps/web apps/web
COPY content content
COPY deploy deploy
RUN npm run build:packages \
 && npx -w @koto/api prisma generate \
 && npm run build -w @koto/api \
 && npm run build:seed -w @koto/api \
 && npm run build -w @koto/web

ENV NODE_ENV=production \
    PORT=3000 \
    NODE_OPTIONS=--max-old-space-size=384 \
    WEB_DIST=/app/apps/web/dist
EXPOSE 3000
HEALTHCHECK --interval=30s --timeout=5s --start-period=60s CMD node -e "fetch('http://127.0.0.1:'+(process.env.PORT||3000)+'/api/health').then(r=>process.exit(r.ok?0:1)).catch(()=>process.exit(1))"
CMD ["sh", "deploy/start.sh"]
