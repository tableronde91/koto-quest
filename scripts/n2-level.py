# Niveau N2 : 8 îles, 24 leçons et un examen blanc (français + anglais).
# Usage : python3 scripts/n2-level.py   (réécrit content/n2/n2.json)
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from kq_content import *

REGION = 'Capitale d’été'
ORDER = lambda fr, en: (f'Remets la phrase dans l’ordre : « {fr} »', f'Put the sentence in order: “{en}”')

# ═════════════════════════ Île 1 : points de vue et sources ═════════════════════════
W1 = WORLD('n2-w1', ('Points de vue et sources', 'Standpoints and sources'), REGION,
  ('Juger depuis un point de vue, transmettre une information et dire sur quoi l’on se fonde.', 'Judge from a standpoint, pass on information, and say what you are basing yourself on.'),
  (('La Nue aux Quatre Visages', 'The Four-Faced Nue'), '鵺', ('Tête de singe, corps de tanuki, pattes de tigre, queue de serpent : la Nue change selon l’endroit d’où on la regarde. D’après qui, et vu d’où ?', 'A monkey’s head, a tanuki’s body, a tiger’s legs, a snake’s tail: the Nue changes depending on where you look from. According to whom, and seen from where?')),
  [CH('n2-w1-c1', ('Juger et rapporter', 'Judging and reporting'), [
    L('n2-kara-suru-to', ('Du point de vue de… : 〜からすると・〜から見ると', 'From the standpoint of…: 〜からすると・〜から見ると'), ('Juger une situation depuis un point de vue ou à partir d’un indice.', 'Judge a situation from a standpoint or from a clue.'), 10, [
        ('Nom + からすると / からすれば = du point de vue de, à en juger par : 親からすると、子どもは いつまでも 子どもだ.', 'Noun + からすると / からすれば = from the standpoint of, judging from: 親からすると、子どもは いつまでも 子どもだ.'),
        ('Nom + から見ると / から見て / から見れば a le même sens : 私から見ると. Attention, 〜から言うと ne suit pas directement une personne : 親の 立場から言うと.', 'Noun + から見ると / から見て / から見れば means the same: 私から見ると. Note that 〜から言うと cannot directly follow a person: 親の 立場から言うと.'),
        ('Avec un indice, on en tire une déduction : あの 話し方からすると、彼は 関西の 人だろう.', 'With a clue, you draw a conclusion from it: あの 話し方からすると、彼は 関西の 人だろう.'),
      ], [
        G('gram-n2-kara-suru-to', '〜からすると', '〜からすると', '~kara suru to', ('du point de vue de… ; à en juger par…', 'from the standpoint of… ; judging from…')),
        G('gram-n2-kara-miru-to', '〜から見ると', '〜からみると', '~kara miru to', ('vu depuis…, aux yeux de…', 'seen from…, in the eyes of…')),
        V('vocab-tachiba', '立場', 'たちば', 'tachiba', ('position, point de vue (de quelqu’un)', 'position, standpoint')),
        V('vocab-senmonka', '専門家', 'せんもんか', 'senmonka', ('spécialiste, expert', 'specialist, expert')),
        V('vocab-shouhisha', '消費者', 'しょうひしゃ', 'shouhisha', ('consommateur', 'consumer')),
        V('vocab-hyouka', '評価', 'ひょうか', 'hyouka', ('évaluation, appréciation', 'evaluation, assessment')),
        K('kanji-n2-han', '判', 'はん', 'han', ('juger, sceau', 'judge, seal'), ['ハン', 'バン'], [], 7),
        K('kanji-n2-hyou', '評', 'ひょう', 'hyou', ('critique, jugement porté', 'critique, appraisal'), ['ヒョウ'], [], 12),
      ], [
        ex('親からすると、子どもは いくつに なっても 心配な ものです。', 'おやからすると、こどもは いくつに なっても しんぱいな ものです。', 'Du point de vue des parents, on s’inquiète pour ses enfants quel que soit leur âge.', 'From a parent’s standpoint, children are a worry however old they get.'),
        ex('専門家から見ると、この 計画には 問題が 多いそうです。', 'せんもんかから みると、この けいかくには もんだいが おおいそうです。', 'Aux yeux des spécialistes, ce projet poserait beaucoup de problèmes.', 'In the eyes of specialists, this plan apparently has many problems.'),
      ], [
        FB(CHOOSE, 'あの 話し方＿、彼は 関西の 人だろう。', ['からすると', 'からには', 'からこそ'], 'からすると', ('Indice + からすると = à en juger par.', 'Clue + からすると = judging from.'), ('À en juger par sa façon de parler, il doit être du Kansai.', 'Judging from the way he talks, he must be from Kansai.')),
        PC(COMPLETE, '消費者の 立場＿ 言うと、値段は 安い ほうが いい。', ['から', 'まで', 'ので'], 'から', ('〜の 立場から言うと = du point de vue de.', '〜の 立場から言うと = from the standpoint of.'), ('Du point de vue du consommateur, mieux vaut un prix bas.', 'From the consumer’s standpoint, a lower price is better.')),
        SO(ORDER('Vu par un étranger, cette coutume est étonnante.', 'Seen by a foreigner, this custom is surprising.'), ['外国人', 'から見ると', 'この 習慣は', '不思議です'], ('Nom + から見ると, puis le jugement.', 'Noun + から見ると, then the judgement.')),
        TF('私から見ると、彼の 評価は 低すぎると 思います。', ('La personne trouve que cette évaluation est juste.', 'The speaker thinks the evaluation is fair.'), FAUX, ('低すぎる = trop basse : à ses yeux, l’évaluation est injuste.', '低すぎる = too low: in the speaker’s eyes, the evaluation is unfair.')),
      ]),
    L('n2-to-no-koto', ('On me dit que… : 〜とのことだ・〜ということだ', 'I am told that…: 〜とのことだ・〜ということだ'), ('Transmettre une information ou un message reçu, dans un registre soigné.', 'Pass on information or a message you received, in a careful register.'), 10, [
        ('Phrase à la forme neutre + とのことだ = on m’a dit que, il est indiqué que. Sert à transmettre un message : 部長は 少し 遅れるとの ことです.', 'Plain-form sentence + とのことだ = I was told that, it says that. Used to pass on a message: 部長は 少し 遅れるとの ことです.'),
        ('〜ということだ rapporte une information entendue ou lue, souvent avec 〜によると (d’après) : ニュースによると、台風が 来るという ことだ.', '〜ということだ reports something heard or read, often with 〜によると (according to): ニュースによると、台風が 来るという ことだ.'),
        ('〜ということだ peut aussi tirer une conclusion : つまり、中止という ことですね (autrement dit, c’est annulé).', '〜ということだ can also draw a conclusion: つまり、中止という ことですね (in other words, it is cancelled).'),
      ], [
        G('gram-n2-to-no-koto', '〜とのことだ', '〜とのことだ', '~to no koto da', ('on me dit que…, il est indiqué que…', 'I am told that…, it says that…')),
        G('gram-n2-to-iu-koto', '〜ということだ', '〜ということだ', '~to iu koto da', ('à ce qu’on dit… ; cela veut dire que…', 'I hear that… ; that means…')),
        V('vocab-houkoku', '報告', 'ほうこく', 'houkoku', ('rapport, compte rendu', 'report (account)')),
        V('vocab-higai', '被害', 'ひがい', 'higai', ('dégâts, dommages', 'damage, harm')),
        V('vocab-happyou', '発表', 'はっぴょう', 'happyou', ('annonce, présentation', 'announcement, presentation')),
        V('vocab-enki', '延期', 'えんき', 'enki', ('report (à plus tard)', 'postponement')),
        K('kanji-n2-hou', '報', 'ほう', 'hou', ('informer, nouvelle', 'inform, news'), ['ホウ'], ['むく(いる)'], 12),
        K('kanji-n2-koku', '告', 'こく', 'koku', ('annoncer, déclarer', 'announce, declare'), ['コク'], ['つ(げる)'], 7),
      ], [
        ex('山本さんから 電話が ありました。少し 遅れるとの ことです。', 'やまもとさんから でんわが ありました。すこし おくれるとの ことです。', 'M. Yamamoto a téléphoné. Il aura un peu de retard, m’a-t-il dit.', 'Mr Yamamoto phoned. He says he will be a little late.'),
        ex('発表によると、試合は 来週に 延期されたという ことです。', 'はっぴょうによると、しあいは らいしゅうに えんきされたという ことです。', 'D’après l’annonce, le match a été reporté à la semaine prochaine.', 'According to the announcement, the match has been postponed to next week.'),
      ], [
        FB(CHOOSE, 'ニュース＿、台風の 被害は 大きいという ことだ。', ['によると', 'について', 'にとって'], 'によると', ('Source de l’information : 〜によると.', 'Source of the information: 〜によると.'), ('D’après les informations, les dégâts du typhon seraient importants.', 'According to the news, the typhoon damage is said to be severe.')),
        FB(COMPLETE, '先生は 今日 お休みだ＿ ことです。', ['との', 'ような', 'ための'], 'との', ('Message transmis : forme neutre + とのことです.', 'A passed-on message: plain form + とのことです.'), ('On me dit que le professeur est absent aujourd’hui.', 'I am told the teacher is off today.')),
        DC(('Ton chef demande si le client a appelé. Tu transmets le message.', 'Your boss asks whether the client called. You pass on the message.'), [('部長', '田中さんから 連絡は ありましたか。')], ('Le chef demande si M. Tanaka a donné des nouvelles.', 'The boss asks whether Mr Tanaka has been in touch.'), ['はい。報告は 明日 届くとの ことです。', 'はい。報告は 明日 届く ことに します。', 'はい。報告は 明日 届く つもりです。'], 'はい。報告は 明日 届くとの ことです。', ('〜とのことです transmet ce que l’autre a dit.', '〜とのことです passes on what the other person said.')),
        TF('つまり、会議は 中止という ことですね。', ('La personne vérifie qu’elle a bien compris : la réunion est annulée.', 'The speaker is checking their understanding: the meeting is cancelled.'), VRAI, ('つまり〜ということですね = autrement dit…, c’est bien ça ?', 'つまり〜ということですね = in other words…, is that right?')),
      ]),
    L('n2-ni-motozuite', ('Sur la base de… : 〜に基づいて・〜をもとに', 'On the basis of…: 〜に基づいて・〜をもとに'), ('Dire sur quoi reposent une décision, un récit ou une création.', 'Say what a decision, a story or a creation is based on.'), 10, [
        ('Nom + に基づいて = en se fondant sur (une règle, des données, un fait) : 調査の 結果に 基づいて 決めます. Devant un nom : 〜に基づいた / 〜に基づく.', 'Noun + に基づいて = on the basis of (a rule, data, a fact): 調査の 結果に 基づいて 決めます. Before a noun: 〜に基づいた / 〜に基づく.'),
        ('Nom + をもとに(して) = à partir de, en prenant pour matériau : 事実を もとに 書かれた 小説.', 'Noun + をもとに(して) = starting from, using as material: 事実を もとに 書かれた 小説.'),
        ('Nuance : に基づいて reste fidèle à sa base (loi, données) ; をもとに s’en inspire pour créer autre chose.', 'Nuance: に基づいて stays faithful to its basis (law, data); をもとに draws on it to create something else.'),
      ], [
        G('gram-n2-ni-motozuite', '〜に基づいて', '〜にもとづいて', '~ni motozuite', ('en se fondant sur…', 'based on…, in accordance with…')),
        G('gram-n2-wo-moto-ni', '〜をもとに', '〜をもとに', '~wo moto ni', ('à partir de…, en s’inspirant de…', 'using… as a basis, drawing on…')),
        V('vocab-chousa', '調査', 'ちょうさ', 'chousa', ('enquête, étude', 'survey, investigation')),
        V('vocab-kekka', '結果', 'けっか', 'kekka', ('résultat', 'result')),
        V('vocab-jijitsu', '事実', 'じじつ', 'jijitsu', ('fait (réel)', 'fact')),
        V('vocab-keiken', '経験', 'けいけん', 'keiken', ('expérience (vécue)', 'experience')),
        K('kanji-n2-moto', '基', 'もと', 'moto', ('base, fondement', 'base, foundation'), ['キ'], ['もと', 'もと(づく)'], 11),
        K('kanji-n2-jun', '準', 'じゅん', 'jun', ('norme, niveau', 'standard, level'), ['ジュン'], [], 13),
      ], [
        ex('この 映画は 事実に 基づいて 作られました。', 'この えいがは じじつに もとづいて つくられました。', 'Ce film a été réalisé d’après des faits réels.', 'This film was made based on real events.'),
        ex('留学の 経験を もとに、本を 書きました。', 'りゅうがくの けいけんを もとに、ほんを かきました。', 'J’ai écrit un livre à partir de mon expérience d’études à l’étranger.', 'I wrote a book drawing on my experience of studying abroad.'),
      ], [
        PC(COMPLETE, '調査の 結果＿ 基づいて、計画を 変えました。', ['に', 'を', 'で'], 'に', ('〜に 基づいて.', '〜に 基づいて.'), ('Nous avons modifié le projet en nous fondant sur les résultats de l’enquête.', 'We changed the plan based on the results of the survey.')),
        PC(COMPLETE, 'この 歌は 古い 話＿ もとに 作られた。', ['を', 'に', 'が'], 'を', ('〜を もとに.', '〜を もとに.'), ('Cette chanson a été composée à partir d’une vieille histoire.', 'This song was written from an old story.')),
        FB(COMPLETE, 'これは 規則に ＿ 決定です。', ['基づいた', '基づいて', 'もとに'], '基づいた', ('Devant un nom : 〜に基づいた + nom.', 'Before a noun: 〜に基づいた + noun.'), ('C’est une décision fondée sur le règlement.', 'This is a decision based on the rules.')),
        TF('この ドラマは 作者の 経験を もとに して います。', ('L’histoire s’inspire de ce que l’auteur a vécu.', 'The story draws on what the author lived through.'), VRAI, ('経験を もとに = à partir de son expérience.', '経験を もとに = drawing on experience.')),
      ]),
  ])])

