import { setHanLanguage, type StudyLanguage } from '@koto/shared';

/**
 * Applique la langue étudiée : lecture des caractères seuls (chinois ou japonais) et attribut du document,
 * qui donne aux caractères chinois les formes du chinois simplifié (voir index.css, html[data-study="zh"]).
 */
export function applyStudyLanguage(lang: StudyLanguage | null | undefined) {
  setHanLanguage(lang);
  if (typeof document !== 'undefined' && document.documentElement.dataset.study !== (lang ?? 'ja')) document.documentElement.dataset.study = lang ?? 'ja';
}
