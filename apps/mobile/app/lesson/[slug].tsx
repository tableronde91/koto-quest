import { useState } from 'react';
import { Pressable, Text, View } from 'react-native';
import { useLocalSearchParams, useRouter } from 'expo-router';
import { useQuery, useQueryClient } from '@tanstack/react-query';
import type { LessonCompletionDto, LessonDto, SessionDto } from '@koto/shared';
import { api, post } from '../../src/api';
import { QuizRunner, RunSummary } from '../../src/QuizRunner';
import { speak } from '../../src/speech';
import { C } from '../../src/theme';
import { Button, Card, ErrorBox, H1, H2, Loading, P, Screen } from '../../src/ui';

const KIND: Record<string, string> = { kana: 'Kana', vocabulary: 'Vocabulaire', kanji: 'Kanji', grammar: 'Grammaire' };
type Stage = 'intro' | 'quiz' | 'completing' | 'mini' | 'done';

export default function LessonScreen() {
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
  if (error || !lesson) return <Screen><ErrorBox error={error} onRetry={refetch} /><Button tone="quiet" label="Retour" onPress={() => router.back()} /></Screen>;
  if (err) return <Screen><ErrorBox error={err} /><Button tone="quiet" label="Retour au parcours" onPress={() => router.replace('/path')} /></Screen>;

  if (stage === 'quiz' && session) return <Screen><QuizRunner questions={session.questions} onQuit={() => router.back()} onFinish={complete} /></Screen>;
  if (stage === 'completing') return <Loading label="Validation de la leçon…" />;
  if (stage === 'mini' && completion)
    return (
      <Screen>
        <Card style={{ borderColor: C.gold, borderWidth: 2 }}><P><Text style={{ fontWeight: '800' }}>Mini-révision</Text> : quelques questions éclair pour ancrer la leçon.</P></Card>
        <QuizRunner questions={completion.miniReview} onFinish={(s) => { setMini(s); setStage('done'); }} />
      </Screen>
    );
  if (stage === 'done' && completion)
    return (
      <Screen>
        <View style={{ alignItems: 'center', gap: 10, marginTop: 30 }}>
          <Text style={{ fontSize: 80, fontWeight: '900', color: C.ko }}>{completion.perfect ? '満点' : '完了'}</Text>
          <H1>{completion.perfect ? 'Sans faute !' : 'Leçon terminée'}</H1>
          <P style={{ textAlign: 'center' }}>{lesson.title} : {completion.correct}/{completion.total} bonnes réponses ({completion.score} %){mini ? `, mini-révision ${mini.correct}/${mini.total}` : ''}.</P>
          <Text style={{ color: C.goldInk, fontWeight: '800', fontSize: 16, textAlign: 'center' }}>
            {completion.coinsGained > 0 ? `+${completion.coinsGained} pièces, ` : ''}+{completion.xpGained} XP{mini ? `, +${mini.xp} XP de mini-révision` : ''}
          </Text>
          <P soft style={{ textAlign: 'center' }}>Ces notions reviendront dans quelques heures sous forme de défi.</P>
        </View>
        {completion.nextLessonSlug && <Button tone="gold" label="Leçon suivante" onPress={() => router.replace(`/lesson/${completion.nextLessonSlug}`)} />}
        <Button tone="quiet" label="Retour à l’accueil" onPress={() => router.replace('/')} />
      </Screen>
    );

  return (
    <Screen>
      <Pressable onPress={() => router.back()} accessibilityRole="link"><Text style={{ color: C.inkSoft, textDecorationLine: 'underline' }}>← {lesson.world.title}</Text></Pressable>
      <H1>{lesson.title}</H1>
      <P soft>{lesson.objective}</P>
      {lesson.explanation.map((e, i) => <P key={i}>{e}</P>)}
      <H2>Notions</H2>
      <View style={{ gap: 8 }}>
        {lesson.items.map((it) => (
          <Pressable key={it.id} onPress={() => speak(it.reading ?? it.front)} accessibilityLabel={`${it.front}, ${it.meaning}, écouter`}>
            <Card style={{ flexDirection: 'row', alignItems: 'center', gap: 12 }}>
              <Text style={{ fontSize: [...it.front].length <= 2 ? 40 : 24, fontWeight: '800', color: C.ink, minWidth: 56, textAlign: 'center' }}>{it.front}</Text>
              <View style={{ flex: 1 }}>
                {it.reading && it.reading !== it.front && <Text style={{ color: C.inkSoft }}>{it.reading}{it.romaji ? ` · ${it.romaji}` : ''}</Text>}
                <Text style={{ fontWeight: '700', color: C.ink }}>{it.meaning}</Text>
                <Text style={{ color: C.inkSoft, fontSize: 12 }}>{KIND[it.kind]}</Text>
              </View>
              <Text style={{ fontSize: 18 }}>🔊</Text>
            </Card>
          </Pressable>
        ))}
      </View>
      {lesson.examples.length > 0 && <H2>Exemples</H2>}
      {lesson.examples.map((e, i) => (
        <Pressable key={i} onPress={() => speak(e.reading ?? e.jp)}>
          <Card style={{ gap: 2 }}>
            <Text style={{ fontSize: 20, color: C.ink }}>{e.jp} 🔊</Text>
            {e.reading && <Text style={{ color: C.inkSoft }}>{e.reading}</Text>}
            <Text style={{ color: C.ink }}>{e.fr}</Text>
          </Card>
        </Pressable>
      ))}
      <Button tone="gold" label="Passer aux exercices" onPress={start} />
    </Screen>
  );
}
