# Niveau TOPIK 6 (coréen, TOPIK II niveau 6, le plus haut) : 8 îles, 24 leçons et un examen blanc au format du TOPIK II.
# Saga : la légende de Dangun et les mythes fondateurs (Hwanung, l'ourse Ungnyeo, Jumong, Bak Hyeokgeose,
# la cloche d'Emille, la flûte Manpasikjeok, Cheoyong) ; dernière île : proverbes et expressions en quatre caractères.
# Usage : python3 scripts/topik6-level.py   (réécrit content/topik6/topik6.json)
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from kq_content import *

REGION = 'Royaume de Gojoseon'

# ═════════════════════════ Île 1 : la cité divine ═════════════════════════
W1 = WORLD('topik6-w1', ('La cité divine du mont Taebaek', 'The divine city of Mount Taebaek'), REGION,
  ('La langue des discours et des textes officiels : -고자 하다, -(으)며, -는 바이다.', 'The language of speeches and official texts: -고자 하다, -(으)며, -는 바이다.'),
  (('Hwanung, fils du Ciel', 'Hwanung, Son of Heaven'), '환', ('Descendu du ciel avec les maîtres du vent, de la pluie et des nuages, Hwanung fonda la cité divine pour « bénéficier largement à l’humanité ». Il ne reçoit que ceux qui s’expriment avec la dignité d’un discours.', 'Descending from heaven with the masters of wind, rain and clouds, Hwanung founded the divine city to “benefit all humankind”. He receives only those who speak with the dignity of an address.')),
  [CH('topik6-w1-c1', ('Parler en public', 'Speaking in public'), [
    L('ko-gojahada', ('Dans le but de (formel) : -고자 하다', 'Intending to (formal): -고자 하다'), ('Annoncer une intention dans un discours ou un écrit officiel.', 'Announce an intention in a speech or official text.'), 10, [
        ('-고자 하다 = avoir l’intention de, vouloir (style soutenu) : 오늘은 환경 문제에 대해 말씀드리고자 합니다.', '-고자 하다 = to intend to, to wish to (formal style): 오늘은 환경 문제에 대해 말씀드리고자 합니다.'),
        ('Devant un autre verbe, -고자 = afin de : 백성을 돕고자 하늘에서 내려왔다.', 'Before another verb, -고자 = in order to: 백성을 돕고자 하늘에서 내려왔다.'),
      ], [
        G('gram-ko-gojahada', '-고자 하다', None, '-goja hada', ('avoir l’intention de (formel)', 'to intend to (formal)')),
        V('ko-ingan', '인간', None, 'ingan', ('être humain', 'human being')),
        V('ko-sesang', '세상', None, 'sesang', ('le monde (des hommes)', 'the world (human society)')),
        V('ko-daseurida', '다스리다', None, 'daseurida', ('gouverner', 'to govern, to rule')),
        V('ko-neolli', '널리', None, 'neolli', ('largement, partout', 'widely')),
        V('ko-iropda', '이롭다', None, 'iropda', ('être profitable, bénéfique', 'to be beneficial')),
        V('ko-hongigingan', '홍익인간', None, 'hongigingan', ('bénéficier largement à l’humanité', 'to benefit all humankind')),
      ], [
        ex('환웅은 인간 세상을 널리 이롭게 하고자 하늘에서 내려왔다.', None, 'Hwanung descendit du ciel afin d’apporter de grands bienfaits au monde des hommes.', 'Hwanung came down from heaven in order to greatly benefit the human world.'),
        ex('오늘은 한국의 건국 신화에 대해 말씀드리고자 합니다.', None, 'Aujourd’hui, je souhaiterais vous parler du mythe fondateur de la Corée.', 'Today I would like to speak to you about Korea’s founding myth.'),
      ], [
        FB(CHOOSE, '이번 발표에서는 연구 결과를 ＿ 합니다.', ['소개하고자', '소개하는 바', '소개하며'], '소개하고자', ('Intention formelle : -고자 하다.', 'Formal intention: -고자 하다.'), ('Dans cette présentation, je souhaite vous présenter les résultats de la recherche.', 'In this presentation, I intend to introduce the research results.')),
        FB(CHOOSE, '환웅은 세상을 ＿ 바람, 비, 구름을 거느리고 내려왔다.', ['다스리고자', '다스린 나머지', '다스릴망정'], '다스리고자', ('But (soutenu) : -고자.', 'Purpose (formal): -고자.'), ('Pour gouverner le monde, Hwanung descendit accompagné du vent, de la pluie et des nuages.', 'To govern the world, Hwanung came down leading wind, rain and clouds.')),
        SO(('Remets dans l’ordre : « Je souhaiterais dire quelques mots. »', 'Put in order: “I would like to say a few words.”'), ['몇', '말씀', '드리고자', '합니다.'], ('Formule de discours : -고자 합니다.', 'Speech formula: -고자 합니다.')),
        TF('「홍익인간」은 널리 인간을 이롭게 한다는 뜻이다.', ('Hongik ingan signifie « bénéficier largement à l’humanité ».', 'Hongik ingan means “to benefit all humankind”.'), VRAI, ('널리 인간을 이롭게 하다 = être bénéfique à tous les hommes.', '널리 인간을 이롭게 하다 = to benefit all people.')),
      ]),
    L('ko-eumyeo', ('Et, tout en (écrit) : -(으)며', 'And, while (written): -(으)며'), ('Enchaîner des idées à l’écrit.', 'Link ideas in writing.'), 9, [
        ('-(으)며 = et (énumération écrite) : 그는 학자이며 시인이다. Aussi = tout en : 노래를 부르며 춤을 췄다.', '-(으)며 = and (written listing): 그는 학자이며 시인이다. Also = while: 노래를 부르며 춤을 췄다.'),
        ('C’est la version écrite de -고 et de -(으)면서.', 'It is the written version of -고 and -(으)면서.'),
      ], [
        G('gram-ko-eumyeo', '-(으)며', None, '-(eu)myeo', ('et ; tout en (écrit)', 'and; while (written)')),
        V('ko-goksik', '곡식', None, 'goksik', ('céréales', 'grain, cereals')),
        V('ko-saengmyeong', '생명', None, 'saengmyeong', ('vie (biologique)', 'life (living)')),
        V('ko-jilbyeong', '질병', None, 'jilbyeong', ('maladie (soutenu)', 'disease')),
        V('ko-hyeongbeol', '형벌', None, 'hyeongbeol', ('sanction, punition', 'punishment, penalty')),
        V('ko-seonak', '선악', None, 'seonak', ('le bien et le mal', 'good and evil')),
      ], [
        ex('환웅은 곡식과 생명, 질병과 형벌, 선악을 다스렸으며 인간 세상의 삼백육십 가지 일을 맡았다.', None, 'Hwanung régnait sur les céréales et la vie, les maladies et les châtiments, le bien et le mal, et se chargeait des trois cent soixante affaires du monde.', 'Hwanung ruled over grain and life, disease and punishment, good and evil, and took charge of the 360 affairs of the human world.'),
        ex('그는 소설가이며 화가이다.', None, 'Il est romancier et peintre.', 'He is a novelist and a painter.'),
      ], [
        FB(CHOOSE, '이 도시는 역사가 ＿ 자연환경도 아름답다.', ['깊으며', '깊고자', '깊은 나머지'], '깊으며', ('Énumération écrite : -(으)며.', 'Written listing: -(으)며.'), ('Cette ville a une longue histoire, et son environnement naturel est beau.', 'This city has a long history, and its natural environment is beautiful too.')),
        FB(CHOOSE, '아이들은 노래를 ＿ 춤을 추었다.', ['부르며', '부르고자', '부를망정'], '부르며', ('Simultanéité (écrit) : -(으)며.', 'Simultaneity (written): -(으)며.'), ('Les enfants dansaient en chantant.', 'The children danced while singing.')),
        SO(('Remets dans l’ordre : « Il est enseignant et écrivain. »', 'Put in order: “He is a teacher and a writer.”'), ['그는', '교사이며', '작가이다.'], ('Nom + -(이)며.', 'Noun + -(이)며.')),
        TF('환웅은 선악과 형벌을 다스렸다.', ('Hwanung ne s’occupait que des céréales.', 'Hwanung only dealt with grain.'), FAUX, ('Il gouvernait aussi le bien, le mal et les châtiments.', 'He also ruled good, evil and punishment.')),
      ]),
    L('ko-neun-baida', ('Ce que… (formel) : -는 바', 'What… (formal): -는 바'), ('Employer 바 dans les discours et les textes officiels.', 'Use 바 in speeches and official texts.'), 9, [
        ('-는 바이다 = c’est ce que… (déclaration solennelle) : 여러분의 협조를 부탁드리는 바입니다.', '-는 바이다 = it is what… (solemn statement): 여러분의 협조를 부탁드리는 바입니다.'),
        ('-(으)ㄴ/는 바와 같이 = comme : 앞에서 말한 바와 같이 (comme indiqué plus haut). 바 remplace 것 dans le style écrit.', '-(으)ㄴ/는 바와 같이 = as: 앞에서 말한 바와 같이 (as mentioned above). 바 replaces 것 in written style.'),
      ], [
        G('gram-ko-neun-baida', '-는 바이다 / -(으)ㄴ 바와 같이', None, '-neun baida / -(eu)n bawa gachi', ('c’est ce que… ; comme (formel)', 'it is that…; as (formal)')),
        V('ko-seoneonhada', '선언하다', None, 'seoneonhada', ('déclarer, proclamer', 'to declare, to proclaim')),
        V('ko-gangjohada', '강조하다', None, 'gangjohada', ('souligner, insister', 'to emphasise')),
        V('ko-jujanghada', '주장하다', None, 'jujanghada', ('affirmer, soutenir', 'to claim, to argue')),
        V('ko-jeanhada', '제안하다', None, 'jeanhada', ('proposer', 'to propose')),
        V('ko-yeonseol', '연설', None, 'yeonseol', ('discours', 'speech, address')),
        V('ko-gungmin', '국민', None, 'gungmin', ('citoyens, peuple d’un pays', 'the people, citizens')),
      ], [
        ex('앞에서 말씀드린 바와 같이 이 정책은 국민 모두를 위한 것입니다.', None, 'Comme je l’ai indiqué plus haut, cette politique est destinée à tous les citoyens.', 'As I mentioned earlier, this policy is for all citizens.'),
        ex('이에 새 나라의 시작을 선언하는 바입니다.', None, 'Je proclame donc ici la naissance d’un nouveau pays.', 'I hereby declare the beginning of a new nation.'),
      ], [
        FB(CHOOSE, '앞에서 ＿ 바와 같이 환경 보호가 중요합니다.', ['강조한', '강조하며', '강조하고자'], '강조한', ('Comme on l’a dit : -(으)ㄴ 바와 같이.', 'As stated: -(으)ㄴ 바와 같이.'), ('Comme souligné plus haut, la protection de l’environnement est importante.', 'As emphasised above, protecting the environment is important.')),
        FB(CHOOSE, '여러분의 적극적인 참여를 ＿ 바입니다.', ['부탁드리는', '부탁드린 나머지', '부탁드릴망정'], '부탁드리는', ('Déclaration solennelle : -는 바입니다.', 'Solemn statement: -는 바입니다.'), ('Nous vous demandons votre participation active.', 'We ask for your active participation.')),
        SO(('Remets dans l’ordre : « Le président a souligné ce point dans son discours. »', 'Put in order: “The president emphasised this point in his speech.”'), ['대통령은', '연설에서', '이', '점을', '강조했다.'], ('Sujet + lieu + objet + verbe.', 'Subject + place + object + verb.')),
        TF('그는 연설에서 새로운 정책을 제안했다.', ('Il a proposé une nouvelle politique.', 'He proposed a new policy.'), VRAI, ('제안했다 = a proposé.', '제안했다 = proposed.')),
      ]),
  ])])

