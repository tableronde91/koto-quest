import { INestApplication, ValidationPipe } from '@nestjs/common';
import { DocumentBuilder, SwaggerModule } from '@nestjs/swagger';
import cookieParser from 'cookie-parser';
import helmet from 'helmet';
import express, { type NextFunction, type Request, type Response } from 'express';
import { existsSync } from 'fs';
import { join } from 'path';
import { config } from './config';

/** Configuration commune à l'application et aux tests d'intégration. */
export function configureApp(app: INestApplication) {
  if (config.trustProxy) {
    const v = config.trustProxy;
    app.getHttpAdapter().getInstance().set('trust proxy', /^\d+$/.test(v) ? Number(v) : v === 'true' ? true : v);
  }
  app.setGlobalPrefix('api');
  app.use(helmet());
  app.use(cookieParser());
  // WEB_ORIGIN accepte plusieurs origines séparées par des virgules (ex. web + aperçu web de l'appli mobile).
  // Les applications natives n'envoient pas d'en-tête Origin et ne sont pas concernées par le CORS.
  app.enableCors({ origin: config.webOrigin.split(',').map((o) => o.trim()), credentials: true });
  app.useGlobalPipes(
    new ValidationPipe({ whitelist: true, forbidNonWhitelisted: true, transform: true, transformOptions: { enableImplicitConversion: false } }),
  );
  app.enableShutdownHooks();
}

export function setupSwagger(app: INestApplication) {
  const doc = new DocumentBuilder()
    .setTitle('Koto Quest API')
    .setDescription('API de l’application d’apprentissage du japonais Koto Quest. Authentification par cookie de session httpOnly (web) ou jeton Bearer (application mobile).')
    .setVersion('0.1.0')
    .addCookieAuth('koto_session')
    .addBearerAuth()
    .build();
  SwaggerModule.setup('api/docs', app, SwaggerModule.createDocument(app, doc));
}

/**
 * En production, l'API sert aussi le site web compilé : fichiers statiques, puis index.html
 * pour toutes les autres adresses (navigation côté client), sauf /api.
 */
export function serveWeb(app: INestApplication, dist: string) {
  if (!dist || !existsSync(join(dist, 'index.html'))) return false;
  const index = join(dist, 'index.html');
  app.use(
    express.static(dist, {
      index: false,
      setHeaders: (res, path) => {
        if (/[\\/]assets[\\/]/.test(path)) res.setHeader('Cache-Control', 'public, max-age=31536000, immutable');
        else res.setHeader('Cache-Control', 'no-cache');
      },
    }),
  );
  app.use((req: Request, res: Response, next: NextFunction) => {
    if ((req.method !== 'GET' && req.method !== 'HEAD') || req.path === '/api' || req.path.startsWith('/api/')) return next();
    res.setHeader('Cache-Control', 'no-cache');
    res.sendFile(index);
  });
  return true;
}
