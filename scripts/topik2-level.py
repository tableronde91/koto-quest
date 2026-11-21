# Niveau TOPIK 2 (coréen, TOPIK I niveau 2) : 8 îles, 24 leçons et un examen blanc (français + anglais).
# Suite du TOPIK 1 : raisons, permissions, expériences, propositions relatives, temps, intentions, honorifiques, comparaisons.
# Usage : python3 scripts/topik2-level.py   (réécrit content/topik2/topik2.json)
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from kq_content import *

REGION = 'Pays des contes'

# ═════════════════════════ Île 1 : le village de Jeonju ═════════════════════════
W1 = WORLD('topik2-w1', ('Le village de Jeonju', 'Jeonju Hanok Village'), REGION,
  ('Donner une raison : -아서/-어서, -(으)니까 et 때문에.', 'Giving a reason: -아서/-어서, -(으)니까 and 때문에.'),
  (('Les Jangseung du village', 'The Village Jangseung'), '장', ('Ces deux grands totems de bois gardent l’entrée du village. À chaque voyageur, ils demandent pourquoi il vient : donne-leur de bonnes raisons, bien construites.', 'These two tall wooden totems guard the village entrance. They ask every traveller why they have come: give them good reasons, well put.')),
  [CH('topik2-w1-c1', ('Parce que…', 'Because…'), [
    L('ko-aseo', ('Parce que, alors : -아서/-어서', 'Because, so: -아서/-어서'), ('Relier une cause et sa conséquence avec -아서/-어서.', 'Link a cause and its result with -아서/-어서.'), 9, [
        ('-아서/-어서 relie deux phrases : la première donne la cause, la seconde la conséquence. Même règle de voyelle qu’au présent : 가 → 가서, 먹 → 먹어서, 하다 → 해서.', '-아서/-어서 links two clauses: the first gives the cause, the second the result. Same vowel rule as in the present: 가 → 가서, 먹 → 먹어서, 하다 → 해서.'),
        ('Jamais de passé devant -아서 : on dit 늦어서 죄송합니다 (désolé d’être en retard), pas 늦었어서. Le temps se met à la fin de la phrase.', 'Never use the past before -아서: you say 늦어서 죄송합니다 (sorry I’m late), not 늦었어서. The tense goes at the end of the sentence.'),
        ('Les radicaux en ㅡ perdent cette voyelle : 바쁘다 → 바빠서, 아프다 → 아파서, 배고프다 → 배고파서.', 'Stems in ㅡ lose that vowel: 바쁘다 → 바빠서, 아프다 → 아파서, 배고프다 → 배고파서.'),
      ], [
        G('gram-ko-aseo', '-아서/-어서', None, '-aseo / -eoseo', ('parce que, comme (cause)', 'because, so (cause)')),
        V('ko-baegopeuda', '배고프다', None, 'baegopeuda', ('avoir faim', 'to be hungry')),
        V('ko-pigonhada', '피곤하다', None, 'pigonhada', ('être fatigué', 'to be tired')),
        V('ko-neutda', '늦다', None, 'neutda', ('être en retard', 'to be late')),
        V('ko-apeuda', '아프다', None, 'apeuda', ('avoir mal, être malade', 'to be ill, to hurt')),
        V('ko-bappeuda', '바쁘다', None, 'bappeuda', ('être occupé', 'to be busy')),
        V('ko-hanok', '한옥', None, 'hanok', ('maison traditionnelle coréenne', 'traditional Korean house')),
      ], [
        ex('배가 고파서 비빔밥을 두 그릇 먹었어요.', None, 'J’avais faim, alors j’ai mangé deux bols de bibimbap.', 'I was hungry, so I ate two bowls of bibimbap.'),
        ex('늦어서 죄송합니다. 버스가 안 왔어요.', None, 'Désolé d’être en retard. Le bus n’est pas venu.', 'Sorry I’m late. The bus didn’t come.'),
      ], [
        FB(CHOOSE, '배가 ＿ 밥을 많이 먹었어요.', ['고파서', '고프서', '고팠어서'], '고파서', ('고프다 : le ㅡ tombe → 고파서. Jamais de passé devant -아서.', '고프다: the ㅡ drops → 고파서. Never a past form before -아서.'), ('J’avais faim, alors j’ai beaucoup mangé.', 'I was hungry, so I ate a lot.')),
        FB(CHOOSE, '어제 너무 ＿ 일찍 잤어요.', ['피곤해서', '피곤하서', '피곤했어서'], '피곤해서', ('하다 → 해서.', '하다 → 해서.'), ('Hier, j’étais trop fatigué, alors je me suis couché tôt.', 'Yesterday I was too tired, so I went to bed early.')),
        DC(('Ton ami te demande pourquoi tu es en retard.', 'Your friend asks why you are late.'), [('민지', '왜 늦었어요?')], ('Minji te demande pourquoi tu es en retard.', 'Minji asks why you are late.'), ['버스가 안 와서 늦었어요.', '버스를 타세요.', '내일 늦을 거예요.'], '버스가 안 와서 늦었어요.', ('On donne la cause avec -아서/-어서.', 'You give the cause with -아서/-어서.')),
        TF('머리가 아파서 학교에 안 갔어요.', ('La personne est allée à l’école.', 'The speaker went to school.'), FAUX, ('아파서 = parce que j’avais mal ; 안 갔어요 = je n’y suis pas allé.', '아파서 = because it hurt; 안 갔어요 = I didn’t go.')),
      ]),
    L('ko-nikka', ('Puisque… : -(으)니까', 'Since…: -(으)니까'), ('Donner une raison avant un conseil ou une proposition avec -(으)니까.', 'Give a reason before advice or a suggestion with -(으)니까.'), 9, [
        ('-(으)니까 donne aussi une raison : -으니까 après une consonne (먹으니까), -니까 après une voyelle (가니까). Avec un radical en ㄹ, le ㄹ tombe : 열다 → 여니까.', '-(으)니까 also gives a reason: -으니까 after a consonant (먹으니까), -니까 after a vowel (가니까). With a ㄹ stem, the ㄹ drops: 열다 → 여니까.'),
        ('Devant un ordre poli (-(으)세요) ou une proposition (-(으)ㄹ까요, -(으)ㅂ시다), seul -(으)니까 est possible : 비가 오니까 우산을 가져가세요.', 'Before a polite command (-(으)세요) or a suggestion (-(으)ㄹ까요, -(으)ㅂ시다), only -(으)니까 is possible: 비가 오니까 우산을 가져가세요.'),
        ('Contrairement à -아서, -(으)니까 accepte le passé : 다 먹었으니까 갑시다 (on a fini de manger, allons-y).', 'Unlike -아서, -(으)니까 accepts the past: 다 먹었으니까 갑시다 (we’ve finished eating, let’s go).'),
      ], [
        G('gram-ko-nikka', '-(으)니까', None, '-(eu)nikka', ('puisque, comme (raison, souvent avant un conseil)', 'since, as (reason, often before advice)')),
        V('ko-usan', '우산', None, 'usan', ('parapluie', 'umbrella')),
        V('ko-wiheomhada', '위험하다', None, 'wiheomhada', ('être dangereux', 'to be dangerous')),
        V('ko-josimhada', '조심하다', None, 'josimhada', ('faire attention', 'to be careful')),
        V('ko-mun', '문', None, 'mun', ('porte', 'door')),
        V('ko-datda', '닫다', None, 'datda', ('fermer', 'to close')),
        V('ko-yeolda', '열다', None, 'yeolda', ('ouvrir', 'to open')),
      ], [
        ex('비가 오니까 우산을 가져가세요.', None, 'Il pleut, prends un parapluie.', 'It’s raining, so take an umbrella.'),
        ex('추우니까 문을 닫을까요?', None, 'Il fait froid : on ferme la porte ?', 'It’s cold, shall we close the door?'),
      ], [
        FB(CHOOSE, '비가 ＿ 우산을 가져가세요.', ['오니까', '와서', '오으니까'], '오니까', ('Conseil (가져가세요) : -(으)니까, pas -아서. Après une voyelle : -니까.', 'Advice (가져가세요): -(으)니까, not -아서. After a vowel: -니까.'), ('Il pleut, alors prends un parapluie.', 'It’s raining, so take an umbrella.')),
        FB(CHOOSE, '길이 ＿ 조심하세요.', ['위험하니까', '위험해서', '위험하으니까'], '위험하니까', ('Devant -(으)세요, on utilise -(으)니까.', 'Before -(으)세요, you use -(으)니까.'), ('La route est dangereuse, faites attention.', 'The road is dangerous, be careful.')),
        SO(('Remets dans l’ordre : « Il fait froid, fermez la porte. »', 'Put in order: “It’s cold, close the door.”'), ['추우니까', '문을', '닫으세요.'], ('Raison -(으)니까 + complément + ordre poli.', 'Reason -(으)니까 + object + polite command.')),
        TF('시간이 없으니까 택시를 탑시다.', ('Les personnes ont beaucoup de temps.', 'The speakers have plenty of time.'), FAUX, ('시간이 없으니까 = comme on n’a pas le temps.', '시간이 없으니까 = since we have no time.')),
      ]),
    L('ko-ttaemune', ('À cause de : 때문에', 'Because of: 때문에'), ('Expliquer une cause avec 때문에 et -기 때문에.', 'Explain a cause with 때문에 and -기 때문에.'), 8, [
        ('Nom + 때문에 = à cause de : 감기 때문에 (à cause d’un rhume), 눈 때문에 (à cause de la neige).', 'Noun + 때문에 = because of: 감기 때문에 (because of a cold), 눈 때문에 (because of the snow).'),
        ('Verbe ou adjectif + -기 때문에 = parce que, plus soutenu et fréquent à l’écrit : 시험이 있기 때문에 공부해요.', 'Verb or adjective + -기 때문에 = because, more formal and common in writing: 시험이 있기 때문에 공부해요.'),
        ('Comme -아서, -기 때문에 ne s’emploie pas devant un ordre ou une proposition.', 'Like -아서, -기 때문에 is not used before a command or a suggestion.'),
      ], [
        G('gram-ko-ttaemune', '때문에 / -기 때문에', None, 'ttaemune / -gi ttaemune', ('à cause de ; parce que', 'because of; because')),
        V('ko-gamgi', '감기', None, 'gamgi', ('rhume', 'a cold')),
        V('ko-siheom', '시험', None, 'siheom', ('examen', 'exam, test')),
        V('ko-gyotong', '교통', None, 'gyotong', ('circulation, transports', 'traffic, transport')),
        V('ko-geokjeonghada', '걱정하다', None, 'geokjeonghada', ('s’inquiéter', 'to worry')),
        V('ko-nun', '눈', None, 'nun', ('neige ; œil', 'snow; eye')),
      ], [
        ex('눈 때문에 비행기가 늦게 출발했어요.', None, 'À cause de la neige, l’avion est parti en retard.', 'Because of the snow, the plane took off late.'),
        ex('내일 시험이 있기 때문에 오늘은 못 놀아요.', None, 'J’ai un examen demain, alors aujourd’hui je ne peux pas sortir m’amuser.', 'I have an exam tomorrow, so I can’t go out today.'),
      ], [
        PC(CHOOSE, '감기＿ 회사에 못 갔어요.', ['때문에', '기 때문에', '니까'], '때문에', ('Après un nom : 때문에 directement.', 'After a noun: 때문에 directly.'), ('Je ne suis pas allé au travail à cause d’un rhume.', 'I couldn’t go to work because of a cold.')),
        FB(CHOOSE, '내일 시험이 ＿ 오늘은 못 놀아요.', ['있기 때문에', '있때문에', '있어서 때문에'], '있기 때문에', ('Après un verbe : -기 때문에.', 'After a verb: -기 때문에.'), ('J’ai un examen demain, alors je ne peux pas m’amuser aujourd’hui.', 'I have an exam tomorrow, so I can’t have fun today.')),
        DC(('Ton amie a l’air inquiète.', 'Your friend looks worried.'), [('민지', '왜 그렇게 걱정해요?')], ('Minji te demande pourquoi tu t’inquiètes autant.', 'Minji asks you why you are so worried.'), ['내일 시험 때문에 걱정해요.', '걱정하지 마세요.', '시험을 잘 봤어요.'], '내일 시험 때문에 걱정해요.', ('On explique la cause avec 때문에.', 'You explain the cause with 때문에.')),
        TF('교통 때문에 늦었어요.', ('La personne est en retard à cause de la circulation.', 'The speaker is late because of the traffic.'), VRAI, ('교통 때문에 = à cause de la circulation.', '교통 때문에 = because of the traffic.')),
      ]),
  ])])

