# Niveau TOPIK 5 (coréen, TOPIK II niveau 5) : 8 îles, 24 leçons et un examen blanc au format du TOPIK II.
# Saga : le chant de la princesse Bari (바리공주), qui descend au royaume des morts chercher l'eau de vie.
# Les gardiens viennent des mythes et légendes coréens (femme-escargot, Yeono et Seo-nyeo, l'enfant général,
# le garçon-arbre, Oneuri, Jacheongbi, Mago, Mujangseung).
# Usage : python3 scripts/topik5-level.py   (réécrit content/topik5/topik5.json)
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from kq_content import *

REGION = 'Terres des mythes'

# ═════════════════════════ Île 1 ═════════════════════════
W1 = WORLD('topik5-w1', ('Le rivage de l’abandon', 'The shore of abandonment'), REGION,
  ('Exprimer des vérités générales : -(으)ㄹ 뿐이다, -기 마련이다, -는 법이다.', 'Stating general truths: -(으)ㄹ 뿐이다, -기 마련이다, -는 법이다.'),
  (('La Femme-escargot', 'The Snail Bride'), '우', ('Cachée dans sa coquille, la Femme-escargot prépare en secret le repas des pêcheurs solitaires. Elle connaît les lois de la vie : énonce-les avec justesse, et elle sortira de sa coquille.', 'Hidden in her shell, the Snail Bride secretly cooks for lonely fishermen. She knows the laws of life: state them correctly, and she will come out of her shell.')),
  [CH('topik5-w1-c1', ('Ainsi va la vie', 'That’s life'), [
    L('ko-ppunida', ('Seulement : -(으)ㄹ 뿐이다', 'Only: -(으)ㄹ 뿐이다'), ('Dire qu’on ne fait qu’une chose, rien de plus.', 'Say you only do one thing, nothing more.'), 10, [
        ('-(으)ㄹ 뿐이다 = ne faire que, c’est tout : 저는 제 일을 했을 뿐이에요 (je n’ai fait que mon travail). Nom + 뿐이다 : 가진 것은 이 상자뿐이에요.', '-(으)ㄹ 뿐이다 = to only do, that’s all: 저는 제 일을 했을 뿐이에요 (I only did my job). Noun + 뿐이다: 가진 것은 이 상자뿐이에요.'),
        ('Ton modeste ou résigné, fréquent à l’écrit et dans les discours.', 'A modest or resigned tone, common in writing and speeches.'),
      ], [
        G('gram-ko-ppunida', '-(으)ㄹ 뿐이다', None, '-(eu)l ppunida', ('seulement, ne faire que', 'only, merely')),
        V('ko-beorida', '버리다', None, 'beorida', ('jeter, abandonner', 'to throw away, to abandon')),
        V('ko-gongju', '공주', None, 'gongju', ('princesse', 'princess')),
        V('ko-ttal', '딸', None, 'ttal', ('fille (enfant)', 'daughter')),
        V('ko-adeul', '아들', None, 'adeul', ('fils', 'son')),
        V('ko-sangja', '상자', None, 'sangja', ('boîte, coffre', 'box, chest')),
        V('ko-tteonaeryeogada', '떠내려가다', None, 'tteonaeryeogada', ('être emporté par le courant', 'to be swept away')),
      ], [
        ex('왕은 아들을 원했을 뿐이에요. 그래서 일곱째 딸을 버렸어요.', None, 'Le roi voulait seulement un fils. Alors il abandonna sa septième fille.', 'The king only wanted a son. So he abandoned his seventh daughter.'),
        ex('공주가 가진 것은 작은 상자뿐이었어요.', None, 'La princesse ne possédait qu’un petit coffre.', 'All the princess had was a small box.'),
      ], [
        FB(CHOOSE, '감사할 것 없어요. 저는 할 일을 ＿.', ['했을 뿐이에요', '하기 마련이에요', '할 법해요'], '했을 뿐이에요', ('Modestie : -았/었을 뿐이다.', 'Modesty: -았/었을 뿐이다.'), ('Pas besoin de me remercier : je n’ai fait que mon travail.', 'No need to thank me, I only did what I had to.')),
        PC(CHOOSE, '지금 제게 남은 것은 이 상자＿이에요.', ['뿐', '마련', '법'], '뿐', ('Nom + 뿐이다 : seulement.', 'Noun + 뿐이다: only.'), ('Tout ce qui me reste, c’est ce coffre.', 'This box is all I have left.')),
        DC(('Ton ami s’excuse de t’avoir aidé si peu.', 'Your friend apologises for helping so little.'), [('친구', '많이 도와주지 못해서 미안해요.')], ('Ton ami regrette de ne pas t’avoir beaucoup aidé.', 'Your friend is sorry not to have helped much.'), ['아니에요, 그 마음만으로도 고마울 뿐이에요.', '도와주기 마련이에요.', '도와줄 법해요.'], '아니에요, 그 마음만으로도 고마울 뿐이에요.', ('Gratitude humble : -(으)ㄹ 뿐이다.', 'Humble gratitude: -(으)ㄹ 뿐이다.')),
        TF('공주가 탄 상자는 바다로 떠내려갔어요.', ('Le coffre de la princesse a été emporté par la mer.', 'The princess’s box was swept out to sea.'), VRAI, ('떠내려갔어요 = a été emporté.', '떠내려갔어요 = was swept away.')),
      ]),
    L('ko-gi-maryeonida', ('C’est inévitable : -기 마련이다', 'It’s bound to: -기 마련이다'), ('Énoncer ce qui arrive forcément.', 'State what is bound to happen.'), 10, [
        ('-기 마련이다 = il est naturel que, c’est inévitable : 만남이 있으면 이별이 있기 마련이에요.', '-기 마련이다 = it’s only natural that, it’s bound to: 만남이 있으면 이별이 있기 마련이에요.'),
        ('Souvent pour consoler ou relativiser : 처음에는 누구나 실수하기 마련이에요.', 'Often used to console or put things in perspective: 처음에는 누구나 실수하기 마련이에요.'),
      ], [
        G('gram-ko-gi-maryeonida', '-기 마련이다', None, '-gi maryeonida', ('il est naturel que, c’est inévitable', 'it is natural that, it’s bound to')),
        V('ko-heeojida', '헤어지다', None, 'heeojida', ('se séparer, rompre', 'to part, to break up')),
        V('ko-mannam', '만남', None, 'mannam', ('rencontre', 'encounter, meeting')),
        V('ko-ibyeol', '이별', None, 'ibyeol', ('séparation, adieu', 'farewell, parting')),
        V('ko-sewol', '세월', None, 'sewol', ('le temps qui passe, les années', 'the years, time')),
        V('ko-heureuda', '흐르다', None, 'heureuda', ('couler, s’écouler', 'to flow')),
        V('ko-jayeonseureopda', '자연스럽다', None, 'jayeonseureopda', ('être naturel', 'to be natural')),
      ], [
        ex('만남이 있으면 이별이 있기 마련이에요.', None, 'Là où il y a des rencontres, il y a forcément des adieux.', 'Where there are meetings, there are bound to be partings.'),
        ex('세월이 흐르면 상처도 잊히기 마련이에요.', None, 'Avec le temps, même les blessures finissent par s’oublier.', 'As time passes, even wounds are bound to be forgotten.'),
      ], [
        FB(CHOOSE, '처음에는 누구나 ＿.', ['실수하기 마련이에요', '실수할 뿐이에요요', '실수한 셈이에요'], '실수하기 마련이에요', ('Ce qui arrive forcément : -기 마련이다.', 'What is bound to happen: -기 마련이다.'), ('Au début, tout le monde fait des erreurs.', 'Everyone makes mistakes at first.')),
        FB(CHOOSE, '열심히 노력하면 좋은 결과가 ＿.', ['나오기 마련이에요', '나올 리가 없어요', '나온 척해요'], '나오기 마련이에요', ('Conséquence naturelle : -기 마련이다.', 'Natural consequence: -기 마련이다.'), ('Si tu fais des efforts, les bons résultats finissent toujours par venir.', 'If you work hard, good results are bound to come.')),
        DC(('Ton amie est triste d’avoir quitté son village.', 'Your friend is sad to have left her village.'), [('친구', '고향을 떠나니까 너무 외로워요.')], ('Ton amie se sent seule loin de chez elle.', 'Your friend feels lonely away from home.'), ['처음에는 누구나 외롭기 마련이에요.', '외로울 리가 없어요.', '외로운 척하세요.'], '처음에는 누구나 외롭기 마련이에요.', ('Consoler : -기 마련이다.', 'Consoling: -기 마련이다.')),
        TF('세월이 흐르면 사람은 변하기 마련이에요.', ('Les gens ne changent jamais.', 'People never change.'), FAUX, ('변하기 마련이에요 = on change forcément.', '변하기 마련이에요 = people are bound to change.')),
      ]),
    L('ko-neun-beobida', ('C’est la règle : -는 법이다', 'That’s how it is: -는 법이다'), ('Énoncer une loi de la vie ou une règle morale.', 'State a law of life or a moral rule.'), 9, [
        ('-는 법이다 = c’est ainsi, c’est la loi : 은혜는 갚는 법이에요 (un bienfait se rend). Adjectif : -(으)ㄴ 법이다.', '-는 법이다 = that’s the way it is, it’s the rule: 은혜는 갚는 법이에요 (a kindness must be repaid). Adjective: -(으)ㄴ 법이다.'),
        ('Très proche de -기 마련이다, avec une nuance de leçon morale.', 'Very close to -기 마련이다, with a nuance of moral lesson.'),
      ], [
        G('gram-ko-neun-beobida', '-는 법이다', None, '-neun beobida', ('c’est la règle, c’est ainsi que', 'that’s the way it is, it’s the rule')),
        V('ko-jilli', '진리', None, 'jilli', ('vérité (universelle)', 'universal truth')),
        V('ko-insaeng', '인생', None, 'insaeng', ('vie (existence)', 'life (one’s existence)')),
        V('ko-daega', '대가', None, 'daega', ('prix à payer, contrepartie', 'price, cost (of something)')),
        V('ko-eunhye', '은혜', None, 'eunhye', ('bienfait, faveur', 'kindness, favour')),
        V('ko-gapda', '갚다', None, 'gapda', ('rendre, rembourser', 'to repay')),
      ], [
        ex('받은 은혜는 갚는 법이에요.', None, 'Un bienfait reçu se rend : c’est la règle.', 'A kindness received must be repaid.'),
        ex('무엇이든 대가가 있는 법이에요.', None, 'Toute chose a un prix.', 'Everything has its price.'),
      ], [
        FB(CHOOSE, '좋은 약은 입에 ＿.', ['쓴 법이에요', '쓸 뿐이에요', '쓰는 척해요'], '쓴 법이에요', ('Adjectif + -(으)ㄴ 법이다 : vérité générale.', 'Adjective + -(으)ㄴ 법이다: general truth.'), ('Un bon remède est toujours amer.', 'Good medicine always tastes bitter.')),
        FB(CHOOSE, '도움을 받으면 은혜를 ＿.', ['갚는 법이에요', '갚을 리가 없어요', '갚은 셈이에요'], '갚는 법이에요', ('Règle morale : -는 법이다.', 'Moral rule: -는 법이다.'), ('Quand on reçoit de l’aide, on rend le bienfait.', 'When you receive help, you repay the kindness.')),
        SO(('Remets dans l’ordre : « Dans la vie, il y a des hauts et des bas. »', 'Put in order: “Life has its ups and downs.”'), ['인생에는', '좋은', '날도', '나쁜', '날도', '있는', '법이에요.'], ('Vérité de la vie : -는 법이다.', 'Truth of life: -는 법이다.')),
        TF('무엇이든 공짜는 없는 법이에요.', ('La personne pense que tout a un prix.', 'The speaker thinks everything has a price.'), VRAI, ('공짜는 없는 법이에요 = rien n’est gratuit.', '공짜는 없는 법이에요 = nothing is free.')),
      ]),
  ])])

