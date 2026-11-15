# Extension du N4 : une deuxième série de leçons dans chaque île et une huitième île.
# Chaque texte est rédigé en français et en anglais : le français va dans content/n4/n4.json,
# l'anglais dans le dictionnaire content/i18n/en/content.json.
# Usage : python3 scripts/n4-extension.py   (idempotent : remplace les leçons déjà ajoutées)
import json, os, sys

ROOT = os.path.join(os.path.dirname(__file__), '..')
P_N4 = os.path.join(ROOT, 'content/n4/n4.json')
P_N5 = os.path.join(ROOT, 'content/n5/n5.json')
P_EXPR = os.path.join(ROOT, 'content/expressions/expressions.json')
P_DICT = os.path.join(ROOT, 'content/i18n/en/content.json')

EN = {}  # français → anglais

def t(pair):
    fr, en = pair
    if fr in EN and EN[fr] != en:
        raise SystemExit(f'Traduction contradictoire pour « {fr} » : « {EN[fr]} » / « {en} »')
    EN[fr] = en
    return fr

_DICO = json.load(open(os.path.join(os.path.dirname(__file__), '..', 'content/i18n/en/content.json'), encoding='utf-8'))

def item(slug, kind, front, reading, romaji, meaning, kanji=None):
    # Un sens identique à un sens existant garde la même traduction (ex. kanji 洗 et verbe 洗います).
    fr = meaning[0]
    meaning = (fr, EN.get(fr) or _DICO.get(fr) or meaning[1])
    it = {'slug': slug, 'kind': kind, 'front': front, 'reading': reading, 'romaji': romaji, 'meaning': t(meaning)}
    if kanji:
        on, kun, strokes = kanji
        it['kanji'] = {'onyomi': on, 'kunyomi': kun, 'strokes': strokes}
    return it

def G(slug, front, reading, romaji, meaning):
    return item(slug, 'grammar', front, reading, romaji, meaning)

def V(slug, front, reading, romaji, meaning):
    return item(slug, 'vocabulary', front, reading, romaji, meaning)

def K(slug, front, reading, romaji, meaning, on, kun, strokes):
    return item(slug, 'kanji', front, reading, romaji, meaning, (on, kun, strokes))

def ex(jp, reading, fr, en):
    return {'jp': jp, 'reading': reading, 'fr': t((fr, en))}

def FB(prompt, sentence, choices, answer, expl, tr, kind='fill_blank'):
    assert answer in choices, (sentence, answer)
    return {'type': kind, 'prompt': t(prompt), 'sentence': sentence, 'choices': choices, 'answer': answer, 'explanation': t(expl), 'translation': t(tr)}

def PC(prompt, sentence, choices, answer, expl, tr):
    return FB(prompt, sentence, choices, answer, expl, tr, 'particle_choice')

def SO(prompt, tokens, expl):
    return {'type': 'sentence_order', 'prompt': t(prompt), 'answer': tokens, 'explanation': t(expl)}

def TF(sentence, claim, answer, expl):
    return {'type': 'true_false', 'prompt': t(('Vrai ou faux ?', 'True or false?')), 'sentence': sentence, 'translation': t(claim), 'choices': [t(('Vrai', 'True')), t(('Faux', 'False'))], 'answer': t(answer), 'explanation': t(expl)}

def DC(prompt, lines, tr, choices, answer, expl):
    assert answer in choices
    return {'type': 'dialogue_choice', 'prompt': t(prompt), 'lines': [{'speaker': s, 'jp': j} for s, j in lines], 'translation': t(tr), 'choices': choices, 'answer': answer, 'explanation': t(expl)}

def L(slug, title, objective, minutes, explanation, items, examples, exercises):
    return {'slug': slug, 'title': t(title), 'objective': t(objective), 'minutes': minutes, 'explanation': [t(e) for e in explanation], 'items': items, 'examples': examples, 'exercises': exercises}

def CH(slug, title, lessons):
    return {'slug': slug, 'title': t(title), 'lessons': lessons}

COMPLETE = ('Complète la phrase.', 'Complete the sentence.')
CHOOSE = ('Choisis la forme qui convient.', 'Choose the right form.')
VRAI, FAUX = ('Vrai', 'True'), ('Faux', 'False')

# ═════════════════════════ Île 1 : la forme en て — Essayer, finir ═════════════════════════
W1 = CH('n4-w1-c2', ('Essayer et terminer', 'Trying and finishing'), [
  L('n4-te-miru', ('Essayer : 〜てみる', 'Trying: 〜てみる'), ('Dire qu’on essaie de faire quelque chose pour voir.', 'Say that you try doing something to see what it is like.'), 8, [
      ('Forme en て + みる (みます) = faire quelque chose « pour voir », essayer.', 'て-form + みる (みます) = do something “to see”, to try it out.'),
      ('食べてみます : je vais goûter. 着てみてもいいですか : je peux l’essayer ?', '食べてみます: I’ll taste it. 着てみてもいいですか: may I try it on?'),
      ('Avec 〜たい : 行ってみたいです = j’aimerais bien y aller (pour découvrir).', 'With 〜たい: 行ってみたいです = I’d like to go there (to discover it).'),
    ], [
      G('gram-te-miru', '〜てみる', '〜てみる', '~te miru', ('essayer de…, faire pour voir', 'try doing…, do something to see')),
      V('vocab-tsukurimasu', '作ります', 'つくります', 'tsukurimasu', ('fabriquer, préparer (un plat)', 'to make, to cook (a dish)')),
      V('vocab-ryouri', '料理', 'りょうり', 'ryouri', ('cuisine, plat cuisiné', 'cooking, dish')),
      V('vocab-kikimasu', '聞きます', 'ききます', 'kikimasu', ('écouter, demander', 'to listen, to ask')),
      V('vocab-kutsu', '靴', 'くつ', 'kutsu', ('chaussures', 'shoes')),
      K('kanji-tsukuru', '作', 'つくる', 'tsukuru', ('faire, fabriquer', 'make, create'), ['サク', 'サ'], ['つく(る)'], 7),
    ], [
      ex('日本の 料理を 作って みました。', 'にほんの りょうりを つくって みました。', 'J’ai essayé de préparer un plat japonais.', 'I tried making a Japanese dish.'),
      ex('この 靴を はいて みても いいですか。', 'この くつを はいて みても いいですか。', 'Je peux essayer ces chaussures ?', 'May I try these shoes on?'),
    ], [
      FB(COMPLETE, 'この ケーキ、おいしそうですね。ちょっと 食べて ＿。', ['みます', 'います', 'あります'], 'みます', ('〜てみます : goûter « pour voir ».', '〜てみます: taste it “to see”.'), ('Ce gâteau a l’air bon. Je vais y goûter un peu.', 'This cake looks good. I’ll try a little.')),
      FB(COMPLETE, '一度 富士山に 登って ＿ たいです。', ['み', 'い', 'あげ'], 'み', ('〜てみたい : avoir envie d’essayer.', '〜てみたい: want to try.'), ('J’aimerais gravir le mont Fuji une fois.', 'I’d like to climb Mount Fuji once.')),
      SO(('Remets dans l’ordre : « J’ai essayé d’écrire en kanji. »', 'Put in order: “I tried writing in kanji.”'), ['漢字で', '書いて', 'みました。'], ('Moyen (漢字で) + verbe en て + みました.', 'Means (漢字で) + verb in て-form + みました.')),
      TF('この 服を 着て みても いいですか。', ('La personne demande si elle peut essayer un vêtement.', 'The person asks whether they may try on some clothes.'), VRAI, ('着てみてもいいですか = « puis-je l’essayer ? ».', '着てみてもいいですか = “may I try it on?”.')),
    ]),
  L('n4-te-shimau', ('Finir, ou regretter : 〜てしまう', 'Finishing or regretting: 〜てしまう'), ('Exprimer qu’une action est complètement terminée, ou qu’on la regrette.', 'Say that an action is completely finished, or that you regret it.'), 9, [
      ('Forme en て + しまう (しまいます) a deux sens : « finir complètement » et « faire, hélas ».', 'て-form + しまう (しまいます) has two meanings: “finish completely” and “do, unfortunately”.'),
      ('宿題を やってしまいました : j’ai fini mes devoirs. 財布を 忘れてしまいました : j’ai oublié mon portefeuille (zut !).', '宿題を やってしまいました: I’ve finished my homework. 財布を 忘れてしまいました: I forgot my wallet (oops!).'),
      ('À l’oral, 〜てしまう devient souvent 〜ちゃう, et 〜でしまう devient 〜じゃう : 忘れちゃった.', 'In speech, 〜てしまう often becomes 〜ちゃう, and 〜でしまう becomes 〜じゃう: 忘れちゃった.'),
    ], [
      G('gram-te-shimau', '〜てしまう', '〜てしまう', '~te shimau', ('finir complètement ; faire (hélas)', 'finish completely; do (unfortunately)')),
      V('vocab-saifu', '財布', 'さいふ', 'saifu', ('portefeuille', 'wallet')),
      V('vocab-nakushimasu', 'なくします', 'なくします', 'nakushimasu', ('perdre (un objet)', 'to lose (an object)')),
      V('vocab-kowashimasu', '壊します', 'こわします', 'kowashimasu', ('casser, abîmer', 'to break, to damage')),
      V('vocab-zenbu', '全部', 'ぜんぶ', 'zenbu', ('tout, la totalité', 'all, everything')),
      K('kanji-owaru', '終', 'おわる', 'owaru', ('finir, se terminer', 'end, finish'), ['シュウ'], ['お(わる)', 'お(える)'], 11),
      K('kanji-wasureru', '忘', 'わすれる', 'wasureru', ('oublier', 'forget'), ['ボウ'], ['わす(れる)'], 7),
    ], [
      ex('ケーキを 全部 食べて しまいました。', 'ケーキを ぜんぶ たべて しまいました。', 'J’ai mangé tout le gâteau (oups).', 'I ate the whole cake (oops).'),
      ex('電車に かさを 忘れて しまいました。', 'でんしゃに かさを わすれて しまいました。', 'J’ai oublié mon parapluie dans le train.', 'I left my umbrella on the train.'),
    ], [
      FB(COMPLETE, 'スマホを 落として、壊して ＿。', ['しまいました', 'みました', 'おきました'], 'しまいました', ('Regret : 〜てしまいました.', 'Regret: 〜てしまいました.'), ('J’ai fait tomber mon téléphone et je l’ai cassé.', 'I dropped my phone and broke it.')),
      FB(CHOOSE, '財布を なくし＿。', ['ちゃった', 'じゃった', 'ちゃって'], 'ちゃった', ('なくして + しまった → なくしちゃった (familier).', 'なくして + しまった → なくしちゃった (casual).'), ('J’ai perdu mon portefeuille.', 'I lost my wallet.')),
      FB(CHOOSE, '本を 全部 読ん＿ しまいました。', ['で', 'て', 'た'], 'で', ('読みます → 読んで, puis しまいました.', '読みます → 読んで, then しまいました.'), ('J’ai lu le livre en entier.', 'I read the whole book.')),
      TF('宿題を やって しまいました。', ('Ici, 〜てしまいました peut signifier « j’ai fini mes devoirs ».', 'Here, 〜てしまいました can mean “I’ve finished my homework”.'), VRAI, ('Premier sens de 〜てしまう : achever complètement.', 'First meaning of 〜てしまう: complete an action.')),
    ]),
])

