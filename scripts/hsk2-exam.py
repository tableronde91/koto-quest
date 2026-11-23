# Banque de questions de l'examen blanc HSK 2 (content/exams/hsk2.json), au format de l'épreuve officielle (HSK 2.0) :
# 听力 (écoute, 35 questions en quatre parties) et 阅读 (lecture, 25 questions en quatre parties), 55 minutes,
# notation sur 200, réussite à 120. Le pinyin accompagne le texte ; les images sont remplacées par des pictogrammes.
# Dans chaque question, le premier choix est la bonne réponse (l'ordre est mélangé à chaque examen).
# Usage : python3 scripts/hsk2-exam.py
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
L1 = PART('l-judge', 'listening', '听力 第一部分（1～10）', 'Image : vrai ou faux', '听录音，判断对错。', 10, [
  JUDGE('N|我每天早上跑步。', '🏃', True),
  JUDGE('N|他正在游泳呢。', '⚽', False),
  JUDGE('N|外面下雪了，真冷啊！', '❄️', True),
  JUDGE('N|妈妈在洗衣服。', '🍳', False),
  JUDGE('N|这是我的新手表。', '⌚', True),
  JUDGE('N|哥哥喜欢打篮球。', '🏀', True),
  JUDGE('N|我生病了，在吃药。', '🎂', False),
  JUDGE('N|祝你生日快乐！', '🎂', True),
  JUDGE('N|我们坐公共汽车去吧。', '✈️', False),
  JUDGE('N|她在唱歌。', '🎤', True),
  JUDGE('N|桌子上有一个西瓜。', '🍉', True),
  JUDGE('N|爸爸在看报纸。', '📺', False),
], listening=True)

L2 = PART('l-dialogue-picture', 'listening', '听力 第二部分（11～20）', 'Dialogue et image', '听对话，选择对应的图片。', 10, [
  LQ('M|你怎么了？\nF|我眼睛不舒服，要去医院。', ['🏥', '🏫', '🏨', '🛒']),
  LQ('F|你想喝咖啡还是牛奶？\nM|牛奶，谢谢。', ['🥛', '☕', '🍵', '🍉']),
  LQ('M|这件衣服是什么颜色的？\nF|红色的，很漂亮。', ['🟥', '⬛', '⬜', '🟦']),
  LQ('F|明天天气怎么样？\nM|明天是晴天。', ['☀️', '☔', '❄️', '☁️']),
  LQ('M|你在找什么？\nF|我在找我的手机。', ['📱', '⌚', '📖', '✏️']),
  LQ('F|你喜欢什么运动？\nM|我最喜欢踢足球。', ['⚽', '🏀', '🏊', '🏃']),
  LQ('M|我们怎么去机场？\nF|坐出租车吧，快一点儿。', ['🚕', '🚌', '🚆', '🚲']),
  LQ('F|你妹妹在做什么？\nM|她在跳舞呢。', ['💃', '🎤', '😴', '✍️']),
  LQ('M|晚上吃什么？\nF|吃鱼吧，我买了一条大鱼。', ['🐟', '🍚', '🥚', '🍉']),
  LQ('F|请问，宾馆在哪儿？\nM|往前走，就在右边。', ['🏨', '🏥', '🏫', '🚉']),
  LQ('M|你考试准备得怎么样了？\nF|我正在看书呢。', ['📖', '📺', '🎬', '📞']),
  LQ('F|你送我什么生日礼物？\nM|一个新手表。', ['⌚', '📱', '👕', '🍉']),
], listening=True)