# ═════════════════════════ Île 2 : la caverne ═════════════════════════
W2 = WORLD('topik6-w2', ('La caverne de l’ourse et du tigre', 'The cave of the bear and the tiger'), REGION,
  ('La concession forte : -(으)ㄴ들, -(으)ㄹ지언정, -(으)ㄹ망정.', 'Strong concession: -(으)ㄴ들, -(으)ㄹ지언정, -(으)ㄹ망정.'),
  (('Ungnyeo, la femme-ourse', 'Ungnyeo, the Bear Woman'), '웅', ('L’ourse resta cent jours dans la caverne, sans voir le soleil, à ne manger que de l’armoise et de l’ail. Le tigre abandonna ; elle devint femme et mère de Dangun. Elle n’honore que la persévérance absolue.', 'The bear stayed a hundred days in the cave, never seeing the sun, eating only mugwort and garlic. The tiger gave up; she became a woman and the mother of Dangun. She honours only absolute perseverance.')),
  [CH('topik6-w2-c1', ('Coûte que coûte', 'Whatever it costs'), [
    L('ko-eundeul', ('À quoi bon… : -(으)ㄴ들', 'Even if… what’s the use: -(으)ㄴ들'), ('Dire qu’une hypothèse ne changerait rien.', 'Say a hypothesis would change nothing.'), 10, [
        ('-(으)ㄴ들 = même si…, (à quoi bon / ça ne changerait rien) : 지금 후회한들 무슨 소용이 있겠어요?', '-(으)ㄴ들 = even if…, (what’s the use / it wouldn’t change anything): 지금 후회한들 무슨 소용이 있겠어요?'),
        ('Souvent suivi d’une question rhétorique : 아무리 빨리 간들 늦지 않겠어요?', 'Often followed by a rhetorical question: 아무리 빨리 간들 늦지 않겠어요?'),
      ], [
        G('gram-ko-eundeul', '-(으)ㄴ들', None, '-(eu)ndeul', ('même si… (à quoi bon)', 'even if… (what’s the use)')),
        V('ko-donggul', '동굴', None, 'donggul', ('caverne, grotte', 'cave')),
        V('ko-ssuk', '쑥', None, 'ssuk', ('armoise', 'mugwort')),
        V('ko-maneul', '마늘', None, 'maneul', ('ail', 'garlic')),
        V('ko-haetbit', '햇빛', None, 'haetbit', ('lumière du soleil', 'sunlight')),
        V('ko-gom', '곰', None, 'gom', ('ours', 'bear')),
        V('ko-horangi', '호랑이', None, 'horangi', ('tigre', 'tiger')),
      ], [
        ex('호랑이가 아무리 후회한들 이미 늦었다.', None, 'Le tigre avait beau regretter, il était déjà trop tard.', 'However much the tiger regretted it, it was already too late.'),
        ex('햇빛을 백 일 동안 보지 못한들 사람이 될 수 있다면 참겠어요.', None, 'Même si je ne dois pas voir le soleil pendant cent jours, je tiendrai si je peux devenir humaine.', 'Even if I can’t see the sun for a hundred days, I’ll endure it if I can become human.'),
      ], [
        FB(CHOOSE, '지금 ＿ 무슨 소용이 있겠어요?', ['후회한들', '후회하고자', '후회하며'], '후회한들', ('À quoi bon : -(으)ㄴ들 + question rhétorique.', 'What’s the use: -(으)ㄴ들 + rhetorical question.'), ('À quoi bon regretter maintenant ?', 'What’s the use of regretting now?')),
        FB(CHOOSE, '아무리 빨리 ＿ 기차를 탈 수 있을까요?', ['달린들', '달린 나머지', '달리는 바'], '달린들', ('Hypothèse vaine : -(으)ㄴ들.', 'Pointless hypothesis: -(으)ㄴ들.'), ('Même en courant le plus vite possible, est-ce que j’attraperai le train ?', 'Even if I run as fast as I can, will I make the train?')),
        DC(('Ton ami s’en veut d’avoir raté une occasion.', 'Your friend blames himself for missing an opportunity.'), [('친구', '그때 그 회사에 지원할걸 그랬어요.')], ('Ton ami regrette de ne pas avoir postulé.', 'Your friend regrets not applying.'), ['이제 와서 후회한들 소용없어요. 다음 기회를 준비해요.', '후회하고자 합니다.', '후회하는 바입니다.'], '이제 와서 후회한들 소용없어요. 다음 기회를 준비해요.', ('Consoler : -(으)ㄴ들 소용없다.', 'Consoling: -(으)ㄴ들 소용없다.')),
        TF('곰은 동굴에서 쑥과 마늘만 먹으며 견뎠다.', ('L’ourse a mangé de la viande dans la caverne.', 'The bear ate meat in the cave.'), FAUX, ('쑥과 마늘만 = seulement de l’armoise et de l’ail.', '쑥과 마늘만 = only mugwort and garlic.')),
      ]),
    L('ko-euljieonjeong', ('Plutôt… que : -(으)ㄹ지언정', 'Would rather… than: -(으)ㄹ지언정'), ('Exprimer une résolution inébranlable.', 'Express unshakeable resolve.'), 10, [
        ('-(으)ㄹ지언정 = quitte à…, plutôt… que : 굶을지언정 뜻을 굽히지 않겠다 (je préfère jeûner plutôt que de renoncer).', '-(으)ㄹ지언정 = even at the cost of…, would rather… than: 굶을지언정 뜻을 굽히지 않겠다 (I’d rather starve than give in).'),
        ('Ton fort et littéraire, souvent avec 차라리 (plutôt).', 'A strong, literary tone, often with 차라리 (rather).'),
      ], [
        G('gram-ko-euljieonjeong', '-(으)ㄹ지언정', None, '-(eu)ljieonjeong', ('quitte à…, plutôt… que', 'even at the cost of, would rather… than')),
        V('ko-gumda', '굶다', None, 'gumda', ('jeûner, ne pas manger', 'to go hungry, to starve')),
        V('ko-gupida', '굽히다', None, 'gupida', ('plier, céder', 'to bend, to yield')),
        V('ko-jajonsim', '자존심', None, 'jajonsim', ('fierté, amour-propre', 'pride, self-respect')),
        V('ko-tteut', '뜻', None, 'tteut', ('sens ; volonté', 'meaning; will, intention')),
        V('ko-kkeokda', '꺾다', None, 'kkeokda', ('briser, casser', 'to break, to snap')),
        V('ko-charari', '차라리', None, 'charari', ('plutôt, autant', 'rather, would sooner')),
      ], [
        ex('굶을지언정 남의 것을 빼앗지는 않겠다.', None, 'Je préfère jeûner plutôt que de prendre ce qui appartient aux autres.', 'I would rather starve than take what belongs to others.'),
        ex('곰은 힘들지언정 끝까지 뜻을 꺾지 않았다.', None, 'Si dur que ce fût, l’ourse ne renonça jamais.', 'Hard as it was, the bear never gave up her resolve.'),
      ], [
        FB(CHOOSE, '차라리 ＿ 거짓말은 하지 않겠어요.', ['혼날지언정', '혼난들요', '혼나고자'], '혼날지언정', ('Plutôt… que : -(으)ㄹ지언정.', 'Would rather… than: -(으)ㄹ지언정.'), ('Je préfère me faire gronder plutôt que de mentir.', 'I’d rather be told off than tell a lie.')),
        FB(CHOOSE, '가난하게 ＿ 자존심을 버리지는 않겠다.', ['살지언정', '사는 바', '살며'], '살지언정', ('Résolution : -(으)ㄹ지언정.', 'Resolve: -(으)ㄹ지언정.'), ('Quitte à vivre pauvrement, je ne renoncerai pas à ma fierté.', 'I may live in poverty, but I won’t give up my pride.')),
        SO(('Remets dans l’ordre : « Je ne céderai pas. »', 'Put in order: “I will not give in.”'), ['결코', '뜻을', '굽히지', '않겠다.'], ('Adverbe + objet + 굽히지 않겠다.', 'Adverb + object + 굽히지 않겠다.')),
        TF('호랑이는 굶을지언정 끝까지 참았다.', ('Le tigre a tenu jusqu’au bout.', 'The tiger held out to the end.'), FAUX, ('Dans le mythe, le tigre abandonne avant les cent jours.', 'In the myth, the tiger gives up before the hundred days.')),
      ]),
    L('ko-eulmangjeong', ('Même si… au moins : -(으)ㄹ망정', 'Even if… at least: -(으)ㄹ망정'), ('Admettre un défaut pour mettre en valeur une qualité.', 'Admit a flaw to highlight a virtue.'), 9, [
        ('-(으)ㄹ망정 = même si…, (au moins) : 비록 가난할망정 떳떳하게 살겠다 (pauvre peut-être, mais intègre).', '-(으)ㄹ망정 = even if…, (at least): 비록 가난할망정 떳떳하게 살겠다 (poor perhaps, but upright).'),
        ('Souvent avec 비록 (bien que). Très proche de -(으)ㄹ지언정.', 'Often with 비록 (although). Very close to -(으)ㄹ지언정.'),
      ], [
        G('gram-ko-eulmangjeong', '-(으)ㄹ망정', None, '-(eu)lmangjeong', ('même si… (au moins)', 'even if… (at least)')),
        V('ko-gananhada', '가난하다', None, 'gananhada', ('être pauvre', 'to be poor')),
        V('ko-birok', '비록', None, 'birok', ('bien que, malgré le fait que', 'although, even though')),
        V('ko-tteottteotada', '떳떳하다', None, 'tteottteotada', ('avoir la conscience tranquille, être intègre', 'to be upright, unashamed')),
        V('ko-chameulseong', '참을성', None, 'chameulseong', ('patience', 'patience')),
        V('ko-innae', '인내', None, 'innae', ('endurance, persévérance', 'perseverance, endurance')),
        V('ko-baegil', '백일', None, 'baegil', ('cent jours ; centième jour (d’un bébé)', 'a hundred days; a baby’s 100th day')),
      ], [
        ex('비록 가난할망정 떳떳하게 살고 싶어요.', None, 'Même si je suis pauvre, je veux vivre la tête haute.', 'Even if I’m poor, I want to live with my head held high.'),
        ex('곰은 인내와 참을성으로 백일을 견뎌 사람이 되었다.', None, 'Grâce à sa persévérance et à sa patience, l’ourse tint cent jours et devint humaine.', 'Through perseverance and patience, the bear endured a hundred days and became human.'),
      ], [
        FB(CHOOSE, '비록 시험에 ＿ 최선을 다했으니 후회는 없어요.', ['떨어졌을망정', '떨어지고자', '떨어진 바'], '떨어졌을망정', ('Admettre un échec : -았/었을망정.', 'Admitting a failure: -았/었을망정.'), ('Même si j’ai échoué, j’ai fait de mon mieux : je n’ai pas de regrets.', 'Even though I failed, I did my best, so I have no regrets.')),
        FB(CHOOSE, '집은 ＿ 마음은 편해요.', ['작을망정', '작으며', '작고자'], '작을망정', ('Défaut + qualité : -(으)ㄹ망정.', 'Flaw + virtue: -(으)ㄹ망정.'), ('La maison est petite, peut-être, mais on y est bien.', 'The house may be small, but I feel at ease.')),
        SO(('Remets dans l’ordre : « Il lui faut de la patience. »', 'Put in order: “He needs patience.”'), ['그에게는', '참을성이', '필요하다.'], ('Personne-에게는 + nom-이 필요하다.', 'Person-에게는 + noun-이 필요하다.')),
        TF('비록 늦을망정 포기하지 않겠어요.', ('La personne renonce parce qu’elle est en retard.', 'The speaker gives up because they’re late.'), FAUX, ('포기하지 않겠어요 = je n’abandonnerai pas.', '포기하지 않겠어요 = I won’t give up.')),
      ]),
  ])])

