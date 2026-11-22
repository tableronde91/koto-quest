/**
 * Illustrations de la partie 1 du TOEIC (« Photographs ») : scènes du quotidien professionnel dessinées en SVG.
 * Une seule source pour le web (image en data URI) et le mobile (SvgXml de react-native-svg).
 * Chaque scène est décrite par quatre phrases dans les banques d'examen ; une seule est exacte.
 */

const SKIN = ['#F2C9A0', '#C68A5E', '#8D5A3B', '#E8B48A'];
const INK = '#2B2A33';

/** Personne debout vue de face : tête, cheveux, buste, jambes. */
function person(x: number, y: number, shirt: string, skin = SKIN[0], hair = '#4A3326', opts: { skirt?: boolean; armUp?: boolean; armOut?: number } = {}) {
  const arm = opts.armUp
    ? `<path d="M${x + 9} ${y - 48} L${x + 24} ${y - 72}" stroke="${shirt}" stroke-width="6" stroke-linecap="round"/><circle cx="${x + 25}" cy="${y - 74}" r="3.5" fill="${skin}"/>`
    : opts.armOut && opts.armOut > 0
      ? `<path d="M${x + 9} ${y - 48} L${x + 9 + opts.armOut} ${y - 44}" stroke="${shirt}" stroke-width="6" stroke-linecap="round"/><circle cx="${x + 11 + opts.armOut}" cy="${y - 44}" r="3.5" fill="${skin}"/>`
      : `<path d="M${x + 9} ${y - 48} L${x + 12} ${y - 28}" stroke="${shirt}" stroke-width="6" stroke-linecap="round"/>`;
  const left = opts.armOut && opts.armOut < 0
    ? `<path d="M${x - 9} ${y - 48} L${x - 9 + opts.armOut} ${y - 44}" stroke="${shirt}" stroke-width="6" stroke-linecap="round"/><circle cx="${x - 11 + opts.armOut}" cy="${y - 44}" r="3.5" fill="${skin}"/>`
    : `<path d="M${x - 9} ${y - 48} L${x - 12} ${y - 28}" stroke="${shirt}" stroke-width="6" stroke-linecap="round"/>`;
  const legs = opts.skirt
    ? `<path d="M${x - 10} ${y - 24} L${x + 10} ${y - 24} L${x + 13} ${y - 10} L${x - 13} ${y - 10}Z" fill="${INK}"/><path d="M${x - 5} ${y - 10} V${y} M${x + 5} ${y - 10} V${y}" stroke="${skin}" stroke-width="4"/>`
    : `<path d="M${x - 5} ${y - 24} V${y} M${x + 5} ${y - 24} V${y}" stroke="${INK}" stroke-width="7" stroke-linecap="round"/>`;
  return `<g>${legs}<rect x="${x - 10}" y="${y - 52}" width="20" height="30" rx="6" fill="${shirt}"/>${left}${arm}<circle cx="${x}" cy="${y - 62}" r="10" fill="${skin}"/><path d="M${x - 10} ${y - 63} Q${x} ${y - 78} ${x + 10} ${y - 63} Q${x} ${y - 70} ${x - 10} ${y - 63}Z" fill="${hair}"/></g>`;
}

/** Personne assise de profil (tournée vers la droite). */
function seated(x: number, y: number, shirt: string, skin = SKIN[0], hair = '#4A3326') {
  return `<g><path d="M${x} ${y - 20} H${x + 18} V${y}" stroke="${INK}" stroke-width="7" stroke-linecap="round" fill="none"/><rect x="${x - 8}" y="${y - 50}" width="16" height="32" rx="6" fill="${shirt}"/><path d="M${x + 4} ${y - 44} L${x + 20} ${y - 34}" stroke="${shirt}" stroke-width="6" stroke-linecap="round"/><circle cx="${x + 1}" cy="${y - 60}" r="10" fill="${skin}"/><path d="M${x - 9} ${y - 62} Q${x - 2} ${y - 76} ${x + 10} ${y - 64} Q${x - 1} ${y - 68} ${x - 9} ${y - 62}Z" fill="${hair}"/></g>`;
}

