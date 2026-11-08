import { Body, Controller, HttpCode, Param, Post } from '@nestjs/common';
import { ApiTags } from '@nestjs/swagger';
import { AuthUser, CurrentUser } from '../common/decorators';
import { CompleteLessonDto } from '../learning/dto';
import { BossService } from './boss.service';

@ApiTags('boss')
@Controller('worlds/:slug/boss')
export class BossController {
  constructor(private boss: BossService) {}

  @Post('start') start(@CurrentUser() u: AuthUser, @Param('slug') slug: string) {
    return this.boss.start(u.id, slug);
  }

  @Post('finish') @HttpCode(200) finish(@CurrentUser() u: AuthUser, @Param('slug') slug: string, @Body() dto: CompleteLessonDto) {
    return this.boss.finish(u.id, slug, dto.sessionId);
  }
}
