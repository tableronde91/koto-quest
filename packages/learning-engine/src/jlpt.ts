import { AuthoredExercise, EngineItem, Question, authoredToQuestion, generateQuestion } from './exercises';
import { Rng, shuffle } from './random';

/**
 * Exercices au format du JLPT, générés à partir des notions apprises :
 *  - 漢字読み : lire un mot en kanji, avec les pièges classiques de l'examen
 *    (voyelle longue, son voisé/non voisé, petit っ, ゃゅょ) ;
 *  - 表記 : écrire en kanji un mot donné en hiragana, avec des kanji sosies et des okurigana fautifs ;
 *  - 文の組み立て : la case ★ d'une phrase à reconstituer ;
 *  - consignes en japonais, comme sur la copie.
 */

export const JLPT_PROMPTS = {
  reading: '＿＿の ことばは ひらがなで どう かきますか。',
  writing: '＿＿の ことばは どう かきますか。',
  grammar: '（　）に 何を 入れますか。',
  star: '★に 入る ものは どれですか。',
  listening: 'はなしを きいて、ただしい こたえを えらんで ください。',
} as const;

const KANJI_RE = /[一-龯々]/;
export const hasKanji = (s: string) => KANJI_RE.test(s);

// ─────────── Pièges de lecture ───────────

const VOICE: Record<string, string> = {
  か: 'が', き: 'ぎ', く: 'ぐ', け: 'げ', こ: 'ご', さ: 'ざ', し: 'じ', す: 'ず', せ: 'ぜ', そ: 'ぞ',
  た: 'だ', ち: 'ぢ', つ: 'づ', て: 'で', と: 'ど', は: 'ば', ひ: 'び', ふ: 'ぶ', へ: 'べ', ほ: 'ぼ',
};
const UNVOICE: Record<string, string> = Object.fromEntries(Object.entries(VOICE).map(([a, b]) => [b, a]));
const SMALL: Record<string, string> = { ゃ: 'や', ゅ: 'ゆ', ょ: 'よ' };
const O_ROW = 'おこそとのほもよろごぞどぼぽょ';
const E_ROW = 'えけせてねへめれげぜでべぺ';
const STOP_BEFORE = 'かきくけこさしすせそたちつてとぱぴぷぺぽ';

/** Lectures fautives plausibles (une seule modification), comme les distracteurs du JLPT. */
export function readingTraps(reading: string): string[] {
  const chars = [...reading];
  const out = new Set<string>();
  const put = (arr: string[]) => {
    const s = arr.join('');
    if (s && s !== reading) out.add(s);
  };
  chars.forEach((c, i) => {
    // Son voisé ↔ non voisé (て/で, か/が…)
    if (VOICE[c]) put([...chars.slice(0, i), VOICE[c], ...chars.slice(i + 1)]);
    if (UNVOICE[c]) put([...chars.slice(0, i), UNVOICE[c], ...chars.slice(i + 1)]);
    // Voyelle longue en trop ou en moins (せんせい / せんせ, こうこう / ここう)
    const next = chars[i + 1];
    if ((O_ROW.includes(c) && next === 'う') || (E_ROW.includes(c) && next === 'い')) put([...chars.slice(0, i + 1), ...chars.slice(i + 2)]);
    if ((O_ROW.includes(c) && next !== 'う') || (E_ROW.includes(c) && next !== 'い' && i === chars.length - 1)) put([...chars.slice(0, i + 1), O_ROW.includes(c) ? 'う' : 'い', ...chars.slice(i + 1)]);
    // Petit っ en trop ou en moins (がっこう / がこう)
    if (c === 'っ') put([...chars.slice(0, i), ...chars.slice(i + 1)]);
    else if (i > 0 && STOP_BEFORE.includes(c) && chars[i - 1] !== 'っ' && chars[i - 1] !== 'ん') put([...chars.slice(0, i), 'っ', ...chars.slice(i)]);
    // ゃゅょ en grand (しゃ / しや)
    if (SMALL[c]) put([...chars.slice(0, i), SMALL[c], ...chars.slice(i + 1)]);
  });
  return [...out];
}

// ─────────── Pièges d'écriture ───────────

