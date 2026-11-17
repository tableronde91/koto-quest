import { useState } from 'react';
import { Pressable, Text, View } from 'react-native';
import { useQueryClient } from '@tanstack/react-query';
import type { JlptCode, OnboardingInput, SelfLevel } from '@koto/shared';
import { put } from '../src/api';
import { C } from '../src/theme';
import { Button, H1, H2, P, Screen } from '../src/ui';
import { T, getLocale } from '../src/i18n';

const LEVELS = (): { value: SelfLevel; label: string; hint: string }[] => [
  { value: 'beginner', label: T('Je pars de zéro'), hint: T('On commence par les hiragana.') },
  { value: 'kana', label: T('Je lis les kana'), hint: T('On passe aux premières phrases.') },
  { value: 'basics', label: T('Je connais des bases'), hint: T('Les premières îles restent ouvertes.') },
  { value: 'n5', label: T('J’ai le niveau N5'), hint: T('Vise le N4 juste en dessous.') },
];
const MINUTES = [10, 15, 20, 30];
const TARGETS: { code: JlptCode; hint: string }[] = [
  { code: 'N5', hint: 'Débutant' },
  { code: 'N4', hint: 'Élémentaire' },
  { code: 'N3', hint: 'Intermédiaire' },
  { code: 'N2', hint: 'Avancé' },
  { code: 'N1', hint: 'Expert' },
];

function Choice({ selected, label, hint, onPress }: { selected: boolean; label: string; hint?: string; onPress: () => void }) {
  return (
    <Pressable accessibilityRole="radio" accessibilityState={{ selected }} onPress={onPress} style={{ borderWidth: 2, borderColor: selected ? C.ink : C.line, backgroundColor: C.surface, borderRadius: 16, padding: 14 }}>
      <Text style={{ fontWeight: '800', fontSize: 16, color: C.ink }}>{label}</Text>
      {hint && <Text style={{ color: C.inkSoft }}>{hint}</Text>}
    </Pressable>
  );
}

/** Profil en un écran : niveau actuel, niveau visé, temps par jour. */
export default function Onboarding() {
  const qc = useQueryClient();
  const [selfLevel, setSelf] = useState<SelfLevel>('beginner');
  const [target, setTarget] = useState<JlptCode>('N5');
  const [minutes, setMinutes] = useState(15);
  const [busy, setBusy] = useState(false);
  const [error, setError] = useState<string | null>(null);

  async function save() {
    setBusy(true);
    setError(null);
    try {
      const body: OnboardingInput = { selfLevel, targetLevel: target, minutesPerDay: minutes, difficultAreas: [], reminderMode: 'normal', timezone: Intl.DateTimeFormat().resolvedOptions().timeZone, locale: getLocale() };
      await put('/me/onboarding', body);
      await qc.invalidateQueries();
    } catch (e) {
      setError(e instanceof Error ? e.message : T('Erreur'));
    } finally {
      setBusy(false);
    }
  }

  return (
    <Screen>
      <H1>{T('Bienvenue dans l’archipel !')}</H1>
      <P soft>{T('Trois questions pour adapter ton programme.')}</P>
      <H2>{T('Où en es-tu en japonais ?')}</H2>
      <View style={{ gap: 8 }}>{LEVELS().map((l) => <Choice key={l.value} selected={selfLevel === l.value} label={l.label} hint={l.hint} onPress={() => { setSelf(l.value); if (l.value === 'n5') setTarget('N4'); }} />)}</View>
      <H2>{T('Quel niveau vises-tu ?')}</H2>
      <View style={{ flexDirection: 'row', flexWrap: 'wrap', gap: 8 }}>
        {TARGETS.map((c) => <View key={c.code} style={{ width: '31%', flexGrow: 1 }}><Choice selected={target === c.code} label={c.code} hint={T(c.hint)} onPress={() => setTarget(c.code)} /></View>)}
      </View>
      <H2>{T('Combien de temps par jour ?')}</H2>
      <View style={{ flexDirection: 'row', gap: 8 }}>
        {MINUTES.map((m) => <View key={m} style={{ flex: 1 }}><Choice selected={minutes === m} label={T('{0} min', [m])} onPress={() => setMinutes(m)} /></View>)}
      </View>
      {error && <Text style={{ color: C.ko, fontWeight: '700' }}>{error}</Text>}
      <Button tone="gold" label={busy ? '…' : T('Commencer l’aventure')} disabled={busy} onPress={save} />
    </Screen>
  );
}
