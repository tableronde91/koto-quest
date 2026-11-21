import type { ReactNode } from 'react';
import { motion } from 'motion/react';

/**
 * Mode histoire coréen (TOPIK 1, la Voie du hwarang ; TOPIK 2, le Conteur du tigre blanc ; TOPIK 3, l'Inspecteur royal secret ; TOPIK 4, l'Historien des Annales ; TOPIK 5, le Chant de la princesse Bari ; TOPIK 6, la Légende de Dangun) : le décor de chaque île raconte son chapitre.
 * Palais aux toits relevés et aux couleurs du dancheong, marché de Namdaemun, hanok, temple de montagne,
 * pleine lune de Chuseok, port de Busan, observatoire de Cheomseongdae. Dessins originaux, centrés sur (0, 0).
 */
const GIWA = '#3A3F46';
const GIWA_DARK = '#272B31';
const WALL = '#F4EEDF';
const WOOD = '#7A4E30';
const DARK_WOOD = '#4A3424';
const STONE = '#A39C90';
const STONE_DARK = '#7E776C';
const DAN_GREEN = '#2E8B7A';
const DAN_RED = '#B23A3A';
const DAN_BLUE = '#2F5D8A';
const GOLD = '#E2B84A';

type P = { x: number; y: number; s?: number };
const at = ({ x, y, s = 1 }: P, flip = false) => `translate(${x} ${y}) scale(${flip ? -s : s} ${s})`;

/** Toit de tuiles (giwa) aux extrémités relevées. */
function Roof({ w, h, y = 0, color = GIWA }: { w: number; h: number; y?: number; color?: string }) {
  return (
    <g transform={`translate(0 ${y})`}>
      <path d={`M${-w} 0 Q${-w * 0.78} ${-h * 0.25} ${-w * 0.6} ${-h} H${w * 0.6} Q${w * 0.78} ${-h * 0.25} ${w} 0 Q0 ${-h * 0.42} ${-w} 0Z`} fill={color} />
      <path d={`M${-w * 0.6} ${-h} H${w * 0.6}`} stroke={GIWA_DARK} strokeWidth="1.6" strokeLinecap="round" />
      <path d={`M${-w} 0 Q0 ${-h * 0.42} ${w} 0`} stroke={DAN_GREEN} strokeWidth="1.2" fill="none" opacity={0.9} />
    </g>
  );
}

/** Maison traditionnelle (hanok) : murs blancs à colombages, piliers de bois, toit de tuiles. */
function Hanok({ w = 16, lit = false, ...p }: P & { w?: number; lit?: boolean }) {
  return (
    <g transform={at(p)}>
      <rect x={-w - 2} y="0" width={(w + 2) * 2} height="3" fill={STONE} />
      <rect x={-w + 2} y="-11" width={(w - 2) * 2} height="11" fill={WALL} />
      {[-w + 2, -w / 3, w / 3, w - 3.6].map((px) => <rect key={px} x={px} y="-11" width="1.6" height="11" fill={WOOD} />)}
      <rect x="-3.5" y="-8" width="7" height="8" fill={lit ? '#FFD27A' : '#C9B48E'} stroke={WOOD} strokeWidth="0.8" />
      <path d="M0 -8 V0 M-3.5 -4 H3.5" stroke={WOOD} strokeWidth="0.6" />
      <Roof w={w + 6} h={9} y={-10} />
    </g>
  );
}

/** Porte de palais (Gwanghwamun / Sungnyemun) : socle de pierre percé d'arches, pavillon à double toit. */
function PalaceGate({ arches = 3, ...p }: P & { arches?: number }) {
  const w = arches === 3 ? 26 : 18;
  return (
    <g transform={at(p)}>
      <rect x={-w} y="-14" width={w * 2} height="16" fill={STONE} />
      {[-w, -w / 2, 0, w / 2].map((bx, i) => <path key={i} d={`M${bx} -7 H${bx + w / 2}`} stroke={STONE_DARK} strokeWidth="0.5" />)}
      {(arches === 3 ? [-14, 0, 14] : [0]).map((ax) => (
        <path key={ax} d={`M${ax - 4} 2 V-6 Q${ax} -11 ${ax + 4} -6 V2Z`} fill="#2B2420" />
      ))}
      <rect x={-w * 0.7} y="-21" width={w * 1.4} height="7" fill={DAN_RED} />
      {[-0.55, -0.2, 0.2, 0.55].map((k) => <rect key={k} x={k * w - 0.8} y="-21" width="1.6" height="7" fill={DAN_GREEN} />)}
      <Roof w={w * 0.95} h={8} y={-20} />
      <rect x={-w * 0.5} y="-31" width={w} height="5" fill={DAN_RED} />
      <Roof w={w * 0.75} h={8} y={-30} />
    </g>
  );
}

/** Haetae : lion de pierre gardien des palais. */
function Haetae({ flip = false, ...p }: P & { flip?: boolean }) {
  return (
    <g transform={at(p, flip)}>
      <rect x="-5" y="0" width="10" height="3" fill={STONE_DARK} />
      <path d="M-5 0 Q-6 -7 -2 -9 L3 -9 Q6 -7 5 0Z" fill={STONE} />
      <circle cx="2.5" cy="-11.5" r="4" fill={STONE} />
      <path d="M-1 -14 q3.5 -3 7 0" stroke={STONE_DARK} strokeWidth="1.2" fill="none" />
      <circle cx="3.6" cy="-12.2" r="0.8" fill="#2B2420" />
      <path d="M1 -9.5 q2 1.4 4 0" stroke={STONE_DARK} strokeWidth="0.8" fill="none" />
    </g>
  );
}

/** Statue dorée du roi Sejong, assis, un livre ouvert à la main. */
function KingStatue(p: P) {
  return (
    <g transform={at(p)}>
      <rect x="-11" y="-6" width="22" height="8" fill={STONE} />
      <rect x="-9" y="-9" width="18" height="3" fill={STONE_DARK} />
      <path d="M-8 -9 Q-9 -20 -4 -24 H4 Q9 -20 8 -9Z" fill={GOLD} />
      <circle cx="0" cy="-28" r="4.2" fill={GOLD} />
      <rect x="-4.5" y="-35" width="9" height="3.6" rx="1" fill="#B8902F" />
      <path d="M-5 -16 L0 -14 L5 -16 L5 -12 L0 -10 L-5 -12Z" fill="#FFF6E0" stroke="#B8902F" strokeWidth="0.6" />
    </g>
  );
}

/** Livre ouvert avec deux lettres du hangeul. */
function HangulBook({ left = 'ㄱ', right = 'ㅏ', ...p }: P & { left?: string; right?: string }) {
  return (
    <g transform={at(p)}>
      <path d="M0 -2 Q-7 -6 -14 -3 V-14 Q-7 -17 0 -13Z" fill="#FFF6E0" stroke={DARK_WOOD} strokeWidth="0.9" />
      <path d="M0 -2 Q7 -6 14 -3 V-14 Q7 -17 0 -13Z" fill="#FFF6E0" stroke={DARK_WOOD} strokeWidth="0.9" />
      <text x="-7" y="-8" dy="0.36em" textAnchor="middle" fontSize="7" fontWeight="900" className="jp" fill={DAN_BLUE}>{left}</text>
      <text x="7" y="-8" dy="0.36em" textAnchor="middle" fontSize="7" fontWeight="900" className="jp" fill={DAN_RED}>{right}</text>
    </g>
  );
}

/** Panneau de bois avec une syllabe. */
function Sign({ glyph, tilt = 0, ...p }: P & { glyph: string; tilt?: number }) {
  return (
    <g transform={`${at(p)} rotate(${tilt})`}>
      <rect x="-0.8" y="-4" width="1.6" height="10" fill={DARK_WOOD} />
      <rect x="-6" y="-15" width="12" height="11" rx="1.5" fill="#FFF6E0" stroke={DARK_WOOD} strokeWidth="1" />
      <text y="-9.5" dy="0.36em" textAnchor="middle" fontSize="7.5" fontWeight="900" className="jp" fill={DAN_RED}>{glyph}</text>
    </g>
  );
}