/** Kanji qui se ressemblent (niveau N5) : ce sont les pièges de l'épreuve 表記. */
export const LOOKALIKES: Record<string, string[]> = {
  休: ['体', '木'], 体: ['休', '本'], 本: ['木', '体'], 木: ['本', '休'], 人: ['入', '八'], 入: ['人', '八'], 八: ['人', '入'],
  大: ['太', '犬', '天'], 太: ['大', '犬'], 犬: ['大', '太'], 天: ['夫', '大'], 日: ['目', '白', '曰'], 目: ['日', '自', '月'], 白: ['日', '百', '自'],
  百: ['白', '首'], 右: ['石', '左'], 左: ['右', '在'], 石: ['右', '古'], 千: ['干', '午'], 午: ['牛', '千'], 牛: ['午', '生'],
  土: ['士', '上'], 上: ['土', '止'], 下: ['卞', '不'], 王: ['玉', '主'], 玉: ['王', '主'], 手: ['毛', '午'], 毛: ['手', '尾'],
  間: ['問', '聞', '門'], 聞: ['間', '問', '開'], 門: ['間', '問'], 開: ['閉', '間'], 読: ['話', '語', '続'], 話: ['語', '読', '詰'], 語: ['話', '読', '誤'],
  買: ['貝', '員', '売'], 売: ['買', '読'], 見: ['貝', '兄'], 貝: ['見', '員'], 外: ['夕', '多'], 夕: ['外', '多'], 名: ['各', '多'],
  今: ['会', '令'], 会: ['今', '合'], 社: ['仕', '杜'], 気: ['汽', '風'], 電: ['雷', '雲', '雪'], 雨: ['両', '雪'], 書: ['晝', '昼', '者'],
  北: ['比', '化', '兆'], 学: ['字', '覚'], 字: ['学', '子'], 子: ['了', '字'], 校: ['交', '絞'], 店: ['庄', '広', '后'], 広: ['店', '応'],
  後: ['役', '復', '彼'], 前: ['煎', '首'], 先: ['洗', '牛'], 生: ['牛', '性', '主'], 東: ['車', '東', '束'], 車: ['東', '連', '軍'], 西: ['酉', '四'],
  南: ['商', '内'], 四: ['西', '匹'], 小: ['少', '心'], 少: ['小', '沙'], 新: ['親', '近'], 親: ['新', '視'], 長: ['張', '帳'], 高: ['髙', '喬'],
  安: ['女', '案'], 女: ['安', '好'], 男: ['田', '思'], 田: ['由', '男', '甲'], 円: ['丹', '内'], 万: ['方', '力'], 方: ['万', '放'],
  年: ['午', '牛'], 時: ['特', '持', '詩'], 半: ['伴', '羊'], 分: ['今', '公'], 来: ['米', '未'], 毎: ['海', '梅'], 週: ['遇', '周', '過'],
  朝: ['潮', '期'], 晩: ['勉', '晴'], 飲: ['飯', '欲'], 食: ['良', '飲'], 走: ['足', '赴', '起'], 足: ['走', '是'], 起: ['走', '超'],
  行: ['衍', '往'], 帰: ['掃', '婦'], 耳: ['目', '取'], 口: ['日', '中'], 川: ['州', '三'], 山: ['出', '凸'], 出: ['山', '凸'],
  友: ['反', '有', '支'], 有: ['友', '右'], 国: ['困', '固', '因'], 何: ['可', '河'], 母: ['毎', '舟'], 父: ['交', '文'],
  銀: ['鉄', '鋼'], 院: ['阮', '完'], 病: ['痛', '疲'], 館: ['官', '飯'], 近: ['新', '斤'], 遠: ['園', '達'], 明: ['朋', '昭'], 暗: ['暑', '晴'],
};

/** Okurigana fautifs : 新しい → 新い / 新らしい, 休み → 休すみ. */
function okuriganaTraps(front: string, reading: string): string[] {
  const m = /^(.*[一-龯々])([ぁ-ゖ]+)$/.exec(front);
  if (!m) return [];
  const [, stem, okuri] = m;
  if (!reading.endsWith(okuri)) return [];
  const stemReading = reading.slice(0, reading.length - okuri.length);
  const out: string[] = [];
  if (okuri.length > 1) out.push(stem + okuri.slice(1)); // une kana de moins
  if (stemReading.length > 1) out.push(stem + stemReading.slice(-1) + okuri); // une kana de trop
  return out;
}

