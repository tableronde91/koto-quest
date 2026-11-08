import { useState } from 'react';
import { Link, useNavigate, useParams } from 'react-router';
import { useQueryClient } from '@tanstack/react-query';
import type { LessonCompletionDto, LessonDto, MeDto, SessionDto } from '@koto/shared';
import { post } from '../api/client';
import { useLesson } from '../api/hooks';
import { QuizRunner, RunSummary } from '../components/QuizRunner';
import { ErrorBox, Jp, SpeakButtons, Spinner } from '../components/ui';
import { KIND_LABEL, MASTERY_LABEL } from '../lib/format';
import { Avatar } from '../components/Avatar';
import { Cheer, Confetti, Stamp } from '../components/Celebrate';
import { T } from '../i18n';

type Stage = 'intro' | 'exercises' | 'completing' | 'mini' | 'done';

export function LessonPage({ me }: { me: MeDto }) {
  const { slug = '' } = useParams();
  const { data: lesson, isLoading, error } = useLesson(slug);
  const [stage, setStage] = useState<Stage>('intro');
  const [session, setSession] = useState<SessionDto | null>(null);
  const [completion, setCompletion] = useState<LessonCompletionDto | null>(null);
  const [miniSummary, setMiniSummary] = useState<RunSummary | null>(null);
  const [err, setErr] = useState<string | null>(null);
  const [furigana, setFurigana] = useState(me.preferences.showFurigana);
  const qc = useQueryClient();
  const navigate = useNavigate();

  if (isLoading) return <Spinner />;
  if (error || !lesson)
    return (
      <div className="flex flex-col gap-4">
        <ErrorBox error={error} />
        <Link to="/path" className="underline">{T("Retour au parcours")}</Link>
      </div>
    );

  async function start() {
    setErr(null);
    try {
      setSession(await post<SessionDto>(`/lessons/${slug}/start`));
      setStage('exercises');
    } catch (e) {
      setErr(e instanceof Error ? e.message : T("Erreur"));
    }
  }

  async function complete() {
    setStage('completing');
    try {
      const c = await post<LessonCompletionDto>(`/lessons/${slug}/complete`, { sessionId: session!.sessionId });
      setCompletion(c);
      setStage(c.miniReview.length ? 'mini' : 'done');
      qc.invalidateQueries();
    } catch (e) {
      setErr(e instanceof Error ? e.message : T("Erreur"));
      setStage('exercises');
    }
  }

  // Réserve la place des furigana sur toutes les cartes seulement si l'une d'elles en affiche.
  const rubyRow = furigana && lesson.items.some((it) => it.kind !== 'kana' && it.reading && it.reading !== it.front && /[\u4e00-\u9faf]/.test(it.front));

  const quit = () => {
    if (confirm(T("Quitter la leçon ? Tes réponses déjà données sont enregistrées."))) navigate('/path');
  };

  if (stage === 'exercises' && session) return <QuizRunner questions={session.questions} furigana={furigana} onFinish={complete} onQuit={quit} />;
  if (stage === 'completing') return <Spinner label={T("Validation de la leçon…")} />;
  if (stage === 'mini' && completion)
    return (
      <div className="flex flex-col gap-4">
        <div className="rounded-2xl bg-surface-2 p-4">
          <p className="font-bold">{T("Mini-révision")}</p>
          <p className="text-ink-soft">{T("Quelques questions sous une autre forme pour vérifier que c’est bien ancré.")}</p>
        </div>
        <QuizRunner questions={completion.miniReview} furigana={furigana} onFinish={(s) => { setMiniSummary(s); setStage('done'); qc.invalidateQueries(); }} />
      </div>
    );
  if (stage === 'done' && completion) return <LessonDone lesson={lesson} completion={completion} mini={miniSummary} avatar={me.avatar} />;

  return (
    <article className="flex flex-col gap-7">
      <div className="flex items-center justify-between gap-3">
        <Link to="/path" className="text-ink-soft underline">← {lesson.world.title}</Link>
        <label className="flex items-center gap-2 text-sm">
          <input type="checkbox" checked={furigana} onChange={(e) => setFurigana(e.target.checked)} className="h-5 w-5 accent-[var(--ink)]" />{T("Afficher les furigana")}</label>
      </div>
      <header>
        <p className="text-ink-soft">{T("{0} · {1} min", [lesson.chapter.title , lesson.minutes ])}</p>
        <h1 className="jp mt-1 text-4xl">{lesson.title}</h1>
        <p className="mt-3 rounded-2xl border-l-4 border-gold bg-surface px-4 py-3"><strong>{T("Objectif :")}</strong> {lesson.objective}</p>
      </header>

      <section className="flex max-w-[68ch] flex-col gap-3 text-lg">
        {lesson.explanation.map((p, i) => <p key={i}>{p}</p>)}
      </section>

      <section aria-labelledby="items-title" data-ruby={rubyRow ? '1' : undefined}>
        <h2 id="items-title" className="text-xl">{T("À retenir")}</h2>
        <ul className="mt-3 grid grid-cols-2 gap-3 sm:grid-cols-3">
          {lesson.items.map((it) => (
            <ItemCard key={it.id} item={it} furigana={furigana} reserveRuby={rubyRow} />
          ))}
        </ul>
      </section>

      {lesson.examples.length > 0 && (
        <section aria-labelledby="ex-title">
          <h2 id="ex-title" className="text-xl">{T("Exemples")}</h2>
          <ul className="mt-3 flex flex-col gap-3">
            {lesson.examples.map((e, i) => (
              <li key={i} className="flex flex-col gap-3 rounded-2xl border border-line bg-surface p-4 sm:flex-row sm:items-center sm:justify-between">
                <div className="min-w-0">
                  {/* Phrase entière : la lecture va sur sa propre ligne plutôt qu'au-dessus de toute la phrase. */}
                  <Jp text={e.jp} furigana={false} className="text-2xl" />
                  {furigana && e.reading && e.reading !== e.jp && <p lang="ja" className="jp text-sm text-ink-soft">{e.reading}</p>}
                  <p className="text-ink-soft">{e.fr}</p>
                </div>
                <SpeakButtons text={e.reading ?? e.jp} />
              </li>
            ))}
          </ul>
        </section>
      )}

      {err && <ErrorBox error={new Error(err)} />}
      <div className="sticky bottom-0 -mx-4 flex justify-end border-t border-line bg-paper/95 px-4 py-3 backdrop-blur sm:-mx-8 sm:px-8">
        <button className="btn btn-gold min-h-14 w-full px-8 text-lg sm:w-auto" onClick={start}>
          {lesson.status === 'completed' ? T("Refaire les exercices") : T("Passer aux exercices")}
        </button>
      </div>
    </article>
  );
}