L3 = PART('l-dialogue-question', 'listening', '听力 第三部分（21～30）', 'Dialogue et question', '听对话，选择正确答案。', 10, [
  LQ('M|你家离公司远吗？\nF|不远，走路十分钟就到了。\nN|问：女的家离公司远吗？', ['不远 bù yuǎn', '很远 hěn yuǎn', '要一个小时 yào yí ge xiǎoshí']),
  LQ('F|你哥哥比你大几岁？\nM|他比我大三岁。\nN|问：谁比较大？', ['哥哥 gēge', '男的 nán de', '他们一样大 tāmen yíyàng dà']),
  LQ('M|你去过北京吗？\nF|没去过，我希望明年去。\nN|问：女的去过北京吗？', ['没去过 méi qùguo', '去过一次 qùguo yí cì', '去过两次 qùguo liǎng cì']),
  LQ('F|你为什么没来上课？\nM|因为我生病了。\nN|问：男的为什么没来？', ['生病了 shēngbìng le', '太忙了 tài máng le', '下雨了 xià yǔ le']),
  LQ('M|这个西瓜多少钱？\nF|三块钱一公斤，这个五公斤。\nN|问：这个西瓜多少钱？', ['十五块 shíwǔ kuài', '三块 sān kuài', '五块 wǔ kuài']),
  LQ('F|电影几点开始？\nM|七点半，我们快点儿走吧。\nN|问：电影什么时候开始？', ['七点半 qī diǎn bàn', '七点 qī diǎn', '八点半 bā diǎn bàn']),
  LQ('M|你汉语说得真好！\nF|哪里，我学了两年了。\nN|问：女的学了多长时间汉语？', ['两年 liǎng nián', '两个月 liǎng ge yuè', '两天 liǎng tiān']),
  LQ('M|你丈夫做什么工作？\nF|他是医生，在医院工作。\nN|问：女的丈夫做什么工作？', ['医生 yīshēng', '老师 lǎoshī', '服务员 fúwùyuán']),
  LQ('M|你昨天几点起床的？\nF|六点，我每天早上都去跑步。\nN|问：女的早上做什么？', ['跑步 pǎobù', '游泳 yóuyǒng', '睡觉 shuìjiào']),
  LQ('F|我们一起去唱歌吧！\nM|对不起，我晚上要准备考试。\nN|问：男的晚上要做什么？', ['准备考试 zhǔnbèi kǎoshì', '唱歌 chànggē', '上班 shàngbān']),
  LQ('M|你的房间在几楼？\nF|在三楼，旁边是电梯。\nN|问：女的房间在几楼？', ['三楼 sān lóu', '二楼 èr lóu', '四楼 sì lóu']),
  LQ('F|你觉得这件衣服怎么样？\nM|颜色很好，但是太贵了。\nN|问：男的觉得衣服怎么样？', ['太贵了 tài guì le', '很便宜 hěn piányi', '颜色不好 yánsè bù hǎo']),
], listening=True)

L4 = PART('l-long-dialogue', 'listening', '听力 第四部分（31～35）', 'Dialogue long et question', '听对话，选择正确答案。', 5, [
  LQ('F|你好，我想要一个房间。\nM|好的，您住几天？\nF|三天，星期五走。\nM|房间在五楼，这是您的票。\nN|问：女的要住几天？', ['三天 sān tiān', '五天 wǔ tiān', '一个星期 yí ge xīngqī']),
  LQ('M|你怎么还没到？\nF|对不起，路上车太多了。\nM|你现在在哪儿？\nF|快到了，就在学校旁边。\nN|问：女的为什么还没到？', ['车太多 chē tài duō', '她生病了 tā shēngbìng le', '她起床晚了 tā qǐchuáng wǎn le']),
  LQ('F|你周末做什么了？\nM|星期六我去游泳了。\nF|星期天呢？\nM|星期天在家休息，太累了。\nN|问：男的星期天做什么了？', ['在家休息 zài jiā xiūxi', '去游泳 qù yóuyǒng', '去上班 qù shàngbān']),
  LQ('M|这是你妹妹吗？\nF|不是，是我姐姐。\nM|她看起来比你小！\nF|她比我大两岁。\nN|问：照片上的人是谁？', ['女的姐姐 nǚ de jiějie', '女的妹妹 nǚ de mèimei', '男的妻子 nán de qīzi']),
  LQ('F|请问，去火车站怎么走？\nM|往前走，到了医院往左。\nF|远吗？\nM|不远，走路五分钟。\nN|问：火车站离这儿远吗？', ['不远 bù yuǎn', '很远 hěn yuǎn', '要坐车 yào zuò chē']),
  LQ('M|服务员，我们要两杯咖啡。\nF|好的，还要别的吗？\nM|再要一个蛋糕。\nF|一共六十块。\nN|问：他们一共花了多少钱？', ['六十块 liùshí kuài', '两块 liǎng kuài', '十六块 shíliù kuài']),
  LQ('F|你的汉语老师是哪国人？\nM|她是中国人，姓王。\nF|她上课上得怎么样？\nM|非常好，我们都很喜欢她。\nN|问：男的觉得王老师怎么样？', ['非常好 fēicháng hǎo', '不太好 bú tài hǎo', '太忙了 tài máng le']),
], listening=True)

