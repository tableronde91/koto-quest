import { useState } from 'react';
import { Pressable, Text, View } from 'react-native';
import type { AnswerResultDto, IssuedQuestionDto } from '@koto/shared';
import { post } from './api';
import { QuestionView } from './QuestionView';
import { C } from './theme';
import { ProgressBar } from './ui';

export interface RunSummary {
  correct: number;
  total: number;
  xp: number;
  fixed: number;
}

/** Enchaîne les exercices ; un exercice raté revient en fin de séance (au plus deux reprises). */
export function QuizRunner({ questions, onFinish, onQuit }: { questions: IssuedQuestionDto[]; onFinish: (s: RunSummary) => void; onQuit?: () => void }) {
  const [queue, setQueue] = useState(questions);
  const [index, setIndex] = useState(0);
  const [summary, setSummary] = useState<RunSummary>({ correct: 0, total: 0, xp: 0, fixed: 0 });
  const [pendingRetry, setPendingRetry] = useState<{ id: string; promise: Promise<IssuedQuestionDto | null> } | null>(null);
  const [busy, setBusy] = useState(false);
  const q = queue[index];

  function onResult(r: AnswerResultDto) {
    if (r.correct) return;
    setPendingRetry({ id: q.id, promise: post<IssuedQuestionDto>(`/questions/${q.id}/retry`).catch(() => null) });
  }

  async function next(r: AnswerResultDto) {
    if (busy) return;
    const isRetry = !!q.retryOf;
    const s: RunSummary = {
      correct: summary.correct + (!isRetry && r.correct ? 1 : 0),
      total: summary.total + (isRetry ? 0 : 1),
      xp: summary.xp + r.xpGained,
      fixed: summary.fixed + (isRetry && r.correct ? 1 : 0),
    };
    setSummary(s);
    let nextQueue = queue;
    if (!r.correct && pendingRetry?.id === q.id) {
      setBusy(true);
      const again = await pendingRetry.promise;
      setBusy(false);
      setPendingRetry(null);
      if (again && !queue.some((x) => x.id === again.id)) nextQueue = [...queue, again];
      setQueue(nextQueue);
    }
    if (index + 1 >= nextQueue.length) onFinish(s);
    else setIndex(index + 1);
  }

  if (!q) return null;
  let depth = 0;
  for (let p = q.retryOf; p && depth < 5; depth++) p = queue.find((x) => x.id === p)?.retryOf ?? null;
  const willRetry = depth < 2;
  const last = index + 1 >= queue.length;
  return (
    <View style={{ gap: 16 }}>
      <View style={{ flexDirection: 'row', alignItems: 'center', gap: 12 }}>
        {onQuit && (
          <Pressable accessibilityRole="button" accessibilityLabel="Quitter la session" onPress={onQuit} hitSlop={10}>
            <Text style={{ fontSize: 22, color: C.inkSoft }}>✕</Text>
          </Pressable>
        )}
        <ProgressBar value={index} max={queue.length} label={`Question ${index + 1} sur ${queue.length}`} />
        <Text style={{ color: C.inkSoft }}>{index + 1}/{queue.length}</Text>
      </View>
      {q.retryOf && (
        <View style={{ flexDirection: 'row', gap: 10, alignItems: 'center', borderWidth: 2, borderColor: C.gold, borderRadius: 14, padding: 10, backgroundColor: C.surface }}>
          <Text style={{ fontSize: 22, fontWeight: '900', color: C.goldInk }}>復</Text>
          <Text style={{ flex: 1, fontWeight: '700', color: C.ink }}>On reprend un exercice raté.</Text>
        </View>
      )}
      <QuestionView key={q.id} q={q} onResult={onResult} onDone={next} willRetry={willRetry} continueLabel={(r) => (busy ? '…' : last && (r.correct || !willRetry) ? 'Terminer' : 'Continuer')} />
    </View>
  );
}
