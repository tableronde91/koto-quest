import { Injectable } from '@nestjs/common';

/** Horloge injectable : permet aux tests de « voyager dans le temps » pour vérifier les révisions. */
@Injectable()
export class ClockService {
  private offsetMs = 0;
  now(): Date {
    return new Date(Date.now() + this.offsetMs);
  }
  /** Réservé aux tests. */
  advance(ms: number) {
    this.offsetMs += ms;
  }
  reset() {
    this.offsetMs = 0;
  }
}