# ═════════════════════════ Île 2 : l'atelier du potier ═════════════════════════
W2 = WORLD('topik2-w2', ('L’atelier du potier d’Icheon', 'The potter’s workshop in Icheon'), REGION,
  ('Dire ce qu’on sait faire, ce qui est permis, interdit ou obligatoire.', 'Say what you can do and what is allowed, forbidden or required.'),
  (('Le Crapaud d’or', 'The Golden Toad'), '두', ('Ce crapaud porte-bonheur veille sur les fours des potiers. Il ne laisse toucher l’argile qu’à ceux qui connaissent les règles de l’atelier.', 'This lucky toad watches over the potters’ kilns. Only those who know the workshop rules may touch the clay.')),
  [CH('topik2-w2-c1', ('Pouvoir, avoir le droit, devoir', 'Can, may, must'), [
    L('ko-su-itda', ('Savoir faire : -(으)ㄹ 수 있어요', 'Being able to: -(으)ㄹ 수 있어요'), ('Dire ce qu’on peut ou ne peut pas faire.', 'Say what you can or cannot do.'), 9, [
        ('Radical + -을 수 있어요 après une consonne (먹을 수 있어요), -ㄹ 수 있어요 après une voyelle (갈 수 있어요). Le contraire : -(으)ㄹ 수 없어요.', 'Stem + -을 수 있어요 after a consonant (먹을 수 있어요), -ㄹ 수 있어요 after a vowel (갈 수 있어요). The opposite: -(으)ㄹ 수 없어요.'),
        ('Les radicaux en ㄹ ajoutent seulement 수 있어요 : 만들다 → 만들 수 있어요.', 'Stems ending in ㄹ just add 수 있어요: 만들다 → 만들 수 있어요.'),
        ('못 + verbe dit presque la même chose : 못 가요 ≈ 갈 수 없어요.', '못 + verb means almost the same: 못 가요 ≈ 갈 수 없어요.'),
      ], [
        G('gram-ko-su-itda', '-(으)ㄹ 수 있다/없다', None, '-(eu)l su itda / eopda', ('pouvoir, savoir (faire) / ne pas pouvoir', 'can, be able to / cannot')),
        V('ko-mandeulda', '만들다', None, 'mandeulda', ('fabriquer, faire', 'to make')),
        V('ko-dojagi', '도자기', None, 'dojagi', ('céramique, poterie', 'ceramics, pottery')),
        V('ko-unjeonhada', '운전하다', None, 'unjeonhada', ('conduire', 'to drive')),
        V('ko-norae', '노래', None, 'norae', ('chanson', 'song')),
        V('ko-honja', '혼자', None, 'honja', ('seul, tout seul', 'alone, by oneself')),
      ], [
        ex('저는 혼자 도자기를 만들 수 있어요.', None, 'Je sais faire une poterie tout seul.', 'I can make pottery by myself.'),
        ex('운전할 수 있어요? — 아니요, 운전할 수 없어요.', None, 'Tu sais conduire ? — Non, je ne sais pas conduire.', 'Can you drive? — No, I can’t drive.'),
      ], [
        FB(CHOOSE, '저는 한국 음식을 ＿ 수 있어요.', ['만들', '만드', '만들을'], '만들', ('Radical en ㄹ : on ajoute seulement 수 있다.', 'ㄹ stem: you just add 수 있다.'), ('Je sais cuisiner des plats coréens.', 'I can cook Korean food.')),
        FB(CHOOSE, '내일은 바빠서 ＿ 수 없어요.', ['갈', '가을', '갔을'], '갈', ('가 finit par une voyelle : -ㄹ 수.', '가 ends with a vowel: -ㄹ 수.'), ('Demain je suis occupé, je ne peux pas y aller.', 'I’m busy tomorrow, so I can’t go.')),
        DC(('Un collègue te demande si tu sais conduire. Tu ne sais pas.', 'A colleague asks whether you can drive. You can’t.'), [('준호', '운전할 수 있어요?')], ('Junho te demande si tu sais conduire.', 'Junho asks whether you can drive.'), ['아니요, 운전할 수 없어요.', '네, 운전했어요.', '운전하세요.'], '아니요, 운전할 수 없어요.', ('-(으)ㄹ 수 없어요 = je ne peux pas, je ne sais pas.', '-(으)ㄹ 수 없어요 = I can’t.')),
        TF('저는 혼자 도자기를 만들 수 있어요.', ('La personne a besoin d’aide pour faire une poterie.', 'The speaker needs help to make pottery.'), FAUX, ('혼자 만들 수 있어요 = je sais le faire tout seul.', '혼자 만들 수 있어요 = I can make it by myself.')),
      ]),
    L('ko-ado-dwaeyo', ('Permis ou interdit : -아도 돼요, -(으)면 안 돼요', 'Allowed or forbidden: -아도 돼요, -(으)면 안 돼요'), ('Demander la permission et dire ce qui est interdit.', 'Ask for permission and say what is forbidden.'), 9, [
        ('-아도/어도 돼요 = on peut, c’est permis : 사진을 찍어도 돼요? (je peux prendre une photo ?). Même règle de voyelle : 가도, 먹어도, 해도.', '-아도/어도 돼요 = you may, it’s allowed: 사진을 찍어도 돼요? (may I take a photo?). Same vowel rule: 가도, 먹어도, 해도.'),
        ('-(으)면 안 돼요 = il ne faut pas, c’est interdit : 만지면 안 돼요 (on ne touche pas), 들어가면 안 돼요 (défense d’entrer).', '-(으)면 안 돼요 = you must not, it’s forbidden: 만지면 안 돼요 (don’t touch), 들어가면 안 돼요 (no entry).'),
        ('Pour répondre : 네, 돼요 (oui, c’est permis) ou 아니요, 안 돼요 (non).', 'To answer: 네, 돼요 (yes, it’s allowed) or 아니요, 안 돼요 (no).'),
      ], [
        G('gram-ko-ado-dwaeyo', '-아도/어도 돼요', None, '-ado / -eodo dwaeyo', ('on peut, avoir le droit de', 'may, be allowed to')),
        G('gram-ko-myeon-an-dwaeyo', '-(으)면 안 돼요', None, '-(eu)myeon an dwaeyo', ('il ne faut pas, c’est interdit de', 'must not, not allowed to')),
        V('ko-sajin', '사진', None, 'sajin', ('photo', 'photo')),
        V('ko-jjikda', '찍다', None, 'jjikda', ('prendre (une photo)', 'to take (a photo)')),
        V('ko-manjida', '만지다', None, 'manjida', ('toucher', 'to touch')),
        V('ko-dambae', '담배', None, 'dambae', ('cigarette, tabac', 'cigarette, tobacco')),
        V('ko-piuda', '피우다', None, 'piuda', ('fumer', 'to smoke')),
        V('ko-deureogada', '들어가다', None, 'deureogada', ('entrer', 'to go in, to enter')),
      ], [
        ex('여기에서 사진을 찍어도 돼요? — 네, 찍어도 돼요.', None, 'Je peux prendre des photos ici ? — Oui, vous pouvez.', 'May I take photos here? — Yes, you may.'),
        ex('도자기를 만지면 안 돼요.', None, 'Il ne faut pas toucher les poteries.', 'You must not touch the pottery.'),
      ], [
        FB(CHOOSE, '여기에서 사진을 ＿ 돼요?', ['찍어도', '찍아도', '찍으면'], '찍어도', ('찍 : voyelle ㅣ → -어도.', '찍: vowel ㅣ → -어도.'), ('Je peux prendre des photos ici ?', 'May I take photos here?')),
        FB(CHOOSE, '도자기를 손으로 만지＿ 안 돼요.', ['면', '어도', '고'], '면', ('Interdiction : -(으)면 안 돼요.', 'Prohibition: -(으)면 안 돼요.'), ('Il ne faut pas toucher les poteries avec les mains.', 'You must not touch the pottery with your hands.')),
        DC(('Tu t’approches d’une salle de l’atelier.', 'You walk towards a room in the workshop.'), [('직원', '죄송하지만, 여기에 들어가면 안 돼요.')], ('L’employé dit qu’il ne faut pas entrer ici.', 'The staff member says you must not go in here.'), ['아, 죄송합니다.', '네, 들어가도 돼요.', '사진을 찍었어요.'], '아, 죄송합니다.', ('On s’excuse quand on apprend qu’une chose est interdite.', 'You apologise when you learn something is forbidden.')),
        TF('여기에서 담배를 피우면 안 돼요.', ('On a le droit de fumer ici.', 'Smoking is allowed here.'), FAUX, ('피우면 안 돼요 = il est interdit de fumer.', '피우면 안 돼요 = smoking is forbidden.')),
      ]),
    L('ko-aya-haeyo', ('Il faut : -아야/어야 해요', 'Must: -아야/어야 해요'), ('Dire ce qu’on doit faire.', 'Say what you have to do.'), 8, [
        ('-아야/어야 해요 = il faut, je dois : 가야 해요, 먹어야 해요, 공부해야 해요.', '-아야/어야 해요 = I must, I have to: 가야 해요, 먹어야 해요, 공부해야 해요.'),
        ('On entend aussi -아야/어야 돼요 avec le même sens. Au passé : 가야 했어요 (j’ai dû y aller).', 'You also hear -아야/어야 돼요 with the same meaning. In the past: 가야 했어요 (I had to go).'),
      ], [
        G('gram-ko-aya-haeyo', '-아야/어야 해요', None, '-aya / -eoya haeyo', ('il faut, devoir', 'must, to have to')),
        V('ko-sukje', '숙제', None, 'sukje', ('devoirs', 'homework')),
        V('ko-junbihada', '준비하다', None, 'junbihada', ('préparer', 'to prepare')),
        V('ko-iljjik', '일찍', None, 'iljjik', ('tôt', 'early')),
        V('ko-ireonada', '일어나다', None, 'ireonada', ('se lever', 'to get up')),
        V('ko-yak', '약', None, 'yak', ('médicament', 'medicine')),
        V('ko-naeda', '내다', None, 'naeda', ('payer ; rendre (un devoir)', 'to pay; to hand in')),
      ], [
        ex('내일은 일찍 일어나야 해요.', None, 'Demain, il faut que je me lève tôt.', 'I have to get up early tomorrow.'),
        ex('숙제를 금요일까지 내야 해요.', None, 'Il faut rendre les devoirs avant vendredi.', 'The homework has to be handed in by Friday.'),
      ], [
        FB(CHOOSE, '내일 시험이 있어서 공부＿.', ['해야 해요', '하야 해요', '해도 돼요'], '해야 해요', ('하다 → 해야 해요 (obligation).', '하다 → 해야 해요 (obligation).'), ('J’ai un examen demain, il faut que j’étudie.', 'I have an exam tomorrow, so I have to study.')),
        FB(CHOOSE, '감기에 걸렸어요. 약을 ＿ 해요.', ['먹어야', '먹아야', '먹으면'], '먹어야', ('먹 : voyelle ㅓ → -어야.', '먹: vowel ㅓ → -어야.'), ('J’ai attrapé un rhume. Il faut que je prenne des médicaments.', 'I caught a cold. I have to take medicine.')),
        SO(('Remets dans l’ordre : « Demain, il faut se lever tôt. »', 'Put in order: “Tomorrow I have to get up early.”'), ['내일은', '일찍', '일어나야', '해요.'], ('Moment + adverbe + verbe-아야/어야 해요.', 'Time + adverb + verb-아야/어야 해요.')),
        TF('숙제를 내일까지 내야 해요.', ('Les devoirs sont à rendre pour demain.', 'The homework is due tomorrow.'), VRAI, ('내일까지 내야 해요 = il faut le rendre d’ici demain.', '내일까지 내야 해요 = it must be handed in by tomorrow.')),
      ]),
  ])])

