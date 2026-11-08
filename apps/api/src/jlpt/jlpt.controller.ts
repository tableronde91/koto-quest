import { Controller, Get, HttpCode, Param, Post } from '@nestjs/common';
import { ApiTags } from '@nestjs/swagger';
import { AuthUser, CurrentUser } from '../common/decorators';
import { JlptService } from './jlpt.service';

@ApiTags('atelier JLPT')
@Controller('jlpt')
export class JlptController {
  constructor(private jlpt: JlptService) {}

  @Get('drills') drills(@CurrentUser() u: AuthUser) {
    return this.jlpt.drills(u.id);
  }

  @Post('drills/:part') @HttpCode(201) start(@CurrentUser() u: AuthUser, @Param('part') part: string) {
    return this.jlpt.start(u.id, part);
  }
}
