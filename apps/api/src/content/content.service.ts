import { ForbiddenException, Injectable, NotFoundException } from '@nestjs/common';
import { EngineItem, ItemKind, exampleIndex, focusedPool, masteryOf } from '@koto/learning-engine';
import type { JlptCode, LessonDto, LessonStatus, PathDto, SelfLevel } from '@koto/shared';
import { PrismaService } from '../common/prisma.service';
import { ClockService } from '../common/clock.service';
import { toCardState } from '../learning/card-mapper';

/** Monde de départ selon le niveau déclaré à l'onboarding (en attendant le test de positionnement). */
export function startWorldOrder(selfLevel: string, levelCode = 'N5'): number {
  // Seul le N5 commence par les kana : les autres niveaux s'ouvrent toujours au premier monde.
  if (levelCode !== 'N5') return 1;
  return (['kana', 'basics', 'n5', 'n4plus'] as SelfLevel[]).includes(selfLevel as SelfLevel) ? 3 : 1;
}

interface SequenceEntry {
  lessonId: string;
  slug: string;
  title: string;
  worldOrder: number;
  worldTitle: string;
}

@Injectable()
export class ContentService {
  private poolCache = new Map<string, { at: number; items: EngineItem[] }>();

  constructor(private prisma: PrismaService, private clock: ClockService) {}

  private exampleCache = new Map<string, { at: number; map: Map<string, string> }>();

  /** Phrase d'exemple (tirée des leçons du niveau) pour chaque notion en kanji : questions au format JLPT. */
  async examples(levelCode: string): Promise<Map<string, string>> {
    const cached = this.exampleCache.get(levelCode);
    if (cached && Date.now() - cached.at < 5 * 60_000) return cached.map;
    const [rows, items] = await Promise.all([
      this.prisma.example.findMany({ where: { lesson: { chapter: { world: { levelCode } } } }, select: { jp: true } }),
      this.enginePool(levelCode),
    ]);
    const map = exampleIndex(items, rows.map((r) => r.jp));
    this.exampleCache.set(levelCode, { at: Date.now(), map });
    return map;
  }

  /** Notions d'un niveau au format du moteur (sert à générer des distracteurs). */
  async enginePool(levelCode: string): Promise<EngineItem[]> {
    const cached = this.poolCache.get(levelCode);
    if (cached && Date.now() - cached.at < 5 * 60_000) return cached.items;
    const rows = await this.prisma.learningItem.findMany({ where: { levelCode } });
    const items = rows.map(toEngineItem);
    this.poolCache.set(levelCode, { at: Date.now(), items });
    return items;
  }

  /** Réserve de distracteurs centrée sur un monde (voir focusedPool). */
  async worldPool(worldId: string, levelCode: string): Promise<EngineItem[]> {
    const key = `world:${worldId}`;
    const cached = this.poolCache.get(key);
    if (cached && Date.now() - cached.at < 5 * 60_000) return cached.items;
    const rows = await this.prisma.learningItem.findMany({ where: { lessons: { some: { lesson: { chapter: { worldId } } } } } });
    const items = focusedPool(rows.map(toEngineItem), await this.enginePool(levelCode));
    this.poolCache.set(key, { at: Date.now(), items });
    return items;
  }

  /** Leçons du niveau dans l'ordre pédagogique. */
  async lessonSequence(levelCode: string): Promise<SequenceEntry[]> {
    const worlds = await this.prisma.world.findMany({
      where: { levelCode },
      orderBy: { order: 'asc' },
      include: { chapters: { orderBy: { order: 'asc' }, include: { lessons: { orderBy: { order: 'asc' } } } } },
    });
    return worlds.flatMap((w) =>
      w.chapters.flatMap((c) => c.lessons.map((l) => ({ lessonId: l.id, slug: l.slug, title: l.title, worldOrder: w.order, worldTitle: w.title }))),
    );
  }