# ═════════════════════════ Île 3 : le festival des lanternes ═════════════════════════
W3 = WORLD('topik2-w3', ('Le festival des lanternes', 'The lantern festival'), REGION,
  ('Dire ce qu’on est en train de faire, essayer quelque chose et raconter ses expériences.', 'Say what you are doing, try something out and talk about your experiences.'),
  (('La Pie messagère', 'The Messenger Magpie'), '까', ('Dans les peintures populaires, la pie annonce les bonnes nouvelles et se moque du tigre. Raconte-lui ce que tu fais et ce que tu as déjà vécu : elle répandra la nouvelle.', 'In folk paintings, the magpie brings good news and teases the tiger. Tell it what you are doing and what you have already done: it will spread the word.')),
  [CH('topik2-w3-c1', ('En ce moment et déjà', 'Right now and already'), [
    L('ko-go-itda', ('Être en train de : -고 있어요', 'Being in the middle of: -고 있어요'), ('Décrire une action en cours.', 'Describe an action in progress.'), 8, [
        ('Radical + -고 있어요 = être en train de : 먹고 있어요, 기다리고 있어요. Au passé : 하고 있었어요 (j’étais en train de faire).', 'Stem + -고 있어요 = to be …-ing: 먹고 있어요, 기다리고 있어요. In the past: 하고 있었어요 (I was doing).'),
        ('Avec les verbes d’habillement, -고 있어요 décrit un état : 한복을 입고 있어요 = elle porte un hanbok.', 'With clothing verbs, -고 있어요 describes a state: 한복을 입고 있어요 = she is wearing a hanbok.'),
      ], [
        G('gram-ko-go-itda', '-고 있어요', None, '-go isseoyo', ('être en train de', 'to be …-ing')),
        V('ko-yeondeung', '연등', None, 'yeondeung', ('lanterne de lotus', 'lotus lantern')),
        V('ko-chukje', '축제', None, 'chukje', ('festival, fête', 'festival')),
        V('ko-gugyeonghada', '구경하다', None, 'gugyeonghada', ('regarder, visiter (en curieux)', 'to look around, to go sightseeing')),
        V('ko-gang', '강', None, 'gang', ('rivière, fleuve', 'river')),
        V('ko-jeonhwahada', '전화하다', None, 'jeonhwahada', ('téléphoner', 'to phone, to call')),
      ], [
        ex('사람들이 강에서 연등을 구경하고 있어요.', None, 'Les gens sont en train de regarder les lanternes sur la rivière.', 'People are watching the lanterns on the river.'),
        ex('지금 친구를 기다리고 있어요.', None, 'J’attends un ami en ce moment.', 'I’m waiting for a friend right now.'),
      ], [
        FB(CHOOSE, '지금 친구를 ＿ 있어요.', ['기다리고', '기다려', '기다리는'], '기다리고', ('Action en cours : radical + 고 있어요.', 'Action in progress: stem + 고 있어요.'), ('J’attends un ami en ce moment.', 'I’m waiting for a friend right now.')),
        FB(CHOOSE, '사람들이 강에서 연등을 ＿.', ['보고 있어요', '봐고 있어요', '보고 해요'], '보고 있어요', ('보다 → 보고 있어요.', '보다 → 보고 있어요.'), ('Les gens regardent les lanternes sur la rivière.', 'People are watching the lanterns on the river.')),
        DC(('Ta mère t’appelle pendant le festival.', 'Your mother calls you during the festival.'), [('엄마', '지금 뭐 해요?')], ('Ta mère te demande ce que tu fais.', 'Your mother asks what you are doing.'), ['축제를 구경하고 있어요.', '축제를 구경할 수 없어요.', '어제 구경했어요.'], '축제를 구경하고 있어요.', ('À « que fais-tu ? », on répond avec -고 있어요.', 'You answer “what are you doing?” with -고 있어요.')),
        TF('언니는 지금 전화하고 있어요.', ('La grande sœur est en train de téléphoner.', 'The older sister is on the phone right now.'), VRAI, ('전화하고 있어요 = elle est en train de téléphoner.', '전화하고 있어요 = she is on the phone.')),
      ]),
    L('ko-a-boda', ('Essayer : -아/어 보세요', 'Trying: -아/어 보세요'), ('Proposer d’essayer et dire qu’on a essayé.', 'Suggest trying something and say you tried it.'), 8, [
        ('-아/어 보다 = essayer, faire pour voir : 먹어 보세요 (goûtez), 입어 봐도 돼요? (je peux l’essayer ?).', '-아/어 보다 = to try, to do something to see: 먹어 보세요 (try it), 입어 봐도 돼요? (may I try it on?).'),
        ('Au passé, il raconte une expérience : 한복을 입어 봤어요 (j’ai déjà porté un hanbok).', 'In the past, it tells of an experience: 한복을 입어 봤어요 (I have worn a hanbok).'),
      ], [
        G('gram-ko-a-boda', '-아/어 보다', None, '-a / -eo boda', ('essayer de, faire pour voir', 'to try (doing)')),
        V('ko-ipda', '입다', None, 'ipda', ('mettre, porter (un vêtement)', 'to wear, to put on (clothes)')),
        V('ko-hanbok', '한복', None, 'hanbok', ('hanbok, costume traditionnel', 'hanbok, traditional dress')),
        V('ko-sinda', '신다', None, 'sinda', ('chausser, mettre (des chaussures)', 'to put on (shoes)')),
        V('ko-mat', '맛', None, 'mat', ('goût, saveur', 'taste, flavour')),
        V('ko-tteok', '떡', None, 'tteok', ('gâteau de riz', 'rice cake')),
        V('ko-cheoeum', '처음', None, 'cheoeum', ('première fois ; au début', 'first time; at first')),
      ], [
        ex('이 떡 한번 먹어 보세요. 정말 맛있어요.', None, 'Goûtez ce gâteau de riz. Il est vraiment bon.', 'Try this rice cake. It’s really good.'),
        ex('처음으로 한복을 입어 봤어요.', None, 'J’ai porté un hanbok pour la première fois.', 'I wore a hanbok for the first time.'),
      ], [
        FB(CHOOSE, '이 떡 한번 ＿ 보세요. 맛있어요.', ['먹어', '먹아', '먹고'], '먹어', ('먹 → 먹어 보세요.', '먹 → 먹어 보세요.'), ('Goûte ce gâteau de riz. Il est bon.', 'Try this rice cake. It’s good.')),
        FB(CHOOSE, '이 한복을 ＿ 봐도 돼요?', ['입어', '입아', '입고'], '입어', ('입 : voyelle ㅣ → 입어 보다.', '입: vowel ㅣ → 입어 보다.'), ('Je peux essayer ce hanbok ?', 'May I try on this hanbok?')),
        DC(('Ton amie te conseille d’essayer un hanbok.', 'Your friend suggests you try on a hanbok.'), [('민지', '이 한복 예뻐요. 한번 입어 보세요!')], ('Minji te dit d’essayer ce hanbok.', 'Minji tells you to try on this hanbok.'), ['좋아요. 입어 봐요.', '아니요, 한복이 아니에요.', '어제 한복이 없었어요.'], '좋아요. 입어 봐요.', ('On accepte l’invitation à essayer avec -아/어 보다.', 'You accept the invitation to try with -아/어 보다.')),
        TF('처음 떡볶이를 먹어 봤어요.', ('La personne a goûté le tteokbokki pour la première fois.', 'The speaker tried tteokbokki for the first time.'), VRAI, ('처음 … 먹어 봤어요 = j’en ai mangé pour la première fois.', '처음 … 먹어 봤어요 = I tried it for the first time.')),
      ]),
    L('ko-jeogi-itda', ('Avoir déjà… : -(으)ㄴ 적이 있어요', 'Having ever…: -(으)ㄴ 적이 있어요'), ('Dire ce qu’on a déjà fait ou jamais fait.', 'Say what you have or have never done.'), 9, [
        ('-(으)ㄴ 적이 있어요 = avoir déjà fait : 간 적이 있어요, 먹은 적이 있어요. Le contraire : -(으)ㄴ 적이 없어요 (n’avoir jamais).', '-(으)ㄴ 적이 있어요 = to have done before: 간 적이 있어요, 먹은 적이 있어요. The opposite: -(으)ㄴ 적이 없어요 (never).'),
        ('On le combine souvent avec -아/어 보다 : 가 본 적이 있어요? (tu y es déjà allé ?).', 'It is often combined with -아/어 보다: 가 본 적이 있어요? (have you ever been there?).'),
        ('Pour répondre « pas encore » : 아직 없어요.', 'To answer “not yet”: 아직 없어요.'),
      ], [
        G('gram-ko-jeogi-itda', '-(으)ㄴ 적이 있다/없다', None, '-(eu)n jeogi itda / eopda', ('avoir déjà… / n’avoir jamais…', 'to have (ever) done / to have never done')),
        V('ko-oeguk', '외국', None, 'oeguk', ('pays étranger, l’étranger', 'foreign country, abroad')),
        V('ko-gyeongheom', '경험', None, 'gyeongheom', ('expérience (vécue)', 'experience')),
        V('ko-han-beon', '한 번', None, 'han beon', ('une fois', 'once')),
        V('ko-ajik', '아직', None, 'ajik', ('encore ; pas encore', 'still; (not) yet')),
        V('ko-hoksi', '혹시', None, 'hoksi', ('par hasard, est-ce que par hasard', 'by any chance')),
      ], [
        ex('혹시 한국에 가 본 적이 있어요? — 아니요, 아직 없어요.', None, 'Tu es déjà allé en Corée, par hasard ? — Non, pas encore.', 'Have you ever been to Korea, by any chance? — No, not yet.'),
        ex('저는 외국에서 일한 경험이 있어요.', None, 'J’ai une expérience de travail à l’étranger.', 'I have experience of working abroad.'),
      ], [
        FB(CHOOSE, '저는 제주도에 ＿ 적이 있어요.', ['간', '가는', '갈'], '간', ('Expérience passée : -(으)ㄴ 적이 있어요.', 'Past experience: -(으)ㄴ 적이 있어요.'), ('Je suis déjà allé à Jeju.', 'I have been to Jeju.')),
        FB(CHOOSE, '혹시 한국 영화를 ＿ 적이 있어요?', ['본', '보는', '볼'], '본', ('보다 → 본 적이 있어요.', '보다 → 본 적이 있어요.'), ('As-tu déjà vu un film coréen ?', 'Have you ever seen a Korean film?')),
        DC(('Junho te pose une question sur tes voyages. Tu n’es jamais allé en Corée.', 'Junho asks about your travels. You have never been to Korea.'), [('준호', '혹시 한국에 가 본 적이 있어요?')], ('Junho te demande si tu es déjà allé en Corée.', 'Junho asks whether you have ever been to Korea.'), ['아니요, 아직 없어요.', '네, 갈 거예요.', '한국에 가고 있어요.'], '아니요, 아직 없어요.', ('아직 없어요 = pas encore.', '아직 없어요 = not yet.')),
        TF('외국에 한 번 가 본 적이 있어요.', ('La personne n’est jamais allée à l’étranger.', 'The speaker has never been abroad.'), FAUX, ('한 번 가 본 적이 있어요 = j’y suis allé une fois.', '한 번 가 본 적이 있어요 = I have been once.')),
      ]),
  ])])

