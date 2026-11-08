import { useEffect, useMemo, useRef } from 'react';
import { motion } from 'motion/react';
import type { AvatarConfig, PathWorldDto } from '@koto/shared';
import { Avatar } from './Avatar';
import { useCalm } from './Celebrate';
import { T } from '../i18n';

/**
 * Carte du niveau en archipel : chaque monde est une île, reliée à la suivante par un chemin
 * lumineux (ou un pont quand elles sont proches). Le personnage se tient sur l'île en cours ;
 * toucher une île fait défiler jusqu'à ses leçons. Illustration 100 % vectorielle et originale.
 */
const W = 1000;
const H = 600;

/** Gabarit de 9 emplacements, du sud-ouest au sud-est en serpentant (comme un parcours de jeu de plateau). */
const SLOTS = [
  { x: 150, y: 440 },
  { x: 360, y: 375 },
  { x: 175, y: 230 },
  { x: 385, y: 125 },
  { x: 590, y: 110 },
  { x: 575, y: 300 },
  { x: 680, y: 450 },
  { x: 820, y: 235 },
  { x: 900, y: 440 },
];
function islandPositions(n: number) {
  // Mêmes emplacements pour tous les niveaux : les îles restantes apparaissent dans la brume (contenu à venir).
  if (n <= 9) return SLOTS.slice(0, n).map((p, i) => ({ ...p, slot: i }));
  // Au-delà de 9 mondes : grille en serpentin.
  const cols = Math.ceil(n / 3);
  return Array.from({ length: n }, (_, i) => {
    const row = Math.floor(i / cols);
    const col = row % 2 === 0 ? i % cols : cols - 1 - (i % cols);
    return { x: 110 + (col * (W - 220)) / Math.max(1, cols - 1), y: 470 - row * 170, slot: i % 9 };
  });
}

export type WorldState = 'done' | 'current' | 'open' | 'soon';

export function worldStates(worlds: PathWorldDto[]): WorldState[] {
  const finished = (w: PathWorldDto) => !w.comingSoon && w.progress.completed === w.progress.total && (!w.boss || w.boss.defeated) && (!w.exam || w.exam.passed);
  let currentIdx = worlds.findIndex((w) => !w.comingSoon && !w.optional && !finished(w));
  if (currentIdx < 0) currentIdx = worlds.findIndex((w) => !w.comingSoon && !finished(w));
  return worlds.map((w, i) => (w.comingSoon ? 'soon' : finished(w) ? 'done' : i === currentIdx ? 'current' : 'open'));
}

// ───────────── Formes ─────────────

/** Petit générateur déterministe : la même île garde la même forme d'un affichage à l'autre. */
function rng(seed: number) {
  let s = seed * 9301 + 49297;
  return () => {
    s = (s * 9301 + 49297) % 233280;
    return s / 233280;
  };
}

/** Contour organique fermé (courbes lissées autour d'un centre). */
function blob(cx: number, cy: number, rx: number, ry: number, seed: number, wobble = 0.18, n = 10) {
  const r = rng(seed);
  const pts = Array.from({ length: n }, (_, i) => {
    const a = (i / n) * Math.PI * 2;
    const k = 1 - wobble / 2 + r() * wobble;
    return [cx + Math.cos(a) * rx * k, cy + Math.sin(a) * ry * k];
  });
  const mid = (a: number[], b: number[]) => [(a[0] + b[0]) / 2, (a[1] + b[1]) / 2];
  let d = `M${mid(pts[n - 1], pts[0]).join(' ')}`;
  pts.forEach((p, i) => {
    const m = mid(p, pts[(i + 1) % n]);
    d += ` Q${p[0].toFixed(1)} ${p[1].toFixed(1)} ${m[0].toFixed(1)} ${m[1].toFixed(1)}`;
  });
  return `${d}Z`;
}

// ───────────── Décors ─────────────

const SAKURA = '#F4A9C0';
const SAKURA_DARK = '#E07A9B';
const LEAF = '#4E8B4A';
const LEAF_DARK = '#356B3A';
const WOOD = '#7A4E2D';
const VERMILION = '#C8323F';
const SAND = '#EBD9AE';
const ROCK = '#7D7468';
const ROCK_DARK = '#5A5249';

function Tree({ x, y, s = 1, pink = false }: { x: number; y: number; s?: number; pink?: boolean }) {
  return (
    <g transform={`translate(${x} ${y}) scale(${s})`}>
      <rect x="-1.6" y="-4" width="3.2" height="10" fill={WOOD} />
      <circle cx="0" cy="-9" r="9" fill={pink ? SAKURA : LEAF} />
      <circle cx="-5" cy="-6" r="6" fill={pink ? SAKURA_DARK : LEAF_DARK} opacity={0.55} />
    </g>
  );
}

function Palm({ x, y, s = 1 }: { x: number; y: number; s?: number }) {
  return (
    <g transform={`translate(${x} ${y}) scale(${s})`}>
      <path d="M0 6 Q2 -8 -2 -20" stroke={WOOD} strokeWidth="2.6" fill="none" />
      {[-60, -20, 20, 60, 150].map((a) => (
        <path key={a} d="M-2 -20 q8 -4 15 3" stroke={LEAF} strokeWidth="3.4" fill="none" strokeLinecap="round" transform={`rotate(${a} -2 -20)`} />
      ))}
    </g>
  );
}

