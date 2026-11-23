# Lecture en chinois : fables des Royaumes combattants (domaine public : Han Feizi, Stratagèmes des Royaumes combattants),
# réécrites en chinois simple. Ajoute (ou remplace) les contes chinois dans content/reading/stories.json.
# Les phrases s'écrivent mot à mot : « 农民:nóngmín » (mot et pinyin), la ponctuation seule. Le pinyin est affiché
# au-dessus des mots (notation {汉字|pinyin}) : tous les mots au HSK 1 et 2, puis de moins en moins (voir PINYIN_FROM).
# Usage : python3 scripts/zh-reading.py
import json, os
ROOT = os.path.join(os.path.dirname(__file__), '..')
P = os.path.join(ROOT, 'content/reading/stories.json')

def tokens(seg):
    for tok in seg.split():
        if ':' in tok:
            zh, py = tok.split(':')
            yield zh, py.replace('_', ' ')
        else:
            yield tok, None

def S(seg, fr, en, annotate=lambda zh: True):
    """Phrase : le texte avec pinyin {汉字|pinyin} et le texte à prononcer (caractères seuls)."""
    jp, kana = '', ''
    for zh, py in tokens(seg):
        kana += zh
        jp += f'{{{zh}|{py}}}' if py and annotate(zh) else zh
    return {'jp': jp, 'fr': fr, 'en': en, 'kana': kana}

def W(zh, py, fr, en):
    return {'jp': zh, 'reading': py, 'fr': fr, 'en': en}

def Q(q, choices, answer):
    return {'q': {'fr': q[0], 'en': q[1]}, 'choices': [{'fr': f, 'en': e} for f, e in choices], 'answer': answer}

def CH(slug, title, paragraphs, words, questions):
    zh, fr, en = title
    return {'slug': slug, 'title': {'jp': zh, 'fr': fr, 'en': en}, 'paragraphs': paragraphs, 'words': words, 'questions': questions}

def STORY(slug, glyph, level, color, title, summary, chapters):
    zh, fr, en = title
    return {'slug': slug, 'glyph': glyph, 'level': level, 'color': color, 'title': {'jp': zh, 'fr': fr, 'en': en}, 'summary': {'fr': summary[0], 'en': summary[1]}, 'chapters': chapters}

# ═════════════════════════ 守株待兔 (royaume de Song) ═════════════════════════
SHOUZHU = STORY('shou-zhu-dai-tu', '兔', 'HSK1', '#B5793A', ('守株待兔', 'Le paysan qui attendait le lièvre', 'The farmer who waited for the hare'),
  ('Un paysan du royaume de Song voit un lièvre se cogner contre un arbre. Pourquoi travailler encore ?', 'A farmer of the state of Song sees a hare run into a tree. Why work any more?'), [
  CH('shou-zhu-dai-tu-1', ('宋国的农民', 'Le paysan de Song', 'The farmer of Song'), [
    [S('从前:cóngqián ， 宋国:Sòngguó 有:yǒu 一个:yí_ge 农民:nóngmín 。', 'Autrefois, dans le royaume de Song, vivait un paysan.', 'Long ago, in the state of Song, there lived a farmer.'),
     S('他:tā 每天:měi_tiān 在:zài 田:tián 里:li 工作:gōngzuò 。', 'Chaque jour, il travaillait dans son champ.', 'Every day he worked in his field.'),
     S('他的:tā_de 田:tián 里:li 有:yǒu 一:yì 棵:kē 大:dà 树:shù 。', 'Dans son champ, il y avait un grand arbre.', 'In his field there was a big tree.')],
    [S('一天:yì_tiān ， 他:tā 工作:gōngzuò 的:de 时候:shíhou ， 一只:yì_zhī 兔子:tùzi 跑:pǎo 来:lái 了:le 。', 'Un jour, pendant qu’il travaillait, un lièvre arriva en courant.', 'One day, while he was working, a hare came running.'),
     S('兔子:tùzi 跑:pǎo 得:de 太:tài 快:kuài 了:le ， 撞:zhuàng 在:zài 树:shù 上:shang ， 死:sǐ 了:le 。', 'Le lièvre courait trop vite : il se cogna contre l’arbre et mourut.', 'The hare was running too fast: it crashed into the tree and died.'),
     S('农民:nóngmín 很:hěn 高兴:gāoxìng ： “ 太:tài 好:hǎo 了:le ！ ”', 'Le paysan était ravi : « Formidable ! »', 'The farmer was delighted: “Wonderful!”')],
  ], [
    W('从前', 'cóngqián', 'autrefois', 'long ago'),
    W('农民', 'nóngmín', 'paysan', 'farmer'),
    W('田', 'tián', 'champ', 'field'),
    W('树', 'shù', 'arbre', 'tree'),
    W('兔子', 'tùzi', 'lièvre, lapin', 'hare, rabbit'),
    W('跑', 'pǎo', 'courir', 'to run'),
    W('快', 'kuài', 'rapide, vite', 'fast'),
  ], [
    Q(('Où travaillait le paysan ?', 'Where did the farmer work?'), [('Au marché', 'At the market'), ('Dans son champ', 'In his field'), ('À l’école', 'At school')], 1),
    Q(('Que s’est-il passé avec le lièvre ?', 'What happened to the hare?'), [('Il s’est cogné contre l’arbre', 'It crashed into the tree'), ('Il a mangé le riz', 'It ate the rice'), ('Il s’est enfui', 'It ran away')], 0),
  ]),
  CH('shou-zhu-dai-tu-2', ('等兔子', 'Attendre le lièvre', 'Waiting for the hare'), [
    [S('农民:nóngmín 回家:huí_jiā 了:le 。', 'Le paysan rentra chez lui.', 'The farmer went home.'),
     S('那天:nà_tiān 晚上:wǎnshang ， 他:tā 吃:chī 了:le 兔子:tùzi ， 很:hěn 高兴:gāoxìng 。', 'Ce soir-là, il mangea le lièvre, très content.', 'That evening he ate the hare and was very happy.'),
     S('他:tā 想:xiǎng ： “ 我:wǒ 不:bù 想:xiǎng 工作:gōngzuò 了:le 。 我:wǒ 在:zài 树:shù 下:xià 等:děng 兔子:tùzi ！ ”', 'Il pensa : « Je n’ai plus envie de travailler. Je vais attendre les lièvres sous l’arbre ! »', 'He thought: “I don’t want to work any more. I’ll wait for hares under the tree!”')],
    [S('第二天:dì-èr_tiān ， 他:tā 没:méi 去:qù 田:tián 里:li 工作:gōngzuò 。', 'Le lendemain, il n’alla pas travailler dans son champ.', 'The next day he didn’t go to work in his field.'),
     S('他:tā 坐:zuò 在:zài 树:shù 下:xià ， 等:děng 兔子:tùzi 来:lái 。', 'Il s’assit sous l’arbre et attendit qu’un lièvre arrive.', 'He sat under the tree, waiting for a hare to come.'),
     S('一天:yì_tiān 、 两天:liǎng_tiān 、 三天:sān_tiān …… 兔子:tùzi 没有:méiyǒu 来:lái 。', 'Un jour, deux jours, trois jours… aucun lièvre ne vint.', 'One day, two days, three days… no hare came.')],
  ], [
    W('回家', 'huí jiā', 'rentrer à la maison', 'to go home'),
    W('晚上', 'wǎnshang', 'soir', 'evening'),
    W('等', 'děng', 'attendre', 'to wait'),
    W('第二天', 'dì-èr tiān', 'le lendemain', 'the next day'),
    W('坐', 'zuò', 's’asseoir', 'to sit'),
    W('树下', 'shù xià', 'sous l’arbre', 'under the tree'),
  ], [
    Q(('Que mange le paysan ce soir-là ?', 'What does the farmer eat that evening?'), [('Le lièvre', 'The hare'), ('Du riz', 'Rice'), ('Une pomme', 'An apple')], 0),
    Q(('Que fait-il le lendemain ?', 'What does he do the next day?'), [('Il travaille dans son champ', 'He works in his field'), ('Il s’assoit sous l’arbre et attend', 'He sits under the tree and waits'), ('Il va au marché', 'He goes to the market')], 1),
  ]),
  CH('shou-zhu-dai-tu-3', ('田里没有米', 'Plus de riz dans le champ', 'No rice left in the field'), [
    [S('很多:hěn_duō 天:tiān 过去:guòqu 了:le 。', 'Bien des jours passèrent.', 'Many days went by.'),
     S('农民:nóngmín 每天:měi_tiān 坐:zuò 在:zài 树:shù 下:xià ， 可是:kěshì 一只:yì_zhī 兔子:tùzi 也:yě 没有:méiyǒu 来:lái 。', 'Chaque jour, le paysan restait assis sous l’arbre, mais pas un seul lièvre ne vint.', 'Every day the farmer sat under the tree, but not a single hare came.'),
     S('他的:tā_de 田:tián 里:li 没有:méiyǒu 米:mǐ ， 也:yě 没有:méiyǒu 菜:cài 。', 'Dans son champ, il n’y avait plus ni riz ni légumes.', 'In his field there was no rice and no vegetables.')],
    [S('宋国:Sòngguó 的:de 人:rén 都:dōu 笑:xiào 他:tā 。', 'Tous les gens de Song se moquaient de lui.', 'All the people of Song laughed at him.'),
     S('他们:tāmen 说:shuō ： “ 你:nǐ 不:bù 工作:gōngzuò ， 只:zhǐ 等:děng 兔子:tùzi ， 太:tài 不:bù 聪明:cōngming 了:le ！ ”', 'Ils disaient : « Tu ne travailles pas, tu ne fais qu’attendre les lièvres, ce n’est vraiment pas malin ! »', 'They said: “You don’t work, you just wait for hares — that’s really not clever!”'),
     S('这:zhè 就是:jiù_shì “ 守株待兔:shǒu_zhū_dài_tù ” 。', 'Voilà l’histoire de « garder la souche en attendant le lièvre ».', 'That is the story of “guarding the stump, waiting for the hare”.')],
  ], [
    W('过去', 'guòqu', 'passer (le temps)', 'to pass (time)'),
    W('可是', 'kěshì', 'mais', 'but'),
    W('都', 'dōu', 'tous, tout', 'all'),
    W('笑', 'xiào', 'rire, se moquer', 'to laugh'),
    W('只', 'zhǐ', 'seulement', 'only'),
    W('聪明', 'cōngming', 'intelligent, malin', 'clever'),
  ], [
    Q(('Combien de lièvres sont venus ensuite ?', 'How many hares came after that?'), [('Un seul', 'Just one'), ('Aucun', 'None'), ('Trois', 'Three')], 1),
    Q(('Que disent les gens de Song ?', 'What do the people of Song say?'), [('Qu’il est courageux', 'That he is brave'), ('Qu’il n’est pas très malin', 'That he is not very clever'), ('Qu’il est riche', 'That he is rich')], 1),
  ]),
])

