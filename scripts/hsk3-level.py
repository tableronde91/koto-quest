# Niveau HSK 3 (chinois, HSK 2.0 niveau 3) : 8 étapes au royaume de Qi, leçons et examen blanc (français + anglais).
# Mode histoire : disciple de l'académie Jixia à Linzi, au temps des Cent Écoles (voir gen-story.py).
# Écrit aussi la section HSK 3 de l'onglet Hanzi.
# Usage : python3 scripts/hsk3-level.py   (après hsk1-level.py et hsk2-level.py)
from zh_common import *

# Slugs déjà pris par un autre niveau : suffixe « -h3 » (le même mot peut exister en japonais, coréen…).
_TAKEN = set()
for _p in ALL_LEVELS + HSK_PATHS[:2]:
    for _it in items_of(json.load(open(os.path.join(ROOT, _p), encoding='utf-8'))):
        _TAKEN.add(_it['slug'])
for _th in json.load(open(os.path.join(ROOT, 'content/expressions/expressions.json'), encoding='utf-8'))['themes']:
    _TAKEN.update(_e['slug'] for _e in _th['expressions'])
def _free(full):
    return full + '-h3' if full in _TAKEN else full
_Z, _ZG, _H = Z, ZG, H
def Z(slug, *a): return {**_Z(slug, *a), 'slug': _free('zh-' + slug)}
def ZG(slug, *a): return {**_ZG(slug, *a), 'slug': _free('gram-zh-' + slug)}
def H(slug, *a): return {**_H(slug, *a), 'slug': _free('hz-' + slug)}

REGION = 'Côtes de Qi'

# ═════════════════════════ 1 : l'auberge de Linzi — 把, la maison, la famille ═════════════════════════
W1 = WORLD('hsk3-w1', ('L’auberge de Linzi', 'The inn at Linzi'), REGION,
  ('Ranger, déplacer, nettoyer avec 把 ; la maison, les étages et les voisins ; toute la famille, et dire qui ressemble à qui (跟…一样, 像).', 'Tidying, moving and cleaning with 把; the house, floors and neighbours; the whole family, and saying who looks like whom (跟…一样, 像).'),
  (('Le Taowu têtu', 'The Stubborn Taowu'), '梼', ('Le Taowu, bête à visage d’homme et à crocs de sanglier, s’est couché dans l’auberge où tu loges et refuse de bouger quoi que ce soit. Dis précisément où mettre chaque chose pour le déloger.', 'The Taowu, a beast with a human face and boar’s tusks, has lain down in the inn where you are staying and refuses to move anything. Say exactly where to put each thing to dislodge it.')),
  [CH('hsk3-w1-c1', ('Ranger l’auberge', 'Tidying the inn'), [
    HL('zh-hz-ba', ('Les caractères du rangement : 把 搬 放 拿 带 换 关 楼', 'Tidying characters: 把 搬 放 拿 带 换 关 楼'), ('Reconnaître les caractères pour déplacer et ranger.', 'Recognise the characters for moving and tidying things.'), [
      ('把 (bǎ), 搬 (bān), 拿 (ná) et 换 (huàn) portent tous la clé de la main 扌 (ou 手 sous 拿, « réunir les mains ») : ce sont des gestes.', '把 (bǎ), 搬 (bān), 拿 (ná) and 换 (huàn) all carry the hand radical 扌 (or 手 under 拿, “bring the hands together”): they are gestures.'),
      ('楼 (lóu, immeuble) porte la clé du bois 木 : les premiers étages chinois étaient des pavillons en bois. 关 (guān) dessinait la barre qui ferme un portail.', '楼 (lóu, building) carries the wood radical 木: the first Chinese upper floors were wooden pavilions. 关 (guān) drew the bar that closes a gate.'),
    ], [
      H('ba', '把', 'bǎ', ('(marque l’objet que l’on déplace ou traite)', '(marks the object being moved or handled)'), 7), H('ban-move', '搬', 'bān', ('déménager, transporter', 'to move (house), to carry'), 13),
      H('fang', '放', 'fàng', ('poser, mettre', 'to put, to place'), 8), H('na', '拿', 'ná', ('prendre (en main)', 'to take, to hold'), 10),
      H('dai', '带', 'dài', ('emporter, emmener', 'to take along, to bring'), 9), H('huan', '换', 'huàn', ('changer, échanger', 'to change, to exchange'), 10),
      H('guan', '关', 'guān', ('fermer, éteindre', 'to close, to switch off'), 6), H('lou', '楼', 'lóu', ('immeuble, bâtiment à étages', 'building (with floors)'), 13),
    ]),
    L('zh-ba', ('Mettre la tasse sur la table : la phrase avec 把', 'Put the cup on the table: the 把 sentence'), ('Dire ce qu’on fait d’un objet précis.', 'Say what you do with a specific object.'), 10, [
        ('Sujet + 把 + objet + verbe + suite : 我把杯子放在桌子上 (je pose la tasse sur la table). 把 avance l’objet devant le verbe pour dire ce qu’il devient.', 'Subject + 把 + object + verb + result: 我把杯子放在桌子上 (I put the cup on the table). 把 moves the object before the verb to say what happens to it.'),
        ('Le verbe ne reste jamais seul après 把 : il faut un résultat, un lieu ou 了. On dit 把门关上 ou 把门关了, pas « 把门关 ». L’objet est connu : « la » porte, « ce » livre.', 'The verb is never left alone after 把: it needs a result, a place or 了. You say 把门关上 or 把门关了, not “把门关”. The object is a known one: “the” door, “that” book.'),
        ('La négation se place avant 把 : 我没把手机带来 (je n’ai pas apporté mon portable).', 'The negative goes before 把: 我没把手机带来 (I didn’t bring my phone).'),
      ], [
        ZG('ba', '主语 + 把 + 宾语 + 动词 + 其他', 'bǎ', ('faire quelque chose à un objet précis (phrase en 把)', 'to do something to a specific object (把 sentence)')),
        Z('ba', '把', 'bǎ', ('(marque l’objet que l’on déplace ou traite)', '(marks the object being moved or handled)')),
        Z('fang', '放', 'fàng', ('poser, mettre', 'to put, to place')),
        Z('na', '拿', 'ná', ('prendre (en main)', 'to take, to hold')),
        Z('dai', '带', 'dài', ('emporter, emmener', 'to take along, to bring')),
        Z('ban', '搬', 'bān', ('déménager, transporter', 'to move (house), to carry')),
        Z('huan', '换', 'huàn', ('changer, échanger', 'to change, to exchange')),
        Z('guan', '关', 'guān', ('fermer, éteindre', 'to close, to switch off')),
        Z('deng', '灯', 'dēng', ('lampe, lumière', 'lamp, light')),
        Z('ganjing', '干净', 'gānjìng', ('propre', 'clean')),
        Z('dasao', '打扫', 'dǎsǎo', ('faire le ménage, nettoyer', 'to clean, to sweep')),
      ], [
        x('请把门关上，外面很冷。', 'Qǐng bǎ mén guānshang, wàimiàn hěn lěng.', 'Ferme la porte, s’il te plaît, il fait froid dehors.', 'Please close the door; it’s cold outside.'),
        x('我已经把房间打扫干净了。', 'Wǒ yǐjīng bǎ fángjiān dǎsǎo gānjìng le.', 'J’ai déjà fait le ménage dans la chambre.', 'I’ve already cleaned the room.'),
      ], [
        FB(COMPLETE, '你＿书放在哪儿了？', ['把', '被', '给'], '把', ('Ce qu’on fait d’un objet connu : 把 + objet + verbe.', 'What you do with a known object: 把 + object + verb.'), ('Où as-tu mis le livre ?', 'Where did you put the book?')),
        FB(COMPLETE, '睡觉以前，请把灯＿了。', ['关', '放', '拿'], '关', ('Éteindre la lumière : 关灯.', 'Switch off the light: 关灯.'), ('Avant de dormir, éteins la lumière, s’il te plaît.', 'Please switch off the light before going to sleep.')),
        SO(ORDER('Il a mis la valise dans la voiture.', 'He put the suitcase in the car.'), ['他', '把', '箱子', '放在', '车里', '了。'], ('Sujet + 把 + objet + verbe + lieu.', 'Subject + 把 + object + verb + place.')),
        TF('我没把手机带来。', ('La personne a apporté son portable.', 'The speaker brought their phone.'), FAUX, ('没把…带来 = ne pas avoir apporté.', '没把…带来 = didn’t bring.')),
      ]),
    L('zh-building', ('Étages, ascenseur, voisins : la vie dans l’immeuble', 'Floors, lift, neighbours: life in a building'), ('Décrire son logement et ses habitudes à la maison.', 'Describe your home and your routine at home.'), 9, [
        ('楼 (lóu) = immeuble : 那栋楼很高 ; on habite au 三楼 (troisième étage). 层 (céng) compte les étages : 这个楼有二十层. 电梯 (diàntī) = ascenseur.', '楼 (lóu) = building: 那栋楼很高; you live on the 三楼 (third floor). 层 (céng) counts floors: 这个楼有二十层. 电梯 (diàntī) = lift.'),
        ('À la maison : 冰箱 (réfrigérateur), 空调 (climatisation), 洗手间 (toilettes). Le soir, on 刷牙 (se brosse les dents) et on 洗澡 (prend une douche).', 'At home: 冰箱 (fridge), 空调 (air conditioning), 洗手间 (toilet). In the evening you 刷牙 (brush your teeth) and 洗澡 (take a shower).'),
        ('一边…一边… = faire deux choses en même temps : 他一边吃饭，一边看电视.', '一边…一边… = to do two things at once: 他一边吃饭，一边看电视.'),
      ], [
        ZG('yibian', '一边…，一边…', 'yìbiān…, yìbiān…', ('faire deux choses à la fois', 'to do two things at the same time')),
        Z('lou', '楼', 'lóu', ('immeuble, bâtiment à étages', 'building (with floors)')),
        Z('ceng', '层', 'céng', ('étage (classificateur)', 'floor, storey (measure word)')),
        Z('dianti', '电梯', 'diàntī', ('ascenseur', 'lift, elevator')),
        Z('linju', '邻居', 'línjū', ('voisin', 'neighbour')),
        Z('bingxiang', '冰箱', 'bīngxiāng', ('réfrigérateur', 'fridge')),
        Z('kongtiao', '空调', 'kōngtiáo', ('climatisation', 'air conditioning')),
        Z('xishoujian', '洗手间', 'xǐshǒujiān', ('toilettes', 'toilet, restroom')),
        Z('xizao', '洗澡', 'xǐzǎo', ('prendre une douche, un bain', 'to take a shower, to bathe')),
        Z('shuaya', '刷牙', 'shuāyá', ('se brosser les dents', 'to brush one’s teeth')),
        Z('anjing', '安静', 'ānjìng', ('calme, silencieux', 'quiet')),
        Z('fangbian', '方便', 'fāngbiàn', ('pratique, commode', 'convenient')),
      ], [
        x('我住在十二楼，每天坐电梯上下。', 'Wǒ zhù zài shí’èr lóu, měi tiān zuò diàntī shàngxià.', 'J’habite au douzième étage, je prends l’ascenseur tous les jours.', 'I live on the twelfth floor and take the lift every day.'),
        x('我的邻居一边洗澡，一边唱歌。', 'Wǒ de línjū yìbiān xǐzǎo, yìbiān chànggē.', 'Mon voisin chante sous la douche.', 'My neighbour sings while he showers.'),
      ], [
        FB(COMPLETE, '这个楼有三十＿，我们坐电梯吧。', ['层', '楼', '个'], '层', ('Compter les étages : 层.', 'Counting floors: 层.'), ('Cet immeuble a trente étages, prenons l’ascenseur.', 'This building has thirty floors; let’s take the lift.')),
        FB(COMPLETE, '牛奶在＿里。', ['冰箱', '空调', '电梯'], '冰箱', ('Le lait se garde au réfrigérateur : 冰箱.', 'Milk is kept in the fridge: 冰箱.'), ('Le lait est dans le réfrigérateur.', 'The milk is in the fridge.')),
        SO(ORDER('Elle écoute de la musique en faisant ses devoirs.', 'She listens to music while doing her homework.'), ['她', '一边', '听歌，', '一边', '做作业。'], ('一边 A，一边 B.', '一边 A，一边 B.')),
        TF('这儿很安静，住在这儿很方便。', ('L’endroit est bruyant.', 'The place is noisy.'), FAUX, ('安静 = calme.', '安静 = quiet.')),
      ]),
  ]),
  CH('hsk3-w1-c2', ('La famille de l’aubergiste', 'The innkeeper’s family'), [
    L('zh-family3', ('Grands-parents, oncles, tantes : 跟…一样 et 像', 'Grandparents, uncles, aunts: 跟…一样 and 像'), ('Présenter la famille élargie et comparer les ressemblances.', 'Introduce the wider family and compare likenesses.'), 10, [
        ('爷爷 / 奶奶 = grand-père / grand-mère (côté du père). 叔叔 = oncle, et 阿姨 = tante ; les enfants appellent aussi ainsi tous les adultes amis de la famille.', '爷爷 / 奶奶 = grandfather / grandmother (father’s side). 叔叔 = uncle and 阿姨 = aunt; children also call any adult family friend this way.'),
        ('A 跟 B 一样 (+ adjectif) = A est pareil que B : 我跟哥哥一样高. A 像 B = A ressemble à B : 你很像你妈妈.', 'A 跟 B 一样 (+ adjective) = A is the same as B: 我跟哥哥一样高. A 像 B = A looks like B: 你很像你妈妈.'),
        ('照顾 (zhàogù) = s’occuper de quelqu’un ; 关心 (guānxīn) = se soucier de. 自己 (zìjǐ) = soi-même ; 别人 (biérén) = les autres.', '照顾 (zhàogù) = to look after someone; 关心 (guānxīn) = to care about. 自己 (zìjǐ) = oneself; 别人 (biérén) = other people.'),
      ], [
        ZG('gen-yiyang', 'A 跟 B 一样 (+ 形容词)', 'gēn… yíyàng', ('A est pareil que B', 'A is the same as B')),
        Z('yeye', '爷爷', 'yéye', ('grand-père (paternel)', 'grandfather (paternal)')),
        Z('nainai', '奶奶', 'nǎinai', ('grand-mère (paternelle)', 'grandmother (paternal)')),
        Z('shushu', '叔叔', 'shūshu', ('oncle', 'uncle')),
        Z('ayi', '阿姨', 'āyí', ('tante, madame', 'aunt, auntie')),
        Z('gen', '跟', 'gēn', ('avec ; suivre', 'with; to follow')),
        Z('yiyang', '一样', 'yíyàng', ('la même chose, pareil', 'the same')),
        Z('xiang', '像', 'xiàng', ('ressembler à ; comme', 'to resemble; like')),
        Z('zhaogu', '照顾', 'zhàogù', ('s’occuper de, prendre soin de', 'to look after')),
        Z('guanxin', '关心', 'guānxīn', ('se soucier de', 'to care about')),
        Z('nianqing', '年轻', 'niánqīng', ('jeune', 'young')),
        Z('lao', '老', 'lǎo', ('vieux ; âgé (âge)', 'old')),
        Z('ziji', '自己', 'zìjǐ', ('soi-même', 'oneself')),
        Z('bieren', '别人', 'biérén', ('les autres, autrui', 'other people')),
      ], [
        x('奶奶年纪大了，妈妈每天照顾她。', 'Nǎinai niánjì dà le, māma měi tiān zhàogù tā.', 'Grand-mère est âgée, maman s’occupe d’elle tous les jours.', 'Grandma is getting old; mum looks after her every day.'),
        x('你跟你爸爸一样高，也很像他。', 'Nǐ gēn nǐ bàba yíyàng gāo, yě hěn xiàng tā.', 'Tu es aussi grand que ton père, et tu lui ressembles beaucoup.', 'You’re as tall as your father, and you look a lot like him.'),
      ], [
        FB(COMPLETE, '我的衣服跟你的＿。', ['一样', '比', '像'], '一样', ('Pareil : A 跟 B 一样.', 'The same: A 跟 B 一样.'), ('Mes vêtements sont pareils que les tiens.', 'My clothes are the same as yours.')),
        FB(COMPLETE, '他长得很＿他爷爷。', ['像', '跟', '一样'], '像', ('Ressembler à : 像.', 'To look like: 像.'), ('Il ressemble beaucoup à son grand-père.', 'He looks a lot like his grandfather.')),
        DC(ANSWER, [('阿姨', '你妈妈的身体怎么样？')], ('Une amie de la famille demande des nouvelles de ta mère (elle va bien, merci).', 'A family friend asks after your mother (she is well, thank you).'), ['她很好，谢谢阿姨关心。', '她很好，阿姨很年轻。', '她跟阿姨一样。'], '她很好，谢谢阿姨关心。', ('Remercier de l’attention : 谢谢…关心.', 'Thank someone for their concern: 谢谢…关心.')),
        TF('别人的东西不能随便拿。', ('On peut prendre les affaires des autres.', 'You can take other people’s things.'), FAUX, ('不能随便拿 = ne pas prendre sans demander.', '不能随便拿 = don’t take without asking.')),
      ]),
  ])])

