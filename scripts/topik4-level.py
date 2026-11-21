# Niveau TOPIK 4 (coréen, TOPIK II niveau 4) : 8 îles, 24 leçons et un examen blanc au format du TOPIK II.
# Saga : l'historien royal (사관) qui consigne les Annales de Joseon, en hiver.
# Usage : python3 scripts/topik4-level.py   (réécrit content/topik4/topik4.json)
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from kq_content import *

REGION = 'Annales de Joseon'

# ═════════════════════════ Île 1 : la salle des annales ═════════════════════════
W1 = WORLD('topik4-w1', ('La salle des annales', 'The hall of annals'), REGION,
  ('Ce qu’on a entendu dire et ce qu’on a constaté : -다면서요, -더라고요, -던데요.', 'What you heard and what you saw for yourself: -다면서요, -더라고요, -던데요.'),
  (('Le Serpent gardien du grenier', 'The Granary Guardian Serpent'), '업', ('Ce grand serpent porte-bonheur veille sur les réserves de la maison. Il ne laisse entrer que ceux qui distinguent ce qu’ils ont entendu dire de ce qu’ils ont vu de leurs yeux.', 'This great lucky serpent watches over the household stores. It only lets in those who can tell what they heard from what they saw with their own eyes.')),
  [CH('topik4-w1-c1', ('Entendu et vu', 'Heard and seen'), [
    L('ko-damyeonseoyo', ('C’est vrai que… ? : -다면서요', 'I hear that…, right?: -다면서요'), ('Vérifier une information qu’on a entendue.', 'Check a piece of information you heard.'), 10, [
        ('-다면서요? = on m’a dit que…, c’est vrai ? : 승진했다면서요? Mêmes formes que le discours indirect : -ㄴ/는다면서요 pour un verbe, -다면서요 pour un adjectif, -(이)라면서요 pour un nom.', '-다면서요? = I heard that…, is it true?: 승진했다면서요? Same forms as indirect speech: -ㄴ/는다면서요 for a verb, -다면서요 for an adjective, -(이)라면서요 for a noun.'),
        ('À l’oral, on entend souvent la forme courte -다며? entre amis.', 'In speech, friends often use the short form -다며?.'),
      ], [
        G('gram-ko-damyeonseoyo', '-다면서요?', None, '-damyeonseoyo', ('on m’a dit que…, c’est vrai ?', 'I hear that…, is that right?')),
        V('ko-seungjinhada', '승진하다', None, 'seungjinhada', ('obtenir une promotion', 'to get promoted')),
        V('ko-gisa', '기사', None, 'gisa', ('article (de presse)', 'article (in the press)')),
        V('ko-gija', '기자', None, 'gija', ('journaliste', 'journalist')),
        V('ko-inteobyu', '인터뷰', None, 'inteobyu', ('interview', 'interview')),
        V('ko-balpyohada', '발표하다', None, 'balpyohada', ('annoncer, présenter', 'to announce, to present')),
        V('ko-daehoe', '대회', None, 'daehoe', ('concours, compétition', 'contest, competition')),
      ], [
        ex('다음 달에 결혼한다면서요? 축하해요!', None, 'Il paraît que tu te maries le mois prochain ? Félicitations !', 'I hear you’re getting married next month? Congratulations!'),
        ex('그 기자가 왕을 인터뷰했다면서요?', None, 'C’est vrai que ce journaliste a interviewé le roi ?', 'Is it true that journalist interviewed the king?'),
      ], [
        FB(CHOOSE, '민수 씨, 이번에 ＿? 축하해요!', ['승진했다면서요', '승진했더라고요', '승진하던데요'], '승진했다면서요', ('Vérifier ce qu’on a entendu : -다면서요?', 'Checking something you heard: -다면서요?'), ('Minsu, il paraît que tu as été promu ? Félicitations !', 'Minsu, I hear you got promoted? Congratulations!')),
        FB(CHOOSE, '내일 결과를 ＿?', ['발표한다면서요', '발표하다면서요', '발표했으라면서요'], '발표한다면서요', ('Verbe après une voyelle : -ㄴ다면서요.', 'Verb after a vowel: -ㄴ다면서요.'), ('Il paraît qu’ils annoncent les résultats demain ?', 'I hear they announce the results tomorrow?')),
        DC(('Ta collègue a lu la nouvelle dans le journal.', 'Your colleague read the news in the paper.'), [('동료', '우리 팀이 대회에서 일 등을 했다면서요?')], ('Ta collègue veut vérifier que votre équipe a gagné le concours.', 'Your colleague wants to check your team won the contest.'), ['네, 저도 어제 들었어요.', '네, 일 등을 할 거예요.', '대회가 있다면서요요.'], '네, 저도 어제 들었어요.', ('On confirme l’information entendue.', 'You confirm what she heard.')),
        TF('그 가수가 다음 주에 새 앨범을 낸다면서요?', ('La personne vérifie une information qu’elle a entendue.', 'The speaker is checking something they heard.'), VRAI, ('-다면서요? sert à vérifier une information.', '-다면서요? is used to check information.')),
      ]),
    L('ko-deorago', ('J’ai constaté que… : -더라고요', 'I found that…: -더라고요'), ('Raconter ce qu’on a vu ou vécu soi-même.', 'Tell what you saw or experienced yourself.'), 10, [
        ('-더라고요 rapporte une chose constatée de ses propres yeux, avec un petit air de surprise : 제주도는 바람이 많이 불더라고요.', '-더라고요 reports something you saw yourself, often with a hint of surprise: 제주도는 바람이 많이 불더라고요.'),
        ('Il ne s’emploie pas pour ses propres actions volontaires : on dit 저는 어제 영화를 봤어요, pas 봤더라고요.', 'It isn’t used for your own deliberate actions: you say 저는 어제 영화를 봤어요, not 봤더라고요.'),
      ], [
        G('gram-ko-deorago', '-더라고요', None, '-deoragoyo', ('j’ai constaté que… (expérience vécue)', 'I found that… (first-hand experience)')),
        V('ko-jikjeop', '직접', None, 'jikjeop', ('directement, soi-même', 'in person, directly')),
        V('ko-bunwigi', '분위기', None, 'bunwigi', ('ambiance', 'atmosphere, mood (of a place)')),
        V('ko-saenggakboda', '생각보다', None, 'saenggakboda', ('plus que prévu, contrairement à ce qu’on pensait', 'than expected')),
        V('ko-gyeongchi', '경치', None, 'gyeongchi', ('paysage, vue', 'scenery, view')),
        V('ko-bumbida', '붐비다', None, 'bumbida', ('être bondé', 'to be crowded')),
        V('ko-chinjeolhada', '친절하다', None, 'chinjeolhada', ('être aimable', 'to be kind, friendly')),
      ], [
        ex('직접 가 보니까 경치가 정말 아름답더라고요.', None, 'En y allant moi-même, j’ai vu que le paysage était vraiment magnifique.', 'When I went myself, the scenery turned out to be really beautiful.'),
        ex('그 식당은 생각보다 사람이 많더라고요.', None, 'Ce restaurant était plus bondé que je ne le pensais.', 'That restaurant was busier than I expected.'),
      ], [
        FB(CHOOSE, '어제 시장에 가 보니까 사람들이 아주 ＿.', ['친절하더라고요', '친절했다면서요', '친절하라고요'], '친절하더라고요', ('Constat personnel : -더라고요.', 'Personal observation: -더라고요.'), ('Hier, au marché, j’ai trouvé les gens très aimables.', 'At the market yesterday, I found people very friendly.')),
        FB(CHOOSE, '주말이라서 그런지 지하철이 너무 ＿.', ['붐비더라고요', '붐볐다면서요', '붐비자고요'], '붐비더라고요', ('Ce qu’on a vu : -더라고요.', 'What you saw: -더라고요.'), ('Peut-être parce que c’était le week-end, le métro était bondé.', 'Maybe because it was the weekend, the subway was packed.')),
        DC(('Un ami te demande comment était ton voyage à Busan.', 'A friend asks how your trip to Busan was.'), [('친구', '부산 여행 어땠어요?')], ('Ton ami te demande comment s’est passé ton voyage à Busan.', 'Your friend asks how your trip to Busan was.'), ['바다가 생각보다 따뜻하더라고요.', '부산에 간다면서요?', '바다가 따뜻하라고요.'], '바다가 생각보다 따뜻하더라고요.', ('On raconte ce qu’on a constaté : -더라고요.', 'You tell what you noticed: -더라고요.')),
        TF('직접 먹어 보니까 생각보다 안 맵더라고요.', ('La personne a trouvé le plat plus épicé que prévu.', 'The speaker found the dish spicier than expected.'), FAUX, ('안 맵더라고요 = j’ai trouvé que ce n’était pas épicé.', '안 맵더라고요 = I found it wasn’t spicy.')),
      ]),
    L('ko-deondeyo', ('Pourtant j’ai vu… : -던데요', 'But I saw…: -던데요'), ('Rapporter un constat pour nuancer, objecter ou suggérer.', 'Report an observation to qualify, object or suggest.'), 9, [
        ('-던데요 rapporte aussi une chose constatée, mais laisse la phrase ouverte : 그 옷 잘 어울리던데요 (ce vêtement t’allait bien, pourtant…).', '-던데요 also reports something you noticed, but leaves the sentence open: 그 옷 잘 어울리던데요 (that outfit suited you, though…).'),
        ('Au milieu de la phrase, -던데 sert de contexte : 그 식당 맛있던데 같이 갈래요?', 'Mid-sentence, -던데 gives context: 그 식당 맛있던데 같이 갈래요?'),
      ], [
        G('gram-ko-deonde', '-던데(요)', None, '-deonde(yo)', ('j’ai vu que… pourtant (constat nuancé)', 'I noticed that… though (qualified observation)')),
        V('ko-eoullida', '어울리다', None, 'eoullida', ('aller bien (à quelqu’un) ; fréquenter', 'to suit; to hang out with')),
        V('ko-gwaenchanta', '괜찮다', None, 'gwaenchanta', ('aller bien, être correct', 'to be fine, to be OK')),
        V('ko-byeollo', '별로', None, 'byeollo', ('pas spécialement (avec négation)', 'not particularly')),
        V('ko-ingi', '인기', None, 'ingi', ('popularité, succès', 'popularity')),
        V('ko-pyeongga', '평가', None, 'pyeongga', ('évaluation, critique', 'evaluation, review')),
        V('ko-sonnim', '손님', None, 'sonnim', ('client, invité', 'customer, guest')),
      ], [
        ex('그 영화 평가가 별로 안 좋던데요.', None, 'Les critiques de ce film n’étaient pas terribles, pourtant.', 'The reviews for that film weren’t great, though.'),
        ex('그 가게 손님이 많던데 우리도 가 볼까요?', None, 'J’ai vu qu’il y avait beaucoup de clients dans cette boutique : on y va ?', 'That shop had lots of customers. Shall we try it?'),
      ], [
        FB(CHOOSE, '왜 안 사요? 그 옷 아주 잘 ＿.', ['어울리던데요', '어울린다면서요', '어울리라고요'], '어울리던데요', ('Constat qui nuance (pourquoi tu ne l’achètes pas ?) : -던데요.', 'Observation that objects (why not buy it?): -던데요.'), ('Pourquoi tu ne l’achètes pas ? Il t’allait très bien.', 'Why aren’t you buying it? It really suited you.')),
        FB(CHOOSE, '그 식당 음식이 ＿ 이번 주말에 같이 가요.', ['괜찮던데', '괜찮다면서', '괜찮자고'], '괜찮던데', ('Constat comme contexte d’une proposition : -던데.', 'Observation as context for a suggestion: -던데.'), ('La cuisine de ce restaurant était bonne : allons-y ce week-end.', 'The food at that restaurant was good, let’s go this weekend.')),
        DC(('Ton ami pense que le nouveau café n’a pas de succès.', 'Your friend thinks the new café isn’t popular.'), [('친구', '새로 생긴 카페는 인기가 없나 봐요.')], ('Ton ami suppose que le nouveau café ne marche pas.', 'Your friend guesses the new café isn’t doing well.'), ['어제 가 보니까 손님이 많던데요.', '손님이 많다면서요.', '손님이 많아야겠어요.'], '어제 가 보니까 손님이 많던데요.', ('On objecte avec ce qu’on a vu : -던데요.', 'You object with what you saw: -던데요.')),
        TF('그 책 평가가 아주 좋던데요.', ('La personne a vu que le livre était bien noté.', 'The speaker saw the book was well reviewed.'), VRAI, ('좋던데요 = j’ai vu que c’était bon.', '좋던데요 = I saw it was good.')),
      ]),
  ])])

