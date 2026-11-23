import { AuthoredExercise, EngineItem, Question, QuestionType, authoredToQuestion, checkAnswer, generateQuestion } from './exercises';
import { Rng, shuffle } from './random';

/**
 * Examen blanc (phase 3) — format inspiré des épreuves du JLPT, sans prétendre les reproduire :
 * c'est un entraînement non officiel.
 */
export type ExamSectionId = 'vocab' | 'grammar' | 'listening' | 'reading' | 'writing';

export interface ExamSectionDef {
  id: ExamSectionId;
  title: string;
  jpTitle: string;
  count: number;
}

export interface ExamDef {
  slug: string;
  level: string;
  title: string;
  durationMin: number;
  sections: ExamSectionDef[];
  /** Seuils indicatifs de Koto Quest (volontairement exigeants). */
  passPercent: number;
  sectionMinPercent: number;
  /** Banque de questions rédigées (format officiel) au lieu des notions du parcours */
  bank?: string;
  /** Notation : pourcentages (défaut), barème du JLPT (180 points) ou du TOPIK I (200 points) */
  scoring?: 'percent' | 'jlpt' | 'jlpt3' | 'topik' | 'topik2' | 'toeic' | 'hsk' | 'hsk3';
  /** TOPIK : niveau à obtenir pour réussir l'examen (1 par défaut) */
  passLevel?: 1 | 2 | 3 | 4 | 5 | 6;
}

/** Barème officiel N4/N5 : langue + lecture sur 120, écoute sur 60 ; réussite à 80/180 (N5) ou 90/180 (N4), avec 38 et 19 minimum. */
export const JLPT_SCALE = { language: 120, listening: 60, total: 180, passTotal: 80, passLanguage: 38, passListening: 19 } as const;

/**
 * Barème officiel N3 à N1 : connaissances de la langue (vocabulaire, grammaire), lecture et écoute,
 * chacune sur 60, soit 180 ; au moins 19 dans chaque partie.
 */
export const JLPT3_SCALE = { language: 60, reading: 60, listening: 60, total: 180, passLanguage: 19, passReading: 19, passListening: 19 } as const;

/** Total à atteindre au JLPT selon le niveau. */
export const JLPT_PASS_TOTAL: Record<string, number> = { N5: 80, N4: 90, N3: 95, N2: 90, N1: 100 };

/**
 * Barème du TOPIK I : écoute (듣기) sur 100 et lecture (읽기) sur 100. Pas de minimum par épreuve :
 * niveau 1 à partir de 80/200, niveau 2 à partir de 140/200.
 */
export const TOPIK_I_SCALE = { language: 100, listening: 100, total: 200, passTotal: 80, passLanguage: 0, passListening: 0, level2: 140 } as const;

/**
 * Barème du TOPIK II : écoute (듣기), écriture (쓰기) et lecture (읽기), chacune sur 100, soit 300 points.
 * Niveau 3 à partir de 120, 4 à 150, 5 à 190, 6 à 230.
 */
export const TOPIK_II_SCALE = { language: 100, listening: 100, writing: 100, total: 300, levels: [{ level: 3, min: 120 }, { level: 4, min: 150 }, { level: 5, min: 190 }, { level: 6, min: 230 }] } as const;

/**
 * Barème du TOEIC Listening & Reading : écoute et lecture notées chacune de 5 à 495, soit 10 à 990.
 * Le TOEIC n'a pas de seuil de réussite : Koto Quest vise le score correspondant au niveau du CECRL
 * (table de correspondance d'ETS), sans minimum par épreuve.
 */
export const TOEIC_SCALE = { listening: 495, reading: 495, total: 990, floor: 5 } as const;
export const TOEIC_PASS_TOTAL: Record<string, number> = { A1: 120, A2: 225, B1: 550, B2: 785, C1: 945 };

/**
 * Barème du HSK 2.0 : chaque épreuve (听力 écoute, 阅读 lecture, 书写 écriture à partir du HSK 3) est notée sur 100.
 * HSK 1 et 2 : 200 points, réussite à 120 ; HSK 3 à 6 : 300 points, réussite à 180. Pas de minimum par épreuve.
 */
export const HSK_SCALE = { listening: 100, reading: 100, writing: 100 } as const;
export const HSK_PASS_TOTAL = { hsk: 120, hsk3: 180 } as const;

export interface ExamScale {
  system: 'jlpt' | 'topik' | 'toeic' | 'hsk';
  language: number;
  listening: number;
  total: number;
  passTotal: number;
  passLanguage: number;
  passListening: number;
  /** TOPIK : seuils des niveaux obtenus (1 puis 2) */
  levels?: { level: number; min: number }[];
  /** TOPIK : niveau à obtenir pour réussir cet examen */
  passLevel?: number;
  /** TOPIK II : écriture (쓰기) */
  writing?: number;
  /** JLPT N3 à N1 : lecture (読解), notée à part */
  reading?: number;
  passReading?: number;
}

/** Barème d'un examen noté sur points (JLPT ou TOPIK), ou null s'il est noté en pourcentage. */
export function examScale(def: ExamDef): ExamScale | null {
  if (def.scoring === 'jlpt') return { system: 'jlpt', ...JLPT_SCALE, passTotal: JLPT_PASS_TOTAL[def.level] ?? JLPT_SCALE.passTotal };
  if (def.scoring === 'jlpt3') return { system: 'jlpt', ...JLPT3_SCALE, passTotal: JLPT_PASS_TOTAL[def.level] ?? 95 };
  if (def.scoring === 'topik') {
    const { level2, ...rest } = TOPIK_I_SCALE;
    return { system: 'topik', ...rest, levels: [{ level: 1, min: TOPIK_I_SCALE.passTotal }, { level: 2, min: level2 }], passLevel: def.passLevel ?? 1 };
  }
  if (def.scoring === 'toeic')
    return { system: 'toeic', language: TOEIC_SCALE.reading, listening: TOEIC_SCALE.listening, total: TOEIC_SCALE.total, passTotal: TOEIC_PASS_TOTAL[def.level] ?? 550, passLanguage: 0, passListening: 0 };
  if (def.scoring === 'hsk')
    return { system: 'hsk', language: HSK_SCALE.reading, listening: HSK_SCALE.listening, total: 200, passTotal: HSK_PASS_TOTAL.hsk, passLanguage: 0, passListening: 0 };
  if (def.scoring === 'hsk3')
    return { system: 'hsk', language: HSK_SCALE.reading, listening: HSK_SCALE.listening, writing: HSK_SCALE.writing, total: 300, passTotal: HSK_PASS_TOTAL.hsk3, passLanguage: 0, passListening: 0 };
  if (def.scoring === 'topik2') {
    const passLevel = def.passLevel ?? 3;
    return {
      system: 'topik', language: TOPIK_II_SCALE.language, listening: TOPIK_II_SCALE.listening, writing: TOPIK_II_SCALE.writing, total: TOPIK_II_SCALE.total,
      passTotal: TOPIK_II_SCALE.levels[0].min, passLanguage: 0, passListening: 0, levels: TOPIK_II_SCALE.levels.map((l) => ({ ...l })), passLevel,
    };
  }
  return null;
}

