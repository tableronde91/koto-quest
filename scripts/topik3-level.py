# Niveau TOPIK 3 (coréen, TOPIK II niveau 3) : 8 îles, 24 leçons et un examen blanc au format du TOPIK II.
# Saga : l'inspecteur royal secret (암행어사) de l'époque Joseon, d'après le récit de Chunhyang.
# Usage : python3 scripts/topik3-level.py   (réécrit content/topik3/topik3.json)
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from kq_content import *

REGION = 'Royaume de Joseon'

# ═════════════════════════ Île 1 : le marché aux rumeurs ═════════════════════════
W1 = WORLD('topik3-w1', ('Le marché aux rumeurs', 'The market of rumours'), REGION,
  ('Rapporter les paroles des autres : discours indirect et formes contractées.', 'Reporting what others say: indirect speech and contracted forms.'),
  (('Le Jangsanbeom imitateur', 'The Mimicking Jangsanbeom'), '산', ('Cette bête au pelage blanc imite la voix des gens pour semer le trouble. Rapporte chaque parole exactement, et elle ne pourra plus tromper personne.', 'This white-furred beast mimics people’s voices to sow confusion. Report every word exactly, and it will no longer fool anyone.')),
  [CH('topik3-w1-c1', ('Il paraît que…', 'Apparently…'), [
    L('ko-dago', ('Il dit que… : -다고 하다', 'He says that…: -다고 하다'), ('Rapporter une affirmation au discours indirect.', 'Report a statement in indirect speech.'), 10, [
        ('Pour rapporter une affirmation, on met la phrase au style neutre puis on ajoute -고 하다 : adjectif + -다고 (바쁘다고 해요), verbe + -ㄴ다고/-는다고 (간다고, 먹는다고), nom + -(이)라고 (학생이라고).', 'To report a statement, put the sentence in the plain style and add -고 하다: adjective + -다고 (바쁘다고 해요), verb + -ㄴ다고/-는다고 (간다고, 먹는다고), noun + -(이)라고 (학생이라고).'),
        ('Au passé : -았/었다고 (갔다고 했어요). Au futur : -(으)ㄹ 거라고 (올 거라고 했어요).', 'In the past: -았/었다고 (갔다고 했어요). In the future: -(으)ㄹ 거라고 (올 거라고 했어요).'),
        ('Les journaux et la télévision rapportent ainsi : 뉴스에서 내일 비가 온다고 했어요.', 'Newspapers and TV report things this way: 뉴스에서 내일 비가 온다고 했어요.'),
      ], [
        G('gram-ko-dago-hada', '-다고 하다', None, '-dago hada', ('rapporter une affirmation (discours indirect)', 'to report a statement (indirect speech)')),
        V('ko-somun', '소문', None, 'somun', ('rumeur', 'rumour')),
        V('ko-nyuseu', '뉴스', None, 'nyuseu', ('actualités, informations', 'news')),
        V('ko-jeonhada', '전하다', None, 'jeonhada', ('transmettre, faire passer', 'to pass on, to convey')),
        V('ko-sasil', '사실', None, 'sasil', ('fait ; en fait', 'fact; in fact')),
        V('ko-sijang', '시장', None, 'sijang', ('marché', 'market')),
        V('ko-sangin', '상인', None, 'sangin', ('marchand', 'merchant')),
      ], [
        ex('뉴스에서 내일 비가 온다고 했어요.', None, 'Aux informations, ils ont dit qu’il pleuvrait demain.', 'The news said it would rain tomorrow.'),
        ex('상인들이 새 원님이 아주 무섭다고 해요.', None, 'Les marchands disent que le nouveau magistrat est très redoutable.', 'The merchants say the new magistrate is very fearsome.'),
      ], [
        FB(CHOOSE, '민지 씨가 오늘 좀 ＿ 했어요.', ['바쁘다고', '바쁜다고', '바빠라고'], '바쁘다고', ('Adjectif : radical + -다고.', 'Adjective: stem + -다고.'), ('Minji a dit qu’elle était un peu occupée aujourd’hui.', 'Minji said she was a bit busy today.')),
        FB(CHOOSE, '친구가 주말에 부산에 ＿ 했어요.', ['간다고', '가다고', '가는다고'], '간다고', ('Verbe après une voyelle : -ㄴ다고.', 'Verb after a vowel: -ㄴ다고.'), ('Mon ami a dit qu’il allait à Busan ce week-end.', 'My friend said he was going to Busan at the weekend.')),
        FB(CHOOSE, '그 사람이 자기가 원님＿ 했어요.', ['이라고', '이다고', '라고는'], '이라고', ('Nom après une consonne : -이라고.', 'Noun after a consonant: -이라고.'), ('Cet homme a dit qu’il était le magistrat.', 'That man said he was the magistrate.')),
        TF('상인이 쌀값이 올랐다고 했어요.', ('Le marchand a dit que le prix du riz avait augmenté.', 'The merchant said the price of rice had gone up.'), VRAI, ('올랐다고 = (il a dit) que c’était monté.', '올랐다고 = (he said) that it had gone up.')),
      ]),
    L('ko-nyago', ('Questions, propositions, ordres rapportés', 'Reported questions, suggestions and orders'), ('Rapporter une question, une proposition, un ordre ou une demande.', 'Report a question, a suggestion, an order or a request.'), 10, [
        ('Question : -냐고 (어디에 가냐고 물었어요). Proposition : -자고 (같이 가자고 했어요). Ordre : -(으)라고 (빨리 오라고 했어요).', 'Question: -냐고 (어디에 가냐고 물었어요). Suggestion: -자고 (같이 가자고 했어요). Order: -(으)라고 (빨리 오라고 했어요).'),
        ('Demande d’un service : -아/어 달라고 (pour soi) ou -아/어 주라고 (pour un autre) : 도와 달라고 부탁했어요.', 'Asking for a favour: -아/어 달라고 (for oneself) or -아/어 주라고 (for someone else): 도와 달라고 부탁했어요.'),
      ], [
        G('gram-ko-nyago-jago', '-냐고 / -자고 / -(으)라고', None, '-nyago / -jago / -(eu)rago', ('rapporter une question, une proposition, un ordre', 'to report a question, a suggestion, an order')),
        V('ko-butakada', '부탁하다', None, 'butakada', ('demander un service', 'to ask a favour')),
        V('ko-jilmun', '질문', None, 'jilmun', ('question', 'question')),
        V('ko-daedapada', '대답하다', None, 'daedapada', ('répondre', 'to answer')),
        V('ko-josahada', '조사하다', None, 'josahada', ('enquêter, examiner', 'to investigate')),
        V('ko-jeungin', '증인', None, 'jeungin', ('témoin', 'witness')),
        V('ko-gwalli', '관리', None, 'gwalli', ('fonctionnaire (de l’État)', 'government official')),
      ], [
        ex('증인이 저에게 어디에서 왔냐고 물었어요.', None, 'Le témoin m’a demandé d’où je venais.', 'The witness asked me where I came from.'),
        ex('관리가 백성들에게 세금을 내라고 했어요.', None, 'Le fonctionnaire a ordonné au peuple de payer l’impôt.', 'The official told the people to pay their taxes.'),
      ], [
        FB(CHOOSE, '친구가 같이 점심을 ＿ 했어요.', ['먹자고', '먹냐고', '먹으라고'], '먹자고', ('Proposition (먹자) : -자고.', 'Suggestion (먹자): -자고.'), ('Mon ami m’a proposé de déjeuner ensemble.', 'My friend suggested having lunch together.')),
        FB(CHOOSE, '선생님이 숙제를 내일까지 ＿ 하셨어요.', ['내라고', '내자고', '내냐고'], '내라고', ('Ordre : -(으)라고.', 'Order: -(으)라고.'), ('Le professeur a dit de rendre les devoirs d’ici demain.', 'The teacher told us to hand in the homework by tomorrow.')),
        FB(CHOOSE, '할머니가 저에게 짐을 좀 들어 ＿ 부탁하셨어요.', ['달라고', '주라고', '주자고'], '달라고', ('Service pour la personne qui parle : -아/어 달라고.', 'Favour for the speaker: -아/어 달라고.'), ('La grand-mère m’a demandé de porter ses bagages.', 'The grandmother asked me to carry her bags.')),
        TF('그 사람이 저에게 이름이 뭐냐고 물었어요.', ('On a demandé son nom à la personne.', 'Someone asked the speaker their name.'), VRAI, ('뭐냐고 물었어요 = on m’a demandé ce que c’était.', '뭐냐고 물었어요 = asked what it was.')),
      ]),
    L('ko-daeyo', ('Il paraît : -대요, -래요', 'Apparently: -대요, -래요'), ('Rapporter une information avec les formes contractées de l’oral.', 'Report information with the contracted spoken forms.'), 9, [
        ('À l’oral, -다고 해요 se contracte en -대요 : 바쁘대요, 간대요, 먹는대요. -(이)라고 해요 devient -(이)래요 : 학생이래요.', 'In speech, -다고 해요 contracts to -대요: 바쁘대요, 간대요, 먹는대요. -(이)라고 해요 becomes -(이)래요: 학생이래요.'),
        ('De même : -냐고 해요 → -냬요, -자고 해요 → -재요, -(으)라고 해요 → -(으)래요 (빨리 오래요).', 'Likewise: -냐고 해요 → -냬요, -자고 해요 → -재요, -(으)라고 해요 → -(으)래요 (빨리 오래요).'),
      ], [
        G('gram-ko-daeyo', '-대요 / -래요', None, '-daeyo / -raeyo', ('il paraît que (forme contractée)', 'apparently, they say (contracted form)')),
        V('ko-baekseong', '백성', None, 'baekseong', ('le peuple (sous l’ancien régime)', 'the common people')),
        V('ko-segeum', '세금', None, 'segeum', ('impôt', 'tax')),
        V('ko-eogulhada', '억울하다', None, 'eogulhada', ('être victime d’une injustice', 'to feel wronged')),
        V('ko-wonnim', '원님', None, 'wonnim', ('magistrat de district', 'district magistrate')),
        V('ko-jinjja', '진짜', None, 'jinjja', ('vraiment ; vrai', 'really; real')),
      ], [
        ex('원님이 세금을 두 배로 올렸대요.', None, 'Il paraît que le magistrat a doublé les impôts.', 'Apparently the magistrate has doubled the taxes.'),
        ex('민수 씨가 내일 같이 가재요.', None, 'Minsu propose qu’on y aille ensemble demain.', 'Minsu suggests we go together tomorrow.'),
      ], [
        FB(CHOOSE, '민지 씨는 오늘 못 ＿.', ['온대요', '오대요', '온래요'], '온대요', ('온다고 해요 → 온대요.', '온다고 해요 → 온대요.'), ('Il paraît que Minji ne peut pas venir aujourd’hui.', 'Apparently Minji can’t come today.')),
        FB(CHOOSE, '저 사람이 새 원님＿.', ['이래요', '이대요', '이재요'], '이래요', ('Nom : -(이)라고 해요 → -(이)래요.', 'Noun: -(이)라고 해요 → -(이)래요.'), ('Il paraît que cet homme est le nouveau magistrat.', 'Apparently that man is the new magistrate.')),
        DC(('Ton collègue revient de chez le chef.', 'Your colleague comes back from the boss’s office.'), [('동료', '부장님이 뭐라고 하셨어요?')], ('Ton collègue te demande ce qu’a dit le chef.', 'Your colleague asks what the boss said.'), ['회의를 세 시에 하재요.', '회의를 세 시에 했어요.', '회의가 세 시예요?'], '회의를 세 시에 하재요.', ('Proposition rapportée : -재요.', 'Reported suggestion: -재요.')),
        TF('백성들이 너무 억울하대요.', ('Le peuple se dit victime d’une injustice.', 'The people say they have been wronged.'), VRAI, ('억울하대요 = ils disent se sentir lésés.', '억울하대요 = they say they feel wronged.')),
      ]),
  ])])

