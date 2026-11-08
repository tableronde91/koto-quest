import { ReactNode, createContext, useCallback, useContext, useEffect, useState } from 'react';
import { useQuery, useQueryClient } from '@tanstack/react-query';
import type { MeDto } from '@koto/shared';
import { ApiError, api, loadToken, post, saveToken } from './api';

interface AuthState {
  ready: boolean;
  me: MeDto | null;
  login: (email: string, password: string) => Promise<void>;
  register: (displayName: string, email: string, password: string) => Promise<void>;
  logout: () => Promise<void>;
}

const Ctx = createContext<AuthState | null>(null);

export function AuthProvider({ children }: { children: ReactNode }) {
  const qc = useQueryClient();
  const [tokenLoaded, setTokenLoaded] = useState(false);
  const [hasToken, setHasToken] = useState(false);

  useEffect(() => {
    loadToken().then((t) => {
      setHasToken(!!t);
      setTokenLoaded(true);
    });
  }, []);

  const meQuery = useQuery({
    queryKey: ['me'],
    enabled: tokenLoaded && hasToken,
    queryFn: async () => {
      try {
        return await api<MeDto>('/me');
      } catch (e) {
        if (e instanceof ApiError && e.status === 401) {
          await saveToken(null);
          setHasToken(false);
          return null;
        }
        throw e;
      }
    },
  });

  const start = useCallback(
    async (token: string | undefined) => {
      if (!token) throw new Error('Réponse de connexion inattendue.');
      await saveToken(token);
      setHasToken(true);
      await qc.invalidateQueries();
    },
    [qc],
  );

  const value: AuthState = {
    ready: tokenLoaded && (!hasToken || !meQuery.isLoading),
    me: hasToken ? meQuery.data ?? null : null,
    login: async (email, password) => start((await post<{ token?: string }>('/auth/login', { email, password })).token),
    register: async (displayName, email, password) => start((await post<{ token?: string }>('/auth/register', { displayName, email, password })).token),
    logout: async () => {
      await post('/auth/logout').catch(() => undefined);
      await saveToken(null);
      setHasToken(false);
      qc.clear();
    },
  };
  return <Ctx.Provider value={value}>{children}</Ctx.Provider>;
}

export function useAuth() {
  const v = useContext(Ctx);
  if (!v) throw new Error('AuthProvider manquant');
  return v;
}
