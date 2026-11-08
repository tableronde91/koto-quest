import { Controller, Get } from '@nestjs/common';
import { ApiTags } from '@nestjs/swagger';
import { AuthUser, CurrentUser } from '../common/decorators';
import { DashboardService } from './dashboard.service';

@ApiTags('suivi')
@Controller()
export class DashboardController {
  constructor(private dash: DashboardService) {}

  @Get('dashboard') dashboard(@CurrentUser() u: AuthUser) {
    return this.dash.dashboard(u.id);
  }

  @Get('stats') stats(@CurrentUser() u: AuthUser) {
    return this.dash.stats(u.id);
  }
}
