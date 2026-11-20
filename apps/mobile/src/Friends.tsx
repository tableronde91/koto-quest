import { ReactNode, useState } from 'react';
import { Text, TextInput, View } from 'react-native';
import { useRouter } from 'expo-router';
import { useQueryClient } from '@tanstack/react-query';
import type { FriendDto } from '@koto/shared';
import { del, post } from './api';
import { useFriends } from './hooks';
import { RankBadge } from './RankBadge';
import { C } from './theme';
import { Button, Card, ErrorBox, H2, P } from './ui';
import { T } from './i18n';

function useFriendActions(onOpen: (id: string) => void) {
  const qc = useQueryClient();
  const [err, setErr] = useState<unknown>(null);
  const [msg, setMsg] = useState<string | null>(null);
  const refresh = () => {
    void qc.invalidateQueries({ queryKey: ['friends'] });
    void qc.invalidateQueries({ queryKey: ['duels'] });
  };
  const act = async (fn: () => Promise<unknown>) => {
    setErr(null);
    setMsg(null);
    try {
      await fn();
    } catch (e) {
      setErr(e);
    }
  };
  const challenge = (f: FriendDto) =>
    act(async () => onOpen((await post<{ duelId: string }>('/duels/challenges', { userId: f.player.userId })).duelId));
  return { err, msg, setMsg, refresh, act, challenge };
}

function FriendRow({ f, children }: { f: FriendDto; children: ReactNode }) {
  return (
    <View testID="friend" style={{ flexDirection: 'row', alignItems: 'center', gap: 10 }}>
      <View>
        <RankBadge rank={f.player.rank} size={40} />
        <View style={{ position: 'absolute', right: -2, bottom: -2, width: 14, height: 14, borderRadius: 7, borderWidth: 2, borderColor: C.surface, backgroundColor: f.online ? C.ok : C.line }} />
      </View>
      <View style={{ flex: 1 }}>
        <Text style={{ fontWeight: '800', color: C.ink }}>{f.player.name}</Text>
        <Text style={{ fontSize: 12, color: f.online ? C.ok : C.inkSoft, fontWeight: f.online ? '700' : '400' }}>
          {f.online ? T('En ligne') : T('Hors ligne')}
          <Text style={{ color: C.inkSoft, fontWeight: '400' }}> · {T('{0} V – {1} D', [f.record.wins, f.record.losses])}</Text>
        </Text>
      </View>
      {children}
    </View>
  );
}

