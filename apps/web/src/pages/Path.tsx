import { useEffect, useState } from 'react';
import { Link, useSearchParams } from 'react-router';
import { ApiError } from '../api/client';
import type { PathLessonDto, WorldBossDto } from '@koto/shared';
import { BossSeal } from './Boss';
import { useMe, usePath } from '../api/hooks';
import { IslandVignette, WorldMap } from '../components/WorldMap';
import { DEFAULT_AVATAR } from '@koto/learning-engine';
import { ErrorBox, PageTitle, Spinner } from '../components/ui';
import { motion } from 'motion/react';
import { WorldVignette } from '../components/Illustrations';
import { EXAMS } from '@koto/learning-engine';
import { T } from '../i18n';
import { sagaFor, storyChapter, type Saga } from '../lib/story';

/** Parcours : chemin vertical de « pierres » (inspiré du sugoroku), une par leçon. */
const LEVEL_KEY = 'koto-path-level';
function storedLevel(): string | null {
  try {
    return localStorage.getItem(LEVEL_KEY);
  } catch {
    return null;
  }
}

export function PathPage() {
  const [params, setParams] = useSearchParams();
  const { data: me } = useMe();
  const level = params.get('niveau') ?? storedLevel() ?? me?.preferences.targetLevel ?? 'N5';
  const { data, isLoading, error, refetch } = usePath(level);
  const choose = (code: string) => {
    try {
      localStorage.setItem(LEVEL_KEY, code);
    } catch {
      /* préférence non mémorisée : sans conséquence */
    }
    setParams({ niveau: code }, { replace: true });
  };
  // Niveau mémorisé qui n'existe plus : retour au N5.
  const missing = error instanceof ApiError && error.status === 404 && level !== 'N5';
  useEffect(() => {
    if (missing) choose('N5');
  });
  if (missing || isLoading) return <Spinner />;
  if (error || !data) return <ErrorBox error={error} onRetry={refetch} />;

  const saga = sagaFor(data.level.code);
  const worldDone = (w: (typeof data.worlds)[number]) => (w.exam && w.progress.total === 0 ? w.exam.passed : w.boss ? w.boss.defeated : w.progress.total > 0 && w.progress.completed === w.progress.total);
  const sagaDone = data.worlds.length > 0 && data.worlds.every((w) => !w.comingSoon && worldDone(w));

  return (
    <div>
      {saga ? <SagaBanner saga={saga} code={data.level.code} region={data.level.region} notice={data.level.notice} done={sagaDone} /> : <PageTitle sub={data.level.notice}>{T("{0} : {1}", [data.level.code, data.level.region])}</PageTitle>}
      {data.levels.length > 1 && (
        <div role="tablist" aria-label={T("Niveau du parcours")} className="mb-6 flex flex-wrap gap-2">
          {data.levels.map((l) => {
            const active = l.code === data.level.code;
            return (
              <button
                key={l.code}
                role="tab"
                aria-selected={active}
                onClick={() => choose(l.code)}
                className={`flex min-h-12 items-center gap-3 rounded-2xl border-2 px-4 text-left ${active ? 'border-ink bg-ink text-paper' : 'border-line bg-surface hover:border-ink-soft'}`}
              >
                <span className="font-display text-xl">{l.code}</span>
                <span className="text-sm leading-tight">
                  <span className="block font-bold">{sagaFor(l.code)?.short ?? l.title.split(' : ')[0]}</span>
                  <span className={active ? 'opacity-80' : 'text-ink-soft'}>{T("{0}/{1} leçons", [l.completed , l.lessons ])}</span>
                </span>
              </button>
            );
          })}
        </div>
      )}
      <Link to="/prepa" className="mb-6 flex items-center gap-4 rounded-3xl border-2 border-[#8E1B26] bg-surface p-4 hover:bg-surface-2">
        <span aria-hidden="true" className="jp flex h-12 w-12 shrink-0 items-center justify-center rounded-2xl bg-[#8E1B26] text-2xl font-black text-white">試</span>
        <span className="flex-1"><span className="block font-bold">{T("Atelier JLPT")}</span><span className="text-sm text-ink-soft">{T("Entraîne-toi épreuve par épreuve au format de l’examen, avec ce que tu as appris.")}</span></span>
        <span aria-hidden="true" className="text-xl">→</span>
      </Link>
      <WorldMap worlds={data.worlds} avatar={me?.avatar ?? DEFAULT_AVATAR} region={data.level.region} level={data.level.code} saga={saga ? { glyph: saga.glyph, title: saga.title } : undefined} />
      <ol className="flex flex-col gap-10">
        {data.worlds.map((w) => {
          const ch = storyChapter(w.slug);
          const done = !w.comingSoon && worldDone(w);
          return (
          <li key={w.slug} aria-labelledby={`w-${w.slug}`} className="scroll-mt-6">
            <div className="flex items-center gap-4 border-b-2 border-line pb-2">
              <motion.div initial={{ scale: 0.6, opacity: 0 }} whileInView={{ scale: 1, opacity: 1 }} viewport={{ once: true }} transition={{ type: 'spring', stiffness: 220, damping: 15 }}>
                {saga ? <IslandVignette slug={w.slug} level={data.level.code} size={72} /> : <WorldVignette slug={w.slug} size={64} />}
              </motion.div>
              <h2 id={`w-${w.slug}`} className="flex-1 text-2xl">
                {ch && (
                  <span className="block">
                    <span className="mr-1 text-ink-soft">{T("Chapitre {0}", [w.order])}</span>{' '}
                    {ch.title}
                  </span>
                )}
                <span className={ch ? 'block font-sans text-base font-bold text-ink-soft' : undefined}>
                  <span className={ch ? undefined : 'mr-2 text-ink-soft'}>{T("Île {0}", [ w.order])}</span>
                  {ch ? ' · ' : ''}
                  {w.title}
                </span>
              </h2>
              <span className="shrink-0 text-sm text-ink-soft">
                {w.comingSoon ? T("Bientôt") : `${w.progress.completed}/${w.progress.total}`}
              </span>
            </div>
            {ch && saga && (
              <blockquote className="mt-3 rounded-r-2xl border-l-4 bg-surface-2 px-4 py-3 leading-relaxed" style={{ borderColor: saga.color }}>
                <p>{ch.intro}</p>
                {done && (
                  <p className="mt-2 font-bold" style={{ color: saga.color }}>
                    <span aria-hidden="true" className="jp mr-2">済</span>
                    {ch.outro}
                  </p>
                )}
              </blockquote>
            )}
            <p className="mt-2 text-ink-soft">
              {w.description}
              {w.optional && !w.comingSoon && T(" Tu as indiqué connaître ces bases : cette île reste ouverte pour réviser.")}
            </p>
            {w.chapters.map((c) => (
              <div key={c.slug} className="mt-5">
                <h3 className="text-base text-ink-soft">{c.title}</h3>
                <ul className="mt-3 flex flex-col">
                  {c.lessons.map((l, i) => (
                    <Stone key={l.slug} lesson={l} offset={i % 2 === 0 ? 0 : 1} />
                  ))}
                </ul>
              </div>
            ))}
            {w.boss && <BossStone worldSlug={w.slug} boss={w.boss} />}
            {w.exam && (
              <Link to={`/exam/${w.exam.slug}`} className="mt-4 flex items-center gap-4 rounded-2xl border-2 border-dashed border-ink p-3 hover:bg-surface-2" aria-label={`${w.exam.title} : ${w.exam.attempts ? `meilleur score ${w.exam.bestPercent} %` : T("jamais passé")}`}>
                <span aria-hidden="true" className="jp flex h-14 w-14 shrink-0 items-center justify-center rounded-2xl bg-ink text-2xl font-black text-paper">模</span>
                <span className="flex-1">
                  <span className="block text-lg font-bold">{w.exam.title}</span>
                  <span className="block text-sm text-ink-soft">
                    {w.exam.attempts
                      ? T(w.exam.passed ? "Meilleur score : {0} %, seuil atteint" : "Meilleur score : {0} %", [w.exam.bestPercent])
                      : EXAMS[w.exam.slug]
                        ? T("{0} minutes, {1} questions, non officiel", [EXAMS[w.exam.slug].durationMin, EXAMS[w.exam.slug].sections.reduce((n, sec) => n + sec.count, 0)])
                        : T("Examen blanc non officiel")}
                  </span>
                </span>
                <span className="btn btn-gold hidden sm:inline-flex">{w.exam.attempts ? T("Repasser") : T("Passer l’examen")}</span>
              </Link>
            )}
          </li>
          );
        })}
      </ol>
    </div>
  );
}

