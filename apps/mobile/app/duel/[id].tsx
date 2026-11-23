import { useDecor, useRankLabel } from '../../src/study';
import { useEffect, useRef, useState } from 'react';
import { Pressable, Text, View } from 'react-native';
import { useLocalSearchParams, useRouter } from 'expo-router';
import { useQuery, useQueryClient } from '@tanstack/react-query';
import type { DuelSideResultDto, DuelStateDto } from '@koto/shared';
import { api, post } from '../../src/api';
import { C } from '../../src/theme';
import { Button, Card, ErrorBox, H1, H2, Loading, P, Screen } from '../../src/ui';
import { RankBadge } from '../../src/RankBadge';
import { T } from '../../src/i18n';

const JP_RE = /[぀-ヿ一-龯]/;

/** Arène : même question et même chrono pour les deux duellistes, synchronisés sur l'horloge du serveur. */
export default function DuelArenaScreen() {
  const { id = '' } = useLocalSearchParams<{ id: string }>();
  const router = useRouter();
  const qc = useQueryClient();
  const offset = useRef(0);
  const { data: s, error, refetch } = useQuery({
    queryKey: ['duel', id],
    queryFn: async () => {
      const r = await api<DuelStateDto>(`/duels/${id}`);
      offset.current = Date.parse(r.serverNow) - Date.now();
      return r;
    },
    refetchInterval: (q) => {
      const st = q.state.data?.status;
      return st === 'active' ? 600 : st === 'pending' ? 2000 : false;
    },
    staleTime: 0,
  });
  const [, setTick] = useState(0);
  useEffect(() => {
    const t = setInterval(() => setTick((x) => x + 1), 200);
    return () => clearInterval(t);
  }, []);
  const now = Date.now() + offset.current;

  // Relance exactement au début de chaque question
  useEffect(() => {
    if (!s?.roundStartsAt || s.status !== 'active') return;
    const wait = Date.parse(s.roundStartsAt) - (Date.now() + offset.current);
    if (wait <= 0) return;
    const t = setTimeout(() => void refetch(), wait + 40);
    return () => clearTimeout(t);
  }, [s?.roundStartsAt, s?.status, refetch]);

  // Le résultat s'affiche après la dernière correction
  const [showResult, setShowResult] = useState(false);
  useEffect(() => {
    if (s?.status !== 'finished') return;
    const t = setTimeout(() => setShowResult(true), s.result?.endReason === 'forfeit' ? 0 : 1500);
    return () => clearTimeout(t);
  }, [s?.status, s?.result?.endReason]);

  const [picked, setPicked] = useState<{ round: number; answer: string } | null>(null);
  const [confirmQuit, setConfirmQuit] = useState(false);

  if (error && !s) return <Screen><ErrorBox error={error} onRetry={refetch} /></Screen>;
  if (!s) return <Loading label={T('Entrée dans l’arène…')} />;

  const back = () => (router.canGoBack() ? router.back() : router.replace('/duel'));

  if (s.status === 'pending') return <PendingView s={s} now={now} onChange={() => qc.invalidateQueries({ queryKey: ['duel', id] })} onLeave={back} />;
  if (s.status === 'declined' || s.status === 'cancelled' || s.status === 'expired')
    return (
      <Screen>
        <View style={{ alignItems: 'center', gap: 14, paddingTop: 40 }}>
          <Text style={{ fontSize: 64, fontWeight: '900', color: C.inkSoft }}>⚔</Text>
          <H1 style={{ textAlign: 'center' }}>{s.status === 'declined' ? T('Défi refusé') : s.status === 'expired' ? T('Défi expiré') : T('Défi annulé')}</H1>
          <P soft style={{ textAlign: 'center' }}>{s.status === 'declined' ? T('{0} a décliné le duel.', [s.opponent.name]) : s.status === 'expired' ? T('Personne n’a répondu à temps.') : T('Ce défi a été annulé.')}</P>
          <Button label={T('Retour au dojo')} onPress={back} style={{ alignSelf: 'stretch' }} />
        </View>
      </Screen>
    );
  if (s.status === 'finished' && showResult && s.result) return <ResultView s={s} onLeave={back} />;

  const start = s.roundStartsAt ? Date.parse(s.roundStartsAt) : now;
  const countdown = s.status === 'active' && s.round === 0 && now < start ? Math.ceil((start - now) / 1000) : null;
  const q = s.question;
  const myPick = picked && q && picked.round === q.index ? picked.answer : null;
  const remaining = q ? Math.max(0, s.rules.roundMs - (now - start)) : 0;
  const answered = !!s.mine || !!myPick;

  async function choose(answer: string) {
    if (!q || answered) return;
    setPicked({ round: q.index, answer });
    try {
      qc.setQueryData(['duel', id], await post<DuelStateDto>(`/duels/${id}/answer`, { round: q.index, answer }));
    } catch {
      void refetch();
    }
  }

  async function forfeit() {
    setConfirmQuit(false);
    if (s!.status !== 'active') return back();
    const r = await post<DuelStateDto>(`/duels/${id}/forfeit`).catch(() => null);
    if (r) qc.setQueryData(['duel', id], r);
  }

  return (
    <Screen>
      {/* Les deux combattants */}
      <Card style={{ backgroundColor: '#2A2858', borderColor: '#2A2858', gap: 12 }} testID="duel-arena">
        <View style={{ flexDirection: 'row', alignItems: 'center', justifyContent: 'space-between' }}>
          <Text style={{ color: '#ffffffbb', fontWeight: '800', fontSize: 12, letterSpacing: 1 }}>
            {(s.kind === 'ranked' ? T('Duel classé') : s.kind === 'practice' ? T('Entraînement') : T('Duel amical')).toUpperCase()} · {Math.min(s.round + 1, s.rules.rounds)}/{s.rules.rounds}
          </Text>
          {s.status === 'active' && (
            <Pressable accessibilityRole="button" onPress={() => setConfirmQuit(true)} hitSlop={10}>
              <Text style={{ color: '#ffffffbb', fontWeight: '700' }}>{T('Abandonner')}</Text>
            </Pressable>
          )}
        </View>
        <Fighter name={T('Toi')} hp={s.me.hp} max={s.rules.hp} combo={s.me.combo} rank={s.me.rank} hit={s.last?.opponent} />
        <Text style={{ color: C.gold, fontWeight: '900', textAlign: 'center', fontSize: 16 }}>VS</Text>
        <Fighter name={s.opponent.name} hp={s.opponent.hp} max={s.rules.hp} combo={s.opponent.combo} rank={s.opponent.rank} hit={s.last?.me} answered={!!q && s.opponentAnswered} />
      </Card>

      {countdown !== null ? (
        <View style={{ alignItems: 'center', paddingVertical: 20 }}>
          <Text style={{ fontSize: 72, fontWeight: '900', color: C.ko }}>{countdown}</Text>
          <P soft>{T('Prépare-toi…')}</P>
        </View>
      ) : q ? (
        <View style={{ gap: 14 }} testID="duel-question">
          <View style={{ flexDirection: 'row', alignItems: 'center', gap: 10 }}>
            <View style={{ flex: 1, height: 10, borderRadius: 99, backgroundColor: C.surface2, overflow: 'hidden' }} accessibilityRole="progressbar" accessibilityLabel={T('Temps restant')}>
              <View style={{ width: `${(remaining / s.rules.roundMs) * 100}%`, height: '100%', backgroundColor: remaining < 3000 ? C.ko : C.gold }} />
            </View>
            <Text style={{ fontWeight: '800', color: C.ink, width: 34, textAlign: 'right' }}>{Math.ceil(remaining / 1000)} s</Text>
          </View>
          <P style={{ fontWeight: '800', fontSize: 18 }}>{q.prompt}</P>
          {(q.display?.jp || q.display?.text) && (
            <Card style={{ alignItems: 'center', backgroundColor: C.surface2, borderColor: C.surface2 }}>
              {q.display?.jp && <Text style={{ fontSize: [...q.display.jp].length <= 3 ? 56 : 34, fontWeight: '800', color: C.ink }}>{q.display.jp}</Text>}
              {q.display?.text && <Text style={{ fontSize: q.display.jp ? 15 : 22, color: q.display.jp ? C.inkSoft : C.ink, fontWeight: q.display.jp ? '400' : '800' }}>{q.display.text}</Text>}
            </Card>
          )}
          <View style={{ flexDirection: 'row', flexWrap: 'wrap', gap: 10 }}>
            {q.choices.map((c) => {
              const mine = (s.mine?.answer ?? myPick) === c;
              const verdict = mine && s.mine ? (s.mine.correct ? 'ok' : 'ko') : null;
              return (
                <Pressable
                  key={c}
                  testID="duel-choice"
                  accessibilityRole="button"
                  accessibilityState={{ disabled: answered, selected: mine }}
                  disabled={answered}
                  onPress={() => choose(c)}
                  style={{
                    width: '48%',
                    flexGrow: 1,
                    minHeight: 64,
                    borderRadius: 16,
                    borderWidth: 2,
                    paddingHorizontal: 10,
                    alignItems: 'center',
                    justifyContent: 'center',
                    borderColor: verdict === 'ok' ? C.ok : verdict === 'ko' ? C.ko : mine ? C.ink : C.line,
                    backgroundColor: verdict === 'ok' ? C.okBg : verdict === 'ko' ? C.koBg : C.surface,
                    opacity: answered && !mine ? 0.55 : 1,
                  }}
                >
                  <Text style={{ fontSize: JP_RE.test(c) ? 22 : 17, fontWeight: '800', color: C.ink, textAlign: 'center' }}>{c}</Text>
                </Pressable>
              );
            })}
          </View>
          <View accessibilityLiveRegion="polite" style={{ minHeight: 26, alignItems: 'center' }}>
            {s.mine ? (
              s.mine.correct ? (
                <Text style={{ color: C.ok, fontWeight: '800', fontSize: 16 }}>
                  {T('Juste ! Coup de {0}', [s.mine.damage])}{s.mine.critical ? T(' (critique !)') : ''}{s.mine.combo >= 2 ? ' ' + T('· combo ×{0}', [s.mine.combo]) : ''}
                </Text>
              ) : (
                <Text style={{ color: C.ko, fontWeight: '800', fontSize: 16 }}>{T('Raté… pas de coup cette fois.')}</Text>
              )
            ) : myPick ? (
              <Text style={{ color: C.inkSoft }}>…</Text>
            ) : null}
          </View>
        </View>
      ) : s.last ? (
        <RevealView s={s} />
      ) : (
        <P soft style={{ textAlign: 'center', paddingVertical: 20 }}>{T('Prépare-toi : la première question arrive…')}</P>
      )}

      {confirmQuit && (
        <Card style={{ gap: 10, borderColor: C.ko, borderWidth: 2 }}>
          <H2>{T('Abandonner le duel ?')}</H2>
          <P soft>{s.kind === 'ranked' ? T('Tu perdras le duel et des points de classement.') : T('Tu perdras ce duel.')}</P>
          <Button label={T('Continuer le combat')} onPress={() => setConfirmQuit(false)} />
          <Button label={T('Abandonner')} tone="quiet" onPress={forfeit} />
        </Card>
      )}
    </Screen>
  );
}

