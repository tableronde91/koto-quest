import { useState } from 'react';
import { useQueryClient } from '@tanstack/react-query';
import { DUEL_TIER_NAMES, STUDY_LANGUAGES, decor, examLevelLabel, languageInfo, type DecorKey, type MeDto, type StudyLanguage } from '@koto/shared';
import { applyStudyLanguage } from '../lib/studyLanguage';
import { put } from '../api/client';
import { useMe } from '../api/hooks';
import { T } from '../i18n';

/** Mots qui changent selon la langue étudiée (japonais, coréen, anglais, chinois). */
export function studyWords(lang: StudyLanguage) {
  const ko = lang === 'ko';
  const en = lang === 'en';
  const zh = lang === 'zh';
  const es = lang === 'es';
  /** Valeur selon la langue étudiée : japonais, coréen, anglais, chinois, espagnol. */
  const pick = <V,>(ja: V, kor: V, eng: V, chi: V, esp: V): V => (ko ? kor : en ? eng : zh ? chi : es ? esp : ja);
  return {
    lang,
    ko,
    en,
    zh,
    es,
    pick,
    info: languageInfo(lang),
    /** Nom de l'examen : JLPT, TOPIK, TOEIC ou HSK */
    exam: languageInfo(lang).exam,
    /** « le japonais », « le coréen », « l'anglais », « le chinois » */
    theLanguage: pick(T('le japonais'), T('le coréen'), T('l’anglais'), T('le chinois'), T('l’espagnol')),
    /** adjectif : « japonais », « coréen », « anglais », « chinois » */
    adjective: pick(T('japonais'), T('coréen'), T('anglais'), T('chinois'), T('espagnol')),
    /** Nom de l'écriture à apprendre en premier (l'anglais n'en a pas) */
    script: pick(T('les kana'), T('le hangeul'), '', T('les caractères'), ''),
    /** Onglet Caractères (libellé court et glyphe) ; l'anglais n'a pas d'onglet d'écriture */
    charsShort: pick(T('Kana'), T('Hangeul'), '', T('Hanzi'), ''),
    charsGlyph: pick('あ', '한', '', '字', ''),
    hasCharacters: !en && !es,
    /** Atelier d'entraînement */
    workshop: pick(T('Atelier JLPT'), T('Atelier TOPIK'), T('Atelier TOEIC'), T('Atelier HSK'), T('Atelier DELE')),
    /** Glyphe des examens */
    examGlyph: pick('試', '시', 'T', '考', 'E'),
    /** Attribut lang des textes dans la langue étudiée */
    htmlLang: lang as string,
    levelLabel: examLevelLabel,
  };
}

export function useStudyLang() {
  const { data: me } = useMe();
  const lang = me?.preferences.studyLanguage ?? 'ja';
  applyStudyLanguage(lang);
  return studyWords(lang);
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

/** Sélecteur de langue étudiée : 日本語 / 한국어 / English / 中文 / Español. */
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

/** Glyphes décoratifs (tampons, pictos) dans la langue étudiée : jamais de japonais en coréen, anglais ou chinois. */
export function useDecor() {
  const { lang } = useStudyLang();
  return (key: DecorKey) => decor(key, lang);
}

/** Libellé d'un rang de duel dans la langue étudiée (« Ashigaru II » en japonais, « Fantassin II » sinon). */
export function useRankLabel() {
  const { lang } = useStudyLang();
  return (rank: { tierId: string; label: string }) => {
    const n = DUEL_TIER_NAMES[rank.tierId];
    return lang === 'ja' || !n ? rank.label : rank.label.replace(n.ja, T(n.other));
  };
}
