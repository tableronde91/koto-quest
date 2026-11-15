import { Ctx, createTestApp, resetUsers, signUp } from './helpers';
import { RetentionService } from '../src/common/retention.service';

describe('Durées de conservation', () => {
  let ctx: Ctx;
  beforeAll(async () => {
    ctx = await createTestApp();
    await resetUsers(ctx.prisma);
  });
  afterAll(() => ctx.app.close());
  afterEach(() => ctx.clock.reset());

  it('la visite est enregistrée, un compte inactif depuis 3 ans est supprimé avec ses données', async () => {
    const active = await signUp(ctx.app);
    const idle = await signUp(ctx.app);
    await active.agent.get('/api/me').expect(200);
    await idle.agent.get('/api/me').expect(200);
    const seen = await ctx.prisma.user.findUniqueOrThrow({ where: { email: idle.email } });
    expect(seen.lastSeenAt).not.toBeNull();

    // 3 ans et 1 jour plus tard, seul le premier compte revient
    ctx.clock.advance((3 * 365 + 1) * 86_400_000);
    await active.agent.post('/api/auth/login').send({ email: active.email, password: 'motdepasse123' }).expect(200);
    await active.agent.get('/api/me').expect(200);
    const res = await ctx.app.get(RetentionService).purge();
    expect(res.users).toBe(1);
    expect(await ctx.prisma.user.findUnique({ where: { email: idle.email } })).toBeNull();
    expect(await ctx.prisma.user.findUnique({ where: { email: active.email } })).not.toBeNull();
  });
});
