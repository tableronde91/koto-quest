import { useState } from 'react';
import { Pressable, ScrollView, Text, View } from 'react-native';
import { useRouter } from 'expo-router';
import type { PathLessonDto, PathWorldDto } from '@koto/shared';
import { usePath } from '../../src/hooks';
import { sagaFor, storyChapter } from '../../src/story';
import { C } from '../../src/theme';
import { ErrorBox, Loading, P, Screen, Seal } from '../../src/ui';

const STATUS_GLYPH: Record<PathLessonDto['status'], string> = { completed: '済', in_progress: '進', available: '道', locked: '錠' };

const worldDone = (w: PathWorldDto) => (w.exam && w.progress.total === 0 ? w.exam.passed : w.boss ? w.boss.defeated : w.progress.total > 0 && w.progress.completed === w.progress.total);

/** Parcours en mode histoire : un onglet par niveau (une saga par héros), un chapitre par île. */
export default function PathScreen() {
  const router = useRouter();
  const [level, setLevel] = useState('N5');
  const [more, setMore] = useState(false);
  const { data, isLoading, error, refetch } = usePath(level);
  if (isLoading) return <Loading />;
  if (error || !data) return <Screen><ErrorBox error={error} onRetry={refetch} /></Screen>;
  const saga = sagaFor(data.level.code);
  const color = saga?.color ?? C.ink;
  const sagaDone = data.worlds.length > 0 && data.worlds.every((w) => !w.comingSoon && worldDone(w));
  return (
    <Screen>
      <ScrollView horizontal showsHorizontalScrollIndicator={false} contentContainerStyle={{ gap: 8 }} accessibilityRole="tablist">
        {data.levels.map((l) => {
          const on = l.code === data.level.code;
          return (
            <Pressable key={l.code} accessibilityRole="tab" accessibilityState={{ selected: on }} accessibilityLabel={`${l.code}, ${sagaFor(l.code)?.short ?? ''}, ${l.completed}/${l.lessons} leçons`} onPress={() => { setLevel(l.code); setMore(false); }} style={{ minWidth: 104, borderRadius: 16, borderWidth: 2, borderColor: on ? C.ink : C.line, backgroundColor: on ? C.ink : C.surface, padding: 10 }}>
              <Text style={{ fontSize: 20, fontWeight: '900', color: on ? C.paper : C.ink }}>{l.code}</Text>
              <Text style={{ color: on ? C.paper : C.ink, fontWeight: '700', fontSize: 13 }}>{sagaFor(l.code)?.short ?? l.title}</Text>
              <Text style={{ color: on ? C.paper : C.inkSoft, fontSize: 12 }}>{l.completed}/{l.lessons} leçons</Text>
            </Pressable>
          );
        })}
      </ScrollView>

      {saga && (
        <View style={{ borderRadius: 24, overflow: 'hidden', borderWidth: 2, borderColor: color, backgroundColor: C.surface }}>
          <View style={{ backgroundColor: color, padding: 14, flexDirection: 'row', alignItems: 'center', gap: 12 }}>
            <View style={{ width: 52, height: 52, borderRadius: 14, borderWidth: 2, borderColor: 'rgba(255,255,255,0.7)', backgroundColor: 'rgba(0,0,0,0.15)', alignItems: 'center', justifyContent: 'center' }}>
              <Text style={{ fontSize: 30, fontWeight: '900', color: '#fff' }}>{saga.glyph}</Text>
            </View>
            <View style={{ flex: 1 }}>
              <Text style={{ color: '#fff', fontSize: 12, fontWeight: '800', opacity: 0.9 }}>MODE HISTOIRE · {saga.hero.toUpperCase()}</Text>
              <Text accessibilityRole="header" style={{ color: '#fff', fontSize: 24, fontWeight: '800' }}>{data.level.code} : {saga.title}</Text>
              <Text style={{ color: '#fff', opacity: 0.9 }}>{saga.jp}</Text>
            </View>
          </View>
          <View style={{ padding: 14, gap: 8 }}>
            <P style={{ lineHeight: 23 }} >{more ? saga.prologue : `${saga.prologue.slice(0, 150).replace(/\s\S*$/, '')}…`}</P>
            {sagaDone && <P style={{ fontWeight: '800', color }}>{saga.epilogue}</P>}
            <Pressable accessibilityRole="button" onPress={() => setMore(!more)} style={{ minHeight: 44, justifyContent: 'center' }}>
              <Text style={{ fontWeight: '800', textDecorationLine: 'underline', color: C.ink }}>{more ? 'Replier' : 'Lire la suite'}</Text>
            </Pressable>
          </View>
        </View>
      )}

      {data.worlds.map((w) => (
        <Island
          key={w.slug}
          w={w}
          color={color}
          onLesson={(slug) => router.push(`/lesson/${slug}`)}
          onBoss={() => router.push({ pathname: '/boss/[slug]', params: { slug: w.slug, order: String(w.order), name: w.boss?.name ?? '', glyph: w.boss?.glyph ?? '' } })}
          onExam={() => w.exam && router.push({ pathname: '/exam/[slug]', params: { slug: w.exam.slug, title: w.title } })}
        />
      ))}
    </Screen>
  );
}

