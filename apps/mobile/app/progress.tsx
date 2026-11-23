import { useDecor } from '../src/study';
import { ReactNode } from 'react';
import { Pressable, Text, View } from 'react-native';
import { useRouter } from 'expo-router';
import { useQuery } from '@tanstack/react-query';
import type { AchievementsDto, Mastery, StatsDto } from '@koto/shared';
import { api } from '../src/api';
import { Avatar } from '../src/Avatar';
import { useDashboard } from '../src/hooks';
import { MASTERY_COLOR } from '../src/mastery';
import { C } from '../src/theme';
import { Button, ErrorBox, H1, Loading, P, ProgressBar, Screen } from '../src/ui';
import { T, getLocale } from '../src/i18n';
import { useStudyLang } from '../src/study';

// Libellés traduits à l'affichage avec T()
const RANKS: [number, string][] = [
  [16, 'Maître du Koto'],
  [12, 'Sensei en herbe'],
  [8, 'Gardien·ne des kanji'],
  [5, 'Lame des kana'],
  [3, 'Voyageur·se des îles'],
  [1, 'Apprenti·e du dojo'],
];
const RANKS_KO: [number, string][] = [
  [16, 'Maître du Koto'],
  [12, 'Sensei en herbe'],
  [8, 'Gardien·ne des contes'],
  [5, 'Pinceau du hangeul'],
  [3, 'Voyageur·se des îles'],
  [1, 'Apprenti·e du dojo'],
];
const RANKS_ZH: [number, string][] = [
  [16, 'Maître du Koto'],
  [12, 'Stratège des Royaumes'],
  [8, 'Gardien·ne des caractères'],
  [5, 'Pinceau de Qin'],
  [3, 'Voyageur·se des îles'],
  [1, 'Apprenti·e lettré·e'],
];
const rankFor = (level: number, ko = false, zh = false) => (zh ? RANKS_ZH : ko ? RANKS_KO : RANKS).find(([min]) => level >= min)![1];

/** Niveau d'une compétence : un palier tous les 10 éléments maîtrisés (comme sur le web). */
const SKILL_STEP = 10;
const SKILLS = [
  { kind: 'kana', glyph: 'あ', label: 'Kana', color: '#E36A3A' },
  { kind: 'vocabulary', glyph: '語', label: 'Vocabulaire', color: '#3F8F5B' },
  { kind: 'kanji', glyph: '字', label: 'Kanji', color: '#8E1B26' },
  { kind: 'grammar', glyph: '文', label: 'Grammaire', color: '#4F5DB8' },
] as const;
/** En coréen : le hangeul remplace les kana, pas de kanji. */
const SKILLS_KO = [
  { kind: 'kana', glyph: '한', label: 'Hangeul', color: '#E36A3A' },
  { kind: 'vocabulary', glyph: '말', label: 'Vocabulaire', color: '#3F8F5B' },
  { kind: 'grammar', glyph: '문', label: 'Grammaire', color: '#4F5DB8' },
] as const;
/** En chinois : les hanzi, pas de kana. */
const SKILLS_ZH = [
  { kind: 'kanji', glyph: '字', label: 'Hanzi', color: '#8E1B26' },
  { kind: 'vocabulary', glyph: '词', label: 'Vocabulaire', color: '#3F8F5B' },
  { kind: 'grammar', glyph: '语', label: 'Grammaire', color: '#4F5DB8' },
] as const;
/** En anglais : vocabulaire et grammaire. */
const SKILLS_EN = [
  { kind: 'vocabulary', glyph: 'W', label: 'Vocabulaire', color: '#3F8F5B' },
  { kind: 'grammar', glyph: 'G', label: 'Grammaire', color: '#4F5DB8' },
] as const;

const GARDEN: { m: Mastery; icon: string; label: string; hint: string }[] = [
  { m: 'mastered', icon: '🌸', label: 'En fleur', hint: 'maîtrisées' },
  { m: 'learning', icon: '🌿', label: 'En pousse', hint: 'en apprentissage' },
  { m: 'discovered', icon: '🌱', label: 'Graines', hint: 'découvertes' },
  { m: 'fragile', icon: '🍂', label: 'Feuilles fragiles', hint: 'à consolider' },
  { m: 'urgent', icon: '🥀', label: 'À arroser vite', hint: 'à réviser maintenant' },
];

const dateLocale = () => (getLocale() === 'en' ? 'en-GB' : 'fr-FR');

function duration(seconds: number) {
  const m = Math.round(seconds / 60);
  if (m < 60) return T('{0} min', [m]);
  return `${Math.floor(m / 60)} h ${String(m % 60).padStart(2, '0')}`;
}