function Hut({ x, y, s = 1 }: { x: number; y: number; s?: number }) {
  return (
    <g transform={`translate(${x} ${y}) scale(${s})`}>
      <rect x="-10" y="-8" width="20" height="12" fill="#B8865A" />
      <path d="M-15 -7 L0 -20 L15 -7Z" fill="#8C6A3F" />
      <rect x="-3" y="-3" width="6" height="7" fill="#3B2A1C" />
      <rect x="4" y="-5" width="4" height="3" fill="#FFD27A" />
    </g>
  );
}

function Torii({ x, y, s = 1 }: { x: number; y: number; s?: number }) {
  return (
    <g transform={`translate(${x} ${y}) scale(${s})`} fill={VERMILION}>
      <path d="M-18 -30 Q0 -34 18 -30 L18 -26 Q0 -30 -18 -26Z" fill="#2B2B2B" />
      <rect x="-16" y="-26" width="32" height="4" />
      <rect x="-12" y="-19" width="24" height="3" />
      <rect x="-12" y="-24" width="4" height="26" />
      <rect x="8" y="-24" width="4" height="26" />
    </g>
  );
}

function Pagoda({ x, y, s = 1 }: { x: number; y: number; s?: number }) {
  return (
    <g transform={`translate(${x} ${y}) scale(${s})`}>
      {[0, 1, 2].map((i) => (
        <g key={i} transform={`translate(0 ${-i * 13})`}>
          <rect x={-9 + i * 1.5} y="-9" width={18 - i * 3} height="9" fill="#C59B6B" />
          <path d={`M${-17 + i * 2} -8 Q0 ${-16} ${17 - i * 2} -8 L${12 - i * 2} -12 L${-12 + i * 2} -12Z`} fill="#3A2F2A" />
        </g>
      ))}
      <path d="M0 -50 V-40" stroke="#C9A24A" strokeWidth="2" />
    </g>
  );
}

function Lighthouse({ x, y, s = 1, calm }: { x: number; y: number; s?: number; calm: boolean }) {
  return (
    <g transform={`translate(${x} ${y}) scale(${s})`}>
      <path d="M-6 0 L-4 -34 L4 -34 L6 0Z" fill="#F5F1E8" />
      <rect x="-5" y="-22" width="10" height="5" fill={VERMILION} />
      <rect x="-5" y="-10" width="10" height="5" fill={VERMILION} />
      <rect x="-5" y="-41" width="10" height="7" fill="#FFE08A" />
      <path d="M-7 -41 L0 -48 L7 -41Z" fill={VERMILION} />
      {!calm && (
        <motion.path d="M0 -38 L60 -52 L60 -24Z" fill="#FFE9A8" opacity={0.35} style={{ transformOrigin: '0px -38px' }} animate={{ rotate: [0, 360] }} transition={{ duration: 8, repeat: Infinity, ease: 'linear' }} />
      )}
    </g>
  );
}

function Fuji({ x, y, s = 1 }: { x: number; y: number; s?: number }) {
  return (
    <g transform={`translate(${x} ${y}) scale(${s})`}>
      <path d="M-48 4 L-10 -50 Q0 -58 10 -50 L48 4Z" fill="#5E6B78" />
      <path d="M-10 -50 Q0 -58 10 -50 L20 -36 L12 -40 L5 -32 L-2 -40 L-9 -33 L-20 -36Z" fill="#FFFFFF" />
      <path d="M-48 4 L-20 -30 L-14 4Z" fill="#4E5A66" opacity={0.6} />
    </g>
  );
}

function Bamboo({ x, y, s = 1 }: { x: number; y: number; s?: number }) {
  return (
    <g transform={`translate(${x} ${y}) scale(${s})`}>
      {[-12, -6, 0, 6, 12].map((dx, i) => (
        <g key={dx}>
          <rect x={dx - 1.6} y={-38 + (i % 2) * 6} width="3.2" height={40 - (i % 2) * 6} fill="#6FAE4F" />
          <path d={`M${dx} ${-30 + i} q8 -4 12 2 M${dx} ${-20 + i} q-8 -4 -12 2`} stroke="#4E8B3A" strokeWidth="2.4" fill="none" strokeLinecap="round" />
        </g>
      ))}
    </g>
  );
}

function Lanterns({ x, y, s = 1, calm }: { x: number; y: number; s?: number; calm: boolean }) {
  return (
    <g transform={`translate(${x} ${y}) scale(${s})`}>
      <path d="M-24 -28 Q0 -18 24 -28" stroke="#3B2A1C" strokeWidth="1.5" fill="none" />
      {[-16, 0, 16].map((dx, i) => (
        <motion.g key={dx} animate={calm ? undefined : { opacity: [0.85, 1, 0.85] }} transition={{ duration: 2 + i * 0.4, repeat: Infinity }}>
          <ellipse cx={dx} cy={-20 + (i === 1 ? 3 : 0)} rx="5" ry="6.5" fill="#FF9A3D" />
          <ellipse cx={dx} cy={-20 + (i === 1 ? 3 : 0)} rx="9" ry="10" fill="#FFB65C" opacity={0.25} />
        </motion.g>
      ))}
      <Hut x={0} y={2} s={1.1} />
    </g>
  );
}

