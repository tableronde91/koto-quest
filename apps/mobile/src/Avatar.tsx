import { useId } from 'react';
import type { AvatarConfig } from '@koto/shared';
import Svg, { Circle, ClipPath, Defs, Ellipse, G, Path, Rect } from 'react-native-svg';
import { T } from './i18n';

/**
 * Personnage dessiné en SVG, par calques : décor, tenue, tête, cheveux, couvre-chef, accessoire.
 * Création originale (style « chibi » arrondi), sans reprise d'aucun personnage existant.
 */
export const SKIN_TONES = ['#F7DCC9', '#EEC4A3', '#D9A07A', '#B07650', '#7A4E33'];
export const HAIR_COLORS = ['#2B2233', '#5A3A22', '#A0582A', '#D9B26A', '#9A9DB0', '#3B5BA5'];
/** Libellés traduits à l'affichage avec T(). */
export const HAIR_LABELS: Record<AvatarConfig['hair'], string> = { short: 'Courts', long: 'Longs', bun: 'Chignon', spiky: 'En pétard', bob: 'Carré', none: 'Rasés' };
export const EYES_LABELS: Record<AvatarConfig['eyes'], string> = { round: 'Ronds', happy: 'Rieurs', calm: 'Sereins' };
export const HAIR_COLOR_LABELS = ['Noir', 'Châtain', 'Roux', 'Blond', 'Gris', 'Bleu'];

const INK = '#1B2550';

