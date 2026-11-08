import { Body, Controller, Get, HttpCode, Post } from '@nestjs/common';
import { ApiProperty, ApiTags } from '@nestjs/swagger';
import { IsString, Length } from 'class-validator';
import { AuthUser, CurrentUser } from '../common/decorators';
import { ExpressionsService } from './expressions.service';

class ExpressionPracticeDto {
  @ApiProperty({ description: 'Thème (ex. politesse, restaurant)' }) @IsString() @Length(2, 40) theme: string;
}

@ApiTags('expressions')
@Controller('expressions')
export class ExpressionsController {
  constructor(private expressions: ExpressionsService) {}

  @Get() overview(@CurrentUser() u: AuthUser) {
    return this.expressions.overview(u.id);
  }

  @Post('practice') @HttpCode(201) practice(@CurrentUser() u: AuthUser, @Body() dto: ExpressionPracticeDto) {
    return this.expressions.practice(u.id, dto.theme);
  }
}
