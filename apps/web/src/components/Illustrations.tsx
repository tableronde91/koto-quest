import { motion } from 'motion/react';
import type { AvatarConfig } from '@koto/shared';
import { Avatar } from './Avatar';
import { T } from '../i18n';

/**
 * Illustrations originales en SVG (aucune image externe) : couleurs tirées des jetons du thème,
 * donc lisibles en mode clair comme en mode sombre.
 */

const INK = 'var(--ink)';
const GOLD = 'var(--gold)';
const BENI = 'var(--ko)';
const MATCHA = 'var(--ok)';

/** Pétales de cerisier qui tombent (boucle douce ; immobiles si les animations sont réduites). */
function FallingPetals({ count = 7, width = 400, height = 300 }: { count?: number; width?: number; height?: number }) {
  return (
    <g aria-hidden="true">
      {Array.from({ length: count }, (_, i) => {
        const x = ((i * 53) % (width - 40)) + 20;
        return (
          <motion.ellipse
            key={i}
            cx={x}
            cy={-10}
            rx="4.5"
            ry="7.5"
            fill="#F2A7BB"
            opacity={0.9}
            animate={{ cy: [-10, height + 10], cx: [x, x + (i % 2 ? 30 : -30)], rotate: [0, 220] }}
            transition={{ duration: 7 + (i % 3) * 2, repeat: Infinity, delay: i * 1.1, ease: 'linear' }}
          />
        );
      })}
    </g>
  );
}

/** Scène d'accueil : mont, torii, branche de cerisier et le personnage qui salue. */
export function HeroScene({ avatar }: { avatar: AvatarConfig }) {
  return (
    <div className="relative mx-auto aspect-[4/3] md:mx-0 w-full max-w-md" aria-hidden="true">
      <svg viewBox="0 0 400 300" className="absolute inset-0 h-full w-full">
        <defs>
          <clipPath id="hero-clip">
            <rect width="400" height="300" rx="36" />
          </clipPath>
        </defs>
        <g clipPath="url(#hero-clip)">
          <rect width="400" height="300" fill="var(--surface-2)" />
          <motion.circle cx="300" cy="80" r="38" fill={GOLD} opacity={0.85} animate={{ r: [38, 41, 38] }} transition={{ duration: 6, repeat: Infinity }} />
          <path d="M-20 240 L140 90 Q170 70 200 90 L360 240Z" fill={INK} opacity={0.85} />
          <path d="M140 90 Q170 70 200 90 L188 104 L176 94 L166 108 L154 94 L146 104Z" fill="var(--surface)" />
          <path d="M0 250 Q200 215 400 250 L400 300 L0 300Z" fill={MATCHA} opacity={0.55} />
          <g fill={BENI}>
            <path d="M250 150 Q305 140 360 150 L360 158 Q305 148 250 158Z" />
            <rect x="262" y="166" width="86" height="6" />
            <rect x="270" y="156" width="8" height="100" />
            <rect x="332" y="156" width="8" height="100" />
          </g>
          <path d="M400 18 Q330 30 300 6" stroke="#6B4A3A" strokeWidth="6" fill="none" strokeLinecap="round" />
          {[[330, 20], [352, 14], [372, 24], [315, 10]].map(([x, y], i) => (
            <circle key={i} cx={x} cy={y} r="9" fill="#F2A7BB" />
          ))}
          <FallingPetals />
        </g>
      </svg>
      <motion.div
        className="absolute bottom-[4%] left-[8%] w-[38%]"
        initial={{ y: 30, opacity: 0 }}
        animate={{ y: 0, opacity: 1 }}
        transition={{ delay: 0.2, type: 'spring', stiffness: 160, damping: 14 }}
      >
        <motion.div animate={{ rotate: [0, -3, 3, 0] }} transition={{ duration: 2.4, repeat: Infinity, repeatDelay: 1.5 }} style={{ transformOrigin: '50% 100%' }}>
          <Avatar config={avatar} size={150} title={T("Ton futur personnage")} bare />
        </motion.div>
      </motion.div>
      <motion.div
        className="absolute left-[44%] top-[44%] rounded-2xl bg-surface px-3 py-2 shadow-md"
        initial={{ scale: 0, opacity: 0 }}
        animate={{ scale: 1, opacity: 1 }}
        transition={{ delay: 0.7, type: 'spring' }}
        style={{ transformOrigin: '0% 100%' }}
      >
        <span lang="ja" className="jp text-xl font-bold">こんにちは！</span>
      </motion.div>
    </div>
  );
}

