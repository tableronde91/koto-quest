import { useEffect, useRef, useState } from 'react';
import { Link, useNavigate, useParams, useSearchParams } from 'react-router';
import { useQueryClient } from '@tanstack/react-query';
import type { CharacterDto, CharacterGroupDto, CharacterSectionDto, MeDto, SessionDto } from '@koto/shared';
import { post } from '../api/client';
import { useCharacters } from '../api/hooks';
import { QuizRunner, RunSummary } from '../components/QuizRunner';
import { ErrorBox, PageTitle, ProgressBar, SpeakButtons, Spinner } from '../components/ui';
import { MASTERY_COLOR, MASTERY_LABEL } from '../lib/format';
import { speak } from '../lib/speech';
import { Stamp } from '../components/Celebrate';
import { T } from '../i18n';

type SectionSlug = CharacterSectionDto['slug'];

/** Onglet Caractères : grilles hiragana / katakana / kanji, ouvertes à tous, avec maîtrise par caractère. */
export function CharactersPage() {
  const { data, isLoading, error, refetch } = useCharacters();
  const [params, setParams] = useSearchParams();
  const [detail, setDetail] = useState<CharacterDto | null>(null);
  const navigate = useNavigate();
  if (isLoading) return <Spinner />;
  if (error || !data) return <ErrorBox error={error} onRetry={refetch} />;

  const current = (params.get('s') as SectionSlug) ?? 'hiragana';
  const section = data.sections.find((s) => s.slug === current) ?? data.sections[0];
  const practice = (scope: string) => navigate(`/characters/practice/${scope}`);

  return (
    <div>
      <PageTitle sub={T("Les écritures japonaises, accessibles à tout moment. Chaque caractère a sa propre barre de maîtrise, partagée avec ton parcours.")}>{T("Caractères")}</PageTitle>

      <div role="tablist" aria-label={T("Écriture")} className="mb-6 grid grid-cols-3 rounded-2xl bg-surface-2 p-1">
        {data.sections.map((s) => (
          <button
            key={s.slug}
            role="tab"
            aria-selected={s.slug === section.slug}
            onClick={() => setParams({ s: s.slug }, { replace: true })}
            className={`min-h-12 rounded-xl font-bold ${s.slug === section.slug ? 'bg-surface shadow-sm' : 'text-ink-soft'}`}
          >
            <span lang="ja" className="jp mr-1 hidden sm:inline">{s.slug === 'hiragana' ? 'あ' : s.slug === 'katakana' ? 'ア' : '字'}</span>
            {s.title}
          </button>
        ))}
      </div>

      <section role="tabpanel" aria-label={section.title}>
        <div className="flex flex-col gap-4 rounded-3xl bg-ink p-5 text-paper sm:flex-row sm:items-center sm:justify-between sm:p-6">
          <div className="flex-1">
            <p className="max-w-[52ch] opacity-85">{section.description}</p>
            <div className="mt-3 max-w-md">
              <ProgressBar value={section.learned} max={section.total} label={`${section.title} vus`} tone="gold" />
            </div>
            <p className="mt-1 text-sm opacity-85">{T("{0} sur {1} vus, {2} maîtrisés", [ section.learned , section.total , section.mastered ])}</p>
          </div>
          <button className="btn btn-gold min-h-14 px-6 text-lg" onClick={() => practice(section.slug)}>
            {section.due > 0 ? T("Réviser {0} caractère{1}", [section.due, section.due > 1 ? 's' : '']) : section.learned === 0 ? T("Apprendre les {0}", [section.title.toLowerCase()]) : T("Continuer")}
          </button>
        </div>

        <div className="mt-8 flex flex-col gap-8">
          {section.groups.map((g) => (
            <Group key={g.slug} group={g} kanji={section.slug === 'kanji'} onPractice={() => practice(g.slug)} onOpen={setDetail} />
          ))}
        </div>
        {section.slug === 'kanji' && data.notice && <p className="mt-6 text-sm text-ink-soft">{data.notice}</p>}
      </section>

      {detail && <CharacterSheet c={detail} onClose={() => setDetail(null)} />}
    </div>
  );
}