export interface BankQuestion {
  jp?: string;
  text?: string;
  passage?: string;
  /** Document sonore : lignes « N|… » (narrateur), « M|… » (homme), « F|… » (femme) */
  audio?: string;
  audioChoices?: boolean;
  /** Partie 1 du TOEIC : scène illustrée (identifiant de TOEIC_SCENES) ; les phrases sont lues, pas écrites. */
  image?: string;
  choices: string[];
  answer: string;
  explanation?: string;
}

export interface BankPart {
  id: string;
  section: ExamSectionId;
  jpTitle: string;
  title: string;
  prompt: string;
  count: number;
  listening?: boolean;
  questions: BankQuestion[];
}

export interface ExamBank {
  slug: string;
  level: string;
  notice?: string;
  parts: BankPart[];
}

/** Tirage d'une épreuve dans la banque : nombre de questions fixé par partie, choix mélangés. */
export function planBankExam(bank: ExamBank, rng: Rng): PlannedExamQuestion[] {
  return bank.parts.flatMap((part) =>
    shuffle(part.questions, rng)
      .slice(0, part.count)
      .map((bq) => {
        const choices = shuffle(bq.choices, rng);
        // Photo (partie 1 du TOEIC) : les quatre phrases sont lues dans l'ordre affiché, numérotées.
        const audio = bq.image ? choices.map((c, i) => `N|${i + 1}. ${c}`).join('\n') : bq.audio;
        return {
          section: part.section,
          question: {
            type: (part.listening ? 'listening_choice' : 'particle_choice') as QuestionType,
            prompt: part.prompt,
            display: { jp: bq.jp, text: bq.text, passage: bq.passage, audioChoices: bq.audioChoices || !!bq.image, image: bq.image, part: part.jpTitle, maxPlays: part.listening ? 2 : undefined },
            audio,
            choices,
            answer: bq.answer,
            explanation: bq.explanation ?? `Réponse : ${bq.answer}`,
            guessable: false,
          },
        };
      }),
  );
}

/** Nombre de questions par section d'une banque (pour la définition de l'examen). */
export function bankSections(bank: ExamBank): Partial<Record<ExamSectionId, number>> {
  const out: Partial<Record<ExamSectionId, number>> = {};
  for (const p of bank.parts) out[p.section] = (out[p.section] ?? 0) + p.count;
  return out;
}

export const EXAM_N5: ExamDef = {
  slug: 'n5-mock',
  level: 'N5',
  title: 'Examen blanc JLPT N5',
  durationMin: 25,
  sections: [
    { id: 'vocab', title: 'Vocabulaire et kanji', jpTitle: '文字・語彙', count: 12 },
    { id: 'grammar', title: 'Grammaire et compréhension', jpTitle: '文法・読解', count: 10 },
    { id: 'listening', title: 'Compréhension orale', jpTitle: '聴解', count: 8 },
  ],
  passPercent: 60,
  sectionMinPercent: 40,
};

export const EXAM_N4: ExamDef = {
  slug: 'n4-mock',
  level: 'N4',
  title: 'Examen blanc JLPT N4',
  durationMin: 30,
  sections: [
    { id: 'vocab', title: 'Vocabulaire et kanji', jpTitle: '文字・語彙', count: 14 },
    { id: 'grammar', title: 'Grammaire et compréhension', jpTitle: '文法・読解', count: 12 },
    { id: 'listening', title: 'Compréhension orale', jpTitle: '聴解', count: 8 },
  ],
  passPercent: 60,
  sectionMinPercent: 40,
};

export const EXAM_N3: ExamDef = {
  slug: 'n3-mock',
  level: 'N3',
  title: 'Examen blanc JLPT N3',
  durationMin: 35,
  sections: [
    { id: 'vocab', title: 'Vocabulaire et kanji', jpTitle: '文字・語彙', count: 16 },
    { id: 'grammar', title: 'Grammaire et compréhension', jpTitle: '文法・読解', count: 14 },
    { id: 'listening', title: 'Compréhension orale', jpTitle: '聴解', count: 8 },
  ],
  passPercent: 60,
  sectionMinPercent: 40,
};

/** Examen blanc N5 au format officiel : banque rédigée, épreuves et barème du JLPT. */
export const EXAM_N5_JLPT: ExamDef = {
  slug: 'n5-jlpt',
  level: 'N5',
  title: 'Examen blanc JLPT N5 — format officiel',
  durationMin: 70,
  sections: [
    { id: 'vocab', title: 'Vocabulaire et kanji', jpTitle: '言語知識（文字・語彙）', count: 28 },
    { id: 'grammar', title: 'Grammaire et lecture', jpTitle: '言語知識（文法）・読解', count: 21 },
    { id: 'listening', title: 'Compréhension orale', jpTitle: '聴解', count: 18 },
  ],
  passPercent: 44,
  sectionMinPercent: 32,
  bank: 'n5-jlpt',
  scoring: 'jlpt',
};

const JLPT_OFFICIAL = (level: 'N4' | 'N3' | 'N2' | 'N1', durationMin: number, vocab: number, grammar: number, reading: number, listening: number): ExamDef => ({
  slug: `${level.toLowerCase()}-jlpt`,
  level,
  title: `Examen blanc JLPT ${level} — format officiel (abrégé)`,
  durationMin,
  sections:
    level === 'N4'
      ? [
          { id: 'vocab', title: 'Vocabulaire et kanji', jpTitle: '言語知識（文字・語彙）', count: vocab },
          { id: 'grammar', title: 'Grammaire et lecture', jpTitle: '言語知識（文法）・読解', count: grammar },
          { id: 'listening', title: 'Compréhension orale', jpTitle: '聴解', count: listening },
        ]
      : [
          { id: 'vocab', title: 'Vocabulaire et kanji', jpTitle: '言語知識（文字・語彙）', count: vocab },
          { id: 'grammar', title: 'Grammaire', jpTitle: '言語知識（文法）', count: grammar },
          { id: 'reading', title: 'Compréhension écrite', jpTitle: '読解', count: reading },
          { id: 'listening', title: 'Compréhension orale', jpTitle: '聴解', count: listening },
        ],
  passPercent: 50,
  sectionMinPercent: 32,
  bank: `${level.toLowerCase()}-jlpt`,
  scoring: level === 'N4' ? 'jlpt' : 'jlpt3',
});

