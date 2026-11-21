import type { ReactNode } from 'react';
import { T } from '../i18n';

/**
 * Gardiens de fin d'île : yokai originaux dessinés en SVG, style « chibi » cohérent avec l'avatar.
 * Une créature par sceau (glyphe). L'expression change selon le combat.
 */
export type BossMood = 'idle' | 'hurt' | 'angry' | 'ko' | 'laugh';

const INK = '#1F2433';

interface Species {
  body: string;
  belly: string;
  head?: string;
  /** Derrière le corps : queues, ailes, carapace */
  back?: ReactNode;
  /** Sur la tête : oreilles, cornes, coiffe */
  top?: ReactNode;
  /** Sous les yeux : masque, marques */
  under?: ReactNode;
  /** Sur le visage : bec, nez, moustaches */
  face?: ReactNode;
  /** Devant : objet tenu */
  front?: ReactNode;
  /** Couleur des yeux (clairs sur fond sombre) */
  eye?: string;
}

const ear = (x: number, flip: boolean, color: string, inner: string) => (
  <g transform={`translate(${x} 48) scale(${flip ? -1 : 1} 1)`}>
    <path d="M0 0 L16 -34 L30 4Z" fill={color} />
    <path d="M7 -2 L16 -24 L23 2Z" fill={inner} />
  </g>
);

