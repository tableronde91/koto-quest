# Niveau HSK 1 (chinois, HSK 2.0 niveau 1) : 8 royaumes, 26 leçons et un examen blanc (français + anglais).
# Mode histoire : le messager des Royaumes combattants (voir gen-story.py). Écrit aussi la section HSK 1 de l'onglet Hanzi.
# Usage : python3 scripts/hsk1-level.py   (réécrit content/hsk1/hsk1.json et content/characters/hanzi.json)
from zh_common import *

REGION = 'Plaine du Fleuve Jaune'

# ═════════════════════════ Royaume 1 : Lu, l'école du maître ═════════════════════════
W1 = WORLD('hsk1-w1', ('L’école du maître', 'The master’s school'), REGION,
  ('Le pinyin, les quatre tons, les nombres de un à dix et les premiers caractères.', 'Pinyin, the four tones, the numbers one to ten and the first characters.'),
  (('Le Nian du Nouvel An', 'The New Year Nian'), '年', ('Chaque hiver, la bête Nian descend de la montagne pour dévorer les récoltes du royaume de Lu. Elle ne craint que le rouge, le bruit… et ceux qui prononcent les tons sans faute.', 'Every winter, the Nian beast comes down from the mountain to devour the harvests of the state of Lu. It fears only red, noise… and those who pronounce the tones without a mistake.')),
  [CH('hsk1-w1-c1', ('Les sons du chinois', 'The sounds of Chinese'), [
    L('zh-tones', ('Le pinyin et les quatre tons', 'Pinyin and the four tones'), ('Lire le pinyin et reconnaître les quatre tons sur les nombres de un à dix.', 'Read pinyin and recognise the four tones on the numbers one to ten.'), 9, [
        ('Le pinyin écrit la prononciation du chinois en lettres latines. Chaque syllabe porte un ton, noté par un accent : ā (1er ton, haut et plat), á (2e, montant), ǎ (3e, descendant puis montant), à (4e, descendant sec).', 'Pinyin writes Chinese pronunciation in Latin letters. Each syllable carries a tone, shown by an accent: ā (1st tone, high and level), á (2nd, rising), ǎ (3rd, falling then rising), à (4th, sharp fall).'),
        ('Le ton change le sens : mā (maman), má (chanvre), mǎ (cheval), mà (gronder). Une syllabe sans accent est neutre, légère et brève : ma, de, le.', 'The tone changes the meaning: mā (mother), má (hemp), mǎ (horse), mà (to scold). A syllable without an accent is neutral, light and short: ma, de, le.'),
        ('Les nombres sont un bon entraînement : yī, èr, sān, sì, wǔ, liù, qī, bā, jiǔ, shí. Attention : en pinyin, x se dit presque « s chuintant », q presque « tch », et sh comme « ch ».', 'Numbers are good practice: yī, èr, sān, sì, wǔ, liù, qī, bā, jiǔ, shí. Careful: in pinyin, x sounds close to a soft “sh”, q close to “ch”, and sh like “sh”.'),
      ], [
        Z('yi', '一', 'yī', ('un', 'one')),
        Z('er', '二', 'èr', ('deux', 'two')),
        Z('san', '三', 'sān', ('trois', 'three')),
        Z('si', '四', 'sì', ('quatre', 'four')),
        Z('wu', '五', 'wǔ', ('cinq', 'five')),
        Z('liu', '六', 'liù', ('six', 'six')),
        Z('qi', '七', 'qī', ('sept', 'seven')),
        Z('ba', '八', 'bā', ('huit', 'eight')),
        Z('jiu', '九', 'jiǔ', ('neuf', 'nine')),
        Z('shi', '十', 'shí', ('dix', 'ten')),
      ], [
        x('一、二、三、四、五', 'yī, èr, sān, sì, wǔ', 'un, deux, trois, quatre, cinq', 'one, two, three, four, five'),
        x('六、七、八、九、十', 'liù, qī, bā, jiǔ, shí', 'six, sept, huit, neuf, dix', 'six, seven, eight, nine, ten'),
      ], [
        FB(('Quel est le pinyin de ce nombre ?', 'What is the pinyin of this number?'), '八 = ＿', ['bā', 'bà', 'pā'], 'bā', ('八 se dit bā, au 1er ton (haut et plat).', '八 is said bā, in the 1st tone (high and level).'), ('huit', 'eight')),
        FB(('Quel est le pinyin de ce nombre ?', 'What is the pinyin of this number?'), '五 = ＿', ['wǔ', 'wù', 'wú'], 'wǔ', ('五 se dit wǔ, au 3e ton (descendant puis montant).', '五 is said wǔ, in the 3rd tone (falling then rising).'), ('cinq', 'five')),
        FB(('Quel est le pinyin de ce nombre ?', 'What is the pinyin of this number?'), '十 = ＿', ['shí', 'sì', 'xí'], 'shí', ('十 = shí (2e ton) ; ne le confonds pas avec 四 sì (quatre).', '十 = shí (2nd tone); do not confuse it with 四 sì (four).'), ('dix', 'ten')),
        TF('七', ('Ce caractère se lit qī et signifie « sept ».', 'This character is read qī and means “seven”.'), VRAI, ('七 = qī, sept.', '七 = qī, seven.')),
      ]),
  ]),
  CH('hsk1-w1-c2', ('Le pinceau et l’encre', 'Brush and ink'), [
    HL('zh-hz-strokes', ('Les premiers traits : 一 二 三 十 人 大 小 口', 'The first strokes: 一 二 三 十 人 大 小 口'), ('Reconnaître huit caractères simples et leur pinyin.', 'Recognise eight simple characters and their pinyin.'), [
      ('Un caractère se trace dans un ordre fixe : de haut en bas, de gauche à droite, l’horizontale avant la verticale. 十 : d’abord 一, puis le trait vertical.', 'A character is written in a fixed order: top to bottom, left to right, horizontal before vertical. 十: first 一, then the vertical stroke.'),
      ('Beaucoup de caractères dessinent ce qu’ils disent : 人 (rén) est une personne qui marche, 大 (dà) une personne qui écarte les bras, 口 (kǒu) une bouche ouverte.', 'Many characters draw what they mean: 人 (rén) is a person walking, 大 (dà) a person spreading their arms, 口 (kǒu) an open mouth.'),
    ], [
      H('yi', '一', 'yī', ('un', 'one'), 1), H('er', '二', 'èr', ('deux', 'two'), 2), H('san', '三', 'sān', ('trois', 'three'), 3), H('shi', '十', 'shí', ('dix', 'ten'), 2),
      H('ren', '人', 'rén', ('personne, être humain', 'person, human being'), 2), H('da', '大', 'dà', ('grand', 'big'), 3), H('xiao', '小', 'xiǎo', ('petit', 'small'), 3), H('kou', '口', 'kǒu', ('bouche', 'mouth'), 3),
    ]),
    HL('zh-hz-pictures', ('Les caractères-images : 日 月 水 火 女 子 中 上 下', 'Picture characters: 日 月 水 火 女 子 中 上 下'), ('Reconnaître neuf caractères nés d’un dessin.', 'Recognise nine characters that began as drawings.'), [
      ('日 (rì) était un soleil rond devenu carré, 月 (yuè) un croissant de lune, 水 (shuǐ) de l’eau qui coule, 火 (huǒ) des flammes.', '日 (rì) was a round sun that became square, 月 (yuè) a crescent moon, 水 (shuǐ) flowing water, 火 (huǒ) flames.'),
      ('Certains caractères montrent une idée : 上 (shàng, au-dessus) et 下 (xià, en dessous) placent un trait au-dessus ou au-dessous d’une ligne ; 中 (zhōng, milieu) traverse un carré en son centre.', 'Some characters show an idea: 上 (shàng, above) and 下 (xià, below) put a stroke above or below a line; 中 (zhōng, middle) crosses a square through its centre.'),
    ], [
      H('ri', '日', 'rì', ('soleil, jour', 'sun, day'), 4), H('yue', '月', 'yuè', ('lune, mois', 'moon, month'), 4), H('shui', '水', 'shuǐ', ('eau', 'water'), 4),
      H('huo', '火', 'huǒ', ('feu', 'fire'), 4), H('nv', '女', 'nǚ', ('femme', 'woman'), 3), H('zi', '子', 'zǐ', ('enfant', 'child'), 3),
      H('zhong', '中', 'zhōng', ('milieu, centre', 'middle, centre'), 4), H('shang', '上', 'shàng', ('au-dessus, sur', 'above, on'), 3), H('xia', '下', 'xià', ('en dessous, sous', 'below, under'), 3),
    ]),
  ])])

