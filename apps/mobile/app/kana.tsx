import { spokenForm } from '@koto/shared';
import { useMemo, useState } from 'react';
import { Modal, Pressable, Text, TextInput, View } from 'react-native';
import { useRouter } from 'expo-router';
import type { CharacterDto, CharacterGroupDto, ExpressionDto, ExpressionRegister, ExpressionsDto } from '@koto/shared';
import { useCharacters, useExpressions } from '../src/hooks';
import { MASTERY_COLOR, MASTERY_LABEL } from '../src/mastery';
import { speak } from '../src/speech';
import { C } from '../src/theme';
import { Button, Card, ErrorBox, TitleBar, H1, H2, Loading, P, ProgressBar, Screen } from '../src/ui';
import { T } from '../src/i18n';
import { useStudyLang } from '../src/study';

type Pane = string;
// Libellés traduits à l'affichage avec T()
const PANES: Record<'ja' | 'ko' | 'en' | 'zh' | 'es', { slug: Pane; glyph: string; label: string }[]> = {
  ja: [
    { slug: 'hiragana', glyph: 'あ', label: 'Hiragana' },
    { slug: 'katakana', glyph: 'ア', label: 'Katakana' },
    { slug: 'kanji', glyph: '字', label: 'Kanji' },
    { slug: 'expressions', glyph: '話', label: 'Expressions' },
  ],
  ko: [
    { slug: 'hangul-vowels', glyph: 'ㅏ', label: 'Voyelles' },
    { slug: 'hangul-consonants', glyph: 'ㄱ', label: 'Consonnes' },
    { slug: 'hangul-syllables', glyph: '가', label: 'Syllabes' },
    { slug: 'expressions', glyph: '말', label: 'Expressions' },
  ],
  // Pas d'écriture à apprendre en anglais : seulement les expressions et idiomes
  en: [{ slug: 'expressions', glyph: '“', label: 'Expressions' }],
  // Chinois : les caractères (une section, un groupe par niveau du HSK) et les expressions
  zh: [
    { slug: 'hanzi', glyph: '字', label: 'Hanzi' },
    { slug: 'expressions', glyph: '话', label: 'Expressions' },
  ],
  // Espagnol : alphabet latin, seulement les expressions
  es: [{ slug: 'expressions', glyph: '¡!', label: 'Expressions' }],
};

// Traduits à l'affichage avec T()
const REGISTER: Record<ExpressionRegister, { label: string; color: string; bg: string }> = {
  polite: { label: 'Poli', color: '#1F5FA8', bg: '#E3EEFA' },
  neutral: { label: 'Neutre', color: '#4F5B66', bg: '#ECEFF2' },
  casual: { label: 'Familier', color: '#A3520F', bg: '#FCEBDD' },
  formal: { label: 'Formel', color: '#6A3FA0', bg: '#EEE6F8' },
};

/** Onglet commun à tous : l'écriture de la langue étudiée (kana et kanji, ou hangeul) et les expressions. */
export default function KanaTab() {
  const w = useStudyLang();
  const panes = PANES[w.lang];
  const [picked, setPane] = useState<Pane>(panes[0].slug);
  // Après un changement de langue, l'onglet choisi peut ne plus exister
  const pane = panes.some((p) => p.slug === picked) ? picked : panes[0].slug;
  return (
    <Screen>
      <TitleBar title={w.pick(T('Caractères'), T('Hangeul'), T('Expressions'), T('Hanzi'), T('Expressions'))} fallback="/learn" />
      <P soft>{w.pick(T('Les écritures japonaises et les expressions du quotidien, accessibles à tout moment.'), T('L’alphabet coréen, les expressions du quotidien et les proverbes, accessibles à tout moment.'), T('Les expressions idiomatiques et les verbes à particule les plus utiles, accessibles à tout moment.'), T('Les caractères chinois avec leur pinyin et les expressions du quotidien, accessibles à tout moment.'), T('Les expressions et les tournures les plus utiles de l’espagnol, accessibles à tout moment.'))}</P>
      <View accessibilityRole="tablist" accessibilityLabel={T('Écriture')} style={{ flexDirection: 'row', backgroundColor: C.surface2, borderRadius: 16, padding: 4 }}>
        {panes.map((p) => {
          const on = p.slug === pane;
          return (
            <Pressable key={p.slug} accessibilityRole="tab" accessibilityState={{ selected: on }} accessibilityLabel={T(p.label)} onPress={() => setPane(p.slug)} style={{ flex: 1, alignItems: 'center', paddingVertical: 8, borderRadius: 12, backgroundColor: on ? C.surface : 'transparent' }}>
              <Text style={{ fontSize: 18, fontWeight: '900', color: on ? C.ink : C.inkSoft }}>{p.glyph}</Text>
              <Text numberOfLines={1} style={{ fontSize: 11, fontWeight: '800', color: on ? C.ink : C.inkSoft }}>{T(p.label)}</Text>
            </Pressable>
          );
        })}
      </View>
      {pane === 'expressions' ? <ExpressionsPane /> : <CharactersPane slug={pane} />}
    </Screen>
  );
}