/** Examens blancs N4 à N1 au format officiel (abrégé) : banques content/exams/nX-jlpt.json, barème du JLPT. */
export const EXAM_N4_JLPT = JLPT_OFFICIAL('N4', 60, 18, 14, 0, 8);
export const EXAM_N3_JLPT = JLPT_OFFICIAL('N3', 70, 18, 11, 3, 8);
export const EXAM_N2_JLPT = JLPT_OFFICIAL('N2', 75, 18, 11, 3, 8);
export const EXAM_N1_JLPT = JLPT_OFFICIAL('N1', 80, 14, 11, 3, 7);

export const EXAM_N2: ExamDef = {
  slug: 'n2-mock',
  level: 'N2',
  title: 'Examen blanc JLPT N2',
  durationMin: 40,
  sections: [
    { id: 'vocab', title: 'Vocabulaire et kanji', jpTitle: '文字・語彙', count: 18 },
    { id: 'grammar', title: 'Grammaire et compréhension', jpTitle: '文法・読解', count: 16 },
    { id: 'listening', title: 'Compréhension orale', jpTitle: '聴解', count: 8 },
  ],
  passPercent: 60,
  sectionMinPercent: 40,
};

export const EXAM_N1: ExamDef = {
  slug: 'n1-mock',
  level: 'N1',
  title: 'Examen blanc JLPT N1',
  durationMin: 45,
  sections: [
    { id: 'vocab', title: 'Vocabulaire et kanji', jpTitle: '文字・語彙', count: 18 },
    { id: 'grammar', title: 'Grammaire et compréhension', jpTitle: '文法・読解', count: 18 },
    { id: 'listening', title: 'Compréhension orale', jpTitle: '聴解', count: 8 },
  ],
  passPercent: 60,
  sectionMinPercent: 40,
};

/** Examen d'entraînement TOPIK 1 généré à partir des leçons (vocabulaire, grammaire, écoute). */
export const EXAM_TOPIK1_MOCK: ExamDef = {
  slug: 'topik1-mock',
  level: 'TOPIK1',
  title: 'Entraînement TOPIK 1',
  durationMin: 25,
  sections: [
    { id: 'vocab', title: 'Vocabulaire', jpTitle: '어휘', count: 12 },
    { id: 'grammar', title: 'Grammaire', jpTitle: '문법', count: 10 },
    { id: 'listening', title: 'Compréhension orale', jpTitle: '듣기', count: 8 },
  ],
  passPercent: 60,
  sectionMinPercent: 40,
};

/** Examen blanc TOPIK I au format officiel : banque rédigée en coréen, épreuves et barème du TOPIK I. */
export const EXAM_TOPIK1: ExamDef = {
  slug: 'topik1-official',
  level: 'TOPIK1',
  title: 'Examen blanc TOPIK I — format officiel',
  durationMin: 100,
  sections: [
    { id: 'listening', title: 'Compréhension orale', jpTitle: '듣기', count: 30 },
    { id: 'reading', title: 'Compréhension écrite', jpTitle: '읽기', count: 40 },
  ],
  passPercent: 40,
  sectionMinPercent: 0,
  bank: 'topik1',
  scoring: 'topik',
};

/** Examen blanc du niveau 2 : même format que le TOPIK I, banque enrichie de questions plus difficiles, réussite au niveau 2 (140/200). */
export const EXAM_TOPIK2: ExamDef = {
  ...EXAM_TOPIK1,
  slug: 'topik2-official',
  level: 'TOPIK2',
  title: 'Examen blanc TOPIK I (niveau 2) — format officiel',
  bank: 'topik2',
  passPercent: 70,
  passLevel: 2,
};

/** Examen blanc TOPIK II (version abrégée) : écoute, écriture (format adapté à choix) et lecture, notée sur 300 ; réussite au niveau 3 (120). */
export const EXAM_TOPIK3: ExamDef = {
  slug: 'topik3-official',
  level: 'TOPIK3',
  title: 'Examen blanc TOPIK II — format officiel (abrégé)',
  durationMin: 90,
  sections: [
    { id: 'listening', title: 'Compréhension orale', jpTitle: '듣기', count: 25 },
    { id: 'writing', title: 'Expression écrite', jpTitle: '쓰기', count: 5 },
    { id: 'reading', title: 'Compréhension écrite', jpTitle: '읽기', count: 25 },
  ],
  passPercent: 40,
  sectionMinPercent: 0,
  bank: 'topik3',
  scoring: 'topik2',
  passLevel: 3,
};

/** Examen blanc TOPIK II du niveau 4 : même format, banque enrichie de questions plus difficiles, réussite au niveau 4 (150/300). */
export const EXAM_TOPIK4: ExamDef = {
  ...EXAM_TOPIK3,
  slug: 'topik4-official',
  level: 'TOPIK4',
  title: 'Examen blanc TOPIK II (niveau 4) — format officiel (abrégé)',
  bank: 'topik4',
  passPercent: 50,
  passLevel: 4,
};

/** Examens blancs TOPIK II des niveaux 5 et 6 : banques enrichies, réussite à 190 puis 230 points sur 300. */
export const EXAM_TOPIK5: ExamDef = { ...EXAM_TOPIK3, slug: 'topik5-official', level: 'TOPIK5', title: 'Examen blanc TOPIK II (niveau 5) — format officiel (abrégé)', bank: 'topik5', passPercent: 63, passLevel: 5 };
export const EXAM_TOPIK6: ExamDef = { ...EXAM_TOPIK3, slug: 'topik6-official', level: 'TOPIK6', title: 'Examen blanc TOPIK II (niveau 6) — format officiel (abrégé)', bank: 'topik6', passPercent: 77, passLevel: 6 };
export const EXAM_TOPIK5_MOCK: ExamDef = { ...EXAM_TOPIK1_MOCK, slug: 'topik5-mock', level: 'TOPIK5', title: 'Entraînement TOPIK 5' };
export const EXAM_TOPIK6_MOCK: ExamDef = { ...EXAM_TOPIK1_MOCK, slug: 'topik6-mock', level: 'TOPIK6', title: 'Entraînement TOPIK 6' };

