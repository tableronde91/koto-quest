import { ApiProperty } from '@nestjs/swagger';
import { IsDefined, IsInt, IsUUID, Max, Min } from 'class-validator';

export class AnswerDto {
  @ApiProperty({ description: 'Réponse : texte choisi, ou liste ordonnée (remise en ordre, association).' })
  @IsDefined({ message: 'Réponse manquante.' })
  answer: string | string[];

  @ApiProperty({ description: 'Temps de réponse en millisecondes' })
  @IsInt() @Min(0) @Max(3_600_000)
  responseMs: number;
}

export class CompleteLessonDto {
  @ApiProperty() @IsUUID() sessionId: string;
}