# ═════════════════════════ Île 2 : les ruelles de nuit ═════════════════════════
W2 = WORLD('topik3-w2', ('Les ruelles de Hanyang la nuit', 'The night lanes of Hanyang'), REGION,
  ('Poser le décor, expliquer et rappeler une évidence : -는데, -거든요, -잖아요.', 'Setting the scene, explaining and reminding: -는데, -거든요, -잖아요.'),
  (('L’Eoduksini des ténèbres', 'The Eoduksini of Darkness'), '둑', ('Cette ombre grandit à mesure qu’on la regarde avec peur. Explique calmement ce qui se passe et pourquoi : elle rapetisse jusqu’à disparaître.', 'This shadow grows the more fearfully you look at it. Explain calmly what is happening and why: it shrinks until it vanishes.')),
  [CH('topik3-w2-c1', ('Contexte et explications', 'Context and explanations'), [
    L('ko-neunde', ('Poser le contexte : -는데', 'Setting the scene: -는데'), ('Donner un contexte avant une question ou une proposition, ou opposer deux idées.', 'Give context before a question or suggestion, or contrast two ideas.'), 10, [
        ('-는데 pose le décor avant la phrase principale : 비가 오는데 우산 있어요? (il pleut : tu as un parapluie ?). Verbe : -는데 ; adjectif : -(으)ㄴ데 (추운데) ; nom : -인데 (학생인데).', '-는데 sets the scene before the main clause: 비가 오는데 우산 있어요? (it’s raining: do you have an umbrella?). Verb: -는데; adjective: -(으)ㄴ데 (추운데); noun: -인데 (학생인데).'),
        ('Il exprime aussi un contraste doux : 맛있는데 비싸요 (c’est bon, mais cher).', 'It also expresses a mild contrast: 맛있는데 비싸요 (it’s tasty, but expensive).'),
        ('En fin de phrase, -는데요 laisse la phrase en suspens, poliment : 지금 없는데요… (il n’est pas là, en fait…).', 'At the end of a sentence, -는데요 leaves it politely hanging: 지금 없는데요… (he’s not here, actually…).'),
      ], [
        G('gram-ko-neunde', '-(으)ㄴ/는데', None, '-(eu)n / -neunde', ('mise en contexte ; mais (contraste léger)', 'setting the scene; but (mild contrast)')),
        V('ko-eodupda', '어둡다', None, 'eodupda', ('être sombre', 'to be dark')),
        V('ko-bakda', '밝다', None, 'bakda', ('être clair, lumineux', 'to be bright')),
        V('ko-golmok', '골목', None, 'golmok', ('ruelle', 'alley, lane')),
        V('ko-deungbul', '등불', None, 'deungbul', ('lampe à huile, lanterne', 'oil lamp, lantern light')),
        V('ko-isanghada', '이상하다', None, 'isanghada', ('être bizarre', 'to be strange')),
        V('ko-gapjagi', '갑자기', None, 'gapjagi', ('tout d’un coup', 'all of a sudden')),
      ], [
        ex('골목이 너무 어두운데 등불 좀 켜 주세요.', None, 'La ruelle est trop sombre : allume la lanterne, s’il te plaît.', 'The alley is too dark, please light the lantern.'),
        ex('이 집은 음식은 맛있는데 좀 비싸요.', None, 'Dans ce restaurant, c’est bon, mais un peu cher.', 'The food here is tasty but a bit expensive.'),
      ], [
        FB(CHOOSE, '밖이 ＿ 같이 가 줄까요?', ['어두운데', '어둡는데', '어두워는데'], '어두운데', ('Adjectif en ㅂ : 어둡다 → 어두운데.', 'ㅂ adjective: 어둡다 → 어두운데.'), ('Il fait sombre dehors : tu veux que je t’accompagne ?', 'It’s dark outside, shall I go with you?')),
        FB(CHOOSE, '지금 비가 ＿ 우산 있어요?', ['오는데', '온데', '오은데'], '오는데', ('Verbe : -는데.', 'Verb: -는데.'), ('Il pleut : tu as un parapluie ?', 'It’s raining, do you have an umbrella?')),
        DC(('Au téléphone, quelqu’un demande ton collègue, absent.', 'On the phone, someone asks for your colleague, who is out.'), [('손님', '김 대리님 계세요?')], ('Le client demande si M. Kim est là.', 'The customer asks whether Mr Kim is in.'), ['지금 자리에 안 계시는데요.', '지금 자리에 안 계세요?', '김 대리님이세요.'], '지금 자리에 안 계시는데요.', ('-는데요 adoucit la réponse et laisse la suite ouverte.', '-는데요 softens the answer and leaves room for more.')),
        TF('이 골목은 밝은데 좀 이상해요.', ('La ruelle est sombre.', 'The alley is dark.'), FAUX, ('밝은데 = elle est claire, mais…', '밝은데 = it is bright, but…')),
      ]),
    L('ko-geodeunyo', ('C’est que… : -거든요', 'You see…: -거든요'), ('Donner une explication que l’autre ne connaît pas.', 'Give an explanation the listener doesn’t know.'), 9, [
        ('-거든요 explique une raison que l’interlocuteur ignore : 오늘 못 가요. 약속이 있거든요 (je ne peux pas venir : c’est que j’ai un rendez-vous).', '-거든요 explains a reason the listener doesn’t know: 오늘 못 가요. 약속이 있거든요 (I can’t come today: I have an appointment, you see).'),
        ('Il peut aussi introduire un sujet avant de poursuivre : 어제 시장에 갔거든요. 그런데… (hier je suis allé au marché. Et alors…).', 'It can also bring up a topic before going on: 어제 시장에 갔거든요. 그런데… (I went to the market yesterday, right. And then…).'),
      ], [
        G('gram-ko-geodeunyo', '-거든요', None, '-geodeunyo', ('c’est que… (explication)', 'you see… (explanation)')),
        V('ko-sajeong', '사정', None, 'sajeong', ('circonstances, situation', 'circumstances, situation')),
        V('ko-iyu', '이유', None, 'iyu', ('raison (d’un fait)', 'reason, cause')),
        V('ko-wollae', '원래', None, 'wollae', ('à l’origine, normalement', 'originally, usually')),
        V('ko-honnada', '혼나다', None, 'honnada', ('se faire gronder', 'to get told off')),
        V('ko-jamkkan', '잠깐', None, 'jamkkan', ('un instant', 'a moment')),
      ], [
        ex('오늘은 먼저 갈게요. 집에 일이 있거든요.', None, 'Je pars en avance aujourd’hui : j’ai à faire à la maison.', 'I’ll leave first today. I have something to do at home, you see.'),
        ex('늦으면 안 돼요. 어머니께 혼나거든요.', None, 'Je ne dois pas rentrer tard : sinon je me fais gronder par ma mère.', 'I mustn’t be late. My mother tells me off, you see.'),
      ], [
        FB(CHOOSE, '커피를 안 마셔요. 밤에 잠을 못 ＿.', ['자거든요', '자잖아요', '자는데요'], '자거든요', ('Explication que l’autre ignore : -거든요.', 'Explanation the listener doesn’t know: -거든요.'), ('Je ne bois pas de café : sinon je ne dors pas la nuit.', 'I don’t drink coffee: I can’t sleep at night, you see.')),
        FB(CHOOSE, '어제 못 갔어요. 갑자기 일이 ＿.', ['생겼거든요', '생기거든요요', '생겼잖아서'], '생겼거든요', ('Raison passée : -았/었거든요.', 'Past reason: -았/었거든요.'), ('Je n’ai pas pu venir hier : il y a eu un imprévu.', 'I couldn’t go yesterday: something came up, you see.')),
        DC(('Ton ami s’étonne que tu étudies le soir.', 'Your friend is surprised you study in the evening.'), [('친구', '왜 밤에 공부해요?')], ('Ton ami te demande pourquoi tu étudies la nuit.', 'Your friend asks why you study at night.'), ['낮에는 일을 하거든요.', '낮에 일을 하세요.', '밤에 공부했잖아요.'], '낮에는 일을 하거든요.', ('On donne la raison avec -거든요.', 'You give the reason with -거든요.')),
        TF('잠깐만요. 지갑을 두고 왔거든요.', ('La personne a oublié son portefeuille.', 'The speaker left their wallet behind.'), VRAI, ('두고 왔거든요 = c’est que je l’ai laissé.', '두고 왔거든요 = I left it behind, you see.')),
      ]),
    L('ko-janayo', ('Tu sais bien : -잖아요', 'You know: -잖아요'), ('Rappeler une chose que l’interlocuteur sait déjà.', 'Remind the listener of something they already know.'), 9, [
        ('-잖아요 rappelle une évidence connue des deux : 내일 시험이잖아요 (c’est demain, l’examen, tu le sais bien).', '-잖아요 reminds the listener of something both know: 내일 시험이잖아요 (the exam is tomorrow, you know).'),
        ('Au passé : 아까 말했잖아요 (je te l’ai dit tout à l’heure !). Le ton peut être doux ou un peu agacé.', 'In the past: 아까 말했잖아요 (I told you earlier!). The tone can be gentle or slightly annoyed.'),
      ], [
        G('gram-ko-janayo', '-잖아요', None, '-janayo', ('tu sais bien que…', 'you know…, as you know')),
        V('ko-dangyeonhada', '당연하다', None, 'dangyeonhada', ('être évident, normal', 'to be natural, obvious')),
        V('ko-akka', '아까', None, 'akka', ('tout à l’heure (passé)', 'a moment ago')),
        V('ko-beolsseo', '벌써', None, 'beolsseo', ('déjà', 'already')),
        V('ko-malhada', '말하다', None, 'malhada', ('dire, parler', 'to say, to speak')),
        V('ko-gieokada', '기억하다', None, 'gieokada', ('se souvenir', 'to remember')),
        V('ko-ijeobeorida', '잊어버리다', None, 'ijeobeorida', ('oublier', 'to forget')),
      ], [
        ex('아까 말했잖아요. 오늘은 시장이 일찍 닫아요.', None, 'Je te l’ai dit tout à l’heure : aujourd’hui, le marché ferme tôt.', 'I told you earlier. The market closes early today.'),
        ex('당연하잖아요. 친구니까요.', None, 'C’est normal, voyons : on est amis.', 'Of course, we’re friends.'),
      ], [
        FB(CHOOSE, '우산을 가져가세요. 오늘 비가 ＿.', ['오잖아요', '오거든요요', '왔잖아서'], '오잖아요', ('Fait connu des deux (la météo du jour) : -잖아요.', 'Fact both know (today’s weather): -잖아요.'), ('Prends un parapluie : il pleut aujourd’hui, tu le sais bien.', 'Take an umbrella. It’s raining today, you know.')),
        FB(CHOOSE, '아까 제가 ＿. 기억 안 나요?', ['말했잖아요', '말하잖았어요', '말했거든서'], '말했잖아요', ('Passé + -잖아요 : 말했잖아요.', 'Past + -잖아요: 말했잖아요.'), ('Je te l’ai dit tout à l’heure. Tu ne t’en souviens pas ?', 'I told you earlier. Don’t you remember?')),
        DC(('Ton ami a oublié l’anniversaire de sa mère.', 'Your friend forgot his mother’s birthday.'), [('친구', '어? 오늘이 어머니 생신이에요?')], ('Ton ami s’étonne que ce soit l’anniversaire de sa mère.', 'Your friend is surprised it is his mother’s birthday.'), ['네, 어제 말했잖아요.', '네, 어제 말했거든요?', '네, 생신이세요.'], '네, 어제 말했잖아요.', ('On rappelle ce qui a déjà été dit : -잖아요.', 'You remind him of what was already said: -잖아요.')),
        TF('벌써 잊어버렸어요? 어제 같이 갔잖아요.', ('La personne rappelle qu’ils y sont allés ensemble hier.', 'The speaker reminds the other that they went together yesterday.'), VRAI, ('같이 갔잖아요 = on y est allés ensemble, tu te souviens.', '같이 갔잖아요 = we went together, remember.')),
      ]),
  ])])