function Background({ sku, clip }: { sku: string | null; clip: string }) {
  switch (sku) {
    case 'bg-sakura':
      return (
        <G clipPath={`url(#${clip})`}>
          <Rect width="200" height="220" fill="#FBE3EA" />
          {[[30, 40, 20], [160, 30, -30], [140, 90, 60], [25, 120, -10], [175, 150, 35], [60, 20, 80], [100, 12, -50]].map(([x, y, r], i) => (
            <Ellipse key={i} cx={x} cy={y} rx="4.5" ry="8" transform={`rotate(${r} ${x} ${y})`} fill="#F2A7BB" opacity={0.85} />
          ))}
        </G>
      );
    case 'bg-night':
      return (
        <G clipPath={`url(#${clip})`}>
          <Rect width="200" height="220" fill="#1C2452" />
          <Circle cx="155" cy="45" r="20" fill="#F6E7B0" />
          <Circle cx="163" cy="40" r="17" fill="#1C2452" />
          {[[30, 30], [60, 60], [120, 25], [40, 110], [170, 110], [90, 45]].map(([x, y], i) => <Circle key={i} cx={x} cy={y} r="2" fill="#F6E7B0" />)}
        </G>
      );
    case 'bg-fuji':
      return (
        <G clipPath={`url(#${clip})`}>
          <Rect width="200" height="220" fill="#FBE6CF" />
          <Circle cx="40" cy="50" r="16" fill="#E9875A" />
          <Path d="M-10 170 L70 70 Q100 50 130 70 L210 170Z" fill="#6E7FB5" />
          <Path d="M70 70 Q100 50 130 70 L118 82 L108 74 L98 84 L88 74 L80 82Z" fill="#FFFFFF" />
        </G>
      );
    case 'bg-torii':
      return (
        <G clipPath={`url(#${clip})`}>
          <Rect width="200" height="220" fill="#E8F0EE" />
          <G fill="#C23B4A">
            <Path d="M10 38 Q100 22 190 38 L190 48 Q100 34 10 48Z" />
            <Rect x="22" y="58" width="156" height="9" />
            <Rect x="38" y="44" width="11" height="176" />
            <Rect x="151" y="44" width="11" height="176" />
          </G>
        </G>
      );
    case 'bg-dragon':
      return (
        <G clipPath={`url(#${clip})`}>
          <Rect width="200" height="220" fill="#4B3A7A" />
          <Path d="M-10 60 C30 30 60 90 100 60 S170 30 210 60" stroke="#8C7BD1" strokeWidth="10" fill="none" strokeLinecap="round" />
          <Path d="M-10 120 C30 90 60 150 100 120 S170 90 210 120" stroke="#6A59A8" strokeWidth="8" fill="none" strokeLinecap="round" />
          <Circle cx="160" cy="30" r="6" fill="#F0B552" />
        </G>
      );
    case 'bg-palace':
      return (
        <G clipPath={`url(#${clip})`}>
          <Rect width="200" height="220" fill="#F3E6CF" />
          <Circle cx="160" cy="36" r="14" fill="#E9875A" />
          <Rect x="-10" y="150" width="220" height="70" fill="#C9B79A" />
          <Rect x="20" y="96" width="160" height="58" fill="#F4EEDF" />
          <G fill="#B23A3A">
            <Rect x="26" y="96" width="9" height="58" />
            <Rect x="70" y="96" width="9" height="58" />
            <Rect x="121" y="96" width="9" height="58" />
            <Rect x="165" y="96" width="9" height="58" />
          </G>
          <Rect x="18" y="88" width="164" height="9" fill="#2E8B7A" />
          <Path d="M18 92 H182" stroke="#E2B84A" strokeWidth="2" />
          <Path d="M-8 90 Q8 78 24 72 H176 Q192 78 208 90 Q100 76 -8 90Z" fill="#3A3F46" />
          <Path d="M24 72 Q100 54 176 72 L168 58 H32Z" fill="#3A3F46" />
          <Path d="M32 58 H168" stroke="#272B31" strokeWidth="3" />
        </G>
      );
    case 'bg-hanok':
      return (
        <G clipPath={`url(#${clip})`}>
          <Rect width="200" height="220" fill="#22305E" />
          <Circle cx="150" cy="44" r="18" fill="#FFF3C4" />
          <Circle cx="145" cy="40" r="3" fill="#EADBA0" />
          <Circle cx="156" cy="50" r="2" fill="#EADBA0" />
          <Circle cx="30" cy="30" r="1.8" fill="#F6E7B0" />
          <Circle cx="70" cy="18" r="1.5" fill="#F6E7B0" />
          <Circle cx="110" cy="34" r="1.5" fill="#F6E7B0" />
          <Rect x="-4" y="148" width="62" height="72" fill="#F4EEDF" />
          <Path d="M-14 152 Q10 132 68 138 L64 148 Q10 144 -14 162Z" fill="#2B2F36" />
          <Rect x="10" y="166" width="14" height="18" fill="#F2B84B" opacity={0.85} />
          <Rect x="146" y="144" width="64" height="76" fill="#F4EEDF" />
          <Path d="M136 146 Q190 128 214 134 L214 154 Q190 140 140 156Z" fill="#2B2F36" />
          <Rect x="174" y="164" width="14" height="18" fill="#F2B84B" opacity={0.85} />
        </G>
      );
    case 'bg-east-sea':
      return (
        <G clipPath={`url(#${clip})`}>
          <Rect width="200" height="220" fill="#CDEBF2" />
          <Circle cx="40" cy="44" r="16" fill="#F29A3A" />
          <Path d="M150 124 C170 92 198 102 190 72 C186 58 172 60 176 46" stroke="#2F8F7A" strokeWidth="10" fill="none" strokeLinecap="round" />
          <Path d="M172 48 L186 36 L183 52Z" fill="#E7B53B" />
          <Path d="M-10 140 Q20 128 50 140 T110 140 T170 140 T230 140 V220 H-10Z" fill="#3F8FD9" />
          <Path d="M-10 168 Q20 156 50 168 T110 168 T170 168 T230 168 V220 H-10Z" fill="#2F6FB0" />
        </G>
      );
    default:
      return (
        <G clipPath={`url(#${clip})`}>
          <Rect width="200" height="220" fill="#E2EBE8" />
          <Circle cx="100" cy="108" r="78" fill="#EEF3F1" />
        </G>
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
        <G>
          <Path d={body} fill={base} />
          <Path d="M84 168 L100 200 L116 168" fill="none" stroke="#FFFFFF" strokeWidth="6" />
          <Rect x="52" y="200" width="96" height="12" rx="3" fill={sku === 'outfit-yukata-ai' ? '#E3A13A' : '#8F3B5A'} />
          {[[60, 185], [140, 186], [70, 214], [132, 214]].map(([x, y], i) => <Circle key={i} cx={x} cy={y} r="3.5" fill={motif} opacity={0.8} />)}
        </G>
      );
    }
    case 'outfit-happi':
      return (
        <G>
          <Path d={body} fill="#C23B4A" />
          <Path d="M80 167 L92 222 M120 167 L108 222" stroke="#FFFFFF" strokeWidth="9" />
          <Path d="M40 212 H160" stroke="#FFFFFF" strokeWidth="4" strokeDasharray="6 5" />
        </G>
      );
    case 'outfit-hakama':
      return (
        <G>
          <Path d={body} fill="#F4F1EC" />
          <Path d="M84 168 L100 196 L116 168" fill="none" stroke="#C9C3B8" strokeWidth="4" />
          <Path d="M46 198 H154 L162 222 H38Z" fill="#4A3A6B" />
          <Path d="M80 198 V222 M100 198 V222 M120 198 V222" stroke="#382B54" strokeWidth="2" />
        </G>
      );
    case 'outfit-hanbok':
      return (
        <G>
          <Path d={body} fill="#C8323F" />
          <Path d="M38 202 C42 178 64 166 100 166 C136 166 158 178 162 202 Q100 212 38 202Z" fill="#F2C94C" />
          <Path d="M44 194 L60 190 M42 200 L58 196" stroke="#2E8B7A" strokeWidth="3" />
          <Path d="M156 194 L140 190 M158 200 L142 196" stroke="#2E8B7A" strokeWidth="3" />
          <Path d="M84 168 L100 192 L116 168" fill="none" stroke="#FFFFFF" strokeWidth="5" />
          <Path d="M100 192 Q94 206 88 222 M100 192 Q108 206 112 220" stroke="#8E3B8E" strokeWidth="5" fill="none" strokeLinecap="round" />
        </G>
      );
    case 'outfit-durumagi':
      return (
        <G>
          <Path d={body} fill="#5E7A9A" />
          <Path d="M84 168 L100 196 L116 168" fill="none" stroke="#FFFFFF" strokeWidth="5" />
          <Path d="M100 196 V222" stroke="#4A6280" strokeWidth="3" />
          <Path d="M100 196 Q90 206 88 216 M100 196 Q108 208 112 214" stroke="#E9D9B0" strokeWidth="4" fill="none" strokeLinecap="round" />
        </G>
      );
    default:
      return (
        <G>
          <Path d={body} fill="#6E8BC9" />
          <Path d="M84 168 Q100 182 116 168" fill="none" stroke="#56709F" strokeWidth="4" />
        </G>
      );
  }
}