# ═════════════════════════ 画蛇添足 (royaume de Chu) ═════════════════════════
HUASHE = STORY('hua-she-tian-zu', '蛇', 'HSK1', '#3F8F5B', ('画蛇添足', 'Le serpent à pattes', 'The snake with legs'),
  ('À Chu, des amis jouent une coupe de vin à qui dessinera un serpent le plus vite. Le plus rapide en fait un peu trop…', 'In Chu, friends compete for a cup of wine: whoever draws a snake fastest wins it. The fastest one goes a little too far…'), [
  CH('hua-she-tian-zu-1', ('一杯酒', 'Une coupe de vin', 'A cup of wine'), [
    [S('从前:cóngqián ， 楚国:Chǔguó 有:yǒu 一个:yí_ge 人:rén 。', 'Autrefois, dans le royaume de Chu, vivait un homme.', 'Long ago, in the state of Chu, there lived a man.'),
     S('他:tā 请:qǐng 朋友们:péngyoumen 来:lái 家:jiā 里:li 吃饭:chī_fàn 。', 'Il invita ses amis à manger chez lui.', 'He invited his friends to his house for a meal.'),
     S('吃:chī 了:le 饭:fàn ， 他:tā 给:gěi 朋友们:péngyoumen 一:yì 杯:bēi 酒:jiǔ 。', 'Après le repas, il offrit à ses amis une coupe de vin.', 'After the meal, he gave his friends a cup of wine.')],
    [S('朋友们:péngyoumen 说:shuō ： “ 我们:wǒmen 有:yǒu 很多:hěn_duō 人:rén ， 可是:kěshì 只:zhǐ 有:yǒu 一:yì 杯:bēi 酒:jiǔ 。 ”', 'Les amis dirent : « Nous sommes nombreux, mais il n’y a qu’une coupe de vin. »', 'The friends said: “There are many of us, but there is only one cup of wine.”'),
     S('一个:yí_ge 人:rén 说:shuō ： “ 我们:wǒmen 画:huà 蛇:shé 吧:ba ！ ”', 'L’un d’eux dit : « Dessinons un serpent ! »', 'One of them said: “Let’s draw a snake!”'),
     S('“ 谁:shéi 先:xiān 画:huà 好:hǎo ， 谁:shéi 喝:hē 这:zhè 杯:bēi 酒:jiǔ ！ ”', '« Le premier qui a fini boit la coupe ! »', '“Whoever finishes first drinks the cup!”')],
  ], [
    W('楚国', 'Chǔguó', 'le royaume de Chu', 'the state of Chu'),
    W('给', 'gěi', 'donner', 'to give'),
    W('酒', 'jiǔ', 'vin, alcool', 'wine, alcohol'),
    W('画', 'huà', 'dessiner', 'to draw'),
    W('蛇', 'shé', 'serpent', 'snake'),
    W('先', 'xiān', 'd’abord, en premier', 'first'),
  ], [
    Q(('Combien de coupes de vin y a-t-il ?', 'How many cups of wine are there?'), [('Une', 'One'), ('Deux', 'Two'), ('Beaucoup', 'Many')], 0),
    Q(('Que décident les amis ?', 'What do the friends decide?'), [('De dessiner un serpent', 'To draw a snake'), ('De chanter', 'To sing'), ('De partager le vin', 'To share the wine')], 0),
  ]),
  CH('hua-she-tian-zu-2', ('蛇有脚吗？', 'Les serpents ont-ils des pattes ?', 'Do snakes have legs?'), [
    [S('大家:dàjiā 都:dōu 在:zài 地上:dìshang 画:huà 蛇:shé 。', 'Tout le monde se mit à dessiner un serpent par terre.', 'Everyone began drawing a snake on the ground.'),
     S('一个:yí_ge 人:rén 画:huà 得:de 很:hěn 快:kuài ， 他:tā 先:xiān 画:huà 好:hǎo 了:le 。', 'L’un d’eux dessinait très vite : il finit le premier.', 'One of them drew very fast: he finished first.'),
     S('他:tā 拿:ná 起:qǐ 酒杯:jiǔbēi ， 看:kàn 了:le 看:kan 朋友们:péngyoumen 。', 'Il prit la coupe et regarda ses amis.', 'He picked up the cup and looked at his friends.')],
    [S('他:tā 想:xiǎng ： “ 他们:tāmen 画:huà 得:de 太:tài 慢:màn 了:le ！ 我:wǒ 还:hái 能:néng 给:gěi 蛇:shé 画:huà 几:jǐ 只:zhī 脚:jiǎo 。 ”', 'Il pensa : « Ils dessinent trop lentement ! J’ai encore le temps d’ajouter quelques pattes au serpent. »', 'He thought: “They are drawing far too slowly! I can still give the snake a few legs.”'),
     S('他:tā 左手:zuǒshǒu 拿:ná 着:zhe 酒:jiǔ ， 右手:yòushǒu 画:huà 蛇:shé 脚:jiǎo 。', 'La coupe dans la main gauche, il dessina des pattes de la main droite.', 'Holding the wine in his left hand, he drew legs with his right.')],
  ], [
    W('大家', 'dàjiā', 'tout le monde', 'everyone'),
    W('地上', 'dìshang', 'par terre', 'on the ground'),
    W('拿', 'ná', 'prendre, tenir', 'to take, to hold'),
    W('慢', 'màn', 'lent', 'slow'),
    W('还', 'hái', 'encore', 'still'),
    W('脚', 'jiǎo', 'pied, patte', 'foot, leg'),
    W('左手', 'zuǒshǒu', 'main gauche', 'left hand'),
  ], [
    Q(('Qui finit le premier ?', 'Who finishes first?'), [('L’un des amis', 'One of the friends'), ('L’hôte', 'The host'), ('Tout le monde en même temps', 'Everyone at the same time')], 0),
    Q(('Que fait-il une fois son serpent fini ?', 'What does he do once his snake is finished?'), [('Il boit le vin', 'He drinks the wine'), ('Il ajoute des pattes au serpent', 'He adds legs to the snake'), ('Il rentre chez lui', 'He goes home')], 1),
  ]),
  CH('hua-she-tian-zu-3', ('没喝到酒', 'Pas de vin pour lui', 'No wine for him'), [
    [S('这个:zhè_ge 时候:shíhou ， 另:lìng 一个:yí_ge 人:rén 也:yě 画:huà 好:hǎo 了:le 。', 'À ce moment-là, un autre avait fini lui aussi.', 'At that moment, another man finished too.'),
     S('他:tā 拿:ná 过:guò 酒杯:jiǔbēi ， 说:shuō ： “ 蛇:shé 没有:méiyǒu 脚:jiǎo ！ 你:nǐ 画:huà 的:de 不是:bú_shì 蛇:shé 。 ”', 'Il prit la coupe et dit : « Les serpents n’ont pas de pattes ! Ce que tu as dessiné n’est pas un serpent. »', 'He took the cup and said: “Snakes have no legs! What you drew is not a snake.”'),
     S('他:tā 喝:hē 了:le 那:nà 杯:bēi 酒:jiǔ 。', 'Et il but la coupe de vin.', 'And he drank the cup of wine.')],
    [S('给:gěi 蛇:shé 画:huà 脚:jiǎo 的:de 人:rén 没:méi 喝:hē 到:dào 酒:jiǔ 。', 'Celui qui avait dessiné des pattes au serpent n’eut pas de vin.', 'The man who drew legs on the snake got no wine.'),
     S('这:zhè 就是:jiù_shì “ 画蛇添足:huà_shé_tiān_zú ” 。 做:zuò 得:de 太:tài 多:duō ， 有时候:yǒu_shíhou 不:bù 好:hǎo ！', 'Voilà ce qu’on appelle « ajouter des pattes au serpent ». En faire trop, parfois, ce n’est pas bien !', 'That is what is called “adding legs to the snake”. Doing too much is sometimes a bad thing!')],
  ], [
    W('另', 'lìng', 'autre', 'other, another'),
    W('酒杯', 'jiǔbēi', 'coupe de vin', 'wine cup'),
    W('到', 'dào', 'obtenir, arriver à', 'to get, to reach'),
    W('有时候', 'yǒu shíhou', 'parfois', 'sometimes'),
    W('画蛇添足', 'huà shé tiān zú', 'en faire trop et tout gâcher', 'to overdo it and spoil everything'),
    W('不是', 'bú shì', 'ne pas être', 'is not'),
  ], [
    Q(('Pourquoi le deuxième homme boit-il le vin ?', 'Why does the second man drink the wine?'), [('Parce qu’il est le plus âgé', 'Because he is the oldest'), ('Parce qu’un serpent n’a pas de pattes', 'Because a snake has no legs'), ('Parce qu’il a dessiné le plus vite', 'Because he drew the fastest')], 1),
    Q(('Quelle est la morale de l’histoire ?', 'What is the moral of the story?'), [('Il faut toujours finir le premier', 'You must always finish first'), ('En faire trop peut tout gâcher', 'Overdoing it can spoil everything'), ('Il ne faut jamais boire de vin', 'You should never drink wine')], 1),
  ]),
])

# ═════════════════════════ 自相矛盾 (royaume de Chu, Han Feizi) ═════════════════════════
MAODUN = STORY('zi-xiang-mao-dun', '盾', 'HSK1', '#8E1B26', ('自相矛盾', 'La lance et le bouclier', 'The spear and the shield'),
  ('Un marchand de Chu vante une lance qui perce tout et un bouclier que rien ne perce. Un passant pose une question…', 'A merchant of Chu boasts of a spear that pierces everything and a shield nothing can pierce. A passer-by asks a question…'), [
  CH('zi-xiang-mao-dun-1', ('最好的矛', 'La meilleure lance', 'The best spear'), [
    [S('从前:cóngqián ， 楚国:Chǔguó 有:yǒu 一个:yí_ge 人:rén ， 他:tā 卖:mài 矛:máo 和:hé 盾:dùn 。', 'Autrefois, dans le royaume de Chu, un homme vendait des lances et des boucliers.', 'Long ago, in the state of Chu, a man sold spears and shields.'),
     S('他:tā 在:zài 商店:shāngdiàn 前面:qiánmiàn 说:shuō ： “ 请:qǐng 看:kàn 我的:wǒ_de 矛:máo ！ ”', 'Devant sa boutique, il criait : « Regardez ma lance ! »', 'In front of his shop he called out: “Look at my spear!”'),
     S('“ 我的:wǒ_de 矛:máo 是:shì 最:zuì 好:hǎo 的:de ， 什么:shénme 都:dōu 能:néng 刺破:cìpò ！ ”', '« Ma lance est la meilleure, elle perce tout ! »', '“My spear is the best: it can pierce anything!”')],
    [S('他:tā 又:yòu 拿:ná 起:qǐ 盾:dùn ， 说:shuō ： “ 请:qǐng 看:kàn 我的:wǒ_de 盾:dùn ！ ”', 'Puis il prit un bouclier et dit : « Regardez mon bouclier ! »', 'Then he picked up a shield and said: “Look at my shield!”'),
     S('“ 我的:wǒ_de 盾:dùn 也:yě 是:shì 最:zuì 好:hǎo 的:de ， 什么:shénme 都:dōu 不:bù 能:néng 刺破:cìpò 它:tā ！ ”', '« Mon bouclier aussi est le meilleur : rien ne peut le percer ! »', '“My shield is the best too: nothing can pierce it!”'),
     S('很多:hěn_duō 人:rén 来:lái 看:kàn 他的:tā_de 东西:dōngxi 。', 'Beaucoup de gens vinrent voir sa marchandise.', 'Many people came to look at his goods.')],
  ], [
    W('卖', 'mài', 'vendre', 'to sell'),
    W('矛', 'máo', 'lance', 'spear'),
    W('盾', 'dùn', 'bouclier', 'shield'),
    W('最', 'zuì', 'le plus', 'the most'),
    W('刺破', 'cìpò', 'percer', 'to pierce'),
    W('又', 'yòu', 'de nouveau, puis', 'again, then'),
  ], [
    Q(('Que vend l’homme ?', 'What does the man sell?'), [('Des fruits', 'Fruit'), ('Des lances et des boucliers', 'Spears and shields'), ('Des livres', 'Books')], 1),
    Q(('Que dit-il de son bouclier ?', 'What does he say about his shield?'), [('Rien ne peut le percer', 'Nothing can pierce it'), ('Il est très léger', 'It is very light'), ('Il est bon marché', 'It is cheap')], 0),
  ]),
  CH('zi-xiang-mao-dun-2', ('用你的矛刺你的盾', 'Ta lance contre ton bouclier', 'Your spear against your shield'), [
    [S('一个:yí_ge 人:rén 问:wèn 他:tā ： “ 如果:rúguǒ 用:yòng 你的:nǐ_de 矛:máo 刺:cì 你的:nǐ_de 盾:dùn ， 会:huì 怎么样:zěnmeyàng ？ ”', 'Un passant lui demanda : « Et si l’on frappe ton bouclier avec ta lance, que se passe-t-il ? »', 'Someone asked him: “What happens if you strike your shield with your spear?”'),
     S('卖:mài 东西:dōngxi 的:de 人:rén 不:bù 说话:shuōhuà 了:le 。', 'Le marchand se tut.', 'The merchant fell silent.'),
     S('他:tā 不:bù 知道:zhīdào 怎么:zěnme 回答:huídá 。', 'Il ne savait pas quoi répondre.', 'He didn’t know how to answer.')],
    [S('大家:dàjiā 都:dōu 笑:xiào 了:le 。', 'Tout le monde éclata de rire.', 'Everyone burst out laughing.'),
     S('他的:tā_de 话:huà 前后:qiánhòu 不:bù 一样:yíyàng ， 这:zhè 就是:jiù_shì “ 自相矛盾:zì_xiāng_máodùn ” 。', 'Ses paroles ne s’accordaient pas entre elles : voilà ce qu’on appelle « se contredire ».', 'His words did not match each other: this is what is called “contradicting oneself”.')],
  ], [
    W('问', 'wèn', 'demander, interroger', 'to ask'),
    W('如果', 'rúguǒ', 'si', 'if'),
    W('用', 'yòng', 'utiliser', 'to use'),
    W('知道', 'zhīdào', 'savoir', 'to know'),
    W('回答', 'huídá', 'répondre', 'to answer'),
    W('一样', 'yíyàng', 'pareil', 'the same'),
  ], [
    Q(('Quelle question pose le passant ?', 'What question does the passer-by ask?'), [('Combien coûte la lance', 'How much the spear costs'), ('Ce qui se passe si sa lance frappe son bouclier', 'What happens if his spear strikes his shield'), ('Où se trouve sa boutique', 'Where his shop is')], 1),
    Q(('Comment réagit le marchand ?', 'How does the merchant react?'), [('Il ne sait pas quoi répondre', 'He doesn’t know what to answer'), ('Il se met en colère', 'He gets angry'), ('Il baisse ses prix', 'He lowers his prices')], 0),
  ]),
])


