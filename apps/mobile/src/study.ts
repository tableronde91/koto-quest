import { DUEL_TIER_NAMES, decor, languageInfo, setHanLanguage, type DecorKey, type StudyLanguage } from '@koto/shared';
import { useAuth } from './auth';
import { T } from './i18n';

/** Mots qui changent selon la langue étudiée (japonais, coréen, anglais, chinois), comme sur le web. */
export function studyWords(lang: StudyLanguage) {
  const ko = lang === 'ko';
  const en = lang === 'en';
  const zh = lang === 'zh';
  /** Valeur selon la langue étudiée : japonais, coréen, anglais, chinois. */
  const pick = <V,>(ja: V, kor: V, eng: V, chi: V): V => (ko ? kor : en ? eng : zh ? chi : ja);
  return {
    lang,
    ko,
    en,
    zh,
    pick,
    info: languageInfo(lang),
    /** Nom de l'examen : JLPT, TOPIK ou TOEIC */
    exam: languageInfo(lang).exam,
    /** « le japonais », « le coréen », « l'anglais » */
    theLanguage: pick(T('le japonais'), T('le coréen'), T('l’anglais'), T('le chinois')),
    /** adjectif : « japonais », « coréen », « anglais » */
    adjective: pick(T('japonais'), T('coréen'), T('anglais'), T('chinois')),
    /** Onglet des caractères (libellé et glyphe) ; en anglais, seulement les expressions */
    charsTitle: pick(T('Kana et kanji'), T('Hangeul et expressions'), T('Expressions'), T('Hanzi et expressions')),
    charsGlyph: pick('あ', '한', '“', '字'),
    /** Atelier d'entraînement */
    workshop: pick(T('Atelier JLPT'), T('Atelier TOPIK'), T('Atelier TOEIC'), T('Atelier HSK')),
  };
}

/** Langue étudiée de l'utilisateur connecté. */
export function useStudyLang() {
  const { me } = useAuth();
  const lang = me?.preferences.studyLanguage ?? 'ja';
  setHanLanguage(lang);
  return studyWords(lang);
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
