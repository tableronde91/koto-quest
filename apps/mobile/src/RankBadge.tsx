import { Text, View } from 'react-native';
import type { DuelRankDto } from '@koto/shared';

/** Écusson de rang : l'idéogramme de la division dans un disque de sa couleur. */
export function RankBadge({ rank, size = 56 }: { rank: DuelRankDto; size?: number }) {
  return (
    <View accessibilityLabel={rank.label} style={{ width: size, height: size, borderRadius: size / 2, backgroundColor: rank.color, borderWidth: 3, borderColor: '#ffffffaa', alignItems: 'center', justifyContent: 'center' }}>
      <Text style={{ color: '#fff', fontWeight: '900', fontSize: size * ([...rank.jp].length > 1 ? 0.3 : 0.42) }}>{rank.jp}</Text>
    </View>
  );
}