# ═════════════════════════ Île 2 : permis ou interdit — Obligations et conseils ═════════════════════════
W2 = CH('n4-w2-c2', ('Obligations et conseils', 'Obligations and advice'), [
  L('n4-nakereba', ('Devoir : 〜なければなりません', 'Must: 〜なければなりません'), ('Dire ce qu’on doit faire, et ce qu’on n’est pas obligé de faire.', 'Say what you must do, and what you don’t have to do.'), 10, [
      ('Forme en ない sans い + ければなりません = devoir : 行かない → 行かなければなりません.', 'ない-form minus い + ければなりません = must: 行かない → 行かなければなりません.'),
      ('À l’oral : 〜なきゃ ou 〜ないと (いけない) : もう 帰らなきゃ = je dois rentrer.', 'In speech: 〜なきゃ or 〜ないと (いけない): もう 帰らなきゃ = I have to go home.'),
      ('Ne pas être obligé : forme en ない sans い + くてもいいです : 来なくてもいいです.', 'Not having to: ない-form minus い + くてもいいです: 来なくてもいいです.'),
    ], [
      G('gram-nakereba', '〜なければなりません', '〜なければなりません', '~nakereba narimasen', ('devoir, être obligé de…', 'must, have to…')),
      G('gram-nakutemo-ii', '〜なくてもいいです', '〜なくてもいいです', '~nakutemo ii desu', ('ne pas être obligé de…', 'don’t have to…')),
      V('vocab-haraimasu', '払います', 'はらいます', 'haraimasu', ('payer', 'to pay')),
      V('vocab-kanarazu', '必ず', 'かならず', 'kanarazu', ('sans faute, toujours', 'without fail, always')),
      V('vocab-shimekiri', '締め切り', 'しめきり', 'shimekiri', ('date limite', 'deadline')),
      K('kanji-kanarazu', '必', 'かならず', 'kanarazu', ('nécessaire, sans faute', 'necessary, certain'), ['ヒツ'], ['かなら(ず)'], 5),
      K('kanji-harau', '払', 'はらう', 'harau', ('payer, balayer', 'pay, sweep away'), ['フツ'], ['はら(う)'], 5),
    ], [
      ex('明日までに レポートを 出さなければ なりません。', 'あしたまでに レポートを ださなければ なりません。', 'Je dois rendre le rapport d’ici demain.', 'I have to hand in the report by tomorrow.'),
      ex('土曜日は 学校へ 行かなくても いいです。', 'どようびは がっこうへ いかなくても いいです。', 'Le samedi, je ne suis pas obligé d’aller à l’école.', 'On Saturdays, I don’t have to go to school.'),
    ], [
      FB(CHOOSE, '毎日 薬を 飲ま＿ なりません。', ['なければ', 'なくても', 'ないで'], 'なければ', ('Obligation : 〜なければなりません.', 'Obligation: 〜なければなりません.'), ('Je dois prendre un médicament tous les jours.', 'I have to take medicine every day.')),
      FB(CHOOSE, '名前は 書か＿ いいです。', ['なくても', 'なければ', 'ないと'], 'なくても', ('Absence d’obligation : 〜なくてもいいです.', 'No obligation: 〜なくてもいいです.'), ('Tu n’es pas obligé d’écrire ton nom.', 'You don’t have to write your name.')),
      DC(('Ton ami doit partir. Que dit-il ?', 'Your friend has to leave. What does he say?'), [('Ken', 'もう 十時だ！')], ('Ken remarque qu’il est déjà 22 h.', 'Ken notices it is already 10 p.m.'), ['帰らなきゃ。', '帰らなくてもいい。', '帰ってみる。'], '帰らなきゃ。', ('〜なきゃ = forme orale de 〜なければ(ならない).', '〜なきゃ = spoken form of 〜なければ(ならない).')),
      TF('お金は 払わなくても いいです。', ('Cela veut dire qu’il faut absolument payer.', 'This means you absolutely have to pay.'), FAUX, ('〜なくてもいい = on n’est pas obligé : ici, c’est gratuit.', '〜なくてもいい = you don’t have to: here it is free.')),
    ]),
  L('n4-hou-ga-ii', ('Conseiller : 〜たほうがいいです', 'Giving advice: 〜たほうがいいです'), ('Donner un conseil ou mettre en garde.', 'Give advice or a warning.'), 8, [
      ('Forme en た + ほうがいいです = tu ferais mieux de… : 早く 寝たほうがいいです.', 'た-form + ほうがいいです = you had better…: 早く 寝たほうがいいです.'),
      ('Pour déconseiller, on garde la forme en ない : 無理しないほうがいいです.', 'To advise against, use the ない-form: 無理しないほうがいいです.'),
      ('Le conseil est assez direct : on l’adoucit avec 〜と思います ou よ.', 'The advice is fairly direct: soften it with 〜と思います or よ.'),
    ], [
      G('gram-hou-ga-ii', '〜たほうがいい・〜ないほうがいい', '〜たほうがいい・〜ないほうがいい', '~ta hou ga ii / ~nai hou ga ii', ('tu ferais mieux de… / de ne pas…', 'you had better… / better not…')),
      V('vocab-hayaku', '早く', 'はやく', 'hayaku', ('tôt, vite', 'early, quickly')),
      V('vocab-muri', '無理', 'むり', 'muri', ('impossible, excessif (forcer)', 'impossible, too much (overdoing it)')),
      V('vocab-isha', '医者', 'いしゃ', 'isha', ('médecin', 'doctor')),
      V('vocab-yasumimasu', '休みます', 'やすみます', 'yasumimasu', ('se reposer, être absent', 'to rest, to take time off')),
      K('kanji-okiru', '起', 'おきる', 'okiru', ('se lever, se produire', 'get up, occur'), ['キ'], ['お(きる)', 'お(こす)'], 10),
    ], [
      ex('熱が ありますね。医者に 行った ほうが いいですよ。', 'ねつが ありますね。いしゃに いった ほうが いいですよ。', 'Tu as de la fièvre. Tu devrais aller chez le médecin.', 'You have a fever. You should see a doctor.'),
      ex('あまり 無理を しない ほうが いいです。', 'あまり むりを しない ほうが いいです。', 'Tu ferais mieux de ne pas trop forcer.', 'You had better not overdo it.'),
    ], [
      FB(CHOOSE, '明日は 早いから、早く 寝＿ ほうが いいです。', ['た', 'る', 'て'], 'た', ('Conseil : forme en た + ほうがいい.', 'Advice: た-form + ほうがいい.'), ('Demain tu commences tôt : tu devrais te coucher tôt.', 'You start early tomorrow: you should go to bed early.')),
      FB(CHOOSE, 'かぜの ときは、お酒を 飲ま＿ ほうが いいです。', ['ない', 'なかった', 'なくて'], 'ない', ('Déconseiller : forme en ない (pas en た) + ほうがいい.', 'Advising against: ない-form (not た) + ほうがいい.'), ('Quand on est enrhumé, mieux vaut ne pas boire d’alcool.', 'When you have a cold, it’s better not to drink alcohol.')),
      SO(('Remets dans l’ordre : « Tu devrais te reposer. »', 'Put in order: “You should rest.”'), ['休んだ', 'ほうが', 'いいです。'], ('Forme en た + ほうが + いいです.', 'た-form + ほうが + いいです.')),
      DC(('Ton ami tousse depuis trois jours. Quel conseil lui donnes-tu ?', 'Your friend has been coughing for three days. What advice do you give?'), [('Aya', 'ずっと せきが 出るんです。')], ('Aya dit qu’elle tousse sans arrêt.', 'Aya says she keeps coughing.'), ['病院に 行った ほうが いいよ。', '病院に 行かなくても いいよ。', '病院に 行って しまったよ。'], '病院に 行った ほうが いいよ。', ('Conseil : 〜たほうがいい.', 'Advice: 〜たほうがいい.')),
    ]),
])

