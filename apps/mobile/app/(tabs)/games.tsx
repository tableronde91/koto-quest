import { Text, View } from 'react-native';
import { useRouter } from 'expo-router';
import { GAME_GLYPH, KIND_HINT } from '../../src/games';
import { useGames } from '../../src/hooks';
import { C } from '../../src/theme';
import { Button, Card, ErrorBox, H1, H2, Loading, P, Screen } from '../../src/ui';
import { T, plural } from '../../src/i18n';


/** Mini-jeux : une minute chrono sur les notions déjà rencontrées, sans toucher aux révisions. */
export default function GamesScreen() {
  const router = useRouter();
  const { data, isLoading, error, refetch } = useGames();
  if (isLoading) return <Loading />;
  if (error || !data) return <Screen><ErrorBox error={error} onRetry={refetch} /></Screen>;
  return (
    <Screen>
      <H1>{T('Jeux')}</H1>
      <Card style={{ gap: 10, backgroundColor: '#2A2858', borderColor: '#2A2858' }} testID="duel-card">
        <View style={{ flexDirection: 'row', alignItems: 'center', gap: 12 }}>
          <View style={{ width: 56, height: 56, borderRadius: 16, backgroundColor: C.ko, alignItems: 'center', justifyContent: 'center' }}>
            <Text style={{ fontSize: 30, fontWeight: '900', color: '#fff' }}>闘</Text>
          </View>
          <View style={{ flex: 1 }}>
            <Text accessibilityRole="header" style={{ fontSize: 19, fontWeight: '800', color: '#fff' }}>{T('Duels')}</Text>
            <Text style={{ color: '#ffffffcc', fontSize: 13 }}>{T('Classé, entre amis ou contre un rōnin')}</Text>
          </View>
        </View>
        <Text style={{ color: '#ffffffdd', fontSize: 15, lineHeight: 21 }}>{T('Même question, même chrono : le plus rapide frappe le plus fort.')}</Text>
        <Button label={T('Entrer dans le dojo')} tone="gold" onPress={() => router.push('/duel')} />
      </Card>
      <H2>{T('Mini-jeux')}</H2>
      <P soft>{T('Une minute chrono sur les notions que tu as déjà rencontrées. Les mini-jeux entraînent tes réflexes sans modifier tes révisions.')}</P>
      {data.games.map((g) => (
        <Card key={g.id} style={{ gap: 10 }} testID="game-card">
          <View style={{ flexDirection: 'row', alignItems: 'center', gap: 12 }}>
            <View style={{ width: 56, height: 56, borderRadius: 16, backgroundColor: g.available ? C.ink : C.surface2, alignItems: 'center', justifyContent: 'center' }}>
              <Text style={{ fontSize: 30, fontWeight: '900', color: g.available ? C.paper : C.inkSoft }}>{GAME_GLYPH[g.id]}</Text>
            </View>
            <View style={{ flex: 1 }}>
              <Text accessibilityRole="header" style={{ fontSize: 19, fontWeight: '800', color: C.ink }}>{g.title}</Text>
              <Text style={{ color: C.inkSoft, fontSize: 13 }}>{g.plays > 0 ? plural(g.plays, 'Record : {0}, {1} partie', 'Record : {0}, {1} parties', [g.bestScore, g.plays]) : T('Jamais joué')}</Text>
            </View>
          </View>
          <P soft>{g.description}</P>
          {g.available ? (
            <Button label={T('Jouer à {0}', [g.title])} tone="gold" onPress={() => router.push(`/games/${g.id}`)} />
          ) : (
            <View style={{ backgroundColor: C.surface2, borderRadius: 14, padding: 12 }}>
              <P>{T('Débloqué après avoir rencontré {0} {1} ({2}/{0}). Continue tes leçons.', [g.minItems, T(KIND_HINT[g.id]), g.seenItems])}</P>
            </View>
          )}
        </Card>
      ))}
      <P soft>{T('Une pièce toutes les 5 bonnes réponses, dans la limite de 15 par jour.')} {plural(data.coinsLeftToday, 'Encore aujourd’hui : {0} pièce.', 'Encore aujourd’hui : {0} pièces.')}</P>
    </Screen>
  );
}