# ═════════════════════════ Royaume 2 : Qi, le calendrier du roi ═════════════════════════
W2 = WORLD('hsk1-w2', ('Le calendrier du roi de Qi', 'The calendar of the king of Qi'), REGION,
  ('Les dates, l’âge, les jours de la semaine, aujourd’hui, demain et hier.', 'Dates, age, days of the week, today, tomorrow and yesterday.'),
  (('Le Taotie glouton', 'The Greedy Taotie'), '饕', ('Le Taotie, monstre affamé gravé sur les bronzes de Qi, a avalé le calendrier du roi. Rends à chaque jour sa date pour qu’il le recrache !', 'The Taotie, a hungry monster carved on the bronzes of Qi, has swallowed the king’s calendar. Give each day back its date to make it spit it out!')),
  [CH('hsk1-w2-c1', ('Compter les jours', 'Counting the days'), [
    HL('zh-hz-time', ('Les caractères du temps : 几 岁 年 号 星 期 今 明 天 昨', 'Time characters: 几 岁 年 号 星 期 今 明 天 昨'), ('Reconnaître les caractères des dates et de l’âge.', 'Recognise the characters of dates and age.'), [
      ('今 (jīn, maintenant), 明 (míng, clair : le soleil 日 et la lune 月 ensemble) et 昨 (zuó, la veille) se combinent avec 天 (tiān, ciel, jour) : 今天, 明天, 昨天.', '今 (jīn, now), 明 (míng, bright: the sun 日 and the moon 月 together) and 昨 (zuó, the day before) combine with 天 (tiān, sky, day): 今天, 明天, 昨天.'),
      ('星期 (xīngqī) signifie « semaine » ; 号 (hào) le numéro du jour dans le mois ; 岁 (suì) les années d’âge.', '星期 (xīngqī) means “week”; 号 (hào) the number of the day in the month; 岁 (suì) years of age.'),
    ], [
      H('ji', '几', 'jǐ', ('combien (petit nombre)', 'how many (small number)'), 2), H('sui', '岁', 'suì', ('an (d’âge)', 'year (of age)'), 6), H('nian', '年', 'nián', ('an, année', 'year'), 6),
      H('hao', '号', 'hào', ('numéro, jour du mois', 'number, day of the month'), 5), H('xing', '星', 'xīng', ('étoile', 'star'), 9), H('qi-period', '期', 'qī', ('période', 'period'), 12),
      H('jin', '今', 'jīn', ('maintenant, aujourd’hui', 'now, today'), 4), H('ming', '明', 'míng', ('clair, lumineux', 'bright, clear'), 8), H('tian', '天', 'tiān', ('ciel, jour', 'sky, day'), 4), H('zuo-yesterday', '昨', 'zuó', ('hier, la veille', 'yesterday, the day before'), 9),
    ]),
    L('zh-dates', ('Les dates : 年、月、号 et 星期', 'Dates: 年, 月, 号 and 星期'), ('Dire une date et un jour de la semaine.', 'Say a date and a day of the week.'), 9, [
        ('Une date va du plus grand au plus petit : année + 年, mois + 月, jour + 号 (à l’écrit 日). 2026年11月22号 = le 22 novembre 2026.', 'A date goes from largest to smallest: year + 年, month + 月, day + 号 (日 in writing). 2026年11月22号 = 22 November 2026.'),
        ('Les mois se comptent : 一月 (janvier), 二月 (février)… 十二月 (décembre). Les jours de la semaine aussi : 星期一 (lundi)… 星期六 (samedi), mais dimanche = 星期天 (ou 星期日).', 'Months are counted: 一月 (January), 二月 (February)… 十二月 (December). So are the days of the week: 星期一 (Monday)… 星期六 (Saturday), but Sunday = 星期天 (or 星期日).'),
        ('Pour demander : 今天几号？(quel jour sommes-nous ?), 今天星期几？(quel jour de la semaine ?). La réponse prend la place de 几.', 'To ask: 今天几号？(what is the date today?), 今天星期几？(what day of the week is it?). The answer takes the place of 几.'),
      ], [
        ZG('date-order', '年 + 月 + 号', None, ('ordre de la date : année, mois, jour', 'date order: year, month, day')),
        Z('nian', '年', 'nián', ('an, année', 'year')),
        Z('yue', '月', 'yuè', ('mois', 'month')),
        Z('hao', '号', 'hào', ('jour (du mois)', 'day (of the month)')),
        Z('xingqi', '星期', 'xīngqī', ('semaine', 'week')),
        Z('jintian', '今天', 'jīntiān', ('aujourd’hui', 'today')),
        Z('mingtian', '明天', 'míngtiān', ('demain', 'tomorrow')),
        Z('zuotian', '昨天', 'zuótiān', ('hier', 'yesterday')),
      ], [
        x('今天几号？——今天十一月二十二号。', 'Jīntiān jǐ hào? — Jīntiān shíyī yuè èrshí’èr hào.', 'Quel jour sommes-nous ? — Nous sommes le 22 novembre.', 'What is the date today? — Today is 22 November.'),
        x('明天星期天。', 'Míngtiān xīngqītiān.', 'Demain, c’est dimanche.', 'Tomorrow is Sunday.'),
      ], [
        FB(COMPLETE, '今天十月一＿。', ['号', '年', '星期'], '号', ('Le jour du mois : nombre + 号.', 'The day of the month: number + 号.'), ('Aujourd’hui, c’est le 1er octobre.', 'Today is 1 October.')),
        FB(COMPLETE, '今天星期＿？', ['几', '号', '月'], '几', ('Pour demander le jour de la semaine : 星期几？', 'To ask the day of the week: 星期几？'), ('Quel jour de la semaine sommes-nous ?', 'What day of the week is it today?')),
        TF('昨天星期一，今天星期二。', ('Aujourd’hui, c’est mardi.', 'Today is Tuesday.'), VRAI, ('星期二 = mardi (deuxième jour).', '星期二 = Tuesday (second day).')),
        SO(ORDER('Demain, c’est le 3 mai.', 'Tomorrow is 3 May.'), ['明天', '五月', '三号。'], ('Le moment, puis le mois, puis le jour.', 'The time word, then the month, then the day.')),
      ]),
  ]),
  CH('hsk1-w2-c2', ('L’âge du prince', 'The prince’s age'), [
    L('zh-age', ('L’âge : 几岁 et 多大', 'Age: 几岁 and 多大'), ('Demander et dire l’âge de quelqu’un.', 'Ask and give someone’s age.'), 8, [
        ('Nombre + 岁 = … ans. Le verbe « être » n’est pas nécessaire : 我二十岁 (j’ai vingt ans).', 'Number + 岁 = … years old. The verb “to be” is not needed: 我二十岁 (I am twenty).'),
        ('Les dizaines se forment comme en multipliant : 二十 (2 × 10 = 20), 三十五 (35), 九十九 (99). Cent = 一百.', 'Tens are formed by multiplying: 二十 (2 × 10 = 20), 三十五 (35), 九十九 (99). A hundred = 一百.'),
        ('À un enfant : 你几岁？(petit nombre attendu). À un adulte : 你多大？ou 你多大了？', 'To a child: 你几岁？(a small number is expected). To an adult: 你多大？or 你多大了？'),
      ], [
        ZG('sui', '数字 + 岁', None, ('avoir … ans', 'to be … years old')),
        Z('sui', '岁', 'suì', ('an (âge)', 'year old')),
        Z('ji', '几', 'jǐ', ('combien (petit nombre)', 'how many (small number)')),
        Z('duo', '多', 'duō', ('beaucoup, nombreux', 'many, much')),
        Z('da', '大', 'dà', ('grand, âgé', 'big, old (age)')),
        Z('ling', '零', 'líng', ('zéro', 'zero')),
      ], [
        x('你女儿几岁？——她七岁。', 'Nǐ nǚ’ér jǐ suì? — Tā qī suì.', 'Quel âge a ta fille ? — Elle a sept ans.', 'How old is your daughter? — She is seven.'),
        x('王老师四十五岁。', 'Wáng lǎoshī sìshíwǔ suì.', 'Le professeur Wang a quarante-cinq ans.', 'Teacher Wang is forty-five.'),
      ], [
        FB(COMPLETE, '我二十三＿。', ['岁', '号', '年'], '岁', ('L’âge : nombre + 岁.', 'Age: number + 岁.'), ('J’ai vingt-trois ans.', 'I am twenty-three.')),
        FB(('Comment écrit-on 35 ?', 'How do you write 35?'), '35 = ＿', ['三十五', '五十三', '三五'], '三十五', ('3 × 10 + 5 : 三十五.', '3 × 10 + 5: 三十五.'), ('trente-cinq', 'thirty-five')),
        DC(ANSWER, [('小明', '你几岁？')], ('Xiaoming demande ton âge (tu as huit ans).', 'Xiaoming asks your age (you are eight).'), ['我八岁。', '我八号。', '今天八号。'], '我八岁。', ('L’âge se dit avec 岁.', 'Age is given with 岁.')),
        TF('他九十岁。', ('Il a dix-neuf ans.', 'He is nineteen.'), FAUX, ('九十 = 90 ; dix-neuf se dit 十九.', '九十 = 90; nineteen is 十九.')),
      ]),
  ])])

