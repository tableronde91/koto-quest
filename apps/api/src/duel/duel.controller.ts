import { Body, Controller, Delete, Get, HttpCode, Param, ParseUUIDPipe, Post, Query } from '@nestjs/common';
import { ApiProperty, ApiPropertyOptional, ApiTags } from '@nestjs/swagger';
import { SkipThrottle } from '@nestjs/throttler';
import { IsInt, IsOptional, IsString, IsUUID, Matches, Max, MaxLength, Min } from 'class-validator';
import { AuthUser, CurrentUser } from '../common/decorators';
import { DuelService } from './duel.service';

class DuelAnswerDto {
  @ApiProperty() @IsInt() @Min(0) @Max(50) round: number;
  @ApiProperty() @IsString() @MaxLength(200) answer: string;
}

class ChallengeDto {
  @ApiPropertyOptional({ description: 'Code de duelliste (KQ-XXXXXX)' })
  @IsOptional() @IsString() @Matches(/^(KQ-?)?[A-Z0-9]{6}$/i, { message: 'Code de duelliste invalide.' })
  code?: string;
  @ApiPropertyOptional() @IsOptional() @IsUUID() userId?: string;
}

@ApiTags('duels')
@Controller('duels')
export class DuelController {
  constructor(private duels: DuelService) {}

  @Get() lobby(@CurrentUser() u: AuthUser) {
    return this.duels.lobby(u.id);
  }

  /** Défis reçus (sondé régulièrement par l'application pour afficher une alerte) */
  @SkipThrottle() @Get('invites') invites(@CurrentUser() u: AuthUser) {
    return this.duels.invites(u.id);
  }

  @Get('leaderboard') leaderboard(@CurrentUser() u: AuthUser, @Query('sort') sort?: string) {
    return this.duels.leaderboard(u.id, sort === 'wins' ? 'wins' : 'rating');
  }

  @Get('players') search(@CurrentUser() u: AuthUser, @Query('q') q = '') {
    return this.duels.search(u.id, String(q).slice(0, 40));
  }

  @Post('queue') @HttpCode(200) join(@CurrentUser() u: AuthUser) {
    return this.duels.joinQueue(u.id);
  }

  @SkipThrottle() @Get('queue') poll(@CurrentUser() u: AuthUser) {
    return this.duels.pollQueue(u.id);
  }

  @Delete('queue') leave(@CurrentUser() u: AuthUser) {
    return this.duels.leaveQueue(u.id);
  }

  @Post('practice') practice(@CurrentUser() u: AuthUser) {
    return this.duels.practice(u.id);
  }

  @Post('challenges') challenge(@CurrentUser() u: AuthUser, @Body() dto: ChallengeDto) {
    return this.duels.challenge(u.id, dto);
  }

  @SkipThrottle() @Get(':id') state(@CurrentUser() u: AuthUser, @Param('id', ParseUUIDPipe) id: string) {
    return this.duels.state(u.id, id);
  }

  @Post(':id/accept') @HttpCode(200) accept(@CurrentUser() u: AuthUser, @Param('id', ParseUUIDPipe) id: string) {
    return this.duels.accept(u.id, id);
  }

  @Post(':id/decline') @HttpCode(200) decline(@CurrentUser() u: AuthUser, @Param('id', ParseUUIDPipe) id: string) {
    return this.duels.decline(u.id, id);
  }

  @Post(':id/answer') @HttpCode(200) answer(@CurrentUser() u: AuthUser, @Param('id', ParseUUIDPipe) id: string, @Body() dto: DuelAnswerDto) {
    return this.duels.answer(u.id, id, dto.round, dto.answer);
  }

  @Post(':id/forfeit') @HttpCode(200) forfeit(@CurrentUser() u: AuthUser, @Param('id', ParseUUIDPipe) id: string) {
    return this.duels.forfeit(u.id, id);
  }
}
