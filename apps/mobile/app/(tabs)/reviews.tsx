import { Text, View } from 'react-native';
import { useRouter } from 'expo-router';
import { useReviewSummary } from '../../src/hooks';
import { C } from '../../src/theme';
import { Button, Card, ErrorBox, H1, Loading, P, Screen } from '../../src/ui';

export default function Reviews() {
  const router = useRouter();
  const { data, isLoading, error, refetch } = useReviewSummary();
  if (isLoading) return <Loading />;
  if (error || !data) return <Screen><ErrorBox error={error} onRetry={refetch} /></Screen>;
  return (
    <Screen>
      <H1>Révisions</H1>
      <P soft>Chaque notion revient au moment où tu risques de l’oublier. Les intervalles s’allongent quand tu réussis.</P>
      {data.due > 0 ? (
        <View style={{ backgroundColor: C.ink, borderRadius: 24, padding: 20, gap: 10 }}>
          <Text style={{ color: C.paper, fontSize: 48, fontWeight: '900' }}>{data.due}</Text>
          <Text style={{ color: C.paper, opacity: 0.85 }}>notion{data.due > 1 ? 's' : ''} à réviser maintenant{data.due > 20 ? ' (par séries de 20)' : ''}</Text>
          <Button tone="gold" label="Lancer la révision" onPress={() => router.push('/review')} />
        </View>
      ) : (
        <Card style={{ alignItems: 'center', gap: 8, borderStyle: 'dashed', borderWidth: 2 }}>
          <Text style={{ fontSize: 56 }}>😺💤</Text>
          <Text style={{ fontSize: 18, fontWeight: '800', color: C.ink }}>Rien à réviser pour l’instant.</Text>
          <P soft style={{ textAlign: 'center' }}>{data.learningSoon > 0 ? `${data.learningSoon} notion(s) reviendront dans l’heure.` : 'Apprends une nouvelle leçon pour alimenter tes prochaines révisions.'}</P>
          <Button tone="quiet" label="Voir le parcours" onPress={() => router.push('/path')} />
        </Card>
      )}
    </Screen>
  );
}