/** Examen d'entraînement TOPIK 4 généré à partir des leçons. */
export const EXAM_TOPIK4_MOCK: ExamDef = { ...EXAM_TOPIK1_MOCK, slug: 'topik4-mock', level: 'TOPIK4', title: 'Entraînement TOPIK 4' };

/** Examen d'entraînement TOPIK 3 généré à partir des leçons. */
export const EXAM_TOPIK3_MOCK: ExamDef = { ...EXAM_TOPIK1_MOCK, slug: 'topik3-mock', level: 'TOPIK3', title: 'Entraînement TOPIK 3' };

/** Examen d'entraînement TOPIK 2 généré à partir des leçons. */
export const EXAM_TOPIK2_MOCK: ExamDef = { ...EXAM_TOPIK1_MOCK, slug: 'topik2-mock', level: 'TOPIK2', title: 'Entraînement TOPIK 2' };

/**
 * Examen blanc TOEIC Listening & Reading (version abrégée) : parties 1 à 4 (écoute, dont des photos), 5 et 6 (phrases et
 * textes à compléter), 7 (compréhension écrite), noté sur 990. Banques content/exams/<niveau>-toeic.json.
 */
const TOEIC_OFFICIAL = (level: string, durationMin: number, listening: number, grammar: number, reading: number): ExamDef => ({
  slug: `${level.toLowerCase()}-toeic`,
  level,
  title: `Examen blanc TOEIC ${level} — format officiel (abrégé)`,
  durationMin,
  sections: [
    { id: 'listening', title: 'Compréhension orale', jpTitle: 'Listening (Parts 1–4)', count: listening },
    { id: 'grammar', title: 'Phrases et textes à compléter', jpTitle: 'Reading (Parts 5–6)', count: grammar },
    { id: 'reading', title: 'Compréhension écrite', jpTitle: 'Reading (Part 7)', count: reading },
  ],
  passPercent: 50,
  sectionMinPercent: 0,
  bank: `${level.toLowerCase()}-toeic`,
  scoring: 'toeic',
});

/** Entraînement généré à partir des leçons d'un niveau d'anglais (notions et exercices déjà rencontrés). */
const TOEIC_MOCK = (level: string): ExamDef => ({
  slug: `${level.toLowerCase()}-mock`,
  level,
  title: `Entraînement anglais ${level}`,
  durationMin: 25,
  sections: [
    { id: 'vocab', title: 'Vocabulaire', jpTitle: 'Vocabulary', count: 12 },
    { id: 'grammar', title: 'Grammaire', jpTitle: 'Grammar', count: 10 },
    { id: 'listening', title: 'Compréhension orale', jpTitle: 'Listening', count: 8 },
  ],
  passPercent: 60,
  sectionMinPercent: 40,
});

export const EXAM_A1_TOEIC = TOEIC_OFFICIAL('A1', 30, 12, 12, 6);
export const EXAM_A1_MOCK = TOEIC_MOCK('A1');
export const EXAM_A2_TOEIC = TOEIC_OFFICIAL('A2', 35, 14, 14, 8);
export const EXAM_A2_MOCK = TOEIC_MOCK('A2');
export const EXAM_B1_TOEIC = TOEIC_OFFICIAL('B1', 40, 16, 16, 10);
export const EXAM_B1_MOCK = TOEIC_MOCK('B1');
export const EXAM_B2_TOEIC = TOEIC_OFFICIAL('B2', 45, 18, 18, 12);
export const EXAM_B2_MOCK = TOEIC_MOCK('B2');
export const EXAM_C1_TOEIC = TOEIC_OFFICIAL('C1', 50, 20, 20, 14);
export const EXAM_C1_MOCK = TOEIC_MOCK('C1');

/**
 * Examen blanc HSK 2.0 au format officiel : 听力 (écoute), 阅读 (lecture) et, à partir du HSK 3, 书写 (écriture,
 * en format à choix adapté). Banques content/exams/hsk<n>.json, rédigées en chinois.
 */
const HSK_OFFICIAL = (n: number, durationMin: number, listening: number, reading: number, writing = 0, abridged = false): ExamDef => ({
  slug: `hsk${n}-official`,
  level: `HSK${n}`,
  title: `Examen blanc HSK ${n} — format officiel${abridged ? ' (abrégé)' : ''}`,
  durationMin,
  sections: [
    { id: 'listening', title: 'Compréhension orale', jpTitle: '听力', count: listening },
    { id: 'reading', title: 'Compréhension écrite', jpTitle: '阅读', count: reading },
    ...(writing ? [{ id: 'writing' as const, title: 'Expression écrite', jpTitle: '书写', count: writing }] : []),
  ],
  passPercent: 60,
  sectionMinPercent: 0,
  bank: `hsk${n}`,
  scoring: writing ? 'hsk3' : 'hsk',
});

/** Entraînement généré à partir des leçons d'un niveau HSK. */
const HSK_MOCK = (n: number): ExamDef => ({
  slug: `hsk${n}-mock`,
  level: `HSK${n}`,
  title: `Entraînement HSK ${n}`,
  durationMin: 25,
  sections: [
    { id: 'vocab', title: 'Vocabulaire', jpTitle: '词汇', count: 12 },
    { id: 'grammar', title: 'Grammaire', jpTitle: '语法', count: 10 },
    { id: 'listening', title: 'Compréhension orale', jpTitle: '听力', count: 8 },
  ],
  passPercent: 60,
  sectionMinPercent: 40,
});

export const EXAM_HSK1 = HSK_OFFICIAL(1, 40, 20, 20);
export const EXAM_HSK1_MOCK = HSK_MOCK(1);
export const EXAM_HSK2 = HSK_OFFICIAL(2, 55, 35, 25);
export const EXAM_HSK2_MOCK = HSK_MOCK(2);

