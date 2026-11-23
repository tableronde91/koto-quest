# Niveau HSK 2 (chinois, HSK 2.0 niveau 2) : 8 étapes au royaume de Wu, leçons et examen blanc (français + anglais).
# Mode histoire : l'art de la guerre aux côtés du général Sun (voir gen-story.py). Écrit aussi la section HSK 2 de l'onglet Hanzi.
# Usage : python3 scripts/hsk2-level.py   (après hsk1-level.py)
from zh_common import *

REGION = 'Rives du Yangzi'

# ═════════════════════════ 1 : le camp de Gusu — comparer ═════════════════════════
W1 = WORLD('hsk2-w1', ('Le camp de Gusu', 'The camp at Gusu'), REGION,
  ('Comparer avec 比, 更, 最 et 没有…那么 ; décrire avec 高, 长, 快, 慢, 新, 贵, 便宜.', 'Compare with 比, 更, 最 and 没有…那么; describe with 高, 长, 快, 慢, 新, 贵, 便宜.'),
  (('Le Xingtian sans tête', 'The Headless Xingtian'), '刑', ('Le Xingtian, géant décapité qui combat avec ses yeux à la place des seins et sa bouche au nombril, défie les soldats de Wu : « Qui est le plus fort ? » Compare juste pour le faire reculer.', 'The Xingtian, a beheaded giant who fights with eyes where his chest is and a mouth at his navel, challenges the soldiers of Wu: “Who is the strongest?” Compare correctly to make him back down.')),
  [CH('hsk2-w1-c1', ('Plus grand, plus rapide', 'Taller, faster'), [
    HL('zh-hz-compare', ('Les caractères de la comparaison : 比 更 最 高 长 快 慢 新', 'Comparison characters: 比 更 最 高 长 快 慢 新'), ('Reconnaître les caractères pour comparer et décrire.', 'Recognise the characters for comparing and describing.'), [
      ('比 (bǐ) montre deux personnes côte à côte, comme pour les mesurer l’une à l’autre. 最 (zuì) coiffe 取 (prendre) du soleil 日 : ce qu’on prend au sommet.', '比 (bǐ) shows two people side by side, as if measuring one against the other. 最 (zuì) puts the sun 日 on top of 取 (to take): what you take from the very top.'),
      ('快 (kuài, rapide) et 慢 (màn, lent) portent la clé du cœur 忄 : la vitesse se vivait comme un état d’esprit.', '快 (kuài, fast) and 慢 (màn, slow) carry the heart radical 忄: speed was felt as a state of mind.'),
    ], [
      H('bi', '比', 'bǐ', ('comparer, que (comparaison)', 'to compare, than'), 4), H('geng', '更', 'gèng', ('encore plus', 'even more'), 7), H('zui', '最', 'zuì', ('le plus', 'the most'), 12), H('gao', '高', 'gāo', ('grand (de taille), haut', 'tall, high'), 10),
      H('chang', '长', 'cháng', ('long', 'long'), 4), H('kuai-fast', '快', 'kuài', ('rapide', 'fast'), 7), H('man', '慢', 'màn', ('lent', 'slow'), 14), H('xin', '新', 'xīn', ('nouveau', 'new'), 13),
    ]),
    L('zh-bi', ('Comparer : A 比 B + adjectif', 'Comparing: A 比 B + adjective'), ('Comparer deux personnes ou deux choses.', 'Compare two people or two things.'), 10, [
        ('A 比 B + adjectif = A est plus … que B : 哥哥比我高 (mon grand frère est plus grand que moi). Jamais de 很 dans cette phrase : on ne dit pas « 比我很高 ».', 'A 比 B + adjective = A is more … than B: 哥哥比我高 (my older brother is taller than me). Never use 很 in this sentence: you don’t say “比我很高”.'),
        ('Pour insister, on ajoute 更 (encore plus) devant l’adjectif, ou une précision après : 他比我高一点儿 (un peu), 他比我大三岁 (trois ans de plus).', 'To stress it, add 更 (even more) before the adjective, or a detail after it: 他比我高一点儿 (a little), 他比我大三岁 (three years older).'),
        ('La négation la plus courante est A 没有 B (那么) + adjectif : 我没有哥哥那么高 (je ne suis pas aussi grand que mon frère).', 'The most common negative is A 没有 B (那么) + adjective: 我没有哥哥那么高 (I’m not as tall as my brother).'),
      ], [
        ZG('bi', 'A 比 B + 形容词', 'bǐ', ('A est plus … que B', 'A is more … than B')),
        ZG('meiyou-name', 'A 没有 B (那么) + 形容词', 'méiyǒu… nàme', ('A n\'est pas aussi … que B', 'A is not as … as B')),
        Z('bi', '比', 'bǐ', ('que (comparaison)', 'than (comparison)')),
        Z('geng', '更', 'gèng', ('encore plus', 'even more')),
        Z('gao', '高', 'gāo', ('grand (de taille), haut', 'tall, high')),
        Z('chang', '长', 'cháng', ('long', 'long')),
        Z('kuai-fast', '快', 'kuài', ('rapide', 'fast')),
        Z('man', '慢', 'màn', ('lent', 'slow')),
      ], [
        x('哥哥比我高。', 'Gēge bǐ wǒ gāo.', 'Mon grand frère est plus grand que moi.', 'My older brother is taller than me.'),
        x('火车没有飞机那么快。', 'Huǒchē méiyǒu fēijī nàme kuài.', 'Le train n’est pas aussi rapide que l’avion.', 'The train is not as fast as the plane.'),
      ], [
        FB(COMPLETE, '今天＿昨天冷。', ['比', '最', '很'], '比', ('Comparer deux choses : A 比 B + adjectif.', 'Compare two things: A 比 B + adjective.'), ('Il fait plus froid aujourd’hui qu’hier.', 'Today is colder than yesterday.')),
        FB(COMPLETE, '我姐姐比我＿高。', ['更', '很', '太'], '更', ('Après 比, on peut renforcer avec 更, jamais avec 很.', 'After 比 you can add 更 for emphasis, never 很.'), ('Ma grande sœur est encore plus grande que moi.', 'My older sister is even taller than me.')),
        SO(ORDER('Mon père a cinq ans de plus que ma mère.', 'My father is five years older than my mother.'), ['爸爸', '比', '妈妈', '大', '五岁。'], ('A 比 B + adjectif + écart.', 'A 比 B + adjective + difference.')),
        TF('我没有他那么快。', ('Je cours plus vite que lui.', 'I am faster than him.'), FAUX, ('没有…那么 = pas aussi … que.', '没有…那么 = not as … as.')),
      ]),
  ]),
  CH('hsk2-w1-c2', ('Le meilleur soldat', 'The best soldier'), [
    L('zh-zui', ('Le plus : 最 ; prix et qualités : 贵、便宜、新', 'The most: 最; price and quality: 贵, 便宜, 新'), ('Désigner le plus grand, le moins cher, le plus récent.', 'Point out the tallest, the cheapest, the newest.'), 9, [
        ('最 + adjectif = le plus … : 他最高 (c’est lui le plus grand), 这个最便宜 (celui-ci est le moins cher). 最 marche aussi avec les verbes de goût : 我最喜欢茶.', '最 + adjective = the most …: 他最高 (he is the tallest), 这个最便宜 (this one is the cheapest). 最 also works with verbs of liking: 我最喜欢茶.'),
        ('贵 (guì) = cher, 便宜 (piányi) = bon marché. 新 (xīn) = nouveau, neuf ; 旧 est son contraire, que tu verras plus tard.', '贵 (guì) = expensive, 便宜 (piányi) = cheap. 新 (xīn) = new; its opposite 旧 comes later.'),
      ], [
        ZG('zui', '最 + 形容词 / 动词', 'zuì', ('le plus (superlatif)', 'the most (superlative)')),
        Z('zui', '最', 'zuì', ('le plus', 'the most')),
        Z('gui', '贵', 'guì', ('cher, coûteux', 'expensive')),
        Z('pianyi', '便宜', 'piányi', ('bon marché', 'cheap')),
        Z('xin', '新', 'xīn', ('nouveau', 'new')),
        Z('feichang', '非常', 'fēicháng', ('extrêmement', 'extremely')),
      ], [
        x('我们班他最高。', 'Wǒmen bān tā zuì gāo.', 'Dans notre classe, c’est lui le plus grand.', 'He is the tallest in our class.'),
        x('这个手机非常贵，那个便宜一点儿。', 'Zhè ge shǒujī fēicháng guì, nà ge piányi yìdiǎnr.', 'Ce téléphone est très cher, celui-là est un peu moins cher.', 'This phone is very expensive, that one is a bit cheaper.'),
      ], [
        FB(COMPLETE, '三个杯子，这个＿便宜。', ['最', '比', '更'], '最', ('Parmi plusieurs : 最.', 'Among several: 最.'), ('Des trois verres, celui-ci est le moins cher.', 'Of the three cups, this one is the cheapest.')),
        FB(COMPLETE, '这件衣服太＿了！', ['贵', '新', '高'], '贵', ('Le prix est trop élevé : 太贵了.', 'The price is too high: 太贵了.'), ('Ce vêtement est trop cher !', 'These clothes are too expensive!')),
        DC(ANSWER, [('小王', '你最喜欢什么水果？')], ('Xiao Wang te demande ton fruit préféré (la pastèque).', 'Xiao Wang asks your favourite fruit (watermelon).'), ['我最喜欢西瓜。', '西瓜最便宜。', '我比西瓜高。'], '我最喜欢西瓜。', ('Préféré : 最喜欢.', 'Favourite: 最喜欢.')),
        TF('这个手机很新。', ('Le téléphone est récent.', 'The phone is new.'), VRAI, ('新 = nouveau.', '新 = new.')),
      ]),
  ])])