const SPECIES: Record<string, Species> = {
  // ───── Gardiens coréens (TOPIK 1) ─────
  // Dokkaebi : lutin à corne unique, peau bleue, massue magique (bangmangi) à clous
  도: {
    body: '#4F7FBF', belly: '#BFD3EE', eye: '#FFFFFF',
    top: <><path d="M92 50 L100 18 L108 50Z" fill="#F2D98A" stroke="#C9A24A" strokeWidth="3" /><path d="M58 64 q-10 -18 6 -26 M142 64 q10 -18 -6 -26" stroke="#2E3F66" strokeWidth="8" fill="none" strokeLinecap="round" /></>,
    under: <><path d="M70 74 l18 6 M130 74 l-18 6" stroke="#22304F" strokeWidth="5" strokeLinecap="round" /></>,
    front: <g transform="rotate(-25 160 150)"><rect x="155" y="112" width="12" height="56" rx="5" fill="#8A5A34" /><ellipse cx="161" cy="112" rx="16" ry="22" fill="#A8743F" />{[[150, 100], [172, 100], [150, 122], [172, 122], [161, 92]].map(([x, y], i) => <circle key={i} cx={x} cy={y} r="3.5" fill="#E9E1CF" />)}</g>,
  },
  // Haetae : lion de pierre couleur de jade, crinière bouclée, petite corne, cloche au cou
  해: {
    body: '#8FB7A8', belly: '#D7E7DF', eye: INK,
    top: <>{[60, 78, 96, 114, 132, 150].map((x, i) => <circle key={x} cx={x - 5} cy={i % 2 ? 50 : 58} r="14" fill="#5F8F7E" />)}<path d="M94 40 L100 22 L106 40Z" fill="#E2B84A" /></>,
    face: <><ellipse cx="100" cy="104" rx="16" ry="10" fill="#B6D2C6" /><ellipse cx="100" cy="99" rx="7" ry="5" fill={INK} /></>,
    front: <><path d="M74 128 Q100 138 126 128" stroke="#B23A3A" strokeWidth="6" fill="none" /><circle cx="100" cy="140" r="7" fill="#E2B84A" stroke="#A57E22" strokeWidth="2" /></>,
  },
  // Gumiho : renarde à neuf queues, pelage doré, bijou bleu au front
  호: {
    body: '#F6E3BE', belly: '#FFF8EA', eye: INK,
    back: <>{[-48, -36, -24, -12, 0, 12, 24, 36, 48].map((a) => <path key={a} d="M100 150 Q144 124 162 74 Q174 112 144 150Z" fill="#F0D29C" stroke="#D9B577" strokeWidth="2.5" transform={`rotate(${a} 100 150)`} />)}{[-48, -24, 0, 24, 48].map((a) => <path key={a} d="M156 84 Q162 76 162 74 Q168 90 160 98Z" fill="#FFFFFF" transform={`rotate(${a} 100 150)`} />)}</>,
    top: <>{ear(56, false, '#F6E3BE', '#F2A7BB')}{ear(144, true, '#F6E3BE', '#F2A7BB')}</>,
    face: <><path d="M100 54 l-6 8 l6 8 l6 -8Z" fill="#2F5D8A" /><path d="M94 100 L106 100 L100 107Z" fill={INK} /></>,
  },
  // Tigre du conte (호랑이) : rayures noires, oreilles rondes, et le kaki séché qu'il redoute
  범: {
    body: '#E8913A', belly: '#FFF3DE', eye: INK,
    back: <path d="M148 158 Q196 150 186 104 Q176 96 172 108 Q178 138 146 140Z" fill="#E8913A" stroke="#1F2433" strokeWidth="0" />,
    top: <><circle cx="66" cy="54" r="15" fill="#E8913A" /><circle cx="66" cy="54" r="7" fill="#FFF3DE" /><circle cx="134" cy="54" r="15" fill="#E8913A" /><circle cx="134" cy="54" r="7" fill="#FFF3DE" /></>,
    under: <>{[[100, 46, 100, 60], [84, 48, 88, 60], [116, 48, 112, 60], [58, 86, 72, 88], [142, 86, 128, 88]].map(([x1, y1, x2, y2], i) => <path key={i} d={`M${x1} ${y1} L${x2} ${y2}`} stroke={INK} strokeWidth="5" strokeLinecap="round" />)}</>,
    face: <><ellipse cx="100" cy="104" rx="18" ry="11" fill="#FFF3DE" /><path d="M94 98 L106 98 L100 104Z" fill={INK} /></>,
    front: <g transform="translate(150 150)"><ellipse rx="11" ry="9" fill="#D9682B" /><path d="M-4 -9 q4 -6 8 0" stroke="#5B3A2A" strokeWidth="2.5" fill="none" /></g>,
  },
  // Imugi : serpent d'eau qui rêve de devenir dragon (pas encore de cornes), crête et perle convoitée
  무: {
    body: '#3E8E6B', belly: '#CFE8C9', eye: '#FFF3C4',
    back: <path d="M60 170 Q20 150 34 116 Q48 92 30 70 Q60 84 54 118 Q48 146 84 160Z" fill="#3E8E6B" stroke="#2C6A4F" strokeWidth="3" />,
    top: <>{[70, 86, 100, 114, 130].map((x, i) => <path key={x} d={`M${x - 7} ${54 - (i % 2) * 2} L${x} ${34 - (i === 2 ? 8 : 0)} L${x + 7} ${54 - (i % 2) * 2}Z`} fill="#6FC1A0" />)}</>,
    face: <><path d="M86 108 q14 8 28 0" stroke="#2C6A4F" strokeWidth="3" fill="none" /><circle cx="92" cy="102" r="2" fill="#2C6A4F" /><circle cx="108" cy="102" r="2" fill="#2C6A4F" /></>,
    front: <><circle cx="158" cy="150" r="13" fill="#E9F4FF" stroke="#9FD8FF" strokeWidth="3" /><circle cx="154" cy="146" r="4" fill="#FFFFFF" /></>,
  },
  // Bulgasari : monstre de bronze mangeur de fer, couvert de plaques et de piquants, une cloche avalée à moitié
  불: {
    body: '#8C6E4E', belly: '#C9A97A', eye: '#FFD27A',
    back: <>{[0, 1, 2, 3, 4].map((i) => <path key={i} d={`M${48 + i * 26} ${108 - (i === 2 ? 6 : 0)} l13 -28 l13 28Z`} fill="#6B5238" />)}</>,
    top: <><path d="M70 48 L62 26 L82 42Z M130 48 L138 26 L118 42Z" fill="#B8865A" /></>,
    under: <>{[[70, 120], [130, 120], [100, 170]].map(([x, y], i) => <rect key={i} x={x - 9} y={y - 6} width="18" height="12" rx="3" fill="#A88A62" stroke="#6B5238" strokeWidth="2" />)}</>,
    front: <g transform="translate(152 160)"><path d="M-12 8 Q-13 -10 0 -14 Q13 -10 12 8Z" fill="#C9A24A" stroke="#8C6A2A" strokeWidth="2" /><rect x="-13" y="6" width="26" height="4" rx="2" fill="#8C6A2A" /></g>,
  },
  // Jeoseung saja : messager de l'au-delà, robe noire, visage pâle, grand chapeau gat
  저: {
    body: '#2B2B33', belly: '#3A3A44', head: '#ECE6DC', eye: INK,
    top: <><ellipse cx="100" cy="46" rx="64" ry="10" fill="#141418" /><rect x="76" y="14" width="48" height="34" rx="10" fill="#141418" /><path d="M58 50 q-6 30 4 46 M142 50 q6 30 -4 46" stroke="#5A4632" strokeWidth="2" strokeDasharray="3 4" fill="none" /></>,
    under: <><path d="M70 74 q10 -6 20 0 M110 74 q10 -6 20 0" stroke="#5A5A66" strokeWidth="3" fill="none" /></>,
    front: <g transform="translate(150 146)"><rect x="-10" y="-14" width="20" height="28" rx="2" fill="#F6EBD3" stroke="#8C7A5A" strokeWidth="2" /><path d="M-6 -6 H6 M-6 0 H6 M-6 6 H4" stroke="#B23A3A" strokeWidth="2" /></g>,
  },
  // Dragon de la mer de l'Est : bois de cerf dorés, moustaches, perle
  용: {
    body: '#2E8B7A', belly: '#F2D98A', eye: '#FFF3C4',
    back: <path d="M150 156 Q196 132 180 92 Q172 112 156 116 Q170 134 140 146Z" fill="#2E8B7A" stroke="#1F5C52" strokeWidth="3" />,
    top: <><path d="M74 52 L60 22 M66 36 L52 30 M126 52 L140 22 M134 36 L148 30" stroke="#E2B84A" strokeWidth="6" strokeLinecap="round" /><path d="M84 46 q16 -14 32 0" stroke="#1F5C52" strokeWidth="5" fill="none" /></>,
    face: <><ellipse cx="100" cy="104" rx="20" ry="12" fill="#5FB7A4" /><circle cx="93" cy="101" r="2.5" fill="#1F5C52" /><circle cx="107" cy="101" r="2.5" fill="#1F5C52" /><path d="M82 108 q-26 4 -34 20 M118 108 q26 4 34 20" stroke="#E2B84A" strokeWidth="3" fill="none" strokeLinecap="round" /></>,
    front: <><circle cx="100" cy="176" r="10" fill="#E9F4FF" stroke="#E2B84A" strokeWidth="3" /></>,
  },

  // ───── Gardiens coréens (TOPIK 2) ─────
  // Jangseung : totem de bois du village, chapeau noir, sourcils broussailleux, gros nez
  장: {
    body: '#A8743F', belly: '#C9935A', eye: INK,
    top: <><rect x="72" y="14" width="56" height="34" rx="6" fill="#1F2433" /><ellipse cx="100" cy="46" rx="44" ry="7" fill="#1F2433" /></>,
    under: <><path d="M64 70 q16 -12 30 0 M106 70 q14 -12 30 0" stroke="#3B2A1A" strokeWidth="7" fill="none" strokeLinecap="round" /><circle cx="80" cy="84" r="13" fill="#F4EEDF" /><circle cx="120" cy="84" r="13" fill="#F4EEDF" /></>,
    face: <><path d="M92 92 Q100 112 108 92Z" fill="#8A5A34" /><path d="M86 112 l4 6 l4 -6 M106 112 l4 6 l4 -6" stroke="#FFFFFF" strokeWidth="3" fill="none" /></>,
    front: <>{[110, 126, 142].map((y) => <path key={y} d={`M74 ${y} H126`} stroke="#8A5A34" strokeWidth="2" opacity={0.6} />)}<text x="100" y="166" textAnchor="middle" fontSize="16" fontWeight="900" fill="#B23A3A">대장군</text></>,
  },
  // Crapaud d'or (금두꺼비) : peau dorée à pustules, larges yeux, pièce trouée (yeopjeon)
  두: {
    body: '#E2B84A', belly: '#F6E3A8', eye: INK,
    top: <><circle cx="76" cy="56" r="18" fill="#E2B84A" /><circle cx="124" cy="56" r="18" fill="#E2B84A" /></>,
    under: <>{[[64, 100], [136, 100], [86, 60], [114, 60], [100, 54]].map(([x, y], i) => <circle key={i} cx={x} cy={y} r="4" fill="#C9962A" />)}</>,
    face: <path d="M68 108 Q100 124 132 108" stroke="#8C6A2A" strokeWidth="4" fill="none" strokeLinecap="round" />,
    front: <g transform="translate(100 150)"><circle r="16" fill="#C9A24A" stroke="#8C6A2A" strokeWidth="3" /><rect x="-5" y="-5" width="10" height="10" fill="#F6E3A8" stroke="#8C6A2A" strokeWidth="2" /></g>,
  },
  // Pie (까치) : plumage noir et blanc aux reflets bleus, longue queue, bec noir
  까: {
    body: '#26304A', belly: '#FFFFFF', eye: '#FFFFFF',
    back: <><path d="M148 150 L196 176 L188 160 L198 150Z" fill="#26304A" /><path d="M58 116 Q10 96 18 150 Q38 138 60 150Z" fill="#3B5BA5" /><path d="M142 116 Q190 96 182 150 Q162 138 140 150Z" fill="#3B5BA5" /><path d="M24 140 Q36 128 52 132 M176 140 Q164 128 148 132" stroke="#FFFFFF" strokeWidth="5" fill="none" /></>,
    face: <path d="M90 96 L110 96 L100 116Z" fill="#141418" stroke="#3B5BA5" strokeWidth="2" />,
  },
  // Samjogo : corbeau à trois pattes, oiseau du soleil, disque rouge derrière lui
  삼: {
    body: '#2B2B33', belly: '#4A4A55', eye: '#FFD27A',
    back: <><circle cx="100" cy="92" r="84" fill="#D9483B" opacity={0.85} /><path d="M58 120 Q14 92 22 150 Q42 138 62 150Z" fill="#1A1A20" /><path d="M142 120 Q186 92 178 150 Q158 138 138 150Z" fill="#1A1A20" /></>,
    top: <path d="M86 44 Q100 26 114 44" stroke="#1A1A20" strokeWidth="8" fill="none" strokeLinecap="round" />,
    face: <path d="M88 96 Q100 90 112 96 L100 120Z" fill="#E2B84A" stroke="#A57E22" strokeWidth="2" />,
    front: <ellipse cx="100" cy="186" rx="13" ry="8" fill="#2B2B33" />,
  },
  // Grand-mère Seolmundae : géante de Jeju, chignon et épingle, jupe moussue pleine de terre et de pierres
  설: {
    body: '#6E8B5A', belly: '#C9D9B0', head: '#F2D6B8', eye: INK,
    top: <><circle cx="100" cy="40" r="20" fill="#9A9A9A" /><path d="M70 40 H130" stroke="#E2B84A" strokeWidth="5" strokeLinecap="round" /><path d="M58 70 Q60 40 100 40 Q140 40 142 70" fill="#B0B0B0" /></>,
    under: <><path d="M70 72 q10 -4 20 0 M110 72 q10 -4 20 0" stroke="#9A9A9A" strokeWidth="3" fill="none" /></>,
    front: <>{[[80, 150, '#5C5348'], [100, 158, '#7E776C'], [120, 148, '#5C5348'], [92, 138, '#4A3F36']].map(([x, y, c], i) => <ellipse key={i} cx={x as number} cy={y as number} rx="11" ry="8" fill={c as string} />)}<path d="M66 162 Q100 186 134 162" stroke="#4E6B3E" strokeWidth="5" fill="none" /></>,
  },
  // Masque de Hahoe : masque de bois souriant aux joues ridées, mâchoire détachée, robe sombre
  탈: {
    body: '#3E4C6B', belly: '#E9E1CF', head: '#E9D3A8', eye: INK,
    under: <><path d="M62 96 q8 6 4 16 M138 96 q-8 6 -4 16" stroke="#B8935A" strokeWidth="3" fill="none" /><path d="M76 66 q6 -6 12 0 M112 66 q6 -6 12 0" stroke="#7A5A34" strokeWidth="3" fill="none" /></>,
    face: <><path d="M94 92 Q100 104 106 92" stroke="#B8935A" strokeWidth="3" fill="none" /><path d="M78 110 Q100 126 122 110 Q100 118 78 110Z" fill={INK} /><path d="M80 124 Q100 140 120 124 L116 132 Q100 142 84 132Z" fill="#D9BE8C" stroke="#B8935A" strokeWidth="2" /></>,
  },
  // Bonghwang : phénix royal, crête, queue en éventail aux couleurs du dancheong, bec d'or
  봉: {
    body: '#D9483B', belly: '#F2C14E', eye: INK,
    back: <>{[-50, -25, 0, 25, 50].map((a, i) => <path key={a} d="M100 150 Q120 90 100 30 Q80 90 100 150Z" fill={['#2E8B7A', '#2F5D8A', '#E2B84A', '#2F5D8A', '#2E8B7A'][i]} transform={`rotate(${a} 100 150)`} />)}</>,
    top: <><path d="M100 46 Q92 24 104 12 Q100 28 112 34 Q104 36 100 46Z" fill="#E2B84A" /><circle cx="104" cy="14" r="5" fill="#2E8B7A" /></>,
    face: <path d="M90 96 Q100 90 110 96 L100 114Z" fill="#E2B84A" stroke="#A57E22" strokeWidth="2" />,
  },
  // Tigre blanc (백호) : pelage blanc à rayures noires, yeux bleus, gardien de l'Ouest
  백: {
    body: '#F4F1EA', belly: '#FFFFFF', eye: '#2F5D8A',
    back: <path d="M148 158 Q196 150 186 104 Q176 96 172 108 Q178 138 146 140Z" fill="#F4F1EA" stroke="#C9C2B4" strokeWidth="2" />,
    top: <><circle cx="66" cy="54" r="15" fill="#F4F1EA" stroke="#C9C2B4" strokeWidth="2" /><circle cx="66" cy="54" r="7" fill="#F2A7BB" /><circle cx="134" cy="54" r="15" fill="#F4F1EA" stroke="#C9C2B4" strokeWidth="2" /><circle cx="134" cy="54" r="7" fill="#F2A7BB" /></>,
    under: <>{[[100, 46, 100, 60], [84, 48, 88, 60], [116, 48, 112, 60], [58, 86, 72, 88], [142, 86, 128, 88], [60, 100, 72, 98], [140, 100, 128, 98]].map(([x1, y1, x2, y2], i) => <path key={i} d={`M${x1} ${y1} L${x2} ${y2}`} stroke={INK} strokeWidth="5" strokeLinecap="round" />)}</>,
    face: <><ellipse cx="100" cy="104" rx="18" ry="11" fill="#FFFFFF" stroke="#E2DED4" strokeWidth="2" /><path d="M94 98 L106 98 L100 104Z" fill="#D2526A" /></>,
    front: <>{[[74, 140], [126, 140], [100, 168]].map(([x, y], i) => <path key={i} d={`M${x - 8} ${y} L${x + 8} ${y + 4}`} stroke={INK} strokeWidth="4" strokeLinecap="round" />)}</>,
  },

  // ───── Gardiens coréens (TOPIK 3) ─────
  // Jangsanbeom : bête au long pelage blanc qui imite les voix, crinière en mèches
  산: {
    body: '#EDEAE2', belly: '#FFFFFF', eye: '#B23A3A',
    back: <>{Array.from({ length: 11 }, (_, i) => <path key={i} d={`M100 90 Q${40 + i * 12} ${40 + (i % 2) * 10} ${30 + i * 14} ${150 + (i % 3) * 8}`} stroke="#DAD5CA" strokeWidth="10" fill="none" strokeLinecap="round" />)}</>,
    top: <><path d="M60 64 Q56 30 76 40 M140 64 Q144 30 124 40" stroke="#DAD5CA" strokeWidth="9" fill="none" strokeLinecap="round" /></>,
    face: <><path d="M90 98 L110 98 L100 106Z" fill="#B8AFA0" /><path d="M86 110 q14 10 28 0" stroke="#8A8275" strokeWidth="3" fill="none" /><path d="M60 100 H78 M122 100 H140" stroke="#B8AFA0" strokeWidth="2" /></>,
  },
  // Eoduksini : ombre noire qui grandit, yeux jaunes, contours vaporeux
  둑: {
    body: '#22222E', belly: '#2E2E3C', eye: '#F2D94E',
    back: <>{[[40, 70, 30], [160, 60, 34], [30, 140, 26], [172, 136, 28], [100, 30, 36]].map(([x, y, r], i) => <circle key={i} cx={x} cy={y} r={r} fill="#22222E" opacity={0.55} />)}</>,
    top: <path d="M62 60 Q70 28 84 46 Q92 20 104 42 Q116 18 122 46 Q134 26 140 60Z" fill="#22222E" />,
    under: <><ellipse cx="80" cy="84" rx="15" ry="12" fill="#14141C" /><ellipse cx="120" cy="84" rx="15" ry="12" fill="#14141C" /></>,
  },
  // Esprit du grand arbre (dangsan namu) : feuillage, tronc, corde de paille sacrée et rubans
  당: {
    body: '#7A5A3A', belly: '#9A7650', head: '#5E9E5A', eye: INK,
    back: <>{[[50, 70], [150, 70], [70, 40], [130, 40], [100, 26]].map(([x, y], i) => <circle key={i} cx={x} cy={y} r="30" fill="#4E8A4A" />)}</>,
    front: <><path d="M56 120 Q100 136 144 120" stroke="#D9C38A" strokeWidth="7" fill="none" />{[70, 90, 110, 130].map((x, i) => <path key={x} d={`M${x} ${126 + (i % 2) * 3} v22`} stroke={['#D9483B', '#2F5D8A', '#F2C14E', '#FFFFFF'][i]} strokeWidth="5" strokeLinecap="round" />)}</>,
  },
  // Cheval céleste (천마) : cheval blanc ailé, crinière de flammes
  천: {
    body: '#F6F3EC', belly: '#FFFFFF', eye: INK,
    back: <><path d="M58 120 Q8 70 22 150 Q40 132 62 146Z" fill="#E9D9B0" stroke="#C9A24A" strokeWidth="2" /><path d="M142 120 Q192 70 178 150 Q160 132 138 146Z" fill="#E9D9B0" stroke="#C9A24A" strokeWidth="2" /></>,
    top: <><path d="M72 56 L66 32 L84 46Z M128 56 L134 32 L116 46Z" fill="#F6F3EC" stroke="#D9D2C2" strokeWidth="2" />{[0, 1, 2, 3].map((i) => <path key={i} d={`M${84 + i * 10} 46 q-6 -18 4 -26 q-2 12 8 18`} fill="#E36A3A" />)}</>,
    face: <><ellipse cx="100" cy="106" rx="20" ry="12" fill="#ECE5D6" /><circle cx="93" cy="106" r="2.5" fill={INK} /><circle cx="107" cy="106" r="2.5" fill={INK} /></>,
  },
  // Cerf de longévité : bois de corail, taches claires, champignon de l'immortalité
  록: {
    body: '#C98A4E', belly: '#F2DDB8', eye: INK,
    top: <><path d="M76 52 L66 20 M70 34 L56 26 M68 28 L74 14 M124 52 L134 20 M130 34 L144 26 M132 28 L126 14" stroke="#E36A5A" strokeWidth="6" strokeLinecap="round" /></>,
    under: <>{[[64, 120], [136, 124], [78, 146], [124, 150]].map(([x, y], i) => <circle key={i} cx={x} cy={y} r="5" fill="#F6E7CC" />)}</>,
    face: <ellipse cx="100" cy="104" rx="8" ry="6" fill={INK} />,
    front: <g transform="translate(152 162)"><path d="M-12 0 Q-12 -14 0 -16 Q12 -14 12 0Z" fill="#C8323F" /><rect x="-3" y="0" width="6" height="10" rx="2" fill="#E9D9B0" /></g>,
  },
  // Mulgwisin : esprit des eaux, peau bleutée, cheveux trempés, algues
  물: {
    body: '#5E8FA8', belly: '#A8CCDA', head: '#9FC2D0', eye: '#FFFFFF',
    top: <path d="M54 92 Q50 40 100 38 Q150 40 146 92 Q140 64 128 78 Q120 56 100 62 Q80 56 72 78 Q60 64 54 92Z" fill="#1F3D4E" />,
    under: <><path d="M68 70 q4 20 -2 34 M132 70 q-4 20 2 34" stroke="#1F3D4E" strokeWidth="5" fill="none" strokeLinecap="round" /></>,
    front: <>{[[60, 150], [140, 154], [100, 172]].map(([x, y], i) => <path key={i} d={`M${x} ${y} q-6 -10 0 -20 q6 -10 0 -20`} stroke="#3E8E6B" strokeWidth="4" fill="none" strokeLinecap="round" />)}</>,
  },
  // Janghwa et Hongryeon : esprit d'une jeune fille en hanbok blanc, ruban rouge, fleur de lotus
  홍: {
    body: '#F4F1EC', belly: '#FFFFFF', head: '#F6E3D6', eye: INK,
    back: <path d="M54 150 Q40 176 60 190 Q80 176 70 150Z M146 150 Q160 176 140 190 Q120 176 130 150Z" fill="#F4F1EC" opacity={0.6} />,
    top: <><path d="M56 96 Q52 40 100 40 Q148 40 144 96 Q132 64 100 62 Q68 64 56 96Z" fill="#1F2433" /><path d="M136 70 Q156 76 150 120" stroke="#1F2433" strokeWidth="10" fill="none" strokeLinecap="round" /><path d="M144 112 l10 8 l-12 4Z" fill="#C8323F" /></>,
    front: <g transform="translate(100 150)"><path d="M0 0 Q-14 -6 -10 -18 Q-2 -10 0 -20 Q2 -10 10 -18 Q14 -6 0 0Z" fill="#F29BB8" /><path d="M-30 -24 Q0 -10 30 -24" stroke="#C8323F" strokeWidth="4" fill="none" /></g>,
  },
  // Préfet Byeon : magistrat cupide, chapeau gat, moustache, robe rouge et sacs d'or
  변: {
    body: '#B23A3A', belly: '#D9A93E', head: '#F2D6B8', eye: INK,
    top: <><ellipse cx="100" cy="48" rx="62" ry="9" fill="#141418" /><rect x="78" y="16" width="44" height="32" rx="8" fill="#141418" /></>,
    under: <path d="M66 72 l18 6 M134 72 l-18 6" stroke="#3B2F26" strokeWidth="5" strokeLinecap="round" />,
    face: <><path d="M80 108 Q90 102 100 108 Q110 102 120 108 Q110 112 100 110 Q90 112 80 108Z" fill="#3B2F26" /><path d="M94 100 L106 100 L100 106Z" fill="#D9A08A" /></>,
    front: <>{[[58, 162], [144, 164]].map(([x, y], i) => <g key={i} transform={`translate(${x} ${y})`}><path d="M-12 0 Q-14 -14 0 -16 Q14 -14 12 0Z" fill="#E2B84A" stroke="#A57E22" strokeWidth="2" /><text x="0" y="-3" textAnchor="middle" fontSize="10" fontWeight="900" fill="#8C6A2A">₩</text></g>)}</>,
  },

  // ───── Gardiens coréens (TOPIK 4) ─────
  // Serpent gardien du grenier (업구렁이) : grand serpent doré enroulé sur des sacs de riz
  업: {
    body: '#C9A24A', belly: '#F2E2B0', eye: INK,
    back: <path d="M30 170 Q10 120 60 110 Q20 96 40 70" stroke="#B08A34" strokeWidth="22" fill="none" strokeLinecap="round" />,
    under: <>{[[72, 132], [100, 142], [128, 132], [86, 156], [114, 156]].map(([x, y], i) => <path key={i} d={`M${x - 8} ${y} q8 -6 16 0`} stroke="#A57E22" strokeWidth="3" fill="none" />)}</>,
    face: <path d="M100 110 v10 M100 120 l-6 6 M100 120 l6 6" stroke="#C8323F" strokeWidth="3" strokeLinecap="round" />,
    front: <>{[[60, 176], [140, 176]].map(([x, y], i) => <g key={i} transform={`translate(${x} ${y})`}><path d="M-14 0 Q-16 -18 0 -20 Q16 -18 14 0Z" fill="#E9D9B0" stroke="#A8987A" strokeWidth="2" /><text x="0" y="-5" textAnchor="middle" fontSize="11" fontWeight="900" fill="#8A3A2A">米</text></g>)}</>,
  },
  // Yagwanggwi : petit fantôme du Nouvel An qui vole les souliers
  야: {
    body: '#EEF0F8', belly: '#FFFFFF', eye: INK,
    back: <path d="M50 150 Q46 186 64 176 Q72 192 84 180 Q100 196 116 180 Q128 192 136 176 Q154 186 150 150Z" fill="#EEF0F8" />,
    top: <path d="M100 40 L94 22 L106 22Z" fill="#9AA6D9" />,
    front: <>{[[56, 168, -20], [148, 170, 20]].map(([x, y, r], i) => <g key={i} transform={`translate(${x} ${y}) rotate(${r})`}><path d="M-14 0 Q-14 -8 -4 -8 L12 -6 Q16 0 10 2 H-12Z" fill={i ? '#D9483B' : '#2F5D8A'} /><path d="M-6 -8 Q0 -12 6 -7" stroke="#F2C14E" strokeWidth="2" fill="none" /></g>)}</>,
  },
  // Jowangsin : esprit du foyer, flamme sur la tête, tablier, bol d'eau claire
  조: {
    body: '#C8553D', belly: '#F2E2C4', head: '#F2D6B8', eye: INK,
    top: <><path d="M100 50 Q80 30 92 10 Q96 26 104 18 Q102 34 116 24 Q120 44 100 50Z" fill="#F29A3A" /><path d="M100 48 Q92 36 98 26 Q102 36 108 32 Q108 44 100 48Z" fill="#F2D94E" /></>,
    front: <g transform="translate(100 162)"><ellipse rx="18" ry="6" fill="#F6F3EC" stroke="#2F5D8A" strokeWidth="2" /><ellipse cy="-1" rx="13" ry="3" fill="#A8D8EA" /></g>,
  },
  // Grand-mère Samsin : déesse des naissances, coiffe blanche, cordon de naissance (금줄)
  신: {
    body: '#F4F1EC', belly: '#E9D9B0', head: '#F2D6B8', eye: INK,
    top: <><path d="M56 80 Q56 36 100 34 Q144 36 144 80 Q130 56 100 56 Q70 56 56 80Z" fill="#B0B0B0" /><path d="M52 70 Q100 20 148 70 Q100 50 52 70Z" fill="#FFFFFF" stroke="#DAD5CA" strokeWidth="2" /></>,
    under: <path d="M74 106 q4 4 8 0 M118 106 q4 4 8 0" stroke="#C9A98A" strokeWidth="2" fill="none" />,
    front: <><path d="M48 132 Q100 150 152 132" stroke="#D9C38A" strokeWidth="5" fill="none" />{[66, 84, 116, 134].map((x, i) => <g key={x}>{i % 2 ? <ellipse cx={x} cy={144} rx="4" ry="6" fill="#2E2E3C" /> : <path d={`M${x} 140 l-4 10 h8Z`} fill="#C8323F" />}</g>)}</>,
  },
  // Dueoksini : gobelin aux cheveux hirsutes, cornes, gourdin
  억: {
    body: '#5E7A3A', belly: '#9AB46A', head: '#7E9A4E', eye: '#F2D94E',
    top: <><path d="M48 80 Q40 40 64 54 Q60 22 88 40 Q96 14 112 40 Q138 22 136 54 Q160 40 152 80" fill="#3B2F26" /><path d="M78 40 L72 18 L86 34Z M122 40 L128 18 L114 34Z" fill="#E9D9B0" /></>,
    face: <><path d="M80 112 Q100 104 120 112 L116 122 Q100 116 84 122Z" fill={INK} /><path d="M88 112 l3 7 l3 -7 M106 112 l3 7 l3 -7" fill="#FFFFFF" /></>,
    front: <g transform="translate(156 150) rotate(20)"><rect x="-6" y="-46" width="12" height="52" rx="6" fill="#8A5A34" />{[-36, -24, -12].map((y) => <circle key={y} cx={y % 24 ? 6 : -6} cy={y} r="3" fill="#B8AFA0" />)}</g>,
  },
  // Gangcheori : bête de feu de la sécheresse, crinière de flammes, terre craquelée
  강: {
    body: '#B83A2A', belly: '#F29A3A', eye: '#F2D94E',
    back: <>{Array.from({ length: 7 }, (_, i) => <path key={i} d={`M${46 + i * 18} 90 Q${40 + i * 18} 40 ${56 + i * 18} 24 Q${52 + i * 18} 52 ${66 + i * 18} 60`} fill={i % 2 ? '#F29A3A' : '#E3542E'} />)}</>,
    face: <><path d="M88 102 L112 102 L100 112Z" fill="#5A1A10" /><path d="M84 116 Q100 126 116 116" stroke="#5A1A10" strokeWidth="3" fill="none" /></>,
    front: <path d="M44 186 L70 176 L84 186 L104 174 L120 186 L140 176 L158 186" stroke="#7A4E30" strokeWidth="3" fill="none" />,
  },
  // Chiens de feu (불개) : chien noir aux flammes bleues qui mord la lune
  개: {
    body: '#2B2B33', belly: '#4A4A55', eye: '#7FD0F2',
    back: <path d="M150 150 Q190 130 176 96 Q170 120 158 128 Q168 104 150 92 Q156 120 140 134Z" fill="#3F8FD9" />,
    top: <><path d="M62 70 L54 28 L84 54Z M138 70 L146 28 L116 54Z" fill="#2B2B33" /><path d="M64 60 L60 38 L76 54Z M136 60 L140 38 L124 54Z" fill="#3F8FD9" /></>,
    face: <><ellipse cx="100" cy="106" rx="20" ry="12" fill="#3A3A44" /><ellipse cx="100" cy="100" rx="7" ry="5" fill={INK} /><path d="M90 114 Q100 120 110 114" stroke="#7FD0F2" strokeWidth="2" fill="none" /></>,
    front: <g transform="translate(152 46)"><circle r="20" fill="#F6E7B0" /><circle cx="-12" cy="-6" r="10" fill="#2B2B33" /></g>,
  },
  // Hyeonmu : tortue noire du Nord enlacée par un serpent, carapace à motifs
  현: {
    body: '#2F3E4A', belly: '#5E7A6A', eye: '#E9FF8A',
    back: <><ellipse cx="100" cy="128" rx="80" ry="56" fill="#24313B" />{[[70, 112], [100, 100], [130, 112], [80, 144], [120, 144]].map(([x, y], i) => <path key={i} d={`M${x} ${y - 14} l12 7 v14 l-12 7 l-12 -7 v-14Z`} fill="none" stroke="#4E6A6A" strokeWidth="3" />)}</>,
    front: <path d="M36 150 Q60 110 100 150 Q140 190 166 140 Q176 118 160 110" stroke="#3E8E6B" strokeWidth="9" fill="none" strokeLinecap="round" />,
  },

  // ───── Gardiens coréens (TOPIK 5 — mythes et contes) ─────
  // Femme-escargot (우렁각시) : coquille spiralée dans le dos, bol de riz fumant
  우: {
    body: '#7FA88A', belly: '#E9EFD9', head: '#F2D6B8', eye: INK,
    back: <g transform="translate(100 120)"><circle r="70" fill="#C99A6A" /><path d="M0 0 m-56 0 a56 56 0 1 1 56 56 a40 40 0 1 1 -40 -40 a24 24 0 1 1 24 24 a10 10 0 1 1 -10 -10" stroke="#8A5E3A" strokeWidth="6" fill="none" /></g>,
    top: <path d="M58 74 Q58 34 100 32 Q142 34 142 74 Q128 52 100 52 Q72 52 58 74Z" fill="#2E2E3C" />,
    front: <g transform="translate(100 166)"><path d="M-20 -6 H20 Q18 10 0 12 Q-18 10 -20 -6Z" fill="#F6F3EC" stroke="#2F5D8A" strokeWidth="2" /><ellipse cy="-6" rx="18" ry="5" fill="#FFFFFF" /><path d="M-6 -14 q-4 -6 0 -12 M6 -14 q4 -6 0 -12" stroke="#C9D3EA" strokeWidth="2" fill="none" /></g>,
  },
  // Yeono et Seo-nyeo : rocher-tortue qui emporte vers le Japon, soleil et lune
  연: {
    body: '#6E7F8C', belly: '#B9C6CF', eye: INK,
    back: <><ellipse cx="100" cy="150" rx="86" ry="30" fill="#5A6773" /><path d="M14 176 Q40 166 64 176 T114 176 T164 176 T200 176" stroke="#3F8FD9" strokeWidth="5" fill="none" /></>,
    top: <><circle cx="60" cy="40" r="16" fill="#F29A3A" /><circle cx="142" cy="40" r="14" fill="#F6E7B0" /><circle cx="136" cy="36" r="10" fill="#6E7F8C" /></>,
    face: <path d="M90 112 Q100 118 110 112" stroke={INK} strokeWidth="3" fill="none" />,
  },
  // Enfant général ailé (아기장수) : petites ailes sous les bras, cheval-dragon
  아: {
    body: '#E9D9B0', belly: '#FFF6DE', head: '#F2D6B8', eye: INK,
    back: <><path d="M58 112 Q8 80 22 142 Q40 126 62 138Z" fill="#FFFFFF" stroke="#D9D4C8" strokeWidth="2" /><path d="M142 112 Q192 80 178 142 Q160 126 138 138Z" fill="#FFFFFF" stroke="#D9D4C8" strokeWidth="2" /></>,
    top: <><circle cx="100" cy="40" r="12" fill="#2E2E3C" /><path d="M60 70 Q60 40 100 40 Q140 40 140 70 Q120 54 100 56 Q80 54 60 70Z" fill="#2E2E3C" /></>,
    front: <g transform="translate(154 152)"><path d="M-14 0 Q-10 -26 8 -22 L20 -30 L16 -16 Q22 -4 12 4Z" fill="#3E8E6B" /><circle cx="6" cy="-18" r="2" fill="#F2D94E" /></g>,
  },
  // Garçon-arbre (나무도령) : tronc, feuillage en couronne, racines
  목: {
    body: '#8A5E3A', belly: '#B98A5E', eye: '#F6E7B0',
    back: <>{[[60, 50], [100, 30], [140, 50], [80, 34], [120, 34]].map(([x, y], i) => <circle key={i} cx={x} cy={y} r="26" fill={i % 2 ? '#4E9A4A' : '#3E7A3A'} />)}</>,
    under: <path d="M70 120 q6 -10 0 -20 M130 120 q-6 -10 0 -20" stroke="#6A4428" strokeWidth="3" fill="none" />,
    front: <path d="M60 184 Q66 170 76 176 M90 186 Q96 172 104 186 M124 176 Q134 170 140 184" stroke="#6A4428" strokeWidth="6" fill="none" strokeLinecap="round" />,
  },
  // Oneuri : jeune fille du jardin des saisons, fleurs des quatre saisons
  오: {
    body: '#D97A9A', belly: '#F7D9E2', head: '#F2D6B8', eye: INK,
    top: <><path d="M58 76 Q58 36 100 34 Q142 36 142 76 Q128 54 100 54 Q72 54 58 76Z" fill="#2E2E3C" />{[['#F2A7C0', 64], ['#4E9A4A', 86], ['#E36A3A', 114], ['#FFFFFF', 136]].map(([c, x], i) => <circle key={i} cx={x} cy={44 - (i % 2) * 6} r="7" fill={c as string} stroke="#B07A8A" strokeWidth="1.5" />)}</>,
    front: <g transform="translate(150 150)"><rect x="-3" y="-30" width="6" height="40" fill="#6A4428" /><circle cy="-34" r="10" fill="#F2A7C0" /></g>,
  },
  // Jacheongbi : déesse de l'agriculture, gerbe de céréales, fleurs magiques
  자: {
    body: '#C9A24A', belly: '#F2E2B0', head: '#F2D6B8', eye: INK,
    top: <><path d="M58 76 Q58 36 100 34 Q142 36 142 76 Q128 54 100 54 Q72 54 58 76Z" fill="#2E2E3C" /><path d="M86 30 L100 14 L114 30Z" fill="#E7B53B" /></>,
    front: <g transform="translate(150 160) rotate(-15)">{[-8, 0, 8].map((x) => <g key={x}><path d={`M${x} 0 V-50`} stroke="#A57E22" strokeWidth="3" />{[-46, -38, -30].map((y) => <ellipse key={y} cx={x} cy={y} rx="4" ry="6" fill="#E7B53B" />)}</g>)}<path d="M-12 -6 H12" stroke="#C8323F" strokeWidth="4" /></g>,
  },
  // Grand-mère Mago (마고할미) : géante qui modèle les montagnes
  마: {
    body: '#7A6A5A', belly: '#B8A890', head: '#E2C6A8', eye: INK,
    back: <path d="M0 186 L40 120 L70 160 L110 96 L150 150 L200 110 L200 186Z" fill="#5E6A5A" />,
    top: <><path d="M54 82 Q50 30 100 30 Q150 30 146 82 Q130 52 100 52 Q70 52 54 82Z" fill="#E8E4DA" /><circle cx="100" cy="30" r="14" fill="#E8E4DA" /></>,
    under: <path d="M72 100 q6 4 12 0 M116 100 q6 4 12 0" stroke="#B8987A" strokeWidth="2" fill="none" />,
    front: <g transform="translate(48 160)"><circle r="14" fill="#9A9A92" /><circle cx="6" cy="-4" r="4" fill="#B8B8B0" /></g>,
  },
  // Mujangseung : gardien de l'eau de vie, géant barbu, gourde de vie
  생: {
    body: '#3E5A7A', belly: '#9AB6D2', head: '#D9B898', eye: INK,
    top: <><path d="M60 74 L58 30 H142 L140 74 Q120 54 100 54 Q80 54 60 74Z" fill="#1F2433" /></>,
    face: <path d="M74 112 Q100 170 126 112 Q114 124 100 120 Q86 124 74 112Z" fill="#2E2E3C" />,
    front: <g transform="translate(150 150)"><path d="M0 -24 Q14 -24 12 -10 Q24 4 14 18 Q0 28 -14 18 Q-24 4 -12 -10 Q-14 -24 0 -24Z" fill="#E9C46A" stroke="#A57E22" strokeWidth="2" /><path d="M-6 -2 q6 -8 12 0 q-6 8 -12 0Z" fill="#7FD0F2" /></g>,
  },

  // ───── Gardiens coréens (TOPIK 6 — mythes fondateurs) ─────
  // Hwanung : fils du Ciel, couronne, trois sceaux célestes (천부인)
  환: {
    body: '#F2E2B0', belly: '#FFFFFF', head: '#F2D6B8', eye: INK,
    back: <circle cx="100" cy="80" r="76" fill="#F6E7B0" opacity={0.6} />,
    top: <><path d="M66 56 L72 26 L86 44 L100 20 L114 44 L128 26 L134 56Z" fill="#E7B53B" stroke="#A57E22" strokeWidth="2" /><circle cx="100" cy="34" r="4" fill="#C8323F" /></>,
    front: <>{[[56, 168, 'mirror'], [100, 176, 'sword'], [144, 168, 'bell']].map(([x, y, k]) => <g key={k as string} transform={`translate(${x} ${y})`}>{k === 'mirror' ? <circle r="11" fill="#D9D4C8" stroke="#A57E22" strokeWidth="3" /> : k === 'sword' ? <path d="M0 -20 V10 M-7 4 H7" stroke="#A8B4C0" strokeWidth="4" /> : <path d="M-9 8 Q-10 -12 0 -12 Q10 -12 9 8Z" fill="#C9A24A" />}</g>)}</>,
  },
  // Ungnyeo : ourse devenue femme, oreilles d'ourse, armoise et ail
  웅: {
    body: '#6A4A34', belly: '#C9A98A', head: '#F2D6B8', eye: INK,
    top: <><circle cx="62" cy="50" r="16" fill="#6A4A34" /><circle cx="62" cy="50" r="8" fill="#C9A98A" /><circle cx="138" cy="50" r="16" fill="#6A4A34" /><circle cx="138" cy="50" r="8" fill="#C9A98A" /><path d="M64 78 Q64 44 100 44 Q136 44 136 78 Q120 60 100 60 Q80 60 64 78Z" fill="#2E2E3C" /></>,
    front: <><g transform="translate(56 166)"><path d="M0 0 V-30 M0 -20 l-8 -8 M0 -14 l8 -8 M0 -26 l6 -6" stroke="#5E8A4A" strokeWidth="4" strokeLinecap="round" /></g><g transform="translate(146 170)"><path d="M0 -16 Q14 -10 10 4 Q0 12 -10 4 Q-14 -10 0 -16Z" fill="#F6F3EC" stroke="#C9C2B4" strokeWidth="2" /><path d="M0 -16 V2" stroke="#C9C2B4" strokeWidth="1.5" /></g></>,
  },
  // Jumong : archer né d'un œuf, arc tendu, carquois
  주: {
    body: '#2F5D8A', belly: '#A8C4DE', head: '#F2D6B8', eye: INK,
    back: <path d="M40 60 Q10 110 40 160" stroke="#8A5A34" strokeWidth="6" fill="none" />,
    top: <><path d="M62 74 Q62 40 100 40 Q138 40 138 74 Q120 58 100 58 Q80 58 62 74Z" fill="#2E2E3C" /><path d="M70 50 H130" stroke="#C8323F" strokeWidth="5" /></>,
    front: <><path d="M40 60 L40 160" stroke="#E9D9B0" strokeWidth="2" /><path d="M40 110 H140 M132 104 L144 110 L132 116" stroke="#6A4428" strokeWidth="3" fill="none" /><g transform="translate(160 170)"><ellipse rx="14" ry="18" fill="#F6F3EC" stroke="#C9C2B4" strokeWidth="2" /><path d="M-10 -2 L-4 4 L2 -4 L8 2" stroke="#C9C2B4" strokeWidth="2" fill="none" /></g></>,
  },
  // Bak Hyeokgeose : roi né d'un œuf de lumière, cheval blanc, halo
  박: {
    body: '#F6F3EC', belly: '#FFFFFF', head: '#F2D6B8', eye: INK,
    back: <>{Array.from({ length: 12 }, (_, i) => <path key={i} d="M0 -64 L4 -84 L-4 -84Z" fill="#F2D94E" transform={`translate(100 90) rotate(${i * 30})`} />)}<circle cx="100" cy="90" r="64" fill="#FFF3B0" opacity={0.7} /></>,
    top: <path d="M70 52 H130 L124 34 H76Z" fill="#E7B53B" stroke="#A57E22" strokeWidth="2" />,
    front: <g transform="translate(154 166)"><path d="M-14 0 Q-12 -20 4 -20 L14 -28 L12 -14 Q18 -4 10 2Z" fill="#FFFFFF" stroke="#C9C2B4" strokeWidth="2" /></g>,
  },
  // Esprit de la cloche d'Emille : grande cloche de bronze, ondes sonores
  종: {
    body: '#7A8A6A', belly: '#9AAA8A', eye: '#F6E7B0',
    back: <><path d="M40 170 Q30 60 100 40 Q170 60 160 170Z" fill="#5E6E4E" /><path d="M14 120 q-10 20 0 40 M186 120 q10 20 0 40 M4 110 q-14 30 0 60 M196 110 q14 30 0 60" stroke="#A8C4A0" strokeWidth="3" fill="none" /></>,
    top: <path d="M84 40 Q84 18 100 18 Q116 18 116 40" stroke="#4E5E3E" strokeWidth="8" fill="none" />,
    front: <g transform="translate(100 168)"><ellipse rx="14" ry="8" fill="#C9A24A" /><path d="M-6 0 l6 -4 l6 4 l-6 4Z" fill="#8A6A2A" /></g>,
  },
  // Manpasikjeok : flûte magique qui apaise les vagues, dragon de la mer de l'Est
  적: {
    body: '#2F8F9A', belly: '#BDE6EA', eye: '#FFFFFF',
    back: <path d="M10 170 Q40 150 60 170 T110 170 T160 170 T200 170 L200 200 L10 200Z" fill="#3F8FD9" opacity={0.7} />,
    top: <><path d="M72 52 Q62 26 76 16 Q74 36 86 46Z M128 52 Q138 26 124 16 Q126 36 114 46Z" fill="#E7B53B" /></>,
    face: <path d="M78 104 Q50 100 42 118 M122 104 Q150 100 158 118" stroke="#E7B53B" strokeWidth="3" fill="none" strokeLinecap="round" />,
    front: <g transform="translate(100 140) rotate(-20)"><rect x="-50" y="-5" width="100" height="10" rx="5" fill="#7A9A4A" />{[-30, -14, 2, 18, 34].map((x) => <circle key={x} cx={x} cy="0" r="2.5" fill="#3A4A2A" />)}<path d="M-50 -5 V5 M-20 -5 V5 M10 -5 V5" stroke="#5A7A3A" strokeWidth="2" /></g>,
  },
  // Cheoyong : danseur au masque rouge, chapeau de fleurs de pivoine
  처: {
    body: '#2F5D8A', belly: '#E7B53B', head: '#C8553D', eye: '#FFFFFF',
    top: <><path d="M62 60 Q62 30 100 26 Q138 30 138 60Z" fill="#141418" />{[[70, 34], [100, 22], [130, 34]].map(([x, y], i) => <g key={i}><circle cx={x} cy={y} r="10" fill="#E36A8A" /><circle cx={x} cy={y} r="4" fill="#F2D94E" /></g>)}</>,
    face: <><path d="M88 96 Q100 90 112 96 L100 112Z" fill="#A83A2A" /><path d="M82 118 Q100 128 118 118" stroke={INK} strokeWidth="3" fill="none" /></>,
    front: <><path d="M40 120 Q20 140 30 170" stroke="#F6F3EC" strokeWidth="10" fill="none" strokeLinecap="round" /><path d="M160 120 Q180 140 170 170" stroke="#F6F3EC" strokeWidth="10" fill="none" strokeLinecap="round" /></>,
  },
  // Dangun : roi fondateur, robe dorée, sceptre de l'arbre sacré, mont Taebaek
  단: {
    body: '#A57E22', belly: '#F2E2B0', head: '#F2D6B8', eye: INK,
    back: <path d="M0 190 L60 90 L100 130 L140 70 L200 190Z" fill="#5E6A5A" opacity={0.7} />,
    top: <><path d="M64 60 L68 22 H132 L136 60Z" fill="#141418" /><path d="M64 44 H136" stroke="#E7B53B" strokeWidth="4" /><circle cx="100" cy="32" r="5" fill="#3E8E6B" /></>,
    face: <path d="M82 112 Q100 150 118 112 Q100 122 82 112Z" fill="#3B2F26" />,
    front: <g transform="translate(156 176)"><path d="M0 0 V-70" stroke="#6A4428" strokeWidth="5" /><circle cy="-76" r="14" fill="#3E7A3A" /><circle cx="-8" cy="-82" r="8" fill="#4E9A4A" /></g>,
  },

  // ───── Gardiens japonais ─────
  // Kappa : carapace, bec, assiette d'eau sur la tête
  河: {
    body: '#5FA85A', belly: '#E8D98C', eye: INK,
    back: <ellipse cx="100" cy="132" rx="62" ry="54" fill="#3F6F3B" stroke="#2D5229" strokeWidth="4" />,
    top: <><ellipse cx="100" cy="44" rx="30" ry="9" fill="#DDEFF5" stroke="#9CC6D1" strokeWidth="3" /><path d="M64 56 l8 -14 l6 12 l8 -14 l6 12 l8 -12 l6 12 l8 -12 l6 14 l8 -12 l6 14" stroke="#2E5A2A" strokeWidth="5" fill="none" strokeLinejoin="round" /></>,
    face: <path d="M86 98 Q100 92 114 98 L100 112Z" fill="#E7B53B" stroke="#B88A1E" strokeWidth="2" />,
  },
  // Tanuki : masque sombre, oreilles rondes, feuille sur la tête
  狸: {
    body: '#9A6B45', belly: '#E9D3B0', eye: '#FFFFFF',
    back: <path d="M150 150 Q190 150 182 112 Q170 130 146 128Z" fill="#7A5235" />,
    top: <><circle cx="66" cy="54" r="14" fill="#6E4A2F" /><circle cx="134" cy="54" r="14" fill="#6E4A2F" /><path d="M96 34 Q112 14 124 30 Q112 40 96 34Z" fill="#6DA84E" /><path d="M96 34 L120 26" stroke="#4E7F36" strokeWidth="2" /></>,
    under: <><ellipse cx="80" cy="86" rx="20" ry="15" fill="#4A3020" /><ellipse cx="120" cy="86" rx="20" ry="15" fill="#4A3020" /></>,
    face: <ellipse cx="100" cy="102" rx="9" ry="6" fill={INK} />,
  },
  // Kitsune : renarde blanche, marques vermillon, trois queues
  狐: {
    body: '#F4EFE6', belly: '#FFFFFF', eye: INK,
    back: <>{[-30, 0, 30].map((a) => <path key={a} d="M100 150 Q150 120 170 70 Q182 110 150 150Z" fill="#F4EFE6" stroke="#E2D7C5" strokeWidth="3" transform={`rotate(${a} 100 150)`} />)}{[-30, 0, 30].map((a) => <path key={a} d="M163 80 Q170 72 170 70 Q176 86 168 96Z" fill="#E36A3A" transform={`rotate(${a} 100 150)`} />)}</>,
    top: <>{ear(56, false, '#F4EFE6', '#F2A7BB')}{ear(144, true, '#F4EFE6', '#F2A7BB')}</>,
    face: <><path d="M68 72 Q78 64 86 74" stroke="#D2352F" strokeWidth="4" fill="none" strokeLinecap="round" /><path d="M114 74 Q122 64 132 72" stroke="#D2352F" strokeWidth="4" fill="none" strokeLinecap="round" /><path d="M100 56 v10" stroke="#D2352F" strokeWidth="4" strokeLinecap="round" /><path d="M94 100 L106 100 L100 107Z" fill={INK} /></>,
  },
  // Tengu de la montagne : visage rouge, long nez, ailes, petite coiffe
  山: {
    body: '#3E4C6B', belly: '#E9DCC3', head: '#D9483B', eye: '#FFFFFF',
    back: <><path d="M60 120 Q10 90 18 150 Q40 140 62 150Z" fill="#2A2F3A" /><path d="M140 120 Q190 90 182 150 Q160 140 138 150Z" fill="#2A2F3A" /></>,
    top: <><path d="M86 42 L114 42 L108 26 L92 26Z" fill={INK} /><path d="M60 62 Q100 40 140 62" stroke="#FFFFFF" strokeWidth="8" fill="none" strokeLinecap="round" /></>,
    face: <path d="M94 96 Q100 92 106 96 L134 107 Q137 113 131 114 L100 108Z" fill="#C53A2E" stroke="#A12C22" strokeWidth="2" />,
  },
  // Maneki-neko : chat porte-bonheur, patte levée, grelot et pièce d'or
  招: {
    body: '#FBF8F1', belly: '#FFFFFF', eye: INK,
    back: <path d="M150 166 Q186 168 182 140" stroke="#FBF8F1" strokeWidth="12" fill="none" strokeLinecap="round" />,
    top: <>{ear(58, false, '#FBF8F1', '#F2A7BB')}{ear(142, true, '#FBF8F1', '#F2A7BB')}<path d="M118 50 Q132 46 138 58" fill="#E9A25A" /><circle cx="128" cy="56" r="10" fill="#E9A25A" opacity={0.8} /></>,
    face: <><path d="M95 100 L105 100 L100 105Z" fill="#D2526A" /><path d="M60 98 H80 M60 106 H80 M120 98 H140 M120 106 H140" stroke="#C9C2B4" strokeWidth="2" strokeLinecap="round" /></>,
    front: <><path d="M60 128 Q100 140 140 128" stroke="#C8323F" strokeWidth="7" fill="none" strokeLinecap="round" /><circle cx="100" cy="140" r="7" fill="#E7B53B" stroke="#B88A1E" strokeWidth="2" /><ellipse cx="148" cy="96" rx="13" ry="18" fill="#FBF8F1" stroke="#E2D7C5" strokeWidth="2" /><path d="M141 84 v6 M148 82 v7 M155 84 v6" stroke="#E2D7C5" strokeWidth="2" strokeLinecap="round" /><ellipse cx="100" cy="164" rx="16" ry="11" fill="#E7B53B" stroke="#B88A1E" strokeWidth="2" /><text x="100" y="169" textAnchor="middle" fontSize="12" fontWeight="900" fill="#8A6414">千</text></>,
  },
  // Raijū : bête de l'orage, fourrure hérissée, queue en éclair
  雷: {
    body: '#4F5DB8', belly: '#F6E7A8', eye: '#FFFFFF',
    back: <><path d="M146 160 L176 128 L162 126 L190 88 L150 120 L164 122 L138 150Z" fill="#FFD84A" stroke="#E0A800" strokeWidth="2" strokeLinejoin="round" />{[[34, 70], [176, 54]].map(([x, y], i) => <path key={i} d={`M${x} ${y} l8 -14 l-2 10 l8 -2 l-10 16 l2 -10Z`} fill="#FFD84A" />)}</>,
    top: <><path d="M62 70 L58 36 L78 52 L86 26 L98 46 L110 24 L118 48 L136 32 L138 66Z" fill="#3D4895" />{ear(56, false, '#4F5DB8', '#8F9BE0')}{ear(144, true, '#4F5DB8', '#8F9BE0')}</>,
    face: <><ellipse cx="100" cy="104" rx="14" ry="9" fill="#6C79D0" /><ellipse cx="100" cy="100" rx="6" ry="4" fill={INK} /></>,
  },
  // Chat-boulier : chat tigré qui tient un boulier
  算: {
    body: '#E8A64A', belly: '#FFF1D6', eye: INK,
    back: <path d="M148 160 Q196 150 186 104" stroke="#E8A64A" strokeWidth="14" fill="none" strokeLinecap="round" />,
    top: <>{ear(58, false, '#E8A64A', '#F7C9A0')}{ear(142, true, '#E8A64A', '#F7C9A0')}<path d="M92 46 l4 12 M100 44 v14 M108 46 l-4 12" stroke="#C47A22" strokeWidth="4" strokeLinecap="round" /></>,
    face: <><path d="M95 100 L105 100 L100 105Z" fill="#D2526A" /><path d="M60 98 H80 M60 106 H80 M120 98 H140 M120 106 H140" stroke={INK} strokeWidth="2" strokeLinecap="round" /></>,
    front: <g transform="translate(70 128)"><rect width="60" height="40" rx="4" fill="none" stroke="#7A4E2D" strokeWidth="5" />{[10, 20, 30].map((y) => <g key={y}><path d={`M2 ${y} H58`} stroke="#7A4E2D" strokeWidth="2" />{[12, 22, 40, 50].map((x, i) => <circle key={x} cx={x} cy={y} r="4" fill={i < 2 ? '#C8323F' : '#E7B53B'} />)}</g>)}</g>,
  },
  // Oni : peau rouge, cornes, cheveux en bataille, massue
  鬼: {
    body: '#D9483B', belly: '#F2C14E', eye: '#FFFFFF',
    top: <><path d="M74 58 L62 18 L90 46Z" fill="#F2C14E" stroke="#C9962A" strokeWidth="2" /><path d="M126 58 L138 18 L110 46Z" fill="#F2C14E" stroke="#C9962A" strokeWidth="2" /></>,
    under: <path d="M56 78 Q56 40 100 42 Q144 40 144 78 Q134 58 120 62 Q108 50 98 60 Q86 50 76 62 Q64 58 56 78Z" fill={INK} />,
    face: <><path d="M86 108 L90 116 L94 108 M106 108 L110 116 L114 108" fill="#FFFFFF" /><path d="M84 106 Q100 114 116 106" stroke={INK} strokeWidth="3" fill="none" /></>,
    front: <g transform="translate(142 96) rotate(20)"><rect x="-7" y="0" width="14" height="70" rx="6" fill="#6B4A2E" />{[10, 26, 42].map((y) => <circle key={y} cx="0" cy={y} r="3" fill="#C9C2B4" />)}</g>,
  },
  // Dragon des caractères : museau, cornes, moustaches, ventre écaillé
  龍: {
    body: '#2F8F7A', belly: '#E9D98C', eye: '#FFFFFF',
    back: <path d="M150 150 Q200 130 190 80 Q176 110 156 112 Q170 96 160 80" stroke="#2F8F7A" strokeWidth="16" fill="none" strokeLinecap="round" />,
    top: <><path d="M70 50 Q60 24 74 14 Q72 34 84 44Z" fill="#E7B53B" /><path d="M130 50 Q140 24 126 14 Q128 34 116 44Z" fill="#E7B53B" /><path d="M86 40 l6 -10 l6 10 l6 -10 l6 10" stroke="#1E6B5B" strokeWidth="4" fill="none" /></>,
    face: <><ellipse cx="100" cy="104" rx="24" ry="14" fill="#3FA68E" /><circle cx="92" cy="102" r="2.5" fill={INK} /><circle cx="108" cy="102" r="2.5" fill={INK} /><path d="M76 104 Q50 100 40 120 M124 104 Q150 100 160 120" stroke="#E7B53B" strokeWidth="3" fill="none" strokeLinecap="round" /></>,
  },
  // Karasu-tengu : corbeau bleu nuit, bec jaune, ailes
  天: {
    body: '#33416B', belly: '#C9D3EA', eye: '#FFFFFF',
    back: <><path d="M58 116 Q4 76 14 150 Q36 132 60 150Z" fill="#232C49" /><path d="M142 116 Q196 76 186 150 Q164 132 140 150Z" fill="#232C49" /></>,
    top: <><path d="M88 42 L112 42 L106 28 L94 28Z" fill={INK} /><path d="M72 52 Q100 36 128 52" stroke="#4A5A8C" strokeWidth="6" fill="none" /></>,
    face: <path d="M88 96 Q100 88 112 96 L100 122Z" fill="#E7B53B" stroke="#B88A1E" strokeWidth="2" />,
  },
  // Komainu : chien-lion de pierre, crinière bouclée dorée
  狛: {
    body: '#A7A39A', belly: '#D9D4C8', eye: INK,
    back: <>{Array.from({ length: 9 }, (_, i) => <circle key={i} cx={100 + Math.cos((i / 9) * Math.PI * 2) * 52} cy={86 + Math.sin((i / 9) * Math.PI * 2) * 50} r="17" fill="#C9A24A" stroke="#A88331" strokeWidth="3" />)}</>,
    top: <><circle cx="68" cy="54" r="10" fill="#8F8B82" /><circle cx="132" cy="54" r="10" fill="#8F8B82" /></>,
    face: <><ellipse cx="100" cy="104" rx="16" ry="10" fill="#8F8B82" /><ellipse cx="100" cy="98" rx="7" ry="5" fill={INK} /><path d="M80 66 Q88 60 94 68 M106 68 Q112 60 120 66" stroke="#6E6A62" strokeWidth="4" fill="none" strokeLinecap="round" /></>,
  },
  // Baku : tapir des rêves, trompe, étoiles
  獏: {
    body: '#8E7BC2', belly: '#D9CFF0', eye: INK,
    back: <>{[[40, 70], [168, 60], [176, 110]].map(([x, y], i) => <path key={i} d={`M${x} ${y - 8} L${x + 3} ${y - 2} L${x + 9} ${y} L${x + 3} ${y + 2} L${x} ${y + 8} L${x - 3} ${y + 2} L${x - 9} ${y} L${x - 3} ${y - 2}Z`} fill="#FFE08A" />)}</>,
    top: <><ellipse cx="64" cy="58" rx="12" ry="16" fill="#7564A8" /><ellipse cx="136" cy="58" rx="12" ry="16" fill="#7564A8" /></>,
    face: <path d="M90 96 Q100 92 110 96 Q112 120 104 132 Q98 138 94 130 Q100 122 96 110Z" fill="#7F6BB5" stroke="#6555A0" strokeWidth="2" />,
  },
  // Grue : blanche, calotte rouge, long bec, plumes noires
  鶴: {
    body: '#F7F5F0', belly: '#FFFFFF', head: '#F7F5F0', eye: INK,
    back: <><path d="M150 150 Q190 160 194 130 Q176 140 152 128Z" fill={INK} /><path d="M56 120 Q14 100 22 150 Q40 140 60 150Z" fill="#E8E4DA" /><path d="M144 120 Q186 100 178 150 Q160 140 140 150Z" fill="#E8E4DA" /></>,
    top: <ellipse cx="100" cy="46" rx="18" ry="10" fill="#D2352F" />,
    face: <><path d="M94 96 L100 92 L106 96 L102 132 L98 132Z" fill="#B9B2A3" /><path d="M64 118 Q100 136 136 118 L136 128 Q100 146 64 128Z" fill={INK} /></>,
  },
  // Kirin : cerf-dragon doré, bois, crinière de flammes
  麒: {
    body: '#D9A93E', belly: '#F6E3A8', eye: INK,
    back: <>{[0, 1, 2, 3, 4].map((i) => <path key={i} d="M0 0 Q-10 -20 0 -34 Q4 -18 12 -10Z" fill="#E36A3A" transform={`translate(${60 + i * 20} ${56 - Math.sin((i / 4) * Math.PI) * 10}) rotate(${-30 + i * 15})`} />)}</>,
    top: <><path d="M80 46 L72 18 M72 30 L62 22 M120 46 L128 18 M128 30 L138 22" stroke="#8A5A2B" strokeWidth="5" strokeLinecap="round" /></>,
    face: <><ellipse cx="100" cy="104" rx="18" ry="11" fill="#E9BE5A" /><circle cx="94" cy="102" r="2" fill={INK} /><circle cx="106" cy="102" r="2" fill={INK} />{[[70, 80], [130, 80], [84, 66], [116, 66]].map(([x, y], i) => <circle key={i} cx={x} cy={y} r="4" fill="#3FA68E" opacity={0.7} />)}</>,
  },
};

