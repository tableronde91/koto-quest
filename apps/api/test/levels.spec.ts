import { Ctx, completeFirstLesson, correctAnswer, createTestApp, resetUsers, signUp } from './helpers';

describe('Niveaux : parcours N4', () => {
  let ctx: Ctx;
  beforeAll(async () => {
    ctx = await createTestApp();
    await resetUsers(ctx.prisma);
  });
  afterAll(() => ctx.app.close());

  it('liste les niveaux disponibles et ouvre le N4 au premier monde, même pour un débutant', async () => {
    const { agent } = await signUp(ctx.app);
    const path = (await agent.get('/api/path/N4').expect(200)).body;
    expect(path.level.code).toBe('N4');
    expect(path.levels.map((l: any) => l.code)).toEqual(['N5', 'N4', 'N3', 'N2', 'N1']);
    // Le N3 s'ouvre lui aussi à sa première leçon
    const n3 = (await agent.get('/api/path/N3').expect(200)).body;
    expect(n3.level).toMatchObject({ code: 'N3', region: 'Cimes enneigées' });
    expect(n3.worlds).toHaveLength(9);
    expect(n3.worlds.at(-1)).toMatchObject({ slug: 'n3-final', exam: { slug: 'n3-jlpt' } });
    expect(n3.worlds[0].chapters[0].lessons[0]).toMatchObject({ slug: 'n3-you-da', status: 'available' });
    // Le N2 s'ouvre de la même façon : 8 îles à gardien, puis l'examen blanc
    const n2 = (await agent.get('/api/path/N2').expect(200)).body;
    expect(n2.level).toMatchObject({ code: 'N2', region: 'Capitale d’été' });
    expect(n2.worlds).toHaveLength(9);
    expect(n2.worlds.slice(0, 8).every((w: any) => w.boss && !w.exam && !w.comingSoon && w.progress.total === 3)).toBe(true);
    expect(n2.worlds.at(-1)).toMatchObject({ slug: 'n2-final', exam: { slug: 'n2-jlpt' } });
    // Le N1 : 8 îles à gardien, puis l'examen blanc
    const n1 = (await agent.get('/api/path/N1').expect(200)).body;
    expect(n1.level).toMatchObject({ code: 'N1', region: 'Domaine du shōgun' });
    expect(n1.worlds).toHaveLength(9);
    expect(n1.worlds.slice(0, 8).every((w: any) => w.boss && !w.exam && !w.comingSoon && w.progress.total === 3)).toBe(true);
    expect(n1.worlds.at(-1)).toMatchObject({ slug: 'n1-final', exam: { slug: 'n1-jlpt' } });
    expect(n1.worlds[0].chapters[0].lessons[0]).toMatchObject({ slug: 'n1-wo-motte', status: 'available' });
    expect(n2.worlds[0].chapters[0].lessons[0]).toMatchObject({ slug: 'n2-kara-suru-to', status: 'available' });
    expect(path.worlds.length).toBeGreaterThanOrEqual(3);
    const lessons = path.worlds.flatMap((w: any) => w.chapters.flatMap((c: any) => c.lessons));
    expect(lessons[0]).toMatchObject({ slug: 'n4-te-ru', status: 'available' });
    expect(lessons[1].status).toBe('locked');
    expect(path.worlds.filter((w: any) => !w.exam).every((w: any) => w.boss)).toBe(true);
    expect(path.worlds.at(-1)).toMatchObject({ slug: 'n4-final', exam: { slug: 'n4-jlpt' } });
  });

  it('les kana déjà connus (déclarés à l’onboarding) ne décalent pas le départ du N4', async () => {
    const { agent } = await signUp(ctx.app, { selfLevel: 'n5' });
    const path = (await agent.get('/api/path/N4').expect(200)).body;
    expect(path.worlds[0].optional).toBe(false);
    expect(path.worlds[0].chapters[0].lessons[0].status).toBe('available');
  });

  it('une leçon N4 se joue comme une leçon N5 et compte dans la progression du niveau', async () => {
    const { agent } = await signUp(ctx.app);
    const { done } = await completeFirstLesson(ctx, agent, 'n4-te-ru');
    expect(done.correct).toBe(done.total);
    expect(done.nextLessonSlug).toBe('n4-te-u');
    const path = (await agent.get('/api/path/N4').expect(200)).body;
    expect(path.levels.find((l: any) => l.code === 'N4').completed).toBe(1);
  });

  it('une fois le N5 terminé, la prochaine leçon conseillée est au N4', async () => {
    const { agent, email } = await signUp(ctx.app);
    const user = await ctx.prisma.user.findUniqueOrThrow({ where: { email } });
    const n5 = await ctx.prisma.lesson.findMany({ where: { chapter: { world: { levelCode: 'N5' } } } });
    await ctx.prisma.userLessonProgress.createMany({ data: n5.map((l) => ({ userId: user.id, lessonId: l.id, status: 'completed', attempts: 1, bestScore: 100, completedAt: new Date() })) });
    const dash = (await agent.get('/api/dashboard').expect(200)).body;
    expect(dash.nextLesson).toMatchObject({ slug: 'n4-te-ru' });
  });

  it('examen blanc N4 : 34 questions issues du contenu N4, conseils propres au N4', async () => {
    const { agent } = await signUp(ctx.app);
    const exam = await agent.post('/api/exams/n4-mock/start').expect(201);
    expect(exam.body.exam).toMatchObject({ title: 'Examen blanc JLPT N4', durationMin: 30 });
    const qs = exam.body.questions;
    expect(qs).toHaveLength(34);
    const issued = await ctx.prisma.issuedQuestion.findMany({ where: { id: { in: qs.map((q: any) => q.id) } } });
    const itemIds = issued.map((q) => q.itemId).filter((x): x is string => !!x);
    const items = await ctx.prisma.learningItem.findMany({ where: { id: { in: itemIds } }, include: { lessons: { include: { lesson: { include: { chapter: { include: { world: true } } } } } } } });
    expect(items.length).toBeGreaterThan(10);
    // Toutes les notions viennent des leçons N4 (un kanji déjà vu au N5, comme 雨, peut y être repris)
    expect(items.filter((i) => !i.lessons.some((l) => l.lesson.chapter.world.levelCode === 'N4')).map((i) => i.slug)).toEqual([]);
    const res = (await agent.post('/api/exams/n4-mock/submit').send({ sessionId: exam.body.sessionId, answers: {} }).expect(200)).body;
    expect(res).toMatchObject({ correct: 0, passed: false });
    expect(res.recommendations.join(' ')).toMatch(/N4/);
  });

  it('examen blanc N3 : 38 questions issues du contenu N3, conseils propres au N3', async () => {
    const { agent } = await signUp(ctx.app);
    const exam = await agent.post('/api/exams/n3-mock/start').expect(201);
    expect(exam.body.exam).toMatchObject({ title: 'Examen blanc JLPT N3', durationMin: 35 });
    const qs = exam.body.questions;
    expect(qs).toHaveLength(38);
    const issued = await ctx.prisma.issuedQuestion.findMany({ where: { id: { in: qs.map((q: any) => q.id) } } });
    const items = await ctx.prisma.learningItem.findMany({ where: { id: { in: issued.map((q) => q.itemId).filter((x): x is string => !!x) } } });
    expect(items.length).toBeGreaterThan(10);
    expect(items.every((i) => i.levelCode === 'N3')).toBe(true);
    const res = (await agent.post('/api/exams/n3-mock/submit').send({ sessionId: exam.body.sessionId, answers: {} }).expect(200)).body;
    expect(res).toMatchObject({ correct: 0, passed: false });
    expect(res.recommendations.join(' ')).toMatch(/N3/);
  });

  it('examen blanc N2 : 42 questions issues du contenu N2, conseils propres au N2', async () => {
    const { agent } = await signUp(ctx.app);
    const exam = await agent.post('/api/exams/n2-mock/start').expect(201);
    expect(exam.body.exam).toMatchObject({ title: 'Examen blanc JLPT N2', durationMin: 40 });
    const qs = exam.body.questions;
    expect(qs).toHaveLength(42);
    const issued = await ctx.prisma.issuedQuestion.findMany({ where: { id: { in: qs.map((q: any) => q.id) } } });
    const items = await ctx.prisma.learningItem.findMany({ where: { id: { in: issued.map((q) => q.itemId).filter((x): x is string => !!x) } } });
    expect(items.length).toBeGreaterThan(10);
    expect(items.every((i) => i.levelCode === 'N2')).toBe(true);
    const res = (await agent.post('/api/exams/n2-mock/submit').send({ sessionId: exam.body.sessionId, answers: {} }).expect(200)).body;
    expect(res).toMatchObject({ correct: 0, passed: false });
    expect(res.recommendations.join(' ')).toMatch(/N2/);
  });

  it('examen blanc N1 : 44 questions issues du contenu N1, conseils propres au N1', async () => {
    const { agent } = await signUp(ctx.app);
    const exam = await agent.post('/api/exams/n1-mock/start').expect(201);
    expect(exam.body.exam).toMatchObject({ title: 'Examen blanc JLPT N1', durationMin: 45 });
    const qs = exam.body.questions;
    expect(qs).toHaveLength(44);
    const issued = await ctx.prisma.issuedQuestion.findMany({ where: { id: { in: qs.map((q: any) => q.id) } } });
    const items = await ctx.prisma.learningItem.findMany({ where: { id: { in: issued.map((q) => q.itemId).filter((x): x is string => !!x) } } });
    expect(items.length).toBeGreaterThan(10);
    expect(items.every((i) => i.levelCode === 'N1')).toBe(true);
    const res = (await agent.post('/api/exams/n1-mock/submit').send({ sessionId: exam.body.sessionId, answers: {} }).expect(200)).body;
    expect(res).toMatchObject({ correct: 0, passed: false });
    expect(res.recommendations.join(' ')).toMatch(/N1/);
  });

  it.each([
    ['n4', 40, 90],
    ['n3', 40, 95],
    ['n2', 40, 90],
    ['n1', 35, 100],
  ])('examen blanc %s au format officiel : barème du JLPT, réussite seulement au total et aux minimums', async (lv, n, pass) => {
    const { agent } = await signUp(ctx.app);
    const exam = (await agent.post(`/api/exams/${lv}-jlpt/start`).expect(201)).body;
    expect(exam.questions).toHaveLength(n);
    // Tout juste sauf l'écoute : le total est là, mais pas le minimum en écoute
    const answers: Record<string, unknown> = {};
    for (const q of exam.questions) if (q.section !== 'listening') answers[q.id] = await correctAnswer(ctx.prisma, q.id);
    const res = (await agent.post(`/api/exams/${lv}-jlpt/submit`).send({ sessionId: exam.sessionId, answers }).expect(200)).body;
    expect(res).toMatchObject({ passed: false, scaled: { listening: 0, max: { total: 180, passTotal: pass } } });
    expect(res.scaled.total).toBe(120);
  });

  it('niveau JLPT inconnu : 400', async () => {
    const { agent } = await signUp(ctx.app);
    await agent.get('/api/path/N0').expect(400);
  });
});

describe('Contenus : identifiants des notions', () => {
  it('un même identifiant désigne toujours le même caractère ou mot, d’un fichier à l’autre', () => {
    const { readFileSync } = require('fs') as typeof import('fs');
    const { resolve } = require('path') as typeof import('path');
    const seen = new Map<string, Set<string>>();
    const walk = (o: unknown): void => {
      if (Array.isArray(o)) o.forEach(walk);
      else if (o && typeof o === 'object') {
        const r = o as Record<string, unknown>;
        if (typeof r.slug === 'string' && typeof r.front === 'string') {
          if (!seen.has(r.slug)) seen.set(r.slug, new Set());
          seen.get(r.slug)!.add(`${r.front}|${r.reading ?? ''}`);
        }
        Object.values(r).forEach(walk);
      }
    };
    for (const f of ['n5/n5', 'n4/n4', 'n3/n3', 'n2/n2', 'n1/n1', 'characters/characters', 'expressions/expressions'])
      walk(JSON.parse(readFileSync(resolve(__dirname, `../../../content/${f}.json`), 'utf8')));
    expect([...seen].filter(([, v]) => v.size > 1).map(([k, v]) => `${k}: ${[...v].join(' / ')}`)).toEqual([]);
  });
});
