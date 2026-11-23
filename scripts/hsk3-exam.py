# Banque de questions de l'examen blanc HSK 3 (content/exams/hsk3.json), au format de l'épreuve officielle (HSK 2.0) :
# 听力 (écoute, 40 questions en quatre parties), 阅读 (lecture, 30 questions en trois parties) et 书写 (écriture,
# 10 questions en deux parties, ici en format à choix), 90 minutes, notation sur 300, réussite à 180.
# Comme à l'examen officiel, plus de pinyin à partir du HSK 3, sauf pour les caractères à écrire (书写 第二部分).
# Dans chaque question, le premier choix est la bonne réponse (l'ordre est mélangé à chaque examen).
# Usage : python3 scripts/hsk3-exam.py
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

def LJ(audio, statement, true):
    """Écoute une phrase, puis juge la phrase ★."""
    return LQ(audio, [YES, NO] if true else [NO, YES], '★ ' + statement)

def RQ(choices, jp=None, text=None, expl=None):
    q = {'choices': choices, 'answer': choices[0], 'explanation': expl or f'Réponse : {choices[0]}'}
    if jp: q['jp'] = jp
    if text: q['text'] = text
    return q

def RP(passage, question, choices):
    """Lecture : un court texte, une question ★."""
    q = RQ(choices, None, '★ ' + question)
    q['passage'] = passage
    return q

def ORDER(words, correct, *wrong):
    """书写 1 : remettre les mots dans l'ordre (choisir la phrase bien construite)."""
    assert sorted(''.join(words)) == sorted(correct.rstrip('。？！')), (words, correct)
    return RQ([correct, *wrong], ' ／ '.join(words), None)

def CHAR(sentence, pinyin, answer, *wrong):
    """书写 2 : écrire le caractère d'après le pinyin (choisir le bon caractère)."""
    assert '（＿）' in sentence
    return RQ([answer, *wrong], sentence.replace('（＿）', f'（{pinyin}）'), None, 'Réponse : ' + sentence.replace('（＿）', answer))

def PART(id, section, jpTitle, title, prompt, count, questions, listening=False):
    for q in questions:
        assert 2 <= len(set(q['choices'])) == len(q['choices']) <= 4, q
    assert len(questions) >= count, id
    p = {'id': id, 'section': section, 'jpTitle': jpTitle, 'title': title, 'prompt': prompt, 'count': count, 'questions': questions}
    if listening:
        p['listening'] = True
    return p

# ═════════════════════════ 听力 ═════════════════════════
L1 = PART('l-dialogue-picture', 'listening', '听力 第一部分（1～10）', 'Dialogue et image', '听对话，选择对应的图片。', 10, [
  LQ('M|你把伞放在哪儿了？\nF|在门旁边，外面还在下雨呢。', ['☔', '🎒', '📷', '👓']),
  LQ('F|你怎么了？脸这么红。\nM|我感冒了，有点儿发烧。', ['🤒', '😂', '🏃', '🍺']),
  LQ('M|周末我们去爬山吧！\nF|好啊，我带照相机。', ['⛰️', '🏊', '🎤', '📚']),
  LQ('F|这双皮鞋怎么样？\nM|很好看，就是有点儿贵。', ['👞', '👗', '🎩', '👖']),
  LQ('M|你在看什么呢？\nF|一个关于熊猫的节目，太可爱了。', ['🐼', '🐎', '🐦', '🐟']),
  LQ('F|我们坐地铁还是骑自行车？\nM|骑自行车吧，天气这么好。', ['🚲', '🚇', '🚢', '✈️']),
  LQ('M|服务员，给我们拿两双筷子。\nF|好的，马上来。', ['🥢', '🍽️', '🥣', '🍾']),
  LQ('F|你的行李箱太重了，我帮你拿吧。\nM|谢谢，我们坐电梯上去。', ['🧳', '🎁', '💼', '☂️']),
  LQ('M|生日快乐！这是送给你的礼物。\nF|谢谢！是什么？我能打开吗？', ['🎁', '🎂', '💐', '✉️']),
  LQ('F|你每天早上做什么运动？\nM|我在公园里跑步，跑半个小时。', ['🏃', '🚴', '🏊', '⚽']),
  LQ('M|冰箱里还有牛奶吗？\nF|没有了，只有几瓶啤酒。', ['🍺', '🥛', '🧃', '☕']),
  LQ('F|别玩儿游戏了，快去刷牙睡觉！\nM|好，马上就去。', ['🪥', '🎮', '🛁', '📺']),
], listening=True)