export const EXAMS: Record<string, ExamDef> = {
  [EXAM_HSK1_MOCK.slug]: EXAM_HSK1_MOCK,
  [EXAM_HSK1.slug]: EXAM_HSK1,
  [EXAM_HSK2_MOCK.slug]: EXAM_HSK2_MOCK,
  [EXAM_HSK2.slug]: EXAM_HSK2,
  [EXAM_A1_MOCK.slug]: EXAM_A1_MOCK,
  [EXAM_A1_TOEIC.slug]: EXAM_A1_TOEIC,
  [EXAM_A2_MOCK.slug]: EXAM_A2_MOCK,
  [EXAM_A2_TOEIC.slug]: EXAM_A2_TOEIC,
  [EXAM_B1_MOCK.slug]: EXAM_B1_MOCK,
  [EXAM_B1_TOEIC.slug]: EXAM_B1_TOEIC,
  [EXAM_B2_MOCK.slug]: EXAM_B2_MOCK,
  [EXAM_B2_TOEIC.slug]: EXAM_B2_TOEIC,
  [EXAM_C1_MOCK.slug]: EXAM_C1_MOCK,
  [EXAM_C1_TOEIC.slug]: EXAM_C1_TOEIC,
  [EXAM_N1.slug]: EXAM_N1,
  [EXAM_N5.slug]: EXAM_N5,
  [EXAM_N4.slug]: EXAM_N4,
  [EXAM_N3.slug]: EXAM_N3,
  [EXAM_N2.slug]: EXAM_N2,
  [EXAM_N5_JLPT.slug]: EXAM_N5_JLPT,
  [EXAM_N4_JLPT.slug]: EXAM_N4_JLPT,
  [EXAM_N3_JLPT.slug]: EXAM_N3_JLPT,
  [EXAM_N2_JLPT.slug]: EXAM_N2_JLPT,
  [EXAM_N1_JLPT.slug]: EXAM_N1_JLPT,
  [EXAM_TOPIK1_MOCK.slug]: EXAM_TOPIK1_MOCK,
  [EXAM_TOPIK1.slug]: EXAM_TOPIK1,
  [EXAM_TOPIK2_MOCK.slug]: EXAM_TOPIK2_MOCK,
  [EXAM_TOPIK2.slug]: EXAM_TOPIK2,
  [EXAM_TOPIK3_MOCK.slug]: EXAM_TOPIK3_MOCK,
  [EXAM_TOPIK3.slug]: EXAM_TOPIK3,
  [EXAM_TOPIK4_MOCK.slug]: EXAM_TOPIK4_MOCK,
  [EXAM_TOPIK4.slug]: EXAM_TOPIK4,
  [EXAM_TOPIK5_MOCK.slug]: EXAM_TOPIK5_MOCK,
  [EXAM_TOPIK5.slug]: EXAM_TOPIK5,
  [EXAM_TOPIK6_MOCK.slug]: EXAM_TOPIK6_MOCK,
  [EXAM_TOPIK6.slug]: EXAM_TOPIK6,
};

/** Types de questions exclus d'une épreuve sans correction immédiate (association à plusieurs réponses). */
const EXAM_TYPES_EXCLUDED = new Set(['matching']);

export interface PlannedExamQuestion {
  section: ExamSectionId;
  question: Question;
}

function pickTyped(items: EngineItem[], pool: EngineItem[], types: QuestionType[], count: number, rng: Rng): Question[] {
  const out: Question[] = [];
  const used = new Set<string>();
  for (const item of shuffle(items, rng)) {
    if (out.length >= count) break;
    if (used.has(item.id)) continue;
    const allowed = types.filter((t) => t !== 'reading_choice' || (item.reading && item.reading !== item.front));
    const q = generateQuestion(item, pool, allowed[Math.floor(rng() * allowed.length)] ?? 'meaning_choice', rng);
    if (q) {
      out.push(q);
      used.add(item.id);
    }
  }
  return out;
}

/** Compose l'examen à partir du contenu du niveau (notions + exercices rédigés). */
export function planExam(def: ExamDef, items: EngineItem[], authored: AuthoredExercise[], pool: EngineItem[], rng: Rng): PlannedExamQuestion[] {
  const count = (id: ExamSectionId) => def.sections.find((s) => s.id === id)!.count;
  const lexical = items.filter((i) => i.kind === 'vocabulary' || i.kind === 'kanji');
  const vocab = pickTyped(lexical, pool, ['reading_choice', 'meaning_choice', 'reverse_choice'], count('vocab'), rng);

  const grammarAuthored = shuffle(
    authored.filter((e) => ['particle_choice', 'fill_blank', 'sentence_order', 'dialogue_choice'].includes(e.type)),
    rng,
  )
    .slice(0, count('grammar'))
    .map((e) => authoredToQuestion(e, rng));
  const grammarItems = pickTyped(items.filter((i) => i.kind === 'grammar'), pool, ['meaning_choice', 'reverse_choice'], count('grammar') - grammarAuthored.length, rng);

  const listening = pickTyped(items.filter((i) => i.kind === 'vocabulary' || i.kind === 'kana'), pool, ['listening_choice'], count('listening'), rng);

  return [
    ...vocab.map((q) => ({ section: 'vocab' as const, question: q })),
    ...[...grammarAuthored, ...grammarItems].filter((q) => !EXAM_TYPES_EXCLUDED.has(q.type)).map((q) => ({ section: 'grammar' as const, question: q })),
    ...listening.map((q) => ({ section: 'listening' as const, question: q })),
  ];
}

export interface ExamSectionScore {
  id: ExamSectionId;
  title: string;
  jpTitle: string;
  correct: number;
  total: number;
  percent: number;
}

export interface ExamGrade {
  sections: ExamSectionScore[];
  correct: number;
  total: number;
  percent: number;
  passed: boolean;
  weakest: ExamSectionId | null;
  /** Barème JLPT ou TOPIK (si l'examen l'utilise). TOPIK : `language` = lecture (읽기), `level` = niveau obtenu (0 = aucun). */
  scaled?: { language: number; listening: number; total: number; level?: number; writing?: number; reading?: number };
}

