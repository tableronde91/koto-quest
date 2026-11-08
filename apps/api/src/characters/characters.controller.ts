import { Body, Controller, Get, HttpCode, Post } from '@nestjs/common';
import { ApiProperty, ApiTags } from '@nestjs/swagger';
import { IsString, Length } from 'class-validator';
import { AuthUser, CurrentUser } from '../common/decorators';
import { CharactersService } from './characters.service';

class PracticeDto {
  @ApiProperty({ description: 'hiragana, katakana, kanji ou un groupe (ex. hira-k)' }) @IsString() @Length(2, 40) scope: string;
}

@ApiTags('caractères')
@Controller('characters')
export class CharactersController {
  constructor(private chars: CharactersService) {}

  @Get() overview(@CurrentUser() u: AuthUser) {
    return this.chars.overview(u.id);
  }

  @Post('practice') @HttpCode(201) practice(@CurrentUser() u: AuthUser, @Body() dto: PracticeDto) {
    return this.chars.practice(u.id, dto.scope);
  }
}
