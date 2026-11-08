/** Client HTTP : cookie de session httpOnly (credentials), JSON. Les réponses sont traduites dans la langue choisie. */
import { T, locale, translator } from '../i18n';

export class ApiError extends Error {
  constructor(public status: number, message: string) {
    super(message);
  }
}

const tz = Intl.DateTimeFormat().resolvedOptions().timeZone;

/** Version hors ligne : tout est traité dans le navigateur (src/local/backend.ts). */
export const LOCAL = import.meta.env.VITE_LOCAL === '1';

export async function api<T>(path: string, init: { method?: string; body?: unknown } = {}): Promise<T> {
  if (!translator) return raw<T>(path, init);
  // Réponses du joueur renvoyées en VO ; tout le texte reçu est traduit.
  const body = init.body === undefined ? undefined : translator.answersBack(init.body);
  try {
    return translator.deep(await raw<T>(path, { ...init, body }));
  } catch (e) {
    if (e instanceof ApiError) throw new ApiError(e.status, translator.tr(e.message));
    throw e;
  }
}

async function raw<T>(path: string, init: { method?: string; body?: unknown }): Promise<T> {
  if (LOCAL) {
    const { handle, HttpError } = await import('../local/backend');
    try {
      // Copie profonde : l'interface ne doit jamais modifier l'état local par référence.
      const r = await handle(init.method ?? "GET", path, init.body === undefined ? undefined : JSON.parse(JSON.stringify(init.body)));
      return (r === undefined ? undefined : JSON.parse(JSON.stringify(r))) as T;
    } catch (e) {
      if (e instanceof HttpError) throw new ApiError(e.status, e.message);
      throw new ApiError(500, e instanceof Error ? e.message : T('Erreur inattendue.'));
    }
  }
  let res: Response;
  try {
    res = await fetch(`/api${path}`, {
      method: init.method ?? "GET",
      credentials: 'same-origin',
      headers: { 'Content-Type': 'application/json', 'X-Timezone': tz, 'Accept-Language': locale },
      body: init.body === undefined ? undefined : JSON.stringify(init.body),
    });
  } catch {
    throw new ApiError(0, T('Connexion impossible. Vérifie ta connexion internet puis réessaie.'));
  }
  if (res.status === 204) return undefined as T;
  const data = await res.json().catch(() => null);
  if (!res.ok) {
    const msg = data?.message;
    throw new ApiError(res.status, Array.isArray(msg) ? msg[0] : msg ?? T('Une erreur est survenue.'));
  }
  return data as T;
}

/** Étapes qui peuvent débloquer un succès : l'application demande alors une vérification au serveur. */
const MILESTONE = /\/(lessons\/[\w-]+\/complete|worlds\/[\w-]+\/boss\/finish|games\/[\w-]+\/finish|exams\/[\w-]+\/submit|placement\/answer|shop\/acquire)$/;
export const PROGRESS_EVENT = 'koto:progress';

export const post = async <T>(path: string, body: unknown = {}) => {
  const r = await api<T>(path, { method: 'POST', body });
  if (MILESTONE.test(path) && typeof window !== 'undefined') window.dispatchEvent(new Event(PROGRESS_EVENT));
  return r;
};
export const put = <T>(path: string, body: unknown) => api<T>(path, { method: "PUT", body });
export const del = <T>(path: string, body?: unknown) => api<T>(path, { method: 'DELETE', body });