# ═════════════════════════ Île 2 ═════════════════════════
W2 = WORLD('topik5-w2', ('La pierre de Yeono', 'Yeono’s rock'), REGION,
  ('Comparer et opposer : -(으)ㄴ/는 반면에, -는가 하면, -(으)ㄴ/는 데 반해.', 'Comparing and contrasting: -(으)ㄴ/는 반면에, -는가 하면, -(으)ㄴ/는 데 반해.'),
  (('Yeono et Seo-nyeo', 'Yeono and Seo-nyeo'), '연', ('Ce couple de pêcheurs, emporté au-delà de la mer par un rocher, a emporté avec lui la lumière du soleil et de la lune. Pour la faire revenir, il faut savoir peser le pour et le contre.', 'This fishing couple, carried across the sea by a rock, took the light of the sun and moon with them. To bring it back, you must weigh up the pros and cons.')),
  [CH('topik5-w2-c1', ('D’un côté… de l’autre', 'On the one hand… on the other'), [
    L('ko-banmyeon', ('En revanche : -는 반면에', 'Whereas: -는 반면에'), ('Opposer deux aspects d’une même chose.', 'Contrast two aspects of the same thing.'), 10, [
        ('-(으)ㄴ/는 반면(에) = alors que, en revanche : 이 일은 월급이 많은 반면에 시간이 없어요.', '-(으)ㄴ/는 반면(에) = whereas, on the other hand: 이 일은 월급이 많은 반면에 시간이 없어요.'),
        ('Idéal pour présenter avantages et inconvénients (장점과 단점) à l’écrit.', 'Ideal for presenting advantages and disadvantages (장점과 단점) in writing.'),
      ], [
        G('gram-ko-banmyeon', '-(으)ㄴ/는 반면(에)', None, '-(eu)n / -neun banmyeon(e)', ('alors que, en revanche', 'whereas, on the other hand')),
        V('ko-jangjeom', '장점', None, 'jangjeom', ('avantage, point fort', 'advantage, strength')),
        V('ko-danjeom', '단점', None, 'danjeom', ('inconvénient, point faible', 'disadvantage, weakness')),
        V('ko-hae', '해', None, 'hae', ('soleil', 'sun')),
        V('ko-dal', '달', None, 'dal', ('lune ; mois', 'moon; month')),
        V('ko-bit', '빛', None, 'bit', ('lumière, rayon', 'light, ray')),
        V('ko-bawi', '바위', None, 'bawi', ('rocher', 'rock, boulder')),
      ], [
        ex('도시 생활은 편리한 반면에 공기가 나빠요.', None, 'La vie en ville est pratique, mais en revanche l’air est mauvais.', 'City life is convenient, whereas the air is bad.'),
        ex('해는 뜨거운 빛을 주는 반면에 달은 부드러운 빛을 줘요.', None, 'Le soleil donne une lumière brûlante, alors que la lune donne une lumière douce.', 'The sun gives burning light, whereas the moon gives soft light.'),
      ], [
        FB(CHOOSE, '이 집은 넓은 ＿ 교통이 불편해요.', ['반면에', '셈이에요', '법이에요'], '반면에', ('Contraste : -(으)ㄴ 반면에.', 'Contrast: -(으)ㄴ 반면에.'), ('Cette maison est grande, mais en revanche mal desservie.', 'This house is spacious, whereas transport is inconvenient.')),
        FB(CHOOSE, '이 일은 월급이 ＿ 반면에 일이 너무 많아요.', ['많은', '많는', '많을'], '많은', ('Adjectif : -(으)ㄴ 반면에.', 'Adjective: -(으)ㄴ 반면에.'), ('Ce travail paie bien, mais en revanche il y a trop de travail.', 'This job pays well, whereas there’s far too much work.')),
        DC(('Ton ami hésite entre deux appartements.', 'Your friend is torn between two flats.'), [('친구', '이 아파트 어때요?')], ('Ton ami te demande ton avis sur cet appartement.', 'Your friend asks your opinion on this flat.'), ['깨끗한 반면에 좀 비싸네요.', '깨끗할 리가 없어요.', '깨끗한 척해요.'], '깨끗한 반면에 좀 비싸네요.', ('Avantage puis inconvénient : -(으)ㄴ 반면에.', 'Pro then con: -(으)ㄴ 반면에.')),
        TF('이 방법은 장점이 많은 반면에 단점도 있어요.', ('La méthode n’a que des avantages.', 'The method has only advantages.'), FAUX, ('단점도 있어요 = il y a aussi des inconvénients.', '단점도 있어요 = it has drawbacks too.')),
      ]),
    L('ko-neunga-hamyeon', ('Certains… d’autres : -는가 하면', 'Some… others: -는가 하면'), ('Présenter des cas ou des réactions différents.', 'Present different cases or reactions.'), 10, [
        ('-는가 하면 = certains…, d’autres… ; tantôt… tantôt : 찬성하는 사람이 있는가 하면 반대하는 사람도 있어요.', '-는가 하면 = some…, others…; at times… at other times: 찬성하는 사람이 있는가 하면 반대하는 사람도 있어요.'),
        ('Adjectif : -(으)ㄴ가 하면. Fréquent dans les textes d’opinion du TOPIK.', 'Adjective: -(으)ㄴ가 하면. Common in TOPIK opinion texts.'),
      ], [
        G('gram-ko-neunga-hamyeon', '-는가 하면', None, '-neunga hamyeon', ('certains… d’autres ; tantôt… tantôt', 'some… others; at times… at other times')),
        V('ko-dayanghada', '다양하다', None, 'dayanghada', ('être varié', 'to be diverse, to be varied')),
        V('ko-taedo', '태도', None, 'taedo', ('attitude', 'attitude')),
        V('ko-baneung', '반응', None, 'baneung', ('réaction', 'reaction, response')),
        V('ko-jeonhyeo', '전혀', None, 'jeonhyeo', ('pas du tout', 'not at all')),
        V('ko-mugwansimhada', '무관심하다', None, 'mugwansimhada', ('être indifférent', 'to be indifferent')),
        V('ko-jeokgeukjeok', '적극적', None, 'jeokgeukjeok', ('actif, volontaire', 'proactive, active')),
      ], [
        ex('이 소식에 기뻐하는 사람이 있는가 하면 걱정하는 사람도 있어요.', None, 'Certains se réjouissent de cette nouvelle, d’autres s’inquiètent.', 'Some people are delighted by this news, while others are worried.'),
        ex('그 아이는 적극적인가 하면 갑자기 무관심해지기도 해요.', None, 'Cet enfant est tantôt plein d’entrain, tantôt soudain indifférent.', 'That child is sometimes keen and then suddenly indifferent.'),
      ], [
        FB(CHOOSE, '아침형 인간이 ＿ 저녁형 인간도 있어요.', ['있는가 하면', '있는 반면에요', '있을 뿐이고'], '있는가 하면', ('Certains… d’autres : -는가 하면.', 'Some… others: -는가 하면.'), ('Il y a des gens du matin, et il y a aussi des gens du soir.', 'There are morning people, and there are evening people too.')),
        FB(CHOOSE, '사람들의 반응은 ＿. 좋아하는 사람이 있는가 하면 싫어하는 사람도 있어요.', ['다양했어요', '전혀 없었어요', '무관심했어요요'], '다양했어요', ('Les réactions étaient variées.', 'Reactions were varied.'), ('Les réactions ont été diverses : certains ont aimé, d’autres non.', 'Reactions varied: some liked it, others didn’t.')),
        SO(('Remets dans l’ordre : « Certains travaillent, d’autres se reposent. »', 'Put in order: “Some work, others rest.”'), ['일하는', '사람이', '있는가', '하면', '쉬는', '사람도', '있어요.'], ('-는가 하면 … 도 있다.', '-는가 하면 … 도 있다.')),
        TF('정책에 대해 적극적으로 찬성하는 사람이 있는가 하면 전혀 관심이 없는 사람도 있어요.', ('Tout le monde a la même réaction.', 'Everyone reacts in the same way.'), FAUX, ('-는가 하면 introduit des réactions différentes.', '-는가 하면 introduces different reactions.')),
      ]),
    L('ko-e-banhae', ('Contrairement à : -는 데 반해', 'Unlike: -는 데 반해'), ('Comparer deux données ou deux groupes.', 'Compare two figures or two groups.'), 9, [
        ('-(으)ㄴ/는 데 반해 = tandis que, contrairement à : 도시 인구는 증가하는 데 반해 농촌 인구는 감소하고 있다. Nom + 에 반해.', '-(으)ㄴ/는 데 반해 = while, unlike: 도시 인구는 증가하는 데 반해 농촌 인구는 감소하고 있다. Noun + 에 반해.'),
        ('Très fréquent pour décrire un graphique à l’épreuve d’écriture.', 'Very common when describing a chart in the writing paper.'),
      ], [
        G('gram-ko-e-banhae', '-(으)ㄴ/는 데 반해', None, '-(eu)n / -neun de banhae', ('tandis que, contrairement à', 'while, unlike')),
        V('ko-dosi', '도시', None, 'dosi', ('ville', 'city')),
        V('ko-nongchon', '농촌', None, 'nongchon', ('campagne, zone rurale', 'countryside, rural area')),
        V('ko-ingu', '인구', None, 'ingu', ('population', 'population')),
        V('ko-jeunggahada', '증가하다', None, 'jeunggahada', ('augmenter (soutenu)', 'to increase (formal)')),
        V('ko-gamsohada', '감소하다', None, 'gamsohada', ('diminuer (soutenu)', 'to decrease (formal)')),
        V('ko-chai', '차이', None, 'chai', ('différence, écart', 'difference, gap')),
      ], [
        ex('도시 인구는 증가하는 데 반해 농촌 인구는 감소하고 있다.', None, 'La population des villes augmente, tandis que celle des campagnes diminue.', 'The urban population is increasing, while the rural population is decreasing.'),
        ex('형은 조용한 데 반해 동생은 활발해요.', None, 'L’aîné est calme, contrairement au cadet qui est plein de vie.', 'The older brother is quiet, unlike the younger one who is lively.'),
      ], [
        FB(CHOOSE, '20대는 스마트폰 사용 시간이 ＿ 60대는 짧았다.', ['긴 데 반해', '길 뿐이고', '긴 척하고'], '긴 데 반해', ('Comparaison de données : -(으)ㄴ 데 반해.', 'Comparing data: -(으)ㄴ 데 반해.'), ('Les 20-29 ans passent beaucoup de temps sur leur smartphone, tandis que les 60 ans et plus peu.', 'People in their 20s spent a long time on smartphones, while those in their 60s spent little.')),
        FB(CHOOSE, '수출은 ＿ 데 반해 수입은 증가했다.', ['감소한', '감소하는다', '감소할 뿐인'], '감소한', ('Passé : -(으)ㄴ 데 반해.', 'Past: -(으)ㄴ 데 반해.'), ('Les exportations ont baissé, tandis que les importations ont augmenté.', 'Exports fell, while imports rose.')),
        SO(('Remets dans l’ordre : « Il y a peu d’écart entre les deux. »', 'Put in order: “There is little difference between the two.”'), ['두', '사람의', '차이가', '크지', '않다.'], ('Sujet + 차이가 + prédicat.', 'Subject + 차이가 + predicate.')),
        TF('도시 인구는 증가한 데 반해 농촌 인구는 감소했다.', ('Les deux populations ont augmenté.', 'Both populations increased.'), FAUX, ('-는 데 반해 oppose une hausse et une baisse.', '-는 데 반해 contrasts a rise and a fall.')),
      ]),
  ])])

