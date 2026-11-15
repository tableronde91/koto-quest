import { Body, Controller, Get, HttpCode, Param, Post } from '@nestjs/common';
import { ApiProperty, ApiPropertyOptional, ApiTags } from '@nestjs/swagger';
import { ArrayMaxSize, IsArray, IsInt, IsOptional, Max, Min } from 'class-validator';
import { AuthUser, CurrentUser } from '../common/decorators';
import { ReadingService } from './reading.service';

class ReadingCompleteDto {
  @ApiProperty({ type: [Number], description: 'Indice du choix pour chaque question' })
  @IsArray()
  @ArrayMaxSize(10)
  @IsInt({ each: true })
  @Min(0, { each: true })
  @Max(9, { each: true })
  answers: number[];

  @ApiPropertyOptional() @IsOptional() @IsInt() @Min(0) @Max(36000) seconds?: number;
}

@ApiTags('reading')
@Controller('reading')
export class ReadingController {
  constructor(private reading: ReadingService) {}

  @Get() overview(@CurrentUser() u: AuthUser) {
    return this.reading.overview(u.id);
  }

  @Get('chapters/:slug') chapter(@CurrentUser() u: AuthUser, @Param('slug') slug: string) {
    return this.reading.chapter(u.id, slug);
  }

  @Post('chapters/:slug/complete') @HttpCode(201) complete(@CurrentUser() u: AuthUser, @Param('slug') slug: string, @Body() dto: ReadingCompleteDto) {
    return this.reading.complete(u.id, slug, dto.answers, dto.seconds);
  }
}
