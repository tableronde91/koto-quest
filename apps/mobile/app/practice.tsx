import { useEffect, useState } from 'react';
import { Text, View } from 'react-native';
import { useLocalSearchParams, useRouter } from 'expo-router';
import { useQueryClient } from '@tanstack/react-query';
import type { SessionDto } from '@koto/shared';
import { post } from '../src/api';
import { QuizRunner, RunSummary } from '../src/QuizRunner';
import { C } from '../src/theme';
import { Button, ErrorBox, H1, Loading, P, Screen } from '../src/ui';
import { T } from '../src/i18n';

/** Séance de pratique d'un ensemble de caractères (hiragana, groupe « ka »…) ou d'un thème d'expressions. */
export default function Practice() {
  const { kind = 'characters', scope = 'hiragana' } = useLocalSearchParams<{ kind: 'characters' | 'expressions'; scope: string }>();
  const router = useRouter();
  const qc = useQueryClient();
  const [session, setSession] = useState<SessionDto | null>(null);
  const [summary, setSummary] = useState<RunSummary | null>(null);
  const [error, setError] = useState<unknown>(null);

  const start = () => {
    setSummary(null);
    setSession(null);
    setError(null);
    const req = kind === 'expressions' ? post<SessionDto>('/expressions/practice', { theme: scope }) : post<SessionDto>('/characters/practice', { scope });
    req.then(setSession).catch(setError);
  };
  useEffect(start, [kind, scope]);

  const leave = () => {
    void qc.invalidateQueries();
    if (router.canGoBack()) router.back();
    else router.replace('/kana');
  };
  const backLabel = kind === 'expressions' ? T('Retour aux expressions') : T('Retour aux caractères');

  if (error) return <Screen><ErrorBox error={error} onRetry={start} /><Button tone="quiet" label={backLabel} onPress={leave} /></Screen>;
  if (!session) return <Loading label={T('Préparation de la séance…')} />;
  if (summary || session.questions.length === 0)
    return (
      <Screen>
        <View style={{ alignItems: 'center', gap: 10, marginTop: 30 }}>
          <Text style={{ fontSize: 72, fontWeight: '900', color: C.ko }}>{summary ? '練習' : '空'}</Text>
          <H1>{summary ? T('Séance terminée') : T('Rien à pratiquer ici')}</H1>
          {summary && <P>{T('{0}/{1} bonnes réponses · +{2} XP', [summary.correct, summary.total, summary.xp])}</P>}
        </View>
        {summary && <Button tone="gold" label={T('Encore une séance')} onPress={() => { void qc.invalidateQueries(); start(); }} />}
        <Button tone="quiet" label={backLabel} onPress={leave} />
      </Screen>
    );
  return <Screen><QuizRunner questions={session.questions} onQuit={leave} onFinish={(s) => { setSummary(s); void qc.invalidateQueries(); }} /></Screen>;
}
