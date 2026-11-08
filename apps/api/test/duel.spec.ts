import { DUEL_RULES } from '@koto/learning-engine';
import { Agent, Ctx, createTestApp, resetUsers, signUp } from './helpers';

describe('Duels', () => {
  let ctx: Ctx;
  beforeAll(async () => {
    ctx = await createTestApp();
    await resetUsers(ctx.prisma);
  });
  afterAll(() => ctx.app.close());
  afterEach(() => ctx.clock.reset());

  const goodAnswer = async (duelId: string, round: number) => {
    const d = await ctx.prisma.duel.findUniqueOrThrow({ where: { id: duelId } });
    return String((d.questions as any[])[round].answer);
  };
  const badAnswer = async (duelId: string, round: number) => {
    const d = await ctx.prisma.duel.findUniqueOrThrow({ where: { id: duelId } });
    const q = (d.questions as any[])[round];
    return q.choices.find((c: string) => c !== q.answer);
  };
  /** Avance jusqu'au début de la question en cours. */
  const toRoundStart = async (duelId: string) => {
    const d = await ctx.prisma.duel.findUniqueOrThrow({ where: { id: duelId } });
    const wait = d.roundStartsAt!.getTime() - ctx.clock.now().getTime();
    if (wait > 0) ctx.clock.advance(wait + 1);
  };

  async function matchTwo(): Promise<{ a: Agent; b: Agent; duelId: string }> {
    const a = (await signUp(ctx.app)).agent;
    const b = (await signUp(ctx.app)).agent;
    expect((await a.post('/api/duels/queue').expect(200)).body.status).toBe('searching');
    const mb = await b.post('/api/duels/queue').expect(200);
    expect(mb.body.status).toBe('matched');
    const ma = await a.get('/api/duels/queue').expect(200);
    expect(ma.body).toEqual({ status: 'matched', duelId: mb.body.duelId });
    return { a, b, duelId: mb.body.duelId };
  }

  it('matchmaking : deux joueurs en file sont associés, la même question arrive au même instant, sans la réponse', async () => {
    const { a, b, duelId } = await matchTwo();
    const s0 = await a.get(`/api/duels/${duelId}`).expect(200);
    expect(s0.body).toMatchObject({ status: 'active', kind: 'ranked', round: 0, question: null });
    expect(s0.body.me.hp).toBe(DUEL_RULES.hp);
    await toRoundStart(duelId);
    const qa = (await a.get(`/api/duels/${duelId}`).expect(200)).body.question;
    const qb = (await b.get(`/api/duels/${duelId}`).expect(200)).body.question;
    expect(qa).toEqual(qb);
    expect(qa.choices.length).toBeGreaterThanOrEqual(3);
    expect(JSON.stringify(qa)).not.toContain('"answer"');
  });

  it('plus on répond vite, plus on fait de dégâts ; le K.-O. met à jour le classement', async () => {
    const { a, b, duelId } = await matchTwo();
    let state: any;
    for (let r = 0; r < DUEL_RULES.rounds; r++) {
      await toRoundStart(duelId);
      ctx.clock.advance(r === 0 ? 1000 : 500);
      // A répond vite et juste ; B lentement (et faux une fois sur deux)
      const ra = await a.post(`/api/duels/${duelId}/answer`).send({ round: r, answer: await goodAnswer(duelId, r) }).expect(200);
      expect(ra.body.mine).toMatchObject({ correct: true });
      if (r === 0) {
        expect(ra.body.mine.critical).toBe(true);
        expect(ra.body.opponentAnswered).toBe(false);
        await a.post(`/api/duels/${duelId}/answer`).send({ round: 0, answer: 'x' }).expect(409);
      }
      ctx.clock.advance(6000);
      state = (await b.post(`/api/duels/${duelId}/answer`).send({ round: r, answer: r % 2 ? await badAnswer(duelId, r) : await goodAnswer(duelId, r) }).expect(200)).body;
      if (state.status === 'finished') break;
      expect(state.last.me.damage).toBeLessThan(state.last.opponent.damage);
      expect(state.last.answer).toBe(await goodAnswer(duelId, r));
    }
    expect(state.status).toBe('finished');
    expect(state.result).toMatchObject({ outcome: 'loss', endReason: 'ko', ratingBefore: 1000, delta: -16 });
    const ra = (await a.get(`/api/duels/${duelId}`).expect(200)).body;
    expect(ra.result).toMatchObject({ outcome: 'win', ratingAfter: 1016, xp: 30, coins: 15 });
    expect(ra.opponent.hp).toBe(0);

    const lobbyA = (await a.get('/api/duels').expect(200)).body;
    expect(lobbyA.profile).toMatchObject({ rating: 1016, wins: 1, losses: 0, streak: 1 });
    expect(lobbyA.history[0]).toMatchObject({ result: 'win', delta: 16, endReason: 'ko' });
    const board = (await b.get('/api/duels/leaderboard?sort=wins').expect(200)).body;
    expect(board.entries[0]).toMatchObject({ wins: 1, rating: 1016 });
    expect(board.me).toMatchObject({ rating: 984 });
  });

  it('sans réponse, la question est corrigée à la fin du chrono', async () => {
    const { a, b, duelId } = await matchTwo();
    await toRoundStart(duelId);
    ctx.clock.advance(DUEL_RULES.roundMs + DUEL_RULES.graceMs + 10);
    await b.get(`/api/duels/${duelId}`).expect(200);
    const s = (await a.get(`/api/duels/${duelId}`).expect(200)).body;
    expect(s.round).toBe(1);
    expect(s.last.me).toMatchObject({ answer: null, damage: 0 });
    expect(s.me.hp).toBe(DUEL_RULES.hp);
    await a.post(`/api/duels/${duelId}/answer`).send({ round: 0, answer: 'x' }).expect(409);
  });

  it('défi par code : accepter, refuser, et abandon', async () => {
    const a = (await signUp(ctx.app)).agent;
    const b = (await signUp(ctx.app)).agent;
    const codeB = (await b.get('/api/duels').expect(200)).body.profile.code;
    expect(codeB).toMatch(/^KQ-[A-Z0-9]{6}$/);
    await a.post('/api/duels/challenges').send({ code: 'KQ-ZZZZZZ' }).expect(404);
    const codeA = (await a.get('/api/duels').expect(200)).body.profile.code;
    await a.post('/api/duels/challenges').send({ code: codeA }).expect(400);

    // Refus
    const c1 = await a.post('/api/duels/challenges').send({ code: codeB.toLowerCase() }).expect(201);
    const inv = (await b.get('/api/duels').expect(200)).body.invites;
    expect(inv).toHaveLength(1);
    expect(inv[0].id).toBe(c1.body.duelId);
    await a.post(`/api/duels/${c1.body.duelId}/accept`).expect(404);
    await b.post(`/api/duels/${c1.body.duelId}/decline`).expect(200);
    expect((await a.get(`/api/duels/${c1.body.duelId}`).expect(200)).body.status).toBe('declined');

    // Acceptation puis abandon
    const c2 = await a.post('/api/duels/challenges').send({ code: codeB }).expect(201);
    expect((await a.get(`/api/duels/${c2.body.duelId}`).expect(200)).body.status).toBe('pending');
    await b.post(`/api/duels/${c2.body.duelId}/accept`).expect(200);
    const s = (await a.get(`/api/duels/${c2.body.duelId}`).expect(200)).body;
    expect(s).toMatchObject({ status: 'active', kind: 'friendly' });
    const out = (await b.post(`/api/duels/${c2.body.duelId}/forfeit`).expect(200)).body;
    expect(out.result).toMatchObject({ outcome: 'loss', endReason: 'forfeit', delta: 0, xp: 0 });
    // Un duel amical ne change pas le classement
    expect((await a.get('/api/duels').expect(200)).body.profile).toMatchObject({ rating: 1000, wins: 0 });

    // Un défi expire
    const c3 = await a.post('/api/duels/challenges').send({ code: codeB }).expect(201);
    ctx.clock.advance(DUEL_RULES.inviteTtlMs + 1000);
    await b.post(`/api/duels/${c3.body.duelId}/accept`).expect(409);
  });

  it('recherche de joueurs et isolation : impossible de lire le duel des autres', async () => {
    const { duelId } = await matchTwo();
    const c = (await signUp(ctx.app)).agent;
    await c.get(`/api/duels/${duelId}`).expect(404);
    await c.post(`/api/duels/${duelId}/answer`).send({ round: 0, answer: 'a' }).expect(404);
    const found = (await c.get('/api/duels/players?q=testeur').expect(200)).body.players;
    expect(found.length).toBeGreaterThan(0);
    expect(found[0].code).toMatch(/^KQ-/);
  });

  it('un joueur qui ne donne plus signe de vie perd par abandon', async () => {
    const { a, duelId } = await matchTwo();
    await toRoundStart(duelId);
    for (let i = 0; i < 3; i++) {
      ctx.clock.advance(10_000);
      await a.get(`/api/duels/${duelId}`).expect(200);
    }
    const s = (await a.get(`/api/duels/${duelId}`).expect(200)).body;
    expect(s.result).toMatchObject({ outcome: 'win', endReason: 'forfeit' });
  });

  it('entraînement contre un rōnin : l’IA répond, sans effet sur le classement', async () => {
    const a = (await signUp(ctx.app)).agent;
    const { duelId } = (await a.post('/api/duels/practice').expect(201)).body;
    let s: any = (await a.get(`/api/duels/${duelId}`).expect(200)).body;
    expect(s.opponent).toMatchObject({ isBot: true });
    expect(s.kind).toBe('practice');
    for (let r = 0; r < DUEL_RULES.rounds && s.status === 'active'; r++) {
      await toRoundStart(duelId);
      ctx.clock.advance(800);
      s = (await a.post(`/api/duels/${duelId}/answer`).send({ round: r, answer: await goodAnswer(duelId, r) }).expect(200)).body;
      ctx.clock.advance(DUEL_RULES.roundMs + DUEL_RULES.graceMs);
      s = (await a.get(`/api/duels/${duelId}`).expect(200)).body;
    }
    expect(s.status).toBe('finished');
    expect(s.result.outcome).toBe('win');
    expect(s.result.delta).toBe(0);
    expect((await a.get('/api/duels').expect(200)).body.profile).toMatchObject({ rating: 1000, wins: 0 });
  });
});