# ═════════════════════════ Île 3 : le grand arbre du village ═════════════════════════
W3 = WORLD('topik3-w3', ('La forêt de bambous de Damyang', 'The bamboo forest of Damyang'), REGION,
  ('Raconter un changement : -게 되다, -아/어지다 et faire faire : -게 하다.', 'Telling about change: -게 되다, -아/어지다, and making someone do something: -게 하다.'),
  (('Le Grand Arbre du village', 'The Great Village Tree'), '당', ('Ce vieil arbre sacré, ceint de cordes et de rubans, a vu changer des générations. Raconte-lui comment les choses ont évolué, et il te livrera ses souvenirs.', 'This old sacred tree, tied with ropes and ribbons, has watched generations change. Tell it how things have evolved, and it will share its memories.')),
  [CH('topik3-w3-c1', ('Ce qui change', 'What changes'), [
    L('ko-ge-doeda', ('Finir par : -게 되다', 'Coming to: -게 되다'), ('Dire qu’une situation est arrivée sans qu’on l’ait vraiment décidé.', 'Say a situation came about without being really decided.'), 9, [
        ('Radical + -게 되다 = finir par, en venir à : 한국에서 살게 됐어요 (je me suis retrouvé à vivre en Corée).', 'Stem + -게 되다 = to end up, to come to: 한국에서 살게 됐어요 (I ended up living in Korea).'),
        ('Il sert aussi aux décisions prises par d’autres ou par les circonstances : 다음 달에 서울로 가게 됐어요 (je vais être muté à Séoul).', 'It is also used for decisions made by others or by circumstances: 다음 달에 서울로 가게 됐어요 (I’m being sent to Seoul next month).'),
      ], [
        G('gram-ko-ge-doeda', '-게 되다', None, '-ge doeda', ('finir par, en venir à', 'to end up, to come to')),
        V('ko-najunge', '나중에', None, 'najunge', ('plus tard', 'later')),
        V('ko-gyeolguk', '결국', None, 'gyeolguk', ('finalement, au bout du compte', 'in the end, eventually')),
        V('ko-uyeonhi', '우연히', None, 'uyeonhi', ('par hasard', 'by chance')),
        V('ko-daenamu', '대나무', None, 'daenamu', ('bambou', 'bamboo')),
        V('ko-salda', '살다', None, 'salda', ('vivre, habiter', 'to live')),
      ], [
        ex('우연히 그 사람을 만나서 친하게 지내게 됐어요.', None, 'Je l’ai rencontré par hasard, et nous avons fini par devenir proches.', 'I met him by chance and we ended up becoming close.'),
        ex('결국 이 마을에서 살게 됐어요.', None, 'Finalement, je me suis retrouvé à vivre dans ce village.', 'In the end I came to live in this village.'),
      ], [
        FB(CHOOSE, '회사 일 때문에 부산에서 ＿ 됐어요.', ['살게', '살아', '사는'], '살게', ('Situation venue des circonstances : -게 되다.', 'Situation brought about by circumstances: -게 되다.'), ('À cause du travail, je me suis retrouvé à vivre à Busan.', 'Because of work, I ended up living in Busan.')),
        FB(CHOOSE, '한국 드라마를 보고 한국어를 ＿ 되었어요.', ['좋아하게', '좋아해서', '좋아하는'], '좋아하게', ('Changement progressif : -게 되다.', 'Gradual change: -게 되다.'), ('En regardant des dramas, j’en suis venu à aimer le coréen.', 'Watching Korean dramas, I came to love Korean.')),
        SO(('Remets dans l’ordre : « Finalement, je n’ai pas pu y aller. »', 'Put in order: “In the end, I couldn’t go.”'), ['결국', '못', '가게', '됐어요.'], ('Adverbe + 못 + verbe-게 됐어요.', 'Adverb + 못 + verb-게 됐어요.')),
        TF('나중에 그 이유를 알게 됐어요.', ('La personne a compris la raison plus tard.', 'The speaker found out the reason later.'), VRAI, ('알게 됐어요 = j’ai fini par savoir.', '알게 됐어요 = I came to know.')),
      ]),
    L('ko-eojida', ('Devenir : -아/어지다', 'Becoming: -아/어지다'), ('Décrire un changement d’état avec un adjectif.', 'Describe a change of state with an adjective.'), 9, [
        ('Adjectif + -아/어지다 = devenir : 따뜻하다 → 따뜻해지다 (se réchauffer), 예쁘다 → 예뻐지다 (embellir).', 'Adjective + -아/어지다 = to become: 따뜻하다 → 따뜻해지다 (to get warmer), 예쁘다 → 예뻐지다 (to get prettier).'),
        ('On l’associe souvent à 점점 (de plus en plus) : 날씨가 점점 추워져요.', 'It often goes with 점점 (more and more): 날씨가 점점 추워져요.'),
      ], [
        G('gram-ko-eojida', '-아/어지다', None, '-a / -eojida', ('devenir (changement d’état)', 'to become (change of state)')),
        V('ko-ttatteuthada', '따뜻하다', None, 'ttatteuthada', ('être chaud, doux (agréable)', 'to be warm')),
        V('ko-siwonhada', '시원하다', None, 'siwonhada', ('être frais (agréable)', 'to be cool, refreshing')),
        V('ko-geongang', '건강', None, 'geongang', ('santé', 'health')),
        V('ko-byeonhada', '변하다', None, 'byeonhada', ('changer', 'to change')),
        V('ko-jeomjeom', '점점', None, 'jeomjeom', ('de plus en plus, peu à peu', 'gradually, more and more')),
        V('ko-yeppeuda', '예쁘다', None, 'yeppeuda', ('être joli', 'to be pretty')),
      ], [
        ex('봄이 되니까 날씨가 점점 따뜻해져요.', None, 'Avec le printemps, il fait de plus en plus doux.', 'Now spring has come, the weather is getting warmer.'),
        ex('대나무 숲에 들어가니까 시원해졌어요.', None, 'En entrant dans la forêt de bambous, il a fait plus frais.', 'When we went into the bamboo forest, it got cooler.'),
      ], [
        FB(CHOOSE, '겨울이 되니까 날씨가 점점 ＿.', ['추워져요', '춥어져요', '추워지어요'], '추워져요', ('춥다 → 추워 + 지다 → 추워져요.', '춥다 → 추워 + 지다 → 추워져요.'), ('Avec l’hiver, il fait de plus en plus froid.', 'Now winter is here, it’s getting colder and colder.')),
        FB(CHOOSE, '운동을 시작한 후에 ＿.', ['건강해졌어요', '건강하게 했어요', '건강해 있어요'], '건강해졌어요', ('Changement d’état : -아/어졌어요.', 'Change of state: -아/어졌어요.'), ('Depuis que je fais du sport, je suis en meilleure santé.', 'Since I started exercising, I’ve become healthier.')),
        DC(('Tu revois une amie après des années.', 'You see a friend again after years.'), [('친구', '오랜만이에요! 저 많이 변했지요?')], ('Ton amie te demande si elle a beaucoup changé.', 'Your friend asks if she has changed a lot.'), ['네, 더 예뻐졌어요.', '네, 더 예쁘게 됐어요요.', '아니요, 예뻐요?'], '네, 더 예뻐졌어요.', ('예쁘다 → 예뻐지다.', '예쁘다 → 예뻐지다.')),
        TF('마을이 옛날보다 조용해졌어요.', ('Le village est devenu plus bruyant qu’avant.', 'The village has become noisier than before.'), FAUX, ('조용해졌어요 = est devenu calme.', '조용해졌어요 = has become quiet.')),
      ]),
    L('ko-ge-hada', ('Faire faire : -게 하다', 'Making someone do: -게 하다'), ('Dire qu’on fait faire ou qu’on laisse faire quelque chose à quelqu’un.', 'Say you make or let someone do something.'), 9, [
        ('Radical + -게 하다 = faire faire, laisser faire : 아이에게 숙제를 하게 했어요 (j’ai fait faire ses devoirs à l’enfant).', 'Stem + -게 하다 = to make or let someone do: 아이에게 숙제를 하게 했어요 (I made the child do his homework).'),
        ('Avec un adjectif : 사람을 기쁘게 하다 (rendre quelqu’un heureux), 걱정하게 하다 (inquiéter).', 'With an adjective: 사람을 기쁘게 하다 (to make someone happy), 걱정하게 하다 (to worry someone).'),
      ], [
        G('gram-ko-ge-hada', '-게 하다', None, '-ge hada', ('faire faire, laisser faire', 'to make or let (someone) do')),
        V('ko-namu', '나무', None, 'namu', ('arbre ; bois', 'tree; wood')),
        V('ko-jikida', '지키다', None, 'jikida', ('protéger, garder ; respecter', 'to protect, to guard; to keep')),
        V('ko-gidohada', '기도하다', None, 'gidohada', ('prier', 'to pray')),
        V('ko-sowon', '소원', None, 'sowon', ('vœu, souhait', 'wish')),
        V('ko-bilda', '빌다', None, 'bilda', ('faire un vœu, implorer', 'to make a wish, to beg')),
        V('ko-ai', '아이', None, 'ai', ('enfant', 'child')),
      ], [
        ex('할머니는 아이들에게 나무에 소원을 빌게 하셨어요.', None, 'La grand-mère a fait faire un vœu aux enfants devant l’arbre.', 'Grandmother had the children make a wish at the tree.'),
        ex('늦게 와서 어머니를 걱정하게 했어요.', None, 'Je suis rentré tard et j’ai inquiété ma mère.', 'I came home late and made my mother worry.'),
      ], [
        FB(CHOOSE, '선생님이 학생들에게 책을 ＿ 하셨어요.', ['읽게', '읽어', '읽기'], '읽게', ('Faire faire : radical + -게 하다.', 'Make someone do: stem + -게 하다.'), ('Le professeur a fait lire le livre aux élèves.', 'The teacher had the students read the book.')),
        FB(CHOOSE, '그 소식이 저를 아주 ＿ 했어요.', ['기쁘게', '기뻐서', '기쁜'], '기쁘게', ('Adjectif + -게 하다 : rendre…', 'Adjective + -게 하다: to make (someone) …'), ('Cette nouvelle m’a rendu très heureux.', 'That news made me very happy.')),
        SO(('Remets dans l’ordre : « Ma mère m’a fait ranger ma chambre. »', 'Put in order: “My mother made me tidy my room.”'), ['어머니가', '저에게', '방을', '청소하게', '하셨어요.'], ('Sujet + personne-에게 + objet + verbe-게 하다.', 'Subject + person-에게 + object + verb-게 하다.')),
        TF('마을 사람들은 이 나무가 마을을 지킨다고 믿어요.', ('Les villageois croient que l’arbre protège le village.', 'The villagers believe the tree protects the village.'), VRAI, ('지킨다고 믿어요 = ils croient qu’il protège.', '지킨다고 믿어요 = they believe it protects.')),
      ]),
  ])])