# ═════════════════════════ Île 3 : expériences et projets — Activités et intentions ═════════════════════════
W3 = CH('n4-w3-c2', ('Activités et intentions', 'Activities and intentions'), [
  L('n4-tari', ('Énumérer : 〜たり〜たりします', 'Listing: 〜たり〜たりします'), ('Citer quelques activités parmi d’autres.', 'Mention a few activities among others.'), 9, [
      ('Forme en た + り, deux fois, puis します : 本を 読んだり、音楽を 聞いたり します.', 'た-form + り, twice, then します: 本を 読んだり、音楽を 聞いたり します.'),
      ('La liste n’est pas complète : « entre autres choses, je lis, j’écoute de la musique… ».', 'The list is not complete: “among other things, I read, I listen to music…”.'),
      ('Le temps se marque à la fin : 〜たりしました (passé), 〜たりしたいです (envie).', 'Tense goes at the end: 〜たりしました (past), 〜たりしたいです (wish).'),
    ], [
      G('gram-tari', '〜たり〜たりする', '〜たり〜たりする', '~tari ~tari suru', ('faire entre autres… et…', 'do things like… and…')),
      V('vocab-souji', '掃除', 'そうじ', 'souji', ('ménage', 'cleaning')),
      V('vocab-sentaku', '洗濯', 'せんたく', 'sentaku', ('lessive (laver le linge)', 'laundry (washing clothes)')),
      V('vocab-shuumatsu', '週末', 'しゅうまつ', 'shuumatsu', ('week-end', 'weekend')),
      V('vocab-arau', '洗います', 'あらいます', 'araimasu', ('laver', 'to wash')),
      K('kanji-arau', '洗', 'あらう', 'arau', ('laver', 'wash'), ['セン'], ['あら(う)'], 9),
    ], [
      ex('週末は 掃除を したり、洗濯を したり します。', 'しゅうまつは そうじを したり、せんたくを したり します。', 'Le week-end, je fais entre autres le ménage et la lessive.', 'At weekends, I do things like cleaning and laundry.'),
      ex('京都で お寺を 見たり、写真を 撮ったり しました。', 'きょうとで おてらを みたり、しゃしんを とったり しました。', 'À Kyoto, j’ai visité des temples, pris des photos…', 'In Kyoto, I saw temples, took photos and so on.'),
    ], [
      FB(CHOOSE, '休みの 日は、映画を 見＿、ゲームを したり します。', ['たり', 'て', 'たら'], 'たり', ('Les deux verbes prennent 〜たり.', 'Both verbs take 〜たり.'), ('Les jours de congé, je regarde des films, je joue aux jeux vidéo…', 'On days off, I watch films, play video games and so on.')),
      FB(CHOOSE, '公園で 走ったり、泳＿ しました。', ['いだり', 'いたり', 'んだり'], 'いだり', ('泳ぎます → 泳いだ → 泳いだり.', '泳ぎます → 泳いだ → 泳いだり.'), ('Au parc, j’ai couru, nagé…', 'At the park, I ran, swam and so on.')),
      SO(('Remets dans l’ordre : « J’ai lavé la voiture, nettoyé la chambre… »', 'Put in order: “I washed the car, cleaned the room…”'), ['車を', '洗ったり、', '部屋を', '掃除したり', 'しました。'], ('Chaque action en 〜たり, et します à la fin porte le temps.', 'Each action in 〜たり, and the final します carries the tense.')),
      TF('日曜日は 本を 読んだり、料理を したり します。', ('Le dimanche, la personne ne fait que lire.', 'On Sundays, the person only reads.'), FAUX, ('〜たり〜たり : elle lit, cuisine, entre autres.', '〜たり〜たり: she reads, cooks, among other things.')),
    ]),
  L('n4-ikou', ('Intention : la forme volitive 〜(よ)うと思います', 'Intention: the volitional 〜(よ)うと思います'), ('Former la forme volitive et dire ce qu’on compte faire.', 'Form the volitional and say what you plan to do.'), 10, [
      ('Groupe 2 : る → よう (食べる → 食べよう). Groupe 1 : u → ō (行く → 行こう, 飲む → 飲もう).', 'Group 2: る → よう (食べる → 食べよう). Group 1: u → ō (行く → 行こう, 飲む → 飲もう).'),
      ('Irréguliers : する → しよう, 来る → 来よう (こよう).', 'Irregular: する → しよう, 来る → 来よう (こよう).'),
      ('Seule, c’est « faisons… » entre amis. Avec 〜と思います : « je compte… » : 来年 日本へ 行こうと思います.', 'On its own it means “let’s…” among friends. With 〜と思います: “I’m thinking of…”: 来年 日本へ 行こうと思います.'),
    ], [
      G('gram-ikou', '〜(よ)う', '〜(よ)う', '~(y)ou', ('forme volitive (faisons…)', 'volitional form (let’s…)')),
      G('gram-ikou-to-omou', '〜(よ)うと思います', '〜(よ)うとおもいます', '~(y)ou to omoimasu', ('je compte…, je pense faire…', 'I’m thinking of doing…')),
      V('vocab-naraimasu', '習います', 'ならいます', 'naraimasu', ('apprendre (avec quelqu’un)', 'to learn (from someone)')),
      V('vocab-hajimemasu', '始めます', 'はじめます', 'hajimemasu', ('commencer', 'to start')),
      V('vocab-rainen', '来年', 'らいねん', 'rainen', ('l’année prochaine', 'next year')),
      K('kanji-hajimeru', '始', 'はじめる', 'hajimeru', ('commencer', 'begin'), ['シ'], ['はじ(める)', 'はじ(まる)'], 8),
      K('kanji-narau', '習', 'ならう', 'narau', ('apprendre', 'learn'), ['シュウ'], ['なら(う)'], 11),
    ], [
      ex('来年から 柔道を 習おうと 思います。', 'らいねんから じゅうどうを ならおうと おもいます。', 'Je compte apprendre le judo à partir de l’année prochaine.', 'I’m thinking of learning judo from next year.'),
      ex('疲れたね。ちょっと 休もう。', 'つかれたね。ちょっと やすもう。', 'On est fatigués. Faisons une petite pause.', 'We’re tired. Let’s take a short break.'),
    ], [
      FB(CHOOSE, '今晩は 早く 寝＿と 思います。', ['よう', 'ろう', 'こう'], 'よう', ('寝る (groupe 2) → 寝よう.', '寝る (group 2) → 寝よう.'), ('Ce soir, je compte me coucher tôt.', 'Tonight, I’m thinking of going to bed early.')),
      FB(CHOOSE, 'いっしょに 昼ごはんを 食べに 行＿！', ['こう', 'きよう', 'くう'], 'こう', ('行く → 行こう (u → ō).', '行く → 行こう (u → ō).'), ('Allons déjeuner ensemble !', 'Let’s go and have lunch together!')),
      FB(CHOOSE, '明日から ダイエットを ＿と 思います。', ['しよう', 'すろう', 'さよう'], 'しよう', ('する → しよう (irrégulier).', 'する → しよう (irregular).'), ('Je compte commencer un régime demain.', 'I’m thinking of starting a diet tomorrow.')),
      SO(('Remets dans l’ordre : « Je compte commencer le piano. »', 'Put in order: “I’m thinking of starting piano.”'), ['ピアノを', '始めようと', '思います。'], ('Objet + forme volitive + と思います.', 'Object + volitional + と思います.')),
    ]),
])

