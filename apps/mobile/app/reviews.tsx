import { Text, View } from 'react-native';
import { useRouter } from 'expo-router';
import { useReviewSummary } from '../src/hooks';
import { C } from '../src/theme';
import { Button, Card, ErrorBox, TitleBar, H1, Loading, P, Screen } from '../src/ui';
import { T, plural } from '../src/i18n';

export default function Reviews() {
  const router = useRouter();
  const { data, isLoading, error, refetch } = useReviewSummary();
  if (isLoading) return <Loading />;
  if (error || !data) return <Screen><ErrorBox error={error} onRetry={refetch} /></Screen>;
  return (
    <Screen>
      <TitleBar title={T('Révisions')} fallback="/learn" />
      <P soft>{T('Chaque notion revient au moment où tu risques de l’oublier. Les intervalles s’allongent quand tu réussis.')}</P>
      {data.due > 0 ? (
        <View style={{ backgroundColor: C.ink, borderRadius: 24, padding: 20, gap: 10 }}>
          <Text style={{ color: C.paper, fontSize: 48, fontWeight: '900' }}>{data.due}</Text>
          <Text style={{ color: C.paper, opacity: 0.85 }}>{plural(data.due, 'notion à réviser maintenant', 'notions à réviser maintenant', [])}{data.due > 20 ? T(' (par séries de 20)') : ''}</Text>
          <Button tone="gold" label={T('Lancer la révision')} onPress={() => router.push('/review')} />
        </View>
      ) : (
        <Card style={{ alignItems: 'center', gap: 8, borderStyle: 'dashed', borderWidth: 2 }}>
          <Text style={{ fontSize: 56 }}>😺💤</Text>
          <Text style={{ fontSize: 18, fontWeight: '800', color: C.ink }}>{T('Rien à réviser pour l’instant.')}</Text>
          <P soft style={{ textAlign: 'center' }}>{data.learningSoon > 0 ? T('{0} notion(s) reviendront dans l’heure.', [data.learningSoon]) : T('Apprends une nouvelle leçon pour alimenter tes prochaines révisions.')}</P>
          <Button tone="quiet" label={T('Voir le parcours')} onPress={() => router.push('/path')} />
        </Card>
      )}
    </Screen>
  );
}
