import { Pressable, Text, View } from 'react-native';
import { useRouter } from 'expo-router';
import { useQuery } from '@tanstack/react-query';
import type { AchievementDto, AchievementsDto } from '@koto/shared';
import { api } from '../src/api';
import { Medal, RARITY_LABEL } from '../src/Achievements';
import { C } from '../src/theme';
import { ErrorBox, H1, H2, Loading, P, ProgressBar, Screen } from '../src/ui';
import { T, getLocale } from '../src/i18n';

// Traduits à l'affichage avec T()
const CATEGORIES: { id: AchievementDto['category']; title: string }[] = [
  { id: 'study', title: 'Étude' },
  { id: 'streak', title: 'Régularité' },
  { id: 'mastery', title: 'Maîtrise' },
  { id: 'adventure', title: 'Aventure' },
  { id: 'play', title: 'Jeux et collection' },
];

export default function Achievements() {
  const router = useRouter();
  const { data, isLoading, error, refetch } = useQuery({ queryKey: ['achievements'], queryFn: () => api<AchievementsDto>('/achievements') });
  if (isLoading) return <Loading />;
  if (error || !data) return <Screen><ErrorBox error={error} onRetry={refetch} /></Screen>;
  return (
    <Screen>
      <View style={{ flexDirection: 'row', alignItems: 'center', gap: 8 }}>
        <Pressable accessibilityRole="button" accessibilityLabel={T('Retour')} onPress={() => (router.canGoBack() ? router.back() : router.replace('/profile'))} hitSlop={12}>
          <Text style={{ fontSize: 26, color: C.ink, fontWeight: '800' }}>‹</Text>
        </Pressable>
        <H1>{T('Succès')}</H1>
      </View>
      <P soft>{T('Chaque succès rapporte des pièces et de l’expérience, une seule fois.')}</P>
      <View style={{ flexDirection: 'row' }}><ProgressBar value={data.unlocked} max={data.total} color={C.gold} label={T('Succès débloqués')} /></View>
      <P soft style={{ fontSize: 14 }}>{T('{0} sur {1} débloqués', [data.unlocked, data.total])}</P>
      {CATEGORIES.map((cat) => {
        const list = data.achievements.filter((a) => a.category === cat.id);
        if (!list.length) return null;
        return (
          <View key={cat.id} style={{ gap: 10 }}>
            <H2>{T(cat.title)} <Text style={{ fontSize: 15, fontWeight: '400', color: C.inkSoft }}>{list.filter((a) => a.unlocked).length}/{list.length}</Text></H2>
            {list.map((a) => (
              <View key={a.slug} testID="achievement" style={{ flexDirection: 'row', alignItems: 'center', gap: 12, borderWidth: 1, borderStyle: a.unlocked ? 'solid' : 'dashed', borderColor: C.line, borderRadius: 16, padding: 10, backgroundColor: a.unlocked ? C.surface : 'transparent' }}>
                <Medal a={a} size={56} />
                <View style={{ flex: 1, gap: 2 }}>
                  <Text style={{ fontWeight: '800', color: a.unlocked ? C.ink : C.inkSoft }}>{a.title}</Text>
                  <Text style={{ fontSize: 13, color: C.inkSoft }}>{a.description}</Text>
                  <Text style={{ fontSize: 12, color: C.inkSoft }}>
                    {T(RARITY_LABEL[a.rarity])} ·{' '}
                    {a.unlocked
                      ? a.unlockedAt
                        ? T('obtenu le {0}', [new Date(a.unlockedAt).toLocaleDateString(getLocale() === 'en' ? 'en-GB' : 'fr-FR', { day: 'numeric', month: 'short' })])
                        : T('obtenu')
                      : T('{0}/{1} · +{2} pièces', [a.value, a.target, a.coins])}
                  </Text>
                </View>
              </View>
            ))}
          </View>
        );
      })}
    </Screen>
  );
}
