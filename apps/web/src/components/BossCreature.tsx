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
  // ───── Gardiens chinois (HSK 1 — Royaumes combattants, bêtes du Classique des monts et des mers) ─────
  // Nian : bête du Nouvel An, rouge, corne unique, crinière dorée, pétards
  年: {
    body: '#C8323F', belly: '#F2C14E', head: '#D9483B', eye: '#FFF3DC',
    top: <><path d="M60 70 Q50 40 74 46 Q78 28 96 38 Q110 24 120 40 Q144 30 140 70Z" fill="#E2B84A" /><path d="M100 44 L96 14 L108 40Z" fill="#F6EBD3" stroke="#B8962A" strokeWidth="2" /></>,
    face: <path d="M86 116 Q100 130 114 116" stroke="#5A1A10" strokeWidth="3" fill="none" />,
    front: <g transform="translate(160 150)"><rect x="-5" y="-14" width="10" height="22" rx="2" fill="#C8323F" stroke="#E2B84A" strokeWidth="2" /><path d="M0 -14 Q4 -22 0 -26" stroke="#5A4A3A" strokeWidth="2" fill="none" /></g>,
  },
  // Taotie : glouton des bronzes, vert-de-gris, motifs en spirale, grandes cornes
  饕: {
    body: '#3E7A6A', belly: '#8FBFA8', head: '#4E8A78', eye: '#F2D94E',
    top: <path d="M62 66 Q40 40 56 22 Q60 44 78 50 M138 66 Q160 40 144 22 Q140 44 122 50" stroke="#2E5A4E" strokeWidth="9" fill="none" strokeLinecap="round" />,
    under: <path d="M62 96 q8 -10 16 0 q-8 10 -16 0Z M122 96 q8 -10 16 0 q-8 10 -16 0Z" fill="none" stroke="#C9A24A" strokeWidth="2.4" />,
    face: <path d="M80 118 H120 M86 118 v8 M100 118 v10 M114 118 v8" stroke="#F6EBD3" strokeWidth="3" strokeLinecap="round" />,
  },
  // Renarde à neuf queues : fourrure blanche et orange, éventail de queues
  尾: {
    body: '#F2F0EA', belly: '#FFFFFF', head: '#F6F3EC', eye: '#C8323F',
    back: <g fill="#E8772E" stroke="#F6EBD3" strokeWidth="3">{[-60, -42, -24, -8, 8, 24, 42, 60, 0].map((a, i) => <ellipse key={i} cx="100" cy="96" rx="12" ry="56" transform={`rotate(${a} 100 150)`} />)}</g>,
    top: <>{ear(58, false, '#F2F0EA', '#E8772E')}{ear(142, true, '#F2F0EA', '#E8772E')}</>,
    under: <path d="M70 92 q6 -6 12 0 M118 92 q6 -6 12 0" stroke="#C8323F" strokeWidth="2.4" fill="none" />,
    face: <path d="M95 106 L105 106 L100 112Z" fill="#5A4A4A" />,
  },
  // Kui : bête à une patte, gris de tempête, corne courte, tambour de peau
  夔: {
    body: '#5A6A7A', belly: '#9AAAB8', head: '#6A7A8A', eye: '#F2D94E',
    top: <path d="M88 50 L94 30 L100 48 L106 30 L112 50" stroke="#3A4A58" strokeWidth="5" fill="none" strokeLinejoin="round" />,
    face: <path d="M84 116 Q100 126 116 116" stroke="#2A3440" strokeWidth="3" fill="none" />,
    front: <g transform="translate(152 150)"><ellipse cx="0" cy="0" rx="16" ry="12" fill="#C9A86A" stroke="#7A5A34" strokeWidth="3" /><path d="M-24 -18 L-12 -6 M-30 -6 L-18 -2" stroke="#F2D94E" strokeWidth="3" strokeLinecap="round" /></g>,
  },
  // Pixiu : lion ailé doré qui avale l'or, pièces trouées
  貔: {
    body: '#D9A63A', belly: '#F6E3A8', head: '#E2B84A', eye: '#5A1A10',
    back: <path d="M50 120 Q10 92 20 64 Q40 84 58 100 M150 120 Q190 92 180 64 Q160 84 142 100" fill="#C9A24A" stroke="#9A7A2A" strokeWidth="3" />,
    top: <path d="M96 46 Q100 26 112 22 Q106 36 106 46" fill="#9A7A2A" />,
    face: <path d="M84 116 Q100 128 116 116" stroke="#7A4A10" strokeWidth="3" fill="none" />,
    front: <g transform="translate(156 160)">{[0, 12].map((d) => <g key={d} transform={`translate(${d - 6} ${-d})`}><circle r="8" fill="#E2B84A" stroke="#9A7A2A" strokeWidth="2" /><rect x="-2.5" y="-2.5" width="5" height="5" fill="#9A7A2A" /></g>)}</g>,
  },
  // Bifang : oiseau de feu à une patte, plumes bleues tachées de rouge, bec blanc, flammes
  毕: {
    body: '#2E6AA8', belly: '#9AC4E8', head: '#3A7ABA', eye: '#FFF3DC',
    back: <path d="M46 130 Q8 110 16 76 Q34 102 56 112 M154 130 Q192 110 184 76 Q166 102 144 112" fill="#2E5A92" />,
    top: <path d="M92 46 Q96 24 104 20 Q104 34 110 44" fill="#C8323F" />,
    under: <path d="M64 136 l6 -4 M80 150 l6 -4 M120 150 l6 -4 M134 136 l6 -4" stroke="#C8323F" strokeWidth="4" strokeLinecap="round" />,
    face: <path d="M92 104 L108 104 L100 120Z" fill="#F6F3EC" stroke="#C9C4BA" strokeWidth="1.5" />,
    front: <g transform="translate(160 156)"><path d="M0 12 Q-12 0 -4 -10 Q-2 0 4 -2 Q2 -14 10 -20 Q12 -4 10 6 Q8 12 0 12Z" fill="#E8772E" /><path d="M2 10 Q-4 2 0 -4 Q4 2 6 0 Q8 6 2 10Z" fill="#F2D94E" /></g>,
  },
  // Xiangliu : serpent vert à neuf têtes dressées
  柳: {
    body: '#4E7A3A', belly: '#B8C98A', head: '#5E8A48', eye: '#E2483B',
    back: <g stroke="#3E6A2E" strokeWidth="9" fill="none" strokeLinecap="round">{[-70, -52, -34, 34, 52, 70].map((a, i) => <path key={i} d="M100 130 Q100 80 100 40" transform={`rotate(${a} 100 130)`} />)}</g>,
    under: <g fill="#5E8A48">{[-70, -52, -34, 34, 52, 70].map((a, i) => <circle key={i} cx="100" cy="36" r="8" transform={`rotate(${a} 100 130)`} />)}</g>,
    face: <path d="M96 116 v10 l-4 5 M104 116 v10 l4 5" stroke="#C8323F" strokeWidth="2.6" fill="none" strokeLinecap="round" />,
  },
  // Zhulong : dragon-chandelle rouge, cornes de cerf, moustaches, bougie allumée
  烛: {
    body: '#B8322E', belly: '#F2C14E', head: '#C8423A', eye: '#F2D94E',
    top: <path d="M78 50 L70 22 L62 28 M70 22 L76 10 M122 50 L130 22 L138 28 M130 22 L124 10" stroke="#E2B84A" strokeWidth="5" fill="none" strokeLinecap="round" />,
    face: <path d="M84 112 Q60 118 46 108 M116 112 Q140 118 154 108" stroke="#F2C14E" strokeWidth="3" fill="none" strokeLinecap="round" />,
    back: <path d="M150 170 Q196 160 188 120 Q180 96 160 104" stroke="#B8322E" strokeWidth="14" fill="none" strokeLinecap="round" />,
    front: <g transform="translate(156 152)"><rect x="-5" y="-6" width="10" height="22" rx="2" fill="#FFF3DC" stroke="#C9A24A" strokeWidth="2" /><path d="M0 -8 Q-6 -16 0 -26 Q6 -16 0 -8Z" fill="#F2A93B" /></g>,
  },
  // ───── Gardiens chinois (HSK 2 — royaume de Wu) ─────
  // Xingtian : géant sans tête, yeux sur la poitrine, bouche au nombril, hache et bouclier
  刑: {
    body: '#7A5A3A', belly: '#C9A86A', head: '#7A5A3A', eye: '#F6EBD3',
    top: <path d="M70 66 H130" stroke="#5A3A24" strokeWidth="6" strokeLinecap="round" />,
    face: <path d="M86 122 Q100 132 114 122 Q100 126 86 122Z" fill="#5A1A10" />,
    front: <g transform="translate(150 150)"><path d="M0 -30 V22" stroke="#5A3A24" strokeWidth="4" /><path d="M0 -30 Q20 -26 18 -10 Q8 -14 0 -12Z" fill="#B9AE98" stroke="#6A6458" strokeWidth="1.5" /></g>,
    back: <ellipse cx="44" cy="140" rx="18" ry="24" fill="#8E1B26" stroke="#E2B84A" strokeWidth="3" />,
  },
  // Jiuying : monstre d'eau et de feu à neuf têtes (bleu et rouge)
  婴: {
    body: '#2E5A92', belly: '#E8772E', head: '#3A6AA8', eye: '#F2D94E',
    back: <g strokeWidth="8" fill="none" strokeLinecap="round">{[-64, -44, -24, 24, 44, 64].map((a, i) => <path key={i} d="M100 130 Q100 90 100 48" stroke={i % 2 ? '#C8323F' : '#2E5A92'} transform={`rotate(${a} 100 130)`} />)}</g>,
    under: <g>{[-64, -44, -24, 24, 44, 64].map((a, i) => <circle key={i} cx="100" cy="44" r="7" fill={i % 2 ? '#C8323F' : '#3A6AA8'} transform={`rotate(${a} 100 130)`} />)}</g>,
    face: <ellipse cx="100" cy="120" rx="8" ry="6" fill="#1A2A40" />,
  },
  // Qiongqi : tigre ailé aux rayures sombres
  穷: {
    body: '#E8962E', belly: '#F6E3C8', head: '#F0A23A', eye: '#2A3A2A',
    back: <path d="M48 116 Q4 84 18 52 Q36 80 60 96 M152 116 Q196 84 182 52 Q164 80 140 96" fill="#6A5A4A" stroke="#3A2A1A" strokeWidth="2" />,
    top: <>{ear(62, false, '#F0A23A', '#3A2A1A')}{ear(138, true, '#F0A23A', '#3A2A1A')}</>,
    under: <path d="M76 66 l6 12 M100 60 v14 M124 66 l-6 12 M64 140 l12 -4 M136 140 l-12 -4" stroke="#3A2A1A" strokeWidth="4" strokeLinecap="round" />,
    face: <path d="M88 118 Q100 126 112 118 M94 118 v6 M106 118 v6" stroke="#3A2A1A" strokeWidth="2.6" fill="none" strokeLinecap="round" />,
  },
  // Kun : poisson géant des mers du Nord, nageoires, écailles
  鲲: {
    body: '#3E6A8A', belly: '#BFD8E8', head: '#4E7A9A', eye: '#F6EBD3',
    back: <path d="M30 150 L6 120 L10 170Z M170 150 L194 120 L190 170Z" fill="#2E5A7A" />,
    top: <path d="M82 54 Q100 18 118 54Z" fill="#2E5A7A" />,
    under: <g fill="none" stroke="#2E5A7A" strokeWidth="2">{[0, 1, 2].map((r) => [0, 1, 2, 3].map((c) => <path key={`${r}${c}`} d={`M${66 + c * 18 + (r % 2) * 9} ${140 + r * 10} q9 8 18 0`} />))}</g>,
    face: <path d="M86 118 Q100 124 114 118" stroke="#1A3A52" strokeWidth="3" fill="none" />,
  },
  // Hundun : chaos sans visage, sac jaune à six pattes et quatre ailes rouges
  混: {
    body: '#E2B84A', belly: '#F2D58A', head: '#E2B84A', eye: '#E2B84A',
    back: <path d="M50 110 Q14 90 22 60 Q40 88 58 98 M150 110 Q186 90 178 60 Q160 88 142 98" fill="#C8323F" />,
    face: <path d="M70 100 q10 -8 20 0 q10 8 20 0 q10 -8 20 0" stroke="#C9A24A" strokeWidth="2" fill="none" />,
    front: <g fill="#C9A24A">{[64, 84, 116, 136].map((x) => <rect key={x} x={x - 4} y="182" width="8" height="10" rx="3" />)}</g>,
  },
  // Baize : bête blanche savante, cornes, barbiche, rouleau
  泽: {
    body: '#F2F0EA', belly: '#FFFFFF', head: '#F6F3EC', eye: '#2F7A6E',
    top: <path d="M80 50 Q70 26 80 14 M120 50 Q130 26 120 14" stroke="#C9A24A" strokeWidth="6" fill="none" strokeLinecap="round" />,
    under: <path d="M66 140 q6 -6 12 0 M122 140 q6 -6 12 0 M94 72 q6 -6 12 0" stroke="#2F7A6E" strokeWidth="2.4" fill="none" />,
    face: <path d="M96 124 Q100 140 104 124" fill="#E8E2D4" stroke="#C9C4BA" strokeWidth="1.5" />,
    front: <g transform="translate(156 156)"><rect x="-12" y="-6" width="24" height="12" fill="#D9C28A" stroke="#9A8452" strokeWidth="1.5" /><path d="M-12 0 H12" stroke="#C8323F" strokeWidth="1.5" /></g>,
  },
  // Hanba : démone de la sécheresse en robe verte, soleil brûlant
  魃: {
    body: '#3E7A4A', belly: '#8FBF8A', head: '#C9B08A', eye: '#C8323F',
    top: <path d="M64 70 Q60 40 80 48 Q84 30 100 40 Q116 30 120 48 Q140 40 136 70" fill="#2A2A2A" />,
    face: <path d="M88 118 Q100 112 112 118" stroke="#5A3A24" strokeWidth="3" fill="none" />,
    front: <g transform="translate(158 54)"><circle r="12" fill="#F2A93B" />{[0, 45, 90, 135, 180, 225, 270, 315].map((a) => <path key={a} d="M0 -16 V-22" stroke="#E8772E" strokeWidth="3" transform={`rotate(${a})`} />)}</g>,
  },
  // Chiyou : dieu de la guerre, front de bronze, cornes, huit bras
  蚩: {
    body: '#6A2A2A', belly: '#A86A4A', head: '#7A3A2A', eye: '#F2D94E',
    back: <g stroke="#6A2A2A" strokeWidth="10" strokeLinecap="round">{[-50, -30, 30, 50].map((a, i) => <path key={i} d="M100 120 L100 46" transform={`rotate(${a} 100 120)`} />)}</g>,
    top: <><rect x="70" y="56" width="60" height="12" rx="3" fill="#B8962A" /><path d="M74 58 Q60 30 70 18 M126 58 Q140 30 130 18" stroke="#E2D9C4" strokeWidth="7" fill="none" strokeLinecap="round" /></>,
    face: <path d="M84 116 L92 124 L100 116 L108 124 L116 116" stroke="#F6EBD3" strokeWidth="3" fill="none" strokeLinejoin="round" />,
    front: <g transform="translate(154 150)"><path d="M0 -36 V20" stroke="#5A3A24" strokeWidth="4" /><path d="M0 -36 L-10 -22 H10Z" fill="#B9AE98" /></g>,
  },
  // ───── Gardiens chinois (HSK 3 — les Cent Écoles au royaume de Qi) ─────
  // Taowu : bête têtue à visage d'homme, longs poils gris, défenses de sanglier, queue immense
  梼: {
    body: '#6E6A62', belly: '#A39C8E', head: '#C9A27A', eye: '#2A2A2A',
    back: <path d="M40 160 Q0 150 10 110 Q20 140 46 140" fill="#5A564E" />,
    top: <path d="M62 74 Q56 40 80 46 Q86 28 100 38 Q114 28 120 46 Q144 40 138 74" fill="#8A847A" />,
    face: <><path d="M88 116 Q100 122 112 116" stroke="#4A2A1A" strokeWidth="3" fill="none" /><path d="M86 118 Q80 104 84 96 M114 118 Q120 104 116 96" stroke="#F6EBD3" strokeWidth="4" fill="none" strokeLinecap="round" /></>,
  },
  // Jingwei : petit oiseau à tête tachetée, bec blanc, pattes rouges, caillou dans le bec
  精: {
    body: '#3A3A44', belly: '#D9D4C8', head: '#4A4A56', eye: '#F6EBD3',
    back: <path d="M48 120 Q10 100 20 70 Q36 96 58 104 M152 120 Q190 100 180 70 Q164 96 142 104" fill="#2A2A34" />,
    under: <g fill="#E2D9C4">{[[78, 70], [96, 62], [116, 68], [88, 80], [110, 82]].map(([x, y]) => <circle key={`${x}${y}`} cx={x} cy={y} r="3.4" />)}</g>,
    face: <><path d="M92 114 L100 132 L108 114Z" fill="#F6F3EC" stroke="#B9AE98" strokeWidth="1" /><circle cx="100" cy="134" r="5" fill="#8A847A" /></>,
    front: <path d="M80 184 v10 M120 184 v10" stroke="#C8323F" strokeWidth="4" strokeLinecap="round" />,
  },
  // Zheng : léopard rouge à cinq queues et à une corne
  狰: {
    body: '#C8423A', belly: '#F2C8A0', head: '#D9524A', eye: '#F2D94E',
    back: <g stroke="#A8322A" strokeWidth="6" fill="none" strokeLinecap="round">{[-40, -20, 0, 20, 40].map((a) => <path key={a} d="M150 160 Q178 140 186 112" transform={`rotate(${a} 150 160)`} />)}</g>,
    top: <><path d="M100 46 L94 14 L106 14Z" fill="#E2D9C4" stroke="#9A8452" strokeWidth="1.5" />{ear(64, false, '#D9524A', '#3A1A1A')}{ear(136, true, '#D9524A', '#3A1A1A')}</>,
    under: <g fill="#7A1A14">{[[70, 140], [90, 150], [116, 146], [134, 136], [80, 70], [122, 72]].map(([x, y]) => <circle key={`${x}${y}`} cx={x} cy={y} r="4" />)}</g>,
    face: <path d="M88 118 Q100 126 112 118 M94 118 v5 M106 118 v5" stroke="#3A1A1A" strokeWidth="2.4" fill="none" strokeLinecap="round" />,
  },
  // Kuafu : géant qui poursuit le soleil, serpents jaunes aux oreilles, bâton
  夸: {
    body: '#8A5A3A', belly: '#D9B08A', head: '#C9925A', eye: '#2A1A10',
    top: <><path d="M58 70 Q40 56 52 40 Q60 56 66 60 M142 70 Q160 56 148 40 Q140 56 134 60" stroke="#E2B84A" strokeWidth="5" fill="none" strokeLinecap="round" /><path d="M66 64 Q100 36 134 64" fill="#3A2A1A" /></>,
    face: <path d="M86 116 Q100 128 114 116" stroke="#5A1A10" strokeWidth="3" fill="none" />,
    front: <g transform="translate(158 150)"><path d="M0 -46 V30" stroke="#5A3A24" strokeWidth="4" /><circle cy="-52" r="9" fill="#F2A93B" /></g>,
  },
  // Xiezhi : licorne noire des juges, une corne, crinière
  獬: {
    body: '#2A2A30', belly: '#5A5A64', head: '#34343C', eye: '#F2D94E',
    top: <><path d="M100 48 Q96 20 104 6 Q106 26 108 48Z" fill="#E2B84A" stroke="#9A8452" strokeWidth="1.5" /><path d="M62 72 Q56 50 72 50 Q76 38 88 46" fill="#1A1A20" /></>,
    under: <path d="M66 140 q8 -8 16 0 M118 140 q8 -8 16 0" stroke="#E2B84A" strokeWidth="2.4" fill="none" />,
    face: <path d="M90 118 Q100 124 110 118" stroke="#E2B84A" strokeWidth="2.4" fill="none" />,
  },
  // Hou : bête au poil de flamme qui dévore les dragons
  犼: {
    body: '#D9632E', belly: '#F2B84A', head: '#E2733A', eye: '#2A1A10',
    back: <path d="M44 120 Q20 96 32 70 Q40 96 56 104 Q36 84 46 60 Q56 88 66 96" fill="#C8323F" />,
    top: <><path d="M62 70 Q66 40 80 50 Q88 26 100 42 Q112 26 120 50 Q134 40 138 70" fill="#C8323F" />{ear(70, false, '#E2733A', '#7A2A14')}{ear(130, true, '#E2733A', '#7A2A14')}</>,
    face: <path d="M84 116 L92 124 L100 116 L108 124 L116 116" stroke="#3A1A10" strokeWidth="3" fill="none" strokeLinejoin="round" />,
  },
  // Yinglong : dragon ailé des pluies, ailes, cornes, nuages
  应: {
    body: '#2F7A6E', belly: '#E2D9A4', head: '#3A8A7C', eye: '#F2D94E',
    back: <path d="M50 116 Q6 78 24 40 Q40 76 60 90 Q36 66 48 34 Q60 70 70 82 M150 116 Q194 78 176 40 Q160 76 140 90 Q164 66 152 34 Q140 70 130 82" fill="#5FA89A" stroke="#1F5A50" strokeWidth="2" />,
    top: <path d="M80 52 Q70 30 80 18 Q82 34 88 46 M120 52 Q130 30 120 18 Q118 34 112 46" stroke="#E2B84A" strokeWidth="5" fill="none" strokeLinecap="round" />,
    face: <><path d="M88 118 Q100 126 112 118" stroke="#1F4A40" strokeWidth="3" fill="none" /><path d="M80 114 Q64 112 58 120 M120 114 Q136 112 142 120" stroke="#1F4A40" strokeWidth="2" fill="none" /></>,
  },
  // Gonggong : dieu des eaux furieux, cheveux rouges, corps de serpent, vagues
  共: {
    body: '#2E5A92', belly: '#9CC4E4', head: '#4A7AA8', eye: '#F2D94E',
    top: <path d="M60 72 Q52 36 72 42 Q76 20 92 34 Q100 14 108 34 Q124 20 128 42 Q148 36 140 72" fill="#C8323F" />,
    face: <path d="M86 120 Q100 112 114 120" stroke="#1A2A40" strokeWidth="3" fill="none" />,
    front: <path d="M20 190 q12 -10 24 0 t24 0 t24 0 t24 0 t24 0 t24 0 t24 0" stroke="#9CC4E4" strokeWidth="4" fill="none" />,
  },
  // ───── Gardiens chinois (HSK 4 — l'empire de Qin) ─────
  // Fei : bœuf blanc pestilentiel, queue de serpent
  蜚: {
    body: '#E8E4DA', belly: '#FFFFFF', head: '#F2EEE4', eye: '#2A2A2A',
    back: <path d="M150 160 Q190 150 182 120 Q176 104 188 96" stroke="#6E8A4A" strokeWidth="7" fill="none" strokeLinecap="round" />,
    top: <path d="M70 58 Q54 40 60 26 Q70 42 82 50 M130 58 Q146 40 140 26 Q130 42 118 50" fill="#C9B08A" stroke="#9A8452" strokeWidth="2" />,
    under: <ellipse cx="100" cy="86" rx="16" ry="14" fill="#F6EBD3" stroke="#B9AE98" strokeWidth="2" />,
    face: <ellipse cx="100" cy="122" rx="14" ry="8" fill="#E2B0A0" />,
  },
  // Zhuyan : singe à tête blanche et aux pieds rouges
  朱: {
    body: '#8A6A4A', belly: '#C9A27A', head: '#F2EEE4', eye: '#2A1A10',
    back: <path d="M150 150 Q190 120 170 80" stroke="#8A6A4A" strokeWidth="8" fill="none" strokeLinecap="round" />,
    top: <><circle cx="56" cy="92" r="12" fill="#F2EEE4" /><circle cx="144" cy="92" r="12" fill="#F2EEE4" /></>,
    face: <path d="M88 118 Q100 112 112 118" stroke="#5A1A10" strokeWidth="3" fill="none" />,
    front: <g fill="#C8323F">{[84, 116].map((x) => <ellipse key={x} cx={x} cy="190" rx="12" ry="6" />)}</g>,
  },
  // Xiqu : bête cornue à corps de bœuf, cuir épais
  犀: {
    body: '#5A6A7A', belly: '#8A9AAA', head: '#6A7A8A', eye: '#F2D94E',
    top: <path d="M100 50 L92 22 Q100 14 108 22Z M80 56 L74 40 L88 50Z" fill="#E2D9C4" stroke="#9A8452" strokeWidth="1.5" />,
    under: <path d="M62 136 q10 -4 18 0 M120 136 q10 -4 18 0 M66 156 q14 -4 26 0" stroke="#3A4A5A" strokeWidth="3" fill="none" />,
    face: <path d="M86 120 Q100 128 114 120" stroke="#2A3A4A" strokeWidth="3" fill="none" />,
  },
  // Feiyi : serpent à six pattes et quatre ailes, soleil de sécheresse
  肥: {
    body: '#B8962A', belly: '#F2D58A', head: '#C9A23A', eye: '#C8323F',
    back: <path d="M52 108 Q12 88 22 58 Q38 84 60 96 M52 126 Q14 120 18 96 M148 108 Q188 88 178 58 Q162 84 140 96 M148 126 Q186 120 182 96" stroke="#8A6A1A" strokeWidth="3" fill="#E2C46A" />,
    face: <path d="M96 120 l4 10 l4 -10" stroke="#C8323F" strokeWidth="2.5" fill="none" />,
    front: <g fill="#8A6A1A">{[60, 80, 120, 140].map((x) => <rect key={x} x={x - 4} y="180" width="8" height="12" rx="3" />)}</g>,
  },
  // Xuangui : tortue noire à tête d'oiseau et à queue de serpent
  旋: {
    body: '#2E3A30', belly: '#6E7A5A', head: '#3E4A40', eye: '#F2D94E',
    back: <ellipse cx="100" cy="150" rx="70" ry="42" fill="#4E5A3A" stroke="#2A3220" strokeWidth="3" />,
    under: <path d="M60 146 L80 132 L100 146 L120 132 L140 146" stroke="#2A3220" strokeWidth="2.5" fill="none" />,
    face: <path d="M92 116 L100 132 L108 116Z" fill="#E2B84A" stroke="#9A8452" strokeWidth="1" />,
  },
  // Zouyu : grand tigre blanc à rayures sombres, queue immense
  驺: {
    body: '#F2EEE4', belly: '#FFFFFF', head: '#F6F3EC', eye: '#2F7A6E',
    back: <path d="M150 170 Q200 160 196 110 Q194 70 170 60" stroke="#F2EEE4" strokeWidth="9" fill="none" strokeLinecap="round" />,
    top: <>{ear(66, false, '#F6F3EC', '#2A2A2A')}{ear(134, true, '#F6F3EC', '#2A2A2A')}</>,
    under: <path d="M76 66 l6 12 M100 60 v14 M124 66 l-6 12 M62 140 l12 -4 M138 140 l-12 -4 M70 160 l12 -2 M130 160 l-12 -2" stroke="#2A2A2A" strokeWidth="4" strokeLinecap="round" />,
    face: <path d="M88 118 Q100 126 112 118 M94 118 v6 M106 118 v6" stroke="#2A2A2A" strokeWidth="2.4" fill="none" strokeLinecap="round" />,
  },
  // Huashe : serpent ailé à visage humain, appelle les eaux
  化: {
    body: '#4E7A9A', belly: '#BFD8E8', head: '#D9B08A', eye: '#2A1A10',
    back: <path d="M50 116 Q8 84 22 50 Q40 80 62 94 M150 116 Q192 84 178 50 Q160 80 138 94" fill="#9CC4E4" stroke="#2E5A7A" strokeWidth="2" />,
    top: <path d="M64 74 Q60 46 82 50 Q90 34 100 44 Q110 34 118 50 Q140 46 136 74" fill="#2A2A2A" />,
    face: <path d="M90 120 Q100 116 110 120" stroke="#5A3A24" strokeWidth="2.5" fill="none" />,
    front: <path d="M20 190 q12 -10 24 0 t24 0 t24 0 t24 0 t24 0 t24 0 t24 0" stroke="#9CC4E4" strokeWidth="4" fill="none" />,
  },
  // Bibi : renard ailé couleur de sable
  獙: {
    body: '#D9A25A', belly: '#F6E3C8', head: '#E2B06A', eye: '#2A1A10',
    back: <path d="M48 116 Q8 92 18 56 Q36 86 60 98 M152 116 Q192 92 182 56 Q164 86 140 98" fill="#F2D58A" stroke="#9A7A3A" strokeWidth="2" />,
    top: <>{ear(66, false, '#E2B06A', '#7A4A1A')}{ear(134, true, '#E2B06A', '#7A4A1A')}</>,
    under: <path d="M150 170 Q190 160 186 128" stroke="#E2B06A" strokeWidth="12" fill="none" strokeLinecap="round" />,
    face: <path d="M92 118 Q100 124 108 118" stroke="#4A2A1A" strokeWidth="2.5" fill="none" />,
  },
  // ───── Gardiens chinois (HSK 5 — les mers de l'Est) ─────
  // Yuqiang : dieu des vents marins, corps d'oiseau, serpents verts aux oreilles
  禺: {
    body: '#2A2A3A', belly: '#6A6A8A', head: '#C9A27A', eye: '#2A1A10',
    back: <path d="M50 116 Q8 84 22 46 Q40 80 62 94 M150 116 Q192 84 178 46 Q160 80 138 94" fill="#3A3A4E" stroke="#1A1A28" strokeWidth="2" />,
    top: <path d="M58 92 Q40 80 48 62 Q56 74 66 78 M142 92 Q160 80 152 62 Q144 74 134 78" stroke="#3E8A4A" strokeWidth="5" fill="none" strokeLinecap="round" />,
    face: <path d="M90 118 Q100 124 110 118" stroke="#4A2A1A" strokeWidth="2.5" fill="none" />,
    front: <path d="M30 60 q14 -8 28 0 M142 50 q14 -8 28 0" stroke="#9CC4E4" strokeWidth="3" fill="none" strokeLinecap="round" />,
  },
  // Shen : palourde géante qui souffle des mirages
  蜃: {
    body: '#C9B8D8', belly: '#F2E8F6', head: '#D8C8E4', eye: '#3A2A4A',
    back: <path d="M24 150 Q100 70 176 150 Q100 190 24 150Z" fill="#B8A2C9" stroke="#7A5A8A" strokeWidth="3" />,
    under: <path d="M40 150 Q100 100 160 150" stroke="#7A5A8A" strokeWidth="2" fill="none" />,
    face: <path d="M92 118 Q100 124 108 118" stroke="#3A2A4A" strokeWidth="2.5" fill="none" />,
    front: <g fill="#F2E8F6" opacity="0.8"><rect x="146" y="28" width="10" height="20" /><path d="M140 30 L151 18 L162 30Z" /><rect x="164" y="36" width="8" height="12" /></g>,
  },
  // Jiaoren : gens de la mer à queue de poisson, perles
  鲛: {
    body: '#3E8A8A', belly: '#BFE4E0', head: '#E8C8A8', eye: '#2A1A10',
    back: <path d="M150 170 Q190 160 186 130 L196 120 L176 128 Q172 150 150 156" fill="#2F7A6E" />,
    top: <path d="M62 80 Q58 44 84 48 Q94 30 106 40 Q126 34 132 56 Q146 66 138 92" fill="#2A4A5A" />,
    face: <path d="M92 118 Q100 124 108 118" stroke="#8A3A2A" strokeWidth="2.5" fill="none" />,
    front: <g fill="#F6F3EC" stroke="#C9C4BA" strokeWidth="1">{[[64, 186], [76, 192], [124, 190]].map(([x, y]) => <circle key={x} cx={x} cy={y} r="4" />)}</g>,
  },
  // Ao : tortue colossale portant des îles sur son dos
  鳌: {
    body: '#4E6A4A', belly: '#9AB08A', head: '#5E7A5A', eye: '#F2D94E',
    back: <><ellipse cx="100" cy="150" rx="76" ry="44" fill="#6E5A3A" stroke="#3A2A1A" strokeWidth="3" /><path d="M56 112 L68 92 L80 112Z M118 108 L132 84 L146 108Z" fill="#5E8C3A" /></>,
    under: <path d="M56 150 L76 136 L100 150 L124 136 L144 150" stroke="#3A2A1A" strokeWidth="2.5" fill="none" />,
    face: <path d="M88 118 Q100 126 112 118" stroke="#1F3A1A" strokeWidth="3" fill="none" />,
  },
  // Jiaolong : dragon sans cornes des crues, écailles, éclairs
  蛟: {
    body: '#2E5A7A', belly: '#9CC4E4', head: '#3E6A8A', eye: '#F2D94E',
    back: <path d="M150 160 Q194 140 184 100 Q176 72 196 56" stroke="#2E5A7A" strokeWidth="12" fill="none" strokeLinecap="round" />,
    under: <g fill="none" stroke="#1E4A6A" strokeWidth="2">{[0, 1].map((r) => [0, 1, 2, 3].map((c) => <path key={`${r}${c}`} d={`M${66 + c * 18 + (r % 2) * 9} ${140 + r * 12} q9 8 18 0`} />))}</g>,
    face: <><path d="M86 118 Q100 126 114 118" stroke="#1A2A40" strokeWidth="3" fill="none" /><path d="M80 112 Q64 108 56 116 M120 112 Q136 108 144 116" stroke="#1A2A40" strokeWidth="2" fill="none" /></>,
    front: <path d="M30 40 L40 58 L34 58 L44 78" stroke="#F2D94E" strokeWidth="3" fill="none" strokeLinejoin="round" />,
  },
  // Heluo : poisson à une tête et dix corps
  何: {
    body: '#6A8AAA', belly: '#C8D8E8', head: '#7A9ABA', eye: '#2A1A10',
    back: <g fill="#5A7A9A" stroke="#3A5A7A" strokeWidth="2">{[-50, -30, -10, 10, 30, 50].map((a) => <path key={a} d="M100 150 L100 92 L92 80 L108 80 L100 92Z" transform={`rotate(${a + 180} 100 150)`} />)}</g>,
    face: <path d="M90 120 Q100 116 110 120" stroke="#1A2A40" strokeWidth="2.5" fill="none" />,
  },
  // Chiru : poisson rouge à visage humain
  鱬: {
    body: '#D9483B', belly: '#F2B8A0', head: '#E8C8A8', eye: '#2A1A10',
    back: <path d="M150 160 Q186 150 190 120 L200 140 L190 160 L200 180 L186 170 Q170 172 150 166" fill="#C8323F" />,
    top: <path d="M64 80 Q60 50 84 54 Q100 40 116 54 Q140 50 136 80" fill="#3A2A1A" />,
    under: <path d="M62 140 q8 -6 16 0 M122 140 q8 -6 16 0" stroke="#8E1B26" strokeWidth="2.5" fill="none" />,
    face: <path d="M88 118 Q100 112 112 118" stroke="#5A1A10" strokeWidth="2.5" fill="none" />,
  },
  // Ranyi : poisson à tête de serpent et à six pieds
  冉: {
    body: '#4A3A5A', belly: '#9A8AAA', head: '#5A4A6A', eye: '#F2D94E',
    back: <path d="M150 160 Q186 150 190 120 L200 140 L190 160 L200 180 L186 170 Q170 172 150 166" fill="#3A2A4A" />,
    top: <path d="M78 52 Q100 36 122 52" stroke="#2A1A3A" strokeWidth="6" fill="none" strokeLinecap="round" />,
    face: <path d="M96 120 l4 10 l4 -10" stroke="#C8323F" strokeWidth="2.5" fill="none" />,
    front: <g fill="#3A2A4A">{[56, 74, 92, 108, 126, 144].map((x) => <rect key={x} x={x - 3} y="182" width="6" height="12" rx="2" />)}</g>,
  },
  // ───── Gardiens chinois (HSK 6 — la route de la soie) ─────
  // Paoxiao : corps de mouton, visage d'homme, yeux sous les aisselles, glouton
  狍: {
    body: '#E8E0CC', belly: '#FFFFFF', head: '#E8C8A8', eye: '#2A1A10',
    back: <g fill="#F6F0E0" stroke="#C9BFA6" strokeWidth="2">{[[40, 120], [58, 100], [142, 100], [160, 120], [100, 92]].map(([x, y]) => <circle key={`${x}${y}`} cx={x} cy={y} r="20" />)}</g>,
    top: <path d="M64 70 Q44 60 50 40 Q60 54 74 58 M136 70 Q156 60 150 40 Q140 54 126 58" stroke="#8A7A5A" strokeWidth="7" fill="none" strokeLinecap="round" />,
    face: <path d="M84 114 Q100 132 116 114 Z" fill="#8E1B26" />,
    front: <g fill="#F2D94E" stroke="#2A1A10" strokeWidth="1.5"><circle cx="40" cy="150" r="5" /><circle cx="160" cy="150" r="5" /></g>,
  },
  // Aoyin : bœuf blanc à quatre cornes, poil tombant comme un manteau de paille
  獓: {
    body: '#F2EEE6', belly: '#FFFFFF', head: '#F6F3EC', eye: '#2A1A10',
    back: <path d="M40 120 L30 186 M56 116 L50 190 M144 116 L150 190 M160 120 L170 186" stroke="#C9B88A" strokeWidth="6" strokeLinecap="round" />,
    top: <path d="M66 64 Q44 44 48 24 M80 54 Q70 34 78 18 M120 54 Q130 34 122 18 M134 64 Q156 44 152 24" stroke="#8A7A5A" strokeWidth="7" fill="none" strokeLinecap="round" />,
    face: <path d="M88 118 Q100 126 112 118" stroke="#4A2A1A" strokeWidth="3" fill="none" />,
  },
  // Bo : cheval blanc à queue noire, une corne, griffes de tigre
  驳: {
    body: '#F6F3EC', belly: '#FFFFFF', head: '#F2EEE6', eye: '#2A1A10',
    back: <path d="M150 160 Q190 150 192 110 Q196 140 180 170" fill="#1F2433" />,
    top: <><path d="M100 46 L94 8 L108 44Z" fill="#C9A24A" stroke="#8A6A2A" strokeWidth="2" /><path d="M70 60 Q80 40 100 46 Q120 40 130 60" stroke="#1F2433" strokeWidth="8" fill="none" /></>,
    face: <path d="M90 118 Q100 124 110 118" stroke="#4A2A1A" strokeWidth="2.5" fill="none" />,
    front: <g stroke="#1F2433" strokeWidth="2.5" fill="none">{[56, 140].map((x) => <path key={x} d={`M${x} 186 l-5 8 M${x + 6} 186 l0 9 M${x + 12} 186 l5 8`} />)}</g>,
  },
  // Toulou : mouton à quatre cornes tapi sous les dunes
  蝼: {
    body: '#D9B07A', belly: '#F2DEB8', head: '#E2BC88', eye: '#2A1A10',
    top: <path d="M66 64 Q50 40 62 30 Q66 46 78 50 M82 56 Q78 36 88 28 M118 56 Q122 36 112 28 M134 64 Q150 40 138 30 Q134 46 122 50" stroke="#6E5A3A" strokeWidth="6" fill="none" strokeLinecap="round" />,
    face: <path d="M88 116 Q100 112 112 116" stroke="#5A3A24" strokeWidth="2.5" fill="none" />,
    front: <path d="M10 196 Q50 170 100 192 Q150 172 190 196Z" fill="#E8C88A" />,
  },
  // Jiao : chien tacheté comme un léopard, cornes de bœuf
  狡: {
    body: '#E2A24A', belly: '#F6E0B8', head: '#E8AE5A', eye: '#2A1A10',
    back: <path d="M150 160 Q188 150 186 118" stroke="#E2A24A" strokeWidth="10" fill="none" strokeLinecap="round" />,
    top: <><path d="M62 64 Q42 52 44 34 Q56 48 72 52 M138 64 Q158 52 156 34 Q144 48 128 52" stroke="#6E5A3A" strokeWidth="7" fill="none" strokeLinecap="round" />{ear(70, false, '#E8AE5A', '#7A4A1A')}{ear(130, true, '#E8AE5A', '#7A4A1A')}</>,
    under: <g fill="#5A3A1A">{[[60, 150], [80, 168], [120, 166], [140, 150], [100, 156]].map(([x, y]) => <circle key={`${x}${y}`} cx={x} cy={y} r="4.5" />)}</g>,
    face: <path d="M92 118 Q100 124 108 118" stroke="#4A2A1A" strokeWidth="2.5" fill="none" />,
  },
  // Jufu : singe aux bras tigrés qui lance des pierres
  举: {
    body: '#8A6A4A', belly: '#D8C0A0', head: '#C9A27A', eye: '#2A1A10',
    back: <path d="M150 160 Q194 150 186 106 Q180 86 194 76" stroke="#8A6A4A" strokeWidth="8" fill="none" strokeLinecap="round" />,
    top: <>{ear(66, false, '#8A6A4A', '#D8C0A0')}{ear(134, true, '#8A6A4A', '#D8C0A0')}</>,
    under: <path d="M30 150 l10 -6 M34 160 l10 -6 M156 144 l10 6 M152 154 l10 6" stroke="#2A1A10" strokeWidth="3" />,
    face: <path d="M88 120 Q100 112 112 120" stroke="#4A2A1A" strokeWidth="2.5" fill="none" />,
    front: <ellipse cx="172" cy="40" rx="12" ry="10" fill="#8A8A8A" stroke="#4A4A4A" strokeWidth="2" />,
  },
  // Luwu : corps de tigre, neuf queues, visage d'homme, gardien de Kunlun
  陆: {
    body: '#E8A23A', belly: '#F6E0B8', head: '#E8C8A8', eye: '#2A1A10',
    back: <g stroke="#E8A23A" strokeWidth="7" fill="none" strokeLinecap="round">{[-56, -42, -28, -14, 0, 14, 28, 42, 56].map((a) => <path key={a} d="M100 150 Q104 110 100 76" transform={`rotate(${a} 100 150)`} />)}</g>,
    top: <path d="M64 80 Q60 48 84 52 Q100 38 116 52 Q140 48 136 80" fill="#3A2A1A" />,
    under: <path d="M52 140 l14 4 M50 156 l14 2 M148 140 l-14 4 M150 156 l-14 2" stroke="#2A1A10" strokeWidth="3.5" strokeLinecap="round" />,
    face: <path d="M90 118 Q100 124 110 118" stroke="#5A3A24" strokeWidth="2.5" fill="none" />,
  },
  // Eshou : lièvre à visage d'homme, menteur
  讹: {
    body: '#C9C0B0', belly: '#F2EEE6', head: '#E8C8A8', eye: '#2A1A10',
    top: <path d="M78 56 Q66 6 82 4 Q92 20 90 52 M122 56 Q134 6 118 4 Q108 20 110 52" fill="#C9C0B0" stroke="#8A8070" strokeWidth="2" />,
    face: <path d="M88 116 Q96 124 104 116 Q110 112 114 118" stroke="#4A2A1A" strokeWidth="2.5" fill="none" />,
    front: <g transform="translate(156 140)"><rect x="-14" y="-18" width="28" height="36" rx="3" fill="#F6EBD3" stroke="#8A6A3A" strokeWidth="2" /><path d="M-8 -8 H8 M-8 0 H8 M-8 8 H4" stroke="#8A6A3A" strokeWidth="2" /></g>,
  },
  // ───── Gardiens espagnols (DELE A1 — les chemins de la Manche) ─────
  // Duende : petit lutin des maisons, bonnet rouge pointu, clé dérobée
  Á: {
    body: '#6E8A4A', belly: '#C8D8A8', head: '#E8C8A8', eye: '#2A1A10',
    top: <path d="M58 72 Q70 20 120 10 Q108 40 142 72Z" fill="#C8323F" stroke="#8E1B26" strokeWidth="2" />,
    face: <path d="M90 116 Q100 124 110 116" stroke="#5A3A24" strokeWidth="2.5" fill="none" />,
    front: <g transform="translate(160 150) rotate(30)" fill="#E2B84A" stroke="#9A7A2A" strokeWidth="1.5"><circle cx="0" cy="-12" r="7" fill="none" strokeWidth="4" stroke="#E2B84A" /><rect x="-2" y="-5" width="4" height="22" /><rect x="2" y="10" width="7" height="3" /></g>,
  },
  // Trasgu : lutin asturien noiraud, petites cornes, bonnet rouge, une main percée
  É: {
    body: '#4A3A3A', belly: '#8A7A6A', head: '#6A5048', eye: '#F2D94E',
    top: <><path d="M74 58 Q66 40 76 32 M126 58 Q134 40 124 32" stroke="#E8DCC0" strokeWidth="5" fill="none" strokeLinecap="round" /><path d="M66 60 Q100 24 134 60Z" fill="#C8323F" /></>,
    face: <path d="M90 118 Q100 112 110 118" stroke="#F6E7C8" strokeWidth="2.5" fill="none" />,
    front: <circle cx="146" cy="150" r="4" fill="#1F2433" />,
  },
  // Nuberu : vieux maître des nuages en peaux de chèvre, grand chapeau, grêle
  Í: {
    body: '#8A7A5A', belly: '#C9B88A', head: '#D8C0A0', eye: '#2A1A10',
    top: <><ellipse cx="100" cy="52" rx="58" ry="10" fill="#3A3A4A" /><path d="M72 52 Q74 26 100 24 Q126 26 128 52Z" fill="#3A3A4A" /></>,
    under: <path d="M70 108 Q100 150 130 108" fill="#E8E8E8" />,
    front: <g fill="#B8C4D8"><ellipse cx="40" cy="36" rx="22" ry="12" /><ellipse cx="58" cy="30" rx="16" ry="11" /><circle cx="36" cy="56" r="3" fill="#FFFFFF" /><circle cx="48" cy="62" r="3" fill="#FFFFFF" /><circle cx="60" cy="54" r="3" fill="#FFFFFF" /></g>,
  },
  // Ojáncanu : géant cantabre à un seul œil et barbe rousse
  Ó: {
    body: '#A86A4A', belly: '#E2B48A', head: '#D9A07A', eye: '#2A1A10',
    top: <path d="M62 78 Q58 46 82 48 Q100 34 118 48 Q142 46 138 78" fill="#C8562E" />,
    under: <path d="M62 104 Q100 168 138 104 Q120 124 100 124 Q80 124 62 104Z" fill="#C8562E" />,
    face: <><rect x="66" y="72" width="68" height="26" rx="12" fill="#D9A07A" /><circle cx="100" cy="84" r="13" fill="#FFFFFF" stroke="#5A3A24" strokeWidth="2" /><circle cx="100" cy="85" r="6" fill="#2A1A10" /></>,
  },
  // Busgosu : gardien des bois mi-homme mi-bouc, cornes, feuillage
  Ü: {
    body: '#6E5A3A', belly: '#B8A07A', head: '#C9A27A', eye: '#2A1A10',
    top: <path d="M70 60 Q50 40 58 18 Q66 36 80 46 M130 60 Q150 40 142 18 Q134 36 120 46" stroke="#E8DCC0" strokeWidth="7" fill="none" strokeLinecap="round" />,
    under: <path d="M90 112 Q100 140 110 112" fill="#8A7A5A" />,
    front: <g fill="#3E7A3A">{[[30, 120], [40, 104], [170, 116], [160, 100]].map(([x, y]) => <ellipse key={`${x}${y}`} cx={x} cy={y} rx="9" ry="5" transform={`rotate(-30 ${x} ${y})`} />)}</g>,
  },
  // Cuélebre : serpent ailé des Asturies couché sur son trésor
  Ú: {
    body: '#3E7A4A', belly: '#BFE0A0', head: '#4E8A5A', eye: '#F2D94E',
    back: <path d="M50 116 Q6 86 18 46 Q38 80 62 94 M150 116 Q194 86 182 46 Q162 80 138 94" fill="#2E6A3A" stroke="#1E4A2A" strokeWidth="2" />,
    under: <g fill="none" stroke="#2E6A3A" strokeWidth="2">{[0, 1, 2].map((c) => <path key={c} d={`M${70 + c * 20} 150 q10 8 20 0`} />)}</g>,
    face: <path d="M88 116 Q100 124 112 116" stroke="#1E3A20" strokeWidth="3" fill="none" />,
    front: <g fill="#E2B84A" stroke="#9A7A2A" strokeWidth="1">{[[52, 190], [64, 194], [140, 192], [152, 188]].map(([x, y]) => <circle key={x} cx={x} cy={y} r="5" />)}</g>,
  },
  // Basajaun : géant velu des forêts basques, longue chevelure, bâton de berger
  '¿': {
    body: '#6A4A2A', belly: '#9A7A5A', head: '#C9A27A', eye: '#2A1A10',
    back: <path d="M44 70 Q30 130 52 170 L148 170 Q170 130 156 70 Q100 30 44 70Z" fill="#5A3A1A" />,
    top: <path d="M58 86 Q56 40 100 36 Q144 40 142 86 Q130 60 100 58 Q70 60 58 86Z" fill="#5A3A1A" />,
    face: <path d="M90 118 Q100 124 110 118" stroke="#3A2A1A" strokeWidth="2.5" fill="none" />,
    front: <path d="M168 196 L176 70 Q178 58 168 56" stroke="#8A6A3A" strokeWidth="5" fill="none" strokeLinecap="round" />,
  },
  // Coco : croque-mitaine des berceuses, ombre drapée aux yeux luisants
  '¡': {
    body: '#2A2A3A', belly: '#3A3A4E', head: '#2E2E40', eye: '#F2D94E',
    back: <path d="M30 190 Q40 120 60 80 Q100 20 140 80 Q160 120 170 190 Q150 176 135 190 Q118 176 100 190 Q82 176 65 190 Q50 176 30 190Z" fill="#1F1F2E" />,
    face: <path d="M86 118 L92 124 L100 118 L108 124 L114 118" stroke="#F2D94E" strokeWidth="2" fill="none" strokeLinejoin="round" />,
  },
  // ───── Gardiens allemands (Goethe A1 — la Route des contes des frères Grimm) ─────
  // Rumpelstilzchen : petit bonhomme à longue barbe, bonnet pointu, fil d'or
  Ä: {
    body: '#7A5A3A', belly: '#C9B08A', head: '#E8C8A8', eye: '#2A1A10',
    top: <path d="M56 70 Q76 14 132 6 Q116 38 144 70Z" fill="#6E3A8A" stroke="#4A2460" strokeWidth="2" />,
    under: <path d="M70 108 Q100 176 130 108 Q116 122 100 122 Q84 122 70 108Z" fill="#E8E0D0" />,
    face: <path d="M94 104 Q100 112 106 104" stroke="#8A5A3A" strokeWidth="3" fill="none" strokeLinecap="round" />,
    front: <g transform="translate(158 150)"><circle r="12" fill="none" stroke="#E2B84A" strokeWidth="5" /><path d="M-12 0 H12 M0 -12 V12" stroke="#E2B84A" strokeWidth="2" /><path d="M12 0 Q26 -20 18 -40" stroke="#E2B84A" strokeWidth="2" fill="none" /></g>,
  },
  // Les sept Nains : bonnet rouge tombant, barbe blanche, pioche et lanterne
  Ö: {
    body: '#3A6AA8', belly: '#9CC0E4', head: '#E8C8A8', eye: '#2A1A10',
    top: <path d="M56 72 Q70 22 118 26 Q150 30 158 62 Q138 44 142 72Z" fill="#C8323F" stroke="#8E1B26" strokeWidth="2" />,
    under: <path d="M66 104 Q100 164 134 104 Q118 120 100 120 Q82 120 66 104Z" fill="#FFFFFF" />,
    front: <g><path d="M30 196 L52 110" stroke="#7A4A2A" strokeWidth="5" strokeLinecap="round" /><path d="M36 106 Q54 96 70 112" stroke="#8A93A6" strokeWidth="6" fill="none" strokeLinecap="round" /><text x="160" y="168" fontSize="26" fontWeight="900" fill="#E2B84A" textAnchor="middle">7</text></g>,
  },
  // Le Loup du Chaperon rouge : pelage gris, grandes oreilles, bonnet de nuit de la grand-mère
  ß: {
    body: '#6A6E78', belly: '#C9CCD4', head: '#7A7E88', eye: '#F2D94E',
    top: <>{ear(58, false, '#6A6E78', '#E8B8B0')}{ear(142, true, '#6A6E78', '#E8B8B0')}<path d="M62 62 Q100 22 138 62 Q120 50 100 50 Q80 50 62 62Z" fill="#FFFFFF" stroke="#E8B8D0" strokeWidth="3" /></>,
    under: <ellipse cx="100" cy="112" rx="22" ry="16" fill="#C9CCD4" />,
    face: <><ellipse cx="100" cy="102" rx="7" ry="5" fill="#1F2433" /><path d="M86 116 L91 124 L96 116 L100 124 L104 116 L109 124 L114 116" fill="#FFFFFF" stroke="#1F2433" strokeWidth="1.5" strokeLinejoin="round" /></>,
  },
  // La Sorcière de pain d'épices : chapeau noir, nez crochu, bonhomme de pain d'épices
  ä: {
    body: '#4A3A5A', belly: '#7A6A8A', head: '#C8D8A8', eye: '#2A1A10',
    top: <><ellipse cx="100" cy="52" rx="60" ry="9" fill="#2A2233" /><path d="M72 52 Q88 2 124 -4 Q112 26 128 52Z" fill="#2A2233" /><rect x="74" y="42" width="52" height="7" fill="#B8733A" /></>,
    face: <path d="M100 92 Q112 104 100 112" stroke="#8AA06A" strokeWidth="6" fill="none" strokeLinecap="round" />,
    front: <g transform="translate(156 152)" fill="#B8733A" stroke="#FFFFFF" strokeWidth="1.5"><circle cx="0" cy="-14" r="7" /><path d="M-4 -8 H4 L12 -2 L10 2 L5 -1 V8 L9 18 H4 L0 10 L-4 18 H-9 L-5 8 V-1 L-10 2 L-12 -2Z" /></g>,
  },
  // La Treizième Fée : voile sombre, fuseau et rose des ronces
  ö: {
    body: '#3A2A5A', belly: '#6A5A9A', head: '#E8D8E8', eye: '#5A2A8A',
    back: <path d="M40 80 Q20 150 44 190 L156 190 Q180 150 160 80 Q100 20 40 80Z" fill="#2A1F44" />,
    top: <path d="M54 84 Q54 34 100 30 Q146 34 146 84 Q130 56 100 54 Q70 56 54 84Z" fill="#2A1F44" />,
    front: <g><path d="M160 196 V112" stroke="#C9B08A" strokeWidth="3" /><path d="M160 104 L154 122 H166Z" fill="#E8E0D0" stroke="#8A7A5A" strokeWidth="1.5" /><g transform="translate(40 150)"><circle r="8" fill="#C8323F" /><path d="M-4 -2 Q0 4 4 -2" stroke="#8E1B26" strokeWidth="1.5" fill="none" /><path d="M0 8 V26 M0 16 l6 -4" stroke="#2F6B4F" strokeWidth="2.5" /></g></g>,
  },
  // Le Vaillant Petit Tailleur : ceinture « 7 », ciseaux, bonnet à plume
  '7': {
    body: '#2F6B4F', belly: '#F4EDDC', head: '#E8C8A8', eye: '#2A1A10',
    top: <><path d="M58 66 Q100 26 142 66 Q120 54 100 54 Q80 54 58 66Z" fill="#8A6A3A" /><path d="M128 52 Q146 20 160 22 Q150 38 140 58Z" fill="#C8323F" /></>,
    under: <g><rect x="52" y="156" width="96" height="12" fill="#E2B84A" /><text x="100" y="166" fontSize="11" fontWeight="900" fill="#5A3A1A" textAnchor="middle">7</text></g>,
    front: <g transform="translate(158 140) rotate(20)" stroke="#8A93A6" strokeWidth="3" fill="none"><path d="M-6 -22 L4 8 M6 -22 L-4 8" /><circle cx="-6" cy="14" r="5" stroke="#C8323F" /><circle cx="6" cy="14" r="5" stroke="#C8323F" /></g>,
  },
  // Dame Holle : coiffe blanche, édredon et flocons
  '❄': {
    body: '#8AA8C8', belly: '#E8F0F8', head: '#F0DCCB', eye: '#2A3A5A',
    top: <><path d="M54 78 Q54 30 100 28 Q146 30 146 78 Q124 56 100 56 Q76 56 54 78Z" fill="#FFFFFF" stroke="#C9D4E4" strokeWidth="2" /><path d="M54 78 Q46 96 54 112 M146 78 Q154 96 146 112" stroke="#FFFFFF" strokeWidth="8" fill="none" strokeLinecap="round" /></>,
    front: <g><rect x="132" y="126" width="46" height="34" rx="10" fill="#FFFFFF" stroke="#C9D4E4" strokeWidth="2" /><path d="M144 126 V160 M156 126 V160 M168 126 V160" stroke="#C9D4E4" strokeWidth="1.5" /><g fill="#FFFFFF" stroke="#C9D4E4" strokeWidth="1">{[[24, 40], [38, 70], [16, 96], [176, 36], [186, 84], [150, 14]].map(([x, y]) => <circle key={`${x}${y}`} cx={x} cy={y} r="4" />)}</g></g>,
  },
  // Le Joueur de flûte : habit bariolé, chapeau à plume, flûte et notes
  '♪': {
    body: '#C8323F', belly: '#E2B84A', head: '#E8C8A8', eye: '#2A1A10',
    back: <path d="M50 120 L50 184 L74 170 L100 186 L126 170 L150 184 L150 120Z" fill="#2F6B4F" />,
    top: <><path d="M56 68 Q100 30 144 68 Q120 56 100 56 Q80 56 56 68Z" fill="#2F6B4F" /><path d="M60 62 Q40 26 30 30 Q44 44 52 68Z" fill="#E2B84A" /></>,
    under: <path d="M100 118 V178 M84 124 V176 M116 124 V176" stroke="#3A6AA8" strokeWidth="5" opacity="0.7" />,
    front: <g><path d="M104 112 L168 96" stroke="#7A4A2A" strokeWidth="5" strokeLinecap="round" /><g fill="#1F2433"><circle cx="176" cy="66" r="5" /><rect x="179" y="44" width="2.5" height="22" /><circle cx="158" cy="54" r="5" /><rect x="161" y="32" width="2.5" height="22" /></g></g>,
  },
  // ───── Gardiens allemands (Goethe A2 — du Rhin à la Forêt-Noire) ─────
  // Le Roi Grenouille : grenouille verte, petite couronne, balle d'or
  '♔': {
    body: '#4E9A4A', belly: '#D8ECA8', head: '#5AAE56', eye: '#1F3A20',
    top: <><circle cx="70" cy="52" r="16" fill="#5AAE56" /><circle cx="130" cy="52" r="16" fill="#5AAE56" /><path d="M84 40 L88 22 L96 34 L100 18 L104 34 L112 22 L116 40Z" fill="#E2B84A" stroke="#9A7A2A" strokeWidth="1.5" /></>,
    face: <path d="M74 112 Q100 132 126 112" stroke="#1F3A20" strokeWidth="3" fill="none" strokeLinecap="round" />,
    front: <circle cx="156" cy="158" r="13" fill="#E2B84A" stroke="#9A7A2A" strokeWidth="2" />,
  },
  // La Marâtre de Cendrillon : chignon sévère, col haut, balai
  '♟': {
    body: '#4A3A4E', belly: '#7A6A80', head: '#E8D0C0', eye: '#2A1A2A',
    top: <><circle cx="100" cy="36" r="18" fill="#5A4A4A" /><path d="M56 84 Q56 40 100 38 Q144 40 144 84 Q126 60 100 60 Q74 60 56 84Z" fill="#5A4A4A" /></>,
    under: <path d="M70 128 Q100 112 130 128 L124 140 Q100 128 76 140Z" fill="#E8E0D0" />,
    face: <path d="M90 118 Q100 112 110 118" stroke="#6A3A3A" strokeWidth="2.5" fill="none" strokeLinecap="round" />,
    front: <g><path d="M34 196 L46 96" stroke="#7A4A2A" strokeWidth="5" strokeLinecap="round" /><path d="M24 196 L34 172 H46 L42 198Z" fill="#C9A24A" /></g>,
  },
  // Dame Gothel : capuche sombre, mèche grise, grande tresse dorée volée
  '♜': {
    body: '#3A4A3A', belly: '#5E6E5A', head: '#D8D0B8', eye: '#2A2A1A',
    back: <path d="M42 84 Q24 150 46 190 L154 190 Q176 150 158 84 Q100 22 42 84Z" fill="#2A3A2A" />,
    top: <path d="M52 86 Q52 32 100 28 Q148 32 148 86 Q130 54 100 52 Q70 54 52 86Z" fill="#2A3A2A" />,
    under: <path d="M76 62 Q86 78 80 96" stroke="#B8B8B8" strokeWidth="6" fill="none" strokeLinecap="round" />,
    front: <path d="M150 110 Q170 130 158 150 Q146 170 162 196" stroke="#E2B84A" strokeWidth="9" fill="none" strokeLinecap="round" />,
  },
  // La Reine au miroir : haute couronne, col noir, miroir à main
  '♕': {
    body: '#5A2A6A', belly: '#8A5A9A', head: '#F0E0D8', eye: '#2A1A3A',
    back: <path d="M50 96 Q30 60 60 44 Q100 76 140 44 Q170 60 150 96Z" fill="#1F1A2A" />,
    top: <><path d="M56 82 Q56 38 100 36 Q144 38 144 82 Q126 58 100 58 Q74 58 56 82Z" fill="#1F1A2A" /><path d="M72 40 L72 14 L86 30 L100 8 L114 30 L128 14 L128 40Z" fill="#E2B84A" stroke="#9A7A2A" strokeWidth="1.5" /></>,
    face: <path d="M92 116 Q100 120 108 116" stroke="#8E1B26" strokeWidth="3" fill="none" strokeLinecap="round" />,
    front: <g transform="translate(160 146)"><path d="M0 14 V40" stroke="#E2B84A" strokeWidth="5" strokeLinecap="round" /><ellipse rx="14" ry="17" fill="#E2B84A" /><ellipse rx="10" ry="13" fill="#CFE6F2" /></g>,
  },
  // Jean le Chanceux : chapeau de paille, baluchon, trèfle
  '☘': {
    body: '#B8823A', belly: '#F4EDDC', head: '#E8C8A8', eye: '#2A1A10',
    top: <><ellipse cx="100" cy="54" rx="62" ry="9" fill="#E2C46A" /><path d="M70 54 Q72 28 100 26 Q128 28 130 54Z" fill="#E2C46A" stroke="#B89A3A" strokeWidth="1.5" /></>,
    front: <g><path d="M176 196 L150 92" stroke="#7A4A2A" strokeWidth="4" strokeLinecap="round" /><circle cx="150" cy="88" r="15" fill="#C8323F" /><g transform="translate(42 150)" fill="#3E8A3A"><circle cx="-5" cy="-3" r="6" /><circle cx="5" cy="-3" r="6" /><circle cx="0" cy="5" r="6" /><path d="M0 8 V18" stroke="#3E8A3A" strokeWidth="2.5" /></g></g>,
  },
  // Le Chat botté : chat roux, chapeau à plume, grandes bottes
  '♞': {
    body: '#C8823A', belly: '#F6E0B8', head: '#D8924A', eye: '#2E6A3A',
    top: <>{ear(58, false, '#C8823A', '#F2B8A8')}{ear(142, true, '#C8823A', '#F2B8A8')}<ellipse cx="100" cy="50" rx="50" ry="8" fill="#3A2A2A" /><path d="M76 50 Q78 30 100 28 Q122 30 124 50Z" fill="#3A2A2A" /><path d="M122 40 Q150 10 162 16 Q150 30 134 50Z" fill="#C8323F" /></>,
    face: <><path d="M96 104 L104 104 L100 110Z" fill="#8E3A2A" /><path d="M70 106 H48 M70 112 H50 M130 106 H152 M130 112 H150" stroke="#5A3A1A" strokeWidth="1.5" /></>,
    front: <g fill="#5A3A24"><path d="M60 168 H96 V192 H56 Q54 180 60 168Z" /><path d="M104 168 H140 Q146 180 144 192 H104Z" /><rect x="58" y="164" width="40" height="7" fill="#7A5A3A" /><rect x="102" y="164" width="40" height="7" fill="#7A5A3A" /></g>,
  },
  // L'Oie d'or : plumage doré, bec orange, plumes brillantes
  '♢': {
    body: '#E2B84A', belly: '#FFF0B8', head: '#EEC85A', eye: '#2A1A10',
    back: <path d="M48 120 Q14 104 20 70 Q40 96 62 104 M152 120 Q186 104 180 70 Q160 96 138 104" fill="#C89A2A" stroke="#9A7A2A" strokeWidth="2" />,
    face: <path d="M86 104 Q100 96 114 104 Q108 120 100 122 Q92 120 86 104Z" fill="#E2703A" stroke="#B8502A" strokeWidth="1.5" />,
    front: <g fill="#FFFFFF" opacity="0.9">{[[36, 40], [166, 34], [150, 180], [44, 176]].map(([x, y]) => <path key={`${x}${y}`} d={`M${x} ${y - 7} L${x + 2} ${y - 2} L${x + 7} ${y} L${x + 2} ${y + 2} L${x} ${y + 7} L${x - 2} ${y + 2} L${x - 7} ${y} L${x - 2} ${y - 2}Z`} />)}</g>,
  },
  // Le Roi Barbe-de-Grive : couronne, longue barbe pointue, violon de ménestrel
  '♚': {
    body: '#3A5A8A', belly: '#9CB8D8', head: '#E8C8A8', eye: '#2A1A10',
    top: <path d="M66 48 L66 20 L82 36 L100 14 L118 36 L134 20 L134 48Z" fill="#E2B84A" stroke="#9A7A2A" strokeWidth="1.5" />,
    under: <path d="M72 108 Q100 124 128 108 Q116 150 100 176 Q84 150 72 108Z" fill="#8A5A3A" />,
    front: <g transform="translate(158 150) rotate(-25)"><ellipse rx="11" ry="15" fill="#B8733A" stroke="#7A4A2A" strokeWidth="1.5" /><rect x="-2" y="-40" width="4" height="28" fill="#7A4A2A" /><path d="M-1 -12 V12 M1 -12 V12" stroke="#F4EDDC" strokeWidth="0.8" /></g>,
  },
  // ───── Gardiens allemands (Goethe B1 — le pays des légendes) ─────
  // L'Empereur Barberousse : couronne impériale, immense barbe rousse, yeux mi-clos
  '♤': {
    body: '#7A2A2A', belly: '#B8923A', head: '#E8C8A8', eye: '#3A2A1A',
    top: <><path d="M64 50 L64 24 L78 38 L100 12 L122 38 L136 24 L136 50Z" fill="#E2B84A" stroke="#9A7A2A" strokeWidth="1.5" /><circle cx="100" cy="30" r="5" fill="#C8323F" /></>,
    under: <path d="M64 100 Q100 120 136 100 Q150 160 100 196 Q50 160 64 100Z" fill="#C8582A" />,
    face: <><path d="M76 84 H92 M108 84 H124" stroke="#3A2A1A" strokeWidth="4" strokeLinecap="round" /><path d="M84 108 Q100 116 116 108" stroke="#8A3A1A" strokeWidth="3" fill="none" /></>,
  },
  // Rübezahl : géant des montagnes, barbe de mousse, bâton noueux
  '♧': {
    body: '#5A6A4A', belly: '#8A9A7A', head: '#C8B898', eye: '#2A3A1A',
    top: <path d="M52 76 Q60 30 100 26 Q140 30 148 76 Q128 52 100 50 Q72 52 52 76Z" fill="#4A5A3A" />,
    under: <path d="M68 104 Q100 120 132 104 Q128 150 100 170 Q72 150 68 104Z" fill="#6E8A5A" />,
    front: <g><path d="M164 198 Q158 140 166 84" stroke="#6A4A2A" strokeWidth="8" fill="none" strokeLinecap="round" /><circle cx="166" cy="80" r="9" fill="#6A4A2A" /><path d="M24 150 L34 128 L44 150Z M16 170 L30 144 L44 170Z" fill="#2F6B4F" /></g>,
  },
  // La Femme du pêcheur (Ilsebill) : fichu, couronne trop grande, vague sombre
  '♡': {
    body: '#3A5A7A', belly: '#7A9AB8', head: '#E8D0C0', eye: '#2A2A3A',
    back: <path d="M10 196 q22 -30 44 0 q22 -30 46 0 q24 -30 46 0 q22 -30 44 0 V200 H10Z" fill="#2A3A4A" />,
    top: <><path d="M54 84 Q54 36 100 34 Q146 36 146 84 Q126 58 100 58 Q74 58 54 84Z" fill="#C8323F" /><path d="M70 40 L70 20 L84 32 L100 14 L116 32 L130 20 L130 40Z" fill="#E2B84A" stroke="#9A7A2A" strokeWidth="1.5" transform="rotate(-12 100 30)" /></>,
    face: <path d="M88 118 Q100 110 112 118" stroke="#8E1B26" strokeWidth="3" fill="none" strokeLinecap="round" />,
  },
  // Les Lutins de Cologne : bonnet pointu, tablier, marteau et lanterne
  '♙': {
    body: '#8A4A6A', belly: '#F4EDDC', head: '#E8C8A8', eye: '#2A1A10',
    top: <path d="M58 72 Q84 10 96 -6 Q112 30 142 72Z" fill="#3A6AA8" stroke="#2A4A78" strokeWidth="2" />,
    under: <path d="M72 130 H128 V176 Q100 186 72 176Z" fill="#F4EDDC" stroke="#C9B08A" strokeWidth="1.5" />,
    front: <g><path d="M160 190 L150 120" stroke="#7A4A2A" strokeWidth="5" strokeLinecap="round" /><rect x="136" y="106" width="30" height="16" rx="3" fill="#8A93A6" /><g transform="translate(40 156)"><rect x="-8" y="-12" width="16" height="20" rx="3" fill="#E2B84A" stroke="#5A3A24" strokeWidth="2" /><path d="M-5 -12 Q0 -22 5 -12" stroke="#5A3A24" strokeWidth="2" fill="none" /></g></g>,
  },
  // Le Docteur Faust : bonnet de savant, col blanc, livre et plume
  '♗': {
    body: '#2A2A3A', belly: '#4A4A5E', head: '#E8D8C8', eye: '#2A1A2A',
    top: <path d="M56 70 Q60 34 100 30 Q140 34 144 70 Q146 52 100 50 Q54 52 56 70Z" fill="#5A1F2A" />,
    under: <><path d="M70 126 Q100 114 130 126 L126 138 Q100 128 74 138Z" fill="#FFFFFF" /><path d="M84 106 Q100 126 116 106 Q108 130 100 136 Q92 130 84 106Z" fill="#B8B8B8" /></>,
    front: <g><g transform="translate(152 152)"><path d="M-18 -10 Q-9 -16 0 -10 Q9 -16 18 -10 V10 Q9 4 0 10 Q-9 4 -18 10Z" fill="#F4EDDC" stroke="#5A3A24" strokeWidth="1.5" /><path d="M0 -10 V10" stroke="#5A3A24" strokeWidth="1" /></g><path d="M36 180 Q44 140 60 116" stroke="#F4EDDC" strokeWidth="3" fill="none" strokeLinecap="round" /></g>,
  },
  // Till l'Espiègle : bonnet de bouffon à grelots, chouette et miroir
  '♘': {
    body: '#C8323F', belly: '#E2B84A', head: '#E8C8A8', eye: '#2A1A10',
    top: <><path d="M58 70 Q30 40 20 62 Q40 60 60 84Z" fill="#E2B84A" /><path d="M142 70 Q170 40 180 62 Q160 60 140 84Z" fill="#3E8A3A" /><path d="M56 78 Q60 36 100 34 Q140 36 144 78 Q124 56 100 56 Q76 56 56 78Z" fill="#C8323F" /><circle cx="20" cy="64" r="5" fill="#E2B84A" stroke="#9A7A2A" /><circle cx="180" cy="64" r="5" fill="#E2B84A" stroke="#9A7A2A" /></>,
    under: <path d="M100 122 V180" stroke="#3E8A3A" strokeWidth="46" opacity="0.5" strokeDasharray="14 14" />,
    face: <path d="M80 110 Q100 128 120 110" stroke="#8E1B26" strokeWidth="3" fill="none" strokeLinecap="round" />,
    front: <g transform="translate(160 150)"><path d="M0 14 V38" stroke="#7A4A2A" strokeWidth="5" strokeLinecap="round" /><circle r="14" fill="#C9D4E4" stroke="#7A4A2A" strokeWidth="3" /></g>,
  },
  // La Lorelei : longue chevelure dorée, peigne d'or, vagues du Rhin
  '♫': {
    body: '#3A7A8A', belly: '#A8D8D0', head: '#F0E0D8', eye: '#2A4A5A',
    back: <path d="M46 80 Q20 140 40 196 L160 196 Q180 140 154 80 Q100 20 46 80Z" fill="#E2B84A" />,
    top: <path d="M54 84 Q54 34 100 30 Q146 34 146 84 Q128 56 100 54 Q72 56 54 84Z" fill="#E2B84A" />,
    front: <g><g transform="translate(160 132) rotate(20)"><rect x="-10" y="-4" width="20" height="6" rx="2" fill="#C89A2A" />{[-8, -4, 0, 4, 8].map((x) => <rect key={x} x={x - 1} y="2" width="2" height="10" fill="#C89A2A" />)}</g><path d="M14 184 q14 -14 28 0 q14 14 28 0" fill="none" stroke="#FFFFFF" strokeWidth="3" opacity="0.8" /></g>,
  },
  // Le Baron de Münchhausen : tricorne, moustache en croc, boulet de canon
  '♖': {
    body: '#2E4A7A', belly: '#E2B84A', head: '#E8C8A8', eye: '#2A1A10',
    top: <path d="M40 66 Q100 20 160 66 Q130 54 100 60 Q70 54 40 66Z" fill="#1F1A2A" stroke="#E2B84A" strokeWidth="2" />,
    face: <><path d="M100 104 Q84 98 72 108 M100 104 Q116 98 128 108" stroke="#5A3A1A" strokeWidth="4" fill="none" strokeLinecap="round" /><path d="M92 116 Q100 120 108 116" stroke="#8A3A1A" strokeWidth="2.5" fill="none" /></>,
    front: <g><circle cx="158" cy="160" r="18" fill="#3A3A3A" /><circle cx="152" cy="154" r="5" fill="#7A7A7A" /><path d="M170 144 Q182 132 178 120" stroke="#E2703A" strokeWidth="3" fill="none" strokeLinecap="round" /></g>,
  },
  // ───── Gardiens allemands (Goethe B2 — Weimar, la cour des poètes) ─────
  // Le Roi des Aulnes : couronne de branches, manteau de brume, longue traîne grise
  '☾': {
    body: '#5A6A72', belly: '#A8B8BE', head: '#D8E0DC', eye: '#E8F4F0',
    back: <path d="M30 196 Q20 120 60 70 Q100 40 140 70 Q180 120 170 196 Q140 176 100 190 Q60 176 30 196Z" fill="#8A9AA0" opacity="0.7" />,
    top: <><path d="M62 62 L56 26 M78 54 L72 14 M100 50 V8 M122 54 L128 14 M138 62 L144 26" stroke="#4A5A4A" strokeWidth="5" strokeLinecap="round" /><path d="M72 30 l-8 -6 M100 22 l8 -8 M128 30 l8 -6" stroke="#4A5A4A" strokeWidth="3" strokeLinecap="round" /></>,
    face: <path d="M88 116 Q100 110 112 116" stroke="#3A4A52" strokeWidth="3" fill="none" strokeLinecap="round" />,
    front: <path d="M10 160 q14 -10 28 0 t28 0 M134 176 q14 -10 28 0 t28 0" stroke="#FFFFFF" strokeWidth="3" fill="none" opacity="0.6" strokeLinecap="round" />,
  },
  // Le Balai ensorcelé : manche de bois, brins de paille, deux seaux qui débordent
  '✤': {
    body: '#C8A45A', belly: '#E8D08A', head: '#9A6A3A', eye: '#FFFFFF',
    top: <rect x="93" y="-6" width="14" height="60" rx="5" fill="#7A4A2A" />,
    under: <path d="M64 150 L58 198 M76 154 L72 198 M88 156 L86 198 M100 158 V198 M112 156 L114 198 M124 154 L128 198 M136 150 L142 198" stroke="#B8923A" strokeWidth="5" strokeLinecap="round" />,
    front: <g><g transform="translate(30 150)"><path d="M-12 -12 H12 L9 12 H-9Z" fill="#7A4A2A" stroke="#5A3A24" strokeWidth="2" /><path d="M-12 -12 Q0 -30 12 -12" stroke="#5A3A24" strokeWidth="2.5" fill="none" /><path d="M-10 -12 H10 V-8 H-10Z" fill="#7FC4D8" /><path d="M-6 12 q-2 8 0 12 M6 12 q2 8 0 12" stroke="#7FC4D8" strokeWidth="3" strokeLinecap="round" /></g><g transform="translate(170 150)"><path d="M-12 -12 H12 L9 12 H-9Z" fill="#7A4A2A" stroke="#5A3A24" strokeWidth="2" /><path d="M-12 -12 Q0 -30 12 -12" stroke="#5A3A24" strokeWidth="2.5" fill="none" /><path d="M-10 -12 H10 V-8 H-10Z" fill="#7FC4D8" /></g></g>,
  },
  // Le Monstre du gouffre : pieuvre des abysses, tentacules, coupe d'or
  '❂': {
    body: '#3A4A7A', belly: '#6A7AB8', head: '#4A5A8E', eye: '#F2D94E',
    back: <path d="M40 150 Q10 170 14 198 M60 170 Q40 186 44 200 M160 150 Q190 170 186 198 M140 170 Q160 186 156 200" stroke="#3A4A7A" strokeWidth="12" fill="none" strokeLinecap="round" />,
    top: <path d="M56 80 Q54 28 100 24 Q146 28 144 80 Q124 60 100 60 Q76 60 56 80Z" fill="#2A3A66" />,
    under: <>{[70, 85, 100, 115, 130].map((x) => <circle key={x} cx={x} cy="150" r="4" fill="#A8B4E0" />)}</>,
    front: <g transform="translate(164 120)"><path d="M-12 -12 H12 Q12 4 0 6 Q-12 4 -12 -12Z" fill="#E2B84A" stroke="#9A7A2A" strokeWidth="1.5" /><path d="M0 6 V16 M-7 16 H7" stroke="#9A7A2A" strokeWidth="3" strokeLinecap="round" /></g>,
  },
  // Le Lion de l'arène : crinière fauve, museau, gant tombé à ses pieds
  '✠': {
    body: '#C8923A', belly: '#F0D8A0', head: '#E2B45A', eye: '#3A2A10',
    back: <>{Array.from({ length: 12 }, (_, i) => { const a = (i * Math.PI) / 6; return <ellipse key={i} cx={100 + Math.cos(a) * 52} cy={84 + Math.sin(a) * 50} rx="20" ry="14" transform={`rotate(${(i * 30)} ${100 + Math.cos(a) * 52} ${84 + Math.sin(a) * 50})`} fill="#8A5A2A" />; })}</>,
    face: <><path d="M92 100 H108 L100 110Z" fill="#5A3A1A" /><path d="M100 110 V116 M100 116 Q92 124 84 118 M100 116 Q108 124 116 118" stroke="#5A3A1A" strokeWidth="2.5" fill="none" strokeLinecap="round" /></>,
    front: <g transform="translate(156 184) rotate(-14)"><path d="M-14 -8 H6 Q14 -8 14 0 Q14 8 6 8 H-14Z" fill="#F4EDDC" stroke="#8A7A5A" strokeWidth="1.5" /><path d="M-14 -8 V8" stroke="#C8323F" strokeWidth="4" /></g>,
  },
  // Les Grues d'Ibycus : long cou, calotte rouge, ailes grises déployées
  '❖': {
    body: '#8A93A0', belly: '#D8DCE2', head: '#E8ECF0', eye: '#2A2A2A',
    back: <><path d="M56 130 Q10 110 2 150 Q30 140 60 160Z" fill="#6A7380" /><path d="M144 130 Q190 110 198 150 Q170 140 140 160Z" fill="#6A7380" /></>,
    top: <path d="M78 60 Q100 44 122 60 Q112 52 100 52 Q88 52 78 60Z" fill="#C8323F" stroke="#C8323F" strokeWidth="6" strokeLinejoin="round" />,
    face: <path d="M92 100 L100 132 L108 100Z" fill="#3A3A3A" />,
    front: <g stroke="#3A3A3A" strokeWidth="2.5" fill="none" strokeLinecap="round"><path d="M20 40 l10 8 l10 -8" /><path d="M150 30 l10 8 l10 -8" /><path d="M164 60 l8 6 l8 -6" /></g>,
  },
  // Le Chasseur sauvage : chapeau à plume, barbe noire, cor de chasse
  '✺': {
    body: '#2F4A36', belly: '#5A7A5E', head: '#D8B898', eye: '#E2703A',
    top: <><path d="M44 66 Q100 50 156 66 Q132 60 100 62 Q68 60 44 66Z" fill="#1F2E22" stroke="#1F2E22" strokeWidth="6" strokeLinejoin="round" /><path d="M66 60 Q70 30 100 28 Q130 30 134 60Z" fill="#1F2E22" /><path d="M128 40 Q150 10 166 14 Q150 26 138 50Z" fill="#C8323F" /></>,
    under: <path d="M72 106 Q100 122 128 106 Q124 150 100 164 Q76 150 72 106Z" fill="#1F1A1A" />,
    front: <g transform="translate(158 150)"><path d="M-16 6 Q-22 -22 4 -22 Q22 -22 18 -2" stroke="#E2B84A" strokeWidth="7" fill="none" strokeLinecap="round" /><path d="M18 -2 L28 12 L8 10Z" fill="#E2B84A" /></g>,
  },
  // L'Ondine : chevelure d'algues, couronne de nénuphars, eau jusqu'aux épaules
  '⚘': {
    body: '#3F8A8A', belly: '#A8E0D8', head: '#E0F0E8', eye: '#1F5A6A',
    back: <path d="M50 78 Q24 130 36 196 L164 196 Q176 130 150 78 Q100 24 50 78Z" fill="#2F6B5A" />,
    top: <><path d="M56 82 Q56 36 100 32 Q144 36 144 82 Q126 58 100 56 Q74 58 56 82Z" fill="#2F6B5A" />{[72, 100, 128].map((x) => <g key={x} transform={`translate(${x} ${x === 100 ? 34 : 42})`}><path d="M0 0 q-4 -8 0 -12 q4 4 0 12Z M0 0 q-9 -3 -9 -9 q7 0 9 9Z M0 0 q9 -3 9 -9 q-7 0 -9 9Z" fill="#F4C8D8" /><circle r="2" fill="#E2B84A" /></g>)}</>,
    front: <path d="M0 176 q16 -14 32 0 t32 0 t34 0 t34 0 t34 0 t34 0 V200 H0Z" fill="#7FC4D8" opacity="0.85" />,
  },
  // Méphisto : calotte rouge à plume, barbiche, contrat roulé et plume
  '✥': {
    body: '#7A1F26', belly: '#2A1A1E', head: '#E0C8B8', eye: '#F2D94E',
    top: <><path d="M58 72 Q60 30 100 26 Q140 30 142 72 Q122 54 100 54 Q78 54 58 72Z" fill="#C8323F" /><path d="M100 56 L92 70 H108Z" fill="#C8323F" /><path d="M134 40 Q160 4 170 10 Q156 24 142 52Z" fill="#1F1A1A" /></>,
    under: <path d="M92 124 Q100 128 108 124 L100 150Z" fill="#1F1A1A" />,
    face: <><path d="M72 74 L92 82 M128 74 L108 82" stroke="#1F1A1A" strokeWidth="4" strokeLinecap="round" /><path d="M84 112 Q100 122 118 108" stroke="#5A1F1A" strokeWidth="3" fill="none" strokeLinecap="round" /></>,
    front: <g><g transform="translate(160 150) rotate(-18)"><rect x="-10" y="-22" width="20" height="44" rx="4" fill="#F4EDDC" stroke="#8A7A5A" strokeWidth="1.5" /><path d="M-5 -12 H5 M-5 -4 H5 M-5 4 H3" stroke="#8A7A5A" strokeWidth="1.5" /><circle cx="4" cy="14" r="4" fill="#C8323F" /></g><path d="M34 186 Q44 150 62 126" stroke="#F4EDDC" strokeWidth="3" fill="none" strokeLinecap="round" /></g>,
  },
  // ───── Gardiens espagnols (DELE A2 — la route de Barcelone) ─────
  // Lamia : nymphe des rivières, longue chevelure dorée, peigne d'or
  ñ: {
    body: '#5A8AA8', belly: '#BFDCEA', head: '#E8C8A8', eye: '#1F3A5A',
    back: <path d="M54 70 Q34 140 50 186 L80 150 Q70 110 78 78Z M146 70 Q166 140 150 186 L120 150 Q130 110 122 78Z" fill="#E2B84A" />,
    top: <path d="M60 84 Q58 40 100 36 Q142 40 140 84 Q124 58 100 56 Q76 58 60 84Z" fill="#E2B84A" />,
    face: <path d="M90 116 Q100 124 110 116" stroke="#8A4A3A" strokeWidth="2.5" fill="none" />,
    front: <g transform="translate(158 146)"><rect x="-12" y="-4" width="24" height="7" rx="2" fill="#E2B84A" stroke="#9A7A2A" strokeWidth="1" /><path d="M-10 3 V12 M-5 3 V12 M0 3 V12 M5 3 V12 M10 3 V12" stroke="#E2B84A" strokeWidth="2" /></g>,
  },
  // Tragaldabas : ogre goinfre, gros ventre, serviette nouée, cuisse de poulet
  á: {
    body: '#B87A4A', belly: '#F2C89A', head: '#D9A07A', eye: '#2A1A10',
    top: <path d="M70 60 Q80 40 100 46 Q120 40 130 60" stroke="#5A3A24" strokeWidth="6" fill="none" strokeLinecap="round" />,
    under: <path d="M74 132 L100 150 L126 132 L100 138Z" fill="#F6F1E6" stroke="#B9AE98" strokeWidth="1.5" />,
    face: <><ellipse cx="100" cy="104" rx="8" ry="6" fill="#C8784A" /><path d="M82 120 Q100 134 118 120" stroke="#5A2A1A" strokeWidth="3" fill="#8E3A2A" /></>,
    front: <g transform="translate(160 150) rotate(-20)"><ellipse cx="0" cy="-8" rx="9" ry="12" fill="#C8823A" /><rect x="-2.5" y="2" width="5" height="12" rx="2" fill="#F6F1E6" /></g>,
  },
  // Hombre del Saco : vieux vagabond en manteau, chapeau rabattu, sac sur l'épaule
  é: {
    body: '#4A4038', belly: '#6A5E50', head: '#C9A27A', eye: '#F2D94E',
    top: <><ellipse cx="100" cy="54" rx="50" ry="8" fill="#2E2A26" /><path d="M72 54 Q74 30 100 28 Q126 30 128 54Z" fill="#2E2A26" /></>,
    under: <path d="M76 110 Q100 140 124 110 Q112 124 100 124 Q88 124 76 110Z" fill="#8A8078" />,
    back: <g transform="translate(150 70) rotate(18)"><ellipse cx="0" cy="20" rx="26" ry="30" fill="#A8925A" stroke="#6A5A3A" strokeWidth="2" /><path d="M-8 -8 Q0 -14 8 -8" stroke="#6A5A3A" strokeWidth="3" fill="none" /></g>,
  },
  // Encantada : demoiselle enchantée, voile d'eau, perles
  í: {
    body: '#7AA8C8', belly: '#DCEBF4', head: '#F0D2B8', eye: '#2A3A5A',
    back: <path d="M40 186 Q50 100 100 60 Q150 100 160 186 Q130 170 100 186 Q70 170 40 186Z" fill="#BFDCEA" opacity="0.8" />,
    top: <><path d="M62 82 Q60 42 100 38 Q140 42 138 82 Q120 62 100 60 Q80 62 62 82Z" fill="#2A2A3A" />{[76, 88, 100, 112, 124].map((x) => <circle key={x} cx={x} cy={46 - Math.abs(x - 100) / 6} r="3" fill="#FFFFFF" />)}</>,
    face: <path d="M92 118 Q100 122 108 118" stroke="#A84A5A" strokeWidth="2.5" fill="none" />,
  },
  // Diablo Cojuelo : petit diable boiteux, cornes, béquille, tuile à la main
  ó: {
    body: '#A83A2E', belly: '#E27A5A', head: '#C84A3A', eye: '#F2D94E',
    top: <path d="M74 58 Q60 34 70 22 Q74 40 86 50 M126 58 Q140 34 130 22 Q126 40 114 50" stroke="#2A1A10" strokeWidth="6" fill="none" strokeLinecap="round" />,
    face: <path d="M86 116 Q100 128 114 116 M94 120 L96 126 M104 120 L106 126" stroke="#2A1A10" strokeWidth="2.5" fill="none" />,
    front: <><path d="M40 196 L46 120 Q46 112 38 112" stroke="#7A4A2A" strokeWidth="5" fill="none" strokeLinecap="round" /><path d="M150 130 L176 124 L178 138 L152 144Z" fill="#9A3E22" /></>,
  },
  // Mari : dame des montagnes basques, couronne de flammes, boule de feu
  ú: {
    body: '#6A4A7A', belly: '#B8A0C8', head: '#E8C8A8', eye: '#2A1A30',
    top: <><path d="M62 84 Q58 42 100 38 Q142 42 138 84 Q122 60 100 58 Q78 60 62 84Z" fill="#3A2A2A" /><path d="M76 40 L82 22 L90 36 L100 16 L110 36 L118 22 L124 40Z" fill="#E2862A" /></>,
    face: <path d="M90 118 Q100 124 110 118" stroke="#8A3A4A" strokeWidth="2.5" fill="none" />,
    front: <g transform="translate(160 132)"><circle r="13" fill="#E2862A" /><circle r="7" fill="#F2D94E" /><path d="M-10 -10 Q-4 -24 0 -12 Q6 -26 10 -10" fill="#E2862A" /></g>,
  },
  // Mula Guita : mule de fête catalane, harnais rouge et or, étincelles
  ü: {
    body: '#3A3A3A', belly: '#6A6A6A', head: '#4A4A4A', eye: '#F2D94E',
    top: <path d="M74 56 Q64 18 80 12 Q86 30 88 52 M126 56 Q136 18 120 12 Q114 30 112 52" fill="#3A3A3A" stroke="#1F1F1F" strokeWidth="2" />,
    under: <path d="M58 136 H142 L136 150 H64Z" fill="#C8323F" stroke="#E2B84A" strokeWidth="2" />,
    face: <><ellipse cx="100" cy="118" rx="18" ry="11" fill="#6A6A6A" /><circle cx="93" cy="118" r="2.5" fill="#1F1F1F" /><circle cx="107" cy="118" r="2.5" fill="#1F1F1F" /></>,
    front: <g fill="#F2D94E">{[[150, 96], [164, 108], [172, 90], [40, 100], [30, 116]].map(([x, y]) => <path key={x} d={`M${x} ${y - 6} L${x + 2} ${y - 2} L${x + 6} ${y} L${x + 2} ${y + 2} L${x} ${y + 6} L${x - 2} ${y + 2} L${x - 6} ${y} L${x - 2} ${y - 2}Z`} />)}</g>,
  },
  // Drac : dragon de la légende de Sant Jordi, écailles vertes, ailes, rose
  Ñ: {
    body: '#3E8A5A', belly: '#C8E0A0', head: '#4E9A6A', eye: '#F2D94E',
    back: <path d="M50 110 Q10 70 24 30 Q40 64 64 84 M150 110 Q190 70 176 30 Q160 64 136 84" fill="#2E6A4A" stroke="#1E4A2A" strokeWidth="2" />,
    top: <path d="M78 56 L84 36 L92 52 L100 30 L108 52 L116 36 L122 56" fill="#E2B84A" />,
    face: <><path d="M86 116 Q100 126 114 116" stroke="#1E3A20" strokeWidth="3" fill="none" /><circle cx="94" cy="106" r="2" fill="#1E3A20" /><circle cx="106" cy="106" r="2" fill="#1E3A20" /></>,
    front: <g transform="translate(160 150)"><path d="M0 14 V-4" stroke="#3E7A3A" strokeWidth="2" /><circle cx="0" cy="-8" r="6" fill="#C8323F" /></g>,
  },
  // ───── Gardiens espagnols (DELE B1 — le chemin de Saint-Jacques) ─────
  // Herensuge : dragon à sept têtes de la sierra d'Aralar (petites têtes sur les épaules)
  'Ç': {
    body: '#4A7A3A', belly: '#C8D890', head: '#5A8A4A', eye: '#F2D94E',
    back: <g fill="#5A8A4A" stroke="#2E4A22" strokeWidth="1.5">{[[34, 78], [50, 56], [150, 56], [166, 78], [24, 104], [176, 104]].map(([x, y]) => <g key={`${x}${y}`}><path d={`M100 110 Q${(x + 100) / 2} ${y + 20} ${x} ${y}`} fill="none" strokeWidth="9" stroke="#4A7A3A" /><circle cx={x} cy={y} r="10" /><circle cx={x + 3} cy={y - 2} r="2.2" fill="#F2D94E" stroke="none" /></g>)}</g>,
    top: <path d="M84 56 L90 38 L96 54 L104 54 L110 38 L116 56" fill="#E2B84A" />,
    face: <path d="M88 118 Q100 126 112 118" stroke="#1E3A18" strokeWidth="3" fill="none" />,
  },
  // Gizotso : loup-garou basque, fourrure grise, oreilles pointues, crocs
  'ç': {
    body: '#6A6A72', belly: '#A8A8B0', head: '#7A7A84', eye: '#F2D94E',
    top: <>{ear(66, false, '#6A6A72', '#C8A8A8')}{ear(134, true, '#6A6A72', '#C8A8A8')}</>,
    face: <><ellipse cx="100" cy="114" rx="16" ry="11" fill="#9A9AA2" /><ellipse cx="100" cy="108" rx="5" ry="3.5" fill="#1F2433" /><path d="M92 120 L94 126 L96 120 M104 120 L106 126 L108 120" fill="#FFFFFF" /></>,
    back: <path d="M150 170 Q192 150 186 110 Q172 140 150 146Z" fill="#5A5A62" />,
  },
  // Tarasca : dragon de procession, carapace de tortue, cavalière juchée sur le dos
  'º': {
    body: '#3E7A5A', belly: '#BFE0A0', head: '#4E8A6A', eye: '#F2D94E',
    back: <><ellipse cx="100" cy="130" rx="82" ry="52" fill="#8A6A3A" stroke="#5A4A2A" strokeWidth="3" />{[[70, 112], [100, 104], [130, 112], [84, 146], [116, 146]].map(([x, y]) => <path key={`${x}${y}`} d={`M${x - 10} ${y} l10 -8 l10 8 l-10 8Z`} fill="#A8824A" />)}</>,
    top: <g transform="translate(100 40)"><path d="M-10 0 L0 -26 L10 0Z" fill="#C8323F" /><circle cx="0" cy="-30" r="6" fill="#E8C8A8" /></g>,
    face: <path d="M86 118 Q100 128 114 118" stroke="#1E3A20" strokeWidth="3" fill="#C8323F" />,
  },
  // Basilic : roi des serpents, crête de coq et couronne d'or
  'ª': {
    body: '#6E8A2E', belly: '#D8E08A', head: '#7E9A3E', eye: '#E2422E',
    top: <><path d="M80 52 L86 34 L94 48 L100 30 L106 48 L114 34 L120 52Z" fill="#E2B84A" stroke="#9A7A2A" strokeWidth="1.5" /><path d="M92 30 Q96 16 102 26 Q108 14 110 30" fill="#C8323F" /></>,
    back: <path d="M150 180 Q196 168 184 132 Q176 156 154 160 Q176 140 166 118" stroke="#5E7A1E" strokeWidth="14" fill="none" strokeLinecap="round" />,
    face: <><path d="M92 116 L100 124 L108 116Z" fill="#E2B84A" /><path d="M100 124 V132 M100 132 L96 136 M100 132 L104 136" stroke="#C8323F" strokeWidth="2" /></>,
  },
  // Trenti : petit lutin cantabre couvert de mousse et de feuilles
  '«': {
    body: '#5A7A3A', belly: '#8AAA5A', head: '#7A9A4A', eye: '#2A1A10',
    top: <g fill="#3E6A2A">{[[70, 62], [86, 46], [100, 40], [114, 46], [130, 62]].map(([x, y]) => <ellipse key={x} cx={x} cy={y} rx="12" ry="7" transform={`rotate(${(x - 100) / 2} ${x} ${y})`} />)}</g>,
    under: <path d="M78 112 Q100 150 122 112 Q110 126 100 126 Q90 126 78 112Z" fill="#4A6A2A" />,
    front: <g fill="#C8823A">{[[36, 140], [164, 136], [44, 170]].map(([x, y]) => <path key={x} d={`M${x} ${y} q6 -10 12 0 q-6 6 -12 0Z`} />)}</g>,
  },
  // Diaño burlón : diable farceur qui change de forme, cornes de bouc et sourire moqueur
  '»': {
    body: '#3A2A4A', belly: '#6A5A7A', head: '#B8323A', eye: '#F2D94E',
    top: <path d="M72 60 Q58 40 66 20 Q74 40 86 50 M128 60 Q142 40 134 20 Q126 40 114 50" stroke="#E8DCC0" strokeWidth="7" fill="none" strokeLinecap="round" />,
    face: <><path d="M82 114 Q100 132 118 114" stroke="#1F1F1F" strokeWidth="3" fill="#FFFFFF" /><path d="M96 134 Q100 150 104 134" fill="#3A2A2A" /></>,
    back: <path d="M150 160 Q186 170 180 130 L188 124 L178 122" stroke="#3A2A4A" strokeWidth="6" fill="none" strokeLinecap="round" />,
  },
  // Meiga : sorcière galicienne, foulard noir, chaudron de queimada aux flammes bleues
  '~': {
    body: '#2A2A3A', belly: '#4A4A5E', head: '#E8C8A8', eye: '#3A5A2A',
    top: <path d="M58 86 Q56 40 100 34 Q144 40 142 86 Q132 70 100 66 Q68 70 58 86Z" fill="#1F1F2A" />,
    face: <path d="M90 118 Q100 124 110 118" stroke="#6A2A3A" strokeWidth="2.5" fill="none" />,
    front: <g transform="translate(158 158)"><path d="M-18 -6 H18 Q16 16 0 18 Q-16 16 -18 -6Z" fill="#3A3A3A" /><path d="M-10 -8 Q-6 -24 0 -12 Q4 -26 10 -8" fill="#5A9AE2" opacity="0.85" /></g>,
  },
  // Urco : grand chien noir des côtes galiciennes, cornes de taureau, ruisselant d'eau de mer
  '€': {
    body: '#1F1F26', belly: '#3A3A44', head: '#2A2A32', eye: '#F2D94E',
    top: <path d="M70 62 Q48 52 44 30 Q60 44 80 50 M130 62 Q152 52 156 30 Q140 44 120 50" stroke="#E8DCC0" strokeWidth="7" fill="none" strokeLinecap="round" />,
    face: <><ellipse cx="100" cy="116" rx="17" ry="11" fill="#3A3A44" /><ellipse cx="100" cy="110" rx="6" ry="4" fill="#0F0F14" /></>,
    front: <g fill="#7AB8E2">{[[60, 186], [80, 192], [124, 192], [144, 186]].map(([x, y]) => <path key={x} d={`M${x} ${y - 8} Q${x + 3} ${y - 2} ${x} ${y} Q${x - 3} ${y - 2} ${x} ${y - 8}Z`} />)}</g>,
  },
  // ───── Gardiens hispano-américains (DELE B2 — la traversée des Amériques ; voyelles à tilde du guaraní) ─────
  // Guayota : démon guanche des volcans, corps de lave, cornes de basalte
  'ã': {
    body: '#3A2A2A', belly: '#E2622E', head: '#4A3030', eye: '#F2D94E',
    top: <path d="M74 58 Q62 36 72 20 Q78 38 88 48 M126 58 Q138 36 128 20 Q122 38 112 48" stroke="#2A1A1A" strokeWidth="7" fill="none" strokeLinecap="round" />,
    under: <g stroke="#E2862A" strokeWidth="2" fill="none">{[[70, 140, 82, 160], [130, 140, 118, 166], [100, 150, 104, 176]].map(([a, b, c, d]) => <path key={a} d={`M${a} ${b} L${c} ${d}`} />)}</g>,
    face: <path d="M86 118 Q100 128 114 118" stroke="#E2622E" strokeWidth="3" fill="none" />,
  },
  // Ciguapa : femme sauvage des Caraïbes, longue chevelure noire, pieds tournés vers l'arrière
  'ẽ': {
    body: '#A86A4A', belly: '#D89A72', head: '#C88A62', eye: '#2A1A10',
    back: <path d="M50 70 Q36 150 56 196 L144 196 Q164 150 150 70 Q100 30 50 70Z" fill="#1F1A1A" />,
    top: <path d="M60 86 Q58 40 100 36 Q142 40 140 86 Q124 64 100 62 Q76 64 60 86Z" fill="#1F1A1A" />,
    face: <path d="M90 118 Q100 124 110 118" stroke="#6A2A2A" strokeWidth="2.5" fill="none" />,
    front: <g fill="#A86A4A">{[78, 122].map((x) => <path key={x} d={`M${x - 10} 196 Q${x} 186 ${x + 10} 196 L${x + 14} 202 H${x - 6}Z`} transform={`scale(-1 1) translate(${-2 * x} 0)`} />)}</g>,
  },
  // Nahual : sorcier masqué qui se change en jaguar (oreilles et taches de jaguar)
  'ĩ': {
    body: '#C8923A', belly: '#F2D8A0', head: '#D8A24A', eye: '#2A1A10',
    top: <>{ear(70, false, '#C8923A', '#F2D8A0')}{ear(130, true, '#C8923A', '#F2D8A0')}</>,
    under: <g fill="#5A3A1A">{[[72, 140], [92, 156], [116, 146], [132, 164], [84, 176]].map(([x, y]) => <circle key={`${x}${y}`} cx={x} cy={y} r="4.5" />)}</g>,
    face: <><rect x="70" y="86" width="60" height="16" rx="6" fill="#3A8A7A" /><path d="M94 114 L100 120 L106 114Z" fill="#3A2A1A" /></>,
  },
  // Sombrerón : petit homme au chapeau immense et à la guitare
  'õ': {
    body: '#2A2A3A', belly: '#4A4A5E', head: '#C9A27A', eye: '#2A1A10',
    top: <><ellipse cx="100" cy="56" rx="78" ry="14" fill="#1F1F2A" /><path d="M66 56 Q68 14 100 12 Q132 14 134 56Z" fill="#1F1F2A" /><rect x="66" y="44" width="68" height="6" fill="#C8323F" /></>,
    face: <path d="M88 116 Q100 126 112 116 M86 108 Q100 112 114 108" stroke="#2A1A10" strokeWidth="2.5" fill="none" />,
    front: <g transform="translate(160 150) rotate(-30)"><ellipse cx="0" cy="8" rx="12" ry="14" fill="#C8823A" /><circle cx="0" cy="8" r="4" fill="#3A2A1A" /><rect x="-2" y="-30" width="4" height="26" fill="#7A4A2A" /></g>,
  },
  // Mohán : vieux sorcier du fleuve, longue barbe, pipe fumante
  'ũ': {
    body: '#3A5A4A', belly: '#6A8A6A', head: '#C9A27A', eye: '#2A1A10',
    top: <path d="M62 86 Q60 46 100 42 Q140 46 138 86 Q130 66 100 64 Q70 66 62 86Z" fill="#E8E8E8" />,
    under: <path d="M68 108 Q100 196 132 108 Q118 130 100 130 Q82 130 68 108Z" fill="#E8E8E8" />,
    front: <g transform="translate(124 120)"><path d="M0 0 L22 6" stroke="#5A3A24" strokeWidth="3" /><rect x="20" y="0" width="8" height="10" rx="2" fill="#5A3A24" /><g fill="#B8B8C0" opacity="0.8"><circle cx="26" cy="-6" r="4" /><circle cx="30" cy="-14" r="5" /></g></g>,
  },
  // Muki : gnome des mines andines, casque d'or, lampe
  'Ã': {
    body: '#8A5A3A', belly: '#C89A6A', head: '#D9A07A', eye: '#2A1A10',
    top: <><path d="M62 70 Q62 30 100 28 Q138 30 138 70Z" fill="#E2B84A" stroke="#9A7A2A" strokeWidth="2" /><circle cx="100" cy="44" r="7" fill="#FFF6C8" stroke="#9A7A2A" strokeWidth="1.5" /></>,
    under: <path d="M72 110 Q100 160 128 110 Q114 126 100 126 Q86 126 72 110Z" fill="#E8E8E8" />,
    front: <g transform="translate(160 150)"><path d="M-6 0 L6 -18 L12 -14" stroke="#7A7A7A" strokeWidth="4" fill="none" /><path d="M8 -20 L22 -12 L14 -8Z" fill="#9A9A9A" /></g>,
  },
  // Caleuche : navire fantôme vivant, coque sombre, voiles lumineuses
  'Õ': {
    body: '#2A3A4A', belly: '#4A5A6A', head: '#3A4A5A', eye: '#F2F6FF',
    back: <g><path d="M100 14 V60 M36 30 V130 M164 30 V130" stroke="#1F2A3A" strokeWidth="4" /><path d="M36 34 L6 118 H36Z M164 34 L194 118 H164Z M100 16 L76 52 H100Z" fill="#D8E4F8" stroke="#7A8AA8" strokeWidth="2" /></g>,
    under: <g fill="#F2D94E">{[64, 84, 104, 124, 144].map((x) => <circle key={x} cx={x} cy={170} r="4" />)}</g>,
    face: <path d="M88 118 Q100 112 112 118" stroke="#E8F0FF" strokeWidth="2.5" fill="none" />,
  },
  // Pombero : petit homme velu des forêts, chapeau de paille, oiseaux autour
  'ỹ': {
    body: '#5A3A2A', belly: '#8A6A4A', head: '#7A5A3A', eye: '#F2D94E',
    top: <><ellipse cx="100" cy="54" rx="56" ry="10" fill="#E2C87A" /><path d="M72 54 Q74 30 100 28 Q126 30 128 54Z" fill="#E2C87A" /></>,
    under: <path d="M70 106 Q100 150 130 106 Q116 122 100 122 Q84 122 70 106Z" fill="#4A2A1A" />,
    front: <g>{[[36, 70, '#E2622E'], [168, 84, '#3A8AE2'], [40, 140, '#E2B84A']].map(([x, y, c]) => <g key={String(x)} transform={`translate(${x} ${y})`}><ellipse rx="9" ry="6" fill={String(c)} /><path d="M7 -2 L13 0 L7 2Z" fill="#E2B84A" /><circle cx="3" cy="-2" r="1.4" fill="#1F2433" /></g>)}</g>,
  },
  // ───── Gardiens de la Bibliothèque enchantée (DELE C1 — personnages des classiques espagnols ; signes typographiques) ─────
  // Lion du Cid : crinière fauve, couronne
  '§': {
    body: '#C8923A', belly: '#F2D8A0', head: '#D8A24A', eye: '#2A1A10',
    back: <g fill="#A8622A">{Array.from({ length: 12 }, (_, i) => i * 30).map((a) => <ellipse key={a} cx="100" cy="46" rx="14" ry="26" transform={`rotate(${a} 100 96)`} />)}</g>,
    top: <path d="M80 50 L86 34 L94 46 L100 30 L106 46 L114 34 L120 50Z" fill="#E2B84A" stroke="#9A7A2A" strokeWidth="1.5" />,
    face: <><ellipse cx="100" cy="112" rx="14" ry="10" fill="#F2D8A0" /><path d="M94 106 L100 112 L106 106Z" fill="#5A3A24" /><path d="M100 112 V118 M92 120 Q100 124 108 120" stroke="#5A3A24" strokeWidth="2" fill="none" /></>,
  },
  // Célestine : vieille entremetteuse, mante noire, quenouille et fil rouge
  '¶': {
    body: '#3A2A3A', belly: '#5A4A5A', head: '#D8B898', eye: '#2A1A10',
    top: <path d="M56 92 Q52 40 100 34 Q148 40 144 92 Q132 66 100 62 Q68 66 56 92Z" fill="#2A1F2A" />,
    face: <><path d="M88 120 Q100 114 112 120" stroke="#6A3A2A" strokeWidth="2.5" fill="none" /><path d="M80 98 Q86 94 92 98 M108 98 Q114 94 120 98" stroke="#8A6A5A" strokeWidth="1.2" fill="none" /></>,
    front: <g transform="translate(160 140)"><path d="M0 -40 V40" stroke="#7A4A2A" strokeWidth="4" /><ellipse cx="0" cy="-30" rx="8" ry="12" fill="#E8DCC0" /><path d="M0 -20 Q-30 0 -60 10" stroke="#C8323F" strokeWidth="2" fill="none" /></g>,
  },
  // Aveugle du Lazarillo : yeux clos, bâton, cruche de vin
  '†': {
    body: '#6A5A4A', belly: '#9A8A6A', head: '#C9A27A', eye: '#C9A27A',
    top: <path d="M62 70 Q66 40 100 38 Q134 40 138 70 Q120 58 100 58 Q80 58 62 70Z" fill="#4A3A2A" />,
    under: <path d="M78 96 Q88 92 96 96 M104 96 Q112 92 122 96" stroke="#3A2A1A" strokeWidth="3" fill="none" strokeLinecap="round" />,
    front: <><path d="M40 196 L56 80" stroke="#8A6A3A" strokeWidth="5" strokeLinecap="round" /><g transform="translate(160 156)"><path d="M-10 -14 Q-12 6 0 10 Q12 6 10 -14Z" fill="#B8562E" /><rect x="-4" y="-20" width="8" height="7" fill="#9A4A2A" /></g></>,
  },
  // Segismundo : prince sauvage vêtu de peaux, chaînes aux poignets
  '‡': {
    body: '#8A6A4A', belly: '#B89A6A', head: '#D9A07A', eye: '#2A1A10',
    top: <path d="M58 86 Q54 34 100 30 Q146 34 142 86 Q134 56 120 60 Q110 44 100 54 Q90 44 80 60 Q66 56 58 86Z" fill="#3A2A1A" />,
    under: <path d="M66 140 Q100 170 134 140 L140 160 Q100 186 60 160Z" fill="#6A4A2A" />,
    front: <g fill="none" stroke="#6A6A6A" strokeWidth="3">{[[44, 150], [56, 160], [68, 168]].map(([x, y]) => <ellipse key={x} cx={x} cy={y} rx="6" ry="4" />)}{[[156, 150], [144, 160], [132, 168]].map(([x, y]) => <ellipse key={x} cx={x} cy={y} rx="6" ry="4" />)}</g>,
  },
  // Licencié de verre : corps translucide, reflets
  '°': {
    body: '#BFE0F0', belly: '#E8F6FC', head: '#CFE8F4', eye: '#2A4A6A',
    top: <path d="M70 60 Q74 40 100 38 Q126 40 130 60" stroke="#7AA8C8" strokeWidth="3" fill="none" />,
    under: <g stroke="#FFFFFF" strokeWidth="4" strokeLinecap="round" fill="none"><path d="M70 130 Q74 120 80 116" /><path d="M120 76 Q126 72 130 74" /></g>,
    face: <path d="M90 118 Q100 124 110 118" stroke="#2A4A6A" strokeWidth="2.5" fill="none" />,
  },
  // Commandeur : statue de pierre en armure, épée
  '¤': {
    body: '#9A9A96', belly: '#B8B8B4', head: '#A8A8A4', eye: '#F2F2EE',
    top: <><path d="M64 80 Q62 36 100 34 Q138 36 136 80Z" fill="#8A8A86" /><path d="M100 34 V20 M94 24 H106" stroke="#7A7A76" strokeWidth="4" /></>,
    under: <path d="M70 140 H130 M100 126 V160" stroke="#7A7A76" strokeWidth="3" />,
    front: <path d="M162 190 L170 80 M160 100 H180" stroke="#7A7A76" strokeWidth="5" strokeLinecap="round" />,
  },
  // Dame aux yeux verts : chevelure d'eau, yeux d'émeraude
  '‰': {
    body: '#5A9AA8', belly: '#BFE0E8', head: '#E8D0C0', eye: '#2EA86A',
    back: <path d="M48 70 Q30 150 50 196 Q70 180 80 196 Q90 180 100 196 Q110 180 120 196 Q130 180 150 196 Q170 150 152 70 Q100 30 48 70Z" fill="#3A7A8A" opacity="0.85" />,
    top: <path d="M60 86 Q58 40 100 36 Q142 40 140 86 Q124 64 100 62 Q76 64 60 86Z" fill="#3A7A8A" />,
    face: <path d="M92 118 Q100 122 108 118" stroke="#8A4A5A" strokeWidth="2.5" fill="none" />,
    front: <g fill="#7AC8E2">{[[40, 120], [164, 132], [52, 160]].map(([x, y]) => <path key={x} d={`M${x} ${y - 8} Q${x + 4} ${y - 2} ${x} ${y} Q${x - 4} ${y - 2} ${x} ${y - 8}Z`} />)}</g>,
  },
  // Spectre de Salamanque : dame voilée de blanc, visage pâle
  '¬': {
    body: '#E8E8F0', belly: '#F6F6FA', head: '#DADAE6', eye: '#3A3A4A',
    back: <path d="M44 196 Q40 110 60 70 Q100 20 140 70 Q160 110 156 196 Q140 184 128 196 Q114 184 100 196 Q86 184 72 196 Q58 184 44 196Z" fill="#F2F2F8" stroke="#C8C8D8" strokeWidth="2" />,
    top: <path d="M58 90 Q56 40 100 34 Q144 40 142 90 Q130 70 100 68 Q70 70 58 90Z" fill="#F6F6FA" stroke="#C8C8D8" strokeWidth="2" />,
    face: <path d="M92 120 Q100 116 108 120" stroke="#5A5A6A" strokeWidth="2" fill="none" />,
  },
  // ───── Gardiens du Rayon secret (DELE C2 — personnages des classiques d'Espagne et d'Amérique ; fleurons typographiques) ─────
  // Dixième Muse (Sor Juana) : habit blanc, voile noir, grand médaillon sur la poitrine
  '❦': {
    body: '#F2EEE6', belly: '#E6DFD2', head: '#E8C8A8', eye: '#2A1A10',
    back: <path d="M52 92 Q44 150 54 196 H146 Q156 150 148 92 Q100 64 52 92Z" fill="#1F1A22" />,
    top: <><path d="M56 96 Q52 38 100 32 Q148 38 144 96 Q138 70 100 64 Q62 70 56 96Z" fill="#1F1A22" /><path d="M66 92 Q66 60 100 56 Q134 60 134 92 Q120 78 100 76 Q80 78 66 92Z" fill="#FFFFFF" /></>,
    face: <path d="M92 120 Q100 124 108 120" stroke="#8A4A3A" strokeWidth="2" fill="none" />,
    front: <><circle cx="100" cy="152" r="17" fill="#E2B84A" stroke="#9A7A2A" strokeWidth="2" /><circle cx="100" cy="152" r="12" fill="#7A9AC8" /><path d="M160 190 L176 120 Q180 112 178 124 L166 190Z" fill="#FFFFFF" stroke="#B9AE98" strokeWidth="1" /></>,
  },
  // Cygne de Darío : plumes blanches, grandes ailes, bec orange, aigrette bleue (Azul…)
  '❧': {
    body: '#FAFAF6', belly: '#FFFFFF', head: '#F6F6F2', eye: '#1A1A22',
    back: <g fill="#ECECE6" stroke="#C8C8C0" strokeWidth="1.5"><path d="M60 120 Q14 96 20 60 Q50 80 70 108Z" /><path d="M140 120 Q186 96 180 60 Q150 80 130 108Z" /></g>,
    top: <path d="M92 44 Q100 22 108 44 Q100 36 92 44Z" fill="#3A6AB8" />,
    face: <path d="M90 112 L100 128 L110 112Z" fill="#E2902A" stroke="#A85A1A" strokeWidth="1.2" />,
  },
  // Souris de fray Martín : pelage gris, grandes oreilles roses, moustaches, longue queue
  '☙': {
    body: '#9A9AA4', belly: '#C8C8D0', head: '#A8A8B2', eye: '#1A1A22',
    back: <path d="M150 170 Q186 168 182 132 Q178 108 192 96" stroke="#C88A9A" strokeWidth="4" fill="none" strokeLinecap="round" />,
    top: <g><circle cx="66" cy="58" r="22" fill="#A8A8B2" /><circle cx="66" cy="58" r="14" fill="#E8B0BA" /><circle cx="134" cy="58" r="22" fill="#A8A8B2" /><circle cx="134" cy="58" r="14" fill="#E8B0BA" /></g>,
    face: <><circle cx="100" cy="114" r="5" fill="#E88A9A" /><path d="M94 116 L66 110 M94 118 L66 122 M106 116 L134 110 M106 118 L134 122" stroke="#5A5A62" strokeWidth="1.2" /></>,
  },
  // Miroir déformant : cadre doré, reflet argenté ondulé
  '⁂': {
    body: '#C8D4DE', belly: '#E4ECF2', head: '#D2DCE4', eye: '#3A2A4A',
    back: <rect x="34" y="28" width="132" height="168" rx="40" fill="#8A5A2A" stroke="#E2B84A" strokeWidth="4" />,
    top: <path d="M70 50 Q100 24 130 50 Q118 40 100 40 Q82 40 70 50Z" fill="#E2B84A" />,
    under: <g stroke="#FFFFFF" strokeWidth="3" fill="none" opacity="0.8"><path d="M64 140 Q82 128 100 140 T136 140" /><path d="M70 160 Q86 150 100 160 T130 160" /></g>,
    face: <path d="M86 118 Q94 128 100 116 Q106 128 114 118" stroke="#6A3A5A" strokeWidth="2.5" fill="none" />,
  },
  // Martín Fierro : chapeau de gaucho, moustache, poncho, guitare
  '✦': {
    body: '#8A3A2A', belly: '#B8562E', head: '#C99A70', eye: '#2A1A10',
    top: <><ellipse cx="100" cy="64" rx="56" ry="10" fill="#2A2420" /><path d="M72 62 Q74 36 100 34 Q126 36 128 62Z" fill="#2A2420" /></>,
    under: <path d="M56 136 L100 180 L144 136 L150 150 L100 196 L50 150Z" fill="#E2B84A" opacity="0.9" />,
    face: <path d="M84 116 Q92 110 100 116 Q108 110 116 116 Q108 122 100 118 Q92 122 84 116Z" fill="#3A2A1A" />,
    front: <g transform="translate(160 150) rotate(-25)"><circle cx="0" cy="10" r="13" fill="#C8823A" /><circle cx="0" cy="-6" r="10" fill="#C8823A" /><circle cx="0" cy="2" r="3.5" fill="#3A2414" /><rect x="-2.5" y="-48" width="5" height="40" fill="#7A4A2A" /></g>,
  },
  // Tortue géante de Quiroga : carapace à écailles, lianes, regard patient
  '✿': {
    body: '#6A7A3A', belly: '#C8C08A', head: '#8A9A5A', eye: '#2A2A1A',
    back: <g><path d="M30 170 Q24 76 100 70 Q176 76 170 170Z" fill="#5A6A2A" stroke="#3A4A1A" strokeWidth="3" />{[[70, 120], [100, 104], [130, 120], [84, 150], [116, 150]].map(([x, y]) => <path key={`${x}-${y}`} d={`M${x} ${y - 14} L${x + 12} ${y - 6} L${x + 12} ${y + 8} L${x} ${y + 14} L${x - 12} ${y + 8} L${x - 12} ${y - 6}Z`} fill="#7A8A3A" stroke="#3A4A1A" strokeWidth="2" />)}</g>,
    top: <path d="M60 60 Q80 40 100 52 Q120 40 140 56" stroke="#2E7A3A" strokeWidth="4" fill="none" strokeLinecap="round" />,
    face: <path d="M90 120 Q100 126 110 120" stroke="#3A4A1A" strokeWidth="2.5" fill="none" />,
  },
  // Augusto dans le brouillard : chapeau melon, parapluie, volutes de brume
  '◊': {
    body: '#5A6470', belly: '#8A949E', head: '#D8C0A8', eye: '#2A2A3A',
    back: <g stroke="#DCE2E8" strokeWidth="8" fill="none" strokeLinecap="round" opacity="0.7"><path d="M20 120 Q50 108 80 120" /><path d="M120 176 Q150 164 184 176" /><path d="M14 176 Q40 166 64 176" /></g>,
    top: <><ellipse cx="100" cy="62" rx="40" ry="7" fill="#1F2228" /><path d="M76 60 Q76 32 100 32 Q124 32 124 60Z" fill="#1F2228" /></>,
    face: <path d="M92 120 L108 120" stroke="#6A4A3A" strokeWidth="2.5" strokeLinecap="round" />,
    front: <g transform="translate(164 120)"><path d="M-28 0 Q0 -34 28 0 Q20 -6 14 0 Q7 -6 0 0 Q-7 -6 -14 0 Q-20 -6 -28 0Z" fill="#2A2A32" /><path d="M0 0 V54 Q0 62 -8 60" stroke="#3A2A1A" strokeWidth="3" fill="none" /></g>,
  },
  // Manuscrit de Benengeli : parchemin, turban, lignes d'écriture arabe, calame
  '✧': {
    body: '#E6D4A8', belly: '#F2E6C6', head: '#C9A27A', eye: '#2A1A10',
    top: <path d="M58 82 Q54 40 100 36 Q146 40 142 82 Q128 70 100 70 Q72 70 58 82Z M100 36 Q112 46 100 58 Q88 46 100 36Z" fill="#F6F1E6" stroke="#B89A6A" strokeWidth="2" />,
    under: <g stroke="#5A3A2A" strokeWidth="2" fill="none">{[138, 152, 166].map((y) => <path key={y} d={`M128 ${y} Q120 ${y - 4} 112 ${y} T96 ${y} T80 ${y} T70 ${y}`} />)}</g>,
    face: <path d="M90 120 Q100 126 110 120" stroke="#6A3A2A" strokeWidth="2" fill="none" />,
    front: <path d="M168 186 L178 110 L182 112 L172 186Z" fill="#7A4A2A" />,
  },
  // ───── Gardiens anglais (C1 — îles du Nord) ─────
  // Nuckelavee : démon marin sans peau, rouge vif, veines jaunes, un seul œil
  n: {
    body: '#B8322E', belly: '#E26A5A', head: '#C8423A', eye: '#F2D94E',
    back: <path d="M40 120 Q10 160 30 196 M160 120 Q190 160 170 196" stroke="#8E1B26" strokeWidth="12" fill="none" strokeLinecap="round" />,
    under: <path d="M70 140 Q80 120 90 140 M110 140 Q120 120 130 140 M84 170 Q100 150 116 170" stroke="#F2D94E" strokeWidth="2" fill="none" />,
    face: <path d="M84 116 Q100 126 116 116" stroke="#5A1A10" strokeWidth="3" fill="none" />,
    front: <path d="M20 190 Q40 180 60 190 T100 190 T140 190 T180 190" stroke="#5E8FA0" strokeWidth="4" fill="none" strokeLinecap="round" />,
  },
  // Hommes bleus du Minch : peau bleue, cheveux d'écume, vagues
  p: {
    body: '#2E5A9A', belly: '#6A9AD8', head: '#4A7AC0', eye: '#F4F1EA',
    top: <path d="M58 72 q4 -28 18 -30 q6 -14 16 -6 q10 -14 20 0 q14 -8 16 8 q14 4 14 28" fill="#E8F2F8" />,
    face: <path d="M82 114 Q100 128 118 114" stroke="#0E2A5A" strokeWidth="3" fill="none" />,
    front: <path d="M14 182 Q34 166 54 182 T94 182 T134 182 T174 182 T194 182" stroke="#E8F2F8" strokeWidth="5" fill="none" strokeLinecap="round" />,
  },
  // Wulver : homme à tête de loup, pelage brun, poisson
  g: {
    body: '#6A5A4A', belly: '#B8A890', head: '#7A6A58', eye: '#F2D94E',
    top: <>{ear(58, false, '#5A4A3A', '#B8A890')}{ear(142, true, '#5A4A3A', '#B8A890')}</>,
    face: <><ellipse cx="100" cy="114" rx="16" ry="10" fill="#9A8A74" /><ellipse cx="100" cy="108" rx="5" ry="3.5" fill={INK} /></>,
    front: <g transform="translate(152 158)"><path d="M-18 0 Q-6 -10 10 0 Q-6 10 -18 0Z" fill="#9AB8C8" /><path d="M10 0 L20 -8 L20 8Z" fill="#9AB8C8" /></g>,
  },
  // Gwrach y Rhibyn : sorcière galloise aux ailes de cuir
  r: {
    body: '#4A4458', belly: '#8A84A0', head: '#B8B0A8', eye: '#E2483B',
    back: <><path d="M58 110 Q6 80 18 160 Q28 130 44 150 Q50 128 62 146Z" fill="#2A2434" /><path d="M142 110 Q194 80 182 160 Q172 130 156 150 Q150 128 138 146Z" fill="#2A2434" /></>,
    top: <path d="M56 82 Q52 32 100 28 Q148 32 144 82 Q140 54 100 52 Q60 54 56 82Z" fill="#D8D4CC" />,
    face: <path d="M86 116 l5 4 l5 -4 l5 4 l5 -4 l5 4" stroke={INK} strokeWidth="2.5" fill="none" />,
  },
  // Cailleach : vieille déesse de l'hiver, voile bleu, marteau
  c: {
    body: '#3E5A7A', belly: '#9AB8D8', head: '#D8D0C8', eye: '#2A3A5A',
    top: <path d="M54 90 Q52 26 100 22 Q148 26 146 90 Q140 50 100 48 Q60 50 54 90Z" fill="#DDEFF5" stroke="#9CC6D1" strokeWidth="2" />,
    face: <path d="M86 118 Q100 112 114 118" stroke={INK} strokeWidth="2.5" fill="none" />,
    front: <g transform="translate(160 146)"><path d="M0 44 V-30" stroke="#6A4428" strokeWidth="5" /><rect x="-14" y="-44" width="28" height="16" rx="3" fill="#8A8E96" /></g>,
  },
  // Hob : petit esprit domestique poilu, jatte de crème
  e: {
    body: '#8A6A48', belly: '#C8A87A', head: '#9A7A56', eye: INK,
    top: <path d="M60 74 q-4 -20 10 -26 q4 -14 16 -8 q10 -12 22 0 q12 -6 18 8 q14 6 10 26" fill="#6A4E34" />,
    face: <><ellipse cx="100" cy="110" rx="6" ry="4" fill="#C87A5A" /><path d="M88 120 Q100 128 112 120" stroke={INK} strokeWidth="2.5" fill="none" /></>,
    front: <g transform="translate(100 176)"><path d="M-22 -6 H22 Q20 10 0 12 Q-20 10 -22 -6Z" fill="#E8D8B8" stroke="#A8987A" strokeWidth="2" /><ellipse cx="0" cy="-6" rx="22" ry="5" fill="#FBF8F1" /></g>,
  },
  // Morgawr : serpent de mer de Cornouailles, bosses, long cou
  s: {
    body: '#3E6A5E', belly: '#8FBFA8', head: '#4E7F70', eye: '#F2D94E',
    back: <>{[[28, 176], [172, 176]].map(([cx, cy]) => <path key={cx} d={`M${cx - 18} ${cy} Q${cx} ${cy - 30} ${cx + 18} ${cy}`} fill="#3E6A5E" />)}</>,
    top: <path d="M80 50 l6 -10 l6 8 l8 -12 l8 12 l6 -8 l6 10" stroke="#2E5A4E" strokeWidth="4" fill="none" />,
    front: <path d="M10 190 Q30 180 50 190 T90 190 T130 190 T170 190 T200 190" stroke="#5E9FC4" strokeWidth="4" fill="none" strokeLinecap="round" />,
  },
  // La Dame du Lac : robe d'eau, Excalibur
  a: {
    body: '#4A7AA8', belly: '#A8CCE8', head: '#EAD8C8', eye: '#2E4A6A',
    top: <path d="M56 86 Q54 26 100 22 Q146 26 144 86 Q138 50 100 48 Q62 50 56 86Z" fill="#3A2E28" />,
    back: <path d="M50 100 Q24 160 40 196 L160 196 Q176 160 150 100Z" fill="#7FB8D8" opacity={0.7} />,
    front: <g transform="translate(160 150)"><path d="M0 40 V-46" stroke="#D8E0E8" strokeWidth="5" /><path d="M-10 26 H10" stroke="#C9A24A" strokeWidth="5" /><circle cy="34" r="3" fill="#C9A24A" /></g>,
  },
  // ───── Gardiens anglais (B2 — Marches galloises) ─────
  // Barghest : chien-gobelin noir aux yeux de braise
  b: {
    body: '#1A1A20', belly: '#2E2E36', head: '#22222A', eye: '#F2482B',
    top: <path d="M58 70 Q44 40 62 30 Q70 50 80 58 M142 70 Q156 40 138 30 Q130 50 120 58" fill="#1A1A20" stroke="#1A1A20" strokeWidth="4" />,
    face: <><ellipse cx="100" cy="112" rx="14" ry="8" fill="#0E0E12" /><path d="M90 122 l4 6 l4 -6 M102 122 l4 6 l4 -6" stroke="#F6F3EC" strokeWidth="2" fill="none" /></>,
    back: <path d="M30 170 Q60 150 50 190 M170 170 Q140 150 150 190" stroke="#4A4A58" strokeWidth="6" fill="none" opacity={0.6} strokeLinecap="round" />,
  },
  // Spring-heeled Jack : cape noire, haut-de-forme, bottes à ressorts
  Z: {
    body: '#22222E', belly: '#4A4A5E', head: '#D8D0C0', eye: '#E2483B',
    top: <><rect x="72" y="16" width="56" height="34" fill="#1A1A20" /><rect x="60" y="48" width="80" height="8" rx="2" fill="#1A1A20" /></>,
    back: <path d="M54 80 Q20 150 34 196 L166 196 Q180 150 146 80Z" fill="#5A1A22" />,
    front: <>{[70, 130].map((x) => <path key={x} d={`M${x - 8} 186 l16 -6 l-16 -6 l16 -6`} stroke="#9AA0A8" strokeWidth="3" fill="none" />)}</>,
  },
  // Grindylow : démon aquatique vert, longs bras, nénuphars
  I: {
    body: '#3E6E52', belly: '#7FAF8E', head: '#4E8A62', eye: '#F2D94E',
    back: <path d="M50 110 Q10 150 30 190 M150 110 Q190 150 170 190" stroke="#2E5A40" strokeWidth="10" fill="none" strokeLinecap="round" />,
    top: <path d="M70 52 l6 -14 l6 12 l8 -16 l8 16 l8 -16 l8 16 l6 -12 l6 14" stroke="#2E5A40" strokeWidth="4" fill="none" />,
    face: <path d="M84 114 l6 8 l6 -8 l6 8 l6 -8 l6 8" stroke="#F6F3EC" strokeWidth="2.5" fill="none" />,
    front: <>{[[46, 190], [154, 192]].map(([cx, cy]) => <g key={cx}><ellipse cx={cx} cy={cy} rx="14" ry="5" fill="#6DA84E" /><circle cx={cx} cy={cy - 4} r="4" fill="#F2A7BB" /></g>)}</>,
  },
  // Coblynau : petits lutins des mines, hirsutes, outil cassé
  h: {
    body: '#6A5A48', belly: '#A8987A', head: '#7A6A56', eye: '#F2D94E',
    top: <path d="M58 70 q-6 -24 12 -30 q2 -16 18 -12 q8 -16 24 -4 q16 -10 22 8 q16 4 10 30" fill="#4A3E30" />,
    face: <path d="M84 116 Q100 104 116 116" stroke={INK} strokeWidth="3" fill="none" strokeLinecap="round" />,
    front: <g transform="translate(150 166) rotate(20)"><path d="M-12 -12 H12 V12 H-12Z" fill="#C9C4BA" stroke="#8A8478" strokeWidth="2" /><path d="M-12 -12 L4 2 L-2 12" stroke="#5A564C" strokeWidth="2" fill="none" /></g>,
  },
  // Selkie : mi-femme mi-phoque, peau de phoque grise, vagues
  f: {
    body: '#7A8A96', belly: '#C9D4DC', head: '#E8D2BE', eye: '#3A5A7A',
    top: <path d="M56 84 Q56 26 100 24 Q144 26 144 84 Q140 50 100 46 Q60 50 56 84Z" fill="#2E3A4A" />,
    back: <path d="M48 96 Q20 160 52 194 L148 194 Q180 160 152 96Z" fill="#5A6A78" />,
    front: <path d="M30 186 Q46 176 62 186 T94 186 T126 186 T158 186" stroke="#7FC4D9" strokeWidth="4" fill="none" strokeLinecap="round" />,
  },
  // Bean Nighe : lavandière des Highlands, linge blanc, eau du gué
  m: {
    body: '#3E5A4A', belly: '#7F9A88', head: '#D8C8B0', eye: '#2A3A30',
    top: <path d="M58 80 Q58 30 100 26 Q142 30 142 80 Q130 60 100 58 Q70 60 58 80Z" fill="#7A7A7A" />,
    face: <path d="M88 116 H112" stroke={INK} strokeWidth="2.5" strokeLinecap="round" />,
    front: <g transform="translate(100 176)"><path d="M-30 0 Q-10 -12 10 0 Q24 8 30 0" fill="#F4F1EA" stroke="#C9C4BA" strokeWidth="2" /><path d="M-44 12 Q-20 4 0 12 T44 12" stroke="#7FC4D9" strokeWidth="3" fill="none" /></g>,
  },
  // Gwyn ap Nudd : roi de l'Autre Monde, bois de cerf, cor de chasse
  d: {
    body: '#2E3A5A', belly: '#6A7AA0', head: '#D8D0E0', eye: '#7FD9E2',
    top: <path d="M74 52 L66 24 L58 30 M66 24 L70 12 M126 52 L134 24 L142 30 M134 24 L130 12" stroke="#C9B89A" strokeWidth="5" fill="none" strokeLinecap="round" />,
    back: <path d="M54 96 Q18 150 36 194 L164 194 Q182 150 146 96Z" fill="#1E2640" />,
    front: <g transform="translate(152 150)"><path d="M-14 -10 Q10 -16 16 6 L8 10 Q4 -4 -12 -2Z" fill="#E2D2A8" stroke="#A8987A" strokeWidth="2" /></g>,
  },
  // Mordred : chevalier félon, armure noire, couronne volée, épée
  k: {
    body: '#2A2A34', belly: '#5A5A6A', head: '#D8C8B8', eye: '#5A1A22',
    top: <><path d="M60 78 Q58 30 100 26 Q142 30 140 78 Q124 56 100 56 Q76 56 60 78Z" fill="#3A2A20" /><path d="M72 36 L78 20 L88 32 L100 16 L112 32 L122 20 L128 36Z" fill="#C9A24A" stroke="#8C6A2A" strokeWidth="2" /></>,
    face: <path d="M86 118 Q100 112 114 118" stroke="#5A1A22" strokeWidth="3" fill="none" strokeLinecap="round" />,
    back: <path d="M52 92 Q22 150 36 196 L164 196 Q178 150 148 92Z" fill="#5A1A22" />,
    front: <g transform="translate(158 144)"><path d="M0 44 V-40" stroke="#A8B4C0" strokeWidth="5" /><path d="M-10 30 H10" stroke="#2A2A34" strokeWidth="5" /></g>,
  },
  // ───── Gardiens anglais (B1 — côtes de Cornouailles) ─────
  // L'Afanc : monstre du lac, castor-crocodile écailleux, vagues
  A: {
    body: '#3E6A6E', belly: '#8FBFB8', head: '#5E8F88', eye: '#F2D94E',
    back: <path d="M52 150 Q10 170 30 196 Q60 188 70 170Z" fill="#2E4F52" />,
    top: <path d="M66 60 l8 -16 l8 14 l8 -16 l8 14 l8 -16 l8 14 l8 -16 l6 18" stroke="#2E4F52" strokeWidth="5" fill="none" strokeLinejoin="round" />,
    face: <path d="M84 114 l6 6 l6 -6 l6 6 l6 -6 l6 6" stroke="#F6F3EC" strokeWidth="3" fill="none" />,
    front: <path d="M20 186 Q40 174 60 186 T100 186 T140 186 T180 186" stroke="#7FC4D9" strokeWidth="5" fill="none" strokeLinecap="round" />,
  },
  // Cait Sìth : grand chat noir à tache blanche sur la poitrine
  C: {
    body: '#1E1E26', belly: '#F4F1EA', head: '#26262F', eye: '#7FD957',
    top: <>{ear(58, false, '#26262F', '#5A4A5A')}{ear(142, true, '#26262F', '#5A4A5A')}</>,
    face: <><path d="M94 104 L106 104 L100 110Z" fill="#E28A9A" /><path d="M70 108 H50 M70 114 H52 M130 108 H150 M130 114 H148" stroke="#C9C4BA" strokeWidth="2" /></>,
    back: <path d="M150 170 Q196 150 180 100" stroke="#1E1E26" strokeWidth="12" fill="none" strokeLinecap="round" />,
  },
  // Le ver de Lambton : serpent géant enroulé, écailles, puits
  L: {
    body: '#6A7A3A', belly: '#C9C98A', head: '#7F8F48', eye: '#E2483B',
    back: <><path d="M30 160 Q20 110 60 104 M170 160 Q180 110 140 104" stroke="#55652E" strokeWidth="22" fill="none" strokeLinecap="round" /></>,
    face: <path d="M96 116 v12 l-5 6 M104 116 v12 l5 6" stroke="#C8323F" strokeWidth="3" fill="none" strokeLinecap="round" />,
    front: <g transform="translate(100 182)"><rect x="-26" y="-8" width="52" height="16" rx="3" fill="#8A8478" stroke="#5A564C" strokeWidth="2" /><path d="M-26 0 H26 M-10 -8 V8 M10 -8 V8" stroke="#5A564C" strokeWidth="2" /></g>,
  },
  // Tom Tit Tot : petit diable noir à longue queue, rouet
  T: {
    body: '#2A2228', belly: '#6A5A60', head: '#3A2E34', eye: '#F2A23B',
    top: <path d="M66 58 Q60 34 74 26 Q72 44 80 52 M134 58 Q140 34 126 26 Q128 44 120 52" stroke="#1A1418" strokeWidth="7" fill="none" strokeLinecap="round" />,
    face: <path d="M82 112 Q100 126 118 112" stroke="#F2A23B" strokeWidth="3" fill="none" strokeLinecap="round" />,
    back: <path d="M140 170 Q190 170 178 120 l8 -6 l-14 0Z" stroke="#1A1418" strokeWidth="5" fill="#1A1418" />,
    front: <g transform="translate(152 158)"><circle r="18" fill="none" stroke="#8C6A2A" strokeWidth="4" />{[0, 60, 120].map((a) => <path key={a} d="M-18 0 H18" stroke="#8C6A2A" strokeWidth="2" transform={`rotate(${a})`} />)}</g>,
  },
  // La Licorne d'Écosse : blanche, corne dorée, crinière, chaîne d'or
  U: {
    body: '#F4F1EA', belly: '#FFFFFF', head: '#FBF8F1', eye: '#3A4E8F',
    top: <><path d="M92 46 L100 6 L108 46Z" fill="#E2B84A" stroke="#B08A2A" strokeWidth="2" /><path d="M58 72 Q50 40 80 36 Q66 56 70 72Z" fill="#B9C9E8" /></>,
    face: <><ellipse cx="92" cy="112" rx="3" ry="2" fill="#B8A8A0" /><ellipse cx="108" cy="112" rx="3" ry="2" fill="#B8A8A0" /></>,
    front: <path d="M56 166 q8 -8 16 0 q8 8 16 0 q8 -8 16 0 q8 8 16 0 q8 -8 16 0" stroke="#E2B84A" strokeWidth="4" fill="none" />,
  },
  // L'Homme-hibou : plumes grises, aigrettes, grands yeux rouges, bec
  O: {
    body: '#7A7468', belly: '#C9C0AE', head: '#8A8478', eye: '#E2483B',
    top: <path d="M62 60 L58 26 L82 50 M138 60 L142 26 L118 50" stroke="#4A463E" strokeWidth="6" fill="#4A463E" strokeLinejoin="round" />,
    under: <><circle cx="80" cy="88" r="15" fill="#F2E9D0" /><circle cx="120" cy="88" r="15" fill="#F2E9D0" /></>,
    face: <path d="M92 102 L108 102 L100 120Z" fill="#2A2A2A" />,
    back: <><path d="M58 110 Q6 90 20 160 Q40 140 62 150Z" fill="#5A564C" /><path d="M142 110 Q194 90 180 160 Q160 140 138 150Z" fill="#5A564C" /></>,
  },
  // Les dragons de Vortigern : rouge et blanc, tour qui tremble
  V: {
    body: '#B8322E', belly: '#F2E9E0', head: '#C84A3E', eye: '#F2D94E',
    back: <><path d="M58 110 Q8 70 24 150 Q42 130 62 146Z" fill="#F4F1EA" stroke="#B9B1A0" strokeWidth="2" /><path d="M142 110 Q192 70 176 150 Q158 130 138 146Z" fill="#8E1B26" /></>,
    top: <path d="M74 52 L68 28 L86 46 M126 52 L132 28 L114 46" stroke="#F2E9E0" strokeWidth="6" fill="none" strokeLinecap="round" />,
    face: <path d="M90 110 Q100 116 110 110 M94 100 h2 M104 100 h2" stroke="#5A1A10" strokeWidth="3" fill="none" />,
    front: <g transform="translate(152 150)"><rect x="-12" y="-26" width="24" height="50" fill="#8A8478" stroke="#5A564C" strokeWidth="2" /><path d="M-12 -26 v-6 h6 v6 h6 v-6 h6 v6 h6 v-6" stroke="#5A564C" strokeWidth="2" fill="#8A8478" /></g>,
  },
  // Y Brenin Llwyd, le roi gris : vieillard de brume, couronne de givre
  Y: {
    body: '#8E96A0', belly: '#C9D0D8', head: '#B9C0C8', eye: '#3A4A5A',
    back: <><circle cx="40" cy="160" r="26" fill="#D8DEE4" opacity={0.8} /><circle cx="164" cy="164" r="30" fill="#D8DEE4" opacity={0.8} /><circle cx="100" cy="190" r="24" fill="#E4E8EC" opacity={0.8} /></>,
    top: <path d="M70 52 L74 30 L86 44 L100 24 L114 44 L126 30 L130 52Z" fill="#DDEFF5" stroke="#9CC6D1" strokeWidth="2" />,
    face: <path d="M74 112 Q100 160 126 112 Q112 124 100 122 Q88 124 74 112Z" fill="#E4E8EC" stroke="#B9C0C8" strokeWidth="2" />,
  },
  // ───── Gardiens anglais (A2 — terres de Logres) ─────
  // Redcap : lutin trapu au bonnet rouge, bottes de fer, pique
  R: {
    body: '#6E6A5E', belly: '#B9B19A', head: '#C9A882', eye: '#E2483B',
    top: <path d="M58 72 Q58 22 104 14 Q112 30 146 40 Q130 46 142 72Z" fill="#C8323F" />,
    face: <path d="M86 116 l6 -6 l6 6 l6 -6 l6 6 l6 -6" stroke="#F6F3EC" strokeWidth="3" fill="none" />,
    front: <g transform="translate(160 150)"><path d="M0 40 V-46" stroke="#6A4428" strokeWidth="5" /><path d="M-6 -46 L0 -64 L6 -46Z" fill="#9AA0A8" /></g>,
  },
  // Jenny Greenteeth : sorcière des étangs, cheveux d'algues, dents vertes, lentilles d'eau
  J: {
    body: '#4E7F5E', belly: '#9CC4A2', head: '#8FB89A', eye: '#F2D94E',
    back: <path d="M48 90 Q30 150 50 186 M152 90 Q170 150 150 186 M60 80 Q44 130 64 176 M140 80 Q156 130 136 176" stroke="#2F6B3E" strokeWidth="8" fill="none" strokeLinecap="round" />,
    top: <path d="M56 80 Q60 30 100 26 Q140 30 144 80 Q130 56 100 54 Q70 56 56 80Z" fill="#2F6B3E" />,
    face: <path d="M84 112 Q100 122 116 112 M88 113 v6 M96 115 v7 M104 115 v7 M112 113 v6" stroke="#3E8E3A" strokeWidth="3" fill="none" />,
    front: <>{[[40, 186], [70, 192], [150, 188], [176, 182]].map(([cx, cy]) => <ellipse key={cx} cx={cx} cy={cy} rx="9" ry="4" fill="#7FB84E" />)}</>,
  },
  // Morgane la fée : couronne, longs cheveux noirs, miroir magique
  M: {
    body: '#5A3E7A', belly: '#B9A2D6', head: '#EAD2C0', eye: '#3E2A5E',
    back: <path d="M54 70 Q30 140 56 180 L144 180 Q170 140 146 70Z" fill="#1F1A2E" />,
    top: <path d="M70 46 L76 26 L88 40 L100 20 L112 40 L124 26 L130 46Z" fill="#E2B84A" stroke="#B08A2A" strokeWidth="2" />,
    front: <g transform="translate(154 146)"><ellipse rx="14" ry="18" fill="#BFD6E8" stroke="#E2B84A" strokeWidth="4" /><path d="M0 18 V36" stroke="#E2B84A" strokeWidth="5" /><path d="M-6 -6 L4 4" stroke="#FFFFFF" strokeWidth="2" /></g>,
  },
  // Bête glatissante : corps tacheté de léopard, tête de serpent, queue de lion
  Q: {
    body: '#D9A23B', belly: '#F2D9A0', head: '#8A9A4A', eye: '#F2D94E',
    back: <path d="M150 150 Q190 150 186 120 Q196 110 188 104 Q182 116 170 126 Q160 136 146 136Z" fill="#B87F2A" />,
    under: <>{[[64, 130], [80, 152], [120, 156], [136, 132], [100, 170]].map(([cx, cy]) => <circle key={cx} cx={cx} cy={cy} r="6" fill="#7A4E1A" />)}</>,
    face: <path d="M100 112 V122 M100 122 l-5 6 M100 122 l5 6" stroke="#C8323F" strokeWidth="2.5" fill="none" />,
  },
  // Kelpie : cheval des eaux, crinière d'algues, gouttes
  H: {
    body: '#D9E4EA', belly: '#F6F8FA', eye: '#1F3A5F',
    top: <><path d="M68 66 L60 34 L84 52Z" fill="#D9E4EA" /><path d="M132 66 L140 34 L116 52Z" fill="#D9E4EA" /><path d="M86 40 Q100 20 116 40 Q124 60 140 70 Q120 66 112 52 Q100 60 86 40Z" fill="#3E7A6A" /></>,
    face: <><ellipse cx="100" cy="112" rx="16" ry="10" fill="#C2D1DA" /><circle cx="94" cy="112" r="2" fill="#5E6E7A" /><circle cx="106" cy="112" r="2" fill="#5E6E7A" /></>,
    front: <>{[[40, 160], [164, 150], [52, 190]].map(([cx, cy]) => <path key={cx} d={`M${cx} ${cy} q-6 8 0 12 q6 -4 0 -12Z`} fill="#7FB4E8" />)}</>,
  },
  // Herne le chasseur : bois de cerf, cape de feuilles, cor de chasse
  E: {
    body: '#6A5A3E', belly: '#A89A78', head: '#C9A882', eye: '#2E3A2A',
    top: <path d="M74 50 L60 20 M66 34 L52 30 M64 26 L70 12 M126 50 L140 20 M134 34 L148 30 M136 26 L130 12" stroke="#8A6A44" strokeWidth="6" fill="none" strokeLinecap="round" />,
    back: <path d="M50 100 Q40 160 60 186 L140 186 Q160 160 150 100Z" fill="#3E6B3A" />,
    front: <g transform="translate(150 150)"><path d="M-16 0 Q0 -18 16 -10 L18 2 Q2 -6 -12 8Z" fill="#E9DCC0" stroke="#A8946A" strokeWidth="2" /></g>,
  },
  // Reine Mab : minuscule fée aux ailes de libellule, couronne de fleurs
  F: {
    body: '#E7B7D6', belly: '#FBE6F2', head: '#F6DCC8', eye: '#5A3E7A',
    back: <><ellipse cx="50" cy="96" rx="34" ry="18" fill="#CFE8FB" opacity={0.8} transform="rotate(-25 50 96)" /><ellipse cx="150" cy="96" rx="34" ry="18" fill="#CFE8FB" opacity={0.8} transform="rotate(25 150 96)" /></>,
    top: <>{[74, 88, 100, 112, 126].map((x, i) => <circle key={x} cx={x} cy={i % 2 ? 44 : 48} r="5" fill={i % 2 ? '#F2D94E' : '#E2709A'} />)}</>,
    front: <g transform="translate(158 140)"><path d="M0 30 V0" stroke="#C9A24A" strokeWidth="3" /><path d="M0 -8 l3 6 l6 1 l-5 4 l1 6 l-5 -3 l-5 3 l1 -6 l-5 -4 l6 -1Z" fill="#F2D94E" /></g>,
  },
  // Chevalier noir : armure sombre, heaume à fente, bouclier
  X: {
    body: '#2B2F38', belly: '#4A505C', head: '#3A404C', eye: '#E2483B',
    top: <><path d="M62 84 Q60 30 100 26 Q140 30 138 84Z" fill="#3A404C" stroke="#1A1E26" strokeWidth="3" /><path d="M100 26 Q108 8 124 6" stroke="#1A1E26" strokeWidth="6" fill="none" strokeLinecap="round" /></>,
    under: <path d="M74 96 H126" stroke="#111" strokeWidth="6" />,
    front: <g transform="translate(152 150)"><path d="M-18 -22 H18 V4 Q18 22 0 30 Q-18 22 -18 4Z" fill="#1A1E26" stroke="#8A8E96" strokeWidth="3" /><path d="M0 -22 V30 M-18 0 H18" stroke="#8A8E96" strokeWidth="2" /></g>,
  },
  // ───── Gardiens anglais (A1 — légendes britanniques) ─────
  // Boggart : lutin des maisons, nez crochu, bonnet mité, trousseau de badges volés
  B: {
    body: '#7A6A4A', belly: '#C9B98F', eye: '#F2D94E',
    top: <><path d="M62 64 Q66 26 100 20 Q130 24 140 64 Q120 50 100 50 Q80 50 62 64Z" fill="#5A3E5E" /><circle cx="134" cy="26" r="7" fill="#C9A24A" /></>,
    face: <path d="M100 92 Q114 104 104 112 Q98 108 100 92Z" fill="#5E4E34" />,
    front: <g transform="translate(152 150)"><circle r="10" fill="none" stroke="#B0B6BE" strokeWidth="3" /><rect x="-4" y="6" width="16" height="12" rx="2" fill="#3F6FB5" /><rect x="-14" y="8" width="14" height="10" rx="2" fill="#C8323F" /></g>,
  },
  // Puck : lutin des bois, oreilles pointues, couronne de feuilles, fleur magique
  P: {
    body: '#6DA84E', belly: '#D7EBC4', head: '#E8C9A4', eye: INK,
    top: <>{ear(58, false, '#E8C9A4', '#F2A7BB')}{ear(142, true, '#E8C9A4', '#F2A7BB')}{[64, 82, 100, 118, 136].map((x, i) => <path key={x} d={`M${x} ${i % 2 ? 44 : 50} q8 -14 16 0 q-8 6 -16 0Z`} fill="#3E7A3A" />)}</>,
    face: <path d="M84 112 Q100 124 116 112" stroke={INK} strokeWidth="4" fill="none" strokeLinecap="round" />,
    front: <g transform="translate(156 150)"><path d="M0 0 V24" stroke="#4E7F36" strokeWidth="3" />{[0, 72, 144, 216, 288].map((r) => <ellipse key={r} cx="0" cy="-8" rx="5" ry="9" fill="#A97BD6" transform={`rotate(${r})`} />)}<circle r="4" fill="#F2D94E" /></g>,
  },
  // Feu follet : petite flamme bleue qui flotte, lanterne de brume
  W: {
    body: '#7FB4E8', belly: '#DDEEFB', eye: '#1F3A5F',
    back: <><path d="M100 190 Q40 160 56 100 Q66 120 76 110 Q70 70 100 30 Q130 70 124 110 Q134 120 144 100 Q160 160 100 190Z" fill="#A9D3F5" opacity={0.85} /><circle cx="40" cy="70" r="6" fill="#CFE8FB" /><circle cx="164" cy="60" r="4" fill="#CFE8FB" /></>,
    top: <path d="M82 54 Q90 30 100 22 Q110 30 118 54Z" fill="#CFE8FB" />,
  },
  // Black Shuck : grand chien fantôme noir, yeux rouges, chaînes
  S: {
    body: '#2B2B33', belly: '#4A4A55', eye: '#E2483B',
    back: <path d="M150 150 Q196 140 186 100 Q174 124 148 128Z" fill="#2B2B33" />,
    top: <><path d="M58 70 L50 30 L82 54Z" fill="#2B2B33" /><path d="M142 70 L150 30 L118 54Z" fill="#2B2B33" /></>,
    face: <><ellipse cx="100" cy="104" rx="18" ry="12" fill="#3A3A44" /><ellipse cx="100" cy="98" rx="7" ry="5" fill="#111" /><path d="M90 114 l4 8 l4 -8 M102 114 l4 8 l4 -8" fill="#F6F3EC" /></>,
    front: <path d="M60 150 q10 8 20 0 q10 -8 20 0 q10 8 20 0 q10 -8 20 0" stroke="#8A8E96" strokeWidth="4" fill="none" />,
  },
  // Cormoran : géant de Cornouailles, barbe rousse, massue, tasse de thé géante
  G: {
    body: '#8A6A4A', belly: '#D9C2A0', head: '#E8B994', eye: INK,
    top: <path d="M62 70 Q60 36 100 32 Q140 36 138 70 Q120 52 100 52 Q80 52 62 70Z" fill="#B5542E" />,
    face: <path d="M74 112 Q100 168 126 112 Q114 126 100 122 Q86 126 74 112Z" fill="#B5542E" />,
    front: <g transform="translate(152 160)"><path d="M-14 -12 H14 V8 Q14 18 0 18 Q-14 18 -14 8Z" fill="#F6F3EC" stroke="#C9C2B4" strokeWidth="2" /><path d="M14 -6 q10 0 10 8 q0 8 -10 8" stroke="#C9C2B4" strokeWidth="3" fill="none" /><path d="M-6 -18 q4 -6 0 -12 M4 -18 q4 -6 0 -12" stroke="#C9C2B4" strokeWidth="2" fill="none" /></g>,
  },
  // Nessie : monstre du loch, long cou, bosses dans l'eau, écailles vertes
  N: {
    body: '#3E8E6B', belly: '#A8D9BF', eye: INK,
    back: <><path d="M0 178 Q30 166 60 178 T120 178 T200 178 L200 200 L0 200Z" fill="#3F7FBF" opacity={0.75} /><path d="M150 176 Q162 146 176 176Z M24 176 Q36 152 48 176Z" fill="#3E8E6B" /></>,
    top: <>{[70, 86, 102, 118].map((x) => <path key={x} d={`M${x} 46 l8 -12 l8 12Z`} fill="#2E6B4F" />)}</>,
    face: <><circle cx="86" cy="104" r="3" fill="#2E6B4F" /><circle cx="114" cy="104" r="3" fill="#2E6B4F" /></>,
  },
  // Chevalier vert : armure verte, heaume, hache, branche de houx
  K: {
    body: '#3E7A3A', belly: '#8FBF7A', head: '#8FBF7A', eye: '#F6F3EC',
    top: <><path d="M62 82 Q60 32 100 28 Q140 32 138 82 L128 82 L128 70 H72 V82Z" fill="#5E8A4A" stroke="#2E5A2A" strokeWidth="3" /><path d="M100 28 Q96 12 108 4" stroke="#C8323F" strokeWidth="5" fill="none" strokeLinecap="round" /></>,
    under: <path d="M72 84 H128" stroke="#2E5A2A" strokeWidth="4" />,
    front: <g transform="translate(158 150) rotate(-15)"><path d="M0 40 V-40" stroke="#6A4428" strokeWidth="6" /><path d="M0 -40 Q26 -34 22 -10 Q10 -16 0 -14Z" fill="#B0B6BE" stroke="#7A808A" strokeWidth="2" /></g>,
  },
  // Y Ddraig Goch : dragon rouge du pays de Galles, ailes, cornes, flammes
  D: {
    body: '#C8323F', belly: '#F2C27A', eye: '#F2D94E',
    back: <><path d="M60 120 Q10 80 20 40 Q40 70 60 60 Q50 90 70 110Z" fill="#A82632" /><path d="M140 120 Q190 80 180 40 Q160 70 140 60 Q150 90 130 110Z" fill="#A82632" /></>,
    top: <><path d="M70 56 Q60 30 74 18 Q76 38 86 48Z" fill="#F2C27A" /><path d="M130 56 Q140 30 126 18 Q124 38 114 48Z" fill="#F2C27A" /></>,
    face: <><circle cx="92" cy="104" r="3" fill="#7A1A22" /><circle cx="108" cy="104" r="3" fill="#7A1A22" /></>,
    front: <path d="M118 120 Q150 114 164 130 Q152 124 146 134 Q140 124 130 130Z" fill="#F2943A" />,
  },
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
    front: <>{[[60, 176], [140, 176]].map(([x, y], i) => <g key={i} transform={`translate(${x} ${y})`}><path d="M-14 0 Q-16 -18 0 -20 Q16 -18 14 0Z" fill="#E9D9B0" stroke="#A8987A" strokeWidth="2" /><text x="0" y="-5" textAnchor="middle" fontSize="11" fontWeight="900" fill="#8A3A2A">쌀</text></g>)}</>,
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
      {!['河', '天', '鶴', '獏', '해', '범', '용', '두', '까', '삼', '탈', '봉', '백', '산', '록', '변', '업', '억', '강', '개', '연', '목', '마', '생', '종', '적', '처', '단', '毕', '¡', 'ß', '♔', '♟', '♕', '♢', '♤', '♡', '♘', '♖', '☾', '✠', '❖', '✥'].includes(glyph) && <Mouth mood={mood} />}
      {sp.front}
    </svg>
  );
}