# ═════════════════════════ Île 2 : l'instant précis ═════════════════════════
W2 = WORLD('n2-w2', ('L’instant précis', 'The exact moment'), REGION,
  ('Dire qu’une chose arrive à peine une autre finie, à une occasion solennelle ou en plein milieu d’une action.', 'Say that something happens the instant another ends, on a formal occasion, or right in the middle of an action.'),
  (('La Lanterne aux Aguets', 'The Watchful Lantern'), '瞬', ('Cette lanterne-fantôme ouvre l’œil à l’instant même où tu baisses la garde. À peine as-tu commencé ta phrase qu’elle a déjà changé de place.', 'This ghost lantern opens its eye the very instant you drop your guard. You have barely begun your sentence and it has already moved.')),
  [CH('n2-w2-c1', ('À peine, lors de, en plein', 'No sooner, on the occasion of, in the middle of'), [
    L('n2-ta-totan', ('À peine… que… : 〜たとたん・〜かと思うと', 'No sooner… than…: 〜たとたん・〜かと思うと'), ('Dire qu’un événement inattendu suit immédiatement un autre.', 'Say that an unexpected event follows straight after another.'), 10, [
        ('Verbe en た + とたん(に) = à l’instant où, à peine… que. La suite est soudaine et involontaire : 立ち上がったとたん、めまいが した.', 'た-form verb + とたん(に) = the very moment, no sooner… than. What follows is sudden and involuntary: 立ち上がったとたん、めまいが した.'),
        ('Verbe en た + かと思うと / かと思ったら = on croit à peine que… et déjà… ; le changement surprend celui qui observe : 空が 暗く なったかと思うと、雨が 降り出した.', 'た-form verb + かと思うと / かと思ったら = you have barely registered… when already…; the change surprises the observer: 空が 暗く なったかと思うと、雨が 降り出した.'),
        ('Ces deux formes décrivent ce qu’on constate : on ne les emploie ni pour ses propres actions voulues, ni pour un ordre ou une intention.', 'Both forms describe what you observe: they are not used for your own deliberate actions, nor with an order or an intention.'),
      ], [
        G('gram-n2-ta-totan', '〜たとたん（に）', '〜たとたん（に）', '~ta totan (ni)', ('à l’instant même où…', 'the very moment…')),
        G('gram-n2-ka-to-omou-to', '〜かと思うと', '〜かとおもうと', '~ka to omou to', ('à peine… que déjà…', 'no sooner… than…')),
        V('vocab-tachiagarimasu', '立ち上がります', 'たちあがります', 'tachiagarimasu', ('se mettre debout', 'to stand up')),
        V('vocab-memai', 'めまい', 'めまい', 'memai', ('vertige', 'dizziness')),
        V('vocab-totsuzen', '突然', 'とつぜん', 'totsuzen', ('soudain, tout à coup', 'suddenly')),
        V('vocab-kaminari', '雷', 'かみなり', 'kaminari', ('tonnerre, foudre', 'thunder, lightning')),
        K('kanji-n2-shun', '瞬', 'しゅん', 'shun', ('instant, cligner', 'instant, blink'), ['シュン'], ['またた(く)'], 18),
        K('kanji-n2-tsuku', '突', 'つく', 'tsuku', ('heurter, surgir', 'thrust, burst out'), ['トツ'], ['つ(く)'], 8),
      ], [
        ex('立ち上がったとたんに、めまいが しました。', 'たちあがったとたんに、めまいが しました。', 'À l’instant où je me suis mis debout, j’ai eu un vertige.', 'The moment I stood up, I felt dizzy.'),
        ex('空が 暗く なったかと思うと、突然 雷が 鳴りました。', 'そらが くらく なったかとおもうと、とつぜん かみなりが なりました。', 'À peine le ciel s’était-il assombri que le tonnerre a soudain grondé.', 'No sooner had the sky gone dark than thunder suddenly rumbled.'),
      ], [
        FB(CHOOSE, 'ドアを ＿とたん、猫が 外へ 飛び出した。', ['開けた', '開ける', '開けて'], '開けた', ('とたん suit la forme en た.', 'とたん follows the た-form.'), ('À l’instant où j’ai ouvert la porte, le chat a bondi dehors.', 'The moment I opened the door, the cat shot outside.')),
        FB(CHOOSE, '赤ちゃんは 泣いた＿、もう 笑って いる。', ['かと思うと', 'とたんで', 'あいだに'], 'かと思うと', ('Changement rapide qu’on observe : 〜たかと思うと.', 'A quick change you observe: 〜たかと思うと.'), ('Le bébé pleurait à peine qu’il rit déjà.', 'The baby had no sooner cried than it is already laughing.')),
        TF('家に 帰ったとたん、勉強を 始める つもりです。', ('Cette phrase est naturelle en japonais.', 'This sentence is natural Japanese.'), FAUX, ('〜たとたん ne s’emploie pas avec une intention : la suite doit être un fait soudain, déjà constaté.', '〜たとたん is not used with an intention: what follows must be a sudden fact already observed.')),
        SO(ORDER('À l’instant où je suis sorti, il s’est mis à pleuvoir.', 'The moment I went out, it started to rain.'), ['外に', '出た', 'とたん', '雨が', '降り出した'], ('Verbe en た + とたん, puis l’événement soudain.', 'た-form verb + とたん, then the sudden event.')),
      ]),
    L('n2-sai', ('Lors de… : 〜際（に）・〜に際して', 'On the occasion of…: 〜際（に）・〜に際して'), ('Parler d’une occasion dans un registre formel : annonces, guichets, contrats.', 'Talk about an occasion in a formal register: announcements, counters, contracts.'), 10, [
        ('〜際(に) = lorsque, à l’occasion de ; c’est le とき des annonces et des documents. Verbe (dictionnaire ou た) + 際 ; nom + の + 際 : お降りの 際は、足元に ご注意ください.', '〜際(に) = when, on the occasion of; it is the とき of announcements and documents. Verb (dictionary or た-form) + 際; noun + の + 際: お降りの 際は、足元に ご注意ください.'),
        ('Nom / verbe au dictionnaire + に際して = au moment d’entreprendre (un événement important, qui n’arrive pas tous les jours) : 契約に 際して、説明を 受けました.', 'Noun / dictionary-form verb + に際して = on the occasion of undertaking (an important event that does not happen every day): 契約に 際して、説明を 受けました.'),
        ('〜に際して ne s’emploie que pour ce qui va commencer ; 〜際 convient aussi pour le passé : 先日 お会いした 際に.', '〜に際して is only used for what is about to begin; 〜際 also works for the past: 先日 お会いした 際に.'),
      ], [
        G('gram-n2-sai', '〜際（に）', '〜さい（に）', '~sai (ni)', ('lors de…, à l’occasion de… (formel)', 'when…, on the occasion of… (formal)')),
        G('gram-n2-ni-saishite', '〜に際して', '〜にさいして', '~ni saishite', ('au moment d’entreprendre…', 'on the occasion of undertaking…')),
        V('vocab-keiyaku', '契約', 'けいやく', 'keiyaku', ('contrat', 'contract')),
        V('vocab-mibunshoumeisho', '身分証明書', 'みぶんしょうめいしょ', 'mibunshoumeisho', ('pièce d’identité', 'identity document')),
        V('vocab-hijouguchi', '非常口', 'ひじょうぐち', 'hijouguchi', ('sortie de secours', 'emergency exit')),
        V('vocab-moushikomi', '申し込み', 'もうしこみ', 'moushikomi', ('demande, inscription', 'application, sign-up')),
        K('kanji-n2-sai', '際', 'さい', 'sai', ('occasion, bord', 'occasion, edge'), ['サイ'], ['きわ'], 14),
        K('kanji-n2-kei', '契', 'けい', 'kei', ('engagement, pacte', 'pledge, pact'), ['ケイ'], ['ちぎ(る)'], 9),
      ], [
        ex('お申し込みの 際は、身分証明書が 必要です。', 'おもうしこみの さいは、みぶんしょうめいしょが ひつようです。', 'Lors de l’inscription, une pièce d’identité est nécessaire.', 'When applying, an identity document is required.'),
        ex('契約に 際して、いくつか 注意して いただきたい ことが あります。', 'けいやくに さいして、いくつか ちゅういして いただきたい ことが あります。', 'Au moment de signer le contrat, je vous demanderai de faire attention à quelques points.', 'On signing the contract, there are a few points I would ask you to note.'),
      ], [
        FB(CHOOSE, '非常の ＿は、この 非常口を ご利用ください。', ['際', '間', '最中'], '際', ('Nom + の + 際 : formule d’annonce.', 'Noun + の + 際: an announcement formula.'), ('En cas d’urgence, veuillez utiliser cette sortie de secours.', 'In an emergency, please use this emergency exit.')),
        PC(COMPLETE, '出発＿ 際して、先生が あいさつを しました。', ['に', 'を', 'で'], 'に', ('〜に 際して.', '〜に 際して.'), ('Au moment du départ, le professeur a dit quelques mots.', 'On our departure, the teacher said a few words.')),
        TF('お帰りの 際は、忘れ物に ご注意ください。', ('C’est une phrase qu’on entend plutôt dans une annonce qu’entre amis.', 'This is a sentence you would hear in an announcement rather than between friends.'), VRAI, ('〜際 est formel : entre amis, on dirait 帰る とき.', '〜際 is formal: between friends you would say 帰る とき.')),
        DC(('Au guichet, un client demande ce qu’il faut apporter pour s’inscrire.', 'At the counter, a customer asks what to bring to sign up.'), [('客', '申し込みには 何が 必要ですか。')], ('Le client demande ce qui est nécessaire pour l’inscription.', 'The customer asks what is needed to apply.'), ['お申し込みの 際は、身分証明書を お持ちください。', 'お申し込みの とたん、身分証明書を お持ちください。', 'お申し込みの 最中、身分証明書を お持ちください。'], 'お申し込みの 際は、身分証明書を お持ちください。', ('Occasion formelle : 〜の 際は.', 'A formal occasion: 〜の 際は.')),
      ]),
    L('n2-saichuu', ('En plein… : 〜最中に・〜ところに', 'Right in the middle of…: 〜最中に・〜ところに'), ('Dire qu’un événement survient au beau milieu d’une action.', 'Say that something happens right in the middle of an action.'), 10, [
        ('Verbe en ている / nom + の + 最中(に) = en plein milieu de : 会議の 最中に 停電に なった. Ce qui arrive dérange souvent l’action.', 'ている-form verb / noun + の + 最中(に) = right in the middle of: 会議の 最中に 停電に なった. What happens often disrupts the action.'),
        ('Verbe + ところに / ところへ = juste au moment où (quelqu’un ou quelque chose arrive) : 出かけようと した ところへ、客が 来た.', 'Verb + ところに / ところへ = just as (someone or something arrives): 出かけようと した ところへ、客が 来た.'),
        ('〜ところを s’emploie dans des formules d’excuse ou de remerciement : お忙しい ところを すみません (désolé de vous déranger en plein travail).', '〜ところを is used in set phrases of apology or thanks: お忙しい ところを すみません (sorry to disturb you when you are busy).'),
      ], [
        G('gram-n2-saichuu', '〜最中（に）', '〜さいちゅう（に）', '~saichuu (ni)', ('en plein milieu de…', 'right in the middle of…')),
        G('gram-n2-tokoro-ni', '〜ところに・〜ところへ', '〜ところに・〜ところへ', '~tokoro ni / ~tokoro e', ('juste au moment où… (quelque chose survient)', 'just as… (something turns up)')),
        V('vocab-kaigi', '会議', 'かいぎ', 'kaigi', ('réunion (de travail)', 'meeting (at work)')),
        V('vocab-teiden', '停電', 'ていでん', 'teiden', ('panne de courant', 'power cut')),
        V('vocab-jama', '邪魔', 'じゃま', 'jama', ('gêne, dérangement', 'hindrance, disturbance')),
        V('vocab-tazunemasu', '訪ねます', 'たずねます', 'tazunemasu', ('rendre visite à', 'to call on, to visit')),
        K('kanji-n2-to', '途', 'と', 'to', ('chemin, cours (des choses)', 'way, course'), ['ト'], [], 10),
        K('kanji-n2-gi', '議', 'ぎ', 'gi', ('délibérer, débat', 'deliberate, debate'), ['ギ'], [], 20),
      ], [
        ex('会議の 最中に、突然 停電に なりました。', 'かいぎの さいちゅうに、とつぜん ていでんに なりました。', 'En pleine réunion, il y a eu soudain une panne de courant.', 'Right in the middle of the meeting, there was suddenly a power cut.'),
        ex('出かけようと した ところへ、友だちが 訪ねて 来ました。', 'でかけようと した ところへ、ともだちが たずねて きました。', 'Juste au moment où j’allais sortir, un ami est venu me rendre visite.', 'Just as I was about to go out, a friend came to call.'),
      ], [
        FB(CHOOSE, '今、食事の ＿だから、後で 電話します。', ['最中', '際', 'とたん'], '最中', ('Nom + の + 最中 = en plein.', 'Noun + の + 最中 = in the middle of.'), ('Je suis en plein repas, je rappellerai plus tard.', 'I am in the middle of a meal, so I will call back later.')),
        FB(CHOOSE, '試験を ＿ 最中に、電話が 鳴って しまった。', ['受けて いる', '受ける', '受けた'], '受けて いる', ('Verbe en ている + 最中.', 'ている-form verb + 最中.'), ('Mon téléphone a sonné en plein examen.', 'My phone rang right in the middle of the exam.')),
        FB(COMPLETE, 'お忙しい ＿ すみませんが、少し よろしいですか。', ['ところを', '最中を', '際を'], 'ところを', ('お忙しい ところを すみません : formule pour s’excuser de déranger.', 'お忙しい ところを すみません: a set phrase to apologise for disturbing.'), ('Désolé de vous déranger en plein travail, auriez-vous un instant ?', 'Sorry to disturb you when you are busy, but do you have a moment?')),
        TF('ちょうど 困って いた ところに、先生が 来て くれた。', ('Le professeur est arrivé au bon moment.', 'The teacher arrived at just the right moment.'), VRAI, ('〜ところに = juste à ce moment-là ; 来て くれた montre que c’était le bienvenu.', '〜ところに = just at that moment; 来て くれた shows it was welcome.')),
      ]),
  ])])