/** En-tête du mode histoire : sceau du héros, titre de la saga, prologue (puis épilogue une fois le niveau terminé). */
function SagaBanner({ saga, code, region, notice, done }: { saga: Saga; code: string; region: string; notice?: string | null; done: boolean }) {
  // Sur téléphone, le prologue est replié pour laisser la carte visible.
  const [open, setOpen] = useState(false);
  return (
    <header className="mb-6 overflow-hidden rounded-3xl border-2 bg-surface" style={{ borderColor: saga.color }}>
      <div className="flex items-center gap-3 p-3 text-white sm:gap-4 sm:p-5" style={{ background: saga.color }}>
        <span aria-hidden="true" className="jp flex h-12 w-12 shrink-0 items-center justify-center rounded-2xl border-2 border-white/70 bg-black/15 text-3xl font-black sm:h-16 sm:w-16 sm:text-4xl">{saga.glyph}</span>
        <div className="min-w-0">
          <p className="text-xs font-bold uppercase tracking-wide opacity-90 sm:text-sm">{T("Mode histoire · {0}", [saga.hero])}</p>
          <h1 className="text-2xl text-white sm:text-4xl">{T("{0} : {1}", [code, saga.title])}</h1>
          <p className="jp mt-0.5 text-sm opacity-90" lang="ja">{saga.jp}</p>
        </div>
      </div>
      <div className="p-3 sm:p-5">
        <p className={`max-w-[70ch] leading-relaxed ${open ? '' : 'line-clamp-3 sm:line-clamp-none'}`}>{saga.prologue}</p>
        {done && <p className="mt-3 max-w-[70ch] font-bold leading-relaxed" style={{ color: saga.color }}>{saga.epilogue}</p>}
        <p className={`mt-3 text-sm text-ink-soft ${open ? '' : 'hidden sm:block'}`}>
          {region}
          {notice ? ` · ${notice}` : ''}
        </p>
        <button type="button" onClick={() => setOpen(!open)} aria-expanded={open} className="mt-2 min-h-11 text-sm font-bold underline sm:hidden">
          {open ? T("Replier") : T("Lire la suite")}
        </button>
      </div>
    </header>
  );
}