function ItemCard({ item, furigana, reserveRuby }: { item: LessonDto['items'][number]; furigana: boolean; reserveRuby: boolean }) {
  const audio = item.kind === 'grammar' ? null : item.reading ?? item.front;
  return (
    <li className="flex flex-col gap-1 rounded-2xl border border-line bg-surface p-4">
      <span className="truncate text-xs text-ink-soft">{KIND_LABEL[item.kind]}{item.mastery ? `, ${MASTERY_LABEL[item.mastery]}` : ''}</span>
      {/* Zone de hauteur fixe, alignée en bas : glyphes et furigana restent sur la même ligne d'une carte à l'autre. */}
      <button type="button" className={`flex items-end text-left ${reserveRuby ? 'h-16' : 'mt-1'}`} onClick={() => audio && import('../lib/speech').then((m) => m.speak(audio))} aria-label={T("Écouter {0}", [item.front])} disabled={!audio}>
        <Jp text={item.front} reading={item.kind === 'kana' ? null : item.reading} furigana={furigana} className={`${[...item.front].length <= 2 ? 'text-5xl' : 'text-2xl sm:text-3xl'} font-bold leading-tight`} />
      </button>
      <span className="font-bold">{item.meaning}</span>
      {item.kind !== 'kana' && item.romaji && <span className="text-sm text-ink-soft">{item.romaji}</span>}
      {item.kanji && (
        <span className="text-sm text-ink-soft">{T("On :")}{' '}<span className="jp">{item.kanji.onyomi.join('、')}</span>
          <br />{T("Kun :")}{' '}<span className="jp">{item.kanji.kunyomi.join('、') || '—'}</span>
        </span>
      )}
    </li>
  );
}

function LessonDone({ lesson, completion, mini, avatar }: { lesson: LessonDto; completion: LessonCompletionDto; mini: RunSummary | null; avatar: MeDto['avatar'] }) {
  return (
    <div className="flex flex-col items-start gap-6 py-6">
      <Confetti count={completion.perfect ? 60 : 36} />
      <div className="flex items-end gap-4">
        <Cheer><Avatar config={avatar} size={110} /></Cheer>
      <Stamp className="jp text-8xl font-black text-ko">{completion.perfect ? '満点' : '完了'}</Stamp>
      </div>
      <h1 className="text-4xl">{completion.perfect ? T("Sans faute !") : T("Leçon terminée")}</h1>
      <p className="text-lg">
        <span className="jp">{lesson.title}</span> : {completion.correct}/{completion.total}{' '}{T("bonnes réponses (")}{completion.score} %)
        {mini && T(", mini-révision {0}/{1}", [mini.correct, mini.total])}.
      </p>
      <p className="text-lg font-bold text-gold-ink">{T("{0}+{1} XP de fin de leçon{2}", [completion.coinsGained > 0 && T("+{0} pièces, ", [completion.coinsGained]) , completion.xpGained , mini ? T(", +{0} XP de mini-révision", [mini.xp]) : ''])}</p>
      <p className="max-w-[55ch] text-ink-soft">{T("Ces notions reviendront dans quelques heures sous forme de défi, puis de plus en plus espacées à mesure que tu les retiens.")}</p>
      <div className="flex flex-wrap gap-3">
        {completion.nextLessonSlug && <Link to={`/lesson/${completion.nextLessonSlug}`} className="btn btn-gold">{T("Leçon suivante")}</Link>}
        <Link to="/" className="btn btn-quiet">{T("Retour à l’accueil")}</Link>
      </div>
    </div>
  );
}
