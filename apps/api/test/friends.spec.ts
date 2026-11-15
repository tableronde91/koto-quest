import { Ctx, createTestApp, resetUsers, signUp } from './helpers';

describe('Amis', () => {
  let ctx: Ctx;
  beforeAll(async () => {
    ctx = await createTestApp();
    await resetUsers(ctx.prisma);
  });
  afterAll(() => ctx.app.close());
  afterEach(() => ctx.clock.reset());

  const codeOf = async (agent: any) => (await agent.get('/api/duels').expect(200)).body.profile.code as string;

  it('demande par code, acceptation, présence en ligne, défi direct, bilan, retrait', async () => {
    const a = (await signUp(ctx.app)).agent;
    const b = (await signUp(ctx.app)).agent;
    const codeA = await codeOf(a);
    const codeB = await codeOf(b);

    await a.post('/api/friends').send({ code: codeA }).expect(400);
    await a.post('/api/friends').send({ code: 'KQ-ZZZZZZ' }).expect(404);
    await a.post('/api/friends').send({ code: 'pas un code' }).expect(400);
    const req = (await a.post('/api/friends').send({ code: codeB.replace('KQ-', '').toLowerCase() }).expect(201)).body;
    expect(req).toMatchObject({ status: 'pending', player: { code: codeB } });
    // Deuxième demande : pas de doublon
    expect((await a.post('/api/friends').send({ code: codeB }).expect(201)).body.id).toBe(req.id);

    const la = (await a.get('/api/friends').expect(200)).body;
    expect(la.outgoing).toHaveLength(1);
    expect(la.friends).toHaveLength(0);
    const incoming = (await b.get('/api/friends/requests').expect(200)).body;
    expect(incoming).toHaveLength(1);
    expect(incoming[0].player.code).toBe(codeA);
    expect(JSON.stringify(incoming)).not.toContain('@'); // jamais d'adresse e-mail

    // Le demandeur ne peut pas accepter à la place de l'invité
    await a.post(`/api/friends/${req.id}/accept`).expect(403);
    expect((await b.post(`/api/friends/${req.id}/accept`).expect(200)).body).toMatchObject({ status: 'accepted', player: { code: codeA } });
    await a.post('/api/friends').send({ code: codeB }).expect(409);

    // Présence : B ouvre l'application (sondage des défis), A le voit en ligne
    await b.get('/api/duels/invites').expect(200);
    let fa = (await a.get('/api/friends').expect(200)).body.friends;
    expect(fa).toHaveLength(1);
    expect(fa[0]).toMatchObject({ online: true, record: { wins: 0, losses: 0, draws: 0 }, pendingDuelId: null, player: { code: codeB } });
    ctx.clock.advance(60_000);
    expect((await a.get('/api/friends').expect(200)).body.friends[0].online).toBe(false);

    // Recherche : le lien d'amitié est indiqué
    const name = fa[0].player.name;
    const search = (await a.get(`/api/duels/players?q=${encodeURIComponent(codeB)}`).expect(200)).body.players;
    expect(search[0]).toMatchObject({ code: codeB, relation: 'friend', friendshipId: req.id });
    expect(name).toBeTruthy();

    // Défi direct depuis la liste d'amis, puis abandon : le bilan compte la victoire
    const duelId = (await a.post('/api/duels/challenges').send({ userId: fa[0].player.userId }).expect(201)).body.duelId;
    fa = (await a.get('/api/friends').expect(200)).body.friends;
    expect(fa[0].pendingDuelId).toBe(duelId);
    await b.post(`/api/duels/${duelId}/accept`).expect(200);
    await b.post(`/api/duels/${duelId}/forfeit`).expect(200);
    fa = (await a.get('/api/friends').expect(200)).body.friends;
    expect(fa[0].record).toEqual({ wins: 1, losses: 0, draws: 0 });
    expect((await b.get('/api/friends').expect(200)).body.friends[0].record).toEqual({ wins: 0, losses: 1, draws: 0 });

    // Retrait : disparaît des deux côtés
    await b.delete(`/api/friends/${req.id}`).expect(200);
    expect((await a.get('/api/friends').expect(200)).body.friends).toHaveLength(0);
    await a.delete(`/api/friends/${req.id}`).expect(404);
  });

  it('demandes croisées : la seconde accepte la première ; refus ; un tiers ne peut rien faire', async () => {
    const a = (await signUp(ctx.app)).agent;
    const b = (await signUp(ctx.app)).agent;
    const c = (await signUp(ctx.app)).agent;
    const codeA = await codeOf(a);
    const codeB = await codeOf(b);
    const r1 = (await a.post('/api/friends').send({ code: codeB }).expect(201)).body;
    await c.post(`/api/friends/${r1.id}/accept`).expect(404);
    await c.delete(`/api/friends/${r1.id}`).expect(404);
    const r2 = (await b.post('/api/friends').send({ code: codeA }).expect(201)).body;
    expect(r2).toMatchObject({ id: r1.id, status: 'accepted' });

    const codeC = await codeOf(c);
    const r3 = (await a.post('/api/friends').send({ code: codeC }).expect(201)).body;
    await c.delete(`/api/friends/${r3.id}`).expect(200); // refus
    expect((await a.get('/api/friends').expect(200)).body.outgoing).toHaveLength(0);
  });

  it('les données d’amis sont dans l’export et supprimées avec le compte', async () => {
    const a = (await signUp(ctx.app)).agent;
    const b = (await signUp(ctx.app)).agent;
    const codeB = await codeOf(b);
    await a.post('/api/friends').send({ code: codeB }).expect(201);
    const exp = (await a.get('/api/me/export').expect(200)).body;
    expect(JSON.stringify(exp)).toContain('friendsAsked');
    await b.delete('/api/me').send({ password: 'motdepasse123' }).expect(204);
    const after = (await a.get('/api/friends').expect(200)).body;
    expect(after.outgoing).toHaveLength(0);
  });
});