# ═════════════════════════ Île 4 : comparer — Apparences et suppositions ═════════════════════════
W4 = CH('n4-w4-c2', ('Apparences et suppositions', 'Appearances and guesses'), [
  L('n4-sou-mitai', ('Avoir l’air : 〜そうです', 'Looking like: 〜そうです'), ('Décrire ce qui semble, d’après ce qu’on voit.', 'Describe how something seems, from what you see.'), 9, [
      ('Adjectif en い sans い + そうです : おいしそう (ça a l’air bon). Adjectif en な + そう : 元気そう.', 'い-adjective minus い + そうです: おいしそう (looks tasty). な-adjective + そう: 元気そう.'),
      ('Verbe en ます sans ます + そうです : 雨が 降りそうです = on dirait qu’il va pleuvoir.', 'Verb ます-stem + そうです: 雨が 降りそうです = it looks like it will rain.'),
      ('Exceptions : いい → よさそう, ない → なさそう. Devant un nom : おいしそうな ケーキ.', 'Exceptions: いい → よさそう, ない → なさそう. Before a noun: おいしそうな ケーキ.'),
    ], [
      G('gram-sou-yousu', '〜そうです（様子）', '〜そうです', '~sou desu', ('avoir l’air…, on dirait que…', 'look…, seem as if…')),
      V('vocab-ame', '雨', 'あめ', 'ame', ('pluie', 'rain')),
      V('vocab-tanoshii', '楽しい', 'たのしい', 'tanoshii', ('agréable, amusant', 'fun, enjoyable')),
      V('vocab-tsumetai', '冷たい', 'つめたい', 'tsumetai', ('froid (au toucher)', 'cold (to the touch)')),
      V('vocab-ochimasu', '落ちます', 'おちます', 'ochimasu', ('tomber (objet)', 'to fall (object)')),
      K('kanji-ame', '雨', 'あめ', 'ame', ('pluie', 'rain'), ['ウ'], ['あめ', 'あま'], 8),
      K('kanji-furu', '降', 'ふる', 'furu', ('tomber (pluie), descendre', 'fall (rain), get off'), ['コウ'], ['ふ(る)', 'お(りる)'], 10),
    ], [
      ex('空が 暗いですね。雨が 降りそうです。', 'そらが くらいですね。あめが ふりそうです。', 'Le ciel est sombre. On dirait qu’il va pleuvoir.', 'The sky is dark. It looks like it’s going to rain.'),
      ex('その ラーメン、おいしそうですね。', 'その ラーメン、おいしそうですね。', 'Ces ramen ont l’air délicieux.', 'Those ramen look delicious.'),
    ], [
      FB(CHOOSE, 'この ケーキは とても あま＿です。', ['そう', 'いそう', 'さそう'], 'そう', ('あまい → あまそう (on retire い).', 'あまい → あまそう (drop い).'), ('Ce gâteau a l’air très sucré.', 'This cake looks very sweet.')),
      FB(CHOOSE, '天気が よ＿ですね。', ['さそう', 'そう', 'いそう'], 'さそう', ('Exception : いい → よさそう.', 'Exception: いい → よさそう.'), ('Il a l’air de faire beau.', 'The weather looks nice.')),
      FB(CHOOSE, 'あ、コップが 落ち＿です！', ['そう', 'るそう', 'たそう'], 'そう', ('落ちます → 落ちそう (sur le point de tomber).', '落ちます → 落ちそう (about to fall).'), ('Ah, le verre va tomber !', 'Oh, the glass is about to fall!')),
      TF('田中さんは 楽しそうです。', ('D’après son allure, Tanaka a l’air de s’amuser.', 'Judging by how he looks, Tanaka seems to be having fun.'), VRAI, ('〜そう décrit l’apparence : 楽しそう = a l’air content.', '〜そう describes appearance: 楽しそう = looks happy.')),
    ]),
  L('n4-kamoshirenai', ('Probable ou possible : 〜でしょう・〜かもしれません', 'Probable or possible: 〜でしょう・〜かもしれません'), ('Nuancer une supposition selon son degré de certitude.', 'Hedge a guess according to how sure you are.'), 9, [
      ('〜でしょう = sans doute (assez sûr). 明日は 晴れるでしょう : demain, il fera sans doute beau.', '〜でしょう = probably (fairly sure). 明日は 晴れるでしょう: it will probably be sunny tomorrow.'),
      ('〜かもしれません = peut-être (moins sûr). 遅れるかもしれません : je serai peut-être en retard.', '〜かもしれません = maybe (less sure). 遅れるかもしれません: I may be late.'),
      ('Les deux suivent la forme neutre ; avec un nom ou un adjectif en な, pas de だ : 雨かもしれません.', 'Both follow the plain form; with a noun or な-adjective, drop だ: 雨かもしれません.'),
    ], [
      G('gram-deshou', '〜でしょう', '〜でしょう', '~deshou', ('sans doute, probablement', 'probably, likely')),
      G('gram-kamoshirenai', '〜かもしれません', '〜かもしれません', '~kamoshiremasen', ('peut-être, il se peut que…', 'maybe, might…')),
      V('vocab-haremasu', '晴れます', 'はれます', 'haremasu', ('se dégager (beau temps)', 'to clear up (fine weather)')),
      V('vocab-tenkiyohou', '天気予報', 'てんきよほう', 'tenkiyohou', ('prévisions météo', 'weather forecast')),
      V('vocab-osoku', '遅く', 'おそく', 'osoku', ('tard', 'late')),
      K('kanji-hareru', '晴', 'はれる', 'hareru', ('beau temps, se dégager', 'clear up, sunny'), ['セイ'], ['は(れる)'], 12),
    ], [
      ex('天気予報に よると、明日は 晴れるでしょう。', 'てんきよほうに よると、あしたは はれるでしょう。', 'D’après la météo, il fera sans doute beau demain.', 'According to the forecast, it will probably be sunny tomorrow.'),
      ex('電車が 遅れて いるので、少し 遅く なるかもしれません。', 'でんしゃが おくれて いるので、すこし おそく なるかもしれません。', 'Le train a du retard, je serai peut-être un peu en retard.', 'The train is delayed, so I may be a little late.'),
    ], [
      FB(CHOOSE, 'あの 人は 先生＿ しれません。', ['かも', 'でしょう', 'そう'], 'かも', ('Nom + かもしれません (sans だ).', 'Noun + かもしれません (no だ).'), ('Cette personne est peut-être professeur.', 'That person might be a teacher.')),
      FB(COMPLETE, '午後から 雪が 降る＿。かさを 持って 行って ください。', ['でしょう', 'たい', 'てしまう'], 'でしょう', ('Prévision probable : 〜でしょう.', 'Likely forecast: 〜でしょう.'), ('Il neigera sans doute cet après-midi. Prends un parapluie.', 'It will probably snow this afternoon. Take an umbrella.')),
      DC(('On te demande si Mari viendra à la fête. Tu n’en es pas sûr.', 'You are asked whether Mari will come to the party. You are not sure.'), [('Yu', 'まりさんも パーティーに 来ますか。')], ('Yu demande si Mari vient aussi à la fête.', 'Yu asks whether Mari is coming to the party too.'), ['来るかもしれません。', '来て みました。', '来なければ なりません。'], '来るかもしれません。', ('Incertitude : 〜かもしれません.', 'Uncertainty: 〜かもしれません.')),
      TF('明日は 雨かもしれません。', ('La personne est certaine qu’il pleuvra demain.', 'The speaker is certain it will rain tomorrow.'), FAUX, ('かもしれません = peut-être, ce n’est pas une certitude.', 'かもしれません = maybe, not a certainty.')),
    ]),
])

