import type { ReactNode } from 'react';

/**
 * Mode histoire espagnol (l'écuyer·ère de Don Quichotte) : le décor de chaque île raconte son chapitre.
 * DELE A1, la Manche : moulins à vent, maisons blanches, venta, oliviers, sierra et château des Ducs.
 * DELE A2, la route de Barcelone : rivière, ferme d'Aragon, fontaine, diligence, toits envolés, crêtes, fête et port.
 * DELE B1, le chemin de Saint-Jacques : col des Pyrénées, vignes, cathédrales, blés de la Meseta, château templier, hórreo, phare.
 * DELE B2, la traversée des Amériques : Teide, La Havane, Mexico, Antigua, Magdalena, Andes, Chiloé, Buenos Aires.
 * DELE C1, la Bibliothèque enchantée : rayonnages, manuscrits, lion de pierre, tour, verre, statue, source, façade de Salamanque.
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

/** Volcan : cône et panache (éteint quand l'île est apaisée). */
function Volcano({ calm = false, ...p }: P & { calm?: boolean }) {
  return (
    <g transform={at(p)}>
      <path d="M-30 0 L-8 -32 H8 L30 0Z" fill="#7A5A4A" />
      <path d="M-8 -32 H8 L4 -26 H-4Z" fill={calm ? '#5A4A3A' : '#E2622E'} />
      <path d="M-14 -24 L-8 -32 L-6 -20Z M10 -22 L8 -32 L14 -26Z" fill={WHITE} opacity="0.7" />
      {!calm && <g fill="#8A8A92" opacity="0.8"><circle cx="0" cy="-40" r="6" /><circle cx="8" cy="-48" r="7" /><circle cx="-4" cy="-54" r="5" /></g>}
    </g>
  );
}

/** Palmier. */
function Palm({ ...p }: P) {
  return (
    <g transform={at(p)}>
      <path d="M0 0 Q-2 -14 2 -26" stroke={WOOD} strokeWidth="2.4" fill="none" />
      {[-60, -20, 20, 60, 100].map((a) => <path key={a} d="M2 -26 Q10 -30 16 -24" stroke={OLIVE} strokeWidth="2.4" fill="none" transform={`rotate(${a} 2 -26)`} />)}
    </g>
  );
}

/** Maison coloniale colorée à arcades. */
function ColonialHouse({ color = '#E2A23B', ...p }: P & { color?: string }) {
  return (
    <g transform={at(p)}>
      <rect x="-14" y="-16" width="28" height="16" fill={color} />
      <rect x="-14" y="-18" width="28" height="2" fill={WHITE} />
      {[-9, 0, 9].map((x) => <path key={x} d={`M${x - 3} 0 V-7 Q${x} -11 ${x + 3} -7 V0Z`} fill="#3A2A1A" />)}
      {[-9, 0, 9].map((x) => <rect key={`w${x}`} x={x - 2} y="-15" width="4" height="4" fill="#3A6AA8" />)}
    </g>
  );
}

/** Voiture ancienne (La Havane). */
function ClassicCar({ ...p }: P) {
  return (
    <g transform={at(p)}>
      <path d="M-16 -4 V-9 Q-12 -10 -8 -10 L-4 -16 H6 L10 -10 Q16 -10 16 -6 V-4Z" fill="#3AA8A0" />
      <path d="M-3 -15 H5 L8 -10 H-6Z" fill={SKY} />
      {[-9, 9].map((x) => <circle key={x} cx={x} cy={-3} r="3.4" fill="#2A2A2A" stroke={STONE} strokeWidth="1" />)}
    </g>
  );
}

/** Pyramide à degrés. */
function Pyramid({ ...p }: P) {
  return (
    <g transform={at(p)}>
      {[0, 1, 2, 3].map((i) => <rect key={i} x={-24 + i * 5} y={-6 - i * 6} width={48 - i * 10} height="6" fill={i % 2 ? '#B89A6A' : '#A88A5A'} />)}
      <rect x="-5" y="-32" width="10" height="8" fill="#8A6A3A" />
      <path d="M-2 -6 V-24 H2 V-6Z" fill="#8A6A3A" />
    </g>
  );
}

/** Arche coloniale à horloge (Antigua). */
function ClockArch({ ...p }: P) {
  return (
    <g transform={at(p)}>
      <path d="M-20 0 V-22 H20 V0 H10 V-8 Q0 -18 -10 -8 V0Z" fill="#E2B84A" stroke="#B8902A" strokeWidth="0.8" />
      <rect x="-5" y="-30" width="10" height="9" fill="#E2B84A" />
      <circle cx="0" cy="-26" r="3" fill={WHITE} stroke={WOOD} strokeWidth="0.6" />
      <path d="M0 -26 V-28 M0 -26 H1.6" stroke={WOOD} strokeWidth="0.6" />
    </g>
  );
}

