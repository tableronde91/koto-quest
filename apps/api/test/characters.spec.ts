import { Ctx, completeFirstLesson, correctAnswer, createTestApp, resetUsers, signUp } from './helpers';

describe('Onglet Caractères', () => {
  let ctx: Ctx;
  beforeAll(async () => {
    ctx = await createTestApp();
    await resetUsers(ctx.prisma);
  });
  afterAll(() => ctx.app.close());

  it('expose hiragana, katakana et kanji à tous, sans déblocage', async () => {
    const { agent } = await signUp(ctx.app);
    const res = await agent.get('/api/characters').expect(200);
    const bySlug = Object.fromEntries(res.body.sections.map((s: any) => [s.slug, s]));
    expect(bySlug.hiragana.total).toBe(104);
    expect(bySlug.katakana.total).toBe(104);
    expect(bySlug.kanji.total).toBeGreaterThanOrEqual(50);
    expect(bySlug.hiragana.groups[0].items.map((i: any) => i.front)).toEqual(['あ', 'い', 'う', 'え', 'お']);
    expect(bySlug.kanji.groups[0].items[0]).toMatchObject({ front: '一', meaning: 'un', kanji: { onyomi: ['イチ', 'イツ'] } });
    expect(bySlug.hiragana.learned).toBe(0);
  });

  it('partage la maîtrise avec le parcours : une leçon de kana remplit la grille', async () => {
    const { agent } = await signUp(ctx.app);
    await completeFirstLesson(ctx, agent);
    const res = await agent.get('/api/characters').expect(200);
    const hira = res.body.sections.find((s: any) => s.slug === 'hiragana');
    expect(hira.learned).toBe(5);
    expect(hira.groups[0].items.every((i: any) => i.mastery !== null && i.score >= 0)).toBe(true);
  });

  it('lance une pratique ciblée, corrigée côté serveur, qui met à jour la maîtrise', async () => {
    const { agent } = await signUp(ctx.app);
    const s = await agent.post('/api/characters/practice').send({ scope: 'kata-k' }).expect(201);
    expect(s.body.questions.length).toBeGreaterThanOrEqual(10);
    for (const q of s.body.questions) {
      expect(q.phase).toBe('practice');
      expect(q.answer).toBeUndefined();
      // Choix uniquement en katakana ou en romaji, jamais de hiragana
      for (const c of q.choices ?? []) expect(c).not.toMatch(/[぀-ゟ]/);
      await agent.post(`/api/questions/${q.id}/answer`).send({ answer: await correctAnswer(ctx.prisma, q.id), responseMs: 3000 }).expect(200);
    }
    const res = await agent.get('/api/characters').expect(200);
    const kata = res.body.sections.find((x: any) => x.slug === 'katakana');
    expect(kata.groups.find((g: any) => g.slug === 'kata-k').items.every((i: any) => i.mastery !== null)).toBe(true);
    await agent.post('/api/characters/practice').send({ scope: 'inconnu' }).expect(404);
  });
});
