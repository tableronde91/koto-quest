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
};
