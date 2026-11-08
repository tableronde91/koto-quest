import { ApiPropertyOptional, ApiProperty } from '@nestjs/swagger';
import { Type } from 'class-transformer';
import { ArrayMaxSize, IsArray, IsBoolean, IsIn, IsInt, IsISO8601, IsOptional, IsString, IsUrl, Max, MaxLength, Min, ValidateIf, ValidateNested } from 'class-validator';

export class NotificationPrefsInput {
  @ApiPropertyOptional() @IsOptional() @IsBoolean() consent?: boolean;
  @ApiPropertyOptional() @IsOptional() @IsBoolean() enabled?: boolean;
  @ApiPropertyOptional() @IsOptional() @IsIn(['calm', 'normal', 'intense', 'custom']) mode?: string;
  @ApiPropertyOptional() @IsOptional() @IsArray() @ArrayMaxSize(10) @IsInt({ each: true }) @Min(0, { each: true }) @Max(1439, { each: true }) customTimes?: number[];
  @ApiPropertyOptional() @IsOptional() @IsInt() @Min(0) @Max(1439) windowStart?: number;
  @ApiPropertyOptional() @IsOptional() @IsInt() @Min(1) @Max(1440) windowEnd?: number;
  @ApiPropertyOptional() @IsOptional() @ValidateIf((_, v) => v !== null) @IsInt() @Min(0) @Max(1439) quietStart?: number | null;
  @ApiPropertyOptional() @IsOptional() @ValidateIf((_, v) => v !== null) @IsInt() @Min(0) @Max(1439) quietEnd?: number | null;
  @ApiPropertyOptional({ description: 'Pause jusqu’à cette date (null pour reprendre)' }) @IsOptional() @ValidateIf((_, v) => v !== null) @IsISO8601() pausedUntil?: string | null;
}

class PushKeys {
  @IsString() @MaxLength(200) p256dh: string;
  @IsString() @MaxLength(100) auth: string;
}

export class PushSubscriptionInput {
  @ApiProperty() @IsUrl({ protocols: ['https'], require_tld: false }) @MaxLength(1000) endpoint: string;
  @ApiProperty() @ValidateNested() @Type(() => PushKeys) keys: PushKeys;
}

export class UnsubscribeInput {
  @ApiProperty() @IsString() @MaxLength(1000) endpoint: string;
}