# ═════════════════════════ 2 : le marché de Linzi — faim, repas, achats ═════════════════════════
W2 = WORLD('hsk3-w2', ('Le marché de Linzi', 'The Linzi market'), REGION,
  ('Avoir faim, soif, être rassasié ; commander au restaurant, payer en tout ; 又…又 et 除了…以外.', 'Being hungry, thirsty or full; ordering at a restaurant, paying in total; 又…又 and 除了…以外.'),
  (('L’oiseau Jingwei', 'The Jingwei Bird'), '精', ('Jingwei, la princesse noyée devenue oiseau, jette sans relâche des cailloux dans la mer… et dans les paniers des marchands de Linzi. Commande, compte et paie sans erreur pour l’apaiser.', 'Jingwei, the drowned princess turned bird, endlessly drops pebbles into the sea… and into the baskets of Linzi’s merchants. Order, count and pay without a mistake to calm her.')),
  [CH('hsk3-w2-c1', ('Les étals', 'The stalls'), [
    HL('zh-hz-food', ('Les caractères du repas : 饿 饱 渴 甜 鲜 面 包 碗', 'Meal characters: 饿 饱 渴 甜 鲜 面 包 碗'), ('Reconnaître les caractères de la faim et de la nourriture.', 'Recognise the characters for hunger and food.'), [
      ('饿 (è, avoir faim) et 饱 (bǎo, rassasié) portent la clé de la nourriture 饣 ; 渴 (kě, avoir soif) celle de l’eau 氵.', '饿 (è, hungry) and 饱 (bǎo, full) carry the food radical 饣; 渴 (kě, thirsty) the water radical 氵.'),
      ('鲜 (xiān, frais) réunit le poisson 鱼 et le mouton 羊 : les deux mets les plus savoureux. 甜 (tián, sucré) met la langue 舌 à côté de 甘 (doux).', '鲜 (xiān, fresh) joins fish 鱼 and sheep 羊: the two tastiest foods. 甜 (tián, sweet) puts the tongue 舌 next to 甘 (sweet).'),
    ], [
      H('e', '饿', 'è', ('avoir faim', 'hungry'), 10), H('bao-full', '饱', 'bǎo', ('rassasié', 'full (after eating)'), 8),
      H('ke-thirsty', '渴', 'kě', ('avoir soif', 'thirsty'), 12), H('tian', '甜', 'tián', ('doux, sucré', 'sweet'), 11),
      H('xian', '鲜', 'xiān', ('frais', 'fresh'), 14), H('mian', '面', 'miàn', ('farine, nouilles ; face', 'flour, noodles; face'), 9),
      H('bao-bag', '包', 'bāo', ('sac ; envelopper', 'bag; to wrap'), 5), H('wan', '碗', 'wǎn', ('bol', 'bowl'), 13),
    ]),
    L('zh-hungry', ('J’ai faim ! 饿、饱、渴 et 又…又', 'I’m hungry! 饿, 饱, 渴 and 又…又'), ('Dire si l’on a faim ou soif et décrire ce qu’on mange.', 'Say whether you are hungry or thirsty and describe what you eat.'), 9, [
        ('饿 (è) = avoir faim, 渴 (kě) = avoir soif, 饱 (bǎo) = être rassasié. Ce sont des adjectifs : 我饿了 (j’ai faim, maintenant), 我吃饱了 (j’ai assez mangé).', '饿 (è) = hungry, 渴 (kě) = thirsty, 饱 (bǎo) = full. They are adjectives: 我饿了 (I’m hungry now), 我吃饱了 (I’ve had enough).'),
        ('又 A 又 B = à la fois A et B : 这个蛋糕又甜又好吃 (ce gâteau est à la fois sucré et bon).', '又 A 又 B = both A and B: 这个蛋糕又甜又好吃 (this cake is both sweet and tasty).'),
        ('Au marché : 面包 (pain), 面条 (nouilles), 蛋糕 (gâteau), 香蕉 (banane), 果汁 (jus de fruits), 啤酒 (bière), 饮料 (boisson).', 'At the market: 面包 (bread), 面条 (noodles), 蛋糕 (cake), 香蕉 (banana), 果汁 (fruit juice), 啤酒 (beer), 饮料 (drink).'),
      ], [
        ZG('you-you', '又 + 形容词 + 又 + 形容词', 'yòu… yòu…', ('à la fois… et…', 'both… and…')),
        Z('e', '饿', 'è', ('avoir faim', 'hungry')),
        Z('bao', '饱', 'bǎo', ('rassasié', 'full (after eating)')),
        Z('ke-thirsty', '渴', 'kě', ('avoir soif', 'thirsty')),
        Z('tian', '甜', 'tián', ('doux, sucré', 'sweet')),
        Z('xinxian', '新鲜', 'xīnxiān', ('frais', 'fresh')),
        Z('you-again', '又', 'yòu', ('de nouveau (déjà fait) ; à la fois', 'again (already done); both')),
        Z('mianbao', '面包', 'miànbāo', ('pain', 'bread')),
        Z('miantiao', '面条', 'miàntiáo', ('nouilles', 'noodles')),
        Z('dangao', '蛋糕', 'dàngāo', ('gâteau', 'cake')),
        Z('xiangjiao', '香蕉', 'xiāngjiāo', ('banane', 'banana')),
        Z('guozhi', '果汁', 'guǒzhī', ('jus de fruits', 'fruit juice')),
        Z('pijiu', '啤酒', 'píjiǔ', ('bière', 'beer')),
        Z('yinliao', '饮料', 'yǐnliào', ('boisson', 'drink, beverage')),
      ], [
        x('我饿了，我们去吃面条吧。', 'Wǒ è le, wǒmen qù chī miàntiáo ba.', 'J’ai faim, allons manger des nouilles.', 'I’m hungry; let’s go and eat noodles.'),
        x('这儿的水果又新鲜又便宜。', 'Zhèr de shuǐguǒ yòu xīnxiān yòu piányi.', 'Ici, les fruits sont à la fois frais et bon marché.', 'The fruit here is both fresh and cheap.'),
      ], [
        FB(COMPLETE, '我吃＿了，不要了，谢谢。', ['饱', '饿', '渴'], '饱', ('Assez mangé : 吃饱了.', 'Had enough: 吃饱了.'), ('J’ai assez mangé, je n’en veux plus, merci.', 'I’m full, no more, thank you.')),
        FB(COMPLETE, '跑了一个小时，我很＿，想喝水。', ['渴', '饱', '甜'], '渴', ('Envie de boire : 渴.', 'Wanting to drink: 渴.'), ('Après une heure de course, j’ai très soif et je veux boire de l’eau.', 'After running for an hour I’m very thirsty and want some water.')),
        FB(COMPLETE, '这个蛋糕＿甜＿好吃。', ['又…又', '一边…一边', '因为…所以'], '又…又', ('Deux qualités : 又 A 又 B.', 'Two qualities: 又 A 又 B.'), ('Ce gâteau est sucré et délicieux.', 'This cake is sweet and delicious.')),
        TF('他不喝啤酒，他喝果汁。', ('Il boit de la bière.', 'He drinks beer.'), FAUX, ('不喝啤酒 = il ne boit pas de bière.', '不喝啤酒 = he doesn’t drink beer.')),
      ]),
  ]),
  CH('hsk3-w2-c2', ('À la table du marché', 'At the market table'), [
    L('zh-restaurant', ('Au restaurant : la carte, les bols, l’addition', 'At the restaurant: the menu, bowls, the bill'), ('Commander, demander ce qu’il faut et payer.', 'Order, ask for what you need and pay.'), 10, [
        ('菜单 (càidān) = la carte. On demande : 服务员，请给我们菜单. Sur la table : 碗 (bol), 盘子 (assiette), 筷子 (baguettes), 瓶子 (bouteille).', '菜单 (càidān) = the menu. You ask: 服务员，请给我们菜单. On the table: 碗 (bowl), 盘子 (plate), 筷子 (chopsticks), 瓶子 (bottle).'),
        ('L’argent : 一共 (en tout), 角 (jiǎo, un dixième de yuan, à l’oral 毛), 万 (dix mille) : 一万元. 花 (huā) = dépenser : 我花了一百块.', 'Money: 一共 (in total), 角 (jiǎo, a tenth of a yuan, spoken 毛), 万 (ten thousand): 一万元. 花 (huā) = to spend: 我花了一百块.'),
        ('除了 A (以外)，都 / 还 … = à part A, … : 除了鱼以外，我什么都吃 (je mange tout sauf le poisson) ; 除了茶，我还喝咖啡 (en plus du thé, je bois aussi du café).', '除了 A (以外)，都 / 还 … = apart from A, …: 除了鱼以外，我什么都吃 (I eat everything except fish); 除了茶，我还喝咖啡 (besides tea, I also drink coffee).'),
      ], [
        ZG('chule', '除了…（以外），都 / 还…', 'chúle… (yǐwài)', ('à part…, en plus de…', 'apart from…, besides…')),
        Z('caidan', '菜单', 'càidān', ('menu, carte', 'menu')),
        Z('wan', '碗', 'wǎn', ('bol', 'bowl')),
        Z('panzi', '盘子', 'pánzi', ('assiette', 'plate')),
        Z('kuaizi', '筷子', 'kuàizi', ('baguettes', 'chopsticks')),
        Z('pingzi', '瓶子', 'píngzi', ('bouteille', 'bottle')),
        Z('keren', '客人', 'kèrén', ('invité, client', 'guest, customer')),
        Z('reqing', '热情', 'rèqíng', ('chaleureux, accueillant', 'warm, welcoming')),
        Z('yigong', '一共', 'yígòng', ('en tout, au total', 'in total')),
        Z('jiao', '角', 'jiǎo', ('jiao (dixième de yuan) ; corne, angle', 'jiao (tenth of a yuan); horn, corner')),
        Z('wan-tenk', '万', 'wàn', ('dix mille', 'ten thousand')),
        Z('chaoshi', '超市', 'chāoshì', ('supermarché', 'supermarket')),
        Z('chule', '除了', 'chúle', ('à part, sauf', 'except, apart from')),
      ], [
        x('服务员，我们要两碗米饭，一共多少钱？', 'Fúwùyuán, wǒmen yào liǎng wǎn mǐfàn, yígòng duōshao qián?', 'S’il vous plaît, deux bols de riz. Ça fait combien en tout ?', 'Excuse me, two bowls of rice. How much is it altogether?'),
        x('除了筷子以外，我们还需要两个盘子。', 'Chúle kuàizi yǐwài, wǒmen hái xūyào liǎng ge pánzi.', 'En plus des baguettes, il nous faut aussi deux assiettes.', 'Besides chopsticks, we also need two plates.'),
      ], [
        FB(COMPLETE, '一＿面条十五块。', ['碗', '个', '张'], '碗', ('Un bol de nouilles : 一碗面条.', 'A bowl of noodles: 一碗面条.'), ('Un bol de nouilles coûte quinze yuans.', 'A bowl of noodles costs fifteen yuan.')),
        FB(COMPLETE, '这些东西＿一百二十块。', ['一共', '一起', '一样'], '一共', ('Le total : 一共.', 'The total: 一共.'), ('Tout cela fait cent vingt yuans en tout.', 'All these things come to a hundred and twenty yuan in total.')),
        FB(COMPLETE, '＿星期天，我每天都上班。', ['除了', '因为', '虽然'], '除了', ('Sauf le dimanche : 除了星期天.', 'Except Sunday: 除了星期天.'), ('Je travaille tous les jours sauf le dimanche.', 'I work every day except Sunday.')),
        DC(ANSWER, [('服务员', '您好，几位？')], ('Le serveur demande combien vous êtes (trois).', 'The waiter asks how many you are (three).'), ['三位，请给我们菜单。', '三碗，谢谢。', '三块钱。'], '三位，请给我们菜单。', ('Compter poliment les personnes : 位.', 'Counting people politely: 位.')),
      ]),
  ])])