/** Corrige une copie : `answers` contient la réponse donnée (ou rien) pour chaque question. */
export function gradeExam(def: ExamDef, questions: { section: ExamSectionId; type: string; answer: string | string[] }[], answers: (unknown | undefined)[]): ExamGrade & { results: boolean[] } {
  const results = questions.map((q, i) => answers[i] !== undefined && answers[i] !== null && checkAnswer({ type: q.type as QuestionType, answer: q.answer }, answers[i]));
  const sections = def.sections.map((s) => {
    const idx = questions.map((q, i) => (q.section === s.id ? i : -1)).filter((i) => i >= 0);
    const correct = idx.filter((i) => results[i]).length;
    return { id: s.id, title: s.title, jpTitle: s.jpTitle, correct, total: idx.length, percent: idx.length ? Math.round((correct / idx.length) * 100) : 0 };
  });
  const correct = results.filter(Boolean).length;
  const total = questions.length;
  const weakest = sections.filter((s) => s.total > 0).sort((a, b) => a.percent - b.percent)[0]?.id ?? null;
  if (def.scoring === 'jlpt') {
    const lang = sections.filter((s) => s.id !== 'listening');
    const langTotal = lang.reduce((n, s) => n + s.total, 0);
    const langCorrect = lang.reduce((n, s) => n + s.correct, 0);
    const lis = sections.find((s) => s.id === 'listening')!;
    const scaled = {
      language: langTotal ? Math.round((langCorrect / langTotal) * JLPT_SCALE.language) : 0,
      listening: lis.total ? Math.round((lis.correct / lis.total) * JLPT_SCALE.listening) : 0,
      total: 0,
    };
    scaled.total = scaled.language + scaled.listening;
    const passTotal = JLPT_PASS_TOTAL[def.level] ?? JLPT_SCALE.passTotal;
    const passed = scaled.total >= passTotal && scaled.language >= JLPT_SCALE.passLanguage && scaled.listening >= JLPT_SCALE.passListening;
    return { sections, correct, total, percent: Math.round((scaled.total / JLPT_SCALE.total) * 100), passed, weakest, results, scaled };
  }
  if (def.scoring === 'jlpt3') {
    const pts = (list: typeof sections, max: number) => {
      const t = list.reduce((n, s) => n + s.total, 0);
      return t ? Math.round((list.reduce((n, s) => n + s.correct, 0) / t) * max) : 0;
    };
    const scaled = {
      language: pts(sections.filter((s) => s.id === 'vocab' || s.id === 'grammar'), JLPT3_SCALE.language),
      reading: pts(sections.filter((s) => s.id === 'reading'), JLPT3_SCALE.reading),
      listening: pts(sections.filter((s) => s.id === 'listening'), JLPT3_SCALE.listening),
      total: 0,
    };
    scaled.total = scaled.language + scaled.reading + scaled.listening;
    const passed = scaled.total >= (JLPT_PASS_TOTAL[def.level] ?? 95) && scaled.language >= JLPT3_SCALE.passLanguage && scaled.reading >= JLPT3_SCALE.passReading && scaled.listening >= JLPT3_SCALE.passListening;
    return { sections, correct, total, percent: Math.round((scaled.total / JLPT3_SCALE.total) * 100), passed, weakest, results, scaled };
  }
  if (def.scoring === 'topik') {
    const lis = sections.filter((s) => s.id === 'listening');
    const read = sections.filter((s) => s.id !== 'listening');
    const pts = (list: typeof sections, max: number) => {
      const t = list.reduce((n, s) => n + s.total, 0);
      return t ? Math.round((list.reduce((n, s) => n + s.correct, 0) / t) * max) : 0;
    };
    const scaled = { language: pts(read, TOPIK_I_SCALE.language), listening: pts(lis, TOPIK_I_SCALE.listening), total: 0, level: 0 };
    scaled.total = scaled.language + scaled.listening;
    scaled.level = scaled.total >= TOPIK_I_SCALE.level2 ? 2 : scaled.total >= TOPIK_I_SCALE.passTotal ? 1 : 0;
    return { sections, correct, total, percent: Math.round((scaled.total / TOPIK_I_SCALE.total) * 100), passed: scaled.level >= (def.passLevel ?? 1), weakest, results, scaled };
  }
  if (def.scoring === 'topik2') {
    const pts = (id: ExamSectionId, max: number) => {
      const s = sections.find((x) => x.id === id);
      return s && s.total ? Math.round((s.correct / s.total) * max) : 0;
    };
    const scaled = { listening: pts('listening', TOPIK_II_SCALE.listening), writing: pts('writing', TOPIK_II_SCALE.writing), language: pts('reading', TOPIK_II_SCALE.language), total: 0, level: 0 };
    scaled.total = scaled.listening + scaled.writing + scaled.language;
    scaled.level = [...TOPIK_II_SCALE.levels].reverse().find((l) => scaled.total >= l.min)?.level ?? 0;
    return { sections, correct, total, percent: Math.round((scaled.total / TOPIK_II_SCALE.total) * 100), passed: scaled.level >= (def.passLevel ?? 3), weakest, results, scaled };
  }
  if (def.scoring === 'hsk' || def.scoring === 'hsk3') {
    // HSK : 听力 (écoute), 阅读 (lecture, `language`) et, à partir du HSK 3, 书写 (écriture), chacune sur 100.
    const pts = (id: ExamSectionId) => {
      const x = sections.find((y) => y.id === id);
      return x && x.total ? Math.round((x.correct / x.total) * 100) : 0;
    };
    const writing = def.scoring === 'hsk3';
    const scaled: NonNullable<ExamGrade['scaled']> = { listening: pts('listening'), language: pts('reading'), total: 0 };
    if (writing) scaled.writing = pts('writing');
    scaled.total = scaled.listening + scaled.language + (scaled.writing ?? 0);
    const max = writing ? 300 : 200;
    return { sections, correct, total, percent: Math.round((scaled.total / max) * 100), passed: scaled.total >= HSK_PASS_TOTAL[def.scoring], weakest, results, scaled };
  }
  if (def.scoring === 'toeic') {
    // Lecture = parties 5 à 7 (phrases et textes à compléter, compréhension écrite) ; chaque épreuve vaut de 5 à 495.
    const pts = (list: typeof sections) => {
      const t = list.reduce((n, s) => n + s.total, 0);
      const c = list.reduce((n, s) => n + s.correct, 0);
      return Math.round((TOEIC_SCALE.floor + (t ? (c / t) * (TOEIC_SCALE.listening - TOEIC_SCALE.floor) : 0)) / 5) * 5;
    };
    const scaled = { listening: pts(sections.filter((s) => s.id === 'listening')), language: pts(sections.filter((s) => s.id !== 'listening')), total: 0 };
    scaled.total = scaled.listening + scaled.language;
    return { sections, correct, total, percent: Math.round((scaled.total / TOEIC_SCALE.total) * 100), passed: scaled.total >= (TOEIC_PASS_TOTAL[def.level] ?? 550), weakest, results, scaled };
  }
  const percent = total ? Math.round((correct / total) * 100) : 0;
  const passed = percent >= def.passPercent && sections.every((s) => s.total === 0 || s.percent >= def.sectionMinPercent);
  return { sections, correct, total, percent, passed, weakest, results };
}

