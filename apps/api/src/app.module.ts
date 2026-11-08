import { Module } from '@nestjs/common';
import { APP_GUARD } from '@nestjs/core';
import { ScheduleModule } from '@nestjs/schedule';
import { ThrottlerModule } from '@nestjs/throttler';
import { KotoThrottlerGuard } from './common/throttler.guard';
import { PrismaService } from './common/prisma.service';
import { ClockService } from './common/clock.service';
import { AuthController } from './auth/auth.controller';
import { AuthService } from './auth/auth.service';
import { AuthGuard } from './auth/auth.guard';
import { MailService } from './auth/mail.service';
import { MeController } from './me/me.controller';
import { MeService } from './me/me.service';
import { ContentController } from './content/content.controller';
import { ContentService } from './content/content.service';
import { LearningController } from './learning/learning.controller';
import { LearningService } from './learning/learning.service';
import { ActivityService } from './learning/activity.service';
import { DashboardController } from './dashboard/dashboard.controller';
import { DashboardService } from './dashboard/dashboard.service';
import { NotificationsController } from './notifications/notifications.controller';
import { NotificationsService } from './notifications/notifications.service';
import { PushService } from './notifications/push.service';
import { HealthController } from './health.controller';
import { CharactersController } from './characters/characters.controller';
import { CharactersService } from './characters/characters.service';
import { BossController } from './boss/boss.controller';
import { BossService } from './boss/boss.service';
import { ShopController } from './shop/shop.controller';
import { ShopService } from './shop/shop.service';
import { GamesController } from './games/games.controller';
import { GamesService } from './games/games.service';
import { ExamController } from './exam/exam.controller';
import { ExamService } from './exam/exam.service';
import { AchievementsController } from './achievements/achievements.controller';
import { AchievementsService } from './achievements/achievements.service';
import { JlptController } from './jlpt/jlpt.controller';
import { JlptService } from './jlpt/jlpt.service';
import { DuelController } from './duel/duel.controller';
import { ExpressionsController } from './expressions/expressions.controller';
import { ExpressionsService } from './expressions/expressions.service';
import { DuelService } from './duel/duel.service';

@Module({
  imports: [
    ScheduleModule.forRoot(),
    // Protection contre les abus : 300 requêtes/minute par IP par défaut (plus strict sur l'authentification).
    ThrottlerModule.forRoot([{ ttl: 60_000, limit: Number(process.env.API_RATE_LIMIT ?? 300) }]),
  ],
  controllers: [HealthController, AuthController, MeController, ContentController, LearningController, DashboardController, NotificationsController, CharactersController, BossController, ShopController, GamesController, ExamController, AchievementsController, JlptController, DuelController, ExpressionsController],
  providers: [
    PrismaService,
    ClockService,
    MailService,
    AuthService,
    MeService,
    ContentService,
    ActivityService,
    LearningService,
    AchievementsService,
    JlptService,
    DuelService,
    ExpressionsService,
    DashboardService,
    PushService,
    NotificationsService,
    CharactersService,
    BossService,
    ShopService,
    GamesService,
    ExamService,
    { provide: APP_GUARD, useClass: KotoThrottlerGuard },
    { provide: APP_GUARD, useClass: AuthGuard },
  ],
})
export class AppModule {}
