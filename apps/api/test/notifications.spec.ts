import { DEFAULT_REMINDER_PREFS, localParts, reminderSlots } from '@koto/learning-engine';
import { Ctx, completeFirstLesson, correctAnswer, createTestApp, resetUsers, setNow, signUp } from './helpers';

const HOUR = 3600_000;
const SUB = { endpoint: 'https://push.example.test/abc', keys: { p256dh: 'BPkey', auth: 'authkey' } };

/** Un instant juste après un créneau du mode « normal », au moins 5 h après maintenant (cartes dues). */
function nextSlotInstant(): Date {
  const slots = reminderSlots({ ...DEFAULT_REMINDER_PREFS, mode: 'normal' });
  let t = Math.ceil((Date.now() + 5 * HOUR) / 60_000) * 60_000;
  for (let i = 0; i < 48 * 60; i++, t += 60_000) {
    const { minutes } = localParts(new Date(t), 'Europe/Paris');
    if (slots.includes(minutes - 1)) return new Date(t);
  }
  throw new Error('aucun créneau');
}

describe('Rappels et mini-défis', () => {
  let ctx: Ctx;
  beforeAll(async () => {
    ctx = await createTestApp();
  });
  beforeEach(async () => {
    await resetUsers(ctx.prisma);
    ctx.push.sent = [];
    ctx.push.nextResult = 'ok';
    ctx.clock.reset();
  });
  afterAll(() => ctx.app.close());

  it('n’envoie rien sans consentement explicite, même avec des révisions dues', async () => {
    const { agent } = await signUp(ctx.app);
    await completeFirstLesson(ctx, agent);
    await agent.put('/api/notifications/preferences').send({ enabled: true }).expect(400);
    await agent.post('/api/notifications/push-subscription').send(SUB).expect(400);
    setNow(ctx.clock, nextSlotInstant());
    expect((await ctx.notifications.runScheduler()).sent).toBe(0);
    expect(await ctx.prisma.notification.count()).toBe(0);
    expect(ctx.push.sent).toHaveLength(0);
  });

  it('push refusé par le navigateur : le défi arrive quand même en popup in-app et mène au mini-quiz', async () => {
    const { agent } = await signUp(ctx.app);
    await completeFirstLesson(ctx, agent);
    await agent.put('/api/notifications/preferences').send({ consent: true, enabled: true }).expect(200);
    setNow(ctx.clock, nextSlotInstant());
    expect((await ctx.notifications.runScheduler()).sent).toBe(1);
    expect(ctx.push.sent).toHaveLength(0); // aucun abonnement push
    const inbox = await agent.get('/api/notifications/inbox').expect(200);
    expect(inbox.body).toHaveLength(1);
    expect(inbox.body[0].questionId).toBeTruthy();

    // Un seul rappel par créneau
    expect((await ctx.notifications.runScheduler()).sent).toBe(0);

    await agent.post(`/api/notifications/${inbox.body[0].id}/open`).expect(200);
    const qid = inbox.body[0].questionId;
    const q = await agent.get(`/api/questions/${qid}`).expect(200);
    expect(q.body.question.phase).toBe('quiz');
    expect(q.body.question.answer).toBeUndefined();
    const res = await agent.post(`/api/questions/${qid}/answer`).send({ answer: await correctAnswer(ctx.prisma, qid), responseMs: 3000 }).expect(200);
    expect(res.body).toMatchObject({ correct: true, xpGained: 8 });
    // La mémorisation est mise à jour : prochaine révision dans au moins un jour
    expect(new Date(res.body.nextReviewAt).getTime()).toBeGreaterThan(ctx.clock.now().getTime() + 20 * HOUR);
    expect((await agent.get('/api/notifications/inbox')).body).toHaveLength(0);
  });

  it('envoie un push quand l’utilisateur est abonné, et nettoie les abonnements expirés', async () => {
    const { agent } = await signUp(ctx.app);
    await completeFirstLesson(ctx, agent);
    await agent.put('/api/notifications/preferences').send({ consent: true, enabled: true }).expect(200);
    await agent.post('/api/notifications/push-subscription').send(SUB).expect(201);
    setNow(ctx.clock, nextSlotInstant());
    await ctx.notifications.runScheduler();
    expect(ctx.push.sent).toHaveLength(1);
    expect(ctx.push.sent[0].payload.url).toMatch(/^\/quiz\/[0-9a-f-]{36}\?n=/);

    ctx.push.nextResult = 'gone';
    await agent.post('/api/notifications/test').expect(201);
    expect(await ctx.prisma.pushSubscription.count()).toBe(0);
  });

  it('ne sollicite pas l’utilisateur quand il n’y a rien à réviser, ni pendant une pause', async () => {
    const { agent } = await signUp(ctx.app);
    await agent.put('/api/notifications/preferences').send({ consent: true, enabled: true }).expect(200);
    setNow(ctx.clock, nextSlotInstant());
    expect((await ctx.notifications.runScheduler()).sent).toBe(0);
    await agent.post('/api/notifications/test').expect(409);

    ctx.clock.reset();
    await completeFirstLesson(ctx, agent);
    const slot = nextSlotInstant();
    await agent.put('/api/notifications/preferences').send({ pausedUntil: new Date(slot.getTime() + 24 * HOUR).toISOString() }).expect(200);
    setNow(ctx.clock, slot);
    expect((await ctx.notifications.runScheduler()).sent).toBe(0);
  });

  it('retirer son consentement coupe les rappels et supprime les abonnements', async () => {
    const { agent } = await signUp(ctx.app);
    await agent.put('/api/notifications/preferences').send({ consent: true, enabled: true, mode: 'calm' }).expect(200);
    await agent.post('/api/notifications/push-subscription').send(SUB).expect(201);
    const prefs = await agent.put('/api/notifications/preferences').send({ consent: false }).expect(200);
    expect(prefs.body).toMatchObject({ consent: false, enabled: false, pushSubscribed: false });
    expect(prefs.body.slots).toHaveLength(2);
  });
});
