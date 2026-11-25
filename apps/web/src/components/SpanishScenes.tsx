import type { ReactNode } from 'react';

/**
 * Mode histoire espagnol (l'écuyer·ère de Don Quichotte) : le décor de chaque île raconte son chapitre.
 * DELE A1, la Manche : moulins à vent, maisons blanches, venta, oliviers, sierra et château des Ducs.
 * DELE A2, la route de Barcelone : rivière, ferme d'Aragon, fontaine, diligence, toits envolés, crêtes, fête et port.
 * DELE B1, le chemin de Saint-Jacques : col des Pyrénées, vignes, cathédrales, blés de la Meseta, château templier, hórreo, phare.
 * Dessins originaux, centrés sur (0, 0).
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

const SEA = '#3A7FB0';

/** Rivière qui serpente, avec un gué de pierres. */
function River({ ...p }: P) {
  return (
    <g transform={at(p)}>
      <path d="M-26 0 Q-14 -6 -4 -2 Q8 3 18 -3 Q24 -6 28 -4 L28 2 Q22 0 16 4 Q6 9 -6 4 Q-16 0 -26 6Z" fill={SKY} stroke={SEA} strokeWidth="0.6" />
      {[-12, -4, 4].map((x) => <ellipse key={x} cx={x} cy={1} rx="2.6" ry="1.4" fill={STONE} />)}
    </g>
  );
}

/** Fontaine de pierre et son jet d'eau. */
function Fountain({ ...p }: P) {
  return (
    <g transform={at(p)}>
      <ellipse cx="0" cy="-2" rx="14" ry="4" fill={STONE} />
      <rect x="-14" y="-6" width="28" height="4" fill={STONE} />
      <ellipse cx="0" cy="-6" rx="12" ry="2.5" fill={SKY} />
      <rect x="-1.5" y="-18" width="3" height="12" fill={STONE} />
      <path d="M0 -18 Q-6 -24 -8 -12 M0 -18 Q6 -24 8 -12" stroke={SKY} strokeWidth="1.2" fill="none" />
    </g>
  );
}

/** Diligence : caisse, roues et timon. */
function Coach({ ...p }: P) {
  return (
    <g transform={at(p)}>
      <rect x="-12" y="-18" width="22" height="12" rx="2" fill={ROOF} />
      <rect x="-9" y="-16" width="6" height="5" fill={SKY} />
      <rect x="1" y="-16" width="6" height="5" fill={SKY} />
      <path d="M10 -8 L20 -4" stroke={WOOD} strokeWidth="1.4" />
      {[-7, 6].map((x) => <g key={x}><circle cx={x} cy={-4} r="4" fill="none" stroke={WOOD} strokeWidth="1.4" /><path d={`M${x - 4} -4 H${x + 4} M${x} -8 V0`} stroke={WOOD} strokeWidth="0.6" /></g>)}
    </g>
  );
}

/** Maison dont le toit s'envole (le Diablo Cojuelo). */
function RooflessHouse({ calm = false, ...p }: P & { calm?: boolean }) {
  return (
    <g transform={at(p)}>
      <rect x="-12" y="-14" width="24" height="14" fill={WHITE} stroke={STONE} strokeWidth="0.6" />
      <rect x="-3" y="-8" width="6" height="8" fill={WOOD} />
      <rect x="-9" y="-11" width="4" height="4" fill="#3A6AA8" />
      <rect x="5" y="-11" width="4" height="4" fill="#3A6AA8" />
      <path d={calm ? 'M-14 -14 L0 -22 L14 -14Z' : 'M-10 -24 L4 -34 L18 -28Z'} fill={ROOF} transform={calm ? undefined : 'rotate(-12 4 -28)'} />
    </g>
  );
}

/** Crêtes montagneuses enneigées. */
function Ridge({ ...p }: P) {
  return (
    <g transform={at(p)}>
      <path d="M-30 0 L-16 -26 L-6 -12 L6 -34 L22 -8 L30 0Z" fill="#7A8A9A" />
      <path d="M-20 -18 L-16 -26 L-12 -20Z M2 -26 L6 -34 L10 -26 L6 -28Z" fill={WHITE} />
    </g>
  );
}

/** Guirlande de fête et lampions. */
function Festoon({ ...p }: P) {
  return (
    <g transform={at(p)}>
      <path d="M-24 -24 Q0 -14 24 -24" stroke={WOOD} strokeWidth="0.6" fill="none" />
      {[-18, -9, 0, 9, 18].map((x, i) => <path key={x} d={`M${x - 3} ${-21 + Math.abs(x) / 9} l3 6 l3 -6Z`} fill={[RED, GOLD, SEA, OLIVE, RED][i]} />)}
      <path d="M-20 0 V-22 M20 0 V-22" stroke={WOOD} strokeWidth="1.2" />
    </g>
  );
}

