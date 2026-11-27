import type { ReactNode } from 'react';

/**
 * Mode histoire allemand (l'apprenti·e des frères Grimm) : le décor de chaque île raconte son chapitre.
 * Goethe A1, la Route des contes : maisons à colombages de Hanau et Steinau, ruelles de Marbourg, maison de pain d'épices,
 * château de Sababurg sous les ronces, marché de Göttingen, mont de Dame Holle, Hamelin et les Musiciens de Brême.
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
};
