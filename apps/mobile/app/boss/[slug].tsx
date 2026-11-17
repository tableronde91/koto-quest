import { useState } from 'react';
import { Text, View } from 'react-native';
import { useLocalSearchParams, useRouter } from 'expo-router';
import { useQueryClient } from '@tanstack/react-query';
import { simulateBoss } from '@koto/learning-engine';
import type { BossFightDto, BossOutcomeDto } from '@koto/shared';
import { post } from '../../src/api';
import { QuestionView } from '../../src/QuestionView';
import { storyChapter } from '../../src/story';
import { C } from '../../src/theme';
import { Button, Card, ErrorBox, H1, Loading, P, ProgressBar, Screen, Seal } from '../../src/ui';
import { T, plural } from '../../src/i18n';

/** Combat contre le gardien d'une île : chaque bonne réponse le frappe, chaque erreur coûte un cœur. */
export default function BossScreen() {
  const { slug, order, name, glyph } = useLocalSearchParams<{ slug: string; order?: string; name?: string; glyph?: string }>();
  const router = useRouter();
  const qc = useQueryClient();
  const chapter = storyChapter(slug);
  const [fight, setFight] = useState<BossFightDto | null>(null);
  const [results, setResults] = useState<boolean[]>([]);
  const [index, setIndex] = useState(0);
  const [outcome, setOutcome] = useState<BossOutcomeDto | null>(null);
  const [busy, setBusy] = useState(false);
  const [error, setError] = useState<unknown>(null);

  const start = async () => {
    setBusy(true);
    setError(null);
    try {
      setFight(await post<BossFightDto>(`/worlds/${slug}/boss/start`));
      setResults([]);
      setIndex(0);
      setOutcome(null);
    } catch (e) {
      setError(e);
    } finally {
      setBusy(false);
    }
  };

  const finish = async (f: BossFightDto) => {
    setBusy(true);
    try {
      setOutcome(await post<BossOutcomeDto>(`/worlds/${slug}/boss/finish`, { sessionId: f.sessionId }));
      qc.invalidateQueries({ queryKey: ['path'] });
      qc.invalidateQueries({ queryKey: ['dashboard'] });
    } catch (e) {
      setError(e);
    } finally {
      setBusy(false);
    }
  };

  if (busy && !fight) return <Loading label={T('Le gardien approche…')} />;

  if (outcome && fight) {
    const won = outcome.state === 'won';
    return (
      <Screen>
        <View style={{ alignItems: 'center', gap: 14, paddingTop: 20 }}>
          <Seal glyph={fight.boss.glyph} size={110} color={won ? C.ok : C.seal} />
          <H1 style={{ textAlign: 'center' }}>{won ? T('{0} est vaincu !', [fight.boss.name]) : T('{0} l’emporte…', [fight.boss.name])}</H1>
          {won && chapter && <Card><P style={{ fontSize: 18, textAlign: 'center' }}>{chapter.outro}</P></Card>}
          <P>{plural(outcome.hits, '{0} coup porté', '{0} coups portés')}, {plural(outcome.heartsLeft, '{0} cœur restant', '{0} cœurs restants')}.</P>
          <Text style={{ color: C.goldInk, fontWeight: '800', fontSize: 18 }}>+{outcome.xpGained} XP{outcome.coinsGained > 0 ? ' · ' + T('+{0} pièces', [outcome.coinsGained]) : ''}</Text>
          {outcome.firstVictory && <P style={{ fontWeight: '800' }}>{T('Première victoire contre ce gardien !')}</P>}
          {!won && <Button label={T('Revanche')} tone="gold" onPress={start} style={{ alignSelf: 'stretch' }} />}
          <Button label={T('Retour au parcours')} tone={won ? 'gold' : 'quiet'} onPress={() => router.back()} style={{ alignSelf: 'stretch' }} />
        </View>
      </Screen>
    );
  }

  if (fight) {
    const progress = simulateBoss(results, fight.rules);
    const q = fight.questions[index];
    const hpLeft = fight.rules.hp - progress.hits;
    return (
      <Screen>
        <Card style={{ gap: 10, backgroundColor: C.ink, borderColor: C.ink }} testID="arena">
          <View style={{ flexDirection: 'row', alignItems: 'center', gap: 12 }}>
            <Seal glyph={fight.boss.glyph} size={52} color={C.seal} />
            <View style={{ flex: 1, gap: 6 }}>
              <Text style={{ color: C.paper, fontWeight: '800', fontSize: 16 }}>{fight.boss.name}</Text>
              <View style={{ flexDirection: 'row' }}>
                <ProgressBar value={hpLeft} max={fight.rules.hp} color={C.ko} label={T('Vie du gardien : {0} sur {1}', [hpLeft, fight.rules.hp])} />
              </View>
            </View>
          </View>
          <Text accessibilityLabel={T('{0} cœurs restants', [progress.heartsLeft])} style={{ color: C.paper, fontSize: 22, letterSpacing: 4 }}>
            {'♥'.repeat(progress.heartsLeft)}<Text style={{ opacity: 0.3 }}>{'♥'.repeat(fight.rules.hearts - progress.heartsLeft)}</Text>
          </Text>
        </Card>
        <P soft>{T('Question {0}', [index + 1])}</P>
        <QuestionView
          key={q.id}
          q={q}
          onResult={(r) => setResults((x) => [...x, r.correct])}
          continueLabel={(r) => {
            const after = simulateBoss([...results.slice(0, index), r.correct], fight.rules);
            return after.state === 'won' ? T('Coup final !') : after.state === 'lost' ? T('Voir le résultat') : T('Continuer');
          }}
          onDone={() => {
            const now = simulateBoss(results, fight.rules);
            if (now.state !== 'ongoing' || index + 1 >= fight.questions.length) finish(fight);
            else setIndex(index + 1);
          }}
        />
        {error ? <ErrorBox error={error} /> : null}
      </Screen>
    );
  }

  return (
    <Screen>
      <Button label={T('← Parcours')} tone="quiet" onPress={() => router.back()} style={{ alignSelf: 'flex-start' }} />
      <View style={{ alignItems: 'center', gap: 12 }}>
        {chapter && <P soft style={{ fontWeight: '700' }}>{order ? T('Chapitre {0} · {1}', [order, chapter.title]) : chapter.title}</P>}
        {glyph && <Seal glyph={glyph} size={96} color={C.seal} />}
        <Text style={{ color: C.inkSoft }}>{T('Gardien de l’île')}</Text>
        <H1 style={{ textAlign: 'center' }}>{name || T('Le gardien')}</H1>
      </View>
      {chapter && <Card><P>{chapter.intro}</P></Card>}
      <Card style={{ gap: 6 }}>
        <P>{T('Chaque bonne réponse frappe le gardien. Chaque erreur te coûte un cœur : trois erreurs et le combat est perdu.')}</P>
      </Card>
      {error ? <ErrorBox error={error} /> : null}
      <Button label={T('Engager le combat')} tone="gold" onPress={start} />
    </Screen>
  );
}
