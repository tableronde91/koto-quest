import { useEffect, useMemo, useState } from 'react';
import { Link, useNavigate, useParams, useSearchParams } from 'react-router';
import { motion } from 'motion/react';
import { useQuery, useQueryClient } from '@tanstack/react-query';
import type { ExpressionDto, ExpressionRegister, ExpressionsDto, MeDto, SessionDto } from '@koto/shared';
import { api, post } from '../api/client';
import { QuizRunner, RunSummary } from '../components/QuizRunner';
import { ErrorBox, PageTitle, ProgressBar, SoundIcon, Spinner } from '../components/ui';
import { Stamp } from '../components/Celebrate';
import { MASTERY_COLOR, MASTERY_LABEL } from '../lib/format';
import { speak, speechSupported } from '../lib/speech';
import { T } from '../i18n';

const REGISTER: Record<ExpressionRegister, { label: string; hint: string; color: string; bg: string }> = {
  polite: { label: T('Poli'), hint: T('Pour la plupart des situations, avec des inconnus et en public.'), color: '#1F5FA8', bg: '#E3EEFA' },
  neutral: { label: T('Neutre'), hint: T('Passe partout, quel que soit l’interlocuteur.'), color: '#4F5B66', bg: '#ECEFF2' },
  casual: { label: T('Familier'), hint: T('Entre amis et en famille ; à éviter avec un supérieur.'), color: '#A3520F', bg: '#FCEBDD' },
  formal: { label: T('Formel'), hint: T('Travail, clients, situations officielles (keigo).'), color: '#6A3FA0', bg: '#EEE6F8' },
};

export const useExpressions = () => useQuery({ queryKey: ['expressions'], queryFn: () => api<ExpressionsDto>('/expressions') });

