import { useEffect, useRef, useState } from 'react';
import { Pressable, Text, View } from 'react-native';
import type { IssuedQuestionDto } from '@koto/shared';
import { speak, speakScript } from './speech';
import { C } from './theme';
import { Button, P } from './ui';
import { T, plural } from './i18n';

const JP = /[぀-ヿ一-龯]/;
export type ExamAnswer = string | string[] | undefined;

/** Question d'épreuve : réponse choisie (modifiable), sans correction avant la fin. Même logique que le web. */
export function ExamQuestion({ q, number, value, onChange }: { q: IssuedQuestionDto; number: number; value: ExamAnswer; onChange: (v: ExamAnswer) => void }) {
  const d = q.display ?? {};
  const script = q.type === 'listening_choice' && q.audio ? q.audio : null;
  const legacy = !!script && !script.includes('|');
  const [plays, setPlays] = useState(0);
  const auto = useRef<string | null>(null);
  const left = d.maxPlays === undefined ? Infinity : d.maxPlays - plays;
  const play = () => {
    if (!script || left <= 0) return;
    setPlays((p) => p + 1);
    if (legacy) speak(script);
    else speakScript(script);
  };
  useEffect(() => {
    if (auto.current === q.id || !script) return;
    auto.current = q.id;
    play();
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [q.id]);

  return (
    <View style={{ gap: 14 }} testID="exam-question">
      {d.part && <Text style={{ fontSize: 13, fontWeight: '700', color: C.inkSoft }}>{d.part}</Text>}
      <Text style={{ fontSize: 18, fontWeight: '800', color: C.ink }}><Text style={{ color: C.inkSoft }}>{number}. </Text>{q.prompt}</Text>

      {script ? (
        <View style={{ backgroundColor: C.surface2, borderRadius: 24, padding: 18, alignItems: 'center', gap: 8 }}>
          <Button label={left <= 0 ? T('Plus d’écoute disponible') : `🔊  ${T('Écouter')}`} disabled={left <= 0} onPress={play} />
          {d.maxPlays !== undefined && <P soft>{plural(Math.max(0, left), '{0} écoute restante sur {1}', '{0} écoutes restantes sur {1}', [Math.max(0, left), d.maxPlays])}</P>}
          {d.text && <Text style={{ fontSize: 20, fontWeight: '800', color: C.ink, textAlign: 'center' }}>{d.text}</Text>}
        </View>
      ) : d.passage ? (
        <View style={{ gap: 8 }}>
          <View style={{ borderWidth: 2, borderColor: C.line, borderRadius: 18, padding: 14, backgroundColor: C.surface }}>
            <Text style={{ fontSize: 18, lineHeight: 30, color: C.ink }}>{d.passage}</Text>
          </View>
          {d.text && <Text style={{ fontSize: 19, fontWeight: '800', color: C.ink }}>{d.text}</Text>}
        </View>
      ) : d.lines ? (
        <View style={{ backgroundColor: C.surface2, borderRadius: 24, padding: 16, gap: 8 }}>
          {d.lines.map((l, i) => (
            <View key={i} style={{ flexDirection: 'row', gap: 12 }}>
              <Text style={{ width: 60, fontWeight: '700', color: C.inkSoft }}>{l.speaker}</Text>
              <Text style={{ flex: 1, fontSize: 20, color: C.ink }}>{l.jp}</Text>
            </View>
          ))}
          {d.text && <P soft>{d.text}</P>}
        </View>
      ) : d.jp || d.text ? (
        <View style={{ backgroundColor: C.surface2, borderRadius: 24, padding: 18, alignItems: 'center', gap: 6 }}>
          {d.jp && !(q.type === 'true_false' && d.text) && (
            <Text style={{ fontSize: [...d.jp].length <= 3 ? 56 : 26, fontWeight: '800', color: C.ink, textAlign: 'center', lineHeight: [...d.jp].length <= 3 ? 70 : 40 }}>
              {d.jp.replace(/＿+/g, '（　）').split(/(\{\{.*?\}\})/).map((seg, i) => (seg.startsWith('{{') ? <Text key={i} style={{ textDecorationLine: 'underline' }}>{seg.slice(2, -2)}</Text> : seg))}
            </Text>
          )}
          {d.text && <Text style={{ fontSize: d.jp && q.type !== 'true_false' ? 16 : 22, color: d.jp && q.type !== 'true_false' ? C.inkSoft : C.ink, textAlign: 'center' }}>{d.text}</Text>}
        </View>
      ) : null}

      {q.choices && (
        <View style={{ gap: 10 }} accessibilityRole="radiogroup">
          {q.choices.map((c, i) => {
            const on = value === c;
            return (
              <Pressable key={c} accessibilityRole="radio" accessibilityState={{ checked: on }} accessibilityLabel={d.audioChoices ? T('Réponse {0}', [i + 1]) : c} onPress={() => onChange(c)} style={{ minHeight: 54, flexDirection: 'row', alignItems: 'center', gap: 12, paddingHorizontal: 14, borderRadius: 16, borderWidth: 2, borderColor: on ? C.ink : C.line, backgroundColor: on ? C.surface2 : C.surface }}>
                <View style={{ width: 22, height: 22, borderRadius: 11, borderWidth: 2, borderColor: C.ink, alignItems: 'center', justifyContent: 'center' }}>{on && <View style={{ width: 11, height: 11, borderRadius: 6, backgroundColor: C.ink }} />}</View>
                {d.audioChoices ? (
                  <View style={{ flex: 1, flexDirection: 'row', justifyContent: 'space-between', alignItems: 'center' }}>
                    <Text style={{ fontSize: 20, fontWeight: '800', color: C.ink }}>{i + 1}</Text>
                    <Pressable accessibilityRole="button" accessibilityLabel={T('Écouter la réponse {0}', [i + 1])} onPress={() => speak(c)} style={{ padding: 8 }}><Text>🔊</Text></Pressable>
                  </View>
                ) : (
                  <Text style={{ flex: 1, fontSize: JP.test(c) ? 20 : 17, color: C.ink }}>{c}</Text>
                )}
              </Pressable>
            );
          })}
        </View>
      )}

      {q.type === 'sentence_order' && q.tokens && <OrderPicker tokens={q.tokens} value={Array.isArray(value) ? value : []} onChange={(v) => onChange(v.length ? v : undefined)} />}
    </View>
  );
}

function OrderPicker({ tokens, value, onChange }: { tokens: string[]; value: string[]; onChange: (v: string[]) => void }) {
  const used: number[] = [];
  for (const v of value) {
    const i = tokens.findIndex((t, k) => t === v && !used.includes(k));
    if (i >= 0) used.push(i);
  }
  const chip = (label: string, filled: boolean, onPress: () => void, key: number) => (
    <Pressable key={key} accessibilityRole="button" onPress={onPress} style={{ minHeight: 46, paddingHorizontal: 12, justifyContent: 'center', borderRadius: 12, borderWidth: 2, borderColor: filled ? C.ink : C.line, backgroundColor: filled ? C.ink : C.surface }}>
      <Text style={{ fontSize: 20, color: filled ? C.paper : C.ink }}>{label}</Text>
    </Pressable>
  );
  return (
    <View style={{ gap: 10 }}>
      <View style={{ minHeight: 60, flexDirection: 'row', flexWrap: 'wrap', gap: 8, padding: 10, borderRadius: 16, borderWidth: 2, borderColor: C.line, backgroundColor: C.surface }}>
        {value.length === 0 && <P soft>{T('Touche les morceaux dans le bon ordre.')}</P>}
        {used.map((i, k) => chip(tokens[i], true, () => onChange(value.filter((_, j) => j !== k)), k))}
      </View>
      <View style={{ flexDirection: 'row', flexWrap: 'wrap', gap: 8, justifyContent: 'center' }}>
        {tokens.map((t, i) => (used.includes(i) ? <View key={i} style={{ minHeight: 46, minWidth: 40, borderRadius: 12, borderWidth: 2, borderStyle: 'dashed', borderColor: C.line }} /> : chip(t, false, () => onChange([...value, t]), i)))}
      </View>
    </View>
  );
}
