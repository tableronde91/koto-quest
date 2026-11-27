import type { ReactNode } from 'react';

/**
 * Mode histoire allemand (l'apprenti·e des frères Grimm) : le décor de chaque île raconte son chapitre.
 * Goethe A1, la Route des contes : maisons à colombages de Hanau et Steinau, ruelles de Marbourg, maison de pain d'épices,
 * château de Sababurg sous les ronces, marché de Göttingen, mont de Dame Holle, Hamelin et les Musiciens de Brême.
 * Goethe B2, Weimar : route du Roi des Aulnes, atelier de l'Apprenti sorcier, gouffre du Plongeur, arène, théâtre de Corinthe, forêt, lac, bibliothèque.
 * Goethe B1, le pays des légendes : grotte de Barberousse, monts de Rübezahl, barque du Pêcheur, Cologne, cabinet de Faust, rocher de la Lorelei, Brocken.
 * Goethe A2, du Rhin à la Forêt-Noire : puits du Roi Grenouille, bal de Cendrillon, tour de Raiponce, miroir de la Reine, halte du Chat botté, Oie d'or, château de Barbe-de-Grive.
 * Dessins originaux, centrés sur (0, 0).
 */
const PLASTER = '#F4EDDC';
const BEAM = '#5A3A24';
const ROOF = '#A8442E';
const STONE = '#A9A396';
const FIR = '#2F6B4F';
const FIR_DARK = '#1F4A36';
const WOOD = '#7A4A2A';
const RED = '#C8323F';
const GOLD = '#E2B84A';
const GINGER = '#B8733A';
const SNOW = '#FFFFFF';

type P = { x: number; y: number; s?: number };
const at = ({ x, y, s = 1 }: P) => `translate(${x} ${y}) scale(${s})`;

/** Maison à colombages : crépi clair, poutres sombres, toit rouge pentu. */
function TimberHouse({ ...p }: P) {
  return (
    <g transform={at(p)}>
      <rect x="-11" y="-15" width="22" height="15" fill={PLASTER} stroke={BEAM} strokeWidth="1" />
      <path d="M-11 -8 H11 M0 -15 V0 M-11 -15 L0 -8 M11 -15 L0 -8" stroke={BEAM} strokeWidth="1" fill="none" />
      <path d="M-13 -15 L0 -29 L13 -15Z" fill={ROOF} />
      <rect x="-8" y="-6" width="5" height="6" fill={WOOD} />
      <rect x="3" y="-13" width="4" height="4" fill="#3A6AA8" />
    </g>
  );
}

/** Sapin de la forêt des contes. */
function Fir({ ...p }: P) {
  return (
    <g transform={at(p)}>
      <rect x="-1.2" y="-4" width="2.4" height="5" fill={WOOD} />
      <path d="M0 -24 L8 -12 L4 -12 L10 -3 L-10 -3 L-4 -12 L-8 -12Z" fill={FIR} />
      <path d="M0 -24 L-8 -12 L-4 -12 L-10 -3 L-2 -3Z" fill={FIR_DARK} opacity="0.6" />
    </g>
  );
}

/** Feu de camp du Rumpelstilzchen : bûches et flammes (braises seules une fois le lutin reparti). */
function Campfire({ calm = false, ...p }: P & { calm?: boolean }) {
  return (
    <g transform={at(p)}>
      <path d="M-7 0 L7 -3 M-7 -3 L7 0" stroke={WOOD} strokeWidth="2.4" strokeLinecap="round" />
      {calm ? <circle cx="0" cy="-3" r="2" fill="#E2703A" /> : <><path d="M0 -16 Q7 -8 3 -2 H-3 Q-7 -8 0 -16Z" fill="#E2703A" /><path d="M0 -10 Q3 -6 1.5 -2 H-1.5 Q-3 -6 0 -10Z" fill={GOLD} /></>}
    </g>
  );
}

/** Les sept petits lits des Nains, alignés. */
function DwarfBeds({ ...p }: P) {
  return (
    <g transform={at(p)}>
      {[0, 1, 2, 3, 4, 5, 6].map((i) => (
        <g key={i} transform={`translate(${-15 + i * 5} 0)`}>
          <rect x="-2" y="-4" width="4" height="4" fill={i % 2 ? RED : '#3A6AA8'} />
          <rect x="-2" y="-6" width="4" height="2" fill={SNOW} />
        </g>
      ))}
    </g>
  );
}

/** Poteau indicateur à deux flèches, au carrefour du Loup. */
function Signpost({ ...p }: P) {
  return (
    <g transform={at(p)}>
      <rect x="-1" y="-20" width="2" height="20" fill={WOOD} />
      <path d="M1 -19 H10 L13 -16.5 L10 -14 H1Z" fill={PLASTER} stroke={BEAM} strokeWidth="0.7" />
      <path d="M-1 -12 H-10 L-13 -9.5 L-10 -7 H-1Z" fill={PLASTER} stroke={BEAM} strokeWidth="0.7" />
    </g>
  );
}