# ═════════════════════════ Royaume 3 : Chu, les présentations à la cour ═════════════════════════
W3 = WORLD('hsk1-w3', ('La cour de Chu', 'The court of Chu'), REGION,
  ('Saluer, remercier, s’excuser, dire son nom et sa nationalité, poser une question avec 吗 et 呢.', 'Greet, thank, apologise, give your name and nationality, ask a question with 吗 and 呢.'),
  (('La Renarde à neuf queues', 'The Nine-Tailed Fox'), '尾', ('À la cour de Chu, une renarde à neuf queues a pris l’apparence d’une dame d’honneur. Salue chacun comme il se doit et elle trahira sa vraie nature.', 'At the court of Chu, a nine-tailed fox has taken the form of a lady-in-waiting. Greet everyone properly and she will betray her true nature.')),
  [CH('hsk1-w3-c1', ('Bonjour et merci', 'Hello and thank you'), [
    HL('zh-hz-people', ('Les caractères des personnes : 你 我 他 她 们 好 是 不', 'People characters: 你 我 他 她 们 好 是 不'), ('Reconnaître les pronoms et les premiers verbes.', 'Recognise the pronouns and the first verbs.'), [
      ('Beaucoup de caractères ont une « clé » qui indique le thème : 亻 (la personne) dans 你, 他, 们 ; 女 (la femme) dans 她 et 好.', 'Many characters have a “radical” that shows the theme: 亻 (person) in 你, 他, 们; 女 (woman) in 她 and 好.'),
      ('好 (hǎo, bien) réunit une femme 女 et un enfant 子 : ce qui est bon. 他 (il) et 她 (elle) se prononcent tous les deux tā.', '好 (hǎo, good) brings together a woman 女 and a child 子: what is good. 他 (he) and 她 (she) are both pronounced tā.'),
    ], [
      H('ni', '你', 'nǐ', ('tu, toi', 'you (singular)'), 7), H('wo', '我', 'wǒ', ('je, moi', 'I, me'), 7), H('ta-he', '他', 'tā', ('il, lui', 'he, him'), 5), H('ta-she', '她', 'tā', ('elle', 'she, her'), 6),
      H('men', '们', 'men', ('marque du pluriel (personnes)', 'plural marker (people)'), 5), H('hao-good', '好', 'hǎo', ('bien, bon', 'good, well'), 6), H('shi-be', '是', 'shì', ('être', 'to be'), 9), H('bu', '不', 'bù', ('ne… pas', 'not'), 4),
    ]),
    L('zh-greetings', ('Bonjour, merci, pardon', 'Hello, thank you, sorry'), ('Saluer, remercier, s’excuser et prendre congé.', 'Greet, thank, apologise and say goodbye.'), 8, [
        ('你好 (nǐ hǎo) = bonjour. À plusieurs personnes : 你们好. Le 3e ton de 你 devient montant devant un autre 3e ton : on dit « ní hǎo ».', '你好 (nǐ hǎo) = hello. To several people: 你们好. The 3rd tone of 你 becomes rising before another 3rd tone: you say “ní hǎo”.'),
        ('谢谢 (xièxie) = merci ; on répond 不客气 (bú kèqi, de rien). 对不起 (duìbuqǐ) = pardon ; on répond 没关系 (méi guānxi, ce n’est pas grave).', '谢谢 (xièxie) = thank you; the answer is 不客气 (bú kèqi, you’re welcome). 对不起 (duìbuqǐ) = sorry; the answer is 没关系 (méi guānxi, it doesn’t matter).'),
        ('再见 (zàijiàn) = au revoir, littéralement « se revoir ».', '再见 (zàijiàn) = goodbye, literally “see again”.'),
      ], [
        Z('nihao', '你好', 'nǐ hǎo', ('bonjour', 'hello')),
        Z('xiexie', '谢谢', 'xièxie', ('merci', 'thank you')),
        Z('bukeqi', '不客气', 'bú kèqi', ('de rien', 'you’re welcome')),
        Z('duibuqi', '对不起', 'duìbuqǐ', ('pardon, désolé', 'sorry')),
        Z('meiguanxi', '没关系', 'méi guānxi', ('ce n’est pas grave', 'it doesn’t matter')),
        Z('zaijian', '再见', 'zàijiàn', ('au revoir', 'goodbye')),
      ], [
        x('谢谢你！——不客气。', 'Xièxie nǐ! — Bú kèqi.', 'Merci ! — De rien.', 'Thank you! — You’re welcome.'),
        x('对不起！——没关系。', 'Duìbuqǐ! — Méi guānxi.', 'Pardon ! — Ce n’est pas grave.', 'Sorry! — It doesn’t matter.'),
      ], [
        DC(ANSWER, [('王老师', '谢谢你！')], ('Le professeur Wang te remercie.', 'Teacher Wang thanks you.'), ['不客气。', '没关系。', '再见。'], '不客气。', ('À 谢谢, on répond 不客气.', 'You answer 谢谢 with 不客气.')),
        DC(ANSWER, [('小明', '对不起！')], ('Xiaoming te bouscule et s’excuse.', 'Xiaoming bumps into you and apologises.'), ['没关系。', '不客气。', '你好。'], '没关系。', ('À 对不起, on répond 没关系.', 'You answer 对不起 with 没关系.')),
        FB(COMPLETE, '老师，再＿！', ['见', '好', '是'], '见', ('Au revoir : 再见.', 'Goodbye: 再见.'), ('Au revoir, professeur !', 'Goodbye, teacher!')),
        TF('你们好！', ('On salue plusieurs personnes.', 'You are greeting several people.'), VRAI, ('们 marque le pluriel : 你们 = vous.', '们 marks the plural: 你们 = you (plural).')),
      ]),
  ]),
  CH('hsk1-w3-c2', ('Qui es-tu ?', 'Who are you?'), [
    L('zh-shi', ('Être : 是, 不是 et la question 吗', 'To be: 是, 不是 and questions with 吗'), ('Dire qui l’on est et poser une question fermée.', 'Say who you are and ask a yes/no question.'), 9, [
        ('Sujet + 是 + nom : 我是学生 (je suis étudiant). Les verbes ne se conjuguent jamais : 我是, 你是, 他是.', 'Subject + 是 + noun: 我是学生 (I am a student). Verbs are never conjugated: 我是, 你是, 他是.'),
        ('La négation 不 se place devant le verbe : 我不是老师. Devant un 4e ton, 不 se prononce bú : bú shì.', 'The negation 不 goes before the verb: 我不是老师. Before a 4th tone, 不 is pronounced bú: bú shì.'),
        ('Pour une question fermée, ajoute 吗 à la fin d’une affirmation : 你是老师吗？On répond par le verbe : 是 / 不是.', 'For a yes/no question, add 吗 at the end of a statement: 你是老师吗？You answer with the verb: 是 / 不是.'),
      ], [
        ZG('shi', '是', 'shì', ('être (sujet + 是 + nom)', 'to be (subject + 是 + noun)')),
        ZG('bu', '不', 'bù', ('négation : ne… pas', 'negation: not')),
        ZG('ma', '吗', 'ma', ('particule de question (oui / non)', 'question particle (yes / no)')),
        Z('wo', '我', 'wǒ', ('je, moi', 'I, me')),
        Z('ni', '你', 'nǐ', ('tu, toi', 'you (singular)')),
        Z('ta-he', '他', 'tā', ('il, lui', 'he, him')),
        Z('ta-she', '她', 'tā', ('elle', 'she, her')),
        Z('women', '我们', 'wǒmen', ('nous', 'we, us')),
        Z('laoshi', '老师', 'lǎoshī', ('professeur', 'teacher')),
        Z('xuesheng', '学生', 'xuésheng', ('étudiant, élève', 'student, pupil')),
      ], [
        x('你是学生吗？——是，我是学生。', 'Nǐ shì xuésheng ma? — Shì, wǒ shì xuésheng.', 'Tu es étudiant ? — Oui, je suis étudiant.', 'Are you a student? — Yes, I am a student.'),
        x('她不是老师，她是学生。', 'Tā bú shì lǎoshī, tā shì xuésheng.', 'Elle n’est pas professeure, elle est étudiante.', 'She is not a teacher, she is a student.'),
      ], [
        FB(COMPLETE, '他是老师＿？', ['吗', '不', '是'], '吗', ('Question fermée : phrase + 吗.', 'Yes/no question: sentence + 吗.'), ('Est-il professeur ?', 'Is he a teacher?')),
        FB(COMPLETE, '我＿是老师，我是学生。', ['不', '吗', '们'], '不', ('La négation 不 se place devant 是.', 'The negation 不 goes before 是.'), ('Je ne suis pas professeur, je suis étudiant.', 'I am not a teacher, I am a student.')),
        SO(ORDER('Nous sommes étudiants.', 'We are students.'), ['我们', '是', '学生。'], ('Sujet + 是 + nom.', 'Subject + 是 + noun.')),
        TF('他不是学生。', ('Il est étudiant.', 'He is a student.'), FAUX, ('不是 = n’est pas.', '不是 = is not.')),
      ]),
    L('zh-name', ('Le nom et le pays : 叫、什么、哪国人', 'Name and country: 叫, 什么, 哪国人'), ('Demander et dire son nom et sa nationalité.', 'Ask and give your name and nationality.'), 9, [
        ('我叫… = je m’appelle… ; 你叫什么名字？= comment t’appelles-tu ? Le mot interrogatif reste à la place de la réponse : 什么 remplace le nom.', '我叫… = my name is…; 你叫什么名字？= what is your name? The question word stays where the answer goes: 什么 replaces the name.'),
        ('Nationalité = pays + 人 : 中国人 (Chinois), 法国人 (Français). Pour demander : 你是哪国人？', 'Nationality = country + 人: 中国人 (Chinese), 法国人 (French). To ask: 你是哪国人？'),
        ('呢 renvoie la question : 我是法国人，你呢？(je suis français, et toi ?).', '呢 bounces the question back: 我是法国人，你呢？(I am French, and you?).'),
      ], [
        ZG('ne', '呢', 'ne', ('et toi ? (question renvoyée)', 'and you? (question bounced back)')),
        Z('jiao', '叫', 'jiào', ('s’appeler', 'to be called')),
        Z('shenme', '什么', 'shénme', ('quoi', 'what')),
        Z('mingzi', '名字', 'míngzi', ('nom, prénom', 'name')),
        Z('zhongguo', '中国', 'Zhōngguó', ('la Chine', 'China')),
        Z('ren', '人', 'rén', ('personne, gens', 'person, people')),
        Z('pengyou', '朋友', 'péngyou', ('ami', 'friend')),
        Z('tongxue', '同学', 'tóngxué', ('camarade de classe', 'classmate')),
      ], [
        x('你叫什么名字？——我叫李月。', 'Nǐ jiào shénme míngzi? — Wǒ jiào Lǐ Yuè.', 'Comment t’appelles-tu ? — Je m’appelle Li Yue.', 'What is your name? — My name is Li Yue.'),
        x('我是中国人，你呢？', 'Wǒ shì Zhōngguó rén, nǐ ne?', 'Je suis chinois, et toi ?', 'I am Chinese, and you?'),
      ], [
        FB(COMPLETE, '你叫＿名字？', ['什么', '吗', '呢'], '什么', ('什么 remplace le nom demandé.', '什么 replaces the name being asked for.'), ('Comment t’appelles-tu ?', 'What is your name?')),
        FB(COMPLETE, '我是学生，你＿？', ['呢', '吗', '什么'], '呢', ('呢 renvoie la question : et toi ?', '呢 bounces the question back: and you?'), ('Je suis étudiant, et toi ?', 'I am a student, and you?')),
        DC(ANSWER, [('大卫', '你是哪国人？')], ('David te demande ta nationalité (tu es chinois).', 'David asks your nationality (you are Chinese).'), ['我是中国人。', '我叫中国。', '中国人呢？'], '我是中国人。', ('Pays + 人 pour la nationalité.', 'Country + 人 for nationality.')),
        SO(ORDER('Il est mon ami.', 'He is my friend.'), ['他', '是', '我', '朋友。'], ('Sujet + 是 + nom (我朋友 : mon ami, entre proches).', 'Subject + 是 + noun (我朋友: my friend, between close people).')),
      ]),
  ])])