# ═════════════════════════ 3 : l'école de Confucius — étudier ═════════════════════════
W3 = WORLD('hsk3-w3', ('L’école de Confucius', 'The school of Confucius'), REGION,
  ('Réviser, s’exercer, progresser (越来越) ; dire si l’on peut comprendre (看得懂, 听不清楚) ; emprunter à la bibliothèque, se souvenir, oublier.', 'Revising, practising, improving (越来越); saying whether you can understand (看得懂, 听不清楚); borrowing from the library, remembering, forgetting.'),
  (('Le Zheng aux cinq queues', 'The Five-Tailed Zheng'), '狰', ('Le Zheng, léopard rouge à cinq queues et à une corne, fait un bruit de pierres qui s’entrechoquent : plus personne n’entend le maître. Montre que tu comprends malgré le vacarme.', 'The Zheng, a red leopard with five tails and one horn, makes a noise like clashing stones: no one can hear the master any more. Show that you understand despite the din.')),
  [CH('hsk3-w3-c1', ('Les élèves du maître', 'The master’s pupils'), [
    HL('zh-hz-study', ('Les caractères de l’étude : 复 习 练 作 业 级 努 力', 'Study characters: 复 习 练 作 业 级 努 力'), ('Reconnaître les caractères de l’étude et de l’effort.', 'Recognise the characters of study and effort.'), [
      ('习 (xí) montrait un oisillon qui bat des ailes encore et encore : apprendre, c’est répéter. Confucius commence ses Entretiens par 学而时习之 (apprendre et réviser sans cesse).', '习 (xí) showed a fledgling beating its wings again and again: to learn is to repeat. Confucius opens his Analects with 学而时习之 (to learn and keep practising).'),
      ('努 (nǔ) et 力 (lì) : 力 dessine une charrue ou un bras musclé ; 努 ajoute l’esclave 奴 au-dessus : faire un effort de toutes ses forces.', '努 (nǔ) and 力 (lì): 力 draws a plough or a strong arm; 努 adds 奴 (slave) on top: to strive with all one’s strength.'),
    ], [
      H('fu', '复', 'fù', ('répéter, revenir', 'to repeat, to return'), 9), H('xi-practice', '习', 'xí', ('s’exercer, habitude', 'to practise, habit'), 3),
      H('lian', '练', 'liàn', ('s’entraîner', 'to train'), 8), H('zuo-make', '作', 'zuò', ('faire, œuvre', 'to do, work'), 7),
      H('ye', '业', 'yè', ('métier, études', 'trade, studies'), 5), H('ji-grade', '级', 'jí', ('degré, année (scolaire)', 'grade, level'), 6),
      H('nu', '努', 'nǔ', ('faire un effort', 'to strive'), 7), H('li', '力', 'lì', ('force', 'strength, force'), 2),
    ]),
    L('zh-study', ('Réviser et progresser : 复习、练习、越来越', 'Revising and improving: 复习, 练习, 越来越'), ('Parler de ses études et de ses progrès.', 'Talk about your studies and your progress.'), 10, [
        ('复习 (fùxí) = réviser ; 练习 (liànxí) = s’exercer, un exercice ; 作业 (zuòyè) = les devoirs ; 成绩 (chéngjì) = les résultats ; 水平 (shuǐpíng) = le niveau.', '复习 (fùxí) = to revise; 练习 (liànxí) = to practise, an exercise; 作业 (zuòyè) = homework; 成绩 (chéngjì) = results, grades; 水平 (shuǐpíng) = level.'),
        ('越来越 + adjectif = de plus en plus : 你的汉语越来越好了 (ton chinois est de mieux en mieux).', '越来越 + adjective = more and more: 你的汉语越来越好了 (your Chinese is getting better and better).'),
        ('提高 (tígāo) = améliorer : 提高水平. 努力 (nǔlì) = faire des efforts ; 认真 (rènzhēn) = sérieux ; 聪明 (cōngming) = intelligent.', '提高 (tígāo) = to improve: 提高水平. 努力 (nǔlì) = to work hard; 认真 (rènzhēn) = conscientious; 聪明 (cōngming) = clever.'),
      ], [
        ZG('yuelaiyue', '越来越 + 形容词', 'yuè lái yuè', ('de plus en plus', 'more and more')),
        Z('fuxi', '复习', 'fùxí', ('réviser', 'to revise')),
        Z('lianxi', '练习', 'liànxí', ('s’exercer ; exercice', 'to practise; exercise')),
        Z('zuoye', '作业', 'zuòyè', ('devoirs', 'homework')),
        Z('nianji', '年级', 'niánjí', ('année (scolaire)', 'grade, year (at school)')),
        Z('shuxue', '数学', 'shùxué', ('mathématiques', 'mathematics')),
        Z('lishi', '历史', 'lìshǐ', ('histoire (du passé)', 'history')),
        Z('chengji', '成绩', 'chéngjì', ('résultats (scolaires), notes', 'results, grades')),
        Z('shuiping', '水平', 'shuǐpíng', ('niveau', 'level, standard')),
        Z('tigao', '提高', 'tígāo', ('améliorer, élever', 'to improve, to raise')),
        Z('nuli', '努力', 'nǔlì', ('faire des efforts', 'to work hard, to make an effort')),
        Z('renzhen', '认真', 'rènzhēn', ('sérieux, consciencieux', 'conscientious, serious')),
        Z('congming', '聪明', 'cōngming', ('intelligent', 'clever')),
      ], [
        x('我每天晚上复习一个小时，成绩越来越好了。', 'Wǒ měi tiān wǎnshang fùxí yí ge xiǎoshí, chéngjì yuè lái yuè hǎo le.', 'Je révise une heure chaque soir : mes notes sont de mieux en mieux.', 'I revise for an hour every evening; my grades are getting better and better.'),
        x('他是三年级的学生，学习非常认真。', 'Tā shì sān niánjí de xuésheng, xuéxí fēicháng rènzhēn.', 'Il est en troisième année et étudie très sérieusement.', 'He’s a third-year student and studies very conscientiously.'),
      ], [
        FB(COMPLETE, '天气＿冷了。', ['越来越', '一边', '又'], '越来越', ('De plus en plus : 越来越.', 'More and more: 越来越.'), ('Il fait de plus en plus froid.', 'It’s getting colder and colder.')),
        FB(COMPLETE, '要＿汉语水平，就要多听多说。', ['提高', '复习', '努力'], '提高', ('Améliorer le niveau : 提高水平.', 'Raise your level: 提高水平.'), ('Pour améliorer son niveau de chinois, il faut beaucoup écouter et parler.', 'To improve your Chinese, you must listen and speak a lot.')),
        DC(ANSWER, [('老师', '作业做完了吗？')], ('Le maître demande si tu as fini tes devoirs (oui, depuis longtemps).', 'The master asks if you have finished your homework (yes, long ago).'), ['早就做完了。', '我很聪明。', '我在三年级。'], '早就做完了。', ('Fini depuis longtemps : 早就做完了.', 'Finished long ago: 早就做完了.')),
        TF('她数学成绩很好，历史成绩不太好。', ('Elle est forte en histoire.', 'She is good at history.'), FAUX, ('历史成绩不太好 = pas très bonne en histoire.', '历史成绩不太好 = not very good at history.')),
      ]),
    L('zh-potential', ('Je comprends, je ne vois pas : 看得懂、听不清楚', 'I understand, I can’t see: 看得懂, 听不清楚'), ('Dire si l’on peut, ou non, arriver au résultat.', 'Say whether you can, or can’t, achieve a result.'), 10, [
        ('Verbe + 得 + résultat = pouvoir y arriver ; verbe + 不 + résultat = ne pas y arriver : 看得懂 (je comprends en lisant), 听不清楚 (je n’entends pas bien), 做不完 (je ne pourrai pas finir).', 'Verb + 得 + result = can achieve it; verb + 不 + result = can’t: 看得懂 (I can read and understand), 听不清楚 (I can’t hear clearly), 做不完 (I can’t finish).'),
        ('清楚 (qīngchu) = clair ; 明白 (míngbai) = comprendre, clair ; 了解 (liǎojiě) = bien connaître, se renseigner sur.', '清楚 (qīngchu) = clear; 明白 (míngbai) = to understand, clear; 了解 (liǎojiě) = to know well, to find out about.'),
        ('简单 / 容易 = simple / facile ; 难 = difficile. 讲 (jiǎng) = expliquer, raconter ; 教 (jiāo) = enseigner : 他教我们历史.', '简单 / 容易 = simple / easy; 难 = difficult. 讲 (jiǎng) = to explain, to tell; 教 (jiāo) = to teach: 他教我们历史.'),
      ], [
        ZG('kede', '动词 + 得 / 不 + 结果', 'de / bu', ('pouvoir / ne pas pouvoir (complément de potentiel)', 'can / can’t (potential complement)')),
        Z('qingchu', '清楚', 'qīngchu', ('clair', 'clear')),
        Z('mingbai', '明白', 'míngbai', ('comprendre ; clair', 'to understand; clear')),
        Z('liaojie', '了解', 'liǎojiě', ('bien connaître, se renseigner', 'to know well, to find out')),
        Z('jiandan', '简单', 'jiǎndān', ('simple', 'simple')),
        Z('rongyi', '容易', 'róngyì', ('facile', 'easy')),
        Z('nan', '难', 'nán', ('difficile', 'difficult')),
        Z('juzi', '句子', 'jùzi', ('phrase', 'sentence')),
        Z('cidian', '词典', 'cídiǎn', ('dictionnaire', 'dictionary')),
        Z('heiban', '黑板', 'hēibǎn', ('tableau noir', 'blackboard')),
        Z('jiang', '讲', 'jiǎng', ('expliquer, raconter', 'to explain, to tell')),
        Z('jiao-teach', '教', 'jiāo', ('enseigner', 'to teach')),
      ], [
        x('老师写在黑板上的字，你看得清楚吗？', 'Lǎoshī xiě zài hēibǎn shang de zì, nǐ kàn de qīngchu ma?', 'Tu arrives à lire les caractères que le maître écrit au tableau ?', 'Can you see the characters the teacher writes on the board clearly?'),
        x('这个句子太难了，我看不懂。', 'Zhè ge jùzi tài nán le, wǒ kàn bu dǒng.', 'Cette phrase est trop difficile, je ne la comprends pas.', 'This sentence is too hard; I can’t understand it.'),
      ], [
        FB(COMPLETE, '他说得太快了，我听不＿。', ['清楚', '容易', '简单'], '清楚', ('Ne pas entendre clairement : 听不清楚.', 'Can’t hear clearly: 听不清楚.'), ('Il parle trop vite, je n’entends pas bien.', 'He speaks too fast; I can’t hear clearly.')),
        FB(COMPLETE, '这本书很简单，我看＿懂。', ['得', '不', '了'], '得', ('Pouvoir comprendre : 看得懂.', 'Can understand: 看得懂.'), ('Ce livre est simple, je le comprends.', 'This book is simple; I can understand it.')),
        SO(ORDER('Cette question est facile, je peux y répondre.', 'This question is easy; I can answer it.'), ['这个', '问题', '很容易，', '我', '回答得了。'], ('Verbe + 得 + 了 = pouvoir le faire.', 'Verb + 得 + 了 = can do it.')),
        TF('我不明白这个字的意思。', ('La personne comprend ce caractère.', 'The speaker understands this character.'), FAUX, ('不明白 = ne pas comprendre.', '不明白 = not understand.')),
      ]),
  ]),
  CH('hsk3-w3-c2', ('La salle des rouleaux', 'The hall of scrolls'), [
    L('zh-library', ('À la bibliothèque : emprunter, se souvenir, oublier', 'At the library: borrowing, remembering, forgetting'), ('Emprunter un livre et parler du temps qui vient de passer.', 'Borrow a book and talk about the time that has just gone by.'), 9, [
        ('借 (jiè) = emprunter ou prêter : 我借了一本书 (j’ai emprunté) ; 借给你 (je te prête). On le fait au 图书馆 (bibliothèque).', '借 (jiè) = to borrow or to lend: 我借了一本书 (I borrowed); 借给你 (I lend it to you). You do this at the 图书馆 (library).'),
        ('记得 (jìde) = se souvenir ; 忘记 (wàngjì) = oublier : 别忘记带书. 检查 (jiǎnchá) = vérifier, examiner.', '记得 (jìde) = to remember; 忘记 (wàngjì) = to forget: 别忘记带书. 检查 (jiǎnchá) = to check, to examine.'),
        ('刚才 (gāngcái) = il y a un instant ; 一会儿 (yíhuìr) = un moment : 等一会儿 (attends un moment), 一会儿见 (à tout à l’heure).', '刚才 (gāngcái) = a moment ago; 一会儿 (yíhuìr) = a moment: 等一会儿 (wait a moment), 一会儿见 (see you in a bit).'),
      ], [
        Z('tushuguan', '图书馆', 'túshūguǎn', ('bibliothèque', 'library')),
        Z('jie', '借', 'jiè', ('emprunter, prêter', 'to borrow, to lend')),
        Z('bijiben', '笔记本', 'bǐjìběn', ('carnet ; ordinateur portable', 'notebook; laptop')),
        Z('xiaozhang', '校长', 'xiàozhǎng', ('directeur d’école', 'headmaster, principal')),
        Z('ban-class', '班', 'bān', ('classe (groupe d’élèves)', 'class (group of students)')),
        Z('jide', '记得', 'jìde', ('se souvenir', 'to remember')),
        Z('wangji', '忘记', 'wàngjì', ('oublier', 'to forget')),
        Z('jiancha', '检查', 'jiǎnchá', ('vérifier, examiner', 'to check, to examine')),
        Z('gangcai', '刚才', 'gāngcái', ('il y a un instant', 'a moment ago')),
        Z('yihuir', '一会儿', 'yíhuìr', ('un moment', 'a moment, a while')),
      ], [
        x('我刚才在图书馆借了两本历史书。', 'Wǒ gāngcái zài túshūguǎn jièle liǎng běn lìshǐ shū.', 'Je viens d’emprunter deux livres d’histoire à la bibliothèque.', 'I just borrowed two history books from the library.'),
        x('你还记得我们的校长吗？', 'Nǐ hái jìde wǒmen de xiàozhǎng ma?', 'Tu te souviens encore de notre directeur ?', 'Do you still remember our headmaster?'),
      ], [
        FB(COMPLETE, '我忘记带笔了，你能＿我一支吗？', ['借给', '借了', '还给'], '借给', ('Prêter à quelqu’un : 借给 + personne.', 'Lend to someone: 借给 + person.'), ('J’ai oublié mon stylo, tu peux m’en prêter un ?', 'I forgot my pen; can you lend me one?')),
        FB(COMPLETE, '考试以前，要再＿一下。', ['检查', '忘记', '记得'], '检查', ('Vérifier sa copie : 检查.', 'Check your paper: 检查.'), ('Avant de rendre, il faut encore vérifier.', 'Before handing in, you should check once more.')),
        DC(ANSWER, [('小李', '你什么时候去图书馆？')], ('Xiao Li te demande quand tu vas à la bibliothèque (dans un moment).', 'Xiao Li asks when you are going to the library (in a moment).'), ['一会儿就去。', '刚才就去。', '我忘记了图书馆。'], '一会儿就去。', ('Bientôt : 一会儿就….', 'Soon: 一会儿就….')),
        TF('他记得老师的名字。', ('Il a oublié le nom du maître.', 'He has forgotten the master’s name.'), FAUX, ('记得 = se souvenir.', '记得 = remember.')),
      ]),
  ])])