# ═════════════════════════ Île 2 : le village sous la neige ═════════════════════════
W2 = WORLD('topik4-w2', ('Le village sous la neige', 'The snowbound village'), REGION,
  ('Faire des suppositions à partir d’indices : -는 모양이다, -나 보다, -(으)ㄹ 텐데.', 'Guessing from clues: -는 모양이다, -나 보다, -(으)ㄹ 텐데.'),
  (('Le Yagwanggwi voleur de souliers', 'The Shoe-stealing Yagwanggwi'), '야', ('La nuit du Nouvel An, ce petit fantôme essaie les souliers laissés dehors et emporte ceux qui lui vont. Lis les traces dans la neige pour deviner où il est passé.', 'On New Year’s night, this little ghost tries on the shoes left outside and steals the ones that fit. Read the tracks in the snow to guess where it went.')),
  [CH('topik4-w2-c1', ('Il semble que…', 'It seems that…'), [
    L('ko-moyangida', ('Apparemment : -는 모양이다', 'Apparently: -는 모양이다'), ('Faire une supposition fondée sur ce qu’on observe.', 'Make a guess based on what you observe.'), 10, [
        ('-(으)ㄴ/는 모양이다 = apparemment, on dirait que (d’après des indices) : 밤새 눈이 온 모양이에요 (il a apparemment neigé toute la nuit).', '-(으)ㄴ/는 모양이다 = apparently, it looks as if (from clues): 밤새 눈이 온 모양이에요 (it apparently snowed all night).'),
        ('Verbe au présent : -는 모양이다 ; passé : -(으)ㄴ 모양이다 ; adjectif : -(으)ㄴ 모양이다 ; futur : -(으)ㄹ 모양이다.', 'Present verb: -는 모양이다; past: -(으)ㄴ 모양이다; adjective: -(으)ㄴ 모양이다; future: -(으)ㄹ 모양이다.'),
      ], [
        G('gram-ko-moyangida', '-(으)ㄴ/는 모양이다', None, '-(eu)n / -neun moyangida', ('apparemment, on dirait que', 'apparently, it looks as if')),
        V('ko-baljaguk', '발자국', None, 'baljaguk', ('empreinte de pas', 'footprint')),
        V('ko-ssaida', '쌓이다', None, 'ssaida', ('s’accumuler, s’entasser', 'to pile up')),
        V('ko-sinbal', '신발', None, 'sinbal', ('chaussures', 'shoes')),
        V('ko-eopseojida', '없어지다', None, 'eopseojida', ('disparaître', 'to disappear, to go missing')),
        V('ko-heunjeok', '흔적', None, 'heunjeok', ('trace', 'trace')),
        V('ko-bamsae', '밤새', None, 'bamsae', ('toute la nuit', 'all night')),
      ], [
        ex('마당에 눈이 많이 쌓였어요. 밤새 눈이 온 모양이에요.', None, 'La neige s’est accumulée dans la cour. Il a apparemment neigé toute la nuit.', 'Snow has piled up in the yard. It must have snowed all night.'),
        ex('신발이 없어졌어요. 누가 가져간 모양이에요.', None, 'Mes chaussures ont disparu. Apparemment, quelqu’un les a prises.', 'My shoes are gone. It looks as if someone took them.'),
      ], [
        FB(CHOOSE, '발자국이 있어요. 누가 다녀간 ＿.', ['모양이에요', '모양했어요', '모양이라고요'], '모양이에요', ('Supposition d’après un indice : -(으)ㄴ 모양이에요.', 'Guess from a clue: -(으)ㄴ 모양이에요.'), ('Il y a des empreintes. Quelqu’un est passé, apparemment.', 'There are footprints. Someone seems to have come by.')),
        FB(CHOOSE, '불이 꺼져 있네요. 다들 ＿ 모양이에요.', ['자는', '잔다', '자기'], '자는', ('Verbe au présent : -는 모양이다.', 'Present verb: -는 모양이다.'), ('Les lumières sont éteintes. Tout le monde dort, apparemment.', 'The lights are off. Everyone seems to be asleep.')),
        SO(('Remets dans l’ordre : « Apparemment, il a beaucoup neigé. »', 'Put in order: “It seems to have snowed a lot.”'), ['눈이', '많이', '온', '모양이에요.'], ('Verbe au passé -(으)ㄴ + 모양이에요.', 'Past verb -(으)ㄴ + 모양이에요.')),
        TF('흔적이 없는 걸 보니 아무도 안 온 모양이에요.', ('D’après la personne, quelqu’un est venu.', 'The speaker thinks someone came.'), FAUX, ('아무도 안 온 모양이에요 = apparemment personne n’est venu.', '아무도 안 온 모양이에요 = apparently no one came.')),
      ]),
    L('ko-na-boda', ('On dirait que : -나 보다', 'It seems: -나 보다'), ('Supposer à partir de ce qu’on voit ou entend sur le moment.', 'Guess from what you see or hear in the moment.'), 9, [
        ('Verbe + -나 보다, adjectif + -(으)ㄴ가 보다 = on dirait que : 기침을 하는 걸 보니 감기에 걸렸나 봐요. 표정이 안 좋은 걸 보니 기분이 나쁜가 봐요.', 'Verb + -나 보다, adjective + -(으)ㄴ가 보다 = it seems that: 기침을 하는 걸 보니 감기에 걸렸나 봐요. 표정이 안 좋은 걸 보니 기분이 나쁜가 봐요.'),
        ('Souvent précédé de -는 걸 보니 (vu que…). On ne l’emploie pas pour soi-même.', 'Often preceded by -는 걸 보니 (seeing that…). It isn’t used about yourself.'),
      ], [
        G('gram-ko-na-boda', '-나 보다 / -(으)ㄴ가 보다', None, '-na boda / -(eu)nga boda', ('on dirait que (d’après ce qu’on voit)', 'it seems that (from what one sees)')),
        V('ko-bul', '불', None, 'bul', ('feu ; lumière', 'fire; light')),
        V('ko-kkeojida', '꺼지다', None, 'kkeojida', ('s’éteindre', 'to go out (light, fire)')),
        V('ko-gichim', '기침', None, 'gichim', ('toux', 'cough')),
        V('ko-yeol', '열', None, 'yeol', ('fièvre ; chaleur', 'fever; heat')),
        V('ko-pyojeong', '표정', None, 'pyojeong', ('expression du visage', 'facial expression')),
        V('ko-gibun', '기분', None, 'gibun', ('humeur', 'mood')),
      ], [
        ex('기침을 하는 걸 보니 감기에 걸렸나 봐요.', None, 'Vu qu’il tousse, il a dû attraper un rhume.', 'Seeing him cough, he must have caught a cold.'),
        ex('표정을 보니 기분이 좋은가 봐요.', None, 'À voir sa tête, il est de bonne humeur.', 'Judging from her face, she’s in a good mood.'),
      ], [
        FB(CHOOSE, '계속 웃는 걸 보니 좋은 일이 ＿.', ['있나 봐요', '있은가 봐요', '있더라고요'], '있나 봐요', ('있다 + -나 보다.', '있다 + -나 보다.'), ('Vu qu’il n’arrête pas de sourire, il a dû lui arriver quelque chose de bien.', 'Since he keeps smiling, something good must have happened.')),
        FB(CHOOSE, '얼굴이 빨개요. 열이 ＿.', ['많은가 봐요', '많나 봐요요', '많던가요'], '많은가 봐요', ('Adjectif : -(으)ㄴ가 보다.', 'Adjective: -(으)ㄴ가 보다.'), ('Il a le visage tout rouge. Il doit avoir beaucoup de fièvre.', 'His face is red. He must have a high fever.')),
        DC(('Les lumières de la maison d’en face sont éteintes.', 'The lights in the house opposite are off.'), [('엄마', '옆집에 불이 다 꺼졌네.')], ('Ta mère remarque que les lumières des voisins sont éteintes.', 'Your mother notices the neighbours’ lights are off.'), ['여행을 갔나 봐요.', '여행을 갈게요.', '여행을 갔다면서요?'], '여행을 갔나 봐요.', ('Supposition d’après ce qu’on voit : -나 봐요.', 'Guess from what you see: -나 봐요.')),
        TF('불이 꺼진 걸 보니 다들 나갔나 봐요.', ('La personne suppose que tout le monde est sorti.', 'The speaker guesses everyone has gone out.'), VRAI, ('나갔나 봐요 = ils sont sortis, on dirait.', '나갔나 봐요 = they seem to have gone out.')),
      ]),
    L('ko-eul-tende', ('Ça doit… : -(으)ㄹ 텐데', 'It must…: -(으)ㄹ 텐데'), ('Exprimer une supposition qui fonde une inquiétude ou un conseil.', 'Express an assumption behind a worry or a piece of advice.'), 9, [
        ('-(으)ㄹ 텐데 = ça doit sûrement… (alors) : 길이 미끄러울 텐데 조심하세요. Souvent suivi d’un conseil ou d’une proposition.', '-(으)ㄹ 텐데 = it’s probably… (so): 길이 미끄러울 텐데 조심하세요. Often followed by advice or a suggestion.'),
        ('En fin de phrase, -(으)ㄹ 텐데요 exprime une inquiétude : 늦으면 걱정하실 텐데요.', 'At the end of a sentence, -(으)ㄹ 텐데요 voices a worry: 늦으면 걱정하실 텐데요.'),
      ], [
        G('gram-ko-eul-tende', '-(으)ㄹ 텐데', None, '-(eu)l tende', ('ça doit sûrement… (supposition + conseil)', 'it’s probably… (assumption + advice)')),
        V('ko-chulchulhada', '출출하다', None, 'chulchulhada', ('avoir un petit creux', 'to be peckish')),
        V('ko-makida', '막히다', None, 'makida', ('être bouché, embouteillé', 'to be blocked, to be congested')),
        V('ko-mikkeureopda', '미끄럽다', None, 'mikkeureopda', ('être glissant', 'to be slippery')),
        V('ko-eolda', '얼다', None, 'eolda', ('geler', 'to freeze')),
        V('ko-nunsaram', '눈사람', None, 'nunsaram', ('bonhomme de neige', 'snowman')),
        V('ko-janggap', '장갑', None, 'janggap', ('gants', 'gloves')),
      ], [
        ex('길이 얼어서 미끄러울 텐데 천천히 가세요.', None, 'La route a gelé, ça doit être glissant : roulez doucement.', 'The road has frozen, it must be slippery, so go slowly.'),
        ex('출출할 텐데 떡이라도 좀 드세요.', None, 'Vous devez avoir un petit creux : prenez au moins un gâteau de riz.', 'You must be peckish, have some rice cake at least.'),
      ], [
        FB(CHOOSE, '밖이 ＿ 장갑을 끼고 나가세요.', ['추울 텐데', '추운 텐데', '추웠는 텐데'], '추울 텐데', ('Supposition + conseil : -(으)ㄹ 텐데.', 'Assumption + advice: -(으)ㄹ 텐데.'), ('Il doit faire froid dehors : mets des gants avant de sortir.', 'It must be cold outside, so wear gloves.')),
        FB(CHOOSE, '지금 출발하면 길이 ＿ 조금 있다가 가세요.', ['막힐 텐데', '막혔나 봐요', '막히더라고요'], '막힐 텐데', ('Supposition sur l’avenir avant un conseil : -(으)ㄹ 텐데.', 'Assumption about the future before advice: -(으)ㄹ 텐데.'), ('Si tu pars maintenant, ça doit bouchonner : attends un peu.', 'If you leave now, the roads will probably be jammed, so wait a bit.')),
        DC(('Ton ami part dans la neige sans manteau.', 'Your friend is heading out into the snow without a coat.'), [('친구', '잠깐 나갔다 올게요.')], ('Ton ami dit qu’il sort un moment.', 'Your friend says he’s popping out.'), ['눈이 와서 미끄러울 텐데 조심하세요.', '눈이 와서 미끄럽더라고요?', '눈사람을 만들 텐데요요.'], '눈이 와서 미끄러울 텐데 조심하세요.', ('Inquiétude + conseil : -(으)ㄹ 텐데.', 'Worry + advice: -(으)ㄹ 텐데.')),
        TF('아이들이 눈사람을 만들면 좋아할 텐데요.', ('La personne pense que les enfants seraient contents.', 'The speaker thinks the children would be pleased.'), VRAI, ('좋아할 텐데요 = ils seraient sûrement contents.', '좋아할 텐데요 = they would surely like it.')),
      ]),
  ])])

