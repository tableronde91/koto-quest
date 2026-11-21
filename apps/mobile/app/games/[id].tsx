import { useCallback, useEffect, useRef, useState } from 'react';
import { Pressable, Text, View } from 'react-native';
import { useLocalSearchParams, useRouter } from 'expo-router';
import { useQueryClient } from '@tanstack/react-query';
import type { AnswerResultDto, GameInfoDto, GameResultDto, GameStartDto } from '@koto/shared';
import { post } from '../../src/api';
import { useGames } from '../../src/hooks';
import { useAuth } from '../../src/auth';
import { speak, stopSpeech } from '../../src/speech';
import { C } from '../../src/theme';
import { Button, ErrorBox, H1, Loading, P, Screen } from '../../src/ui';
import { GAME_GLYPH, KIND_HINT } from '../../src/games';
import { T, plural } from '../../src/i18n';

type Stage = { kind: 'intro' } | { kind: 'countdown'; game: GameStartDto } | { kind: 'play'; game: GameStartDto; startedAt: number } | { kind: 'finishing' } | { kind: 'done'; result: GameResultDto; info: GameInfoDto };

/** Partie de mini-jeu : compte à rebours, une minute de questions enchaînées, score validé par le serveur. */
export default function GameScreen() {
  const { me } = useAuth();
  const { id } = useLocalSearchParams<{ id: string }>();
  const router = useRouter();
  const qc = useQueryClient();
  const { data, isLoading } = useGames();
  const [stage, setStage] = useState<Stage>({ kind: 'intro' });
  const [error, setError] = useState<unknown>(null);

  const start = async () => {
    setError(null);
    try {
      setStage({ kind: 'countdown', game: await post<GameStartDto>(`/games/${id}/start`) });
    } catch (e) {
      setError(e);
    }
  };
  const finish = useCallback(
    async (game: GameStartDto) => {
      stopSpeech();
      setStage({ kind: 'finishing' });
      // Le serveur n'accepte la fin qu'une fois le temps écoulé : on réessaie brièvement si l'horloge est un peu en avance.
      for (let attempt = 0; attempt < 5; attempt++) {
        try {
          const result = await post<GameResultDto>(`/games/${id}/finish`, { sessionId: game.sessionId });
          setStage({ kind: 'done', result, info: game.game });
          qc.invalidateQueries();
          return;
        } catch (e) {
          if (attempt === 4) setError(e);
          else await new Promise((r) => setTimeout(r, 800));
        }
      }
    },
    [id, qc],
  );

  if (isLoading) return <Loading />;
  const info = data?.games.find((g) => g.id === id);
  if (!info) return <Screen><ErrorBox error={new Error(T('Mini-jeu inconnu.'))} /></Screen>;
  if (error) return <Screen><ErrorBox error={error} /><Button label={T('Retour aux mini-jeux')} tone="quiet" onPress={() => router.back()} /></Screen>;
  if (stage.kind === 'countdown') return <Countdown onDone={() => setStage({ kind: 'play', game: stage.game, startedAt: Date.now() })} />;
  if (stage.kind === 'play') return <Play game={stage.game} startedAt={stage.startedAt} onEnd={() => finish(stage.game)} onQuit={() => { stopSpeech(); router.back(); }} />;
  if (stage.kind === 'finishing') return <Loading label={T('Calcul du score…')} />;
  if (stage.kind === 'done')
    return (
      <Screen>
        <View style={{ alignItems: 'center', gap: 10, paddingTop: 24 }}>
          <Text style={{ fontSize: 52, fontWeight: '900', color: C.ko }}>{me?.preferences.studyLanguage === 'ko' ? (stage.result.newBest ? '신기록' : '끝') : stage.result.newBest ? '新記録' : '終了'}</Text>
          <H1 style={{ textAlign: 'center' }}>{stage.result.newBest ? T('Nouveau record !') : T('Partie terminée')}</H1>
          <Text testID="final-score" style={{ fontSize: 72, fontWeight: '900', color: C.ink }}>{stage.result.score}</Text>
          <P soft>{plural(stage.result.score, 'bonne réponse sur {1}, record : {2}', 'bonnes réponses sur {1}, record : {2}', [stage.result.score, stage.result.answered, stage.result.bestScore])}</P>
          <Text style={{ color: C.goldInk, fontWeight: '800', fontSize: 18 }}>+{stage.result.xpGained} XP{stage.result.coinsGained > 0 ? ' · ' + plural(stage.result.coinsGained, '+{0} pièce', '+{0} pièces') : ''}</Text>
        </View>
        <Button label={T('Rejouer à {0}', [stage.info.title])} tone="gold" onPress={start} />
        <Button label={T('Autres mini-jeux')} tone="quiet" onPress={() => router.back()} />
      </Screen>
    );
  return (
    <Screen>
      <Button label={T('← Mini-jeux')} tone="quiet" onPress={() => router.back()} style={{ alignSelf: 'flex-start' }} />
      <View style={{ alignItems: 'center', gap: 14 }}>
        <View style={{ width: 110, height: 110, borderRadius: 28, backgroundColor: C.ink, alignItems: 'center', justifyContent: 'center' }}>
          <Text style={{ fontSize: 60, fontWeight: '900', color: C.paper }}>{GAME_GLYPH[info.id]}</Text>
        </View>
        <H1 style={{ textAlign: 'center' }}>{info.title}</H1>
        <P style={{ textAlign: 'center', fontSize: 17 }}>{info.description}</P>
        <P soft style={{ textAlign: 'center' }}>{T('{0} secondes, pas de pause. Touche une réponse : la suivante arrive aussitôt.', [info.durationSec])}</P>
        {info.plays > 0 && <P>{T('Ton record :')} <Text style={{ fontWeight: '900' }}>{info.bestScore}</Text></P>}
      </View>
      {info.available ? (
        <Button label={T('C’est parti')} tone="gold" onPress={start} />
      ) : (
        <P>{T('Rencontre au moins {0} {1} pour débloquer ce jeu ({2}/{0}).', [info.minItems, T(KIND_HINT[info.id]), info.seenItems])}</P>
      )}
    </Screen>
  );
}

