import { addDays } from './time';

/**
 * Succès (badges) : définis ici une seule fois, évalués à partir de statistiques agrégées
 * calculées côté serveur (ou par le mode hors ligne). Un succès débloqué le reste, même si la
 * statistique redescend plus tard (ex. une notion maîtrisée redevenue fragile).
 */

export type AchievementRarity = 'common' | 'rare' | 'epic';
export type AchievementCategory = 'study' | 'streak' | 'mastery' | 'adventure' | 'play';

export interface AchievementStats {
  lessonsCompleted: number;
  perfectLessons: number;
  /** Plus longue suite de jours actifs consécutifs */
  bestStreak: number;
  correctAnswers: number;
  reviewsDone: number;
  /** Meilleure série de bonnes réponses d'affilée sur une journée */
  bestCombo: number;
  masteredItems: number;
  masteredKanji: number;
  bossesDefeated: number;
  examsTaken: number;
  examsPassed: number;
  gamesPlayed: number;
  bestGameScore: number;
  itemsCollected: number;
  placementDone: number;
  /** Kana (hiragana, katakana) maîtrisés */
  masteredKana: number;
  /** Gardiens japonais (îles du JLPT) vaincus */
  japaneseBosses: number;
  /** Examens blancs du JLPT validés */
  jlptPassed: number;
  /** Chapitres de contes japonais lus */
  japaneseChapters: number;
  /** Lettres et syllabes du hangeul maîtrisées */
  masteredHangul: number;
  /** Gardiens coréens (îles du TOPIK) vaincus */
  koreanBosses: number;
  /** Examens blancs du TOPIK validés */
  topikPassed: number;
  /** Chapitres de contes coréens lus */
  koreanChapters: number;
  /** Gardiens anglais (îles A1 à C1) vaincus */
  englishBosses: number;
  /** Examens blancs du TOEIC validés */
  toeicPassed: number;
  /** Chapitres de contes anglais lus */
  englishChapters: number;
  /** Gardiens chinois (îles du HSK) vaincus */
  chineseBosses: number;
  /** Examens blancs du HSK validés */
  hskPassed: number;
  /** Chapitres de contes chinois lus */
  chineseChapters: number;
  /** Gardiens espagnols (îles du DELE) vaincus */
  spanishBosses: number;
  /** Examens blancs du DELE validés */
  delePassed: number;
  /** Chapitres de contes espagnols lus */
  spanishChapters: number;
  /** Gardiens allemands (îles du Goethe-Zertifikat) vaincus */
  germanBosses: number;
  /** Examens blancs du Goethe-Zertifikat validés */
  goethePassed: number;
  /** Chapitres de contes allemands lus */
  germanChapters: number;
}

/** Langue d'un monde ou d'un examen d'après son slug : topik… → coréen, a1-…/c1-… → anglais, hsk… → chinois, dele… → espagnol, goethe… → allemand, sinon japonais. */
export function languageOfSlug(slug: string): 'ja' | 'ko' | 'en' | 'zh' | 'es' | 'de' {
  if (slug.startsWith('topik')) return 'ko';
  if (slug.startsWith('dele')) return 'es';
  if (slug.startsWith('goethe')) return 'de';
  if (slug.startsWith('hsk')) return 'zh';
  return /^[abc][12]-/.test(slug) ? 'en' : 'ja';
}

export interface AchievementDef {
  slug: string;
  title: string;
  description: string;
  /** Idéogramme du badge */
  glyph: string;
  category: AchievementCategory;
  rarity: AchievementRarity;
  metric: keyof AchievementStats;
  target: number;
  /** Succès propre à une langue étudiée : montré seulement à qui l'étudie (ou l'a déjà débloqué). */
  language?: 'ja' | 'ko' | 'en' | 'zh' | 'es' | 'de';
}

export const ACHIEVEMENT_COINS: Record<AchievementRarity, number> = { common: 10, rare: 25, epic: 50 };
export const ACHIEVEMENT_XP: Record<AchievementRarity, number> = { common: 10, rare: 30, epic: 60 };

export const ACHIEVEMENT_CATEGORIES: Record<AchievementCategory, string> = {
  study: 'Étude',
  streak: 'Régularité',
  mastery: 'Maîtrise',
  adventure: 'Aventure',
  play: 'Jeux et collection',
};

const a = (slug: string, glyph: string, title: string, description: string, category: AchievementCategory, rarity: AchievementRarity, metric: keyof AchievementStats, target: number, language?: 'ja' | 'ko' | 'en' | 'zh' | 'es' | 'de'): AchievementDef => ({ slug, glyph, title, description, category, rarity, metric, target, ...(language ? { language } : {}) });

