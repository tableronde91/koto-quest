/**
 * Import du contenu pédagogique (content/<niveau>/*.json) dans la base.
 * Idempotent : upsert par slug. La progression des utilisateurs n'est jamais touchée.
 * Le contenu est validé avant import ; en cas d'erreur, rien n'est écrit.
 */
import 'dotenv/config';
import { readdirSync, readFileSync, statSync } from 'fs';
import { join, resolve } from 'path';
import { createHash } from 'crypto';
import { PrismaClient, Prisma } from '@prisma/client';
import { PrismaPg } from '@prisma/adapter-pg';
import { AuthoredExercise, EXAMS, validateAuthoredExercise } from '@koto/learning-engine';

interface ItemJson {
  slug: string;
  kind: 'kana' | 'vocabulary' | 'kanji' | 'grammar';
  front: string;
  reading?: string;
  romaji?: string;
  meaning: string;
  kanji?: { onyomi: string[]; kunyomi: string[]; strokes?: number };
}
interface LessonJson {
  slug: string;
  title: string;
  objective: string;
  minutes: number;
  explanation: string[];
  items: ItemJson[];
  examples: { jp: string; reading?: string; fr: string }[];
  exercises: AuthoredExercise[];
}
interface LevelJson {
  contentVersion: string;
  notice?: string;
  level: { code: string; title: string; region: string; order: number };
  worlds: { slug: string; title: string; region: string; description: string; boss?: { name: string; glyph: string; intro: string }; exam?: string; chapters: { slug: string; title: string; lessons: LessonJson[] }[] }[];
}

export function validateLevel(data: LevelJson): string[] {
  const errors: string[] = [];
  const slugs = new Set<string>();
  const items = new Map<string, ItemJson>();
  const unique = (slug: string, where: string) => {
    if (slugs.has(slug)) errors.push(`${where} : slug en double « ${slug} »`);
    slugs.add(slug);
  };
  for (const w of data.worlds) {
    unique(w.slug, 'monde');
    for (const c of w.chapters) {
      unique(c.slug, 'chapitre');
      for (const l of c.lessons) {
        unique(l.slug, 'leçon');
        if (!l.items.length) errors.push(`${l.slug} : aucune notion`);
        if (l.minutes < 3 || l.minutes > 15) errors.push(`${l.slug} : durée hors de la plage 3–15 min`);
        for (const it of l.items) {
          if (!it.front?.trim() || !it.meaning?.trim()) errors.push(`${it.slug} : champs front/meaning requis`);
          const prev = items.get(it.slug);
          if (prev && JSON.stringify(prev) !== JSON.stringify(it)) errors.push(`${it.slug} : défini différemment dans deux leçons`);
          items.set(it.slug, it);
        }
        l.exercises.forEach((ex, i) => validateAuthoredExercise(ex).forEach((e) => errors.push(`${l.slug} exercice ${i + 1} : ${e}`)));
      }
    }
  }
  return errors;
}

function loadContent(root: string): LevelJson[] {
  return readdirSync(root)
    .filter((d) => statSync(join(root, d)).isDirectory() && !['characters', 'cosmetics', 'exams', 'expressions', 'i18n'].includes(d))
    .flatMap((d) => readdirSync(join(root, d)).filter((f) => f.endsWith('.json')).map((f) => JSON.parse(readFileSync(join(root, d, f), 'utf8')) as LevelJson));
}

