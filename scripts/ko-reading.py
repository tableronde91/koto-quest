# Lecture en coréen : contes traditionnels coréens (domaine public) réécrits en coréen simple.
# Ajoute (ou remplace) les contes coréens dans content/reading/stories.json, sans toucher aux contes japonais.
# Usage : python3 scripts/ko-reading.py
import json, os
ROOT = os.path.join(os.path.dirname(__file__), '..')
P = os.path.join(ROOT, 'content/reading/stories.json')

def S(ko, fr, en):
    """Phrase : le texte à lire et à prononcer est le même (pas de furigana en coréen)."""
    return {'jp': ko, 'fr': fr, 'en': en, 'kana': ko}

def W(ko, rom, fr, en):
    return {'jp': ko, 'reading': rom, 'fr': fr, 'en': en}

def Q(q, choices, answer):
    return {'q': {'fr': q[0], 'en': q[1]}, 'choices': [{'fr': f, 'en': e} for f, e in choices], 'answer': answer}

def CH(slug, title, paragraphs, words, questions):
    ko, fr, en = title
    return {'slug': slug, 'title': {'jp': ko, 'fr': fr, 'en': en}, 'paragraphs': paragraphs, 'words': words, 'questions': questions}

def STORY(slug, glyph, level, color, title, summary, chapters):
    ko, fr, en = title
    return {'slug': slug, 'glyph': glyph, 'level': level, 'color': color, 'title': {'jp': ko, 'fr': fr, 'en': en}, 'summary': {'fr': summary[0], 'en': summary[1]}, 'chapters': chapters}

# ═════════════════════════ 해님 달님 ═════════════════════════
HAENIM = STORY('haenim-dalnim', '해', 'TOPIK1', '#E9A23B', ('해님 달님', 'Le Soleil et la Lune', 'The Sun and the Moon'),
  ('Un tigre affamé poursuit un frère et une sœur jusqu’en haut d’un arbre. Le ciel leur tend une corde…', 'A hungry tiger chases a brother and sister to the top of a tree. Heaven lowers them a rope…'), [
  CH('haenim-dalnim-1', ('떡 장수 어머니', 'La mère marchande de gâteaux de riz', 'The rice-cake seller'), [
    [S('옛날 옛날에 산속 작은 집에 어머니와 오누이가 살았어요.', 'Il était une fois, dans une petite maison au milieu des montagnes, une mère et ses deux enfants, un frère et une sœur.', 'Once upon a time, in a small house in the mountains, there lived a mother with her son and daughter.'),
     S('오빠와 여동생은 아주 사이가 좋았어요.', 'Le grand frère et la petite sœur s’entendaient très bien.', 'The brother and his little sister got on very well.'),
     S('어머니는 매일 시장에서 떡을 팔았어요.', 'Chaque jour, la mère vendait des gâteaux de riz au marché.', 'Every day, the mother sold rice cakes at the market.')],
    [S('어느 날 어머니는 늦게까지 일했어요.', 'Un jour, la mère travailla jusque tard.', 'One day, the mother worked until late.'),
     S('「얘들아, 문을 꼭 잠가!」', '« Les enfants, fermez bien la porte à clé ! »', '“Children, lock the door tight!”'),
     S('어머니는 남은 떡을 머리에 이고 고개를 넘었어요.', 'La mère posa les gâteaux qui restaient sur sa tête et prit le chemin du col.', 'The mother carried the leftover rice cakes on her head and set off over the mountain pass.')],
  ], [
    W('옛날', 'yennal', 'autrefois', 'long ago'),
    W('오누이', 'onui', 'frère et sœur', 'brother and sister'),
    W('떡', 'tteok', 'gâteau de riz', 'rice cake'),
    W('시장', 'sijang', 'marché', 'market'),
    W('고개', 'gogae', 'col (de montagne)', 'mountain pass'),
    W('잠그다', 'jamgeuda', 'fermer à clé', 'to lock'),
  ], [
    Q(('Que vendait la mère ?', 'What did the mother sell?'), [('Du poisson', 'Fish'), ('Des gâteaux de riz', 'Rice cakes'), ('Des vêtements', 'Clothes')], 1),
    Q(('Où vivait la famille ?', 'Where did the family live?'), [('Au bord de la mer', 'By the sea'), ('Dans une grande ville', 'In a big city'), ('Dans une petite maison dans la montagne', 'In a small house in the mountains')], 2),
  ]),
  CH('haenim-dalnim-2', ('떡 하나 주면 안 잡아먹지', 'Donne-moi un gâteau et je ne te mangerai pas', 'Give me a rice cake and I won’t eat you'), [
    [S('첫 번째 고개에서 커다란 호랑이가 나타났어요.', 'Au premier col, un énorme tigre apparut.', 'At the first pass, a huge tiger appeared.'),
     S('「떡 하나 주면 안 잡아먹지!」', '« Donne-moi un gâteau de riz et je ne te mangerai pas ! »', '“Give me a rice cake and I won’t eat you!”'),
     S('어머니는 무서워서 떡을 하나 주었어요.', 'La mère, effrayée, lui donna un gâteau.', 'The mother was frightened, so she gave it a rice cake.')],
    [S('하지만 호랑이는 다음 고개에서도 또 나타났어요.', 'Mais le tigre réapparut au col suivant.', 'But the tiger appeared again at the next pass.'),
     S('고개를 넘을 때마다 떡이 하나씩 없어졌어요.', 'À chaque col, un gâteau de plus disparaissait.', 'At every pass, one more rice cake was gone.'),
     S('마지막 고개에서 떡이 하나도 없었어요. 배고픈 호랑이는 어머니를 잡아먹었어요.', 'Au dernier col, il ne restait plus un seul gâteau. Le tigre affamé dévora la mère.', 'At the last pass there were no rice cakes left. The hungry tiger ate the mother.')],
  ], [
    W('호랑이', 'horangi', 'tigre', 'tiger'),
    W('나타나다', 'natanada', 'apparaître', 'to appear'),
    W('무섭다', 'museopda', 'avoir peur ; être effrayant', 'to be scared; to be scary'),
    W('배고프다', 'baegopeuda', 'avoir faim', 'to be hungry'),
    W('잡아먹다', 'jabameokda', 'dévorer', 'to devour'),
    W('마지막', 'majimak', 'dernier', 'last'),
  ], [
    Q(('Que demande le tigre ?', 'What does the tiger ask for?'), [('De l’argent', 'Money'), ('Un gâteau de riz', 'A rice cake'), ('De l’eau', 'Water')], 1),
    Q(('Combien de gâteaux reste-t-il au dernier col ?', 'How many rice cakes are left at the last pass?'), [('Aucun', 'None'), ('Un seul', 'Just one'), ('Beaucoup', 'Lots')], 0),
  ]),
  CH('haenim-dalnim-3', ('엄마 손이 왜 이래요?', 'Maman, pourquoi ta main est comme ça ?', 'Mum, why is your hand like that?'), [
    [S('호랑이는 어머니 옷을 입고 오누이의 집에 갔어요.', 'Le tigre enfila les vêtements de la mère et se rendit chez les enfants.', 'The tiger put on the mother’s clothes and went to the children’s house.'),
     S('「얘들아, 엄마 왔다. 문 열어라.」', '« Les enfants, maman est rentrée. Ouvrez la porte. »', '“Children, Mum’s home. Open the door.”'),
     S('그런데 목소리가 이상했어요.', 'Mais sa voix était bizarre.', 'But the voice sounded strange.')],
    [S('「엄마, 손 좀 보여 주세요.」', '« Maman, montre-nous ta main, s’il te plaît. »', '“Mum, please show us your hand.”'),
     S('문틈으로 들어온 손에는 털이 가득했어요.', 'La main qui passa par l’entrebâillement de la porte était couverte de poils.', 'The hand that came through the gap in the door was covered in fur.'),
     S('「일을 많이 해서 그래.」 호랑이가 거짓말을 했어요.', '« C’est parce que j’ai beaucoup travaillé. » Le tigre mentait.', '“It’s because I worked so hard.” The tiger was lying.')],
  ], [
    W('옷', 'ot', 'vêtement', 'clothes'),
    W('목소리', 'moksori', 'voix', 'voice'),
    W('이상하다', 'isanghada', 'être bizarre', 'to be strange'),
    W('털', 'teol', 'poils, fourrure', 'fur, hair'),
    W('거짓말', 'geojinmal', 'mensonge', 'lie'),
    W('문틈', 'munteum', 'entrebâillement de la porte', 'gap in the door'),
  ], [
    Q(('Que porte le tigre ?', 'What is the tiger wearing?'), [('Les vêtements de la mère', 'The mother’s clothes'), ('Un chapeau de paille', 'A straw hat'), ('Rien', 'Nothing')], 0),
    Q(('Pourquoi les enfants se méfient-ils ?', 'Why are the children suspicious?'), [('La porte était ouverte', 'The door was open'), ('La voix et la main sont étranges', 'The voice and the hand are strange'), ('Il est en retard', 'It is late')], 1),
  ]),
  CH('haenim-dalnim-4', ('나무 위로 도망가요', 'Ils s’enfuient en haut de l’arbre', 'They escape up the tree'), [
    [S('오누이는 뒷문으로 몰래 나가서 우물가의 큰 나무 위로 올라갔어요.', 'Les enfants sortirent en cachette par la porte de derrière et grimpèrent dans le grand arbre près du puits.', 'The children slipped out of the back door and climbed the big tree by the well.'),
     S('호랑이가 우물 속을 보았어요. 물에 아이들의 얼굴이 보였어요.', 'Le tigre regarda au fond du puits. Les visages des enfants se reflétaient dans l’eau.', 'The tiger looked into the well. The children’s faces could be seen in the water.'),
     S('「너희들 거기 있니?」', '« Vous êtes là-dedans ? »', '“Are you in there?”')],
    [S('여동생이 웃음을 참지 못하고 「하하하!」 웃었어요.', 'La petite sœur ne put retenir son rire : « Ha ha ha ! »', 'The little sister couldn’t hold back her laughter: “Ha ha ha!”'),
     S('호랑이가 위를 보았어요. 「어떻게 올라갔니?」', 'Le tigre leva les yeux. « Comment êtes-vous montés ? »', 'The tiger looked up. “How did you get up there?”'),
     S('「참기름을 바르고 올라왔지!」 오빠의 꾀에 호랑이는 미끄러져서 자꾸 떨어졌어요.', '« On s’est enduits d’huile de sésame et on est montés ! » Piégé par la ruse du frère, le tigre glissait et retombait sans cesse.', '“We rubbed on sesame oil and climbed up!” Tricked by the brother, the tiger kept slipping and falling down.')],
  ], [
    W('나무', 'namu', 'arbre', 'tree'),
    W('우물', 'umul', 'puits', 'well'),
    W('올라가다', 'ollagada', 'monter, grimper', 'to climb'),
    W('참기름', 'chamgireum', 'huile de sésame', 'sesame oil'),
    W('미끄러지다', 'mikkeureojida', 'glisser', 'to slip'),
    W('웃음', 'useum', 'rire', 'laughter'),
  ], [
    Q(('Où se cachent les enfants ?', 'Where do the children hide?'), [('Dans le puits', 'In the well'), ('En haut d’un arbre', 'Up a tree'), ('Sous le lit', 'Under the bed')], 1),
    Q(('Pourquoi le tigre tombe-t-il ?', 'Why does the tiger fall?'), [('Il a mis de l’huile de sésame sur l’arbre', 'He put sesame oil on the tree'), ('Il est trop lourd', 'He is too heavy'), ('Il s’endort', 'He falls asleep')], 0),
  ]),
  CH('haenim-dalnim-5', ('해와 달이 되었어요', 'Ils devinrent le soleil et la lune', 'They became the sun and the moon'), [
    [S('그런데 여동생이 그만 말해 버렸어요. 「도끼로 찍고 올라오면 되지!」', 'Mais la petite sœur laissa échapper : « Il suffit de faire des marches avec une hache ! »', 'But the little sister blurted out: “You just have to cut steps with an axe!”'),
     S('호랑이는 도끼로 나무를 찍으면서 올라왔어요.', 'Le tigre grimpa en entaillant l’arbre à coups de hache.', 'The tiger climbed up, chopping into the tree with an axe.'),
     S('오누이는 하늘을 보고 빌었어요. 「하느님, 저희를 살려 주세요!」', 'Les enfants levèrent les yeux vers le ciel et prièrent : « Ciel, sauvez-nous ! »', 'The children looked up to the sky and prayed: “Heaven, please save us!”')],
    [S('그러자 하늘에서 튼튼한 줄이 내려왔어요. 오누이는 줄을 잡고 하늘로 올라갔어요.', 'Alors une corde solide descendit du ciel. Les enfants s’y accrochèrent et montèrent au ciel.', 'Then a strong rope came down from the sky. The children grabbed it and rose up into the sky.'),
     S('호랑이에게는 썩은 줄이 내려왔어요. 호랑이는 땅으로 떨어졌어요.', 'Pour le tigre, ce fut une corde pourrie qui descendit. Il tomba sur le sol.', 'For the tiger, a rotten rope came down. He fell to the ground.'),
     S('하늘에서 밤이 무서운 동생은 해가 되고, 오빠는 달이 되었어요.', 'Dans le ciel, la petite sœur, qui avait peur de la nuit, devint le soleil, et son frère devint la lune.', 'In the sky, the little sister, who was afraid of the dark, became the sun, and her brother became the moon.')],
  ], [
    W('도끼', 'dokki', 'hache', 'axe'),
    W('하늘', 'haneul', 'ciel', 'sky'),
    W('빌다', 'bilda', 'prier, implorer', 'to pray, to beg'),
    W('줄', 'jul', 'corde', 'rope'),
    W('해', 'hae', 'soleil', 'sun'),
    W('달', 'dal', 'lune', 'moon'),
  ], [
    Q(('Qu’est-ce qui descend du ciel pour les enfants ?', 'What comes down from the sky for the children?'), [('Une corde solide', 'A strong rope'), ('Une échelle', 'A ladder'), ('Un dragon', 'A dragon')], 0),
    Q(('Que devient la petite sœur ?', 'What does the little sister become?'), [('La lune', 'The moon'), ('Une étoile', 'A star'), ('Le soleil', 'The sun')], 2),
  ]),
])

