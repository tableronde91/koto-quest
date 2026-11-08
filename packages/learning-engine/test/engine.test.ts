import { describe, expect, it } from 'vitest';
import {
  AuthoredExercise,
  DEFAULT_REMINDER_PREFS,
  EngineItem,
  ReminderPrefs,
  authoredToQuestion,
  checkAnswer,
  computeStreak,
  createRng,
  dailyQuests,
  decideReminder,
  estimateReadiness,
  generateMatching,
  generateQuestion,
  isInQuietHours,
  levelFromXp,
  localParts,
  newCard,
  orderReviewQueue,
  pickDistractors,
  planDailyLoad,
  questionTypesFor,
  reminderSlots,
  schedule,
  toPublic,
  validateAuthoredExercise,
  fillBlank,
  reshuffleForRetry,
  focusedPool,
} from '../src';

const kana = (id: string, front: string, romaji: string): EngineItem => ({ id, kind: 'kana', front, reading: front, romaji, meaning: romaji });
const vocab = (id: string, front: string, reading: string, meaning: string): EngineItem => ({ id, kind: 'vocabulary', front, reading, meaning });

const POOL: EngineItem[] = [
  vocab('neko', '猫', 'ねこ', 'chat'),
  vocab('inu', '犬', 'いぬ', 'chien'),
  vocab('tori', '鳥', 'とり', 'oiseau'),
  vocab('sakana', '魚', 'さかな', 'poisson'),
  vocab('neko2', 'ネコ', 'ねこ', 'chat'), // même sens : ne doit jamais être un distracteur
  kana('ji', 'じ', 'ji'),
  kana('dji', 'ぢ', 'ji'),
  kana('a', 'あ', 'a'),
  kana('i', 'い', 'i'),
  kana('u', 'う', 'u'),
];

describe('génération d’exercices', () => {
  it('produit le QCM « Que signifie 猫 ? » avec une seule bonne réponse', () => {
    const q = generateQuestion(POOL[0], POOL, 'meaning_choice', createRng(1))!;
    expect(q.prompt).toBe('Que signifie ce mot ?');
    expect(q.display?.jp).toBe('猫');
    expect(q.choices).toHaveLength(4);
    expect(q.choices!.filter((c) => c === 'chat')).toHaveLength(1);
    expect(new Set(q.choices).size).toBe(4);
    expect(checkAnswer(q, 'chat')).toBe(true);
    expect(checkAnswer(q, 'chien')).toBe(false);
  });

  it('n’envoie jamais la réponse dans la version publique', () => {
    const q = generateQuestion(POOL[0], POOL, 'reverse_choice', createRng(2))!;
    const pub = toPublic(q) as Record<string, unknown>;
    expect(pub.answer).toBeUndefined();
    expect(pub.explanation).toBeUndefined();
  });

  it('écarte les distracteurs ambigus (même sens ou même lecture)', () => {
    for (let s = 0; s < 50; s++) {
      expect(pickDistractors(POOL[0], POOL, 'meaning', 3, createRng(s))).not.toContain('chat');
      expect(pickDistractors(POOL[5], POOL, 'meaning', 3, createRng(s))).not.toContain('ji');
    }
  });

  it('ne mélange jamais hiragana et katakana dans les choix', () => {
    const mixed = [...POOL, { id: 'kata-ka', kind: 'kana' as const, front: 'カ', reading: 'カ', romaji: 'ka', meaning: 'ka' }, { id: 'kata-ki', kind: 'kana' as const, front: 'キ', reading: 'キ', romaji: 'ki', meaning: 'ki' }];
    for (let s = 0; s < 30; s++) {
      const q = generateQuestion(POOL[7], mixed, 'reverse_choice', createRng(s))!;
      expect(q.choices!.every((c) => /^[\u3040-\u309f]+$/.test(c))).toBe(true);
    }
  });

  it('centre les distracteurs sur le monde en cours quand il y a assez de notions', () => {
    const world = POOL.filter((i) => i.kind === 'kana').slice(0, 4);
    const extra = { id: 'hira-pyu', kind: 'kana' as const, front: 'ぴゅ', reading: 'ぴゅ', romaji: 'pyu', meaning: 'pyu' };
    const pool = focusedPool(world, [...POOL, extra]);
    expect(pool.some((i) => i.id === 'hira-pyu')).toBe(false);
    expect(pool.some((i) => i.kind === 'vocabulary')).toBe(true); // type absent du monde : complété par le niveau
  });

  it('renvoie null s’il n’y a pas assez de distracteurs', () => {
    expect(generateQuestion(POOL[0], [POOL[0], POOL[1]], 'meaning_choice', createRng(1))).toBeNull();
  });

  it('propose la lecture uniquement pour les mots écrits en kanji', () => {
    expect(questionTypesFor(POOL[0])).toContain('reading_choice');
    expect(questionTypesFor(vocab('x', 'すし', 'すし', 'sushi'))).not.toContain('reading_choice');
  });

  it('génère vrai/faux et l’association de mots', () => {
    const tf = generateQuestion(POOL[0], POOL, 'true_false', createRng(3))!;
    expect(tf.guessable).toBe(true);
    expect(['Vrai', 'Faux']).toContain(tf.answer);
    const m = generateMatching(POOL.slice(0, 5), createRng(4))!;
    expect(m.pairs!.left.length).toBe(m.pairs!.right.length);
    expect(checkAnswer(m, m.answer)).toBe(true);
    expect(checkAnswer(m, [...(m.answer as string[])].reverse())).toBe(false);
  });

  it('est déterministe pour une même graine', () => {
    const a = generateQuestion(POOL[0], POOL, 'meaning_choice', createRng('s'));
    const b = generateQuestion(POOL[0], POOL, 'meaning_choice', createRng('s'));
    expect(a).toEqual(b);
  });

  it('normalise les réponses (pleine chasse, espaces, casse)', () => {
    expect(checkAnswer({ type: 'fill_blank', answer: 'は' }, ' は ')).toBe(true);
    expect(checkAnswer({ type: 'meaning_choice', answer: 'Chat' }, 'chat')).toBe(true);
  });
});