# ═════════════════════════ HSK 2 ═════════════════════════
# 孙子练兵 (Mémoires historiques, Sima Qian) — version adoucie : les chefs de file sont remplacés.
SUNZI = STORY('sunzi-lian-bing', '鼓', 'HSK2', '#2F5E7A', ('孙子练兵', 'Le général et les dames de la cour', 'The general and the court ladies'),
  ('Le roi de Wu met le général Sun à l’épreuve : saura-t-il faire de 180 dames de la cour une troupe disciplinée ?', 'The king of Wu puts General Sun to the test: can he turn 180 court ladies into a disciplined troop?'), [
  CH('sunzi-lian-bing-1', ('吴王的考试', 'L’épreuve du roi de Wu', 'The king of Wu’s test'), [
    [S('孙子:Sūnzǐ 写:xiě 了:le 一:yì 本:běn 书:shū ， 叫:jiào 《 孙子兵法:Sūnzǐ_Bīngfǎ 》 。', 'Sunzi écrivit un livre intitulé « L’Art de la guerre de Sunzi ».', 'Sunzi wrote a book called “Sunzi’s Art of War”.'),
     S('吴王:Wú_wáng 看:kàn 完:wán 了:le ， 觉得:juéde 很:hěn 有意思:yǒu_yìsi 。', 'Le roi de Wu le lut jusqu’au bout et le trouva très intéressant.', 'The king of Wu read it to the end and found it very interesting.'),
     S('但是:dànshì 他:tā 想:xiǎng ： “ 他:tā 真:zhēn 的:de 会:huì 带:dài 兵:bīng 吗:ma ？ ”', 'Mais il se demandait : « Sait-il vraiment commander des soldats ? »', 'But he wondered: “Can he really lead soldiers?”')],
    [S('吴王:Wú_wáng 问:wèn 孙子:Sūnzǐ ： “ 你:nǐ 可以:kěyǐ 让:ràng 宫:gōng 里:li 的:de 女人:nǚrén 当:dāng 兵:bīng 吗:ma ？ ”', 'Le roi demanda à Sunzi : « Peux-tu faire des soldats avec les femmes du palais ? »', 'The king asked Sunzi: “Can you turn the women of the palace into soldiers?”'),
     S('孙子:Sūnzǐ 回答:huídá ： “ 可以:kěyǐ 。 ”', 'Sunzi répondit : « Oui. »', 'Sunzi answered: “I can.”'),
     S('吴王:Wú_wáng 就:jiù 叫:jiào 来:lái 了:le 一百八十:yìbǎi_bāshí 个:ge 女人:nǚrén 。', 'Le roi fit aussitôt venir cent quatre-vingts femmes.', 'The king immediately summoned a hundred and eighty women.')],
  ], [
    W('本', 'běn', 'classificateur des livres', 'measure word for books'),
    W('兵', 'bīng', 'soldat', 'soldier'),
    W('带', 'dài', 'mener, emmener', 'to lead, to bring'),
    W('宫', 'gōng', 'palais', 'palace'),
    W('当', 'dāng', 'servir de, devenir', 'to serve as, to become'),
    W('吴王', 'Wú wáng', 'le roi de Wu', 'the king of Wu'),
  ], [
    Q(('Qu’a écrit Sunzi ?', 'What did Sunzi write?'), [('Un livre sur la guerre', 'A book about war'), ('Une lettre au roi', 'A letter to the king'), ('Un poème', 'A poem')], 0),
    Q(('Combien de femmes le roi fait-il venir ?', 'How many women does the king summon?'), [('Dix-huit', 'Eighteen'), ('Cent quatre-vingts', 'A hundred and eighty'), ('Cent', 'A hundred')], 1),
  ]),
  CH('sunzi-lian-bing-2', ('她们笑了', 'Elles rient', 'They laugh'), [
    [S('孙子:Sūnzǐ 让:ràng 她们:tāmen 站:zhàn 成:chéng 两:liǎng 队:duì ， 王:wáng 最:zuì 喜欢:xǐhuan 的:de 两个:liǎng_ge 女人:nǚrén 当:dāng 队长:duìzhǎng 。', 'Sunzi les mit en deux rangs, avec pour cheffes les deux favorites du roi.', 'Sunzi lined them up in two ranks, with the king’s two favourites as leaders.'),
     S('他:tā 问:wèn ： “ 你们:nǐmen 知道:zhīdào 左边:zuǒbian 、 右边:yòubian 、 前面:qiánmiàn 、 后面:hòumiàn 吗:ma ？ ”', 'Il demanda : « Savez-vous où sont la gauche, la droite, l’avant et l’arrière ? »', 'He asked: “Do you know left, right, front and back?”'),
     S('女人们:nǚrénmen 说:shuō ： “ 知道:zhīdào ！ ”', 'Les femmes répondirent : « Oui ! »', 'The women said: “We do!”')],
    [S('孙子:Sūnzǐ 打:dǎ 鼓:gǔ ， 说:shuō ： “ 往:wǎng 右:yòu ！ ”', 'Sunzi frappa le tambour et cria : « À droite ! »', 'Sunzi beat the drum and called: “Right!”'),
     S('可是:kěshì 女人们:nǚrénmen 都:dōu 笑:xiào 了:le ， 没有:méiyǒu 人:rén 动:dòng 。', 'Mais toutes les femmes éclatèrent de rire, et personne ne bougea.', 'But all the women laughed, and nobody moved.'),
     S('孙子:Sūnzǐ 说:shuō ： “ 我:wǒ 没:méi 说:shuō 清楚:qīngchu ， 是:shì 我的:wǒ_de 错:cuò 。 ” 他:tā 又:yòu 说:shuō 了:le 一次:yí_cì 。', 'Sunzi dit : « Je n’ai pas été clair, c’est ma faute. » Et il répéta les ordres.', 'Sunzi said: “I wasn’t clear; it’s my fault.” And he explained once more.')],
  ], [
    W('站', 'zhàn', 'se tenir debout', 'to stand'),
    W('队', 'duì', 'rang, file', 'rank, line'),
    W('队长', 'duìzhǎng', 'chef de file', 'team leader'),
    W('鼓', 'gǔ', 'tambour', 'drum'),
    W('动', 'dòng', 'bouger', 'to move'),
    W('清楚', 'qīngchu', 'clair', 'clear'),
  ], [
    Q(('Que font les femmes au premier ordre ?', 'What do the women do at the first order?'), [('Elles tournent à droite', 'They turn right'), ('Elles rient sans bouger', 'They laugh and don’t move'), ('Elles s’en vont', 'They leave')], 1),
    Q(('À qui Sunzi attribue-t-il la première erreur ?', 'Whom does Sunzi blame for the first mistake?'), [('À lui-même', 'Himself'), ('Aux femmes', 'The women'), ('Au roi', 'The king')], 0),
  ]),
  CH('sunzi-lian-bing-3', ('军令如山', 'Un ordre est un ordre', 'An order is an order'), [
    [S('孙子:Sūnzǐ 再:zài 打:dǎ 鼓:gǔ ： “ 往:wǎng 左:zuǒ ！ ”', 'Sunzi frappa de nouveau le tambour : « À gauche ! »', 'Sunzi beat the drum again: “Left!”'),
     S('女人们:nǚrénmen 还是:háishi 笑:xiào 。', 'Les femmes riaient toujours.', 'The women were still laughing.'),
     S('孙子:Sūnzǐ 说:shuō ： “ 我:wǒ 已经:yǐjīng 说:shuō 清楚:qīngchu 了:le ， 你们:nǐmen 不:bù 听:tīng ， 是:shì 队长:duìzhǎng 的:de 错:cuò 。 ”', 'Sunzi dit : « J’ai été clair cette fois. Si vous n’obéissez pas, c’est la faute des cheffes. »', 'Sunzi said: “This time I was clear. If you don’t obey, it’s the leaders’ fault.”')],
    [S('吴王:Wú_wáng 很:hěn 着急:zháojí ， 可是:kěshì 孙子:Sūnzǐ 没有:méiyǒu 听:tīng 他:tā 的:de 。', 'Le roi s’inquiéta, mais Sunzi ne l’écouta pas.', 'The king grew anxious, but Sunzi didn’t listen to him.'),
     S('他:tā 让:ràng 别的:biéde 女人:nǚrén 当:dāng 队长:duìzhǎng ， 又:yòu 打:dǎ 鼓:gǔ 。', 'Il nomma d’autres cheffes et frappa encore le tambour.', 'He appointed other leaders and beat the drum once more.'),
     S('这次:zhè_cì ， 没有:méiyǒu 人:rén 笑:xiào 了:le ， 大家:dàjiā 走:zǒu 得:de 非常:fēicháng 好:hǎo 。', 'Cette fois, personne ne rit : toutes marchèrent parfaitement.', 'This time nobody laughed: they all marched perfectly.'),
     S('吴王:Wú_wáng 知道:zhīdào 了:le ： 孙子:Sūnzǐ 真:zhēn 会:huì 带:dài 兵:bīng 。', 'Le roi comprit alors que Sunzi savait vraiment commander.', 'The king understood that Sunzi really knew how to lead troops.')],
  ], [
    W('还是', 'háishi', 'toujours, encore', 'still'),
    W('着急', 'zháojí', 'inquiet, pressé', 'anxious'),
    W('别的', 'biéde', 'autre', 'other'),
    W('这次', 'zhè cì', 'cette fois', 'this time'),
    W('非常', 'fēicháng', 'extrêmement', 'extremely'),
    W('军令如山', 'jūn lìng rú shān', 'un ordre militaire est inébranlable', 'a military order is unshakeable'),
  ], [
    Q(('Que fait Sunzi des deux cheffes de file ?', 'What does Sunzi do with the two leaders?'), [('Il les remplace par d’autres', 'He replaces them with others'), ('Il les félicite', 'He congratulates them'), ('Il leur donne du vin', 'He gives them wine')], 0),
    Q(('Que comprend le roi à la fin ?', 'What does the king understand in the end?'), [('Que Sunzi sait commander', 'That Sunzi knows how to command'), ('Que les femmes ne savent pas marcher', 'That the women can’t march'), ('Que le livre est mauvais', 'That the book is bad')], 0),
  ]),
])

