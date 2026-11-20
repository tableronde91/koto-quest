import { useEffect, useState } from 'react';
import { Stack, useRouter, useSegments } from 'expo-router';
import { StatusBar } from 'expo-status-bar';
import { QueryClient, QueryClientProvider } from '@tanstack/react-query';
import { SafeAreaProvider } from 'react-native-safe-area-context';
import { AuthProvider, useAuth } from '../src/auth';
import { AchievementWatcher } from '../src/Achievements';
import { onNotificationOpen } from '../src/notifications';
import { C } from '../src/theme';
import { Loading } from '../src/ui';
import { T, followAccount, getLocale, initLocale, takeReturnPath, useLocale } from '../src/i18n';

const queryClient = new QueryClient({ defaultOptions: { queries: { retry: 1, staleTime: 15_000 } } });

/** Aiguillage : non connecté → accueil ; connecté sans profil → onboarding ; sinon les onglets. */
function Gate() {
  const { ready, me } = useAuth();
  const segments = useSegments();
  const router = useRouter();

  useEffect(() => {
    if (!ready) return;
    const first = segments[0];
    if (!me && first !== 'welcome') router.replace('/welcome');
    else if (me && !me.onboarded && first !== 'onboarding') router.replace('/onboarding');
    else if (me && me.onboarded && (first === 'welcome' || first === 'onboarding')) router.replace('/');
  }, [ready, me, segments, router]);

  useEffect(() => onNotificationOpen((url) => router.push(url as never)), [router]);

  // Connecté sans choix fait sur ce téléphone : la langue suit celle du compte.
  useEffect(() => followAccount(me?.onboarded ? me.preferences.locale : undefined), [me?.onboarded, me?.preferences.locale]);

  // Après un changement de langue (appli redessinée), on revient sur l'écran où l'on était.
  useEffect(() => {
    if (!ready) return;
    const back = takeReturnPath();
    if (!back || back === '/') return;
    const t = setTimeout(() => router.replace(back as never), 0);
    return () => clearTimeout(t);
  }, [ready, router]);

  if (!ready) return <Loading label={T('Ouverture de Koto Quest…')} />;
  return (
    <>
    <Stack screenOptions={{ headerShown: false, contentStyle: { backgroundColor: C.paper } }}>
      <Stack.Screen name="(tabs)" />
      <Stack.Screen name="welcome" />
      <Stack.Screen name="onboarding" />
      <Stack.Screen name="lesson/[slug]" options={{ gestureEnabled: false }} />
      <Stack.Screen name="review" options={{ gestureEnabled: false }} />
      <Stack.Screen name="reading/[slug]" />
      <Stack.Screen name="boss/[slug]" options={{ gestureEnabled: false }} />
      <Stack.Screen name="exam/[slug]" options={{ gestureEnabled: false }} />
      <Stack.Screen name="games/[id]" options={{ gestureEnabled: false }} />
      <Stack.Screen name="settings" />
      <Stack.Screen name="character" />
      <Stack.Screen name="achievements" />
      <Stack.Screen name="progress" />
      <Stack.Screen name="practice" options={{ gestureEnabled: false }} />
      <Stack.Screen name="duel/index" />
      <Stack.Screen name="duel/[id]" options={{ gestureEnabled: false }} />
    </Stack>
    <AchievementWatcher />
    </>
  );
}

export default function RootLayout() {
  const [localeReady, setLocaleReady] = useState(false);
  const locale = useLocale();
  const [shown, setShown] = useState(locale);
  useEffect(() => {
    initLocale().then(() => {
      setShown(getLocale());
      setLocaleReady(true);
    });
  }, []);
  // Changement de langue : les données déjà reçues sont retraduites en les rechargeant.
  useEffect(() => {
    if (!localeReady || locale === shown) return;
    void queryClient.invalidateQueries(); // rechargées en arrière-plan, sans repasser par l'écran de chargement
    setShown(locale);
  }, [locale, shown, localeReady]);

  if (!localeReady) return <Loading />;
  return (
    <SafeAreaProvider>
      <QueryClientProvider client={queryClient}>
        <AuthProvider>
          <StatusBar style="dark" />
          <Gate key={locale} />
        </AuthProvider>
      </QueryClientProvider>
    </SafeAreaProvider>
  );
}