# ═════════════════════════ Royaume 4 : Yan, la maison du général ═════════════════════════
W4 = WORLD('hsk1-w4', ('La maison du général de Yan', 'The house of the general of Yan'), REGION,
  ('La famille, la possession avec 的, avoir avec 有 / 没有, les classificateurs 个 et 口, et ceci, cela, qui.', 'Family, possession with 的, to have with 有 / 没有, the measure words 个 and 口, and this, that, who.'),
  (('Le Kui à une patte', 'The One-Legged Kui'), '夔', ('Le Kui, bête à une seule patte dont le cri sonne comme le tonnerre, s’est installé dans la maison du général. Il ne partira que si tu nommes chaque membre de la famille.', 'The Kui, a one-legged beast whose cry sounds like thunder, has moved into the general’s house. It will only leave if you name every member of the family.')),
  [CH('hsk1-w4-c1', ('La famille', 'Family'), [
    HL('zh-hz-family', ('Les caractères de la maison : 家 爸 妈 儿 有 没 的 个', 'House characters: 家 爸 妈 儿 有 没 的 个'), ('Reconnaître les caractères de la famille et de la possession.', 'Recognise the characters of family and possession.'), [
      ('家 (jiā, maison, famille) montre un cochon 豕 sous un toit 宀 : dans la Chine ancienne, une maison abritait aussi les bêtes.', '家 (jiā, home, family) shows a pig 豕 under a roof 宀: in ancient China, a house also sheltered the animals.'),
      ('爸 (bà, papa) et 妈 (mā, maman) associent un sens et un son : 父 (père) + 巴 (ba), 女 (femme) + 马 (ma).', '爸 (bà, dad) and 妈 (mā, mum) combine a meaning and a sound: 父 (father) + 巴 (ba), 女 (woman) + 马 (ma).'),
    ], [
      H('jia', '家', 'jiā', ('maison, famille', 'home, family'), 10), H('ba', '爸', 'bà', ('papa', 'dad'), 8), H('ma', '妈', 'mā', ('maman', 'mum'), 6), H('er-child', '儿', 'ér', ('fils, enfant', 'son, child'), 2),
      H('you', '有', 'yǒu', ('avoir, il y a', 'to have, there is'), 6), H('mei', '没', 'méi', ('ne pas (avoir)', 'not (have)'), 7), H('de', '的', 'de', ('particule de possession', 'possessive particle'), 8), H('ge', '个', 'gè', ('classificateur général', 'general measure word'), 3),
    ]),
    L('zh-family', ('La famille et 的', 'Family and 的'), ('Présenter sa famille et dire à qui est une chose.', 'Introduce your family and say whose something is.'), 9, [
        ('的 relie le possesseur à l’objet : 我的书 (mon livre), 老师的名字 (le nom du professeur). Avec la famille et les proches, on l’omet souvent : 我妈妈, 我朋友.', '的 links the owner to the object: 我的书 (my book), 老师的名字 (the teacher’s name). With family and close people it is often left out: 我妈妈, 我朋友.'),
        ('Famille : 爸爸 (papa), 妈妈 (maman), 儿子 (fils), 女儿 (fille). 谁 (shéi) = qui : 他是谁？', 'Family: 爸爸 (dad), 妈妈 (mum), 儿子 (son), 女儿 (daughter). 谁 (shéi) = who: 他是谁？'),
      ], [
        ZG('de', '的', 'de', ('de (possession) : 我的 = mon, ma', 'possession: 我的 = my')),
        Z('jia', '家', 'jiā', ('maison, famille', 'home, family')),
        Z('baba', '爸爸', 'bàba', ('papa', 'dad')),
        Z('mama', '妈妈', 'māma', ('maman', 'mum')),
        Z('erzi', '儿子', 'érzi', ('fils', 'son')),
        Z('nver', '女儿', 'nǚ’ér', ('fille (enfant)', 'daughter')),
        Z('shei', '谁', 'shéi', ('qui', 'who')),
      ], [
        x('这是我的家。', 'Zhè shì wǒ de jiā.', 'Voici ma maison.', 'This is my home.'),
        x('她是谁？——她是我女儿。', 'Tā shì shéi? — Tā shì wǒ nǚ’ér.', 'Qui est-elle ? — C’est ma fille.', 'Who is she? — She is my daughter.'),
      ], [
        FB(COMPLETE, '这是老师＿书。', ['的', '吗', '个'], '的', ('Possession : 老师的书.', 'Possession: 老师的书.'), ('C’est le livre du professeur.', 'This is the teacher’s book.')),
        FB(COMPLETE, '他是＿？——他是我爸爸。', ['谁', '什么', '几'], '谁', ('Pour une personne : 谁.', 'For a person: 谁.'), ('Qui est-ce ? — C’est mon père.', 'Who is he? — He is my father.')),
        SO(ORDER('C’est mon fils.', 'He is my son.'), ['他', '是', '我', '儿子。'], ('Sujet + 是 + 我 + membre de la famille.', 'Subject + 是 + 我 + family member.')),
        TF('她是我妈妈。', ('La personne présente sa mère.', 'The speaker is introducing their mother.'), VRAI, ('妈妈 = maman.', '妈妈 = mum.')),
      ]),
  ]),
  CH('hsk1-w4-c2', ('Compter ce que l’on a', 'Counting what you have'), [
    L('zh-you', ('Avoir : 有, 没有 et les classificateurs', 'To have: 有, 没有 and measure words'), ('Dire ce que l’on a et compter avec 个 et 口.', 'Say what you have and count with 个 and 口.'), 10, [
        ('有 = avoir, il y a. Sa négation est toujours 没有 (jamais 不有) : 我没有猫.', '有 = to have, there is. Its negation is always 没有 (never 不有): 我没有猫.'),
        ('Entre un nombre et un nom, il faut un classificateur : 一个人, 三个朋友. Pour les membres d’une famille : 我家有四口人 (nous sommes quatre à la maison).', 'Between a number and a noun you need a measure word: 一个人, 三个朋友. For family members: 我家有四口人 (there are four of us at home).'),
        ('Devant un classificateur, deux se dit 两 (liǎng) : 两个人. 二 sert pour compter (一、二、三) et dans les nombres (十二).', 'Before a measure word, two is 两 (liǎng): 两个人. 二 is used for counting (一、二、三) and in numbers (十二).'),
      ], [
        ZG('you', '有 / 没有', 'yǒu / méiyǒu', ('avoir, il y a / ne pas avoir', 'to have, there is / not to have')),
        ZG('ge', '数字 + 个 + 名词', None, ('nombre + classificateur + nom', 'number + measure word + noun')),
        Z('ge', '个', 'gè', ('classificateur général', 'general measure word')),
        Z('kou', '口', 'kǒu', ('classificateur des membres d’une famille', 'measure word for family members')),
        Z('gou', '狗', 'gǒu', ('chien', 'dog')),
        Z('mao', '猫', 'māo', ('chat', 'cat')),
        Z('meiyou', '没有', 'méiyǒu', ('ne pas avoir, il n’y a pas', 'not have, there is not')),
      ], [
        x('我家有三口人：爸爸、妈妈和我。', 'Wǒ jiā yǒu sān kǒu rén: bàba, māma hé wǒ.', 'Nous sommes trois à la maison : papa, maman et moi.', 'There are three people in my family: dad, mum and me.'),
        x('我有一个狗，我没有猫。', 'Wǒ yǒu yí ge gǒu, wǒ méiyǒu māo.', 'J’ai un chien, je n’ai pas de chat.', 'I have a dog, I don’t have a cat.'),
      ], [
        FB(COMPLETE, '我＿有猫。', ['没', '不', '吗'], '没', ('La négation de 有 est toujours 没有.', 'The negation of 有 is always 没有.'), ('Je n’ai pas de chat.', 'I don’t have a cat.')),
        FB(COMPLETE, '我有三＿朋友。', ['个', '口', '岁'], '个', ('Le classificateur général 个.', 'The general measure word 个.'), ('J’ai trois amis.', 'I have three friends.')),
        FB(COMPLETE, '你家有几＿人？', ['口', '个', '号'], '口', ('Pour compter les membres d’une famille : 口.', 'To count family members: 口.'), ('Combien êtes-vous dans ta famille ?', 'How many people are there in your family?')),
        TF('我有两个儿子。', ('La personne a deux fils.', 'The speaker has two sons.'), VRAI, ('两个 = deux (devant un classificateur).', '两个 = two (before a measure word).')),
      ]),
    L('zh-this-that', ('Ceci, cela, lequel : 这、那、哪', 'This, that, which: 这, 那, 哪'), ('Montrer et demander une chose avec 这, 那 et 哪.', 'Point at and ask about something with 这, 那 and 哪.'), 8, [
        ('这 (zhè) = ceci, proche ; 那 (nà) = cela, loin ; 哪 (nǎ) = lequel ? Avec un classificateur : 这个, 那个, 哪个.', '这 (zhè) = this, near; 那 (nà) = that, far; 哪 (nǎ) = which? With a measure word: 这个, 那个, 哪个.'),
        ('这是什么？= qu’est-ce que c’est ? Attention aux tons : nà (cela) et nǎ (lequel) ne diffèrent que par le ton.', '这是什么？= what is this? Watch the tones: nà (that) and nǎ (which) differ only in tone.'),
      ], [
        Z('zhe', '这', 'zhè', ('ceci, ce', 'this')),
        Z('na-that', '那', 'nà', ('cela, ce… là', 'that')),
        Z('na-which', '哪', 'nǎ', ('lequel, quel', 'which (one)')),
        Z('shu', '书', 'shū', ('livre', 'book')),
        Z('beizi', '杯子', 'bēizi', ('verre, tasse', 'glass, cup')),
        Z('dongxi', '东西', 'dōngxi', ('chose, objet', 'thing, object')),
      ], [
        x('这是什么？——这是我的书。', 'Zhè shì shénme? — Zhè shì wǒ de shū.', 'Qu’est-ce que c’est ? — C’est mon livre.', 'What is this? — It’s my book.'),
        x('哪个杯子是你的？——那个。', 'Nǎ ge bēizi shì nǐ de? — Nà ge.', 'Quel verre est à toi ? — Celui-là.', 'Which cup is yours? — That one.'),
      ], [
        FB(COMPLETE, '＿是什么？——这是杯子。', ['这', '哪', '谁'], '这', ('Ce qui est proche : 这.', 'Something near: 这.'), ('Qu’est-ce que c’est ? — C’est un verre.', 'What is this? — It’s a cup.')),
        FB(COMPLETE, '你是＿国人？', ['哪', '那', '这'], '哪', ('Pour demander lequel : 哪 (3e ton).', 'To ask which: 哪 (3rd tone).'), ('De quel pays es-tu ?', 'Which country are you from?')),
        DC(ANSWER, [('李月', '这是谁的书？')], ('Li Yue tient ton livre.', 'Li Yue is holding your book.'), ['是我的。', '是这个。', '我没有。'], '是我的。', ('À qui ? → 我的 (à moi).', 'Whose? → 我的 (mine).')),
        TF('那个东西是我的。', ('La chose là-bas est à moi.', 'That thing over there is mine.'), VRAI, ('那个 = celui-là, 我的 = à moi.', '那个 = that one, 我的 = mine.')),
      ]),
  ])])