# ═════════════════════════ 2 : l'infirmerie du camp — santé, cause ═════════════════════════
W2 = WORLD('hsk2-w2', ('L’infirmerie du camp', 'The camp infirmary'), REGION,
  ('Le corps et la santé, être fatigué, se reposer, prendre un médicament ; expliquer avec 因为…所以 et 为什么.', 'The body and health, being tired, resting, taking medicine; explaining with 因为…所以 and 为什么.'),
  (('Le Jiuying aux neuf voix', 'The Nine-Voiced Jiuying'), '婴', ('Le Jiuying, monstre d’eau et de feu à neuf têtes, crie comme un nourrisson et rend malade tout le camp. Soigne chaque soldat et explique pourquoi il souffre.', 'The Jiuying, a nine-headed monster of water and fire, cries like a baby and makes the whole camp ill. Treat every soldier and explain why they are suffering.')),
  [CH('hsk2-w2-c1', ('Le corps du soldat', 'The soldier’s body'), [
    HL('zh-hz-health', ('Les caractères de la santé : 身 体 病 药 眼 累 因 为', 'Health characters: 身 体 病 药 眼 累 因 为'), ('Reconnaître les caractères du corps et de la cause.', 'Recognise the characters of the body and of cause.'), [
      ('病 (bìng, maladie) porte la clé 疒, un lit de malade vu de côté : on la retrouve dans beaucoup de mots de santé. 药 (yào, médicament) porte celle des plantes 艹 : les premiers remèdes étaient des herbes.', '病 (bìng, illness) carries the radical 疒, a sickbed seen from the side: it appears in many health words. 药 (yào, medicine) carries the plant radical 艹: the first remedies were herbs.'),
      ('眼 (yǎn, œil) porte la clé de l’œil 目. 因为 (yīnwèi) = parce que : 因 (cause) + 为 (pour).', '眼 (yǎn, eye) carries the eye radical 目. 因为 (yīnwèi) = because: 因 (cause) + 为 (for).'),
    ], [
      H('shen', '身', 'shēn', ('corps', 'body'), 7), H('ti', '体', 'tǐ', ('corps, forme', 'body, form'), 7), H('bing', '病', 'bìng', ('maladie', 'illness'), 10), H('yao-medicine', '药', 'yào', ('médicament', 'medicine'), 9),
      H('yan', '眼', 'yǎn', ('œil', 'eye'), 11), H('lei', '累', 'lèi', ('fatigué', 'tired'), 11), H('yin', '因', 'yīn', ('cause', 'cause'), 6), H('wei-for', '为', 'wèi', ('pour, à cause de', 'for, because of'), 4),
    ]),
    L('zh-health', ('La santé : 身体、生病、药、休息', 'Health: 身体, 生病, 药, 休息'), ('Dire comment on se sent et ce qu’il faut faire.', 'Say how you feel and what you should do.'), 10, [
        ('身体 (shēntǐ) = le corps, la santé : 你身体好吗？(tu vas bien ?). 生病 (shēngbìng) = tomber malade : 我生病了.', '身体 (shēntǐ) = body, health: 你身体好吗？(are you well?). 生病 (shēngbìng) = to fall ill: 我生病了.'),
        ('累 (lèi) = fatigué ; 休息 (xiūxi) = se reposer ; 吃药 (chī yào) = prendre un médicament (« manger » le médicament).', '累 (lèi) = tired; 休息 (xiūxi) = to rest; 吃药 (chī yào) = to take medicine (literally “eat” the medicine).'),
        ('要 + verbe = devoir, il faut : 你要多休息 (tu dois te reposer davantage). 别 + verbe = ne… pas (interdiction) : 别喝咖啡.', '要 + verb = must, should: 你要多休息 (you should rest more). 别 + verb = don’t: 别喝咖啡.'),
      ], [
        ZG('yao-should', '要 + 动词', 'yào', ('devoir, il faut (faire)', 'must, should (do)')),
        ZG('bie', '别 + 动词', 'bié', ('ne… pas ! (interdiction)', 'don’t! (prohibition)')),
        Z('shenti', '身体', 'shēntǐ', ('corps, santé', 'body, health')),
        Z('shengbing', '生病', 'shēngbìng', ('tomber malade', 'to fall ill')),
        Z('yao', '药', 'yào', ('médicament', 'medicine')),
        Z('xiuxi', '休息', 'xiūxi', ('se reposer', 'to rest')),
        Z('lei', '累', 'lèi', ('fatigué', 'tired')),
        Z('yanjing', '眼睛', 'yǎnjing', ('yeux', 'eyes')),
        Z('bie', '别', 'bié', ('ne… pas (impératif)', 'don’t (imperative)')),
      ], [
        x('我生病了，今天不能去上班。', 'Wǒ shēngbìng le, jīntiān bù néng qù shàngbān.', 'Je suis malade, je ne peux pas aller travailler aujourd’hui.', 'I’m ill, I can’t go to work today.'),
        x('你太累了，要多休息，别看电视了。', 'Nǐ tài lèi le, yào duō xiūxi, bié kàn diànshì le.', 'Tu es trop fatigué, repose-toi, arrête de regarder la télé.', 'You’re too tired, you should rest more and stop watching TV.'),
      ], [
        FB(COMPLETE, '医生说我要多＿。', ['休息', '生病', '眼睛'], '休息', ('Le médecin conseille du repos : 休息.', 'The doctor recommends rest: 休息.'), ('Le médecin dit que je dois me reposer davantage.', 'The doctor says I should rest more.')),
        FB(COMPLETE, '你生病了，＿喝咖啡！', ['别', '没', '不是'], '别', ('Interdiction : 别 + verbe.', 'Prohibition: 别 + verb.'), ('Tu es malade, ne bois pas de café !', 'You’re ill, don’t drink coffee!')),
        DC(ANSWER, [('医生', '你身体怎么样？')], ('Le médecin te demande comment tu vas (tu es très fatigué).', 'The doctor asks how you are (you are very tired).'), ['我很累。', '我很贵。', '我很高。'], '我很累。', ('Fatigué : 累.', 'Tired: 累.')),
        TF('他吃药了。', ('Il a pris son médicament.', 'He took his medicine.'), VRAI, ('吃药 = prendre un médicament.', '吃药 = take medicine.')),
      ]),
  ]),
  CH('hsk2-w2-c2', ('Pourquoi ?', 'Why?'), [
    L('zh-yinwei', ('Pourquoi ? 为什么 et 因为…所以', 'Why? 为什么 and 因为…所以'), ('Demander et donner une raison.', 'Ask for and give a reason.'), 10, [
        ('为什么 (wèishénme) = pourquoi : 你为什么不来？On répond avec 因为 (parce que) : 因为我生病了.', '为什么 (wèishénme) = why: 你为什么不来？You answer with 因为 (because): 因为我生病了.'),
        ('因为… 所以… = parce que… donc… En chinois on garde souvent les deux mots : 因为下雨了，所以我没去. La cause vient d’abord.', '因为… 所以… = because… so… Chinese often keeps both words: 因为下雨了，所以我没去. The cause comes first.'),
        ('觉得 (juéde) = trouver, penser (avis) : 我觉得这个药很好. 可能 (kěnéng) = peut-être, il est possible que : 他可能生病了.', '觉得 (juéde) = to feel, to think (opinion): 我觉得这个药很好. 可能 (kěnéng) = maybe, possibly: 他可能生病了.'),
      ], [
        ZG('yinwei-suoyi', '因为…，所以…', 'yīnwèi…, suǒyǐ…', ('parce que…, donc…', 'because…, so…')),
        Z('weishenme', '为什么', 'wèishénme', ('pourquoi', 'why')),
        Z('yinwei', '因为', 'yīnwèi', ('parce que', 'because')),
        Z('suoyi', '所以', 'suǒyǐ', ('donc, c’est pourquoi', 'so, therefore')),
        Z('juede', '觉得', 'juéde', ('trouver, penser (avis)', 'to feel, to think (opinion)')),
        Z('keneng', '可能', 'kěnéng', ('peut-être, possible', 'maybe, possible')),
      ], [
        x('你为什么没来？——因为我生病了。', 'Nǐ wèishénme méi lái? — Yīnwèi wǒ shēngbìng le.', 'Pourquoi n’es-tu pas venu ? — Parce que j’étais malade.', 'Why didn’t you come? — Because I was ill.'),
        x('因为很累，所以他早上没起床。', 'Yīnwèi hěn lèi, suǒyǐ tā zǎoshang méi qǐchuáng.', 'Comme il était très fatigué, il ne s’est pas levé ce matin.', 'Because he was very tired, he didn’t get up this morning.'),
      ], [
        FB(COMPLETE, '因为下雨了，＿我们没去。', ['所以', '因为', '可能'], '所以', ('因为… 所以… : la conséquence après 所以.', '因为… 所以…: the consequence comes after 所以.'), ('Comme il pleuvait, nous n’y sommes pas allés.', 'Because it rained, we didn’t go.')),
        FB(COMPLETE, '你＿不喝茶？', ['为什么', '因为', '什么时候'], '为什么', ('Pourquoi ? = 为什么.', 'Why? = 为什么.'), ('Pourquoi ne bois-tu pas de thé ?', 'Why don’t you drink tea?')),
        DC(ANSWER, [('王老师', '小明为什么没来上课？')], ('Le professeur demande pourquoi Xiaoming est absent (il est malade).', 'The teacher asks why Xiaoming is absent (he is ill).'), ['因为他生病了。', '所以他生病了。', '他可能来。'], '因为他生病了。', ('On répond à 为什么 avec 因为.', 'You answer 为什么 with 因为.')),
        TF('我觉得这个菜很好吃。', ('La personne donne son avis sur un plat.', 'The speaker gives an opinion on a dish.'), VRAI, ('觉得 = trouver (avis).', '觉得 = to find, to think (opinion).')),
      ]),
  ])])

