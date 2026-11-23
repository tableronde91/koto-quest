import type { ReactNode } from 'react';

/**
 * Mode histoire espagnol (DELE A1, l'écuyer·ère de Don Quichotte) : le décor de chaque île raconte son chapitre.
 * La Manche : moulins à vent, maisons blanches, venta, oliviers, sierra et château des Ducs. Dessins originaux, centrés sur (0, 0).
 */
const WHITE = '#F6F1E6';
const OCHRE = '#C8923A';
const TERRACOTTA = '#B8562E';
const ROOF = '#9A3E22';
const OLIVE = '#6E7A3A';
const STONE = '#B9AE98';
const WOOD = '#7A4A2A';
const RED = '#C8323F';
const GOLD = '#E2B84A';
const SKY = '#9CC4E4';

type P = { x: number; y: number; s?: number };
const at = ({ x, y, s = 1 }: P) => `translate(${x} ${y}) scale(${s})`;

/** Moulin à vent de la Manche : tour blanche, toit conique, quatre ailes. */
function Windmill({ spin = false, ...p }: P & { spin?: boolean }) {
  return (
    <g transform={at(p)}>
      <path d="M-7 0 L-5 -24 H5 L7 0Z" fill={WHITE} stroke={STONE} strokeWidth="0.8" />
      <path d="M-6 -24 L0 -32 L6 -24Z" fill="#3A3F46" />
      <rect x="-1.5" y="-8" width="3" height="5" fill={WOOD} />
      <g transform={`rotate(${spin ? 30 : 0} 0 -26)`} stroke={WOOD} strokeWidth="1.2">
        {[0, 90, 180, 270].map((a) => (
          <g key={a} transform={`rotate(${a} 0 -26)`}>
            <path d="M0 -26 V-44" />
            <rect x="0.5" y="-43" width="4" height="15" fill="#E9DCC0" strokeWidth="0.5" />
          </g>
        ))}
      </g>
    </g>
  );
}

/** Maison blanche aux tuiles rouges. */
function WhiteHouse({ ...p }: P) {
  return (
    <g transform={at(p)}>
      <rect x="-12" y="-14" width="24" height="14" fill={WHITE} stroke={STONE} strokeWidth="0.6" />
      <path d="M-14 -14 L0 -22 L14 -14Z" fill={ROOF} />
      <rect x="-3" y="-8" width="6" height="8" fill={WOOD} />
      <rect x="-9" y="-11" width="4" height="4" fill="#3A6AA8" />
      <rect x="5" y="-11" width="4" height="4" fill="#3A6AA8" />
    </g>
  );
}

/** Église du village : clocher et cloche. */
function Church({ ...p }: P) {
  return (
    <g transform={at(p)}>
      <rect x="-10" y="-16" width="20" height="16" fill={OCHRE} />
      <rect x="4" y="-32" width="8" height="18" fill={OCHRE} />
      <path d="M3 -32 L8 -40 L13 -32Z" fill={ROOF} />
      <circle cx="8" cy="-26" r="2" fill={GOLD} />
      <path d="M-4 0 V-7 Q0 -11 4 -7 V0Z" fill={WOOD} />
    </g>
  );
}

/** Olivier noueux. */
function OliveTree({ ...p }: P) {
  return (
    <g transform={at(p)}>
      <path d="M0 0 Q-2 -6 1 -12" stroke={WOOD} strokeWidth="2.4" fill="none" />
      <ellipse cx="0" cy="-16" rx="11" ry="7" fill={OLIVE} />
      <ellipse cx="-6" cy="-19" rx="6" ry="4" fill="#7E8A4A" />
      <ellipse cx="6" cy="-20" rx="6" ry="4" fill="#5E6A2E" />
    </g>
  );
}

/** La venta : auberge basse, enseigne et tonneau. */
function Venta({ ...p }: P) {
  return (
    <g transform={at(p)}>
      <rect x="-16" y="-12" width="32" height="12" fill={WHITE} stroke={STONE} strokeWidth="0.6" />
      <path d="M-18 -12 H18 L14 -18 H-14Z" fill={TERRACOTTA} />
      <rect x="-4" y="-8" width="8" height="8" fill={WOOD} />
      <path d="M8 -18 V-24 H16 V-20 H8" fill={RED} />
      <ellipse cx="-11" cy="-3" rx="3" ry="3.5" fill={WOOD} stroke="#5A3A1A" strokeWidth="0.6" />
    </g>
  );
}

/** Mouton de Sancho. */
function Sheep({ ...p }: P) {
  return (
    <g transform={at(p)}>
      <path d="M-5 0 V-4 M-2 0 V-4 M3 0 V-4 M6 0 V-4" stroke="#3A3A3A" strokeWidth="1" />
      <ellipse cx="0" cy="-7" rx="8" ry="5" fill={WHITE} stroke={STONE} strokeWidth="0.6" />
      <ellipse cx="8" cy="-9" rx="3" ry="2.5" fill="#3A3A3A" />
    </g>
  );
}

