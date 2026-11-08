import { useCallback, useEffect, useRef, useState } from 'react';
import { Link, useNavigate, useParams } from 'react-router';
import { useQuery, useQueryClient } from '@tanstack/react-query';
import type { AnswerResultDto, GameInfoDto, GameResultDto, GameStartDto, GamesDto, IssuedQuestionDto } from '@koto/shared';
import { api, post } from '../api/client';
import { ErrorBox, Jp, PageTitle, Spinner } from '../components/ui';
import { speak, speechSupported } from '../lib/speech';
import { Coins } from './Character';
import { Confetti, CountUp, Stamp } from '../components/Celebrate';
import { T } from '../i18n';

const GLYPH: Record<GameInfoDto['id'], string> = { 'kanji-rush': '速', speed: '走', listening: '耳' };
const KIND_HINT: Record<GameInfoDto['id'], string> = { 'kanji-rush': 'kanji', speed: 'notions', listening: T("kana ou mots") };

const useGames = () => useQuery({ queryKey: ['games'], queryFn: () => api<GamesDto>('/games') });

export function GamesPage() {
  const { data, isLoading, error, refetch } = useGames();
  if (isLoading) return <Spinner />;
  if (error || !data) return <ErrorBox error={error} onRetry={refetch} />;
  return (
    <div>
      <PageTitle sub={T("Une minute chrono sur les notions que tu as déjà rencontrées. Les mini-jeux entraînent tes réflexes sans modifier tes révisions.")}>{T("Mini-jeux")}</PageTitle>
      <ul className="grid gap-4 sm:grid-cols-3">
        {data.games.map((g) => (
          <li key={g.id} className="flex flex-col gap-3 rounded-3xl border border-line bg-surface p-5">
            <span aria-hidden="true" className="jp flex h-14 w-14 items-center justify-center rounded-2xl text-3xl font-black" style={{ background: g.available ? 'var(--ink)' : 'var(--surface-2)', color: g.available ? 'var(--paper)' : 'var(--ink-soft)' }}>
              {GLYPH[g.id]}
            </span>
            <h2 className="text-xl">{g.title}</h2>
            <p className="flex-1 text-ink-soft">{g.description}</p>
            {g.available ? (
              <>
                <p className="text-sm">{g.plays > 0 ? <>{T("Record :")}{' '}<strong>{g.bestScore}</strong>, {g.plays}{' '}{T("partie")}{g.plays > 1 ? 's' : ''}</> : T("Jamais joué")}</p>
                <Link to={`/games/${g.id}`} className="btn btn-gold">{T("Jouer")}</Link>
              </>
            ) : (
              <p className="rounded-2xl bg-surface-2 p-3 text-sm">{T("Débloqué après avoir rencontré {0} {1} ({2}/{3}). Continue tes leçons ou l’onglet Caractères.", [ g.minItems , KIND_HINT[g.id] , g.seenItems , g.minItems ])}</p>
            )}
          </li>
        ))}
      </ul>
      <p className="mt-6 flex flex-wrap items-center gap-2 text-sm text-ink-soft">{T("Une pièce toutes les 5 bonnes réponses, dans la limite de 15 par jour. Encore aujourd’hui :")}{' '}<Coins value={data.coinsLeftToday} className="text-gold-ink" />
      </p>
    </div>
  );
}

type Stage = { kind: 'intro' } | { kind: 'countdown'; game: GameStartDto } | { kind: 'play'; game: GameStartDto; startedAt: number } | { kind: 'finishing' } | { kind: 'done'; result: GameResultDto; info: GameInfoDto };

