import { useState } from 'react';
import { Pressable, Text, View } from 'react-native';
import { useQueryClient } from '@tanstack/react-query';
import { STUDY_LANGUAGES, languageInfo, levelLabel, type JlptCode, type OnboardingInput, type SelfLevel, type StudyLanguage } from '@koto/shared';
import { put } from '../src/api';
import { useAuth } from '../src/auth';
import { studyWords } from '../src/study';
import { C } from '../src/theme';
import { Button, H1, H2, P, Screen } from '../src/ui';
import { T, getLocale } from '../src/i18n';

const LEVELS = (lang: StudyLanguage): { value: SelfLevel; label: string; hint: string }[] =>
  lang === 'en' || lang === 'es'
    ? [
        { value: 'beginner', label: T('Je pars de zéro ou presque'), hint: T('On commence par les salutations et les phrases de tous les jours.') },
        { value: 'basics', label: T('Je me débrouille un peu'), hint: T('Les premières îles restent ouvertes.') },
      ]
    : lang === 'zh'
    ? [
        { value: 'beginner', label: T('Je pars de zéro'), hint: T('On commence par le pinyin, les quatre tons et les premiers caractères.') },
        { value: 'basics', label: T('Je connais le pinyin et quelques caractères'), hint: T('Les îles du pinyin restent ouvertes.') },
      ]
    : lang === 'ko'
    ? [
        { value: 'beginner', label: T('Je pars de zéro'), hint: T('On commence par le hangeul, l’alphabet coréen.') },
        { value: 'kana', label: T('Je lis le hangeul'), hint: T('On passe aux premières phrases.') },
        { value: 'basics', label: T('Je connais des bases'), hint: T('Les îles du hangeul restent ouvertes.') },
      ]
    : [
        { value: 'beginner', label: T('Je pars de zéro'), hint: T('On commence par les hiragana.') },
        { value: 'kana', label: T('Je lis les kana'), hint: T('On passe aux premières phrases.') },
        { value: 'basics', label: T('Je connais des bases'), hint: T('Les premières îles restent ouvertes.') },
        { value: 'n5', label: T('J’ai le niveau N5'), hint: T('Vise le N4 juste en dessous.') },
      ];
const MINUTES = [10, 15, 20, 30];
const TARGETS: Record<StudyLanguage, { code: JlptCode; hint: string }[]> = {
  ja: [
    { code: 'N5', hint: 'Débutant' },
    { code: 'N4', hint: 'Élémentaire' },
    { code: 'N3', hint: 'Intermédiaire' },
    { code: 'N2', hint: 'Avancé' },
    { code: 'N1', hint: 'Expert' },
  ],
  ko: [
    { code: 'TOPIK1', hint: 'Débutant' },
    { code: 'TOPIK2', hint: 'Élémentaire' },
    { code: 'TOPIK3', hint: 'Intermédiaire' },
    { code: 'TOPIK4', hint: 'Intermédiaire avancé' },
    { code: 'TOPIK5', hint: 'Avancé' },
    { code: 'TOPIK6', hint: 'Maîtrise' },
  ],
  // Anglais : les cinq niveaux du CECRL, de A1 à C1
  en: [
    { code: 'A1', hint: 'Découverte · TOEIC 120+' },
    { code: 'A2', hint: 'Survie · TOEIC 225+' },
    { code: 'B1', hint: 'Seuil · TOEIC 550+' },
    { code: 'B2', hint: 'Avancé · TOEIC 785+' },
    { code: 'C1', hint: 'Autonome · TOEIC 945+' },
  ],
  // Chinois : seuls les niveaux dont le parcours est prêt
  zh: [
    { code: 'HSK1', hint: 'Débutant · 150 mots' },
    { code: 'HSK2', hint: 'Élémentaire · 300 mots' },
    { code: 'HSK3', hint: 'Intermédiaire · 600 mots' },
    { code: 'HSK4', hint: 'Intermédiaire avancé · 1 200 mots' },
    { code: 'HSK5', hint: 'Avancé · 2 500 mots' },
    { code: 'HSK6', hint: 'Maîtrise · 5 000 mots' },
  ],
  // Espagnol : seuls les niveaux dont le parcours est prêt
  es: [
    { code: 'DELEA1', hint: 'Découverte' },
    { code: 'DELEA2', hint: 'Survie' },
  ],
};

