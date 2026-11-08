import { Link } from 'react-router';
import { motion } from 'motion/react';
import { CountUp, Flame, SpeechBubble } from '../components/Celebrate';
import { Avatar } from '../components/Avatar';
import { Coins } from './Character';
import { useAchievements, useDashboard } from '../api/hooks';
import { Medal } from '../components/Achievements';
import { ErrorBox, ProgressBar, Spinner } from '../components/ui';
import { formatDuration } from '../lib/format';
import { T, DATE_LOCALE } from '../i18n';

function greeting() {
  const h = new Date().getHours();
  return h < 11 ? 'おはよう' : h < 18 ? 'こんにちは' : 'こんばんは';
}

export function DashboardPage() {
  const { data: d, isLoading, error, refetch } = useDashboard();
  if (isLoading) return <Spinner />;
  if (error || !d) return <ErrorBox error={error} onRetry={refetch} />;

  const hasReviews = d.reviews.due > 0;
  return (
    <div className="flex flex-col gap-8">
      <header className="flex items-start gap-4">
        <div className="min-w-0 flex-1">
        <p lang="ja" className="jp text-xl text-ink-soft">{greeting()}、{d.displayName}</p>
        <h1 className="mt-1 text-3xl sm:text-4xl">
          {hasReviews ? T("{0} notion{1} à réviser", [d.reviews.due, d.reviews.due > 1 ? 's' : '']) : d.nextLesson ? T("Prêt·e pour la suite ?") : T("Tout est à jour")}
        </h1>
        </div>
        <div className="flex shrink-0 flex-col items-end gap-2">
          <Link to="/avatar?t=boutique" className="rounded-full border border-line bg-surface px-3 py-1.5 text-gold-ink" aria-label={T("{0} pièces, ouvrir la boutique", [d.coins])}>
            <Coins value={d.coins} />
          </Link>
          <Link to="/settings" className="rounded-full p-2 text-ink-soft hover:bg-surface-2 md:hidden" aria-label={T("Réglages")}>
            <svg width="22" height="22" viewBox="0 0 24 24" fill="none" aria-hidden="true"><circle cx="12" cy="12" r="3" stroke="currentColor" strokeWidth="2" /><path d="M19 12a7 7 0 00-.1-1.2l2-1.6-2-3.4-2.4 1a7 7 0 00-2-1.2L14 3h-4l-.5 2.6a7 7 0 00-2 1.2l-2.4-1-2 3.4 2 1.6A7 7 0 005 12c0 .4 0 .8.1 1.2l-2 1.6 2 3.4 2.4-1a7 7 0 002 1.2L10 21h4l.5-2.6a7 7 0 002-1.2l2.4 1 2-3.4-2-1.6c.1-.4.1-.8.1-1.2z" stroke="currentColor" strokeWidth="2" strokeLinejoin="round" /></svg>
          </Link>
        </div>
      </header>

      {/* Le personnage de l'utilisateur sert de compagnon : un conseil contextuel */}
      <section aria-label={T("Message de ton compagnon")} className="flex items-center gap-3">
        <Link to="/avatar" aria-label={T("Mon personnage")} className="shrink-0">
          <motion.div animate={{ y: [0, -4, 0] }} transition={{ duration: 2.6, repeat: Infinity, ease: 'easeInOut' }}>
            <Avatar config={d.avatar} size={76} />
          </motion.div>
        </Link>
        <SpeechBubble>{companionLine(d, hasReviews)}</SpeechBubble>
      </section>

      {/* Action principale : une seule chose à faire maintenant */}
      <section aria-label={T("Prochaine étape")} className="relative overflow-hidden rounded-3xl bg-ink p-6 text-paper sm:p-8">
        <span aria-hidden="true" className="jp pointer-events-none absolute -right-4 -top-10 select-none text-[11rem] font-black leading-none opacity-10">
          {hasReviews ? '復' : '学'}
        </span>
        {hasReviews ? (
          <>
            <p className="max-w-[45ch] opacity-85">{T("Ces notions sont sur le point de t’échapper. Une révision maintenant les fixe pour plusieurs jours.")}</p>
            <Link to="/reviews/session" className="btn btn-gold mt-5">{T("Réviser maintenant")}</Link>
            {d.nextLesson && <Link to={`/lesson/${d.nextLesson.slug}`} className="ml-3 mt-5 inline-block underline opacity-90">{T("ou continuer la leçon « {0} »", [ d.nextLesson.title ])}</Link>}
          </>
        ) : d.nextLesson ? (
          <>
            <p className="opacity-75">{d.nextLesson.worldTitle}</p>
            <p className="jp mt-1 text-2xl font-bold sm:text-3xl">{d.nextLesson.title}</p>
            <Link to={`/lesson/${d.nextLesson.slug}`} className="btn btn-gold mt-5">{T("Commencer la leçon")}</Link>
          </>
        ) : (
          <p>{T("Tu as terminé tout le contenu disponible. Les révisions continueront d’arriver au bon moment.")}</p>
        )}
        {d.plan.catchUpMode && (
          <p className="mt-4 max-w-[55ch] text-sm opacity-85">{T("Tu as un peu de retard : on limite les nouveautés aujourd’hui pour que les révisions restent raisonnables.")}</p>
        )}
      </section>

      {d.suggestPlacement && (
        <section className="flex flex-col gap-3 rounded-3xl border-2 border-dashed border-gold p-5 sm:flex-row sm:items-center">
          <span aria-hidden="true" className="jp text-4xl font-black text-gold-ink">診断</span>
          <div className="flex-1">
            <p className="font-bold">{T("Tu connais déjà des bases ?")}</p>
            <p className="text-ink-soft">{T("Le test de positionnement valide les mondes que tu maîtrises, en 5 minutes environ.")}</p>
          </div>
          <Link to="/placement" className="btn btn-quiet">{T("Passer le test")}</Link>
        </section>
      )}

      <section aria-label={T("Ta progression")} className="grid grid-cols-2 gap-x-6 gap-y-5 lg:grid-cols-4">
        <Stat label={T("Série")} icon={<Flame lit={d.streak.todayDone} />} value={<><CountUp value={d.streak.current} />{' '}{T("jour")}{d.streak.current > 1 ? 's' : ''}</>} note={d.streak.todayDone ? T("Fait aujourd’hui") : T("Pas encore aujourd’hui")} />
        <Stat label={T("Aujourd’hui")} value={formatDuration(d.today.seconds)} note={d.today.accuracy !== null ? T("{0} % de réussite", [d.today.accuracy]) : T("Objectif : {0} min", [d.plan.estimatedMinutes])} />
        <Stat label={T("Mots maîtrisés")} value={<CountUp value={d.mastered.words} />} note={T("{0} kana, {1} points de grammaire", [d.mastered.kana, d.mastered.grammar])} />
        <Stat label={T("Kanji maîtrisés")} value={<CountUp value={d.mastered.kanji} />} note={d.reviews.learningSoon ? T("{0} révision(s) dans l’heure", [d.reviews.learningSoon]) : ' '} />
      </section>

      <div className="grid gap-8 lg:grid-cols-[1.2fr_1fr]">
        <section aria-labelledby="quests-title">
          <h2 id="quests-title" className="text-xl">{T("Quêtes du jour")}</h2>
          <ul className="mt-3 flex flex-col gap-3">
            {d.quests.map((q) => (
              <li key={q.id} className="flex items-center gap-4 rounded-2xl border border-line bg-surface p-4">
                <span aria-hidden="true" className="jp flex h-10 w-10 shrink-0 items-center justify-center rounded-full text-lg font-bold" style={{ background: q.done ? 'var(--gold)' : 'var(--surface-2)', color: q.done ? '#2a1a00' : 'var(--ink-soft)' }}>
                  {q.done ? '済' : '・'}
                </span>
                <div className="flex-1">
                  <p className="font-bold">{q.title}</p>
                  <div className="mt-2 flex items-center gap-3">
                    <ProgressBar value={q.progress} max={q.target} label={q.title} tone={q.done ? 'gold' : 'ink'} />
                    <span className="shrink-0 text-sm text-ink-soft">{q.progress}/{q.target}</span>
                  </div>
                </div>
                <span className="text-right text-sm font-bold text-gold-ink">{q.xp}{' '}{T("XP")}<br /><span className="font-normal text-ink-soft">{T("+5 pièces")}</span></span>
              </li>
            ))}
          </ul>
        </section>

        <section aria-labelledby="level-title" className="flex flex-col gap-5">
          <div>
            <h2 id="level-title" className="text-xl">{T("Niveau {0}", [ d.xp.level])}</h2>
            <div className="mt-2"><ProgressBar value={d.xp.intoLevel} max={d.xp.forNext} label={T("Expérience vers le niveau suivant")} tone="gold" /></div>
            <p className="mt-1 text-sm text-ink-soft">{T("{0} XP avant le niveau {1}, {2} XP au total", [d.xp.forNext - d.xp.intoLevel , d.xp.level + 1 , d.xp.total ])}</p>
          </div>
          <AchievementsStrip />
          <Link to="/prepa" className="flex items-center gap-4 rounded-2xl border border-line p-4 hover:border-ink-soft">
            <span aria-hidden="true" className="jp flex h-11 w-11 shrink-0 items-center justify-center rounded-xl bg-[#8E1B26] text-xl font-black text-white">試</span>
            <span><span className="block font-bold">{T("Atelier JLPT")}</span><span className="text-sm text-ink-soft">{T("Kanji, orthographe, grammaire, ★, écoute : au format de l’examen.")}</span></span>
          </Link>
          <div>
            <h2 className="text-xl">{T("Parcours {0}", [ d.targetLevel])}</h2>
            <div className="mt-2"><ProgressBar value={d.progress.completedLessons} max={d.progress.totalLessons} label={T("Leçons {0} terminées", [d.targetLevel])} tone="ok" /></div>
            <p className="mt-1 text-sm text-ink-soft">{T("{0} leçon(s) sur {1} disponibles", [d.progress.completedLessons , d.progress.totalLessons ])}</p>
          </div>
          <div className="rounded-2xl border border-line p-4">
            <p className="font-bold">{T("Préparation estimée : {0} %", [ d.readiness.percent ])}</p>
            <p className="text-sm text-ink-soft">{T("{0}. Estimation volontairement prudente, calculée sur le contenu de Koto Quest ; ce n’est pas une prédiction de réussite au JLPT officiel.", [d.readiness.label ])}</p>
            {d.examDate && <p className="mt-1 text-sm">{T("Examen prévu le {0}.", [ new Date(d.examDate).toLocaleDateString(DATE_LOCALE, { day: 'numeric', month: 'long', year: 'numeric' }) ])}</p>}
          </div>
          {!d.notifications.consent && (
            <div className="rounded-2xl bg-surface-2 p-4">
              <p className="font-bold">{T("Reçois tes défis dans la journée")}</p>
              <p className="text-sm text-ink-soft">{T("Une question courte, au bon moment, pour ancrer ce que tu viens d’apprendre.")}</p>
              <Link to="/settings#rappels" className="btn btn-quiet mt-3">{T("Activer les défis")}</Link>
            </div>
          )}
        </section>
      </div>
    </div>
  );
}