# ═════════════════════════ Île 5 : opinions et raisons — Rapporter et justifier ═════════════════════════
W5 = CH('n4-w5-c2', ('Rapporter et justifier', 'Reporting and justifying'), [
  L('n4-sou-denbun', ('On dit que… : 〜そうです (ouï-dire)', 'I hear that…: 〜そうです (hearsay)'), ('Rapporter une information entendue ou lue.', 'Pass on information you heard or read.'), 9, [
      ('Forme neutre + そうです = il paraît que… : 明日は 雨が 降るそうです.', 'Plain form + そうです = I hear that…: 明日は 雨が 降るそうです.'),
      ('Attention : 降りそう (on dirait qu’il va pleuvoir) ≠ 降るそう (il paraît qu’il va pleuvoir).', 'Careful: 降りそう (looks like rain) ≠ 降るそう (I hear it will rain).'),
      ('La source se donne avec 〜によると : ニュースに よると = selon les informations.', 'Give the source with 〜によると: ニュースに よると = according to the news.'),
    ], [
      G('gram-sou-denbun', '〜そうです（伝聞）', '〜そうです', '~sou desu (denbun)', ('il paraît que…, on dit que…', 'I hear that…, they say that…')),
      G('gram-ni-yoru-to', '〜によると', '〜によると', '~ni yoru to', ('d’après…, selon…', 'according to…')),
      V('vocab-nyuusu', 'ニュース', 'ニュース', 'nyuusu', ('actualités, informations', 'news')),
      V('vocab-kekkon', '結婚', 'けっこん', 'kekkon', ('mariage', 'marriage')),
      V('vocab-kikoemasu', '聞こえます', 'きこえます', 'kikoemasu', ('s’entendre, être audible', 'to be audible, can be heard')),
      K('kanji-kiku', '聞', 'きく', 'kiku', ('entendre, écouter, demander', 'hear, listen, ask'), ['ブン', 'モン'], ['き(く)', 'き(こえる)'], 14),
      K('kanji-iu', '言', 'いう', 'iu', ('dire, mot', 'say, word'), ['ゲン', 'ゴン'], ['い(う)', 'こと'], 7),
    ], [
      ex('ニュースに よると、台風が 来るそうです。', 'ニュースに よると、たいふうが くるそうです。', 'D’après les informations, un typhon arrive.', 'According to the news, a typhoon is coming.'),
      ex('山田さんは 来月 結婚するそうです。', 'やまださんは らいげつ けっこんするそうです。', 'Il paraît que M. Yamada se marie le mois prochain.', 'I hear Mr Yamada is getting married next month.'),
    ], [
      FB(CHOOSE, '天気予報に よると、明日は 寒い＿です。', ['そう', 'さそう', 'でしょう'], 'そう', ('Ouï-dire : adjectif complet + そうです (寒いそう).', 'Hearsay: full adjective + そうです (寒いそう).'), ('D’après la météo, il fera froid demain.', 'According to the forecast, it will be cold tomorrow.')),
      FB(CHOOSE, 'リンさんの 話に よると、あの 店は 安い＿。', ['そうです', 'みたいに', 'ほうが'], 'そうです', ('Information rapportée : 〜そうです.', 'Reported information: 〜そうです.'), ('D’après Lin, ce magasin est bon marché.', 'According to Lin, that shop is cheap.')),
      TF('明日 雪が 降るそうです。', ('La personne rapporte une information entendue.', 'The speaker is passing on something they heard.'), VRAI, ('Forme neutre (降る) + そうです = ouï-dire.', 'Plain form (降る) + そうです = hearsay.')),
      TF('雪が 降りそうです。', ('La personne rapporte ce que dit la météo.', 'The speaker is quoting the weather forecast.'), FAUX, ('Radical (降り) + そう = « on dirait », d’après ce qu’on voit.', 'Stem (降り) + そう = “looks like”, from what you see.')),
    ]),
  L('n4-shi', ('Plusieurs raisons : 〜し、〜し', 'Several reasons: 〜し、〜し'), ('Donner plusieurs raisons ou qualités à la suite.', 'Give several reasons or qualities in a row.'), 8, [
      ('Forme neutre + し relie des raisons qui vont dans le même sens : 安いし、おいしいし.', 'Plain form + し links reasons pointing the same way: 安いし、おいしいし.'),
      ('Avec un nom ou un adjectif en な : だし : 静かだし、駅から 近いし.', 'With a noun or な-adjective: だし: 静かだし、駅から 近いし.'),
      ('Souvent, on termine par la conclusion : 〜し、〜し、この 店が 好きです.', 'You often end with the conclusion: 〜し、〜し、この 店が 好きです.'),
    ], [
      G('gram-shi', '〜し、〜し', '〜し、〜し', '~shi, ~shi', ('et en plus…, d’ailleurs… (raisons)', 'and what’s more… (reasons)')),
      V('vocab-yachin', '家賃', 'やちん', 'yachin', ('loyer', 'rent')),
      V('vocab-apaato', 'アパート', 'アパート', 'apaato', ('appartement', 'apartment, flat')),
      V('vocab-koutsuu', '交通', 'こうつう', 'koutsuu', ('transports, circulation', 'transport, traffic')),
      K('kanji-oya', '親', 'おや', 'oya', ('parent, intime', 'parent, intimate'), ['シン'], ['おや', 'した(しい)'], 16),
      K('kanji-ben', '便', 'べん', 'ben', ('pratique, courrier', 'convenience, mail'), ['ベン', 'ビン'], ['たよ(り)'], 9),
    ], [
      ex('この アパートは 駅から 近いし、家賃も 安いです。', 'この アパートは えきから ちかいし、やちんも やすいです。', 'Cet appartement est près de la gare, et en plus le loyer est bas.', 'This flat is close to the station, and the rent is low too.'),
      ex('東京は 交通が 便利だし、店も 多いし、住みやすいです。', 'とうきょうは こうつうが べんりだし、みせも おおいし、すみやすいです。', 'Tokyo, c’est pratique pour les transports, il y a plein de magasins : on y vit bien.', 'Tokyo has handy transport and lots of shops: it’s an easy place to live.'),
    ], [
      FB(CHOOSE, 'この 町は 静か＿、きれいだし、好きです。', ['だし', 'し', 'なし'], 'だし', ('Adjectif en な : 静かだし.', 'な-adjective: 静かだし.'), ('J’aime cette ville : elle est calme, et propre en plus.', 'I like this town: it’s quiet, and clean too.')),
      FB(CHOOSE, '今日は 頭も 痛い＿、熱も あるし、休みます。', ['し', 'だし', 'から'], 'し', ('Adjectif en い : 痛いし.', 'い-adjective: 痛いし.'), ('Aujourd’hui j’ai mal à la tête, et de la fièvre : je reste chez moi.', 'Today I have a headache and a fever too, so I’ll stay home.')),
      SO(('Remets dans l’ordre : « C’est bon marché, et délicieux en plus. »', 'Put in order: “It’s cheap, and delicious too.”'), ['安いし、', 'おいしいし、', 'いい', '店です。'], ('Raison + し, raison + し, puis la conclusion.', 'Reason + し, reason + し, then the conclusion.')),
      TF('先生は 親切だし、おもしろいです。', ('Le professeur a au moins deux qualités.', 'The teacher has at least two good qualities.'), VRAI, ('〜し accumule : gentil, et en plus intéressant.', '〜し stacks them: kind, and interesting too.')),
    ]),
])

# ═════════════════════════ Île 6 : donner et recevoir — Demandes et buts ═════════════════════════
W6 = CH('n4-w6-c2', ('Demandes polies et buts', 'Polite requests and goals'), [
  L('n4-te-kuremasenka', ('Demander un service : 〜てくれませんか', 'Asking a favour: 〜てくれませんか'), ('Demander poliment, puis très poliment, un service.', 'Ask for a favour politely, then very politely.'), 8, [
      ('〜てくれませんか = tu ne voudrais pas… ? (plus doux que 〜てください).', '〜てくれませんか = won’t you…? (softer than 〜てください).'),
      ('〜てもらえませんか = pourrais-je avoir que tu… ? Encore plus poli : 〜ていただけませんか.', '〜てもらえませんか = could I have you…? Even more polite: 〜ていただけませんか.'),
      ('Avec un supérieur ou un inconnu, 〜ていただけませんか est le choix sûr.', 'With a superior or a stranger, 〜ていただけませんか is the safe choice.'),
    ], [
      G('gram-te-kuremasenka', '〜てくれませんか', '〜てくれませんか', '~te kuremasen ka', ('tu ne voudrais pas… ? (demande)', 'won’t you…? (request)')),
      G('gram-te-itadakemasenka', '〜ていただけませんか', '〜ていただけませんか', '~te itadakemasen ka', ('pourriez-vous… ? (très poli)', 'could you possibly…? (very polite)')),
      V('vocab-okurimasu', '送ります', 'おくります', 'okurimasu', ('envoyer, raccompagner', 'to send, to see off')),
      V('vocab-shiryou', '資料', 'しりょう', 'shiryou', ('documents, dossier', 'documents, materials')),
      V('vocab-mou-sukoshi', 'もう少し', 'もうすこし', 'mou sukoshi', ('encore un peu', 'a little more')),
      K('kanji-okuru', '送', 'おくる', 'okuru', ('envoyer', 'send'), ['ソウ'], ['おく(る)'], 9),
      K('kanji-oshieru', '教', 'おしえる', 'oshieru', ('enseigner', 'teach'), ['キョウ'], ['おし(える)', 'おそ(わる)'], 11),
    ], [
      ex('すみません、写真を 撮って くれませんか。', 'すみません、しゃしんを とって くれませんか。', 'Excusez-moi, vous voulez bien me prendre en photo ?', 'Excuse me, would you take a photo of me?'),
      ex('資料を メールで 送って いただけませんか。', 'しりょうを メールで おくって いただけませんか。', 'Pourriez-vous m’envoyer les documents par e-mail ?', 'Could you possibly send me the documents by email?'),
    ], [
      FB(COMPLETE, 'もう少し ゆっくり 話して ＿か。', ['くれません', 'あげません', 'しまいません'], 'くれません', ('Demande : 〜てくれませんか.', 'Request: 〜てくれませんか.'), ('Tu pourrais parler un peu plus lentement ?', 'Could you speak a little more slowly?')),
      DC(('Tu demandes à ton chef de relire ton rapport. Que dis-tu ?', 'You ask your boss to check your report. What do you say?'), [('部長', 'どうしましたか。')], ('Ton chef demande ce qu’il y a.', 'Your boss asks what is up.'), ['レポートを 見て いただけませんか。', 'レポートを 見て くれ。', 'レポートを 見て あげます。'], 'レポートを 見て いただけませんか。', ('Avec un supérieur : 〜ていただけませんか.', 'With a superior: 〜ていただけませんか.')),
      SO(('Remets dans l’ordre : « Tu voudrais bien m’apprendre le japonais ? »', 'Put in order: “Would you teach me Japanese?”'), ['日本語を', '教えて', 'くれませんか。'], ('Objet + verbe en て + くれませんか.', 'Object + verb in て-form + くれませんか.')),
      TF('窓を 開けて もらえませんか。', ('La personne demande qu’on ouvre la fenêtre.', 'The speaker is asking someone to open the window.'), VRAI, ('〜てもらえませんか = demande polie.', '〜てもらえませんか = polite request.')),
    ]),
  L('n4-tame-ni', ('Dans le but de : 〜ために・〜ように', 'In order to: 〜ために・〜ように'), ('Exprimer un but.', 'Express a purpose.'), 10, [
      ('Verbe volontaire (forme du dictionnaire) + ために : 留学する ために、お金を ためます.', 'Volitional verb (dictionary form) + ために: 留学する ために、お金を ためます.'),
      ('Nom + の ために = pour… : 家族の ために 働きます.', 'Noun + の ために = for…: 家族の ために 働きます.'),
      ('Avec un état ou un verbe non volontaire (potentiel, ない) : 〜ように : 聞こえるように 大きい 声で 話します.', 'With a state or non-volitional verb (potential, ない): 〜ように: 聞こえるように 大きい 声で 話します.'),
    ], [
      G('gram-tame-ni', '〜ために', '〜ために', '~tame ni', ('pour, dans le but de…', 'in order to, for the sake of…')),
      G('gram-you-ni', '〜ように', '〜ように', '~you ni', ('pour que…, afin de pouvoir…', 'so that…, so as to be able to…')),
      V('vocab-tamemasu', 'ためます', 'ためます', 'tamemasu', ('économiser, mettre de côté', 'to save up')),
      V('vocab-hatarakimasu', '働きます', 'はたらきます', 'hatarakimasu', ('travailler', 'to work')),
      V('vocab-undou', '運動', 'うんどう', 'undou', ('exercice physique', 'physical exercise')),
      K('kanji-hataraku', '働', 'はたらく', 'hataraku', ('travailler', 'work'), ['ドウ'], ['はたら(く)'], 13),
      K('kanji-hakobu', '運', 'はこぶ', 'hakobu', ('transporter, chance', 'carry, luck'), ['ウン'], ['はこ(ぶ)'], 12),
    ], [
      ex('日本の 大学に 入る ために、毎日 勉強して います。', 'にほんの だいがくに はいる ために、まいにち べんきょうして います。', 'J’étudie tous les jours pour entrer dans une université japonaise.', 'I study every day in order to get into a Japanese university.'),
      ex('忘れないように、メモを 書きます。', 'わすれないように、メモを かきます。', 'Je prends des notes pour ne pas oublier.', 'I write notes so that I don’t forget.'),
    ], [
      FB(CHOOSE, '健康の ＿、毎朝 運動します。', ['ために', 'ように', 'そうに'], 'ために', ('Nom + の ために.', 'Noun + の ために.'), ('Je fais du sport tous les matins pour ma santé.', 'I exercise every morning for my health.')),
      FB(CHOOSE, '後ろの 人も 見える＿、字を 大きく 書きます。', ['ように', 'ために', 'たら'], 'ように', ('見える n’est pas volontaire : 〜ように.', '見える is not volitional: 〜ように.'), ('J’écris gros pour que les gens du fond voient aussi.', 'I write big so that people at the back can see too.')),
      FB(CHOOSE, '車を 買う＿、アルバイトを して います。', ['ために', 'ように', 'ので'], 'ために', ('買う est volontaire : 〜ために.', '買う is volitional: 〜ために.'), ('Je fais un petit boulot pour acheter une voiture.', 'I have a part-time job to buy a car.')),
      TF('風邪を ひかないように、手を 洗います。', ('On se lave les mains pour ne pas attraper froid.', 'You wash your hands so as not to catch a cold.'), VRAI, ('Forme en ない + ように = afin de ne pas….', 'ない-form + ように = so as not to….')),
    ]),
])

