import { AuthoredExercise, EngineItem, Question, QuestionType, authoredToQuestion, checkAnswer, generateQuestion } from './exercises';
import { Rng, shuffle } from './random';

/**
 * Examen blanc (phase 3) — format inspiré des épreuves du JLPT, sans prétendre les reproduire :
 * c'est un entraînement non officiel.
 */
export type ExamSectionId = 'vocab' | 'grammar' | 'listening';

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
  /** Notation : pourcentages (défaut) ou barème du JLPT (180 points) */
  scoring?: 'percent' | 'jlpt';
}

/** Barème officiel N4/N5 : langue + lecture sur 120, écoute sur 60 ; réussite à 80/180 avec 38 et 19 minimum. */
export const JLPT_SCALE = { language: 120, listening: 60, total: 180, passTotal: 80, passLanguage: 38, passListening: 19 } as const;

export interface BankQuestion {
  jp?: string;
  text?: string;
  passage?: string;
  /** Document sonore : lignes « N|… » (narrateur), « M|… » (homme), « F|… » (femme) */
  audio?: string;
  audioChoices?: boolean;
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
      .map((bq) => ({
        section: part.section,
        question: {
          type: (part.listening ? 'listening_choice' : 'particle_choice') as QuestionType,
          prompt: part.prompt,
          display: { jp: bq.jp, text: bq.text, passage: bq.passage, audioChoices: bq.audioChoices, part: part.jpTitle, maxPlays: part.listening ? 2 : undefined },
          audio: bq.audio,
          choices: shuffle(bq.choices, rng),
          answer: bq.answer,
          explanation: bq.explanation ?? `Réponse : ${bq.answer}`,
          guessable: false,
        },
      })),
  );
}

/** Nombre de questions par section d'une banque (pour la définition de l'examen). */
export function bankSections(bank: ExamBank): Record<ExamSectionId, number> {
  const out: Record<ExamSectionId, number> = { vocab: 0, grammar: 0, listening: 0 };
  for (const p of bank.parts) out[p.section] += p.count;
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

export const EXAMS: Record<string, ExamDef> = { [EXAM_N5.slug]: EXAM_N5, [EXAM_N4.slug]: EXAM_N4, [EXAM_N5_JLPT.slug]: EXAM_N5_JLPT };

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
  /** Barème JLPT (si l'examen l'utilise) */
  scaled?: { language: number; listening: number; total: number };
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
    const passed = scaled.total >= JLPT_SCALE.passTotal && scaled.language >= JLPT_SCALE.passLanguage && scaled.listening >= JLPT_SCALE.passListening;
    return { sections, correct, total, percent: Math.round((scaled.total / JLPT_SCALE.total) * 100), passed, weakest, results, scaled };
  }
  const percent = total ? Math.round((correct / total) * 100) : 0;
  const passed = percent >= def.passPercent && sections.every((s) => s.total === 0 || s.percent >= def.sectionMinPercent);
  return { sections, correct, total, percent, passed, weakest, results };
}

/** Conseils de révision selon les sections les plus faibles. */
const TIPS_N4: Record<ExamSectionId, string> = {
  vocab: 'Vocabulaire et kanji : refais les leçons du N4 et entraîne-toi aux kanji avec Kanji Rush.',
  grammar: 'Grammaire : reprends les formes en て, ない, た et du dictionnaire (îles 1 à 3), puis les comparaisons et les raisons (îles 4 et 5), donner/recevoir et 〜たら (îles 6 et 7).',
  listening: 'Écoute : joue à Listening Ninja et réécoute les exemples des leçons N4 en vitesse lente.',
};

export function examRecommendations(grade: ExamGrade, level = 'N5'): string[] {
  const tips: Record<ExamSectionId, string> = level === 'N4' ? TIPS_N4 : {
    vocab: 'Vocabulaire et kanji : entraîne-toi dans l’onglet Caractères et avec Kanji Rush, puis refais les leçons des mondes 5 et 7.',
    grammar: 'Grammaire : reprends les leçons sur les particules (mondes 3, 4 et 6) et les phrases à remettre dans l’ordre.',
    listening: 'Écoute : joue à Listening Ninja et réécoute les exemples des leçons en vitesse lente.',
  };
  const weak = grade.sections.filter((s) => s.total > 0 && s.percent < 75).sort((a, b) => a.percent - b.percent);
  if (!weak.length) return ['Très bon résultat dans toutes les sections. Continue tes révisions quotidiennes pour le garder dans la durée.'];
  return weak.map((s) => tips[s.id]);
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