# ═════════════════════════ Île 3 : la cuisine du palais ═════════════════════════
W3 = WORLD('topik4-w3', ('La cuisine du palais', 'The palace kitchen'), REGION,
  ('Hypothèses et conditions : -다면, -았/었더라면, -거든.', 'Hypotheses and conditions: -다면, -았/었더라면, -거든.'),
  (('Jowangsin, l’esprit du foyer', 'Jowangsin, the Hearth Spirit'), '조', ('L’esprit du foyer veille sur le feu de la cuisine royale. À la fin de l’année, il monte au ciel raconter ce qui s’est passé : il ne tolère que des hypothèses bien posées.', 'The hearth spirit watches over the royal kitchen fire. At year’s end it rises to heaven to report what happened: it only accepts well-stated hypotheses.')),
  [CH('topik4-w3-c1', ('Et si…', 'What if…'), [
    L('ko-damyeon', ('Si (hypothèse) : -다면', 'If (hypothetical): -다면'), ('Poser une hypothèse peu probable ou imaginaire.', 'Make an unlikely or imaginary assumption.'), 10, [
        ('-다면 = si (hypothèse peu probable) : 복권에 당첨된다면 세계 여행을 하고 싶어요. Formes : verbe -ㄴ/는다면, adjectif -다면, nom -(이)라면.', '-다면 = if (unlikely hypothesis): 복권에 당첨된다면 세계 여행을 하고 싶어요. Forms: verb -ㄴ/는다면, adjective -다면, noun -(이)라면.'),
        ('Avec 만약 (si jamais) pour renforcer : 만약 내가 왕이라면… -(으)면 reste la condition ordinaire.', 'With 만약 (if ever) for emphasis: 만약 내가 왕이라면… -(으)면 remains the ordinary condition.'),
      ], [
        G('gram-ko-damyeon', '-다면', None, '-damyeon', ('si (hypothèse peu probable)', 'if (unlikely hypothesis)')),
        V('ko-manyak', '만약', None, 'manyak', ('si jamais, au cas où', 'if, in case')),
        V('ko-gihoe', '기회', None, 'gihoe', ('occasion, opportunité', 'opportunity, chance')),
        V('ko-bokgwon', '복권', None, 'bokgwon', ('billet de loterie', 'lottery ticket')),
        V('ko-dangcheomdoeda', '당첨되다', None, 'dangcheomdoeda', ('gagner (à un tirage)', 'to win (a draw)')),
        V('ko-segye', '세계', None, 'segye', ('monde', 'world')),
        V('ko-yeoyu', '여유', None, 'yeoyu', ('marge, temps libre, aisance', 'leeway, spare time')),
      ], [
        ex('만약 복권에 당첨된다면 뭘 하고 싶어요?', None, 'Si tu gagnais à la loterie, qu’aimerais-tu faire ?', 'If you won the lottery, what would you like to do?'),
        ex('시간 여유가 있다면 한국 요리를 배우고 싶어요.', None, 'Si j’avais du temps libre, j’aimerais apprendre la cuisine coréenne.', 'If I had spare time, I’d like to learn Korean cooking.'),
      ], [
        FB(CHOOSE, '만약 내가 왕＿ 백성을 위해 일하겠어요.', ['이라면', '이다면', '라면서'], '이라면', ('Nom + -(이)라면.', 'Noun + -(이)라면.'), ('Si j’étais roi, je travaillerais pour le peuple.', 'If I were king, I would work for the people.')),
        FB(CHOOSE, '다시 태어날 기회가 ＿ 무엇이 되고 싶어요?', ['있다면', '있는다면', '있다라면'], '있다면', ('있다 : -다면.', '있다: -다면.'), ('Si tu avais l’occasion de renaître, que voudrais-tu être ?', 'If you had the chance to be born again, what would you want to be?')),
        DC(('Ton amie rêve à voix haute.', 'Your friend is daydreaming out loud.'), [('친구', '복권에 당첨된다면 뭐 할 거예요?')], ('Ton amie te demande ce que tu ferais si tu gagnais à la loterie.', 'Your friend asks what you’d do if you won the lottery.'), ['세계 여행을 떠날 거예요.', '복권을 샀다면서요?', '당첨됐나 봐요.'], '세계 여행을 떠날 거예요.', ('On répond à l’hypothèse par un projet.', 'You answer the hypothesis with a plan.')),
        TF('시간 여유가 있다면 매일 운동할 거예요.', ('La personne fait du sport tous les jours.', 'The speaker exercises every day.'), FAUX, ('있다면 = si j’avais (hypothèse).', '있다면 = if I had (hypothesis).')),
      ]),
    L('ko-deoramyeon', ('Si j’avais… : -았/었더라면', 'If I had…: -았/었더라면'), ('Imaginer un passé différent, avec regret ou soulagement.', 'Imagine a different past, with regret or relief.'), 10, [
        ('-았/었더라면 = si (dans le passé, ce qui n’a pas eu lieu) : 조금만 일찍 출발했더라면 기차를 놓치지 않았을 거예요.', '-았/었더라면 = if (in the past, something that didn’t happen): 조금만 일찍 출발했더라면 기차를 놓치지 않았을 거예요.'),
        ('La fin est souvent -았/었을 거예요 (aurait…) ou -(으)ㄹ 뻔했어요 (a failli…) : 네가 없었더라면 큰일 날 뻔했어.', 'The ending is often -았/었을 거예요 (would have…) or -(으)ㄹ 뻔했어요 (nearly…): 네가 없었더라면 큰일 날 뻔했어.'),
      ], [
        G('gram-ko-deoramyeon', '-았/었더라면', None, '-at / -eotdeoramyeon', ('si (passé irréel)', 'if (unreal past)')),
        V('ko-jogeumman', '조금만', None, 'jogeumman', ('rien qu’un peu', 'just a little')),
        V('ko-silsu', '실수', None, 'silsu', ('erreur, faute', 'mistake')),
        V('ko-nochida', '놓치다', None, 'nochida', ('rater, manquer', 'to miss (a chance, a train)')),
        V('ko-chungbunhi', '충분히', None, 'chungbunhi', ('suffisamment', 'enough, sufficiently')),
        V('ko-dahaeng', '다행', None, 'dahaeng', ('chance, soulagement', 'good fortune, relief')),
        V('ko-sago', '사고', None, 'sago', ('accident', 'accident')),
      ], [
        ex('조금만 일찍 출발했더라면 기차를 놓치지 않았을 거예요.', None, 'Si j’étais parti un peu plus tôt, je n’aurais pas raté le train.', 'If I had left a little earlier, I wouldn’t have missed the train.'),
        ex('안전띠를 안 했더라면 큰 사고가 날 뻔했어요. 정말 다행이에요.', None, 'Sans ma ceinture, ça aurait pu être un grave accident. Quel soulagement.', 'If I hadn’t worn a seatbelt, it could have been a bad accident. What a relief.'),
      ], [
        FB(CHOOSE, '충분히 ＿ 실수하지 않았을 거예요.', ['준비했더라면', '준비한다면', '준비하더라고요'], '준비했더라면', ('Passé irréel : -았/었더라면.', 'Unreal past: -았/었더라면.'), ('Si je m’étais suffisamment préparé, je n’aurais pas fait d’erreur.', 'If I had prepared enough, I wouldn’t have made a mistake.')),
        FB(CHOOSE, '그때 그 기회를 놓치지 ＿ 지금 달라졌을 거예요.', ['않았더라면', '않는다면', '않았던데'], '않았더라면', ('Négatif : -지 않았더라면.', 'Negative: -지 않았더라면.'), ('Si je n’avais pas laissé passer cette occasion, les choses seraient différentes.', 'If I hadn’t missed that chance, things would be different now.')),
        SO(('Remets dans l’ordre : « Si tu n’avais pas été là, ça aurait été grave. »', 'Put in order: “If you hadn’t been there, it would have been serious.”'), ['네가', '없었더라면', '큰일', '날', '뻔했어.'], ('-았/었더라면 + -(으)ㄹ 뻔했다.', '-았/었더라면 + -(으)ㄹ 뻔했다.')),
        TF('미리 예약했더라면 기다리지 않았을 거예요.', ('La personne avait réservé à l’avance.', 'The speaker had booked in advance.'), FAUX, ('예약했더라면 = si j’avais réservé (ce qui n’a pas été fait).', '예약했더라면 = if I had booked (which I didn’t).')),
      ]),
    L('ko-geodeun', ('Si (alors fais…) : -거든', 'If (then do…): -거든'), ('Poser une condition avant un conseil, un ordre ou une proposition.', 'Set a condition before advice, an order or a suggestion.'), 9, [
        ('-거든 = si, au cas où, toujours suivi d’un ordre, d’un conseil ou d’une intention : 궁금한 게 있거든 언제든지 물어보세요.', '-거든 = if, should…, always followed by an order, advice or intention: 궁금한 게 있거든 언제든지 물어보세요.'),
        ('À ne pas confondre avec -거든요 en fin de phrase (explication) vu au TOPIK 3.', 'Not to be confused with sentence-final -거든요 (explanation) from TOPIK 3.'),
      ], [
        G('gram-ko-geodeun', '-거든', None, '-geodeun', ('si (+ ordre, conseil)', 'if (+ order, advice)')),
        V('ko-gunggeumhada', '궁금하다', None, 'gunggeumhada', ('se demander, être curieux de savoir', 'to wonder, to be curious')),
        V('ko-eonjedeunji', '언제든지', None, 'eonjedeunji', ('n’importe quand', 'any time')),
        V('ko-bulpyeonhada', '불편하다', None, 'bulpyeonhada', ('être inconfortable, gênant', 'to be uncomfortable, inconvenient')),
        V('ko-munuihada', '문의하다', None, 'munuihada', ('se renseigner', 'to enquire')),
        V('ko-jaeryo', '재료', None, 'jaeryo', ('ingrédient, matériau', 'ingredient, material')),
        V('ko-namda', '남다', None, 'namda', ('rester (en surplus)', 'to be left over')),
      ], [
        ex('궁금한 게 있거든 언제든지 문의하세요.', None, 'Si vous avez des questions, renseignez-vous quand vous voulez.', 'If you have any questions, feel free to ask any time.'),
        ex('재료가 남거든 내일 다시 쓰세요.', None, 'S’il reste des ingrédients, réutilise-les demain.', 'If there are ingredients left over, use them again tomorrow.'),
      ], [
        FB(CHOOSE, '불편한 점이 ＿ 말씀해 주세요.', ['있거든', '있거든요', '있더라면'], '있거든', ('Condition + demande polie : -거든.', 'Condition + polite request: -거든.'), ('Si quelque chose vous gêne, dites-le-moi.', 'If anything is inconvenient, please tell me.')),
        FB(CHOOSE, '집에 ＿ 전화해 줘.', ['도착하거든', '도착했더라면', '도착하더라고'], '도착하거든', ('Quand tu arriveras (alors appelle) : -거든.', 'When you arrive (then call): -거든.'), ('Appelle-moi quand tu seras arrivé à la maison.', 'Call me when you get home.')),
        DC(('Un client hésite devant le menu du palais.', 'A customer hesitates over the palace menu.'), [('손님', '이 음식에 어떤 재료가 들어가요?')], ('Le client demande quels ingrédients contient le plat.', 'The customer asks what ingredients are in the dish.'), ['궁금하시거든 요리사에게 문의해 보세요.', '궁금했더라면 물어봤을 거예요.', '재료가 남았나 봐요.'], '궁금하시거든 요리사에게 문의해 보세요.', ('-거든 + conseil.', '-거든 + advice.')),
        TF('시간이 있거든 우리 집에 들르세요.', ('C’est une invitation sous condition.', 'It is a conditional invitation.'), VRAI, ('있거든 = si tu as (le temps), passe.', '있거든 = if you have (time), drop by.')),
      ]),
  ])])

