import { useQuery } from '@tanstack/react-query';
import type { DashboardDto, NotificationPrefsDto, PathDto } from '@koto/shared';
import { api } from './api';

export const useDashboard = () => useQuery({ queryKey: ['dashboard'], queryFn: () => api<DashboardDto>('/dashboard') });
export const usePath = (level: string) => useQuery({ queryKey: ['path', level], queryFn: () => api<PathDto>(`/path/${level}`) });
export const useReviewSummary = () => useQuery({ queryKey: ['reviews'], queryFn: () => api<{ due: number; learningSoon: number }>('/reviews/summary') });
export const useNotifPrefs = () => useQuery({ queryKey: ['notif-prefs'], queryFn: () => api<NotificationPrefsDto>('/notifications/preferences') });
