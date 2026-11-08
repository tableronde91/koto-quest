import { StrictMode, Suspense, lazy, useEffect } from 'react';
import { createRoot } from 'react-dom/client';
import { BrowserRouter, HashRouter, Navigate, Route, Routes, useLocation } from 'react-router';
import { MutationCache, QueryCache, QueryClient, QueryClientProvider } from '@tanstack/react-query';
import { MotionConfig, motion } from 'motion/react';
import './index.css';
import { ApiError, LOCAL } from './api/client';
import { useMe } from './api/hooks';
import { locale, setLocale } from './i18n';
import { AppShell } from './components/AppShell';
import { ErrorBox, Spinner } from './components/ui';
import { registerServiceWorker } from './lib/push';
import { ForgotPasswordPage, ResetPasswordPage, WelcomePage } from './pages/Auth';
import { BossPage } from './pages/Boss';
import { CharacterPage } from './pages/Character';
import { GamePlayPage, GamesPage } from './pages/Games';
import { ExamPage, PlacementPage } from './pages/Exam';
import { CharacterPracticePage, CharactersPage } from './pages/Characters';
import { DashboardPage } from './pages/Dashboard';
import { LessonPage } from './pages/Lesson';
import { OnboardingPage } from './pages/Onboarding';
import { PathPage } from './pages/Path';
import { QuizPage, ReviewSessionPage, ReviewsPage } from './pages/Reviews';
import { SettingsPage } from './pages/Settings';
// Les graphiques (recharts) ne sont chargés qu'à l'ouverture de la page Progrès.
import { AchievementsPage } from './pages/Achievements';
import { PrepaPage } from './pages/Prepa';
import { DuelArenaPage, DuelLobbyPage } from './pages/Duel';
import { ExpressionPracticePage, ExpressionsPage } from './pages/Expressions';
const StatsPage = lazy(() => import('./pages/Stats').then((m) => ({ default: m.StatsPage })));

const onAuthError = (e: unknown) => {
  // Session expirée : on renvoie vers la connexion
  if (e instanceof ApiError && e.status === 401) queryClient.setQueryData(['me'], null);
};
const queryClient = new QueryClient({
  defaultOptions: { queries: { retry: (n, e) => !(e instanceof ApiError && e.status < 500) && n < 2, refetchOnWindowFocus: true } },
  queryCache: new QueryCache({ onError: onAuthError }),
  mutationCache: new MutationCache({ onError: onAuthError }),
});

function App() {
  const { data: me, isLoading, error, refetch } = useMe();
  const location = useLocation();

  useEffect(() => {
    const theme = me?.preferences.theme ?? 'system';
    if (theme === 'system') delete document.documentElement.dataset.theme;
    else document.documentElement.dataset.theme = theme;
    document.documentElement.classList.toggle('reduced', !!me?.preferences.reducedMotion);
  }, [me?.preferences.theme, me?.preferences.reducedMotion]);

  // Connecté, la langue suit celle enregistrée sur le compte (une seule fois par session).
  useEffect(() => {
    const want = me?.onboarded ? me.preferences.locale : undefined;
    if (LOCAL || !want || want === locale) return;
    try {
      if (sessionStorage.getItem('koto-locale-sync') === want) return;
      sessionStorage.setItem('koto-locale-sync', want);
    } catch {
      return;
    }
    setLocale(want);
  }, [me?.onboarded, me?.preferences.locale]);

  if (isLoading) return <Spinner />;
  if (error) return <div className="p-6"><ErrorBox error={error} onRetry={refetch} /></div>;

  if (!me) {
    return (
      <Routes>
        <Route path="/welcome" element={<WelcomePage />} />
        <Route path="/forgot-password" element={<ForgotPasswordPage />} />
        <Route path="/reset-password" element={<ResetPasswordPage />} />
        {/* Après connexion, on revient sur la page demandée (ex. un mini-quiz ouvert depuis une notification) */}
        <Route path="*" element={<Navigate to="/welcome" replace state={{ from: location.pathname + location.search }} />} />
      </Routes>
    );
  }
  if (!me.onboarded) return <OnboardingPage me={me} />;

  return (
    <MotionConfig reducedMotion={me.preferences.reducedMotion ? 'always' : 'user'}>
      <AppShell me={me}>
        {/* Transition douce à chaque changement de page (désactivée si animations réduites) */}
        <motion.div key={location.pathname} initial={{ opacity: 0, y: 8 }} animate={{ opacity: 1, y: 0 }} transition={{ duration: 0.22, ease: 'easeOut' }}>
        <Routes>
          <Route path="/" element={<DashboardPage />} />
          <Route path="/path" element={<PathPage />} />
          <Route path="/lesson/:slug" element={<LessonPage key={location.pathname} me={me} />} />
          <Route path="/boss/:world" element={<BossPage key={location.pathname} me={me} />} />
          <Route path="/avatar" element={<CharacterPage />} />
          <Route path="/exam/:slug" element={<ExamPage key={location.pathname} />} />
          <Route path="/placement" element={<PlacementPage />} />
          <Route path="/games" element={<GamesPage />} />
          <Route path="/games/:id" element={<GamePlayPage key={location.pathname} />} />
          <Route path="/characters" element={<CharactersPage />} />
          <Route path="/expressions" element={<ExpressionsPage />} />
          <Route path="/expressions/practice/:theme" element={<ExpressionPracticePage key={location.pathname} me={me} />} />
          <Route path="/characters/practice/:scope" element={<CharacterPracticePage key={location.pathname} me={me} />} />
          <Route path="/reviews" element={<ReviewsPage />} />
          <Route path="/reviews/session" element={<ReviewSessionPage me={me} />} />
          <Route path="/quiz/:id" element={<QuizPage me={me} />} />
          <Route path="/achievements" element={<AchievementsPage />} />
          <Route path="/duel" element={<DuelLobbyPage />} />
          <Route path="/duel/:id" element={<DuelArenaPage key={location.pathname} />} />
          <Route path="/prepa" element={<PrepaPage me={me} />} />
          <Route path="/stats" element={<Suspense fallback={<Spinner />}><StatsPage /></Suspense>} />
          <Route path="/settings" element={<SettingsPage me={me} />} />
          <Route path="/welcome" element={<Navigate to={(location.state as { from?: string } | null)?.from ?? '/'} replace />} />
          <Route path="*" element={<Navigate to="/" replace />} />
        </Routes>
        </motion.div>
      </AppShell>
    </MotionConfig>
  );
}

// Hors ligne (fichier ouvert directement) : routage par « # » et pas de service worker.
const Router = LOCAL ? HashRouter : BrowserRouter;
if (LOCAL) import('./local/reminders').then((m) => m.startLocalReminders(queryClient));
else registerServiceWorker();

createRoot(document.getElementById('root')!).render(
  <StrictMode>
    <QueryClientProvider client={queryClient}>
      <Router>
        <App />
      </Router>
    </QueryClientProvider>
  </StrictMode>,
);