# ═════════════════════════ Île 3 : Jumong ═════════════════════════
W3 = WORLD('topik6-w3', ('La rivière de Jumong', 'Jumong’s river'), REGION,
  ('Comparer et décrire finement : -다시피, -(으)ㄴ/는 듯하다, -듯이.', 'Fine comparison and description: -다시피, -(으)ㄴ/는 듯하다, -듯이.'),
  (('Jumong, l’archer né d’un œuf', 'Jumong, the Archer Born from an Egg'), '주', ('Né d’un œuf, Jumong tirait si juste qu’on le jalousa ; poursuivi, il traversa la rivière sur un pont de poissons et de tortues et fonda Goguryeo. Il teste la précision de ta langue comme celle d’une flèche.', 'Born from an egg, Jumong shot so accurately that he was envied; when pursued, he crossed the river on a bridge of fish and turtles and founded Goguryeo. He tests the precision of your language like that of an arrow.')),
  [CH('topik6-w3-c1', ('Comme…', 'As…'), [
    L('ko-dasipi', ('Comme vous le savez : -다시피', 'As you know: -다시피'), ('Renvoyer à ce que l’interlocuteur sait ou voit.', 'Refer to what the listener knows or sees.'), 10, [
        ('-다시피 = comme (vous le savez, le voyez) : 아시다시피 주몽은 활을 잘 쏘았습니다. Avec 알다, 보다, 듣다, 느끼다.', '-다시피 = as (you know, can see): 아시다시피 주몽은 활을 잘 쏘았습니다. With 알다, 보다, 듣다, 느끼다.'),
        ('Avec d’autres verbes, -다시피 하다 = presque, pour ainsi dire : 매일 굶다시피 했다.', 'With other verbs, -다시피 하다 = almost, practically: 매일 굶다시피 했다.'),
      ], [
        G('gram-ko-dasipi', '-다시피', None, '-dasipi', ('comme (vous le savez) ; presque', 'as (you know); practically')),
        V('ko-hwal', '활', None, 'hwal', ('arc', 'bow')),
        V('ko-ssoda', '쏘다', None, 'ssoda', ('tirer (une flèche)', 'to shoot')),
        V('ko-hwasal', '화살', None, 'hwasal', ('flèche', 'arrow')),
        V('ko-myeongjunghada', '명중하다', None, 'myeongjunghada', ('atteindre la cible', 'to hit the target')),
        V('ko-somssi', '솜씨', None, 'somssi', ('adresse, savoir-faire', 'skill, dexterity')),
        V('ko-gwanyeok', '과녁', None, 'gwanyeok', ('cible', 'target')),
      ], [
        ex('여러분도 아시다시피 주몽은 활 솜씨가 뛰어났습니다.', None, 'Comme vous le savez, Jumong était un archer remarquable.', 'As you all know, Jumong was an outstanding archer.'),
        ex('시험 기간에는 도서관에서 살다시피 했어요.', None, 'Pendant les examens, je vivais pratiquement à la bibliothèque.', 'During exams I practically lived in the library.'),
      ], [
        FB(CHOOSE, '보시＿ 이 화살은 과녁에 정확히 명중했습니다.', ['다시피', '듯이', '며'], '다시피', ('Comme vous le voyez : 보시다시피.', 'As you can see: 보시다시피.'), ('Comme vous le voyez, cette flèche a atteint la cible en plein centre.', 'As you can see, this arrow hit the target dead centre.')),
        FB(CHOOSE, '이사 준비 때문에 일주일 동안 밤을 ＿ 했어요.', ['새우다시피', '새운 듯이', '새우고자'], '새우다시피', ('Presque : -다시피 하다.', 'Practically: -다시피 하다.'), ('À cause des préparatifs du déménagement, j’ai pratiquement passé des nuits blanches toute la semaine.', 'Because of moving, I practically stayed up all night for a week.')),
        SO(('Remets dans l’ordre : « Comme vous le savez, l’examen est demain. »', 'Put in order: “As you know, the exam is tomorrow.”'), ['아시다시피', '시험은', '내일입니다.'], ('아시다시피 en tête de phrase.', '아시다시피 at the start of the sentence.')),
        TF('주몽은 화살을 쏘면 과녁에 명중했다.', ('Jumong ratait souvent la cible.', 'Jumong often missed the target.'), FAUX, ('명중했다 = il atteignait la cible.', '명중했다 = he hit the target.')),
      ]),
    L('ko-eun-deutada', ('Il semble que (écrit) : -는 듯하다', 'It seems (written): -는 듯하다'), ('Exprimer une impression avec un style soutenu.', 'Express an impression in a formal style.'), 9, [
        ('-(으)ㄴ/는 듯하다 = il semble que, on dirait (soutenu) : 알이 곧 깨질 듯하다. Équivalent écrit de -는 것 같다.', '-(으)ㄴ/는 듯하다 = it seems, it looks as if (formal): 알이 곧 깨질 듯하다. Written equivalent of -는 것 같다.'),
        ('Futur : -(으)ㄹ 듯하다 ; passé : -(으)ㄴ 듯하다.', 'Future: -(으)ㄹ 듯하다; past: -(으)ㄴ 듯하다.'),
      ], [
        G('gram-ko-eun-deutada', '-(으)ㄴ/는 듯하다', None, '-(eu)n / -neun deutada', ('il semble que (soutenu)', 'it seems that (formal)')),
        V('ko-al', '알', None, 'al', ('œuf ; grain', 'egg; grain')),
        V('ko-kkaeda', '깨다', None, 'kkaeda', ('casser ; se réveiller', 'to break; to wake')),
        V('ko-sinbiropda', '신비롭다', None, 'sinbiropda', ('être mystérieux', 'to be mysterious')),
        V('ko-bibeomhada', '비범하다', None, 'bibeomhada', ('être hors du commun', 'to be extraordinary')),
        V('ko-sigihada', '시기하다', None, 'sigihada', ('jalouser', 'to be jealous of, to envy')),
        V('ko-talchulhada', '탈출하다', None, 'talchulhada', ('s’échapper', 'to escape')),
      ], [
        ex('알에서 신비로운 빛이 나는 듯했다.', None, 'Une lumière mystérieuse semblait émaner de l’œuf.', 'A mysterious light seemed to come from the egg.'),
        ex('왕자들은 주몽의 비범한 재주를 시기한 듯하다.', None, 'Les princes semblent avoir jalousé les talents hors du commun de Jumong.', 'The princes seem to have envied Jumong’s extraordinary talents.'),
      ], [
        FB(CHOOSE, '하늘이 어두워지는 걸 보니 곧 비가 ＿.', ['올 듯하다', '오다시피 하다', '오는 바이다'], '올 듯하다', ('Impression sur l’avenir : -(으)ㄹ 듯하다.', 'Impression about the future: -(으)ㄹ 듯하다.'), ('Le ciel s’assombrit : il va sans doute pleuvoir.', 'The sky is darkening, it seems it will rain soon.')),
        FB(CHOOSE, '그는 무언가 ＿ 듯했지만 끝내 말하지 않았다.', ['숨기는', '숨기며', '숨기고자'], '숨기는', ('Présent : -는 듯하다.', 'Present: -는 듯하다.'), ('Il semblait cacher quelque chose, mais il ne dit rien jusqu’au bout.', 'He seemed to be hiding something, but he never said it.')),
        SO(('Remets dans l’ordre : « L’œuf s’est cassé et un enfant en est sorti. »', 'Put in order: “The egg broke and a child came out.”'), ['알이', '깨지고', '아이가', '나왔다.'], ('Deux propositions reliées par -고.', 'Two clauses linked by -고.')),
        TF('주몽은 왕자들의 시기를 피해 탈출했다.', ('Jumong a fui la jalousie des princes.', 'Jumong escaped the princes’ envy.'), VRAI, ('시기를 피해 탈출했다 = s’est échappé pour fuir la jalousie.', '시기를 피해 탈출했다 = escaped to avoid their envy.')),
      ]),
    L('ko-deusi', ('Comme si : -듯이', 'As if: -듯이'), ('Comparer une action à une autre, souvent dans des images.', 'Compare one action to another, often in imagery.'), 9, [
        ('-듯이 = comme, de même que : 물 쓰듯이 돈을 쓰다 (dépenser l’argent comme de l’eau). Aussi -는 듯이 = comme si : 아무 일도 없었다는 듯이.', '-듯이 = like, just as: 물 쓰듯이 돈을 쓰다 (to spend money like water). Also -는 듯이 = as if: 아무 일도 없었다는 듯이.'),
        ('Fréquent dans les proverbes et les récits.', 'Common in proverbs and stories.'),
      ], [
        G('gram-ko-deusi', '-듯이', None, '-deusi', ('comme, comme si', 'like, as if')),
        V('ko-mulgogi', '물고기', None, 'mulgogi', ('poisson', 'fish')),
        V('ko-jara', '자라', None, 'jara', ('tortue d’eau douce', 'soft-shelled turtle')),
        V('ko-dari', '다리', None, 'dari', ('pont ; jambe', 'bridge; leg')),
        V('ko-geonneoda', '건너다', None, 'geonneoda', ('traverser', 'to cross')),
        V('ko-jjotgida', '쫓기다', None, 'jjotgida', ('être poursuivi', 'to be chased')),
        V('ko-seuda', '세우다', None, 'seuda', ('fonder, ériger ; arrêter', 'to found, to build; to stop')),
      ], [
        ex('물고기와 자라들이 약속이라도 한 듯이 다리를 만들었다.', None, 'Les poissons et les tortues formèrent un pont, comme s’ils s’étaient donné le mot.', 'The fish and turtles formed a bridge, as if they had agreed to it.'),
        ex('그는 돈을 물 쓰듯이 썼다.', None, 'Il dépensait l’argent comme de l’eau.', 'He spent money like water.'),
      ], [
        FB(CHOOSE, '그는 아무 일도 없었다는 ＿ 웃었다.', ['듯이', '다시피', '바와'], '듯이', ('Comme si : -는 듯이.', 'As if: -는 듯이.'), ('Il souriait comme si de rien n’était.', 'He smiled as if nothing had happened.')),
        FB(CHOOSE, '쫓기던 주몽은 물고기 다리를 ＿ 강을 건넜다.', ['밟으며', '밟고자', '밟을망정'], '밟으며', ('Tout en (écrit) : -(으)며.', 'While (written): -(으)며.'), ('Poursuivi, Jumong traversa la rivière en marchant sur le pont de poissons.', 'Pursued, Jumong crossed the river stepping on the fish bridge.')),
        SO(('Remets dans l’ordre : « Jumong fonda un pays. »', 'Put in order: “Jumong founded a country.”'), ['주몽은', '나라를', '세웠다.'], ('Sujet + 나라를 세우다.', 'Subject + 나라를 세우다.')),
        TF('물고기와 자라가 다리를 만들어 주몽을 도왔다.', ('Des poissons et des tortues ont aidé Jumong.', 'Fish and turtles helped Jumong.'), VRAI, ('다리를 만들어 도왔다 = ils l’ont aidé en formant un pont.', '다리를 만들어 도왔다 = they helped by forming a bridge.')),
      ]),
  ])])