# ═════════════════════════ 흥부와 놀부 ═════════════════════════
HEUNGBU = STORY('heungbu-nolbu', '박', 'TOPIK1', '#6FA35A', ('흥부와 놀부', 'Heungbu et Nolbu', 'Heungbu and Nolbu'),
  ('Deux frères, une hirondelle blessée et des calebasses magiques : le bon cœur est récompensé, l’avidité punie.', 'Two brothers, an injured swallow and magic gourds: a kind heart is rewarded, greed is punished.'), [
  CH('heungbu-nolbu-1', ('욕심쟁이 형 놀부', 'Nolbu, le frère avide', 'Nolbu, the greedy brother'), [
    [S('옛날에 형 놀부와 동생 흥부가 살았어요.', 'Il était une fois deux frères : l’aîné, Nolbu, et le cadet, Heungbu.', 'Long ago there lived two brothers: Nolbu, the elder, and Heungbu, the younger.'),
     S('형 놀부는 부자였지만 욕심이 많고 마음이 나빴어요.', 'Nolbu était riche, mais avide et méchant.', 'Nolbu was rich, but greedy and mean-hearted.'),
     S('동생 흥부는 가난했지만 착했어요.', 'Heungbu était pauvre, mais bon.', 'Heungbu was poor, but kind.')],
    [S('부모님이 돌아가셨어요. 놀부는 흥부 가족을 집에서 쫓아냈어요.', 'Leurs parents moururent. Nolbu chassa la famille de Heungbu de la maison.', 'Their parents died. Nolbu threw Heungbu’s family out of the house.'),
     S('흥부는 아이들과 함께 작은 초가집에서 살았어요.', 'Heungbu alla vivre avec ses enfants dans une petite chaumière.', 'Heungbu went to live with his children in a little thatched cottage.'),
     S('먹을 것이 없어도 흥부 가족은 서로 아끼고 웃었어요.', 'Même sans rien à manger, la famille de Heungbu s’aimait et riait.', 'Even with nothing to eat, Heungbu’s family cared for each other and laughed.')],
  ], [
    W('형', 'hyeong', 'grand frère (d’un garçon)', 'older brother (of a boy)'),
    W('부자', 'buja', 'riche', 'rich person'),
    W('욕심', 'yoksim', 'avidité', 'greed'),
    W('가난하다', 'gananhada', 'être pauvre', 'to be poor'),
    W('착하다', 'chakhada', 'être gentil, bon', 'to be kind, good'),
    W('초가집', 'chogajip', 'chaumière', 'thatched cottage'),
  ], [
    Q(('Comment est Nolbu ?', 'What is Nolbu like?'), [('Pauvre et gentil', 'Poor and kind'), ('Riche mais avide', 'Rich but greedy'), ('Malade', 'Ill')], 1),
    Q(('Où vit Heungbu ?', 'Where does Heungbu live?'), [('Dans un palais', 'In a palace'), ('Dans une petite chaumière', 'In a little thatched cottage'), ('Chez Nolbu', 'At Nolbu’s house')], 1),
  ]),
  CH('heungbu-nolbu-2', ('다친 제비', 'L’hirondelle blessée', 'The injured swallow'), [
    [S('어느 봄날, 흥부의 집에 제비가 둥지를 만들었어요.', 'Un jour de printemps, une hirondelle fit son nid chez Heungbu.', 'One spring day, a swallow built its nest at Heungbu’s house.'),
     S('그런데 아기 제비 한 마리가 땅에 떨어져서 다리를 다쳤어요.', 'Mais un bébé hirondelle tomba par terre et se blessa à la patte.', 'But a baby swallow fell to the ground and hurt its leg.'),
     S('흥부는 제비 다리를 정성껏 치료해 주었어요.', 'Heungbu soigna la patte de l’hirondelle avec grand soin.', 'Heungbu carefully tended the swallow’s leg.')],
    [S('제비는 금방 건강해졌어요.', 'L’hirondelle fut vite guérie.', 'The swallow soon got better.'),
     S('가을이 되었어요. 제비는 따뜻한 남쪽 나라로 떠났어요.', 'L’automne arriva. L’hirondelle partit vers les pays chauds du sud.', 'Autumn came. The swallow left for the warm lands of the south.'),
     S('「고마워, 제비야. 잘 가!」 흥부가 손을 흔들었어요.', '« Merci, petite hirondelle. Bon voyage ! » dit Heungbu en agitant la main.', '“Thank you, little swallow. Safe journey!” Heungbu waved goodbye.')],
  ], [
    W('제비', 'jebi', 'hirondelle', 'swallow'),
    W('둥지', 'dungji', 'nid', 'nest'),
    W('다리', 'dari', 'jambe, patte', 'leg'),
    W('다치다', 'dachida', 'se blesser', 'to get hurt'),
    W('남쪽', 'namjjok', 'sud', 'south'),
    W('떠나다', 'tteonada', 'partir', 'to leave'),
  ], [
    Q(('Qu’est-il arrivé au bébé hirondelle ?', 'What happened to the baby swallow?'), [('Il s’est blessé à la patte', 'It hurt its leg'), ('Il a perdu sa mère', 'It lost its mother'), ('Il a trop mangé', 'It ate too much')], 0),
    Q(('Où part l’hirondelle en automne ?', 'Where does the swallow go in autumn?'), [('Vers le nord', 'To the north'), ('Vers un pays chaud du sud', 'To a warm land in the south'), ('Dans la montagne', 'Into the mountains')], 1),
  ]),
  CH('heungbu-nolbu-3', ('박씨 하나', 'Une graine de calebasse', 'A gourd seed'), [
    [S('다음 해 봄, 제비가 돌아와서 흥부에게 박씨 하나를 주었어요.', 'Le printemps suivant, l’hirondelle revint et offrit à Heungbu une graine de calebasse.', 'The next spring, the swallow came back and gave Heungbu a gourd seed.'),
     S('흥부는 씨를 심었어요. 가을에 지붕 위에 커다란 박이 열렸어요.', 'Heungbu la planta. En automne, d’énormes calebasses poussèrent sur le toit.', 'Heungbu planted it. In autumn, huge gourds grew on the roof.'),
     S('「박을 타서 죽을 끓여 먹자.」 흥부와 아내는 톱으로 박을 탔어요.', '« Ouvrons une calebasse pour faire une bouillie. » Heungbu et sa femme la scièrent en deux.', '“Let’s open a gourd and make porridge.” Heungbu and his wife sawed it open.')],
    [S('박이 쩍! 열렸어요. 안에서 금과 은이 쏟아져 나왔어요!', 'Crac ! La calebasse s’ouvrit. De l’or et de l’argent s’en déversèrent !', 'Crack! The gourd split open. Gold and silver poured out!'),
     S('다른 박에서는 쌀과 비단, 그리고 멋진 집이 나왔어요.', 'Des autres calebasses sortirent du riz, de la soie et même une belle maison.', 'From the other gourds came rice, silk and even a beautiful house.'),
     S('흥부 가족은 하루아침에 부자가 되었어요.', 'Du jour au lendemain, la famille de Heungbu devint riche.', 'Overnight, Heungbu’s family became rich.')],
  ], [
    W('박', 'bak', 'calebasse', 'gourd'),
    W('씨', 'ssi', 'graine', 'seed'),
    W('심다', 'simda', 'planter', 'to plant'),
    W('금', 'geum', 'or', 'gold'),
    W('쌀', 'ssal', 'riz (cru)', 'rice (uncooked)'),
    W('하루아침에', 'haruachime', 'du jour au lendemain', 'overnight'),
  ], [
    Q(('Que donne l’hirondelle à Heungbu ?', 'What does the swallow give Heungbu?'), [('Une pièce d’or', 'A gold coin'), ('Une graine de calebasse', 'A gourd seed'), ('Une plume', 'A feather')], 1),
    Q(('Que trouvent-ils dans les calebasses ?', 'What do they find in the gourds?'), [('De l’or, du riz et une maison', 'Gold, rice and a house'), ('Des serpents', 'Snakes'), ('Rien du tout', 'Nothing at all')], 0),
  ]),
  CH('heungbu-nolbu-4', ('놀부의 꾀', 'La ruse de Nolbu', 'Nolbu’s scheme'), [
    [S('소문을 들은 놀부는 배가 아팠어요.', 'En apprenant la nouvelle, Nolbu crevait de jalousie (litt. « avait mal au ventre »).', 'When he heard the news, Nolbu was green with envy (literally, “his stomach hurt”).'),
     S('「나도 부자가 될 거야!」', '« Moi aussi, je vais devenir riche ! »', '“I’m going to get rich too!”'),
     S('놀부는 제비를 잡아서 일부러 다리를 부러뜨렸어요.', 'Nolbu attrapa une hirondelle et lui cassa la patte exprès.', 'Nolbu caught a swallow and broke its leg on purpose.')],
    [S('그리고 다리를 대충 묶어 주었어요.', 'Puis il lui banda la patte à la va-vite.', 'Then he bound the leg any old how.'),
     S('다음 해 봄, 그 제비도 박씨 하나를 가지고 왔어요.', 'Au printemps suivant, cette hirondelle aussi rapporta une graine de calebasse.', 'The next spring, that swallow also brought back a gourd seed.'),
     S('놀부는 신이 나서 씨를 심었어요.', 'Tout excité, Nolbu la planta.', 'Nolbu planted it excitedly.')],
  ], [
    W('소문', 'somun', 'rumeur', 'rumour'),
    W('배가 아프다', 'baega apeuda', 'être jaloux (litt. avoir mal au ventre)', 'to be jealous (lit. to have a stomach ache)'),
    W('일부러', 'ilbureo', 'exprès', 'on purpose'),
    W('부러뜨리다', 'bureotteurida', 'casser', 'to break'),
    W('신이 나다', 'sini nada', 'être tout excité', 'to be excited'),
    W('대충', 'daechung', 'à la va-vite, grossièrement', 'roughly, any old how'),
  ], [
    Q(('Que fait Nolbu à l’hirondelle ?', 'What does Nolbu do to the swallow?'), [('Il la soigne avec soin', 'He looks after it carefully'), ('Il lui casse la patte exprès', 'He breaks its leg on purpose'), ('Il la libère', 'He sets it free')], 1),
    Q(('Ici, « 배가 아팠어요 » veut dire…', 'Here, “배가 아팠어요” means…'), [('Il avait trop mangé', 'He had eaten too much'), ('Il était jaloux', 'He was jealous'), ('Il avait faim', 'He was hungry')], 1),
  ]),
  CH('heungbu-nolbu-5', ('놀부의 박', 'Les calebasses de Nolbu', 'Nolbu’s gourds'), [
    [S('가을에 놀부의 박도 아주 크게 자랐어요.', 'En automne, les calebasses de Nolbu devinrent elles aussi énormes.', 'In autumn, Nolbu’s gourds grew very big too.'),
     S('놀부는 기뻐서 첫 번째 박을 탔어요.', 'Ravi, Nolbu ouvrit la première.', 'Delighted, Nolbu sawed open the first one.'),
     S('그런데 박에서 도깨비들이 나와서 놀부를 혼내 주었어요!', 'Mais des dokkaebi en sortirent et lui donnèrent une bonne leçon !', 'But goblins jumped out and taught Nolbu a lesson!')],
    [S('다른 박에서는 더러운 물이 쏟아졌어요. 놀부의 집과 돈이 모두 사라졌어요.', 'Des autres calebasses jaillit une eau sale. La maison et l’argent de Nolbu disparurent.', 'Dirty water gushed out of the other gourds. Nolbu’s house and money all vanished.'),
     S('흥부는 갈 곳 없는 형을 따뜻하게 맞아 주었어요.', 'Heungbu accueillit chaleureusement son frère, qui n’avait plus nulle part où aller.', 'Heungbu warmly welcomed his brother, who had nowhere to go.'),
     S('놀부는 잘못을 뉘우치고, 두 형제는 사이좋게 살았어요.', 'Nolbu se repentit, et les deux frères vécurent en bonne entente.', 'Nolbu repented, and the two brothers lived happily together.')],
  ], [
    W('자라다', 'jarada', 'grandir, pousser', 'to grow'),
    W('도깨비', 'dokkaebi', 'dokkaebi (lutin coréen)', 'dokkaebi (Korean goblin)'),
    W('혼내다', 'honnaeda', 'punir, gronder', 'to scold, to punish'),
    W('사라지다', 'sarajida', 'disparaître', 'to disappear'),
    W('뉘우치다', 'nwiuchida', 'se repentir', 'to repent'),
    W('사이좋게', 'saijoke', 'en bonne entente', 'on good terms'),
  ], [
    Q(('Qu’est-ce qui sort de la calebasse de Nolbu ?', 'What comes out of Nolbu’s gourd?'), [('De l’or', 'Gold'), ('Des dokkaebi', 'Goblins (dokkaebi)'), ('Une hirondelle', 'A swallow')], 1),
    Q(('Comment l’histoire se termine-t-elle ?', 'How does the story end?'), [('Heungbu chasse Nolbu', 'Heungbu drives Nolbu away'), ('Les deux frères vivent en paix', 'The two brothers live in peace'), ('Nolbu devient roi', 'Nolbu becomes king')], 1),
  ]),
])

# ═════════════════════════ 견우와 직녀 ═════════════════════════
GYEONU = STORY('gyeonu-jiknyeo', '별', 'TOPIK1', '#5A6FD1', ('견우와 직녀', 'Gyeonu et Jiknyeo', 'Gyeonu and Jiknyeo'),
  ('Le bouvier et la tisserande séparés par la Voie lactée ne se retrouvent qu’une nuit par an, sur un pont d’oiseaux.', 'The cowherd and the weaver, separated by the Milky Way, meet only one night a year, on a bridge of birds.'), [
  CH('gyeonu-jiknyeo-1', ('하늘나라의 두 사람', 'Deux habitants du ciel', 'Two people of the heavens'), [
    [S('옛날 하늘나라에 옥황상제의 딸 직녀가 살았어요.', 'Il y a longtemps, au royaume du ciel, vivait Jiknyeo, la fille de l’Empereur de Jade.', 'Long ago, in the kingdom of heaven, lived Jiknyeo, daughter of the Jade Emperor.'),
     S('직녀는 옷감을 아주 잘 짰어요.', 'Jiknyeo tissait merveilleusement bien.', 'Jiknyeo was a wonderful weaver.'),
     S('은하수 건너편에는 소를 키우는 성실한 청년 견우가 있었어요.', 'De l’autre côté de la Voie lactée vivait Gyeonu, un jeune bouvier travailleur.', 'Across the Milky Way lived Gyeonu, a hard-working young cowherd.')],
    [S('두 사람은 만나서 사랑에 빠졌어요.', 'Ils se rencontrèrent et tombèrent amoureux.', 'The two met and fell in love.'),
     S('옥황상제는 두 사람의 결혼을 허락했어요.', 'L’Empereur de Jade consentit à leur mariage.', 'The Jade Emperor gave his permission for them to marry.')],
  ], [
    W('하늘나라', 'haneullara', 'royaume du ciel', 'kingdom of heaven'),
    W('딸', 'ttal', 'fille (enfant)', 'daughter'),
    W('짜다', 'jjada', 'tisser', 'to weave'),
    W('은하수', 'eunhasu', 'Voie lactée', 'Milky Way'),
    W('소', 'so', 'vache, bœuf', 'cow, ox'),
    W('결혼', 'gyeolhon', 'mariage', 'marriage'),
  ], [
    Q(('Que fait Jiknyeo ?', 'What does Jiknyeo do?'), [('Elle tisse', 'She weaves'), ('Elle élève des bœufs', 'She raises cattle'), ('Elle chante', 'She sings')], 0),
    Q(('Qu’est-ce qui les sépare au départ ?', 'What separates them at first?'), [('Une montagne', 'A mountain'), ('La Voie lactée', 'The Milky Way'), ('La mer', 'The sea')], 1),
  ]),
  CH('gyeonu-jiknyeo-2', ('일을 하지 않아요', 'Ils ne travaillent plus', 'They stop working'), [
    [S('결혼한 뒤 두 사람은 너무 행복했어요.', 'Une fois mariés, ils étaient si heureux…', 'Once married, the two of them were so happy…'),
     S('그래서 매일 놀기만 하고 일을 하지 않았어요.', '… qu’ils ne faisaient que s’amuser et ne travaillaient plus.', '… that they did nothing but enjoy themselves and stopped working.'),
     S('하늘나라에는 옷이 모자라고, 소들은 배가 고팠어요.', 'Au ciel, les vêtements vinrent à manquer et les bœufs avaient faim.', 'In heaven, clothes ran short and the cattle went hungry.')],
    [S('옥황상제는 크게 화가 났어요.', 'L’Empereur de Jade entra dans une grande colère.', 'The Jade Emperor became very angry.'),
     S('「견우는 은하수 동쪽에, 직녀는 서쪽에 살아라!」', '« Gyeonu vivra à l’est de la Voie lactée, et Jiknyeo à l’ouest ! »', '“Gyeonu shall live east of the Milky Way, and Jiknyeo to the west!”'),
     S('「일 년에 한 번, 칠월 칠석에만 만나라!」', '« Vous ne vous verrez qu’une fois par an, le septième jour du septième mois ! »', '“You may meet only once a year, on the seventh day of the seventh month!”')],
  ], [
    W('행복하다', 'haengbokhada', 'être heureux', 'to be happy'),
    W('놀다', 'nolda', 'jouer, s’amuser', 'to play, to have fun'),
    W('모자라다', 'mojarada', 'manquer', 'to be lacking'),
    W('화가 나다', 'hwaga nada', 'se mettre en colère', 'to get angry'),
    W('칠석', 'chilseok', 'Chilseok (7e jour du 7e mois lunaire)', 'Chilseok (7th day of the 7th lunar month)'),
    W('동쪽', 'dongjjok', 'est', 'east'),
  ], [
    Q(('Pourquoi l’Empereur se fâche-t-il ?', 'Why does the Emperor get angry?'), [('Ils ne travaillent plus', 'They have stopped working'), ('Ils se disputent', 'They argue'), ('Ils sont partis', 'They have left')], 0),
    Q(('Combien de fois peuvent-ils se voir ?', 'How often can they meet?'), [('Chaque jour', 'Every day'), ('Une fois par mois', 'Once a month'), ('Une fois par an', 'Once a year')], 2),
  ]),
  CH('gyeonu-jiknyeo-3', ('까마귀와 까치의 다리', 'Le pont des corbeaux et des pies', 'The bridge of crows and magpies'), [
    [S('견우와 직녀는 매일 울면서 일 년을 기다렸어요.', 'Gyeonu et Jiknyeo attendirent une année entière en pleurant chaque jour.', 'Gyeonu and Jiknyeo waited a whole year, crying every day.'),
     S('드디어 칠석이 되었어요. 하지만 은하수가 너무 넓어서 건널 수 없었어요.', 'Enfin, Chilseok arriva. Mais la Voie lactée était trop large pour la traverser.', 'At last Chilseok came. But the Milky Way was too wide to cross.'),
     S('두 사람의 눈물이 비가 되어 땅에 내렸어요.', 'Leurs larmes se changèrent en pluie et tombèrent sur la terre.', 'Their tears turned into rain and fell on the earth.')],
    [S('땅의 까마귀와 까치들이 두 사람을 불쌍하게 생각했어요.', 'Sur la terre, les corbeaux et les pies eurent pitié d’eux.', 'On earth, the crows and magpies took pity on them.'),
     S('새들은 하늘로 날아가서 서로 머리를 맞대고 다리를 만들었어요.', 'Les oiseaux s’envolèrent vers le ciel et, tête contre tête, formèrent un pont.', 'The birds flew up to the sky and, head to head, made a bridge.'),
     S('사람들은 이 다리를 「오작교」라고 불러요.', 'On appelle ce pont « Ojakgyo », le pont des corbeaux et des pies.', 'People call this bridge “Ojakgyo”, the bridge of crows and magpies.')],
  ], [
    W('울다', 'ulda', 'pleurer', 'to cry'),
    W('드디어', 'deudieo', 'enfin', 'at last'),
    W('넓다', 'neolda', 'être large', 'to be wide'),
    W('눈물', 'nunmul', 'larmes', 'tears'),
    W('까치', 'kkachi', 'pie', 'magpie'),
    W('다리', 'dari', 'pont', 'bridge'),
  ], [
    Q(('Que deviennent leurs larmes ?', 'What do their tears become?'), [('De la pluie', 'Rain'), ('Des étoiles', 'Stars'), ('De la neige', 'Snow')], 0),
    Q(('Qui construit le pont ?', 'Who builds the bridge?'), [('L’Empereur de Jade', 'The Jade Emperor'), ('Les corbeaux et les pies', 'The crows and magpies'), ('Gyeonu', 'Gyeonu')], 1),
  ]),
  CH('gyeonu-jiknyeo-4', ('칠석날의 비', 'La pluie de Chilseok', 'The rain of Chilseok'), [
    [S('견우와 직녀는 오작교에서 만나서 기쁨의 눈물을 흘렸어요.', 'Gyeonu et Jiknyeo se retrouvèrent sur le pont et versèrent des larmes de joie.', 'Gyeonu and Jiknyeo met on the bridge and shed tears of joy.'),
     S('그래서 지금도 칠석날에는 비가 자주 와요.', 'C’est pourquoi, aujourd’hui encore, il pleut souvent le jour de Chilseok.', 'That is why, even today, it often rains on Chilseok.'),
     S('「칠석날의 비는 견우와 직녀의 눈물이에요.」 사람들은 이렇게 말해요.', '« La pluie de Chilseok, ce sont les larmes de Gyeonu et Jiknyeo », dit-on.', '“The rain on Chilseok is Gyeonu and Jiknyeo’s tears,” people say.')],
    [S('그리고 칠석이 지나면 까치의 머리에 털이 조금 없어요.', 'Et après Chilseok, les pies ont un peu moins de plumes sur la tête.', 'And after Chilseok, magpies have fewer feathers on their heads.'),
     S('견우와 직녀가 다리를 건널 때 새들의 머리를 밟았기 때문이에요.', 'C’est parce que Gyeonu et Jiknyeo leur ont marché sur la tête en traversant le pont.', 'It is because Gyeonu and Jiknyeo stepped on the birds’ heads as they crossed the bridge.')],
  ], [
    W('기쁨', 'gippeum', 'joie', 'joy'),
    W('흘리다', 'heullida', 'verser (des larmes)', 'to shed (tears)'),
    W('자주', 'jaju', 'souvent', 'often'),
    W('밟다', 'balda', 'marcher sur', 'to step on'),
    W('때문', 'ttaemun', 'à cause de, parce que', 'because of'),
    W('까치', 'kkachi', 'pie', 'magpie'),
  ], [
    Q(('Pourquoi pleut-il souvent le jour de Chilseok ?', 'Why does it often rain on Chilseok?'), [('Ce sont les larmes du couple', 'It is the couple’s tears'), ('C’est la saison des moussons', 'It is the monsoon season'), ('Les pies se baignent', 'The magpies are bathing')], 0),
    Q(('Pourquoi les pies ont-elles peu de plumes sur la tête ?', 'Why do magpies have few feathers on their heads?'), [('Elles sont vieilles', 'They are old'), ('Le couple leur a marché sur la tête', 'The couple stepped on their heads'), ('Il fait froid', 'It is cold')], 1),
  ]),
])

