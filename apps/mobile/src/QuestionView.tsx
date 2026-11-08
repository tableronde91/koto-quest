import { useEffect, useRef, useState } from 'react';
import { Pressable, Text, View } from 'react-native';
import * as Haptics from 'expo-haptics';
import { fillBlank, hasBlank } from '@koto/learning-engine';
import type { AnswerResultDto, IssuedQuestionDto } from '@koto/shared';
import { post } from './api';
import { speak } from './speech';
import { C } from './theme';
import { Button, P } from './ui';

const JP = /[぀-ヿ一-龯]/;
const isJp = (s: string) => JP.test(s);
const same = (a: string | string[], b: string | string[]) => (Array.isArray(a) ? Array.isArray(b) && a.join('|') === b.join('|') : a === b);

function spokenAfter(q: IssuedQuestionDto, answer: string | string[]): string | null {
  if (q.answerAudio) {
    if (!Array.isArray(answer) && !isJp(answer)) return hasBlank(q.answerAudio) ? null : q.answerAudio;
    return fillBlank(q.answerAudio, answer);
  }
  return q.type === 'listening_choice' ? null : q.audio ?? null;
}

function vibrate(ok: boolean) {
  Haptics.notificationAsync(ok ? Haptics.NotificationFeedbackType.Success : Haptics.NotificationFeedbackType.Error).catch(() => undefined);
}