/** Maison de pain d'épices : murs bruns, glaçage blanc, bonbons. */
function GingerbreadHouse({ ...p }: P) {
  return (
    <g transform={at(p)}>
      <rect x="-11" y="-13" width="22" height="13" fill={GINGER} />
      <path d="M-14 -13 L0 -27 L14 -13Z" fill="#8A4E22" />
      <path d="M-14 -13 q3.5 4 7 0 q3.5 4 7 0 q3.5 4 7 0 q3.5 4 7 0" fill="none" stroke={SNOW} strokeWidth="1.6" />
      <rect x="-3" y="-8" width="6" height="8" rx="3" fill="#6A3A1A" />
      {[[-8, -6, RED], [7, -6, GOLD], [-5, -19, SNOW], [5, -19, RED], [0, -23, GOLD]].map(([cx, cy, c]) => <circle key={`${cx}${cy}`} cx={cx} cy={cy} r="1.5" fill={c as string} />)}
    </g>
  );
}

/** Château de la Belle au bois dormant : deux tours rondes, et les ronces tant que le temps est figé. */
function BriarCastle({ calm = false, ...p }: P & { calm?: boolean }) {
  return (
    <g transform={at(p)}>
      <rect x="-12" y="-14" width="24" height="14" fill={STONE} />
      <rect x="-17" y="-24" width="8" height="24" fill="#BDB7AA" />
      <rect x="9" y="-24" width="8" height="24" fill="#BDB7AA" />
      <path d="M-19 -24 L-13 -34 L-7 -24Z M7 -24 L13 -34 L19 -24Z" fill={ROOF} />
      <rect x="-3" y="-8" width="6" height="8" rx="3" fill={BEAM} />
      {calm ? <path d="M13 -34 V-40 L18 -38 L13 -36" fill={RED} stroke={BEAM} strokeWidth="0.5" /> : <path d="M-22 0 Q-16 -14 -8 -6 Q0 -18 8 -6 Q16 -14 22 0" fill="none" stroke={FIR_DARK} strokeWidth="1.6" />}
      {!calm && [[-15, -8], [0, -12], [15, -8]].map(([cx, cy]) => <circle key={cx} cx={cx} cy={cy} r="1.6" fill={RED} />)}
    </g>
  );
}

/** Étal du marché : auvent rayé et rouleaux de tissu. */
function ClothStall({ ...p }: P) {
  return (
    <g transform={at(p)}>
      <path d="M-11 -6 V0 M11 -6 V0" stroke={WOOD} strokeWidth="1.4" />
      <rect x="-11" y="-8" width="22" height="4" fill={WOOD} />
      <path d="M-13 -16 H13 L11 -10 H-11Z" fill={RED} />
      <path d="M-7 -16 L-6 -10 M0 -16 V-10 M7 -16 L6 -10" stroke={SNOW} strokeWidth="2" />
      {[[-6, '#3A6AA8'], [0, GOLD], [6, FIR]].map(([cx, c]) => <rect key={cx as number} x={(cx as number) - 2} y="-11" width="4" height="3" rx="1" fill={c as string} />)}
    </g>
  );
}

/** Le mont de Dame Holle : il neige tant qu'elle secoue ses édredons, le soleil revient ensuite. */
function HolleMountain({ calm = false, ...p }: P & { calm?: boolean }) {
  return (
    <g transform={at(p)}>
      <path d="M-22 0 L-4 -26 L6 -12 L12 -18 L24 0Z" fill="#7E8A7A" />
      <path d="M-4 -26 L-9 -18 L-5 -19 L-3 -16 L0 -19 L2 -17.5Z" fill={SNOW} />
      {calm ? (
        <g transform="translate(18 -30)"><circle r="5" fill={GOLD} />{[0, 60, 120, 180, 240, 300].map((a) => <path key={a} d="M0 -7.5 V-10" stroke={GOLD} strokeWidth="1.3" transform={`rotate(${a})`} />)}</g>
      ) : (
        <g fill={SNOW}><ellipse cx="14" cy="-32" rx="10" ry="5" /><ellipse cx="20" cy="-35" rx="7" ry="4" />{[[8, -24], [14, -20], [20, -25], [2, -30], [24, -16]].map(([cx, cy]) => <circle key={`${cx}${cy}`} cx={cx} cy={cy} r="1.2" />)}</g>
      )}
    </g>
  );
}