function Fighter({ name, hp, max, combo, rank, hit, answered }: { name: string; hp: number; max: number; combo: number; rank: DuelStateDto['me']['rank']; hit?: DuelSideResultDto; answered?: boolean }) {
  const pct = Math.max(0, Math.min(100, (hp / max) * 100));
  return (
    <View style={{ flexDirection: 'row', alignItems: 'center', gap: 12 }}>
      <RankBadge rank={rank} size={48} />
      <View style={{ flex: 1, gap: 4 }}>
        <View style={{ flexDirection: 'row', justifyContent: 'space-between' }}>
          <Text style={{ color: '#fff', fontWeight: '800', fontSize: 16 }} numberOfLines={1}>{name}{answered ? ' ✓' : ''}</Text>
          <Text style={{ color: '#fff', fontWeight: '800' }}>{T('{0} PV', [hp])}{combo >= 2 ? ` · ×${combo}` : ''}</Text>
        </View>
        <View accessibilityRole="progressbar" accessibilityLabel={T('Points de vie de {0}', [name])} accessibilityValue={{ min: 0, max, now: hp }} style={{ height: 12, borderRadius: 99, backgroundColor: '#ffffff26', overflow: 'hidden' }}>
          <View style={{ width: `${pct}%`, height: '100%', backgroundColor: pct > 50 ? '#6CC04A' : pct > 25 ? C.gold : C.ko, borderRadius: 99 }} />
        </View>
        {hit && hit.damage > 0 && <Text style={{ color: '#FFB4BB', fontSize: 12, fontWeight: '700' }}>{T('−{0} au dernier échange', [hit.damage])}{hit.critical ? T(' (critique)') : ''}</Text>}
      </View>
    </View>
  );
}

