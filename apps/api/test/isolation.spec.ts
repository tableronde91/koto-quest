import { Ctx, completeFirstLesson, correctAnswer, createTestApp, resetUsers, signUp } from './helpers';

describe('Isolation des comptes et RGPD', () => {
  let ctx: Ctx;
  beforeAll(async () => {
    ctx = await createTestApp();
    await resetUsers(ctx.prisma);
  });
  afterAll(() => ctx.app.close());

  it('un utilisateur ne peut ni lire ni répondre aux questions d’un autre', async () => {
    const alice = await signUp(ctx.app);
    const bob = await signUp(ctx.app);
    const start = await alice.agent.post('/api/lessons/n5-hira-a/start').expect(201);
    const q = start.body.questions[0];
    await bob.agent.get(`/api/questions/${q.id}`).expect(404);
    await bob.agent.post(`/api/questions/${q.id}/answer`).send({ answer: await correctAnswer(ctx.prisma, q.id), responseMs: 1000 }).expect(404);
    await bob.agent.post('/api/lessons/n5-hira-a/complete').send({ sessionId: start.body.sessionId }).expect(404);
    await alice.agent.get(`/api/questions/${q.id}`).expect(200);
  });

  it('progression, révisions et statistiques restent propres à chaque compte', async () => {
    const alice = await signUp(ctx.app);
    const bob = await signUp(ctx.app);
    await completeFirstLesson(ctx, alice.agent);
    const a = (await alice.agent.get('/api/dashboard')).body;
    const b = (await bob.agent.get('/api/dashboard')).body;
    expect(a.progress.completedLessons).toBe(1);
    expect(b.progress.completedLessons).toBe(0);
    expect(b.xp.total).toBe(0);
    expect((await bob.agent.get('/api/stats')).body.items).toHaveLength(0);
  });

  it('exporte les données de l’utilisateur sans secret', async () => {
    const alice = await signUp(ctx.app);
    await completeFirstLesson(ctx, alice.agent);
    const res = await alice.agent.get('/api/me/export').expect(200);
    expect(res.headers['content-disposition']).toMatch(/attachment/);
    expect(res.body.data.email).toBe(alice.email);
    expect(res.body.data.passwordHash).toBeUndefined();
    expect(res.body.data.reviewCards.length).toBe(5);
    expect(JSON.stringify(res.body)).not.toMatch(/tokenHash/);
  });

  it('supprime définitivement le compte et toutes ses données (avec confirmation)', async () => {
    const alice = await signUp(ctx.app);
    await completeFirstLesson(ctx, alice.agent);
    const user = await ctx.prisma.user.findUniqueOrThrow({ where: { email: alice.email } });
    await alice.agent.delete('/api/me').send({ password: 'mauvais' }).expect(403);
    await alice.agent.delete('/api/me').send({ password: 'motdepasse123' }).expect(204);
    await alice.agent.get('/api/me').expect(401);
    expect(await ctx.prisma.reviewCard.count({ where: { userId: user.id } })).toBe(0);
    expect(await ctx.prisma.exerciseAnswer.count({ where: { userId: user.id } })).toBe(0);
    expect(await ctx.prisma.dailyActivity.count({ where: { userId: user.id } })).toBe(0);
  });
});
