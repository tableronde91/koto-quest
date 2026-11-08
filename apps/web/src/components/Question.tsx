import { ReactNode, useEffect, useMemo, useRef, useState } from 'react';
import { AnimatePresence, motion } from 'motion/react';
import { TIMEOUT_ANSWER, fillBlank, hasBlank } from '@koto/learning-engine';
import type { AnswerResultDto, IssuedQuestionDto } from '@koto/shared';
import { post } from '../api/client';
import { speak, speechSupported } from '../lib/speech';
import { MASTERY_LABEL } from '../lib/format';
import { Jp, SpeakButtons } from './ui';
import { FloatingXp } from './Celebrate';
import { ExamSentence } from './ExamQuestion';
import { T } from '../i18n';

interface Props {
  question: IssuedQuestionDto;
  furigana: boolean;
  onDone: (result: AnswerResultDto) => void;
  /** Appelé dès que la correction est connue (avant « Continuer »). */
  onResult?: (result: AnswerResultDto) => void;
  /** Résultat déjà connu (question rouverte). */
  initialResult?: AnswerResultDto | null;
  continueLabel?: string | ((result: AnswerResultDto) => string);
  /** Afficher « Tu le referas en fin de séance » après une erreur. */
  willRetry?: boolean;
  /** Combat : temps maximal de réponse (secondes). À zéro, la question est perdue. */
  timeLimitSec?: number;
  /** Appelé à l'affichage de la question (départ du chrono côté serveur). */
  onShown?: () => void;
}

