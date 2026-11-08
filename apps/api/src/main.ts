import { NestFactory } from '@nestjs/core';
import { Logger } from '@nestjs/common';
import { AppModule } from './app.module';
import { configureApp, serveWeb, setupSwagger } from './bootstrap';
import { config } from './config';

async function bootstrap() {
  const app = await NestFactory.create(AppModule);
  configureApp(app);
  setupSwagger(app);
  if (serveWeb(app, config.webDist)) Logger.log(`Site web servi depuis ${config.webDist}`, 'Koto Quest');
  await app.listen(config.port, '0.0.0.0');
  Logger.log(`API prête sur http://localhost:${config.port}/api — documentation : /api/docs`, 'Koto Quest');
}
bootstrap();
