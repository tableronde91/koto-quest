import { languageInfo, setHanLanguage, type StudyLanguage } from '@koto/shared';
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