# ═════════════════════════ 3 : le terrain d'exercice — sport, degré ═════════════════════════
W3 = WORLD('hsk2-w3', ('Le terrain d’exercice', 'The training ground'), REGION,
  ('Le sport et les loisirs, juger une action avec 得 (跑得很快), faire ensemble avec 一起, dire combien de fois avec 次.', 'Sport and leisure, judging an action with 得 (跑得很快), doing things together with 一起, saying how many times with 次.'),
  (('Le Qiongqi ailé', 'The Winged Qiongqi'), '穷', ('Le Qiongqi, tigre ailé qui récompense les tricheurs et punit les honnêtes, a envahi le terrain d’exercice. Juge chaque soldat avec justesse pour le chasser.', 'The Qiongqi, a winged tiger that rewards cheats and punishes the honest, has invaded the training ground. Judge every soldier fairly to drive it away.')),
  [CH('hsk2-w3-c1', ('L’entraînement', 'Training'), [
    HL('zh-hz-sport', ('Les caractères du sport : 运 动 跑 步 球 唱 歌 得', 'Sport characters: 运 动 跑 步 球 唱 歌 得'), ('Reconnaître les caractères du sport et des loisirs.', 'Recognise the characters of sport and leisure.'), [
      ('跑 (pǎo, courir) porte la clé du pied 𧾷 ; 球 (qiú, balle) celle du jade 王 : les premières balles précieuses étaient en pierre polie.', '跑 (pǎo, to run) carries the foot radical 𧾷; 球 (qiú, ball) that of jade 王: the first precious balls were polished stone.'),
      ('得 (de) relie un verbe à son appréciation : 跑得快 (courir vite). Il se lit aussi dé (obtenir) ou děi (devoir), que tu verras plus tard.', '得 (de) links a verb to how it is done: 跑得快 (run fast). It is also read dé (to obtain) or děi (must), which you’ll see later.'),
    ], [
      H('yun', '运', 'yùn', ('transporter, mouvoir', 'to move, to transport'), 7), H('dong-move', '动', 'dòng', ('bouger', 'to move'), 6), H('pao', '跑', 'pǎo', ('courir', 'to run'), 12), H('bu-step', '步', 'bù', ('pas', 'step'), 7),
      H('qiu', '球', 'qiú', ('balle, ballon', 'ball'), 11), H('chang-sing', '唱', 'chàng', ('chanter', 'to sing'), 11), H('ge-song', '歌', 'gē', ('chanson', 'song'), 14), H('de-degree', '得', 'de', ('particule de degré', 'degree particle'), 11),
    ]),
    L('zh-sports', ('Le sport : 运动、跑步、游泳、踢足球', 'Sport: 运动, 跑步, 游泳, 踢足球'), ('Parler de ses sports et de ses loisirs.', 'Talk about your sports and hobbies.'), 9, [
        ('运动 (yùndòng) = faire du sport, le sport. Chaque sport a son verbe : 跑步 (courir), 游泳 (nager), 踢足球 (jouer au football, « taper du pied »), 打篮球 (jouer au basket, « frapper »).', '运动 (yùndòng) = to exercise, sport. Each sport has its own verb: 跑步 (to run), 游泳 (to swim), 踢足球 (to play football, “kick”), 打篮球 (to play basketball, “hit”).'),
        ('一起 (yìqǐ) = ensemble, avant le verbe : 我们一起去游泳吧 ! 吧 en fin de phrase propose quelque chose.', '一起 (yìqǐ) = together, before the verb: 我们一起去游泳吧！吧 at the end of a sentence makes a suggestion.'),
        ('Loisirs : 唱歌 (chanter), 跳舞 (danser), 玩 (jouer, s’amuser).', 'Leisure: 唱歌 (to sing), 跳舞 (to dance), 玩 (to play, to have fun).'),
      ], [
        ZG('yiqi', '一起 + 动词', 'yìqǐ', ('faire ensemble', 'to do together')),
        Z('yundong', '运动', 'yùndòng', ('faire du sport, sport', 'to exercise, sport')),
        Z('paobu', '跑步', 'pǎobù', ('courir (footing)', 'to jog, to run')),
        Z('youyong', '游泳', 'yóuyǒng', ('nager', 'to swim')),
        Z('ti-zuqiu', '踢足球', 'tī zúqiú', ('jouer au football', 'to play football')),
        Z('da-lanqiu', '打篮球', 'dǎ lánqiú', ('jouer au basket', 'to play basketball')),
        Z('changge', '唱歌', 'chànggē', ('chanter', 'to sing')),
        Z('tiaowu', '跳舞', 'tiàowǔ', ('danser', 'to dance')),
        Z('wan', '玩', 'wán', ('jouer, s’amuser', 'to play, to have fun')),
        Z('yiqi', '一起', 'yìqǐ', ('ensemble', 'together')),
      ], [
        x('星期六我们一起去踢足球吧！', 'Xīngqīliù wǒmen yìqǐ qù tī zúqiú ba!', 'Samedi, allons jouer au foot ensemble !', 'Let’s go and play football together on Saturday!'),
        x('我妹妹很喜欢唱歌和跳舞。', 'Wǒ mèimei hěn xǐhuan chànggē hé tiàowǔ.', 'Ma petite sœur adore chanter et danser.', 'My little sister loves singing and dancing.'),
      ], [
        FB(COMPLETE, '你喜欢什么＿？——我喜欢游泳。', ['运动', '跳舞', '一起'], '运动', ('Le sport : 运动.', 'Sport: 运动.'), ('Quel sport aimes-tu ? — J’aime nager.', 'What sport do you like? — I like swimming.')),
        FB(COMPLETE, '我们＿去跑步吧！', ['一起', '比', '最'], '一起', ('Ensemble : 一起 + verbe.', 'Together: 一起 + verb.'), ('Allons courir ensemble !', 'Let’s go running together!')),
        FB(COMPLETE, '他们在＿篮球。', ['打', '踢', '玩'], '打', ('Le basket se « frappe » : 打篮球.', 'Basketball is “hit”: 打篮球.'), ('Ils jouent au basket.', 'They are playing basketball.')),
        TF('我每天早上跑步。', ('La personne court tous les matins.', 'The speaker runs every morning.'), VRAI, ('每天早上 = tous les matins.', '每天早上 = every morning.')),
      ]),
  ]),
  CH('hsk2-w3-c2', ('Bien ou mal fait ?', 'Done well or badly?'), [
    L('zh-de', ('Juger une action : verbe + 得 + adjectif', 'Judging an action: verb + 得 + adjective'), ('Dire comment quelqu’un fait quelque chose.', 'Say how someone does something.'), 10, [
        ('Verbe + 得 + (很) adjectif = faire quelque chose de telle façon : 他跑得很快 (il court vite), 你说得很好 (tu parles bien).', 'Verb + 得 + (很) adjective = to do something in a certain way: 他跑得很快 (he runs fast), 你说得很好 (you speak well).'),
        ('Avec un complément, on répète le verbe ou on le met devant : 他说汉语说得很好 = 他汉语说得很好.', 'With an object, repeat the verb or put the object first: 他说汉语说得很好 = 他汉语说得很好.'),
        ('Négation : 他跑得不快. Question : 他跑得快不快？ou 他跑得怎么样？', 'Negative: 他跑得不快. Question: 他跑得快不快？or 他跑得怎么样？'),
      ], [
        ZG('de-degree', '动词 + 得 + 形容词', 'de', ('faire (de telle façon)', 'to do (in a certain way)')),
        Z('de', '得', 'de', ('particule de degré (après le verbe)', 'degree particle (after the verb)')),
        Z('zaoshang', '早上', 'zǎoshang', ('le matin (tôt)', 'early morning')),
        Z('mei', '每', 'měi', ('chaque', 'every, each')),
        Z('ci', '次', 'cì', ('fois', 'time (occurrence)')),
        Z('xiao-laugh', '笑', 'xiào', ('rire, sourire', 'to laugh, to smile')),
      ], [
        x('你汉语说得很好！——哪里哪里。', 'Nǐ Hànyǔ shuō de hěn hǎo! — Nǎli nǎli.', 'Tu parles très bien chinois ! — Oh, pas du tout.', 'You speak Chinese very well! — Oh, not really.'),
        x('我一个星期游泳三次。', 'Wǒ yí ge xīngqī yóuyǒng sān cì.', 'Je nage trois fois par semaine.', 'I swim three times a week.'),
      ], [
        FB(COMPLETE, '他唱歌唱＿很好。', ['得', '的', '了'], '得', ('Après le verbe, pour juger : 得.', 'After the verb, to judge it: 得.'), ('Il chante très bien.', 'He sings very well.')),
        FB(COMPLETE, '她每天跑步两＿。', ['次', '个', '岁'], '次', ('Combien de fois : nombre + 次.', 'How many times: number + 次.'), ('Elle court deux fois par jour.', 'She runs twice a day.')),
        SO(ORDER('Mon grand frère nage très vite.', 'My older brother swims very fast.'), ['哥哥', '游泳', '游得', '很快。'], ('Verbe + objet, verbe + 得 + adjectif.', 'Verb + object, verb + 得 + adjective.')),
        TF('他跳舞跳得不好。', ('Il danse bien.', 'He dances well.'), FAUX, ('跳得不好 = danse mal.', '跳得不好 = dances badly.')),
      ]),
  ])])