# ═════════════════════════ Île 3 : raisons et engagements ═════════════════════════
W3 = WORLD('n2-w3', ('Raisons et engagements', 'Reasons and commitments'), REGION,
  ('Dire qu’on ira jusqu’au bout puisqu’on s’est engagé, qu’un excès entraîne une conséquence, et qu’une cause explique un résultat.', 'Say that you will see something through since you committed to it, that an excess leads to a consequence, and that a cause accounts for a result.'),
  (('La Hannya aux Serments', 'The Hannya of Vows'), '誓', ('Son masque est né d’un serment trahi. Puisque tu as promis, iras-tu jusqu’au bout ? Et que fait-on, à force d’émotion ?', 'Her mask was born of a broken vow. Since you have promised, will you see it through? And what does one do when emotion takes over?')),
  [CH('n2-w3-c1', ('Puisque, à force de, justement parce que', 'Now that, so much that, precisely because'), [
    L('n2-kara-ni-wa', ('Puisque… : 〜からには・〜以上（は）', 'Now that…: 〜からには・〜以上（は）'), ('Exprimer une conséquence qui s’impose : devoir, résolution, conseil.', 'Express a consequence that follows as a matter of course: duty, resolve, advice.'), 10, [
        ('Forme neutre + からには = puisque, du moment que ; la suite est une résolution, un devoir ou une demande : やるからには、最後まで やります.', 'Plain form + からには = now that, since; what follows is a resolve, a duty or a request: やるからには、最後まで やります.'),
        ('Forme neutre + 以上(は) a le même sens, en plus formel ; nom + である + 以上 : 学生である 以上、勉強しなければ ならない.', 'Plain form + 以上(は) means the same, more formally; noun + である + 以上: 学生である 以上、勉強しなければ ならない.'),
        ('La seconde partie contient souvent 〜べきだ, 〜なければならない, 〜つもりだ, 〜てください : jamais un simple constat.', 'The second half often contains 〜べきだ, 〜なければならない, 〜つもりだ, 〜てください: never a mere statement of fact.'),
      ], [
        G('gram-n2-kara-ni-wa', '〜からには', '〜からには', '~kara ni wa', ('puisque…, du moment que…', 'now that…, since… (so naturally)')),
        G('gram-n2-ijou-wa', '〜以上（は）', '〜いじょう（は）', '~ijou (wa)', ('dès lors que… (formel)', 'given that… (formal)')),
        V('vocab-gimu', '義務', 'ぎむ', 'gimu', ('obligation, devoir', 'obligation, duty')),
        V('vocab-hikiukemasu', '引き受けます', 'ひきうけます', 'hikiukemasu', ('accepter (une tâche), se charger de', 'to take on (a task)')),
        V('vocab-zenryoku', '全力', 'ぜんりょく', 'zenryoku', ('toutes ses forces', 'all one’s strength')),
        V('vocab-mamorimasu', '守ります', 'まもります', 'mamorimasu', ('respecter (une règle), tenir (une promesse)', 'to keep (a rule, a promise)')),
        K('kanji-n2-mu', '務', 'む', 'mu', ('tâche, fonction', 'task, function'), ['ム'], ['つと(める)'], 11),
        K('kanji-n2-makaseru', '任', 'まかせる', 'makaseru', ('confier, charge', 'entrust, charge'), ['ニン'], ['まか(せる)'], 6),
      ], [
        ex('引き受けたからには、最後まで 全力で やります。', 'ひきうけたからには、さいごまで ぜんりょくで やります。', 'Puisque j’ai accepté, je m’y consacrerai de toutes mes forces jusqu’au bout.', 'Now that I have taken it on, I will give it my all to the end.'),
        ex('約束した 以上は、守らなければ なりません。', 'やくそくした いじょうは、まもらなければ なりません。', 'Dès lors qu’on a promis, il faut tenir parole.', 'Given that you have promised, you must keep your word.'),
      ], [
        FB(CHOOSE, '日本に 来た＿、日本語を 上手に 話せるように なりたい。', ['からには', 'からでは', 'からして'], 'からには', ('Puisque… + souhait ou résolution : 〜からには.', 'Since… + wish or resolve: 〜からには.'), ('Puisque je suis venu au Japon, je veux arriver à bien parler japonais.', 'Now that I have come to Japan, I want to become able to speak Japanese well.')),
        FB(CHOOSE, '学生＿ 以上、勉強を 第一に 考えるべきだ。', ['である', 'の', 'な'], 'である', ('Nom + である + 以上.', 'Noun + である + 以上.'), ('Dès lors qu’on est étudiant, on doit faire passer les études en premier.', 'Given that you are a student, you should put your studies first.')),
        TF('試合に 出るからには、勝ちたいです。', ('La personne compte jouer sans se soucier du résultat.', 'The speaker intends to play without caring about the result.'), FAUX, ('〜からには : puisqu’elle participe, elle veut gagner.', '〜からには: since they are taking part, they want to win.')),
        SO(ORDER('Puisque c’est un devoir, il faut le respecter.', 'Since it is a duty, it must be kept.'), ['義務である', '以上は', '守らなければ', 'なりません'], ('〜である 以上は, puis l’obligation.', '〜である 以上は, then the obligation.')),
      ]),
    L('n2-amari', ('Tellement… que… : 〜あまり・あまりの〜に', 'So much that…: 〜あまり・あまりの〜に'), ('Dire qu’un sentiment ou un état excessif entraîne un résultat inattendu.', 'Say that an excessive feeling or state leads to an unexpected result.'), 10, [
        ('Nom + の + あまり / verbe au dictionnaire ou en た + あまり = tellement… que ; le résultat est souvent négatif : 緊張の あまり、何も 言えなかった.', 'Noun + の + あまり / dictionary or た-form verb + あまり = so… that; the result is often negative: 緊張の あまり、何も 言えなかった.'),
        ('あまりの + nom + に = devant un tel…, tant… : あまりの 暑さに、外へ 出られない.', 'あまりの + noun + に = faced with such…, so much…: あまりの 暑さに、外へ 出られない.'),
        ('Avec un adjectif, on le transforme en nom : うれしさの あまり、悲しみの あまり. On ne l’emploie ni avec un ordre ni avec une intention.', 'With an adjective, turn it into a noun: うれしさの あまり、悲しみの あまり. It is not used with an order or an intention.'),
      ], [
        G('gram-n2-amari', '〜あまり', '〜あまり', '~amari', ('tellement… que…, à force de…', 'so… that…, out of sheer…')),
        G('gram-n2-amari-no', 'あまりの〜に', 'あまりの〜に', 'amari no ~ ni', ('devant un(e) tel(le)…', 'because of such a…')),
        V('vocab-kinchou', '緊張', 'きんちょう', 'kinchou', ('nervosité, tension', 'nervousness, tension')),
        V('vocab-kandou', '感動', 'かんどう', 'kandou', ('émotion (être touché)', 'being moved, deep emotion')),
        V('vocab-namida', '涙', 'なみだ', 'namida', ('larme', 'tear (from crying)')),
        V('vocab-koufun', '興奮', 'こうふん', 'koufun', ('excitation', 'excitement')),
        K('kanji-n2-kin', '緊', 'きん', 'kin', ('tendu, serré', 'tense, tight'), ['キン'], [], 15),
        K('kanji-n2-kan', '感', 'かん', 'kan', ('ressentir, sensation', 'feel, sensation'), ['カン'], [], 13),
      ], [
        ex('緊張の あまり、自分の 名前も 言えませんでした。', 'きんちょうの あまり、じぶんの なまえも いえませんでした。', 'J’étais tellement nerveux que je n’ai même pas pu dire mon nom.', 'I was so nervous that I could not even say my own name.'),
        ex('あまりの 感動に、涙が 止まりませんでした。', 'あまりの かんどうに、なみだが とまりませんでした。', 'Devant une telle émotion, je ne pouvais plus arrêter mes larmes.', 'I was so moved that I could not stop my tears.'),
      ], [
        PC(COMPLETE, '心配＿ あまり、夜も 眠れなかった。', ['の', 'な', 'に'], 'の', ('Nom + の + あまり.', 'Noun + の + あまり.'), ('J’étais tellement inquiet que je n’en dormais plus la nuit.', 'I was so worried that I could not sleep at night.')),
        FB(CHOOSE, '＿ 寒さに、手が 動かなく なった。', ['あまりの', 'あまり', 'あまりに'], 'あまりの', ('あまりの + nom + に.', 'あまりの + noun + に.'), ('Il faisait un tel froid que mes mains ne bougeaient plus.', 'It was so cold that my hands stopped moving.')),
        FB(COMPLETE, '彼は 興奮した＿、大きな 声を 出して しまった。', ['あまり', 'あまりの', 'あまりで'], 'あまり', ('Verbe + あまり.', 'Verb + あまり.'), ('Dans son excitation, il s’est mis à parler très fort.', 'In his excitement, he ended up raising his voice.')),
        TF('うれしさの あまり、彼女は 泣き出した。', ('Elle a pleuré de tristesse.', 'She cried out of sadness.'), FAUX, ('うれしさの あまり = tant elle était heureuse.', 'うれしさの あまり = because she was so happy.')),
      ]),
    L('n2-bakari-ni', ('Rien que parce que…, comme attendu… : 〜ばかりに・〜だけあって', 'Simply because…, as you would expect…: 〜ばかりに・〜だけあって'), ('Regretter une cause unique qui a mal tourné, ou saluer un résultat à la hauteur.', 'Regret a single cause that turned out badly, or praise a result that lives up to expectations.'), 10, [
        ('Forme neutre + ばかりに = rien que parce que… (résultat regrettable) : 油断した ばかりに、試合に 負けた.', 'Plain form + ばかりに = simply because… (a regrettable result): 油断した ばかりに、試合に 負けた.'),
        ('Forme neutre + だけあって = comme on pouvait s’y attendre de… (éloge) : 十年 住んで いた だけあって、日本語が 上手だ. Souvent avec さすが.', 'Plain form + だけあって = as you would expect from… (praise): 十年 住んで いた だけあって、日本語が 上手だ. Often with さすが.'),
        ('〜だけに = justement parce que… ; le résultat en est d’autant plus fort, en bien ou en mal : 楽しみに して いた だけに、中止は つらい.', '〜だけに = precisely because…; the result is all the stronger for it, for better or worse: 楽しみに して いた だけに、中止は つらい.'),
      ], [
        G('gram-n2-bakari-ni', '〜ばかりに', '〜ばかりに', '~bakari ni', ('rien que parce que… (regret)', 'simply because… (regret)')),
        G('gram-n2-dake-atte', '〜だけあって', '〜だけあって', '~dake atte', ('comme on pouvait s’y attendre de…', 'as you would expect from…')),
        V('vocab-doryoku', '努力', 'どりょく', 'doryoku', ('effort', 'effort')),
        V('vocab-seiseki', '成績', 'せいせき', 'seiseki', ('résultats (scolaires), notes', 'results, grades')),
        V('vocab-yudan', '油断', 'ゆだん', 'yudan', ('relâchement, manque de vigilance', 'carelessness, lowering one’s guard')),
        V('vocab-sasuga', 'さすが', 'さすが', 'sasuga', ('c’est bien digne de…, vraiment', 'just as one would expect')),
        K('kanji-n2-do', '努', 'ど', 'do', ('s’efforcer', 'strive'), ['ド'], ['つと(める)'], 7),
        K('kanji-n2-seki', '績', 'せき', 'seki', ('exploit, résultat obtenu', 'achievement'), ['セキ'], [], 17),
      ], [
        ex('うそを 言った ばかりに、友だちを なくして しまいました。', 'うそを いった ばかりに、ともだちを なくして しまいました。', 'Rien que pour avoir menti, j’ai perdu un ami.', 'Simply because I told a lie, I lost a friend.'),
        ex('毎日 努力した だけあって、成績が 上がりました。', 'まいにち どりょくした だけあって、せいせきが あがりました。', 'Ses efforts quotidiens ont payé, comme on pouvait s’y attendre : ses notes ont monté.', 'As you would expect after working hard every day, his grades went up.'),
      ], [
        FB(CHOOSE, '油断した＿、大切な 試合に 負けて しまった。', ['ばかりに', 'だけあって', 'からには'], 'ばかりに', ('Cause unique, résultat regrettable : 〜ばかりに.', 'A single cause, a regrettable result: 〜ばかりに.'), ('Rien que pour m’être relâché, j’ai perdu un match important.', 'Simply because I let my guard down, I lost an important match.')),
        FB(CHOOSE, 'さすが 有名な 店＿、料理が おいしい。', ['だけあって', 'ばかりに', 'のあまり'], 'だけあって', ('Éloge attendu : 〜だけあって, souvent avec さすが.', 'Expected praise: 〜だけあって, often with さすが.'), ('C’est bien un restaurant réputé : la cuisine est délicieuse.', 'Just as you would expect of a famous restaurant, the food is delicious.')),
        TF('お金が ない ばかりに、旅行に 行けなかった。', ('La personne regrette de ne pas avoir pu partir.', 'The speaker regrets not having been able to go.'), VRAI, ('〜ばかりに exprime un regret : cette seule raison l’en a empêchée.', '〜ばかりに expresses regret: that one reason alone stopped them.')),
        DC(('Ton amie a réussi son examen après des mois de travail. Tu la félicites.', 'Your friend has passed her exam after months of work. You congratulate her.'), [('友だち', '試験に 合格したよ。')], ('Ton amie annonce qu’elle a réussi l’examen.', 'Your friend says she has passed the exam.'), ['おめでとう。努力した だけあって、すごいね。', 'おめでとう。努力した ばかりに、すごいね。', 'おめでとう。努力の あまり、すごいね。'], 'おめでとう。努力した だけあって、すごいね。', ('Pour un éloge : 〜だけあって. 〜ばかりに exprimerait un regret.', 'For praise: 〜だけあって. 〜ばかりに would express regret.')),
      ]),
  ])])