# 狐假虎威 (Stratagèmes des Royaumes combattants, royaume de Chu)
HUJIA = STORY('hu-jia-hu-wei', '狐', 'HSK2', '#E8772E', ('狐假虎威', 'Le renard et le tigre', 'The fox and the tiger'),
  ('Un renard capturé par un tigre prétend être le roi des animaux… et le prouve.', 'A fox caught by a tiger claims to be king of the animals… and proves it.'), [
  CH('hu-jia-hu-wei-1', ('老虎抓到了狐狸', 'Le tigre attrape le renard', 'The tiger catches the fox'), [
    [S('从前:cóngqián ， 山:shān 里:li 有:yǒu 一只:yì_zhī 老虎:lǎohǔ 。', 'Autrefois, dans la montagne, vivait un tigre.', 'Long ago, a tiger lived in the mountains.'),
     S('一天:yì_tiān ， 老虎:lǎohǔ 饿:è 了:le ， 它:tā 出去:chūqu 找:zhǎo 东西:dōngxi 吃:chī 。', 'Un jour, le tigre eut faim et sortit chercher à manger.', 'One day the tiger was hungry and went out to find food.'),
     S('它:tā 抓:zhuā 到:dào 了:le 一只:yì_zhī 狐狸:húli 。', 'Il attrapa un renard.', 'It caught a fox.')],
    [S('狐狸:húli 说:shuō ： “ 你:nǐ 不:bù 能:néng 吃:chī 我:wǒ ！ 天帝:Tiāndì 让:ràng 我:wǒ 当:dāng 所有:suǒyǒu 动物:dòngwù 的:de 王:wáng 。 ”', 'Le renard dit : « Tu ne peux pas me manger ! L’Empereur du Ciel m’a fait roi de tous les animaux. »', 'The fox said: “You can’t eat me! The Emperor of Heaven made me king of all the animals.”'),
     S('“ 你:nǐ 不:bù 相信:xiāngxìn ？ 你:nǐ 跟:gēn 我:wǒ 走:zǒu ， 看看:kànkan 动物们:dòngwùmen 怕:pà 不:bù 怕:pà 我:wǒ 。 ”', '« Tu ne me crois pas ? Suis-moi et regarde si les animaux ont peur de moi. »', '“You don’t believe me? Follow me and see whether the animals are afraid of me.”')],
  ], [
    W('老虎', 'lǎohǔ', 'tigre', 'tiger'),
    W('饿', 'è', 'avoir faim', 'hungry'),
    W('抓', 'zhuā', 'attraper', 'to catch'),
    W('狐狸', 'húli', 'renard', 'fox'),
    W('动物', 'dòngwù', 'animal', 'animal'),
    W('怕', 'pà', 'avoir peur', 'to be afraid'),
    W('相信', 'xiāngxìn', 'croire', 'to believe'),
  ], [
    Q(('Pourquoi le tigre sort-il ?', 'Why does the tiger go out?'), [('Il a faim', 'It is hungry'), ('Il est malade', 'It is ill'), ('Il cherche un ami', 'It is looking for a friend')], 0),
    Q(('Que prétend le renard ?', 'What does the fox claim?'), [('Qu’il est le roi des animaux', 'That it is king of the animals'), ('Qu’il est malade', 'That it is ill'), ('Qu’il court plus vite', 'That it runs faster')], 0),
  ]),
  CH('hu-jia-hu-wei-2', ('动物们都跑了', 'Tous les animaux s’enfuient', 'All the animals run away'), [
    [S('狐狸:húli 走:zǒu 在:zài 前面:qiánmiàn ， 老虎:lǎohǔ 走:zǒu 在:zài 后面:hòumiàn 。', 'Le renard marchait devant, le tigre derrière.', 'The fox walked in front, the tiger behind.'),
     S('动物们:dòngwùmen 看见:kànjiàn 了:le ， 都:dōu 很快:hěn_kuài 地:de 跑:pǎo 了:le 。', 'En les voyant, tous les animaux s’enfuirent à toute vitesse.', 'When the animals saw them, they all ran away fast.'),
     S('狐狸:húli 笑:xiào 着:zhe 说:shuō ： “ 你:nǐ 看:kàn ， 它们:tāmen 都:dōu 怕:pà 我:wǒ ！ ”', 'Le renard dit en souriant : « Tu vois, ils ont tous peur de moi ! »', 'The fox said with a smile: “You see, they’re all afraid of me!”')],
    [S('老虎:lǎohǔ 不:bù 知道:zhīdào ， 动物们:dòngwùmen 怕:pà 的:de 是:shì 它:tā ， 不是:bú_shì 狐狸:húli 。', 'Le tigre ne savait pas que c’était lui que les animaux craignaient, pas le renard.', 'The tiger didn’t know that the animals were afraid of it, not of the fox.'),
     S('它:tā 就:jiù 让:ràng 狐狸:húli 走:zǒu 了:le 。', 'Il laissa donc partir le renard.', 'So it let the fox go.'),
     S('这:zhè 就是:jiù_shì “ 狐假虎威:hú_jiǎ_hǔ_wēi ” 。', 'Voilà ce qu’on appelle « le renard qui emprunte la majesté du tigre ».', 'This is what is called “the fox borrowing the tiger’s might”.')],
  ], [
    W('前面', 'qiánmiàn', 'devant', 'in front'),
    W('看见', 'kànjiàn', 'voir', 'to see'),
    W('地', 'de', 'particule adverbiale', 'adverbial particle'),
    W('它们', 'tāmen', 'ils, elles (animaux, choses)', 'they (animals, things)'),
    W('威', 'wēi', 'majesté, prestige', 'might, prestige'),
    W('狐假虎威', 'hú jiǎ hǔ wēi', 'se prévaloir de la puissance d’un autre', 'to use someone else’s power to intimidate'),
  ], [
    Q(('Qui marche devant ?', 'Who walks in front?'), [('Le renard', 'The fox'), ('Le tigre', 'The tiger'), ('Les autres animaux', 'The other animals')], 0),
    Q(('De qui les animaux ont-ils vraiment peur ?', 'Who are the animals really afraid of?'), [('Du renard', 'The fox'), ('Du tigre', 'The tiger'), ('Des chasseurs', 'The hunters')], 1),
  ]),
])

# 塞翁失马 (Huainanzi)
SAIWENG = STORY('sai-weng-shi-ma', '马', 'HSK2', '#7A5A3A', ('塞翁失马', 'Le vieil homme de la frontière', 'The old man of the frontier'),
  ('Le cheval d’un vieil homme s’enfuit. Malheur ou chance ? Lui seul ne se presse pas de juger.', 'An old man’s horse runs away. Misfortune or luck? He alone is in no hurry to judge.'), [
  CH('sai-weng-shi-ma-1', ('马跑了', 'Le cheval s’enfuit', 'The horse runs away'), [
    [S('从前:cóngqián ， 有:yǒu 一个:yí_ge 老人:lǎorén 住:zhù 在:zài 边境:biānjìng 。', 'Autrefois, un vieil homme vivait à la frontière.', 'Long ago, an old man lived on the frontier.'),
     S('一天:yì_tiān ， 他的:tā_de 马:mǎ 跑:pǎo 了:le 。', 'Un jour, son cheval s’enfuit.', 'One day his horse ran away.'),
     S('朋友们:péngyoumen 都:dōu 说:shuō ： “ 真:zhēn 可惜:kěxī ！ ”', 'Ses amis lui dirent tous : « Quel dommage ! »', 'His friends all said: “What a pity!”')],
    [S('老人:lǎorén 笑:xiào 着:zhe 说:shuō ： “ 没关系:méi_guānxi ， 这:zhè 可能:kěnéng 是:shì 好:hǎo 事:shì 。 ”', 'Le vieil homme répondit en souriant : « Ce n’est pas grave, c’est peut-être une bonne chose. »', 'The old man smiled and said: “It doesn’t matter; it may be a good thing.”')],
  ], [
    W('老人', 'lǎorén', 'vieil homme, personne âgée', 'old man, elderly person'),
    W('边境', 'biānjìng', 'frontière', 'border, frontier'),
    W('马', 'mǎ', 'cheval', 'horse'),
    W('可惜', 'kěxī', 'dommage', 'what a pity'),
    W('事', 'shì', 'chose, affaire', 'matter, thing'),
    W('可能', 'kěnéng', 'peut-être', 'maybe'),
  ], [
    Q(('Qu’arrive-t-il au cheval ?', 'What happens to the horse?'), [('Il s’enfuit', 'It runs away'), ('Il tombe malade', 'It falls ill'), ('Il est vendu', 'It is sold')], 0),
    Q(('Comment réagit le vieil homme ?', 'How does the old man react?'), [('Il pleure', 'He cries'), ('Il dit que c’est peut-être une bonne chose', 'He says it may be a good thing'), ('Il part le chercher', 'He goes looking for it')], 1),
  ]),
  CH('sai-weng-shi-ma-2', ('马回来了', 'Le cheval revient', 'The horse comes back'), [
    [S('几个:jǐ_ge 月:yuè 以后:yǐhòu ， 他的:tā_de 马:mǎ 回来:huílai 了:le ， 还:hái 带:dài 来:lái 了:le 一:yì 匹:pǐ 好:hǎo 马:mǎ 。', 'Quelques mois plus tard, son cheval revint, et ramena même un autre bon cheval.', 'A few months later his horse came back, bringing another fine horse with it.'),
     S('朋友们:péngyoumen 说:shuō ： “ 太:tài 好:hǎo 了:le ！ ”', 'Ses amis s’écrièrent : « Formidable ! »', 'His friends said: “Wonderful!”'),
     S('老人:lǎorén 说:shuō ： “ 这:zhè 可能:kěnéng 是:shì 坏:huài 事:shì 。 ”', 'Le vieil homme dit : « C’est peut-être une mauvaise chose. »', 'The old man said: “It may be a bad thing.”')],
    [S('老人的:lǎorén_de 儿子:érzi 非常:fēicháng 喜欢:xǐhuan 这:zhè 匹:pǐ 新:xīn 马:mǎ 。', 'Le fils du vieil homme adorait ce nouveau cheval.', 'The old man’s son loved the new horse.'),
     S('他:tā 每天:měi_tiān 骑:qí 马:mǎ 。 有:yǒu 一天:yì_tiān ， 他:tā 从:cóng 马:mǎ 上:shang 掉:diào 下来:xiàlai ， 腿:tuǐ 断:duàn 了:le 。', 'Il le montait tous les jours. Un jour, il tomba et se cassa la jambe.', 'He rode it every day. One day he fell off and broke his leg.')],
  ], [
    W('以后', 'yǐhòu', 'après, plus tard', 'after, later'),
    W('带', 'dài', 'amener, emporter', 'to bring'),
    W('匹', 'pǐ', 'classificateur des chevaux', 'measure word for horses'),
    W('坏', 'huài', 'mauvais', 'bad'),
    W('骑', 'qí', 'monter (à cheval)', 'to ride'),
    W('腿', 'tuǐ', 'jambe', 'leg'),
  ], [
    Q(('Avec quoi le cheval revient-il ?', 'What does the horse come back with?'), [('Avec un autre bon cheval', 'With another fine horse'), ('Avec de l’argent', 'With money'), ('Seul', 'Alone')], 0),
    Q(('Qu’arrive-t-il au fils ?', 'What happens to the son?'), [('Il se casse la jambe', 'He breaks his leg'), ('Il part à la guerre', 'He goes to war'), ('Il vend le cheval', 'He sells the horse')], 0),
  ]),
  CH('sai-weng-shi-ma-3', ('好事还是坏事？', 'Bonne ou mauvaise chose ?', 'Good thing or bad?'), [
    [S('朋友们:péngyoumen 又:yòu 说:shuō ： “ 真:zhēn 可惜:kěxī ！ ”', 'Ses amis dirent encore : « Quel dommage ! »', 'His friends said again: “What a pity!”'),
     S('老人:lǎorén 还是:háishi 说:shuō ： “ 这:zhè 可能:kěnéng 是:shì 好:hǎo 事:shì 。 ”', 'Le vieil homme répéta : « C’est peut-être une bonne chose. »', 'The old man still said: “It may be a good thing.”')],
    [S('第二年:dì-èr_nián ， 打仗:dǎzhàng 了:le ， 年轻人:niánqīngrén 都:dōu 要:yào 去:qù 当:dāng 兵:bīng 。', 'L’année suivante, la guerre éclata : tous les jeunes durent partir comme soldats.', 'The next year war broke out, and all the young men had to become soldiers.'),
     S('老人的:lǎorén_de 儿子:érzi 腿:tuǐ 不:bù 好:hǎo ， 不用:bú_yòng 去:qù ， 他:tā 和:hé 父亲:fùqin 一起:yìqǐ 留:liú 在:zài 了:le 家:jiā 里:li 。', 'Le fils, avec sa jambe blessée, n’eut pas à partir : il resta à la maison avec son père.', 'With his bad leg, the son didn’t have to go: he stayed at home with his father.'),
     S('这:zhè 就是:jiù_shì “ 塞翁失马:sài_wēng_shī_mǎ ， 焉知非福:yān_zhī_fēi_fú ” 。', 'Voilà le proverbe : « Le vieil homme de la frontière perd son cheval : qui sait si ce n’est pas une chance ? »', 'Hence the saying: “The old man of the frontier lost his horse: who knows if it wasn’t a blessing?”')],
  ], [
    W('第二年', 'dì-èr nián', 'l’année suivante', 'the next year'),
    W('打仗', 'dǎzhàng', 'faire la guerre', 'to go to war'),
    W('年轻人', 'niánqīngrén', 'les jeunes', 'young people'),
    W('不用', 'bú yòng', 'ne pas avoir besoin de', 'no need to'),
    W('留', 'liú', 'rester', 'to stay'),
    W('父亲', 'fùqin', 'père', 'father'),
  ], [
    Q(('Pourquoi le fils ne part-il pas à la guerre ?', 'Why doesn’t the son go to war?'), [('À cause de sa jambe', 'Because of his leg'), ('Il est trop jeune', 'He is too young'), ('Il est malade', 'He is ill')], 0),
    Q(('Que veut dire cette histoire ?', 'What does this story mean?'), [('Un malheur peut cacher une chance', 'Misfortune can hide good luck'), ('Il faut toujours garder ses chevaux', 'You should always keep your horses'), ('La guerre est toujours une bonne chose', 'War is always a good thing')], 0),
  ]),
])