# ═════════════════════════ 토끼와 자라 (TOPIK 2) ═════════════════════════
TOKKI = STORY('tokki-jara', '토', 'TOPIK2', '#3FA7A0', ('토끼와 자라', 'Le Lapin et la Tortue d’eau', 'The Rabbit and the Terrapin'),
  ('Le Roi Dragon a besoin d’un foie de lapin pour guérir. Un lapin rusé saura-t-il sauver sa peau ?', 'The Dragon King needs a rabbit’s liver to be cured. Will a clever rabbit manage to save its skin?'), [
  CH('tokki-jara-1', ('병든 용왕', 'Le Roi Dragon malade', 'The sick Dragon King'), [
    [S('옛날 바닷속 용궁에 용왕이 살았어요.', 'Il était une fois un Roi Dragon qui vivait dans son palais, au fond de la mer.', 'Long ago, a Dragon King lived in his palace under the sea.'),
     S('어느 날 용왕이 큰 병에 걸렸어요.', 'Un jour, le Roi Dragon tomba gravement malade.', 'One day, the Dragon King fell seriously ill.'),
     S('의사가 말했어요. 「토끼의 간을 먹으면 나을 수 있습니다.」', 'Le médecin déclara : « Si vous mangez le foie d’un lapin, vous pourrez guérir. »', 'The doctor said: “If you eat a rabbit’s liver, you can be cured.”')],
    [S('하지만 바닷속에는 토끼가 없었어요.', 'Mais il n’y avait aucun lapin au fond de la mer.', 'But there were no rabbits under the sea.'),
     S('그때 충성스러운 자라가 나섰어요.', 'C’est alors qu’une fidèle tortue d’eau s’avança.', 'Then a loyal terrapin stepped forward.'),
     S('「제가 육지에 가서 토끼를 데려오겠습니다!」', '« J’irai sur la terre ferme et je vous ramènerai un lapin ! »', '“I will go on land and bring back a rabbit!”')],
  ], [
    W('용궁', 'yonggung', 'palais du Dragon', 'Dragon Palace'),
    W('병', 'byeong', 'maladie', 'illness'),
    W('간', 'gan', 'foie', 'liver'),
    W('낫다', 'natda', 'guérir', 'to get better'),
    W('자라', 'jara', 'tortue d’eau douce', 'terrapin'),
    W('육지', 'yukji', 'terre ferme', 'dry land'),
  ], [
    Q(('Que faut-il pour guérir le roi ?', 'What is needed to cure the king?'), [('Le foie d’un lapin', 'A rabbit’s liver'), ('Une perle', 'A pearl'), ('Du ginseng', 'Ginseng')], 0),
    Q(('Qui part chercher le lapin ?', 'Who goes to fetch the rabbit?'), [('Le médecin', 'The doctor'), ('La tortue d’eau', 'The terrapin'), ('Le roi lui-même', 'The king himself')], 1),
  ]),
  CH('tokki-jara-2', ('용궁에 가요', 'Direction le palais', 'Off to the palace'), [
    [S('자라는 산에서 토끼를 만났어요.', 'Dans la montagne, la tortue rencontra un lapin.', 'In the mountains, the terrapin met a rabbit.'),
     S('「토끼님, 용궁에 가면 맛있는 음식도 많고 높은 벼슬도 받을 수 있어요.」', '« Monsieur Lapin, au palais du Dragon, il y a plein de bonnes choses à manger, et vous pourriez recevoir un titre important. »', '“Mr Rabbit, at the Dragon Palace there is lots of delicious food, and you could be given a high rank.”'),
     S('토끼는 그 말에 마음이 흔들렸어요.', 'Ces paroles firent hésiter le lapin.', 'The rabbit was tempted by these words.')],
    [S('토끼는 자라의 등에 타고 바닷속으로 들어갔어요.', 'Le lapin monta sur le dos de la tortue et plongea dans la mer.', 'The rabbit climbed onto the terrapin’s back and went down into the sea.'),
     S('용궁은 아주 크고 아름다웠어요.', 'Le palais du Dragon était immense et magnifique.', 'The Dragon Palace was huge and beautiful.')],
  ], [
    W('음식', 'eumsik', 'nourriture', 'food'),
    W('벼슬', 'byeoseul', 'titre, rang officiel', 'official rank'),
    W('흔들리다', 'heundeullida', 'être ébranlé, hésiter', 'to waver'),
    W('등', 'deung', 'dos', 'back'),
    W('아름답다', 'areumdapda', 'être beau', 'to be beautiful'),
    W('바닷속', 'badatsok', 'le fond de la mer', 'under the sea'),
  ], [
    Q(('Que promet la tortue au lapin ?', 'What does the terrapin promise the rabbit?'), [('De la bonne nourriture et un titre', 'Good food and a title'), ('De l’or', 'Gold'), ('Une maison', 'A house')], 0),
    Q(('Comment le lapin va-t-il sous la mer ?', 'How does the rabbit get under the sea?'), [('Il nage', 'He swims'), ('Sur le dos de la tortue', 'On the terrapin’s back'), ('En bateau', 'By boat')], 1),
  ]),
  CH('tokki-jara-3', ('간을 두고 왔어요', 'J’ai laissé mon foie là-haut', 'I left my liver behind'), [
    [S('그런데 용왕이 말했어요. 「토끼야, 미안하지만 네 간을 줘야겠다.」', 'Mais le Roi Dragon déclara : « Lapin, je suis désolé, mais il me faut ton foie. »', 'But the Dragon King said: “Rabbit, I’m sorry, but I must have your liver.”'),
     S('토끼는 깜짝 놀랐어요. 하지만 침착하게 생각했어요.', 'Le lapin sursauta. Mais il réfléchit calmement.', 'The rabbit was startled. But it thought calmly.'),
     S('「아이고, 용왕님! 제 간은 너무 귀해서 산속 바위 밑에 숨겨 두고 왔어요.」', '« Oh, Majesté ! Mon foie est si précieux que je l’ai caché sous un rocher, dans la montagne. »', '“Oh, Your Majesty! My liver is so precious that I hid it under a rock in the mountains.”')],
    [S('「간을 가지고 오겠습니다. 저를 다시 보내 주세요.」', '« Je vais aller le chercher. Laissez-moi repartir. »', '“I will fetch it for you. Please send me back.”'),
     S('용왕은 토끼의 말을 믿었어요.', 'Le Roi Dragon crut le lapin.', 'The Dragon King believed the rabbit.')],
  ], [
    W('깜짝 놀라다', 'kkamjjak nollada', 'sursauter, être très surpris', 'to be startled'),
    W('침착하다', 'chimchakhada', 'être calme, garder son sang-froid', 'to be calm'),
    W('귀하다', 'gwihada', 'être précieux', 'to be precious'),
    W('바위', 'bawi', 'rocher', 'rock'),
    W('숨기다', 'sumgida', 'cacher', 'to hide'),
    W('믿다', 'mitda', 'croire', 'to believe'),
  ], [
    Q(('Qu’apprend le lapin au palais ?', 'What does the rabbit learn at the palace?'), [('Le roi veut son foie', 'The king wants his liver'), ('Il va devenir roi', 'He will become king'), ('Il peut rester pour toujours', 'He can stay forever')], 0),
    Q(('Où le lapin dit-il avoir laissé son foie ?', 'Where does the rabbit say he left his liver?'), [('Dans la mer', 'In the sea'), ('Sous un rocher dans la montagne', 'Under a rock in the mountains'), ('Chez le médecin', 'At the doctor’s')], 1),
  ]),
  CH('tokki-jara-4', ('꾀 많은 토끼', 'Le lapin plein de ruse', 'The clever rabbit'), [
    [S('자라는 다시 토끼를 등에 태우고 육지로 갔어요.', 'La tortue reprit le lapin sur son dos et retourna sur la terre ferme.', 'The terrapin carried the rabbit on its back and went back to land.'),
     S('육지에 도착했어요. 토끼는 깡충 뛰어내려서 말했어요.', 'Arrivé sur la rive, le lapin sauta à terre d’un bond et dit :', 'When they reached land, the rabbit hopped off and said:'),
     S('「바보 같은 자라야! 간을 빼놓고 다니는 동물이 어디 있니?」', '« Tortue naïve ! Où as-tu vu un animal qui se promène sans son foie ? »', '“Silly terrapin! Where have you ever seen an animal that goes about without its liver?”')],
    [S('자라는 아무것도 하지 못하고 혼자 바다로 돌아갔어요.', 'La tortue, impuissante, rentra seule dans la mer.', 'The terrapin could do nothing and went back to the sea alone.'),
     S('지혜로운 토끼는 위험한 순간에도 침착해서 살 수 있었어요.', 'Le lapin, plein de sagesse, avait gardé son calme face au danger : il avait sauvé sa vie.', 'The wise rabbit stayed calm even in danger, and so it saved its life.')],
  ], [
    W('태우다', 'taeuda', 'faire monter (sur un véhicule, sur son dos)', 'to give a ride'),
    W('도착하다', 'dochakhada', 'arriver', 'to arrive'),
    W('바보', 'babo', 'idiot, naïf', 'fool'),
    W('지혜롭다', 'jihyeropda', 'être sage, avisé', 'to be wise'),
    W('위험하다', 'wiheomhada', 'être dangereux', 'to be dangerous'),
    W('깡충', 'kkangchung', 'd’un bond (en sautillant)', 'with a hop'),
  ], [
    Q(('Que fait le lapin une fois sur la terre ferme ?', 'What does the rabbit do once on land?'), [('Il va chercher son foie', 'He goes to fetch his liver'), ('Il s’enfuit en se moquant de la tortue', 'He runs off, laughing at the terrapin'), ('Il s’endort', 'He falls asleep')], 1),
    Q(('Quelle est la leçon du conte ?', 'What is the moral of the tale?'), [('Garder son calme face au danger', 'Stay calm in the face of danger'), ('Toujours obéir au roi', 'Always obey the king'), ('Ne jamais voyager', 'Never travel')], 0),
  ]),
])

# ═════════════════════════ 선녀와 나무꾼 (TOPIK 2) ═════════════════════════
SEONNYEO = STORY('seonnyeo-namukkun', '선', 'TOPIK2', '#8E5BA8', ('선녀와 나무꾼', 'La Fée et le Bûcheron', 'The Fairy and the Woodcutter'),
  ('Un bûcheron au grand cœur sauve un cerf, qui lui révèle où se baignent les fées du ciel…', 'A kind-hearted woodcutter saves a deer, which tells him where the fairies of heaven come to bathe…'), [
  CH('seonnyeo-namukkun-1', ('사슴을 구해 준 나무꾼', 'Le bûcheron qui sauva un cerf', 'The woodcutter who saved a deer'), [
    [S('옛날 어느 산골 마을에 마음이 착한 나무꾼이 살았어요.', 'Il était une fois, dans un village de montagne, un bûcheron au cœur bon.', 'Once upon a time, in a mountain village, there lived a kind-hearted woodcutter.'),
     S('나무꾼은 매일 산에 가서 나무를 했어요.', 'Chaque jour, il allait dans la montagne couper du bois.', 'Every day he went into the mountains to cut wood.'),
     S('어느 날 나무를 하고 있을 때 사슴 한 마리가 뛰어왔어요.', 'Un jour, alors qu’il coupait du bois, un cerf accourut vers lui.', 'One day, while he was cutting wood, a deer came running up to him.')],
    [S('「나무꾼님, 사냥꾼이 저를 쫓아오고 있어요. 저를 좀 숨겨 주세요!」', '« Bûcheron, un chasseur me poursuit. Cachez-moi, je vous en prie ! »', '“Woodcutter, a hunter is chasing me. Please hide me!”'),
     S('나무꾼은 사슴을 나무 뒤에 숨겨 주었어요.', 'Le bûcheron cacha le cerf derrière un tas de bois.', 'The woodcutter hid the deer behind the woodpile.'),
     S('사냥꾼이 와서 물었지만 나무꾼은 「저쪽으로 갔어요.」라고 말했어요.', 'Le chasseur arriva et l’interrogea, mais le bûcheron répondit : « Il est parti par là-bas. »', 'The hunter came and asked, but the woodcutter said: “It went that way.”')],
  ], [
    W('나무꾼', 'namukkun', 'bûcheron', 'woodcutter'),
    W('착하다', 'chakada', 'être bon, gentil', 'to be kind-hearted'),
    W('사슴', 'saseum', 'cerf', 'deer'),
    W('사냥꾼', 'sanyangkkun', 'chasseur', 'hunter'),
    W('쫓아오다', 'jjochaoda', 'poursuivre', 'to chase'),
    W('숨기다', 'sumgida', 'cacher', 'to hide'),
  ], [
    Q(('Que faisait le bûcheron quand le cerf est arrivé ?', 'What was the woodcutter doing when the deer arrived?'), [('Il coupait du bois', 'He was cutting wood'), ('Il dormait', 'He was sleeping'), ('Il chassait', 'He was hunting')], 0),
    Q(('Comment le bûcheron aide-t-il le cerf ?', 'How does the woodcutter help the deer?'), [('Il le soigne', 'He treats its wounds'), ('Il le cache et trompe le chasseur', 'He hides it and misleads the hunter'), ('Il l’emmène chez lui', 'He takes it home')], 1),
  ]),
  CH('seonnyeo-namukkun-2', ('하늘에서 내려온 선녀', 'Les fées descendues du ciel', 'The fairies who came down from heaven'), [
    [S('사슴은 고마워서 나무꾼에게 비밀을 알려 주었어요.', 'Reconnaissant, le cerf confia un secret au bûcheron.', 'Out of gratitude, the deer told the woodcutter a secret.'),
     S('「보름달이 뜨는 밤에 선녀들이 산속 연못에 목욕하러 내려와요.」', '« Les nuits de pleine lune, les fées descendent se baigner dans l’étang de la montagne. »', '“On full-moon nights, the fairies come down to bathe in the mountain pond.”'),
     S('「선녀의 날개옷을 숨기면 선녀와 결혼할 수 있어요. 하지만 아이를 셋 낳기 전에는 옷을 돌려주면 안 돼요.」', '« Si vous cachez la robe ailée d’une fée, vous pourrez l’épouser. Mais il ne faut pas lui rendre sa robe avant qu’elle ait eu trois enfants. »', '“If you hide a fairy’s winged robe, you can marry her. But you must not give the robe back before she has had three children.”')],
    [S('보름달이 뜬 밤, 나무꾼은 연못에 가서 날개옷 하나를 숨겼어요.', 'La nuit de pleine lune, le bûcheron se rendit à l’étang et cacha une des robes ailées.', 'On the full-moon night, the woodcutter went to the pond and hid one of the winged robes.'),
     S('다른 선녀들은 하늘로 올라갔지만, 막내 선녀는 올라갈 수 없었어요.', 'Les autres fées remontèrent au ciel, mais la plus jeune ne put pas s’envoler.', 'The other fairies flew back up to heaven, but the youngest could not.')],
  ], [
    W('비밀', 'bimil', 'secret', 'secret'),
    W('보름달', 'boreumdal', 'pleine lune', 'full moon'),
    W('선녀', 'seonnyeo', 'fée céleste', 'heavenly fairy'),
    W('연못', 'yeonmot', 'étang', 'pond'),
    W('날개옷', 'nalgaeot', 'robe ailée', 'winged robe'),
    W('막내', 'mangnae', 'le plus jeune, cadet', 'the youngest'),
  ], [
    Q(('Quand les fées descendent-elles à l’étang ?', 'When do the fairies come down to the pond?'), [('Les nuits de pleine lune', 'On full-moon nights'), ('Tous les matins', 'Every morning'), ('Au Nouvel An', 'At New Year')], 0),
    Q(('Que ne faut-il pas faire, selon le cerf ?', 'According to the deer, what must not be done?'), [('Parler aux fées', 'Talk to the fairies'), ('Rendre la robe avant le troisième enfant', 'Give the robe back before the third child'), ('Aller à l’étang', 'Go to the pond')], 1),
  ]),
  CH('seonnyeo-namukkun-3', ('날개옷을 돌려준 나무꾼', 'Le bûcheron rend la robe ailée', 'The woodcutter gives back the robe'), [
    [S('나무꾼과 선녀는 결혼해서 행복하게 살았어요. 아이도 둘 낳았어요.', 'Le bûcheron et la fée se marièrent et vécurent heureux. Ils eurent deux enfants.', 'The woodcutter and the fairy married and lived happily. They had two children.'),
     S('하지만 선녀는 보름달을 볼 때마다 하늘을 그리워했어요.', 'Mais chaque fois qu’elle voyait la pleine lune, la fée regrettait le ciel.', 'But every time she saw the full moon, the fairy longed for heaven.'),
     S('「날개옷을 한 번만 보여 주세요. 입어 보고 싶어요.」', '« Montrez-moi ma robe ailée, rien qu’une fois. J’aimerais la passer. »', '“Show me my winged robe, just once. I would like to try it on.”')],
    [S('나무꾼은 선녀가 불쌍해서 날개옷을 꺼내 주었어요.', 'Ému par sa tristesse, le bûcheron sortit la robe ailée et la lui donna.', 'Feeling sorry for her, the woodcutter took out the winged robe and gave it to her.'),
     S('선녀는 날개옷을 입자마자 두 아이를 안고 하늘로 날아갔어요.', 'À peine l’eut-elle enfilée que la fée prit ses deux enfants dans ses bras et s’envola vers le ciel.', 'As soon as she put it on, the fairy took her two children in her arms and flew up to heaven.')],
  ], [
    W('결혼하다', 'gyeolhonhada', 'se marier', 'to get married'),
    W('행복하다', 'haengbokada', 'être heureux', 'to be happy'),
    W('그리워하다', 'geuriwohada', 'regretter, avoir la nostalgie de', 'to long for'),
    W('불쌍하다', 'bulssanghada', 'être à plaindre, faire pitié', 'to be pitiful'),
    W('꺼내다', 'kkeonaeda', 'sortir (un objet)', 'to take out'),
    W('안다', 'anda', 'prendre dans ses bras', 'to hold in one’s arms'),
  ], [
    Q(('Combien d’enfants ont-ils quand le bûcheron rend la robe ?', 'How many children do they have when the woodcutter gives back the robe?'), [('Un', 'One'), ('Deux', 'Two'), ('Trois', 'Three')], 1),
    Q(('Pourquoi le bûcheron rend-il la robe ?', 'Why does the woodcutter give back the robe?'), [('Parce que la fée lui fait pitié', 'Because he feels sorry for the fairy'), ('Parce que le cerf le lui a dit', 'Because the deer told him to'), ('Parce qu’il veut aller au ciel', 'Because he wants to go to heaven')], 0),
  ]),
  CH('seonnyeo-namukkun-4', ('하늘로 올라간 나무꾼', 'Le bûcheron monte au ciel', 'The woodcutter goes up to heaven'), [
    [S('나무꾼이 슬퍼서 울고 있을 때 사슴이 다시 찾아왔어요.', 'Alors que le bûcheron pleurait de chagrin, le cerf revint le trouver.', 'While the woodcutter was weeping with grief, the deer came to see him again.'),
     S('「이제 선녀들은 연못에 내려오지 않아요. 대신 하늘에서 두레박을 내려서 물을 길어요.」', '« Désormais, les fées ne descendent plus à l’étang. À la place, elles font descendre un seau depuis le ciel pour puiser l’eau. »', '“Now the fairies no longer come down to the pond. Instead, they lower a bucket from heaven to draw water.”'),
     S('「그 두레박을 타면 하늘에 올라갈 수 있을 거예요.」', '« Si vous montez dans ce seau, vous pourrez sans doute monter au ciel. »', '“If you ride in that bucket, you should be able to go up to heaven.”')],
    [S('나무꾼은 두레박을 타고 하늘나라에 올라갔어요.', 'Le bûcheron monta dans le seau et gagna le royaume céleste.', 'The woodcutter rode the bucket up to the kingdom of heaven.'),
     S('그리고 하늘나라에서 선녀와 아이들을 다시 만나서 함께 행복하게 살았어요.', 'Là-haut, il retrouva la fée et leurs enfants, et ils vécurent heureux ensemble.', 'There he found the fairy and their children again, and they lived happily together.')],
  ], [
    W('슬프다', 'seulpeuda', 'être triste', 'to be sad'),
    W('울다', 'ulda', 'pleurer', 'to cry'),
    W('대신', 'daesin', 'à la place', 'instead'),
    W('두레박', 'durebak', 'seau de puits', 'well bucket'),
    W('물을 긷다', 'mureul gitda', 'puiser de l’eau', 'to draw water'),
    W('하늘나라', 'haneullara', 'royaume céleste', 'kingdom of heaven'),
  ], [
    Q(('Comment le bûcheron monte-t-il au ciel ?', 'How does the woodcutter go up to heaven?'), [('Avec la robe ailée', 'With the winged robe'), ('Dans le seau qui puise l’eau', 'In the bucket used to draw water'), ('Sur le dos du cerf', 'On the deer’s back')], 1),
    Q(('Comment se termine le conte ?', 'How does the tale end?'), [('La famille est réunie au ciel', 'The family is reunited in heaven'), ('Le bûcheron reste seul', 'The woodcutter stays alone'), ('La fée redescend sur terre', 'The fairy comes back down to earth')], 0),
  ]),
])

