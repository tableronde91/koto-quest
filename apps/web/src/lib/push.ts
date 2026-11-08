/** Web Push : nécessite un navigateur compatible, l'accord de l'utilisateur et une clé VAPID côté serveur. */
import { del, post } from '../api/client';

export const pushSupported = () => 'serviceWorker' in navigator && 'PushManager' in window && 'Notification' in window;

export function permission(): NotificationPermission | 'unsupported' {
  return pushSupported() ? Notification.permission : 'unsupported';
}

function urlBase64ToUint8Array(base64: string) {
  const padding = '='.repeat((4 - (base64.length % 4)) % 4);
  const raw = atob((base64 + padding).replace(/-/g, '+').replace(/_/g, '/'));
  return Uint8Array.from([...raw].map((c) => c.charCodeAt(0)));
}

export async function registerServiceWorker() {
  if (!('serviceWorker' in navigator)) return null;
  try {
    return await navigator.serviceWorker.register('/sw.js');
  } catch {
    return null;
  }
}

/** Demande l'autorisation puis abonne ce navigateur. Renvoie un état lisible. */
export async function subscribePush(vapidKey: string): Promise<'subscribed' | 'denied' | 'unsupported' | 'error'> {
  if (!pushSupported()) return 'unsupported';
  const perm = await Notification.requestPermission();
  if (perm !== 'granted') return 'denied';
  try {
    const reg = (await navigator.serviceWorker.getRegistration()) ?? (await registerServiceWorker());
    if (!reg) return 'error';
    await navigator.serviceWorker.ready;
    const sub = (await reg.pushManager.getSubscription()) ?? (await reg.pushManager.subscribe({ userVisibleOnly: true, applicationServerKey: urlBase64ToUint8Array(vapidKey) }));
    const json = sub.toJSON();
    await post('/notifications/push-subscription', { endpoint: json.endpoint, keys: json.keys });
    return 'subscribed';
  } catch {
    return 'error';
  }
}

export async function unsubscribePush() {
  const reg = await navigator.serviceWorker?.getRegistration();
  const sub = await reg?.pushManager.getSubscription();
  if (sub) {
    await del('/notifications/push-subscription', { endpoint: sub.endpoint }).catch(() => undefined);
    await sub.unsubscribe();
  }
}