/** Étal du marché sous sa bâche. */
function MarketStall({ color = DAN_BLUE, ...p }: P & { color?: string }) {
  return (
    <g transform={at(p)}>
      <rect x="-10" y="-13" width="1.4" height="15" fill={DARK_WOOD} />
      <rect x="8.6" y="-13" width="1.4" height="15" fill={DARK_WOOD} />
      <rect x="-10" y="-5" width="20" height="7" fill="#B8865A" />
      {[['#E8772E', -5], ['#C8323F', 0], ['#6FAE4F', 5]].map(([c, cx]) => <circle key={cx} cx={cx} cy="-7" r="2" fill={c as string} />)}
      <path d="M-13 -12 L-10 -19 H10 L13 -12Z" fill={color} />
      <path d="M-13 -12 H13" stroke="#FFFFFF" strokeWidth="1" opacity={0.6} />
    </g>
  );
}

/** Kaki séché suspendu (gotgam), l'effroi du tigre. */
function Persimmons(p: P) {
  return (
    <g transform={at(p)}>
      <path d="M0 -22 V0" stroke={DARK_WOOD} strokeWidth="0.8" />
      {[-18, -12, -6].map((cy) => <ellipse key={cy} cx="0" cy={cy} rx="2.6" ry="2.2" fill="#D9682B" />)}
    </g>
  );
}

/** Tour de Séoul sur sa colline. */
function SeoulTower(p: P) {
  return (
    <g transform={at(p)}>
      <path d="M-16 4 Q0 -10 16 4Z" fill="#4E8B57" />
      <path d="M-1.6 -8 L-1 -40 H1 L1.6 -8Z" fill="#E9E4DA" />
      <ellipse cx="0" cy="-34" rx="5" ry="2.6" fill="#D7D0C4" />
      <ellipse cx="0" cy="-34" rx="5" ry="1" fill={DAN_BLUE} />
      <path d="M0 -40 V-48" stroke="#C8323F" strokeWidth="1.2" />
    </g>
  );
}

/** Puits de pierre. */
function Well(p: P) {
  return (
    <g transform={at(p)}>
      <ellipse cx="0" cy="0" rx="7" ry="2.6" fill={STONE_DARK} />
      <rect x="-7" y="-6" width="14" height="6" fill={STONE} />
      <ellipse cx="0" cy="-6" rx="7" ry="2.6" fill="#2F4A66" stroke={STONE_DARK} strokeWidth="1" />
      <path d="M-6 -6 V-15 M6 -6 V-15 M-8 -15 H8" stroke={DARK_WOOD} strokeWidth="1.4" />
    </g>
  );
}

/** Jarres de terre (onggi) sur leur terrasse. */
function Onggi(p: P) {
  return (
    <g transform={at(p)}>
      <rect x="-12" y="0" width="24" height="2.4" fill={STONE} />
      {[[-7, 1], [0, 1.25], [7, 0.9]].map(([cx, k]) => (
        <g key={cx} transform={`translate(${cx} 0) scale(${k})`}>
          <path d="M-4 0 Q-6 -5 -3 -8 H3 Q6 -5 4 0Z" fill="#6B3E26" />
          <rect x="-3.2" y="-9.5" width="6.4" height="1.6" rx="0.8" fill="#4A2A19" />
        </g>
      ))}
    </g>
  );
}

/** Montagne verte aux crêtes de rocher (Seoraksan). */
function Mountain({ w, h, ...p }: P & { w: number; h: number }) {
  return (
    <g transform={at(p)}>
      <path d={`M${-w} 0 L${-w * 0.35} ${-h * 0.7} L${-w * 0.1} ${-h * 0.55} L${w * 0.15} ${-h} L${w} 0Z`} fill="#4E7A55" />
      <path d={`M${w * 0.15} ${-h} L${w * 0.32} ${-h * 0.62} L${w * 0.05} ${-h * 0.7}Z`} fill="#C9C2B6" />
      <path d={`M${-w * 0.35} ${-h * 0.7} L${-w * 0.2} ${-h * 0.45} L${-w * 0.42} ${-h * 0.5}Z`} fill="#C9C2B6" />
    </g>
  );
}

/** Cloche de bronze sous son pavillon. */
function BellPavilion({ calm, ...p }: P & { calm: boolean }) {
  return (
    <g transform={at(p)}>
      <rect x="-12" y="0" width="24" height="2.6" fill={STONE} />
      {[-10, 8.4].map((px) => <rect key={px} x={px} y="-17" width="1.6" height="17" fill={DAN_RED} />)}
      <motion.g style={{ originX: '0px', originY: '-16px' }} animate={calm ? undefined : { rotate: [-5, 5, -5] }} transition={{ duration: 3, repeat: Infinity, ease: 'easeInOut' }}>
        <path d="M0 -16 V-13" stroke={DARK_WOOD} strokeWidth="0.8" />
        <path d="M-4.5 -2 Q-5 -11 0 -13 Q5 -11 4.5 -2Z" fill="#8C6A3F" />
        <rect x="-5" y="-3" width="10" height="1.6" rx="0.8" fill="#6E5230" />
      </motion.g>
      <Roof w={17} h={7} y={-16} />
    </g>
  );
}

/** Pleine lune de Chuseok, au-dessus d'un plateau de songpyeon. */
function FullMoon({ calm, ...p }: P & { calm: boolean }) {
  return (
    <g transform={at(p)}>
      <motion.circle r="14" fill="#FFE9A8" opacity={0.25} animate={calm ? undefined : { r: [13, 16, 13] }} transition={{ duration: 4, repeat: Infinity, ease: 'easeInOut' }} />
      <circle r="9" fill="#FFF3C4" />
      <circle cx="-2.5" cy="-1.5" r="1.8" fill="#EADBA0" />
      <circle cx="3" cy="2.5" r="1.2" fill="#EADBA0" />
    </g>
  );
}

function Songpyeon(p: P) {
  return (
    <g transform={at(p)}>
      <ellipse cx="0" cy="0" rx="10" ry="3" fill={WOOD} />
      {[['#F6E7C9', -5], ['#B9D8A5', 0], ['#F2B6C6', 5], ['#F6E7C9', -2.5], ['#B9D8A5', 2.5]].map(([c, cx], i) => (
        <path key={i} d={`M${(cx as number) - 2.6} ${i > 2 ? -3.6 : -1.4} q2.6 -3.4 5.2 0Z`} fill={c as string} />
      ))}
    </g>
  );
}

/** Phare rouge du port de Busan. */
function Lighthouse({ calm, ...p }: P & { calm: boolean }) {
  return (
    <g transform={at(p)}>
      <path d="M-4 2 L-2.6 -22 H2.6 L4 2Z" fill="#D9483B" />
      {[-15, -8].map((sy) => <rect key={sy} x="-3.4" y={sy} width="6.8" height="2" fill="#FFFFFF" />)}
      <rect x="-3.6" y="-27" width="7.2" height="5" fill="#2F3B4A" />
      <motion.circle cy="-24.5" r="2" fill="#FFD27A" animate={calm ? undefined : { opacity: [1, 0.3, 1] }} transition={{ duration: 2, repeat: Infinity }} />
      <path d="M-4.5 -27 L0 -31 L4.5 -27Z" fill="#D9483B" />
    </g>
  );
}

/** Dragon de la mer de l'Est qui ondule entre les vagues. */
function SeaDragon({ calm, ...p }: P & { calm: boolean }) {
  return (
    <motion.g transform={at(p)} animate={calm ? undefined : { y: [0, -2, 0] }} transition={{ duration: 3, repeat: Infinity, ease: 'easeInOut' }}>
      <path d="M-22 4 Q-16 -8 -9 2 Q-2 12 4 0 Q8 -9 13 -6" stroke="#2E8B7A" strokeWidth="4.5" fill="none" strokeLinecap="round" />
      <path d="M-22 4 Q-16 -8 -9 2 Q-2 12 4 0 Q8 -9 13 -6" stroke={GOLD} strokeWidth="1" strokeDasharray="1.5 2.5" fill="none" />
      <path d="M11 -9 Q18 -12 20 -6 Q16 -3 12 -4Z" fill="#2E8B7A" />
      <circle cx="16.5" cy="-7.8" r="0.9" fill="#FFF3C4" />
      <path d="M17 -11 l3 -4 M14 -11 l1 -5" stroke={GOLD} strokeWidth="0.9" strokeLinecap="round" />
      <path d="M20 -6 q4 1 6 4" stroke={GOLD} strokeWidth="0.7" fill="none" />
    </motion.g>
  );
}

