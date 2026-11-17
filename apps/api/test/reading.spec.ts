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

  it('tous les chapitres ouverts, chapitre conseillé, relecture libre, récompense unique, série de jours', async () => {
    setNow(ctx.clock, new Date('2026-11-10T09:00:00Z'));
    const { agent } = await signUp(ctx.app);
    const o = (await agent.get('/api/reading').expect(200)).body;
    expect(o.today.state).toBe('new');
    expect(o.today.chapter).toMatchObject({ slug: 'momotaro-1', day: 1, state: 'available' });
    expect(o.upcoming).toMatchObject({ slug: 'momotaro-2', state: 'available' });
    // Rien n'est verrouillé : tous les chapitres de tous les contes sont disponibles dès le départ
    expect(o.stories.flatMap((s: any) => s.chapters).every((c: any) => c.state === 'available')).toBe(true);
    expect(o.totalChapters).toBeGreaterThanOrEqual(28);

    const last = catalog.stories.at(-1).chapters.at(-1);
    expect((await agent.get(`/api/reading/chapters/${last.slug}`).expect(200)).body).toMatchObject({ state: 'available', next: null });
    await agent.get('/api/reading/chapters/inconnu').expect(404);
    const ch = (await agent.get('/api/reading/chapters/momotaro-1').expect(200)).body;
    expect(ch.chapter.paragraphs[0][0].jp).toContain('{村|むら}');
    expect(JSON.stringify(ch.chapter.questions)).not.toContain('answer');
    expect(ch.result).toBeNull();

    await agent.post('/api/reading/chapters/momotaro-1/complete').send({ answers: [0] }).expect(400);
    const answers = catalog.stories[0].chapters[0].questions.map((q: any) => q.answer);
    const coins = (await agent.get('/api/me').expect(200)).body.coins;
    const r = (await agent.post('/api/reading/chapters/momotaro-1/complete').send({ answers, seconds: 120 }).expect(201)).body;
    expect(r).toMatchObject({ correct: answers.length, firstTime: true, xpGained: 15 + 5 * answers.length, coinsGained: 10, streak: 1, next: { slug: 'momotaro-2', state: 'available' } });
    expect((await agent.get('/api/me').expect(200)).body.coins).toBe(coins + 10);

    // Relecture : aucune récompense
    const again = (await agent.post('/api/reading/chapters/momotaro-1/complete').send({ answers }).expect(201)).body;
    expect(again).toMatchObject({ firstTime: false, xpGained: 0, coinsGained: 0 });
    const done = (await agent.get('/api/reading').expect(200)).body;
    expect(done.today).toMatchObject({ state: 'done', chapter: { slug: 'momotaro-1', state: 'read' } });
    expect(done.upcoming).toMatchObject({ slug: 'momotaro-2', state: 'available' });
    expect(done.chaptersRead).toBe(1);
    expect(done.charsRead).toBeGreaterThan(50);
    expect((await agent.get('/api/reading/chapters/momotaro-1').expect(200)).body.result).toMatchObject({ correct: answers.length, answers });

    // Le même jour, on peut enchaîner : un chapitre d'un autre conte, lu dans le désordre, est récompensé lui aussi
    const other = catalog.stories[3].chapters[2];
    const same = (await agent.post(`/api/reading/chapters/${other.slug}/complete`).send({ answers: other.questions.map((q: any) => q.answer) }).expect(201)).body;
    expect(same).toMatchObject({ firstTime: true, streak: 1 });
    expect((await agent.get('/api/reading').expect(200)).body).toMatchObject({ chaptersRead: 2, today: { state: 'done', chapter: { slug: other.slug } }, upcoming: { slug: 'momotaro-2' } });

    // Le lendemain (heure de Paris), le conseil du jour est le premier chapitre pas encore lu
    setNow(ctx.clock, new Date('2026-11-11T07:00:00Z'));
    const next = (await agent.get('/api/reading').expect(200)).body;
    expect(next.today).toMatchObject({ state: 'new', chapter: { slug: 'momotaro-2', state: 'available' } });
    expect(next.streak).toBe(1);
    const r2 = (await agent.post('/api/reading/chapters/momotaro-2/complete').send({ answers: [9, 9] }).expect(201)).body;
    expect(r2).toMatchObject({ correct: 0, firstTime: true, coinsGained: 5, streak: 2 });

    const exp = (await agent.get('/api/me/export').expect(200)).body;
    expect(JSON.stringify(exp)).toContain('momotaro-2');
  });
});
