import { Injectable, NotFoundException } from '@nestjs/common';
import { readFileSync } from 'fs';
import { resolve } from 'path';
import { EngineItem, createRng, masteryOf, masteryScore, planCharacterPractice } from '@koto/learning-engine';
import { languageOfLevel, type CharacterDto, type CharactersDto, type SessionDto, type StudyLanguage } from '@koto/shared';
import { PrismaService } from '../common/prisma.service';
import { ClockService } from '../common/clock.service';
import { LearningService } from '../learning/learning.service';
import { toEngineItem } from '../content/content.service';
import { toCardState } from '../learning/card-mapper';

interface CharactersJson {
  contentVersion: string;
  language?: StudyLanguage;
  notice?: string;
  sections: { slug: string; glyph?: string; title: string; description: string; groups: { slug: string; title: string; items: { slug: string }[] }[] }[];
}

/** Le catalogue (ordre, groupes) vient des fichiers de contenu (un par langue) ; les notions et la maîtrise de la base. */
const CATALOG_PATHS: Record<StudyLanguage, string | null> = {
  ja: resolve(__dirname, '../../../../content/characters/characters.json'),
  ko: resolve(__dirname, '../../../../content/characters/hangul.json'),
  // L'anglais s'écrit avec l'alphabet latin : pas d'onglet d'écriture
  en: null,
};

@Injectable()
export class CharactersService {
  private catalogs = new Map<StudyLanguage, CharactersJson>();

  constructor(private prisma: PrismaService, private clock: ClockService, private learning: LearningService) {}

  private load(lang: StudyLanguage): CharactersJson {
    let c = this.catalogs.get(lang);
    if (!c) {
      const path = CATALOG_PATHS[lang];
      c = path ? (JSON.parse(readFileSync(path, 'utf8')) as CharactersJson) : { contentVersion: '', language: lang, sections: [] };
      this.catalogs.set(lang, c);
    }
    return c;
  }

  private async context(userId: string) {
    const prefs = await this.prisma.userPreferences.findUnique({ where: { userId }, select: { targetLevel: true } });
    const catalog = this.load(languageOfLevel(prefs?.targetLevel));
    const slugs = catalog.sections.flatMap((s) => s.groups.flatMap((g) => g.items.map((i) => i.slug)));
    const items = await this.prisma.learningItem.findMany({ where: { slug: { in: slugs } }, include: { kanji: true } });
    const bySlug = new Map(items.map((i) => [i.slug, i]));
    const cards = await this.prisma.reviewCard.findMany({ where: { userId, itemId: { in: items.map((i) => i.id) } } });
    const cardByItem = new Map(cards.map((c) => [c.itemId, toCardState(c)]));
    return { catalog, bySlug, cardByItem };
  }

  async overview(userId: string): Promise<CharactersDto> {
    const { catalog, bySlug, cardByItem } = await this.context(userId);
    const now = this.clock.now();
    return {
      notice: catalog.notice ?? null,
      sections: catalog.sections.map((s) => {
        let learned = 0, mastered = 0, due = 0, total = 0;
        const groups = s.groups.map((g) => ({
          slug: g.slug,
          title: g.title,
          items: g.items
            .map((ci) => bySlug.get(ci.slug))
            .filter((i): i is NonNullable<typeof i> => !!i)
            .map((i): CharacterDto => {
              const card = cardByItem.get(i.id);
              const m = card ? masteryOf(card, now) : null;
              total++;
              if (card) learned++;
              if (m === 'mastered') mastered++;
              if (card && card.state !== 'new' && card.due <= now) due++;
              return {
                id: i.id,
                kind: i.kind as 'kana' | 'kanji',
                front: i.front,
                reading: i.reading,
                romaji: i.romaji,
                meaning: i.meaning,
                kanji: i.kanji ? { onyomi: i.kanji.onyomi, kunyomi: i.kanji.kunyomi, strokes: i.kanji.strokes } : null,
                mastery: m,
                score: card ? masteryScore(card, now) : 0,
              };
            }),
        }));
        return { slug: s.slug, glyph: s.glyph, title: s.title, description: s.description, learned, mastered, due, total, groups };
      }),
    };
  }

  /** scope : une section (hiragana, katakana, kanji) ou un groupe (ex. hira-k). */
  async practice(userId: string, scope: string): Promise<SessionDto> {
    const { catalog, bySlug, cardByItem } = await this.context(userId);
    const section = catalog.sections.find((s) => s.slug === scope || s.groups.some((g) => g.slug === scope));
    if (!section) throw new NotFoundException('Ensemble de caractères inconnu.');
    const groups = section.slug === scope ? section.groups : section.groups.filter((g) => g.slug === scope);
    const toEntries = (gs: typeof groups) =>
      gs.flatMap((g) => g.items.map((ci) => bySlug.get(ci.slug)).filter((i): i is NonNullable<typeof i> => !!i));
    const pool: EngineItem[] = toEntries(section.groups).map(toEngineItem);
    const entries = toEntries(groups).map((i) => ({ item: toEngineItem(i), card: cardByItem.get(i.id) ?? null }));
    const now = this.clock.now();
    const plan = planCharacterPractice(entries, pool, now, createRng(`${userId}:${scope}:${now.getTime()}`));
    if (!plan.questions.length) return { sessionId: '', questions: [] };
    const session = await this.prisma.learningSession.create({ data: { userId, kind: 'characters' } });
    return { sessionId: session.id, questions: await this.learning.issue(userId, session.id, 'practice', plan.questions) };
  }
}
