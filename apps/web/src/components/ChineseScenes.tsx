import type { ReactNode } from 'react';

/**
 * Mode histoire chinois (HSK 1, le messager des Royaumes) : le décor de chaque île raconte son chapitre.
 * Royaumes combattants : écoles, bronzes, palais, marchés, remparts. Dessins originaux, centrés sur (0, 0).
 */
const LACQUER = '#8E1B26';
const RED = '#C8323F';
const GOLD = '#E2B84A';
const JADE = '#2F7A6E';
const BRONZE = '#4E8A78';
const WOOD = '#7A4A2A';
const PAPER = '#FFF3DC';
const ROOF = '#3A3F46';
const STONE = '#B9AE98';

type P = { x: number; y: number; s?: number };
const at = ({ x, y, s = 1 }: P) => `translate(${x} ${y}) scale(${s})`;

/** Pavillon à toit relevé (école, palais). */
function Pavilion({ fill = LACQUER, ...p }: P & { fill?: string }) {
  return (
    <g transform={at(p)}>
      <rect x="-12" y="-14" width="24" height="14" fill={fill} />
      <rect x="-3" y="-9" width="6" height="9" fill={WOOD} />
      <path d="M-18 -14 Q-12 -16 -10 -22 H10 Q12 -16 18 -14 Q20 -18 22 -16 L16 -12 H-16 L-22 -16 Q-20 -18 -18 -14Z" fill={ROOF} />
      <path d="M-14 -0.5 H14" stroke={STONE} strokeWidth="2" />
    </g>
  );
}

/** Tour à étages. */
function Tower({ ...p }: P) {
  return (
    <g transform={at(p)}>
      {[0, 1, 2].map((i) => (
        <g key={i} transform={`translate(0 ${-i * 12}) scale(${1 - i * 0.18})`}>
          <rect x="-8" y="-10" width="16" height="10" fill={RED} />
          <path d="M-13 -10 L-9 -14 H9 L13 -10Z" fill={ROOF} />
        </g>
      ))}
      <path d="M0 -38 V-44" stroke={GOLD} strokeWidth="1.5" />
    </g>
  );
}

/** Chaudron de bronze tripode (ding), décor de taotie. */
function Ding({ ...p }: P) {
  return (
    <g transform={at(p)}>
      <path d="M-11 -14 H11 Q11 -2 0 -2 Q-11 -2 -11 -14Z" fill={BRONZE} stroke="#2E5A4E" strokeWidth="1" />
      <path d="M-9 -14 v-5 h3 v5 M6 -14 v-5 h3 v5" stroke={BRONZE} strokeWidth="2" fill="none" />
      <path d="M-7 -2 L-9 4 M0 -2 V4 M7 -2 L9 4" stroke="#2E5A4E" strokeWidth="2" />
      <path d="M-5 -9 q2.5 -3 5 0 q2.5 3 5 0" stroke={GOLD} strokeWidth="1.2" fill="none" />
    </g>
  );
}

/** Lanterne rouge suspendue. */
function Lantern({ ...p }: P) {
  return (
    <g transform={at(p)}>
      <path d="M0 -20 V-14" stroke={WOOD} strokeWidth="1" />
      <ellipse cx="0" cy="-8" rx="6" ry="7" fill={RED} />
      <path d="M-3 -14 V-2 M3 -14 V-2" stroke={GOLD} strokeWidth="0.8" />
      <path d="M0 -1 V4" stroke={GOLD} strokeWidth="1.4" />
    </g>
  );
}

/** Pétards du Nouvel An. */
function Firecrackers({ ...p }: P) {
  return (
    <g transform={at(p)}>
      <path d="M0 -26 V-2" stroke={WOOD} strokeWidth="1" />
      {[-22, -16, -10, -4].map((y, i) => <rect key={y} x={i % 2 ? 0 : -5} y={y} width="5" height="5" rx="1" fill={RED} stroke={GOLD} strokeWidth="0.6" />)}
    </g>
  );
}