/** Porte de ville de Hamelin : arche de pierre et toit pointu. */
function TownGate({ ...p }: P) {
  return (
    <g transform={at(p)}>
      <rect x="-9" y="-20" width="18" height="20" fill={STONE} />
      <path d="M-11 -20 L0 -32 L11 -20Z" fill={ROOF} />
      <path d="M-4 0 V-8 Q0 -13 4 -8 V0Z" fill={BEAM} />
      <rect x="-2" y="-18" width="4" height="4" fill="#3A6AA8" />
    </g>
  );
}

/** Flûte et notes de musique du Joueur de flûte. */
function PipeNotes({ ...p }: P) {
  return (
    <g transform={at(p)}>
      <path d="M-8 0 L8 -6" stroke={WOOD} strokeWidth="2" strokeLinecap="round" />
      <g fill={BEAM}><circle cx="2" cy="-14" r="1.8" /><rect x="3.2" y="-22" width="0.9" height="8" /><circle cx="9" cy="-18" r="1.8" /><rect x="10.2" y="-26" width="0.9" height="8" /><path d="M3.2 -22 L11.1 -26 V-24 L3.2 -20Z" /></g>
    </g>
  );
}

/** Les Musiciens de Brême : l'âne, le chien, le chat et le coq, l'un sur l'autre. */
function Musicians({ ...p }: P) {
  return (
    <g transform={at(p)}>
      {/* Âne */}
      <rect x="-9" y="-12" width="18" height="8" rx="3" fill="#8A8A8A" />
      <path d="M-7 -4 V0 M-3 -4 V0 M3 -4 V0 M7 -4 V0" stroke="#6A6A6A" strokeWidth="1.8" />
      <path d="M8 -12 L13 -18 L14 -11Z" fill="#8A8A8A" /><path d="M11 -18 L12 -23 M13 -18 L15 -22" stroke="#6A6A6A" strokeWidth="1.2" />
      {/* Chien */}
      <rect x="-6" y="-19" width="12" height="7" rx="3" fill="#B8823A" /><circle cx="6" cy="-19" r="3" fill="#B8823A" />
      {/* Chat */}
      <rect x="-4" y="-25" width="8" height="6" rx="3" fill="#3A3A3A" /><path d="M2 -25 L3 -29 L5 -25 M4 -25 L6 -29 L7 -25" fill="#3A3A3A" /><circle cx="5" cy="-24" r="2.4" fill="#3A3A3A" />
      {/* Coq */}
      <ellipse cx="0" cy="-28" rx="3" ry="2.6" fill={SNOW} /><circle cx="3" cy="-31" r="1.8" fill={SNOW} /><path d="M2 -33 q1 -2 2 0 q1 -2 2 0" fill={RED} /><path d="M4.6 -31 L7 -30.5 L4.6 -30Z" fill={GOLD} />
    </g>
  );
}

/** Hôtel de ville de Brême : façade à pignons et arcades. */
function BremenHall({ ...p }: P) {
  return (
    <g transform={at(p)}>
      <rect x="-14" y="-14" width="28" height="14" fill="#C9A27A" />
      <path d="M-14 -14 L-9 -22 L-4 -14 L0 -24 L4 -14 L9 -22 L14 -14Z" fill="#6E8A7A" />
      {[-10, -3, 4].map((x) => <path key={x} d={`M${x} 0 V-5 Q${x + 3} -9 ${x + 6} -5 V0Z`} fill={BEAM} />)}
    </g>
  );
}

/** Vieux puits de pierre, sa poulie et la balle d'or. */
function Well({ calm = false, ...p }: P & { calm?: boolean }) {
  return (
    <g transform={at(p)}>
      <rect x="-9" y="-8" width="18" height="8" rx="2" fill={STONE} />
      <ellipse cx="0" cy="-8" rx="9" ry="3" fill="#3A6AA8" />
      <path d="M-8 -8 V-20 M8 -8 V-20" stroke={WOOD} strokeWidth="1.6" />
      <path d="M-11 -20 L0 -26 L11 -20Z" fill={ROOF} />
      <circle cx={calm ? 14 : 0} cy={calm ? -2 : -9} r="2.4" fill={GOLD} />
    </g>
  );
}

/** Tour de Raiponce : haute, sans porte, une seule fenêtre et la tresse dorée. */
function Tower({ calm = false, ...p }: P & { calm?: boolean }) {
  return (
    <g transform={at(p)}>
      <rect x="-6" y="-30" width="12" height="30" fill="#BDB7AA" />
      <path d="M-9 -30 L0 -42 L9 -30Z" fill={ROOF} />
      <rect x="-2.5" y="-26" width="5" height="6" rx="2.5" fill={BEAM} />
      {calm && <path d="M2 -21 Q7 -12 4 -2" stroke={GOLD} strokeWidth="2" fill="none" strokeLinecap="round" />}
      <path d="M-6 -8 H6 M-6 -16 H6" stroke={STONE} strokeWidth="0.6" />
    </g>
  );
}