# ═════════════════════════ Royaume 5 : Han, le marché de Xinzheng ═════════════════════════
W5 = WORLD('hsk1-w5', ('Le marché de Xinzheng', 'The Xinzheng market'), REGION,
  ('Faire ses courses : acheter, demander un prix, compter l’argent, manger, boire, dire ce que l’on veut.', 'Go shopping: buy, ask a price, count money, eat, drink, say what you would like.'),
  (('Le Pixiu dévoreur d’or', 'The Gold-Eating Pixiu'), '貔', ('Au marché de Xinzheng, le Pixiu avale toutes les pièces sans jamais les rendre. Marchande au juste prix et il crachera l’or des marchands.', 'At the Xinzheng market, the Pixiu swallows every coin and never gives any back. Bargain at the right price and it will spit out the merchants’ gold.')),
  [CH('hsk1-w5-c1', ('Combien ça coûte ?', 'How much is it?'), [
    HL('zh-hz-market', ('Les caractères du marché : 买 钱 块 多 少 东 西 些', 'Market characters: 买 钱 块 多 少 东 西 些'), ('Reconnaître les caractères des achats.', 'Recognise the characters of shopping.'), [
      ('钱 (qián, argent) porte la clé du métal 钅 : les premières monnaies étaient en bronze. 买 (mǎi, acheter) et 卖 (mài, vendre) ne diffèrent que d’un trait et d’un ton.', '钱 (qián, money) has the metal radical 钅: the first coins were bronze. 买 (mǎi, to buy) and 卖 (mài, to sell) differ by just one stroke and one tone.'),
      ('东 (dōng, est) + 西 (xī, ouest) = 东西 (dōngxi), « les choses » : tout ce qu’on trouve d’est en ouest.', '东 (dōng, east) + 西 (xī, west) = 东西 (dōngxi), “things”: everything found from east to west.'),
    ], [
      H('mai', '买', 'mǎi', ('acheter', 'to buy'), 6), H('qian', '钱', 'qián', ('argent', 'money'), 10), H('kuai', '块', 'kuài', ('morceau ; yuan (oral)', 'piece; yuan (spoken)'), 7), H('duo', '多', 'duō', ('beaucoup, nombreux', 'many, much'), 6),
      H('shao', '少', 'shǎo', ('peu', 'few, little'), 4), H('dong', '东', 'dōng', ('est', 'east'), 5), H('xi', '西', 'xī', ('ouest', 'west'), 6), H('xie', '些', 'xiē', ('quelques', 'some'), 8),
    ]),
    L('zh-shopping', ('Acheter : 买、多少钱、块', 'Buying: 买, 多少钱, 块'), ('Demander un prix et l’annoncer en yuans.', 'Ask a price and give it in yuan.'), 9, [
        ('多少钱？= combien ça coûte ? On répond avec 块 (kuài), le mot courant pour « yuan » : 十块 (10 yuans), 三块五 (3,50 yuans).', '多少钱？= how much is it? The answer uses 块 (kuài), the everyday word for “yuan”: 十块 (10 yuan), 三块五 (3.50 yuan).'),
        ('多少 (duōshao) demande une quantité quelconque, souvent grande ; 几 attend un petit nombre (moins de dix) et un classificateur.', '多少 (duōshao) asks about any quantity, often a large one; 几 expects a small number (under ten) and a measure word.'),
        ('一些 (yìxiē) = quelques, un peu de : 买一些水果 (acheter quelques fruits).', '一些 (yìxiē) = some, a few: 买一些水果 (buy some fruit).'),
      ], [
        ZG('duoshao', '多少钱？', 'duōshao qián?', ('combien ça coûte ?', 'how much is it?')),
        Z('mai', '买', 'mǎi', ('acheter', 'to buy')),
        Z('qian', '钱', 'qián', ('argent', 'money')),
        Z('kuai', '块', 'kuài', ('yuan (oral)', 'yuan (spoken)')),
        Z('duoshao', '多少', 'duōshao', ('combien (quantité)', 'how much, how many')),
        Z('shangdian', '商店', 'shāngdiàn', ('magasin', 'shop')),
        Z('yixie', '一些', 'yìxiē', ('quelques, un peu de', 'some, a few')),
        Z('shao', '少', 'shǎo', ('peu', 'few, little')),
      ], [
        x('这个杯子多少钱？——二十块。', 'Zhè ge bēizi duōshao qián? — Èrshí kuài.', 'Combien coûte ce verre ? — Vingt yuans.', 'How much is this cup? — Twenty yuan.'),
        x('我去商店买一些东西。', 'Wǒ qù shāngdiàn mǎi yìxiē dōngxi.', 'Je vais au magasin acheter quelques affaires.', 'I’m going to the shop to buy a few things.'),
      ], [
        FB(COMPLETE, '这本书多少＿？', ['钱', '块', '几'], '钱', ('Le prix : 多少钱？', 'The price: 多少钱？'), ('Combien coûte ce livre ?', 'How much is this book?')),
        FB(COMPLETE, '五十＿。', ['块', '个', '口'], '块', ('Les yuans à l’oral : 块.', 'Yuan in speech: 块.'), ('Cinquante yuans.', 'Fifty yuan.')),
        DC(ANSWER, [('商店', '你好！你买什么？')], ('Le marchand te demande ce que tu achètes (des verres).', 'The shopkeeper asks what you are buying (cups).'), ['我买杯子。', '我是杯子。', '杯子多少？'], '我买杯子。', ('Sujet + 买 + objet.', 'Subject + 买 + object.')),
        TF('苹果三块五。', ('Les pommes coûtent 3,50 yuans.', 'The apples cost 3.50 yuan.'), VRAI, ('三块五 = 3 yuans 50.', '三块五 = 3 yuan 50.')),
      ]),
  ]),
  CH('hsk1-w5-c2', ('À l’auberge', 'At the inn'), [
    L('zh-food', ('Manger et boire : 吃、喝、想', 'Eating and drinking: 吃, 喝, 想'), ('Dire ce que l’on veut manger ou boire avec 想.', 'Say what you would like to eat or drink with 想.'), 9, [
        ('想 + verbe = avoir envie de, vouloir : 我想喝茶 (je voudrais boire du thé). Négation : 不想.', '想 + verb = to feel like, to want: 我想喝茶 (I would like to drink tea). Negation: 不想.'),
        ('吃 (chī) = manger : 吃米饭 (manger du riz), 吃菜 (manger des plats). 喝 (hē) = boire : 喝水, 喝茶.', '吃 (chī) = to eat: 吃米饭 (eat rice), 吃菜 (eat dishes). 喝 (hē) = to drink: 喝水, 喝茶.'),
        ('L’ordre est toujours sujet + verbe + complément, comme en français : 我吃苹果.', 'The order is always subject + verb + object, as in English: 我吃苹果.'),
      ], [
        ZG('xiang', '想 + 动词', 'xiǎng', ('avoir envie de, vouloir (faire)', 'to want to, would like to')),
        Z('chi', '吃', 'chī', ('manger', 'to eat')),
        Z('he', '喝', 'hē', ('boire', 'to drink')),
        Z('xiang', '想', 'xiǎng', ('vouloir, penser', 'to want, to think')),
        Z('cha', '茶', 'chá', ('thé', 'tea')),
        Z('shui', '水', 'shuǐ', ('eau', 'water')),
        Z('mifan', '米饭', 'mǐfàn', ('riz (cuit)', 'rice (cooked)')),
        Z('cai', '菜', 'cài', ('plat, légume', 'dish, vegetable')),
        Z('pingguo', '苹果', 'píngguǒ', ('pomme', 'apple')),
        Z('shuiguo', '水果', 'shuǐguǒ', ('fruit', 'fruit')),
      ], [
        x('你想喝什么？——我想喝茶。', 'Nǐ xiǎng hē shénme? — Wǒ xiǎng hē chá.', 'Que veux-tu boire ? — Je voudrais du thé.', 'What would you like to drink? — I’d like some tea.'),
        x('我不想吃米饭，我想吃水果。', 'Wǒ bù xiǎng chī mǐfàn, wǒ xiǎng chī shuǐguǒ.', 'Je n’ai pas envie de riz, je voudrais des fruits.', 'I don’t want rice, I’d like some fruit.'),
      ], [
        FB(COMPLETE, '我想＿水。', ['喝', '吃', '买'], '喝', ('On boit l’eau : 喝水.', 'You drink water: 喝水.'), ('Je voudrais boire de l’eau.', 'I’d like to drink some water.')),
        FB(COMPLETE, '你＿吃什么？', ['想', '是', '有'], '想', ('Vouloir faire : 想 + verbe.', 'Want to do: 想 + verb.'), ('Que veux-tu manger ?', 'What would you like to eat?')),
        SO(ORDER('Je ne veux pas manger de pomme.', 'I don’t want to eat an apple.'), ['我', '不想', '吃', '苹果。'], ('Sujet + 不想 + verbe + objet.', 'Subject + 不想 + verb + object.')),
        TF('他想喝茶。', ('Il veut manger du riz.', 'He wants to eat rice.'), FAUX, ('喝茶 = boire du thé.', '喝茶 = drink tea.')),
      ]),
    L('zh-tai', ('Trop, très : 太…了 et 很', 'Too, very: 太…了 and 很'), ('Donner son avis sur un prix ou un plat.', 'Give your opinion on a price or a dish.'), 8, [
        ('太 + adjectif + 了 = trop, vraiment : 太贵了？Non ! Au HSK 1 on dit plutôt 太多了 (c’est trop), 太好了 (génial !), 太少了 (c’est trop peu).', '太 + adjective + 了 = too, really: 太多了 (that’s too much), 太好了 (great!), 太少了 (too little).'),
        ('Un adjectif s’emploie sans 是 : 这个苹果很大 (cette pomme est grande). 很 (hěn) se met presque toujours devant, même sans vouloir dire « très ».', 'An adjective is used without 是: 这个苹果很大 (this apple is big). 很 (hěn) almost always goes in front, even without really meaning “very”.'),
      ], [
        ZG('tai-le', '太…了', 'tài… le', ('trop…, vraiment… !', 'too…, really…!')),
        ZG('hen', '很 + 形容词', 'hěn', ('(très) + adjectif, sans 是', '(very) + adjective, without 是')),
        Z('tai', '太', 'tài', ('trop', 'too (much)')),
        Z('hen', '很', 'hěn', ('très', 'very')),
        Z('hao-good', '好', 'hǎo', ('bien, bon', 'good, well')),
        Z('xiao', '小', 'xiǎo', ('petit', 'small')),
      ], [
        x('五十块？太多了！', 'Wǔshí kuài? Tài duō le!', 'Cinquante yuans ? C’est trop !', 'Fifty yuan? That’s too much!'),
        x('这个菜很好。', 'Zhè ge cài hěn hǎo.', 'Ce plat est très bon.', 'This dish is very good.'),
      ], [
        FB(COMPLETE, '太好＿！', ['了', '吗', '的'], '了', ('Exclamation : 太 + adjectif + 了.', 'Exclamation: 太 + adjective + 了.'), ('Génial !', 'Great!')),
        FB(COMPLETE, '这个杯子＿小。', ['很', '是', '有'], '很', ('Adjectif sans 是 : 很 + adjectif.', 'Adjective without 是: 很 + adjective.'), ('Ce verre est (très) petit.', 'This cup is (very) small.')),
        DC(ANSWER, [('商店', '这个一百块。')], ('Le marchand demande 100 yuans pour un verre.', 'The shopkeeper asks 100 yuan for a cup.'), ['太多了！', '太好了！', '很小。'], '太多了！', ('Le prix est trop élevé : 太多了.', 'The price is too high: 太多了.')),
        TF('水果太少了。', ('Il y a trop peu de fruits.', 'There is too little fruit.'), VRAI, ('太少了 = trop peu.', '太少了 = too little.')),
      ]),
  ])])