/** Graphies fautives plausibles d'un mot en kanji. */
export function writingTraps(front: string, reading: string): string[] {
  const out = new Set<string>();
  [...front].forEach((c, i) => {
    for (const alt of LOOKALIKES[c] ?? []) {
      if (alt === c) continue;
      out.add([...front].map((x, k) => (k === i ? alt : x)).join(''));
    }
  });
  okuriganaTraps(front, reading).forEach((t) => out.add(t));
  out.delete(front);
  return [...out];
}

// ─────────── Questions ───────────

const underline = (sentence: string, word: string) => (sentence.includes(word) ? sentence.replace(word, `{{${word}}}`) : `{{${word}}}`);

/** 漢字読み : lecture d'un mot (dans une phrase d'exemple si elle existe). */
export function jlptReadingQuestion(item: EngineItem, pool: readonly EngineItem[], rng: Rng, example?: string): Question | null {
  // Des mots seulement : un kanji isolé a plusieurs lectures selon le mot (日 : ひ, に, にち…).
  if (!item.reading || !hasKanji(item.front) || item.kind !== 'vocabulary') return null;
  let traps = shuffle(readingTraps(item.reading), rng).slice(0, 3);
  if (traps.length < 3) {
    const others = shuffle(pool.filter((p) => p.id !== item.id && p.reading && p.reading !== item.reading && hasKanji(p.front)), rng).map((p) => p.reading!);
    traps = [...new Set([...traps, ...others])].filter((t) => t !== item.reading).slice(0, 3);
  }
  if (traps.length < 2) return null;
  return {
    type: 'jlpt_reading',
    itemId: item.id,
    prompt: JLPT_PROMPTS.reading,
    display: { jp: underline(example ?? item.front, item.front), part: 'もんだい１　漢字読み' },
    choices: shuffle([item.reading, ...traps], rng),
    answer: item.reading,
    explanation: `「${item.front}」 se lit 「${item.reading}」 (${item.meaning}).`,
    answerAudio: example ?? item.reading,
    guessable: false,
  };
}

/** 表記 : écrire un mot en kanji (le mot est donné en hiragana). */
export function jlptWritingQuestion(item: EngineItem, pool: readonly EngineItem[], rng: Rng, example?: string): Question | null {
  if (!item.reading || !hasKanji(item.front) || item.kind !== 'vocabulary' || item.reading === item.front) return null;
  let traps = shuffle(writingTraps(item.front, item.reading), rng).slice(0, 3);
  if (traps.length < 3) {
    const others = shuffle(pool.filter((p) => p.id !== item.id && hasKanji(p.front) && p.kind === item.kind && [...p.front].length === [...item.front].length), rng).map((p) => p.front);
    traps = [...new Set([...traps, ...others])].filter((t) => t !== item.front).slice(0, 3);
  }
  if (traps.length < 2) return null;
  const sentence = example ? example.replace(item.front, item.reading) : item.reading;
  return {
    type: 'jlpt_writing',
    itemId: item.id,
    prompt: JLPT_PROMPTS.writing,
    display: { jp: underline(sentence, item.reading), part: 'もんだい２　表記' },
    choices: shuffle([item.front, ...traps], rng),
    answer: item.front,
    explanation: `「${item.reading}」 s'écrit 「${item.front}」 (${item.meaning}).`,
    answerAudio: example ?? item.reading,
    guessable: false,
  };
}

