import { useCallback, useEffect, useRef, useState } from 'react';
import { Alert, Platform, Pressable, ScrollView, Text, View } from 'react-native';
import { useLocalSearchParams, useRouter } from 'expo-router';
import { useQueryClient } from '@tanstack/react-query';
import type { ExamResultDto, ExamStartDto } from '@koto/shared';
import { post } from '../../src/api';
import { ExamQuestion, type ExamAnswer } from '../../src/ExamQuestion';
import { stopSpeech } from '../../src/speech';
import { C } from '../../src/theme';
import { Button, Card, ErrorBox, H1, H2, Loading, P, ProgressBar, Screen } from '../../src/ui';

type Answers = Record<string, ExamAnswer>;

/** Examen blanc chronométré : copie corrigée par le serveur à la fin, résultat par compétence. */
export default function ExamScreen() {
  const { slug, title } = useLocalSearchParams<{ slug: string; title?: string }>();
  const router = useRouter();
  const qc = useQueryClient();
  const [exam, setExam] = useState<ExamStartDto | null>(null);
  const [result, setResult] = useState<ExamResultDto | null>(null);
  const [busy, setBusy] = useState(false);
  const [error, setError] = useState<unknown>(null);

  const start = async () => {
    setBusy(true);
    setError(null);
    try {
      setExam(await post<ExamStartDto>(`/exams/${slug}/start`));
      setResult(null);
    } catch (e) {
      setError(e);
    } finally {
      setBusy(false);
    }
  };
  const submit = useCallback(
    async (answers: Answers) => {
      if (!exam) return;
      stopSpeech();
      setBusy(true);
      try {
        const clean = Object.fromEntries(Object.entries(answers).filter(([, v]) => v !== undefined));
        setResult(await post<ExamResultDto>(`/exams/${slug}/submit`, { sessionId: exam.sessionId, answers: clean }));
        setExam(null);
        qc.invalidateQueries({ queryKey: ['path'] });
        qc.invalidateQueries({ queryKey: ['dashboard'] });
      } catch (e) {
        setError(e);
      } finally {
        setBusy(false);
      }
    },
    [exam, slug, qc],
  );

  if (busy) return <Loading label={exam ? 'Correction de ta copie…' : 'Préparation de l’examen…'} />;
  if (result) return <ExamResult result={result} onAgain={start} onBack={() => router.back()} />;
  if (exam) return <ExamRunner exam={exam} onSubmit={submit} />;
  return (
    <Screen>
      <Button label="← Parcours" tone="quiet" onPress={() => router.back()} style={{ alignSelf: 'flex-start' }} />
      <View style={{ alignItems: 'center', gap: 10 }}>
        <Text style={{ fontSize: 56, fontWeight: '900', color: C.ko }}>模試</Text>
        <H1 style={{ textAlign: 'center' }}>{title ?? 'Examen blanc'}</H1>
      </View>
      <P>Questions réparties comme au JLPT : vocabulaire et kanji (文字・語彙), grammaire (文法・読解) et écoute (聴解). Pas de correction pendant l’épreuve : ta copie est corrigée à la fin. Le temps est limité.</P>
      <Card><P soft>Examen blanc non officiel, conçu par Koto Quest : il ne remplace pas la certification du JLPT et son résultat n’en prédit pas la réussite.</P></Card>
      {error ? <ErrorBox error={error} /> : null}
      <Button label="Commencer l’examen" tone="gold" onPress={start} />
    </Screen>
  );
}