function Waterfall({ x, y, s = 1, calm }: { x: number; y: number; s?: number; calm: boolean }) {
  return (
    <g transform={`translate(${x} ${y}) scale(${s})`}>
      <path d="M-14 -30 L14 -30 L10 6 L-10 6Z" fill={ROCK_DARK} />
      <rect x="-6" y="-30" width="12" height="36" fill="#BFE8F2" />
      {!calm && (
        <motion.rect x="-6" y="-30" width="12" height="36" fill="url(#km-fall)" animate={{ y: [-30, -24] }} transition={{ duration: 0.6, repeat: Infinity, ease: 'linear' }} />
      )}
      <ellipse cx="0" cy="8" rx="14" ry="4" fill="#FFFFFF" opacity={0.7} />
    </g>
  );
}

function Shrine({ x, y, s = 1 }: { x: number; y: number; s?: number }) {
  return (
    <g transform={`translate(${x} ${y}) scale(${s})`}>
      <rect x="-14" y="-14" width="28" height="14" fill="#E9DCC3" />
      <path d="M-22 -13 Q0 -30 22 -13Z" fill="#2F3B4A" />
      <rect x="-4" y="-10" width="8" height="10" fill={VERMILION} />
      <Torii x={-30} y={4} s={0.8} />
    </g>
  );
}

const LANDMARKS = ['torii', 'village', 'waterfall', 'pagoda', 'fuji', 'bamboo', 'lighthouse', 'lanterns', 'shrine'] as const;
type Landmark = (typeof LANDMARKS)[number];

function LandmarkFor({ kind, calm }: { kind: Landmark; calm: boolean }) {
  switch (kind) {
    case 'torii':
      return <><Hut x={-18} y={4} /><Torii x={20} y={14} s={1.1} /><Palm x={-36} y={8} /></>;
    case 'village':
      return <><Hut x={-16} y={2} s={1.2} /><Hut x={14} y={-4} /><Hut x={6} y={14} s={0.9} /></>;
    case 'waterfall':
      return <><Waterfall x={-10} y={4} calm={calm} /><Pagoda x={22} y={6} s={0.7} /></>;
    case 'pagoda':
      return <Pagoda x={0} y={10} s={1.1} />;
    case 'fuji':
      return <Fuji x={0} y={14} s={1.05} />;
    case 'bamboo':
      return <><Bamboo x={-6} y={10} /><Hut x={20} y={10} s={0.8} /></>;
    case 'lighthouse':
      return <><Lighthouse x={14} y={8} calm={calm} /><Hut x={-16} y={10} s={0.9} /></>;
    case 'lanterns':
      return <Lanterns x={0} y={10} s={1.1} calm={calm} />;
    case 'shrine':
      return <Shrine x={8} y={10} s={1.15} />;
  }
}

// ───────────── Île ─────────────

function Island({ x, y, slot, seed, landmark, state, calm }: { x: number; y: number; slot: number; seed: number; landmark: Landmark; state: WorldState; calm: boolean }) {
  const rx = 74;
  const ry = 44;
  const pink = slot % 2 === 0;
  if (state === 'done') return <RuinedIsland x={x} y={y} seed={seed} landmark={landmark} calm={calm} />;
  return (
    <g transform={`translate(${x} ${y})`}>
      {/* Hauts-fonds turquoise, ombre portée, falaise, plage puis végétation */}
      <path d={blob(0, 10, rx + 26, ry + 22, seed + 1, 0.25)} fill="#5FD1C9" opacity={0.35} />
      <path d={blob(0, 18, rx + 4, ry + 6, seed + 2)} fill={ROCK_DARK} />
      <path d={blob(0, 10, rx, ry, seed + 2)} fill={ROCK} />
      <path d={blob(0, 2, rx - 4, ry - 6, seed + 3)} fill={SAND} />
      <path d={blob(4, -2, rx - 16, ry - 14, seed + 4, 0.28)} fill="#6FA85A" />
      <path d={blob(-8, -6, rx - 34, ry - 24, seed + 5, 0.3)} fill="#5B9A4C" />
      {/* Écume */}
      <path d={blob(0, 14, rx + 6, ry + 8, seed + 2)} fill="none" stroke="#FFFFFF" strokeWidth="2" strokeDasharray="10 14" opacity={0.6} />
      <Tree x={-52} y={0} pink={pink} />
      <Tree x={48} y={-6} s={0.9} pink={!pink} />
      <Palm x={54} y={14} s={0.8} />
      <Tree x={-38} y={-18} s={0.75} />
      <g transform="translate(0 -6)"><LandmarkFor kind={landmark} calm={calm} /></g>
      {state === 'soon' && <path d={blob(0, 0, rx + 20, ry + 20, seed + 6, 0.2)} fill="#E8EEF2" opacity={0.75} />}
    </g>
  );
}