/** Miroir de la Reine : cadre doré ovale sur pied. */
function Mirror({ ...p }: P) {
  return (
    <g transform={at(p)}>
      <path d="M0 0 V-8" stroke={GOLD} strokeWidth="2" />
      <path d="M-5 0 H5" stroke={GOLD} strokeWidth="2" strokeLinecap="round" />
      <ellipse cx="0" cy="-18" rx="8" ry="11" fill={GOLD} />
      <ellipse cx="0" cy="-18" rx="6" ry="9" fill="#CFE6F2" />
      <path d="M-3 -23 L2 -14" stroke={SNOW} strokeWidth="1.4" opacity="0.8" />
    </g>
  );
}

/** Château du Sud : donjon, deux ailes et bannière. */
function Castle({ ...p }: P) {
  return (
    <g transform={at(p)}>
      <rect x="-16" y="-12" width="32" height="12" fill={STONE} />
      <rect x="-6" y="-26" width="12" height="26" fill="#BDB7AA" />
      <path d="M-8 -26 L0 -36 L8 -26Z" fill={ROOF} />
      <path d="M-16 -12 V-15 H-13 V-12 M-10 -12 V-15 H-7 V-12 M7 -12 V-15 H10 V-12 M13 -12 V-15 H16 V-12" stroke={STONE} strokeWidth="2" />
      <rect x="-2.5" y="-7" width="5" height="7" rx="2.5" fill={BEAM} />
      <path d="M0 -36 V-42 L5 -40 L0 -38" fill={GOLD} stroke={BEAM} strokeWidth="0.5" />
    </g>
  );
}

/** L'Oie d'or. */
function Goose({ ...p }: P) {
  return (
    <g transform={at(p)}>
      <ellipse cx="0" cy="-5" rx="7" ry="5" fill={GOLD} />
      <path d="M5 -7 Q9 -14 6 -17" stroke={GOLD} strokeWidth="3" fill="none" strokeLinecap="round" />
      <circle cx="6" cy="-17" r="2.4" fill={GOLD} />
      <path d="M8 -17 L11 -16.5 L8 -16Z" fill="#E2703A" />
      <path d="M-2 0 V2 M2 0 V2" stroke="#E2703A" strokeWidth="1.2" />
    </g>
  );
}

/** Borne et panneau de gare : le voyage du Chat botté. */
function Halt({ ...p }: P) {
  return (
    <g transform={at(p)}>
      <path d="M-14 0 H14" stroke={BEAM} strokeWidth="1.4" />
      <path d="M-12 0 V2 M-6 0 V2 M0 0 V2 M6 0 V2 M12 0 V2" stroke={WOOD} strokeWidth="1.6" />
      <rect x="-1" y="-16" width="2" height="16" fill={WOOD} />
      <rect x="-8" y="-20" width="16" height="6" rx="1" fill={PLASTER} stroke={BEAM} strokeWidth="0.7" />
      <path d="M-5 -17 H5" stroke={BEAM} strokeWidth="1" />
    </g>
  );
}

/** Montagne creuse du Kyffhäuser : la grotte de l'empereur et ses corbeaux. */
function Cave({ calm = false, ...p }: P & { calm?: boolean }) {
  return (
    <g transform={at(p)}>
      <path d="M-24 0 L-8 -28 L4 -16 L12 -24 L26 0Z" fill="#6E7468" />
      <path d="M-7 0 V-8 Q0 -16 7 -8 V0Z" fill="#2A2420" />
      <circle cx="0" cy="-5" r="2" fill={calm ? GOLD : RED} />
      {!calm && <g fill="#1F1A1A"><path d="M-14 -32 l4 -2 l4 2 l-4 1Z" /><path d="M10 -34 l4 -2 l4 2 l-4 1Z" /><path d="M0 -40 l3 -2 l3 2 l-3 1Z" /></g>}
    </g>
  );
}

/** Barque de pêcheur sur une mer qui s'assombrit à chaque vœu. */
function FisherBoat({ calm = false, ...p }: P & { calm?: boolean }) {
  return (
    <g transform={at(p)}>
      <path d="M-22 2 q5.5 -5 11 0 q5.5 5 11 0 q5.5 -5 11 0 q5.5 5 11 0" fill="none" stroke={calm ? '#7FC4D8' : '#2A3A4A'} strokeWidth="2.4" />
      <path d="M-10 -2 H10 L7 4 H-7Z" fill={WOOD} />
      <path d="M0 -2 V-18" stroke={BEAM} strokeWidth="1.2" />
      <path d="M0 -17 L9 -6 H0Z" fill={PLASTER} />
    </g>
  );
}

