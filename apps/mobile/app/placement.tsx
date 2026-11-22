import { useState } from 'react';
import { Text, View } from 'react-native';
import { useStudyLang } from '../src/study';
import { useRouter } from 'expo-router';
import { useQueryClient } from '@tanstack/react-query';
import type { PlacementStepDto } from '@koto/shared';
import { post } from '../src/api';
import { ExamAnswer, ExamQuestion } from '../src/ExamQuestion';
import { C } from '../src/theme';
import { Button, ErrorBox, H1, P, ProgressBar, Screen, TitleBar } from '../src/ui';
import { T } from '../src/i18n';

/** Test de positionnement : trois questions par monde, on valide les mondes déjà maîtrisés. */
export default function Placement() {
  const w = useStudyLang();
  const router = useRouter();
  const qc = useQueryClient();
  const [step, setStep] = useState<PlacementStepDto | null>(null);
  const [answers, setAnswers] = useState<Record<string, ExamAnswer>>({});
  const [validatedSoFar, setValidatedSoFar] = useState<string[]>([]);
  const [error, setError] = useState<unknown>(null);
  const [busy, setBusy] = useState(false);

  async function start() {
    setError(null);
    try {
      setStep(await post<PlacementStepDto>('/placement/start'));
      setValidatedSoFar([]);
    } catch (e) {
      setError(e);
    }
  }

  async function submit(a: Record<string, ExamAnswer>) {
    if (!step || step.done || busy) return;
    setBusy(true);
    setError(null);
    try {
      const next = await post<PlacementStepDto>('/placement/answer', { sessionId: step.block.sessionId, answers: a });
      if (!next.done && next.lastPassed) setValidatedSoFar([...validatedSoFar, step.block.world.title]);
      setStep(next);
      setAnswers({});
      if (next.done) void qc.invalidateQueries();
    } catch (e) {
      setError(e);
    } finally {
      setBusy(false);
    }
  }

  if (!step)
    return (
      <Screen>
        <TitleBar title={T('Test de niveau')} fallback="/learn" />
        <View style={{ alignItems: 'center', gap: 12 }}>
          <Text style={{ fontSize: 64, fontWeight: '900', color: C.ko }}>{w.pick('診断', '진단', 'Test')}</Text>
          <P style={{ textAlign: 'center' }}>{w.en ? T('Tu connais déjà un peu d’anglais ? Trois questions par monde, dans l’ordre du parcours : chaque monde réussi (2 bonnes réponses sur 3) est validé, et le test s’arrête au premier monde à travailler.') : w.ko ? T('Tu connais déjà un peu de coréen ? Trois questions par monde, dans l’ordre du parcours : chaque monde réussi (2 bonnes réponses sur 3) est validé, et le test s’arrête au premier monde à travailler.') : T('Tu connais déjà un peu de japonais ? Trois questions par monde, dans l’ordre du parcours : chaque monde réussi (2 bonnes réponses sur 3) est validé, et le test s’arrête au premier monde à travailler.')}</P>
          <P soft style={{ textAlign: 'center', fontSize: 14 }}>{T('Réponds sans deviner : « Je ne sais pas » vaut mieux qu’un coup de chance. Les mondes validés reviendront en révision pour vérifier qu’ils sont bien acquis.')}</P>
        </View>
        {error != null && <ErrorBox error={error} />}
        <Button tone="gold" label={T('Commencer le test')} onPress={start} />
      </Screen>
    );

  if (step.done)
    return (
      <Screen>
        <View style={{ alignItems: 'center', gap: 10, marginTop: 30 }}>
          <Text style={{ fontSize: 64, fontWeight: '900', color: C.ko }}>{w.pick('完了', '완료', 'Done!')}</Text>
          <H1 style={{ textAlign: 'center' }}>{step.validated.length ? T('{0} monde(s) validé(s)', [step.validated.length]) : T('On commence au début')}</H1>
          {step.validated.map((w) => <Text key={w.slug} style={{ fontWeight: '800', color: C.ok }}>✓ {w.title}</Text>)}
          {step.stoppedAt && <P style={{ textAlign: 'center' }}>{T('Ton parcours reprend au monde « {0} ».', [step.stoppedAt.title])}</P>}
        </View>
        {step.nextLesson && <Button tone="gold" label={T('Commencer : {0}', [step.nextLesson.title])} onPress={() => router.replace(`/lesson/${step.nextLesson!.slug}`)} />}
        <Button tone="quiet" label={T('Voir le parcours')} onPress={() => router.replace('/path')} />
      </Screen>
    );

  const b = step.block;
  const complete = b.questions.every((q) => answers[q.id] !== undefined);
  return (
    <Screen>
      <View style={{ gap: 6 }}>
        <View style={{ flexDirection: 'row' }}><ProgressBar value={b.index} max={b.totalWorlds} color={C.gold} label={T('Monde {0} sur {1}', [b.index + 1, b.totalWorlds])} /></View>
        <P soft style={{ fontSize: 13 }}>{T('Monde {0} sur {1}', [b.world.order, b.totalWorlds])}{validatedSoFar.length ? T(', déjà validés : {0}', [validatedSoFar.join(', ')]) : ''}</P>
        <H1>{b.world.title}</H1>
      </View>
      {b.questions.map((q, i) => <ExamQuestion key={q.id} q={q} number={i + 1} value={answers[q.id]} onChange={(v) => setAnswers({ ...answers, [q.id]: v })} />)}
      {error != null && <ErrorBox error={error} />}
      <Button tone="gold" label={T('Valider ces réponses')} disabled={!complete || busy} onPress={() => submit(answers)} />
      <Button tone="quiet" label={T('Je ne sais pas')} disabled={busy} onPress={() => submit(answers)} />
    </Screen>
  );
}
