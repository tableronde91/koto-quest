import { useState } from 'react';
import { Text, View } from 'react-native';
import { useRouter } from 'expo-router';
import { useQuery, useQueryClient } from '@tanstack/react-query';
import type { JlptDrillsDto, SessionDto } from '@koto/shared';
import { api, post } from '../src/api';
import { useAuth } from '../src/auth';
import { QuizRunner, RunSummary } from '../src/QuizRunner';
import { C } from '../src/theme';
import { Button, Card, ErrorBox, H1, H2, Loading, P, Screen, TitleBar } from '../src/ui';
import { T } from '../src/i18n';

const GLYPH: Record<JlptDrillsDto['drills'][number]['part'], string> = { kanji: '読', writing: '書', grammar: '文', star: '★', listening: '聴' };
import { MOCK_EXAM } from '../src/exams';
import { useStudyLang } from '../src/study';
import { examLevelLabel } from '@koto/shared';

/** Atelier JLPT : chaque épreuve au format de l'examen, avec seulement ce qu'on a déjà appris. */
export default function Prepa() {
  const router = useRouter();
  const qc = useQueryClient();
  const { me } = useAuth();
  const w = useStudyLang();
  const { data, isLoading, error, refetch } = useQuery({ queryKey: ['jlpt-drills'], queryFn: () => api<JlptDrillsDto>('/jlpt/drills') });
  const [run, setRun] = useState<{ part: string; title: string; session: SessionDto } | null>(null);
  const [summary, setSummary] = useState<{ part: string; title: string; s: RunSummary } | null>(null);
  const [startError, setStartError] = useState<unknown>(null);

  async function start(part: string, title: string) {
    setStartError(null);
    setSummary(null);
    try {
      setRun({ part, title, session: await post<SessionDto>(`/jlpt/drills/${part}`) });
    } catch (e) {
      setStartError(e);
    }
  }

  if (run)
    return (
      <Screen>
        <QuizRunner key={run.session.sessionId} questions={run.session.questions} onQuit={() => setRun(null)} onFinish={(s) => { setSummary({ part: run.part, title: run.title, s }); setRun(null); void qc.invalidateQueries(); }} />
      </Screen>
    );

  if (summary) {
    const pct = summary.s.total ? Math.round((summary.s.correct / summary.s.total) * 100) : 0;
    return (
      <Screen>
        <View style={{ alignItems: 'center', gap: 10, marginTop: 30 }}>
          <Text style={{ fontSize: 64, fontWeight: '900', color: C.ko }}>{w.ko ? (pct >= 80 ? '합격' : '연습') : pct >= 80 ? '合格' : '練習'}</Text>
          <H1 style={{ textAlign: 'center' }}>{T('{0} : {1} %', [summary.title, pct])}</H1>
          <P style={{ textAlign: 'center' }}>{T('{0}/{1} bonnes réponses · +{2} XP', [summary.s.correct, summary.s.total, summary.s.xp])}</P>
          <P soft style={{ textAlign: 'center' }}>{pct >= 80 ? T('Niveau examen atteint sur cette épreuve. Varie avec les autres épreuves.') : T('Les notions ratées reviendront dans tes révisions. Une autre série pour consolider ?')}</P>
        </View>
        <Button tone="gold" label={T('Nouvelle série')} onPress={() => start(summary.part, summary.title)} />
        <Button tone="quiet" label={T('Autres épreuves')} onPress={() => setSummary(null)} />
      </Screen>
    );
  }

  if (isLoading) return <Loading />;
  if (error || !data) return <Screen><ErrorBox error={error} onRetry={refetch} /></Screen>;
  const level = me?.preferences.targetLevel ?? 'N5';
  return (
    <Screen>
      <TitleBar title={w.workshop} fallback="/learn" />
      <P soft>{w.ko ? T('Les épreuves du TOPIK, consignes en coréen, avec seulement ce que tu as déjà appris. Correction immédiate, erreurs reprises en fin de série.') : T('Chaque épreuve du JLPT, au format exact de l’examen, avec seulement ce que tu as déjà appris. Correction immédiate, erreurs reprises en fin de série.')}</P>
      {startError != null && <ErrorBox error={startError} />}
      {data.drills.map((d) => {
        const ready = d.available >= data.minQuestions;
        return (
          <Card key={d.part} style={{ gap: 10 }} testID="drill">
            <View style={{ flexDirection: 'row', alignItems: 'center', gap: 12 }}>
              <View style={{ width: 52, height: 52, borderRadius: 16, backgroundColor: C.seal, alignItems: 'center', justifyContent: 'center' }}>
                <Text style={{ color: '#fff', fontSize: 28, fontWeight: '900' }}>{w.ko ? (d.part === 'listening' ? '듣' : '문') : GLYPH[d.part]}</Text>
              </View>
              <View style={{ flex: 1 }}>
                <Text style={{ color: C.inkSoft, fontWeight: '700', fontSize: 12 }}>{d.jpTitle}</Text>
                <H2>{d.title}</H2>
              </View>
            </View>
            <P soft style={{ fontSize: 14 }}>{d.description}</P>
            <Text style={{ fontSize: 13, color: C.inkSoft }}>{ready ? T('{0} questions par série', [Math.min(10, d.available)]) : T('Termine quelques leçons de plus pour débloquer cette épreuve.')}</Text>
            <Button label={T('S’entraîner')} disabled={!ready} onPress={() => start(d.part, d.title)} />
          </Card>
        );
      })}
      <View style={{ backgroundColor: C.ink, borderRadius: 24, padding: 18, gap: 10 }}>
        <Text style={{ color: C.paper, fontSize: 18, fontWeight: '800' }}>{T('Prêt·e pour l’épreuve complète ?')}</Text>
        <Text style={{ color: C.paper, opacity: 0.85 }}>{T('Examen blanc {0} : toutes les épreuves, chronométré, noté comme le vrai.', [examLevelLabel(level)])}</Text>
        <Button tone="gold" label={T('Passer l’examen blanc')} onPress={() => router.push(`/exam/${MOCK_EXAM[level] ?? 'n5-jlpt'}`)} />
      </View>
    </Screen>
  );
}