/** Disposition « gojūon » : les trous de la grille (ya _ yu _ yo, wa _ _ _ wo) restent visibles. */
function layout(g: CharacterGroupDto): (CharacterDto | null)[] {
  if (g.slug.endsWith('-y') && g.items.length === 3) return [g.items[0], null, g.items[1], null, g.items[2]];
  if (g.slug.endsWith('-w') && g.items.length === 3) return [g.items[0], null, null, null, g.items[1], g.items[2]];
  return g.items;
}

function Group({ group: g, kanji, onPractice, onOpen }: { group: CharacterGroupDto; kanji: boolean; onPractice: () => void; onOpen: (c: CharacterDto) => void }) {
  const combo = g.slug.endsWith('-combo');
  const cols = kanji ? 'grid-cols-4 sm:grid-cols-6' : combo ? 'grid-cols-3' : 'grid-cols-5';
  const learned = g.items.filter((i) => i.mastery).length;
  return (
    <div>
      <div className="mb-3 flex items-center justify-between gap-3">
        <h2 className="text-lg">
          {g.title}
          <span className="ml-2 text-sm font-normal text-ink-soft">{learned}/{g.items.length}</span>
        </h2>
        <button className="btn btn-quiet min-h-10 px-4 text-sm" onClick={onPractice} aria-label={T("Pratiquer : {0}", [g.title])}>{T("Pratiquer")}</button>
      </div>
      <ul className={`grid ${cols} gap-2 sm:gap-3`}>
        {layout(g).map((c, i) =>
          c ? (
            <li key={c.id}>
              <Cell c={c} kanji={kanji} onOpen={onOpen} />
            </li>
          ) : (
            <li key={`gap-${i}`} aria-hidden="true" />
          ),
        )}
      </ul>
    </div>
  );
}

function Cell({ c, kanji, onOpen }: { c: CharacterDto; kanji: boolean; onOpen: (c: CharacterDto) => void }) {
  const label = kanji ? c.meaning : c.romaji ?? c.meaning;
  return (
    <button
      type="button"
      onClick={() => {
        speak(c.reading ?? c.front);
        onOpen(c);
      }}
      aria-label={`${c.front}, ${label}${c.mastery ? `, ${MASTERY_LABEL[c.mastery]}` : ', pas encore vu'}`}
      className="flex w-full flex-col items-center gap-1 rounded-2xl border-2 border-line bg-surface px-1 pb-2 pt-3 hover:border-ink-soft"
    >
      <span lang="ja" className={`jp font-bold leading-none ${c.front.length > 1 ? 'text-2xl sm:text-3xl' : 'text-3xl sm:text-4xl'}`} style={{ color: c.mastery ? 'var(--ink)' : 'var(--ink-soft)' }}>
        {c.front}
      </span>
      <span className="w-full truncate text-center text-xs text-ink-soft sm:text-sm">{label}</span>
      <span className="mt-1 h-1.5 w-4/5 overflow-hidden rounded-full bg-surface-2" aria-hidden="true">
        <span className="block h-full rounded-full" style={{ width: `${c.mastery ? Math.max(8, c.score) : 0}%`, background: c.mastery ? MASTERY_COLOR[c.mastery] : 'transparent' }} />
      </span>
    </button>
  );
}