# ═════════════════════════ 4 : les monts de Zhuangzi — nature, saisons, récit ═════════════════════════
W4 = WORLD('hsk3-w4', ('Les monts de Zhuangzi', 'Zhuangzi’s mountains'), REGION,
  ('Saisons, vent, nuages et soleil ; plantes, animaux et paysages ; raconter dans l’ordre (先…然后, 后来, 终于) et indiquer la direction d’un mouvement (走上去, 跑回来).', 'Seasons, wind, clouds and sun; plants, animals and landscapes; telling events in order (先…然后, 后来, 终于) and showing the direction of a movement (走上去, 跑回来).'),
  (('Le géant Kuafu', 'The Giant Kuafu'), '夸', ('Kuafu, le géant qui voulut rattraper le soleil, court à travers les monts et assèche les rivières sur son passage. Raconte-lui les saisons et le chemin, pour qu’il s’arrête enfin.', 'Kuafu, the giant who tried to catch the sun, races through the mountains and drinks the rivers dry as he goes. Tell him about the seasons and the way, so that he finally stops.')),
  [CH('hsk3-w4-c1', ('Le papillon de Zhuangzi', 'Zhuangzi’s butterfly'), [
    HL('zh-hz-seasons', ('Les caractères des saisons : 春 夏 秋 冬 季 节 草 鸟', 'Season characters: 春 夏 秋 冬 季 节 草 鸟'), ('Reconnaître les caractères des saisons et de la nature.', 'Recognise the characters of the seasons and of nature.'), [
      ('春 (chūn) montrait des pousses sous le soleil 日 ; 秋 (qiū) réunit la céréale 禾 et le feu 火 : la saison où l’on brûle les chaumes après la moisson.', '春 (chūn) showed shoots under the sun 日; 秋 (qiū) joins grain 禾 and fire 火: the season when stubble is burnt after the harvest.'),
      ('草 (cǎo, herbe) et 节 (jié) portent la clé des plantes 艹 : 节 était le nœud du bambou, d’où « fête », « saison ».', '草 (cǎo, grass) and 节 (jié) carry the plant radical 艹: 节 was the joint of a bamboo stem, hence “festival” and “season”.'),
    ], [
      H('chun', '春', 'chūn', ('printemps', 'spring'), 9), H('xia-summer', '夏', 'xià', ('été', 'summer'), 10),
      H('qiu-autumn', '秋', 'qiū', ('automne', 'autumn'), 9), H('dong-winter', '冬', 'dōng', ('hiver', 'winter'), 5),
      H('ji-season', '季', 'jì', ('saison', 'season'), 8), H('jie', '节', 'jié', ('fête ; nœud', 'festival; joint'), 5),
      H('cao', '草', 'cǎo', ('herbe', 'grass'), 9), H('niao', '鸟', 'niǎo', ('oiseau', 'bird'), 5),
    ]),
    L('zh-seasons', ('Les quatre saisons : 春夏秋冬 et 越…越', 'The four seasons: 春夏秋冬 and 越…越'), ('Décrire les saisons et le temps qu’il fait.', 'Describe the seasons and the weather.'), 9, [
        ('春天、夏天、秋天、冬天 : les quatre 季节 (saisons). Le temps : 刮风 (il y a du vent), 云 (nuage), 太阳 (soleil), 月亮 (lune).', '春天, 夏天, 秋天, 冬天: the four 季节 (seasons). Weather: 刮风 (it’s windy), 云 (cloud), 太阳 (sun), 月亮 (moon).'),
        ('越 A 越 B = plus A, plus B : 雨越下越大 (la pluie tombe de plus en plus fort), 你越说我越不明白.', '越 A 越 B = the more A, the more B: 雨越下越大 (the rain gets heavier and heavier), 你越说我越不明白.'),
        ('变化 (biànhuà) = changement, changer : 天气变化很大.', '变化 (biànhuà) = change, to change: 天气变化很大.'),
      ], [
        ZG('yue-yue', '越 A 越 B', 'yuè… yuè…', ('plus…, plus…', 'the more…, the more…')),
        Z('chun', '春', 'chūn', ('printemps', 'spring')),
        Z('xia', '夏', 'xià', ('été', 'summer')),
        Z('qiu', '秋', 'qiū', ('automne', 'autumn')),
        Z('dong-winter', '冬', 'dōng', ('hiver', 'winter')),
        Z('jijie', '季节', 'jìjié', ('saison', 'season')),
        Z('guafeng', '刮风', 'guāfēng', ('faire du vent', 'to be windy')),
        Z('yun', '云', 'yún', ('nuage', 'cloud')),
        Z('taiyang', '太阳', 'tàiyáng', ('soleil', 'sun')),
        Z('yueliang', '月亮', 'yuèliang', ('lune', 'moon')),
        Z('bianhua', '变化', 'biànhuà', ('changement ; changer', 'change; to change')),
      ], [
        x('秋天是北京最好的季节，不冷也不热。', 'Qiūtiān shì Běijīng zuì hǎo de jìjié, bù lěng yě bú rè.', 'L’automne est la plus belle saison à Pékin : ni froid ni chaud.', 'Autumn is the best season in Beijing: neither cold nor hot.'),
        x('风越刮越大，太阳也看不见了。', 'Fēng yuè guā yuè dà, tàiyáng yě kàn bu jiàn le.', 'Le vent souffle de plus en plus fort, on ne voit même plus le soleil.', 'The wind is blowing harder and harder; you can’t even see the sun any more.'),
      ], [
        FB(COMPLETE, '一年有四个＿。', ['季节', '节日', '变化'], '季节', ('Les saisons : 季节.', 'Seasons: 季节.'), ('Une année a quatre saisons.', 'A year has four seasons.')),
        FB(COMPLETE, '他＿跑越快。', ['越', '又', '更'], '越', ('越 A 越 B.', '越 A 越 B.'), ('Il court de plus en plus vite.', 'He runs faster and faster.')),
        DC(ANSWER, [('朋友', '你最喜欢哪个季节？')], ('Un ami te demande ta saison préférée (le printemps, pour les fleurs).', 'A friend asks your favourite season (spring, for the flowers).'), ['春天，因为有很多花。', '月亮，因为很漂亮。', '刮风，因为很冷。'], '春天，因为有很多花。', ('Une saison : 春天.', 'A season: 春天.')),
        TF('今天晚上没有云，月亮很亮。', ('Ce soir, le ciel est couvert.', 'Tonight the sky is cloudy.'), FAUX, ('没有云 = pas de nuages.', '没有云 = no clouds.')),
      ]),
    L('zh-nature', ('Herbe, arbres et pandas : la nature et les directions', 'Grass, trees and pandas: nature and directions'), ('Décrire un paysage et dire dans quel sens on se déplace.', 'Describe a landscape and say which way you are moving.'), 10, [
        ('La nature : 草 (herbe), 树 (arbre), 花 (fleur ; aussi « dépenser »), 鸟 (oiseau), 动物 (animal), 马 (cheval), 熊猫 (panda), 河 (rivière) ; 黄河 = le fleuve Jaune.', 'Nature: 草 (grass), 树 (tree), 花 (flower; also “to spend”), 鸟 (bird), 动物 (animal), 马 (horse), 熊猫 (panda), 河 (river); 黄河 = the Yellow River.'),
        ('Direction du mouvement : verbe + 上 / 下 / 进 / 出 / 回 / 过 / 起 + 来 (vers moi) ou 去 (loin de moi) : 他跑上来了 (il est monté en courant jusqu’ici), 鸟飞过去了 (l’oiseau est passé en volant).', 'Direction of movement: verb + 上 / 下 / 进 / 出 / 回 / 过 / 起 + 来 (towards me) or 去 (away from me): 他跑上来了 (he ran up here), 鸟飞过去了 (the bird flew past).'),
        ('爬山 (páshān) = faire de la montagne ; 公园 (gōngyuán) = parc ; 环境 (huánjìng) = environnement.', '爬山 (páshān) = to climb mountains; 公园 (gōngyuán) = park; 环境 (huánjìng) = environment.'),
      ], [
        ZG('quxiang', '动词 + 上 / 下 / 进 / 出 / 回 / 过 / 起 + 来 / 去', 'lai / qu', ('direction du mouvement (vers moi / loin de moi)', 'direction of movement (towards / away from me)')),
        Z('cao', '草', 'cǎo', ('herbe', 'grass')),
        Z('shu', '树', 'shù', ('arbre', 'tree')),
        Z('hua', '花', 'huā', ('fleur ; dépenser', 'flower; to spend')),
        Z('niao', '鸟', 'niǎo', ('oiseau', 'bird')),
        Z('dongwu', '动物', 'dòngwù', ('animal', 'animal')),
        Z('ma', '马', 'mǎ', ('cheval', 'horse')),
        Z('xiongmao', '熊猫', 'xióngmāo', ('panda', 'panda')),
        Z('he', '河', 'hé', ('rivière, fleuve', 'river')),
        Z('huanghe', '黄河', 'Huáng Hé', ('le fleuve Jaune', 'the Yellow River')),
        Z('pashan', '爬山', 'páshān', ('faire de la montagne, grimper', 'to climb a mountain')),
        Z('gongyuan', '公园', 'gōngyuán', ('parc', 'park')),
        Z('huanjing', '环境', 'huánjìng', ('environnement', 'environment')),
      ], [
        x('周末我们去爬山吧，山上有很多树和鸟。', 'Zhōumò wǒmen qù páshān ba, shān shang yǒu hěn duō shù hé niǎo.', 'Ce week-end, allons en montagne : il y a plein d’arbres et d’oiseaux là-haut.', 'Let’s go hiking this weekend; there are lots of trees and birds up there.'),
        x('小狗从公园里跑出来了。', 'Xiǎo gǒu cóng gōngyuán li pǎo chūlai le.', 'Le petit chien est sorti du parc en courant.', 'The puppy came running out of the park.'),
      ], [
        FB(COMPLETE, '熊猫是中国最有名的＿。', ['动物', '环境', '公园'], '动物', ('Un animal : 动物.', 'An animal: 动物.'), ('Le panda est l’animal le plus célèbre de Chine.', 'The panda is China’s most famous animal.')),
        FB(COMPLETE, '他在楼上，你快走＿去吧。', ['上', '下', '出'], '上', ('Monter (loin de moi) : 走上去.', 'Go up (away from me): 走上去.'), ('Il est en haut, monte vite le rejoindre.', 'He’s upstairs; go up quickly.')),
        SO(ORDER('Le chat a couru dans la chambre.', 'The cat ran into the room.'), ['猫', '跑', '进', '房间', '去了。'], ('Verbe + 进 + lieu + 去.', 'Verb + 进 + place + 去.')),
        TF('这儿的环境很好，有很多树和花。', ('L’environnement est agréable.', 'The surroundings are pleasant.'), VRAI, ('环境很好 = environnement agréable.', '环境很好 = nice surroundings.')),
      ]),
  ]),
  CH('hsk3-w4-c2', ('La course du géant', 'The giant’s race'), [
    L('zh-time3', ('D’abord, ensuite, enfin : raconter une histoire', 'First, then, finally: telling a story'), ('Ordonner les événements d’un récit.', 'Put the events of a story in order.'), 10, [
        ('先 A，然后 B = d’abord A, ensuite B : 我们先吃饭，然后去看电影. 后来 (hòulái) = par la suite (seulement pour le passé) ; 最后 (zuìhòu) = à la fin.', '先 A，然后 B = first A, then B: 我们先吃饭，然后去看电影. 后来 (hòulái) = later on (only for the past); 最后 (zuìhòu) = in the end.'),
        ('突然 (tūrán) = soudain ; 终于 (zhōngyú) = enfin (après une longue attente) ; 一直 (yìzhí) = sans cesse, tout droit : 一直往前走.', '突然 (tūrán) = suddenly; 终于 (zhōngyú) = at last (after a long wait); 一直 (yìzhí) = all along, straight on: 一直往前走.'),
        ('以前 / 以后 = avant / après (ou autrefois / plus tard) : 吃饭以前洗手. 最近 (zuìjìn) = ces derniers temps ; 过去 (guòqù) = le passé, passer.', '以前 / 以后 = before / after (or in the past / later): 吃饭以前洗手. 最近 (zuìjìn) = lately; 过去 (guòqù) = the past, to go past.'),
      ], [
        ZG('xian-ranhou', '先…，然后…', 'xiān…, ránhòu…', ('d’abord…, ensuite…', 'first…, then…')),
        Z('xian', '先', 'xiān', ('d’abord', 'first (of all)')),
        Z('ranhou', '然后', 'ránhòu', ('ensuite, puis', 'then, afterwards')),
        Z('houlai', '后来', 'hòulái', ('par la suite (récit)', 'later on (in a story)')),
        Z('zuihou', '最后', 'zuìhòu', ('finalement, en dernier', 'finally, last')),
        Z('turan', '突然', 'tūrán', ('soudain, tout à coup', 'suddenly')),
        Z('zhongyu', '终于', 'zhōngyú', ('enfin', 'at last')),
        Z('yizhi', '一直', 'yìzhí', ('sans cesse ; tout droit', 'all along; straight on')),
        Z('yiqian', '以前', 'yǐqián', ('avant, autrefois', 'before, in the past')),
        Z('yihou', '以后', 'yǐhòu', ('après, plus tard', 'after, later')),
        Z('zuijin', '最近', 'zuìjìn', ('ces derniers temps', 'lately, recently')),
        Z('guoqu', '过去', 'guòqù', ('le passé ; passer', 'the past; to go past')),
      ], [
        x('夸父一直追太阳，后来他太渴了，最后死在了路上。', 'Kuāfù yìzhí zhuī tàiyáng, hòulái tā tài kě le, zuìhòu sǐ zài le lù shang.', 'Kuafu poursuivit sans cesse le soleil ; puis il eut trop soif, et mourut finalement en chemin.', 'Kuafu chased the sun without stopping; then he became too thirsty, and in the end he died on the way.'),
        x('等了一个小时，公共汽车终于来了。', 'Děngle yí ge xiǎoshí, gōnggòng qìchē zhōngyú lái le.', 'Après une heure d’attente, le bus est enfin arrivé.', 'After waiting an hour, the bus finally came.'),
      ], [
        FB(COMPLETE, '我们先去买票，＿进去看电影。', ['然后', '以前', '最近'], '然后', ('D’abord… ensuite : 先…然后.', 'First… then: 先…然后.'), ('On achète d’abord les billets, puis on entre voir le film.', 'First we buy tickets, then we go in to see the film.')),
        FB(COMPLETE, '找了很久，我＿找到了我的手机。', ['终于', '突然', '一直'], '终于', ('Après longtemps : 终于.', 'After a long time: 终于.'), ('Après avoir longtemps cherché, j’ai enfin retrouvé mon portable.', 'After searching for ages, I finally found my phone.')),
        FB(COMPLETE, '我们在说话，他＿哭了。', ['突然', '终于', '最后'], '突然', ('Sans prévenir : 突然.', 'Without warning: 突然.'), ('Nous parlions quand, soudain, il s’est mis à pleurer.', 'We were talking when he suddenly burst into tears.')),
        TF('他以前住在北京，后来搬到了上海。', ('Il habite toujours à Pékin.', 'He still lives in Beijing.'), FAUX, ('后来搬到了上海 = il a ensuite déménagé à Shanghai.', '后来搬到了上海 = he later moved to Shanghai.')),
      ]),
  ])])