# ═════════════════════════ HSK 3 : moins de pinyin ═════════════════════════
# À partir du HSK 3, seuls les mots qui dépassent le HSK 2 (et les noms propres) gardent leur pinyin : les mots
# écrits sans pinyin doivent n'utiliser que des caractères déjà vus dans les mots du HSK 1 et du HSK 2.
def _known_chars(upto):
    chars = set('，。！？：“”《》、；')
    for n in range(1, upto):
        lv = json.load(open(os.path.join(ROOT, f'content/hsk{n}/hsk{n}.json'), encoding='utf-8'))
        for w in lv['worlds']:
            for c in w['chapters']:
                for l in c['lessons']:
                    for it in l['items']:
                        if it['kind'] == 'vocabulary':
                            chars.update(it['front'])
    return chars
MISSING = []
BASE_CHARS = set('了的着过得地也都和就还很在是不没一个们里两晚吧用')
KNOWN_CHARS = _known_chars(3) | BASE_CHARS

def S3(seg, fr, en, known=None):
    known = known or KNOWN_CHARS
    for zh, py in tokens(seg):
        if py is None:
            unknown = [c for c in zh if c not in known]
            if unknown:
                MISSING.append(f'pinyin manquant pour {zh} ({"".join(unknown)}) dans : {seg}')
    return S(seg, fr, en)

# 孟母三迁 (Biographies des femmes exemplaires, Liu Xiang) — Mencius, maître de Qi et de l'académie Jixia
MENGMU = STORY('meng-mu-san-qian', '迁', 'HSK3', '#5E6E3A', ('孟母三迁', 'Les trois déménagements de la mère de Mencius', 'Mencius’s mother moves three times'),
  ('Pour que son fils grandisse au bon endroit, la mère de Mencius n’hésite pas à déménager encore et encore.', 'So that her son grows up in the right place, Mencius’s mother doesn’t hesitate to move again and again.'), [
  CH('meng-mu-san-qian-1', ('住在墓地旁边', 'À côté du cimetière', 'Next to the cemetery'), [
    [S3('孟子:Mèngzǐ 小 的 时候 ， 父亲:fùqin 就 去世:qùshì 了 。', 'Mencius était petit quand son père mourut.', 'Mencius was little when his father died.'),
     S3('他 和 妈妈 住 在 一个 墓地:mùdì 旁边 。', 'Il habitait avec sa mère à côté d’un cimetière.', 'He lived with his mother next to a cemetery.'),
     S3('每天 都 有 人 来 这儿 哭:kū 。', 'Tous les jours, des gens venaient y pleurer.', 'Every day people came there to weep.')],
    [S3('孟子:Mèngzǐ 觉得 很 有意思 ， 就 跟:gēn 别的:biéde 孩子 一起 学 他们 哭:kū 。', 'Mencius trouvait cela amusant et, avec d’autres enfants, il imitait les pleureurs.', 'Mencius found it amusing and, with other children, he imitated the mourners.'),
     S3('孟母:Mèng_mǔ 看见 了 ， 很 担心:dānxīn ： “ 我 的 孩子 不 应该:yīnggāi 住 在 这儿 。 ”', 'Sa mère le vit et s’inquiéta : « Mon enfant ne devrait pas vivre ici. »', 'His mother saw it and worried: “My child shouldn’t live here.”'),
     S3('她 决定:juédìng 搬家:bānjiā 。', 'Elle décida de déménager.', 'She decided to move.')],
  ], [
    W('去世', 'qùshì', 'mourir, décéder', 'to pass away'),
    W('墓地', 'mùdì', 'cimetière', 'cemetery'),
    W('哭', 'kū', 'pleurer', 'to cry'),
    W('担心', 'dānxīn', 's’inquiéter', 'to worry'),
    W('决定', 'juédìng', 'décider', 'to decide'),
    W('搬家', 'bānjiā', 'déménager', 'to move house'),
  ], [
    Q(('Où habitent-ils au début ?', 'Where do they live at first?'), [('À côté d’un cimetière', 'Next to a cemetery'), ('À côté d’un marché', 'Next to a market'), ('À côté d’une école', 'Next to a school')], 0),
    Q(('Que fait le petit Mencius ?', 'What does little Mencius do?'), [('Il imite ceux qui pleurent', 'He imitates the mourners'), ('Il lit des livres', 'He reads books'), ('Il vend des légumes', 'He sells vegetables')], 0),
  ]),
  CH('meng-mu-san-qian-2', ('市场旁边', 'À côté du marché', 'Next to the market'), [
    [S3('他们 搬:bān 到:dào 了 一个 市场:shìchǎng 旁边 。', 'Ils s’installèrent à côté d’un marché.', 'They moved next to a market.'),
     S3('市场:shìchǎng 里 人 很 多 ， 非常 热闹:rènao 。', 'Le marché était plein de monde, très animé.', 'The market was crowded and very lively.'),
     S3('卖 东西 的 人 都 大声:dàshēng 地 说话 。', 'Les marchands parlaient tous à voix haute.', 'The traders all spoke loudly.')],
    [S3('没 过 多久:duō_jiǔ ， 孟子:Mèngzǐ 又:yòu 开始 学 他们 ， 每天 大声:dàshēng 地 卖 东西 。', 'Peu de temps après, Mencius se mit à les imiter, criant chaque jour comme un marchand.', 'Before long Mencius began to imitate them, loudly selling things every day.'),
     S3('孟母:Mèng_mǔ 又:yòu 着急:zháojí 了 ： “ 这儿 也 不 适合:shìhé 我 的 孩子 。 ”', 'Sa mère s’inquiéta de nouveau : « Cet endroit ne convient pas non plus à mon enfant. »', 'His mother grew anxious again: “This place doesn’t suit my child either.”'),
     S3('于是:yúshì ， 他们 又:yòu 搬家:bānjiā 了 。', 'Alors, ils déménagèrent encore.', 'So they moved again.')],
  ], [
    W('市场', 'shìchǎng', 'marché', 'market'),
    W('热闹', 'rènao', 'animé', 'lively'),
    W('大声', 'dàshēng', 'à voix haute', 'loudly'),
    W('适合', 'shìhé', 'convenir à', 'to suit'),
    W('于是', 'yúshì', 'alors, c’est pourquoi', 'so, thereupon'),
    W('着急', 'zháojí', 'inquiet, pressé', 'anxious'),
  ], [
    Q(('Qu’imite Mencius au marché ?', 'What does Mencius imitate at the market?'), [('Les marchands', 'The traders'), ('Les maîtres', 'The teachers'), ('Les soldats', 'The soldiers')], 0),
    Q(('Que fait sa mère ensuite ?', 'What does his mother do next?'), [('Elle déménage encore', 'She moves again'), ('Elle ouvre une boutique', 'She opens a shop'), ('Elle le punit', 'She punishes him')], 0),
  ]),
  CH('meng-mu-san-qian-3', ('学校旁边', 'À côté de l’école', 'Next to the school'), [
    [S3('这 一 次 ， 他们 搬:bān 到:dào 了 一个 学校 旁边 。', 'Cette fois, ils s’installèrent à côté d’une école.', 'This time they moved next to a school.'),
     S3('学校 里 的 老师 每天 给 学生 讲:jiǎng 礼:lǐ ， 学生 们 认真:rènzhēn 地 读书 。', 'Chaque jour, le maître y enseignait les rites et les élèves étudiaient avec sérieux.', 'Every day the teacher taught the rites and the pupils studied conscientiously.'),
     S3('孟子:Mèngzǐ 也 跟:gēn 着 他们 学习 ， 变得:biàn_de 很 有 礼貌:lǐmào 。', 'Mencius étudia avec eux et devint très poli.', 'Mencius studied with them and became very polite.')],
    [S3('孟母:Mèng_mǔ 终于:zhōngyú 放心:fàngxīn 了 ： “ 这儿 才:cái 是 我 的 孩子 应该:yīnggāi 住 的 地方:dìfang 。 ”', 'Sa mère fut enfin rassurée : « Voilà l’endroit où mon enfant doit vivre. »', 'His mother was finally at ease: “This is where my child should live.”'),
     S3('后来:hòulái ， 孟子:Mèngzǐ 成为:chéngwéi 了 一个 有名:yǒumíng 的 思想家:sīxiǎngjiā 。', 'Plus tard, Mencius devint un penseur célèbre.', 'Later Mencius became a famous thinker.'),
     S3('这 就是 “ 孟母三迁:Mèng_mǔ_sān_qiān ” 的 故事:gùshi 。', 'C’est l’histoire des « trois déménagements de la mère de Mencius ».', 'This is the story of “Mencius’s mother moving three times”.')],
  ], [
    W('礼', 'lǐ', 'les rites', 'the rites'),
    W('礼貌', 'lǐmào', 'politesse ; poli', 'politeness; polite'),
    W('放心', 'fàngxīn', 'être rassuré', 'to be at ease'),
    W('成为', 'chéngwéi', 'devenir', 'to become'),
    W('思想家', 'sīxiǎngjiā', 'penseur', 'thinker'),
    W('终于', 'zhōngyú', 'enfin', 'at last'),
  ], [
    Q(('Que fait-on à l’école voisine ?', 'What happens at the nearby school?'), [('On y étudie les rites', 'People study the rites'), ('On y vend des livres', 'People sell books'), ('On y pleure', 'People weep')], 0),
    Q(('Que devient Mencius ?', 'What does Mencius become?'), [('Un penseur célèbre', 'A famous thinker'), ('Un riche marchand', 'A rich merchant'), ('Un général', 'A general')], 0),
  ]),
])