function Countdown({ onDone }: { onDone: () => void }) {
  const [n, setN] = useState(3);
  useEffect(() => {
    if (n === 0) {
      onDone();
      return;
    }
    const t = setTimeout(() => setN(n - 1), 700);
    return () => clearTimeout(t);
  }, [n, onDone]);
  return (
    <View accessibilityRole="text" accessibilityLiveRegion="assertive" style={{ flex: 1, alignItems: 'center', justifyContent: 'center', backgroundColor: C.paper }}>
      <Text style={{ fontSize: 120, fontWeight: '900', color: C.ink }}>{n || 'Go'}</Text>
    </View>
  );
}

function Play({ game, startedAt, onEnd, onQuit }: { game: GameStartDto; startedAt: number; onEnd: () => void; onQuit: () => void }) {
  const duration = game.game.durationSec * 1000;
  const [now, setNow] = useState(Date.now());
  const [index, setIndex] = useState(0);
  const [score, setScore] = useState(0);
  const [combo, setCombo] = useState(0);
  const [flash, setFlash] = useState<{ choice: string; answer: string } | null>(null);
  const ended = useRef(false);
  const shownAt = useRef(Date.now());
  const q = game.questions[index];
  const left = Math.max(0, duration - (now - startedAt));

  const end = useCallback(() => {
    if (ended.current) return;
    ended.current = true;
    onEnd();
  }, [onEnd]);
  useEffect(() => {
    const t = setInterval(() => setNow(Date.now()), 100);
    return () => clearInterval(t);
  }, []);
  useEffect(() => {
    if (left <= 0 || !q) end();
  }, [left, q, end]);
  useEffect(() => {
    shownAt.current = Date.now();
    if (q?.type === 'listening_choice' && q.audio) speak(q.audio);
  }, [q?.id, q?.type, q?.audio]);

  async function pick(choice: string) {
    if (!q || flash || ended.current) return;
    setFlash({ choice, answer: '' });
    try {
      const r = await post<AnswerResultDto>(`/questions/${q.id}/answer`, { answer: choice, responseMs: Date.now() - shownAt.current });
      setFlash({ choice, answer: Array.isArray(r.correctAnswer) ? r.correctAnswer.join('') : r.correctAnswer });
      if (r.correct) {
        setScore((s) => s + 1);
        setCombo((c) => c + 1);
      } else setCombo(0);
      setTimeout(() => {
        setFlash(null);
        setIndex((i) => i + 1);
      }, r.correct ? 220 : 650);
    } catch {
      setFlash(null);
      setIndex((i) => i + 1);
    }
  }

  if (!q) return <Loading label={T('Fin de la partie…')} />;
  const d = q.display ?? {};
  const secs = Math.ceil(left / 1000);
  return (
    <Screen>
      <View style={{ flexDirection: 'row', alignItems: 'center', gap: 12 }} testID="game">
        <Pressable accessibilityRole="button" accessibilityLabel={T('Abandonner la partie')} onPress={onQuit} style={{ width: 44, height: 44, alignItems: 'center', justifyContent: 'center' }}>
          <Text style={{ fontSize: 22, color: C.inkSoft }}>✕</Text>
        </Pressable>
        <View accessibilityRole="timer" accessibilityLabel={T('{0} secondes restantes', [secs])} style={{ flex: 1, height: 12, borderRadius: 99, backgroundColor: C.surface2, overflow: 'hidden' }}>
          <View style={{ width: `${(left / duration) * 100}%`, height: '100%', backgroundColor: left < 10_000 ? C.ko : C.ink, borderRadius: 99 }} />
        </View>
        <Text style={{ width: 40, textAlign: 'right', fontWeight: '800', color: C.ink, fontVariant: ['tabular-nums'] }}>{secs} s</Text>
      </View>
      <View style={{ flexDirection: 'row', justifyContent: 'space-between', alignItems: 'baseline' }}>
        <Text style={{ fontSize: 17, color: C.ink }}>{T('Score :')} <Text testID="score" style={{ fontSize: 24, fontWeight: '900' }}>{score}</Text></Text>
        {combo >= 3 && <Text style={{ fontWeight: '800', color: C.goldInk }}>{T('Série × {0}', [combo])}</Text>}
      </View>
      <Text style={{ fontWeight: '800', color: C.ink, fontSize: 16 }}>{q.prompt}</Text>
      <View style={{ minHeight: 150, borderRadius: 24, backgroundColor: C.surface2, alignItems: 'center', justifyContent: 'center', padding: 18 }}>
        {q.type === 'listening_choice' ? (
          <Button label={`🔊  ${T('Réécouter')}`} tone="quiet" onPress={() => q.audio && speak(q.audio)} />
        ) : d.jp ? (
          <Text style={{ fontSize: [...d.jp].length <= 2 ? 72 : 40, fontWeight: '800', color: C.ink, textAlign: 'center' }}>{d.jp.replace(/\{\{|\}\}/g, '')}</Text>
        ) : (
          <Text style={{ fontSize: 24, fontWeight: '800', color: C.ink, textAlign: 'center' }}>{d.text}</Text>
        )}
      </View>
      <View accessibilityLabel={T('Réponses')} style={{ flexDirection: 'row', flexWrap: 'wrap', gap: 10 }}>
        {q.choices?.map((c) => {
          const isPicked = flash?.choice === c;
          const isAnswer = !!flash?.answer && flash.answer === c;
          const bg = flash?.answer ? (isAnswer ? C.okBg : isPicked ? C.koBg : C.surface) : C.surface;
          const border = flash?.answer ? (isAnswer ? C.ok : isPicked ? C.ko : C.line) : C.line;
          const jp = /[぀-ヿ一-龯]/.test(c);
          return (
            <Pressable key={c} accessibilityRole="button" accessibilityLabel={c} disabled={!!flash} onPress={() => pick(c)} style={{ width: '48%', flexGrow: 1, minHeight: 84, borderRadius: 18, borderWidth: 2, borderColor: border, backgroundColor: bg, alignItems: 'center', justifyContent: 'center', padding: 8 }}>
              <Text style={{ fontSize: jp ? 30 : 17, fontWeight: jp ? '500' : '800', color: C.ink, textAlign: 'center' }}>{c}</Text>
            </Pressable>
          );
        })}
      </View>
    </Screen>
  );
}