const STATUS_TEXT: Record<PathLessonDto['status'], string> = {
  completed: T("Terminée"),
  in_progress: T("Commencée"),
  available: T("Disponible"),
  locked: T("Verrouillée"),
};

function Stone({ lesson: l, offset }: { lesson: PathLessonDto; offset: number }) {
  const locked = l.status === 'locked';
  const done = l.status === 'completed';
  const content = (
    <>
      <span
        aria-hidden="true"
        className="jp flex h-14 w-14 shrink-0 items-center justify-center rounded-full border-4 text-xl font-bold"
        style={{
          background: done ? 'var(--ok)' : locked ? 'var(--surface-2)' : 'var(--gold)',
          borderColor: done ? 'var(--ok)' : locked ? 'var(--line)' : 'var(--ink)',
          color: done ? 'var(--paper)' : locked ? 'var(--ink-soft)' : '#2a1a00',
        }}
      >
        {done ? '✓' : locked ? '錠' : '道'}
      </span>
      <span className="flex-1">
        <span className="jp block text-lg font-bold">{l.title}</span>
        <span className="block text-sm text-ink-soft">{T("{0}, {1} min, {2} notions", [ STATUS_TEXT[l.status] , l.minutes , l.itemCount ])}</span>
      </span>
    </>
  );
  return (
    <li className="relative py-2" data-offset={offset}>
      {/* Trait vertical qui relie les étapes : toutes les pierres sont sur le même axe. */}
      <span aria-hidden="true" className="absolute bottom-0 left-[2.125rem] top-0 w-1 rounded-full bg-line" />
      {locked ? (
        <div className="relative flex items-center gap-4 p-2 opacity-70" aria-label={T("{0} — verrouillée", [l.title])}>{content}</div>
      ) : (
        <Link to={`/lesson/${l.slug}`} className="relative flex items-center gap-4 rounded-2xl p-2 hover:bg-surface-2">
          {content}
        </Link>
      )}
    </li>
  );
}

/** Gardien en fin de monde : verrouillé tant que le monde n'est pas terminé. */
function BossStone({ worldSlug, boss }: { worldSlug: string; boss: WorldBossDto }) {
  const status = boss.defeated ? T("Vaincu, combat rejouable") : boss.available ? T("Prêt à t’affronter") : T("Termine l’île pour l’affronter");
  const content = (
    <>
      <BossSeal glyph={boss.glyph} size="sm" dim={!boss.available} />
      <span className="flex-1">
        <span className="block text-sm text-ink-soft">{T("Gardien de l’île")}</span>
        <span className="block text-lg font-bold">{boss.name}</span>
        <span className="block text-sm text-ink-soft">{status}</span>
      </span>
      {boss.available && <span className={`btn ${boss.defeated ? 'btn-quiet' : 'btn-gold'} hidden sm:inline-flex`}>{boss.defeated ? T("Rejouer") : T("Affronter")}</span>}
    </>
  );
  return (
    <div className="mt-4 rounded-2xl border-2 border-dashed p-2" style={{ borderColor: boss.available && !boss.defeated ? 'var(--ko)' : 'var(--line)' }}>
      {boss.available ? (
        <Link to={`/boss/${worldSlug}`} className="flex items-center gap-4 rounded-xl p-1 hover:bg-surface-2" aria-label={`${boss.name} : ${status}`}>{content}</Link>
      ) : (
        <div className="flex items-center gap-4 p-1 opacity-70" aria-label={`${boss.name} : ${status}`}>{content}</div>
      )}
    </div>
  );
}