# ═════════════════════════ 4 : les voyages du stratège — expérience ═════════════════════════
W4 = WORLD('hsk2-w4', ('Les voyages du stratège', 'The strategist’s travels'), REGION,
  ('Raconter une expérience avec 过, dire que c’est déjà fait avec 已经…了, voyager : aéroport, billet, hôtel, chambre.', 'Talk about experiences with 过, say something is already done with 已经…了, travelling: airport, ticket, hotel, room.'),
  (('Le Kun des mers du Nord', 'The Kun of the Northern Sea'), '鲲', ('Le Kun, poisson si grand que nul ne sait combien de milliers de li il mesure, barre la route maritime vers Wu. Raconte-lui tes voyages et il se changera en oiseau Peng pour t’emporter.', 'The Kun, a fish so huge no one knows how many thousand li long it is, blocks the sea route to Wu. Tell it about your travels and it will turn into the Peng bird and carry you away.')),
  [CH('hsk2-w4-c1', ('Déjà vu ?', 'Been there before?'), [
    HL('zh-hz-travel', ('Les caractères du voyage : 过 已 经 旅 游 票 房 次', 'Travel characters: 过 已 经 旅 游 票 房 次'), ('Reconnaître les caractères du voyage et de l’expérience.', 'Recognise the characters of travel and experience.'), [
      ('过 (guò, passer) et beaucoup de verbes de mouvement portent la clé de la marche 辶, en bas à gauche.', '过 (guò, to pass) and many movement verbs carry the walking radical 辶, at the bottom left.'),
      ('旅 (lǚ) montre des gens sous un étendard : une troupe en déplacement. 游 (yóu) porte l’eau 氵 : nager, puis voyager.', '旅 (lǚ) shows people under a banner: a troop on the move. 游 (yóu) carries water 氵: to swim, then to travel.'),
    ], [
      H('guo', '过', 'guò', ('passer ; marque d’expérience', 'to pass; experience marker'), 6), H('yi-already', '已', 'yǐ', ('déjà', 'already'), 3), H('jing', '经', 'jīng', ('passer par', 'to pass through'), 8), H('lv', '旅', 'lǚ', ('voyage', 'journey'), 10),
      H('you-swim', '游', 'yóu', ('nager, voyager', 'to swim, to travel'), 12), H('piao', '票', 'piào', ('billet, ticket', 'ticket'), 11), H('fang', '房', 'fáng', ('maison, pièce', 'house, room'), 8), H('ci', '次', 'cì', ('fois', 'time (occurrence)'), 6),
    ]),
    L('zh-guo', ('L’expérience : verbe + 过', 'Experience: verb + 过'), ('Dire ce qu’on a déjà fait (ou jamais fait) dans sa vie.', 'Say what you have (or have never) done in your life.'), 10, [
        ('Verbe + 过 = avoir déjà fait au moins une fois : 我去过北京 (je suis déjà allé à Pékin). On compte avec 次 : 我去过两次.', 'Verb + 过 = to have done at least once: 我去过北京 (I have been to Beijing). Count with 次: 我去过两次.'),
        ('Négation : 没 + verbe + 过 = n’avoir jamais fait : 我没吃过羊肉. Question : 你去过中国吗？', 'Negative: 没 + verb + 过 = have never done: 我没吃过羊肉. Question: 你去过中国吗？'),
        ('第一次 (dì-yī cì) = la première fois : 这是我第一次坐飞机.', '第一次 (dì-yī cì) = the first time: 这是我第一次坐飞机.'),
      ], [
        ZG('guo', '动词 + 过', 'guo', ('avoir déjà fait (expérience)', 'have done before (experience)')),
        Z('lvyou', '旅游', 'lǚyóu', ('voyager (tourisme)', 'to travel (tourism)')),
        Z('diyi', '第一', 'dì-yī', ('premier', 'first')),
        Z('yangrou', '羊肉', 'yángròu', ('viande de mouton', 'mutton, lamb')),
        Z('qunian', '去年', 'qùnián', ('l’année dernière', 'last year')),
        Z('jichang', '机场', 'jīchǎng', ('aéroport', 'airport')),
      ], [
        x('你去过中国吗？——去过，去年我去中国旅游了。', 'Nǐ qùguo Zhōngguó ma? — Qùguo, qùnián wǒ qù Zhōngguó lǚyóu le.', 'Tu es déjà allé en Chine ? — Oui, j’y suis allé en voyage l’an dernier.', 'Have you been to China? — Yes, I travelled there last year.'),
        x('我没吃过羊肉。', 'Wǒ méi chīguo yángròu.', 'Je n’ai jamais mangé de mouton.', 'I have never eaten mutton.'),
      ], [
        FB(COMPLETE, '我去＿北京两次。', ['过', '了', '得'], '过', ('Expérience vécue : verbe + 过.', 'Experience: verb + 过.'), ('Je suis allé deux fois à Pékin.', 'I have been to Beijing twice.')),
        FB(COMPLETE, '我＿坐过飞机。', ['没', '不', '别'], '没', ('Jamais fait : 没 + verbe + 过.', 'Never done: 没 + verb + 过.'), ('Je n’ai jamais pris l’avion.', 'I have never taken a plane.')),
        SO(ORDER('C’est la première fois que je viens en Chine.', 'This is my first time in China.'), ['这是', '我', '第一次', '来', '中国。'], ('第一次 avant le verbe.', '第一次 before the verb.')),
        TF('他去年去过机场。', ('Il est allé à l’aéroport l’an dernier.', 'He went to the airport last year.'), VRAI, ('去年 = l’année dernière.', '去年 = last year.')),
      ]),
  ]),
  CH('hsk2-w4-c2', ('À l’auberge', 'At the inn'), [
    L('zh-yijing', ('Déjà : 已经…了 ; à l’hôtel : 宾馆、房间、票', 'Already: 已经…了; at the hotel: 宾馆, 房间, 票'), ('Dire qu’une chose est déjà faite et réserver une chambre.', 'Say something is already done and book a room.'), 10, [
        ('已经 + verbe + 了 = déjà : 我已经买票了 (j’ai déjà acheté les billets). 已经 + nombre + 了 : 已经十点了 (il est déjà dix heures).', '已经 + verb + 了 = already: 我已经买票了 (I’ve already bought the tickets). 已经 + number + 了: 已经十点了 (it’s already ten o’clock).'),
        ('À l’hôtel : 宾馆 (bīnguǎn, hôtel), 房间 (fángjiān, chambre), 票 (piào, billet). 欢迎 (huānyíng) = bienvenue : 欢迎你们！', 'At the hotel: 宾馆 (bīnguǎn, hotel), 房间 (fángjiān, room), 票 (piào, ticket). 欢迎 (huānyíng) = welcome: 欢迎你们！'),
      ], [
        ZG('yijing-le', '已经…了', 'yǐjīng… le', ('déjà (fait)', 'already (done)')),
        Z('yijing', '已经', 'yǐjīng', ('déjà', 'already')),
        Z('binguan', '宾馆', 'bīnguǎn', ('hôtel', 'hotel')),
        Z('fangjian', '房间', 'fángjiān', ('chambre, pièce', 'room')),
        Z('piao', '票', 'piào', ('billet, ticket', 'ticket')),
        Z('huanying', '欢迎', 'huānyíng', ('bienvenue, accueillir', 'welcome')),
        Z('shijian', '时间', 'shíjiān', ('temps (durée)', 'time (duration)')),
        Z('xiaoshi', '小时', 'xiǎoshí', ('heure (durée)', 'hour (duration)')),
      ], [
        x('欢迎！您的房间在三楼。', 'Huānyíng! Nín de fángjiān zài sān lóu.', 'Bienvenue ! Votre chambre est au deuxième étage.', 'Welcome! Your room is on the third floor.'),
        x('我已经等了两个小时了！', 'Wǒ yǐjīng děngle liǎng ge xiǎoshí le!', 'Ça fait déjà deux heures que j’attends !', 'I’ve already been waiting for two hours!'),
      ], [
        FB(COMPLETE, '我＿买票了。', ['已经', '第一', '过'], '已经', ('Déjà fait : 已经…了.', 'Already done: 已经…了.'), ('J’ai déjà acheté le billet.', 'I’ve already bought the ticket.')),
        FB(COMPLETE, '这个宾馆的＿很大。', ['房间', '时间', '小时'], '房间', ('La chambre : 房间.', 'The room: 房间.'), ('Les chambres de cet hôtel sont grandes.', 'This hotel’s rooms are big.')),
        DC(ANSWER, [('服务员', '欢迎！你们有几个人？')], ('À l’hôtel, l’employé t’accueille (vous êtes deux).', 'At the hotel, the receptionist welcomes you (there are two of you).'), ['我们两个人。', '我们两个房间。', '我们两点。'], '我们两个人。', ('Combien de personnes : 两个人.', 'How many people: 两个人.')),
        TF('已经十二点了。', ('Il est déjà midi (ou minuit).', 'It’s already twelve o’clock.'), VRAI, ('已经…了 = déjà.', '已经…了 = already.')),
      ]),
  ])])

# ═════════════════════════ 5 : les routes de Wu — direction, distance ═════════════════════════
W5 = WORLD('hsk2-w5', ('Les routes de Wu', 'The roads of Wu'), REGION,
  ('Dire la distance avec 离 (远 / 近), aller d’un lieu à un autre avec 从…到, s’orienter : 往, 左边, 右边, 旁边, 外.', 'Give distances with 离 (远 / 近), go from one place to another with 从…到, find your way: 往, 左边, 右边, 旁边, 外.'),
  (('Le Hundun sans visage', 'The Faceless Hundun'), '混', ('Le Hundun, chaos sans yeux ni bouche qui roule sur six pattes, brouille toutes les routes de Wu. Donne des directions précises et il se perdra lui-même.', 'The Hundun, a chaos with no eyes or mouth rolling on six legs, scrambles every road in Wu. Give precise directions and it will get lost itself.')),
  [CH('hsk2-w5-c1', ('Loin ou près ?', 'Far or near?'), [
    HL('zh-hz-roads', ('Les caractères de la route : 离 远 近 从 路 走 进 出', 'Road characters: 离 远 近 从 路 走 进 出'), ('Reconnaître les caractères du déplacement et de la distance.', 'Recognise the characters of moving and distance.'), [
      ('远 (yuǎn, loin), 近 (jìn, près), 进 (jìn, entrer) portent tous la clé de la marche 辶. 路 (lù, route) porte celle du pied 𧾷.', '远 (yuǎn, far), 近 (jìn, near) and 进 (jìn, to enter) all carry the walking radical 辶. 路 (lù, road) carries the foot radical 𧾷.'),
      ('从 (cóng, depuis) montre une personne qui en suit une autre ; 出 (chū, sortir) un pied qui quitte un enclos.', '从 (cóng, from) shows one person following another; 出 (chū, to go out) a foot leaving an enclosure.'),
    ], [
      H('li-from', '离', 'lí', ('être éloigné de', 'to be away from'), 10), H('yuan', '远', 'yuǎn', ('loin', 'far'), 7), H('jin-near', '近', 'jìn', ('près', 'near'), 7), H('cong', '从', 'cóng', ('depuis, de', 'from'), 4),
      H('lu', '路', 'lù', ('route, chemin', 'road, way'), 13), H('zou', '走', 'zǒu', ('marcher, partir', 'to walk, to leave'), 7), H('jin-enter', '进', 'jìn', ('entrer', 'to enter'), 7), H('chu', '出', 'chū', ('sortir', 'to go out'), 5),
    ]),
    L('zh-li', ('La distance : 离、远、近 et 从…到', 'Distance: 离, 远, 近 and 从…到'), ('Dire si un lieu est loin et combien de temps il faut.', 'Say whether a place is far and how long it takes.'), 10, [
        ('A 离 B + 远 / 近 = A est loin de / près de B : 我家离公司很远 (ma maison est loin de l’entreprise).', 'A 离 B + 远 / 近 = A is far from / near B: 我家离公司很远 (my home is far from the office).'),
        ('从 A 到 B = de A à B : 从我家到学校要二十分钟 (il faut vingt minutes de chez moi à l’école). 要 + durée = il faut (tant de temps).', '从 A 到 B = from A to B: 从我家到学校要二十分钟 (it takes twenty minutes from my home to school). 要 + duration = it takes (that long).'),
        ('走 (zǒu) = marcher, partir : 走路 (aller à pied). 公共汽车 (gōnggòng qìchē) = bus.', '走 (zǒu) = to walk, to leave: 走路 (to go on foot). 公共汽车 (gōnggòng qìchē) = bus.'),
      ], [
        ZG('li', 'A 离 B + 远 / 近', 'lí', ('A est loin / près de B', 'A is far from / near B')),
        ZG('cong-dao', '从 A 到 B', 'cóng… dào…', ('de A à B', 'from A to B')),
        Z('li', '离', 'lí', ('être éloigné de', 'to be away from')),
        Z('yuan', '远', 'yuǎn', ('loin', 'far')),
        Z('jin', '近', 'jìn', ('près', 'near, close')),
        Z('cong', '从', 'cóng', ('depuis, de', 'from')),
        Z('dao', '到', 'dào', ('arriver, jusqu’à', 'to arrive, to')),
        Z('zou', '走', 'zǒu', ('marcher, partir', 'to walk, to leave')),
        Z('lu', '路', 'lù', ('route, chemin', 'road, way')),
        Z('gonggong-qiche', '公共汽车', 'gōnggòng qìchē', ('bus', 'bus')),
        Z('gongsi', '公司', 'gōngsī', ('entreprise', 'company')),
      ], [
        x('你家离这儿远吗？——不远，很近。', 'Nǐ jiā lí zhèr yuǎn ma? — Bù yuǎn, hěn jìn.', 'Ta maison est loin d’ici ? — Non, c’est tout près.', 'Is your home far from here? — No, it’s very close.'),
        x('从机场到宾馆要一个小时。', 'Cóng jīchǎng dào bīnguǎn yào yí ge xiǎoshí.', 'Il faut une heure de l’aéroport à l’hôtel.', 'It takes an hour from the airport to the hotel.'),
      ], [
        FB(COMPLETE, '学校＿我家很近。', ['离', '从', '到'], '离', ('La distance : A 离 B + 近 / 远.', 'Distance: A 离 B + 近 / 远.'), ('L’école est tout près de chez moi.', 'The school is very close to my home.')),
        FB(COMPLETE, '从北京＿上海要五个小时。', ['到', '离', '去'], '到', ('De A à B : 从 A 到 B.', 'From A to B: 从 A 到 B.'), ('Il faut cinq heures de Pékin à Shanghai.', 'It takes five hours from Beijing to Shanghai.')),
        DC(ANSWER, [('大卫', '公司离你家远吗？')], ('David demande si ton entreprise est loin (non, c’est à dix minutes à pied).', 'David asks if your company is far (no, ten minutes on foot).'), ['不远，走路十分钟。', '很远，我很累。', '我从公司来。'], '不远，走路十分钟。', ('Pas loin : 不远.', 'Not far: 不远.')),
        TF('我坐公共汽车去公司。', ('La personne va au travail à pied.', 'The speaker walks to work.'), FAUX, ('坐公共汽车 = prendre le bus.', '坐公共汽车 = take the bus.')),
      ]),
  ]),
  CH('hsk2-w5-c2', ('À gauche, à droite', 'Left and right'), [
    L('zh-directions', ('S’orienter : 往、左边、右边、旁边、外', 'Finding your way: 往, 左边, 右边, 旁边, 外'), ('Indiquer un chemin et situer un lieu.', 'Give directions and locate a place.'), 9, [
        ('往 + direction + verbe = aller vers : 往前走 (va tout droit), 往左走 (tourne à gauche), 往右走 (tourne à droite).', '往 + direction + verb = go towards: 往前走 (go straight on), 往左走 (go left), 往右走 (go right).'),
        ('左边 (à gauche), 右边 (à droite), 旁边 (à côté), 外边 / 外 (dehors) : 银行在学校旁边. 进 = entrer, 出 = sortir : 请进！', '左边 (on the left), 右边 (on the right), 旁边 (next to), 外边 / 外 (outside): 银行在学校旁边. 进 = to enter, 出 = to go out: 请进！'),
      ], [
        ZG('wang', '往 + 方向 + 动词', 'wǎng', ('aller vers (direction)', 'to go towards (direction)')),
        Z('wang', '往', 'wǎng', ('vers, en direction de', 'towards')),
        Z('zuobian', '左边', 'zuǒbian', ('à gauche', 'on the left')),
        Z('youbian', '右边', 'yòubian', ('à droite', 'on the right')),
        Z('pangbian', '旁边', 'pángbiān', ('à côté', 'beside, next to')),
        Z('wai', '外', 'wài', ('dehors, extérieur', 'outside')),
        Z('jin-enter', '进', 'jìn', ('entrer', 'to enter')),
        Z('chu', '出', 'chū', ('sortir', 'to go out')),
        Z('men', '门', 'mén', ('porte', 'door')),
      ], [
        x('请问，火车站怎么走？——往前走，再往右走。', 'Qǐngwèn, huǒchēzhàn zěnme zǒu? — Wǎng qián zǒu, zài wǎng yòu zǒu.', 'Excusez-moi, comment va-t-on à la gare ? — Tout droit, puis à droite.', 'Excuse me, how do I get to the station? — Go straight on, then turn right.'),
        x('饭馆在宾馆旁边，门在左边。', 'Fànguǎn zài bīnguǎn pángbiān, mén zài zuǒbian.', 'Le restaurant est à côté de l’hôtel, l’entrée est à gauche.', 'The restaurant is next to the hotel; the door is on the left.'),
      ], [
        FB(COMPLETE, '＿前走，就到了。', ['往', '从', '离'], '往', ('Direction : 往 + direction + verbe.', 'Direction: 往 + direction + verb.'), ('Va tout droit et tu y es.', 'Go straight on and you’re there.')),
        FB(COMPLETE, '医院在学校＿。', ['旁边', '往', '进'], '旁边', ('À côté : 旁边.', 'Next to: 旁边.'), ('L’hôpital est à côté de l’école.', 'The hospital is next to the school.')),
        DC(ANSWER, [('老师', '请进！')], ('On frappe ; le professeur t’invite à entrer.', 'You knock; the teacher invites you in.'), ['谢谢老师！', '我在外边。', '往右走。'], '谢谢老师！', ('On remercie en entrant.', 'You say thank you as you come in.')),
        TF('他的房间在右边。', ('Sa chambre est à gauche.', 'His room is on the left.'), FAUX, ('右边 = à droite.', '右边 = on the right.')),
      ]),
  ])])

