import { useDecor } from '../../src/study';
import { useState } from 'react';
import { Pressable, Text, View } from 'react-native';
import { useLocalSearchParams, useRouter } from 'expo-router';
import { useQuery, useQueryClient } from '@tanstack/react-query';
import { hasHangul, type LessonCompletionDto, type LessonDto, type SessionDto, spokenForm } from '@koto/shared';
import { api, post } from '../../src/api';
import { QuizRunner, RunSummary } from '../../src/QuizRunner';
import { speak } from '../../src/speech';
import { C } from '../../src/theme';
import { Button, Card, ErrorBox, H1, H2, Loading, P, Screen } from '../../src/ui';
import { T } from '../../src/i18n';

const KIND: Record<string, string> = { kana: 'Kana', vocabulary: 'Vocabulaire', kanji: 'Kanji', grammar: 'Grammaire' }; // traduits à l'affichage
type Stage = 'intro' | 'quiz' | 'completing' | 'mini' | 'done';

export default function LessonScreen() {
  const D = useDecor();
  const { slug = '' } = useLocalSearchParams<{ slug: string }>();
  const router = useRouter();
  const qc = useQueryClient();
  const { data: lesson, isLoading, error, refetch } = useQuery({ queryKey: ['lesson', slug], queryFn: () => api<LessonDto>(`/lessons/${slug}`) });
  const [stage, setStage] = useState<Stage>('intro');
  const [session, setSession] = useState<SessionDto | null>(null);
  const [completion, setCompletion] = useState<LessonCompletionDto | null>(null);
  const [mini, setMini] = useState<RunSummary | null>(null);
  const [err, setErr] = useState<unknown>(null);

  async function start() {
    setErr(null);
    try {
      setSession(await post<SessionDto>(`/lessons/${slug}/start`));
      setStage('quiz');
    } catch (e) {
      setErr(e);
    }
  }

  async function complete() {
    setStage('completing');
    try {
      const c = await post<LessonCompletionDto>(`/lessons/${slug}/complete`, { sessionId: session!.sessionId });
      setCompletion(c);
      setStage(c.miniReview.length ? 'mini' : 'done');
      qc.invalidateQueries();
    } catch (e) {
      setErr(e);
    }
  }

  if (isLoading) return <Loading />;
  if (error || !lesson) return <Screen><ErrorBox error={error} onRetry={refetch} /><Button tone="quiet" label={T('Retour')} onPress={() => router.back()} /></Screen>;
  if (err) return <Screen><ErrorBox error={err} /><Button tone="quiet" label={T('Retour au parcours')} onPress={() => router.replace('/path')} /></Screen>;

  if (stage === 'quiz' && session) return <Screen><QuizRunner questions={session.questions} onQuit={() => router.back()} onFinish={complete} /></Screen>;
  if (stage === 'completing') return <Loading label={T('Validation de la leçon…')} />;
  if (stage === 'mini' && completion)
    return (
      <Screen>
        <Card style={{ borderColor: C.gold, borderWidth: 2 }}><P><Text style={{ fontWeight: '800' }}>{T('Mini-révision')}</Text>{T(' : quelques questions éclair pour ancrer la leçon.')}</P></Card>
        <QuizRunner questions={completion.miniReview} onFinish={(s) => { setMini(s); setStage('done'); }} />
      </Screen>
    );
  if (stage === 'done' && completion)
    return (
      <Screen>
        <View style={{ alignItems: 'center', gap: 10, marginTop: 30 }}>
          <Text style={{ fontSize: 80, fontWeight: '900', color: C.ko }}>{completion.perfect ? D('perfect') : D('done')}</Text>
          <H1>{completion.perfect ? T('Sans faute !') : T('Leçon terminée')}</H1>
          <P style={{ textAlign: 'center' }}>{T('{0} : {1}/{2} bonnes réponses ({3} %)', [lesson.title, completion.correct, completion.total, completion.score])}{mini ? T(', mini-révision {0}/{1}', [mini.correct, mini.total]) : ''}.</P>
          <Text style={{ color: C.goldInk, fontWeight: '800', fontSize: 16, textAlign: 'center' }}>
            {completion.coinsGained > 0 ? T('+{0} pièces', [completion.coinsGained]) + ', ' : ''}+{completion.xpGained} XP{mini ? T(', +{0} XP de mini-révision', [mini.xp]) : ''}
          </Text>
          <P soft style={{ textAlign: 'center' }}>{T('Ces notions reviendront dans quelques heures sous forme de défi.')}</P>
        </View>
        {completion.nextLessonSlug && <Button tone="gold" label={T('Leçon suivante')} onPress={() => router.replace(`/lesson/${completion.nextLessonSlug}`)} />}
        <Button tone="quiet" label={T('Retour à l’accueil')} onPress={() => router.replace('/')} />
      </Screen>
    );

  return (
    <Screen>
      <Pressable onPress={() => router.back()} accessibilityRole="link"><Text style={{ color: C.inkSoft, textDecorationLine: 'underline' }}>← {lesson.world.title}</Text></Pressable>
      <H1>{lesson.title}</H1>
      <P soft>{lesson.objective}</P>
      {lesson.explanation.map((e, i) => <P key={i}>{e}</P>)}
      <H2>{T('Notions')}</H2>
      <View style={{ gap: 8 }}>
        {lesson.items.map((it) => (
          <Pressable key={it.id} onPress={() => speak(spokenForm(it.front, it.reading))} accessibilityLabel={`${it.front}, ${it.meaning}, ${T('écouter')}`}>
            <Card style={{ flexDirection: 'row', alignItems: 'center', gap: 12 }}>
              <Text style={{ fontSize: [...it.front].length <= 2 ? 40 : 24, fontWeight: '800', color: C.ink, minWidth: 56, textAlign: 'center' }}>{it.front}</Text>
              <View style={{ flex: 1 }}>
                {it.reading && it.reading !== it.front && <Text style={{ color: C.inkSoft }}>{it.reading}{it.romaji ? ` · ${it.romaji}` : ''}</Text>}
                <Text style={{ fontWeight: '700', color: C.ink }}>{it.meaning}</Text>
                <Text style={{ color: C.inkSoft, fontSize: 12 }}>{T(it.kind === 'kana' && hasHangul(it.front) ? 'Hangeul' : it.kind === 'kanji' && /[a-zA-Zāáǎàēéěèīíǐìōóǒòūúǔùǖǘǚǜü]/.test(it.reading ?? '') ? 'Hanzi' : KIND[it.kind] ?? it.kind)}</Text>
              </View>
              <Text style={{ fontSize: 18 }}>🔊</Text>
            </Card>
          </Pressable>
        ))}
      </View>
      {lesson.examples.length > 0 && <H2>{T('Exemples')}</H2>}
      {lesson.examples.map((e, i) => (
        <Pressable key={i} onPress={() => speak(spokenForm(e.jp, e.reading))}>
          <Card style={{ gap: 2 }}>
            <Text style={{ fontSize: 20, color: C.ink }}>{e.jp} 🔊</Text>
            {e.reading && <Text style={{ color: C.inkSoft }}>{e.reading}</Text>}
            <Text style={{ color: C.ink }}>{e.fr}</Text>
          </Card>
        </Pressable>
      ))}
      <Button tone="gold" label={T('Passer aux exercices')} onPress={start} />
    </Screen>
  );
}
