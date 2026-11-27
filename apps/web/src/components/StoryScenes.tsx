import type { ReactNode } from 'react';
import { motion } from 'motion/react';
import { Bamboo, Castle, DawnGate, Hut, Lanterns, Pagoda, Torii, ROCK, ROCK_DARK, VERMILION } from './MapParts';
import { KOREAN_SCENES } from './KoreanScenes';
import { ENGLISH_SCENES } from './EnglishScenes';
import { CHINESE_SCENES } from './ChineseScenes';
import { SPANISH_SCENES } from './SpanishScenes';
import { GERMAN_SCENES } from './GermanScenes';

/**
 * Mode histoire : le décor de chaque île raconte son chapitre (content/story/story.json).
 * N5, la route du samouraï ; N4, la mission du ninja, de nuit ; N3, le monde des esprits sous la neige ;
 * N2, la capitale de l'onmyōji en été ; N1, le règne du shōgun à l'aube du Nouvel An.
 * Chaque scène est dessinée autour de (0, 0), le centre de l'île ; `calm` coupe les animations.
 */
const LIT = '#FFD27A';
const ROOF = '#2F3B4A';
const WALL = '#F2ECDD';
const STONE = '#8A8177';
const DARK_WOOD = '#4A3424';
const SNOW = '#FFFFFF';

type P = { x: number; y: number; s?: number };
const at = ({ x, y, s = 1 }: P, flip = false) => `translate(${x} ${y}) scale(${flip ? -s : s} ${s})`;

/** Bannière verticale (nobori). */
function Nobori({ color = VERMILION, ...p }: P & { color?: string }) {
  return (
    <g transform={at(p)}>
      <rect x="-0.8" y="-30" width="1.6" height="32" fill="#3B2A1C" />
      <rect x="0.8" y="-29" width="8" height="19" fill="#FFFFFF" />
      <rect x="0.8" y="-29" width="8" height="5" fill={color} />
      <circle cx="4.8" cy="-17" r="2.2" fill={color} />
    </g>
  );
}

/** Cours d'eau qui traverse l'île (ou rivière gelée). */
function River({ d, color = '#6CC5D8', edge = '#3E97AE' }: { d: string; color?: string; edge?: string }) {
  return (
    <>
      <path d={d} stroke={edge} strokeWidth="12" fill="none" strokeLinecap="round" opacity={0.55} />
      <path d={d} stroke={color} strokeWidth="8.5" fill="none" strokeLinecap="round" />
    </>
  );
}

/** Enseigne de bois avec un caractère. */
function Sign({ glyph, tilt = 0, ...p }: P & { glyph: string; tilt?: number }) {
  return (
    <g transform={`${at(p)} rotate(${tilt})`}>
      <rect x="-0.8" y="-4" width="1.6" height="10" fill={DARK_WOOD} />
      <rect x="-6" y="-15" width="12" height="11" rx="1.5" fill="#FFF6E0" stroke={DARK_WOOD} strokeWidth="1" />
      <text y="-9.5" dy="0.36em" textAnchor="middle" fontSize="8" fontWeight="900" className="jp" fill={VERMILION}>{glyph}</text>
    </g>
  );
}

/** Muraille blanche coiffée de tuiles. */
function Rampart({ w = 34 }: { w?: number }) {
  return (
    <>
      <rect x={-w} y="-2" width={w * 2} height="6" fill={STONE} />
      <rect x={-w} y="-13" width={w * 2} height="11" fill={WALL} />
      <path d={`M${-w - 3} -12 H${w + 3} L${w - 1} -17 H${-w + 1}Z`} fill={ROOF} />
    </>
  );
}

/** Porte fortifiée à étage. */
function GateHouse({ lit = false, ...p }: P & { lit?: boolean }) {
  return (
    <g transform={at(p)}>
      <rect x="-13" y="-14" width="26" height="18" fill="#6B4A32" />
      <rect x="-8" y="-9" width="16" height="13" fill="#2E2018" />
      <path d="M0 -9 V4" stroke="#6B4A32" strokeWidth="1" />
      <rect x="-13" y="-27" width="26" height="13" fill={WALL} />
      {[-7, 4].map((wx) => <rect key={wx} x={wx} y="-23" width="3.5" height="5" fill={lit ? LIT : '#3B2A1C'} />)}
      <path d="M-20 -26 Q0 -39 20 -26 L14 -31 H-14Z" fill={ROOF} />
    </g>
  );
}

/** Sommet rocheux, enneigé ou non. */
function Peak({ w, h, fill = '#66727E', snow = true, ...p }: P & { w: number; h: number; fill?: string; snow?: boolean }) {
  return (
    <g transform={at(p)}>
      <path d={`M${-w} 0 L0 ${-h} L${w} 0Z`} fill={fill} />
      <path d={`M${-w} 0 L0 ${-h} L${-w * 0.25} 0Z`} fill="#000000" opacity={0.14} />
      {snow && <path d={`M0 ${-h} L${w * 0.3} ${-h * 0.7} L${w * 0.12} ${-h * 0.76} L0 ${-h * 0.62} L${-w * 0.14} ${-h * 0.76} L${-w * 0.3} ${-h * 0.7}Z`} fill={SNOW} />}
    </g>
  );
}

/** Étal de marché sous son auvent rayé. */
function Stall({ color = VERMILION, lit = false, ...p }: P & { color?: string; lit?: boolean }) {
  return (
    <g transform={at(p)}>
      <rect x="-11" y="-14" width="1.6" height="16" fill={DARK_WOOD} />
      <rect x="9.4" y="-14" width="1.6" height="16" fill={DARK_WOOD} />
      <rect x="-11" y="-5" width="22" height="7" fill="#B8865A" />
      {[['#E9A23B', -6], ['#6FAE4F', 0], ['#C8323F', 6]].map(([c, cx]) => <circle key={cx} cx={cx} cy="-7" r="2" fill={c as string} />)}
      <path d="M-14 -13 L-11 -21 H11 L14 -13Z" fill="#FFF6E0" />
      {[0, 0.4, 0.8].map((a) => (
        <path key={a} d={`M${-11 + 22 * a} -21 H${-11 + 22 * (a + 0.2)} L${-14 + 28 * (a + 0.2)} -13 H${-14 + 28 * a}Z`} fill={color} />
      ))}
      {lit && (
        <>
          <circle cx="0" cy="-10" r="7" fill="#FFB65C" opacity={0.3} />
          <ellipse cx="0" cy="-10.5" rx="2.4" ry="3" fill="#FF9A3D" />
        </>
      )}
    </g>
  );
}

/** Dojo ou grande maison de bois. */
function Dojo({ lit = false, ...p }: P & { lit?: boolean }) {
  return (
    <g transform={at(p)}>
      <rect x="-16" y="-10" width="32" height="13" fill="#6B4A32" />
      <rect x="-4" y="-6" width="8" height="9" fill={lit ? LIT : '#2E2018'} />
      {[-12, 8].map((wx) => <rect key={wx} x={wx} y="-6" width="4" height="4" fill={lit ? LIT : '#2E2018'} />)}
      <path d="M-23 -9 L-15 -20 H15 L23 -9Z" fill={ROOF} />
      <rect x="-15" y="-22" width="30" height="2.4" fill="#1F2833" />
    </g>
  );
}

/** Cible d'entraînement, une étoile de ninja plantée dedans. */
function Target(p: P) {
  return (
    <g transform={at(p)}>
      <rect x="-1" y="-9" width="2" height="12" fill={DARK_WOOD} />
      <circle cy="-13" r="5.5" fill="#E3CF9A" stroke="#8C6A3F" strokeWidth="1" />
      <circle cy="-13" r="2.2" fill={VERMILION} />
      <path d="M2.5 -18 l1 2.4 l2.4 1 l-2.4 1 l-1 2.4 l-1 -2.4 l-2.4 -1 l2.4 -1Z" fill="#C9D2DC" />
    </g>
  );
}

/** Lion-chien de pierre sur son socle. */
function Komainu({ flip = false, ...p }: P & { flip?: boolean }) {
  return (
    <g transform={at(p, flip)}>
      <rect x="-6" y="-3" width="12" height="6" fill="#6E6862" />
      <path d="M-5 -3 Q-6 -12 0 -13 L4 -13 Q6 -8 4 -3Z" fill="#A8A29A" />
      <circle cx="3" cy="-15" r="4.2" fill="#B9B2A6" />
      <path d="M0 -18 l1 -3.4 l2.4 3Z" fill="#B9B2A6" />
      <circle cx="4.6" cy="-15.6" r="0.8" fill="#2B231D" />
    </g>
  );
}

/** Porte de bois du village caché. */
function WoodGate(p: P) {
  return (
    <g transform={at(p)}>
      <rect x="-10" y="-15" width="20" height="19" fill="#6B4A32" />
      <path d="M0 -15 V4" stroke="#2E2018" strokeWidth="1" />
      <circle cx="-2.5" cy="-5" r="1" fill="#C9A24A" />
      <circle cx="2.5" cy="-5" r="1" fill="#C9A24A" />
      <rect x="-13" y="-22" width="3" height="26" fill={DARK_WOOD} />
      <rect x="10" y="-22" width="3" height="26" fill={DARK_WOOD} />
      <rect x="-17" y="-22" width="34" height="3.5" fill="#3A2A1E" />
      <path d="M-20 -22 L-14 -28 H14 L20 -22Z" fill={ROOF} />
    </g>
  );
}

/** Palissade de pieux taillés en pointe. */
function Palisade({ from, to, y }: { from: number; to: number; y: number }) {
  const stakes = Array.from({ length: Math.floor((to - from) / 4) + 1 }, (_, i) => from + i * 4);
  return (
    <>
      {stakes.map((sx) => <path key={sx} d={`M${sx - 1.6} ${y} V${y - 11} L${sx} ${y - 14} L${sx + 1.6} ${y - 11} V${y}Z`} fill="#5A4632" />)}
    </>
  );
}

