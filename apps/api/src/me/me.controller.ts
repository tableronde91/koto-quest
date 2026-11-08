import { Body, Controller, Delete, Get, HttpCode, Put, Res } from '@nestjs/common';
import { ApiTags } from '@nestjs/swagger';
import type { Response } from 'express';
import { AuthUser, CurrentUser } from '../common/decorators';
import { SESSION_COOKIE } from '../config';
import { DeleteAccountDto, OnboardingDto, PreferencesDto } from './dto';
import { MeService } from './me.service';

@ApiTags('compte')
@Controller('me')
export class MeController {
  constructor(private me: MeService) {}

  @Get() get(@CurrentUser() u: AuthUser) {
    return this.me.me(u.id);
  }

  @Put('onboarding') onboarding(@CurrentUser() u: AuthUser, @Body() dto: OnboardingDto) {
    return this.me.onboarding(u.id, dto);
  }

  @Put('preferences') prefs(@CurrentUser() u: AuthUser, @Body() dto: PreferencesDto) {
    return this.me.updatePreferences(u.id, dto);
  }

  @Get('export') async export(@CurrentUser() u: AuthUser, @Res({ passthrough: true }) res: Response) {
    res.setHeader('Content-Disposition', 'attachment; filename="koto-quest-export.json"');
    return this.me.export(u.id);
  }

  @Delete() @HttpCode(204) async remove(@CurrentUser() u: AuthUser, @Body() dto: DeleteAccountDto, @Res({ passthrough: true }) res: Response) {
    await this.me.deleteAccount(u.id, dto.password);
    res.clearCookie(SESSION_COOKIE, { path: '/' });
  }
}
