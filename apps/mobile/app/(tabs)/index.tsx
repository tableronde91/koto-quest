import { Pressable, RefreshControl, ScrollView, Text, View } from 'react-native';
import { useRouter } from 'expo-router';
import { SafeAreaView } from 'react-native-safe-area-context';
import { useDashboard } from '../../src/hooks';
import { C } from '../../src/theme';
import { Button, Card, ErrorBox, H2, Loading, P, ProgressBar } from '../../src/ui';
import { T, plural } from '../../src/i18n';

function greeting() {
  const h = new Date().getHours();
  return h < 11 ? 'おはよう' : h < 18 ? 'こんにちは' : 'こんばんは';
}

export default function Home() {
  const router = useRouter();
  const { data: d, isLoading, error, refetch, isRefetching } = useDashboard();
  if (isLoading) return <Loading />;
  if (error || !d) return <View style={{ padding: 18, paddingTop: 60 }}><ErrorBox error={error} onRetry={refetch} /></View>;
  const due = d.reviews.due;
  return (
    <SafeAreaView style={{ flex: 1, backgroundColor: C.paper }} edges={['top']}>
      <ScrollView contentContainerStyle={{ padding: 18, gap: 18, paddingBottom: 40 }} refreshControl={<RefreshControl refreshing={isRefetching} onRefresh={() => { refetch(); }} />}>
        <View style={{ flexDirection: 'row', justifyContent: 'space-between', alignItems: 'center' }}>
          <View style={{ flex: 1 }}>
            <Text style={{ color: C.inkSoft, fontSize: 18 }}>{greeting()}、{d.displayName}</Text>
            <Text accessibilityRole="header" style={{ fontSize: 26, fontWeight: '800', color: C.ink }}>{due ? plural(due, '{0} notion à réviser', '{0} notions à réviser') : d.nextLesson ? T('Prêt·e pour la suite ?') : T('Tout est à jour')}</Text>
          </View>
          <Pressable accessibilityRole="button" accessibilityLabel={T('{0} pièces, ouvrir la boutique', [d.coins])} onPress={() => router.push({ pathname: '/character', params: { t: 'boutique' } })} style={{ backgroundColor: C.surface, borderRadius: 99, paddingHorizontal: 12, paddingVertical: 6, borderWidth: 1, borderColor: C.line }}>
            <Text style={{ fontWeight: '800', color: C.goldInk }}>🪙 {d.coins}</Text>
          </Pressable>
        </View>

        {/* Action principale */}
        <View style={{ backgroundColor: C.ink, borderRadius: 24, padding: 20, gap: 12, overflow: 'hidden' }}>
          <Text style={{ position: 'absolute', right: -10, top: -24, fontSize: 150, fontWeight: '900', color: '#ffffff', opacity: 0.08 }}>{due ? '復' : '学'}</Text>
          {due > 0 ? (
            <>
              <Text style={{ color: C.paper, opacity: 0.85, fontSize: 16 }}>{T('Ces notions sont sur le point de t’échapper. Une révision maintenant les fixe pour plusieurs jours.')}</Text>
              <Button tone="gold" label={T('Réviser maintenant')} onPress={() => router.push('/review')} />
            </>
          ) : d.nextLesson ? (
            <>
              <Text style={{ color: C.paper, opacity: 0.75 }}>{d.nextLesson.worldTitle}</Text>
              <Text style={{ color: C.paper, fontSize: 24, fontWeight: '800' }}>{d.nextLesson.title}</Text>
              <Button tone="gold" label={T('Commencer la leçon')} onPress={() => router.push(`/lesson/${d.nextLesson!.slug}`)} />
            </>
          ) : (
            <Text style={{ color: C.paper }}>{T('Tu as terminé tout le contenu disponible. Les révisions continueront d’arriver au bon moment.')}</Text>
          )}
        </View>

        <View style={{ flexDirection: 'row', gap: 10 }}>
          {[
            { k: T('Série'), v: T('{0} j', [d.streak.current]), icon: d.streak.todayDone ? '🔥' : '🪵' },
            { k: T('Niveau'), v: String(d.xp.level), icon: '⭐' },
            { k: T('Mots'), v: String(d.mastered.words), icon: '🌸' },
          ].map((x) => (
            <Card key={x.k} style={{ flex: 1, alignItems: 'center', paddingVertical: 12 }}>
              <Text style={{ fontSize: 22 }}>{x.icon}</Text>
              <Text style={{ fontSize: 22, fontWeight: '800', color: C.ink }}>{x.v}</Text>
              <Text style={{ color: C.inkSoft, fontSize: 12 }}>{x.k}</Text>
            </Card>
          ))}
        </View>

        <View style={{ gap: 6 }}>
          <H2>{T('Niveau {0}', [d.xp.level])}</H2>
          <View style={{ flexDirection: 'row' }}><ProgressBar value={d.xp.intoLevel} max={d.xp.forNext} color={C.gold} label={T('Expérience vers le niveau suivant')} /></View>
          <P soft>{T('{0} XP avant le niveau {1}', [d.xp.forNext - d.xp.intoLevel, d.xp.level + 1])}</P>
          <Button tone="quiet" label={T('Mon aventure')} onPress={() => router.push('/progress')} />
        </View>

        <View style={{ gap: 10 }}>
          <H2>{T('Quêtes du jour')}</H2>
          {d.quests.map((q) => (
            <Card key={q.id} style={{ flexDirection: 'row', alignItems: 'center', gap: 12 }}>
              <View style={{ width: 36, height: 36, borderRadius: 18, backgroundColor: q.done ? C.gold : C.surface2, alignItems: 'center', justifyContent: 'center' }}>
                <Text style={{ fontWeight: '900', color: q.done ? '#2a1a00' : C.inkSoft }}>{q.done ? '済' : '・'}</Text>
              </View>
              <View style={{ flex: 1, gap: 6 }}>
                <Text style={{ fontWeight: '700', color: C.ink }}>{q.title}</Text>
                <View style={{ flexDirection: 'row', alignItems: 'center', gap: 8 }}>
                  <ProgressBar value={q.progress} max={q.target} color={q.done ? C.gold : C.ink} label={q.title} />
                  <Text style={{ color: C.inkSoft, fontSize: 12 }}>{q.progress}/{q.target}</Text>
                </View>
              </View>
              <Text style={{ color: C.goldInk, fontWeight: '800' }}>{q.xp} XP</Text>
            </Card>
          ))}
        </View>
      </ScrollView>
    </SafeAreaView>
  );
}