/** Feu de camp. */
function Campfire({ calm, ...p }: P & { calm: boolean }) {
  return (
    <g transform={at(p)}>
      <circle r="12" cy="-4" fill="#FFB65C" opacity={0.25} />
      <path d="M-7 2 L7 -1 M-7 -1 L7 2" stroke="#3A2A1E" strokeWidth="2.6" strokeLinecap="round" />
      <motion.g style={{ transformOrigin: '0px 0px' }} animate={calm ? undefined : { scaleY: [1, 1.18, 0.94, 1.1, 1], scaleX: [1, 0.94, 1.05, 0.97, 1] }} transition={{ duration: 0.9, repeat: Infinity }}>
        <path d="M0 0 C-6 0 -6 -6 -3 -9 C-2 -11 0 -12 0 -16 C4 -12 6 -7 5 -3 C4 -1 2 0 0 0Z" fill="#FF8A3D" />
        <path d="M0 -1 C-3 -1 -3 -4 -1 -6 C0 -7 0 -8 0 -10 C2 -8 3 -5 2.5 -3 C2 -2 1 -1 0 -1Z" fill="#FFE08A" />
      </motion.g>
    </g>
  );
}

/** Maison à grand toit de tuiles. */
function TiledHouse({ w, lit = false, ...p }: P & { w: number; lit?: boolean }) {
  return (
    <g transform={at(p)}>
      <rect x={-w + 3} y="-6" width={2 * w - 6} height="10" fill="#D9CBB0" />
      <rect x="-2" y="-3" width="4" height="4.5" fill={lit ? LIT : '#3B2A1C'} />
      <path d={`M${-w - 3} -5 Q0 -9 ${w + 3} -5 L${w - 3} -16 H${-w + 3}Z`} fill="#3D4A5C" />
      {[-0.5, 0, 0.5].map((k) => <path key={k} d={`M${k * w} -15 L${k * (w + 6)} -6.5`} stroke="#2A3442" strokeWidth="1" opacity={0.6} />)}
      <rect x={-w + 3} y="-18" width={2 * w - 6} height="2.6" fill="#2A3442" />
    </g>
  );
}

/** Grue du Japon. */
function Crane(p: P) {
  return (
    <g transform={at(p)}>
      <path d="M-1 2 V9 M2 2 V9" stroke="#2B231D" strokeWidth="0.9" />
      <path d="M-5 -1 l-6 3 l6 1.5Z" fill="#2B231D" />
      <ellipse rx="6" ry="3.6" fill="#FFFFFF" />
      <path d="M5 -1 Q9 -8 6.5 -12" stroke="#FFFFFF" strokeWidth="2.2" fill="none" strokeLinecap="round" />
      <circle cx="6.5" cy="-13" r="2.1" fill="#FFFFFF" />
      <circle cx="6.5" cy="-14.8" r="1.1" fill={VERMILION} />
      <path d="M8 -13.4 l5.5 0.8 l-5.5 0.9Z" fill="#D9A23B" />
    </g>
  );
}

/** Lanterne de pierre. */
function StoneLantern({ lit = false, ...p }: P & { lit?: boolean }) {
  return (
    <g transform={at(p)}>
      {lit && <circle cy="-11" r="9" fill="#FFB65C" opacity={0.28} />}
      <rect x="-4" y="0" width="8" height="2.5" fill="#6E6862" />
      <rect x="-1.5" y="-7" width="3" height="7" fill="#8D8780" />
      <rect x="-4" y="-14" width="8" height="7" fill="#A8A29A" />
      <rect x="-2" y="-12.5" width="4" height="4" fill={lit ? LIT : '#3B2A1C'} />
      <path d="M-6.5 -14 L0 -20 L6.5 -14Z" fill="#6E6862" />
    </g>
  );
}

/** Chat porte-bonheur, la patte levée. */
function ManekiNeko(p: P) {
  return (
    <g transform={at(p)}>
      <ellipse cy="-5" rx="6.5" ry="7" fill="#FFFFFF" />
      <ellipse cx="6.4" cy="-17" rx="2.2" ry="3.8" fill="#FFFFFF" />
      <path d="M-5 -18 L-4.4 -23.5 L-0.8 -20Z M5 -18 L4.4 -23.5 L0.8 -20Z" fill="#FFFFFF" />
      <path d="M-4.2 -19.5 L-4 -22 L-2.2 -20.2Z M4.2 -19.5 L4 -22 L2.2 -20.2Z" fill="#F4A9C0" />
      <circle cy="-15.5" r="5.6" fill="#FFFFFF" />
      <path d="M-3.4 -16 q1.2 -1.4 2.4 0 M1 -16 q1.2 -1.4 2.4 0" stroke="#2B231D" strokeWidth="0.9" fill="none" strokeLinecap="round" />
      <path d="M-1 -13.6 h2 l-1 1.1Z" fill="#E07A9B" />
      <rect x="-4.6" y="-11" width="9.2" height="2" rx="1" fill={VERMILION} />
      <circle cy="-8.6" r="1.5" fill="#F2C14E" />
      <ellipse cx="-3" cy="-3.5" rx="2.4" ry="3.4" fill="#F2C14E" stroke="#B08D3C" strokeWidth="0.6" />
    </g>
  );
}

/** Nuage d'orage et son éclair. */
function StormCloud({ calm, ...p }: P & { calm: boolean }) {
  const bolt = <path d="M2 6 L-7 24 L-1 24 L-9 44 L7 19 L1 19 L8 6Z" fill="#FFE98A" stroke="#FFFFFF" strokeWidth="0.6" />;
  return (
    <g transform={at(p)}>
      {calm ? bolt : <motion.g animate={{ opacity: [0, 0, 1, 0.2, 1, 0, 0] }} transition={{ duration: 3.2, repeat: Infinity, times: [0, 0.55, 0.6, 0.66, 0.72, 0.82, 1] }}>{bolt}</motion.g>}
      <ellipse cx="0" cy="2" rx="26" ry="9" fill="#4A5266" />
      <ellipse cx="-10" cy="-5" rx="13" ry="9" fill="#586178" />
      <ellipse cx="10" cy="-4" rx="12" ry="8" fill="#4F5870" />
      <ellipse cx="0" cy="5" rx="22" ry="5" fill="#363C4E" />
    </g>
  );
}

/** Tour de guet. */
function WatchTower({ lit = false, ...p }: P & { lit?: boolean }) {
  return (
    <g transform={at(p)}>
      <path d="M-9 4 L-7 -14 H7 L9 4Z" fill={STONE} />
      <rect x="-8" y="-26" width="16" height="12" fill={WALL} />
      <rect x="-3" y="-23" width="6" height="6" fill={lit ? LIT : '#3B2A1C'} />
      <path d="M-13 -25 Q0 -36 13 -25 L9 -30 H-9Z" fill={ROOF} />
    </g>
  );
}

/** Palais du seigneur : grande salle à piliers rouges. */
function Palace({ lit = false, ...p }: P & { lit?: boolean }) {
  return (
    <g transform={at(p)}>
      <rect x="-27" y="0" width="54" height="3.5" fill={STONE} />
      <rect x="-24" y="-12" width="48" height="12" fill={WALL} />
      {[-18, -6, 6, 18].map((wx) => <rect key={wx} x={wx - 3.5} y="-9" width="7" height="7" fill={lit ? LIT : '#3B2A1C'} />)}
      {[-24, -12, 0, 12, 24].map((px) => <rect key={px} x={px - 1.2} y="-12" width="2.4" height="12" fill={VERMILION} />)}
      <path d="M-32 -11 Q0 -19 32 -11 L22 -24 H-22Z" fill={ROOF} />
      <rect x="-12" y="-32" width="24" height="8" fill={WALL} />
      {[-6, 3].map((wx) => <rect key={wx} x={wx} y="-30" width="3" height="4" fill={lit ? LIT : '#3B2A1C'} />)}
      <path d="M-18 -31 Q0 -38 18 -31 L12 -41 H-12Z" fill={ROOF} />
      <path d="M-12 -41 l-3 -3 M12 -41 l3 -3" stroke="#C9A24A" strokeWidth="1.6" strokeLinecap="round" />
    </g>
  );
}

/** Cabane sous la neige. */
function SnowHut(p: P) {
  return (
    <g transform={at(p)}>
      <Hut x={0} y={0} />
      <path d="M-16 -6.5 L0 -21 L16 -6.5 L11 -8 L0 -16.5 L-11 -8Z" fill={SNOW} />
    </g>
  );
}

/** Renard de pierre des sanctuaires, bavoir rouge. */
function FoxStatue({ flip = false, ...p }: P & { flip?: boolean }) {
  return (
    <g transform={at(p, flip)}>
      <rect x="-5.5" y="-3" width="11" height="6" fill="#8D99A6" />
      <path d="M-4 -4 Q-10 -8 -7 -16 Q-4 -10 -2.6 -6Z" fill="#FFFFFF" />
      <path d="M-4 -3 Q-5 -13 1 -14 Q5 -12 4 -3Z" fill="#FFFFFF" />
      <path d="M-0.6 -18 l0.4 -5.4 l3 3.4Z M3 -19 l2.6 -4.4 l1 5.2Z" fill="#FFFFFF" />
      <circle cx="2.2" cy="-16.4" r="3.7" fill="#FFFFFF" />
      <path d="M4.6 -17.6 l5.4 2 l-5.4 1.4Z" fill="#FFFFFF" />
      <circle cx="3.4" cy="-17" r="0.7" fill="#2B231D" />
      <path d="M-2.2 -12.6 h6.4 l-1 4.4 h-4.4Z" fill={VERMILION} />
    </g>
  );
}