/** Pupitre de savant : livre ouvert, plume et bougie. */
function Desk({ ...p }: P) {
  return (
    <g transform={at(p)}>
      <rect x="-12" y="-8" width="24" height="3" fill={WOOD} />
      <path d="M-10 -5 V0 M10 -5 V0" stroke={WOOD} strokeWidth="2" />
      <path d="M-8 -9 Q-4 -13 0 -9 Q4 -13 8 -9 V-11 Q4 -15 0 -11 Q-4 -15 -8 -11Z" fill={PLASTER} stroke={BEAM} strokeWidth="0.6" />
      <rect x="9" y="-14" width="2" height="6" fill={PLASTER} /><path d="M10 -18 q2 2 0 4 q-2 -2 0 -4Z" fill={GOLD} />
    </g>
  );
}

/** Rocher de la Lorelei au-dessus du Rhin. */
function LoreleiRock({ calm = false, ...p }: P & { calm?: boolean }) {
  return (
    <g transform={at(p)}>
      <path d="M-14 0 L-10 -22 L-2 -30 L8 -26 L14 0Z" fill="#7E8A7A" />
      <path d="M-10 -22 L-2 -30 L0 -18Z" fill="#6A7668" />
      <circle cx="0" cy="-34" r="2.6" fill="#E8C8A8" />
      <path d="M-2.6 -34 Q-6 -26 -3 -22" stroke={GOLD} strokeWidth="2.2" fill="none" strokeLinecap="round" />
      {!calm && <g fill={BEAM}><circle cx="12" cy="-36" r="1.4" /><rect x="13" y="-42" width="0.8" height="6" /><circle cx="18" cy="-32" r="1.4" /><rect x="19" y="-38" width="0.8" height="6" /></g>}
    </g>
  );
}

/** Le boulet de canon du Baron, lancé au-dessus des toits. */
function Cannonball({ ...p }: P) {
  return (
    <g transform={at(p)}>
      <path d="M-16 6 Q-2 -14 12 -12" stroke={SNOW} strokeWidth="1.6" fill="none" strokeDasharray="2 3" opacity="0.8" />
      <circle cx="12" cy="-12" r="5" fill="#3A3A3A" />
      <circle cx="10.5" cy="-13.5" r="1.4" fill="#7A7A7A" />
    </g>
  );
}

/** Feu de la nuit de Walpurgis au sommet du Brocken. */
function Bonfire({ ...p }: P) {
  return (
    <g transform={at(p)}>
      <path d="M-22 0 L0 -20 L22 0Z" fill="#6E7468" />
      <path d="M-6 -16 L6 -20 M-6 -20 L6 -16" stroke={WOOD} strokeWidth="2.2" strokeLinecap="round" />
      <path d="M0 -36 Q8 -26 4 -19 H-4 Q-8 -26 0 -36Z" fill="#E2703A" />
      <path d="M0 -28 Q3 -24 2 -19 H-2 Q-3 -24 0 -28Z" fill={GOLD} />
    </g>
  );
}

/** Saule gris au bord du chemin : le Roi des Aulnes n'est plus qu'un arbre une fois la ballade rentrée. */
function Willow({ calm = false, ...p }: P & { calm?: boolean }) {
  return (
    <g transform={at(p)}>
      <path d="M-1.5 0 Q-3 -10 0 -20 Q3 -10 1.5 0Z" fill={WOOD} />
      <path d="M0 -22 Q-16 -24 -15 -4 M0 -22 Q-9 -22 -9 -2 M0 -22 Q9 -22 9 -2 M0 -22 Q16 -24 15 -4 M0 -22 Q-3 -20 -3 -6 M0 -22 Q3 -20 3 -6" stroke={calm ? '#7FA06A' : '#6E7C78'} strokeWidth="2" fill="none" strokeLinecap="round" />
      {!calm && <path d="M-26 -10 q6 -5 12 0 t12 0 M14 -16 q6 -5 12 0" stroke={SNOW} strokeWidth="1.6" fill="none" opacity="0.7" strokeLinecap="round" />}
    </g>
  );
}

/** Seaux et flaque de l'Apprenti sorcier (l'eau se retire quand le balai s'arrête). */
function Buckets({ calm = false, ...p }: P & { calm?: boolean }) {
  return (
    <g transform={at(p)}>
      {!calm && <ellipse cx="0" cy="1" rx="20" ry="3.4" fill="#7FC4D8" opacity="0.85" />}
      <path d="M-12 -10 H-4 L-5.5 0 H-10.5Z" fill={WOOD} stroke={BEAM} strokeWidth="0.8" />
      <path d="M-12 -10 Q-8 -17 -4 -10" stroke={BEAM} strokeWidth="1" fill="none" />
      <path d="M4 -8 H12 L10.5 0 H5.5Z" fill={WOOD} stroke={BEAM} strokeWidth="0.8" />
      {!calm && <path d="M5 -8 H11 V-7 H5Z" fill="#7FC4D8" />}
    </g>
  );
}

