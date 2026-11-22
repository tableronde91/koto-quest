import type { ReactNode } from 'react';

/**
 * Mode histoire anglais (A1, l'Épée dans le bureau) : le décor de chaque île raconte son chapitre.
 * Londres et ses bureaux, cafés, lochs écossais, collines galloises. Dessins originaux, centrés sur (0, 0).
 */
const STONE = '#B9B2A4';
const STONE_DARK = '#8C8577';
const BRICK = '#A8553D';
const ROOF = '#3A3F46';
const WINDOW = '#F6E7B0';
const GREEN = '#2E6B4F';
const RED = '#C8323F';
const BLUE = '#1F3A5F';
const GOLD = '#E2B84A';

type P = { x: number; y: number; s?: number };
const at = ({ x, y, s = 1 }: P, flip = false) => `translate(${x} ${y}) scale(${flip ? -s : s} ${s})`;

/** Tour de l'horloge (Big Ben) : cadran doré, flèche. */
function ClockTower({ hands = '12', ...p }: P & { hands?: '12' | 'wild' }) {
  return (
    <g transform={at(p)}>
      <rect x="-6" y="-40" width="12" height="40" fill="#C9B27A" stroke="#9A8452" strokeWidth="1" />
      <rect x="-8" y="-48" width="16" height="10" fill="#D9C28A" stroke="#9A8452" strokeWidth="1" />
      <circle cx="0" cy="-43" r="5" fill="#FFF8E6" stroke={GOLD} strokeWidth="1.2" />
      {hands === '12' ? <path d="M0 -43 V-47 M0 -43 H3" stroke="#1F2433" strokeWidth="1" /> : <path d="M0 -43 L3 -46 M0 -43 L-2 -40" stroke="#1F2433" strokeWidth="1" />}
      <path d="M-8 -48 L0 -62 L8 -48Z" fill="#5A6A5A" />
      <path d="M0 -62 V-66" stroke={GOLD} strokeWidth="1" />
    </g>
  );
}

/** Immeuble de bureaux (Avalon & Co.) aux fenêtres éclairées. */
function Office({ ...p }: P) {
  return (
    <g transform={at(p)}>
      <rect x="-14" y="-30" width="28" height="30" fill={BRICK} />
      {[-24, -16, -8].map((y) => [-9, -1, 7].map((x) => <rect key={`${x}${y}`} x={x} y={y} width="4" height="5" fill={WINDOW} />))}
      <rect x="-3" y="-6" width="6" height="6" fill={BLUE} />
      <path d="M-16 -30 H16" stroke={ROOF} strokeWidth="2" />
    </g>
  );
}

/** Bus rouge à impériale. */
function Bus({ ...p }: P) {
  return (
    <g transform={at(p)}>
      <rect x="-12" y="-14" width="24" height="14" rx="2" fill={RED} />
      <path d="M-10 -11 H10 M-10 -5 H10" stroke={WINDOW} strokeWidth="2.4" />
      <circle cx="-7" cy="0" r="2.4" fill="#1F2433" /><circle cx="7" cy="0" r="2.4" fill="#1F2433" />
    </g>
  );
}

/** Cabine téléphonique rouge. */
function PhoneBox({ ...p }: P) {
  return (
    <g transform={at(p)}>
      <rect x="-4" y="-16" width="8" height="16" rx="1" fill={RED} />
      <rect x="-2.5" y="-12" width="5" height="8" fill={WINDOW} opacity={0.8} />
      <path d="M-4 -16 Q0 -20 4 -16" fill={RED} />
    </g>
  );
}

/** Cadre photo (portrait de famille). */
function Frame({ hue = '#E9C9A4', ...p }: P & { hue?: string }) {
  return (
    <g transform={at(p)}>
      <rect x="-7" y="-14" width="14" height="14" fill="#8A5A34" />
      <rect x="-5" y="-12" width="10" height="10" fill="#F6EBD3" />
      <circle cx="0" cy="-8" r="2.4" fill={hue} /><path d="M-3 -3 Q0 -6 3 -3" fill={hue} />
    </g>
  );
}

/** Petite flamme bleue (feu follet). */
function Wisp({ ...p }: P) {
  return (
    <g transform={at(p)}>
      <path d="M0 0 Q-6 -6 -2 -14 Q0 -10 2 -12 Q6 -6 0 0Z" fill="#7FB4E8" />
      <path d="M0 -2 Q-3 -5 -1 -9 Q1 -6 2 -7 Q3 -4 0 -2Z" fill="#DDEEFB" />
    </g>
  );
}

