import { useEffect, useRef, useState } from 'react';
import { Link, useNavigate, useParams } from 'react-router';
import { motion } from 'motion/react';
import { useQuery, useQueryClient } from '@tanstack/react-query';
import { rubySegments } from '@koto/learning-engine';
import type { BiText, MeDto, ReadingChapterDto, ReadingChapterRefDto, ReadingOverviewDto, ReadingResultDto, ReadingSentenceDto, ReadingStoryInfoDto, ReadingTitle } from '@koto/shared';
import { api, post } from '../api/client';
import { ErrorBox, PageTitle, ProgressBar, SoundIcon, Spinner } from '../components/ui';
import { Confetti, Flame, Stamp, useCalm } from '../components/Celebrate';
import { say, speechSupported, stopSpeech } from '../lib/speech';
import { T, locale } from '../i18n';
import { langOf } from '../lib/format';
import { languageOfLevel, levelLabel } from '@koto/shared';
import { studyWords } from '../components/StudyLanguage';

/** Texte dans la langue de l'interface (les contes sont rédigés en français et en anglais). */
const bi = (b: BiText) => (locale === 'en' ? b.en : b.fr);
const minutes = (chars: number) => Math.max(1, Math.round(chars / 120));

export const useReading = () => useQuery({ queryKey: ['reading'], queryFn: () => api<ReadingOverviewDto>('/reading') });

/** Japonais avec furigana notés {漢字|かな}. */
export function Ruby({ text, furigana, className = '' }: { text: string; furigana: boolean; className?: string }) {
  return (
    <span lang={langOf(text)} className={`jp ${className}`}>
      {rubySegments(text).map((s, i) =>
        s.ruby && furigana ? (
          <ruby key={i}>
            {s.text}
            <rp>(</rp>
            <rt>{s.ruby}</rt>
            <rp>)</rp>
          </ruby>
        ) : (
          <span key={i}>{s.text}</span>
        ),
      )}
    </span>
  );
}

function StoryGlyph({ story, size = 'md' }: { story: ReadingStoryInfoDto; size?: 'sm' | 'md' | 'lg' }) {
  const cls = size === 'lg' ? 'h-20 w-20 text-5xl rounded-3xl' : size === 'sm' ? 'h-10 w-10 text-xl rounded-xl' : 'h-14 w-14 text-3xl rounded-2xl';
  return (
    <span aria-hidden="true" lang="ja" className={`jp flex shrink-0 items-center justify-center font-black text-white shadow-sm ${cls}`} style={{ background: story.color }}>
      {story.glyph}
    </span>
  );
}

function ChapterMeta({ c }: { c: ReadingChapterRefDto }) {
  return <>{T('{0} phrases · {1} caractères · ≈ {2} min', [c.sentences, c.chars, minutes(c.chars)])}</>;
}