/** Un exercice émis par le serveur : réponse envoyée, correction reçue (la bonne réponse n'est jamais connue avant). */
export function QuestionView({ q, onDone, onResult, continueLabel = 'Continuer', willRetry = false }: { q: IssuedQuestionDto; onDone: (r: AnswerResultDto) => void; onResult?: (r: AnswerResultDto) => void; continueLabel?: string | ((r: AnswerResultDto) => string); willRetry?: boolean }) {
  const [result, setResult] = useState<AnswerResultDto | null>(null);
  const [given, setGiven] = useState<string | string[] | null>(null);
  const [pending, setPending] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const started = useRef(Date.now());

  useEffect(() => {
    started.current = Date.now();
    if (q.type === 'listening_choice' && q.audio) speak(q.audio);
  }, [q.id, q.type, q.audio]);

  async function submit(answer: string | string[]) {
    if (pending || result) return;
    setGiven(answer);
    setPending(true);
    setError(null);
    try {
      const r = await post<AnswerResultDto>(`/questions/${q.id}/answer`, { answer, responseMs: Date.now() - started.current });
      setResult(r);
      vibrate(r.correct);
      onResult?.(r);
      if (r.correct) {
        const t = spokenAfter(q, answer);
        if (t) speak(t);
      }
    } catch (e) {
      setGiven(null);
      setError(e instanceof Error ? e.message : 'Erreur');
    } finally {
      setPending(false);
    }
  }

  const d = q.display ?? {};
  const blank = hasBlank(d.jp);
  const fill = result && blank && !Array.isArray(result.correctAnswer) ? result.correctAnswer : null;
  const mainText = d.jp ? (d.part ? d.jp : fill ? d.jp.replace(/＿+/, `【${fill}】`) : d.jp.replace(/＿+/g, '（　）')) : null;
  const len = d.jp ? [...d.jp].length : 0;

  return (
    <View style={{ gap: 16 }} testID="question">
      <Text style={{ fontSize: 18, fontWeight: '800', color: C.ink }}>{q.prompt}</Text>

      {/* Zone principale */}
      {q.type === 'listening_choice' ? (
        <View style={{ backgroundColor: C.surface2, borderRadius: 24, padding: 24, alignItems: 'center', gap: 12 }}>
          <Button label="🔊  Écouter" onPress={() => q.audio && speak(q.audio)} />
          <Pressable onPress={() => q.audio && speak(q.audio, true)}><Text style={{ color: C.inkSoft, textDecorationLine: 'underline' }}>Écouter lentement</Text></Pressable>
        </View>
      ) : d.lines ? (
        <View style={{ backgroundColor: C.surface2, borderRadius: 24, padding: 18, gap: 10 }}>
          {d.lines.map((l, i) => (
            <View key={i} style={{ flexDirection: 'row', gap: 12, alignItems: 'baseline' }}>
              <Text style={{ width: 64, fontWeight: '700', color: C.inkSoft }}>{l.speaker}</Text>
              <Text style={{ flex: 1, fontSize: 22, color: C.ink }}>{l.jp}</Text>
            </View>
          ))}
          {d.text && <P soft>{d.text}</P>}
        </View>
      ) : mainText || d.text ? (
        <View style={{ backgroundColor: C.surface2, borderRadius: 24, paddingVertical: 22, paddingHorizontal: 16, alignItems: 'center', gap: 6, minHeight: 120, justifyContent: 'center' }}>
          {d.part && <Text style={{ alignSelf: 'flex-start', fontSize: 12, fontWeight: '700', color: C.inkSoft }}>{d.part}</Text>}
          {mainText && !(q.type === 'true_false' && d.text) && (
            <Text style={{ fontSize: d.part ? 26 : q.type === 'true_false' || len > 6 ? 28 : len <= 2 ? 72 : 48, fontWeight: '800', color: C.ink, textAlign: 'center' }}>
              {/* Format JLPT : {{mot}} souligné, ★ et ＿＿ en cases */}
              {mainText.split(/(\{\{.*?\}\})/).map((seg, i) => (seg.startsWith('{{') ? <Text key={i} style={{ textDecorationLine: 'underline' }}>{seg.slice(2, -2)}</Text> : seg))}
            </Text>
          )}
          {d.reading && q.type !== 'reading_choice' && !(q.type === 'fill_blank' && !result) && !blank && <Text style={{ color: C.inkSoft, fontSize: 16 }}>{d.reading}</Text>}
          {d.text && <Text style={{ fontSize: mainText && q.type !== 'true_false' ? 16 : 24, color: mainText && q.type !== 'true_false' ? C.inkSoft : C.ink, fontWeight: mainText && q.type !== 'true_false' ? '400' : '800', textAlign: 'center' }}>{d.text}</Text>}
          {(result ? spokenAfter(q, given ?? '') : q.audio && q.type !== 'reading_choice') && (
            <Pressable accessibilityLabel="Écouter" onPress={() => speak((result ? spokenAfter(q, given ?? '') : q.audio) ?? '')} style={{ position: 'absolute', right: 10, top: 10, padding: 6 }}>
              <Text style={{ fontSize: 20 }}>🔊</Text>
            </Pressable>
          )}
        </View>
      ) : null}

      {/* Réponses */}
      {q.choices && (
        <View style={{ flexDirection: 'row', flexWrap: 'wrap', gap: 10 }}>
          {q.choices.map((c) => {
            const right = result && same(result.correctAnswer, c);
            const wrong = result && given === c && !right;
            const compact = q.choices!.every((x) => [...x].length <= 4);
            return (
              <Pressable
                key={c}
                accessibilityRole="button"
                disabled={!!result || pending}
                onPress={() => submit(c)}
                style={({ pressed }) => ({
                  width: compact && q.choices!.length !== 3 ? '48%' : '100%',
                  minHeight: compact ? 72 : 56,
                  borderRadius: 16,
                  borderWidth: 2,
                  borderColor: right ? C.ok : wrong ? C.ko : C.line,
                  backgroundColor: right ? C.okBg : wrong ? C.koBg : pressed ? C.surface2 : C.surface,
                  opacity: result && !right && !wrong ? 0.55 : 1,
                  alignItems: compact ? 'center' : 'flex-start',
                  justifyContent: 'center',
                  paddingHorizontal: 14,
                })}
              >
                <Text style={{ fontSize: isJp(c) ? (compact ? 28 : 20) : 17, fontWeight: compact ? '800' : '500', color: C.ink }}>{c}</Text>
              </Pressable>
            );
          })}
        </View>
      )}
      {q.type === 'sentence_order' && q.tokens && <SentenceOrder tokens={q.tokens} disabled={!!result || pending} onSubmit={submit} />}
      {q.type === 'matching' && q.pairs && <Matching pairs={q.pairs} disabled={!!result || pending} onSubmit={submit} expected={result && Array.isArray(result.correctAnswer) ? result.correctAnswer : null} />}

      {error && <Text style={{ color: C.ko, fontWeight: '700' }}>{error}</Text>}

      {/* Correction */}
      {result && (
        <View accessibilityLiveRegion="polite" style={{ backgroundColor: result.correct ? C.okBg : C.koBg, borderRadius: 18, padding: 16, gap: 8 }}>
          <View style={{ flexDirection: 'row', alignItems: 'center', gap: 12 }}>
            <View style={{ width: 52, height: 52, borderRadius: 10, borderWidth: 3, borderColor: result.correct ? C.ko : C.ink, alignItems: 'center', justifyContent: 'center', transform: [{ rotate: '-8deg' }] }}>
              <Text style={{ fontSize: 26, fontWeight: '900', color: result.correct ? C.ko : C.ink }}>{result.correct ? '正' : '惜'}</Text>
            </View>
            <View style={{ flex: 1 }}>
              <Text style={{ fontSize: 18, fontWeight: '800', color: C.ink }}>{result.correct ? 'Bonne réponse !' : 'Pas tout à fait.'}</Text>
              {result.xpGained > 0 && <Text style={{ color: C.goldInk, fontWeight: '800' }}>+{result.xpGained} XP</Text>}
            </View>
          </View>
          {!result.correct && q.type !== 'matching' && <P>Réponse attendue : <Text style={{ fontWeight: '800' }}>{Array.isArray(result.correctAnswer) ? result.correctAnswer.join(' ') : result.correctAnswer}</Text></P>}
          <P soft>{result.explanation}</P>
          {!result.correct && willRetry && <P soft>Tu le referas en fin de séance.</P>}
          {result.questsCompleted?.map((qc) => <Text key={qc.title} style={{ color: C.goldInk, fontWeight: '700' }}>Quête accomplie : {qc.title} (+{qc.xp} XP)</Text>)}
          <Button label={typeof continueLabel === 'function' ? continueLabel(result) : continueLabel} onPress={() => onDone(result)} />
        </View>
      )}
    </View>
  );
}