function Waves({ y = 0, w = 30 }: { y?: number; w?: number }) {
  return <path d={`M${-w} ${y} q5 -4 10 0 t10 0 t10 0 t10 0 t10 0 t10 0`} stroke="#FFFFFF" strokeWidth="1.4" fill="none" opacity={0.8} />;
}

/** Cheomseongdae : l'observatoire des étoiles de Silla, tour de pierre en forme de bouteille. */
function Cheomseongdae({ calm, ...p }: P & { calm: boolean }) {
  return (
    <g transform={at(p)}>
      <rect x="-12" y="0" width="24" height="3" fill={STONE_DARK} />
      <path d="M-10 0 Q-11 -14 -6 -26 Q-5 -32 -5 -36 H5 Q5 -32 6 -26 Q11 -14 10 0Z" fill="#CDBFA4" />
      {[-6, -12, -18, -24, -30].map((ly) => <path key={ly} d={`M-10 ${ly} H10`} stroke="#A8987A" strokeWidth="0.6" />)}
      <rect x="-2.4" y="-19" width="4.8" height="4.8" fill="#3B2F26" />
      <rect x="-6.5" y="-40" width="13" height="4" fill="#B6A685" />
      {[[-16, -44], [14, -48], [-6, -54], [20, -36]].map(([sx, sy], i) => (
        <motion.circle key={i} cx={sx} cy={sy} r="1.3" fill="#FFF3C4" animate={calm ? undefined : { opacity: [0.3, 1, 0.3] }} transition={{ duration: 2 + i * 0.5, repeat: Infinity }} />
      ))}
    </g>
  );
}

// ───── Décors du TOPIK 2 (le Conteur du tigre blanc) ─────

/** Jangseung : totem de bois du village, chapeau noir et grands yeux ronds. */
function Jangseung({ flip = false, ...p }: P & { flip?: boolean }) {
  return (
    <g transform={at(p, flip)}>
      <rect x="-4" y="-30" width="8" height="30" rx="2" fill="#A8743F" />
      <rect x="-5" y="-38" width="10" height="7" rx="1.5" fill="#1F2433" />
      <ellipse cx="0" cy="-31" rx="7" ry="1.5" fill="#1F2433" />
      <circle cx="-2" cy="-25" r="1.6" fill="#F4EEDF" /><circle cx="2" cy="-25" r="1.6" fill="#F4EEDF" />
      <path d="M-1 -22 L0 -19 L1 -22Z" fill="#7A4E30" />
      <path d="M-2.5 -16 H2.5" stroke="#3B2A1A" strokeWidth="0.8" />
      <path d="M0 -13 V-3" stroke={DAN_RED} strokeWidth="1.2" opacity={0.8} />
    </g>
  );
}

/** Four de potier (deungyo) à flanc de colline, avec une jarre de céladon. */
function Kiln({ calm, ...p }: P & { calm: boolean }) {
  return (
    <g transform={at(p)}>
      <path d="M-24 0 Q-20 -12 -8 -14 Q4 -16 16 -10 Q24 -6 26 0Z" fill="#8C6E4E" />
      {[-16, -6, 4, 14].map((x) => <path key={x} d={`M${x} -1 a3 3 0 0 1 6 0`} fill="#3A2A1C" />)}
      <motion.circle cx="22" cy="-14" r="3" fill="#C9C2B4" animate={calm ? undefined : { cy: [-14, -26], opacity: [0.6, 0] }} transition={{ duration: 3, repeat: Infinity }} />
      <g transform="translate(-30 0)">
        <path d="M-5 0 Q-8 -8 -3 -14 H3 Q8 -8 5 0Z" fill="#8FC4B0" stroke="#5F9A86" strokeWidth="0.6" />
        <rect x="-2.6" y="-16" width="5.2" height="2.2" rx="1" fill="#5F9A86" />
      </g>
    </g>
  );
}

/** Lanterne de lotus (yeondeung) qui flotte sur l'eau. */
function LotusLantern({ calm, color = '#F29BB8', ...p }: P & { calm: boolean; color?: string }) {
  return (
    <motion.g transform={at(p)} animate={calm ? undefined : { y: [0, -1.5, 0] }} transition={{ duration: 3, repeat: Infinity, ease: 'easeInOut' }}>
      <ellipse cx="0" cy="0" rx="7" ry="2" fill="#2E8B7A" opacity={0.7} />
      {[-4, 0, 4].map((x) => <path key={x} d={`M${x - 3} -1 Q${x} -10 ${x + 3} -1Z`} fill={color} stroke="#FFFFFF" strokeWidth="0.4" />)}
      <circle cx="0" cy="-5" r="6" fill="#FFE9A8" opacity={0.3} />
    </motion.g>
  );
}

/** Pie posée sur une branche. */
function Magpie({ flip = false, ...p }: P & { flip?: boolean }) {
  return (
    <g transform={at(p, flip)}>
      <path d="M-14 2 Q0 -2 14 3" stroke={DARK_WOOD} strokeWidth="1.6" fill="none" />
      <ellipse cx="0" cy="-3" rx="5" ry="3.4" fill="#26304A" />
      <ellipse cx="-0.5" cy="-2" rx="2.6" ry="2" fill="#FFFFFF" />
      <circle cx="4" cy="-6" r="2.4" fill="#26304A" />
      <path d="M6 -6.5 L8.5 -6 L6 -5.4Z" fill="#141418" />
      <path d="M-4 -3 L-12 -6 L-11 -3Z" fill="#3B5BA5" />
    </g>
  );
}

/** Pavillon de bibliothèque royale avec des rouleaux et des livres empilés. */
function Library({ label = '규장각', ...p }: P & { label?: string }) {
  return (
    <g transform={at(p)}>
      <rect x="-18" y="0" width="36" height="3" fill={STONE} />
      <rect x="-14" y="-14" width="28" height="14" fill={WALL} />
      {[-9, -3, 3, 9].map((x) => <rect key={x} x={x - 1} y="-14" width="2" height="14" fill={DAN_RED} />)}
      <Roof w={20} h={8} y={-14} />
      <rect x="-5" y="-27" width="10" height="4" fill={DAN_BLUE} /><text x="0" y="-25" dy="0.35em" textAnchor="middle" fontSize="3" fill="#FFFFFF" fontWeight="900">{label}</text>
    </g>
  );
}

function Books(p: P) {
  return (
    <g transform={at(p)}>
      {[[DAN_BLUE, 0], [DAN_GREEN, -3], [DAN_RED, -6], ['#E9D9B0', -9]].map(([c, y], i) => <rect key={i} x={-7 + (i % 2)} y={y as number} width="14" height="3" rx="0.6" fill={c as string} stroke="#3B2F26" strokeWidth="0.3" />)}
      <g transform="translate(12 -2) rotate(-15)"><rect x="-2" y="-8" width="4" height="10" rx="2" fill="#F6EBD3" stroke="#A8987A" strokeWidth="0.4" /><rect x="-2.6" y="-9" width="5.2" height="1.6" rx="0.8" fill={WOOD} /></g>
    </g>
  );
}

/** Dol hareubang : grand-père de pierre de Jeju. */
function Hareubang(p: P) {
  return (
    <g transform={at(p)}>
      <path d="M-6 0 V-16 Q-6 -20 0 -20 Q6 -20 6 -16 V0Z" fill="#5C5650" />
      <path d="M-6 -20 Q0 -30 6 -20Z" fill="#4A4540" />
      <circle cx="-2.4" cy="-16" r="1.3" fill="#3A3632" /><circle cx="2.4" cy="-16" r="1.3" fill="#3A3632" />
      <ellipse cx="0" cy="-12.5" rx="1.6" ry="2.2" fill="#4A4540" />
      <path d="M-5 -7 H5 M-5 -4 H5" stroke="#4A4540" strokeWidth="1.2" />
    </g>
  );
}

