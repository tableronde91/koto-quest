import { useEffect, useRef, useState } from 'react';
import { Pressable, Text, View } from 'react-native';
import { useLocalSearchParams, useRouter } from 'expo-router';
import { useQueryClient } from '@tanstack/react-query';
import type { ReadingResultDto } from '@koto/shared';
import { stripRuby } from '@koto/learning-engine';
import { post } from '../../src/api';
import { useReadingChapter } from '../../src/hooks';
import { Ruby } from '../../src/Ruby';
import { useStudyLang } from '../../src/study';
import { speak } from '../../src/speech';
import { C } from '../../src/theme';
import { Button, Card, ErrorBox, H2, Loading, P, Screen } from '../../src/ui';
import { T, bi, plural } from '../../src/i18n';

/** Liseuse : furigana à la demande, traduction au toucher, vocabulaire, questions de compréhension. */
export default function ReadingChapterScreen() {
  const { slug } = useLocalSearchParams<{ slug: string }>();
  const router = useRouter();
  const qc = useQueryClient();
  const { data, isLoading, error, refetch } = useReadingChapter(slug);
  const { zh, ko, en, es } = useStudyLang();
  const [furigana, setFurigana] = useState(true);
  const [roman, setRoman] = useState(false);
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
        <Text style={{ fontWeight: '800', color: C.ink }}>{T('← Tous les contes')}</Text>
      </Pressable>
      <Text style={{ color: C.inkSoft, fontWeight: '700' }}>{bi(story.title)} · {T('chapitre {0}/{1}', [chapter.index, chapter.count])} · {story.level}</Text>
      <Ruby text={chapter.title.jp} furigana={furigana} size={26} />
      <Text accessibilityRole="header" style={{ fontSize: 22, fontWeight: '800', color: C.ink }}>{bi(chapter.title)}</Text>

      <View style={{ flexDirection: 'row', gap: 8, flexWrap: 'wrap' }}>
        {!ko && !en && !es && <Button label={zh ? (furigana ? T('Masquer le pinyin') : T('Afficher le pinyin')) : furigana ? T('Masquer les furigana') : T('Afficher les furigana')} tone="quiet" style={{ flex: 1 }} onPress={() => setFurigana(!furigana)} />}
        {chapter.paragraphs.some((p) => p.some((s) => s.roman)) && (
          <Button
            testID="roman-toggle"
            label={zh ? (roman ? T('Masquer le pinyin complet') : T('Afficher le pinyin complet')) : ko ? (roman ? T('Masquer la romanisation') : T('Afficher la romanisation')) : roman ? T('Masquer le rōmaji') : T('Afficher le rōmaji')}
            tone="quiet"
            style={{ flex: 1 }}
            onPress={() => setRoman(!roman)}
          />
        )}
      </View>
      <P soft>{T('Touche une phrase pour voir sa traduction et l’écouter.')}</P>

      <Card style={{ gap: 14 }} testID="reader">
        {chapter.paragraphs.map((para, pi) => (
          <View key={pi} style={{ gap: 10 }}>
            {para.map((s, si) => {
              const id = `${pi}-${si}`;
              const on = open === id;
              return (
                <Pressable key={id} accessibilityRole="button" accessibilityLabel={stripRuby(s.jp)} accessibilityState={{ expanded: on }} onPress={() => { setOpen(on ? null : id); if (!on) speak(s.kana); }} style={{ borderRadius: 10, padding: 6, backgroundColor: on ? '#FBEFD9' : 'transparent' }}>
                  <Ruby text={s.jp} furigana={furigana} />
                  {roman && s.roman && <Text style={{ marginTop: 2, color: C.inkSoft, fontSize: 15, fontStyle: 'italic' }}>{s.roman}</Text>}
                  {on && <Text style={{ marginTop: 6, color: C.inkSoft, fontSize: 15 }}>{bi(s)}</Text>}
                </Pressable>
              );
            })}
          </View>
        ))}
      </Card>

      <H2>{T('Vocabulaire')}</H2>
      <Card style={{ gap: 8 }}>
        {chapter.words.map((w) => (
          <View key={w.jp} style={{ flexDirection: 'row', gap: 10, flexWrap: 'wrap' }}>
            <Text style={{ fontWeight: '800', color: C.ink, fontSize: 16 }}>{w.jp}</Text>
            {w.reading && <Text style={{ color: C.inkSoft }}>{w.reading}</Text>}
            <Text style={{ color: C.ink, flexShrink: 1 }}>{bi(w)}</Text>
          </View>
        ))}
      </Card>

      <H2>{T('Compréhension')}</H2>
      {chapter.questions.map((q, qi) => (
        <Card key={qi} style={{ gap: 8 }}>
          <P style={{ fontWeight: '800' }}>{qi + 1}. {bi(q.q)}</P>
          {q.choices.map((c, ci) => {
            const picked = (shown ? shown.answers[qi] : answers[qi]) === ci && !shown;
            const good = shown && shown.answers[qi] === ci;
            const mine = !shown && answers[qi] === ci;
            return (
              <Pressable key={ci} accessibilityRole="radio" accessibilityState={{ checked: mine, disabled: !!shown }} disabled={!!shown} onPress={() => setAnswers((a) => { const n = [...a]; n[qi] = ci; return n; })} style={{ minHeight: 44, justifyContent: 'center', paddingHorizontal: 12, borderRadius: 12, borderWidth: 2, borderColor: good ? C.ok : mine || picked ? C.ink : C.line, backgroundColor: good ? C.okBg : mine ? C.surface2 : C.surface }}>
                <Text style={{ color: C.ink, fontWeight: mine || good ? '800' : '500' }}>{bi(c)}</Text>
              </Pressable>
            );
          })}
        </Card>
      ))}

      {!shown && (
        <Button label={T('Valider mes réponses')} tone="gold" disabled={sending || chapter.questions.some((_, i) => answers[i] === undefined)} onPress={submit} />
      )}
      {shown && (
        <Card style={{ gap: 10, borderColor: C.ok }}>
          <Text accessibilityRole="header" style={{ fontSize: 20, fontWeight: '800', color: C.ink }}>{T('{0}/{1} bonnes réponses', [shown.correct, shown.total])}</Text>
          {result?.firstTime && <P>{T('+{0} XP · +{1} pièces', [result.xpGained, result.coinsGained])} · {plural(result.streak, 'série de {0} jour', 'série de {0} jours')}</P>}
          {!result && <P soft>{T('Chapitre déjà lu : les bonnes réponses sont surlignées.')}</P>}
          {data.next && <Button label={T('Chapitre suivant')} tone="gold" onPress={() => router.replace(`/reading/${data.next!.slug}`)} />}
          <Button label={T('Tous les contes')} tone="quiet" onPress={() => router.back()} />
        </Card>
      )}
    </Screen>
  );
}
