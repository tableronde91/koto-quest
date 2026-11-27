import { useDecor } from './StudyLanguage';
import { createContext, useContext, useEffect, useMemo, useRef } from 'react';
import { motion } from 'motion/react';
import type { AvatarConfig, PathWorldDto } from '@koto/shared';
import { Avatar } from './Avatar';
import { useCalm } from './Celebrate';
import { T } from '../i18n';
import { storyScene } from './StoryScenes';
import { Bamboo, Castle, DawnGate, Hut, Lanterns, Pagoda, Torii, SAKURA, LEAF, WOOD, VERMILION, ROCK, ROCK_DARK } from './MapParts';

/**
 * Carte du niveau en archipel : chaque monde est une île, reliée à la suivante par un chemin
 * lumineux (ou un pont quand elles sont proches). Le personnage se tient sur l'île en cours ;
 * toucher une île fait défiler jusqu'à ses leçons. Illustration 100 % vectorielle et originale.
 */
const W = 1000;
const H = 600;

/** Gabarit de 9 emplacements, du sud-ouest au sud-est en serpentant (comme un parcours de jeu de plateau). */
const SLOTS = [
  { x: 150, y: 440 },
  { x: 360, y: 375 },
  { x: 175, y: 230 },
  { x: 385, y: 125 },
  { x: 590, y: 110 },
  { x: 575, y: 300 },
  { x: 680, y: 450 },
  { x: 820, y: 235 },
  { x: 900, y: 440 },
];
function islandPositions(n: number) {
  // Mêmes emplacements pour tous les niveaux : les îles restantes apparaissent dans la brume (contenu à venir).
  if (n <= 9) return SLOTS.slice(0, n).map((p, i) => ({ ...p, slot: i }));
  // Au-delà de 9 mondes : grille en serpentin.
  const cols = Math.ceil(n / 3);
  return Array.from({ length: n }, (_, i) => {
    const row = Math.floor(i / cols);
    const col = row % 2 === 0 ? i % cols : cols - 1 - (i % cols);
    return { x: 110 + (col * (W - 220)) / Math.max(1, cols - 1), y: 470 - row * 170, slot: i % 9 };
  });
}

export type WorldState = 'done' | 'current' | 'open' | 'soon';

export function worldStates(worlds: PathWorldDto[]): WorldState[] {
  const finished = (w: PathWorldDto) => !w.comingSoon && w.progress.completed === w.progress.total && (!w.boss || w.boss.defeated) && (!w.exam || w.exam.passed);
  let currentIdx = worlds.findIndex((w) => !w.comingSoon && !w.optional && !finished(w));
  if (currentIdx < 0) currentIdx = worlds.findIndex((w) => !w.comingSoon && !finished(w));
  return worlds.map((w, i) => (w.comingSoon ? 'soon' : finished(w) ? 'done' : i === currentIdx ? 'current' : 'open'));
}

// ───────────── Formes ─────────────

/** Petit générateur déterministe : la même île garde la même forme d'un affichage à l'autre. */
function rng(seed: number) {
  let s = seed * 9301 + 49297;
  return () => {
    s = (s * 9301 + 49297) % 233280;
    return s / 233280;
  };
}

/** Contour organique fermé (courbes lissées autour d'un centre). */
function blob(cx: number, cy: number, rx: number, ry: number, seed: number, wobble = 0.18, n = 10) {
  const r = rng(seed);
  const pts = Array.from({ length: n }, (_, i) => {
    const a = (i / n) * Math.PI * 2;
    const k = 1 - wobble / 2 + r() * wobble;
    return [cx + Math.cos(a) * rx * k, cy + Math.sin(a) * ry * k];
  });
  const mid = (a: number[], b: number[]) => [(a[0] + b[0]) / 2, (a[1] + b[1]) / 2];
  let d = `M${mid(pts[n - 1], pts[0]).join(' ')}`;
  pts.forEach((p, i) => {
    const m = mid(p, pts[(i + 1) % n]);
    d += ` Q${p[0].toFixed(1)} ${p[1].toFixed(1)} ${m[0].toFixed(1)} ${m[1].toFixed(1)}`;
  });
  return `${d}Z`;
}

// ───────────── Décors ─────────────

// ───────────── Ambiance de chaque niveau ─────────────
// N5 : printemps lumineux (cerisiers, soleil). N4 : automne au crépuscule, plus sobre (érables, pins, lune, brume).
interface MapTheme {
  id: 'spring' | 'summer' | 'autumn' | 'winter' | 'newyear' | 'korea' | 'albion' | 'china' | 'spain' | 'germany';
  sea: [string, string, string];
  waves: number;
  horizon: string;
  shallow: string;
  shallowOpacity: number;
  grass: [string, string];
  sand: string;
  blossom: string;
  blossomDark: string;
  leaf: string;
  leafDark: string;
  cloud: string;
  cloudOpacity: number;
  foam: number;
  path: string;
  particles: string[];
  banner: { fill: string; stroke: string; text: string; seal: string };
  plaque: { fill: string; stroke: string; text: string; accent: string };
  sail: string;
  dusk: boolean;
  /** Pétales (azalées, forsythias) au lieu de feuilles d'érable */
  petals?: boolean;
  /** Lucioles d'été au lieu de feuilles d'érable */
  fireflies?: boolean;
  /** Flocons de neige au lieu de feuilles d'érable */
  snow?: boolean;
}

const SPRING: MapTheme = {
  id: 'spring',
  sea: ['#1E6F8E', '#1A8C9C', '#127A86'],
  waves: 0.1,
  horizon: '#2E5E57',
  shallow: '#5FD1C9',
  shallowOpacity: 0.35,
  grass: ['#6FA85A', '#5B9A4C'],
  sand: '#EBD9AE',
  blossom: '#F4A9C0',
  blossomDark: '#E07A9B',
  leaf: '#4E8B4A',
  leafDark: '#356B3A',
  cloud: '#FFFFFF',
  cloudOpacity: 0.85,
  foam: 0.6,
  path: '#FFF3C4',
  particles: ['#F4A9C0'],
  banner: { fill: '#F6EBD3', stroke: '#7A4E2D', text: '#3B2A1C', seal: '#8E1B26' },
  plaque: { fill: '#F6EBD3', stroke: '#7A4E2D', text: '#3B2A1C', accent: '#C8323F' },
  sail: '#C8323F',
  dusk: false,
};

const AUTUMN: MapTheme = {
  id: 'autumn',
  sea: ['#1B2A40', '#22394F', '#1A3044'],
  waves: 0.06,
  horizon: '#141F2B',
  shallow: '#6F928F',
  shallowOpacity: 0.18,
  grass: ['#857A47', '#6C663E'],
  sand: '#CDBB94',
  blossom: '#C4472B',
  blossomDark: '#8F2E1E',
  leaf: '#2F5240',
  leafDark: '#1F392C',
  cloud: '#AEB7C2',
  cloudOpacity: 0.35,
  foam: 0.3,
  path: '#E6D3A0',
  particles: ['#C4472B', '#D9822B', '#9E3424'],
  banner: { fill: '#1E1B22', stroke: '#B08D3C', text: '#EBDDB5', seal: '#9E3424' },
  plaque: { fill: '#2B2622', stroke: '#8E7445', text: '#EFE3C8', accent: '#E2A23B' },
  sail: '#5A4632',
  dusk: true,
};

// N3 : nuit de neige dans le monde des esprits, juste avant l'aube (îles blanches sur une mer indigo, lueurs bleues).
const WINTER: MapTheme = {
  id: 'winter',
  sea: ['#1F2552', '#2B3470', '#3A3A7C'],
  waves: 0.08,
  horizon: '#161B40',
  shallow: '#9FD8FF',
  shallowOpacity: 0.2,
  grass: ['#F3F7FA', '#DCE7EE'],
  sand: '#BFCBDD',
  blossom: '#FFFFFF',
  blossomDark: '#C9D9E4',
  leaf: '#2E5A4C',
  leafDark: '#1E4236',
  cloud: '#C9D3F0',
  cloudOpacity: 0.28,
  foam: 0.55,
  path: '#BFE8FF',
  particles: ['#FFFFFF'],
  banner: { fill: '#1B2148', stroke: '#9FD8FF', text: '#EAF4FF', seal: '#2F6FA8' },
  plaque: { fill: '#F4F8FB', stroke: '#2F4A66', text: '#1F3247', accent: '#2F6FA8' },
  sail: '#2F6FA8',
  dusk: false,
};

// N2 : soir d'été dans la capitale (eau de jade, verdure dense, hortensias, lucioles, feux d'artifice).
const SUMMER: MapTheme = {
  id: 'summer',
  sea: ['#0F5E5A', '#15786A', '#1C8C76'],
  waves: 0.09,
  horizon: '#0B4440',
  shallow: '#8EE6C4',
  shallowOpacity: 0.3,
  grass: ['#3F9150', '#2F7A45'],
  sand: '#E6D4A0',
  blossom: '#8FA8F0',
  blossomDark: '#B48CE0',
  leaf: '#2F7A45',
  leafDark: '#1F5C36',
  cloud: '#FFF3D6',
  cloudOpacity: 0.7,
  foam: 0.5,
  path: '#FFE9A8',
  particles: ['#E9FF8A'],
  banner: { fill: '#0E3B36', stroke: '#E2B84A', text: '#F6EBD3', seal: '#C8323F' },
  plaque: { fill: '#F6EBD3', stroke: '#1F5C4D', text: '#17352F', accent: '#1F7A66' },
  sail: '#F2C14E',
  dusk: false,
};