/** Flotteur orange des haenyeo (taewak) sur les vagues. */
function Taewak({ calm, ...p }: P & { calm: boolean }) {
  return (
    <motion.g transform={at(p)} animate={calm ? undefined : { y: [0, -2, 0] }} transition={{ duration: 2.6, repeat: Infinity, ease: 'easeInOut' }}>
      <circle cx="0" cy="-3" r="4.5" fill="#E8772E" stroke="#B85A1F" strokeWidth="0.6" />
      <path d="M-4 -3 H4" stroke="#B85A1F" strokeWidth="0.5" />
      <path d="M0 1 V8" stroke="#3B2F26" strokeWidth="0.6" strokeDasharray="1 1" />
    </motion.g>
  );
}

/** Masque de Hahoe souriant, accroché à un poteau. */
function HahoeMask(p: P) {
  return (
    <g transform={at(p)}>
      <rect x="-1" y="-6" width="2" height="22" fill={WOOD} />
      <ellipse cx="0" cy="-12" rx="8" ry="10" fill="#E9D3A8" stroke="#B8935A" strokeWidth="0.8" />
      <path d="M-5 -14 q2.5 -3 5 0 M0 -14 q2.5 -3 5 0" stroke="#3B2F26" strokeWidth="1" fill="none" transform="translate(-0.5 0)" />
      <path d="M-4 -8 Q0 -4 4 -8" stroke="#3B2F26" strokeWidth="1.2" fill="none" />
      <path d="M-4 -5 Q0 0 4 -5" fill="#D9BE8C" stroke="#B8935A" strokeWidth="0.5" />
    </g>
  );
}

/** Danseur masqué en robe ample, manches qui volent. */
function Dancer({ calm, color = DAN_BLUE, ...p }: P & { calm: boolean; color?: string }) {
  return (
    <motion.g transform={at(p)} animate={calm ? undefined : { rotate: [-6, 6, -6] }} transition={{ duration: 2.4, repeat: Infinity, ease: 'easeInOut' }}>
      <path d="M-6 0 L-3 -14 H3 L6 0Z" fill={color} />
      <path d="M-3 -12 Q-12 -16 -14 -8 M3 -12 Q12 -16 14 -8" stroke="#F4EEDF" strokeWidth="2.4" fill="none" strokeLinecap="round" />
      <circle cx="0" cy="-17" r="3.4" fill="#E9D3A8" />
      <path d="M-1.6 -17 q0.8 -1 1.6 0 M0 -17 q0.8 -1 1.6 0" stroke="#3B2F26" strokeWidth="0.5" fill="none" />
    </motion.g>
  );
}

/** Table basse de Seollal : bol de tteokguk et enveloppe d'argent de poche. */
function SeollalTable(p: P) {
  return (
    <g transform={at(p)}>
      <rect x="-14" y="-4" width="28" height="3" rx="1" fill="#8A3A2A" />
      <path d="M-12 -1 V4 M12 -1 V4" stroke="#6A2A1E" strokeWidth="1.6" />
      <path d="M-9 -4 Q-9 -9 -4 -9 Q1 -9 1 -4Z" fill="#F4EEDF" stroke="#2F5D8A" strokeWidth="0.6" />
      <ellipse cx="-4" cy="-8.4" rx="4" ry="1" fill="#FFF8E6" />
      <rect x="4" y="-8" width="7" height="4" rx="0.6" fill="#D9483B" /><path d="M4 -8 L7.5 -5.6 L11 -8" stroke={GOLD} strokeWidth="0.5" fill="none" />
    </g>
  );
}

/** Phénix en vol au-dessus de la cour. */
function Phoenix({ calm, ...p }: P & { calm: boolean }) {
  return (
    <motion.g transform={at(p)} animate={calm ? undefined : { y: [0, -3, 0] }} transition={{ duration: 3.4, repeat: Infinity, ease: 'easeInOut' }}>
      {[-30, -10, 10].map((a, i) => <path key={a} d="M0 0 Q14 6 22 18 Q10 10 0 4Z" fill={[DAN_GREEN, GOLD, DAN_BLUE][i]} transform={`rotate(${a})`} />)}
      <path d="M-12 -2 Q-4 -10 6 -4 Q-2 -6 -12 -2Z" fill="#D9483B" />
      <path d="M-14 -6 Q-10 -12 -6 -8" stroke={GOLD} strokeWidth="1.2" fill="none" />
      <circle cx="-8" cy="-4" r="2.6" fill="#D9483B" /><path d="M-10.6 -4 L-13 -3 L-10.6 -2.6Z" fill={GOLD} />
    </motion.g>
  );
}

/** Porte de la forteresse de Hwaseong : arche de pierre, créneaux et pavillon. */
function FortressGate(p: P) {
  return (
    <g transform={at(p)}>
      <path d="M-34 0 V-12 H34 V0Z" fill="#B8AE9C" />
      {[-34, -26, -18, 18, 26].map((x) => <rect key={x} x={x} y="-15" width="5" height="3" fill="#B8AE9C" />)}
      {[-6, -2].map((y) => <path key={y} d={`M-34 ${y} H34`} stroke={STONE_DARK} strokeWidth="0.4" />)}
      <path d="M-7 0 V-6 Q0 -13 7 -6 V0Z" fill="#3B2F26" />
      <rect x="-12" y="-22" width="24" height="10" fill={WALL} />
      {[-8, -3, 2, 7].map((x) => <rect key={x} x={x} y="-22" width="1.6" height="10" fill={DAN_RED} />)}
      <Roof w={17} h={7} y={-22} />
    </g>
  );
}

/** Tigre blanc couché sur le rempart. */
function WhiteTiger({ calm, ...p }: P & { calm: boolean }) {
  return (
    <g transform={at(p)}>
      <ellipse cx="0" cy="-4" rx="11" ry="4.5" fill="#F4F1EA" stroke="#C9C2B4" strokeWidth="0.5" />
      {[-5, -1, 3].map((x) => <path key={x} d={`M${x} -8 l1 4`} stroke="#1F2433" strokeWidth="1" strokeLinecap="round" />)}
      <circle cx="10" cy="-8" r="4" fill="#F4F1EA" stroke="#C9C2B4" strokeWidth="0.5" />
      <circle cx="8" cy="-11.5" r="1.4" fill="#F4F1EA" stroke="#C9C2B4" strokeWidth="0.4" /><circle cx="12" cy="-11.5" r="1.4" fill="#F4F1EA" stroke="#C9C2B4" strokeWidth="0.4" />
      <motion.g animate={calm ? undefined : { scaleY: [1, 0.1, 1] }} transition={{ duration: 4, repeat: Infinity, times: [0, 0.05, 0.1] }} style={{ transformOrigin: '10px -8.6px' }}>
        <circle cx="8.8" cy="-8.6" r="0.7" fill="#2F5D8A" /><circle cx="11.2" cy="-8.6" r="0.7" fill="#2F5D8A" />
      </motion.g>
      <path d="M-11 -4 Q-18 -8 -16 -14" stroke="#F4F1EA" strokeWidth="2" fill="none" strokeLinecap="round" />
    </g>
  );
}

// ───── Décors du TOPIK 3 (l'Inspecteur royal secret) ─────

/** Bosquet de bambous. */
function Bamboo({ calm, ...p }: P & { calm: boolean }) {
  return (
    <g transform={at(p)}>
      {[-10, -4, 2, 8, 13].map((x, i) => (
        <motion.g key={x} animate={calm ? undefined : { rotate: [-2, 2, -2] }} transition={{ duration: 3 + i * 0.4, repeat: Infinity, ease: 'easeInOut' }} style={{ transformOrigin: `${x}px 0px` }}>
          <rect x={x - 1.2} y={-40 + (i % 2) * 6} width="2.4" height={40 - (i % 2) * 6} fill="#5E9E4A" />
          {[-30, -20, -10].map((y) => <rect key={y} x={x - 1.6} y={y + (i % 2) * 3} width="3.2" height="0.9" fill="#3E7A34" />)}
          <path d={`M${x} ${-38 + (i % 2) * 6} l6 -3 M${x} ${-30 + (i % 2) * 6} l-6 -3`} stroke="#4E8A3E" strokeWidth="1.4" strokeLinecap="round" />
        </motion.g>
      ))}
    </g>
  );
}

