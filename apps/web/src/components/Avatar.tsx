import { useId } from 'react';
import type { AvatarConfig } from '@koto/shared';
import { T } from '../i18n';

/**
 * Personnage dessiné en SVG, par calques : décor, tenue, tête, cheveux, couvre-chef, accessoire.
 * Création originale (style « chibi » arrondi), sans reprise d'aucun personnage existant.
 */
export const SKIN_TONES = ['#F7DCC9', '#EEC4A3', '#D9A07A', '#B07650', '#7A4E33'];
export const HAIR_COLORS = ['#2B2233', '#5A3A22', '#A0582A', '#D9B26A', '#9A9DB0', '#3B5BA5'];
export const HAIR_LABELS: Record<AvatarConfig['hair'], string> = { short: T("Courts"), long: T("Longs"), bun: T("Chignon"), spiky: T("En pétard"), bob: T("Carré"), none: T("Rasés") };
export const EYES_LABELS: Record<AvatarConfig['eyes'], string> = { round: T("Ronds"), happy: T("Rieurs"), calm: T("Sereins") };
export const HAIR_COLOR_LABELS = [T("Noir"), T("Châtain"), T("Roux"), T("Blond"), T("Gris"), T("Bleu")];

const INK = '#1B2550';

function Background({ sku, clip }: { sku: string | null; clip: string }) {
  switch (sku) {
    case 'bg-sakura':
      return (
        <g clipPath={`url(#${clip})`}>
          <rect width="200" height="220" fill="#FBE3EA" />
          {[[30, 40, 20], [160, 30, -30], [140, 90, 60], [25, 120, -10], [175, 150, 35], [60, 20, 80], [100, 12, -50]].map(([x, y, r], i) => (
            <ellipse key={i} cx={x} cy={y} rx="4.5" ry="8" transform={`rotate(${r} ${x} ${y})`} fill="#F2A7BB" opacity={0.85} />
          ))}
        </g>
      );
    case 'bg-night':
      return (
        <g clipPath={`url(#${clip})`}>
          <rect width="200" height="220" fill="#1C2452" />
          <circle cx="155" cy="45" r="20" fill="#F6E7B0" />
          <circle cx="163" cy="40" r="17" fill="#1C2452" />
          {[[30, 30], [60, 60], [120, 25], [40, 110], [170, 110], [90, 45]].map(([x, y], i) => <circle key={i} cx={x} cy={y} r="2" fill="#F6E7B0" />)}
        </g>
      );
    case 'bg-fuji':
      return (
        <g clipPath={`url(#${clip})`}>
          <rect width="200" height="220" fill="#FBE6CF" />
          <circle cx="40" cy="50" r="16" fill="#E9875A" />
          <path d="M-10 170 L70 70 Q100 50 130 70 L210 170Z" fill="#6E7FB5" />
          <path d="M70 70 Q100 50 130 70 L118 82 L108 74 L98 84 L88 74 L80 82Z" fill="#FFFFFF" />
        </g>
      );
    case 'bg-torii':
      return (
        <g clipPath={`url(#${clip})`}>
          <rect width="200" height="220" fill="#E8F0EE" />
          <g fill="#C23B4A">
            <path d="M10 38 Q100 22 190 38 L190 48 Q100 34 10 48Z" />
            <rect x="22" y="58" width="156" height="9" />
            <rect x="38" y="44" width="11" height="176" />
            <rect x="151" y="44" width="11" height="176" />
          </g>
        </g>
      );
    case 'bg-dragon':
      return (
        <g clipPath={`url(#${clip})`}>
          <rect width="200" height="220" fill="#4B3A7A" />
          <path d="M-10 60 C30 30 60 90 100 60 S170 30 210 60" stroke="#8C7BD1" strokeWidth="10" fill="none" strokeLinecap="round" />
          <path d="M-10 120 C30 90 60 150 100 120 S170 90 210 120" stroke="#6A59A8" strokeWidth="8" fill="none" strokeLinecap="round" />
          <circle cx="160" cy="30" r="6" fill="#F0B552" />
        </g>
      );
    default:
      return (
        <g clipPath={`url(#${clip})`}>
          <rect width="200" height="220" fill="#E2EBE8" />
          <circle cx="100" cy="108" r="78" fill="#EEF3F1" />
        </g>
      );
  }
}