/** Feux d'artifice (éteints quand l'île est apaisée). */
function Fireworks({ calm = false, ...p }: P & { calm?: boolean }) {
  if (calm) return null;
  return (
    <g transform={at(p)} stroke={GOLD} strokeWidth="1" strokeLinecap="round">
      {[0, 45, 90, 135, 180, 225, 270, 315].map((a) => <path key={a} d="M0 -3 V-8" transform={`rotate(${a})`} />)}
      <g transform="translate(14 6) scale(0.7)" stroke={RED}>{[0, 60, 120, 180, 240, 300].map((a) => <path key={a} d="M0 -3 V-8" transform={`rotate(${a})`} />)}</g>
    </g>
  );
}

/** La mer et un voilier. */
function SeaBoat({ ...p }: P) {
  return (
    <g transform={at(p)}>
      <path d="M-30 0 Q-22 -4 -15 0 T0 0 T15 0 T30 0 V6 H-30Z" fill={SEA} />
      <path d="M-6 -2 H10 L7 2 H-3Z" fill={WOOD} />
      <path d="M2 -2 V-22 L12 -6Z" fill={WHITE} stroke={STONE} strokeWidth="0.5" />
      <path d="M1 -2 V-18 L-6 -6Z" fill={WHITE} stroke={STONE} strokeWidth="0.5" />
    </g>
  );
}

/** Tours de cathédrale moderniste (silhouette générique). */
function Spires({ ...p }: P) {
  return (
    <g transform={at(p)} fill={OCHRE}>
      {[-9, -3, 3, 9].map((x, i) => <path key={x} d={`M${x - 2.5} 0 V${-26 - (i % 3) * 4} Q${x} ${-36 - (i % 3) * 4} ${x + 2.5} ${-26 - (i % 3) * 4} V0Z`} />)}
      <rect x="-13" y="-10" width="26" height="10" fill="#B8823A" />
    </g>
  );
}

/** Rose de Sant Jordi. */
function Rose({ ...p }: P) {
  return (
    <g transform={at(p)}>
      <path d="M0 0 V-12" stroke={OLIVE} strokeWidth="1.2" />
      <path d="M0 -6 Q4 -8 5 -5" fill={OLIVE} />
      <circle cx="0" cy="-14" r="3.5" fill={RED} />
      <path d="M-2 -15 Q0 -12 2 -15" stroke="#8E1B26" strokeWidth="0.6" fill="none" />
    </g>
  );
}

/** Rangs de vigne et grappes. */
function Vineyard({ ...p }: P) {
  return (
    <g transform={at(p)}>
      {[-8, -2, 4].map((y, i) => <path key={y} d={`M${-26 + i * 3} ${y} Q0 ${y - 3} ${26 - i * 3} ${y}`} stroke={OLIVE} strokeWidth="2.2" fill="none" strokeDasharray="3 2" />)}
      {[-14, 2, 16].map((x) => <g key={x} fill="#6A2A5A">{[[0, 0], [2, 0], [1, 2]].map(([dx, dy]) => <circle key={`${dx}${dy}`} cx={x + dx} cy={-12 + dy} r="1.3" />)}</g>)}
    </g>
  );
}

/** Tonneau de vin. */
function Barrel({ ...p }: P) {
  return (
    <g transform={at(p)}>
      <ellipse cx="0" cy="-8" rx="7" ry="9" fill={WOOD} />
      <path d="M-6 -13 H6 M-6 -3 H6" stroke="#4A2A1A" strokeWidth="1.2" />
      <ellipse cx="0" cy="-8" rx="2.5" ry="3" fill="#5A3420" />
    </g>
  );
}

/** Cathédrale gothique : deux flèches ajourées et une rosace. */
function Gothic({ ...p }: P) {
  return (
    <g transform={at(p)}>
      <rect x="-14" y="-18" width="28" height="18" fill={STONE} />
      {[-10, 10].map((x) => <g key={x}><rect x={x - 4} y="-30" width="8" height="14" fill={STONE} /><path d={`M${x - 4} -30 L${x} -46 L${x + 4} -30Z`} fill="#9A9080" /></g>)}
      <circle cx="0" cy="-11" r="4.5" fill="#3A6AA8" stroke={GOLD} strokeWidth="1" />
      <path d="M-3 0 V-4 Q0 -7 3 -4 V0Z" fill={WOOD} />
    </g>
  );
}

