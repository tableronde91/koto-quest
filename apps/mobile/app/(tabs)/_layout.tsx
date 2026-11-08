import { Tabs } from 'expo-router';
import { ColorValue, Text } from 'react-native';
import { useReviewSummary } from '../../src/hooks';
import { C } from '../../src/theme';

const icon = (glyph: string) => ({ color }: { color: ColorValue }) => <Text style={{ fontSize: 20, fontWeight: '900', color }}>{glyph}</Text>;

export default function TabsLayout() {
  const { data } = useReviewSummary();
  return (
    <Tabs screenOptions={{ headerShown: false, tabBarActiveTintColor: C.ink, tabBarInactiveTintColor: C.inkSoft, tabBarStyle: { backgroundColor: C.surface, borderTopColor: C.line, height: 64, paddingBottom: 8 }, tabBarLabelStyle: { fontWeight: '700' } }}>
      <Tabs.Screen name="index" options={{ title: 'Accueil', tabBarIcon: icon('家') }} />
      <Tabs.Screen name="path" options={{ title: 'Parcours', tabBarIcon: icon('島') }} />
      <Tabs.Screen name="reviews" options={{ title: 'Révisions', tabBarIcon: icon('復'), tabBarBadge: data?.due ? data.due : undefined, tabBarBadgeStyle: { backgroundColor: C.gold, color: '#2a1a00' } }} />
      <Tabs.Screen name="settings" options={{ title: 'Réglages', tabBarIcon: icon('設') }} />
    </Tabs>
  );
}