/** Tasse de thé fumante. */
function Teacup({ ...p }: P) {
  return (
    <g transform={at(p)}>
      <path d="M-8 -10 H8 V-4 Q8 2 0 2 Q-8 2 -8 -4Z" fill="#F6F3EC" stroke="#C9C2B4" strokeWidth="1" />
      <path d="M8 -8 q5 0 5 3 q0 3 -5 3" stroke="#C9C2B4" strokeWidth="1.4" fill="none" />
      <path d="M-3 -13 q2 -3 0 -6 M3 -13 q2 -3 0 -6" stroke="#FFFFFF" strokeWidth="1.2" fill="none" opacity={0.9} />
      <ellipse cx="0" cy="3" rx="11" ry="2" fill="#E9E1CF" />
    </g>
  );
}

/** Le château fort sur la colline. */
function Castle({ ...p }: P) {
  return (
    <g transform={at(p)}>
      <rect x="-16" y="-16" width="32" height="16" fill={STONE} />
      <rect x="-20" y="-24" width="9" height="24" fill={STONE_DARK} />
      <rect x="11" y="-24" width="9" height="24" fill={STONE_DARK} />
      {[-20, -16.5, -13.5, 11, 14.5, 17.5].map((x) => <rect key={x} x={x} y="-27" width="2.5" height="3" fill={STONE_DARK} />)}
      <path d="M-3 0 V-7 Q0 -10 3 -7 V0Z" fill="#4A3424" />
      <path d="M15.5 -24 V-34" stroke="#4A3424" strokeWidth="0.8" /><path d="M15.5 -34 L23 -31 L15.5 -28Z" fill={RED} />
    </g>
  );
}

/** Bosses de Nessie dans le loch. */
function Nessie({ ...p }: P) {
  return (
    <g transform={at(p)}>
      <path d="M-24 0 Q-18 -10 -12 0Z M-6 0 Q0 -12 6 0Z" fill="#3E8E6B" />
      <path d="M12 0 Q12 -18 20 -20 Q26 -20 26 -14 Q22 -16 20 -12 Q18 -6 20 0Z" fill="#3E8E6B" />
      <circle cx="22" cy="-17" r="0.9" fill="#1F2433" />
      <path d="M-28 1 H30" stroke="#A9D3F5" strokeWidth="1.4" opacity={0.8} />
    </g>
  );
}

/** Heaume du Chevalier vert et branche de houx. */
function Helm({ ...p }: P) {
  return (
    <g transform={at(p)}>
      <path d="M-9 0 V-12 Q-9 -22 0 -22 Q9 -22 9 -12 V0Z" fill="#5E8A4A" stroke="#2E5A2A" strokeWidth="1.2" />
      <path d="M-6 -10 H6" stroke="#1F2A1F" strokeWidth="2" />
      <path d="M0 -22 Q-2 -28 4 -30" stroke={RED} strokeWidth="2" fill="none" strokeLinecap="round" />
      <g transform="translate(14 -4)"><path d="M0 0 q4 -6 8 0 q-4 3 -8 0Z" fill={GREEN} /><circle cx="3" cy="-3" r="1.6" fill={RED} /><circle cx="5.5" cy="-2" r="1.6" fill={RED} /></g>
    </g>
  );
}

/** Drapeau gallois : dragon rouge sur blanc et vert. */
function WelshFlag({ ...p }: P) {
  return (
    <g transform={at(p)}>
      <path d="M0 0 V-30" stroke="#4A3424" strokeWidth="1.4" />
      <rect x="0" y="-30" width="20" height="7" fill="#FFFFFF" />
      <rect x="0" y="-23" width="20" height="7" fill="#3E8E3A" />
      <path d="M4 -22 Q8 -30 12 -24 Q16 -28 17 -22 Q12 -20 4 -22Z" fill={RED} />
    </g>
  );
}

/** L'épée dans le rocher. */
function SwordInStone({ glow = false, ...p }: P & { glow?: boolean }) {
  return (
    <g transform={at(p)}>
      {glow && <circle cx="0" cy="-16" r="16" fill="#FFF3B0" opacity={0.5} />}
      <path d="M-14 0 Q-12 -12 0 -12 Q12 -12 14 0Z" fill={STONE_DARK} />
      <path d="M0 -10 V-30" stroke="#C9D1DA" strokeWidth="2.4" />
      <path d="M-5 -28 H5" stroke={GOLD} strokeWidth="2" />
      <circle cx="0" cy="-33" r="1.8" fill={GOLD} />
    </g>
  );
}