# ═════════════════════════ Île 4 : le pavillon de la déesse ═════════════════════════
W4 = WORLD('topik4-w4', ('Le pavillon de Samsin', 'Samsin’s pavilion'), REGION,
  ('La concession : -더라도, -는데도, -아/어 봤자.', 'Concession: -더라도, -는데도, -아/어 봤자.'),
  (('Grand-mère Samsin', 'Grandmother Samsin'), '신', ('La déesse qui veille sur les naissances a vu passer bien des épreuves. Elle n’accorde sa bénédiction qu’à ceux qui persévèrent malgré tout.', 'The goddess who watches over births has seen many hardships. She grants her blessing only to those who persevere in spite of everything.')),
  [CH('topik4-w4-c1', ('Malgré tout', 'In spite of everything'), [
    L('ko-deorado', ('Même si : -더라도', 'Even if: -더라도'), ('Dire qu’une chose ne changera pas, même dans une situation difficile.', 'Say something won’t change, even in a hard situation.'), 10, [
        ('-더라도 = même si (hypothèse) : 힘들더라도 포기하지 마세요. Plus fort que -아/어도.', '-더라도 = even if (hypothesis): 힘들더라도 포기하지 마세요. Stronger than -아/어도.'),
        ('On l’emploie souvent avec 아무리 (si … que) : 아무리 바쁘더라도 아침은 꼭 먹어요.', 'It often goes with 아무리 (however…): 아무리 바쁘더라도 아침은 꼭 먹어요.'),
      ], [
        G('gram-ko-deorado', '-더라도', None, '-deorado', ('même si', 'even if')),
        V('ko-pogihada', '포기하다', None, 'pogihada', ('renoncer, abandonner', 'to give up')),
        V('ko-himdeulda', '힘들다', None, 'himdeulda', ('être pénible, dur', 'to be hard, to be tiring')),
        V('ko-bandeusi', '반드시', None, 'bandeusi', ('à coup sûr, impérativement', 'necessarily, by all means')),
        V('ko-kkeutkkaji', '끝까지', None, 'kkeutkkaji', ('jusqu’au bout', 'to the end')),
        V('ko-silpaehada', '실패하다', None, 'silpaehada', ('échouer, rater', 'to fail (at something)')),
        V('ko-gyesok', '계속', None, 'gyesok', ('continuellement, sans arrêt', 'continuously')),
      ], [
        ex('힘들더라도 끝까지 포기하지 마세요.', None, 'Même si c’est dur, n’abandonne pas jusqu’au bout.', 'Even if it’s hard, don’t give up until the end.'),
        ex('실패하더라도 다시 도전하면 돼요.', None, 'Même si tu échoues, tu n’as qu’à réessayer.', 'Even if you fail, you can just try again.'),
      ], [
        FB(CHOOSE, '아무리 ＿ 아침은 꼭 드세요.', ['바쁘더라도', '바쁘던데', '바쁜 탓에'], '바쁘더라도', ('Même si : -더라도.', 'Even if: -더라도.'), ('Même très occupé, prends ton petit-déjeuner.', 'However busy you are, make sure you eat breakfast.')),
        FB(CHOOSE, '이번에 ＿ 실망하지 마세요.', ['실패하더라도', '실패했더라면', '실패하거든요'], '실패하더라도', ('Hypothèse + conseil : -더라도.', 'Hypothesis + advice: -더라도.'), ('Même si tu échoues cette fois, ne sois pas déçu.', 'Even if you fail this time, don’t be disappointed.')),
        SO(('Remets dans l’ordre : « Même si c’est dur, je continuerai. »', 'Put in order: “Even if it’s hard, I’ll keep going.”'), ['힘들더라도', '계속', '할', '거예요.'], ('-더라도 + décision.', '-더라도 + decision.')),
        TF('비가 오더라도 경기는 반드시 열립니다.', ('Le match sera annulé s’il pleut.', 'The match will be cancelled if it rains.'), FAUX, ('오더라도 … 열립니다 = même s’il pleut, il aura lieu.', '오더라도 … 열립니다 = even if it rains, it will go ahead.')),
      ]),
    L('ko-neundedo', ('Bien que : -는데도', 'Although: -는데도'), ('Opposer un fait réel et un résultat inattendu.', 'Contrast a real fact with an unexpected result.'), 9, [
        ('-(으)ㄴ/는데도 = bien que, malgré le fait que (fait réel) : 약을 먹었는데도 병이 안 나아요.', '-(으)ㄴ/는데도 = although, despite the fact that (real fact): 약을 먹었는데도 병이 안 나아요.'),
        ('Différence avec -더라도 : -더라도 imagine, -는데도 constate. 열심히 공부했는데도 떨어졌어요 (j’ai étudié, pourtant…).', 'Difference from -더라도: -더라도 imagines, -는데도 states. 열심히 공부했는데도 떨어졌어요 (I did study, yet…).'),
      ], [
        G('gram-ko-neundedo', '-(으)ㄴ/는데도', None, '-(eu)n / -neundedo', ('bien que, malgré le fait que', 'although, even though')),
        V('ko-amuri', '아무리', None, 'amuri', ('avoir beau, si… que', 'however (much)')),
        V('ko-hyogwa', '효과', None, 'hyogwa', ('effet', 'effect')),
        V('ko-yeojeonhi', '여전히', None, 'yeojeonhi', ('toujours, comme avant', 'still, as before')),
        V('ko-gochida', '고치다', None, 'gochida', ('réparer, corriger', 'to fix, to correct')),
        V('ko-natda', '낫다', None, 'natda', ('guérir ; être meilleur', 'to get better; to be better')),
        V('ko-byeong', '병', None, 'byeong', ('maladie ; bouteille', 'illness; bottle')),
      ], [
        ex('약을 먹었는데도 여전히 기침이 나요.', None, 'J’ai pris des médicaments, et pourtant je tousse toujours.', 'I took medicine, yet I’m still coughing.'),
        ex('아무리 고쳐도 효과가 없어요.', None, 'J’ai beau le réparer, ça ne change rien.', 'However much I fix it, it makes no difference.'),
      ], [
        FB(CHOOSE, '열심히 ＿ 시험에 떨어졌어요.', ['공부했는데도', '공부하더라도', '공부했더라면'], '공부했는데도', ('Fait réel + résultat inattendu : -는데도.', 'Real fact + unexpected result: -는데도.'), ('J’ai étudié sérieusement, et pourtant j’ai échoué à l’examen.', 'I studied hard, yet I failed the exam.')),
        FB(CHOOSE, '날씨가 ＿ 사람들이 많이 왔어요.', ['추운데도', '춥는데도', '추웠더라도'], '추운데도', ('Adjectif : -(으)ㄴ데도.', 'Adjective: -(으)ㄴ데도.'), ('Bien qu’il fasse froid, il est venu beaucoup de monde.', 'Even though it was cold, lots of people came.')),
        DC(('Ton ami a l’air toujours malade.', 'Your friend still looks ill.'), [('친구', '병원에 다녀왔는데도 여전히 아파요.')], ('Ton ami dit qu’il est allé à l’hôpital et qu’il a toujours mal.', 'Your friend says he went to hospital and still feels ill.'), ['그럼 오늘은 푹 쉬어야겠네요.', '병원에 갔다면서요?', '아프더라고요.'], '그럼 오늘은 푹 쉬어야겠네요.', ('On réagit au fait inattendu par un conseil.', 'You react to the unexpected fact with advice.')),
        TF('여러 번 고쳤는데도 컴퓨터가 여전히 고장이에요.', ('L’ordinateur ne marche toujours pas.', 'The computer still doesn’t work.'), VRAI, ('고쳤는데도 여전히 = malgré les réparations, toujours.', '고쳤는데도 여전히 = despite repairs, still.')),
      ]),
    L('ko-abwatja', ('Ça ne sert à rien de… : -아/어 봤자', 'There’s no point…: -아/어 봤자'), ('Dire qu’une action ne servira à rien.', 'Say an action will be pointless.'), 9, [
        ('-아/어 봤자 = avoir beau…, ça ne servira à rien : 지금 가 봤자 문이 닫혔을 거예요. Souvent suivi de 소용없다 (c’est inutile).', '-아/어 봤자 = no matter if…, it’s no use: 지금 가 봤자 문이 닫혔을 거예요. Often followed by 소용없다 (it’s no use).'),
        ('Le ton est souvent résigné : 이미 끝났는데 화내 봤자 소용없어요.', 'The tone is often resigned: 이미 끝났는데 화내 봤자 소용없어요.'),
      ], [
        G('gram-ko-abwatja', '-아/어 봤자', None, '-a / -eo bwatja', ('avoir beau…, ça ne sert à rien de', 'no matter if…, there’s no point')),
        V('ko-soyongeopda', '소용없다', None, 'soyongeopda', ('être inutile', 'to be no use')),
        V('ko-imi', '이미', None, 'imi', ('déjà (c’est trop tard)', 'already (too late)')),
        V('ko-hwanaeda', '화내다', None, 'hwanaeda', ('se fâcher', 'to get angry (at someone)')),
        V('ko-ttajida', '따지다', None, 'ttajida', ('contester, demander des comptes', 'to argue, to call to account')),
        V('ko-bakkuda', '바꾸다', None, 'bakkuda', ('échanger, remplacer', 'to exchange, to swap')),
        V('ko-gyeolgwa', '결과', None, 'gyeolgwa', ('résultat', 'result')),
      ], [
        ex('지금 가 봤자 이미 문을 닫았을 거예요.', None, 'Ça ne sert à rien d’y aller maintenant : ce sera déjà fermé.', 'There’s no point going now, it’ll already be closed.'),
        ex('결과가 나왔는데 따져 봤자 소용없어요.', None, 'Les résultats sont sortis : ça ne sert à rien de contester.', 'The results are out, so there’s no point arguing.'),
      ], [
        FB(CHOOSE, '이미 끝난 일인데 화내 ＿ 소용없어요.', ['봤자', '보더라도요', '보거든'], '봤자', ('Inutile de : -아/어 봤자.', 'No point: -아/어 봤자.'), ('C’est déjà fini : ça ne sert à rien de se fâcher.', 'It’s already over, there’s no use getting angry.')),
        FB(CHOOSE, '지금 ＿ 기차를 놓쳤을 거예요.', ['뛰어 봤자', '뛰었더라면', '뛰는데도요'], '뛰어 봤자', ('Action jugée inutile : -아/어 봤자.', 'Action judged pointless: -아/어 봤자.'), ('Même si je cours maintenant, j’aurai sûrement raté le train.', 'Even if I run now, I’ll have missed the train.')),
        DC(('Ton collègue veut aller se plaindre au chef.', 'Your colleague wants to complain to the boss.'), [('동료', '부장님께 가서 따져야겠어요.')], ('Ton collègue veut aller demander des comptes au chef.', 'Your colleague wants to go and confront the boss.'), ['따져 봤자 결과는 안 바뀔 거예요.', '따졌더라면 좋았을 거예요.', '따지러 갔나 봐요.'], '따져 봤자 결과는 안 바뀔 거예요.', ('On le dissuade : -아/어 봤자.', 'You talk him out of it: -아/어 봤자.')),
        TF('지금 바꿔 봤자 소용없어요.', ('La personne pense qu’un échange serait utile.', 'The speaker thinks exchanging it would help.'), FAUX, ('바꿔 봤자 소용없어요 = échanger ne servirait à rien.', '바꿔 봤자 소용없어요 = exchanging it would be no use.')),
      ]),
  ])])