function HairBack({ style, color }: { style: AvatarConfig['hair']; color: string }) {
  if (style === 'long') return <Path d="M50 100 C50 52 150 52 150 100 V182 C150 190 140 194 132 190 V120 H68 V190 C60 194 50 190 50 182Z" fill={color} />;
  if (style === 'bob') return <Path d="M52 100 C52 52 148 52 148 100 V140 C148 150 138 152 132 146 V112 H68 V146 C62 152 52 150 52 140Z" fill={color} />;
  if (style === 'bun') return <Circle cx="100" cy="50" r="17" fill={color} />;
  return null;
}

function HairFront({ style, color }: { style: AvatarConfig['hair']; color: string }) {
  switch (style) {
    case 'none':
      return <Path d="M52 100 C46 40 154 40 148 100 C134 76 66 76 52 100Z" fill={color} opacity={0.3} />;
    case 'spiky':
      return <Path d="M52 100 L50 74 L64 80 L66 58 L80 70 L88 50 L100 66 L112 50 L120 70 L134 58 L136 80 L150 74 L148 100 C138 84 62 84 52 100Z" fill={color} />;
    case 'long':
    case 'bob':
      return <Path d="M50 106 C42 28 158 28 150 106 C144 90 132 80 118 80 C108 92 88 94 76 84 C64 86 54 94 50 106Z" fill={color} />;
    default:
      // Courts : volume sur le dessus, raie sur le côté, petites pattes devant les oreilles.
      return <Path d="M52 110 C42 28 158 28 148 110 C146 98 142 88 136 82 C122 86 100 84 86 74 C80 84 66 90 58 92 C56 98 54 104 52 110Z" fill={color} />;
  }
}