/** Train à vapeur sur ses rails. */
function Train({ ...p }: P) {
  return (
    <g transform={at(p)}>
      <path d="M-26 0 H26" stroke="#4A3424" strokeWidth="1.5" />
      <rect x="-24" y="-12" width="16" height="10" rx="1" fill={GREEN} /><rect x="-6" y="-12" width="16" height="10" rx="1" fill={GREEN} />
      <rect x="12" y="-14" width="12" height="12" rx="2" fill="#1F2433" /><rect x="15" y="-20" width="4" height="7" fill="#1F2433" />
      {[-20, -12, -2, 6, 16, 22].map((x) => <circle key={x} cx={x} cy="-1" r="2" fill="#1F2433" />)}
      {[-21, -3].map((x) => <rect key={x} x={x} y="-10" width="10" height="4" fill={WINDOW} />)}
    </g>
  );
}

/** Étal de marché sous une toile rayée. */
function MarketStall({ ...p }: P) {
  return (
    <g transform={at(p)}>
      <path d="M-16 -18 H16 L14 -12 H-14Z" fill={RED} /><path d="M-8 -18 L-7 -12 M0 -18 V-12 M8 -18 L7 -12" stroke="#FFFFFF" strokeWidth="2" />
      <path d="M-14 -12 V0 M14 -12 V0" stroke="#6A4428" strokeWidth="1.4" />
      <rect x="-14" y="-6" width="28" height="4" fill="#A8794A" />
      {[-10, -4, 2, 8].map((x, i) => <circle key={x} cx={x} cy="-8" r="2" fill={['#E2709A', GOLD, '#7FB84E', '#E2483B'][i]} />)}
    </g>
  );
}

/** Tour de la fée, fenêtre éclairée. */
function Tower({ ...p }: P) {
  return (
    <g transform={at(p)}>
      <rect x="-7" y="-36" width="14" height="36" fill={STONE_DARK} />
      <path d="M-9 -36 L0 -52 L9 -36Z" fill="#5A3E7A" />
      <rect x="-2" y="-28" width="4" height="6" rx="2" fill="#E9C9FF" />
    </g>
  );
}

/** Arbre de forêt sombre. */
function Oak({ ...p }: P) {
  return (
    <g transform={at(p)}>
      <path d="M0 0 V-12" stroke="#5A3E28" strokeWidth="3" />
      <circle cx="0" cy="-18" r="10" fill="#3E6B3A" /><circle cx="-7" cy="-14" r="6" fill="#4E7F46" /><circle cx="7" cy="-14" r="6" fill="#2E5A2A" />
    </g>
  );
}

/** Champignons et cercle de fées. */
function FairyRing({ ...p }: P) {
  return (
    <g transform={at(p)}>
      {[-14, -6, 4, 12].map((x, i) => <g key={x} transform={`translate(${x} ${i % 2 ? 1 : -1})`}><rect x="-1" y="-4" width="2" height="4" fill="#F6F3EC" /><path d="M-4 -4 Q0 -10 4 -4Z" fill={i % 2 ? RED : '#E2709A'} /></g>)}
      <circle cx="-2" cy="-14" r="1.2" fill={GOLD} /><circle cx="6" cy="-18" r="1" fill={GOLD} />
    </g>
  );
}

/** Pont de pierre en arche. */
function Bridge({ ...p }: P) {
  return (
    <g transform={at(p)}>
      <path d="M-24 0 V-8 Q0 -22 24 -8 V0 H14 Q0 -12 -14 0Z" fill={STONE} stroke={STONE_DARK} strokeWidth="1" />
    </g>
  );
}

/** Table ronde et chaises. */
function RoundTable({ ...p }: P) {
  return (
    <g transform={at(p)}>
      <ellipse cx="0" cy="-6" rx="20" ry="7" fill="#8A5A34" stroke="#5A3A20" strokeWidth="1" />
      {[-18, -6, 6, 18].map((x) => <rect key={x} x={x - 2} y="-16" width="4" height="8" fill="#5A3A20" />)}
      <path d="M0 -6 V0" stroke="#5A3A20" strokeWidth="3" />
    </g>
  );
}