# ═════════════════════════ Île 5 : la forêt des goblins ═════════════════════════
W5 = WORLD('topik4-w5', ('La forêt des Dueoksini', 'The forest of the Dueoksini'), REGION,
  ('Causes et conséquences : -는 바람에, -(으)ㄴ/는 탓에, -느라고.', 'Causes and consequences: -는 바람에, -(으)ㄴ/는 탓에, -느라고.'),
  (('Le Dueoksini furieux', 'The Furious Dueoksini'), '억', ('Ce gobelin aux cheveux hirsutes renverse tout sur son passage, puis accuse les voyageurs. Explique précisément ce qui a causé chaque incident, et il se calmera.', 'This shaggy-haired goblin knocks everything over and then blames travellers. Explain exactly what caused each mishap, and it will calm down.')),
  [CH('topik4-w5-c1', ('À cause de quoi ?', 'Because of what?'), [
    L('ko-neun-barame', ('À cause d’un imprévu : -는 바람에', 'Because of a mishap: -는 바람에'), ('Expliquer un résultat négatif causé par un événement inattendu.', 'Explain a bad result caused by something unexpected.'), 10, [
        ('-는 바람에 = à cause de (événement imprévu, résultat négatif) : 늦잠을 자는 바람에 지각했어요. La fin de phrase est toujours au passé.', '-는 바람에 = because of (unexpected event, negative result): 늦잠을 자는 바람에 지각했어요. The sentence always ends in the past.'),
        ('On garde -는 même pour un événement passé : 넘어지는 바람에 다쳤어요.', 'You keep -는 even for a past event: 넘어지는 바람에 다쳤어요.'),
      ], [
        G('gram-ko-neun-barame', '-는 바람에', None, '-neun barame', ('à cause de (imprévu, résultat négatif)', 'because of (unexpected, bad result)')),
        V('ko-jeongjeon', '정전', None, 'jeongjeon', ('panne de courant', 'power cut')),
        V('ko-gojang-nada', '고장 나다', None, 'gojang nada', ('tomber en panne', 'to break down')),
        V('ko-neutjam', '늦잠', None, 'neutjam', ('grasse matinée', 'oversleeping, a lie-in')),
        V('ko-jigakada', '지각하다', None, 'jigakada', ('arriver en retard (en cours, au travail)', 'to be late (for school or work)')),
        V('ko-neomeojida', '넘어지다', None, 'neomeojida', ('tomber (par terre)', 'to fall over')),
        V('ko-dachida-hurt', '다치다', None, 'dachida', ('se blesser', 'to get hurt')),
      ], [
        ex('늦잠을 자는 바람에 회사에 지각했어요.', None, 'J’ai fait la grasse matinée, du coup je suis arrivé en retard au travail.', 'I overslept, so I was late for work.'),
        ex('갑자기 정전이 되는 바람에 보고서가 다 지워졌어요.', None, 'À cause d’une coupure de courant soudaine, tout mon rapport s’est effacé.', 'A sudden power cut wiped out my whole report.'),
      ], [
        FB(CHOOSE, '길이 미끄러워서 ＿ 다리를 다쳤어요.', ['넘어지는 바람에', '넘어지느라고', '넘어지더라도'], '넘어지는 바람에', ('Imprévu → résultat négatif : -는 바람에.', 'Mishap → bad result: -는 바람에.'), ('La route était glissante : je suis tombé et je me suis blessé à la jambe.', 'The road was slippery, I fell and hurt my leg.')),
        FB(CHOOSE, '차가 ＿ 약속에 늦었어요.', ['고장 나는 바람에', '고장 났더라면', '고장 나거든'], '고장 나는 바람에', ('Panne imprévue : -는 바람에.', 'Unexpected breakdown: -는 바람에.'), ('Ma voiture est tombée en panne, alors je suis arrivé en retard au rendez-vous.', 'My car broke down, so I was late for the appointment.')),
        DC(('Ton chef te demande pourquoi tu es en retard.', 'Your boss asks why you are late.'), [('부장님', '오늘 왜 지각했어요?')], ('Ton chef te demande pourquoi tu es arrivé en retard.', 'Your boss asks why you were late today.'), ['지하철이 고장 나는 바람에 늦었습니다.', '지하철이 고장 나거든요요.', '지하철을 타 봤자예요.'], '지하철이 고장 나는 바람에 늦었습니다.', ('Excuse polie : -는 바람에 + passé.', 'Polite excuse: -는 바람에 + past.')),
        TF('정전이 되는 바람에 엘리베이터에 갇혔어요.', ('La personne est restée coincée à cause d’une coupure de courant.', 'The speaker got stuck because of a power cut.'), VRAI, ('정전이 되는 바람에 = à cause de la coupure.', '정전이 되는 바람에 = because of the power cut.')),
      ]),
    L('ko-tase', ('C’est la faute de… : -는 탓에', 'Owing to…: -는 탓에'), ('Désigner la cause d’un problème, avec une nuance de reproche.', 'Name the cause of a problem, with a hint of blame.'), 9, [
        ('-(으)ㄴ/는 탓에 = à cause de, par la faute de (résultat négatif) : 환경이 오염된 탓에 물고기가 줄었어요. Nom + 탓 : 날씨 탓이에요.', '-(으)ㄴ/는 탓에 = because of, owing to (bad result): 환경이 오염된 탓에 물고기가 줄었어요. Noun + 탓: 날씨 탓이에요.'),
        ('Fréquent dans les articles de presse et les explications de problèmes de société.', 'Common in newspaper articles and explanations of social problems.'),
      ], [
        G('gram-ko-tase', '-(으)ㄴ/는 탓에', None, '-(eu)n / -neun tase', ('à cause de, par la faute de', 'owing to, because of (blame)')),
        V('ko-hwangyeong', '환경', None, 'hwangyeong', ('environnement', 'environment')),
        V('ko-oyeom', '오염', None, 'oyeom', ('pollution', 'pollution')),
        V('ko-sseuregi', '쓰레기', None, 'sseuregi', ('déchets, ordures', 'rubbish, waste')),
        V('ko-julda', '줄다', None, 'julda', ('diminuer', 'to decrease')),
        V('ko-neulda', '늘다', None, 'neulda', ('augmenter, progresser', 'to increase, to improve')),
        V('ko-gion', '기온', None, 'gion', ('température (de l’air)', 'air temperature')),
      ], [
        ex('기온이 갑자기 오른 탓에 눈이 다 녹았어요.', None, 'À cause de la brusque hausse des températures, toute la neige a fondu.', 'Because temperatures suddenly rose, all the snow melted.'),
        ex('쓰레기가 늘어난 탓에 바다가 오염되고 있어요.', None, 'L’augmentation des déchets pollue la mer.', 'The sea is being polluted because of the growing amount of rubbish.'),
      ], [
        FB(CHOOSE, '물이 ＿ 물고기가 많이 줄었어요.', ['오염된 탓에', '오염되느라고', '오염되더라도'], '오염된 탓에', ('Cause d’un problème : -(으)ㄴ 탓에.', 'Cause of a problem: -(으)ㄴ 탓에.'), ('À cause de la pollution de l’eau, les poissons ont beaucoup diminué.', 'Because the water is polluted, the fish have greatly decreased.')),
        FB(CHOOSE, '운동을 안 한 ＿ 건강이 나빠졌어요.', ['탓에', '김에', '겸'], '탓에', ('Reproche : -(으)ㄴ 탓에.', 'Blame: -(으)ㄴ 탓에.'), ('Faute d’avoir fait du sport, ma santé s’est dégradée.', 'Because I didn’t exercise, my health got worse.')),
        SO(('Remets dans l’ordre : « Ce n’est pas la faute de la météo. »', 'Put in order: “It isn’t the weather’s fault.”'), ['날씨', '탓이', '아니에요.'], ('Nom + 탓이 아니다.', 'Noun + 탓이 아니다.')),
        TF('기온이 오른 탓에 눈이 다 녹았어요.', ('La neige a fondu parce que les températures ont baissé.', 'The snow melted because temperatures dropped.'), FAUX, ('오른 탓에 = parce que les températures ont monté.', '오른 탓에 = because temperatures rose.')),
      ]),
    L('ko-neurago', ('Trop occupé à : -느라고', 'Too busy…: -느라고'), ('Dire qu’une activité a empêché autre chose.', 'Say one activity prevented something else.'), 9, [
        ('-느라고 = occupé à… (et donc pas pu) : 보고서를 쓰느라고 밤을 새웠어요. Même sujet dans les deux parties, toujours un verbe d’action.', '-느라고 = busy doing… (so couldn’t): 보고서를 쓰느라고 밤을 새웠어요. Same subject in both clauses, always an action verb.'),
        ('Souvent pour s’excuser : 일하느라고 전화를 못 받았어요.', 'Often used to apologise: 일하느라고 전화를 못 받았어요.'),
      ], [
        G('gram-ko-neurago', '-느라고', None, '-neurago', ('occupé à… (donc pas pu)', 'busy doing… (so couldn’t)')),
        V('ko-bamsaeuda', '밤새우다', None, 'bamsaeuda', ('passer une nuit blanche', 'to stay up all night')),
        V('ko-jeongsineopda', '정신없다', None, 'jeongsineopda', ('être débordé, ne plus savoir où donner de la tête', 'to be frantic, to be swamped')),
        V('ko-magam', '마감', None, 'magam', ('date limite, clôture', 'deadline, closing')),
        V('ko-bogoseo', '보고서', None, 'bogoseo', ('rapport', 'report')),
        V('ko-kkeunnaeda', '끝내다', None, 'kkeunnaeda', ('terminer (quelque chose)', 'to finish (something)')),
        V('ko-jeongnihada', '정리하다', None, 'jeongnihada', ('ranger, mettre en ordre', 'to tidy, to organise')),
      ], [
        ex('보고서를 끝내느라고 밤을 새웠어요.', None, 'J’ai passé une nuit blanche à finir mon rapport.', 'I stayed up all night finishing my report.'),
        ex('이사 짐을 정리하느라고 정신없었어요.', None, 'J’étais débordé à ranger les cartons du déménagement.', 'I was swamped sorting out my moving boxes.'),
      ], [
        FB(CHOOSE, '회의를 ＿ 전화를 못 받았어요.', ['하느라고', '하는 바람에요', '한 탓에요'], '하느라고', ('Occupé à (même sujet) : -느라고.', 'Busy doing (same subject): -느라고.'), ('J’étais en réunion, je n’ai pas pu répondre au téléphone.', 'I was in a meeting so I couldn’t answer the phone.')),
        FB(CHOOSE, '마감 때문에 보고서를 ＿ 점심도 못 먹었어요.', ['쓰느라고', '썼느라고', '쓰더라도'], '쓰느라고', ('Jamais de passé devant -느라고.', 'Never a past form before -느라고.'), ('À cause de la date limite, j’étais à écrire mon rapport et je n’ai même pas déjeuné.', 'Because of the deadline I was writing the report and couldn’t even have lunch.')),
        DC(('Ton ami te reproche de ne pas avoir répondu.', 'Your friend complains you didn’t reply.'), [('친구', '어제 왜 연락이 없었어요?')], ('Ton ami demande pourquoi tu ne lui as pas donné de nouvelles hier.', 'Your friend asks why you didn’t get in touch yesterday.'), ['시험 준비하느라고 정신없었어요.', '시험 준비했더라면요.', '시험을 준비하거든.'], '시험 준비하느라고 정신없었어요.', ('Excuse : -느라고.', 'Excuse: -느라고.')),
        TF('짐을 정리하느라고 친구를 못 만났어요.', ('La personne a vu son ami.', 'The speaker met the friend.'), FAUX, ('못 만났어요 = n’a pas pu le voir.', '못 만났어요 = couldn’t meet.')),
      ]),
  ])])