# ═════════════════════════ Île 7 : si, quand et pouvoir — Autres conditions ═════════════════════════
W7 = CH('n4-w7-c2', ('Autres conditions et capacités', 'More conditions and abilities'), [
  L('n4-ba', ('La condition : 〜ば', 'Conditional: 〜ば'), ('Former la condition en ば et l’utiliser.', 'Form the ば-conditional and use it.'), 10, [
      ('Verbes : u → e + ば : 行く → 行けば, 食べる → 食べれば, する → すれば, 来る → 来れば (くれば).', 'Verbs: u → e + ば: 行く → 行けば, 食べる → 食べれば, する → すれば, 来る → 来れば (くれば).'),
      ('Adjectif en い : い → ければ : 安い → 安ければ. いい → よければ. Négation : 〜なければ.', 'い-adjective: い → ければ: 安い → 安ければ. いい → よければ. Negative: 〜なければ.'),
      ('〜ば insiste sur la condition : « il suffit de… », « si seulement… » : 急げば 間に合います.', '〜ば stresses the condition: “all you need is…”, “if only…”: 急げば 間に合います.'),
    ], [
      G('gram-ba', '〜ば', '〜ば', '~ba', ('si… (condition)', 'if… (condition)')),
      V('vocab-isogimasu', '急ぎます', 'いそぎます', 'isogimasu', ('se dépêcher', 'to hurry')),
      V('vocab-maniaimasu', '間に合います', 'まにあいます', 'maniaimasu', ('être à l’heure, avoir le temps', 'to make it in time')),
      V('vocab-yokereba', 'よければ', 'よければ', 'yokereba', ('si ça te va, si tu veux', 'if you like, if that’s OK')),
      V('vocab-wakarimasu', '分かります', 'わかります', 'wakarimasu', ('comprendre', 'to understand')),
      K('kanji-isogu', '急', 'いそぐ', 'isogu', ('urgent, se dépêcher', 'hurry, sudden'), ['キュウ'], ['いそ(ぐ)'], 9),
    ], [
      ex('今 急げば、電車に 間に合います。', 'いま いそげば、でんしゃに まにあいます。', 'Si on se dépêche maintenant, on aura le train.', 'If we hurry now, we’ll catch the train.'),
      ex('よければ、いっしょに 行きませんか。', 'よければ、いっしょに いきませんか。', 'Si tu veux, on y va ensemble ?', 'If you like, shall we go together?'),
    ], [
      FB(CHOOSE, 'この 薬を 飲め＿、すぐ よく なりますよ。', ['ば', 'たら', 'て'], 'ば', ('飲む → 飲めば.', '飲む → 飲めば.'), ('Si tu prends ce médicament, tu iras vite mieux.', 'If you take this medicine, you’ll soon feel better.')),
      FB(CHOOSE, '天気が ＿、ピクニックに 行きましょう。', ['よければ', 'いければ', 'よいば'], 'よければ', ('いい → よければ.', 'いい → よければ.'), ('S’il fait beau, allons pique-niquer.', 'If the weather is nice, let’s go for a picnic.')),
      FB(CHOOSE, '分からない ことが ＿、聞いて ください。', ['あれば', 'あるば', 'あったば'], 'あれば', ('ある → あれば.', 'ある → あれば.'), ('S’il y a quelque chose que tu ne comprends pas, demande.', 'If there’s anything you don’t understand, please ask.')),
      FB(CHOOSE, '安＿、買います。', ['ければ', 'いば', 'ければば'], 'ければ', ('安い → 安ければ.', '安い → 安ければ.'), ('Si c’est bon marché, je l’achète.', 'If it’s cheap, I’ll buy it.')),
    ]),
  L('n4-koto-ga-dekiru', ('Savoir faire : 〜ことができます', 'Being able to: 〜ことができます'), ('Dire ce qu’on sait ou peut faire avec 〜ことができます.', 'Say what you can do with 〜ことができます.'), 8, [
      ('Forme du dictionnaire + ことができます = pouvoir, savoir : 漢字を 書く ことが できます.', 'Dictionary form + ことができます = can, be able to: 漢字を 書く ことが できます.'),
      ('Plus formel que la forme potentielle (書けます), on le voit dans les règlements : ここで 食べる ことが できます.', 'More formal than the potential form (書けます), it appears in rules: ここで 食べる ことが できます.'),
      ('Avec un nom d’activité : 運転が できます, 日本語が できます.', 'With an activity noun: 運転が できます, 日本語が できます.'),
    ], [
      G('gram-koto-ga-dekiru', '〜ことができます', '〜ことができます', '~koto ga dekimasu', ('pouvoir faire, savoir faire', 'can do, be able to')),
      V('vocab-unten', '運転', 'うんてん', 'unten', ('conduite (d’un véhicule)', 'driving (a vehicle)')),
      V('vocab-piano', 'ピアノ', 'ピアノ', 'piano', ('piano', 'piano')),
      V('vocab-hikimasu', '弾きます', 'ひきます', 'hikimasu', ('jouer (d’un instrument à cordes ou clavier)', 'to play (a string or keyboard instrument)')),
      K('kanji-ten', '転', 'てん', 'ten', ('tourner, rouler, tomber', 'turn, roll, fall'), ['テン'], ['ころ(ぶ)', 'ころ(がる)'], 11),
      K('kanji-uta', '歌', 'うた', 'uta', ('chanson, chanter', 'song, sing'), ['カ'], ['うた', 'うた(う)'], 14),
    ], [
      ex('姉は ピアノを 弾く ことが できます。', 'あねは ピアノを ひく ことが できます。', 'Ma grande sœur sait jouer du piano.', 'My older sister can play the piano.'),
      ex('この 図書館では 本を 三冊 借りる ことが できます。', 'この としょかんでは ほんを さんさつ かりる ことが できます。', 'Dans cette bibliothèque, on peut emprunter trois livres.', 'At this library, you can borrow three books.'),
    ], [
      FB(CHOOSE, '父は 車の 運転＿ できます。', ['が', 'を', 'に'], 'が', ('Nom + が できます.', 'Noun + が できます.'), ('Mon père sait conduire.', 'My father can drive.')),
      FB(COMPLETE, '日本語の 歌を 歌う ＿ できます。', ['ことが', 'ことを', 'のが'], 'ことが', ('Verbe + ことが できます.', 'Verb + ことが できます.'), ('Je sais chanter des chansons en japonais.', 'I can sing songs in Japanese.')),
      SO(('Remets dans l’ordre : « On peut nager ici. »', 'Put in order: “You can swim here.”'), ['ここで', '泳ぐ', 'ことが', 'できます。'], ('Lieu + で, verbe + ことができます.', 'Place + で, verb + ことができます.')),
      TF('弟は 漢字を 読む ことが できません。', ('Le petit frère sait lire les kanji.', 'The younger brother can read kanji.'), FAUX, ('できません = il ne peut pas.', 'できません = he cannot.')),
    ]),
])

