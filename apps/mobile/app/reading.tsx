import { Pressable, Text, View } from 'react-native';
import { useRouter } from 'expo-router';
import { useReading } from '../src/hooks';
import { Ruby } from '../src/Ruby';
import { C } from '../src/theme';
import { Button, Card, ErrorBox, TitleBar, H1, H2, Loading, P, Screen, Seal } from '../src/ui';
import { T, bi } from '../src/i18n';
import { useStudyLang } from '../src/study';

/** Lecture : contes de la langue étudiée (japonais ou coréen), tous ouverts ; un chapitre conseillé chaque jour. */
export default function ReadingScreen() {
  const router = useRouter();
  const w = useStudyLang();
  const { data, isLoading, error, refetch } = useReading();
  if (isLoading) return <Loading />;
  if (error || !data) return <Screen><ErrorBox error={error} onRetry={refetch} /></Screen>;
  const { today, upcoming } = data;
  const suggested = today.state === 'new' ? today.chapter?.slug : upcoming?.slug;
  return (
    <Screen>
      <TitleBar title={T('Lecture')} fallback="/learn" />
      <P soft>{w.es ? T('Des contes et légendes en espagnol à lire à ton rythme : tous les chapitres sont ouverts. Lire un peu chaque jour aide beaucoup à progresser.') : w.en ? T('Des contes et légendes en anglais à lire à ton rythme : tous les chapitres sont ouverts. Lire un peu chaque jour aide beaucoup à progresser.') : w.zh ? T('Des contes chinois à lire à ton rythme : tous les chapitres sont ouverts. Lire un peu chaque jour aide beaucoup à progresser.') : w.ko ? T('Des contes coréens à lire à ton rythme : tous les chapitres sont ouverts. Lire un peu chaque jour aide beaucoup à progresser.') : T('Des contes japonais à lire à ton rythme : tous les chapitres sont ouverts. Lire un peu chaque jour aide beaucoup à progresser.')}</P>

      {today.chapter && today.story && (
        <Card style={{ gap: 10, backgroundColor: C.ink, borderColor: C.ink }}>
          <Text style={{ color: C.gold, fontWeight: '800' }}>{today.state === 'new' ? T('Conseillé aujourd’hui') : T('Lu aujourd’hui')}</Text>
          <Ruby text={today.chapter.title.jp} furigana size={22} color={C.paper} />
          <Text style={{ color: C.paper, fontSize: 18, fontWeight: '800' }}>{bi(today.chapter.title)}</Text>
          <Text style={{ color: C.paper, opacity: 0.8 }}>{bi(today.story.title)} · {T('{0} phrases', [today.chapter.sentences])}</Text>
          {today.state === 'done' && upcoming && <Text style={{ color: C.paper }}>{T('Bravo ! Envie de continuer ? La suite, « {0} », t’attend.', [bi(upcoming.title)])}</Text>}
          {today.state === 'done' && upcoming && <Button label={T('Continuer la lecture')} tone="gold" onPress={() => router.push(`/reading/${upcoming.slug}`)} />}
          <Button label={today.state === 'new' ? T('Lire le chapitre du jour') : T('Relire')} tone={today.state === 'new' ? 'gold' : 'quiet'} style={today.state === 'new' ? undefined : { borderColor: C.paper }} onPress={() => router.push(`/reading/${today.chapter!.slug}`)} />
        </Card>
      )}

      <View style={{ flexDirection: 'row', gap: 10 }}>
        {[
          [String(data.streak), T('jours de suite')],
          [`${data.chaptersRead}/${data.totalChapters}`, T('chapitres lus')],
          [String(data.charsRead), T('caractères lus')],
        ].map(([v, l]) => (
          <Card key={l} style={{ flex: 1, padding: 10, alignItems: 'center' }}>
            <Text style={{ fontSize: 20, fontWeight: '900', color: C.ink }}>{v}</Text>
            <Text style={{ fontSize: 12, color: C.inkSoft, textAlign: 'center' }}>{l}</Text>
          </Card>
        ))}
      </View>

      <H2>{T('Tous les contes')}</H2>
      {data.stories.map((s) => (
        <Card key={s.slug} style={{ gap: 8, borderLeftWidth: 6, borderLeftColor: s.color }} testID="story">
          <View style={{ flexDirection: 'row', alignItems: 'center', gap: 10 }}>
            <Seal glyph={s.glyph} size={40} color={s.color} />
            <View style={{ flex: 1 }}>
              <Text accessibilityRole="header" style={{ fontSize: 17, fontWeight: '800', color: C.ink }}>{bi(s.title)}</Text>
              <Text style={{ color: C.inkSoft, fontSize: 12 }}>{s.level} · {T('{0}/{1} chapitres lus', [s.read, s.chapters.length])}</Text>
            </View>
          </View>
          <P soft>{bi(s.summary)}</P>
          {s.chapters.map((c, i) => {
            const on = c.slug === suggested;
            return (
              <Pressable key={c.slug} accessibilityRole="link" accessibilityLabel={T('Chapitre {0} : {1}', [i + 1, bi(c.title)]) + (on ? T(' (conseillé)') : '')} onPress={() => router.push(`/reading/${c.slug}`)} style={{ flexDirection: 'row', alignItems: 'center', gap: 10, minHeight: 44, paddingHorizontal: 10, borderRadius: 12, borderWidth: 2, borderColor: on ? C.gold : C.line, backgroundColor: on ? '#FBEFD9' : 'transparent' }}>
                <Text style={{ fontWeight: '900', color: c.state === 'read' ? C.ok : C.ink }}>{c.state === 'read' ? '✓' : '●'}</Text>
                <Text style={{ flex: 1, color: C.ink, fontWeight: on ? '800' : '500' }}>{i + 1}. {bi(c.title)}</Text>
                <Text style={{ color: C.inkSoft, fontSize: 12 }}>{T('{0} phr.', [c.sentences])}</Text>
              </Pressable>
            );
          })}
        </Card>
      ))}
    </Screen>
  );
}