// N1 : aube du Nouvel An sur le domaine du shōgun (nuit violette qui s'embrase d'or, pins, pruniers en fleur, paillettes d'or).
const NEWYEAR: MapTheme = {
  id: 'newyear',
  sea: ['#1E2348', '#3E3A6E', '#9C5E72'],
  waves: 0.08,
  horizon: '#15193A',
  shallow: '#FFD9A0',
  shallowOpacity: 0.22,
  grass: ['#4E7A4A', '#3E6A3E'],
  sand: '#E9D7B0',
  blossom: '#E0566E',
  blossomDark: '#B83A55',
  leaf: '#2F5A3A',
  leafDark: '#1F4229',
  cloud: '#F6D9B8',
  cloudOpacity: 0.4,
  foam: 0.5,
  path: '#FFD27A',
  particles: ['#F2C14E'],
  banner: { fill: '#1A1414', stroke: '#D4A537', text: '#F6E7C1', seal: '#C8323F' },
  plaque: { fill: '#FFF8E6', stroke: '#8A6A2A', text: '#2B1F0E', accent: '#C8323F' },
  sail: '#C8323F',
  dusk: false,
};

// A1 : printemps d'Albion (mer grise de la Manche, collines vert vif, bruyère et ajoncs, ciel de nuages).
const ALBION: MapTheme = {
  id: 'albion',
  sea: ['#4A6E85', '#557C93', '#628AA0'],
  waves: 0.12,
  horizon: '#3B5A6E',
  shallow: '#A9D2D6',
  shallowOpacity: 0.26,
  grass: ['#6FA84E', '#5B9340'],
  sand: '#E6DCC0',
  blossom: '#A97BD6',
  blossomDark: '#E9C23B',
  leaf: '#3E7A3A',
  leafDark: '#2C5A2A',
  cloud: '#FFFFFF',
  cloudOpacity: 0.85,
  foam: 0.6,
  path: '#F2E2B0',
  particles: ['#A97BD6', '#E9C23B', '#FFFFFF'],
  banner: { fill: '#1F3A5F', stroke: '#C8A24A', text: '#F6EBD3', seal: '#C8323F' },
  plaque: { fill: '#F6EBD3', stroke: '#2E6B4F', text: '#1F2A24', accent: '#C8323F' },
  sail: '#1F3A5F',
  dusk: false,
};

// TOPIK 1 : automne lumineux sur la péninsule (mer bleue, érables rouges du Seoraksan, couleurs du dancheong).
const KOREA: MapTheme = {
  id: 'korea',
  sea: ['#2B6FA0', '#3584B3', '#3F95BF'],
  waves: 0.1,
  horizon: '#1F5680',
  shallow: '#9FE0E6',
  shallowOpacity: 0.28,
  grass: ['#6E9A55', '#5A874A'],
  sand: '#E9D9B0',
  blossom: '#D9483B',
  blossomDark: '#E8772E',
  leaf: '#3F6E45',
  leafDark: '#2C5233',
  cloud: '#FFFFFF',
  cloudOpacity: 0.75,
  foam: 0.55,
  path: '#FFE3A0',
  particles: ['#D9483B', '#E8772E', '#E2B84A'],
  banner: { fill: '#1F5C52', stroke: '#E2B84A', text: '#F6EBD3', seal: '#B23A3A' },
  plaque: { fill: '#F6EBD3', stroke: '#2E8B7A', text: '#1F3D37', accent: '#B23A3A' },
  sail: '#B23A3A',
  dusk: false,
};

// HSK : la plaine du Fleuve jaune au temps des Royaumes combattants (eaux de jade, fleurs de prunier, laque vermillon et or).
const CHINA: MapTheme = {
  id: 'china',
  sea: ['#2F7A6E', '#3A8C7C', '#47A08A'],
  waves: 0.1,
  horizon: '#5A4A3A',
  shallow: '#E9D9A0',
  shallowOpacity: 0.3,
  grass: ['#8FA65A', '#7A944A'],
  sand: '#E9CF9A',
  blossom: '#E25A6A',
  blossomDark: '#B23A4A',
  leaf: '#4E6E3A',
  leafDark: '#3A552A',
  cloud: '#FFF6E6',
  cloudOpacity: 0.8,
  foam: 0.55,
  path: '#F2D58A',
  particles: ['#F4B6C2', '#E25A6A', '#FFFFFF'],
  banner: { fill: '#8E1B26', stroke: '#E2B84A', text: '#FFF3DC', seal: '#E2B84A' },
  plaque: { fill: '#FFF3DC', stroke: '#8E1B26', text: '#3A1A14', accent: '#2F7A6E' },
  sail: '#8E1B26',
  dusk: false,
  petals: true,
};

// DELE : la Manche en été (mer Méditerranée profonde, plaines ocre, oliviers, coquelicots, or et rouge de Castille).
const SPAIN: MapTheme = {
  id: 'spain',
  sea: ['#1F5A8E', '#2A6FA3', '#3584B8'],
  waves: 0.1,
  horizon: '#1A4A72',
  shallow: '#9FD8E6',
  shallowOpacity: 0.28,
  grass: ['#B8A24E', '#A08C3E'],
  sand: '#EBD49A',
  blossom: '#D9483B',
  blossomDark: '#E2B84A',
  leaf: '#6E7A3A',
  leafDark: '#535E2A',
  cloud: '#FFFFFF',
  cloudOpacity: 0.7,
  foam: 0.55,
  path: '#F6E2A8',
  particles: ['#D9483B', '#E2B84A', '#FFFFFF'],
  banner: { fill: '#8E1B26', stroke: '#E2B84A', text: '#FFF3DC', seal: '#E2B84A' },
  plaque: { fill: '#FFF6E0', stroke: '#B8562E', text: '#3A1F10', accent: '#C8323F' },
  sail: '#C8323F',
  dusk: false,
  petals: true,
};

// Goethe-Zertifikat : la Route des contes (rivières sombres de Hesse, prairies et forêts profondes, toits rouges des maisons à colombages, or des contes).
const GERMANY: MapTheme = {
  id: 'germany',
  sea: ['#2E5A6E', '#3A6B7E', '#477C8E'],
  waves: 0.1,
  horizon: '#24485A',
  shallow: '#A8D8D0',
  shallowOpacity: 0.26,
  grass: ['#5E9A4A', '#4A853C'],
  sand: '#E2D6B4',
  blossom: '#C8323F',
  blossomDark: '#E2B84A',
  leaf: '#2F6B4F',
  leafDark: '#1F4A36',
  cloud: '#FFFFFF',
  cloudOpacity: 0.8,
  foam: 0.55,
  path: '#F2E2B0',
  particles: ['#E2B84A', '#C8323F', '#FFFFFF'],
  banner: { fill: '#1F4A36', stroke: '#E2B84A', text: '#FFF6E0', seal: '#C8323F' },
  plaque: { fill: '#FFF6E0', stroke: '#2F6B4F', text: '#1F2A24', accent: '#C8323F' },
  sail: '#2F6B4F',
  dusk: false,
};

// TOPIK 2 : printemps coréen (azalées roses et forsythias jaunes sur les collines, mer turquoise, couleurs du dancheong).
const KOREA_SPRING: MapTheme = {
  ...KOREA,
  sea: ['#1F7F92', '#2696A3', '#2FA6AE'],
  horizon: '#1D6475',
  shallow: '#A8F0E0',
  grass: ['#7FB063', '#6A9D52'],
  blossom: '#E9709A',
  blossomDark: '#F2C230',
  particles: ['#F29BB8', '#E9709A', '#F2C230'],
  banner: { fill: '#4A2E5C', stroke: '#E2B84A', text: '#F6EBD3', seal: '#B23A3A' },
  plaque: { fill: '#F8EEF3', stroke: '#8E5BA8', text: '#3A2347', accent: '#B23A3A' },
  sail: '#8E5BA8',
  petals: true,
};

// TOPIK 3 : soir d'été sous les Joseon (mer de jade, rizières vertes, lotus, lucioles, lanternes du banquet).
const KOREA_SUMMER: MapTheme = {
  ...KOREA,
  sea: ['#14564F', '#1C6E62', '#25806E'],
  horizon: '#0F423C',
  shallow: '#8EE6C4',
  grass: ['#4E9A4E', '#3F8A45'],
  blossom: '#F29BB8',
  blossomDark: '#E36A5A',
  cloud: '#FFE9C4',
  cloudOpacity: 0.55,
  particles: ['#E9FF8A'],
  banner: { fill: '#5A2A1A', stroke: '#E2B84A', text: '#F6EBD3', seal: '#B5562E' },
  plaque: { fill: '#F6EBD3', stroke: '#B5562E', text: '#3A1F14', accent: '#2E8B7A' },
  sail: '#B5562E',
  fireflies: true,
};

// TOPIK 4 : hiver coréen (mer d'ardoise, îles enneigées, pins, flocons).
const KOREA_WINTER: MapTheme = {
  ...KOREA,
  sea: ['#3E5C7A', '#4E6E8C', '#5E7E9A'],
  horizon: '#2E4A66',
  shallow: '#D8ECF6',
  grass: ['#E8EEF2', '#D6E0E8'],
  blossom: '#C8323F',
  blossomDark: '#9A2230',
  cloud: '#FFFFFF',
  cloudOpacity: 0.7,
  particles: ['#FFFFFF'],
  banner: { fill: '#1F2F45', stroke: '#C9D6E2', text: '#F2F6FA', seal: '#C8323F' },
  plaque: { fill: '#F2F6FA', stroke: '#3E5C8A', text: '#1F2F45', accent: '#C8323F' },
  sail: '#3E5C8A',
  snow: true,
};

