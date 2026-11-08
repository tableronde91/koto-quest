import { Bar, BarChart, CartesianGrid, Line, LineChart, ResponsiveContainer, Tooltip, XAxis, YAxis } from 'recharts';
import type { Mastery } from '@koto/shared';
import { Link } from 'react-router';
import { motion } from 'motion/react';
import { useAchievements, useDashboard, usePath, useStats } from '../api/hooks';
import { Avatar } from '../components/Avatar';
import { BossCreature } from '../components/BossCreature';
import { CountUp, Flame } from '../components/Celebrate';
import { ErrorBox, PageTitle, Spinner } from '../components/ui';
import { KIND_LABEL, MASTERY_COLOR, MASTERY_LABEL, formatDuration } from '../lib/format';
import { Sprout } from '../components/Illustrations';
import { T, DATE_LOCALE } from '../i18n';

const shortDate = (d: string) => new Date(`${d}T12:00:00`).toLocaleDateString(DATE_LOCALE, { day: 'numeric', month: 'short' });
const axis = { stroke: 'var(--ink-soft)', fontSize: 12 };
const tooltipStyle = { background: 'var(--surface)', border: '1px solid var(--line)', borderRadius: 12, color: 'var(--ink)' };

const RANKS: [number, string][] = [
  [16, T("Maître du Koto")],
  [12, T("Sensei en herbe")],
  [8, T("Gardien·ne des kanji")],
  [5, T("Lame des kana")],
  [3, T("Voyageur·se des îles")],
  [1, T("Apprenti·e du dojo")],
];
const rankFor = (level: number) => RANKS.find(([min]) => level >= min)![1];

/** Niveau d'une compétence : un palier tous les 10 éléments maîtrisés. */
const SKILL_STEP = 10;
const SKILLS = [
  { kind: 'kana', glyph: 'あ', label: T("Kana"), color: '#E36A3A' },
  { kind: 'vocabulary', glyph: '語', label: T("Vocabulaire"), color: '#3F8F5B' },
  { kind: 'kanji', glyph: '字', label: T("Kanji"), color: '#8E1B26' },
  { kind: 'grammar', glyph: '文', label: T("Grammaire"), color: '#4F5DB8' },
] as const;

const GARDEN: { m: Mastery; icon: string; label: string; hint: string }[] = [
  { m: 'mastered', icon: '🌸', label: T("En fleur"), hint: T("maîtrisées") },
  { m: 'learning', icon: '🌿', label: T("En pousse"), hint: T("en apprentissage") },
  { m: 'discovered', icon: '🌱', label: T("Graines"), hint: T("découvertes") },
  { m: 'fragile', icon: '🍂', label: T("Feuilles fragiles"), hint: T("à consolider") },
  { m: 'urgent', icon: '🥀', label: T("À arroser vite"), hint: T("à réviser maintenant") },
];

function XpRing({ value, max, level }: { value: number; max: number; level: number }) {
  const r = 44;
  const c = 2 * Math.PI * r;
  return (
    <div className="relative h-24 w-24 shrink-0 sm:h-28 sm:w-28" role="img" aria-label={T("Niveau {0}, {1} XP sur {2} vers le niveau suivant", [level, value, max])}>
      <svg viewBox="0 0 100 100" className="h-full w-full -rotate-90">
        <circle cx="50" cy="50" r={r} fill="none" stroke="rgb(255 255 255 / .15)" strokeWidth="8" />
        <motion.circle cx="50" cy="50" r={r} fill="none" stroke="var(--gold)" strokeWidth="8" strokeLinecap="round" strokeDasharray={c} initial={{ strokeDashoffset: c }} animate={{ strokeDashoffset: c * (1 - value / max) }} transition={{ duration: 1, ease: 'easeOut' }} />
      </svg>
      <div className="absolute inset-0 flex flex-col items-center justify-center">
        <span className="text-xs font-bold uppercase tracking-wide opacity-75">{T("Niv.")}</span>
        <span className="font-display text-4xl leading-none"><CountUp value={level} /></span>
      </div>
    </div>
  );
}

