import { Body, ConflictException, Controller, Delete, Get, HttpCode, Param, ParseUUIDPipe, Post, Put } from '@nestjs/common';
import { ApiTags } from '@nestjs/swagger';
import { Throttle } from '@nestjs/throttler';
import { AuthUser, CurrentUser } from '../common/decorators';
import { NotificationPrefsInput, PushSubscriptionInput, UnsubscribeInput } from './dto';
import { NotificationsService } from './notifications.service';

@ApiTags('rappels')
@Controller('notifications')
export class NotificationsController {
  constructor(private notifs: NotificationsService) {}

  @Get('preferences') get(@CurrentUser() u: AuthUser) {
    return this.notifs.getPrefs(u.id);
  }

  @Put('preferences') update(@CurrentUser() u: AuthUser, @Body() dto: NotificationPrefsInput) {
    return this.notifs.updatePrefs(u.id, dto);
  }

  @Post('push-subscription') subscribe(@CurrentUser() u: AuthUser, @Body() dto: PushSubscriptionInput) {
    return this.notifs.subscribe(u.id, dto);
  }

  @Delete('push-subscription') unsubscribe(@CurrentUser() u: AuthUser, @Body() dto: UnsubscribeInput) {
    return this.notifs.unsubscribe(u.id, dto.endpoint);
  }

  @Get('inbox') inbox(@CurrentUser() u: AuthUser) {
    return this.notifs.inbox(u.id);
  }

  @Post(':id/open') @HttpCode(200) open(@CurrentUser() u: AuthUser, @Param('id', ParseUUIDPipe) id: string) {
    return this.notifs.open(u.id, id);
  }

  /** « Envoie-moi un défi maintenant » : pratique pour tester les rappels. */
  @Throttle({ default: { limit: 5, ttl: 60_000 } })
  @Post('test') async test(@CurrentUser() u: AuthUser) {
    const r = await this.notifs.createChallenge(u.id, { allowNotDue: true });
    if (!r) throw new ConflictException('Aucune notion à réviser pour le moment : apprends d’abord une leçon !');
    return r;
  }
}