/** Falaise et tourbillon du Plongeur. */
function Whirlpool({ calm = false, ...p }: P & { calm?: boolean }) {
  return (
    <g transform={at(p)}>
      <path d="M-26 0 L-24 -26 L-12 -30 L-8 0Z" fill="#7E8A7A" />
      <path d="M-24 -26 L-12 -30 L-14 -14Z" fill="#6A7668" />
      <ellipse cx="10" cy="-2" rx="16" ry="5" fill={calm ? '#7FC4D8' : '#2A4A5A'} />
      {!calm && <path d="M0 -2 q10 -6 18 0 q-8 5 -13 0 q4 -3 8 0" stroke={SNOW} strokeWidth="1.2" fill="none" opacity="0.85" />}
      {calm && <path d="M7 -6 h6 l-1.4 4 h-3.2Z M10 -2 v2.4 M8 0.6 h4" stroke={GOLD} strokeWidth="1.2" fill={GOLD} />}
    </g>
  );
}

/** Arène à arcades du Gant. */
function Arena({ ...p }: P) {
  return (
    <g transform={at(p)}>
      <path d="M-22 0 V-16 Q0 -24 22 -16 V0Z" fill={STONE} />
      <path d="M-17 0 V-8 a3.5 3.5 0 0 1 7 0 V0Z M-7 0 V-9 a3.5 3.5 0 0 1 7 0 V0Z M3 0 V-9 a3.5 3.5 0 0 1 7 0 V0Z M13 0 V-8 a3 3 0 0 1 6 0 V0Z" fill="#4A4038" />
      <path d="M-22 -16 Q0 -24 22 -16" stroke={BEAM} strokeWidth="1.2" fill="none" />
      <path d="M0 -21 V-30 M0 -30 L7 -27.5 L0 -25Z" stroke={BEAM} strokeWidth="1" fill={RED} />
    </g>
  );
}

/** Gradins du théâtre et vol de grues. */
function Amphitheatre({ calm = false, ...p }: P & { calm?: boolean }) {
  return (
    <g transform={at(p)}>
      <path d="M-22 0 Q0 -8 22 0Z" fill={STONE} />
      <path d="M-20 -3 Q0 -12 20 -3 M-17 -7 Q0 -16 17 -7 M-13 -11 Q0 -19 13 -11" stroke="#8A8478" strokeWidth="2.4" fill="none" />
      <g stroke={calm ? '#B8B4A8' : '#3A3A3A'} strokeWidth="1.4" fill="none" strokeLinecap="round" opacity={calm ? 0.7 : 1}>
        <path d="M-12 -30 l4 3 l4 -3" /><path d="M0 -35 l4 3 l4 -3" /><path d="M12 -29 l4 3 l4 -3" />
      </g>
    </g>
  );
}

/** Cor de chasse du Chasseur sauvage, suspendu à une branche. */
function HuntingHorn({ ...p }: P) {
  return (
    <g transform={at(p)}>
      <path d="M-8 -6 Q-10 -18 2 -18 Q12 -18 10 -8" stroke={GOLD} strokeWidth="3" fill="none" strokeLinecap="round" />
      <path d="M10 -8 L14 -2 L5 -3Z" fill={GOLD} />
      <path d="M-8 -6 v-3" stroke={BEAM} strokeWidth="1.6" />
      <path d="M-4 -18 Q0 -26 6 -18" stroke={RED} strokeWidth="1" fill="none" />
    </g>
  );
}

/** Lac de l'Ondine : roseaux et nénuphar. */
function Lake({ calm = false, ...p }: P & { calm?: boolean }) {
  return (
    <g transform={at(p)}>
      <ellipse cx="0" cy="-1" rx="22" ry="5.5" fill={calm ? '#7FC4D8' : '#3F6A8A'} />
      <path d="M-18 -2 V-14 M-15 -2 V-11 M17 -2 V-13" stroke={FIR} strokeWidth="1.2" />
      <path d="M-18 -14 v-4 M-15 -11 v-3 M17 -13 v-4" stroke={WOOD} strokeWidth="2.2" strokeLinecap="round" />
      <ellipse cx="4" cy="-1" rx="5" ry="1.8" fill="#4F8A5A" />
      <path d="M4 -2 q-2 -4 0 -5 q2 1 0 5Z M4 -2 q-4 -2 -4 -4 q3 0 4 4Z M4 -2 q4 -2 4 -4 q-3 0 -4 4Z" fill="#F4C8D8" />
      {!calm && <path d="M-8 -4 q2 -2 4 0 M10 -5 q2 -2 4 0" stroke={SNOW} strokeWidth="1" fill="none" opacity="0.8" />}
    </g>
  );
}

