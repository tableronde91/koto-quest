import { Body, Controller, Get, HttpCode, Param, Post } from '@nestjs/common';
import { ApiTags } from '@nestjs/swagger';
import { AuthUser, CurrentUser } from '../common/decorators';
import { CompleteLessonDto } from '../learning/dto';
import { GamesService } from './games.service';

@ApiTags('mini-jeux')
@Controller('games')
export class GamesController {
  constructor(private games: GamesService) {}

  @Get() list(@CurrentUser() u: AuthUser) {
    return this.games.overview(u.id);
  }

  @Post(':id/start') start(@CurrentUser() u: AuthUser, @Param('id') id: string) {
    return this.games.start(u.id, id);
  }

  @Post(':id/finish') @HttpCode(200) finish(@CurrentUser() u: AuthUser, @Param('id') id: string, @Body() dto: CompleteLessonDto) {
    return this.games.finish(u.id, id, dto.sessionId);
  }
}