/** Souche calcinée (arbre brûlé). */
function Stump({ x, y, s = 1, tilt = 0 }: { x: number; y: number; s?: number; tilt?: number }) {
  return (
    <g transform={`translate(${x} ${y}) scale(${s}) rotate(${tilt})`}>
      <path d="M-3 6 L-2 -8 L-4 -14 M-2 -8 L1 -16 L3 -10 L3 6Z" fill="#2B231D" stroke="#2B231D" strokeWidth="1.6" strokeLinejoin="round" />
      <path d="M1 -10 l5 -5 M-2 -4 l-5 -3" stroke="#2B231D" strokeWidth="1.4" strokeLinecap="round" />
      <ellipse cx="0" cy="6" rx="5" ry="1.6" fill="#1E1915" opacity={0.6} />
    </g>
  );
}

/** Colonne de fumée qui s'élève (fixe si les animations sont réduites). */
function Smoke({ x, y, delay = 0, calm }: { x: number; y: number; delay?: number; calm: boolean }) {
  const puffs = [0, 1, 2];
  if (calm)
    return (
      <g transform={`translate(${x} ${y})`} opacity={0.5}>
        <circle cx="0" cy="-6" r="5" fill="#6E6862" />
        <circle cx="4" cy="-16" r="7" fill="#837D76" />
        <circle cx="-2" cy="-28" r="9" fill="#9A948D" opacity={0.7} />
      </g>
    );
  return (
    <g transform={`translate(${x} ${y})`}>
      {puffs.map((i) => (
        <motion.circle
          key={i}
          r="7"
          fill="#5E5853"
          initial={{ cx: 0, cy: 0, opacity: 0, scale: 0.6 }}
          animate={{ cx: [0, 4, -3, 6], cy: [0, -14, -30, -46], opacity: [0, 0.85, 0.55, 0], scale: [0.6, 1.3, 1.9, 2.5] }}
          transition={{ duration: 4.2, repeat: Infinity, delay: delay + i * 1.4, ease: 'easeOut' }}
        />
      ))}
    </g>
  );
}

/** Drapeau de victoire planté sur une île conquise. */
function VictoryFlag({ x, y, calm }: { x: number; y: number; calm: boolean }) {
  return (
    <g transform={`translate(${x} ${y})`}>
      <ellipse cx="0" cy="2" rx="6" ry="2" fill="#1E1915" opacity={0.5} />
      <rect x="-1.3" y="-44" width="2.6" height="46" rx="1" fill="#3A2A1E" />
      <circle cx="0" cy="-45" r="2.4" fill="#F2C14E" />
      <motion.g style={{ transformOrigin: '1px -42px' }} animate={calm ? undefined : { skewY: [0, -6, 0, 5, 0], scaleX: [1, 0.94, 1, 0.97, 1] }} transition={{ duration: 2.4, repeat: Infinity, ease: 'easeInOut' }}>
        <path d="M1 -42 L28 -38 Q24 -32 28 -26 L1 -24Z" fill={VERMILION} stroke="#8E1B26" strokeWidth="1" />
        <text x="13" y="-28.5" textAnchor="middle" fontSize="11" fontWeight="900" fill="#FFF6E0" fontFamily="'Noto Sans JP', sans-serif">勝</text>
      </motion.g>
    </g>
  );
}

/**
 * Île conquise : terre brûlée, falaise fissurée, végétation réduite en souches,
 * repère effondré et calciné, fumée qui monte… et le drapeau de victoire du joueur.
 */
function RuinedIsland({ x, y, seed, landmark, calm }: { x: number; y: number; seed: number; landmark: Landmark; calm: boolean }) {
  const rx = 74;
  const ry = 44;
  const tilt = seed % 2 === 0 ? -9 : 8;
  return (
    <g transform={`translate(${x} ${y})`}>
      {/* Eaux troublées par les cendres */}
      <path d={blob(0, 10, rx + 26, ry + 22, seed + 1, 0.25)} fill="#5E8C88" opacity={0.35} />
      <path d={blob(0, 18, rx + 4, ry + 6, seed + 2)} fill="#3F3933" />
      <path d={blob(0, 10, rx, ry, seed + 2)} fill="#5F5750" />
      {/* Fissures dans la falaise */}
      <g stroke="#2A2420" strokeWidth="1.6" fill="none" strokeLinecap="round" strokeLinejoin="round">
        <path d="M-58 26 l6 -6 l-2 -6 l5 -5" />
        <path d="M22 44 l3 -8 l-4 -5 l6 -7" />
        <path d="M60 22 l-5 -4 l2 -6" />
      </g>
      <path d={blob(0, 2, rx - 4, ry - 6, seed + 3)} fill="#B9A887" />
      {/* Terre brûlée */}
      <path d={blob(4, -2, rx - 16, ry - 14, seed + 4, 0.28)} fill="#6B5A47" />
      <path d={blob(-8, -6, rx - 34, ry - 24, seed + 5, 0.3)} fill="#54473A" />
      <ellipse cx="-4" cy="-2" rx="46" ry="24" fill="url(#km-scorch)" />
      {/* Écume grise */}
      <path d={blob(0, 14, rx + 6, ry + 8, seed + 2)} fill="none" stroke="#D9D4CC" strokeWidth="2" strokeDasharray="6 18" opacity={0.45} />
      <Stump x={-52} y={0} tilt={-6} />
      <Stump x={48} y={-6} s={0.9} tilt={10} />
      <Stump x={56} y={14} s={0.7} tilt={-14} />
      <Stump x={-38} y={-18} s={0.75} tilt={4} />
      {/* Repère effondré : penché, calciné, à moitié enfoui */}
      <g transform={`translate(0 2) rotate(${tilt}) translate(0 -8)`} filter="url(#km-ruin)" opacity={0.92}>
        <LandmarkFor kind={landmark} calm />
      </g>
      {/* Gravats au pied du repère */}
      <g fill="#4A423B" stroke="#2A2420" strokeWidth="0.8">
        <path d="M-22 10 l6 -5 l7 2 l1 5Z" />
        <path d="M10 12 l5 -6 l8 1 l-1 6Z" />
        <path d="M-6 14 l4 -4 l5 1 l0 4Z" />
        <path d="M26 4 l4 -3 l4 2 l-1 3Z" />
      </g>
      {/* Braises */}
      {[[-30, 6], [18, -4], [-12, -16], [34, 10]].map(([ex, ey], i) =>
        calm ? (
          <circle key={i} cx={ex} cy={ey} r="1.8" fill="#FF8A3D" opacity={0.7} />
        ) : (
          <motion.circle key={i} cx={ex} cy={ey} r="1.8" fill="#FF8A3D" animate={{ opacity: [0.2, 1, 0.2] }} transition={{ duration: 1.4 + i * 0.3, repeat: Infinity }} />
        ),
      )}
      <Smoke x={-18} y={-10} calm={calm} />
      <Smoke x={22} y={-14} delay={0.7} calm={calm} />
      <VictoryFlag x={-44} y={14} calm={calm} />
    </g>
  );
}