# ═════════════════════════ Île 4 : malgré tout ═════════════════════════
W4 = WORLD('n2-w4', ('Malgré tout', 'In spite of everything'), REGION,
  ('Opposer deux faits : malgré, bien que, alors que, contrairement à.', 'Set two facts against each other: despite, although, whereas, contrary to.'),
  (('Le Kasa-obake Contrariant', 'The Contrary Umbrella Ghost'), '逆', ('Ce parapluie-fantôme fait tout à l’envers : il s’ouvre quand il fait beau et se ferme sous l’averse. Malgré quoi ? Contrairement à quoi ?', 'This umbrella ghost does everything the wrong way round: it opens in fine weather and closes in the downpour. In spite of what? Contrary to what?')),
  [CH('n2-w4-c1', ('Malgré, bien que, alors que', 'Despite, although, whereas'), [
    L('n2-nimo-kakawarazu', ('Malgré… : 〜にもかかわらず・〜ものの', 'In spite of…: 〜にもかかわらず・〜ものの'), ('Dire qu’un résultat va à l’encontre de ce qu’on attendait.', 'Say that a result goes against what was expected.'), 10, [
        ('Nom / forme neutre + にもかかわらず = malgré, bien que (registre soigné) : 悪天候にも かかわらず、大会は 行われた.', 'Noun / plain form + にもかかわらず = in spite of, although (careful register): 悪天候にも かかわらず、大会は 行われた.'),
        ('Forme neutre + ものの = certes… mais ; on reconnaît un fait, puis on dit que la suite ne suit pas : 買った ものの、一度も 使って いない.', 'Plain form + ものの = it is true that… but; you grant a fact, then say that what should follow does not: 買った ものの、一度も 使って いない.'),
        ('Nom et adjectif en な devant ものの : 〜である ものの / 〜な ものの. La seconde partie est un constat, pas un ordre.', 'Noun and な-adjective before ものの: 〜である ものの / 〜な ものの. The second half is a statement of fact, not an order.'),
      ], [
        G('gram-n2-nimo-kakawarazu', '〜にもかかわらず', '〜にもかかわらず', '~ni mo kakawarazu', ('malgré…, bien que… (soigné)', 'in spite of…, although… (formal)')),
        G('gram-n2-monono', '〜ものの', '〜ものの', '~mono no', ('certes… mais…', 'it is true that… but…')),
        V('vocab-tenkou', '天候', 'てんこう', 'tenkou', ('conditions météo', 'weather conditions')),
        V('vocab-taikai', '大会', 'たいかい', 'taikai', ('tournoi, grand rassemblement', 'tournament, large event')),
        V('vocab-jouken', '条件', 'じょうけん', 'jouken', ('condition (à remplir)', 'condition, requirement')),
        V('vocab-kouka', '効果', 'こうか', 'kouka', ('effet, efficacité', 'effect, effectiveness')),
        K('kanji-n2-kou', '候', 'こう', 'kou', ('saison, signe', 'season, sign'), ['コウ'], ['そうろう'], 10),
        K('kanji-n2-ken', '件', 'けん', 'ken', ('affaire, cas', 'matter, case'), ['ケン'], [], 6),
      ], [
        ex('悪い 天候にも かかわらず、大会は 行われました。', 'わるい てんこうにも かかわらず、たいかいは おこなわれました。', 'Malgré le mauvais temps, le tournoi a eu lieu.', 'In spite of the bad weather, the tournament went ahead.'),
        ex('薬を 飲んだ ものの、あまり 効果が ありませんでした。', 'くすりを のんだ ものの、あまり こうかが ありませんでした。', 'J’ai bien pris le médicament, mais il n’a guère fait d’effet.', 'Although I took the medicine, it had little effect.'),
      ], [
        FB(CHOOSE, '彼は 熱が ある＿、仕事を 続けた。', ['にもかかわらず', 'からには', 'だけあって'], 'にもかかわらず', ('Fait contraire à l’attente : 〜にもかかわらず.', 'A fact contrary to expectation: 〜にもかかわらず.'), ('Bien qu’il ait de la fièvre, il a continué à travailler.', 'In spite of having a fever, he carried on working.')),
        FB(CHOOSE, '高い 辞書を 買った＿、ほとんど 使って いない。', ['ものの', 'ものを', 'ものか'], 'ものの', ('On reconnaît un fait, puis on nuance : 〜ものの.', 'You grant a fact, then qualify it: 〜ものの.'), ('J’ai bien acheté un dictionnaire cher, mais je ne m’en sers presque pas.', 'Although I bought an expensive dictionary, I hardly use it.')),
        TF('条件は いい ものの、その 仕事は 断りました。', ('La personne a accepté ce travail.', 'The speaker accepted the job.'), FAUX, ('〜ものの : les conditions sont bonnes, et pourtant elle a refusé.', '〜ものの: the conditions are good, and yet they turned it down.')),
        SO(ORDER('Malgré la pluie, beaucoup de gens sont venus.', 'In spite of the rain, many people came.'), ['雨', 'にもかかわらず', 'たくさんの 人が', '来ました'], ('Nom + にもかかわらず, puis le fait inattendu.', 'Noun + にもかかわらず, then the unexpected fact.')),
      ]),
    L('n2-ippou', ('D’un côté…, contrairement à… : 〜一方（で）・〜に反して', 'On the one hand…, contrary to…: 〜一方（で）・〜に反して'), ('Mettre en regard deux aspects, ou dire qu’un résultat contredit une attente.', 'Set two aspects side by side, or say that a result contradicts an expectation.'), 10, [
        ('Forme neutre + 一方(で) = d’un côté… de l’autre ; alors que : 人口が 減る 一方で、一人暮らしは 増えて いる.', 'Plain form + 一方(で) = on the one hand… on the other; whereas: 人口が 減る 一方で、一人暮らしは 増えて いる.'),
        ('Nom + に反して = contrairement à (une attente, une prévision, une volonté) : 予想に 反して、試験は やさしかった.', 'Noun + に反して = contrary to (an expectation, a forecast, someone’s wishes): 予想に 反して、試験は やさしかった.'),
        ('À ne pas confondre : verbe au dictionnaire + 一方だ = ne cesser de… (une tendance) : 物の 値段は 上がる 一方だ.', 'Not to be confused: dictionary-form verb + 一方だ = to keep on …ing (a trend): 物の 値段は 上がる 一方だ.'),
      ], [
        G('gram-n2-ippou-de', '〜一方（で）', '〜いっぽう（で）', '~ippou (de)', ('d’un côté… de l’autre ; alors que…', 'on the one hand… on the other; whereas…')),
        G('gram-n2-ni-hanshite', '〜に反して', '〜にはんして', '~ni hanshite', ('contrairement à…', 'contrary to…')),
        V('vocab-zouka', '増加', 'ぞうか', 'zouka', ('augmentation', 'increase')),
        V('vocab-genshou', '減少', 'げんしょう', 'genshou', ('diminution', 'decrease')),
        V('vocab-yosou', '予想', 'よそう', 'yosou', ('prévision, pronostic', 'forecast, expectation')),
        V('vocab-jinkou', '人口', 'じんこう', 'jinkou', ('population', 'population')),
        K('kanji-n2-fueru', '増', 'ふえる', 'fueru', ('augmenter, s’accroître', 'increase, grow'), ['ゾウ'], ['ふ(える)', 'ま(す)'], 14),
        K('kanji-n2-heru', '減', 'へる', 'heru', ('diminuer, se réduire', 'decrease, shrink'), ['ゲン'], ['へ(る)'], 12),
      ], [
        ex('都会の 人口が 増加する 一方で、地方では 減少して います。', 'とかいの じんこうが ぞうかする いっぽうで、ちほうでは げんしょうして います。', 'Alors que la population des grandes villes augmente, elle diminue en province.', 'While the population of the big cities is increasing, it is decreasing in the regions.'),
        ex('予想に 反して、今年の 夏は 涼しかったです。', 'よそうに はんして、ことしの なつは すずしかったです。', 'Contrairement aux prévisions, l’été a été frais cette année.', 'Contrary to expectations, this summer was cool.'),
      ], [
        FB(CHOOSE, '父は 厳しい＿、とても 優しい ところも あります。', ['一方で', '一方に', '一方を'], '一方で', ('Deux aspects en regard : 〜一方で.', 'Two aspects side by side: 〜一方で.'), ('Mon père est sévère, mais d’un autre côté il a aussi beaucoup de douceur.', 'My father is strict, but on the other hand he also has a very gentle side.')),
        PC(COMPLETE, '親の 期待＿ 反して、彼は 音楽の 道を 選んだ。', ['に', 'を', 'と'], 'に', ('〜に 反して.', '〜に 反して.'), ('Contrairement à ce qu’espéraient ses parents, il a choisi la voie de la musique.', 'Contrary to his parents’ hopes, he chose the path of music.')),
        TF('物の 値段は 上がる 一方だ。', ('Les prix montent sans cesse.', 'Prices keep going up.'), VRAI, ('Verbe au dictionnaire + 一方だ = ne cesser de…', 'Dictionary-form verb + 一方だ = to keep on …ing.')),
        FB(COMPLETE, '予想に ＿、試合は 私たちの チームが 勝った。', ['反して', '対して', '関して'], '反して', ('Contraire à une prévision : 〜に 反して.', 'Contrary to a forecast: 〜に 反して.'), ('Contre toute attente, c’est notre équipe qui a gagné le match.', 'Against all expectations, our team won the match.')),
      ]),
    L('n2-kuse-ni', ('Alors même que… : 〜くせに・〜ながら（も）', 'Even though…: 〜くせに・〜ながら（も）'), ('Reprocher une contradiction, ou reconnaître un contraste avec retenue.', 'Criticise a contradiction, or acknowledge a contrast with restraint.'), 10, [
        ('Forme neutre + くせに = alors même que… (reproche, ton familier) : 知って いる くせに、教えて くれない. Nom + の + くせに ; adjectif en な + な + くせに.', 'Plain form + くせに = even though… (reproach, casual tone): 知って いる くせに、教えて くれない. Noun + の + くせに; な-adjective + な + くせに.'),
        ('〜ながら(も) = tout en…, bien que (plus neutre, plutôt écrit) : 狭い ながらも、楽しい 我が家. Avec la base en ます, un adjectif en い ou un nom.', '〜ながら(も) = while…, although (more neutral, rather written): 狭い ながらも、楽しい 我が家. With the ます-stem, an い-adjective or a noun.'),
        ('〜くせに ne s’emploie pas pour parler de soi, et le sujet des deux parties est le même.', '〜くせに is not used about oneself, and both halves share the same subject.'),
      ], [
        G('gram-n2-kuse-ni', '〜くせに', '〜くせに', '~kuse ni', ('alors même que… (reproche)', 'even though… (reproach)')),
        G('gram-n2-nagara-mo', '〜ながら（も）', '〜ながら（も）', '~nagara (mo)', ('tout en…, bien que… (contraste)', 'while…, though… (contrast)')),
        V('vocab-mazushii', '貧しい', 'まずしい', 'mazushii', ('pauvre, démuni', 'poor, needy')),
        V('vocab-gyaku', '逆', 'ぎゃく', 'gyaku', ('inverse, à l’envers', 'reverse, the other way round')),
        V('vocab-erasou', '偉そう', 'えらそう', 'erasou', ('hautain, qui prend de grands airs', 'self-important, pompous')),
        V('vocab-shiawase', '幸せ', 'しあわせ', 'shiawase', ('heureux ; bonheur', 'happy; happiness')),
        K('kanji-n2-sakarau', '逆', 'さからう', 'sakarau', ('aller à l’encontre', 'go against'), ['ギャク'], ['さか(らう)', 'さか'], 9),
        K('kanji-n2-hin', '貧', 'ひん', 'hin', ('pauvreté, manque', 'poverty, want'), ['ヒン', 'ビン'], ['まず(しい)'], 11),
      ], [
        ex('弟は 何も 知らない くせに、偉そうに 話します。', 'おとうとは なにも しらない くせに、えらそうに はなします。', 'Mon petit frère ne sait rien, et pourtant il parle en prenant de grands airs.', 'My little brother knows nothing, and yet he talks as if he were important.'),
        ex('貧しい ながらも、家族は 幸せに 暮らして いました。', 'まずしい ながらも、かぞくは しあわせに くらして いました。', 'Bien que pauvre, la famille vivait heureuse.', 'Though poor, the family lived happily.'),
      ], [
        FB(CHOOSE, '自分で 約束した＿、彼は 来なかった。', ['くせに', 'ばかりに', 'からには'], 'くせに', ('Reproche : 〜くせに.', 'Reproach: 〜くせに.'), ('C’est lui qui avait promis, et il n’est même pas venu.', 'He was the one who promised, and yet he did not come.')),
        PC(COMPLETE, '子ども＿ くせに、大人の ような ことを 言う。', ['の', 'な', 'だ'], 'の', ('Nom + の + くせに.', 'Noun + の + くせに.'), ('Ce n’est qu’un enfant, et il parle comme un adulte.', 'He is only a child, and yet he talks like a grown-up.')),
        FB(COMPLETE, '残念＿、今回は 参加できません。', ['ながら', 'くせに', 'ばかりに'], 'ながら', ('残念ながら = malheureusement (formule figée).', '残念ながら = unfortunately (a set phrase).'), ('Malheureusement, je ne pourrai pas participer cette fois.', 'Unfortunately, I cannot take part this time.')),
        TF('この 部屋は 狭い ながらも、とても 使いやすい。', ('La personne se plaint de sa chambre.', 'The speaker is complaining about the room.'), FAUX, ('〜ながらも : petite, certes, mais très pratique. Le jugement est positif.', '〜ながらも: small, admittedly, but very practical. The judgement is positive.')),
      ]),
  ])])