export const ACHIEVEMENTS: AchievementDef[] = [
  // Étude
  a('first-lesson', '始', 'Premier pas', 'Terminer une première leçon.', 'study', 'common', 'lessonsCompleted', 1),
  a('ten-lessons', '学', 'Apprenti·e assidu·e', 'Terminer 10 leçons.', 'study', 'rare', 'lessonsCompleted', 10),
  a('all-n5-lessons', '修', 'Voyageur du N5', 'Terminer 25 leçons.', 'study', 'epic', 'lessonsCompleted', 25),
  a('first-perfect', '満', 'Sans faute', 'Réussir une leçon sans aucune erreur.', 'study', 'common', 'perfectLessons', 1),
  a('ten-perfect', '極', 'Perfectionniste', 'Réussir 10 leçons sans faute.', 'study', 'epic', 'perfectLessons', 10),
  a('hundred-correct', '百', 'Cent bonnes réponses', 'Donner 100 bonnes réponses.', 'study', 'common', 'correctAnswers', 100),
  a('thousand-correct', '千', 'Mille bonnes réponses', 'Donner 1 000 bonnes réponses.', 'study', 'epic', 'correctAnswers', 1000),
  a('combo-10', '連', 'Sur une lancée', '10 bonnes réponses d’affilée dans la journée.', 'study', 'common', 'bestCombo', 10),
  a('combo-30', '雷', 'Inarrêtable', '30 bonnes réponses d’affilée dans la journée.', 'study', 'rare', 'bestCombo', 30),
  // Régularité
  a('streak-3', '火', 'Ça chauffe', 'Étudier 3 jours de suite.', 'streak', 'common', 'bestStreak', 3),
  a('streak-7', '週', 'Une semaine complète', 'Étudier 7 jours de suite.', 'streak', 'rare', 'bestStreak', 7),
  a('streak-30', '月', 'Un mois sans faiblir', 'Étudier 30 jours de suite.', 'streak', 'epic', 'bestStreak', 30),
  a('reviews-50', '復', 'Mémoire entretenue', 'Faire 50 révisions.', 'streak', 'common', 'reviewsDone', 50),
  a('reviews-500', '憶', 'Mémoire d’éléphant', 'Faire 500 révisions.', 'streak', 'rare', 'reviewsDone', 500),
  // Maîtrise
  a('mastered-25', '芽', 'Premières pousses', 'Maîtriser 25 notions.', 'mastery', 'common', 'masteredItems', 25),
  a('mastered-100', '木', 'Jeune arbre', 'Maîtriser 100 notions.', 'mastery', 'rare', 'masteredItems', 100),
  a('mastered-300', '森', 'Forêt du savoir', 'Maîtriser 300 notions.', 'mastery', 'epic', 'masteredItems', 300),
  a('kanji-10', '字', 'Calligraphe', 'Maîtriser 10 kanji.', 'mastery', 'common', 'masteredKanji', 10, 'ja'),
  a('kanji-50', '書', 'Maître du pinceau', 'Maîtriser 50 kanji.', 'mastery', 'epic', 'masteredKanji', 50, 'ja'),
  a('kana-20', 'あ', 'Premiers kana', 'Maîtriser 20 hiragana ou katakana.', 'mastery', 'common', 'masteredKana', 20, 'ja'),
  a('kana-92', 'ア', 'Virtuose des kana', 'Maîtriser 92 kana (les hiragana et katakana de base).', 'mastery', 'epic', 'masteredKana', 92, 'ja'),
  a('hangul-10', '한', 'Premières lettres', 'Maîtriser 10 lettres ou syllabes du hangeul.', 'mastery', 'common', 'masteredHangul', 10, 'ko'),
  a('hangul-40', '글', 'Héritier·e du roi Sejong', 'Maîtriser 40 lettres et syllabes du hangeul.', 'mastery', 'epic', 'masteredHangul', 40, 'ko'),
  // Aventure
  a('first-boss', '勝', 'Premier gardien', 'Vaincre un gardien de fin de monde.', 'adventure', 'common', 'bossesDefeated', 1),
  a('four-bosses', '武', 'Chasseur de yokai', 'Vaincre 4 gardiens.', 'adventure', 'rare', 'bossesDefeated', 4),
  a('all-bosses', '王', 'Protecteur des huit mondes', 'Vaincre 8 gardiens.', 'adventure', 'epic', 'bossesDefeated', 8),
  a('placement', '診', 'Bilan fait', 'Passer le test de positionnement.', 'adventure', 'common', 'placementDone', 1),
  a('first-exam', '試', 'Premier examen blanc', 'Rendre un examen blanc complet.', 'adventure', 'common', 'examsTaken', 1),
  a('exam-passed', '合', 'Seuil atteint', 'Atteindre le seuil indicatif d’un examen blanc.', 'adventure', 'epic', 'examsPassed', 1),
  a('ja-bosses-8', '鬼', 'Exorciste en herbe', 'Vaincre 8 gardiens japonais.', 'adventure', 'rare', 'japaneseBosses', 8, 'ja'),
  a('ja-bosses-24', '侍', 'Shōgun des îles', 'Vaincre 24 gardiens japonais.', 'adventure', 'epic', 'japaneseBosses', 24, 'ja'),
  a('jlpt-passed', '認', 'JLPT en poche', 'Valider un examen blanc du JLPT.', 'adventure', 'epic', 'jlptPassed', 1, 'ja'),
  a('ja-tales-10', '読', 'Conteur·se du Japon', 'Lire 10 chapitres de contes japonais.', 'study', 'rare', 'japaneseChapters', 10, 'ja'),
  a('ko-bosses-8', '범', 'Ami·e des dokkaebi', 'Vaincre 8 gardiens coréens.', 'adventure', 'rare', 'koreanBosses', 8, 'ko'),
  a('ko-bosses-24', '용', 'Gardien·ne des mythes', 'Vaincre 24 gardiens coréens.', 'adventure', 'epic', 'koreanBosses', 24, 'ko'),
  a('topik-passed', '합', 'TOPIK en poche', 'Valider un examen blanc du TOPIK au niveau visé.', 'adventure', 'epic', 'topikPassed', 1, 'ko'),
  a('ko-tales-10', '읽', 'Conteur·se de Corée', 'Lire 10 chapitres de contes coréens.', 'study', 'rare', 'koreanChapters', 10, 'ko'),
  a('en-bosses-8', '♞', 'Chevalier·ère de la Table ronde', 'Vaincre 8 gardiens anglais.', 'adventure', 'rare', 'englishBosses', 8, 'en'),
  a('en-bosses-24', '♛', 'Légende d’Albion', 'Vaincre 24 gardiens anglais.', 'adventure', 'epic', 'englishBosses', 24, 'en'),
  a('toeic-passed', 'T', 'TOEIC en poche', 'Atteindre le score TOEIC visé à un examen blanc.', 'adventure', 'epic', 'toeicPassed', 1, 'en'),
  a('en-tales-10', '✒', 'Conteur·se d’Albion', 'Lire 10 chapitres de contes anglais.', 'study', 'rare', 'englishChapters', 10, 'en'),
  a('zh-bosses-8', '戈', 'Stratège des Royaumes', 'Vaincre 8 gardiens chinois.', 'adventure', 'rare', 'chineseBosses', 8, 'zh'),
  a('zh-bosses-24', '秦', 'Unificateur·rice des Royaumes', 'Vaincre 24 gardiens chinois.', 'adventure', 'epic', 'chineseBosses', 24, 'zh'),
  a('hsk-passed', '过', 'HSK en poche', 'Valider un examen blanc du HSK.', 'adventure', 'epic', 'hskPassed', 1, 'zh'),
  a('zh-tales-10', '书', 'Conteur·se de l’Empire du Milieu', 'Lire 10 chapitres de contes chinois.', 'study', 'rare', 'chineseChapters', 10, 'zh'),
  a('es-bosses-8', '♜', 'Chevalier·ère errant·e', 'Vaincre 8 gardiens espagnols.', 'adventure', 'rare', 'spanishBosses', 8, 'es'),
  a('es-bosses-24', '♚', 'Légende de la Manche', 'Vaincre 24 gardiens espagnols.', 'adventure', 'epic', 'spanishBosses', 24, 'es'),
  a('dele-passed', 'Ñ', 'DELE en poche', 'Valider un examen blanc du DELE.', 'adventure', 'epic', 'delePassed', 1, 'es'),
  a('es-tales-10', '✍', 'Conteur·se de la Péninsule', 'Lire 10 chapitres de contes espagnols.', 'study', 'rare', 'spanishChapters', 10, 'es'),
  a('de-bosses-8', '♞', 'Compagnon·ne des Grimm', 'Vaincre 8 gardiens allemands.', 'adventure', 'rare', 'germanBosses', 8, 'de'),
  a('de-bosses-24', '♛', 'Légende de la Route des contes', 'Vaincre 24 gardiens allemands.', 'adventure', 'epic', 'germanBosses', 24, 'de'),
  a('goethe-passed', 'ß', 'Goethe-Zertifikat en poche', 'Valider un examen blanc du Goethe-Zertifikat.', 'adventure', 'epic', 'goethePassed', 1, 'de'),
  a('de-tales-10', '❦', 'Conteur·se de la Forêt', 'Lire 10 chapitres de contes allemands.', 'study', 'rare', 'germanChapters', 10, 'de'),
  // Jeux et collection
  a('games-10', '遊', 'Joueur·se', 'Jouer 10 parties de mini-jeux.', 'play', 'common', 'gamesPlayed', 10),
  a('game-score-20', '速', 'Réflexes éclair', 'Marquer 20 points dans une partie de mini-jeu.', 'play', 'rare', 'bestGameScore', 20),
  a('first-item', '宝', 'Collectionneur', 'Obtenir un premier objet pour ton personnage.', 'play', 'common', 'itemsCollected', 1),
  a('five-items', '蔵', 'Garde-robe garnie', 'Obtenir 5 objets pour ton personnage.', 'play', 'rare', 'itemsCollected', 5),
];

