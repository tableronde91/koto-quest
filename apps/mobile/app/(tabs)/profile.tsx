import { ReactNode, useState } from 'react';
import { Pressable, Text, TextInput, View } from 'react-native';
import { useRouter } from 'expo-router';
import { useQueryClient } from '@tanstack/react-query';
import { levelFromXp } from '@koto/learning-engine';
import { examLevelLabel, levelLabel, levelsOfLanguage, type MeDto } from '@koto/shared';
import { put } from '../../src/api';
import { useAuth } from '../../src/auth';
import { FriendsManager } from '../../src/Friends';
import { useDuelLobby } from '../../src/hooks';
import { RankBadge } from '../../src/RankBadge';
import { Avatar } from '../../src/Avatar';
import { C } from '../../src/theme';
import { Button, Card, ErrorBox, H1, H2, Loading, P, ProgressBar, Screen } from '../../src/ui';
import { studyWords } from '../../src/study';
import { T } from '../../src/i18n';

const MINUTES = [10, 15, 20, 30, 45, 60, 90];
const DATE_RE = /^\d{4}-\d{2}-\d{2}$/;

/** Profil : carte d'identité, objectifs et amis. Les réglages de l'appli s'ouvrent d'ici. */
export default function Profile() {
  const router = useRouter();
  const { me } = useAuth();
  const { data: lobby } = useDuelLobby();
  if (!me) return <Loading />;
  const lv = levelFromXp(me.xp);

  return (
    <Screen>
      <View style={{ flexDirection: 'row', alignItems: 'center', gap: 8 }}>
        <H1 style={{ flex: 1 }}>{T('Profil')}</H1>
        <Pressable accessibilityRole="button" accessibilityLabel={T('Réglages')} onPress={() => router.push('/settings')} style={{ flexDirection: 'row', alignItems: 'center', gap: 6, borderWidth: 2, borderColor: C.line, borderRadius: 99, paddingHorizontal: 12, minHeight: 40 }}>
          <Text style={{ fontWeight: '900', color: C.ink }}>設</Text>
          <Text style={{ fontWeight: '800', color: C.ink }}>{T('Réglages')}</Text>
        </Pressable>
      </View>

      {/* Carte d'identité */}
      <View testID="identity" style={{ backgroundColor: C.ink, borderRadius: 24, padding: 20, gap: 12, overflow: 'hidden' }}>
        <Text style={{ position: 'absolute', right: -6, top: -26, fontSize: 140, fontWeight: '900', color: '#ffffff', opacity: 0.08 }}>人</Text>
        <View style={{ flexDirection: 'row', alignItems: 'center', gap: 14 }}>
          <Pressable accessibilityRole="button" accessibilityLabel={T('Mon personnage')} onPress={() => router.push('/character')} style={{ borderRadius: 20, overflow: 'hidden', borderWidth: 2, borderColor: '#ffffff44' }}>
            <Avatar config={me.avatar} size={72} />
          </Pressable>
          <View style={{ flex: 1, gap: 2 }}>
            <Text style={{ color: C.paper, fontSize: 24, fontWeight: '800' }}>{me.displayName}</Text>
            <Text style={{ color: C.paper, opacity: 0.85 }}>{T('Niveau {0} · objectif {1}', [lv.level, examLevelLabel(me.preferences.targetLevel)])}</Text>
          </View>
          {lobby && (
            <View style={{ alignItems: 'center', gap: 2 }}>
              <RankBadge rank={lobby.profile.rank} size={48} />
              <Text style={{ color: C.paper, fontSize: 11, fontWeight: '700' }}>{lobby.profile.rank.label}</Text>
            </View>
          )}
        </View>
        <View style={{ flexDirection: 'row' }}><ProgressBar value={lv.intoLevel} max={Math.max(1, lv.forNext)} color={C.gold} label={T('XP du niveau')} /></View>
        <Text style={{ color: C.paper, opacity: 0.75, fontSize: 13 }}>{T('{0} / {1} XP', [lv.intoLevel, lv.forNext])} · 🪙 {me.coins}</Text>
        <View style={{ flexDirection: 'row', gap: 10 }}>
          <Button tone="gold" label={T('Personnaliser')} onPress={() => router.push('/character')} style={{ flex: 1 }} />
          <Button tone="quiet" label={T('Mes succès')} onPress={() => router.push('/achievements')} style={{ flex: 1, backgroundColor: C.surface }} />
        </View>
        <Button tone="quiet" label={T('Mon aventure')} onPress={() => router.push('/progress')} style={{ backgroundColor: C.surface }} />
      </View>

      <Goals me={me} />

      {lobby ? <FriendsManager code={lobby.profile.code} /> : null}
    </Screen>
  );
}