# ═════════════════════════ Île 6 : le pays de la sécheresse ═════════════════════════
W6 = WORLD('topik4-w6', ('Les rizières assoiffées', 'The thirsty rice fields'), REGION,
  ('Ajouter des arguments : -(으)ㄹ 뿐만 아니라, -는 데다가, -기도 하다.', 'Adding arguments: -(으)ㄹ 뿐만 아니라, -는 데다가, -기도 하다.'),
  (('Le Gangcheori de la sécheresse', 'The Drought Gangcheori'), '강', ('Partout où passe cette bête de feu, les rizières se dessèchent. Seul un rapport complet, qui additionne tous les dégâts et toutes les solutions, peut la faire reculer.', 'Wherever this fiery beast goes, the rice fields dry out. Only a complete report, adding up all the damage and every solution, can drive it back.')),
  [CH('topik4-w6-c1', ('Non seulement… mais aussi', 'Not only… but also'), [
    L('ko-ppunmanaonira', ('Non seulement : -(으)ㄹ 뿐만 아니라', 'Not only: -(으)ㄹ 뿐만 아니라'), ('Ajouter une seconde idée, souvent plus forte.', 'Add a second, often stronger, point.'), 10, [
        ('-(으)ㄹ 뿐만 아니라 = non seulement… mais aussi : 가뭄은 농사에 피해를 줄 뿐만 아니라 물가도 오르게 해요. Nom + 뿐만 아니라 : 농부뿐만 아니라 도시 사람들도.', '-(으)ㄹ 뿐만 아니라 = not only… but also: 가뭄은 농사에 피해를 줄 뿐만 아니라 물가도 오르게 해요. Noun + 뿐만 아니라: 농부뿐만 아니라 도시 사람들도.'),
        ('La seconde partie prend souvent 도 (aussi).', 'The second part often takes 도 (also).'),
      ], [
        G('gram-ko-ppunmanaonira', '-(으)ㄹ 뿐만 아니라', None, '-(eu)l ppunman anira', ('non seulement… mais aussi', 'not only… but also')),
        V('ko-nongsa', '농사', None, 'nongsa', ('agriculture, culture', 'farming')),
        V('ko-gamum', '가뭄', None, 'gamum', ('sécheresse', 'drought')),
        V('ko-pihae', '피해', None, 'pihae', ('dégâts, dommages', 'damage, harm')),
        V('ko-hongsu', '홍수', None, 'hongsu', ('inondation', 'flood')),
        V('ko-mulga', '물가', None, 'mulga', ('niveau des prix', 'prices, cost of living')),
        V('ko-oreuda', '오르다', None, 'oreuda', ('monter, augmenter', 'to rise, to go up')),
      ], [
        ex('가뭄은 농사에 피해를 줄 뿐만 아니라 물가도 오르게 해요.', None, 'La sécheresse nuit non seulement aux cultures, mais fait aussi monter les prix.', 'Drought not only damages crops but also pushes up prices.'),
        ex('농부뿐만 아니라 도시 사람들도 어려움을 겪고 있어요.', None, 'Non seulement les paysans, mais aussi les citadins sont en difficulté.', 'Not only farmers but city people too are struggling.'),
      ], [
        FB(CHOOSE, '이 식당은 음식이 ＿ 값도 싸요.', ['맛있을 뿐만 아니라', '맛있는 탓에', '맛있더라도'], '맛있을 뿐만 아니라', ('Addition d’arguments : -(으)ㄹ 뿐만 아니라.', 'Adding points: -(으)ㄹ 뿐만 아니라.'), ('Ce restaurant est non seulement bon, mais aussi bon marché.', 'This restaurant is not only tasty but also cheap.')),
        PC(CHOOSE, '홍수는 농사＿ 사람들의 생활에도 피해를 줘요.', ['뿐만 아니라', '탓에', '김에'], '뿐만 아니라', ('Nom + 뿐만 아니라 … 도.', 'Noun + 뿐만 아니라 … 도.'), ('Les inondations nuisent non seulement aux cultures, mais aussi à la vie des gens.', 'Floods harm not only farming but people’s lives too.')),
        SO(('Remets dans l’ordre : « Non seulement les prix ont augmenté, mais les dégâts sont importants. »', 'Put in order: “Not only have prices risen, but the damage is great.”'), ['물가가', '올랐을', '뿐만', '아니라', '피해도', '커요.'], ('Passé -았/었을 뿐만 아니라 + … 도.', 'Past -았/었을 뿐만 아니라 + … 도.')),
        TF('가뭄 때문에 물가가 올랐을 뿐만 아니라 농사도 어려워졌어요.', ('La sécheresse a eu deux conséquences.', 'The drought had two consequences.'), VRAI, ('Hausse des prix + difficultés agricoles.', 'Higher prices + farming difficulties.')),
      ]),
    L('ko-neun-de-daga', ('En plus de : -는 데다가', 'On top of: -는 데다가'), ('Empiler des raisons dans le même sens.', 'Pile up reasons pointing the same way.'), 9, [
        ('-(으)ㄴ/는 데다가 = en plus de…, de surcroît : 이 집은 위치가 좋은 데다가 깨끗해요. Les deux idées vont dans le même sens (positif ou négatif).', '-(으)ㄴ/는 데다가 = on top of…, besides: 이 집은 위치가 좋은 데다가 깨끗해요. Both points go the same way (positive or negative).'),
        ('Entre deux phrases, on dit 게다가 : 비가 와요. 게다가 바람도 불어요.', 'Between two sentences, use 게다가: 비가 와요. 게다가 바람도 불어요.'),
      ], [
        G('gram-ko-neun-de-daga', '-(으)ㄴ/는 데다가', None, '-(eu)n / -neun dedaga', ('en plus de, de surcroît', 'on top of, besides')),
        V('ko-gedaga', '게다가', None, 'gedaga', ('de plus, en outre', 'moreover, what’s more')),
        V('ko-jeoryeomhada', '저렴하다', None, 'jeoryeomhada', ('être bon marché', 'to be inexpensive')),
        V('ko-pyeollihada', '편리하다', None, 'pyeollihada', ('être pratique', 'to be convenient')),
        V('ko-wichi', '위치', None, 'wichi', ('emplacement', 'location')),
        V('ko-kkaekkeutada', '깨끗하다', None, 'kkaekkeutada', ('être propre', 'to be clean')),
        V('ko-siseol', '시설', None, 'siseol', ('installations, équipements', 'facilities')),
      ], [
        ex('이 숙소는 위치가 좋은 데다가 가격도 저렴해요.', None, 'Ce logement est bien situé, et en plus il est bon marché.', 'This accommodation is well located and inexpensive too.'),
        ex('비가 오는 데다가 바람까지 불어서 너무 추워요.', None, 'Il pleut et en plus il y a du vent : il fait très froid.', 'It’s raining and windy on top of that, so it’s freezing.'),
      ], [
        FB(CHOOSE, '이 도서관은 시설이 ＿ 조용해서 공부하기 좋아요.', ['깨끗한 데다가', '깨끗하는 데다가', '깨끗한 탓에'], '깨끗한 데다가', ('Adjectif : -(으)ㄴ 데다가.', 'Adjective: -(으)ㄴ 데다가.'), ('Cette bibliothèque est propre et en plus calme : idéale pour étudier.', 'This library is clean and quiet too, great for studying.')),
        FB(CHOOSE, '오늘은 늦잠을 ＿ 길까지 막혀서 지각했어요.', ['잔 데다가', '자는 데다가요', '잤더라도'], '잔 데다가', ('Passé : -(으)ㄴ 데다가.', 'Past: -(으)ㄴ 데다가.'), ('Ce matin, j’ai trop dormi et en plus ça bouchonnait : je suis arrivé en retard.', 'This morning I overslept and the roads were jammed too, so I was late.')),
        DC(('Ton ami te demande pourquoi tu aimes ton quartier.', 'Your friend asks why you like your neighbourhood.'), [('친구', '그 동네가 왜 좋아요?')], ('Ton ami demande pourquoi tu apprécies ce quartier.', 'Your friend asks why you like that area.'), ['교통이 편리한 데다가 물가도 저렴해요.', '교통이 편리했더라면 좋았을 거예요.', '교통이 편리한 탓이에요.'], '교통이 편리한 데다가 물가도 저렴해요.', ('Deux arguments positifs : -(으)ㄴ 데다가.', 'Two positive points: -(으)ㄴ 데다가.')),
        TF('그 호텔은 비싼 데다가 시설도 낡았어요.', ('L’hôtel est bon marché et moderne.', 'The hotel is cheap and modern.'), FAUX, ('비싼 데다가 낡았어요 = cher et en plus vétuste.', '비싼 데다가 낡았어요 = expensive and run-down too.')),
      ]),
    L('ko-gido-hada', ('Il arrive aussi que : -기도 하다', 'Sometimes also: -기도 하다'), ('Nuancer en ajoutant une autre possibilité ou un autre aspect.', 'Add nuance with another possibility or aspect.'), 9, [
        ('-기도 하다 = il arrive aussi que, c’est aussi… : 가끔 혼자 여행하기도 해요. Avec deux verbes : -기도 하고 -기도 하다 (tantôt… tantôt…).', '-기도 하다 = sometimes also, it’s also…: 가끔 혼자 여행하기도 해요. With two verbs: -기도 하고 -기도 하다 (sometimes… sometimes…).'),
        ('Utile pour présenter des opinions partagées : 찬성하는 사람도 있고 반대하기도 해요.', 'Useful for presenting divided opinions: 찬성하는 사람도 있고 반대하기도 해요.'),
      ], [
        G('gram-ko-gido-hada', '-기도 하다', None, '-gido hada', ('il arrive aussi que ; être aussi', 'sometimes also; to be also')),
        V('ko-gakkeum', '가끔', None, 'gakkeum', ('parfois, de temps en temps', 'sometimes, occasionally')),
        V('ko-daebubun', '대부분', None, 'daebubun', ('la plupart', 'most, the majority')),
        V('ko-gyeongu', '경우', None, 'gyeongu', ('cas, situation', 'case, circumstance')),
        V('ko-bandae', '반대', None, 'bandae', ('opposition ; contraire', 'opposition; the opposite')),
        V('ko-chanseong', '찬성', None, 'chanseong', ('approbation, être pour', 'approval, being in favour')),
        V('ko-uigyeon', '의견', None, 'uigyeon', ('avis, opinion', 'opinion, view')),
      ], [
        ex('대부분 집에서 일하지만 가끔 카페에서 일하기도 해요.', None, 'Je travaille la plupart du temps chez moi, mais il m’arrive aussi de travailler au café.', 'I mostly work at home, but sometimes I work in a café too.'),
        ex('이 정책에 대해 찬성하는 사람도 있고 반대하는 사람도 있어요.', None, 'Certains sont pour cette politique, d’autres contre.', 'Some people support this policy and some oppose it.'),
      ], [
        FB(CHOOSE, '주말에는 보통 쉬지만 가끔 일을 ＿.', ['하기도 해요', '하느라고요', '할 뿐이에요'], '하기도 해요', ('Il arrive aussi que : -기도 하다.', 'Sometimes also: -기도 하다.'), ('Le week-end, je me repose en général, mais il m’arrive aussi de travailler.', 'At weekends I usually rest, but sometimes I work too.')),
        FB(CHOOSE, '그 소식을 듣고 기쁘기도 ＿ 슬프기도 했어요.', ['하고', '해서', '하면'], '하고', ('Tantôt… tantôt : -기도 하고 -기도 하다.', 'Both… and: -기도 하고 -기도 하다.'), ('En apprenant la nouvelle, j’étais à la fois heureux et triste.', 'Hearing the news, I felt both happy and sad.')),
        DC(('Un journaliste te demande ton avis sur un projet de loi.', 'A journalist asks your opinion on a bill.'), [('기자', '이 정책에 대해 어떻게 생각하세요?')], ('Le journaliste te demande ce que tu penses de cette politique.', 'The journalist asks what you think of this policy.'), ['좋은 점도 있지만 걱정되기도 해요.', '좋은 점이 있다면서요?', '걱정하느라고요.'], '좋은 점도 있지만 걱정되기도 해요.', ('Avis nuancé : -기도 하다.', 'Nuanced opinion: -기도 하다.')),
        TF('대부분의 경우 찬성하지만 반대하기도 해요.', ('La personne est toujours pour, sans exception.', 'The speaker always agrees, without exception.'), FAUX, ('반대하기도 해요 = il lui arrive aussi d’être contre.', '반대하기도 해요 = sometimes they disagree too.')),
      ]),
  ])])