/** Profil : code à partager, ajout par code, demandes, liste d'amis avec défi et retrait. */
export function FriendsManager({ code }: { code: string }) {
  const router = useRouter();
  const { data } = useFriends();
  const { err, msg, setMsg, refresh, act, challenge } = useFriendActions((id) => router.push(`/duel/${id}`));
  const [input, setInput] = useState('');
  const [confirm, setConfirm] = useState<string | null>(null);
  const friends = data?.friends ?? [];

  return (
    <Card style={{ gap: 12 }} testID="friends">
      <View style={{ flexDirection: 'row', alignItems: 'center', gap: 12 }}>
        <View style={{ width: 52, height: 52, borderRadius: 14, backgroundColor: '#3FA7A0', alignItems: 'center', justifyContent: 'center' }}>
          <Text style={{ fontSize: 28, fontWeight: '900', color: '#fff' }}>友</Text>
        </View>
        <View style={{ flex: 1 }}>
          <H2>{T('Mes amis')}</H2>
          <P soft style={{ fontSize: 14 }}>
            {friends.length ? T('{0} en ligne sur {1}', [friends.filter((f) => f.online).length, friends.length]) : T('Duel amical, sans effet sur le classement.')}
          </P>
        </View>
      </View>
      <P>{T('Ton code de duelliste :')} <Text testID="my-code" style={{ fontWeight: '900', letterSpacing: 1 }}>{code}</Text></P>
      <View style={{ flexDirection: 'row', gap: 8 }}>
        <TextInput
          value={input}
          onChangeText={setInput}
          autoCapitalize="characters"
          autoCorrect={false}
          placeholder={T('Code d’un ami (KQ-…)')}
          placeholderTextColor={C.inkSoft}
          accessibilityLabel={T('Code de duelliste d’un ami')}
          style={{ flex: 1, borderWidth: 2, borderColor: C.line, borderRadius: 14, paddingHorizontal: 12, fontSize: 16, color: C.ink, minHeight: 50 }}
        />
        <Button
          label={T('Ajouter')}
          disabled={!input.trim()}
          onPress={() => act(async () => {
            await post('/friends', { code: input.trim() });
            setInput('');
            setMsg(T('Demande envoyée.'));
            refresh();
          })}
        />
      </View>
      {msg && <P style={{ color: C.ok, fontWeight: '700' }}>{msg}</P>}
      {err != null && <ErrorBox error={err} />}

      {data?.incoming.map((r) => (
        <View key={r.id} style={{ flexDirection: 'row', alignItems: 'center', gap: 10 }}>
          <RankBadge rank={r.player.rank} size={36} />
          <P style={{ flex: 1 }}>{T('{0} veut être ton ami', [r.player.name])}</P>
          <Button label={T('Accepter')} tone="gold" onPress={() => act(async () => { await post(`/friends/${r.id}/accept`); refresh(); })} />
          <Button label={T('Refuser')} tone="quiet" onPress={() => act(async () => { await del(`/friends/${r.id}`); refresh(); })} />
        </View>
      ))}
      {data?.outgoing.map((r) => (
        <View key={r.id} style={{ flexDirection: 'row', alignItems: 'center', gap: 10 }}>
          <P soft style={{ flex: 1, fontSize: 14 }}>{T('Demande envoyée à {0}, en attente.', [r.player.name])}</P>
          <Button label={T('Annuler')} tone="quiet" onPress={() => act(async () => { await del(`/friends/${r.id}`); refresh(); })} />
        </View>
      ))}

      {data && friends.length === 0 && <P soft style={{ fontSize: 14 }}>{T('Pas encore d’ami : partage ton code ou entre le leur.')}</P>}
      {friends.map((f) => (
        <FriendRow key={f.id} f={f}>
          {confirm === f.id ? (
            <>
              <Button label={T('Retirer ?')} tone="quiet" style={{ borderColor: C.ko }} onPress={() => act(async () => { await del(`/friends/${f.id}`); setConfirm(null); refresh(); })} />
              <Button label="✕" tone="quiet" onPress={() => setConfirm(null)} />
            </>
          ) : (
            <>
              {f.pendingDuelId ? (
                <Button label={T('Voir le défi')} tone="quiet" onPress={() => router.push(`/duel/${f.pendingDuelId}`)} />
              ) : (
                <Button label={T('Défier')} tone={f.online ? 'gold' : 'primary'} onPress={() => challenge(f)} />
              )}
              <Button label="⋯" tone="quiet" onPress={() => setConfirm(f.id)} />
            </>
          )}
        </FriendRow>
      ))}
    </Card>
  );
}

/** Dojo : les amis à défier (en ligne d'abord) ; ajout et gestion dans le profil. */
export function FriendsQuick({ onOpen }: { onOpen: (id: string) => void }) {
  const router = useRouter();
  const { data } = useFriends();
  const { err, challenge } = useFriendActions(onOpen);
  const friends = [...(data?.friends ?? [])].sort((a, b) => Number(b.online) - Number(a.online)).slice(0, 5);
  return (
    <Card style={{ gap: 12 }} testID="duel-friends">
      <View style={{ flexDirection: 'row', alignItems: 'center', gap: 12 }}>
        <View style={{ width: 52, height: 52, borderRadius: 14, backgroundColor: '#3FA7A0', alignItems: 'center', justifyContent: 'center' }}>
          <Text style={{ fontSize: 28, fontWeight: '900', color: '#fff' }}>友</Text>
        </View>
        <View style={{ flex: 1 }}>
          <H2>{T('Défier un ami')}</H2>
          <P soft style={{ fontSize: 14 }}>{T('Duel amical, sans effet sur le classement.')}</P>
        </View>
      </View>
      {data && friends.length === 0 && <P soft style={{ fontSize: 14 }}>{T('Tu n’as pas encore d’amis. Ajoute-les depuis ton profil avec leur code de duelliste.')}</P>}
      {friends.map((f) => (
        <FriendRow key={f.id} f={f}>
          {f.pendingDuelId ? (
            <Button label={T('Voir le défi')} tone="quiet" onPress={() => onOpen(f.pendingDuelId!)} />
          ) : (
            <Button label={T('Défier')} tone={f.online ? 'gold' : 'primary'} onPress={() => challenge(f)} />
          )}
        </FriendRow>
      ))}
      {err != null && <ErrorBox error={err} />}
      <Button label={T('Gérer mes amis')} tone="quiet" onPress={() => router.push('/profile')} />
    </Card>
  );
}