/** Étal du marché : auvent rayé, paniers. */
function MarketStall({ ...p }: P) {
  return (
    <g transform={at(p)}>
      <path d="M-14 0 V-12 M14 0 V-12" stroke={WOOD} strokeWidth="1.4" />
      <path d="M-16 -12 H16 L14 -18 H-14Z" fill={RED} />
      <path d="M-10 -18 L-12 -12 M-2 -18 L-4 -12 M6 -18 L4 -12" stroke={WHITE} strokeWidth="2" />
      <rect x="-12" y="-6" width="24" height="4" fill={WOOD} />
      <circle cx="-7" cy="-7" r="2" fill="#E8772E" />
      <circle cx="-2" cy="-7" r="2" fill="#E8772E" />
      <circle cx="5" cy="-7" r="2" fill="#5E8C3A" />
    </g>
  );
}

/** Sierra : montagnes enneigées. */
function Sierra({ ...p }: P) {
  return (
    <g transform={at(p)}>
      <path d="M-22 0 L-8 -22 L2 -10 L10 -24 L24 0Z" fill="#8A8070" />
      <path d="M-8 -22 L-4 -15 L-11 -17Z M10 -24 L14 -17 L6 -18Z" fill={WHITE} />
    </g>
  );
}

/** Nuage de pluie (le Nuberu) ou soleil (calme). */
function Weather({ calm = false, ...p }: P & { calm?: boolean }) {
  if (calm)
    return (
      <g transform={at(p)}>
        <circle cx="0" cy="0" r="6" fill={GOLD} />
        {[0, 45, 90, 135, 180, 225, 270, 315].map((a) => <path key={a} d="M0 -9 V-12" stroke={GOLD} strokeWidth="1.4" transform={`rotate(${a})`} />)}
      </g>
    );
  return (
    <g transform={at(p)}>
      <ellipse cx="0" cy="0" rx="12" ry="6" fill="#8A93A6" />
      <ellipse cx="7" cy="-3" rx="8" ry="5" fill="#9AA3B6" />
      <path d="M-6 8 l-2 4 M0 8 l-2 4 M6 8 l-2 4" stroke={SKY} strokeWidth="1.4" />
    </g>
  );
}

/** Château des Ducs : tours crénelées et bannière. */
function Palace({ ...p }: P) {
  return (
    <g transform={at(p)}>
      <rect x="-16" y="-18" width="32" height="18" fill={OCHRE} />
      <rect x="-20" y="-28" width="8" height="28" fill="#B8823A" />
      <rect x="12" y="-28" width="8" height="28" fill="#B8823A" />
      <path d="M-20 -28 v-3 h2 v3 h2 v-3 h2 v3 M12 -28 v-3 h2 v3 h2 v-3 h2 v3" stroke="#B8823A" strokeWidth="1.4" fill="none" />
      <path d="M16 -31 V-40 L23 -37 L16 -34" fill={RED} stroke={WOOD} strokeWidth="0.6" />
      <path d="M-4 0 V-9 Q0 -13 4 -9 V0Z" fill={WOOD} />
    </g>
  );
}

/** Lance et bouclier du chevalier. */
function Lance({ ...p }: P) {
  return (
    <g transform={at(p)}>
      <path d="M-10 0 L12 -30" stroke={WOOD} strokeWidth="1.6" />
      <path d="M12 -30 L14 -35 L10 -32Z" fill={STONE} />
      <ellipse cx="-2" cy="-8" rx="6" ry="7.5" fill={STONE} stroke="#6A6A6A" strokeWidth="1" />
      <path d="M-2 -14 V-2 M-7 -8 H3" stroke={RED} strokeWidth="1.4" />
    </g>
  );
}

export const SPANISH_SCENES: Record<string, (calm: boolean) => ReactNode> = {
  // L'auberge où Don Quichotte se fait adouber
  'delea1-w1': () => (<><Venta x={-10} y={12} /><Lance x={16} y={12} /><OliveTree x={30} y={12} s={0.7} /></>),
  // La maison de Sancho : la ferme et les moutons
  'delea1-w2': () => (<><WhiteHouse x={-12} y={12} /><Sheep x={10} y={14} /><Sheep x={22} y={12} s={0.8} /></>),
  // Le village : église et maisons, sous l'orage du Nuberu
  'delea1-w3': (calm) => (<><Church x={-12} y={12} /><WhiteHouse x={10} y={12} s={0.8} /><Weather x={24} y={-18} calm={calm} /></>),
  // La venta et ses oliviers
  'delea1-w4': () => (<><Venta x={-8} y={12} s={1.1} /><OliveTree x={20} y={12} /><OliveTree x={32} y={14} s={0.6} /></>),
  // La forêt du Busgosu
  'delea1-w5': () => (<><OliveTree x={-14} y={12} /><OliveTree x={2} y={14} s={0.8} /><WhiteHouse x={22} y={12} s={0.7} /></>),
  // Le marché du Toboso
  'delea1-w6': () => (<><MarketStall x={-10} y={12} /><MarketStall x={14} y={12} s={0.8} /><Church x={30} y={12} s={0.6} /></>),
  // La sierra en toutes saisons
  'delea1-w7': (calm) => (<><Sierra x={-6} y={12} /><Sheep x={20} y={12} s={0.8} /><Weather x={-20} y={-18} calm={calm} /></>),
  // Les géants de la plaine
  'delea1-w8': (calm) => (<><Windmill x={-14} y={12} spin={!calm} /><Windmill x={6} y={12} s={0.85} spin={!calm} /><Windmill x={24} y={12} s={0.7} spin={!calm} /></>),
  // Le palais des Ducs
  'delea1-final': () => (<><Palace x={-4} y={14} s={1.1} /><Windmill x={26} y={12} s={0.6} /></>),
};