// ───── Décors B1 : côtes de Cornouailles ─────
function Lighthouse({ ...p }: P) {
  return (
    <g transform={at(p)}>
      <path d="M-6 0 L-4 -34 H4 L6 0Z" fill="#F4F1EA" stroke={STONE_DARK} strokeWidth="1" />
      <path d="M-5.5 -10 H5.5 M-5 -22 H5" stroke={RED} strokeWidth="4" />
      <rect x="-5" y="-40" width="10" height="6" fill={GOLD} />
      <path d="M-6 -40 L0 -46 L6 -40Z" fill={RED} />
    </g>
  );
}
function Waves({ ...p }: P) {
  return (
    <g transform={at(p)}>
      <path d="M-30 0 Q-22 -6 -15 0 T0 0 T15 0 T30 0" stroke="#5E9FC4" strokeWidth="2.5" fill="none" strokeLinecap="round" />
      <path d="M-24 6 Q-16 0 -9 6 T6 6 T21 6" stroke="#7FC4D9" strokeWidth="2" fill="none" strokeLinecap="round" />
    </g>
  );
}
function Mill({ ...p }: P) {
  return (
    <g transform={at(p)}>
      <path d="M-9 0 L-6 -24 H6 L9 0Z" fill={BRICK} />
      <path d="M-7 -24 L0 -32 L7 -24Z" fill={ROOF} />
      <g transform="translate(0 -24)">{[0, 90].map((a) => <path key={a} d="M-18 0 H18" stroke="#6A4428" strokeWidth="3" transform={`rotate(${a + 20})`} />)}</g>
    </g>
  );
}
function Grail({ ...p }: P) {
  return (
    <g transform={at(p)}>
      <circle cx="0" cy="-14" r="12" fill={GOLD} opacity={0.25} />
      <path d="M-7 -20 H7 Q7 -10 0 -8 Q-7 -10 -7 -20Z" fill={GOLD} stroke="#A57E22" strokeWidth="1" />
      <path d="M0 -8 V-2 M-5 0 H5" stroke="#A57E22" strokeWidth="2" />
    </g>
  );
}
function Mist({ ...p }: P) {
  return (
    <g transform={at(p)} opacity={0.75}>
      <ellipse cx="-12" cy="0" rx="16" ry="5" fill="#E4E8EC" />
      <ellipse cx="10" cy="-4" rx="18" ry="6" fill="#D8DEE4" />
    </g>
  );
}

