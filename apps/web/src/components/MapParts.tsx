import { motion } from 'motion/react';

/** Éléments de décor de la carte qui ne dépendent pas de la saison : bâtiments, portes, lanternes. */
export const SAKURA = '#F4A9C0';
export const SAKURA_DARK = '#E07A9B';
export const LEAF = '#4E8B4A';
export const LEAF_DARK = '#356B3A';
export const WOOD = '#7A4E2D';
export const VERMILION = '#C8323F';
export const SAND = '#EBD9AE';
export const ROCK = '#7D7468';
export const ROCK_DARK = '#5A5249';

export function Hut({ x, y, s = 1 }: { x: number; y: number; s?: number }) {
  return (
    <g transform={`translate(${x} ${y}) scale(${s})`}>
      <rect x="-10" y="-8" width="20" height="12" fill="#B8865A" />
      <path d="M-15 -7 L0 -20 L15 -7Z" fill="#8C6A3F" />
      <rect x="-3" y="-3" width="6" height="7" fill="#3B2A1C" />
      <rect x="4" y="-5" width="4" height="3" fill="#FFD27A" />
    </g>
  );
}

export function Torii({ x, y, s = 1 }: { x: number; y: number; s?: number }) {
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

export function Pagoda({ x, y, s = 1 }: { x: number; y: number; s?: number }) {
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

export function Bamboo({ x, y, s = 1 }: { x: number; y: number; s?: number }) {
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

export function Lanterns({ x, y, s = 1, calm }: { x: number; y: number; s?: number; calm: boolean }) {
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

/** Château à donjon (mode histoire : le château du seigneur). */
export function Castle({ x, y, s = 1, fill, lit = false }: { x: number; y: number; s?: number; fill?: string; lit?: boolean }) {
  const wall = fill ?? '#F2ECDD';
  const roof = fill ?? '#2F3B4A';
  return (
    <g transform={`translate(${x} ${y}) scale(${s})`}>
      <path d="M-24 0 L-19 -12 H19 L24 0Z" fill={fill ?? '#8A8177'} />
      {[0, 1, 2].map((i) => (
        <g key={i} transform={`translate(0 ${-12 - i * 12})`}>
          <rect x={-14 + i * 3} y="-9" width={28 - i * 6} height="9" fill={wall} />
          <path d={`M${-21 + i * 3} -8 Q0 -15 ${21 - i * 3} -8 L${15 - i * 3} -13 H${-15 + i * 3}Z`} fill={roof} />
          {lit && !fill && [-1, 1].map((k) => <rect key={k} x={k * (7 - i * 1.5) - 1.5} y="-6" width="3" height="4" fill="#FFD27A" />)}
        </g>
      ))}
      <path d="M-5 -45 Q0 -54 5 -45Z" fill={roof} />
      {!fill && <path d="M-3 -52 L0 -57 L3 -52" stroke="#C9A24A" strokeWidth="1.6" fill="none" strokeLinecap="round" />}
    </g>
  );
}

/** Porte de l'aube (mode histoire N3) : grand torii devant le soleil levant. */
export function DawnGate({ x, y, s = 1 }: { x: number; y: number; s?: number }) {
  return (
    <g transform={`translate(${x} ${y}) scale(${s})`}>
      <circle cy="-16" r="24" fill="#FFD58A" opacity={0.35} filter="url(#km-soft)" />
      <circle cy="-14" r="13" fill="#FFC56B" />
      <Torii x={0} y={2} s={1.5} />
    </g>
  );
}
