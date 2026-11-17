import story from '../../../../content/story/story.json';
import { locale } from '../i18n';

/** Mode histoire : une saga par niveau (content/story/story.json), un chapitre par île. */
interface Bi {
  fr: string;
  en: string;
}
interface RawChapter {
  title: Bi;
  intro: Bi;
  outro: Bi;
}
interface RawSaga {
  glyph: string;
  jp: string;
  color: string;
  saga: Bi;
  hero: Bi;
  short: Bi;
  prologue: Bi;
  epilogue: Bi;
  chapters: Record<string, RawChapter>;
}
export interface Saga {
  glyph: string;
  jp: string;
  color: string;
  title: string;
  hero: string;
  short: string;
  prologue: string;
  epilogue: string;
}
export interface StoryChapter {
  title: string;
  intro: string;
  outro: string;
}

const bi = (b: Bi) => (locale === 'en' ? b.en : b.fr);
const LEVELS = story.levels as Record<string, RawSaga>;

export function sagaFor(level: string): Saga | null {
  const s = LEVELS[level.toUpperCase()];
  if (!s) return null;
  return { glyph: s.glyph, jp: s.jp, color: s.color, title: bi(s.saga), hero: bi(s.hero), short: bi(s.short), prologue: bi(s.prologue), epilogue: bi(s.epilogue) };
}

export function storyChapter(worldSlug: string): StoryChapter | null {
  for (const s of Object.values(LEVELS)) {
    const c = s.chapters[worldSlug];
    if (c) return { title: bi(c.title), intro: bi(c.intro), outro: bi(c.outro) };
  }
  return null;
}
