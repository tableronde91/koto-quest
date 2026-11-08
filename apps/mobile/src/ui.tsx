import { ReactNode } from 'react';
import { ActivityIndicator, Pressable, ScrollView, StyleProp, StyleSheet, Text, TextStyle, View, ViewStyle } from 'react-native';
import { SafeAreaView } from 'react-native-safe-area-context';
import { C, R } from './theme';

export function Screen({ children, scroll = true, padded = true }: { children: ReactNode; scroll?: boolean; padded?: boolean }) {
  const inner = <View style={[padded && { padding: 18, gap: 18 }, { flexGrow: 1 }]}>{children}</View>;
  return (
    <SafeAreaView style={{ flex: 1, backgroundColor: C.paper }} edges={['top', 'left', 'right']}>
      {scroll ? <ScrollView contentContainerStyle={{ flexGrow: 1, paddingBottom: 32 }} keyboardShouldPersistTaps="handled">{inner}</ScrollView> : inner}
    </SafeAreaView>
  );
}

export function H1({ children, style }: { children: ReactNode; style?: StyleProp<TextStyle> }) {
  return <Text accessibilityRole="header" style={[s.h1, style]}>{children}</Text>;
}
export function H2({ children }: { children: ReactNode }) {
  return <Text accessibilityRole="header" style={s.h2}>{children}</Text>;
}
export function P({ children, soft, style }: { children: ReactNode; soft?: boolean; style?: StyleProp<TextStyle> }) {
  return <Text style={[s.p, soft && { color: C.inkSoft }, style]}>{children}</Text>;
}

export function Card({ children, style }: { children: ReactNode; style?: StyleProp<ViewStyle> }) {
  return <View style={[s.card, style]}>{children}</View>;
}

export function Button({ label, onPress, tone = 'primary', disabled, style, testID }: { label: string; onPress: () => void; tone?: 'primary' | 'gold' | 'quiet'; disabled?: boolean; style?: StyleProp<ViewStyle>; testID?: string }) {
  const bg = tone === 'gold' ? C.gold : tone === 'quiet' ? 'transparent' : C.ink;
  const fg = tone === 'gold' ? '#2a1a00' : tone === 'quiet' ? C.ink : C.paper;
  return (
    <Pressable
      testID={testID}
      accessibilityRole="button"
      accessibilityState={{ disabled: !!disabled }}
      disabled={disabled}
      onPress={onPress}
      style={({ pressed }) => [s.btn, { backgroundColor: bg, opacity: disabled ? 0.5 : 1, transform: [{ translateY: pressed ? 1 : 0 }] }, tone === 'quiet' && { borderWidth: 2, borderColor: C.line }, style]}
    >
      <Text style={[s.btnText, { color: fg }]}>{label}</Text>
    </Pressable>
  );
}

export function ProgressBar({ value, max, color = C.ink, label }: { value: number; max: number; color?: string; label: string }) {
  const pct = max > 0 ? Math.min(100, (value / max) * 100) : 0;
  return (
    <View accessibilityRole="progressbar" accessibilityLabel={label} accessibilityValue={{ min: 0, max, now: value }} style={s.bar}>
      <View style={{ width: `${pct}%`, height: '100%', backgroundColor: color, borderRadius: 99 }} />
    </View>
  );
}

export function Loading({ label }: { label?: string }) {
  return (
    <View style={{ flex: 1, alignItems: 'center', justifyContent: 'center', gap: 12, padding: 24, backgroundColor: C.paper }}>
      <ActivityIndicator color={C.ink} size="large" />
      {label && <P soft>{label}</P>}
    </View>
  );
}

export function ErrorBox({ error, onRetry }: { error: unknown; onRetry?: () => void }) {
  return (
    <Card style={{ borderColor: C.ko, gap: 10 }}>
      <P style={{ fontWeight: '700', color: C.ko }}>{error instanceof Error ? error.message : 'Une erreur est survenue.'}</P>
      {onRetry && <Button label="Réessayer" tone="quiet" onPress={onRetry} />}
    </Card>
  );
}

export function Seal({ glyph, size = 44, color = C.seal }: { glyph: string; size?: number; color?: string }) {
  return (
    <View style={{ width: size, height: size, borderRadius: size / 2, backgroundColor: color, alignItems: 'center', justifyContent: 'center' }}>
      <Text style={{ color: '#fff', fontWeight: '900', fontSize: size * 0.48 }}>{glyph}</Text>
    </View>
  );
}

export const s = StyleSheet.create({
  h1: { fontSize: 28, fontWeight: '800', color: C.ink },
  h2: { fontSize: 20, fontWeight: '800', color: C.ink },
  p: { fontSize: 16, color: C.ink, lineHeight: 22 },
  card: { backgroundColor: C.surface, borderRadius: R.md, borderWidth: 1, borderColor: C.line, padding: 16 },
  btn: { minHeight: 50, borderRadius: 14, paddingHorizontal: 20, alignItems: 'center', justifyContent: 'center' },
  btnText: { fontSize: 16, fontWeight: '800' },
  bar: { height: 10, backgroundColor: C.surface2, borderRadius: 99, overflow: 'hidden', flex: 1 },
});
