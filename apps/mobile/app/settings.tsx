import { useEffect, useState } from 'react';
import { Pressable, Switch, Text, View } from 'react-native';
import { useRouter } from 'expo-router';
import { useQueryClient } from '@tanstack/react-query';
import { STUDY_LANGUAGES, type MeDto, type NotificationPrefsDto, type StudyLanguage } from '@koto/shared';
import { put } from '../src/api';
import { useAuth } from '../src/auth';
import { API_URL } from '../src/config';
import { useNotifPrefs } from '../src/hooks';
import { cancelReminders, notificationsSupported, requestPermission, scheduleReminders } from '../src/notifications';
import { C } from '../src/theme';
import { Button, Card, H1, H2, P, Screen } from '../src/ui';
import { LanguageSwitch } from '../src/LanguageSwitch';
import { T, plural } from '../src/i18n';

const hhmm = (m: number) => `${String(Math.floor(m / 60)).padStart(2, '0')}:${String(m % 60).padStart(2, '0')}`;

export default function Settings() {
  const { me, logout } = useAuth();
  const router = useRouter();
  const qc = useQueryClient();
  const { data: prefs } = useNotifPrefs();
  const [busy, setBusy] = useState(false);
  const [msg, setMsg] = useState<string | null>(null);

  // À chaque ouverture, on resynchronise les rappels du téléphone avec les créneaux du serveur.
  useEffect(() => {
    if (prefs) scheduleReminders(prefs).catch(() => undefined);
  }, [prefs]);

  async function toggle(on: boolean) {
    setBusy(true);
    setMsg(null);
    try {
      if (on && notificationsSupported() && !(await requestPermission())) {
        setMsg(T('Autorisation refusée : active les notifications de Koto Quest dans les réglages du téléphone.'));
        return;
      }
      const next = await put<NotificationPrefsDto>('/notifications/preferences', on ? { consent: true, enabled: true } : { enabled: false });
      qc.setQueryData(['notif-prefs'], next);
      if (on) {
        const n = await scheduleReminders(next);
        setMsg(notificationsSupported() ? plural(n, '{0} rappel programmé chaque jour.', '{0} rappels programmés chaque jour.') : T('Rappels enregistrés (les notifications s’affichent sur le téléphone).'));
      } else {
        await cancelReminders();
        setMsg(T('Rappels désactivés sur ce téléphone.'));
      }
    } catch (e) {
      setMsg(e instanceof Error ? e.message : T('Erreur'));
    } finally {
      setBusy(false);
    }
  }

  const [switching, setSwitching] = useState(false);
  async function chooseStudy(lang: StudyLanguage) {
    setSwitching(true);
    try {
      const next = await put<MeDto>('/me/preferences', { studyLanguage: lang });
      qc.setQueryData(['me'], next);
      void qc.invalidateQueries({ predicate: (q) => q.queryKey[0] !== 'me' });
    } catch (e) {
      setMsg(e instanceof Error ? e.message : T('Erreur'));
    } finally {
      setSwitching(false);
    }
  }

  const on = !!prefs?.consent && !!prefs?.enabled;
  return (
    <Screen>
      <View style={{ flexDirection: 'row', alignItems: 'center', gap: 8 }}>
        <Pressable accessibilityRole="button" accessibilityLabel={T('Retour')} onPress={() => (router.canGoBack() ? router.back() : router.replace('/profile'))} hitSlop={12}>
          <Text style={{ fontSize: 26, color: C.ink, fontWeight: '800' }}>‹</Text>
        </Pressable>
        <H1>{T('Réglages')}</H1>
      </View>

      <H2>{T('Langue')}</H2>
      <LanguageSwitch saveToAccount />

      <H2>{T('Langue étudiée')}</H2>
      <View accessibilityRole="radiogroup" accessibilityLabel={T('Langue étudiée')} style={{ flexDirection: 'row', flexWrap: 'wrap', gap: 8 }}>
        {STUDY_LANGUAGES.map((l) => {
          const active = (me?.preferences.studyLanguage ?? 'ja') === l.code;
          return (
            <Pressable key={l.code} testID={`study-${l.code}`} accessibilityRole="radio" accessibilityState={{ checked: active, disabled: switching }} accessibilityLabel={`${T(l.name)} · ${l.native}`} disabled={switching} onPress={() => !active && chooseStudy(l.code)} style={{ paddingHorizontal: 14, paddingVertical: 8, borderRadius: 99, borderWidth: 2, borderColor: active ? C.ink : C.line, backgroundColor: active ? C.ink : C.surface }}>
              <Text style={{ fontWeight: '800', color: active ? C.paper : C.inkSoft }}>{`${T(l.name)} · ${l.native}`}</Text>
            </Pressable>
          );
        })}
      </View>
      <P soft style={{ fontSize: 13 }}>{T('Parcours, révisions, lecture et caractères suivent la langue choisie. Ta progression dans l’autre langue est conservée.')}</P>

      <H2>{T('Rappels sur ce téléphone')}</H2>
      <Card style={{ gap: 10 }}>
        <View style={{ flexDirection: 'row', alignItems: 'center', gap: 12 }}>
          <Text style={{ flex: 1, fontSize: 16, color: C.ink }}>{T('Recevoir un petit défi aux bons moments')}</Text>
          <Switch accessibilityLabel={T('Recevoir les rappels')} value={on} disabled={busy || !prefs} onValueChange={toggle} trackColor={{ true: C.ok, false: C.line }} />
        </View>
        {on && prefs && prefs.slots.length > 0 && <P soft>{T('Créneaux du jour : {0} (ajustés par Koto Quest selon tes révisions et ta plage horaire).', [prefs.slots.map(hhmm).join(', ')])}</P>}
        {msg && <P>{msg}</P>}
        <P soft style={{ fontSize: 12 }}>{T('La fréquence, la plage horaire et la pause se règlent aussi depuis la version web ; ce téléphone suit les mêmes réglages.')}</P>
      </Card>

      <H2>{T('Compte')}</H2>
      <P soft>{T('Connecté avec {0}', [me?.email ?? ''])}</P>
      <Button tone="quiet" label={T('Se déconnecter')} onPress={async () => { await cancelReminders(); await logout(); }} />
      <P soft style={{ fontSize: 12, textAlign: 'center' }}>{T('Serveur : {0}', [API_URL])}</P>
    </Screen>
  );
}
