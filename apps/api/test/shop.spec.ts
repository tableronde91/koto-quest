import { Ctx, completeFirstLesson, createTestApp, resetUsers, signUp } from './helpers';

describe('Personnage, boutique et économie de pièces', () => {
  let ctx: Ctx;
  beforeAll(async () => {
    ctx = await createTestApp();
    await resetUsers(ctx.prisma);
  });
  afterAll(() => ctx.app.close());

  const setCoins = (email: string, coins: number) => ctx.prisma.user.update({ where: { email }, data: { coins } });

  it('donne un avatar par défaut et une garde-robe de départ', async () => {
    const { agent } = await signUp(ctx.app);
    const me = await agent.get('/api/me').expect(200);
    expect(me.body.avatar).toMatchObject({ outfit: 'outfit-tshirt', background: 'bg-paper', hat: null });
    expect(me.body.coins).toBe(0);
    const shop = await agent.get('/api/shop').expect(200);
    expect(shop.body.items.find((i: any) => i.sku === 'outfit-tshirt')).toMatchObject({ owned: true, equipped: true });
    expect(shop.body.items.find((i: any) => i.sku === 'hat-kitsune')).toMatchObject({ owned: false, lockedBy: 'La Kitsune masquée' });
  });

  it('une leçon terminée pour la première fois rapporte des pièces (une seule fois)', async () => {
    const { agent, email } = await signUp(ctx.app);
    const { done } = await completeFirstLesson(ctx, agent);
    expect(done.coinsGained).toBe(15); // 10 + 5 sans faute
    const again = await completeFirstLesson(ctx, agent);
    expect(again.done.coinsGained).toBe(0);
    const user = await ctx.prisma.user.findUniqueOrThrow({ where: { email } });
    // Pièces de leçon + éventuelles quêtes du jour (5 chacune)
    expect(user.coins).toBeGreaterThanOrEqual(15);
    expect((user.coins - 15) % 5).toBe(0);
  });

  it('les quêtes du jour sont récompensées une seule fois, en XP et en pièces', async () => {
    const { agent, email } = await signUp(ctx.app);
    await completeFirstLesson(ctx, agent);
    await completeFirstLesson(ctx, agent);
    const user = await ctx.prisma.user.findUniqueOrThrow({ where: { email } });
    const day = await ctx.prisma.dailyActivity.findFirstOrThrow({ where: { userId: user.id } });
    const dash = (await agent.get('/api/dashboard').expect(200)).body;
    const done = dash.quests.filter((q: any) => q.done).map((q: any) => q.id).sort();
    expect([...day.questsClaimed].sort()).toEqual(done);
    const questXp = await ctx.prisma.xpEvent.aggregate({ where: { userId: user.id, reason: 'quest' }, _sum: { amount: true } });
    expect(questXp._sum.amount ?? 0).toBe(dash.quests.filter((q: any) => q.done).reduce((n: number, q: any) => n + q.xp, 0));
  });

  it('achat validé côté serveur : solde suffisant, pas de double achat, pas de solde négatif', async () => {
    const { agent, email } = await signUp(ctx.app);
    await agent.post('/api/shop/acquire').send({ sku: 'hat-kasa' }).expect(400);
    await setCoins(email, 60);
    const shop = await agent.post('/api/shop/acquire').send({ sku: 'hat-kasa' }).expect(200);
    expect(shop.body.coins).toBe(10);
    expect(shop.body.items.find((i: any) => i.sku === 'hat-kasa').owned).toBe(true);
    await agent.post('/api/shop/acquire').send({ sku: 'hat-kasa' }).expect(409);
    await agent.post('/api/shop/acquire').send({ sku: 'inconnu' }).expect(404);

    // Achats simultanés : un seul passe, le solde n'est jamais négatif
    await setCoins(email, 50);
    const results = await Promise.all([
      agent.post('/api/shop/acquire').send({ sku: 'bg-sakura' }),
      agent.post('/api/shop/acquire').send({ sku: 'bg-sakura' }),
    ]);
    expect(results.map((r) => r.status).sort()).toEqual([200, 409]);
    expect((await ctx.prisma.user.findUniqueOrThrow({ where: { email } })).coins).toBe(0);
  });

  it('les trophées exigent la victoire sur le gardien', async () => {
    const { agent, email } = await signUp(ctx.app);
    await setCoins(email, 999);
    await agent.post('/api/shop/acquire').send({ sku: 'hat-tanuki-leaf' }).expect(403);
    const user = await ctx.prisma.user.findUniqueOrThrow({ where: { email } });
    await ctx.prisma.bossResult.create({ data: { userId: user.id, worldSlug: 'n5-w2', attempts: 1, victories: 1, firstVictoryAt: new Date() } });
    const shop = await agent.post('/api/shop/acquire').send({ sku: 'hat-tanuki-leaf' }).expect(200);
    expect(shop.body.coins).toBe(999);
  });

  it('enregistre l’apparence uniquement avec des objets possédés', async () => {
    const { agent, email } = await signUp(ctx.app);
    const base = (await agent.get('/api/me')).body.avatar;
    await agent.put('/api/me/avatar').send({ avatar: { ...base, hat: 'hat-kasa' } }).expect(400);
    await agent.put('/api/me/avatar').send({ avatar: { ...base, hair: 'mohawk' } }).expect(400);
    await setCoins(email, 50);
    await agent.post('/api/shop/acquire').send({ sku: 'hat-kasa' }).expect(200);
    const saved = await agent.put('/api/me/avatar').send({ avatar: { ...base, hat: 'hat-kasa', hair: 'bun', hairColor: 3, skin: 2, eyes: 'happy', extra: 'ignored' } }).expect(200);
    expect(saved.body).toEqual({ ...base, hat: 'hat-kasa', hair: 'bun', hairColor: 3, skin: 2, eyes: 'happy' });
    expect((await agent.get('/api/me')).body.avatar.hat).toBe('hat-kasa');
    const shop = (await agent.get('/api/shop')).body;
    expect(shop.items.find((i: any) => i.sku === 'hat-kasa').equipped).toBe(true);
  });
});