# ═════════════════════════ Île 8 (nouvelle) : politesse et voix ═════════════════════════
W8 = {
  'slug': 'n4-w8',
  'title': t(('Politesse et voix', 'Politeness and voice')),
  'region': 'Archipel des voyageurs',
  'description': t(('Parler avec respect, et dire ce qu’on subit ou ce qu’on fait faire.', 'Speak respectfully, and say what is done to you or what you make others do.')),
  'boss': {
    'name': t(('Le Seigneur des Bonnes Manières', 'The Lord of Good Manners')),
    'glyph': '礼',
    'intro': t(('Ce seigneur exige des formules impeccables. Une faute de politesse, et il te renvoie au port !', 'This lord demands flawless phrasing. One slip in politeness, and he sends you back to port!')),
  },
  'chapters': [
    CH('n4-w8-c1', ('Parler avec respect', 'Speaking respectfully'), [
      L('n4-sonkeigo', ('Respect : le langage honorifique (尊敬語)', 'Respect: honorific language (尊敬語)'), ('Utiliser les verbes honorifiques courants pour parler des actions d’autrui.', 'Use common honorific verbs to talk about other people’s actions.'), 10, [
          ('Le 尊敬語 élève la personne dont on parle (client, supérieur). On ne l’utilise jamais pour soi.', '尊敬語 raises the person you talk about (customer, superior). Never use it about yourself.'),
          ('Verbes spéciaux : いる・行く・来る → いらっしゃる ; 食べる・飲む → 召し上がる ; 言う → おっしゃる ; 見る → ご覧になる.', 'Special verbs: いる・行く・来る → いらっしゃる; 食べる・飲む → 召し上がる; 言う → おっしゃる; 見る → ご覧になる.'),
          ('Forme générale : お + radical + になります : 待つ → お待ちになります.', 'General pattern: お + stem + になります: 待つ → お待ちになります.'),
        ], [
          G('gram-sonkeigo', 'お〜になります', 'お〜になります', 'o~ni narimasu', ('forme honorifique (actions d’autrui)', 'honorific form (others’ actions)')),
          V('vocab-irasshaimasu', 'いらっしゃいます', 'いらっしゃいます', 'irasshaimasu', ('être, aller, venir (honorifique)', 'to be, go, come (honorific)')),
          V('vocab-meshiagarimasu', '召し上がります', 'めしあがります', 'meshiagarimasu', ('manger, boire (honorifique)', 'to eat, drink (honorific)')),
          V('vocab-osshaimasu', 'おっしゃいます', 'おっしゃいます', 'osshaimasu', ('dire (honorifique)', 'to say (honorific)')),
          V('vocab-goran', 'ご覧になります', 'ごらんになります', 'goran ni narimasu', ('regarder (honorifique)', 'to look (honorific)')),
          K('kanji-mesu', '召', 'めす', 'mesu', ('convoquer ; (honorifique) prendre', 'summon; (honorific) partake'), ['ショウ'], ['め(す)'], 5),
          K('kanji-sama', '様', 'さま', 'sama', ('M./Mme (très poli), manière', 'Mr/Ms (very polite), manner'), ['ヨウ'], ['さま'], 14),
        ], [
          ex('先生は 何時ごろ いらっしゃいますか。', 'せんせいは なんじごろ いらっしゃいますか。', 'Vers quelle heure le professeur viendra-t-il ?', 'Around what time will the teacher come?'),
          ex('どうぞ 召し上がって ください。', 'どうぞ めしあがって ください。', 'Je vous en prie, servez-vous.', 'Please, help yourself.'),
        ], [
          FB(CHOOSE, '社長は 今 会議室に ＿。', ['いらっしゃいます', 'まいります', 'おります'], 'いらっしゃいます', ('Le président (un autre) : いらっしゃいます.', 'The president (someone else): いらっしゃいます.'), ('Le président est actuellement en salle de réunion.', 'The president is in the meeting room now.')),
          FB(CHOOSE, '先生が そう ＿。', ['おっしゃいました', '申しました', '言いました'], 'おっしゃいました', ('Paroles d’un supérieur : おっしゃいました.', 'A superior’s words: おっしゃいました.'), ('C’est ce que le professeur a dit.', 'That’s what the teacher said.')),
          FB(CHOOSE, '少々 お待ち＿ ください。', ['に なって', 'して', 'いたして'], 'に なって', ('お + radical + になってください.', 'お + stem + になってください.'), ('Veuillez patienter un instant.', 'Please wait a moment.')),
          TF('わたしは 毎朝 パンを 召し上がります。', ('Cette phrase est correcte.', 'This sentence is correct.'), FAUX, ('On n’utilise pas le 尊敬語 pour soi : 食べます ou いただきます.', 'Don’t use 尊敬語 about yourself: 食べます or いただきます.')),
        ]),
      L('n4-kenjougo', ('Modestie : le langage humble (謙譲語)', 'Modesty: humble language (謙譲語)'), ('Parler de ses propres actions avec humilité.', 'Talk about your own actions humbly.'), 10, [
          ('Le 謙譲語 abaisse ses propres actions pour respecter l’autre (souvent au travail).', '謙譲語 lowers your own actions to show respect to the other person (often at work).'),
          ('Verbes spéciaux : 行く・来る → まいる ; いる → おる ; 言う → 申す ; 食べる・もらう → いただく ; する → いたす.', 'Special verbs: 行く・来る → まいる; いる → おる; 言う → 申す; 食べる・もらう → いただく; する → いたす.'),
          ('Forme générale : お + radical + します : 持つ → お持ちします (je vous le porte).', 'General pattern: お + stem + します: 持つ → お持ちします (let me carry it).'),
        ], [
          G('gram-kenjougo', 'お〜します', 'お〜します', 'o~shimasu', ('forme humble (mes actions)', 'humble form (my actions)')),
          V('vocab-mairimasu', 'まいります', 'まいります', 'mairimasu', ('aller, venir (humble)', 'to go, come (humble)')),
          V('vocab-moushimasu', '申します', 'もうします', 'moushimasu', ('dire, s’appeler (humble)', 'to say, to be called (humble)')),
          V('vocab-itashimasu', 'いたします', 'いたします', 'itashimasu', ('faire (humble)', 'to do (humble)')),
          V('vocab-orimasu', 'おります', 'おります', 'orimasu', ('être, se trouver (humble)', 'to be (humble)')),
          K('kanji-mousu', '申', 'もうす', 'mousu', ('dire (humble), déclarer', 'say (humble), declare'), ['シン'], ['もう(す)'], 5),
          K('kanji-mairu', '参', 'まいる', 'mairu', ('aller (humble), participer', 'go (humble), participate'), ['サン'], ['まい(る)'], 8),
        ], [
          ex('はじめまして。マルタンと 申します。', 'はじめまして。マルタンと もうします。', 'Enchanté. Je m’appelle Martin.', 'Nice to meet you. My name is Martin.'),
          ex('お荷物を お持ちしましょうか。', 'おにもつを おもちしましょうか。', 'Voulez-vous que je porte vos bagages ?', 'Shall I carry your luggage?'),
        ], [
          FB(CHOOSE, 'はじめまして。田中と ＿。', ['申します', 'おっしゃいます', '言います'], '申します', ('Se présenter humblement : 〜と申します.', 'Humble self-introduction: 〜と申します.'), ('Enchanté. Je m’appelle Tanaka.', 'Nice to meet you. My name is Tanaka.')),
          FB(CHOOSE, '明日 三時に そちらへ ＿。', ['まいります', 'いらっしゃいます', '召し上がります'], 'まいります', ('Mon propre déplacement : まいります.', 'My own movement: まいります.'), ('Je viendrai chez vous demain à 15 h.', 'I will come to you tomorrow at 3 p.m.')),
          FB(CHOOSE, '駅まで お送り ＿。', ['します', 'に なります', 'なさいます'], 'します', ('Action humble : お + radical + します.', 'Humble action: お + stem + します.'), ('Je vous raccompagne jusqu’à la gare.', 'I’ll see you to the station.')),
          DC(('Au téléphone, on demande si M. Sato est là. Tu es M. Sato.', 'On the phone, someone asks if Mr Sato is there. You are Mr Sato.'), [('客', '佐藤さんは いらっしゃいますか。')], ('Un client demande si M. Sato est présent.', 'A customer asks whether Mr Sato is in.'), ['はい、わたしが 佐藤で ございます。', 'はい、佐藤が いらっしゃいます。', 'はい、佐藤さまです。'], 'はい、わたしが 佐藤で ございます。', ('On ne s’applique jamais 尊敬語 ni さま : でございます est la forme humble.', 'Never use 尊敬語 or さま about yourself: でございます is the humble form.')),
        ]),
    ]),
    CH('n4-w8-c2', ('Subir et faire faire', 'Being done to and making others do'), [
      L('n4-ukemi', ('Le passif : 〜られる', 'The passive: 〜られる'), ('Former le passif et dire ce qu’on a subi.', 'Form the passive and say what happened to you.'), 10, [
          ('Groupe 2 : る → られる (見る → 見られる). Groupe 1 : u → a + れる (書く → 書かれる, 言う → 言われる).', 'Group 2: る → られる (見る → 見られる). Group 1: u → a + れる (書く → 書かれる, 言う → 言われる).'),
          ('Irréguliers : する → される, 来る → 来られる (こられる). L’auteur de l’action est marqué par に.', 'Irregular: する → される, 来る → 来られる (こられる). The doer is marked with に.'),
          ('Le passif japonais exprime souvent un désagrément : 雨に 降られました = la pluie m’est tombée dessus.', 'The Japanese passive often expresses a nuisance: 雨に 降られました = I got caught in the rain.'),
        ], [
          G('gram-ukemi', '〜られる・〜れる（受身）', '〜られる・〜れる', '~rareru / ~reru (ukemi)', ('forme passive (subir)', 'passive form (be done to)')),
          V('vocab-shikarimasu', '叱ります', 'しかります', 'shikarimasu', ('gronder', 'to scold')),
          V('vocab-homemasu', 'ほめます', 'ほめます', 'homemasu', ('féliciter, complimenter', 'to praise')),
          V('vocab-yobimasu', '呼びます', 'よびます', 'yobimasu', ('appeler, inviter', 'to call, to invite')),
          V('vocab-nusumimasu', '盗みます', 'ぬすみます', 'nusumimasu', ('voler, dérober', 'to steal')),
          K('kanji-yobu', '呼', 'よぶ', 'yobu', ('appeler', 'call'), ['コ'], ['よ(ぶ)'], 8),
        ], [
          ex('子どもの とき、よく 母に 叱られました。', 'こどもの とき、よく ははに しかられました。', 'Enfant, je me faisais souvent gronder par ma mère.', 'As a child, I was often scolded by my mother.'),
          ex('電車の 中で 財布を 盗まれました。', 'でんしゃの なかで さいふを ぬすまれました。', 'On m’a volé mon portefeuille dans le train.', 'I had my wallet stolen on the train.'),
        ], [
          FB(CHOOSE, '先生に ほめ＿ました。', ['られ', 'させ', 'れ'], 'られ', ('ほめる (groupe 2) → ほめられる.', 'ほめる (group 2) → ほめられる.'), ('J’ai été félicité par le professeur.', 'I was praised by the teacher.')),
          FB(CHOOSE, '名前を 呼＿ました。', ['ばれ', 'ばせ', 'びられ'], 'ばれ', ('呼ぶ → 呼ばれる (u → a + れる).', '呼ぶ → 呼ばれる (u → a + れる).'), ('On m’a appelé (par mon nom).', 'My name was called.')),
          PC(('Choisis la particule qui marque l’auteur de l’action.', 'Choose the particle that marks the doer.'), '弟＿ ケーキを 食べられました。', ['に', 'を', 'で'], 'に', ('Au passif, l’auteur est marqué par に.', 'In the passive, the doer takes に.'), ('Mon petit frère m’a mangé mon gâteau.', 'My little brother ate my cake (on me).')),
          TF('雨に 降られました。', ('La personne a été gênée par la pluie.', 'The speaker was inconvenienced by the rain.'), VRAI, ('Passif de désagrément : la pluie m’est tombée dessus.', 'Nuisance passive: the rain fell on me.')),
        ]),
      L('n4-shieki', ('Le causatif : 〜させる', 'The causative: 〜させる'), ('Dire qu’on fait ou laisse faire quelque chose à quelqu’un.', 'Say that you make or let someone do something.'), 10, [
          ('Groupe 2 : る → させる (食べる → 食べさせる). Groupe 1 : u → a + せる (行く → 行かせる). する → させる, 来る → 来させる.', 'Group 2: る → させる (食べる → 食べさせる). Group 1: u → a + せる (行く → 行かせる). する → させる, 来る → 来させる.'),
          ('Sens : faire faire ou laisser faire : 子どもに 野菜を 食べさせます.', 'Meaning: make or let someone do: 子どもに 野菜を 食べさせます.'),
          ('Demande polie de faire soi-même : 〜させてください : 私に 払わせて ください = laissez-moi payer.', 'Politely asking to do it yourself: 〜させてください: 私に 払わせて ください = let me pay.'),
        ], [
          G('gram-shieki', '〜させる・〜せる（使役）', '〜させる・〜せる', '~saseru / ~seru (shieki)', ('forme causative (faire faire)', 'causative form (make someone do)')),
          G('gram-sasete-kudasai', '〜させてください', '〜させてください', '~sasete kudasai', ('laissez-moi…, permettez-moi de…', 'let me…, allow me to…')),
          V('vocab-renshuu', '練習', 'れんしゅう', 'renshuu', ('entraînement, exercice', 'practice, training')),
          V('vocab-yasai', '野菜', 'やさい', 'yasai', ('légumes', 'vegetables')),
          K('kanji-tsukau', '使', 'つかう', 'tsukau', ('utiliser, envoyé', 'use, envoy'), ['シ'], ['つか(う)'], 8),
          K('kanji-nomu', '飲', 'のむ', 'nomu', ('boire', 'drink'), ['イン'], ['の(む)'], 12),
        ], [
          ex('コーチは 選手に 毎日 走らせます。', 'コーチは せんしゅに まいにち はしらせます。', 'L’entraîneur fait courir les joueurs tous les jours.', 'The coach makes the players run every day.'),
          ex('すみません、少し 考えさせて ください。', 'すみません、すこし かんがえさせて ください。', 'Excusez-moi, laissez-moi réfléchir un peu.', 'Sorry, let me think about it a little.'),
        ], [
          FB(CHOOSE, '母は 弟に 部屋を 掃除＿ました。', ['させ', 'され', 'し'], 'させ', ('する → させる (faire faire).', 'する → させる (make someone do).'), ('Ma mère a fait ranger sa chambre à mon petit frère.', 'My mother made my little brother clean his room.')),
          FB(CHOOSE, '先生は 学生に 本を 読＿ました。', ['ませ', 'まれ', 'ませられ'], 'ませ', ('読む → 読ませる (u → a + せる).', '読む → 読ませる (u → a + せる).'), ('Le professeur a fait lire un livre aux étudiants.', 'The teacher had the students read a book.')),
          DC(('Au restaurant, tu veux payer pour ton ami. Que dis-tu ?', 'At a restaurant, you want to pay for your friend. What do you say?'), [('友だち', 'じゃ、払いますね。')], ('Ton ami s’apprête à payer.', 'Your friend is about to pay.'), ['今日は わたしに 払わせて ください。', '今日は わたしに 払われて ください。', '今日は 払って しまいました。'], '今日は わたしに 払わせて ください。', ('〜させてください = laissez-moi….', '〜させてください = let me….')),
          TF('子どもに 野菜を 食べさせます。', ('C’est l’enfant qui fait manger les parents.', 'The child makes the parents eat.'), FAUX, ('に marque celui qu’on fait agir : l’enfant mange.', 'に marks the person made to act: the child eats.')),
        ]),
    ]),
  ],
}

