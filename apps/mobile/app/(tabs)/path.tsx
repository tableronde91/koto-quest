import type { DecorKey } from '@koto/shared';
import { useDecor } from '../../src/study';
import { useState } from 'react';
import { Pressable, ScrollView, Text, View } from 'react-native';
import { useRouter } from 'expo-router';
import { languageOfLevel, levelLabel, type PathLessonDto, type PathWorldDto } from '@koto/shared';
import { useAuth } from '../../src/auth';
import { usePath } from '../../src/hooks';
import { sagaFor, storyChapter } from '../../src/story';
import { C } from '../../src/theme';
import { ErrorBox, Loading, P, Screen, Seal } from '../../src/ui';
import { T } from '../../src/i18n';

const STATUS_GLYPH: Record<PathLessonDto['status'], DecorKey> = { completed: 'completed', in_progress: 'inProgress', available: 'open', locked: 'locked' };

const worldDone = (w: PathWorldDto) => (w.exam && w.progress.total === 0 ? w.exam.passed : w.boss ? w.boss.defeated : w.progress.total > 0 && w.progress.completed === w.progress.total);

/** Parcours en mode histoire : un onglet par niveau (une saga par héros), un chapitre par île. */
export default function PathScreen() {
  const router = useRouter();
  const { me } = useAuth();
  const target = me?.preferences.targetLevel ?? 'N5';
  const [picked, setLevel] = useState<string | null>(null);
  // Le niveau affiché suit le niveau visé, et revient à lui après un changement de langue étudiée
  const level = picked && languageOfLevel(picked) === languageOfLevel(target) ? picked : target;
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
            <Pressable key={l.code} accessibilityRole="tab" accessibilityState={{ selected: on }} accessibilityLabel={`${levelLabel(l.code)}, ${sagaFor(l.code)?.short ?? ''}, ${T('{0}/{1} leçons', [l.completed, l.lessons])}`} onPress={() => { setLevel(l.code); setMore(false); }} style={{ minWidth: 104, borderRadius: 16, borderWidth: 2, borderColor: on ? C.ink : C.line, backgroundColor: on ? C.ink : C.surface, padding: 10 }}>
              <Text style={{ fontSize: 20, fontWeight: '900', color: on ? C.paper : C.ink }}>{levelLabel(l.code)}</Text>
              <Text style={{ color: on ? C.paper : C.ink, fontWeight: '700', fontSize: 13 }}>{sagaFor(l.code)?.short ?? l.title}</Text>
              <Text style={{ color: on ? C.paper : C.inkSoft, fontSize: 12 }}>{T('{0}/{1} leçons', [l.completed, l.lessons])}</Text>
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
              <Text style={{ color: '#fff', fontSize: 12, fontWeight: '800', opacity: 0.9 }}>{T('MODE HISTOIRE · {0}', [saga.hero.toUpperCase()])}</Text>
              <Text accessibilityRole="header" style={{ color: '#fff', fontSize: 24, fontWeight: '800' }}>{T('{0} : {1}', [levelLabel(data.level.code), saga.title])}</Text>
              <Text style={{ color: '#fff', opacity: 0.9 }}>{saga.jp}</Text>
            </View>
          </View>
          <View style={{ padding: 14, gap: 8 }}>
            <P style={{ lineHeight: 23 }} >{more ? saga.prologue : `${saga.prologue.slice(0, 150).replace(/\s\S*$/, '')}…`}</P>
            {sagaDone && <P style={{ fontWeight: '800', color }}>{saga.epilogue}</P>}
            <Pressable accessibilityRole="button" onPress={() => setMore(!more)} style={{ minHeight: 44, justifyContent: 'center' }}>
              <Text style={{ fontWeight: '800', textDecorationLine: 'underline', color: C.ink }}>{more ? T('Replier') : T('Lire la suite')}</Text>
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
  const D = useDecor();
  const lessons = w.chapters.flatMap((c) => c.lessons);
  const ch = storyChapter(w.slug);
  const done = !w.comingSoon && worldDone(w);
  return (
    <View style={{ borderRadius: 24, overflow: 'hidden', backgroundColor: C.surface, borderWidth: 1, borderColor: C.line }}>
      <View style={{ backgroundColor: color, padding: 14, flexDirection: 'row', alignItems: 'center', gap: 12 }}>
        <View style={{ flex: 1 }}>
          <Text accessibilityRole="header" style={{ color: '#FFFFFF', fontWeight: '800', fontSize: 18 }}>{ch ? T('Chapitre {0} · {1}', [w.order, ch.title]) : T('Île {0} · {1}', [w.order, w.title])}</Text>
          {ch && <Text style={{ color: '#FFFFFF', opacity: 0.9, fontWeight: '700', fontSize: 13 }}>{T('Île {0} · {1}', [w.order, w.title])}</Text>}
        </View>
        {w.boss && <Seal glyph={w.boss.glyph} size={40} color={w.boss.defeated ? C.ok : 'rgba(0,0,0,0.35)'} />}
      </View>
      <View style={{ padding: 14, gap: 4 }}>
        {ch && (
          <View style={{ borderLeftWidth: 4, borderLeftColor: color, backgroundColor: C.surface2, borderRadius: 10, padding: 10, gap: 6, marginBottom: 6 }}>
            <P style={{ lineHeight: 23 }}>{ch.intro}</P>
            {done && <P style={{ fontWeight: '800', color }}>{D('questDone')} {ch.outro}</P>}
          </View>
        )}
        <P soft>{w.description}</P>
        {w.comingSoon && <P soft>{T('Bientôt disponible.')}</P>}
        {lessons.map((l) => {
          const locked = l.status === 'locked';
          return (
            <Pressable key={l.slug} accessibilityRole="button" accessibilityLabel={`${l.title}, ${locked ? T('verrouillée') : l.status === 'completed' ? T('terminée') : T('disponible')}`} disabled={locked} onPress={() => onLesson(l.slug)} style={{ flexDirection: 'row', alignItems: 'center', gap: 12, paddingVertical: 8, opacity: locked ? 0.55 : 1 }}>
              <View style={{ width: 44, height: 44, borderRadius: 22, borderWidth: 3, borderColor: locked ? C.line : C.ink, backgroundColor: l.status === 'completed' ? C.ok : l.status === 'available' || l.status === 'in_progress' ? C.gold : C.surface2, alignItems: 'center', justifyContent: 'center' }}>
                <Text style={{ fontWeight: '900', color: l.status === 'completed' ? '#fff' : C.ink }}>{D(STATUS_GLYPH[l.status])}</Text>
              </View>
              <View style={{ flex: 1 }}>
                <Text style={{ fontWeight: '700', color: C.ink, fontSize: 16 }}>{l.title}</Text>
                <Text style={{ color: C.inkSoft, fontSize: 12 }}>{T('{0} min · {1} notions', [l.minutes, l.itemCount])}</Text>
              </View>
            </Pressable>
          );
        })}
        {w.boss && (
          <Pressable accessibilityRole="button" accessibilityLabel={`${T('Gardien : {0}', [w.boss.name])}${w.boss.defeated ? T(', vaincu') : w.boss.available ? T(', prêt au combat') : T(', termine les leçons pour l’affronter')}`} disabled={!w.boss.available && !w.boss.defeated} onPress={onBoss} style={{ flexDirection: 'row', alignItems: 'center', gap: 10, marginTop: 6, padding: 10, borderRadius: 14, backgroundColor: w.boss.available && !w.boss.defeated ? '#FBEFD9' : C.surface2, borderWidth: 2, borderColor: w.boss.available && !w.boss.defeated ? C.gold : 'transparent' }}>
            <Seal glyph={w.boss.glyph} size={36} color={w.boss.defeated ? C.ok : C.seal} />
            <View style={{ flex: 1 }}>
              <Text style={{ color: C.ink, fontWeight: '800' }}>{w.boss.name}</Text>
              <Text style={{ color: C.inkSoft, fontSize: 13 }}>{w.boss.defeated ? T('Vaincu · revanche possible') : w.boss.available ? T('Prêt : touche pour combattre') : T('Termine les leçons de l’île pour l’affronter')}</Text>
            </View>
          </Pressable>
        )}
        {w.exam && (
          <Pressable accessibilityRole="button" accessibilityLabel={T('Examen blanc : {0}', [w.title])} onPress={onExam} style={{ flexDirection: 'row', alignItems: 'center', gap: 10, marginTop: 6, padding: 12, borderRadius: 14, backgroundColor: '#FBEFD9', borderWidth: 2, borderColor: C.gold }}>
            <Text style={{ fontSize: 22, fontWeight: '900', color: C.ko }}>{D('mockExam')}</Text>
            <View style={{ flex: 1 }}>
              <Text style={{ color: C.ink, fontWeight: '800' }}>{T('Passer l’examen blanc')}</Text>
              <Text style={{ color: C.inkSoft, fontSize: 13 }}>{w.exam.attempts ? T('Meilleur score : {0} %', [w.exam.bestPercent]) + (w.exam.passed ? T(', seuil atteint') : '') : T('Chronométré, non officiel')}</Text>
            </View>
          </Pressable>
        )}
      </View>
    </View>
  );
}
