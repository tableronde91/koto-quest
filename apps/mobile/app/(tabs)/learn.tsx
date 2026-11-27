import { Pressable, Text, View } from 'react-native';
import { useRouter } from 'expo-router';
import { useAuth } from '../../src/auth';
import { useDashboard, useReading } from '../../src/hooks';
import { C } from '../../src/theme';
import { H1, P, Screen } from '../../src/ui';
import { T, plural } from '../../src/i18n';
import { MOCK_EXAM } from '../../src/exams';
import { useDecor, useStudyLang } from '../../src/study';
import { examLevelLabel } from '@koto/shared';

interface Tile { href: string; glyph: string; color: string; title: string; text: string; badge?: string | null; testID?: string }

/** Apprendre : toutes les façons d'étudier, chacune expliquée en une phrase. */
export default function Learn() {
  const D = useDecor();
  const router = useRouter();
  const { me } = useAuth();
  const w = useStudyLang();
  const { data: d } = useDashboard();
  const { data: reading } = useReading();
  const due = d?.reviews.due ?? 0;
  const level = me?.preferences.targetLevel ?? 'N5';

  const daily: Tile[] = [
    { href: '/reviews', glyph: D('review'), color: C.gold, title: T('Révisions'), text: due ? T('Les notions que tu risques d’oublier, au bon moment.') : T('Rien à réviser pour l’instant : reviens plus tard.'), badge: due ? plural(due, '{0} à revoir', '{0} à revoir') : null, testID: 'learn-reviews' },
    { href: '/reading', glyph: D('read'), color: '#3F8F5B', title: T('Lecture'), text: w.de ? T('Des contes et légendes en allemand simple, un chapitre par jour.') : w.es ? T('Des contes et légendes en espagnol simple, un chapitre par jour.') : w.en ? T('Des contes et légendes en anglais simple, un chapitre par jour.') : w.zh ? T('Des contes chinois en chinois simple, un chapitre par jour.') : w.ko ? T('Des contes coréens en coréen simple, un chapitre par jour.') : T('Des contes japonais en japonais simple, un chapitre par jour.'), badge: reading?.today.state === 'new' ? T('Chapitre du jour') : null },
  ];
  const study: Tile[] = [
    { href: '/kana', glyph: w.charsGlyph, color: '#E36A3A', title: w.charsTitle, text: w.de ? T('Les expressions et les proverbes de l’allemand du quotidien.') : w.es ? T('Les expressions et les proverbes de l’espagnol du quotidien.') : w.en ? T('Les expressions idiomatiques et les verbes à particule du quotidien.') : w.zh ? T('Les caractères chinois et les expressions du quotidien.') : w.ko ? T('Le hangeul, les expressions du quotidien et les proverbes.') : T('Les grilles d’écriture et les expressions du quotidien.') },
    { href: '/prepa', glyph: D('exam'), color: C.seal, title: w.workshop, text: T('S’entraîner épreuve par épreuve, au format de l’examen.') },
    { href: `/exam/${MOCK_EXAM[level] ?? 'n5-jlpt'}?title=${encodeURIComponent(T('Examen blanc {0}', [examLevelLabel(level)]))}`, glyph: D('mockExam'), color: '#4F5DB8', title: T('Examen blanc {0}', [examLevelLabel(level)]), text: T('Toutes les épreuves, chronométrées, notées comme le vrai.') },
    { href: '/placement', glyph: D('placement'), color: '#7B5BD6', title: T('Test de niveau'), text: w.de ? T('Tu connais déjà un peu d’allemand ? Saute ce que tu sais.') : w.es ? T('Tu connais déjà un peu d’espagnol ? Saute ce que tu sais.') : w.en ? T('Tu connais déjà un peu d’anglais ? Saute ce que tu sais.') : w.zh ? T('Tu connais déjà un peu de chinois ? Saute ce que tu sais.') : w.ko ? T('Tu connais déjà un peu de coréen ? Saute ce que tu sais.') : T('Tu connais déjà un peu de japonais ? Saute ce que tu sais.') },
  ];

  return (
    <Screen>
      <H1>{T('Apprendre')}</H1>
      <P soft>{T('Choisis comment étudier aujourd’hui.')}</P>
      <Section title={T('Chaque jour')} tiles={daily} onOpen={(h) => router.push(h as never)} />
      <Section title={T('Pour progresser')} tiles={study} onOpen={(h) => router.push(h as never)} />
    </Screen>
  );
}

function Section({ title, tiles, onOpen }: { title: string; tiles: Tile[]; onOpen: (href: string) => void }) {
  return (
    <View style={{ gap: 10 }}>
      <Text accessibilityRole="header" style={{ fontSize: 13, fontWeight: '800', color: C.inkSoft, textTransform: 'uppercase', letterSpacing: 0.6 }}>{title}</Text>
      {tiles.map((t) => (
        <Pressable key={t.href} testID={t.testID} accessibilityRole="button" accessibilityLabel={t.title} onPress={() => onOpen(t.href)} style={{ flexDirection: 'row', alignItems: 'center', gap: 14, backgroundColor: C.surface, borderWidth: 1, borderColor: C.line, borderRadius: 20, padding: 14 }}>
          <View style={{ width: 52, height: 52, borderRadius: 16, backgroundColor: t.color, alignItems: 'center', justifyContent: 'center' }}>
            <Text style={{ color: '#fff', fontSize: 26, fontWeight: '900' }}>{t.glyph}</Text>
          </View>
          <View style={{ flex: 1, gap: 2 }}>
            <View style={{ flexDirection: 'row', alignItems: 'center', gap: 8, flexWrap: 'wrap' }}>
              <Text style={{ fontSize: 17, fontWeight: '800', color: C.ink }}>{t.title}</Text>
              {t.badge && <Text style={{ fontSize: 11, fontWeight: '800', color: '#2a1a00', backgroundColor: C.gold, borderRadius: 99, paddingHorizontal: 8, paddingVertical: 2, overflow: 'hidden' }}>{t.badge}</Text>}
            </View>
            <Text style={{ fontSize: 13, color: C.inkSoft }}>{t.text}</Text>
          </View>
          <Text style={{ fontSize: 24, color: C.inkSoft }}>›</Text>
        </Pressable>
      ))}
    </View>
  );
}
