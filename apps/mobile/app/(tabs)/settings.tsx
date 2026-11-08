import { useEffect, useState } from 'react';
import { Switch, Text, View } from 'react-native';
import { useQueryClient } from '@tanstack/react-query';
import type { NotificationPrefsDto } from '@koto/shared';
import { put } from '../../src/api';
import { useAuth } from '../../src/auth';
import { API_URL } from '../../src/config';
import { useNotifPrefs } from '../../src/hooks';
import { cancelReminders, notificationsSupported, requestPermission, scheduleReminders } from '../../src/notifications';
import { C } from '../../src/theme';
import { Button, Card, H1, H2, P, Screen } from '../../src/ui';

const hhmm = (m: number) => `${String(Math.floor(m / 60)).padStart(2, '0')}:${String(m % 60).padStart(2, '0')}`;

export default function Settings() {
  const { me, logout } = useAuth();
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
        setMsg('Autorisation refusée : active les notifications de Koto Quest dans les réglages du téléphone.');
        return;
      }
      const next = await put<NotificationPrefsDto>('/notifications/preferences', on ? { consent: true, enabled: true } : { enabled: false });
      qc.setQueryData(['notif-prefs'], next);
      if (on) {
        const n = await scheduleReminders(next);
        setMsg(notificationsSupported() ? `${n} rappel${n > 1 ? 's' : ''} programmé${n > 1 ? 's' : ''} chaque jour.` : 'Rappels enregistrés (les notifications s’affichent sur le téléphone).');
      } else {
        await cancelReminders();
        setMsg('Rappels désactivés sur ce téléphone.');
      }
    } catch (e) {
      setMsg(e instanceof Error ? e.message : 'Erreur');
    } finally {
      setBusy(false);
    }
  }

  const on = !!prefs?.consent && !!prefs?.enabled;
  return (
    <Screen>
      <H1>Réglages</H1>
      <Card style={{ gap: 4 }}>
        <Text style={{ fontWeight: '800', fontSize: 18, color: C.ink }}>{me?.displayName}</Text>
        <P soft>{me?.email}</P>
        <P soft>Objectif {me?.preferences.targetLevel} · {me?.preferences.minutesPerDay} min par jour</P>
      </Card>

      <H2>Rappels sur ce téléphone</H2>
      <Card style={{ gap: 10 }}>
        <View style={{ flexDirection: 'row', alignItems: 'center', gap: 12 }}>
          <Text style={{ flex: 1, fontSize: 16, color: C.ink }}>Recevoir un petit défi aux bons moments</Text>
          <Switch accessibilityLabel="Recevoir les rappels" value={on} disabled={busy || !prefs} onValueChange={toggle} trackColor={{ true: C.ok, false: C.line }} />
        </View>
        {on && prefs && prefs.slots.length > 0 && <P soft>Créneaux du jour : {prefs.slots.map(hhmm).join(', ')} (ajustés par Koto Quest selon tes révisions et ta plage horaire).</P>}
        {msg && <P>{msg}</P>}
        <P soft style={{ fontSize: 12 }}>La fréquence, la plage horaire et la pause se règlent aussi depuis la version web ; ce téléphone suit les mêmes réglages.</P>
      </Card>

      <H2>Compte</H2>
      <Button tone="quiet" label="Se déconnecter" onPress={async () => { await cancelReminders(); await logout(); }} />
      <P soft style={{ fontSize: 12, textAlign: 'center' }}>Serveur : {API_URL}</P>
    </Screen>
  );
}
