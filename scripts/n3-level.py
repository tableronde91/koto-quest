# Niveau N3 : 8 îles, 24 leçons et un examen blanc (français + anglais).
# Usage : python3 scripts/n3-level.py   (réécrit content/n3/n3.json)
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from kq_content import *

REGION = 'Cimes enneigées'

# ═════════════════════════ Île 1 : impressions et déductions ═════════════════════════
W1 = WORLD('n3-w1', ('Impressions et déductions', 'Impressions and deductions'), REGION,
  ('Dire ce qui semble, ce qu’on a entendu dire et ce qui devrait être vrai.', 'Say how things seem, what you have heard, and what ought to be true.'),
  (('Le Renard des Apparences', 'The Fox of Appearances'), '狐', ('Ce renard change de forme à chaque instant. Sauras-tu dire ce qui semble vrai, et ce qui l’est sûrement ?', 'This fox changes shape at every moment. Can you tell what seems true from what surely is?')),
  [CH('n3-w1-c1', ('Sembler, paraître, devoir être', 'Seeming, appearing, ought to be'), [
    L('n3-you-da', ('On dirait que… : 〜ようだ・〜みたいだ', 'It seems that…: 〜ようだ・〜みたいだ'), ('Exprimer une impression fondée sur ce qu’on perçoit, et comparer.', 'Express an impression based on what you perceive, and make comparisons.'), 10, [
        ('〜ようだ suit la forme neutre : 留守のようだ, 雨が 降ったようだ. Avec un nom : の ; avec un adjectif en な : な.', '〜ようだ follows the plain form: 留守のようだ, 雨が 降ったようだ. With a noun: の; with a な-adjective: な.'),
        ('〜みたいだ a le même sens, en plus familier, et se colle directement : 留守みたいだ, 風邪を ひいたみたい.', '〜みたいだ means the same, more casually, and attaches directly: 留守みたいだ, 風邪を ひいたみたい.'),
        ('Comparaison : まるで 夢のようだ (comme un rêve). Devant un nom : 〜ような ; devant un verbe : 〜ように.', 'Comparison: まるで 夢のようだ (like a dream). Before a noun: 〜ような; before a verb: 〜ように.'),
      ], [
        G('gram-n3-you-da', '〜ようだ', '〜ようだ', '~you da', ('on dirait que…, il semble que… (neutre)', 'it seems that…, it looks as if… (neutral)')),
        G('gram-n3-mitai', '〜みたいだ', '〜みたいだ', '~mitai da', ('on dirait…, comme… (familier)', 'looks like…, like… (casual)')),
        V('vocab-rusu', '留守', 'るす', 'rusu', ('absence (de chez soi)', 'being away from home')),
        V('vocab-guai', '具合', 'ぐあい', 'guai', ('état, condition (santé, appareil)', 'condition, state (health, device)')),
        V('vocab-marude', 'まるで', 'まるで', 'marude', ('tout à fait comme, on croirait', 'just like, as if')),
        V('vocab-yume', '夢', 'ゆめ', 'yume', ('rêve', 'dream')),
        K('kanji-tomeru', '留', 'とめる', 'tomeru', ('retenir, rester', 'detain, stay'), ['リュウ', 'ル'], ['と(める)', 'と(まる)'], 10),
        K('kanji-mamoru', '守', 'まもる', 'mamoru', ('protéger, garder', 'protect, guard'), ['シュ', 'ス'], ['まも(る)'], 6),
      ], [
        ex('電気が 消えて います。田中さんは 留守のようです。', 'でんきが きえて います。たなかさんは るすのようです。', 'La lumière est éteinte. On dirait que M. Tanaka est absent.', 'The lights are off. It seems Mr Tanaka is out.'),
        ex('この 景色は まるで 絵みたいですね。', 'この けしきは まるで えみたいですね。', 'Ce paysage, on croirait un tableau.', 'This view is just like a painting.'),
      ], [
        FB(CHOOSE, '彼は 具合が 悪い＿です。顔が 青いです。', ['よう', 'のよう', 'なよう'], 'よう', ('Adjectif en い + ようだ, sans rien ajouter.', 'い-adjective + ようだ, with nothing added.'), ('Il a l’air de ne pas aller bien. Il est tout pâle.', 'He seems unwell. His face is pale.')),
        FB(CHOOSE, 'あの 人は 学生＿ ようです。', ['の', 'な', 'だ'], 'の', ('Nom + の + ようだ.', 'Noun + の + ようだ.'), ('Cette personne semble être étudiante.', 'That person seems to be a student.')),
        FB(CHOOSE, '彼女は 人形の＿ 顔を して います。', ['ような', 'ように', 'ようだ'], 'ような', ('Devant un nom : 〜ような.', 'Before a noun: 〜ような.'), ('Elle a un visage de poupée.', 'She has a face like a doll’s.')),
        TF('どうやら 道を 間違えたみたいだ。', ('La personne est certaine de s’être trompée de chemin.', 'The speaker is certain they took the wrong road.'), FAUX, ('〜みたいだ exprime une impression, pas une certitude.', '〜みたいだ expresses an impression, not a certainty.')),
      ]),
    L('n3-rashii', ('Il paraît que… : 〜らしい', 'Apparently…: 〜らしい'), ('Rapporter une information indirecte et dire ce qui est typique.', 'Report indirect information and say what is typical.'), 10, [
        ('〜らしい suit la forme neutre (sans だ après un nom) : 引っ越すらしい, 病気らしい. On s’appuie sur ce qu’on a entendu ou lu.', '〜らしい follows the plain form (no だ after a noun): 引っ越すらしい, 病気らしい. It relies on what you have heard or read.'),
        ('Différence : 〜ようだ = ma propre impression ; 〜らしい = une information venue d’ailleurs ; 〜そうだ (ouï-dire) = je répète ce qu’on m’a dit.', 'Difference: 〜ようだ = my own impression; 〜らしい = information from elsewhere; 〜そうだ (hearsay) = I repeat what I was told.'),
        ('Nom + らしい peut aussi vouloir dire « digne de, typique de » : 春らしい 天気, 子どもらしい.', 'Noun + らしい can also mean “typical of, worthy of”: 春らしい 天気, 子どもらしい.'),
      ], [
        G('gram-n3-rashii', '〜らしい', '〜らしい', '~rashii', ('il paraît que… ; typique de…', 'apparently… ; typical of…')),
        V('vocab-hikkoshimasu', '引っ越します', 'ひっこします', 'hikkoshimasu', ('déménager', 'to move house')),
        V('vocab-saikin', '最近', 'さいきん', 'saikin', ('récemment, ces derniers temps', 'recently, lately')),
        V('vocab-ninki', '人気', 'にんき', 'ninki', ('popularité, succès', 'popularity')),
        V('vocab-haru', '春', 'はる', 'haru', ('printemps', 'spring (season)')),
        K('kanji-mottomo', '最', 'もっとも', 'mottomo', ('le plus, extrême', 'most, utmost'), ['サイ'], ['もっと(も)'], 12),
        K('kanji-kosu', '越', 'こす', 'kosu', ('franchir, dépasser', 'cross over, exceed'), ['エツ'], ['こ(す)', 'こ(える)'], 12),
      ], [
        ex('山田さんは 来月 大阪へ 引っ越すらしいです。', 'やまださんは らいげつ おおさかへ ひっこすらしいです。', 'Il paraît que M. Yamada déménage à Osaka le mois prochain.', 'Apparently Mr Yamada is moving to Osaka next month.'),
        ex('今日は 春らしい 暖かい 日ですね。', 'きょうは はるらしい あたたかい ひですね。', 'Aujourd’hui, il fait doux : une vraie journée de printemps.', 'Today is a warm, truly spring-like day.'),
      ], [
        FB(CHOOSE, 'あの 店の ラーメンは おいしい＿。いつも 人が 並んで います。', ['らしい', 'だらしい', 'のらしい'], 'らしい', ('Adjectif en い + らしい.', 'い-adjective + らしい.'), ('Il paraît que les ramen de ce restaurant sont bons. Il y a toujours la queue.', 'Apparently that shop’s ramen is good. There is always a queue.')),
        FB(CHOOSE, '最近、あの 歌手は とても 人気＿ らしい。', ['が ある', 'だ', 'な'], 'が ある', ('人気が ある + らしい (pas de だ devant らしい).', '人気が ある + らしい (no だ before らしい).'), ('Il paraît que ce chanteur est très populaire en ce moment.', 'Apparently that singer is very popular these days.')),
        FB(COMPLETE, '泣かないで。あなた＿ないよ。', ['らしく', 'らしい', 'みたいに'], 'らしく', ('〜らしくない = cela ne te ressemble pas.', '〜らしくない = that is not like you.'), ('Ne pleure pas. Ça ne te ressemble pas.', 'Don’t cry. It’s not like you.')),
        TF('新しい 先生は 厳しいらしい。', ('La personne a elle-même constaté que le professeur est sévère.', 'The speaker has personally found the teacher to be strict.'), FAUX, ('〜らしい : information indirecte, entendue de quelqu’un d’autre.', '〜らしい: indirect information, heard from someone else.')),
      ]),
    L('n3-hazu', ('Normalement… : 〜はずだ', 'It should be…: 〜はずだ'), ('Exprimer une attente logique, et dire qu’une chose est impossible.', 'Express a logical expectation, and say that something cannot be.'), 10, [
        ('〜はずだ = cela devrait être le cas, d’après ce que je sais : 荷物は 明日 届くはずです.', '〜はずだ = it should be so, from what I know: 荷物は 明日 届くはずです.'),
        ('Forme neutre + はず ; nom + の + はず ; adjectif en な + な + はず : 休みのはず, 元気なはず.', 'Plain form + はず; noun + の + はず; な-adjective + な + はず: 休みのはず, 元気なはず.'),
        ('〜はずがない = c’est impossible, il n’y a aucune raison que… : 彼が そんな ことを 言うはずがない.', '〜はずがない = it cannot be, there is no way that…: 彼が そんな ことを 言うはずがない.'),
      ], [
        G('gram-n3-hazu', '〜はずだ', '〜はずだ', '~hazu da', ('normalement…, cela devrait…', 'it should…, it is expected that…')),
        G('gram-n3-hazu-ga-nai', '〜はずがない', '〜はずがない', '~hazu ga nai', ('il est impossible que…', 'there is no way that…')),
        V('vocab-yotei', '予定', 'よてい', 'yotei', ('programme, projet prévu', 'schedule, plan')),
        V('vocab-tashika', '確か', 'たしか', 'tashika', ('sûr, certain ; si je ne me trompe pas', 'sure, certain; if I remember rightly')),
        V('vocab-todokimasu', '届きます', 'とどきます', 'todokimasu', ('arriver, être livré', 'to arrive, to be delivered')),
        V('vocab-nimotsu', '荷物', 'にもつ', 'nimotsu', ('bagage, colis', 'luggage, parcel')),
        K('kanji-tashika', '確', 'たしか', 'tashika', ('certain, vérifier', 'certain, confirm'), ['カク'], ['たし(か)', 'たし(かめる)'], 15),
        K('kanji-sadameru', '定', 'さだめる', 'sadameru', ('fixer, déterminer', 'fix, determine'), ['テイ', 'ジョウ'], ['さだ(める)'], 8),
      ], [
        ex('昨日 送ったから、荷物は 今日 届くはずです。', 'きのう おくったから、にもつは きょう とどくはずです。', 'Je l’ai envoyé hier, le colis devrait donc arriver aujourd’hui.', 'I sent it yesterday, so the parcel should arrive today.'),
        ex('まじめな 彼が うそを つくはずがない。', 'まじめな かれが うそを つくはずがない。', 'Lui qui est si sérieux, il est impossible qu’il mente.', 'He is so serious; there is no way he would lie.'),
      ], [
        FB(CHOOSE, '今日は 日曜日だから、銀行は 休み＿ はずです。', ['の', 'な', 'だ'], 'の', ('Nom + の + はず.', 'Noun + の + はず.'), ('Comme c’est dimanche, la banque devrait être fermée.', 'It is Sunday, so the bank should be closed.')),
        FB(COMPLETE, '会議は 三時に 終わる 予定だから、もう 終わった＿です。', ['はず', 'らしい', 'みたい'], 'はず', ('Déduction logique à partir d’un fait connu : 〜はずだ.', 'Logical deduction from a known fact: 〜はずだ.'), ('La réunion devait finir à 15 h, elle devrait donc être terminée.', 'The meeting was due to end at three, so it should be over by now.')),
        FB(COMPLETE, 'こんなに 簡単な 問題を 間違える＿。', ['はずがない', 'はずだ', 'ようだ'], 'はずがない', ('Impossibilité : 〜はずがない.', 'Impossibility: 〜はずがない.'), ('Il est impossible de se tromper sur une question aussi simple.', 'There is no way anyone would get such an easy question wrong.')),
        SO(('Remets dans l’ordre : « Il devrait venir, c’est sûr. »', 'Put in order: “He should be coming, for sure.”'), ['彼は', '確かに', '来る', 'はずです。'], ('Sujet + adverbe + verbe neutre + はずです.', 'Subject + adverb + plain verb + はずです.')),
      ]),
  ])])