# ═════════════════════════ 춘향전 (TOPIK 3) ═════════════════════════
CHUNHYANG = STORY('chunhyang', '춘', 'TOPIK3', '#B5562E', ('춘향전', 'Le Dit de Chunhyang', 'The Tale of Chunhyang'),
  ('À Namwon, la fidèle Chunhyang tient tête à un préfet cruel en attendant son bien-aimé, parti passer le grand concours.', 'In Namwon, faithful Chunhyang stands up to a cruel prefect while waiting for her beloved, who has gone to sit the great state examination.'), [
  CH('chunhyang-1', ('그네 타는 춘향', 'Chunhyang sur la balançoire', 'Chunhyang on the swing'), [
    [S('조선 시대 남원에 춘향이라는 아름다운 처녀가 살았어요.', 'À l’époque Joseon vivait à Namwon une belle jeune fille nommée Chunhyang.', 'In the Joseon era, a beautiful young woman named Chunhyang lived in Namwon.'),
     S('단옷날, 춘향은 광한루 근처에서 그네를 타고 있었어요.', 'Le jour de la fête de Dano, Chunhyang se balançait près du pavillon Gwanghallu.', 'On the day of the Dano festival, Chunhyang was riding a swing near the Gwanghallu pavilion.'),
     S('마침 그곳에 놀러 온 원님의 아들 이몽룡이 춘향을 보자마자 첫눈에 반했어요.', 'Lee Mongryong, le fils du magistrat, venu s’y promener, tomba amoureux d’elle au premier regard.', 'Lee Mongryong, the magistrate’s son, who had come there for an outing, fell for her at first sight.')],
    [S('몽룡은 하인 방자에게 춘향을 데려오라고 했어요.', 'Mongryong ordonna à son serviteur Bangja d’aller chercher Chunhyang.', 'Mongryong told his servant Bangja to bring Chunhyang to him.'),
     S('두 사람은 이야기를 나누면서 서로 사랑하게 되었고, 몰래 혼인을 약속했어요.', 'En parlant, ils tombèrent amoureux l’un de l’autre et se promirent secrètement le mariage.', 'As they talked, they came to love each other and secretly promised to marry.')],
  ], [
    W('처녀', 'cheonyeo', 'jeune fille', 'maiden'),
    W('단옷날', 'danonnal', 'jour de la fête de Dano', 'Dano festival day'),
    W('그네를 타다', 'geuneureul tada', 'faire de la balançoire', 'to ride a swing'),
    W('첫눈에 반하다', 'cheonnune banhada', 'tomber amoureux au premier regard', 'to fall in love at first sight'),
    W('하인', 'hain', 'serviteur', 'servant'),
    W('혼인', 'honin', 'mariage', 'marriage'),
  ], [
    Q(('Où Mongryong voit-il Chunhyang pour la première fois ?', 'Where does Mongryong first see Chunhyang?'), [('Près du pavillon Gwanghallu, sur une balançoire', 'Near the Gwanghallu pavilion, on a swing'), ('Au marché', 'At the market'), ('À Hanyang', 'In Hanyang')], 0),
    Q(('Que se promettent-ils ?', 'What do they promise each other?'), [('De partir en voyage', 'To go travelling'), ('De se marier', 'To marry'), ('De ne jamais se revoir', 'Never to meet again')], 1),
  ]),
  CH('chunhyang-2', ('한양으로 떠난 몽룡', 'Mongryong part pour Hanyang', 'Mongryong leaves for Hanyang'), [
    [S('그런데 얼마 후 몽룡의 아버지가 한양으로 가게 되었어요.', 'Mais peu après, le père de Mongryong fut appelé à Hanyang.', 'But soon afterwards, Mongryong’s father was posted to Hanyang.'),
     S('몽룡도 아버지를 따라 떠나야 했어요.', 'Mongryong dut suivre son père.', 'Mongryong had to leave with his father.'),
     S('「과거 시험에 합격하면 꼭 너를 데리러 올게.」', '« Quand j’aurai réussi le grand concours, je reviendrai te chercher, c’est promis. »', '“When I pass the state examination, I will come back for you, I promise.”')],
    [S('춘향은 눈물을 흘리면서 몽룡에게 거울을 주었고, 몽룡은 춘향에게 옥가락지를 주었어요.', 'En larmes, Chunhyang donna un miroir à Mongryong, et lui offrit à Chunhyang une bague de jade.', 'In tears, Chunhyang gave Mongryong a mirror, and he gave her a jade ring.'),
     S('그 후로 춘향은 매일 몽룡을 기다렸어요.', 'Dès lors, Chunhyang attendit Mongryong chaque jour.', 'From then on, Chunhyang waited for Mongryong every day.')],
  ], [
    W('따르다', 'ttareuda', 'suivre', 'to follow'),
    W('과거 시험', 'gwageo siheom', 'concours de la fonction publique', 'state examination'),
    W('합격하다', 'hapgyeokada', 'réussir (un examen)', 'to pass (an exam)'),
    W('눈물을 흘리다', 'nunmureul heullida', 'verser des larmes', 'to shed tears'),
    W('거울', 'geoul', 'miroir', 'mirror'),
    W('옥가락지', 'okgarakji', 'bague de jade', 'jade ring'),
  ], [
    Q(('Pourquoi Mongryong part-il ?', 'Why does Mongryong leave?'), [('Son père est envoyé à Hanyang', 'His father is sent to Hanyang'), ('Il se dispute avec Chunhyang', 'He quarrels with Chunhyang'), ('Il part à la guerre', 'He goes to war')], 0),
    Q(('Que reçoit Chunhyang en souvenir ?', 'What does Chunhyang receive as a keepsake?'), [('Un miroir', 'A mirror'), ('Une bague de jade', 'A jade ring'), ('Un éventail', 'A fan')], 1),
  ]),
  CH('chunhyang-3', ('변 사또의 욕심', 'La cupidité du préfet Byeon', 'Prefect Byeon’s greed'), [
    [S('새로 온 원님 변학도는 욕심이 많고 나쁜 사람이었어요.', 'Le nouveau magistrat, Byeon Hakdo, était un homme cupide et mauvais.', 'The new magistrate, Byeon Hakdo, was a greedy, wicked man.'),
     S('변학도는 춘향이 아름답다는 소문을 듣고 자기의 사람이 되라고 했어요.', 'Ayant entendu dire que Chunhyang était belle, Byeon Hakdo lui ordonna de devenir sienne.', 'Having heard that Chunhyang was beautiful, Byeon Hakdo ordered her to become his.'),
     S('하지만 춘향은 「저는 이미 혼인을 약속한 사람이 있습니다.」라고 대답했어요.', 'Mais Chunhyang répondit : « Je suis déjà promise à quelqu’un. »', 'But Chunhyang answered: “I am already promised to someone.”')],
    [S('화가 난 변학도는 춘향을 감옥에 가두었어요.', 'Furieux, Byeon Hakdo la fit jeter en prison.', 'In a rage, Byeon Hakdo had her thrown into prison.'),
     S('춘향은 매를 맞으면서도 마음을 바꾸지 않았어요.', 'Même sous les coups de bâton, Chunhyang ne changea pas d’avis.', 'Even when she was beaten, Chunhyang did not change her mind.')],
  ], [
    W('욕심', 'yoksim', 'cupidité, avidité', 'greed'),
    W('사또', 'satto', 'magistrat (titre populaire)', 'magistrate (popular title)'),
    W('가두다', 'gaduda', 'enfermer', 'to lock up'),
    W('화가 나다', 'hwaga nada', 'se mettre en colère', 'to get angry'),
    W('매를 맞다', 'maereul matda', 'recevoir des coups de bâton', 'to be beaten'),
    W('마음을 바꾸다', 'maeumeul bakkuda', 'changer d’avis', 'to change one’s mind'),
  ], [
    Q(('Que demande Byeon Hakdo à Chunhyang ?', 'What does Byeon Hakdo demand of Chunhyang?'), [('De devenir sienne', 'That she become his'), ('De payer un impôt', 'That she pay a tax'), ('De quitter Namwon', 'That she leave Namwon')], 0),
    Q(('Comment réagit Chunhyang en prison ?', 'How does Chunhyang react in prison?'), [('Elle accepte', 'She gives in'), ('Elle reste fidèle à Mongryong', 'She stays faithful to Mongryong'), ('Elle s’enfuit', 'She escapes')], 1),
  ]),
  CH('chunhyang-4', ('암행어사 출두요!', '« Voici l’inspecteur royal ! »', '“Make way for the royal inspector!”'), [
    [S('한편 몽룡은 과거 시험에 장원으로 합격해서 암행어사가 되었어요.', 'Pendant ce temps, Mongryong réussit le concours en tête et devint inspecteur royal secret.', 'Meanwhile, Mongryong passed the examination in first place and became a secret royal inspector.'),
     S('그는 거지처럼 낡은 옷을 입고 남원에 돌아왔어요.', 'Il revint à Namwon vêtu de haillons, comme un mendiant.', 'He returned to Namwon dressed in rags, like a beggar.'),
     S('마침 변학도의 생일 잔치가 열리고 있었어요.', 'Justement, on célébrait l’anniversaire de Byeon Hakdo par un grand banquet.', 'As it happened, Byeon Hakdo’s birthday banquet was under way.')],
    [S('「암행어사 출두요!」 소리가 들리자 잔치는 엉망이 되었어요.', 'Au cri de « Voici l’inspecteur royal ! », le banquet tourna à la débandade.', 'At the cry of “Make way for the royal inspector!”, the banquet fell into chaos.'),
     S('몽룡은 변학도를 벌하고 춘향을 감옥에서 구했어요. 두 사람은 한양으로 가서 행복하게 살았어요.', 'Mongryong punit Byeon Hakdo et délivra Chunhyang. Tous deux partirent pour Hanyang et vécurent heureux.', 'Mongryong punished Byeon Hakdo and rescued Chunhyang from prison. The two went to Hanyang and lived happily.')],
  ], [
    W('장원', 'jangwon', 'premier reçu (au concours)', 'top candidate'),
    W('거지', 'geoji', 'mendiant', 'beggar'),
    W('낡다', 'nakda', 'être usé, vieux', 'to be worn out'),
    W('잔치', 'janchi', 'banquet, fête', 'feast, banquet'),
    W('출두', 'chuldu', 'comparution, apparition (officielle)', 'official appearance'),
    W('벌하다', 'beolhada', 'punir', 'to punish'),
  ], [
    Q(('Comment Mongryong revient-il à Namwon ?', 'How does Mongryong return to Namwon?'), [('Déguisé en mendiant', 'Disguised as a beggar'), ('Avec une grande armée', 'With a great army'), ('En habit de magistrat', 'In magistrate’s robes')], 0),
    Q(('Que se passe-t-il pendant le banquet ?', 'What happens during the banquet?'), [('Byeon Hakdo devient roi', 'Byeon Hakdo becomes king'), ('L’inspecteur royal apparaît et punit Byeon Hakdo', 'The royal inspector appears and punishes Byeon Hakdo'), ('Chunhyang chante', 'Chunhyang sings')], 1),
  ]),
])