describe('exercices rédigés', () => {
  const particle: AuthoredExercise = {
    type: 'particle_choice',
    prompt: 'Choisis la particule.',
    sentence: 'わたし＿がくせいです。',
    choices: ['は', 'を', 'に'],
    answer: 'は',
    explanation: 'は marque le thème.',
  };

  it('valide la cohérence du contenu', () => {
    expect(validateAuthoredExercise(particle)).toEqual([]);
    expect(validateAuthoredExercise({ ...particle, answer: 'が' })).not.toEqual([]);
    expect(validateAuthoredExercise({ ...particle, choices: ['は', 'は', 'を'] })).not.toEqual([]);
    expect(validateAuthoredExercise({ ...particle, explanation: '' })).not.toEqual([]);
  });

  it('prononce la phrase complète avec le mot choisi, jamais la phrase à trou avant la réponse', () => {
    const q = authoredToQuestion(particle, createRng(1));
    expect(q.display?.jp).toBe('わたし＿がくせいです。');
    expect(q.audio).toBeUndefined();
    expect(fillBlank(q.answerAudio!, 'は')).toBe('わたしはがくせいです。');
    const dialogue = authoredToQuestion(
      { type: 'dialogue_choice', prompt: '?', lines: [{ speaker: 'Ken', jp: 'がくせいですか。' }], choices: ['はい、がくせいです。', 'いいえ。'], answer: 'はい、がくせいです。', explanation: '…' },
      createRng(2),
    );
    expect(fillBlank(dialogue.answerAudio!, 'はい、がくせいです。')).toBe('がくせいですか。　はい、がくせいです。');
    const reading = authoredToQuestion({ type: 'fill_blank', prompt: 'Lis', sentence: 'ねこ', choices: ['neko', 'nako'], answer: 'neko', explanation: '…' }, createRng(3));
    expect(reading.audio).toBeUndefined(); // entendre ねこ donnerait la réponse
    expect(fillBlank(reading.answerAudio!, 'neko')).toBe('ねこ');
  });

  it('remélange une question reprise sans changer la bonne réponse', () => {
    const q = authoredToQuestion({ type: 'sentence_order', prompt: '…', answer: ['わたしは', 'がくせい', 'です'], explanation: '…' }, createRng(4));
    const pub = toPublic(q);
    for (let s = 0; s < 10; s++) {
      const again = reshuffleForRetry(pub, q.answer, createRng(s));
      expect([...again.tokens!].sort()).toEqual([...pub.tokens!].sort());
      expect(again.tokens!.join()).not.toBe((q.answer as string[]).join());
      expect(fillBlank(again.answerAudio!, q.answer)).toBe('わたしはがくせいです');
    }
    const m = generateMatching(POOL.slice(0, 5), createRng(5))!;
    const mr = reshuffleForRetry(toPublic(m), m.answer, createRng(6));
    expect(mr.pairs!.left).toEqual(m.pairs!.left);
    expect([...mr.pairs!.right].sort()).toEqual([...m.pairs!.right].sort());
  });

  it('mélange les segments d’une phrase à reconstruire sans donner l’ordre correct', () => {
    const order: AuthoredExercise = {
      type: 'sentence_order',
      prompt: 'Remets dans l’ordre.',
      answer: ['わたしは', 'がくせい', 'です'],
      explanation: '…',
    };
    for (let s = 0; s < 20; s++) {
      const q = authoredToQuestion(order, createRng(s));
      expect([...q.tokens!].sort()).toEqual([...order.answer].sort());
      expect(q.tokens!.join()).not.toBe((order.answer as string[]).join());
      expect(checkAnswer(q, order.answer)).toBe(true);
    }
  });
});