function Chip({ label, onPress, filled, disabled }: { label: string; onPress: () => void; filled?: boolean; disabled?: boolean }) {
  return (
    <Pressable accessibilityRole="button" disabled={disabled} onPress={onPress} style={{ minHeight: 46, paddingHorizontal: 12, justifyContent: 'center', borderRadius: 12, borderWidth: 2, borderColor: filled ? C.ink : C.line, backgroundColor: filled ? C.ink : C.surface }}>
      <Text style={{ fontSize: 20, color: filled ? C.paper : C.ink }}>{label}</Text>
    </Pressable>
  );
}

function SentenceOrder({ tokens, disabled, onSubmit }: { tokens: string[]; disabled: boolean; onSubmit: (a: string[]) => void }) {
  const [placed, setPlaced] = useState<number[]>([]);
  return (
    <View style={{ gap: 12 }}>
      <View style={{ minHeight: 64, flexDirection: 'row', flexWrap: 'wrap', gap: 8, padding: 10, borderRadius: 16, borderWidth: 2, borderColor: C.line, backgroundColor: C.surface }}>
        {placed.length === 0 && <P soft>Touche les morceaux dans le bon ordre.</P>}
        {placed.map((i) => <Chip key={i} label={tokens[i]} filled disabled={disabled} onPress={() => setPlaced(placed.filter((p) => p !== i))} />)}
      </View>
      <View style={{ flexDirection: 'row', flexWrap: 'wrap', gap: 8, justifyContent: 'center' }}>
        {tokens.map((t, i) => (placed.includes(i) ? <View key={i} style={{ minHeight: 46, minWidth: 40, borderRadius: 12, borderWidth: 2, borderStyle: 'dashed', borderColor: C.line }} /> : <Chip key={i} label={t} disabled={disabled} onPress={() => setPlaced([...placed, i])} />))}
      </View>
      {!disabled && <Button label="Vérifier" disabled={placed.length !== tokens.length} onPress={() => onSubmit(placed.map((i) => tokens[i]))} />}
    </View>
  );
}

