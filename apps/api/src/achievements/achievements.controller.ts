import { Controller, Get, HttpCode, Post } from '@nestjs/common';
import { ApiTags } from '@nestjs/swagger';
import { AuthUser, CurrentUser } from '../common/decorators';
import { AchievementsService } from './achievements.service';

@ApiTags('succès')
@Controller('achievements')
export class AchievementsController {
  constructor(private achievements: AchievementsService) {}

  @Get() list(@CurrentUser() u: AuthUser) {
    return this.achievements.list(u.id);
  }

  /** Vérifie et attribue les succès atteints (appelé par l'application après une progression). */
  @Post('check') @HttpCode(200) check(@CurrentUser() u: AuthUser) {
    return this.achievements.check(u.id);
  }
}
