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
      {!['河', '天', '鶴', '獏'].includes(glyph) && <Mouth mood={mood} />}
      {sp.front}
    </svg>
  );
}