/** Rouleau de bambou (lettre du messager). */
function Scroll({ ...p }: P) {
  return (
    <g transform={at(p)}>
      <rect x="-10" y="-10" width="20" height="10" fill="#D9C28A" stroke="#9A8452" strokeWidth="1" />
      {[-6, -2, 2, 6].map((x) => <path key={x} d={`M${x} -10 V0`} stroke="#9A8452" strokeWidth="0.6" />)}
      <path d="M-10 -5 H10" stroke={RED} strokeWidth="1.4" />
      <circle cx="0" cy="-5" r="2.2" fill={RED} />
    </g>
  );
}

/** Étal de marché sous auvent. */
function Stall({ ...p }: P) {
  return (
    <g transform={at(p)}>
      <path d="M-14 -18 H14 L10 -12 H-10Z" fill={GOLD} stroke={WOOD} strokeWidth="1" />
      <path d="M-10 -12 V0 M10 -12 V0" stroke={WOOD} strokeWidth="1.6" />
      <rect x="-11" y="-5" width="22" height="5" fill={WOOD} />
      {[-6, 0, 6].map((x) => <circle key={x} cx={x} cy="-7" r="2.2" fill={x ? '#E25A6A' : '#8FA65A'} />)}
    </g>
  );
}

/** Clepsydre (horloge à eau) en bronze. */
function Clepsydra({ ...p }: P) {
  return (
    <g transform={at(p)}>
      <rect x="-6" y="-22" width="12" height="8" fill={BRONZE} />
      <rect x="-8" y="-12" width="16" height="12" fill={BRONZE} />
      <path d="M0 -14 V-12" stroke="#7FC4D9" strokeWidth="1.6" />
      <path d="M-5 -6 H5" stroke={GOLD} strokeWidth="1" />
    </g>
  );
}

/** Char à deux roues. */
function Chariot({ ...p }: P) {
  return (
    <g transform={at(p)}>
      <rect x="-8" y="-12" width="16" height="7" fill={WOOD} />
      <path d="M8 -8 H18" stroke={WOOD} strokeWidth="1.6" />
      <circle cx="0" cy="-4" r="5" fill="none" stroke={ROOF} strokeWidth="1.6" />
      <path d="M-5 -4 H5 M0 -9 V1" stroke={ROOF} strokeWidth="0.8" />
      <path d="M-4 -12 V-20 L4 -17 L-4 -14" fill={RED} stroke={WOOD} strokeWidth="0.8" />
    </g>
  );
}

/** Rempart crénelé avec porte. */
function Wall({ ...p }: P) {
  return (
    <g transform={at(p)}>
      <path d="M-26 0 V-14 h4 v-3 h4 v3 h4 v-3 h4 v3 h4 v-3 h4 v3 h4 v-3 h4 v3 h4 v-3 h4 v3 h4 v-3 h4 v3 V0Z" fill={STONE} stroke="#8C8577" strokeWidth="0.8" />
      <path d="M-5 0 V-8 Q0 -12 5 -8 V0Z" fill={WOOD} />
      <path d="M-10 -17 L-4 -24 H4 L10 -17Z" fill={ROOF} />
      <rect x="-7" y="-17" width="14" height="3" fill={LACQUER} />
    </g>
  );
}

/** Branche de prunier en fleur. */
function Plum({ ...p }: P) {
  return (
    <g transform={at(p)}>
      <path d="M0 0 Q-2 -12 6 -20 M-1 -8 Q-8 -12 -10 -18" stroke={WOOD} strokeWidth="1.6" fill="none" />
      {[[6, -20], [-10, -18], [2, -13], [-5, -11], [8, -15]].map(([x, y]) => <circle key={`${x}${y}`} cx={x} cy={y} r="2.4" fill="#F4B6C2" stroke="#E25A6A" strokeWidth="0.6" />)}
    </g>
  );
}