# ═════════════════════════ Île 7 : l'éclipse ═════════════════════════
W7 = WORLD('topik4-w7', ('La nuit de l’éclipse', 'The night of the eclipse'), REGION,
  ('Intentions et occasions : -(으)ㄹ까 하다, -는 김에, -(으)ㄹ 겸.', 'Intentions and opportunities: -(으)ㄹ까 하다, -는 김에, -(으)ㄹ 겸.'),
  (('Les Chiens de feu', 'The Fire Dogs'), '개', ('Envoyés par un roi des ténèbres, ces chiens de feu mordent le soleil et la lune : c’est l’éclipse. Raconte-leur tes projets et profite de chaque occasion, ils lâcheront prise.', 'Sent by a king of darkness, these fire dogs bite the sun and moon: that is an eclipse. Tell them your plans and seize every opportunity, and they will let go.')),
  [CH('topik4-w7-c1', ('Projets et occasions', 'Plans and opportunities'), [
    L('ko-eulkka-hada', ('Je pense peut-être… : -(으)ㄹ까 하다', 'I’m thinking of…: -(으)ㄹ까 하다'), ('Évoquer un projet encore incertain.', 'Mention a plan you haven’t settled on.'), 9, [
        ('-(으)ㄹ까 하다 = je pense peut-être…, j’envisage de : 이번 휴가에 제주도에 갈까 해요. Moins sûr que -(으)려고 하다.', '-(으)ㄹ까 하다 = I’m thinking of…, I might: 이번 휴가에 제주도에 갈까 해요. Less certain than -(으)려고 하다.'),
        ('Au passé : -(으)ㄹ까 했어요 = j’avais pensé à… (mais) : 회사를 그만둘까 했는데 참았어요.', 'In the past: -(으)ㄹ까 했어요 = I was thinking of… (but): 회사를 그만둘까 했는데 참았어요.'),
      ], [
        G('gram-ko-eulkka-hada', '-(으)ㄹ까 하다', None, '-(eu)lkka hada', ('je pense peut-être…, envisager de', 'to be thinking of (doing)')),
        V('ko-hyuga', '휴가', None, 'hyuga', ('congés, vacances (de travail)', 'holiday, leave')),
        V('ko-dongari', '동아리', None, 'dongari', ('club (étudiant)', 'club (student society)')),
        V('ko-gaipada', '가입하다', None, 'gaipada', ('adhérer, s’inscrire', 'to join, to sign up')),
        V('ko-geumanduda', '그만두다', None, 'geumanduda', ('arrêter, quitter', 'to quit, to stop')),
        V('ko-yuhak', '유학', None, 'yuhak', ("études à l'étranger", 'studying abroad')),
        V('ko-ilsik', '일식', None, 'ilsik', ('éclipse de soleil', 'solar eclipse')),
      ], [
        ex('이번 휴가에는 제주도에 갈까 해요.', None, 'Pour ces congés, je pense peut-être aller à Jeju.', 'I’m thinking of going to Jeju for this holiday.'),
        ex('사진 동아리에 가입할까 하는데 같이 할래요?', None, 'J’envisage de m’inscrire au club photo : tu viens avec moi ?', 'I’m thinking of joining the photo club, want to join too?'),
      ], [
        FB(CHOOSE, '내년에 한국으로 유학을 ＿ 해요.', ['갈까', '가려고는', '간다면'], '갈까', ('Projet incertain : -(으)ㄹ까 하다.', 'Uncertain plan: -(으)ㄹ까 하다.'), ('Je pense peut-être partir étudier en Corée l’année prochaine.', 'I’m thinking of going to study in Korea next year.')),
        FB(CHOOSE, '회사를 그만둘까 ＿ 조금 더 다니기로 했어요.', ['했는데', '하는 김에', '할 겸'], '했는데', ('Au passé : -(으)ㄹ까 했는데 (mais…).', 'In the past: -(으)ㄹ까 했는데 (but…).'), ('J’avais pensé quitter l’entreprise, mais j’ai décidé de rester encore un peu.', 'I was thinking of quitting, but I decided to stay a bit longer.')),
        DC(('Ton ami te demande ce que tu fais ce soir.', 'Your friend asks what you’re doing tonight.'), [('친구', '오늘 밤에 뭐 해요?')], ('Ton ami te demande ce que tu fais ce soir.', 'Your friend asks what you’re doing tonight.'), ['일식을 보러 갈까 해요.', '일식을 봤더라면요.', '일식을 보느라고요.'], '일식을 보러 갈까 해요.', ('Projet pas encore décidé : -(으)ㄹ까 해요.', 'Undecided plan: -(으)ㄹ까 해요.')),
        TF('운동 동아리에 가입할까 해요.', ('La personne s’est déjà inscrite au club.', 'The speaker has already joined the club.'), FAUX, ('가입할까 해요 = j’envisage de m’inscrire.', '가입할까 해요 = I’m thinking of joining.')),
      ]),
    L('ko-neun-gime', ('Tant qu’on y est : -는 김에', 'While I’m at it: -는 김에'), ('Profiter d’une action pour en faire une autre.', 'Take advantage of one action to do another.'), 9, [
        ('-는 김에 = tant qu’on y est, puisqu’on est en train de : 시장에 가는 김에 우체국에 들를게요. Passé : -(으)ㄴ 김에 (온 김에 쉬었다 가세요).', '-는 김에 = while I’m at it, since I’m already…: 시장에 가는 김에 우체국에 들를게요. Past: -(으)ㄴ 김에 (온 김에 쉬었다 가세요).'),
        ('Expression proche : 겸사겸사 (pour faire d’une pierre deux coups).', 'A related expression: 겸사겸사 (to kill two birds with one stone).'),
      ], [
        G('gram-ko-neun-gime', '-는 김에', None, '-neun gime', ('tant qu’on y est, en profitant de', 'while one is at it')),
        V('ko-deulleuda', '들르다', None, 'deulleuda', ('passer (chez, par)', 'to drop by, to stop off')),
        V('ko-nagada', '나가다', None, 'nagada', ('sortir', 'to go out')),
        V('ko-jang-boda', '장 보다', None, 'jang boda', ('faire les courses', 'to do the grocery shopping')),
        V('ko-ucheguk', '우체국', None, 'ucheguk', ('bureau de poste', 'post office')),
        V('ko-buchida', '부치다', None, 'buchida', ('envoyer (un colis, une lettre)', 'to send (a parcel, a letter)')),
        V('ko-gyeomsagyeomsa', '겸사겸사', None, 'gyeomsagyeomsa', ('pour faire d’une pierre deux coups', 'for two reasons at once')),
      ], [
        ex('장 보러 나가는 김에 우체국에 들러서 소포를 부칠게요.', None, 'Puisque je sors faire les courses, je passerai à la poste envoyer le colis.', 'Since I’m going out shopping, I’ll stop at the post office to send the parcel.'),
        ex('서울에 온 김에 친구도 만났어요.', None, 'Tant que j’étais à Séoul, j’en ai profité pour voir un ami.', 'While I was in Seoul, I met up with a friend too.'),
      ], [
        FB(CHOOSE, '청소하＿ 창문도 닦았어요.', ['는 김에', '느라고', '는 탓에'], '는 김에', ('En profitant d’une action : -는 김에.', 'Taking advantage of an action: -는 김에.'), ('Tant que je faisais le ménage, j’ai aussi lavé les vitres.', 'While I was cleaning, I wiped the windows too.')),
        FB(CHOOSE, '여기까지 ＿ 점심이라도 먹고 가세요.', ['온 김에', '오는 바람에', '올까 하고'], '온 김에', ('Action déjà faite : -(으)ㄴ 김에.', 'Action already done: -(으)ㄴ 김에.'), ('Puisque vous êtes venu jusqu’ici, déjeunez au moins avant de repartir.', 'Since you’ve come all this way, at least have lunch before you go.')),
        DC(('Ta colocataire sort à la supérette.', 'Your flatmate is going out to the corner shop.'), [('룸메이트', '편의점에 잠깐 갔다 올게요.')], ('Ta colocataire dit qu’elle fait un saut à la supérette.', 'Your flatmate says she’s popping to the corner shop.'), ['가는 김에 우유 좀 사다 줄래요?', '가는 탓에 우유가 없어요.', '갔더라면 좋았을 텐데요.'], '가는 김에 우유 좀 사다 줄래요?', ('Demande en profitant de sa sortie : -는 김에.', 'Request taking advantage of her trip: -는 김에.')),
        TF('부산에 출장 간 김에 바다도 구경했어요.', ('La personne a profité de son déplacement pour voir la mer.', 'The speaker took the chance to see the sea during a business trip.'), VRAI, ('간 김에 = en profitant du voyage.', '간 김에 = while there.')),
      ]),
    L('ko-eul-gyeom', ('À la fois pour… : -(으)ㄹ 겸', 'Both to… and to: -(으)ㄹ 겸'), ('Donner deux buts à une même action.', 'Give two purposes for one action.'), 9, [
        ('-(으)ㄹ 겸 = à la fois pour… : 운동도 할 겸 산책도 할 겸 공원에 가요. Nom + 겸 : 아침 겸 점심 (brunch).', '-(으)ㄹ 겸 = both to… (and to): 운동도 할 겸 산책도 할 겸 공원에 가요. Noun + 겸: 아침 겸 점심 (brunch).'),
        ('On peut ne citer qu’un des buts : 기분 전환도 할 겸 머리를 잘랐어요 (entre autres pour changer d’air).', 'You can mention just one purpose: 기분 전환도 할 겸 머리를 잘랐어요 (partly for a change of mood).'),
      ], [
        G('gram-ko-eul-gyeom', '-(으)ㄹ 겸', None, '-(eu)l gyeom', ('à la fois pour… (deux buts)', 'both to… (two purposes)')),
        V('ko-sanchaek', '산책', None, 'sanchaek', ('promenade', 'walk, stroll')),
        V('ko-gibun-jeonhwan', '기분 전환', None, 'gibun jeonhwan', ('changement d’air, se changer les idées', 'change of mood')),
        V('ko-guhada', '구하다', None, 'guhada', ('chercher, trouver ; sauver', 'to look for, to find; to save')),
        V('ko-areubaiteu', '아르바이트', None, 'areubaiteu', ('petit boulot', 'part-time job')),
        V('ko-ssata', '쌓다', None, 'ssata', ('accumuler, empiler', 'to build up, to pile')),
        V('ko-beolda', '벌다', None, 'beolda', ('gagner (de l’argent)', 'to earn (money)')),
      ], [
        ex('경험도 쌓을 겸 용돈도 벌 겸 아르바이트를 해요.', None, 'Je fais un petit boulot, à la fois pour l’expérience et pour gagner de l’argent de poche.', 'I have a part-time job, both to gain experience and to earn pocket money.'),
        ex('기분 전환도 할 겸 산책하러 나갔어요.', None, 'Je suis sorti me promener, entre autres pour me changer les idées.', 'I went out for a walk, partly to clear my head.'),
      ], [
        FB(CHOOSE, '운동도 ＿ 회사까지 걸어서 가요.', ['할 겸', '하는 김에요', '하느라고'], '할 겸', ('But secondaire : -(으)ㄹ 겸.', 'Additional purpose: -(으)ㄹ 겸.'), ('Je vais au bureau à pied, entre autres pour faire du sport.', 'I walk to work, partly to get some exercise.')),
        PC(CHOOSE, '아침＿ 점심으로 빵을 먹었어요.', ['겸', '김에', '탓에'], '겸', ('Nom + 겸 + nom : les deux à la fois.', 'Noun + 겸 + noun: both at once.'), ('J’ai mangé du pain en guise de petit-déjeuner et déjeuner.', 'I had bread as a combined breakfast and lunch.')),
        DC(('Ton ami s’étonne que tu prennes des cours du soir.', 'Your friend is surprised you take evening classes.'), [('친구', '요즘 왜 학원에 다녀요?')], ('Ton ami demande pourquoi tu suis des cours en ce moment.', 'Your friend asks why you’re going to classes these days.'), ['일자리도 구할 겸 공부를 다시 시작했어요.', '일자리를 구하는 탓이에요.', '일자리를 구할까 했더라면요.'], '일자리도 구할 겸 공부를 다시 시작했어요.', ('Donner un des buts : -(으)ㄹ 겸.', 'Giving one of the purposes: -(으)ㄹ 겸.')),
        TF('돈도 벌 겸 경험도 쌓을 겸 일해요.', ('La personne travaille pour deux raisons.', 'The speaker works for two reasons.'), VRAI, ('-(으)ㄹ 겸 … -(으)ㄹ 겸 = deux buts.', '-(으)ㄹ 겸 … -(으)ㄹ 겸 = two purposes.')),
      ]),
  ])])