# ═════════════════════════ Île 3 ═════════════════════════
W3 = WORLD('topik5-w3', ('La montagne de l’enfant général', 'The mountain of the child general'), REGION,
  ('Évaluer et juger : -(으)ㄹ 만하다, -(으)ㄹ 법하다, -(으)ㄹ 리가 없다.', 'Evaluating and judging: -(으)ㄹ 만하다, -(으)ㄹ 법하다, -(으)ㄹ 리가 없다.'),
  (('L’Enfant général ailé', 'The Winged Child General'), '아', ('Né avec des ailes sous les bras, l’Enfant général fut caché par ses parents qui craignaient le roi. Son cheval l’attend encore sur la montagne. Juge avec justesse ce qui est possible ou impossible.', 'Born with wings under his arms, the Child General was hidden by parents who feared the king. His horse still waits for him on the mountain. Judge rightly what is possible and what is not.')),
  [CH('topik5-w3-c1', ('Possible ou impossible ?', 'Possible or impossible?'), [
    L('ko-eul-manhada', ('Ça vaut la peine : -(으)ㄹ 만하다', 'Worth it: -(으)ㄹ 만하다'), ('Dire qu’une chose mérite d’être faite, ou qu’elle est supportable.', 'Say something is worth doing, or bearable.'), 9, [
        ('-(으)ㄹ 만하다 = valoir la peine, être digne de : 이 책은 읽을 만해요 (ce livre vaut la peine d’être lu).', '-(으)ㄹ 만하다 = to be worth doing: 이 책은 읽을 만해요 (this book is worth reading).'),
        ('Aussi : être supportable, faisable : 이 정도 일은 혼자 할 만해요. 믿을 만한 사람 = quelqu’un de fiable.', 'Also: bearable, doable: 이 정도 일은 혼자 할 만해요. 믿을 만한 사람 = a trustworthy person.'),
      ], [
        G('gram-ko-eul-manhada', '-(으)ㄹ 만하다', None, '-(eu)l manhada', ('valoir la peine, être digne de', 'to be worth (doing)')),
        V('ko-chucheonhada', '추천하다', None, 'chucheonhada', ('recommander', 'to recommend')),
        V('ko-bolgeori', '볼거리', None, 'bolgeori', ('chose à voir, attraction', 'sight, attraction')),
        V('ko-gachi-value', '가치', None, 'gachi', ('valeur', 'value, worth')),
        V('ko-jeonseol', '전설', None, 'jeonseol', ('légende', 'legend')),
        V('ko-nalgae', '날개', None, 'nalgae', ('aile', 'wing')),
        V('ko-jangsu', '장수', None, 'jangsu', ('général (guerrier)', 'general, warrior')),
      ], [
        ex('그 마을은 볼거리가 많아서 가 볼 만해요.', None, 'Ce village a beaucoup de choses à voir : il vaut le détour.', 'That village has lots to see, so it’s worth a visit.'),
        ex('아기 장수 전설은 한 번쯤 들어 볼 만한 이야기예요.', None, 'La légende de l’enfant général est une histoire qui mérite d’être entendue.', 'The legend of the child general is a story worth hearing.'),
      ], [
        FB(CHOOSE, '이 영화는 정말 ＿. 추천해요.', ['볼 만해요', '볼 리가 없어요', '본 셈이에요'], '볼 만해요', ('Valoir la peine : -(으)ㄹ 만하다.', 'Worth doing: -(으)ㄹ 만하다.'), ('Ce film vaut vraiment la peine. Je le recommande.', 'This film is really worth seeing. I recommend it.')),
        FB(CHOOSE, '그 사람은 ＿ 사람이에요. 걱정하지 마세요.', ['믿을 만한', '믿을 리가 없는', '믿는 척하는'], '믿을 만한', ('Digne de confiance : 믿을 만한.', 'Trustworthy: 믿을 만한.'), ('C’est quelqu’un de fiable. Ne t’inquiète pas.', 'He’s someone you can trust. Don’t worry.')),
        DC(('Un touriste te demande un conseil.', 'A tourist asks you for advice.'), [('관광객', '이 근처에 가 볼 만한 곳이 있어요?')], ('Le touriste demande s’il y a un endroit qui vaut la visite.', 'The tourist asks if there’s anywhere worth visiting nearby.'), ['산 위의 절이 가 볼 만해요.', '절에 갈 리가 없어요.', '가 볼 만했을 뿐이에요요.'], '산 위의 절이 가 볼 만해요.', ('Recommandation : -(으)ㄹ 만하다.', 'Recommendation: -(으)ㄹ 만하다.')),
        TF('이 정도 추위는 참을 만해요.', ('Le froid est insupportable pour la personne.', 'The speaker finds the cold unbearable.'), FAUX, ('참을 만해요 = c’est supportable.', '참을 만해요 = it’s bearable.')),
      ]),
    L('ko-eul-beophada', ('Il est vraisemblable : -(으)ㄹ 법하다', 'It’s likely: -(으)ㄹ 법하다'), ('Dire qu’une chose est plausible ou compréhensible.', 'Say something is plausible or understandable.'), 9, [
        ('-(으)ㄹ 법하다 = il est vraisemblable que, on peut comprendre que : 그렇게 오래 기다렸으니 화가 날 법해요.', '-(으)ㄹ 법하다 = it’s likely that, it’s understandable that: 그렇게 오래 기다렸으니 화가 날 법해요.'),
        ('Plus soutenu que -(으)ㄹ 것 같다 ; souvent pour juger la réaction de quelqu’un.', 'More formal than -(으)ㄹ 것 같다; often used to judge someone’s reaction.'),
      ], [
        G('gram-ko-eul-beophada', '-(으)ㄹ 법하다', None, '-(eu)l beophada', ('il est vraisemblable que', 'it is likely that, understandably')),
        V('ko-geureoldeuthada', '그럴듯하다', None, 'geureoldeuthada', ('être plausible', 'to be plausible')),
        V('ko-jimjakada', '짐작하다', None, 'jimjakada', ('deviner, supposer', 'to guess, to suppose')),
        V('ko-chungbunhada', '충분하다', None, 'chungbunhada', ('être suffisant', 'to be enough')),
        V('ko-silmanghada', '실망하다', None, 'silmanghada', ('être déçu', 'to be disappointed')),
        V('ko-ohaehada', '오해하다', None, 'ohaehada', ('mal comprendre', 'to misunderstand')),
        V('ko-somunnada', '소문나다', None, 'somunnada', ('se répandre (rumeur), devenir célèbre', 'to get around (rumour), to become well known')),
      ], [
        ex('그렇게 말하면 오해할 법해요.', None, 'Si tu le dis comme ça, on peut comprendre qu’il se méprenne.', 'If you say it like that, he may well misunderstand.'),
        ex('그 정도 실력이면 소문날 법하지요.', None, 'Avec un tel talent, normal que ça se sache.', 'With that much skill, it’s no wonder word got around.'),
      ], [
        FB(CHOOSE, '약속을 세 번이나 어겼으니 친구가 ＿.', ['실망할 법해요', '실망할 만해요요', '실망할 뿐이에요'], '실망할 법해요', ('Réaction compréhensible : -(으)ㄹ 법하다.', 'Understandable reaction: -(으)ㄹ 법하다.'), ('Tu as manqué trois fois à ta parole : normal que ton ami soit déçu.', 'You broke your promise three times, so it’s understandable your friend is disappointed.')),
        FB(CHOOSE, '그 이야기는 ＿ 사실이 아니에요.', ['그럴듯하지만', '그럴듯한 데 반해', '그럴듯할 법해서'], '그럴듯하지만', ('Plausible, mais… : -지만.', 'Plausible, but…: -지만.'), ('Cette histoire est plausible, mais ce n’est pas vrai.', 'That story sounds plausible but it isn’t true.')),
        SO(('Remets dans l’ordre : « On aurait pu le deviner. »', 'Put in order: “We could have guessed it.”'), ['충분히', '짐작할', '법했어요.'], ('Adverbe + -(으)ㄹ 법했다.', 'Adverb + -(으)ㄹ 법했다.')),
        TF('그렇게 오래 기다렸으니 화가 날 법해요.', ('La personne trouve la colère compréhensible.', 'The speaker finds the anger understandable.'), VRAI, ('화가 날 법해요 = on comprend qu’il soit en colère.', '화가 날 법해요 = it’s understandable to be angry.')),
      ]),
    L('ko-eul-riga-eopda', ('Impossible que : -(으)ㄹ 리가 없다', 'No way that: -(으)ㄹ 리가 없다'), ('Affirmer qu’une chose est impossible.', 'Say something cannot be true.'), 9, [
        ('-(으)ㄹ 리가 없다 = il est impossible que, ça ne peut pas être : 그 사람이 거짓말을 할 리가 없어요.', '-(으)ㄹ 리가 없다 = there’s no way that: 그 사람이 거짓말을 할 리가 없어요.'),
        ('Souvent avec 설마 (tout de même pas) : 설마 그럴 리가요! Au passé : -았/었을 리가 없다.', 'Often with 설마 (surely not): 설마 그럴 리가요! In the past: -았/었을 리가 없다.'),
      ], [
        G('gram-ko-eul-riga-eopda', '-(으)ㄹ 리가 없다', None, '-(eu)l riga eopda', ('il est impossible que', 'there is no way that')),
        V('ko-geojinmal', '거짓말', None, 'geojinmal', ('mensonge', 'lie')),
        V('ko-jeongjikada', '정직하다', None, 'jeongjikada', ('être honnête', 'to be honest')),
        V('ko-uisimhada', '의심하다', None, 'uisimhada', ('soupçonner, douter', 'to suspect, to doubt')),
        V('ko-hwaksilhada', '확실하다', None, 'hwaksilhada', ('être certain', 'to be certain')),
        V('ko-seolma', '설마', None, 'seolma', ('tout de même pas…', 'surely not')),
        V('ko-baesinhada', '배신하다', None, 'baesinhada', ('trahir', 'to betray')),
      ], [
        ex('그렇게 정직한 사람이 거짓말을 할 리가 없어요.', None, 'Une personne aussi honnête ne peut pas mentir.', 'There’s no way such an honest person would lie.'),
        ex('설마 친구가 나를 배신했을 리가 없어요.', None, 'Mon ami ne m’a tout de même pas trahi, c’est impossible.', 'Surely my friend can’t have betrayed me.'),
      ], [
        FB(CHOOSE, '어제 분명히 문을 잠갔어요. 문이 열려 있을 ＿.', ['리가 없어요', '법해요', '만해요'], '리가 없어요', ('Impossibilité : -(으)ㄹ 리가 없다.', 'Impossibility: -(으)ㄹ 리가 없다.'), ('Hier j’ai bien fermé la porte à clé. Elle ne peut pas être ouverte.', 'I definitely locked the door yesterday. There’s no way it’s open.')),
        FB(CHOOSE, '그 사람이 벌써 ＿ 리가 없어요. 아까 출발했거든요.', ['도착했을', '도착하는', '도착한'], '도착했을', ('Passé : -았/었을 리가 없다.', 'Past: -았/었을 리가 없다.'), ('Il ne peut pas être déjà arrivé : il est parti tout à l’heure.', 'He can’t have arrived already. He only left a moment ago.')),
        DC(('Ton collègue soupçonne un ami commun.', 'Your colleague suspects a mutual friend.'), [('동료', '민수 씨가 돈을 가져간 것 같아요.')], ('Ton collègue pense que Minsu a pris l’argent.', 'Your colleague thinks Minsu took the money.'), ['설마요. 민수 씨가 그럴 리가 없어요.', '민수 씨가 그럴 만해요.', '가져가기 마련이에요.'], '설마요. 민수 씨가 그럴 리가 없어요.', ('Protester : 그럴 리가 없다.', 'Protesting: 그럴 리가 없다.')),
        TF('그가 거짓말을 했을 리가 없어요.', ('La personne est sûre qu’il a menti.', 'The speaker is sure he lied.'), FAUX, ('했을 리가 없어요 = impossible qu’il l’ait fait.', '했을 리가 없어요 = he can’t have done it.')),
      ]),
  ])])

