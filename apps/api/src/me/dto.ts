import { ApiProperty, ApiPropertyOptional } from '@nestjs/swagger';
import { ArrayMaxSize, IsArray, IsBoolean, IsIn, IsInt, IsISO8601, IsOptional, IsString, Length, Max, Min, ValidateIf } from 'class-validator';
import { DIFFICULT_AREAS, JLPT_LEVELS } from '@koto/shared';

const SELF_LEVELS = ['beginner', 'kana', 'basics', 'n5', 'n4plus'];

export class OnboardingDto {
  @ApiProperty({ enum: SELF_LEVELS }) @IsIn(SELF_LEVELS) selfLevel: string;
  @ApiProperty({ enum: JLPT_LEVELS }) @IsIn(JLPT_LEVELS) targetLevel: string;
  @ApiPropertyOptional() @IsOptional() @ValidateIf((_, v) => v !== null) @IsISO8601() examDate?: string | null;
  @ApiProperty() @IsInt() @Min(5) @Max(240) minutesPerDay: number;
  @ApiProperty({ isArray: true, enum: DIFFICULT_AREAS }) @IsArray() @ArrayMaxSize(6) @IsIn(DIFFICULT_AREAS, { each: true }) difficultAreas: string[];
  @ApiProperty({ enum: ['off', 'calm', 'normal', 'intense', 'custom'] }) @IsIn(['off', 'calm', 'normal', 'intense', 'custom']) reminderMode: string;
  @ApiPropertyOptional() @IsOptional() @IsString() @Length(1, 64) timezone?: string;
  @ApiPropertyOptional({ enum: ['fr', 'en'] }) @IsOptional() @IsIn(['fr', 'en']) locale?: string;
}

export class PreferencesDto {
  @IsOptional() @IsIn(SELF_LEVELS) selfLevel?: string;
  @IsOptional() @IsIn(JLPT_LEVELS) targetLevel?: string;
  @IsOptional() @ValidateIf((_, v) => v !== null) @IsISO8601() examDate?: string | null;
  @IsOptional() @IsInt() @Min(5) @Max(240) minutesPerDay?: number;
  @IsOptional() @IsArray() @IsIn(DIFFICULT_AREAS, { each: true }) difficultAreas?: string[];
  @IsOptional() @IsString() @Length(1, 64) timezone?: string;
  @IsOptional() @IsBoolean() showFurigana?: boolean;
  @IsOptional() @IsIn(['system', 'light', 'dark']) theme?: string;
  @IsOptional() @IsBoolean() reducedMotion?: boolean;
  @IsOptional() @IsIn(['fr', 'en']) locale?: string;
  @IsOptional() @IsString() @Length(1, 40) displayName?: string;
}

export class DeleteAccountDto {
  @ApiProperty({ description: 'Mot de passe (confirmation)' }) @IsString() @Length(1, 128) password: string;
}