# ═════════════════════════ 6 : le marché de Gusu — achats, couleurs ═════════════════════════
W6 = WORLD('hsk2-w6', ('Le marché de Gusu', 'The Gusu market'), REGION,
  ('Les couleurs, les classificateurs 件 et 张, les centaines et les milliers, choisir avec 还是, demander la permission avec 可以.', 'Colours, the measure words 件 and 张, hundreds and thousands, choosing with 还是, asking permission with 可以.'),
  (('Le Baize savant', 'The Learned Baize'), '泽', ('Le Baize, bête blanche qui connaît le nom de tous les monstres, garde l’entrée du marché. Il ne laisse passer que ceux qui nomment chaque marchandise, sa couleur et son prix.', 'The Baize, a white beast that knows the name of every monster, guards the market gate. It only lets through those who can name each item, its colour and its price.')),
  [CH('hsk2-w6-c1', ('Les étals', 'The stalls'), [
    HL('zh-hz-colors', ('Les caractères du marché : 卖 红 白 黑 件 百 千 元', 'Market characters: 卖 红 白 黑 件 百 千 元'), ('Reconnaître les couleurs, les grands nombres et la monnaie.', 'Recognise colours, big numbers and money.'), [
      ('卖 (mài, vendre) = 买 (mǎi, acheter) avec 十 au-dessus : le marchand « sort » la marchandise. 红 (hóng, rouge) porte la soie 纟 : on parlait d’abord de tissu teint.', '卖 (mài, to sell) = 买 (mǎi, to buy) with 十 on top: the merchant “puts out” the goods. 红 (hóng, red) carries silk 纟: it first described dyed cloth.'),
      ('元 (yuán) est l’unité officielle de la monnaie ; à l’oral on dit 块. 百 (bǎi) = cent, 千 (qiān) = mille.', '元 (yuán) is the official currency unit; in speech people say 块. 百 (bǎi) = hundred, 千 (qiān) = thousand.'),
    ], [
      H('mai-sell', '卖', 'mài', ('vendre', 'to sell'), 8), H('hong', '红', 'hóng', ('rouge', 'red'), 6), H('bai', '白', 'bái', ('blanc', 'white'), 5), H('hei', '黑', 'hēi', ('noir', 'black'), 12),
      H('jian', '件', 'jiàn', ('pièce (classificateur)', 'piece (measure word)'), 6), H('bai-hundred', '百', 'bǎi', ('cent', 'hundred'), 6), H('qian-thousand', '千', 'qiān', ('mille', 'thousand'), 3), H('yuan-money', '元', 'yuán', ('yuan (monnaie)', 'yuan (currency)'), 4),
    ]),
    L('zh-colors', ('Couleurs et classificateurs : 颜色、件、张', 'Colours and measure words: 颜色, 件, 张'), ('Décrire un vêtement ou un objet par sa couleur.', 'Describe clothes or an object by its colour.'), 10, [
        ('颜色 (yánsè) = couleur : 你喜欢什么颜色？红色 (rouge), 白色 (blanc), 黑色 (noir). Devant un nom, on peut dire 红衣服 ou 红色的衣服.', '颜色 (yánsè) = colour: 你喜欢什么颜色？红色 (red), 白色 (white), 黑色 (black). Before a noun you can say 红衣服 or 红色的衣服.'),
        ('件 compte les vêtements et les affaires : 一件衣服, 一件事情. 张 compte les choses plates : 一张票, 一张桌子.', '件 counts clothes and matters: 一件衣服, 一件事情. 张 counts flat things: 一张票, 一张桌子.'),
        ('穿 (chuān) = porter, mettre (un vêtement) : 她穿着红衣服.', '穿 (chuān) = to wear, to put on (clothes): 她穿着红衣服.'),
      ], [
        Z('yanse', '颜色', 'yánsè', ('couleur', 'colour')),
        Z('hong', '红', 'hóng', ('rouge', 'red')),
        Z('bai', '白', 'bái', ('blanc', 'white')),
        Z('hei', '黑', 'hēi', ('noir', 'black')),
        Z('jian', '件', 'jiàn', ('classificateur des vêtements, des affaires', 'measure word for clothes, matters')),
        Z('zhang', '张', 'zhāng', ('classificateur des objets plats', 'measure word for flat things')),
        Z('chuan', '穿', 'chuān', ('porter (un vêtement)', 'to wear')),
        Z('shoubiao', '手表', 'shǒubiǎo', ('montre', 'watch')),
        Z('shouji', '手机', 'shǒujī', ('téléphone portable', 'mobile phone')),
      ], [
        x('我想买一件白衬衫……不，一件红衣服。', 'Wǒ xiǎng mǎi yí jiàn bái chènshān… bù, yí jiàn hóng yīfu.', 'Je voudrais acheter une chemise blanche… non, un vêtement rouge.', 'I’d like to buy a white shirt… no, a red top.'),
        x('这张票是你的吗？', 'Zhè zhāng piào shì nǐ de ma?', 'Ce billet est à toi ?', 'Is this ticket yours?'),
      ], [
        FB(COMPLETE, '我买了两＿衣服。', ['件', '张', '个'], '件', ('Les vêtements se comptent avec 件.', 'Clothes are counted with 件.'), ('J’ai acheté deux vêtements.', 'I bought two items of clothing.')),
        FB(COMPLETE, '你有几＿火车票？', ['张', '件', '口'], '张', ('Les billets, plats, se comptent avec 张.', 'Tickets, being flat, are counted with 张.'), ('Combien de billets de train as-tu ?', 'How many train tickets do you have?')),
        FB(COMPLETE, '你喜欢什么＿？——红色。', ['颜色', '衣服', '手表'], '颜色', ('La couleur : 颜色.', 'Colour: 颜色.'), ('Quelle couleur aimes-tu ? — Le rouge.', 'What colour do you like? — Red.')),
        TF('他的手机是黑色的。', ('Son téléphone est noir.', 'His phone is black.'), VRAI, ('黑色 = noir.', '黑色 = black.')),
      ]),
  ]),
  CH('hsk2-w6-c2', ('Ceci ou cela ?', 'This or that?'), [
    L('zh-haishi', ('Choisir : 还是 ; grands prix : 百、千 ; 可以', 'Choosing: 还是; big prices: 百, 千; 可以'), ('Proposer un choix, compter en centaines et demander la permission.', 'Offer a choice, count in hundreds and ask permission.'), 10, [
        ('A 还是 B ? = A ou B ? (dans une question) : 你喝茶还是喝咖啡？La réponse choisit l’un des deux, sans 吗.', 'A 还是 B? = A or B? (in a question): 你喝茶还是喝咖啡？The answer picks one of the two, without 吗.'),
        ('Grands nombres : 一百 (100), 三百五十 (350), 一千 (1 000), 两千 (2 000). Prix écrits : 元 ; à l’oral : 块. 公斤 (gōngjīn) = kilo.', 'Big numbers: 一百 (100), 三百五十 (350), 一千 (1,000), 两千 (2,000). Written prices: 元; spoken: 块. 公斤 (gōngjīn) = kilo.'),
        ('可以 + verbe = pouvoir (permission) : 我可以看看吗？(je peux regarder ?). On répond 可以 ou 不行.', '可以 + verb = may, can (permission): 我可以看看吗？(may I have a look?). The answer is 可以 or 不行.'),
      ], [
        ZG('haishi', 'A 还是 B？', 'háishi', ('A ou B ? (question de choix)', 'A or B? (choice question)')),
        ZG('keyi', '可以 + 动词', 'kěyǐ', ('pouvoir (permission)', 'may, can (permission)')),
        Z('haishi', '还是', 'háishi', ('ou (dans une question)', 'or (in a question)')),
        Z('keyi', '可以', 'kěyǐ', ('pouvoir (avoir le droit)', 'may, can')),
        Z('bai-hundred', '百', 'bǎi', ('cent', 'hundred')),
        Z('qian-thousand', '千', 'qiān', ('mille', 'thousand')),
        Z('yuan-money', '元', 'yuán', ('yuan (écrit)', 'yuan (written)')),
        Z('gongjin', '公斤', 'gōngjīn', ('kilogramme', 'kilogram')),
        Z('mai-sell', '卖', 'mài', ('vendre', 'to sell')),
        Z('kafei', '咖啡', 'kāfēi', ('café', 'coffee')),
        Z('niunai', '牛奶', 'niúnǎi', ('lait', 'milk')),
        Z('jidan', '鸡蛋', 'jīdàn', ('œuf', 'egg')),
        Z('xigua', '西瓜', 'xīguā', ('pastèque', 'watermelon')),
        Z('yu', '鱼', 'yú', ('poisson', 'fish')),
      ], [
        x('你要咖啡还是牛奶？——咖啡，谢谢。', 'Nǐ yào kāfēi háishi niúnǎi? — Kāfēi, xièxie.', 'Tu veux du café ou du lait ? — Du café, merci.', 'Would you like coffee or milk? — Coffee, thanks.'),
        x('西瓜怎么卖？——两块钱一公斤。', 'Xīguā zěnme mài? — Liǎng kuài qián yì gōngjīn.', 'Combien la pastèque ? — Deux yuans le kilo.', 'How much is the watermelon? — Two yuan a kilo.'),
      ], [
        FB(COMPLETE, '你吃鱼＿吃羊肉？', ['还是', '和', '吗'], '还是', ('Question de choix : A 还是 B.', 'Choice question: A 还是 B.'), ('Tu manges du poisson ou du mouton ?', 'Will you have fish or mutton?')),
        FB(COMPLETE, '我＿进来吗？', ['可以', '还是', '会'], '可以', ('Demander la permission : 可以…吗？', 'Ask permission: 可以…吗？'), ('Je peux entrer ?', 'May I come in?')),
        FB(('Comment écrit-on 2 500 ?', 'How do you write 2,500?'), '2500 = ＿', ['两千五百', '二百五十', '两千五十'], '两千五百', ('2 × 1 000 + 5 × 100 : 两千五百.', '2 × 1,000 + 5 × 100: 两千五百.'), ('deux mille cinq cents', 'two thousand five hundred')),
        TF('鸡蛋八块钱一公斤。', ('Les œufs coûtent huit yuans le kilo.', 'Eggs cost eight yuan a kilo.'), VRAI, ('八块 = 8 yuans, 一公斤 = un kilo.', '八块 = 8 yuan, 一公斤 = one kilo.')),
      ]),
  ])])

