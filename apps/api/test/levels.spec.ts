import { Ctx, completeFirstLesson, createTestApp, resetUsers, signUp } from './helpers';

describe('Niveaux : parcours N4', () => {
  let ctx: Ctx;
  beforeAll(async () => {
    ctx = await createTestApp();
    await resetUsers(ctx.prisma);
  });
  afterAll(() => ctx.app.close());

  it('liste les niveaux disponibles et ouvre le N4 au premier monde, même pour un débutant', async () => {
    const { agent } = await signUp(ctx.app);
    const path = (await agent.get('/api/path/N4').expect(200)).body;
    expect(path.level.code).toBe('N4');
    expect(path.levels.map((l: any) => l.code)).toEqual(['N5', 'N4']);
    expect(path.worlds.length).toBeGreaterThanOrEqual(3);
    const lessons = path.worlds.flatMap((w: any) => w.chapters.flatMap((c: any) => c.lessons));
    expect(lessons[0]).toMatchObject({ slug: 'n4-te-ru', status: 'available' });
    expect(lessons[1].status).toBe('locked');
    expect(path.worlds.filter((w: any) => !w.exam).every((w: any) => w.boss)).toBe(true);
    expect(path.worlds.at(-1)).toMatchObject({ slug: 'n4-final', exam: { slug: 'n4-mock' } });
  });

  it('les kana déjà connus (déclarés à l’onboarding) ne décalent pas le départ du N4', async () => {
    const { agent } = await signUp(ctx.app, { selfLevel: 'n5' });
    const path = (await agent.get('/api/path/N4').expect(200)).body;
    expect(path.worlds[0].optional).toBe(false);
    expect(path.worlds[0].chapters[0].lessons[0].status).toBe('available');
  });

  it('une leçon N4 se joue comme une leçon N5 et compte dans la progression du niveau', async () => {
    const { agent } = await signUp(ctx.app);
    const { done } = await completeFirstLesson(ctx, agent, 'n4-te-ru');
    expect(done.correct).toBe(done.total);
    expect(done.nextLessonSlug).toBe('n4-te-u');
    const path = (await agent.get('/api/path/N4').expect(200)).body;
    expect(path.levels.find((l: any) => l.code === 'N4').completed).toBe(1);
  });

  it('une fois le N5 terminé, la prochaine leçon conseillée est au N4', async () => {
    const { agent, email } = await signUp(ctx.app);
    const user = await ctx.prisma.user.findUniqueOrThrow({ where: { email } });
    const n5 = await ctx.prisma.lesson.findMany({ where: { chapter: { world: { levelCode: 'N5' } } } });
    await ctx.prisma.userLessonProgress.createMany({ data: n5.map((l) => ({ userId: user.id, lessonId: l.id, status: 'completed', attempts: 1, bestScore: 100, completedAt: new Date() })) });
    const dash = (await agent.get('/api/dashboard').expect(200)).body;
    expect(dash.nextLesson).toMatchObject({ slug: 'n4-te-ru' });
  });

  it('examen blanc N4 : 34 questions issues du contenu N4, conseils propres au N4', async () => {
    const { agent } = await signUp(ctx.app);
    const exam = await agent.post('/api/exams/n4-mock/start').expect(201);
    expect(exam.body.exam).toMatchObject({ title: 'Examen blanc JLPT N4', durationMin: 30 });
    const qs = exam.body.questions;
    expect(qs).toHaveLength(34);
    const issued = await ctx.prisma.issuedQuestion.findMany({ where: { id: { in: qs.map((q: any) => q.id) } } });
    const itemIds = issued.map((q) => q.itemId).filter((x): x is string => !!x);
    const items = await ctx.prisma.learningItem.findMany({ where: { id: { in: itemIds } } });
    expect(items.length).toBeGreaterThan(10);
    expect(items.every((i) => i.levelCode === 'N4')).toBe(true);
    const res = (await agent.post('/api/exams/n4-mock/submit').send({ sessionId: exam.body.sessionId, answers: {} }).expect(200)).body;
    expect(res).toMatchObject({ correct: 0, passed: false });
    expect(res.recommendations.join(' ')).toMatch(/N4/);
  });

  it('niveau inexistant : 404', async () => {
    const { agent } = await signUp(ctx.app);
    await agent.get('/api/path/N1').expect(404);
  });
});