# ═════════════════════════ 홍길동전 (TOPIK 4) ═════════════════════════
HONGGILDONG = STORY('hong-gildong', '홍', 'TOPIK4', '#3E5C8A', ('홍길동전', 'Le Dit de Hong Gildong', 'The Tale of Hong Gildong'),
  ('Fils d’un ministre mais né d’une servante, Hong Gildong ne peut ni appeler son père « père », ni servir l’État. Il devient le chef de bandits justiciers qui volent les riches corrompus.', 'The son of a minister but born to a servant, Hong Gildong may neither call his father “father” nor serve the state. He becomes the leader of righteous outlaws who rob corrupt officials.'), [
  CH('hong-gildong-1', ('아버지를 아버지라 부르지 못하고', 'Ne pas pouvoir appeler son père « père »', 'Not allowed to call his father “father”'), [
    [S('조선 시대에 홍 판서의 아들 홍길동이 태어났어요.', 'À l’époque Joseon naquit Hong Gildong, fils du ministre Hong.', 'In the Joseon era, Hong Gildong was born, the son of Minister Hong.'),
     S('길동은 어릴 때부터 머리가 좋고 무술도 잘했지만, 어머니가 하녀였던 탓에 서자로 차별을 받았어요.', 'Dès l’enfance, Gildong était brillant et excellait aux arts martiaux, mais parce que sa mère était servante, il subissait le mépris réservé aux fils illégitimes.', 'From childhood Gildong was clever and skilled in martial arts, but because his mother was a maid he was discriminated against as an illegitimate son.'),
     S('그는 아버지를 아버지라 부르지 못하고, 형을 형이라 부르지 못했어요.', 'Il ne pouvait appeler son père « père », ni son frère « grand frère ».', 'He could not call his father “father”, nor his brother “big brother”.')],
    [S('「아무리 노력하더라도 저는 벼슬을 할 수 없겠지요.」', '« J’aurai beau faire des efforts, je ne pourrai jamais devenir fonctionnaire. »', '“However hard I try, I will never be able to hold office.”'),
     S('길동은 결국 집을 떠나기로 결심했어요.', 'Gildong finit par décider de quitter la maison.', 'In the end, Gildong made up his mind to leave home.')],
  ], [
    W('판서', 'panseo', 'ministre (Joseon)', 'minister (Joseon)'),
    W('무술', 'musul', 'arts martiaux', 'martial arts'),
    W('하녀', 'hanyeo', 'servante', 'maid, servant'),
    W('서자', 'seoja', 'fils illégitime (né d’une concubine)', 'illegitimate son'),
    W('차별', 'chabyeol', 'discrimination', 'discrimination'),
    W('벼슬', 'byeoseul', 'charge officielle', 'government post'),
  ], [
    Q(('Pourquoi Gildong est-il traité différemment ?', 'Why is Gildong treated differently?'), [('Sa mère était servante', 'His mother was a maid'), ('Il était paresseux', 'He was lazy'), ('Il était malade', 'He was ill')], 0),
    Q(('Que décide-t-il finalement ?', 'What does he finally decide?'), [('De passer le concours', 'To sit the examination'), ('De quitter la maison', 'To leave home'), ('De se marier', 'To marry')], 1),
  ]),
  CH('hong-gildong-2', ('활빈당의 두목', 'Le chef de la Hwalbindang', 'Leader of the Hwalbindang'), [
    [S('집을 떠난 길동은 산속에서 도적들을 만났어요.', 'Après avoir quitté la maison, Gildong rencontra des brigands dans la montagne.', 'After leaving home, Gildong met a band of outlaws in the mountains.'),
     S('도적들은 커다란 돌을 들어 올리는 사람을 두목으로 삼겠다고 했어요.', 'Les brigands déclarèrent qu’ils prendraient pour chef celui qui soulèverait un énorme rocher.', 'The outlaws said they would make whoever could lift a huge rock their leader.'),
     S('길동은 그 돌을 가볍게 들어 올리고 두목이 되었어요.', 'Gildong souleva le rocher sans effort et devint leur chef.', 'Gildong lifted the rock with ease and became their leader.')],
    [S('길동은 무리의 이름을 「활빈당」이라고 지었어요. 가난한 백성을 살리는 무리라는 뜻이에요.', 'Gildong appela la bande « Hwalbindang », ce qui signifie « la bande qui sauve les pauvres ».', 'Gildong named the band the “Hwalbindang”, meaning “the band that saves the poor”.'),
     S('활빈당은 백성의 재물을 빼앗은 욕심 많은 관리들의 창고만 털었어요.', 'La Hwalbindang ne pillait que les entrepôts des fonctionnaires cupides qui avaient dépouillé le peuple.', 'The Hwalbindang only raided the storehouses of greedy officials who had robbed the people.')],
  ], [
    W('도적', 'dojeok', 'brigand', 'outlaw, bandit'),
    W('두목', 'dumok', 'chef (de bande)', 'leader (of a gang)'),
    W('들어 올리다', 'deureo ollida', 'soulever', 'to lift up'),
    W('무리', 'muri', 'bande, groupe', 'band, group'),
    W('재물', 'jaemul', 'biens, richesses', 'wealth, property'),
    W('창고', 'changgo', 'entrepôt', 'storehouse'),
  ], [
    Q(('Comment Gildong devient-il chef ?', 'How does Gildong become leader?'), [('En soulevant un énorme rocher', 'By lifting a huge rock'), ('En gagnant un combat à l’épée', 'By winning a sword fight'), ('En payant les brigands', 'By paying the outlaws')], 0),
    Q(('Qui la Hwalbindang vole-t-elle ?', 'Whom does the Hwalbindang rob?'), [('Les paysans', 'Farmers'), ('Les fonctionnaires cupides', 'Greedy officials'), ('Les marchands étrangers', 'Foreign merchants')], 1),
  ]),
  CH('hong-gildong-3', ('여덟 명의 길동', 'Huit Gildong', 'Eight Gildongs'), [
    [S('나라에서는 길동을 잡으려고 군사를 보냈지만 소용없었어요.', 'Le royaume envoya des soldats pour capturer Gildong, mais en vain.', 'The kingdom sent soldiers to capture Gildong, but it was no use.'),
     S('길동은 도술을 부려 짚으로 여덟 명의 길동을 만들었어요.', 'Par magie, Gildong fabriqua avec de la paille huit autres Gildong.', 'Using magic, Gildong made eight Gildongs out of straw.'),
     S('여덟 명의 길동이 전국 곳곳에 나타나는 바람에 아무도 진짜 길동을 찾을 수 없었어요.', 'Comme huit Gildong apparaissaient partout dans le pays, personne ne put trouver le vrai.', 'Because eight Gildongs appeared all over the country, no one could find the real one.')],
    [S('결국 왕은 길동의 형에게 길동을 잡아 오라고 명령했어요.', 'Finalement, le roi ordonna au frère aîné de Gildong de le capturer.', 'In the end, the king ordered Gildong’s older brother to bring him in.'),
     S('형이 아버지가 병이 났다는 편지를 보내자 길동은 스스로 잡혀 왔어요.', 'Quand son frère lui écrivit que leur père était tombé malade, Gildong se laissa prendre de lui-même.', 'When his brother wrote that their father had fallen ill, Gildong let himself be caught.')],
  ], [
    W('군사', 'gunsa', 'soldats, troupes', 'soldiers, troops'),
    W('도술', 'dosul', 'magie (taoïste)', 'magic arts'),
    W('짚', 'jip', 'paille', 'straw'),
    W('곳곳', 'gotgot', 'partout, en tous lieux', 'everywhere'),
    W('명령하다', 'myeongnyeonghada', 'ordonner', 'to order'),
    W('스스로', 'seuseuro', 'de soi-même', 'by oneself, of one’s own accord'),
  ], [
    Q(('Pourquoi personne ne trouve-t-il le vrai Gildong ?', 'Why can no one find the real Gildong?'), [('Huit Gildong de paille apparaissent partout', 'Eight straw Gildongs appear everywhere'), ('Il se cache en Chine', 'He hides in China'), ('Il change de nom', 'He changes his name')], 0),
    Q(('Pourquoi Gildong se laisse-t-il capturer ?', 'Why does Gildong let himself be caught?'), [('Il est fatigué', 'He is tired'), ('Son père est malade', 'His father is ill'), ('Le roi lui offre de l’argent', 'The king offers him money')], 1),
  ]),
  CH('hong-gildong-4', ('율도국의 왕', 'Le roi de Yuldo', 'King of Yuldo'), [
    [S('왕은 길동의 재주를 보고 그에게 병조 판서라는 높은 벼슬을 주었어요.', 'Voyant ses talents, le roi lui accorda une haute charge : ministre de la Guerre.', 'Seeing his talents, the king gave him a high post: Minister of War.'),
     S('길동은 왕에게 감사의 인사를 드린 후 무리를 데리고 조선을 떠났어요.', 'Après avoir remercié le roi, Gildong quitta Joseon avec sa bande.', 'After thanking the king, Gildong left Joseon with his band.')],
    [S('그들은 바다 건너 율도국이라는 섬나라에 도착했어요.', 'Ils arrivèrent de l’autre côté de la mer, dans un royaume insulaire nommé Yuldo.', 'They arrived across the sea in an island kingdom called Yuldo.'),
     S('길동은 그곳의 왕이 되어 신분의 차별이 없는 나라를 만들었어요.', 'Gildong en devint le roi et y fonda un pays sans discrimination de naissance.', 'Gildong became its king and built a country without discrimination by birth.'),
     S('사람들은 지금도 홍길동을 정의로운 영웅으로 기억하고 있어요.', 'Aujourd’hui encore, on se souvient de Hong Gildong comme d’un héros juste.', 'People still remember Hong Gildong as a righteous hero.')],
  ], [
    W('재주', 'jaeju', 'talent', 'talent'),
    W('병조 판서', 'byeongjo panseo', 'ministre de la Guerre', 'Minister of War'),
    W('섬나라', 'seomnara', 'pays insulaire', 'island country'),
    W('신분', 'sinbun', 'rang social, condition', 'social status'),
    W('정의롭다', 'jeonguiropda', 'être juste', 'to be righteous'),
    W('영웅', 'yeongung', 'héros', 'hero'),
  ], [
    Q(('Quelle charge le roi donne-t-il à Gildong ?', 'What post does the king give Gildong?'), [('Ministre de la Guerre', 'Minister of War'), ('Magistrat de Namwon', 'Magistrate of Namwon'), ('Historien royal', 'Royal historian')], 0),
    Q(('Quel pays Gildong fonde-t-il à Yuldo ?', 'What kind of country does Gildong build in Yuldo?'), [('Un pays sans roi', 'A country without a king'), ('Un pays sans discrimination de naissance', 'A country without discrimination by birth'), ('Un pays de brigands', 'A country of outlaws')], 1),
  ]),
])

# ═════════════════════════ 바리공주 (TOPIK 5) ═════════════════════════
BARI = STORY('bari-gongju', '바', 'TOPIK5', '#6A4C93', ('바리공주', 'La Princesse Bari', 'Princess Bari'),
  ('Abandonnée à la naissance parce qu’elle n’était pas un fils, la septième princesse descend pourtant au royaume des morts pour sauver le père qui l’a rejetée.', 'Abandoned at birth because she was not a son, the seventh princess nonetheless goes down to the realm of the dead to save the father who rejected her.'), [
  CH('bari-gongju-1', ('버려진 일곱째 딸', 'La septième fille abandonnée', 'The abandoned seventh daughter'), [
    [S('옛날 어느 나라의 왕과 왕비는 아들을 간절히 원했지만 딸만 여섯을 낳았다.', 'Il était une fois un roi et une reine qui désiraient ardemment un fils, mais n’eurent que six filles.', 'Long ago, a king and queen longed for a son but had only six daughters.'),
     S('일곱째도 딸이 태어나자 왕은 크게 실망한 나머지 아기를 버리라고 명령했다.', 'Quand la septième naquit fille elle aussi, le roi, profondément déçu, ordonna qu’on l’abandonne.', 'When the seventh was also a girl, the king, bitterly disappointed, ordered the baby to be abandoned.'),
     S('아기는 옥으로 만든 상자에 담겨 바다에 버려졌다.', 'Le bébé fut placé dans un coffre de jade et jeté à la mer.', 'The baby was put in a jade box and cast into the sea.')],
    [S('그러나 바다의 거북이 상자를 등에 업고 바닷가로 데려다주었다.', 'Mais une tortue de mer porta le coffre sur son dos jusqu’au rivage.', 'But a sea turtle carried the box on its back to the shore.'),
     S('가난한 노부부가 아기를 발견하고 「버려진 아이」라는 뜻으로 바리라고 불렀다.', 'Un vieux couple pauvre trouva l’enfant et l’appela Bari, « l’abandonnée ».', 'A poor old couple found the child and named her Bari, meaning “the abandoned one”.')],
  ], [
    W('간절히', 'ganjeolhi', 'ardemment', 'earnestly'),
    W('왕비', 'wangbi', 'reine', 'queen'),
    W('옥', 'ok', 'jade', 'jade'),
    W('담기다', 'damgida', 'être placé (dans un contenant)', 'to be put in'),
    W('업다', 'eopda', 'porter sur le dos', 'to carry on one’s back'),
    W('노부부', 'nobubu', 'vieux couple', 'elderly couple'),
  ], [
    Q(('Pourquoi le roi abandonne-t-il le bébé ?', 'Why does the king abandon the baby?'), [('Il voulait un fils', 'He wanted a son'), ('Le bébé était malade', 'The baby was ill'), ('Une prophétie l’y obligeait', 'A prophecy forced him to')], 0),
    Q(('Que signifie le nom « Bari » ?', 'What does the name “Bari” mean?'), [('La lumineuse', 'The bright one'), ('L’abandonnée', 'The abandoned one'), ('La septième', 'The seventh')], 1),
  ]),
  CH('bari-gongju-2', ('병든 왕', 'Le roi malade', 'The sick king'), [
    [S('십오 년이 지나 왕과 왕비가 큰 병에 걸렸다.', 'Quinze ans plus tard, le roi et la reine tombèrent gravement malades.', 'Fifteen years later, the king and queen fell gravely ill.'),
     S('점쟁이는 저승에 있는 생명수를 마셔야만 병이 나을 수 있다고 말했다.', 'Le devin déclara que seule l’eau de vie de l’au-delà pourrait les guérir.', 'The fortune-teller said only the water of life from the afterlife could cure them.'),
     S('그러나 여섯 공주는 저마다 핑계를 대며 아무도 가려고 하지 않았다.', 'Mais les six princesses trouvèrent chacune un prétexte, et aucune ne voulut y aller.', 'But each of the six princesses made an excuse, and none was willing to go.')],
    [S('소식을 들은 바리는 자신을 버린 부모를 원망하기는커녕 「제가 가겠습니다.」라고 말했다.', 'En apprenant la nouvelle, Bari, loin d’en vouloir aux parents qui l’avaient abandonnée, déclara : « J’irai. »', 'On hearing the news, Bari, far from resenting the parents who had abandoned her, said: “I will go.”'),
     S('낳아 준 은혜를 갚는 것이 자식의 도리라고 생각했기 때문이다.', 'Car elle pensait qu’un enfant doit rendre le bienfait de la vie reçue.', 'For she believed it was a child’s duty to repay the gift of life.')],
  ], [
    W('점쟁이', 'jeomjaengi', 'devin', 'fortune-teller'),
    W('저마다', 'jeomada', 'chacun', 'each'),
    W('핑계를 대다', 'pinggyereul daeda', 'trouver un prétexte', 'to make an excuse'),
    W('원망하다', 'wonmanghada', 'en vouloir à', 'to resent'),
    W('자식', 'jasik', 'enfant (de ses parents)', 'child (offspring)'),
    W('도리', 'dori', 'devoir moral', 'moral duty'),
  ], [
    Q(('Que faut-il pour guérir le roi ?', 'What is needed to cure the king?'), [('L’eau de vie de l’au-delà', 'The water of life from the afterlife'), ('Une herbe de la montagne', 'A mountain herb'), ('Le sang d’un dragon', 'A dragon’s blood')], 0),
    Q(('Comment réagit Bari ?', 'How does Bari react?'), [('Elle refuse par rancune', 'She refuses out of resentment'), ('Elle accepte d’y aller', 'She agrees to go'), ('Elle envoie ses sœurs', 'She sends her sisters')], 1),
  ]),
  CH('bari-gongju-3', ('저승으로 가는 길', 'Le chemin de l’au-delà', 'The road to the afterlife'), [
    [S('바리는 남자 옷을 입고 홀로 저승을 향해 길을 떠났다.', 'Vêtue en homme, Bari partit seule vers l’au-delà.', 'Dressed as a man, Bari set out alone for the afterlife.'),
     S('험한 산을 넘고 가시밭길을 지나며 끝없이 걸었다.', 'Elle franchit des montagnes escarpées, traversa des chemins d’épines et marcha sans fin.', 'She crossed steep mountains and paths of thorns, walking on and on.'),
     S('저승의 강가에 이르자 죄 많은 넋들이 울고 있었다.', 'Arrivée au bord du fleuve des morts, elle trouva des âmes chargées de fautes qui pleuraient.', 'When she reached the river of the dead, sinful souls were weeping there.')],
    [S('바리는 그 넋들을 불쌍히 여겨 극락으로 보내 주었다.', 'Prise de pitié, Bari les envoya au paradis.', 'Taking pity on them, Bari sent them on to paradise.'),
     S('마침내 생명수를 지키는 무장승을 만났다.', 'Enfin, elle rencontra Mujangseung, gardien de l’eau de vie.', 'At last she met Mujangseung, guardian of the water of life.')],
  ], [
    W('홀로', 'hollo', 'seul(e)', 'alone'),
    W('험하다', 'heomhada', 'être escarpé, rude', 'to be rough, steep'),
    W('가시밭길', 'gasibatgil', 'chemin d’épines', 'thorny path'),
    W('넋', 'neok', 'âme (d’un défunt)', 'soul (of the dead)'),
    W('불쌍히 여기다', 'bulssanghi yeogida', 'prendre en pitié', 'to take pity on'),
    W('극락', 'geungnak', 'paradis (bouddhique)', 'paradise'),
  ], [
    Q(('Comment Bari voyage-t-elle ?', 'How does Bari travel?'), [('Seule, habillée en homme', 'Alone, dressed as a man'), ('Avec ses sœurs', 'With her sisters'), ('À cheval avec une armée', 'On horseback with an army')], 0),
    Q(('Que fait-elle pour les âmes qui pleurent ?', 'What does she do for the weeping souls?'), [('Elle les ignore', 'She ignores them'), ('Elle les envoie au paradis', 'She sends them to paradise'), ('Elle leur prend leur eau', 'She takes their water')], 1),
  ]),
  CH('bari-gongju-4', ('생명수와 신이 된 공주', 'L’eau de vie et la princesse devenue déesse', 'The water of life and the princess who became a goddess'), [
    [S('무장승은 생명수를 주는 대신에 구 년 동안 일하라고 했다.', 'Mujangseung exigea neuf ans de travail en échange de l’eau de vie.', 'Mujangseung demanded nine years of work in exchange for the water of life.'),
     S('바리는 물을 긷고 나무를 하며 구 년을 견뎠고, 무장승과 혼인하여 아들도 낳았다.', 'Bari puisa l’eau et coupa le bois pendant neuf ans ; elle épousa Mujangseung et lui donna des fils.', 'Bari drew water and cut wood for nine years, married Mujangseung and bore him sons.'),
     S('마침내 생명수와 되살리는 꽃을 얻어 이승으로 돌아왔다.', 'Enfin, elle obtint l’eau de vie et les fleurs de résurrection et revint dans le monde des vivants.', 'At last she obtained the water of life and the flowers of revival and returned to the world of the living.')],
    [S('그러나 왕과 왕비는 이미 숨을 거둔 뒤였다.', 'Mais le roi et la reine avaient déjà rendu leur dernier souffle.', 'But the king and queen had already breathed their last.'),
     S('바리가 꽃과 생명수를 바르자 두 사람은 기적처럼 다시 눈을 떴다.', 'Quand Bari les oignit des fleurs et de l’eau de vie, ils rouvrirent les yeux, comme par miracle.', 'When Bari applied the flowers and the water of life, the two opened their eyes again, as if by miracle.'),
     S('그 후 바리는 죽은 이의 넋을 저승으로 인도하는 신이 되었다.', 'Bari devint ensuite la déesse qui guide les âmes des morts vers l’au-delà.', 'Bari then became the goddess who guides the souls of the dead to the afterlife.')],
  ], [
    W('되살리다', 'doesallida', 'ramener à la vie', 'to revive'),
    W('이승', 'iseung', 'le monde des vivants', 'this world, the world of the living'),
    W('숨을 거두다', 'sumeul geoduda', 'rendre son dernier souffle', 'to breathe one’s last'),
    W('바르다', 'bareuda', 'appliquer, enduire', 'to apply, to spread'),
    W('기적', 'gijeok', 'miracle', 'miracle'),
    W('인도하다', 'indohada', 'guider, conduire', 'to guide, to lead'),
  ], [
    Q(('Que demande Mujangseung en échange ?', 'What does Mujangseung ask in exchange?'), [('Neuf ans de travail', 'Nine years of work'), ('De l’or', 'Gold'), ('La couronne du roi', 'The king’s crown')], 0),
    Q(('Que devient Bari à la fin ?', 'What does Bari become in the end?'), [('Reine du royaume', 'Queen of the kingdom'), ('La déesse qui guide les âmes', 'The goddess who guides souls'), ('Une tortue de mer', 'A sea turtle')], 1),
  ]),
])