export const ACHIEVEMENT_BY_SLUG = new Map(ACHIEVEMENTS.map((x) => [x.slug, x]));

export interface AchievementProgress {
  def: AchievementDef;
  value: number;
  unlocked: boolean;
}

/**
 * Progression de chaque succès (valeur plafonnée à la cible). Avec une langue, les succès propres
 * à l'autre langue sont cachés, sauf s'ils ont déjà été débloqués.
 */
export function achievementProgress(stats: AchievementStats, unlocked: Iterable<string>, language?: 'ja' | 'ko' | 'en' | 'zh' | 'es' | 'de'): AchievementProgress[] {
  const done = new Set(unlocked);
  return ACHIEVEMENTS.filter((def) => !language || !def.language || def.language === language || done.has(def.slug)).map((def) => {
    const raw = Math.max(0, Math.floor(stats[def.metric] ?? 0));
    const isUnlocked = done.has(def.slug) || raw >= def.target;
    return { def, value: isUnlocked ? def.target : Math.min(raw, def.target), unlocked: isUnlocked };
  });
}

/** Succès nouvellement atteints (pas encore enregistrés), dans l'ordre du catalogue. */
export function newlyUnlocked(stats: AchievementStats, alreadyUnlocked: Iterable<string>): AchievementDef[] {
  const done = new Set(alreadyUnlocked);
  return ACHIEVEMENTS.filter((def) => !done.has(def.slug) && (stats[def.metric] ?? 0) >= def.target);
}