/** Pirogue sur l'eau. */
function Canoe({ ...p }: P) {
  return (
    <g transform={at(p)}>
      <path d="M-18 -4 Q0 4 18 -4 L14 0 Q0 6 -14 0Z" fill={WOOD} />
      <path d="M6 -14 L-2 4" stroke="#5A3A24" strokeWidth="1.4" />
      <ellipse cx="-2" cy="4" rx="3" ry="1.4" fill="#5A3A24" />
    </g>
  );
}

/** Lama des Andes. */
function Llama({ ...p }: P) {
  return (
    <g transform={at(p)}>
      <ellipse cx="0" cy="-10" rx="9" ry="5" fill="#F2E6D0" />
      <path d="M6 -12 V-26" stroke="#F2E6D0" strokeWidth="4" strokeLinecap="round" />
      <ellipse cx="8" cy="-27" rx="3.5" ry="2.4" fill="#F2E6D0" />
      <path d="M5 -29 L5 -33 M7 -29 L8 -33" stroke="#F2E6D0" strokeWidth="1.2" />
      {[-6, -2, 3, 7].map((x) => <path key={x} d={`M${x} -6 V0`} stroke="#D8C8B0" strokeWidth="1.6" />)}
      <rect x="-4" y="-16" width="8" height="3" fill={RED} />
    </g>
  );
}

/** Entrée de mine dans la montagne. */
function Mine({ ...p }: P) {
  return (
    <g transform={at(p)}>
      <path d="M-28 0 L-10 -30 L4 -18 L14 -34 L30 0Z" fill="#8A7A6A" />
      <path d="M-8 0 V-12 Q0 -20 8 -12 V0Z" fill="#2A2420" />
      <path d="M-9 0 V-13 M9 0 V-13 M-10 -13 H10" stroke={WOOD} strokeWidth="1.6" />
      <circle cx="14" cy="-6" r="1.6" fill={GOLD} />
    </g>
  );
}

/** Palafito de Chiloé : maison sur pilotis. */
function Palafito({ color = '#C8562E', ...p }: P & { color?: string }) {
  return (
    <g transform={at(p)}>
      {[-8, 0, 8].map((x) => <rect key={x} x={x - 0.8} y="-6" width="1.6" height="6" fill={WOOD} />)}
      <rect x="-11" y="-17" width="22" height="11" fill={color} />
      <path d="M-13 -17 L0 -24 L13 -17Z" fill="#5A4A4A" />
      <rect x="-3" y="-13" width="6" height="5" fill={SKY} />
    </g>
  );
}

/** Vaisseau fantôme lumineux (le Caleuche). */
function GhostShip({ calm = false, ...p }: P & { calm?: boolean }) {
  return (
    <g transform={at(p)} opacity={calm ? 0.35 : 1}>
      <path d="M-20 -4 H20 L14 4 H-14Z" fill="#3A3A4A" />
      <path d="M-2 -4 V-30 M10 -4 V-22" stroke="#3A3A4A" strokeWidth="1.4" />
      <path d="M-2 -28 L-14 -10 H-2Z M10 -20 L18 -8 H10Z" fill="#E8F0FF" opacity="0.85" />
      {[-12, -4, 4, 12].map((x) => <circle key={x} cx={x} cy={-1} r="1.4" fill={GOLD} />)}
    </g>
  );
}

/** Obélisque de Buenos Aires. */
function Obelisk({ ...p }: P) {
  return (
    <g transform={at(p)}>
      <path d="M-4 0 L-2.6 -40 L0 -44 L2.6 -40 L4 0Z" fill={WHITE} stroke={STONE} strokeWidth="0.6" />
      <rect x="-1" y="-30" width="2" height="2" fill="#3A3A4A" />
    </g>
  );
}

/** Théâtre à l'italienne (le Colón). */
function Theatre({ ...p }: P) {
  return (
    <g transform={at(p)}>
      <rect x="-20" y="-20" width="40" height="20" fill="#E8DCC0" />
      <path d="M-22 -20 H22 L18 -26 H-18Z" fill="#B8A07A" />
      {[-14, -7, 0, 7, 14].map((x) => <rect key={x} x={x - 1.4} y="-18" width="2.8" height="18" fill={WHITE} />)}
      <path d="M-6 -26 Q0 -34 6 -26Z" fill="#7A9AA0" />
    </g>
  );
}