# ═════════════════════════ Île 5 : bien au-delà ═════════════════════════
W5 = WORLD('n2-w5', ('Bien au-delà', 'Far beyond'), REGION,
  ('Dire qu’une chose ne se limite pas à un cas, qu’elle va à l’opposé de ce qu’on croit, ou qu’elle s’étend sur toute une durée.', 'Say that something is not limited to one case, that it is the opposite of what one thinks, or that it extends over a whole period.'),
  (('La Tsuchigumo aux Mille Fils', 'The Tsuchigumo of a Thousand Threads'), '蜘', ('Sa toile ne couvre pas seulement le jardin : elle court sur toute la ville, d’un bout à l’autre de la nuit. Jusqu’où s’étend-elle, et pendant combien de temps ?', 'Her web does not cover the garden alone: it runs across the whole city, from one end of the night to the other. How far does it reach, and for how long?')),
  [CH('n2-w5-c1', ('Pas seulement, loin de, tout au long de', 'Not only, far from, throughout'), [
    L('n2-ni-kagirazu', ('Pas seulement… : 〜に限らず・〜のみならず', 'Not only…: 〜に限らず・〜のみならず'), ('Dire qu’une chose vaut bien au-delà d’un seul cas.', 'Say that something holds well beyond a single case.'), 10, [
        ('Nom + に限らず = pas seulement…, mais aussi (tous les autres) : 子どもに 限らず、大人も 楽しめます.', 'Noun + に限らず = not just…, but (all the others) too: 子どもに 限らず、大人も 楽しめます.'),
        ('Nom / forme neutre + のみならず = non seulement… mais encore (écrit, soutenu) : 日本のみならず、世界中で 人気が ある.', 'Noun / plain form + のみならず = not only… but also (written, literary): 日本のみならず、世界中で 人気が ある.'),
        ('À l’inverse, nom + に限って = justement (et seulement) dans ce cas : 急いで いる ときに 限って、バスが 来ない.', 'Conversely, noun + に限って = precisely (and only) in that case: 急いで いる ときに 限って、バスが 来ない.'),
      ], [
        G('gram-n2-ni-kagirazu', '〜に限らず', '〜にかぎらず', '~ni kagirazu', ('pas seulement…, mais aussi…', 'not just…, but also…')),
        G('gram-n2-nominarazu', '〜のみならず', '〜のみならず', '~nominarazu', ('non seulement… mais encore… (soutenu)', 'not only… but also… (literary)')),
        V('vocab-ippan', '一般', 'いっぱん', 'ippan', ('général, ordinaire', 'general, ordinary')),
        V('vocab-sekaijuu', '世界中', 'せかいじゅう', 'sekaijuu', ('le monde entier', 'all over the world')),
        V('vocab-dansei', '男性', 'だんせい', 'dansei', ('homme (sexe masculin)', 'man, male')),
        V('vocab-josei', '女性', 'じょせい', 'josei', ('femme (sexe féminin)', 'woman, female')),
        K('kanji-n2-kagiru', '限', 'かぎる', 'kagiru', ('limiter, borne', 'limit, bound'), ['ゲン'], ['かぎ(る)'], 9),
        K('kanji-n2-ippan', '般', 'はん', 'han', ('ensemble, sorte', 'all, sort'), ['ハン'], [], 10),
      ], [
        ex('この ゲームは 子どもに 限らず、大人にも 人気が あります。', 'この ゲームは こどもに かぎらず、おとなにも にんきが あります。', 'Ce jeu plaît non seulement aux enfants, mais aussi aux adultes.', 'This game is popular not just with children but with adults too.'),
        ex('彼女は 国内のみならず、世界中で 知られて います。', 'かのじょは こくないのみならず、せかいじゅうで しられて います。', 'Elle est connue non seulement dans le pays, mais dans le monde entier.', 'She is known not only at home but all over the world.'),
      ], [
        FB(CHOOSE, 'この 料理は 女性に ＿、男性にも 人気が ある。', ['限らず', '限って', '限り'], '限らず', ('Pas seulement… : 〜に限らず.', 'Not just…: 〜に限らず.'), ('Ce plat plaît non seulement aux femmes, mais aussi aux hommes.', 'This dish is popular not just with women but with men too.')),
        FB(CHOOSE, '出かけようと する ときに ＿、雨が 降る。', ['限って', '限らず', 'のみならず'], '限って', ('Justement dans ce cas-là : 〜に限って.', 'Precisely in that case: 〜に限って.'), ('C’est toujours quand je m’apprête à sortir qu’il se met à pleuvoir.', 'It always starts raining just when I am about to go out.')),
        TF('この 問題は 学生のみならず、一般の 人にも 関係が あります。', ('Le problème ne concerne que les étudiants.', 'The problem concerns students only.'), FAUX, ('〜のみならず : pas seulement les étudiants, le grand public aussi.', '〜のみならず: not only students, the general public too.')),
        SO(ORDER('Pas seulement l’été, on peut en profiter toute l’année.', 'Not just in summer, you can enjoy it all year round.'), ['夏', 'に限らず', '一年中', '楽しめます'], ('Nom + に限らず, puis le cas plus large.', 'Noun + に限らず, then the wider case.')),
      ]),
    L('n2-dokoroka', ('Loin de…, et même… : 〜どころか・〜ばかりか', 'Far from…, and even…: 〜どころか・〜ばかりか'), ('Corriger une attente par son contraire, ou renchérir sur ce qu’on vient de dire.', 'Correct an expectation with its opposite, or go one further than what was just said.'), 10, [
        ('Forme neutre / nom + どころか = loin de…, bien au contraire : 薬を 飲んだのに、治るどころか、悪く なった.', 'Plain form / noun + どころか = far from…, quite the opposite: 薬を 飲んだのに、治るどころか、悪く なった.'),
        ('〜どころか peut aussi renchérir : 漢字どころか、ひらがなも 読めない (les kanji ? il ne lit même pas les hiragana).', '〜どころか can also go one further: 漢字どころか、ひらがなも 読めない (kanji? he cannot even read hiragana).'),
        ('Forme neutre / nom + ばかりか = non seulement… mais en plus (souvent avec 〜も ou 〜まで) : 彼は 英語ばかりか、中国語も 話せる.', 'Plain form / noun + ばかりか = not only… but on top of that (often with 〜も or 〜まで): 彼は 英語ばかりか、中国語も 話せる.'),
      ], [
        G('gram-n2-dokoroka', '〜どころか', '〜どころか', '~dokoro ka', ('loin de… ; sans parler de…', 'far from… ; let alone…')),
        G('gram-n2-bakari-ka', '〜ばかりか', '〜ばかりか', '~bakari ka', ('non seulement… mais en plus…', 'not only… but on top of that…')),
        V('vocab-kaifuku', '回復', 'かいふく', 'kaifuku', ('rétablissement, reprise', 'recovery')),
        V('vocab-akka', '悪化', 'あっか', 'akka', ('aggravation', 'worsening')),
        V('vocab-meiwaku', '迷惑', 'めいわく', 'meiwaku', ('gêne causée aux autres', 'nuisance, trouble (to others)')),
        V('vocab-kansha', '感謝', 'かんしゃ', 'kansha', ('gratitude', 'gratitude')),
        K('kanji-n2-fuku', '復', 'ふく', 'fuku', ('revenir, de nouveau', 'return, again'), ['フク'], [], 12),
        K('kanji-n2-mayou', '迷', 'まよう', 'mayou', ('hésiter, se perdre', 'hesitate, get lost'), ['メイ'], ['まよ(う)'], 9),
      ], [
        ex('薬を 飲んだのに、回復するどころか、悪化して しまいました。', 'くすりを のんだのに、かいふくするどころか、あっかして しまいました。', 'J’ai pris le médicament, mais loin de me rétablir, mon état s’est aggravé.', 'I took the medicine, but far from recovering, I got worse.'),
        ex('彼は 手伝って くれた ばかりか、お金まで 貸して くれました。', 'かれは てつだって くれた ばかりか、おかねまで かして くれました。', 'Non seulement il m’a aidé, mais il m’a même prêté de l’argent.', 'Not only did he help me, he even lent me money.'),
      ], [
        FB(CHOOSE, '休み＿、今週は 毎日 残業です。', ['どころか', 'ばかりか', 'に限らず'], 'どころか', ('Le contraire de ce qu’on attend : 〜どころか.', 'The opposite of what is expected: 〜どころか.'), ('Du repos ? Loin de là : cette semaine, je fais des heures supplémentaires tous les jours.', 'A break? Far from it: this week I am working overtime every day.')),
        FB(CHOOSE, 'あの 店は 料理が まずい＿、値段も 高い。', ['ばかりか', 'どころか', 'からには'], 'ばかりか', ('On ajoute un second défaut : 〜ばかりか〜も.', 'A second fault is added: 〜ばかりか〜も.'), ('Dans ce restaurant, non seulement la cuisine est mauvaise, mais en plus c’est cher.', 'At that restaurant, not only is the food bad, it is expensive too.')),
        TF('彼は 感謝するどころか、文句を 言った。', ('Il a remercié.', 'He said thank you.'), FAUX, ('〜どころか : au lieu de remercier, il s’est plaint.', '〜どころか: instead of being grateful, he complained.')),
        DC(('Un collègue s’excuse de t’avoir dérangé. En réalité, il t’a rendu service.', 'A colleague apologises for bothering you. In fact, he did you a favour.'), [('同僚', '昨日は 迷惑を かけて、すみません。')], ('Ton collègue s’excuse de t’avoir causé du dérangement hier.', 'Your colleague apologises for causing you trouble yesterday.'), ['いいえ。迷惑どころか、助かりました。', 'いいえ。迷惑ばかりか、助かりました。', 'いいえ。迷惑に 限らず、助かりました。'], 'いいえ。迷惑どころか、助かりました。', ('Loin d’être une gêne, cela a rendu service : 〜どころか.', 'Far from being a nuisance, it helped: 〜どころか.')),
      ]),
    L('n2-ni-watatte', ('Tout au long de… : 〜にわたって・〜を通じて', 'Throughout…: 〜にわたって・〜を通じて'), ('Dire qu’une chose s’étend sur toute une durée ou un espace, ou passe par un intermédiaire.', 'Say that something extends over a whole period or area, or goes through an intermediary.'), 10, [
        ('Nom (durée, étendue, nombre) + にわたって = sur toute l’étendue de : 三日間に わたって, 全国に わたって. Devant un nom : 〜にわたる.', 'Noun (duration, area, number) + にわたって = over the whole span of: 三日間に わたって, 全国に わたって. Before a noun: 〜にわたる.'),
        ('Nom + を通じて / を通して = pendant toute (une période) : 一年を 通じて 暖かい.', 'Noun + を通じて / を通して = throughout (a period): 一年を 通じて 暖かい.'),
        ('〜を通じて signifie aussi « par l’intermédiaire de » : 友人を 通じて 知り合った, インターネットを 通じて.', '〜を通じて also means “by way of”: 友人を 通じて 知り合った, インターネットを 通じて.'),
      ], [
        G('gram-n2-ni-watatte', '〜にわたって', '〜にわたって', '~ni watatte', ('sur toute l’étendue de…', 'over the whole span of…')),
        G('gram-n2-wo-tsuujite', '〜を通じて', '〜をつうじて', '~wo tsuujite', ('tout au long de… ; par l’intermédiaire de…', 'throughout… ; by way of…')),
        V('vocab-kikan', '期間', 'きかん', 'kikan', ('période, durée', 'period, length of time')),
        V('vocab-zenkoku', '全国', 'ぜんこく', 'zenkoku', ('tout le pays', 'the whole country')),
        V('vocab-chiiki', '地域', 'ちいき', 'chiiki', ('région, quartier', 'region, local area')),
        V('vocab-kouryuu', '交流', 'こうりゅう', 'kouryuu', ('échanges (entre personnes)', 'exchange (between people)')),
        K('kanji-n2-ki', '期', 'き', 'ki', ('période, terme', 'period, term'), ['キ'], [], 12),
        K('kanji-n2-iki', '域', 'いき', 'iki', ('zone, domaine', 'zone, domain'), ['イキ'], [], 11),
      ], [
        ex('祭りは 三日間に わたって 行われます。', 'まつりは みっかかんに わたって おこなわれます。', 'La fête se déroule sur trois jours.', 'The festival is held over three days.'),
        ex('この 地域は 一年を 通じて 雨が 多いです。', 'この ちいきは いちねんを つうじて あめが おおいです。', 'Dans cette région, il pleut beaucoup tout au long de l’année.', 'In this region it rains a lot throughout the year.'),
      ], [
        PC(COMPLETE, '会議は 五時間＿ わたって 続きました。', ['に', 'を', 'で'], 'に', ('〜に わたって.', '〜に わたって.'), ('La réunion a duré cinq heures d’affilée.', 'The meeting went on for a full five hours.')),
        FB(CHOOSE, '私たちは インターネットを ＿ 知り合いました。', ['通じて', 'わたって', '限って'], '通じて', ('Par l’intermédiaire de : 〜を通じて.', 'By way of: 〜を通じて.'), ('Nous nous sommes connus par Internet.', 'We got to know each other through the internet.')),
        FB(COMPLETE, '全国に ＿ 調査が 行われた。', ['わたる', 'わたって', '通じる'], 'わたる', ('Devant un nom : 〜にわたる + nom.', 'Before a noun: 〜にわたる + noun.'), ('Une enquête couvrant tout le pays a été menée.', 'A survey covering the whole country was carried out.')),
        TF('この 交流は 十年に わたって 続いて います。', ('Ces échanges ont duré une seule année.', 'These exchanges lasted a single year.'), FAUX, ('十年に わたって = sur dix ans.', '十年に わたって = over ten years.')),
      ]),
  ])])