# ═════════════════════════ Île 4 ═════════════════════════
W4 = WORLD('topik5-w4', ('Le déluge et le garçon-arbre', 'The flood and the tree boy'), REGION,
  ('Conditions et causes à l’écrit : -는 한, -기에, -(으)므로.', 'Written conditions and causes: -는 한, -기에, -(으)므로.'),
  (('Le Garçon-arbre', 'The Tree Boy'), '목', ('Fils d’un arbre et d’une fée, il survécut au grand déluge accroché à son père-arbre, en sauvant fourmis et moustiques. Il ne parle qu’une langue soutenue et précise.', 'Son of a tree and a fairy, he survived the great flood clinging to his tree father, saving ants and mosquitoes along the way. He speaks only a formal, precise language.')),
  [CH('topik5-w4-c1', ('Tant que, puisque', 'As long as, since'), [
    L('ko-neun-han', ('Tant que : -는 한', 'As long as: -는 한'), ('Poser une condition qui dure.', 'Set a lasting condition.'), 10, [
        ('-는 한 = tant que, du moment que : 희망을 버리지 않는 한 길은 있어요. Au passé : -(으)ㄴ 한.', '-는 한 = as long as: 희망을 버리지 않는 한 길은 있어요. Past: -(으)ㄴ 한.'),
        ('Fréquent dans les promesses et les règlements : 특별한 일이 없는 한 참석하겠습니다.', 'Common in promises and regulations: 특별한 일이 없는 한 참석하겠습니다.'),
      ], [
        G('gram-ko-neun-han', '-는 한', None, '-neun han', ('tant que, du moment que', 'as long as')),
        V('ko-saranamda', '살아남다', None, 'saranamda', ('survivre', 'to survive')),
        V('ko-ppajida', '빠지다', None, 'ppajida', ('tomber (dans), se noyer ; manquer', 'to fall into; to be missing')),
        V('ko-gujohada', '구조하다', None, 'gujohada', ('secourir', 'to rescue')),
        V('ko-huimang', '희망', None, 'huimang', ('espoir', 'hope')),
        V('ko-beotida', '버티다', None, 'beotida', ('tenir bon', 'to hold out, to endure')),
        V('ko-jonjaehada', '존재하다', None, 'jonjaehada', ('exister', 'to exist')),
      ], [
        ex('희망을 버리지 않는 한 살아남을 수 있어요.', None, 'Tant qu’on ne renonce pas à l’espoir, on peut survivre.', 'As long as you don’t give up hope, you can survive.'),
        ex('특별한 일이 없는 한 회의에 참석하겠습니다.', None, 'Sauf imprévu, j’assisterai à la réunion.', 'Unless something comes up, I will attend the meeting.'),
      ], [
        FB(CHOOSE, '포기하지 ＿ 기회는 다시 와요.', ['않는 한', '않은 반면에', '않을 리가'], '않는 한', ('Condition durable : -는 한.', 'Lasting condition: -는 한.'), ('Tant que tu n’abandonnes pas, l’occasion reviendra.', 'As long as you don’t give up, the chance will come again.')),
        FB(CHOOSE, '제가 ＿ 한 아무도 너를 괴롭히지 못할 거야.', ['살아 있는', '살아 있던', '살아 있을'], '살아 있는', ('Verbe : -는 한.', 'Verb: -는 한.'), ('Tant que je serai en vie, personne ne pourra te faire de mal.', 'As long as I’m alive, no one will be able to hurt you.')),
        SO(('Remets dans l’ordre : « Tant qu’il n’y a pas de raison particulière, je viendrai. »', 'Put in order: “Unless there’s a particular reason, I’ll come.”'), ['특별한', '이유가', '없는', '한', '오겠습니다.'], ('Condition -는 한 + promesse.', 'Condition -는 한 + promise.')),
        TF('나무를 붙잡고 버티는 한 물에 빠지지 않을 거예요.', ('Tant qu’il tient l’arbre, il ne se noiera pas.', 'As long as he holds on to the tree, he won’t drown.'), VRAI, ('버티는 한 = tant qu’il tient bon.', '버티는 한 = as long as he holds on.')),
      ]),
    L('ko-gie', ('Comme (écrit) : -기에', 'Since (written): -기에'), ('Donner la raison d’un jugement ou d’une décision, à l’écrit.', 'Give the reason for a judgement or decision, in writing.'), 9, [
        ('-기에 = comme, étant donné que (style soutenu) : 상황이 위급하기에 바로 구조하기로 했다.', '-기에 = as, given that (formal style): 상황이 위급하기에 바로 구조하기로 했다.'),
        ('Pas d’ordre ni de proposition après -기에. On l’entend aussi dans 내가 보기에는 (à mon avis).', 'No command or suggestion after -기에. Also heard in 내가 보기에는 (in my view).'),
      ], [
        G('gram-ko-gie', '-기에', None, '-gie', ('comme, étant donné que (soutenu)', 'as, given that (formal)')),
        V('ko-pandanhada', '판단하다', None, 'pandanhada', ('juger, estimer', 'to judge')),
        V('ko-gyeoljeong', '결정', None, 'gyeoljeong', ('décision', 'decision')),
        V('ko-sanghwang', '상황', None, 'sanghwang', ('situation (état des choses)', 'situation, state of affairs')),
        V('ko-wigeupada', '위급하다', None, 'wigeupada', ('être critique, urgent', 'to be critical, to be urgent')),
        V('ko-naemilda', '내밀다', None, 'naemilda', ('tendre, avancer', 'to hold out, to stick out')),
        V('ko-gaemi', '개미', None, 'gaemi', ('fourmi', 'ant')),
      ], [
        ex('개미들이 물에 빠져 있기에 소년은 나뭇가지를 내밀었다.', None, 'Comme des fourmis se noyaient, le garçon leur tendit une branche.', 'Since some ants were drowning, the boy held out a branch.'),
        ex('제가 보기에는 그 결정이 옳은 것 같아요.', None, 'À mon avis, cette décision est la bonne.', 'In my view, that decision seems right.'),
      ], [
        FB(CHOOSE, '상황이 ＿ 바로 구조대를 불렀다.', ['위급하기에', '위급하는 한', '위급한 척'], '위급하기에', ('Raison (écrit) : -기에.', 'Reason (written): -기에.'), ('La situation étant critique, on appela aussitôt les secours.', 'As the situation was critical, the rescue team was called at once.')),
        FB(CHOOSE, '제가 ＿ 이 계획은 문제가 없어요.', ['보기에는', '보는 한은', '볼 리가'], '보기에는', ('Expression figée : 보기에는 (à mon avis).', 'Set phrase: 보기에는 (in my view).'), ('À mon avis, ce projet ne pose pas de problème.', 'In my view, there’s nothing wrong with this plan.')),
        SO(('Remets dans l’ordre : « Comme il pleuvait, l’événement a été reporté. »', 'Put in order: “As it was raining, the event was postponed.”'), ['비가', '많이', '오기에', '행사를', '미루었다.'], ('Cause -기에 + décision au passé.', 'Cause -기에 + decision in the past.')),
        TF('소년은 개미를 구하기에 나뭇가지를 내밀었다.', ('Le garçon a tendu une branche.', 'The boy held out a branch.'), VRAI, ('나뭇가지를 내밀었다 = il a tendu une branche.', '나뭇가지를 내밀었다 = he held out a branch.')),
      ]),
    L('ko-eumeuro', ('Parce que (formel) : -(으)므로', 'Because (formal): -(으)므로'), ('Expliquer une cause dans un texte officiel ou scientifique.', 'Explain a cause in an official or scientific text.'), 9, [
        ('-(으)므로 = parce que, attendu que (écrit formel) : 비가 많이 오므로 주의하시기 바랍니다.', '-(으)므로 = because, whereas (formal writing): 비가 많이 오므로 주의하시기 바랍니다.'),
        ('Avec 따라서 (par conséquent), il structure les textes argumentatifs : 원인 → 결과.', 'With 따라서 (therefore), it structures argumentative texts: cause → effect.'),
      ], [
        G('gram-ko-eumeuro', '-(으)므로', None, '-(eu)meuro', ('parce que (écrit formel)', 'because (formal writing)')),
        V('ko-ttaraseo', '따라서', None, 'ttaraseo', ('par conséquent', 'therefore')),
        V('ko-wonin', '원인', None, 'wonin', ('cause', 'cause')),
        V('ko-yeonghyang', '영향', None, 'yeonghyang', ('influence, impact', 'influence, impact')),
        V('ko-juuihada', '주의하다', None, 'juuihada', ('prendre garde', 'to pay attention, to take care')),
        V('ko-balsaenghada', '발생하다', None, 'balsaenghada', ('se produire, survenir', 'to occur')),
        V('ko-yebanghada', '예방하다', None, 'yebanghada', ('prévenir', 'to prevent')),
      ], [
        ex('홍수가 발생할 수 있으므로 강가에 가지 마십시오.', None, 'Des inondations pouvant se produire, n’allez pas au bord de la rivière.', 'As flooding may occur, do not go near the river.'),
        ex('운동은 병을 예방하므로 꾸준히 하는 것이 좋다.', None, 'Le sport prévient les maladies : il est donc bon d’en faire régulièrement.', 'Exercise prevents illness, so it is good to do it regularly.'),
      ], [
        FB(CHOOSE, '길이 ＿ 운전에 주의하시기 바랍니다.', ['미끄러우므로', '미끄러울 뿐', '미끄러운 척'], '미끄러우므로', ('Avis officiel : -(으)므로.', 'Official notice: -(으)므로.'), ('La route étant glissante, nous vous prions de conduire prudemment.', 'As the road is slippery, please drive carefully.')),
        FB(CHOOSE, '이 문제는 여러 원인이 있다. ＿ 한 가지 방법으로 해결하기 어렵다.', ['따라서', '설마', '하마터면'], '따라서', ('Conséquence logique : 따라서.', 'Logical consequence: 따라서.'), ('Ce problème a plusieurs causes. Par conséquent, il est difficile à résoudre d’une seule manière.', 'This problem has several causes. Therefore it is hard to solve in a single way.')),
        SO(('Remets dans l’ordre : « Le climat influence l’agriculture. »', 'Put in order: “The climate influences farming.”'), ['기후는', '농사에', '큰', '영향을', '준다.'], ('Sujet + 에 영향을 주다.', 'Subject + 에 영향을 주다.')),
        TF('사고가 발생할 수 있으므로 주의해야 한다.', ('Le texte invite à la prudence.', 'The text calls for caution.'), VRAI, ('주의해야 한다 = il faut faire attention.', '주의해야 한다 = one must be careful.')),
      ]),
  ])])