// TOPIK 5 : crépuscule des esprits (mer violette, îles de brume, fleurs de résurrection, lueurs d'âmes).
const KOREA_SPIRIT: MapTheme = {
  ...KOREA,
  sea: ['#2E2350', '#3A2E66', '#4A3A7A'],
  horizon: '#1F1838',
  shallow: '#C9A6F2',
  grass: ['#6A8A6A', '#5A7A5E'],
  blossom: '#C9A6F2',
  blossomDark: '#8E6AC2',
  cloud: '#E9DDF6',
  cloudOpacity: 0.5,
  particles: ['#E9DDF6', '#C9A6F2', '#FFE9A8'],
  banner: { fill: '#3A2A5A', stroke: '#C9A6F2', text: '#F3EEFA', seal: '#6A4C93' },
  plaque: { fill: '#F3EEFA', stroke: '#6A4C93', text: '#2A1F44', accent: '#C8323F' },
  sail: '#6A4C93',
  fireflies: true,
};

// TOPIK 6 : aube du premier royaume (mer dorée, monts sacrés, poussière d'or du ciel).
const KOREA_DAWN: MapTheme = {
  ...KOREA,
  sea: ['#2F5D7A', '#4A7A8A', '#C9A06A'],
  horizon: '#E2A65A',
  shallow: '#F6E3A8',
  grass: ['#7A9A4E', '#6A8A42'],
  blossom: '#E7B53B',
  blossomDark: '#A57E22',
  cloud: '#FFF0D0',
  cloudOpacity: 0.75,
  particles: ['#F2D94E', '#FFE9A8', '#E7B53B'],
  banner: { fill: '#4A3410', stroke: '#E7B53B', text: '#FFF6DE', seal: '#A57E22' },
  plaque: { fill: '#FFF6DE', stroke: '#A57E22', text: '#3A2A10', accent: '#2E8B7A' },
  sail: '#A57E22',
  fireflies: true,
};

const ThemeCtx = createContext<MapTheme>(SPRING);
const useMapTheme = () => useContext(ThemeCtx);
export const mapThemeFor = (level: string) => (/^HSK/i.test(level) ? CHINA : /^DELE/i.test(level) ? SPAIN : /^GOETHE/i.test(level) ? GERMANY : /^[ABC][12]$/i.test(level) ? ALBION : /^TOPIK2$/i.test(level) ? KOREA_SPRING : /^TOPIK3$/i.test(level) ? KOREA_SUMMER : /^TOPIK4$/i.test(level) ? KOREA_WINTER : /^TOPIK5$/i.test(level) ? KOREA_SPIRIT : /^TOPIK6$/i.test(level) ? KOREA_DAWN : /^TOPIK/i.test(level) ? KOREA : /N1/i.test(level) ? NEWYEAR : /N2/i.test(level) ? SUMMER : /N3/i.test(level) ? WINTER : /N4/i.test(level) ? AUTUMN : SPRING);


function Tree({ x, y, s = 1, pink = false }: { x: number; y: number; s?: number; pink?: boolean }) {
  const t = useMapTheme();
  if (t.id !== 'spring' && t.id !== 'summer' && !pink) return <Pine x={x} y={y} s={s} />;
  return (
    <g transform={`translate(${x} ${y}) scale(${s})`}>
      <rect x="-1.6" y="-4" width="3.2" height="10" fill={WOOD} />
      <circle cx="0" cy="-9" r="9" fill={pink ? t.blossom : t.leaf} />
      <circle cx="-5" cy="-6" r="6" fill={pink ? t.blossomDark : t.leafDark} opacity={0.55} />
    </g>
  );
}

/** Pin noir japonais (niveaux d'automne). */
function Pine({ x, y, s = 1 }: { x: number; y: number; s?: number }) {
  const t = useMapTheme();
  return (
    <g transform={`translate(${x} ${y}) scale(${s})`}>
      <rect x="-1.4" y="-6" width="2.8" height="12" fill="#4A3424" />
      <path d="M0 -26 L9 -12 L4 -12 L11 -2 L-11 -2 L-4 -12 L-9 -12Z" fill={t.leaf} />
      <path d="M0 -26 L-9 -12 L-4 -12 L-11 -2 L-2 -2Z" fill={t.leafDark} opacity={0.6} />
      {t.id === 'winter' && <path d="M0 -27 L6 -17 L2 -18 L0 -15 L-2 -18 L-6 -17Z M-9 -10 L-4 -12 L0 -9 L4 -12 L9 -10 L5 -7 L0 -9 L-5 -7Z" fill="#FFFFFF" />}
    </g>
  );
}

/** Petit pin de bord de mer (les palmiers d'origine ne collaient pas au Japon des sagas). */
function Palm({ x, y, s = 1 }: { x: number; y: number; s?: number }) {
  return <Pine x={x} y={y} s={s * 0.9} />;
}

function Lighthouse({ x, y, s = 1, calm }: { x: number; y: number; s?: number; calm: boolean }) {
  return (
    <g transform={`translate(${x} ${y}) scale(${s})`}>
      <path d="M-6 0 L-4 -34 L4 -34 L6 0Z" fill="#F5F1E8" />
      <rect x="-5" y="-22" width="10" height="5" fill={VERMILION} />
      <rect x="-5" y="-10" width="10" height="5" fill={VERMILION} />
      <rect x="-5" y="-41" width="10" height="7" fill="#FFE08A" />
      <path d="M-7 -41 L0 -48 L7 -41Z" fill={VERMILION} />
      {!calm && (
        <motion.path d="M0 -38 L60 -52 L60 -24Z" fill="#FFE9A8" opacity={0.35} style={{ transformOrigin: '0px -38px' }} animate={{ rotate: [0, 360] }} transition={{ duration: 8, repeat: Infinity, ease: 'linear' }} />
      )}
    </g>
  );
}

function Fuji({ x, y, s = 1 }: { x: number; y: number; s?: number }) {
  return (
    <g transform={`translate(${x} ${y}) scale(${s})`}>
      <path d="M-48 4 L-10 -50 Q0 -58 10 -50 L48 4Z" fill="#5E6B78" />
      <path d="M-10 -50 Q0 -58 10 -50 L20 -36 L12 -40 L5 -32 L-2 -40 L-9 -33 L-20 -36Z" fill="#FFFFFF" />
      <path d="M-48 4 L-20 -30 L-14 4Z" fill="#4E5A66" opacity={0.6} />
    </g>
  );
}

function Waterfall({ x, y, s = 1, calm }: { x: number; y: number; s?: number; calm: boolean }) {
  return (
    <g transform={`translate(${x} ${y}) scale(${s})`}>
      <path d="M-14 -30 L14 -30 L10 6 L-10 6Z" fill={ROCK_DARK} />
      <rect x="-6" y="-30" width="12" height="36" fill="#BFE8F2" />
      {!calm && (
        <motion.rect x="-6" y="-30" width="12" height="36" fill="url(#km-fall)" animate={{ y: [-30, -24] }} transition={{ duration: 0.6, repeat: Infinity, ease: 'linear' }} />
      )}
      <ellipse cx="0" cy="8" rx="14" ry="4" fill="#FFFFFF" opacity={0.7} />
    </g>
  );
}

function Shrine({ x, y, s = 1 }: { x: number; y: number; s?: number }) {
  return (
    <g transform={`translate(${x} ${y}) scale(${s})`}>
      <rect x="-14" y="-14" width="28" height="14" fill="#E9DCC3" />
      <path d="M-22 -13 Q0 -30 22 -13Z" fill="#2F3B4A" />
      <rect x="-4" y="-10" width="8" height="10" fill={VERMILION} />
      <Torii x={-30} y={4} s={0.8} />
    </g>
  );
}

/** Étoile de ninja qui scintille dans le ciel du soir. */
function Shuriken({ x, y, s = 1, delay = 0, calm }: { x: number; y: number; s?: number; delay?: number; calm: boolean }) {
  return (
    <motion.g initial={{ x, y }} animate={calm ? undefined : { rotate: [0, 90], opacity: [0.35, 0.85, 0.35] }} transition={{ duration: 5, repeat: Infinity, ease: 'easeInOut', delay }} opacity={0.6}>
      <g transform={`scale(${s})`}>
        <path d="M0 -9 L2.4 -2.4 L9 0 L2.4 2.4 L0 9 L-2.4 2.4 L-9 0 L-2.4 -2.4Z" fill="#D9DEE6" />
        <circle r="1.6" fill="#232A3D" />
      </g>
    </motion.g>
  );
}

/** Feu follet (hitodama) : petite flamme bleue qui flotte au-dessus de l'eau. */
function Hitodama({ x, y, s = 1, delay = 0, calm }: { x: number; y: number; s?: number; delay?: number; calm: boolean }) {
  return (
    <motion.g initial={{ x, y }} animate={calm ? undefined : { y: [y, y - 10, y], x: [x, x + 6, x], opacity: [0.55, 0.95, 0.55] }} transition={{ duration: 4.5, repeat: Infinity, ease: 'easeInOut', delay }} opacity={0.8}>
      <g transform={`scale(${s})`}>
        <circle r="13" fill="#9FD8FF" opacity={0.35} filter="url(#km-soft)" />
        <path d="M0 9 C-8 9 -9 0 -4 -5 C-2 -8 2 -10 1 -16 C7 -10 10 -3 8 3 C7 7 4 9 0 9Z" fill="#BFE8FF" />
        <path d="M0 6 C-4 6 -5 1 -2 -2 C0 -4 1 -5 1 -8 C4 -4 5 0 4 3 C3 5 2 6 0 6Z" fill="#FFFFFF" />
      </g>
    </motion.g>
  );
}

const LANDMARKS = ['torii', 'village', 'waterfall', 'pagoda', 'fuji', 'bamboo', 'lighthouse', 'lanterns', 'shrine', 'castle', 'dawn'] as const;
type Landmark = (typeof LANDMARKS)[number];