function Eyes({ mood, color, y = 84 }: { mood: BossMood; color: string; y?: number }) {
  if (mood === 'ko')
    return (
      <g stroke={color} strokeWidth="3.5" strokeLinecap="round">
        {[80, 120].map((x) => <path key={x} d={`M${x - 8} ${y - 8} L${x + 8} ${y + 8} M${x + 8} ${y - 8} L${x - 8} ${y + 8}`} />)}
      </g>
    );
  if (mood === 'hurt')
    return (
      <g stroke={color} strokeWidth="4" fill="none" strokeLinecap="round" strokeLinejoin="round">
        <path d={`M72 ${y - 6} L84 ${y} L72 ${y + 6}`} />
        <path d={`M128 ${y - 6} L116 ${y} L128 ${y + 6}`} />
      </g>
    );
  if (mood === 'laugh')
    return (
      <g stroke={color} strokeWidth="4" fill="none" strokeLinecap="round">
        <path d={`M72 ${y + 3} Q80 ${y - 7} 88 ${y + 3}`} />
        <path d={`M112 ${y + 3} Q120 ${y - 7} 128 ${y + 3}`} />
      </g>
    );
  return (
    <g>
      <g className="avatar-blink">
        <ellipse cx="80" cy={y} rx="7" ry="9" fill={color} />
        <ellipse cx="120" cy={y} rx="7" ry="9" fill={color} />
        {color !== '#FFFFFF' && <><circle cx="82.5" cy={y - 3} r="2.4" fill="#FFFFFF" /><circle cx="122.5" cy={y - 3} r="2.4" fill="#FFFFFF" /></>}
      </g>
      {mood === 'angry' && (
        <g stroke={INK} strokeWidth="5" strokeLinecap="round">
          <path d={`M68 ${y - 18} L90 ${y - 10}`} />
          <path d={`M132 ${y - 18} L110 ${y - 10}`} />
        </g>
      )}
    </g>
  );
}

