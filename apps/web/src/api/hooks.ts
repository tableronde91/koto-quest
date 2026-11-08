import { useMutation, useQuery, useQueryClient } from '@tanstack/react-query';
import type { AchievementsDto, CharactersDto, DashboardDto, InboxItemDto, LessonDto, MeDto, NotificationPrefsDto, PathDto, StatsDto } from '@koto/shared';
import { ApiError, api, put } from './client';

export const qk = {
  me: ['me'] as const,
  dashboard: ['dashboard'] as const,
  path: (l: string) => ['path', l] as const,
  lesson: (s: string) => ['lesson', s] as const,
  stats: ['stats'] as const,
  reviews: ['reviews'] as const,
  notifPrefs: ['notif-prefs'] as const,
  inbox: ['inbox'] as const,
  characters: ['characters'] as const,
  achievements: ['achievements'] as const,
};

export function useMe() {
  return useQuery({
    queryKey: qk.me,
    queryFn: async () => {
      try {
        return await api<MeDto>('/me');
      } catch (e) {
        if (e instanceof ApiError && e.status === 401) return null;
        throw e;
      }
    },
    staleTime: 60_000,
  });
}

export const useDashboard = () => useQuery({ queryKey: qk.dashboard, queryFn: () => api<DashboardDto>('/dashboard') });
export const usePath = (level: string) => useQuery({ queryKey: qk.path(level), queryFn: () => api<PathDto>(`/path/${level}`) });
export const useLesson = (slug: string) => useQuery({ queryKey: qk.lesson(slug), queryFn: () => api<LessonDto>(`/lessons/${slug}`), retry: false });
export const useAchievements = () => useQuery({ queryKey: qk.achievements, queryFn: () => api<AchievementsDto>('/achievements') });
export const useStats = () => useQuery({ queryKey: qk.stats, queryFn: () => api<StatsDto>('/stats') });
export const useReviewSummary = () =>
  useQuery({ queryKey: qk.reviews, queryFn: () => api<{ due: number; learningSoon: number; plan: DashboardDto['plan'] }>('/reviews/summary') });
export const useNotifPrefs = () => useQuery({ queryKey: qk.notifPrefs, queryFn: () => api<NotificationPrefsDto>('/notifications/preferences') });

/** Boîte de réception des défis : interrogée régulièrement pour afficher les popups in-app. */
export const useInbox = (enabled: boolean) =>
  useQuery({ queryKey: qk.inbox, queryFn: () => api<InboxItemDto[]>('/notifications/inbox'), enabled, refetchInterval: 60_000, refetchOnWindowFocus: true });

export function useUpdateNotifPrefs() {
  const qc = useQueryClient();
  return useMutation({
    mutationFn: (body: Partial<NotificationPrefsDto>) => put<NotificationPrefsDto>('/notifications/preferences', body),
    // Mise à jour optimiste : la case cochée réagit immédiatement, et revient en arrière en cas d'erreur.
    onMutate: async (body) => {
      await qc.cancelQueries({ queryKey: qk.notifPrefs });
      const previous = qc.getQueryData<NotificationPrefsDto>(qk.notifPrefs);
      if (previous) qc.setQueryData(qk.notifPrefs, { ...previous, ...body });
      return { previous };
    },
    onError: (_e, _b, ctx) => {
      if (ctx?.previous) qc.setQueryData(qk.notifPrefs, ctx.previous);
    },
    onSuccess: (data) => {
      qc.setQueryData(qk.notifPrefs, data);
      qc.invalidateQueries({ queryKey: qk.dashboard });
    },
  });
}

export function useUpdatePrefs() {
  const qc = useQueryClient();
  return useMutation({
    mutationFn: (body: Record<string, unknown>) => put<MeDto>('/me/preferences', body),
    onSuccess: (me) => {
      qc.setQueryData(qk.me, me);
      qc.invalidateQueries();
    },
  });
}

export const useCharacters = () => useQuery({ queryKey: qk.characters, queryFn: () => api<CharactersDto>('/characters') });