/** Mon aventure : fiche du héros, compétences, jardin de la mémoire, carnet de route, examens. */
export default function Progress() {
  const D = useDecor();
  const { ko, en, zh } = useStudyLang();
  const router = useRouter();
  const stats = useQuery({ queryKey: ['stats'], queryFn: () => api<StatsDto>('/stats') });
  const ach = useQuery({ queryKey: ['achievements'], queryFn: () => api<AchievementsDto>('/achievements') });
  const { data: d } = useDashboard();
  const s = stats.data;
  if (stats.isLoading || !d) return <Loading />;
  if (stats.error || !s) return <Screen><ErrorBox error={stats.error} onRetry={stats.refetch} /></Screen>;

  const order: Mastery[] = ['mastered', 'learning', 'discovered', 'fragile', 'urgent'];
  const totalCards = order.reduce((n, m) => n + s.masteryDistribution[m], 0);
  const needsCare = s.masteryDistribution.fragile + s.masteryDistribution.urgent;
  const last14 = s.days.slice(-14);
  const activeDays = last14.filter((x) => x.answers > 0).length;

  return (
    <Screen>
      <View style={{ flexDirection: 'row', alignItems: 'center', gap: 8 }}>
        <Pressable accessibilityRole="button" accessibilityLabel={T('Retour')} onPress={() => (router.canGoBack() ? router.back() : router.replace('/'))} hitSlop={12}>
          <Text style={{ fontSize: 26, color: C.ink, fontWeight: '800' }}>‹</Text>
        </Pressable>
        <H1>{T('Mon aventure')}</H1>
      </View>

      {/* Fiche du héros */}
      <View testID="hero" style={{ backgroundColor: '#2A2858', borderRadius: 24, padding: 18, gap: 14, overflow: 'hidden' }}>
        <Text style={{ position: 'absolute', right: -10, top: -30, fontSize: 120, fontWeight: '900', color: '#fff', opacity: 0.08 }}>{D('adventure')}</Text>
        <View style={{ flexDirection: 'row', alignItems: 'center', gap: 14 }}>
          <View style={{ borderRadius: 18, overflow: 'hidden', borderWidth: 3, borderColor: '#ffffffcc' }}>
            <Avatar config={d.avatar} size={80} />
          </View>
          <View style={{ flex: 1, gap: 2 }}>
            <Text style={{ color: '#FFD58A', fontWeight: '800', fontSize: 12, textTransform: 'uppercase', letterSpacing: 0.5 }}>{T(rankFor(d.xp.level, ko, zh))}</Text>
            <Text style={{ color: '#fff', fontSize: 24, fontWeight: '800' }}>{d.displayName}</Text>
            <Text style={{ color: '#fff', opacity: 0.8, fontSize: 13 }}>{T('Niveau {0} · {1} XP au total', [d.xp.level, d.xp.total])}</Text>
          </View>
        </View>
        <View style={{ flexDirection: 'row' }}><ProgressBar value={d.xp.intoLevel} max={Math.max(1, d.xp.forNext)} color={C.gold} label={T('XP du niveau')} /></View>
        <Text style={{ color: '#fff', opacity: 0.8, fontSize: 13 }}>{T('{0} XP avant le niveau {1}', [d.xp.forNext - d.xp.intoLevel, d.xp.level + 1])}</Text>
        <View style={{ flexDirection: 'row', flexWrap: 'wrap', marginHorizontal: -4 }}>
          {[
            { icon: d.streak.todayDone ? '🔥' : '🪵', v: T('{0} j', [d.streak.current]), k: T('Série en cours') },
            { icon: '🪙', v: String(d.coins), k: T('Pièces') },
            { icon: '📜', v: String(s.totals.lessonsCompleted), k: T('Leçons terminées') },
            { icon: '⏳', v: duration(s.totals.studySeconds), k: T('Temps d’étude') },
          ].map((c) => (
            <View key={c.k} style={{ width: '50%', padding: 4 }}>
              <View style={{ flexDirection: 'row', alignItems: 'center', gap: 8, backgroundColor: '#ffffff1a', borderRadius: 14, padding: 10 }}>
                <Text style={{ fontSize: 20 }}>{c.icon}</Text>
                <View>
                  <Text style={{ color: '#fff', fontWeight: '800', fontSize: 17 }}>{c.v}</Text>
                  <Text style={{ color: '#fff', opacity: 0.8, fontSize: 11 }}>{c.k}</Text>
                </View>
              </View>
            </View>
          ))}
        </View>
      </View>

      {/* Compétences */}
      <Section glyph={D('skills')} title={T('Compétences')}>
        {(en ? SKILLS_EN : zh ? SKILLS_ZH : ko ? SKILLS_KO : SKILLS).map((k) => {
          const v = s.byKind[k.kind];
          const lv = 1 + Math.floor(v.mastered / SKILL_STEP);
          const into = v.mastered % SKILL_STEP;
          return (
            <View key={k.kind} testID="skill" style={{ flexDirection: 'row', alignItems: 'center', gap: 12, borderWidth: 1, borderColor: C.line, borderRadius: 16, backgroundColor: C.surface, padding: 12 }}>
              <View style={{ width: 48, height: 48, borderRadius: 14, backgroundColor: k.color, alignItems: 'center', justifyContent: 'center' }}>
                <Text style={{ color: '#fff', fontSize: 26, fontWeight: '900' }}>{k.glyph}</Text>
              </View>
              <View style={{ flex: 1, gap: 6 }}>
                <View style={{ flexDirection: 'row', justifyContent: 'space-between' }}>
                  <Text style={{ fontWeight: '800', color: C.ink }}>{T(k.label)}</Text>
                  <Text style={{ fontWeight: '800', color: C.ink, backgroundColor: C.surface2, borderRadius: 99, paddingHorizontal: 8, overflow: 'hidden' }}>{T('Niv. {0}', [lv])}</Text>
                </View>
                <View style={{ flexDirection: 'row' }}><ProgressBar value={into} max={SKILL_STEP} color={k.color} label={T('{0} : progression vers le niveau {1}', [T(k.label), lv + 1])} /></View>
                <Text style={{ fontSize: 12, color: C.inkSoft }}>{T('{0} maîtrisé(s) · {1} rencontré(s) · encore {2} pour monter', [v.mastered, v.learned, SKILL_STEP - into])}</Text>
              </View>
            </View>
          );
        })}
      </Section>

      {/* Jardin de la mémoire */}
      <Section glyph={D('garden')} title={T('Jardin de la mémoire')}>
        {totalCards === 0 ? (
          <P soft>{T('Termine une première leçon : chaque notion apprise sera plantée ici et fleurira à force de révisions.')}</P>
        ) : (
          <View style={{ gap: 12, backgroundColor: C.okBg, borderRadius: 20, padding: 12 }}>
            <View style={{ flexDirection: 'row', flexWrap: 'wrap', marginHorizontal: -4 }}>
              {GARDEN.map((g) => (
                <View key={g.m} style={{ width: '33.33%', padding: 4 }}>
                  <View style={{ alignItems: 'center', backgroundColor: C.surface, borderRadius: 14, paddingVertical: 8 }}>
                    <Text style={{ fontSize: 26 }}>{g.icon}</Text>
                    <Text style={{ fontSize: 20, fontWeight: '800', color: C.ink }}>{s.masteryDistribution[g.m]}</Text>
                    <Text style={{ fontSize: 11, fontWeight: '700', color: C.ink, textAlign: 'center' }}>{T(g.label)}</Text>
                  </View>
                </View>
              ))}
            </View>
            <View style={{ flexDirection: 'row', height: 10, borderRadius: 99, overflow: 'hidden' }}>
              {order.map((m) => (s.masteryDistribution[m] > 0 ? <View key={m} style={{ flex: s.masteryDistribution[m], backgroundColor: MASTERY_COLOR[m] }} /> : null))}
            </View>
            {needsCare > 0 ? (
              <View style={{ gap: 8 }}>
                <P>{T('{0} notion(s) à arroser.', [needsCare])}</P>
                <Button tone="gold" label={T('Arroser le jardin')} onPress={() => router.push('/review')} />
              </View>
            ) : (
              <P soft>{T('Tout ton jardin est en bonne santé. 🌞')}</P>
            )}
          </View>
        )}
      </Section>

      {/* Carnet de route : 14 derniers jours */}
      <Section glyph={D('log')} title={T('Carnet de route')}>
        <P soft style={{ fontSize: 14 }}>
          {T('{0} jour(s) d’entraînement sur les 14 derniers', [activeDays])}
          {s.accuracy !== null ? T(' · {0} % de bonnes réponses en moyenne', [s.accuracy]) : ''}
        </P>
        <View style={{ flexDirection: 'row', flexWrap: 'wrap', marginHorizontal: -3 }}>
          {last14.map((day, i) => {
            const on = day.answers > 0;
            const today = i === last14.length - 1;
            return (
              <View key={day.date} style={{ width: `${100 / 7}%`, padding: 3 }}>
                <View accessibilityLabel={on ? T('{0} réponses, {1} XP', [day.answers, day.xp]) : T('pas d’entraînement')} style={{ alignItems: 'center', gap: 2, borderWidth: 2, borderColor: today ? C.ink : C.line, borderRadius: 12, paddingVertical: 6, backgroundColor: on ? C.surface : C.surface2 }}>
                  <Text style={{ fontSize: 9, color: C.inkSoft }}>{new Date(`${day.date}T12:00:00`).toLocaleDateString(dateLocale(), { weekday: 'short' }).replace('.', '')}</Text>
                  {on ? (
                    <Text style={{ fontSize: 13, fontWeight: '900', color: C.ko, borderWidth: 2, borderColor: C.ko, borderRadius: 5, paddingHorizontal: 2, transform: [{ rotate: '-6deg' }] }}>{D('completed')}</Text>
                  ) : (
                    <View style={{ width: 22, height: 22, borderRadius: 5, borderWidth: 2, borderStyle: 'dashed', borderColor: C.line }} />
                  )}
                  <Text style={{ fontSize: 9, fontWeight: '800', color: C.ink }}>{on ? `+${day.xp}` : '·'}</Text>
                </View>
              </View>
            );
          })}
        </View>
      </Section>

      {/* Succès */}
      <Pressable accessibilityRole="button" accessibilityLabel={T('Mes succès')} onPress={() => router.push('/achievements')} style={{ flexDirection: 'row', alignItems: 'center', gap: 12, borderWidth: 1, borderColor: C.line, borderRadius: 20, backgroundColor: C.surface, padding: 12 }}>
        <View style={{ width: 52, height: 52, borderRadius: 26, backgroundColor: C.gold, alignItems: 'center', justifyContent: 'center' }}>
          <Text style={{ fontSize: 28, fontWeight: '900', color: '#2a1a00' }}>{D('award')}</Text>
        </View>
        <View style={{ flex: 1 }}>
          <Text style={{ fontWeight: '800', fontSize: 17, color: C.ink }}>{T('Mes succès')}</Text>
          <Text style={{ color: C.inkSoft, fontSize: 13 }}>{ach.data ? T('{0} sur {1} débloqués', [ach.data.unlocked, ach.data.total]) : T('Badges à débloquer')}</Text>
        </View>
        <Text style={{ fontSize: 22, color: C.inkSoft }}>›</Text>
      </Pressable>

      {/* Examens blancs */}
      <Section glyph={D('exam')} title={T('Examens blancs')}>
        {s.exams.length === 0 ? (
          <P soft>{zh ? T('Aucun examen blanc passé. Tu le trouveras à la fin du parcours HSK 1.') : en ? T('Aucun examen blanc passé. Tu le trouveras à la fin du parcours A1.') : ko ? T('Aucun examen blanc passé. Tu le trouveras à la fin du parcours TOPIK 1.') : T('Aucun examen blanc passé. Tu le trouveras à la fin du parcours N5.')}</P>
        ) : (
          [...s.exams].reverse().map((e) => (
            <View key={e.date} testID="exam-result" style={{ gap: 4, borderWidth: 1, borderColor: C.line, borderRadius: 14, backgroundColor: C.surface, padding: 10 }}>
              <Text style={{ color: C.ink }}>
                <Text style={{ fontWeight: '900' }}>{e.percent} %</Text>{' '}
                <Text style={{ color: e.passed ? C.ok : C.inkSoft }}>{e.passed ? T('(seuil atteint)') : T('(seuil non atteint)')}</Text>{' '}
                <Text style={{ fontSize: 12, color: C.inkSoft }}>{new Date(e.date).toLocaleDateString(dateLocale(), { day: 'numeric', month: 'short', year: 'numeric' })}</Text>
              </Text>
              <Text style={{ fontSize: 12, color: C.inkSoft }}>{e.title}</Text>
              <Text style={{ fontSize: 12, color: C.inkSoft }}>{e.sections.map((x) => `${x.title} ${x.percent} %`).join(' · ')}</Text>
            </View>
          ))
        )}
      </Section>
    </Screen>
  );
}

function Section({ glyph, title, children }: { glyph: string; title: string; children: ReactNode }) {
  return (
    <View style={{ gap: 10 }}>
      <View style={{ flexDirection: 'row', alignItems: 'center', gap: 10 }}>
        <View style={{ width: 34, height: 34, borderRadius: 10, backgroundColor: C.ink, alignItems: 'center', justifyContent: 'center' }}>
          <Text style={{ color: C.paper, fontWeight: '900', fontSize: 18 }}>{glyph}</Text>
        </View>
        <Text accessibilityRole="header" style={{ fontSize: 20, fontWeight: '800', color: C.ink }}>{title}</Text>
      </View>
      {children}
    </View>
  );
}