# ═════════════════════════ Île 2 : changements et décisions ═════════════════════════
W2 = WORLD('n3-w2', ('Changements et décisions', 'Changes and decisions'), REGION,
  ('Dire ce qui a changé, ce qu’on s’efforce de faire et ce qui a été décidé.', 'Say what has changed, what you make an effort to do, and what has been decided.'),
  (('Le Tengu des Résolutions', 'The Tengu of Resolutions'), '決', ('Du haut de sa montagne, le Tengu exige des décisions nettes. Hésite, et il t’emporte dans le vent !', 'From his mountaintop, the Tengu demands firm decisions. Hesitate, and he sweeps you away on the wind!')),
  [CH('n3-w2-c1', ('Devenir, s’efforcer, décider', 'Becoming, making an effort, deciding'), [
    L('n3-you-ni-naru', ('Un changement : 〜ようになる', 'A change: 〜ようになる'), ('Dire qu’on est devenu capable de faire quelque chose, ou qu’une habitude a changé.', 'Say that you have become able to do something, or that a habit has changed.'), 9, [
        ('Verbe (dictionnaire ou potentiel) + ようになる = en venir à, finir par pouvoir : 漢字が 読めるようになりました.', 'Verb (dictionary or potential) + ようになる = come to, become able to: 漢字が 読めるようになりました.'),
        ('Le changement est progressif : avant je ne pouvais pas, maintenant je peux.', 'The change is gradual: before I could not, now I can.'),
        ('Dans l’autre sens : 〜なくなる = ne plus… : テレビを 見なくなりました.', 'In the other direction: 〜なくなる = no longer…: テレビを 見なくなりました.'),
      ], [
        G('gram-n3-you-ni-naru', '〜ようになる', '〜ようになる', '~you ni naru', ('en venir à…, devenir capable de…', 'come to…, become able to…')),
        G('gram-n3-naku-naru', '〜なくなる', '〜なくなる', '~naku naru', ('ne plus… (changement)', 'no longer… (change)')),
        V('vocab-naremasu', '慣れます', 'なれます', 'naremasu', ('s’habituer', 'to get used to')),
        V('vocab-saisho', '最初', 'さいしょ', 'saisho', ('le début, d’abord', 'the beginning, at first')),
        V('vocab-seikatsu', '生活', 'せいかつ', 'seikatsu', ('vie quotidienne', 'daily life')),
        K('kanji-nareru', '慣', 'なれる', 'nareru', ('s’habituer, coutume', 'get used to, custom'), ['カン'], ['な(れる)'], 14),
        K('kanji-hajime', '初', 'はじめ', 'hajime', ('premier, début', 'first, beginning'), ['ショ'], ['はじ(め)', 'はつ'], 7),
      ], [
        ex('最初は 大変でしたが、日本の 生活に 慣れて、一人で 買い物が できるようになりました。', 'さいしょは たいへんでしたが、にほんの せいかつに なれて、ひとりで かいものが できるようになりました。', 'Au début c’était dur, mais je me suis habitué à la vie au Japon et j’arrive maintenant à faire mes courses seul.', 'It was hard at first, but I got used to life in Japan and can now do my shopping on my own.'),
        ex('子どもが 生まれてから、あまり 映画を 見なくなりました。', 'こどもが うまれてから、あまり えいがを みなくなりました。', 'Depuis la naissance de mon enfant, je ne regarde presque plus de films.', 'Since my child was born, I hardly watch films any more.'),
      ], [
        FB(CHOOSE, '毎日 練習して、やっと 泳げる＿ なりました。', ['ように', 'ような', 'ことに'], 'ように', ('Potentiel + ようになる = devenir capable de.', 'Potential + ようになる = become able to.'), ('À force de m’entraîner tous les jours, j’ai enfin appris à nager.', 'By practising every day, I have finally become able to swim.')),
        FB(CHOOSE, '大人に なって、野菜を 食べる＿。', ['ようになりました', 'ことがあります', 'ほうがいいです'], 'ようになりました', ('Nouvelle habitude : 〜ようになりました.', 'New habit: 〜ようになりました.'), ('En devenant adulte, je me suis mis à manger des légumes.', 'As an adult, I have started eating vegetables.')),
        FB(CHOOSE, 'スマホを 買ってから、手紙を 書か＿ なりました。', ['なく', 'ないで', 'なくて'], 'なく', ('Ne plus faire : 〜なくなる.', 'No longer doing: 〜なくなる.'), ('Depuis que j’ai un smartphone, je n’écris plus de lettres.', 'Since buying a smartphone, I no longer write letters.')),
        TF('日本語の ニュースが 分かるようになりました。', ('Avant, la personne ne comprenait pas les informations en japonais.', 'Before, the speaker could not understand the news in Japanese.'), VRAI, ('〜ようになる marque un changement : avant non, maintenant oui.', '〜ようになる marks a change: not before, but now yes.')),
      ]),
    L('n3-you-ni-suru', ('S’efforcer, décider : 〜ようにする・〜ことにする', 'Making an effort, deciding: 〜ようにする・〜ことにする'), ('Dire ce qu’on s’efforce de faire, et ce qu’on a décidé soi-même.', 'Say what you make an effort to do, and what you have decided yourself.'), 10, [
        ('〜ようにする = faire en sorte de, s’efforcer de : 毎日 野菜を 食べるようにして います.', '〜ようにする = make sure to, try to: 毎日 野菜を 食べるようにして います.'),
        ('〜ことにする = décider de (par soi-même) : 来月から ジムに 通うことにしました.', '〜ことにする = decide to (by oneself): 来月から ジムに 通うことにしました.'),
        ('〜ことにしている = règle personnelle que l’on suit : 夜は コーヒーを 飲まないことにして います.', '〜ことにしている = a personal rule you follow: 夜は コーヒーを 飲まないことにして います.'),
      ], [
        G('gram-n3-you-ni-suru', '〜ようにする', '〜ようにする', '~you ni suru', ('faire en sorte de…, s’efforcer de…', 'make sure to…, try to…')),
        G('gram-n3-koto-ni-suru', '〜ことにする', '〜ことにする', '~koto ni suru', ('décider de…', 'decide to…')),
        V('vocab-kimemasu', '決めます', 'きめます', 'kimemasu', ('décider, fixer', 'to decide')),
        V('vocab-kenkou', '健康', 'けんこう', 'kenkou', ('santé', 'health')),
        V('vocab-kayoimasu', '通います', 'かよいます', 'kayoimasu', ('fréquenter, aller régulièrement à', 'to attend, to go regularly to')),
        K('kanji-kimeru', '決', 'きめる', 'kimeru', ('décider', 'decide'), ['ケツ'], ['き(める)', 'き(まる)'], 7),
        K('kanji-sukoyaka', '健', 'すこやか', 'sukoyaka', ('sain, robuste', 'healthy, robust'), ['ケン'], ['すこ(やか)'], 11),
      ], [
        ex('健康の ために、できるだけ 歩くように して います。', 'けんこうの ために、できるだけ あるくように して います。', 'Pour ma santé, je m’efforce de marcher autant que possible.', 'For my health, I try to walk as much as possible.'),
        ex('よく 考えて、会社を 辞めることに しました。', 'よく かんがえて、かいしゃを やめることに しました。', 'Après mûre réflexion, j’ai décidé de quitter mon entreprise.', 'After thinking it over carefully, I decided to leave my company.'),
      ], [
        FB(CHOOSE, '約束の 時間に 遅れない＿ して ください。', ['ように', 'ことに', 'みたいに'], 'ように', ('Faire en sorte de ne pas… : 〜ないようにする.', 'Make sure not to…: 〜ないようにする.'), ('Veillez à ne pas être en retard au rendez-vous.', 'Please make sure you are not late for the appointment.')),
        FB(CHOOSE, '今年の 夏は 北海道へ 行く＿ しました。', ['ことに', 'ように', 'はずに'], 'ことに', ('Décision personnelle : 〜ことにしました.', 'Personal decision: 〜ことにしました.'), ('Cet été, j’ai décidé d’aller à Hokkaidō.', 'This summer, I have decided to go to Hokkaidō.')),
        DC(('Un ami te propose un café à 22 h. Tu as une règle personnelle.', 'A friend offers you coffee at 10 p.m. You have a personal rule.'), [('友だち', 'コーヒー、飲む？')], ('Ton ami te propose un café.', 'Your friend offers you a coffee.'), ['夜は 飲まないことに して いるんだ。', '夜は 飲めるように なったんだ。', '夜は 飲むはずなんだ。'], '夜は 飲まないことに して いるんだ。', ('〜ことにしている = règle que l’on s’est fixée.', '〜ことにしている = a rule you have set yourself.')),
        SO(('Remets dans l’ordre : « Je m’efforce de me lever tôt. »', 'Put in order: “I try to get up early.”'), ['早く', '起きる', 'ように', 'して います。'], ('Verbe + ように + しています.', 'Verb + ように + しています.')),
      ]),
    L('n3-koto-ni-naru', ('C’est décidé : 〜ことになる', 'It has been decided: 〜ことになる'), ('Annoncer une décision prise par d’autres ou par les circonstances.', 'Announce a decision made by others or by circumstances.'), 9, [
        ('〜ことになる = il a été décidé que… (pas par moi) : 来月 大阪に 転勤することに なりました.', '〜ことになる = it has been decided that… (not by me): 来月 大阪に 転勤することに なりました.'),
        ('C’est aussi une façon modeste d’annoncer sa propre décision : 結婚することに なりました.', 'It is also a modest way to announce your own decision: 結婚することに なりました.'),
        ('〜ことになっている = c’est la règle, c’est prévu ainsi : ここでは 靴を 脱ぐことに なって います.', '〜ことになっている = that is the rule, that is how it is arranged: ここでは 靴を 脱ぐことに なって います.'),
      ], [
        G('gram-n3-koto-ni-naru', '〜ことになる', '〜ことになる', '~koto ni naru', ('il a été décidé que…', 'it has been decided that…')),
        G('gram-n3-koto-ni-natte-iru', '〜ことになっている', '〜ことになっている', '~koto ni natte iru', ('il est de règle que…, il est prévu que…', 'the rule is that…, it is arranged that…')),
        V('vocab-tenkin', '転勤', 'てんきん', 'tenkin', ('mutation (professionnelle)', 'job transfer')),
        V('vocab-shucchou', '出張', 'しゅっちょう', 'shucchou', ('déplacement professionnel', 'business trip')),
        V('vocab-kisoku', '規則', 'きそく', 'kisoku', ('règlement, règle', 'rule, regulation')),
        K('kanji-tsutomeru', '勤', 'つとめる', 'tsutomeru', ('être employé, servir', 'be employed, serve'), ['キン'], ['つと(める)'], 12),
        K('kanji-haru', '張', 'はる', 'haru', ('tendre, étirer', 'stretch, spread'), ['チョウ'], ['は(る)'], 11),
      ], [
        ex('来週、部長と 東京へ 出張することに なりました。', 'らいしゅう、ぶちょうと とうきょうへ しゅっちょうすることに なりました。', 'Il a été décidé que j’irai en déplacement à Tokyo la semaine prochaine avec mon chef.', 'It has been decided that I will go on a business trip to Tokyo next week with my manager.'),
        ex('この 寮では、十時までに 帰ることに なって います。', 'この りょうでは、じゅうじまでに かえることに なって います。', 'Dans cette résidence, la règle est de rentrer avant 22 h.', 'In this dormitory, the rule is to be back by ten o’clock.'),
      ], [
        FB(CHOOSE, '四月から 大阪に 転勤する＿ なりました。', ['ことに', 'ように', 'みたいに'], 'ことに', ('Décision de l’entreprise : 〜ことになりました.', 'The company’s decision: 〜ことになりました.'), ('Il a été décidé que je serai muté à Osaka à partir d’avril.', 'It has been decided that I will be transferred to Osaka from April.')),
        FB(CHOOSE, '規則で、教室では 日本語だけで 話す＿。', ['ことになっています', 'ことにしました', 'ようになりました'], 'ことになっています', ('Règle établie : 〜ことになっている.', 'Established rule: 〜ことになっている.'), ('Le règlement veut qu’on ne parle que japonais en classe.', 'By the rules, only Japanese is spoken in the classroom.')),
        TF('自分で 決めて、留学することに しました。', ('C’est la personne elle-même qui a pris la décision.', 'The speaker made the decision themselves.'), VRAI, ('〜ことにする = ma décision ; 〜ことになる = décision extérieure.', '〜ことにする = my decision; 〜ことになる = an outside decision.')),
        TF('来月、結婚することに なりました。', ('Cette phrase est une façon polie et modeste d’annoncer son mariage.', 'This sentence is a polite, modest way of announcing one’s marriage.'), VRAI, ('〜ことになりました présente la décision comme un fait, sans se mettre en avant.', '〜ことになりました presents the decision as a fact, without putting oneself forward.')),
      ]),
  ])])