/** Chat endormi : état vide « rien à réviser ». */
export function SleepingCat({ className = '' }: { className?: string }) {
  return (
    <svg viewBox="0 0 220 140" className={className} aria-hidden="true">
      <ellipse cx="110" cy="122" rx="86" ry="10" fill="var(--surface-2)" />
      <path d="M40 116 C30 70 90 52 130 64 C170 74 186 100 176 118Z" fill={GOLD} />
      <path d="M60 112 C40 112 34 96 50 92" stroke={GOLD} strokeWidth="12" fill="none" strokeLinecap="round" />
      <circle cx="152" cy="92" r="24" fill={GOLD} />
      <path d="M134 76 L138 58 L150 72Z M160 70 L170 56 L172 76Z" fill={GOLD} />
      <path d="M142 94 Q146 98 150 94 M158 94 Q162 98 166 94" stroke={INK} strokeWidth="2.5" fill="none" strokeLinecap="round" />
      <path d="M90 82 Q100 76 110 82 M80 96 Q92 90 104 96" stroke="#B8803A" strokeWidth="4" fill="none" strokeLinecap="round" opacity={0.6} />
      {['Z', 'z', 'z'].map((z, i) => (
        <motion.text
          key={i}
          x={184 + i * 10}
          y={60 - i * 14}
          fontSize={18 - i * 3}
          fontWeight="700"
          fill="var(--ink-soft)"
          animate={{ opacity: [0, 1, 0], y: [60 - i * 14, 50 - i * 14] }}
          transition={{ duration: 2.4, repeat: Infinity, delay: i * 0.5 }}
        >
          {z}
        </motion.text>
      ))}
    </svg>
  );
}

/** Jeune pousse : état vide « aucune notion encore ». */
export function Sprout({ className = '' }: { className?: string }) {
  return (
    <svg viewBox="0 0 120 120" className={className} aria-hidden="true">
      <ellipse cx="60" cy="104" rx="40" ry="8" fill="var(--surface-2)" />
      <path d="M60 104 V60" stroke={MATCHA} strokeWidth="5" strokeLinecap="round" />
      <motion.g style={{ transformOrigin: '60px 70px' }} animate={{ rotate: [-4, 4, -4] }} transition={{ duration: 3, repeat: Infinity }}>
        <path d="M60 70 C40 70 30 52 34 40 C50 42 60 54 60 70Z" fill={MATCHA} />
        <path d="M60 62 C78 62 90 46 86 32 C70 34 60 46 60 62Z" fill={MATCHA} opacity={0.8} />
      </motion.g>
    </svg>
  );
}

/** Vignette illustrée de chaque monde (en-têtes du parcours). */
export function WorldVignette({ slug, size = 72 }: { slug: string; size?: number }) {
  const scene = VIGNETTES[slug] ?? VIGNETTES.default;
  return (
    <svg viewBox="0 0 80 80" width={size} height={size} aria-hidden="true" className="shrink-0">
      <rect width="80" height="80" rx="20" fill="var(--surface-2)" />
      {scene}
    </svg>
  );
}

const glyph = (t: string, x: number, y: number, size: number, fill: string = INK) => (
  <text x={x} y={y} fontSize={size} fontWeight="900" textAnchor="middle" fill={fill} className="jp">
    {t}
  </text>
);