/** Bibliothèque et chapitre du jour (/lecture). */
export function ReadingPage() {
  const { data, isLoading, error, refetch } = useReading();
  const navigate = useNavigate();
  if (isLoading) return <Spinner />;
  if (error || !data) return <ErrorBox error={error} onRetry={refetch} />;
  const { today, upcoming } = data;
  const words = studyWords(languageOfLevel(data.stories[0]?.level));
  // Chapitre mis en avant dans la bibliothèque : le prochain à lire (tout reste ouvert).
  const suggested = today.state === 'new' ? today.chapter?.slug : upcoming?.slug;

  return (
    <div className="flex flex-col gap-6">
      <PageTitle sub={words.en ? T('Des contes et légendes en anglais à lire à ton rythme : tous les chapitres sont ouverts, du plus simple au plus long. Lire un peu tous les jours est l’un des meilleurs moyens de progresser.') : words.ko ? T('Des contes coréens à lire à ton rythme : tous les chapitres sont ouverts, du plus simple au plus long. Lire un peu tous les jours est l’un des meilleurs moyens de progresser.') : T('Des contes japonais à lire à ton rythme : tous les chapitres sont ouverts, du plus simple au plus long. Lire un peu tous les jours est l’un des meilleurs moyens de progresser.')}>{T('Lecture')}</PageTitle>

      {/* Chapitre du jour */}
      <section aria-label={T('Chapitre du jour')} className="relative overflow-hidden rounded-3xl bg-ink p-5 text-paper sm:p-7">
        <span aria-hidden="true" lang="ja" className="jp pointer-events-none absolute -right-4 -top-8 select-none text-[11rem] font-black leading-none opacity-[0.07]">読</span>
        {today.chapter && today.story ? (
          <div className="relative flex flex-col gap-5 sm:flex-row sm:items-center">
            <StoryGlyph story={today.story} size="lg" />
            <div className="flex-1">
              <p className="text-sm font-bold uppercase tracking-wide text-gold">
                {today.state === 'new' ? T('Conseillé aujourd’hui') : T('Lu aujourd’hui')}
              </p>
              <h2 className="mt-1 text-2xl sm:text-3xl">
                <Ruby text={today.chapter.title.jp} furigana className="mr-2" />
                <span className="font-normal opacity-85">· {bi(today.chapter.title)}</span>
              </h2>
              <p className="mt-1 opacity-85">{bi(today.story.title)}</p>
              <p className="mt-1 text-sm opacity-75"><ChapterMeta c={today.chapter} /></p>
              {today.state === 'done' && upcoming && (
                <p className="mt-3 max-w-[52ch]">
                  {T('Bravo ! Envie de continuer ? La suite, « {0} », t’attend.', [bi(upcoming.title)])}
                </p>
              )}
            </div>
            <div className="flex flex-col gap-2">
              {today.state === 'done' && upcoming && (
                <button className="btn btn-gold min-h-14 px-6 text-lg" onClick={() => navigate(`/lecture/${upcoming.slug}`)}>{T('Continuer la lecture')}</button>
              )}
              <button className={`btn px-6 ${today.state === 'new' ? 'btn-gold min-h-14 text-lg' : 'min-h-11 border-2'}`}
                style={today.state === 'new' ? undefined : { background: 'transparent', color: 'var(--paper)', borderColor: 'currentColor' }} onClick={() => navigate(`/lecture/${today.chapter!.slug}`)}>
                {today.state === 'new' ? T('Lire le chapitre du jour') : T('Relire')}
              </button>
            </div>
          </div>
        ) : (
          <div className="relative">
            <h2 className="text-2xl">{T('Tu as lu tous les contes !')}</h2>
            <p className="mt-1 opacity-85">{T('Relis tes préférés : chaque relecture rend la lecture plus fluide.')}</p>
          </div>
        )}
      </section>

      {/* Statistiques */}
      <dl className="grid grid-cols-3 gap-3">
        <div className="flex flex-col items-start gap-1 rounded-2xl border border-line bg-surface p-4">
          <dt className="text-sm text-ink-soft">{T('Jours d’affilée')}</dt>
          <dd className="flex items-center gap-2 text-2xl font-bold"><Flame lit={data.streak > 0} />{data.streak}</dd>
        </div>
        <div className="flex flex-col gap-1 rounded-2xl border border-line bg-surface p-4">
          <dt className="text-sm text-ink-soft">{T('Chapitres lus')}</dt>
          <dd className="text-2xl font-bold">{data.chaptersRead}<span className="text-base font-normal text-ink-soft">/{data.totalChapters}</span></dd>
        </div>
        <div className="flex flex-col gap-1 rounded-2xl border border-line bg-surface p-4">
          <dt className="text-sm text-ink-soft">{T('Caractères lus')}</dt>
          <dd className="text-2xl font-bold">{data.charsRead.toLocaleString(locale === 'en' ? 'en-GB' : 'fr-FR')}</dd>
        </div>
      </dl>

      {/* Bibliothèque */}
      <section aria-labelledby="library" className="flex flex-col gap-4">
        <h2 id="library" className="text-2xl">{T('Les contes')}</h2>
        {data.stories.map((s, i) => (
          <motion.article key={s.slug} initial={{ opacity: 0, y: 8 }} animate={{ opacity: 1, y: 0 }} transition={{ delay: Math.min(0.3, i * 0.05) }} className="rounded-3xl border border-line bg-surface p-5" data-testid="story">
            <div className="flex items-start gap-4">
              <StoryGlyph story={s} />
              <div className="min-w-0 flex-1">
                <div className="flex flex-wrap items-center gap-2">
                  <h3 className="text-xl"><Ruby text={s.title.jp} furigana={false} /></h3>
                  <span className="rounded-full bg-surface-2 px-2.5 py-0.5 text-xs font-bold">{levelLabel(s.level)}</span>
                  {s.read === s.chapters.length && <span className="rounded-full bg-ok-bg px-2.5 py-0.5 text-xs font-bold">{T('Terminé')}</span>}
                </div>
                <p className="font-bold">{bi(s.title)}</p>
                <p className="text-ink-soft">{bi(s.summary)}</p>
              </div>
            </div>
            <ol className="mt-4 flex flex-wrap gap-2">
              {s.chapters.map((c, k) => {
                const label = T('Chapitre {0} : {1}', [k + 1, bi(c.title)]);
                const inner = (
                  <>
                    <span aria-hidden="true" className="font-bold">{c.state === 'read' ? '✓' : '●'}</span>
                    <span>{k + 1}. {bi(c.title)}</span>
                  </>
                );
                const base = 'flex min-h-10 items-center gap-2 rounded-xl border-2 px-3 text-sm';
                return (
                  <li key={c.slug}>
                    <Link to={`/lecture/${c.slug}`} aria-label={c.slug === suggested ? `${label} (${T('conseillé')})` : label} aria-current={c.slug === suggested ? 'step' : undefined} className={`${base} ${c.slug === suggested ? 'border-gold bg-gold/15 font-bold' : 'border-line hover:border-ink-soft'}`}>{inner}</Link>
                  </li>
                );
              })}
            </ol>
          </motion.article>
        ))}
        <p className="text-sm text-ink-soft">{bi(data.notice)}</p>
      </section>
    </div>
  );
}