function Matching({ pairs, disabled, onSubmit, expected }: { pairs: { left: string[]; right: string[] }; disabled: boolean; onSubmit: (a: string[]) => void; expected: string[] | null }) {
  const [assign, setAssign] = useState<Record<number, string>>({});
  const [active, setActive] = useState<number | null>(0);
  const owner = new Map(Object.entries(assign).map(([l, r]) => [r, Number(l)]));
  const choose = (r: string) => {
    if (active === null) return;
    const next = Object.fromEntries(Object.entries(assign).filter(([, v]) => v !== r));
    next[active] = r;
    setAssign(next);
    const free = pairs.left.findIndex((_, i) => next[i] === undefined);
    setActive(free >= 0 ? free : null);
  };
  const badge = (n: number | undefined) => (
    <View style={{ width: 22, height: 22, borderRadius: 11, backgroundColor: n === undefined ? C.surface2 : C.ink, alignItems: 'center', justifyContent: 'center' }}>
      <Text style={{ color: C.paper, fontSize: 12, fontWeight: '800' }}>{n === undefined ? '' : n + 1}</Text>
    </View>
  );
  return (
    <View style={{ gap: 8 }}>
      {pairs.left.map((l, i) => {
        const r = pairs.right[i];
        const ok = expected ? expected[i] === assign[i] : null;
        return (
          <View key={l} style={{ flexDirection: 'row', gap: 8 }}>
            <Pressable accessibilityRole="button" accessibilityLabel={l} accessibilityState={{ selected: active === i }} disabled={disabled} onPress={() => setActive(i)} style={{ flex: 1, minHeight: 52, flexDirection: 'row', alignItems: 'center', gap: 8, padding: 8, borderRadius: 14, borderWidth: 2, backgroundColor: C.surface, borderColor: ok === null ? (active === i ? C.ink : C.line) : ok ? C.ok : C.ko }}>
              {badge(assign[i] !== undefined ? i : undefined)}
              <Text style={{ fontSize: 20, color: C.ink, flexShrink: 1 }}>{l}</Text>
            </Pressable>
            <Pressable testID="match-right" accessibilityRole="button" accessibilityLabel={r} disabled={disabled || active === null} onPress={() => choose(r)} style={{ flex: 1, minHeight: 52, flexDirection: 'row', alignItems: 'center', gap: 8, padding: 8, borderRadius: 14, borderWidth: 2, backgroundColor: C.surface, borderColor: owner.has(r) ? C.inkSoft : C.line }}>
              {badge(owner.get(r))}
              <Text style={{ fontSize: 14, color: C.ink, flexShrink: 1 }}>{r}</Text>
            </Pressable>
          </View>
        );
      })}
      {expected && expected.some((e, i) => e !== assign[i]) && (
        <View style={{ backgroundColor: C.surface2, borderRadius: 14, padding: 10 }}>
          {pairs.left.map((l, i) => <P key={l}>{l} = <Text style={{ fontWeight: expected[i] === assign[i] ? '400' : '800', color: expected[i] === assign[i] ? C.ink : C.ko }}>{expected[i]}</Text></P>)}
        </View>
      )}
      {!disabled && <Button label="Vérifier" disabled={Object.keys(assign).length !== pairs.left.length} onPress={() => onSubmit(pairs.left.map((_, i) => assign[i]))} />}
    </View>
  );
}