function Eyes({ kind }: { kind: AvatarConfig['eyes'] }) {
  if (kind === 'happy')
    return (
      <G fill="none" stroke={INK} strokeWidth="4" strokeLinecap="round">
        <Path d="M74 110 Q82 101 90 110" />
        <Path d="M110 110 Q118 101 126 110" />
      </G>
    );
  if (kind === 'calm')
    return (
      <G fill="none" stroke={INK} strokeWidth="4" strokeLinecap="round">
        <Path d="M74 108 Q82 113 90 108" />
        <Path d="M110 108 Q118 113 126 108" />
      </G>
    );
  return (
    <G>
      <Ellipse cx="82" cy="107" rx="6.5" ry="8" fill={INK} />
      <Ellipse cx="118" cy="107" rx="6.5" ry="8" fill={INK} />
      <Circle cx="84.5" cy="104" r="2.2" fill="#FFFFFF" />
      <Circle cx="120.5" cy="104" r="2.2" fill="#FFFFFF" />
    </G>
  );
}

function Hat({ sku }: { sku: string | null }) {
  switch (sku) {
    case 'hat-hachimaki':
      return (
        <G>
          <Path d="M52 84 Q100 70 148 84 L147 95 Q100 82 53 95Z" fill="#FFFFFF" stroke="#D8D2C8" strokeWidth="1.5" />
          <Circle cx="100" cy="84" r="5" fill="#C23B4A" />
          <Path d="M146 88 L166 80 L162 94Z M146 90 L168 98 L158 104Z" fill="#FFFFFF" stroke="#D8D2C8" strokeWidth="1.5" />
        </G>
      );
    case 'hat-kasa':
      return (
        <G>
          <Path d="M18 78 L100 30 L182 78 Q100 90 18 78Z" fill="#D9B26A" />
          <Path d="M100 30 L60 80 M100 30 L140 80 M100 30 L100 84" stroke="#B8903F" strokeWidth="2" />
        </G>
      );
    case 'hat-kappa':
      return (
        <G>
          <Ellipse cx="100" cy="58" rx="30" ry="9" fill="#5E8A3A" />
          <Ellipse cx="100" cy="56" rx="24" ry="6" fill="#A9CF7E" />
        </G>
      );
    case 'hat-tanuki-leaf':
      return (
        <G transform="rotate(-18 100 50)">
          <Path d="M100 30 C122 38 122 62 100 72 C78 62 78 38 100 30Z" fill="#5E8A3A" />
          <Path d="M100 32 V76" stroke="#3E6324" strokeWidth="2.5" />
        </G>
      );
    case 'hat-kitsune':
      return (
        <G transform="rotate(18 150 72)">
          <Path d="M128 70 L132 44 L146 60 L160 60 L172 44 L174 70 C174 92 128 92 128 70Z" fill="#FFFFFF" stroke="#D8D2C8" strokeWidth="1.5" />
          <Path d="M136 70 L146 68 M156 68 L166 70" stroke="#C23B4A" strokeWidth="3" strokeLinecap="round" />
          <Path d="M147 82 Q151 86 155 82" stroke="#C23B4A" strokeWidth="2.5" fill="none" />
        </G>
      );
    case 'hat-oni':
      return (
        <G fill="#F0D9A8" stroke="#C9A866" strokeWidth="1.5">
          <Path d="M70 70 L62 40 L84 64Z" />
          <Path d="M130 70 L138 40 L116 64Z" />
        </G>
      );
    case 'hat-binyeo':
      return (
        <G transform="rotate(-8 100 60)">
          <Rect x="58" y="58" width="86" height="5" rx="2.5" fill="#E2B84A" stroke="#A57E22" strokeWidth="1" />
          <Circle cx="58" cy="60.5" r="6.5" fill="#C8323F" />
          <Circle cx="58" cy="60.5" r="2.5" fill="#F2C94C" />
        </G>
      );
    case 'hat-dokkaebi':
      return (
        <G>
          <Path d="M91 68 L100 32 L109 68Z" fill="#F0D9A8" stroke="#C9A866" strokeWidth="1.5" />
          <Path d="M95 56 H105 M97 46 H103" stroke="#C9A866" strokeWidth="1.5" />
        </G>
      );
    case 'hat-gat':
      return (
        <G>
          <Ellipse cx="100" cy="66" rx="74" ry="10" fill="#141418" opacity={0.92} />
          <Path d="M78 66 V36 Q100 28 122 36 V66Z" fill="#141418" opacity={0.92} />
          <Path d="M62 72 Q60 120 72 150 M138 72 Q140 120 128 150" stroke="#141418" strokeWidth="2" fill="none" />
        </G>
      );
    default:
      return null;
  }
}