type TranslationMode = 'tap' | 'all' | 'none';

/** Liseuse d'un chapitre (/lecture/:slug). */
export function ReadingChapterPage({ me }: { me: MeDto }) {
  const { slug = '' } = useParams();
  const { data, isLoading, error, refetch } = useQuery({ queryKey: ['reading', slug], queryFn: () => api<ReadingChapterDto>(`/reading/chapters/${slug}`) });
  const [furigana, setFurigana] = useState(me.preferences.showFurigana);
  const [mode, setMode] = useState<TranslationMode>('tap');
  const [shown, setShown] = useState<Set<string>>(new Set());
  const [playing, setPlaying] = useState<string | null>(null);
  const [answers, setAnswers] = useState<(number | null)[]>([]);
  const [result, setResult] = useState<ReadingResultDto | null>(null);
  const [sending, setSending] = useState(false);
  const [sendError, setSendError] = useState<unknown>(null);
  const started = useRef(Date.now());
  const qc = useQueryClient();
  const calm = useCalm();

  useEffect(() => {
    started.current = Date.now();
    setAnswers([]);
    setResult(null);
    setShown(new Set());
    return () => stopSpeech();
  }, [slug]);

  if (isLoading) return <Spinner />;
  if (error || !data) return <ErrorBox error={error} onRetry={refetch} />;
  const { story, chapter } = data;
  const sentences = chapter.paragraphs.flatMap((p, i) => p.map((s, j) => ({ s, id: `${i}-${j}` })));

  /** Lecture à voix haute, phrase par phrase, avec la phrase en cours surlignée. */
  const play = (from: number, single = false) => {
    const list = single ? [sentences[from]] : sentences.slice(from);
    say(list.map(({ s, id }) => ({ text: s.kana, rate: 0.85, onStart: () => setPlaying(id) })), () => setPlaying(null));
  };
  const stop = () => {
    stopSpeech();
    setPlaying(null);
  };

  const toggle = (id: string) =>
    setShown((prev) => {
      const next = new Set(prev);
      if (next.has(id)) next.delete(id);
      else next.add(id);
      return next;
    });

  const submit = async () => {
    setSending(true);
    setSendError(null);
    try {
      const r = await post<ReadingResultDto>(`/reading/chapters/${slug}/complete`, { answers, seconds: Math.round((Date.now() - started.current) / 1000) });
      setResult(r);
      qc.invalidateQueries();
    } catch (e) {
      setSendError(e);
    } finally {
      setSending(false);
    }
  };

  const solution = result?.answers ?? null;
  const complete = answers.length === chapter.questions.length && answers.every((a) => a !== null && a !== undefined);

  return (
    <article className="flex flex-col gap-6" data-testid="reader">
      <div className="flex flex-wrap items-center justify-between gap-2">
        <Link to="/lecture" className="text-ink-soft underline">← {T('Tous les contes')}</Link>
        <span className="rounded-full bg-surface-2 px-2.5 py-0.5 text-sm font-bold">{levelLabel(story.level)}</span>
      </div>

      <header className="flex items-center gap-4">
        <StoryGlyph story={story} />
        <div>
          <p className="text-sm text-ink-soft">{bi(story.title)} · {T('chapitre {0} sur {1}', [chapter.index, chapter.count])}</p>
          <h1 className="text-3xl sm:text-4xl"><Ruby text={chapter.title.jp} furigana={furigana} /></h1>
          <p className="text-lg text-ink-soft">{bi(chapter.title)}</p>
        </div>
      </header>

      {/* Réglages de lecture */}
      <div className="flex flex-wrap items-center gap-2 sm:sticky sm:top-0 sm:z-10 sm:rounded-2xl sm:border sm:border-line sm:bg-paper/95 sm:px-4 sm:py-2 sm:backdrop-blur">
        {languageOfLevel(story.level) === 'ja' && (
          <button type="button" aria-pressed={furigana} onClick={() => setFurigana(!furigana)} className={`min-h-10 rounded-xl border-2 px-3 text-sm font-bold ${furigana ? 'border-ink bg-ink text-paper' : 'border-line'}`}>
            <span lang="ja" className="jp">ふりがな</span> {furigana ? T('affichés') : T('masqués')}
          </button>
        )}
        <div role="radiogroup" aria-label={T('Traduction')} className="flex items-center rounded-xl border-2 border-line p-0.5 text-sm">
          <span className="px-2 font-bold text-ink-soft">{T('Traduction')}</span>
          {([['tap', T('au toucher')], ['all', T('tout')], ['none', T('aucune')]] as [TranslationMode, string][]).map(([m, label]) => (
            <button key={m} type="button" role="radio" aria-checked={mode === m} onClick={() => setMode(m)} className={`min-h-9 rounded-lg px-2.5 font-bold ${mode === m ? 'bg-surface-2' : 'text-ink-soft'}`}>
              {label}
            </button>
          ))}
        </div>
        {speechSupported() && (
          <button type="button" className="btn btn-quiet ml-auto min-h-10 px-3" onClick={() => (playing ? stop() : play(0))} aria-label={playing ? T('Arrêter') : T('Écouter le chapitre')}>
            <SoundIcon /> <span className="hidden sm:inline">{playing ? T('Arrêter') : T('Écouter le chapitre')}</span>
          </button>
        )}
      </div>

      {/* Texte */}
      <div className="flex flex-col gap-6 rounded-3xl bg-surface p-5 sm:p-8" style={{ borderTop: `6px solid ${story.color}` }}>
        {chapter.paragraphs.map((p, i) => (
          <div key={i} className="flex flex-col gap-3">
            {p.map((s, j) => {
              const id = `${i}-${j}`;
              const index = sentences.findIndex((x) => x.id === id);
              return (
                <Sentence
                  key={id}
                  s={s}
                  furigana={furigana}
                  translated={mode === 'all' || (mode === 'tap' && shown.has(id))}
                  tappable={mode === 'tap'}
                  active={playing === id}
                  onTap={() => toggle(id)}
                  onListen={() => play(index, true)}
                />
              );
            })}
          </div>
        ))}
      </div>

      {/* Vocabulaire */}
      <section aria-labelledby="words" className="flex flex-col gap-3">
        <h2 id="words" className="text-2xl">{T('Vocabulaire du chapitre')}</h2>
        <ul className="grid gap-2 sm:grid-cols-2 lg:grid-cols-3">
          {chapter.words.map((w) => (
            <li key={w.jp} className="flex flex-wrap items-baseline gap-x-3 gap-y-0.5 rounded-2xl border border-line bg-surface px-4 py-3">
              <span lang={langOf(w.jp)} className="jp whitespace-nowrap text-xl font-bold">{w.jp}</span>
              {w.reading && <span lang={langOf(w.reading)} className="jp whitespace-nowrap text-sm text-ink-soft">{w.reading}</span>}
              <span className="ml-auto text-right">{bi(w)}</span>
            </li>
          ))}
        </ul>
      </section>

      {/* Compréhension */}
      <section aria-labelledby="quiz" className="flex flex-col gap-4 rounded-3xl border-2 border-line p-5 sm:p-6">
        <div>
          <h2 id="quiz" className="text-2xl">{T('As-tu compris ?')}</h2>
          {data.state === 'read' && !result && <p className="text-ink-soft">{T('Déjà lu : relis et réponds autant que tu veux (sans récompense).')}</p>}
        </div>
        {chapter.questions.map((q, i) => (
          <fieldset key={i} className="flex flex-col gap-2" disabled={!!result}>
            <legend className="mb-1 font-bold">{i + 1}. {bi(q.q)}</legend>
            {q.choices.map((c, k) => {
              const picked = answers[i] === k;
              const right = solution && solution[i] === k;
              const wrong = solution && picked && solution[i] !== k;
              return (
                <label
                  key={k}
                  className={`flex min-h-12 cursor-pointer items-center gap-3 rounded-2xl border-2 px-4 py-2 ${right ? 'border-ok bg-ok-bg' : wrong ? 'border-ko bg-ko-bg' : picked ? 'border-ink' : 'border-line'}`}
                >
                  <input
                    type="radio"
                    name={`q${i}`}
                    checked={picked}
                    onChange={() =>
                      setAnswers((a) => {
                        const n = Array.from({ length: chapter.questions.length }, (_, x) => a[x] ?? null);
                        n[i] = k;
                        return n;
                      })
                    }
                    className="h-5 w-5 accent-[var(--ink)]"
                  />
                  <span className="flex-1">{bi(c)}</span>
                  {right && <span aria-label={T('Bonne réponse')}>✓</span>}
                  {wrong && <span aria-label={T('Mauvaise réponse')}>✗</span>}
                </label>
              );
            })}
          </fieldset>
        ))}
        {sendError ? <ErrorBox error={sendError} /> : null}
        {!result && (
          <button className="btn btn-primary self-start" disabled={!complete || sending} onClick={submit}>
            {sending ? T('Un instant…') : T('Valider mes réponses')}
          </button>
        )}
        {result && (
          <motion.div initial={{ opacity: 0, y: 8 }} animate={{ opacity: 1, y: 0 }} className="relative flex flex-col gap-3 overflow-hidden rounded-2xl bg-surface-2 p-5" role="status">
            {result.firstTime && result.correct === result.total && !calm && <Confetti count={24} origin="center" />}
            <div className="flex flex-wrap items-center gap-4">
              <Stamp className="jp text-6xl font-black text-ko">{result.correct === result.total ? '読' : '頑'}</Stamp>
              <div>
                <p className="text-2xl font-bold">{T('{0}/{1} bonnes réponses', [result.correct, result.total])}</p>
                {result.firstTime ? (
                  <p>{T('+{0} XP · +{1} pièces · {2} jour(s) de lecture d’affilée', [result.xpGained, result.coinsGained, result.streak])}</p>
                ) : (
                  <p className="text-ink-soft">{T('Relecture : pas de récompense, mais ta lecture devient plus fluide.')}</p>
                )}
              </div>
            </div>
            {result.next ? (
              <Link to={`/lecture/${result.next.slug}`} className="btn btn-gold self-start">{T('Chapitre suivant')}</Link>
            ) : (
              <p>{T('C’était le dernier chapitre. Bravo, tu as lu tous les contes !')}</p>
            )}
            <div className="flex flex-wrap gap-3">
              <button className="btn btn-quiet" onClick={() => { setResult(null); setAnswers([]); window.scrollTo({ top: 0, behavior: calm ? 'auto' : 'smooth' }); }}>{T('Relire le chapitre')}</button>
              <Link to="/lecture" className="btn btn-quiet">{T('Tous les contes')}</Link>
            </div>
          </motion.div>
        )}
      </section>

      <nav aria-label={T('Chapitres')} className="flex justify-between gap-3">
        {data.previous ? <Link to={`/lecture/${data.previous}`} className="btn btn-quiet">← {T('Chapitre précédent')}</Link> : <span />}
        {data.next && <Link to={`/lecture/${data.next.slug}`} className="btn btn-quiet">{T('Chapitre suivant')} →</Link>}
      </nav>
    </article>
  );
}