/** Champ de blé et arbre solitaire de la Meseta. */
function Wheat({ ...p }: P) {
  return (
    <g transform={at(p)}>
      <path d="M-30 0 Q0 -6 30 0Z" fill={GOLD} />
      {[-22, -14, -6, 2, 10, 18].map((x) => <path key={x} d={`M${x} -1 V-7 M${x - 1.5} -6 L${x} -8 L${x + 1.5} -6`} stroke="#B8902A" strokeWidth="0.8" fill="none" />)}
      <path d="M24 0 V-12" stroke={WOOD} strokeWidth="1.6" />
      <circle cx="24" cy="-15" r="6" fill={OLIVE} />
    </g>
  );
}

/** Rosace de vitrail. */
function RoseWindow({ ...p }: P) {
  return (
    <g transform={at(p)}>
      <circle cx="0" cy="-14" r="13" fill={STONE} />
      {[0, 45, 90, 135, 180, 225, 270, 315].map((a, i) => <path key={a} d="M0 -14 L0 -25 A11 11 0 0 1 7.8 -21.8Z" transform={`rotate(${a} 0 -14)`} fill={[RED, '#3A6AA8', GOLD, OLIVE][i % 4]} />)}
      <circle cx="0" cy="-14" r="3" fill={GOLD} />
    </g>
  );
}

/** Château templier : tours crénelées. */
function Castle({ ...p }: P) {
  return (
    <g transform={at(p)}>
      <rect x="-16" y="-16" width="32" height="16" fill={STONE} />
      {[-16, 8].map((x) => <g key={x}><rect x={x} y="-26" width="8" height="26" fill="#A89E88" /><path d={`M${x} -26 v-3 h2 v3 h2 v-3 h2 v3 h2 v-3`} stroke="#A89E88" strokeWidth="1.4" fill="none" /></g>)}
      <path d="M-3 0 V-8 Q0 -11 3 -8 V0Z" fill="#3A2A1A" />
      <path d="M0 -26 V-36 L8 -33 L0 -30" fill="#F6F1E6" stroke={WOOD} strokeWidth="0.6" />
      <path d="M2 -34 H5 M3.5 -35.5 V-31.5" stroke={RED} strokeWidth="0.8" />
    </g>
  );
}

/** Hórreo galicien : grenier de pierre sur pilotis, croix sur le toit. */
function Horreo({ ...p }: P) {
  return (
    <g transform={at(p)}>
      {[-10, 10].map((x) => <rect key={x} x={x - 1.5} y="-6" width="3" height="6" fill={STONE} />)}
      <rect x="-14" y="-8" width="28" height="2" fill="#9A9080" />
      <rect x="-12" y="-17" width="24" height="9" fill={STONE} />
      {[-8, -4, 0, 4, 8].map((x) => <rect key={x} x={x - 0.5} y="-16" width="1" height="7" fill="#6A6458" />)}
      <path d="M-14 -17 L0 -23 L14 -17Z" fill={ROOF} />
      <path d="M-14 -23 V-27 M-15.5 -25.5 H-12.5" stroke={STONE} strokeWidth="1" />
    </g>
  );
}

/** Coquille Saint-Jacques. */
function Scallop({ ...p }: P) {
  return (
    <g transform={at(p)}>
      <path d="M-8 -2 Q-10 -14 0 -16 Q10 -14 8 -2 Z" fill={GOLD} stroke="#B8902A" strokeWidth="0.8" />
      {[-5, -2.5, 0, 2.5, 5].map((x) => <path key={x} d={`M0 -2 L${x * 1.4} -14`} stroke="#B8902A" strokeWidth="0.6" />)}
      <rect x="-3" y="-3" width="6" height="2" fill="#B8902A" />
    </g>
  );
}

/** Phare au bord de la falaise. */
function Lighthouse({ calm = false, ...p }: P & { calm?: boolean }) {
  return (
    <g transform={at(p)}>
      <path d="M-14 0 L-10 -6 L10 -6 L14 0Z" fill="#7A6A5A" />
      <path d="M-4 -6 L-3 -26 H3 L4 -6Z" fill={WHITE} stroke={STONE} strokeWidth="0.6" />
      <rect x="-3" y="-18" width="6" height="3" fill={RED} />
      <rect x="-3.5" y="-31" width="7" height="5" fill={GOLD} />
      <path d="M-4 -31 L0 -35 L4 -31Z" fill={RED} />
      {!calm && <path d="M4 -29 L24 -36 L24 -22Z" fill={GOLD} opacity="0.45" />}
    </g>
  );
}

