import { useState } from 'react';
import type { AnswerResultDto, IssuedQuestionDto } from '@koto/shared';
import { post } from '../api/client';
import { Question } from './Question';
import { ProgressBar } from './ui';
import { T } from '../i18n';

export interface RunSummary {
  /** Bonnes réponses au premier essai. */
  correct: number;
  /** Nombre d'exercices (hors reprises). */
  total: number;
  xp: number;
  /** Exercices ratés puis réussis lors d'une reprise. */
  fixed: number;
}

/**
 * Enchaîne une série de questions émises par le serveur.
 * Chaque exercice raté est ajouté à la fin de la file pour être refait (au plus deux reprises).
 */
export function QuizRunner({ questions, furigana, onFinish, onQuit }: { questions: IssuedQuestionDto[]; furigana: boolean; onFinish: (s: RunSummary) => void; onQuit?: () => void }) {
  const [queue, setQueue] = useState<IssuedQuestionDto[]>(questions);
  const [index, setIndex] = useState(0);
  const [summary, setSummary] = useState<RunSummary>({ correct: 0, total: 0, xp: 0, fixed: 0 });
  const [busy, setBusy] = useState(false);
  const q = queue[index];
  const firstRetry = queue.findIndex((x) => x.retryOf);

  // La reprise d'un exercice raté est demandée dès la correction : « Continuer » reste instantané.
  const [pendingRetry, setPendingRetry] = useState<{ id: string; promise: Promise<IssuedQuestionDto | null> } | null>(null);

  function onResult(r: AnswerResultDto) {
    if (r.correct) return;
    const promise = post<IssuedQuestionDto>(`/questions/${q.id}/retry`).catch(() => null); // reprise impossible : la notion reviendra en révision
    setPendingRetry({ id: q.id, promise });
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
  const last = index + 1 >= queue.length;
  // Profondeur de reprise de la question courante (au plus deux reprises par exercice, comme côté serveur).
  let depth = 0;
  for (let p = q.retryOf; p && depth < 5; depth++) p = queue.find((x) => x.id === p)?.retryOf ?? null;
  const willRetry = depth < 2;
  return (
    <div className="flex flex-col gap-6">
      <div className="flex items-center gap-4">
        {onQuit && (
          <button className="rounded-full p-2 text-ink-soft hover:bg-surface-2" onClick={onQuit} aria-label={T("Quitter la session")}>
            <svg width="22" height="22" viewBox="0 0 24 24" aria-hidden="true"><path d="M6 6l12 12M18 6L6 18" stroke="currentColor" strokeWidth="2.5" strokeLinecap="round" /></svg>
          </button>
        )}
        <ProgressBar value={index} max={queue.length} label={T("Question {0} sur {1}", [index + 1, queue.length])} />
        <span className="shrink-0 text-sm tabular-nums text-ink-soft" aria-hidden="true">{index + 1}/{queue.length}</span>
      </div>
      {q.retryOf && (
        <div className="flex items-center gap-3 rounded-2xl border-2 border-gold bg-surface px-4 py-3" role="note">
          <span aria-hidden="true" className="jp text-2xl font-black text-gold-ink">復</span>
          <p>
            <strong>{T("On reprend un exercice raté.")}</strong>
            {index === firstRetry && <span className="block text-sm text-ink-soft">{T("Les exercices ratés reviennent à la fin pour que tu les retravailles.")}</span>}
          </p>
        </div>
      )}
      <Question
        key={q.id}
        question={q}
        furigana={furigana}
        onDone={next}
        onResult={onResult}
        willRetry={willRetry}
        continueLabel={(r) => (busy ? '…' : last && (r.correct || !willRetry) ? T("Terminer") : T("Continuer"))}
      />
    </div>
  );
}