# ═════════════════════════ Île 4 : la forêt de Gyerim ═════════════════════════
W4 = WORLD('topik6-w4', ('Le puits du cheval blanc', 'The white horse’s well'), REGION,
  ('Les degrés extrêmes : -(으)ㄹ 나위가 없다, -기 그지없다, -기 짝이 없다.', 'Extreme degrees: -(으)ㄹ 나위가 없다, -기 그지없다, -기 짝이 없다.'),
  (('Bak Hyeokgeose, roi né d’un œuf', 'Bak Hyeokgeose, the Egg-born King'), '박', ('Près d’un puits, un cheval blanc s’agenouilla devant un grand œuf, puis s’envola : il en sortit Bak Hyeokgeose, premier roi de Silla. Il n’accepte que des éloges et des reproches mesurés au plus juste.', 'Beside a well, a white horse knelt before a great egg and then flew away: out came Bak Hyeokgeose, the first king of Silla. He accepts only praise and blame measured exactly.')),
  [CH('topik6-w4-c1', ('On ne peut plus…', 'As… as can be'), [
    L('ko-eul-nawi', ('Rien de mieux : -(으)ㄹ 나위가 없다', 'Couldn’t be better: -(으)ㄹ 나위가 없다'), ('Dire qu’une chose est parfaite, qu’il n’y a rien à ajouter.', 'Say something is perfect, with nothing to add.'), 10, [
        ('더할 나위 없다 = il n’y a rien de mieux, c’est parfait : 더할 나위 없이 행복해요. Aussi 말할 나위도 없다 (cela va sans dire).', '더할 나위 없다 = nothing could be better, it’s perfect: 더할 나위 없이 행복해요. Also 말할 나위도 없다 (it goes without saying).'),
        ('Expression figée, utilisée surtout avec 더하다 et 말하다.', 'A set expression, used mostly with 더하다 and 말하다.'),
      ], [
        G('gram-ko-eul-nawi', '-(으)ㄹ 나위가 없다', None, '-(eu)l nawiga eopda', ('il n’y a rien de plus à…', 'there is no need / room to…')),
        V('ko-wanbyeokada', '완벽하다', None, 'wanbyeokada', ('être parfait', 'to be perfect')),
        V('ko-hullyunghada', '훌륭하다', None, 'hullyunghada', ('être remarquable, admirable', 'to be excellent, admirable')),
        V('ko-manjokada', '만족하다', None, 'manjokada', ('être satisfait', 'to be satisfied')),
        V('ko-baengma', '백마', None, 'baengma', ('cheval blanc', 'white horse')),
        V('ko-umul', '우물', None, 'umul', ('puits', 'well')),
        V('ko-tansaeng', '탄생', None, 'tansaeng', ('naissance', 'birth')),
      ], [
        ex('새 왕의 탄생을 지켜본 백성들은 더할 나위 없이 기뻐했다.', None, 'Le peuple, témoin de la naissance du nouveau roi, fut on ne peut plus heureux.', 'The people who witnessed the new king’s birth were overjoyed.'),
        ex('그의 실력이 훌륭하다는 것은 말할 나위도 없다.', None, 'Il va sans dire que son talent est remarquable.', 'It goes without saying that his skill is excellent.'),
      ], [
        FB(CHOOSE, '이번 여행은 날씨도 좋고 음식도 맛있어서 더할 ＿ 없었어요.', ['나위', '짝이', '그지'], '나위', ('Expression : 더할 나위 없다.', 'Expression: 더할 나위 없다.'), ('Le voyage, avec le beau temps et la bonne cuisine, était parfait.', 'With good weather and great food, the trip couldn’t have been better.')),
        FB(CHOOSE, '그 선수가 최고라는 것은 ＿ 나위도 없어요.', ['말할', '말한', '말하는'], '말할', ('Cela va sans dire : 말할 나위도 없다.', 'It goes without saying: 말할 나위도 없다.'), ('Il va sans dire que ce joueur est le meilleur.', 'It goes without saying that player is the best.')),
        SO(('Remets dans l’ordre : « Je suis parfaitement satisfait du résultat. »', 'Put in order: “I’m perfectly satisfied with the result.”'), ['결과에', '더할', '나위', '없이', '만족해요.'], ('더할 나위 없이 + verbe.', '더할 나위 없이 + verb.')),
        TF('우물 옆에서 백마가 큰 알을 지키고 있었다.', ('Un cheval blanc gardait un grand œuf près du puits.', 'A white horse was guarding a big egg near the well.'), VRAI, ('우물 옆 = près du puits.', '우물 옆 = beside the well.')),
      ]),
    L('ko-gi-geujieopda', ('Infiniment : -기 그지없다', 'Utterly: -기 그지없다'), ('Exprimer un sentiment poussé à l’extrême, dans un style soutenu.', 'Express a feeling taken to the extreme, in a formal style.'), 9, [
        ('Adjectif + -기 그지없다 = infiniment, au plus haut point : 기쁘기 그지없습니다 (je suis infiniment heureux).', 'Adjective + -기 그지없다 = utterly, beyond measure: 기쁘기 그지없습니다 (I am overjoyed).'),
        ('Propre aux discours et aux lettres : 감사하기 그지없습니다, 송구하기 그지없습니다.', 'Typical of speeches and letters: 감사하기 그지없습니다, 송구하기 그지없습니다.'),
      ], [
        G('gram-ko-gi-geujieopda', '-기 그지없다', None, '-gi geujieopda', ('infiniment, au plus haut point', 'utterly, beyond measure')),
        V('ko-gippeuda', '기쁘다', None, 'gippeuda', ('être heureux, joyeux', 'to be glad, joyful')),
        V('ko-gamgyeokada', '감격하다', None, 'gamgyeokada', ('être profondément ému', 'to be deeply moved')),
        V('ko-yeonggwang', '영광', None, 'yeonggwang', ('honneur, gloire', 'honour, glory')),
        V('ko-songguhada', '송구하다', None, 'songguhada', ('être confus (excuses)', 'to feel deeply sorry')),
        V('ko-chukbok', '축복', None, 'chukbok', ('bénédiction', 'blessing')),
      ], [
        ex('이런 상을 받게 되어 영광스럽기 그지없습니다.', None, 'Recevoir un tel prix est pour moi un immense honneur.', 'It is the greatest honour to receive such an award.'),
        ex('기다리게 해 드려서 송구하기 그지없습니다.', None, 'Je suis infiniment confus de vous avoir fait attendre.', 'I am deeply sorry to have kept you waiting.'),
      ], [
        FB(CHOOSE, '여러분의 축하를 받으니 ＿ 그지없습니다.', ['기쁘기', '기쁜', '기뻐서'], '기쁘기', ('Adjectif + -기 그지없다.', 'Adjective + -기 그지없다.'), ('Recevoir vos félicitations me remplit d’une joie infinie.', 'Receiving your congratulations makes me overjoyed.')),
        FB(CHOOSE, '큰 실수를 하여 ＿ 그지없습니다.', ['송구하기', '송구하고자', '송구하며'], '송구하기', ('Excuses solennelles : 송구하기 그지없다.', 'Solemn apology: 송구하기 그지없다.'), ('J’ai commis une grave erreur : j’en suis infiniment confus.', 'I made a serious mistake and am deeply sorry.')),
        SO(('Remets dans l’ordre : « Ce fut une bénédiction pour le pays. »', 'Put in order: “It was a blessing for the country.”'), ['그것은', '나라의', '축복이었다.'], ('Sujet + nom-이었다.', 'Subject + noun-이었다.')),
        TF('감사하기 그지없습니다.', ('La personne exprime une immense gratitude.', 'The speaker expresses immense gratitude.'), VRAI, ('감사하기 그지없다 = infiniment reconnaissant.', '감사하기 그지없다 = utterly grateful.')),
      ]),
    L('ko-gi-jjak', ('On ne peut plus (négatif) : -기 짝이 없다', 'Utterly (negative): -기 짝이 없다'), ('Critiquer avec force.', 'Criticise strongly.'), 9, [
        ('Adjectif + -기 짝이 없다 = on ne peut plus…, au dernier degré (souvent négatif) : 무례하기 짝이 없다 (d’une impolitesse sans nom).', 'Adjective + -기 짝이 없다 = utterly, extremely (often negative): 무례하기 짝이 없다 (incredibly rude).'),
        ('Plus familier que -기 그지없다 ; à réserver aux jugements sévères.', 'More colloquial than -기 그지없다; reserve it for harsh judgements.'),
      ], [
        G('gram-ko-gi-jjak', '-기 짝이 없다', None, '-gi jjagi eopda', ('on ne peut plus… (souvent négatif)', 'utterly, extremely (often negative)')),
        V('ko-eoriseokda', '어리석다', None, 'eoriseokda', ('être sot, stupide', 'to be foolish')),
        V('ko-muryehada', '무례하다', None, 'muryehada', ('être impoli', 'to be rude')),
        V('ko-bukkeureopda', '부끄럽다', None, 'bukkeureopda', ('avoir honte', 'to be ashamed')),
        V('ko-hansimhada', '한심하다', None, 'hansimhada', ('être lamentable', 'to be pathetic')),
        V('ko-ppeonppeonhada', '뻔뻔하다', None, 'ppeonppeonhada', ('être effronté', 'to be shameless')),
        V('ko-changpihada', '창피하다', None, 'changpihada', ('être gêné, avoir honte', 'to be embarrassed')),
      ], [
        ex('약속을 어기고도 사과하지 않다니 뻔뻔하기 짝이 없다.', None, 'Ne pas tenir sa promesse et ne même pas s’excuser : quel culot !', 'Breaking a promise and not even apologising: utterly shameless.'),
        ex('그런 실수를 하다니 창피하기 짝이 없어요.', None, 'Avoir fait une telle erreur, j’en ai terriblement honte.', 'Making such a mistake is utterly embarrassing.'),
      ], [
        FB(CHOOSE, '어른께 그렇게 말하다니 ＿ 짝이 없어요.', ['무례하기', '무례한', '무례하고자'], '무례하기', ('Critique forte : -기 짝이 없다.', 'Strong criticism: -기 짝이 없다.'), ('Parler ainsi à un aîné, c’est d’une impolitesse sans nom.', 'Speaking to an elder like that is incredibly rude.')),
        FB(CHOOSE, '같은 실수를 세 번이나 하다니 ＿ 짝이 없다.', ['한심하기', '한심하며', '한심할망정'], '한심하기', ('-기 짝이 없다.', '-기 짝이 없다.'), ('Faire trois fois la même erreur : c’est lamentable.', 'Making the same mistake three times is pathetic.')),
        DC(('Ton ami a trébuché devant toute la classe.', 'Your friend tripped in front of the whole class.'), [('친구', '사람들 앞에서 넘어져서 너무 창피했어요.')], ('Ton ami a eu honte d’être tombé en public.', 'Your friend was embarrassed to fall in public.'), ['괜찮아요. 누구나 그럴 수 있어요.', '창피하기 짝이 없네요.', '창피하고자 했어요?'], '괜찮아요. 누구나 그럴 수 있어요.', ('On console plutôt que d’enfoncer.', 'You console rather than rub it in.')),
        TF('그 행동은 어리석기 짝이 없었다.', ('Le comportement était très sage.', 'The behaviour was very wise.'), FAUX, ('어리석기 짝이 없다 = d’une sottise extrême.', '어리석기 짝이 없다 = utterly foolish.')),
      ]),
  ])])