# ═════════════════════════ 5 : le tribunal de Han Fei — devoir, 被, hypothèses ═════════════════════════
W5 = WORLD('hsk3-w5', ('Le tribunal de Han Fei', 'Han Fei’s court'), REGION,
  ('Ce qui arrive à quelqu’un (被), les émotions ; devoir, falloir, décider, être d’accord ; hypothèses avec 如果…就 et nuances (其实, 只, 或者).', 'What happens to someone (被), emotions; must, should, deciding, agreeing; hypotheses with 如果…就 and nuances (其实, 只, 或者).'),
  (('Le Xiezhi justicier', 'The Xiezhi of Justice'), '獬', ('Le Xiezhi, licorne noire des juges, frappe de sa corne celui qui ment. Au tribunal du légiste Han Fei, il te met à l’épreuve : dis exactement ce qui s’est passé, ce qu’il faut faire et à quelles conditions.', 'The Xiezhi, the judges’ black unicorn, strikes liars with its horn. At the legalist Han Fei’s court it puts you to the test: say exactly what happened, what must be done and on what conditions.')),
  [CH('hsk3-w5-c1', ('L’affaire du marché', 'The market case'), [
    HL('zh-hz-rules', ('Les caractères de la loi : 必 须 应 该 被 决 定 注', 'Characters of the law: 必 须 应 该 被 决 定 注'), ('Reconnaître les caractères du devoir et de la décision.', 'Recognise the characters of duty and decision.'), [
      ('应该 (yīnggāi) et 必须 (bìxū) disent ce qu’il faut faire : 必 (bì) est « sans faute », 须 (xū) portait autrefois la barbe 彡 du visage 页.', '应该 (yīnggāi) and 必须 (bìxū) say what must be done: 必 (bì) means “without fail”; 须 (xū) once showed the beard 彡 on a face 页.'),
      ('被 (bèi) porte la clé du vêtement 衤 : c’était la couverture qui « recouvre », d’où la voix passive, ce qu’on subit. 决定 (juédìng) : 决 ouvrir une digue, 定 fixer.', '被 (bèi) carries the clothing radical 衤: it was the blanket that “covers”, hence the passive, what you undergo. 决定 (juédìng): 决 to breach a dyke, 定 to fix.'),
    ], [
      H('bi-must', '必', 'bì', ('nécessairement', 'necessarily'), 5), H('xu', '须', 'xū', ('falloir', 'it is necessary'), 9),
      H('ying', '应', 'yīng', ('devoir, répondre', 'should, to respond'), 7), H('gai', '该', 'gāi', ('devoir, il faut', 'ought to'), 8),
      H('bei', '被', 'bèi', ('(marque le passif)', '(passive marker)'), 10), H('jue', '决', 'jué', ('décider, fixer', 'to decide'), 6),
      H('ding', '定', 'dìng', ('fixer, sûr', 'to fix, certain'), 8), H('zhu', '注', 'zhù', ('verser ; faire attention', 'to pour; to pay attention'), 8),
    ]),
    L('zh-bei', ('Mon vélo a été volé : la phrase passive avec 被', 'My bike was taken: the passive with 被'), ('Raconter ce qui est arrivé à quelqu’un ou à quelque chose.', 'Tell what happened to someone or something.'), 10, [
        ('Sujet + 被 (+ auteur) + verbe + suite : 我的蛋糕被弟弟吃了 (mon gâteau a été mangé par mon petit frère). Comme avec 把, le verbe ne reste pas seul.', 'Subject + 被 (+ doer) + verb + result: 我的蛋糕被弟弟吃了 (my cake was eaten by my little brother). As with 把, the verb is not left alone.'),
        ('被 sert surtout pour ce qu’on subit, souvent une mauvaise surprise : 杯子被打坏了 (la tasse a été cassée). 坏 (huài) = cassé, mauvais.', '被 is mostly used for things you suffer, often an unpleasant surprise: 杯子被打坏了 (the cup got broken). 坏 (huài) = broken, bad.'),
        ('Les émotions : 生气 (se fâcher), 害怕 (avoir peur), 担心 (s’inquiéter), 着急 (être pressé, inquiet), 难过 (être triste), 哭 (pleurer), 奇怪 (étrange).', 'Emotions: 生气 (to get angry), 害怕 (to be afraid), 担心 (to worry), 着急 (to be anxious, in a hurry), 难过 (to be sad), 哭 (to cry), 奇怪 (strange).'),
      ], [
        ZG('bei', '主语 + 被 (+ 人) + 动词 + 其他', 'bèi', ('être …é (par quelqu’un), phrase passive', 'to be …ed (by someone), passive sentence')),
        Z('bei', '被', 'bèi', ('(marque le passif)', '(passive marker)')),
        Z('huai', '坏', 'huài', ('cassé, mauvais', 'broken, bad')),
        Z('faxian', '发现', 'fāxiàn', ('découvrir, s’apercevoir', 'to discover, to notice')),
        Z('yudao', '遇到', 'yùdào', ('rencontrer (par hasard)', 'to run into, to meet by chance')),
        Z('ku', '哭', 'kū', ('pleurer', 'to cry')),
        Z('shengqi', '生气', 'shēngqì', ('se fâcher', 'to get angry')),
        Z('haipa', '害怕', 'hàipà', ('avoir peur', 'to be afraid')),
        Z('danxin', '担心', 'dānxīn', ('s’inquiéter', 'to worry')),
        Z('zhaoji', '着急', 'zháojí', ('inquiet, pressé', 'anxious, in a hurry')),
        Z('nanguo', '难过', 'nánguò', ('triste', 'sad')),
        Z('qiguai', '奇怪', 'qíguài', ('étrange', 'strange')),
      ], [
        x('我的自行车被人骑走了，我很着急。', 'Wǒ de zìxíngchē bèi rén qízǒu le, wǒ hěn zháojí.', 'Quelqu’un est parti avec mon vélo, je suis très inquiet.', 'Someone rode off with my bike; I’m really worried.'),
        x('妈妈发现杯子被打坏了，可是她没有生气。', 'Māma fāxiàn bēizi bèi dǎhuài le, kěshì tā méiyǒu shēngqì.', 'Maman a vu que la tasse était cassée, mais elle ne s’est pas fâchée.', 'Mum saw the cup had been broken, but she didn’t get angry.'),
      ], [
        FB(COMPLETE, '我的蛋糕＿弟弟吃完了。', ['被', '把', '给'], '被', ('Ce qu’on subit : 被 + auteur + verbe.', 'What you suffer: 被 + doer + verb.'), ('Mon gâteau a été entièrement mangé par mon petit frère.', 'My cake was all eaten by my little brother.')),
        FB(COMPLETE, '别＿，医生说没问题。', ['担心', '奇怪', '发现'], '担心', ('Ne t’inquiète pas : 别担心.', 'Don’t worry: 别担心.'), ('Ne t’inquiète pas, le médecin dit que tout va bien.', 'Don’t worry, the doctor says it’s fine.')),
        SO(ORDER('Mon portable a été cassé par le chat.', 'My phone was broken by the cat.'), ['我的', '手机', '被', '猫', '弄坏了。'], ('Sujet + 被 + auteur + verbe + résultat.', 'Subject + 被 + doer + verb + result.')),
        TF('昨天我在路上遇到了我的老师。', ('La rencontre était prévue.', 'The meeting was planned.'), FAUX, ('遇到 = rencontrer par hasard.', '遇到 = to run into.')),
      ]),
    L('zh-must', ('Il faut, tu devrais, je veux bien : 必须、应该、愿意', 'You must, you should, I’m willing: 必须, 应该, 愿意'), ('Exprimer l’obligation, le conseil, l’accord et la décision.', 'Express obligation, advice, agreement and decision.'), 10, [
        ('必须 (bìxū) = il faut absolument ; 应该 (yīnggāi) = on devrait ; 需要 (xūyào) = avoir besoin de. La négation de 必须 est 不用 (pas la peine) : 你不用来.', '必须 (bìxū) = absolutely must; 应该 (yīnggāi) = should; 需要 (xūyào) = to need. The negative of 必须 is 不用 (no need): 你不用来.'),
        ('一定 (yídìng) = sans faute, certainement : 我一定来. 注意 (zhùyì) = faire attention ; 小心 (xiǎoxīn) = attention !, prudent.', '一定 (yídìng) = for sure, without fail: 我一定来. 注意 (zhùyì) = to pay attention; 小心 (xiǎoxīn) = careful!, be careful.'),
        ('决定 (juédìng) = décider ; 同意 (tóngyì) = être d’accord ; 相信 (xiāngxìn) = croire, faire confiance ; 满意 (mǎnyì) = satisfait ; 愿意 (yuànyì) = vouloir bien ; 要求 (yāoqiú) = exiger, exigence.', '决定 (juédìng) = to decide; 同意 (tóngyì) = to agree; 相信 (xiāngxìn) = to believe, to trust; 满意 (mǎnyì) = satisfied; 愿意 (yuànyì) = to be willing; 要求 (yāoqiú) = to require, requirement.'),
      ], [
        Z('bixu', '必须', 'bìxū', ('devoir absolument', 'must')),
        Z('yinggai', '应该', 'yīnggāi', ('devoir (il faudrait)', 'should, ought to')),
        Z('xuyao', '需要', 'xūyào', ('avoir besoin de', 'to need')),
        Z('yiding', '一定', 'yídìng', ('certainement, sans faute', 'certainly, without fail')),
        Z('zhuyi', '注意', 'zhùyì', ('faire attention', 'to pay attention')),
        Z('xiaoxin', '小心', 'xiǎoxīn', ('prudent ; attention !', 'careful; look out!')),
        Z('jueding', '决定', 'juédìng', ('décider ; décision', 'to decide; decision')),
        Z('yaoqiu', '要求', 'yāoqiú', ('exiger ; exigence', 'to require; requirement')),
        Z('tongyi', '同意', 'tóngyì', ('être d’accord ; accepter', 'to agree')),
        Z('xiangxin', '相信', 'xiāngxìn', ('croire, faire confiance', 'to believe, to trust')),
        Z('manyi', '满意', 'mǎnyì', ('satisfait', 'satisfied')),
        Z('yuanyi', '愿意', 'yuànyì', ('vouloir bien', 'to be willing')),
      ], [
        x('明天考试，你今天晚上必须早点儿睡觉。', 'Míngtiān kǎoshì, nǐ jīntiān wǎnshang bìxū zǎo diǎnr shuìjiào.', 'Tu as un examen demain, tu dois absolument te coucher tôt ce soir.', 'You have an exam tomorrow; you must go to bed early tonight.'),
        x('法官决定相信他，大家都同意。', 'Fǎguān juédìng xiāngxìn tā, dàjiā dōu tóngyì.', 'Le juge a décidé de le croire, et tout le monde était d’accord.', 'The judge decided to believe him, and everyone agreed.'),
      ], [
        FB(COMPLETE, '过马路的时候要＿车。', ['注意', '同意', '满意'], '注意', ('Faire attention à : 注意.', 'Watch out for: 注意.'), ('En traversant la rue, il faut faire attention aux voitures.', 'When crossing the road you must watch out for cars.')),
        FB(COMPLETE, '你明天＿要来，我等你。', ['一定', '一样', '一共'], '一定', ('Sans faute : 一定.', 'Without fail: 一定.'), ('Viens sans faute demain, je t’attends.', 'Be sure to come tomorrow; I’ll be waiting.')),
        DC(ANSWER, [('经理', '你愿意去北京工作吗？')], ('Le directeur te demande si tu veux bien travailler à Pékin (oui, volontiers).', 'The manager asks if you are willing to work in Beijing (yes, gladly).'), ['我很愿意。', '我很满意。', '我很小心。'], '我很愿意。', ('Vouloir bien : 愿意.', 'Be willing: 愿意.')),
        TF('老师对他的作业很满意。', ('Le maître n’est pas content de ses devoirs.', 'The master is unhappy with his homework.'), FAUX, ('很满意 = très satisfait.', '很满意 = very satisfied.')),
      ]),
  ]),
  CH('hsk3-w5-c2', ('Le jugement', 'The verdict'), [
    L('zh-ruguo', ('Si… alors : 如果…就, 其实, 只, 或者', 'If… then: 如果…就, 其实, 只, 或者'), ('Poser une condition, nuancer et proposer une solution.', 'Set a condition, qualify and suggest a solution.'), 10, [
        ('如果 A（的话），（主语）就 B = si A, alors B : 如果明天下雨，我们就不去了. 就 se place après le sujet de la seconde partie.', '如果 A（的话），(subject) 就 B = if A, then B: 如果明天下雨，我们就不去了. 就 goes after the subject of the second half.'),
        ('或者 (huòzhě) = ou, dans une affirmation : 星期六或者星期天都可以. Pour une question, on garde 还是. 只 (zhǐ) = seulement : 我只有十块钱.', '或者 (huòzhě) = or, in a statement: 星期六或者星期天都可以. In a question, use 还是. 只 (zhǐ) = only: 我只有十块钱.'),
        ('其实 (qíshí) = en fait ; 当然 (dāngrán) = bien sûr ; 办法 (bànfǎ) = moyen, solution ; 解决 (jiějué) = résoudre ; 影响 (yǐngxiǎng) = influencer ; 根据 (gēnjù) = d’après.', '其实 (qíshí) = actually; 当然 (dāngrán) = of course; 办法 (bànfǎ) = way, solution; 解决 (jiějué) = to solve; 影响 (yǐngxiǎng) = to affect; 根据 (gēnjù) = according to.'),
      ], [
        ZG('ruguo-jiu', '如果…（的话），就…', 'rúguǒ… (dehuà), jiù…', ('si…, alors…', 'if…, then…')),
        Z('ruguo', '如果', 'rúguǒ', ('si', 'if')),
        Z('huozhe', '或者', 'huòzhě', ('ou (affirmation)', 'or (in a statement)')),
        Z('zhi-only', '只', 'zhǐ', ('seulement', 'only')),
        Z('qishi', '其实', 'qíshí', ('en fait', 'actually')),
        Z('dangran', '当然', 'dāngrán', ('bien sûr', 'of course')),
        Z('banfa', '办法', 'bànfǎ', ('moyen, solution', 'way, method')),
        Z('jiejue', '解决', 'jiějué', ('résoudre', 'to solve')),
        Z('yingxiang', '影响', 'yǐngxiǎng', ('influencer ; influence', 'to affect; influence')),
        Z('guanxi', '关系', 'guānxi', ('relation, rapport', 'relationship')),
        Z('genju', '根据', 'gēnjù', ('d’après, selon', 'according to')),
      ], [
        x('如果你有问题，就来办公室找我。', 'Rúguǒ nǐ yǒu wèntí, jiù lái bàngōngshì zhǎo wǒ.', 'Si tu as une question, viens me voir au bureau.', 'If you have a question, come and find me in the office.'),
        x('其实这个问题很简单，只有一个办法。', 'Qíshí zhè ge wèntí hěn jiǎndān, zhǐ yǒu yí ge bànfǎ.', 'En fait, ce problème est simple : il n’y a qu’une solution.', 'Actually this problem is simple; there’s only one solution.'),
      ], [
        FB(COMPLETE, '如果你累了，＿休息一下吧。', ['就', '才', '还'], '就', ('如果…就….', '如果…就….'), ('Si tu es fatigué, repose-toi un peu.', 'If you’re tired, have a rest.')),
        FB(COMPLETE, '你可以坐地铁＿坐出租车。', ['或者', '还是', '但是'], '或者', ('« Ou » dans une affirmation : 或者.', '“Or” in a statement: 或者.'), ('Tu peux prendre le métro ou un taxi.', 'You can take the underground or a taxi.')),
        DC(ANSWER, [('朋友', '你能帮我吗？')], ('Un ami te demande de l’aide (bien sûr).', 'A friend asks for your help (of course).'), ['当然可以！', '其实不是。', '只有一个。'], '当然可以！', ('Bien sûr : 当然.', 'Of course: 当然.')),
        TF('下雨对比赛没有影响。', ('La pluie gêne le match.', 'The rain affects the match.'), FAUX, ('没有影响 = aucune influence.', '没有影响 = no effect.')),
      ]),
  ])])

