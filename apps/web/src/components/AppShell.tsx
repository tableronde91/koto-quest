import { ReactNode, useEffect, useState } from 'react';
import { NavLink, useLocation, useNavigate } from 'react-router';
import { AnimatePresence, motion } from 'motion/react';
import { useQueryClient } from '@tanstack/react-query';
import type { InboxItemDto, MeDto } from '@koto/shared';
import type { IssuedQuestionDto } from '@koto/shared';
import { api, post } from '../api/client';
import { qk, useInbox, useReviewSummary } from '../api/hooks';
import { Question } from './Question';
import { Avatar } from './Avatar';
import { Coins } from '../pages/Character';
import { AchievementWatcher } from './Achievements';
import { DuelInviteWatcher } from '../pages/Duel';
import { T } from '../i18n';

const NAV = [
  { to: '/', label: T("Accueil"), icon: 'M3 11l9-7 9 7v9a1 1 0 01-1 1h-5v-6h-6v6H4a1 1 0 01-1-1z' },
  { to: '/path', label: T("Parcours"), icon: "M5 20c3-1 4-4 7-4s4 3 7 2M7 12a2 2 0 100-4 2 2 0 000 4zM17 9a2 2 0 100-4 2 2 0 000 4zM8 10c3 0 5-2 8-3" },
  { to: '/characters', label: T("Caractères"), short: T("Kana"), glyph: 'あ', icon: '' },
  { to: '/expressions', label: T("Expressions"), short: T("Phrases"), glyph: '話', icon: '' },
  { to: '/reviews', label: T("Révisions"), icon: 'M4 12a8 8 0 0114-5.3M20 12a8 8 0 01-14 5.3M18 3v4h-4M6 21v-4h4' },
  { to: '/games', label: T("Jeux"), icon: 'M6 12h4M8 10v4M15 11h.01M18 13h.01M7 6h10a5 5 0 015 5v2a5 5 0 01-5 5c-1.5 0-2.5-1-3.5-2h-3c-1 1-2 2-3.5 2a5 5 0 01-5-5v-2a5 5 0 015-5z' },
  { to: '/duel', label: T("Duels"), glyph: '闘', icon: '' },
  { to: '/stats', label: T("Progrès"), icon: 'M4 20V10M10 20V4M16 20v-7M22 20H2' },
  { to: '/settings', label: T("Réglages"), icon: "M12 15a3 3 0 100-6 3 3 0 000 6zM19 12a7 7 0 00-.1-1.2l2-1.6-2-3.4-2.4 1a7 7 0 00-2-1.2L14 3h-4l-.5 2.6a7 7 0 00-2 1.2l-2.4-1-2 3.4 2 1.6A7 7 0 005 12c0 .4 0 .8.1 1.2l-2 1.6 2 3.4 2.4-1a7 7 0 002 1.2L10 21h4l.5-2.6a7 7 0 002-1.2l2.4 1 2-3.4-2-1.6c.1-.4.1-.8.1-1.2z" },
];

function Icon({ d, glyph }: { d: string; glyph?: string }) {
  if (glyph)
    return (
      <span aria-hidden="true" className="jp flex h-6 w-6 items-center justify-center rounded-md border-2 border-current text-sm font-bold leading-none">
        {glyph}
      </span>
    );
  return (
    <svg width="24" height="24" viewBox="0 0 24 24" fill="none" aria-hidden="true">
      <path d={d} stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" />
    </svg>
  );
}

export function AppShell({ me, children }: { me: MeDto; children: ReactNode }) {
  const { data: reviews } = useReviewSummary();
  const due = reviews?.due ?? 0;
  const location = useLocation();
  const immersive = /^\/(lesson|quiz|boss|games|exam|duel)\//.test(location.pathname) || location.pathname === '/placement' || location.pathname === '/reviews/session' || location.pathname.startsWith('/characters/practice') || location.pathname.startsWith('/expressions/practice');

  return (
    <div className="min-h-dvh md:flex">
      <a href="#main" className="sr-only focus:not-sr-only focus:absolute focus:left-2 focus:top-2 focus:z-50 focus:rounded-lg focus:bg-surface focus:p-3">{T("Aller au contenu")}</a>
      {!immersive && (
        <nav aria-label={T("Navigation principale")} className="sticky top-0 hidden h-dvh w-60 shrink-0 flex-col gap-1 border-r border-line p-4 md:flex">
          <div className="mb-6 flex items-center gap-3 px-2">
            <img src="/icons/icon.svg" alt="" className="h-10 w-10" />
            <div>
              <p className="font-display text-lg leading-tight">{T("Koto Quest")}</p>
              <p className="jp text-sm text-ink-soft">言葉の旅</p>
            </div>
          </div>
          {NAV.map((n) => (
            <NavLink
              key={n.to}
              to={n.to}
              end={n.to === '/'}
              className={({ isActive }) => `flex min-h-12 items-center gap-3 rounded-xl px-3 font-bold ${isActive ? 'bg-ink text-paper' : 'text-ink-soft hover:bg-surface-2 hover:text-ink'}`}
            >
              <Icon d={n.icon} glyph={(n as { glyph?: string }).glyph} />
              <span className="flex-1">{n.label}</span>
              {n.to === '/reviews' && due > 0 && <span className="rounded-full bg-gold px-2 text-sm text-[#2a1a00]">{due}</span>}
            </NavLink>
          ))}
          <NavLink to="/avatar" className={({ isActive }) => `mt-auto flex items-center gap-3 rounded-2xl p-2 ${isActive ? 'bg-surface-2' : 'hover:bg-surface-2'}`} aria-label={T("Mon personnage, {0} pièces", [me.coins])}>
            <span className="overflow-hidden rounded-xl border border-line"><Avatar config={me.avatar} size={48} /></span>
            <span className="min-w-0">
              <span className="block truncate font-bold">{me.displayName}</span>
              <Coins value={me.coins} className="text-sm text-gold-ink" />
            </span>
          </NavLink>
        </nav>
      )}

      <main id="main" className={`mx-auto w-full flex-1 px-4 pt-6 sm:px-8 ${immersive ? 'max-w-3xl pb-10' : 'max-w-5xl pb-28 md:pb-12'}`}>
        {children}
      </main>

      {!immersive && (
        <nav aria-label={T("Navigation principale")} className="fixed inset-x-0 bottom-0 z-30 grid grid-cols-8 border-t border-line bg-surface pb-[env(safe-area-inset-bottom)] md:hidden">
          {NAV.filter((n) => n.to !== '/settings').map((n) => (
            <NavLink key={n.to} to={n.to} end={n.to === '/'} aria-label={n.label} className={({ isActive }) => `relative flex min-h-16 flex-col items-center justify-center gap-0.5 text-[10px] font-bold ${isActive ? 'text-ink' : 'text-ink-soft'}`}>
              <Icon d={n.icon} glyph={(n as { glyph?: string }).glyph} />
              {(n as { short?: string }).short ?? n.label}
              {n.to === '/reviews' && due > 0 && <span className="absolute right-[22%] top-2 h-2.5 w-2.5 rounded-full bg-gold" aria-label={T("{0} révisions", [due])} />}
            </NavLink>
          ))}
        </nav>
      )}

      <ChallengePopup me={me} paused={immersive} />
      <AchievementWatcher />
      <DuelInviteWatcher path={location.pathname} />
    </div>
  );
}