function Sentence({ s, furigana, translated, tappable, active, onTap, onListen }: { s: ReadingSentenceDto; furigana: boolean; translated: boolean; tappable: boolean; active: boolean; onTap: () => void; onListen: () => void }) {
  const text = <Ruby text={s.jp} furigana={furigana} className="text-xl leading-[2.2] sm:text-2xl sm:leading-[2.4]" />;
  return (
    <div className={`group flex items-start gap-2 rounded-2xl px-2 transition-colors ${active ? 'bg-gold/20' : ''}`} data-testid="sentence">
      <div className="min-w-0 flex-1">
        {tappable ? (
          <button type="button" onClick={onTap} aria-expanded={translated} className="w-full rounded-xl text-left hover:bg-surface-2" title={T('Toucher pour voir la traduction')}>
            {text}
          </button>
        ) : (
          text
        )}
        {translated && <p className="pb-1 text-ink-soft" data-testid="translation">{bi(s)}</p>}
      </div>
      {speechSupported() && (
        <button type="button" onClick={onListen} aria-label={T('Écouter la phrase')} className="mt-2 inline-flex h-9 w-9 shrink-0 items-center justify-center rounded-full text-ink-soft hover:bg-surface-2 hover:text-ink">
          <SoundIcon />
        </button>
      )}
    </div>
  );
}

/** Carte « lecture du jour » pour l'accueil. */
export function ReadingTodayCard() {
  const { data } = useReading();
  if (!data || !data.today.chapter || !data.today.story) return null;
  const { chapter, story, state } = data.today;
  return (
    <Link to={state === 'new' ? `/lecture/${chapter.slug}` : '/lecture'} className="flex items-center gap-4 rounded-3xl border border-line bg-surface p-4 hover:border-ink-soft" data-testid="reading-today">
      <StoryGlyph story={story} size="sm" />
      <span className="min-w-0 flex-1">
        <span className="block text-sm text-ink-soft">{state === 'new' ? T('Lecture du jour · {0} min', [minutes(chapter.chars)]) : T('Lecture du jour faite ✓')}</span>
        <span className="block truncate font-bold">{bi(story.title)} — {bi(chapter.title as ReadingTitle)}</span>
      </span>
      {data.streak > 0 && <span className="flex items-center gap-1 font-bold"><Flame lit />{data.streak}</span>}
    </Link>
  );
}