# ═════════════════════════ 단군 신화 (TOPIK 6) ═════════════════════════
DANGUN = STORY('dangun-sinhwa', '단', 'TOPIK6', '#A57E22', ('단군 신화', 'Le Mythe de Dangun', 'The Myth of Dangun'),
  ('Le mythe fondateur de la Corée : le fils du Ciel, l’ourse devenue femme et la naissance de Gojoseon, le premier royaume.', 'Korea’s founding myth: the son of Heaven, the bear who became a woman, and the birth of Gojoseon, the first kingdom.'), [
  CH('dangun-sinhwa-1', ('하늘에서 내려온 환웅', 'Hwanung descend du ciel', 'Hwanung comes down from heaven'), [
    [S('아주 먼 옛날, 하늘을 다스리는 환인에게는 환웅이라는 아들이 있었다.', 'Il y a très, très longtemps, Hwanin, maître du Ciel, avait un fils nommé Hwanung.', 'Long, long ago, Hwanin, ruler of Heaven, had a son named Hwanung.'),
     S('환웅은 늘 인간 세상을 내려다보며 그곳을 다스리고자 하였다.', 'Hwanung contemplait sans cesse le monde des hommes et désirait le gouverner.', 'Hwanung always gazed down on the human world and wished to govern it.'),
     S('환인은 아들의 뜻을 알고 인간을 널리 이롭게 할 만하다고 여겨 허락하였다.', 'Connaissant son désir et jugeant qu’il pourrait apporter de grands bienfaits aux hommes, Hwanin y consentit.', 'Knowing his wish and judging that he could greatly benefit humankind, Hwanin gave his consent.')],
    [S('환웅은 바람과 비와 구름을 다스리는 신하들과 무리 삼천을 이끌고 태백산 꼭대기 신단수 아래로 내려왔다.', 'Avec les ministres du vent, de la pluie et des nuages et trois mille compagnons, Hwanung descendit au sommet du mont Taebaek, sous l’arbre sacré du santal.', 'Leading the ministers of wind, rain and cloud and three thousand followers, Hwanung descended to the summit of Mount Taebaek, beneath the sacred sandalwood tree.'),
     S('그곳을 신시라 부르며 세상을 다스렸다.', 'Il nomma ce lieu Sinsi, la cité divine, et gouverna le monde.', 'He called the place Sinsi, the divine city, and ruled the world.')],
  ], [
    W('내려다보다', 'naeryeodaboda', 'regarder d’en haut', 'to look down on'),
    W('허락하다', 'heorakada', 'permettre, consentir', 'to allow, to permit'),
    W('신하', 'sinha', 'ministre, sujet (d’un roi)', 'minister, subject (of a king)'),
    W('이끌다', 'ikkeulda', 'mener, conduire', 'to lead'),
    W('꼭대기', 'kkokdaegi', 'sommet', 'top, summit'),
    W('신단수', 'sindansu', 'arbre sacré (santal)', 'sacred sandalwood tree'),
  ], [
    Q(('Pourquoi Hwanung veut-il descendre ?', 'Why does Hwanung want to come down?'), [('Pour gouverner le monde des hommes', 'To govern the human world'), ('Pour fuir son père', 'To flee his father'), ('Pour chercher un trésor', 'To look for treasure')], 0),
    Q(('Où descend-il ?', 'Where does he come down?'), [('Au bord de la mer', 'By the sea'), ('Au sommet du mont Taebaek', 'On the summit of Mount Taebaek'), ('Dans une caverne', 'In a cave')], 1),
  ]),
  CH('dangun-sinhwa-2', ('곰과 호랑이', 'L’ourse et le tigre', 'The bear and the tiger'), [
    [S('그때 한 동굴에 사는 곰과 호랑이가 환웅에게 사람이 되게 해 달라고 빌었다.', 'Alors, une ourse et un tigre qui vivaient dans une caverne supplièrent Hwanung de les rendre humains.', 'At that time, a bear and a tiger living in a cave begged Hwanung to make them human.'),
     S('환웅은 쑥 한 묶음과 마늘 스무 개를 주며 말했다.', 'Hwanung leur donna une botte d’armoise et vingt gousses d’ail, et dit :', 'Hwanung gave them a bundle of mugwort and twenty cloves of garlic, and said:'),
     S('「이것을 먹으며 백 일 동안 햇빛을 보지 않으면 사람이 될 것이다.」', '« Mangez ceci et ne voyez pas la lumière du soleil pendant cent jours : vous deviendrez humains. »', '“Eat this and do not see sunlight for a hundred days, and you will become human.”')],
    [S('호랑이는 참지 못하고 동굴을 뛰쳐나갔다.', 'Le tigre, incapable de patienter, s’enfuit de la caverne.', 'The tiger could not bear it and ran out of the cave.'),
     S('그러나 곰은 끝까지 견뎌 스무하루 만에 여자가 되었다. 그녀가 바로 웅녀이다.', 'Mais l’ourse tint bon jusqu’au bout et, au vingt et unième jour, devint une femme : Ungnyeo.', 'But the bear endured to the end and on the twenty-first day became a woman: Ungnyeo.')],
  ], [
    W('빌다', 'bilda', 'supplier, prier', 'to beg, to pray'),
    W('묶음', 'mukkeum', 'botte, faisceau', 'bundle'),
    W('뛰쳐나가다', 'ttwichyeonagada', 'se précipiter dehors', 'to dash out'),
    W('견디다', 'gyeondida', 'endurer, tenir bon', 'to endure'),
    W('스무하루', 'seumuharu', 'vingt et un jours', 'twenty-one days'),
    W('웅녀', 'ungnyeo', 'Ungnyeo, la femme-ourse', 'Ungnyeo, the bear woman'),
  ], [
    Q(('Que doivent manger l’ourse et le tigre ?', 'What must the bear and tiger eat?'), [('De l’armoise et de l’ail', 'Mugwort and garlic'), ('Du riz et du poisson', 'Rice and fish'), ('Des fruits', 'Fruit')], 0),
    Q(('Que fait le tigre ?', 'What does the tiger do?'), [('Il devient homme', 'He becomes a man'), ('Il s’enfuit de la caverne', 'He runs out of the cave'), ('Il épouse Hwanung', 'He marries Hwanung')], 1),
  ]),
  CH('dangun-sinhwa-3', ('단군의 탄생', 'La naissance de Dangun', 'The birth of Dangun'), [
    [S('사람이 된 웅녀는 혼인할 사람이 없어 매일 신단수 아래에서 아이를 갖게 해 달라고 빌었다.', 'Devenue femme mais sans personne à épouser, Ungnyeo priait chaque jour sous l’arbre sacré pour avoir un enfant.', 'Having become a woman but with no one to marry, Ungnyeo prayed every day beneath the sacred tree for a child.'),
     S('환웅은 잠시 사람의 모습으로 변하여 웅녀와 혼인하였다.', 'Hwanung prit un temps forme humaine et l’épousa.', 'Hwanung briefly took human form and married her.'),
     S('그리하여 아들이 태어났는데, 그가 바로 단군왕검이다.', 'Ainsi naquit un fils : Dangun Wanggeom.', 'Thus a son was born: Dangun Wanggeom.')],
    [S('단군은 자라면서 하늘의 지혜와 땅의 인내를 모두 갖추게 되었다.', 'En grandissant, Dangun réunit la sagesse du ciel et la persévérance de la terre.', 'As he grew, Dangun came to possess both the wisdom of heaven and the perseverance of the earth.')],
  ], [
    W('모습', 'moseup', 'apparence, forme', 'appearance, form'),
    W('변하다', 'byeonhada', 'se transformer', 'to transform'),
    W('그리하여', 'geurihayeo', 'ainsi, c’est ainsi que', 'thus, and so'),
    W('왕검', 'wanggeom', 'Wanggeom (titre royal)', 'Wanggeom (royal title)'),
    W('땅', 'ttang', 'terre, sol', 'land, earth'),
    W('갖추게 되다', 'gatchuge doeda', 'finir par posséder', 'to come to possess'),
  ], [
    Q(('Pour quoi Ungnyeo prie-t-elle ?', 'What does Ungnyeo pray for?'), [('Pour avoir un enfant', 'For a child'), ('Pour redevenir ourse', 'To become a bear again'), ('Pour la pluie', 'For rain')], 0),
    Q(('Qui sont les parents de Dangun ?', 'Who are Dangun’s parents?'), [('Hwanin et le tigre', 'Hwanin and the tiger'), ('Hwanung et Ungnyeo', 'Hwanung and Ungnyeo'), ('Un roi et une reine', 'A king and queen')], 1),
  ]),
  CH('dangun-sinhwa-4', ('고조선을 세우다', 'La fondation de Gojoseon', 'The founding of Gojoseon'), [
    [S('단군왕검은 평양성에 도읍을 정하고 나라 이름을 조선이라 하였다.', 'Dangun Wanggeom établit sa capitale à Pyongyang et nomma son pays Joseon.', 'Dangun Wanggeom set his capital at Pyongyang and named his country Joseon.'),
     S('후대의 조선과 구별하여 이 나라를 고조선이라 부른다.', 'Pour le distinguer du Joseon plus tardif, on l’appelle Gojoseon, « l’ancien Joseon ».', 'To distinguish it from the later Joseon, it is called Gojoseon, “Old Joseon”.'),
     S('단군은 천오백 년 동안 나라를 다스린 후 산으로 들어가 산신이 되었다고 전해진다.', 'On raconte qu’après avoir régné mille cinq cents ans, Dangun se retira dans la montagne et devint l’esprit des monts.', 'It is said that after ruling for 1,500 years, Dangun withdrew into the mountains and became a mountain god.')],
    [S('오늘날 한국에서는 매년 시월 삼일을 개천절로 정하여 나라가 처음 세워진 날을 기념한다.', 'Aujourd’hui, la Corée célèbre chaque 3 octobre la fête de Gaecheonjeol, jour de la fondation du pays.', 'Today, Korea celebrates 3 October each year as Gaecheonjeol, the day the nation was founded.'),
     S('「홍익인간」의 정신은 지금도 교육의 이념으로 이어지고 있다.', 'L’idéal de « bénéficier largement à l’humanité » inspire encore aujourd’hui l’éducation.', 'The ideal of “benefiting all humankind” still underpins education today.')],
  ], [
    W('도읍', 'doeup', 'capitale (ancienne)', 'capital (ancient)'),
    W('구별하다', 'gubyeolhada', 'distinguer', 'to distinguish'),
    W('전해지다', 'jeonhaejida', 'être transmis, se raconter', 'to be handed down'),
    W('산신', 'sansin', 'esprit de la montagne', 'mountain god'),
    W('기념하다', 'ginyeomhada', 'commémorer', 'to commemorate'),
    W('이념', 'inyeom', 'idéal, idéologie', 'ideal, ideology'),
  ], [
    Q(('Pourquoi dit-on « Gojoseon » ?', 'Why is it called “Gojoseon”?'), [('Pour le distinguer du Joseon plus tardif', 'To distinguish it from the later Joseon'), ('Parce qu’il était petit', 'Because it was small'), ('Parce qu’il était au sud', 'Because it was in the south')], 0),
    Q(('Que commémore le 3 octobre ?', 'What does 3 October commemorate?'), [('La naissance de Bari', 'Bari’s birth'), ('La fondation du pays', 'The founding of the nation'), ('Le Nouvel An', 'New Year')], 1),
  ]),
])

