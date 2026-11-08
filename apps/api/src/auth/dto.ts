import { ApiProperty } from '@nestjs/swagger';
import { IsEmail, IsString, Length, MaxLength, MinLength } from 'class-validator';
import { Transform } from 'class-transformer';

const lower = ({ value }: { value: unknown }) => (typeof value === 'string' ? value.trim().toLowerCase() : value);

export class RegisterDto {
  @ApiProperty() @Transform(lower) @IsEmail({}, { message: 'Adresse e-mail invalide.' }) @MaxLength(254) email: string;
  @ApiProperty({ minLength: 8 }) @IsString() @MinLength(8, { message: 'Le mot de passe doit contenir au moins 8 caractères.' }) @MaxLength(128) password: string;
  @ApiProperty() @IsString() @Length(1, 40, { message: 'Le pseudo doit contenir 1 à 40 caractères.' }) displayName: string;
}

export class LoginDto {
  @ApiProperty() @Transform(lower) @IsEmail({}, { message: 'Adresse e-mail invalide.' }) email: string;
  @ApiProperty() @IsString() @MaxLength(128) password: string;
}

export class ForgotPasswordDto {
  @ApiProperty() @Transform(lower) @IsEmail({}, { message: 'Adresse e-mail invalide.' }) email: string;
}

export class ResetPasswordDto {
  @ApiProperty() @IsString() @Length(10, 200) token: string;
  @ApiProperty() @IsString() @MinLength(8, { message: 'Le mot de passe doit contenir au moins 8 caractères.' }) @MaxLength(128) password: string;
}