# ═════════════════════════ Île 5 : la cloche d'Emille ═════════════════════════
W5 = WORLD('topik6-w5', ('La cloche d’Emille', 'The Emille Bell'), REGION,
  ('Craintes et avis prudents : -(으)ㄹ까 봐, -(으)ㄹ세라, -지 않을까 싶다.', 'Fears and cautious opinions: -(으)ㄹ까 봐, -(으)ㄹ세라, -지 않을까 싶다.'),
  (('L’esprit de la cloche d’Emille', 'The Spirit of the Emille Bell'), '종', ('La légende dit qu’on ne parvint à fondre la grande cloche de Silla qu’en y versant un enfant, et que son tintement appelle encore « emille, emille », maman. Parle-lui avec délicatesse et prudence.', 'Legend says the great bell of Silla could only be cast when a child was poured into it, and that its toll still calls “emille, emille”, mother. Speak to it with gentleness and care.')),
  [CH('topik6-w5-c1', ('De peur que…', 'For fear that…'), [
    L('ko-eulkka-bwa', ('De peur que : -(으)ㄹ까 봐', 'For fear that: -(으)ㄹ까 봐'), ('Dire ce qu’on fait par crainte de quelque chose.', 'Say what you do for fear of something.'), 10, [
        ('-(으)ㄹ까 봐(서) = de peur que : 늦을까 봐 택시를 탔어요. On ne l’emploie pas avec un ordre.', '-(으)ㄹ까 봐(서) = for fear that: 늦을까 봐 택시를 탔어요. It isn’t used with a command.'),
        ('En fin de phrase : -(으)ㄹ까 봐 걱정이에요 (j’ai peur que…).', 'At the end of a sentence: -(으)ㄹ까 봐 걱정이에요 (I’m worried that…).'),
      ], [
        G('gram-ko-eulkka-bwa', '-(으)ㄹ까 봐(서)', None, '-(eu)lkka bwa(seo)', ('de peur que', 'for fear that')),
        V('ko-jong', '종', None, 'jong', ('cloche', 'bell')),
        V('ko-nokda', '녹다', None, 'nokda', ('fondre', 'to melt')),
        V('ko-soe', '쇠', None, 'soe', ('fer, métal', 'iron, metal')),
        V('ko-jeongseong', '정성', None, 'jeongseong', ('dévouement, soin sincère', 'devotion, sincere effort')),
        V('ko-geokjeongdoeda', '걱정되다', None, 'geokjeongdoeda', ('être inquiet', 'to be worried')),
      ], [
        ex('종이 또 깨질까 봐 모두 정성을 다했다.', None, 'De peur que la cloche ne se brise encore, tous y mirent tout leur cœur.', 'Fearing the bell would crack again, everyone put their whole heart into it.'),
        ex('시험에 떨어질까 봐 걱정이에요.', None, 'J’ai peur d’échouer à l’examen.', 'I’m worried I’ll fail the exam.'),
      ], [
        FB(CHOOSE, '늦을 ＿ 서둘러 나갔어요.', ['까 봐', '세라요', '듯이요'], '까 봐', ('De peur que : -(으)ㄹ까 봐.', 'For fear that: -(으)ㄹ까 봐.'), ('De peur d’être en retard, je suis sorti en vitesse.', 'Afraid of being late, I hurried out.')),
        FB(CHOOSE, '아이가 감기에 ＿ 걱정돼요.', ['걸릴까 봐', '걸리고자', '걸린 나머지'], '걸릴까 봐', ('Inquiétude : -(으)ㄹ까 봐 걱정되다.', 'Worry: -(으)ㄹ까 봐 걱정되다.'), ('J’ai peur que l’enfant n’attrape un rhume.', 'I’m worried the child will catch a cold.')),
        DC(('Ton amie hésite à dire la vérité à son amie.', 'Your friend hesitates to tell her friend the truth.'), [('친구', '사실대로 말하면 친구가 화낼까 봐 무서워요.')], ('Ton amie a peur que son amie se fâche.', 'Your friend is afraid her friend will get angry.'), ['솔직하게 말하는 게 더 나을 거예요.', '화낼까 봐 말하세요.', '화낼세라 기뻐요.'], '솔직하게 말하는 게 더 나을 거예요.', ('On rassure par un conseil.', 'You reassure with advice.')),
        TF('쇠가 녹지 않을까 봐 걱정했다.', ('On craignait que le métal ne fonde pas.', 'They feared the metal wouldn’t melt.'), VRAI, ('녹지 않을까 봐 = de peur qu’il ne fonde pas.', '녹지 않을까 봐 = for fear it wouldn’t melt.')),
      ]),
    L('ko-eulsera', ('De crainte que (littéraire) : -(으)ㄹ세라', 'Lest (literary): -(으)ㄹ세라'), ('Exprimer une crainte délicate, dans un récit ou un poème.', 'Express a delicate fear, in a story or poem.'), 9, [
        ('-(으)ㄹ세라 = de crainte que, de peur que… (littéraire) : 아기가 깰세라 살금살금 걸었다.', '-(으)ㄹ세라 = lest, for fear that… (literary): 아기가 깰세라 살금살금 걸었다.'),
        ('Plus poétique que -(으)ㄹ까 봐 ; souvent avec 행여 (au cas où, par malheur).', 'More poetic than -(으)ㄹ까 봐; often with 행여 (lest, by any chance).'),
      ], [
        G('gram-ko-eulsera', '-(으)ㄹ세라', None, '-(eu)lsera', ('de crainte que (littéraire)', 'lest (literary)')),
        V('ko-josimseureopda', '조심스럽다', None, 'josimseureopda', ('être précautionneux', 'to be cautious, careful')),
        V('ko-salgeumsalgeum', '살금살금', None, 'salgeumsalgeum', ('à pas de loup', 'stealthily, on tiptoe')),
        V('ko-haengyeo', '행여', None, 'haengyeo', ('par malheur, au cas où', 'by any chance (fearing)')),
        V('ko-agi', '아기', None, 'agi', ('bébé', 'baby')),
        V('ko-sumjugida', '숨죽이다', None, 'sumjugida', ('retenir son souffle', 'to hold one’s breath')),
        V('ko-sojunghada', '소중하다', None, 'sojunghada', ('être précieux', 'to be precious')),
      ], [
        ex('어머니는 아기가 깰세라 숨죽이며 방을 나갔다.', None, 'De peur de réveiller le bébé, la mère sortit de la pièce en retenant son souffle.', 'Lest the baby wake, the mother left the room holding her breath.'),
        ex('소중한 편지를 행여 잃어버릴세라 품에 꼭 안았다.', None, 'De crainte de perdre la précieuse lettre, il la serra contre lui.', 'Lest he lose the precious letter, he held it tight to his chest.'),
      ], [
        FB(CHOOSE, '아기가 ＿ 살금살금 걸었다.', ['깰세라', '깨고자', '깬 나머지'], '깰세라', ('Crainte littéraire : -(으)ㄹ세라.', 'Literary fear: -(으)ㄹ세라.'), ('De peur de réveiller le bébé, il marcha à pas de loup.', 'Lest the baby wake, he walked on tiptoe.')),
        FB(CHOOSE, '꽃이 ＿ 조심스럽게 들고 갔다.', ['꺾일세라', '꺾이며', '꺾일 나위'], '꺾일세라', ('-(으)ㄹ세라 + action prudente.', '-(으)ㄹ세라 + careful action.'), ('De crainte que la fleur ne se brise, il la porta avec précaution.', 'Lest the flower snap, he carried it carefully.')),
        SO(('Remets dans l’ordre : « Elle marcha à pas de loup. »', 'Put in order: “She walked on tiptoe.”'), ['그녀는', '살금살금', '걸었다.'], ('Adverbe 살금살금 + verbe.', 'Adverb 살금살금 + verb.')),
        TF('그는 행여 들킬세라 숨죽였다.', ('Il retenait son souffle de peur d’être découvert.', 'He held his breath lest he be discovered.'), VRAI, ('들킬세라 = de peur d’être découvert.', '들킬세라 = lest he be found out.')),
      ]),
    L('ko-ji-aneulkka', ('Il me semble que : -지 않을까 싶다', 'I suspect that: -지 않을까 싶다'), ('Donner un avis avec prudence et modestie.', 'Give an opinion cautiously and modestly.'), 9, [
        ('-지 않을까 싶다 = je me demande si… ne… pas, il me semble que : 조금 쉬는 게 좋지 않을까 싶어요.', '-지 않을까 싶다 = I wonder if… might not, I suspect: 조금 쉬는 게 좋지 않을까 싶어요.'),
        ('Façon très coréenne d’adoucir une opinion, fréquente à l’oral de l’examen et dans les débats.', 'A very Korean way to soften an opinion, common in debates.'),
      ], [
        G('gram-ko-ji-aneulkka', '-지 않을까 싶다', None, '-ji aneulkka sipda', ('il me semble que (avis prudent)', 'I suspect that (cautious opinion)')),
        V('ko-baramjikada', '바람직하다', None, 'baramjikada', ('être souhaitable', 'to be desirable')),
        V('ko-sinjunghada', '신중하다', None, 'sinjunghada', ('être prudent, réfléchi', 'to be careful, prudent')),
        V('ko-jinachida', '지나치다', None, 'jinachida', ('être excessif ; passer devant', 'to be excessive; to pass by')),
        V('ko-murihada', '무리하다', None, 'murihada', ('en faire trop, forcer', 'to overdo it')),
        V('ko-jeokjeolhada', '적절하다', None, 'jeokjeolhada', ('être approprié', 'to be appropriate')),
        V('ko-daean', '대안', None, 'daean', ('alternative, solution de rechange', 'alternative')),
      ], [
        ex('지금 결정하기보다는 조금 더 신중하게 생각하는 게 바람직하지 않을까 싶습니다.', None, 'Plutôt que de décider maintenant, il serait peut-être souhaitable d’y réfléchir encore un peu.', 'Rather than deciding now, it might be better to think about it a little more carefully.'),
        ex('너무 무리하면 건강을 해치지 않을까 싶어요.', None, 'J’ai l’impression qu’à trop forcer, on risque d’abîmer sa santé.', 'I suspect overdoing it may harm your health.'),
      ], [
        FB(CHOOSE, '이 방법보다는 다른 대안을 찾는 게 ＿.', ['낫지 않을까 싶어요', '나을세라요', '나을 나위가 없어요'], '낫지 않을까 싶어요', ('Avis prudent : -지 않을까 싶다.', 'Cautious opinion: -지 않을까 싶다.'), ('Il serait peut-être mieux de chercher une autre solution que cette méthode.', 'I suspect it would be better to look for an alternative to this method.')),
        FB(CHOOSE, '그 표현은 이 자리에 ＿ 싶어요.', ['적절하지 않지 않을까', '적절하지 않을까', '적절할까 봐'], '적절하지 않을까', ('Il me semble que c’est approprié : -지 않을까 싶다.', 'I think it’s appropriate: -지 않을까 싶다.'), ('Il me semble que cette expression convient à l’occasion.', 'I think that expression suits the occasion.')),
        DC(('En réunion, on te demande ton avis sur un projet coûteux.', 'In a meeting you’re asked your opinion on a costly project.'), [('부장님', '이 계획에 대해 어떻게 생각해요?')], ('Ton chef demande ce que tu penses du projet.', 'Your boss asks what you think of the plan.'), ['비용이 좀 지나치지 않을까 싶습니다.', '비용이 지나칠세라 기쁩니다.', '비용이 지나친 바입니다.'], '비용이 좀 지나치지 않을까 싶습니다.', ('Critique adoucie : -지 않을까 싶다.', 'Softened criticism: -지 않을까 싶다.')),
        TF('너무 무리하지 않는 게 좋지 않을까 싶어요.', ('La personne conseille de forcer davantage.', 'The speaker advises pushing harder.'), FAUX, ('무리하지 않는 게 좋다 = mieux vaut ne pas forcer.', '무리하지 않는 게 좋다 = better not to overdo it.')),
      ]),
  ])])