# ═════════════════════════ Île 4 : la bibliothèque royale ═════════════════════════
W4 = WORLD('topik2-w4', ('La bibliothèque royale', 'The royal library'), REGION,
  ('Décrire avec des propositions relatives : le livre que je lis, celui que j’ai lu, celui que je vais lire.', 'Describe with relative clauses: the book I am reading, the one I read, the one I will read.'),
  (('Le Corbeau à trois pattes', 'The Three-legged Crow'), '삼', ('Le Samjogo, oiseau du soleil, garde les livres du roi Jeongjo. Il ne prête un livre qu’à celui qui sait le décrire exactement.', 'The Samjogo, bird of the sun, guards King Jeongjo’s books. It lends a book only to those who can describe it exactly.')),
  [CH('topik2-w4-c1', ('Décrire un nom', 'Describing a noun'), [
    L('ko-neun-mod', ('Le livre que je lis : -는', 'The book I am reading: -는'), ('Décrire un nom avec un verbe au présent.', 'Describe a noun with a verb in the present.'), 9, [
        ('En coréen, ce qui décrit un nom se place devant lui. Verbe au présent + 는 + nom : 읽는 책 (le livre que je lis), 공부하는 학생 (l’étudiant qui étudie).', 'In Korean, whatever describes a noun goes in front of it. Present verb + 는 + noun: 읽는 책 (the book I am reading), 공부하는 학생 (the student who is studying).'),
        ('Le ㄹ final tombe : 알다 → 아는 사람 (quelqu’un que je connais). 있다/없다 prennent aussi -는 : 맛있는 음식, 재미없는 영화.', 'A final ㄹ drops: 알다 → 아는 사람 (someone I know). 있다/없다 also take -는: 맛있는 음식, 재미없는 영화.'),
      ], [
        G('gram-ko-neun-mod', '-는 (+ nom)', None, '-neun', ('qui…, que… (présent, devant un nom)', 'who…, that… (present, before a noun)')),
        V('ko-doseogwan', '도서관', None, 'doseogwan', ('bibliothèque', 'library')),
        V('ko-billida', '빌리다', None, 'billida', ('emprunter', 'to borrow')),
        V('ko-soseol', '소설', None, 'soseol', ('roman', 'novel')),
        V('ko-sajeon', '사전', None, 'sajeon', ('dictionnaire', 'dictionary')),
        V('ko-sseuda', '쓰다', None, 'sseuda', ('écrire ; utiliser', 'to write; to use')),
        V('ko-alda', '알다', None, 'alda', ('savoir, connaître', 'to know')),
      ], [
        ex('지금 읽는 책은 한국 소설이에요.', None, 'Le livre que je lis en ce moment est un roman coréen.', 'The book I’m reading now is a Korean novel.'),
        ex('도서관에서 책을 빌리는 사람이 많아요.', None, 'Beaucoup de gens empruntent des livres à la bibliothèque.', 'Many people borrow books from the library.'),
      ], [
        FB(CHOOSE, '지금 ＿ 책이 뭐예요?', ['읽는', '읽은', '읽을'], '읽는', ('지금 : action présente → -는.', '지금: present action → -는.'), ('Quel est le livre que tu lis en ce moment ?', 'What is the book you are reading now?')),
        FB(CHOOSE, '이 반에는 제가 ＿ 사람이 없어요.', ['아는', '알는', '알은'], '아는', ('알다 : le ㄹ tombe devant -는 → 아는.', '알다: the ㄹ drops before -는 → 아는.'), ('Dans cette classe, je ne connais personne.', 'I don’t know anyone in this class.')),
        SO(('Remets dans l’ordre : « C’est un plat délicieux. »', 'Put in order: “It’s a delicious dish.”'), ['이것은', '맛있는', '음식이에요.'], ('Le mot qui décrit (맛있는) se place devant le nom.', 'The describing word (맛있는) comes before the noun.')),
        TF('사전을 쓰는 학생이 많아요.', ('Beaucoup d’étudiants utilisent un dictionnaire.', 'Many students use a dictionary.'), VRAI, ('사전을 쓰는 학생 = les étudiants qui utilisent un dictionnaire.', '사전을 쓰는 학생 = students who use a dictionary.')),
      ]),
    L('ko-eun-mod', ('Le film que j’ai vu : -(으)ㄴ', 'The film I saw: -(으)ㄴ'), ('Décrire un nom avec un verbe au passé ou un adjectif.', 'Describe a noun with a past verb or an adjective.'), 9, [
        ('Verbe au passé + (으)ㄴ + nom : 어제 본 영화 (le film que j’ai vu hier), 읽은 책 (le livre que j’ai lu).', 'Past verb + (으)ㄴ + noun: 어제 본 영화 (the film I saw yesterday), 읽은 책 (the book I read).'),
        ('Adjectif + (으)ㄴ + nom, au présent : 큰 집 (une grande maison), 작은 가방, 유명한 그림 (un tableau célèbre).', 'Adjective + (으)ㄴ + noun, in the present: 큰 집 (a big house), 작은 가방, 유명한 그림 (a famous painting).'),
      ], [
        G('gram-ko-eun-mod', '-(으)ㄴ (+ nom)', None, '-(eu)n', ('que j’ai… (passé) ; qui est… (adjectif)', 'that I … (past); that is … (adjective)')),
        V('ko-yennal', '옛날', None, 'yennal', ('autrefois, jadis', 'the old days, long ago')),
        V('ko-wang', '왕', None, 'wang', ('roi', 'king')),
        V('ko-yumyeonghada', '유명하다', None, 'yumyeonghada', ('être célèbre', 'to be famous')),
        V('ko-oraedoeda', '오래되다', None, 'oraedoeda', ('être ancien, vieux (choses)', 'to be old (of things)')),
        V('ko-geurim', '그림', None, 'geurim', ('tableau, dessin', 'picture, painting')),
      ], [
        ex('어제 본 영화가 정말 재미있었어요.', None, 'Le film que j’ai vu hier était vraiment bien.', 'The film I saw yesterday was really good.'),
        ex('여기는 옛날 왕이 책을 읽은 곳이에요.', None, 'C’est ici qu’un roi d’autrefois lisait ses livres.', 'This is where a king of old read his books.'),
      ], [
        FB(CHOOSE, '어제 ＿ 영화가 재미있었어요.', ['본', '보는', '볼'], '본', ('어제 : action passée → -(으)ㄴ.', '어제: past action → -(으)ㄴ.'), ('Le film que j’ai vu hier était intéressant.', 'The film I saw yesterday was good.')),
        FB(CHOOSE, '이것은 아주 ＿ 그림이에요.', ['유명한', '유명하는', '유명할'], '유명한', ('Adjectif devant un nom : -(으)ㄴ.', 'Adjective before a noun: -(으)ㄴ.'), ('C’est un tableau très célèbre.', 'This is a very famous painting.')),
        FB(CHOOSE, '여기는 아주 ＿ 도서관이에요.', ['오래된', '오래되는', '오래될'], '오래된', ('오래되다 : état acquis → 오래된 (ancien).', '오래되다: resulting state → 오래된 (old).'), ('C’est une très vieille bibliothèque.', 'This is a very old library.')),
        TF('옛날에 이 도서관에는 왕의 책이 있었어요.', ('Autrefois, cette bibliothèque contenait les livres du roi.', 'Long ago, this library held the king’s books.'), VRAI, ('옛날에 = autrefois ; 왕의 책 = les livres du roi.', '옛날에 = long ago; 왕의 책 = the king’s books.')),
      ]),
    L('ko-eul-mod', ('Ce que je vais lire : -(으)ㄹ', 'What I will read: -(으)ㄹ'), ('Décrire un nom avec une action à venir.', 'Describe a noun with an action still to come.'), 8, [
        ('Verbe + (으)ㄹ + nom pour une action future ou prévue : 내일 볼 영화, 방학에 읽을 책, 친구에게 줄 선물.', 'Verb + (으)ㄹ + noun for a future or planned action: 내일 볼 영화, 방학에 읽을 책, 친구에게 줄 선물.'),
        ('Expressions courantes : 할 일 (choses à faire), 먹을 것 (de quoi manger), -(으)ㄹ 계획이에요 (j’ai prévu de).', 'Common expressions: 할 일 (things to do), 먹을 것 (something to eat), -(으)ㄹ 계획이에요 (I plan to).'),
      ], [
        G('gram-ko-eul-mod', '-(으)ㄹ (+ nom)', None, '-(eu)l', ('que je vais… (futur, devant un nom)', 'that I will… (future, before a noun)')),
        V('ko-gyehoek', '계획', None, 'gyehoek', ('projet, plan', 'plan')),
        V('ko-banghak', '방학', None, 'banghak', ('vacances scolaires', 'school holidays')),
        V('ko-seonmul', '선물', None, 'seonmul', ('cadeau', 'present, gift')),
        V('ko-sada', '사다', None, 'sada', ('acheter', 'to buy')),
        V('ko-mulgeon', '물건', None, 'mulgeon', ('objet, chose', 'thing, item')),
      ], [
        ex('방학에 읽을 책을 세 권 샀어요.', None, 'J’ai acheté trois livres à lire pendant les vacances.', 'I bought three books to read over the holidays.'),
        ex('오늘은 할 일이 너무 많아요.', None, 'Aujourd’hui, j’ai trop de choses à faire.', 'I have too many things to do today.'),
      ], [
        FB(CHOOSE, '방학에 ＿ 책을 샀어요.', ['읽을', '읽는', '읽은'], '읽을', ('Lecture à venir : -(으)ㄹ.', 'Reading still to come: -(으)ㄹ.'), ('J’ai acheté des livres à lire pendant les vacances.', 'I bought books to read during the holidays.')),
        FB(CHOOSE, '친구에게 줄 ＿을 사요.', ['선물', '계획', '방학'], '선물', ('줄 선물 = un cadeau à offrir.', '줄 선물 = a present to give.'), ('J’achète un cadeau pour un ami.', 'I’m buying a present for a friend.')),
        DC(('Minji te demande tes projets de vacances.', 'Minji asks about your holiday plans.'), [('민지', '방학 계획이 있어요?')], ('Minji te demande si tu as des projets pour les vacances.', 'Minji asks if you have plans for the holidays.'), ['네, 부산에 갈 계획이에요.', '네, 부산에 간 계획이에요.', '아니요, 방학이에요.'], '네, 부산에 갈 계획이에요.', ('Projet à venir : 갈 계획이에요.', 'Future plan: 갈 계획이에요.')),
        TF('오늘은 할 일이 많아요.', ('La personne n’a rien à faire aujourd’hui.', 'The speaker has nothing to do today.'), FAUX, ('할 일이 많아요 = j’ai beaucoup de choses à faire.', '할 일이 많아요 = I have a lot to do.')),
      ]),
  ])])

