import { HttpException, Injectable } from '@nestjs/common';
import { readFileSync } from 'fs';
import { resolve } from 'path';
import { readingReward } from '@koto/learning-engine';
import { ReadingError, readingChapter, readingGrade, readingOverview, readingResult, type ReadingCatalog, type ReadingChapterDto, type ReadingOverviewDto, type ReadingResultDto } from '@koto/shared';
import { PrismaService } from '../common/prisma.service';
import { ActivityService } from '../learning/activity.service';

const CATALOG_PATH = resolve(__dirname, '../../../../content/reading/stories.json');

/** Lecture quotidienne : contes en feuilleton, un nouveau chapitre par jour (logique commune dans @koto/shared). */
@Injectable()
export class ReadingService {
  private catalog: ReadingCatalog | null = null;

  constructor(private prisma: PrismaService, private activity: ActivityService) {}

  private load(): ReadingCatalog {
    this.catalog ??= JSON.parse(readFileSync(CATALOG_PATH, 'utf8')) as ReadingCatalog;
    return this.catalog;
  }

  private async state(userId: string) {
    const [logs, today] = await Promise.all([this.prisma.readingLog.findMany({ where: { userId } }), this.activity.todayKey(userId)]);
    return { logs, today };
  }

  private run<T>(fn: () => T): T {
    try {
      return fn();
    } catch (e) {
      if (e instanceof ReadingError) throw new HttpException(e.message, e.status);
      throw e;
    }
  }

  async overview(userId: string): Promise<ReadingOverviewDto> {
    const { logs, today } = await this.state(userId);
    return readingOverview(this.load(), logs, today);
  }

  async chapter(userId: string, slug: string): Promise<ReadingChapterDto> {
    const { logs, today } = await this.state(userId);
    return this.run(() => readingChapter(this.load(), logs, today, slug));
  }

  async complete(userId: string, slug: string, answers: number[], seconds = 0): Promise<ReadingResultDto> {
    const { logs, today } = await this.state(userId);
    const graded = this.run(() => readingGrade(this.load(), logs, today, slug, answers));
    let firstTime = false;
    if (graded.log) {
      // Insertion unique : deux validations simultanées ne récompensent qu'une fois.
      const created = await this.prisma.readingLog.createMany({
        data: [{ userId, ...graded.log, seconds: Math.max(0, Math.min(3600, Math.round(seconds))) }],
        skipDuplicates: true,
      });
      firstTime = created.count === 1;
      if (firstTime) {
        const reward = readingReward(graded.correct, graded.total);
        await this.prisma.user.update({ where: { id: userId }, data: { coins: { increment: reward.coins } } });
        await this.activity.addXp(userId, reward.xp, 'reading', slug);
        await this.activity.record(userId, { seconds: Math.min(3600, seconds), xp: reward.xp });
      }
    }
    const after = firstTime ? [...logs, graded.log!] : logs;
    return readingResult(this.load(), after, today, slug, graded.correct, firstTime);
  }
}