// ─────────────── Caractères ───────────────

function CharactersPane({ slug }: { slug: string }) {
  const router = useRouter();
  const { data, isLoading, error, refetch } = useCharacters();
  const [detail, setDetail] = useState<CharacterDto | null>(null);
  if (isLoading) return <Loading />;
  if (error || !data) return <ErrorBox error={error} onRetry={refetch} />;
  const section = data.sections.find((s) => s.slug === slug) ?? data.sections[0];
  const practice = (scope: string) => router.push({ pathname: '/practice', params: { kind: 'characters', scope } });

  return (
    <View style={{ gap: 18 }} testID="characters">
      <View style={{ backgroundColor: C.ink, borderRadius: 24, padding: 18, gap: 10 }}>
        <Text style={{ color: C.paper, opacity: 0.85 }}>{section.description}</Text>
        <View style={{ flexDirection: 'row' }}><ProgressBar value={section.learned} max={section.total} color={C.gold} label={T('{0} vus', [section.title])} /></View>
        <Text style={{ color: C.paper, opacity: 0.85, fontSize: 13 }}>{T('{0} sur {1} vus, {2} maîtrisés', [section.learned, section.total, section.mastered])}</Text>
        <Button
          tone="gold"
          label={section.due > 0 ? T('Réviser {0} caractère{1}', [section.due, section.due > 1 ? 's' : '']) : section.learned === 0 ? T('Apprendre les {0}', [section.title.toLowerCase()]) : T('Continuer')}
          onPress={() => practice(section.slug)}
        />
      </View>
      {section.groups.map((g) => (
        <Group key={g.slug} g={g} kanji={section.slug === 'kanji'} onPractice={() => practice(g.slug)} onOpen={setDetail} />
      ))}
      {section.slug === 'kanji' && data.notice && <P soft style={{ fontSize: 12 }}>{data.notice}</P>}
      <CharacterSheet c={detail} onClose={() => setDetail(null)} />
    </View>
  );
}

/** Disposition « gojūon » : les trous de la grille (ya _ yu _ yo, wa _ _ _ wo) restent visibles. */
function layout(g: CharacterGroupDto): (CharacterDto | null)[] {
  if (g.slug.endsWith('-y') && g.items.length === 3) return [g.items[0], null, g.items[1], null, g.items[2]];
  if (g.slug.endsWith('-w') && g.items.length === 3) return [g.items[0], null, null, null, g.items[1], g.items[2]];
  return g.items;
}

function Group({ g, kanji, onPractice, onOpen }: { g: CharacterGroupDto; kanji: boolean; onPractice: () => void; onOpen: (c: CharacterDto) => void }) {
  const cols = kanji ? 4 : g.slug.endsWith('-combo') ? 3 : 5;
  const learned = g.items.filter((i) => i.mastery).length;
  return (
    <View style={{ gap: 10 }} testID="char-group">
      <View style={{ flexDirection: 'row', alignItems: 'center', gap: 10 }}>
        <Text style={{ flex: 1, fontSize: 17, fontWeight: '800', color: C.ink }}>
          {g.title} <Text style={{ fontSize: 13, fontWeight: '400', color: C.inkSoft }}>{learned}/{g.items.length}</Text>
        </Text>
        <Pressable accessibilityRole="button" accessibilityLabel={T('Pratiquer : {0}', [g.title])} onPress={onPractice} style={{ borderWidth: 2, borderColor: C.line, borderRadius: 99, paddingHorizontal: 14, paddingVertical: 6 }}>
          <Text style={{ fontWeight: '800', color: C.ink }}>{T('Pratiquer')}</Text>
        </Pressable>
      </View>
      <View style={{ flexDirection: 'row', flexWrap: 'wrap', marginHorizontal: -4 }}>
        {layout(g).map((c, i) => (
          <View key={c?.id ?? `gap-${i}`} style={{ width: `${100 / cols}%`, padding: 4 }}>
            {c && <Cell c={c} kanji={kanji} onOpen={onOpen} />}
          </View>
        ))}
      </View>
    </View>
  );
}