function LandmarkFor({ kind, calm }: { kind: Landmark; calm: boolean }) {
  switch (kind) {
    case 'torii':
      return <><Hut x={-18} y={4} /><Torii x={20} y={14} s={1.1} /><Palm x={-36} y={8} /></>;
    case 'village':
      return <><Hut x={-16} y={2} s={1.2} /><Hut x={14} y={-4} /><Hut x={6} y={14} s={0.9} /></>;
    case 'waterfall':
      return <><Waterfall x={-10} y={4} calm={calm} /><Pagoda x={22} y={6} s={0.7} /></>;
    case 'pagoda':
      return <Pagoda x={0} y={10} s={1.1} />;
    case 'fuji':
      return <Fuji x={0} y={14} s={1.05} />;
    case 'bamboo':
      return <><Bamboo x={-6} y={10} /><Hut x={20} y={10} s={0.8} /></>;
    case 'lighthouse':
      return <><Lighthouse x={14} y={8} calm={calm} /><Hut x={-16} y={10} s={0.9} /></>;
    case 'lanterns':
      return <Lanterns x={0} y={10} s={1.1} calm={calm} />;
    case 'shrine':
      return <Shrine x={8} y={10} s={1.15} />;
    case 'castle':
      return <Castle x={2} y={20} s={1.05} />;
    case 'dawn':
      return <DawnGate x={2} y={14} />;
  }
}

// ───────────── Île ─────────────

function Island({ x, y, slot, seed, landmark, scene, state, calm }: { x: number; y: number; slot: number; seed: number; landmark: Landmark; scene?: string; state: WorldState; calm: boolean }) {
  const t = useMapTheme();
  const rx = 74;
  const ry = 44;
  const pink = slot % 2 === 0;
  if (state === 'done') return <RuinedIsland x={x} y={y} seed={seed} landmark={landmark} scene={scene} calm={calm} />;
  return (
    <g transform={`translate(${x} ${y})`}>
      {/* Hauts-fonds turquoise, ombre portée, falaise, plage puis végétation */}
      <path d={blob(0, 10, rx + 26, ry + 22, seed + 1, 0.25)} fill={t.shallow} opacity={t.shallowOpacity} />
      <path d={blob(0, 18, rx + 4, ry + 6, seed + 2)} fill={ROCK_DARK} />
      <path d={blob(0, 10, rx, ry, seed + 2)} fill={ROCK} />
      <path d={blob(0, 2, rx - 4, ry - 6, seed + 3)} fill={t.sand} />
      <path d={blob(4, -2, rx - 16, ry - 14, seed + 4, 0.28)} fill={t.grass[0]} />
      <path d={blob(-8, -6, rx - 34, ry - 24, seed + 5, 0.3)} fill={t.grass[1]} />
      {/* Écume */}
      <path d={blob(0, 14, rx + 6, ry + 8, seed + 2)} fill="none" stroke="#FFFFFF" strokeWidth="2" strokeDasharray="10 14" opacity={t.foam} />
      <Tree x={-52} y={0} pink={pink} />
      <Tree x={48} y={-6} s={0.9} pink={!pink} />
      <Palm x={54} y={14} s={0.8} />
      <Tree x={-38} y={-18} s={0.75} />
      <g transform="translate(0 -6)">{(scene && storyScene(scene, calm)) ?? <LandmarkFor kind={landmark} calm={calm} />}</g>
      {state === 'soon' && <path d={blob(0, 0, rx + 20, ry + 20, seed + 6, 0.2)} fill={t.dusk ? '#5B6878' : '#E8EEF2'} opacity={0.75} />}
    </g>
  );
}

/** Souche calcinée (arbre brûlé). */
function Stump({ x, y, s = 1, tilt = 0 }: { x: number; y: number; s?: number; tilt?: number }) {
  return (
    <g transform={`translate(${x} ${y}) scale(${s}) rotate(${tilt})`}>
      <path d="M-3 6 L-2 -8 L-4 -14 M-2 -8 L1 -16 L3 -10 L3 6Z" fill="#2B231D" stroke="#2B231D" strokeWidth="1.6" strokeLinejoin="round" />
      <path d="M1 -10 l5 -5 M-2 -4 l-5 -3" stroke="#2B231D" strokeWidth="1.4" strokeLinecap="round" />
      <ellipse cx="0" cy="6" rx="5" ry="1.6" fill="#1E1915" opacity={0.6} />
    </g>
  );
}

/** Colonne de fumée qui s'élève (fixe si les animations sont réduites). */
function Smoke({ x, y, delay = 0, calm }: { x: number; y: number; delay?: number; calm: boolean }) {
  const puffs = [0, 1, 2];
  if (calm)
    return (
      <g transform={`translate(${x} ${y})`} opacity={0.5}>
        <circle cx="0" cy="-6" r="5" fill="#6E6862" />
        <circle cx="4" cy="-16" r="7" fill="#837D76" />
        <circle cx="-2" cy="-28" r="9" fill="#9A948D" opacity={0.7} />
      </g>
    );
  return (
    <g transform={`translate(${x} ${y})`}>
      {puffs.map((i) => (
        <motion.circle
          key={i}
          r="7"
          fill="#5E5853"
          initial={{ cx: 0, cy: 0, opacity: 0, scale: 0.6 }}
          animate={{ cx: [0, 4, -3, 6], cy: [0, -14, -30, -46], opacity: [0, 0.85, 0.55, 0], scale: [0.6, 1.3, 1.9, 2.5] }}
          transition={{ duration: 4.2, repeat: Infinity, delay: delay + i * 1.4, ease: 'easeOut' }}
        />
      ))}
    </g>
  );
}

/** Drapeau de victoire planté sur une île conquise. */
function VictoryFlag({ x, y, calm }: { x: number; y: number; calm: boolean }) {
  const D = useDecor();
  return (
    <g transform={`translate(${x} ${y})`}>
      <ellipse cx="0" cy="2" rx="6" ry="2" fill="#1E1915" opacity={0.5} />
      <rect x="-1.3" y="-44" width="2.6" height="46" rx="1" fill="#3A2A1E" />
      <circle cx="0" cy="-45" r="2.4" fill="#F2C14E" />
      <motion.g style={{ transformOrigin: '1px -42px' }} animate={calm ? undefined : { skewY: [0, -6, 0, 5, 0], scaleX: [1, 0.94, 1, 0.97, 1] }} transition={{ duration: 2.4, repeat: Infinity, ease: 'easeInOut' }}>
        <path d="M1 -42 L28 -38 Q24 -32 28 -26 L1 -24Z" fill={VERMILION} stroke="#8E1B26" strokeWidth="1" />
        <text x="13" y="-28.5" textAnchor="middle" fontSize="11" fontWeight="900" fill="#FFF6E0" fontFamily="'Noto Sans JP', sans-serif">{D('win')}</text>
      </motion.g>
    </g>
  );
}

/**
 * Île conquise : terre brûlée, falaise fissurée, végétation réduite en souches,
 * repère effondré et calciné, fumée qui monte… et le drapeau de victoire du joueur.
 */
function RuinedIsland({ x, y, seed, landmark, scene, calm }: { x: number; y: number; seed: number; landmark: Landmark; scene?: string; calm: boolean }) {
  const rx = 74;
  const ry = 44;
  const tilt = seed % 2 === 0 ? -9 : 8;
  return (
    <g transform={`translate(${x} ${y})`}>
      {/* Eaux troublées par les cendres */}
      <path d={blob(0, 10, rx + 26, ry + 22, seed + 1, 0.25)} fill="#5E8C88" opacity={0.35} />
      <path d={blob(0, 18, rx + 4, ry + 6, seed + 2)} fill="#3F3933" />
      <path d={blob(0, 10, rx, ry, seed + 2)} fill="#5F5750" />
      {/* Fissures dans la falaise */}
      <g stroke="#2A2420" strokeWidth="1.6" fill="none" strokeLinecap="round" strokeLinejoin="round">
        <path d="M-58 26 l6 -6 l-2 -6 l5 -5" />
        <path d="M22 44 l3 -8 l-4 -5 l6 -7" />
        <path d="M60 22 l-5 -4 l2 -6" />
      </g>
      <path d={blob(0, 2, rx - 4, ry - 6, seed + 3)} fill="#B9A887" />
      {/* Terre brûlée */}
      <path d={blob(4, -2, rx - 16, ry - 14, seed + 4, 0.28)} fill="#6B5A47" />
      <path d={blob(-8, -6, rx - 34, ry - 24, seed + 5, 0.3)} fill="#54473A" />
      <ellipse cx="-4" cy="-2" rx="46" ry="24" fill="url(#km-scorch)" />
      {/* Écume grise */}
      <path d={blob(0, 14, rx + 6, ry + 8, seed + 2)} fill="none" stroke="#D9D4CC" strokeWidth="2" strokeDasharray="6 18" opacity={0.45} />
      <Stump x={-52} y={0} tilt={-6} />
      <Stump x={48} y={-6} s={0.9} tilt={10} />
      <Stump x={56} y={14} s={0.7} tilt={-14} />
      <Stump x={-38} y={-18} s={0.75} tilt={4} />
      {/* Repère effondré : penché, calciné, à moitié enfoui */}
      <g transform={`translate(0 2) rotate(${tilt}) translate(0 -8)`} filter="url(#km-ruin)" opacity={0.92}>
        {(scene && storyScene(scene, true)) ?? <LandmarkFor kind={landmark} calm />}
      </g>
      {/* Gravats au pied du repère */}
      <g fill="#4A423B" stroke="#2A2420" strokeWidth="0.8">
        <path d="M-22 10 l6 -5 l7 2 l1 5Z" />
        <path d="M10 12 l5 -6 l8 1 l-1 6Z" />
        <path d="M-6 14 l4 -4 l5 1 l0 4Z" />
        <path d="M26 4 l4 -3 l4 2 l-1 3Z" />
      </g>
      {/* Braises */}
      {[[-30, 6], [18, -4], [-12, -16], [34, 10]].map(([ex, ey], i) =>
        calm ? (
          <circle key={i} cx={ex} cy={ey} r="1.8" fill="#FF8A3D" opacity={0.7} />
        ) : (
          <motion.circle key={i} cx={ex} cy={ey} r="1.8" fill="#FF8A3D" animate={{ opacity: [0.2, 1, 0.2] }} transition={{ duration: 1.4 + i * 0.3, repeat: Infinity }} />
        ),
      )}
      <Smoke x={-18} y={-10} calm={calm} />
      <Smoke x={22} y={-14} delay={0.7} calm={calm} />
      <VictoryFlag x={-44} y={14} calm={calm} />
    </g>
  );
}