# ═════════════════════════ Île 3 : contrastes et concessions ═════════════════════════
W3 = WORLD('n3-w3', ('Contrastes et concessions', 'Contrasts and concessions'), REGION,
  ('Exprimer la déception, la concession et l’excès.', 'Express disappointment, concession and excess.'),
  (('La Yuki-onna des Regrets', 'The Yuki-onna of Regrets'), '雪', ('La dame des neiges souffle ses « et pourtant… » glacés. Réponds juste avant que tes phrases ne gèlent !', 'The snow woman breathes her icy “and yet…”. Answer correctly before your sentences freeze!')),
  [CH('n3-w3-c1', ('Pourtant, même si, rien que', 'And yet, even if, nothing but'), [
    L('n3-noni', ('Et pourtant… : 〜のに', 'And yet…: 〜のに'), ('Exprimer un résultat contraire à ce qu’on attendait, avec regret ou surprise.', 'Express a result contrary to expectation, with regret or surprise.'), 9, [
        ('〜のに relie deux faits qui s’opposent, avec un sentiment de déception ou d’étonnement : 約束したのに、来ませんでした.', '〜のに links two opposing facts, with a feeling of disappointment or surprise: 約束したのに、来ませんでした.'),
        ('Forme neutre + のに ; nom et adjectif en な + な + のに : 日曜日なのに, 元気なのに.', 'Plain form + のに; noun and な-adjective + な + のに: 日曜日なのに, 元気なのに.'),
        ('Contrairement à 〜が ou 〜けど, 〜のに porte toujours une émotion. En fin de phrase : 言って くれれば よかったのに (dommage…).', 'Unlike 〜が or 〜けど, 〜のに always carries emotion. At the end of a sentence: 言って くれれば よかったのに (what a pity…).'),
      ], [
        G('gram-n3-noni', '〜のに', '〜のに', '~noni', ('alors que…, et pourtant…', 'even though…, and yet…')),
        V('vocab-yakusoku', '約束', 'やくそく', 'yakusoku', ('promesse, rendez-vous', 'promise, appointment')),
        V('vocab-gakkari', 'がっかりします', 'がっかりします', 'gakkari shimasu', ('être déçu', 'to be disappointed')),
        V('vocab-sekkaku', 'せっかく', 'せっかく', 'sekkaku', ('exprès, avec tant de peine', 'specially, with great effort')),
        V('vocab-isshoukenmei', '一生懸命', 'いっしょうけんめい', 'isshoukenmei', ('de toutes ses forces', 'with all one’s might')),
        K('kanji-taba', '束', 'たば', 'taba', ('botte, lier', 'bundle, bind'), ['ソク'], ['たば'], 7),
        K('kanji-nokoru', '残', 'のこる', 'nokoru', ('rester, laisser', 'remain, leave behind'), ['ザン'], ['のこ(る)', 'のこ(す)'], 10),
      ], [
        ex('一生懸命 勉強したのに、試験に 落ちて しまいました。', 'いっしょうけんめい べんきょうしたのに、しけんに おちて しまいました。', 'J’ai pourtant travaillé de toutes mes forces, et j’ai raté l’examen.', 'I studied as hard as I could, and yet I failed the exam.'),
        ex('せっかく 料理を 作ったのに、だれも 食べて くれません。', 'せっかく りょうりを つくったのに、だれも たべて くれません。', 'J’ai cuisiné exprès, et pourtant personne ne mange.', 'I went to the trouble of cooking, and yet nobody will eat.'),
      ], [
        FB(CHOOSE, '今日は 日曜日＿ のに、会社へ 行かなければ なりません。', ['な', 'だ', 'の'], 'な', ('Nom + な + のに.', 'Noun + な + のに.'), ('C’est dimanche, et pourtant je dois aller au bureau.', 'It is Sunday, and yet I have to go to the office.')),
        FB(COMPLETE, '薬を 飲んだ＿、熱が 下がりません。', ['のに', 'ので', 'から'], 'のに', ('Résultat contraire à l’attente : 〜のに.', 'Result contrary to expectation: 〜のに.'), ('J’ai pris le médicament, et pourtant la fièvre ne baisse pas.', 'I took the medicine, and yet my fever won’t go down.')),
        DC(('Ton ami n’est pas venu au rendez-vous. Tu exprimes ta déception.', 'Your friend did not turn up. You express your disappointment.'), [('友だち', 'ごめん、忘れて いた。')], ('Ton ami s’excuse : il avait oublié.', 'Your friend apologises: he had forgotten.'), ['約束したのに……。', '約束したはずだ。', '約束することにした。'], '約束したのに……。', ('〜のに en fin de phrase exprime le regret.', '〜のに at the end of a sentence expresses regret.')),
        TF('雨が 降って いるのに、彼は 傘を 持って いません。', ('La personne trouve cela surprenant.', 'The speaker finds this surprising.'), VRAI, ('〜のに marque l’étonnement devant un fait inattendu.', '〜のに marks surprise at an unexpected fact.')),
      ]),
    L('n3-temo', ('Même si… : 〜ても', 'Even if…: 〜ても'), ('Dire qu’un résultat ne change pas, quelle que soit la condition.', 'Say that a result does not change, whatever the condition.'), 9, [
        ('Forme en て + も = même si : 雨が 降っても、行きます. Adjectif en い : 〜くても ; nom et adjectif en な : 〜でも.', 'て-form + も = even if: 雨が 降っても、行きます. い-adjective: 〜くても; noun and な-adjective: 〜でも.'),
        ('Avec un mot interrogatif = peu importe : いくら 考えても 分かりません, どんなに 忙しくても.', 'With a question word = no matter: いくら 考えても 分かりません, どんなに 忙しくても.'),
        ('Souvent renforcé par たとえ : たとえ 反対されても、あきらめません.', 'Often reinforced by たとえ: たとえ 反対されても、あきらめません.'),
      ], [
        G('gram-n3-temo', '〜ても', '〜ても', '~temo', ('même si…, bien que…', 'even if…, even though…')),
        G('gram-n3-ikura-temo', 'いくら〜ても', 'いくら〜ても', 'ikura ~temo', ('on a beau…, peu importe combien…', 'no matter how much…')),
        V('vocab-hantai', '反対', 'はんたい', 'hantai', ('opposition, contraire', 'opposition, opposite')),
        V('vocab-akiramemasu', 'あきらめます', 'あきらめます', 'akiramemasu', ('renoncer, abandonner', 'to give up')),
        V('vocab-shippai', '失敗', 'しっぱい', 'shippai', ('échec, erreur', 'failure, mistake')),
        V('vocab-tatoe', 'たとえ', 'たとえ', 'tatoe', ('même si, quand bien même', 'even supposing')),
        K('kanji-soru', '反', 'そる', 'soru', ('anti-, se cambrer', 'anti-, bend back'), ['ハン'], ['そ(る)', 'そ(らす)'], 4),
        K('kanji-yabureru', '敗', 'やぶれる', 'yabureru', ('être vaincu, échec', 'be defeated, failure'), ['ハイ'], ['やぶ(れる)'], 11),
      ], [
        ex('たとえ 両親に 反対されても、留学するつもりです。', 'たとえ りょうしんに はんたいされても、りゅうがくするつもりです。', 'Même si mes parents s’y opposent, j’ai l’intention de partir étudier à l’étranger.', 'Even if my parents object, I intend to study abroad.'),
        ex('何度 失敗しても、あきらめないで ください。', 'なんど しっぱいしても、あきらめないで ください。', 'Même si vous échouez plusieurs fois, ne renoncez pas.', 'However many times you fail, please don’t give up.'),
      ], [
        FB(CHOOSE, 'いくら 高＿、この 本は 買いたいです。', ['くても', 'いても', 'でも'], 'くても', ('Adjectif en い : 高い → 高くても.', 'い-adjective: 高い → 高くても.'), ('Peu importe son prix, je veux acheter ce livre.', 'However expensive it is, I want to buy this book.')),
        FB(CHOOSE, '日曜日＿、彼は 仕事を して います。', ['でも', 'ても', 'くても'], 'でも', ('Nom + でも.', 'Noun + でも.'), ('Même le dimanche, il travaille.', 'Even on Sundays, he works.')),
        FB(CHOOSE, 'どんなに 眠＿、宿題は 終わらせます。', ['くても', 'っても', 'でも'], 'くても', ('眠い → 眠くても.', '眠い → 眠くても.'), ('J’ai beau avoir sommeil, je finirai mes devoirs.', 'However sleepy I am, I will finish my homework.')),
        SO(('Remets dans l’ordre : « J’ai beau chercher, je ne trouve pas. »', 'Put in order: “However much I look, I can’t find it.”'), ['いくら', '探しても', '見つかりません。'], ('いくら + verbe en ても + résultat inchangé.', 'いくら + verb in ても + unchanged result.')),
      ]),
    L('n3-bakari', ('Rien que… : 〜ばかり', 'Nothing but…: 〜ばかり'), ('Critiquer un excès : ne faire que, n’avoir que.', 'Criticise an excess: doing nothing but, having nothing but.'), 9, [
        ('Nom + ばかり = rien que, uniquement (trop) : 甘い ものばかり 食べて います.', 'Noun + ばかり = nothing but, only (too much): 甘い ものばかり 食べて います.'),
        ('Verbe en て + ばかりいる = ne faire que… : 弟は ゲームを してばかり います.', 'Verb in て-form + ばかりいる = do nothing but…: 弟は ゲームを してばかり います.'),
        ('Le ton est critique. À ne pas confondre avec 〜たばかり (venir de faire), qui se construit sur la forme en た.', 'The tone is critical. Do not confuse with 〜たばかり (have just done), which is built on the た-form.'),
      ], [
        G('gram-n3-bakari', '〜ばかり', '〜ばかり', '~bakari', ('rien que…, ne faire que…', 'nothing but…, do nothing but…')),
        V('vocab-monku', '文句', 'もんく', 'monku', ('plainte, reproche', 'complaint')),
        V('vocab-amai', '甘い', 'あまい', 'amai', ('sucré ; indulgent', 'sweet; lenient')),
        V('vocab-manga', '漫画', 'まんが', 'manga', ('manga, bande dessinée', 'manga, comics')),
        K('kanji-amai', '甘', 'あまい', 'amai', ('doux, sucré', 'sweet'), ['カン'], ['あま(い)', 'あま(える)'], 5),
        K('kanji-asobu', '遊', 'あそぶ', 'asobu', ('jouer, s’amuser', 'play, enjoy oneself'), ['ユウ'], ['あそ(ぶ)'], 12),
      ], [
        ex('兄は 休みの 日、寝てばかり います。', 'あには やすみの ひ、ねてばかり います。', 'Les jours de congé, mon grand frère ne fait que dormir.', 'On his days off, my older brother does nothing but sleep.'),
        ex('文句ばかり 言わないで、手伝って ください。', 'もんくばかり いわないで、てつだって ください。', 'Arrête de te plaindre sans cesse et aide-moi.', 'Stop complaining all the time and help me.'),
      ], [
        FB(CHOOSE, '妹は 漫画＿ 読んで いて、勉強しません。', ['ばかり', 'しか', 'だけで'], 'ばかり', ('Nom + ばかり = rien que (reproche).', 'Noun + ばかり = nothing but (reproach).'), ('Ma petite sœur ne lit que des mangas et n’étudie pas.', 'My little sister reads nothing but manga and doesn’t study.')),
        FB(CHOOSE, '遊んで＿ いないで、宿題を しなさい。', ['ばかり', 'ほど', 'まで'], 'ばかり', ('Verbe en て + ばかりいる.', 'Verb in て-form + ばかりいる.'), ('Arrête de ne faire que jouer et fais tes devoirs.', 'Stop just playing around and do your homework.')),
        TF('この 子は 甘い ものばかり 食べて います。', ('La personne trouve que l’enfant mange trop de sucreries.', 'The speaker thinks the child eats too many sweets.'), VRAI, ('〜ばかり porte un jugement : c’est excessif.', '〜ばかり carries a judgement: it is excessive.')),
        SO(('Remets dans l’ordre : « Il ne fait que regarder la télé. »', 'Put in order: “He does nothing but watch TV.”'), ['彼は', 'テレビを', '見て', 'ばかり', 'います。'], ('Objet + verbe en て + ばかり + います.', 'Object + verb in て-form + ばかり + います.')),
      ]),
  ])])