function Cell({ c, kanji, onOpen }: { c: CharacterDto; kanji: boolean; onOpen: (c: CharacterDto) => void }) {
  const label = kanji ? c.meaning : c.romaji ?? c.meaning;
  return (
    <Pressable
      accessibilityRole="button"
      accessibilityLabel={`${c.front}, ${label}, ${c.mastery ? T(MASTERY_LABEL[c.mastery]) : T('Pas encore vu')}`}
      onPress={() => {
        speak(spokenForm(c.front, c.reading));
        onOpen(c);
      }}
      style={{ alignItems: 'center', gap: 3, borderWidth: 2, borderColor: C.line, borderRadius: 16, backgroundColor: C.surface, paddingTop: 10, paddingBottom: 8, paddingHorizontal: 2 }}
    >
      <Text style={{ fontSize: [...c.front].length > 1 ? 24 : 30, fontWeight: '700', color: c.mastery ? C.ink : C.inkSoft }}>{c.front}</Text>
      <Text numberOfLines={1} style={{ fontSize: 11, color: C.inkSoft }}>{label}</Text>
      <View style={{ width: '80%', height: 5, borderRadius: 99, backgroundColor: C.surface2, overflow: 'hidden' }}>
        <View style={{ width: `${c.mastery ? Math.max(8, c.score) : 0}%`, height: '100%', borderRadius: 99, backgroundColor: c.mastery ? MASTERY_COLOR[c.mastery] : 'transparent' }} />
      </View>
    </Pressable>
  );
}

function CharacterSheet({ c, onClose }: { c: CharacterDto | null; onClose: () => void }) {
  const { zh } = useStudyLang();
  return (
    <Modal visible={!!c} transparent animationType="fade" onRequestClose={onClose}>
      <Pressable onPress={onClose} style={{ flex: 1, backgroundColor: 'rgba(10,14,40,0.55)', justifyContent: 'flex-end', padding: 12 }}>
        {c && (
          <Pressable accessibilityRole="none" onPress={() => undefined} style={{ backgroundColor: C.paper, borderRadius: 24, padding: 22, gap: 10 }} testID="char-sheet">
            <View style={{ flexDirection: 'row', alignItems: 'flex-start' }}>
              <Text style={{ flex: 1, fontSize: 84, fontWeight: '900', color: C.ink, lineHeight: 96 }}>{c.front}</Text>
              <Pressable accessibilityRole="button" accessibilityLabel={T('Fermer')} onPress={onClose} hitSlop={12}>
                <Text style={{ fontSize: 22, color: C.inkSoft }}>✕</Text>
              </Pressable>
            </View>
            <Text style={{ fontSize: 22, fontWeight: '800', color: C.ink }}>{c.kind === 'kanji' ? c.meaning : c.romaji}</Text>
            {c.kind === 'kanji' && (
              <View style={{ gap: 4 }}>
                <Row k={zh ? T('Pinyin') : T('Lecture courante')} v={c.reading ?? '—'} />
                {(c.kanji?.onyomi.length ?? 0) + (c.kanji?.kunyomi.length ?? 0) > 0 && <Row k={T('On’yomi')} v={c.kanji?.onyomi.join('、') || '—'} />}
                {(c.kanji?.onyomi.length ?? 0) + (c.kanji?.kunyomi.length ?? 0) > 0 && <Row k={T('Kun’yomi')} v={c.kanji?.kunyomi.join('、') || '—'} />}
                {c.kanji?.strokes ? <Row k={T('Traits')} v={String(c.kanji.strokes)} /> : null}
              </View>
            )}
            <View style={{ flexDirection: 'row', alignItems: 'center', gap: 8 }}>
              <View style={{ width: 10, height: 10, borderRadius: 5, backgroundColor: c.mastery ? MASTERY_COLOR[c.mastery] : C.line }} />
              <Text style={{ color: C.ink }}>{c.mastery ? T(MASTERY_LABEL[c.mastery]) : T('Pas encore vu')}</Text>
            </View>
            <View style={{ flexDirection: 'row', gap: 10 }}>
              <Button label={`🔊 ${T('Écouter')}`} onPress={() => speak(spokenForm(c.front, c.reading))} style={{ flex: 1 }} />
              <Button label={`🐢 ${T('Lentement')}`} tone="quiet" onPress={() => speak(spokenForm(c.front, c.reading), true)} style={{ flex: 1 }} />
            </View>
          </Pressable>
        )}
      </Pressable>
    </Modal>
  );
}