# ═════════════════════════ Île 6 : conditions et hypothèses ═════════════════════════
W6 = WORLD('n2-w6', ('Conditions et hypothèses', 'Conditions and hypotheses'), REGION,
  ('Poser une condition, raisonner sur une supposition et dire de quoi dépend la suite.', 'Set a condition, reason from a supposition, and say what the outcome depends on.'),
  (('Le Nurarihyon aux Conditions', 'The Nurarihyon of Conditions'), '仮', ('Ce vieillard insaisissable s’installe au conseil comme s’il en était le maître, et ne cède jamais rien sans condition. Tant que… à supposer que… tout dépend de… : sauras-tu négocier ?', 'This slippery old man settles into the council as if he were its master, and never gives way without a condition. As long as… supposing that… it all depends on…: can you negotiate?')),
  [CH('n2-w6-c1', ('Tant que, à supposer que, selon', 'As long as, supposing that, depending on'), [
    L('n2-kagiri', ('Tant que… : 〜限り・〜ない限り', 'As long as…: 〜限り・〜ない限り'), ('Poser la condition sans laquelle rien ne change, ou la limite de ce qu’on sait.', 'State the condition without which nothing changes, or the limit of what you know.'), 10, [
        ('Forme neutre + 限り = tant que, aussi longtemps que : 体が 丈夫な 限り、働きたい.', 'Plain form + 限り = as long as, for as long as: 体が 丈夫な 限り、働きたい.'),
        ('Verbe en ない + 限り = à moins que, tant que… ne… pas : 許可が ない 限り、入れません.', 'ない-form + 限り = unless, as long as… not: 許可が ない 限り、入れません.'),
        ('Deux formules utiles : 私の 知る 限り = pour autant que je sache ; できる 限り = dans toute la mesure du possible.', 'Two useful set phrases: 私の 知る 限り = as far as I know; できる 限り = as far as possible.'),
      ], [
        G('gram-n2-kagiri', '〜限り', '〜かぎり', '~kagiri', ('tant que… ; autant que…', 'as long as… ; as far as…')),
        G('gram-n2-nai-kagiri', '〜ない限り', '〜ないかぎり', '~nai kagiri', ('à moins que…, tant que… ne… pas', 'unless…, as long as… not')),
        V('vocab-kyoka', '許可', 'きょか', 'kyoka', ('autorisation', 'permission')),
        V('vocab-jijou', '事情', 'じじょう', 'jijou', ('circonstances, situation', 'circumstances, situation')),
        V('vocab-kyouryoku', '協力', 'きょうりょく', 'kyouryoku', ('coopération', 'cooperation')),
        V('vocab-joubu', '丈夫', 'じょうぶ', 'joubu', ('solide, robuste', 'sturdy, robust')),
        K('kanji-n2-yurusu', '許', 'ゆるす', 'yurusu', ('permettre, pardonner', 'permit, forgive'), ['キョ'], ['ゆる(す)'], 11),
        K('kanji-n2-kyou', '協', 'きょう', 'kyou', ('s’unir, ensemble', 'unite, joint'), ['キョウ'], [], 8),
      ], [
        ex('許可が ない 限り、この 部屋には 入れません。', 'きょかが ない かぎり、この へやには はいれません。', 'À moins d’une autorisation, on ne peut pas entrer dans cette pièce.', 'Unless you have permission, you cannot enter this room.'),
        ex('私の 知る 限り、彼は そんな 人では ありません。', 'わたしの しる かぎり、かれは そんな ひとでは ありません。', 'Pour autant que je sache, il n’est pas ce genre de personne.', 'As far as I know, he is not that kind of person.'),
      ], [
        FB(CHOOSE, 'みんなの 協力が ＿ 限り、この 計画は 成功しない。', ['ない', 'ある', 'あった'], 'ない', ('À moins de… : verbe en ない + 限り.', 'Unless…: ない-form + 限り.'), ('Sans la coopération de tous, ce projet ne réussira pas.', 'Unless everyone cooperates, this plan will not succeed.')),
        FB(CHOOSE, '体が 丈夫な＿、この 仕事を 続ける つもりです。', ['限り', '限らず', 'どころか'], '限り', ('Tant que… : 〜限り.', 'As long as…: 〜限り.'), ('Tant que ma santé tiendra, je compte continuer ce travail.', 'As long as I stay healthy, I intend to continue this work.')),
        FB(COMPLETE, 'できる＿ 早く 返事を します。', ['限り', 'ばかり', 'ながら'], '限り', ('できる 限り = autant que possible.', 'できる 限り = as far as possible.'), ('Je répondrai le plus vite possible.', 'I will reply as quickly as I can.')),
        TF('特別な 事情が ない 限り、欠席は 認められません。', ('On peut être absent sans raison particulière.', 'You may be absent without any particular reason.'), FAUX, ('〜ない限り : sans circonstance particulière, l’absence n’est pas acceptée.', '〜ない限り: without special circumstances, absence is not accepted.')),
      ]),
    L('n2-to-shitara', ('À supposer que… : 〜としたら・〜とすれば', 'Supposing that…: 〜としたら・〜とすれば'), ('Raisonner à partir d’une hypothèse, réelle ou imaginaire.', 'Reason from a hypothesis, real or imaginary.'), 10, [
        ('Forme neutre + としたら / とすれば / とすると = à supposer que, si l’on admet que : 行くと したら、来週です.', 'Plain form + としたら / とすれば / とすると = supposing that, if we accept that: 行くと したら、来週です.'),
        ('Avec 仮に ou もし, l’hypothèse est imaginaire : 仮に 宝くじが 当たったと したら、何を 買いますか.', 'With 仮に or もし, the hypothesis is imaginary: 仮に 宝くじが 当たったと したら、何を 買いますか.'),
        ('〜とすれば et 〜とすると servent surtout à tirer une conclusion logique : それが 本当だと すれば、大変だ. 〜としたら accepte aussi un souhait ou une question.', '〜とすれば and 〜とすると mainly serve to draw a logical conclusion: それが 本当だと すれば、大変だ. 〜としたら also accepts a wish or a question.'),
      ], [
        G('gram-n2-to-shitara', '〜としたら', '〜としたら', '~to shitara', ('à supposer que…, si jamais…', 'supposing that…, if ever…')),
        G('gram-n2-to-sureba', '〜とすれば', '〜とすれば', '~to sureba', ('si l’on admet que…', 'if we accept that…')),
        V('vocab-karini', '仮に', 'かりに', 'karini', ('à supposer, par hypothèse', 'hypothetically, supposing')),
        V('vocab-takarakuji', '宝くじ', 'たからくじ', 'takarakuji', ('loterie', 'lottery')),
        V('vocab-atarimasu', '当たります', 'あたります', 'atarimasu', ('gagner (à un tirage), tomber juste', 'to win (a draw), to hit the mark')),
        V('vocab-souzou', '想像', 'そうぞう', 'souzou', ('imagination', 'imagination')),
        K('kanji-n2-kari', '仮', 'かり', 'kari', ('provisoire, supposé', 'provisional, supposed'), ['カ'], ['かり'], 6),
        K('kanji-n2-sou', '想', 'そう', 'sou', ('idée, pensée', 'idea, thought'), ['ソウ'], [], 13),
      ], [
        ex('仮に 宝くじが 当たったと したら、何を しますか。', 'かりに たからくじが あたったと したら、なにを しますか。', 'À supposer que vous gagniez à la loterie, que feriez-vous ?', 'Supposing you won the lottery, what would you do?'),
        ex('その 話が 本当だと すれば、すぐに 知らせなければ なりません。', 'その はなしが ほんとうだと すれば、すぐに しらせなければ なりません。', 'Si cette histoire est vraie, il faut prévenir tout de suite.', 'If that story is true, we must let people know at once.'),
      ], [
        FB(CHOOSE, '留学する＿、どの 国が いいですか。', ['としたら', 'どころか', 'ばかりに'], 'としたら', ('Hypothèse + question : 〜としたら.', 'Hypothesis + question: 〜としたら.'), ('Si tu devais partir étudier à l’étranger, quel pays choisirais-tu ?', 'If you were to study abroad, which country would be good?')),
        FB(CHOOSE, '＿ 明日 世界が 終わると したら、何を 食べたいですか。', ['仮に', '必ず', 'さすが'], '仮に', ('仮に renforce l’hypothèse imaginaire.', '仮に reinforces the imaginary hypothesis.'), ('À supposer que le monde s’arrête demain, que voudrais-tu manger ?', 'Supposing the world ended tomorrow, what would you want to eat?')),
        TF('一人で 行くと すれば、三時間は かかるだろう。', ('La personne affirme qu’elle ira seule.', 'The speaker states that they will go alone.'), FAUX, ('〜とすれば : simple hypothèse, rien n’est décidé.', '〜とすれば: a mere hypothesis, nothing is decided.')),
        SO(ORDER('Si c’est vrai, c’est grave.', 'If it is true, it is serious.'), ['それが', '本当だ', 'と すれば', '大変です'], ('Forme neutre + と すれば, puis la conclusion.', 'Plain form + と すれば, then the conclusion.')),
      ]),
    L('n2-shidai', ('Dès que…, selon… : 〜次第', 'As soon as…, depending on…: 〜次第'), ('Annoncer qu’on agira dès qu’une chose sera faite, et dire de quoi dépend un résultat.', 'Announce that you will act as soon as something is done, and say what a result depends on.'), 10, [
        ('Base en ます + 次第 = dès que (formel, pour une action future voulue) : 到着し次第、ご連絡します. Avec un nom d’action : 確認 次第.', 'ます-stem + 次第 = as soon as (formal, for a deliberate future action): 到着し次第、ご連絡します. With an action noun: 確認 次第.'),
        ('Nom + 次第だ / 次第で = dépendre de : 結果は 努力 次第だ ; 天気 次第で 予定を 変えます.', 'Noun + 次第だ / 次第で = to depend on: 結果は 努力 次第だ; 天気 次第で 予定を 変えます.'),
        ('〜次第 (dès que) ne s’emploie pas au passé : la suite est une promesse, une demande ou une intention.', '〜次第 (as soon as) is not used in the past: what follows is a promise, a request or an intention.'),
      ], [
        G('gram-n2-shidai', '〜次第', '〜しだい', '~shidai', ('dès que… (formel)', 'as soon as… (formal)')),
        G('gram-n2-shidai-da', '〜次第だ・〜次第で', '〜しだいだ・〜しだいで', '~shidai da / ~shidai de', ('dépendre de…, selon…', 'to depend on…, depending on…')),
        V('vocab-touchaku', '到着', 'とうちゃく', 'touchaku', ('arrivée (à destination)', 'arrival')),
        V('vocab-kakunin', '確認', 'かくにん', 'kakunin', ('vérification, confirmation', 'checking, confirmation')),
        V('vocab-ketsuron', '結論', 'けつろん', 'ketsuron', ('conclusion', 'conclusion')),
        V('vocab-honnin', '本人', 'ほんにん', 'honnin', ('l’intéressé(e), la personne elle-même', 'the person in question')),
        K('kanji-n2-tsugi', '次', 'つぎ', 'tsugi', ('suivant, ordre', 'next, order'), ['ジ', 'シ'], ['つぎ', 'つ(ぐ)'], 6),
        K('kanji-n2-tou', '到', 'とう', 'tou', ('atteindre, parvenir', 'reach, attain'), ['トウ'], [], 8),
      ], [
        ex('荷物が 到着し次第、お知らせします。', 'にもつが とうちゃくし しだい、おしらせします。', 'Dès que le colis arrivera, je vous préviendrai.', 'As soon as the parcel arrives, I will let you know.'),
        ex('合格できるか どうかは、本人の 努力 次第です。', 'ごうかくできるか どうかは、ほんにんの どりょく しだいです。', 'Réussir ou non dépend des efforts de l’intéressé.', 'Whether one passes or not depends on the person’s own efforts.'),
      ], [
        FB(CHOOSE, '結論が ＿ 次第、ご報告します。', ['出', '出る', '出た'], '出', ('Base en ます + 次第 : 出ます → 出.', 'ます-stem + 次第: 出ます → 出.'), ('Dès qu’une conclusion sera trouvée, je vous en rendrai compte.', 'As soon as a conclusion is reached, I will report to you.')),
        FB(CHOOSE, '明日の 試合は 天気＿です。', ['次第', '限り', '最中'], '次第', ('Nom + 次第だ = dépendre de.', 'Noun + 次第だ = to depend on.'), ('Le match de demain dépendra du temps.', 'Tomorrow’s match depends on the weather.')),
        TF('昨日、家に 着き次第、電話しました。', ('Cette phrase est naturelle en japonais.', 'This sentence is natural Japanese.'), FAUX, ('〜次第 (dès que) ne s’emploie pas au passé : on dirait 着いて すぐ.', '〜次第 (as soon as) is not used in the past: you would say 着いて すぐ.')),
        DC(('Un client attend une réponse. Tu promets de le rappeler après vérification.', 'A customer is waiting for an answer. You promise to call back after checking.'), [('客', 'いつ 分かりますか。')], ('Le client demande quand il aura la réponse.', 'The customer asks when he will know.'), ['確認でき次第、お電話いたします。', '確認できた とたん、お電話いたします。', '確認できる 限り、お電話いたします。'], '確認でき次第、お電話いたします。', ('Promesse formelle : base en ます + 次第.', 'A formal promise: ます-stem + 次第.')),
      ]),
  ])])