# ═════════════════════════ Île 5 ═════════════════════════
W5 = WORLD('topik5-w5', ('Le jardin de Wondangcheon', 'The garden of Wondangcheon'), REGION,
  ('Bilan, apparences et accidents évités : -(으)ㄴ 셈이다, -(으)ㄴ 척하다, -(으)ㄹ 뻔하다.', 'Taking stock, appearances and near misses: -(으)ㄴ 셈이다, -(으)ㄴ 척하다, -(으)ㄹ 뻔하다.'),
  (('Oneuri, l’enfant sans parents', 'Oneuri, the Child Without Parents'), '오', ('Née de nulle part sur une plaine de Jeju, Oneuri chercha ses parents jusqu’au jardin des saisons. Elle déteste ceux qui font semblant : sois franc avec elle.', 'Born from nowhere on a Jeju plain, Oneuri searched for her parents all the way to the garden of the seasons. She hates pretenders: be frank with her.')),
  [CH('topik5-w5-c1', ('En somme', 'All in all'), [
    L('ko-eun-semida', ('Cela revient à : -(으)ㄴ 셈이다', 'It amounts to: -(으)ㄴ 셈이다'), ('Faire le bilan : en somme, pratiquement.', 'Sum up: in effect, practically.'), 10, [
        ('-(으)ㄴ/는 셈이다 = cela revient à, c’est comme si : 열 명 중 아홉 명이 왔으니 다 온 셈이에요 (neuf sur dix sont venus : pratiquement tout le monde est là).', '-(으)ㄴ/는 셈이다 = it amounts to, it’s as if: 열 명 중 아홉 명이 왔으니 다 온 셈이에요 (nine out of ten came, so practically everyone came).'),
        ('Avec 거의 (presque), 마찬가지 (pareil), 절반 (moitié) : 일을 절반쯤 끝낸 셈이에요.', 'With 거의 (almost), 마찬가지 (the same), 절반 (half): 일을 절반쯤 끝낸 셈이에요.'),
      ], [
        G('gram-ko-eun-semida', '-(으)ㄴ/는 셈이다', None, '-(eu)n / -neun semida', ('cela revient à, c’est comme si', 'it amounts to, practically')),
        V('ko-geoui', '거의', None, 'geoui', ('presque', 'almost')),
        V('ko-gyejeol', '계절', None, 'gyejeol', ('saison', 'season')),
        V('ko-bumo', '부모', None, 'bumo', ('parents', 'parents')),
        V('ko-pyeongsaeng', '평생', None, 'pyeongsaeng', ('toute la vie', 'one’s whole life')),
        V('ko-machangaji', '마찬가지', None, 'machangaji', ('la même chose, pareil', 'the same')),
        V('ko-jeolban', '절반', None, 'jeolban', ('la moitié', 'half')),
      ], [
        ex('열 명 중에 아홉 명이 왔으니까 거의 다 온 셈이에요.', None, 'Neuf personnes sur dix sont venues : pratiquement tout le monde est là.', 'Nine out of ten came, so practically everyone came.'),
        ex('이 숙제는 절반쯤 끝낸 셈이에요.', None, 'J’ai fait la moitié de ces devoirs, en somme.', 'I’ve done about half of this homework, in effect.'),
      ], [
        FB(CHOOSE, '이십 년을 여기서 살았으니 여기가 고향인 ＿.', ['셈이에요', '척해요', '뻔해요'], '셈이에요', ('Bilan : -인 셈이다.', 'Summing up: -인 셈이다.'), ('J’ai vécu ici vingt ans : c’est pratiquement ma ville natale.', 'I’ve lived here twenty years, so it’s practically my hometown.')),
        FB(CHOOSE, '하루에 세 시간씩 공부하니까 일주일에 스물한 시간 ＿ 셈이에요.', ['공부하는', '공부할', '공부했을'], '공부하는', ('Fait habituel : -는 셈이다.', 'Habitual fact: -는 셈이다.'), ('J’étudie trois heures par jour, ce qui fait vingt et une heures par semaine.', 'I study three hours a day, which comes to twenty-one hours a week.')),
        DC(('Ton ami t’aide à déménager presque tous les meubles.', 'Your friend helps move almost all the furniture.'), [('친구', '이제 상자 두 개만 남았어요.')], ('Ton ami dit qu’il ne reste que deux cartons.', 'Your friend says only two boxes are left.'), ['그럼 이사가 거의 끝난 셈이네요.', '이사가 끝날 리가 없어요.', '끝난 척해요.'], '그럼 이사가 거의 끝난 셈이네요.', ('Bilan : 거의 … 셈이다.', 'Summing up: 거의 … 셈이다.')),
        TF('오늘이는 평생 부모를 찾아다닌 셈이에요.', ('Oneuri a cherché ses parents pendant presque toute sa vie.', 'Oneuri spent practically her whole life looking for her parents.'), VRAI, ('평생 … 셈이에요 = pratiquement toute sa vie.', '평생 … 셈이에요 = practically all her life.')),
      ]),
    L('ko-neun-cheok', ('Faire semblant : -는 척하다', 'Pretending: -는 척하다'), ('Dire que quelqu’un fait semblant.', 'Say someone is pretending.'), 9, [
        ('-(으)ㄴ/는 척하다 = faire semblant : 모르는 척하다 (faire l’ignorant), 자는 척하다, 아픈 척하다.', '-(으)ㄴ/는 척하다 = to pretend: 모르는 척하다 (to play dumb), 자는 척하다, 아픈 척하다.'),
        ('On dit aussi -(으)ㄴ/는 체하다. Le contraire de la franchise : 솔직하게 말하다.', 'You can also say -(으)ㄴ/는 체하다. The opposite of frankness: 솔직하게 말하다.'),
      ], [
        G('gram-ko-neun-cheok', '-(으)ㄴ/는 척하다', None, '-(eu)n / -neun cheokada', ('faire semblant', 'to pretend')),
        V('ko-sogida', '속이다', None, 'sogida', ('tromper, duper', 'to deceive')),
        V('ko-nunchi', '눈치', None, 'nunchi', ('tact, sens de l’ambiance', 'tact, social awareness')),
        V('ko-soljikada', '솔직하다', None, 'soljikada', ('être franc', 'to be frank, to be honest')),
        V('ko-deulkida', '들키다', None, 'deulkida', ('être découvert, se faire prendre', 'to be found out')),
        V('ko-jinsim', '진심', None, 'jinsim', ('sincérité, fond du cœur', 'sincerity, true feelings')),
      ], [
        ex('동생은 숙제를 안 하려고 아픈 척했어요.', None, 'Mon petit frère a fait semblant d’être malade pour ne pas faire ses devoirs.', 'My little brother pretended to be ill to get out of his homework.'),
        ex('모르는 척하다가 결국 들켰어요.', None, 'Il faisait l’ignorant, mais il a fini par se faire prendre.', 'He played dumb but was found out in the end.'),
      ], [
        FB(CHOOSE, '엄마가 들어오자 아이는 ＿.', ['자는 척했어요', '잘 셈이었어요', '잘 뻔했어요'], '자는 척했어요', ('Faire semblant : -는 척하다.', 'Pretending: -는 척하다.'), ('Quand sa mère est entrée, l’enfant a fait semblant de dormir.', 'When his mother came in, the child pretended to be asleep.')),
        FB(CHOOSE, '잘 모르면서 ＿ 하지 마세요.', ['아는 척', '알 셈', '알 뻔'], '아는 척', ('Faire le savant : 아는 척하다.', 'Pretending to know: 아는 척하다.'), ('Ne fais pas semblant de savoir alors que tu ne sais pas.', 'Don’t pretend to know when you don’t.')),
        DC(('Ta sœur voit que tu es triste.', 'Your sister sees you are sad.'), [('언니', '괜찮은 척하지 말고 솔직하게 말해 봐.')], ('Ta sœur te demande d’arrêter de faire semblant d’aller bien.', 'Your sister asks you to stop pretending you’re fine.'), ['사실은 좀 힘들어요.', '괜찮은 셈이에요.', '괜찮을 리가 없어요.'], '사실은 좀 힘들어요.', ('On répond avec franchise.', 'You answer frankly.')),
        TF('그는 진심으로 기뻐하는 척했어요.', ('Il était sincèrement heureux.', 'He was sincerely happy.'), FAUX, ('기뻐하는 척했어요 = il faisait semblant d’être content.', '기뻐하는 척했어요 = he pretended to be pleased.')),
      ]),
    L('ko-eul-ppeonhada', ('Avoir failli : -(으)ㄹ 뻔하다', 'Nearly: -(으)ㄹ 뻔하다'), ('Raconter ce qui a failli arriver.', 'Tell what nearly happened.'), 9, [
        ('-(으)ㄹ 뻔했다 = avoir failli : 미끄러져서 넘어질 뻔했어요. Toujours au passé.', '-(으)ㄹ 뻔했다 = nearly did: 미끄러져서 넘어질 뻔했어요. Always in the past.'),
        ('Souvent avec 하마터면 (à deux doigts de) : 하마터면 기차를 놓칠 뻔했어요.', 'Often with 하마터면 (almost): 하마터면 기차를 놓칠 뻔했어요.'),
      ], [
        G('gram-ko-eul-ppeonhada', '-(으)ㄹ 뻔하다', None, '-(eu)l ppeonhada', ('avoir failli', 'to nearly (happen)')),
        V('ko-keunil', '큰일', None, 'keunil', ('catastrophe, gros problème', 'big trouble, disaster')),
        V('ko-hamateomyeon', '하마터면', None, 'hamateomyeon', ('à deux doigts de', 'almost, nearly')),
        V('ko-mikkeureojida', '미끄러지다', None, 'mikkeureojida', ('glisser', 'to slip')),
        V('ko-budichida', '부딪히다', None, 'budichida', ('se heurter', 'to bump into')),
        V('ko-gyeou', '겨우', None, 'gyeou', ('à peine, tout juste', 'barely, only just')),
        V('ko-musahi', '무사히', None, 'musahi', ('sain et sauf, sans encombre', 'safely')),
      ], [
        ex('하마터면 차에 부딪힐 뻔했어요.', None, 'J’ai failli me faire renverser par une voiture.', 'I nearly got hit by a car.'),
        ex('길을 잃어서 큰일 날 뻔했는데 겨우 무사히 도착했어요.', None, 'Je me suis perdu et ça aurait pu mal finir, mais je suis arrivé sain et sauf, tout juste.', 'I got lost and it nearly went badly, but I only just made it safely.'),
      ], [
        FB(CHOOSE, '얼음 위에서 미끄러져서 ＿.', ['넘어질 뻔했어요', '넘어지는 척했어요', '넘어진 셈이에요'], '넘어질 뻔했어요', ('A failli : -(으)ㄹ 뻔했다.', 'Nearly: -(으)ㄹ 뻔했다.'), ('J’ai glissé sur la glace et j’ai failli tomber.', 'I slipped on the ice and nearly fell.')),
        FB(CHOOSE, '＿ 약속을 잊어버릴 뻔했어요.', ['하마터면', '설마', '따라서'], '하마터면', ('하마터면 + -(으)ㄹ 뻔하다.', '하마터면 + -(으)ㄹ 뻔하다.'), ('J’ai bien failli oublier le rendez-vous.', 'I very nearly forgot the appointment.')),
        DC(('Ton ami arrive essoufflé juste à temps.', 'Your friend arrives breathless, just in time.'), [('친구', '휴, 기차 출발 일 분 전에 겨우 탔어요.')], ('Ton ami dit qu’il a attrapé le train une minute avant le départ.', 'Your friend says he caught the train a minute before it left.'), ['하마터면 놓칠 뻔했네요.', '놓친 척했네요.', '놓칠 만했네요.'], '하마터면 놓칠 뻔했네요.', ('Ce qui a failli arriver : -(으)ㄹ 뻔하다.', 'What nearly happened: -(으)ㄹ 뻔하다.')),
        TF('오늘이는 강을 건너다가 물에 빠질 뻔했어요.', ('Oneuri est tombée dans la rivière.', 'Oneuri fell into the river.'), FAUX, ('빠질 뻔했어요 = elle a failli tomber.', '빠질 뻔했어요 = she nearly fell in.')),
      ]),
  ])])