const VIGNETTES: Record<string, React.ReactNode> = {
  // Hiragana : pinceau et trait d'encre
  'n5-w1': (
    <g>
      {glyph('あ', 32, 52, 34)}
      <path d="M50 18 L66 50" stroke="#8A5A2B" strokeWidth="5" strokeLinecap="round" />
      <path d="M66 50 L70 60 L62 56Z" fill={INK} />
    </g>
  ),
  // Katakana : lanterne
  'n5-w2': (
    <g>
      <path d="M40 10 V16" stroke={INK} strokeWidth="3" />
      <rect x="28" y="16" width="24" height="5" rx="2" fill={INK} />
      <ellipse cx="40" cy="42" rx="20" ry="22" fill={BENI} />
      <rect x="28" y="62" width="24" height="5" rx="2" fill={INK} />
      {glyph('ア', 40, 51, 22, '#FFFFFF')}
    </g>
  ),
  // Se présenter : deux bulles
  'n5-w3': (
    <g>
      <rect x="8" y="14" width="40" height="26" rx="10" fill="var(--surface)" stroke={INK} strokeWidth="2.5" />
      <path d="M18 40 L16 48 L26 40Z" fill="var(--surface)" stroke={INK} strokeWidth="2.5" strokeLinejoin="round" />
      {glyph('はい', 28, 33, 13)}
      <rect x="34" y="40" width="38" height="24" rx="10" fill={GOLD} />
      {glyph('どうも', 53, 57, 11, '#2a1a00')}
    </g>
  ),
  // Premières phrases : livre ouvert
  'n5-w4': (
    <g>
      <path d="M10 24 Q25 18 40 24 V62 Q25 56 10 62Z" fill="var(--surface)" stroke={INK} strokeWidth="2.5" />
      <path d="M70 24 Q55 18 40 24 V62 Q55 56 70 62Z" fill="var(--surface)" stroke={INK} strokeWidth="2.5" />
      <path d="M17 34 H33 M17 42 H31 M47 34 H63 M47 42 H61 M47 50 H58" stroke="var(--ink-soft)" strokeWidth="2.5" strokeLinecap="round" />
    </g>
  ),
  // Nombres : boulier
  'n5-w5': (
    <g>
      <rect x="10" y="16" width="60" height="48" rx="6" fill="none" stroke="#8A5A2B" strokeWidth="4" />
      {[28, 40, 52].map((y) => (
        <g key={y}>
          <path d={`M12 ${y} H68`} stroke="#8A5A2B" strokeWidth="2" />
          {[20, 30, 52, 62].map((x, i) => (
            <circle key={x} cx={x} cy={y} r="5" fill={i < 2 ? BENI : GOLD} />
          ))}
        </g>
      ))}
    </g>
  ),
  // Verbes : bol de riz et baguettes
  'n5-w6': (
    <g>
      <path d="M50 12 L30 44 M60 14 L38 46" stroke="#8A5A2B" strokeWidth="3.5" strokeLinecap="round" />
      <path d="M12 42 H68 Q66 66 40 66 Q14 66 12 42Z" fill={BENI} />
      <path d="M14 42 Q40 26 66 42Z" fill="#FFFFFF" />
      <path d="M22 54 H58" stroke="#FFFFFF" strokeWidth="2" opacity={0.6} />
    </g>
  ),
  // Kanji : rouleau
  'n5-w7': (
    <g>
      <rect x="18" y="10" width="44" height="60" fill="var(--surface)" stroke={INK} strokeWidth="2.5" />
      <rect x="14" y="6" width="52" height="7" rx="3" fill="#8A5A2B" />
      <rect x="14" y="67" width="52" height="7" rx="3" fill="#8A5A2B" />
      {glyph('字', 40, 52, 30)}
    </g>
  ),
  // Conversations : échoppe avec rideau noren
  'n5-w8': (
    <g>
      <path d="M8 22 L40 8 L72 22Z" fill={INK} />
      <rect x="12" y="22" width="56" height="10" fill={BENI} />
      {[16, 30, 44, 58].map((x) => (
        <rect key={x} x={x} y="32" width="10" height="16" fill={BENI} opacity={0.85} />
      ))}
      <rect x="14" y="48" width="52" height="22" fill="var(--surface)" stroke={INK} strokeWidth="2" />
      {glyph('店', 40, 66, 16)}
    </g>
  ),
  // Examen blanc : torii et rouleau
  'n5-final': (
    <g>
      <path d="M8 18 Q40 10 72 18 L72 24 Q40 16 8 24Z" fill={BENI} />
      <rect x="14" y="28" width="52" height="5" fill={BENI} />
      <rect x="18" y="22" width="6" height="50" fill={BENI} />
      <rect x="56" y="22" width="6" height="50" fill={BENI} />
      <rect x="30" y="38" width="20" height="28" rx="2" fill="var(--surface)" stroke={INK} strokeWidth="2" />
      {glyph('模', 40, 58, 14)}
    </g>
  ),
  // N4 · forme en て : deux actions reliées
  'n4-w1': (
    <g>
      <circle cx="20" cy="40" r="12" fill={GOLD} />
      <circle cx="60" cy="40" r="12" fill={MATCHA} />
      <path d="M32 40 H48" stroke={INK} strokeWidth="4" strokeLinecap="round" />
      <path d="M44 34 L50 40 L44 46" stroke={INK} strokeWidth="4" fill="none" strokeLinecap="round" strokeLinejoin="round" />
      {glyph('て', 40, 70, 16)}
    </g>
  ),
  // N4 · permis ou interdit : panneaux ○ et ✕
  'n4-w2': (
    <g>
      <circle cx="24" cy="38" r="14" fill="none" stroke={MATCHA} strokeWidth="6" />
      <path d="M46 26 L68 50 M68 26 L46 50" stroke={BENI} strokeWidth="6" strokeLinecap="round" />
      <path d="M24 58 V70 M57 58 V70" stroke={INK} strokeWidth="3" />
    </g>
  ),
  // N4 · expériences et projets : valise de voyage
  'n4-w3': (
    <g>
      <rect x="30" y="16" width="20" height="10" rx="4" fill="none" stroke={INK} strokeWidth="3" />
      <rect x="14" y="24" width="52" height="40" rx="8" fill={BENI} />
      <path d="M14 38 H66" stroke="#FFFFFF" strokeWidth="3" opacity={0.6} />
      <circle cx="54" cy="52" r="6" fill={GOLD} />
      <circle cx="24" cy="70" r="3" fill={INK} />
      <circle cx="56" cy="70" r="3" fill={INK} />
    </g>
  ),
  default: glyph('道', 40, 52, 30),
};
