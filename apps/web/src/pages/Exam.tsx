import { useCallback, useEffect, useRef, useState } from 'react';
import { Link, useNavigate, useParams } from 'react-router';
import { useQueryClient } from '@tanstack/react-query';
import type { ExamResultDto, ExamStartDto, PlacementStepDto } from '@koto/shared';
import { post } from '../api/client';
import { usePath } from '../api/hooks';
import { ExamQuestion } from '../components/ExamQuestion';
import { ErrorBox, Jp, ProgressBar, Spinner } from '../components/ui';
import { Coins } from './Character';
import { Confetti, CountUp, Stamp } from '../components/Celebrate';
import { EXAMS } from '@koto/learning-engine';
import { T } from '../i18n';

type Answers = Record<string, string | string[] | undefined>;
// Une question sans réponse est simplement absente de la copie : elle compte comme fausse.

// ───────────────────────── Examen blanc ─────────────────────────

export function ExamPage() {
  const { slug = '' } = useParams();
  const def = EXAMS[slug];
  const { data: path } = usePath(def?.level ?? 'N5');
  const [exam, setExam] = useState<ExamStartDto | null>(null);
  const [result, setResult] = useState<ExamResultDto | null>(null);
  const [error, setError] = useState<unknown>(null);
  const [busy, setBusy] = useState(false);
  const qc = useQueryClient();
  const info = path?.worlds.find((w) => w.exam?.slug === slug)?.exam;

  async function start() {
    setError(null);
    setResult(null);
    try {
      setExam(await post<ExamStartDto>(`/exams/${slug}/start`));
    } catch (e) {
      setError(e);
    }
  }

  const submit = useCallback(
    async (answers: Answers) => {
      if (!exam || busy) return;
      setBusy(true);
      try {
        setResult(await post<ExamResultDto>(`/exams/${slug}/submit`, { sessionId: exam.sessionId, answers }));
        setExam(null);
        qc.invalidateQueries();
      } catch (e) {
        setError(e);
      } finally {
        setBusy(false);
      }
    },
    [exam, busy, slug, qc],
  );

  if (error) return <div className="flex flex-col gap-4"><ErrorBox error={error} /><Link to="/path" className="underline">{T("Retour au parcours")}</Link></div>;
  if (result) return <ExamResult result={result} onAgain={start} />;
  if (exam) return busy ? <Spinner label={T("Correction de ta copie…")} /> : <ExamRunner exam={exam} onSubmit={submit} />;

  return (
    <div className="flex flex-col items-center gap-5 py-6 text-center">
      <Link to={`/path?niveau=${def?.level ?? 'N5'}`} className="self-start text-ink-soft underline">{T("← Parcours")}</Link>
      <Stamp className="jp text-6xl font-black text-ko">模試</Stamp>
      <h1 className="text-4xl">{def?.title ?? T("Examen blanc")}</h1>
      <p className="max-w-[52ch] text-lg">{T("{0} questions en {1} minutes, réparties comme au JLPT : vocabulaire et kanji (文字・語彙), grammaire (文法・読解) et écoute (聴解). Pas de correction pendant l’épreuve : tu peux revenir sur tes réponses avant de rendre ta copie.", [ def ? def.sections.reduce((n, x) => n + x.count, 0) : 30 , def?.durationMin ?? 25 ])}</p>
      {def?.scoring === 'jlpt' && (
        <ul className="grid w-full max-w-xl gap-2 text-left text-sm sm:grid-cols-3">
          <li className="rounded-2xl border border-line bg-surface p-3"><strong className="block">{T("Tout en japonais")}</strong>{T("Consignes, questions et réponses, comme le jour J.")}</li>
          <li className="rounded-2xl border border-line bg-surface p-3"><strong className="block">{T("Écoute réelle")}</strong>{T("Dialogues à deux voix, 2 écoutes au maximum, réponses parfois à entendre.")}</li>
          <li className="rounded-2xl border border-line bg-surface p-3"><strong className="block">{T("Barème officiel")}</strong>{T("Sur 180 : réussite à 80, avec au moins 38/120 et 19/60.")}</li>
        </ul>
      )}
      {def?.scoring === 'jlpt' && (
        <p className="text-sm text-ink-soft">{T("Pas encore prêt·e ?")}{' '}<Link to="/prepa" className="underline">{T("Atelier JLPT")}</Link>{' '}{T("(épreuve par épreuve) ·")}{' '}<Link to="/exam/n5-mock" className="underline">{T("version entraînement")}</Link>{' '}{T("(plus facile)")}</p>
      )}
      <p className="max-w-[52ch] rounded-2xl bg-surface-2 p-4 text-sm">{T("Examen blanc non officiel, conçu par Koto Quest : il ne remplace pas la certification du JLPT et son résultat n’en prédit pas la réussite.")}</p>
      {info && info.attempts > 0 && <p>{T("Meilleur score :")}{' '}<strong>{info.bestPercent} %</strong> ({info.attempts}{' '}{T("tentative")}{info.attempts > 1 ? 's' : ''})</p>}
      <button className="btn btn-gold min-h-14 px-10 text-lg" onClick={start}>{T("Commencer l’examen")}</button>
    </div>
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
        onSubmit(latest.current); // envoi automatique à la fin du temps
      }
    }, 500);
    return () => clearInterval(t);
  }, [onSubmit]);

  const q = exam.questions[index];
  const section = exam.exam.sections.find((s) => s.id === q.section);
  const answered = exam.questions.filter((x) => answers[x.id] !== undefined).length;
  const mm = Math.floor(left / 60_000);
  const ss = String(Math.floor((left % 60_000) / 1000)).padStart(2, '0');

  return (
    <div className="flex flex-col gap-5">
      <div className="flex items-center justify-between gap-3">
        <p className="font-bold">{exam.exam.title}</p>
        <p role="timer" aria-label={T("Temps restant : {0} minutes {1} secondes", [mm, ss])} className={`rounded-full px-3 py-1 font-bold tabular-nums ${left < 120_000 ? 'bg-ko-bg text-ko' : 'bg-surface-2'}`}>
          {mm}:{ss}
        </p>
      </div>
      <nav aria-label={T("Questions")} className="flex flex-wrap gap-1.5">
        {exam.questions.map((x, i) => (
          <button
            key={x.id}
            onClick={() => setIndex(i)}
            aria-current={i === index}
            aria-label={T("Question {0}{1}", [i + 1, answers[x.id] !== undefined ? T(", répondue") : ''])}
            className="h-8 w-8 rounded-lg border-2 text-xs font-bold tabular-nums"
            style={{ borderColor: i === index ? 'var(--ink)' : 'var(--line)', background: answers[x.id] !== undefined ? 'var(--ink)' : 'var(--surface)', color: answers[x.id] !== undefined ? 'var(--paper)' : 'var(--ink-soft)' }}
          >
            {i + 1}
          </button>
        ))}
      </nav>
      {section && (
        <p className="text-sm text-ink-soft">
          <span lang="ja" className="jp mr-2">{section.jpTitle}</span>
          {section.title}
        </p>
      )}
      <ExamQuestion key={q.id} q={q} number={index + 1} value={answers[q.id]} onChange={(v) => setAnswers({ ...answers, [q.id]: v })} />
      <div className="flex flex-wrap items-center justify-between gap-3">
        <button className="btn btn-quiet" disabled={index === 0} onClick={() => setIndex(index - 1)}>{T("Précédente")}</button>
        {index + 1 < exam.questions.length ? (
          <button className="btn btn-primary" onClick={() => setIndex(index + 1)}>{T("Suivante")}</button>
        ) : (
          <button className="btn btn-gold" onClick={() => setConfirm(true)}>{T("Rendre ma copie")}</button>
        )}
      </div>
      <p className="text-sm text-ink-soft">
        {answered}{' '}{T("réponse")}{answered > 1 ? 's' : ''}{' '}{T("sur")}{' '}{exam.questions.length}.{' '}
        <button className="underline" onClick={() => setConfirm(true)}>{T("Rendre ma copie maintenant")}</button>
      </p>
      {confirm && (
        <div role="alertdialog" aria-labelledby="confirm-title" className="rounded-2xl border-2 border-ink bg-surface p-4">
          <p id="confirm-title" className="font-bold">{T("Rendre ta copie ? {0}", [ answered < exam.questions.length && T("{0} question(s) sans réponse compteront comme fausses.", [exam.questions.length - answered]) ])}</p>
          <div className="mt-3 flex gap-3">
            <button className="btn btn-gold" onClick={() => onSubmit(answers)}>{T("Rendre ma copie")}</button>
            <button className="btn btn-quiet" onClick={() => setConfirm(false)}>{T("Continuer l’examen")}</button>
          </div>
        </div>
      )}
    </div>
  );
}