/** Grand arbre sacré du village, ceint d'une corde de paille et de rubans. */
function SacredTree(p: P) {
  return (
    <g transform={at(p)}>
      <path d="M-4 0 Q-3 -12 -5 -20 H5 Q3 -12 4 0Z" fill="#7A5A3A" />
      {[[-12, -26, 11], [10, -26, 11], [0, -34, 13], [-4, -22, 9], [6, -20, 9]].map(([x, y, r], i) => <circle key={i} cx={x} cy={y} r={r} fill={i % 2 ? '#4E8A4A' : '#5E9E5A'} />)}
      <path d="M-5 -10 Q0 -8 5 -10" stroke="#D9C38A" strokeWidth="1.6" fill="none" />
      {[-3, 0, 3].map((x, i) => <path key={x} d={`M${x} -9 v5`} stroke={[DAN_RED, DAN_BLUE, GOLD][i]} strokeWidth="1.1" />)}
    </g>
  );
}

/** Tumulus royal de Gyeongju, butte herbeuse. */
function Tumulus({ w = 26, ...p }: P & { w?: number }) {
  return (
    <g transform={at(p)}>
      <path d={`M${-w} 0 Q0 ${-w * 0.9} ${w} 0Z`} fill="#6E9A55" />
      <path d={`M${-w * 0.7} -4 Q0 ${-w * 0.7} ${w * 0.7} -4`} stroke="#5A874A" strokeWidth="0.8" fill="none" />
    </g>
  );
}

/** Cheval céleste en vol, ailes déployées. */
function FlyingHorse({ calm, ...p }: P & { calm: boolean }) {
  return (
    <motion.g transform={at(p)} animate={calm ? undefined : { y: [0, -3, 0] }} transition={{ duration: 3, repeat: Infinity, ease: 'easeInOut' }}>
      <path d="M-10 0 Q-2 -6 8 -2 Q12 0 10 4 Q0 6 -10 3Z" fill="#F6F3EC" stroke="#C9C2B4" strokeWidth="0.5" />
      <path d="M8 -2 Q12 -10 16 -8 Q14 -4 12 -2Z" fill="#F6F3EC" stroke="#C9C2B4" strokeWidth="0.5" />
      <path d="M10 -8 q-3 -4 0 -6 M12 -9 q-2 -4 1 -5" stroke="#E36A3A" strokeWidth="1.2" fill="none" />
      <path d="M-2 -3 Q-6 -16 6 -18 Q2 -10 4 -3Z" fill="#E9D9B0" stroke="#C9A24A" strokeWidth="0.6" />
      {[-8, -4, 4, 8].map((x) => <path key={x} d={`M${x} 3 l${x < 0 ? -2 : 2} 6`} stroke="#C9C2B4" strokeWidth="1.2" strokeLinecap="round" />)}
    </motion.g>
  );
}

/** Pavillon de jardin au bord d'un étang (Buyongjeong). */
function GardenPavilion(p: P) {
  return (
    <g transform={at(p)}>
      <ellipse cx="0" cy="4" rx="24" ry="5" fill="#3F95BF" opacity={0.8} />
      {[-8, 8].map((x) => <rect key={x} x={x - 1} y="-10" width="2" height="12" fill={DAN_RED} />)}
      <rect x="-11" y="0" width="22" height="2" fill={WOOD} />
      <Roof w={15} h={7} y={-10} />
      <ellipse cx="-16" cy="4" rx="3" ry="1.2" fill="#E9709A" /><ellipse cx="14" cy="5" rx="3" ry="1.2" fill="#E9709A" />
    </g>
  );
}

/** Cerf aux bois de corail. */
function Deer({ flip = false, ...p }: P & { flip?: boolean }) {
  return (
    <g transform={at(p, flip)}>
      <ellipse cx="0" cy="-8" rx="8" ry="4" fill="#C98A4E" />
      {[-6, -3, 3, 6].map((x) => <rect key={x} x={x - 0.6} y="-5" width="1.2" height="6" fill="#A86E3A" />)}
      <path d="M6 -10 L9 -16" stroke="#C98A4E" strokeWidth="3" strokeLinecap="round" />
      <ellipse cx="10" cy="-17" rx="2.6" ry="2" fill="#C98A4E" />
      <path d="M9 -19 L7 -24 M7 -22 L5 -23 M11 -19 L13 -24 M13 -22 L15 -23" stroke="#E36A5A" strokeWidth="0.9" strokeLinecap="round" />
      {[-3, 1, -1].map((x, i) => <circle key={i} cx={x} cy={-9 + (i % 2)} r="0.8" fill="#F6E7CC" />)}
    </g>
  );
}

/** Barque à fond plat sur le fleuve. */
function Boat({ calm, ...p }: P & { calm: boolean }) {
  return (
    <motion.g transform={at(p)} animate={calm ? undefined : { rotate: [-3, 3, -3] }} transition={{ duration: 3.2, repeat: Infinity, ease: 'easeInOut' }}>
      <path d="M-14 -2 H14 L10 3 H-10Z" fill={WOOD} />
      <path d="M2 -2 V-16" stroke={DARK_WOOD} strokeWidth="1" />
      <path d="M2 -15 Q10 -10 2 -4Z" fill="#F4EEDF" />
    </motion.g>
  );
}

/** Balançoire de la fête de Dano, suspendue à un arbre. */
function Swing({ calm, ...p }: P & { calm: boolean }) {
  return (
    <g transform={at(p)}>
      <path d="M-12 0 V-28 M12 0 V-28 M-14 -28 H14" stroke={WOOD} strokeWidth="2" />
      <motion.g animate={calm ? undefined : { rotate: [-18, 18, -18] }} transition={{ duration: 2.6, repeat: Infinity, ease: 'easeInOut' }} style={{ transformOrigin: '0px -28px' }}>
        <path d="M-3 -28 V-6 M3 -28 V-6" stroke="#D9C38A" strokeWidth="0.8" />
        <rect x="-4" y="-6" width="8" height="1.6" fill={DARK_WOOD} />
        <path d="M-3 -6 L0 -16 L3 -6Z" fill="#F29BB8" /><circle cx="0" cy="-18" r="2.2" fill="#F6E3D6" />
      </motion.g>
    </g>
  );
}

/** Mapae : plaque de bronze aux chevaux des inspecteurs royaux. */
function Mapae({ calm, ...p }: P & { calm: boolean }) {
  return (
    <motion.g transform={at(p)} animate={calm ? undefined : { rotate: [-6, 6, -6] }} transition={{ duration: 2.8, repeat: Infinity, ease: 'easeInOut' }}>
      <path d="M0 -14 V-10" stroke={DAN_RED} strokeWidth="1.2" />
      <circle cx="0" cy="0" r="10" fill="#C9A24A" stroke="#8C6A2A" strokeWidth="1.2" />
      {[-5, 0, 5].map((x) => <path key={x} d={`M${x - 2} 3 l1 -4 h2 l1 -2 l1 2 l-1 4`} stroke="#6B5022" strokeWidth="0.8" fill="none" />)}
    </motion.g>
  );
}

// ───── Décors du TOPIK 4 (l'Historien des Annales, en hiver) ─────

/** Neige posée sur un toit ou un sol : bourrelets blancs. */
function Snow({ w = 18, ...p }: P & { w?: number }) {
  return <g transform={at(p)}>{Array.from({ length: Math.max(2, Math.round(w / 6)) }, (_, i) => <ellipse key={i} cx={-w + i * 6 + 3} cy={0} rx={4.5} ry={1.8} fill="#FFFFFF" />)}</g>;
}

/** Sapin enneigé. */
function SnowPine(p: P) {
  return (
    <g transform={at(p)}>
      <rect x="-1" y="-4" width="2" height="4" fill={DARK_WOOD} />
      {[0, -6, -12].map((y, i) => <g key={y}><path d={`M${-9 + i * 2} ${y - 2} L0 ${y - 12} L${9 - i * 2} ${y - 2}Z`} fill="#2E5E4A" /><path d={`M${-6 + i * 2} ${y - 5} L0 ${y - 12} L${6 - i * 2} ${y - 5}Z`} fill="#FFFFFF" opacity={0.85} /></g>)}
    </g>
  );
}