# ═════════════════════════ 阅读 ═════════════════════════
R1 = PART('r-picture', 'reading', '阅读 第一部分（36～40）', 'Phrase et image', '选择与句子对应的图片。', 5, [
  RQ(['🏊', '🏃', '⚽', '🏀'], '他游泳游得非常快。', 'Tā yóuyǒng yóu de fēicháng kuài.'),
  RQ(['🎂', '🍉', '☕', '🥚'], '今天是我女儿的生日。', 'Jīntiān shì wǒ nǚ’ér de shēngrì.'),
  RQ(['❄️', '☀️', '☔', '☁️'], '下雪了，我们出去玩儿吧！', 'Xià xuě le, wǒmen chūqu wánr ba!'),
  RQ(['💊', '📖', '📱', '⌚'], '医生让我每天吃三次药。', 'Yīshēng ràng wǒ měi tiān chī sān cì yào.'),
  RQ(['🚌', '🚕', '✈️', '🚆'], '我每天坐公共汽车去上班。', 'Wǒ měi tiān zuò gōnggòng qìchē qù shàngbān.'),
  RQ(['🎫', '📰', '✏️', '🔑'], '这是你的火车票，请拿好。', 'Zhè shì nǐ de huǒchē piào, qǐng ná hǎo.'),
  RQ(['📰', '🎫', '✏️', '📱'], '爸爸每天早上都看报纸。', 'Bàba měi tiān zǎoshang dōu kàn bàozhǐ.'),
])

R2 = PART('r-blank', 'reading', '阅读 第二部分（41～45）', 'Choisir le mot', '选词填空。', 5, [
  RQ(['比 bǐ', '最 zuì', '很 hěn', '更 gèng'], '今天＿＿昨天热。', 'Jīntiān ＿＿ zuótiān rè.'),
  RQ(['过 guo', '着 zhe', '得 de', '的 de'], '你去＿＿上海吗？', 'Nǐ qù ＿＿ Shànghǎi ma?'),
  RQ(['离 lí', '从 cóng', '往 wǎng', '在 zài'], '我家＿＿学校很近。', 'Wǒ jiā ＿＿ xuéxiào hěn jìn.'),
  RQ(['得 de', '的 de', '地 de', '了 le'], '她说汉语说＿＿很好。', 'Tā shuō Hànyǔ shuō ＿＿ hěn hǎo.'),
  RQ(['件 jiàn', '张 zhāng', '个 gè', '次 cì'], '我想买一＿＿白衬衫。', 'Wǒ xiǎng mǎi yí ＿＿ bái chènshān.'),
  RQ(['所以 suǒyǐ', '但是 dànshì', '因为 yīnwèi', '虽然 suīrán'], '因为下雨了，＿＿我们没去公园。', 'Yīnwèi xià yǔ le, ＿＿ wǒmen méi qù gōngyuán.'),
  RQ(['已经 yǐjīng', '正在 zhèngzài', '一起 yìqǐ', '可能 kěnéng'], '快走吧，＿＿八点了！', 'Kuài zǒu ba, ＿＿ bā diǎn le!'),
])

def JR(passage, pinyin, statement, true):
    """Lecture : un court texte, puis une phrase ★ à juger vraie ou fausse."""
    q = RQ([YES, NO] if true else [NO, YES], None, '★ ' + statement)
    q['passage'] = passage + '\n' + pinyin
    return q

R3 = PART('r-judge', 'reading', '阅读 第三部分（46～50）', 'Texte et affirmation', '判断句子对错。', 5, [
  JR('我每天早上六点起床，然后去跑步，跑半个小时。', 'Wǒ měi tiān zǎoshang liù diǎn qǐchuáng, ránhòu qù pǎobù, pǎo bàn ge xiǎoshí.', '他每天早上跑步。', True),
  JR('我哥哥比我高，但是我比他重。', 'Wǒ gēge bǐ wǒ gāo, dànshì wǒ bǐ tā zhòng.', '我比哥哥高。', False),
  JR('这家饭馆的菜很好吃，也不贵，所以人非常多。', 'Zhè jiā fànguǎn de cài hěn hǎochī, yě bú guì, suǒyǐ rén fēicháng duō.', '这家饭馆的菜很贵。', False),
  JR('我去过两次中国，第一次是去年，我去了北京。', 'Wǒ qùguo liǎng cì Zhōngguó, dì-yī cì shì qùnián, wǒ qùle Běijīng.', '他去过中国。', True),
  JR('今天虽然是星期六，但是我还要去公司上班。', 'Jīntiān suīrán shì xīngqīliù, dànshì wǒ hái yào qù gōngsī shàngbān.', '他今天不上班。', False),
  JR('我妹妹十岁，她很喜欢唱歌，唱得非常好。', 'Wǒ mèimei shí suì, tā hěn xǐhuan chànggē, chàng de fēicháng hǎo.', '妹妹唱歌唱得很好。', True),
  JR('医生说我要多休息，别喝咖啡，所以我现在每天喝茶。', 'Yīshēng shuō wǒ yào duō xiūxi, bié hē kāfēi, suǒyǐ wǒ xiànzài měi tiān hē chá.', '他现在每天喝咖啡。', False),
])