function Goals({ me }: { me: MeDto }) {
  const qc = useQueryClient();
  const p = me.preferences;
  const [name, setName] = useState(me.displayName);
  const [exam, setExam] = useState(p.examDate ?? '');
  const [err, setErr] = useState<unknown>(null);

  async function save(body: Record<string, unknown>) {
    setErr(null);
    try {
      const next = await put<MeDto>('/me/preferences', body);
      qc.setQueryData(['me'], next);
      void qc.invalidateQueries({ predicate: (q) => q.queryKey[0] !== 'me' });
    } catch (e) {
      setErr(e);
    }
  }

  return (
    <Card style={{ gap: 14 }}>
      <H2>{T('Identité et objectifs')}</H2>
      <Field label={T('Pseudo')}>
        <TextInput
          value={name}
          onChangeText={setName}
          maxLength={40}
          accessibilityLabel={T('Pseudo')}
          onEndEditing={() => name.trim() && name.trim() !== me.displayName && save({ displayName: name.trim() })}
          onBlur={() => name.trim() && name.trim() !== me.displayName && save({ displayName: name.trim() })}
          style={inputStyle}
        />
      </Field>
      <P soft style={{ fontSize: 13 }}>{T('Tu étudies {0}. La langue se change dans les Réglages.', [studyWords(p.studyLanguage ?? 'ja').theLanguage])}</P>
      <Field label={T('Niveau visé')}>
        <Chips label={T('Niveau visé')} options={levelsOfLanguage(p.studyLanguage ?? 'ja').map((l) => ({ value: l, label: levelLabel(l) }))} value={p.targetLevel} onChange={(v) => save({ targetLevel: v })} />
      </Field>
      <Field label={T('Temps d’étude par jour')}>
        <Chips label={T('Temps d’étude par jour')} options={MINUTES.map((m) => ({ value: m, label: T('{0} min', [m]) }))} value={p.minutesPerDay} onChange={(v) => save({ minutesPerDay: v })} />
      </Field>
      <Field label={T('Date d’examen')}>
        <TextInput
          value={exam}
          onChangeText={setExam}
          placeholder={T('AAAA-MM-JJ (facultatif)')}
          placeholderTextColor={C.inkSoft}
          accessibilityLabel={T('Date d’examen')}
          keyboardType="numbers-and-punctuation"
          maxLength={10}
          onBlur={() => {
            const v = exam.trim();
            if (v === (p.examDate ?? '')) return;
            if (!v) return void save({ examDate: null });
            if (DATE_RE.test(v) && !Number.isNaN(Date.parse(v))) void save({ examDate: v });
            else setErr(new Error(T('Date attendue au format AAAA-MM-JJ, par exemple 2027-07-04.')));
          }}
          style={inputStyle}
        />
      </Field>
      {err != null && <ErrorBox error={err} />}
    </Card>
  );
}

const inputStyle = { borderWidth: 2, borderColor: C.line, borderRadius: 14, paddingHorizontal: 12, fontSize: 16, color: C.ink, minHeight: 48 } as const;

function Field({ label, children }: { label: string; children: ReactNode }) {
  return (
    <View style={{ gap: 6 }}>
      <Text style={{ fontWeight: '800', color: C.ink }}>{label}</Text>
      {children}
    </View>
  );
}

function Chips<V extends string | number>({ label, options, value, onChange }: { label: string; options: { value: V; label: string }[]; value: V; onChange: (v: V) => void }) {
  return (
    <View accessibilityRole="radiogroup" accessibilityLabel={label} style={{ flexDirection: 'row', flexWrap: 'wrap', gap: 8 }}>
      {options.map((o) => {
        const on = o.value === value;
        return (
          <Pressable key={String(o.value)} accessibilityRole="radio" accessibilityState={{ checked: on }} accessibilityLabel={o.label} onPress={() => !on && onChange(o.value)} style={{ paddingHorizontal: 14, paddingVertical: 8, borderRadius: 99, borderWidth: 2, borderColor: on ? C.ink : C.line, backgroundColor: on ? C.ink : C.surface }}>
            <Text style={{ fontWeight: '800', color: on ? C.paper : C.inkSoft }}>{o.label}</Text>
          </Pressable>
        );
      })}
    </View>
  );
}
