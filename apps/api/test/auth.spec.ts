import request from 'supertest';
import { Ctx, createTestApp, resetUsers, signUp } from './helpers';

describe('Authentification et sessions', () => {
  let ctx: Ctx;
  beforeAll(async () => {
    ctx = await createTestApp();
    await resetUsers(ctx.prisma);
  });
  afterEach(() => ctx.clock.reset());
  afterAll(() => ctx.app.close());

  it('inscrit un utilisateur avec un cookie httpOnly et le reconnaît', async () => {
    const agent = request.agent(ctx.app.getHttpServer());
    const res = await agent.post('/api/auth/register').send({ email: 'Alice@Test.local ', password: 'secret1234', displayName: 'Alice' }).expect(201);
    const cookie = String(res.headers['set-cookie']);
    expect(cookie).toMatch(/koto_session=/);
    expect(cookie).toMatch(/HttpOnly/i);
    expect(cookie).toMatch(/SameSite=Lax/i);
    const me = await agent.get('/api/me').expect(200);
    expect(me.body).toMatchObject({ email: 'alice@test.local', displayName: 'Alice', onboarded: false });
    expect(me.body.passwordHash).toBeUndefined();
  });

  it('refuse un e-mail déjà utilisé, des données invalides et des champs inattendus', async () => {
    const http = request(ctx.app.getHttpServer());
    await http.post('/api/auth/register').send({ email: 'alice@test.local', password: 'secret1234', displayName: 'A' }).expect(409);
    const bad = await http.post('/api/auth/register').send({ email: 'pas-un-email', password: 'court', displayName: '' }).expect(400);
    expect(JSON.stringify(bad.body.message)).toMatch(/e-mail invalide/);
    await http.post('/api/auth/register').send({ email: 'x@test.local', password: 'secret1234', displayName: 'X', isAdmin: true }).expect(400);
  });

  it('connecte avec le bon mot de passe uniquement', async () => {
    const http = request(ctx.app.getHttpServer());
    await http.post('/api/auth/login').send({ email: 'alice@test.local', password: 'mauvais!!' }).expect(401);
    await http.post('/api/auth/login').send({ email: 'inconnu@test.local', password: 'mauvais!!' }).expect(401);
    await http.post('/api/auth/login').send({ email: 'alice@test.local', password: 'secret1234' }).expect(200);
  });

  it('protège les routes et révoque la session à la déconnexion', async () => {
    await request(ctx.app.getHttpServer()).get('/api/dashboard').expect(401);
    const { agent } = await signUp(ctx.app);
    await agent.get('/api/dashboard').expect(200);
    await agent.post('/api/auth/logout').expect(204);
    await agent.get('/api/dashboard').expect(401);
  });

  it('expire les sessions après leur durée de vie', async () => {
    const { agent } = await signUp(ctx.app);
    ctx.clock.advance(31 * 86_400_000);
    await agent.get('/api/me').expect(401);
  });

  it('réinitialise le mot de passe via un lien à usage unique et révoque les sessions', async () => {
    const { agent, email } = await signUp(ctx.app);
    const http = request(ctx.app.getHttpServer());
    const r = await http.post('/api/auth/forgot-password').send({ email }).expect(200);
    // Même réponse pour une adresse inconnue : pas d'énumération des comptes.
    const r2 = await http.post('/api/auth/forgot-password').send({ email: 'nobody@test.local' }).expect(200);
    expect(r2.body).toEqual(r.body);
    const mail = ctx.mail.outbox.filter((m) => m.to === email).pop()!;
    const token = /token=([\w-]+)/.exec(mail.body)![1];
    await http.post('/api/auth/reset-password').send({ token, password: 'nouveau-mdp-42' }).expect(200);
    await http.post('/api/auth/reset-password').send({ token, password: 'encore-un-42' }).expect(400);
    await agent.get('/api/me').expect(401);
    await http.post('/api/auth/login').send({ email, password: 'nouveau-mdp-42' }).expect(200);
  });

  it('enregistre l’onboarding, le rythme de rappels choisi et le fuseau horaire', async () => {
    const { agent } = await signUp(ctx.app, { onboard: false });
    const me = await agent
      .put('/api/me/onboarding')
      .send({ selfLevel: 'kana', targetLevel: 'N5', examDate: '2027-07-05', minutesPerDay: 45, difficultAreas: ['kanji', 'listening'], reminderMode: 'intense', timezone: 'Asia/Tokyo' })
      .expect(200);
    expect(me.body).toMatchObject({ onboarded: true, preferences: { selfLevel: 'kana', minutesPerDay: 45, timezone: 'Asia/Tokyo', examDate: '2027-07-05' } });
    const notif = await agent.get('/api/notifications/preferences').expect(200);
    expect(notif.body).toMatchObject({ mode: 'intense', consent: false, enabled: false });
    await agent.put('/api/me/preferences').send({ timezone: 'Mars/Olympus' }).expect(400);
  });
});

describe('Session de l’application mobile (jeton Bearer)', () => {
  let ctx: Ctx;
  beforeAll(async () => {
    ctx = await createTestApp();
  });
  afterAll(() => ctx.app.close());

  it('renvoie un jeton (sans cookie) au client mobile, accepté en Authorization Bearer, révoqué à la déconnexion', async () => {
    const http = request(ctx.app.getHttpServer());
    const email = `mobile${Date.now()}@test.local`;
    await http.post('/api/auth/register').send({ email, password: 'motdepasse123', displayName: 'Mobile' }).expect(201);
    const login = await http.post('/api/auth/login').set('X-Koto-Client', 'mobile').send({ email, password: 'motdepasse123' }).expect(200);
    expect(login.headers['set-cookie']).toBeUndefined();
    expect(typeof login.body.token).toBe('string');
    const me = await http.get('/api/me').set('Authorization', `Bearer ${login.body.token}`).expect(200);
    expect(me.body.email).toBe(email);
    await http.get('/api/me').set('Authorization', 'Bearer faux-jeton').expect(401);
    await http.post('/api/auth/logout').set('Authorization', `Bearer ${login.body.token}`).expect(204);
    await http.get('/api/me').set('Authorization', `Bearer ${login.body.token}`).expect(401);
  });

  it('le navigateur ne reçoit jamais le jeton dans la réponse', async () => {
    const http = request(ctx.app.getHttpServer());
    const email = `web${Date.now()}@test.local`;
    const reg = await http.post('/api/auth/register').send({ email, password: 'motdepasse123', displayName: 'Web' }).expect(201);
    expect(reg.body.token).toBeUndefined();
    expect(reg.headers['set-cookie']).toBeDefined();
  });
});