# ═════════════════════════ Royaume 6 : Wei, une journée au palais ═════════════════════════
W6 = WORLD('hsk1-w6', ('Une journée au palais de Wei', 'A day at the palace of Wei'), REGION,
  ('L’heure, les moments de la journée, les activités quotidiennes et l’action accomplie avec 了.', 'Telling the time, parts of the day, daily activities and completed actions with 了.'),
  (('Le Bifang, oiseau de feu', 'The Bifang Fire Bird'), '毕', ('Le Bifang, oiseau à une seule patte qui fait naître le feu, a déréglé toutes les clepsydres du palais de Wei. Donne l’heure juste pour éteindre ses flammes.', 'The Bifang, a one-legged bird that kindles fire, has thrown every water clock in the palace of Wei out of order. Tell the right time to put out its flames.')),
  [CH('hsk1-w6-c1', ('Quelle heure est-il ?', 'What time is it?'), [
    HL('zh-hz-day', ('Les caractères de la journée : 点 分 午 时 现 在 看 书', 'Characters of the day: 点 分 午 时 现 在 看 书'), ('Reconnaître les caractères de l’heure et des activités.', 'Recognise the characters of time and activities.'), [
      ('点 (diǎn, point, heure) et 分 (fēn, minute) donnent l’heure : 三点十分 = 3 h 10. 午 (wǔ) désigne midi : 上午 (le matin), 中午 (midi), 下午 (l’après-midi).', '点 (diǎn, dot, o’clock) and 分 (fēn, minute) tell the time: 三点十分 = 3:10. 午 (wǔ) means noon: 上午 (morning), 中午 (noon), 下午 (afternoon).'),
      ('看 (kàn, regarder) montre une main 手 au-dessus d’un œil 目, comme pour se protéger du soleil en regardant au loin.', '看 (kàn, to look) shows a hand 手 above an eye 目, as if shading your eyes to look far away.'),
    ], [
      H('dian', '点', 'diǎn', ('point, heure', 'dot, o’clock'), 9), H('fen', '分', 'fēn', ('minute, diviser', 'minute, to divide'), 4), H('wu-noon', '午', 'wǔ', ('midi', 'noon'), 4), H('shi-time', '时', 'shí', ('temps, heure', 'time, hour'), 7),
      H('xian', '现', 'xiàn', ('présent, actuel', 'present, current'), 8), H('zai', '在', 'zài', ('être à, se trouver', 'to be at'), 6), H('kan', '看', 'kàn', ('regarder, lire', 'to look, to read'), 9), H('shu', '书', 'shū', ('livre', 'book'), 4),
    ]),
    L('zh-time', ('L’heure : 点、分、现在', 'Telling the time: 点, 分, 现在'), ('Demander et dire l’heure, situer une action dans la journée.', 'Ask and tell the time, place an action in the day.'), 9, [
        ('现在几点？= quelle heure est-il ? Réponse : 现在八点 (il est 8 h), 八点二十分 (8 h 20). 分 peut s’omettre : 八点二十.', '现在几点？= what time is it? Answer: 现在八点 (it’s 8 o’clock), 八点二十分 (8:20). 分 can be dropped: 八点二十.'),
        ('Le moment se place avant le verbe, jamais à la fin : 我下午三点去 (j’y vais à 15 h). On peut aussi le mettre en tête : 下午三点我去.', 'The time goes before the verb, never at the end: 我下午三点去 (I’m going at 3 p.m.). It can also go first: 下午三点我去.'),
        ('时候 (shíhou) = moment : 什么时候？= quand ? 你什么时候来？(quand viens-tu ?)', '时候 (shíhou) = moment: 什么时候？= when? 你什么时候来？(when are you coming?)'),
      ], [
        ZG('time-before-verb', '时间 + 动词', None, ('le moment se place avant le verbe', 'the time goes before the verb')),
        Z('xianzai', '现在', 'xiànzài', ('maintenant', 'now')),
        Z('dian', '点', 'diǎn', ('heure(s) pile', 'o’clock')),
        Z('fenzhong', '分钟', 'fēnzhōng', ('minute (durée)', 'minute (duration)')),
        Z('shangwu', '上午', 'shàngwǔ', ('matin', 'morning')),
        Z('zhongwu', '中午', 'zhōngwǔ', ('midi', 'noon')),
        Z('xiawu', '下午', 'xiàwǔ', ('après-midi', 'afternoon')),
        Z('shihou', '时候', 'shíhou', ('moment', 'time, moment')),
      ], [
        x('现在几点？——现在十点十分。', 'Xiànzài jǐ diǎn? — Xiànzài shí diǎn shí fēn.', 'Quelle heure est-il ? — Il est 10 h 10.', 'What time is it? — It’s ten past ten.'),
        x('我们中午十二点吃饭。', 'Wǒmen zhōngwǔ shí’èr diǎn chī fàn.', 'Nous déjeunons à midi.', 'We have lunch at twelve noon.'),
      ], [
        FB(COMPLETE, '现在几＿？——三点。', ['点', '号', '岁'], '点', ('L’heure : 几点？', 'The time: 几点？'), ('Quelle heure est-il ? — Trois heures.', 'What time is it? — Three o’clock.')),
        FB(COMPLETE, '你什么＿来？', ['时候', '现在', '中午'], '时候', ('Quand ? = 什么时候？', 'When? = 什么时候？'), ('Quand viens-tu ?', 'When are you coming?')),
        SO(ORDER('Je viens à 9 h du matin.', 'I’m coming at 9 a.m.'), ['我', '上午', '九点', '来。'], ('Sujet + moment + verbe.', 'Subject + time + verb.')),
        TF('下午两点', ('Il s’agit de 14 h.', 'This is 2 p.m.'), VRAI, ('下午 = l’après-midi ; 两点 = deux heures.', '下午 = afternoon; 两点 = two o’clock.')),
      ]),
  ]),
  CH('hsk1-w6-c2', ('Les occupations du palais', 'Palace occupations'), [
    L('zh-activities', ('Les activités : 看、读、写、学习、工作', 'Activities: 看, 读, 写, 学习, 工作'), ('Raconter ses activités de la journée.', 'Talk about your daily activities.'), 9, [
        ('看 = regarder, lire des yeux : 看书 (lire un livre), 看电视 (regarder la télé), 看电影 (voir un film). 读 = lire à voix haute, 写 = écrire : 写字 (écrire des caractères).', '看 = to look, to read silently: 看书 (read a book), 看电视 (watch TV), 看电影 (see a film). 读 = to read aloud, 写 = to write: 写字 (write characters).'),
        ('学习 (xuéxí) = étudier ; 工作 (gōngzuò) = travailler, le travail ; 做 (zuò) = faire : 你做什么工作？(quel est ton métier ?)', '学习 (xuéxí) = to study; 工作 (gōngzuò) = to work, a job; 做 (zuò) = to do: 你做什么工作？(what do you do for a living?)'),
        ('在 + verbe = être en train de : 他在看书 (il est en train de lire).', '在 + verb = to be doing: 他在看书 (he is reading).'),
      ], [
        ZG('zai-doing', '在 + 动词', 'zài', ('être en train de', 'to be doing')),
        Z('kan', '看', 'kàn', ('regarder, lire', 'to look, to read')),
        Z('du', '读', 'dú', ('lire (à voix haute)', 'to read (aloud)')),
        Z('xie', '写', 'xiě', ('écrire', 'to write')),
        Z('zi', '字', 'zì', ('caractère (écrit)', 'character (written)')),
        Z('xuexi', '学习', 'xuéxí', ('étudier', 'to study')),
        Z('gongzuo', '工作', 'gōngzuò', ('travailler, travail', 'to work, job')),
        Z('zuo', '做', 'zuò', ('faire', 'to do, to make')),
        Z('dianshi', '电视', 'diànshì', ('télévision', 'television')),
        Z('dianying', '电影', 'diànyǐng', ('film', 'film, movie')),
      ], [
        x('他在看电视。', 'Tā zài kàn diànshì.', 'Il est en train de regarder la télé.', 'He is watching TV.'),
        x('我们在学校学习汉语。', 'Wǒmen zài xuéxiào xuéxí Hànyǔ.', 'Nous étudions le chinois à l’école.', 'We study Chinese at school.'),
      ], [
        FB(COMPLETE, '我在＿书。', ['看', '喝', '坐'], '看', ('Lire un livre : 看书.', 'Read a book: 看书.'), ('Je suis en train de lire.', 'I am reading.')),
        FB(COMPLETE, '你做什么＿？——我是老师。', ['工作', '学习', '电影'], '工作', ('Le métier : 做什么工作？', 'Your job: 做什么工作？'), ('Que fais-tu comme travail ? — Je suis professeur.', 'What do you do? — I am a teacher.')),
        DC(ANSWER, [('妈妈', '你在做什么？')], ('Ta mère te demande ce que tu fais (tu écris des caractères).', 'Your mother asks what you are doing (you are writing characters).'), ['我在写字。', '我想写字。', '我是字。'], '我在写字。', ('在 + verbe : en train de.', '在 + verb: in the middle of doing.')),
        TF('她在看电影。', ('Elle regarde un film.', 'She is watching a film.'), VRAI, ('看电影 = voir un film.', '看电影 = watch a film.')),
      ]),
    L('zh-le', ('C’est fait : 了 et 睡觉、打电话', 'Done: 了, 睡觉 and 打电话'), ('Dire qu’une action a eu lieu avec 了.', 'Say that an action has happened with 了.'), 9, [
        ('了 après le verbe (ou en fin de phrase) indique une action accomplie : 我买了一个杯子 (j’ai acheté un verre), 他去商店了 (il est allé au magasin).', '了 after the verb (or at the end of the sentence) marks a completed action: 我买了一个杯子 (I bought a cup), 他去商店了 (he went to the shop).'),
        ('La négation d’une action passée est 没 (sans 了) : 我没去 (je n’y suis pas allé).', 'The negation of a past action is 没 (without 了): 我没去 (I didn’t go).'),
        ('Verbes de la journée : 睡觉 (shuìjiào, dormir, se coucher), 打电话 (dǎ diànhuà, téléphoner), 回家 (rentrer à la maison).', 'Daily verbs: 睡觉 (shuìjiào, to sleep, go to bed), 打电话 (dǎ diànhuà, to make a phone call), 回家 (go home).'),
      ], [
        ZG('le', '动词 + 了', 'le', ('action accomplie', 'completed action')),
        ZG('mei-past', '没 + 动词', 'méi', ('ne pas avoir fait (passé)', 'did not (past)')),
        Z('shuijiao', '睡觉', 'shuìjiào', ('dormir, se coucher', 'to sleep, to go to bed')),
        Z('da-dianhua', '打电话', 'dǎ diànhuà', ('téléphoner', 'to make a phone call')),
        Z('hui', '回', 'huí', ('rentrer, revenir', 'to return, to go back')),
        Z('fanguan', '饭馆', 'fànguǎn', ('restaurant', 'restaurant')),
      ], [
        x('昨天我给妈妈打电话了。', 'Zuótiān wǒ gěi māma dǎ diànhuà le.', 'Hier, j’ai téléphoné à ma mère.', 'Yesterday I called my mother.'),
        x('你昨天几点睡觉的？——十一点。', 'Nǐ zuótiān jǐ diǎn shuìjiào de? — Shíyī diǎn.', 'À quelle heure t’es-tu couché hier ? — À 23 h.', 'What time did you go to bed yesterday? — At eleven.'),
      ], [
        FB(COMPLETE, '我买＿两个苹果。', ['了', '吗', '的'], '了', ('Action accomplie : verbe + 了.', 'Completed action: verb + 了.'), ('J’ai acheté deux pommes.', 'I bought two apples.')),
        FB(COMPLETE, '昨天我＿去饭馆。', ['没', '不', '了'], '没', ('Ne pas avoir fait : 没 + verbe (sans 了).', 'Did not do: 没 + verb (without 了).'), ('Hier, je ne suis pas allé au restaurant.', 'Yesterday I didn’t go to the restaurant.')),
        SO(ORDER('Il est rentré à la maison.', 'He went home.'), ['他', '回家', '了。'], ('了 en fin de phrase : c’est fait.', '了 at the end of the sentence: it has happened.')),
        TF('我昨天没睡觉。', ('La personne a bien dormi hier.', 'The speaker slept well yesterday.'), FAUX, ('没睡觉 = n’a pas dormi.', '没睡觉 = did not sleep.')),
      ]),
  ])])