# ═════════════════════════ Île 6 ═════════════════════════
W6 = WORLD('topik5-w6', ('Les champs de Jacheongbi', 'Jacheongbi’s fields'), REGION,
  ('Progression et conséquences : -(으)ㄹ수록, -다 보면, -다가는.', 'Progression and consequences: -(으)ㄹ수록, -다 보면, -다가는.'),
  (('Jacheongbi, déesse des récoltes', 'Jacheongbi, Goddess of the Harvest'), '자', ('Cette jeune femme courageuse rapporta du ciel les graines des cinq céréales et devint la déesse de l’agriculture de Jeju. Elle n’aide que ceux qui comprennent que l’effort paie avec le temps.', 'This brave young woman brought the seeds of the five grains down from heaven and became Jeju’s goddess of farming. She only helps those who understand that effort pays off over time.')),
  [CH('topik5-w6-c1', ('À force de…', 'By dint of…'), [
    L('ko-eulsurok', ('Plus… plus : -(으)ㄹ수록', 'The more… the more: -(으)ㄹ수록'), ('Exprimer une progression proportionnelle.', 'Express a proportional progression.'), 10, [
        ('-(으)ㄹ수록 = plus…, plus… : 땀을 흘릴수록 풍년이 와요. Forme renforcée : -(으)면 -(으)ㄹ수록 (보면 볼수록 좋아요).', '-(으)ㄹ수록 = the more…, the more…: 땀을 흘릴수록 풍년이 와요. Emphatic form: -(으)면 -(으)ㄹ수록 (보면 볼수록 좋아요).'),
        ('Avec un adjectif aussi : 많을수록 좋아요 (plus il y en a, mieux c’est).', 'With adjectives too: 많을수록 좋아요 (the more the better).'),
      ], [
        G('gram-ko-eulsurok', '-(으)면 -(으)ㄹ수록', None, '-(eu)myeon -(eu)lsurok', ('plus… plus', 'the more… the more')),
        V('ko-ssiat', '씨앗', None, 'ssiat', ('graine', 'seed')),
        V('ko-simda', '심다', None, 'simda', ('planter', 'to plant')),
        V('ko-jarada', '자라다', None, 'jarada', ('grandir, pousser', 'to grow')),
        V('ko-geoduda', '거두다', None, 'geoduda', ('récolter ; obtenir', 'to harvest; to achieve')),
        V('ko-ttam', '땀', None, 'ttam', ('sueur', 'sweat')),
        V('ko-pungnyeon', '풍년', None, 'pungnyeon', ('bonne récolte, année d’abondance', 'bumper harvest')),
      ], [
        ex('땀을 많이 흘릴수록 더 많은 것을 거둘 수 있어요.', None, 'Plus on transpire, plus on récolte.', 'The more you sweat, the more you can harvest.'),
        ex('그 이야기는 들으면 들을수록 재미있어요.', None, 'Plus on écoute cette histoire, plus elle est intéressante.', 'The more you hear that story, the more interesting it gets.'),
      ], [
        FB(CHOOSE, '한국어는 공부하면 ＿ 재미있어요.', ['할수록', '하다 보면', '하다가는'], '할수록', ('Plus… plus : -(으)면 -(으)ㄹ수록.', 'The more… the more: -(으)면 -(으)ㄹ수록.'), ('Plus j’étudie le coréen, plus ça me plaît.', 'The more I study Korean, the more fun it is.')),
        FB(CHOOSE, '나이가 ＿ 건강이 중요해져요.', ['들수록', '든 셈', '들 뻔'], '들수록', ('Progression : -(으)ㄹ수록.', 'Progression: -(으)ㄹ수록.'), ('Plus on vieillit, plus la santé devient importante.', 'The older you get, the more important health becomes.')),
        SO(('Remets dans l’ordre : « Plus il y a de graines, mieux c’est. »', 'Put in order: “The more seeds, the better.”'), ['씨앗은', '많을수록', '좋아요.'], ('Adjectif + -(으)ㄹ수록.', 'Adjective + -(으)ㄹ수록.')),
        TF('씨앗을 많이 심을수록 많이 거둘 수 있어요.', ('Planter plus de graines permet de récolter plus.', 'Planting more seeds lets you harvest more.'), VRAI, ('-(으)ㄹ수록 = plus… plus.', '-(으)ㄹ수록 = the more… the more.')),
      ]),
    L('ko-da-bomyeon', ('À force de : -다 보면', 'If you keep on: -다 보면'), ('Dire qu’une action répétée finira par produire un résultat.', 'Say a repeated action will eventually lead to a result.'), 9, [
        ('-다 보면 = à force de…, si l’on continue à… : 꾸준히 연습하다 보면 실력이 늘 거예요.', '-다 보면 = if you keep on…, by doing… over time: 꾸준히 연습하다 보면 실력이 늘 거예요.'),
        ('Au passé, -다 보니(까) = à force de…, je me suis aperçu que : 매일 듣다 보니 익숙해졌어요.', 'In the past, -다 보니(까) = after doing… for a while, I found that: 매일 듣다 보니 익숙해졌어요.'),
      ], [
        G('gram-ko-da-bomyeon', '-다 보면', None, '-da bomyeon', ('à force de, si l’on continue', 'if you keep on, over time')),
        V('ko-iksukada', '익숙하다', None, 'iksukada', ('être habitué', 'to be used to')),
        V('ko-sillyeok', '실력', None, 'sillyeok', ('compétence, niveau', 'ability, skill')),
        V('ko-kkujunhi', '꾸준히', None, 'kkujunhi', ('régulièrement, avec constance', 'steadily, consistently')),
        V('ko-seupgwan', '습관', None, 'seupgwan', ('habitude', 'habit')),
        V('ko-jeojeollo', '저절로', None, 'jeojeollo', ('tout seul, spontanément', 'by itself, naturally')),
        V('ko-banbokada', '반복하다', None, 'banbokada', ('répéter', 'to repeat')),
      ], [
        ex('매일 반복하다 보면 저절로 습관이 돼요.', None, 'À force de répéter chaque jour, ça devient une habitude toute seule.', 'If you repeat it every day, it becomes a habit by itself.'),
        ex('한국 드라마를 보다 보니 한국어에 익숙해졌어요.', None, 'À force de regarder des dramas, je me suis habitué au coréen.', 'After watching Korean dramas for a while, I got used to Korean.'),
      ], [
        FB(CHOOSE, '꾸준히 ＿ 실력이 늘 거예요.', ['연습하다 보면', '연습하다가는', '연습할 뻔'], '연습하다 보면', ('Résultat positif à force : -다 보면.', 'Positive result over time: -다 보면.'), ('À force de t’entraîner régulièrement, tu progresseras.', 'If you keep practising steadily, your skills will improve.')),
        FB(CHOOSE, '이 일을 오래 ＿ 익숙해졌어요.', ['하다 보니', '하다가는', '할수록요'], '하다 보니', ('Constat après coup : -다 보니.', 'Realisation afterwards: -다 보니.'), ('À force de faire ce travail longtemps, je m’y suis habitué.', 'After doing this job for a long time, I’ve got used to it.')),
        DC(('Ton ami se décourage avec le coréen.', 'Your friend is losing heart with Korean.'), [('친구', '한국어 발음이 너무 어려워요.')], ('Ton ami trouve la prononciation coréenne trop difficile.', 'Your friend finds Korean pronunciation too hard.'), ['매일 따라 하다 보면 좋아질 거예요.', '따라 하다가는 망칠 거예요.', '어려울 리가 없어요.'], '매일 따라 하다 보면 좋아질 거예요.', ('Encourager : -다 보면.', 'Encouraging: -다 보면.')),
        TF('씨앗을 심고 기다리다 보면 저절로 자라요.', ('Les graines ne poussent jamais.', 'The seeds never grow.'), FAUX, ('저절로 자라요 = elles poussent toutes seules.', '저절로 자라요 = they grow by themselves.')),
      ]),
    L('ko-daganeun', ('Si tu continues : -다가는', 'If you go on like this: -다가는'), ('Mettre en garde contre une mauvaise habitude.', 'Warn against a bad habit.'), 9, [
        ('-다가는 = si tu continues à…, (alors malheur) : 그렇게 게으르다가는 일을 망칠 거예요. Suivi d’une conséquence négative.', '-다가는 = if you keep on…, (something bad will happen): 그렇게 게으르다가는 일을 망칠 거예요. Followed by a negative consequence.'),
        ('Souvent précédé de 이렇게/그렇게 : 그렇게 돈을 낭비하다가는 큰일 나요.', 'Often preceded by 이렇게/그렇게: 그렇게 돈을 낭비하다가는 큰일 나요.'),
      ], [
        G('gram-ko-daganeun', '-다가는', None, '-daganeun', ('si tu continues à… (avertissement)', 'if you keep on… (warning)')),
        V('ko-mangchida', '망치다', None, 'mangchida', ('gâcher, ruiner', 'to ruin')),
        V('ko-geeureuda', '게으르다', None, 'geeureuda', ('être paresseux', 'to be lazy')),
        V('ko-nangbihada', '낭비하다', None, 'nangbihada', ('gaspiller', 'to waste')),
        V('ko-gyeonggohada', '경고하다', None, 'gyeonggohada', ('avertir, mettre en garde', 'to warn')),
        V('ko-ilta', '잃다', None, 'ilta', ('perdre (la confiance, la santé)', 'to lose (trust, health)')),
        V('ko-sinroe', '신뢰', None, 'sinroe', ('confiance', 'trust')),
      ], [
        ex('그렇게 게으르다가는 한 해 농사를 망칠 거예요.', None, 'Si tu continues à être aussi paresseux, tu vas gâcher la récolte de l’année.', 'If you stay this lazy, you’ll ruin this year’s harvest.'),
        ex('거짓말을 계속하다가는 신뢰를 잃게 돼요.', None, 'À continuer de mentir, on perd la confiance des autres.', 'If you keep lying, you’ll lose people’s trust.'),
      ], [
        FB(CHOOSE, '이렇게 돈을 ＿ 나중에 후회할 거예요.', ['낭비하다가는', '낭비하다 보면요', '낭비할수록요'], '낭비하다가는', ('Avertissement : -다가는.', 'Warning: -다가는.'), ('Si tu gaspilles ton argent comme ça, tu le regretteras plus tard.', 'If you waste money like this, you’ll regret it later.')),
        FB(CHOOSE, '매일 늦게 ＿ 건강을 잃을 거예요.', ['자다가는', '자다 보니', '잘 만하면'], '자다가는', ('Mauvaise habitude → conséquence : -다가는.', 'Bad habit → consequence: -다가는.'), ('Si tu continues à te coucher tard tous les jours, tu vas perdre la santé.', 'If you keep going to bed late every day, you’ll ruin your health.')),
        DC(('Ton petit frère joue aux jeux vidéo la veille d’un examen.', 'Your little brother is gaming the night before an exam.'), [('동생', '한 판만 더 할게.')], ('Ton petit frère veut faire encore une partie.', 'Your brother wants one more game.'), ['그러다가는 시험을 망칠 거야.', '그러다 보면 잘할 거야.', '한 판 할 만해.'], '그러다가는 시험을 망칠 거야.', ('Mise en garde : 그러다가는.', 'Warning: 그러다가는.')),
        TF('여신은 게으른 농부에게 경고했어요.', ('La déesse a mis en garde le paysan paresseux.', 'The goddess warned the lazy farmer.'), VRAI, ('경고했어요 = a averti.', '경고했어요 = warned.')),
      ]),
  ])])