# ═════════════════════════ Île 5 : Jeju et les haenyeo ═════════════════════════
W5 = WORLD('topik2-w5', ('Jeju, l’île des plongeuses', 'Jeju, island of the divers'), REGION,
  ('Situer dans le temps : avant, après, quand, pendant.', 'Placing events in time: before, after, when, while.'),
  (('Grand-mère Seolmundae', 'Grandmother Seolmundae'), '설', ('La géante qui a créé Jeju avec sa jupe pleine de terre raconte l’histoire de l’île. Elle attend de toi des récits bien ordonnés : avant, après, pendant.', 'The giant who made Jeju from a skirtful of earth tells the island’s story. She expects well-ordered accounts from you: before, after, while.')),
  [CH('topik2-w5-c1', ('Avant, après, pendant', 'Before, after, while'), [
    L('ko-gi-jeone', ('Avant de : -기 전에', 'Before: -기 전에'), ('Dire ce qu’on fait avant une autre action.', 'Say what you do before another action.'), 8, [
        ('Radical + -기 전에 = avant de : 자기 전에 (avant de dormir), 먹기 전에 (avant de manger).', 'Stem + -기 전에 = before (doing): 자기 전에 (before sleeping), 먹기 전에 (before eating).'),
        ('Nom + 전에 : 수업 전에 (avant le cours). Durée + 전에 = il y a : 삼 년 전에 (il y a trois ans).', 'Noun + 전에: 수업 전에 (before class). Length of time + 전에 = ago: 삼 년 전에 (three years ago).'),
      ], [
        G('gram-ko-gi-jeone', '-기 전에', None, '-gi jeone', ('avant de', 'before (doing)')),
        V('ko-haenyeo', '해녀', None, 'haenyeo', ('plongeuse de Jeju', 'Jeju woman diver')),
        V('ko-ssitda', '씻다', None, 'ssitda', ('laver', 'to wash')),
        V('ko-son', '손', None, 'son', ('main', 'hand')),
        V('ko-chulbalhada', '출발하다', None, 'chulbalhada', ('partir, se mettre en route', 'to depart, to set off')),
        V('ko-hwaginhada', '확인하다', None, 'hwaginhada', ('vérifier', 'to check')),
        V('ko-baram', '바람', None, 'baram', ('vent', 'wind')),
      ], [
        ex('해녀들은 바다에 들어가기 전에 바람을 확인해요.', None, 'Avant d’entrer dans la mer, les plongeuses vérifient le vent.', 'Before going into the sea, the divers check the wind.'),
        ex('밥을 먹기 전에 손을 씻으세요.', None, 'Lavez-vous les mains avant de manger.', 'Wash your hands before eating.'),
      ], [
        FB(CHOOSE, '밥을 먹＿ 손을 씻으세요.', ['기 전에', '은 후에', '으면서'], '기 전에', ('On se lave les mains avant de manger : -기 전에.', 'You wash your hands before eating: -기 전에.'), ('Lave-toi les mains avant de manger.', 'Wash your hands before eating.')),
        FB(CHOOSE, '출발하기 ＿ 표를 확인하세요.', ['전에', '후에', '때'], '전에', ('-기 전에 = avant de.', '-기 전에 = before.'), ('Vérifiez votre billet avant de partir.', 'Check your ticket before you set off.')),
        SO(('Remets dans l’ordre : « J’ai appris le coréen il y a trois ans. »', 'Put in order: “I learnt Korean three years ago.”'), ['삼', '년', '전에', '한국어를', '배웠어요.'], ('Durée + 전에 = il y a.', 'Length of time + 전에 = ago.')),
        TF('바다에 들어가기 전에 바람을 확인해요.', ('On vérifie le vent après être sorti de la mer.', 'You check the wind after coming out of the sea.'), FAUX, ('들어가기 전에 = avant d’entrer.', '들어가기 전에 = before going in.')),
      ]),
    L('ko-eun-hue', ('Après : -(으)ㄴ 후에', 'After: -(으)ㄴ 후에'), ('Dire ce qu’on fait après une autre action.', 'Say what you do after another action.'), 8, [
        ('Radical + -(으)ㄴ 후에 = après avoir : 먹은 후에, 끝난 후에. On dit aussi -(으)ㄴ 다음에.', 'Stem + -(으)ㄴ 후에 = after (doing): 먹은 후에, 끝난 후에. You can also say -(으)ㄴ 다음에.'),
        ('Nom + 후에 : 수업 후에 (après le cours), 식사 후에 (après le repas).', 'Noun + 후에: 수업 후에 (after class), 식사 후에 (after the meal).'),
      ], [
        G('gram-ko-eun-hue', '-(으)ㄴ 후에', None, '-(eu)n hue', ('après avoir', 'after (doing)')),
        V('ko-kkeunnada', '끝나다', None, 'kkeunnada', ('finir, se terminer', 'to end, to be over')),
        V('ko-sueop', '수업', None, 'sueop', ('cours, classe', 'class, lesson')),
        V('ko-joreophada', '졸업하다', None, 'joreophada', ('obtenir son diplôme', 'to graduate')),
        V('ko-swida', '쉬다', None, 'swida', ('se reposer', 'to rest')),
        V('ko-gyul', '귤', None, 'gyul', ('mandarine', 'tangerine')),
      ], [
        ex('수업이 끝난 후에 같이 점심 먹어요.', None, 'Déjeunons ensemble après le cours.', 'Let’s have lunch together after class.'),
        ex('물질을 한 후에 해녀들은 불 옆에서 쉬어요.', None, 'Après la plongée, les haenyeo se reposent près du feu.', 'After diving, the haenyeo rest by the fire.'),
      ], [
        FB(CHOOSE, '수업이 ＿ 후에 같이 점심 먹어요.', ['끝난', '끝나는', '끝날'], '끝난', ('Après : -(으)ㄴ 후에.', 'After: -(으)ㄴ 후에.'), ('Déjeunons ensemble après le cours.', 'Let’s have lunch together after class.')),
        FB(CHOOSE, '대학교를 ＿ 후에 회사에 들어갔어요.', ['졸업한', '졸업하는', '졸업할'], '졸업한', ('졸업하다 → 졸업한 후에.', '졸업하다 → 졸업한 후에.'), ('Après mon diplôme, je suis entré dans une entreprise.', 'After graduating, I joined a company.')),
        DC(('Ton ami veut fixer l’heure du rendez-vous.', 'Your friend wants to set a time to meet.'), [('친구', '언제 만날까요?')], ('Ton ami te demande quand vous vous voyez.', 'Your friend asks when you should meet.'), ['수업이 끝난 후에 만나요.', '수업이 끝난 후에 만났어요.', '수업 전에 만났어요.'], '수업이 끝난 후에 만나요.', ('On propose un moment à venir : 끝난 후에 만나요.', 'You suggest a future time: 끝난 후에 만나요.')),
        TF('바다에서 나온 후에 귤을 먹었어요.', ('La personne a mangé une mandarine avant d’aller dans l’eau.', 'The speaker ate a tangerine before going into the water.'), FAUX, ('나온 후에 = après être sorti.', '나온 후에 = after coming out.')),
      ]),
    L('ko-eul-ttae', ('Quand et pendant : -(으)ㄹ 때, -(으)면서', 'When and while: -(으)ㄹ 때, -(으)면서'), ('Dire quand une chose arrive, ou deux actions en même temps.', 'Say when something happens, or two actions at once.'), 9, [
        ('-(으)ㄹ 때 = quand, lorsque : 어릴 때 (quand j’étais petit), 비가 올 때 (quand il pleut). Nom + 때 : 방학 때, 점심 때.', '-(으)ㄹ 때 = when: 어릴 때 (when I was little), 비가 올 때 (when it rains). Noun + 때: 방학 때, 점심 때.'),
        ('-(으)면서 = en faisant, tout en : deux actions en même temps, avec le même sujet. 음악을 들으면서 공부해요.', '-(으)면서 = while (doing): two actions at once, with the same subject. 음악을 들으면서 공부해요.'),
      ], [
        G('gram-ko-eul-ttae', '-(으)ㄹ 때', None, '-(eu)l ttae', ('quand', 'when')),
        G('gram-ko-myeonseo', '-(으)면서', None, '-(eu)myeonseo', ('en (faisant), tout en', 'while (doing)')),
        V('ko-eorida', '어리다', None, 'eorida', ('être jeune (enfant)', 'to be young (a child)')),
        V('ko-eumak', '음악', None, 'eumak', ('musique', 'music')),
        V('ko-utda', '웃다', None, 'utda', ('rire, sourire', 'to laugh, to smile')),
        V('ko-iyagihada', '이야기하다', None, 'iyagihada', ('parler, raconter', 'to talk, to tell')),
      ], [
        ex('어릴 때 제주도에 살았어요.', None, 'Quand j’étais petit, je vivais à Jeju.', 'When I was little, I lived on Jeju.'),
        ex('해녀들은 웃으면서 이야기해요.', None, 'Les haenyeo bavardent en riant.', 'The haenyeo chat and laugh.'),
      ], [
        FB(CHOOSE, '＿ 때 제주도에 살았어요.', ['어릴', '어린', '어리는'], '어릴', ('Quand : -(으)ㄹ 때 → 어릴 때.', 'When: -(으)ㄹ 때 → 어릴 때.'), ('Quand j’étais petit, je vivais à Jeju.', 'When I was little, I lived on Jeju.')),
        FB(CHOOSE, '밥을 먹＿ 텔레비전을 봐요.', ['으면서', '을 때', '기 전에'], '으면서', ('Deux actions en même temps : -(으)면서.', 'Two actions at once: -(으)면서.'), ('Je regarde la télévision en mangeant.', 'I watch TV while eating.')),
        SO(('Remets dans l’ordre : « Quand il pleut, je reste à la maison. »', 'Put in order: “When it rains, I stay at home.”'), ['비가', '올', '때', '집에', '있어요.'], ('Proposition avec -(으)ㄹ 때, puis la phrase principale.', 'Clause with -(으)ㄹ 때, then the main clause.')),
        TF('해녀들은 웃으면서 이야기해요.', ('Les haenyeo parlent en riant.', 'The haenyeo talk while laughing.'), VRAI, ('웃으면서 = en riant.', '웃으면서 = while laughing.')),
      ]),
  ])])