# ═════════════════════════ Île 7 : tendances et évolutions ═════════════════════════
W7 = WORLD('n2-w7', ('Tendances et évolutions', 'Trends and changes'), REGION,
  ('Décrire un changement en cours, deux évolutions liées, et un état qui s’installe.', 'Describe a change under way, two linked developments, and a state that is setting in.'),
  (('La Rokurokubi qui s’Allonge', 'The Stretching Rokurokubi'), '伸', ('Le jour, c’est une dame comme les autres. La nuit, son cou s’allonge, s’allonge encore… Plus l’heure avance, plus il grandit. Décris ce qui est en train de changer.', 'By day she is a lady like any other. By night her neck grows longer, and longer still… The later the hour, the more it stretches. Describe what is in the middle of changing.')),
  [CH('n2-w7-c1', ('De plus en plus, à mesure que, un peu trop', 'More and more, as, a little too'), [
    L('n2-tsutsu-aru', ('En train de changer : 〜つつある・〜一方だ', 'In the middle of changing: 〜つつある・〜一方だ'), ('Décrire une évolution en cours ou une tendance qui ne s’arrête pas.', 'Describe a change under way or a trend that does not stop.'), 10, [
        ('Base en ます + つつある = être en train de (changer peu à peu ; plutôt écrit) : 景気は 回復しつつある.', 'ます-stem + つつある = to be in the process of (changing little by little; rather written): 景気は 回復しつつある.'),
        ('Verbe au dictionnaire + 一方だ = ne cesser de…, aller toujours plus… (souvent en mal) : 物価は 上がる 一方だ.', 'Dictionary-form verb + 一方だ = to keep on …ing, more and more (often for the worse): 物価は 上がる 一方だ.'),
        ('Ces formes s’emploient avec des verbes de changement (増える, 減る, 変わる, 進む), pas avec des actions ponctuelles.', 'These forms are used with verbs of change (増える, 減る, 変わる, 進む), not with one-off actions.'),
      ], [
        G('gram-n2-tsutsu-aru', '〜つつある', '〜つつある', '~tsutsu aru', ('être en train de… (évolution)', 'to be in the process of… (change)')),
        G('gram-n2-ippou-da', '〜一方だ', '〜いっぽうだ', '~ippou da', ('ne cesser de…, aller toujours plus…', 'to keep on …ing, more and more')),
        V('vocab-keiki', '景気', 'けいき', 'keiki', ('conjoncture économique', 'economic climate')),
        V('vocab-bukka', '物価', 'ぶっか', 'bukka', ('niveau des prix', 'prices, cost of living')),
        V('vocab-koureika', '高齢化', 'こうれいか', 'koureika', ('vieillissement de la population', 'ageing of the population')),
        V('vocab-fukyuu', '普及', 'ふきゅう', 'fukyuu', ('diffusion, généralisation', 'spread, wide adoption')),
        K('kanji-n2-keshiki', '景', 'けい', 'kei', ('vue, aspect', 'view, aspect'), ['ケイ'], [], 12),
        K('kanji-n2-rei', '齢', 'れい', 'rei', ('âge (en années)', 'age (in years)'), ['レイ'], [], 17),
      ], [
        ex('景気は 少しずつ 回復しつつ あります。', 'けいきは すこしずつ かいふくしつつ あります。', 'L’économie est en train de se redresser peu à peu.', 'The economy is gradually recovering.'),
        ex('この 町の 人口は 減る 一方です。', 'この まちの じんこうは へる いっぽうです。', 'La population de cette ville ne cesse de diminuer.', 'The population of this town keeps falling.'),
      ], [
        FB(CHOOSE, '新しい 技術が 世界中に 普及し＿。', ['つつある', '一方だ', '次第だ'], 'つつある', ('Base en ます + つつある.', 'ます-stem + つつある.'), ('La nouvelle technologie est en train de se répandre dans le monde entier.', 'The new technology is spreading all over the world.')),
        FB(CHOOSE, '物価は ＿ 一方で、生活が 苦しい。', ['上がる', '上がり', '上がって'], '上がる', ('Verbe au dictionnaire + 一方だ.', 'Dictionary-form verb + 一方だ.'), ('Les prix ne cessent de monter, et la vie est difficile.', 'Prices just keep rising, and life is hard.')),
        TF('日本では 高齢化が 進みつつ あります。', ('Le vieillissement est un changement déjà terminé.', 'Ageing is a change that is already complete.'), FAUX, ('〜つつある : le changement est en cours.', '〜つつある: the change is still under way.')),
        SO(ORDER('La situation ne cesse d’empirer.', 'The situation keeps getting worse.'), ['状況は', '悪く', 'なる', '一方です'], ('Verbe au dictionnaire + 一方です.', 'Dictionary-form verb + 一方です.')),
      ]),
    L('n2-ni-tsurete', ('À mesure que… : 〜につれて・〜にしたがって', 'As…: 〜につれて・〜にしたがって'), ('Relier deux évolutions qui avancent ensemble.', 'Link two developments that move forward together.'), 10, [
        ('Verbe au dictionnaire / nom + につれて = à mesure que (deux changements progressifs) : 年を 取るに つれて、体力が 落ちる.', 'Dictionary-form verb / noun + につれて = as (two gradual changes): 年を 取るに つれて、体力が 落ちる.'),
        ('〜にしたがって a le même sens, en plus formel ; il signifie aussi « conformément à » : 指示に したがって 行動する.', '〜にしたがって means the same, more formally; it also means “in accordance with”: 指示に したがって 行動する.'),
        ('Les deux parties expriment un changement : on évite un ordre ou une action ponctuelle dans la seconde.', 'Both halves express a change: avoid an order or a one-off action in the second.'),
      ], [
        G('gram-n2-ni-tsurete', '〜につれて', '〜につれて', '~ni tsurete', ('à mesure que…', 'as… (gradually)')),
        G('gram-n2-ni-shitagatte', '〜にしたがって', '〜にしたがって', '~ni shitagatte', ('à mesure que… ; en suivant…', 'as… ; following…')),
        V('vocab-seichou', '成長', 'せいちょう', 'seichou', ('croissance (grandir)', 'growth (growing up)')),
        V('vocab-henka', '変化', 'へんか', 'henka', ('changement, évolution', 'change, shift')),
        V('vocab-hatten', '発展', 'はってん', 'hatten', ('développement, essor', 'development, expansion')),
        V('vocab-tairyoku', '体力', 'たいりょく', 'tairyoku', ('force physique, endurance', 'physical strength, stamina')),
        K('kanji-n2-kawaru', '変', 'かわる', 'kawaru', ('changer ; étrange', 'change; strange'), ['ヘン'], ['か(わる)', 'か(える)'], 9),
        K('kanji-n2-ten', '展', 'てん', 'ten', ('déployer, exposer', 'unfold, display'), ['テン'], [], 10),
      ], [
        ex('子どもは 成長するに つれて、親と 話さなく なります。', 'こどもは せいちょうするに つれて、おやと はなさなく なります。', 'À mesure qu’ils grandissent, les enfants parlent moins à leurs parents.', 'As children grow up, they stop talking to their parents.'),
        ex('町の 発展に したがって、交通も 便利に なりました。', 'まちの はってんに したがって、こうつうも べんりに なりました。', 'À mesure que la ville s’est développée, les transports sont devenus plus pratiques.', 'As the town developed, transport became more convenient too.'),
      ], [
        FB(CHOOSE, '年を 取る＿、体力が 落ちて きた。', ['につれて', 'に限って', '次第'], 'につれて', ('Deux changements liés : 〜につれて.', 'Two linked changes: 〜につれて.'), ('À mesure que je vieillis, mes forces diminuent.', 'As I get older, my stamina has been declining.')),
        PC(COMPLETE, '時代の 変化＿ したがって、考え方も 変わる。', ['に', 'を', 'が'], 'に', ('〜に したがって.', '〜に したがって.'), ('À mesure que l’époque change, les façons de penser changent aussi.', 'As the times change, ways of thinking change too.')),
        TF('係員の 指示に したがって、避難して ください。', ('Ici, 〜にしたがって signifie « en suivant ».', 'Here, 〜にしたがって means “following”.'), VRAI, ('指示に したがって = en suivant les consignes.', '指示に したがって = following the instructions.')),
        FB(COMPLETE, '日本語が 上手に なるに ＿、友だちが 増えた。', ['つれて', '限って', 'わたって'], 'つれて', ('〜に つれて.', '〜に つれて.'), ('À mesure que mon japonais s’est amélioré, je me suis fait plus d’amis.', 'As my Japanese improved, I made more friends.')),
      ]),
    L('n2-gimi', ('Un peu…, couvert de… : 〜気味・〜だらけ', 'A touch of…, covered in…: 〜気味・〜だらけ'), ('Décrire un léger état qui s’installe, ou quelque chose qui en est rempli.', 'Describe a slight state setting in, or something that is full of it.'), 10, [
        ('Nom / base en ます + 気味 = avoir un peu tendance à, se sentir un peu… (souvent négatif) : 風邪気味, 疲れ気味, 太り気味.', 'Noun / ます-stem + 気味 = to tend slightly towards, to feel a little… (often negative): 風邪気味, 疲れ気味, 太り気味.'),
        ('Nom + だらけ = plein de, couvert de (quelque chose de désagréable) : 泥だらけ, 間違いだらけ, 傷だらけ.', 'Noun + だらけ = full of, covered in (something unpleasant): 泥だらけ, 間違いだらけ, 傷だらけ.'),
        ('〜気味 décrit une impression légère, là où 〜がち (N3) parle de fréquence : 最近 疲れ気味だ / 最近 休みがちだ.', '〜気味 describes a slight impression, whereas 〜がち (N3) is about frequency: 最近 疲れ気味だ / 最近 休みがちだ.'),
      ], [
        G('gram-n2-gimi', '〜気味', '〜ぎみ', '~gimi', ('un peu…, une légère tendance à…', 'a touch of…, slightly…')),
        G('gram-n2-darake', '〜だらけ', '〜だらけ', '~darake', ('plein de…, couvert de…', 'full of…, covered in…')),
        V('vocab-doro', '泥', 'どろ', 'doro', ('boue', 'mud')),
        V('vocab-machigai', '間違い', 'まちがい', 'machigai', ('erreur, faute', 'mistake, error')),
        V('vocab-nebusoku', '寝不足', 'ねぶそく', 'nebusoku', ('manque de sommeil', 'lack of sleep')),
        V('vocab-kizu', '傷', 'きず', 'kizu', ('blessure, éraflure', 'wound, scratch')),
        K('kanji-n2-tsukareru', '疲', 'つかれる', 'tsukareru', ('se fatiguer', 'tire, grow weary'), ['ヒ'], ['つか(れる)'], 10),
        K('kanji-n2-yogoreru', '汚', 'よごれる', 'yogoreru', ('salir, sale', 'dirty, soil'), ['オ'], ['よご(れる)', 'きたな(い)'], 6),
      ], [
        ex('最近、寝不足で 少し 疲れ気味です。', 'さいきん、ねぶそくで すこし つかれぎみです。', 'Ces temps-ci, par manque de sommeil, je me sens un peu fatigué.', 'Lately, from lack of sleep, I have been feeling a little tired.'),
        ex('子どもたちは 泥だらけに なって 遊んで います。', 'こどもたちは どろだらけに なって あそんで います。', 'Les enfants jouent, couverts de boue.', 'The children are playing, covered in mud.'),
      ], [
        FB(CHOOSE, '今日は 風邪＿なので、早く 帰ります。', ['気味', 'だらけ', '次第'], '気味', ('Léger état : nom + 気味.', 'A slight state: noun + 気味.'), ('Je me sens un peu enrhumé aujourd’hui, alors je rentre tôt.', 'I feel a cold coming on today, so I am going home early.')),
        FB(CHOOSE, 'この 作文は 間違い＿だ。', ['だらけ', '気味', 'がち'], 'だらけ', ('Plein de (négatif) : nom + だらけ.', 'Full of (negative): noun + だらけ.'), ('Cette rédaction est truffée de fautes.', 'This essay is full of mistakes.')),
        TF('彼の 足は 傷だらけだった。', ('Il avait une seule petite blessure à la jambe.', 'He had a single small wound on his leg.'), FAUX, ('傷だらけ = couvert de blessures.', '傷だらけ = covered in wounds.')),
        FB(COMPLETE, '最近、少し 太り＿なので、運動を 始めました。', ['気味', 'だらけ', '一方'], '気味', ('Base en ます + 気味 : 太ります → 太り気味.', 'ます-stem + 気味: 太ります → 太り気味.'), ('J’ai un peu grossi ces temps-ci, alors je me suis mis au sport.', 'I have put on a little weight lately, so I have started exercising.')),
      ]),
  ])])

