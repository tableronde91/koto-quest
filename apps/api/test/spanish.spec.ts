import request from 'supertest';
import { readFileSync } from 'fs';
import { resolve } from 'path';
import { Ctx, completeFirstLesson, correctAnswer, createTestApp, resetUsers } from './helpers';

/** Espagnol (DELE, niveaux du CECRL) : une cinquième langue, avec son parcours, ses expressions, ses contes et son examen. */
const stories = JSON.parse(readFileSync(resolve(__dirname, '../../../content/reading/stories.json'), 'utf8'));

async function signUpSpanish(ctx: Ctx) {
  const agent = request.agent(ctx.app.getHttpServer());
  await agent.post('/api/auth/register').send({ email: `es${Date.now()}${Math.random()}@test.local`, password: 'motdepasse123', displayName: 'Lucía' }).expect(201);
  const me = (await agent.put('/api/me/onboarding').send({ selfLevel: 'beginner', targetLevel: 'DELEA1', studyLanguage: 'es', minutesPerDay: 20, difficultAreas: [], reminderMode: 'normal' }).expect(200)).body;
  return { agent, me };
}

describe('Espagnol : préparer le DELE', () => {
  let ctx: Ctx;
  beforeAll(async () => {
    ctx = await createTestApp();
    await resetUsers(ctx.prisma);
  });
  afterAll(() => ctx.app.close());

  it('onboarding en espagnol : parcours DELE A1, première île ouverte, niveaux espagnols seulement', async () => {
    const { agent, me } = await signUpSpanish(ctx);
    expect(me.preferences).toMatchObject({ studyLanguage: 'es', targetLevel: 'DELEA1' });
    const path = (await agent.get('/api/path/DELEA1').expect(200)).body;
    expect(path.level).toMatchObject({ code: 'DELEA1', region: 'Chemins de la Manche' });
    expect(path.levels.map((l: any) => l.code)).toEqual(['DELEA1', 'DELEA2', 'DELEB1', 'DELEB2', 'DELEC1']);
    expect(path.worlds).toHaveLength(9);
    expect(path.worlds.slice(0, 8).map((w: any) => w.boss.glyph)).toEqual(['Á', 'É', 'Í', 'Ó', 'Ü', 'Ú', '¿', '¡']);
    expect(path.worlds.at(-1)).toMatchObject({ slug: 'delea1-final', exam: { slug: 'delea1-official' } });
    expect(path.worlds[0].chapters[0].lessons[0]).toMatchObject({ slug: 'es-hola', status: 'available' });
    const dash = (await agent.get('/api/dashboard').expect(200)).body;
    expect(dash).toMatchObject({ targetLevel: 'DELEA1', nextLesson: { slug: 'es-hola' } });
    // Changer de langue retrouve son niveau ; revenir à l'espagnol aussi
    await agent.put('/api/me/preferences').send({ studyLanguage: 'en' }).expect(200);
    const back = (await agent.put('/api/me/preferences').send({ studyLanguage: 'es' }).expect(200)).body;
    expect(back.preferences).toMatchObject({ studyLanguage: 'es', targetLevel: 'DELEA1' });
  });

  it('pas d’écriture à apprendre ; expressions, contes, jeux et atelier en espagnol', async () => {
    const { agent } = await signUpSpanish(ctx);
    expect((await agent.get('/api/characters').expect(200)).body.sections).toEqual([]);

    const expr = (await agent.get('/api/expressions').expect(200)).body;
    expect(expr.themes.map((t: any) => t.slug)).toEqual(['es-cortesia', 'es-diario', 'es-imagenes', 'es-refranes']);
    expect(expr.themes.find((t: any) => t.slug === 'es-diario').expressions.map((e: any) => e.front)).toContain('¡Vale!');
    const s = (await agent.post('/api/expressions/practice').send({ theme: 'es-refranes' }).expect(201)).body;
    expect(s.questions.length).toBeGreaterThan(5);

    const reading = (await agent.get('/api/reading').expect(200)).body;
    expect(reading.stories.map((x: any) => x.slug)).toEqual(['medio-pollito', 'ratita-presumida', 'molinos-de-viento', 'juan-sin-miedo', 'blanca-luna', 'gallo-santo-domingo', 'ciudad-de-duio', 'el-dorado', 'hombres-de-maiz', 'don-illan', 'ojos-verdes']);
    await agent.get('/api/reading/chapters/goldilocks-1').expect(404);
    const ch = stories.stories.find((x: any) => x.slug === 'medio-pollito').chapters[0];
    const r = (await agent.post('/api/reading/chapters/medio-pollito-1/complete').send({ answers: ch.questions.map((q: any) => q.answer) }).expect(201)).body;
    expect(r).toMatchObject({ firstTime: true, correct: ch.questions.length, next: { slug: 'medio-pollito-2' } });

    const games = (await agent.get('/api/games').expect(200)).body.games;
    expect(games.map((g: any) => g.id)).toEqual(['word-rush', 'speed', 'listening']);

    const drills = (await agent.get('/api/jlpt/drills').expect(200)).body.drills;
    expect(drills.map((d: any) => [d.part, d.jpTitle])).toEqual([['grammar', 'Comprensión de lectura'], ['listening', 'Comprensión auditiva']]);

    const slugs = (await agent.get('/api/achievements').expect(200)).body.achievements.map((a: any) => a.slug);
    expect(slugs).toEqual(expect.arrayContaining(['es-bosses-8', 'dele-passed', 'es-tales-10']));
    expect(slugs).not.toContain('hsk-passed');
  });

  it('une leçon se joue en espagnol, sans mélanger les langues dans les révisions', async () => {
    const { agent } = await signUpSpanish(ctx);
    const { start } = await completeFirstLesson(ctx, agent, 'es-hola');
    expect(start.questions.some((q: any) => q.display?.jp === 'hola' || q.choices?.includes('hola'))).toBe(true);
    const userId = (await agent.get('/api/me').expect(200)).body.id;
    expect(await ctx.prisma.reviewCard.count({ where: { userId, item: { levelCode: 'DELEA1' } } })).toBeGreaterThanOrEqual(6);
    expect(await ctx.prisma.reviewCard.count({ where: { userId, item: { levelCode: { not: 'DELEA1' } } } })).toBe(0);
    const games = (await agent.get('/api/games').expect(200)).body.games;
    expect(games[0]).toMatchObject({ id: 'word-rush', available: true });
  });

  it('examen blanc DELE A1 : 25 + 25 + 5 questions en 90 minutes, sur 100 en deux groupes', async () => {
    const { agent } = await signUpSpanish(ctx);
    const exam = (await agent.post('/api/exams/delea1-official/start').expect(201)).body;
    expect(exam.questions).toHaveLength(55);
    expect(exam.exam.durationMin).toBe(90);
    expect(exam.questions.filter((q: any) => q.type === 'listening_choice')).toHaveLength(25);
    const answers: Record<string, unknown> = {};
    for (const q of exam.questions) answers[q.id] = await correctAnswer(ctx.prisma, q.id);
    const result = (await agent.post('/api/exams/delea1-official/submit').send({ sessionId: exam.sessionId, answers }).expect(200)).body;
    expect(result).toMatchObject({ passed: true, scaled: { total: 100, language: 25, writing: 25, listening: 50, max: { system: 'dele', passTotal: 60 } } });

    // Sans aucune bonne réponse à l'écoute, le groupe 2 n'atteint pas 30 : échec malgré l'écrit parfait
    const exam2 = (await agent.post('/api/exams/delea1-official/start').expect(201)).body;
    const answers2: Record<string, unknown> = {};
    for (const q of exam2.questions) answers2[q.id] = q.type === 'listening_choice' ? '—' : await correctAnswer(ctx.prisma, q.id);
    const fail = (await agent.post('/api/exams/delea1-official/submit').send({ sessionId: exam2.sessionId, answers: answers2 }).expect(200)).body;
    expect(fail).toMatchObject({ passed: false, scaled: { language: 25, writing: 25, listening: 0 } });
  });

  it('DELE A2 : la route de Barcelone, ses gardiens, sa saga et son examen (25 + 30 + 5 questions)', async () => {
    const { agent } = await signUpSpanish(ctx);
    await agent.put('/api/me/preferences').send({ targetLevel: 'DELEA2' }).expect(200);
    const path = (await agent.get('/api/path/DELEA2').expect(200)).body;
    expect(path.level).toMatchObject({ code: 'DELEA2', region: 'Route de Barcelone' });
    expect(path.worlds).toHaveLength(9);
    expect(path.worlds.slice(0, 8).map((w: any) => w.boss.glyph)).toEqual(['ñ', 'á', 'é', 'í', 'ó', 'ú', 'ü', 'Ñ']);
    expect(path.worlds[0].chapters[0].lessons[0]).toMatchObject({ slug: 'es-perfecto' });
    expect(path.worlds.at(-1)).toMatchObject({ slug: 'delea2-final', exam: { slug: 'delea2-official' } });

    const exam = (await agent.post('/api/exams/delea2-official/start').expect(201)).body;
    expect(exam.questions).toHaveLength(60);
    expect(exam.exam.durationMin).toBe(110);
    expect(exam.questions.filter((q: any) => q.type === 'listening_choice')).toHaveLength(30);
    const answers: Record<string, unknown> = {};
    for (const q of exam.questions) answers[q.id] = await correctAnswer(ctx.prisma, q.id);
    const result = (await agent.post('/api/exams/delea2-official/submit').send({ sessionId: exam.sessionId, answers }).expect(200)).body;
    expect(result).toMatchObject({ passed: true, scaled: { total: 100, language: 25, writing: 25, listening: 50, max: { system: 'dele' } } });
  });

  it('DELE B1 : le chemin de Saint-Jacques, ses gardiens et son examen (30 + 30 + 5 questions)', async () => {
    const { agent } = await signUpSpanish(ctx);
    await agent.put('/api/me/preferences').send({ targetLevel: 'DELEB1' }).expect(200);
    const path = (await agent.get('/api/path/DELEB1').expect(200)).body;
    expect(path.level).toMatchObject({ code: 'DELEB1', region: 'Chemin de Saint-Jacques' });
    expect(path.worlds).toHaveLength(9);
    expect(path.worlds.slice(0, 8).map((w: any) => w.boss.glyph)).toEqual(['Ç', 'ç', 'º', 'ª', '«', '»', '~', '€']);
    expect(path.worlds[0].chapters[0].lessons[0]).toMatchObject({ slug: 'es-futuro' });
    expect(path.worlds.at(-1)).toMatchObject({ slug: 'deleb1-final', exam: { slug: 'deleb1-official' } });

    const exam = (await agent.post('/api/exams/deleb1-official/start').expect(201)).body;
    expect(exam.questions).toHaveLength(65);
    expect(exam.exam.durationMin).toBe(130);
    expect(exam.questions.filter((q: any) => q.type === 'listening_choice')).toHaveLength(30);
    const answers: Record<string, unknown> = {};
    for (const q of exam.questions) answers[q.id] = await correctAnswer(ctx.prisma, q.id);
    const result = (await agent.post('/api/exams/deleb1-official/submit').send({ sessionId: exam.sessionId, answers }).expect(200)).body;
    expect(result).toMatchObject({ passed: true, scaled: { total: 100, language: 25, writing: 25, listening: 50, max: { system: 'dele' } } });
  });

  it('DELE B2 : la traversée des Amériques, ses gardiens et son examen (36 + 30 + 5 questions)', async () => {
    const { agent } = await signUpSpanish(ctx);
    await agent.put('/api/me/preferences').send({ targetLevel: 'DELEB2' }).expect(200);
    const path = (await agent.get('/api/path/DELEB2').expect(200)).body;
    expect(path.level).toMatchObject({ code: 'DELEB2', region: 'Traversée des Amériques' });
    expect(path.worlds).toHaveLength(9);
    expect(path.worlds.slice(0, 8).map((w: any) => w.boss.glyph)).toEqual(['ã', 'ẽ', 'ĩ', 'õ', 'ũ', 'Ã', 'Õ', 'ỹ']);
    expect(path.worlds[0].chapters[0].lessons[0]).toMatchObject({ slug: 'es-ser-estar-b2' });
    expect(path.worlds.at(-1)).toMatchObject({ slug: 'deleb2-final', exam: { slug: 'deleb2-official' } });

    const exam = (await agent.post('/api/exams/deleb2-official/start').expect(201)).body;
    expect(exam.questions).toHaveLength(71);
    expect(exam.exam.durationMin).toBe(150);
    expect(exam.questions.filter((q: any) => q.type === 'listening_choice')).toHaveLength(30);
    const answers: Record<string, unknown> = {};
    for (const q of exam.questions) answers[q.id] = await correctAnswer(ctx.prisma, q.id);
    const result = (await agent.post('/api/exams/deleb2-official/submit').send({ sessionId: exam.sessionId, answers }).expect(200)).body;
    expect(result).toMatchObject({ passed: true, scaled: { total: 100, language: 25, writing: 25, listening: 50, max: { system: 'dele' } } });
  });

  it('DELE C1 : la Bibliothèque enchantée, ses gardiens et son examen (40 + 30 + 5 questions)', async () => {
    const { agent } = await signUpSpanish(ctx);
    await agent.put('/api/me/preferences').send({ targetLevel: 'DELEC1' }).expect(200);
    const path = (await agent.get('/api/path/DELEC1').expect(200)).body;
    expect(path.level).toMatchObject({ code: 'DELEC1', region: 'Bibliothèque enchantée' });
    expect(path.worlds).toHaveLength(9);
    expect(path.worlds.slice(0, 8).map((w: any) => w.boss.glyph)).toEqual(['§', '¶', '†', '‡', '°', '¤', '‰', '¬']);
    expect(path.worlds[0].chapters[0].lessons[0]).toMatchObject({ slug: 'es-registro' });
    expect(path.worlds.at(-1)).toMatchObject({ slug: 'delec1-final', exam: { slug: 'delec1-official' } });

    const exam = (await agent.post('/api/exams/delec1-official/start').expect(201)).body;
    expect(exam.questions).toHaveLength(75);
    expect(exam.exam.durationMin).toBe(170);
    expect(exam.questions.filter((q: any) => q.type === 'listening_choice')).toHaveLength(30);
    const answers: Record<string, unknown> = {};
    for (const q of exam.questions) answers[q.id] = await correctAnswer(ctx.prisma, q.id);
    const result = (await agent.post('/api/exams/delec1-official/submit').send({ sessionId: exam.sessionId, answers }).expect(200)).body;
    expect(result).toMatchObject({ passed: true, scaled: { total: 100, language: 25, writing: 25, listening: 50, max: { system: 'dele' } } });
  });
});
