import request from 'supertest';
import { readFileSync } from 'fs';
import { resolve } from 'path';
import { Ctx, completeFirstLesson, correctAnswer, createTestApp, resetUsers } from './helpers';

/** Anglais (TOEIC, niveaux du CECRL) : une troisième langue, avec son parcours, ses expressions, ses contes et son examen. */
const stories = JSON.parse(readFileSync(resolve(__dirname, '../../../content/reading/stories.json'), 'utf8'));
const bank = JSON.parse(readFileSync(resolve(__dirname, '../../../content/exams/a1-toeic.json'), 'utf8'));

async function signUpEnglish(ctx: Ctx) {
  const agent = request.agent(ctx.app.getHttpServer());
  await agent.post('/api/auth/register').send({ email: `en${Date.now()}${Math.random()}@test.local`, password: 'motdepasse123', displayName: 'Emma' }).expect(201);
  const me = (await agent.put('/api/me/onboarding').send({ selfLevel: 'beginner', targetLevel: 'A1', studyLanguage: 'en', minutesPerDay: 20, difficultAreas: [], reminderMode: 'normal' }).expect(200)).body;
  return { agent, me };
}

describe('Anglais : préparer le TOEIC', () => {
  let ctx: Ctx;
  beforeAll(async () => {
    ctx = await createTestApp();
    await resetUsers(ctx.prisma);
  });
  afterAll(() => ctx.app.close());

  it('onboarding en anglais : parcours A1, première île ouverte, niveaux anglais seulement', async () => {
    const { agent, me } = await signUpEnglish(ctx);
    expect(me.preferences).toMatchObject({ studyLanguage: 'en', targetLevel: 'A1' });
    const path = (await agent.get('/api/path/A1').expect(200)).body;
    expect(path.level).toMatchObject({ code: 'A1', region: 'Royaume d’Albion' });
    expect(path.levels.map((l: any) => l.code)).toEqual(['A1', 'A2', 'B1', 'B2', 'C1']);
    expect(path.worlds).toHaveLength(9);
    expect(path.worlds.slice(0, 8).map((w: any) => w.boss.glyph)).toEqual(['B', 'P', 'W', 'S', 'G', 'N', 'K', 'D']);
    expect(path.worlds.at(-1)).toMatchObject({ slug: 'a1-final', exam: { slug: 'a1-toeic' } });
    expect(path.worlds[0].chapters[0].lessons[0]).toMatchObject({ slug: 'en-hello', status: 'available' });
    const dash = (await agent.get('/api/dashboard').expect(200)).body;
    expect(dash).toMatchObject({ targetLevel: 'A1', nextLesson: { slug: 'en-hello' } });
  });

  it('pas d’écriture à apprendre ; expressions, contes, jeux et atelier en anglais', async () => {
    const { agent } = await signUpEnglish(ctx);
    expect((await agent.get('/api/characters').expect(200)).body.sections).toEqual([]);

    const expr = (await agent.get('/api/expressions').expect(200)).body;
    expect(expr.themes.map((t: any) => t.slug)).toEqual(['en-politeness', 'en-office', 'en-phrasal', 'en-idioms', 'en-proverbs']);
    expect(expr.themes.find((t: any) => t.slug === 'en-idioms').expressions.map((e: any) => e.front)).toContain('a piece of cake');
    const s = (await agent.post('/api/expressions/practice').send({ theme: 'en-office' }).expect(201)).body;
    expect(s.questions.length).toBeGreaterThan(5);

    const reading = (await agent.get('/api/reading').expect(200)).body;
    expect(reading.stories.map((x: any) => x.slug)).toEqual(['goldilocks', 'dick-whittington', 'sword-in-the-stone', 'jack-beanstalk', 'king-canute', 'robin-hood', 'pedlar-swaffham', 'tam-lin', 'gelert', 'lady-of-shalott', 'thomas-rhymer']);
    await agent.get('/api/reading/chapters/momotaro-1').expect(404);
    const ch = stories.stories.find((x: any) => x.slug === 'goldilocks').chapters[0];
    const r = (await agent.post('/api/reading/chapters/goldilocks-1/complete').send({ answers: ch.questions.map((q: any) => q.answer) }).expect(201)).body;
    expect(r).toMatchObject({ firstTime: true, correct: ch.questions.length, next: { slug: 'goldilocks-2' } });

    const games = (await agent.get('/api/games').expect(200)).body.games;
    expect(games.map((g: any) => g.id)).toEqual(['word-rush', 'speed', 'listening']);

    const drills = (await agent.get('/api/jlpt/drills').expect(200)).body.drills;
    expect(drills.map((d: any) => [d.part, d.jpTitle])).toEqual([['grammar', 'Part 5'], ['listening', 'Part 2']]);
  });

  it('une leçon se joue en anglais, avec des phrases à remettre dans l’ordre séparées par des espaces', async () => {
    const { agent } = await signUpEnglish(ctx);
    const { start } = await completeFirstLesson(ctx, agent, 'en-hello');
    expect(start.questions.some((q: any) => q.display?.jp === 'hello' || q.choices?.includes('hello'))).toBe(true);
    const userId = (await agent.get('/api/me').expect(200)).body.id;
    expect(await ctx.prisma.reviewCard.count({ where: { userId, item: { levelCode: 'A1' } } })).toBeGreaterThanOrEqual(6);
    expect(await ctx.prisma.reviewCard.count({ where: { userId, item: { levelCode: { not: 'A1' } } } })).toBe(0);
    // Word Rush se débloque après la première leçon (7 mots)
    const games = (await agent.get('/api/games').expect(200)).body.games;
    expect(games[0]).toMatchObject({ id: 'word-rush', available: true });
  });

  it('examen blanc TOEIC A1 : parties du TOEIC, notation sur 990, objectif 120', async () => {
    const { agent } = await signUpEnglish(ctx);
    const exam = (await agent.post('/api/exams/a1-toeic/start').expect(201)).body;
    expect(exam.questions).toHaveLength(30);
    expect(exam.questions.filter((q: any) => q.type === 'listening_choice')).toHaveLength(12);
    // Partie 1 : deux photos, phrases lues (numérotées dans l'ordre affiché), sans texte à lire
    const photos = exam.questions.filter((q: any) => q.display?.image);
    expect(photos).toHaveLength(2);
    for (const q of photos) {
      expect(q.display.audioChoices).toBe(true);
      expect(q.audio).toBe(q.choices.map((c: string, i: number) => `N|${i + 1}. ${c}`).join('\n'));
    }
    expect(new Set(exam.questions.map((q: any) => q.display?.part))).toEqual(new Set(bank.parts.map((p: any) => p.jpTitle)));
    const answers: Record<string, unknown> = {};
    for (const q of exam.questions) answers[q.id] = await correctAnswer(ctx.prisma, q.id);
    const result = (await agent.post('/api/exams/a1-toeic/submit').send({ sessionId: exam.sessionId, answers }).expect(200)).body;
    expect(result).toMatchObject({ passed: true, scaled: { listening: 495, language: 495, total: 990, max: { system: 'toeic', total: 990, passTotal: 120 } } });

    const empty = (await agent.post('/api/exams/a1-toeic/start').expect(201)).body;
    const zero = (await agent.post('/api/exams/a1-toeic/submit').send({ sessionId: empty.sessionId, answers: {} }).expect(200)).body;
    expect(zero).toMatchObject({ passed: false, scaled: { listening: 5, language: 5, total: 10 } });
  });

  it.each([
    ['a2', 36, 14, 225],
    ['b1', 42, 16, 550],
    ['b2', 48, 18, 785],
    ['c1', 54, 20, 945],
  ])('examen blanc TOEIC %s : nombre de questions, écoute et objectif', async (lvl, total, listening, target) => {
    const { agent } = await signUpEnglish(ctx);
    const exam = (await agent.post(`/api/exams/${lvl}-toeic/start`).expect(201)).body;
    expect(exam.questions).toHaveLength(total);
    expect(exam.questions.filter((q: any) => q.type === 'listening_choice')).toHaveLength(listening);
    const answers: Record<string, unknown> = {};
    for (const q of exam.questions) answers[q.id] = await correctAnswer(ctx.prisma, q.id);
    const result = (await agent.post(`/api/exams/${lvl}-toeic/submit`).send({ sessionId: exam.sessionId, answers }).expect(200)).body;
    expect(result).toMatchObject({ passed: true, scaled: { total: 990, max: { passTotal: target } } });
    const path = (await agent.get(`/api/path/${lvl.toUpperCase()}`).expect(200)).body;
    expect(path.worlds.at(-1)).toMatchObject({ exam: { slug: `${lvl}-toeic` } });
  });

  it('succès propres à l’anglais, cachés aux autres langues', async () => {
    const { agent } = await signUpEnglish(ctx);
    const slugs = (await agent.get('/api/achievements').expect(200)).body.achievements.map((a: any) => a.slug);
    expect(slugs).toEqual(expect.arrayContaining(['en-bosses-8', 'toeic-passed', 'en-tales-10']));
    expect(slugs).not.toContain('hangul-10');
    expect(slugs).not.toContain('kana-20');
  });
});