/** Nuage de bon augure. */
function LuckyCloud({ ...p }: P) {
  return (
    <g transform={at(p)}>
      <path d="M-12 0 q0 -6 6 -6 q2 -6 8 -4 q6 -4 8 2 q6 0 4 8Z" fill={PAPER} stroke={GOLD} strokeWidth="1" />
      <path d="M-4 -2 q3 -3 6 0" stroke={GOLD} strokeWidth="0.8" fill="none" />
    </g>
  );
}


/** Tente de campagne et fanion. */
function Tent({ ...p }: P) {
  return (
    <g transform={at(p)}>
      <path d="M-14 0 L0 -18 L14 0Z" fill="#D9C28A" stroke={WOOD} strokeWidth="1" />
      <path d="M0 -18 L-4 0 H4Z" fill={WOOD} />
      <path d="M0 -18 V-28 L8 -25 L0 -22" fill={RED} stroke={WOOD} strokeWidth="0.8" />
    </g>
  );
}

/** Tambour de guerre. */
function Drum({ ...p }: P) {
  return (
    <g transform={at(p)}>
      <path d="M-8 -2 L-10 4 M8 -2 L10 4" stroke={WOOD} strokeWidth="1.6" />
      <ellipse cx="0" cy="-10" rx="10" ry="9" fill={RED} stroke={GOLD} strokeWidth="1" />
      <ellipse cx="0" cy="-10" rx="5" ry="7" fill={PAPER} />
    </g>
  );
}

/** Jonque sur le fleuve. */
function Junk({ ...p }: P) {
  return (
    <g transform={at(p)}>
      <path d="M-16 -4 H16 L12 2 H-12Z" fill={WOOD} />
      <path d="M-2 -4 V-26 M8 -4 V-20" stroke={WOOD} strokeWidth="1.2" />
      <path d="M-2 -24 Q-12 -14 -2 -6Z M8 -18 Q2 -12 8 -6Z" fill="#E9CF9A" stroke="#9A8452" strokeWidth="0.6" />
    </g>
  );
}

/** Pin sur un rocher (les monts de Zhuangzi). */
function Pine({ ...p }: P) {
  return (
    <g transform={at(p)}>
      <path d="M-10 0 Q-8 -6 0 -5 Q8 -7 10 0Z" fill={STONE} />
      <path d="M0 -4 Q-2 -14 2 -26" stroke={WOOD} strokeWidth="2" fill="none" />
      <path d="M-12 -14 Q0 -22 12 -15 Q2 -12 -12 -14Z M-8 -22 Q2 -29 10 -23 Q2 -20 -8 -22Z" fill={JADE} />
    </g>
  );
}

/** Touffe de bambous (l'école des lettrés). */
function Bamboo({ ...p }: P) {
  return (
    <g transform={at(p)}>
      {[-6, 0, 6].map((x, i) => <path key={x} d={`M${x} 0 V${-22 - i * 4}`} stroke="#5E8C3A" strokeWidth="2" strokeDasharray="6 1" />)}
      <path d="M0 -18 q6 -2 10 -6 M-6 -14 q-6 -1 -9 -5 M6 -24 q5 0 8 -3" stroke="#5E8C3A" strokeWidth="1.6" fill="none" strokeLinecap="round" />
    </g>
  );
}

/** Carillon de cloches de bronze (le débat de l'académie). */
function Bells({ ...p }: P) {
  return (
    <g transform={at(p)}>
      <path d="M-14 0 V-24 M14 0 V-24 M-16 -24 H16" stroke={WOOD} strokeWidth="1.6" />
      {[-8, 0, 8].map((x, i) => <path key={x} d={`M${x - 3 + i * 0.3} -22 V${-16 + i} Q${x} ${-13 + i} ${x + 3 - i * 0.3} ${-16 + i} V-22Z`} fill={BRONZE} stroke={GOLD} strokeWidth="0.6" />)}
    </g>
  );
}

