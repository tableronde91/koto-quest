import { Ctx, createTestApp, resetUsers, signUp } from './helpers';

describe('Expressions', () => {
  let ctx: Ctx;
  beforeAll(async () => {
    ctx = await createTestApp();
    await resetUsers(ctx.prisma);
  });
  afterAll(() => ctx.app.close());

  it('recueil par thèmes, entraînement, maîtrise partagée avec les révisions', async () => {
    const { agent } = await signUp(ctx.app);
    const o = (await agent.get('/api/expressions').expect(200)).body;
    expect(o.themes.length).toBe(10);
    const polite = o.themes.find((t: any) => t.slug === 'politesse');
    expect(polite).toMatchObject({ glyph: '礼', learned: 0, total: polite.expressions.length });
    const yoro = polite.expressions.find((e: any) => e.front === 'よろしくお願いします');
    expect(yoro).toMatchObject({ reading: 'よろしくおねがいします', register: 'polite', mastery: null });
    expect(yoro.note).toContain('présenté');
    expect(yoro.example.jp).toContain('よろしく');

    await agent.post('/api/expressions/practice').send({ theme: 'inconnu' }).expect(404);
    const s = (await agent.post('/api/expressions/practice').send({ theme: 'politesse' }).expect(201)).body;
    expect(s.questions.length).toBeGreaterThanOrEqual(5);
    expect(JSON.stringify(s.questions)).not.toContain('"answer"');
    for (const q of s.questions) {
      const r = await agent.post(`/api/questions/${q.id}/answer`).send({ answer: q.choices?.[0] ?? q.pairs?.right ?? 'x', responseMs: 2000 });
      expect([200, 201]).toContain(r.status);
    }
    const after = (await agent.get('/api/expressions').expect(200)).body.themes.find((t: any) => t.slug === 'politesse');
    expect(after.learned).toBeGreaterThan(0);
  });
});