export const ENGLISH_SCENES: Record<string, (calm: boolean) => ReactNode> = {
  // Le badge disparu : la tour de l'horloge et l'immeuble d'Avalon & Co.
  'a1-w1': () => (
    <>
      <ClockTower x={-22} y={12} />
      <Office x={12} y={14} />
      <PhoneBox x={34} y={14} />
    </>
  ),
  // Les portraits échangés : cadres de famille posés de travers.
  'a1-w2': () => (
    <>
      <Office x={-14} y={12} />
      <Frame x={14} y={12} />
      <Frame x={28} y={6} hue="#C99A74" />
      <Frame x={-36} y={12} hue="#F2D6B8" />
    </>
  ),
  // La flamme des couloirs : bureaux et feux follets.
  'a1-w3': () => (
    <>
      <Office x={0} y={14} />
      <Wisp x={-26} y={0} />
      <Wisp x={26} y={-6} />
    </>
  ),
  // Les horloges déréglées : tour de l'horloge aux aiguilles folles.
  'a1-w4': () => (
    <>
      <ClockTower x={0} y={14} hands="wild" />
      <Bus x={-26} y={14} />
    </>
  ),
  // Le géant affamé : le café du coin et une tasse de thé géante.
  'a1-w5': () => (
    <>
      <Office x={-16} y={12} />
      <Teacup x={18} y={10} s={1.3} />
    </>
  ),
  // Le loch des voyageurs perdus : Nessie et un château écossais.
  'a1-w6': () => (
    <>
      <Castle x={-20} y={6} s={0.8} />
      <Nessie x={8} y={16} />
    </>
  ),
  // Le défi du chevalier : heaume vert et houx d'hiver.
  'a1-w7': () => (
    <>
      <Castle x={18} y={8} s={0.8} />
      <Helm x={-18} y={14} />
    </>
  ),
  // Sous la colline du dragon : château gallois et drapeau au dragon.
  'a1-w8': () => (
    <>
      <Castle x={-8} y={10} />
      <WelshFlag x={24} y={14} />
    </>
  ),
  // L'épée dans le rocher.
  'a1-final': () => <SwordInStone x={0} y={14} s={1.3} glow />,
  // ───── A2 : terres de Logres ─────
  'a2-w1': () => (<><Train x={0} y={14} /><Castle x={-30} y={4} s={0.6} /></>),
  'a2-w2': () => (<><MarketStall x={-14} y={14} /><MarketStall x={16} y={12} s={0.8} /></>),
  'a2-w3': () => (<><Tower x={0} y={14} /><Wisp x={18} y={-14} /></>),
  'a2-w4': () => (<><Oak x={-20} y={14} /><Oak x={4} y={12} s={1.2} /><Oak x={24} y={14} s={0.9} /></>),
  'a2-w5': () => (<><Bridge x={0} y={14} /><Castle x={-26} y={4} s={0.6} /></>),
  'a2-w6': () => (<><Oak x={-14} y={14} s={1.3} /><Oak x={14} y={12} /></>),
  'a2-w7': () => (<><FairyRing x={0} y={14} /><Wisp x={-18} y={-4} /><Wisp x={20} y={-8} /></>),
  'a2-w8': () => (<><Bridge x={0} y={14} /><Helm x={-24} y={8} s={0.8} /></>),
  'a2-final': () => (<><RoundTable x={0} y={14} s={1.2} /><Castle x={0} y={-6} s={0.7} /></>),
  // ───── B1 : côtes de Cornouailles ─────
  'b1-w1': () => (<><Waves x={0} y={16} /><Office x={-22} y={10} s={0.7} /></>),
  'b1-w2': () => (<><Oak x={-18} y={14} s={0.9} /><Castle x={16} y={8} s={0.6} /></>),
  'b1-w3': () => (<><Office x={0} y={14} /><Waves x={-24} y={18} s={0.6} /></>),
  'b1-w4': () => (<><Mill x={0} y={14} /><Oak x={26} y={14} s={0.7} /></>),
  'b1-w5': () => (<><Oak x={-20} y={14} /><Wisp x={14} y={-10} /></>),
  'b1-w6': () => (<><Tower x={0} y={14} /><Wisp x={-18} y={-12} /></>),
  'b1-w7': () => (<><Tower x={-10} y={14} /><Castle x={18} y={10} s={0.6} /></>),
  'b1-w8': () => (<><Mist x={0} y={6} /><Castle x={0} y={14} s={0.6} /><Mist x={-10} y={14} /></>),
  'b1-final': () => (<><Lighthouse x={-24} y={14} /><Grail x={8} y={6} s={1.3} /><Waves x={0} y={18} /></>),
  // ───── B2 : Marches galloises ─────
  'b2-w1': () => (<><Mist x={-6} y={10} /><Waves x={10} y={18} /><Oak x={-26} y={14} s={0.7} /></>),
  'b2-w2': () => (<><ClockTower x={-16} y={12} /><Office x={14} y={14} /></>),
  'b2-w3': () => (<><Waves x={0} y={16} /><Oak x={-22} y={12} s={0.8} /><Oak x={22} y={14} s={0.7} /></>),
  'b2-w4': () => (<><Office x={-8} y={14} /><Teacup x={20} y={14} /></>),
  'b2-w5': () => (<><Waves x={0} y={18} /><Lighthouse x={22} y={14} s={0.8} /></>),
  'b2-w6': () => (<><Bridge x={0} y={14} /><Mist x={-14} y={8} /></>),
  'b2-w7': () => (<><Castle x={0} y={14} s={0.8} /><Wisp x={-20} y={-14} /><Wisp x={20} y={-10} /></>),
  'b2-w8': () => (<><Helm x={-14} y={10} /><Oak x={14} y={14} s={1.1} /></>),
  'b2-final': () => (<><Castle x={0} y={14} s={0.9} /><Oak x={-28} y={14} s={0.8} /><Oak x={28} y={14} s={0.8} /></>),
  // ───── C1 : îles du Nord ─────
  'c1-w1': () => (<><Waves x={0} y={18} /><Mist x={-10} y={6} /><Lighthouse x={24} y={14} s={0.7} /></>),
  'c1-w2': () => (<><Waves x={-6} y={14} /><Waves x={8} y={20} s={0.8} /></>),
  'c1-w3': () => (<><Waves x={-14} y={18} s={0.7} /><Oak x={14} y={14} s={0.8} /></>),
  'c1-w4': () => (<><Tower x={-10} y={14} /><Mist x={14} y={4} /></>),
  'c1-w5': () => (<><Castle x={-14} y={14} s={0.7} /><Mist x={12} y={2} /></>),
  'c1-w6': () => (<><Waves x={0} y={18} /><Lighthouse x={-22} y={14} s={0.8} /></>),
  'c1-w7': () => (<><Mill x={-6} y={14} /><Teacup x={20} y={14} /></>),
  'c1-w8': () => (<><Waves x={0} y={18} /><SwordInStone x={0} y={10} /></>),
  'c1-final': () => (<><Mist x={0} y={6} /><Castle x={0} y={14} s={0.8} /><Waves x={0} y={20} /></>),
};
