/** Langues étudiées et niveaux (JLPT, TOPIK, TOEIC/CECRL, HSK, DELE, Goethe-Zertifikat). Sans dépendance : importé par index et reading. */

// ───────────────────────── Langues étudiées ─────────────────────────

/** Langue étudiée : japonais (JLPT), coréen (TOPIK), anglais (TOEIC, niveaux du CECRL), chinois (HSK), espagnol (DELE) ou allemand (Goethe-Zertifikat). */
export type StudyLanguage = 'ja' | 'ko' | 'en' | 'zh' | 'es' | 'de';

export type JlptLevelCode = 'N5' | 'N4' | 'N3' | 'N2' | 'N1';
export type TopikCode = 'TOPIK1' | 'TOPIK2' | 'TOPIK3' | 'TOPIK4' | 'TOPIK5' | 'TOPIK6';
/** Niveaux du CECRL suivis pour l'anglais (préparation au TOEIC). */
export type CefrCode = 'A1' | 'A2' | 'B1' | 'B2' | 'C1';
/** Niveaux du HSK (format en six niveaux, celui des sessions ordinaires). */
export type HskCode = 'HSK1' | 'HSK2' | 'HSK3' | 'HSK4' | 'HSK5' | 'HSK6';
/** Niveaux du DELE (espagnol, Instituto Cervantes), alignés sur le CECRL. */
export type DeleCode = 'DELEA1' | 'DELEA2' | 'DELEB1' | 'DELEB2' | 'DELEC1' | 'DELEC2';
/** Code d'un niveau du parcours, toutes langues confondues (le nom est historique). */
/** Niveaux du Goethe-Zertifikat (allemand, Goethe-Institut), alignés sur le CECRL. */
export type GoetheCode = 'GOETHEA1' | 'GOETHEA2' | 'GOETHEB1' | 'GOETHEB2' | 'GOETHEC1' | 'GOETHEC2';
export type JlptCode = JlptLevelCode | TopikCode | CefrCode | HskCode | DeleCode | GoetheCode;
export type LevelCode = JlptCode;

/** Niveaux du JLPT, du plus facile au plus difficile. */
export const JLPT_ONLY_LEVELS: JlptLevelCode[] = ['N5', 'N4', 'N3', 'N2', 'N1'];
/** Niveaux du TOPIK (TOPIK I : 1-2, TOPIK II : 3-6), du plus facile au plus difficile. */
export const TOPIK_LEVELS: TopikCode[] = ['TOPIK1', 'TOPIK2', 'TOPIK3', 'TOPIK4', 'TOPIK5', 'TOPIK6'];
/** Niveaux du CECRL pour l'anglais, du plus facile au plus difficile. */
export const CEFR_LEVELS: CefrCode[] = ['A1', 'A2', 'B1', 'B2', 'C1'];
/** Score TOEIC Listening & Reading (sur 990) correspondant à chaque niveau du CECRL, d'après la table d'ETS. */
export const TOEIC_SCORE_OF: Record<CefrCode, number> = { A1: 120, A2: 225, B1: 550, B2: 785, C1: 945 };
/** Niveaux du HSK, du plus facile au plus difficile. */
export const HSK_LEVELS: HskCode[] = ['HSK1', 'HSK2', 'HSK3', 'HSK4', 'HSK5', 'HSK6'];
/** Niveaux du DELE, du plus facile au plus difficile. */
export const DELE_LEVELS: DeleCode[] = ['DELEA1', 'DELEA2', 'DELEB1', 'DELEB2', 'DELEC1', 'DELEC2'];
/** Niveaux du Goethe-Zertifikat, du plus facile au plus difficile. */
export const GOETHE_LEVELS: GoetheCode[] = ['GOETHEA1', 'GOETHEA2', 'GOETHEB1', 'GOETHEB2', 'GOETHEC1', 'GOETHEC2'];
/** Tous les niveaux acceptés par l'API (le nom est historique). */
export const JLPT_LEVELS: JlptCode[] = [...JLPT_ONLY_LEVELS, ...TOPIK_LEVELS, ...CEFR_LEVELS, ...HSK_LEVELS, ...DELE_LEVELS, ...GOETHE_LEVELS];
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
  exam: 'JLPT' | 'TOPIK' | 'TOEIC' | 'HSK' | 'DELE' | 'Goethe';
  /** Code BCP 47 pour la synthèse vocale */
  speech: string;
  levels: JlptCode[];
  /** Premier niveau du parcours */
  firstLevel: JlptCode;
}

export const STUDY_LANGUAGES: StudyLanguageInfo[] = [
  { code: 'ja', name: 'Japonais', native: '日本語', glyph: '言', exam: 'JLPT', speech: 'ja-JP', levels: JLPT_ONLY_LEVELS, firstLevel: 'N5' },
  { code: 'ko', name: 'Coréen', native: '한국어', glyph: '한', exam: 'TOPIK', speech: 'ko-KR', levels: TOPIK_LEVELS, firstLevel: 'TOPIK1' },
  { code: 'en', name: 'Anglais', native: 'English', glyph: 'E', exam: 'TOEIC', speech: 'en-GB', levels: CEFR_LEVELS, firstLevel: 'A1' },
  { code: 'zh', name: 'Chinois', native: '中文', glyph: '中', exam: 'HSK', speech: 'zh-CN', levels: HSK_LEVELS, firstLevel: 'HSK1' },
  { code: 'es', name: 'Espagnol', native: 'Español', glyph: 'Ñ', exam: 'DELE', speech: 'es-ES', levels: DELE_LEVELS, firstLevel: 'DELEA1' },
  { code: 'de', name: 'Allemand', native: 'Deutsch', glyph: 'ß', exam: 'Goethe', speech: 'de-DE', levels: GOETHE_LEVELS, firstLevel: 'GOETHEA1' },
];
export const STUDY_LANGUAGE_CODES: StudyLanguage[] = STUDY_LANGUAGES.map((l) => l.code);