# ═════════════════════════ Île 7 ═════════════════════════
W7 = WORLD('topik5-w7', ('Les montagnes de Mago', 'Mago’s mountains'), REGION,
  ('Renchérir : -기는커녕, 조차, 마저.', 'Going one step further: -기는커녕, 조차, 마저.'),
  (('Mago, la géante créatrice', 'Mago, the Creator Giant'), '마', ('Mago la géante a façonné les montagnes avec la terre de sa jupe. Ses colères font trembler la péninsule : seul un récit précis, qui dit jusqu’où vont les choses, l’apaise.', 'Mago the giant shaped the mountains with earth from her skirt. Her anger shakes the peninsula: only a precise account, saying how far things go, soothes her.')),
  [CH('topik5-w7-c1', ('Pas même…', 'Not even…'), [
    L('ko-gineunkeonyeong', ('Loin de : -기는커녕', 'Far from: -기는커녕'), ('Dire qu’on a obtenu le contraire de ce qu’on attendait.', 'Say you got the opposite of what you expected.'), 10, [
        ('-기는커녕 = loin de…, au lieu de… : 칭찬을 받기는커녕 꾸중만 들었어요. Nom + 은/는커녕 : 칭찬은커녕.', '-기는커녕 = far from…, instead of…: 칭찬을 받기는커녕 꾸중만 들었어요. Noun + 은/는커녕: 칭찬은커녕.'),
        ('Souvent suivi de 오히려 (au contraire) ou de 도/조차 : 도움은커녕 방해만 됐어요.', 'Often followed by 오히려 (on the contrary) or 도/조차: 도움은커녕 방해만 됐어요.'),
      ], [
        G('gram-ko-gineunkeonyeong', '-기는커녕', None, '-gineunkeonyeong', ('loin de, au lieu de', 'far from, let alone')),
        V('ko-chingchan', '칭찬', None, 'chingchan', ('éloge, compliment', 'praise')),
        V('ko-kkujung', '꾸중', None, 'kkujung', ('réprimande', 'scolding')),
        V('ko-doum', '도움', None, 'doum', ('aide', 'help')),
        V('ko-banghae', '방해', None, 'banghae', ('gêne, dérangement', 'hindrance, disturbance')),
        V('ko-gomapda', '고맙다', None, 'gomapda', ('être reconnaissant', 'to be grateful')),
        V('ko-ohiryeo', '오히려', None, 'ohiryeo', ('au contraire, plutôt', 'rather, on the contrary')),
      ], [
        ex('도와주려고 했는데 도움은커녕 방해만 됐어요.', None, 'Je voulais aider, mais loin d’aider, je n’ai fait que gêner.', 'I wanted to help, but far from helping I only got in the way.'),
        ex('칭찬을 받기는커녕 오히려 꾸중을 들었어요.', None, 'Au lieu d’être félicité, je me suis fait réprimander.', 'Far from being praised, I was scolded instead.'),
      ], [
        FB(CHOOSE, '약을 먹었는데 낫기는＿ 더 아파요.', ['커녕', '조차', '마저'], '커녕', ('Loin de : -기는커녕.', 'Far from: -기는커녕.'), ('J’ai pris un médicament, mais loin d’aller mieux, j’ai encore plus mal.', 'I took medicine, but far from getting better I feel worse.')),
        PC(CHOOSE, '고맙다는 말＿ 화를 냈어요.', ['은커녕', '조차요', '마저요'], '은커녕', ('Nom + 은/는커녕.', 'Noun + 은/는커녕.'), ('Loin de me remercier, il s’est mis en colère.', 'Far from saying thank you, he got angry.')),
        DC(('Ton amie demande si tu t’es reposé pendant les vacances.', 'Your friend asks if you rested during the holiday.'), [('친구', '휴가 때 푹 쉬었어요?')], ('Ton amie demande si tu t’es bien reposé.', 'Your friend asks whether you had a good rest.'), ['쉬기는커녕 일만 더 했어요.', '쉬기 마련이에요.', '쉴 뻔했어요.'], '쉬기는커녕 일만 더 했어요.', ('Le contraire de l’attendu : -기는커녕.', 'The opposite of what was expected: -기는커녕.')),
        TF('비가 그치기는커녕 더 많이 와요.', ('La pluie s’est arrêtée.', 'The rain has stopped.'), FAUX, ('그치기는커녕 더 많이 = loin de s’arrêter, encore plus.', '그치기는커녕 더 많이 = far from stopping, even more.')),
      ]),
    L('ko-jocha', ('Pas même : 조차', 'Not even: 조차'), ('Souligner qu’on n’atteint même pas le minimum.', 'Stress that even the minimum isn’t reached.'), 9, [
        ('Nom + 조차 = même (pas), surtout dans une phrase négative : 너무 바빠서 밥조차 못 먹었어요.', 'Noun + 조차 = even (not), mostly in negative sentences: 너무 바빠서 밥조차 못 먹었어요.'),
        ('Avec 상상하다 : 상상조차 할 수 없어요 (on ne peut même pas l’imaginer).', 'With 상상하다: 상상조차 할 수 없어요 (you can’t even imagine it).'),
      ], [
        G('gram-ko-jocha', '조차', None, 'jocha', ('même (pas)', 'even (not)')),
        V('ko-sangsanghada', '상상하다', None, 'sangsanghada', ('imaginer', 'to imagine')),
        V('ko-kkumedo', '꿈에도', None, 'kkumedo', ('même en rêve', 'even in one’s dreams')),
        V('ko-geoin', '거인', None, 'geoin', ('géant', 'giant')),
        V('ko-chima', '치마', None, 'chima', ('jupe', 'skirt')),
        V('ko-sanmaek', '산맥', None, 'sanmaek', ('chaîne de montagnes', 'mountain range')),
        V('ko-heuk', '흙', None, 'heuk', ('terre (matière)', 'soil, earth')),
      ], [
        ex('거인 할머니가 치마로 흙을 날라 산맥을 만들었다니 상상조차 하기 어려워요.', None, 'Une grand-mère géante qui aurait formé des montagnes avec la terre de sa jupe ? C’est difficile même à imaginer.', 'A giant grandmother who made mountain ranges with earth carried in her skirt? It’s hard even to imagine.'),
        ex('너무 피곤해서 말조차 하기 싫어요.', None, 'Je suis si fatigué que je n’ai même pas envie de parler.', 'I’m so tired I don’t even want to talk.'),
      ], [
        PC(CHOOSE, '너무 바빠서 물＿ 못 마셨어요.', ['조차', '커녕', '대신'], '조차', ('Même pas (minimum) : 조차.', 'Not even (minimum): 조차.'), ('J’étais si occupé que je n’ai même pas bu d’eau.', 'I was so busy I couldn’t even drink water.')),
        PC(CHOOSE, '그런 일이 생길 줄은 꿈에＿ 몰랐어요.', ['도', '조차는', '마저도요'], '도', ('Expression figée : 꿈에도 (même en rêve).', 'Set phrase: 꿈에도 (even in one’s dreams).'), ('Je n’aurais jamais imaginé, même en rêve, que cela arriverait.', 'I never dreamed such a thing would happen.')),
        SO(('Remets dans l’ordre : « Je ne connais même pas son nom. »', 'Put in order: “I don’t even know his name.”'), ['그', '사람의', '이름조차', '몰라요.'], ('Nom + 조차 + négation.', 'Noun + 조차 + negative.')),
        TF('그 소식은 상상조차 못 했어요.', ('La personne s’attendait à cette nouvelle.', 'The speaker expected this news.'), FAUX, ('상상조차 못 했어요 = je ne l’avais même pas imaginé.', '상상조차 못 했어요 = I couldn’t even have imagined it.')),
      ]),
    L('ko-majeo', ('Même le dernier : 마저', 'Even the last: 마저'), ('Dire que même la dernière chose qui restait a disparu.', 'Say that even the last thing left is gone.'), 9, [
        ('Nom + 마저 = même (le dernier, en plus du reste) : 마지막 희망마저 사라졌어요.', 'Noun + 마저 = even (the last one, on top of everything): 마지막 희망마저 사라졌어요.'),
        ('Différence : 조차 = même pas le minimum ; 마저 = même ce qui restait. Ton souvent tragique.', 'Difference: 조차 = not even the minimum; 마저 = even what was left. Often a tragic tone.'),
      ], [
        G('gram-ko-majeo', '마저', None, 'majeo', ('même (le dernier qui restait)', 'even (the last remaining)')),
        V('ko-majimak', '마지막', None, 'majimak', ('dernier', 'last')),
        V('ko-oeropda', '외롭다', None, 'oeropda', ('se sentir seul', 'to be lonely')),
        V('ko-gyeondida', '견디다', None, 'gyeondida', ('supporter, résister', 'to bear, to withstand')),
        V('ko-namgimeopsi', '남김없이', None, 'namgimeopsi', ('sans rien laisser', 'without leaving anything')),
        V('ko-un', '운', None, 'un', ('chance (sort)', 'luck')),
      ], [
        ex('친구마저 떠나 버려서 너무 외로웠어요.', None, 'Même mon ami est parti : je me sentais terriblement seul.', 'Even my friend left, so I felt terribly lonely.'),
        ex('비에 바람마저 불어서 견디기 힘들었어요.', None, 'À la pluie s’est ajouté même le vent : c’était dur à supporter.', 'On top of the rain, even the wind blew, so it was hard to bear.'),
      ], [
        PC(CHOOSE, '돈도 없는데 마지막 희망＿ 사라졌어요.', ['마저', '커녕', '대로'], '마저', ('Même le dernier qui restait : 마저.', 'Even the last that remained: 마저.'), ('Je n’ai pas d’argent, et même mon dernier espoir s’est envolé.', 'I have no money, and even my last hope has gone.')),
        PC(CHOOSE, '운＿ 따르지 않았어요.', ['마저', '처럼', '뿐'], '마저', ('Même la chance (en plus du reste) : 마저.', 'Even luck (on top of the rest): 마저.'), ('Même la chance n’était pas de mon côté.', 'Even luck wasn’t on my side.')),
        SO(('Remets dans l’ordre : « Ils ont tout mangé, sans rien laisser. »', 'Put in order: “They ate everything, leaving nothing.”'), ['음식을', '남김없이', '다', '먹었어요.'], ('Adverbe 남김없이 + 다.', 'Adverb 남김없이 + 다.')),
        TF('가족마저 그를 믿지 않았어요.', ('Même sa famille ne le croyait pas.', 'Even his family didn’t believe him.'), VRAI, ('가족마저 = même sa famille.', '가족마저 = even his family.')),
      ]),
  ])])