# ═════════════════════════ Assemblage et contrôles ═════════════════════════
def items_of(levels):
    for lvl in levels:
        for w in lvl['worlds']:
            for c in w['chapters']:
                for l in c['lessons']:
                    yield from l['items']

n4 = json.load(open(P_N4, encoding='utf-8'))
n5 = json.load(open(P_N5, encoding='utf-8'))
expr = json.load(open(P_EXPR, encoding='utf-8'))
dico = json.load(open(P_DICT, encoding='utf-8'))

# Idempotent : on retire d'abord ce que ce script a déjà ajouté.
NEW_CHAPTERS = {'n4-w1': W1, 'n4-w2': W2, 'n4-w3': W3, 'n4-w4': W4, 'n4-w5': W5, 'n4-w6': W6, 'n4-w7': W7}
n4['worlds'] = [w for w in n4['worlds'] if w['slug'] != 'n4-w8']
for w in n4['worlds']:
    w['chapters'] = [c for c in w['chapters'] if not c['slug'].endswith('-c2')]
    if w['slug'] in NEW_CHAPTERS:
        w['chapters'].append(NEW_CHAPTERS[w['slug']])
final = [w for w in n4['worlds'] if w['slug'] == 'n4-final']
n4['worlds'] = [w for w in n4['worlds'] if w['slug'] != 'n4-final'] + [W8] + final

new_items = [it for w in list(NEW_CHAPTERS.values()) for l in w['lessons'] for it in l['items']] + [it for c in W8['chapters'] for l in c['lessons'] for it in l['items']]
old = {}
for it in items_of([n5, json.load(open(P_N4, encoding='utf-8'))]):
    old[it['slug']] = it
for th in expr['themes']:
    for it in th['expressions']:
        old.setdefault(it['slug'], it)
problems = []
seen_new = {}
for it in new_items:
    if it['slug'] in old and old[it['slug']] != it :
        problems.append(f"slug déjà utilisé autrement : {it['slug']}")
    if it['slug'] in seen_new and seen_new[it['slug']] != it:
        problems.append(f"slug en double dans l'extension : {it['slug']}")
    seen_new[it['slug']] = it
    if it['kind'] == 'vocabulary':
        for o in old.values():
            if o.get('kind') == 'vocabulary' and o['front'] == it['front'] and o['slug'] != it['slug']:
                problems.append(f"mot déjà présent : {it['front']} ({o['slug']})")

# Sens : deux sens français différents ne doivent pas avoir la même traduction anglaise.
full = {**dico, **EN}
by_en = {}
for it in list(old.values()) + new_items:
    e = full.get(it['meaning'], it['meaning'])
    by_en.setdefault(e, set()).add(it['meaning'])
for e, frs in by_en.items():
    if len(frs) > 1:
        problems.append(f"sens anglais en double : {e} ← {' | '.join(frs)}")
# Traductions déjà présentes mais différentes
for fr, en in EN.items():
    if fr in dico and dico[fr] != en:
        problems.append(f"traduction existante différente : {fr} → {dico[fr]} / {en}")
if problems:
    print('\n'.join(problems))
    sys.exit(1)

n4['contentVersion'] = '2026.11.10'
json.dump(n4, open(P_N4, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
dico.update(EN)
json.dump(dico, open(P_DICT, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
lessons = sum(len(c['lessons']) for w in n4['worlds'] for c in w['chapters'])
nitems = len({it['slug'] for w in n4['worlds'] for c in w['chapters'] for l in c['lessons'] for it in l['items']})
print(f'N4 : {len(n4["worlds"])} îles, {lessons} leçons, {nitems} notions ; {len(EN)} traductions')
