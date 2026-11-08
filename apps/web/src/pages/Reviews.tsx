import { useEffect, useState } from 'react';
import { Link, useNavigate, useParams, useSearchParams } from 'react-router';
import { useQuery, useQueryClient } from '@tanstack/react-query';
import type { IssuedQuestionDto, MeDto, SessionDto } from '@koto/shared';
import { api, post } from '../api/client';
import { useReviewSummary } from '../api/hooks';
import { Question } from '../components/Question';
import { QuizRunner, RunSummary } from '../components/QuizRunner';
import { ErrorBox, PageTitle, Spinner } from '../components/ui';
import { Stamp } from '../components/Celebrate';
import { SleepingCat } from '../components/Illustrations';
import { T } from '../i18n';

export function ReviewsPage() {
  const { data, isLoading, error, refetch } = useReviewSummary();
  if (isLoading) return <Spinner />;
  if (error || !data) return <ErrorBox error={error} onRetry={refetch} />;
  return (
    <div>
      <PageTitle sub={T("Chaque notion revient au moment où tu risques de l’oublier. Les intervalles s’allongent quand tu réussis et se raccourcissent quand tu hésites.")}>{T("Révisions")}</PageTitle>
      {data.due > 0 ? (
        <div className="rounded-3xl bg-ink p-6 text-paper">
          <p className="font-display text-5xl">{data.due}</p>
          <p className="mt-1 opacity-85">{T("notion{0} à réviser maintenant{1}", [ data.due > 1 ? 's' : '' , data.due > 20 ? T(" (par séries de 20)") : ''])}</p>
          <Link to="/reviews/session" className="btn btn-gold mt-5">{T("Lancer la révision")}</Link>
        </div>
      ) : (
        <div className="flex flex-col gap-4 rounded-3xl border-2 border-dashed border-line p-6 sm:flex-row sm:items-center">
          <SleepingCat className="w-40 shrink-0" />
          <div>
          <p className="text-xl font-bold">{T("Rien à réviser pour l’instant.")}</p>
          <p className="mt-1 text-ink-soft">
            {data.learningSoon > 0 ? T("{0} notion(s) reviendront dans l’heure.", [data.learningSoon]) : T("Apprends une nouvelle leçon pour alimenter tes prochaines révisions.")}
          </p>
          <Link to="/path" className="btn btn-quiet mt-4">{T("Voir le parcours")}</Link>
          </div>
        </div>
      )}
      <p className="mt-6 text-ink-soft">{T("Plan du jour : jusqu’à {0} révisions et {1} nouvelles notions, environ {2} min.{3}", [ data.plan.reviewLimit , data.plan.newItemLimit , data.plan.estimatedMinutes , data.plan.catchUpMode && T(" Tu as du retard : on étale les révisions sur plusieurs jours plutôt que de tout imposer aujourd’hui.") ])}</p>
      <p className="mt-2"><Link to="/stats#notions" className="underline">{T("Voir toutes mes notions et leur statut")}</Link></p>
    </div>
  );
}

export function ReviewSessionPage({ me }: { me: MeDto }) {
  const [session, setSession] = useState<SessionDto | null>(null);
  const [error, setError] = useState<unknown>(null);
  const [summary, setSummary] = useState<RunSummary | null>(null);
  const navigate = useNavigate();
  const qc = useQueryClient();

  useEffect(() => {
    post<SessionDto>('/reviews/session').then(setSession).catch(setError);
  }, []);

  if (error) return <ErrorBox error={error} />;
  if (!session) return <Spinner label={T("Préparation des révisions…")} />;
  if (summary || session.questions.length === 0)
    return (
      <div className="flex flex-col items-start gap-5 py-6">
        {summary ? <Stamp className="jp text-8xl font-black text-ko">復習</Stamp> : <SleepingCat className="w-52" />}
        <h1 className="text-4xl">{summary ? T("Révision terminée") : T("Aucune révision due")}</h1>
        {summary && <p className="text-lg">{T("{0}/{1} bonnes réponses · +{2} XP", [summary.correct , summary.total , summary.xp ])}</p>}
        <div className="flex gap-3">
          <button className="btn btn-gold" onClick={() => { qc.invalidateQueries(); setSummary(null); setSession(null); post<SessionDto>('/reviews/session').then(setSession).catch(setError); }}>{T("Continuer à réviser")}</button>
          <Link to="/" className="btn btn-quiet" onClick={() => qc.invalidateQueries()}>{T("Accueil")}</Link>
        </div>
      </div>
    );
  return (
    <QuizRunner
      questions={session.questions}
      furigana={me.preferences.showFurigana}
      onFinish={(s) => { setSummary(s); qc.invalidateQueries(); }}
      onQuit={() => { qc.invalidateQueries(); navigate('/reviews'); }}
    />
  );
}

/** Mini-quiz ouvert depuis une notification push (/quiz/:id). */
export function QuizPage({ me }: { me: MeDto }) {
  const { id = '' } = useParams();
  const [params] = useSearchParams();
  const qc = useQueryClient();
  const navigate = useNavigate();
  const { data, isLoading, error } = useQuery({
    queryKey: ['question', id],
    queryFn: () => api<{ question: IssuedQuestionDto; answered: boolean; result: { correct: boolean; correctAnswer: string | string[]; explanation: string } | null }>(`/questions/${id}`),
    retry: false,
  });

  useEffect(() => {
    const n = params.get('n');
    if (n) post(`/notifications/${n}/open`).catch(() => undefined);
  }, [params]);

  if (isLoading) return <Spinner />;
  if (error || !data) return <ErrorBox error={error} />;
  const done = () => {
    qc.invalidateQueries();
    navigate('/');
  };
  return (
    <div className="flex flex-col gap-4">
      <PageTitle>{T("Petit défi japonais")}</PageTitle>
      <Question
        question={data.question}
        furigana={me.preferences.showFurigana}
        onDone={done}
        initialResult={data.result ? { ...data.result, xpGained: 0, mastery: null, nextReviewAt: null } : null}
        continueLabel={T("Retour à l’accueil")}
      />
    </div>
  );
}