# ═════════════════════════ Royaume 7 : Zhao, les routes de Handan ═════════════════════════
W7 = WORLD('hsk1-w7', ('Les routes de Handan', 'The roads of Handan'), REGION,
  ('Se situer avec 在, demander où se trouve un lieu, aller, venir, prendre un moyen de transport.', 'Say where things are with 在, ask where a place is, go, come, take a means of transport.'),
  (('Le Xiangliu à neuf têtes', 'The Nine-Headed Xiangliu'), '柳', ('Le Xiangliu, serpent à neuf têtes, empoisonne les routes du royaume de Zhao. Chaque tête montre une direction différente : trouve la bonne pour arriver à Handan.', 'The Xiangliu, a nine-headed serpent, poisons the roads of the state of Zhao. Each head points a different way: find the right one to reach Handan.')),
  [CH('hsk1-w7-c1', ('Où est-ce ?', 'Where is it?'), [
    HL('zh-hz-places', ('Les caractères des lieux : 去 来 回 坐 车 前 后 里', 'Place characters: 去 来 回 坐 车 前 后 里'), ('Reconnaître les caractères du déplacement.', 'Recognise the characters of moving around.'), [
      ('车 (chē, char, voiture) est le dessin d’un char vu de dessus : l’essieu et les deux roues. Il se retrouve dans 火车 (train) et 出租车 (taxi).', '车 (chē, cart, car) is a drawing of a chariot seen from above: the axle and two wheels. It appears in 火车 (train) and 出租车 (taxi).'),
      ('去 (qù) = aller (s’éloigner), 来 (lái) = venir (vers celui qui parle), 回 (huí) = revenir : deux carrés emboîtés, comme un retour au point de départ.', '去 (qù) = to go (away), 来 (lái) = to come (towards the speaker), 回 (huí) = to return: two nested squares, like a return to the starting point.'),
    ], [
      H('qu', '去', 'qù', ('aller', 'to go'), 5), H('lai', '来', 'lái', ('venir', 'to come'), 7), H('hui', '回', 'huí', ('rentrer, revenir', 'to return, to go back'), 6), H('zuo-sit', '坐', 'zuò', ('s’asseoir, prendre (un transport)', 'to sit, to take (transport)'), 7),
      H('che', '车', 'chē', ('voiture, char', 'car, cart'), 4), H('qian-front', '前', 'qián', ('devant, avant', 'front, before'), 9), H('hou', '后', 'hòu', ('derrière, après', 'back, after'), 6), H('li', '里', 'lǐ', ('dedans, intérieur', 'inside'), 7),
    ]),
    L('zh-zai', ('Se trouver : 在、哪儿、这儿、那儿', 'Being somewhere: 在, 哪儿, 这儿, 那儿'), ('Dire où se trouve une personne ou une chose.', 'Say where a person or thing is.'), 9, [
        ('Sujet + 在 + lieu = se trouver à : 我在家 (je suis à la maison), 书在桌子上 (le livre est sur la table).', 'Subject + 在 + place = to be at: 我在家 (I am at home), 书在桌子上 (the book is on the table).'),
        ('哪儿 (nǎr) = où ? 这儿 (zhèr) = ici, 那儿 (nàr) = là-bas : 你在哪儿？——我在这儿.', '哪儿 (nǎr) = where? 这儿 (zhèr) = here, 那儿 (nàr) = there: 你在哪儿？——我在这儿.'),
        ('La position se met après le nom : 桌子上 (sur la table), 桌子下 (sous la table), 杯子里 (dans le verre), 学校前面 (devant l’école), 后面 (derrière).', 'The position comes after the noun: 桌子上 (on the table), 桌子下 (under the table), 杯子里 (in the cup), 学校前面 (in front of the school), 后面 (behind).'),
      ], [
        ZG('zai-place', '在 + 地点', 'zài', ('se trouver à (un lieu)', 'to be at (a place)')),
        ZG('noun-position', '名词 + 上 / 下 / 里', None, ('sur / sous / dans (après le nom)', 'on / under / in (after the noun)')),
        Z('zai', '在', 'zài', ('être à, se trouver', 'to be at, to be in')),
        Z('nar', '哪儿', 'nǎr', ('où', 'where')),
        Z('zher', '这儿', 'zhèr', ('ici', 'here')),
        Z('nar-there', '那儿', 'nàr', ('là-bas', 'there')),
        Z('zhuozi', '桌子', 'zhuōzi', ('table', 'table')),
        Z('yizi', '椅子', 'yǐzi', ('chaise', 'chair')),
        Z('qianmian', '前面', 'qiánmiàn', ('devant', 'in front')),
        Z('houmian', '后面', 'hòumiàn', ('derrière', 'behind')),
      ], [
        x('你妈妈在哪儿？——她在家。', 'Nǐ māma zài nǎr? — Tā zài jiā.', 'Où est ta mère ? — Elle est à la maison.', 'Where is your mother? — She is at home.'),
        x('猫在椅子下面。', 'Māo zài yǐzi xiàmiàn.', 'Le chat est sous la chaise.', 'The cat is under the chair.'),
      ], [
        FB(COMPLETE, '你在＿？——我在学校。', ['哪儿', '那儿', '这儿'], '哪儿', ('Où ? = 哪儿 (3e ton).', 'Where? = 哪儿 (3rd tone).'), ('Où es-tu ? — Je suis à l’école.', 'Where are you? — I am at school.')),
        FB(COMPLETE, '杯子在桌子＿。', ['上', '前', '在'], '上', ('Sur la table : 桌子上.', 'On the table: 桌子上.'), ('Le verre est sur la table.', 'The cup is on the table.')),
        SO(ORDER('Mon père est au restaurant.', 'My father is at the restaurant.'), ['我爸爸', '在', '饭馆。'], ('Sujet + 在 + lieu.', 'Subject + 在 + place.')),
        TF('狗在桌子后面。', ('Le chien est devant la table.', 'The dog is in front of the table.'), FAUX, ('后面 = derrière ; devant = 前面.', '后面 = behind; in front = 前面.')),
      ]),
  ]),
  CH('hsk1-w7-c2', ('En route', 'On the way'), [
    L('zh-transport', ('Aller et venir : 去、来、坐', 'Going and coming: 去, 来, 坐'), ('Dire où l’on va et comment.', 'Say where you are going and how.'), 10, [
        ('去 + lieu = aller à : 我去北京 (je vais à Pékin). 来 + lieu = venir : 你来我家吧 (viens chez moi).', '去 + place = to go to: 我去北京 (I’m going to Beijing). 来 + place = to come: 你来我家吧 (come to my place).'),
        ('Le moyen de transport se place avant le verbe : 坐 + transport + 去 + lieu. 我坐出租车去医院 (je vais à l’hôpital en taxi).', 'The means of transport goes before the verb: 坐 + transport + 去 + place. 我坐出租车去医院 (I go to the hospital by taxi).'),
        ('Lieux : 学校 (école), 医院 (hôpital), 火车站 (gare). Transports : 飞机 (avion), 火车 (train), 出租车 (taxi).', 'Places: 学校 (school), 医院 (hospital), 火车站 (railway station). Transport: 飞机 (plane), 火车 (train), 出租车 (taxi).'),
      ], [
        ZG('zuo-qu', '坐 + 交通 + 去 + 地点', None, ('aller quelque part en (transport)', 'go somewhere by (transport)')),
        Z('qu', '去', 'qù', ('aller', 'to go')),
        Z('lai', '来', 'lái', ('venir', 'to come')),
        Z('zuo-sit', '坐', 'zuò', ('s’asseoir ; prendre (un transport)', 'to sit; to take (transport)')),
        Z('xuexiao', '学校', 'xuéxiào', ('école', 'school')),
        Z('yiyuan', '医院', 'yīyuàn', ('hôpital', 'hospital')),
        Z('yisheng', '医生', 'yīshēng', ('médecin', 'doctor')),
        Z('huochezhan', '火车站', 'huǒchēzhàn', ('gare', 'railway station')),
        Z('feiji', '飞机', 'fēijī', ('avion', 'plane')),
        Z('chuzuche', '出租车', 'chūzūchē', ('taxi', 'taxi')),
      ], [
        x('明天我坐飞机去北京。', 'Míngtiān wǒ zuò fēijī qù Běijīng.', 'Demain, je vais à Pékin en avion.', 'Tomorrow I’m flying to Beijing.'),
        x('医生在医院工作。', 'Yīshēng zài yīyuàn gōngzuò.', 'Le médecin travaille à l’hôpital.', 'The doctor works at the hospital.'),
      ], [
        FB(COMPLETE, '我＿出租车去火车站。', ['坐', '在', '来'], '坐', ('Prendre un transport : 坐.', 'Take a means of transport: 坐.'), ('Je vais à la gare en taxi.', 'I go to the station by taxi.')),
        FB(COMPLETE, '你什么时候＿我家？', ['来', '坐', '在'], '来', ('Vers celui qui parle : 来.', 'Towards the speaker: 来.'), ('Quand viens-tu chez moi ?', 'When are you coming to my place?')),
        SO(ORDER('Je vais à l’école en taxi.', 'I go to school by taxi.'), ['我', '坐出租车', '去', '学校。'], ('坐 + transport, puis 去 + lieu.', '坐 + transport, then 去 + place.')),
        DC(ANSWER, [('大卫', '你去哪儿？')], ('David te demande où tu vas (à l’hôpital).', 'David asks where you are going (to the hospital).'), ['我去医院。', '我在医院。', '医院在哪儿？'], '我去医院。', ('Aller à : 去 + lieu.', 'Go to: 去 + place.')),
      ]),
  ])])

