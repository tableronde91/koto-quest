import { Ctx, correctAnswer, createTestApp, resetUsers, signUp, wrongAnswer, Agent } from './helpers';

describe('Mini-jeux chronométrés', () => {
  let ctx: Ctx;
  beforeAll(async () => {
    ctx = await createTestApp();
    await resetUsers(ctx.prisma);
  });
  afterEach(() => ctx.clock.reset());
  afterAll(() => ctx.app.close());

  async function learnKanji(agent: Agent) {
    for (let i = 0; i < 2; i++) {
      const s = await agent.post('/api/characters/practice').send({ scope: 'kanji-nombres' }).expect(201);
      for (const q of s.body.questions) await agent.post(`/api/questions/${q.id}/answer`).send({ answer: await correctAnswer(ctx.prisma, q.id), responseMs: 3000 }).expect(200);
    }
  }

  it('reste verrouillé tant que trop peu de notions ont été vues', async () => {
    const { agent } = await signUp(ctx.app);
    const list = await agent.get('/api/games').expect(200);
    expect(list.body.games.map((g: any) => g.id)).toEqual(['kanji-rush', 'speed', 'listening']);
    expect(list.body.games.every((g: any) => !g.available)).toBe(true);
    expect(list.body.coinsLeftToday).toBe(15);
    await agent.post('/api/games/kanji-rush/start').expect(403);
    await agent.post('/api/games/pacman/start').expect(404);
  });

  it('score recalculé côté serveur : seules les réponses dans le temps comptent, sans toucher aux révisions', async () => {
    const { agent, email } = await signUp(ctx.app);
    await learnKanji(agent);
    const user = await ctx.prisma.user.findUniqueOrThrow({ where: { email } });
    const cardsBefore = await ctx.prisma.reviewCard.findMany({ where: { userId: user.id }, orderBy: { id: 'asc' } });

    const game = await agent.post('/api/games/kanji-rush/start').expect(201);
    expect(game.body.questions.length).toBe(60);
    expect(game.body.questions[0].phase).toBe('game');
    expect(game.body.questions[0].answer).toBeUndefined();
    await agent.post('/api/games/kanji-rush/finish').send({ sessionId: game.body.sessionId }).expect(400); // trop tôt

    const qs = game.body.questions;
    for (const q of qs.slice(0, 12)) await agent.post(`/api/questions/${q.id}/answer`).send({ answer: await correctAnswer(ctx.prisma, q.id), responseMs: 900 }).expect(200);
    const wrong = qs[12];
    const r = await agent.post(`/api/questions/${wrong.id}/answer`).send({ answer: wrongAnswer(wrong, await correctAnswer(ctx.prisma, wrong.id)), responseMs: 900 }).expect(200);
    expect(r.body.xpGained).toBe(0);
    await agent.post(`/api/questions/${wrong.id}/retry`).expect(400);

    // Après la fin du chrono : réponses non comptées
    ctx.clock.advance(70_000);
    for (const q of qs.slice(13, 18)) await agent.post(`/api/questions/${q.id}/answer`).send({ answer: await correctAnswer(ctx.prisma, q.id), responseMs: 900 }).expect(200);
    const res = await agent.post('/api/games/kanji-rush/finish').send({ sessionId: game.body.sessionId }).expect(200);
    expect(res.body).toMatchObject({ score: 12, answered: 13, bestScore: 12, newBest: true, xpGained: 24, coinsGained: 2 });
    await agent.post('/api/games/kanji-rush/finish').send({ sessionId: game.body.sessionId }).expect(409);

    const cardsAfter = await ctx.prisma.reviewCard.findMany({ where: { userId: user.id }, orderBy: { id: 'asc' } });
    expect(cardsAfter.map((c) => c.due.getTime())).toEqual(cardsBefore.map((c) => c.due.getTime()));

    const list = await agent.get('/api/games').expect(200);
    expect(list.body.games.find((g: any) => g.id === 'kanji-rush')).toMatchObject({ bestScore: 12, plays: 1, available: true });
    expect(list.body.coinsLeftToday).toBe(13);
  });

  it('plafonne les pièces de mini-jeux à 15 par jour', async () => {
    const { agent, email } = await signUp(ctx.app);
    await learnKanji(agent);
    const user = await ctx.prisma.user.findUniqueOrThrow({ where: { email } });
    const day = await ctx.prisma.dailyActivity.findFirstOrThrow({ where: { userId: user.id } });
    await ctx.prisma.dailyActivity.update({ where: { userId_dateKey: { userId: user.id, dateKey: day.dateKey } }, data: { gameCoins: 14 } });
    const game = await agent.post('/api/games/kanji-rush/start').expect(201);
    for (const q of game.body.questions.slice(0, 20)) await agent.post(`/api/questions/${q.id}/answer`).send({ answer: await correctAnswer(ctx.prisma, q.id), responseMs: 500 }).expect(200);
    ctx.clock.advance(61_000);
    const res = await agent.post('/api/games/kanji-rush/finish').send({ sessionId: game.body.sessionId }).expect(200);
    expect(res.body).toMatchObject({ score: 20, coinsGained: 1 });
    const other = await signUp(ctx.app);
    await other.agent.post('/api/games/kanji-rush/finish').send({ sessionId: game.body.sessionId }).expect(404);
  });
});
