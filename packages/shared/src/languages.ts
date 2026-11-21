/** Langues étudiées et niveaux (JLPT, TOPIK). Sans dépendance : importé par index et reading. */

// ───────────────────────── Langues étudiées ─────────────────────────

/** Langue étudiée : japonais (JLPT) ou coréen (TOPIK). */
export type StudyLanguage = 'ja' | 'ko';

export type JlptLevelCode = 'N5' | 'N4' | 'N3' | 'N2' | 'N1';
export type TopikCode = 'TOPIK1' | 'TOPIK2' | 'TOPIK3' | 'TOPIK4' | 'TOPIK5' | 'TOPIK6';
/** Code d'un niveau du parcours, toutes langues confondues (le nom est historique). */
export type JlptCode = JlptLevelCode | TopikCode;
export type LevelCode = JlptCode;

/** Niveaux du JLPT, du plus facile au plus difficile. */
export const JLPT_ONLY_LEVELS: JlptLevelCode[] = ['N5', 'N4', 'N3', 'N2', 'N1'];
/** Niveaux du TOPIK (TOPIK I : 1-2, TOPIK II : 3-6), du plus facile au plus difficile. */
export const TOPIK_LEVELS: TopikCode[] = ['TOPIK1', 'TOPIK2', 'TOPIK3', 'TOPIK4', 'TOPIK5', 'TOPIK6'];
/** Tous les niveaux acceptés par l'API (le nom est historique). */
export const JLPT_LEVELS: JlptCode[] = [...JLPT_ONLY_LEVELS, ...TOPIK_LEVELS];
export const ALL_LEVELS = JLPT_LEVELS;

export interface StudyLanguageInfo {
  code: StudyLanguage;
  /** Nom de la langue (français, traduit par le dictionnaire) */
  name: string;
  /** Nom dans la langue elle-même */
  native: string;
  /** Glyphe emblème */
  glyph: string;
  /** Examen préparé */
  exam: 'JLPT' | 'TOPIK';
  /** Code BCP 47 pour la synthèse vocale */
  speech: string;
  levels: JlptCode[];
  /** Premier niveau du parcours */
  firstLevel: JlptCode;
}

export const STUDY_LANGUAGES: StudyLanguageInfo[] = [
  { code: 'ja', name: 'Japonais', native: '日本語', glyph: '言', exam: 'JLPT', speech: 'ja-JP', levels: JLPT_ONLY_LEVELS, firstLevel: 'N5' },
  { code: 'ko', name: 'Coréen', native: '한국어', glyph: '한', exam: 'TOPIK', speech: 'ko-KR', levels: TOPIK_LEVELS, firstLevel: 'TOPIK1' },
];
export const STUDY_LANGUAGE_CODES: StudyLanguage[] = STUDY_LANGUAGES.map((l) => l.code);

export function languageInfo(lang: StudyLanguage): StudyLanguageInfo {
  return STUDY_LANGUAGES.find((l) => l.code === lang) ?? STUDY_LANGUAGES[0];
}

/** Langue d'un niveau : les codes TOPIK sont coréens, les autres japonais. */
export function languageOfLevel(code: string | null | undefined): StudyLanguage {
  return code && code.startsWith('TOPIK') ? 'ko' : 'ja';
}

/** Libellé court d'un niveau : « N5 », « TOPIK 1 ». */
export function levelLabel(code: string): string {
  return code.startsWith('TOPIK') ? `TOPIK ${code.slice(5)}` : code;
}

/** Libellé d'un niveau avec son examen : « JLPT N5 », « TOPIK 1 ». */
export function examLevelLabel(code: string): string {
  return code.startsWith('TOPIK') ? `TOPIK ${code.slice(5)}` : `JLPT ${code}`;
}

/** Vrai si le texte contient du hangeul (coréen). */
export function hasHangul(s: string): boolean {
  return /[ᄀ-ᇿ㄰-㆏가-힯]/.test(s);
}

// ───────── Changement de langue étudiée ─────────

export interface StudyChoice {
  studyLanguage: StudyLanguage;
  targetLevel: JlptCode;
  /** Dernier niveau visé dans chaque langue */
  levelByLanguage: Partial<Record<StudyLanguage, JlptCode>>;
}

/**
 * Applique un changement de langue ou de niveau visé (serveur et version hors ligne).
 * Le niveau visé appartient toujours à la langue étudiée ; en changeant de langue, on retrouve
 * le dernier niveau choisi dans cette langue (ou son premier niveau).
 */
export function applyStudyChoice(current: StudyChoice, patch: { studyLanguage?: StudyLanguage; targetLevel?: JlptCode }): StudyChoice {
  const map = { ...current.levelByLanguage, [languageOfLevel(current.targetLevel)]: current.targetLevel };
  let lang: StudyLanguage = patch.studyLanguage ?? (patch.targetLevel ? languageOfLevel(patch.targetLevel) : current.studyLanguage);
  if (!STUDY_LANGUAGE_CODES.includes(lang)) lang = 'ja';
  let level: JlptCode;
  if (patch.targetLevel && languageOfLevel(patch.targetLevel) === lang) level = patch.targetLevel;
  else if (languageOfLevel(current.targetLevel) === lang) level = current.targetLevel;
  else level = map[lang] ?? languageInfo(lang).firstLevel;
  map[lang] = level;
  return { studyLanguage: lang, targetLevel: level, levelByLanguage: map };
}

/** Niveaux d'une langue (du plus facile au plus difficile). */
export function levelsOfLanguage(lang: StudyLanguage): JlptCode[] {
  return languageInfo(lang).levels;
}