# ═════════════════════════ Île 6 : le village de Hahoe ═════════════════════════
W6 = WORLD('topik2-w6', ('Le village des masques', 'The village of masks'), REGION,
  ('Faire des hypothèses, dire ce qu’on compte faire, promettre et décider.', 'Make hypotheses, say what you intend to do, promise and decide.'),
  (('L’esprit du masque de Hahoe', 'The Spirit of the Hahoe Mask'), '탈', ('Ce masque de bois au grand sourire danse depuis huit siècles. Il veut savoir ce que tu ferais si…, ce que tu comptes faire et ce que tu promets.', 'This broadly smiling wooden mask has been dancing for eight centuries. It wants to know what you would do if…, what you plan to do and what you promise.')),
  [CH('topik2-w6-c1', ('Si, pour, promis', 'If, in order to, promise'), [
    L('ko-myeon', ('Si : -(으)면', 'If: -(으)면'), ('Exprimer une condition avec -(으)면.', 'Express a condition with -(으)면.'), 8, [
        ('-(으)면 = si, quand : -으면 après une consonne (있으면), -면 après une voyelle ou ㄹ (가면, 만들면).', '-(으)면 = if, when: -으면 after a consonant (있으면), -면 after a vowel or ㄹ (가면, 만들면).'),
        ('La conséquence suit : 시간이 있으면 같이 가요 (si tu as le temps, allons-y ensemble).', 'The result follows: 시간이 있으면 같이 가요 (if you have time, let’s go together).'),
      ], [
        G('gram-ko-myeon', '-(으)면', None, '-(eu)myeon', ('si, quand (condition)', 'if, when (condition)')),
        V('ko-don', '돈', None, 'don', ('argent', 'money')),
        V('ko-maeul', '마을', None, 'maeul', ('village', 'village')),
        V('ko-tal', '탈', None, 'tal', ('masque (traditionnel)', 'mask (traditional)')),
        V('ko-chum', '춤', None, 'chum', ('danse', 'dance')),
        V('ko-chuda', '추다', None, 'chuda', ('danser (une danse)', 'to dance (a dance)')),
        V('ko-manta', '많다', None, 'manta', ('être nombreux, y avoir beaucoup', 'to be many, to be a lot')),
      ], [
        ex('시간이 있으면 같이 탈춤을 봐요.', None, 'Si tu as le temps, allons voir la danse des masques.', 'If you have time, let’s go and watch the mask dance.'),
        ex('돈이 많으면 세계 여행을 하고 싶어요.', None, 'Si j’avais beaucoup d’argent, j’aimerais faire le tour du monde.', 'If I had lots of money, I’d like to travel the world.'),
      ], [
        FB(CHOOSE, '시간이 ＿ 같이 탈춤을 봐요.', ['있으면', '있면', '있어서면'], '있으면', ('있 finit par une consonne : -으면.', '있 ends with a consonant: -으면.'), ('Si tu as le temps, allons voir la danse des masques.', 'If you have time, let’s go and watch the mask dance.')),
        FB(CHOOSE, '돈이 많＿ 세계 여행을 하고 싶어요.', ['으면', '면', '어도'], '으면', ('많 finit par une consonne : -으면.', '많 ends with a consonant: -으면.'), ('Si j’avais beaucoup d’argent, je voudrais voyager dans le monde entier.', 'If I had a lot of money, I would like to travel the world.')),
        DC(('Vous prévoyez une sortie au village demain.', 'You are planning a trip to the village tomorrow.'), [('준호', '내일 비가 오면 어떻게 해요?')], ('Junho te demande ce que tu feras s’il pleut demain.', 'Junho asks what you will do if it rains tomorrow.'), ['비가 오면 집에서 쉴 거예요.', '비가 와서 쉬었어요.', '비가 오면 안 돼요.'], '비가 오면 집에서 쉴 거예요.', ('Condition -(으)면 + projet au futur.', 'Condition -(으)면 + future plan.')),
        TF('마을에 가면 탈춤을 볼 수 있어요.', ('Si on va au village, on peut voir la danse des masques.', 'If you go to the village, you can see the mask dance.'), VRAI, ('가면 = si on y va ; 볼 수 있어요 = on peut voir.', '가면 = if you go; 볼 수 있어요 = you can see.')),
      ]),
    L('ko-ryeogo', ('Avoir l’intention de : -(으)려고 해요', 'Intending to: -(으)려고 해요'), ('Dire ce qu’on compte faire et dans quel but.', 'Say what you intend to do and why.'), 9, [
        ('-(으)려고 해요 = je compte, j’ai l’intention de : -으려고 après une consonne (먹으려고), -려고 après une voyelle ou ㄹ (가려고, 만들려고).', '-(으)려고 해요 = I intend to, I’m planning to: -으려고 after a consonant (먹으려고), -려고 after a vowel or ㄹ (가려고, 만들려고).'),
        ('Devant un autre verbe, -(으)려고 indique le but : 한국어를 배우려고 한국에 왔어요 (je suis venu en Corée pour apprendre le coréen).', 'Before another verb, -(으)려고 gives the purpose: 한국어를 배우려고 한국에 왔어요 (I came to Korea to learn Korean).'),
      ], [
        G('gram-ko-ryeogo', '-(으)려고 하다', None, '-(eu)ryeogo hada', ('avoir l’intention de, compter', 'to intend to, to plan to')),
        V('ko-baeuda', '배우다', None, 'baeuda', ('apprendre', 'to learn')),
        V('ko-isahada', '이사하다', None, 'isahada', ('déménager', 'to move (house)')),
        V('ko-chwijikhada', '취직하다', None, 'chwijikhada', ('trouver un emploi', 'to get a job')),
        V('ko-olhae', '올해', None, 'olhae', ('cette année', 'this year')),
        V('ko-yeolsimhi', '열심히', None, 'yeolsimhi', ('avec ardeur, sérieusement', 'hard, diligently')),
      ], [
        ex('올해는 한국어를 열심히 배우려고 해요.', None, 'Cette année, je compte apprendre le coréen sérieusement.', 'This year I intend to study Korean hard.'),
        ex('한국 회사에 취직하려고 한국어를 공부해요.', None, 'J’étudie le coréen pour trouver un emploi dans une entreprise coréenne.', 'I’m studying Korean to get a job at a Korean company.'),
      ], [
        FB(CHOOSE, '올해 한국어를 열심히 ＿ 해요.', ['배우려고', '배우으려고', '배워려고'], '배우려고', ('배우 finit par une voyelle : -려고.', '배우 ends with a vowel: -려고.'), ('Cette année, je compte apprendre le coréen sérieusement.', 'This year I intend to study Korean hard.')),
        FB(CHOOSE, '한국 회사에 ＿ 한국어를 공부해요.', ['취직하려고', '취직했으려고', '취직하으려고'], '취직하려고', ('But : -(으)려고, jamais au passé.', 'Purpose: -(으)려고, never in the past.'), ('J’étudie le coréen pour travailler dans une entreprise coréenne.', 'I study Korean to get a job at a Korean company.')),
        DC(('Minji te demande ce que tu fais ce week-end.', 'Minji asks what you are doing this weekend.'), [('민지', '주말에 뭐 할 거예요?')], ('Minji te demande ce que tu vas faire ce week-end.', 'Minji asks what you will do at the weekend.'), ['이사하려고 해요.', '이사했어요.', '이사할 수 없었어요.'], '이사하려고 해요.', ('Projet : -(으)려고 해요.', 'Plan: -(으)려고 해요.')),
        TF('다음 달에 이사하려고 해요.', ('La personne a déménagé le mois dernier.', 'The speaker moved last month.'), FAUX, ('다음 달에 이사하려고 해요 = je compte déménager le mois prochain.', '다음 달에 이사하려고 해요 = I plan to move next month.')),
      ]),
    L('ko-eulgeyo', ('Promettre et décider : -(으)ㄹ게요, -기로 했어요', 'Promising and deciding: -(으)ㄹ게요, -기로 했어요'), ('S’engager auprès de quelqu’un et annoncer une décision.', 'Commit to someone and announce a decision.'), 9, [
        ('-(으)ㄹ게요 = je vais…, promis : un engagement pris envers la personne à qui l’on parle. Toujours à la 1re personne : 제가 할게요, 내일 연락할게요.', '-(으)ㄹ게요 = I will…, I promise: a commitment made to the person you are talking to. Always first person: 제가 할게요, 내일 연락할게요.'),
        ('-기로 했어요 = j’ai (nous avons) décidé de : 같이 여행하기로 했어요. Avec 약속하다 : 다시 만나기로 약속했어요.', '-기로 했어요 = I (we) decided to: 같이 여행하기로 했어요. With 약속하다: 다시 만나기로 약속했어요.'),
      ], [
        G('gram-ko-eulgeyo', '-(으)ㄹ게요', None, '-(eu)lgeyo', ('je vais…, promis (engagement envers l’autre)', 'I will… (promise to the listener)')),
        G('gram-ko-giro-hada', '-기로 하다', None, '-giro hada', ('décider de', 'to decide to')),
        V('ko-yaksok', '약속', None, 'yaksok', ('promesse ; rendez-vous', 'promise; appointment')),
        V('ko-yeollakhada', '연락하다', None, 'yeollakhada', ('contacter, donner des nouvelles', 'to contact, to get in touch')),
        V('ko-kkok', '꼭', None, 'kkok', ('absolument, sans faute', 'definitely, without fail')),
        V('ko-dasi', '다시', None, 'dasi', ('de nouveau, encore', 'again')),
        V('ko-naenyeon', '내년', None, 'naenyeon', ('l’année prochaine', 'next year')),
      ], [
        ex('도착하면 꼭 연락할게요.', None, 'Je te donne des nouvelles dès que j’arrive, promis.', 'I’ll be sure to get in touch when I arrive.'),
        ex('친구하고 내년에 같이 여행하기로 했어요.', None, 'Mon ami et moi avons décidé de voyager ensemble l’année prochaine.', 'My friend and I decided to travel together next year.'),
      ], [
        FB(CHOOSE, '도착하면 꼭 ＿.', ['연락할게요', '연락할까요', '연락하세요요'], '연락할게요', ('Promesse faite à l’autre : -(으)ㄹ게요.', 'Promise to the listener: -(으)ㄹ게요.'), ('Je t’appelle dès que j’arrive, promis.', 'I’ll definitely get in touch when I arrive.')),
        FB(CHOOSE, '친구하고 내년에 같이 여행하＿ 했어요.', ['기로', '기 전에', '면서'], '기로', ('Décision : -기로 했어요.', 'Decision: -기로 했어요.'), ('Mon ami et moi avons décidé de voyager ensemble l’année prochaine.', 'My friend and I decided to travel together next year.')),
        DC(('Avant que tu sortes, ta mère te parle.', 'As you go out, your mother speaks to you.'), [('엄마', '늦지 마!')], ('Ta mère te dit de ne pas rentrer tard.', 'Your mother tells you not to be late.'), ['네, 일찍 올게요.', '네, 일찍 왔어요.', '일찍 오세요.'], '네, 일찍 올게요.', ('On rassure avec une promesse : 올게요.', 'You reassure with a promise: 올게요.')),
        TF('우리는 다시 만나기로 약속했어요.', ('Ils ont promis de se revoir.', 'They promised to meet again.'), VRAI, ('만나기로 약속했어요 = ils se sont promis de se revoir.', '만나기로 약속했어요 = they promised to meet.')),
      ]),
  ])])

