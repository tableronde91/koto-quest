import { Platform } from 'react-native';
import * as Notifications from 'expo-notifications';
import type { NotificationPrefsDto } from '@koto/shared';

/**
 * Rappels natifs : notifications locales planifiées chaque jour aux créneaux calculés par le serveur
 * (mêmes réglages que la version web). Toucher la notification ouvre une séance de révision.
 */
export const REVIEW_URL = '/review';
const supported = Platform.OS !== 'web';

if (supported) {
  Notifications.setNotificationHandler({
    handleNotification: async () => ({ shouldShowBanner: true, shouldShowList: true, shouldPlaySound: false, shouldSetBadge: false }),
  });
}

export const notificationsSupported = () => supported;

export async function requestPermission(): Promise<boolean> {
  if (!supported) return false;
  const current = await Notifications.getPermissionsAsync();
  if (current.granted) return true;
  const asked = await Notifications.requestPermissionsAsync();
  return asked.granted;
}

const MESSAGES = [
  { title: 'Un petit défi t’attend ⛩️', body: 'Quelques notions sont sur le point de t’échapper : deux minutes suffisent.' },
  { title: 'Le gardien s’impatiente 👹', body: 'Une révision rapide pour garder ta série ?' },
  { title: 'Ton jardin a soif 🌸', body: 'Arrose tes notions avant qu’elles ne fanent.' },
];

/** Remplace les rappels planifiés par ceux des créneaux actuels (minutes depuis minuit). */
export async function scheduleReminders(prefs: Pick<NotificationPrefsDto, 'enabled' | 'consent' | 'slots'>): Promise<number> {
  if (!supported) return 0;
  await Notifications.cancelAllScheduledNotificationsAsync();
  if (!prefs.consent || !prefs.enabled) return 0;
  if (Platform.OS === 'android') {
    await Notifications.setNotificationChannelAsync('rappels', { name: 'Rappels de révision', importance: Notifications.AndroidImportance.DEFAULT });
  }
  let n = 0;
  for (const [i, minutes] of prefs.slots.entries()) {
    const m = MESSAGES[i % MESSAGES.length];
    await Notifications.scheduleNotificationAsync({
      content: { title: m.title, body: m.body, data: { url: REVIEW_URL } },
      trigger: { type: Notifications.SchedulableTriggerInputTypes.DAILY, hour: Math.floor(minutes / 60), minute: minutes % 60, channelId: 'rappels' },
    });
    n++;
  }
  return n;
}

export async function cancelReminders() {
  if (supported) await Notifications.cancelAllScheduledNotificationsAsync();
}

/** Ouvre la bonne page quand on touche une notification (y compris au démarrage de l'appli). */
export function onNotificationOpen(open: (url: string) => void): () => void {
  if (!supported) return () => undefined;
  const handle = (r: Notifications.NotificationResponse | null) => {
    const url = r?.notification.request.content.data?.url;
    if (typeof url === 'string') open(url);
  };
  Notifications.getLastNotificationResponseAsync().then(handle).catch(() => undefined);
  const sub = Notifications.addNotificationResponseReceivedListener(handle);
  return () => sub.remove();
}