/** Îlot encore inexploré : silhouette dans la brume, sans interaction. */
function MistyIslet({ x, y, seed }: { x: number; y: number; seed: number }) {
  return (
    <g transform={`translate(${x} ${y})`} opacity={0.55} aria-hidden="true">
      <path d={blob(0, 14, 66, 36, seed, 0.3)} fill="#5FD1C9" opacity={0.25} />
      <path d={blob(0, 10, 52, 28, seed + 1)} fill="#6D7F84" />
      <path d={blob(0, 2, 44, 22, seed + 2, 0.3)} fill="#7FA184" />
      <Tree x={-14} y={0} s={0.8} />
      <Tree x={12} y={-4} s={0.7} />
      <path d={blob(0, 0, 80, 46, seed + 3, 0.2)} fill="#E8F1F2" opacity={0.7} filter="url(#km-soft)" />
      <text y="6" textAnchor="middle" fontSize="22" fontWeight="900" fill="#FFFFFF" opacity={0.9}>?</text>
    </g>
  );
}

/** Pont de bois à rambardes vermillon entre deux îles proches. */
function Bridge({ a, b }: { a: { x: number; y: number }; b: { x: number; y: number } }) {
  const dx = b.x - a.x;
  const dy = b.y - a.y;
  const len = Math.hypot(dx, dy);
  const ux = dx / len;
  const uy = dy / len;
  const s = { x: a.x + ux * 66, y: a.y + uy * 40 };
  const e = { x: b.x - ux * 66, y: b.y - uy * 40 };
  const nx = -uy * 6;
  const ny = ux * 6;
  const line = (ox: number, oy: number) => `M${s.x + ox} ${s.y + oy} Q${(s.x + e.x) / 2 + ox} ${(s.y + e.y) / 2 + oy - 14} ${e.x + ox} ${e.y + oy}`;
  return (
    <g>
      <path d={line(0, 6)} stroke="#000" strokeOpacity={0.15} strokeWidth="12" fill="none" />
      <path d={line(0, 0)} stroke={WOOD} strokeWidth="11" fill="none" />
      <path d={line(0, 0)} stroke="#C9A06B" strokeWidth="8" strokeDasharray="2 3" fill="none" />
      <path d={line(nx, ny)} stroke={VERMILION} strokeWidth="2" fill="none" />
      <path d={line(-nx, -ny)} stroke={VERMILION} strokeWidth="2" fill="none" />
    </g>
  );
}

function Boat({ x, y, s = 1, flip = false, drift, calm }: { x: number; y: number; s?: number; flip?: boolean; drift: number; calm: boolean }) {
  return (
    <motion.g initial={{ x, y }} animate={calm ? { x, y } : { x: [x, x + drift, x], y: [y, y - 3, y] }} transition={{ duration: 14, repeat: Infinity, ease: 'easeInOut' }}>
      <g transform={`scale(${flip ? -s : s} ${s})`}>
        <path d="M-12 0 L12 0 L8 6 L-8 6Z" fill={WOOD} />
        <path d="M0 0 V-20" stroke="#3B2A1C" strokeWidth="1.5" />
        <path d="M1 -19 L12 -4 L1 -4Z" fill={VERMILION} />
        <path d="M-1 -16 L-9 -4 L-1 -4Z" fill="#F5F1E8" />
        <path d="M-16 8 Q0 11 16 8" stroke="#FFFFFF" strokeWidth="1.2" fill="none" opacity={0.7} />
      </g>
    </motion.g>
  );
}