# ═════════════════════════ Île 4 : le tumulus du cheval céleste ═════════════════════════
W4 = WORLD('topik3-w4', ('Le tumulus du cheval céleste', 'The tomb of the heavenly horse'), REGION,
  ('Exprimer un but : -기 위해서, -도록, -(으)려면.', 'Expressing a purpose: -기 위해서, -도록, -(으)려면.'),
  (('Le Cheval céleste', 'The Heavenly Horse'), '천', ('Peint sur une selle de bouleau il y a quinze siècles, ce cheval ailé ne porte que les cavaliers qui savent où ils vont et pourquoi.', 'Painted on a birch-bark saddle flap fifteen centuries ago, this winged horse carries only riders who know where they are going and why.')),
  [CH('topik3-w4-c1', ('Dans quel but ?', 'For what purpose?'), [
    L('ko-gi-wihae', ('Pour, afin de : -기 위해서', 'In order to: -기 위해서'), ('Exprimer un but avec -기 위해서 et 을/를 위해서.', 'Express a purpose with -기 위해서 and 을/를 위해서.'), 9, [
        ('Verbe + -기 위해서 = pour, afin de : 시험에 합격하기 위해서 열심히 공부해요. Plus soutenu que -(으)려고.', 'Verb + -기 위해서 = in order to: 시험에 합격하기 위해서 열심히 공부해요. More formal than -(으)려고.'),
        ('Nom + 을/를 위해서 = pour (quelqu’un, quelque chose) : 가족을 위해서 일해요.', 'Noun + 을/를 위해서 = for (someone, something): 가족을 위해서 일해요.'),
      ], [
        G('gram-ko-gi-wihae', '-기 위해(서)', None, '-gi wihae(seo)', ('pour, afin de', 'in order to')),
        V('ko-mokpyo', '목표', None, 'mokpyo', ('objectif, but', 'goal, target')),
        V('ko-noryeokada', '노력하다', None, 'noryeokada', ('faire des efforts', 'to make an effort')),
        V('ko-kkum', '꿈', None, 'kkum', ('rêve', 'dream')),
        V('ko-iruda', '이루다', None, 'iruda', ('réaliser, accomplir', 'to achieve, to fulfil')),
        V('ko-seonggonghada', '성공하다', None, 'seonggonghada', ('réussir', 'to succeed')),
        V('ko-cheonma', '천마', None, 'cheonma', ('cheval céleste', 'heavenly horse')),
      ], [
        ex('꿈을 이루기 위해서 매일 노력하고 있어요.', None, 'Je fais des efforts tous les jours pour réaliser mon rêve.', 'I make an effort every day to achieve my dream.'),
        ex('부모님은 우리를 위해서 열심히 일하셨어요.', None, 'Nos parents ont travaillé dur pour nous.', 'Our parents worked hard for us.'),
      ], [
        FB(CHOOSE, '토픽 시험에 합격하＿ 매일 공부해요.', ['기 위해서', '도록 해서', '려면서'], '기 위해서', ('But : -기 위해서.', 'Purpose: -기 위해서.'), ('J’étudie tous les jours pour réussir le TOPIK.', 'I study every day to pass the TOPIK.')),
        PC(CHOOSE, '가족＿ 위해서 요리를 했어요.', ['을', '이', '에'], '을', ('Nom + 을/를 위해서.', 'Noun + 을/를 위해서.'), ('J’ai cuisiné pour ma famille.', 'I cooked for my family.')),
        SO(('Remets dans l’ordre : « Pour réussir, il faut faire des efforts. »', 'Put in order: “To succeed, you have to make an effort.”'), ['성공하기', '위해서', '노력해야', '해요.'], ('But -기 위해서 + obligation -아야 해요.', 'Purpose -기 위해서 + obligation -아야 해요.')),
        TF('목표를 이루기 위해서 한국에 왔어요.', ('La personne est venue en Corée pour atteindre son objectif.', 'The speaker came to Korea to reach a goal.'), VRAI, ('이루기 위해서 = pour accomplir.', '이루기 위해서 = in order to achieve.')),
      ]),
    L('ko-dorok', ('Pour que : -도록', 'So that: -도록'), ('Dire ce qu’on fait pour qu’une chose arrive (ou n’arrive pas).', 'Say what you do so that something happens (or doesn’t).'), 9, [
        ('-도록 = pour que, de façon à : 뒤에 있는 사람도 들리도록 크게 말하세요 (parlez fort pour que les gens du fond entendent aussi).', '-도록 = so that: 뒤에 있는 사람도 들리도록 크게 말하세요 (speak loudly so that people at the back can hear too).'),
        ('-지 않도록 = pour éviter que : 감기에 걸리지 않도록 조심하세요. -도록 하세요 = veillez à… : 일찍 오도록 하세요.', '-지 않도록 = so as not to: 감기에 걸리지 않도록 조심하세요. -도록 하세요 = make sure you…: 일찍 오도록 하세요.'),
      ], [
        G('gram-ko-dorok', '-도록', None, '-dorok', ('pour que, de façon à', 'so that')),
        V('ko-keuge', '크게', None, 'keuge', ('fort, en grand', 'loudly, big')),
        V('ko-jasehi', '자세히', None, 'jasehi', ('en détail', 'in detail')),
        V('ko-seolmyeonghada', '설명하다', None, 'seolmyeonghada', ('expliquer', 'to explain')),
        V('ko-modu', '모두', None, 'modu', ('tous, tout le monde', 'all, everyone')),
        V('ko-ihaehada', '이해하다', None, 'ihaehada', ('comprendre', 'to understand')),
        V('ko-memohada', '메모하다', None, 'memohada', ('prendre des notes', 'to take notes')),
      ], [
        ex('모두 이해할 수 있도록 자세히 설명해 주세요.', None, 'Expliquez en détail, pour que tout le monde puisse comprendre.', 'Please explain in detail so that everyone can understand.'),
        ex('잊어버리지 않도록 메모해 두세요.', None, 'Prends-en note pour ne pas oublier.', 'Write it down so you don’t forget.'),
      ], [
        FB(CHOOSE, '뒤에서도 ＿ 크게 말해 주세요.', ['들리도록', '들리기 위해서', '들리려면'], '들리도록', ('Pour que (sujet différent, ici le son) : -도록.', 'So that (different subject, here the sound): -도록.'), ('Parlez fort pour qu’on entende aussi au fond.', 'Please speak loudly so it can be heard at the back too.')),
        FB(CHOOSE, '감기에 걸리지 ＿ 따뜻하게 입으세요.', ['않도록', '않으려고', '않기 위해'], '않도록', ('Pour éviter que : -지 않도록.', 'So as not to: -지 않도록.'), ('Habille-toi chaudement pour ne pas attraper froid.', 'Dress warmly so you don’t catch a cold.')),
        DC(('Le professeur donne une consigne pour demain.', 'The teacher gives an instruction for tomorrow.'), [('선생님', '내일은 아홉 시까지 오도록 하세요.')], ('Le professeur demande d’arriver pour 9 h.', 'The teacher asks you to arrive by nine.'), ['네, 늦지 않도록 할게요.', '네, 늦도록 할게요.', '네, 아홉 시였어요.'], '네, 늦지 않도록 할게요.', ('-지 않도록 할게요 = je ferai en sorte de ne pas…', '-지 않도록 할게요 = I’ll make sure not to…')),
        TF('잊어버리지 않도록 메모했어요.', ('La personne a pris des notes pour ne pas oublier.', 'The speaker took notes so as not to forget.'), VRAI, ('잊어버리지 않도록 = pour ne pas oublier.', '잊어버리지 않도록 = so as not to forget.')),
      ]),
    L('ko-ryeomyeon', ('Si l’on veut… : -(으)려면', 'If you want to…: -(으)려면'), ('Dire ce qu’il faut faire pour obtenir quelque chose.', 'Say what you must do to get something.'), 9, [
        ('-(으)려면 = si l’on veut, pour : 박물관에 가려면 지하철을 타세요. Souvent suivi de -아/어야 해요 ou 필요해요.', '-(으)려면 = if you want to, to: 박물관에 가려면 지하철을 타세요. Often followed by -아/어야 해요 or 필요해요.'),
        ('-으려면 après une consonne (먹으려면), -려면 après une voyelle ou ㄹ (가려면, 만들려면).', '-으려면 after a consonant (먹으려면), -려면 after a vowel or ㄹ (가려면, 만들려면).'),
      ], [
        G('gram-ko-ryeomyeon', '-(으)려면', None, '-(eu)ryeomyeon', ('si l’on veut…, pour…', 'if you want to…, to…')),
        V('ko-piryohada', '필요하다', None, 'piryohada', ('être nécessaire', 'to be necessary, to need')),
        V('ko-yeyakada', '예약하다', None, 'yeyakada', ('réserver', 'to book, to reserve')),
        V('ko-miri', '미리', None, 'miri', ('à l’avance', 'in advance')),
        V('ko-pyo', '표', None, 'pyo', ('billet, ticket ; tableau', 'ticket; table, chart')),
        V('ko-bangmulgwan', '박물관', None, 'bangmulgwan', ('musée', 'museum')),
        V('ko-sincheonghada', '신청하다', None, 'sincheonghada', ('s’inscrire, faire une demande', 'to apply, to sign up')),
      ], [
        ex('천마총에 들어가려면 표가 필요해요.', None, 'Pour entrer dans le tumulus du cheval céleste, il faut un billet.', 'You need a ticket to go into the Heavenly Horse Tomb.'),
        ex('주말에 가려면 미리 예약해야 해요.', None, 'Si tu veux y aller le week-end, il faut réserver à l’avance.', 'If you want to go at the weekend, you have to book in advance.'),
      ], [
        FB(CHOOSE, '박물관에 ＿ 몇 번 버스를 타야 해요?', ['가려면', '가기 위해서는요', '가도록'], '가려면', ('Pour aller (condition-but) : -(으)려면.', 'To get there (purpose-condition): -(으)려면.'), ('Pour aller au musée, quel bus faut-il prendre ?', 'Which bus do I take to get to the museum?')),
        FB(CHOOSE, '이 수업을 ＿ 오늘까지 신청하세요.', ['들으려면', '듣으려면', '들려면'], '들으려면', ('듣다 (ㄷ irrégulier) → 들으려면.', '듣다 (irregular ㄷ) → 들으려면.'), ('Si vous voulez suivre ce cours, inscrivez-vous aujourd’hui.', 'If you want to take this class, sign up by today.')),
        DC(('Un touriste veut voir le spectacle du soir.', 'A tourist wants to see the evening show.'), [('관광객', '저녁 공연을 보고 싶은데요.')], ('Le touriste dit qu’il veut voir le spectacle du soir.', 'The tourist says he wants to see the evening show.'), ['보시려면 미리 예약하셔야 해요.', '보셨으면 예약하세요.', '공연을 봤어요.'], '보시려면 미리 예약하셔야 해요.', ('-(으)려면 + obligation.', '-(으)려면 + obligation.')),
        TF('표를 사려면 신분증이 필요해요.', ('Il faut une pièce d’identité pour acheter un billet.', 'You need ID to buy a ticket.'), VRAI, ('사려면 … 필요해요 = pour acheter, il faut…', '사려면 … 필요해요 = to buy, you need…')),
      ]),
  ])])