/** Recueil d'expressions utiles, classées par thème, avec écoute, usage et entraînement. */
export function ExpressionsPage() {
  const { data, isLoading, error, refetch } = useExpressions();
  const [params, setParams] = useSearchParams();
  const [query, setQuery] = useState('');
  const navigate = useNavigate();

  const q = query.trim().toLowerCase();
  const results = useMemo(() => {
    if (!data || q.length < 2) return [];
    return data.themes.flatMap((t) =>
      t.expressions.filter((e) => [e.front, e.reading ?? '', e.romaji ?? '', e.meaning].some((s) => s.toLowerCase().includes(q))).map((e) => ({ e, theme: t.title })),
    );
  }, [data, q]);

  if (isLoading) return <Spinner />;
  if (error || !data) return <ErrorBox error={error} onRetry={refetch} />;
  const theme = data.themes.find((t) => t.slug === params.get('t')) ?? data.themes[0];
  const practice = () => navigate(`/expressions/practice/${theme.slug}`);

  return (
    <div className="flex flex-col gap-6">
      <PageTitle sub={T('Les phrases toutes faites qu’on entend partout au Japon : quand les dire, à qui, et comment les prononcer.')}>{T('Expressions')}</PageTitle>

      <label className="flex items-center gap-3 rounded-2xl border-2 border-line bg-surface px-4 focus-within:border-ink">
        <span aria-hidden="true" className="text-xl">🔎</span>
        <span className="sr-only">{T('Rechercher une expression')}</span>
        <input value={query} onChange={(e) => setQuery(e.target.value)} placeholder={T('Rechercher : merci, おねがい, sumimasen…')} className="min-h-12 flex-1 bg-transparent outline-none" />
        {query && (
          <button type="button" className="text-ink-soft" onClick={() => setQuery('')} aria-label={T('Effacer la recherche')}>
            ✕
          </button>
        )}
      </label>

      {q.length >= 2 ? (
        <section aria-label={T('Résultats de recherche')} className="flex flex-col gap-3">
          <p className="text-ink-soft">{results.length ? T('{0} expression(s) trouvée(s)', [results.length]) : T('Aucune expression ne correspond.')}</p>
          <div className="grid gap-4 lg:grid-cols-2">
            {results.map(({ e, theme: t }) => (
              <ExpressionCard key={e.id} e={e} themeTitle={t} />
            ))}
          </div>
        </section>
      ) : (
        <>
          {/* Thèmes */}
          <nav aria-label={T('Thèmes')} className="grid grid-cols-2 gap-2 sm:grid-cols-3 lg:grid-cols-5">
            {data.themes.map((t) => {
              const active = t.slug === theme.slug;
              return (
                <button
                  key={t.slug}
                  aria-pressed={active}
                  onClick={() => setParams({ t: t.slug }, { replace: true })}
                  className={`flex items-center gap-2.5 rounded-2xl border-2 p-2.5 text-left transition-colors ${active ? 'border-ink bg-ink text-paper' : 'border-line bg-surface hover:border-ink-soft'}`}
                >
                  <span aria-hidden="true" lang="ja" className={`jp flex h-10 w-10 shrink-0 items-center justify-center rounded-xl text-xl font-black ${active ? 'bg-gold text-[#2a1a00]' : 'bg-surface-2'}`}>{t.glyph}</span>
                  <span className="min-w-0">
                    <span className="block text-sm font-bold leading-tight">{t.title}</span>
                    <span className={`block text-xs ${active ? 'opacity-80' : 'text-ink-soft'}`}>{T('{0}/{1} vues', [t.learned, t.total])}{t.due > 0 ? ` · ${T('{0} à revoir', [t.due])}` : ''}</span>
                  </span>
                </button>
              );
            })}
          </nav>

          <section aria-label={theme.title} className="flex flex-col gap-5">
            <div className="flex flex-col gap-4 rounded-3xl bg-ink p-5 text-paper sm:flex-row sm:items-center sm:justify-between sm:p-6">
              <div className="flex flex-1 items-center gap-4">
                <span aria-hidden="true" lang="ja" className="jp hidden h-16 w-16 shrink-0 items-center justify-center rounded-2xl bg-gold text-4xl font-black text-[#2a1a00] sm:flex">{theme.glyph}</span>
                <div className="flex-1">
                  <h2 className="text-2xl">{theme.title}</h2>
                  <p className="max-w-[52ch] opacity-85">{theme.description}</p>
                  <div className="mt-3 max-w-md">
                    <ProgressBar value={theme.learned} max={theme.total} label={T('Expressions vues : {0}', [theme.title])} tone="gold" />
                  </div>
                  <p className="mt-1 text-sm opacity-85">{T('{0} sur {1} vues, {2} maîtrisées', [theme.learned, theme.total, theme.mastered])}</p>
                </div>
              </div>
              <button className="btn btn-gold min-h-14 px-6 text-lg" onClick={practice}>
                {theme.due > 0 ? T('Revoir {0} expression(s)', [theme.due]) : theme.learned === 0 ? T('Apprendre ces expressions') : theme.learned < theme.total ? T('Continuer') : T('S’entraîner')}
              </button>
            </div>

            <div className="grid gap-4 lg:grid-cols-2">
              {theme.expressions.map((e, i) => (
                <motion.div key={e.id} initial={{ opacity: 0, y: 8 }} animate={{ opacity: 1, y: 0 }} transition={{ delay: Math.min(0.3, i * 0.03) }}>
                  <ExpressionCard e={e} />
                </motion.div>
              ))}
            </div>
          </section>

          <details className="rounded-3xl bg-surface-2 p-5">
            <summary className="cursor-pointer text-lg font-bold">{T('Les registres de langue')}</summary>
            <ul className="mt-3 flex flex-col gap-2">
              {(Object.keys(REGISTER) as ExpressionRegister[]).map((r) => (
                <li key={r} className="flex items-start gap-3">
                  <RegisterBadge r={r} />
                  <span className="text-ink-soft">{REGISTER[r].hint}</span>
                </li>
              ))}
            </ul>
            {data.notice && <p className="mt-4 text-sm text-ink-soft">{data.notice}</p>}
          </details>
        </>
      )}
    </div>
  );
}

function RegisterBadge({ r }: { r: ExpressionRegister }) {
  const reg = REGISTER[r];
  return (
    <span className="shrink-0 rounded-full px-2.5 py-0.5 text-xs font-bold" style={{ color: reg.color, background: reg.bg }} title={reg.hint}>
      {reg.label}
    </span>
  );
}