function Accessory({ sku }: { sku: string | null }) {
  switch (sku) {
    case 'acc-glasses':
      return (
        <G fill="none" stroke={INK} strokeWidth="3">
          <Circle cx="82" cy="107" r="13" />
          <Circle cx="118" cy="107" r="13" />
          <Path d="M95 106 H105" />
        </G>
      );
    case 'acc-scarf':
      return (
        <G fill="#C23B4A">
          <Path d="M68 160 Q100 178 132 160 L134 172 Q100 190 66 172Z" />
          <Path d="M116 172 L126 206 L112 206 L106 176Z" />
        </G>
      );
    case 'acc-sensu':
      return (
        <G transform="translate(36 160) rotate(-20)">
          <Path d="M0 40 L-26 6 A42 42 0 0 1 26 6Z" fill="#F4F1EC" stroke="#C9C3B8" strokeWidth="1.5" />
          <Path d="M0 40 L-14 2 M0 40 L0 0 M0 40 L14 2" stroke="#C23B4A" strokeWidth="1.5" />
        </G>
      );
    case 'acc-tengu-fan':
      return (
        <G transform="translate(38 168) rotate(-25)">
          <Path d="M0 36 C-22 20 -18 -14 0 -22 C18 -14 22 20 0 36Z" fill="#3E6324" />
          <Path d="M0 36 V-18" stroke="#A9CF7E" strokeWidth="2" />
          <Rect x="-3" y="34" width="6" height="16" rx="2" fill="#8A5A2B" />
        </G>
      );
    case 'acc-maneki':
      return (
        <G transform="translate(162 182)">
          <Circle cx="0" cy="12" r="15" fill="#FFFFFF" stroke="#D8D2C8" />
          <Circle cx="0" cy="-6" r="12" fill="#FFFFFF" stroke="#D8D2C8" />
          <Path d="M-10 -12 L-8 -24 L-2 -16Z M10 -12 L8 -24 L2 -16Z" fill="#FFFFFF" stroke="#D8D2C8" />
          <Path d="M-5 -6 h2 M3 -6 h2" stroke={INK} strokeWidth="2" strokeLinecap="round" />
          <Path d="M10 2 L14 -12" stroke="#FFFFFF" strokeWidth="6" strokeLinecap="round" />
          <Circle cx="0" cy="12" r="4" fill="#E3A13A" />
        </G>
      );
    case 'acc-lantern':
      return (
        <G transform="translate(164 168)">
          <Path d="M0 -24 V-14" stroke={INK} strokeWidth="2" />
          <Rect x="-10" y="-16" width="20" height="4" rx="1" fill={INK} />
          <Ellipse cx="0" cy="6" rx="16" ry="20" fill="#C23B4A" />
          <Path d="M-16 6 H16 M-14 -4 H14 M-14 16 H14" stroke="#9E2C3A" strokeWidth="1.5" />
          <Rect x="-10" y="24" width="20" height="4" rx="1" fill={INK} />
        </G>
      );
    case 'acc-buchae':
      return (
        <G transform="translate(36 160) rotate(-20)">
          <Path d="M0 40 L-28 4 A44 44 0 0 1 28 4Z" fill="#F29BB8" />
          <Path d="M-28 4 A44 44 0 0 1 28 4" stroke="#FFFFFF" strokeWidth="5" fill="none" />
          <Path d="M0 40 L-14 2 M0 40 L0 -2 M0 40 L14 2" stroke="#C8323F" strokeWidth="1.5" />
          <Circle cx="0" cy="40" r="3" fill="#E2B84A" />
        </G>
      );
    case 'acc-haetae':
      return (
        <G transform="translate(162 184)">
          <Ellipse cx="0" cy="12" rx="16" ry="13" fill="#E2B84A" stroke="#A57E22" />
          <Circle cx="0" cy="-6" r="12" fill="#E2B84A" stroke="#A57E22" />
          <Circle cx="-9" cy="-14" r="5" fill="#2E8B7A" />
          <Circle cx="9" cy="-14" r="5" fill="#2E8B7A" />
          <Circle cx="0" cy="-18" r="5" fill="#2E8B7A" />
          <Path d="M-5 -6 h2 M3 -6 h2" stroke={INK} strokeWidth="2" strokeLinecap="round" />
          <Path d="M-4 0 Q0 3 4 0" stroke={INK} strokeWidth="1.5" fill="none" />
        </G>
      );
    case 'acc-fox-bead':
      return (
        <G transform="translate(160 176)">
          <Circle r="17" fill="#9FD8F2" opacity={0.45} />
          <Circle r="10" fill="#5FB8E8" />
          <Circle cx="-3" cy="-3" r="3" fill="#FFFFFF" opacity={0.85} />
        </G>
      );
    case 'acc-gotgam':
      return (
        <G transform="translate(34 150)">
          <Path d="M0 -10 V52" stroke="#7A4E30" strokeWidth="2" />
          <Ellipse cx="0" cy="0" rx="9" ry="8" fill="#E36A3A" stroke="#B8502A" />
          <Ellipse cx="0" cy="18" rx="9" ry="8" fill="#E36A3A" stroke="#B8502A" />
          <Ellipse cx="0" cy="36" rx="9" ry="8" fill="#E36A3A" stroke="#B8502A" />
        </G>
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
    <Svg width={size} height={(size * 220) / 200} viewBox="0 0 200 220" accessibilityLabel={title ?? T('Ton personnage')}>
      <Defs>
        <ClipPath id={clip}>
          <Rect width="200" height="220" rx="28" />
        </ClipPath>
      </Defs>
      {!bare && <Background sku={config.background} clip={clip} />}
      <G clipPath={`url(#${clip})`}>
        <HairBack style={config.hair} color={hair} />
        <Outfit sku={config.outfit} />
        <Rect x="90" y="146" width="20" height="24" rx="8" fill={skin} />
        <Circle cx="100" cy="104" r="48" fill={skin} />
        <Ellipse cx="72" cy="124" rx="8" ry="5" fill="#F2A7A0" opacity={0.6} />
        <Ellipse cx="128" cy="124" rx="8" ry="5" fill="#F2A7A0" opacity={0.6} />
        <Eyes kind={config.eyes} />
        <Path d="M93 128 Q100 135 107 128" fill="none" stroke={INK} strokeWidth="3" strokeLinecap="round" />
        <HairFront style={config.hair} color={hair} />
        <Hat sku={config.hat} />
        <Accessory sku={config.accessory} />
      </G>
    </Svg>
  );
}