function Mouth({ mood }: { mood: BossMood }) {
  if (mood === 'hurt' || mood === 'ko') return <ellipse cx="100" cy="118" rx="7" ry="5" fill={INK} />;
  if (mood === 'laugh' || mood === 'angry') return <path d="M86 114 Q100 130 114 114Z" fill={INK} />;
  return <path d="M92 116 Q100 122 108 116" stroke={INK} strokeWidth="3" fill="none" strokeLinecap="round" />;
}

/** Lanterne hantée (chōchin-obake) : la lanterne est le corps, un seul grand œil et une langue. */
function Lantern({ mood }: { mood: BossMood }) {
  return (
    <g>
      <rect x="82" y="22" width="36" height="10" rx="3" fill={INK} />
      <path d="M100 8 V22" stroke={INK} strokeWidth="3" />
      <ellipse cx="100" cy="100" rx="62" ry="72" fill="#F2E3C2" stroke="#D9C49A" strokeWidth="3" />
      {[50, 72, 94, 116, 138, 158].map((y) => <path key={y} d={`M${100 - Math.sqrt(Math.max(0, 1 - ((y - 100) / 72) ** 2)) * 62} ${y} Q100 ${y + 6} ${100 + Math.sqrt(Math.max(0, 1 - ((y - 100) / 72) ** 2)) * 62} ${y}`} stroke="#CDB688" strokeWidth="2" fill="none" />)}
      <rect x="82" y="168" width="36" height="10" rx="3" fill={INK} />
      <ellipse cx="100" cy="100" rx="70" ry="80" fill="#FFB65C" opacity={0.12} />
      {mood === 'ko' ? (
        <path d="M88 76 L112 100 M112 76 L88 100" stroke={INK} strokeWidth="5" strokeLinecap="round" />
      ) : (
        <g className={mood === 'hurt' ? undefined : 'avatar-blink'}>
          <ellipse cx="100" cy="86" rx="20" ry={mood === 'hurt' ? 4 : 18} fill="#FFFFFF" stroke={INK} strokeWidth="3" />
          {mood !== 'hurt' && <circle cx="104" cy="88" r="8" fill={INK} />}
        </g>
      )}
      <path d="M76 124 Q100 146 124 124" stroke={INK} strokeWidth="4" fill={mood === 'laugh' || mood === 'angry' ? INK : 'none'} />
      <path d="M100 132 Q110 160 98 172 Q92 160 96 136Z" fill="#D2526A" />
    </g>
  );
}

