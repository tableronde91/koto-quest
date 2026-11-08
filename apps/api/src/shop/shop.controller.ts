import { Body, Controller, Get, HttpCode, Post, Put } from '@nestjs/common';
import { ApiProperty, ApiTags } from '@nestjs/swagger';
import { IsObject, IsString, Length } from 'class-validator';
import { AuthUser, CurrentUser } from '../common/decorators';
import { ShopService } from './shop.service';

class AcquireDto {
  @ApiProperty() @IsString() @Length(2, 60) sku: string;
}
class AvatarDto {
  @ApiProperty({ description: 'AvatarConfig' }) @IsObject() avatar: Record<string, unknown>;
}

@ApiTags('personnage')
@Controller()
export class ShopController {
  constructor(private shop: ShopService) {}

  @Get('shop') get(@CurrentUser() u: AuthUser) {
    return this.shop.shop(u.id);
  }

  @Post('shop/acquire') @HttpCode(200) acquire(@CurrentUser() u: AuthUser, @Body() dto: AcquireDto) {
    return this.shop.acquire(u.id, dto.sku);
  }

  @Put('me/avatar') avatar(@CurrentUser() u: AuthUser, @Body() dto: AvatarDto) {
    return this.shop.saveAvatar(u.id, dto.avatar);
  }
}
