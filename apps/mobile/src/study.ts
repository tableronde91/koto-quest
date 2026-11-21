import { languageInfo, type StudyLanguage } from '@koto/shared';
import { useAuth } from './auth';
import { T } from './i18n';

/** Mots qui changent selon la langue étudiée (japonais / coréen), comme sur le web. */
export function studyWords(lang: StudyLanguage) {
  const ko = lang === 'ko';
  return {
    lang,
    ko,
    info: languageInfo(lang),
    /** Nom de l'examen : JLPT ou TOPIK */
    exam: ko ? 'TOPIK' : 'JLPT',
    /** adjectif : « japonais », « coréen » */
    adjective: ko ? T('coréen') : T('japonais'),
    /** Onglet des caractères (libellé et glyphe) */
    charsTitle: ko ? T('Hangeul et expressions') : T('Kana et kanji'),
    charsGlyph: ko ? '한' : 'あ',
    /** Atelier d'entraînement */
    workshop: ko ? T('Atelier TOPIK') : T('Atelier JLPT'),
  };
}

/** Langue étudiée de l'utilisateur connecté. */
export function useStudyLang() {
  const { me } = useAuth();
  return studyWords(me?.preferences.studyLanguage ?? 'ja');
}
