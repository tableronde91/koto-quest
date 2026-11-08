import { useEffect } from 'react';
import { Stack, useRouter, useSegments } from 'expo-router';
import { StatusBar } from 'expo-status-bar';
import { QueryClient, QueryClientProvider } from '@tanstack/react-query';
import { SafeAreaProvider } from 'react-native-safe-area-context';
import { AuthProvider, useAuth } from '../src/auth';
import { onNotificationOpen } from '../src/notifications';
import { C } from '../src/theme';
import { Loading } from '../src/ui';

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

  if (!ready) return <Loading label="Ouverture de Koto Quest…" />;
  return (
    <Stack screenOptions={{ headerShown: false, contentStyle: { backgroundColor: C.paper } }}>
      <Stack.Screen name="(tabs)" />
      <Stack.Screen name="welcome" />
      <Stack.Screen name="onboarding" />
      <Stack.Screen name="lesson/[slug]" options={{ gestureEnabled: false }} />
      <Stack.Screen name="review" options={{ gestureEnabled: false }} />
    </Stack>
  );
}

export default function RootLayout() {
  return (
    <SafeAreaProvider>
      <QueryClientProvider client={queryClient}>
        <AuthProvider>
          <StatusBar style="dark" />
          <Gate />
        </AuthProvider>
      </QueryClientProvider>
    </SafeAreaProvider>
  );
}