describe('planification de la charge quotidienne', () => {
  it('répartit le temps entre révisions et nouveautés', () => {
    const p = planDailyLoad({ minutesPerDay: 20, dueCount: 30, newItemsAvailable: 100 });
    expect(p.reviewLimit).toBe(30);
    expect(p.newItemLimit).toBeGreaterThan(0);
    expect(p.catchUpMode).toBe(false);
    expect(p.estimatedMinutes).toBeLessThanOrEqual(20);
  });

  it('en cas de retard, plafonne les révisions et ralentit les nouveautés', () => {
    const normal = planDailyLoad({ minutesPerDay: 15, dueCount: 10, newItemsAvailable: 100 });
    const late = planDailyLoad({ minutesPerDay: 15, dueCount: 900, newItemsAvailable: 100 });
    expect(late.catchUpMode).toBe(true);
    expect(late.reviewLimit).toBeLessThan(900);
    expect(late.reviewLimit * 10).toBeLessThanOrEqual(15 * 60 * 0.7);
    expect(late.newItemLimit).toBeLessThan(normal.newItemLimit);
    expect(late.estimatedMinutes).toBeLessThanOrEqual(15);
  });

  it('ordonne la file : les notions les plus oubliées d’abord', () => {
    const now = new Date('2026-03-01T10:00:00Z');
    const fresh = { id: 'fresh', card: { ...newCard(now), state: 'review' as const, stability: 30, difficulty: 5, lastReview: new Date('2026-02-28T10:00:00Z'), due: new Date('2026-03-01T09:00:00Z'), reps: 5 } };
    const old = { id: 'old', card: { ...fresh.card, lastReview: new Date('2025-12-01T10:00:00Z'), stability: 5 } };
    const notDue = { id: 'later', card: { ...fresh.card, due: new Date('2026-04-01T00:00:00Z') } };
    expect(orderReviewQueue([fresh, notDue, old], now).map((e) => e.id)).toEqual(['old', 'fresh']);
  });
});