# ═════════════════════════ Île 5 : le jardin secret ═════════════════════════
W5 = WORLD('topik3-w5', ('Le jardin secret du palais', 'The palace’s secret garden'), REGION,
  ('Exprimer le degré et la manière : -(으)ㄹ 정도로, -(으)ㄴ/는 대로, 처럼 et 만큼.', 'Expressing degree and manner: -(으)ㄹ 정도로, -(으)ㄴ/는 대로, 처럼 and 만큼.'),
  (('Le Cerf de longévité', 'The Deer of Longevity'), '록', ('Parmi les dix symboles de longue vie, ce cerf aux bois de corail garde le jardin secret. Décris la beauté du lieu avec justesse : ni trop, ni trop peu.', 'Among the ten symbols of long life, this coral-antlered deer guards the secret garden. Describe the beauty of the place just right: neither too much nor too little.')),
  [CH('topik3-w5-c1', ('À quel point ?', 'How much?'), [
    L('ko-jeongdo', ('Au point de : -(으)ㄹ 정도로', 'So much that: -(으)ㄹ 정도로'), ('Exprimer l’intensité par une conséquence.', 'Express intensity through a consequence.'), 9, [
        ('-(으)ㄹ 정도로 = au point de : 눈물이 날 정도로 아름다워요 (c’est beau à en pleurer).', '-(으)ㄹ 정도로 = so much that: 눈물이 날 정도로 아름다워요 (it’s so beautiful it brings tears).'),
        ('En fin de phrase : -(으)ㄹ 정도예요 (숨을 못 쉴 정도예요). Nom + 정도 = environ : 한 시간 정도.', 'At the end of a sentence: -(으)ㄹ 정도예요 (숨을 못 쉴 정도예요). Noun + 정도 = about: 한 시간 정도.'),
      ], [
        G('gram-ko-eul-jeongdo', '-(으)ㄹ 정도로', None, '-(eu)l jeongdoro', ('au point de', 'so much that, to the point of')),
        V('ko-areumdapda', '아름답다', None, 'areumdapda', ('être beau', 'to be beautiful')),
        V('ko-nollada', '놀라다', None, 'nollada', ('être surpris', 'to be surprised')),
        V('ko-gamdonghada', '감동하다', None, 'gamdonghada', ('être ému', 'to be moved')),
        V('ko-nunmul', '눈물', None, 'nunmul', ('larme', 'tear (crying)')),
        V('ko-sum', '숨', None, 'sum', ('souffle, respiration', 'breath')),
        V('ko-jeongwon', '정원', None, 'jeongwon', ('jardin', 'garden')),
      ], [
        ex('정원이 눈물이 날 정도로 아름다웠어요.', None, 'Le jardin était beau à en pleurer.', 'The garden was so beautiful it brought tears to my eyes.'),
        ex('숨을 못 쉴 정도로 웃었어요.', None, 'J’ai ri à en perdre le souffle.', 'I laughed so hard I couldn’t breathe.'),
      ], [
        FB(CHOOSE, '배가 터질 ＿ 많이 먹었어요.', ['정도로', '만큼요', '대로'], '정도로', ('Au point de : -(으)ㄹ 정도로.', 'So much that: -(으)ㄹ 정도로.'), ('J’ai mangé à en exploser.', 'I ate so much I could burst.')),
        FB(CHOOSE, '깜짝 ＿ 정도로 큰 소리가 났어요.', ['놀랄', '놀란', '놀라는'], '놀랄', ('Devant 정도 : -(으)ㄹ.', 'Before 정도: -(으)ㄹ.'), ('Il y a eu un bruit si fort que j’ai sursauté.', 'There was a noise so loud it made me jump.')),
        SO(('Remets dans l’ordre : « C’était émouvant au point de pleurer. »', 'Put in order: “It was moving enough to make me cry.”'), ['눈물이', '날', '정도로', '감동했어요.'], ('Conséquence -(으)ㄹ 정도로 + verbe principal.', 'Consequence -(으)ㄹ 정도로 + main verb.')),
        TF('여기서 집까지 한 시간 정도 걸려요.', ('Il faut environ une heure pour aller chez soi.', 'It takes about an hour to get home.'), VRAI, ('한 시간 정도 = environ une heure.', '한 시간 정도 = about an hour.')),
      ]),
    L('ko-daero', ('Comme, tel que : -는 대로', 'As, just as: -는 대로'), ('Dire qu’on fait une chose conformément à ce qui a été dit ou vu.', 'Say you do something just as it was said or seen.'), 9, [
        ('-(으)ㄴ/는 대로 = comme, tel que : 들은 대로 말하세요 (dites-le comme vous l’avez entendu), 배운 대로 해 보세요.', '-(으)ㄴ/는 대로 = as, just as: 들은 대로 말하세요 (say it as you heard it), 배운 대로 해 보세요.'),
        ('Nom + 대로 : 계획대로 (comme prévu), 순서대로 (dans l’ordre), 마음대로 (comme on veut). 그대로 = tel quel.', 'Noun + 대로: 계획대로 (as planned), 순서대로 (in order), 마음대로 (as you like). 그대로 = as it is.'),
      ], [
        G('gram-ko-daero', '-(으)ㄴ/는 대로', None, '-(eu)n / -neun daero', ('comme, tel que', 'as, just as')),
        V('ko-geudaero', '그대로', None, 'geudaero', ('tel quel', 'as it is')),
        V('ko-sunseo', '순서', None, 'sunseo', ('ordre, tour', 'order, sequence')),
        V('ko-gyuchik', '규칙', None, 'gyuchik', ('règle', 'rule')),
        V('ko-ttareuda', '따르다', None, 'ttareuda', ('suivre (des règles, quelqu’un)', 'to follow')),
        V('ko-maeum', '마음', None, 'maeum', ('cœur, esprit', 'heart, mind')),
        V('ko-yeonmot', '연못', None, 'yeonmot', ('étang', 'pond')),
      ], [
        ex('안내원이 말한 대로 순서대로 들어가세요.', None, 'Entrez dans l’ordre, comme l’a dit le guide.', 'Go in one at a time, as the guide said.'),
        ex('연못은 옛날 모습 그대로예요.', None, 'L’étang est resté tel qu’il était autrefois.', 'The pond is just as it was long ago.'),
      ], [
        FB(CHOOSE, '선생님이 ＿ 대로 해 보세요.', ['말씀하신', '말씀하실', '말씀하시는데'], '말씀하신', ('Ce qui a déjà été dit : -(으)ㄴ 대로.', 'What was already said: -(으)ㄴ 대로.'), ('Faites comme le professeur l’a dit.', 'Do it the way the teacher said.')),
        PC(CHOOSE, '모든 일이 계획＿ 잘 됐어요.', ['대로', '만큼', '처럼요'], '대로', ('Nom + 대로 : comme prévu.', 'Noun + 대로: as planned.'), ('Tout s’est bien passé, comme prévu.', 'Everything went well, as planned.')),
        DC(('Un visiteur entre dans le jardin et ne sait pas où aller.', 'A visitor enters the garden and doesn’t know where to go.'), [('관람객', '어디로 가면 돼요?')], ('Le visiteur demande par où aller.', 'The visitor asks which way to go.'), ['안내판에 있는 순서대로 가세요.', '안내판처럼 가셨어요.', '순서가 있어요?'], '안내판에 있는 순서대로 가세요.', ('순서대로 = dans l’ordre indiqué.', '순서대로 = in the order shown.')),
        TF('규칙대로 하지 않았어요.', ('La personne a suivi les règles.', 'The speaker followed the rules.'), FAUX, ('하지 않았어요 = n’a pas fait (selon les règles).', '하지 않았어요 = didn’t do it (by the rules).')),
      ]),
    L('ko-cheoreom', ('Comme et autant que : 처럼, 만큼', 'Like and as much as: 처럼, 만큼'), ('Comparer par ressemblance ou par égalité.', 'Compare by likeness or by equality.'), 8, [
        ('Nom + 처럼 = comme (ressemblance) : 그림처럼 아름다워요, 사슴처럼 빨라요.', 'Noun + 처럼 = like (resemblance): 그림처럼 아름다워요, 사슴처럼 빨라요.'),
        ('Nom + 만큼 = autant que (égalité) : 형만큼 키가 커요. -(으)ㄴ/는 만큼 = dans la mesure où : 노력한 만큼 결과가 나와요.', 'Noun + 만큼 = as much as (equality): 형만큼 키가 커요. -(으)ㄴ/는 만큼 = in proportion to: 노력한 만큼 결과가 나와요.'),
      ], [
        G('gram-ko-cheoreom-mankeum', '처럼 / 만큼', None, 'cheoreom / mankeum', ('comme ; autant que', 'like; as much as')),
        V('ko-saseum', '사슴', None, 'saseum', ('cerf', 'deer')),
        V('ko-hak', '학', None, 'hak', ('grue (oiseau)', 'crane (bird)')),
        V('ko-sonamu', '소나무', None, 'sonamu', ('pin', 'pine tree')),
        V('ko-geobuk', '거북', None, 'geobuk', ('tortue', 'turtle, tortoise')),
        V('ko-orae', '오래', None, 'orae', ('longtemps', 'for a long time')),
        V('ko-sipjangsaeng', '십장생', None, 'sipjangsaeng', ('les dix symboles de longévité', 'the ten symbols of longevity')),
      ], [
        ex('거북처럼 오래 사세요.', None, 'Vivez aussi longtemps que la tortue.', 'May you live as long as a tortoise.'),
        ex('이 정원은 그림처럼 아름다워요.', None, 'Ce jardin est beau comme un tableau.', 'This garden is as beautiful as a painting.'),
      ], [
        PC(CHOOSE, '동생도 형＿ 키가 커요.', ['만큼', '처럼요', '보다는요'], '만큼', ('Égalité de degré : 만큼.', 'Equal degree: 만큼.'), ('Le petit frère est aussi grand que l’aîné.', 'The younger brother is as tall as the older one.')),
        PC(CHOOSE, '할머니는 소나무＿ 늘 푸르게 사셨어요.', ['처럼', '만큼요', '대로요'], '처럼', ('Ressemblance (comme un pin) : 처럼.', 'Resemblance (like a pine): 처럼.'), ('Grand-mère a toujours vécu verte comme un pin.', 'Grandmother always lived evergreen like a pine.')),
        FB(CHOOSE, '노력한 ＿ 좋은 결과가 나올 거예요.', ['만큼', '처럼', '대로요'], '만큼', ('-(으)ㄴ 만큼 = en proportion de.', '-(으)ㄴ 만큼 = in proportion to.'), ('Tu obtiendras de bons résultats à la mesure de tes efforts.', 'You’ll get results in proportion to your effort.')),
        TF('학처럼 오래 사세요.', ('C’est un vœu de longue vie.', 'It is a wish for a long life.'), VRAI, ('La grue est un symbole de longévité.', 'The crane is a symbol of longevity.')),
      ]),
  ])])

