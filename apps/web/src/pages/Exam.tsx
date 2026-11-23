import { languageOfLevel } from '@koto/shared';
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
import { EXAMS, examScale } from '@koto/learning-engine';
import { langOf } from '../lib/format';
import { T } from '../i18n';
import { useStudyLang, useDecor } from '../components/StudyLanguage';

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
  const topik = (def?.level ?? '').startsWith('TOPIK');
  const english = languageOfLevel(def?.level) === 'en';
  const hsk = languageOfLevel(def?.level) === 'zh';
  const dele = languageOfLevel(def?.level) === 'es';

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
      <Stamp className="jp text-6xl font-black text-ko">{english ? 'Mock test' : hsk ? '模拟考试' : dele ? 'Simulacro' : topik ? '모의고사' : '模試'}</Stamp>
      <h1 className="text-4xl">{def?.title ?? T("Examen blanc")}</h1>
      {english ? (
        <p className="max-w-[52ch] text-lg">{def?.scoring === 'toeic' ? T("{0} questions en {1} minutes, réparties comme au TOEIC : écoute (photos, questions-réponses, conversations, annonces, avec des accents américain, britannique, australien et canadien), phrases et textes à compléter, compréhension écrite. Pas de correction pendant l’épreuve : tu peux revenir sur tes réponses avant de rendre ta copie.", [def.sections.reduce((n, x) => n + x.count, 0), def.durationMin]) : T("{0} questions en {1} minutes sur les leçons du niveau : vocabulaire, grammaire et écoute. Pas de correction pendant l’épreuve : tu peux revenir sur tes réponses avant de rendre ta copie.", [def ? def.sections.reduce((n, x) => n + x.count, 0) : 30, def?.durationMin ?? 25])}</p>
      ) : hsk ? (
        <p className="max-w-[52ch] text-lg">{def?.bank ? T("{0} questions en {1} minutes, réparties comme au HSK : {2}. Pas de correction pendant l’épreuve : tu peux revenir sur tes réponses avant de rendre ta copie.", [def.sections.reduce((n, x) => n + x.count, 0), def.durationMin, def.sections.map((x) => `${x.title.toLowerCase()} (${x.jpTitle})`).join(', ')]) : T("{0} questions en {1} minutes, tirées des leçons du niveau : vocabulaire, grammaire et écoute.", [def ? def.sections.reduce((n, x) => n + x.count, 0) : 30, def?.durationMin ?? 25])}</p>
      ) : dele ? (
        <p className="max-w-[52ch] text-lg">{def?.bank ? T("{0} questions en {1} minutes, réparties comme au DELE : {2}. Pas de correction pendant l’épreuve : tu peux revenir sur tes réponses avant de rendre ta copie.", [def.sections.reduce((n, x) => n + x.count, 0), def.durationMin, def.sections.map((x) => `${x.title.toLowerCase()} (${x.jpTitle})`).join(', ')]) : T("{0} questions en {1} minutes, tirées des leçons du niveau : vocabulaire, grammaire et écoute.", [def ? def.sections.reduce((n, x) => n + x.count, 0) : 30, def?.durationMin ?? 25])}</p>
      ) : topik ? (
        <p className="max-w-[52ch] text-lg">{T("{0} questions en {1} minutes, réparties comme au TOPIK : {2}. Pas de correction pendant l’épreuve : tu peux revenir sur tes réponses avant de rendre ta copie.", [def ? def.sections.reduce((n, x) => n + x.count, 0) : 30, def?.durationMin ?? 25, def?.sections.map((x) => `${x.title.toLowerCase()} (${x.jpTitle})`).join(', ') ?? ''])}</p>
      ) : (
        <p className="max-w-[52ch] text-lg">{def?.scoring === 'jlpt3' ? T("{0} questions en {1} minutes, réparties comme au JLPT : connaissances de la langue (言語知識), lecture (読解) et écoute (聴解). Pas de correction pendant l’épreuve : tu peux revenir sur tes réponses avant de rendre ta copie.", [def.sections.reduce((n, x) => n + x.count, 0), def.durationMin]) : T("{0} questions en {1} minutes, réparties comme au JLPT : vocabulaire et kanji (文字・語彙), grammaire (文法・読解) et écoute (聴解). Pas de correction pendant l’épreuve : tu peux revenir sur tes réponses avant de rendre ta copie.", [ def ? def.sections.reduce((n, x) => n + x.count, 0) : 30 , def?.durationMin ?? 25 ])}</p>
      )}
      {def?.scoring === 'topik' && (
        <ul className="grid w-full max-w-xl gap-2 text-left text-sm sm:grid-cols-3">
          <li className="rounded-2xl border border-line bg-surface p-3"><strong className="block">{T("Tout en coréen")}</strong>{T("Consignes, questions et réponses, comme le jour J.")}</li>
          <li className="rounded-2xl border border-line bg-surface p-3"><strong className="block">{T("Écoute réelle")}</strong>{T("Dialogues à deux voix, 2 écoutes au maximum.")}</li>
          <li className="rounded-2xl border border-line bg-surface p-3"><strong className="block">{T("Barème officiel")}</strong>{T("Sur 200 : niveau 1 à partir de 80, niveau 2 à partir de 140.")}</li>
        </ul>
      )}
      {def?.scoring === 'topik' && (
        <p className="text-sm text-ink-soft">{T("Pas encore prêt·e ?")}{' '}<Link to="/prepa" className="underline">{T("Atelier TOPIK")}</Link>{' '}{T("(épreuve par épreuve) ·")}{' '}<Link to={def?.level === 'TOPIK6' ? '/exam/topik6-mock' : def?.level === 'TOPIK5' ? '/exam/topik5-mock' : def?.level === 'TOPIK4' ? '/exam/topik4-mock' : def?.level === 'TOPIK3' ? '/exam/topik3-mock' : def?.level === 'TOPIK2' ? '/exam/topik2-mock' : '/exam/topik1-mock'} className="underline">{T("version entraînement")}</Link>{' '}{T("(plus facile)")}</p>
      )}
      {(def?.scoring === 'hsk' || def?.scoring === 'hsk3') && (
        <ul className="grid w-full max-w-xl gap-2 text-left text-sm sm:grid-cols-3">
          <li className="rounded-2xl border border-line bg-surface p-3"><strong className="block">{T("Tout en chinois")}</strong>{T("Consignes, questions et réponses, comme le jour J (pinyin seulement au HSK 1 et 2).")}</li>
          <li className="rounded-2xl border border-line bg-surface p-3"><strong className="block">{T("Écoute réelle")}</strong>{T("Phrases et dialogues à deux voix, 2 écoutes au maximum.")}</li>
          <li className="rounded-2xl border border-line bg-surface p-3"><strong className="block">{T("Barème officiel")}</strong>{T("Sur {0} : chaque partie sur 100, réussite à {1} au total.", [examScale(def)!.total, examScale(def)!.passTotal])}</li>
        </ul>
      )}
      {hsk && (
        <p className="text-sm text-ink-soft">{T("Pas encore prêt·e ?")}{' '}<Link to="/prepa" className="underline">{T("Atelier HSK")}</Link>{' '}{T("(épreuve par épreuve) ·")}{' '}<Link to={def?.bank ? `/exam/${def.level.toLowerCase()}-mock` : `/exam/${(def?.level ?? 'HSK1').toLowerCase()}-official`} className="underline">{def?.bank ? T("Entraînement sur les leçons") : T("Examen blanc au format officiel")}</Link></p>
      )}
      {def?.scoring === 'dele' && (
        <ul className="grid w-full max-w-xl gap-2 text-left text-sm sm:grid-cols-3">
          <li className="rounded-2xl border border-line bg-surface p-3"><strong className="block">{T("Tout en espagnol")}</strong>{T("Consignes, questions et réponses, comme le jour J.")}</li>
          <li className="rounded-2xl border border-line bg-surface p-3"><strong className="block">{T("Écoute réelle")}</strong>{T("Dialogues et annonces à deux voix, 2 écoutes au maximum.")}</li>
          <li className="rounded-2xl border border-line bg-surface p-3"><strong className="block">{T("Barème du DELE")}</strong>{T("Sur 100, en deux groupes de 50 : au moins 30 dans chacun. L’oral n’est pas évalué : le groupe 2 est noté sur l’écoute.")}</li>
        </ul>
      )}
      {dele && (
        <p className="text-sm text-ink-soft">{T("Pas encore prêt·e ?")}{' '}<Link to="/prepa" className="underline">{T("Atelier DELE")}</Link>{' '}{T("(épreuve par épreuve) ·")}{' '}<Link to={def?.bank ? `/exam/${def.level.toLowerCase()}-mock` : `/exam/${(def?.level ?? 'DELEA1').toLowerCase()}-official`} className="underline">{def?.bank ? T("Entraînement sur les leçons") : T("Examen blanc au format officiel")}</Link></p>
      )}
      {def?.scoring === 'toeic' && (
        <ul className="grid w-full max-w-xl gap-2 text-left text-sm sm:grid-cols-3">
          <li className="rounded-2xl border border-line bg-surface p-3"><strong className="block">{T("Tout en anglais")}</strong>{T("Consignes, questions et réponses, comme le jour J.")}</li>
          <li className="rounded-2xl border border-line bg-surface p-3"><strong className="block">{T("Écoute réelle")}</strong>{T("Dialogues et annonces à plusieurs voix, 2 écoutes au maximum.")}</li>
          <li className="rounded-2xl border border-line bg-surface p-3"><strong className="block">{T("Barème du TOEIC")}</strong>{T("Sur 990 : Listening et Reading de 5 à 495 chacun ; objectif {0} pour le niveau {1}.", [examScale(def)!.passTotal, def.level])}</li>
        </ul>
      )}
      {english && (
        <p className="text-sm text-ink-soft">{T("Pas encore prêt·e ?")}{' '}<Link to="/prepa" className="underline">{T("Atelier TOEIC")}</Link>{' '}{T("(épreuve par épreuve) ·")}{' '}<Link to={def?.scoring === 'toeic' ? `/exam/${def.level.toLowerCase()}-mock` : `/exam/${(def?.level ?? 'A1').toLowerCase()}-toeic`} className="underline">{def?.scoring === 'toeic' ? T("version entraînement") : T("examen au format TOEIC")}</Link>{' '}{def?.scoring === 'toeic' ? T("(plus facile)") : ''}</p>
      )}
      {(def?.scoring === 'jlpt' || def?.scoring === 'jlpt3') && (
        <ul className="grid w-full max-w-xl gap-2 text-left text-sm sm:grid-cols-3">
          <li className="rounded-2xl border border-line bg-surface p-3"><strong className="block">{T("Tout en japonais")}</strong>{T("Consignes, questions et réponses, comme le jour J.")}</li>
          <li className="rounded-2xl border border-line bg-surface p-3"><strong className="block">{T("Écoute réelle")}</strong>{T("Dialogues à deux voix, 2 écoutes au maximum, réponses parfois à entendre.")}</li>
          <li className="rounded-2xl border border-line bg-surface p-3"><strong className="block">{T("Barème officiel")}</strong>{def.scoring === 'jlpt3' ? T("Sur 180 : réussite à {0}, avec au moins 19/60 dans chacune des trois parties.", [examScale(def)!.passTotal]) : T("Sur 180 : réussite à {0}, avec au moins 38/120 et 19/60.", [examScale(def)!.passTotal])}</li>
        </ul>
      )}
      {(def?.scoring === 'jlpt' || def?.scoring === 'jlpt3') && (
        <p className="text-sm text-ink-soft">{T("Pas encore prêt·e ?")}{' '}<Link to="/prepa" className="underline">{T("Atelier JLPT")}</Link>{' '}{T("(épreuve par épreuve) ·")}{' '}<Link to={`/exam/${def.level.toLowerCase()}-mock`} className="underline">{T("version entraînement")}</Link>{' '}{T("(plus facile)")}</p>
      )}
      <p className="max-w-[52ch] rounded-2xl bg-surface-2 p-4 text-sm">{english ? T("Examen blanc non officiel, conçu par Koto Quest : il ne remplace pas le TOEIC d’ETS et son résultat n’en prédit pas le score.") : hsk ? T("Examen blanc non officiel, conçu par Koto Quest : il ne remplace pas la certification du HSK et son résultat n’en prédit pas la réussite.") : dele ? T("Examen blanc non officiel, conçu par Koto Quest : il ne remplace pas le DELE de l’Instituto Cervantes et son résultat n’en prédit pas la réussite.") : topik ? T("Examen blanc non officiel, conçu par Koto Quest : il ne remplace pas la certification du TOPIK et son résultat n’en prédit pas la réussite.") : T("Examen blanc non officiel, conçu par Koto Quest : il ne remplace pas la certification du JLPT et son résultat n’en prédit pas la réussite.")}</p>
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
  const topik = result.scaled?.max.system === 'topik';
  const toeic = result.scaled?.max.system === 'toeic';
  const hsk = result.scaled?.max.system === 'hsk';
  const dele = result.scaled?.max.system === 'dele';
  return (
    <div className="flex flex-col gap-8">
      <header className="flex flex-col items-center gap-2 text-center">
        {result.passed && <Confetti count={60} />}
        <Stamp className="jp text-5xl font-black text-ko">{toeic ? (result.passed ? 'Target reached' : 'Keep going') : hsk ? (result.passed ? '合格' : '不合格') : dele ? (result.passed ? 'Apto' : 'No apto') : topik ? (result.scaled!.level ? `${result.scaled!.level}급` : '불합격') : result.passed ? '合格' : '不合格'}</Stamp>
        <h1 className="text-4xl">{toeic ? (result.passed ? T("Score visé atteint") : T("Pas encore le score visé ({0})", [result.scaled!.max.passTotal])) : hsk ? (result.passed ? T("Examen réussi") : T("Pas encore la réussite ({0} points)", [result.scaled!.max.passTotal])) : dele ? (result.passed ? T("Examen réussi") : T("Pas encore la réussite (30 points dans chaque groupe)")) : topik ? (result.scaled!.level ? T("Niveau {0} du TOPIK atteint", [result.scaled!.level]) : T("Pas encore le niveau {0}", [result.scaled!.max.levels?.[0]?.level ?? 1])) : result.passed ? T("Seuil indicatif atteint") : T("Pas encore le seuil")}</h1>
        {topik && !result.passed && (result.scaled!.level ?? 0) > 0 && <p className="font-bold text-ko">{T("Il faut le niveau {0} ({1} points) pour valider cet examen.", [result.scaled!.max.passLevel ?? 2, result.scaled!.max.levels?.find((l) => l.level === (result.scaled!.max.passLevel ?? 2))?.min ?? 140])}</p>}
        {result.scaled ? (
          <p className="font-display text-7xl tabular-nums"><CountUp value={result.scaled.total} /><span className="text-3xl text-ink-soft"> / {result.scaled.max.total}</span></p>
        ) : (
          <p className="font-display text-7xl tabular-nums"><CountUp value={result.percent} /> %</p>
        )}
        <p className="text-ink-soft">{T("{0} bonnes réponses sur {1}{2}", [result.correct , result.total, result.late ? T(" (copie rendue après le temps imparti)") : ''])}</p>
        <p className="flex items-center gap-3 font-bold text-gold-ink">+{result.xpGained}{' '}{T("XP")}{' '}{result.coinsGained > 0 && <Coins value={result.coinsGained} />}</p>
        <p className="max-w-[56ch] text-sm text-ink-soft">
          {dele
            ? T("Barème du DELE : groupe 1 (compréhension et expression écrites, 25 + 25) et groupe 2 (compréhension auditive et expression orale, ici l’écoute seule sur 50) ; au moins 30 points dans chaque groupe. Questions rédigées par Koto Quest, non officielles.")
            : hsk
            ? T("Barème du HSK : {0}, chacune sur 100, soit {1} points ; réussite à {2} au total, sans minimum par partie. Questions rédigées par Koto Quest, non officielles.", [result.scaled!.max.writing ? T("écoute, lecture et écriture") : T("écoute et lecture"), result.scaled!.max.total, result.scaled!.max.passTotal])
            : toeic
            ? T("Barème du TOEIC Listening & Reading : écoute et lecture notées chacune de 5 à 495, soit 990 au total ; score visé {0}. Version abrégée, score converti de façon linéaire ; questions rédigées par Koto Quest, non officielles.", [result.scaled!.max.passTotal])
            : topik && result.scaled!.max.writing
            ? T("Barème du TOPIK II : écoute, écriture et lecture sur {0} points chacune, soit {1} ; niveau 3 à partir de {2}, 4 à {3}, 5 à {4}, 6 à {5}. Version abrégée, écriture adaptée en questions à choix ; questions rédigées par Koto Quest, non officielles.", [result.scaled!.max.listening, result.scaled!.max.total, ...(result.scaled!.max.levels ?? []).map((l) => l.min)])
            : topik
            ? T("Barème du TOPIK I : écoute sur {0} et lecture sur {1}, soit {2} points ; niveau 1 à partir de {3}, niveau 2 à partir de {4}. Questions rédigées par Koto Quest, non officielles.", [result.scaled!.max.listening, result.scaled!.max.language, result.scaled!.max.total, result.scaled!.max.levels?.[0]?.min ?? 80, result.scaled!.max.levels?.[1]?.min ?? 140])
            : result.scaled?.max.reading
            ? T("Barème du JLPT : réussite à {0}/{1}, avec au moins {2}/{3} en connaissances de la langue, en lecture et en écoute. Version abrégée ; questions rédigées par Koto Quest, non officielles.", [result.scaled.max.passTotal, result.scaled.max.total, result.scaled.max.passLanguage, result.scaled.max.language])
            : result.scaled
            ? T("Barème du JLPT : réussite à {0}/{1}, avec au moins {2}/{3} en langue et lecture et {4}/{5} en écoute. Questions rédigées par Koto Quest, non officielles.", [result.scaled.max.passTotal, result.scaled.max.total, result.scaled.max.passLanguage, result.scaled.max.language, result.scaled.max.passListening, result.scaled.max.listening])
            : T("Seuil Koto Quest : {0} % au total et au moins {1} % dans chaque section. Examen blanc non officiel.", [result.passPercent, result.sectionMinPercent])}
        </p>
      </header>

      {result.scaled && (
        <section aria-labelledby="jlpt-title" className={`grid gap-4 ${result.scaled.max.writing || result.scaled.max.reading ? "sm:grid-cols-3" : "sm:grid-cols-2"}`}>
          <h2 id="jlpt-title" className="sr-only">{T("Score par partie (barème JLPT)")}</h2>
          {(toeic
            ? [
                { label: 'Listening', sub: T("Écoute"), v: result.scaled.listening, max: result.scaled.max.listening, min: 0 },
                { label: 'Reading', sub: T("Lecture"), v: result.scaled.language, max: result.scaled.max.language, min: 0 },
              ]
            : dele
            ? [
                { label: 'Lectura', sub: T("Compréhension écrite"), v: result.scaled.language, max: result.scaled.max.language, min: 0 },
                { label: 'Escritura', sub: T("Expression écrite"), v: result.scaled.writing ?? 0, max: result.scaled.max.writing ?? 25, min: 0 },
                { label: 'Audición', sub: T("Compréhension auditive (groupe 2)"), v: result.scaled.listening, max: result.scaled.max.listening, min: result.scaled.max.passListening },
              ]
            : hsk
            ? [
                { label: '听力', sub: T("Écoute"), v: result.scaled.listening, max: result.scaled.max.listening, min: 0 },
                { label: '阅读', sub: T("Lecture"), v: result.scaled.language, max: result.scaled.max.language, min: 0 },
                ...(result.scaled.max.writing ? [{ label: '书写', sub: T("Écriture"), v: result.scaled.writing ?? 0, max: result.scaled.max.writing, min: 0 }] : []),
              ]
            : topik
            ? [
                { label: '듣기', sub: T("Écoute"), v: result.scaled.listening, max: result.scaled.max.listening, min: result.scaled.max.passListening },
                ...(result.scaled.max.writing ? [{ label: '쓰기', sub: T("Écriture"), v: result.scaled.writing ?? 0, max: result.scaled.max.writing, min: 0 }] : []),
                { label: '읽기', sub: T("Lecture"), v: result.scaled.language, max: result.scaled.max.language, min: result.scaled.max.passLanguage },
              ]
            : result.scaled.max.reading
            ? [
                { label: '言語知識', sub: T("Langue (vocabulaire, grammaire)"), v: result.scaled.language, max: result.scaled.max.language, min: result.scaled.max.passLanguage },
                { label: '読解', sub: T("Lecture"), v: result.scaled.reading ?? 0, max: result.scaled.max.reading, min: result.scaled.max.passReading ?? 0 },
                { label: '聴解', sub: T("Écoute"), v: result.scaled.listening, max: result.scaled.max.listening, min: result.scaled.max.passListening },
              ]
            : [
                { label: '言語知識・読解', sub: T("Langue et lecture"), v: result.scaled.language, max: result.scaled.max.language, min: result.scaled.max.passLanguage },
                { label: '聴解', sub: T("Écoute"), v: result.scaled.listening, max: result.scaled.max.listening, min: result.scaled.max.passListening },
              ]
          ).map((x) => (
            <div key={x.label} className="rounded-2xl border border-line bg-surface p-4">
              <p className="flex items-baseline justify-between gap-2"><span><span lang={langOf(x.label)} className="jp font-bold">{x.label}</span> <span className="text-sm text-ink-soft">{x.sub}</span></span><span className="font-display text-2xl tabular-nums">{x.v}<span className="text-base text-ink-soft">/{x.max}</span></span></p>
              <div className="relative mt-2">
                <ProgressBar value={x.v} max={x.max} label={T("{0} : {1} sur {2}", [x.sub, x.v, x.max])} tone={x.v >= x.min ? 'ok' : 'gold'} />
                <span aria-hidden="true" className="absolute -top-1 h-5 w-0.5 bg-ko" style={{ left: `${(x.min / x.max) * 100}%` }} />
              </div>
              {x.min > 0 && <p className="mt-1 text-xs text-ink-soft">{T("Minimum : {0} {1}", [ x.min , x.v >= x.min ? '✓' : '✗'])}</p>}
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
                  <span lang={langOf(s.jpTitle)} className="jp mr-2 text-ink-soft">{s.jpTitle}</span>
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
  const D = useDecor();
  const study = useStudyLang();
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
        <Stamp className="jp text-6xl font-black text-ko">{study.pick('診断', '진단', 'Test', '测试', 'Prueba')}</Stamp>
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
        <Stamp className="jp text-6xl font-black text-ko">{D('done')}</Stamp>
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