function Row({ k, v }: { k: string; v: string }) {
  return (
    <View style={{ flexDirection: 'row', gap: 12 }}>
      <Text style={{ width: 130, color: C.inkSoft }}>{k}</Text>
      <Text style={{ flex: 1, color: C.ink, fontSize: 16 }}>{v}</Text>
    </View>
  );
}

// ─────────────── Expressions ───────────────

function ExpressionsPane() {
  const router = useRouter();
  const { ko, zh, es } = useStudyLang();
  const { data, isLoading, error, refetch } = useExpressions();
  const [themeSlug, setThemeSlug] = useState<string | null>(null);
  const [query, setQuery] = useState('');
  const q = query.trim().toLowerCase();
  const results = useMemo(() => search(data, q), [data, q]);
  if (isLoading) return <Loading />;
  if (error || !data) return <ErrorBox error={error} onRetry={refetch} />;
  const theme = data.themes.find((t) => t.slug === themeSlug) ?? data.themes[0];

  return (
    <View style={{ gap: 16 }} testID="expressions">
      <TextInput
        value={query}
        onChangeText={setQuery}
        placeholder={es ? T('Rechercher : merci, gracias, perdón…') : zh ? T('Rechercher : merci, 谢谢, xièxie…') : ko ? T('Rechercher : merci, 감사, gamsa…') : T('Rechercher : merci, おねがい, sumimasen…')}
        placeholderTextColor={C.inkSoft}
        accessibilityLabel={T('Rechercher une expression')}
        autoCorrect={false}
        style={{ borderWidth: 2, borderColor: C.line, borderRadius: 14, paddingHorizontal: 12, fontSize: 16, color: C.ink, minHeight: 48, backgroundColor: C.surface }}
      />
      {q.length >= 2 ? (
        <>
          <P soft>{results.length ? T('{0} expression(s) trouvée(s)', [results.length]) : T('Aucune expression ne correspond.')}</P>
          {results.map((e) => <ExpressionCard key={e.id} e={e} />)}
        </>
      ) : (
        <>
          <View accessibilityLabel={T('Thèmes')} style={{ flexDirection: 'row', flexWrap: 'wrap', gap: 8 }}>
            {data.themes.map((t) => {
              const on = t.slug === theme.slug;
              return (
                <Pressable key={t.slug} accessibilityRole="button" accessibilityState={{ selected: on }} accessibilityLabel={t.title} onPress={() => setThemeSlug(t.slug)} style={{ flexDirection: 'row', alignItems: 'center', gap: 6, borderWidth: 2, borderColor: on ? C.ink : C.line, backgroundColor: on ? C.ink : C.surface, borderRadius: 99, paddingLeft: 6, paddingRight: 12, paddingVertical: 5 }}>
                  <Text style={{ fontSize: 16, fontWeight: '900', color: on ? C.gold : C.ink }}>{t.glyph}</Text>
                  <Text style={{ fontWeight: '800', fontSize: 13, color: on ? C.paper : C.ink }}>{t.title}</Text>
                </Pressable>
              );
            })}
          </View>
          <View style={{ backgroundColor: C.ink, borderRadius: 24, padding: 18, gap: 10 }}>
            <View style={{ flexDirection: 'row', alignItems: 'center', gap: 12 }}>
              <View style={{ width: 52, height: 52, borderRadius: 16, backgroundColor: C.gold, alignItems: 'center', justifyContent: 'center' }}>
                <Text style={{ fontSize: 28, fontWeight: '900', color: '#2a1a00' }}>{theme.glyph}</Text>
              </View>
              <Text accessibilityRole="header" style={{ flex: 1, color: C.paper, fontSize: 22, fontWeight: '800' }}>{theme.title}</Text>
            </View>
            <Text style={{ color: C.paper, opacity: 0.85 }}>{theme.description}</Text>
            <View style={{ flexDirection: 'row' }}><ProgressBar value={theme.learned} max={theme.total} color={C.gold} label={T('Expressions vues : {0}', [theme.title])} /></View>
            <Text style={{ color: C.paper, opacity: 0.85, fontSize: 13 }}>{T('{0} sur {1} vues, {2} maîtrisées', [theme.learned, theme.total, theme.mastered])}</Text>
            <Button
              tone="gold"
              label={theme.due > 0 ? T('Revoir {0} expression(s)', [theme.due]) : theme.learned === 0 ? T('Apprendre ces expressions') : theme.learned < theme.total ? T('Continuer') : T('S’entraîner')}
              onPress={() => router.push({ pathname: '/practice', params: { kind: 'expressions', scope: theme.slug } })}
            />
          </View>
          {theme.expressions.map((e) => <ExpressionCard key={e.id} e={e} />)}
          {data.notice && <P soft style={{ fontSize: 12 }}>{data.notice}</P>}
        </>
      )}
    </View>
  );
}