L2 = PART('l-judge', 'listening', '听力 第二部分（11～20）', 'Phrase et affirmation', '听句子，判断对错。', 10, [
  LJ('N|我以前不喜欢吃面条，后来去了一次北方，就爱上了。', '他现在喜欢吃面条。', True),
  LJ('N|这个房间又干净又安静，离地铁站也很近，就是有点儿小。', '这个房间很大。', False),
  LJ('N|为了提高汉语水平，小王每天晚上都看一个小时中文节目。', '小王想提高汉语水平。', True),
  LJ('N|会议本来九点开始，可是经理九点半才到。', '经理迟到了。', True),
  LJ('N|我把护照忘在宾馆里了，只好坐出租车回去拿。', '他的护照在包里。', False),
  LJ('N|妹妹不但数学成绩好，而且历史也学得很好。', '妹妹只是数学好。', False),
  LJ('N|奶奶年纪大了，除了周末，叔叔每天都去照顾她。', '叔叔周末不去照顾奶奶。', True),
  LJ('N|今天风刮得特别大，我们别去公园了，在家看电影吧。', '他们打算去公园。', False),
  LJ('N|我的自行车被邻居借走了，所以今天坐公共汽车上班。', '他今天骑自行车上班。', False),
  LJ('N|这家超市的水果很新鲜，我一般周末来这儿买。', '他经常在周末来这家超市。', True),
  LJ('N|他越说越生气，最后一句话也没说就离开了。', '他最后很高兴。', False),
  LJ('N|飞机晚上八点起飞，我们最好六点就到机场。', '飞机八点起飞。', True),
], listening=True)

L3 = PART('l-dialogue-question', 'listening', '听力 第三部分（21～30）', 'Dialogue et question', '听对话，选择正确答案。', 10, [
  LQ('M|你的作业做完了吗？\nF|还没有，数学题太难了。\nN|问：女的为什么还没做完作业？', ['题太难', '没有时间', '她生病了']),
  LQ('F|你看见我的眼镜了吗？\nM|在电脑旁边，你刚才放在那儿了。\nN|问：眼镜在哪儿？', ['电脑旁边', '包里', '桌子下面']),
  LQ('M|这条裤子有点儿长，有短一点儿的吗？\nF|有，您试试这条。\nN|问：他们最可能在哪儿？', ['商店', '医院', '图书馆']),
  LQ('F|你最近怎么总是迟到？\nM|对不起，我搬家了，现在住得比较远。\nN|问：男的为什么迟到？', ['住得远', '起床晚了', '车坏了']),
  LQ('M|下个月你去中国旅游吗？\nF|我打算去，但是还没决定去南方还是去北方。\nN|问：女的还没决定什么？', ['去哪儿', '什么时候去', '和谁去']),
  LQ('F|这个故事你听过吗？\nM|听过，我小时候奶奶给我讲过很多次。\nN|问：谁给男的讲过这个故事？', ['奶奶', '老师', '爸爸']),
  LQ('M|喂，你到了吗？\nF|快了，再过一刻钟就到。\nN|问：女的多长时间以后到？', ['十五分钟', '一个小时', '五分钟']),
  LQ('F|我想买一个新的冰箱，你有什么好的选择吗？\nM|你可以先上网看看，再去商店。\nN|问：男的让女的先做什么？', ['上网看看', '去商店', '问朋友']),
  LQ('M|你怎么不吃了？\nF|我已经吃饱了，这个蛋糕太甜了。\nN|问：女的觉得蛋糕怎么样？', ['太甜了', '不新鲜', '太贵了']),
  LQ('F|您好，请问校长办公室在几层？\nM|在五层，你可以坐电梯上去。\nN|问：校长办公室在几层？', ['五层', '三层', '一层']),
  LQ('M|你怎么这么高兴？\nF|我参加的比赛结束了，我拿了第一！\nN|问：女的为什么高兴？', ['比赛拿了第一', '买了礼物', '要结婚了']),
  LQ('F|你对中国文化感兴趣吗？\nM|很感兴趣，特别是中国音乐。\nN|问：男的对什么特别感兴趣？', ['中国音乐', '中国菜', '中国历史']),
], listening=True)