# ═════════════════════════ 6 : la route du Sud — transports, ville, fréquence ═════════════════════════
W6 = WORLD('hsk3-w6', ('La route du Sud', 'The road south'), REGION,
  ('Métro, bateau, vélo et passeport ; s’orienter en ville (东西南北, 附近, 中间) ; dire quand (一…就, 才) et combien de fois (经常, 总是, 一般).', 'Underground, boat, bike and passport; finding your way in town (东西南北, 附近, 中间); saying when (一…就, 才) and how often (经常, 总是, 一般).'),
  (('Le Hou dévoreur de dragons', 'The Dragon-Eating Hou'), '犼', ('Le Hou, bête au poil de flamme qui dévore les dragons, a pris position au carrefour des routes du Sud. Pour passer, indique-lui chaque direction et chaque horaire sans te tromper.', 'The Hou, a flame-furred beast that devours dragons, has taken up position at the crossroads of the southern roads. To get past, give it every direction and every timetable without a mistake.')),
  [CH('hsk3-w6-c1', ('Le départ', 'Setting off'), [
    HL('zh-hz-travel', ('Les caractères du voyage : 船 骑 城 市 街 图 北 南', 'Travel characters: 船 骑 城 市 街 图 北 南'), ('Reconnaître les caractères du voyage et de la ville.', 'Recognise the characters of travel and of the town.'), [
      ('船 (chuán, bateau) porte la clé du bateau 舟 ; 骑 (qí, monter) celle du cheval 马 : on monte un cheval avant de monter un vélo.', '船 (chuán, boat) carries the boat radical 舟; 骑 (qí, to ride) the horse radical 马: people rode horses long before bicycles.'),
      ('城 (chéng) est un rempart de terre 土 : 城市 = la ville fortifiée et son marché 市. 北 (běi) montre deux hommes dos à dos : le nord est le côté où l’on tourne le dos au soleil.', '城 (chéng) is an earth 土 rampart: 城市 = the walled town and its market 市. 北 (běi) shows two people back to back: north is the side where you turn your back to the sun.'),
    ], [
      H('chuan', '船', 'chuán', ('bateau', 'boat'), 11), H('qi-ride', '骑', 'qí', ('monter (à vélo, à cheval)', 'to ride'), 11),
      H('cheng', '城', 'chéng', ('ville, remparts', 'city walls, town'), 9), H('shi-market', '市', 'shì', ('marché, ville', 'market, city'), 5),
      H('jie-street', '街', 'jiē', ('rue', 'street'), 12), H('tu', '图', 'tú', ('dessin, plan', 'drawing, map'), 8),
      H('bei-north', '北', 'běi', ('nord', 'north'), 5), H('nan-south', '南', 'nán', ('sud', 'south'), 9),
    ]),
    L('zh-transport', ('Métro, bateau, vélo : voyager et 一…就', 'Underground, boat, bike: travelling and 一…就'), ('Choisir son moyen de transport et enchaîner deux actions.', 'Choose how to travel and link two actions.'), 10, [
        ('坐 se dit pour ce où l’on s’assoit : 坐地铁 (métro), 坐船 (bateau) ; 骑 (qí) pour ce qu’on enfourche : 骑自行车 (vélo), 骑马 (cheval).', '坐 is for what you sit in: 坐地铁 (underground), 坐船 (boat); 骑 (qí) for what you straddle: 骑自行车 (bike), 骑马 (horse).'),
        ('一 A 就 B = dès que A, B : 我一到北京就给你打电话 (dès que j’arrive à Pékin, je t’appelle).', '一 A 就 B = as soon as A, B: 我一到北京就给你打电话 (as soon as I get to Beijing, I’ll call you).'),
        ('Au départ : 护照 (passeport), 行李箱 (valise), 起飞 (décoller), 司机 (chauffeur), 站 (arrêt, station), 迟到 (être en retard).', 'Setting off: 护照 (passport), 行李箱 (suitcase), 起飞 (to take off), 司机 (driver), 站 (stop, station), 迟到 (to be late).'),
      ], [
        ZG('yi-jiu', '一…就…', 'yī… jiù…', ('dès que…', 'as soon as…')),
        Z('ditie', '地铁', 'dìtiě', ('métro', 'underground, subway')),
        Z('chuan', '船', 'chuán', ('bateau', 'boat')),
        Z('qi', '骑', 'qí', ('monter (à vélo, à cheval)', 'to ride')),
        Z('zixingche', '自行车', 'zìxíngchē', ('vélo', 'bicycle')),
        Z('siji', '司机', 'sījī', ('chauffeur', 'driver')),
        Z('huzhao', '护照', 'hùzhào', ('passeport', 'passport')),
        Z('xinglixiang', '行李箱', 'xínglixiāng', ('valise', 'suitcase')),
        Z('qifei', '起飞', 'qǐfēi', ('décoller', 'to take off')),
        Z('chidao', '迟到', 'chídào', ('être en retard', 'to be late')),
        Z('zhan', '站', 'zhàn', ('station, arrêt ; se tenir debout', 'station, stop; to stand')),
      ], [
        x('飞机一起飞，他就睡着了。', 'Fēijī yì qǐfēi, tā jiù shuìzháo le.', 'Dès que l’avion a décollé, il s’est endormi.', 'As soon as the plane took off, he fell asleep.'),
        x('我每天骑自行车去地铁站。', 'Wǒ měi tiān qí zìxíngchē qù dìtiězhàn.', 'Chaque jour, je vais à la station de métro à vélo.', 'Every day I ride my bike to the underground station.'),
      ], [
        FB(COMPLETE, '他每天＿自行车上班。', ['骑', '坐', '开'], '骑', ('Un vélo s’enfourche : 骑.', 'You ride a bike: 骑.'), ('Il va au travail à vélo tous les jours.', 'He cycles to work every day.')),
        FB(COMPLETE, '我一下课＿去图书馆。', ['就', '才', '再'], '就', ('一…就… = dès que.', '一…就… = as soon as.'), ('Dès la fin du cours, je vais à la bibliothèque.', 'As soon as class ends, I go to the library.')),
        DC(ANSWER, [('机场工作人员', '请给我看一下您的护照。')], ('Au contrôle, on te demande ton passeport.', 'At the desk you are asked for your passport.'), ['好的，给您。', '我迟到了。', '飞机起飞了。'], '好的，给您。', ('Tendre quelque chose : 给您.', 'Hand something over: 给您.')),
        TF('快点儿，我们要迟到了！', ('Ils ont tout leur temps.', 'They have plenty of time.'), FAUX, ('要迟到了 = être sur le point d’être en retard.', '要迟到了 = about to be late.')),
      ]),
    L('zh-city', ('Nord, sud, à côté, au milieu : s’orienter en ville', 'North, south, nearby, in the middle: finding your way in town'), ('Situer un lieu et dire par où l’on passe.', 'Locate a place and say which way you go.'), 9, [
        ('Les points cardinaux : 东 (est), 西 (ouest), 南 (sud), 北 (nord). On dit 东边 (côté est), 北方 (le nord du pays) ; 东南 = sud-est (l’est d’abord !).', 'The points of the compass: 东 (east), 西 (west), 南 (south), 北 (north). You say 东边 (east side), 北方 (the north of the country); 东南 = south-east (east first!).'),
        ('附近 (fùjìn) = à proximité ; 中间 (zhōngjiān) = au milieu, entre : 银行和超市中间. 向 (xiàng) + direction = vers : 向东走.', '附近 (fùjìn) = nearby; 中间 (zhōngjiān) = in the middle, between: 银行和超市中间. 向 (xiàng) + direction = towards: 向东走.'),
        ('经过 (jīngguò) = passer par ; 离开 (líkāi) = quitter ; 地图 (dìtú) = carte, plan ; 街道 (jiēdào) = rue.', '经过 (jīngguò) = to pass through; 离开 (líkāi) = to leave; 地图 (dìtú) = map; 街道 (jiēdào) = street.'),
      ], [
        Z('dong-east', '东', 'dōng', ('est', 'east')),
        Z('xi-west', '西', 'xī', ('ouest', 'west')),
        Z('nan-south', '南', 'nán', ('sud', 'south')),
        Z('beifang', '北方', 'běifāng', ('le nord (région)', 'the north (region)')),
        Z('xiang-towards', '向', 'xiàng', ('vers, en direction de', 'towards')),
        Z('fujin', '附近', 'fùjìn', ('à proximité', 'nearby')),
        Z('zhongjian', '中间', 'zhōngjiān', ('au milieu, entre', 'in the middle, between')),
        Z('chengshi', '城市', 'chéngshì', ('ville', 'city')),
        Z('jiedao', '街道', 'jiēdào', ('rue', 'street')),
        Z('ditu', '地图', 'dìtú', ('carte, plan', 'map')),
        Z('difang', '地方', 'dìfang', ('endroit, lieu', 'place')),
        Z('yinhang', '银行', 'yínháng', ('banque', 'bank')),
        Z('jingguo', '经过', 'jīngguò', ('passer par', 'to pass through')),
        Z('likai', '离开', 'líkāi', ('partir, quitter', 'to leave')),
        Z('guojia', '国家', 'guójiā', ('pays', 'country')),
        Z('shijie', '世界', 'shìjiè', ('monde', 'world')),
      ], [
        x('我家附近有一个银行，在超市和公园中间。', 'Wǒ jiā fùjìn yǒu yí ge yínháng, zài chāoshì hé gōngyuán zhōngjiān.', 'Près de chez moi, il y a une banque, entre le supermarché et le parc.', 'Near my home there’s a bank, between the supermarket and the park.'),
        x('一直向南走，经过两条街道就到了。', 'Yìzhí xiàng nán zǒu, jīngguò liǎng tiáo jiēdào jiù dào le.', 'Va tout droit vers le sud : deux rues plus loin, tu y es.', 'Go straight on southwards; two streets later you’re there.'),
      ], [
        FB(COMPLETE, '你看看＿，我们现在在哪儿？', ['地图', '地方', '城市'], '地图', ('Pour s’orienter : 地图.', 'To find your way: 地图.'), ('Regarde le plan : où sommes-nous maintenant ?', 'Look at the map: where are we now?')),
        FB(COMPLETE, '这个＿太漂亮了，我不想离开。', ['地方', '中间', '附近'], '地方', ('Un endroit : 地方.', 'A place: 地方.'), ('Cet endroit est si beau que je ne veux pas partir.', 'This place is so beautiful I don’t want to leave.')),
        SO(ORDER('Il y a un hôtel près de la gare.', 'There is a hotel near the station.'), ['火车站', '附近', '有', '一个', '宾馆。'], ('Lieu + 有 + chose.', 'Place + 有 + thing.')),
        TF('中国是世界上人最多的国家之一。', ('La Chine est l’un des pays les plus peuplés.', 'China is one of the most populous countries.'), VRAI, ('人最多的国家之一 = l’un des pays les plus peuplés.', '人最多的国家之一 = one of the most populous countries.')),
      ]),
  ]),
  CH('hsk3-w6-c2', ('Les horaires des relais', 'The post-station timetables'), [
    L('zh-cai', ('Tôt ou tard : 就 et 才 ; souvent, toujours, en général', 'Early or late: 就 and 才; often, always, usually'), ('Dire si quelque chose arrive tôt ou tard, et à quelle fréquence.', 'Say whether something happens early or late, and how often.'), 10, [
        ('就 = déjà, tôt, facilement : 他七点就来了 (il était là dès sept heures). 才 = seulement alors, tard, difficilement : 他十点才来 (il n’est arrivé qu’à dix heures). Avec 才, pas de 了.', '就 = already, early, easily: 他七点就来了 (he was here as early as seven). 才 = only then, late, with difficulty: 他十点才来 (he didn’t come until ten). With 才, no 了.'),
        ('Fréquence : 经常 (souvent), 总是 (toujours), 一般 (en général), 几乎 (presque). 久 (jiǔ) = longtemps : 好久不见 !', 'Frequency: 经常 (often), 总是 (always), 一般 (usually), 几乎 (almost). 久 (jiǔ) = a long time: 好久不见!'),
        ('L’heure : 半 (demi), 刻 (quart), 差 (moins) : 八点一刻 (8 h 15), 差五分九点 (9 h moins 5). 周末 = week-end ; 打算 = avoir l’intention de.', 'Telling the time: 半 (half), 刻 (quarter), 差 (to, minus): 八点一刻 (8:15), 差五分九点 (five to nine). 周末 = weekend; 打算 = to plan to.'),
      ], [
        ZG('cai-jiu', '时间 + 就…了 / 才…', 'jiù / cái', ('tôt (就) ou tard (才)', 'early (就) or late (才)')),
        Z('cai', '才', 'cái', ('seulement alors, pas avant', 'only then, not until')),
        Z('jingchang', '经常', 'jīngcháng', ('souvent', 'often')),
        Z('zongshi', '总是', 'zǒngshì', ('toujours', 'always')),
        Z('yiban', '一般', 'yìbān', ('en général ; ordinaire', 'usually; ordinary')),
        Z('jihu', '几乎', 'jīhū', ('presque', 'almost')),
        Z('jiu-long', '久', 'jiǔ', ('longtemps', 'a long time')),
        Z('ban-half', '半', 'bàn', ('la moitié', 'half')),
        Z('ke-quarter', '刻', 'kè', ('quart d’heure', 'quarter of an hour')),
        Z('cha', '差', 'chà', ('manquer ; moins (heure) ; mauvais', 'to lack; to (time); poor')),
        Z('zhoumo', '周末', 'zhōumò', ('week-end', 'weekend')),
        Z('dasuan', '打算', 'dǎsuàn', ('avoir l’intention de', 'to plan to')),
      ], [
        x('火车八点半开，他八点就到车站了。', 'Huǒchē bā diǎn bàn kāi, tā bā diǎn jiù dào chēzhàn le.', 'Le train partait à huit heures et demie ; il était à la gare dès huit heures.', 'The train left at half past eight; he was at the station by eight.'),
        x('我周末一般在家休息，几乎不出门。', 'Wǒ zhōumò yìbān zài jiā xiūxi, jīhū bù chūmén.', 'Le week-end, je me repose en général chez moi, je ne sors presque pas.', 'At weekends I usually rest at home and hardly ever go out.'),
      ], [
        FB(COMPLETE, '会议九点开始，他十点＿来。', ['才', '就', '再'], '才', ('En retard : 才 (sans 了).', 'Late: 才 (no 了).'), ('La réunion commençait à neuf heures ; il n’est arrivé qu’à dix heures.', 'The meeting started at nine; he didn’t come until ten.')),
        FB(COMPLETE, '他＿迟到，老师很生气。', ['总是', '一共', '刚才'], '总是', ('Toujours : 总是.', 'Always: 总是.'), ('Il est toujours en retard, le maître est fâché.', 'He’s always late; the teacher is angry.')),
        DC(ANSWER, [('同事', '周末你打算做什么？')], ('Un collègue te demande tes projets du week-end (aller nager).', 'A colleague asks your weekend plans (going swimming).'), ['我打算去游泳。', '我经常迟到。', '现在差五分九点。'], '我打算去游泳。', ('Projet : 打算 + verbe.', 'Plan: 打算 + verb.')),
        TF('现在八点一刻。', ('Il est huit heures et quart.', 'It is a quarter past eight.'), VRAI, ('一刻 = un quart d’heure.', '一刻 = a quarter of an hour.')),
      ]),
  ])])