R4 = PART('r-match', 'reading', '阅读 第四部分（51～60）', 'Question et réponse', '选择正确的回答。', 10, [
  RQ(['还没呢，我正在写。', '是的，我很忙。', '我去过一次。', '在桌子上。'], '你的作业写完了吗？', 'Nǐ de zuòyè xiěwán le ma?'),
  RQ(['不远，坐车十分钟。', '他比我高。', '我们一起去吧。', '已经十点了。'], '机场离这儿远吗？', 'Jīchǎng lí zhèr yuǎn ma?'),
  RQ(['因为我太累了。', '所以我没去。', '我觉得很好。', '他生病了吗？'], '你为什么不去跑步？', 'Nǐ wèishénme bú qù pǎobù?'),
  RQ(['咖啡，谢谢。', '在左边。', '三块钱。', '我喝过。'], '你喝茶还是喝咖啡？', 'Nǐ hē chá háishi hē kāfēi?'),
  RQ(['我姓王。', '我叫贵。', '我是王。', '谢谢您。'], '您贵姓？', 'Nín guì xìng?'),
  RQ(['谢谢你！', '没关系。', '对不起。', '不客气。'], '祝你生日快乐！', 'Zhù nǐ shēngrì kuàilè!'),
  RQ(['当然可以，请进。', '我已经进了。', '门在右边。', '不用谢。'], '我可以进来吗？', 'Wǒ kěyǐ jìnlai ma?'),
  RQ(['跑得很快。', '跑过两次。', '跑步很累。', '在跑步呢。'], '他跑得怎么样？', 'Tā pǎo de zěnmeyàng?'),
  RQ(['晴天，不冷。', '我很好。', '很有意思。', '是红色的。'], '明天天气怎么样？', 'Míngtiān tiānqì zěnmeyàng?'),
  RQ(['八百块。', '八个。', '八点。', '八岁。'], '这个手机多少钱？', 'Zhè ge shǒujī duōshao qián?'),
  RQ(['我在等公共汽车。', '我在家。', '我等过他。', '公共汽车很快。'], '你在这儿做什么？', 'Nǐ zài zhèr zuò shénme?'),
  RQ(['是我丈夫。', '是我的手机。', '他很高。', '他在医院。'], '那个穿黑衣服的人是谁？', 'Nà ge chuān hēi yīfu de rén shì shéi?'),
])

PARTS = [L1, L2, L3, L4, R1, R2, R3, R4]
lis = sum(p['count'] for p in PARTS if p['section'] == 'listening')
rea = sum(p['count'] for p in PARTS if p['section'] == 'reading')
assert (lis, rea) == (35, 25), (lis, rea)
bank = {
  'slug': 'hsk2',
  'level': 'HSK2',
  'contentVersion': '2026.11.23',
  'notice': 'Questions rédigées par Koto Quest au format de l’examen officiel du HSK 2 (HSK 2.0 : types d’épreuves, consignes en chinois, pinyin, notation sur 200). Les images sont remplacées par des pictogrammes. Ce ne sont pas des questions officielles.',
  'parts': PARTS,
}
json.dump(bank, open(os.path.join(ROOT, 'content/exams/hsk2.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
EN = {
  bank['notice']: 'Questions written by Koto Quest in the format of the official HSK 2 exam (HSK 2.0: question types, instructions in Chinese, pinyin, scoring out of 200). Pictures are replaced by pictograms. They are not official questions.',
  'Image : vrai ou faux': 'Picture: true or false', 'Dialogue et image': 'Dialogue and picture', 'Dialogue et question': 'Dialogue and question',
  'Dialogue long et question': 'Long dialogue and question', 'Phrase et image': 'Sentence and picture', 'Choisir le mot': 'Choosing the word',
  'Texte et affirmation': 'Text and statement', 'Question et réponse': 'Question and answer',
}
P_DICT = os.path.join(ROOT, 'content/i18n/en/content.json')
d = json.load(open(P_DICT, encoding='utf-8'))
for k, v in EN.items():
    if k in d and d[k] != v:
        raise SystemExit(f'traduction existante différente : {k} → {d[k]} / {v}')
d.update(EN)
json.dump(d, open(P_DICT, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(f"HSK 2 : {sum(len(p['questions']) for p in PARTS)} questions en banque ; examen de {lis} + {rea} questions")
