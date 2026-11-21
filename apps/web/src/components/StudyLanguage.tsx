import { useState } from 'react';
import { useQueryClient } from '@tanstack/react-query';
import { STUDY_LANGUAGES, examLevelLabel, languageInfo, type MeDto, type StudyLanguage } from '@koto/shared';
import { put } from '../api/client';
import { useMe } from '../api/hooks';
import { T } from '../i18n';

/** Mots qui changent selon la langue étudiée (japonais / coréen). */
export function studyWords(lang: StudyLanguage) {
  const ko = lang === 'ko';
  return {
    lang,
    ko,
    info: languageInfo(lang),
    /** Nom de l'examen : JLPT ou TOPIK */
    exam: ko ? 'TOPIK' : 'JLPT',
    /** « le japonais », « le coréen » */
    theLanguage: ko ? T('le coréen') : T('le japonais'),
    /** adjectif : « japonais », « coréen » */
    adjective: ko ? T('coréen') : T('japonais'),
    /** Nom de l'écriture à apprendre en premier */
    script: ko ? T('le hangeul') : T('les kana'),
    /** Onglet Caractères (libellé court et glyphe) */
    charsShort: ko ? T('Hangeul') : T('Kana'),
    charsGlyph: ko ? '한' : 'あ',
    /** Atelier d'entraînement */
    workshop: ko ? T('Atelier TOPIK') : T('Atelier JLPT'),
    /** Attribut lang des textes dans la langue étudiée */
    htmlLang: ko ? 'ko' : 'ja',
    levelLabel: examLevelLabel,
  };
}

export function useStudyLang() {
  const { data: me } = useMe();
  return studyWords(me?.preferences.studyLanguage ?? 'ja');
}

/** Clé du niveau affiché dans Parcours (voir Path.tsx) : oubliée quand on change de langue. */
const PATH_LEVEL_KEY = 'koto-path-level';

/** Change la langue étudiée : le parcours, les révisions, la lecture et les caractères suivent. */
export async function switchStudyLanguage(lang: StudyLanguage, qc: ReturnType<typeof useQueryClient>) {
  const me = await put<MeDto>('/me/preferences', { studyLanguage: lang });
  try {
    localStorage.removeItem(PATH_LEVEL_KEY);
  } catch {
    // stockage indisponible : sans conséquence
  }
  qc.setQueryData(['me'], me);
  await qc.invalidateQueries();
  return me;
}

/** Sélecteur de langue étudiée : 日本語 / 한국어. */
export function StudyLanguageSwitch({ className = '', compact = false }: { className?: string; compact?: boolean }) {
  const { data: me } = useMe();
  const qc = useQueryClient();
  const [busy, setBusy] = useState(false);
  if (!me) return null;
  const current = me.preferences.studyLanguage ?? 'ja';
  const choose = async (lang: StudyLanguage) => {
    if (lang === current || busy) return;
    setBusy(true);
    try {
      await switchStudyLanguage(lang, qc);
    } finally {
      setBusy(false);
    }
  };
  return (
    <div role="radiogroup" aria-label={T('Langue étudiée')} className={`grid grid-cols-2 rounded-2xl bg-surface-2 p-1 ${className}`} data-testid="study-language">
      {STUDY_LANGUAGES.map((l) => (
        <button
          key={l.code}
          role="radio"
          aria-checked={l.code === current}
          disabled={busy}
          onClick={() => choose(l.code)}
          className={`flex min-h-11 items-center justify-center gap-2 rounded-xl px-2 font-bold ${l.code === current ? 'bg-surface shadow-sm' : 'text-ink-soft hover:text-ink'}`}
        >
          <span lang={l.code} className="jp">{l.native}</span>
          {!compact && <span className="text-sm font-normal">{T(l.name)}</span>}
        </button>
      ))}
    </div>
  );
}