# ═════════════════════════ Île 6 : le fleuve Nakdong ═════════════════════════
W6 = WORLD('topik3-w6', ('Les rives du Nakdong', 'The banks of the Nakdong'), REGION,
  ('Le passif, le causatif et l’état résultant : -이/히/리/기-, -아/어 있다.', 'The passive, the causative and the resulting state: -이/히/리/기-, -아/어 있다.'),
  (('Le Mulgwisin du fleuve', 'The Mulgwisin of the River'), '물', ('Cet esprit des eaux tire les imprudents par les chevilles. Distingue ce qu’on fait, ce qu’on subit et ce qu’on fait faire : il lâchera prise.', 'This water spirit pulls the careless under by their ankles. Tell apart what you do, what is done to you and what you make others do: it will let go.')),
  [CH('topik3-w6-c1', ('Faire, subir, faire faire', 'Doing, undergoing, making do'), [
    L('ko-passive', ('Le passif : 보이다, 열리다, 닫히다', 'The passive: 보이다, 열리다, 닫히다'), ('Reconnaître et utiliser les verbes passifs courants.', 'Recognise and use common passive verbs.'), 10, [
        ('Le passif se forme avec -이-, -히-, -리-, -기- : 보다 → 보이다 (se voir, être visible), 닫다 → 닫히다, 열다 → 열리다, 듣다 → 들리다, 잡다 → 잡히다, 안다 → 안기다.', 'The passive is formed with -이-, -히-, -리-, -기-: 보다 → 보이다 (to be seen, visible), 닫다 → 닫히다, 열다 → 열리다, 듣다 → 들리다, 잡다 → 잡히다, 안다 → 안기다.'),
        ('L’objet devient sujet : 문을 열어요 (j’ouvre la porte) → 문이 열려요 (la porte s’ouvre). L’agent se marque avec 에게 : 고양이가 개에게 잡혔어요.', 'The object becomes the subject: 문을 열어요 (I open the door) → 문이 열려요 (the door opens). The agent takes 에게: 고양이가 개에게 잡혔어요.'),
      ], [
        G('gram-ko-passive', '피동 : -이/히/리/기-', None, 'pidong : -i/hi/ri/gi-', ('forme passive des verbes', 'passive form of verbs')),
        V('ko-boida', '보이다', None, 'boida', ('se voir, être visible', 'to be seen, to be visible')),
        V('ko-deullida', '들리다', None, 'deullida', ('s’entendre, être entendu', 'to be heard')),
        V('ko-yeollida', '열리다', None, 'yeollida', ('s’ouvrir, être ouvert', 'to be opened, to open')),
        V('ko-dachida', '닫히다', None, 'dachida', ('se fermer, être fermé', 'to be closed, to shut')),
        V('ko-japida', '잡히다', None, 'japida', ('être attrapé', 'to be caught')),
        V('ko-angida', '안기다', None, 'angida', ('être pris dans les bras', 'to be held in someone’s arms')),
      ], [
        ex('강 건너편에 마을이 보여요.', None, 'On voit un village de l’autre côté du fleuve.', 'A village can be seen across the river.'),
        ex('바람 때문에 문이 갑자기 닫혔어요.', None, 'À cause du vent, la porte s’est fermée d’un coup.', 'The door suddenly slammed shut because of the wind.'),
      ], [
        FB(CHOOSE, '창문 밖으로 바다가 ＿.', ['보여요', '봐요', '보게 해요'], '보여요', ('Être visible : 보이다 → 보여요.', 'To be visible: 보이다 → 보여요.'), ('On voit la mer par la fenêtre.', 'You can see the sea from the window.')),
        FB(CHOOSE, '도둑이 경찰에게 ＿.', ['잡혔어요', '잡았어요', '잡게 했어요'], '잡혔어요', ('Le voleur subit l’action : 잡히다.', 'The thief undergoes the action: 잡히다.'), ('Le voleur a été attrapé par la police.', 'The thief was caught by the police.')),
        FB(CHOOSE, '어디서 노랫소리가 ＿.', ['들려요', '들어요', '듣겨요'], '들려요', ('Être entendu : 들리다 → 들려요.', 'To be heard: 들리다 → 들려요.'), ('On entend une chanson quelque part.', 'A song can be heard somewhere.')),
        TF('문이 열려 있어요.', ('La porte est fermée.', 'The door is closed.'), FAUX, ('열려 있어요 = elle est ouverte.', '열려 있어요 = it is open.')),
      ]),
    L('ko-causative', ('Le causatif : 먹이다, 입히다, 웃기다', 'The causative: 먹이다, 입히다, 웃기다'), ('Faire faire une action à quelqu’un avec les verbes causatifs.', 'Make someone do something with causative verbs.'), 10, [
        ('Le causatif se forme avec -이-, -히-, -리-, -기-, -우- : 먹다 → 먹이다 (faire manger), 입다 → 입히다 (habiller), 울다 → 울리다 (faire pleurer), 웃다 → 웃기다 (faire rire), 자다 → 재우다 (coucher).', 'The causative is formed with -이-, -히-, -리-, -기-, -우-: 먹다 → 먹이다 (to feed), 입다 → 입히다 (to dress someone), 울다 → 울리다 (to make cry), 웃다 → 웃기다 (to make laugh), 자다 → 재우다 (to put to bed).'),
        ('Certains ressemblent au passif : seul le sens décide (아이를 울려요 = je fais pleurer l’enfant).', 'Some look like the passive: only the meaning tells them apart (아이를 울려요 = I make the child cry).'),
      ], [
        G('gram-ko-causative', '사동 : -이/히/리/기/우-', None, 'sadong : -i/hi/ri/gi/u-', ('forme causative des verbes', 'causative form of verbs')),
        V('ko-meogida', '먹이다', None, 'meogida', ('faire manger, nourrir', 'to feed')),
        V('ko-ipida', '입히다', None, 'ipida', ('habiller (quelqu’un)', 'to dress (someone)')),
        V('ko-ullida', '울리다', None, 'ullida', ('faire pleurer ; faire sonner', 'to make cry; to ring')),
        V('ko-utgida', '웃기다', None, 'utgida', ('faire rire ; être drôle', 'to make laugh; to be funny')),
        V('ko-jaeuda', '재우다', None, 'jaeuda', ('coucher, endormir (quelqu’un)', 'to put to sleep')),
      ], [
        ex('어머니가 아기에게 밥을 먹이고 옷을 입혔어요.', None, 'La mère a fait manger le bébé, puis l’a habillé.', 'The mother fed the baby and then dressed him.'),
        ex('그 이야기가 너무 웃겨서 모두 웃었어요.', None, 'Cette histoire était si drôle que tout le monde a ri.', 'That story was so funny that everyone laughed.'),
      ], [
        FB(CHOOSE, '엄마가 아이에게 우유를 ＿.', ['먹였어요', '먹혔어요', '먹었어요'], '먹였어요', ('Faire boire/manger : 먹이다.', 'To feed: 먹이다.'), ('La maman a fait boire du lait à l’enfant.', 'The mother gave the child milk.')),
        FB(CHOOSE, '아기를 ＿ 후에 책을 읽었어요.', ['재운', '잔', '자게'], '재운', ('Coucher quelqu’un : 재우다 → 재운 후에.', 'To put someone to bed: 재우다 → 재운 후에.'), ('Après avoir couché le bébé, j’ai lu un livre.', 'After putting the baby to bed, I read a book.')),
        DC(('Ton petit frère pleure à cause de son grand frère.', 'Your little brother is crying because of his big brother.'), [('엄마', '왜 동생을 울렸어?')], ('La mère demande pourquoi il a fait pleurer son petit frère.', 'The mother asks why he made his little brother cry.'), ['일부러 울린 게 아니에요.', '동생이 울었어요?', '울리면 안 돼요?'], '일부러 울린 게 아니에요.', ('울리다 = faire pleurer.', '울리다 = to make cry.')),
        TF('그 친구는 정말 웃겨요.', ('Cet ami est vraiment drôle.', 'That friend is really funny.'), VRAI, ('웃기다 = faire rire, être drôle.', '웃기다 = to make laugh, to be funny.')),
      ]),
    L('ko-a-itda', ('L’état : -아/어 있다', 'The state: -아/어 있다'), ('Décrire l’état qui résulte d’une action.', 'Describe the state that results from an action.'), 9, [
        ('-아/어 있다 décrit un état qui dure après l’action : 문이 열려 있어요 (la porte est ouverte), 의자에 앉아 있어요 (il est assis).', '-아/어 있다 describes a state lasting after the action: 문이 열려 있어요 (the door is open), 의자에 앉아 있어요 (he is sitting).'),
        ('Ne pas confondre avec -고 있다 (action en cours) : 옷을 입고 있어요 (il porte / s’habille) mais 서 있어요 (il est debout).', 'Don’t confuse it with -고 있다 (action in progress): 옷을 입고 있어요 (he is wearing / putting on) but 서 있어요 (he is standing).'),
      ], [
        G('gram-ko-a-itda', '-아/어 있다', None, '-a / -eo itda', ('être (état résultant d’une action)', 'to be (state resulting from an action)')),
        V('ko-seoda', '서다', None, 'seoda', ('se tenir debout, s’arrêter', 'to stand, to stop')),
        V('ko-nupda', '눕다', None, 'nupda', ('s’allonger', 'to lie down')),
        V('ko-tteoreojida', '떨어지다', None, 'tteoreojida', ('tomber ; échouer', 'to fall; to fail')),
        V('ko-kyeoda', '켜다', None, 'kyeoda', ('allumer', 'to turn on')),
        V('ko-kkeuda', '끄다', None, 'kkeuda', ('éteindre', 'to turn off')),
        V('ko-gangga', '강가', None, 'gangga', ('bord de rivière', 'riverside')),
      ], [
        ex('강가에 배 한 척이 서 있어요.', None, 'Une barque est arrêtée au bord du fleuve.', 'A boat is moored at the riverside.'),
        ex('방에 불이 켜져 있어요. 누가 있나 봐요.', None, 'La lumière est allumée dans la chambre. Il doit y avoir quelqu’un.', 'The light is on in the room. Someone must be there.'),
      ], [
        FB(CHOOSE, '할아버지가 나무 아래에 ＿ 있어요.', ['앉아', '앉고', '앉게'], '앉아', ('État (assis) : -아/어 있다.', 'State (sitting): -아/어 있다.'), ('Le grand-père est assis sous l’arbre.', 'Grandfather is sitting under the tree.')),
        FB(CHOOSE, '땅에 낙엽이 많이 ＿ 있어요.', ['떨어져', '떨어지고', '떨어질'], '떨어져', ('État résultant : 떨어져 있다.', 'Resulting state: 떨어져 있다.'), ('Il y a beaucoup de feuilles tombées par terre.', 'There are lots of fallen leaves on the ground.')),
        DC(('Tu rentres et la télévision marche alors que personne ne regarde.', 'You come home and the TV is on though nobody is watching.'), [('엄마', '텔레비전이 왜 켜져 있어?')], ('Ta mère demande pourquoi la télévision est allumée.', 'Your mother asks why the TV is on.'), ['아, 끄는 걸 잊어버렸어요.', '켜고 있어요.', '텔레비전을 켰어요?'], '아, 끄는 걸 잊어버렸어요.', ('켜져 있다 = être allumé.', '켜져 있다 = to be on.')),
        TF('동생이 침대에 누워 있어요.', ('Le petit frère est allongé sur le lit.', 'The younger brother is lying on the bed.'), VRAI, ('눕다 → 누워 있다 = être allongé.', '눕다 → 누워 있다 = to be lying down.')),
      ]),
  ])])

