import { Tabs } from 'expo-router';
import { ColorValue, Text } from 'react-native';
import { useReviewSummary } from '../../src/hooks';
import { C } from '../../src/theme';
import { T } from '../../src/i18n';
import { useDecor } from '../../src/study';

const icon = (glyph: string) => ({ color }: { color: ColorValue }) => <Text style={{ fontSize: 20, fontWeight: '900', color }}>{glyph}</Text>;

export default function TabsLayout() {
  const { data } = useReviewSummary();
  const D = useDecor();
  return (
    <Tabs backBehavior="history" screenOptions={{ headerShown: false, tabBarActiveTintColor: C.ink, tabBarInactiveTintColor: C.inkSoft, tabBarStyle: { backgroundColor: C.surface, borderTopColor: C.line, height: 64, paddingBottom: 8 }, tabBarLabelStyle: { fontWeight: '700', fontSize: 11 } }}>
      <Tabs.Screen name="index" options={{ title: T('Accueil'), tabBarIcon: icon(D('home')) }} />
      <Tabs.Screen name="path" options={{ title: T('Parcours'), tabBarIcon: icon(D('island')) }} />
      <Tabs.Screen name="learn" options={{ title: T('Apprendre'), tabBarIcon: icon(D('learn')), tabBarBadge: data?.due ? data.due : undefined, tabBarBadgeStyle: { backgroundColor: C.gold, color: '#2a1a00' } }} />
      <Tabs.Screen name="games" options={{ title: T('Jouer'), tabBarIcon: icon(D('play')) }} />
      <Tabs.Screen name="profile" options={{ title: T('Profil'), tabBarIcon: icon(D('me')) }} />
    </Tabs>
  );
}