/** Conseils de révision selon les sections les plus faibles. */
const TIPS_TOPIK1: Partial<Record<ExamSectionId, string>> = {
  vocab: 'Vocabulaire : refais les leçons TOPIK 1 et révise les mots du quotidien (nombres, lieux, famille, nourriture).',
  grammar: 'Grammaire : reprends les particules (은/는, 이/가, 을/를, 에/에서) et les terminaisons -아요/-어요, -았어요, -(으)ㄹ 거예요.',
  listening: 'Écoute (듣기) : réécoute les dialogues des leçons et joue à Listening Ninja ; entraîne-toi à reconnaître le lieu et le sujet d’une conversation.',
  reading: 'Lecture (읽기) : lis un chapitre de conte coréen chaque jour et entraîne-toi à repérer le sujet d’un court texte, d’une annonce ou d’un message.',
};

const TIPS_TOPIK2: Partial<Record<ExamSectionId, string>> = {
  vocab: 'Vocabulaire : refais les leçons TOPIK 2 et révise les mots des îles (raisons, permissions, temps, respect).',
  grammar: 'Grammaire : reprends les raisons (-아서, -(으)니까), les permissions et obligations, les propositions relatives (-는, -(으)ㄴ, -(으)ㄹ) et les honorifiques (-(으)시-, 드시다, 께).',
  listening: 'Écoute (듣기) : réécoute les dialogues des leçons TOPIK 2 et repère l’idée principale et les détails (qui, quand, pourquoi).',
  reading: 'Lecture (읽기) : lis les contes de niveau TOPIK 2 et entraîne-toi aux textes plus longs : idée principale, ordre des phrases, détails.',
};

const TIPS_TOPIK3: Partial<Record<ExamSectionId, string>> = {
  vocab: 'Vocabulaire : refais les leçons TOPIK 3 et révise les mots des îles (rumeurs, changements, buts, passif et causatif).',
  grammar: 'Grammaire : reprends le discours indirect (-다고, -냐고, -대요), -는데, -거든요, -잖아요, -게 되다, -아/어지다, -기 위해서, -도록 et le passif.',
  listening: 'Écoute (듣기) : réécoute les dialogues TOPIK 3 et entraîne-toi à deviner la suite d’une conversation et l’action qui va suivre.',
  reading: 'Lecture (읽기) : lis les contes de niveau TOPIK 3 et entraîne-toi aux titres de presse, aux reformulations et aux textes longs.',
  writing: 'Écriture (쓰기) : complète des phrases avec la grammaire du niveau (-기 위해서, -는데, -(으)ㄹ 것 같다) et entraîne-toi à décrire un tableau ou un graphique.',
};

const TIPS_TOPIK4: Partial<Record<ExamSectionId, string>> = {
  vocab: 'Vocabulaire : refais les leçons TOPIK 4 et révise les mots de société (environnement, prix, travail, presse).',
  grammar: 'Grammaire : reprends -다면서요, -더라고요, -는 모양이다, -나 보다, -다면, -았/었더라면, -더라도, -는데도, -는 바람에, -느라고, -는 김에 et -아/어 버리다.',
  listening: 'Écoute (듣기) : réécoute les dialogues TOPIK 4 et entraîne-toi à repérer l’attitude et l’intention de la personne qui parle.',
  reading: 'Lecture (읽기) : lis les contes de niveau TOPIK 4 et entraîne-toi aux articles de presse, aux titres et au but d’un texte.',
  writing: 'Écriture (쓰기) : complète des textes argumentés avec -더라도, -(으)ㄹ 뿐만 아니라, -는 데다가, et décris l’évolution d’un graphique.',
};

const TIPS_TOPIK5: Partial<Record<ExamSectionId, string>> = {
  vocab: 'Vocabulaire : refais les leçons TOPIK 5 et révise les mots abstraits (valeur, cause, influence, responsabilité, destin).',
  grammar: 'Grammaire : reprends -기 마련이다, -는 법이다, -는 반면에, -(으)ㄹ 만하다, -(으)ㄹ 리가 없다, -는 한, -(으)므로, -(으)ㄴ 셈이다, -(으)ㄹ수록, -다가는, -기는커녕, 조차, 마저 et -(으)ㄴ 이상.',
  listening: 'Écoute (듣기) : réécoute les dialogues TOPIK 5 et entraîne-toi aux exposés et aux débats : idée centrale, attitude, argument.',
  reading: 'Lecture (읽기) : lis le conte de la princesse Bari et entraîne-toi aux textes argumentatifs et aux reformulations.',
  writing: 'Écriture (쓰기) : complète des textes argumentés avec -기 마련이다, -(으)므로, -는 반면에, et compare des données d’un graphique.',
};

const TIPS_TOPIK6: Partial<Record<ExamSectionId, string>> = {
  vocab: 'Vocabulaire : refais les leçons TOPIK 6 et révise les proverbes (속담) et les expressions en quatre caractères (사자성어).',
  grammar: 'Grammaire : reprends -고자 하다, -(으)며, -는 바, -(으)ㄴ들, -(으)ㄹ지언정, -다시피, -는 듯하다, -기 그지없다, -(으)ㄹ까 봐, -는 마당에, -(으)ㄴ 나머지, -기 십상이다 et -(으)ㄹ 게 뻔하다.',
  listening: 'Écoute (듣기) : réécoute les dialogues TOPIK 6 et entraîne-toi aux conférences : but de l’intervenant, organisation, nuances.',
  reading: 'Lecture (읽기) : lis le mythe de Dangun et entraîne-toi aux textes académiques, aux proverbes et aux idées implicites.',
  writing: 'Écriture (쓰기) : complète des textes soutenus (-고자, -(으)며, -는 바와 같이) et justifie une opinion avec des arguments nuancés.',
};

const TIPS_N4: Partial<Record<ExamSectionId, string>> = {
  vocab: 'Vocabulaire et kanji : refais les leçons du N4 et entraîne-toi aux kanji avec Kanji Rush.',
  grammar: 'Grammaire : reprends les formes en て, ない, た et du dictionnaire (îles 1 à 3), puis les comparaisons et les raisons (îles 4 et 5), donner/recevoir et 〜たら (îles 6 et 7).',
  listening: 'Écoute : joue à Listening Ninja et réécoute les exemples des leçons N4 en vitesse lente.',
};

const TIPS_N1: Partial<Record<ExamSectionId, string>> = {
  vocab: 'Vocabulaire et kanji : refais les leçons du N1 et entraîne-toi aux kanji avec Kanji Rush.',
  grammar: 'Grammaire : reprends le style des proclamations et les extrêmes (îles 1 et 2), les concessions et les jugements (îles 3 et 4), puis les degrés, les occasions et les conditions inévitables (îles 5 à 7) et le style des discours (île 8).',
  listening: 'Écoute : joue à Listening Ninja et réécoute les exemples des leçons N1 en vitesse lente.',
};

