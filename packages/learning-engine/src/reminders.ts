import { localParts } from './time';

export type ReminderMode = 'calm' | 'normal' | 'intense' | 'custom';

export const REMINDERS_PER_MODE: Record<Exclude<ReminderMode, 'custom'>, number> = {
  calm: 2, // Tranquille : 1 à 2
  normal: 4, // Normal : 3 à 5
  intense: 8, // Intensif : 6 à 10
};

export interface ReminderPrefs {
  enabled: boolean;
  /** Consentement explicite donné par l'utilisateur. */
  consent: boolean;
  mode: ReminderMode;
  /** Créneaux personnalisés (minutes depuis minuit) pour le mode « custom ». */
  customTimes: number[];
  /** Fenêtre d'envoi (minutes depuis minuit). */
  windowStart: number;
  windowEnd: number;
  /** Heures silencieuses (peuvent chevaucher minuit). */
  quietStart: number | null;
  quietEnd: number | null;
  pausedUntil: Date | null;
  timezone: string;
}

export const DEFAULT_REMINDER_PREFS: ReminderPrefs = {
  enabled: false,
  consent: false,
  mode: 'normal',
  customTimes: [],
  windowStart: 9 * 60,
  windowEnd: 21 * 60,
  quietStart: 22 * 60,
  quietEnd: 8 * 60,
  pausedUntil: null,
  timezone: 'Europe/Paris',
};

export function isInQuietHours(minutes: number, prefs: Pick<ReminderPrefs, 'quietStart' | 'quietEnd'>): boolean {
  const { quietStart: s, quietEnd: e } = prefs;
  if (s == null || e == null || s === e) return false;
  return s < e ? minutes >= s && minutes < e : minutes >= s || minutes < e;
}

/** Créneaux du jour (minutes locales), régulièrement espacés et hors heures silencieuses. */
export function reminderSlots(prefs: ReminderPrefs): number[] {
  let slots: number[];
  if (prefs.mode === 'custom') {
    slots = [...new Set(prefs.customTimes.filter((m) => m >= 0 && m < 1440))].sort((a, b) => a - b).slice(0, 10);
  } else {
    const count = REMINDERS_PER_MODE[prefs.mode];
    const start = prefs.windowStart;
    const end = prefs.windowEnd > start ? prefs.windowEnd : start + 60;
    const step = (end - start) / count;
    slots = Array.from({ length: count }, (_, i) => Math.round((start + (i + 0.5) * step) / 5) * 5);
  }
  return slots.filter((m) => !isInQuietHours(m, prefs));
}

export interface ReminderContext {
  now: Date;
  prefs: ReminderPrefs;
  /** Nombre de notions pertinentes à interroger (révisions dues ou cartes en apprentissage). */
  relevantItems: number;
  /** Dernier créneau déjà traité (clé AAAA-MM-JJ#index). */
  lastSlotKey: string | null;
  /** Dernière activité d'étude (pour ne pas déranger quelqu'un qui étudie déjà). */
  lastActivityAt: Date | null;
}

export type ReminderDecision =
  | { send: true; slotKey: string }
  | { send: false; reason: string; slotKey?: string };

/** Délai au-delà duquel un créneau manqué (serveur arrêté…) n'est plus rattrapé. */
const SLOT_GRACE_MINUTES = 45;

/**
 * Décide si un rappel doit partir maintenant. Fonction pure, appelée chaque minute
 * par le planificateur côté serveur (et réutilisable côté mobile pour les notifications locales).
 */
export function decideReminder(ctx: ReminderContext): ReminderDecision {
  const { prefs, now } = ctx;
  if (!prefs.consent) return { send: false, reason: 'no_consent' };
  if (!prefs.enabled) return { send: false, reason: 'disabled' };
  if (prefs.pausedUntil && prefs.pausedUntil.getTime() > now.getTime()) return { send: false, reason: 'paused' };

  const { dateKey, minutes } = localParts(now, prefs.timezone);
  if (isInQuietHours(minutes, prefs)) return { send: false, reason: 'quiet_hours' };

  const slots = reminderSlots(prefs);
  let index = -1;
  for (let i = 0; i < slots.length; i++) if (slots[i] <= minutes) index = i;
  if (index < 0) return { send: false, reason: 'no_slot_yet' };
  const slotKey = `${dateKey}#${index}`;
  if (ctx.lastSlotKey === slotKey) return { send: false, reason: 'already_handled', slotKey };
  if (minutes - slots[index] > SLOT_GRACE_MINUTES) return { send: false, reason: 'slot_missed', slotKey };
  if (ctx.relevantItems <= 0) return { send: false, reason: 'nothing_to_review', slotKey };
  if (ctx.lastActivityAt && now.getTime() - ctx.lastActivityAt.getTime() < 20 * 60_000)
    return { send: false, reason: 'recently_active', slotKey };

  return { send: true, slotKey };
}

const MESSAGES = [
  'Un petit défi japonais t’attend ! 🐱',
  'Trente secondes pour réveiller ta mémoire ? 🧠',
  'Un mot veut te dire bonjour… こんにちは ! 👋',
  'Ta prochaine révision est prête ⛩️',
  'Petit quiz express : tu te souviens ? 🍙',
];

export function reminderMessage(seed: number): string {
  return MESSAGES[Math.abs(seed) % MESSAGES.length];
}