# ═════════════════════════ Île 8 : le gardien du Nord ═════════════════════════
W8 = WORLD('topik4-w8', ('Les archives du Nord', 'The northern archives'), REGION,
  ('L’action achevée : -아/어 버리다, -고 말다, -아/어 놓다/두다.', 'Completed action: -아/어 버리다, -고 말다, -아/어 놓다/두다.'),
  (('Hyeonmu, la Tortue noire', 'Hyeonmu, the Black Tortoise'), '현', ('Gardienne du Nord et de l’hiver, la Tortue noire protège les copies des Annales cachées dans la montagne. Elle ne laisse consulter les archives qu’à qui sait dire ce qui est fini, perdu ou mis de côté.', 'Guardian of the North and of winter, the Black Tortoise protects the copies of the Annals hidden in the mountains. It lets only those who can say what is finished, lost or set aside consult the archives.')),
  [CH('topik4-w8-c1', ('Fini, perdu, mis de côté', 'Finished, lost, set aside'), [
    L('ko-a-beorida', ('Complètement : -아/어 버리다', 'Completely: -아/어 버리다'), ('Insister sur une action totalement achevée, avec regret ou soulagement.', 'Stress a completely finished action, with regret or relief.'), 9, [
        ('-아/어 버리다 = complètement, une fois pour toutes : 숙제를 다 해 버렸어요 (soulagement), 지갑을 잃어버렸어요 (regret).', '-아/어 버리다 = completely, once and for all: 숙제를 다 해 버렸어요 (relief), 지갑을 잃어버렸어요 (regret).'),
        ('Certains verbes l’ont intégré : 잃어버리다 (perdre), 잊어버리다 (oublier).', 'Some verbs have it built in: 잃어버리다 (to lose), 잊어버리다 (to forget).'),
      ], [
        G('gram-ko-a-beorida', '-아/어 버리다', None, '-a / -eo beorida', ('complètement, une fois pour toutes', 'completely, once and for all')),
        V('ko-ireobeorida', '잃어버리다', None, 'ireobeorida', ('perdre (un objet)', 'to lose (something)')),
        V('ko-kkaejida', '깨지다', None, 'kkaejida', ('se casser, se briser', 'to break, to shatter')),
        V('ko-jiuda', '지우다', None, 'jiuda', ('effacer', 'to erase')),
        V('ko-da', '다', None, 'da', ('tout, entièrement', 'everything, completely')),
        V('ko-soksanghada', '속상하다', None, 'soksanghada', ('être contrarié, peiné', 'to be upset')),
      ], [
        ex('실수로 파일을 다 지워 버렸어요. 너무 속상해요.', None, 'J’ai effacé tous les fichiers par erreur. Je suis tellement contrarié.', 'I accidentally deleted all the files. I’m so upset.'),
        ex('할 일을 다 해 버리니까 마음이 편해요.', None, 'Maintenant que j’ai tout fini, je me sens léger.', 'Now that I’ve got everything done, I feel at ease.'),
      ], [
        FB(CHOOSE, '동생이 제 케이크를 다 ＿.', ['먹어 버렸어요', '먹어 놓았어요', '먹고 말까요'], '먹어 버렸어요', ('Action totale, avec regret : -아/어 버리다.', 'Complete action, with regret: -아/어 버리다.'), ('Mon petit frère a mangé tout mon gâteau.', 'My little brother ate all my cake.')),
        FB(CHOOSE, '컵을 떨어뜨려서 ＿.', ['깨져 버렸어요', '깨지기도 해요', '깨질 겸요'], '깨져 버렸어요', ('Résultat complet et regrettable.', 'Complete, regrettable result.'), ('J’ai fait tomber la tasse : elle s’est cassée.', 'I dropped the cup and it broke.')),
        SO(('Remets dans l’ordre : « J’ai perdu mon portefeuille dans le métro. »', 'Put in order: “I lost my wallet on the subway.”'), ['지하철에서', '지갑을', '잃어버렸어요.'], ('Lieu + objet + 잃어버리다.', 'Place + object + 잃어버리다.')),
        TF('숙제를 다 해 버려서 마음이 편해요.', ('La personne n’a pas encore fini ses devoirs.', 'The speaker hasn’t finished the homework yet.'), FAUX, ('다 해 버려서 = tout fini.', '다 해 버려서 = all done.')),
      ]),
    L('ko-go-malda', ('Finir par : -고 말다', 'End up: -고 말다'), ('Dire qu’une chose a fini par arriver, ou qu’on la fera coûte que coûte.', 'Say something ended up happening, or that you’ll do it no matter what.'), 9, [
        ('-고 말았다 = finir par (malgré soi) : 참으려고 했는데 울음을 터뜨리고 말았어요.', '-고 말았다 = to end up (despite oneself): 참으려고 했는데 울음을 터뜨리고 말았어요.'),
        ('-고 말겠다 = coûte que coûte, j’y arriverai : 이번에는 꼭 이기고 말겠어요.', '-고 말겠다 = no matter what, I’ll do it: 이번에는 꼭 이기고 말겠어요.'),
      ], [
        G('gram-ko-go-malda', '-고 말다', None, '-go malda', ('finir par ; coûte que coûte', 'to end up; no matter what')),
        V('ko-ureum', '울음', None, 'ureum', ('pleurs', 'crying, tears')),
        V('ko-teotteurida', '터뜨리다', None, 'teotteurida', ('faire éclater ; éclater (en)', 'to burst; to burst out')),
        V('ko-igida', '이기다', None, 'igida', ('gagner, vaincre', 'to win, to beat')),
        V('ko-jida', '지다', None, 'jida', ('perdre (un match)', 'to lose (a match)')),
        V('ko-haenaeda', '해내다', None, 'haenaeda', ('réussir à faire, venir à bout de', 'to pull off, to manage')),
      ], [
        ex('끝까지 참으려고 했는데 결국 울음을 터뜨리고 말았어요.', None, 'J’ai essayé de tenir jusqu’au bout, mais j’ai fini par éclater en sanglots.', 'I tried to hold it in, but I ended up bursting into tears.'),
        ex('다음 경기에서는 반드시 이기고 말겠어요.', None, 'Au prochain match, je gagnerai coûte que coûte.', 'I will win the next match no matter what.'),
      ], [
        FB(CHOOSE, '열심히 뛰었지만 결국 경기에서 ＿.', ['지고 말았어요', '져 놓았어요', '질 겸이에요'], '지고 말았어요', ('Résultat subi : -고 말았다.', 'Outcome despite efforts: -고 말았다.'), ('J’ai couru de toutes mes forces, mais j’ai fini par perdre le match.', 'I ran hard, but I ended up losing the match.')),
        FB(CHOOSE, '이번에는 꼭 ＿.', ['해내고 말겠어요', '해내고 말았어요', '해내 버렸겠어요'], '해내고 말겠어요', ('Détermination : -고 말겠다.', 'Determination: -고 말겠다.'), ('Cette fois, j’y arriverai coûte que coûte.', 'This time I’ll pull it off no matter what.')),
        DC(('Ton amie revient d’un entretien raté.', 'Your friend is back from a failed interview.'), [('친구', '긴장해서 대답을 하나도 못 했어요.')], ('Ton amie dit qu’elle était si stressée qu’elle n’a rien su répondre.', 'Your friend says she was so nervous she couldn’t answer anything.'), ['다음에는 꼭 해내고 말 거예요.', '해내고 말았어요?', '해내 놓았나 봐요.'], '다음에는 꼭 해내고 말 거예요.', ('Encouragement : -고 말 거예요.', 'Encouragement: -고 말 거예요.')),
        TF('결국 그 비밀을 말하고 말았어요.', ('La personne a fini par révéler le secret.', 'The speaker ended up revealing the secret.'), VRAI, ('말하고 말았어요 = a fini par le dire.', '말하고 말았어요 = ended up telling.')),
      ]),
    L('ko-a-nota', ('À l’avance : -아/어 놓다, -아/어 두다', 'In advance: -아/어 놓다, -아/어 두다'), ('Dire qu’on a fait une chose à l’avance et que le résultat demeure.', 'Say you did something ahead of time and the result remains.'), 9, [
        ('-아/어 놓다 / -아/어 두다 = faire à l’avance et laisser ainsi : 창문을 열어 놓았어요 (j’ai laissé la fenêtre ouverte), 음식을 냉장고에 넣어 두세요.', '-아/어 놓다 / -아/어 두다 = to do in advance and leave it so: 창문을 열어 놓았어요 (I left the window open), 음식을 냉장고에 넣어 두세요.'),
        ('-아/어 두다 insiste sur la conservation à long terme : 중요한 일은 기록해 두세요. Les Annales de Joseon ont été copiées et gardées ainsi pour les descendants.', '-아/어 두다 stresses long-term keeping: 중요한 일은 기록해 두세요. The Annals of Joseon were copied and kept this way for future generations.'),
      ], [
        G('gram-ko-a-nota', '-아/어 놓다 / 두다', None, '-a / -eo nota / duda', ('faire à l’avance et laisser ainsi', 'to do in advance and leave it so')),
        V('ko-naengjanggo', '냉장고', None, 'naengjanggo', ('réfrigérateur', 'fridge')),
        V('ko-changmun', '창문', None, 'changmun', ('fenêtre', 'window')),
        V('ko-girokada', '기록하다', None, 'girokada', ('consigner, enregistrer', 'to record, to write down')),
        V('ko-bogwanhada', '보관하다', None, 'bogwanhada', ('conserver, garder', 'to store, to keep')),
        V('ko-sillok', '실록', None, 'sillok', ('annales royales', 'royal annals')),
        V('ko-huson', '후손', None, 'huson', ('descendants', 'descendants')),
      ], [
        ex('사관들은 왕의 말과 행동을 모두 기록해 두었어요.', None, 'Les historiens royaux consignaient toutes les paroles et tous les actes du roi.', 'The royal historians recorded everything the king said and did.'),
        ex('손님이 오기 전에 음식을 미리 만들어 놓았어요.', None, 'J’ai préparé les plats à l’avance, avant l’arrivée des invités.', 'I made the food in advance, before the guests arrived.'),
      ], [
        FB(CHOOSE, '더워서 창문을 ＿ 잤어요.', ['열어 놓고', '열어 버리고요', '열고 말고'], '열어 놓고', ('Laisser dans un état : -아/어 놓다.', 'Leave in a state: -아/어 놓다.'), ('Il faisait chaud : j’ai dormi la fenêtre ouverte.', 'It was hot, so I slept with the window open.')),
        FB(CHOOSE, '남은 음식은 냉장고에 ＿.', ['넣어 두세요', '넣고 마세요', '넣어 봤자예요'], '넣어 두세요', ('Conserver : -아/어 두다.', 'Keep: -아/어 두다.'), ('Mets les restes au réfrigérateur.', 'Put the leftovers in the fridge.')),
        DC(('Ton collègue part en voyage d’affaires demain.', 'Your colleague leaves on a business trip tomorrow.'), [('동료', '내일 출장 준비는 다 했어요?')], ('Ton collègue demande si tu es prêt pour le déplacement de demain.', 'Your colleague asks if you’re ready for tomorrow’s trip.'), ['네, 표도 미리 예약해 놓았어요.', '네, 표를 예약해 버렸어요?', '표를 예약할 겸이에요.'], '네, 표도 미리 예약해 놓았어요.', ('Préparatif fait à l’avance : -아/어 놓다.', 'Preparation done ahead: -아/어 놓다.')),
        TF('실록은 후손을 위해 여러 곳에 보관해 두었어요.', ('Les annales étaient conservées en plusieurs endroits.', 'The annals were kept in several places.'), VRAI, ('여러 곳에 보관해 두었어요 = conservées en plusieurs lieux.', '여러 곳에 보관해 두었어요 = stored in several places.')),
      ]),
  ])])

FINAL = {
  'slug': 'topik4-final',
  'title': t(('Simulation TOPIK II — niveau 4', 'TOPIK II simulation — level 4')),
  'region': REGION,
  'description': t(('Examen blanc au format du TOPIK II (version abrégée), avec des questions plus difficiles : écoute, écriture et lecture, noté sur 300. Il faut 150 points pour obtenir le niveau 4 et valider l’île.', 'Mock exam in TOPIK II format (shortened), with harder questions: listening, writing and reading, marked out of 300. You need 150 points to reach level 4 and clear the island.')),
  'exam': 'topik4-official',
  'chapters': [],
}

level = {
  'contentVersion': '2026.11.21',
  'level': {'code': 'TOPIK4', 'title': t(('Intermédiaire avancé : actualités et société en coréen', 'Upper intermediate: news and society in Korean')), 'region': REGION, 'order': 13},
  'notice': t(('Les listes de vocabulaire de Koto Quest sont alignées sur les compétences attendues au TOPIK II (niveau 4) mais ne constituent pas des listes officielles du TOPIK.', 'Koto Quest’s vocabulary lists are aligned with the skills expected at TOPIK II (level 4) but are not official TOPIK lists.')),
  'worlds': [W1, W2, W3, W4, W5, W6, W7, W8, FINAL],
}
t((REGION, 'Annals of Joseon'))
os.makedirs(os.path.join(ROOT, 'content/topik4'), exist_ok=True)
check_and_write(level, 'content/topik4/topik4.json', ['content/n5/n5.json', 'content/n4/n4.json', 'content/n3/n3.json', 'content/n2/n2.json', 'content/n1/n1.json', 'content/topik1/topik1.json', 'content/topik2/topik2.json', 'content/topik3/topik3.json'])