describe('rappels intelligents', () => {
  const prefs: ReminderPrefs = { ...DEFAULT_REMINDER_PREFS, enabled: true, consent: true, mode: 'normal', timezone: 'Europe/Paris' };
  // 2026-06-10 à 12:00 heure de Paris (UTC+2)
  const noonParis = new Date('2026-06-10T10:00:00Z');
  /** Un instant 1 minute après le dernier créneau passé avant midi. */
  const justAfterSlot = () => {
    const slots = reminderSlots(prefs);
    const minutes = localParts(noonParis, 'Europe/Paris').minutes;
    const idx = slots.filter((s) => s <= minutes).length - 1;
    return new Date(noonParis.getTime() + (slots[idx] - minutes + 1) * 60_000);
  };

  it('respecte le nombre de rappels par mode', () => {
    expect(reminderSlots({ ...prefs, mode: 'calm' })).toHaveLength(2);
    expect(reminderSlots({ ...prefs, mode: 'normal' }).length).toBeGreaterThanOrEqual(3);
    expect(reminderSlots({ ...prefs, mode: 'intense' }).length).toBeGreaterThanOrEqual(6);
    // Mode personnalisé : créneaux dédoublonnés et triés.
    expect(reminderSlots({ ...prefs, mode: 'custom', customTimes: [1200, 480, 720, 720] })).toEqual([480, 720, 1200]);
  });

  it('exclut les heures silencieuses, y compris quand elles chevauchent minuit', () => {
    expect(isInQuietHours(23 * 60, prefs)).toBe(true);
    expect(isInQuietHours(7 * 60, prefs)).toBe(true);
    expect(isInQuietHours(12 * 60, prefs)).toBe(false);
    const late = reminderSlots({ ...prefs, mode: 'custom', customTimes: [60, 720, 1380] });
    expect(late).toEqual([720]);
  });

  it('n’envoie rien sans consentement explicite', () => {
    expect(decideReminder({ now: noonParis, prefs: { ...prefs, consent: false }, relevantItems: 5, lastSlotKey: null, lastActivityAt: null })).toMatchObject({ send: false, reason: 'no_consent' });
  });

  it('n’envoie rien quand il n’y a rien de pertinent à réviser', () => {
    expect(decideReminder({ now: justAfterSlot(), prefs, relevantItems: 0, lastSlotKey: null, lastActivityAt: null })).toMatchObject({ send: false, reason: 'nothing_to_review' });
  });

  it('ne rattrape pas un créneau manqué depuis longtemps', () => {
    const now = new Date(justAfterSlot().getTime() + 50 * 60_000);
    expect(decideReminder({ now, prefs: { ...prefs, mode: 'calm' }, relevantItems: 3, lastSlotKey: null, lastActivityAt: null }).send).toBe(false);
  });

  it('envoie une seule fois par créneau', () => {
    const slots = reminderSlots(prefs);
    const minutes = localParts(noonParis, 'Europe/Paris').minutes;
    const idx = slots.filter((s) => s <= minutes).length - 1;
    // Positionne « maintenant » juste après le créneau courant.
    const now = new Date(noonParis.getTime() + (slots[idx] - minutes + 1) * 60_000);
    const first = decideReminder({ now, prefs, relevantItems: 3, lastSlotKey: null, lastActivityAt: null });
    expect(first.send).toBe(true);
    const second = decideReminder({ now, prefs, relevantItems: 3, lastSlotKey: (first as { slotKey: string }).slotKey, lastActivityAt: null });
    expect(second).toMatchObject({ send: false, reason: 'already_handled' });
  });

  it('respecte la pause et ne dérange pas un utilisateur en train d’étudier', () => {
    const slots = reminderSlots(prefs);
    const minutes = localParts(noonParis, 'Europe/Paris').minutes;
    const idx = slots.filter((s) => s <= minutes).length - 1;
    const now = new Date(noonParis.getTime() + (slots[idx] - minutes + 1) * 60_000);
    expect(decideReminder({ now, prefs: { ...prefs, pausedUntil: new Date(now.getTime() + 3600_000) }, relevantItems: 3, lastSlotKey: null, lastActivityAt: null })).toMatchObject({ reason: 'paused' });
    expect(decideReminder({ now, prefs, relevantItems: 3, lastSlotKey: null, lastActivityAt: new Date(now.getTime() - 5 * 60_000) })).toMatchObject({ reason: 'recently_active' });
  });

  it('calcule l’heure locale selon le fuseau', () => {
    expect(localParts(new Date('2026-01-15T23:30:00Z'), 'Europe/Paris')).toEqual({ dateKey: '2026-01-16', minutes: 30 });
    expect(localParts(new Date('2026-01-15T23:30:00Z'), 'America/New_York').dateKey).toBe('2026-01-15');
  });
});

describe('séries, XP, quêtes, préparation', () => {
  it('compte les jours consécutifs et garde la série si aujourd’hui n’est pas encore fait', () => {
    expect(computeStreak(['2026-03-08', '2026-03-09', '2026-03-10'], '2026-03-10')).toMatchObject({ current: 3, todayDone: true });
    expect(computeStreak(['2026-03-08', '2026-03-09'], '2026-03-10')).toMatchObject({ current: 2, todayDone: false });
  });

  it('pardonne un jour manqué mais pas deux', () => {
    expect(computeStreak(['2026-03-06', '2026-03-07', '2026-03-09', '2026-03-10'], '2026-03-10')).toMatchObject({ current: 4, graceDaysUsed: 1 });
    expect(computeStreak(['2026-03-06', '2026-03-07', '2026-03-10'], '2026-03-10').current).toBe(1);
    expect(computeStreak([], '2026-03-10').current).toBe(0);
  });

  it('calcule le niveau à partir de l’XP', () => {
    expect(levelFromXp(0)).toEqual({ level: 1, intoLevel: 0, forNext: 100 });
    expect(levelFromXp(150)).toEqual({ level: 2, intoLevel: 50, forNext: 200 });
  });

  it('propose 3 quêtes stables pour la journée', () => {
    const stats = { newItems: 6, reviews: 3, kanjiReviews: 0, bestCombo: 5, perfectLessons: 0, listeningCorrect: 0 };
    const q = dailyQuests('2026-03-10', stats);
    expect(q).toHaveLength(3);
    expect(dailyQuests('2026-03-10', stats)).toEqual(q);
    q.forEach((x) => expect(x.progress).toBeLessThanOrEqual(x.target));
  });

  it('reste prudente dans l’estimation de préparation', () => {
    const now = new Date('2026-03-10T00:00:00Z');
    const perfect = Array.from({ length: 10 }, () => ({ ...newCard(now), state: 'review' as const, stability: 365, lastReview: now, due: now }));
    expect(estimateReadiness(perfect, 10, now).percent).toBeLessThanOrEqual(90);
    expect(estimateReadiness([], 100, now).percent).toBe(0);
    expect(estimateReadiness([schedule(newCard(now), 3, now)], 100, now).percent).toBe(0);
  });
});