# ═════════════════════════ Île 7 : la maison des ancêtres ═════════════════════════
W7 = WORLD('topik2-w7', ('La maison des ancêtres', 'The ancestral house'), REGION,
  ('Parler des aînés avec respect : l’honorifique -(으)시-, les verbes de respect, 께 et 드리다.', 'Speak about elders with respect: the honorific -(으)시-, respectful verbs, 께 and 드리다.'),
  (('Le Phénix Bonghwang', 'The Bonghwang Phoenix'), '봉', ('Cet oiseau royal n’apparaît qu’aux époques de paix et de respect. Parle des aînés avec les mots qui leur conviennent, et il déploiera ses ailes.', 'This royal bird appears only in times of peace and respect. Speak about elders with the words they deserve, and it will spread its wings.')),
  [CH('topik2-w7-c1', ('Le respect dans la langue', 'Respect in the language'), [
    L('ko-eusi', ('L’honorifique : -(으)시-, 께서', 'The honorific: -(으)시-, 께서'), ('Montrer du respect envers la personne dont on parle.', 'Show respect for the person you are talking about.'), 9, [
        ('Quand le sujet est une personne respectée (un aîné, un professeur, un client), on ajoute -(으)시- au verbe : 가세요 (il va), 읽으세요 (elle lit), 가셨어요 (il est allé).', 'When the subject is a respected person (an elder, a teacher, a customer), you add -(으)시- to the verb: 가세요 (he goes), 읽으세요 (she reads), 가셨어요 (he went).'),
        ('La particule sujet devient 께서 (au lieu de 이/가) : 할머니께서 신문을 읽으세요.', 'The subject particle becomes 께서 (instead of 이/가): 할머니께서 신문을 읽으세요.'),
        ('On ne l’utilise jamais pour soi-même.', 'You never use it about yourself.'),
      ], [
        G('gram-ko-eusi', '-(으)시-', None, '-(eu)si-', ('marque de respect envers le sujet', 'honorific marker (respect for the subject)')),
        G('gram-ko-kkeseo', '께서', None, 'kkeseo', ('particule sujet de respect', 'honorific subject particle')),
        V('ko-halmeoni', '할머니', None, 'halmeoni', ('grand-mère', 'grandmother')),
        V('ko-harabeoji', '할아버지', None, 'harabeoji', ('grand-père', 'grandfather')),
        V('ko-sajangnim', '사장님', None, 'sajangnim', ('patron, directeur', 'company president, boss')),
        V('ko-sinmun', '신문', None, 'sinmun', ('journal', 'newspaper')),
        V('ko-yojeum', '요즘', None, 'yojeum', ('ces temps-ci', 'these days')),
      ], [
        ex('할아버지께서 마당에서 신문을 읽으세요.', None, 'Grand-père lit le journal dans la cour.', 'Grandfather is reading the newspaper in the yard.'),
        ex('사장님은 어제 부산에 가셨어요.', None, 'Le directeur est allé à Busan hier.', 'The boss went to Busan yesterday.'),
      ], [
        PC(CHOOSE, '할아버지＿ 신문을 읽으세요.', ['께서', '께', '에서'], '께서', ('Sujet respecté : 께서.', 'Respected subject: 께서.'), ('Grand-père lit le journal.', 'Grandfather is reading the newspaper.')),
        FB(CHOOSE, '사장님은 어제 부산에 ＿.', ['가셨어요', '가세었어요', '갔으세요'], '가셨어요', ('Passé de respect : -(으)셨어요.', 'Honorific past: -(으)셨어요.'), ('Le directeur est allé à Busan hier.', 'The boss went to Busan yesterday.')),
        DC(('Un ami demande des nouvelles de ta grand-mère.', 'A friend asks about your grandmother.'), [('친구', '할머니는 요즘 어떻게 지내세요?')], ('Ton ami demande comment va ta grand-mère ces temps-ci.', 'Your friend asks how your grandmother is these days.'), ['잘 지내세요.', '잘 지냈어요?', '안녕히 주무세요.'], '잘 지내세요.', ('On parle de la grand-mère avec -(으)시- : 지내세요.', 'You talk about grandmother with -(으)시-: 지내세요.')),
        TF('할머니께서 요즘 바쁘세요.', ('La grand-mère est occupée ces temps-ci.', 'Grandmother is busy these days.'), VRAI, ('바쁘세요 = elle est occupée (respect).', '바쁘세요 = she is busy (honorific).')),
      ]),
    L('ko-hon-verbs', ('Les verbes de respect : 드시다, 주무시다, 계시다', 'Respectful verbs: 드시다, 주무시다, 계시다'), ('Utiliser les verbes et les noms spéciaux du respect.', 'Use the special respectful verbs and nouns.'), 9, [
        ('Certains verbes changent complètement : 먹다/마시다 → 드시다, 자다 → 주무시다, 있다 (être quelque part) → 계시다.', 'Some verbs change completely: 먹다/마시다 → 드시다, 자다 → 주무시다, 있다 (to be somewhere) → 계시다.'),
        ('Certains noms aussi : 말 → 말씀 (paroles), 나이 → 연세 (âge), 밥 → 진지 (repas).', 'Some nouns too: 말 → 말씀 (words), 나이 → 연세 (age), 밥 → 진지 (meal).'),
        ('안녕히 주무세요 = bonne nuit (à un aîné). 진지 드세요 = mangez, je vous en prie.', '안녕히 주무세요 = good night (to an elder). 진지 드세요 = please eat.'),
      ], [
        G('gram-ko-honorific-verbs', '드시다 · 주무시다 · 계시다', None, 'deusida · jumusida · gyesida', ('manger, dormir, être (formes de respect)', 'to eat, to sleep, to be (respectful forms)')),
        V('ko-deusida', '드시다', None, 'deusida', ('manger, boire (respect)', 'to eat, to drink (honorific)')),
        V('ko-jumusida', '주무시다', None, 'jumusida', ('dormir (respect)', 'to sleep (honorific)')),
        V('ko-gyesida', '계시다', None, 'gyesida', ('être, se trouver (respect)', 'to be somewhere (honorific)')),
        V('ko-malsseum', '말씀', None, 'malsseum', ('paroles (respect)', 'words, speech (honorific)')),
        V('ko-yeonse', '연세', None, 'yeonse', ('âge (respect)', 'age (honorific)')),
        V('ko-jinji', '진지', None, 'jinji', ('repas (respect)', 'meal (honorific)')),
      ], [
        ex('할아버지, 진지 드세요.', None, 'Grand-père, à table, je vous en prie.', 'Grandfather, please have your meal.'),
        ex('할머니께서는 방에서 주무세요.', None, 'Grand-mère dort dans sa chambre.', 'Grandmother is sleeping in her room.'),
      ], [
        FB(CHOOSE, '할아버지, 진지 ＿.', ['드세요', '먹으세요', '먹어요'], '드세요', ('Pour un aîné, 먹다 devient 드시다 → 드세요.', 'For an elder, 먹다 becomes 드시다 → 드세요.'), ('Grand-père, mangez, je vous en prie.', 'Grandfather, please eat.')),
        FB(CHOOSE, '할머니께서 방에서 ＿.', ['주무세요', '자세요', '자요'], '주무세요', ('자다 → 주무시다 pour un aîné.', '자다 → 주무시다 for an elder.'), ('Grand-mère dort dans sa chambre.', 'Grandmother is sleeping in her room.')),
        DC(('Un client entre dans le bureau et demande le directeur, qui est absent.', 'A customer comes into the office and asks for the boss, who is out.'), [('손님', '사장님 계세요?')], ('Le client demande si le directeur est là.', 'The customer asks whether the boss is in.'), ['지금 안 계세요.', '지금 안 있어요.', '지금 주무셨어요.'], '지금 안 계세요.', ('있다 → 계시다 pour une personne respectée.', '있다 → 계시다 for a respected person.')),
        TF('할아버지 연세가 어떻게 되세요?', ('On demande poliment l’âge du grand-père.', 'Someone politely asks grandfather’s age.'), VRAI, ('연세 = âge (respect).', '연세 = age (honorific).')),
      ]),
    L('ko-deurida', ('Donner à un aîné : 께, 드리다', 'Giving to an elder: 께, 드리다'), ('Offrir et demander poliment à une personne respectée.', 'Give to and ask a respected person politely.'), 8, [
        ('Pour une personne respectée, 에게/한테 (à) devient 께, et 주다 (donner) devient 드리다 : 어머니께 선물을 드렸어요.', 'For a respected person, 에게/한테 (to) becomes 께, and 주다 (to give) becomes 드리다: 어머니께 선물을 드렸어요.'),
        ('Demander à un aîné : 여쭤보다. Au Nouvel An (설날), on fait le 세배 aux aînés, qui offrent du 용돈.', 'To ask an elder: 여쭤보다. At the Lunar New Year (설날), you bow (세배) to your elders, who give pocket money (용돈).'),
      ], [
        G('gram-ko-kke-deurida', '께 드리다', None, 'kke deurida', ('donner à (une personne respectée)', 'to give to (a respected person)')),
        V('ko-deurida', '드리다', None, 'deurida', ('donner, offrir (respect)', 'to give (honorific)')),
        V('ko-yeojjwoboda', '여쭤보다', None, 'yeojjwoboda', ('demander (à un aîné)', 'to ask (a respected person)')),
        V('ko-sebae', '세배', None, 'sebae', ('salut du Nouvel An', 'New Year’s bow')),
        V('ko-seollal', '설날', None, 'seollal', ('Nouvel An lunaire', 'Lunar New Year')),
        V('ko-yongdon', '용돈', None, 'yongdon', ('argent de poche', 'pocket money')),
        V('ko-bumonim', '부모님', None, 'bumonim', ('parents (respect)', 'parents (honorific)')),
      ], [
        ex('설날에 할아버지께 세배를 드렸어요.', None, 'Au Nouvel An, j’ai fait le salut à mon grand-père.', 'At New Year I bowed to my grandfather.'),
        ex('모르는 것은 선생님께 여쭤보세요.', None, 'Ce que tu ne sais pas, demande-le au professeur.', 'Ask the teacher about anything you don’t know.'),
      ], [
        PC(CHOOSE, '부모님＿ 편지를 드렸어요.', ['께', '께서', '에서'], '께', ('Destinataire respecté : 께.', 'Respected recipient: 께.'), ('J’ai donné une lettre à mes parents.', 'I gave my parents a letter.')),
        FB(CHOOSE, '할머니께 선물을 ＿.', ['드렸어요', '주셨어요', '주무셨어요'], '드렸어요', ('Je donne à un aîné : 드리다 → 드렸어요.', 'I give to an elder: 드리다 → 드렸어요.'), ('J’ai offert un cadeau à ma grand-mère.', 'I gave my grandmother a present.')),
        SO(('Remets dans l’ordre : « Au Nouvel An, j’ai fait le salut à mon grand-père. »', 'Put in order: “At New Year I bowed to my grandfather.”'), ['설날에', '할아버지께', '세배를', '드렸어요.'], ('Moment + destinataire (께) + objet + 드렸어요.', 'Time + recipient (께) + object + 드렸어요.')),
        TF('설날에 세배를 하면 용돈을 받아요.', ('Au Nouvel An, après le salut, on reçoit de l’argent de poche.', 'At New Year, after bowing, you receive pocket money.'), VRAI, ('세배를 하면 용돈을 받아요 = si on fait le salut, on reçoit de l’argent de poche.', '세배를 하면 용돈을 받아요 = if you bow, you receive pocket money.')),
      ]),
  ])])