export async function seed(prisma: PrismaClient, contentRoot = resolve(__dirname, '../../../content')) {
  const levels = loadContent(contentRoot);
  const allErrors = levels.flatMap((l) => validateLevel(l).map((e) => `[${l.level.code}] ${e}`));
  // Une notion appartient à un seul niveau : un slug réutilisé ailleurs la « déplacerait » silencieusement.
  const owner = new Map<string, string>();
  for (const l of levels)
    for (const w of l.worlds) for (const c of w.chapters) for (const le of c.lessons) for (const it of le.items) {
      const prev = owner.get(it.slug);
      if (prev && prev !== l.level.code) allErrors.push(`notion « ${it.slug} » présente en ${prev} et en ${l.level.code}`);
      owner.set(it.slug, l.level.code);
    }
  if (allErrors.length) throw new Error(`Contenu invalide :\n- ${allErrors.join('\n- ')}`);

  for (const data of levels) {
    const v = data.contentVersion;
    const { code } = data.level;
    await prisma.jlptLevel.upsert({
      where: { code },
      create: { ...data.level, notice: data.notice, contentVersion: v },
      update: { title: data.level.title, region: data.level.region, order: data.level.order, notice: data.notice, contentVersion: v },
    });
    let itemCount = 0;
    let lessonCount = 0;
    for (const [wi, w] of data.worlds.entries()) {
      const world = await prisma.world.upsert({
        where: { slug: w.slug },
        create: { slug: w.slug, levelCode: code, order: wi + 1, title: w.title, region: w.region, description: w.description, bossName: w.boss?.name ?? null, bossGlyph: w.boss?.glyph ?? null, bossIntro: w.boss?.intro ?? null, examSlug: w.exam ?? null },
        update: { levelCode: code, order: wi + 1, title: w.title, region: w.region, description: w.description, bossName: w.boss?.name ?? null, bossGlyph: w.boss?.glyph ?? null, bossIntro: w.boss?.intro ?? null, examSlug: w.exam ?? null },
      });
      for (const [ci, c] of w.chapters.entries()) {
        const chapter = await prisma.chapter.upsert({
          where: { slug: c.slug },
          create: { slug: c.slug, worldId: world.id, order: ci + 1, title: c.title },
          update: { worldId: world.id, order: ci + 1, title: c.title },
        });
        for (const [li, l] of c.lessons.entries()) {
          lessonCount++;
          const lessonData = { chapterId: chapter.id, order: li + 1, title: l.title, objective: l.objective, minutes: l.minutes, explanation: l.explanation, contentVersion: v };
          const lesson = await prisma.lesson.upsert({ where: { slug: l.slug }, create: { slug: l.slug, ...lessonData }, update: lessonData });

          await prisma.lessonItem.deleteMany({ where: { lessonId: lesson.id } });
          for (const [ii, it] of l.items.entries()) {
            itemCount++;
            const base = { kind: it.kind, front: it.front, reading: it.reading ?? null, romaji: it.romaji ?? null, meaning: it.meaning, levelCode: code, contentVersion: v };
            const item = await prisma.learningItem.upsert({ where: { slug: it.slug }, create: { slug: it.slug, ...base }, update: base });
            if (it.kind === 'kanji' && it.kanji) {
              const k = { onyomi: it.kanji.onyomi, kunyomi: it.kanji.kunyomi, strokes: it.kanji.strokes ?? null };
              await prisma.kanji.upsert({ where: { itemId: item.id }, create: { itemId: item.id, ...k }, update: k });
            } else if (it.kind === 'vocabulary') {
              await prisma.vocabulary.upsert({ where: { itemId: item.id }, create: { itemId: item.id }, update: {} });
            } else if (it.kind === 'grammar') {
              await prisma.grammarPoint.upsert({ where: { itemId: item.id }, create: { itemId: item.id, pattern: it.front }, update: { pattern: it.front } });
            }
            await prisma.lessonItem.create({ data: { lessonId: lesson.id, itemId: item.id, order: ii } });
          }

          await prisma.example.deleteMany({ where: { lessonId: lesson.id } });
          await prisma.example.createMany({ data: l.examples.map((e, i) => ({ lessonId: lesson.id, order: i, jp: e.jp, reading: e.reading ?? null, fr: e.fr })) });

          const keep: string[] = [];
          for (const [ei, ex] of l.exercises.entries()) {
            const slug = `${l.slug}-ex${ei + 1}`;
            keep.push(slug);
            const d = { lessonId: lesson.id, order: ei, type: ex.type, payload: ex as unknown as Prisma.InputJsonValue };
            await prisma.exercise.upsert({ where: { slug }, create: { slug, ...d }, update: d });
          }
          await prisma.exercise.deleteMany({ where: { lessonId: lesson.id, slug: { notIn: keep } } });
        }
      }
    }
    for (const exam of Object.values(EXAMS).filter((e) => e.level === code)) {
      const ex = { levelCode: code, title: exam.title, sections: exam.sections as unknown as Prisma.InputJsonValue };
      await prisma.exam.upsert({ where: { slug: exam.slug }, create: { slug: exam.slug, ...ex }, update: ex });
    }
    console.log(`✔ ${code} (contenu ${v}) : ${data.worlds.length} mondes, ${lessonCount} leçons, ${itemCount} notions`);
  }
  await seedCharacters(prisma, contentRoot);
  await seedExpressions(prisma, contentRoot);
}

export interface CharactersJson {
  contentVersion: string;
  notice?: string;
  sections: { slug: 'hiragana' | 'katakana' | 'kanji'; title: string; description: string; groups: { slug: string; title: string; items: ItemJson[] }[] }[];
}