/** Rayonnage de livres. */
function Bookshelf({ ...p }: P) {
  const colors = [RED, '#3A6AA8', OLIVE, GOLD, '#6A3A5A', TERRACOTTA];
  return (
    <g transform={at(p)}>
      <rect x="-18" y="-30" width="36" height="30" fill={WOOD} />
      {[-28, -18, -8].map((y, r) => <g key={y}>{[0, 1, 2, 3, 4, 5].map((i) => <rect key={i} x={-16 + i * 5.4} y={y} width="4.6" height="8" fill={colors[(i + r) % colors.length]} />)}<rect x="-18" y={y + 8} width="36" height="1.6" fill="#5A3420" /></g>)}
    </g>
  );
}

/** Livre ouvert. */
function OpenBook({ ...p }: P) {
  return (
    <g transform={at(p)}>
      <path d="M0 -4 Q-10 -10 -20 -6 V-18 Q-10 -22 0 -16Z" fill={WHITE} stroke={STONE} strokeWidth="0.8" />
      <path d="M0 -4 Q10 -10 20 -6 V-18 Q10 -22 0 -16Z" fill={WHITE} stroke={STONE} strokeWidth="0.8" />
      {[-14, -11, -8].map((y) => <path key={y} d={`M-16 ${y} Q-9 ${y - 3} -3 ${y + 1} M3 ${y + 1} Q9 ${y - 3} 16 ${y}`} stroke="#9A9080" strokeWidth="0.5" fill="none" />)}
    </g>
  );
}

/** Plume et encrier. */
function Quill({ ...p }: P) {
  return (
    <g transform={at(p)}>
      <rect x="-4" y="-6" width="8" height="6" rx="1.5" fill="#2A2A3A" />
      <path d="M0 -6 L10 -28 Q14 -34 12 -24 Q8 -14 1 -6Z" fill={WHITE} stroke={STONE} strokeWidth="0.6" />
    </g>
  );
}

/** Lion de pierre sur son socle. */
function LionStatue({ ...p }: P) {
  return (
    <g transform={at(p)}>
      <rect x="-14" y="-6" width="28" height="6" fill={STONE} />
      <ellipse cx="0" cy="-12" rx="11" ry="6" fill="#C8A86A" />
      <circle cx="9" cy="-19" r="6" fill="#B8904A" />
      <circle cx="10" cy="-19" r="3.4" fill="#D8B87A" />
      <path d="M-11 -12 Q-18 -18 -14 -22" stroke="#C8A86A" strokeWidth="2" fill="none" />
    </g>
  );
}

/** Tour de pierre avec chaînes. */
function ChainTower({ ...p }: P) {
  return (
    <g transform={at(p)}>
      <rect x="-8" y="-36" width="16" height="36" fill="#8A8070" />
      <path d="M-9 -36 v-3 h3 v3 h3 v-3 h3 v3 h3 v-3 h3 v3" stroke="#8A8070" strokeWidth="1.6" fill="none" />
      <rect x="-2.5" y="-26" width="5" height="7" fill="#2A2420" />
      <path d="M8 -14 Q16 -10 14 -2" stroke="#5A5A5A" strokeWidth="1.2" strokeDasharray="2 1" fill="none" />
    </g>
  );
}

/** Carafe de verre. */
function GlassFlask({ ...p }: P) {
  return (
    <g transform={at(p)}>
      <path d="M-3 -24 H3 V-16 Q12 -10 10 -2 Q8 2 0 2 Q-8 2 -10 -2 Q-12 -10 -3 -16Z" fill="#CFE6F2" stroke="#7AA8C8" strokeWidth="1" opacity="0.9" />
      <path d="M-5 -8 Q-4 -4 -2 -3" stroke={WHITE} strokeWidth="1.2" fill="none" />
    </g>
  );
}

/** Statue de pierre du Commandeur. */
function StoneStatue({ ...p }: P) {
  return (
    <g transform={at(p)}>
      <rect x="-10" y="-6" width="20" height="6" fill="#8A8A86" />
      <path d="M-6 -6 V-24 Q0 -28 6 -24 V-6Z" fill="#A8A8A4" />
      <circle cx="0" cy="-29" r="4.4" fill="#A8A8A4" />
      <path d="M6 -20 L14 -32" stroke="#8A8A86" strokeWidth="1.6" />
    </g>
  );
}

/** Source aux yeux verts. */
function GreenEyesSpring({ calm = false, ...p }: P & { calm?: boolean }) {
  return (
    <g transform={at(p)}>
      <ellipse cx="0" cy="-2" rx="18" ry="5" fill="#5A9AA8" />
      {!calm && <g fill="#2EA86A">{[-5, 5].map((x) => <ellipse key={x} cx={x} cy={-2} rx="2.4" ry="1.3" />)}</g>}
      <path d="M-18 -2 Q-22 -10 -16 -14 M18 -2 Q22 -10 16 -14" stroke={OLIVE} strokeWidth="1.6" fill="none" />
    </g>
  );
}

