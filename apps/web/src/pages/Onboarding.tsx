import { useState } from 'react';
import { useNavigate } from 'react-router';
import { useQueryClient } from '@tanstack/react-query';
import type { DifficultArea, JlptCode, MeDto, OnboardingInput, SelfLevel } from '@koto/shared';
import { put } from '../api/client';
import { qk } from '../api/hooks';
import { ProgressBar } from '../components/ui';
import { T, locale } from '../i18n';
import { LanguageSwitch } from '../components/LanguageSwitch';

const LEVELS: { value: SelfLevel; label: string; hint: string }[] = [
  { value: 'beginner', label: T("Je pars de zéro"), hint: T("On commence par les hiragana.") },
  { value: 'kana', label: T("Je lis les hiragana et katakana"), hint: T("On passe directement aux premières phrases.") },
  { value: 'basics', label: T("Je connais quelques kanji et bases de grammaire"), hint: T("Les premiers mondes restent accessibles en révision.") },
  { value: 'n5', label: T("J’ai le niveau N5"), hint: T("Vise le N4 à l’étape suivante : ses premiers mondes sont ouverts.") },
];
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
    targetLevel: 'N5',
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

  const steps = [
    {
      title: T("Où en es-tu en japonais ?"),
      body: (
        <Choices
          value={data.selfLevel}
          onChange={(v) => set({ selfLevel: v as SelfLevel })}
          options={LEVELS.map((l) => ({ value: l.value, label: l.label, hint: l.hint }))}
        />
      ),
    },
    {
      title: T("Quel niveau JLPT vises-tu ?"),
      body: (
        <>
          <Choices
            value={data.targetLevel}
            onChange={(v) => set({ targetLevel: v as JlptCode })}
            options={[
              { value: 'N5', label: T("N5 — débutant"), hint: T("Disponible") },
              { value: 'N4', label: T("N4 — élémentaire"), hint: T("Premiers mondes disponibles, la suite arrive") },
            ]}
          />
          <p className="mt-3 text-sm text-ink-soft">{T("Les niveaux N3 à N1 seront ajoutés progressivement.")}</p>
        </>
      ),
    },
    {
      title: T("Quand veux-tu passer l’examen ?"),
      body: (
        <div className="flex flex-col gap-3">
          <label className="flex flex-col gap-1 font-bold">{T("Date de l’examen (facultatif)")}<input type="date" className="field max-w-xs font-normal" value={data.examDate ?? ''} onChange={(e) => set({ examDate: e.target.value || null })} />
          </label>
          <p className="text-sm text-ink-soft">{T("Le JLPT a lieu en juillet et en décembre dans la plupart des pays. Sans date, tu avances à ton rythme.")}</p>
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
          {AREAS.map((a) => {
            const on = data.difficultAreas.includes(a.value);
            return (
              <button
                key={a.value}
                type="button"
                aria-pressed={on}
                onClick={() => set({ difficultAreas: on ? data.difficultAreas.filter((x) => x !== a.value) : [...data.difficultAreas, a.value] })}
                className={`btn ${on ? 'btn-primary' : 'btn-quiet'}`}
              >
                {a.label}
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
    </div>
  );
}

function Choices({ value, onChange, options }: { value: string; onChange: (v: string) => void; options: { value: string; label: string; hint?: string }[] }) {
  return (
    <div role="radiogroup" className="flex flex-col gap-3">
      {options.map((o) => (
        <button
          key={o.value}
          type="button"
          role="radio"
          aria-checked={value === o.value}
          onClick={() => onChange(o.value)}
          className="flex min-h-14 flex-col items-start rounded-2xl border-2 bg-surface px-4 py-3 text-left"
          style={{ borderColor: value === o.value ? 'var(--ink)' : 'var(--line)' }}
        >
          <span className="font-bold">{o.label}</span>
          {o.hint && <span className="text-sm text-ink-soft">{o.hint}</span>}
        </button>
      ))}
    </div>
  );
}