function Choice({ selected, label, hint, glyph, onPress, testID }: { selected: boolean; label: string; hint?: string; glyph?: string; onPress: () => void; testID?: string }) {
  return (
    <Pressable testID={testID} accessibilityRole="radio" accessibilityState={{ selected }} onPress={onPress} style={{ flexDirection: 'row', alignItems: 'center', gap: 12, borderWidth: 2, borderColor: selected ? C.ink : C.line, backgroundColor: C.surface, borderRadius: 16, padding: 14 }}>
      {glyph && (
        <View style={{ width: 44, height: 44, borderRadius: 12, backgroundColor: C.ink, alignItems: 'center', justifyContent: 'center' }}>
          <Text style={{ color: C.paper, fontSize: 24, fontWeight: '900' }}>{glyph}</Text>
        </View>
      )}
      <View style={{ flex: 1 }}>
        <Text style={{ fontWeight: '800', fontSize: 16, color: C.ink }}>{label}</Text>
        {hint && <Text style={{ color: C.inkSoft }}>{hint}</Text>}
      </View>
    </Pressable>
  );
}

/** Profil en un écran : langue étudiée, niveau actuel, niveau visé, temps par jour. */
export default function Onboarding() {
  const qc = useQueryClient();
  const { me } = useAuth();
  const [lang, setLang] = useState<StudyLanguage>(me?.preferences.studyLanguage ?? 'ja');
  const [selfLevel, setSelf] = useState<SelfLevel>('beginner');
  const [target, setTarget] = useState<JlptCode>(languageInfo(lang).firstLevel);
  const [minutes, setMinutes] = useState(15);
  const [busy, setBusy] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const words = studyWords(lang);

  function chooseLanguage(l: StudyLanguage) {
    setLang(l);
    setTarget(languageInfo(l).firstLevel);
    if (!LEVELS(l).some((x) => x.value === selfLevel)) setSelf('beginner');
  }

  async function save() {
    setBusy(true);
    setError(null);
    try {
      const body: OnboardingInput = { selfLevel, targetLevel: target, studyLanguage: lang, minutesPerDay: minutes, difficultAreas: [], reminderMode: 'normal', timezone: Intl.DateTimeFormat().resolvedOptions().timeZone, locale: getLocale() };
      await put('/me/onboarding', body);
      await qc.invalidateQueries();
    } catch (e) {
      setError(e instanceof Error ? e.message : T('Erreur'));
    } finally {
      setBusy(false);
    }
  }

  return (
    <Screen>
      <H1>{T('Bienvenue dans l’archipel !')}</H1>
      <P soft>{T('Quatre questions pour adapter ton programme.')}</P>
      <H2>{T('Quelle langue veux-tu apprendre ?')}</H2>
      <View style={{ gap: 8 }}>
        {STUDY_LANGUAGES.map((l) => (
          <Choice key={l.code} testID={`lang-${l.code}`} glyph={l.glyph} selected={lang === l.code} label={`${T(l.name)} · ${l.native}`} hint={l.code === 'ko' ? T('Préparation au TOPIK, en commençant par le hangeul') : l.code === 'en' ? T('Préparation au TOEIC, du niveau A1 au C1') : l.code === 'zh' ? T('Préparation au HSK, du niveau 1 au 6, avec le pinyin') : l.code === 'es' ? T('Préparation au DELE, en commençant par le niveau A1') : T('Préparation au JLPT, du N5 au N1')} onPress={() => chooseLanguage(l.code)} />
        ))}
      </View>
      <H2>{T('Où en es-tu en {0} ?', [words.adjective])}</H2>
      <View style={{ gap: 8 }}>{LEVELS(lang).map((l) => <Choice key={l.value} selected={selfLevel === l.value} label={l.label} hint={l.hint} onPress={() => { setSelf(l.value); if (l.value === 'n5') setTarget('N4'); }} />)}</View>
      <H2>{T('Quel niveau {0} vises-tu ?', [words.exam])}</H2>
      <View style={{ flexDirection: 'row', flexWrap: 'wrap', gap: 8 }}>
        {TARGETS[lang].map((c) => <View key={c.code} style={{ width: '31%', flexGrow: 1 }}><Choice selected={target === c.code} label={levelLabel(c.code)} hint={T(c.hint)} onPress={() => setTarget(c.code)} /></View>)}
      </View>
      <H2>{T('Combien de temps par jour ?')}</H2>
      <View style={{ flexDirection: 'row', gap: 8 }}>
        {MINUTES.map((m) => <View key={m} style={{ flex: 1 }}><Choice selected={minutes === m} label={T('{0} min', [m])} onPress={() => setMinutes(m)} /></View>)}
      </View>
      {error && <Text style={{ color: C.ko, fontWeight: '700' }}>{error}</Text>}
      <Button tone="gold" label={busy ? '…' : T('Commencer l’aventure')} disabled={busy} onPress={save} />
    </Screen>
  );
}