function Section({ title, glyph, children, id }: { title: string; glyph: string; children: React.ReactNode; id?: string }) {
  return (
    <section aria-labelledby={`${id ?? glyph}-t`} id={id} className="scroll-mt-6">
      <h2 id={`${id ?? glyph}-t`} className="mb-3 flex items-center gap-3 text-xl">
        <span aria-hidden="true" className="jp flex h-9 w-9 items-center justify-center rounded-xl bg-[#8E1B26] text-lg font-black text-white">{glyph}</span>
        {title}
      </h2>
      {children}
    </section>
  );
}

export function StatsPage() {
  const { data: s, isLoading, error, refetch } = useStats();
  const { data: d } = useDashboard();
  const { data: ach } = useAchievements();
  const { data: n5 } = usePath('N5');
  const { data: n4 } = usePath('N4');
  if (isLoading) return <Spinner />;
  if (error || !s) return <ErrorBox error={error} onRetry={refetch} />;

  const order: Mastery[] = ['mastered', 'learning', 'discovered', 'fragile', 'urgent'];
  const totalCards = order.reduce((n, m) => n + s.masteryDistribution[m], 0);
  const daily = s.days.map((d) => ({ ...d, label: shortDate(d.date), accuracy: d.answers ? Math.round((d.correct / d.answers) * 100) : null, minutes: Math.round(d.seconds / 60) }));
  const last14 = s.days.slice(-14);
  const activeDays = last14.filter((x) => x.answers > 0).length;
  const bosses = [...(n5?.worlds ?? []), ...(n4?.worlds ?? [])].filter((w) => w.boss).map((w) => ({ slug: w.slug, island: w.title, ...w.boss! }));
  const defeated = bosses.filter((b) => b.defeated).length;
  const bestExam = s.exams.length ? Math.max(...s.exams.map((e) => e.percent)) : null;
  const needsCare = s.masteryDistribution.fragile + s.masteryDistribution.urgent;

  return (
    <div className="flex flex-col gap-10">
      <PageTitle sub={T("Ton personnage, tes compétences et tes trophées.")}>{T("Mon aventure")}</PageTitle>

      {/* Fiche du héros */}
      {d && (
        <section aria-label={T("Fiche du héros")} className="relative overflow-hidden rounded-3xl p-5 text-white sm:p-7" style={{ background: 'linear-gradient(135deg,#1F2B57 0%,#3B2F6B 55%,#8E1B26 120%)' }}>
          <span aria-hidden="true" className="jp pointer-events-none absolute -right-6 -top-10 select-none text-[10rem] font-black leading-none opacity-10">冒険</span>
          <div className="relative flex flex-wrap items-center justify-between gap-4 sm:gap-5">
            <motion.div animate={{ y: [0, -5, 0] }} transition={{ duration: 2.4, repeat: Infinity, ease: 'easeInOut' }} className="overflow-hidden rounded-2xl border-[3px] border-white/80 shadow-lg">
              <Avatar config={d.avatar} size={96} />
            </motion.div>
            <div className="order-last min-w-0 basis-full sm:order-none sm:basis-auto sm:flex-1">
              <p className="text-sm font-bold uppercase tracking-wide text-[#FFD58A]">{rankFor(d.xp.level)}</p>
              <p className="font-display text-3xl leading-tight">{d.displayName}</p>
              <p className="mt-1 text-sm opacity-80">{T("{0} XP avant le niveau {1} · {2} XP au total", [d.xp.forNext - d.xp.intoLevel , d.xp.level + 1 , d.xp.total ])}</p>
            </div>
            <XpRing value={d.xp.intoLevel} max={d.xp.forNext} level={d.xp.level} />
          </div>
          <ul className="relative mt-5 grid grid-cols-2 gap-2 sm:grid-cols-4">
            {[
              { icon: <Flame lit={d.streak.todayDone} />, value: <><CountUp value={d.streak.current} /> j</>, label: T("Série en cours") },
              { icon: <span className="text-2xl">🪙</span>, value: <CountUp value={d.coins} />, label: T("Pièces") },
              { icon: <span className="text-2xl">📜</span>, value: <CountUp value={s.totals.lessonsCompleted} />, label: T("Leçons terminées") },
              { icon: <span className="text-2xl">⏳</span>, value: formatDuration(s.totals.studySeconds), label: T("Temps d’étude") },
            ].map((c, i) => (
              <motion.li key={i} initial={{ opacity: 0, y: 8 }} animate={{ opacity: 1, y: 0 }} transition={{ delay: 0.1 + i * 0.07 }} className="flex items-center gap-3 rounded-2xl bg-white/10 px-3 py-2.5">
                <span aria-hidden="true" className="flex w-7 justify-center">{c.icon}</span>
                <span><span className="block font-display text-xl leading-tight">{c.value}</span><span className="text-xs opacity-80">{c.label}</span></span>
              </motion.li>
            ))}
          </ul>
        </section>
      )}

      {/* Compétences */}
      <Section title={T("Compétences")} glyph="技">
        <ul className="grid gap-3 sm:grid-cols-2">
          {SKILLS.map((k, i) => {
            const v = s.byKind[k.kind];
            const lv = 1 + Math.floor(v.mastered / SKILL_STEP);
            const into = v.mastered % SKILL_STEP;
            return (
              <motion.li key={k.kind} initial={{ opacity: 0, x: -10 }} animate={{ opacity: 1, x: 0 }} transition={{ delay: i * 0.08 }} className="flex items-center gap-4 rounded-2xl border border-line bg-surface p-4">
                <span aria-hidden="true" className="jp flex h-14 w-14 shrink-0 items-center justify-center rounded-2xl text-3xl font-black text-white shadow-[0_3px_0_rgb(0_0_0/0.2)]" style={{ background: k.color }}>{k.glyph}</span>
                <div className="min-w-0 flex-1">
                  <p className="flex items-baseline justify-between gap-2"><span className="font-bold">{k.label}</span><span className="rounded-full bg-surface-2 px-2 text-sm font-bold">{T("Niv. {0}", [ lv])}</span></p>
                  <div className="mt-2 h-3 overflow-hidden rounded-full bg-surface-2" role="progressbar" aria-label={T("{0} : progression vers le niveau {1}", [k.label, lv + 1])} aria-valuenow={into} aria-valuemin={0} aria-valuemax={SKILL_STEP}>
                    <motion.div className="h-full rounded-full" style={{ background: k.color }} initial={{ width: 0 }} animate={{ width: `${(into / SKILL_STEP) * 100}%` }} transition={{ duration: 0.8, delay: 0.2 + i * 0.08 }} />
                  </div>
                  <p className="mt-1 text-xs text-ink-soft">{T("{0} maîtrisé{1} · {2} rencontré{3} · encore {4} pour monter", [v.mastered , v.mastered > 1 ? 's' : '' , v.learned , v.learned > 1 ? 's' : '' , SKILL_STEP - into ])}</p>
                </div>
              </motion.li>
            );
          })}
        </ul>
      </Section>

      {/* Jardin de la mémoire */}
      <Section title={T("Jardin de la mémoire")} glyph="庭">
        {totalCards === 0 ? (
          <div className="flex items-center gap-4 rounded-3xl border-2 border-dashed border-line p-5"><Sprout className="w-20 shrink-0" /><p className="text-ink-soft">{T("Termine une première leçon : chaque notion apprise sera plantée ici et fleurira à force de révisions.")}</p></div>
        ) : (
          <div className="rounded-3xl p-5" style={{ background: 'linear-gradient(180deg,var(--surface) 0%,color-mix(in srgb,var(--ok) 14%,var(--surface)) 100%)' }}>
            <ul className="grid grid-cols-2 gap-3 sm:grid-cols-5">
              {GARDEN.map((g, i) => (
                <motion.li key={g.m} initial={{ scale: 0.6, opacity: 0 }} animate={{ scale: 1, opacity: 1 }} transition={{ type: 'spring', delay: i * 0.08 }} className="flex flex-col items-center rounded-2xl bg-surface p-3 text-center shadow-sm">
                  <span aria-hidden="true" className="text-4xl">{g.icon}</span>
                  <span className="font-display text-2xl"><CountUp value={s.masteryDistribution[g.m]} /></span>
                  <span className="text-sm font-bold">{g.label}</span>
                  <span className="text-xs text-ink-soft">{g.hint}</span>
                </motion.li>
              ))}
            </ul>
            <div className="mt-4 flex h-3 w-full overflow-hidden rounded-full" role="img" aria-label={order.map((m) => `${MASTERY_LABEL[m]} : ${s.masteryDistribution[m]}`).join(', ')}>
              {order.map((m) => s.masteryDistribution[m] > 0 && <div key={m} style={{ width: `${(s.masteryDistribution[m] / totalCards) * 100}%`, background: MASTERY_COLOR[m] }} />)}
            </div>
            {needsCare > 0 ? (
              <p className="mt-4 flex flex-wrap items-center gap-3">
                <span>{T("{0} notion{1} {2} soif.", [needsCare , needsCare > 1 ? 's' : '' , needsCare > 1 ? 'ont' : 'a' ])}</span>
                <Link to="/reviews" className="btn btn-gold min-h-10">{T("Arroser le jardin")}</Link>
              </p>
            ) : (
              <p className="mt-4 text-ink-soft">{T("Tout ton jardin est en bonne santé. 🌞")}</p>
            )}
          </div>
        )}
      </Section>

      {/* Carnet des 14 derniers jours */}
      <Section title={T("Carnet de route")} glyph="暦">
        <p className="mb-3 text-ink-soft">{T("{0} jour{1} d’entraînement sur les 14 derniers{2}.", [activeDays , activeDays > 1 ? 's' : '' , s.accuracy !== null ? T(" · {0} % de bonnes réponses en moyenne", [s.accuracy]) : '' ])}</p>
        <ol className="grid grid-cols-7 gap-2">
          {last14.map((day, i) => {
            const on = day.answers > 0;
            const isToday = i === last14.length - 1;
            return (
              <motion.li key={day.date} initial={{ opacity: 0, scale: 0.7 }} animate={{ opacity: 1, scale: 1 }} transition={{ delay: i * 0.03 }} className={`flex aspect-square flex-col items-center justify-center rounded-2xl border-2 text-center ${isToday ? 'border-ink' : 'border-line'} ${on ? 'bg-surface' : 'bg-surface-2'}`} aria-label={`${shortDate(day.date)} : ${on ? T("{0} réponses, {1} XP", [day.answers, day.xp]) : T("pas d’entraînement")}`}>
                <span className="text-[10px] text-ink-soft sm:text-xs">{new Date(`${day.date}T12:00:00`).toLocaleDateString(DATE_LOCALE, { weekday: 'short' }).replace('.', '')}</span>
                {on ? (
                  <span aria-hidden="true" className="jp flex h-7 w-7 -rotate-6 items-center justify-center rounded-md border-2 border-[#C8323F] text-sm font-black text-[#C8323F] sm:h-9 sm:w-9 sm:text-base">済</span>
                ) : (
                  <span aria-hidden="true" className="h-7 w-7 rounded-md border-2 border-dashed border-line sm:h-9 sm:w-9" />
                )}
                <span className="text-[10px] font-bold sm:text-xs">{on ? `+${day.xp}` : '·'}</span>
              </motion.li>
            );
          })}
        </ol>
      </Section>

      {/* Vitrine des gardiens */}
      <Section title={T("Gardiens vaincus · {0}/{1}", [defeated, bosses.length])} glyph="勝">
        <ul className="grid grid-cols-3 gap-3 sm:grid-cols-5 lg:grid-cols-7">
          {bosses.map((b, i) => (
            <motion.li key={b.slug} initial={{ opacity: 0, y: 10 }} animate={{ opacity: 1, y: 0 }} transition={{ delay: i * 0.04 }} className={`flex flex-col items-center rounded-2xl p-2 text-center ${b.defeated ? 'bg-surface shadow-sm' : 'bg-surface-2'}`}>
              <div style={b.defeated ? undefined : { filter: 'brightness(0)', opacity: 0.18 }}>
                <BossCreature glyph={b.glyph} mood={b.defeated ? 'laugh' : 'idle'} size={72} title={b.defeated ? b.name : T("Gardien encore inconnu")} />
              </div>
              <span className="mt-1 text-xs font-bold leading-tight">{b.defeated ? b.name : '???'}</span>
              <span className="text-[10px] text-ink-soft">{b.island}</span>
            </motion.li>
          ))}
        </ul>
      </Section>

      {/* Succès et tableau d'honneur */}
      <div className="grid gap-4 sm:grid-cols-2">
        <Link to="/achievements" className="flex items-center gap-4 rounded-3xl border border-line bg-surface p-4 hover:border-ink-soft">
          <span aria-hidden="true" className="jp flex h-14 w-14 items-center justify-center rounded-full bg-gold text-3xl font-black text-[#2a1a00]">賞</span>
          <span><span className="block text-lg font-bold">{T("Mes succès")}</span><span className="text-sm text-ink-soft">{ach ? T("{0} badge{1} sur {2}", [ach.unlocked, ach.unlocked > 1 ? 's' : '', ach.total]) : T("Badges à débloquer")}</span></span>
        </Link>
        <a href="#examens" className="flex items-center gap-4 rounded-3xl border border-line bg-surface p-4 hover:border-ink-soft">
          <span aria-hidden="true" className="flex h-14 w-14 items-center justify-center rounded-full bg-surface-2 text-3xl">{bestExam === null ? '🎯' : bestExam >= 60 ? '🏆' : '🎖️'}</span>
          <span><span className="block text-lg font-bold">{T("Tableau d’honneur")}</span><span className="text-sm text-ink-soft">{bestExam === null ? T("Aucun examen blanc passé") : `Meilleur examen blanc : ${bestExam} %`}</span></span>
        </a>
      </div>

      <section id="examens" aria-labelledby="exams-title" className="scroll-mt-6">
        <h2 id="exams-title" className="text-xl">{T("Examens blancs")}</h2>
        {s.exams.length === 0 ? (
          <p className="mt-2 text-ink-soft">{T("Aucun examen blanc passé. Tu le trouveras à la fin du parcours N5.")}</p>
        ) : (
          <>
            {s.exams.length > 1 && (
              <Chart title={T("Évolution du score (%)")}>
                <LineChart data={s.exams.map((e, i) => ({ n: `#${i + 1}`, percent: e.percent }))}>
                  <CartesianGrid stroke="var(--line)" vertical={false} />
                  <XAxis dataKey="n" tick={axis} />
                  <YAxis tick={axis} domain={[0, 100]} width={32} />
                  <Tooltip contentStyle={tooltipStyle} formatter={(v) => [`${v} %`, T("Score")]} />
                  <Line type="monotone" dataKey="percent" stroke="var(--ink)" strokeWidth={2.5} dot={{ r: 4 }} />
                </LineChart>
              </Chart>
            )}
            <ul className="mt-3 flex flex-col gap-2">
              {[...s.exams].reverse().map((e) => (
                <li key={e.date} className="flex flex-wrap items-baseline justify-between gap-2 rounded-2xl border border-line bg-surface p-3">
                  <span>
                    <strong>{e.percent} %</strong> {e.passed ? <span className="text-ok">{T("(seuil atteint)")}</span> : <span className="text-ink-soft">{T("(seuil non atteint)")}</span>}
                    <span className="ml-2 text-sm text-ink-soft">{new Date(e.date).toLocaleDateString(DATE_LOCALE, { day: 'numeric', month: 'short', year: 'numeric' })}</span>
                  </span>
                  <span className="text-sm text-ink-soft">{e.sections.map((x) => `${x.title} ${x.percent} %`).join(', ')}</span>
                </li>
              ))}
            </ul>
          </>
        )}
      </section>

      <section id="notions" aria-labelledby="items-title">
        <h2 id="items-title" className="text-xl">{T("Grimoire des notions")}</h2>
        {s.items.length === 0 ? (
          <p className="mt-2 text-ink-soft">{T("Aucune notion pour l’instant.")}</p>
        ) : (
          <div className="mt-3 overflow-x-auto">
            <table className="w-full min-w-[520px] text-left">
              <thead className="text-sm text-ink-soft">
                <tr>
                  <th className="py-2 pr-3 font-normal">{T("Notion")}</th>
                  <th className="py-2 pr-3 font-normal">{T("Sens")}</th>
                  <th className="py-2 pr-3 font-normal">{T("Statut")}</th>
                  <th className="py-2 font-normal">{T("Prochaine révision")}</th>
                </tr>
              </thead>
              <tbody>
                {s.items.map((it) => (
                  <tr key={it.id} className="border-t border-line">
                    <td className="py-2 pr-3"><span lang="ja" className="jp text-xl">{it.front}</span>{it.reading && it.reading !== it.front && <span className="jp ml-2 text-sm text-ink-soft">{it.reading}</span>}</td>
                    <td className="py-2 pr-3">{it.meaning}</td>
                    <td className="py-2 pr-3"><span className="inline-flex items-center gap-2"><span className="h-2.5 w-2.5 rounded-full" style={{ background: MASTERY_COLOR[it.mastery] }} aria-hidden="true" />{MASTERY_LABEL[it.mastery]}</span></td>
                    <td className="py-2 text-sm text-ink-soft">{new Date(it.due).toLocaleString(DATE_LOCALE, { day: 'numeric', month: 'short', hour: '2-digit', minute: '2-digit' })}</td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        )}
      </section>

      <details className="group rounded-3xl border border-line bg-surface p-4">
        <summary className="cursor-pointer list-none font-bold">
          <span className="mr-2 inline-block transition-transform group-open:rotate-90">▸</span>{T("Statistiques détaillées (graphiques)")}</summary>
        <div className="mt-5">
      <div className="grid gap-10 lg:grid-cols-2">
        <Chart title={T("Temps d’étude par semaine (min)")}>
          <BarChart data={s.weeks.map((w) => ({ ...w, label: shortDate(w.weekStart) }))}>
            <CartesianGrid stroke="var(--line)" vertical={false} />
            <XAxis dataKey="label" tick={axis} />
            <YAxis tick={axis} allowDecimals={false} width={32} />
            <Tooltip contentStyle={tooltipStyle} formatter={(v) => [T("{0} min", [v]), T("Étude")]} />
            <Bar dataKey="minutes" fill="var(--ink)" radius={[6, 6, 0, 0]} />
          </BarChart>
        </Chart>
        <Chart title={T("Notions vues et maîtrisées (30 jours)")}>
          <LineChart data={s.growth.map((g) => ({ ...g, label: shortDate(g.date) }))}>
            <CartesianGrid stroke="var(--line)" vertical={false} />
            <XAxis dataKey="label" tick={axis} interval={6} />
            <YAxis tick={axis} allowDecimals={false} width={32} />
            <Tooltip contentStyle={tooltipStyle} />
            <Line type="monotone" dataKey="learned" name="Vues" stroke="var(--ink)" strokeWidth={2.5} dot={false} />
            <Line type="monotone" dataKey="mastered" name="Maîtrisées" stroke="var(--ok)" strokeWidth={2.5} dot={false} />
          </LineChart>
        </Chart>
        <Chart title={T("Activité quotidienne (réponses)")}>
          <BarChart data={daily}>
            <CartesianGrid stroke="var(--line)" vertical={false} />
            <XAxis dataKey="label" tick={axis} interval={6} />
            <YAxis tick={axis} allowDecimals={false} width={32} />
            <Tooltip contentStyle={tooltipStyle} />
            <Bar dataKey="correct" name="Bonnes réponses" stackId="a" fill="var(--ok)" />
            <Bar dataKey="answers" name="Total" fill="var(--surface-2)" />
          </BarChart>
        </Chart>
        <Chart title={T("Taux de bonnes réponses{0}", [s.accuracy !== null ? ` (moyenne ${s.accuracy} %)` : ''])}>
          <LineChart data={daily}>
            <CartesianGrid stroke="var(--line)" vertical={false} />
            <XAxis dataKey="label" tick={axis} interval={6} />
            <YAxis tick={axis} domain={[0, 100]} width={32} />
            <Tooltip contentStyle={tooltipStyle} formatter={(v) => [`${v} %`, T("Réussite")]} />
            <Line type="monotone" dataKey="accuracy" stroke="var(--gold)" strokeWidth={2.5} connectNulls dot={{ r: 3 }} />
          </LineChart>
        </Chart>
      </div>
        </div>
      </details>
    </div>
  );
}

function Chart({ title, children }: { title: string; children: React.ReactElement }) {
  return (
    <figure>
      <figcaption className="mb-2 font-bold">{title}</figcaption>
      <div className="h-56 w-full">
        <ResponsiveContainer width="100%" height="100%">{children}</ResponsiveContainer>
      </div>
    </figure>
  );
}