export const CHINESE_SCENES: Record<string, (calm: boolean) => ReactNode> = {
  // L'école du maître : pavillon de Lu, pétards contre le Nian, prunier.
  'hsk1-w1': () => (<><Pavilion x={-14} y={12} /><Firecrackers x={14} y={8} /><Plum x={30} y={12} /></>),
  // Le calendrier avalé : chaudron de bronze et rouleaux.
  'hsk1-w2': () => (<><Ding x={-16} y={12} /><Scroll x={10} y={10} /><Lantern x={28} y={6} /></>),
  // La cour de Chu : palais laqué et lanternes.
  'hsk1-w3': () => (<><Pavilion x={-6} y={12} s={1.1} /><Lantern x={-28} y={4} /><Lantern x={20} y={2} /></>),
  // La maison du général de Yan : pavillon, char de guerre.
  'hsk1-w4': () => (<><Pavilion x={-16} y={12} fill={JADE} /><Chariot x={14} y={12} /></>),
  // Le marché de Xinzheng : étals.
  'hsk1-w5': () => (<><Stall x={-18} y={12} /><Stall x={10} y={14} s={0.9} /><Lantern x={30} y={4} /></>),
  // Le palais de Wei : clepsydres et tour.
  'hsk1-w6': () => (<><Tower x={-16} y={14} /><Clepsydra x={8} y={12} /><Clepsydra x={24} y={12} s={0.8} /></>),
  // Les routes de Handan : char et nuages.
  'hsk1-w7': () => (<><Chariot x={-12} y={12} /><LuckyCloud x={16} y={-4} /><Plum x={26} y={12} /></>),
  // Les portes de Xianyang : rempart de Qin.
  'hsk1-w8': () => (<><Wall x={0} y={12} /><Lantern x={-30} y={2} /><Lantern x={30} y={2} /></>),
  // La cour de Luoyang : tour, rouleau, nuages de bon augure.
  'hsk1-final': () => (<><Tower x={-12} y={14} s={1.1} /><Scroll x={14} y={10} /><LuckyCloud x={24} y={-10} /></>),
  // HSK 2 — l'art de la guerre au royaume de Wu
  'hsk2-w1': () => (<><Tent x={-16} y={12} /><Tent x={6} y={14} s={0.8} /><Drum x={26} y={12} /></>),
  'hsk2-w2': () => (<><Tent x={-14} y={12} /><Ding x={12} y={12} s={0.8} /><Lantern x={28} y={4} /></>),
  'hsk2-w3': () => (<><Drum x={-14} y={12} /><Chariot x={14} y={12} /></>),
  'hsk2-w4': () => (<><Junk x={-4} y={10} /><LuckyCloud x={22} y={-8} /></>),
  'hsk2-w5': () => (<><Chariot x={-14} y={12} /><Wall x={16} y={12} s={0.6} /></>),
  'hsk2-w6': () => (<><Stall x={-16} y={12} /><Stall x={12} y={14} s={0.9} /></>),
  'hsk2-w7': () => (<><Tent x={-16} y={12} /><Drum x={4} y={12} /><Tent x={22} y={14} s={0.8} /></>),
  'hsk2-w8': () => (<><Pavilion x={-8} y={12} s={1.1} /><Scroll x={20} y={10} /></>),
  'hsk2-final': () => (<><Tower x={-12} y={14} s={1.1} /><Junk x={16} y={12} s={0.8} /></>),
  // HSK 3 — les Cent Écoles au royaume de Qi
  'hsk3-w1': () => (<><Pavilion x={-12} y={12} fill={WOOD} /><Lantern x={14} y={4} /><Lantern x={26} y={6} s={0.8} /></>),
  'hsk3-w2': () => (<><Stall x={-16} y={12} /><Stall x={8} y={14} s={0.9} /><Junk x={28} y={10} s={0.6} /></>),
  'hsk3-w3': () => (<><Pavilion x={-10} y={12} /><Scroll x={14} y={10} /><Bamboo x={28} y={12} /></>),
  'hsk3-w4': () => (<><Pine x={-14} y={12} /><Pine x={10} y={14} s={0.8} /><LuckyCloud x={24} y={-10} /></>),
  'hsk3-w5': () => (<><Tower x={-12} y={14} /><Drum x={12} y={12} /><Ding x={28} y={12} s={0.7} /></>),
  'hsk3-w6': () => (<><Chariot x={-14} y={12} /><Junk x={12} y={10} /><Wall x={30} y={12} s={0.5} /></>),
  'hsk3-w7': () => (<><Pavilion x={-12} y={12} fill={JADE} /><Ding x={12} y={12} s={0.8} /><Pine x={28} y={12} s={0.7} /></>),
  'hsk3-w8': () => (<><Pavilion x={-10} y={12} s={1.1} /><Bells x={18} y={12} /></>),
  'hsk3-final': () => (<><Tower x={-12} y={14} s={1.1} /><Bells x={14} y={12} s={0.9} /><LuckyCloud x={26} y={-10} /></>),
  // HSK 4 — l'empire unifié de Qin
  'hsk4-w1': () => (<><Pavilion x={-12} y={12} fill={ROOF} /><Scroll x={12} y={10} /><Scroll x={26} y={12} s={0.8} /></>),
  'hsk4-w2': () => (<><Stall x={-16} y={12} /><Ding x={8} y={12} s={0.8} /><Stall x={26} y={14} s={0.8} /></>),
  'hsk4-w3': () => (<><Chariot x={-14} y={12} /><Wall x={14} y={12} s={0.7} /></>),
  'hsk4-w4': () => (<><Pavilion x={-12} y={12} /><Ding x={12} y={12} /><Lantern x={28} y={4} /></>),
  'hsk4-w5': () => (<><Tower x={-12} y={14} /><Pavilion x={14} y={12} s={0.9} /></>),
  'hsk4-w6': () => (<><Ding x={-14} y={12} /><Bells x={8} y={12} s={0.9} /><Ding x={28} y={12} s={0.7} /></>),
  'hsk4-w7': () => (<><Pine x={-14} y={12} /><Tent x={8} y={12} /><Drum x={26} y={12} s={0.8} /></>),
  'hsk4-w8': () => (<><Tower x={-10} y={14} s={1.1} /><Scroll x={18} y={10} /></>),
  'hsk4-final': () => (<><Wall x={-8} y={12} /><Tower x={18} y={14} s={0.9} /><LuckyCloud x={28} y={-12} /></>),
  // HSK 5 — l'expédition de Xu Fu vers les mers de l'Est
  'hsk5-w1': () => (<><Junk x={-12} y={10} /><Junk x={12} y={12} s={0.8} /><Stall x={30} y={14} s={0.7} /></>),
  'hsk5-w2': () => (<><Pavilion x={-10} y={10} s={0.9} fill={STONE} /><LuckyCloud x={14} y={-6} /><Junk x={26} y={12} s={0.7} /></>),
  'hsk5-w3': () => (<><Tent x={-14} y={12} /><Scroll x={8} y={10} /><Bamboo x={26} y={12} /></>),
  'hsk5-w4': () => (<><Pine x={-14} y={12} /><Pine x={6} y={14} s={0.7} /><Junk x={24} y={12} s={0.7} /></>),
  'hsk5-w5': () => (<><Tower x={-12} y={14} s={0.9} /><LuckyCloud x={10} y={-10} /><Drum x={26} y={12} s={0.8} /></>),
  'hsk5-w6': () => (<><Ding x={-14} y={12} /><Plum x={6} y={12} /><Pavilion x={24} y={12} s={0.7} fill={JADE} /></>),
  'hsk5-w7': () => (<><Stall x={-14} y={12} /><Junk x={10} y={10} s={0.8} /><Lantern x={28} y={4} /></>),
  'hsk5-w8': () => (<><Pavilion x={-10} y={12} s={1.1} fill={GOLD} /><LuckyCloud x={18} y={-8} /><Plum x={28} y={12} /></>),
  'hsk5-final': () => (<><Tower x={-12} y={14} s={1.1} /><Pavilion x={14} y={12} fill={GOLD} /><LuckyCloud x={26} y={-12} /></>),
};