function RevealView({ s }: { s: DuelStateDto }) {
  const last = s.last!;
  const line = (who: string, r: DuelSideResultDto) => (
    <View style={{ flexDirection: 'row', justifyContent: 'space-between', gap: 8 }}>
      <Text style={{ fontWeight: '800', color: C.ink }}>{who}</Text>
      <Text style={{ color: r.correct ? C.ok : C.ko, fontWeight: '700', flexShrink: 1, textAlign: 'right' }}>
        {r.answer === null ? T('pas de réponse') : r.correct ? T('juste en {0} s', [((r.ms ?? 0) / 1000).toFixed(1)]) : T('faux')}
        {r.damage > 0 ? ' ' + T('· {0} dégâts{1}', [r.damage, r.critical ? T(' (critique)') : '']) : ''}
      </Text>
    </View>
  );
  return (
    <Card style={{ gap: 10 }} testID="duel-reveal">
      <P soft style={{ textAlign: 'center' }}>{last.question.prompt} {last.question.display?.jp ?? ''}</P>
      <P style={{ textAlign: 'center', fontSize: 18 }}>{T('Réponse :')} <Text style={{ fontWeight: '900' }}>{last.answer}</Text></P>
      {line(T('Toi'), last.me)}
      {line(s.opponent.name, last.opponent)}
      {s.status === 'active' && <P soft style={{ textAlign: 'center', fontSize: 14 }}>{T('Question suivante…')}</P>}
    </Card>
  );
}

