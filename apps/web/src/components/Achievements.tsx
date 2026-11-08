import { useCallback, useEffect, useRef, useState } from 'react';
import { Link, useLocation } from 'react-router';
import { AnimatePresence, motion } from 'motion/react';
import { useQueryClient } from '@tanstack/react-query';
import type { AchievementCheckDto, AchievementDto } from '@koto/shared';
import { PROGRESS_EVENT, post } from '../api/client';
import { Confetti } from './Celebrate';
import { T } from '../i18n';

export const RARITY_LABEL: Record<AchievementDto['rarity'], string> = { common: T("Courant"), rare: T("Rare"), epic: T("Épique") };
const RARITY_RING: Record<AchievementDto['rarity'], string> = { common: '#B9835A', rare: '#6E8FB5', epic: 'var(--gold)' };

/** Médaille d'un succès : idéogramme au centre, anneau de rareté ; grisée avec jauge si verrouillée. */
export function Medal({ a, size = 72 }: { a: Pick<AchievementDto, 'glyph' | 'rarity' | 'unlocked' | 'value' | 'target'>; size?: number }) {
  const ring = RARITY_RING[a.rarity];
  const r = 34;
  const c = 2 * Math.PI * r;
  const pct = a.unlocked ? 1 : a.value / a.target;
  return (
    <svg viewBox="0 0 80 80" width={size} height={size} aria-hidden="true" className="shrink-0">
      {a.unlocked && a.rarity !== 'common' && (
        <g fill={ring} opacity={0.35}>
          {Array.from({ length: 12 }, (_, i) => (
            <path key={i} d="M40 2 L43 12 L37 12Z" transform={`rotate(${i * 30} 40 40)`} />
          ))}
        </g>
      )}
      <circle cx="40" cy="40" r={r} fill={a.unlocked ? 'var(--surface)' : 'var(--surface-2)'} stroke="var(--line)" strokeWidth="5" />
      {pct > 0 && (
        <circle cx="40" cy="40" r={r} fill="none" stroke={a.unlocked ? ring : 'var(--ink-soft)'} strokeWidth="5" strokeDasharray={`${c * pct} ${c}`} strokeLinecap="round" transform="rotate(-90 40 40)" />
      )}
      <circle cx="40" cy="40" r="26" fill={a.unlocked ? ring : 'transparent'} opacity={a.unlocked ? 0.16 : 1} />
      <text x="40" y="51" textAnchor="middle" fontSize="30" fontWeight="900" className="jp" fill={a.unlocked ? 'var(--ink)' : 'var(--line)'}>
        {a.glyph}
      </text>
    </svg>
  );
}

/**
 * Vérifie les succès après chaque étape importante (fin de leçon, gardien, jeu, examen, achat)
 * et à chaque changement de page, puis affiche les nouveaux succès un par un.
 */
export function AchievementWatcher() {
  const qc = useQueryClient();
  const location = useLocation();
  const [queue, setQueue] = useState<AchievementDto[]>([]);
  const timer = useRef<number | undefined>(undefined);
  const busy = useRef(false);

  const check = useCallback(() => {
    window.clearTimeout(timer.current);
    timer.current = window.setTimeout(async () => {
      if (busy.current) return;
      busy.current = true;
      try {
        const r = await post<AchievementCheckDto>('/achievements/check');
        if (r.unlocked.length) {
          setQueue((q) => [...q, ...r.unlocked]);
          qc.invalidateQueries({ queryKey: ['achievements'] });
          qc.invalidateQueries({ queryKey: ['me'] });
          qc.invalidateQueries({ queryKey: ['dashboard'] });
          qc.invalidateQueries({ queryKey: ['shop'] });
        }
      } catch {
        // Silencieux : la vérification sera refaite à la prochaine étape.
      } finally {
        busy.current = false;
      }
    }, 500);
  }, [qc]);

  useEffect(() => {
    window.addEventListener(PROGRESS_EVENT, check);
    return () => window.removeEventListener(PROGRESS_EVENT, check);
  }, [check]);
  useEffect(() => check(), [location.pathname, check]);

  // Pendant un exercice, on garde la notification pour la fin : pas de distraction en pleine réponse.
  const [busyAnswering, setBusyAnswering] = useState(false);
  useEffect(() => {
    if (!queue.length) return;
    const probe = () => setBusyAnswering(!!document.querySelector('[data-testid="question"], [data-testid="exam-question"]'));
    probe();
    const id = window.setInterval(probe, 700);
    return () => window.clearInterval(id);
  }, [queue.length]);

  const current = busyAnswering ? undefined : queue[0];
  useEffect(() => {
    if (!current) return;
    const t = window.setTimeout(() => setQueue((q) => q.slice(1)), 5000);
    return () => window.clearTimeout(t);
  }, [current]);

  return (
    <div className="pointer-events-none fixed inset-x-0 top-3 z-[70] flex justify-center px-3" role="status" aria-live="polite">
      <AnimatePresence mode="wait">
        {current && (
          <motion.div
            key={current.slug}
            data-testid="achievement-toast"
            initial={{ y: -80, opacity: 0, scale: 0.9 }}
            animate={{ y: 0, opacity: 1, scale: 1 }}
            exit={{ y: -60, opacity: 0 }}
            transition={{ type: 'spring', stiffness: 300, damping: 22 }}
            className="pointer-events-auto flex w-full max-w-md items-center gap-4 rounded-3xl border border-line bg-surface p-3 pr-4 shadow-xl"
          >
            {current.rarity === 'epic' && <Confetti count={40} />}
            <motion.div initial={{ rotate: -120, scale: 0.4 }} animate={{ rotate: 0, scale: 1 }} transition={{ type: 'spring', stiffness: 200, damping: 12, delay: 0.1 }}>
              <Medal a={current} size={64} />
            </motion.div>
            <div className="min-w-0 flex-1">
              <p className="text-xs font-bold uppercase tracking-wide text-gold-ink">{T("Succès débloqué · {0}", [ RARITY_LABEL[current.rarity]])}</p>
              <p className="truncate text-lg font-bold">{current.title}</p>
              <p className="text-sm text-ink-soft">{current.description} <span className="font-bold text-gold-ink">{T("+{0} pièces", [ current.coins ])}</span></p>
            </div>
            <div className="flex flex-col items-end gap-1">
              <Link to="/achievements" className="text-sm font-bold underline" onClick={() => setQueue([])}>{T("Voir")}</Link>
              <button type="button" className="text-sm text-ink-soft" onClick={() => setQueue((q) => q.slice(1))} aria-label={T("Fermer")}>✕</button>
            </div>
          </motion.div>
        )}
      </AnimatePresence>
    </div>
  );
}