# ═════════════════════════ Royaume 8 : Qin, les portes de Xianyang ═════════════════════════
W8 = WORLD('hsk1-w8', ('Les portes de Xianyang', 'The gates of Xianyang'), REGION,
  ('Le temps qu’il fait, ce que l’on aime, ce que l’on sait faire avec 会 et 能, et les premières conversations.', 'The weather, what you like, what you can do with 会 and 能, and the first conversations.'),
  (('Le Zhulong, dragon-chandelle', 'The Zhulong Candle Dragon'), '烛', ('Aux portes de Xianyang veille le Zhulong : quand il ouvre les yeux, c’est le jour ; quand il les ferme, la nuit. Parle-lui du temps, de ce que tu aimes et de ce que tu sais faire, et il t’ouvrira la capitale de Qin.', 'At the gates of Xianyang watches the Zhulong: when it opens its eyes it is day, when it closes them it is night. Talk to it about the weather, what you like and what you can do, and it will open the capital of Qin to you.')),
  [CH('hsk1-w8-c1', ('Le temps qu’il fait', 'The weather'), [
    HL('zh-hz-feelings', ('Les caractères du cœur : 爱 喜 欢 会 能 说 听 请', 'Heart characters: 爱 喜 欢 会 能 说 听 请'), ('Reconnaître les caractères des goûts et des capacités.', 'Recognise the characters of likes and abilities.'), [
      ('说 (shuō, parler) et 请 (qǐng, prier, inviter) portent la clé de la parole 讠. 听 (tīng, écouter) porte celle de la bouche 口.', '说 (shuō, to speak) and 请 (qǐng, to ask, to invite) carry the speech radical 讠. 听 (tīng, to listen) carries the mouth radical 口.'),
      ('喜 (xǐ, joie) + 欢 (huān, gaieté) = 喜欢, aimer bien. 爱 (ài) est plus fort : aimer, adorer.', '喜 (xǐ, joy) + 欢 (huān, merriment) = 喜欢, to like. 爱 (ài) is stronger: to love.'),
    ], [
      H('ai', '爱', 'ài', ('aimer, adorer', 'to love'), 10), H('xi-joy', '喜', 'xǐ', ('joie', 'joy'), 12), H('huan', '欢', 'huān', ('gai, joyeux', 'merry, joyful'), 6), H('hui-can', '会', 'huì', ('savoir (faire)', 'can, know how to'), 6),
      H('neng', '能', 'néng', ('pouvoir', 'can, to be able'), 10), H('shuo', '说', 'shuō', ('parler, dire', 'to speak, to say'), 9), H('ting', '听', 'tīng', ('écouter', 'to listen'), 7), H('qing', '请', 'qǐng', ('s’il vous plaît, inviter', 'please, to invite'), 10),
    ]),
    L('zh-weather', ('Le temps : 天气、冷、热、下雨、怎么样', 'The weather: 天气, 冷, 热, 下雨, 怎么样'), ('Parler du temps et demander comment est quelque chose.', 'Talk about the weather and ask what something is like.'), 9, [
        ('怎么样 (zěnmeyàng) = comment est… ? 今天天气怎么样？(quel temps fait-il aujourd’hui ?) Il sert aussi à proposer : 我们去饭馆，怎么样？(on va au restaurant, ça te dit ?)', '怎么样 (zěnmeyàng) = how is…? 今天天气怎么样？(what’s the weather like today?) It is also used to suggest: 我们去饭馆，怎么样？(shall we go to the restaurant?)'),
        ('Les adjectifs se construisent avec 很 ou 太…了 : 今天很冷 (il fait froid), 太热了 (il fait trop chaud). Pluie : 下雨 (il pleut), 下雨了 (il s’est mis à pleuvoir).', 'Adjectives are built with 很 or 太…了: 今天很冷 (it’s cold), 太热了 (it’s too hot). Rain: 下雨 (to rain), 下雨了 (it has started raining).'),
      ], [
        ZG('zenmeyang', '…怎么样？', 'zěnmeyàng', ('comment est… ? ; et si… ?', 'how is…?; how about…?')),
        Z('tianqi', '天气', 'tiānqì', ('temps (météo)', 'weather')),
        Z('leng', '冷', 'lěng', ('froid', 'cold')),
        Z('re', '热', 'rè', ('chaud', 'hot')),
        Z('xiayu', '下雨', 'xià yǔ', ('pleuvoir', 'to rain')),
        Z('zenme', '怎么', 'zěnme', ('comment', 'how')),
        Z('zenmeyang', '怎么样', 'zěnmeyàng', ('comment (est-ce)', 'how is it')),
      ], [
        x('今天天气怎么样？——很热。', 'Jīntiān tiānqì zěnmeyàng? — Hěn rè.', 'Quel temps fait-il aujourd’hui ? — Il fait très chaud.', 'What’s the weather like today? — It’s very hot.'),
        x('下雨了，我们坐出租车去吧。', 'Xià yǔ le, wǒmen zuò chūzūchē qù ba.', 'Il pleut, allons-y en taxi.', 'It’s raining, let’s take a taxi.'),
      ], [
        FB(COMPLETE, '明天天气＿？', ['怎么样', '什么', '哪儿'], '怎么样', ('Comment est… ? = 怎么样？', 'How is…? = 怎么样？'), ('Quel temps fera-t-il demain ?', 'What will the weather be like tomorrow?')),
        FB(COMPLETE, '今天太＿了！', ['冷', '雨', '天'], '冷', ('太 + adjectif + 了 : 太冷了.', '太 + adjective + 了: 太冷了.'), ('Il fait vraiment trop froid aujourd’hui !', 'It’s far too cold today!')),
        DC(ANSWER, [('小明', '我们明天去饭馆，怎么样？')], ('Xiaoming propose d’aller au restaurant demain.', 'Xiaoming suggests going to the restaurant tomorrow.'), ['太好了！', '很冷。', '是饭馆。'], '太好了！', ('On accepte avec enthousiasme : 太好了！', 'You accept enthusiastically: 太好了！')),
        TF('昨天下雨了。', ('Il a plu hier.', 'It rained yesterday.'), VRAI, ('下雨了 = il a plu.', '下雨了 = it rained.')),
      ]),
  ]),
  CH('hsk1-w8-c2', ('Ce que j’aime, ce que je sais faire', 'What I like, what I can do'), [
    L('zh-like', ('Aimer : 喜欢、爱 ; connaître : 认识', 'Liking: 喜欢, 爱; knowing someone: 认识'), ('Dire ce que l’on aime et qui l’on connaît.', 'Say what you like and who you know.'), 9, [
        ('喜欢 + nom ou verbe = aimer bien : 我喜欢猫, 我喜欢看电影. 爱 = aimer (fort) : 我爱我的家.', '喜欢 + noun or verb = to like: 我喜欢猫, 我喜欢看电影. 爱 = to love: 我爱我的家.'),
        ('认识 (rènshi) = connaître une personne : 认识你很高兴 (enchanté de te connaître). 高兴 (gāoxìng) = content.', '认识 (rènshi) = to know a person: 认识你很高兴 (nice to meet you). 高兴 (gāoxìng) = happy, glad.'),
        ('Pour être poli : 请 + verbe = je vous en prie : 请坐 (asseyez-vous), 请喝茶 (prenez du thé). 先生 (monsieur), 小姐 (mademoiselle).', 'To be polite: 请 + verb = please: 请坐 (please sit down), 请喝茶 (please have some tea). 先生 (Mr, sir), 小姐 (Miss).'),
      ], [
        ZG('qing', '请 + 动词', 'qǐng', ('je vous prie de…, s’il vous plaît', 'please (do)…')),
        Z('xihuan', '喜欢', 'xǐhuan', ('aimer (bien)', 'to like')),
        Z('ai', '爱', 'ài', ('aimer, adorer', 'to love')),
        Z('renshi', '认识', 'rènshi', ('connaître (quelqu’un)', 'to know (someone)')),
        Z('gaoxing', '高兴', 'gāoxìng', ('content, heureux', 'happy, glad')),
        Z('qing', '请', 'qǐng', ('s’il vous plaît, inviter', 'please, to invite')),
        Z('xiansheng', '先生', 'xiānsheng', ('monsieur', 'Mr, sir')),
        Z('xiaojie', '小姐', 'xiǎojiě', ('mademoiselle', 'Miss')),
        Z('piaoliang', '漂亮', 'piàoliang', ('joli, beau', 'pretty, beautiful')),
        Z('yifu', '衣服', 'yīfu', ('vêtement', 'clothes')),
      ], [
        x('认识你很高兴！', 'Rènshi nǐ hěn gāoxìng!', 'Enchanté de faire ta connaissance !', 'Nice to meet you!'),
        x('王先生，请坐，请喝茶。', 'Wáng xiānsheng, qǐng zuò, qǐng hē chá.', 'Monsieur Wang, asseyez-vous, prenez du thé.', 'Mr Wang, please sit down and have some tea.'),
      ], [
        FB(COMPLETE, '我很＿看书。', ['喜欢', '认识', '高兴'], '喜欢', ('Aimer faire : 喜欢 + verbe.', 'Like doing: 喜欢 + verb.'), ('J’aime beaucoup lire.', 'I really like reading.')),
        FB(COMPLETE, '＿你很高兴！', ['认识', '喜欢', '请'], '认识', ('Enchanté : 认识你很高兴.', 'Nice to meet you: 认识你很高兴.'), ('Enchanté de te connaître !', 'Nice to meet you!')),
        DC(ANSWER, [('李小姐', '你好！我叫李月。')], ('Li Yue se présente à toi.', 'Li Yue introduces herself to you.'), ['认识你很高兴！', '不客气！', '没关系！'], '认识你很高兴！', ('Après une présentation : 认识你很高兴.', 'After an introduction: 认识你很高兴.')),
        TF('这件衣服很漂亮。', ('Ce vêtement est joli.', 'This piece of clothing is pretty.'), VRAI, ('漂亮 = joli.', '漂亮 = pretty.')),
      ]),
    L('zh-hui-neng', ('Savoir et pouvoir : 会、能、说汉语', 'Know how and be able: 会, 能, speaking Chinese'), ('Dire ce que l’on sait faire et ce que l’on peut faire.', 'Say what you know how to do and what you are able to do.'), 10, [
        ('会 + verbe = savoir faire (appris) : 我会说汉语 (je sais parler chinois), 我会写汉字. 能 + verbe = pouvoir (possibilité, permission) : 你能来吗？(tu peux venir ?)', '会 + verb = know how to (learned): 我会说汉语 (I can speak Chinese), 我会写汉字. 能 + verb = can (possibility, permission): 你能来吗？(can you come?)'),
        ('Négations : 不会 (ne pas savoir), 不能 (ne pas pouvoir). 会 annonce aussi l’avenir probable : 明天会下雨 (il pleuvra demain).', 'Negatives: 不会 (not know how), 不能 (cannot). 会 also announces a likely future: 明天会下雨 (it will rain tomorrow).'),
        ('说 = parler, dire ; 听 = écouter ; 汉语 (Hànyǔ) = le chinois ; 说话 = parler, discuter. 住 (zhù) = habiter : 你住在哪儿？', '说 = to speak, say; 听 = to listen; 汉语 (Hànyǔ) = Chinese; 说话 = to talk. 住 (zhù) = to live: 你住在哪儿？'),
      ], [
        ZG('hui', '会 + 动词', 'huì', ('savoir faire (会 + verbe)', 'know how to (会 + verb)')),
        ZG('neng', '能 + 动词', 'néng', ('pouvoir (possibilité)', 'can, be able to')),
        Z('hui-can', '会', 'huì', ('savoir (faire)', 'can, know how to')),
        Z('neng', '能', 'néng', ('pouvoir', 'can, to be able')),
        Z('shuo', '说', 'shuō', ('parler, dire', 'to speak, to say')),
        Z('shuohua', '说话', 'shuōhuà', ('parler, discuter', 'to talk')),
        Z('ting', '听', 'tīng', ('écouter', 'to listen')),
        Z('hanyu', '汉语', 'Hànyǔ', ('le chinois (langue)', 'Chinese (language)')),
        Z('zhu', '住', 'zhù', ('habiter', 'to live (somewhere)')),
        Z('kaiche', '开车', 'kāi chē', ('conduire (une voiture)', 'to drive (a car)')),
      ], [
        x('你会说汉语吗？——我会说一点儿。', 'Nǐ huì shuō Hànyǔ ma? — Wǒ huì shuō yìdiǎnr.', 'Tu sais parler chinois ? — Un petit peu.', 'Can you speak Chinese? — A little.'),
        x('我今天不能去，我明天能去。', 'Wǒ jīntiān bù néng qù, wǒ míngtiān néng qù.', 'Je ne peux pas y aller aujourd’hui, je peux demain.', 'I can’t go today, I can go tomorrow.'),
      ], [
        FB(COMPLETE, '我＿开车。', ['会', '是', '在'], '会', ('Savoir conduire (appris) : 会开车.', 'Know how to drive (learned): 会开车.'), ('Je sais conduire.', 'I can drive.')),
        FB(COMPLETE, '明天我有工作，不＿去。', ['能', '会', '想'], '能', ('Pas possible : 不能.', 'Not possible: 不能.'), ('Demain je travaille, je ne peux pas y aller.', 'Tomorrow I’m working, I can’t go.')),
        DC(ANSWER, [('大卫', '你住在哪儿？')], ('David te demande où tu habites (à Pékin).', 'David asks where you live (in Beijing).'), ['我住在北京。', '我会北京。', '我想北京。'], '我住在北京。', ('Habiter à : 住在 + lieu.', 'Live in: 住在 + place.')),
        SO(ORDER('Mon fils sait écrire les caractères chinois.', 'My son can write Chinese characters.'), ['我儿子', '会', '写', '汉字。'], ('Sujet + 会 + verbe + objet.', 'Subject + 会 + verb + object.')),
      ]),
  ])])

write_level(1, ('HSK 1 : le messager des Royaumes', 'HSK 1: the messenger of the Kingdoms'), REGION, 'Yellow River Plain',
  [W1, W2, W3, W4, W5, W6, W7, W8, FINAL(1, REGION, ('Simulation HSK 1 : la cour de Luoyang', 'HSK 1 simulation: the court of Luoyang'), 200, 120, 'écoute (听力) et lecture (阅读)', 'listening (听力) and reading (阅读)')])