const TIPS_N2: Partial<Record<ExamSectionId, string>> = {
  vocab: 'Vocabulaire et kanji : refais les leçons du N2 et entraîne-toi aux kanji avec Kanji Rush.',
  grammar: 'Grammaire : reprends les points de vue et les sources (île 1), l’instant précis (île 2), les raisons et les oppositions (îles 3 et 4), puis l’étendue, les conditions et les tendances (îles 5 à 7) et les convictions du locuteur (île 8).',
  listening: 'Écoute : joue à Listening Ninja et réécoute les exemples des leçons N2 en vitesse lente.',
};

const TIPS_N3: Partial<Record<ExamSectionId, string>> = {
  vocab: 'Vocabulaire et kanji : refais les leçons du N3 et entraîne-toi aux kanji avec Kanji Rush.',
  grammar: 'Grammaire : reprends les impressions (〜ようだ, 〜らしい, 〜はずだ) et les décisions (îles 1 et 2), puis les concessions et le moment de l’action (îles 3 et 4), les raisons, les degrés et les points de vue (îles 5 à 7).',
  listening: 'Écoute : joue à Listening Ninja et réécoute les exemples des leçons N3 en vitesse lente.',
};

const TIPS_EN: Partial<Record<ExamSectionId, string>> = {
  vocab: 'Vocabulaire : refais les leçons du niveau et joue à Word Rush pour retrouver vite le sens des mots.',
  grammar: 'Phrases à compléter (parties 5 et 6) : reprends les leçons de grammaire du niveau et entraîne-toi dans l’atelier TOEIC.',
  listening: 'Écoute (parties 1 à 4) : décris les photos à voix haute, réécoute les dialogues des leçons, joue à Listening Ninja et entraîne-toi aux questions-réponses de l’atelier TOEIC.',
  reading: 'Compréhension écrite (partie 7) : lis un chapitre de conte en anglais chaque jour et entraîne-toi à repérer l’essentiel d’un e-mail, d’une annonce ou d’un mémo.',
};

/** Conseils HSK (communs aux niveaux : les leçons et contes du niveau étudié). */
const TIPS_HSK: Partial<Record<ExamSectionId, string>> = {
  vocab: 'Vocabulaire : refais les leçons du niveau et joue à Hanzi Rush pour reconnaître vite les caractères, leur sens et leur pinyin.',
  grammar: 'Grammaire : reprends les leçons de grammaire du niveau (ordre des mots, 的, 了, 吗, les mesures) et les phrases à remettre dans l’ordre.',
  listening: 'Écoute (听力) : réécoute les dialogues des leçons, joue à Listening Ninja et entraîne-toi à reconnaître les tons des mots du niveau.',
  reading: 'Lecture (阅读) : lis un chapitre de conte chinois chaque jour et entraîne-toi à lire sans le pinyin les mots que tu connais.',
  writing: 'Écriture (书写) : remets des mots dans l’ordre pour former une phrase et entraîne-toi à reconnaître le bon caractère d’après son pinyin.',
};

export function examRecommendations(grade: ExamGrade, level = 'N5'): string[] {
  if (/^HSK[1-6]$/.test(level)) {
    const weakZh = grade.sections.filter((s) => s.total > 0 && s.percent < 75).sort((a, b) => a.percent - b.percent);
    if (!weakZh.length) return ['Très bon résultat dans toutes les sections. Continue tes révisions quotidiennes pour le garder dans la durée.'];
    return weakZh.map((s) => TIPS_HSK[s.id] ?? TIPS_HSK.grammar!).filter(Boolean);
  }
  if (/^[ABC][12]$/.test(level)) {
    const weakEn = grade.sections.filter((s) => s.total > 0 && s.percent < 75).sort((a, b) => a.percent - b.percent);
    if (!weakEn.length) return ['Très bon résultat dans toutes les sections. Continue tes révisions quotidiennes pour le garder dans la durée.'];
    return weakEn.map((s) => TIPS_EN[s.id] ?? TIPS_EN.grammar!).filter(Boolean);
  }
  const tips: Partial<Record<ExamSectionId, string>> = level === 'TOPIK1' ? TIPS_TOPIK1 : level === 'TOPIK2' ? TIPS_TOPIK2 : level === 'TOPIK3' ? TIPS_TOPIK3 : level === 'TOPIK4' ? TIPS_TOPIK4 : level === 'TOPIK5' ? TIPS_TOPIK5 : level === 'TOPIK6' ? TIPS_TOPIK6 : level === 'N1' ? TIPS_N1 : level === 'N2' ? TIPS_N2 : level === 'N3' ? TIPS_N3 : level === 'N4' ? TIPS_N4 : {
    vocab: 'Vocabulaire et kanji : entraîne-toi dans l’onglet Caractères et avec Kanji Rush, puis refais les leçons des mondes 5 et 7.',
    grammar: 'Grammaire : reprends les leçons sur les particules (mondes 3, 4 et 6) et les phrases à remettre dans l’ordre.',
    listening: 'Écoute : joue à Listening Ninja et réécoute les exemples des leçons en vitesse lente.',
  };
  const weak = grade.sections.filter((s) => s.total > 0 && s.percent < 75).sort((a, b) => a.percent - b.percent);
  if (!weak.length) return ['Très bon résultat dans toutes les sections. Continue tes révisions quotidiennes pour le garder dans la durée.'];
  return weak.map((s) => tips[s.id] ?? tips.grammar ?? '').filter(Boolean);
}

// ───────── Test de positionnement ─────────

export const PLACEMENT_BLOCK = 3;
export const PLACEMENT_PASS = 2;

/** Bloc de questions pour un monde : notions du monde et, si possible, un exercice rédigé. */
export function planPlacementBlock(items: EngineItem[], authored: AuthoredExercise[], pool: EngineItem[], rng: Rng): Question[] {
  const fromAuthored = shuffle(authored.filter((e) => e.type !== 'sentence_order'), rng).slice(0, 1).map((e) => authoredToQuestion(e, rng));
  const generated = pickTyped(items.filter((i) => i.kind !== 'grammar'), pool, ['meaning_choice', 'reverse_choice'], PLACEMENT_BLOCK - fromAuthored.length, rng);
  return shuffle([...generated, ...fromAuthored], rng).filter((q) => !EXAM_TYPES_EXCLUDED.has(q.type));
}

export const placementBlockPassed = (correct: number) => correct >= PLACEMENT_PASS;
