import { Ctx, completeFirstLesson, createTestApp, resetUsers, signUp } from './helpers';

describe('Succès', () => {
  let ctx: Ctx;
  beforeAll(async () => {
    ctx = await createTestApp();
    await resetUsers(ctx.prisma);
  });
  afterAll(() => ctx.app.close());

  it('aucun succès au départ ; le catalogue complet est listé avec la progression', async () => {
    const { agent } = await signUp(ctx.app);
    const list = (await agent.get('/api/achievements').expect(200)).body;
    expect(list.unlocked).toBe(0);
    expect(list.total).toBeGreaterThan(20);
    expect(list.achievements.find((a: any) => a.slug === 'first-lesson')).toMatchObject({ unlocked: false, value: 0, target: 1 });
    const check = (await agent.post('/api/achievements/check').expect(200)).body;
    expect(check).toEqual({ unlocked: [], coinsGained: 0, xpGained: 0 });
  });

  it('débloque à partir des données serveur et ne récompense qu’une seule fois, même en parallèle', async () => {
    const { agent, email } = await signUp(ctx.app);
    await completeFirstLesson(ctx, agent);
    const before = await ctx.prisma.user.findUniqueOrThrow({ where: { email } });
    const results = await Promise.all([1, 2, 3].map(() => agent.post('/api/achievements/check').expect(200)));
    const all = results.flatMap((r) => r.body.unlocked.map((a: any) => a.slug));
    expect(all.filter((s: string) => s === 'first-lesson')).toHaveLength(1);
    expect(all).toContain('first-perfect');
    const coins = results.reduce((n, r) => n + r.body.coinsGained, 0);
    const after = await ctx.prisma.user.findUniqueOrThrow({ where: { email } });
    expect(after.coins - before.coins).toBe(coins);
    const expected = results.flatMap((r) => r.body.unlocked).reduce((n: number, a: any) => n + a.coins, 0);
    expect(coins).toBe(expected);
    const again = (await agent.post('/api/achievements/check').expect(200)).body;
    expect(again.unlocked).toEqual([]);
    const list = (await agent.get('/api/achievements').expect(200)).body;
    expect(list.achievements.find((a: any) => a.slug === 'first-lesson')).toMatchObject({ unlocked: true });
    expect(list.achievements.find((a: any) => a.slug === 'first-lesson').unlockedAt).toBeTruthy();
  });

  it('les succès sont propres à chaque utilisateur et exigent une session', async () => {
    const { agent } = await signUp(ctx.app);
    const list = (await agent.get('/api/achievements').expect(200)).body;
    expect(list.unlocked).toBe(0);
    const anon = (await import('supertest')).default(ctx.app.getHttpServer());
    await anon.get('/api/achievements').expect(401);
  });
});