L4 = PART('l-long-dialogue', 'listening', '听力 第四部分（31～40）', 'Dialogue long et question', '听对话，选择正确答案。', 10, [
  LQ('M|你好，我想借这本书。\nF|好的，请给我看一下你的学生证。\nM|给您。我可以借多长时间？\nF|两个星期，别忘了按时还。\nN|问：这本书可以借多长时间？', ['两个星期', '一个星期', '一个月']),
  LQ('F|你的腿怎么了？\nM|昨天踢足球的时候被别人踢了一下。\nF|疼吗？去医院检查了吗？\nM|还有点儿疼，医生说没什么问题。\nN|问：男的腿为什么疼？', ['踢足球时被踢了', '爬山时摔了', '骑车撞了']),
  LQ('M|这个周末你有什么打算？\nF|我想去看电影，你呢？\nM|我要在家打扫房间，我妈妈下周来。\nF|那我们下个周末一起去吧。\nN|问：男的这个周末要做什么？', ['打扫房间', '看电影', '去接妈妈']),
  LQ('F|先生，您要喝点儿什么？\nM|有果汁吗？\nF|有，苹果汁和西瓜汁。\nM|那给我一杯西瓜汁吧，不要太冰的。\nN|问：男的要喝什么？', ['西瓜汁', '苹果汁', '啤酒']),
  LQ('M|听说你要搬家了？\nF|是啊，新房子离公司很近，走路十分钟。\nM|那太方便了！需要帮忙吗？\nF|太好了，星期六你有空吗？\nN|问：女的为什么搬家？', ['新家离公司近', '房子太小', '邻居太吵']),
  LQ('F|你的汉语越来越好了！\nM|谢谢，我每天都跟中国同事说汉语。\nF|你们说什么？\nM|什么都说，工作、生活、电影。\nN|问：男的汉语为什么越来越好？', ['每天跟中国同事说汉语', '每天看中文书', '在中国上学']),
  LQ('M|请问，去火车站怎么走？\nF|一直往前走，到了第二个路口向右。\nM|远吗？要坐车吗？\nF|不远，走过去也就十分钟。\nN|问：到火车站要多长时间？', ['走路十分钟', '坐车十分钟', '走路半个小时']),
  LQ('F|小李，你的照片拍得真好！\nM|谢谢，这是我在黄河边上拍的。\nF|你用什么照相机？\nM|就是我的手机，那天的太阳特别好。\nN|问：照片是用什么拍的？', ['手机', '新照相机', '朋友的照相机']),
  LQ('M|妈妈，我饿了，有什么吃的？\nF|冰箱里有面包和鸡蛋。\nM|我想吃面条。\nF|那你先把作业做完，我一会儿给你做。\nN|问：妈妈让儿子先做什么？', ['做作业', '吃面包', '去买面条']),
  LQ('F|经理，会议几点开始？\nM|本来是三点，现在改到四点了。\nF|那我还有时间把材料准备好。\nM|好，别忘了告诉其他同事。\nN|问：会议现在几点开始？', ['四点', '三点', '两点']),
  LQ('M|你的新邻居怎么样？\nF|很热情，常常请我去他家吃饭。\nM|他是做什么的？\nF|是一位老师，教历史的。\nN|问：新邻居教什么？', ['历史', '数学', '音乐']),
  LQ('F|明天你几点到机场？\nM|飞机十点起飞，我八点到。\nF|我开车送你吧。\nM|太好了，谢谢你！\nN|问：女的明天要做什么？', ['开车送男的', '坐飞机', '去机场接人']),
], listening=True)