/** Coffre d'archives (sago) avec rouleaux des Annales. */
function ArchiveChest(p: P) {
  return (
    <g transform={at(p)}>
      <rect x="-10" y="-10" width="20" height="10" rx="1" fill="#8A3A2A" stroke="#5A2418" strokeWidth="0.6" />
      <rect x="-10" y="-13" width="20" height="3" rx="1" fill="#6A2A1E" />
      <rect x="-2" y="-8" width="4" height="4" fill={GOLD} />
      {[-6, 0, 6].map((x) => <rect key={x} x={x - 1.5} y="-19" width="3" height="7" rx="1.5" fill="#F6EBD3" stroke="#A8987A" strokeWidth="0.3" />)}
    </g>
  );
}

/** Souliers (gomusin) alignés devant une porte. */
function Shoes(p: P) {
  return (
    <g transform={at(p)}>
      {[[-6, '#FFFFFF'], [0, '#2F5D8A'], [6, '#FFFFFF']].map(([x, c], i) => <path key={i} d={`M${(x as number) - 3} 0 Q${(x as number) - 3} -3 ${(x as number)} -3 L${(x as number) + 3} -2 L${(x as number) + 3} 0Z`} fill={c as string} stroke="#8E8E8E" strokeWidth="0.4" />)}
    </g>
  );
}

/** Fourneau de cuisine (아궁이) avec marmite fumante. */
function Stove({ calm, ...p }: P & { calm: boolean }) {
  return (
    <g transform={at(p)}>
      <rect x="-12" y="-8" width="24" height="8" rx="1.5" fill="#A8987A" />
      <path d="M-4 0 V-4 Q0 -7 4 -4 V0Z" fill="#3A2A1C" />
      <motion.path d="M-3 -1 Q0 -6 3 -1Z" fill="#F29A3A" animate={calm ? undefined : { scaleY: [1, 1.3, 1] }} transition={{ duration: 0.8, repeat: Infinity }} style={{ transformOrigin: '0px -1px' }} />
      <path d="M-8 -8 Q-8 -14 0 -14 Q8 -14 8 -8Z" fill="#3B3B3B" />
      <motion.path d="M0 -16 q-3 -4 0 -8 q3 -4 0 -8" stroke="#E9E9E9" strokeWidth="1.2" fill="none" animate={calm ? undefined : { opacity: [0.2, 0.9, 0.2] }} transition={{ duration: 2.4, repeat: Infinity }} />
    </g>
  );
}

/** Berceau suspendu sous un cordon de naissance. */
function Cradle(p: P) {
  return (
    <g transform={at(p)}>
      <path d="M-14 -16 Q0 -12 14 -16" stroke="#D9C38A" strokeWidth="1.2" fill="none" />
      {[-8, -2, 4, 10].map((x, i) => <path key={x} d={`M${x} -15 v3`} stroke={i % 2 ? '#2E2E3C' : DAN_RED} strokeWidth="1.2" />)}
      <path d="M-9 -4 Q0 4 9 -4Z" fill={WOOD} />
      <path d="M-6 -4 Q0 -8 6 -4" fill="#F6E3D6" />
      <path d="M0 -14 V-6" stroke={DARK_WOOD} strokeWidth="0.6" />
    </g>
  );
}

/** Rizière craquelée par la sécheresse. */
function DryField(p: P) {
  return (
    <g transform={at(p)}>
      <path d="M-22 0 L-18 -6 H18 L22 0Z" fill="#C9A26A" />
      <path d="M-14 -4 l4 2 l3 -3 l4 3 l3 -2 l5 2 l4 -1" stroke="#8A6A3A" strokeWidth="0.6" fill="none" />
      {[-12, -2, 9].map((x) => <path key={x} d={`M${x} -6 l-1 -4 M${x + 1} -6 l1 -3`} stroke="#B8A25A" strokeWidth="0.8" />)}
    </g>
  );
}

/** Lune en éclipse mordue par l'ombre. */
function Eclipse({ calm, ...p }: P & { calm: boolean }) {
  return (
    <g transform={at(p)}>
      <circle r="10" fill="#F6E7B0" />
      <motion.circle r="9" fill="#14141C" initial={{ cx: -10 }} animate={calm ? undefined : { cx: [-10, 2, -10] }} transition={{ duration: 6, repeat: Infinity, ease: 'easeInOut' }} cx={-4} />
      <circle r="13" fill="none" stroke="#F6E7B0" strokeWidth="0.6" opacity={0.5} />
    </g>
  );
}

/** Coquille d'escargot géante (우렁각시). */
function SnailShell(p: P) {
  return (
    <g transform={at(p)}>
      <circle r="9" fill="#C99A6A" />
      <path d="M0 0 m-7 0 a7 7 0 1 1 7 7 a5 5 0 1 1 -5 -5 a3 3 0 1 1 3 3" stroke="#8A5E3A" strokeWidth="1.2" fill="none" />
      <path d="M-12 8 Q0 12 14 8" stroke="#7FA88A" strokeWidth="3" fill="none" strokeLinecap="round" />
    </g>
  );
}
/** Œuf lumineux (naissance de Jumong ou de Bak Hyeokgeose). */
function GlowEgg({ calm, ...p }: P & { calm: boolean }) {
  return (
    <g transform={at(p)}>
      <motion.ellipse rx="12" ry="14" fill="#FFF3B0" opacity={0.35} animate={calm ? undefined : { opacity: [0.2, 0.5, 0.2] }} transition={{ duration: 3, repeat: Infinity }} />
      <ellipse rx="6" ry="8" fill="#FFFDF2" stroke="#E2B84A" strokeWidth="0.8" />
    </g>
  );
}
/** Entrée de caverne (l'ourse et le tigre). */
function Cave(p: P) {
  return (
    <g transform={at(p)}>
      <path d="M-18 0 Q-16 -20 0 -22 Q16 -20 18 0Z" fill={STONE_DARK} />
      <path d="M-9 0 Q-8 -12 0 -13 Q8 -12 9 0Z" fill="#1F2433" />
    </g>
  );
}
/** Armoise et gousses d'ail. */
function Garlic(p: P) {
  return (
    <g transform={at(p)}>
      <path d="M-6 0 V-10 M-6 -6 l-3 -3 M-6 -4 l3 -3" stroke="#5E8A4A" strokeWidth="1.4" strokeLinecap="round" />
      {[2, 7].map((x) => <path key={x} d={`M${x} 0 Q${x - 3} -3 ${x} -6 Q${x + 3} -3 ${x} 0Z`} fill="#F6F3EC" stroke="#C9C2B4" strokeWidth="0.6" />)}
    </g>
  );
}
/** Grande cloche de bronze (cloche d'Emille). */
function BigBell({ calm, ...p }: P & { calm: boolean }) {
  return (
    <g transform={at(p)}>
      <path d="M-11 0 Q-12 -18 0 -20 Q12 -18 11 0Z" fill="#6E7E5E" />
      <rect x="-12" y="-1" width="24" height="2.5" fill="#4E5E3E" />
      <motion.path d="M15 -14 q4 6 0 12 M-15 -14 q-4 6 0 12" stroke="#A8C4A0" strokeWidth="1.2" fill="none" animate={calm ? undefined : { opacity: [0, 1, 0] }} transition={{ duration: 2.4, repeat: Infinity }} />
    </g>
  );
}
/** Flûte de bambou magique (만파식적). */
function Flute(p: P) {
  return (
    <g transform={at(p)}>
      <rect x="-14" y="-1.5" width="28" height="3" rx="1.5" fill="#7A9A4A" transform="rotate(-18)" />
      {[-8, -3, 2, 7].map((x) => <circle key={x} cx={x} cy={x * -0.32} r="0.7" fill="#3A4A2A" />)}
    </g>
  );
}
/** Arc et flèche (Jumong l'archer). */
function Bow(p: P) {
  return (
    <g transform={at(p)}>
      <path d="M-4 -14 Q8 0 -4 14" stroke={WOOD} strokeWidth="1.8" fill="none" />
      <path d="M-4 -14 V14" stroke="#E9D9B0" strokeWidth="0.6" />
      <path d="M-6 0 H14 M11 -2 L14 0 L11 2" stroke={DARK_WOOD} strokeWidth="1" fill="none" />
    </g>
  );
}
/** Fleur de résurrection (꽃) du jardin des esprits. */
function SpiritFlower({ color = '#C9A6F2', ...p }: P & { color?: string }) {
  return (
    <g transform={at(p)}>
      <path d="M0 0 V-8" stroke="#4E7A55" strokeWidth="1" />
      {[0, 72, 144, 216, 288].map((r) => <ellipse key={r} cy="-3" rx="1.6" ry="3" fill={color} transform={`translate(0 -9) rotate(${r})`} />)}
      <circle cy="-9" r="1.4" fill="#F2D94E" />
    </g>
  );
}

