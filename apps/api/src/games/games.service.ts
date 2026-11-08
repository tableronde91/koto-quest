import { BadRequestException, ConflictException, ForbiddenException, Injectable, NotFoundException } from '@nestjs/common';
import { DAILY_GAME_COIN_CAP, EngineItem, GAMES, GAME_IDS, GameDef, GameId, createRng, eligibleItems, focusedPool, gameReward, planTimedGame, scoreTimedGame } from '@koto/learning-engine';
import type { GameInfoDto, GameResultDto, GameStartDto, GamesDto } from '@koto/shared';
import { PrismaService } from '../common/prisma.service';
import { ClockService } from '../common/clock.service';
import { ContentService, toEngineItem } from '../content/content.service';
import { LearningService } from '../learning/learning.service';
import { ActivityService } from '../learning/activity.service';

@Injectable()
export class GamesService {
  constructor(
    private prisma: PrismaService,
    private clock: ClockService,
    private content: ContentService,
    private learning: LearningService,
    private activity: ActivityService,
  ) {}

  /** Notions déjà rencontrées par l'utilisateur. */
  private async seen(userId: string): Promise<EngineItem[]> {
    const cards = await this.prisma.reviewCard.findMany({ where: { userId, state: { not: 'new' } }, include: { item: true } });
    return cards.map((c) => toEngineItem(c.item));
  }

  private async coinsLeftToday(userId: string) {
    const day = await this.prisma.dailyActivity.findUnique({ where: { userId_dateKey: { userId, dateKey: await this.activity.todayKey(userId) } } });
    return Math.max(0, DAILY_GAME_COIN_CAP - (day?.gameCoins ?? 0));
  }

  private info(def: GameDef, seen: EngineItem[], result?: { bestScore: number; plays: number } | null): GameInfoDto {
    const n = eligibleItems(def, seen).length;
    return { id: def.id, title: def.title, description: def.description, durationSec: def.durationSec, minItems: def.minItems, seenItems: n, available: n >= def.minItems, bestScore: result?.bestScore ?? 0, plays: result?.plays ?? 0 };
  }

  private def(id: string): GameDef {
    if (!GAME_IDS.includes(id as GameId)) throw new NotFoundException('Mini-jeu inconnu.');
    return GAMES[id as GameId];
  }

  async overview(userId: string): Promise<GamesDto> {
    const [seen, results, left] = await Promise.all([this.seen(userId), this.prisma.gameResult.findMany({ where: { userId } }), this.coinsLeftToday(userId)]);
    const by = new Map(results.map((r) => [r.gameId, r]));
    return { games: GAME_IDS.map((id) => this.info(GAMES[id], seen, by.get(id))), coinsLeftToday: left };
  }

  async start(userId: string, id: string): Promise<GameStartDto> {
    const def = this.def(id);
    const seen = await this.seen(userId);
    const info = this.info(def, seen, await this.prisma.gameResult.findUnique({ where: { userId_gameId: { userId, gameId: id } } }));
    if (!info.available) throw new ForbiddenException(`Rencontre au moins ${def.minItems} notions adaptées dans tes leçons pour débloquer ${def.title}.`);
    const prefs = await this.prisma.userPreferences.findUnique({ where: { userId } });
    const pool = focusedPool(seen, await this.content.enginePool(prefs?.targetLevel ?? 'N5'));
    const questions = planTimedGame(def, seen, pool, createRng(`${userId}:${id}:${this.clock.now().getTime()}`));
    const session = await this.prisma.learningSession.create({ data: { userId, kind: 'game', scope: id, startedAt: this.clock.now() } });
    return { sessionId: session.id, game: info, questions: await this.learning.issue(userId, session.id, 'game', questions) };
  }

  /** Le score est recalculé à partir de l'heure d'enregistrement de chaque réponse côté serveur. */
  async finish(userId: string, id: string, sessionId: string): Promise<GameResultDto> {
    const def = this.def(id);
    const session = await this.prisma.learningSession.findFirst({ where: { id: sessionId, userId, kind: 'game', scope: id }, include: { questions: true } });
    if (!session) throw new NotFoundException('Partie introuvable.');
    if (session.endedAt) throw new ConflictException('Cette partie est déjà terminée.');
    const now = this.clock.now();
    const elapsed = now.getTime() - session.startedAt.getTime();
    const allAnswered = session.questions.every((q) => q.answeredAt);
    if (elapsed < def.durationSec * 1000 - 2000 && !allAnswered) throw new BadRequestException('La partie n’est pas terminée.');

    const { score, answered } = scoreTimedGame(
      def,
      session.questions.filter((q) => q.answeredAt).map((q) => ({ correct: !!q.correct, atMs: q.answeredAt!.getTime() - session.startedAt.getTime() })),
    );
    const left = await this.coinsLeftToday(userId);
    const reward = gameReward(score, DAILY_GAME_COIN_CAP - left);
    const previous = await this.prisma.gameResult.findUnique({ where: { userId_gameId: { userId, gameId: id } } });
    const bestScore = Math.max(previous?.bestScore ?? 0, score);
    const dateKey = await this.activity.todayKey(userId);
    await this.prisma.$transaction([
      this.prisma.learningSession.update({ where: { id: session.id }, data: { endedAt: now, xpEarned: reward.xp } }),
      this.prisma.gameResult.upsert({
        where: { userId_gameId: { userId, gameId: id } },
        create: { userId, gameId: id, plays: 1, bestScore, lastScore: score },
        update: { plays: { increment: 1 }, bestScore, lastScore: score },
      }),
      this.prisma.user.update({ where: { id: userId }, data: { coins: { increment: reward.coins } } }),
      this.prisma.dailyActivity.upsert({
        where: { userId_dateKey: { userId, dateKey } },
        create: { userId, dateKey, gameCoins: reward.coins, xp: reward.xp },
        update: { gameCoins: { increment: reward.coins }, xp: { increment: reward.xp } },
      }),
    ]);
    await this.activity.addXp(userId, reward.xp, `game_${id}`, session.id);
    return { score, answered, bestScore, newBest: score > 0 && score > (previous?.bestScore ?? 0), xpGained: reward.xp, coinsGained: reward.coins };
  }
}