/** Îlot encore inexploré : silhouette dans la brume, sans interaction. */
function MistyIslet({ x, y, seed }: { x: number; y: number; seed: number }) {
  const t = useMapTheme();
  return (
    <g transform={`translate(${x} ${y})`} opacity={0.55} aria-hidden="true">
      <path d={blob(0, 14, 66, 36, seed, 0.3)} fill="#5FD1C9" opacity={0.25} />
      <path d={blob(0, 10, 52, 28, seed + 1)} fill="#6D7F84" />
      <path d={blob(0, 2, 44, 22, seed + 2, 0.3)} fill="#7FA184" />
      <Tree x={-14} y={0} s={0.8} />
      <Tree x={12} y={-4} s={0.7} />
      <path d={blob(0, 0, 80, 46, seed + 3, 0.2)} fill={t.dusk ? '#56657A' : '#E8F1F2'} opacity={0.7} filter="url(#km-soft)" />
      <text y="6" textAnchor="middle" fontSize="22" fontWeight="900" fill="#FFFFFF" opacity={0.9}>?</text>
    </g>
  );
}

/** Pont de bois à rambardes vermillon entre deux îles proches. */
function Bridge({ a, b }: { a: { x: number; y: number }; b: { x: number; y: number } }) {
  const dx = b.x - a.x;
  const dy = b.y - a.y;
  const len = Math.hypot(dx, dy);
  const ux = dx / len;
  const uy = dy / len;
  const s = { x: a.x + ux * 66, y: a.y + uy * 40 };
  const e = { x: b.x - ux * 66, y: b.y - uy * 40 };
  const nx = -uy * 6;
  const ny = ux * 6;
  const line = (ox: number, oy: number) => `M${s.x + ox} ${s.y + oy} Q${(s.x + e.x) / 2 + ox} ${(s.y + e.y) / 2 + oy - 14} ${e.x + ox} ${e.y + oy}`;
  return (
    <g>
      <path d={line(0, 6)} stroke="#000" strokeOpacity={0.15} strokeWidth="12" fill="none" />
      <path d={line(0, 0)} stroke={WOOD} strokeWidth="11" fill="none" />
      <path d={line(0, 0)} stroke="#C9A06B" strokeWidth="8" strokeDasharray="2 3" fill="none" />
      <path d={line(nx, ny)} stroke={VERMILION} strokeWidth="2" fill="none" />
      <path d={line(-nx, -ny)} stroke={VERMILION} strokeWidth="2" fill="none" />
    </g>
  );
}

function Boat({ x, y, s = 1, flip = false, drift, calm }: { x: number; y: number; s?: number; flip?: boolean; drift: number; calm: boolean }) {
  const t = useMapTheme();
  if (t.id === 'winter')
    return (
      <motion.g initial={{ x, y }} animate={calm ? { x, y } : { x: [x, x + drift, x], y: [y, y - 3, y] }} transition={{ duration: 18, repeat: Infinity, ease: 'easeInOut' }}>
        {/* Lanterne de papier confiée à l'eau (tōrō nagashi) */}
        <g transform={`scale(${s * 1.25})`}>
          <circle cy="-6" r="16" fill="#FFC86B" opacity={0.22} filter="url(#km-soft)" />
          <rect x="-8" y="0" width="16" height="2.4" rx="1" fill="#5A4632" />
          <rect x="-5.5" y="-11" width="11" height="11" rx="1.2" fill="#FFE2A6" stroke="#B08D3C" strokeWidth="0.8" />
          <ellipse cy="-5" rx="2.2" ry="3.4" fill="#FF9A3D" />
          <path d="M-12 4 Q0 6.5 12 4" stroke="#FFE2A6" strokeWidth="1" fill="none" opacity={0.5} />
        </g>
      </motion.g>
    );
  return (
    <motion.g initial={{ x, y }} animate={calm ? { x, y } : { x: [x, x + drift, x], y: [y, y - 3, y] }} transition={{ duration: 14, repeat: Infinity, ease: 'easeInOut' }}>
      <g transform={`scale(${flip ? -s : s} ${s})`}>
        <path d="M-12 0 L12 0 L8 6 L-8 6Z" fill={WOOD} />
        <path d="M0 0 V-20" stroke="#3B2A1C" strokeWidth="1.5" />
        <path d="M1 -19 L12 -4 L1 -4Z" fill={t.sail} />
        <path d="M-1 -16 L-9 -4 L-1 -4Z" fill={t.dusk ? '#CDBFA3' : '#F5F1E8'} />
        {t.dusk && <circle cx="-10" cy="-2" r="1.8" fill="#FFC86B" />}
        <path d="M-16 8 Q0 11 16 8" stroke="#FFFFFF" strokeWidth="1.2" fill="none" opacity={0.7} />
      </g>
    </motion.g>
  );
}

/** Vignette d'un chapitre : la même île que sur la carte, en miniature (décor du mode histoire, sans animation). */
export function IslandVignette({ slug, level, size = 64 }: { slug: string; level: string; size?: number }) {
  const t = mapThemeFor(level);
  const scene = storyScene(slug, true);
  if (!scene) return null;
  return (
    <ThemeCtx.Provider value={t}>
      <svg viewBox="-56 -64 112 112" width={size} height={size} aria-hidden="true" className="shrink-0 rounded-2xl" style={{ background: t.sea[1] }}>
        <ellipse cy="20" rx="52" ry="25" fill={t.shallow} opacity={t.shallowOpacity} />
        <ellipse cy="19" rx="48" ry="23" fill={ROCK_DARK} />
        <ellipse cy="14" rx="48" ry="23" fill={t.sand} />
        <ellipse cy="11" rx="41" ry="18" fill={t.grass[0]} />
        {scene}
      </svg>
    </ThemeCtx.Provider>
  );
}

