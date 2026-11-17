import { useState } from 'react';
import { Pressable, Text, View } from 'react-native';
import { usePathname } from 'expo-router';
import { put } from './api';
import { LOCALES, T, setLocale, useLocale, type Locale } from './i18n';
import { C } from './theme';

/**
 * Choix de la langue (français / anglais). Connecté, le choix est aussi enregistré sur le compte
 * (rappels et e-mails dans la même langue, et même langue sur le web).
 */
export function LanguageSwitch({ saveToAccount = false }: { saveToAccount?: boolean }) {
  const locale = useLocale();
  const path = usePathname();
  const [busy, setBusy] = useState(false);
  async function choose(next: Locale) {
    if (next === locale || busy) return;
    setBusy(true);
    try {
      if (saveToAccount) await put('/me/preferences', { locale: next }).catch(() => undefined);
    } finally {
      setBusy(false);
      await setLocale(next, path);
    }
  }
  return (
    <View accessibilityRole="radiogroup" accessibilityLabel={T('Langue')} style={{ flexDirection: 'row', alignSelf: 'center', backgroundColor: C.surface, borderWidth: 2, borderColor: C.line, borderRadius: 99, padding: 3 }}>
      {LOCALES.map((l) => (
        <Pressable key={l.code} accessibilityRole="radio" accessibilityState={{ checked: l.code === locale }} accessibilityLabel={l.label} onPress={() => choose(l.code)} style={{ paddingHorizontal: 14, paddingVertical: 6, borderRadius: 99, backgroundColor: l.code === locale ? C.ink : 'transparent' }}>
          <Text style={{ fontWeight: '800', color: l.code === locale ? C.paper : C.inkSoft }}>{l.label}</Text>
        </Pressable>
      ))}
    </View>
  );
}
