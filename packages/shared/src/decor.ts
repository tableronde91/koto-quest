/**
 * Glyphes décoratifs (tampons, pictos du menu, médailles) selon la langue étudiée.
 * Un apprenant de coréen, d'anglais, de chinois ou d'espagnol ne doit jamais voir de japonais dans l'interface :
 * chaque tampon existe en japonais, en coréen (hangeul), en anglais (mot ou symbole), en chinois simplifié et en espagnol.
 */
import type { StudyLanguage } from './languages';

type Four = readonly [ja: string, ko: string, en: string, zh: string, es: string];

const DECOR = {
  // Correction d'une réponse
  correct: ['正', '정답', '✓', '对', '✓'],
  wrong: ['惜', '아차', '✗', '错', '✗'],
  // Fin de leçon
  perfect: ['満点', '만점', '100%', '满分', '100%'],
  done: ['完了', '완료', 'Done', '完成', '¡Hecho!'],
  // Révisions
  review: ['復', '복', '↺', '复', '↺'],
  reviewStamp: ['復習', '복습', 'Review', '复习', 'Repaso'],
  learn: ['学', '학', 'Aa', '学', 'Ñ'],
  // Lecture
  read: ['読', '읽', 'Aa', '读', 'Aa'],
  readRetry: ['頑', '힘내', 'Go!', '加油', '¡Ánimo!'],
  // Caractères et expressions
  practice: ['練習', '연습', 'Practice', '练习', 'Práctica'],
  empty: ['空', '빈', '—', '空', '—'],
  talk: ['会話', '회화', 'Talk', '会话', 'Habla'],
  phrases: ['話', '말', '“”', '话', '«»'],
  // Examens et atelier
  pass: ['合格', '합격', 'Pass', '合格', 'Apto'],
  mock: ['模', '모', 'M', '模', 'M'],
  // Combats
  victory: ['勝利', '승리', 'Victory', '胜利', '¡Victoria!'],
  defeat: ['敗北', '패배', 'Defeat', '失败', 'Derrota'],
  win: ['勝', '승', 'W', '胜', 'V'],
  loss: ['負', '패', 'L', '负', 'D'],
  draw: ['分', '무', '=', '平', '='],
  start: ['始め!', '시작!', 'Go!', '开始！', '¡Vamos!'],
  fight: ['戦', '전', '⚔', '战', '⚔'],
  duel: ['闘', '투', '⚔', '斗', '⚔'],
  friend: ['友', '친', '♥', '友', '♥'],
  training: ['浪', '수', '◎', '练', '◎'],
  // Parcours
  locked: ['錠', '잠', '⋯', '锁', '⋯'],
  open: ['道', '길', '▶', '路', '▶'],
  questDone: ['✓', '✓', '✓', '✓', '✓'],
  completed: ['済', '완', '✓', '毕', '✓'],
  questTodo: ['·', '·', '·', '·', '·'],
  // Profil et progrès
  me: ['人', '나', 'Me', '人', 'Yo'],
  adventure: ['冒険', '모험', 'Quest', '冒险', 'Aventura'],
  skills: ['技', '기', '✦', '技', '✦'],
  garden: ['庭', '뜰', '✿', '园', '✿'],
  log: ['暦', '력', '✎', '历', '✎'],
  guardians: ['勝', '승', '⚔', '胜', '⚔'],
  award: ['賞', '상', '★', '奖', '★'],
  // Menus de l'appli mobile
  home: ['家', '집', '⌂', '家', '⌂'],
  island: ['島', '섬', '⛵', '岛', '⛵'],
  play: ['遊', '놀', '♟', '玩', '♟'],
  settings: ['設', '설', '⚙', '设', '⚙'],
  character: ['衣', '옷', '☺', '衣', '☺'],
  exam: ['試', '시', 'T', '考', 'E'],
  mockExam: ['模試', '모의', 'Mock', '模拟', 'Simulacro'],
  placement: ['診', '진', '?', '测', '?'],
  inProgress: ['進', '진', '…', '进', '…'],
  // Mini-jeux
  speed: ['走', '빨', '⚡', '快', '⚡'],
  listening: ['耳', '귀', '♪', '听', '♪'],
} satisfies Record<string, Four>;

