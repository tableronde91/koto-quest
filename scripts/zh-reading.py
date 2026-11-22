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

ZH_STORIES = [SHOUZHU, HUASHE, MAODUN]

data = json.load(open(P, encoding='utf-8'))
data['stories'] = [s for s in data['stories'] if not s['level'].startswith('HSK')] + ZH_STORIES
data.setdefault('notices', {}).update({
  'zh': {'fr': 'Fables chinoises de l’époque des Royaumes combattants (domaine public), réécrites en chinois simple pour Koto Quest. Le pinyin s’affiche au-dessus des mots ; touche une phrase pour l’entendre et la traduire.', 'en': 'Chinese fables from the Warring States period (public domain), retold in simple Chinese for Koto Quest. Pinyin is shown above the words; tap a sentence to hear and translate it.'},
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
                assert '{' in sent['jp'] and ':' not in sent['kana'], sent['kana']
json.dump(data, open(P, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(f"Contes chinois : {len(ZH_STORIES)} contes, {sum(len(s['chapters']) for s in ZH_STORIES)} chapitres")