# ═════════════════════════ 금도끼 은도끼 (TOPIK 1) ═════════════════════════
GEUMDOKKI = STORY('geumdokki-eundokki', '금', 'TOPIK1', '#D9A93E', ('금도끼 은도끼', 'La Hache d’or et la Hache d’argent', 'The Golden Axe and the Silver Axe'),
  ('Un pauvre bûcheron laisse tomber sa hache dans un étang. L’esprit de la montagne lui propose une hache d’or…', 'A poor woodcutter drops his axe into a pond. The mountain spirit offers him a golden axe…'), [
  CH('geumdokki-eundokki-1', ('연못에 빠진 도끼', 'La hache tombée dans l’étang', 'The axe in the pond'), [
    [S('옛날에 가난한 나무꾼이 살았어요.', 'Il était une fois un pauvre bûcheron.', 'Once upon a time there lived a poor woodcutter.'),
     S('나무꾼은 매일 산에서 나무를 했어요.', 'Chaque jour, le bûcheron coupait du bois dans la montagne.', 'Every day, the woodcutter cut wood in the mountains.'),
     S('어느 날 연못 옆에서 나무를 하다가 도끼를 물에 떨어뜨렸어요.', 'Un jour, alors qu’il coupait du bois près d’un étang, il laissa tomber sa hache dans l’eau.', 'One day, while cutting wood by a pond, he dropped his axe into the water.')],
    [S('「아이고, 내 도끼! 이제 어떻게 해요?」', '« Oh non, ma hache ! Qu’est-ce que je vais faire ? »', '“Oh no, my axe! What am I going to do now?”'),
     S('나무꾼은 연못 앞에 앉아서 엉엉 울었어요.', 'Le bûcheron s’assit devant l’étang et pleura à chaudes larmes.', 'The woodcutter sat down by the pond and wept and wept.')],
  ], [
    W('나무꾼', 'namukkun', 'bûcheron', 'woodcutter'),
    W('가난하다', 'gananhada', 'être pauvre', 'to be poor'),
    W('도끼', 'dokki', 'hache', 'axe'),
    W('연못', 'yeonmot', 'étang', 'pond'),
    W('떨어뜨리다', 'tteoreotteurida', 'laisser tomber', 'to drop'),
    W('울다', 'ulda', 'pleurer', 'to cry'),
  ], [
    Q(('Que fait le bûcheron chaque jour ?', 'What does the woodcutter do every day?'), [('Il pêche', 'He fishes'), ('Il coupe du bois', 'He cuts wood'), ('Il vend des gâteaux', 'He sells cakes')], 1),
    Q(('Où tombe la hache ?', 'Where does the axe fall?'), [('Dans un étang', 'Into a pond'), ('Dans la rivière', 'Into the river'), ('Dans un puits', 'Into a well')], 0),
  ]),
  CH('geumdokki-eundokki-2', ('산신령이 나왔어요', 'L’esprit de la montagne apparaît', 'The mountain spirit appears'), [
    [S('그때 연못에서 하얀 수염의 산신령이 나왔어요.', 'Alors, un esprit de la montagne à la barbe blanche sortit de l’étang.', 'Then a mountain spirit with a white beard came out of the pond.'),
     S('「왜 울고 있느냐?」', '« Pourquoi pleures-tu ? »', '“Why are you crying?”'),
     S('산신령은 물속에 들어갔다가 금도끼를 가지고 나왔어요.', 'L’esprit plongea dans l’eau et en ressortit avec une hache d’or.', 'The spirit went into the water and came back out with a golden axe.')],
    [S('「이 금도끼가 네 도끼냐?」', '« Cette hache d’or est-elle la tienne ? »', '“Is this golden axe yours?”'),
     S('「아니요, 제 도끼는 금도끼가 아니에요.」', '« Non, ma hache n’est pas une hache d’or. »', '“No, my axe is not a golden axe.”'),
     S('산신령은 다시 은도끼를 가지고 왔어요. 나무꾼은 또 「아니요.」라고 대답했어요.', 'L’esprit revint avec une hache d’argent. Le bûcheron répondit encore : « Non. »', 'The spirit came back with a silver axe. The woodcutter answered “No” again.')],
  ], [
    W('산신령', 'sansillyeong', 'esprit de la montagne', 'mountain spirit'),
    W('수염', 'suyeom', 'barbe', 'beard'),
    W('물속', 'mulsok', 'sous l’eau', 'underwater'),
    W('금', 'geum', 'or', 'gold'),
    W('은', 'eun', 'argent (métal)', 'silver'),
    W('대답하다', 'daedapada', 'répondre', 'to answer'),
  ], [
    Q(('Quelle hache l’esprit montre-t-il d’abord ?', 'Which axe does the spirit show first?'), [('Une hache de fer', 'An iron axe'), ('Une hache d’argent', 'A silver axe'), ('Une hache d’or', 'A golden axe')], 2),
    Q(('Que répond le bûcheron ?', 'What does the woodcutter answer?'), [('« Oui, c’est la mienne »', '“Yes, it’s mine”'), ('« Non »', '“No”'), ('Il ne dit rien', 'He says nothing')], 1),
  ]),
  CH('geumdokki-eundokki-3', ('정직한 나무꾼', 'Le bûcheron honnête', 'The honest woodcutter'), [
    [S('마지막으로 산신령은 낡은 쇠도끼를 가지고 왔어요.', 'Pour finir, l’esprit rapporta une vieille hache de fer.', 'Finally, the spirit brought back an old iron axe.'),
     S('「네, 그게 제 도끼예요!」 나무꾼은 아주 기뻐했어요.', '« Oui, c’est ma hache ! » Le bûcheron était fou de joie.', '“Yes, that’s my axe!” The woodcutter was overjoyed.')],
    [S('「너는 정말 정직하구나. 세 도끼를 모두 가져가거라.」', '« Tu es vraiment honnête. Prends les trois haches. »', '“You are truly honest. Take all three axes.”'),
     S('나무꾼은 금도끼와 은도끼를 팔아서 부자가 되었어요.', 'Le bûcheron vendit la hache d’or et la hache d’argent et devint riche.', 'The woodcutter sold the golden and silver axes and became rich.')],
  ], [
    W('쇠', 'soe', 'fer', 'iron'),
    W('낡다', 'nakda', 'être vieux, usé', 'to be old, worn'),
    W('기뻐하다', 'gippeohada', 'se réjouir', 'to be glad'),
    W('정직하다', 'jeongjikada', 'être honnête', 'to be honest'),
    W('모두', 'modu', 'tous, tout', 'all'),
    W('부자', 'buja', 'personne riche', 'rich person'),
  ], [
    Q(('De quoi est faite la hache du bûcheron ?', 'What is the woodcutter’s axe made of?'), [('De fer', 'Iron'), ('D’or', 'Gold'), ('De bois', 'Wood')], 0),
    Q(('Pourquoi l’esprit lui donne-t-il les trois haches ?', 'Why does the spirit give him all three axes?'), [('Parce qu’il pleure', 'Because he is crying'), ('Parce qu’il est honnête', 'Because he is honest'), ('Parce qu’il est riche', 'Because he is rich')], 1),
  ]),
  CH('geumdokki-eundokki-4', ('욕심쟁이 이웃', 'Le voisin cupide', 'The greedy neighbour'), [
    [S('이웃에 욕심이 많은 나무꾼이 살았어요.', 'Un bûcheron très cupide habitait à côté.', 'A very greedy woodcutter lived next door.'),
     S('그 이야기를 듣고 일부러 도끼를 연못에 던졌어요.', 'En entendant l’histoire, il jeta exprès sa hache dans l’étang.', 'Hearing the story, he threw his axe into the pond on purpose.'),
     S('산신령이 금도끼를 보여 주자 「네, 그게 제 도끼예요!」라고 했어요.', 'Quand l’esprit lui montra la hache d’or, il s’écria : « Oui, c’est ma hache ! »', 'When the spirit showed him the golden axe, he said, “Yes, that’s my axe!”')],
    [S('산신령은 화가 나서 아무것도 주지 않았어요.', 'L’esprit, furieux, ne lui donna rien du tout.', 'The spirit got angry and gave him nothing at all.'),
     S('욕심쟁이는 자기 쇠도끼까지 잃어버렸어요.', 'Le cupide perdit même sa propre hache de fer.', 'The greedy man even lost his own iron axe.')],
  ], [
    W('이웃', 'iut', 'voisin', 'neighbour'),
    W('욕심', 'yoksim', 'cupidité', 'greed'),
    W('일부러', 'ilbureo', 'exprès', 'on purpose'),
    W('던지다', 'deonjida', 'jeter, lancer', 'to throw'),
    W('화가 나다', 'hwaga nada', 'se fâcher', 'to get angry'),
    W('잃어버리다', 'ireobeorida', 'perdre', 'to lose'),
  ], [
    Q(('Comment la hache du voisin tombe-t-elle dans l’eau ?', 'How does the neighbour’s axe end up in the water?'), [('Par accident', 'By accident'), ('Il la jette exprès', 'He throws it in on purpose'), ('Un oiseau la fait tomber', 'A bird knocks it in')], 1),
    Q(('Que reçoit le voisin à la fin ?', 'What does the neighbour get in the end?'), [('Rien, il perd même sa hache', 'Nothing, he even loses his axe'), ('La hache d’or', 'The golden axe'), ('Les trois haches', 'All three axes')], 0),
  ]),
])

# ═════════════════════════ 혹부리 영감 (TOPIK 2) ═════════════════════════
HOKBURI = STORY('hokburi-yeonggam', '혹', 'TOPIK2', '#5E7A3A', ('혹부리 영감', 'Le Vieil Homme à la bosse', 'The Old Man with the Lump'),
  ('Un vieil homme à la grosse bosse chante si bien que les dokkaebi veulent lui acheter le secret de sa voix.', 'An old man with a big lump sings so well that the dokkaebi goblins want to buy the secret of his voice.'), [
  CH('hokburi-yeonggam-1', ('혹이 달린 할아버지', 'Le grand-père à la bosse', 'The grandfather with the lump'), [
    [S('옛날 어느 마을에 볼에 커다란 혹이 달린 할아버지가 살았어요.', 'Autrefois, dans un village, vivait un grand-père qui avait une énorme bosse sur la joue.', 'Long ago, in a village, there lived a grandfather with a huge lump on his cheek.'),
     S('사람들은 그를 혹부리 영감이라고 불렀어요.', 'Les gens l’appelaient « le vieil homme à la bosse ».', 'People called him “the old man with the lump”.'),
     S('할아버지는 마음씨가 착하고 노래를 아주 잘 불렀어요.', 'Il avait bon cœur et chantait merveilleusement bien.', 'He was kind-hearted and sang beautifully.')],
    [S('어느 날 산에서 나무를 하다가 날이 저물어 길을 잃고 말았어요.', 'Un jour, alors qu’il coupait du bois dans la montagne, la nuit tomba et il se perdit.', 'One day, while cutting wood in the mountains, night fell and he got lost.'),
     S('할아버지는 빈 집을 발견하고 거기에서 하룻밤을 자기로 했어요.', 'Il trouva une maison vide et décida d’y passer la nuit.', 'He found an empty house and decided to spend the night there.')],
  ], [
    W('볼', 'bol', 'joue', 'cheek'),
    W('혹', 'hok', 'bosse, grosseur', 'lump'),
    W('영감', 'yeonggam', 'vieil homme', 'old man'),
    W('날이 저물다', 'nari jeomulda', 'la nuit tombe', 'night falls'),
    W('길을 잃다', 'gireul ilta', 'se perdre', 'to get lost'),
    W('하룻밤', 'harutbam', 'une nuit', 'one night'),
  ], [
    Q(('Qu’a de particulier le grand-père ?', 'What is special about the grandfather?'), [('Une bosse sur la joue', 'A lump on his cheek'), ('Une longue barbe', 'A long beard'), ('Un seul œil', 'Only one eye')], 0),
    Q(('Pourquoi dort-il dans une maison vide ?', 'Why does he sleep in an empty house?'), [('Il s’est perdu', 'He got lost'), ('Sa maison a brûlé', 'His house burned down'), ('Il veut voir les dokkaebi', 'He wants to see the dokkaebi')], 0),
  ]),
  CH('hokburi-yeonggam-2', ('도깨비들의 잔치', 'La fête des dokkaebi', 'The dokkaebi feast'), [
    [S('밤이 깊어지자 도깨비들이 몰려와서 잔치를 벌였어요.', 'Au cœur de la nuit, une bande de dokkaebi arriva et se mit à festoyer.', 'Late at night, a crowd of dokkaebi arrived and threw a feast.'),
     S('할아버지는 무서웠지만 용기를 내서 노래를 불렀어요.', 'Le grand-père avait peur, mais il prit son courage à deux mains et chanta.', 'The grandfather was scared, but he plucked up his courage and sang.'),
     S('도깨비들은 노래에 반해서 덩실덩실 춤을 추었어요.', 'Charmés par la chanson, les dokkaebi se mirent à danser joyeusement.', 'Charmed by the song, the dokkaebi danced merrily.')],
    [S('「영감, 그렇게 좋은 노래가 어디에서 나오는 거요?」', '« Grand-père, d’où sort une si belle chanson ? »', '“Old man, where does such a lovely song come from?”'),
     S('할아버지는 꾀를 내어 대답했어요. 「이 혹에서 나오지요.」', 'Le grand-père eut une idée rusée et répondit : « De cette bosse, pardi. »', 'The grandfather had a clever idea and answered: “From this lump, of course.”')],
  ], [
    W('도깨비', 'dokkaebi', 'dokkaebi (lutin coréen)', 'dokkaebi (Korean goblin)'),
    W('몰려오다', 'mollyeooda', 'arriver en foule', 'to flock in'),
    W('잔치', 'janchi', 'fête, festin', 'feast'),
    W('용기를 내다', 'yonggireul naeda', 'prendre son courage', 'to pluck up courage'),
    W('반하다', 'banhada', 'être charmé', 'to be charmed'),
    W('꾀', 'kkoe', 'ruse, astuce', 'trick, wit'),
  ], [
    Q(('Que fait le grand-père face aux dokkaebi ?', 'What does the grandfather do in front of the dokkaebi?'), [('Il s’enfuit', 'He runs away'), ('Il chante', 'He sings'), ('Il se cache', 'He hides')], 1),
    Q(('D’où vient sa chanson, selon lui ?', 'Where does his song come from, according to him?'), [('De son cœur', 'From his heart'), ('De sa bosse', 'From his lump'), ('De la montagne', 'From the mountain')], 1),
  ]),
  CH('hokburi-yeonggam-3', ('혹을 팔다', 'La bosse vendue', 'Selling the lump'), [
    [S('도깨비들은 보물을 잔뜩 주고 혹을 떼어 갔어요.', 'Les dokkaebi lui donnèrent quantité de trésors et emportèrent la bosse.', 'The dokkaebi gave him plenty of treasure and took the lump away.'),
     S('혹이 없어지자 얼굴이 가벼워졌어요.', 'Sans sa bosse, son visage était tout léger.', 'Without the lump, his face felt light.')],
    [S('할아버지는 부자가 되어 마을로 돌아왔어요.', 'Le grand-père rentra au village, devenu riche.', 'The grandfather returned to the village a rich man.'),
     S('마을 사람들은 깜짝 놀라서 무슨 일이 있었는지 물었어요.', 'Les villageois, stupéfaits, lui demandèrent ce qui s’était passé.', 'The astonished villagers asked him what had happened.')],
  ], [
    W('보물', 'bomul', 'trésor', 'treasure'),
    W('잔뜩', 'jantteuk', 'plein de, beaucoup', 'plenty'),
    W('떼다', 'tteda', 'détacher, enlever', 'to detach, to remove'),
    W('가볍다', 'gabyeopda', 'être léger', 'to be light'),
    W('돌아오다', 'doraoda', 'revenir', 'to come back'),
    W('깜짝 놀라다', 'kkamjjak nollada', 'être stupéfait', 'to be startled'),
  ], [
    Q(('Que reçoit le grand-père en échange de sa bosse ?', 'What does the grandfather get in exchange for his lump?'), [('Des trésors', 'Treasure'), ('Une nouvelle voix', 'A new voice'), ('Une maison', 'A house')], 0),
    Q(('Comment se sent son visage ?', 'How does his face feel?'), [('Lourd', 'Heavy'), ('Léger', 'Light'), ('Douloureux', 'Painful')], 1),
  ]),
  CH('hokburi-yeonggam-4', ('욕심 많은 혹부리 영감', 'L’autre vieil homme, cupide', 'The other, greedy old man'), [
    [S('이웃 마을의 또 다른 혹부리 영감이 그 이야기를 들었어요.', 'Un autre vieil homme à la bosse, du village voisin, entendit l’histoire.', 'Another old man with a lump, from the next village, heard the story.'),
     S('그도 보물을 얻으려고 그 빈 집에 가서 노래를 불렀어요.', 'Voulant lui aussi des trésors, il alla dans la maison vide et chanta.', 'Wanting treasure too, he went to the empty house and sang.'),
     S('하지만 노래 실력이 형편없었어요.', 'Mais il chantait affreusement mal.', 'But his singing was dreadful.')],
    [S('「노래가 혹에서 나온다고? 거짓말쟁이!」', '« La chanson sort de la bosse ? Menteur ! »', '“The song comes from the lump? Liar!”'),
     S('화가 난 도깨비들은 지난번 혹을 그의 다른 볼에 붙여 주었어요.', 'Furieux, les dokkaebi lui collèrent l’ancienne bosse sur l’autre joue.', 'The furious dokkaebi stuck the first lump onto his other cheek.'),
     S('결국 그는 혹이 두 개가 되었어요.', 'Il finit ainsi avec deux bosses.', 'In the end, he had two lumps.')],
  ], [
    W('얻다', 'eotda', 'obtenir', 'to obtain'),
    W('실력', 'sillyeok', 'talent, niveau', 'skill'),
    W('형편없다', 'hyeongpyeoneopda', 'être lamentable', 'to be dreadful'),
    W('거짓말쟁이', 'geojinmaljaengi', 'menteur', 'liar'),
    W('붙이다', 'buchida', 'coller, attacher', 'to stick on'),
    W('결국', 'gyeolguk', 'finalement', 'in the end'),
  ], [
    Q(('Pourquoi le second vieil homme va-t-il à la maison vide ?', 'Why does the second old man go to the empty house?'), [('Pour avoir des trésors', 'To get treasure'), ('Pour dormir', 'To sleep'), ('Pour aider son voisin', 'To help his neighbour')], 0),
    Q(('Combien de bosses a-t-il à la fin ?', 'How many lumps does he have in the end?'), [('Aucune', 'None'), ('Une', 'One'), ('Deux', 'Two')], 2),
  ]),
])