function ListenButton({ text, label, small }: { text: string; label: string; small?: boolean }) {
  if (!speechSupported()) return null;
  return (
    <button type="button" onClick={() => speak(text)} aria-label={label} className={`inline-flex shrink-0 items-center justify-center rounded-full bg-surface-2 text-ink hover:bg-line ${small ? 'h-8 w-8' : 'h-11 w-11'}`}>
      <SoundIcon />
    </button>
  );
}

/** Fiche d'une expression : japonais, lecture, romaji, sens, usage et exemple. */
function ExpressionCard({ e, themeTitle }: { e: ExpressionDto; themeTitle?: string }) {
  const speakable = (e.reading ?? e.front).replace(/〜/g, '');
  return (
    <article className="flex h-full flex-col gap-3 rounded-3xl border border-line bg-surface p-5" data-testid="expression">
      <div className="flex items-start gap-3">
        <div className="min-w-0 flex-1">
          <p lang="ja" className="jp text-2xl font-bold leading-snug sm:text-3xl">{e.front}</p>
          {e.reading && e.reading !== e.front && <p lang="ja" className="jp text-ink-soft">{e.reading}</p>}
          {e.romaji && <p className="text-sm italic text-ink-soft">{e.romaji}</p>}
        </div>
        <ListenButton text={speakable} label={T('Écouter {0}', [e.front])} />
      </div>
      <div className="flex flex-wrap items-center gap-2">
        <p className="text-lg font-bold">{e.meaning}</p>
        <RegisterBadge r={e.register} />
        {themeTitle && <span className="text-xs text-ink-soft">· {themeTitle}</span>}
      </div>
      <p className="text-ink-soft">{e.note}</p>
      {e.example && (
        <div className="mt-auto flex items-start gap-3 rounded-2xl bg-surface-2 p-3">
          <div className="flex-1">
            <p lang="ja" className="jp text-lg">{e.example.jp}</p>
            <p className="text-sm text-ink-soft">{e.example.fr}</p>
          </div>
          <ListenButton small text={e.example.jp} label={T('Écouter l’exemple')} />
        </div>
      )}
      <p className="flex items-center gap-2 text-xs text-ink-soft">
        <span className="h-2.5 w-2.5 rounded-full" style={{ background: e.mastery ? MASTERY_COLOR[e.mastery] : 'var(--line)' }} aria-hidden="true" />
        {e.mastery ? MASTERY_LABEL[e.mastery] : T('Pas encore vu')}
      </p>
    </article>
  );
}

/** Entraînement sur un thème (/expressions/practice/:theme). */
export function ExpressionPracticePage({ me }: { me: MeDto }) {
  const { theme = 'politesse' } = useParams();
  const [session, setSession] = useState<SessionDto | null>(null);
  const [error, setError] = useState<unknown>(null);
  const [summary, setSummary] = useState<RunSummary | null>(null);
  const navigate = useNavigate();
  const qc = useQueryClient();
  const back = `/expressions?t=${theme}`;

  const start = () => {
    setSummary(null);
    setSession(null);
    post<SessionDto>('/expressions/practice', { theme }).then(setSession).catch(setError);
  };
  useEffect(start, [theme]);

  if (error) return <ErrorBox error={error} />;
  if (!session) return <Spinner label={T('Préparation de la séance…')} />;
  if (summary || session.questions.length === 0)
    return (
      <div className="flex flex-col items-start gap-5 py-6">
        <Stamp className="jp text-8xl font-black text-ko">{summary ? '会話' : '空'}</Stamp>
        <h1 className="text-4xl">{summary ? T('Séance terminée') : T('Rien à pratiquer ici')}</h1>
        {summary && <p className="text-lg">{T('{0}/{1} bonnes réponses, +{2} XP', [summary.correct, summary.total, summary.xp])}</p>}
        {summary && <p className="max-w-[52ch] text-ink-soft">{T('Ces expressions reviendront dans tes révisions, au moment où tu risques de les oublier.')}</p>}
        <div className="flex flex-wrap gap-3">
          {summary && <button className="btn btn-gold" onClick={start}>{T('Encore une séance')}</button>}
          <Link to={back} className="btn btn-quiet" onClick={() => qc.invalidateQueries()}>{T('Retour aux expressions')}</Link>
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