# 揠苗助长 (Mencius, Gongsun Chou I)
YAMIAO = STORY('ya-miao-zhu-zhang', '苗', 'HSK3', '#6E9A3A', ('揠苗助长', 'Le paysan qui tirait sur ses pousses', 'The farmer who pulled his shoots'),
  ('Un paysan pressé veut aider son riz à pousser plus vite… à sa manière.', 'An impatient farmer wants to help his rice grow faster… in his own way.'), [
  CH('ya-miao-zhu-zhang-1', ('着急的农民', 'Le paysan impatient', 'The impatient farmer'), [
    [S3('宋国:Sòng_guó 有 一个 农民:nóngmín ， 他 种:zhòng 了 很 多 禾苗:hémiáo 。', 'Au pays de Song, un paysan avait planté beaucoup de jeunes pousses.', 'In the state of Song, a farmer had planted many young shoots.'),
     S3('他 每天 都 去 田:tián 里 看 ， 希望 禾苗:hémiáo 快 一点儿 长:zhǎng 高 。', 'Il allait chaque jour au champ, espérant qu’elles pousseraient plus vite.', 'Every day he went to the field, hoping they would grow faster.'),
     S3('可是:kěshì 禾苗:hémiáo 长:zhǎng 得 太 慢 了 ， 他 越:yuè 看 越:yuè 着急:zháojí 。', 'Mais elles poussaient trop lentement, et plus il les regardait, plus il s’impatientait.', 'But they grew too slowly, and the more he looked, the more impatient he became.')],
    [S3('一 天 ， 他 突然:tūrán 想 到 了 一个 办法:bànfǎ 。', 'Un jour, une idée lui vint soudain.', 'One day an idea suddenly came to him.'),
     S3('他 走 进 田:tián 里 ， 把:bǎ 每 一 棵:kē 禾苗:hémiáo 都 往 上 拔:bá 了 一点儿 。', 'Il entra dans le champ et tira chaque pousse un peu vers le haut.', 'He went into the field and pulled every shoot up a little.'),
     S3('他 从 早上 一直:yìzhí 拔:bá 到 晚上 ， 累 极了:jí_le 。', 'Il tira du matin au soir et fut épuisé.', 'He pulled from morning till night and was exhausted.')],
  ], [
    W('农民', 'nóngmín', 'paysan', 'farmer'),
    W('种', 'zhòng', 'planter', 'to plant'),
    W('禾苗', 'hémiáo', 'jeune pousse (de céréale)', 'young shoot (of grain)'),
    W('田', 'tián', 'champ', 'field'),
    W('长', 'zhǎng', 'pousser, grandir', 'to grow'),
    W('拔', 'bá', 'tirer, arracher', 'to pull up'),
  ], [
    Q(('Pourquoi le paysan s’impatiente-t-il ?', 'Why does the farmer grow impatient?'), [('Les pousses grandissent trop lentement', 'The shoots grow too slowly'), ('Il pleut trop', 'It rains too much'), ('Les oiseaux mangent tout', 'Birds eat everything')], 0),
    Q(('Que fait-il dans le champ ?', 'What does he do in the field?'), [('Il tire les pousses vers le haut', 'He pulls the shoots upwards'), ('Il arrose', 'He waters them'), ('Il plante encore', 'He plants more')], 0),
  ]),
  CH('ya-miao-zhu-zhang-2', ('禾苗都死了', 'Toutes les pousses meurent', 'All the shoots die'), [
    [S3('回 到 家 ， 他 高兴 地 对 家 里 人 说 ： “ 今天 我 累 坏:huài 了 ！ 我 帮助 禾苗:hémiáo 长:zhǎng 高 了 。 ”', 'Rentré chez lui, il dit tout joyeux à sa famille : « Je suis mort de fatigue ! J’ai aidé les pousses à grandir. »', 'Back home, he happily told his family: “I’m worn out! I helped the shoots grow.”'),
     S3('他 的 儿子 觉得 很 奇怪:qíguài ， 马上:mǎshàng 跑 到 田:tián 里 去 看 。', 'Son fils, intrigué, courut aussitôt au champ.', 'His son, puzzled, ran straight to the field.'),
     S3('他 发现:fāxiàn 禾苗:hémiáo 都 已经 死:sǐ 了 。', 'Il découvrit que toutes les pousses étaient mortes.', 'He found that all the shoots had died.')],
    [S3('孟子:Mèngzǐ 用:yòng 这个 故事:gùshi 告诉 我们 ： 做 事情 不 能 太 着急:zháojí 。', 'Mencius se sert de cette histoire pour nous dire qu’il ne faut pas trop se presser.', 'Mencius uses this story to tell us not to be in too much of a hurry.'),
     S3('如果:rúguǒ 想 快 一点儿 ， 反而:fǎn’ér 会 把:bǎ 事情 做 坏:huài 。', 'À vouloir aller trop vite, on gâche tout au contraire.', 'If you try to go faster, you end up spoiling things.'),
     S3('这 就是 “ 揠苗助长:yà_miáo_zhù_zhǎng ” 。', 'C’est ce qu’on appelle « tirer sur les pousses pour les aider à grandir ».', 'This is “pulling up shoots to help them grow”.')],
  ], [
    W('坏', 'huài', 'abîmé ; terriblement', 'broken; terribly'),
    W('奇怪', 'qíguài', 'étrange', 'strange'),
    W('马上', 'mǎshàng', 'tout de suite', 'right away'),
    W('死', 'sǐ', 'mourir', 'to die'),
    W('反而', 'fǎn’ér', 'au contraire', 'on the contrary'),
    W('揠苗助长', 'yà miáo zhù zhǎng', 'vouloir hâter les choses et tout gâcher', 'to spoil things by being too hasty'),
  ], [
    Q(('Que découvre le fils ?', 'What does the son discover?'), [('Les pousses sont mortes', 'The shoots are dead'), ('Les pousses ont grandi', 'The shoots have grown'), ('Le champ a été volé', 'The field was stolen')], 0),
    Q(('Quelle est la leçon de Mencius ?', 'What is Mencius’s lesson?'), [('Il ne faut pas trop se presser', 'Don’t be in too much of a hurry'), ('Il faut travailler la nuit', 'Work at night'), ('Il faut planter plus', 'Plant more')], 0),
  ]),
])

# 庄周梦蝶 (Zhuangzi, De l'égalité des choses)
ZHUANGZI = STORY('zhuang-zhou-meng-die', '蝶', 'HSK3', '#7B5BD6', ('庄周梦蝶', 'Zhuangzi rêve qu’il est un papillon', 'Zhuangzi dreams he is a butterfly'),
  ('Zhuangzi s’endort et devient papillon. À son réveil, une question le trouble : qui rêve de qui ?', 'Zhuangzi falls asleep and becomes a butterfly. When he wakes up, a question troubles him: who is dreaming of whom?'), [
  CH('zhuang-zhou-meng-die-1', ('一个梦', 'Un rêve', 'A dream'), [
    [S3('庄子:Zhuāngzǐ 是 战国:Zhànguó 时候 一个 很 有名:yǒumíng 的 思想家:sīxiǎngjiā 。', 'Zhuangzi était un penseur célèbre de l’époque des Royaumes combattants.', 'Zhuangzi was a famous thinker of the Warring States period.'),
     S3('一 天 下午 ， 他 在 树:shù 下面 睡着:shuìzháo 了 ， 做 了 一个 梦:mèng 。', 'Un après-midi, il s’endormit sous un arbre et fit un rêve.', 'One afternoon he fell asleep under a tree and had a dream.'),
     S3('在 梦:mèng 里 ， 他 变成:biànchéng 了 一 只:zhī 蝴蝶:húdié 。', 'En rêve, il se changea en papillon.', 'In the dream he turned into a butterfly.')],
    [S3('蝴蝶:húdié 在 花:huā 和 草:cǎo 中间:zhōngjiān 飞:fēi 来 飞:fēi 去 ， 快乐 极了:jí_le 。', 'Le papillon voletait parmi les fleurs et les herbes, merveilleusement heureux.', 'The butterfly flitted among the flowers and grass, blissfully happy.'),
     S3('它 一点儿 也 不 记得:jìde 自己:zìjǐ 是 庄子:Zhuāngzǐ 。', 'Il ne se souvenait pas du tout d’être Zhuangzi.', 'It didn’t remember at all that it was Zhuangzi.'),
     S3('太阳:tàiyáng 很 暖和:nuǎnhuo ， 风:fēng 也 很 舒服:shūfu 。', 'Le soleil était doux, le vent agréable.', 'The sun was warm and the breeze pleasant.')],
  ], [
    W('战国', 'Zhànguó', 'les Royaumes combattants', 'the Warring States'),
    W('睡着', 'shuìzháo', 's’endormir', 'to fall asleep'),
    W('梦', 'mèng', 'rêve', 'dream'),
    W('变成', 'biànchéng', 'devenir, se changer en', 'to turn into'),
    W('蝴蝶', 'húdié', 'papillon', 'butterfly'),
    W('暖和', 'nuǎnhuo', 'doux, tiède', 'warm'),
  ], [
    Q(('Où Zhuangzi s’endort-il ?', 'Where does Zhuangzi fall asleep?'), [('Sous un arbre', 'Under a tree'), ('Dans un bateau', 'In a boat'), ('À l’école', 'At school')], 0),
    Q(('En quoi se change-t-il en rêve ?', 'What does he turn into in the dream?'), [('En papillon', 'A butterfly'), ('En oiseau', 'A bird'), ('En poisson', 'A fish')], 0),
  ]),
  CH('zhuang-zhou-meng-die-2', ('我是谁？', 'Qui suis-je ?', 'Who am I?'), [
    [S3('突然:tūrán ， 庄子:Zhuāngzǐ 醒:xǐng 了 。', 'Soudain, Zhuangzi se réveilla.', 'Suddenly Zhuangzi woke up.'),
     S3('他 看 看 自己:zìjǐ 的 手 和 脚:jiǎo ， 发现:fāxiàn 自己:zìjǐ 还是 庄子:Zhuāngzǐ 。', 'Il regarda ses mains et ses pieds : il était toujours Zhuangzi.', 'He looked at his hands and feet: he was still Zhuangzi.'),
     S3('可是 他 不 明白:míngbai 了 ： 是 庄子:Zhuāngzǐ 在 梦:mèng 里 变成:biànchéng 了 蝴蝶:húdié ， 还是 蝴蝶:húdié 在 梦:mèng 里 变成:biànchéng 了 庄子:Zhuāngzǐ ？', 'Mais il ne comprenait plus : était-ce Zhuangzi qui avait rêvé d’être un papillon, ou un papillon qui rêvait d’être Zhuangzi ?', 'But now he didn’t understand: had Zhuangzi dreamt he was a butterfly, or was a butterfly dreaming it was Zhuangzi?')],
    [S3('这个 问题 很 简单:jiǎndān ， 也 很 难:nán 。', 'La question est simple, et pourtant très difficile.', 'The question is simple, and also very hard.'),
     S3('庄子:Zhuāngzǐ 认为:rènwéi ， 世界:shìjiè 上 的 东西 一直:yìzhí 在 变化:biànhuà ， 人 和 蝴蝶:húdié 也 没有 那么 不 一样:yíyàng 。', 'Pour Zhuangzi, tout dans le monde change sans cesse, et l’homme n’est pas si différent du papillon.', 'Zhuangzi held that everything in the world keeps changing, and people are not so different from butterflies.'),
     S3('两千:liǎngqiān 多 年 以后:yǐhòu ， 人们:rénmen 还 在 讲:jiǎng 这个 故事:gùshi 。', 'Plus de deux mille ans plus tard, on raconte encore cette histoire.', 'More than two thousand years later, people still tell this story.')],
  ], [
    W('醒', 'xǐng', 'se réveiller', 'to wake up'),
    W('明白', 'míngbai', 'comprendre', 'to understand'),
    W('认为', 'rènwéi', 'estimer, considérer', 'to consider'),
    W('变化', 'biànhuà', 'changer ; changement', 'to change; change'),
    W('一样', 'yíyàng', 'pareil', 'the same'),
    W('人们', 'rénmen', 'les gens', 'people'),
  ], [
    Q(('Que se demande Zhuangzi à son réveil ?', 'What does Zhuangzi wonder when he wakes?'), [('S’il est un homme ou un papillon', 'Whether he is a man or a butterfly'), ('Quelle heure il est', 'What time it is'), ('Où est sa maison', 'Where his house is')], 0),
    Q(('Selon Zhuangzi, le monde…', 'According to Zhuangzi, the world…'), [('change sans cesse', 'keeps changing'), ('ne change jamais', 'never changes'), ('est un mauvais rêve', 'is a bad dream')], 0),
  ]),
])

# HSK 4 : seuls les mots qui dépassent le HSK 3 (et les noms propres) gardent leur pinyin.
KNOWN_CHARS4 = _known_chars(4) | BASE_CHARS
def S4(seg, fr, en):
    return S3(seg, fr, en, KNOWN_CHARS4)