/** Bibliothèque de Weimar : façade claire, fronton et coupole. */
function Library({ ...p }: P) {
  return (
    <g transform={at(p)}>
      <rect x="-18" y="-16" width="36" height="16" fill={PLASTER} stroke={BEAM} strokeWidth="0.8" />
      <path d="M-20 -16 H20 L0 -25Z" fill={STONE} />
      <path d="M-6 -24 Q0 -34 6 -24Z" fill="#6A8A9A" />
      <path d="M0 -31 v-4" stroke={GOLD} strokeWidth="1.2" />
      <path d="M-13 -13 V0 M-7 -13 V0 M7 -13 V0 M13 -13 V0" stroke={STONE} strokeWidth="2.2" />
      <path d="M-2.5 0 V-8 a2.5 2.5 0 0 1 5 0 V0Z" fill={WOOD} />
    </g>
  );
}

export const GERMAN_SCENES: Record<string, (calm: boolean) => ReactNode> = {
  // Hanau : la maison natale des Grimm et le feu du Rumpelstilzchen
  'goethea1-w1': (calm) => (<><TimberHouse x={-12} y={12} /><Campfire x={12} y={14} calm={calm} /><Fir x={28} y={12} s={0.7} /></>),
  // Steinau : la maison d'enfance et les sept petits lits
  'goethea1-w2': () => (<><TimberHouse x={-14} y={12} s={1.05} /><DwarfBeds x={14} y={14} /><Fir x={34} y={12} s={0.6} /></>),
  // Marbourg : ruelles en pente et carrefour du Loup
  'goethea1-w3': () => (<><TimberHouse x={-18} y={10} s={0.8} /><TimberHouse x={-2} y={14} s={0.95} /><Signpost x={18} y={14} /><Fir x={30} y={12} s={0.7} /></>),
  // Cassel : la maison de pain d'épices dans la forêt
  'goethea1-w4': () => (<><Fir x={-24} y={12} s={0.8} /><GingerbreadHouse x={-2} y={13} /><Fir x={22} y={12} /></>),
  // Sababurg : le château sous les ronces
  'goethea1-w5': (calm) => (<><BriarCastle x={-2} y={13} calm={calm} /><Fir x={30} y={12} s={0.6} /></>),
  // Göttingen : le marché du Tailleur
  'goethea1-w6': () => (<><ClothStall x={-12} y={13} /><ClothStall x={12} y={13} s={0.85} /><TimberHouse x={32} y={11} s={0.6} /></>),
  // Le Meissner : la montagne de Dame Holle
  'goethea1-w7': (calm) => (<><HolleMountain x={-4} y={13} calm={calm} /><Fir x={-28} y={12} s={0.6} /></>),
  // Hamelin : la porte de la ville et la flûte
  'goethea1-w8': (calm) => (<><TownGate x={-12} y={13} /><TimberHouse x={8} y={13} s={0.8} />{!calm && <PipeNotes x={26} y={10} />}</>),
  // Brême : les quatre Musiciens devant l'hôtel de ville
  'goethea1-final': () => (<><BremenHall x={-10} y={13} /><Musicians x={20} y={14} /></>),
  // ───── Goethe A2 : du Rhin à la Forêt-Noire ─────
  // Le puits du Roi Grenouille (la balle d'or en ressort une fois le conte apaisé)
  'goethea2-w1': (calm) => (<><Well x={-4} y={13} calm={calm} /><Fir x={-26} y={12} s={0.8} /><Fir x={24} y={12} s={0.7} /></>),
  // La maison de Cendrillon et le château du bal
  'goethea2-w2': () => (<><TimberHouse x={-16} y={13} s={0.9} /><Castle x={16} y={12} s={0.8} /></>),
  // La tour de Raiponce dans la forêt
  'goethea2-w3': (calm) => (<><Fir x={-24} y={12} /><Tower x={0} y={14} calm={calm} /><Fir x={22} y={12} s={0.8} /></>),
  // Le château de la Reine et son miroir
  'goethea2-w4': () => (<><Castle x={-10} y={13} /><Mirror x={22} y={14} s={0.9} /></>),
  // Le chemin de Jean le Chanceux : le puits au bord de la route
  'goethea2-w5': (calm) => (<><Signpost x={-18} y={14} /><Well x={8} y={13} calm={!calm} /><Fir x={30} y={12} s={0.6} /></>),
  // La halte et l'auberge du Chat botté
  'goethea2-w6': () => (<><Halt x={-14} y={14} /><TimberHouse x={14} y={13} s={0.9} /></>),
  // L'auberge de l'Oie d'or
  'goethea2-w7': () => (<><TimberHouse x={-12} y={13} /><Goose x={14} y={14} /><Fir x={30} y={12} s={0.6} /></>),
  // Le château du Roi Barbe-de-Grive
  'goethea2-w8': () => (<><Castle x={-4} y={13} s={1.1} /><ClothStall x={26} y={13} s={0.6} /></>),
  // Le festin des contes
  'goethea2-final': () => (<><Castle x={-12} y={13} /><Goose x={14} y={14} s={0.8} /><Mirror x={28} y={14} s={0.6} /></>),
  // ───── Goethe B1 : le pays des légendes ─────
  // Le Kyffhäuser : la grotte de Barberousse (les corbeaux s'en vont quand l'empereur a écouté)
  'goetheb1-w1': (calm) => (<><Cave x={-2} y={13} calm={calm} /><Fir x={30} y={12} s={0.6} /></>),
  // Les monts des Géants de Rübezahl
  'goetheb1-w2': (calm) => (<><HolleMountain x={-6} y={13} calm={calm} /><Fir x={-30} y={12} s={0.6} /><Signpost x={26} y={14} s={0.8} /></>),
  // La cabane du Pêcheur et la mer
  'goetheb1-w3': (calm) => (<><TimberHouse x={-16} y={12} s={0.75} /><FisherBoat x={14} y={12} calm={calm} /></>),
  // Cologne : les ateliers et la cathédrale
  'goetheb1-w4': () => (<><TimberHouse x={-18} y={13} s={0.85} /><Tower x={2} y={14} s={0.9} /><Tower x={12} y={14} s={0.9} /><ClothStall x={30} y={13} s={0.6} /></>),
  // Le cabinet du Docteur Faust
  'goetheb1-w5': () => (<><TimberHouse x={-14} y={13} /><Desk x={14} y={14} /></>),
  // La place du marché de Till l'Espiègle
  'goetheb1-w6': () => (<><ClothStall x={-14} y={13} /><TownGate x={12} y={13} s={0.9} /></>),
  // Le rocher de la Lorelei
  'goetheb1-w7': (calm) => (<><LoreleiRock x={-8} y={13} calm={calm} /><FisherBoat x={18} y={12} calm s={0.8} /></>),
  // Le manoir du Baron de Münchhausen
  'goetheb1-w8': (calm) => (<><Castle x={-8} y={13} s={0.9} />{!calm && <Cannonball x={20} y={0} />}</>),
  // Le Brocken, nuit de Walpurgis
  'goetheb1-final': () => (<><Bonfire x={0} y={13} /><Fir x={-28} y={12} s={0.7} /><Fir x={28} y={12} s={0.7} /></>),
  // ───── Goethe B2 : Weimar, la cour des poètes ─────
  // La route de nuit du Roi des Aulnes : un saule gris dans le vent
  'goetheb2-w1': (calm) => (<><Willow x={-10} y={13} calm={calm} /><Fir x={22} y={12} s={0.7} /><Signpost x={34} y={14} s={0.7} /></>),
  // L'atelier de l'Apprenti sorcier, inondé
  'goetheb2-w2': (calm) => (<><TimberHouse x={-14} y={12} /><Buckets x={14} y={14} calm={calm} /></>),
  // Le gouffre du Plongeur (la coupe d'or remonte quand la mer se calme)
  'goetheb2-w3': (calm) => (<><Whirlpool x={0} y={13} calm={calm} /></>),
  // L'arène du Gant
  'goetheb2-w4': () => (<><Arena x={0} y={13} /></>),
  // Le théâtre de Corinthe et les Grues d'Ibycus
  'goetheb2-w5': (calm) => (<><Amphitheatre x={0} y={13} calm={calm} /></>),
  // La forêt du Chasseur sauvage
  'goetheb2-w6': () => (<><Fir x={-24} y={12} s={0.9} /><Fir x={-8} y={13} s={0.7} /><HuntingHorn x={12} y={12} /><Fir x={30} y={12} s={0.8} /></>),
  // Le lac de l'Ondine
  'goetheb2-w7': (calm) => (<><Lake x={-2} y={13} calm={calm} /><Fir x={32} y={11} s={0.6} /></>),
  // Le cabinet de Méphisto
  'goetheb2-w8': () => (<><Desk x={-12} y={14} /><TimberHouse x={16} y={13} s={0.85} /></>),
  // La bibliothèque de Weimar
  'goetheb2-final': () => (<><Library x={0} y={13} /><Fir x={-32} y={12} s={0.6} /><Fir x={32} y={12} s={0.6} /></>),
};