# ═════════════════════════ Île 6 : la flûte ═════════════════════════
W6 = WORLD('topik6-w6', ('La flûte qui apaise les vagues', 'The flute that calms the waves'), REGION,
  ('Circonstances et conséquences : -는 마당에, -(으)ㄴ 나머지, -는 통에.', 'Circumstances and consequences: -는 마당에, -(으)ㄴ 나머지, -는 통에.'),
  (('Manpasikjeok, la flûte des dix mille vagues', 'Manpasikjeok, the Flute of Ten Thousand Waves'), '적', ('Taillée dans un bambou offert par le dragon de la mer de l’Est, cette flûte apaise les tempêtes, guérit les maladies et chasse les ennemis. Elle ne joue que pour qui sait décrire le tumulte et ses conséquences.', 'Carved from bamboo given by the dragon of the Eastern Sea, this flute calms storms, cures illness and drives off enemies. It plays only for those who can describe turmoil and its consequences.')),
  [CH('topik6-w6-c1', ('Dans un tel contexte…', 'In such a situation…'), [
    L('ko-neun-madange', ('Alors que, dans ces circonstances : -는 마당에', 'At a time when: -는 마당에'), ('Juger une action au regard d’une situation critique.', 'Judge an action in light of a critical situation.'), 10, [
        ('-(으)ㄴ/는 마당에 = alors que, dans une telle situation : 나라가 위기에 빠진 마당에 싸울 때가 아니다.', '-(으)ㄴ/는 마당에 = at a time when, in such a situation: 나라가 위기에 빠진 마당에 싸울 때가 아니다.'),
        ('Souvent avec un reproche ou une question rhétorique : 이렇게 된 마당에 무엇을 망설이겠어요?', 'Often with a reproach or rhetorical question: 이렇게 된 마당에 무엇을 망설이겠어요?'),
      ], [
        G('gram-ko-neun-madange', '-(으)ㄴ/는 마당에', None, '-(eu)n / -neun madange', ('alors que, dans ces circonstances', 'at a time when, in such a situation')),
        V('ko-wigi', '위기', None, 'wigi', ('crise', 'crisis')),
        V('ko-jeonjaeng', '전쟁', None, 'jeonjaeng', ('guerre', 'war')),
        V('ko-jeok', '적', None, 'jeok', ('ennemi', 'enemy')),
        V('ko-piri', '피리', None, 'piri', ('flûte', 'flute, pipe')),
        V('ko-pado', '파도', None, 'pado', ('vague', 'wave')),
        V('ko-jamjaeuda', '잠재우다', None, 'jamjaeuda', ('apaiser, calmer', 'to calm, to quell')),
      ], [
        ex('적이 쳐들어오는 마당에 서로 싸울 때가 아닙니다.', None, 'Alors que l’ennemi nous envahit, ce n’est pas le moment de nous disputer.', 'With the enemy invading, this is no time to fight among ourselves.'),
        ex('피리 소리가 거친 파도를 잠재웠다.', None, 'Le son de la flûte apaisa les vagues déchaînées.', 'The sound of the flute calmed the raging waves.'),
      ], [
        FB(CHOOSE, '회사가 어려운 ＿ 휴가를 갈 수는 없지요.', ['마당에', '나머지', '통에'], '마당에', ('Situation critique : -(으)ㄴ 마당에.', 'Critical situation: -(으)ㄴ 마당에.'), ('Alors que l’entreprise est en difficulté, je ne peux pas partir en vacances.', 'With the company struggling, I can’t go on holiday.')),
        FB(CHOOSE, '이미 늦은 ＿ 서두를 필요 없어요.', ['마당에', '나머지', '듯이'], '마당에', ('Puisque la situation est ainsi : -(으)ㄴ 마당에.', 'Given the situation: -(으)ㄴ 마당에.'), ('Puisqu’on est déjà en retard, inutile de se presser.', 'Since we’re already late, there’s no need to hurry.')),
        SO(('Remets dans l’ordre : « La flûte apaisa la tempête. »', 'Put in order: “The flute calmed the storm.”'), ['피리가', '폭풍을', '잠재웠다.'], ('Sujet + objet + 잠재우다.', 'Subject + object + 잠재우다.')),
        TF('나라가 위기에 빠진 마당에 모두 힘을 모았다.', ('Dans la crise, chacun a uni ses forces.', 'In the crisis, everyone joined forces.'), VRAI, ('힘을 모았다 = ont uni leurs forces.', '힘을 모았다 = joined forces.')),
      ]),
    L('ko-eun-nameoji', ('Si… que : -(으)ㄴ 나머지', 'So… that: -(으)ㄴ 나머지'), ('Dire qu’un état excessif a entraîné une conséquence.', 'Say an excessive state led to a consequence.'), 9, [
        ('-(으)ㄴ 나머지 = tellement…, que ; à force de : 너무 긴장한 나머지 실수를 했어요.', '-(으)ㄴ 나머지 = so… that; as a result of being too…: 너무 긴장한 나머지 실수를 했어요.'),
        ('La conséquence est souvent négative et involontaire : 그만 (malgré soi).', 'The consequence is often negative and unintended: 그만 (inadvertently).'),
      ], [
        G('gram-ko-eun-nameoji', '-(으)ㄴ 나머지', None, '-(eu)n nameoji', ('tellement… que, à force de', 'so… that, as a result of')),
        V('ko-ginjanghada', '긴장하다', None, 'ginjanghada', ('être tendu, stressé', 'to be nervous, tense')),
        V('ko-heungbunhada', '흥분하다', None, 'heungbunhada', ('s’exciter, s’emporter', 'to get excited, worked up')),
        V('ko-jichida', '지치다', None, 'jichida', ('être épuisé', 'to be exhausted')),
        V('ko-gijeolhada', '기절하다', None, 'gijeolhada', ('s’évanouir', 'to faint')),
        V('ko-seodureuda', '서두르다', None, 'seodureuda', ('se dépêcher', 'to hurry')),
        V('ko-geuman', '그만', None, 'geuman', ('sans le vouloir, malgré soi ; assez', 'inadvertently; enough')),
      ], [
        ex('너무 긴장한 나머지 그만 대사를 잊어버렸어요.', None, 'J’étais tellement stressé que j’ai oublié mon texte.', 'I was so nervous that I forgot my lines.'),
        ex('서두른 나머지 지갑을 두고 나왔어요.', None, 'Dans ma précipitation, je suis parti sans mon portefeuille.', 'I was in such a rush that I left my wallet behind.'),
      ], [
        FB(CHOOSE, '너무 ＿ 나머지 소리를 질렀어요.', ['흥분한', '흥분하는', '흥분할'], '흥분한', ('Passé : -(으)ㄴ 나머지.', 'Past: -(으)ㄴ 나머지.'), ('J’étais tellement excité que j’ai crié.', 'I got so excited that I shouted.')),
        FB(CHOOSE, '하루 종일 걸어서 ＿ 나머지 바로 잠이 들었어요.', ['지친', '지치는', '지칠'], '지친', ('État excessif → conséquence.', 'Excessive state → consequence.'), ('J’avais tellement marché toute la journée que je me suis endormi aussitôt.', 'I’d walked all day and was so exhausted I fell asleep at once.')),
        SO(('Remets dans l’ordre : « Il s’est évanoui de surprise. »', 'Put in order: “He fainted from shock.”'), ['너무', '놀란', '나머지', '기절했다.'], ('Adverbe + -(으)ㄴ 나머지 + conséquence.', 'Adverb + -(으)ㄴ 나머지 + consequence.')),
        TF('너무 긴장한 나머지 실수를 했어요.', ('La personne a fait une erreur à cause du stress.', 'The speaker made a mistake because of nerves.'), VRAI, ('긴장한 나머지 = tellement stressé que.', '긴장한 나머지 = so nervous that.')),
      ]),
    L('ko-neun-tonge', ('Avec tout ce remue-ménage : -는 통에', 'What with all the commotion: -는 통에'), ('Attribuer un désagrément à une agitation ou un tumulte.', 'Blame an annoyance on commotion or bustle.'), 9, [
        ('-는 통에 = à cause de (agitation, bruit, tumulte) : 옆집이 공사하는 통에 잠을 설쳤어요.', '-는 통에 = because of (bustle, noise, commotion): 옆집이 공사하는 통에 잠을 설쳤어요.'),
        ('Plus familier que -는 바람에 ; insiste sur le chaos de la situation.', 'More colloquial than -는 바람에; stresses the chaos of the situation.'),
      ], [
        G('gram-ko-neun-tonge', '-는 통에', None, '-neun tonge', ('à cause du remue-ménage de', 'what with (the commotion of)')),
        V('ko-sikkeureopda', '시끄럽다', None, 'sikkeureopda', ('être bruyant', 'to be noisy')),
        V('ko-tteodeulda', '떠들다', None, 'tteodeulda', ('faire du bruit, bavarder bruyamment', 'to make noise, to chatter')),
        V('ko-sodong', '소동', None, 'sodong', ('tumulte, remue-ménage', 'commotion, uproar')),
        V('ko-gongsa', '공사', None, 'gongsa', ('travaux', 'construction work')),
        V('ko-seolchida', '설치다', None, 'seolchida', ('mal dormir ; s’agiter', 'to sleep badly; to rush about')),
      ], [
        ex('옆집이 공사하는 통에 밤새 잠을 설쳤어요.', None, 'Avec les travaux chez les voisins, j’ai mal dormi toute la nuit.', 'What with the neighbours’ building work, I slept badly all night.'),
        ex('아이들이 떠드는 통에 전화 소리를 못 들었어요.', None, 'Avec le vacarme des enfants, je n’ai pas entendu le téléphone.', 'With the children making such a racket, I didn’t hear the phone.'),
      ], [
        FB(CHOOSE, '밖이 너무 ＿ 공부를 할 수 없었어요.', ['시끄러운 통에', '시끄러운 마당에요', '시끄러울세라'], '시끄러운 통에', ('Agitation → empêchement : -는 통에.', 'Commotion → hindrance: -는 통에.'), ('Avec tout ce bruit dehors, je n’ai pas pu étudier.', 'What with all the noise outside, I couldn’t study.')),
        FB(CHOOSE, '갑자기 소동이 ＿ 회의가 중단됐어요.', ['벌어지는 통에', '벌어지고자', '벌어질망정'], '벌어지는 통에', ('-는 통에 + conséquence.', '-는 통에 + consequence.'), ('À cause d’un tumulte soudain, la réunion a été interrompue.', 'A sudden commotion broke out, so the meeting was interrupted.')),
        SO(('Remets dans l’ordre : « J’ai mal dormi la nuit dernière. »', 'Put in order: “I slept badly last night.”'), ['어젯밤에', '잠을', '설쳤어요.'], ('잠을 설치다 = mal dormir.', '잠을 설치다 = to sleep badly.')),
        TF('아이들이 떠드는 통에 아기가 깼어요.', ('Le bébé s’est réveillé à cause du bruit des enfants.', 'The baby woke because of the children’s noise.'), VRAI, ('떠드는 통에 = avec le bruit qu’ils faisaient.', '떠드는 통에 = what with their noise.')),
      ]),
  ])])