export const KOREAN_SCENES: Record<string, (calm: boolean) => ReactNode> = {
  // Les lettres du roi : statue de Sejong, livre ouvert sur ㄱ et ㅏ, enseignes brouillées par le Dokkaebi.
  'topik1-w1': () => (
    <>
      <KingStatue x={-4} y={10} s={1.1} />
      <HangulBook x={24} y={14} />
      <Sign x={-32} y={8} glyph="ㄱ" tilt={-12} />
      <Sign x={34} y={-6} glyph="ㅏ" tilt={10} />
    </>
  ),
  // Les portes du palais : Gwanghwamun et ses deux haetae.
  'topik1-w2': () => (
    <>
      <PalaceGate x={0} y={10} />
      <Haetae x={-33} y={12} />
      <Haetae x={33} y={12} flip />
    </>
  ),
  // Les visages de Myeongdong : la tour de Séoul au-dessus des enseignes.
  'topik1-w3': () => (
    <>
      <SeoulTower x={14} y={4} />
      <Hanok x={-20} y={14} w={12} lit />
      <Sign x={-36} y={0} glyph="명" tilt={-8} />
      <Sign x={34} y={14} glyph="안" tilt={8} />
    </>
  ),
  // Le marché de Namdaemun : la porte Sungnyemun, les étals et les kakis séchés.
  'topik1-w4': () => (
    <>
      <PalaceGate x={-10} y={4} arches={1} />
      <MarketStall x={20} y={16} />
      <MarketStall x={-26} y={20} color={DAN_RED} />
      <Persimmons x={36} y={0} />
    </>
  ),
  // Le puits du hanok : la maison de Bukchon, le puits et les jarres.
  'topik1-w5': () => (
    <>
      <Hanok x={-6} y={4} w={18} />
      <Well x={26} y={16} />
      <Onggi x={-24} y={20} />
    </>
  ),
  // Les cloches de Seoraksan : montagnes, temple et cloche de bronze.
  'topik1-w6': (calm) => (
    <>
      <Mountain x={-14} y={6} w={28} h={46} />
      <Mountain x={22} y={8} w={20} h={30} />
      <BellPavilion x={10} y={20} calm={calm} />
    </>
  ),
  // La pleine lune de Chuseok : la maison familiale et le plateau de songpyeon.
  'topik1-w7': (calm) => (
    <>
      <FullMoon x={22} y={-30} calm={calm} />
      <Hanok x={-10} y={8} w={16} lit />
      <Songpyeon x={22} y={18} />
    </>
  ),
  // Le dragon de la mer de l'Est : le phare de Busan et le dragon dans les vagues.
  'topik1-w8': (calm) => (
    <>
      <Lighthouse x={-22} y={10} calm={calm} />
      <Waves y={16} w={18} />
      <SeaDragon x={12} y={4} calm={calm} />
    </>
  ),
  // L'épreuve de Cheomseongdae : l'observatoire sous les étoiles.
  'topik1-final': (calm) => (
    <>
      <Cheomseongdae x={0} y={14} s={1.15} calm={calm} />
      <Hanok x={-30} y={18} w={9} />
    </>
  ),
  // ───── TOPIK 2 : le Conteur du tigre blanc ─────
  // Les gardiens du village : deux jangseung devant les toits de Jeonju.
  'topik2-w1': () => (
    <>
      <Hanok x={4} y={2} w={16} />
      <Jangseung x={-26} y={16} />
      <Jangseung x={34} y={16} flip />
    </>
  ),
  // Le four du potier : four en escalier d'Icheon et vase de céladon.
  'topik2-w2': (calm) => (
    <>
      <Kiln x={6} y={14} calm={calm} />
      <Onggi x={28} y={22} />
    </>
  ),
  // La nuit des lanternes : lanternes de lotus sur la rivière, la pie sur sa branche.
  'topik2-w3': (calm) => (
    <>
      <Waves y={16} w={30} />
      <LotusLantern x={-20} y={12} calm={calm} />
      <LotusLantern x={4} y={18} calm={calm} color="#F2C230" />
      <LotusLantern x={26} y={10} calm={calm} color="#E9709A" />
      <Magpie x={-6} y={-16} />
    </>
  ),
  // La bibliothèque du roi : le pavillon Gyujanggak et ses rouleaux.
  'topik2-w4': () => (
    <>
      <Library x={-6} y={12} />
      <Books x={24} y={18} />
    </>
  ),
  // La géante de Jeju : le Hallasan, un dol hareubang et le flotteur des haenyeo.
  'topik2-w5': (calm) => (
    <>
      <Mountain x={6} y={4} w={30} h={34} />
      <Hareubang x={-26} y={18} />
      <Waves y={20} w={18} />
      <Taewak x={24} y={18} calm={calm} />
    </>
  ),
  // La danse des masques : un masque de Hahoe et un danseur.
  'topik2-w6': (calm) => (
    <>
      <Hanok x={18} y={6} w={14} />
      <HahoeMask x={-22} y={8} />
      <Dancer x={0} y={20} calm={calm} />
    </>
  ),
  // Le Nouvel An des ancêtres : maison familiale, table de Seollal et phénix.
  'topik2-w7': (calm) => (
    <>
      <Hanok x={-8} y={6} w={18} lit />
      <SeollalTable x={24} y={20} />
      <Phoenix x={24} y={-22} calm={calm} />
    </>
  ),
  // Les remparts du tigre blanc : la porte de Hwaseong.
  'topik2-w8': (calm) => (
    <>
      <FortressGate x={0} y={16} />
      <WhiteTiger x={20} y={1} calm={calm} />
    </>
  ),
  // La veillée des récits : la porte sous la pleine lune, livres ouverts.
  'topik2-final': (calm) => (
    <>
      <FullMoon x={-22} y={-26} calm={calm} />
      <FortressGate x={4} y={14} s={0.9} />
      <Books x={30} y={22} />
    </>
  ),
  // ───── TOPIK 3 : l'Inspecteur royal secret ─────
  // Les voix du marché : étals de Hanyang et enseigne des rumeurs.
  'topik3-w1': () => (
    <>
      <MarketStall x={-18} y={14} />
      <MarketStall x={16} y={18} color={DAN_RED} />
      <Sign x={34} y={-4} glyph="말" tilt={8} />
    </>
  ),
  // La nuit de Hanyang : ruelle de hanok éclairés sous la lune.
  'topik3-w2': (calm) => (
    <>
      <FullMoon x={24} y={-30} calm={calm} />
      <Hanok x={-16} y={10} w={14} lit />
      <Hanok x={18} y={16} w={12} />
    </>
  ),
  // L'arbre qui se souvient : forêt de bambous et grand arbre sacré.
  'topik3-w3': (calm) => (
    <>
      <Bamboo x={-24} y={18} calm={calm} />
      <SacredTree x={8} y={16} />
      <Bamboo x={30} y={20} s={0.8} calm={calm} />
    </>
  ),
  // Le cheval de la selle peinte : tumulus de Gyeongju et cheval céleste.
  'topik3-w4': (calm) => (
    <>
      <Tumulus x={-6} y={18} w={28} />
      <Tumulus x={26} y={20} w={14} />
      <FlyingHorse x={10} y={-22} calm={calm} />
    </>
  ),
  // Le jardin secret : pavillon sur l'étang et cerf de longévité.
  'topik3-w5': () => (
    <>
      <GardenPavilion x={-4} y={12} />
      <Deer x={26} y={20} />
    </>
  ),
  // Le gué du Nakdong : montagnes, fleuve et barque.
  'topik3-w6': (calm) => (
    <>
      <Mountain x={-14} y={6} w={26} h={30} />
      <Waves y={16} w={28} />
      <Boat x={14} y={12} calm={calm} />
    </>
  ),
  // Les sœurs de Cheolsan : maison abandonnée et lotus sous la lune.
  'topik3-w7': (calm) => (
    <>
      <FullMoon x={-24} y={-28} calm={calm} />
      <Hanok x={4} y={8} w={16} />
      <LotusLantern x={28} y={20} calm={calm} color="#F4F1EC" />
    </>
  ),
  // Le banquet de Namwon : pavillon Gwanghallu et balançoire de Chunhyang.
  'topik3-w8': (calm) => (
    <>
      <Library x={-10} y={12} label="광한루" />
      <Swing x={24} y={20} calm={calm} />
    </>
  ),
  // « Voici l'inspecteur royal ! » : le pavillon et le mapae levé.
  'topik3-final': (calm) => (
    <>
      <Library x={-8} y={14} label="광한루" />
      <Mapae x={24} y={-6} calm={calm} />
    </>
  ),
  // ───── TOPIK 4 : l'Historien des Annales (hiver) ─────
  // Les pages manquantes : la salle des annales sous la neige.
  'topik4-w1': () => (
    <>
      <Library x={-6} y={12} label="춘추관" />
      <Snow x={-6} y={-6} w={14} />
      <ArchiveChest x={26} y={20} />
    </>
  ),
  // Les traces dans la neige : maison, souliers et sapins.
  'topik4-w2': () => (
    <>
      <Hanok x={-8} y={8} w={16} lit />
      <Snow x={-8} y={-7} w={16} />
      <Shoes x={-8} y={12} />
      <SnowPine x={28} y={18} />
    </>
  ),
  // Le feu de la cuisine royale.
  'topik4-w3': (calm) => (
    <>
      <Hanok x={-14} y={6} w={12} />
      <Snow x={-14} y={-8} w={12} />
      <Stove x={18} y={18} calm={calm} />
    </>
  ),
  // La bénédiction de Samsin : pavillon et berceau.
  'topik4-w4': () => (
    <>
      <Hanok x={-10} y={10} w={14} lit />
      <Snow x={-10} y={-5} w={14} />
      <Cradle x={24} y={18} />
    </>
  ),
  // La colère des goblins : forêt de sapins enneigés.
  'topik4-w5': () => (
    <>
      <SnowPine x={-22} y={18} />
      <SnowPine x={-4} y={12} s={1.3} />
      <SnowPine x={16} y={20} />
      <SnowPine x={32} y={14} s={0.9} />
    </>
  ),
  // Le rapport de la sécheresse : rizières craquelées sous le soleil.
  'topik4-w6': () => (
    <>
      <DryField x={-6} y={18} />
      <Hanok x={24} y={8} w={10} />
    </>
  ),
  // La nuit de l'éclipse : lune mordue au-dessus du palais.
  'topik4-w7': (calm) => (
    <>
      <Eclipse x={18} y={-26} calm={calm} />
      <PalaceGate x={-6} y={14} />
    </>
  ),
  // Les archives de la montagne.
  'topik4-w8': () => (
    <>
      <Mountain x={-10} y={6} w={28} h={32} />
      <Snow x={-10} y={-24} w={8} />
      <ArchiveChest x={22} y={20} />
    </>
  ),
  // Le serment du sagwan.
  'topik4-final': (calm) => (
    <>
      <Library x={-8} y={14} label="사고" />
      <Snow x={-8} y={-4} w={14} />
      <FullMoon x={26} y={-26} calm={calm} />
    </>
  ),
  // ── TOPIK 5 : le Chant de la princesse Bari ──
  // La femme-escargot du rizière.
  'topik5-w1': () => (
    <>
      <Hanok x={-14} y={10} w={12} />
      <Well x={18} y={18} />
      <SnailShell x={4} y={24} />
    </>
  ),
  // Yeono et Seo-nyeo : le rocher qui part vers le soleil levant.
  'topik5-w2': (calm) => (
    <>
      <Waves y={22} w={40} />
      <Boat x={-10} y={16} calm={calm} />
      <FullMoon x={22} y={-24} calm={calm} />
    </>
  ),
  // L'enfant général ailé et son cheval-dragon.
  'topik5-w3': (calm) => (
    <>
      <Mountain x={-12} y={14} w={24} h={30} />
      <FlyingHorse x={20} y={-6} calm={calm} />
    </>
  ),
  // Le garçon-arbre et le grand déluge.
  'topik5-w4': () => (
    <>
      <SacredTree x={-6} y={14} />
      <Waves y={24} w={40} />
      <Deer x={22} y={18} />
    </>
  ),
  // Oneuri au jardin des saisons.
  'topik5-w5': () => (
    <>
      <GardenPavilion x={-12} y={12} />
      <SpiritFlower x={14} y={20} color="#F2A7C0" />
      <SpiritFlower x={22} y={22} color="#E36A3A" />
      <SpiritFlower x={6} y={24} />
    </>
  ),
  // Jacheongbi, déesse des moissons.
  'topik5-w6': () => (
    <>
      <DryField x={-6} y={18} />
      <Onggi x={20} y={14} />
      <Jangseung x={-26} y={10} />
    </>
  ),
  // Grand-mère Mago façonne les montagnes.
  'topik5-w7': () => (
    <>
      <Mountain x={-14} y={14} w={22} h={26} />
      <Mountain x={14} y={16} w={18} h={20} />
      <Hareubang x={30} y={20} />
    </>
  ),
  // Le gardien de l'eau de vie.
  'topik5-w8': (calm) => (
    <>
      <Well x={-8} y={16} />
      <SpiritFlower x={12} y={22} />
      <LotusLantern x={22} y={-10} calm={calm} color="#C9A6F2" />
    </>
  ),
  // La princesse Bari guide les âmes.
  'topik5-final': (calm) => (
    <>
      <Waves y={22} w={40} />
      <LotusLantern x={-18} y={-6} calm={calm} color="#C9A6F2" />
      <LotusLantern x={4} y={-14} calm={calm} />
      <LotusLantern x={22} y={-4} calm={calm} color="#FFE9A8" />
    </>
  ),

  // ── TOPIK 6 : la Légende de Dangun ──
  // Hwanung descend sous l'arbre sacré du mont Taebaek.
  'topik6-w1': (calm) => (
    <>
      <Mountain x={-8} y={18} w={28} h={34} />
      <SacredTree x={4} y={-12} s={0.6} />
      <FullMoon x={26} y={-28} calm={calm} />
    </>
  ),
  // L'ourse et le tigre dans la caverne.
  'topik6-w2': (calm) => (
    <>
      <Cave x={-8} y={20} />
      <Garlic x={16} y={22} />
      <WhiteTiger x={26} y={6} calm={calm} />
    </>
  ),
  // Jumong, né d'un œuf, l'archer.
  'topik6-w3': (calm) => (
    <>
      <GlowEgg x={-14} y={14} calm={calm} />
      <Bow x={14} y={8} />
      <Waves y={24} w={40} />
    </>
  ),
  // Bak Hyeokgeose, roi de Silla.
  'topik6-w4': (calm) => (
    <>
      <Tumulus x={-8} y={20} />
      <GlowEgg x={18} y={4} calm={calm} />
      <Well x={22} y={20} />
    </>
  ),
  // La cloche d'Emille.
  'topik6-w5': (calm) => (
    <>
      <BigBell x={-4} y={14} calm={calm} />
      <Mountain x={24} y={18} w={14} h={18} />
    </>
  ),
  // La flûte qui calme dix mille vagues.
  'topik6-w6': (calm) => (
    <>
      <SeaDragon x={-10} y={10} calm={calm} />
      <Flute x={18} y={-10} />
      <Waves y={24} w={40} />
    </>
  ),
  // La danse de Cheoyong.
  'topik6-w7': (calm) => (
    <>
      <Dancer x={-6} y={14} calm={calm} color={DAN_RED} />
      <HahoeMask x={20} y={-6} />
      <FullMoon x={-26} y={-26} calm={calm} />
    </>
  ),
  // Dangun fonde Gojoseon.
  'topik6-w8': () => (
    <>
      <PalaceGate x={-6} y={16} />
      <Mountain x={24} y={14} w={14} h={18} />
    </>
  ),
  // Le serment du gardien des mythes.
  'topik6-final': (calm) => (
    <>
      <Mountain x={-10} y={20} w={30} h={38} />
      <SacredTree x={2} y={-16} s={0.55} />
      <Phoenix x={26} y={-20} calm={calm} />
    </>
  ),
};
