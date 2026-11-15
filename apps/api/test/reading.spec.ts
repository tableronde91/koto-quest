import { readFileSync } from 'fs';
import { resolve } from 'path';
import { stripRuby } from '@koto/learning-engine';
import { Ctx, createTestApp, resetUsers, setNow, signUp } from './helpers';

const catalog = JSON.parse(readFileSync(resolve(__dirname, '../../../content/reading/stories.json'), 'utf8'));

describe('Lecture quotidienne', () => {
  let ctx: Ctx;
  beforeAll(async () => {
    ctx = await createTestApp();
    await resetUsers(ctx.prisma);
  });
  afterAll(() => {
    ctx.clock.reset();
    return ctx.app.close();
  });

  it('contenu : furigana bien formés, traductions, questions valides, chapitres de plus en plus longs', () => {
    const chapters = catalog.stories.flatMap((s: any) => s.chapters);
    expect(chapters.length).toBeGreaterThanOrEqual(28);
    const slugs = new Set(chapters.map((c: any) => c.slug));
    expect(slugs.size).toBe(chapters.length);
    for (const c of chapters) {
      for (const s of c.paragraphs.flat()) {
        expect(stripRuby(s.jp)).not.toMatch(/[{}|]/);
        expect(s.kana).not.toMatch(/[一-龯]/); // la version kana ne contient plus de kanji
        expect(s.fr.length).toBeGreaterThan(1);
        expect(s.en.length).toBeGreaterThan(1);
      }
      expect(c.questions.length).toBeGreaterThanOrEqual(2);
      for (const q of c.questions) {
        expect(q.choices.length).toBe(3);
        expect(q.answer).toBeGreaterThanOrEqual(0);
        expect(q.answer).toBeLessThan(3);
        for (const ch of q.choices) expect(ch.fr && ch.en).toBeTruthy();
      }
      expect(c.words.length).toBeGreaterThanOrEqual(6);
    }
    const len = (c: any) => c.paragraphs.flat().length;
    expect(len(chapters.at(-2))).toBeGreaterThan(len(chapters[0]) * 1.8);
  });

  it('un chapitre par jour, relecture libre, récompense unique, série de jours', async () => {
    setNow(ctx.clock, new Date('2026-11-10T09:00:00Z'));
    const { agent } = await signUp(ctx.app);
    const o = (await agent.get('/api/reading').expect(200)).body;
    expect(o.today.state).toBe('new');
    expect(o.today.chapter).toMatchObject({ slug: 'momotaro-1', day: 1, state: 'available' });
    expect(o.upcoming).toMatchObject({ slug: 'momotaro-2', state: 'locked' });
    expect(o.stories[0].chapters[1].state).toBe('locked');
    expect(o.totalChapters).toBeGreaterThanOrEqual(28);

    await agent.get('/api/reading/chapters/momotaro-2').expect(403);
    await agent.get('/api/reading/chapters/inconnu').expect(404);
    const ch = (await agent.get('/api/reading/chapters/momotaro-1').expect(200)).body;
    expect(ch.chapter.paragraphs[0][0].jp).toContain('{村|むら}');
    expect(JSON.stringify(ch.chapter.questions)).not.toContain('answer');
    expect(ch.result).toBeNull();

    await agent.post('/api/reading/chapters/momotaro-1/complete').send({ answers: [0] }).expect(400);
    const answers = catalog.stories[0].chapters[0].questions.map((q: any) => q.answer);
    const coins = (await agent.get('/api/me').expect(200)).body.coins;
    const r = (await agent.post('/api/reading/chapters/momotaro-1/complete').send({ answers, seconds: 120 }).expect(201)).body;
    expect(r).toMatchObject({ correct: answers.length, firstTime: true, xpGained: 15 + 5 * answers.length, coinsGained: 10, streak: 1, next: { slug: 'momotaro-2', state: 'locked' } });
    expect((await agent.get('/api/me').expect(200)).body.coins).toBe(coins + 10);

    // Relecture : aucune récompense, le chapitre suivant reste verrouillé jusqu'à demain
    const again = (await agent.post('/api/reading/chapters/momotaro-1/complete').send({ answers }).expect(201)).body;
    expect(again).toMatchObject({ firstTime: false, xpGained: 0, coinsGained: 0 });
    const done = (await agent.get('/api/reading').expect(200)).body;
    expect(done.today).toMatchObject({ state: 'done', chapter: { slug: 'momotaro-1', state: 'read' } });
    expect(done.chaptersRead).toBe(1);
    expect(done.charsRead).toBeGreaterThan(50);
    expect((await agent.get('/api/reading/chapters/momotaro-1').expect(200)).body.result).toMatchObject({ correct: answers.length, answers });
    await agent.post('/api/reading/chapters/momotaro-2/complete').send({ answers: [0, 0] }).expect(403);

    // Le lendemain (heure de Paris), le chapitre 2 s'ouvre
    setNow(ctx.clock, new Date('2026-11-11T07:00:00Z'));
    const next = (await agent.get('/api/reading').expect(200)).body;
    expect(next.today.chapter).toMatchObject({ slug: 'momotaro-2', state: 'available' });
    expect(next.streak).toBe(1);
    const r2 = (await agent.post('/api/reading/chapters/momotaro-2/complete').send({ answers: [9, 9] }).expect(201)).body;
    expect(r2).toMatchObject({ correct: 0, firstTime: true, coinsGained: 5, streak: 2 });

    const exp = (await agent.get('/api/me/export').expect(200)).body;
    expect(JSON.stringify(exp)).toContain('momotaro-2');
  });
});