# ═════════════════════════ Île 4 : le moment juste ═════════════════════════
W4 = WORLD('n3-w4', ('Le moment juste', 'The right moment'), REGION,
  ('Situer une action : sur le point de, en train de, venir de, pendant que.', 'Place an action in time: about to, in the middle of, have just, while.'),
  (('Le Tanuki des Horloges', 'The Tanuki of Clocks'), '刻', ('Ce tanuki dérègle toutes les horloges. Dis-lui précisément où en est l’action, sinon il remonte le temps !', 'This tanuki sets every clock wrong. Tell him exactly where the action stands, or he will turn back time!')),
  [CH('n3-w4-c1', ('Sur le point de, à l’instant, pendant', 'About to, just now, while'), [
    L('n3-tokoro', ('Où en est l’action : 〜ところだ', 'Where the action stands: 〜ところだ'), ('Dire qu’on est sur le point de faire, en train de faire, ou qu’on vient de faire.', 'Say that you are about to do, in the middle of doing, or have just done something.'), 10, [
        ('Dictionnaire + ところ = sur le point de : 今から 出かけるところです.', 'Dictionary form + ところ = about to: 今から 出かけるところです.'),
        ('〜ている + ところ = en plein dans l’action : 今 準備して いるところです.', '〜ている + ところ = right in the middle of it: 今 準備して いるところです.'),
        ('Forme en た + ところ = venir tout juste de : ちょうど 今 着いたところです.', 'た-form + ところ = have only just: ちょうど 今 着いたところです.'),
      ], [
        G('gram-n3-ru-tokoro', '〜るところだ', '〜るところだ', '~ru tokoro da', ('être sur le point de…', 'be about to…')),
        G('gram-n3-teiru-tokoro', '〜ているところだ', '〜ているところだ', '~te iru tokoro da', ('être en train de… (à l’instant)', 'be in the middle of… (right now)')),
        G('gram-n3-ta-tokoro', '〜たところだ', '〜たところだ', '~ta tokoro da', ('venir tout juste de…', 'have only just…')),
        V('vocab-choudo', 'ちょうど', 'ちょうど', 'choudo', ('juste, exactement', 'just, exactly')),
        V('vocab-junbi', '準備', 'じゅんび', 'junbi', ('préparatifs', 'preparation')),
        V('vocab-shuppatsu', '出発', 'しゅっぱつ', 'shuppatsu', ('départ', 'departure')),
        K('kanji-sonaeru', '備', 'そなえる', 'sonaeru', ('préparer, équiper', 'prepare, equip'), ['ビ'], ['そな(える)', 'そな(わる)'], 12),
      ], [
        ex('今 駅に 着いたところです。すぐ そちらへ 行きます。', 'いま えきに ついたところです。すぐ そちらへ いきます。', 'Je viens d’arriver à la gare. J’arrive tout de suite.', 'I have just arrived at the station. I’ll be right there.'),
        ex('ちょうど 今から 出発するところです。', 'ちょうど いまから しゅっぱつするところです。', 'Nous sommes justement sur le point de partir.', 'We are just about to leave.'),
      ], [
        FB(CHOOSE, '「晩ごはんは？」「今 作って ＿ ところです。」', ['いる', 'いた', 'ある'], 'いる', ('En cours : 〜ているところ.', 'In progress: 〜ているところ.'), ('« Et le dîner ? » « Je suis en train de le préparer. »', '“What about dinner?” “I’m in the middle of making it.”')),
        FB(CHOOSE, '「もう 食べましたか。」「いいえ、これから 食べ＿ ところです。」', ['る', 'た', 'て'], 'る', ('Sur le point de : dictionnaire + ところ.', 'About to: dictionary form + ところ.'), ('« Tu as déjà mangé ? » « Non, je m’apprête à manger. »', '“Have you eaten yet?” “No, I’m just about to.”')),
        FB(CHOOSE, 'たった今、会議が 終わっ＿ ところです。', ['た', 'て', 'ている'], 'た', ('Venir de : forme en た + ところ.', 'Have just: た-form + ところ.'), ('La réunion vient tout juste de se terminer.', 'The meeting has only just finished.')),
        DC(('On t’appelle au moment où tu sors de chez toi. Que réponds-tu ?', 'Someone calls just as you are leaving home. What do you answer?'), [('母', '今、どこ？')], ('Ta mère demande où tu es.', 'Your mother asks where you are.'), ['今、家を 出るところだよ。', '今、家を 出てばかりだよ。', '今、家を 出るはずだよ。'], '今、家を 出るところだよ。', ('Sur le point de sortir : 出るところ.', 'About to leave: 出るところ.')),
      ]),
    L('n3-ta-bakari', ('Venir de : 〜たばかり', 'Have just: 〜たばかり'), ('Dire qu’une action est récente, de son point de vue.', 'Say that an action is recent, from your point of view.'), 9, [
        ('Forme en た + ばかり = venir de (c’est récent pour moi) : 日本に 来たばかりです.', 'た-form + ばかり = have just (it feels recent to me): 日本に 来たばかりです.'),
        ('〜たところ = à l’instant même ; 〜たばかり peut couvrir des jours ou des mois : 先月 入社したばかりです.', '〜たところ = this very moment; 〜たばかり can cover days or months: 先月 入社したばかりです.'),
        ('Souvent suivi de なのに ou で : 買ったばかりなのに、もう 壊れました.', 'Often followed by なのに or で: 買ったばかりなのに、もう 壊れました.'),
      ], [
        G('gram-n3-ta-bakari', '〜たばかり', '〜たばかり', '~ta bakari', ('venir de… (récemment)', 'have just… (recently)')),
        V('vocab-nyuusha', '入社', 'にゅうしゃ', 'nyuusha', ('entrée dans une entreprise', 'joining a company')),
        V('vocab-umaremasu', '生まれます', 'うまれます', 'umaremasu', ('naître', 'to be born')),
        V('vocab-sakki', 'さっき', 'さっき', 'sakki', ('tout à l’heure (passé)', 'a little while ago')),
        V('vocab-mada', 'まだ', 'まだ', 'mada', ('encore, pas encore', 'still, not yet')),
        K('kanji-umu', '産', 'うむ', 'umu', ('donner naissance, produire', 'give birth, produce'), ['サン'], ['う(む)', 'う(まれる)'], 11),
      ], [
        ex('先月 入社したばかりなので、まだ 仕事に 慣れて いません。', 'せんげつ にゅうしゃしたばかりなので、まだ しごとに なれて いません。', 'Je viens d’entrer dans l’entreprise le mois dernier, je ne suis pas encore habitué au travail.', 'I only joined the company last month, so I’m not used to the work yet.'),
        ex('さっき 食べたばかりなのに、もう おなかが すきました。', 'さっき たべたばかりなのに、もう おなかが すきました。', 'Je viens pourtant de manger, et j’ai déjà faim.', 'I have only just eaten, and yet I’m already hungry.'),
      ], [
        FB(CHOOSE, 'この パソコンは 先週 買っ＿ ばかりです。', ['た', 'て', 'ている'], 'た', ('Forme en た + ばかり.', 'た-form + ばかり.'), ('J’ai acheté cet ordinateur la semaine dernière seulement.', 'I only bought this computer last week.')),
        FB(COMPLETE, '日本に 来た＿ ころは、何も 分かりませんでした。', ['ばかりの', 'ばかりな', 'ところな'], 'ばかりの', ('Devant un nom : 〜たばかりの.', 'Before a noun: 〜たばかりの.'), ('Quand je venais d’arriver au Japon, je ne comprenais rien.', 'When I had just arrived in Japan, I didn’t understand anything.')),
        TF('弟は ゲームを してばかり います。', ('Ici, ばかり veut dire « venir de ».', 'Here, ばかり means “have just”.'), FAUX, ('Forme en て + ばかりいる = ne faire que. « Venir de » = forme en た + ばかり.', 'て-form + ばかりいる = do nothing but. “Have just” = た-form + ばかり.')),
        TF('赤ちゃんは 生まれたばかりです。', ('Le bébé est né il y a peu de temps.', 'The baby was born a short time ago.'), VRAI, ('〜たばかり = action récente.', '〜たばかり = recent action.')),
      ]),
    L('n3-aida-uchi', ('Pendant que… : 〜あいだに・〜うちに', 'While…: 〜あいだに・〜うちに'), ('Situer une action dans une période, et agir avant qu’il ne soit trop tard.', 'Place an action within a period, and act before it is too late.'), 10, [
        ('〜あいだ = pendant toute la durée ; 〜あいだに = à un moment dans cette durée : 留守の あいだに、荷物が 届きました.', '〜あいだ = throughout the period; 〜あいだに = at some point within it: 留守の あいだに、荷物が 届きました.'),
        ('〜うちに = pendant que c’est encore possible, avant que ça change : 熱い うちに 食べて ください, 若い うちに.', '〜うちに = while it is still possible, before things change: 熱い うちに 食べて ください, 若い うちに.'),
        ('〜ないうちに = avant que… : 忘れない うちに、メモします.', '〜ないうちに = before…: 忘れない うちに、メモします.'),
      ], [
        G('gram-n3-aida-ni', '〜あいだに', '〜あいだに', '~aida ni', ('pendant que… (à un moment)', 'while… (at some point)')),
        G('gram-n3-uchi-ni', '〜うちに', '〜うちに', '~uchi ni', ('tant que…, avant que ça ne change', 'while still…, before it changes')),
        V('vocab-samemasu', '冷めます', 'さめます', 'samemasu', ('refroidir (plat, boisson)', 'to go cold (food, drink)')),
        V('vocab-akachan', '赤ちゃん', 'あかちゃん', 'akachan', ('bébé', 'baby')),
        V('vocab-nemurimasu', '眠ります', 'ねむります', 'nemurimasu', ('s’endormir, être endormi', 'to fall asleep, to be asleep')),
        K('kanji-hieru', '冷', 'ひえる', 'hieru', ('froid, refroidir', 'cold, chill'), ['レイ'], ['つめ(たい)', 'ひ(える)', 'さ(める)'], 7),
        K('kanji-nemuru', '眠', 'ねむる', 'nemuru', ('dormir, sommeil', 'sleep'), ['ミン'], ['ねむ(る)', 'ねむ(い)'], 10),
      ], [
        ex('赤ちゃんが 眠って いる あいだに、掃除を しました。', 'あかちゃんが ねむって いる あいだに、そうじを しました。', 'J’ai fait le ménage pendant que le bébé dormait.', 'I did the cleaning while the baby was asleep.'),
        ex('スープが 冷めない うちに、どうぞ。', 'スープが さめない うちに、どうぞ。', 'Servez-vous avant que la soupe ne refroidisse.', 'Please have some before the soup goes cold.'),
      ], [
        FB(CHOOSE, '若い ＿、いろいろな 国へ 行きたいです。', ['うちに', 'あいだ', 'ところに'], 'うちに', ('Tant que c’est encore possible : 〜うちに.', 'While it is still possible: 〜うちに.'), ('Tant que je suis jeune, je veux visiter toutes sortes de pays.', 'While I’m young, I want to visit all kinds of countries.')),
        FB(CHOOSE, '夏休みの ＿、一度も 雨が 降りませんでした。', ['あいだ', 'あいだに', 'うちに'], 'あいだ', ('Toute la durée : 〜あいだ (sans に).', 'The whole period: 〜あいだ (without に).'), ('Pendant toutes les vacances d’été, il n’a pas plu une seule fois.', 'Throughout the summer holidays, it did not rain once.')),
        FB(CHOOSE, '忘れ＿ うちに、電話番号を 書いて おきます。', ['ない', 'る', 'た'], 'ない', ('Avant que… : 〜ないうちに.', 'Before…: 〜ないうちに.'), ('Je note le numéro de téléphone avant de l’oublier.', 'I’ll write down the phone number before I forget.')),
        SO(('Remets dans l’ordre : « Mangez tant que c’est chaud. »', 'Put in order: “Eat while it’s hot.”'), ['熱い', 'うちに', '食べて', 'ください。'], ('Adjectif + うちに + demande.', 'Adjective + うちに + request.')),
      ]),
  ])])