# 一字千金 (Mémoires historiques, Sima Qian) — Lü Buwei, chancelier de Qin
YIZI = STORY('yi-zi-qian-jin', '金', 'HSK4', '#B8962A', ('一字千金', 'Un caractère vaut mille pièces d’or', 'One character worth a thousand gold'),
  ('Le chancelier Lü Buwei promet une fortune à qui saura corriger un seul caractère de son livre.', 'Chancellor Lü Buwei promises a fortune to anyone who can correct a single character in his book.'), [
  CH('yi-zi-qian-jin-1', ('吕不韦的书', 'Le livre de Lü Buwei', 'Lü Buwei’s book'), [
    [S4('秦国:Qín_guó 有 一个 丞相:chéngxiàng ， 叫 吕不韦:Lǚ_Bùwéi 。', 'Le royaume de Qin avait un chancelier nommé Lü Buwei.', 'The state of Qin had a chancellor called Lü Buwei.'),
     S4('他 请 了 三千 个 有 学问:xuéwen 的 人 ， 一起 写 一 本 书 。', 'Il réunit trois mille savants pour écrire ensemble un livre.', 'He gathered three thousand learned men to write a book together.'),
     S4('这 本 书 写 了 天文:tiānwén 、 地理:dìlǐ 、 历史 ， 内容:nèiróng 非常 丰富:fēngfù 。', 'Le livre traitait d’astronomie, de géographie et d’histoire : son contenu était d’une grande richesse.', 'The book covered astronomy, geography and history: its content was extremely rich.')],
    [S4('书 写 完 以后 ， 吕不韦:Lǚ_Bùwéi 觉得 自己 的 书 是 世界 上 最 好 的 。', 'Une fois le livre achevé, Lü Buwei le jugea le meilleur du monde.', 'When the book was finished, Lü Buwei thought it was the best in the world.'),
     S4('于是:yúshì ， 他 想 出 了 一个 办法 ， 让 所有:suǒyǒu 的 人 都 知道 这 本 书 。', 'Alors il eut une idée pour que tout le monde connaisse ce livre.', 'So he came up with a plan to make everyone know about the book.')],
  ], [
    W('丞相', 'chéngxiàng', 'chancelier', 'chancellor'),
    W('学问', 'xuéwen', 'savoir, érudition', 'learning, scholarship'),
    W('天文', 'tiānwén', 'astronomie', 'astronomy'),
    W('地理', 'dìlǐ', 'géographie', 'geography'),
    W('内容', 'nèiróng', 'contenu', 'content'),
    W('丰富', 'fēngfù', 'riche, abondant', 'rich, abundant'),
  ], [
    Q(('Combien de savants écrivent le livre ?', 'How many scholars write the book?'), [('Trois mille', 'Three thousand'), ('Trois cents', 'Three hundred'), ('Trente', 'Thirty')], 0),
    Q(('Que pense Lü Buwei de son livre ?', 'What does Lü Buwei think of his book?'), [('Que c’est le meilleur du monde', 'That it is the best in the world'), ('Qu’il est trop long', 'That it is too long'), ('Qu’il faut le brûler', 'That it should be burnt')], 0),
  ]),
  CH('yi-zi-qian-jin-2', ('一个字一千金', 'Mille pièces d’or par caractère', 'A thousand gold per character'), [
    [S4('他 把 书 挂:guà 在 咸阳:Xiányáng 的 城门:chéngmén 上 。', 'Il fit suspendre le livre à la porte de Xianyang.', 'He had the book hung on the gate of Xianyang.'),
     S4('旁边 还 放 了 一千 两:liǎng 黄金:huángjīn 。', 'À côté, il fit déposer mille onces d’or.', 'Beside it he placed a thousand taels of gold.'),
     S4('他 说 ： “ 谁 能 在 书 里 改:gǎi 一个 字 ， 这些 黄金:huángjīn 就 给 谁 。 ”', 'Il déclara : « Celui qui pourra changer un seul caractère de ce livre recevra tout cet or. »', 'He announced: “Whoever can change a single character in this book will receive all this gold.”')],
    [S4('很 多 人 来 看 ， 可是 一个 人 也 没有 改:gǎi 。', 'Beaucoup vinrent voir, mais personne ne changea rien.', 'Many came to look, but nobody changed anything.'),
     S4('有 人 说 ， 这 是 因为 书 写 得 太 好 了 ； 也 有 人 说 ， 是 因为 大家 都 害怕 吕不韦:Lǚ_Bùwéi 。', 'Certains disent que le livre était trop bien écrit ; d’autres, que tout le monde avait peur de Lü Buwei.', 'Some say the book was too well written; others say everyone was afraid of Lü Buwei.'),
     S4('后来 ， 人们 用 “ 一字千金:yí_zì_qiān_jīn ” 来 说 文章:wénzhāng 写 得 非常 好 。', 'Depuis, on dit « un caractère vaut mille pièces d’or » d’un texte remarquablement écrit.', 'Since then, people say “one character is worth a thousand gold” of a superbly written text.')],
  ], [
    W('挂', 'guà', 'accrocher, suspendre', 'to hang'),
    W('城门', 'chéngmén', 'porte de la ville', 'city gate'),
    W('黄金', 'huángjīn', 'or (métal)', 'gold'),
    W('改', 'gǎi', 'modifier, corriger', 'to change, to correct'),
    W('文章', 'wénzhāng', 'texte, article', 'essay, article'),
    W('一字千金', 'yí zì qiān jīn', 'un texte d’une grande valeur', 'writing of great value'),
  ], [
    Q(('Que promet Lü Buwei ?', 'What does Lü Buwei promise?'), [('De l’or à qui change un caractère', 'Gold to anyone who changes a character'), ('Un poste de ministre', 'A minister’s post'), ('Un nouveau livre', 'A new book')], 0),
    Q(('Que veut dire « 一字千金 » aujourd’hui ?', 'What does “一字千金” mean today?'), [('Un texte excellent', 'An excellent piece of writing'), ('Un livre très cher', 'A very expensive book'), ('Un caractère difficile', 'A difficult character')], 0),
  ]),
])

# 指鹿为马 (Mémoires historiques) — Zhao Gao à la cour de Qin
ZHILU = STORY('zhi-lu-wei-ma', '鹿', 'HSK4', '#8A5A3A', ('指鹿为马', 'Appeler un cerf un cheval', 'Calling a deer a horse'),
  ('Pour savoir qui lui obéit, le puissant Zhao Gao présente un cerf à l’empereur… et l’appelle un cheval.', 'To find out who obeys him, the powerful Zhao Gao presents a deer to the emperor… and calls it a horse.'), [
  CH('zhi-lu-wei-ma-1', ('一只鹿', 'Un cerf', 'A deer'), [
    [S4('秦始皇:Qín_Shǐhuáng 死:sǐ 了 以后 ， 他 的 儿子 当:dāng 了 皇帝:huángdì 。', 'Après la mort du Premier Empereur, son fils devint empereur.', 'After the First Emperor died, his son became emperor.'),
     S4('可是 真正:zhēnzhèng 有 权力:quánlì 的 人 ， 是 丞相:chéngxiàng 赵高:Zhào_Gāo 。', 'Mais celui qui détenait vraiment le pouvoir, c’était le chancelier Zhao Gao.', 'But the one who really held power was the chancellor Zhao Gao.'),
     S4('赵高:Zhào_Gāo 想 知道 ， 大臣:dàchén 们 是不是 都 听 他 的 话 。', 'Zhao Gao voulait savoir si tous les ministres lui obéissaient.', 'Zhao Gao wanted to know whether all the ministers obeyed him.')],
    [S4('一 天 ， 他 带 了 一 只:zhī 鹿:lù 来 到 皇帝:huángdì 面前:miànqián 。', 'Un jour, il amena un cerf devant l’empereur.', 'One day he brought a deer before the emperor.'),
     S4('他 笑 着 说 ： “ 陛下:bìxià ， 我 送 您 一 匹:pǐ 好 马 。 ”', 'Il dit en souriant : « Majesté, je vous offre un beau cheval. »', 'He said with a smile: “Your Majesty, I present you with a fine horse.”'),
     S4('皇帝:huángdì 笑 了 ： “ 丞相:chéngxiàng ， 你 弄:nòng 错 了 吧 ， 这 明明:míngmíng 是 一 只:zhī 鹿:lù 啊 ！ ”', 'L’empereur rit : « Chancelier, vous vous trompez, c’est de toute évidence un cerf ! »', 'The emperor laughed: “Chancellor, you’ve made a mistake; this is obviously a deer!”')],
  ], [
    W('皇帝', 'huángdì', 'empereur', 'emperor'),
    W('权力', 'quánlì', 'pouvoir', 'power'),
    W('大臣', 'dàchén', 'ministre (de cour)', 'minister (at court)'),
    W('鹿', 'lù', 'cerf', 'deer'),
    W('陛下', 'bìxià', 'Votre Majesté', 'Your Majesty'),
    W('明明', 'míngmíng', 'de toute évidence', 'obviously'),
  ], [
    Q(('Qui a le vrai pouvoir à la cour ?', 'Who holds the real power at court?'), [('Zhao Gao', 'Zhao Gao'), ('L’empereur', 'The emperor'), ('Les soldats', 'The soldiers')], 0),
    Q(('Qu’amène Zhao Gao devant l’empereur ?', 'What does Zhao Gao bring before the emperor?'), [('Un cerf', 'A deer'), ('Un cheval', 'A horse'), ('Un tigre', 'A tiger')], 0),
  ]),
  CH('zhi-lu-wei-ma-2', ('是马还是鹿？', 'Cheval ou cerf ?', 'Horse or deer?'), [
    [S4('赵高:Zhào_Gāo 转:zhuǎn 过 身:shēn ， 问 大臣:dàchén 们 ： “ 你们 说 ， 这 是 马 还是 鹿:lù ？ ”', 'Zhao Gao se retourna et demanda aux ministres : « À votre avis, est-ce un cheval ou un cerf ? »', 'Zhao Gao turned round and asked the ministers: “Tell me, is this a horse or a deer?”'),
     S4('有 的 大臣:dàchén 害怕 赵高:Zhào_Gāo ， 不 说话 ；', 'Certains ministres, qui le craignaient, se turent ;', 'Some ministers, afraid of Zhao Gao, said nothing;'),
     S4('有 的 大臣:dàchén 想 让 赵高:Zhào_Gāo 高兴 ， 马上:mǎshàng 说 ： “ 是 马 ！ ”', 'd’autres, voulant lui plaire, répondirent aussitôt : « C’est un cheval ! »', 'others, wanting to please him, immediately said: “It’s a horse!”')],
    [S4('只有 几 个 诚实:chéngshí 的 大臣:dàchén 说 ： “ 这 是 鹿:lù 。 ”', 'Seuls quelques ministres honnêtes dirent : « C’est un cerf. »', 'Only a few honest ministers said: “It’s a deer.”'),
     S4('后来 ， 赵高:Zhào_Gāo 找 了 理由:lǐyóu ， 把 他们 都 杀:shā 了 。', 'Plus tard, Zhao Gao trouva des prétextes pour les faire tous exécuter.', 'Later, Zhao Gao found pretexts to have them all killed.'),
     S4('从此:cóngcǐ ， 再 也 没有 人 敢:gǎn 反对:fǎnduì 赵高:Zhào_Gāo 了 。 人们 用 “ 指鹿为马:zhǐ_lù_wéi_mǎ ” 来 说 故意:gùyì 把 错 的 说 成 对 的 。', 'Dès lors, plus personne n’osa s’opposer à lui. « Appeler un cerf un cheval », c’est faire passer le faux pour le vrai.', 'From then on, nobody dared oppose him. “Calling a deer a horse” means deliberately passing off falsehood as truth.')],
  ], [
    W('转身', 'zhuǎn shēn', 'se retourner', 'to turn round'),
    W('诚实', 'chéngshí', 'honnête', 'honest'),
    W('理由', 'lǐyóu', 'raison, prétexte', 'reason, pretext'),
    W('杀', 'shā', 'tuer', 'to kill'),
    W('从此', 'cóngcǐ', 'dès lors', 'from then on'),
    W('敢', 'gǎn', 'oser', 'to dare'),
  ], [
    Q(('Que répondent les ministres honnêtes ?', 'What do the honest ministers answer?'), [('Que c’est un cerf', 'That it is a deer'), ('Que c’est un cheval', 'That it is a horse'), ('Rien du tout', 'Nothing at all')], 0),
    Q(('Que signifie « 指鹿为马 » ?', 'What does “指鹿为马” mean?'), [('Faire passer le faux pour le vrai', 'Passing off falsehood as truth'), ('Bien connaître les animaux', 'Knowing animals well'), ('Offrir un cadeau', 'Giving a present')], 0),
  ]),
])

