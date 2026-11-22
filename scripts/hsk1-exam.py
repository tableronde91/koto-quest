# Banque de questions de l'examen blanc HSK 1 (content/exams/hsk1.json), au format de l'épreuve officielle (HSK 2.0) :
# 听力 (écoute, 20 questions en quatre parties) et 阅读 (lecture, 20 questions en quatre parties), notation sur 200, réussite à 120.
# Comme sur la copie du HSK 1, le pinyin accompagne le texte ; les images sont remplacées par des pictogrammes.
# Dans chaque question, le premier choix est la bonne réponse (l'ordre est mélangé à chaque examen).
# Usage : python3 scripts/hsk1-exam.py
import json, os
ROOT = os.path.join(os.path.dirname(__file__), '..')
WHO = {'N': 'Narrateur', 'M': 'Homme', 'F': 'Femme'}
YES, NO = '✓ 对', '✗ 错'

def LQ(audio, choices, text=None):
    lines = [l.strip() for l in audio.strip().split('\n') if l.strip()]
    for l in lines:
        assert l[1] == '|' and l[0] in WHO, l
    q = {'audio': '\n'.join(lines), 'choices': choices, 'answer': choices[0],
         'explanation': 'Transcription : ' + ' / '.join(f"{WHO[l[0]]} : {l[2:]}" for l in lines)}
    if text:
        q['text'] = text
    return q

def JUDGE(audio, picture, true):
    """Écoute + image : la phrase correspond-elle à l'image ?"""
    return LQ(audio, [YES, NO] if true else [NO, YES], picture)

def RQ(choices, jp=None, text=None, expl=None):
    q = {'choices': choices, 'answer': choices[0], 'explanation': expl or f'Réponse : {choices[0]}'}
    if jp: q['jp'] = jp
    if text: q['text'] = text
    return q

def PART(id, section, jpTitle, title, prompt, count, questions, listening=False):
    for q in questions:
        assert 2 <= len(set(q['choices'])) == len(q['choices']) <= 4, q
    assert len(questions) >= count, id
    p = {'id': id, 'section': section, 'jpTitle': jpTitle, 'title': title, 'prompt': prompt, 'count': count, 'questions': questions}
    if listening:
        p['listening'] = True
    return p

# ═════════════════════════ 听力 ═════════════════════════
L1 = PART('l-judge', 'listening', '听力 第一部分（1～5）', 'Image : vrai ou faux', '听录音，判断对错。', 5, [
  JUDGE('N|苹果', '🍎', True),
  JUDGE('N|猫', '🐶', False),
  JUDGE('N|喝茶', '🍵', True),
  JUDGE('N|飞机', '🚆', False),
  JUDGE('N|看书', '📖', True),
  JUDGE('N|下雨', '☀️', False),
  JUDGE('N|打电话', '📞', True),
  JUDGE('N|睡觉', '✍️', False),
], listening=True)

L2 = PART('l-picture', 'listening', '听力 第二部分（6～10）', 'Choisir l’image', '听录音，选择对应的图片。', 5, [
  LQ('N|我喜欢喝水。', ['💧', '🍵', '🍎']),
  LQ('N|他坐出租车去学校。', ['🚕', '✈️', '🚆']),
  LQ('N|我女儿很喜欢猫。', ['🐱', '🐶', '🐟']),
  LQ('N|今天太热了！', ['🔥', '❄️', '☔']),
  LQ('N|我在医院工作，我是医生。', ['🏥', '🏫', '🛒']),
  LQ('N|妈妈在看电视。', ['📺', '📖', '📞']),
  LQ('N|这是我的椅子。', ['🪑', '🍵', '👕']),
], listening=True)

L3 = PART('l-dialogue', 'listening', '听力 第三部分（11～15）', 'Dialogue et image', '听对话，选择对应的图片。', 5, [
  LQ('M|你想吃什么？\nF|我想吃米饭。', ['🍚', '🍎', '🍵', '💧']),
  LQ('F|你去哪儿？\nM|我去火车站。', ['🚉', '🏥', '🏫', '🛒']),
  LQ('M|这件衣服怎么样？\nF|很漂亮！', ['👕', '🪑', '📖', '📺']),
  LQ('F|明天天气怎么样？\nM|明天会下雨。', ['☔', '☀️', '🔥', '❄️']),
  LQ('M|你在做什么？\nF|我在写字。', ['✍️', '😴', '📞', '🍵']),
  LQ('F|你家有狗吗？\nM|有，我家有两个狗。', ['🐶', '🐱', '🐟', '🍎']),
  LQ('M|你会开车吗？\nF|会，我每天开车去工作。', ['🚗', '✈️', '🚆', '🚕']),
], listening=True)

