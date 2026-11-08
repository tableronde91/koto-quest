import { Body, Controller, Get, HttpCode, Param, ParseUUIDPipe, Post } from '@nestjs/common';
import { ApiTags } from '@nestjs/swagger';
import { AuthUser, CurrentUser } from '../common/decorators';
import { AnswerDto, CompleteLessonDto } from './dto';
import { LearningService } from './learning.service';
import { BadRequestException } from '@nestjs/common';

@ApiTags('apprentissage')
@Controller()
export class LearningController {
  constructor(private learning: LearningService) {}

  @Post('lessons/:slug/start')
  start(@CurrentUser() u: AuthUser, @Param('slug') slug: string) {
    return this.learning.startLesson(u.id, slug);
  }

  @Post('lessons/:slug/complete') @HttpCode(200)
  complete(@CurrentUser() u: AuthUser, @Param('slug') slug: string, @Body() dto: CompleteLessonDto) {
    return this.learning.completeLesson(u.id, slug, dto.sessionId);
  }

  @Get('questions/:id')
  question(@CurrentUser() u: AuthUser, @Param('id', ParseUUIDPipe) id: string) {
    return this.learning.getQuestion(u.id, id);
  }

  @Post('questions/:id/answer') @HttpCode(200)
  answer(@CurrentUser() u: AuthUser, @Param('id', ParseUUIDPipe) id: string, @Body() dto: AnswerDto) {
    const valid = typeof dto.answer === 'string' ? dto.answer.length <= 500 : Array.isArray(dto.answer) && dto.answer.length <= 20 && dto.answer.every((a) => typeof a === 'string' && a.length <= 200);
    if (!valid) throw new BadRequestException('Format de réponse invalide.');
    return this.learning.answer(u.id, id, dto.answer, dto.responseMs);
  }

  /** Combat de gardien : départ du chrono de la question. */
  @Post('questions/:id/shown') @HttpCode(200)
  shown(@CurrentUser() u: AuthUser, @Param('id', ParseUUIDPipe) id: string) {
    return this.learning.shown(u.id, id);
  }

  /** Exercice raté : renvoie une copie à refaire en fin de séance. */
  @Post('questions/:id/retry')
  retry(@CurrentUser() u: AuthUser, @Param('id', ParseUUIDPipe) id: string) {
    return this.learning.retry(u.id, id);
  }

  @Get('reviews/summary')
  summary(@CurrentUser() u: AuthUser) {
    return this.learning.reviewSummary(u.id);
  }

  @Post('reviews/session')
  review(@CurrentUser() u: AuthUser) {
    return this.learning.startReviewSession(u.id);
  }

  @Post('quiz/next')
  quiz(@CurrentUser() u: AuthUser) {
    return this.learning.issueQuiz(u.id).then((q) => ({ question: q }));
  }
}