# ═════════════════════════ Île 8 : la forteresse de Suwon ═════════════════════════
W8 = WORLD('topik2-w8', ('La forteresse de Suwon', 'Suwon Fortress'), REGION,
  ('Comparer, faire des suppositions et maîtriser les verbes irréguliers.', 'Compare, make guesses and master irregular verbs.'),
  (('Le Tigre blanc', 'The White Tiger'), '백', ('Le tigre blanc dont parlait la rumeur garde les remparts de Hwaseong. Il compare, devine et tend des pièges de conjugaison : à toi de lui répondre juste.', 'The white tiger of the rumour guards the ramparts of Hwaseong. It compares, guesses and sets conjugation traps: answer it correctly.')),
  [CH('topik2-w8-c1', ('Comparer et supposer', 'Comparing and guessing'), [
    L('ko-boda', ('Comparer : 보다 (더), 제일', 'Comparing: 보다 (더), 제일'), ('Comparer deux choses et dire laquelle est la plus…', 'Compare two things and say which is the most…'), 8, [
        ('A이/가 B보다 (더) + adjectif = A est plus … que B : 서울이 부산보다 (더) 커요.', 'A이/가 B보다 (더) + adjective = A is more … than B: 서울이 부산보다 (더) 커요.'),
        ('제일 ou 가장 + adjectif = le plus : 한라산이 한국에서 제일 높아요. Pour demander : A하고 B 중에서 뭐가 더 좋아요?', '제일 or 가장 + adjective = the most: 한라산이 한국에서 제일 높아요. To ask: A하고 B 중에서 뭐가 더 좋아요?'),
      ], [
        G('gram-ko-boda', '보다 (더)', None, 'boda (deo)', ('plus… que', 'more… than')),
        G('gram-ko-jeil', '제일, 가장', None, 'jeil, gajang', ('le plus', 'the most')),
        V('ko-seong', '성', None, 'seong', ('forteresse, château', 'fortress, castle')),
        V('ko-nopda', '높다', None, 'nopda', ('être haut', 'to be high, to be tall')),
        V('ko-neolda', '넓다', None, 'neolda', ('être vaste, large', 'to be wide, to be spacious')),
        V('ko-gilda', '길다', None, 'gilda', ('être long', 'to be long')),
        V('ko-jjalda', '짧다', None, 'jjalda', ('être court', 'to be short')),
      ], [
        ex('수원 화성은 생각보다 더 넓어요.', None, 'La forteresse Hwaseong de Suwon est plus vaste que je ne le pensais.', 'Suwon’s Hwaseong Fortress is bigger than I thought.'),
        ex('한라산은 한국에서 제일 높은 산이에요.', None, 'Le Hallasan est la plus haute montagne de Corée du Sud.', 'Hallasan is the highest mountain in South Korea.'),
      ], [
        PC(CHOOSE, '기차가 버스＿ 더 빨라요.', ['보다', '하고', '에서'], '보다', ('Comparaison : B보다 (더).', 'Comparison: B보다 (더).'), ('Le train est plus rapide que le bus.', 'The train is faster than the bus.')),
        FB(CHOOSE, '우리 반에서 민수가 키가 ＿ 커요.', ['제일', '보다', '하고'], '제일', ('Le plus : 제일.', 'The most: 제일.'), ('Dans notre classe, c’est Minsu le plus grand.', 'Minsu is the tallest in our class.')),
        DC(('Ton ami te demande ta saison préférée.', 'Your friend asks your favourite season.'), [('친구', '여름하고 겨울 중에서 뭐가 더 좋아요?')], ('Ton ami te demande ce que tu préfères, l’été ou l’hiver.', 'Your friend asks which you prefer, summer or winter.'), ['저는 겨울이 더 좋아요.', '네, 겨울이에요.', '여름에 갔어요.'], '저는 겨울이 더 좋아요.', ('On répond avec 더 (plus).', 'You answer with 더 (more).')),
        TF('한라산은 한국에서 제일 높은 산이에요.', ('Le Hallasan est la plus haute montagne de Corée du Sud.', 'Hallasan is the highest mountain in South Korea.'), VRAI, ('제일 높은 = le plus haut.', '제일 높은 = the highest.')),
      ]),
    L('ko-geot-gatayo', ('Il me semble : -(으)ㄹ 것 같아요', 'It seems: -(으)ㄹ 것 같아요'), ('Faire une supposition ou adoucir son avis.', 'Make a guess or soften an opinion.'), 9, [
        ('-(으)ㄹ 것 같아요 = je pense que…, on dirait que… (pour l’avenir ou ce qu’on ne voit pas) : 비가 올 것 같아요.', '-(으)ㄹ 것 같아요 = I think…, it looks like… (for the future or what you can’t see): 비가 올 것 같아요.'),
        ('Pour ce qui se passe en ce moment : verbe + -는 것 같아요 (자는 것 같아요). Avec un adjectif : -(으)ㄴ 것 같아요 (바쁜 것 같아요).', 'For what is happening now: verb + -는 것 같아요 (자는 것 같아요). With an adjective: -(으)ㄴ 것 같아요 (바쁜 것 같아요).'),
        ('Les Coréens l’emploient aussi pour donner un avis avec douceur : 이게 더 좋은 것 같아요.', 'Koreans also use it to give an opinion gently: 이게 더 좋은 것 같아요.'),
      ], [
        G('gram-ko-geot-gatayo', '-(으)ㄹ 것 같아요', None, '-(eu)l geot gatayo', ('je pense que…, on dirait que…', 'I think…, it looks like…')),
        V('ko-ama', '아마', None, 'ama', ('sans doute, probablement', 'probably')),
        V('ko-gureum', '구름', None, 'gureum', ('nuage', 'cloud')),
        V('ko-museopda', '무섭다', None, 'museopda', ('faire peur ; avoir peur', 'to be scary; to be afraid')),
        V('ko-joyonghada', '조용하다', None, 'joyonghada', ('être calme, silencieux', 'to be quiet')),
        V('ko-sori', '소리', None, 'sori', ('bruit, son', 'sound, noise')),
      ], [
        ex('구름이 많아요. 아마 비가 올 것 같아요.', None, 'Il y a beaucoup de nuages. Il va sans doute pleuvoir.', 'There are lots of clouds. It will probably rain.'),
        ex('조용하네요. 아이가 자는 것 같아요.', None, 'C’est calme. On dirait que l’enfant dort.', 'It’s quiet. The child seems to be asleep.'),
      ], [
        FB(CHOOSE, '구름이 많아요. 비가 ＿ 것 같아요.', ['올', '와', '오고'], '올', ('Supposition sur l’avenir : -(으)ㄹ 것 같아요.', 'Guess about the future: -(으)ㄹ 것 같아요.'), ('Il y a beaucoup de nuages. Il va pleuvoir, je crois.', 'There are lots of clouds. I think it’s going to rain.')),
        FB(CHOOSE, '조용해요. 아이가 자＿ 것 같아요.', ['는', '어', '고'], '는', ('Ce qui se passe maintenant : -는 것 같아요.', 'What is happening now: -는 것 같아요.'), ('C’est calme. On dirait que l’enfant dort.', 'It’s quiet. The child seems to be asleep.')),
        DC(('Vous choisissez un film à voir ce soir.', 'You are choosing a film to watch tonight.'), [('친구', '이 영화 무서울 것 같아요?')], ('Ton ami te demande si, d’après toi, ce film va faire peur.', 'Your friend asks if you think this film will be scary.'), ['네, 좀 무서울 것 같아요.', '아니요, 영화예요.', '영화를 봐야 해요.'], '네, 좀 무서울 것 같아요.', ('On répond par une supposition : -(으)ㄹ 것 같아요.', 'You answer with a guess: -(으)ㄹ 것 같아요.')),
        TF('밖에서 소리가 나요. 누가 온 것 같아요.', ('La personne pense que quelqu’un est arrivé.', 'The speaker thinks someone has arrived.'), VRAI, ('온 것 같아요 = on dirait que quelqu’un est venu.', '온 것 같아요 = it seems someone has come.')),
      ]),
    L('ko-irregular', ('Les irréguliers : ㄷ, 르 et ㅡ', 'Irregular verbs: ㄷ, 르 and ㅡ'), ('Conjuguer les verbes irréguliers les plus courants.', 'Conjugate the most common irregular verbs.'), 10, [
        ('ㄷ → ㄹ devant une voyelle : 듣다 → 들어요, 걷다 → 걸어요, 묻다 → 물어요. Mais 닫다 → 닫아요 reste régulier.', 'ㄷ → ㄹ before a vowel: 듣다 → 들어요, 걷다 → 걸어요, 묻다 → 물어요. But 닫다 → 닫아요 stays regular.'),
        ('르 → ㄹㄹ : 모르다 → 몰라요, 빠르다 → 빨라요, 부르다 → 불러요.', '르 → ㄹㄹ: 모르다 → 몰라요, 빠르다 → 빨라요, 부르다 → 불러요.'),
        ('Le ㅡ final tombe : 바쁘다 → 바빠요, 쓰다 → 써요, 크다 → 커요.', 'A final ㅡ drops: 바쁘다 → 바빠요, 쓰다 → 써요, 크다 → 커요.'),
      ], [
        G('gram-ko-d-irregular', 'ㄷ → ㄹ : 들어요', None, 'd → l : deureoyo', ('verbes irréguliers en ㄷ', 'irregular ㄷ verbs')),
        G('gram-ko-reu-irregular', '르 → ㄹㄹ : 몰라요', None, 'reu → ll : mollayo', ('verbes irréguliers en 르', 'irregular 르 verbs')),
        V('ko-deutda', '듣다', None, 'deutda', ('écouter, entendre', 'to listen, to hear')),
        V('ko-geotda', '걷다', None, 'geotda', ('marcher', 'to walk')),
        V('ko-mutda', '묻다', None, 'mutda', ('demander, poser une question', 'to ask (a question)')),
        V('ko-moreuda', '모르다', None, 'moreuda', ('ne pas savoir', 'not to know')),
        V('ko-ppareuda', '빠르다', None, 'ppareuda', ('être rapide', 'to be fast')),
        V('ko-bureuda', '부르다', None, 'bureuda', ('appeler ; chanter', 'to call; to sing (a song)')),
      ], [
        ex('저는 성벽 위를 걸으면서 음악을 들어요.', None, 'Je marche sur les remparts en écoutant de la musique.', 'I walk along the ramparts listening to music.'),
        ex('죄송해요. 저도 잘 몰라요. 저 사람에게 물어보세요.', None, 'Désolé, je ne sais pas non plus. Demandez à cette personne-là.', 'Sorry, I don’t know either. Ask that person over there.'),
      ], [
        FB(CHOOSE, '저는 매일 한국 노래를 ＿.', ['들어요', '듣어요', '들아요'], '들어요', ('듣다 : ㄷ → ㄹ devant une voyelle → 들어요.', '듣다: ㄷ → ㄹ before a vowel → 들어요.'), ('J’écoute des chansons coréennes tous les jours.', 'I listen to Korean songs every day.')),
        FB(CHOOSE, '죄송해요. 잘 ＿.', ['몰라요', '모라요', '모르어요'], '몰라요', ('모르다 : 르 → ㄹㄹ → 몰라요.', '모르다: 르 → ㄹㄹ → 몰라요.'), ('Désolé, je ne sais pas.', 'Sorry, I don’t know.')),
        FB(CHOOSE, '지하철이 버스보다 ＿.', ['빨라요', '빠라요', '빠르어요'], '빨라요', ('빠르다 → 빨라요.', '빠르다 → 빨라요.'), ('Le métro est plus rapide que le bus.', 'The subway is faster than the bus.')),
        TF('성벽 위를 걸어요.', ('La personne marche sur les remparts.', 'The speaker is walking on the ramparts.'), VRAI, ('걷다 → 걸어요 = je marche.', '걷다 → 걸어요 = I walk.')),
      ]),
  ])])

FINAL = {
  'slug': 'topik2-final',
  'title': t(('Simulation TOPIK I — niveau 2', 'TOPIK I simulation — level 2')),
  'region': REGION,
  'description': t(('Examen blanc au format du TOPIK I, avec plus de questions difficiles : il faut 140 points sur 200 pour obtenir le niveau 2 et valider l’île.', 'Mock exam in TOPIK I format, with more difficult questions: you need 140 points out of 200 to reach level 2 and clear the island.')),
  'exam': 'topik2-official',
  'chapters': [],
}

level = {
  'contentVersion': '2026.11.20',
  'level': {'code': 'TOPIK2', 'title': t(('Élémentaire : raconter et expliquer en coréen', 'Elementary: telling and explaining in Korean')), 'region': REGION, 'order': 15},
  'notice': t(('Les listes de vocabulaire de Koto Quest sont alignées sur les compétences attendues au TOPIK I (niveau 2) mais ne constituent pas des listes officielles du TOPIK.', 'Koto Quest’s vocabulary lists are aligned with the skills expected at TOPIK I (level 2) but are not official TOPIK lists.')),
  'worlds': [W1, W2, W3, W4, W5, W6, W7, W8, FINAL],
}
t((REGION, 'Land of Tales'))
os.makedirs(os.path.join(ROOT, 'content/topik2'), exist_ok=True)
check_and_write(level, 'content/topik2/topik2.json', ['content/n5/n5.json', 'content/n4/n4.json', 'content/n3/n3.json', 'content/n2/n2.json', 'content/n1/n1.json', 'content/topik1/topik1.json'])