# ═════════════════════════ Île 8 ═════════════════════════
W8 = WORLD('topik5-w8', ('La source de vie', 'The spring of life'), REGION,
  ('Argumenter avec style : -는 대신에, -거니와, -(으)ㄴ 이상.', 'Arguing with style: -는 대신에, -거니와, -(으)ㄴ 이상.'),
  (('Mujangseung, gardien de l’eau de vie', 'Mujangseung, Guardian of the Water of Life'), '생', ('Ce géant garde la source de l’eau de vie au bout du royaume des morts. Il exige neuf ans de service en échange d’une seule gourde. Argumente avec sagesse et fermeté.', 'This giant guards the spring of the water of life at the far end of the realm of the dead. He demands nine years of service in exchange for a single gourd. Argue with wisdom and resolve.')),
  [CH('topik5-w8-c1', ('En échange', 'In exchange'), [
    L('ko-neun-daesin', ('En échange : -는 대신에', 'Instead / in exchange: -는 대신에'), ('Remplacer une chose par une autre, ou proposer un échange.', 'Replace one thing with another, or offer an exchange.'), 10, [
        ('-는 대신(에) = au lieu de : 버스를 타는 대신에 걸어갔어요. Aussi = en échange de : 일을 도와주는 대신에 밥을 사 주세요.', '-는 대신(에) = instead of: 버스를 타는 대신에 걸어갔어요. Also = in exchange for: 일을 도와주는 대신에 밥을 사 주세요.'),
        ('Adjectif : -(으)ㄴ 대신에 (compensation) : 값이 비싼 대신에 품질이 좋아요.', 'Adjective: -(으)ㄴ 대신에 (compensation): 값이 비싼 대신에 품질이 좋아요.'),
      ], [
        G('gram-ko-neun-daesin', '-는 대신(에)', None, '-neun daesin(e)', ('au lieu de ; en échange de', 'instead of; in exchange for')),
        V('ko-jogeon', '조건', None, 'jogeon', ('condition', 'condition')),
        V('ko-saengmyeongsu', '생명수', None, 'saengmyeongsu', ('eau de vie (mythe)', 'water of life')),
        V('ko-bongsahada', '봉사하다', None, 'bongsahada', ('servir, faire du bénévolat', 'to serve, to volunteer')),
        V('ko-gyohwanhada', '교환하다', None, 'gyohwanhada', ('échanger (soutenu)', 'to exchange (formal)')),
        V('ko-kkot', '꽃', None, 'kkot', ('fleur', 'flower')),
        V('ko-yaksu', '약수', None, 'yaksu', ('eau de source bienfaisante', 'mineral spring water')),
      ], [
        ex('무장승은 생명수를 주는 대신에 구 년 동안 봉사하라는 조건을 걸었다.', None, 'Mujangseung posa une condition : neuf ans de service en échange de l’eau de vie.', 'Mujangseung set a condition: nine years of service in exchange for the water of life.'),
        ex('이 가방은 비싼 대신에 아주 튼튼해요.', None, 'Ce sac est cher, mais en contrepartie il est très solide.', 'This bag is expensive, but in return it’s very sturdy.'),
      ], [
        FB(CHOOSE, '오늘은 밖에서 먹는 ＿ 집에서 요리했어요.', ['대신에', '셈이에요', '척하고'], '대신에', ('Au lieu de : -는 대신에.', 'Instead of: -는 대신에.'), ('Aujourd’hui, au lieu de manger dehors, j’ai cuisiné à la maison.', 'Today I cooked at home instead of eating out.')),
        FB(CHOOSE, '숙제를 도와주는 대신에 저녁을 ＿.', ['사 주세요', '살 뻔했어요', '살 리가 없어요'], '사 주세요', ('Échange : -는 대신에 + demande.', 'Exchange: -는 대신에 + request.'), ('Je t’aide pour tes devoirs, en échange tu m’offres le dîner.', 'I’ll help with your homework, and in exchange you buy me dinner.')),
        DC(('Le vendeur explique le prix d’un objet.', 'The shopkeeper explains the price of an item.'), [('손님', '이건 왜 이렇게 비싸요?')], ('Le client demande pourquoi c’est si cher.', 'The customer asks why it’s so expensive.'), ['비싼 대신에 오래 쓸 수 있어요.', '비쌀 리가 없어요.', '비싼 척해요.'], '비싼 대신에 오래 쓸 수 있어요.', ('Compensation : -(으)ㄴ 대신에.', 'Compensation: -(으)ㄴ 대신에.')),
        TF('공주는 봉사하는 대신에 생명수를 얻었어요.', ('La princesse a obtenu l’eau de vie en échange de son service.', 'The princess obtained the water of life in exchange for her service.'), VRAI, ('봉사하는 대신에 = en échange de son service.', '봉사하는 대신에 = in exchange for serving.')),
      ]),
    L('ko-geoniwa', ('De plus (soutenu) : -거니와', 'Moreover (formal): -거니와'), ('Ajouter un argument avec un style soutenu.', 'Add an argument in a formal style.'), 9, [
        ('-거니와 = non seulement…, mais en plus (soutenu, écrit) : 그는 지혜롭거니와 용기도 뛰어나다.', '-거니와 = not only…, but moreover (formal, written): 그는 지혜롭거니와 용기도 뛰어나다.'),
        ('Équivalent soutenu de -(으)ㄹ 뿐만 아니라 et de -는 데다가.', 'Formal equivalent of -(으)ㄹ 뿐만 아니라 and -는 데다가.'),
      ], [
        G('gram-ko-geoniwa', '-거니와', None, '-geoniwa', ('non seulement…, de plus (soutenu)', 'not only…, moreover (formal)')),
        V('ko-jihye', '지혜', None, 'jihye', ('sagesse', 'wisdom')),
        V('ko-yonggi', '용기', None, 'yonggi', ('courage', 'courage')),
        V('ko-hyosim', '효심', None, 'hyosim', ('piété filiale', 'filial piety')),
        V('ko-gatchuda', '갖추다', None, 'gatchuda', ('posséder, réunir (des qualités)', 'to possess, to have (qualities)')),
        V('ko-ttwieonada', '뛰어나다', None, 'ttwieonada', ('être excellent, remarquable', 'to be outstanding')),
        V('ko-deok', '덕', None, 'deok', ('vertu ; grâce à', 'virtue; thanks to')),
      ], [
        ex('바리공주는 지혜롭거니와 효심도 깊었다.', None, 'La princesse Bari était sage, et de plus profondément dévouée à ses parents.', 'Princess Bari was wise and, moreover, deeply devoted to her parents.'),
        ex('이 계획은 비용도 많이 들거니와 시간도 부족하다.', None, 'Ce projet coûte cher, et de surcroît le temps manque.', 'This plan is costly and, moreover, there isn’t enough time.'),
      ], [
        FB(CHOOSE, '그는 실력도 ＿ 성격도 좋다.', ['뛰어나거니와', '뛰어날 뻔하고', '뛰어난 척하고'], '뛰어나거니와', ('Addition soutenue : -거니와.', 'Formal addition: -거니와.'), ('Il est non seulement brillant, mais il a aussi bon caractère.', 'He is not only highly skilled but also good-natured.')),
        FB(CHOOSE, '이 길은 ＿ 위험하기도 하다.', ['멀거니와', '멀기는커녕', '멀 리가 없거니와'], '멀거니와', ('Deux défauts additionnés : -거니와.', 'Two drawbacks added: -거니와.'), ('Ce chemin est long, et de plus dangereux.', 'This road is long and dangerous as well.')),
        SO(('Remets dans l’ordre : « Elle possède à la fois sagesse et courage. »', 'Put in order: “She has both wisdom and courage.”'), ['그녀는', '지혜와', '용기를', '모두', '갖추었다.'], ('Objet + 갖추다.', 'Object + 갖추다.')),
        TF('그 공주는 용기도 있거니와 지혜도 뛰어났다.', ('La princesse n’avait qu’une seule qualité.', 'The princess had only one quality.'), FAUX, ('-거니와 additionne deux qualités.', '-거니와 adds two qualities.')),
      ]),
    L('ko-eun-isang', ('Dès lors que : -(으)ㄴ 이상', 'Now that: -(으)ㄴ 이상'), ('Tirer la conséquence d’une situation qu’on ne peut plus changer.', 'Draw the consequence of a situation that can’t be changed.'), 9, [
        ('-(으)ㄴ/는 이상 = dès lors que, puisque (c’est ainsi) : 약속한 이상 지켜야 해요. Nom + 인 이상 : 학생인 이상.', '-(으)ㄴ/는 이상 = now that, since (that’s how it is): 약속한 이상 지켜야 해요. Noun + 인 이상: 학생인 이상.'),
        ('La suite exprime une obligation ou une résolution : -아/어야 하다, -겠다.', 'What follows expresses an obligation or resolution: -아/어야 하다, -겠다.'),
      ], [
        G('gram-ko-eun-isang', '-(으)ㄴ/는 이상', None, '-(eu)n / -neun isang', ('dès lors que, puisque', 'now that, since')),
        V('ko-chaegim', '책임', None, 'chaegim', ('responsabilité', 'responsibility')),
        V('ko-matda', '맡다', None, 'matda', ('se charger de', 'to take charge of')),
        V('ko-doedollida', '되돌리다', None, 'doedollida', ('revenir en arrière, annuler', 'to turn back, to undo')),
        V('ko-gago', '각오', None, 'gago', ('résolution, décision ferme', 'resolve, determination')),
        V('ko-unmyeong', '운명', None, 'unmyeong', ('destin', 'fate, destiny')),
        V('ko-jeoseung', '저승', None, 'jeoseung', ('l’au-delà', 'the afterlife')),
      ], [
        ex('저승까지 온 이상 생명수를 가지고 돌아가겠어요.', None, 'Puisque je suis venue jusque dans l’au-delà, je repartirai avec l’eau de vie.', 'Now that I’ve come all the way to the afterlife, I’ll go back with the water of life.'),
        ex('일을 맡은 이상 끝까지 책임을 져야 해요.', None, 'Dès lors qu’on a accepté une tâche, il faut l’assumer jusqu’au bout.', 'Once you’ve taken on a job, you must see it through.'),
      ], [
        FB(CHOOSE, '약속을 ＿ 반드시 지켜야 해요.', ['한 이상', '하는 셈', '할 뻔한'], '한 이상', ('Dès lors que : -(으)ㄴ 이상.', 'Now that: -(으)ㄴ 이상.'), ('Dès lors qu’on a promis, il faut tenir parole.', 'Given that you have promised, you must keep your word.')),
        PC(CHOOSE, '학생＿ 이상 공부를 열심히 해야지요.', ['인', '일', '이던'], '인', ('Nom + 인 이상.', 'Noun + 인 이상.'), ('Quand on est étudiant, il faut bien étudier.', 'Since you’re a student, you should study hard.')),
        DC(('Ton coéquipier veut abandonner le projet à mi-chemin.', 'Your teammate wants to drop the project halfway.'), [('동료', '너무 힘든데 그만둘까요?')], ('Ton coéquipier propose d’arrêter.', 'Your teammate suggests giving up.'), ['시작한 이상 끝까지 해야지요.', '시작할 리가 없어요.', '시작하는 척해요.'], '시작한 이상 끝까지 해야지요.', ('Résolution : -(으)ㄴ 이상.', 'Resolve: -(으)ㄴ 이상.')),
        TF('이미 결정한 이상 되돌릴 수 없어요.', ('La décision peut encore être annulée.', 'The decision can still be reversed.'), FAUX, ('되돌릴 수 없어요 = on ne peut pas revenir en arrière.', '되돌릴 수 없어요 = it can’t be undone.')),
      ]),
  ])])

FINAL = {
  'slug': 'topik5-final',
  'title': t(('Simulation TOPIK II — niveau 5', 'TOPIK II simulation — level 5')),
  'region': REGION,
  'description': t(('Examen blanc au format du TOPIK II (version abrégée), enrichi de questions avancées : écoute, écriture et lecture, noté sur 300. Il faut 190 points pour obtenir le niveau 5 et valider l’île.', 'Mock exam in TOPIK II format (shortened), with added advanced questions: listening, writing and reading, marked out of 300. You need 190 points to reach level 5 and clear the island.')),
  'exam': 'topik5-official',
  'chapters': [],
}

level = {
  'contentVersion': '2026.11.21',
  'level': {'code': 'TOPIK5', 'title': t(('Avancé : nuancer et argumenter en coréen', 'Advanced: nuance and argument in Korean')), 'region': REGION, 'order': 12},
  'notice': t(('Les listes de vocabulaire de Koto Quest sont alignées sur les compétences attendues au TOPIK II (niveau 5) mais ne constituent pas des listes officielles du TOPIK.', 'Koto Quest’s vocabulary lists are aligned with the skills expected at TOPIK II (level 5) but are not official TOPIK lists.')),
  'worlds': [W1, W2, W3, W4, W5, W6, W7, W8, FINAL],
}
t((REGION, 'Lands of Myth'))
os.makedirs(os.path.join(ROOT, 'content/topik5'), exist_ok=True)
check_and_write(level, 'content/topik5/topik5.json', ['content/n5/n5.json', 'content/n4/n4.json', 'content/n3/n3.json', 'content/n2/n2.json', 'content/n1/n1.json', 'content/topik1/topik1.json', 'content/topik2/topik2.json', 'content/topik3/topik3.json', 'content/topik4/topik4.json'])