L4 = PART('l-question', 'listening', '听力 第四部分（16～20）', 'Phrase et question', '听句子和问题，选择正确答案。', 5, [
  LQ('M|我叫王明，我是老师，在学校工作。\nN|问：王明做什么工作？', ['老师 lǎoshī', '医生 yīshēng', '学生 xuésheng']),
  LQ('F|今天是星期三，明天我去北京。\nN|问：她星期几去北京？', ['星期四 xīngqīsì', '星期三 xīngqīsān', '星期二 xīngqī’èr']),
  LQ('M|这个杯子二十块，那个三十块。\nN|问：那个杯子多少钱？', ['三十块 sānshí kuài', '二十块 èrshí kuài', '十块 shí kuài']),
  LQ('F|我女儿七岁，儿子五岁。\nN|问：她儿子几岁？', ['五岁 wǔ suì', '七岁 qī suì', '十二岁 shí’èr suì']),
  LQ('M|下午三点我们在饭馆前面见。\nN|问：他们几点见？', ['三点 sān diǎn', '十三点 shísān diǎn', '四点 sì diǎn']),
  LQ('F|我不喜欢喝茶，我喜欢喝水。\nN|问：她喜欢喝什么？', ['水 shuǐ', '茶 chá', '米饭 mǐfàn']),
  LQ('M|昨天下雨了，我没去商店。\nN|问：他昨天去商店了吗？', ['没去 méi qù', '去了 qù le', '明天去 míngtiān qù']),
], listening=True)

# ═════════════════════════ 阅读 ═════════════════════════
R1 = PART('r-judge', 'reading', '阅读 第一部分（21～25）', 'Image et mot', '看图片和词语，判断对错。', 5, [
  RQ([YES, NO], '🐱', '猫 māo'),
  RQ([NO, YES], '🍎', '茶 chá'),
  RQ([YES, NO], '✈️', '飞机 fēijī'),
  RQ([NO, YES], '📺', '书 shū'),
  RQ([YES, NO], '🏥', '医院 yīyuàn'),
  RQ([NO, YES], '❄️', '热 rè'),
  RQ([YES, NO], '🪑', '椅子 yǐzi'),
])

R2 = PART('r-picture', 'reading', '阅读 第二部分（26～30）', 'Phrase et image', '选择与句子对应的图片。', 5, [
  RQ(['🚕', '🚆', '✈️'], '我坐出租车回家。', 'Wǒ zuò chūzūchē huí jiā.'),
  RQ(['🍚', '🍎', '🍵'], '中午我们吃米饭。', 'Zhōngwǔ wǒmen chī mǐfàn.'),
  RQ(['☔', '☀️', '❄️'], '今天下雨了。', 'Jīntiān xià yǔ le.'),
  RQ(['😴', '✍️', '📞'], '我儿子在睡觉。', 'Wǒ érzi zài shuìjiào.'),
  RQ(['🎬', '📖', '📺'], '我们去看电影吧。', 'Wǒmen qù kàn diànyǐng ba.'),
  RQ(['🛒', '🏫', '🏥'], '妈妈在商店买东西。', 'Māma zài shāngdiàn mǎi dōngxi.'),
])

R3 = PART('r-answer', 'reading', '阅读 第三部分（31～35）', 'Question et réponse', '选择正确的回答。', 5, [
  RQ(['我叫李月。', '我是中国人。', '我十八岁。', '我在家。'], '你叫什么名字？', 'Nǐ jiào shénme míngzi?'),
  RQ(['我是法国人。', '我是老师。', '我叫大卫。', '我去北京。'], '你是哪国人？', 'Nǐ shì nǎ guó rén?'),
  RQ(['二十五块。', '五个。', '三点。', '星期五。'], '这个苹果多少钱？', 'Zhè ge píngguǒ duōshao qián?'),
  RQ(['不客气。', '没关系。', '再见。', '你好。'], '谢谢你！', 'Xièxie nǐ!'),
  RQ(['在桌子上。', '是我的。', '很好。', '明天。'], '我的书在哪儿？', 'Wǒ de shū zài nǎr?'),
  RQ(['我家有四口人。', '我家很大。', '我爱我的家。', '我在家。'], '你家有几口人？', 'Nǐ jiā yǒu jǐ kǒu rén?'),
  RQ(['会，我会说一点儿。', '是，我是汉语。', '有，我有汉语。', '在，我在汉语。'], '你会说汉语吗？', 'Nǐ huì shuō Hànyǔ ma?'),
  RQ(['八点。', '八号。', '八岁。', '八个。'], '现在几点？', 'Xiànzài jǐ diǎn?'),
])

