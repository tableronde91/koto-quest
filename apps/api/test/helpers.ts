import { INestApplication } from '@nestjs/common';
import { Test } from '@nestjs/testing';
import request from 'supertest';
import { AppModule } from '../src/app.module';
import { configureApp } from '../src/bootstrap';
import { PrismaService } from '../src/common/prisma.service';
import { ClockService } from '../src/common/clock.service';
import { PushPayload, PushResult, PushService } from '../src/notifications/push.service';
import { NotificationsService } from '../src/notifications/notifications.service';
import { MailService } from '../src/auth/mail.service';
import { seed } from '../prisma/seed';

/** Faux service push : enregistre les envois au lieu de contacter un navigateur. */
export class FakePush {
  enabled = true;
  sent: { endpoint: string; payload: PushPayload }[] = [];
  nextResult: PushResult = 'ok';
  async send(sub: { endpoint: string }, payload: PushPayload): Promise<PushResult> {
    this.sent.push({ endpoint: sub.endpoint, payload });
    return this.nextResult;
  }
}

export interface Ctx {
  app: INestApplication;
  prisma: PrismaService;
  clock: ClockService;
  push: FakePush;
  mail: MailService;
  notifications: NotificationsService;
}

export type Agent = ReturnType<typeof request.agent>;

export async function createTestApp(): Promise<Ctx> {
  const push = new FakePush();
  const mod = await Test.createTestingModule({ imports: [AppModule] }).overrideProvider(PushService).useValue(push).compile();
  const app = mod.createNestApplication();
  configureApp(app);
  await app.init();
  const prisma = app.get(PrismaService);
  await seed(prisma);
  return { app, prisma, clock: app.get(ClockService), push, mail: app.get(MailService), notifications: app.get(NotificationsService) };
}

export async function resetUsers(prisma: PrismaService) {
  await prisma.user.deleteMany({});
}

let counter = 0;
/** Crée un compte et renvoie un agent HTTP qui conserve le cookie de session. */
export async function signUp(app: INestApplication, opts: { onboard?: boolean; selfLevel?: string } = {}) {
  const agent = request.agent(app.getHttpServer());
  const email = `user${Date.now()}_${counter++}@test.local`;
  await agent.post('/api/auth/register').set('X-Timezone', 'Europe/Paris').send({ email, password: 'motdepasse123', displayName: 'Testeur' }).expect(201);
  if (opts.onboard !== false) {
    await agent
      .put('/api/me/onboarding')
      .send({ selfLevel: opts.selfLevel ?? 'beginner', targetLevel: 'N5', minutesPerDay: 20, difficultAreas: ['kanji'], reminderMode: 'normal' })
      .expect(200);
  }
  return { agent, email };
}

/** Lit la bonne réponse en base (réservé aux tests : le client ne la reçoit jamais). */
export async function correctAnswer(prisma: PrismaService, questionId: string) {
  const q = await prisma.issuedQuestion.findUniqueOrThrow({ where: { id: questionId } });
  return q.answer as string | string[];
}

export function wrongAnswer(q: { choices?: string[] }, correct: string | string[]) {
  if (Array.isArray(correct)) return [...correct].reverse();
  return q.choices!.find((c) => c !== correct)!;
}

/** Positionne l'horloge du serveur sur un instant précis. */
export function setNow(clock: ClockService, date: Date) {
  clock.reset();
  clock.advance(date.getTime() - Date.now());
}

export async function completeFirstLesson(ctx: Ctx, agent: Agent, slug = 'n5-hira-a', wrongOn: number[] = []) {
  const start = await agent.post(`/api/lessons/${slug}/start`).expect(201);
  for (const [i, q] of start.body.questions.entries()) {
    const ans = await correctAnswer(ctx.prisma, q.id);
    await agent
      .post(`/api/questions/${q.id}/answer`)
      .send({ answer: wrongOn.includes(i) ? wrongAnswer(q, ans) : ans, responseMs: 5000 })
      .expect(200);
  }
  const done = await agent.post(`/api/lessons/${slug}/complete`).send({ sessionId: start.body.sessionId }).expect(200);
  return { start: start.body, done: done.body };
}