function Outfit({ sku }: { sku: string | null }) {
  const body = 'M34 222 C38 182 62 166 100 166 C138 166 162 182 166 222Z';
  switch (sku) {
    case 'outfit-yukata-ai':
    case 'outfit-yukata-sakura': {
      const base = sku === 'outfit-yukata-ai' ? '#2D3F7A' : '#F2B8C6';
      const motif = sku === 'outfit-yukata-ai' ? '#FFFFFF' : '#C2577A';
      return (
        <g>
          <path d={body} fill={base} />
          <path d="M84 168 L100 200 L116 168" fill="none" stroke="#FFFFFF" strokeWidth="6" />
          <rect x="52" y="200" width="96" height="12" rx="3" fill={sku === 'outfit-yukata-ai' ? '#E3A13A' : '#8F3B5A'} />
          {[[60, 185], [140, 186], [70, 214], [132, 214]].map(([x, y], i) => <circle key={i} cx={x} cy={y} r="3.5" fill={motif} opacity={0.8} />)}
        </g>
      );
    }
    case 'outfit-happi':
      return (
        <g>
          <path d={body} fill="#C23B4A" />
          <path d="M80 167 L92 222 M120 167 L108 222" stroke="#FFFFFF" strokeWidth="9" />
          <path d="M40 212 H160" stroke="#FFFFFF" strokeWidth="4" strokeDasharray="6 5" />
        </g>
      );
    case 'outfit-hakama':
      return (
        <g>
          <path d={body} fill="#F4F1EC" />
          <path d="M84 168 L100 196 L116 168" fill="none" stroke="#C9C3B8" strokeWidth="4" />
          <path d="M46 198 H154 L162 222 H38Z" fill="#4A3A6B" />
          <path d="M80 198 V222 M100 198 V222 M120 198 V222" stroke="#382B54" strokeWidth="2" />
        </g>
      );
    default:
      return (
        <g>
          <path d={body} fill="#6E8BC9" />
          <path d="M84 168 Q100 182 116 168" fill="none" stroke="#56709F" strokeWidth="4" />
        </g>
      );
  }
}

function HairBack({ style, color }: { style: AvatarConfig['hair']; color: string }) {
  if (style === 'long') return <path d="M50 100 C50 52 150 52 150 100 V182 C150 190 140 194 132 190 V120 H68 V190 C60 194 50 190 50 182Z" fill={color} />;
  if (style === 'bob') return <path d="M52 100 C52 52 148 52 148 100 V140 C148 150 138 152 132 146 V112 H68 V146 C62 152 52 150 52 140Z" fill={color} />;
  if (style === 'bun') return <circle cx="100" cy="50" r="17" fill={color} />;
  return null;
}

function HairFront({ style, color }: { style: AvatarConfig['hair']; color: string }) {
  switch (style) {
    case 'none':
      return <path d="M52 100 C46 40 154 40 148 100 C134 76 66 76 52 100Z" fill={color} opacity={0.3} />;
    case 'spiky':
      return <path d="M52 100 L50 74 L64 80 L66 58 L80 70 L88 50 L100 66 L112 50 L120 70 L134 58 L136 80 L150 74 L148 100 C138 84 62 84 52 100Z" fill={color} />;
    case 'long':
    case 'bob':
      return <path d="M50 106 C42 28 158 28 150 106 C144 90 132 80 118 80 C108 92 88 94 76 84 C64 86 54 94 50 106Z" fill={color} />;
    default:
      // Courts : volume sur le dessus, raie sur le côté, petites pattes devant les oreilles.
      return <path d="M52 110 C42 28 158 28 148 110 C146 98 142 88 136 82 C122 86 100 84 86 74 C80 84 66 90 58 92 C56 98 54 104 52 110Z" fill={color} />;
  }
}