# ═════════════════════════ Île 8 : convictions du locuteur ═════════════════════════
W8 = WORLD('n2-w8', ('Convictions du locuteur', 'The speaker’s convictions'), REGION,
  ('Affirmer une certitude, ramener une chose à peu, dire ce qu’on ne peut éviter et donner une vérité générale ou un conseil.', 'State a certainty, cut something down to size, say what cannot be avoided, and give a general truth or a piece of advice.'),
  (('Tamamo aux Neuf Queues', 'Tamamo of the Nine Tails'), '尾', ('La plus belle dame de la cour est une renarde à neuf queues. Ce ne peut être qu’elle ; ce n’est qu’une illusion ; on est bien forcé de l’admettre. Tranche, et dis ce que tu penses vraiment.', 'The most beautiful lady at court is a nine-tailed fox. It can only be her; it is no more than an illusion; one is forced to admit it. Decide, and say what you really think.')),
  [CH('n2-w8-c1', ('Sûrement, rien que, forcé de', 'Surely, no more than, forced to'), [
    L('n2-ni-chigainai', ('Sans aucun doute, rien de plus : 〜に違いない・〜にすぎない', 'No doubt, no more than: 〜に違いない・〜にすぎない'), ('Affirmer une conviction forte, ou ramener une chose à ce qu’elle est vraiment.', 'State a strong conviction, or reduce something to what it really is.'), 10, [
        ('Forme neutre / nom + に違いない = c’est sûrement, à n’en pas douter (conviction du locuteur) : 犯人は あの 男に 違いない.', 'Plain form / noun + に違いない = it must be, without a doubt (the speaker’s conviction): 犯人は あの 男に 違いない.'),
        ('À l’écrit, 〜に相違ない a le même sens, en plus formel.', 'In writing, 〜に相違ない means the same, more formally.'),
        ('Forme neutre / nom + にすぎない = n’être que, rien de plus que : それは うわさに すぎない ; 一例に すぎない.', 'Plain form / noun + にすぎない = to be no more than, merely: それは うわさに すぎない; 一例に すぎない.'),
      ], [
        G('gram-n2-ni-chigainai', '〜に違いない', '〜にちがいない', '~ni chigainai', ('sûrement, sans aucun doute', 'surely, without a doubt')),
        G('gram-n2-ni-suginai', '〜にすぎない', '〜にすぎない', '~ni suginai', ('n’être que…, rien de plus que…', 'to be no more than…, merely…')),
        V('vocab-hannin', '犯人', 'はんにん', 'hannin', ('coupable, auteur (d’un délit)', 'culprit')),
        V('vocab-shouko', '証拠', 'しょうこ', 'shouko', ('preuve', 'evidence, proof')),
        V('vocab-uwasa', 'うわさ', 'うわさ', 'uwasa', ('rumeur', 'rumour')),
        V('vocab-guuzen', '偶然', 'ぐうぜん', 'guuzen', ('hasard, par hasard', 'coincidence, by chance')),
        K('kanji-n2-okasu', '犯', 'おかす', 'okasu', ('commettre, enfreindre', 'commit, violate'), ['ハン'], ['おか(す)'], 5),
        K('kanji-n2-shou', '証', 'しょう', 'shou', ('attester, témoignage', 'attest, testimony'), ['ショウ'], [], 12),
      ], [
        ex('部屋の 電気が ついて います。彼は 家に いるに 違いありません。', 'へやの でんきが ついて います。かれは いえに いるに ちがいありません。', 'La lumière de sa chambre est allumée. Il est sûrement chez lui.', 'The light in his room is on. He must surely be at home.'),
        ex('それは 証拠の ない うわさに すぎません。', 'それは しょうこの ない うわさに すぎません。', 'Ce n’est qu’une rumeur sans preuve.', 'That is no more than a rumour with no evidence.'),
      ], [
        FB(CHOOSE, 'こんなに 上手なのだから、たくさん 練習した＿。', ['に違いない', 'にすぎない', 'どころか'], 'に違いない', ('Conviction forte : 〜に違いない.', 'A strong conviction: 〜に違いない.'), ('Pour être aussi doué, il a sûrement beaucoup travaillé.', 'To be this good, he must surely have practised a lot.')),
        FB(CHOOSE, '二人が 同じ 店に いたのは、偶然＿。', ['にすぎない', 'に違いある', 'に限らない'], 'にすぎない', ('Rien de plus que : 〜にすぎない.', 'No more than: 〜にすぎない.'), ('Qu’ils se soient trouvés dans le même magasin n’est qu’un hasard.', 'That the two of them were in the same shop is no more than a coincidence.')),
        TF('犯人は この 中に いるに 違いない。', ('La personne a un simple soupçon, sans y croire vraiment.', 'The speaker has a mere suspicion and does not really believe it.'), FAUX, ('〜に違いない exprime une forte conviction.', '〜に違いない expresses a strong conviction.')),
        SO(ORDER('Ce n’est qu’un exemple parmi d’autres.', 'That is no more than one example.'), ['それは', '一つの', '例に', 'すぎません'], ('Nom + に すぎません.', 'Noun + に すぎません.')),
      ]),
    L('n2-zaru-wo-enai', ('Forcé de…, ne pas pouvoir s’empêcher de… : 〜ざるを得ない・〜ずにはいられない', 'Forced to…, cannot help…: 〜ざるを得ない・〜ずにはいられない'), ('Dire qu’on agit par nécessité, ou sous l’effet d’un élan qu’on ne retient pas.', 'Say that you act out of necessity, or from an impulse you cannot hold back.'), 10, [
        ('Radical en ない + ざるを得ない = ne pas avoir d’autre choix que de (à contrecœur) : 認めざるを 得ない. Irrégulier : する → せざるを得ない.', 'ない-stem + ざるを得ない = to have no choice but to (reluctantly): 認めざるを 得ない. Irregular: する → せざるを得ない.'),
        ('Radical en ない + ずにはいられない = ne pas pouvoir s’empêcher de (émotion, envie) : 笑わずには いられない. する → せずにはいられない.', 'ない-stem + ずにはいられない = cannot help …ing (emotion, urge): 笑わずには いられない. する → せずにはいられない.'),
        ('L’oral préfère 〜ないではいられない et 〜しかない ; ces deux formes appartiennent plutôt à l’écrit et au registre soigné.', 'Speech prefers 〜ないではいられない and 〜しかない; these two forms belong rather to writing and the careful register.'),
      ], [
        G('gram-n2-zaru-wo-enai', '〜ざるを得ない', '〜ざるをえない', '~zaru wo enai', ('ne pas avoir d’autre choix que de…', 'to have no choice but to…')),
        G('gram-n2-zu-ni-wa-irarenai', '〜ずにはいられない', '〜ずにはいられない', '~zu ni wa irarenai', ('ne pas pouvoir s’empêcher de…', 'cannot help …ing')),
        V('vocab-mitomemasu', '認めます', 'みとめます', 'mitomemasu', ('reconnaître, admettre', 'to acknowledge, to admit')),
        V('vocab-gaman', '我慢', 'がまん', 'gaman', ('patience, fait de se retenir', 'endurance, holding back')),
        V('vocab-waraimasu', '笑います', 'わらいます', 'waraimasu', ('rire', 'to laugh')),
        V('vocab-henkou', '変更', 'へんこう', 'henkou', ('modification', 'alteration, modification')),
        K('kanji-n2-mitomeru', '認', 'みとめる', 'mitomeru', ('reconnaître, approuver', 'recognise, approve'), ['ニン'], ['みと(める)'], 14),
        K('kanji-n2-eru', '得', 'える', 'eru', ('obtenir, gagner', 'obtain, gain'), ['トク'], ['え(る)', 'う(る)'], 11),
      ], [
        ex('雨が 強く なったので、試合は 中止せざるを 得ませんでした。', 'あめが つよく なったので、しあいは ちゅうしせざるを えませんでした。', 'La pluie s’étant renforcée, nous avons été contraints d’annuler le match.', 'As the rain grew heavier, we had no choice but to call off the match.'),
        ex('あの 映画を 見ると、泣かずには いられません。', 'あの えいがを みると、なかずには いられません。', 'Quand je vois ce film, je ne peux pas m’empêcher de pleurer.', 'When I watch that film, I cannot help crying.'),
      ], [
        FB(CHOOSE, '証拠が あるので、彼の 話を 信じ＿。', ['ざるを得ない', 'ずにはいられない', 'にすぎない'], 'ざるを得ない', ('Nécessité, à contrecœur : 〜ざるを得ない.', 'Necessity, reluctantly: 〜ざるを得ない.'), ('Puisqu’il y a une preuve, je suis bien forcé de le croire.', 'Since there is evidence, I have no choice but to believe him.')),
        FB(CHOOSE, '計画を 変更＿を 得なかった。', ['せざる', 'しざる', 'さざる'], 'せざる', ('する → せざるを得ない.', 'する → せざるを得ない.'), ('Nous avons été obligés de modifier le projet.', 'We had no choice but to alter the plan.')),
        FB(COMPLETE, 'その 話を 聞いて、笑わ＿ いられなかった。', ['ずには', 'ざるを', 'ないには'], 'ずには', ('Élan irrépressible : 〜ずには いられない.', 'An irrepressible impulse: 〜ずには いられない.'), ('En entendant cette histoire, je n’ai pas pu m’empêcher de rire.', 'Hearing that story, I could not help laughing.')),
        TF('熱が 高いので、今日は 休まざるを 得ない。', ('La personne se repose avec plaisir.', 'The speaker is glad to take the day off.'), FAUX, ('〜ざるを得ない : elle n’a pas le choix, et aurait préféré faire autrement.', '〜ざるを得ない: they have no choice, and would rather have done otherwise.')),
      ]),
    L('n2-mono-da', ('C’est ainsi, voilà ce qu’il faut faire : 〜ものだ・〜ことだ', 'That is how it is, that is the thing to do: 〜ものだ・〜ことだ'), ('Énoncer une vérité générale, évoquer une habitude passée, et donner un conseil.', 'State a general truth, recall a past habit, and give a piece of advice.'), 10, [
        ('Forme neutre + ものだ = il est dans la nature des choses que… : 人は だれでも 年を 取る ものだ. Elle dit aussi ce qui se fait : お年寄りには 席を ゆずる ものだ.', 'Plain form + ものだ = it is in the nature of things that…: 人は だれでも 年を 取る ものだ. It also says what is the done thing: お年寄りには 席を ゆずる ものだ.'),
        ('Verbe en た + ものだ = autrefois, je faisais souvent… (souvenir ému) : 子どもの ころ、この 川で よく 泳いだ ものだ.', 'た-form verb + ものだ = I often used to… (a fond memory): 子どもの ころ、この 川で よく 泳いだ ものだ.'),
        ('Verbe au dictionnaire ou en ない + ことだ = il faut, le mieux est de (conseil personnel) : 上手に なりたければ、毎日 練習する ことだ.', 'Dictionary or ない-form verb + ことだ = you should, the thing to do is (personal advice): 上手に なりたければ、毎日 練習する ことだ.'),
      ], [
        G('gram-n2-mono-da', '〜ものだ', '〜ものだ', '~mono da', ('c’est dans l’ordre des choses ; autrefois, je…', 'that is the way of things ; I used to…')),
        G('gram-n2-koto-da', '〜ことだ', '〜ことだ', '~koto da', ('il faut…, le mieux est de… (conseil)', 'you should…, the thing to do is… (advice)')),
        V('vocab-jinsei', '人生', 'じんせい', 'jinsei', ('vie (d’une personne)', 'life (a person’s)')),
        V('vocab-sunao', '素直', 'すなお', 'sunao', ('franc, sans détour ; docile', 'honest, open; obedient')),
        V('vocab-chuukoku', '忠告', 'ちゅうこく', 'chuukoku', ('conseil, mise en garde', 'advice, warning')),
        V('vocab-omoidoori', '思いどおり', 'おもいどおり', 'omoidoori', ('comme on le souhaite', 'just as one wishes')),
        K('kanji-n2-so', '素', 'そ', 'so', ('simple, brut', 'plain, raw'), ['ソ', 'ス'], [], 10),
        K('kanji-n2-naosu', '直', 'なおす', 'naosu', ('droit ; réparer', 'straight; fix'), ['チョク', 'ジキ'], ['なお(す)', 'ただ(ちに)'], 8),
      ], [
        ex('人生は 思いどおりに ならない ものです。', 'じんせいは おもいどおりに ならない ものです。', 'La vie ne se déroule jamais comme on le voudrait : c’est ainsi.', 'Life never goes just as one wishes: that is how it is.'),
        ex('試験に 合格したければ、毎日 少しずつ 勉強する ことです。', 'しけんに ごうかくしたければ、まいにち すこしずつ べんきょうする ことです。', 'Si tu veux réussir l’examen, le mieux est d’étudier un peu chaque jour.', 'If you want to pass the exam, the thing to do is study a little every day.'),
      ], [
        FB(CHOOSE, '学生の ころは、よく 友だちと 朝まで 話した＿。', ['ものだ', 'ことだ', '次第だ'], 'ものだ', ('Souvenir d’une habitude : verbe en た + ものだ.', 'Recalling a habit: た-form verb + ものだ.'), ('Quand j’étais étudiant, je parlais souvent avec mes amis jusqu’au matin.', 'In my student days, I often used to talk with friends until morning.')),
        FB(CHOOSE, '風邪を 早く 治したいなら、ゆっくり 休む＿。', ['ことだ', 'ものだ', '一方だ'], 'ことだ', ('Conseil : verbe au dictionnaire + ことだ.', 'Advice: dictionary-form verb + ことだ.'), ('Si tu veux guérir vite de ton rhume, le mieux est de bien te reposer.', 'If you want to get over your cold quickly, the thing to do is rest properly.')),
        TF('人の 忠告は 素直に 聞く ものだ。', ('La phrase énonce ce qu’il est normal de faire.', 'The sentence states what is the proper thing to do.'), VRAI, ('〜ものだ : c’est ce qui se fait, ce que le bon sens demande.', '〜ものだ: that is what one does, what common sense requires.')),
        DC(('Ton ami veut progresser en japonais et te demande conseil.', 'Your friend wants to get better at Japanese and asks for advice.'), [('友だち', 'どう すれば、日本語が 上手に なりますか。')], ('Ton ami demande comment progresser en japonais.', 'Your friend asks how to get better at Japanese.'), ['とにかく、毎日 話して みる ことです。', 'とにかく、毎日 話して みた ものです。', 'とにかく、毎日 話して みるに すぎません。'], 'とにかく、毎日 話して みる ことです。', ('Pour conseiller : 〜ことです.', 'To give advice: 〜ことです.')),
      ]),
  ])])

FINAL = {
  'slug': 'n2-final',
  'title': t(('Simulation JLPT N2', 'JLPT N2 simulation')),
  'region': REGION,
  'description': t(('Examen blanc non officiel du N2 : vocabulaire et kanji, grammaire, écoute. Chronométré, corrigé par compétence.', 'Unofficial N2 mock exam: vocabulary and kanji, grammar, listening. Timed, marked by skill.')),
  'exam': 'n2-mock',
  'chapters': [],
}

level = {
  'contentVersion': '2026.11.16b',
  'level': {'code': 'N2', 'title': t(('Intermédiaire avancé : nuances et japonais soigné', 'Upper intermediate: nuance and careful Japanese')), 'region': REGION, 'order': 2},
  'notice': t(('Les listes de vocabulaire et de kanji de Koto Quest sont alignées sur les compétences attendues au N2 mais ne constituent pas des listes officielles du JLPT.', 'Koto Quest’s vocabulary and kanji lists are aligned with the skills expected at N2 but are not official JLPT lists.')),
  'worlds': [W1, W2, W3, W4, W5, W6, W7, W8, FINAL],
}
t((REGION, 'The Summer Capital'))
os.makedirs(os.path.join(ROOT, 'content/n2'), exist_ok=True)
check_and_write(level, 'content/n2/n2.json', ['content/n5/n5.json', 'content/n4/n4.json', 'content/n3/n3.json'])
