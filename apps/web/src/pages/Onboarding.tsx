import { useState } from 'react';
import { useNavigate } from 'react-router';
import { useQueryClient } from '@tanstack/react-query';
import { STUDY_LANGUAGES, languageInfo, levelLabel, type DifficultArea, type JlptCode, type MeDto, type OnboardingInput, type SelfLevel, type StudyLanguage } from '@koto/shared';
import { studyWords } from '../components/StudyLanguage';
import { put } from '../api/client';
import { qk } from '../api/hooks';
import { ProgressBar } from '../components/ui';
import { T, locale } from '../i18n';
import { LanguageSwitch } from '../components/LanguageSwitch';
import { SiteFooter } from './Legal';

const LEVELS: Record<StudyLanguage, { value: SelfLevel; label: string; hint: string }[]> = {
  ja: [
    { value: 'beginner', label: T("Je pars de zéro"), hint: T("On commence par les hiragana.") },
    { value: 'kana', label: T("Je lis les hiragana et katakana"), hint: T("On passe directement aux premières phrases.") },
    { value: 'basics', label: T("Je connais quelques kanji et bases de grammaire"), hint: T("Les premiers mondes restent accessibles en révision.") },
    { value: 'n5', label: T("J’ai le niveau N5"), hint: T("Vise le N4 à l’étape suivante : ses premiers mondes sont ouverts.") },
  ],
  ko: [
    { value: 'beginner', label: T("Je pars de zéro"), hint: T("On commence par le hangeul, l’alphabet coréen.") },
    { value: 'kana', label: T("Je lis le hangeul"), hint: T("On passe directement aux premières phrases.") },
    { value: 'basics', label: T("Je connais quelques bases de grammaire"), hint: T("Les îles du hangeul restent accessibles en révision.") },
  ],
  en: [
    { value: 'beginner', label: T("Je pars de zéro ou presque"), hint: T("On commence par les salutations et les phrases de tous les jours.") },
    { value: 'basics', label: T("Je me débrouille dans les situations simples"), hint: T("Vise directement un niveau plus haut : tu pourras toujours revoir le A1.") },
  ],
};
/** Niveaux visés : seuls les niveaux dont le parcours existe sont proposés comme disponibles. */
const TARGETS: Record<StudyLanguage, { value: JlptCode; label: string; ready: boolean }[]> = {
  ja: [
    { value: 'N5', label: T("N5 — débutant"), ready: true },
    { value: 'N4', label: T("N4 — élémentaire"), ready: true },
    { value: 'N3', label: T("N3 — intermédiaire"), ready: true },
    { value: 'N2', label: T("N2 — intermédiaire avancé"), ready: true },
    { value: 'N1', label: T("N1 — avancé"), ready: true },
  ],
  ko: [
    { value: 'TOPIK1', label: T("TOPIK 1 — débutant (TOPIK I)"), ready: true },
    { value: 'TOPIK2', label: T("TOPIK 2 — élémentaire (TOPIK I)"), ready: true },
    { value: 'TOPIK3', label: T("TOPIK 3 — intermédiaire (TOPIK II)"), ready: true },
    { value: 'TOPIK4', label: T("TOPIK 4 — intermédiaire avancé (TOPIK II)"), ready: true },
    { value: 'TOPIK5', label: T("TOPIK 5 — avancé (TOPIK II)"), ready: true },
    { value: 'TOPIK6', label: T("TOPIK 6 — maîtrise (TOPIK II)"), ready: true },
  ],
  en: [
    { value: 'A1', label: T("A1 — découverte (TOEIC 120+)"), ready: true },
    { value: 'A2', label: T("A2 — survie (TOEIC 225+)"), ready: true },
    { value: 'B1', label: T("B1 — seuil (TOEIC 550+)"), ready: true },
    { value: 'B2', label: T("B2 — avancé (TOEIC 785+)"), ready: true },
    { value: 'C1', label: T("C1 — autonome (TOEIC 945+)"), ready: true },
  ],
};
const AREAS: { value: DifficultArea; label: string }[] = [
  { value: 'kana', label: T("Les kana") },
  { value: 'vocabulary', label: T("Le vocabulaire") },
  { value: 'kanji', label: T("Les kanji") },
  { value: 'grammar', label: T("La grammaire") },
  { value: 'listening', label: T("La compréhension orale") },
  { value: 'reading', label: T("La lecture") },
];
const MINUTES = [10, 20, 30, 45, 60];
const REMINDERS: { value: OnboardingInput['reminderMode']; label: string; hint: string }[] = [
  { value: 'calm', label: T("Tranquille"), hint: T("1 à 2 défis par jour") },
  { value: 'normal', label: T("Normal"), hint: T("3 à 5 défis par jour") },
  { value: 'intense', label: T("Intensif"), hint: T("6 à 10 défis par jour") },
  { value: 'off', label: T("Pas de rappel"), hint: T("Tu pourras changer d’avis") },
];