export function languageInfo(lang: StudyLanguage): StudyLanguageInfo {
  return STUDY_LANGUAGES.find((l) => l.code === lang) ?? STUDY_LANGUAGES[0];
}

/** Vrai pour un niveau du CECRL (anglais) : A1, A2, B1, B2, C1. */
export const isCefr = (code: string | null | undefined): code is CefrCode => !!code && /^[ABC][12]$/.test(code);

/** Vrai pour un niveau du HSK (chinois) : HSK1…HSK6. */
export const isHsk = (code: string | null | undefined): code is HskCode => !!code && /^HSK[1-6]$/.test(code);

/** Vrai pour un niveau du DELE (espagnol) : DELEA1…DELEC2. */
export const isDele = (code: string | null | undefined): code is DeleCode => !!code && /^DELE[ABC][12]$/.test(code);

/** Vrai pour un niveau du Goethe-Zertifikat (allemand) : GOETHEA1…GOETHEC2. */
export const isGoethe = (code: string | null | undefined): code is GoetheCode => !!code && /^GOETHE[ABC][12]$/.test(code);

/** Langue d'un niveau : Goethe → allemand, TOPIK → coréen, A1…C1 → anglais, HSK → chinois, DELE → espagnol, les autres (N5…N1) → japonais. */
export function languageOfLevel(code: string | null | undefined): StudyLanguage {
  if (code && code.startsWith('TOPIK')) return 'ko';
  if (isHsk(code)) return 'zh';
  if (isDele(code)) return 'es';
  if (isGoethe(code)) return 'de';
  return isCefr(code) ? 'en' : 'ja';
}

/** Libellé court d'un niveau : « N5 », « TOPIK 1 », « B1 », « HSK 1 », « DELE A1 ». */
export function levelLabel(code: string): string {
  if (isHsk(code)) return `HSK ${code.slice(3)}`;
  if (isDele(code)) return `DELE ${code.slice(4)}`;
  if (isGoethe(code)) return `Goethe ${code.slice(6)}`;
  return code.startsWith('TOPIK') ? `TOPIK ${code.slice(5)}` : code;
}

/** Libellé d'un niveau avec son examen : « JLPT N5 », « TOPIK 1 », « TOEIC B1 ». */
export function examLevelLabel(code: string): string {
  if (code.startsWith('TOPIK')) return `TOPIK ${code.slice(5)}`;
  if (isHsk(code)) return `HSK ${code.slice(3)}`;
  if (isDele(code)) return `DELE ${code.slice(4)}`;
  if (isGoethe(code)) return `Goethe ${code.slice(6)}`;
  return isCefr(code) ? `TOEIC ${code}` : `JLPT ${code}`;
}

/** Vrai si le texte contient du hangeul (coréen). */
export function hasHangul(s: string): boolean {
  return /[ᄀ-ᇿ㄰-㆏가-힯]/.test(s);
}

/** Vrai si le texte contient des kana (hiragana, katakana) : il est alors japonais. */
export const hasKana = (s: string) => /[\u3040-\u30ff々〆]/.test(s);
/** Vrai si le texte contient des caractères chinois (hanzi ou kanji). */
export const hasHan = (s: string) => /[\u3400-\u9fff]/.test(s);

/**
 * Langue des caractères chinois sans kana : un texte comme « 学生 » est chinois pour qui étudie le chinois,
 * japonais sinon. Fixée par l'application selon la langue étudiée (setHanLanguage).
 */
let hanLanguage: 'ja' | 'zh' = 'ja';
/** Langue des textes en lettres latines : l'espagnol ou l'allemand pour qui les étudie, l'anglais sinon. */
let latinLanguage: 'en' | 'es' | 'de' = 'en';
export function setHanLanguage(lang: StudyLanguage | null | undefined) {
  hanLanguage = lang === 'zh' ? 'zh' : 'ja';
  latinLanguage = lang === 'es' ? 'es' : lang === 'de' ? 'de' : 'en';
}
export const currentLatinLanguage = () => latinLanguage;
export const currentHanLanguage = () => hanLanguage;

/** Langue d'un texte à lire à voix haute : hangeul → coréen, kana → japonais, caractères chinois seuls → chinois ou japonais (selon la langue étudiée), lettres latines seules → espagnol (ñ, ¿, ¡ ou langue étudiée) ou anglais. */
export function textLanguage(s: string): StudyLanguage {
  if (hasHangul(s)) return 'ko';
  if (hasKana(s)) return 'ja';
  if (hasHan(s)) return hanLanguage;
  if (/[ñÑ¿¡]/.test(s)) return 'es';
  if (/[äöÄÖßẞ]/.test(s)) return 'de';
  return /[A-Za-z]/.test(s) ? latinLanguage : hanLanguage;
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

/**
 * Texte à faire lire par la synthèse vocale : la lecture en kana quand il y en a une (japonais),
 * mais jamais le pinyin (lettres latines), qu'une voix chinoise lirait mal : on lit alors les caractères.
 */
export function spokenForm(text: string, reading?: string | null): string {
  // Lecture d'un kanji seul : « なが(い) » se dit « ながい » (les parenthèses marquent l'okurigana).
  return reading && !/[A-Za-zÀ-ɏ]/.test(reading) ? reading.replace(/[()（）]/g, '') : text;
}