function ExamRunner({ exam, onSubmit }: { exam: ExamStartDto; onSubmit: (a: Answers) => void }) {
  const [answers, setAnswers] = useState<Answers>({});
  const [index, setIndex] = useState(0);
  const [confirm, setConfirm] = useState(false);
  const deadline = useRef(Date.now() + exam.exam.durationMin * 60_000);
  const [left, setLeft] = useState(exam.exam.durationMin * 60_000);
  const latest = useRef(answers);
  latest.current = answers;
  useEffect(() => {
    const t = setInterval(() => {
      const l = deadline.current - Date.now();
      setLeft(Math.max(0, l));
      if (l <= 0) {
        clearInterval(t);
        onSubmit(latest.current); // copie rendue automatiquement à la fin du temps
      }
    }, 500);
    return () => clearInterval(t);
  }, [onSubmit]);
  const q = exam.questions[index];
  const section = exam.exam.sections.find((s) => s.id === q.section);
  const answered = exam.questions.filter((x) => answers[x.id] !== undefined).length;
  const mm = Math.floor(left / 60_000);
  const ss = String(Math.floor((left % 60_000) / 1000)).padStart(2, '0');
  const ask = () => {
    const missing = exam.questions.length - answered;
    const msg = missing > 0 ? `${missing} question(s) sans réponse compteront comme fausses.` : 'Toutes les questions ont une réponse.';
    if (Platform.OS === 'web') setConfirm(true);
    else Alert.alert('Rendre ta copie ?', msg, [{ text: 'Continuer l’examen', style: 'cancel' }, { text: 'Rendre ma copie', onPress: () => onSubmit(answers) }]);
  };
  return (
    <Screen>
      <View style={{ flexDirection: 'row', justifyContent: 'space-between', alignItems: 'center' }}>
        <Text style={{ fontWeight: '800', color: C.ink, flex: 1 }}>{exam.exam.title}</Text>
        <Text accessibilityRole="timer" accessibilityLabel={`Temps restant : ${mm} minutes ${ss} secondes`} style={{ fontWeight: '800', fontVariant: ['tabular-nums'], paddingHorizontal: 12, paddingVertical: 4, borderRadius: 99, backgroundColor: left < 120_000 ? C.koBg : C.surface2, color: left < 120_000 ? C.ko : C.ink }}>{mm}:{ss}</Text>
      </View>
      <ScrollView horizontal showsHorizontalScrollIndicator={false} contentContainerStyle={{ gap: 6 }}>
        {exam.questions.map((x, i) => {
          const done = answers[x.id] !== undefined;
          return (
            <Pressable key={x.id} accessibilityRole="button" accessibilityLabel={`Question ${i + 1}${done ? ', répondue' : ''}`} onPress={() => setIndex(i)} style={{ width: 34, height: 34, borderRadius: 8, borderWidth: 2, borderColor: i === index ? C.ink : C.line, backgroundColor: done ? C.ink : C.surface, alignItems: 'center', justifyContent: 'center' }}>
              <Text style={{ fontSize: 12, fontWeight: '800', color: done ? C.paper : C.inkSoft }}>{i + 1}</Text>
            </Pressable>
          );
        })}
      </ScrollView>
      {section && <P soft>{section.jpTitle} · {section.title}</P>}
      <ExamQuestion key={q.id} q={q} number={index + 1} value={answers[q.id]} onChange={(v) => setAnswers({ ...answers, [q.id]: v })} />
      <View style={{ flexDirection: 'row', gap: 10 }}>
        <Button label="Précédente" tone="quiet" disabled={index === 0} onPress={() => setIndex(index - 1)} style={{ flex: 1 }} />
        {index + 1 < exam.questions.length ? <Button label="Suivante" onPress={() => setIndex(index + 1)} style={{ flex: 1 }} /> : <Button label="Rendre ma copie" tone="gold" onPress={ask} style={{ flex: 1 }} />}
      </View>
      <P soft>{answered} réponse{answered > 1 ? 's' : ''} sur {exam.questions.length}.</P>
      <Button label="Rendre ma copie maintenant" tone="quiet" onPress={ask} />
      {confirm && (
        <Card style={{ gap: 10, borderColor: C.ink, borderWidth: 2 }}>
          <P style={{ fontWeight: '800' }}>Rendre ta copie ? {answered < exam.questions.length ? `${exam.questions.length - answered} question(s) sans réponse compteront comme fausses.` : ''}</P>
          <Button label="Confirmer : rendre ma copie" tone="gold" onPress={() => onSubmit(answers)} />
          <Button label="Continuer l’examen" tone="quiet" onPress={() => setConfirm(false)} />
        </Card>
      )}
    </Screen>
  );
}

function ExamResult({ result, onAgain, onBack }: { result: ExamResultDto; onAgain: () => void; onBack: () => void }) {
  return (
    <Screen>
      <View style={{ alignItems: 'center', gap: 6 }}>
        <Text style={{ fontSize: 48, fontWeight: '900', color: C.ko }}>{result.passed ? '合格' : '不合格'}</Text>
        <H1 style={{ textAlign: 'center' }}>{result.passed ? 'Seuil indicatif atteint' : 'Pas encore le seuil'}</H1>
        <Text style={{ fontSize: 56, fontWeight: '900', color: C.ink }}>{result.scaled ? `${result.scaled.total} / ${result.scaled.max.total}` : `${result.percent} %`}</Text>
        <P soft>{result.correct} bonnes réponses sur {result.total}{result.late ? ' (copie rendue après le temps imparti)' : ''}</P>
        <Text style={{ color: C.goldInk, fontWeight: '800', fontSize: 18 }}>+{result.xpGained} XP{result.coinsGained > 0 ? ` · +${result.coinsGained} pièces` : ''}</Text>
        <P soft style={{ textAlign: 'center' }}>Seuil Koto Quest : {result.passPercent} % au total et au moins {result.sectionMinPercent} % dans chaque section. Examen blanc non officiel.</P>
      </View>
      <H2>Par compétence</H2>
      {result.sections.map((s) => (
        <View key={s.id} style={{ gap: 4 }}>
          <View style={{ flexDirection: 'row', justifyContent: 'space-between' }}>
            <Text style={{ fontWeight: '800', color: C.ink }}>{s.jpTitle} · {s.title}</Text>
            <Text style={{ color: C.ink }}>{s.correct}/{s.total} ({s.percent} %)</Text>
          </View>
          <View style={{ flexDirection: 'row' }}><ProgressBar value={s.percent} max={100} color={s.percent >= result.sectionMinPercent ? C.ok : C.gold} label={`${s.title} : ${s.percent} %`} /></View>
        </View>
      ))}
      {result.recommendations.length > 0 && (
        <>
          <H2>Conseils</H2>
          {result.recommendations.map((r) => <Card key={r}><P>{r}</P></Card>)}
        </>
      )}
      {result.mistakes.length > 0 && (
        <>
          <H2>Tes erreurs</H2>
          {result.mistakes.slice(0, 20).map((m, i) => (
            <Card key={i} style={{ gap: 4 }}>
              <P soft>{m.prompt}</P>
              {m.jp && <Text style={{ fontSize: 20, color: C.ink }}>{m.jp.replace(/\{\{|\}\}/g, '')}</Text>}
              <P>Ta réponse : <Text style={{ color: C.ko, fontWeight: '700' }}>{m.given ?? '—'}</Text></P>
              <P>Bonne réponse : <Text style={{ color: C.ok, fontWeight: '800' }}>{m.correctAnswer}</Text></P>
              <P soft>{m.explanation}</P>
            </Card>
          ))}
        </>
      )}
      <Button label="Repasser l’examen" tone="gold" onPress={onAgain} />
      <Button label="Retour au parcours" tone="quiet" onPress={onBack} />
    </Screen>
  );
}
