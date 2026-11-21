import request from 'supertest';
import { readFileSync } from 'fs';
import { resolve } from 'path';
import { Ctx, completeFirstLesson, correctAnswer, createTestApp, resetUsers, signUp } from './helpers';

/** Coréen (TOPIK) : une deuxième langue, avec son parcours, ses caractères, ses contes et son examen. */
const stories = JSON.parse(readFileSync(resolve(__dirname, '../../../content/reading/stories.json'), 'utf8'));

async function signUpKorean(ctx: Ctx, selfLevel = 'beginner') {
  const agent = request.agent(ctx.app.getHttpServer());
  await agent.post('/api/auth/register').send({ email: `ko${Date.now()}${Math.random()}@test.local`, password: 'motdepasse123', displayName: '민지' }).expect(201);
  const me = (await agent.put('/api/me/onboarding').send({ selfLevel, targetLevel: 'TOPIK1', studyLanguage: 'ko', minutesPerDay: 20, difficultAreas: [], reminderMode: 'normal' }).expect(200)).body;
  return { agent, me };
}

describe('Coréen : apprendre une deuxième langue', () => {
  let ctx: Ctx;
  beforeAll(async () => {
    ctx = await createTestApp();
    await resetUsers(ctx.prisma);
  });
  afterAll(() => ctx.app.close());

  it('onboarding en coréen : parcours TOPIK 1, île du hangeul ouverte, niveaux coréens seulement', async () => {
    const { agent, me } = await signUpKorean(ctx);
    expect(me.preferences).toMatchObject({ studyLanguage: 'ko', targetLevel: 'TOPIK1' });
    const path = (await agent.get('/api/path/TOPIK1').expect(200)).body;
    expect(path.level).toMatchObject({ code: 'TOPIK1', region: 'Péninsule du Matin calme' });
    expect(path.levels.map((l: any) => l.code)).toEqual(['TOPIK1', 'TOPIK2', 'TOPIK3', 'TOPIK4', 'TOPIK5', 'TOPIK6']);
    expect(path.worlds).toHaveLength(9);
    expect(path.worlds.slice(0, 8).every((w: any) => w.boss && !w.comingSoon)).toBe(true);
    expect(path.worlds.at(-1)).toMatchObject({ slug: 'topik1-final', exam: { slug: 'topik1-official' } });
    expect(path.worlds[0].chapters[0].lessons[0]).toMatchObject({ slug: 'ko-vowels-1', status: 'available' });
    const dash = (await agent.get('/api/dashboard').expect(200)).body;
    expect(dash).toMatchObject({ targetLevel: 'TOPIK1', nextLesson: { slug: 'ko-vowels-1' } });
  });

  it('qui lit déjà le hangeul commence à l’île 3 (se présenter)', async () => {
    const { agent } = await signUpKorean(ctx, 'kana');
    const dash = (await agent.get('/api/dashboard').expect(200)).body;
    expect(dash.nextLesson).toMatchObject({ slug: 'ko-intro' });
  });

  it('caractères, expressions et contes suivent la langue étudiée', async () => {
    const { agent } = await signUpKorean(ctx);
    const chars = (await agent.get('/api/characters').expect(200)).body;
    expect(chars.sections.map((s: any) => [s.slug, s.glyph])).toEqual([['hangul-vowels', 'ㅏ'], ['hangul-consonants', 'ㄱ'], ['hangul-syllables', '가']]);
    expect(chars.sections[0].groups[0].items.map((c: any) => c.front)).toEqual(['ㅏ', 'ㅓ', 'ㅗ', 'ㅜ', 'ㅡ', 'ㅣ']);
    const session = (await agent.post('/api/characters/practice').send({ scope: 'hg-v-base' }).expect(201)).body;
    expect(session.questions.length).toBeGreaterThan(5);

    const expr = (await agent.get('/api/expressions').expect(200)).body;
    expect(expr.themes[0].expressions.map((e: any) => e.front)).toContain('감사합니다');
    // Révision des proverbes : 속담 et 사자성어, avec leur propre entraînement
    expect(expr.themes.map((t: any) => t.slug)).toEqual(expect.arrayContaining(['ko-sokdam', 'ko-sokdam-contes', 'ko-sajaseongeo']));
    expect(expr.themes.find((t: any) => t.slug === 'ko-sajaseongeo').expressions.map((e: any) => e.front)).toContain('작심삼일');
    const prov = (await agent.post('/api/expressions/practice').send({ theme: 'ko-sokdam' }).expect(201)).body;
    expect(prov.questions.length).toBeGreaterThan(5);

    const reading = (await agent.get('/api/reading').expect(200)).body;
    expect(reading.stories.map((s: any) => s.slug)).toEqual(['haenim-dalnim', 'heungbu-nolbu', 'gyeonu-jiknyeo', 'geumdokki-eundokki', 'tokki-jara', 'seonnyeo-namukkun', 'hokburi-yeonggam', 'kongjwi-patjwi', 'chunhyang', 'simcheong', 'hong-gildong', 'bari-gongju', 'dangun-sinhwa']);
    expect(reading.today.chapter).toMatchObject({ slug: 'haenim-dalnim-1', day: 1 });
    // Un conte japonais n'existe pas pour qui étudie le coréen
    await agent.get('/api/reading/chapters/momotaro-1').expect(404);
    const ch = stories.stories.find((s: any) => s.slug === 'haenim-dalnim').chapters[0];
    const r = (await agent.post('/api/reading/chapters/haenim-dalnim-1/complete').send({ answers: ch.questions.map((q: any) => q.answer) }).expect(201)).body;
    expect(r).toMatchObject({ firstTime: true, correct: ch.questions.length, next: { slug: 'haenim-dalnim-2' } });
  });

  it('une leçon de hangeul se joue en coréen, et les révisions ne mélangent pas les langues', async () => {
    const { agent } = await signUpKorean(ctx);
    const { start } = await completeFirstLesson(ctx, agent, 'ko-vowels-1');
    expect(start.questions.some((q: any) => q.display?.jp === 'ㅏ' || q.choices?.includes('ㅏ'))).toBe(true);
    const userId = (await agent.get('/api/me').expect(200)).body.id;
    const korean = await ctx.prisma.reviewCard.count({ where: { userId, item: { levelCode: 'TOPIK1' } } });
    expect(korean).toBeGreaterThanOrEqual(6);

    // Révisions dues : passons quelques jours
    const due = async () => (await agent.get('/api/reviews/summary').expect(200)).body.due;
    await ctx.prisma.reviewCard.updateMany({ where: { userId }, data: { due: new Date(Date.now() - 60_000) } });
    expect(await due()).toBeGreaterThanOrEqual(6);

    // On passe au japonais : les cartes coréennes disparaissent des révisions, le niveau devient N5
    const ja = (await agent.put('/api/me/preferences').send({ studyLanguage: 'ja' }).expect(200)).body;
    expect(ja.preferences).toMatchObject({ studyLanguage: 'ja', targetLevel: 'N5' });
    expect(await due()).toBe(0);
    expect((await agent.get('/api/characters').expect(200)).body.sections[0].slug).toBe('hiragana');
    expect((await agent.get('/api/reading').expect(200)).body.today.chapter.slug).toBe('momotaro-1');
    expect((await agent.post('/api/reviews/session').expect(201)).body.questions).toEqual([]);

    // Choisir un niveau japonais puis revenir au coréen : chaque langue retrouve son niveau
    await agent.put('/api/me/preferences').send({ targetLevel: 'N4' }).expect(200);
    const ko = (await agent.put('/api/me/preferences').send({ studyLanguage: 'ko' }).expect(200)).body;
    expect(ko.preferences).toMatchObject({ studyLanguage: 'ko', targetLevel: 'TOPIK1' });
    expect(await due()).toBeGreaterThanOrEqual(6);
    const back = (await agent.put('/api/me/preferences').send({ studyLanguage: 'ja' }).expect(200)).body;
    expect(back.preferences.targetLevel).toBe('N4');
    // Choisir un niveau d'une langue fait passer à cette langue
    const direct = (await agent.put('/api/me/preferences').send({ targetLevel: 'TOPIK1' }).expect(200)).body;
    expect(direct.preferences.studyLanguage).toBe('ko');
    await agent.put('/api/me/preferences').send({ studyLanguage: 'zh' }).expect(400);
  });

  it('leçon de grammaire : exercices en coréen, distracteurs coréens', async () => {
    const { agent } = await signUpKorean(ctx, 'kana');
    const start = (await agent.post('/api/lessons/ko-intro/start').expect(201)).body;
    const choices = start.questions.flatMap((q: any) => q.choices ?? []);
    expect(choices.length).toBeGreaterThan(10);
    // Aucun choix en japonais dans une leçon de coréen
    expect(choices.filter((c: string) => /[぀-ヿ一-龯]/.test(c))).toEqual([]);
    for (const q of start.questions) {
      const ans = await correctAnswer(ctx.prisma, q.id);
      await agent.post(`/api/questions/${q.id}/answer`).send({ answer: ans, responseMs: 4000 }).expect(200);
    }
    const done = (await agent.post('/api/lessons/ko-intro/complete').send({ sessionId: start.sessionId }).expect(200)).body;
    expect(done).toMatchObject({ perfect: true, nextLessonSlug: 'ko-topic' });
  });

  it('atelier TOPIK : grammaire et écoute seulement, consignes en coréen', async () => {
    const { agent } = await signUpKorean(ctx, 'kana');
    for (const slug of ['ko-intro', 'ko-topic', 'ko-not-noun']) await completeFirstLesson(ctx, agent, slug);
    const drills = (await agent.get('/api/jlpt/drills').expect(200)).body;
    expect(drills.drills.map((d: any) => d.part)).toEqual(['grammar', 'listening']);
    expect(drills.drills[0]).toMatchObject({ jpTitle: '문법' });
    const s = (await agent.post('/api/jlpt/drills/grammar').expect(201)).body;
    expect(s.questions[0].prompt).toBe('(　)에 들어갈 가장 알맞은 것을 고르십시오.');
    await agent.post('/api/jlpt/drills/kanji').expect(404);
  });

  it('examen blanc TOPIK I : 30 questions d’écoute et 40 de lecture, noté sur 200 avec le niveau obtenu', async () => {
    const { agent } = await signUpKorean(ctx);
    const exam = (await agent.post('/api/exams/topik1-official/start').expect(201)).body;
    expect(exam.exam).toMatchObject({ durationMin: 100, sections: [{ id: 'listening', count: 30 }, { id: 'reading', count: 40 }] });
    expect(exam.questions).toHaveLength(70);
    expect(JSON.stringify(exam.questions)).not.toContain('"answer"');
    const answers: Record<string, unknown> = {};
    // Toute la lecture juste, rien à l'écoute : 100/200 → niveau 1
    for (const q of exam.questions) if (q.section === 'reading') answers[q.id] = await correctAnswer(ctx.prisma, q.id);
    const res = (await agent.post('/api/exams/topik1-official/submit').send({ sessionId: exam.sessionId, answers }).expect(200)).body;
    expect(res).toMatchObject({ passed: true, scaled: { language: 100, listening: 0, total: 100, level: 1, max: { system: 'topik', total: 200 } } });
    expect(res.sections.map((s: any) => s.jpTitle)).toEqual(['듣기', '읽기']);
    expect(res.recommendations.join(' ')).toMatch(/듣기/);
    // Entraînement généré à partir des leçons
    const mock = (await agent.post('/api/exams/topik1-mock/start').expect(201)).body;
    expect(mock.questions.length).toBeGreaterThanOrEqual(28);
  });

  it('TOPIK 2 : parcours du conteur et examen validé seulement au niveau 2', async () => {
    const { agent } = await signUpKorean(ctx);
    await agent.put('/api/me/preferences').send({ targetLevel: 'TOPIK2' }).expect(200);
    const path = (await agent.get('/api/path/TOPIK2').expect(200)).body;
    expect(path.level).toMatchObject({ code: 'TOPIK2', region: 'Pays des contes' });
    expect(path.worlds).toHaveLength(9);
    expect(path.worlds.slice(0, 8).every((w: any) => w.boss && !w.comingSoon)).toBe(true);
    expect(path.worlds.at(-1)).toMatchObject({ slug: 'topik2-final', exam: { slug: 'topik2-official' } });
    const exam = (await agent.post('/api/exams/topik2-official/start').expect(201)).body;
    expect(exam.questions).toHaveLength(70);
    // Toute la lecture juste : 100/200, niveau 1 obtenu mais l'examen du niveau 2 n'est pas validé
    const answers: Record<string, unknown> = {};
    for (const q of exam.questions) if (q.section === 'reading') answers[q.id] = await correctAnswer(ctx.prisma, q.id);
    const res = (await agent.post('/api/exams/topik2-official/submit').send({ sessionId: exam.sessionId, answers }).expect(200)).body;
    expect(res).toMatchObject({ passed: false, scaled: { total: 100, level: 1, max: { system: 'topik', passLevel: 2 } } });
    const mock = (await agent.post('/api/exams/topik2-mock/start').expect(201)).body;
    expect(mock.questions.length).toBeGreaterThanOrEqual(28);
  });

  it('TOPIK 3 : saga de l’inspecteur royal et examen au format du TOPIK II noté sur 300', async () => {
    const { agent } = await signUpKorean(ctx);
    await agent.put('/api/me/preferences').send({ targetLevel: 'TOPIK3' }).expect(200);
    const path = (await agent.get('/api/path/TOPIK3').expect(200)).body;
    expect(path.level).toMatchObject({ code: 'TOPIK3', region: 'Royaume de Joseon' });
    expect(path.worlds).toHaveLength(9);
    expect(path.worlds.at(-1)).toMatchObject({ slug: 'topik3-final', exam: { slug: 'topik3-official' } });
    const exam = (await agent.post('/api/exams/topik3-official/start').expect(201)).body;
    expect(exam.exam.sections.map((s: any) => [s.id, s.count])).toEqual([['listening', 25], ['writing', 5], ['reading', 25]]);
    expect(exam.questions).toHaveLength(55);
    // Écriture et lecture parfaites, rien à l'écoute : 200/300 → niveau 5
    const answers: Record<string, unknown> = {};
    for (const q of exam.questions) if (q.section !== 'listening') answers[q.id] = await correctAnswer(ctx.prisma, q.id);
    const res = (await agent.post('/api/exams/topik3-official/submit').send({ sessionId: exam.sessionId, answers }).expect(200)).body;
    expect(res).toMatchObject({ passed: true, scaled: { listening: 0, writing: 100, language: 100, total: 200, level: 5, max: { total: 300, writing: 100, passLevel: 3 } } });
    expect(res.sections.map((s: any) => s.jpTitle)).toEqual(['듣기', '쓰기', '읽기']);
  });

  it('TOPIK 4 : saga de l’historien et examen validé seulement au niveau 4', async () => {
    const { agent } = await signUpKorean(ctx);
    await agent.put('/api/me/preferences').send({ targetLevel: 'TOPIK4' }).expect(200);
    const path = (await agent.get('/api/path/TOPIK4').expect(200)).body;
    expect(path.level).toMatchObject({ code: 'TOPIK4', region: 'Annales de Joseon' });
    expect(path.worlds.at(-1)).toMatchObject({ slug: 'topik4-final', exam: { slug: 'topik4-official' } });
    const exam = (await agent.post('/api/exams/topik4-official/start').expect(201)).body;
    expect(exam.questions).toHaveLength(55);
    // Seule la lecture est juste : 100/300, pas même le niveau 3
    const answers: Record<string, unknown> = {};
    for (const q of exam.questions) if (q.section === 'reading') answers[q.id] = await correctAnswer(ctx.prisma, q.id);
    const res = (await agent.post('/api/exams/topik4-official/submit').send({ sessionId: exam.sessionId, answers }).expect(200)).body;
    expect(res).toMatchObject({ passed: false, scaled: { language: 100, total: 100, level: 0, max: { passLevel: 4 } } });
  });

  it.each([
    [5, 'Terres des mythes'],
    [6, 'Royaume de Gojoseon'],
  ])('TOPIK %i : saga des mythes et examen validé seulement au bon niveau', async (n, region) => {
    const { agent } = await signUpKorean(ctx);
    await agent.put('/api/me/preferences').send({ targetLevel: `TOPIK${n}` }).expect(200);
    const path = (await agent.get(`/api/path/TOPIK${n}`).expect(200)).body;
    expect(path.level).toMatchObject({ code: `TOPIK${n}`, region });
    expect(path.worlds).toHaveLength(9);
    expect(path.worlds.slice(0, 8).every((w: any) => w.boss && !w.comingSoon)).toBe(true);
    expect(path.worlds.at(-1)).toMatchObject({ slug: `topik${n}-final`, exam: { slug: `topik${n}-official` } });
    const exam = (await agent.post(`/api/exams/topik${n}-official/start`).expect(201)).body;
    expect(exam.questions).toHaveLength(55);
    // Écriture et lecture justes : 200/300, niveau 5 — suffisant au TOPIK 5 seulement
    const answers: Record<string, unknown> = {};
    for (const q of exam.questions) if (q.section !== 'listening') answers[q.id] = await correctAnswer(ctx.prisma, q.id);
    const res = (await agent.post(`/api/exams/topik${n}-official/submit`).send({ sessionId: exam.sessionId, answers }).expect(200)).body;
    expect(res).toMatchObject({ passed: n === 5, scaled: { total: 200, level: 5, max: { passLevel: n } } });
  });

  it('mini-jeux : Hangeul Rush à la place de Kanji Rush, sur les lettres déjà apprises', async () => {
    const { agent } = await signUpKorean(ctx);
    let list = (await agent.get('/api/games').expect(200)).body;
    expect(list.games.map((g: any) => g.id)).toEqual(['hangul-rush', 'speed', 'listening']);
    expect(list.games[0]).toMatchObject({ title: 'Hangeul Rush', available: false });
    for (let i = 0; i < 2; i++) {
      const s = (await agent.post('/api/characters/practice').send({ scope: 'hg-v-base' }).expect(201)).body;
      for (const q of s.questions) await agent.post(`/api/questions/${q.id}/answer`).send({ answer: await correctAnswer(ctx.prisma, q.id), responseMs: 3000 }).expect(200);
    }
    list = (await agent.get('/api/games').expect(200)).body;
    expect(list.games[0].seenItems).toBeGreaterThanOrEqual(6);
    expect(list.games[0]).toMatchObject({ id: 'hangul-rush', available: true });
    const game = (await agent.post('/api/games/hangul-rush/start').expect(201)).body;
    expect(game.questions.length).toBe(60);
    expect(game.questions.every((q: any) => ['meaning_choice', 'reverse_choice'].includes(q.type))).toBe(true);
  });

  it('duels : on n’affronte que des joueurs qui étudient la même langue', async () => {
    const a = await signUpKorean(ctx);
    const b = (await signUp(ctx.app)).agent; // japonais
    const c = await signUpKorean(ctx);
    expect((await b.post('/api/duels/queue').expect(200)).body.status).toBe('searching');
    expect((await a.agent.post('/api/duels/queue').expect(200)).body.status).toBe('searching');
    const matched = (await c.agent.post('/api/duels/queue').expect(200)).body;
    expect(matched.status).toBe('matched');
    const state = (await c.agent.get(`/api/duels/${matched.duelId}`).expect(200)).body;
    // Questions du duel en coréen (kana de départ remplacés par le hangeul)
    expect(JSON.stringify(state)).not.toMatch(/[぀-ヿ]/);
    expect((await b.get('/api/duels/queue').expect(200)).body.status).toBe('searching');
    await b.delete('/api/duels/queue');
  });
});
