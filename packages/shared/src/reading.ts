import { readingReward, readingStates, readingStreak, stripRuby } from '@koto/learning-engine';
import type {
  BiText,
  ReadingChapterDto,
  ReadingChapterRefDto,
  ReadingOverviewDto,
  ReadingResultDto,
  ReadingSentenceDto,
  ReadingStoryInfoDto,
  ReadingTitle,
  ReadingWordDto,
  StudyLanguage,
} from './index';
import { languageOfLevel } from './languages';

/**
 * Lecture : logique commune au serveur et à la version hors ligne. Tous les chapitres sont ouverts dès le départ ;
 * le « chapitre du jour » n'est qu'un conseil (le premier pas encore lu).
 * Le catalogue vient de content/reading/stories.json ; les lectures de l'utilisateur sont passées en entrée.
 */
export interface ReadingCatalog {
  notice: BiText;
  stories: (ReadingStoryInfoDto & {
    chapters: { slug: string; title: ReadingTitle; paragraphs: ReadingSentenceDto[][]; words: ReadingWordDto[]; questions: { q: BiText; choices: BiText[]; answer: number }[] }[];
  })[];
}

export interface ReadingLogRow {
  chapter: string;
  dateKey: string;
  correct: number;
  total: number;
}

export class ReadingError extends Error {
  constructor(public status: 400 | 403 | 404, message: string) {
    super(message);
  }
}

type Story = ReadingCatalog['stories'][number];
type Chapter = Story['chapters'][number] & { day: number; story: Story; index: number; chars: number; sentences: number };

const indexes = new WeakMap<ReadingCatalog, Chapter[]>();
function chaptersOf(catalog: ReadingCatalog): Chapter[] {
  let list = indexes.get(catalog);
  if (!list) {
    let day = 0;
    list = catalog.stories.flatMap((story) =>
      story.chapters.map((c, index) => {
        const all = c.paragraphs.flat();
        return { ...c, day: ++day, story, index, sentences: all.length, chars: all.reduce((n, s) => n + stripRuby(s.jp).length, 0) };
      }),
    );
    indexes.set(catalog, list);
  }
  return list;
}

const info = (s: Story): ReadingStoryInfoDto => ({ slug: s.slug, glyph: s.glyph, level: s.level, color: s.color, title: s.title, summary: s.summary });

function context(catalog: ReadingCatalog, logs: readonly ReadingLogRow[]) {
  const chapters = chaptersOf(catalog);
  const states = readingStates(chapters.map((c) => c.slug), logs);
  const byChapter = new Map(logs.map((l) => [l.chapter, l]));
  const ref = (c: Chapter): ReadingChapterRefDto => ({
    slug: c.slug,
    day: c.day,
    title: c.title,
    state: states.get(c.slug)!,
    sentences: c.sentences,
    chars: c.chars,
    correct: byChapter.get(c.slug)?.correct ?? null,
    total: c.questions.length,
  });
  const find = (slug: string) => {
    const c = chapters.find((x) => x.slug === slug);
    if (!c) throw new ReadingError(404, 'Chapitre introuvable.');
    return c;
  };
  return { chapters, states, byChapter, ref, find };
}

export function readingOverview(catalog: ReadingCatalog, logs: readonly ReadingLogRow[], today: string): ReadingOverviewDto {
  const { chapters, ref } = context(catalog, logs);
  const read = new Set(logs.map((l) => l.chapter));
  const readToday = new Set(logs.filter((l) => l.dateKey === today).map((l) => l.chapter));
  // Chapitre conseillé : le premier pas encore lu. Une fois la lecture du jour faite, on montre ce qui vient d'être lu
  // et on propose la suite (`upcoming`), que le lecteur peut ouvrir tout de suite s'il en a envie.
  const unread = chapters.filter((c) => !read.has(c.slug));
  const lastToday = chapters.filter((c) => readToday.has(c.slug)).at(-1);
  const todayChapter = lastToday ?? unread[0] ?? null;
  const upcoming = lastToday ? unread[0] : unread[1];
  const streak = readingStreak(logs.map((l) => l.dateKey), today);
  return {
    notice: catalog.notice,
    today: { state: lastToday ? 'done' : unread.length ? 'new' : 'finished', chapter: todayChapter ? ref(todayChapter) : null, story: todayChapter ? info(todayChapter.story) : null },
    upcoming: upcoming ? { ...ref(upcoming), story: info(upcoming.story) } : null,
    streak: streak.current,
    bestStreak: streak.best,
    chaptersRead: read.size,
    charsRead: chapters.filter((c) => read.has(c.slug)).reduce((n, c) => n + c.chars, 0),
    totalChapters: chapters.length,
    stories: catalog.stories.map((s) => {
      const list = chapters.filter((c) => c.story === s).map(ref);
      return { ...info(s), chapters: list, read: list.filter((c) => c.state === 'read').length };
    }),
  };
}

