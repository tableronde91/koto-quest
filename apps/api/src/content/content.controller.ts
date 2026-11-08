import { Controller, Get, Param } from '@nestjs/common';
import { ApiTags } from '@nestjs/swagger';
import { JLPT_LEVELS, JlptCode } from '@koto/shared';
import { BadRequestException } from '@nestjs/common';
import { AuthUser, CurrentUser } from '../common/decorators';
import { ContentService } from './content.service';

@ApiTags('contenu')
@Controller()
export class ContentController {
  constructor(private content: ContentService) {}

  @Get('path/:level')
  path(@CurrentUser() user: AuthUser, @Param('level') level: string) {
    const code = level.toUpperCase() as JlptCode;
    if (!JLPT_LEVELS.includes(code)) throw new BadRequestException('Niveau JLPT inconnu.');
    return this.content.path(user.id, code);
  }

  @Get('lessons/:slug')
  lesson(@CurrentUser() user: AuthUser, @Param('slug') slug: string) {
    return this.content.lessonDto(user.id, slug);
  }
}
