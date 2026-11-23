import { useDecor, useRankLabel } from '../../src/study';
import { useEffect, useRef, useState } from 'react';
import { ActivityIndicator, Pressable, Text, View } from 'react-native';
import { useRouter } from 'expo-router';
import { useQueryClient } from '@tanstack/react-query';
import type { DuelInviteDto, DuelQueueDto } from '@koto/shared';
import { DUEL_RULES } from '@koto/learning-engine';
import { api, del, post } from '../../src/api';
import { useDuelLeaderboard, useDuelLobby } from '../../src/hooks';
import { FriendsQuick } from '../../src/Friends';
import { RankBadge } from '../../src/RankBadge';
import { C } from '../../src/theme';
import { Button, Card, ErrorBox, H1, H2, Loading, P, ProgressBar, Screen } from '../../src/ui';
import { T } from '../../src/i18n';

// Traduits à l'affichage avec T()
const RESULT = { win: 'Victoire', loss: 'Défaite', draw: 'Égalité', cancelled: 'Annulé' } as const;
const KIND = { ranked: 'Classé', friendly: 'Amical', practice: 'Entraînement' } as const;

/** Dojo des duels : rang, duel classé, entraînement contre un rōnin, amis, historique et classement. */
export default function DuelLobbyScreen() {
  const RL = useRankLabel();
  const D = useDecor();
  const router = useRouter();
  const qc = useQueryClient();
  const { data, isLoading, error, refetch } = useDuelLobby();
  const [searching, setSearching] = useState<string | null>(null);
  const [actionError, setActionError] = useState<unknown>(null);
  const [tab, setTab] = useState<'board' | 'history'>('board');
  const searchingRef = useRef<string | null>(null);
  searchingRef.current = searching;

  const open = (id: string) => router.push(`/duel/${id}`);

  async function startSearch() {
    setActionError(null);
    try {
      const r = await post<DuelQueueDto>('/duels/queue');
      if (r.status === 'matched' && r.duelId) open(r.duelId);
      else setSearching(r.since ?? new Date().toISOString());
    } catch (e) {
      setActionError(e);
    }
  }
  async function practice() {
    setActionError(null);
    try {
      if (searchingRef.current) await del('/duels/queue').catch(() => undefined);
      setSearching(null);
      open((await post<{ duelId: string }>('/duels/practice')).duelId);
    } catch (e) {
      setActionError(e);
    }
  }
  async function cancelSearch() {
    setSearching(null);
    await del('/duels/queue').catch(() => undefined);
    qc.invalidateQueries({ queryKey: ['duels'] });
  }

  // Reprise d'une recherche en cours
  useEffect(() => {
    if (data?.searching && !searching) setSearching(data.searching.since);
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [data?.searching?.since]);

  // Sondage de la file d'attente
  useEffect(() => {
    if (!searching) return;
    let stop = false;
    const tick = async () => {
      try {
        const r = await api<DuelQueueDto>('/duels/queue');
        if (stop) return;
        if (r.status === 'matched' && r.duelId) {
          searchingRef.current = null;
          setSearching(null);
          open(r.duelId);
        } else if (r.status === 'idle') setSearching(null);
      } catch {
        /* nouvel essai au prochain tour */
      }
    };
    const t = setInterval(tick, 1200);
    void tick();
    return () => {
      stop = true;
      clearInterval(t);
    };
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [searching]);
  // En quittant l'écran, on quitte la file
  useEffect(() => () => void (searchingRef.current && del('/duels/queue').catch(() => undefined)), []);

  if (isLoading) return <Loading label={T('Ouverture du dojo…')} />;
  if (error || !data) return <Screen><ErrorBox error={error} onRetry={refetch} /></Screen>;
  const p = data.profile;
  const played = p.wins + p.losses + p.draws;

  return (
    <Screen>
      <View style={{ flexDirection: 'row', alignItems: 'center', gap: 8 }}>
        <Pressable accessibilityRole="button" accessibilityLabel={T('Retour')} onPress={() => router.back()} hitSlop={12}>
          <Text style={{ fontSize: 26, color: C.ink, fontWeight: '800' }}>‹</Text>
        </Pressable>
        <H1>{T('Duels')}</H1>
      </View>
      <P soft>{T('Affronte d’autres apprentis en temps réel : même question, même chrono. Plus tu réponds vite, plus tu frappes fort.')}</P>

      {/* Écusson et palmarès */}
      <Card style={{ backgroundColor: '#2A2858', borderColor: '#2A2858', gap: 14 }} testID="duel-profile">
        <View style={{ flexDirection: 'row', alignItems: 'center', gap: 14 }}>
          <RankBadge rank={p.rank} size={72} />
          <View style={{ flex: 1, gap: 4 }}>
            <Text style={{ color: '#ffffffbb', fontSize: 12, fontWeight: '800', letterSpacing: 1 }}>{T('Ton rang').toUpperCase()}</Text>
            <Text style={{ color: '#fff', fontSize: 24, fontWeight: '800' }}>{RL(p.rank)}</Text>
            <Text style={{ color: '#fff', fontSize: 15 }}>
              {p.rating} {T('points')}{played > 0 ? ' ' + T('· {0}ᵉ sur {1}', [p.position, p.players]) : ''}
            </Text>
          </View>
        </View>
        {p.rank.next !== null && (
          <View style={{ gap: 4 }}>
            <View style={{ flexDirection: 'row' }}><ProgressBar value={p.rank.progress} max={1} color={p.rank.color} label={T('Progression vers la division suivante')} /></View>
            <Text style={{ color: '#ffffffcc', fontSize: 13 }}>{T('Encore {0} points pour la division suivante', [Math.max(1, p.rank.next - p.rating)])}</Text>
          </View>
        )}
        <View style={{ flexDirection: 'row', gap: 6 }}>
          {([[T('Victoires'), p.wins], [T('Défaites'), p.losses], [T('Série'), p.streak > 0 ? `🔥 ${p.streak}` : '0'], [T('Record'), p.peakRating]] as const).map(([k, v]) => (
            <View key={k} style={{ flex: 1, backgroundColor: '#ffffff1a', borderRadius: 12, paddingVertical: 6, alignItems: 'center' }}>
              <Text style={{ color: '#ffffffbb', fontSize: 11 }}>{k}</Text>
              <Text style={{ color: '#fff', fontSize: 18, fontWeight: '800' }}>{v}</Text>
            </View>
          ))}
        </View>
      </Card>

      {!data.online && <P soft>{T('Mode hors ligne : adversaires simulés.')}</P>}
      {actionError != null && <ErrorBox error={actionError} />}

      {data.activeDuelId && (
        <Card style={{ borderColor: C.ko, borderWidth: 2, backgroundColor: C.koBg, gap: 10 }}>
          <P style={{ fontWeight: '800' }}>{T('Un duel est en cours : reviens vite, sinon il sera perdu par abandon.')}</P>
          <Button label={T('Reprendre le duel')} onPress={() => open(data.activeDuelId!)} />
        </Card>
      )}

      {data.invites.map((inv) => <InviteCard key={inv.id} invite={inv} onOpen={open} onDone={() => qc.invalidateQueries({ queryKey: ['duels'] })} />)}

      {/* Modes de jeu */}
      {searching ? (
        <Card style={{ alignItems: 'center', gap: 12, borderColor: C.ko, borderWidth: 2 }} testID="duel-searching">
          <ActivityIndicator color={C.ko} size="large" />
          <H2>{T('Recherche d’un adversaire…')}</H2>
          <SearchTimer since={searching} />
          <Button label={T('Annuler')} tone="quiet" onPress={cancelSearch} style={{ alignSelf: 'stretch' }} />
          <Button label={T('M’entraîner en attendant')} onPress={practice} style={{ alignSelf: 'stretch' }} />
        </Card>
      ) : (
        <>
          <Mode glyph={D('duel')} color={C.ko} title={T('Duel classé')} text={T('Un adversaire de ton niveau, au hasard. Gagne des points pour monter de rang.')} action={T('Trouver un adversaire')} onPress={startSearch} gold />
          <Mode glyph={D('training')} color="#7B5BD6" title={T('Entraînement')} text={T('Contre un rōnin (IA) de ton niveau. Idéal pour apprendre le rythme.')} action={T('S’entraîner')} onPress={practice} testID="duel-practice" />
        </>
      )}

      <FriendsQuick onOpen={open} />

      <View style={{ flexDirection: 'row', gap: 8 }} accessibilityRole="tablist">
        {(['board', 'history'] as const).map((t) => (
          <Pressable key={t} accessibilityRole="tab" accessibilityState={{ selected: tab === t }} onPress={() => setTab(t)} style={{ paddingHorizontal: 16, paddingVertical: 8, borderRadius: 99, backgroundColor: tab === t ? C.ink : C.surface2 }}>
            <Text style={{ fontWeight: '800', color: tab === t ? C.paper : C.inkSoft }}>{t === 'board' ? T('Classement') : T('Mes duels')}</Text>
          </Pressable>
        ))}
      </View>
      {tab === 'board' ? (
        <Leaderboard />
      ) : data.history.length === 0 ? (
        <P soft>{T('Aucun duel pour l’instant.')}</P>
      ) : (
        <Card style={{ gap: 10 }}>
          {data.history.map((h) => (
            <View key={h.id} style={{ flexDirection: 'row', alignItems: 'center', gap: 10 }}>
              <Text style={{ width: 70, fontWeight: '800', color: h.result === 'win' ? C.ok : h.result === 'loss' ? C.ko : C.inkSoft }}>{T(RESULT[h.result])}</Text>
              <View style={{ flex: 1 }}>
                <Text style={{ fontWeight: '700', color: C.ink }}>{h.opponent}</Text>
                <Text style={{ fontSize: 12, color: C.inkSoft }}>{T(KIND[h.kind])} · {T('{0} PV contre {1}', [h.myHp, h.oppHp])}</Text>
              </View>
              {h.delta !== null && <Text style={{ fontWeight: '800', color: h.delta >= 0 ? C.ok : C.ko }}>{h.delta >= 0 ? '+' : ''}{h.delta}</Text>}
            </View>
          ))}
        </Card>
      )}

      <Card style={{ gap: 6 }}>
        <H2>{T('Comment se déroule un duel ?')}</H2>
        {[
          T('Chacun commence avec {0} PV. {1} questions au maximum, {2} secondes chacune, la même pour les deux.', [data.rules.hp, data.rules.rounds, data.rules.roundMs / 1000]),
          T('Une bonne réponse frappe l’adversaire : de {0} à {1} dégâts selon ta vitesse. Sous {2} secondes, c’est un coup critique (+{3}).', [DUEL_RULES.minDamage, DUEL_RULES.maxDamage, DUEL_RULES.criticalMs / 1000, DUEL_RULES.criticalBonus]),
          T('Les bonnes réponses enchaînées ajoutent un combo (jusqu’à +{0}). Une erreur ne fait rien… mais casse ton combo.', [DUEL_RULES.comboMax]),
          T('Celui qui tombe à 0 PV perd. Sinon, après la dernière question, le plus de PV l’emporte.'),
          T('Quitter un duel en cours compte comme un abandon.'),
        ].map((t) => <P key={t} soft style={{ fontSize: 14 }}>• {t}</P>)}
      </Card>
    </Screen>
  );
}

function SearchTimer({ since }: { since: string }) {
  const [, setTick] = useState(0);
  useEffect(() => {
    const t = setInterval(() => setTick((x) => x + 1), 1000);
    return () => clearInterval(t);
  }, []);
  const s = Math.max(0, Math.floor((Date.now() - Date.parse(since)) / 1000));
  return <P soft>{Math.floor(s / 60)}:{String(s % 60).padStart(2, '0')}. {T('Si personne n’est disponible, un rōnin prendra la place.')}</P>;
}

function Mode({ glyph, color, title, text, action, onPress, gold, testID }: { glyph: string; color: string; title: string; text: string; action: string; onPress: () => void; gold?: boolean; testID?: string }) {
  return (
    <Card style={{ gap: 10 }}>
      <View style={{ flexDirection: 'row', alignItems: 'center', gap: 12 }}>
        <View style={{ width: 52, height: 52, borderRadius: 14, backgroundColor: color, alignItems: 'center', justifyContent: 'center' }}>
          <Text style={{ fontSize: 28, fontWeight: '900', color: '#fff' }}>{glyph}</Text>
        </View>
        <View style={{ flex: 1 }}>
          <H2>{title}</H2>
          <P soft style={{ fontSize: 14 }}>{text}</P>
        </View>
      </View>
      <Button label={action} tone={gold ? 'gold' : 'primary'} onPress={onPress} testID={testID} />
    </Card>
  );
}

function InviteCard({ invite, onOpen, onDone }: { invite: DuelInviteDto; onOpen: (id: string) => void; onDone: () => void }) {
  const [err, setErr] = useState<unknown>(null);
  return (
    <Card style={{ gap: 10, borderColor: C.gold, borderWidth: 2 }}>
      <View style={{ flexDirection: 'row', alignItems: 'center', gap: 12 }}>
        <RankBadge rank={invite.player.rank} size={46} />
        <P style={{ flex: 1, fontWeight: '800' }}>{T('{0} te défie en duel amical !', [invite.player.name])}</P>
      </View>
      {err != null && <ErrorBox error={err} />}
      <View style={{ flexDirection: 'row', gap: 10 }}>
        <Button label={T('Accepter')} tone="gold" style={{ flex: 1 }} onPress={async () => { try { await post(`/duels/${invite.id}/accept`); onOpen(invite.id); } catch (e) { setErr(e); } }} />
        <Button label={T('Refuser')} tone="quiet" style={{ flex: 1 }} onPress={async () => { await post(`/duels/${invite.id}/decline`).catch(() => undefined); onDone(); }} />
      </View>
    </Card>
  );
}

function Leaderboard() {
  const { data, error, refetch } = useDuelLeaderboard();
  if (error) return <ErrorBox error={error} onRetry={refetch} />;
  if (!data) return <ActivityIndicator color={C.ink} />;
  if (!data.entries.length) return <P soft>{T('Le classement est encore vide : sois le premier à gagner un duel classé !')}</P>;
  return (
    <Card style={{ gap: 8 }}>
      {data.entries.slice(0, 20).map((e) => (
        <View key={e.userId} style={{ flexDirection: 'row', alignItems: 'center', gap: 10, backgroundColor: e.me ? C.surface2 : 'transparent', borderRadius: 10, padding: 4 }}>
          <Text style={{ width: 28, textAlign: 'right', fontWeight: '800', color: C.inkSoft }}>{e.position}</Text>
          <RankBadge rank={e.rank} size={32} />
          <Text style={{ flex: 1, fontWeight: e.me ? '900' : '700', color: C.ink }} numberOfLines={1}>{e.name}{e.me ? T(' (toi)') : ''}</Text>
          <Text style={{ fontWeight: '800', color: C.ink }}>{e.rating}</Text>
        </View>
      ))}
      {data.me && data.me.position > 20 && <P soft style={{ fontSize: 14 }}>{T('Ta place : {0}ᵉ, {1} points.', [data.me.position, data.me.rating])}</P>}
    </Card>
  );
}
