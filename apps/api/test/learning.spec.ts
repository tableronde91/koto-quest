import { Ctx, completeFirstLesson, correctAnswer, createTestApp, resetUsers, signUp, wrongAnswer } from './helpers';

const HOUR = 3600_000;

describe('Parcours d’apprentissage et répétition espacée', () => {
  let ctx: Ctx;
  beforeAll(async () => {
    ctx = await createTestApp();
    await resetUsers(ctx.prisma);
  });
  afterEach(() => ctx.clock.reset());
  afterAll(() => ctx.app.close());

  const userByEmail = (email: string) => ctx.prisma.user.findUniqueOrThrow({ where: { email } });

  it('expose le parcours N5 avec déblocage progressif', async () => {
    const { agent } = await signUp(ctx.app);
    const path = await agent.get('/api/path/n5').expect(200);
    const lessons = path.body.worlds.flatMap((w: any) => w.chapters.flatMap((c: any) => c.lessons));
    expect(lessons[0]).toMatchObject({ slug: 'n5-hira-a', status: 'available' });
    expect(lessons[1].status).toBe('locked');
    expect(path.body.level.notice).toMatch(/pas des listes officielles/);
    await agent.post('/api/lessons/n5-hira-ka/start').expect(403);
    await agent.get('/api/lessons/n5-hira-ka').expect(403);
    await agent.get('/api/path/n9').expect(400);
  });

  it('commence au monde 3 pour qui connaît déjà les kana', async () => {
    const { agent } = await signUp(ctx.app, { selfLevel: 'kana' });
    const dash = await agent.get('/api/dashboard').expect(200);
    expect(dash.body.nextLesson.slug).toBe('n5-greetings');
    await agent.post('/api/lessons/n5-greetings/start').expect(201);
    await agent.post('/api/lessons/n5-hira-ka/start').expect(201); // mondes précédents accessibles en révision
  });

  it('émet des questions variées sans jamais exposer la réponse', async () => {
    const { agent } = await signUp(ctx.app, { selfLevel: 'kana' });
    const start = await agent.post('/api/lessons/n5-greetings/start').expect(201);
    const types = new Set(start.body.questions.map((q: any) => q.type));
    expect(types.size).toBeGreaterThanOrEqual(4);
    for (const q of start.body.questions) {
      expect(q.answer).toBeUndefined();
      expect(q.explanation).toBeUndefined();
    }
    expect(start.body.questions.length).toBeGreaterThanOrEqual(10);
  });

  it('corrige côté serveur, une seule fois par question, et sauvegarde réussites et erreurs', async () => {
    const { agent } = await signUp(ctx.app);
    const start = await agent.post('/api/lessons/n5-hira-a/start').expect(201);
    const [q1, q2] = start.body.questions;
    const ok = await agent.post(`/api/questions/${q1.id}/answer`).send({ answer: await correctAnswer(ctx.prisma, q1.id), responseMs: 3000 }).expect(200);
    expect(ok.body).toMatchObject({ correct: true, xpGained: 10, mastery: 'discovered' });
    expect(ok.body.explanation).toMatch(/se lit/);
    await agent.post(`/api/questions/${q1.id}/answer`).send({ answer: 'x', responseMs: 3000 }).expect(409);

    const ans2 = await correctAnswer(ctx.prisma, q2.id);
    const ko = await agent.post(`/api/questions/${q2.id}/answer`).send({ answer: wrongAnswer(q2, ans2), responseMs: 3000 }).expect(200);
    expect(ko.body).toMatchObject({ correct: false, correctAnswer: ans2, xpGained: 1 });

    const saved = await ctx.prisma.exerciseAnswer.findMany({ where: { questionId: { in: [q1.id, q2.id] } } });
    expect(saved.map((s) => s.correct).sort()).toEqual([false, true]);
    await agent.post('/api/lessons/n5-hira-a/complete').send({ sessionId: start.body.sessionId }).expect(400);
    await agent.post(`/api/questions/${start.body.questions[2].id}/answer`).send({ answer: { hack: true }, responseMs: 10 }).expect(400);
  });

  it('valide une leçon, débloque la suivante, propose une mini-révision et attribue l’XP côté serveur', async () => {
    const { agent, email } = await signUp(ctx.app);
    const { start, done } = await completeFirstLesson(ctx, agent, 'n5-hira-a', [0]);
    expect(done).toMatchObject({ perfect: false, nextLessonSlug: 'n5-hira-ka', xpGained: 30 });
    expect(done.miniReview.length).toBeGreaterThan(0);
    expect(done.miniReview[0].phase).toBe('mini_review');
    await agent.post('/api/lessons/n5-hira-a/complete').send({ sessionId: start.sessionId }).expect(409);

    const n = start.questions.length;
    // (n-1) bonnes réponses × 10 + 1 erreur × 1 + 30 de fin de leçon (hors quêtes du jour, comptées à part)
    const user = await userByEmail(email);
    const questXp = (await ctx.prisma.xpEvent.aggregate({ where: { userId: user.id, reason: 'quest' }, _sum: { amount: true } }))._sum.amount ?? 0;
    expect(user.xp - questXp).toBe((n - 1) * 10 + 1 + 30);

    const path = await agent.get('/api/path/n5').expect(200);
    const lessons = path.body.worlds[0].chapters.flatMap((c: any) => c.lessons);
    expect(lessons[0].status).toBe('completed');
    expect(lessons[1].status).toBe('available');
  });

  it('fait reprendre en fin de séance un exercice raté, sans fausser le score ni la planification', async () => {
    const { agent, email } = await signUp(ctx.app);
    const start = await agent.post('/api/lessons/n5-hira-a/start').expect(201);
    const [first, ...rest] = start.body.questions;
    const ans = await correctAnswer(ctx.prisma, first.id);

    // Impossible de reprendre une question pas encore répondue ou réussie
    await agent.post(`/api/questions/${first.id}/retry`).expect(400);
    await agent.post(`/api/questions/${first.id}/answer`).send({ answer: wrongAnswer(first, ans), responseMs: 3000 }).expect(200);
    const user = await userByEmail(email);
    const cardBefore = await ctx.prisma.reviewCard.findFirstOrThrow({ where: { userId: user.id, item: { slug: 'hira-a' } } });

    const r1 = await agent.post(`/api/questions/${first.id}/retry`).expect(201);
    expect(r1.body).toMatchObject({ type: first.type, prompt: first.prompt, phase: 'lesson', retryOf: first.id });
    expect(r1.body.id).not.toBe(first.id);
    expect(r1.body.answer).toBeUndefined();
    expect([...r1.body.choices].sort()).toEqual([...first.choices].sort());
    // Idempotent
    expect((await agent.post(`/api/questions/${first.id}/retry`).expect(201)).body.id).toBe(r1.body.id);

    // Deuxième erreur → une seconde reprise, puis plus rien
    await agent.post(`/api/questions/${r1.body.id}/answer`).send({ answer: wrongAnswer(r1.body, ans), responseMs: 3000 }).expect(200);
    const r2 = await agent.post(`/api/questions/${r1.body.id}/retry`).expect(201);
    await agent.post(`/api/questions/${r2.body.id}/answer`).send({ answer: wrongAnswer(r2.body, ans), responseMs: 3000 }).expect(200);
    await agent.post(`/api/questions/${r2.body.id}/retry`).expect(409);

    // Les reprises ne replanifient pas la carte une seconde fois dans la même séance
    const cardAfter = await ctx.prisma.reviewCard.findFirstOrThrow({ where: { id: cardBefore.id } });
    expect(cardAfter.due.getTime()).toBe(cardBefore.due.getTime());

    // Un autre utilisateur ne peut pas reprendre la question
    const other = await signUp(ctx.app);
    await other.agent.post(`/api/questions/${first.id}/retry`).expect(404);

    for (const q of rest) await agent.post(`/api/questions/${q.id}/answer`).send({ answer: await correctAnswer(ctx.prisma, q.id), responseMs: 3000 }).expect(200);
    const done = await agent.post('/api/lessons/n5-hira-a/complete').send({ sessionId: start.body.sessionId }).expect(200);
    expect(done.body).toMatchObject({ total: start.body.questions.length, correct: start.body.questions.length - 1, perfect: false });
  });

  it('rejouer une leçon ne permet pas d’accumuler les récompenses de fin', async () => {
    const { agent } = await signUp(ctx.app);
    await completeFirstLesson(ctx, agent);
    const { done } = await completeFirstLesson(ctx, agent);
    expect(done.xpGained).toBe(5);
  });

  it('planifie chaque notion individuellement : erreur = retour rapide, réussite = quelques heures', async () => {
    const { agent, email } = await signUp(ctx.app);
    const start = await agent.post('/api/lessons/n5-hira-a/start').expect(201);
    const t0 = Date.now();
    const recognition = start.body.questions.filter((q: any) => q.type === 'meaning_choice').slice(0, 2);
    for (const [i, q] of recognition.entries()) {
      const ans = await correctAnswer(ctx.prisma, q.id);
      await agent.post(`/api/questions/${q.id}/answer`).send({ answer: i === 0 ? ans : wrongAnswer(q, ans), responseMs: 4000 }).expect(200);
    }
    const user = await userByEmail(email);
    const qs = await ctx.prisma.issuedQuestion.findMany({ where: { id: { in: recognition.map((q: any) => q.id) } } });
    const cards = await ctx.prisma.reviewCard.findMany({ where: { userId: user.id } });
    const byItem = new Map(cards.map((c) => [c.itemId, c]));
    const good = byItem.get(qs.find((q) => q.correct)!.itemId!)!;
    const bad = byItem.get(qs.find((q) => !q.correct)!.itemId!)!;
    expect(good.due.getTime() - t0).toBeGreaterThan(3.9 * HOUR);
    expect(good.due.getTime() - t0).toBeLessThan(4.1 * HOUR);
    expect(bad.due.getTime() - t0).toBeLessThan(11 * 60_000);
    expect(bad.difficulty).toBeGreaterThan(good.difficulty);
  });

  it('retrouve ses révisions après reconnexion, et les intervalles s’allongent avec la réussite', async () => {
    const { agent, email } = await signUp(ctx.app);
    await completeFirstLesson(ctx, agent);
    let summary = await agent.get('/api/reviews/summary').expect(200);
    expect(summary.body.due).toBe(0);
    expect((await agent.post('/api/reviews/session').expect(201)).body.questions).toHaveLength(0);

    // Déconnexion, puis retour « quelques heures plus tard »
    await agent.post('/api/auth/logout').expect(204);
    ctx.clock.advance(5 * HOUR);
    await agent.post('/api/auth/login').send({ email, password: 'motdepasse123' }).expect(200);
    summary = await agent.get('/api/reviews/summary').expect(200);
    expect(summary.body.due).toBe(5);
    const session = await agent.post('/api/reviews/session').expect(201);
    expect(session.body.questions).toHaveLength(5);
    for (const q of session.body.questions) {
      expect(q.phase).toBe('review');
      await agent.post(`/api/questions/${q.id}/answer`).send({ answer: await correctAnswer(ctx.prisma, q.id), responseMs: 5000 }).expect(200);
    }
    const now = ctx.clock.now().getTime();
    const cards = await ctx.prisma.reviewCard.findMany({ where: { userId: (await userByEmail(email)).id } });
    for (const c of cards) {
      expect(c.state).toBe('review');
      expect(c.due.getTime() - now).toBeGreaterThanOrEqual(0.9 * 86_400_000);
    }
    expect((await agent.get('/api/reviews/summary')).body.due).toBe(0);

    const stats = await agent.get('/api/stats').expect(200);
    expect(stats.body.totals.reviews).toBeGreaterThanOrEqual(5);
    expect(stats.body.byKind.kana.learned).toBe(5);
    expect(stats.body.items).toHaveLength(5);
    expect(stats.body.days).toHaveLength(30);
  });

  it('alimente le tableau de bord : série, temps du jour, quêtes, préparation prudente', async () => {
    const { agent } = await signUp(ctx.app);
    await completeFirstLesson(ctx, agent);
    const d = (await agent.get('/api/dashboard').expect(200)).body;
    expect(d.streak).toMatchObject({ current: 1, todayDone: true });
    expect(d.today.seconds).toBeGreaterThan(0);
    expect(d.today.accuracy).toBe(100);
    expect(d.progress.completedLessons).toBe(1);
    expect(d.quests).toHaveLength(3);
    expect(d.readiness.percent).toBeLessThanOrEqual(90);
    expect(d.nextLesson.slug).toBe('n5-hira-ka');
  });
});