# ═════════════════════════ Île 5 : raisons et explications ═════════════════════════
W5 = WORLD('n3-w5', ('Raisons et explications', 'Reasons and explanations'), REGION,
  ('Expliquer pourquoi, dire grâce à qui ou à cause de quoi.', 'Explain why, and say thanks to whom or because of what.'),
  (('Le Kappa des Excuses', 'The Kappa of Excuses'), '訳', ('Le kappa a toujours une excuse. Démêle les vraies raisons des fausses avant qu’il ne t’entraîne dans la rivière gelée !', 'The kappa always has an excuse. Sort the real reasons from the false ones before he drags you into the frozen river!')),
  [CH('n3-w5-c1', ('C’est pour ça, grâce à, à cause de', 'That is why, thanks to, because of'), [
    L('n3-wake', ('C’est pour ça : 〜わけだ', 'That is why: 〜わけだ'), ('Tirer une conclusion logique, nuancer, et dire qu’on ne peut pas se permettre.', 'Draw a logical conclusion, add nuance, and say that you cannot afford to.'), 10, [
        ('〜わけだ = voilà pourquoi, c’est donc que… : 十年 住んで いたのですか。日本語が 上手な わけです.', '〜わけだ = no wonder, so that is why…: 十年 住んで いたのですか。日本語が 上手な わけです.'),
        ('〜わけではない = ce n’est pas que…, pas forcément : 嫌いな わけではありません.', '〜わけではない = it is not that…, not necessarily: 嫌いな わけではありません.'),
        ('〜わけにはいかない = je ne peux pas me permettre de (raison morale ou sociale) : 今日は 休む わけにはいきません.', '〜わけにはいかない = I cannot afford to (moral or social reason): 今日は 休む わけにはいきません.'),
      ], [
        G('gram-n3-wake-da', '〜わけだ', '〜わけだ', '~wake da', ('voilà pourquoi…, c’est donc que…', 'no wonder…, so that is why…')),
        G('gram-n3-wake-dewa-nai', '〜わけではない', '〜わけではない', '~wake dewa nai', ('ce n’est pas que…, pas forcément', 'it is not that…, not necessarily')),
        G('gram-n3-wake-niwa-ikanai', '〜わけにはいかない', '〜わけにはいかない', '~wake ni wa ikanai', ('ne pas pouvoir se permettre de…', 'cannot afford to…')),
        V('vocab-setsumei', '説明', 'せつめい', 'setsumei', ('explication', 'explanation')),
        V('vocab-riyuu', '理由', 'りゆう', 'riyuu', ('raison, motif', 'reason')),
        V('vocab-daiji', '大事', 'だいじ', 'daiji', ('important, précieux', 'important, valuable')),
        K('kanji-wake', '訳', 'わけ', 'wake', ('raison ; traduction', 'reason; translation'), ['ヤク'], ['わけ'], 11),
        K('kanji-toku', '説', 'とく', 'toku', ('expliquer, théorie', 'explain, theory'), ['セツ'], ['と(く)'], 14),
      ], [
        ex('なるほど、彼は 日本に 十年も 住んで いたのですか。日本語が 上手な わけですね。', 'なるほど、かれは にほんに じゅうねんも すんで いたのですか。にほんごが じょうずな わけですね。', 'Je vois, il a vécu dix ans au Japon ? Voilà pourquoi il parle si bien japonais.', 'I see, he lived in Japan for ten years? No wonder his Japanese is so good.'),
        ex('大事な 会議が あるので、今日は 休む わけには いきません。', 'だいじな かいぎが あるので、きょうは やすむ わけには いきません。', 'J’ai une réunion importante, je ne peux pas me permettre d’être absent aujourd’hui.', 'I have an important meeting, so I cannot afford to take today off.'),
      ], [
        FB(COMPLETE, '肉を 食べませんが、嫌いな ＿。', ['わけではありません', 'わけです', 'わけにはいきません'], 'わけではありません', ('Nuancer : ce n’est pas que je n’aime pas.', 'Adding nuance: it is not that I dislike it.'), ('Je ne mange pas de viande, mais ce n’est pas que je n’aime pas ça.', 'I don’t eat meat, but it is not that I dislike it.')),
        FB(COMPLETE, '約束したから、行かない ＿。', ['わけにはいきません', 'わけです', 'わけではありません'], 'わけにはいきません', ('Obligation morale : je ne peux pas ne pas y aller.', 'Moral obligation: I cannot not go.'), ('Comme j’ai promis, je ne peux pas me permettre de ne pas y aller.', 'Since I promised, I cannot afford not to go.')),
        FB(COMPLETE, '窓が 開いて いますね。寒い ＿。', ['わけです', 'わけではありません', 'ばかりです'], 'わけです', ('Conclusion logique : voilà pourquoi.', 'Logical conclusion: that is why.'), ('La fenêtre est ouverte. Voilà pourquoi il fait froid.', 'The window is open. No wonder it’s cold.')),
        TF('高い 物が いつも いい わけではない。', ('Selon cette phrase, ce qui est cher est toujours bon.', 'According to this sentence, expensive things are always good.'), FAUX, ('〜わけではない : pas forcément.', '〜わけではない: not necessarily.')),
      ]),
    L('n3-okage-sei', ('Grâce à, à cause de : 〜おかげで・〜せいで', 'Thanks to, because of: 〜おかげで・〜せいで'), ('Attribuer un bon résultat à quelqu’un, ou un mauvais à une cause.', 'Credit someone for a good result, or blame a cause for a bad one.'), 9, [
        ('〜おかげで = grâce à (résultat positif, avec gratitude) : 先生の おかげで、合格しました.', '〜おかげで = thanks to (positive result, with gratitude): 先生の おかげで、合格しました.'),
        ('〜せいで = à cause de, par la faute de (résultat négatif) : 雨の せいで、試合が 中止に なりました.', '〜せいで = because of, through the fault of (negative result): 雨の せいで、試合が 中止に なりました.'),
        ('Les deux suivent nom + の ou la forme neutre : 手伝って くれた おかげで, 寝坊した せいで.', 'Both follow noun + の or the plain form: 手伝って くれた おかげで, 寝坊した せいで.'),
      ], [
        G('gram-n3-okage-de', '〜おかげで', '〜おかげで', '~okage de', ('grâce à…', 'thanks to…')),
        G('gram-n3-sei-de', '〜せいで', '〜せいで', '~sei de', ('à cause de…, par la faute de…', 'because of…, through the fault of…')),
        V('vocab-goukaku', '合格', 'ごうかく', 'goukaku', ('réussite (à un examen)', 'passing (an exam)')),
        V('vocab-chuushi', '中止', 'ちゅうし', 'chuushi', ('annulation', 'cancellation')),
        V('vocab-nebou', '寝坊', 'ねぼう', 'nebou', ('panne d’oreiller, se lever trop tard', 'oversleeping')),
        V('vocab-makemasu', '負けます', 'まけます', 'makemasu', ('perdre (un match)', 'to lose (a match)')),
        K('kanji-tasukeru', '助', 'たすける', 'tasukeru', ('aider, sauver', 'help, rescue'), ['ジョ'], ['たす(ける)', 'たす(かる)'], 7),
        K('kanji-makeru', '負', 'まける', 'makeru', ('perdre, porter (un fardeau)', 'lose, bear (a burden)'), ['フ'], ['ま(ける)', 'お(う)'], 9),
      ], [
        ex('みなさんの おかげで、試験に 合格できました。', 'みなさんの おかげで、しけんに ごうかくできました。', 'Grâce à vous tous, j’ai réussi l’examen.', 'Thanks to all of you, I passed the exam.'),
        ex('寝坊した せいで、電車に 乗り遅れて しまいました。', 'ねぼうした せいで、でんしゃに のりおくれて しまいました。', 'À cause de ma panne d’oreiller, j’ai raté mon train.', 'Because I overslept, I missed my train.'),
      ], [
        FB(CHOOSE, '友だちが 手伝って くれた ＿、早く 終わりました。', ['おかげで', 'せいで', 'のに'], 'おかげで', ('Résultat positif : 〜おかげで.', 'Positive result: 〜おかげで.'), ('Grâce à l’aide de mon ami, j’ai fini vite.', 'Thanks to my friend’s help, I finished quickly.')),
        FB(CHOOSE, '台風の ＿、旅行が 中止に なりました。', ['せいで', 'おかげで', 'ために'], 'せいで', ('Résultat négatif subi : 〜せいで.', 'Negative result: 〜せいで.'), ('À cause du typhon, le voyage a été annulé.', 'Because of the typhoon, the trip was cancelled.')),
        DC(('Ton professeur te félicite pour ton examen. Que réponds-tu ?', 'Your teacher congratulates you on your exam. What do you answer?'), [('先生', '合格、おめでとう！')], ('Le professeur te félicite d’avoir réussi.', 'The teacher congratulates you on passing.'), ['先生の おかげです。', '先生の せいです。', '先生の わけです。'], '先生の おかげです。', ('Remercier : 〜のおかげです.', 'Giving thanks: 〜のおかげです.')),
        TF('彼の ミスの せいで、試合に 負けました。', ('La personne remercie son coéquipier.', 'The speaker is thanking their teammate.'), FAUX, ('〜せいで désigne un responsable d’un mauvais résultat.', '〜せいで points to someone responsible for a bad result.')),
      ]),
    L('n3-ni-yotte', ('Selon, par, à cause de : 〜によって', 'Depending on, by, due to: 〜によって'), ('Exprimer la variation, le moyen ou l’auteur avec 〜によって.', 'Express variation, means or agent with 〜によって.'), 10, [
        ('Variation : 国に よって 習慣が 違います = les coutumes varient selon les pays.', 'Variation: 国に よって 習慣が 違います = customs differ depending on the country.'),
        ('Cause ou moyen (style écrit) : 事故に よって 電車が 止まりました ; インターネットに よって 情報を 集めます.', 'Cause or means (written style): 事故に よって 電車が 止まりました; インターネットに よって 情報を 集めます.'),
        ('Auteur d’un passif : この 寺は 有名な 人に よって 建てられました.', 'Agent of a passive: この 寺は 有名な 人に よって 建てられました.'),
      ], [
        G('gram-n3-ni-yotte', '〜によって', '〜によって', '~ni yotte', ('selon…, par…, à cause de…', 'depending on…, by…, due to…')),
        V('vocab-shuukan', '習慣', 'しゅうかん', 'shuukan', ('coutume, habitude', 'custom, habit')),
        V('vocab-chigaimasu', '違います', 'ちがいます', 'chigaimasu', ('être différent ; se tromper', 'to differ; to be wrong')),
        V('vocab-jiko', '事故', 'じこ', 'jiko', ('accident', 'accident')),
        V('vocab-tatemasu', '建てます', 'たてます', 'tatemasu', ('construire', 'to build')),
        K('kanji-chigau', '違', 'ちがう', 'chigau', ('différer, erreur', 'differ, mistake'), ['イ'], ['ちが(う)', 'ちが(える)'], 13),
        K('kanji-yoru', '因', 'よる', 'yoru', ('cause, dépendre de', 'cause, depend on'), ['イン'], ['よ(る)'], 6),
      ], [
        ex('人に よって、考え方が 違います。', 'ひとに よって、かんがえかたが ちがいます。', 'La façon de penser diffère selon les personnes.', 'Ways of thinking differ from person to person.'),
        ex('この 橋は 百年前に 外国の 会社に よって 建てられました。', 'この はしは ひゃくねんまえに がいこくの かいしゃに よって たてられました。', 'Ce pont a été construit il y a cent ans par une entreprise étrangère.', 'This bridge was built a hundred years ago by a foreign company.'),
      ], [
        FB(CHOOSE, '店＿ よって、値段が 違います。', ['に', 'を', 'で'], 'に', ('〜によって : variation selon….', '〜によって: variation depending on….'), ('Le prix varie selon les magasins.', 'The price differs depending on the shop.')),
        FB(COMPLETE, '事故＿、道が 込んで います。', ['によって', 'にとって', 'について'], 'によって', ('Cause : 〜によって.', 'Cause: 〜によって.'), ('À cause d’un accident, la route est embouteillée.', 'Due to an accident, the road is congested.')),
        TF('この 絵は ピカソに よって 描かれました。', ('C’est Picasso qui a peint ce tableau.', 'It was Picasso who painted this picture.'), VRAI, ('に よって marque l’auteur d’une phrase passive.', 'に よって marks the agent of a passive sentence.')),
        SO(('Remets dans l’ordre : « Les coutumes varient selon les pays. »', 'Put in order: “Customs differ depending on the country.”'), ['国に', 'よって', '習慣が', '違います。'], ('Nom + に よって + ce qui varie.', 'Noun + に よって + what varies.')),
      ]),
  ])])