# 完璧归赵 (Mémoires historiques) — Lin Xiangru face au roi de Qin
WANBI = STORY('wan-bi-gui-zhao', '璧', 'HSK4', '#2F7A6E', ('完璧归赵', 'Le jade rendu intact à Zhao', 'The jade returned intact to Zhao'),
  ('Le roi de Qin propose quinze villes contre un jade célèbre. Lin Xiangru part à Qin… et compte bien le rapporter.', 'The king of Qin offers fifteen cities for a famous jade. Lin Xiangru sets off for Qin… intending to bring it back.'), [
  CH('wan-bi-gui-zhao-1', ('和氏璧', 'Le jade de He', 'The jade of He'), [
    [S4('赵国:Zhào_guó 有 一 块 非常 有名 的 玉:yù ， 叫 “ 和氏璧:Héshì_bì ” 。', 'Le royaume de Zhao possédait un jade célèbre, le « jade de He ».', 'The state of Zhao owned a famous jade called “He’s jade”.'),
     S4('秦王:Qín_wáng 听说:tīngshuō 了 ， 写 信 给 赵王:Zhào_wáng ： “ 我 愿意 用 十五 座:zuò 城 换 你 的 玉:yù 。 ”', 'Le roi de Qin l’apprit et écrivit au roi de Zhao : « Je suis prêt à échanger quinze villes contre votre jade. »', 'The king of Qin heard of it and wrote to the king of Zhao: “I am willing to exchange fifteen cities for your jade.”'),
     S4('赵王:Zhào_wáng 很 着急 ： 给 秦王:Qín_wáng ， 恐怕:kǒngpà 拿 不 到 城 ； 不 给 ， 又 怕:pà 秦国:Qín_guó 来 打 赵国:Zhào_guó 。', 'Le roi de Zhao était inquiet : s’il le donnait, il n’aurait sans doute jamais les villes ; s’il refusait, Qin risquait de l’attaquer.', 'The king of Zhao was worried: if he handed it over, he would probably never get the cities; if he refused, Qin might attack.')],
    [S4('这 时 ， 一个 叫 蔺相如:Lìn_Xiàngrú 的 人 说 ： “ 我 愿意 带 着 玉:yù 去 秦国:Qín_guó 。', 'C’est alors qu’un homme nommé Lin Xiangru déclara : « J’irai à Qin avec le jade.', 'Then a man called Lin Xiangru said: “I will take the jade to Qin.'),
     S4('如果 秦王:Qín_wáng 给 城 ， 我 就 把 玉:yù 留:liú 在 秦国:Qín_guó ； 如果 不 给 ， 我 一定 把 玉:yù 完整:wánzhěng 地 带 回来 。 ”', 'Si le roi de Qin donne les villes, je lui laisserai le jade ; sinon, je le rapporterai intact. »', 'If the king of Qin gives the cities, I will leave the jade there; if not, I will bring it back intact.”')],
  ], [
    W('玉', 'yù', 'jade', 'jade'),
    W('座', 'zuò', 'classificateur (villes, montagnes)', 'measure word for cities, mountains'),
    W('恐怕', 'kǒngpà', 'je crains que', 'I’m afraid that'),
    W('留', 'liú', 'laisser', 'to leave'),
    W('完整', 'wánzhěng', 'intact, entier', 'intact, whole'),
    W('听说', 'tīngshuō', 'entendre dire', 'to hear that'),
  ], [
    Q(('Que propose le roi de Qin ?', 'What does the king of Qin offer?'), [('Quinze villes contre le jade', 'Fifteen cities for the jade'), ('De l’or contre le jade', 'Gold for the jade'), ('La paix', 'Peace')], 0),
    Q(('Que promet Lin Xiangru ?', 'What does Lin Xiangru promise?'), [('Rapporter le jade intact si Qin ne donne rien', 'To bring back the jade intact if Qin gives nothing'), ('Vendre le jade', 'To sell the jade'), ('Rester à Qin', 'To stay in Qin')], 0),
  ]),
  CH('wan-bi-gui-zhao-2', ('在秦王面前', 'Devant le roi de Qin', 'Before the king of Qin'), [
    [S4('蔺相如:Lìn_Xiàngrú 到 了 秦国:Qín_guó ， 把 玉:yù 送 给 秦王:Qín_wáng 。', 'Arrivé à Qin, Lin Xiangru remit le jade au roi.', 'Arriving in Qin, Lin Xiangru presented the jade to the king.'),
     S4('秦王:Qín_wáng 非常 高兴 ， 把 玉:yù 给 身边:shēnbiān 的 人 一个 一个 地 看 ， 可是 一 句 也 不 提:tí 城 的 事 。', 'Ravi, le roi le fit passer de main en main parmi ses proches, mais ne dit pas un mot des villes.', 'Delighted, the king passed it round his courtiers one by one, but never said a word about the cities.'),
     S4('蔺相如:Lìn_Xiàngrú 明白 了 ： 秦王:Qín_wáng 根本:gēnběn 不 想 给 城 。', 'Lin Xiangru comprit : le roi n’avait aucune intention de donner les villes.', 'Lin Xiangru understood: the king had no intention of giving the cities.')],
    [S4('他 走 上前:shàngqián 说 ： “ 这 块 玉:yù 上 有 一个 小 问题 ， 我 指:zhǐ 给 您 看 。 ”', 'Il s’avança : « Ce jade a un petit défaut, je vais vous le montrer. »', 'He stepped forward: “This jade has a small flaw; let me show you.”'),
     S4('秦王:Qín_wáng 把 玉:yù 还:huán 给 了 他 。', 'Le roi lui rendit le jade.', 'The king handed the jade back to him.'),
     S4('蔺相如:Lìn_Xiàngrú 拿 着 玉:yù 站 到 柱子:zhùzi 旁边 ， 大声:dàshēng 说 ： “ 如果 您 要 抢:qiǎng ， 我 就 和 玉:yù 一起 撞:zhuàng 在 柱子:zhùzi 上 ！ ”', 'Le jade en main, Lin Xiangru se plaça près d’une colonne et s’écria : « Si vous voulez le prendre de force, je me fracasse contre cette colonne avec lui ! »', 'Holding the jade, Lin Xiangru stood by a pillar and cried: “If you try to seize it, I’ll smash myself and the jade against this pillar!”')],
  ], [
    W('身边', 'shēnbiān', 'à ses côtés', 'at one’s side'),
    W('提', 'tí', 'mentionner', 'to mention'),
    W('根本', 'gēnběn', 'absolument (pas)', '(not) at all'),
    W('还', 'huán', 'rendre', 'to give back'),
    W('柱子', 'zhùzi', 'colonne', 'pillar'),
    W('抢', 'qiǎng', 's’emparer de force', 'to snatch'),
  ], [
    Q(('Pourquoi Lin Xiangru reprend-il le jade ?', 'Why does Lin Xiangru take the jade back?'), [('Le roi ne parle pas des villes', 'The king doesn’t mention the cities'), ('Le jade est cassé', 'The jade is broken'), ('Le roi le lui offre', 'The king gives it to him')], 0),
    Q(('Que menace-t-il de faire ?', 'What does he threaten to do?'), [('Se jeter contre la colonne avec le jade', 'Smash himself and the jade against the pillar'), ('Partir en courant', 'Run away'), ('Appeler les soldats de Zhao', 'Call the Zhao soldiers')], 0),
  ]),
  CH('wan-bi-gui-zhao-3', ('完璧归赵', 'Retour à Zhao', 'Back to Zhao'), [
    [S4('秦王:Qín_wáng 害怕 玉:yù 被 撞:zhuàng 坏 ， 只好:zhǐhǎo 说 ： “ 别 着急 ， 我 给 你 城 。 ”', 'Craignant que le jade soit brisé, le roi dut dire : « Calmez-vous, je vous donnerai les villes. »', 'Afraid the jade would be smashed, the king had to say: “Calm down, I’ll give you the cities.”'),
     S4('蔺相如:Lìn_Xiàngrú 知道 秦王:Qín_wáng 是 在 骗:piàn 他 。', 'Lin Xiangru savait que le roi le trompait.', 'Lin Xiangru knew the king was deceiving him.'),
     S4('晚上 ， 他 让 一个 手下:shǒuxià 穿 上 普通:pǔtōng 人 的 衣服 ， 偷偷:tōutōu 地 把 玉:yù 带 回 了 赵国:Zhào_guó 。', 'Le soir, il fit habiller un de ses hommes en simple paysan, qui rapporta le jade en secret à Zhao.', 'That night he had one of his men dress as an ordinary person and secretly carry the jade back to Zhao.')],
    [S4('第二 天 ， 秦王:Qín_wáng 发现 玉:yù 已经 不 在 了 ， 非常 生气 。', 'Le lendemain, le roi découvrit que le jade avait disparu et entra dans une grande colère.', 'The next day the king found the jade gone and was furious.'),
     S4('可是 蔺相如:Lìn_Xiàngrú 一点儿 也 不 害怕 ， 他 的 勇敢:yǒnggǎn 让 秦王:Qín_wáng 也 很 佩服:pèifu 。', 'Mais Lin Xiangru n’eut pas peur du tout, et son courage força l’admiration du roi lui-même.', 'But Lin Xiangru wasn’t afraid at all, and his courage won even the king’s admiration.'),
     S4('这 就是 “ 完璧归赵:wán_bì_guī_Zhào ” 的 故事 。', 'C’est l’histoire du « jade rendu intact à Zhao ».', 'This is the story of “returning the jade intact to Zhao”.')],
  ], [
    W('骗', 'piàn', 'tromper', 'to deceive'),
    W('手下', 'shǒuxià', 'homme de confiance, subordonné', 'subordinate'),
    W('普通', 'pǔtōng', 'ordinaire', 'ordinary'),
    W('偷偷', 'tōutōu', 'en cachette', 'secretly'),
    W('勇敢', 'yǒnggǎn', 'courageux', 'brave'),
    W('佩服', 'pèifu', 'admirer', 'to admire'),
  ], [
    Q(('Comment le jade revient-il à Zhao ?', 'How does the jade get back to Zhao?'), [('Un homme le rapporte en secret', 'A man secretly carries it back'), ('Le roi de Qin le rend', 'The king of Qin returns it'), ('Il est vendu', 'It is sold')], 0),
    Q(('Que ressent le roi de Qin pour Lin Xiangru ?', 'What does the king of Qin feel about Lin Xiangru?'), [('De l’admiration', 'Admiration'), ('De l’amitié', 'Friendship'), ('De la pitié', 'Pity')], 0),
  ]),
])

if MISSING:
    raise SystemExit('\n'.join(MISSING))
ZH_STORIES = [SHOUZHU, HUASHE, MAODUN, SUNZI, HUJIA, SAIWENG, MENGMU, YAMIAO, ZHUANGZI, YIZI, ZHILU, WANBI]

data = json.load(open(P, encoding='utf-8'))
data['stories'] = [s for s in data['stories'] if not s['level'].startswith('HSK')] + ZH_STORIES
data.setdefault('notices', {}).update({
  'zh': {'fr': 'Fables chinoises de l’époque des Royaumes combattants (domaine public), réécrites en chinois simple pour Koto Quest. Le pinyin s’affiche au-dessus des mots (à partir du HSK 3, seulement au-dessus des mots nouveaux du niveau) ; touche une phrase pour l’entendre et la traduire.', 'en': 'Chinese fables from the Warring States period (public domain), retold in simple Chinese for Koto Quest. Pinyin is shown above the words (from HSK 3 onwards, only above words new at that level); tap a sentence to hear and translate it.'},
})
slugs = [c['slug'] for s in data['stories'] for c in s['chapters']]
assert len(slugs) == len(set(slugs)), 'slug de chapitre en double'
for s in ZH_STORIES:
    for c in s['chapters']:
        assert len(c['words']) >= 6, c['slug']
        for q in c['questions']:
            assert 0 <= q['answer'] < len(q['choices'])
        for para in c['paragraphs']:
            for sent in para:
                assert (s['level'] in ('HSK3', 'HSK4') or '{' in sent['jp']) and ':' not in sent['kana'], sent['kana']
json.dump(data, open(P, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(f"Contes chinois : {len(ZH_STORIES)} contes, {sum(len(s['chapters']) for s in ZH_STORIES)} chapitres")