/** Onglet Caractères : mêmes notions (même slug) que le parcours, donc une maîtrise partagée. */
async function seedCharacters(prisma: PrismaClient, contentRoot: string) {
  const file = join(contentRoot, 'characters', 'characters.json');
  const data = JSON.parse(readFileSync(file, 'utf8')) as CharactersJson;
  const seen = new Set<string>();
  let n = 0;
  for (const s of data.sections)
    for (const g of s.groups)
      for (const it of g.items) {
        if (seen.has(it.slug)) throw new Error(`Caractères : slug en double ${it.slug}`);
        seen.add(it.slug);
        const base = { kind: it.kind, front: it.front, reading: it.reading ?? null, romaji: it.romaji ?? null, meaning: it.meaning, levelCode: 'N5', contentVersion: data.contentVersion };
        const item = await prisma.learningItem.upsert({ where: { slug: it.slug }, create: { slug: it.slug, ...base }, update: base });
        if (it.kanji) {
          const k = { onyomi: it.kanji.onyomi, kunyomi: it.kanji.kunyomi, strokes: it.kanji.strokes ?? null };
          await prisma.kanji.upsert({ where: { itemId: item.id }, create: { itemId: item.id, ...k }, update: k });
        }
        n++;
      }
  console.log(`✔ Caractères (contenu ${data.contentVersion}) : ${n} caractères`);
}

export interface ExpressionsJson {
  contentVersion: string;
  notice?: string;
  themes: { slug: string; glyph: string; title: string; description: string; expressions: (ItemJson & { note: string; register: string; example?: { jp: string; fr: string } })[] }[];
}

/** Onglet Expressions : des notions de vocabulaire à part entière (révisions et maîtrise comprises). */
async function seedExpressions(prisma: PrismaClient, contentRoot: string) {
  const data = JSON.parse(readFileSync(join(contentRoot, 'expressions', 'expressions.json'), 'utf8')) as ExpressionsJson;
  const seen = new Set<string>();
  let n = 0;
  for (const t of data.themes)
    for (const it of t.expressions) {
      if (seen.has(it.slug)) throw new Error(`Expressions : slug en double ${it.slug}`);
      seen.add(it.slug);
      const base = { kind: 'vocabulary', front: it.front, reading: it.reading ?? null, romaji: it.romaji ?? null, meaning: it.meaning, levelCode: 'N5', contentVersion: data.contentVersion };
      await prisma.learningItem.upsert({ where: { slug: it.slug }, create: { slug: it.slug, ...base }, update: base });
      n++;
    }
  console.log(`✔ Expressions (contenu ${data.contentVersion}) : ${data.themes.length} thèmes, ${n} expressions`);
}

/** Empreinte de tous les fichiers de contenu : l'import est sauté s'ils n'ont pas changé. */
function contentHash(root: string): string {
  const h = createHash('sha256');
  const walk = (dir: string) => {
    for (const f of readdirSync(dir).sort()) {
      const p = join(dir, f);
      if (statSync(p).isDirectory()) walk(p);
      else if (f.endsWith('.json')) h.update(f).update(readFileSync(p));
    }
  };
  walk(root);
  return h.digest('hex');
}

/**
 * Lancement au démarrage du serveur (`--if-changed`) : n'importe les contenus que s'ils ont changé
 * depuis le dernier import, pour un démarrage rapide (réveil d'un hébergement gratuit, redémarrage).
 */
async function seedIfChanged(prisma: PrismaClient, contentRoot = resolve(__dirname, '../../../content')) {
  await prisma.$executeRawUnsafe('CREATE TABLE IF NOT EXISTS "_KotoContent" (id INT PRIMARY KEY, hash TEXT NOT NULL, "importedAt" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP)');
  const hash = contentHash(contentRoot);
  const rows = await prisma.$queryRawUnsafe<{ hash: string }[]>('SELECT hash FROM "_KotoContent" WHERE id = 1');
  if (rows[0]?.hash === hash) {
    console.log('✔ Contenus déjà à jour : import sauté');
    return;
  }
  await seed(prisma, contentRoot);
  await prisma.$executeRawUnsafe('INSERT INTO "_KotoContent" (id, hash) VALUES (1, $1) ON CONFLICT (id) DO UPDATE SET hash = EXCLUDED.hash, "importedAt" = CURRENT_TIMESTAMP', hash);
}

if (require.main === module) {
  const prisma = new PrismaClient({ adapter: new PrismaPg({ connectionString: process.env.DATABASE_URL! }) });
  (process.argv.includes('--if-changed') ? seedIfChanged(prisma) : seed(prisma))
    .catch((e) => {
      console.error(e.message ?? e);
      process.exitCode = 1;
    })
    .finally(() => prisma.$disconnect());
}
