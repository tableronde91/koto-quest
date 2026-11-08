import { Platform } from 'react-native';
import * as SecureStore from 'expo-secure-store';
import { API_URL } from './config';

/**
 * Client HTTP de l'application mobile : jeton de session rangé dans le coffre sécurisé
 * (Keychain / Keystore), envoyé en « Authorization: Bearer ». Sur le web (aperçu), stockage local.
 */
const KEY = 'koto-session';

export class ApiError extends Error {
  constructor(public status: number, message: string) {
    super(message);
  }
}

let memoryToken: string | null = null;

export async function loadToken(): Promise<string | null> {
  try {
    memoryToken = Platform.OS === 'web' ? globalThis.localStorage?.getItem(KEY) ?? null : await SecureStore.getItemAsync(KEY);
  } catch {
    memoryToken = null;
  }
  return memoryToken;
}

export async function saveToken(token: string | null) {
  memoryToken = token;
  try {
    if (Platform.OS === 'web') {
      if (token) globalThis.localStorage?.setItem(KEY, token);
      else globalThis.localStorage?.removeItem(KEY);
    } else if (token) await SecureStore.setItemAsync(KEY, token);
    else await SecureStore.deleteItemAsync(KEY);
  } catch {
    // Coffre indisponible : la session reste en mémoire le temps de l'utilisation.
  }
}

const tz = Intl.DateTimeFormat().resolvedOptions().timeZone;

export async function api<T>(path: string, init: { method?: string; body?: unknown } = {}): Promise<T> {
  let res: Response;
  try {
    res = await fetch(`${API_URL}/api${path}`, {
      method: init.method ?? 'GET',
      headers: {
        'Content-Type': 'application/json',
        'X-Koto-Client': 'mobile',
        'X-Timezone': tz,
        ...(memoryToken ? { Authorization: `Bearer ${memoryToken}` } : {}),
      },
      body: init.body === undefined ? undefined : JSON.stringify(init.body),
    });
  } catch {
    throw new ApiError(0, `Serveur injoignable (${API_URL}). Vérifie que l’API tourne et que le téléphone est sur le même réseau.`);
  }
  if (res.status === 204) return undefined as T;
  const data = await res.json().catch(() => null);
  if (!res.ok) {
    const msg = data?.message;
    throw new ApiError(res.status, Array.isArray(msg) ? msg[0] : msg ?? 'Une erreur est survenue.');
  }
  return data as T;
}

export const post = <T>(path: string, body: unknown = {}) => api<T>(path, { method: 'POST', body });
export const put = <T>(path: string, body: unknown) => api<T>(path, { method: 'PUT', body });
