import { Injectable, NotFoundException } from '@nestjs/common';
import { readFileSync } from 'fs';
import { resolve } from 'path';
import { createRng, masteryOf, masteryScore, planCharacterPractice, type EngineItem } from '@koto/learning-engine';
import type { ExpressionDto, ExpressionRegister, ExpressionsDto, SessionDto } from '@koto/shared';
import { PrismaService } from '../common/prisma.service';
import { ClockService } from '../common/clock.service';
import { LearningService } from '../learning/learning.service';
import { toEngineItem } from '../content/content.service';
import { toCardState } from '../learning/card-mapper';

interface ExpressionsJson {
  notice?: string;
  themes: { slug: string; glyph: string; title: string; description: string; expressions: { slug: string; note: string; register: ExpressionRegister; example?: { jp: string; fr: string } }[] }[];
}

/** Le recueil (thèmes, notes d'usage, exemples) vient du fichier de contenu ; les notions et la maîtrise de la base. */
const CATALOG_PATH = resolve(__dirname, '../../../../content/expressions/expressions.json');

@Injectable()
export class ExpressionsService {
  private catalog: ExpressionsJson | null = null;

  constructor(private prisma: PrismaService, private clock: ClockService, private learning: LearningService) {}

  private load(): ExpressionsJson {
    this.catalog ??= JSON.parse(readFileSync(CATALOG_PATH, 'utf8')) as ExpressionsJson;
    return this.catalog;
  }

  private async context(userId: string) {
    const catalog = this.load();
    const slugs = catalog.themes.flatMap((t) => t.expressions.map((e) => e.slug));
    const items = await this.prisma.learningItem.findMany({ where: { slug: { in: slugs } } });
    const bySlug = new Map(items.map((i) => [i.slug, i]));
    const cards = await this.prisma.reviewCard.findMany({ where: { userId, itemId: { in: items.map((i) => i.id) } } });
    const cardByItem = new Map(cards.map((c) => [c.itemId, toCardState(c)]));
    return { catalog, bySlug, cardByItem };
  }

  async overview(userId: string): Promise<ExpressionsDto> {
    const { catalog, bySlug, cardByItem } = await this.context(userId);
    const now = this.clock.now();
    return {
      notice: catalog.notice ?? null,
      themes: catalog.themes.map((t) => {
        let learned = 0, mastered = 0, due = 0, total = 0;
        const expressions = t.expressions.flatMap((e): ExpressionDto[] => {
          const i = bySlug.get(e.slug);
          if (!i) return [];
          const card = cardByItem.get(i.id);
          const m = card ? masteryOf(card, now) : null;
          total++;
          if (card) learned++;
          if (m === 'mastered') mastered++;
          if (card && card.state !== 'new' && card.due <= now) due++;
          return [{ id: i.id, front: i.front, reading: i.reading, romaji: i.romaji, meaning: i.meaning, note: e.note, register: e.register, example: e.example ?? null, mastery: m, score: card ? masteryScore(card, now) : 0 }];
        });
        return { slug: t.slug, glyph: t.glyph, title: t.title, description: t.description, learned, mastered, due, total, expressions };
      }),
    };
  }

  /** Entraînement sur un thème : révisions dues d'abord, puis nouvelles expressions (5 au plus). */
  async practice(userId: string, theme: string): Promise<SessionDto> {
    const { catalog, bySlug, cardByItem } = await this.context(userId);
    const t = catalog.themes.find((x) => x.slug === theme);
    if (!t) throw new NotFoundException('Thème d’expressions inconnu.');
    const rows = (slugs: string[]) => slugs.map((s) => bySlug.get(s)).filter((i): i is NonNullable<typeof i> => !!i);
    // Distracteurs : toutes les expressions (même registre de langue que les réponses)
    const pool: EngineItem[] = rows(catalog.themes.flatMap((x) => x.expressions.map((e) => e.slug))).map(toEngineItem);
    const entries = rows(t.expressions.map((e) => e.slug)).map((i) => ({ item: toEngineItem(i), card: cardByItem.get(i.id) ?? null }));
    const now = this.clock.now();
    const plan = planCharacterPractice(entries, pool, now, createRng(`${userId}:expr:${theme}:${now.getTime()}`), { maxItems: 8, maxNew: 5 });
    if (!plan.questions.length) return { sessionId: '', questions: [] };
    const session = await this.prisma.learningSession.create({ data: { userId, kind: 'expressions' } });
    return { sessionId: session.id, questions: await this.learning.issue(userId, session.id, 'practice', plan.questions) };
  }
}