/** Arbre nu de l'hiver. */
function BareTree(p: P) {
  return (
    <g transform={at(p)} stroke="#4A3A33" fill="none" strokeLinecap="round">
      <path d="M0 6 V-12" strokeWidth="2.4" />
      <path d="M0 -4 L-8 -13 M0 -8 L8 -16 M0 -12 L-4 -22 M0 -12 L5 -21 M-8 -13 L-12 -13 M8 -16 L12 -15" strokeWidth="1.4" />
    </g>
  );
}

/** Horloge dont les aiguilles tournent trop vite, ou à l'envers. */
function Clock({ r = 6, calm, speed = 4, reverse = false, ...p }: P & { r?: number; calm: boolean; speed?: number; reverse?: boolean }) {
  const turn = reverse ? [0, -360] : [0, 360];
  return (
    <g transform={at(p)}>
      <circle r={r} fill="#FFF6E0" stroke="#3B2A1C" strokeWidth="1.3" />
      <motion.path d={`M0 0 V${-r * 0.72}`} stroke="#3B2A1C" strokeWidth="1.1" strokeLinecap="round" style={{ transformOrigin: '0px 0px' }} animate={calm ? undefined : { rotate: turn }} transition={{ duration: speed, repeat: Infinity, ease: 'linear' }} />
      <motion.path d={`M0 0 H${r * 0.5}`} stroke={VERMILION} strokeWidth="1.3" strokeLinecap="round" style={{ transformOrigin: '0px 0px' }} animate={calm ? undefined : { rotate: turn }} transition={{ duration: speed * 6, repeat: Infinity, ease: 'linear' }} />
      <circle r="0.9" fill="#3B2A1C" />
    </g>
  );
}

/** Auberge à étage sous la neige, horloge au pignon. */
function Inn({ calm, ...p }: P & { calm: boolean }) {
  return (
    <g transform={at(p)}>
      <rect x="-18" y="-10" width="36" height="13" fill="#8C6A3F" />
      <rect x="-3.5" y="-5" width="7" height="8" fill="#3B2A1C" />
      {[-13, 9].map((wx) => <rect key={wx} x={wx} y="-7" width="4.5" height="4.5" fill={LIT} />)}
      <path d="M-25 -8.5 L-18 -17 H18 L25 -8.5Z" fill={ROOF} />
      <path d="M-25 -9.5 L-18 -18 H18 L25 -9.5 L20 -11 L16 -15.5 H-16 L-20 -11Z" fill={SNOW} />
      <rect x="-12" y="-25" width="24" height="8" fill="#8C6A3F" />
      {[-9, 5].map((wx) => <rect key={wx} x={wx} y="-23.5" width="4" height="4" fill={LIT} />)}
      <path d="M-18 -24 L0 -38 L18 -24Z" fill={ROOF} />
      <path d="M-18 -25 L0 -39 L18 -25 L13 -26 L0 -35 L-13 -26Z" fill={SNOW} />
      <Clock x={0} y={-28} r={4.6} calm={calm} speed={3} />
    </g>
  );
}

/** Daruma : un œil peint pour le vœu, l'autre en attente. */
function Daruma(p: P) {
  return (
    <g transform={at(p)}>
      <ellipse cy="-9" rx="9.5" ry="10" fill={VERMILION} />
      <ellipse cy="-11.5" rx="6.4" ry="5.6" fill="#F6EBD3" />
      <path d="M-5 -15 q2.4 -2 4.4 0 M0.6 -15 q2.4 -2 4.4 0" stroke="#2B231D" strokeWidth="1.3" fill="none" strokeLinecap="round" />
      <circle cx="-2.6" cy="-11.6" r="1.8" fill="#FFFFFF" stroke="#2B231D" strokeWidth="0.6" />
      <circle cx="-2.6" cy="-11.6" r="1" fill="#2B231D" />
      <circle cx="2.6" cy="-11.6" r="1.8" fill="#FFFFFF" stroke="#2B231D" strokeWidth="0.6" />
      <path d="M-2 -8.2 q2 1.4 4 0" stroke="#2B231D" strokeWidth="0.9" fill="none" strokeLinecap="round" />
      <path d="M-4 -3.4 q4 3 8 0 M-3 -0.8 q3 2 6 0" stroke="#F2C14E" strokeWidth="1.1" fill="none" strokeLinecap="round" />
    </g>
  );
}

/** Pavillon de temple, toit chargé de neige. */
function TempleHall(p: P) {
  return (
    <g transform={at(p)}>
      <rect x="-18" y="0" width="36" height="3" fill="#8D99A6" />
      <rect x="-15" y="-12" width="30" height="12" fill="#E9DCC3" />
      <rect x="-4" y="-9" width="8" height="9" fill="#3B2A1C" />
      {[-15, 12.6].map((px) => <rect key={px} x={px} y="-12" width="2.4" height="12" fill={VERMILION} />)}
      <path d="M-24 -10.5 Q0 -31 24 -10.5Z" fill={ROOF} />
      <path d="M-22 -12.5 Q0 -32 22 -12.5 Q0 -24 -22 -12.5Z" fill={SNOW} />
    </g>
  );
}

/** Cèdre géant, le nid du corbeau à sa cime. */
function GiantCedar(p: P) {
  return (
    <g transform={at(p)}>
      <rect x="-3" y="-14" width="6" height="20" fill={DARK_WOOD} />
      {[0, 1, 2, 3].map((i) => (
        <g key={i}>
          <path d={`M0 ${-58 + i * 12} L${11 + i * 5} ${-38 + i * 12} H${-11 - i * 5}Z`} fill={i % 2 ? '#1E4236' : '#24503F'} />
          <path d={`M0 ${-58 + i * 12} L${5 + i * 2} ${-49 + i * 12} L0 ${-51 + i * 12} L${-5 - i * 2} ${-49 + i * 12}Z`} fill={SNOW} />
        </g>
      ))}
      <ellipse cy="-58" rx="8" ry="3" fill="#8C6A3F" />
      <path d="M-8 -58 q8 5 16 0" stroke="#5A4632" strokeWidth="1" fill="none" />
      <ellipse cx="-0.5" cy="-63" rx="5" ry="3.4" fill="#16161C" />
      <path d="M-4.5 -63 l-5 2.4 l5 0.6Z" fill="#16161C" />
      <circle cx="4" cy="-66" r="2.7" fill="#16161C" />
      <path d="M6.2 -66.6 l4.4 0.9 l-4.4 1.1Z" fill="#E2A23B" />
      {[[3.2, -67], [5, -66.6], [4.2, -65]].map(([ex, ey], i) => <circle key={i} cx={ex} cy={ey} r="0.55" fill="#BFE8FF" />)}
    </g>
  );
}