export function BossCreature({ glyph, mood = 'idle', size = 180, title }: { glyph: string; mood?: BossMood; size?: number; title?: string }) {
  if (glyph === '灯')
    return (
      <svg viewBox="0 0 200 200" width={size} height={size} role="img" aria-label={title ?? T("Gardien")} className="block overflow-visible">
        <Lantern mood={mood} />
      </svg>
    );
  const sp = SPECIES[glyph] ?? SPECIES['鬼'];
  const head = sp.head ?? sp.body;
  return (
    <svg viewBox="0 0 200 200" width={size} height={size} role="img" aria-label={title ?? T("Gardien")} className="block overflow-visible">
      {sp.back}
      {/* Pieds */}
      <ellipse cx="78" cy="182" rx="16" ry="9" fill={sp.body} stroke="rgb(0 0 0 / .15)" strokeWidth="2" />
      <ellipse cx="122" cy="182" rx="16" ry="9" fill={sp.body} stroke="rgb(0 0 0 / .15)" strokeWidth="2" />
      {/* Corps et ventre */}
      <ellipse cx="100" cy="140" rx="50" ry="44" fill={sp.body} />
      <ellipse cx="100" cy="148" rx="32" ry="30" fill={sp.belly} />
      {/* Bras */}
      <ellipse cx="54" cy="138" rx="12" ry="20" fill={sp.body} transform="rotate(20 54 138)" />
      <ellipse cx="146" cy="138" rx="12" ry="20" fill={sp.body} transform="rotate(-20 146 138)" />
      {/* Tête */}
      {sp.top}
      <circle cx="100" cy="88" r="46" fill={head} />
      <ellipse cx="72" cy="104" rx="8" ry="5" fill="#F2A7A0" opacity={0.5} />
      <ellipse cx="128" cy="104" rx="8" ry="5" fill="#F2A7A0" opacity={0.5} />
      {sp.under}
      <Eyes mood={mood} color={sp.eye ?? INK} />
      {sp.face}
      {!['河', '天', '鶴', '獏', '해', '범', '용', '두', '까', '삼', '탈', '봉', '백', '산', '록', '변', '업', '억', '강', '개', '연', '목', '마', '생', '종', '적', '처', '단'].includes(glyph) && <Mouth mood={mood} />}
      {sp.front}
    </svg>
  );
}