R4 = PART('r-blank', 'reading', '阅读 第四部分（36～40）', 'Choisir le mot', '选词填空。', 5, [
  RQ(['岁 suì', '号 hào', '个 gè', '块 kuài'], '我女儿今年三＿＿。', 'Wǒ nǚ’ér jīnnián sān ＿＿.'),
  RQ(['坐 zuò', '吃 chī', '叫 jiào', '有 yǒu'], '我们＿＿飞机去北京。', 'Wǒmen ＿＿ fēijī qù Běijīng.'),
  RQ(['喝 hē', '看 kàn', '写 xiě', '读 dú'], '你想＿＿什么？茶还是水？', 'Nǐ xiǎng ＿＿ shénme? Chá háishi shuǐ?'),
  RQ(['没 méi', '不 bù', '很 hěn', '太 tài'], '我＿＿有猫，我有一个狗。', 'Wǒ ＿＿ yǒu māo, wǒ yǒu yí ge gǒu.'),
  RQ(['在 zài', '是 shì', '去 qù', '叫 jiào'], '王老师＿＿学校工作。', 'Wáng lǎoshī ＿＿ xuéxiào gōngzuò.'),
  RQ(['认识 rènshi', '喜欢 xǐhuan', '高兴 gāoxìng', '请 qǐng'], '我＿＿他，他是我的同学。', 'Wǒ ＿＿ tā, tā shì wǒ de tóngxué.'),
  RQ(['怎么样 zěnmeyàng', '什么 shénme', '哪儿 nǎr', '几 jǐ'], '今天天气＿＿？', 'Jīntiān tiānqì ＿＿?'),
])

PARTS = [L1, L2, L3, L4, R1, R2, R3, R4]
lis = sum(p['count'] for p in PARTS if p['section'] == 'listening')
rea = sum(p['count'] for p in PARTS if p['section'] == 'reading')
assert (lis, rea) == (20, 20), (lis, rea)
bank = {
  'slug': 'hsk1',
  'level': 'HSK1',
  'contentVersion': '2026.11.22',
  'notice': 'Questions rédigées par Koto Quest au format de l’examen officiel du HSK 1 (HSK 2.0 : types d’épreuves, consignes en chinois, pinyin, notation sur 200). Les images sont remplacées par des pictogrammes. Ce ne sont pas des questions officielles.',
  'parts': PARTS,
}
json.dump(bank, open(os.path.join(ROOT, 'content/exams/hsk1.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
EN = {
  bank['notice']: 'Questions written by Koto Quest in the format of the official HSK 1 exam (HSK 2.0: question types, instructions in Chinese, pinyin, scoring out of 200). Pictures are replaced by pictograms. They are not official questions.',
  'Image : vrai ou faux': 'Picture: true or false', 'Choisir l’image': 'Choosing the picture', 'Dialogue et image': 'Dialogue and picture',
  'Phrase et question': 'Sentence and question', 'Image et mot': 'Picture and word', 'Phrase et image': 'Sentence and picture',
  'Question et réponse': 'Question and answer', 'Choisir le mot': 'Choosing the word',
}
P_DICT = os.path.join(ROOT, 'content/i18n/en/content.json')
d = json.load(open(P_DICT, encoding='utf-8'))
for k, v in EN.items():
    if k in d and d[k] != v:
        raise SystemExit(f'traduction existante différente : {k} → {d[k]} / {v}')
d.update(EN)
json.dump(d, open(P_DICT, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(f"HSK 1 : {sum(len(p['questions']) for p in PARTS)} questions en banque ; examen de {lis} + {rea} questions")