function ExamResult({ result, onAgain }: { result: ExamResultDto; onAgain: () => void }) {
  return (
    <div className="flex flex-col gap-8">
      <header className="flex flex-col items-center gap-2 text-center">
        {result.passed && <Confetti count={60} />}
        <Stamp className="jp text-5xl font-black text-ko">{result.passed ? '合格' : '不合格'}</Stamp>
        <h1 className="text-4xl">{result.passed ? T("Seuil indicatif atteint") : T("Pas encore le seuil")}</h1>
        {result.scaled ? (
          <p className="font-display text-7xl tabular-nums"><CountUp value={result.scaled.total} /><span className="text-3xl text-ink-soft"> / {result.scaled.max.total}</span></p>
        ) : (
          <p className="font-display text-7xl tabular-nums"><CountUp value={result.percent} /> %</p>
        )}
        <p className="text-ink-soft">{T("{0} bonnes réponses sur {1}{2}", [result.correct , result.total, result.late ? T(" (copie rendue après le temps imparti)") : ''])}</p>
        <p className="flex items-center gap-3 font-bold text-gold-ink">+{result.xpGained}{' '}{T("XP")}{' '}{result.coinsGained > 0 && <Coins value={result.coinsGained} />}</p>
        <p className="max-w-[56ch] text-sm text-ink-soft">
          {result.scaled
            ? T("Barème du JLPT : réussite à {0}/{1}, avec au moins {2}/{3} en langue et lecture et {4}/{5} en écoute. Questions rédigées par Koto Quest, non officielles.", [result.scaled.max.passTotal, result.scaled.max.total, result.scaled.max.passLanguage, result.scaled.max.language, result.scaled.max.passListening, result.scaled.max.listening])
            : T("Seuil Koto Quest : {0} % au total et au moins {1} % dans chaque section. Examen blanc non officiel.", [result.passPercent, result.sectionMinPercent])}
        </p>
      </header>

      {result.scaled && (
        <section aria-labelledby="jlpt-title" className="grid gap-4 sm:grid-cols-2">
          <h2 id="jlpt-title" className="sr-only">{T("Score par partie (barème JLPT)")}</h2>
          {[
            { label: '言語知識・読解', sub: T("Langue et lecture"), v: result.scaled.language, max: result.scaled.max.language, min: result.scaled.max.passLanguage },
            { label: '聴解', sub: T("Écoute"), v: result.scaled.listening, max: result.scaled.max.listening, min: result.scaled.max.passListening },
          ].map((x) => (
            <div key={x.label} className="rounded-2xl border border-line bg-surface p-4">
              <p className="flex items-baseline justify-between gap-2"><span><span lang="ja" className="jp font-bold">{x.label}</span> <span className="text-sm text-ink-soft">{x.sub}</span></span><span className="font-display text-2xl tabular-nums">{x.v}<span className="text-base text-ink-soft">/{x.max}</span></span></p>
              <div className="relative mt-2">
                <ProgressBar value={x.v} max={x.max} label={T("{0} : {1} sur {2}", [x.sub, x.v, x.max])} tone={x.v >= x.min ? 'ok' : 'gold'} />
                <span aria-hidden="true" className="absolute -top-1 h-5 w-0.5 bg-ko" style={{ left: `${(x.min / x.max) * 100}%` }} />
              </div>
              <p className="mt-1 text-xs text-ink-soft">{T("Minimum : {0} {1}", [ x.min , x.v >= x.min ? '✓' : '✗'])}</p>
            </div>
          ))}
        </section>
      )}

      <section aria-labelledby="sections-title">
        <h2 id="sections-title" className="text-xl">{T("Par compétence")}</h2>
        <ul className="mt-3 flex flex-col gap-4">
          {result.sections.map((s) => (
            <li key={s.id}>
              <div className="flex items-baseline justify-between gap-3">
                <p className="font-bold">
                  <span lang="ja" className="jp mr-2 text-ink-soft">{s.jpTitle}</span>
                  {s.title}
                </p>
                <p className="tabular-nums">{s.correct}/{s.total} ({s.percent} %)</p>
              </div>
              <div className="mt-1">
                <ProgressBar value={s.percent} max={100} label={`${s.title} : ${s.percent} %`} tone={s.percent >= result.sectionMinPercent ? 'ok' : 'gold'} />
              </div>
            </li>
          ))}
        </ul>
      </section>

      <section aria-labelledby="reco-title" className="rounded-2xl bg-surface-2 p-4">
        <h2 id="reco-title" className="text-xl">{T("Que réviser maintenant ?")}</h2>
        <ul className="mt-2 list-disc pl-5">
          {result.recommendations.map((r) => <li key={r}>{r}</li>)}
        </ul>
        {result.mistakes.length > 0 && <p className="mt-2 text-sm text-ink-soft">{T("Les notions ratées ont été ajoutées à tes révisions.")}</p>}
      </section>

      {result.mistakes.length > 0 && (
        <section aria-labelledby="mistakes-title">
          <h2 id="mistakes-title" className="text-xl">{T("Tes erreurs ({0})", [ result.mistakes.length ])}</h2>
          <ul className="mt-3 flex flex-col gap-3">
            {result.mistakes.map((m, i) => (
              <li key={i} className="rounded-2xl border border-line bg-surface p-4">
                <p className="text-sm text-ink-soft">{m.prompt}</p>
                {m.jp && !m.jp.includes('|') && <Jp text={m.jp.replace(/\{\{(.*?)\}\}/g, '【$1】').replace(/(?<!＿)＿(?!＿)/g, '（　）')} furigana={false} className="text-2xl" />}
                {m.text && <p>{m.text}</p>}
                <p className="mt-1">{T("Ta réponse :")}{' '}<span className="font-bold text-ko">{m.given ?? 'aucune'}</span>{' '}{T("· Bonne réponse :")}{' '}<span className="jp font-bold text-ok">{m.correctAnswer}</span>
                </p>
                <p className="text-sm text-ink-soft">{m.explanation}</p>
              </li>
            ))}
          </ul>
        </section>
      )}

      <div className="flex flex-wrap gap-3">
        <button className="btn btn-gold" onClick={onAgain}>{T("Repasser l’examen")}</button>
        <Link to="/reviews" className="btn btn-quiet">{T("Réviser mes erreurs")}</Link>
        <Link to="/stats#examens" className="btn btn-quiet">{T("Voir l’historique")}</Link>
      </div>
    </div>
  );
}

