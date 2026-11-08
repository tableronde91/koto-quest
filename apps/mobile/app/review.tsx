import { useEffect, useState } from 'react';
import { Text, View } from 'react-native';
import { useRouter } from 'expo-router';
import { useQueryClient } from '@tanstack/react-query';
import type { SessionDto } from '@koto/shared';
import { post } from '../src/api';
import { QuizRunner, RunSummary } from '../src/QuizRunner';
import { C } from '../src/theme';
import { Button, ErrorBox, H1, Loading, P, Screen } from '../src/ui';

/** Séance de révision (aussi ouverte en touchant une notification). */
export default function ReviewSession() {
  const router = useRouter();
  const qc = useQueryClient();
  const [session, setSession] = useState<SessionDto | null>(null);
  const [summary, setSummary] = useState<RunSummary | null>(null);
  const [error, setError] = useState<unknown>(null);

  const load = () => {
    setSummary(null);
    setSession(null);
    post<SessionDto>('/reviews/session').then(setSession).catch(setError);
  };
  useEffect(load, []);

  if (error) return <Screen><ErrorBox error={error} /><Button tone="quiet" label="Retour" onPress={() => router.replace('/')} /></Screen>;
  if (!session) return <Loading label="Préparation de ta révision…" />;
  if (summary || session.questions.length === 0)
    return (
      <Screen>
        <View style={{ alignItems: 'center', gap: 10, marginTop: 30 }}>
          <Text style={{ fontSize: 72, fontWeight: '900', color: C.ko }}>{summary ? '復習' : '😺'}</Text>
          <H1>{summary ? 'Révision terminée' : 'Aucune révision due'}</H1>
          {summary && <P>{summary.correct}/{summary.total} bonnes réponses · +{summary.xp} XP</P>}
        </View>
        <Button tone="gold" label="Continuer à réviser" onPress={() => { qc.invalidateQueries(); load(); }} />
        <Button tone="quiet" label="Accueil" onPress={() => { qc.invalidateQueries(); router.replace('/'); }} />
      </Screen>
    );
  return <Screen><QuizRunner questions={session.questions} onQuit={() => router.replace('/')} onFinish={setSummary} /></Screen>;
}