/** Façade plateresque de l'université de Salamanque (avec sa grenouille). */
function Facade({ ...p }: P) {
  return (
    <g transform={at(p)}>
      <rect x="-18" y="-30" width="36" height="30" fill="#E2B87A" />
      {[-24, -16].map((y) => <path key={y} d={`M-16 ${y} H16`} stroke="#B8904A" strokeWidth="0.8" strokeDasharray="2 1.5" />)}
      {[-9, 9].map((x) => <path key={x} d={`M${x - 4} 0 V-10 Q${x} -15 ${x + 4} -10 V0Z`} fill="#5A3A24" />)}
      <circle cx="0" cy="-20" r="2.2" fill="#7AAA4A" />
    </g>
  );
}

/** Lampe de bibliothèque verte. */
function ReadingLamp({ ...p }: P) {
  return (
    <g transform={at(p)}>
      <rect x="-10" y="-2" width="20" height="2" fill={WOOD} />
      <path d="M0 -2 V-12" stroke={GOLD} strokeWidth="1.4" />
      <path d="M-8 -12 Q0 -20 8 -12Z" fill="#2E7A4A" />
      <ellipse cx="0" cy="-12" rx="8" ry="1.4" fill="#FFF6C8" />
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
  // DELE B2 — la traversée des Amériques : le Teide de Guayota
  'deleb2-w1': (calm) => (<><Volcano x={-6} y={12} calm={calm} /><Palm x={24} y={12} s={0.8} /></>),
  // La Havane : maisons colorées et voiture ancienne
  'deleb2-w2': () => (<><ColonialHouse x={-12} y={12} color="#E2869A" /><ClassicCar x={16} y={14} /></>),
  // Mexico : marché et pyramide
  'deleb2-w3': () => (<><Pyramid x={-10} y={12} /><Festoon x={18} y={12} s={0.6} /></>),
  // Antigua : arche coloniale et volcan
  'deleb2-w4': (calm) => (<><Volcano x={14} y={12} s={0.8} calm={calm} /><ClockArch x={-12} y={12} /></>),
  // Le fleuve Magdalena
  'deleb2-w5': () => (<><River x={0} y={14} /><Canoe x={-4} y={10} s={0.8} /><Palm x={24} y={10} s={0.7} /></>),
  // Les Andes : mine et lama
  'deleb2-w6': () => (<><Mine x={-8} y={12} /><Llama x={20} y={12} /></>),
  // Chiloé : palafitos et vaisseau fantôme
  'deleb2-w7': (calm) => (<><Palafito x={-16} y={12} /><Palafito x={-2} y={12} s={0.8} color="#3A7AA8" /><GhostShip x={22} y={10} s={0.8} calm={calm} /></>),
  // Buenos Aires : l'obélisque et les maisons de couleur
  'deleb2-w8': () => (<><Obelisk x={-12} y={12} /><ColonialHouse x={10} y={12} s={0.8} color="#3AA8A0" /></>),
  // Le théâtre Colón
  'deleb2-final': () => (<><Theatre x={-4} y={12} s={1.1} /><Obelisk x={26} y={12} s={0.6} /></>),
  // DELE C1 — la Bibliothèque enchantée : la salle des incunables et le lion du Cid
  'delec1-w1': () => (<><LionStatue x={-10} y={12} /><OpenBook x={16} y={12} /></>),
  // Les intrigues de la Célestine entre les rayonnages
  'delec1-w2': () => (<><Bookshelf x={-10} y={12} /><Quill x={18} y={12} /></>),
  // Le pont de Salamanque du Lazarillo
  'delec1-w3': () => (<><River x={0} y={14} /><Facade x={-16} y={8} s={0.6} /><Bookshelf x={20} y={10} s={0.6} /></>),
  // La tour de Segismundo
  'delec1-w4': () => (<><ChainTower x={-6} y={12} /><OpenBook x={18} y={12} s={0.8} /></>),
  // Le Licencié de verre
  'delec1-w5': () => (<><GlassFlask x={-10} y={12} /><Bookshelf x={14} y={12} s={0.8} /></>),
  // La statue du Commandeur
  'delec1-w6': () => (<><StoneStatue x={-8} y={12} /><Church x={18} y={12} s={0.6} /></>),
  // La source aux yeux verts
  'delec1-w7': (calm) => (<><GreenEyesSpring x={-4} y={14} calm={calm} /><OliveTree x={22} y={10} s={0.7} /></>),
  // L'université de Salamanque et son spectre
  'delec1-w8': () => (<><Facade x={-6} y={12} /><Quill x={22} y={12} s={0.8} /></>),
  // La salle de lecture
  'delec1-final': () => (<><Bookshelf x={-16} y={12} /><ReadingLamp x={6} y={12} /><Bookshelf x={26} y={12} s={0.7} /></>),
};