export type DecorKey = keyof typeof DECOR;
const INDEX: Record<StudyLanguage, 0 | 1 | 2 | 3 | 4> = { ja: 0, ko: 1, en: 2, zh: 3, es: 4 };

/** Glyphe décoratif dans la langue étudiée. */
export function decor(key: DecorKey, lang: StudyLanguage = 'ja'): string {
  return DECOR[key][INDEX[lang]];
}

/** Médailles communes à toutes les langues : glyphe adapté à la langue étudiée (les médailles propres à une langue gardent le leur). */
const ACHIEVEMENT_GLYPHS: Record<string, Four> = {
  'first-lesson': ['始', '시', '1', '始', '1'],
  'ten-lessons': ['学', '학', '10', '学', '10'],
  'all-n5-lessons': ['修', '수', '25', '修', '25'],
  'first-perfect': ['満', '만', '✓', '满', '✓'],
  'ten-perfect': ['極', '극', '★', '极', '★'],
  'hundred-correct': ['百', '백', '100', '百', '100'],
  'thousand-correct': ['千', '천', '1k', '千', '1k'],
  'combo-10': ['連', '연', '×10', '连', '×10'],
  'combo-30': ['雷', '뢰', '×30', '雷', '×30'],
  'streak-3': ['火', '불', '3', '火', '3'],
  'streak-7': ['週', '주', '7', '周', '7'],
  'streak-30': ['月', '월', '30', '月', '30'],
  'reviews-50': ['復', '복', '↺', '复', '↺'],
  'reviews-500': ['憶', '억', '∞', '忆', '∞'],
  'mastered-25': ['芽', '싹', '❀', '芽', '❀'],
  'mastered-100': ['木', '목', '♣', '木', '♣'],
  'mastered-300': ['森', '숲', '♠', '森', '♠'],
  'first-boss': ['勝', '승', '⚔', '胜', '⚔'],
  'four-bosses': ['武', '무', '♜', '武', '♜'],
  'all-bosses': ['王', '왕', '♔', '王', '♔'],
  placement: ['診', '진', '?', '诊', '?'],
  'first-exam': ['試', '시', '✎', '试', '✎'],
  'exam-passed': ['合', '합', '✓', '合', '✓'],
  'games-10': ['遊', '놀', '♟', '游', '♟'],
  'game-score-20': ['速', '속', '⚡', '速', '⚡'],
  'first-item': ['宝', '보', '◆', '宝', '◆'],
  'five-items': ['蔵', '장', '▣', '藏', '▣'],
};

export function achievementGlyph(slug: string, glyph: string, lang: StudyLanguage = 'ja'): string {
  return ACHIEVEMENT_GLYPHS[slug]?.[INDEX[lang]] ?? glyph;
}

/** Rangs des duels : idéogramme japonais pour le japonais, équivalent pour les autres langues. */
const DUEL_TIER_GLYPHS: Record<string, Four> = {
  ashigaru: ['足軽', '병졸', 'I', '兵', 'I'],
  samurai: ['侍', '무사', 'II', '士', 'II'],
  kengo: ['剣豪', '검객', 'III', '剑客', 'III'],
  daimyo: ['大名', '영주', 'IV', '诸侯', 'IV'],
  shogun: ['将軍', '장군', 'V', '将军', 'V'],
  tenka: ['天下人', '천하인', 'VI', '霸主', 'VI'],
};

export function duelTierGlyph(tierId: string, jp: string, lang: StudyLanguage = 'ja'): string {
  return DUEL_TIER_GLYPHS[tierId]?.[INDEX[lang]] ?? jp;
}

/** Noms des rangs de duel hors japonais (le japonais garde Ashigaru, Samouraï, Kengō…). Libellés français, traduits à l'affichage. */
export const DUEL_TIER_NAMES: Record<string, { ja: string; other: string }> = {
  ashigaru: { ja: 'Ashigaru', other: 'Fantassin' },
  samurai: { ja: 'Samouraï', other: 'Guerrier' },
  kengo: { ja: 'Kengō', other: 'Fine lame' },
  daimyo: { ja: 'Daimyō', other: 'Seigneur' },
  shogun: { ja: 'Shōgun', other: 'Général' },
  tenka: { ja: 'Tenkabito', other: 'Souverain' },
};