/**
 * Popup interactive in-app : quand un rappel est dû et que l'application est ouverte,
 * le mini-quiz s'affiche directement (fonctionne aussi si le push est refusé).
 */
function ChallengePopup({ me, paused }: { me: MeDto; paused: boolean }) {
  const { data: inbox } = useInbox(!paused);
  const [current, setCurrent] = useState<InboxItemDto | null>(null);
  const [question, setQuestion] = useState<Awaited<ReturnType<typeof loadQuestion>> | null>(null);
  const [dismissed, setDismissed] = useState<Set<string>>(new Set());
  const qc = useQueryClient();
  const navigate = useNavigate();

  useEffect(() => {
    if (paused || current) return;
    const next = inbox?.find((n) => n.questionId && !dismissed.has(n.id));
    if (next) setCurrent(next);
  }, [inbox, paused, current, dismissed]);

  useEffect(() => {
    if (!current?.questionId) return;
    post(`/notifications/${current.id}/open`).catch(() => undefined);
    loadQuestion(current.questionId).then(setQuestion).catch(() => close());
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [current?.id]);

  useEffect(() => {
    if (!current) return;
    const onKey = (e: KeyboardEvent) => e.key === 'Escape' && close();
    window.addEventListener('keydown', onKey);
    return () => window.removeEventListener('keydown', onKey);
  });

  function close() {
    if (current) setDismissed(new Set([...dismissed, current.id]));
    setCurrent(null);
    setQuestion(null);
    qc.invalidateQueries({ queryKey: qk.inbox });
    qc.invalidateQueries({ queryKey: qk.dashboard });
    qc.invalidateQueries({ queryKey: qk.reviews });
  }

  return (
    <AnimatePresence>
      {current && question && (
        <motion.div className="fixed inset-0 z-50 flex items-end justify-center bg-[rgb(10_14_40/0.55)] p-3 sm:items-center" initial={{ opacity: 0 }} animate={{ opacity: 1 }} exit={{ opacity: 0 }}>
          <motion.div
            role="dialog"
            aria-modal="true"
            aria-labelledby="challenge-title"
            initial={{ y: 40 }}
            animate={{ y: 0 }}
            className="max-h-[92dvh] w-full max-w-xl overflow-y-auto rounded-3xl bg-paper p-5 shadow-2xl"
          >
            <div className="mb-4 flex items-start justify-between gap-3">
              <h2 id="challenge-title" className="text-xl">{current.body}</h2>
              <button className="rounded-full p-2 text-ink-soft hover:bg-surface-2" onClick={close} aria-label={T("Plus tard")}>
                <svg width="20" height="20" viewBox="0 0 24 24" aria-hidden="true"><path d="M6 6l12 12M18 6L6 18" stroke="currentColor" strokeWidth="2.5" strokeLinecap="round" /></svg>
              </button>
            </div>
            {question.answered ? (
              <p>{T("Ce défi a déjà été relevé.")}</p>
            ) : (
              <Question question={question.question} furigana={me.preferences.showFurigana} onDone={close} continueLabel={T("Fermer")} />
            )}
            <button className="mt-4 text-sm text-ink-soft underline" onClick={() => { close(); navigate('/settings#rappels'); }}>{T("Régler la fréquence des défis")}</button>
          </motion.div>
        </motion.div>
      )}
    </AnimatePresence>
  );
}

function loadQuestion(id: string) {
  return api<{ question: IssuedQuestionDto; answered: boolean }>(`/questions/${id}`);
}