function Eyes({ kind }: { kind: AvatarConfig['eyes'] }) {
  if (kind === 'happy')
    return (
      <g fill="none" stroke={INK} strokeWidth="4" strokeLinecap="round">
        <path d="M74 110 Q82 101 90 110" />
        <path d="M110 110 Q118 101 126 110" />
      </g>
    );
  if (kind === 'calm')
    return (
      <g fill="none" stroke={INK} strokeWidth="4" strokeLinecap="round">
        <path d="M74 108 Q82 113 90 108" />
        <path d="M110 108 Q118 113 126 108" />
      </g>
    );
  return (
    <g className="avatar-blink">
      <ellipse cx="82" cy="107" rx="6.5" ry="8" fill={INK} />
      <ellipse cx="118" cy="107" rx="6.5" ry="8" fill={INK} />
      <circle cx="84.5" cy="104" r="2.2" fill="#FFFFFF" />
      <circle cx="120.5" cy="104" r="2.2" fill="#FFFFFF" />
    </g>
  );
}

function Hat({ sku }: { sku: string | null }) {
  switch (sku) {
    case 'hat-hachimaki':
      return (
        <g>
          <path d="M52 84 Q100 70 148 84 L147 95 Q100 82 53 95Z" fill="#FFFFFF" stroke="#D8D2C8" strokeWidth="1.5" />
          <circle cx="100" cy="84" r="5" fill="#C23B4A" />
          <path d="M146 88 L166 80 L162 94Z M146 90 L168 98 L158 104Z" fill="#FFFFFF" stroke="#D8D2C8" strokeWidth="1.5" />
        </g>
      );
    case 'hat-kasa':
      return (
        <g>
          <path d="M18 78 L100 30 L182 78 Q100 90 18 78Z" fill="#D9B26A" />
          <path d="M100 30 L60 80 M100 30 L140 80 M100 30 L100 84" stroke="#B8903F" strokeWidth="2" />
        </g>
      );
    case 'hat-kappa':
      return (
        <g>
          <ellipse cx="100" cy="58" rx="30" ry="9" fill="#5E8A3A" />
          <ellipse cx="100" cy="56" rx="24" ry="6" fill="#A9CF7E" />
        </g>
      );
    case 'hat-tanuki-leaf':
      return (
        <g transform="rotate(-18 100 50)">
          <path d="M100 30 C122 38 122 62 100 72 C78 62 78 38 100 30Z" fill="#5E8A3A" />
          <path d="M100 32 V76" stroke="#3E6324" strokeWidth="2.5" />
        </g>
      );
    case 'hat-kitsune':
      return (
        <g transform="rotate(18 150 72)">
          <path d="M128 70 L132 44 L146 60 L160 60 L172 44 L174 70 C174 92 128 92 128 70Z" fill="#FFFFFF" stroke="#D8D2C8" strokeWidth="1.5" />
          <path d="M136 70 L146 68 M156 68 L166 70" stroke="#C23B4A" strokeWidth="3" strokeLinecap="round" />
          <path d="M147 82 Q151 86 155 82" stroke="#C23B4A" strokeWidth="2.5" fill="none" />
        </g>
      );
    case 'hat-oni':
      return (
        <g fill="#F0D9A8" stroke="#C9A866" strokeWidth="1.5">
          <path d="M70 70 L62 40 L84 64Z" />
          <path d="M130 70 L138 40 L116 64Z" />
        </g>
      );
    default:
      return null;
  }
}

