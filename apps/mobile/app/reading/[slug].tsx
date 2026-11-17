import { useEffect, useRef, useState } from 'react';
import { Pressable, Text, View } from 'react-native';
import { useLocalSearchParams, useRouter } from 'expo-router';
import { useQueryClient } from '@tanstack/react-query';
import type { ReadingResultDto } from '@koto/shared';
import { stripRuby } from '@koto/learning-engine';
import { post } from '../../src/api';
import { useReadingChapter } from '../../src/hooks';
import { Ruby } from '../../src/Ruby';
import { speak } from '../../src/speech';
import { C } from '../../src/theme';
import { Button, Card, ErrorBox, H2, Loading, P, Screen } from '../../src/ui';

/** Liseuse : furigana à la demande, traduction au toucher, vocabulaire, questions de compréhension. */
export default function ReadingChapterScreen() {
  const { slug } = useLocalSearchParams<{ slug: string }>();
  const router = useRouter();
  const qc = useQueryClient();
  const { data, isLoading, error, refetch } = useReadingChapter(slug);
  const [furigana, setFurigana] = useState(true);
  const [open, setOpen] = useState<string | null>(null);
  const [answers, setAnswers] = useState<number[]>([]);
  const [result, setResult] = useState<ReadingResultDto | null>(null);
  const [sending, setSending] = useState(false);
  const started = useRef(Date.now());
  useEffect(() => {
    setAnswers([]);
    setResult(null);
    setOpen(null);
    started.current = Date.now();
  }, [slug]);

  if (isLoading) return <Loading />;
  if (error || !data) return <Screen><ErrorBox error={error} onRetry={refetch} /></Screen>;
  const { chapter, story } = data;
  const shown = result ?? (data.result ? { ...data.result, firstTime: false } : null);

  const submit = async () => {
    setSending(true);
    try {
      const r = await post<ReadingResultDto>(`/reading/chapters/${chapter.slug}/complete`, { answers, seconds: Math.round((Date.now() - started.current) / 1000) });
      setResult(r);
      qc.invalidateQueries({ queryKey: ['reading'] });
      qc.invalidateQueries({ queryKey: ['dashboard'] });
    } finally {
      setSending(false);
    }
  };

  return (
    <Screen>
      <Pressable accessibilityRole="link" onPress={() => router.back()} style={{ minHeight: 44, justifyContent: 'center' }}>
        <Text style={{ fontWeight: '800', color: C.ink }}>← Tous les contes</Text>
      </Pressable>
      <Text style={{ color: C.inkSoft, fontWeight: '700' }}>{story.title.fr} · chapitre {chapter.index}/{chapter.count} · {story.level}</Text>
      <Ruby text={chapter.title.jp} furigana={furigana} size={26} />
      <Text accessibilityRole="header" style={{ fontSize: 22, fontWeight: '800', color: C.ink }}>{chapter.title.fr}</Text>

      <View style={{ flexDirection: 'row', gap: 8 }}>
        <Button label={furigana ? 'Masquer les furigana' : 'Afficher les furigana'} tone="quiet" style={{ flex: 1 }} onPress={() => setFurigana(!furigana)} />
      </View>
      <P soft>Touche une phrase pour voir sa traduction et l’écouter.</P>

      <Card style={{ gap: 14 }} testID="reader">
        {chapter.paragraphs.map((para, pi) => (
          <View key={pi} style={{ gap: 10 }}>
            {para.map((s, si) => {
              const id = `${pi}-${si}`;
              const on = open === id;
              return (
                <Pressable key={id} accessibilityRole="button" accessibilityLabel={stripRuby(s.jp)} accessibilityState={{ expanded: on }} onPress={() => { setOpen(on ? null : id); if (!on) speak(s.kana); }} style={{ borderRadius: 10, padding: 6, backgroundColor: on ? '#FBEFD9' : 'transparent' }}>
                  <Ruby text={s.jp} furigana={furigana} />
                  {on && <Text style={{ marginTop: 6, color: C.inkSoft, fontSize: 15 }}>{s.fr}</Text>}
                </Pressable>
              );
            })}
          </View>
        ))}
      </Card>

      <H2>Vocabulaire</H2>
      <Card style={{ gap: 8 }}>
        {chapter.words.map((w) => (
          <View key={w.jp} style={{ flexDirection: 'row', gap: 10, flexWrap: 'wrap' }}>
            <Text style={{ fontWeight: '800', color: C.ink, fontSize: 16 }}>{w.jp}</Text>
            {w.reading && <Text style={{ color: C.inkSoft }}>{w.reading}</Text>}
            <Text style={{ color: C.ink, flexShrink: 1 }}>{w.fr}</Text>
          </View>
        ))}
      </Card>

      <H2>Compréhension</H2>
      {chapter.questions.map((q, qi) => (
        <Card key={qi} style={{ gap: 8 }}>
          <P style={{ fontWeight: '800' }}>{qi + 1}. {q.q.fr}</P>
          {q.choices.map((c, ci) => {
            const picked = (shown ? shown.answers[qi] : answers[qi]) === ci && !shown;
            const good = shown && shown.answers[qi] === ci;
            const mine = !shown && answers[qi] === ci;
            return (
              <Pressable key={ci} accessibilityRole="radio" accessibilityState={{ checked: mine, disabled: !!shown }} disabled={!!shown} onPress={() => setAnswers((a) => { const n = [...a]; n[qi] = ci; return n; })} style={{ minHeight: 44, justifyContent: 'center', paddingHorizontal: 12, borderRadius: 12, borderWidth: 2, borderColor: good ? C.ok : mine || picked ? C.ink : C.line, backgroundColor: good ? C.okBg : mine ? C.surface2 : C.surface }}>
                <Text style={{ color: C.ink, fontWeight: mine || good ? '800' : '500' }}>{c.fr}</Text>
              </Pressable>
            );
          })}
        </Card>
      ))}

      {!shown && (
        <Button label="Valider mes réponses" tone="gold" disabled={sending || chapter.questions.some((_, i) => answers[i] === undefined)} onPress={submit} />
      )}
      {shown && (
        <Card style={{ gap: 10, borderColor: C.ok }}>
          <Text accessibilityRole="header" style={{ fontSize: 20, fontWeight: '800', color: C.ink }}>{shown.correct}/{shown.total} bonnes réponses</Text>
          {result?.firstTime && <P>+{result.xpGained} XP · +{result.coinsGained} pièces · série de {result.streak} jour{result.streak > 1 ? 's' : ''}</P>}
          {!result && <P soft>Chapitre déjà lu : les bonnes réponses sont surlignées.</P>}
          {data.next && <Button label="Chapitre suivant" tone="gold" onPress={() => router.replace(`/reading/${data.next!.slug}`)} />}
          <Button label="Tous les contes" tone="quiet" onPress={() => router.back()} />
        </Card>
      )}
    </Screen>
  );
}
