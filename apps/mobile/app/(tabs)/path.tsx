import { useState } from 'react';
import { Pressable, Text, View } from 'react-native';
import { useRouter } from 'expo-router';
import type { PathLessonDto, PathWorldDto } from '@koto/shared';
import { usePath } from '../../src/hooks';
import { C } from '../../src/theme';
import { ErrorBox, H1, Loading, P, Screen, Seal } from '../../src/ui';

const STATUS_GLYPH: Record<PathLessonDto['status'], string> = { completed: '済', in_progress: '進', available: '道', locked: '錠' };

/** Parcours : un onglet par niveau, une carte par île, un sentier de leçons. */
export default function PathScreen() {
  const router = useRouter();
  const [level, setLevel] = useState('N5');
  const { data, isLoading, error, refetch } = usePath(level);
  if (isLoading) return <Loading />;
  if (error || !data) return <Screen><ErrorBox error={error} onRetry={refetch} /></Screen>;
  return (
    <Screen>
      <H1>{data.level.code} : {data.level.region}</H1>
      <View style={{ flexDirection: 'row', gap: 8 }}>
        {data.levels.map((l) => {
          const on = l.code === data.level.code;
          return (
            <Pressable key={l.code} accessibilityRole="tab" accessibilityState={{ selected: on }} onPress={() => setLevel(l.code)} style={{ flex: 1, borderRadius: 16, borderWidth: 2, borderColor: on ? C.ink : C.line, backgroundColor: on ? C.ink : C.surface, padding: 10 }}>
              <Text style={{ fontSize: 20, fontWeight: '900', color: on ? C.paper : C.ink }}>{l.code}</Text>
              <Text style={{ color: on ? C.paper : C.inkSoft, fontSize: 12 }}>{l.completed}/{l.lessons} leçons</Text>
            </Pressable>
          );
        })}
      </View>
      {data.worlds.map((w) => <Island key={w.slug} w={w} onLesson={(slug) => router.push(`/lesson/${slug}`)} />)}
    </Screen>
  );
}

function Island({ w, onLesson }: { w: PathWorldDto; onLesson: (slug: string) => void }) {
  const lessons = w.chapters.flatMap((c) => c.lessons);
  const done = w.progress.completed === w.progress.total && w.progress.total > 0;
  return (
    <View style={{ borderRadius: 24, overflow: 'hidden', backgroundColor: C.surface, borderWidth: 1, borderColor: C.line }}>
      <View style={{ backgroundColor: '#1A8C9C', padding: 14, flexDirection: 'row', alignItems: 'center', gap: 12 }}>
        <View style={{ width: 54, height: 40, borderRadius: 20, backgroundColor: '#EBD9AE', borderBottomWidth: 6, borderBottomColor: '#7D7468', alignItems: 'center', justifyContent: 'center' }}>
          <Text style={{ fontSize: 18 }}>{w.exam ? '⛩️' : done ? '🌸' : '🌴'}</Text>
        </View>
        <View style={{ flex: 1 }}>
          <Text style={{ color: '#E6FFFB', fontWeight: '700', fontSize: 12 }}>Île {w.order}</Text>
          <Text style={{ color: '#FFFFFF', fontWeight: '800', fontSize: 18 }}>{w.title}</Text>
        </View>
        {w.boss && <Seal glyph={w.boss.glyph} size={40} color={w.boss.defeated ? C.ok : C.seal} />}
      </View>
      <View style={{ padding: 14, gap: 4 }}>
        <P soft>{w.description}</P>
        {w.comingSoon && <P soft>Bientôt disponible.</P>}
        {lessons.map((l) => {
          const locked = l.status === 'locked';
          return (
            <Pressable key={l.slug} accessibilityRole="button" accessibilityLabel={`${l.title}, ${locked ? 'verrouillée' : l.status === 'completed' ? 'terminée' : 'disponible'}`} disabled={locked} onPress={() => onLesson(l.slug)} style={{ flexDirection: 'row', alignItems: 'center', gap: 12, paddingVertical: 8, opacity: locked ? 0.55 : 1 }}>
              <View style={{ width: 44, height: 44, borderRadius: 22, borderWidth: 3, borderColor: locked ? C.line : C.ink, backgroundColor: l.status === 'completed' ? C.ok : l.status === 'available' || l.status === 'in_progress' ? C.gold : C.surface2, alignItems: 'center', justifyContent: 'center' }}>
                <Text style={{ fontWeight: '900', color: l.status === 'completed' ? '#fff' : C.ink }}>{STATUS_GLYPH[l.status]}</Text>
              </View>
              <View style={{ flex: 1 }}>
                <Text style={{ fontWeight: '700', color: C.ink, fontSize: 16 }}>{l.title}</Text>
                <Text style={{ color: C.inkSoft, fontSize: 12 }}>{l.minutes} min · {l.itemCount} notions</Text>
              </View>
            </Pressable>
          );
        })}
        {w.boss && (
          <View style={{ flexDirection: 'row', alignItems: 'center', gap: 10, marginTop: 6, padding: 10, borderRadius: 14, backgroundColor: C.surface2 }}>
            <Text style={{ fontSize: 20 }}>👹</Text>
            <Text style={{ flex: 1, color: C.ink }}><Text style={{ fontWeight: '800' }}>{w.boss.name}</Text>{w.boss.defeated ? ' — vaincu' : w.boss.available ? ' — prêt (combat sur la version web)' : ''}</Text>
          </View>
        )}
        {w.exam && <P soft>Examen blanc {w.exam.bestPercent !== null ? `· meilleur score ${w.exam.bestPercent} %` : ''} (sur la version web)</P>}
      </View>
    </View>
  );
}