# ═════════════════════════ 阅读 ═════════════════════════
R1 = PART('r-match', 'reading', '阅读 第一部分（41～50）', 'Question et réponse', '选择正确的回答。', 10, [
  RQ(['还没有，我一会儿就去。', '我已经吃饱了。', '在电梯旁边。', '我很喜欢那个节目。'], '你给奶奶打电话了吗？'),
  RQ(['不用了，我自己能拿。', '没关系，下次吧。', '对，是我的。', '我也不知道。'], '你的行李箱太重了，我帮你吧。'),
  RQ(['小心点儿，别感冒了。', '祝你生日快乐！', '欢迎欢迎！', '你说得对。'], '外面刮大风了，我还想出去跑步。'),
  RQ(['当然了，我从小就学。', '没问题，我借给你。', '是的，在三层。', '他是我叔叔。'], '你的音乐水平这么高，学了很久吧？'),
  RQ(['太好了，祝你们幸福！', '别着急，慢慢来。', '我也觉得很难。', '他还没决定。'], '我和小王下个月结婚。'),
  RQ(['我以为是星期五。', '我决定去北方。', '我把它关了。', '我们先吃饭吧。'], '今天是星期四，你怎么穿得这么随便？'),
  RQ(['我把它放进冰箱了。', '在桌子上写作业。', '我们一起去吧。', '已经十点一刻了。'], '刚才买的西瓜呢？'),
  RQ(['我对中国历史很感兴趣。', '这本书很便宜。', '图书馆八点开门。', '我借了两本。'], '你为什么选择这本书？'),
  RQ(['还可以，就是比较远。', '他个子很高。', '对，我很满意你。', '我饿了。'], '你的新家怎么样？'),
  RQ(['不客气，这是我应该做的。', '没关系，我不生气。', '我也不明白。', '好的，我马上去。'], '谢谢你照顾我的猫！'),
  RQ(['越来越好了，谢谢关心。', '他是一位医生。', '我不同意。', '一共五十块。'], '你爷爷的身体最近怎么样？'),
  RQ(['我更喜欢坐地铁。', '我已经到了。', '路上车很多。', '我没有护照。'], '你骑车去还是坐地铁去？'),
])

R2 = PART('r-blank', 'reading', '阅读 第二部分（51～60）', 'Choisir le mot', '选词填空。', 10, [
  RQ(['把', '被', '给', '跟'], '请＿＿门关上，外面太吵了。'),
  RQ(['被', '把', '让', '对'], '我的蛋糕＿＿弟弟吃完了。'),
  RQ(['越来越', '一边', '一共', '一直'], '天气＿＿热了，我们去游泳吧。'),
  RQ(['而且', '但是', '所以', '然后'], '这家饭馆的菜不但好吃，＿＿很便宜。'),
  RQ(['就', '才', '再', '还'], '如果你明天有时间，＿＿来我家玩儿吧。'),
  RQ(['才', '就', '又', '都'], '电影七点开始，他七点半＿＿到。'),
  RQ(['对', '跟', '给', '为'], '我＿＿中国音乐很感兴趣。'),
  RQ(['为了', '因为', '虽然', '如果'], '＿＿身体健康，他每天早上都去锻炼。'),
  RQ(['除了', '关于', '根据', '为了'], '＿＿星期天，我每天都上班。'),
  RQ(['以为', '认为', '同意', '决定'], '我＿＿你已经回家了，原来你还在办公室！'),
  RQ(['得', '的', '地', '了'], '这个字太小了，我看不清楚，你写＿＿大一点儿。'),
  RQ(['终于', '突然', '一直', '已经'], '等了一个小时，公共汽车＿＿来了。'),
])