/** Récompense totale d'un lot de succès. */
export function achievementReward(defs: AchievementDef[]): { coins: number; xp: number } {
  return defs.reduce((r, d) => ({ coins: r.coins + ACHIEVEMENT_COINS[d.rarity], xp: r.xp + ACHIEVEMENT_XP[d.rarity] }), { coins: 0, xp: 0 });
}

/** Plus longue suite de jours consécutifs parmi des clés « AAAA-MM-JJ ». */
export function longestStreak(dateKeys: Iterable<string>): number {
  const set = new Set(dateKeys);
  let best = 0;
  for (const k of set) {
    if (set.has(addDays(k, -1))) continue; // pas le début d'une suite
    let n = 1;
    let cur = k;
    while (set.has((cur = addDays(cur, 1)))) n++;
    best = Math.max(best, n);
  }
  return best;
}

export const EMPTY_ACHIEVEMENT_STATS: AchievementStats = {
  lessonsCompleted: 0, perfectLessons: 0, bestStreak: 0, correctAnswers: 0, reviewsDone: 0, bestCombo: 0,
  masteredItems: 0, masteredKanji: 0, bossesDefeated: 0, examsTaken: 0, examsPassed: 0, gamesPlayed: 0,
  bestGameScore: 0, itemsCollected: 0, placementDone: 0, masteredKana: 0, japaneseBosses: 0, jlptPassed: 0, japaneseChapters: 0, masteredHangul: 0, koreanBosses: 0, topikPassed: 0, koreanChapters: 0,
  englishBosses: 0, toeicPassed: 0, englishChapters: 0, chineseBosses: 0, hskPassed: 0, chineseChapters: 0,
  spanishBosses: 0, delePassed: 0, spanishChapters: 0,
  germanBosses: 0, goethePassed: 0, germanChapters: 0,
};