export function WorldMap({ worlds, avatar, region }: { worlds: PathWorldDto[]; avatar: AvatarConfig; region: string }) {
  const calm = useCalm();
  const pts = useMemo(() => islandPositions(worlds.length), [worlds.length]);
  const states = worldStates(worlds);
  const current = Math.max(0, states.indexOf('current'));
  const scroller = useRef<HTMLDivElement>(null);
  // Sur petit écran, la carte défile : on centre l'île en cours.
  useEffect(() => {
    const el = scroller.current;
    if (!el || el.scrollWidth <= el.clientWidth) return;
    el.scrollLeft = (pts[current].x / W) * el.scrollWidth - el.clientWidth / 2;
  }, [current, pts]);
  const go = (slug: string) => document.getElementById(`w-${slug}`)?.scrollIntoView({ behavior: 'smooth', block: 'start' });

  // Chemins : pont si les îles sont proches, sinon pointillés lumineux sur l'eau.
  const segments = pts.slice(1).map((b, i) => {
    const a = pts[i];
    const dist = Math.hypot(b.x - a.x, b.y - a.y);
    const mx = (a.x + b.x) / 2 + (b.y - a.y) * 0.18;
    const my = (a.y + b.y) / 2 - (b.x - a.x) * 0.12;
    return { a, b, bridge: dist < 225 && Math.abs(b.y - a.y) < dist * 0.45, d: `M${a.x} ${a.y} Q${mx} ${my} ${b.x} ${b.y}`, reached: i < current || states[i + 1] === 'done' };
  });
  const petals = useMemo(() => Array.from({ length: 10 }, (_, i) => ({ x: (i * 97) % W, d: 9 + (i % 4) * 2, delay: i * 1.3 })), []);

  return (
    <figure className="mb-10 overflow-hidden rounded-3xl border border-line shadow-sm">
      <figcaption className="sr-only">{T("Carte de l’archipel {0} : {1} îles{2}.", [ region , worlds.length , worlds.length < SLOTS.length ? T(", d’autres restent à découvrir") : '' ])}</figcaption>
      <div ref={scroller} className="overflow-x-auto">
        <svg viewBox={`0 0 ${W} ${H}`} className="block h-auto w-full min-w-[720px]" role="group" aria-label={T("Carte : {0}", [region])}>
          <defs>
            <linearGradient id="km-sea" x1="0" y1="0" x2="0" y2="1">
              <stop offset="0" stopColor="#1E6F8E" />
              <stop offset="0.55" stopColor="#1A8C9C" />
              <stop offset="1" stopColor="#127A86" />
            </linearGradient>
            <radialGradient id="km-sun" cx="0.92" cy="0.02" r="0.55">
              <stop offset="0" stopColor="#FFD58A" stopOpacity="0.85" />
              <stop offset="0.4" stopColor="#FFB86B" stopOpacity="0.25" />
              <stop offset="1" stopColor="#FFB86B" stopOpacity="0" />
            </radialGradient>
            <linearGradient id="km-fall" x1="0" y1="0" x2="0" y2="1">
              <stop offset="0" stopColor="#FFFFFF" stopOpacity="0" />
              <stop offset="0.5" stopColor="#FFFFFF" stopOpacity="0.8" />
              <stop offset="1" stopColor="#FFFFFF" stopOpacity="0" />
            </linearGradient>
            <filter id="km-glow" x="-50%" y="-50%" width="200%" height="200%">
              <feGaussianBlur stdDeviation="3" result="b" />
              <feMerge><feMergeNode in="b" /><feMergeNode in={"SourceGraphic"} /></feMerge>
            </filter>
            <filter id="km-soft"><feGaussianBlur stdDeviation="6" /></filter>
            {/* Repère calciné : désaturé et assombri */}
            <filter id="km-ruin">
              <feColorMatrix type="matrix" values="0.26 0.42 0.08 0 0  0.22 0.4 0.08 0 0  0.2 0.36 0.1 0 0  0 0 0 1 0" />
            </filter>
            <radialGradient id="km-scorch">
              <stop offset="0" stopColor="#2E2620" stopOpacity="0.75" />
              <stop offset="1" stopColor="#2E2620" stopOpacity="0" />
            </radialGradient>
            <pattern id="km-waves" width="80" height="40" patternUnits="userSpaceOnUse">
              <path d="M4 20 q6 -4 12 0 M48 34 q9 -5 18 0" stroke="#FFFFFF" strokeWidth="1.2" fill="none" opacity={0.1} strokeLinecap="round" />
            </pattern>
          </defs>

          {/* Océan, reflets et soleil couchant */}
          <rect width={W} height={H} fill="url(#km-sea)" />
          <motion.rect x="-80" width={W + 160} height={H} fill="url(#km-waves)" animate={calm ? undefined : { x: [-80, 0] }} transition={{ duration: 12, repeat: Infinity, ease: 'linear' }} />
          <rect width={W} height={H} fill="url(#km-sun)" />

          {/* Îles lointaines à l'horizon */}
          <g opacity={0.55}>
            <path d={blob(60, 22, 70, 14, 91)} fill="#2E5E57" />
            <path d={blob(760, 18, 90, 12, 92)} fill="#2E5E57" />
            <path d={blob(960, 70, 40, 10, 93)} fill="#2E5E57" />
          </g>

          {/* Nuages */}
          {[{ x: 120, y: 60, s: 1 }, { x: 660, y: 40, s: 0.8 }, { x: 900, y: 140, s: 0.7 }].map((c, i) => (
            <motion.g key={i} initial={{ x: c.x, y: c.y }} animate={calm ? undefined : { x: [c.x, c.x + 40, c.x] }} transition={{ duration: 30 + i * 6, repeat: Infinity, ease: 'easeInOut' }} opacity={0.85}>
              <g transform={`scale(${c.s})`} filter="url(#km-soft)">
                <ellipse cx="0" cy="0" rx="60" ry="16" fill="#FFFFFF" />
                <ellipse cx="-20" cy="-10" rx="30" ry="14" fill="#FFFFFF" />
                <ellipse cx="22" cy="-8" rx="26" ry="12" fill="#FFFFFF" />
              </g>
            </motion.g>
          ))}

          {/* Bateaux */}
          <Boat x={470} y={530} s={1.2} drift={60} calm={calm} />
          <Boat x={640} y={200} drift={-50} flip calm={calm} />
          <Boat x={90} y={330} s={0.8} drift={40} calm={calm} />
          <Boat x={950} y={250} s={0.9} drift={-30} flip calm={calm} />

          {/* Chemins : sous les îles */}
          {segments.map((s, i) =>
            s.bridge ? null : (
              <g key={i}>
                <path d={s.d} fill="none" stroke="#FFF3C4" strokeWidth="6" strokeDasharray="0.1 15" strokeLinecap="round" opacity={s.reached ? 1 : 0.7} filter="url(#km-glow)" />
                {s.reached && !calm && (
                  <motion.path d={s.d} fill="none" stroke="#FFFFFF" strokeWidth="6" strokeDasharray="0.1 16" strokeLinecap="round" animate={{ strokeDashoffset: [0, -32] }} transition={{ duration: 2, repeat: Infinity, ease: 'linear' }} opacity={0.7} />
                )}
              </g>
            ),
          )}

          {/* Branches de cerisier aux coins (sous les îles) */}
          <g pointerEvents="none">
            <path d="M0 560 Q60 520 120 540 M40 530 Q70 490 60 470" stroke="#5B3A2A" strokeWidth="6" fill="none" strokeLinecap="round" />
            {[[30, 525], [62, 505], [95, 530], [120, 545], [58, 470], [15, 555], [80, 488]].map(([cx, cy], i) => (
              <circle key={i} cx={cx} cy={cy} r={i % 2 ? 13 : 16} fill={i % 3 ? SAKURA : SAKURA_DARK} opacity={0.95} />
            ))}
            <path d="M1000 590 Q930 560 870 580 M960 575 Q940 540 955 520" stroke="#5B3A2A" strokeWidth="6" fill="none" strokeLinecap="round" />
            {[[985, 575], [940, 560], [905, 578], [872, 585], [955, 522], [925, 540]].map(([cx, cy], i) => (
              <circle key={i} cx={cx} cy={cy} r={i % 2 ? 13 : 16} fill={i % 3 ? SAKURA : SAKURA_DARK} opacity={0.95} />
            ))}
          </g>
          {/* Îles encore à découvrir */}
          {worlds.length < SLOTS.length && SLOTS.slice(worlds.length).map((p, i) => <MistyIslet key={i} x={p.x} y={p.y} seed={200 + i * 11} />)}
          {worlds.length < SLOTS.length && worlds.length > 0 && (
            <path d={`M${pts[worlds.length - 1].x} ${pts[worlds.length - 1].y} Q${(pts[worlds.length - 1].x + SLOTS[worlds.length].x) / 2 + 30} ${(pts[worlds.length - 1].y + SLOTS[worlds.length].y) / 2} ${SLOTS[worlds.length].x} ${SLOTS[worlds.length].y}`} fill="none" stroke="#FFF3C4" strokeWidth="5" strokeDasharray="0.1 15" strokeLinecap="round" opacity={0.3} />
          )}

          {/* Îles */}
          {worlds.map((w, i) => {
            const p = pts[i];
            // Chaque archipel a ses propres repères : décalage selon le niveau (n5 → 0, n4 → 3, n3 → 6…).
            const lvl = Number(/^n(\d)/.exec(w.slug)?.[1] ?? 5);
            const scenic = LANDMARKS.filter((l) => l !== 'shrine');
            const landmark: Landmark = w.exam ? 'shrine' : scenic[(p.slot + (5 - lvl) * 3) % scenic.length];
            return <Island key={w.slug} x={p.x} y={p.y} slot={p.slot} seed={i * 7 + w.order * 13} landmark={landmark} state={states[i]} calm={calm} />;
          })}

          {/* Ponts : par-dessus l'eau, entre deux îles proches */}
          {segments.map((s, i) => (s.bridge ? <Bridge key={i} a={s.a} b={s.b} /> : null))}

          {/* Sceaux, noms et interaction */}
          {worlds.map((w, i) => {
            const p = pts[i];
            const st = states[i];
            const glyph = w.exam ? '試' : w.boss?.glyph ?? String(w.order);
            const detail = w.exam && w.progress.total === 0 ? (w.exam.passed ? T("examen blanc réussi") : 'examen blanc') : T("{0} leçons sur {1}", [w.progress.completed, w.progress.total]);
            const label = T("Île {0} : {1}, {2}", [w.order, w.title, st === 'done' ? T("terminée") : st === 'current' ? T("en cours") : st === 'soon' ? T("bientôt") : detail]);
            const title = w.title.length > 20 ? `${w.title.slice(0, 19).trimEnd()}…` : w.title;
            return (
              <g key={w.slug} transform={`translate(${p.x} ${p.y})`} role="button" tabIndex={0} aria-label={label} className="cursor-pointer focus:outline-none [&:focus-visible>.km-focus]:opacity-100" onClick={() => go(w.slug)} onKeyDown={(e) => (e.key === 'Enter' || e.key === ' ') && (e.preventDefault(), go(w.slug))}>
                <title>{w.title}</title>
                <ellipse rx="96" ry="66" fill="transparent" />
                <ellipse className="km-focus" rx="100" ry="70" fill="none" stroke="#FFFFFF" strokeWidth="3" strokeDasharray="6 6" opacity={0} />
                {st === 'current' && !calm && (
                  <motion.ellipse rx="92" ry="60" cy="8" fill="none" stroke="#FFE08A" strokeWidth="3" animate={{ opacity: [0.9, 0.2, 0.9], scale: [1, 1.06, 1] }} transition={{ duration: 2.2, repeat: Infinity }} />
                )}
                {/* Sceau rouge (gardien ou numéro) */}
                <g transform="translate(46 -58)">
                  <circle r="21" fill="#FFFFFF" opacity={0.9} />
                  <circle r="18" fill={st === 'soon' ? '#9AA3AB' : '#8E1B26'} />
                  <circle r="18" fill="none" stroke="#FFFFFF" strokeWidth="1.5" opacity={0.5} />
                  <text textAnchor="middle" dy="0.36em" fontSize="18" fontWeight="900" className="jp" fill="#FFFFFF">{glyph}</text>
                  {st === 'done' && (
                    <g transform="translate(15 13)">
                      <circle r="9" fill="var(--ok)" stroke="#FFFFFF" strokeWidth="2" />
                      <path d="M-4 0 L-1 3 L4 -3" stroke="#FFFFFF" strokeWidth="2.2" fill="none" strokeLinecap="round" />
                    </g>
                  )}
                </g>
                {/* Plaque de bois avec le nom */}
                <g transform="translate(0 74)">
                  <rect x={-(title.length * 3.6 + 24)} y="-12" width={title.length * 7.2 + 48} height="24" rx="8" fill="#F6EBD3" stroke={WOOD} strokeWidth="2" />
                  <text textAnchor="middle" dy="0.35em" fontSize="12.5" fontWeight="700" fill="#3B2A1C">
                    <tspan fill={VERMILION}>{w.order} · </tspan>
                    {title}
                  </text>
                </g>
                {st === 'soon' && <text y="4" textAnchor="middle" fontSize="13" fontWeight="700" fill="#5A6670">{T("Bientôt")}</text>}
              </g>
            );
          })}

          <g pointerEvents="none">
            {!calm &&
              petals.map((p, i) => (
                <motion.ellipse key={i} rx="3.5" ry="5.5" fill={SAKURA} opacity={0.9} initial={{ cx: p.x, cy: -10 }} animate={{ cy: [-10, H + 10], cx: [p.x, p.x + (i % 2 ? 40 : -40)], rotate: [0, 200] }} transition={{ duration: p.d, repeat: Infinity, delay: p.delay, ease: 'linear' }} />
              ))}
          </g>

          {/* Bannière de la région */}
          <g transform="translate(24 24)" pointerEvents="none">
            <rect width={region.length * 10.5 + 60} height="44" rx="10" fill="#F6EBD3" stroke={WOOD} strokeWidth="2.5" />
            <circle cx="24" cy="22" r="11" fill="#8E1B26" />
            <text x="24" y="22" dy="0.36em" textAnchor="middle" fontSize="12" fontWeight="900" className="jp" fill="#FFFFFF">島</text>
            <text x="44" y="22" dy="0.35em" fontSize="20" className="font-display" fill="#3B2A1C">{region}</text>
          </g>

          {/* Personnage sur l'île en cours */}
          <motion.g initial={{ x: pts[Math.max(0, current - 1)].x - 62, y: pts[Math.max(0, current - 1)].y - 104 }} animate={{ x: pts[current].x - 62, y: pts[current].y - 104 }} transition={{ duration: 1.1, ease: 'easeInOut' }} pointerEvents="none">
            <motion.g animate={calm ? undefined : { y: [0, -5, 0] }} transition={{ duration: 1.6, repeat: Infinity, ease: 'easeInOut' }}>
              <ellipse cx="30" cy="80" rx="20" ry="5" fill="#000" opacity={0.2} />
              <foreignObject width="60" height="68">
                <div style={{ borderRadius: 14, overflow: 'hidden', border: '3px solid #FFFFFF', boxShadow: '0 4px 10px rgba(0,0,0,.25)', background: 'var(--surface)' }}>
                  <Avatar config={avatar} size={54} title={T("Toi")} />
                </div>
              </foreignObject>
            </motion.g>
          </motion.g>
        </svg>
      </div>
    </figure>
  );
}