R3 = PART('r-passage', 'reading', '阅读 第三部分（61～70）', 'Texte et question', '阅读短文，选择正确答案。', 10, [
  RP('我爷爷今年八十岁了，身体还非常健康。他每天早上六点起床，先在公园里锻炼一个小时，然后回家吃早饭。', '爷爷每天早上先做什么？', ['去公园锻炼', '吃早饭', '去上班', '看报纸']),
  RP('小张对中国文化很感兴趣，特别喜欢中国历史。为了看懂中文书，他每天晚上都去图书馆学习两个小时。', '小张为什么每天去图书馆？', ['想看懂中文书', '想借音乐', '在那儿工作', '去见朋友']),
  RP('这家超市的东西又新鲜又便宜，所以周末人特别多。如果你不想等太久，最好早上八点就来。', '为什么周末超市人多？', ['东西新鲜便宜', '有比赛', '离地铁站近', '周末不开门']),
  RP('我本来打算坐飞机去上海，但是飞机票太贵了，所以我决定坐火车。火车虽然慢一点儿，但是很舒服。', '他最后怎么去上海？', ['坐火车', '坐飞机', '坐船', '开车']),
  RP('妈妈，我刚才把您的眼镜放在电视旁边了，您找不到的话就去那儿看看。我去图书馆了，晚上回来。小明', '小明给妈妈写这个是为了什么？', ['告诉她眼镜在哪儿', '借她的眼镜', '让她去图书馆', '请她看电视']),
  RP('我们班上个月来了一位新老师，她教我们数学。她讲得非常清楚，也很关心学生，所以大家的数学成绩越来越好了。', '大家的数学成绩为什么越来越好？', ['新老师讲得清楚', '作业越来越少', '考试很容易', '学生都很聪明']),
  RP('北京的秋天是最好的季节，不冷也不热，很少刮风下雨。很多人选择这个时候去北京旅游。', '北京的秋天怎么样？', ['不冷也不热', '经常下雨', '特别冷', '风很大']),
  RP('小王的新家在十二层，楼里有电梯，上下很方便。他家附近有地铁站，还有一个很大的公园。', '小王的新家怎么样？', ['很方便', '没有电梯', '离地铁站远', '在一层']),
  RP('昨天我在路上遇到了一位老同学，我们已经十年没见面了。他变化很大，以前很瘦，现在胖了很多，我差点儿没认出来。', '老同学有什么变化？', ['胖了很多', '瘦了很多', '个子高了', '戴眼镜了']),
  RP('各位客人，飞往广州的飞机还有二十分钟就要起飞了，请大家带好护照和行李，到八号门上飞机。', '这段话最可能在哪儿听到？', ['机场', '火车站', '银行', '饭馆']),
  RP('我妹妹很可爱，个子不高，头发很长，眼睛很大。她喜欢穿裙子，最喜欢的颜色是蓝色。', '关于妹妹，下面哪个是对的？', ['头发很长', '个子很高', '不喜欢裙子', '最喜欢绿色']),
  RP('我习惯每天晚上睡觉以前看半个小时书。可是最近工作太忙了，回家就很累，几乎没有时间看书。', '他最近为什么不看书？', ['工作太忙了', '眼睛不舒服', '书太难了', '没有书'], ),
])