# ═════════════════════════ 7 : avant la bataille — en cours, imminent, résultat ═════════════════════════
W7 = WORLD('hsk2-w7', ('Avant la bataille', 'Before the battle'), REGION,
  ('Ce qui se passe en ce moment (正在…呢, 着), ce qui va arriver (要…了, 快…了), le résultat d’une action (完, 到, 懂), le temps (晴, 阴, 雪).', 'What is happening now (正在…呢, 着), what is about to happen (要…了, 快…了), the result of an action (完, 到, 懂), the weather (晴, 阴, 雪).'),
  (('La Hanba de la sécheresse', 'The Hanba of Drought'), '魃', ('La Hanba, démone en robe verte, assèche tout sur son passage : les puits de Wu se vident à l’approche de la bataille. Annonce le temps qu’il va faire et termine les préparatifs pour la chasser vers le nord.', 'The Hanba, a demoness in a green robe, dries up everything in her path: the wells of Wu are emptying as the battle draws near. Announce the coming weather and finish the preparations to drive her north.')),
  [CH('hsk2-w7-c1', ('En ce moment', 'Right now'), [
    HL('zh-hz-now', ('Les caractères du moment : 正 着 完 到 懂 等 找 雪', 'Characters of the moment: 正 着 完 到 懂 等 找 雪'), ('Reconnaître les caractères de l’action en cours et du résultat.', 'Recognise the characters of ongoing actions and results.'), [
      ('着 (zhe) se lit aussi zháo ou zhuó selon le sens ; après un verbe, il indique un état qui dure : 门开着 (la porte est ouverte).', '着 (zhe) can also be read zháo or zhuó depending on meaning; after a verb it marks a lasting state: 门开着 (the door is open).'),
      ('懂 (dǒng, comprendre) porte le cœur 忄 ; 雪 (xuě, neige) la pluie 雨 au-dessus d’une main qui la recueille.', '懂 (dǒng, to understand) carries the heart 忄; 雪 (xuě, snow) has rain 雨 above a hand catching it.'),
    ], [
      H('zheng', '正', 'zhèng', ('droit, juste ; en train de', 'straight, right; in the middle of'), 5), H('zhe', '着', 'zhe', ('marque d’un état qui dure', 'marker of a lasting state'), 11), H('wan', '完', 'wán', ('finir, terminer', 'to finish'), 7), H('dao', '到', 'dào', ('arriver', 'to arrive'), 8),
      H('dong-understand', '懂', 'dǒng', ('comprendre', 'to understand'), 15), H('deng', '等', 'děng', ('attendre', 'to wait'), 12), H('zhao', '找', 'zhǎo', ('chercher', 'to look for'), 7), H('xue-snow', '雪', 'xuě', ('neige', 'snow'), 11),
    ]),
    L('zh-zhengzai', ('En train de : 正在…呢 et verbe + 着', 'In progress: 正在…呢 and verb + 着'), ('Dire ce qui se passe en ce moment et décrire une scène.', 'Say what is happening now and describe a scene.'), 10, [
        ('正在 + verbe (+ 呢) = être en train de, justement : 我正在吃饭呢 (je suis justement en train de manger). Plus court : 在…呢 ou 正…呢.', '正在 + verb (+ 呢) = to be in the middle of doing: 我正在吃饭呢 (I’m eating right now). Shorter: 在…呢 or 正…呢.'),
        ('Verbe + 着 = un état qui dure : 他穿着黑衣服 (il porte des vêtements noirs), 门开着 (la porte est ouverte), 他笑着说 (il dit en souriant).', 'Verb + 着 = a lasting state: 他穿着黑衣服 (he is wearing black), 门开着 (the door is open), 他笑着说 (he says with a smile).'),
        ('等 (děng) = attendre, 找 (zhǎo) = chercher : 我在找我的手机.', '等 (děng) = to wait, 找 (zhǎo) = to look for: 我在找我的手机.'),
      ], [
        ZG('zhengzai', '正在 + 动词 + 呢', 'zhèngzài… ne', ('être en train de', 'to be in the middle of doing')),
        ZG('zhe', '动词 + 着', 'zhe', ('état qui dure', 'lasting state')),
        Z('zhengzai', '正在', 'zhèngzài', ('être en train de', 'in the middle of')),
        Z('zhe-state', '着', 'zhe', ('marque de l’état (après le verbe)', 'state marker (after the verb)')),
        Z('deng', '等', 'děng', ('attendre', 'to wait')),
        Z('zhao', '找', 'zhǎo', ('chercher', 'to look for')),
        Z('xi', '洗', 'xǐ', ('laver', 'to wash')),
        Z('fuwuyuan', '服务员', 'fúwùyuán', ('serveur, employé', 'waiter, attendant')),
      ], [
        x('你在做什么呢？——我正在洗衣服呢。', 'Nǐ zài zuò shénme ne? — Wǒ zhèngzài xǐ yīfu ne.', 'Qu’est-ce que tu fais ? — Je suis en train de laver mon linge.', 'What are you doing? — I’m washing my clothes.'),
        x('服务员笑着说：“欢迎！”', 'Fúwùyuán xiàozhe shuō: “Huānyíng!”', 'Le serveur dit en souriant : « Bienvenue ! »', 'The waiter said with a smile: “Welcome!”'),
      ], [
        FB(COMPLETE, '他正在打电话＿。', ['呢', '吗', '了'], '呢', ('正在…呢 : action en cours.', '正在…呢: action in progress.'), ('Il est en train de téléphoner.', 'He is on the phone.')),
        FB(COMPLETE, '她穿＿一件红衣服。', ['着', '过', '得'], '着', ('État qui dure : verbe + 着.', 'Lasting state: verb + 着.'), ('Elle porte un vêtement rouge.', 'She is wearing a red top.')),
        DC(ANSWER, [('妈妈', '你在找什么？')], ('Ta mère te demande ce que tu cherches (ton téléphone).', 'Your mother asks what you’re looking for (your phone).'), ['我在找我的手机。', '我在等我的手机。', '我在洗手机。'], '我在找我的手机。', ('Chercher : 找.', 'To look for: 找.')),
        TF('我在等公共汽车。', ('La personne attend le bus.', 'The speaker is waiting for the bus.'), VRAI, ('等 = attendre.', '等 = to wait.')),
      ]),
  ]),
  CH('hsk2-w7-c2', ('Bientôt, c’est fait', 'Soon, done'), [
    L('zh-yao-le', ('Bientôt : 要…了 ; le résultat : 完、到、懂', 'Soon: 要…了; results: 完, 到, 懂'), ('Annoncer ce qui va arriver et dire si une action a abouti.', 'Announce what is about to happen and say whether an action succeeded.'), 10, [
        ('要 / 快 / 快要 + verbe + 了 = bientôt, sur le point de : 要下雨了 (il va pleuvoir), 火车快到了 (le train arrive bientôt).', '要 / 快 / 快要 + verb + 了 = soon, about to: 要下雨了 (it’s going to rain), 火车快到了 (the train is about to arrive).'),
        ('Après un verbe, un second mot dit le résultat : 看完 (finir de lire), 找到 (trouver, au bout de la recherche), 听懂 (comprendre en écoutant). Négation : 没 + verbe + résultat : 我没听懂.', 'After a verb, a second word gives the result: 看完 (finish reading), 找到 (find, at the end of searching), 听懂 (understand what you hear). Negative: 没 + verb + result: 我没听懂.'),
        ('Le temps : 晴 (qíng, ensoleillé), 阴 (yīn, couvert), 下雪 (neiger). 准备 (zhǔnbèi) = préparer, 开始 (kāishǐ) = commencer.', 'Weather: 晴 (qíng, sunny), 阴 (yīn, overcast), 下雪 (to snow). 准备 (zhǔnbèi) = to prepare, 开始 (kāishǐ) = to begin.'),
      ], [
        ZG('yao-le', '要 / 快…了', 'yào / kuài… le', ('bientôt, sur le point de', 'soon, about to')),
        ZG('result', '动词 + 完 / 到 / 懂', None, ('verbe + résultat', 'verb + result')),
        Z('wan-finish', '完', 'wán', ('finir, terminé', 'to finish, done')),
        Z('dong', '懂', 'dǒng', ('comprendre', 'to understand')),
        Z('zhunbei', '准备', 'zhǔnbèi', ('préparer', 'to prepare')),
        Z('kaishi', '开始', 'kāishǐ', ('commencer', 'to begin')),
        Z('qing-sunny', '晴', 'qíng', ('ensoleillé, beau', 'sunny, clear')),
        Z('yin', '阴', 'yīn', ('couvert, nuageux', 'overcast, cloudy')),
        Z('xue', '雪', 'xuě', ('neige', 'snow')),
        Z('qichuang', '起床', 'qǐchuáng', ('se lever', 'to get up')),
      ], [
        x('天阴了，要下雨了，我们回家吧。', 'Tiān yīn le, yào xià yǔ le, wǒmen huí jiā ba.', 'Le ciel se couvre, il va pleuvoir, rentrons.', 'It’s clouding over, it’s going to rain, let’s go home.'),
        x('老师说的话，你听懂了吗？——没听懂。', 'Lǎoshī shuō de huà, nǐ tīngdǒng le ma? — Méi tīngdǒng.', 'Tu as compris ce que le professeur a dit ? — Non.', 'Did you understand what the teacher said? — No.'),
      ], [
        FB(COMPLETE, '快八点了，电影要开始＿。', ['了', '着', '过'], '了', ('Bientôt : 要…了.', 'Soon: 要…了.'), ('Il est presque huit heures, le film va commencer.', 'It’s nearly eight, the film is about to start.')),
        FB(COMPLETE, '我找＿我的手表了！', ['到', '完', '懂'], '到', ('Trouver au bout de la recherche : 找到.', 'Find after searching: 找到.'), ('J’ai retrouvé ma montre !', 'I found my watch!')),
        FB(COMPLETE, '这本书你看＿了吗？', ['完', '到', '着'], '完', ('Finir de lire : 看完.', 'Finish reading: 看完.'), ('Tu as fini ce livre ?', 'Have you finished this book?')),
        TF('明天是晴天。', ('Demain, il fera beau.', 'Tomorrow will be sunny.'), VRAI, ('晴天 = un jour de beau temps.', '晴天 = a sunny day.')),
      ]),
  ])])