function search(data: ExpressionsDto | undefined, q: string): ExpressionDto[] {
  if (!data || q.length < 2) return [];
  return data.themes.flatMap((t) => t.expressions.filter((e) => [e.front, e.reading ?? '', e.romaji ?? '', e.meaning].some((s) => s.toLowerCase().includes(q))));
}

function ExpressionCard({ e }: { e: ExpressionDto }) {
  const reg = REGISTER[e.register];
  return (
    <Card style={{ gap: 8 }} testID="expression">
      <View style={{ flexDirection: 'row', alignItems: 'flex-start', gap: 10 }}>
        <View style={{ flex: 1, gap: 2 }}>
          <Text style={{ fontSize: 22, fontWeight: '800', color: C.ink }}>{e.front}</Text>
          {(e.reading && e.reading !== e.front) || e.romaji ? (
            <Text style={{ color: C.inkSoft }}>{[e.reading !== e.front ? e.reading : null, e.romaji].filter(Boolean).join(' · ')}</Text>
          ) : null}
        </View>
        <Pressable accessibilityRole="button" accessibilityLabel={T('Écouter {0}', [e.front])} onPress={() => speak(spokenForm(e.front, e.reading))} hitSlop={10} style={{ width: 44, height: 44, borderRadius: 22, backgroundColor: C.surface2, alignItems: 'center', justifyContent: 'center' }}>
          <Text style={{ fontSize: 20 }}>🔊</Text>
        </Pressable>
      </View>
      <Text style={{ fontSize: 17, fontWeight: '700', color: C.ink }}>{e.meaning}</Text>
      <P soft style={{ fontSize: 14 }}>{e.note}</P>
      {e.example && (
        <View style={{ backgroundColor: C.surface2, borderRadius: 12, padding: 10, gap: 2 }}>
          <Text style={{ color: C.ink, fontSize: 15 }}>{e.example.jp}</Text>
          <Text style={{ color: C.inkSoft, fontSize: 13 }}>{e.example.fr}</Text>
        </View>
      )}
      <View style={{ flexDirection: 'row', alignItems: 'center', gap: 8 }}>
        <Text style={{ fontSize: 12, fontWeight: '800', color: reg.color, backgroundColor: reg.bg, borderRadius: 99, paddingHorizontal: 8, paddingVertical: 2, overflow: 'hidden' }}>{T(reg.label)}</Text>
        <View style={{ width: 8, height: 8, borderRadius: 4, backgroundColor: e.mastery ? MASTERY_COLOR[e.mastery] : C.line }} />
        <Text style={{ fontSize: 12, color: C.inkSoft }}>{e.mastery ? T(MASTERY_LABEL[e.mastery]) : T('Pas encore vue')}</Text>
      </View>
    </Card>
  );
}
