import story from '../../../content/story/story.json';
import { bi } from './i18n';

/** Mode histoire (même source que le web : content/story/story.json). Texte dans la langue choisie. */
interface Bi {
  fr: string;
  en: string;
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
  chapters: Record<string, { title: Bi; intro: Bi; outro: Bi }>;
}
const LEVELS = story.levels as Record<string, RawSaga>;

export function sagaFor(level: string) {
  const s = LEVELS[level.toUpperCase()];
  return s ? { glyph: s.glyph, jp: s.jp, color: s.color, title: bi(s.saga), hero: bi(s.hero), short: bi(s.short), prologue: bi(s.prologue), epilogue: bi(s.epilogue) } : null;
}

export function storyChapter(worldSlug: string) {
  for (const s of Object.values(LEVELS)) {
    const c = s.chapters[worldSlug];
    if (c) return { title: bi(c.title), intro: bi(c.intro), outro: bi(c.outro) };
  }
  return null;
}