# ═════════════════════════ Île 7 : les deux sœurs ═════════════════════════
W7 = WORLD('topik3-w7', ('La maison des deux sœurs', 'The house of the two sisters'), REGION,
  ('Regretter, souhaiter et se décider : -(으)ㄹ걸 그랬다, -았/었으면 좋겠다, -아/어야겠다.', 'Regretting, wishing and making up one’s mind: -(으)ㄹ걸 그랬다, -았/었으면 좋겠다, -아/어야겠다.'),
  (('Les esprits de Janghwa et Hongryeon', 'The Spirits of Janghwa and Hongryeon'), '홍', ('Ces deux sœurs injustement accusées apparaissent à chaque nouveau magistrat. Elles attendent quelqu’un qui sache écouter leurs regrets et décider de faire éclater la vérité.', 'These two wrongly accused sisters appear to every new magistrate. They are waiting for someone who can hear their regrets and decide to bring the truth to light.')),
  [CH('topik3-w7-c1', ('Regrets et résolutions', 'Regrets and resolutions'), [
    L('ko-eulgeol', ('J’aurais dû : -(으)ㄹ걸 그랬다', 'I should have: -(으)ㄹ걸 그랬다'), ('Exprimer un regret sur ce qu’on a fait ou pas fait.', 'Express regret about what you did or didn’t do.'), 9, [
        ('-(으)ㄹ걸 그랬어요 = j’aurais dû : 미리 예약할걸 그랬어요 (j’aurais dû réserver). Seul, -(으)ㄹ걸 se murmure pour soi : 우산을 가져올걸.', '-(으)ㄹ걸 그랬어요 = I should have: 미리 예약할걸 그랬어요 (I should have booked). On its own, -(으)ㄹ걸 is muttered to oneself: 우산을 가져올걸.'),
        ('Au négatif : -지 말걸 그랬어요 = je n’aurais pas dû : 그 말을 하지 말걸.', 'In the negative: -지 말걸 그랬어요 = I shouldn’t have: 그 말을 하지 말걸.'),
      ], [
        G('gram-ko-eulgeol', '-(으)ㄹ걸 그랬다', None, '-(eu)lgeol geuraetda', ('j’aurais dû', 'I should have')),
        V('ko-huhoehada', '후회하다', None, 'huhoehada', ('regretter', 'to regret')),
        V('ko-jinjak', '진작', None, 'jinjak', ('plus tôt (j’aurais dû)', 'sooner, earlier (should have)')),
        V('ko-sagwahada', '사과하다', None, 'sagwahada', ('s’excuser', 'to apologise')),
        V('ko-mitda', '믿다', None, 'mitda', ('croire, faire confiance', 'to believe, to trust')),
        V('ko-jinsil', '진실', None, 'jinsil', ('vérité', 'the truth')),
        V('ko-eonni', '언니', None, 'eonni', ('grande sœur (pour une fille)', 'older sister (of a girl)')),
      ], [
        ex('언니 말을 믿을걸 그랬어요.', None, 'J’aurais dû croire ma grande sœur.', 'I should have believed my sister.'),
        ex('진작 사과할걸. 너무 후회돼요.', None, 'J’aurais dû m’excuser plus tôt. Je le regrette tellement.', 'I should have apologised sooner. I really regret it.'),
      ], [
        FB(CHOOSE, '비가 오네요. 우산을 ＿ 그랬어요.', ['가져올걸', '가져올게', '가져오면'], '가져올걸', ('Regret : -(으)ㄹ걸 그랬어요.', 'Regret: -(으)ㄹ걸 그랬어요.'), ('Il pleut. J’aurais dû prendre un parapluie.', 'It’s raining. I should have brought an umbrella.')),
        FB(CHOOSE, '배가 아파요. 그렇게 많이 먹지 ＿.', ['말걸', '않을걸요', '말게요'], '말걸', ('Je n’aurais pas dû : -지 말걸.', 'I shouldn’t have: -지 말걸.'), ('J’ai mal au ventre. Je n’aurais pas dû manger autant.', 'My stomach hurts. I shouldn’t have eaten so much.')),
        DC(('Ton ami a raté son examen.', 'Your friend failed his exam.'), [('친구', '시험에 떨어졌어요. 너무 속상해요.')], ('Ton ami a échoué et il est triste.', 'Your friend failed and is upset.'), ['저도 더 열심히 공부할걸 그랬어요.', '더 열심히 공부할게요?', '열심히 공부했잖아요요.'], '저도 더 열심히 공부할걸 그랬어요.', ('On partage le regret avec -(으)ㄹ걸 그랬어요.', 'You share the regret with -(으)ㄹ걸 그랬어요.')),
        TF('진실을 말할걸 그랬어요.', ('La personne regrette de ne pas avoir dit la vérité.', 'The speaker regrets not telling the truth.'), VRAI, ('말할걸 그랬어요 = j’aurais dû dire.', '말할걸 그랬어요 = I should have said.')),
      ]),
    L('ko-eosseumyeon', ('J’aimerais que : -았/었으면 좋겠다', 'I wish: -았/었으면 좋겠다'), ('Exprimer un souhait.', 'Express a wish.'), 9, [
        ('-았/었으면 좋겠어요 = j’aimerais que, ce serait bien si : 내일 날씨가 좋았으면 좋겠어요. Le passé ici n’indique pas le temps : il rend le souhait plus fort.', '-았/었으면 좋겠어요 = I wish, it would be nice if: 내일 날씨가 좋았으면 좋겠어요. The past here doesn’t mark time: it makes the wish stronger.'),
        ('On le dit aussi pour soi ou pour les autres : 가족이 모두 행복했으면 좋겠어요.', 'You say it for yourself or for others: 가족이 모두 행복했으면 좋겠어요.'),
      ], [
        G('gram-ko-eosseumyeon', '-았/었으면 좋겠다', None, '-asseumyeon / -eosseumyeon joketda', ('j’aimerais que, je souhaite', 'I wish, I hope')),
        V('ko-barada', '바라다', None, 'barada', ('souhaiter, espérer', 'to hope, to wish for')),
        V('ko-pyeonghwa', '평화', None, 'pyeonghwa', ('paix', 'peace')),
        V('ko-dongsaeng', '동생', None, 'dongsaeng', ('petit frère, petite sœur', 'younger sibling')),
        V('ko-haengbokada', '행복하다', None, 'haengbokada', ('être heureux', 'to be happy')),
        V('ko-yeongwonhi', '영원히', None, 'yeongwonhi', ('pour toujours', 'forever')),
      ], [
        ex('동생이 행복했으면 좋겠어요.', None, 'J’aimerais que ma petite sœur soit heureuse.', 'I hope my younger sister is happy.'),
        ex('이 마을에 영원히 평화가 있었으면 좋겠어요.', None, 'Je souhaite que la paix règne à jamais sur ce village.', 'I wish this village could be at peace forever.'),
      ], [
        FB(CHOOSE, '내일은 날씨가 ＿ 좋겠어요.', ['좋았으면', '좋으면서', '좋아서'], '좋았으면', ('Souhait : -았/었으면 좋겠어요.', 'Wish: -았/었으면 좋겠어요.'), ('J’aimerais qu’il fasse beau demain.', 'I hope the weather is nice tomorrow.')),
        FB(CHOOSE, '빨리 방학이 ＿ 좋겠어요.', ['됐으면', '되면서', '됐거든'], '됐으면', ('되다 → 됐으면 좋겠어요.', '되다 → 됐으면 좋겠어요.'), ('Vivement les vacances !', 'I wish the holidays would come soon.')),
        SO(('Remets dans l’ordre : « J’aimerais que ma famille soit en bonne santé. »', 'Put in order: “I hope my family stays healthy.”'), ['가족이', '건강했으면', '좋겠어요.'], ('Sujet + adjectif-았/었으면 좋겠어요.', 'Subject + adjective-았/었으면 좋겠어요.')),
        TF('시험에 합격했으면 좋겠어요.', ('La personne a déjà réussi l’examen.', 'The speaker has already passed the exam.'), FAUX, ('C’est un souhait, pas un fait accompli.', 'It is a wish, not something that has happened.')),
      ]),
    L('ko-ayagetda', ('Il va falloir que je… : -아/어야겠다', 'I’d better…: -아/어야겠다'), ('Annoncer une décision née de la situation.', 'Announce a decision prompted by the situation.'), 9, [
        ('-아/어야겠어요 = il va falloir que je…, je dois (je le décide maintenant) : 늦었네요. 빨리 가야겠어요.', '-아/어야겠어요 = I’d better…, I must (deciding now): 늦었네요. 빨리 가야겠어요.'),
        ('Plus personnel que -아/어야 해요 (obligation générale) : on y entend la résolution de celui qui parle.', 'More personal than -아/어야 해요 (general obligation): you hear the speaker’s resolve.'),
      ], [
        G('gram-ko-ayagetda', '-아/어야겠다', None, '-aya / -eoyagetda', ('il va falloir que je… (décision)', 'I’d better… (decision)')),
        V('ko-balkida', '밝히다', None, 'balkida', ('révéler, élucider ; éclairer', 'to reveal, to clarify; to light up')),
        V('ko-sageon', '사건', None, 'sageon', ('affaire, incident', 'case, incident')),
        V('ko-beomin', '범인', None, 'beomin', ('coupable, auteur (d’un délit)', 'culprit')),
        V('ko-jeunggeo', '증거', None, 'jeunggeo', ('preuve', 'evidence, proof')),
        V('ko-chatda', '찾다', None, 'chatda', ('chercher, trouver', 'to look for, to find')),
        V('ko-gyeolsimhada', '결심하다', None, 'gyeolsimhada', ('se décider, prendre la résolution', 'to make up one’s mind')),
      ], [
        ex('이 사건의 진실을 꼭 밝혀야겠어요.', None, 'Il va falloir que je fasse toute la lumière sur cette affaire.', 'I must bring the truth of this case to light.'),
        ex('증거가 없네요. 다시 찾아봐야겠어요.', None, 'Il n’y a pas de preuve. Il va falloir que je cherche encore.', 'There’s no evidence. I’d better look again.'),
      ], [
        FB(CHOOSE, '벌써 열 시네요. 이제 집에 ＿.', ['가야겠어요', '갈걸 그랬어요', '갔으면 좋겠어요'], '가야겠어요', ('Décision prise sur le moment : -아/어야겠어요.', 'Decision made on the spot: -아/어야겠어요.'), ('Il est déjà 22 h. Il va falloir que je rentre.', 'It’s already ten. I’d better go home.')),
        FB(CHOOSE, '살이 쪘어요. 운동을 ＿.', ['해야겠어요', '하야겠어요', '해겠어요'], '해야겠어요', ('하다 → 해야겠어요.', '하다 → 해야겠어요.'), ('J’ai grossi. Il va falloir que je fasse du sport.', 'I’ve put on weight. I’d better exercise.')),
        DC(('Le témoin te dit qu’il a vu le coupable.', 'The witness says he saw the culprit.'), [('증인', '그날 밤에 범인을 봤어요.')], ('Le témoin dit avoir vu le coupable cette nuit-là.', 'The witness says he saw the culprit that night.'), ['그럼 자세히 들어 봐야겠어요.', '그럼 범인을 봤어요.', '범인이었으면 좋겠어요.'], '그럼 자세히 들어 봐야겠어요.', ('Résolution : -아/어 봐야겠어요.', 'Resolution: -아/어 봐야겠어요.')),
        TF('범인을 꼭 찾아야겠어요.', ('La personne est décidée à trouver le coupable.', 'The speaker is determined to find the culprit.'), VRAI, ('찾아야겠어요 = il faut que je le trouve.', '찾아야겠어요 = I must find him.')),
      ]),
  ])])

