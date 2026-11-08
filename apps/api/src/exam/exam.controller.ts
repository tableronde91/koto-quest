import { Body, Controller, HttpCode, Param, Post } from '@nestjs/common';
import { ApiProperty, ApiTags } from '@nestjs/swagger';
import { IsObject, IsUUID } from 'class-validator';
import { AuthUser, CurrentUser } from '../common/decorators';
import { ExamService } from './exam.service';

class AnswersDto {
  @ApiProperty() @IsUUID() sessionId: string;
  @ApiProperty({ description: 'Réponses par identifiant de question' }) @IsObject() answers: Record<string, unknown>;
}

@ApiTags('examens')
@Controller()
export class ExamController {
  constructor(private exams: ExamService) {}

  @Post('exams/:slug/start') start(@CurrentUser() u: AuthUser, @Param('slug') slug: string) {
    return this.exams.start(u.id, slug);
  }

  @Post('exams/:slug/submit') @HttpCode(200) submit(@CurrentUser() u: AuthUser, @Param('slug') slug: string, @Body() dto: AnswersDto) {
    return this.exams.submit(u.id, slug, dto.sessionId, dto.answers);
  }

  @Post('placement/start') placement(@CurrentUser() u: AuthUser) {
    return this.exams.placementStart(u.id);
  }

  @Post('placement/answer') @HttpCode(200) placementAnswer(@CurrentUser() u: AuthUser, @Body() dto: AnswersDto) {
    return this.exams.placementAnswer(u.id, dto.sessionId, dto.answers);
  }
}
