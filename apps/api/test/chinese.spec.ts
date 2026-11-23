import request from 'supertest';
import { readFileSync } from 'fs';
import { resolve } from 'path';
import { Ctx, completeFirstLesson, correctAnswer, createTestApp, resetUsers } from './helpers';

/** Chinois (HSK 2.0) : une quatrième langue, avec son parcours, ses hanzi, ses expressions, ses fables et son examen. */
const stories = JSON.parse(readFileSync(resolve(__dirname, '../../../content/reading/stories.json'), 'utf8'));
const bank = JSON.parse(readFileSync(resolve(__dirname, '../../../content/exams/hsk1.json'), 'utf8'));

async function signUpChinese(ctx: Ctx, selfLevel = 'beginner') {
  const agent = request.agent(ctx.app.getHttpServer());
  await agent.post('/api/auth/register').send({ email: `zh${Date.now()}${Math.random()}@test.local`, password: 'motdepasse123', displayName: 'Li' }).expect(201);
  const me = (await agent.put('/api/me/onboarding').send({ selfLevel, targetLevel: 'HSK1', studyLanguage: 'zh', minutesPerDay: 20, difficultAreas: [], reminderMode: 'normal' }).expect(200)).body;
  return { agent, me };
}

describe('Chinois : préparer le HSK', () => {
  let ctx: Ctx;
  beforeAll(async () => {
    ctx = await createTestApp();
    await resetUsers(ctx.prisma);
  });
  afterAll(() => ctx.app.close());

  it('onboarding en chinois : parcours HSK 1, gardiens des Royaumes, niveaux chinois seulement', async () => {
    const { agent, me } = await signUpChinese(ctx);
    expect(me.preferences).toMatchObject({ studyLanguage: 'zh', targetLevel: 'HSK1' });
    const path = (await agent.get('/api/path/HSK1').expect(200)).body;
    expect(path.level).toMatchObject({ code: 'HSK1', region: 'Plaine du Fleuve Jaune' });
    expect(path.levels.map((l: any) => l.code)).toEqual(['HSK1', 'HSK2', 'HSK3', 'HSK4', 'HSK5']);
    expect(path.worlds).toHaveLength(9);
    expect(path.worlds.slice(0, 8).map((w: any) => w.boss.glyph)).toEqual(['年', '饕', '尾', '夔', '貔', '毕', '柳', '烛']);
    expect(path.worlds.at(-1)).toMatchObject({ slug: 'hsk1-final', exam: { slug: 'hsk1-official' } });
    expect(path.worlds[0].chapters[0].lessons[0]).toMatchObject({ slug: 'zh-tones', status: 'available' });
  });

  it('qui connaît déjà les bases commence au deuxième royaume', async () => {
    const { agent } = await signUpChinese(ctx, 'basics');
    const dash = (await agent.get('/api/dashboard').expect(200)).body;
    expect(dash.nextLesson.slug).toBe('zh-hz-time');
  });

  it('hanzi lus en pinyin, expressions, fables, jeux et atelier en chinois', async () => {
    const { agent } = await signUpChinese(ctx);
    const chars = (await agent.get('/api/characters').expect(200)).body;
    expect(chars.sections.map((s: any) => s.slug)).toEqual(['hanzi-hsk1', 'hanzi-hsk2', 'hanzi-hsk3', 'hanzi-hsk4', 'hanzi-hsk5']);
    const ren = chars.sections[0].groups.flatMap((g: any) => g.items).find((c: any) => c.front === '人');
    expect(ren).toMatchObject({ kind: 'kanji', reading: 'rén', kanji: { onyomi: [], kunyomi: [], strokes: 2 } });

    const expr = (await agent.get('/api/expressions').expect(200)).body;
    expect(expr.themes.map((t: any) => t.slug)).toEqual(['zh-politesse', 'zh-rencontres', 'zh-comprendre', 'zh-restaurant', 'zh-marche', 'zh-chengyu']);
    expect(expr.themes[0].expressions[0]).toMatchObject({ front: '你好', reading: 'nǐ hǎo' });

    const reading = (await agent.get('/api/reading').expect(200)).body;
    expect(reading.stories.map((x: any) => x.slug)).toEqual(['shou-zhu-dai-tu', 'hua-she-tian-zu', 'zi-xiang-mao-dun', 'sunzi-lian-bing', 'hu-jia-hu-wei', 'sai-weng-shi-ma', 'meng-mu-san-qian', 'ya-miao-zhu-zhang', 'zhuang-zhou-meng-die', 'yi-zi-qian-jin', 'zhi-lu-wei-ma', 'wan-bi-gui-zhao', 'jing-wei-tian-hai', 'yu-gong-yi-shan', 'yu-bang-xiang-zheng']);
    await agent.get('/api/reading/chapters/momotaro-1').expect(404);
    const ch = stories.stories.find((x: any) => x.slug === 'shou-zhu-dai-tu').chapters[0];
    // Pinyin au-dessus de chaque mot ({汉字|pinyin}) ; le texte prononcé ne garde que les caractères
    expect(ch.paragraphs[0][0].jp).toContain('{农民|nóngmín}');
    expect(ch.paragraphs[0][0].kana).toBe('从前，宋国有一个农民。');
    const r = (await agent.post('/api/reading/chapters/shou-zhu-dai-tu-1/complete').send({ answers: ch.questions.map((q: any) => q.answer) }).expect(201)).body;
    expect(r).toMatchObject({ firstTime: true, correct: ch.questions.length, next: { slug: 'shou-zhu-dai-tu-2' } });

    const games = (await agent.get('/api/games').expect(200)).body.games;
    expect(games.map((g: any) => g.id)).toEqual(['hanzi-rush', 'speed', 'listening']);
  });

  it('une leçon de chinois : questions en chinois, pinyin en lecture, aucune question au format JLPT', async () => {
    const { agent } = await signUpChinese(ctx);
    const { start } = await completeFirstLesson(ctx, agent, 'zh-tones');
    expect(start.questions.some((q: any) => q.display?.jp === '八' || q.choices?.includes('八'))).toBe(true);
    expect(start.questions.every((q: any) => !String(q.type).startsWith('jlpt_'))).toBe(true);
    const userId = (await agent.get('/api/me').expect(200)).body.id;
    expect(await ctx.prisma.reviewCard.count({ where: { userId, item: { levelCode: 'HSK1' } } })).toBeGreaterThanOrEqual(8);
    expect(await ctx.prisma.reviewCard.count({ where: { userId, item: { levelCode: { not: 'HSK1' } } } })).toBe(0);
  });

  it('examen blanc HSK 1 : 20 questions d’écoute et 20 de lecture, notées sur 200, réussite à 120', async () => {
    const { agent } = await signUpChinese(ctx);
    const exam = (await agent.post('/api/exams/hsk1-official/start').expect(201)).body;
    expect(exam.questions).toHaveLength(40);
    expect(exam.questions.filter((q: any) => q.type === 'listening_choice')).toHaveLength(20);
    expect(new Set(exam.questions.map((q: any) => q.display?.part))).toEqual(new Set(bank.parts.map((p: any) => p.jpTitle)));
    const answers: Record<string, unknown> = {};
    for (const q of exam.questions) answers[q.id] = await correctAnswer(ctx.prisma, q.id);
    const result = (await agent.post('/api/exams/hsk1-official/submit').send({ sessionId: exam.sessionId, answers }).expect(200)).body;
    expect(result).toMatchObject({ passed: true, scaled: { listening: 100, language: 100, total: 200, max: { system: 'hsk', total: 200, passTotal: 120 } } });

    const empty = (await agent.post('/api/exams/hsk1-official/start').expect(201)).body;
    const zero = (await agent.post('/api/exams/hsk1-official/submit').send({ sessionId: empty.sessionId, answers: {} }).expect(200)).body;
    expect(zero).toMatchObject({ passed: false, scaled: { total: 0 } });
    const path = (await agent.get('/api/path/HSK1').expect(200)).body;
    expect(path.worlds.at(-1)).toMatchObject({ exam: { slug: 'hsk1-official' } });
  });

  it('HSK 2 : l’art de la guerre au royaume de Wu, examen de 35 + 25 questions en 55 minutes', async () => {
    const { agent } = await signUpChinese(ctx);
    await agent.put('/api/me/preferences').send({ targetLevel: 'HSK2' }).expect(200);
    const path = (await agent.get('/api/path/HSK2').expect(200)).body;
    expect(path.level).toMatchObject({ code: 'HSK2', region: 'Rives du Yangzi' });
    expect(path.worlds.slice(0, 8).map((w: any) => w.boss.glyph)).toEqual(['刑', '婴', '穷', '鲲', '混', '泽', '魃', '蚩']);
    expect(path.worlds.at(-1)).toMatchObject({ slug: 'hsk2-final', exam: { slug: 'hsk2-official' } });
    const exam = (await agent.post('/api/exams/hsk2-official/start').expect(201)).body;
    expect(exam.questions).toHaveLength(60);
    expect(exam.exam.durationMin).toBe(55);
    expect(exam.questions.filter((q: any) => q.type === 'listening_choice')).toHaveLength(35);
    const answers: Record<string, unknown> = {};
    for (const q of exam.questions) answers[q.id] = await correctAnswer(ctx.prisma, q.id);
    const result = (await agent.post('/api/exams/hsk2-official/submit').send({ sessionId: exam.sessionId, answers }).expect(200)).body;
    expect(result).toMatchObject({ passed: true, scaled: { total: 200, max: { system: 'hsk', passTotal: 120 } } });
  });

  it('HSK 3 : les Cent Écoles au royaume de Qi, examen de 40 + 30 + 10 questions en 90 minutes, sur 300', async () => {
    const { agent } = await signUpChinese(ctx);
    await agent.put('/api/me/preferences').send({ targetLevel: 'HSK3' }).expect(200);
    const path = (await agent.get('/api/path/HSK3').expect(200)).body;
    expect(path.level).toMatchObject({ code: 'HSK3', region: 'Côtes de Qi' });
    expect(path.worlds.slice(0, 8).map((w: any) => w.boss.glyph)).toEqual(['梼', '精', '狰', '夸', '獬', '犼', '应', '共']);
    expect(path.worlds[0].chapters[0].lessons.map((l: any) => l.slug)).toEqual(['zh-hz-ba', 'zh-ba', 'zh-building']);
    expect(path.worlds.at(-1)).toMatchObject({ slug: 'hsk3-final', exam: { slug: 'hsk3-official' } });
    const exam = (await agent.post('/api/exams/hsk3-official/start').expect(201)).body;
    expect(exam.questions).toHaveLength(80);
    expect(exam.exam.durationMin).toBe(90);
    expect(exam.questions.filter((q: any) => q.type === 'listening_choice')).toHaveLength(40);
    const answers: Record<string, unknown> = {};
    for (const q of exam.questions) answers[q.id] = await correctAnswer(ctx.prisma, q.id);
    const result = (await agent.post('/api/exams/hsk3-official/submit').send({ sessionId: exam.sessionId, answers }).expect(200)).body;
    expect(result).toMatchObject({ passed: true, scaled: { total: 300, listening: 100, language: 100, writing: 100, max: { system: 'hsk', passTotal: 180 } } });
    // Contes du HSK 3 : le pinyin ne reste qu'au-dessus des mots nouveaux
    const reading = (await agent.get('/api/reading').expect(200)).body;
    const mengmu = reading.stories.find((x: any) => x.slug === 'meng-mu-san-qian');
    expect(mengmu.level).toBe('HSK3');
    const ch = (await agent.get('/api/reading/chapters/meng-mu-san-qian-1').expect(200)).body;
    expect(ch.chapter.paragraphs[0][1].jp).toBe('他和妈妈住在一个{墓地|mùdì}旁边。');
  });

  it('HSK 4 : l’empire de Qin, examen de 45 + 40 + 15 questions en 100 minutes, sur 300', async () => {
    const { agent } = await signUpChinese(ctx);
    await agent.put('/api/me/preferences').send({ targetLevel: 'HSK4' }).expect(200);
    const path = (await agent.get('/api/path/HSK4').expect(200)).body;
    expect(path.level).toMatchObject({ code: 'HSK4', region: 'Plateau de Qin' });
    expect(path.worlds.slice(0, 8).map((w: any) => w.boss.glyph)).toEqual(['蜚', '朱', '犀', '肥', '旋', '驺', '化', '獙']);
    expect(path.worlds.at(-1)).toMatchObject({ slug: 'hsk4-final', exam: { slug: 'hsk4-official' } });
    const exam = (await agent.post('/api/exams/hsk4-official/start').expect(201)).body;
    expect(exam.questions).toHaveLength(100);
    expect(exam.exam.durationMin).toBe(100);
    expect(exam.questions.filter((q: any) => q.type === 'listening_choice')).toHaveLength(45);
    const answers: Record<string, unknown> = {};
    for (const q of exam.questions) answers[q.id] = await correctAnswer(ctx.prisma, q.id);
    const result = (await agent.post('/api/exams/hsk4-official/submit').send({ sessionId: exam.sessionId, answers }).expect(200)).body;
    expect(result).toMatchObject({ passed: true, scaled: { total: 300, writing: 100, max: { system: 'hsk', passTotal: 180 } } });
    // Contes du HSK 4 : pinyin seulement au-dessus des mots qui dépassent le HSK 3
    const ch = (await agent.get('/api/reading/chapters/zhi-lu-wei-ma-2').expect(200)).body;
    expect(ch.chapter.paragraphs[0][1].jp).toBe('有的{大臣|dàchén}害怕{赵高|Zhào Gāo}，不说话；');
  });

  it('HSK 5 : les mers de l’Est, examen de 45 + 45 + 10 questions en 120 minutes, sur 300', async () => {
    const { agent } = await signUpChinese(ctx);
    await agent.put('/api/me/preferences').send({ targetLevel: 'HSK5' }).expect(200);
    const path = (await agent.get('/api/path/HSK5').expect(200)).body;
    expect(path.level).toMatchObject({ code: 'HSK5', region: 'Mers de l’Est' });
    expect(path.worlds.slice(0, 8).map((w: any) => w.boss.glyph)).toEqual(['禺', '蜃', '鲛', '鳌', '蛟', '何', '鱬', '冉']);
    expect(path.worlds.at(-1)).toMatchObject({ slug: 'hsk5-final', exam: { slug: 'hsk5-official' } });
    const exam = (await agent.post('/api/exams/hsk5-official/start').expect(201)).body;
    expect(exam.questions).toHaveLength(100);
    expect(exam.exam.durationMin).toBe(120);
    expect(exam.questions.filter((q: any) => q.type === 'listening_choice')).toHaveLength(45);
    const answers: Record<string, unknown> = {};
    for (const q of exam.questions) answers[q.id] = await correctAnswer(ctx.prisma, q.id);
    const result = (await agent.post('/api/exams/hsk5-official/submit').send({ sessionId: exam.sessionId, answers }).expect(200)).body;
    expect(result).toMatchObject({ passed: true, scaled: { total: 300, writing: 100, max: { system: 'hsk', passTotal: 180 } } });
    // Contes du HSK 5 : pinyin seulement au-dessus des mots qui dépassent le HSK 4
    const ch = (await agent.get('/api/reading/chapters/yu-gong-yi-shan-1').expect(200)).body;
    expect(ch.chapter.paragraphs[0][2].jp).toBe('每次出门，都要{绕|rào}很远的路，非常不方便。');
  });

  it('succès propres au chinois, cachés aux autres langues', async () => {
    const { agent } = await signUpChinese(ctx);
    const slugs = (await agent.get('/api/achievements').expect(200)).body.achievements.map((a: any) => a.slug);
    expect(slugs).toEqual(expect.arrayContaining(['zh-bosses-8', 'hsk-passed', 'zh-tales-10']));
    expect(slugs).not.toContain('hangul-10');
    expect(slugs).not.toContain('toeic-passed');
  });
});