# ═════════════════════════ 8 : la cour du roi Helü — relations, parole ═════════════════════════
W8 = WORLD('hsk2-w8', ('La cour du roi Helü', 'The court of King Helü'), REGION,
  ('La famille élargie et les fêtes, donner et faire faire (给, 送, 让), dire et expliquer (告诉, 介绍, 回答), opposer avec 虽然…但是, l’école et les examens.', 'Extended family and celebrations, giving and making someone do (给, 送, 让), telling and explaining (告诉, 介绍, 回答), contrasting with 虽然…但是, school and exams.'),
  (('Le Chiyou des batailles', 'Chiyou of the Battles'), '蚩', ('Chiyou, dieu de la guerre aux huit bras et au front de bronze, se dresse devant la cour du roi Helü. Avant de livrer l’art de la guerre au roi, prouve que tu sais parler, expliquer et convaincre.', 'Chiyou, the god of war with eight arms and a bronze brow, rises before King Helü’s court. Before handing the art of war to the king, prove that you can speak, explain and persuade.')),
  [CH('hsk2-w8-c1', ('La famille du roi', 'The king’s family'), [
    HL('zh-hz-speech', ('Les caractères de la parole : 让 给 告 诉 问 知 道 真', 'Speech characters: 让 给 告 诉 问 知 道 真'), ('Reconnaître les caractères pour dire, donner et savoir.', 'Recognise the characters for saying, giving and knowing.'), [
      ('诉 (sù) et 让 (ràng) portent la parole 讠 ; 问 (wèn, demander) une bouche 口 dans une porte 门 : on interroge au seuil.', '诉 (sù) and 让 (ràng) carry speech 讠; 问 (wèn, to ask) has a mouth 口 in a door 门: you ask at the threshold.'),
      ('知道 (zhīdào) = savoir : 知 (connaître) + 道 (la voie). 道 est aussi le Dao des philosophes.', '知道 (zhīdào) = to know: 知 (to know) + 道 (the way). 道 is also the Dao of the philosophers.'),
    ], [
      H('rang', '让', 'ràng', ('laisser, faire faire', 'to let, to make (someone do)'), 5), H('gei', '给', 'gěi', ('donner, à', 'to give, to, for'), 9), H('gao-tell', '告', 'gào', ('annoncer', 'to announce'), 7), H('su', '诉', 'sù', ('dire, confier', 'to tell, to confide'), 7),
      H('wen', '问', 'wèn', ('demander, interroger', 'to ask'), 6), H('zhi', '知', 'zhī', ('savoir, connaître', 'to know'), 8), H('dao-way', '道', 'dào', ('voie, chemin', 'way, path'), 12), H('zhen', '真', 'zhēn', ('vrai, vraiment', 'true, really'), 10),
    ]),
    L('zh-family2', ('Frères, sœurs, époux : la famille et les fêtes', 'Brothers, sisters, spouses: family and celebrations'), ('Présenter toute sa famille et souhaiter un anniversaire.', 'Introduce your whole family and wish someone happy birthday.'), 9, [
        ('Frères et sœurs selon l’âge : 哥哥 (grand frère), 弟弟 (petit frère), 姐姐 (grande sœur), 妹妹 (petite sœur). Époux : 丈夫 (mari), 妻子 (épouse).', 'Siblings by age: 哥哥 (older brother), 弟弟 (younger brother), 姐姐 (older sister), 妹妹 (younger sister). Spouses: 丈夫 (husband), 妻子 (wife).'),
        ('孩子 (háizi) = enfant ; 男人 / 女人 = homme / femme. 生日快乐！= joyeux anniversaire ! 送 (sòng) = offrir, raccompagner : 我送你一个手表.', '孩子 (háizi) = child; 男人 / 女人 = man / woman. 生日快乐！= happy birthday! 送 (sòng) = to give (as a gift), to see off: 我送你一个手表.'),
        ('姓 (xìng) = avoir pour nom de famille : 我姓王. Poli : 您贵姓？(quel est votre nom ?)', '姓 (xìng) = to have as surname: 我姓王. Polite: 您贵姓？(what is your surname?)'),
      ], [
        Z('gege', '哥哥', 'gēge', ('grand frère', 'older brother')),
        Z('didi', '弟弟', 'dìdi', ('petit frère', 'younger brother')),
        Z('jiejie', '姐姐', 'jiějie', ('grande sœur', 'older sister')),
        Z('meimei', '妹妹', 'mèimei', ('petite sœur', 'younger sister')),
        Z('zhangfu', '丈夫', 'zhàngfu', ('mari', 'husband')),
        Z('qizi', '妻子', 'qīzi', ('épouse, femme', 'wife')),
        Z('haizi', '孩子', 'háizi', ('enfant', 'child')),
        Z('shengri', '生日', 'shēngrì', ('anniversaire', 'birthday')),
        Z('kuaile', '快乐', 'kuàilè', ('joyeux, heureux', 'happy, joyful')),
        Z('song', '送', 'sòng', ('offrir ; raccompagner', 'to give (a gift); to see off')),
        Z('xing', '姓', 'xìng', ('avoir pour nom de famille', 'to be surnamed')),
      ], [
        x('我有一个哥哥和两个妹妹。', 'Wǒ yǒu yí ge gēge hé liǎng ge mèimei.', 'J’ai un grand frère et deux petites sœurs.', 'I have one older brother and two younger sisters.'),
        x('今天是我妻子的生日，我送她一个新手表。', 'Jīntiān shì wǒ qīzi de shēngrì, wǒ sòng tā yí ge xīn shǒubiǎo.', 'C’est l’anniversaire de ma femme, je lui offre une nouvelle montre.', 'It’s my wife’s birthday today; I’m giving her a new watch.'),
      ], [
        FB(COMPLETE, '＿快乐！', ['生日', '妻子', '孩子'], '生日', ('Joyeux anniversaire : 生日快乐.', 'Happy birthday: 生日快乐.'), ('Joyeux anniversaire !', 'Happy birthday!')),
        FB(COMPLETE, '他是我＿，他比我大两岁。', ['哥哥', '弟弟', '妹妹'], '哥哥', ('Plus âgé, garçon : 哥哥.', 'Older, male: 哥哥.'), ('C’est mon grand frère, il a deux ans de plus que moi.', 'He’s my older brother, two years older than me.')),
        DC(ANSWER, [('王老师', '您贵姓？')], ('On te demande poliment ton nom de famille (Li).', 'You are politely asked your surname (Li).'), ['我姓李。', '我是李。', '我叫姓。'], '我姓李。', ('Nom de famille : 我姓 + nom.', 'Surname: 我姓 + name.')),
        TF('她丈夫是医生。', ('Son mari est médecin.', 'Her husband is a doctor.'), VRAI, ('丈夫 = mari.', '丈夫 = husband.')),
      ]),
    L('zh-gei-rang', ('Donner, dire, faire faire : 给、告诉、让', 'Giving, telling, making: 给, 告诉, 让'), ('Dire à qui l’on donne ou parle, et faire faire quelque chose.', 'Say who you give to or talk to, and get someone to do something.'), 10, [
        ('给 = donner, ou « à / pour » devant le verbe : 给我一杯水 (donne-moi un verre d’eau), 我给妈妈打电话 (je téléphone à maman).', '给 = to give, or “to / for” before the verb: 给我一杯水 (give me a glass of water), 我给妈妈打电话 (I call mum).'),
        ('告诉 (gàosu) = dire à, informer : 请告诉我你的名字. 介绍 (jièshào) = présenter : 我介绍一下 (je fais les présentations). 帮助 (bāngzhù) = aider.', '告诉 (gàosu) = to tell, to inform: 请告诉我你的名字. 介绍 (jièshào) = to introduce: 我介绍一下 (let me introduce). 帮助 (bāngzhù) = to help.'),
        ('A 让 B + verbe = A fait faire / laisse B faire : 妈妈让我早点儿睡觉 (maman me dit de me coucher tôt). 一下 après un verbe adoucit : 等一下 (attends un peu).', 'A 让 B + verb = A makes / lets B do: 妈妈让我早点儿睡觉 (mum tells me to go to bed early). 一下 after a verb softens it: 等一下 (wait a moment).'),
      ], [
        ZG('rang', 'A 让 B + 动词', 'ràng', ('faire faire, laisser faire', 'to make / let someone do')),
        ZG('gei', '给 + 人 + 动词', 'gěi', ('faire pour / à quelqu’un', 'to do for / to someone')),
        ZG('yixia', '动词 + 一下', 'yíxià', ('un peu, un instant (adoucit)', 'a bit, a moment (softens)')),
        Z('gei', '给', 'gěi', ('donner ; à, pour', 'to give; to, for')),
        Z('rang', '让', 'ràng', ('laisser, faire faire', 'to let, to make')),
        Z('gaosu', '告诉', 'gàosu', ('dire à, informer', 'to tell')),
        Z('jieshao', '介绍', 'jièshào', ('présenter', 'to introduce')),
        Z('bangzhu', '帮助', 'bāngzhù', ('aider', 'to help')),
        Z('zhidao', '知道', 'zhīdào', ('savoir, connaître', 'to know')),
        Z('xiwang', '希望', 'xīwàng', ('espérer', 'to hope')),
        Z('wen', '问', 'wèn', ('demander, poser une question', 'to ask (a question)')),
        Z('huida', '回答', 'huídá', ('répondre', 'to answer')),
      ], [
        x('我介绍一下，这是我的朋友大卫。', 'Wǒ jièshào yíxià, zhè shì wǒ de péngyou Dàwèi.', 'Je fais les présentations : voici mon ami David.', 'Let me introduce you: this is my friend David.'),
        x('老师让我们回答问题。', 'Lǎoshī ràng wǒmen huídá wèntí.', 'Le professeur nous fait répondre aux questions.', 'The teacher asks us to answer the questions.'),
      ], [
        FB(COMPLETE, '请＿我你的手机号。', ['告诉', '介绍', '回答'], '告诉', ('Dire à quelqu’un : 告诉 + personne.', 'Tell someone: 告诉 + person.'), ('Dis-moi ton numéro de portable, s’il te plaît.', 'Please tell me your mobile number.')),
        FB(COMPLETE, '晚上我＿妈妈打电话。', ['给', '让', '从'], '给', ('Téléphoner à quelqu’un : 给 + personne + 打电话.', 'Call someone: 给 + person + 打电话.'), ('Ce soir, je téléphone à maman.', 'This evening I’ll call mum.')),
        SO(ORDER('Le médecin me dit de beaucoup me reposer.', 'The doctor tells me to rest a lot.'), ['医生', '让', '我', '多', '休息。'], ('A 让 B + verbe.', 'A 让 B + verb.')),
        TF('我不知道他叫什么名字。', ('La personne connaît son nom.', 'The speaker knows his name.'), FAUX, ('不知道 = ne pas savoir.', '不知道 = not know.')),
      ]),
  ]),
  CH('hsk2-w8-c2', ('Le livre du stratège', 'The strategist’s book'), [
    L('zh-suiran', ('Opposer : 虽然…但是 ; adverbes 就、还、再、真', 'Contrasting: 虽然…但是; adverbs 就, 还, 再, 真'), ('Nuancer une idée et préciser le moment.', 'Qualify an idea and be precise about timing.'), 10, [
        ('虽然…，但是… = bien que…, (pourtant)… : 虽然很累，但是我很快乐. Comme 因为…所以, on garde les deux mots.', '虽然…，但是… = although…, (still)…: 虽然很累，但是我很快乐. As with 因为…所以, both words are kept.'),
        ('就 (jiù) = dès, tout de suite, justement : 我明天就走. 还 (hái) = encore, en plus : 他还没来. 再 (zài) = de nouveau (à l’avenir) : 明天再来吧.', '就 (jiù) = right away, exactly: 我明天就走. 还 (hái) = still, also: 他还没来. 再 (zài) = again (in the future): 明天再来吧.'),
        ('真 (zhēn) = vraiment : 你真好！对 (duì) = juste, correct ; 错 (cuò) = faux, erreur.', '真 (zhēn) = really: 你真好！对 (duì) = right, correct; 错 (cuò) = wrong, mistake.'),
      ], [
        ZG('suiran-danshi', '虽然…，但是…', 'suīrán…, dànshì…', ('bien que…, pourtant…', 'although…, still…')),
        Z('suiran', '虽然', 'suīrán', ('bien que, même si', 'although')),
        Z('danshi', '但是', 'dànshì', ('mais, pourtant', 'but, however')),
        Z('jiu-then', '就', 'jiù', ('tout de suite, justement', 'right away, exactly')),
        Z('hai', '还', 'hái', ('encore, toujours', 'still, yet')),
        Z('zai-again', '再', 'zài', ('de nouveau, encore (à l’avenir)', 'again (in the future)')),
        Z('zhen', '真', 'zhēn', ('vraiment', 'really')),
        Z('dui', '对', 'duì', ('juste, correct', 'right, correct')),
        Z('cuo', '错', 'cuò', ('faux, erroné', 'wrong')),
      ], [
        x('虽然汉语很难，但是我很喜欢。', 'Suīrán Hànyǔ hěn nán, dànshì wǒ hěn xǐhuan.', 'Bien que le chinois soit difficile, je l’adore.', 'Although Chinese is hard, I love it.'),
        x('他还没来，我们再等一下吧。', 'Tā hái méi lái, wǒmen zài děng yíxià ba.', 'Il n’est pas encore arrivé, attendons encore un peu.', 'He hasn’t come yet; let’s wait a little longer.'),
      ], [
        FB(COMPLETE, '虽然下雪了，＿他还是去跑步了。', ['但是', '所以', '因为'], '但是', ('Opposition : 虽然…，但是….', 'Contrast: 虽然…，但是….'), ('Même s’il neigeait, il est quand même allé courir.', 'Although it snowed, he still went running.')),
        FB(COMPLETE, '他＿没起床。', ['还', '再', '就'], '还', ('Toujours pas : 还没.', 'Not yet: 还没.'), ('Il n’est toujours pas levé.', 'He still hasn’t got up.')),
        FB(COMPLETE, '今天太忙了，明天＿说吧。', ['再', '还', '就'], '再', ('De nouveau, plus tard : 再.', 'Again, later: 再.'), ('Je suis trop occupé aujourd’hui, on en reparle demain.', 'I’m too busy today; let’s talk tomorrow.')),
        TF('你说得对。', ('Tu as raison.', 'You are right.'), VRAI, ('说得对 = dire juste.', '说得对 = say it right.')),
      ]),
    L('zh-school', ('À l’école : 考试、课、题、意思', 'At school: 考试, 课, 题, 意思'), ('Parler des cours, des examens et du sens des mots.', 'Talk about classes, exams and what words mean.'), 9, [
        ('考试 (kǎoshì) = examen, passer un examen ; 题 (tí) = question d’examen, exercice ; 课 (kè) = cours, leçon ; 教室 (jiàoshì) = salle de classe.', '考试 (kǎoshì) = exam, to take an exam; 题 (tí) = exam question, exercise; 课 (kè) = class, lesson; 教室 (jiàoshì) = classroom.'),
        ('意思 (yìsi) = sens : 这个字是什么意思？有意思 = intéressant, amusant. 问题 (wèntí) = question, problème : 没问题！(pas de problème !).', '意思 (yìsi) = meaning: 这个字是什么意思？有意思 = interesting, fun. 问题 (wèntí) = question, problem: 没问题！(no problem!).'),
        ('忙 (máng) = occupé ; 上班 (shàngbān) = aller au travail ; 报纸 (bàozhǐ) = journal ; 铅笔 (qiānbǐ) = crayon.', '忙 (máng) = busy; 上班 (shàngbān) = to go to work; 报纸 (bàozhǐ) = newspaper; 铅笔 (qiānbǐ) = pencil.'),
      ], [
        Z('kaoshi', '考试', 'kǎoshì', ('examen', 'exam')),
        Z('ke', '课', 'kè', ('cours, leçon', 'class, lesson')),
        Z('jiaoshi', '教室', 'jiàoshì', ('salle de classe', 'classroom')),
        Z('ti', '题', 'tí', ('question (d’examen), exercice', 'question (in an exam), exercise')),
        Z('yisi', '意思', 'yìsi', ('sens, signification', 'meaning')),
        Z('wenti', '问题', 'wèntí', ('question, problème', 'question, problem')),
        Z('mang', '忙', 'máng', ('occupé', 'busy')),
        Z('shangban', '上班', 'shàngbān', ('aller au travail', 'to go to work')),
        Z('baozhi', '报纸', 'bàozhǐ', ('journal', 'newspaper')),
        Z('qianbi', '铅笔', 'qiānbǐ', ('crayon', 'pencil')),
        Z('shiqing', '事情', 'shìqing', ('affaire, chose (à faire)', 'matter, thing (to do)')),
        Z('dajia', '大家', 'dàjiā', ('tout le monde', 'everyone')),
        Z('ta-it', '它', 'tā', ('il, elle (objet, animal)', 'it')),
        Z('nin', '您', 'nín', ('vous (de politesse)', 'you (polite)')),
      ], [
        x('明天有汉语考试，大家准备好了吗？', 'Míngtiān yǒu Hànyǔ kǎoshì, dàjiā zhǔnbèi hǎo le ma?', 'Demain il y a l’examen de chinois, tout le monde est prêt ?', 'There’s a Chinese exam tomorrow; is everyone ready?'),
        x('这个电影很有意思。', 'Zhè ge diànyǐng hěn yǒu yìsi.', 'Ce film est très intéressant.', 'This film is very interesting.'),
      ], [
        FB(COMPLETE, '这个字是什么＿？', ['意思', '问题', '事情'], '意思', ('Le sens : 意思.', 'Meaning: 意思.'), ('Que veut dire ce caractère ?', 'What does this character mean?')),
        FB(COMPLETE, '你能帮我吗？——没＿！', ['问题', '意思', '事情'], '问题', ('Pas de problème : 没问题.', 'No problem: 没问题.'), ('Tu peux m’aider ? — Pas de problème !', 'Can you help me? — No problem!')),
        DC(ANSWER, [('小王', '你今天忙吗？')], ('Xiao Wang te demande si tu es occupé (oui, tu as un examen).', 'Xiao Wang asks if you are busy (yes, you have an exam).'), ['很忙，我有考试。', '很忙，我是考试。', '不忙，我很累。'], '很忙，我有考试。', ('Occupé : 忙 ; avoir un examen : 有考试.', 'Busy: 忙; have an exam: 有考试.')),
        TF('教室里有很多学生。', ('La salle de classe est vide.', 'The classroom is empty.'), FAUX, ('很多学生 = beaucoup d’élèves.', '很多学生 = many students.')),
      ]),
  ])])

write_level(2, ('HSK 2 : l’art de la guerre', 'HSK 2: the art of war'), REGION, 'Banks of the Yangtze',
  [W1, W2, W3, W4, W5, W6, W7, W8, FINAL(2, REGION, ('Simulation HSK 2 : le palais de Gusu', 'HSK 2 simulation: the palace of Gusu'), 200, 120, 'écoute (听力) et lecture (阅读)', 'listening (听力) and reading (阅读)')])