/** Compte à rebours : barre qui se vide, rouge dans les 5 dernières secondes. */
function Countdown({ limitSec, running, onExpire }: { limitSec: number; running: boolean; onExpire: () => void }) {
  const [left, setLeft] = useState(limitSec * 1000);
  const fired = useRef(false);
  const expire = useRef(onExpire);
  expire.current = onExpire;
  useEffect(() => {
    if (!running) return;
    const end = performance.now() + left;
    const id = window.setInterval(() => {
      const rest = Math.max(0, end - performance.now());
      setLeft(rest);
      if (rest <= 0 && !fired.current) {
        fired.current = true;
        window.clearInterval(id);
        expire.current();
      }
    }, 100);
    return () => window.clearInterval(id);
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [running]);
  const secs = Math.ceil(left / 1000);
  const urgent = secs <= 5;
  return (
    <div className="flex items-center gap-3" data-testid="countdown">
      <span aria-hidden="true" className={`text-xl ${urgent && running ? 'animate-pulse' : ''}`}>⏱</span>
      <div className="h-3 flex-1 overflow-hidden rounded-full bg-surface-2" role="timer" aria-label={`${secs} secondes restantes`}>
        <div className="h-full rounded-full transition-[width] duration-100 ease-linear" style={{ width: `${(left / (limitSec * 1000)) * 100}%`, background: urgent ? 'var(--ko)' : 'var(--gold)' }} />
      </div>
      <span className={`w-10 text-right font-display text-lg tabular-nums ${urgent ? 'text-ko' : ''}`} aria-hidden="true">{secs}s</span>
    </div>
  );
}

const JP_RE = /[぀-ヿ一-龯]/;
const isJp = (s: string) => JP_RE.test(s);

/** Sceau « hanko » apposé sur une bonne réponse : le moment signature de l'application. */
function Hanko({ correct }: { correct: boolean }) {
  return (
    <motion.div
      initial={{ scale: 2.2, opacity: 0, rotate: -18 }}
      animate={{ scale: 1, opacity: 1, rotate: -8 }}
      transition={{ type: 'spring', stiffness: 380, damping: 18 }}
      aria-hidden="true"
      className="jp pointer-events-none flex h-16 w-16 shrink-0 items-center justify-center rounded-xl border-4 text-3xl font-black sm:h-20 sm:w-20 sm:text-4xl"
      style={{ borderColor: correct ? 'var(--ko)' : 'var(--ink-soft)', color: correct ? 'var(--ko)' : 'var(--ink-soft)' }}
    >
      {correct ? '正' : '惜'}
    </motion.div>
  );
}

/** Texte à prononcer une fois la réponse connue : la phrase complète, trou rempli. */
function spokenAfter(q: IssuedQuestionDto, answer: string | string[]): string | null {
  if (q.answerAudio) {
    // Réponse en romaji (exercice de lecture) : on lit le mot japonais, pas la réponse.
    if (!Array.isArray(answer) && !isJp(answer)) return hasBlank(q.answerAudio) ? null : q.answerAudio;
    return fillBlank(q.answerAudio, answer);
  }
  return q.type === 'listening_choice' ? null : (q.audio ?? null);
}

export function Question({ question: q, furigana, onDone, onResult, initialResult = null, continueLabel = T("Continuer"), willRetry = false, timeLimitSec, onShown }: Props) {
  const [result, setResult] = useState<AnswerResultDto | null>(initialResult);
  const [given, setGiven] = useState<string | string[] | null>(null);
  const [pending, setPending] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const startedAt = useRef(performance.now());
  const continueRef = useRef<HTMLButtonElement>(null);

  useEffect(() => {
    onShown?.();
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [q.id]);
  useEffect(() => {
    startedAt.current = performance.now();
    if (q.type === 'listening_choice' && q.audio) speak(q.audio);
  }, [q.id, q.type, q.audio]);
  useEffect(() => {
    if (result) continueRef.current?.focus();
  }, [result]);

  async function submit(answer: string | string[]) {
    if (pending || result) return;
    setGiven(answer);
    setPending(true);
    setError(null);
    try {
      const r = await post<AnswerResultDto>(`/questions/${q.id}/answer`, { answer, responseMs: Math.round(performance.now() - startedAt.current) });
      setResult(r);
      onResult?.(r);
      // Bonne réponse : on entend toute la phrase, avec le mot choisi à sa place.
      if (r.correct) {
        const text = spokenAfter(q, answer);
        if (text) speak(text);
      }
    } catch (e) {
      setGiven(null);
      setError(e instanceof Error ? e.message : T("Erreur"));
    } finally {
      setPending(false);
    }
  }

  // Raccourcis clavier 1–4 pour les choix
  useEffect(() => {
    if (!q.choices || result) return;
    const onKey = (e: KeyboardEvent) => {
      const n = Number(e.key);
      if (n >= 1 && n <= q.choices!.length && !(e.target instanceof HTMLInputElement)) submit(q.choices![n - 1]);
    };
    window.addEventListener('keydown', onKey);
    return () => window.removeEventListener('keydown', onKey);
  });

  const afterText = result ? spokenAfter(q, result.correctAnswer) : null;

  return (
    <div className="flex flex-col gap-5" data-testid="question" data-type={q.type} data-qid={q.id} data-retry={q.retryOf ? "1" : undefined}>
      {timeLimitSec !== undefined && <Countdown key={q.id} limitSec={timeLimitSec} running={!result && !pending} onExpire={() => submit(TIMEOUT_ANSWER)} />}
      <p className="text-lg font-bold" id={`prompt-${q.id}`}>{q.prompt}</p>
      <Stage q={q} furigana={furigana} result={result} afterText={afterText} />

      <div className={result && !result.correct ? 'shake' : undefined}>
      {q.choices && <Choices q={q} given={given} result={result} disabled={!!result || pending} onPick={submit} />}
      {q.type === 'sentence_order' && q.tokens && <SentenceOrder tokens={q.tokens} disabled={!!result || pending} onSubmit={submit} result={result} />}
      {q.type === 'matching' && q.pairs && <Matching pairs={q.pairs} disabled={!!result || pending} onSubmit={submit} result={result} />}
      </div>

      {error && <p role="alert" className="font-bold text-ko">{error}</p>}

      <AnimatePresence>
        {result && (
          <motion.div
            initial={{ y: 16, opacity: 0 }}
            animate={{ y: 0, opacity: 1 }}
            className="relative grid grid-cols-[auto_1fr] items-start gap-x-4 gap-y-3 rounded-2xl p-4 sm:grid-cols-[auto_1fr_auto] sm:items-center"
            style={{ background: result.correct ? 'var(--ok-bg)' : 'var(--ko-bg)' }}
            role="status"
            aria-live="polite"
          >
            {result.correct && <FloatingXp amount={result.xpGained} />}
            <Hanko correct={result.correct} />
            <div className="min-w-0">
              <p className="text-xl font-bold">{result.correct ? T("Bonne réponse !") : result.timedOut ? T("Temps écoulé !") : T("Pas tout à fait.")}</p>
              {!result.correct && q.type !== 'matching' && (
                <p className="mt-1">{T("Réponse attendue :")}{' '}<strong className="jp">{Array.isArray(result.correctAnswer) ? result.correctAnswer.join(' ') : result.correctAnswer}</strong>
                </p>
              )}
              {/* Association : le tableau des bonnes paires suffit, l'explication serait redondante. */}
              {(q.type !== 'matching' || result.correct) && <p className="mt-1 text-ink-soft">{result.explanation}</p>}
              {q.type === 'matching' && !result.correct && <p className="mt-1 text-ink-soft">{T("Les bonnes paires sont indiquées au-dessus.")}</p>}
              <p className="mt-2 flex flex-wrap gap-x-3 gap-y-1 text-sm">
                {result.xpGained > 0 && <span className="font-bold text-gold-ink">{T("+{0} XP", [ result.xpGained ])}</span>}
                {result.mastery && <span className="text-ink-soft">{T("Statut : {0}", [ MASTERY_LABEL[result.mastery]])}</span>}
                {!result.correct && willRetry && <span className="text-ink-soft">{T("Tu le referas en fin de séance.")}</span>}
                {result.questsCompleted?.map((qc) => (
                  <span key={qc.title} className="font-bold text-gold-ink">{T("Quête accomplie : {0} (+{1} XP, +5 pièces)", [ qc.title , qc.xp ])}</span>
                ))}
              </p>
            </div>
            <button ref={continueRef} className="btn btn-primary col-span-2 sm:col-span-1" onClick={() => onDone(result)}>
              {typeof continueLabel === 'function' ? continueLabel(result) : continueLabel}
            </button>
          </motion.div>
        )}
      </AnimatePresence>
    </div>
  );
}

const sameAnswer = (a: string | string[], b: string) => !Array.isArray(a) && a.normalize('NFKC').trim().toLowerCase() === b.normalize('NFKC').trim().toLowerCase();

/** Phrase à trou : le trou est dessiné, puis rempli par la bonne réponse une fois la question corrigée. */
function SentenceWithBlank({ text, fill, className }: { text: string; fill: string | null; className: string }) {
  const parts = text.split(/＿+/);
  const nodes: ReactNode[] = [];
  parts.forEach((p, i) => {
    nodes.push(<span key={`t${i}`}>{p}</span>);
    if (i < parts.length - 1)
      nodes.push(
        fill ? (
          <mark key={`b${i}`} className="mx-0.5 rounded-md bg-gold px-1 text-[#2a1a00]">{fill}</mark>
        ) : (
          <span key={`b${i}`} aria-label="mot manquant" className="mx-1 inline-block w-[2.2em] translate-y-[0.1em] border-b-[3px] border-ink-soft" />
        ),
      );
  });
  return <span lang="ja" className={`jp ${className}`}>{nodes}</span>;
}

/** Zone d'affichage principale : grand glyphe, phrase, dialogue ou bouton d'écoute. */
function Stage({ q, furigana, result, afterText }: { q: IssuedQuestionDto; furigana: boolean; result: AnswerResultDto | null; afterText: string | null }) {
  const d = q.display ?? {};
  const listen = afterText && speechSupported() ? afterText : !result && q.audio && q.type !== 'reading_choice' && speechSupported() ? q.audio : null;
  const speaker = listen ? (
    <button type="button" onClick={() => speak(listen)} className="absolute right-2 top-2 rounded-full p-2 text-ink-soft hover:bg-surface" aria-label={result ? T("Écouter la phrase complète") : T("Écouter la prononciation")}>
      <svg width="22" height="22" viewBox="0 0 24 24" aria-hidden="true"><path d="M4 9v6h4l5 4V5L8 9H4z" fill="currentColor" /><path d="M16 8.5a5 5 0 010 7" stroke="currentColor" strokeWidth="2" strokeLinecap="round" fill="none" /></svg>
    </button>
  ) : null;

  if (q.type === 'listening_choice') {
    return (
      <div className="flex min-h-36 flex-col items-center justify-center gap-3 rounded-3xl bg-surface-2 p-6">
        {speechSupported() ? <SpeakButtons text={q.audio ?? ''} size="lg" /> : <p className="text-center">{T("Ce navigateur ne peut pas lire l’audio japonais. Le mot était :")}{' '}<Jp text={q.audio ?? ''} furigana={false} className="text-3xl" /></p>}
      </div>
    );
  }
  if (d.lines) {
    const reply = result && !Array.isArray(result.correctAnswer) ? result.correctAnswer : null;
    return (
      <div className="relative flex flex-col gap-3 rounded-3xl bg-surface-2 p-5 pr-12">
        {d.lines.map((l, i) => (
          <p key={i} className="grid grid-cols-[4.5rem_1fr] items-baseline gap-3">
            <span className="text-sm font-bold text-ink-soft">{l.speaker}</span>
            <Jp text={l.jp} reading={l.reading} furigana={furigana} className="text-2xl" />
          </p>
        ))}
        {reply && (
          <p className="grid grid-cols-[4.5rem_1fr] items-baseline gap-3">
            <span className="text-sm font-bold text-ink-soft">{T("Toi")}</span>
            <span lang="ja" className="jp text-2xl"><mark className="rounded-md bg-gold px-1 text-[#2a1a00]">{reply}</mark></span>
          </p>
        )}
        {d.text && <p className="text-ink-soft">{d.text}</p>}
        {speaker}
      </div>
    );
  }
  // Rien à montrer (remise en ordre, association) : pas de grand cadre vide.
  if (!d.jp && !d.text) return null;

  // Format JLPT : mot souligné dans une phrase, consigne en japonais, aucune lecture affichée avant la réponse.
  if (d.part && d.jp) {
    return (
      <div className="relative flex min-h-36 flex-col items-center justify-center gap-2 rounded-3xl bg-surface-2 px-12 py-6 text-center">
        <span lang="ja" className="jp absolute left-4 top-3 text-xs font-bold text-ink-soft">{d.part}</span>
        <ExamSentence text={d.jp} className="text-3xl font-bold leading-loose sm:text-4xl" />
        {d.text && <p className="text-ink-soft">{d.text}</p>}
        {speaker}
      </div>
    );
  }
  const blank = hasBlank(d.jp);
  const fill = result && blank && !Array.isArray(result.correctAnswer) ? result.correctAnswer : null;
  // Pour une question de lecture, la lecture n'apparaît qu'après la réponse.
  const reading = q.type === 'reading_choice' || (q.type === 'fill_blank' && !result) ? null : d.reading;
  const len = d.jp ? [...d.jp].length : 0;
  const size = q.type === 'true_false' || len > 6 ? 'text-3xl' : len <= 2 ? 'text-7xl sm:text-8xl' : len <= 4 ? 'text-5xl sm:text-7xl' : 'text-4xl sm:text-5xl';
  return (
    <div className="relative flex min-h-36 flex-col items-center justify-center gap-2 rounded-3xl bg-surface-2 px-12 py-6 text-center">
      {d.jp && !(q.type === 'true_false' && d.text) &&
        (blank ? (
          <SentenceWithBlank text={d.jp} fill={fill} className={`${size} font-bold leading-snug`} />
        ) : (
          <Jp text={d.jp} reading={reading} furigana={furigana} className={`${size} ${len <= 6 ? 'whitespace-nowrap' : ''} font-bold`} />
        ))}
      {d.text && <p className={d.jp && q.type !== 'true_false' ? 'text-ink-soft' : 'jp text-2xl font-bold'}>{d.text}</p>}
      {speaker}
    </div>
  );
}

/**
 * Choix de réponse. Deux dispositions seulement, pour que les cases restent alignées :
 *  - réponses courtes (particules, kana, vrai/faux) : cases carrées de même largeur, texte centré ;
 *  - réponses longues : une colonne sur mobile, deux colonnes sur grand écran si le nombre est pair.
 */
function Choices({ q, given, result, disabled, onPick }: { q: IssuedQuestionDto; given: string | string[] | null; result: AnswerResultDto | null; disabled: boolean; onPick: (c: string) => void }) {
  const choices = q.choices!;
  const compact = choices.every((c) => [...c].length <= 4);
  const n = choices.length;
  const grid = compact
    ? n === 2 ? 'grid-cols-2' : n === 3 ? 'grid-cols-3' : 'grid-cols-2 sm:grid-cols-4'
    : n % 2 === 0 ? 'grid-cols-1 sm:grid-cols-2' : 'grid-cols-1';
  return (
    <div role="group" aria-labelledby={`prompt-${q.id}`} className={`grid gap-3 ${grid}`}>
      {choices.map((c, i) => {
        const isGiven = given === c;
        const isRight = result && sameAnswer(result.correctAnswer, c);
        const state = result ? (isRight ? 'right' : isGiven ? 'wrong' : 'idle') : 'idle';
        const jp = isJp(c);
        return (
          <motion.button
            key={c}
            type="button"
            disabled={disabled}
            onClick={() => onPick(c)}
            initial={{ opacity: 0, y: 10 }}
            animate={{ opacity: result && state === 'idle' ? 0.6 : 1, y: 0, scale: state === 'right' ? [1, 1.06, 1] : 1 }}
            transition={{ delay: result ? 0 : i * 0.05, duration: 0.25 }}
            whileTap={disabled ? undefined : { scale: 0.97 }}
            className={`relative flex items-center rounded-2xl border-2 transition-colors disabled:cursor-default ${
              compact ? 'min-h-20 justify-center px-2 py-3 text-center' : 'min-h-16 gap-3 px-4 py-3 text-left'
            }`}
            style={{
              borderColor: state === 'right' ? 'var(--ok)' : state === 'wrong' ? 'var(--ko)' : 'var(--line)',
              background: state === 'right' ? 'var(--ok-bg)' : state === 'wrong' ? 'var(--ko-bg)' : 'var(--surface)',
            }}
          >
            <kbd className={`hidden h-6 w-6 shrink-0 items-center justify-center rounded-md border border-line text-xs text-ink-soft sm:flex ${compact ? 'absolute left-2 top-2' : ''}`}>{i + 1}</kbd>
            <span lang={jp ? 'ja' : 'fr'} className={jp ? `jp ${compact ? 'text-3xl' : 'text-2xl'}` : compact ? 'text-xl font-bold' : 'text-lg'}>
              {c}
            </span>
          </motion.button>
        );
      })}
    </div>
  );
}

function SentenceOrder({ tokens, disabled, onSubmit, result }: { tokens: string[]; disabled: boolean; onSubmit: (a: string[]) => void; result: AnswerResultDto | null }) {
  const [placed, setPlaced] = useState<number[]>([]);
  const chip = 'jp inline-flex min-h-12 items-center rounded-xl px-3 text-xl';
  const border = result ? (result.correct ? 'var(--ok)' : 'var(--ko)') : 'var(--line)';
  return (
    <div className="flex flex-col gap-4">
      <div className="flex min-h-20 flex-wrap content-center items-center gap-2 rounded-2xl border-2 bg-surface p-3" style={{ borderColor: border }} aria-label={T("Ta phrase")}>
        {placed.length === 0 && <span className="px-1 text-ink-soft">{T("Touche les morceaux dans le bon ordre.")}</span>}
        {placed.map((i) => (
          <button key={i} type="button" disabled={disabled} onClick={() => setPlaced(placed.filter((p) => p !== i))} className={`${chip} bg-ink text-paper`}>
            {tokens[i]}
          </button>
        ))}
      </div>
      {/* Les cases gardent leur place une fois utilisées : la banque ne « saute » pas. */}
      <div className="flex flex-wrap justify-center gap-2" data-testid="token-bank">
        {tokens.map((t, i) =>
          placed.includes(i) ? (
            <span key={i} aria-hidden="true" className={`${chip} border-2 border-dashed border-line text-transparent`}>{t}</span>
          ) : (
            <button key={i} type="button" disabled={disabled} onClick={() => setPlaced([...placed, i])} className={`${chip} border-2 border-line bg-surface`}>
              {t}
            </button>
          ),
        )}
      </div>
      {!result && (
        <button className="btn btn-primary self-stretch sm:self-end" disabled={disabled || placed.length !== tokens.length} onClick={() => onSubmit(placed.map((i) => tokens[i]))}>{T("Vérifier")}</button>
      )}
    </div>
  );
}

/**
 * Association : deux colonnes de cases identiques, alignées ligne à ligne.
 * On touche un élément japonais puis un sens ; la paire formée porte le même numéro des deux côtés.
 */
function Matching({ pairs, disabled, onSubmit, result }: { pairs: { left: string[]; right: string[] }; disabled: boolean; onSubmit: (a: string[]) => void; result: AnswerResultDto | null }) {
  const [assign, setAssign] = useState<Record<number, string>>({});
  const [active, setActive] = useState<number | null>(0);
  const pairNo = useMemo(() => {
    const m = new Map<string, number>();
    Object.entries(assign).forEach(([l, r]) => m.set(r, Number(l)));
    return m;
  }, [assign]);
  const complete = Object.keys(assign).length === pairs.left.length;
  const expected = result && Array.isArray(result.correctAnswer) ? result.correctAnswer : null;

  const choose = (r: string) => {
    if (active === null) return;
    const next = Object.fromEntries(Object.entries(assign).filter(([, v]) => v !== r));
    next[active] = r;
    setAssign(next);
    const free = pairs.left.findIndex((_, i) => next[i] === undefined);
    setActive(free >= 0 ? free : null);
  };

  const cell = 'flex min-h-14 w-full items-center gap-2 rounded-2xl border-2 bg-surface px-3 py-2 text-left';
  const badge = (n: number | undefined) => (
    <span aria-hidden="true" className="flex h-6 w-6 shrink-0 items-center justify-center rounded-full text-xs font-bold" style={{ background: n === undefined ? 'var(--surface-2)' : 'var(--ink)', color: n === undefined ? 'transparent' : 'var(--paper)' }}>
      {n === undefined ? '·' : n + 1}
    </span>
  );

  return (
    <div className="flex flex-col gap-4">
      <div className="grid grid-cols-2 gap-x-3 gap-y-2">
        <p className="text-sm font-bold text-ink-soft" id="match-left">{T("Japonais")}</p>
        <p className="text-sm font-bold text-ink-soft" id="match-right">{T("Sens")}</p>
        {pairs.left.map((l, i) => {
          const r = pairs.right[i];
          const ok = expected ? expected[i] === assign[i] : null;
          return [
            <button
              key={`l-${l}`}
              type="button"
              disabled={disabled}
              aria-describedby="match-left"
              aria-pressed={active === i}
              onClick={() => setActive(i)}
              className={cell}
              style={{ borderColor: ok === null ? (active === i ? 'var(--ink)' : 'var(--line)') : ok ? 'var(--ok)' : 'var(--ko)' }}
            >
              {badge(assign[i] !== undefined ? i : undefined)}
              <span lang="ja" className="jp min-w-0 flex-1 break-all text-lg leading-tight sm:text-2xl">{l}</span>
            </button>,
            <button
              key={`r-${r}`}
              type="button"
              data-match="right"
              disabled={disabled || active === null}
              aria-describedby="match-right"
              onClick={() => choose(r)}
              className={`${cell} disabled:cursor-default`}
              style={{ borderColor: pairNo.has(r) ? 'var(--ink-soft)' : 'var(--line)' }}
            >
              {badge(pairNo.get(r))}
              <span className="min-w-0 flex-1 text-sm leading-tight sm:text-base">{r}</span>
            </button>,
          ];
        })}
      </div>
      {expected && expected.some((e, i) => e !== assign[i]) && (
        <ul className="rounded-2xl bg-surface-2 p-3 text-sm">
          {pairs.left.map((l, i) => (
            <li key={l} className="grid grid-cols-[1fr_auto_1fr] gap-2">
              <span lang="ja" className="jp text-right">{l}</span>
              <span aria-hidden="true">=</span>
              <span className={expected[i] === assign[i] ? '' : 'font-bold text-ko'}>{expected[i]}</span>
            </li>
          ))}
        </ul>
      )}
      {!result && (
        <button className="btn btn-primary self-stretch sm:self-end" disabled={disabled || !complete} onClick={() => onSubmit(pairs.left.map((_, i) => assign[i]))}>{T("Vérifier")}</button>
      )}
    </div>
  );
}
