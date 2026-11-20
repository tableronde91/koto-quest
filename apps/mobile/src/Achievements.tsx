import { useEffect, useRef, useState } from 'react';
import { Pressable, Text, View } from 'react-native';
import { usePathname, useRouter } from 'expo-router';
import { useQueryClient } from '@tanstack/react-query';
import Svg, { Circle, G, Path, Text as SvgText } from 'react-native-svg';
import type { AchievementCheckDto, AchievementDto } from '@koto/shared';
import { post } from './api';
import { useAuth } from './auth';
import { C } from './theme';
import { T } from './i18n';

/** Traduits à l'affichage avec T(). */
export const RARITY_LABEL: Record<AchievementDto['rarity'], string> = { common: 'Courant', rare: 'Rare', epic: 'Épique' };
const RARITY_RING: Record<AchievementDto['rarity'], string> = { common: '#B9835A', rare: '#6E8FB5', epic: C.gold };

/** Médaille d'un succès : idéogramme au centre, anneau de rareté ; grisée avec jauge si verrouillée. */
export function Medal({ a, size = 64 }: { a: Pick<AchievementDto, 'glyph' | 'rarity' | 'unlocked' | 'value' | 'target'>; size?: number }) {
  const ring = RARITY_RING[a.rarity];
  const r = 34;
  const c = 2 * Math.PI * r;
  const pct = a.unlocked ? 1 : Math.min(1, a.value / Math.max(1, a.target));
  return (
    <Svg viewBox="0 0 80 80" width={size} height={size}>
      {a.unlocked && a.rarity !== 'common' && (
        <G fill={ring} opacity={0.35}>
          {Array.from({ length: 12 }, (_, i) => <Path key={i} d="M40 2 L43 12 L37 12Z" transform={`rotate(${i * 30} 40 40)`} />)}
        </G>
      )}
      <Circle cx="40" cy="40" r={r} fill={a.unlocked ? C.surface : C.surface2} stroke={C.line} strokeWidth="5" />
      {pct > 0 && <Circle cx="40" cy="40" r={r} fill="none" stroke={a.unlocked ? ring : C.inkSoft} strokeWidth="5" strokeDasharray={`${c * pct} ${c}`} strokeLinecap="round" transform="rotate(-90 40 40)" />}
      <Circle cx="40" cy="40" r="26" fill={a.unlocked ? ring : 'transparent'} opacity={a.unlocked ? 0.16 : 1} />
      <SvgText x="40" y="51" textAnchor="middle" fontSize="30" fontWeight="900" fill={a.unlocked ? C.ink : C.line}>{a.glyph}</SvgText>
    </Svg>
  );
}

const QUIET = /^\/(lesson|review|boss|exam|games|duel|practice)\b/;

/**
 * Vérifie les succès à chaque changement d'écran (comme le web), hors séance en cours,
 * et affiche les nouveaux succès un par un dans une bannière.
 */
export function AchievementWatcher() {
  const { me } = useAuth();
  const path = usePathname();
  const router = useRouter();
  const qc = useQueryClient();
  const [queue, setQueue] = useState<AchievementDto[]>([]);
  const busy = useRef(false);

  useEffect(() => {
    if (!me?.onboarded || QUIET.test(path) || busy.current) return;
    busy.current = true;
    const t = setTimeout(async () => {
      try {
        const r = await post<AchievementCheckDto>('/achievements/check');
        if (r.unlocked.length) {
          setQueue((q) => [...q, ...r.unlocked]);
          void qc.invalidateQueries({ queryKey: ['achievements'] });
          void qc.invalidateQueries({ queryKey: ['me'] });
          void qc.invalidateQueries({ queryKey: ['dashboard'] });
        }
      } catch {
        /* hors ligne : on réessaiera au prochain écran */
      } finally {
        busy.current = false;
      }
    }, 400);
    return () => {
      clearTimeout(t);
      busy.current = false;
    };
  }, [path, me?.onboarded, qc]);

  const a = queue[0];
  useEffect(() => {
    if (!a) return;
    const t = setTimeout(() => setQueue((q) => q.slice(1)), 5000);
    return () => clearTimeout(t);
  }, [a]);
  if (!a) return null;
  return (
    <View pointerEvents="box-none" style={{ position: 'absolute', left: 12, right: 12, top: 48, zIndex: 50 }}>
      <Pressable
        testID="achievement-toast"
        accessibilityRole="button"
        accessibilityLabel={T('Succès débloqué · {0}', [a.title])}
        onPress={() => {
          setQueue((q) => q.slice(1));
          router.push('/achievements');
        }}
        style={{ flexDirection: 'row', alignItems: 'center', gap: 12, backgroundColor: C.ink, borderRadius: 20, padding: 12, shadowColor: '#000', shadowOpacity: 0.25, shadowRadius: 12, elevation: 6 }}
      >
        <Medal a={a} size={52} />
        <View style={{ flex: 1 }}>
          <Text style={{ color: C.gold, fontWeight: '800', fontSize: 12 }}>{T('Succès débloqué · {0}', [T(RARITY_LABEL[a.rarity])])}</Text>
          <Text style={{ color: C.paper, fontWeight: '800', fontSize: 16 }}>{a.title}</Text>
          <Text style={{ color: C.paper, opacity: 0.8, fontSize: 13 }}>{T('+{0} pièces', [a.coins])}</Text>
        </View>
      </Pressable>
    </View>
  );
}