function CharacterSheet({ c, onClose }: { c: CharacterDto; onClose: () => void }) {
  const closeRef = useRef<HTMLButtonElement>(null);
  useEffect(() => {
    closeRef.current?.focus();
    const onKey = (e: KeyboardEvent) => e.key === 'Escape' && onClose();
    window.addEventListener('keydown', onKey);
    return () => window.removeEventListener('keydown', onKey);
  }, [onClose]);
  return (
    <div className="fixed inset-0 z-50 flex items-end justify-center bg-[rgb(10_14_40/0.55)] p-3 sm:items-center" onClick={onClose}>
      <div role="dialog" aria-modal="true" aria-labelledby="char-title" className="w-full max-w-md rounded-3xl bg-paper p-6 shadow-2xl" onClick={(e) => e.stopPropagation()}>
        <div className="flex items-start justify-between">
          <p id="char-title" lang="ja" className="jp text-8xl font-black leading-none">{c.front}</p>
          <button ref={closeRef} className="rounded-full p-2 text-ink-soft hover:bg-surface-2" onClick={onClose} aria-label={T("Fermer")}>
            <svg width="20" height="20" viewBox="0 0 24 24" aria-hidden="true"><path d="M6 6l12 12M18 6L6 18" stroke="currentColor" strokeWidth="2.5" strokeLinecap="round" /></svg>
          </button>
        </div>
        <p className="mt-4 text-2xl font-bold">{c.kind === 'kanji' ? c.meaning : c.romaji}</p>
        {c.kind === 'kanji' && (
          <dl className="mt-3 grid grid-cols-[auto_1fr] gap-x-4 gap-y-1">
            <dt className="text-ink-soft">{T("Lecture courante")}</dt>
            <dd lang="ja" className="jp">{c.reading}</dd>
            <dt className="text-ink-soft">{T("On’yomi")}</dt>
            <dd lang="ja" className="jp">{c.kanji?.onyomi.join('、') || '—'}</dd>
            <dt className="text-ink-soft">{T("Kun’yomi")}</dt>
            <dd lang="ja" className="jp">{c.kanji?.kunyomi.join('、') || '—'}</dd>
            {c.kanji?.strokes ? (<><dt className="text-ink-soft">{T("Traits")}</dt><dd>{c.kanji.strokes}</dd></>) : null}
          </dl>
        )}
        <p className="mt-3 flex items-center gap-2 text-sm">
          <span className="h-2.5 w-2.5 rounded-full" style={{ background: c.mastery ? MASTERY_COLOR[c.mastery] : 'var(--line)' }} aria-hidden="true" />
          {c.mastery ? MASTERY_LABEL[c.mastery] : T("Pas encore vu")}
        </p>
        <div className="mt-5"><SpeakButtons text={c.reading ?? c.front} /></div>
      </div>
    </div>
  );
}

/** Séance de pratique (/characters/practice/:scope). */
export function CharacterPracticePage({ me }: { me: MeDto }) {
  const { scope = 'hiragana' } = useParams();
  const [session, setSession] = useState<SessionDto | null>(null);
  const [error, setError] = useState<unknown>(null);
  const [summary, setSummary] = useState<RunSummary | null>(null);
  const navigate = useNavigate();
  const qc = useQueryClient();
  const sectionOf = scope.startsWith('hira') ? 'hiragana' : scope.startsWith('kata') ? 'katakana' : 'kanji';
  const back = `/characters?s=${sectionOf}`;

  const start = () => {
    setSummary(null);
    setSession(null);
    post<SessionDto>('/characters/practice', { scope }).then(setSession).catch(setError);
  };
  useEffect(start, [scope]);

  if (error) return <ErrorBox error={error} />;
  if (!session) return <Spinner label={T("Préparation de la séance…")} />;
  if (summary || session.questions.length === 0)
    return (
      <div className="flex flex-col items-start gap-5 py-6">
        <Stamp className="jp text-8xl font-black text-ko">{summary ? '練習' : '空'}</Stamp>
        <h1 className="text-4xl">{summary ? T("Séance terminée") : T("Rien à pratiquer ici")}</h1>
        {summary && <p className="text-lg">{T("{0}/{1} bonnes réponses, +{2} XP", [summary.correct , summary.total , summary.xp ])}</p>}
        <div className="flex flex-wrap gap-3">
          {summary && <button className="btn btn-gold" onClick={start}>{T("Encore une séance")}</button>}
          <Link to={back} className="btn btn-quiet" onClick={() => qc.invalidateQueries()}>{T("Retour aux caractères")}</Link>
        </div>
      </div>
    );
  return (
    <QuizRunner
      questions={session.questions}
      furigana={me.preferences.showFurigana}
      onFinish={(s) => {
        setSummary(s);
        qc.invalidateQueries();
      }}
      onQuit={() => {
        qc.invalidateQueries();
        navigate(back);
      }}
    />
  );
}
