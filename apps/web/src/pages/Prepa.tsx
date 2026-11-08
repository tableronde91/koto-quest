import { useState } from 'react';
import { Link } from 'react-router';
import { motion } from 'motion/react';
import { useQuery, useQueryClient } from '@tanstack/react-query';
import type { JlptDrillsDto, MeDto, SessionDto } from '@koto/shared';
import { api, post } from '../api/client';
import { QuizRunner, RunSummary } from '../components/QuizRunner';
import { ErrorBox, PageTitle, Spinner } from '../components/ui';
import { Confetti, Stamp } from '../components/Celebrate';
import { T } from '../i18n';

const GLYPH: Record<JlptDrillsDto['drills'][number]['part'], string> = { kanji: '読', writing: '書', grammar: '文', star: '★', listening: '聴' };

/**
 * Atelier JLPT : s'entraîner épreuve par épreuve au format de l'examen,
 * avec uniquement ce que l'on a déjà appris (correction immédiate, erreurs reprises en fin de série).
 */
export function PrepaPage({ me }: { me: MeDto }) {
  const qc = useQueryClient();
  const { data, isLoading, error, refetch } = useQuery({ queryKey: ['jlpt-drills'], queryFn: () => api<JlptDrillsDto>('/jlpt/drills') });
  const [run, setRun] = useState<{ part: string; title: string; session: SessionDto } | null>(null);
  const [summary, setSummary] = useState<{ title: string; part: string; s: RunSummary } | null>(null);
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
      <QuizRunner
        key={run.session.sessionId}
        questions={run.session.questions}
        furigana={false}
        onQuit={() => setRun(null)}
        onFinish={(s) => {
          setSummary({ title: run.title, part: run.part, s });
          setRun(null);
          qc.invalidateQueries();
        }}
      />
    );

  if (summary) {
    const pct = summary.s.total ? Math.round((summary.s.correct / summary.s.total) * 100) : 0;
    return (
      <div className="flex flex-col items-center gap-4 py-8 text-center">
        {pct >= 80 && <Confetti />}
        <Stamp className="jp text-6xl font-black text-ko">{pct >= 80 ? '合格' : '練習'}</Stamp>
        <h1 className="text-4xl">{T("{0} : {1} %", [summary.title, pct])}</h1>
        <p className="text-lg">{T("{0}/{1} bonnes réponses du premier coup{2} · +{3} XP", [summary.s.correct , summary.s.total , summary.s.fixed ? T(", {0} corrigée(s) en reprise", [summary.s.fixed]) : '' , summary.s.xp ])}</p>
        <p className="max-w-[50ch] text-ink-soft">{pct >= 80 ? T("Niveau examen atteint sur cette épreuve. Varie avec les autres épreuves.") : T("Les notions ratées reviendront dans tes révisions. Une autre série pour consolider ?")}</p>
        <div className="flex flex-wrap justify-center gap-3">
          <button className="btn btn-gold" onClick={() => start(summary.part, summary.title)}>{T("Nouvelle série")}</button>
          <button className="btn btn-quiet" onClick={() => setSummary(null)}>{T("Autres épreuves")}</button>
        </div>
      </div>
    );
  }

  if (isLoading) return <Spinner />;
  if (error || !data) return <ErrorBox error={error} onRetry={refetch} />;
  return (
    <div className="flex flex-col gap-8">
      <PageTitle sub={T("Chaque épreuve du JLPT, au format exact de l’examen, avec seulement ce que tu as déjà appris. Correction immédiate, erreurs reprises en fin de série.")}>{T("Atelier JLPT")}</PageTitle>
      {startError != null && <ErrorBox error={startError} />}
      <ul className="grid gap-4 sm:grid-cols-2">
        {data.drills.map((d, i) => {
          const ready = d.available >= data.minQuestions;
          return (
            <motion.li key={d.part} initial={{ opacity: 0, y: 10 }} animate={{ opacity: 1, y: 0 }} transition={{ delay: i * 0.06 }} className="flex flex-col gap-3 rounded-3xl border border-line bg-surface p-5">
              <div className="flex items-center gap-4">
                <span aria-hidden="true" className="jp flex h-14 w-14 shrink-0 items-center justify-center rounded-2xl bg-[#8E1B26] text-3xl font-black text-white">{GLYPH[d.part]}</span>
                <div>
                  <p lang="ja" className="jp text-sm font-bold text-ink-soft">{d.jpTitle}</p>
                  <h2 className="text-xl">{d.title}</h2>
                </div>
              </div>
              <p className="text-ink-soft">{d.description}</p>
              <div className="mt-auto flex items-center justify-between gap-3">
                <span className="text-sm text-ink-soft">{ready ? T("{0} questions par série", [Math.min(10, d.available)]) : T("Termine quelques leçons de plus")}</span>
                <button className="btn btn-primary" disabled={!ready} onClick={() => start(d.part, d.title)}>{T("S’entraîner")}</button>
              </div>
            </motion.li>
          );
        })}
      </ul>
      <section className="flex flex-col items-start gap-3 rounded-3xl bg-ink p-6 text-paper sm:flex-row sm:items-center">
        <span aria-hidden="true" className="jp text-5xl font-black">試</span>
        <div className="flex-1">
          <p className="text-lg font-bold">{T("Prêt·e pour l’épreuve complète ?")}</p>
          <p className="opacity-80">{T("Examen blanc {0} : toutes les épreuves, chronométré, noté comme le vrai.", [ me.preferences.targetLevel === 'N4' ? 'N4' : 'N5' ])}</p>
        </div>
        <Link to={me.preferences.targetLevel === 'N4' ? '/exam/n4-mock' : '/exam/n5-jlpt'} className="btn btn-gold">{T("Passer l’examen blanc")}</Link>
      </section>
    </div>
  );
}