const frame = (inner: string, bg = '#EAF1F4') =>
  `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 320 200" width="320" height="200"><rect width="320" height="200" fill="${bg}"/>${inner}</svg>`;

const chair = (x: number, y: number, c = '#5A6A7A') =>
  `<g><rect x="${x}" y="${y - 22}" width="16" height="4" fill="${c}"/><rect x="${x}" y="${y - 40}" width="4" height="22" fill="${c}"/><path d="M${x + 2} ${y - 18} V${y} M${x + 14} ${y - 18} V${y}" stroke="${c}" stroke-width="3"/></g>`;
const box = (x: number, y: number, w = 30, h = 24) =>
  `<g><rect x="${x}" y="${y - h}" width="${w}" height="${h}" fill="#C8955A" stroke="#8C6234" stroke-width="2"/><path d="M${x} ${y - h + 6} H${x + w}" stroke="#8C6234" stroke-width="2"/></g>`;

export const TOEIC_SCENES: Record<string, string> = {
  // Une femme tape sur un ordinateur portable à son bureau ; une plante, une fenêtre.
  'laptop-desk': frame(
    `<rect x="0" y="150" width="320" height="50" fill="#C9B79C"/><rect x="200" y="30" width="90" height="70" fill="#BFE0F0" stroke="#7A8A9A" stroke-width="4"/><path d="M245 30 V100" stroke="#7A8A9A" stroke-width="3"/>` +
      `<rect x="90" y="110" width="150" height="10" fill="#8C6234"/><path d="M100 120 V160 M230 120 V160" stroke="#8C6234" stroke-width="6"/>` +
      `<rect x="150" y="92" width="44" height="18" rx="2" fill="#3A4A5A"/><rect x="146" y="108" width="52" height="4" fill="#5A6A7A"/>` +
      seated(118, 160, '#3F8F9A', SKIN[1], '#1E1A18') +
      `<rect x="250" y="120" width="18" height="30" fill="#B85A3A"/><circle cx="259" cy="110" r="14" fill="#4F9A5A"/>`,
  ),
  // Réunion : trois personnes autour d'une table, l'une montre un graphique à l'écran.
  'meeting-chart': frame(
    `<rect x="0" y="160" width="320" height="40" fill="#B9A88C"/><rect x="180" y="20" width="120" height="80" fill="#FFFFFF" stroke="#5A6A7A" stroke-width="4"/>` +
      `<path d="M195 85 L220 70 L245 75 L280 35" stroke="#C8323F" stroke-width="4" fill="none"/><path d="M195 90 H290 M195 90 V30" stroke="#5A6A7A" stroke-width="2"/>` +
      `<rect x="30" y="120" width="130" height="10" fill="#7A5A3A"/><path d="M45 130 V165 M145 130 V165" stroke="#7A5A3A" stroke-width="6"/>` +
      seated(50, 160, '#C8423A', SKIN[0], '#B8862B') +
      seated(100, 160, '#3E5A9A', SKIN[2], '#1E1A18') +
      person(195, 165, '#2E7A5A', SKIN[3], '#4A3326', { armUp: true, skirt: true }),
  ),
  // Entrepôt : un homme porte un carton ; des cartons empilés, une camionnette.
  'warehouse-boxes': frame(
    `<rect x="0" y="160" width="320" height="40" fill="#9A9A9A"/>` +
      box(20, 160, 40, 30) + box(24, 130, 34, 26) + box(62, 160, 36, 28) +
      `<rect x="200" y="90" width="110" height="60" rx="6" fill="#F4F1EA" stroke="#5A6A7A" stroke-width="3"/><rect x="200" y="100" width="26" height="22" fill="#BFE0F0"/><circle cx="222" cy="155" r="10" fill="${INK}"/><circle cx="290" cy="155" r="10" fill="${INK}"/>` +
      person(140, 165, '#E2A23B', SKIN[1], '#1E1A18', { armOut: 14 }) + box(146, 128, 30, 22),
  ),
  // Café : un serveur verse du café dans la tasse d'une cliente assise.
  'cafe-pouring': frame(
    `<rect x="0" y="160" width="320" height="40" fill="#D8C2A0"/><rect x="120" y="118" width="90" height="8" fill="#7A5A3A"/><path d="M165 126 V165" stroke="#7A5A3A" stroke-width="6"/>` +
      seated(108, 162, '#B85A8A', SKIN[0], '#7A4A2A') +
      `<rect x="150" y="104" width="14" height="14" rx="2" fill="#FFFFFF" stroke="#5A6A7A" stroke-width="2"/>` +
      person(215, 165, '#FFFFFF', SKIN[2], '#1E1A18', { armOut: -20 }) +
      `<rect x="174" y="96" width="16" height="20" rx="4" fill="#5A6A7A"/><path d="M174 104 L166 100" stroke="#5A6A7A" stroke-width="4"/><path d="M165 102 Q160 106 158 112" stroke="#6A4428" stroke-width="3" fill="none"/>`,
    '#F6EEDF',
  ),
  // Gare : des voyageurs avec des valises attendent sur le quai ; un train à l'arrêt.
  'station-platform': frame(
    `<rect x="0" y="150" width="320" height="50" fill="#A8A8A8"/><path d="M0 150 H320" stroke="#F2D94E" stroke-width="5" stroke-dasharray="12 8"/>` +
      `<rect x="10" y="40" width="300" height="70" rx="14" fill="#2E5A8A"/>` +
      [30, 90, 150, 210, 270].map((x) => `<rect x="${x}" y="54" width="36" height="26" rx="3" fill="#BFE0F0"/>`).join('') +
      `<path d="M10 96 H310" stroke="#F4F1EA" stroke-width="4"/>` +
      person(80, 185, '#C8423A', SKIN[0], '#B8862B') + `<rect x="94" y="160" width="20" height="26" rx="3" fill="#5A3A6A"/><path d="M104 160 V150" stroke="${INK}" stroke-width="2"/>` +
      person(200, 185, '#3F7A4A', SKIN[1], '#1E1A18', { skirt: true }) + `<rect x="214" y="164" width="18" height="22" rx="3" fill="#8A6A2A"/>`,
  ),
  // Deux personnes se serrent la main devant une porte vitrée.
  'handshake-entrance': frame(
    `<rect x="0" y="165" width="320" height="35" fill="#B9B2A4"/><rect x="40" y="20" width="240" height="145" fill="#D8DEE4"/><rect x="120" y="50" width="80" height="115" fill="#9CC6D1" stroke="#5A6A7A" stroke-width="4"/><path d="M160 50 V165" stroke="#5A6A7A" stroke-width="3"/><rect x="110" y="26" width="100" height="16" fill="#3A4A5A"/>` +
      person(132, 185, '#3A4A5A', SKIN[0], '#7A4A2A', { armOut: 15 }) +
      person(188, 185, '#7A2E3A', SKIN[2], '#1E1A18', { armOut: -15, skirt: true }),
  ),
  // Salle de conférence vide : des rangées de chaises face à un écran.
  'empty-conference': frame(
    `<rect x="0" y="150" width="320" height="50" fill="#8A9A7A"/><rect x="90" y="18" width="140" height="80" fill="#FFFFFF" stroke="#5A6A7A" stroke-width="4"/><path d="M160 98 V110" stroke="#5A6A7A" stroke-width="3"/>` +
      [40, 80, 120, 160, 200, 240].map((x) => chair(x, 160)).join('') +
      [60, 100, 140, 180, 220, 260].map((x) => chair(x, 192, '#7A8A9A')).join(''),
  ),
  // Un homme passe à vélo devant des bancs vides dans un parc.
  'park-cyclist': frame(
    `<rect x="0" y="150" width="320" height="50" fill="#8FBF6A"/><path d="M0 165 H320" stroke="#C9B79C" stroke-width="20"/>` +
      `<circle cx="40" cy="70" r="30" fill="#4F9A5A"/><rect x="36" y="95" width="8" height="55" fill="#7A5A3A"/><circle cx="280" cy="60" r="34" fill="#5FAA6A"/><rect x="276" y="90" width="8" height="60" fill="#7A5A3A"/>` +
      `<rect x="200" y="128" width="50" height="6" fill="#8C6234"/><path d="M205 134 V148 M245 134 V148" stroke="${INK}" stroke-width="3"/><rect x="200" y="114" width="50" height="5" fill="#8C6234"/>` +
      `<circle cx="100" cy="170" r="14" fill="none" stroke="${INK}" stroke-width="3"/><circle cx="150" cy="170" r="14" fill="none" stroke="${INK}" stroke-width="3"/><path d="M100 170 L120 150 L150 170 M120 150 L140 150 L150 170 M118 150 L114 140" stroke="#C8323F" stroke-width="3" fill="none"/>` +
      `<rect x="112" y="112" width="16" height="28" rx="6" fill="#2E5A8A"/><path d="M120 136 L126 160" stroke="${INK}" stroke-width="6"/><path d="M124 120 L140 146" stroke="#2E5A8A" stroke-width="5"/><circle cx="122" cy="102" r="9" fill="${SKIN[3]}"/>`,
    '#DDEFF5',
  ),
  // Magasin : une cliente paie à la caisse ; un caissier derrière le comptoir.
  'shop-checkout': frame(
    `<rect x="0" y="160" width="320" height="40" fill="#C9C0AE"/><rect x="10" y="20" width="90" height="120" fill="#E8D8B8"/>` +
      [40, 75, 110].map((y) => `<path d="M10 ${y} H100" stroke="#8C6234" stroke-width="4"/>` + [18, 40, 62, 82].map((x) => `<rect x="${x}" y="${y - 14}" width="12" height="14" fill="${['#C8423A', '#3E5A9A', '#E2A23B', '#4F9A5A'][(x + y) % 4]}"/>`).join('')).join('') +
      person(200, 165, '#5A6A7A', SKIN[1], '#1E1A18') +
      `<rect x="150" y="112" width="120" height="50" fill="#7A5A3A"/><rect x="230" y="96" width="30" height="16" fill="#3A4A5A"/>` +
      person(120, 185, '#C84A8A', SKIN[0], '#B8862B', { armOut: 26, skirt: true }) + `<rect x="144" y="134" width="12" height="8" fill="#2E5A8A"/>`,
  ),
  // Un ouvrier sur une échelle repeint un mur.
  'ladder-painting': frame(
    `<rect x="0" y="170" width="320" height="30" fill="#B9B2A4"/><rect x="0" y="0" width="320" height="170" fill="#F4E8C8"/><rect x="0" y="0" width="150" height="170" fill="#BFD8E8"/>` +
      `<path d="M170 170 L200 50 M210 170 L232 50" stroke="#8A8E96" stroke-width="5"/>` +
      [70, 95, 120, 145].map((y) => `<path d="M${170 + (170 - y) * 0.25} ${y} H${210 + (170 - y) * 0.18}" stroke="#8A8E96" stroke-width="4"/>`).join('') +
      person(206, 120, '#E2A23B', SKIN[2], '#1E1A18', { armUp: true }) +
      `<rect x="226" y="36" width="14" height="10" fill="#7A9ABF"/><path d="M233 46 V58" stroke="#6A4428" stroke-width="3"/>` +
      `<rect x="250" y="150" width="22" height="20" fill="#7A9ABF" stroke="#4A6A8A" stroke-width="2"/>`,
  ),
};

/** Illustration d'une scène en data URI (balise <img> sur le web). */
export const toeicSceneUri = (id: string) => (TOEIC_SCENES[id] ? `data:image/svg+xml;utf8,${encodeURIComponent(TOEIC_SCENES[id])}` : null);

/** Accents des écoutes TOEIC : comme à l'examen, voix américaines, britanniques, canadiennes et australiennes. */
export const TOEIC_ACCENTS = ['en-US', 'en-GB', 'en-AU', 'en-CA'] as const;

/** Accent de chaque rôle (N, M, F) d'un document d'écoute : varie d'un document à l'autre, et d'un rôle à l'autre. */
export function scriptAccents(script: string): Record<string, string> {
  let h = 0;
  for (const c of script) h = (h * 31 + c.charCodeAt(0)) >>> 0;
  const o = h % TOEIC_ACCENTS.length;
  const at = (k: number) => TOEIC_ACCENTS[(o + k) % TOEIC_ACCENTS.length];
  return { N: at(0), M: at(1), F: at(2) };
}