function Accessory({ sku }: { sku: string | null }) {
  switch (sku) {
    case 'acc-glasses':
      return (
        <g fill="none" stroke={INK} strokeWidth="3">
          <circle cx="82" cy="107" r="13" />
          <circle cx="118" cy="107" r="13" />
          <path d="M95 106 H105" />
        </g>
      );
    case 'acc-scarf':
      return (
        <g fill="#C23B4A">
          <path d="M68 160 Q100 178 132 160 L134 172 Q100 190 66 172Z" />
          <path d="M116 172 L126 206 L112 206 L106 176Z" />
        </g>
      );
    case 'acc-sensu':
      return (
        <g transform="translate(36 160) rotate(-20)">
          <path d="M0 40 L-26 6 A42 42 0 0 1 26 6Z" fill="#F4F1EC" stroke="#C9C3B8" strokeWidth="1.5" />
          <path d="M0 40 L-14 2 M0 40 L0 0 M0 40 L14 2" stroke="#C23B4A" strokeWidth="1.5" />
        </g>
      );
    case 'acc-tengu-fan':
      return (
        <g transform="translate(38 168) rotate(-25)">
          <path d="M0 36 C-22 20 -18 -14 0 -22 C18 -14 22 20 0 36Z" fill="#3E6324" />
          <path d="M0 36 V-18" stroke="#A9CF7E" strokeWidth="2" />
          <rect x="-3" y="34" width="6" height="16" rx="2" fill="#8A5A2B" />
        </g>
      );
    case 'acc-maneki':
      return (
        <g transform="translate(162 182)">
          <circle cx="0" cy="12" r="15" fill="#FFFFFF" stroke="#D8D2C8" />
          <circle cx="0" cy="-6" r="12" fill="#FFFFFF" stroke="#D8D2C8" />
          <path d="M-10 -12 L-8 -24 L-2 -16Z M10 -12 L8 -24 L2 -16Z" fill="#FFFFFF" stroke="#D8D2C8" />
          <path d="M-5 -6 h2 M3 -6 h2" stroke={INK} strokeWidth="2" strokeLinecap="round" />
          <path d="M10 2 L14 -12" stroke="#FFFFFF" strokeWidth="6" strokeLinecap="round" />
          <circle cx="0" cy="12" r="4" fill="#E3A13A" />
        </g>
      );
    case 'acc-lantern':
      return (
        <g transform="translate(164 168)">
          <path d="M0 -24 V-14" stroke={INK} strokeWidth="2" />
          <rect x="-10" y="-16" width="20" height="4" rx="1" fill={INK} />
          <ellipse cx="0" cy="6" rx="16" ry="20" fill="#C23B4A" />
          <path d="M-16 6 H16 M-14 -4 H14 M-14 16 H14" stroke="#9E2C3A" strokeWidth="1.5" />
          <rect x="-10" y="24" width="20" height="4" rx="1" fill={INK} />
        </g>
      );
    default:
      return null;
  }
}

/** `bare` : sans fond (personnage posé dans une illustration). */
export function Avatar({ config, size = 120, title, bare = false }: { config: AvatarConfig; size?: number; title?: string; bare?: boolean }) {
  const clip = useId().replace(/:/g, '');
  const skin = SKIN_TONES[config.skin] ?? SKIN_TONES[1];
  const hair = HAIR_COLORS[config.hairColor] ?? HAIR_COLORS[0];
  return (
    <svg width={size} height={(size * 220) / 200} viewBox="0 0 200 220" role="img" aria-label={title ?? T("Ton personnage")} className="block">
      <defs>
        <clipPath id={clip}>
          <rect width="200" height="220" rx="28" />
        </clipPath>
      </defs>
      {!bare && <Background sku={config.background} clip={clip} />}
      <g clipPath={`url(#${clip})`}>
        <HairBack style={config.hair} color={hair} />
        <Outfit sku={config.outfit} />
        <rect x="90" y="146" width="20" height="24" rx="8" fill={skin} />
        <circle cx="100" cy="104" r="48" fill={skin} />
        <ellipse cx="72" cy="124" rx="8" ry="5" fill="#F2A7A0" opacity={0.6} />
        <ellipse cx="128" cy="124" rx="8" ry="5" fill="#F2A7A0" opacity={0.6} />
        <Eyes kind={config.eyes} />
        <path d="M93 128 Q100 135 107 128" fill="none" stroke={INK} strokeWidth="3" strokeLinecap="round" />
        <HairFront style={config.hair} color={hair} />
        <Hat sku={config.hat} />
        <Accessory sku={config.accessory} />
      </g>
    </svg>
  );
}