function PendingView({ s, now, onChange, onLeave }: { s: DuelStateDto; now: number; onChange: () => void; onLeave: () => void }) {
  const RL = useRankLabel();
  const [err, setErr] = useState<unknown>(null);
  const left = s.expiresAt ? Math.max(0, Math.ceil((Date.parse(s.expiresAt) - now) / 1000)) : 0;
  const challenger = s.me.side === 1;
  return (
    <Screen>
      <View style={{ alignItems: 'center', gap: 16, paddingTop: 30 }}>
        <View style={{ flexDirection: 'row', alignItems: 'center', gap: 16 }}>
          <RankBadge rank={s.me.rank} size={64} />
          <Text style={{ fontSize: 24, fontWeight: '900', color: C.ink }}>VS</Text>
          <RankBadge rank={s.opponent.rank} size={64} />
        </View>
        {challenger ? (
          <>
            <H1 style={{ textAlign: 'center' }}>{T('Défi envoyé à {0}', [s.opponent.name])}</H1>
            <P soft style={{ textAlign: 'center' }}>{T('Le duel commence dès qu’il accepte. Expire dans {0}:{1}.', [Math.floor(left / 60), String(left % 60).padStart(2, '0')])}</P>
            <Button label={T('Annuler le défi')} tone="quiet" style={{ alignSelf: 'stretch' }} onPress={async () => { await post(`/duels/${s.id}/decline`).catch(() => undefined); onChange(); }} />
          </>
        ) : (
          <>
            <H1 style={{ textAlign: 'center' }}>{T('{0} te défie !', [s.opponent.name])}</H1>
            <P soft>{T('{0} · {1} points · duel amical', [RL(s.opponent.rank), s.opponent.rating])}</P>
            {err != null && <ErrorBox error={err} />}
            <Button label={T('Accepter')} tone="gold" style={{ alignSelf: 'stretch' }} onPress={async () => { try { await post(`/duels/${s.id}/accept`); onChange(); } catch (e) { setErr(e); } }} />
            <Button label={T('Refuser')} tone="quiet" style={{ alignSelf: 'stretch' }} onPress={async () => { await post(`/duels/${s.id}/decline`).catch(() => undefined); onLeave(); }} />
          </>
        )}
      </View>
    </Screen>
  );
}