function Island({ w, color, onLesson, onBoss, onExam }: { w: PathWorldDto; color: string; onLesson: (slug: string) => void; onBoss: () => void; onExam: () => void }) {
  const lessons = w.chapters.flatMap((c) => c.lessons);
  const ch = storyChapter(w.slug);
  const done = !w.comingSoon && worldDone(w);
  return (
    <View style={{ borderRadius: 24, overflow: 'hidden', backgroundColor: C.surface, borderWidth: 1, borderColor: C.line }}>
      <View style={{ backgroundColor: color, padding: 14, flexDirection: 'row', alignItems: 'center', gap: 12 }}>
        <View style={{ flex: 1 }}>
          <Text accessibilityRole="header" style={{ color: '#FFFFFF', fontWeight: '800', fontSize: 18 }}>{ch ? `Chapitre ${w.order} · ${ch.title}` : `Île ${w.order} · ${w.title}`}</Text>
          {ch && <Text style={{ color: '#FFFFFF', opacity: 0.9, fontWeight: '700', fontSize: 13 }}>Île {w.order} · {w.title}</Text>}
        </View>
        {w.boss && <Seal glyph={w.boss.glyph} size={40} color={w.boss.defeated ? C.ok : 'rgba(0,0,0,0.35)'} />}
      </View>
      <View style={{ padding: 14, gap: 4 }}>
        {ch && (
          <View style={{ borderLeftWidth: 4, borderLeftColor: color, backgroundColor: C.surface2, borderRadius: 10, padding: 10, gap: 6, marginBottom: 6 }}>
            <P style={{ lineHeight: 23 }}>{ch.intro}</P>
            {done && <P style={{ fontWeight: '800', color }}>済 {ch.outro}</P>}
          </View>
        )}
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
          <Pressable accessibilityRole="button" accessibilityLabel={`Gardien : ${w.boss.name}${w.boss.defeated ? ', vaincu' : w.boss.available ? ', prêt au combat' : ', termine les leçons pour l’affronter'}`} disabled={!w.boss.available && !w.boss.defeated} onPress={onBoss} style={{ flexDirection: 'row', alignItems: 'center', gap: 10, marginTop: 6, padding: 10, borderRadius: 14, backgroundColor: w.boss.available && !w.boss.defeated ? '#FBEFD9' : C.surface2, borderWidth: 2, borderColor: w.boss.available && !w.boss.defeated ? C.gold : 'transparent' }}>
            <Seal glyph={w.boss.glyph} size={36} color={w.boss.defeated ? C.ok : C.seal} />
            <View style={{ flex: 1 }}>
              <Text style={{ color: C.ink, fontWeight: '800' }}>{w.boss.name}</Text>
              <Text style={{ color: C.inkSoft, fontSize: 13 }}>{w.boss.defeated ? 'Vaincu · revanche possible' : w.boss.available ? 'Prêt : touche pour combattre' : 'Termine les leçons de l’île pour l’affronter'}</Text>
            </View>
          </Pressable>
        )}
        {w.exam && (
          <Pressable accessibilityRole="button" accessibilityLabel={`Examen blanc : ${w.title}`} onPress={onExam} style={{ flexDirection: 'row', alignItems: 'center', gap: 10, marginTop: 6, padding: 12, borderRadius: 14, backgroundColor: '#FBEFD9', borderWidth: 2, borderColor: C.gold }}>
            <Text style={{ fontSize: 22, fontWeight: '900', color: C.ko }}>模試</Text>
            <View style={{ flex: 1 }}>
              <Text style={{ color: C.ink, fontWeight: '800' }}>Passer l’examen blanc</Text>
              <Text style={{ color: C.inkSoft, fontSize: 13 }}>{w.exam.attempts ? `Meilleur score : ${w.exam.bestPercent} %${w.exam.passed ? ', seuil atteint' : ''}` : 'Chronométré, non officiel'}</Text>
            </View>
          </Pressable>
        )}
      </View>
    </View>
  );
}