function Stat({ label, value, note, icon }: { label: string; value: React.ReactNode; note: string; icon?: React.ReactNode }) {
  return (
    <motion.div className="border-l-4 border-gold pl-4" initial={{ opacity: 0, y: 8 }} animate={{ opacity: 1, y: 0 }}>
      <p className="text-sm text-ink-soft">{label}</p>
      <p className="flex items-center gap-2 font-display text-2xl">{icon}<span>{value}</span></p>
      <p className="text-sm text-ink-soft">{note}</p>
    </motion.div>
  );
}

/** Aperçu des succès : derniers obtenus, sinon les plus proches. */
function AchievementsStrip() {
  const { data } = useAchievements();
  if (!data) return null;
  const unlocked = data.achievements.filter((a) => a.unlocked).sort((x, y) => (y.unlockedAt ?? '').localeCompare(x.unlockedAt ?? ''));
  const next = data.achievements.filter((a) => !a.unlocked).sort((x, y) => y.value / y.target - x.value / x.target);
  const shown = [...unlocked.slice(0, 3), ...next].slice(0, 4);
  return (
    <Link to="/achievements" className="block rounded-2xl border border-line p-4 hover:border-ink-soft" aria-label={T("Succès : {0} sur {1}, voir tous", [data.unlocked, data.total])}>
      <p className="flex items-baseline justify-between"><span className="text-xl font-bold">{T("Succès")}</span><span className="text-sm text-ink-soft">{T("{0}/{1} · tout voir", [data.unlocked , data.total ])}</span></p>
      <div className="mt-2 flex gap-2">{shown.map((a) => <Medal key={a.slug} a={a} size={52} />)}</div>
    </Link>
  );
}

type Dash = NonNullable<ReturnType<typeof useDashboard>['data']>;
function companionLine(d: Dash, hasReviews: boolean): string {
  if (hasReviews) return T("Quelques notions commencent à s’effacer… On les revoit ensemble ?");
  if (!d.streak.todayDone && d.streak.current > 0) return T("Ta série de {0} jour{1} t’attend : une petite leçon suffit !", [d.streak.current, d.streak.current > 1 ? 's' : '']);
  if (d.streak.todayDone && d.quests.every((q) => q.done)) return T("Toutes les quêtes du jour sont faites. お疲れさま！");
  if (d.nextLesson) return T("Prochaine étape : « {0} ». がんばって！", [d.nextLesson.title]);
  return T("Tout est à jour. Un mini-jeu pour garder la main ?");
}