function ResultView({ s, onLeave }: { s: DuelStateDto; onLeave: () => void }) {
  const D = useDecor();
  const router = useRouter();
  const qc = useQueryClient();
  const [err, setErr] = useState<unknown>(null);
  const r = s.result!;
  const win = r.outcome === 'win';
  const promoted = r.delta > 0 && r.rankAfter.label !== r.rankBefore.label;
  const demoted = r.delta < 0 && r.rankAfter.label !== r.rankBefore.label;
  useEffect(() => {
    void qc.invalidateQueries({ queryKey: ['duels'] });
    void qc.invalidateQueries({ queryKey: ['dashboard'] });
  }, [qc]);

  async function again() {
    setErr(null);
    try {
      if (s.kind === 'practice') router.replace(`/duel/${(await post<{ duelId: string }>('/duels/practice')).duelId}`);
      else if (s.kind === 'friendly' && s.opponent.userId) router.replace(`/duel/${(await post<{ duelId: string }>('/duels/challenges', { userId: s.opponent.userId })).duelId}`);
      else onLeave();
    } catch (e) {
      setErr(e);
    }
  }

  return (
    <Screen>
      <View style={{ alignItems: 'center', gap: 14, paddingTop: 20 }} testID="duel-result">
        <Text style={{ fontSize: 88, fontWeight: '900', color: win ? C.gold : r.outcome === 'loss' ? C.ko : C.inkSoft }}>{win ? D('win') : r.outcome === 'loss' ? D('loss') : D('draw')}</Text>
        <H1>{win ? T('Victoire !') : r.outcome === 'loss' ? T('Défaite') : T('Égalité')}</H1>
        <P soft style={{ textAlign: 'center' }}>
          {r.endReason === 'ko'
            ? win ? T('{0} est K.-O.', [s.opponent.name]) : T('Tu es K.-O.')
            : r.endReason === 'forfeit'
              ? win ? T('{0} a abandonné.', [s.opponent.name]) : T('Tu as abandonné.')
              : T('{0} PV contre {1} à la fin des questions.', [s.me.hp, s.opponent.hp])}
        </P>
        {s.kind === 'ranked' ? (
          <Card style={{ alignItems: 'center', gap: 8, alignSelf: 'stretch' }}>
            <RankBadge rank={r.rankAfter} size={72} />
            <P style={{ fontWeight: '800', color: promoted ? C.goldInk : demoted ? C.ko : C.ink }}>
              {promoted ? T('Promotion : {0}', [r.rankAfter.label]) : demoted ? T('Retour en {0}', [r.rankAfter.label]) : r.rankAfter.label}
            </P>
            <P>
              <Text style={{ fontWeight: '900', fontSize: 22 }}>{r.ratingAfter}</Text> {T('points')}{' '}
              <Text style={{ fontWeight: '800', color: r.delta >= 0 ? C.ok : C.ko }}>({r.delta >= 0 ? '+' : ''}{r.delta})</Text>
            </P>
          </Card>
        ) : (
          <P soft>{T('{0} : sans effet sur le classement.', [s.kind === 'practice' ? T('Entraînement') : T('Duel amical')])}</P>
        )}
        {(r.xp > 0 || r.coins > 0) && <Text style={{ color: C.goldInk, fontWeight: '800', fontSize: 18 }}>{T('+{0} XP · +{1} pièces', [r.xp, r.coins])}</Text>}
        {err != null && <ErrorBox error={err} />}
        <Button label={s.kind === 'ranked' ? T('Retour au dojo') : s.kind === 'practice' ? T('Rejouer') : T('Revanche')} tone="gold" onPress={again} style={{ alignSelf: 'stretch' }} testID="duel-again" />
        {s.kind !== 'ranked' && <Button label={T('Retour au dojo')} tone="quiet" onPress={onLeave} style={{ alignSelf: 'stretch' }} />}
      </View>
    </Screen>
  );
}