# ═════════════════════════ Île 6 : degrés et limites ═════════════════════════
W6 = WORLD('n3-w6', ('Degrés et limites', 'Degrees and limits'), REGION,
  ('Dire à quel point, donner un ordre de grandeur et poser une condition suffisante.', 'Say to what extent, give a rough measure, and state a sufficient condition.'),
  (('L’Oni des Extrêmes', 'The Oni of Extremes'), '程', ('Cet ogre exagère tout. Mesure chaque chose avec précision, sinon il grossira jusqu’au ciel !', 'This ogre exaggerates everything. Measure each thing precisely, or he will swell up to the sky!')),
  [CH('n3-w6-c1', ('Au point de, à peu près, il suffit de', 'So much that, roughly, all it takes'), [
    L('n3-hodo', ('À quel point : 〜ほど', 'To what extent: 〜ほど'), ('Exprimer un degré, une comparaison négative et une proportion.', 'Express a degree, a negative comparison and a proportion.'), 10, [
        ('〜ほど = au point de : 死ぬほど 疲れました (fatigué à en mourir), 驚くほど 安い.', '〜ほど = to the point of: 死ぬほど 疲れました (dead tired), 驚くほど 安い.'),
        ('A は B ほど 〜ない = A n’est pas aussi… que B : 今年は 去年ほど 寒くないです.', 'A は B ほど 〜ない = A is not as… as B: 今年は 去年ほど 寒くないです.'),
        ('〜ば 〜ほど = plus… plus… : 練習すれば するほど、上手に なります.', '〜ば 〜ほど = the more… the more…: 練習すれば するほど、上手に なります.'),
      ], [
        G('gram-n3-hodo', '〜ほど', '〜ほど', '~hodo', ('au point de…, tellement que…', 'to the point of…, so much that…')),
        G('gram-n3-hodo-nai', '〜ほど〜ない', '〜ほど〜ない', '~hodo ~nai', ('pas aussi… que…', 'not as… as…')),
        G('gram-n3-ba-hodo', '〜ば〜ほど', '〜ば〜ほど', '~ba ~hodo', ('plus… plus…', 'the more… the more…')),
        V('vocab-odorokimasu', '驚きます', 'おどろきます', 'odorokimasu', ('être surpris, s’étonner', 'to be surprised, to be amazed')),
        V('vocab-kyonen', '去年', 'きょねん', 'kyonen', ('l’année dernière', 'last year')),
        V('vocab-shinimasu', '死にます', 'しにます', 'shinimasu', ('mourir', 'to die')),
        K('kanji-hodo', '程', 'ほど', 'hodo', ('degré, mesure', 'degree, extent'), ['テイ'], ['ほど'], 12),
        K('kanji-odoroku', '驚', 'おどろく', 'odoroku', ('s’étonner', 'be surprised'), ['キョウ'], ['おどろ(く)', 'おどろ(かす)'], 22),
      ], [
        ex('今日は 歩けないほど 疲れました。', 'きょうは あるけないほど つかれました。', 'Aujourd’hui, je suis fatigué au point de ne plus pouvoir marcher.', 'Today I’m so tired I can’t walk.'),
        ex('日本語は 勉強すれば するほど、おもしろく なります。', 'にほんごは べんきょうすれば するほど、おもしろく なります。', 'Plus on étudie le japonais, plus il devient intéressant.', 'The more you study Japanese, the more interesting it becomes.'),
      ], [
        FB(CHOOSE, '今年の 冬は 去年＿ 寒くないです。', ['ほど', 'より', 'まで'], 'ほど', ('A は B ほど 〜ない.', 'A は B ほど 〜ない.'), ('Cet hiver n’est pas aussi froid que celui de l’an dernier.', 'This winter is not as cold as last year’s.')),
        FB(CHOOSE, '考えれば 考える＿、分からなく なります。', ['ほど', 'ばかり', 'のに'], 'ほど', ('〜ば 〜ほど = plus… plus….', '〜ば 〜ほど = the more… the more….'), ('Plus j’y réfléchis, moins je comprends.', 'The more I think about it, the less I understand.')),
        FB(COMPLETE, 'この 店の ケーキは 驚く＿ おいしいです。', ['ほど', 'より', 'ので'], 'ほど', ('Degré : 驚くほど = étonnamment.', 'Degree: 驚くほど = amazingly.'), ('Les gâteaux de ce magasin sont étonnamment bons.', 'This shop’s cakes are amazingly good.')),
        TF('東京は 大阪ほど 暑くない。', ('Selon cette phrase, il fait plus chaud à Osaka qu’à Tokyo.', 'According to this sentence, Osaka is hotter than Tokyo.'), VRAI, ('Tokyo n’est pas aussi chaud qu’Osaka.', 'Tokyo is not as hot as Osaka.')),
      ]),
    L('n3-kurai', ('À peu près, au moins : 〜くらい・〜ぐらい', 'About, at least: 〜くらい・〜ぐらい'), ('Donner un ordre de grandeur, un degré et un minimum.', 'Give a rough measure, a degree and a minimum.'), 9, [
        ('Quantité approximative : 一時間ぐらい 待ちました. Degré : 泣きたいくらい うれしいです.', 'Approximate amount: 一時間ぐらい 待ちました. Degree: 泣きたいくらい うれしいです.'),
        ('Minimum, avec une nuance de « c’est peu de chose » : 自分の 部屋ぐらい、自分で 掃除しなさい.', 'Minimum, with a nuance of “it is a small thing”: 自分の 部屋ぐらい、自分で 掃除しなさい.'),
        ('くらい et ぐらい ont le même sens. Avec 〜はない : 彼ぐらい 親切な 人は いません.', 'くらい and ぐらい mean the same. With 〜はない: 彼ぐらい 親切な 人は いません.'),
      ], [
        G('gram-n3-kurai', '〜くらい・〜ぐらい', '〜くらい・〜ぐらい', '~kurai / ~gurai', ('environ ; au point de ; au moins', 'about; to the extent of; at least')),
        V('vocab-nakimasu', '泣きます', 'なきます', 'nakimasu', ('pleurer', 'to cry')),
        V('vocab-chanto', 'ちゃんと', 'ちゃんと', 'chanto', ('correctement, comme il faut', 'properly')),
        V('vocab-aisatsu', 'あいさつ', 'あいさつ', 'aisatsu', ('salutation', 'greeting')),
        K('kanji-kurai', '位', 'くらい', 'kurai', ('rang, environ', 'rank, about'), ['イ'], ['くらい'], 7),
        K('kanji-naku', '泣', 'なく', 'naku', ('pleurer', 'cry'), ['キュウ'], ['な(く)'], 8),
      ], [
        ex('合格したと 聞いて、泣きたいくらい うれしかったです。', 'ごうかくしたと きいて、なきたいくらい うれしかったです。', 'En apprenant que j’étais reçu, j’étais heureux à en pleurer.', 'When I heard I had passed, I was so happy I could have cried.'),
        ex('あいさつぐらい、ちゃんと しなさい。', 'あいさつぐらい、ちゃんと しなさい。', 'Dis au moins bonjour correctement.', 'At least greet people properly.'),
      ], [
        FB(CHOOSE, '駅から 学校まで 歩いて 十分＿ です。', ['ぐらい', 'ほどない', 'ばかりで'], 'ぐらい', ('Durée approximative : 〜ぐらい.', 'Approximate duration: 〜ぐらい.'), ('De la gare à l’école, il y a environ dix minutes à pied.', 'It’s about ten minutes on foot from the station to the school.')),
        FB(COMPLETE, '名前＿ 漢字で 書けるように なりたいです。', ['ぐらい', 'ほど', 'より'], 'ぐらい', ('Minimum : au moins mon nom.', 'Minimum: at least my name.'), ('Je voudrais au moins savoir écrire mon nom en kanji.', 'I’d like at least to be able to write my name in kanji.')),
        TF('この 問題は 子どもでも できるくらい 簡単です。', ('Le problème est très facile.', 'The problem is very easy.'), VRAI, ('Facile au point que même un enfant y arrive.', 'So easy that even a child can do it.')),
        SO(('Remets dans l’ordre : « J’ai attendu environ une heure. »', 'Put in order: “I waited about an hour.”'), ['一時間', 'ぐらい', '待ちました。'], ('Durée + ぐらい + verbe.', 'Duration + ぐらい + verb.')),
      ]),
    L('n3-sae', ('Même, il suffit de : 〜さえ', 'Even, as long as: 〜さえ'), ('Citer un exemple extrême, et poser la seule condition nécessaire.', 'Give an extreme example, and state the only condition needed.'), 10, [
        ('Nom + さえ = même (exemple extrême) : 忙しくて、寝る 時間さえ ありません.', 'Noun + さえ = even (extreme example): 忙しくて、寝る 時間さえ ありません.'),
        ('〜さえ 〜ば = il suffit que… : お金さえ あれば、買えます ; 薬を 飲みさえすれば、治ります.', '〜さえ 〜ば = as long as…, if only…: お金さえ あれば、買えます; 薬を 飲みさえすれば、治ります.'),
        ('さえ remplace が et を, et s’ajoute après les autres particules : 親にさえ 言えません.', 'さえ replaces が and を, and is added after other particles: 親にさえ 言えません.'),
      ], [
        G('gram-n3-sae', '〜さえ', '〜さえ', '~sae', ('même… (exemple extrême)', 'even… (extreme example)')),
        G('gram-n3-sae-ba', '〜さえ〜ば', '〜さえ〜ば', '~sae ~ba', ('il suffit que…, pourvu que…', 'as long as…, if only…')),
        V('vocab-dare-demo', 'だれでも', 'だれでも', 'dare demo', ('n’importe qui, tout le monde', 'anyone, everyone')),
        V('vocab-tayorimasu', '頼ります', 'たよります', 'tayorimasu', ('compter sur, s’appuyer sur', 'to rely on')),
        V('vocab-naorimasu', '治ります', 'なおります', 'naorimasu', ('guérir', 'to get better, to heal')),
        K('kanji-hima', '暇', 'ひま', 'hima', ('loisir, temps libre', 'leisure, spare time'), ['カ'], ['ひま'], 13),
        K('kanji-tanomu', '頼', 'たのむ', 'tanomu', ('demander, compter sur', 'request, rely on'), ['ライ'], ['たの(む)', 'たよ(る)'], 16),
      ], [
        ex('忙しすぎて、ごはんを 食べる 暇さえ ありません。', 'いそがしすぎて、ごはんを たべる ひまさえ ありません。', 'Je suis tellement occupé que je n’ai même pas le temps de manger.', 'I’m so busy that I don’t even have time to eat.'),
        ex('この 薬を 飲みさえすれば、すぐ 治りますよ。', 'この くすりを のみさえすれば、すぐ なおりますよ。', 'Il suffit de prendre ce médicament pour guérir vite.', 'As long as you take this medicine, you’ll soon get better.'),
      ], [
        FB(CHOOSE, '時間＿ あれば、旅行に 行けるのに。', ['さえ', 'ほど', 'ばかり'], 'さえ', ('Seule condition : 〜さえ あれば.', 'Only condition: 〜さえ あれば.'), ('Si seulement j’avais le temps, je pourrais partir en voyage.', 'If only I had the time, I could go on a trip.')),
        FB(CHOOSE, 'あの 人は ひらがな＿ 読めません。', ['さえ', 'ぐらい', 'ほど'], 'さえ', ('Exemple extrême : même les hiragana.', 'Extreme example: even hiragana.'), ('Cette personne ne sait même pas lire les hiragana.', 'That person cannot even read hiragana.')),
        FB(CHOOSE, '練習し＿ すれば、だれでも できます。', ['さえ', 'ほど', 'のに'], 'さえ', ('Radical + さえすれば.', 'Stem + さえすれば.'), ('Il suffit de s’entraîner, tout le monde peut y arriver.', 'As long as you practise, anyone can do it.')),
        TF('あなたさえ いれば、何も いりません。', ('La personne a besoin de beaucoup de choses en plus.', 'The speaker needs many other things as well.'), FAUX, ('〜さえ いれば : toi seul suffis.', '〜さえ いれば: you alone are enough.')),
      ]),
  ])])

