import { Ctx, completeFirstLesson, correctAnswer, createTestApp, resetUsers, signUp, wrongAnswer } from './helpers';

describe('Combats de boss', () => {
  let ctx: Ctx;
  beforeAll(async () => {
    ctx = await createTestApp();
    await resetUsers(ctx.prisma);
  });
  afterAll(() => ctx.app.close());

  /** Utilisateur qui lit déjà les kana et a terminé les 2 leçons de katakana (monde 2). */
  async function readyForKatakanaBoss() {
    const u = await signUp(ctx.app, { selfLevel: 'kana' });
    await u.agent.post('/api/worlds/n5-w2/boss/start').expect(403);
    await completeFirstLesson(ctx, u.agent, 'n5-kata-a');
    await completeFirstLesson(ctx, u.agent, 'n5-kata-ka');
    return u;
  }

  async function answer(agent: Parameters<typeof completeFirstLesson>[1], q: any, ok: boolean) {
    const ans = await correctAnswer(ctx.prisma, q.id);
    await agent.post(`/api/questions/${q.id}/answer`).send({ answer: ok ? ans : wrongAnswer(q, ans), responseMs: 3000 }).expect(200);
  }

  it('apparaît sur le parcours une fois le monde terminé, et se gagne côté serveur', async () => {
    const { agent, email } = await readyForKatakanaBoss();
    const path = await agent.get('/api/path/n5').expect(200);
    const w2 = path.body.worlds.find((w: any) => w.slug === 'n5-w2');
    expect(w2.boss).toMatchObject({ name: 'Le Tanuki farceur', glyph: '狸', available: true, defeated: false });
    expect(path.body.worlds.find((w: any) => w.slug === 'n5-w3').boss.available).toBe(false);

    const fight = await agent.post('/api/worlds/n5-w2/boss/start').expect(201);
    expect(fight.body.rules).toEqual({ hp: 9, hearts: 3 });
    expect(fight.body.questions).toHaveLength(12);
    for (const q of fight.body.questions) {
      expect(q.phase).toBe('boss');
      expect(q.answer).toBeUndefined();
    }
    // Pas de reprise pendant un combat
    const [q0, q1, ...rest] = fight.body.questions;
    await answer(agent, q0, false);
    await agent.post(`/api/questions/${q0.id}/retry`).expect(400);
    await agent.post('/api/worlds/n5-w2/boss/finish').send({ sessionId: fight.body.sessionId }).expect(400);
    await answer(agent, q1, true);
    for (const q of rest.slice(0, 8)) await answer(agent, q, true);

    const before = await ctx.prisma.user.findUniqueOrThrow({ where: { email } });
    const xpBefore = before.xp;
    const out = await agent.post('/api/worlds/n5-w2/boss/finish').send({ sessionId: fight.body.sessionId }).expect(200);
    expect(out.body).toMatchObject({ state: 'won', hits: 9, heartsLeft: 2, firstVictory: true, xpGained: 120, coinsGained: 30 });
    const user = await ctx.prisma.user.findUniqueOrThrow({ where: { email } });
    // + 120 XP et 30 pièces du gardien (les quêtes du jour peuvent s'y ajouter, par tranches)
    const questXpAfter = (await ctx.prisma.xpEvent.aggregate({ where: { userId: user.id, reason: 'quest', createdAt: { gt: before.updatedAt } }, _sum: { amount: true } }))._sum.amount ?? 0;
    expect(user.xp - questXpAfter).toBe(xpBefore + 120);
    expect((user.coins - before.coins - 30) % 5).toBe(0);
    expect(user.coins - before.coins).toBeGreaterThanOrEqual(30);
    await agent.post('/api/worlds/n5-w2/boss/finish').send({ sessionId: fight.body.sessionId }).expect(409);
    expect((await agent.get('/api/path/n5')).body.worlds.find((w: any) => w.slug === 'n5-w2').boss.defeated).toBe(true);

    // Rejouer : récompense symbolique
    const again = await agent.post('/api/worlds/n5-w2/boss/start').expect(201);
    for (const q of again.body.questions.slice(0, 9)) await answer(agent, q, true);
    const out2 = await agent.post('/api/worlds/n5-w2/boss/finish').send({ sessionId: again.body.sessionId }).expect(200);
    expect(out2.body).toMatchObject({ state: 'won', firstVictory: false, xpGained: 15 });
  });

  it('se perd après 3 erreurs, et reste propre à chaque compte', async () => {
    const { agent } = await readyForKatakanaBoss();
    const fight = await agent.post('/api/worlds/n5-w2/boss/start').expect(201);
    for (const q of fight.body.questions.slice(0, 3)) await answer(agent, q, false);
    const other = await signUp(ctx.app);
    await other.agent.post('/api/worlds/n5-w2/boss/finish').send({ sessionId: fight.body.sessionId }).expect(404);
    const out = await agent.post('/api/worlds/n5-w2/boss/finish').send({ sessionId: fight.body.sessionId }).expect(200);
    expect(out.body).toMatchObject({ state: 'lost', hits: 0, heartsLeft: 0, firstVictory: false, xpGained: 5 });
    await agent.post('/api/worlds/n5-final/boss/start').expect(404);
  });

  it('chrono : une réponse trop tardive compte comme une erreur, contrôlé par le serveur', async () => {
    const { agent } = await readyForKatakanaBoss();
    const fight = await agent.post('/api/worlds/n5-w2/boss/start').expect(201);
    const [q0, q1, q2, q3] = fight.body.questions;
    try {
      // Q0 : affichée, puis réponse juste… 40 s plus tard → refusée
      const shown = await agent.post(`/api/questions/${q0.id}/shown`).expect(200);
      expect(shown.body.timeLimitSec).toBeGreaterThanOrEqual(10);
      ctx.clock.advance(40_000);
      const late = await agent.post(`/api/questions/${q0.id}/answer`).send({ answer: await correctAnswer(ctx.prisma, q0.id), responseMs: 1000 }).expect(200);
      expect(late.body).toMatchObject({ correct: false, timedOut: true });

      // Q1 : réponse rapide → acceptée
      await agent.post(`/api/questions/${q1.id}/shown`).expect(200);
      ctx.clock.advance(3_000);
      const fast = await agent.post(`/api/questions/${q1.id}/answer`).send({ answer: await correctAnswer(ctx.prisma, q1.id), responseMs: 3000 }).expect(200);
      expect(fast.body).toMatchObject({ correct: true, timedOut: false });

      // Q2 : sans déclarer l'affichage, le chrono part de la réponse précédente
      ctx.clock.advance(60_000);
      const sneaky = await agent.post(`/api/questions/${q2.id}/answer`).send({ answer: await correctAnswer(ctx.prisma, q2.id), responseMs: 2000 }).expect(200);
      expect(sneaky.body).toMatchObject({ correct: false, timedOut: true });

      // Q3 : temps écoulé côté interface
      await agent.post(`/api/questions/${q3.id}/shown`).expect(200);
      const timeout = await agent.post(`/api/questions/${q3.id}/answer`).send({ answer: '⏱', responseMs: 12000 }).expect(200);
      expect(timeout.body).toMatchObject({ correct: false, timedOut: true });

      // Le combat est perdu (3 erreurs) : recalculé côté serveur
      const out = await agent.post('/api/worlds/n5-w2/boss/finish').send({ sessionId: fight.body.sessionId }).expect(200);
      expect(out.body).toMatchObject({ state: 'lost', hits: 1, heartsLeft: 0 });
    } finally {
      ctx.clock.reset();
    }
  });
});