export function GamePlayPage() {
  const { id = '' } = useParams();
  const { data, isLoading } = useGames();
  const [stage, setStage] = useState<Stage>({ kind: 'intro' });
  const [error, setError] = useState<unknown>(null);
  const qc = useQueryClient();

  const start = async () => {
    setError(null);
    try {
      const game = await post<GameStartDto>(`/games/${id}/start`);
      setStage({ kind: 'countdown', game });
    } catch (e) {
      setError(e);
    }
  };

  const finish = useCallback(
    async (game: GameStartDto) => {
      setStage({ kind: 'finishing' });
      // Le serveur n'accepte la fin qu'une fois le temps écoulé : on réessaie brièvement si l'horloge est un peu en avance.
      for (let attempt = 0; attempt < 5; attempt++) {
        try {
          const result = await post<GameResultDto>(`/games/${id}/finish`, { sessionId: game.sessionId });
          setStage({ kind: 'done', result, info: game.game });
          qc.invalidateQueries();
          return;
        } catch (e) {
          if (attempt === 4) setError(e);
          else await new Promise((r) => setTimeout(r, 800));
        }
      }
    },
    [id, qc],
  );

  if (isLoading) return <Spinner />;
  const info = data?.games.find((g) => g.id === id);
  if (!info) return <ErrorBox error={new Error(T("Mini-jeu inconnu."))} />;
  if (error) return <div className="flex flex-col gap-4"><ErrorBox error={error} /><Link to="/games" className="underline">{T("Retour aux mini-jeux")}</Link></div>;

  if (stage.kind === 'countdown') return <Countdown onDone={() => setStage({ kind: 'play', game: stage.game, startedAt: Date.now() })} />;
  if (stage.kind === 'play') return <Play game={stage.game} startedAt={stage.startedAt} onEnd={() => finish(stage.game)} />;
  if (stage.kind === 'finishing') return <Spinner label={T("Calcul du score…")} />;
  if (stage.kind === 'done') return <Result info={stage.info} result={stage.result} onAgain={start} />;
  return (
    <div className="flex flex-col items-center gap-5 py-8 text-center">
      <Link to="/games" className="self-start text-ink-soft underline">{T("← Mini-jeux")}</Link>
      <span aria-hidden="true" className="jp flex h-28 w-28 items-center justify-center rounded-3xl bg-ink text-6xl font-black text-paper">{GLYPH[info.id]}</span>
      <h1 className="text-4xl">{info.title}</h1>
      <p className="max-w-[44ch] text-lg">{info.description}</p>
      <ul className="text-ink-soft">
        <li>{T("{0} secondes, pas de pause.", [info.durationSec ])}</li>
        <li>{T("Touche une réponse (ou les touches 1 à 4) : la suivante arrive aussitôt.")}</li>
        {info.id === 'listening' && !speechSupported() && <li className="font-bold text-ko">{T("Ce navigateur ne peut pas lire l’audio japonais.")}</li>}
      </ul>
      {info.plays > 0 && <p>{T("Ton record :")}{' '}<strong>{info.bestScore}</strong></p>}
      {info.available ? (
        <button className="btn btn-gold min-h-14 px-10 text-lg" onClick={start}>{T("C’est parti")}</button>
      ) : (
        <p className="rounded-2xl bg-surface-2 p-4">{T("Rencontre au moins {0} {1} pour débloquer ce jeu ({2}/{3}).", [ info.minItems , KIND_HINT[info.id] , info.seenItems , info.minItems ])}</p>
      )}
    </div>
  );
}

function Countdown({ onDone }: { onDone: () => void }) {
  const [n, setN] = useState(3);
  useEffect(() => {
    if (n === 0) {
      onDone();
      return;
    }
    const t = setTimeout(() => setN(n - 1), 700);
    return () => clearTimeout(t);
  }, [n, onDone]);
  return (
    <div className="flex min-h-[60dvh] items-center justify-center" role="status" aria-live="assertive">
      <span className="font-display text-9xl">{n || T("Go")}</span>
    </div>
  );
}