# ═════════════════════════ 7 : le sanctuaire de Bian Que — corps, santé, apparence ═════════════════════════
W7 = WORLD('hsk3-w7', ('Le sanctuaire de Bian Que', 'Bian Que’s sanctuary'), REGION,
  ('Le corps, la fièvre et le rhume, garder la santé (极了) ; l’apparence, les vêtements et les classificateurs (双, 条, 种, 辆) ; s’exclamer avec 多么.', 'The body, fever and colds, staying healthy (极了); appearance, clothes and measure words (双, 条, 种, 辆); exclaiming with 多么.'),
  (('Le dragon ailé Yinglong', 'Yinglong the Winged Dragon'), '应', ('Yinglong, le dragon ailé des pluies, a déchaîné l’orage sur le sanctuaire du médecin Bian Que : les pèlerins tombent malades. Dis où ils ont mal et aide-les à se rétablir.', 'Yinglong, the winged dragon of rain, has unleashed a storm on the sanctuary of the physician Bian Que: the pilgrims are falling ill. Say where it hurts and help them recover.')),
  [CH('hsk3-w7-c1', ('Le médecin Bian Que', 'Bian Que the physician'), [
    HL('zh-hz-body', ('Les caractères du corps : 头 脸 脚 腿 疼 健 康 鞋', 'Body characters: 头 脸 脚 腿 疼 健 康 鞋'), ('Reconnaître les caractères du corps et de la santé.', 'Recognise the characters of the body and of health.'), [
      ('脸 (liǎn, visage), 脚 (jiǎo, pied) et 腿 (tuǐ, jambe) portent la clé de la chair 月 : sous cette forme, ce n’est pas la lune mais 肉, la viande.', '脸 (liǎn, face), 脚 (jiǎo, foot) and 腿 (tuǐ, leg) carry the flesh radical 月: in this position it is not the moon but 肉, meat.'),
      ('疼 (téng, avoir mal) porte la clé de la maladie 疒 au-dessus de 冬 (l’hiver) : une douleur qui gèle. 鞋 (xié, chaussure) porte celle du cuir 革.', '疼 (téng, to hurt) carries the illness radical 疒 over 冬 (winter): a freezing pain. 鞋 (xié, shoe) carries the leather radical 革.'),
    ], [
      H('tou', '头', 'tóu', ('tête', 'head'), 5), H('lian-face', '脸', 'liǎn', ('visage', 'face'), 11),
      H('jiao-foot', '脚', 'jiǎo', ('pied', 'foot'), 11), H('tui', '腿', 'tuǐ', ('jambe', 'leg'), 13),
      H('teng', '疼', 'téng', ('faire mal', 'to hurt'), 10), H('jian', '健', 'jiàn', ('vigoureux', 'vigorous'), 10),
      H('kang', '康', 'kāng', ('en paix, sain', 'healthy, peaceful'), 11), H('xie', '鞋', 'xié', ('chaussure', 'shoe'), 15),
    ]),
    L('zh-body', ('J’ai mal à la tête : le corps et la santé', 'My head hurts: the body and health'), ('Dire où l’on a mal et parler de sa santé.', 'Say where it hurts and talk about your health.'), 10, [
        ('Le corps : 头 (tête) et 头发 (cheveux), 脸 (visage), 鼻子 (nez), 耳朵 (oreille), 腿 (jambe), 脚 (pied). Partie du corps + 疼 = avoir mal à : 我头疼.', 'The body: 头 (head) and 头发 (hair), 脸 (face), 鼻子 (nose), 耳朵 (ear), 腿 (leg), 脚 (foot). Body part + 疼 = to hurt: 我头疼.'),
        ('发烧 (fāshāo) = avoir de la fièvre ; 感冒 (gǎnmào) = rhume, s’enrhumer. 健康 (jiànkāng) = en bonne santé ; 锻炼 (duànliàn) = faire de l’exercice ; 舒服 (shūfu) = se sentir bien.', '发烧 (fāshāo) = to have a fever; 感冒 (gǎnmào) = a cold, to catch a cold. 健康 (jiànkāng) = healthy; 锻炼 (duànliàn) = to exercise; 舒服 (shūfu) = to feel well.'),
        ('Adjectif + 极了 = extrêmement : 好极了 (excellent !), 累极了 (épuisé).', 'Adjective + 极了 = extremely: 好极了 (excellent!), 累极了 (exhausted).'),
      ], [
        ZG('jile', '形容词 + 极了', 'jí le', ('extrêmement', 'extremely')),
        Z('tou', '头', 'tóu', ('tête', 'head')),
        Z('toufa', '头发', 'tóufa', ('cheveux', 'hair')),
        Z('lian', '脸', 'liǎn', ('visage', 'face')),
        Z('bizi', '鼻子', 'bízi', ('nez', 'nose')),
        Z('erduo', '耳朵', 'ěrduo', ('oreille', 'ear')),
        Z('tui', '腿', 'tuǐ', ('jambe', 'leg')),
        Z('jiao-foot', '脚', 'jiǎo', ('pied', 'foot')),
        Z('teng', '疼', 'téng', ('faire mal', 'to hurt')),
        Z('fashao', '发烧', 'fāshāo', ('avoir de la fièvre', 'to have a fever')),
        Z('ganmao', '感冒', 'gǎnmào', ('rhume ; s’enrhumer', 'a cold; to catch a cold')),
        Z('jiankang', '健康', 'jiànkāng', ('en bonne santé ; santé', 'healthy; health')),
        Z('duanlian', '锻炼', 'duànliàn', ('faire du sport', 'to exercise')),
        Z('shufu', '舒服', 'shūfu', ('à l’aise, bien', 'comfortable, well')),
      ], [
        x('我感冒了，头疼，还有点儿发烧。', 'Wǒ gǎnmào le, tóu téng, hái yǒudiǎnr fāshāo.', 'J’ai attrapé un rhume : j’ai mal à la tête et un peu de fièvre.', 'I’ve caught a cold: my head hurts and I’ve got a slight fever.'),
        x('爷爷每天早上锻炼，身体健康极了。', 'Yéye měi tiān zǎoshang duànliàn, shēntǐ jiànkāng jí le.', 'Grand-père fait de l’exercice tous les matins, il est en pleine forme.', 'Grandpa exercises every morning; he’s in excellent health.'),
      ], [
        FB(COMPLETE, '我走了三个小时，脚＿极了。', ['疼', '舒服', '健康'], '疼', ('Avoir mal : 疼.', 'To hurt: 疼.'), ('J’ai marché trois heures, j’ai terriblement mal aux pieds.', 'I walked for three hours; my feet are killing me.')),
        FB(COMPLETE, '你脸很红，是不是＿了？', ['发烧', '锻炼', '洗澡'], '发烧', ('Un visage rouge : la fièvre, 发烧.', 'A red face: fever, 发烧.'), ('Tu as le visage tout rouge, tu as de la fièvre ?', 'Your face is very red; have you got a fever?')),
        DC(ANSWER, [('医生', '你哪儿不舒服？')], ('Le médecin te demande ce qui ne va pas (tu as mal à la gorge… ici, à l’oreille).', 'The doctor asks what’s wrong (your ear hurts).'), ['我耳朵疼。', '我很健康。', '我的头发很长。'], '我耳朵疼。', ('Partie du corps + 疼.', 'Body part + 疼.')),
        TF('他身体很健康，很少生病。', ('Il est souvent malade.', 'He is often ill.'), FAUX, ('很少生病 = rarement malade.', '很少生病 = rarely ill.')),
      ]),
    L('zh-looks', ('Grand, mince, en chemise : décrire quelqu’un', 'Tall, slim, in a shirt: describing someone'), ('Décrire l’apparence et les vêtements d’une personne.', 'Describe someone’s appearance and clothes.'), 10, [
        ('个子 (gèzi) = la taille : 他个子很高. 矮 (ǎi) = petit de taille, 胖 (pàng) = gros, 瘦 (shòu) = mince, 可爱 (kě’ài) = mignon.', '个子 (gèzi) = height: 他个子很高. 矮 (ǎi) = short, 胖 (pàng) = fat, 瘦 (shòu) = thin, 可爱 (kě’ài) = cute.'),
        ('Les vêtements : 衬衫 (chemise), 裤子 (pantalon), 裙子 (jupe), 帽子 (chapeau), 皮鞋 (chaussures de cuir), 眼镜 (lunettes). On les compte avec 件 (haut), 条 (pantalon, jupe), 双 (paire), 顶 (chapeau).', 'Clothes: 衬衫 (shirt), 裤子 (trousers), 裙子 (skirt), 帽子 (hat), 皮鞋 (leather shoes), 眼镜 (glasses). They are counted with 件 (tops), 条 (trousers, skirts), 双 (pairs), 顶 (hats).'),
        ('比较 (bǐjiào) + adjectif = assez, plutôt : 这条裙子比较贵. 试 (shì) = essayer : 我可以试一下吗？', '比较 (bǐjiào) + adjective = rather, fairly: 这条裙子比较贵. 试 (shì) = to try: 我可以试一下吗？'),
      ], [
        ZG('bijiao', '比较 + 形容词', 'bǐjiào', ('plutôt, assez', 'rather, fairly')),
        Z('gezi', '个子', 'gèzi', ('taille (d’une personne)', 'height (of a person)')),
        Z('ai', '矮', 'ǎi', ('petit (de taille)', 'short (in height)')),
        Z('pang', '胖', 'pàng', ('gros', 'fat')),
        Z('shou', '瘦', 'shòu', ('mince, maigre', 'thin')),
        Z('keai', '可爱', 'kě’ài', ('mignon', 'cute')),
        Z('chenshan', '衬衫', 'chènshān', ('chemise', 'shirt')),
        Z('kuzi', '裤子', 'kùzi', ('pantalon', 'trousers')),
        Z('qunzi', '裙子', 'qúnzi', ('jupe', 'skirt')),
        Z('maozi', '帽子', 'màozi', ('chapeau', 'hat')),
        Z('pixie', '皮鞋', 'píxié', ('chaussures en cuir', 'leather shoes')),
        Z('yanjing-glasses', '眼镜', 'yǎnjìng', ('lunettes', 'glasses')),
        Z('bijiao', '比较', 'bǐjiào', ('plutôt ; comparer', 'rather; to compare')),
        Z('shi-try', '试', 'shì', ('essayer', 'to try')),
      ], [
        x('我哥哥个子很高，比较瘦，戴着眼镜。', 'Wǒ gēge gèzi hěn gāo, bǐjiào shòu, dàizhe yǎnjìng.', 'Mon grand frère est grand, plutôt mince, et porte des lunettes.', 'My older brother is tall, fairly thin, and wears glasses.'),
        x('这条裙子很漂亮，我可以试一下吗？', 'Zhè tiáo qúnzi hěn piàoliang, wǒ kěyǐ shì yíxià ma?', 'Cette jupe est très jolie, je peux l’essayer ?', 'This skirt is lovely; may I try it on?'),
      ], [
        FB(COMPLETE, '我想买一＿皮鞋。', ['双', '条', '件'], '双', ('Une paire : 双.', 'A pair: 双.'), ('Je voudrais acheter une paire de chaussures en cuir.', 'I’d like to buy a pair of leather shoes.')),
        FB(COMPLETE, '这＿裤子太长了。', ['条', '件', '双'], '条', ('Un pantalon : 一条裤子.', 'Trousers: 一条裤子.'), ('Ce pantalon est trop long.', 'These trousers are too long.')),
        DC(ANSWER, [('服务员', '这件衬衫怎么样？')], ('La vendeuse te demande ton avis sur la chemise (tu veux l’essayer).', 'The shop assistant asks your opinion on the shirt (you want to try it on).'), ['不错，我可以试试吗？', '我个子很矮。', '他很可爱。'], '不错，我可以试试吗？', ('Essayer : 试试.', 'Try on: 试试.')),
        TF('她又高又瘦。', ('Elle est petite et ronde.', 'She is short and plump.'), FAUX, ('又高又瘦 = grande et mince.', '又高又瘦 = tall and thin.')),
      ]),
  ]),
  CH('hsk3-w7-c2', ('Les offrandes des pèlerins', 'The pilgrims’ offerings'), [
    L('zh-things', ('Parapluie, appareil photo, couleurs : 多么 et les classificateurs', 'Umbrella, camera, colours: 多么 and measure words'), ('Compter les objets et s’exclamer devant un spectacle.', 'Count objects and exclaim at a sight.'), 9, [
        ('Classificateurs : 种 (sorte), 辆 (véhicule), 位 (personne, poli), 段 (passage, période), 条 (chose longue : route, rivière, poisson), 米 (mètre).', 'Measure words: 种 (kind), 辆 (vehicle), 位 (person, polite), 段 (section, period), 条 (long thing: road, river, fish), 米 (metre).'),
        ('多么 + adjectif + 啊 ! = comme c’est… ! : 这儿的花多么漂亮啊 ! 啊 en fin de phrase adoucit ou renforce une exclamation.', '多么 + adjective + 啊! = how…!: 这儿的花多么漂亮啊! 啊 at the end of a sentence softens or strengthens an exclamation.'),
        ('Les objets du pèlerin : 伞 (parapluie), 包 (sac), 照相机 (appareil photo), 照片 (photo), 画 (peindre, tableau). Couleurs : 蓝 (bleu), 绿 (vert).', 'The pilgrim’s things: 伞 (umbrella), 包 (bag), 照相机 (camera), 照片 (photo), 画 (to paint, painting). Colours: 蓝 (blue), 绿 (green).'),
      ], [
        ZG('duome', '多么 + 形容词 + 啊！', 'duōme… a', ('comme c’est… ! (exclamation)', 'how…! (exclamation)')),
        Z('zhong-kind', '种', 'zhǒng', ('sorte, espèce', 'kind, type')),
        Z('liang-mw', '辆', 'liàng', ('classificateur des véhicules', 'measure word for vehicles')),
        Z('wei-mw', '位', 'wèi', ('classificateur poli des personnes', 'polite measure word for people')),
        Z('duan', '段', 'duàn', ('passage, période', 'section, period')),
        Z('tiao', '条', 'tiáo', ('classificateur des choses longues', 'measure word for long things')),
        Z('shuang', '双', 'shuāng', ('paire', 'pair')),
        Z('mi-metre', '米', 'mǐ', ('mètre ; riz', 'metre; rice')),
        Z('duome', '多么', 'duōme', ('comme, combien (exclamation)', 'how (exclamation)')),
        Z('a', '啊', 'a', ('(particule d’exclamation)', '(exclamation particle)')),
        Z('san', '伞', 'sǎn', ('parapluie', 'umbrella')),
        Z('bao-bag', '包', 'bāo', ('sac ; envelopper', 'bag; to wrap')),
        Z('zhaoxiangji', '照相机', 'zhàoxiàngjī', ('appareil photo', 'camera')),
        Z('zhaopian', '照片', 'zhàopiàn', ('photo', 'photo')),
        Z('hua-paint', '画', 'huà', ('peindre, dessiner ; tableau', 'to paint, to draw; painting')),
        Z('lan', '蓝', 'lán', ('bleu', 'blue')),
        Z('lü', '绿', 'lǜ', ('vert', 'green')),
      ], [
        x('天多么蓝啊！我们拍几张照片吧。', 'Tiān duōme lán a! Wǒmen pāi jǐ zhāng zhàopiàn ba.', 'Comme le ciel est bleu ! Prenons quelques photos.', 'How blue the sky is! Let’s take a few photos.'),
        x('门口有两辆车，那位先生是我们的司机。', 'Ménkǒu yǒu liǎng liàng chē, nà wèi xiānsheng shì wǒmen de sījī.', 'Il y a deux voitures devant la porte ; ce monsieur est notre chauffeur.', 'There are two cars at the door; that gentleman is our driver.'),
      ], [
        FB(COMPLETE, '外面下雨了，带上＿吧。', ['伞', '包', '照片'], '伞', ('Contre la pluie : 伞.', 'Against the rain: 伞.'), ('Il pleut dehors, prends un parapluie.', 'It’s raining outside; take an umbrella.')),
        FB(COMPLETE, '这＿河有五百米长。', ['条', '辆', '位'], '条', ('Une rivière : 一条河.', 'A river: 一条河.'), ('Cette rivière fait cinq cents mètres de long.', 'This river is five hundred metres long.')),
        FB(COMPLETE, '请问，您要哪＿颜色？', ['种', '段', '双'], '种', ('Quelle sorte : 哪种.', 'Which kind: 哪种.'), ('Quelle couleur voulez-vous, s’il vous plaît ?', 'Which colour would you like, please?')),
        TF('这张画上有很多绿色的树。', ('Le tableau montre des arbres verts.', 'The painting shows green trees.'), VRAI, ('绿色的树 = arbres verts.', '绿色的树 = green trees.')),
      ]),
  ])])