# ═════════════════════════ 书写 ═════════════════════════
W1 = PART('w-order', 'writing', '书写 第一部分（71～75）', 'Remettre dans l’ordre', '完成句子。', 5, [
  ORDER(['把', '桌子上', '我', '放在', '书', '了'], '我把书放在桌子上了。', '我把桌子上放在书了。', '书把我放在桌子上了。', '我放在把书桌子上了。'),
  ORDER(['被', '我的', '自行车', '弟弟', '骑走了'], '我的自行车被弟弟骑走了。', '弟弟被我的自行车骑走了。', '我的弟弟被自行车骑走了。', '被弟弟我的自行车骑走了。'),
  ORDER(['越来越', '他的', '好了', '汉语'], '他的汉语越来越好了。', '他的越来越汉语好了。', '汉语他的越来越好了。', '他的汉语好了越来越。'),
  ORDER(['感兴趣', '我', '对', '中国历史', '很'], '我对中国历史很感兴趣。', '我很对中国历史感兴趣。', '中国历史对我很感兴趣。', '我对很中国历史感兴趣。'),
  ORDER(['一边', '他', '听音乐', '一边', '跑步'], '他一边听音乐一边跑步。', '一边他听音乐一边跑步。', '他听音乐一边一边跑步。', '他一边一边听音乐跑步。'),
  ORDER(['比', '今天', '昨天', '冷', '一点儿'], '今天比昨天冷一点儿。', '今天冷比昨天一点儿。', '今天比昨天一点儿冷。', '比今天昨天冷一点儿。'),
  ORDER(['终于', '公共汽车', '来了'], '公共汽车终于来了。', '终于公共汽车了来。', '公共汽车来了终于。', '来了公共汽车终于。'),
])

W2 = PART('w-char', 'writing', '书写 第二部分（76～80）', 'Écrire le caractère', '看拼音，写汉字。', 5, [
  CHAR('今天天气很好，我们去（＿）山吧。', 'pá', '爬', '怕', '把', '吧'),
  CHAR('我饿了，想吃一碗（＿）条。', 'miàn', '面', '而', '画', '间'),
  CHAR('外面下雨了，别忘了带（＿）。', 'sǎn', '伞', '半', '平', '三'),
  CHAR('我（＿）冒了，今天不能去上课。', 'gǎn', '感', '赶', '敢', '干'),
  CHAR('他每天骑自行（＿）去上班。', 'chē', '车', '东', '年', '牛'),
  CHAR('这个句子太难了，我看不（＿）。', 'dǒng', '懂', '动', '冬', '董'),
  CHAR('我（＿）中国音乐很感兴趣。', 'duì', '对', '队', '才', '又'),
])

PARTS = [L1, L2, L3, L4, R1, R2, R3, W1, W2]
lis = sum(p['count'] for p in PARTS if p['section'] == 'listening')
rea = sum(p['count'] for p in PARTS if p['section'] == 'reading')
wri = sum(p['count'] for p in PARTS if p['section'] == 'writing')
assert (lis, rea, wri) == (40, 30, 10), (lis, rea, wri)
bank = {
  'slug': 'hsk3',
  'level': 'HSK3',
  'contentVersion': '2026.11.23',
  'notice': 'Questions rédigées par Koto Quest au format de l’examen officiel du HSK 3 (HSK 2.0 : types d’épreuves, consignes en chinois, notation sur 300). Les images sont remplacées par des pictogrammes et l’écriture se fait par choix multiple. Ce ne sont pas des questions officielles.',
  'parts': PARTS,
}
json.dump(bank, open(os.path.join(ROOT, 'content/exams/hsk3.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
EN = {
  bank['notice']: 'Questions written by Koto Quest in the format of the official HSK 3 exam (HSK 2.0: question types, instructions in Chinese, scoring out of 300). Pictures are replaced by pictograms and writing is multiple choice. They are not official questions.',
  'Dialogue et image': 'Dialogue and picture', 'Phrase et affirmation': 'Sentence and statement', 'Dialogue et question': 'Dialogue and question',
  'Dialogue long et question': 'Long dialogue and question', 'Question et réponse': 'Question and answer', 'Choisir le mot': 'Choosing the word',
  'Texte et question': 'Text and question', 'Remettre dans l’ordre': 'Putting in order', 'Écrire le caractère': 'Writing the character',
}
P_DICT = os.path.join(ROOT, 'content/i18n/en/content.json')
d = json.load(open(P_DICT, encoding='utf-8'))
for k, v in EN.items():
    if k in d and d[k] != v:
        raise SystemExit(f'traduction existante différente : {k} → {d[k]} / {v}')
d.update(EN)
json.dump(d, open(P_DICT, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(f"HSK 3 : {sum(len(p['questions']) for p in PARTS)} questions en banque ; examen de {lis} + {rea} + {wri} questions")