# ═════════════════════════ Île 7 : points de vue ═════════════════════════
W7 = WORLD('n3-w7', ('Points de vue', 'Points of view'), REGION,
  ('Dire pour qui, envers qui, à propos de quoi et en tant que quoi.', 'Say for whom, towards whom, about what and in what capacity.'),
  (('Le Corbeau aux Trois Regards', 'The Three-Eyed Crow'), '観', ('Le corbeau voit chaque chose sous trois angles. Choisis le bon point de vue, ou il t’embrouille !', 'The crow sees everything from three angles. Pick the right point of view, or he will muddle you!')),
  [CH('n3-w7-c1', ('Pour, envers, à propos de, en tant que', 'For, towards, about, as'), [
    L('n3-ni-totte', ('Pour moi, envers lui : 〜にとって・〜に対して', 'For me, towards him: 〜にとって・〜に対して'), ('Distinguer le point de vue (にとって) et la cible d’une attitude (に対して).', 'Distinguish the point of view (にとって) from the target of an attitude (に対して).'), 10, [
        ('〜にとって = pour, du point de vue de (suivi d’un jugement) : 私に とって、家族は 宝物です.', '〜にとって = for, from the standpoint of (followed by a judgement): 私に とって、家族は 宝物です.'),
        ('〜に対して = envers, à l’égard de (attitude, action dirigée) : 先生は 学生に 対して 厳しいです.', '〜に対して = towards, with regard to (attitude, directed action): 先生は 学生に 対して 厳しいです.'),
        ('〜に対して marque aussi un contraste : 兄が 静かなのに 対して、弟は にぎやかです.', '〜に対して also marks a contrast: 兄が 静かなのに 対して、弟は にぎやかです.'),
      ], [
        G('gram-n3-ni-totte', '〜にとって', '〜にとって', '~ni totte', ('pour…, du point de vue de…', 'for…, from the standpoint of…')),
        G('gram-n3-ni-taishite', '〜に対して', '〜にたいして', '~ni taishite', ('envers… ; par contraste avec…', 'towards… ; in contrast to…')),
        V('vocab-takaramono', '宝物', 'たからもの', 'takaramono', ('trésor', 'treasure')),
        V('vocab-kibishii', '厳しい', 'きびしい', 'kibishii', ('sévère, strict', 'strict, severe')),
        V('vocab-taido', '態度', 'たいど', 'taido', ('attitude', 'attitude')),
        K('kanji-takara', '宝', 'たから', 'takara', ('trésor', 'treasure'), ['ホウ'], ['たから'], 8),
        K('kanji-kibishii', '厳', 'きびしい', 'kibishii', ('sévère, strict', 'strict, severe'), ['ゲン'], ['きび(しい)'], 17),
      ], [
        ex('外国人に とって、漢字は とても 難しいです。', 'がいこくじんに とって、かんじは とても むずかしいです。', 'Pour les étrangers, les kanji sont très difficiles.', 'For foreigners, kanji are very difficult.'),
        ex('お客さんに 対して、失礼な 態度を とっては いけません。', 'おきゃくさんに たいして、しつれいな たいどを とっては いけません。', 'Il ne faut pas avoir une attitude impolie envers les clients.', 'You must not take a rude attitude towards customers.'),
      ], [
        FB(CHOOSE, '私＿、この 写真は 大切な 宝物です。', ['にとって', 'に対して', 'について'], 'にとって', ('Point de vue + jugement : 〜にとって.', 'Point of view + judgement: 〜にとって.'), ('Pour moi, cette photo est un trésor précieux.', 'For me, this photo is a precious treasure.')),
        FB(CHOOSE, 'あの 先生は 学生＿ とても 親切です。', ['に対して', 'にとって', 'によって'], 'に対して', ('Attitude dirigée vers quelqu’un : 〜に対して.', 'Attitude directed at someone: 〜に対して.'), ('Ce professeur est très gentil envers les étudiants.', 'That teacher is very kind towards the students.')),
        FB(CHOOSE, '子ども＿、遊びは 大切な 勉強です。', ['にとって', 'に対して', 'によると'], 'にとって', ('Du point de vue des enfants.', 'From the children’s point of view.'), ('Pour les enfants, le jeu est un apprentissage important.', 'For children, play is an important kind of learning.')),
        TF('父は 弟に 対して 厳しい。', ('Le père est sévère envers le petit frère.', 'The father is strict towards the younger brother.'), VRAI, ('に対して indique à qui s’adresse l’attitude.', 'に対して shows whom the attitude is directed at.')),
      ]),
    L('n3-ni-tsuite', ('À propos de : 〜について・〜に関して', 'About: 〜について・〜に関して'), ('Indiquer le sujet dont on parle, qu’on étudie ou qu’on interroge.', 'State the topic you talk about, study or ask about.'), 9, [
        ('〜について = au sujet de : 日本の 文化に ついて 調べて います.', '〜について = about: 日本の 文化に ついて 調べて います.'),
        ('〜に関して a le même sens en plus formel (exposés, annonces) : この 件に 関して、ご説明します.', '〜に関して means the same but is more formal (presentations, announcements): この 件に 関して、ご説明します.'),
        ('Devant un nom : 〜についての, 〜に関する : 環境に 関する ニュース.', 'Before a noun: 〜についての, 〜に関する: 環境に 関する ニュース.'),
      ], [
        G('gram-n3-ni-tsuite', '〜について', '〜について', '~ni tsuite', ('au sujet de…, à propos de…', 'about…, concerning…')),
        G('gram-n3-ni-kanshite', '〜に関して', '〜にかんして', '~ni kanshite', ('concernant… (formel)', 'regarding… (formal)')),
        V('vocab-bunka', '文化', 'ぶんか', 'bunka', ('culture', 'culture')),
        V('vocab-shirabemasu', '調べます', 'しらべます', 'shirabemasu', ('rechercher, vérifier', 'to look up, to investigate')),
        V('vocab-kankyou', '環境', 'かんきょう', 'kankyou', ('environnement', 'environment')),
        V('vocab-rekishi', '歴史', 'れきし', 'rekishi', ('histoire (du passé)', 'history')),
        K('kanji-seki', '関', 'せき', 'seki', ('relation, barrière', 'relation, barrier'), ['カン'], ['せき', 'かか(わる)'], 14),
        K('kanji-shiraberu', '調', 'しらべる', 'shiraberu', ('examiner, ton', 'investigate, tone'), ['チョウ'], ['しら(べる)', 'ととの(える)'], 15),
      ], [
        ex('日本の お祭りに ついて、レポートを 書きました。', 'にほんの おまつりに ついて、レポートを かきました。', 'J’ai écrit un rapport sur les fêtes japonaises.', 'I wrote a report about Japanese festivals.'),
        ex('環境に 関する 問題に ついて、意見を 聞かせて ください。', 'かんきょうに かんする もんだいに ついて、いけんを きかせて ください。', 'Donnez-moi votre avis sur les problèmes liés à l’environnement.', 'Please tell me your opinion about environmental issues.'),
      ], [
        FB(CHOOSE, 'この 町の 歴史＿ 調べて います。', ['について', 'にとって', 'に対して'], 'について', ('Sujet d’une recherche : 〜について.', 'Topic of research: 〜について.'), ('Je fais des recherches sur l’histoire de cette ville.', 'I’m researching the history of this town.')),
        FB(CHOOSE, '日本の 文化に 関＿ 本を 読みました。', ['する', 'して', 'した'], 'する', ('Devant un nom : 〜に関する.', 'Before a noun: 〜に関する.'), ('J’ai lu un livre concernant la culture japonaise.', 'I read a book concerning Japanese culture.')),
        DC(('En réunion, tu annonces poliment le thème de ton exposé.', 'In a meeting, you politely announce the topic of your presentation.'), [('部長', 'では、お願いします。')], ('Ton chef te donne la parole.', 'Your manager gives you the floor.'), ['新しい 計画に 関して、ご説明します。', '新しい 計画に とって、ご説明します。', '新しい 計画の せいで、ご説明します。'], '新しい 計画に 関して、ご説明します。', ('Registre formel : 〜に関して.', 'Formal register: 〜に関して.')),
        SO(('Remets dans l’ordre : « Parlons de l’avenir. »', 'Put in order: “Let’s talk about the future.”'), ['将来に', 'ついて', '話しましょう。'], ('Nom + に ついて + verbe de parole.', 'Noun + に ついて + speech verb.')),
      ]),
    L('n3-toshite', ('En tant que : 〜として', 'As: 〜として'), ('Préciser un rôle, une fonction ou une qualité.', 'Specify a role, a function or a capacity.'), 9, [
        ('Nom + として = en tant que, à titre de : 留学生と して 日本に 来ました.', 'Noun + として = as, in the capacity of: 留学生と して 日本に 来ました.'),
        ('〜としては = pour ce qui est de, en tant que… (avis) : 私と しては、反対です.', '〜としては = as for, speaking as… (opinion): 私と しては、反対です.'),
        ('〜としても = même en tant que… ; devant un nom : 〜としての : 親と しての 責任.', '〜としても = even as…; before a noun: 〜としての: 親と しての 責任.'),
      ], [
        G('gram-n3-toshite', '〜として', '〜として', '~toshite', ('en tant que…, à titre de…', 'as…, in the capacity of…')),
        V('vocab-daihyou', '代表', 'だいひょう', 'daihyou', ('représentant', 'representative')),
        V('vocab-sekinin', '責任', 'せきにん', 'sekinin', ('responsabilité', 'responsibility')),
        V('vocab-shumi', '趣味', 'しゅみ', 'shumi', ('passe-temps, loisir', 'hobby')),
        K('kanji-omote', '表', 'おもて', 'omote', ('surface, exprimer, tableau', 'surface, express, chart'), ['ヒョウ'], ['おもて', 'あらわ(す)'], 8),
        K('kanji-kawaru', '代', 'かわる', 'kawaru', ('remplacer, époque', 'substitute, era'), ['ダイ', 'タイ'], ['か(わる)', 'よ'], 5),
      ], [
        ex('彼は 学校の 代表と して、大会に 出ました。', 'かれは がっこうの だいひょうと して、たいかいに でました。', 'Il a participé au tournoi en tant que représentant de l’école.', 'He took part in the tournament as the school’s representative.'),
        ex('趣味と して、週末に 絵を 描いて います。', 'しゅみと して、しゅうまつに えを かいて います。', 'Comme passe-temps, je peins le week-end.', 'As a hobby, I paint at weekends.'),
      ], [
        FB(CHOOSE, '彼女は 医者＿ 働いて います。', ['として', 'にとって', 'について'], 'として', ('Rôle, fonction : 〜として.', 'Role, function: 〜として.'), ('Elle travaille comme médecin.', 'She works as a doctor.')),
        FB(CHOOSE, '親と して＿ 責任を 感じます。', ['の', 'は', 'も'], 'の', ('Devant un nom : 〜としての.', 'Before a noun: 〜としての.'), ('Je ressens ma responsabilité de parent.', 'I feel my responsibility as a parent.')),
        TF('私と しては、その 計画に 賛成です。', ('La personne donne son avis personnel.', 'The speaker is giving their personal opinion.'), VRAI, ('〜としては = pour ma part.', '〜としては = for my part.')),
        SO(('Remets dans l’ordre : « Je suis venu au Japon comme étudiant étranger. »', 'Put in order: “I came to Japan as a foreign student.”'), ['留学生', 'として', '日本に', '来ました。'], ('Nom + として + action.', 'Noun + として + action.')),
      ]),
  ])])