# ═════════════════════════ 8 : le grand débat de Jixia — opinions, intérêts, buts ═════════════════════════
W8 = WORLD('hsk3-w8', ('Le grand débat de Jixia', 'The great Jixia debate'), REGION,
  ('Donner son avis (认为, 以为, 关于) et ajouter un argument (不但…而且) ; ses centres d’intérêt et les médias ; un but (为了), une fête, des vœux.', 'Giving your opinion (认为, 以为, 关于) and adding an argument (不但…而且); interests and media; a purpose (为了), a festival, good wishes.'),
  (('Gonggong le briseur du ciel', 'Gonggong the Sky-Breaker'), '共', ('Gonggong, dieu des eaux furieux, a jadis brisé d’un coup de tête la montagne qui soutenait le ciel. Il veut interrompre le grand débat de l’académie : défends tes idées avec ordre et raison.', 'Gonggong, the furious water god, once broke the mountain that held up the sky with a blow of his head. He wants to stop the academy’s great debate: defend your ideas with order and reason.')),
  [CH('hsk3-w8-c1', ('L’académie Jixia', 'The Jixia Academy'), [
    HL('zh-hz-debate', ('Les caractères du débat : 认 文 化 闻 音 乐 参 加', 'Debate characters: 认 文 化 闻 音 乐 参 加'), ('Reconnaître les caractères de la culture et des opinions.', 'Recognise the characters of culture and opinion.'), [
      ('文 (wén) montrait un homme au torse tatoué : les motifs, puis l’écriture. 文化 (wénhuà) = « transformer par l’écrit », la culture.', '文 (wén) showed a man with a tattooed chest: patterns, then writing. 文化 (wénhuà) = “transforming through writing”, culture.'),
      ('闻 (wén, entendre) met une oreille 耳 dans une porte 门 ; 音 (yīn, son) est une bouche d’où sort un trait. 乐 (yuè, musique) dessinait des cordes sur un support de bois.', '闻 (wén, to hear) puts an ear 耳 inside a door 门; 音 (yīn, sound) is a mouth with a stroke coming out. 乐 (yuè, music) drew strings on a wooden frame.'),
    ], [
      H('ren', '认', 'rèn', ('reconnaître, estimer', 'to recognise, to consider'), 4), H('wen-script', '文', 'wén', ('écrit, culture', 'writing, culture'), 4),
      H('hua-change', '化', 'huà', ('transformer', 'to transform'), 4), H('wen-hear', '闻', 'wén', ('entendre, nouvelle', 'to hear, news'), 9),
      H('yin-sound', '音', 'yīn', ('son', 'sound'), 9), H('yue-music', '乐', 'yuè', ('musique', 'music'), 5),
      H('can', '参', 'cān', ('prendre part', 'to join in'), 8), H('jia', '加', 'jiā', ('ajouter', 'to add'), 5),
    ]),
    L('zh-opinion', ('À mon avis : 认为, 以为, 不但…而且', 'In my view: 认为, 以为, 不但…而且'), ('Donner son opinion et accumuler les arguments.', 'Give your opinion and pile up arguments.'), 10, [
        ('认为 (rènwéi) = estimer, considérer (avis réfléchi) : 我认为他说得对. 以为 (yǐwéi) = croire à tort : 我以为你走了 (je croyais que tu étais parti… mais non).', '认为 (rènwéi) = to consider (a reasoned opinion): 我认为他说得对. 以为 (yǐwéi) = to wrongly think: 我以为你走了 (I thought you had left… but no).'),
        ('不但 A，而且 B = non seulement A, mais aussi B : 他不但会说汉语，而且写得很好.', '不但 A，而且 B = not only A, but also B: 他不但会说汉语，而且写得很好.'),
        ('关于 (guānyú) = au sujet de : 关于这个问题. 特别 (tèbié) = particulièrement ; 重要 (zhòngyào) = important ; 主要 (zhǔyào) = principal ; 有名 (yǒumíng) = célèbre.', '关于 (guānyú) = about, concerning: 关于这个问题. 特别 (tèbié) = especially; 重要 (zhòngyào) = important; 主要 (zhǔyào) = main; 有名 (yǒumíng) = famous.'),
      ], [
        ZG('budan-erqie', '不但…，而且…', 'búdàn…, érqiě…', ('non seulement…, mais aussi…', 'not only…, but also…')),
        Z('renwei', '认为', 'rènwéi', ('estimer, considérer', 'to consider, to think')),
        Z('yiwei', '以为', 'yǐwéi', ('croire (à tort)', 'to (wrongly) believe')),
        Z('guanyu', '关于', 'guānyú', ('au sujet de', 'about, concerning')),
        Z('budan', '不但', 'búdàn', ('non seulement', 'not only')),
        Z('erqie', '而且', 'érqiě', ('de plus, et aussi', 'moreover, and also')),
        Z('wenhua', '文化', 'wénhuà', ('culture', 'culture')),
        Z('gushi', '故事', 'gùshi', ('histoire, récit', 'story')),
        Z('youming', '有名', 'yǒumíng', ('célèbre', 'famous')),
        Z('tebie', '特别', 'tèbié', ('particulièrement ; spécial', 'especially; special')),
        Z('zhongyao', '重要', 'zhòngyào', ('important', 'important')),
        Z('zhuyao', '主要', 'zhǔyào', ('principal', 'main')),
      ], [
        x('我认为学习历史和文化非常重要。', 'Wǒ rènwéi xuéxí lìshǐ hé wénhuà fēicháng zhòngyào.', 'J’estime qu’étudier l’histoire et la culture est très important.', 'I believe studying history and culture is very important.'),
        x('我以为他是老师，其实他是学生。', 'Wǒ yǐwéi tā shì lǎoshī, qíshí tā shì xuésheng.', 'Je croyais que c’était un professeur ; en fait, c’est un étudiant.', 'I thought he was a teacher; actually he’s a student.'),
      ], [
        FB(COMPLETE, '我＿今天是星期六，原来是星期五！', ['以为', '认为', '决定'], '以为', ('Croire à tort : 以为.', 'Wrongly believe: 以为.'), ('Je croyais qu’on était samedi : en fait, c’est vendredi !', 'I thought it was Saturday; it’s actually Friday!')),
        FB(COMPLETE, '这家饭馆不但便宜，＿很好吃。', ['而且', '但是', '所以'], '而且', ('不但…，而且….', '不但…，而且….'), ('Ce restaurant est non seulement bon marché, mais aussi délicieux.', 'This restaurant is not only cheap but also delicious.')),
        FB(COMPLETE, '老师给我们讲了一个＿熊猫的故事。', ['关于', '对于', '根据'], '关于', ('Au sujet de : 关于.', 'About: 关于.'), ('Le maître nous a raconté une histoire sur les pandas.', 'The teacher told us a story about pandas.')),
        TF('孔子是中国历史上很有名的人。', ('Confucius est un personnage célèbre de l’histoire chinoise.', 'Confucius is a famous figure in Chinese history.'), VRAI, ('很有名 = très célèbre.', '很有名 = very famous.')),
      ]),
    L('zh-interest', ('Je m’intéresse à la musique : 对…感兴趣', 'I’m interested in music: 对…感兴趣'), ('Parler de ses intérêts, des médias et des concours.', 'Talk about your interests, media and competitions.'), 10, [
        ('对 A 感兴趣 = s’intéresser à A : 我对中国音乐很感兴趣. 兴趣 (xìngqù) = l’intérêt ; 爱好 (àihào) = le passe-temps.', '对 A 感兴趣 = to be interested in A: 我对中国音乐很感兴趣. 兴趣 (xìngqù) = interest; 爱好 (àihào) = hobby.'),
        ('Les médias : 新闻 (actualités), 节目 (émission), 游戏 (jeu), 上网 (aller sur Internet), 电子邮件 (e-mail), 信 (lettre), 声音 (son, voix).', 'Media: 新闻 (news), 节目 (programme), 游戏 (game), 上网 (to go online), 电子邮件 (email), 信 (letter), 声音 (sound, voice).'),
        ('参加 (cānjiā) = participer : 参加比赛 (participer à un concours). 机会 (jīhuì) = occasion ; 选择 (xuǎnzé) = choisir.', '参加 (cānjiā) = to take part: 参加比赛 (to enter a competition). 机会 (jīhuì) = opportunity; 选择 (xuǎnzé) = to choose.'),
      ], [
        ZG('gan-xingqu', '对 + 名词 + 感兴趣', 'duì… gǎn xìngqù', ('s’intéresser à', 'to be interested in')),
        Z('xingqu', '兴趣', 'xìngqù', ('intérêt', 'interest')),
        Z('aihao', '爱好', 'àihào', ('passe-temps, loisir', 'hobby')),
        Z('yinyue', '音乐', 'yīnyuè', ('musique', 'music')),
        Z('xinwen', '新闻', 'xīnwén', ('actualités, informations', 'news')),
        Z('jiemu', '节目', 'jiémù', ('émission, programme', 'programme, show')),
        Z('youxi', '游戏', 'yóuxì', ('jeu', 'game')),
        Z('shangwang', '上网', 'shàngwǎng', ('aller sur Internet', 'to go online')),
        Z('dianziyoujian', '电子邮件', 'diànzǐ yóujiàn', ('e-mail', 'email')),
        Z('xin-letter', '信', 'xìn', ('lettre', 'letter')),
        Z('shengyin', '声音', 'shēngyīn', ('son, voix', 'sound, voice')),
        Z('canjia', '参加', 'cānjiā', ('participer', 'to take part')),
        Z('bisai', '比赛', 'bǐsài', ('compétition, match', 'competition, match')),
        Z('jihui', '机会', 'jīhuì', ('occasion, chance', 'opportunity')),
        Z('xuanze', '选择', 'xuǎnzé', ('choisir ; choix', 'to choose; choice')),
      ], [
        x('我对中国文化很感兴趣，经常上网看新闻。', 'Wǒ duì Zhōngguó wénhuà hěn gǎn xìngqù, jīngcháng shàngwǎng kàn xīnwén.', 'Je m’intéresse beaucoup à la culture chinoise et je lis souvent les actualités en ligne.', 'I’m very interested in Chinese culture and often read the news online.'),
        x('这是一个很好的机会，你应该参加这次比赛。', 'Zhè shì yí ge hěn hǎo de jīhuì, nǐ yīnggāi cānjiā zhè cì bǐsài.', 'C’est une très bonne occasion : tu devrais participer à ce concours.', 'It’s a great opportunity; you should enter this competition.'),
      ], [
        FB(COMPLETE, '他＿音乐很感兴趣。', ['对', '跟', '给'], '对', ('S’intéresser à : 对…感兴趣.', 'Interested in: 对…感兴趣.'), ('Il s’intéresse beaucoup à la musique.', 'He’s very interested in music.')),
        FB(COMPLETE, '我给你发了一封＿，你看了吗？', ['电子邮件', '节目', '声音'], '电子邮件', ('Envoyer un message : 发电子邮件.', 'Send a message: 发电子邮件.'), ('Je t’ai envoyé un e-mail, tu l’as lu ?', 'I sent you an email; have you read it?')),
        DC(ANSWER, [('同学', '你的爱好是什么？')], ('Un camarade te demande tes passe-temps (la musique et la natation).', 'A classmate asks about your hobbies (music and swimming).'), ['我喜欢音乐和游泳。', '我选择这个。', '我参加了。'], '我喜欢音乐和游泳。', ('Un passe-temps : 喜欢 + activité.', 'A hobby: 喜欢 + activity.')),
        TF('这个节目的声音太小了，我听不清楚。', ('Le son de l’émission est trop fort.', 'The programme’s sound is too loud.'), FAUX, ('声音太小 = son trop faible.', '声音太小 = sound too low.')),
      ]),
  ]),
  CH('hsk3-w8-c2', ('La fin du débat', 'The end of the debate'), [
    L('zh-weile', ('Pour réussir : 为了, fêtes et vœux', 'In order to succeed: 为了, festivals and wishes'), ('Exprimer un but, parler d’une fête et souhaiter quelque chose.', 'State a purpose, talk about a festival and wish someone well.'), 10, [
        ('为了 (wèile) + but, … = pour, afin de : 为了学好汉语，他每天练习. 为 (wèi) + personne = pour quelqu’un : 我为你高兴 (je suis content pour toi).', '为了 (wèile) + purpose, … = in order to: 为了学好汉语，他每天练习. 为 (wèi) + person = for someone: 我为你高兴 (I’m happy for you).'),
        ('结束 (jiéshù) = se terminer ; 完成 (wánchéng) = achever ; 习惯 (xíguàn) = habitude, s’habituer à ; 见面 (jiànmiàn) = se voir.', '结束 (jiéshù) = to end; 完成 (wánchéng) = to complete; 习惯 (xíguàn) = habit, to get used to; 见面 (jiànmiàn) = to meet up.'),
        ('Les fêtes : 节日 (fête), 礼物 (cadeau), 结婚 (se marier), 祝 (souhaiter) : 祝你生日快乐 ! 发 (fā) = envoyer : 发信息.', 'Festivals: 节日 (festival), 礼物 (present), 结婚 (to marry), 祝 (to wish): 祝你生日快乐! 发 (fā) = to send: 发信息.'),
      ], [
        ZG('weile', '为了 + 目的，…', 'wèile', ('pour, afin de (but)', 'in order to (purpose)')),
        Z('weile', '为了', 'wèile', ('pour, afin de', 'in order to')),
        Z('wei-for', '为', 'wèi', ('pour (quelqu’un)', 'for (someone)')),
        Z('jieshu', '结束', 'jiéshù', ('se terminer, finir', 'to end')),
        Z('wancheng', '完成', 'wánchéng', ('terminer, achever', 'to complete')),
        Z('xiguan', '习惯', 'xíguàn', ('habitude ; s’habituer', 'habit; to get used to')),
        Z('jianmian', '见面', 'jiànmiàn', ('se voir, se rencontrer', 'to meet up')),
        Z('jieri', '节日', 'jiérì', ('fête', 'festival, holiday')),
        Z('liwu', '礼物', 'lǐwù', ('cadeau', 'present, gift')),
        Z('jiehun', '结婚', 'jiéhūn', ('se marier', 'to get married')),
        Z('zhu-wish', '祝', 'zhù', ('souhaiter', 'to wish')),
        Z('fa', '发', 'fā', ('envoyer ; émettre', 'to send; to emit')),
      ], [
        x('为了参加比赛，她每天练习三个小时。', 'Wèile cānjiā bǐsài, tā měi tiān liànxí sān ge xiǎoshí.', 'Pour participer au concours, elle s’entraîne trois heures par jour.', 'To take part in the competition, she practises three hours a day.'),
        x('祝你们新年快乐，我们节日以后见面吧！', 'Zhù nǐmen xīnnián kuàilè, wǒmen jiérì yǐhòu jiànmiàn ba!', 'Bonne année à vous ! Voyons-nous après les fêtes.', 'Happy New Year to you all! Let’s meet up after the holidays.'),
      ], [
        FB(COMPLETE, '＿身体健康，爷爷每天去公园锻炼。', ['为了', '因为', '如果'], '为了', ('Un but : 为了.', 'A purpose: 为了.'), ('Pour rester en bonne santé, grand-père va faire de l’exercice au parc tous les jours.', 'To stay healthy, grandpa exercises in the park every day.')),
        FB(COMPLETE, '会议几点＿？', ['结束', '完成', '习惯'], '结束', ('Une réunion se termine : 结束.', 'A meeting ends: 结束.'), ('À quelle heure la réunion se termine-t-elle ?', 'What time does the meeting end?')),
        DC(ANSWER, [('朋友', '我下个月结婚！')], ('Un ami t’annonce son mariage.', 'A friend tells you they are getting married.'), ['真的吗？祝你们幸福！', '我习惯了。', '会议结束了。'], '真的吗？祝你们幸福！', ('Féliciter : 祝你们幸福.', 'Congratulate: 祝你们幸福.')),
        TF('我已经习惯了这儿的天气。', ('La personne ne supporte pas le climat.', 'The speaker can’t stand the climate.'), FAUX, ('习惯了 = s’y être habitué.', '习惯了 = has got used to it.')),
      ]),
  ])])

write_level(3, ('HSK 3 : les Cent Écoles', 'HSK 3: the Hundred Schools'), REGION, 'Shores of Qi',
  [W1, W2, W3, W4, W5, W6, W7, W8, FINAL(3, REGION, ('Simulation HSK 3 : l’académie Jixia', 'HSK 3 simulation: the Jixia Academy'), 300, 180, 'écoute (听力), lecture (阅读) et écriture (书写)', 'listening (听力), reading (阅读) and writing (书写)')])