# ═════════════════════════ 콩쥐팥쥐 (TOPIK 2) ═════════════════════════
KONGJWI = STORY('kongjwi-patjwi', '콩', 'TOPIK2', '#C8553D', ('콩쥐팥쥐', 'Kongjwi et Patjwi', 'Kongjwi and Patjwi'),
  ('La « Cendrillon » coréenne : une jeune fille maltraitée par sa belle-mère, aidée par un crapaud et des oiseaux, et une sandale perdue au bord d’un ruisseau.', 'The Korean “Cinderella”: a girl mistreated by her stepmother, helped by a toad and birds, and a slipper lost by a stream.'), [
  CH('kongjwi-patjwi-1', ('착한 콩쥐', 'La gentille Kongjwi', 'Kind Kongjwi'), [
    [S('옛날에 콩쥐라는 착한 여자아이가 살았어요.', 'Il était une fois une gentille petite fille nommée Kongjwi.', 'Once upon a time there was a kind girl named Kongjwi.'),
     S('어머니가 일찍 돌아가셔서 아버지는 새어머니와 결혼했어요.', 'Sa mère étant morte tôt, son père épousa une autre femme.', 'Her mother died early, so her father married again.'),
     S('새어머니에게는 팥쥐라는 딸이 있었어요.', 'La belle-mère avait une fille nommée Patjwi.', 'The stepmother had a daughter named Patjwi.')],
    [S('새어머니는 팥쥐만 예뻐하고 콩쥐에게는 힘든 일만 시켰어요.', 'La belle-mère ne chérissait que Patjwi et ne donnait que des corvées à Kongjwi.', 'The stepmother doted only on Patjwi and gave Kongjwi nothing but hard chores.'),
     S('그래도 콩쥐는 불평하지 않고 열심히 일했어요.', 'Kongjwi, pourtant, travaillait dur sans jamais se plaindre.', 'Even so, Kongjwi worked hard without complaining.')],
  ], [
    W('착하다', 'chakada', 'être gentil, bon', 'to be kind'),
    W('돌아가시다', 'doragasida', 'décéder (honorifique)', 'to pass away (honorific)'),
    W('새어머니', 'saeeomeoni', 'belle-mère (marâtre)', 'stepmother'),
    W('예뻐하다', 'yeppeohada', 'chérir, chouchouter', 'to dote on'),
    W('시키다', 'sikida', 'faire faire, ordonner', 'to make someone do'),
    W('불평하다', 'bulpyeonghada', 'se plaindre', 'to complain'),
  ], [
    Q(('Qui est Patjwi ?', 'Who is Patjwi?'), [('La fille de la belle-mère', 'The stepmother’s daughter'), ('La sœur de la mère', 'The mother’s sister'), ('Une amie de Kongjwi', 'A friend of Kongjwi')], 0),
    Q(('Comment Kongjwi réagit-elle aux corvées ?', 'How does Kongjwi react to the chores?'), [('Elle se plaint', 'She complains'), ('Elle s’enfuit', 'She runs away'), ('Elle travaille sans se plaindre', 'She works without complaining')], 2),
  ]),
  CH('kongjwi-patjwi-2', ('밑 빠진 독', 'La jarre percée', 'The bottomless jar'), [
    [S('어느 날 새어머니는 팥쥐와 함께 잔치에 가면서 말했어요.', 'Un jour, en partant à une fête avec Patjwi, la belle-mère dit :', 'One day, as she left for a feast with Patjwi, the stepmother said:'),
     S('「저 큰 독에 물을 가득 채워 놓아라.」', '« Remplis cette grande jarre d’eau jusqu’en haut. »', '“Fill that big jar to the brim with water.”'),
     S('그런데 그 독은 밑이 깨져 있어서 아무리 물을 부어도 채워지지 않았어요.', 'Mais le fond de la jarre était cassé : on avait beau verser de l’eau, elle ne se remplissait pas.', 'But the bottom of the jar was broken, so no matter how much water she poured, it would not fill.')],
    [S('콩쥐가 울고 있을 때 커다란 두꺼비가 나타났어요.', 'Pendant que Kongjwi pleurait, un gros crapaud apparut.', 'While Kongjwi was crying, a big toad appeared.'),
     S('「걱정하지 마. 내가 구멍을 막아 줄게.」', '« Ne t’en fais pas. Je vais boucher le trou. »', '“Don’t worry. I’ll block the hole.”'),
     S('두꺼비 덕분에 독은 금방 물로 가득 찼어요.', 'Grâce au crapaud, la jarre fut vite pleine.', 'Thanks to the toad, the jar was soon full of water.')],
  ], [
    W('독', 'dok', 'jarre', 'large jar'),
    W('채우다', 'chaeuda', 'remplir', 'to fill'),
    W('붓다', 'butda', 'verser', 'to pour'),
    W('두꺼비', 'dukkeobi', 'crapaud', 'toad'),
    W('구멍', 'gumeong', 'trou', 'hole'),
    W('덕분에', 'deokbune', 'grâce à', 'thanks to'),
  ], [
    Q(('Pourquoi la jarre ne se remplit-elle pas ?', 'Why won’t the jar fill up?'), [('Son fond est cassé', 'Its bottom is broken'), ('Il n’y a pas d’eau', 'There is no water'), ('Patjwi la vide', 'Patjwi empties it')], 0),
    Q(('Qui aide Kongjwi ?', 'Who helps Kongjwi?'), [('Son père', 'Her father'), ('Un crapaud', 'A toad'), ('Patjwi', 'Patjwi')], 1),
  ]),
  CH('kongjwi-patjwi-3', ('꽃신 한 짝', 'Une sandale brodée', 'One embroidered slipper'), [
    [S('참새들도 날아와서 콩쥐가 벼를 찧는 것을 도와주었어요.', 'Des moineaux vinrent aussi l’aider à décortiquer le riz.', 'Sparrows also flew in to help Kongjwi hull the rice.'),
     S('일을 마친 콩쥐는 서둘러 잔치에 가다가 개울을 건넜어요.', 'Sa tâche finie, Kongjwi se pressa vers la fête et traversa un ruisseau.', 'Her work done, Kongjwi hurried to the feast and crossed a stream.'),
     S('그런데 너무 서두르다가 꽃신 한 짝을 물에 빠뜨렸어요.', 'Mais dans sa hâte, elle fit tomber une de ses sandales brodées dans l’eau.', 'But in her hurry, she dropped one of her embroidered slippers into the water.')],
    [S('마침 그곳을 지나가던 원님이 그 꽃신을 주웠어요.', 'Justement, le magistrat qui passait par là ramassa la sandale.', 'Just then, the magistrate passing by picked up the slipper.'),
     S('「이렇게 고운 신발의 주인을 꼭 찾아라.」', '« Trouvez absolument la propriétaire de cette jolie sandale. »', '“Be sure to find the owner of this lovely slipper.”')],
  ], [
    W('참새', 'chamsae', 'moineau', 'sparrow'),
    W('개울', 'gaeul', 'ruisseau', 'stream'),
    W('건너다', 'geonneoda', 'traverser', 'to cross'),
    W('꽃신', 'kkotsin', 'sandale brodée de fleurs', 'embroidered flower slipper'),
    W('짝', 'jjak', 'un (d’une paire)', 'one of a pair'),
    W('줍다', 'jupda', 'ramasser', 'to pick up'),
  ], [
    Q(('Que perd Kongjwi dans le ruisseau ?', 'What does Kongjwi lose in the stream?'), [('Son collier', 'Her necklace'), ('Une sandale', 'A slipper'), ('Son panier', 'Her basket')], 1),
    Q(('Qui la trouve ?', 'Who finds it?'), [('Le magistrat', 'The magistrate'), ('Patjwi', 'Patjwi'), ('Le crapaud', 'The toad')], 0),
  ]),
  CH('kongjwi-patjwi-4', ('신발의 주인', 'La propriétaire de la sandale', 'The owner of the slipper'), [
    [S('마을의 모든 여자들이 그 꽃신을 신어 보았지만 아무에게도 맞지 않았어요.', 'Toutes les femmes du village essayèrent la sandale, mais elle n’allait à personne.', 'Every woman in the village tried on the slipper, but it fitted no one.'),
     S('팥쥐도 신어 보았지만 발이 너무 커서 들어가지 않았어요.', 'Patjwi l’essaya aussi, mais son pied était bien trop grand.', 'Patjwi tried it too, but her foot was far too big.')],
    [S('마지막으로 콩쥐가 신자 신발이 꼭 맞았어요.', 'Enfin, Kongjwi l’enfila, et elle lui allait parfaitement.', 'Finally Kongjwi put it on, and it fitted perfectly.'),
     S('콩쥐는 원님과 결혼해서 오래오래 행복하게 살았어요.', 'Kongjwi épousa le magistrat et vécut heureuse très longtemps.', 'Kongjwi married the magistrate and lived happily ever after.')],
  ], [
    W('신다', 'sinda', 'mettre (des chaussures)', 'to put on (shoes)'),
    W('맞다', 'matda', 'aller (à la bonne taille)', 'to fit'),
    W('주인', 'juin', 'propriétaire', 'owner'),
    W('꼭', 'kkok', 'parfaitement, exactement', 'exactly'),
    W('오래오래', 'oraeorae', 'très longtemps', 'for a very long time'),
    W('행복하다', 'haengbokada', 'être heureux', 'to be happy'),
  ], [
    Q(('Pourquoi la sandale ne va-t-elle pas à Patjwi ?', 'Why doesn’t the slipper fit Patjwi?'), [('Son pied est trop grand', 'Her foot is too big'), ('Elle refuse de l’essayer', 'She refuses to try it'), ('Elle est mouillée', 'It is wet')], 0),
    Q(('Comment finit l’histoire pour Kongjwi ?', 'How does the story end for Kongjwi?'), [('Elle part en voyage', 'She goes travelling'), ('Elle épouse le magistrat', 'She marries the magistrate'), ('Elle redevient servante', 'She becomes a servant again')], 1),
  ]),
])

# ═════════════════════════ 심청전 (TOPIK 3) ═════════════════════════
SIMCHEONG = STORY('simcheong', '심', 'TOPIK3', '#2F5D8A', ('심청전', 'L’Histoire de Sim Cheong', 'The Tale of Sim Cheong'),
  ('Pour rendre la vue à son père aveugle, une fille dévouée se sacrifie à la mer… et renaît dans une fleur de lotus.', 'To restore her blind father’s sight, a devoted daughter gives herself to the sea… and is reborn in a lotus flower.'), [
  CH('simcheong-1', ('눈먼 아버지와 효녀', 'Le père aveugle et la fille dévouée', 'The blind father and the devoted daughter'), [
    [S('옛날 도화동이라는 마을에 심학규라는 눈먼 선비가 살았어요.', 'Autrefois, au village de Dohwa-dong, vivait un lettré aveugle nommé Sim Hak-gyu.', 'Long ago, in a village called Dohwa-dong, lived a blind scholar named Sim Hak-gyu.'),
     S('사람들은 그를 심 봉사라고 불렀어요.', 'On l’appelait « l’aveugle Sim ».', 'People called him “blind Sim”.'),
     S('아내가 딸 청이를 낳고 세상을 떠나자 심 봉사는 동네를 돌며 젖을 얻어 딸을 키웠어요.', 'Sa femme mourut après avoir mis au monde leur fille Cheong ; l’aveugle Sim éleva l’enfant en allant mendier du lait dans le voisinage.', 'When his wife died after giving birth to their daughter Cheong, blind Sim raised her by begging milk around the neighbourhood.')],
    [S('청이는 자라면서 효심이 깊은 딸이 되었어요.', 'En grandissant, Cheong devint une fille d’une grande piété filiale.', 'As she grew up, Cheong became a deeply devoted daughter.'),
     S('열다섯 살이 되었을 때는 바느질을 해서 번 돈으로 아버지를 정성껏 모셨어요.', 'À quinze ans, elle prenait soin de son père avec dévouement grâce à l’argent gagné en cousant.', 'By fifteen she was caring devotedly for her father with the money she earned sewing.')],
  ], [
    W('눈멀다', 'nunmeolda', 'devenir aveugle', 'to be blind'),
    W('선비', 'seonbi', 'lettré confucéen', 'Confucian scholar'),
    W('세상을 떠나다', 'sesangeul tteonada', 'quitter ce monde, mourir', 'to pass away'),
    W('키우다', 'kiuda', 'élever', 'to raise'),
    W('효심', 'hyosim', 'piété filiale', 'filial devotion'),
    W('모시다', 'mosida', 'prendre soin (d’un aîné)', 'to look after (an elder)'),
  ], [
    Q(('Comment Sim élève-t-il sa fille ?', 'How does Sim raise his daughter?'), [('Il mendie du lait aux voisins', 'He begs milk from the neighbours'), ('Il la confie à un temple', 'He leaves her at a temple'), ('Il engage une nourrice', 'He hires a nurse')], 0),
    Q(('Comment Cheong gagne-t-elle de l’argent ?', 'How does Cheong earn money?'), [('En chantant', 'By singing'), ('En cousant', 'By sewing'), ('En pêchant', 'By fishing')], 1),
  ]),
  CH('simcheong-2', ('공양미 삼백 석', 'Trois cents sacs de riz', 'Three hundred sacks of rice'), [
    [S('어느 날 딸을 마중 나가던 심 봉사가 개울에 빠졌다가 한 스님에게 구조되었어요.', 'Un jour, en allant au-devant de sa fille, l’aveugle Sim tomba dans un ruisseau et fut sauvé par un moine.', 'One day, going out to meet his daughter, blind Sim fell into a stream and was rescued by a monk.'),
     S('스님은 공양미 삼백 석을 부처님께 바치면 눈을 뜰 수 있을 거라고 했어요.', 'Le moine lui dit qu’en offrant trois cents sacs de riz au Bouddha, il pourrait retrouver la vue.', 'The monk told him that if he offered three hundred sacks of rice to the Buddha, he would be able to see.')],
    [S('심 봉사는 앞뒤 생각 없이 약속하고 말았어요.', 'Sans réfléchir, l’aveugle Sim le promit.', 'Without thinking, blind Sim made the promise.'),
     S('하지만 집에 돌아와서는 걱정에 잠겼어요. 가난한 집에서 쌀 삼백 석을 마련할 수 있을 리가 없었으니까요.', 'Mais de retour chez lui, il fut rongé d’inquiétude : jamais une famille pauvre ne pourrait réunir trois cents sacs de riz.', 'But back home he was filled with worry: a poor household could never come up with three hundred sacks of rice.')],
  ], [
    W('마중 나가다', 'majung nagada', 'aller à la rencontre de', 'to go out to meet'),
    W('구조되다', 'gujodoeda', 'être secouru', 'to be rescued'),
    W('스님', 'seunim', 'moine bouddhiste', 'Buddhist monk'),
    W('공양미', 'gongyangmi', 'riz d’offrande', 'offering rice'),
    W('바치다', 'bachida', 'offrir (en don)', 'to offer'),
    W('마련하다', 'maryeonhada', 'réunir, se procurer', 'to come up with, to obtain'),
  ], [
    Q(('Que promet l’aveugle Sim au moine ?', 'What does blind Sim promise the monk?'), [('Trois cents sacs de riz', 'Three hundred sacks of rice'), ('De devenir moine', 'To become a monk'), ('Sa maison', 'His house')], 0),
    Q(('Pourquoi s’inquiète-t-il ensuite ?', 'Why does he worry afterwards?'), [('Il ne peut pas réunir le riz', 'He cannot come up with the rice'), ('Il a perdu le moine', 'He has lost the monk'), ('Sa fille est malade', 'His daughter is ill')], 0),
  ]),
  CH('simcheong-3', ('인당수', 'Les eaux d’Indangsu', 'The waters of Indangsu'), [
    [S('그 무렵 뱃사람들이 거친 바다 인당수의 신에게 바칠 처녀를 찾고 있었어요.', 'À cette époque, des marins cherchaient une jeune fille à offrir au dieu des eaux tumultueuses d’Indangsu.', 'At that time, sailors were looking for a maiden to offer to the god of the rough waters of Indangsu.'),
     S('청이는 쌀 삼백 석을 받는 대신 자기 몸을 팔기로 결심했어요.', 'Cheong décida de se vendre en échange des trois cents sacs de riz.', 'Cheong resolved to sell herself in exchange for the three hundred sacks of rice.')],
    [S('아버지에게는 사실을 숨긴 채 배에 올랐어요.', 'Elle embarqua en cachant la vérité à son père.', 'She boarded the ship, hiding the truth from her father.'),
     S('파도가 높은 인당수에 이르자 청이는 치마를 뒤집어쓰고 바다에 뛰어들었어요.', 'Arrivée aux vagues déchaînées d’Indangsu, Cheong se couvrit la tête de sa jupe et sauta dans la mer.', 'When they reached the towering waves of Indangsu, Cheong pulled her skirt over her head and leapt into the sea.')],
  ], [
    W('무렵', 'muryeop', 'vers (telle époque)', 'around (that time)'),
    W('뱃사람', 'baetsaram', 'marin', 'sailor'),
    W('처녀', 'cheonyeo', 'jeune fille', 'maiden'),
    W('결심하다', 'gyeolsimhada', 'décider fermement', 'to resolve'),
    W('숨기다', 'sumgida', 'cacher', 'to hide'),
    W('뛰어들다', 'ttwieodeulda', 'se jeter, plonger', 'to leap in'),
  ], [
    Q(('Que cherchent les marins ?', 'What are the sailors looking for?'), [('Du riz', 'Rice'), ('Une jeune fille à offrir à la mer', 'A maiden to offer to the sea'), ('Un moine', 'A monk')], 1),
    Q(('Que sait le père du départ de Cheong ?', 'What does the father know about Cheong leaving?'), [('Rien, elle lui cache la vérité', 'Nothing, she hides the truth from him'), ('Il l’accompagne', 'He goes with her'), ('Il l’en empêche', 'He stops her')], 0),
  ]),
  CH('simcheong-4', ('연꽃에서 다시 태어나다', 'Renaître d’une fleur de lotus', 'Reborn from a lotus flower'), [
    [S('바닷속 용왕은 청이의 효심에 감동하여 그녀를 커다란 연꽃에 태워 바다 위로 돌려보냈어요.', 'Le Roi-Dragon des mers, ému par sa piété filiale, la renvoya à la surface dans une immense fleur de lotus.', 'The Dragon King of the sea, moved by her devotion, sent her back to the surface inside a huge lotus flower.'),
     S('연꽃을 발견한 임금은 청이를 왕비로 맞이했어요.', 'Le roi découvrit la fleur et prit Cheong pour reine.', 'The king who found the lotus took Cheong as his queen.')],
    [S('왕비가 된 청이는 아버지를 찾으려고 전국의 맹인들을 위한 잔치를 열었어요.', 'Devenue reine, Cheong organisa un banquet pour tous les aveugles du pays, afin de retrouver son père.', 'Now queen, Cheong held a banquet for all the blind people of the land in order to find her father.'),
     S('딸의 목소리를 들은 심 봉사는 너무 놀라 눈을 번쩍 떴어요.', 'En entendant la voix de sa fille, l’aveugle Sim fut si saisi que ses yeux s’ouvrirent d’un coup.', 'Hearing his daughter’s voice, blind Sim was so astonished that his eyes flew open.')],
  ], [
    W('용왕', 'yongwang', 'Roi-Dragon', 'Dragon King'),
    W('감동하다', 'gamdonghada', 'être ému', 'to be moved'),
    W('연꽃', 'yeonkkot', 'fleur de lotus', 'lotus flower'),
    W('맞이하다', 'majihada', 'accueillir, prendre pour', 'to welcome, to take as'),
    W('맹인', 'maengin', 'aveugle (personne)', 'blind person'),
    W('번쩍', 'beonjjeok', 'd’un coup', 'suddenly, in a flash'),
  ], [
    Q(('Comment Cheong revient-elle à la surface ?', 'How does Cheong return to the surface?'), [('Dans une fleur de lotus', 'In a lotus flower'), ('Sur le dos d’une tortue', 'On a turtle’s back'), ('Dans un bateau', 'In a boat')], 0),
    Q(('Pourquoi organise-t-elle un banquet ?', 'Why does she hold a banquet?'), [('Pour fêter son mariage', 'To celebrate her wedding'), ('Pour retrouver son père', 'To find her father'), ('Pour remercier le Roi-Dragon', 'To thank the Dragon King')], 1),
  ]),
])

KO_STORIES = [HAENIM, HEUNGBU, GYEONU, GEUMDOKKI, TOKKI, SEONNYEO, HOKBURI, KONGJWI, CHUNHYANG, SIMCHEONG, HONGGILDONG, BARI, DANGUN]

data = json.load(open(P, encoding='utf-8'))
data['stories'] = [s for s in data['stories'] if not s['level'].startswith('TOPIK')] + KO_STORIES
data['notices'] = {
  'ko': {'fr': 'Contes traditionnels coréens (domaine public), réécrits en coréen simple pour Koto Quest. La romanisation des mots aide à les prononcer.', 'en': 'Traditional Korean folk tales (public domain), retold in simple Korean for Koto Quest. The romanised words help you pronounce them.'},
}
slugs = [c['slug'] for s in data['stories'] for c in s['chapters']]
assert len(slugs) == len(set(slugs)), 'slug de chapitre en double'
for s in KO_STORIES:
    for c in s['chapters']:
        assert len(c['words']) >= 6, c['slug']
        for q in c['questions']:
            assert 0 <= q['answer'] < len(q['choices'])
json.dump(data, open(P, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(f"Contes coréens : {len(KO_STORIES)} contes, {sum(len(s['chapters']) for s in KO_STORIES)} chapitres")