# ═════════════════════════ Île 8 : devoirs et tendances ═════════════════════════
W8 = WORLD('n3-w8', ('Devoirs et tendances', 'Duties and tendencies'), REGION,
  ('Dire ce qu’il convient de faire, décrire une tendance et faire sans.', 'Say what ought to be done, describe a tendency, and do without.'),
  (('Le Daruma Inflexible', 'The Unbending Daruma'), '義', ('Le Daruma ne tombe jamais et ne pardonne aucun « je devrais ». Tiens bon jusqu’au bout !', 'The Daruma never falls over and forgives no “I should”. Hold firm to the end!')),
  [CH('n3-w8-c1', ('Il faut, avoir tendance à, sans', 'One should, tend to, without'), [
    L('n3-beki', ('Il convient de : 〜べきだ', 'One ought to: 〜べきだ'), ('Exprimer ce qu’il est juste de faire, ou de ne pas faire.', 'Express what it is right to do, or not to do.'), 9, [
        ('Dictionnaire + べきだ = il faut, on devrait (jugement moral, conseil fort) : 約束は 守るべきです.', 'Dictionary form + べきだ = one ought to (moral judgement, strong advice): 約束は 守るべきです.'),
        ('Négation : 〜べきではない (et non 〜ないべき) : 人の 悪口を 言うべきではありません.', 'Negative: 〜べきではない (not 〜ないべき): 人の 悪口を 言うべきではありません.'),
        ('する → するべき ou すべき. Au passé, 〜べきだった exprime un regret : もっと 早く 謝るべきでした.', 'する → するべき or すべき. In the past, 〜べきだった expresses regret: もっと 早く 謝るべきでした.'),
      ], [
        G('gram-n3-beki', '〜べきだ', '〜べきだ', '~beki da', ('il convient de…, on devrait…', 'one ought to…, should…')),
        G('gram-n3-beki-dewa-nai', '〜べきではない', '〜べきではない', '~beki dewa nai', ('on ne devrait pas…', 'one ought not to…')),
        V('vocab-ayamarimasu', '謝ります', 'あやまります', 'ayamarimasu', ('s’excuser', 'to apologise')),
        V('vocab-kotowarimasu', '断ります', 'ことわります', 'kotowarimasu', ('refuser, décliner', 'to refuse, to decline')),
        V('vocab-waruguchi', '悪口', 'わるぐち', 'waruguchi', ('médisance, dire du mal', 'speaking ill, slander')),
        K('kanji-ayamaru', '謝', 'あやまる', 'ayamaru', ('s’excuser, remercier', 'apologise, thank'), ['シャ'], ['あやま(る)'], 17),
        K('kanji-kotowaru', '断', 'ことわる', 'kotowaru', ('refuser, trancher', 'refuse, sever'), ['ダン'], ['ことわ(る)', 'た(つ)'], 11),
      ], [
        ex('悪い ことを したら、すぐに 謝るべきです。', 'わるい ことを したら、すぐに あやまるべきです。', 'Quand on a mal agi, on doit s’excuser tout de suite.', 'When you have done something wrong, you ought to apologise at once.'),
        ex('あの とき、はっきり 断るべきでした。', 'あの とき、はっきり ことわるべきでした。', 'À ce moment-là, j’aurais dû refuser clairement.', 'At that time, I should have refused clearly.'),
      ], [
        FB(CHOOSE, '学生は もっと 本を 読む＿。', ['べきです', 'べきないです', 'ばかりです'], 'べきです', ('Dictionnaire + べきだ.', 'Dictionary form + べきだ.'), ('Les étudiants devraient lire davantage.', 'Students ought to read more.')),
        FB(CHOOSE, '人の 悪口を 言う＿。', ['べきではありません', 'ないべきです', 'べきでした'], 'べきではありません', ('Négation : 〜べきではない.', 'Negative: 〜べきではない.'), ('On ne devrait pas dire du mal des autres.', 'One ought not to speak ill of others.')),
        FB(COMPLETE, '試験の 前に、もっと 勉強する＿。', ['べきでした', 'べきです', 'はずでした'], 'べきでした', ('Regret : 〜べきだった.', 'Regret: 〜べきだった.'), ('J’aurais dû étudier davantage avant l’examen.', 'I should have studied more before the exam.')),
        TF('約束は 守るべきだ。', ('Selon cette phrase, il est normal de tenir ses promesses.', 'According to this sentence, it is right to keep one’s promises.'), VRAI, ('〜べきだ exprime ce qui est juste.', '〜べきだ expresses what is right.')),
      ]),
    L('n3-gachi', ('Avoir tendance à : 〜がち・〜っぽい', 'Tending to: 〜がち・〜っぽい'), ('Décrire une tendance fâcheuse ou une impression dominante.', 'Describe an unwelcome tendency or a dominant impression.'), 9, [
        ('Radical ou nom + がち = avoir (trop) tendance à : 最近、忘れがちです ; 曇りがちの 天気 ; 病気がち.', 'Stem or noun + がち = tend (too much) to: 最近、忘れがちです; 曇りがちの 天気; 病気がち.'),
        ('〜っぽい = qui fait…, qui a l’air de… : 子どもっぽい (puéril), 忘れっぽい (étourdi), 白っぽい (blanchâtre).', '〜っぽい = -ish, having the air of…: 子どもっぽい (childish), 忘れっぽい (forgetful), 白っぽい (whitish).'),
        ('がち décrit une fréquence, っぽい une impression ou un trait de caractère. Les deux sont souvent négatifs.', 'がち describes frequency, っぽい an impression or a character trait. Both are often negative.'),
      ], [
        G('gram-n3-gachi', '〜がち', '〜がち', '~gachi', ('avoir tendance à… (fâcheuse)', 'tend to… (unwelcome)')),
        G('gram-n3-ppoi', '〜っぽい', '〜っぽい', '~ppoi', ('qui fait…, un peu…', '-ish, rather like…')),
        V('vocab-undoubusoku', '運動不足', 'うんどうぶそく', 'undoubusoku', ('manque d’exercice', 'lack of exercise')),
        V('vocab-sobo', '祖母', 'そぼ', 'sobo', ('(ma) grand-mère', '(my) grandmother')),
        V('vocab-okorimasu', '怒ります', 'おこります', 'okorimasu', ('se fâcher', 'to get angry')),
        K('kanji-isogashii', '忙', 'いそがしい', 'isogashii', ('occupé', 'busy'), ['ボウ'], ['いそが(しい)'], 6),
        K('kanji-kumoru', '曇', 'くもる', 'kumoru', ('se couvrir (ciel)', 'cloud over'), ['ドン'], ['くも(る)'], 16),
      ], [
        ex('忙しいと、食事の 時間が 遅く なりがちです。', 'いそがしいと、しょくじの じかんが おそく なりがちです。', 'Quand on est débordé, on a tendance à manger tard.', 'When you’re busy, mealtimes tend to get later.'),
        ex('彼は 怒りっぽいので、気を つけて ください。', 'かれは おこりっぽいので、きを つけて ください。', 'Il se fâche facilement, faites attention.', 'He gets angry easily, so be careful.'),
      ], [
        FB(CHOOSE, '冬は 運動不足に なり＿ です。', ['がち', 'っぽい', 'ばかり'], 'がち', ('Tendance fréquente : 〜がち.', 'Frequent tendency: 〜がち.'), ('En hiver, on a tendance à manquer d’exercice.', 'In winter, people tend not to get enough exercise.')),
        FB(CHOOSE, '弟は もう 二十歳なのに、子ども＿ です。', ['っぽい', 'がち', 'らしい'], 'っぽい', ('Impression (négative) : 子どもっぽい = puéril.', 'Impression (negative): 子どもっぽい = childish.'), ('Mon petit frère a déjà vingt ans, et pourtant il est puéril.', 'My younger brother is already twenty, yet he is childish.')),
        FB(CHOOSE, '最近、曇り＿の 日が 続いて います。', ['がち', 'っぽく', 'そう'], 'がち', ('Nom + がち + の + nom.', 'Noun + がち + の + noun.'), ('Ces derniers temps, les journées plutôt nuageuses se succèdent.', 'Lately, we’ve had a run of mostly cloudy days.')),
        TF('祖母は 最近 忘れっぽく なりました。', ('La grand-mère oublie plus facilement qu’avant.', 'The grandmother forgets things more easily than before.'), VRAI, ('忘れっぽい = étourdi, qui oublie facilement.', '忘れっぽい = forgetful.')),
      ]),
    L('n3-zuni', ('Sans faire, inutile de : 〜ずに・〜ことはない', 'Without doing, no need to: 〜ずに・〜ことはない'), ('Dire qu’on agit sans faire autre chose, et rassurer : ce n’est pas la peine.', 'Say that you act without doing something else, and reassure: there is no need.'), 10, [
        ('Radical en ない + ずに = sans faire (équivalent écrit de 〜ないで) : 朝ごはんを 食べずに 出かけました.', 'ない-stem + ずに = without doing (written equivalent of 〜ないで): 朝ごはんを 食べずに 出かけました.'),
        ('Irrégulier : する → せずに. 予約せずに 行きました.', 'Irregular: する → せずに. 予約せずに 行きました.'),
        ('Dictionnaire + ことはない = ce n’est pas la peine de, inutile de : 心配する ことは ありません.', 'Dictionary form + ことはない = there is no need to: 心配する ことは ありません.'),
      ], [
        G('gram-n3-zuni', '〜ずに', '〜ずに', '~zu ni', ('sans faire…', 'without doing…')),
        G('gram-n3-koto-wa-nai', '〜ことはない', '〜ことはない', '~koto wa nai', ('inutile de…, pas la peine de…', 'there is no need to…')),
        V('vocab-tomarimasu', '泊まります', 'とまります', 'tomarimasu', ('passer la nuit, loger', 'to stay overnight')),
        V('vocab-yoyaku', '予約', 'よやく', 'yoyaku', ('réservation', 'reservation, booking')),
        V('vocab-awatemasu', '慌てます', 'あわてます', 'awatemasu', ('paniquer, se précipiter', 'to panic, to rush')),
        K('kanji-tomaru', '泊', 'とまる', 'tomaru', ('passer la nuit', 'stay overnight'), ['ハク'], ['と(まる)', 'と(める)'], 8),
        K('kanji-kubaru', '配', 'くばる', 'kubaru', ('distribuer', 'distribute'), ['ハイ'], ['くば(る)'], 10),
      ], [
        ex('予約せずに 行ったので、ホテルに 泊まれませんでした。', 'よやくせずに いったので、ホテルに とまれませんでした。', 'Comme j’y suis allé sans réserver, je n’ai pas pu loger à l’hôtel.', 'I went without booking, so I couldn’t stay at the hotel.'),
        ex('まだ 時間が ありますから、慌てる ことは ありません。', 'まだ じかんが ありますから、あわてる ことは ありません。', 'Il reste du temps, inutile de paniquer.', 'There is still time, so there is no need to panic.'),
      ], [
        FB(CHOOSE, '辞書を 使わ＿、この 本を 読みました。', ['ずに', 'ないに', 'なくに'], 'ずに', ('使わない → 使わずに.', '使わない → 使わずに.'), ('J’ai lu ce livre sans utiliser de dictionnaire.', 'I read this book without using a dictionary.')),
        FB(CHOOSE, '何も 連絡＿、会社を 休みました。', ['せずに', 'しずに', 'さずに'], 'せずに', ('する → せずに.', 'する → せずに.'), ('Il s’est absenté du travail sans prévenir.', 'He took the day off work without getting in touch.')),
        DC(('Ton ami s’inquiète pour un petit retard. Tu le rassures.', 'Your friend is worried about a small delay. You reassure them.'), [('友だち', '五分 遅れそう。どうしよう。')], ('Ton ami pense avoir cinq minutes de retard.', 'Your friend thinks they will be five minutes late.'), ['心配する ことは ないよ。', '心配するべきだよ。', '心配せずに いられないよ。'], '心配する ことは ないよ。', ('Rassurer : 〜ことはない.', 'Reassuring: 〜ことはない.')),
        TF('彼は かさを 持たずに 出かけました。', ('Il est sorti avec un parapluie.', 'He went out with an umbrella.'), FAUX, ('持たずに = sans prendre.', '持たずに = without taking.')),
      ]),
  ])])

FINAL = {
  'slug': 'n3-final',
  'title': t(('Simulation JLPT N3', 'JLPT N3 simulation')),
  'region': REGION,
  'description': t(('Examen blanc non officiel du N3 : vocabulaire et kanji, grammaire, écoute. Chronométré, corrigé par compétence.', 'Unofficial N3 mock exam: vocabulary and kanji, grammar, listening. Timed, marked by skill.')),
  'exam': 'n3-mock',
  'chapters': [],
}

level = {
  'contentVersion': '2026.11.16b',
  'level': {'code': 'N3', 'title': t(('Intermédiaire : comprendre le quotidien', 'Intermediate: understanding everyday Japanese')), 'region': REGION, 'order': 3},
  'notice': t(('Les listes de vocabulaire et de kanji de Koto Quest sont alignées sur les compétences attendues au N3 mais ne constituent pas des listes officielles du JLPT.', 'Koto Quest’s vocabulary and kanji lists are aligned with the skills expected at N3 but are not official JLPT lists.')),
  'worlds': [W1, W2, W3, W4, W5, W6, W7, W8, FINAL],
}
t((REGION, 'Snowy Peaks'))
os.makedirs(os.path.join(ROOT, 'content/n3'), exist_ok=True)
check_and_write(level, 'content/n3/n3.json', ['content/n5/n5.json', 'content/n4/n4.json'])