  /** Statut de chaque leçon : déblocage séquentiel à partir du monde de départ de l'utilisateur. */
  async lessonStatuses(userId: string, levelCode: string): Promise<{ seq: SequenceEntry[]; status: Map<string, LessonStatus> }> {
    const [seq, prefs, progress] = await Promise.all([
      this.lessonSequence(levelCode),
      this.prisma.userPreferences.findUnique({ where: { userId } }),
      this.prisma.userLessonProgress.findMany({ where: { userId } }),
    ]);
    const prog = new Map(progress.map((p) => [p.lessonId, p.status]));
    const start = startWorldOrder(prefs?.selfLevel ?? 'beginner', levelCode);
    let startIdx = seq.findIndex((s) => s.worldOrder >= start);
    if (startIdx < 0) startIdx = 0;
    const status = new Map<string, LessonStatus>();
    seq.forEach((s, i) => {
      const p = prog.get(s.lessonId);
      if (p === 'completed') status.set(s.lessonId, 'completed');
      else if (p === 'in_progress') status.set(s.lessonId, 'in_progress');
      else if (i <= startIdx || prog.get(seq[i - 1]?.lessonId) === 'completed') status.set(s.lessonId, 'available');
      else status.set(s.lessonId, 'locked');
    });
    return { seq, status };
  }

  async nextRecommendedLesson(userId: string, levelCode: string) {
    const { seq, status } = await this.lessonStatuses(userId, levelCode);
    const prefs = await this.prisma.userPreferences.findUnique({ where: { userId } });
    const start = startWorldOrder(prefs?.selfLevel ?? 'beginner', levelCode);
    const candidates = [...seq.filter((s) => s.worldOrder >= start), ...seq.filter((s) => s.worldOrder < start)];
    return candidates.find((s) => ['available', 'in_progress'].includes(status.get(s.lessonId)!)) ?? null;
  }

  /** Niveaux disponibles (du plus facile au plus difficile) avec la progression de l'utilisateur. */
  async levelsOverview(userId: string): Promise<PathDto['levels']> {
    const [levels, done] = await Promise.all([
      this.prisma.jlptLevel.findMany({ orderBy: { order: 'desc' }, include: { worlds: { include: { chapters: { include: { _count: { select: { lessons: true } } } } } } } }),
      this.prisma.userLessonProgress.findMany({ where: { userId, status: 'completed' }, include: { lesson: { select: { chapter: { select: { world: { select: { levelCode: true } } } } } } } }),
    ]);
    return levels
      .map((l) => ({
        code: l.code as JlptCode,
        title: l.title,
        lessons: l.worlds.reduce((n, w) => n + w.chapters.reduce((m, c) => m + c._count.lessons, 0), 0),
        completed: done.filter((d) => d.lesson.chapter.world.levelCode === l.code).length,
      }))
      .filter((l) => l.lessons > 0);
  }

  /**
   * Prochaine leçon conseillée : d'abord dans le niveau visé, puis dans les niveaux suivants
   * (N5 → N4 → …), enfin dans les niveaux plus faciles s'il en reste.
   */
  async nextLessonAnyLevel(userId: string, preferred: string) {
    const levels = await this.prisma.jlptLevel.findMany({ orderBy: { order: 'desc' }, select: { code: true, order: true } });
    const pref = levels.find((l) => l.code === preferred);
    const ordered = pref ? [pref, ...levels.filter((l) => l.order < pref.order), ...levels.filter((l) => l.order > pref.order).reverse()] : levels;
    for (const l of ordered) {
      const next = await this.nextRecommendedLesson(userId, l.code);
      if (next) return next;
    }
    return null;
  }

