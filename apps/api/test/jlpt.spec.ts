import { Ctx, completeFirstLesson, correctAnswer, createTestApp, resetUsers, signUp } from './helpers';

describe('Atelier JLPT et exercices au format de l’examen', () => {
  let ctx: Ctx;
  beforeAll(async () => {
    ctx = await createTestApp();
    await resetUsers(ctx.prisma);
  });
  afterAll(() => ctx.app.close());

  it('rien à travailler tant qu’aucune leçon n’est faite', async () => {
    const { agent } = await signUp(ctx.app);
    const list = (await agent.get('/api/jlpt/drills').expect(200)).body;
    expect(list.drills.map((d: any) => d.part)).toEqual(['kanji', 'writing', 'grammar', 'star', 'listening']);
    expect(list.drills.every((d: any) => d.available === 0)).toBe(true);
    await agent.post('/api/jlpt/drills/kanji').expect(409);
    await agent.post('/api/jlpt/drills/inconnu').expect(404);
  });

  it('séries construites sur ce qui est appris, consignes en japonais, corrigées comme un exercice', async () => {
    const { agent, email } = await signUp(ctx.app);
    const user = await ctx.prisma.user.findUniqueOrThrow({ where: { email } });
    const n5 = await ctx.prisma.lesson.findMany({ where: { chapter: { world: { levelCode: 'N5' } } } });
    await ctx.prisma.userLessonProgress.createMany({ data: n5.map((l) => ({ userId: user.id, lessonId: l.id, status: 'completed', attempts: 1, bestScore: 100, completedAt: new Date() })) });
    // Leçons riches en kanji : le calendrier et la ville
    for (const slug of ['n5-calendar', 'n5-city', 'n5-directions-2']) {
      const { start } = await completeFirstLesson(ctx, agent, slug);
      // Les mots en kanji se lisent au format 漢字読み dès la leçon
      if (slug === 'n5-calendar') expect(start.questions.some((q: any) => q.type === 'jlpt_reading' && q.prompt.startsWith('＿＿の ことばは'))).toBe(true);
    }
    const list = (await agent.get('/api/jlpt/drills').expect(200)).body;
    const avail = Object.fromEntries(list.drills.map((d: any) => [d.part, d.available]));
    expect(avail.kanji).toBe(10);
    expect(avail.writing).toBeGreaterThanOrEqual(5);
    expect(avail.star).toBeGreaterThanOrEqual(3);

    const kanji = (await agent.post('/api/jlpt/drills/kanji').expect(201)).body;
    expect(kanji.questions).toHaveLength(10);
    const q = kanji.questions[0];
    expect(q).toMatchObject({ type: 'jlpt_reading', phase: 'practice' });
    expect(q.display.jp).toMatch(/\{\{.+\}\}/);
    expect(q.answer).toBeUndefined();
    const ok = await agent.post(`/api/questions/${q.id}/answer`).send({ answer: await correctAnswer(ctx.prisma, q.id), responseMs: 4000 }).expect(200);
    expect(ok.body.correct).toBe(true);

    const star = (await agent.post('/api/jlpt/drills/star').expect(201)).body;
    expect(star.questions[0].display.jp).toContain('★');
  });
});