export function WorldMap({ worlds, avatar, region, level = 'N5', saga }: { worlds: PathWorldDto[]; avatar: AvatarConfig; region: string; level?: string; saga?: { glyph: string; title: string } }) {
  const calm = useCalm();
  const t = mapThemeFor(level);
  const pts = useMemo(() => islandPositions(worlds.length), [worlds.length]);
  const states = worldStates(worlds);
  const current = Math.max(0, states.indexOf('current'));
  const scroller = useRef<HTMLDivElement>(null);
  // Sur petit écran, la carte défile : on centre l'île en cours.
  useEffect(() => {
    const el = scroller.current;
    if (!el || el.scrollWidth <= el.clientWidth) return;
    el.scrollLeft = (pts[current].x / W) * el.scrollWidth - el.clientWidth / 2;
  }, [current, pts]);
  const go = (slug: string) => document.getElementById(`w-${slug}`)?.scrollIntoView({ behavior: 'smooth', block: 'start' });

  // Chemins : pont si les îles sont proches, sinon pointillés lumineux sur l'eau.
  const segments = pts.slice(1).map((b, i) => {
    const a = pts[i];
    const dist = Math.hypot(b.x - a.x, b.y - a.y);
    const mx = (a.x + b.x) / 2 + (b.y - a.y) * 0.18;
    const my = (a.y + b.y) / 2 - (b.x - a.x) * 0.12;
    return { a, b, bridge: dist < 225 && Math.abs(b.y - a.y) < dist * 0.45, d: `M${a.x} ${a.y} Q${mx} ${my} ${b.x} ${b.y}`, reached: i < current || states[i + 1] === 'done' };
  });
  const petals = useMemo(() => Array.from({ length: 10 }, (_, i) => ({ x: (i * 97) % W, d: 9 + (i % 4) * 2, delay: i * 1.3 })), []);

  return (
    <ThemeCtx.Provider value={t}>
    <figure className="mb-10 overflow-hidden rounded-3xl border border-line shadow-sm" data-theme-map={t.id}>
      <figcaption className="sr-only">{T("Carte de l’archipel {0} : {1} îles{2}.", [ region , worlds.length , worlds.length < SLOTS.length ? T(", d’autres restent à découvrir") : '' ])}</figcaption>
      <div ref={scroller} className="overflow-x-auto">
        <svg viewBox={`0 0 ${W} ${H}`} className="block h-auto w-full min-w-[720px]" role="group" aria-label={T("Carte : {0}", [region])}>
          <defs>
            <linearGradient id="km-sea" x1="0" y1="0" x2="0" y2="1">
              <stop offset="0" stopColor={t.sea[0]} />
              <stop offset="0.55" stopColor={t.sea[1]} />
              <stop offset="1" stopColor={t.sea[2]} />
            </linearGradient>
            {t.dusk ? (
              <radialGradient id="km-sun" cx="0.88" cy="0.1" r="0.5">
                <stop offset="0" stopColor="#F3E9C8" stopOpacity="0.35" />
                <stop offset="0.35" stopColor="#B9A6D6" stopOpacity="0.12" />
                <stop offset="1" stopColor="#B9A6D6" stopOpacity="0" />
              </radialGradient>
            ) : (
              t.id === 'newyear' ? (
                <radialGradient id="km-sun" cx="0.5" cy="1.08" r="0.75">
                  <stop offset="0" stopColor="#FFE3A0" stopOpacity="0.85" />
                  <stop offset="0.35" stopColor="#F59A6A" stopOpacity="0.35" />
                  <stop offset="1" stopColor="#7C5BB0" stopOpacity="0" />
                </radialGradient>
              ) : t.id === 'winter' ? (
                <radialGradient id="km-sun" cx="0.97" cy="0.86" r="0.6">
                  <stop offset="0" stopColor="#FFC9A0" stopOpacity="0.6" />
                  <stop offset="0.35" stopColor="#E78FB3" stopOpacity="0.24" />
                  <stop offset="1" stopColor="#7C6BD0" stopOpacity="0" />
                </radialGradient>
              ) : (
                <radialGradient id="km-sun" cx="0.92" cy="0.02" r="0.55">
                  <stop offset="0" stopColor="#FFD58A" stopOpacity="0.85" />
                  <stop offset="0.4" stopColor="#FFB86B" stopOpacity="0.25" />
                  <stop offset="1" stopColor="#FFB86B" stopOpacity="0" />
                </radialGradient>
              )
            )}
            <linearGradient id="km-fall" x1="0" y1="0" x2="0" y2="1">
              <stop offset="0" stopColor="#FFFFFF" stopOpacity="0" />
              <stop offset="0.5" stopColor="#FFFFFF" stopOpacity="0.8" />
              <stop offset="1" stopColor="#FFFFFF" stopOpacity="0" />
            </linearGradient>
            <filter id="km-glow" x="-50%" y="-50%" width="200%" height="200%">
              <feGaussianBlur stdDeviation="3" result="b" />
              <feMerge><feMergeNode in="b" /><feMergeNode in={"SourceGraphic"} /></feMerge>
            </filter>
            <filter id="km-soft"><feGaussianBlur stdDeviation="6" /></filter>
            {/* Repère calciné : désaturé et assombri */}
            <filter id="km-ruin">
              <feColorMatrix type="matrix" values="0.26 0.42 0.08 0 0  0.22 0.4 0.08 0 0  0.2 0.36 0.1 0 0  0 0 0 1 0" />
            </filter>
            <radialGradient id="km-scorch">
              <stop offset="0" stopColor="#2E2620" stopOpacity="0.75" />
              <stop offset="1" stopColor="#2E2620" stopOpacity="0" />
            </radialGradient>
            <pattern id="km-waves" width="80" height="40" patternUnits="userSpaceOnUse">
              <path d="M4 20 q6 -4 12 0 M48 34 q9 -5 18 0" stroke="#FFFFFF" strokeWidth="1.2" fill="none" opacity={t.waves} strokeLinecap="round" />
            </pattern>
          </defs>

          {/* Océan, reflets et soleil couchant */}
          <rect width={W} height={H} fill="url(#km-sea)" />
          <motion.rect x="-80" width={W + 160} height={H} fill="url(#km-waves)" animate={calm ? undefined : { x: [-80, 0] }} transition={{ duration: 12, repeat: Infinity, ease: 'linear' }} />
          <rect width={W} height={H} fill="url(#km-sun)" />
          {t.dusk && (
            <g pointerEvents="none">
              {/* Lune et son reflet */}
              <circle cx="880" cy="62" r="34" fill="#F3E9C8" opacity={0.12} filter="url(#km-soft)" />
              <circle cx="880" cy="62" r="20" fill="#F1E6C4" />
              <circle cx="888" cy="56" r="17" fill={t.sea[0]} opacity={0.9} />
              {[0, 1, 2, 3].map((i) => <rect key={i} x={866 - i * 6} y={96 + i * 14} width={28 + i * 12} height="2" rx="1" fill="#F1E6C4" opacity={0.25 - i * 0.05} />)}
            </g>
          )}

          {saga && t.id === 'newyear' && (
            <g pointerEvents="none">
              {/* Le mont Fuji au loin, et des grues qui volent vers le soleil levant */}
              <g transform="translate(560 64)" opacity={0.85}>
                <path d="M-150 30 L-38 -38 Q0 -50 38 -38 L150 30Z" fill="#4E4886" />
                <path d="M-38 -38 Q0 -50 38 -38 L56 -26 L34 -22 L20 -30 L6 -20 L-10 -30 L-24 -21 L-56 -26Z" fill="#F4F0FA" />
              </g>
              {[{ x: 180, y: 70, s: 1 }, { x: 214, y: 54, s: 0.8 }, { x: 236, y: 82, s: 0.7 }].map((c, i) => (
                <motion.g key={i} initial={{ x: c.x, y: c.y }} animate={calm ? undefined : { x: [c.x, c.x + 600], y: [c.y, c.y - 30] }} transition={{ duration: 40, repeat: Infinity, ease: 'linear', delay: i * 0.6 }}>
                  <g transform={`scale(${c.s})`}>
                    <path d="M-14 0 Q-6 -10 0 0 Q6 -10 14 0 Q6 -4 0 2 Q-6 -4 -14 0Z" fill="#FFFFFF" />
                    <path d="M0 0 l9 -3" stroke="#FFFFFF" strokeWidth="1.6" strokeLinecap="round" />
                    <circle cx="9.5" cy="-3.2" r="1.2" fill="#C8323F" />
                  </g>
                </motion.g>
              ))}
            </g>
          )}
          {saga && t.id === 'summer' && (
            <g pointerEvents="none">
              {/* Feux d'artifice de la fête d'été */}
              {[{ x: 300, y: 46, c: '#FFD27A', r: 30 }, { x: 560, y: 70, c: '#F4A9C0', r: 24 }, { x: 150, y: 96, c: '#9FE8D0', r: 20 }].map((f, i) => (
                <motion.g key={i} initial={{ x: f.x, y: f.y }} style={{ transformOrigin: '0px 0px' }} animate={calm ? undefined : { scale: [0.2, 1, 1.08], opacity: [0, 0.9, 0] }} transition={{ duration: 2.6, repeat: Infinity, repeatDelay: 2.4, delay: i * 1.5, ease: 'easeOut' }} opacity={0.75}>
                  {Array.from({ length: 12 }, (_, k) => {
                    const a = (k * Math.PI) / 6;
                    return <path key={k} d={`M${Math.cos(a) * f.r * 0.35} ${Math.sin(a) * f.r * 0.35} L${Math.cos(a) * f.r} ${Math.sin(a) * f.r}`} stroke={f.c} strokeWidth="2.4" strokeLinecap="round" />;
                  })}
                  <circle r="3" fill="#FFFFFF" />
                </motion.g>
              ))}
              {/* Nénuphars et lotus sur l'eau */}
              {[[70, 210], [120, 420], [330, 560], [520, 250], [600, 520], [780, 120], [950, 430], [880, 560], [40, 330], [700, 250]].map(([lx, ly], i) => (
                <g key={i} transform={`translate(${lx} ${ly}) scale(${1 + (i % 3) * 0.25})`}>
                  <path d="M0 0 m-9 0 a9 5 0 1 0 18 0 a9 5 0 1 0 -18 0 M0 0 L8 -3" fill="#3F9150" stroke="#2F7A45" strokeWidth="0.8" />
                  {i % 2 === 0 && <path d="M0 -2 q-4 -5 0 -9 q4 4 0 9Z M0 -2 q-7 -1.4 -6 -7 q5 1 6 7Z M0 -2 q7 -1.4 6 -7 q-5 1 -6 7Z" fill="#F4A9C0" />}
                </g>
              ))}
            </g>
          )}
          {saga && t.id === 'autumn' && (
            /* Une ombre bondit devant la lune */
            <motion.g pointerEvents="none" initial={{ x: 872, y: 62 }} animate={calm ? undefined : { x: [846, 872, 898], y: [70, 56, 70], opacity: [0, 1, 1, 0] }} transition={{ duration: 3.4, repeat: Infinity, repeatDelay: 7, ease: 'easeInOut' }}>
              <g fill="#0E1420">
                <circle cx="3" cy="-7" r="2.6" />
                <path d="M-6 0 Q-1 -6 3 -5 L8 -8 L9 -6.6 L5 -3 L6 2 L11 4 L10 5.6 L3 4 L0 0 L-5 4 L-9 3 L-8 1.4Z" />
                <path d="M1 -8 l-7 -1.4 l0.4 1.4Z" />
              </g>
            </motion.g>
          )}
          {saga && t.id === 'winter' && (
            /* Voiles de lumière : le ciel des esprits */
            <g pointerEvents="none" filter="url(#km-soft)">
              {[{ d: 'M-20 60 Q200 10 420 50 T860 30 T1040 60', c: '#7CF0D0', o: 0.3 }, { d: 'M-20 95 Q240 50 480 90 T1040 70', c: '#9FD8FF', o: 0.24 }, { d: 'M-20 30 Q300 -10 560 26 T1040 10', c: '#B89CF0', o: 0.3 }].map((r, i) => (
                <motion.path key={i} d={r.d} stroke={r.c} strokeWidth={26 - i * 4} fill="none" strokeLinecap="round" opacity={r.o} animate={calm ? undefined : { opacity: [r.o * 0.5, r.o * 1.4, r.o * 0.5], y: [0, 6, 0] }} transition={{ duration: 9 + i * 3, repeat: Infinity, ease: 'easeInOut' }} />
              ))}
            </g>
          )}

          {/* Îles lointaines à l'horizon */}
          <g opacity={0.55}>
            <path d={blob(60, 22, 70, 14, 91)} fill={t.horizon} />
            <path d={blob(760, 18, 90, 12, 92)} fill={t.horizon} />
            <path d={blob(960, 70, 40, 10, 93)} fill={t.horizon} />
          </g>

          {/* Mode histoire : le décor du héros */}
          {saga && t.id === 'spring' && (
            <g pointerEvents="none" opacity={0.6}>
              <Castle x={770} y={36} s={0.7} fill={t.horizon} />
              <Castle x={600} y={30} s={0.4} fill={t.horizon} />
            </g>
          )}
          {saga && t.id === 'china' && (
            /* Monts du Shandong à l'horizon, muraille de Qin et tour à étages */
            <g pointerEvents="none" opacity={0.55} fill={t.horizon}>
              <path d="M500 70 L560 26 L600 50 L650 18 L720 70Z" />
              <path d="M800 70 L850 36 L885 54 L935 28 L990 70Z" />
              <path d="M560 70 v-10 h8 v4 h8 v-4 h8 v4 h8 v-4 h8 v4 h8 v-4 h8 v10Z" />
              <path d="M300 70 h18 v-8 h-14 l-4 -4 h22 l-4 4 h-2 v-6 h-12 l-4 -4 h18 l-4 4 h-2 v-6 h-6 v6 h-4Z" />
            </g>
          )}
          {saga && t.id === 'korea' && (
            /* Montagnes de la péninsule à l'horizon, toit de palais et pagode de pierre */
            <g pointerEvents="none" opacity={0.55} fill={t.horizon}>
              <path d="M520 70 L585 22 L620 46 L665 12 L735 70Z" />
              <path d="M820 70 L860 40 L890 56 L930 30 L980 70Z" />
              <path d="M700 70 Q712 58 724 56 H776 Q788 58 800 70Z" />
              <rect x="728" y="58" width="44" height="12" />
              <path d="M300 64 h14 v-6 h-11 v-6 h8 v-6 h-5 v-8 h-2 v8 h-5 v6 h8 v6 h-11 v6Z" />
            </g>
          )}
          {saga && t.id === 'autumn' && (
            <g pointerEvents="none">
              {[{ x: 300, y: 46, s: 1 }, { x: 560, y: 86, s: 0.7 }, { x: 730, y: 30, s: 0.85 }, { x: 150, y: 130, s: 0.6 }, { x: 940, y: 190, s: 0.7 }].map((p, i) => (
                <Shuriken key={i} x={p.x} y={p.y} s={p.s} delay={i * 0.9} calm={calm} />
              ))}
            </g>
          )}

          {/* Nuages */}
          {[{ x: 120, y: 60, s: 1 }, { x: 660, y: 40, s: 0.8 }, { x: 900, y: 140, s: 0.7 }].map((c, i) => (
            <motion.g key={i} initial={{ x: c.x, y: c.y }} animate={calm ? undefined : { x: [c.x, c.x + 40, c.x] }} transition={{ duration: 30 + i * 6, repeat: Infinity, ease: 'easeInOut' }} opacity={t.cloudOpacity}>
              <g transform={`scale(${c.s})`} filter="url(#km-soft)">
                <ellipse cx="0" cy="0" rx="60" ry="16" fill={t.cloud} />
                <ellipse cx="-20" cy="-10" rx="30" ry="14" fill={t.cloud} />
                <ellipse cx="22" cy="-8" rx="26" ry="12" fill={t.cloud} />
              </g>
            </motion.g>
          ))}

          {/* Bateaux */}
          <Boat x={470} y={530} s={1.2} drift={60} calm={calm} />
          <Boat x={640} y={200} drift={-50} flip calm={calm} />
          {!t.dusk && <Boat x={90} y={330} s={0.8} drift={40} calm={calm} />}
          {!t.dusk && <Boat x={950} y={250} s={0.9} drift={-30} flip calm={calm} />}
          {/* Bancs de brume au ras de l'eau */}
          {t.dusk &&
            [{ x: 260, y: 300, w: 260 }, { x: 760, y: 430, w: 220 }, { x: 120, y: 470, w: 180 }].map((m, i) => (
              <motion.ellipse key={i} cx={m.x} cy={m.y} rx={m.w} ry="18" fill="#D9DEE6" opacity={0.1} filter="url(#km-soft)" animate={calm ? undefined : { cx: [m.x, m.x + 30, m.x] }} transition={{ duration: 26 + i * 5, repeat: Infinity, ease: 'easeInOut' }} pointerEvents="none" />
            ))}

          {/* Chemins : sous les îles */}
          {segments.map((s, i) =>
            s.bridge ? null : (
              <g key={i}>
                <path d={s.d} fill="none" stroke={t.path} strokeWidth="6" strokeDasharray="0.1 15" strokeLinecap="round" opacity={s.reached ? 1 : 0.7} filter="url(#km-glow)" />
                {s.reached && !calm && (
                  <motion.path d={s.d} fill="none" stroke="#FFFFFF" strokeWidth="6" strokeDasharray="0.1 16" strokeLinecap="round" animate={{ strokeDashoffset: [0, -32] }} transition={{ duration: 2, repeat: Infinity, ease: 'linear' }} opacity={0.7} />
                )}
              </g>
            ),
          )}

          {/* Branches de cerisier (ou d'érable) aux coins, sous les îles */}
          <g pointerEvents="none">
            <path d="M0 560 Q60 520 120 540 M40 530 Q70 490 60 470" stroke="#5B3A2A" strokeWidth="6" fill="none" strokeLinecap="round" />
            {[[30, 525], [62, 505], [95, 530], [120, 545], [58, 470], [15, 555], [80, 488]].map(([cx, cy], i) => (
              <circle key={i} cx={cx} cy={cy} r={i % 2 ? 13 : 16} fill={i % 3 ? t.blossom : t.blossomDark} opacity={0.95} />
            ))}
            <path d="M1000 590 Q930 560 870 580 M960 575 Q940 540 955 520" stroke="#5B3A2A" strokeWidth="6" fill="none" strokeLinecap="round" />
            {[[985, 575], [940, 560], [905, 578], [872, 585], [955, 522], [925, 540]].map(([cx, cy], i) => (
              <circle key={i} cx={cx} cy={cy} r={i % 2 ? 13 : 16} fill={i % 3 ? t.blossom : t.blossomDark} opacity={0.95} />
            ))}
          </g>
          {/* Îles encore à découvrir */}
          {worlds.length < SLOTS.length && SLOTS.slice(worlds.length).map((p, i) => <MistyIslet key={i} x={p.x} y={p.y} seed={200 + i * 11} />)}
          {worlds.length < SLOTS.length && worlds.length > 0 && (
            <path d={`M${pts[worlds.length - 1].x} ${pts[worlds.length - 1].y} Q${(pts[worlds.length - 1].x + SLOTS[worlds.length].x) / 2 + 30} ${(pts[worlds.length - 1].y + SLOTS[worlds.length].y) / 2} ${SLOTS[worlds.length].x} ${SLOTS[worlds.length].y}`} fill="none" stroke={t.path} strokeWidth="5" strokeDasharray="0.1 15" strokeLinecap="round" opacity={0.3} />
          )}

          {/* Îles */}
          {worlds.map((w, i) => {
            const p = pts[i];
            // Chaque archipel a ses propres repères : décalage selon le niveau (n5 → 0, n4 → 3, n3 → 6…).
            const lvl = Number(/^n(\d)/.exec(w.slug)?.[1] ?? 5);
            const scenic = LANDMARKS.filter((l) => l !== 'shrine' && l !== 'castle' && l !== 'dawn');
            // Dernière île : le château du seigneur (samouraï, ninja) ou la porte de l'aube (esprit).
            const finale: Landmark = !saga ? 'shrine' : t.id === 'winter' ? 'dawn' : 'castle';
            const landmark: Landmark = w.exam ? finale : scenic[(p.slot + (5 - lvl) * 3) % scenic.length];
            return <Island key={w.slug} x={p.x} y={p.y} slot={p.slot} seed={i * 7 + w.order * 13} landmark={landmark} scene={saga ? w.slug : undefined} state={states[i]} calm={calm} />;
          })}

          {/* Ponts : par-dessus l'eau, entre deux îles proches */}
          {segments.map((s, i) => (s.bridge ? <Bridge key={i} a={s.a} b={s.b} /> : null))}

          {/* Sceaux, noms et interaction */}
          {worlds.map((w, i) => {
            const p = pts[i];
            const st = states[i];
            const glyph = w.exam ? (t.id === 'korea' ? '시' : t.id === 'albion' ? 'T' : t.id === 'china' ? '考' : t.id === 'spain' ? 'E' : t.id === 'germany' ? 'P' : '試') : w.boss?.glyph ?? String(w.order);
            const detail = w.exam && w.progress.total === 0 ? (w.exam.passed ? T("examen blanc réussi") : 'examen blanc') : T("{0} leçons sur {1}", [w.progress.completed, w.progress.total]);
            const label = T("Île {0} : {1}, {2}", [w.order, w.title, st === 'done' ? T("terminée") : st === 'current' ? T("en cours") : st === 'soon' ? T("bientôt") : detail]);
            const title = w.title.length > 20 ? `${w.title.slice(0, 19).trimEnd()}…` : w.title;
            return (
              <g key={w.slug} transform={`translate(${p.x} ${p.y})`} role="button" tabIndex={0} aria-label={label} className="cursor-pointer focus:outline-none [&:focus-visible>.km-focus]:opacity-100" onClick={() => go(w.slug)} onKeyDown={(e) => (e.key === 'Enter' || e.key === ' ') && (e.preventDefault(), go(w.slug))}>
                <title>{w.title}</title>
                <ellipse rx="96" ry="66" fill="transparent" />
                <ellipse className="km-focus" rx="100" ry="70" fill="none" stroke="#FFFFFF" strokeWidth="3" strokeDasharray="6 6" opacity={0} />
                {st === 'current' && !calm && (
                  <motion.ellipse rx="92" ry="60" cy="8" fill="none" stroke={t.dusk ? "#E2A23B" : "#FFE08A"} strokeWidth="3" animate={{ opacity: [0.9, 0.2, 0.9], scale: [1, 1.06, 1] }} transition={{ duration: 2.2, repeat: Infinity }} />
                )}
                {/* Sceau rouge (gardien ou numéro) */}
                <g transform="translate(46 -58)">
                  <circle r="21" fill="#FFFFFF" opacity={0.9} />
                  <circle r="18" fill={st === 'soon' ? '#9AA3AB' : '#8E1B26'} />
                  <circle r="18" fill="none" stroke="#FFFFFF" strokeWidth="1.5" opacity={0.5} />
                  <text textAnchor="middle" dy="0.36em" fontSize="18" fontWeight="900" className="jp" fill="#FFFFFF">{glyph}</text>
                  {st === 'done' && (
                    <g transform="translate(15 13)">
                      <circle r="9" fill="var(--ok)" stroke="#FFFFFF" strokeWidth="2" />
                      <path d="M-4 0 L-1 3 L4 -3" stroke="#FFFFFF" strokeWidth="2.2" fill="none" strokeLinecap="round" />
                    </g>
                  )}
                </g>
                {/* Plaque de bois avec le nom */}
                <g transform="translate(0 74)">
                  <rect x={-(title.length * 3.6 + 24)} y="-12" width={title.length * 7.2 + 48} height="24" rx="8" fill={t.plaque.fill} stroke={t.plaque.stroke} strokeWidth="2" />
                  <text textAnchor="middle" dy="0.35em" fontSize="12.5" fontWeight="700" fill={t.plaque.text}>
                    <tspan fill={t.plaque.accent}>{w.order} · </tspan>
                    {title}
                  </text>
                </g>
                {st === 'soon' && <text y="4" textAnchor="middle" fontSize="13" fontWeight="700" fill="#5A6670">{T("Bientôt")}</text>}
              </g>
            );
          })}

          <g pointerEvents="none">
            {!calm &&
              petals.map((p, i) => (
                t.snow ? (
                  /* Flocons qui tombent en se balançant */
                  <motion.circle key={i} r={i % 3 ? 2.4 : 3.4} fill="#FFFFFF" opacity={0.9} initial={{ cx: p.x, cy: -10 }} animate={{ cy: [-10, H + 10], cx: [p.x, p.x + (i % 2 ? 30 : -30), p.x] }} transition={{ duration: p.d * 1.4, repeat: Infinity, delay: p.delay, ease: 'linear' }} />
                ) : t.fireflies ? (
                  /* Lucioles sur les rizières (ou lueurs d'esprits) : elles montent doucement en clignotant */
                  <motion.circle key={i} r={i % 3 ? 2.2 : 3} fill={t.particles[i % t.particles.length]} initial={{ cx: p.x, cy: 90 + ((i * 97) % 460), opacity: 0 }} animate={{ cy: [90 + ((i * 97) % 460), 60 + ((i * 97) % 460)], cx: [p.x, p.x + (i % 2 ? 26 : -26), p.x], opacity: [0, 0.95, 0.2, 0.9, 0] }} transition={{ duration: 5 + (i % 4), repeat: Infinity, delay: p.delay * 0.5, ease: 'easeInOut' }} />
                ) : t.petals ? (
                  /* Pétales d'azalée et de forsythia portés par le vent de printemps */
                  <motion.ellipse key={i} rx="3.2" ry="5" fill={t.particles[i % t.particles.length]} opacity={0.9} initial={{ cx: p.x, cy: -10 }} animate={{ cy: [-10, H + 10], cx: [p.x, p.x + (i % 2 ? 50 : -50)], rotate: [0, 220] }} transition={{ duration: p.d * 1.1, repeat: Infinity, delay: p.delay, ease: 'linear' }} />
                ) : t.dusk || t.id === 'korea' ? (
                  /* Feuilles d'érable qui tombent lentement (automne japonais, érables du Seoraksan) */
                  <motion.g key={i} initial={{ x: p.x, y: -14 }} animate={{ y: [-14, H + 14], x: [p.x, p.x + (i % 2 ? 60 : -60)], rotate: [0, i % 2 ? 260 : -260] }} transition={{ duration: p.d * 1.6, repeat: Infinity, delay: p.delay * 1.5, ease: 'linear' }}>
                    <path d="M0 -7 L2 -2 L7 -3 L3 1 L5 6 L0 3 L-5 6 L-3 1 L-7 -3 L-2 -2Z" fill={t.particles[i % t.particles.length]} opacity={0.85} />
                  </motion.g>
                ) : t.id === 'summer' ? (
                  /* Lucioles : elles montent doucement en clignotant */
                  <motion.circle key={i} r={i % 3 ? 2.2 : 3} fill="#E9FF8A" initial={{ cx: p.x, cy: 90 + ((i * 97) % 460), opacity: 0 }} animate={{ cy: [90 + ((i * 97) % 460), 60 + ((i * 97) % 460)], cx: [p.x, p.x + (i % 2 ? 26 : -26), p.x], opacity: [0, 0.95, 0.2, 0.9, 0] }} transition={{ duration: 5 + (i % 4), repeat: Infinity, delay: p.delay * 0.5, ease: 'easeInOut' }} />
                ) : t.id === 'newyear' ? (
                  /* Paillettes d'or qui descendent en scintillant */
                  <motion.rect key={i} width={i % 3 ? 3 : 4.4} height={i % 3 ? 3 : 4.4} fill="#F2C14E" initial={{ x: p.x, y: -10 }} animate={{ y: [-10, H + 10], x: [p.x, p.x + (i % 2 ? 30 : -30)], rotate: [0, 360], opacity: [0.4, 1, 0.4, 1] }} transition={{ duration: p.d * 1.4, repeat: Infinity, delay: p.delay, ease: 'linear' }} />
                ) : t.id === 'winter' ? (
                  /* Flocons de neige */
                  <motion.circle key={i} r={i % 3 ? 2.6 : 3.8} fill="#FFFFFF" opacity={0.9} initial={{ cx: p.x, cy: -10 }} animate={{ cy: [-10, H + 10], cx: [p.x, p.x + (i % 2 ? 25 : -25), p.x] }} transition={{ duration: p.d * 1.3, repeat: Infinity, delay: p.delay, ease: 'linear' }} />
                ) : (
                  <motion.ellipse key={i} rx="3.5" ry="5.5" fill={SAKURA} opacity={0.9} initial={{ cx: p.x, cy: -10 }} animate={{ cy: [-10, H + 10], cx: [p.x, p.x + (i % 2 ? 40 : -40)], rotate: [0, 200] }} transition={{ duration: p.d, repeat: Infinity, delay: p.delay, ease: 'linear' }} />
                )
              ))}
          </g>

          {saga && t.id === 'winter' && (
            <g pointerEvents="none">
              {[{ x: 210, y: 250, s: 1 }, { x: 470, y: 120, s: 0.8 }, { x: 610, y: 400, s: 0.9 }, { x: 860, y: 330, s: 0.75 }, { x: 330, y: 500, s: 0.7 }].map((p, i) => (
                <Hitodama key={i} x={p.x} y={p.y} s={p.s} delay={i * 0.8} calm={calm} />
              ))}
            </g>
          )}

          {/* Bannière : la saga du niveau (ou la région) */}
          <g transform="translate(24 24)" pointerEvents="none">
            <rect width={(saga?.title ?? region).length * 10.5 + 60} height="44" rx="10" fill={t.banner.fill} stroke={t.banner.stroke} strokeWidth="2.5" />
            <circle cx="24" cy="22" r="11" fill={t.banner.seal} />
            <text x="24" y="22" dy="0.36em" textAnchor="middle" fontSize="12" fontWeight="900" className="jp" fill="#FFFFFF">{saga?.glyph ?? (t.id === 'korea' ? '한' : t.id === 'china' ? '中' : t.id === 'spain' ? 'Ñ' : t.id === 'germany' ? 'ß' : t.id === 'newyear' ? '新' : t.id === 'winter' ? '冬' : t.id === 'summer' ? '夏' : t.dusk ? '秋' : '島')}</text>
            <text x="44" y="22" dy="0.35em" fontSize="20" className="font-display" fill={t.banner.text}>{saga?.title ?? region}</text>
          </g>

          {/* Personnage sur l'île en cours */}
          <motion.g initial={{ x: pts[Math.max(0, current - 1)].x - 62, y: pts[Math.max(0, current - 1)].y - 104 }} animate={{ x: pts[current].x - 62, y: pts[current].y - 104 }} transition={{ duration: 1.1, ease: 'easeInOut' }} pointerEvents="none">
            <motion.g animate={calm ? undefined : { y: [0, -5, 0] }} transition={{ duration: 1.6, repeat: Infinity, ease: 'easeInOut' }}>
              <ellipse cx="30" cy="80" rx="20" ry="5" fill="#000" opacity={0.2} />
              <foreignObject width="60" height="68">
                <div style={{ borderRadius: 14, overflow: 'hidden', border: '3px solid #FFFFFF', boxShadow: '0 4px 10px rgba(0,0,0,.25)', background: 'var(--surface)' }}>
                  <Avatar config={avatar} size={54} title={T("Toi")} />
                </div>
              </foreignObject>
              {saga && (
                <g transform="translate(56 6)">
                  <circle r="12" fill="#FFFFFF" />
                  <circle r="10" fill={t.banner.seal} />
                  <text textAnchor="middle" dy="0.36em" fontSize="12" fontWeight="900" className="jp" fill="#FFFFFF">{saga.glyph}</text>
                </g>
              )}
            </motion.g>
          </motion.g>
        </svg>
      </div>
    </figure>
    </ThemeCtx.Provider>
  );
}