// ───────────────────────── Test de positionnement ─────────────────────────

export function PlacementPage() {
  const [step, setStep] = useState<PlacementStepDto | null>(null);
  const [answers, setAnswers] = useState<Answers>({});
  const [error, setError] = useState<unknown>(null);
  const [busy, setBusy] = useState(false);
  const [validatedSoFar, setValidatedSoFar] = useState<string[]>([]);
  const qc = useQueryClient();
  const navigate = useNavigate();

  async function start() {
    setError(null);
    try {
      setStep(await post<PlacementStepDto>('/placement/start'));
      setValidatedSoFar([]);
    } catch (e) {
      setError(e);
    }
  }

  async function submit() {
    if (!step || step.done) return;
    setBusy(true);
    try {
      const next = await post<PlacementStepDto>('/placement/answer', { sessionId: step.block.sessionId, answers });
      if (!next.done && next.lastPassed) setValidatedSoFar([...validatedSoFar, step.block.world.title]);
      setStep(next);
      setAnswers({});
      if (next.done) qc.invalidateQueries();
    } catch (e) {
      setError(e);
    } finally {
      setBusy(false);
    }
  }

  if (error) return <ErrorBox error={error} />;
  if (!step)
    return (
      <div className="flex flex-col items-center gap-5 py-6 text-center">
        <Link to="/" className="self-start text-ink-soft underline">{T("← Accueil")}</Link>
        <Stamp className="jp text-6xl font-black text-ko">診断</Stamp>
        <h1 className="text-4xl">{T("Test de positionnement")}</h1>
        <p className="max-w-[52ch] text-lg">{T("Trois questions par monde, dans l’ordre du parcours. Chaque monde réussi (2 bonnes réponses sur 3) est validé et tu passes au suivant ; le test s’arrête au premier monde à travailler.")}</p>
        <p className="max-w-[52ch] text-ink-soft">{T("Les notions des mondes validés reviendront en révision dans quelques jours pour vérifier qu’elles sont bien acquises. Réponds sans deviner : « je ne sais pas » vaut mieux qu’un coup de chance.")}</p>
        <button className="btn btn-gold min-h-14 px-10 text-lg" onClick={start}>{T("Commencer le test")}</button>
      </div>
    );

  if (step.done)
    return (
      <div className="flex flex-col items-center gap-5 py-6 text-center">
        {step.validated.length > 0 && <Confetti />}
        <Stamp className="jp text-6xl font-black text-ko">完了</Stamp>
        <h1 className="text-4xl">{step.validated.length ? T("{0} monde{1} validé{2}", [step.validated.length, step.validated.length > 1 ? 's' : '', step.validated.length > 1 ? 's' : '']) : T("On commence au début")}</h1>
        {step.validated.length > 0 && (
          <ul className="flex flex-col gap-1">
            {step.validated.map((w) => <li key={w.slug} className="font-bold text-ok">✓ {w.title}</li>)}
          </ul>
        )}
        {step.stoppedAt && <p className="max-w-[52ch]">{T("Ton parcours reprend au monde « {0} ».", [ step.stoppedAt.title ])}</p>}
        <div className="flex flex-wrap justify-center gap-3">
          {step.nextLesson && <button className="btn btn-gold" onClick={() => navigate(`/lesson/${step.nextLesson!.slug}`)}>{T("Commencer : {0}", [ step.nextLesson.title])}</button>}
          <Link to="/path" className="btn btn-quiet">{T("Voir le parcours")}</Link>
        </div>
      </div>
    );

  const b = step.block;
  const complete = b.questions.every((q) => answers[q.id] !== undefined);
  return (
    <div className="flex flex-col gap-6">
      <div>
        <ProgressBar value={b.index} max={b.totalWorlds} label={T("Monde {0} sur {1}", [b.index + 1, b.totalWorlds])} tone="gold" />
        <p className="mt-2 text-sm text-ink-soft">{T("Monde {0} sur {1}{2}", [ b.world.order , b.totalWorlds , validatedSoFar.length > 0 && T(", déjà validés : {0}", [validatedSoFar.join(', ')]) ])}</p>
        <h1 className="mt-1 text-3xl">{b.world.title}</h1>
      </div>
      {b.questions.map((q, i) => (
        <ExamQuestion key={q.id} q={q} number={i + 1} value={answers[q.id]} onChange={(v) => setAnswers({ ...answers, [q.id]: v })} />
      ))}
      <div className="flex flex-wrap gap-3">
        <button className="btn btn-gold" disabled={!complete || busy} onClick={submit}>{T("Valider ces réponses")}</button>
        <button className="btn btn-quiet" disabled={busy} onClick={() => submitWith(answers)}>{T("Je ne sais pas")}</button>
      </div>
    </div>
  );

  async function submitWith(a: Answers) {
    if (!step || step.done) return;
    setBusy(true);
    try {
      const next = await post<PlacementStepDto>('/placement/answer', { sessionId: step.block.sessionId, answers: a });
      setStep(next);
      setAnswers({});
      if (next.done) qc.invalidateQueries();
    } catch (e) {
      setError(e);
    } finally {
      setBusy(false);
    }
  }
}
