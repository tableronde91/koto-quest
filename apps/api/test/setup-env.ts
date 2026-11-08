process.env.NODE_ENV = 'test';
process.env.DATABASE_URL = process.env.TEST_DATABASE_URL ?? 'postgresql://koto:koto@localhost:5432/koto_test?schema=public';
process.env.SCHEDULER_ENABLED = 'false';
process.env.AUTH_RATE_LIMIT = '1000';
process.env.API_RATE_LIMIT = '100000';
process.env.VAPID_PUBLIC_KEY = '';
process.env.VAPID_PRIVATE_KEY = '';
