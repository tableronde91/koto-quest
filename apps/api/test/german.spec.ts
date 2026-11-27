import request from 'supertest';
import { readFileSync } from 'fs';
import { resolve } from 'path';
import { Ctx, completeFirstLesson, correctAnswer, createTestApp, resetUsers } from './helpers';

/** Allemand (Goethe-Zertifikat, niveaux du CECRL) : une sixième langue, avec son parcours, ses expressions, ses contes et son examen. */
const stories = JSON.parse(readFileSync(resolve(__dirname, '../../../content/reading/stories.json'), 'utf8'));

async function signUpGerman(ctx: Ctx) {
  const agent = request.agent(ctx.app.getHttpServer());
  await agent.post('/api/auth/register').send({ email: `de${Date.now()}${Math.random()}@test.local`, password: 'motdepasse123', displayName: 'Lena' }).expect(201);
  const me = (await agent.put('/api/me/onboarding').send({ selfLevel: 'beginner', targetLevel: 'GOETHEA1', studyLanguage: 'de', minutesPerDay: 20, difficultAreas: [], reminderMode: 'normal' }).expect(200)).body;
  return { agent, me };
}

describe('Allemand : préparer le Goethe-Zertifikat', () => {
  let ctx: Ctx;
  beforeAll(async () => {
    ctx = await createTestApp();
    await resetUsers(ctx.prisma);
  });
  afterAll(() => ctx.app.close());

  it('onboarding en allemand : parcours Goethe A1, première île ouverte, niveaux allemands seulement', async () => {
    const { agent, me } = await signUpGerman(ctx);
    expect(me.preferences).toMatchObject({ studyLanguage: 'de', targetLevel: 'GOETHEA1' });
    const path = (await agent.get('/api/path/GOETHEA1').expect(200)).body;
    expect(path.level).toMatchObject({ code: 'GOETHEA1', region: 'Route des contes' });
    expect(path.levels.map((l: any) => l.code)).toEqual(['GOETHEA1']);
    expect(path.worlds).toHaveLength(9);
    expect(path.worlds.slice(0, 8).map((w: any) => w.boss.glyph)).toEqual(['Ä', 'Ö', 'ß', 'ä', 'ö', '7', '❄', '♪']);
    expect(path.worlds.at(-1)).toMatchObject({ slug: 'goethea1-final', exam: { slug: 'goethea1-official' } });
    expect(path.worlds[0].chapters[0].lessons[0]).toMatchObject({ slug: 'de-hallo', status: 'available' });
    const dash = (await agent.get('/api/dashboard').expect(200)).body;
    expect(dash).toMatchObject({ targetLevel: 'GOETHEA1', nextLesson: { slug: 'de-hallo' } });
    // Changer de langue retrouve son niveau ; revenir à l'allemand aussi
    await agent.put('/api/me/preferences').send({ studyLanguage: 'es' }).expect(200);
    const back = (await agent.put('/api/me/preferences').send({ studyLanguage: 'de' }).expect(200)).body;
    expect(back.preferences).toMatchObject({ studyLanguage: 'de', targetLevel: 'GOETHEA1' });
  });

  it('pas d’écriture à apprendre ; expressions, contes, jeux et atelier en allemand', async () => {
    const { agent } = await signUpGerman(ctx);
    expect((await agent.get('/api/characters').expect(200)).body.sections).toEqual([]);

    const expr = (await agent.get('/api/expressions').expect(200)).body;
    expect(expr.themes.map((t: any) => t.slug)).toEqual(['de-hoeflichkeit', 'de-alltag', 'de-bilder', 'de-sprichwoerter']);
    expect(expr.themes.find((t: any) => t.slug === 'de-alltag').expressions.map((e: any) => e.front)).toContain('Genau!');
    const s = (await agent.post('/api/expressions/practice').send({ theme: 'de-sprichwoerter' }).expect(201)).body;
    expect(s.questions.length).toBeGreaterThan(5);

    const reading = (await agent.get('/api/reading').expect(200)).body;
    expect(reading.stories.map((x: any) => x.slug)).toEqual(['bremer-stadtmusikanten', 'suesser-brei', 'sterntaler']);
    await agent.get('/api/reading/chapters/medio-pollito-1').expect(404);
    const ch = stories.stories.find((x: any) => x.slug === 'suesser-brei').chapters[0];
    const r = (await agent.post('/api/reading/chapters/suesser-brei-1/complete').send({ answers: ch.questions.map((q: any) => q.answer) }).expect(201)).body;
    expect(r).toMatchObject({ firstTime: true, correct: ch.questions.length, next: { slug: 'suesser-brei-2' } });

    const games = (await agent.get('/api/games').expect(200)).body.games;
    expect(games.map((g: any) => g.id)).toEqual(['word-rush', 'speed', 'listening']);

    const drills = (await agent.get('/api/jlpt/drills').expect(200)).body.drills;
    expect(drills.map((d: any) => [d.part, d.jpTitle])).toEqual([['grammar', 'Lesen'], ['listening', 'Hören']]);

    const slugs = (await agent.get('/api/achievements').expect(200)).body.achievements.map((a: any) => a.slug);
    expect(slugs).toEqual(expect.arrayContaining(['de-bosses-8', 'goethe-passed', 'de-tales-10']));
    expect(slugs).not.toContain('dele-passed');
  });

  it('contes : la bonne réponse n’est pas toujours le premier choix', () => {
    for (const prefix of ['GOETHE', 'DELE', 'HSK']) {
      const answers = stories.stories.filter((x: any) => x.level.startsWith(prefix)).flatMap((x: any) => x.chapters.flatMap((c: any) => c.questions.map((q: any) => q.answer)));
      expect(new Set(answers).size).toBeGreaterThan(1);
    }
  });

  it('une leçon se joue en allemand, sans mélanger les langues dans les révisions', async () => {
    const { agent } = await signUpGerman(ctx);
    const { start } = await completeFirstLesson(ctx, agent, 'de-hallo');
    expect(start.questions.some((q: any) => q.display?.jp === 'danke' || q.choices?.includes('danke'))).toBe(true);
    const userId = (await agent.get('/api/me').expect(200)).body.id;
    expect(await ctx.prisma.reviewCard.count({ where: { userId, item: { levelCode: 'GOETHEA1' } } })).toBeGreaterThanOrEqual(6);
    expect(await ctx.prisma.reviewCard.count({ where: { userId, item: { levelCode: { not: 'GOETHEA1' } } } })).toBe(0);
    const games = (await agent.get('/api/games').expect(200)).body.games;
    expect(games[0]).toMatchObject({ id: 'word-rush', available: true });
  });

  it('examen blanc Goethe A1 : 15 + 15 + 5 questions en 65 minutes, noté sur 100 avec réussite à 60', async () => {
    const { agent } = await signUpGerman(ctx);
    const exam = (await agent.post('/api/exams/goethea1-official/start').expect(201)).body;
    expect(exam.questions).toHaveLength(35);
    expect(exam.exam.durationMin).toBe(65);
    expect(exam.questions.filter((q: any) => q.type === 'listening_choice')).toHaveLength(15);
    const answers: Record<string, unknown> = {};
    for (const q of exam.questions) answers[q.id] = await correctAnswer(ctx.prisma, q.id);
    const result = (await agent.post('/api/exams/goethea1-official/submit').send({ sessionId: exam.sessionId, answers }).expect(200)).body;
    expect(result).toMatchObject({ passed: true, percent: 100, passPercent: 60, sectionMinPercent: 0 });
    expect(result.scaled ?? null).toBeNull();

    // Sans aucune bonne réponse à l'écoute : 20 sur 35, soit 57 % — en dessous des 60 points
    const exam2 = (await agent.post('/api/exams/goethea1-official/start').expect(201)).body;
    const answers2: Record<string, unknown> = {};
    for (const q of exam2.questions) answers2[q.id] = q.type === 'listening_choice' ? '—' : await correctAnswer(ctx.prisma, q.id);
    const fail = (await agent.post('/api/exams/goethea1-official/submit').send({ sessionId: exam2.sessionId, answers: answers2 }).expect(200)).body;
    expect(fail).toMatchObject({ passed: false, percent: 57 });
  });

  it('saga : l’apprenti·e des frères Grimm, un chapitre par île', async () => {
    const { agent } = await signUpGerman(ctx);
    const story = (await agent.get('/api/path/GOETHEA1').expect(200)).body;
    expect(story.worlds.map((w: any) => w.slug)).toEqual(['goethea1-w1', 'goethea1-w2', 'goethea1-w3', 'goethea1-w4', 'goethea1-w5', 'goethea1-w6', 'goethea1-w7', 'goethea1-w8', 'goethea1-final']);
    const saga = JSON.parse(readFileSync(resolve(__dirname, '../../../content/story/story.json'), 'utf8')).levels.GOETHEA1;
    expect(saga).toMatchObject({ glyph: 'ß', jp: 'Märchenstraße' });
    expect(Object.keys(saga.chapters)).toHaveLength(9);
  });
});