const SCENES: Record<string, (calm: boolean) => ReactNode> = {
  // ───── N5 · La Voie du samouraï ─────
  // Le gué du Kappa : rivière, pierres de gué, dojo de Maître Koto, pinceau planté sur la berge.
  'n5-w1': () => (
    <>
      <River d="M-36 -20 Q-10 -12 0 2 T36 20" />
      {[[-14, -11], [0, 1], [13, 11]].map(([cx, cy], i) => <ellipse key={i} cx={cx} cy={cy} rx="3.8" ry="2.3" fill="#B9B2A6" stroke="#7D7468" strokeWidth="0.8" />)}
      <Hut x={24} y={-12} s={1.05} />
      <Nobori x={41} y={-8} s={0.8} />
      <g transform="translate(-27 12) rotate(-24)">
        <rect x="-1.6" y="-22" width="3.2" height="17" rx="1" fill="#B8865A" />
        <rect x="-1.9" y="-7" width="3.8" height="2.4" fill="#F2C14E" />
        <path d="M-2.4 -5 Q0 4 0 7 Q0 4 2.4 -5Z" fill="#1E1A22" />
      </g>
    </>
  ),
  // Le village-étape aux enseignes changées par le Tanuki.
  'n5-w2': () => (
    <>
      <Hut x={-20} y={0} s={1.15} />
      <Hut x={16} y={-8} />
      <Hut x={8} y={14} s={0.95} />
      <Sign x={-38} y={8} glyph="ア" tilt={-14} />
      <Sign x={33} y={-2} glyph="カ" tilt={13} />
      <Sign x={-10} y={18} glyph="ナ" tilt={-6} />
    </>
  ),
  // La porte du château et sa muraille.
  'n5-w3': () => (
    <g transform="translate(0 10) scale(1.2)">
      <Rampart w={30} />
      <GateHouse x={0} y={0} />
      <Nobori x={-24} y={2} />
      <Nobori x={19} y={2} />
    </g>
  ),
  // Le col du Tengu : un sentier entre deux sommets, un petit torii au passage.
  'n5-w4': () => (
    <>
      <Peak x={-22} y={14} w={26} h={54} />
      <Peak x={24} y={14} w={24} h={44} />
      <path d="M2 18 Q-7 6 2 -4 Q9 -11 3 -18" stroke="#EBD9AE" strokeWidth="3.4" strokeDasharray="5 4" fill="none" strokeLinecap="round" />
      <Torii x={3} y={-14} s={0.5} />
    </>
  ),
  // Le marché du Chat-boulier.
  'n5-w5': () => (
    <>
      <Stall x={-21} y={2} />
      <Stall x={15} y={-6} color="#2E8B9A" />
      <Stall x={4} y={16} s={0.95} color="#D4A537" />
      <g transform="translate(-36 -16)">
        <rect x="-6" y="-5" width="12" height="10" rx="1" fill="#FFF6E0" stroke={DARK_WOOD} strokeWidth="1.2" />
        <path d="M-6 -1.6 H6 M-6 1.8 H6" stroke={DARK_WOOD} strokeWidth="0.7" />
        {[-3.6, -1.2, 1.2, 3.6].map((bx, i) => <circle key={bx} cx={bx} cy={i % 2 ? 0 : -3.3} r="1" fill={VERMILION} />)}
      </g>
    </>
  ),
  // Le pont rouge où dort l'Oni.
  'n5-w6': () => {
    const arc = (px: number) => {
      const k = (px + 30) / 60;
      return (1 - k) * (1 - k) * 6 + 2 * k * (1 - k) * -22 + k * k * 6;
    };
    return (
      <>
        <River d="M-8 -30 Q8 -10 -4 4 T6 26" />
        <path d="M-30 6 Q0 -22 30 6" stroke="#8E1B26" strokeWidth="7.5" fill="none" strokeLinecap="round" />
        <path d="M-30 6 Q0 -22 30 6" stroke={VERMILION} strokeWidth="4.5" fill="none" strokeLinecap="round" />
        {[-24, -12, 12, 24].map((px) => <rect key={px} x={px - 0.9} y={arc(px) - 9} width="1.8" height="8" fill="#8E1B26" />)}
        <path d="M-28 -2 Q0 -30 28 -2" stroke={VERMILION} strokeWidth="1.6" fill="none" />
        <g transform="translate(1 -12)">
          <ellipse cx="2" rx="9" ry="5" fill="#D9534F" />
          <circle cx="-8" cy="-2" r="4.6" fill="#D9534F" />
          <path d="M-11 -5.4 l-0.6 -4 l3 2.2Z M-6 -6.4 l1.4 -3.8 l1.8 3.4Z" fill="#F2E3B3" />
          <path d="M-10.4 -1.6 h3" stroke="#3B2A1C" strokeWidth="1" strokeLinecap="round" />
          <text x="7" y="-9" fontSize="7" fontWeight="900" fill="#FFFFFF">z</text>
          <text x="12" y="-14" fontSize="5" fontWeight="900" fill="#FFFFFF">z</text>
        </g>
      </>
    );
  },
  // La grotte du Dragon : des kanji brillent dans le noir.
  'n5-w7': (calm) => (
    <>
      <path d="M-42 12 Q-40 -30 -12 -40 Q20 -48 42 12Z" fill={ROCK} />
      <path d="M-42 12 Q-40 -30 -12 -40 Q-24 -10 -20 12Z" fill={ROCK_DARK} opacity={0.6} />
      <path d="M-6 -41 l5 5 l6 -4 l5 6" stroke={ROCK_DARK} strokeWidth="1.4" fill="none" />
      <path d="M-16 12 Q-17 -19 0 -20 Q17 -19 16 12Z" fill="#17131C" />
      <ellipse cx="0" cy="4" rx="11" ry="8" fill="#FFB65C" opacity={0.22} />
      {['山', '日', '川'].map((g, i) => (
        <motion.text key={g} x={[-7.5, 0, 7.5][i]} y={[-1, -9, -1][i]} dy="0.36em" textAnchor="middle" fontSize="7" fontWeight="900" className="jp" fill="#FFD27A" animate={calm ? undefined : { opacity: [0.35, 1, 0.35] }} transition={{ duration: 2.4, repeat: Infinity, delay: i * 0.7 }}>{g}</motion.text>
      ))}
    </>
  ),
  // La ville du château un soir de fête.
  'n5-w8': (calm) => (
    <>
      <Hut x={-27} y={4} s={0.85} />
      <Hut x={29} y={2} s={0.85} />
      <Lanterns x={0} y={12} s={1.15} calm={calm} />
    </>
  ),
  // Le château du seigneur.
  'n5-final': () => (
    <>
      <Castle x={2} y={20} s={1.05} />
      <Nobori x={-31} y={16} />
      <Nobori x={30} y={14} />
    </>
  ),

  // ───── N4 · L'Ombre du ninja ─────
  // Le village caché : dojo éclairé, cibles d'entraînement, bambous.
  'n4-w1': () => (
    <>
      <Bamboo x={-30} y={8} s={0.7} />
      <Dojo x={-4} y={4} lit />
      <Target x={24} y={10} />
      <Target x={34} y={0} s={0.85} />
    </>
  ),
  // La porte du clan gardée par les Komainu.
  'n4-w2': () => (
    <>
      <Palisade from={-38} to={-16} y={8} />
      <Palisade from={16} to={38} y={8} />
      <WoodGate x={0} y={8} />
      <Komainu x={-23} y={16} />
      <Komainu x={23} y={16} flip />
    </>
  ),
  // La veillée : feu de camp et rêves qui s'envolent, proies du Baku.
  'n4-w3': (calm) => (
    <>
      <Hut x={-24} y={0} />
      <Hut x={24} y={-6} s={0.9} />
      <Campfire x={0} y={14} calm={calm} />
      {[0, 1, 2].map((i) => (
        <motion.circle key={i} cx={-22 + i * 5} cy={-24 - i * 9} r={2 + i * 1.7} fill="#CDB9F0" opacity={0.8} animate={calm ? undefined : { cy: [-24 - i * 9, -27 - i * 9, -24 - i * 9], opacity: [0.5, 0.9, 0.5] }} transition={{ duration: 3, repeat: Infinity, delay: i * 0.5 }} />
      ))}
    </>
  ),
  // Les toits de la ville, où guette la Grue rivale.
  'n4-w4': () => (
    <>
      <TiledHouse x={-2} y={-4} w={18} />
      <Crane x={-4} y={-31} />
      <TiledHouse x={-23} y={10} w={15} lit />
      <TiledHouse x={19} y={12} w={15} lit />
    </>
  ),
  // Le temple oublié du Kirin, envahi par la mousse.
  'n4-w5': () => (
    <>
      <Pagoda x={4} y={8} s={1.05} />
      <circle cx="-7" cy="-2" r="4.5" fill="#3F6B4A" opacity={0.85} />
      <circle cx="14" cy="-16" r="3.4" fill="#3F6B4A" opacity={0.85} />
      <path d="M-8 12 h24 M-5 15.5 h18" stroke={STONE} strokeWidth="2.4" strokeLinecap="round" />
      <StoneLantern x={-26} y={12} lit />
      <StoneLantern x={32} y={12} s={0.85} lit />
    </>
  ),
  // Le marché de nuit du Maneki-neko.
  'n4-w6': () => (
    <>
      <Stall x={-22} y={2} color="#9E3424" lit />
      <Stall x={22} y={-2} color="#2F5240" lit />
      <ManekiNeko x={1} y={18} s={1.1} />
    </>
  ),
  // L'infiltration : muraille du palais sous l'orage.
  'n4-w7': (calm) => (
    <>
      <g transform="translate(-4 12)"><Rampart w={32} /></g>
      <WatchTower x={20} y={12} s={1.1} lit />
      <StormCloud x={-12} y={-40} s={0.85} calm={calm} />
    </>
  ),
  // La cour du Seigneur des Bonnes Manières.
  'n4-w8': () => (
    <>
      <Palace x={0} y={12} lit />
      <Nobori x={-38} y={14} s={0.85} color="#3A3F6B" />
      <Nobori x={34} y={14} s={0.85} color="#3A3F6B" />
    </>
  ),
  // Le donjon où dort le Rouleau des Mille Formes.
  'n4-final': () => (
    <>
      <circle cx="2" cy="-12" r="26" fill="#FFD27A" opacity={0.12} />
      <Castle x={2} y={20} s={1.05} lit />
      <StoneLantern x={-32} y={16} lit />
      <StoneLantern x={34} y={16} lit />
    </>
  ),

  // ───── N3 · Le Voyage de l'esprit ─────
  // Le monde flottant : un torii dans la brume, gardé par les renards.
  'n3-w1': (calm) => (
    <>
      <Torii x={0} y={12} s={1.15} />
      <FoxStatue x={-25} y={14} />
      <FoxStatue x={25} y={14} flip />
      {[{ x: -14, y: -8, w: 26 }, { x: 16, y: 2, w: 22 }, { x: -4, y: 14, w: 30 }].map((m, i) => (
        <motion.ellipse key={i} cx={m.x} cy={m.y} rx={m.w} ry="5" fill="#FFFFFF" opacity={0.55} filter="url(#km-soft)" animate={calm ? undefined : { cx: [m.x, m.x + (i % 2 ? -10 : 10), m.x] }} transition={{ duration: 9 + i * 2, repeat: Infinity, ease: 'easeInOut' }} />
      ))}
    </>
  ),
  // Le sommet des résolutions.
  'n3-w2': () => (
    <>
      <Peak x={-26} y={14} w={22} h={36} fill="#8A97AB" />
      <Peak x={6} y={16} w={36} h={64} fill="#73829A" />
      <Nobori x={6} y={-46} s={0.55} />
    </>
  ),
  // La vallée des regrets : l'étang gelé et la Yuki-onna.
  'n3-w3': (calm) => (
    <>
      <Peak x={-32} y={8} w={20} h={34} fill="#8A97AB" />
      <Peak x={34} y={6} w={18} h={30} fill="#8A97AB" />
      <ellipse cx="-2" cy="12" rx="17" ry="6" fill="#BFE3F2" stroke="#FFFFFF" strokeWidth="1.5" />
      <path d="M-10 11 l5 1.5 l3 -2 M2 13 l6 -1" stroke="#8FC2D8" strokeWidth="0.8" fill="none" />
      <BareTree x={-14} y={-2} />
      <motion.g animate={calm ? undefined : { y: [0, -3, 0], opacity: [0.75, 1, 0.75] }} transition={{ duration: 4, repeat: Infinity, ease: 'easeInOut' }}>
        <g transform="translate(13 -2)">
          <circle cy="-6" r="13" fill="#BFE8FF" opacity={0.3} filter="url(#km-soft)" />
          <path d="M0 -14 Q6 -2 7 8 H-7 Q-6 -2 0 -14Z" fill="#FFFFFF" />
          <circle cy="-16" r="3" fill="#F4F8FB" />
          <path d="M-3.4 -16 Q-4 -22 0 -20.5 Q4 -22 3.4 -16 L4.2 -5 L2 -8 L2.4 -15.4 Q0 -17.4 -2.4 -15.4 L-2 -8 L-4.2 -5Z" fill="#1F2A44" />
        </g>
      </motion.g>
    </>
  ),
  // L'auberge hors du temps, aux horloges folles.
  'n3-w4': (calm) => (
    <>
      <Inn x={-6} y={10} calm={calm} />
      <g transform="translate(30 12)">
        <rect x="-1" y="-15" width="2" height="18" fill={DARK_WOOD} />
        <Clock x={0} y={-20} r={6} calm={calm} speed={2.2} reverse />
      </g>
    </>
  ),
  // La rivière gelée du Kappa.
  'n3-w5': () => (
    <>
      <River d="M-36 -20 Q-10 -12 0 2 T36 20" color="#D8F0FA" edge="#9CC7DD" />
      <path d="M-22 -15 l6 3 l-2 4 l7 2 M8 5 l6 1 l1 5 l7 2 M-6 -6 l-3 4" stroke="#6FA3C0" strokeWidth="1" fill="none" strokeLinecap="round" />
      <ellipse cx="1" cy="2" rx="5.4" ry="2.8" fill="#3E7FA0" />
      <path d="M-3.4 2.4 Q-3.6 -5 1 -5 Q5.6 -5 5.4 2.4Z" fill="#5FA36A" />
      <ellipse cx="1" cy="-5" rx="3.2" ry="1.1" fill="#E8F4F8" stroke="#3F7F4E" strokeWidth="0.5" />
      <circle cx="-0.6" cy="-1.4" r="0.7" fill="#17131C" />
      <circle cx="2.6" cy="-1.4" r="0.7" fill="#17131C" />
      <SnowHut x={25} y={-12} />
    </>
  ),
  // La forge de l'Oni : la seule tache de feu dans la neige.
  'n3-w6': (calm) => (
    <>
      <ellipse cx="-4" cy="2" rx="24" ry="13" fill="#FF8A3D" opacity={0.25} filter="url(#km-soft)" />
      <rect x="6" y="-34" width="7" height="16" fill="#3A3540" />
      <rect x="-20" y="-14" width="34" height="18" fill="#4A4550" />
      <path d="M-25 -13 L-17 -23 H11 L19 -13Z" fill="#2B2730" />
      <path d="M-25 -14 L-17 -24 H-4 L-9 -19 L-14 -20 L-19 -14Z" fill={SNOW} />
      <path d="M-11 4 Q-11 -9 -3 -9 Q5 -9 5 4Z" fill="#FF8A3D" />
      <path d="M-7 4 Q-7 -5 -3 -5 Q1 -5 1 4Z" fill="#FFE08A" />
      <path d="M19 -3 h13 l3 -3.4 h-19Z M22 -3 h7 v6 h-7Z M20 3 h11 v2 h-11Z" fill="#2B2730" />
      {[0, 1, 2].map((i) =>
        calm ? (
          <circle key={i} cx={9 + i * 2} cy={-40 - i * 6} r="1.3" fill="#FF8A3D" />
        ) : (
          <motion.circle key={i} r="1.4" fill="#FFB65C" initial={{ cx: 9.5, cy: -36, opacity: 0 }} animate={{ cx: [9.5, 12 - i * 3, 8 + i * 3], cy: [-36, -48, -62], opacity: [0, 1, 0] }} transition={{ duration: 2.2, repeat: Infinity, delay: i * 0.7, ease: 'easeOut' }} />
        ),
      )}
    </>
  ),
  // Le cèdre géant et le nid du Corbeau aux Trois Regards.
  'n3-w7': () => (
    <>
      <GiantCedar x={-6} y={12} />
      <SnowHut x={25} y={10} s={0.85} />
    </>
  ),
  // Le temple du Daruma.
  'n3-w8': () => (
    <>
      <TempleHall x={-12} y={10} />
      <Daruma x={24} y={16} s={1.25} />
    </>
  ),
  // La porte de l'aube.
  'n3-final': () => <DawnGate x={2} y={14} />,

  // ───── N2 · La Capitale de l'onmyōji ─────
  // L'observatoire du Bureau du Yin et du Yang : terrasse de pierre, sphère armillaire, étoiles.
  'n2-w1': (calm) => (
    <>
      <path d="M-34 14 L-28 -2 H28 L34 14Z" fill={STONE} />
      <path d="M-28 -2 H28 L26 -5 H-26Z" fill="#B9B2A6" />
      <path d="M-6 14 L-4 -2 H4 L6 14Z" fill="#6E6862" />
      {[-3, 2, 7, 12].map((sy) => <path key={sy} d={`M-5 ${sy} h10`} stroke="#B9B2A6" strokeWidth="1" />)}
      <g transform="translate(-13 -6)">
        <path d="M-5 0 h10 l-2 -4 h-6Z" fill={DARK_WOOD} />
        <circle cy="-15" r="11" fill="none" stroke="#C9A24A" strokeWidth="1.8" />
        <ellipse cy="-15" rx="11" ry="4" fill="none" stroke="#E2B84A" strokeWidth="1.4" />
        <ellipse cy="-15" rx="4" ry="11" fill="none" stroke="#E2B84A" strokeWidth="1.4" transform="rotate(24 0 -15)" />
        <circle cy="-15" r="2.2" fill="#F2C14E" />
      </g>
      <g transform="translate(15 -5)">
        <rect x="-9" y="-10" width="18" height="10" fill={WALL} />
        <rect x="-2.5" y="-7" width="5" height="7" fill="#3B2A1C" />
        <path d="M-14 -9 Q0 -18 14 -9 L9 -15 H-9Z" fill="#1F5C4D" />
      </g>
      {[[-30, -34, 0], [4, -40, 0.6], [30, -30, 1.2], [-8, -46, 1.8]].map(([sx, sy, d], i) => (
        <motion.path key={i} d={`M${sx} ${sy - 4} l1.2 2.8 l2.8 1.2 l-2.8 1.2 l-1.2 2.8 l-1.2 -2.8 l-2.8 -1.2 l2.8 -1.2Z`} fill="#FFF3C4" animate={calm ? undefined : { opacity: [0.3, 1, 0.3] }} transition={{ duration: 2.6, repeat: Infinity, delay: d }} />
      ))}
    </>
  ),
  // La nuit des lanternes : un char de fête, et la Lanterne-fantôme qui guette.
  'n2-w2': (calm) => (
    <>
      <g transform="translate(-10 10)">
        <rect x="-0.9" y="-58" width="1.8" height="22" fill={DARK_WOOD} />
        <path d="M0 -60 l3 4 l-3 4 l-3 -4Z" fill="#F2C14E" />
        <path d="M-9 -36 L0 -46 L9 -36Z" fill={ROOF} />
        <rect x="-8" y="-36" width="16" height="12" fill={VERMILION} />
        <rect x="-8" y="-32" width="16" height="2" fill="#F2C14E" />
        <path d="M-15 -23 Q0 -30 15 -23 L11 -27 H-11Z" fill={ROOF} />
        <rect x="-13" y="-23" width="26" height="15" fill="#8E1B26" />
        <rect x="-13" y="-18" width="26" height="3" fill="#F2C14E" />
        {[-9, -3, 3, 9].map((lx) => <ellipse key={lx} cx={lx} cy="-11" rx="2" ry="2.6" fill="#FFE2A6" stroke="#B08D3C" strokeWidth="0.5" />)}
        <rect x="-17" y="-8" width="34" height="4" fill={DARK_WOOD} />
        {[-11, 11].map((wx) => (
          <g key={wx}>
            <circle cx={wx} cy="-2" r="6.5" fill="#5A4632" stroke="#2E2018" strokeWidth="1.4" />
            <path d={`M${wx - 6} -2 h12 M${wx} -8 v12`} stroke="#2E2018" strokeWidth="1" />
            <circle cx={wx} cy="-2" r="1.6" fill="#C9A24A" />
          </g>
        ))}
      </g>
      <motion.g animate={calm ? undefined : { y: [0, -4, 0], rotate: [-5, 5, -5] }} transition={{ duration: 3, repeat: Infinity, ease: 'easeInOut' }}>
        <g transform="translate(27 -8)">
          <circle r="13" fill="#FFB65C" opacity={0.28} />
          <rect x="-4" y="-13" width="8" height="2.4" fill="#2B231D" />
          <ellipse rx="8" ry="10" fill="#FFE2A6" stroke="#B08D3C" strokeWidth="0.9" />
          <path d="M-7.6 -3 h15.2 M-7.6 3 h15.2" stroke="#D9B46A" strokeWidth="0.7" />
          <circle cy="-3" r="3.4" fill="#FFFFFF" stroke="#2B231D" strokeWidth="0.8" />
          <circle cx="0.6" cy="-3" r="1.5" fill="#2B231D" />
          <path d="M-4 4.5 Q0 7.5 4 4.5 Q3 11 0 11 Q-3 11 -4 4.5Z" fill={VERMILION} />
          <rect x="-4" y="10" width="8" height="2.4" fill="#2B231D" />
        </g>
      </motion.g>
    </>
  ),
  // Le pavillon des serments, sur l'étang aux lotus ; le masque de la Hannya veille.
  'n2-w3': () => (
    <>
      <ellipse cx="0" cy="8" rx="38" ry="15" fill="#3E97AE" opacity={0.55} />
      <ellipse cx="0" cy="8" rx="35" ry="13" fill="#6CC5D8" />
      {[[-24, 12], [-12, 17], [20, 14], [28, 6]].map(([lx, ly], i) => (
        <g key={i} transform={`translate(${lx} ${ly})`}>
          <path d="M0 0 m-4.4 0 a4.4 2.6 0 1 0 8.8 0 a4.4 2.6 0 1 0 -8.8 0 M0 0 L4 -1.6" fill="#3F8F4E" stroke="#2F7A45" strokeWidth="0.5" />
          {i % 2 === 0 && <path d="M0 -1 q-2.6 -3 0 -5.4 q2.6 2.4 0 5.4Z M0 -1 q-4 -1 -3.4 -4 q3 0.6 3.4 4Z M0 -1 q4 -1 3.4 -4 q-3 0.6 -3.4 4Z" fill="#F4A9C0" />}
        </g>
      ))}
      <g transform="translate(-2 6)">
        {[-11, -4, 4, 11].map((px) => <rect key={px} x={px - 0.9} y="-4" width="1.8" height="8" fill={DARK_WOOD} />)}
        <rect x="-15" y="-6" width="30" height="2.6" fill="#8C6A3F" />
        <rect x="-12" y="-17" width="24" height="11" fill={WALL} />
        {[-12, -4, 4, 9.6].map((px) => <rect key={px} x={px} y="-17" width="2.4" height="11" fill={VERMILION} />)}
        <path d="M-19 -16 Q0 -24 19 -16 L13 -22 H-13Z" fill="#1F5C4D" />
        <rect x="-8" y="-29" width="16" height="7" fill={WALL} />
        <path d="M-13 -28 Q0 -35 13 -28 L8 -35 H-8Z" fill="#1F5C4D" />
        <path d="M0 -35 v-5 M-2 -40 h4" stroke="#E2B84A" strokeWidth="1.4" strokeLinecap="round" />
      </g>
      <path d="M12 4 Q22 -4 32 2" stroke="#8E1B26" strokeWidth="4.4" fill="none" strokeLinecap="round" />
      <path d="M12 4 Q22 -4 32 2" stroke={VERMILION} strokeWidth="2.6" fill="none" strokeLinecap="round" />
      <g transform="translate(-30 -12)">
        <path d="M-4 -7 L-6.5 -14 L-1.6 -9.4Z M4 -7 L6.5 -14 L1.6 -9.4Z" fill="#E2B84A" />
        <path d="M-6 -6 Q0 -11 6 -6 Q7 2 0 7 Q-7 2 -6 -6Z" fill="#F6EBD3" stroke="#3B2A1C" strokeWidth="0.7" />
        <path d="M-4.4 -4.4 l3.4 1.6 M4.4 -4.4 l-3.4 1.6" stroke="#3B2A1C" strokeWidth="1.1" strokeLinecap="round" />
        <circle cx="-2.4" cy="-1.6" r="0.9" fill="#E2B84A" stroke="#3B2A1C" strokeWidth="0.4" />
        <circle cx="2.4" cy="-1.6" r="0.9" fill="#E2B84A" stroke="#3B2A1C" strokeWidth="0.4" />
        <path d="M-3.4 2 Q0 5.4 3.4 2 Q0 3.4 -3.4 2Z" fill={VERMILION} stroke="#3B2A1C" strokeWidth="0.5" />
      </g>
    </>
  ),
  // Le grand pont sous l'averse d'été, et le Kasa-obake qui sautille.
  'n2-w4': (calm) => {
    const arc = (px: number) => {
      const k = (px + 36) / 72;
      return (1 - k) * (1 - k) * 10 + 2 * k * (1 - k) * -14 + k * k * 10;
    };
    return (
      <>
        <River d="M-10 -28 Q10 -10 -4 4 T8 26" />
        <path d="M-36 10 Q0 -14 36 10" stroke="#5A4632" strokeWidth="8" fill="none" strokeLinecap="round" />
        <path d="M-36 10 Q0 -14 36 10" stroke="#B8865A" strokeWidth="5" fill="none" strokeLinecap="round" />
        {[-30, -18, -6, 6, 18, 30].map((px) => (
          <g key={px}>
            <rect x={px - 1} y={arc(px) - 10} width="2" height="9" fill="#5A4632" />
            <circle cx={px} cy={arc(px) - 11} r="1.7" fill="#C9A24A" />
          </g>
        ))}
        <path d="M-34 2 Q0 -22 34 2" stroke="#5A4632" strokeWidth="1.6" fill="none" />
        <motion.g animate={calm ? undefined : { y: [0, -7, 0] }} transition={{ duration: 0.9, repeat: Infinity, ease: 'easeOut' }}>
          <g transform="translate(4 -14)">
            <path d="M-12 -4 Q0 -24 12 -4 Q8 -7 4 -4 Q0 -7 -4 -4 Q-8 -7 -12 -4Z" fill={VERMILION} />
            <path d="M0 -17 V-4 M-6 -13 L-4 -4 M6 -13 L4 -4" stroke="#8E1B26" strokeWidth="0.7" />
            <circle cy="-10" r="3.2" fill="#FFFFFF" stroke="#2B231D" strokeWidth="0.7" />
            <circle cx="0.6" cy="-10" r="1.4" fill="#2B231D" />
            <path d="M-2.6 -5.4 Q0 -3.4 2.6 -5.4 Q2 0 0 0 Q-2 0 -2.6 -5.4Z" fill="#F4A9C0" />
            <rect x="-0.9" y="-4" width="1.8" height="9" fill="#E3CF9A" />
            <path d="M-3.4 5 h6.4 v2 h-6.4Z M-2.4 7 v2 M2 7 v2" fill={DARK_WOOD} stroke={DARK_WOOD} strokeWidth="1" />
          </g>
        </motion.g>
        {[-34, -22, -12, 18, 28, 38, -2, 10].map((rx, i) =>
          calm ? (
            <path key={i} d={`M${rx} ${-40 + (i % 3) * 9} l-3 9`} stroke="#CFEAF2" strokeWidth="1.2" strokeLinecap="round" opacity={0.7} />
          ) : (
            <motion.path key={i} d="M0 0 l-3 9" stroke="#CFEAF2" strokeWidth="1.2" strokeLinecap="round" initial={{ x: rx, y: -52, opacity: 0 }} animate={{ x: [rx, rx - 14], y: [-52, -8], opacity: [0, 0.85, 0] }} transition={{ duration: 0.9, repeat: Infinity, delay: (i * 0.23) % 0.9, ease: 'linear' }} />
          ),
        )}
      </>
    );
  },
  // La toile de la Tsuchigumo tendue sur les jardins du palais.
  'n2-w5': (calm) => (
    <>
      <TiledHouse x={-22} y={12} w={14} lit />
      <TiledHouse x={22} y={10} w={14} lit />
      <g stroke="#EAF4FF" fill="none" strokeLinecap="round">
        {[0, 1, 2, 3, 4, 5, 6, 7].map((k) => {
          const a = (k * Math.PI) / 4;
          return <path key={k} d={`M0 -18 L${Math.cos(a) * 30} ${-18 + Math.sin(a) * 22}`} strokeWidth="0.8" opacity={0.9} />;
        })}
        {[8, 16, 24].map((r) => (
          <path key={r} d={`M${r} -18 ${[1, 2, 3, 4, 5, 6, 7, 8].map((k) => { const a = (k * Math.PI) / 4; return `Q${Math.cos(a - Math.PI / 8) * r * 0.78} ${-18 + Math.sin(a - Math.PI / 8) * r * 0.58} ${Math.cos(a) * r} ${-18 + Math.sin(a) * r * 0.73}`; }).join(' ')}`} strokeWidth="0.7" opacity={0.85} />
        ))}
      </g>
      <motion.g animate={calm ? undefined : { y: [0, 5, 0] }} transition={{ duration: 3.4, repeat: Infinity, ease: 'easeInOut' }}>
        <g transform="translate(0 -18)">
          <path d="M-4 -1 L-11 -6 L-13 -1 M-4 1 L-12 3 L-13 8 M4 -1 L11 -6 L13 -1 M4 1 L12 3 L13 8 M-3 -3 L-7 -11 M3 -3 L7 -11 M-3 3 L-7 10 M3 3 L7 10" stroke="#2B231D" strokeWidth="1.2" fill="none" strokeLinecap="round" />
          <ellipse cy="2" rx="5.4" ry="6" fill="#3A2A1E" />
          <path d="M-4 1 h8 M-3.4 4 h6.8" stroke="#E2B84A" strokeWidth="1.1" />
          <circle cy="-4.6" r="3.6" fill="#2B231D" />
          <circle cx="-1.4" cy="-5" r="0.9" fill={VERMILION} />
          <circle cx="1.4" cy="-5" r="0.9" fill={VERMILION} />
        </g>
      </motion.g>
    </>
  ),
  // La salle du conseil, où le Nurarihyon boit le thé à la place d'honneur.
  'n2-w6': () => (
    <>
      <Palace x={0} y={10} s={0.95} />
      <g transform="translate(0 16)">
        <rect x="-9" y="-1" width="18" height="3" rx="1" fill="#6B4BA8" />
        <path d="M-5 -1 Q-6 -10 0 -11 Q6 -10 5 -1Z" fill="#5A6B5A" />
        <path d="M-5.4 -14 Q-9 -25 0 -25 Q9 -25 5.4 -14 Q4 -10 0 -10 Q-4 -10 -5.4 -14Z" fill="#E9DCC3" />
        <path d="M-3.4 -15 h2.4 M1 -15 h2.4" stroke="#2B231D" strokeWidth="0.9" strokeLinecap="round" />
        <path d="M-2 -12 q2 1.4 4 0" stroke="#2B231D" strokeWidth="0.7" fill="none" />
        <rect x="6" y="-7" width="4" height="3.4" rx="0.8" fill="#FFFFFF" stroke="#2F6FA8" strokeWidth="0.6" />
        <path d="M8 -8 q-1.4 -2 0 -3.4 q1.4 -1.4 0 -3" stroke="#FFFFFF" strokeWidth="0.8" fill="none" opacity={0.8} />
      </g>
    </>
  ),
  // Le couloir des paravents : le cou de la Rokurokubi s'allonge dans la nuit.
  'n2-w7': (calm) => (
    <>
      <TiledHouse x={-2} y={12} w={24} lit />
      {[-30, -20, -10].map((bx, k) => (
        <g key={bx} transform={`translate(${bx} 14)`}>
          <rect x="0" y="-13" width="9" height="14" fill={k % 2 ? '#E9DCC3' : '#F6EBD3'} stroke={DARK_WOOD} strokeWidth="0.8" />
          <path d="M2 -3 q2.4 -5 5 0" stroke="#3F8F4E" strokeWidth="0.9" fill="none" />
        </g>
      ))}
      <path d="M22 4 Q22 -1 26 -1 Q30 -1 30 4 V10 H22Z" fill="#B48CE0" />
      <path d="M22 6 h8" stroke="#F2C14E" strokeWidth="1.4" />
      <motion.g style={{ transformOrigin: '26px 0px' }} animate={calm ? undefined : { scaleY: [0.55, 1, 0.55] }} transition={{ duration: 5, repeat: Infinity, ease: 'easeInOut' }}>
        <path d="M26 0 Q36 -10 26 -20 Q14 -30 22 -42" stroke="#F6EBD3" strokeWidth="3.6" fill="none" strokeLinecap="round" />
        <g transform="translate(22 -46)">
          <path d="M-5.4 -1 Q-7 -9 0 -9 Q7 -9 5.4 -1 L6 6 L3.6 3 Q0 5 -3.6 3 L-6 6Z" fill="#1F2A44" />
          <ellipse cy="0" rx="4.2" ry="4.8" fill="#F6EBD3" />
          <path d="M-2.6 -0.6 q1 -1 2 0 M0.6 -0.6 q1 -1 2 0" stroke="#2B231D" strokeWidth="0.7" fill="none" />
          <path d="M-1 2.4 q1 0.9 2 0" stroke={VERMILION} strokeWidth="0.9" fill="none" />
        </g>
      </motion.g>
    </>
  ),
  // Les appartements de la favorite : derrière le store, neuf queues de renard.
  'n2-w8': (calm) => (
    <>
      <motion.g style={{ transformOrigin: '0px 4px' }} animate={calm ? undefined : { rotate: [-3, 3, -3] }} transition={{ duration: 4, repeat: Infinity, ease: 'easeInOut' }}>
        {[-4, -3, -2, -1, 0, 1, 2, 3, 4].map((k) => (
          <g key={k} transform={`rotate(${k * 21} 0 4)`}>
            <path d="M-3 4 Q-7 -22 0 -40 Q7 -22 3 4Z" fill="#F2B24E" />
            <path d="M-2.4 -26 Q0 -40 2.4 -26 Q0 -22 -2.4 -26Z" fill="#FFFFFF" />
          </g>
        ))}
      </motion.g>
      <g transform="translate(0 10)">
        <path d="M-8 2 Q-9 -12 0 -13 Q9 -12 8 2Z" fill={VERMILION} />
        <path d="M-8 2 Q-4 -4 0 2 Q4 -4 8 2Z" fill="#8E1B26" />
        <path d="M-5 -17 L-7.4 -26 L-1.6 -21Z M5 -17 L7.4 -26 L1.6 -21Z" fill="#F2B24E" />
        <path d="M-6 -16 Q0 -24 6 -16 Q5 -10 0 -7 Q-5 -10 -6 -16Z" fill="#FFF6E0" />
        <path d="M-3.6 -15.4 l2.4 1 M3.6 -15.4 l-2.4 1" stroke="#2B231D" strokeWidth="0.9" strokeLinecap="round" />
        <path d="M-1 -10.6 h2 l-1 1.4Z" fill="#2B231D" />
        <path d="M-6.4 -18 Q0 -27 6.4 -18 Q0 -21 -6.4 -18Z" fill="#1F2A44" />
        <circle cy="-23.4" r="1.6" fill="#F2C14E" />
      </g>
    </>
  ),
  // La grande salle d'audience du palais impérial.
  'n2-final': () => (
    <>
      <circle cx="0" cy="-16" r="26" fill="#FFD27A" opacity={0.2} />
      <Palace x={0} y={14} s={1.12} lit />
      <Nobori x={-42} y={16} s={0.85} color="#1F7A66" />
      <Nobori x={36} y={16} s={0.85} color="#1F7A66" />
    </>
  ),

  // ───── N1 · Le Règne du shōgun ─────
  // La cérémonie de succession : grande salle, et le sceau d'État qui s'abat sur le décret.
  'n1-w1': (calm) => (
    <>
      <Palace x={-10} y={12} s={0.85} lit />
      <g transform="translate(26 10)">
        <rect x="-11" y="-3" width="22" height="9" rx="1" fill="#FFF6E0" stroke="#B08D3C" strokeWidth="0.8" />
        {[-6, -2, 2].map((ly) => <path key={ly} d={`M-8 ${ly + 1} h11`} stroke="#3B2A1C" strokeWidth="0.7" />)}
        <motion.g animate={calm ? undefined : { y: [-10, 0, 0, -10] }} transition={{ duration: 2.4, repeat: Infinity, times: [0, 0.3, 0.7, 1] }}>
          <rect x="-1" y="-22" width="9" height="12" rx="2" fill="#8C6A3F" />
          <rect x="-2" y="-11" width="11" height="5" rx="1" fill="#C8323F" />
          <circle cx="3.5" cy="-24" r="3" fill="#C9A24A" />
        </motion.g>
        <rect x="3" y="0" width="6" height="5" fill="#C8323F" opacity={0.85} />
      </g>
    </>
  ),
  // Le conseil des daimyō, sous l'ombre de l'Ōnyūdō qui grandit.
  'n1-w2': (calm) => (
    <>
      <motion.g style={{ transformOrigin: '0px 10px' }} animate={calm ? undefined : { scale: [0.85, 1.08, 0.85] }} transition={{ duration: 5, repeat: Infinity, ease: 'easeInOut' }}>
        <path d="M-26 10 Q-28 -30 0 -40 Q28 -30 26 10Z" fill="#3B3550" opacity={0.85} />
        <circle cy="-44" r="13" fill="#4A4363" />
        <circle cx="-4.6" cy="-45" r="1.8" fill="#FFD27A" />
        <circle cx="4.6" cy="-45" r="1.8" fill="#FFD27A" />
        <path d="M-16 -22 Q0 -14 16 -22" stroke="#2B263A" strokeWidth="2" fill="none" />
      </motion.g>
      <Dojo x={0} y={12} s={1.05} lit />
      <Nobori x={-34} y={16} s={0.8} color="#A87A1E" />
      <Nobori x={30} y={16} s={0.8} color="#A87A1E" />
    </>
  ),
  // Le col sous la tempête : le cortège avance, Fūjin souffle depuis son nuage.
  'n1-w3': (calm) => (
    <>
      <Peak x={-24} y={14} w={22} h={40} fill="#5C5A80" />
      <Peak x={26} y={14} w={20} h={34} fill="#5C5A80" />
      <path d="M-30 18 Q0 4 30 16" stroke="#EBD9AE" strokeWidth="3.4" strokeDasharray="5 4" fill="none" strokeLinecap="round" />
      {[-14, -4, 6].map((nx, k) => <Nobori key={nx} x={nx} y={14 - k * 2} s={0.55} color="#A87A1E" />)}
      <g transform="translate(-6 -38)">
        <ellipse rx="16" ry="6" fill="#C9D3F0" />
        <circle cy="-8" r="6" fill="#6FAE4F" />
        <circle cx="-2" cy="-9" r="0.9" fill="#2B231D" />
        <circle cx="2" cy="-9" r="0.9" fill="#2B231D" />
        <path d="M-12 -14 Q0 -26 12 -14" stroke="#F2E3B3" strokeWidth="3.4" fill="none" strokeLinecap="round" />
      </g>
      {[0, 1, 2].map((k) => (
        <motion.path key={k} d={`M${10 + k * 4} ${-34 + k * 8} q10 -6 20 0 t20 0`} stroke="#FFFFFF" strokeWidth="1.6" fill="none" strokeLinecap="round" opacity={0.75} animate={calm ? undefined : { x: [0, 14, 0], opacity: [0.2, 0.9, 0.2] }} transition={{ duration: 1.8, repeat: Infinity, delay: k * 0.4 }} />
      ))}
    </>
  ),
  // Le tribunal : Enma siège derrière sa table, le miroir de vérité à ses côtés.
  'n1-w4': () => (
    <>
      <TempleHall x={0} y={10} />
      <g transform="translate(0 2)">
        <rect x="-10" y="-2" width="20" height="8" fill="#5A2A24" />
        <path d="M-6 -2 Q-7 -14 0 -15 Q7 -14 6 -2Z" fill="#C8323F" />
        <circle cy="-19" r="5" fill="#D9534F" />
        <path d="M-6 -23 h12 v-5 h-12Z" fill="#1A1414" />
        <text y="-25.4" dy="0.36em" textAnchor="middle" fontSize="4.2" fontWeight="900" className="jp" fill="#F2C14E">王</text>
        <path d="M-2.4 -19 h1.6 M0.8 -19 h1.6" stroke="#1A1414" strokeWidth="1" />
        <path d="M-3 -15.6 q3 2 6 0" stroke="#1A1414" strokeWidth="0.9" fill="none" />
      </g>
      <g transform="translate(-30 14)">
        <rect x="-1" y="-14" width="2" height="14" fill={DARK_WOOD} />
        <circle cy="-20" r="7" fill="#C9A24A" />
        <circle cy="-20" r="5" fill="#E8F4FF" />
      </g>
      <g transform="translate(30 14)">
        <rect x="-4" y="-8" width="8" height="8" fill="#FFF6E0" stroke="#3B2A1C" strokeWidth="0.6" />
        <path d="M5 -10 L9 -16" stroke="#C8323F" strokeWidth="1.6" strokeLinecap="round" />
      </g>
    </>
  ),
  // La forêt des échos : grands cèdres, et un Kodama qui hoche la tête en résonnant.
  'n1-w5': (calm) => (
    <>
      <GiantCedar x={-24} y={14} s={0.75} />
      <GiantCedar x={22} y={12} s={0.65} />
      <motion.g animate={calm ? undefined : { rotate: [-12, 12, -12] }} style={{ transformOrigin: '0px 12px' }} transition={{ duration: 1.6, repeat: Infinity, ease: 'easeInOut' }}>
        <g transform="translate(0 12)">
          <path d="M-5 0 Q-6 -10 0 -10 Q6 -10 5 0Z" fill="#F4F0E6" />
          <circle cy="-14" r="6" fill="#F4F0E6" />
          <circle cx="-2.2" cy="-14.6" r="1.1" fill="#2B231D" />
          <circle cx="2.2" cy="-14.6" r="1.1" fill="#2B231D" />
          <ellipse cy="-11.4" rx="1" ry="1.4" fill="#2B231D" />
        </g>
      </motion.g>
      {[0, 1, 2].map((k) => (
        <motion.circle key={k} cx="0" cy="-2" r={8 + k * 7} fill="none" stroke="#F6E7C1" strokeWidth="1" animate={calm ? undefined : { opacity: [0, 0.8, 0], scale: [0.6, 1.3, 1.6] }} style={{ transformOrigin: '0px -2px' }} transition={{ duration: 2.2, repeat: Infinity, delay: k * 0.7 }} opacity={calm ? 0.4 : 0} />
      ))}
    </>
  ),
  // Le port de l'ouest : quai, navire marchand, et la tête de l'Umibōzu qui sort de l'eau.
  'n1-w6': (calm) => (
    <>
      <ellipse cx="18" cy="10" rx="24" ry="11" fill="#3E5B8A" />
      <motion.g animate={calm ? undefined : { y: [0, -4, 0] }} transition={{ duration: 3, repeat: Infinity, ease: 'easeInOut' }}>
        <g transform="translate(24 6)">
          <path d="M-12 4 Q-12 -14 0 -16 Q12 -14 12 4Z" fill="#1E2340" />
          <circle cx="-4" cy="-6" r="2.4" fill="#FFF6E0" />
          <circle cx="4" cy="-6" r="2.4" fill="#FFF6E0" />
          <circle cx="-4" cy="-6" r="1.1" fill="#C8323F" />
          <circle cx="4" cy="-6" r="1.1" fill="#C8323F" />
          <path d="M-14 4 q7 -4 14 0 t14 0" stroke="#CFEAF2" strokeWidth="1.4" fill="none" />
        </g>
      </motion.g>
      <rect x="-36" y="4" width="28" height="4" fill="#8C6A3F" />
      {[-32, -22, -12].map((px) => <rect key={px} x={px} y="8" width="2" height="7" fill="#5A4632" />)}
      <g transform="translate(-20 -2)">
        <path d="M-12 4 L12 4 L8 10 L-8 10Z" fill="#6B4A32" />
        <rect x="-0.8" y="-22" width="1.6" height="26" fill="#3B2A1C" />
        <path d="M-9 -20 H9 V-2 H-9Z" fill="#F6E7C1" stroke="#B08D3C" strokeWidth="0.6" />
        {[-15, -10, -5].map((ly) => <path key={ly} d={`M-9 ${ly} H9`} stroke="#B08D3C" strokeWidth="0.6" />)}
      </g>
      <g transform="translate(-34 -8)">
        <ellipse rx="4" ry="5" fill="#B8865A" />
        <path d="M-4 -2 h8 M-4 2 h8" stroke="#6B4A32" strokeWidth="0.8" />
      </g>
    </>
  ),
  // Le siège : la muraille du château rebelle, et le grand squelette qui la surplombe.
  'n1-w7': (calm) => (
    <>
      <motion.g animate={calm ? undefined : { y: [0, -3, 0] }} transition={{ duration: 4, repeat: Infinity, ease: 'easeInOut' }}>
        <g transform="translate(0 -30)" fill="#ECE6D6" stroke="#9A9282" strokeWidth="0.8">
          <path d="M-11 -6 Q-11 -20 0 -20 Q11 -20 11 -6 Q11 2 6 4 L6 8 L-6 8 L-6 4 Q-11 2 -11 -6Z" />
          <ellipse cx="-4.6" cy="-8" rx="3" ry="3.6" fill="#2B263A" stroke="none" />
          <ellipse cx="4.6" cy="-8" rx="3" ry="3.6" fill="#2B263A" stroke="none" />
          <path d="M-1 -3 L0 -1 L1 -3Z" fill="#2B263A" stroke="none" />
          {[-4, -1.4, 1.4, 4].map((tx) => <rect key={tx} x={tx - 1} y="4" width="2" height="3" />)}
          <path d="M-26 22 Q-22 6 -12 10 M26 22 Q22 6 12 10" fill="none" strokeWidth="3" strokeLinecap="round" />
          <circle cx="-4.6" cy="-8" r="1" fill="#FF6A4D" stroke="none" />
          <circle cx="4.6" cy="-8" r="1" fill="#FF6A4D" stroke="none" />
        </g>
      </motion.g>
      <g transform="translate(-2 14)"><Rampart w={30} /></g>
      <GateHouse x={-2} y={14} />
      <Nobori x={-34} y={18} s={0.8} color="#1A1414" />
      <Nobori x={30} y={18} s={0.8} color="#A87A1E" />
    </>
  ),
  // Le discours au peuple : estrade sur la grève, foule, et Ryūjin qui se dresse au large.
  'n1-w8': (calm) => (
    <>
      <motion.g animate={calm ? undefined : { y: [0, -5, 0] }} transition={{ duration: 4.5, repeat: Infinity, ease: 'easeInOut' }}>
        <g transform="translate(22 -14)">
          <path d="M-6 26 C-14 10 4 2 -2 -10 C-6 -18 4 -26 10 -22" stroke="#2E8B6A" strokeWidth="6" fill="none" strokeLinecap="round" />
          <path d="M-6 26 C-14 10 4 2 -2 -10 C-6 -18 4 -26 10 -22" stroke="#F2C14E" strokeWidth="1.2" strokeDasharray="2 3" fill="none" />
          <g transform="translate(12 -24)">
            <path d="M-6 0 Q0 -8 8 -2 L10 2 L2 4 Q-4 4 -6 0Z" fill="#2E8B6A" />
            <circle cx="2" cy="-2.6" r="1.2" fill="#F2C14E" />
            <path d="M-2 -6 l-4 -6 M2 -7 l0 -7" stroke="#F2C14E" strokeWidth="1.2" strokeLinecap="round" />
            <path d="M9 2 q6 3 9 0" stroke="#F6E7C1" strokeWidth="0.9" fill="none" />
          </g>
        </g>
      </motion.g>
      <g transform="translate(-10 12)">
        <rect x="-12" y="-4" width="24" height="7" fill="#8C6A3F" />
        <rect x="-12" y="-6" width="24" height="2" fill="#C8323F" />
        <g transform="translate(0 -6)">
          <path d="M-3.4 0 L-4 -9 Q0 -11 4 -9 L3.4 0Z" fill="#A87A1E" />
          <circle cy="-12.4" r="2.6" fill="#F6E7C1" />
          <path d="M-3 -14 l3 -3 l3 3Z" fill="#1A1414" />
          <path d="M4 -8 l6 -4" stroke="#F6E7C1" strokeWidth="1.4" strokeLinecap="round" />
        </g>
      </g>
      {[-34, -28, -22, -16, -6, 2].map((px, k) => (
        <g key={px} transform={`translate(${px} ${20 + (k % 2) * 2})`}>
          <circle cy="-6" r="2.2" fill="#2B231D" />
          <path d="M-2.6 0 Q0 -5 2.6 0Z" fill={['#3E5B8A', '#C8323F', '#6FAE4F'][k % 3]} />
        </g>
      ))}
    </>
  ),
  // Le premier lever de soleil : le château du shōgun devant le soleil du Nouvel An.
  'n1-final': () => (
    <>
      <circle cx="2" cy="-20" r="30" fill="#FFD27A" opacity={0.25} />
      <circle cx="2" cy="-20" r="17" fill="#FF8A5C" />
      <circle cx="2" cy="-20" r="13" fill="#FFB27A" />
      <Castle x={2} y={20} s={1.1} lit />
      <g transform="translate(-36 18)">
        <rect x="-1" y="-14" width="2" height="14" fill="#3B2A1C" />
        <circle cy="-17" r="4" fill="#E0566E" />
        <circle cx="-4" cy="-13" r="3" fill="#B83A55" />
        <circle cx="4" cy="-14" r="3" fill="#E0566E" />
      </g>
      <Nobori x={34} y={18} s={0.85} color="#A87A1E" />
    </>
  ),
};

/** Décor du chapitre de cette île, ou `null` hors mode histoire. */
export function storyScene(worldSlug: string, calm: boolean): ReactNode | null {
  return (SCENES[worldSlug] ?? KOREAN_SCENES[worldSlug] ?? ENGLISH_SCENES[worldSlug] ?? CHINESE_SCENES[worldSlug] ?? SPANISH_SCENES[worldSlug] ?? GERMAN_SCENES[worldSlug])?.(calm) ?? null;
}
export const hasStoryScene = (worldSlug: string) => worldSlug in SCENES;
