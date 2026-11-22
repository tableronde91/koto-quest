import { languageInfo, type StudyLanguage } from '@koto/shared';
import { useAuth } from './auth';
import { T } from './i18n';

/** Mots qui changent selon la langue étudiée (japonais / coréen), comme sur le web. */
export function studyWords(lang: StudyLanguage) {
  const ko = lang === 'ko';
  const en = lang === 'en';
  /** Valeur selon la langue étudiée : japonais, coréen, anglais. */
  const pick = <V,>(ja: V, kor: V, eng: V): V => (ko ? kor : en ? eng : ja);
  return {
    lang,
    ko,
    en,
    pick,
    info: languageInfo(lang),
    /** Nom de l'examen : JLPT, TOPIK ou TOEIC */
    exam: languageInfo(lang).exam,
    /** « le japonais », « le coréen », « l'anglais » */
    theLanguage: pick(T('le japonais'), T('le coréen'), T('l’anglais')),
    /** adjectif : « japonais », « coréen », « anglais » */
    adjective: pick(T('japonais'), T('coréen'), T('anglais')),
    /** Onglet des caractères (libellé et glyphe) ; en anglais, seulement les expressions */
    charsTitle: pick(T('Kana et kanji'), T('Hangeul et expressions'), T('Expressions')),
    charsGlyph: pick('あ', '한', '“'),
    /** Atelier d'entraînement */
    workshop: pick(T('Atelier JLPT'), T('Atelier TOPIK'), T('Atelier TOEIC')),
  };
}

/** Langue étudiée de l'utilisateur connecté. */
export function useStudyLang() {
  const { me } = useAuth();
  return studyWords(me?.preferences.studyLanguage ?? 'ja');
}
