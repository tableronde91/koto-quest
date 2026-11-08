import { motion } from 'motion/react';
import type { DuelRankDto } from '@koto/shared';
import { useCalm } from './Celebrate';
import { T } from '../i18n';

/** Écusson de rang : blason à la couleur du rang, idéogramme et division (I à III). */
export function RankBadge({ rank, size = 64, glow = false }: { rank: DuelRankDto; size?: number; glow?: boolean }) {
  const calm = useCalm();
  const division = /\b(I{1,3})$/.exec(rank.label)?.[1] ?? '';
  const jpSize = rank.jp.length >= 3 ? 20 : rank.jp.length === 2 ? 25 : 34;
  return (
    <motion.svg
      viewBox="0 0 80 92"
      width={size}
      height={(size * 92) / 80}
      role="img"
      aria-label={T("Rang {0}", [rank.label])}
      animate={glow && !calm ? { filter: [`drop-shadow(0 0 0px ${rank.color})`, `drop-shadow(0 0 10px ${rank.color})`, `drop-shadow(0 0 0px ${rank.color})`] } : undefined}
      transition={{ duration: 2.2, repeat: Infinity }}
    >
      <path d="M40 2 L74 14 L72 52 Q66 76 40 90 Q14 76 8 52 L6 14Z" fill={rank.color} stroke="#1B2550" strokeWidth="3" />
      <path d="M40 9 L67 19 L65 51 Q60 70 40 82 Q20 70 15 51 L13 19Z" fill="none" stroke="#FFFFFF" strokeOpacity="0.55" strokeWidth="1.6" />
      {rank.tierId === 'tenka' && <path d="M24 6 L30 0 L36 6 L40 0 L44 6 L50 0 L56 6" fill="none" stroke="#F2C14E" strokeWidth="3" strokeLinejoin="round" />}
      <text x="40" y={division ? 48 : 54} textAnchor="middle" fontSize={jpSize} fontWeight="900" fontFamily="'Noto Sans JP', sans-serif" stroke="#1B2550" strokeWidth="3" strokeLinejoin="round" style={{ fill: '#FFFFFF', paintOrder: 'stroke' }}>
        {rank.jp}
      </text>
      {division && (
        <text x="40" y="70" textAnchor="middle" fontSize="13" fontWeight="900" fill="#FFFFFF" fontFamily="serif" letterSpacing="1">
          {division}
        </text>
      )}
    </motion.svg>
  );
}

/** Deux katanas croisés (recherche d'adversaire, en-têtes). */
export function CrossedSwords({ size = 96, spin = false }: { size?: number; spin?: boolean }) {
  const calm = useCalm();
  const blade = (rot: number) => (
    <g transform={`rotate(${rot} 50 50)`}>
      <path d="M50 6 L53 12 L53 66 L47 66 L47 12Z" fill="#E6ECF2" stroke="#1B2550" strokeWidth="2" />
      <rect x="40" y="66" width="20" height="5" rx="2" fill="#C9A227" stroke="#1B2550" strokeWidth="2" />
      <rect x="46" y="71" width="8" height="22" rx="2" fill="#2B1B3F" stroke="#1B2550" strokeWidth="2" />
      <path d="M46 75 l8 4 M46 81 l8 4 M46 87 l8 4" stroke="#C8323F" strokeWidth="1.5" />
    </g>
  );
  return (
    <motion.svg viewBox="0 0 100 100" width={size} height={size} aria-hidden="true" animate={spin && !calm ? { rotate: [0, -8, 8, 0] } : undefined} transition={{ duration: 1.4, repeat: Infinity, ease: 'easeInOut' }}>
      {blade(-35)}
      {blade(35)}
    </motion.svg>
  );
}

/** Plaque de vie d'un duelliste. */
export function HpPlate({ name, rank, hp, max, combo, align = 'left', answered }: { name: string; rank: DuelRankDto; hp: number; max: number; combo: number; align?: 'left' | 'right'; answered?: boolean }) {
  const pct = Math.max(0, Math.min(100, (hp / max) * 100));
  const tone = pct <= 25 ? 'var(--ko)' : pct <= 50 ? 'var(--gold)' : 'var(--ok)';
  return (
    <div className={`relative flex w-full min-w-0 flex-col gap-1 rounded-2xl bg-[rgb(255_255_255/0.93)] p-2.5 text-[#1B2550] shadow ${align === 'right' ? 'items-end text-right' : ''}`}>
      <div className={`flex w-full items-center gap-2 ${align === 'right' ? 'flex-row-reverse' : ''}`}>
        <span className="hidden shrink-0 sm:block"><RankBadge rank={rank} size={26} /></span>
        <div className="min-w-0 flex-1">
          <p className="truncate text-sm font-bold leading-tight">{name}</p>
          <p className="truncate text-[11px] leading-tight opacity-75">{rank.label}</p>
        </div>
      </div>
      <div className="relative h-3 w-full overflow-hidden rounded-full bg-[#E3DED4]" role="progressbar" aria-label={T("Vie de {0}", [name])} aria-valuenow={hp} aria-valuemin={0} aria-valuemax={max}>
        <motion.div className={`absolute inset-y-0 rounded-full ${align === 'right' ? 'right-0' : 'left-0'}`} style={{ background: tone }} animate={{ width: `${pct}%` }} transition={{ duration: 0.5, ease: 'easeOut' }} />
      </div>
      <div className={`flex w-full flex-wrap items-center justify-between gap-x-2 gap-y-0.5 whitespace-nowrap text-[11px] font-bold tabular-nums ${align === 'right' ? 'flex-row-reverse' : ''}`}>
        <span>{T("PV {0}/{1}", [ hp , max])}</span>
        {combo >= 2 && <span className="text-[#C8323F]">🔥 ×{combo}</span>}
      </div>
      {answered && (
        <motion.span initial={{ scale: 0 }} animate={{ scale: 1 }} className="absolute -bottom-3 rounded-full bg-[#1B2550] px-2 py-0.5 text-[10px] font-bold text-white shadow">{T("✓ a répondu")}</motion.span>
      )}
    </div>
  );
}
