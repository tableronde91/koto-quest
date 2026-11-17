import story from '../../../content/story/story.json';

/** Mode histoire (même source que le web : content/story/story.json). L'appli mobile est en français. */
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
  return s ? { glyph: s.glyph, jp: s.jp, color: s.color, title: s.saga.fr, hero: s.hero.fr, short: s.short.fr, prologue: s.prologue.fr, epilogue: s.epilogue.fr } : null;
}

export function storyChapter(worldSlug: string) {
  for (const s of Object.values(LEVELS)) {
    const c = s.chapters[worldSlug];
    if (c) return { title: c.title.fr, intro: c.intro.fr, outro: c.outro.fr };
  }
  return null;
}
