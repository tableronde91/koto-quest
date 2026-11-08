import { useEffect, useMemo, useState } from 'react';
import { AnimatePresence, motion, useReducedMotion } from 'motion/react';
import { T } from '../i18n';

const COLORS = ['var(--gold)', 'var(--ko)', 'var(--ok)', '#F2A7BB', 'var(--ink)'];

/** Les animations décoratives sont coupées si l'utilisateur les a réduites (système ou réglage Koto Quest). */
export function useCalm() {
  const system = useReducedMotion();
  return !!system || (typeof document !== 'undefined' && document.documentElement.classList.contains('reduced'));
}

/** Pluie de confettis (décorative, non annoncée aux lecteurs d'écran). */
export function Confetti({ count = 36, origin = 'top' }: { count?: number; origin?: 'top' | 'center' }) {
  const calm = useCalm();
  const pieces = useMemo(
    () =>
      Array.from({ length: count }, (_, i) => ({
        id: i,
        x: (Math.random() - 0.5) * 2,
        delay: Math.random() * 0.25,
        rot: Math.random() * 540 - 270,
        color: COLORS[i % COLORS.length],
        w: 6 + Math.random() * 6,
        h: 8 + Math.random() * 10,
        round: i % 4 === 0,
      })),
    [count],
  );
  if (calm) return null;
  return (
    <div aria-hidden="true" className="pointer-events-none fixed inset-0 z-[60] overflow-hidden">
      {pieces.map((p) => (
        <motion.span
          key={p.id}
          className="absolute"
          style={{ left: '50%', top: origin === 'top' ? '-2%' : '45%', width: p.w, height: p.h, background: p.color, borderRadius: p.round ? '50%' : 2 }}
          initial={{ x: 0, y: 0, rotate: 0, opacity: 1 }}
          animate={{
            x: `${p.x * 48}vw`,
            y: origin === 'top' ? '105vh' : ['0vh', '-25vh', '60vh'],
            rotate: p.rot,
            opacity: [1, 1, 0],
          }}
          transition={{ duration: 2.2 + Math.random(), delay: p.delay, ease: origin === 'top' ? 'easeIn' : 'easeOut' }}
        />
      ))}
    </div>
  );
}

/** Petit « +10 XP » qui s'envole au-dessus d'un élément (positionné en relatif par le parent). */
export function FloatingXp({ amount }: { amount: number }) {
  const calm = useCalm();
  if (calm || amount <= 0) return null;
  return (
    <motion.span
      aria-hidden="true"
      className="pointer-events-none absolute -top-2 right-4 z-10 rounded-full bg-gold px-2 py-0.5 text-sm font-bold text-[#2a1a00] shadow"
      initial={{ y: 0, opacity: 0, scale: 0.6 }}
      animate={{ y: -42, opacity: [0, 1, 1, 0], scale: 1 }}
      transition={{ duration: 1.3, ease: 'easeOut' }}
    >{T("+{0} XP", [ amount ])}</motion.span>
  );
}

/** Nombre qui défile jusqu'à sa valeur (affiche directement la valeur si animations réduites). */
export function CountUp({ value, duration = 700 }: { value: number; duration?: number }) {
  const calm = useCalm();
  const [shown, setShown] = useState(calm ? value : 0);
  useEffect(() => {
    if (calm) {
      setShown(value);
      return;
    }
    const start = performance.now();
    let raf = 0;
    const tick = (t: number) => {
      const k = Math.min(1, (t - start) / duration);
      setShown(Math.round(value * (1 - Math.pow(1 - k, 3))));
      if (k < 1) raf = requestAnimationFrame(tick);
    };
    raf = requestAnimationFrame(tick);
    return () => cancelAnimationFrame(raf);
  }, [value, duration, calm]);
  return <>{shown}</>;
}

/** Flamme de série animée. */
export function Flame({ lit }: { lit: boolean }) {
  return (
    <motion.svg
      width="28"
      height="32"
      viewBox="0 0 28 32"
      aria-hidden="true"
      animate={lit ? { scaleY: [1, 1.08, 0.96, 1], rotate: [0, -2, 2, 0] } : {}}
      transition={{ duration: 1.4, repeat: Infinity }}
      style={{ transformOrigin: '50% 100%' }}
    >
      <path d="M14 1 C18 9 26 12 26 21 A12 11 0 0 1 2 21 C2 15 6 12 8 8 C9 12 11 13 12 13 C12 8 12 5 14 1Z" fill={lit ? 'var(--ko)' : 'var(--line)'} />
      <path d="M14 14 C16 18 20 19 20 23 A6 6 0 0 1 8 23 C8 20 10 19 11 17 C12 19 13 19 13 19 C13 17 13 16 14 14Z" fill={lit ? 'var(--gold)' : 'var(--surface-2)'} />
    </motion.svg>
  );
}

/** Bulle de dialogue du compagnon (le personnage de l'utilisateur). */
export function SpeechBubble({ children }: { children: React.ReactNode }) {
  return (
    <AnimatePresence mode="wait">
      <motion.div
        key={String(children)}
        initial={{ opacity: 0, scale: 0.85, x: -6 }}
        animate={{ opacity: 1, scale: 1, x: 0 }}
        exit={{ opacity: 0 }}
        transition={{ type: 'spring', stiffness: 260, damping: 20 }}
        className="relative rounded-2xl border border-line bg-surface px-4 py-3 shadow-sm"
        style={{ transformOrigin: '0% 50%' }}
      >
        <span aria-hidden="true" className="absolute -left-2 top-5 h-4 w-4 rotate-45 border-b border-l border-line bg-surface" />
        <span className="relative">{children}</span>
      </motion.div>
    </AnimatePresence>
  );
}

/** Grand idéogramme de résultat posé comme un tampon (hanko). */
export function Stamp({ children, className = '' }: { children: React.ReactNode; className?: string }) {
  return (
    <motion.p
      aria-hidden="true"
      className={className}
      initial={{ scale: 2.2, rotate: -10, opacity: 0 }}
      animate={{ scale: 1, rotate: 0, opacity: 1 }}
      transition={{ type: 'spring', stiffness: 320, damping: 16 }}
    >
      {children}
    </motion.p>
  );
}

/** Le personnage saute de joie (ou baisse la tête, puis se reprend). */
export function Cheer({ children, happy = true }: { children: React.ReactNode; happy?: boolean }) {
  return (
    <motion.div
      initial={{ y: 20, opacity: 0 }}
      animate={happy ? { y: [20, 0, -26, 0, -12, 0], opacity: 1 } : { y: 0, opacity: 1, rotate: [0, -4, 0] }}
      transition={{ duration: happy ? 1.2 : 0.8, delay: 0.2 }}
      style={{ transformOrigin: '50% 100%' }}
    >
      {children}
    </motion.div>
  );
}