/** ★ : une phrase à reconstituer devient une question à choix (comme 文の組み立て). */
export function starQuestion(ex: AuthoredExercise, rng: Rng): Question | null {
  if (ex.type !== 'sentence_order' || !Array.isArray(ex.answer) || ex.answer.length < 3) return null;
  const order = ex.answer;
  const star = order.length >= 4 ? 2 : 1;
  const slots = order.map((_, i) => (i === star ? '★' : '＿＿')).join(' ');
  return {
    type: 'particle_choice',
    prompt: JLPT_PROMPTS.star,
    display: { jp: slots, text: ex.prompt.replace(/^Remets dans l'ordre\s*:\s*/, ''), part: 'もんだい２　文の組み立て' },
    choices: shuffle([...new Set(order)], rng),
    answer: order[star],
    explanation: `Ordre : ${order.join(' ')}. ${ex.explanation}`,
    answerAudio: order.join(''),
    guessable: false,
  };
}

/** Exercice de grammaire rédigé, présenté avec la consigne japonaise de l'examen. */
export function jlptGrammarQuestion(ex: AuthoredExercise, rng: Rng): Question | null {
  if (ex.type !== 'particle_choice' && ex.type !== 'fill_blank') return null;
  const q = authoredToQuestion(ex, rng);
  return { ...q, prompt: JLPT_PROMPTS.grammar, display: { ...q.display, reading: undefined, part: 'もんだい１　文法形式の判断' } };
}

/** Dialogue rédigé → écoute : le document est lu, on choisit la réplique. */
export function jlptListeningFromDialogue(ex: AuthoredExercise, rng: Rng): Question | null {
  if (ex.type !== 'dialogue_choice' || !ex.lines?.length) return null;
  const q = authoredToQuestion(ex, rng);
  const script = ex.lines.map((l, i) => `${i % 2 === 0 ? 'F' : 'M'}|${l.reading ?? l.jp}`).join('\n');
  return { ...q, type: 'listening_choice', prompt: JLPT_PROMPTS.listening, display: { text: 'なんと こたえますか。', part: 'もんだい４　即時応答' }, audio: script, answerAudio: undefined };
}

export type JlptDrillPart = 'kanji' | 'writing' | 'grammar' | 'star' | 'listening';

export const JLPT_DRILLS: Record<JlptDrillPart, { title: string; jpTitle: string; description: string }> = {
  kanji: { title: 'Lecture des kanji', jpTitle: '漢字読み', description: 'Lis le mot souligné. Attention aux pièges : voyelle longue, ten-ten, petit っ.' },
  writing: { title: 'Orthographe', jpTitle: '表記', description: 'Choisis la bonne écriture en kanji parmi des caractères qui se ressemblent.' },
  grammar: { title: 'Grammaire', jpTitle: '文法形式の判断', description: 'Complète la phrase avec la bonne particule ou forme, consigne en japonais.' },
  star: { title: 'Phrase à reconstituer', jpTitle: '文の組み立て', description: 'Trouve le morceau qui va dans la case ★.' },
  listening: { title: 'Écoute', jpTitle: '聴解', description: 'Écoute et réponds, sans texte à lire.' },
};

export const JLPT_DRILL_SIZE = 10;

/**
 * Série d'entraînement pour une épreuve, uniquement avec ce que l'utilisateur a déjà appris
 * (notions vues, exercices des leçons terminées).
 */
export function planJlptDrill(part: JlptDrillPart, learned: EngineItem[], authored: AuthoredExercise[], pool: readonly EngineItem[], rng: Rng, examples: Map<string, string> = new Map()): Question[] {
  const n = JLPT_DRILL_SIZE;
  const fromItems = (make: (it: EngineItem) => Question | null) => shuffle(learned, rng).map(make).filter((q): q is Question => !!q).slice(0, n);
  switch (part) {
    case 'kanji':
      return fromItems((it) => jlptReadingQuestion(it, pool, rng, examples.get(it.id)));
    case 'writing':
      return fromItems((it) => jlptWritingQuestion(it, pool, rng, examples.get(it.id)));
    case 'grammar':
      return shuffle(authored, rng).map((ex) => jlptGrammarQuestion(ex, rng)).filter((q): q is Question => !!q).slice(0, n);
    case 'star':
      return shuffle(authored, rng).map((ex) => starQuestion(ex, rng)).filter((q): q is Question => !!q).slice(0, n);
    case 'listening': {
      const dialogues = shuffle(authored, rng).map((ex) => jlptListeningFromDialogue(ex, rng)).filter((q): q is Question => !!q).slice(0, Math.ceil(n / 2));
      const words = shuffle(learned.filter((i) => i.kind === 'vocabulary'), rng)
        .map((it) => generateQuestion(it, pool, 'listening_choice', rng))
        .filter((q): q is Question => !!q)
        .slice(0, n - dialogues.length);
      return shuffle([...dialogues, ...words], rng);
    }
  }
}

/**
 * Exemple d'usage pour chaque notion : première phrase d'exemple (dans les leçons) qui contient le mot.
 * Sert à présenter les questions 漢字読み / 表記 dans une phrase, comme à l'examen.
 */
export function exampleIndex(items: readonly EngineItem[], sentences: readonly string[]): Map<string, string> {
  const out = new Map<string, string>();
  for (const it of items) {
    if (!hasKanji(it.front) || it.kind !== 'vocabulary') continue;
    const s = sentences.find((x) => x.includes(it.front) && [...x].length <= 30);
    if (s) out.set(it.id, s);
  }
  return out;
}
