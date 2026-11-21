import { ConflictException, Injectable, NotFoundException } from '@nestjs/common';
import { AuthoredExercise, EngineItem, JLPT_DRILLS, JlptDrillPart, TOPIK_DRILLS, createRng, planJlptDrill } from '@koto/learning-engine';
import { languageOfLevel, levelsOfLanguage, type JlptDrillsDto, type SessionDto } from '@koto/shared';
import { PrismaService } from '../common/prisma.service';
import { ClockService } from '../common/clock.service';
import { ContentService, toEngineItem } from '../content/content.service';
import { LearningService } from '../learning/learning.service';

const MIN_QUESTIONS = 3;

/**
 * Atelier JLPT : séries d'entraînement par épreuve, au format de l'examen, construites uniquement
 * avec ce que l'utilisateur a déjà appris (notions en révision, exercices des leçons terminées).
 */
@Injectable()
export class JlptService {
  constructor(private prisma: PrismaService, private clock: ClockService, private content: ContentService, private learning: LearningService) {}

  /** Notions et exercices de la langue étudiée seulement. */
  private async material(userId: string) {
    const prefs = await this.prisma.userPreferences.findUnique({ where: { userId }, select: { targetLevel: true } });
    const lang = languageOfLevel(prefs?.targetLevel);
    const levelCode = { in: levelsOfLanguage(lang) };
    const [cards, done] = await Promise.all([
      this.prisma.reviewCard.findMany({ where: { userId, item: { levelCode } }, include: { item: true } }),
      this.prisma.userLessonProgress.findMany({ where: { userId, status: 'completed', lesson: { chapter: { world: { levelCode } } } }, include: { lesson: { include: { exercises: true } } } }),
    ]);
    const learned: EngineItem[] = cards.map((c) => toEngineItem(c.item));
    const levels = [...new Set(cards.map((c) => c.item.levelCode))];
    const pool: EngineItem[] = [];
    const examples = new Map<string, string>();
    for (const l of levels.length ? levels : [lang === 'ko' ? 'TOPIK1' : 'N5']) {
      pool.push(...(await this.content.enginePool(l)));
      for (const [k, v] of await this.content.examples(l)) examples.set(k, v);
    }
    const authored = done.flatMap((p) => p.lesson.exercises.map((e) => e.payload as unknown as AuthoredExercise));
    return { learned, pool, examples, authored, lang, drills: lang === 'ko' ? TOPIK_DRILLS : JLPT_DRILLS };
  }

  async drills(userId: string): Promise<JlptDrillsDto> {
    const m = await this.material(userId);
    const rng = createRng(`${userId}:jlpt-count`);
    return {
      minQuestions: MIN_QUESTIONS,
      drills: (Object.keys(m.drills) as JlptDrillPart[]).map((part) => ({
        part,
        ...m.drills[part]!,
        available: planJlptDrill(part, m.learned, m.authored, m.pool, rng, m.examples, m.lang).length,
      })),
    };
  }

  async start(userId: string, part: string): Promise<SessionDto> {
    const m = await this.material(userId);
    if (!(part in m.drills)) throw new NotFoundException('Épreuve inconnue.');
    const questions = planJlptDrill(part as JlptDrillPart, m.learned, m.authored, m.pool, createRng(`${userId}:jlpt:${part}:${this.clock.now().getTime()}`), m.examples, m.lang);
    if (questions.length < MIN_QUESTIONS) throw new ConflictException('Pas encore assez de notions pour cette épreuve : termine quelques leçons de plus.');
    const session = await this.prisma.learningSession.create({ data: { userId, kind: 'jlpt', scope: part } });
    return { sessionId: session.id, questions: await this.learning.issue(userId, session.id, 'practice', questions) };
  }
}
