import { Body, Controller, Delete, Get, HttpCode, Param, ParseUUIDPipe, Post } from '@nestjs/common';
import { ApiPropertyOptional, ApiTags } from '@nestjs/swagger';
import { SkipThrottle } from '@nestjs/throttler';
import { IsOptional, IsString, IsUUID, Matches } from 'class-validator';
import { AuthUser, CurrentUser } from '../common/decorators';
import { FriendsService } from './friends.service';

class FriendRequestBody {
  @ApiPropertyOptional({ description: 'Code de duelliste (KQ-XXXXXX)' })
  @IsOptional() @IsString() @Matches(/^(KQ-?)?[A-Z0-9]{6}$/i, { message: 'Code de duelliste invalide.' })
  code?: string;
  @ApiPropertyOptional() @IsOptional() @IsUUID() userId?: string;
}

@ApiTags('friends')
@Controller('friends')
export class FriendsController {
  constructor(private friends: FriendsService) {}

  @Get() list(@CurrentUser() u: AuthUser) {
    return this.friends.list(u.id);
  }

  /** Demandes reçues (sondé régulièrement par l'application) */
  @SkipThrottle() @Get('requests') requests(@CurrentUser() u: AuthUser) {
    return this.friends.requests(u.id);
  }

  @Post() @HttpCode(201) request(@CurrentUser() u: AuthUser, @Body() dto: FriendRequestBody) {
    return this.friends.request(u.id, dto);
  }

  @Post(':id/accept') @HttpCode(200) accept(@CurrentUser() u: AuthUser, @Param('id', ParseUUIDPipe) id: string) {
    return this.friends.accept(u.id, id);
  }

  @Delete(':id') remove(@CurrentUser() u: AuthUser, @Param('id', ParseUUIDPipe) id: string) {
    return this.friends.remove(u.id, id);
  }
}