function Play({ game, startedAt, onEnd }: { game: GameStartDto; startedAt: number; onEnd: () => void }) {
  const duration = game.game.durationSec * 1000;
  const [now, setNow] = useState(Date.now());
  const [index, setIndex] = useState(0);
  const [score, setScore] = useState(0);
  const [combo, setCombo] = useState(0);
  const [flash, setFlash] = useState<{ choice: string; correct: boolean; answer: string } | null>(null);
  const ended = useRef(false);
  const shownAt = useRef(performance.now());
  const navigate = useNavigate();
  const q: IssuedQuestionDto | undefined = game.questions[index];
  const left = Math.max(0, duration - (now - startedAt));

  const end = useCallback(() => {
    if (ended.current) return;
    ended.current = true;
    onEnd();
  }, [onEnd]);

  useEffect(() => {
    const t = setInterval(() => setNow(Date.now()), 100);
    return () => clearInterval(t);
  }, []);
  useEffect(() => {
    if (left <= 0 || !q) end();
  }, [left, q, end]);
  useEffect(() => {
    shownAt.current = performance.now();
    if (q?.type === 'listening_choice' && q.audio) speak(q.audio);
  }, [q?.id, q?.type, q?.audio]);

  async function pick(choice: string) {
    if (!q || flash || ended.current) return;
    const responseMs = Math.round(performance.now() - shownAt.current);
    setFlash({ choice, correct: false, answer: '' });
    try {
      const r = await post<AnswerResultDto>(`/questions/${q.id}/answer`, { answer: choice, responseMs });
      setFlash({ choice, correct: r.correct, answer: Array.isArray(r.correctAnswer) ? r.correctAnswer.join('') : r.correctAnswer });
      if (r.correct) {
        setScore((s) => s + 1);
        setCombo((c) => c + 1);
      } else setCombo(0);
      setTimeout(() => {
        setFlash(null);
        setIndex((i) => i + 1);
      }, r.correct ? 220 : 650);
    } catch {
      setFlash(null);
      setIndex((i) => i + 1);
    }
  }

  useEffect(() => {
    const onKey = (e: KeyboardEvent) => {
      const n = Number(e.key);
      if (q?.choices && n >= 1 && n <= q.choices.length) pick(q.choices[n - 1]);
    };
    window.addEventListener('keydown', onKey);
    return () => window.removeEventListener('keydown', onKey);
  });

  if (!q) return <Spinner label={T("Fin de la partie…")} />;
  const d = q.display ?? {};
  return (
    <div className="flex flex-col gap-5" data-testid="game" data-qid={q.id}>
      <div className="flex items-center gap-4">
        <button className="rounded-full p-2 text-ink-soft hover:bg-surface-2" aria-label={T("Abandonner la partie")} onClick={() => navigate('/games')}>
          <svg width="22" height="22" viewBox="0 0 24 24" aria-hidden="true"><path d="M6 6l12 12M18 6L6 18" stroke="currentColor" strokeWidth="2.5" strokeLinecap="round" /></svg>
        </button>
        <div className="h-3 flex-1 overflow-hidden rounded-full bg-surface-2" role="timer" aria-label={`${Math.ceil(left / 1000)} secondes restantes`}>
          <div className="h-full rounded-full transition-[width] duration-100 ease-linear" style={{ width: `${(left / duration) * 100}%`, background: left < 10_000 ? 'var(--ko)' : 'var(--ink)' }} />
        </div>
        <span className="w-10 shrink-0 text-right font-bold tabular-nums">{Math.ceil(left / 1000)} s</span>
      </div>
      <div className="flex items-baseline justify-between">
        <p className="text-lg">{T("Score :")}{' '}<strong className="text-2xl tabular-nums" data-testid="score">{score}</strong></p>
        {combo >= 3 && <p className="font-bold text-gold-ink">{T("Série × {0}", [ combo])}</p>}
      </div>
      <p className="font-bold">{q.prompt}</p>
      <div className="relative flex min-h-36 items-center justify-center rounded-3xl bg-surface-2 p-6 text-center">
        {q.type === 'listening_choice' ? (
          <button className="btn btn-quiet min-h-14 px-6 text-lg" onClick={() => q.audio && speak(q.audio)}>{T("Réécouter")}</button>
        ) : d.jp ? (
          <Jp text={d.jp} furigana={false} className={`${[...d.jp].length <= 2 ? 'text-7xl' : 'text-5xl'} font-bold`} />
        ) : (
          <p className="text-2xl font-bold">{d.text}</p>
        )}
      </div>
      <div role="group" aria-label={T("Réponses")} className="grid grid-cols-2 gap-3">
        {q.choices?.map((c, i) => {
          const isPicked = flash?.choice === c;
          const isAnswer = flash?.answer === c;
          const bg = flash?.answer ? (isAnswer ? 'var(--ok-bg)' : isPicked ? 'var(--ko-bg)' : 'var(--surface)') : 'var(--surface)';
          const border = flash?.answer ? (isAnswer ? 'var(--ok)' : isPicked ? 'var(--ko)' : 'var(--line)') : 'var(--line)';
          const jp = /[぀-ヿ一-龯]/.test(c);
          return (
            <button key={c} type="button" disabled={!!flash} onClick={() => pick(c)} className="relative flex min-h-20 items-center justify-center rounded-2xl border-2 px-2 text-center" style={{ background: bg, borderColor: border }}>
              <kbd className="absolute left-2 top-2 hidden h-6 w-6 items-center justify-center rounded-md border border-line text-xs text-ink-soft sm:flex">{i + 1}</kbd>
              <span lang={jp ? 'ja' : 'fr'} className={jp ? 'jp text-3xl' : 'text-lg font-bold'}>{c}</span>
            </button>
          );
        })}
      </div>
    </div>
  );
}

function Result({ info, result, onAgain }: { info: GameInfoDto; result: GameResultDto; onAgain: () => void }) {
  return (
    <div className="flex flex-col items-center gap-4 py-8 text-center">
      {result.newBest && result.score > 0 && <Confetti />}
      <Stamp className="jp text-6xl font-black text-ko">{result.newBest ? '新記録' : '終了'}</Stamp>
      <h1 className="text-4xl">{result.newBest ? T("Nouveau record !") : T("Partie terminée")}</h1>
      <p className="font-display text-7xl tabular-nums"><CountUp value={result.score} /></p>
      <p className="text-ink-soft">{T("bonne{0} réponse{1} sur {2}, record : {3}", [ result.score > 1 ? 's' : '' , result.score > 1 ? 's' : '' , result.answered , result.bestScore ])}</p>
      <p className="flex items-center gap-3 font-bold text-gold-ink">
        +{result.xpGained}{' '}{T("XP")}{' '}{result.coinsGained > 0 && <Coins value={result.coinsGained} />}
      </p>
      <div className="flex flex-wrap justify-center gap-3">
        <button className="btn btn-gold" onClick={onAgain}>{T("Rejouer à {0}", [ info.title])}</button>
        <Link to="/games" className="btn btn-quiet">{T("Autres mini-jeux")}</Link>
      </div>
    </div>
  );
}