# ═════════════════════════ Île 7 : Cheoyong ═════════════════════════
W7 = WORLD('topik6-w7', ('La porte de Cheoyong', 'Cheoyong’s gate'), REGION,
  ('Prévoir l’évident : -기 십상이다, -기 일쑤이다, -(으)ㄹ 게 뻔하다.', 'Predicting the obvious: -기 십상이다, -기 일쑤이다, -(으)ㄹ 게 뻔하다.'),
  (('Cheoyong, le fils du dragon', 'Cheoyong, Son of the Dragon'), '처', ('Trouvant l’esprit de la peste chez lui, Cheoyong ne se fâcha pas : il chanta et dansa. Confus, l’esprit promit de ne jamais franchir une porte ornée de son portrait. Il apprécie ceux qui voient venir les choses.', 'Finding the plague spirit in his house, Cheoyong did not get angry: he sang and danced. Ashamed, the spirit promised never to cross a door bearing his portrait. He values those who see things coming.')),
  [CH('topik6-w7-c1', ('C’était couru d’avance', 'It was bound to happen'), [
    L('ko-gi-sipsang', ('Avoir toutes les chances de : -기 십상이다', 'Very likely to: -기 십상이다'), ('Prévenir d’un risque très probable.', 'Warn of a very likely risk.'), 10, [
        ('-기 십상이다 = avoir toutes les chances de (résultat négatif) : 방심하면 감기에 걸리기 십상이에요.', '-기 십상이다 = very likely to (bad outcome): 방심하면 감기에 걸리기 십상이에요.'),
        ('Souvent après une condition -(으)면 : 서두르면 실수하기 십상이다.', 'Often after an -(으)면 condition: 서두르면 실수하기 십상이다.'),
      ], [
        G('gram-ko-gi-sipsang', '-기 십상이다', None, '-gi sipsangida', ('avoir toutes les chances de (négatif)', 'very likely to (negative)')),
        V('ko-yeoksin', '역신', None, 'yeoksin', ('esprit de la peste', 'plague spirit')),
        V('ko-jeonyeombyeong', '전염병', None, 'jeonyeombyeong', ('épidémie, maladie contagieuse', 'epidemic, contagious disease')),
        V('ko-peojida', '퍼지다', None, 'peojida', ('se propager', 'to spread')),
        V('ko-bangsimhada', '방심하다', None, 'bangsimhada', ('relâcher son attention', 'to let one’s guard down')),
        V('ko-geollida', '걸리다', None, 'geollida', ('attraper (une maladie) ; prendre (du temps)', 'to catch (an illness); to take (time)')),
        V('ko-sonhae', '손해', None, 'sonhae', ('perte, préjudice', 'loss, damage')),
      ], [
        ex('겨울에 방심하면 감기에 걸리기 십상이에요.', None, 'En hiver, si on relâche son attention, on a toutes les chances d’attraper un rhume.', 'In winter, if you let your guard down, you’re very likely to catch a cold.'),
        ex('전염병은 손을 잘 씻지 않으면 퍼지기 십상이다.', None, 'Si l’on ne se lave pas bien les mains, une épidémie a toutes les chances de se propager.', 'If people don’t wash their hands properly, an epidemic is very likely to spread.'),
      ], [
        FB(CHOOSE, '서두르면 ＿.', ['실수하기 십상이에요', '실수할세라요', '실수할 나위가 없어요'], '실수하기 십상이에요', ('Risque probable : -기 십상이다.', 'Likely risk: -기 십상이다.'), ('Si on se presse, on a toutes les chances de faire une erreur.', 'If you rush, you’re very likely to make a mistake.')),
        FB(CHOOSE, '확인하지 않고 계약하면 손해를 ＿.', ['보기 십상이다', '본 나머지', '보는 바이다'], '보기 십상이다', ('-기 십상이다.', '-기 십상이다.'), ('Signer sans vérifier, c’est s’exposer à une perte.', 'If you sign without checking, you’re very likely to lose out.')),
        SO(('Remets dans l’ordre : « La maladie s’est propagée dans tout le pays. »', 'Put in order: “The disease spread across the whole country.”'), ['병이', '전국에', '퍼졌다.'], ('Sujet + lieu + 퍼지다.', 'Subject + place + 퍼지다.')),
        TF('방심하면 병에 걸리기 십상이다.', ('Relâcher son attention protège des maladies.', 'Letting your guard down protects you from illness.'), FAUX, ('걸리기 십상이다 = on risque fort de tomber malade.', '걸리기 십상이다 = very likely to fall ill.')),
      ]),
    L('ko-gi-ilssu', ('Avoir souvent tendance à : -기 일쑤이다', 'Tend to (often): -기 일쑤이다'), ('Décrire une mauvaise habitude fréquente.', 'Describe a frequent bad habit.'), 9, [
        ('-기 일쑤이다 = avoir souvent tendance à (négatif) : 그는 약속을 잊어버리기 일쑤예요.', '-기 일쑤이다 = to often (do something bad): 그는 약속을 잊어버리기 일쑤예요.'),
        ('Différence : -기 일쑤이다 décrit une habitude ; -기 십상이다 prédit un risque.', 'Difference: -기 일쑤이다 describes a habit; -기 십상이다 predicts a risk.'),
      ], [
        G('gram-ko-gi-ilssu', '-기 일쑤이다', None, '-gi ilssuida', ('avoir souvent tendance à (négatif)', 'to often (do something bad)')),
        V('ko-deolleongdaeda', '덜렁대다', None, 'deolleongdaeda', ('être étourdi', 'to be careless, scatterbrained')),
        V('ko-ppatteurida', '빠뜨리다', None, 'ppatteurida', ('oublier, omettre ; faire tomber', 'to leave out; to drop')),
        V('ko-kkamppakada', '깜빡하다', None, 'kkamppakada', ('oublier sur le moment', 'to slip one’s mind')),
        V('ko-miruda', '미루다', None, 'miruda', ('remettre à plus tard', 'to put off')),
        V('ko-pinggye', '핑계', None, 'pinggye', ('prétexte, excuse', 'excuse, pretext')),
      ], [
        ex('동생은 덜렁대서 물건을 빠뜨리기 일쑤예요.', None, 'Mon petit frère est étourdi : il oublie souvent ses affaires.', 'My little brother is scatterbrained and often leaves things behind.'),
        ex('그는 핑계를 대며 일을 미루기 일쑤였다.', None, 'Il avait la fâcheuse habitude de remettre les choses à plus tard sous un prétexte.', 'He would often put things off, making excuses.'),
      ], [
        FB(CHOOSE, '아침에 늦잠을 자서 ＿ 일쑤예요.', ['지각하기', '지각하고자', '지각한 바'], '지각하기', ('Mauvaise habitude : -기 일쑤이다.', 'Bad habit: -기 일쑤이다.'), ('Je fais souvent la grasse matinée et j’arrive souvent en retard.', 'I oversleep and am often late.')),
        FB(CHOOSE, '바쁘면 점심을 ＿ 일쑤예요.', ['거르기', '거른', '거를세라'], '거르기', ('-기 일쑤이다.', '-기 일쑤이다.'), ('Quand je suis occupé, il m’arrive souvent de sauter le déjeuner.', 'When I’m busy I often skip lunch.')),
        DC(('Ton collègue a encore oublié le dossier.', 'Your colleague has forgotten the file again.'), [('동료', '아, 또 서류를 깜빡했어요.')], ('Ton collègue a encore oublié le document.', 'Your colleague forgot the document again.'), ['메모해 두면 잊어버리지 않을 거예요.', '깜빡하기 일쑤일 나위가 없어요.', '깜빡할세라 기뻐요.'], '메모해 두면 잊어버리지 않을 거예요.', ('Conseil bienveillant.', 'Kind advice.')),
        TF('그는 일을 미루기 일쑤예요.', ('Il fait toujours tout à l’avance.', 'He always does everything in advance.'), FAUX, ('미루기 일쑤예요 = il remet souvent à plus tard.', '미루기 일쑤예요 = he often puts things off.')),
      ]),
    L('ko-eul-ge-ppeonhada', ('C’est évident : -(으)ㄹ 게 뻔하다', 'It’s obvious: -(으)ㄹ 게 뻔하다'), ('Prédire un résultat évident.', 'Predict an obvious result.'), 9, [
        ('-(으)ㄹ 게 뻔하다 = il est évident que, c’est couru d’avance : 지금 출발하면 늦을 게 뻔해요.', '-(으)ㄹ 게 뻔하다 = it’s obvious that, it’s a foregone conclusion: 지금 출발하면 늦을 게 뻔해요.'),
        ('Proverbe proche : 불 보듯 뻔하다 (évident comme le feu qu’on regarde).', 'Related idiom: 불 보듯 뻔하다 (as obvious as watching a fire).'),
      ], [
        G('gram-ko-eul-ge-ppeonhada', '-(으)ㄹ 게 뻔하다', None, '-(eu)l ge ppeonhada', ('il est évident que', 'it is obvious that')),
        V('ko-gyeolmal', '결말', None, 'gyeolmal', ('dénouement, fin', 'ending, conclusion')),
        V('ko-yesanghada', '예상하다', None, 'yesanghada', ('prévoir', 'to expect, to predict')),
        V('ko-neogeureopda', '너그럽다', None, 'neogeureopda', ('être indulgent, généreux', 'to be generous, tolerant')),
        V('ko-yongseohada', '용서하다', None, 'yongseohada', ('pardonner', 'to forgive')),
        V('ko-mulleonada', '물러나다', None, 'mulleonada', ('se retirer, reculer', 'to withdraw, to step back')),
        V('ko-eolgul', '얼굴', None, 'eolgul', ('visage', 'face')),
      ], [
        ex('처용이 너그럽게 용서하자 역신은 부끄러워 물러났다.', None, 'Quand Cheoyong pardonna avec indulgence, l’esprit de la peste se retira, couvert de honte.', 'When Cheoyong generously forgave him, the plague spirit withdrew in shame.'),
        ex('그 드라마는 결말이 뻔해서 재미없어요.', None, 'Ce feuilleton est sans intérêt : la fin est prévisible.', 'That drama is boring because the ending is predictable.'),
      ], [
        FB(CHOOSE, '지금 출발하면 ＿.', ['늦을 게 뻔해요', '늦기 일쑤일 거예요요', '늦을 나위가 없어요'], '늦을 게 뻔해요', ('Évidence : -(으)ㄹ 게 뻔하다.', 'Obvious result: -(으)ㄹ 게 뻔하다.'), ('Si on part maintenant, c’est sûr qu’on sera en retard.', 'If we leave now, we’ll obviously be late.')),
        FB(CHOOSE, '이렇게 준비를 안 하면 ＿.', ['실패할 게 뻔하다', '실패하는 바이다', '실패할세라'], '실패할 게 뻔하다', ('-(으)ㄹ 게 뻔하다.', '-(으)ㄹ 게 뻔하다.'), ('Sans préparation, l’échec est assuré.', 'Without preparation, failure is a foregone conclusion.')),
        DC(('Ton ami se demande si son frère va encore dormir tard.', 'Your friend wonders if his brother will oversleep again.'), [('친구', '동생이 내일 일찍 일어날까요?')], ('Ton ami demande si son frère se lèvera tôt demain.', 'Your friend asks if his brother will get up early tomorrow.'), ['어제도 늦게 잤으니 또 늦잠을 잘 게 뻔해요.', '늦잠을 자고자 해요.', '늦잠을 잘세라 기뻐요.'], '어제도 늦게 잤으니 또 늦잠을 잘 게 뻔해요.', ('Prédiction évidente : -(으)ㄹ 게 뻔하다.', 'Obvious prediction: -(으)ㄹ 게 뻔하다.')),
        TF('역신은 처용의 너그러움에 놀라 물러났다.', ('L’esprit de la peste s’est retiré devant la générosité de Cheoyong.', 'The plague spirit withdrew before Cheoyong’s generosity.'), VRAI, ('물러났다 = s’est retiré.', '물러났다 = withdrew.')),
      ]),
  ])])