/** Cathédrale baroque de Saint-Jacques : deux tours. */
function Santiago({ ...p }: P) {
  return (
    <g transform={at(p)}>
      <rect x="-12" y="-20" width="24" height="20" fill={OCHRE} />
      {[-14, 8].map((x) => <g key={x}><rect x={x} y="-38" width="6" height="38" fill="#B8823A" /><path d={`M${x} -38 L${x + 3} -46 L${x + 6} -38Z`} fill="#9A6A2A" /><circle cx={x + 3} cy="-30" r="1.4" fill={GOLD} /></g>)}
      <path d="M-4 0 V-10 Q0 -14 4 -10 V0Z" fill={WOOD} />
      <circle cx="0" cy="-16" r="2" fill={GOLD} />
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
  // DELE A2 — la deuxième sortie : le gué de la Lamia
  'delea2-w1': () => (<><River x={0} y={14} /><OliveTree x={-20} y={8} s={0.7} /><Lance x={22} y={8} s={0.8} /></>),
  // L'auberge du Tragaldabas
  'delea2-w2': () => (<><Venta x={-10} y={12} /><OliveTree x={18} y={12} s={0.8} /></>),
  // La vieille ferme d'Aragon
  'delea2-w3': () => (<><WhiteHouse x={-12} y={12} s={1.1} /><Sheep x={12} y={14} s={0.9} /><Church x={28} y={12} s={0.55} /></>),
  // La fontaine de l'Encantada et la diligence pour Saragosse
  'delea2-w4': () => (<><Fountain x={-12} y={12} /><Coach x={14} y={12} /></>),
  // La maison sans toit du Diablo Cojuelo
  'delea2-w5': (calm) => (<><RooflessHouse x={-8} y={12} s={1.1} calm={calm} /><WhiteHouse x={18} y={12} s={0.7} /></>),
  // Les crêtes de Mari d'Amboto
  'delea2-w6': (calm) => (<><Ridge x={0} y={12} /><Weather x={-22} y={-20} calm={calm} /></>),
  // La fête du village et la Mula Guita
  'delea2-w7': (calm) => (<><Festoon x={-4} y={12} /><Fireworks x={18} y={-22} calm={calm} /><Church x={26} y={12} s={0.55} /></>),
  // La plage de Barcelone et le Drac
  'delea2-w8': () => (<><SeaBoat x={-6} y={14} /><Rose x={24} y={12} /></>),
  // Le duel sur la plage face au chevalier de la Blanche Lune
  'delea2-final': () => (<><Spires x={-14} y={12} /><SeaBoat x={14} y={14} s={0.8} /><Lance x={30} y={10} s={0.7} /></>),
  // DELE B1 — le chemin de Saint-Jacques : le col des Pyrénées dans la brume de l'Herensuge
  'deleb1-w1': (calm) => (<><Ridge x={-2} y={12} /><Scallop x={24} y={12} /><Weather x={-22} y={-20} calm={calm} /></>),
  // Les vignes de la Rioja
  'deleb1-w2': () => (<><Vineyard x={-4} y={14} /><Barrel x={22} y={12} /></>),
  // La cathédrale de Burgos
  'deleb1-w3': () => (<><Gothic x={-6} y={12} s={1.1} /><WhiteHouse x={20} y={12} s={0.6} /></>),
  // La Meseta infinie
  'deleb1-w4': () => (<><Wheat x={-2} y={14} /><Scallop x={-24} y={12} s={0.8} /></>),
  // Les vitraux de León
  'deleb1-w5': () => (<><RoseWindow x={-8} y={12} /><Gothic x={18} y={12} s={0.6} /></>),
  // Le château des Templiers de Ponferrada
  'deleb1-w6': () => (<><Castle x={-4} y={12} s={1.1} /><OliveTree x={24} y={12} s={0.6} /></>),
  // Les brumes de Galice : hórreo et brouillard
  'deleb1-w7': (calm) => (<><Horreo x={-8} y={12} /><OliveTree x={18} y={12} s={0.7} /><Weather x={22} y={-20} calm={calm} /></>),
  // Fisterra, la fin du monde
  'deleb1-w8': (calm) => (<><Lighthouse x={-12} y={12} calm={calm} /><SeaBoat x={14} y={14} s={0.7} /></>),
  // La cathédrale de Saint-Jacques
  'deleb1-final': () => (<><Santiago x={-6} y={12} s={1.1} /><Scallop x={22} y={12} /></>),
};