# ═════════════════════════ Île 8 : Namwon ═════════════════════════
W8 = WORLD('topik3-w8', ('Le pavillon de Namwon', 'The Namwon pavilion'), REGION,
  ('Situer précisément dans le temps : -자마자, -는 동안, -(으)ㄴ 지.', 'Placing events precisely in time: -자마자, -는 동안, -(으)ㄴ 지.'),
  (('Le Préfet Byeon', 'Prefect Byeon'), '변', ('Le préfet cupide a jeté Chunhyang en prison. Pour le démasquer au milieu de son banquet, il faut raconter les faits dans l’ordre exact, jour après jour.', 'The greedy prefect has thrown Chunhyang into prison. To unmask him in the middle of his banquet, you must tell the facts in their exact order, day by day.')),
  [CH('topik3-w8-c1', ('Dès que, pendant, depuis', 'As soon as, while, since'), [
    L('ko-jamaja', ('Dès que : -자마자', 'As soon as: -자마자'), ('Enchaîner deux actions immédiatement.', 'Link two actions that follow at once.'), 9, [
        ('Radical + -자마자 = dès que, aussitôt que : 집에 도착하자마자 잤어요 (je me suis couché dès que je suis rentré).', 'Stem + -자마자 = as soon as: 집에 도착하자마자 잤어요 (I went to bed as soon as I got home).'),
        ('Le temps se met sur le second verbe : 소식을 듣자마자 달려갔어요.', 'The tense goes on the second verb: 소식을 듣자마자 달려갔어요.'),
      ], [
        G('gram-ko-jamaja', '-자마자', None, '-jamaja', ('dès que, aussitôt que', 'as soon as')),
        V('ko-dochakada', '도착하다', None, 'dochakada', ('arriver', 'to arrive')),
        V('ko-sosik', '소식', None, 'sosik', ('nouvelles (de quelqu’un)', 'word, tidings')),
        V('ko-dallyeogada', '달려가다', None, 'dallyeogada', ('accourir', 'to rush (somewhere)')),
        V('ko-geune', '그네', None, 'geune', ('balançoire', 'swing')),
        V('ko-gamok', '감옥', None, 'gamok', ('prison', 'prison')),
        V('ko-pureo-juda', '풀어 주다', None, 'pureo juda', ('libérer, relâcher', 'to set free, to release')),
      ], [
        ex('소식을 듣자마자 남원으로 달려갔어요.', None, 'Dès qu’il a appris la nouvelle, il a couru à Namwon.', 'As soon as he heard the news, he rushed to Namwon.'),
        ex('도착하자마자 전화할게요.', None, 'Je t’appelle dès que j’arrive.', 'I’ll call you as soon as I arrive.'),
      ], [
        FB(CHOOSE, '집에 ＿ 샤워를 했어요.', ['오자마자', '왔자마자', '오는 동안'], '오자마자', ('Jamais de passé devant -자마자.', 'Never a past form before -자마자.'), ('Dès que je suis rentré, j’ai pris une douche.', 'I took a shower as soon as I got home.')),
        FB(CHOOSE, '수업이 ＿ 학생들이 나갔어요.', ['끝나자마자', '끝나는 동안', '끝난 지'], '끝나자마자', ('Aussitôt après : -자마자.', 'Right after: -자마자.'), ('Dès que le cours s’est terminé, les élèves sont sortis.', 'As soon as the class ended, the students left.')),
        SO(('Remets dans l’ordre : « Dès qu’il l’a vue, il l’a reconnue. »', 'Put in order: “As soon as he saw her, he recognised her.”'), ['보자마자', '알아봤어요.'], ('Verbe-자마자 + verbe principal au passé.', 'Verb-자마자 + main verb in the past.')),
        TF('어사는 도착하자마자 춘향을 감옥에서 풀어 주었어요.', ('L’inspecteur a attendu plusieurs jours avant de libérer Chunhyang.', 'The inspector waited several days before freeing Chunhyang.'), FAUX, ('도착하자마자 = dès son arrivée.', '도착하자마자 = as soon as he arrived.')),
      ]),
    L('ko-dongan', ('Pendant que : -는 동안', 'While: -는 동안'), ('Dire ce qui se passe pendant une autre action ou une durée.', 'Say what happens during another action or a period.'), 9, [
        ('Verbe + -는 동안 = pendant que : 제가 요리하는 동안 기다려 주세요. Les deux sujets peuvent être différents.', 'Verb + -는 동안 = while: 제가 요리하는 동안 기다려 주세요. The two subjects can differ.'),
        ('Nom de durée + 동안 = pendant : 삼 년 동안, 방학 동안.', 'Length of time + 동안 = for, during: 삼 년 동안, 방학 동안.'),
      ], [
        G('gram-ko-neun-dongan', '-는 동안', None, '-neun dongan', ('pendant que', 'while')),
        V('ko-tteonada', '떠나다', None, 'tteonada', ('partir, quitter', 'to leave')),
        V('ko-gwageo', '과거 시험', None, 'gwageo siheom', ('concours de la fonction publique (Joseon)', 'state examination (Joseon)')),
        V('ko-pyeonji', '편지', None, 'pyeonji', ('lettre', 'letter')),
        V('ko-geuriwohada', '그리워하다', None, 'geuriwohada', ('se languir de, regretter l’absence de', 'to miss, to long for')),
        V('ko-chamda', '참다', None, 'chamda', ('supporter, endurer', 'to endure, to hold back')),
        V('ko-sarang', '사랑', None, 'sarang', ('amour', 'love')),
      ], [
        ex('몽룡이 한양에 있는 동안 춘향은 그를 기다렸어요.', None, 'Pendant que Mongryong était à Hanyang, Chunhyang l’a attendu.', 'While Mongryong was in Hanyang, Chunhyang waited for him.'),
        ex('삼 년 동안 편지 한 장도 오지 않았어요.', None, 'Pendant trois ans, pas une seule lettre n’est arrivée.', 'Not a single letter came for three years.'),
      ], [
        FB(CHOOSE, '제가 장을 ＿ 동안 아이를 봐 주세요.', ['보는', '본', '볼'], '보는', ('Pendant que (action en cours) : -는 동안.', 'While (ongoing action): -는 동안.'), ('Garde l’enfant pendant que je fais les courses.', 'Please watch the child while I do the shopping.')),
        PC(CHOOSE, '방학 ＿ 한국어를 열심히 공부했어요.', ['동안', '때문에', '대로'], '동안', ('Durée + 동안 = pendant.', 'Period + 동안 = during.'), ('Pendant les vacances, j’ai étudié le coréen sérieusement.', 'I studied Korean hard during the holidays.')),
        DC(('Ton ami doit attendre que tu finisses.', 'Your friend has to wait until you finish.'), [('친구', '얼마나 기다려야 돼요?')], ('Ton ami demande combien de temps il doit attendre.', 'Your friend asks how long he has to wait.'), ['제가 준비하는 동안 차 한잔 드세요.', '제가 준비한 동안 드세요.', '차를 마시자마자 준비했어요.'], '제가 준비하는 동안 차 한잔 드세요.', ('-는 동안 + proposition polie.', '-는 동안 + polite offer.')),
        TF('춘향은 몽룡을 기다리는 동안 많이 참았어요.', ('Chunhyang a beaucoup enduré pendant qu’elle attendait Mongryong.', 'Chunhyang endured a lot while waiting for Mongryong.'), VRAI, ('기다리는 동안 = pendant qu’elle attendait.', '기다리는 동안 = while she was waiting.')),
      ]),
    L('ko-eunji', ('Cela fait… que : -(으)ㄴ 지', 'It has been… since: -(으)ㄴ 지'), ('Dire depuis combien de temps une chose a eu lieu.', 'Say how long it has been since something happened.'), 9, [
        ('-(으)ㄴ 지 + durée + 되다 = cela fait … que : 한국에 온 지 일 년이 됐어요 (cela fait un an que je suis venu en Corée).', '-(으)ㄴ 지 + period + 되다 = it has been … since: 한국에 온 지 일 년이 됐어요 (it’s been a year since I came to Korea).'),
        ('On peut aussi dire 지났어요 ou 넘었어요 : 헤어진 지 삼 년이 지났어요. Pour demander : 한국어를 배운 지 얼마나 됐어요?', 'You can also say 지났어요 or 넘었어요: 헤어진 지 삼 년이 지났어요. To ask: 한국어를 배운 지 얼마나 됐어요?'),
      ], [
        G('gram-ko-eun-ji', '-(으)ㄴ 지 … 되다', None, '-(eu)n ji … doeda', ('cela fait … que', 'it has been … since')),
        V('ko-nyeon', '년', None, 'nyeon', ('an, année (compteur)', 'year (counter)')),
        V('ko-gaewol', '개월', None, 'gaewol', ('mois (durée)', 'month(s) (duration)')),
        V('ko-jinada', '지나다', None, 'jinada', ('passer (le temps, un lieu)', 'to pass (time, a place)')),
        V('ko-mane', '만에', None, 'mane', ('au bout de, après (une durée)', 'after (a period of time)')),
        V('ko-gyeolhonhada', '결혼하다', None, 'gyeolhonhada', ('se marier', 'to get married')),
        V('ko-amhaengeosa', '암행어사', None, 'amhaengeosa', ('inspecteur royal secret', 'secret royal inspector')),
      ], [
        ex('한국어를 배운 지 이 년이 됐어요.', None, 'Cela fait deux ans que j’apprends le coréen.', 'It’s been two years since I started learning Korean.'),
        ex('몽룡은 삼 년 만에 암행어사가 되어 돌아왔어요.', None, 'Au bout de trois ans, Mongryong est revenu en inspecteur royal secret.', 'After three years, Mongryong came back as a secret royal inspector.'),
      ], [
        FB(CHOOSE, '서울에 ＿ 지 육 개월이 됐어요.', ['온', '오는', '올'], '온', ('Point de départ passé : -(으)ㄴ 지.', 'Past starting point: -(으)ㄴ 지.'), ('Cela fait six mois que je suis arrivé à Séoul.', 'It’s been six months since I came to Seoul.')),
        FB(CHOOSE, '두 사람이 ＿ 지 십 년이 지났어요.', ['결혼한', '결혼하는', '결혼할'], '결혼한', ('결혼하다 → 결혼한 지.', '결혼하다 → 결혼한 지.'), ('Cela fait dix ans que tous les deux se sont mariés.', 'Ten years have passed since the two of them married.')),
        DC(('Un nouveau collègue te demande depuis quand tu travailles ici.', 'A new colleague asks how long you have worked here.'), [('동료', '이 회사에서 일한 지 얼마나 됐어요?')], ('Ton collègue demande depuis combien de temps tu travailles ici.', 'Your colleague asks how long you have worked here.'), ['삼 년쯤 됐어요.', '삼 년 동안 일할 거예요.', '삼 년 만에 왔어요요.'], '삼 년쯤 됐어요.', ('On répond par une durée + 됐어요.', 'You answer with a period + 됐어요.')),
        TF('친구를 오 년 만에 만났어요.', ('La personne n’avait pas vu son ami depuis cinq ans.', 'The speaker hadn’t seen the friend for five years.'), VRAI, ('오 년 만에 = au bout de cinq ans.', '오 년 만에 = after five years.')),
      ]),
  ])])

FINAL = {
  'slug': 'topik3-final',
  'title': t(('Simulation TOPIK II', 'TOPIK II simulation')),
  'region': REGION,
  'description': t(('Examen blanc au format du TOPIK II (version abrégée) : écoute (듣기), écriture (쓰기) et lecture (읽기), en coréen, noté sur 300. Niveau 3 à 120 points, 4 à 150, 5 à 190, 6 à 230.', 'Mock exam in TOPIK II format (shortened): listening (듣기), writing (쓰기) and reading (읽기), in Korean, marked out of 300. Level 3 at 120 points, 4 at 150, 5 at 190, 6 at 230.')),
  'exam': 'topik3-official',
  'chapters': [],
}

level = {
  'contentVersion': '2026.11.21',
  'level': {'code': 'TOPIK3', 'title': t(('Intermédiaire : comprendre et argumenter en coréen', 'Intermediate: understanding and arguing in Korean')), 'region': REGION, 'order': 14},
  'notice': t(('Les listes de vocabulaire de Koto Quest sont alignées sur les compétences attendues au TOPIK II (niveau 3) mais ne constituent pas des listes officielles du TOPIK.', 'Koto Quest’s vocabulary lists are aligned with the skills expected at TOPIK II (level 3) but are not official TOPIK lists.')),
  'worlds': [W1, W2, W3, W4, W5, W6, W7, W8, FINAL],
}
t((REGION, 'Kingdom of Joseon'))
os.makedirs(os.path.join(ROOT, 'content/topik3'), exist_ok=True)
check_and_write(level, 'content/topik3/topik3.json', ['content/n5/n5.json', 'content/n4/n4.json', 'content/n3/n3.json', 'content/n2/n2.json', 'content/n1/n1.json', 'content/topik1/topik1.json', 'content/topik2/topik2.json'])