export function OnboardingPage({ me }: { me: MeDto }) {
  const [step, setStep] = useState(0);
  const [data, setData] = useState<OnboardingInput>({
    selfLevel: 'beginner',
    targetLevel: languageInfo(me.preferences.studyLanguage ?? 'ja').firstLevel,
    studyLanguage: me.preferences.studyLanguage ?? 'ja',
    examDate: null,
    minutesPerDay: 20,
    difficultAreas: [],
    reminderMode: 'normal',
    timezone: Intl.DateTimeFormat().resolvedOptions().timeZone,
  });
  const [error, setError] = useState<string | null>(null);
  const qc = useQueryClient();
  const navigate = useNavigate();
  const set = (patch: Partial<OnboardingInput>) => setData({ ...data, ...patch });

  async function finish() {
    try {
      const updated = await put<MeDto>('/me/onboarding', { ...data, locale });
      qc.setQueryData(qk.me, updated);
      qc.invalidateQueries();
      navigate('/');
    } catch (e) {
      setError(e instanceof Error ? e.message : T("Erreur"));
    }
  }

  const lang: StudyLanguage = data.studyLanguage ?? 'ja';
  const words = studyWords(lang);
  const chooseLanguage = (l: StudyLanguage) =>
    setData({ ...data, studyLanguage: l, targetLevel: languageInfo(l).firstLevel, selfLevel: LEVELS[l].some((x) => x.value === data.selfLevel) ? data.selfLevel : 'beginner' });

  const steps = [
    {
      title: T("Quelle langue veux-tu apprendre ?"),
      body: (
        <>
          <div role="radiogroup" aria-label={T("Langue étudiée")} className="grid gap-3 sm:grid-cols-2">
            {STUDY_LANGUAGES.map((l) => (
              <button
                key={l.code}
                type="button"
                role="radio"
                aria-checked={lang === l.code}
                onClick={() => chooseLanguage(l.code)}
                className="flex items-center gap-4 rounded-2xl border-2 bg-surface p-4 text-left"
                style={{ borderColor: lang === l.code ? 'var(--ink)' : 'var(--line)' }}
              >
                <span lang={l.code} aria-hidden="true" className="jp flex h-14 w-14 shrink-0 items-center justify-center rounded-2xl bg-ink text-3xl font-black text-paper">{l.glyph}</span>
                <span>
                  <span className="block text-lg font-bold">{T(l.name)} <span lang={l.code} className="jp font-normal text-ink-soft">{l.native}</span></span>
                  <span className="text-sm text-ink-soft">{l.code === 'ko' ? T("Préparation au TOPIK, en commençant par le hangeul") : l.code === 'en' ? T("Préparation au TOEIC, du niveau A1 au C1") : T("Préparation au JLPT, du N5 au N1")}</span>
                </span>
              </button>
            ))}
          </div>
          <h2 className="mt-8 text-2xl">{T("Où en es-tu en {0} ?", [words.adjective])}</h2>
          <div className="mt-4">
            <Choices
              value={data.selfLevel}
              onChange={(v) => set({ selfLevel: v as SelfLevel })}
              options={LEVELS[lang].map((l) => ({ value: l.value, label: l.label, hint: l.hint }))}
            />
          </div>
        </>
      ),
    },
    {
      title: T("Quel niveau {0} vises-tu ?", [words.exam]),
      body: (
        <>
          <Choices
            value={data.targetLevel}
            onChange={(v) => set({ targetLevel: v as JlptCode })}
            options={TARGETS[lang].map((t) => ({ value: t.value, label: t.label, hint: t.ready ? T("Disponible") : T("En préparation"), disabled: !t.ready }))}
          />
          {lang === 'en' && <p className="mt-3 text-sm text-ink-soft">{T("Les niveaux suivent le cadre européen (CECRL) ; le score TOEIC indiqué est celui qui correspond à chaque niveau. Les cinq parcours, de A1 à C1, sont prêts.")}</p>}
          {lang === 'ko' && <p className="mt-3 text-sm text-ink-soft">{T("Le TOPIK I regroupe les niveaux 1 et 2 (parcours {0} et {1}), le TOPIK II les niveaux 3 à 6 (parcours {2}, {3}, {4} et {5}) : tous les parcours sont prêts.", [levelLabel('TOPIK1'), levelLabel('TOPIK2'), levelLabel('TOPIK3'), levelLabel('TOPIK4'), levelLabel('TOPIK5'), levelLabel('TOPIK6')])}</p>}
        </>
      ),
    },
    {
      title: T("Quand veux-tu passer l’examen ?"),
      body: (
        <div className="flex flex-col gap-3">
          <label className="flex flex-col gap-1 font-bold">{T("Date de l’examen (facultatif)")}<input type="date" className="field max-w-xs font-normal" value={data.examDate ?? ''} onChange={(e) => set({ examDate: e.target.value || null })} />
          </label>
          <p className="text-sm text-ink-soft">{lang === 'en' ? T("Le TOEIC se passe toute l’année, dans des centres agréés ou en ligne selon les pays. Sans date, tu avances à ton rythme.") : lang === 'ko' ? T("Le TOPIK est organisé plusieurs fois par an, à des dates qui varient selon les pays. Sans date, tu avances à ton rythme.") : T("Le JLPT a lieu en juillet et en décembre dans la plupart des pays. Sans date, tu avances à ton rythme.")}</p>
        </div>
      ),
    },
    {
      title: T("Combien de minutes par jour ?"),
      body: (
        <div className="flex flex-wrap gap-3">
          {MINUTES.map((m) => (
            <button key={m} type="button" aria-pressed={data.minutesPerDay === m} onClick={() => set({ minutesPerDay: m })} className={`btn ${data.minutesPerDay === m ? 'btn-primary' : 'btn-quiet'}`}>{T("{0} min", [ m ])}</button>
          ))}
        </div>
      ),
    },
    {
      title: T("Qu’est-ce qui te semble difficile ?"),
      body: (
        <div className="flex flex-wrap gap-3">
          {AREAS.filter((a) => (lang !== 'ko' || a.value !== 'kanji') && (lang !== 'en' || (a.value !== 'kanji' && a.value !== 'kana'))).map((a) => {
            const on = data.difficultAreas.includes(a.value);
            return (
              <button
                key={a.value}
                type="button"
                aria-pressed={on}
                onClick={() => set({ difficultAreas: on ? data.difficultAreas.filter((x) => x !== a.value) : [...data.difficultAreas, a.value] })}
                className={`btn ${on ? 'btn-primary' : 'btn-quiet'}`}
              >
                {lang === 'ko' && a.value === 'kana' ? T("Le hangeul") : a.label}
              </button>
            );
          })}
        </div>
      ),
    },
    {
      title: T("Combien de petits défis par jour ?"),
      body: (
        <>
          <Choices value={data.reminderMode} onChange={(v) => set({ reminderMode: v as OnboardingInput['reminderMode'] })} options={REMINDERS} />
          <p className="mt-3 text-sm text-ink-soft">{T("Rien ne sera envoyé sans ton accord : tu activeras les rappels dans les réglages, avec heures silencieuses et pause.")}</p>
        </>
      ),
    },
  ];

  const s = steps[step];
  return (
    <div className="mx-auto flex min-h-dvh max-w-2xl flex-col px-5 py-8">
      <ProgressBar value={step + 1} max={steps.length} label={T("Étape {0} sur {1}", [step + 1, steps.length])} tone="gold" />
      <div className="mt-6 flex flex-wrap items-center justify-between gap-3">
        <p className="text-ink-soft">{T("Bienvenue {0} ! Six questions pour adapter ton programme.", [ me.displayName ])}</p>
        <LanguageSwitch compact />
      </div>
      <h1 className="mt-2 text-3xl">{s.title}</h1>
      <div className="mt-6 flex-1">{s.body}</div>
      {error && <p role="alert" className="text-ko">{error}</p>}
      <div className="mt-8 flex justify-between gap-3">
        <button className="btn btn-quiet" disabled={step === 0} onClick={() => setStep(step - 1)}>{T("Retour")}</button>
        {step < steps.length - 1 ? (
          <button className="btn btn-primary" onClick={() => setStep(step + 1)}>{T("Suivant")}</button>
        ) : (
          <button className="btn btn-gold" onClick={finish}>{T("Commencer l’aventure")}</button>
        )}
      </div>
      <SiteFooter />
    </div>
  );
}

function Choices({ value, onChange, options }: { value: string; onChange: (v: string) => void; options: { value: string; label: string; hint?: string; disabled?: boolean }[] }) {
  return (
    <div role="radiogroup" className="flex flex-col gap-3">
      {options.map((o) => (
        <button
          key={o.value}
          type="button"
          role="radio"
          aria-checked={value === o.value}
          disabled={o.disabled}
          onClick={() => onChange(o.value)}
          className="flex min-h-14 flex-col items-start rounded-2xl border-2 bg-surface px-4 py-3 text-left disabled:opacity-50"
          style={{ borderColor: value === o.value ? 'var(--ink)' : 'var(--line)' }}
        >
          <span className="font-bold">{o.label}</span>
          {o.hint && <span className="text-sm text-ink-soft">{o.hint}</span>}
        </button>
      ))}
    </div>
  );
}