# ═════════════════════════ Île 8 : Dangun ═════════════════════════
W8 = WORLD('topik6-w8', ('Le trône de Dangun', 'Dangun’s throne'), REGION,
  ('Aller au-delà, proverbes et expressions en quatre caractères.', 'Going further, proverbs and four-character idioms.'),
  (('Dangun Wanggeom, le fondateur', 'Dangun Wanggeom, the Founder'), '단', ('Fils de Hwanung et de la femme-ourse, Dangun fonda Gojoseon, le premier royaume coréen. Il garde la sagesse des ancêtres : proverbes et expressions que seuls les maîtres de la langue emploient avec justesse.', 'Son of Hwanung and the bear woman, Dangun founded Gojoseon, the first Korean kingdom. He keeps the wisdom of the ancestors: proverbs and idioms that only masters of the language use correctly.')),
  [CH('topik6-w8-c1', ('La sagesse des ancêtres', 'The wisdom of the ancestors'), [
    L('ko-geuchiji-anko', ('Ne pas s’arrêter à : -는 데 그치지 않고', 'Not stopping at: -는 데 그치지 않고'), ('Montrer qu’une action va au-delà de ce qu’on attend.', 'Show that an action goes beyond what is expected.'), 10, [
        ('-는 데 그치지 않고 = ne pas se contenter de…, aller au-delà : 전통을 지키는 데 그치지 않고 새롭게 발전시켰다.', '-는 데 그치지 않고 = not merely…, going further: 전통을 지키는 데 그치지 않고 새롭게 발전시켰다.'),
        ('Fréquent dans les textes d’analyse et de presse de niveau avancé.', 'Common in advanced analytical and press texts.'),
      ], [
        G('gram-ko-geuchiji-anko', '-는 데 그치지 않고', None, '-neun de geuchiji anko', ('ne pas se contenter de, aller au-delà', 'not merely…, going further')),
        V('ko-jeontong', '전통', None, 'jeontong', ('tradition', 'tradition')),
        V('ko-gyeseunghada', '계승하다', None, 'gyeseunghada', ('perpétuer, hériter', 'to carry on, to inherit')),
        V('ko-baljeonsikida', '발전시키다', None, 'baljeonsikida', ('développer, faire progresser', 'to develop')),
        V('ko-huse', '후세', None, 'huse', ('la postérité', 'future generations')),
        V('ko-gaeguk', '개국', None, 'gaeguk', ('fondation d’un pays', 'founding of a nation')),
        V('ko-gaecheonjeol', '개천절', None, 'gaecheonjeol', ('fête de la Fondation nationale (3 octobre)', 'National Foundation Day (3 October)')),
      ], [
        ex('그들은 전통을 계승하는 데 그치지 않고 새롭게 발전시켰다.', None, 'Ils ne se sont pas contentés de perpétuer la tradition : ils l’ont renouvelée.', 'They did not merely carry on the tradition; they developed it anew.'),
        ex('개천절은 단군이 고조선을 세운 것을 기념하는 날이다.', None, 'Gaecheonjeol commémore la fondation de Gojoseon par Dangun.', 'Gaecheonjeol is the day commemorating Dangun’s founding of Gojoseon.'),
      ], [
        FB(CHOOSE, '그는 문제를 ＿ 해결 방법까지 제시했다.', ['지적하는 데 그치지 않고', '지적한 나머지', '지적할세라'], '지적하는 데 그치지 않고', ('Aller au-delà : -는 데 그치지 않고.', 'Going further: -는 데 그치지 않고.'), ('Il ne s’est pas contenté de signaler le problème : il a aussi proposé une solution.', 'He did not merely point out the problem; he also suggested a solution.')),
        FB(CHOOSE, '이 축제는 전통을 후세에 ＿ 중요한 역할을 한다.', ['전하는 데', '전한 나머지', '전할 게 뻔한'], '전하는 데', ('-는 데 (역할을 하다) : rôle dans…', '-는 데 (역할을 하다): role in…'), ('Ce festival joue un rôle important dans la transmission de la tradition à la postérité.', 'This festival plays an important role in passing tradition on to future generations.')),
        SO(('Remets dans l’ordre : « Dangun fonda Gojoseon. »', 'Put in order: “Dangun founded Gojoseon.”'), ['단군이', '고조선을', '세웠다.'], ('Sujet + objet + 세우다.', 'Subject + object + 세우다.')),
        TF('개천절은 단군의 개국을 기념하는 날이다.', ('Gaecheonjeol célèbre la fondation du pays par Dangun.', 'Gaecheonjeol celebrates Dangun’s founding of the country.'), VRAI, ('개국 = fondation du pays.', '개국 = founding of the nation.')),
      ]),
    L('ko-sokdam', ('Les proverbes (속담)', 'Proverbs (속담)'), ('Comprendre et employer les proverbes coréens les plus courants.', 'Understand and use the most common Korean proverbs.'), 12, [
        ('Les proverbes (속담) sont très présents au TOPIK II : on vous demande souvent lequel convient à une situation.', 'Proverbs (속담) feature heavily in the TOPIK II: you are often asked which one fits a situation.'),
        ('Beaucoup reposent sur des images de la vie paysanne : le bœuf, l’étable, les oiseaux, les souris.', 'Many draw on images of farm life: the ox, the stable, birds, mice.'),
      ], [
        G('gram-ko-sokdam', '속담', None, 'sokdam', ('proverbe', 'proverb')),
        V('ko-sokdam-gameun', '가는 말이 고와야 오는 말이 곱다', None, 'ganeun mari gowaya oneun mari gopda', ('qui parle bien reçoit de bonnes paroles', 'speak kindly and you’ll be spoken to kindly')),
        V('ko-sokdam-natmal', '낮말은 새가 듣고 밤말은 쥐가 듣는다', None, 'nanmareun saega deutgo bammareun jwiga deunneunda', ('les murs ont des oreilles', 'walls have ears')),
        V('ko-sokdam-baekji', '백지장도 맞들면 낫다', None, 'baekjijangdo matdeulmyeon natda', ('l’union fait la force', 'many hands make light work')),
        V('ko-sokdam-haneul', '하늘이 무너져도 솟아날 구멍이 있다', None, 'haneuri muneojyeodo sosanal gumeongi itda', ('il y a toujours une issue', 'there is always a way out')),
        V('ko-sokdam-so', '소 잃고 외양간 고친다', None, 'so ilko oeyanggan gochinda', ('fermer l’écurie quand le cheval s’est enfui', 'to shut the stable door after the horse has bolted')),
      ], [
        ex('백지장도 맞들면 낫다고, 같이 하면 금방 끝날 거예요.', None, 'L’union fait la force : à plusieurs, ce sera vite fini.', 'Many hands make light work: if we do it together, it’ll be done in no time.'),
        ex('사고가 난 후에 안전 점검을 하다니, 소 잃고 외양간 고치는 격이네요.', None, 'Contrôler la sécurité après l’accident : c’est fermer l’écurie après la fuite du cheval.', 'Checking safety after the accident is shutting the stable door after the horse has bolted.'),
      ], [
        FB(CHOOSE, '가는 말이 고와야 ＿.', ['오는 말이 곱다', '외양간 고친다', '솟아날 구멍이 있다'], '오는 말이 곱다', ('Proverbe complet : 가는 말이 고와야 오는 말이 곱다.', 'Full proverb: 가는 말이 고와야 오는 말이 곱다.'), ('Qui parle bien reçoit de bonnes paroles.', 'Speak kindly and you’ll be spoken to kindly.')),
        DC(('Ton ami raconte un secret à voix haute dans un café bondé.', 'Your friend tells a secret loudly in a packed café.'), [('친구', '이건 비밀인데요, 우리 부장님이…')], ('Ton ami commence à révéler un secret sur son chef.', 'Your friend starts revealing a secret about the boss.'), ['쉿! 낮말은 새가 듣고 밤말은 쥐가 들어요.', '소 잃고 외양간 고쳐요.', '백지장도 맞들면 나아요.'], '쉿! 낮말은 새가 듣고 밤말은 쥐가 들어요.', ('Les murs ont des oreilles.', 'Walls have ears.')),
        DC(('Ton amie désespère après un gros échec.', 'Your friend despairs after a big failure.'), [('친구', '이제 아무 방법도 없는 것 같아요.')], ('Ton amie pense qu’il n’y a plus aucune solution.', 'Your friend thinks there’s no way out.'), ['하늘이 무너져도 솟아날 구멍이 있다잖아요.', '소 잃고 외양간 고친다잖아요.', '가는 말이 고와야 해요.'], '하늘이 무너져도 솟아날 구멍이 있다잖아요.', ('Il y a toujours une issue.', 'There is always a way out.')),
        TF('「소 잃고 외양간 고친다」는 미리 준비하는 것을 칭찬하는 말이다.', ('Ce proverbe félicite celui qui se prépare à l’avance.', 'This proverb praises preparing in advance.'), FAUX, ('Il critique celui qui agit trop tard.', 'It criticises acting too late.')),
      ]),
    L('ko-sajaseongeo', ('Expressions en quatre caractères (사자성어)', 'Four-character idioms (사자성어)'), ('Comprendre les expressions sino-coréennes en quatre syllabes.', 'Understand Sino-Korean four-syllable idioms.'), 12, [
        ('Les 사자성어 viennent du chinois classique : quatre syllabes qui résument une idée, comme 일석이조 (une pierre, deux oiseaux).', '사자성어 come from classical Chinese: four syllables summing up an idea, like 일석이조 (one stone, two birds).'),
        ('On les retrouve dans la presse, les discours et les questions de lecture du TOPIK II.', 'They appear in the press, speeches and TOPIK II reading questions.'),
      ], [
        G('gram-ko-sajaseongeo', '사자성어', None, 'sajaseongeo', ('expression en quatre caractères', 'four-character idiom')),
        V('ko-ilseogijo', '일석이조', None, 'ilseogijo', ('faire d’une pierre deux coups', 'to kill two birds with one stone')),
        V('ko-uwangjwawang', '우왕좌왕', None, 'uwangjwawang', ('aller dans tous les sens, s’affoler', 'to run around in confusion')),
        V('ko-dongmunseodap', '동문서답', None, 'dongmunseodap', ('répondre à côté de la question', 'an answer beside the point')),
        V('ko-jaksimsamil', '작심삼일', None, 'jaksimsamil', ('bonnes résolutions sans lendemain', 'resolutions that last three days')),
        V('ko-geumsichomun', '금시초문', None, 'geumsichomun', ('première nouvelle', 'the first one has heard of it')),
        V('ko-jaeopjadeuk', '자업자득', None, 'jaeopjadeuk', ('on récolte ce qu’on a semé', 'you reap what you sow')),
      ], [
        ex('운동도 하고 출퇴근도 하니 자전거 출근은 일석이조예요.', None, 'Aller au travail à vélo, c’est faire d’une pierre deux coups : on fait du sport et on se déplace.', 'Cycling to work kills two birds with one stone: you exercise and commute.'),
        ex('새해 계획이 또 작심삼일로 끝났어요.', None, 'Mes résolutions du Nouvel An n’ont encore tenu que trois jours.', 'My New Year’s resolutions fizzled out after three days again.'),
      ], [
        FB(CHOOSE, '매년 운동을 결심하지만 늘 ＿로 끝나요.', ['작심삼일', '일석이조', '금시초문'], '작심삼일', ('Résolution abandonnée : 작심삼일.', 'Abandoned resolution: 작심삼일.'), ('Chaque année je décide de faire du sport, mais ça ne dure jamais.', 'Every year I resolve to exercise, but it never lasts.')),
        DC(('Un collègue t’annonce une nouvelle que tu ignorais.', 'A colleague tells you news you hadn’t heard.'), [('동료', '김 대리가 다음 달에 회사를 그만둔대요.')], ('Ton collègue dit que M. Kim quitte l’entreprise.', 'Your colleague says Mr Kim is leaving the company.'), ['정말요? 금시초문이에요.', '일석이조네요.', '동문서답이에요.'], '정말요? 금시초문이에요.', ('Première nouvelle : 금시초문.', 'First I’ve heard: 금시초문.')),
        FB(CHOOSE, '갑자기 불이 나자 사람들은 ＿하며 어쩔 줄 몰랐다.', ['우왕좌왕', '자업자득', '일석이조'], '우왕좌왕', ('Courir en tous sens : 우왕좌왕.', 'Running around in confusion: 우왕좌왕.'), ('Quand le feu se déclara, les gens couraient en tous sens sans savoir quoi faire.', 'When the fire broke out, people ran around in confusion.')),
        TF('「자업자득」은 자기가 한 일의 결과를 자기가 받는다는 뜻이다.', ('L’expression signifie qu’on récolte ce qu’on a semé.', 'The idiom means you reap what you sow.'), VRAI, ('자업자득 = on subit les conséquences de ses actes.', '자업자득 = you reap what you sow.')),
      ]),
  ])])

FINAL = {
  'slug': 'topik6-final',
  'title': t(('Simulation TOPIK II — niveau 6', 'TOPIK II simulation — level 6')),
  'region': REGION,
  'description': t(('Dernière épreuve : l’examen blanc au format du TOPIK II (version abrégée) avec les questions les plus difficiles, noté sur 300. Il faut 230 points pour obtenir le niveau 6, le plus haut du TOPIK.', 'Final trial: the mock exam in TOPIK II format (shortened) with the hardest questions, marked out of 300. You need 230 points to reach level 6, the highest TOPIK level.')),
  'exam': 'topik6-official',
  'chapters': [],
}

level = {
  'contentVersion': '2026.11.21',
  'level': {'code': 'TOPIK6', 'title': t(('Maîtrise : la langue des discours, des proverbes et des mythes', 'Mastery: the language of speeches, proverbs and myths')), 'region': REGION, 'order': 11},
  'notice': t(('Les listes de vocabulaire de Koto Quest sont alignées sur les compétences attendues au TOPIK II (niveau 6) mais ne constituent pas des listes officielles du TOPIK.', 'Koto Quest’s vocabulary lists are aligned with the skills expected at TOPIK II (level 6) but are not official TOPIK lists.')),
  'worlds': [W1, W2, W3, W4, W5, W6, W7, W8, FINAL],
}
t((REGION, 'Kingdom of Gojoseon'))
os.makedirs(os.path.join(ROOT, 'content/topik6'), exist_ok=True)
check_and_write(level, 'content/topik6/topik6.json', ['content/n5/n5.json', 'content/n4/n4.json', 'content/n3/n3.json', 'content/n2/n2.json', 'content/n1/n1.json', 'content/topik1/topik1.json', 'content/topik2/topik2.json', 'content/topik3/topik3.json', 'content/topik4/topik4.json', 'content/topik5/topik5.json'])