  async path(userId: string, levelCode: JlptCode): Promise<PathDto> {
    const level = await this.prisma.jlptLevel.findUnique({ where: { code: levelCode } });
    if (!level) throw new NotFoundException(`Le niveau ${levelCode} n’est pas encore disponible.`);
    const [worlds, { status }, prefs, bossResults, examAttempts] = await Promise.all([
      this.prisma.world.findMany({
        where: { levelCode },
        orderBy: { order: 'asc' },
        include: {
          chapters: {
            orderBy: { order: 'asc' },
            include: { lessons: { orderBy: { order: 'asc' }, include: { _count: { select: { items: true } } } } },
          },
        },
      }),
      this.lessonStatuses(userId, levelCode),
      this.prisma.userPreferences.findUnique({ where: { userId } }),
      this.prisma.bossResult.findMany({ where: { userId } }),
      this.prisma.examAttempt.findMany({ where: { userId, finishedAt: { not: null } }, include: { exam: { select: { slug: true, title: true } } } }),
    ]);
    const start = startWorldOrder(prefs?.selfLevel ?? 'beginner', levelCode);
    const bossBy = new Map(bossResults.map((b) => [b.worldSlug, b]));
    return {
      level: { code: level.code as JlptCode, title: level.title, region: level.region, notice: level.notice },
      levels: await this.levelsOverview(userId),
      worlds: worlds.map((w) => {
        const lessons = w.chapters.flatMap((c) => c.lessons);
        return {
          slug: w.slug,
          order: w.order,
          title: w.title,
          description: w.description,
          comingSoon: lessons.length === 0 && !w.examSlug,
          optional: w.order < start,
          progress: { completed: lessons.filter((l) => status.get(l.id) === 'completed').length, total: lessons.length },
          boss: w.bossName
            ? {
                name: w.bossName,
                glyph: w.bossGlyph ?? '鬼',
                intro: w.bossIntro ?? '',
                available: lessons.length > 0 && lessons.every((l) => status.get(l.id) === 'completed'),
                defeated: !!bossBy.get(w.slug)?.firstVictoryAt,
                attempts: bossBy.get(w.slug)?.attempts ?? 0,
              }
            : null,
          exam: w.examSlug
            ? (() => {
                const att = examAttempts.filter((a) => a.exam.slug === w.examSlug);
                return {
                  slug: w.examSlug,
                  title: att[0]?.exam.title ?? 'Examen blanc',
                  attempts: att.length,
                  bestPercent: att.length ? Math.max(...att.map((a) => a.percent ?? 0)) : null,
                  passed: att.some((a) => a.passed),
                };
              })()
            : null,
          chapters: w.chapters.map((c) => ({
            slug: c.slug,
            title: c.title,
            lessons: c.lessons.map((l) => ({
              slug: l.slug,
              title: l.title,
              objective: l.objective,
              minutes: l.minutes,
              status: status.get(l.id) ?? 'locked',
              itemCount: l._count.items,
            })),
          })),
        };
      }),
    };
  }

  async lessonBySlug(slug: string) {
    const lesson = await this.prisma.lesson.findUnique({
      where: { slug },
      include: {
        chapter: { include: { world: true } },
        items: { orderBy: { order: 'asc' }, include: { item: { include: { kanji: true } } } },
        examples: { orderBy: { order: 'asc' } },
        exercises: { orderBy: { order: 'asc' } },
      },
    });
    if (!lesson) throw new NotFoundException('Leçon introuvable.');
    return lesson;
  }

  async assertUnlocked(userId: string, lessonId: string, levelCode: string): Promise<LessonStatus> {
    const { status } = await this.lessonStatuses(userId, levelCode);
    const s = status.get(lessonId) ?? 'locked';
    if (s === 'locked') throw new ForbiddenException('Cette leçon est encore verrouillée : termine d’abord la précédente.');
    return s;
  }

  async lessonDto(userId: string, slug: string): Promise<LessonDto> {
    const lesson = await this.lessonBySlug(slug);
    const levelCode = lesson.chapter.world.levelCode;
    const status = await this.assertUnlocked(userId, lesson.id, levelCode);
    const cards = await this.prisma.reviewCard.findMany({
      where: { userId, itemId: { in: lesson.items.map((i) => i.itemId) } },
    });
    const byItem = new Map(cards.map((c) => [c.itemId, c]));
    const now = this.clock.now();
    return {
      slug: lesson.slug,
      title: lesson.title,
      objective: lesson.objective,
      minutes: lesson.minutes,
      explanation: lesson.explanation as string[],
      status,
      world: { slug: lesson.chapter.world.slug, title: lesson.chapter.world.title },
      chapter: { slug: lesson.chapter.slug, title: lesson.chapter.title },
      examples: lesson.examples.map((e) => ({ jp: e.jp, reading: e.reading, fr: e.fr })),
      items: lesson.items.map(({ item }) => {
        const card = byItem.get(item.id);
        return {
          id: item.id,
          kind: item.kind as ItemKind,
          front: item.front,
          reading: item.reading,
          romaji: item.romaji,
          meaning: item.meaning,
          kanji: item.kanji ? { onyomi: item.kanji.onyomi, kunyomi: item.kanji.kunyomi, strokes: item.kanji.strokes } : null,
          mastery: card ? masteryOf(toCardState(card), now) : null,
        };
      }),
    };
  }
}

export function toEngineItem(row: { id: string; kind: string; front: string; reading: string | null; romaji: string | null; meaning: string }): EngineItem {
  return { id: row.id, kind: row.kind as ItemKind, front: row.front, reading: row.reading, romaji: row.romaji, meaning: row.meaning };
}
