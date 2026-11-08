import { Ctx, createTestApp, resetUsers, signUp } from './helpers';

describe('Examen blanc et test de positionnement', () => {
  let ctx: Ctx;
  beforeAll(async () => {
    ctx = await createTestApp();
    await resetUsers(ctx.prisma);
  });
  afterEach(() => ctx.clock.reset());
  afterAll(() => ctx.app.close());

  const answersFor = async (ids: string[], correct: (i: number) => boolean) => {
    const qs = await ctx.prisma.issuedQuestion.findMany({ where: { id: { in: ids } } });
    const by = new Map(qs.map((q) => [q.id, q]));
    return Object.fromEntries(
      ids.map((id, i) => {
        const q = by.get(id)!;
        const ans = q.answer as string | string[];
        const pub = q.payload as { choices?: string[] };
        return [id, correct(i) ? ans : Array.isArray(ans) ? [...ans].reverse() : pub.choices!.find((c) => c !== ans)];
      }),
    );
  };

  it('examen : structure, aucune correction pendant l’épreuve, copie corrigée par le serveur', async () => {
    const { agent, email } = await signUp(ctx.app);
    const path = await agent.get('/api/path/n5').expect(200);
    const final = path.body.worlds.find((w: any) => w.slug === 'n5-final');
    expect(final).toMatchObject({ comingSoon: false, exam: { slug: 'n5-jlpt', attempts: 0, bestPercent: null, passed: false } });

    const exam = await agent.post('/api/exams/n5-mock/start').expect(201);
    expect(exam.body.exam).toMatchObject({ durationMin: 25, passPercent: 60 });
    const qs = exam.body.questions;
    expect(qs).toHaveLength(30);
    expect(qs.filter((q: any) => q.section === 'listening')).toHaveLength(8);
    expect(qs.every((q: any) => q.answer === undefined && q.phase === 'exam')).toBe(true);
    // Pas de correction question par question
    await agent.post(`/api/questions/${qs[0].id}/answer`).send({ answer: 'x', responseMs: 1000 }).expect(400);

    const ids = qs.map((q: any) => q.id);
    const answers = await answersFor(ids, (i) => qs[i].section !== 'listening' || i % 2 === 0);
    const res = await agent.post('/api/exams/n5-mock/submit').send({ sessionId: exam.body.sessionId, answers }).expect(200);
    expect(res.body).toMatchObject({ total: 30, correct: 26, percent: 87, passed: true, late: false, coinsGained: 20, xpGained: 26 * 2 + 30 });
    expect(res.body.sections.find((s: any) => s.id === 'listening')).toMatchObject({ correct: 4, total: 8, percent: 50 });
    expect(res.body.mistakes).toHaveLength(4);
    expect(res.body.mistakes[0]).toMatchObject({ section: 'listening' });
    expect(res.body.recommendations[0]).toMatch(/Listening Ninja/);
    await agent.post('/api/exams/n5-mock/submit').send({ sessionId: exam.body.sessionId, answers }).expect(409);

    // Les notions ratées entrent en révision
    const user = await ctx.prisma.user.findUniqueOrThrow({ where: { email } });
    expect(await ctx.prisma.reviewCard.count({ where: { userId: user.id } })).toBeGreaterThanOrEqual(1);

    // Deuxième réussite : pas de nouvelles pièces ; copie vide rendue en retard
    const again = await agent.post('/api/exams/n5-mock/start').expect(201);
    ctx.clock.advance(30 * 60_000);
    const empty = await agent.post('/api/exams/n5-mock/submit').send({ sessionId: again.body.sessionId, answers: {} }).expect(200);
    expect(empty.body).toMatchObject({ percent: 0, passed: false, late: true, coinsGained: 0 });
    ctx.clock.reset();

    const stats = await agent.get('/api/stats').expect(200);
    expect(stats.body.exams.map((e: any) => e.percent)).toEqual([87, 0]);
    const path2 = await agent.get('/api/path/n5').expect(200);
    // L'île finale affiche l'examen au format officiel : l'entraînement n'y compte pas.
    expect(path2.body.worlds.find((w: any) => w.slug === 'n5-final').exam).toMatchObject({ slug: 'n5-jlpt', attempts: 0 });

    const other = await signUp(ctx.app);
    await other.agent.post('/api/exams/n5-mock/submit').send({ sessionId: again.body.sessionId, answers: {} }).expect(404);
  });

  it('positionnement : avance monde par monde, s’arrête au premier échec, valide les mondes réussis', async () => {
    const { agent, email } = await signUp(ctx.app);
    expect((await agent.get('/api/dashboard')).body.suggestPlacement).toBe(true);
    let step = (await agent.post('/api/placement/start').expect(201)).body;
    expect(step).toMatchObject({ done: false, block: { index: 0, world: { slug: 'n5-w1' } } });
    expect(step.block.questions).toHaveLength(3);
    await agent.post(`/api/questions/${step.block.questions[0].id}/answer`).send({ answer: 'x', responseMs: 1 }).expect(400);

    // Réussit les mondes 1 et 2, échoue au monde 3
    for (const expected of ['n5-w2', null]) {
      const ids = step.block.questions.map((q: any) => q.id);
      step = (await agent.post('/api/placement/answer').send({ sessionId: step.block.sessionId, answers: await answersFor(ids, (i) => i < 2) }).expect(200)).body;
      if (expected) expect(step).toMatchObject({ done: false, lastPassed: true, block: { world: { slug: expected } } });
    }
    expect(step.block.world.slug).toBe('n5-w3');
    const ids = step.block.questions.map((q: any) => q.id);
    const sessionId = step.block.sessionId;
    const done = (await agent.post('/api/placement/answer').send({ sessionId, answers: await answersFor(ids, (i) => i === 0) }).expect(200)).body;
    expect(done).toMatchObject({ done: true, stoppedAt: { slug: 'n5-w3' }, nextLesson: { slug: 'n5-greetings' } });
    expect(done.validated.map((w: any) => w.slug)).toEqual(['n5-w1', 'n5-w2']);
    await agent.post('/api/placement/answer').send({ sessionId, answers: {} }).expect(409);

    const path = (await agent.get('/api/path/n5')).body;
    const w1 = path.worlds.find((w: any) => w.slug === 'n5-w1');
    expect(w1.progress.completed).toBe(w1.progress.total);
    expect(w1.boss.available).toBe(true);
    const user = await ctx.prisma.user.findUniqueOrThrow({ where: { email } });
    const cards = await ctx.prisma.reviewCard.findMany({ where: { userId: user.id } });
    expect(cards.length).toBeGreaterThanOrEqual(46 + 10);
    expect(cards.every((c) => c.state === 'review' && c.due.getTime() > Date.now() + 86_400_000)).toBe(true);
    expect((await agent.get('/api/dashboard')).body.suggestPlacement).toBe(false);
  });

  it('examen au format officiel : 67 questions en japonais, barème JLPT sur 180, minimums par section', async () => {
    const { agent } = await signUp(ctx.app);
    const exam = await agent.post('/api/exams/n5-jlpt/start').expect(201);
    expect(exam.body.exam).toMatchObject({ title: 'Examen blanc JLPT N5 — format officiel', durationMin: 70 });
    const qs = exam.body.questions;
    expect(qs).toHaveLength(67);
    expect(qs.every((q: any) => q.answer === undefined && /[぀-ヿ一-龯]/.test(q.prompt))).toBe(true);
    expect(qs.filter((q: any) => q.section === 'listening').every((q: any) => q.type === 'listening_choice' && q.audio)).toBe(true);
    // Tout juste sauf l'écoute : 120 points mais minimum d'écoute (19/60) non atteint
    const answers = await answersFor(qs.map((q: any) => q.id), (i) => qs[i].section !== 'listening');
    const res = (await agent.post('/api/exams/n5-jlpt/submit').send({ sessionId: exam.body.sessionId, answers }).expect(200)).body;
    expect(res.scaled).toMatchObject({ language: 120, listening: 0, total: 120, max: { total: 180, passTotal: 80 } });
    expect(res.passed).toBe(false);
    expect(res.mistakes.find((m: any) => m.section === 'listening').explanation).toMatch(/Transcription|Phrase entendue|Situation/);
    // Copie complète juste : 180/180
    const again = await agent.post('/api/exams/n5-jlpt/start').expect(201);
    const all = await answersFor(again.body.questions.map((q: any) => q.id), () => true);
    const full = (await agent.post('/api/exams/n5-jlpt/submit').send({ sessionId: again.body.sessionId, answers: all }).expect(200)).body;
    expect(full).toMatchObject({ passed: true, percent: 100, scaled: { total: 180 } });
  });
});
