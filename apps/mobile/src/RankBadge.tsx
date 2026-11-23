import { Text, View } from 'react-native';
import { duelTierGlyph, type DuelRankDto } from '@koto/shared';
import { useRankLabel, useStudyLang } from './study';

/** Écusson de rang : l'idéogramme de la division dans un disque de sa couleur. */
export function RankBadge({ rank, size = 56 }: { rank: DuelRankDto; size?: number }) {
  const { lang } = useStudyLang();
  const RL = useRankLabel();
  const glyph = duelTierGlyph(rank.tierId, rank.jp, lang);
  return (
    <View accessibilityLabel={RL(rank)} style={{ width: size, height: size, borderRadius: size / 2, backgroundColor: rank.color, borderWidth: 3, borderColor: '#ffffffaa', alignItems: 'center', justifyContent: 'center' }}>
      <Text style={{ color: '#fff', fontWeight: '900', fontSize: size * ([...glyph].length > 2 ? 0.26 : [...glyph].length > 1 ? 0.3 : 0.42) }}>{glyph}</Text>
    </View>
  );
}