export function readingChapter(catalog: ReadingCatalog, logs: readonly ReadingLogRow[], today: string, slug: string): ReadingChapterDto {
  const { chapters, states, byChapter, find } = context(catalog, logs);
  const c = find(slug);
  const state = states.get(slug)!;
  const i = chapters.indexOf(c);
  const next = chapters[i + 1];
  const log = byChapter.get(slug);
  return {
    story: info(c.story),
    chapter: {
      slug: c.slug,
      day: c.day,
      index: c.index + 1,
      count: c.story.chapters.length,
      title: c.title,
      paragraphs: c.paragraphs,
      words: c.words,
      questions: c.questions.map(({ q, choices }) => ({ q, choices })),
    },
    state,
    previous: i > 0 ? chapters[i - 1].slug : null,
    next: next ? { slug: next.slug, state: states.get(next.slug)! } : null,
    result: log ? { correct: log.correct, total: log.total, answers: c.questions.map((q) => q.answer) } : null,
  };
}

/** Corrige les réponses ; `log` est la lecture à enregistrer si c'est la première fois (sinon null). */
export function readingGrade(catalog: ReadingCatalog, logs: readonly ReadingLogRow[], today: string, slug: string, answers: readonly number[]) {
  const { states, find } = context(catalog, logs);
  const c = find(slug);
  if (answers.length !== c.questions.length) throw new ReadingError(400, 'Réponds à toutes les questions.');
  const state = states.get(slug)!;
  const correct = c.questions.reduce((n, q, i) => n + (answers[i] === q.answer ? 1 : 0), 0);
  const log: ReadingLogRow | null = state === 'available' ? { chapter: slug, dateKey: today, correct, total: c.questions.length } : null;
  return { correct, total: c.questions.length, log };
}

/** Résultat renvoyé au lecteur, une fois la lecture éventuellement enregistrée. */
export function readingResult(catalog: ReadingCatalog, logsAfter: readonly ReadingLogRow[], today: string, slug: string, correct: number, firstTime: boolean): ReadingResultDto {
  const { chapters, states, find } = context(catalog, logsAfter);
  const c = find(slug);
  const reward = firstTime ? readingReward(correct, c.questions.length) : { xp: 0, coins: 0 };
  const next = chapters[chapters.indexOf(c) + 1];
  return {
    correct,
    total: c.questions.length,
    answers: c.questions.map((q) => q.answer),
    firstTime,
    xpGained: reward.xp,
    coinsGained: reward.coins,
    streak: readingStreak(logsAfter.map((l) => l.dateKey), today).current,
    next: next ? { slug: next.slug, title: next.title, state: states.get(next.slug)! } : null,
  };
}

const byLanguage = new WeakMap<ReadingCatalog, Map<string, ReadingCatalog>>();
/** Contes d'une langue (le niveau du conte dit sa langue : N5…N1 japonais, TOPIK1… coréen). Résultat mis en cache. */
export function readingCatalogFor(catalog: ReadingCatalog, lang: StudyLanguage): ReadingCatalog {
  let m = byLanguage.get(catalog);
  if (!m) byLanguage.set(catalog, (m = new Map()));
  let c = m.get(lang);
  if (!c) {
    const notice = (catalog as ReadingCatalog & { notices?: Partial<Record<StudyLanguage, BiText>> }).notices?.[lang] ?? catalog.notice;
    c = { ...catalog, notice, stories: catalog.stories.filter((s) => languageOfLevel(s.level) === lang) };
    m.set(lang, c);
  }
  return c;
}
