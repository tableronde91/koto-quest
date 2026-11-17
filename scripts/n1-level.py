# Niveau N1 : 8 îles, 24 leçons et un examen blanc (français + anglais).
# Usage : python3 scripts/n1-level.py   (réécrit content/n1/n1.json)
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from kq_content import *

REGION = 'Domaine du shōgun'
ORDER = lambda fr, en: (f'Remets la phrase dans l’ordre : « {fr} »', f'Put the sentence in order: “{en}”')

# ═════════════════════════ Île 1 : ouvrir et clore ═════════════════════════
W1 = WORLD('n1-w1', ('Ouvrir et clore', 'Opening and closing'), REGION,
  ('Annoncer officiellement un début ou une fin, et dire qu’une chose en déclenche aussitôt une autre.', 'Formally announce a beginning or an end, and say that one thing immediately sets off another.'),
  (('Le Sceau Animé', 'The Living Seal'), '印', ('Ce vieux sceau d’État a pris vie après cent ans de service. Il refuse de se laisser apposer tant que le nouveau maître ne parle pas comme un décret : à compter de, à partir de, à peine… que…', 'This old seal of state came to life after a hundred years of service. It will not let itself be stamped until the new master speaks like a decree: as of, starting with, no sooner… than…')),
  [CH('n1-w1-c1', ('Décrets et signaux', 'Decrees and signals'), [
    L('n1-wo-motte', ('À compter de…, par le moyen de… : 〜をもって', 'As of…, by means of…: 〜をもって'), ('Annoncer une date officielle de fin et dire par quel moyen on agit, dans le style des communiqués.', 'Announce an official end date and say by what means one acts, in the style of official notices.'), 10, [
        ('Nom de date + をもって = à compter de, en date de (fin officielle) : 本日を もって 閉店いたします. C’est le style des annonces et des lettres officielles.', 'Date noun + をもって = as of, with effect from (official end): 本日を もって 閉店いたします. This is the style of announcements and formal letters.'),
        ('Nom de moyen + をもって = au moyen de, par : 書面を もって ご連絡いたします. C’est un で très soutenu.', 'Means noun + をもって = by means of, with: 書面を もって ご連絡いたします. It is a very formal で.'),
        ('〜をもってすれば = si l’on dispose de (une qualité, un moyen), alors… : 彼の 実力を もってすれば、優勝も 夢では ない.', '〜をもってすれば = with (a quality, a means), …: 彼の 実力を もってすれば、優勝も 夢では ない.'),
      ], [
        G('gram-n1-wo-motte', '〜をもって', '〜をもって', '~wo motte', ('à compter de… ; au moyen de… (soutenu)', 'as of… ; by means of… (formal)')),
        G('gram-n1-wo-motte-sureba', '〜をもってすれば', '〜をもってすれば', '~wo motte sureba', ('avec… (comme atout), il suffit de…', 'with… (as an asset), given…')),
        V('vocab-heiten', '閉店', 'へいてん', 'heiten', ('fermeture (d’un magasin)', 'closing (of a shop)')),
        V('vocab-shomen', '書面', 'しょめん', 'shomen', ('écrit, document écrit', 'written document, in writing')),
        V('vocab-jitsuryoku', '実力', 'じつりょく', 'jitsuryoku', ('compétence réelle, vrai niveau', 'real ability, true capability')),
        V('vocab-taishoku', '退職', 'たいしょく', 'taishoku', ('départ (d’un emploi), retraite', 'leaving a job, retirement')),
        K('kanji-n1-in', '印', 'いん', 'in', ('sceau, marque', 'seal, mark'), ['イン'], ['しるし'], 6),
        K('kanji-n1-ryou', '了', 'りょう', 'ryou', ('achever, comprendre', 'complete, understand'), ['リョウ'], [], 2),
      ], [
        ex('当店は 三月末日を もって 閉店いたします。', 'とうてんは さんがつまつじつを もって へいてんいたします。', 'Notre magasin fermera définitivement à compter du 31 mars.', 'This shop will close as of the end of March.'),
        ex('結果は 後日、書面を もって お知らせします。', 'けっかは ごじつ、しょめんを もって おしらせします。', 'Le résultat vous sera communiqué ultérieurement par écrit.', 'The result will be notified to you in writing at a later date.'),
      ], [
        PC(COMPLETE, '本日＿ もって、受付を 終了いたしました。', ['を', 'に', 'で'], 'を', ('〜を もって = à compter de.', '〜を もって = as of.'), ('Les inscriptions sont closes à compter d’aujourd’hui.', 'Registration closed as of today.')),
        FB(CHOOSE, '彼の 実力を ＿、この 試験は 簡単だろう。', ['もってすれば', 'もって', 'もとに'], 'もってすれば', ('Avec un atout : 〜をもってすれば.', 'With an asset: 〜をもってすれば.'), ('Avec son niveau, cet examen devrait être facile.', 'Given his ability, this exam should be easy.')),
        TF('田中は 今月を もって 退職する ことに なりました。', ('M. Tanaka commence un nouvel emploi ce mois-ci.', 'Mr Tanaka starts a new job this month.'), FAUX, ('今月を もって 退職 = il quitte son poste à la fin du mois.', '今月を もって 退職 = he leaves his post at the end of the month.')),
        SO(ORDER('Nous vous informerons par écrit.', 'We will inform you in writing.'), ['書面', 'を', 'もって', 'お知らせします'], ('Moyen + を もって, puis le verbe.', 'Means + を もって, then the verb.')),
      ]),
    L('n1-wo-kawakiri', ('À commencer par…, pour la dernière fois : 〜を皮切りに・〜を限りに', 'Starting with…, for the last time: 〜を皮切りに・〜を限りに'), ('Dire par où commence une série d’événements, et marquer le dernier jour de quelque chose.', 'Say where a series of events begins, and mark the last day of something.'), 10, [
        ('Nom + を皮切りに(して) = à commencer par, avec… comme point de départ (une série qui s’étend ensuite) : 東京を 皮切りに、全国で 公演する.', 'Noun + を皮切りに(して) = starting with, with… as the starting point (a series that then spreads): 東京を 皮切りに、全国で 公演する.'),
        ('Nom de date + を限りに = à partir de… on arrête ; … sera la dernière fois : 今日を 限りに、たばこを やめる.', 'Date noun + を限りに = from… on, no more; … will be the last time: 今日を 限りに、たばこを やめる.'),
        ('声を 限りに est une expression figée : crier à pleins poumons.', '声を 限りに is a set expression: to shout at the top of one’s voice.'),
      ], [
        G('gram-n1-wo-kawakiri-ni', '〜を皮切りに', '〜をかわきりに', '~wo kawakiri ni', ('à commencer par…', 'starting with…')),
        G('gram-n1-wo-kagiri-ni', '〜を限りに', '〜をかぎりに', '~wo kagiri ni', ('à partir de… plus jamais ; pour la dernière fois', 'from… on, no more ; for the last time')),
        V('vocab-kouen-show', '公演', 'こうえん', 'kouen', ('représentation (spectacle)', 'performance (show)')),
        V('vocab-kakuchi', '各地', 'かくち', 'kakuchi', ('différentes régions, partout', 'various places, everywhere')),
        V('vocab-intai', '引退', 'いんたい', 'intai', ('retrait (de la vie active, du sport)', 'retirement (from a career, a sport)')),
        V('vocab-kaimaku', '開幕', 'かいまく', 'kaimaku', ('lever de rideau, ouverture', 'curtain rise, opening')),
        K('kanji-n1-kawa', '皮', 'かわ', 'kawa', ('peau, écorce', 'skin, bark'), ['ヒ'], ['かわ'], 5),
        K('kanji-n1-maku', '幕', 'まく', 'maku', ('rideau, acte', 'curtain, act'), ['マク', 'バク'], [], 13),
      ], [
        ex('コンサートは 大阪を 皮切りに、各地で 行われます。', 'コンサートは おおさかを かわきりに、かくちで おこなわれます。', 'Le concert aura lieu dans tout le pays, à commencer par Osaka.', 'The concert will be held all over, starting with Osaka.'),
        ex('彼は 今シーズンを 限りに 引退すると 発表した。', 'かれは こんシーズンを かぎりに いんたいすると はっぴょうした。', 'Il a annoncé qu’il prendrait sa retraite à l’issue de cette saison.', 'He announced he would retire at the end of this season.'),
      ], [
        FB(CHOOSE, '京都での 公演を ＿、全国ツアーが 始まった。', ['皮切りに', '限りに', 'もって'], '皮切りに', ('Point de départ d’une série : 〜を皮切りに.', 'Starting point of a series: 〜を皮切りに.'), ('La tournée nationale a commencé par une représentation à Kyōto.', 'The national tour began with a performance in Kyoto.')),
        FB(CHOOSE, '今日を ＿、お酒を やめます。', ['限りに', '皮切りに', 'もってすれば'], '限りに', ('Dernière fois : 〜を限りに.', 'The last time: 〜を限りに.'), ('À partir d’aujourd’hui, j’arrête l’alcool.', 'As of today, I am giving up alcohol.')),
        TF('彼女は 声を 限りに 叫んだ。', ('Elle a chuchoté.', 'She whispered.'), FAUX, ('声を 限りに = à pleins poumons.', '声を 限りに = at the top of her voice.')),
        PC(COMPLETE, '開幕戦＿ 皮切りに、多くの 試合が 行われる。', ['を', 'に', 'が'], 'を', ('〜を 皮切りに.', '〜を 皮切りに.'), ('À commencer par le match d’ouverture, de nombreux matchs auront lieu.', 'Starting with the opening match, many games will be held.')),
      ]),
    L('n1-ga-hayaika', ('À peine… que déjà… : 〜が早いか・〜や否や', 'No sooner… than…: 〜が早いか・〜や否や'), ('Raconter, dans un style écrit, qu’une action suit immédiatement une autre.', 'Tell, in a written style, that one action immediately follows another.'), 10, [
        ('Verbe au dictionnaire + が早いか = à peine… que (quasi simultané, souvent un geste vif) : ベルが 鳴るが 早いか、生徒は 教室を 飛び出した.', 'Dictionary-form verb + が早いか = no sooner… than (almost simultaneous, often a quick move): ベルが 鳴るが 早いか、生徒は 教室を 飛び出した.'),
        ('Verbe au dictionnaire + や否や / や = dès que, au moment même où (très écrit) : 彼は 家に 着くや否や、眠って しまった.', 'Dictionary-form verb + や否や / や = as soon as, the very moment (very written): 彼は 家に 着くや否や、眠って しまった.'),
        ('Ces formes racontent des faits passés constatés ; on ne les emploie ni pour soi-même au futur, ni avec un ordre.', 'These forms narrate observed past facts; they are not used for oneself in the future, nor with an order.'),
      ], [
        G('gram-n1-ga-hayai-ka', '〜が早いか', '〜がはやいか', '~ga hayai ka', ('à peine… que déjà…', 'no sooner… than…')),
        G('gram-n1-ya-ina-ya', '〜や否や', '〜やいなや', '~ya ina ya', ('dès que…, au moment même où… (écrit)', 'as soon as…, the very moment… (written)')),
        V('vocab-kaisatsu', '改札', 'かいさつ', 'kaisatsu', ('portillon (de gare)', 'ticket gate')),
        V('vocab-aizu', '合図', 'あいず', 'aizu', ('signal, signe convenu', 'signal, sign')),
        V('vocab-kansei', '歓声', 'かんせい', 'kansei', ('cris de joie, acclamations', 'cheers, shouts of joy')),
        V('vocab-issei-ni', '一斉に', 'いっせいに', 'issei ni', ('tous en même temps', 'all at once, in unison')),
        K('kanji-n1-hitoshii', '斉', 'せい', 'sei', ('égal, ensemble', 'equal, together'), ['セイ'], [], 8),
        K('kanji-n1-fuda', '札', 'ふだ', 'fuda', ('billet, étiquette', 'bill, tag'), ['サツ'], ['ふだ'], 5),
      ], [
        ex('合図が 鳴るが 早いか、選手たちは 一斉に 走り出した。', 'あいずが なるが はやいか、せんしゅたちは いっせいに はしりだした。', 'À peine le signal avait-il retenti que les athlètes s’élancèrent tous ensemble.', 'No sooner had the signal sounded than the athletes all broke into a run.'),
        ex('歌手が 登場するや否や、会場から 歓声が 上がった。', 'かしゅが とうじょうするや いなや、かいじょうから かんせいが あがった。', 'Dès que la chanteuse est apparue, la salle a explosé de joie.', 'The moment the singer appeared, cheers rose from the hall.'),
      ], [
        FB(CHOOSE, '電車の ドアが 開く＿、彼は 改札へ 走った。', ['が早いか', 'を皮切りに', 'をもって'], 'が早いか', ('Quasi simultané : 〜が早いか.', 'Almost simultaneous: 〜が早いか.'), ('À peine les portes du train ouvertes, il a couru vers les portillons.', 'No sooner had the train doors opened than he ran to the ticket gates.')),
        FB(CHOOSE, '母の 顔を 見る＿、子どもは 泣き出した。', ['や否や', 'を限りに', 'をもって'], 'や否や', ('Dès que (écrit) : 〜や否や.', 'As soon as (written): 〜や否や.'), ('Dès qu’il a vu le visage de sa mère, l’enfant s’est mis à pleurer.', 'As soon as he saw his mother’s face, the child burst into tears.')),
        TF('仕事が 終わるや否や、帰る つもりです。', ('Cette phrase est naturelle en japonais.', 'This sentence is natural Japanese.'), FAUX, ('〜や否や ne s’emploie pas avec une intention (つもり).', '〜や否や is not used with an intention (つもり).')),
        SO(ORDER('À peine assis, il s’est endormi.', 'No sooner had he sat down than he fell asleep.'), ['座る', 'が早いか', '彼は', '眠って しまった'], ('Verbe au dictionnaire + が早いか.', 'Dictionary-form verb + が早いか.')),
      ]),
  ])])

# ═════════════════════════ Île 2 : jusqu'aux extrêmes ═════════════════════════
W2 = WORLD('n1-w2', ('Jusqu’aux extrêmes', 'To the extremes'), REGION,
  ('Insister sur un cas extrême : même pas, pas un seul, et ce n’est qu’à ce stade que…', 'Stress an extreme case: not even, not a single one, and only at this point did…'),
  (('L’Ōnyūdō Démesuré', 'The Boundless Ōnyūdō'), '巨', ('Ce moine géant grandit à chaque fois qu’on le regarde avec crainte. Pour le réduire, il faut parler des extrêmes sans trembler : même pas un instant, pas un seul mot.', 'This giant monk grows each time someone looks at him in fear. To shrink him, you must speak of extremes without flinching: not even for a moment, not a single word.')),
  [CH('n1-w2-c1', ('Même, pas un seul, seul… peut', 'Even, not a single, only… can'), [
    L('n1-sura', ('Même pas… : 〜すら・〜だに', 'Not even…: 〜すら・〜だに'), ('Insister sur un exemple extrême pour montrer à quel point une situation est poussée.', 'Highlight an extreme example to show how far a situation goes.'), 10, [
        ('Nom (+ particule) + すら = même (souvent dans une phrase négative) : 名前すら 知らない. C’est un さえ plus écrit.', 'Noun (+ particle) + すら = even (often in a negative sentence): 名前すら 知らない. It is a more written さえ.'),
        ('Nom / verbe au dictionnaire + だに = ne serait-ce que (très écrit, avec peu de mots) : 想像するだに 恐ろしい ; 夢にだに 思わなかった.', 'Noun / dictionary-form verb + だに = even just to (very written, with few words): 想像するだに 恐ろしい ; 夢にだに 思わなかった.'),
        ('微動だに しない est une expression figée : ne pas bouger d’un pouce.', '微動だに しない is a set phrase: not to budge an inch.'),
      ], [
        G('gram-n1-sura', '〜すら', '〜すら', '~sura', ('même… (écrit)', 'even… (written)')),
        G('gram-n1-dani', '〜だに', '〜だに', '~dani', ('ne serait-ce que…, rien qu’à…', 'even just…, merely…')),
        V('vocab-kyoufu', '恐怖', 'きょうふ', 'kyoufu', ('terreur, peur intense', 'terror, dread')),
        V('vocab-bidou', '微動', 'びどう', 'bidou', ('léger mouvement', 'slight movement')),
        V('vocab-hitokoto', '一言', 'ひとこと', 'hitokoto', ('un seul mot, un petit mot', 'a single word, a brief remark')),
        V('vocab-ue', '飢え', 'うえ', 'ue', ('faim (famine)', 'hunger, starvation')),
        K('kanji-n1-osoreru', '恐', 'おそれる', 'osoreru', ('craindre', 'fear, dread'), ['キョウ'], ['おそ(れる)', 'おそ(ろしい)'], 10),
        K('kanji-n1-bi', '微', 'び', 'bi', ('infime, subtil', 'minute, subtle'), ['ビ'], [], 13),
      ], [
        ex('忙しくて、食事を する 時間すら ありません。', 'いそがしくて、しょくじを する じかんすら ありません。', 'Je suis si occupé que je n’ai même pas le temps de manger.', 'I am so busy that I do not even have time to eat.'),
        ex('地震の 恐怖は 思い出すだに 体が 震える。', 'じしんの きょうふは おもいだすだに からだが ふるえる。', 'Rien qu’en repensant à la terreur du séisme, je tremble.', 'Merely recalling the terror of the earthquake makes me shake.'),
      ], [
        FB(CHOOSE, 'あの 人は 自分の 国の 首都＿ 知らない。', ['すら', 'だに', 'たりとも'], 'すら', ('Même pas (nom) : 〜すら.', 'Not even (noun): 〜すら.'), ('Cette personne ne connaît même pas la capitale de son propre pays.', 'That person does not even know the capital of his own country.')),
        FB(CHOOSE, '兵士は 微動＿ しなかった。', ['だに', 'すら', 'さえも'], 'だに', ('Expression figée : 微動だに しない.', 'Set phrase: 微動だに しない.'), ('Le soldat n’a pas bougé d’un pouce.', 'The soldier did not move an inch.')),
        TF('優勝するとは 夢にだに 思わなかった。', ('La personne s’attendait à gagner.', 'The speaker expected to win.'), FAUX, ('夢にだに 思わなかった = je n’en avais même pas rêvé.', '夢にだに 思わなかった = I never even dreamt of it.')),
        SO(ORDER('Il n’a même pas dit un mot.', 'He did not even say a word.'), ['彼は', '一言', 'すら', '言わなかった'], ('Nom + すら + négation.', 'Noun + すら + negative.')),
      ]),
    L('n1-taritomo', ('Pas un seul… : 〜たりとも・誰一人として', 'Not a single…: 〜たりとも・誰一人として'), ('Nier avec force en partant de la plus petite quantité possible.', 'Deny forcefully starting from the smallest possible amount.'), 10, [
        ('一 + compteur + たりとも + négation = pas même un seul : 一円たりとも 無駄に できない ; 一瞬たりとも 気を 抜くな.', '一 + counter + たりとも + negative = not even one: 一円たりとも 無駄に できない ; 一瞬たりとも 気を 抜くな.'),
        ('Interrogatif + 一 + compteur + として + négation = pas un seul : 誰一人として 来なかった ; 何一つとして 分からない.', 'Question word + 一 + counter + として + negative = not a single one: 誰一人として 来なかった ; 何一つとして 分からない.'),
        ('Ces formes conviennent aux déclarations fermes, aux règles et aux ordres.', 'These forms suit firm statements, rules and orders.'),
      ], [
        G('gram-n1-taritomo', '〜たりとも', '〜たりとも', '~taritomo', ('pas même un(e) seul(e)…', 'not even a single…')),
        G('gram-n1-hitori-to-shite', '誰一人として〜ない', 'だれひとりとして〜ない', 'dare hitori to shite ~nai', ('personne, pas une seule personne', 'not a single person')),
        V('vocab-isshun', '一瞬', 'いっしゅん', 'isshun', ('un instant', 'an instant')),
        V('vocab-reigai', '例外', 'れいがい', 'reigai', ('exception', 'exception')),
        V('vocab-minogashimasu', '見逃します', 'みのがします', 'minogashimasu', ('laisser passer, ne pas voir', 'to overlook, to let slip')),
        V('vocab-rouhi', '浪費', 'ろうひ', 'rouhi', ('gaspillage', 'waste, squandering')),
        K('kanji-n1-rou', '浪', 'ろう', 'rou', ('vague ; errer', 'wave; wander'), ['ロウ'], [], 10),
        K('kanji-n1-nigeru', '逃', 'にげる', 'nigeru', ('fuir, s’échapper', 'flee, escape'), ['トウ'], ['に(げる)', 'のが(す)'], 9),
      ], [
        ex('試合中は 一瞬たりとも 油断できない。', 'しあいちゅうは いっしゅんたりとも ゆだんできない。', 'Pendant le match, on ne peut pas relâcher son attention une seule seconde.', 'During the match, you cannot let your guard down for a single moment.'),
        ex('その 質問に 答えられる 人は 誰一人として いなかった。', 'その しつもんに こたえられる ひとは だれひとりとして いなかった。', 'Personne, pas une seule personne, n’a su répondre à cette question.', 'Not a single person could answer that question.'),
      ], [
        FB(CHOOSE, '税金は 一円＿ 浪費しては いけない。', ['たりとも', 'すら', 'だに'], 'たりとも', ('一 + compteur + たりとも.', '一 + counter + たりとも.'), ('L’argent public ne doit pas être gaspillé, pas même d’un yen.', 'Tax money must not be wasted, not even a single yen.')),
        FB(CHOOSE, 'この 規則には 一つの ＿も 認めない。', ['例外', '一瞬', '浪費'], '例外', ('例外 = exception.', '例外 = exception.'), ('Ce règlement ne souffre aucune exception.', 'This rule admits no exception at all.')),
        TF('会議では 何一つとして 決まらなかった。', ('La réunion a pris plusieurs décisions.', 'The meeting made several decisions.'), FAUX, ('何一つとして〜ない = rien du tout.', '何一つとして〜ない = nothing at all.')),
        DC(('Ton chef te demande de surveiller une machine importante.', 'Your boss asks you to watch over an important machine.'), [('上司', 'この 数字から 目を 離さないで ください。')], ('Le chef te demande de ne pas quitter ces chiffres des yeux.', 'The boss asks you not to take your eyes off these figures.'), ['はい、一瞬たりとも 見逃しません。', 'はい、一瞬すら 見逃します。', 'はい、一瞬だに 見逃して ください。'], 'はい、一瞬たりとも 見逃しません。', ('Engagement ferme : 一瞬たりとも + négation.', 'A firm commitment: 一瞬たりとも + negative.')),
      ]),
    L('n1-ni-shite', ('Seul… pouvait…, propre à… : 〜にして・〜ならではの', 'Only… could…, unique to…: 〜にして・〜ならではの'), ('Dire qu’une chose n’est possible qu’à un certain niveau, ou qu’elle n’appartient qu’à un lieu ou à une personne.', 'Say that something is only possible at a certain level, or that it belongs to only one place or person.'), 10, [
        ('Nom + にして(初めて) = ce n’est qu’à… que : 四十歳に して 初めて 結婚した. Avec un maître : 名人に して 初めて できる 技.', 'Noun + にして(初めて) = only at… did: 四十歳に して 初めて 結婚した. With a master: 名人に して 初めて できる 技.'),
        ('Proverbe : この 親に して この 子 あり = tel père, tel fils.', 'Proverb: この 親に して この 子 あり = like father, like son.'),
        ('Nom + ならではの + nom = propre à, qu’on ne trouve que chez : 京都ならではの 景色 ; 職人ならではの 技.', 'Noun + ならではの + noun = unique to, found only in: 京都ならではの 景色 ; 職人ならではの 技.'),
      ], [
        G('gram-n1-ni-shite', '〜にして', '〜にして', '~ni shite', ('ce n’est qu’à… que ; seul… peut', 'only at… ; only… can')),
        G('gram-n1-naradewa-no', '〜ならではの', '〜ならではの', '~naradewa no', ('propre à…, typique de…', 'unique to…, only possible with…')),
        V('vocab-meijin', '名人', 'めいじん', 'meijin', ('maître, virtuose', 'master, expert')),
        V('vocab-shokunin', '職人', 'しょくにん', 'shokunin', ('artisan', 'craftsman, artisan')),
        V('vocab-waza', '技', 'わざ', 'waza', ('technique, savoir-faire', 'technique, skill')),
        V('vocab-kyouchi', '境地', 'きょうち', 'kyouchi', ('état d’esprit atteint, stade', 'state of mind, stage reached')),
        K('kanji-n1-takumi', '匠', 'たくみ', 'takumi', ('artisan habile', 'skilled artisan'), ['ショウ'], ['たくみ'], 6),
        K('kanji-n1-sakai', '境', 'さかい', 'sakai', ('frontière, limite', 'border, boundary'), ['キョウ', 'ケイ'], ['さかい'], 14),
      ], [
        ex('これは 名人に して 初めて できる 技です。', 'これは めいじんに して はじめて できる わざです。', 'Seul un maître est capable d’une telle technique.', 'Only a master can perform this technique.'),
        ex('この 祭りでは、地方ならではの 料理が 楽しめる。', 'この まつりでは、ちほうならではの りょうりが たのしめる。', 'Pendant cette fête, on peut goûter des plats propres à la région.', 'At this festival, you can enjoy dishes unique to the region.'),
      ], [
        FB(CHOOSE, '六十歳＿ 初めて、絵を 習い始めた。', ['にして', 'ならでは', 'たりとも'], 'にして', ('Ce n’est qu’à… que : 〜にして初めて.', 'Only at… did: 〜にして初めて.'), ('Ce n’est qu’à soixante ans qu’il a commencé à apprendre la peinture.', 'Only at sixty did he start learning to paint.')),
        FB(CHOOSE, 'これは 職人＿の 丁寧な 仕事だ。', ['ならでは', 'にして', 'すら'], 'ならでは', ('Propre à : 〜ならではの.', 'Unique to: 〜ならではの.'), ('C’est un travail soigné comme seul un artisan sait le faire.', 'This is careful work only a craftsman could do.')),
        TF('この 親に して この 子 あり。', ('Les parents et l’enfant se ressemblent.', 'Parents and child are alike.'), VRAI, ('Proverbe : tel père, tel fils.', 'Proverb: like father, like son.')),
        SO(ORDER('Un paysage qu’on ne voit qu’à Kyōto.', 'A view you only find in Kyoto.'), ['京都', 'ならではの', '景色'], ('Nom + ならではの + nom.', 'Noun + ならではの + noun.')),
      ]),
  ])])

# ═════════════════════════ Île 3 : contre vents et marées ═════════════════════════
W3 = WORLD('n1-w3', ('Contre vents et marées', 'Against all odds'), REGION,
  ('Agir sans se laisser arrêter, faire dépendre une décision d’un critère, et concéder un point tout en le dépassant.', 'Act without being stopped, make a decision depend on a criterion, and concede a point while going beyond it.'),
  (('Fūjin, Seigneur des Vents', 'Fūjin, Lord of the Winds'), '風', ('Le dieu du vent souffle sur la route de l’armée. Il ne laissera passer que celui qui avance malgré la tempête et qui sait dire ce qui dépend de quoi.', 'The wind god blows across the army’s road. He will let through only one who marches on despite the storm and can say what depends on what.')),
  [CH('n1-w3-c1', ('Sans se laisser arrêter', 'Undeterred'), [
    L('n1-wo-monotomosezu', ('Sans se laisser arrêter par… : 〜をものともせず・〜をよそに', 'Undeterred by…: 〜をものともせず・〜をよそに'), ('Dire qu’on agit en bravant un obstacle, ou en ignorant l’avis et l’inquiétude des autres.', 'Say that someone acts in defiance of an obstacle, or ignoring the opinions and worries of others.'), 10, [
        ('Nom + をものともせず(に) = sans se laisser arrêter par, au mépris de (souvent admiratif) : 嵐を ものともせず、船は 進んだ.', 'Noun + をものともせず(に) = undeterred by, in defiance of (often admiring): 嵐を ものともせず、船は 進んだ.'),
        ('Nom + をよそに = sans se soucier de, en ignorant (souvent l’inquiétude des proches, critique) : 親の 心配を よそに、彼は 一人で 旅に 出た.', 'Noun + をよそに = paying no heed to, ignoring (often loved ones’ worry, critical): 親の 心配を よそに、彼は 一人で 旅に 出た.'),
        ('On ne s’en sert pas pour parler de soi : c’est un regard extérieur sur l’action de quelqu’un.', 'They are not used about oneself: they are an outside view of someone’s action.'),
      ], [
        G('gram-n1-wo-monotomosezu', '〜をものともせず', '〜をものともせず', '~wo mono tomo sezu', ('sans se laisser arrêter par…', 'undeterred by…')),
        G('gram-n1-wo-yoso-ni', '〜をよそに', '〜をよそに', '~wo yoso ni', ('sans se soucier de…, en ignorant…', 'paying no heed to…, ignoring…')),
        V('vocab-arashi', '嵐', 'あらし', 'arashi', ('tempête', 'storm')),
        V('vocab-shuui', '周囲', 'しゅうい', 'shuui', ('entourage, alentours', 'surroundings, people around')),
        V('vocab-konnan', '困難', 'こんなん', 'konnan', ('difficulté', 'difficulty, hardship')),
        V('vocab-kyoukou', '強行', 'きょうこう', 'kyoukou', ('passage en force', 'forcing through')),
        K('kanji-n1-arashi', '嵐', 'あらし', 'arashi', ('tempête', 'storm'), ['ラン'], ['あらし'], 12),
        K('kanji-n1-kakomu', '囲', 'かこむ', 'kakomu', ('entourer', 'surround'), ['イ'], ['かこ(む)'], 7),
      ], [
        ex('彼女は 足の けがを ものともせず、最後まで 走り抜いた。', 'かのじょは あしの けがを ものともせず、さいごまで はしりぬいた。', 'Sans se laisser arrêter par sa blessure à la jambe, elle a couru jusqu’au bout.', 'Undeterred by her leg injury, she ran right to the end.'),
        ex('住民の 反対を よそに、工事は 強行された。', 'じゅうみんの はんたいを よそに、こうじは きょうこうされた。', 'Sans tenir compte de l’opposition des habitants, les travaux ont été menés de force.', 'Ignoring the residents’ opposition, the construction was forced through.'),
      ], [
        FB(CHOOSE, '彼は 数々の 困難を ＿、夢を 実現した。', ['ものともせず', 'よそに', '皮切りに'], 'ものともせず', ('Braver un obstacle (admiratif) : 〜をものともせず.', 'Defying an obstacle (admiring): 〜をものともせず.'), ('Sans se laisser arrêter par mille difficultés, il a réalisé son rêve.', 'Undeterred by countless difficulties, he made his dream come true.')),
        FB(CHOOSE, '周囲の 心配を ＿、彼は 会社を 辞めた。', ['よそに', 'ものともせず', '限りに'], 'よそに', ('Ignorer l’inquiétude des autres : 〜をよそに.', 'Ignoring others’ worry: 〜をよそに.'), ('Sans se soucier de l’inquiétude de son entourage, il a quitté son entreprise.', 'Paying no heed to the worries of those around him, he quit his company.')),
        TF('船は 嵐を ものともせず、港を 出た。', ('Le bateau est resté au port à cause de la tempête.', 'The ship stayed in port because of the storm.'), FAUX, ('〜をものともせず : il est parti malgré la tempête.', '〜をものともせず: it left despite the storm.')),
        SO(ORDER('Sans se soucier des inquiétudes de ses parents, il est parti seul.', 'Ignoring his parents’ worries, he left alone.'), ['親の 心配', 'を よそに', '彼は', '一人で 出かけた'], ('Nom + を よそに, puis l’action.', 'Noun + を よそに, then the action.')),
      ]),
    L('n1-ikan', ('Selon…, quel que soit… : 〜いかんで・〜いかんによらず', 'Depending on…, regardless of…: 〜いかんで・〜いかんによらず'), ('Faire dépendre une décision d’un critère, ou dire qu’elle n’en dépend pas, dans le style des règlements.', 'Make a decision depend on a criterion, or say it does not, in the style of regulations.'), 10, [
        ('Nom (+ の) + いかんで / いかんでは / いかんによって = selon, en fonction de : 結果いかんでは、計画を 中止する.', 'Noun (+ の) + いかんで / いかんでは / いかんによって = depending on: 結果いかんでは、計画を 中止する.'),
        ('Nom (+ の) + いかんによらず / いかんにかかわらず / いかんを問わず = quel que soit : 理由の いかんを 問わず、返金は できません.', 'Noun (+ の) + いかんによらず / いかんにかかわらず / いかんを問わず = regardless of: 理由の いかんを 問わず、返金は できません.'),
        ('C’est le style des contrats et des avis officiels ; à l’oral, on dirait 〜次第 ou 〜に関係なく.', 'It is the style of contracts and official notices; in speech you would say 〜次第 or 〜に関係なく.'),
      ], [
        G('gram-n1-ikan-de', '〜いかんで（は）', '〜いかんで（は）', '~ikan de (wa)', ('selon…, en fonction de… (soutenu)', 'depending on… (formal)')),
        G('gram-n1-ikan-ni-yorazu', '〜いかんによらず', '〜いかんによらず', '~ikan ni yorazu', ('quel que soit…', 'regardless of…')),
        V('vocab-seihi', '成否', 'せいひ', 'seihi', ('succès ou échec, issue', 'success or failure, outcome')),
        V('vocab-kokuseki', '国籍', 'こくせき', 'kokuseki', ('nationalité', 'nationality')),
        V('vocab-henkin', '返金', 'へんきん', 'henkin', ('remboursement', 'refund')),
        V('vocab-taiou', '対応', 'たいおう', 'taiou', ('réponse apportée, prise en charge', 'response, handling')),
        K('kanji-n1-seki', '籍', 'せき', 'seki', ('registre, inscription', 'register, enrolment'), ['セキ'], [], 20),
        K('kanji-n1-ou', '応', 'おう', 'ou', ('répondre, s’adapter', 'respond, adapt'), ['オウ'], [], 7),
      ], [
        ex('交渉の 成否は、今後の 対応いかんで 決まる。', 'こうしょうの せいひは、こんごの たいおういかんで きまる。', 'L’issue des négociations dépendra de la manière dont nous réagirons désormais.', 'The outcome of the negotiations depends on how we respond from now on.'),
        ex('国籍の いかんを 問わず、誰でも 参加できます。', 'こくせきの いかんを とわず、だれでも さんかできます。', 'Tout le monde peut participer, quelle que soit sa nationalité.', 'Anyone can take part, regardless of nationality.'),
      ], [
        FB(CHOOSE, '試験の 結果＿では、卒業できない ことも ある。', ['いかん', 'よそ', 'すら'], 'いかん', ('Selon : 〜いかんでは.', 'Depending on: 〜いかんでは.'), ('Selon les résultats de l’examen, il se peut qu’on ne puisse pas obtenir son diplôme.', 'Depending on the exam results, you may not be able to graduate.')),
        FB(CHOOSE, '理由の いかんに ＿、一度 払った お金は 返金しません。', ['よらず', 'よって', 'つれて'], 'よらず', ('Quel que soit : 〜いかんによらず.', 'Regardless of: 〜いかんによらず.'), ('Quelle qu’en soit la raison, nous ne remboursons pas les sommes versées.', 'Whatever the reason, money once paid will not be refunded.')),
        TF('天候いかんでは、大会は 中止に なります。', ('Le tournoi aura lieu quoi qu’il arrive.', 'The tournament will go ahead no matter what.'), FAUX, ('〜いかんでは : selon la météo, il peut être annulé.', '〜いかんでは: depending on the weather, it may be cancelled.')),
        PC(COMPLETE, '年齢＿ いかんを 問わず、応募できます。', ['の', 'を', 'に'], 'の', ('Nom + の + いかんを 問わず.', 'Noun + の + いかんを 問わず.'), ('On peut postuler quel que soit son âge.', 'You can apply regardless of age.')),
      ]),
    L('n1-to-wa-ie', ('Certes…, même… : 〜とはいえ・〜といえども', 'Admittedly…, even…: 〜とはいえ・〜といえども'), ('Concéder un fait tout en montrant qu’il ne suffit pas, ou que même le cas le plus fort n’échappe pas à la règle.', 'Concede a fact while showing that it is not enough, or that even the strongest case is subject to the rule.'), 10, [
        ('Forme neutre / nom + とはいえ = certes…, mais ; bien que (on admet, puis on nuance) : 春とは いえ、まだ 寒い.', 'Plain form / noun + とはいえ = admittedly…, but; although (you grant, then qualify): 春とは いえ、まだ 寒い.'),
        ('Nom + といえども = même (un cas qu’on croirait à part) : 子どもと いえども、法律は 守らなければ ならない.', 'Noun + といえども = even (a case you might think exempt): 子どもと いえども、法律は 守らなければ ならない.'),
        ('Souvent avec いかなる ou たとえ : いかなる 天才と いえども、努力なしには 成功しない.', 'Often with いかなる or たとえ: いかなる 天才と いえども、努力なしには 成功しない.'),
      ], [
        G('gram-n1-to-wa-ie', '〜とはいえ', '〜とはいえ', '~to wa ie', ('certes…, bien que…', 'admittedly…, although…')),
        G('gram-n1-to-iedomo', '〜といえども', '〜といえども', '~to iedomo', ('même… (cas extrême)', 'even… (an extreme case)')),
        V('vocab-tensai', '天才', 'てんさい', 'tensai', ('génie', 'genius')),
        V('vocab-houritsu', '法律', 'ほうりつ', 'houritsu', ('loi', 'law')),
        V('vocab-ihan', '違反', 'いはん', 'ihan', ('infraction, violation', 'violation, breach')),
        V('vocab-risshun', '立春', 'りっしゅん', 'risshun', ('début du printemps (calendrier)', 'first day of spring (calendar)')),
        K('kanji-n1-ritsu', '律', 'りつ', 'ritsu', ('loi, règle', 'law, rule'), ['リツ', 'リチ'], [], 9),
        K('kanji-n1-sai', '才', 'さい', 'sai', ('talent ; âge (ans)', 'talent; years of age'), ['サイ'], [], 3),
      ], [
        ex('立春とは いえ、まだ 雪が 降って いる。', 'りっしゅんとは いえ、まだ ゆきが ふって いる。', 'Certes, le printemps a officiellement commencé, mais il neige encore.', 'It may officially be spring, but it is still snowing.'),
        ex('大臣と いえども、法律に 違反すれば 罰せられる。', 'だいじんと いえども、ほうりつに いはんすれば ばっせられる。', 'Même un ministre est puni s’il enfreint la loi.', 'Even a minister is punished if he breaks the law.'),
      ], [
        FB(CHOOSE, '安い ＿、この 値段では 買えない。', ['とはいえ', 'といえども', 'いかんで'], 'とはいえ', ('Concession : 〜とはいえ.', 'Concession: 〜とはいえ.'), ('C’est certes bon marché, mais je ne peux pas l’acheter à ce prix.', 'It may be cheap, but I cannot buy it at this price.')),
        FB(CHOOSE, 'いかなる 天才と ＿、努力なしでは 成功できない。', ['いえども', 'はいえ', 'して'], 'いえども', ('Même le cas extrême : いかなる〜といえども.', 'Even the extreme case: いかなる〜といえども.'), ('Aucun génie, quel qu’il soit, ne réussit sans effort.', 'No genius whatsoever can succeed without effort.')),
        TF('子どもと いえども、ルールは 守るべきだ。', ('Les enfants sont dispensés de respecter les règles.', 'Children are exempt from following the rules.'), FAUX, ('〜といえども : même les enfants doivent les respecter.', '〜といえども: even children must follow them.')),
        DC(('Un ami te dit que tu as de la chance d’avoir un week-end de trois jours.', 'A friend says you are lucky to have a three-day weekend.'), [('友だち', '三連休で いいね。')], ('Ton ami dit que c’est bien d’avoir trois jours de congé.', 'Your friend says it is nice to have three days off.'), ['休みとは いえ、仕事の 準備で 忙しいんだ。', '休みと いえども、とても 楽しみだ。', '休みを ものともせず、うれしい。'], '休みとは いえ、仕事の 準備で 忙しいんだ。', ('On admet, puis on nuance : 〜とはいえ.', 'Grant, then qualify: 〜とはいえ.')),
      ]),
  ])])

# ═════════════════════════ Île 4 : le tribunal ═════════════════════════
W4 = WORLD('n1-w4', ('Juger et s’indigner', 'Judging and protesting'), REGION,
  ('Dire ce qui est indigne d’un rôle, ce qui mérite ou non l’attention, et une émotion qu’on ne peut retenir.', 'Say what is unworthy of a role, what does or does not deserve attention, and an emotion that cannot be held back.'),
  (('Enma, Juge des Enfers', 'Enma, Judge of the Underworld'), '閻', ('Le roi des enfers siège au tribunal du shōgun. Avant de rendre un verdict, il exige que chacun sache dire ce qui est indigne, ce qui mérite confiance, et ce qu’on ne peut s’empêcher de ressentir.', 'The king of the underworld sits in the shōgun’s court. Before passing judgement, he demands that everyone can say what is unworthy, what deserves trust, and what one cannot help feeling.')),
  [CH('n1-w4-c1', ('Indigne, digne, irrépressible', 'Unworthy, worthy, irrepressible'), [
    L('n1-majiki', ('Indigne de…, interdit de… : 〜まじき・〜べからず', 'Unworthy of…, must not…: 〜まじき・〜べからず'), ('Condamner un acte contraire à ce qu’on attend d’un rôle, et lire les interdictions écrites.', 'Condemn an act contrary to what is expected of a role, and read written prohibitions.'), 10, [
        ('Nom de rôle + に + ある + まじき + nom = indigne de, qu’un… ne devrait jamais commettre : 教師に ある まじき 行為.', 'Role noun + に + ある + まじき + noun = unworthy of, that a… should never commit: 教師に ある まじき 行為.'),
        ('Verbe au dictionnaire + べからず = interdit de (panneaux, maximes) : 立ち入る べからず ; 芝生に 入る べからず. する → す べからず.', 'Dictionary-form verb + べからず = must not (signs, maxims): 立ち入る べからず ; 芝生に 入る べからず. する → す べからず.'),
        ('Verbe + べからざる + nom = qu’on ne doit pas… ; indispensable : 欠く べからざる 存在 (une présence indispensable).', 'Verb + べからざる + noun = that must not be…; indispensable: 欠く べからざる 存在 (an indispensable presence).'),
      ], [
        G('gram-n1-majiki', '〜まじき', '〜まじき', '~majiki', ('indigne de…, inadmissible pour…', 'unworthy of…, unacceptable for…')),
        G('gram-n1-bekarazu', '〜べからず', '〜べからず', '~bekarazu', ('interdit de… (écrit)', 'must not… (written)')),
        V('vocab-koui', '行為', 'こうい', 'koui', ('acte, agissement', 'act, deed')),
        V('vocab-kyoushi', '教師', 'きょうし', 'kyoushi', ('enseignant (métier)', 'teacher (profession)')),
        V('vocab-hatsugen', '発言', 'はつげん', 'hatsugen', ('déclaration, propos', 'statement, remark')),
        V('vocab-shobatsu', '処罰', 'しょばつ', 'shobatsu', ('sanction, punition', 'punishment, penalty')),
        K('kanji-n1-tame', '為', 'ため', 'tame', ('faire, agir', 'do, act'), ['イ'], ['ため'], 9),
        K('kanji-n1-batsu', '罰', 'ばつ', 'batsu', ('punition', 'punishment'), ['バツ', 'バチ'], [], 14),
      ], [
        ex('生徒を 傷つける ことは、教師に ある まじき 行為だ。', 'せいとを きずつける ことは、きょうしに ある まじき こういだ。', 'Blesser un élève est un acte indigne d’un enseignant.', 'Hurting a pupil is conduct unworthy of a teacher.'),
        ex('門には「関係者以外 入る べからず」と 書いて あった。', 'もんには「かんけいしゃいがい はいる べからず」と かいて あった。', 'Sur le portail était écrit : « Entrée interdite aux personnes non autorisées ».', 'On the gate was written: “No entry except for authorised persons.”'),
      ], [
        FB(CHOOSE, '大臣に ある ＿ 発言で、大きな 問題に なった。', ['まじき', 'べからず', 'ならでは'], 'まじき', ('Indigne d’un rôle : 〜にあるまじき + nom.', 'Unworthy of a role: 〜にあるまじき + noun.'), ('Ces propos indignes d’un ministre ont causé un grand scandale.', 'The remark, unworthy of a minister, became a big issue.')),
        FB(CHOOSE, 'ここで たばこを 吸う ＿。', ['べからず', 'まじき', 'たりとも'], 'べからず', ('Interdiction écrite : 〜べからず.', 'Written prohibition: 〜べからず.'), ('Interdiction de fumer ici.', 'No smoking here.')),
        TF('この 規則は 我が社に 欠く べからざる ものだ。', ('Ce règlement est inutile à l’entreprise.', 'This rule is useless to the company.'), FAUX, ('欠く べからざる = indispensable.', '欠く べからざる = indispensable.')),
        SO(ORDER('Un acte indigne d’un policier.', 'Conduct unworthy of a police officer.'), ['警察官', 'に ある', 'まじき', '行為'], ('Rôle + に ある まじき + nom.', 'Role + に ある まじき + noun.')),
      ]),
    L('n1-ni-taenai', ('Insupportable…, digne de… : 〜に堪えない・〜に足る', 'Unbearable…, worthy of…: 〜に堪えない・〜に足る'), ('Juger qu’une chose ne mérite pas qu’on la regarde, ou qu’elle mérite la confiance.', 'Judge that something is not worth looking at, or that it deserves trust.'), 10, [
        ('Verbe au dictionnaire + に堪えない = insupportable à…, qu’on ne peut pas… tant c’est mauvais : 見るに 堪えない 惨状 ; 聞くに 堪えない 悪口.', 'Dictionary-form verb + に堪えない = unbearable to…, too bad to…: 見るに 堪えない 惨状 ; 聞くに 堪えない 悪口.'),
        ('Nom d’émotion + に堪えない = ne pas pouvoir contenir (remerciements formels) : 感謝に 堪えません.', 'Emotion noun + に堪えない = to be overcome with (formal thanks): 感謝に 堪えません.'),
        ('Verbe au dictionnaire / nom + に足る = digne de, qui mérite : 信頼するに 足る 人物 ; 取るに 足りない (insignifiant).', 'Dictionary-form verb / noun + に足る = worthy of, deserving: 信頼するに 足る 人物 ; 取るに 足りない (insignificant).'),
      ], [
        G('gram-n1-ni-taenai', '〜に堪えない', '〜にたえない', '~ni taenai', ('insupportable à… ; ne pas pouvoir contenir…', 'unbearable to… ; overcome with…')),
        G('gram-n1-ni-taru', '〜に足る', '〜にたる', '~ni taru', ('digne de…, qui mérite…', 'worthy of…, deserving…')),
        V('vocab-shinrai', '信頼', 'しんらい', 'shinrai', ('confiance', 'trust')),
        V('vocab-sanjou', '惨状', 'さんじょう', 'sanjou', ('scène désastreuse', 'disastrous scene')),
        V('vocab-jinbutsu', '人物', 'じんぶつ', 'jinbutsu', ('personnage, personne (de valeur)', 'person, figure')),
        V('vocab-hihan', '批判', 'ひはん', 'hihan', ('critique (reproche)', 'criticism')),
        K('kanji-n1-taeru', '堪', 'たえる', 'taeru', ('supporter, endurer', 'endure, bear'), ['カン'], ['た(える)'], 12),
        K('kanji-n1-san', '惨', 'さん', 'san', ('misérable, cruel', 'miserable, cruel'), ['サン', 'ザン'], ['みじ(め)'], 11),
      ], [
        ex('事故現場は 見るに 堪えない 惨状だった。', 'じこげんばは みるに たえない さんじょうだった。', 'Le lieu de l’accident offrait un spectacle insoutenable.', 'The accident scene was a sight too terrible to look at.'),
        ex('彼は 信頼するに 足る 人物だ。', 'かれは しんらいするに たる じんぶつだ。', 'C’est une personne digne de confiance.', 'He is a person worthy of trust.'),
      ], [
        FB(CHOOSE, 'あの 批判は 聞くに ＿ ものだった。', ['堪えない', '足る', 'まじき'], '堪えない', ('Insupportable à entendre : 聞くに 堪えない.', 'Unbearable to hear: 聞くに 堪えない.'), ('Ces critiques étaient insupportables à entendre.', 'That criticism was unbearable to listen to.')),
        FB(CHOOSE, 'それは 取るに ＿ ことだから、気に しないで。', ['足りない', '堪えない', '足る'], '足りない', ('取るに 足りない = insignifiant.', '取るに 足りない = trivial.'), ('C’est insignifiant, ne t’en fais pas.', 'It is a trivial matter, so do not worry.')),
        TF('皆様の ご協力に、感謝に 堪えません。', ('La personne remercie chaleureusement.', 'The speaker is expressing heartfelt thanks.'), VRAI, ('感謝に 堪えない = être infiniment reconnaissant.', '感謝に 堪えない = to be deeply grateful.')),
        SO(ORDER('Une personne digne de confiance.', 'A person worthy of trust.'), ['信頼する', 'に 足る', '人物'], ('Verbe + に 足る + nom.', 'Verb + に 足る + noun.')),
      ]),
    L('n1-wo-kinjienai', ('Ne pas pouvoir retenir… : 〜を禁じ得ない・〜てやまない', 'Cannot hold back…: 〜を禁じ得ない・〜てやまない'), ('Exprimer avec solennité une émotion ou un souhait qu’on ne peut contenir.', 'Solemnly express an emotion or a wish one cannot contain.'), 10, [
        ('Nom d’émotion + を禁じ得ない = ne pas pouvoir s’empêcher de ressentir : 同情を 禁じ得ない ; 怒りを 禁じ得ない. C’est le style des éditoriaux et des discours.', 'Emotion noun + を禁じ得ない = cannot help feeling: 同情を 禁じ得ない ; 怒りを 禁じ得ない. It is the style of editorials and speeches.'),
        ('Verbe en て + やまない = ne cesser de (souhaiter, espérer, aimer) : 皆様の 幸福を 願って やみません.', 'て-form verb + やまない = never cease to (wish, hope, love): 皆様の 幸福を 願って やみません.'),
        ('〜てやまない s’emploie pour ses propres sentiments durables ; on le trouve souvent en fin de discours ou de lettre.', '〜てやまない is used for one’s own lasting feelings; it often comes at the end of a speech or letter.'),
      ], [
        G('gram-n1-wo-kinjienai', '〜を禁じ得ない', '〜をきんじえない', '~wo kinjienai', ('ne pas pouvoir retenir… (émotion)', 'cannot help feeling…')),
        G('gram-n1-te-yamanai', '〜てやまない', '〜てやまない', '~te yamanai', ('ne cesser de… (souhait, sentiment)', 'never cease to… (wish, feeling)')),
        V('vocab-doujou', '同情', 'どうじょう', 'doujou', ('compassion', 'sympathy, compassion')),
        V('vocab-ikari', '怒り', 'いかり', 'ikari', ('colère', 'anger')),
        V('vocab-giseisha', '犠牲者', 'ぎせいしゃ', 'giseisha', ('victime', 'victim, casualty')),
        V('vocab-koufuku', '幸福', 'こうふく', 'koufuku', ('bonheur, prospérité', 'happiness, well-being')),
        K('kanji-n1-gi', '犠', 'ぎ', 'gi', ('sacrifice (animal offert)', 'sacrifice (offering)'), ['ギ'], [], 17),
        K('kanji-n1-sei', '牲', 'せい', 'sei', ('victime offerte', 'sacrificial victim'), ['セイ'], [], 9),
      ], [
        ex('事故の 犠牲者の ことを 思うと、同情を 禁じ得ない。', 'じこの ぎせいしゃの ことを おもうと、どうじょうを きんじえない。', 'Quand je pense aux victimes de l’accident, je ne peux retenir ma compassion.', 'When I think of the accident victims, I cannot help feeling sympathy.'),
        ex('卒業生の 皆さんの 幸福を 願って やみません。', 'そつぎょうせいの みなさんの こうふくを ねがって やみません。', 'Je ne cesse de souhaiter le bonheur de chacun de vous, jeunes diplômés.', 'I wish every happiness to all of you graduates, now and always.'),
      ], [
        FB(CHOOSE, '不公平な 判決に 怒りを ＿。', ['禁じ得ない', 'やまない', '堪えない'], '禁じ得ない', ('Émotion irrépressible : 〜を禁じ得ない.', 'Irrepressible emotion: 〜を禁じ得ない.'), ('Je ne peux contenir ma colère devant ce jugement injuste.', 'I cannot hold back my anger at this unfair ruling.')),
        FB(CHOOSE, '平和が 続く ことを 願って ＿。', ['やみません', '禁じ得ません', '足りません'], 'やみません', ('Souhait durable : 〜てやまない.', 'A lasting wish: 〜てやまない.'), ('Je ne cesse d’espérer que la paix se maintienne.', 'I earnestly hope that peace will last.')),
        TF('その 知らせに、驚きを 禁じ得なかった。', ('La nouvelle n’a pas du tout surpris.', 'The news was not surprising at all.'), FAUX, ('驚きを 禁じ得ない = ne pas pouvoir cacher sa surprise.', '驚きを 禁じ得ない = cannot help being surprised.')),
        PC(COMPLETE, '被害者に 同情＿ 禁じ得ない。', ['を', 'に', 'が'], 'を', ('〜を 禁じ得ない.', '〜を 禁じ得ない.'), ('Je ne peux retenir ma compassion pour les victimes.', 'I cannot help feeling sympathy for the victims.')),
      ]),
  ])])

# ═════════════════════════ Île 5 : presque, à peine besoin ═════════════════════════
W5 = WORLD('n1-w5', ('Presque, inutile de dire', 'Almost, needless to say'), REGION,
  ('Décrire un geste qui semble sur le point d’arriver, dire ce qui va sans dire, et comparer à un degré supérieur.', 'Describe a gesture that seems about to happen, say what goes without saying, and compare to a higher degree.'),
  (('Le Kodama Retentissant', 'The Resounding Kodama'), '響', ('Dans la forêt de l’ouest, l’esprit des arbres répète chaque parole en l’exagérant. Pour le calmer, il faut mesurer ses mots : presque, inutile de, plus encore que.', 'In the western forest, the tree spirit repeats every word, exaggerating it. To calm it, you must measure your words: almost, no need to, even more than.')),
  [CH('n1-w5-c1', ('Presque, inutile, plus encore', 'Almost, needless, even more'), [
    L('n1-n-bakari', ('Comme si… allait… : 〜んばかりに・〜とばかりに', 'As if about to…: 〜んばかりに・〜とばかりに'), ('Décrire une attitude si marquée qu’on croirait l’action sur le point de se produire.', 'Describe an attitude so marked that the action seems about to happen.'), 10, [
        ('Radical en ない + んばかりに / んばかりの + nom = comme si l’on allait… : 泣かんばかりに 頼む ; 溢れんばかりの 笑顔. する → せんばかり.', 'ない-stem + んばかりに / んばかりの + noun = as if about to…: 泣かんばかりに 頼む ; 溢れんばかりの 笑顔. する → せんばかり.'),
        ('Phrase + とばかりに = comme pour dire « … » ; on décrit l’attitude de quelqu’un d’autre : もう 帰れと ばかりに、時計を 見た.', 'Sentence + とばかりに = as if to say “…”; it describes someone else’s attitude: もう 帰れと ばかりに、時計を 見た.'),
        ('Ces formes décrivent une impression extérieure, pas une intention qu’on exprime soi-même.', 'These forms describe an outward impression, not an intention one expresses oneself.'),
      ], [
        G('gram-n1-n-bakari-ni', '〜んばかりに', '〜んばかりに', '~n bakari ni', ('comme si l’on allait…, presque à…', 'as if about to…, almost to the point of…')),
        G('gram-n1-to-bakari-ni', '〜とばかりに', '〜とばかりに', '~to bakari ni', ('comme pour dire…', 'as if to say…')),
        V('vocab-afuremasu', '溢れます', 'あふれます', 'afuremasu', ('déborder', 'to overflow')),
        V('vocab-egao', '笑顔', 'えがお', 'egao', ('visage souriant', 'smiling face')),
        V('vocab-hakushu', '拍手', 'はくしゅ', 'hakushu', ('applaudissements', 'applause')),
        V('vocab-koko-zo', 'ここぞ', 'ここぞ', 'koko zo', ('c’est le moment ou jamais', 'now is the moment')),
        K('kanji-n1-afureru', '溢', 'あふれる', 'afureru', ('déborder', 'overflow'), ['イツ'], ['あふ(れる)'], 13),
        K('kanji-n1-haku', '拍', 'はく', 'haku', ('battement, frapper', 'beat, clap'), ['ハク', 'ヒョウ'], [], 8),
      ], [
        ex('彼女は 泣かんばかりに 助けを 求めた。', 'かのじょは なかんばかりに たすけを もとめた。', 'Elle a demandé de l’aide, presque en larmes.', 'She asked for help, almost in tears.'),
        ex('観客は 待って いたと ばかりに 拍手を 始めた。', 'かんきゃくは まって いたと ばかりに はくしゅを はじめた。', 'Le public s’est mis à applaudir comme s’il n’attendait que ça.', 'The audience began to applaud as if they had been waiting for it.'),
      ], [
        FB(CHOOSE, '子どもたちは 溢れ＿ 笑顔で 迎えて くれた。', ['んばかりの', 'とばかりに', 'までもない'], 'んばかりの', ('Devant un nom : 〜んばかりの.', 'Before a noun: 〜んばかりの.'), ('Les enfants nous ont accueillis avec des sourires débordants.', 'The children welcomed us with beaming smiles.')),
        FB(CHOOSE, '彼は「ここぞ」＿、大きな 声で 意見を 述べた。', ['とばかりに', 'んばかりに', 'にもまして'], 'とばかりに', ('Comme pour dire « … » : 〜とばかりに.', 'As if to say “…”: 〜とばかりに.'), ('Comme si c’était le moment ou jamais, il a exposé son avis d’une voix forte.', 'As if to say “now is the time”, he stated his opinion loudly.')),
        TF('店員は 早く 帰れと ばかりに 片付けを 始めた。', ('Le vendeur a demandé poliment aux clients de rester.', 'The clerk politely asked the customers to stay.'), FAUX, ('〜とばかりに : son attitude disait « partez vite ».', '〜とばかりに: his attitude said “leave quickly”.')),
        PC(COMPLETE, '犬は 散歩に 行きたいと ばかり＿、ドアの 前で 待って いた。', ['に', 'を', 'で'], 'に', ('〜と ばかりに.', '〜と ばかりに.'), ('Le chien attendait devant la porte comme pour dire qu’il voulait sortir.', 'The dog waited at the door as if to say it wanted a walk.')),
      ]),
    L('n1-made-mo-nai', ('Inutile de… : 〜までもない・〜には及ばない', 'No need to…: 〜までもない・〜には及ばない'), ('Dire qu’une action est superflue tant la chose est évidente ou simple.', 'Say that an action is unnecessary because the thing is obvious or simple.'), 10, [
        ('Verbe au dictionnaire + までもない = il n’est pas nécessaire d’aller jusqu’à… : 言うまでもない (il va sans dire). 〜までもなく = sans même avoir besoin de.', 'Dictionary-form verb + までもない = there is no need to go as far as…: 言うまでもない (needless to say). 〜までもなく = without even needing to.'),
        ('Verbe au dictionnaire / nom + には及ばない = ce n’est pas la peine de (formule polie) : わざわざ 来るには 及びません ; ご心配には 及びません.', 'Dictionary-form verb / noun + には及ばない = there is no need to (polite formula): わざわざ 来るには 及びません ; ご心配には 及びません.'),
        ('〜に及ばない sans は signifie aussi « ne pas égaler » : 私は 兄に 及ばない.', '〜に及ばない without は also means “not to match”: 私は 兄に 及ばない.'),
      ], [
        G('gram-n1-made-mo-nai', '〜までもない', '〜までもない', '~made mo nai', ('inutile de…, il va sans dire', 'no need to…, needless to')),
        G('gram-n1-ni-wa-oyobanai', '〜には及ばない', '〜にはおよばない', '~ni wa oyobanai', ('ce n’est pas la peine de… (poli)', 'there is no need to… (polite)')),
        V('vocab-wazawaza', 'わざわざ', 'わざわざ', 'wazawaza', ('exprès, en se donnant la peine', 'expressly, going out of one’s way')),
        V('vocab-meihaku', '明白', 'めいはく', 'meihaku', ('évident, manifeste', 'obvious, plain')),
        V('vocab-joushiki', '常識', 'じょうしき', 'joushiki', ('bon sens, savoir commun', 'common sense')),
        V('vocab-kyouyou', '強要', 'きょうよう', 'kyouyou', ('contrainte (forcer quelqu’un)', 'coercion, forcing')),
        K('kanji-n1-oyobu', '及', 'およぶ', 'oyobu', ('atteindre, s’étendre à', 'reach, extend to'), ['キュウ'], ['およ(ぶ)'], 3),
        K('kanji-n1-haku-white', '白', 'はく', 'haku', ('blanc ; clair', 'white; clear'), ['ハク', 'ビャク'], ['しろ'], 5),
      ], [
        ex('健康が 大切な ことは 言うまでもない。', 'けんこうが たいせつな ことは いうまでもない。', 'Il va sans dire que la santé est essentielle.', 'It goes without saying that health is important.'),
        ex('簡単な 手続きですから、わざわざ 来るには 及びません。', 'かんたんな てつづきですから、わざわざ くるには およびません。', 'C’est une démarche simple, ce n’est pas la peine de vous déplacer.', 'It is a simple procedure, so there is no need to come in person.'),
      ], [
        FB(CHOOSE, 'この 程度の 問題なら、先生に 聞く＿。', ['までもない', 'にもまして', 'とばかりに'], 'までもない', ('Inutile de… : 〜までもない.', 'No need to…: 〜までもない.'), ('Pour un problème de ce niveau, inutile de demander au professeur.', 'For a problem like this, there is no need to ask the teacher.')),
        FB(CHOOSE, 'ご心配には ＿。すぐ 治りますから。', ['及びません', '堪えません', '足りません'], '及びません', ('Formule polie : ご心配には 及びません.', 'Polite formula: ご心配には 及びません.'), ('Ne vous inquiétez pas, je vais vite guérir.', 'There is no need to worry; I will soon be better.')),
        TF('結果は 調べるまでもなく 明白だった。', ('Il a fallu une longue enquête pour connaître le résultat.', 'A long investigation was needed to find out the result.'), FAUX, ('〜までもなく : c’était évident sans même vérifier.', '〜までもなく: it was obvious without even checking.')),
        SO(ORDER('Il va sans dire que c’est important.', 'It goes without saying that it is important.'), ['大切な', 'ことは', '言う', 'までもない'], ('言う + までもない.', '言う + までもない.')),
      ]),
    L('n1-ni-mo-mashite', ('Plus encore que…, contrairement à… : 〜にもまして・〜にひきかえ', 'Even more than…, in contrast to…: 〜にもまして・〜にひきかえ'), ('Comparer en surenchérissant, ou opposer deux personnes ou situations.', 'Compare by going one better, or contrast two people or situations.'), 10, [
        ('Nom + にもまして = plus encore que : 去年にも まして 暑い ; 何にも まして 大切な もの (ce qui compte plus que tout).', 'Noun + にもまして = even more than: 去年にも まして 暑い ; 何にも まして 大切な もの (what matters more than anything).'),
        ('Nom / forme neutre + の + にひきかえ = contrairement à, par contraste avec (souvent avec un jugement) : 兄に ひきかえ、弟は よく 働く.', 'Noun / plain form + の + にひきかえ = in contrast to (often with a judgement): 兄に ひきかえ、弟は よく 働く.'),
        ('〜にひきかえ oppose deux éléments comparables ; c’est plus écrit et plus tranché que 〜に比べて.', '〜にひきかえ contrasts two comparable items; it is more written and sharper than 〜に比べて.'),
      ], [
        G('gram-n1-ni-mo-mashite', '〜にもまして', '〜にもまして', '~ni mo mashite', ('plus encore que…', 'even more than…')),
        G('gram-n1-ni-hikikae', '〜にひきかえ', '〜にひきかえ', '~ni hikikae', ('contrairement à…, par contraste avec…', 'in contrast to…')),
        V('vocab-kinben', '勤勉', 'きんべん', 'kinben', ('travailleur, assidu', 'diligent, hard-working')),
        V('vocab-taida', '怠惰', 'たいだ', 'taida', ('paresse', 'laziness')),
        V('vocab-zennen', '前年', 'ぜんねん', 'zennen', ('l’année précédente', 'the previous year')),
        V('vocab-juuyousei', '重要性', 'じゅうようせい', 'juuyousei', ('importance', 'importance, significance')),
        K('kanji-n1-da', '惰', 'だ', 'da', ('indolence', 'indolence'), ['ダ'], [], 12),
        K('kanji-n1-okotaru', '怠', 'おこたる', 'okotaru', ('négliger, paresser', 'neglect, be idle'), ['タイ'], ['おこた(る)', 'なま(ける)'], 9),
      ], [
        ex('今年の 夏は 前年にも まして 暑い。', 'ことしの なつは ぜんねんにも まして あつい。', 'Cet été est encore plus chaud que l’an dernier.', 'This summer is even hotter than last year.'),
        ex('勤勉な 姉に ひきかえ、妹は 怠惰だ。', 'きんべんな あねに ひきかえ、いもうとは たいだだ。', 'Contrairement à sa sœur aînée, travailleuse, la cadette est paresseuse.', 'Unlike her diligent elder sister, the younger one is lazy.'),
      ], [
        FB(CHOOSE, '何＿ 健康が 大切だ。', ['にもまして', 'にひきかえ', 'までもなく'], 'にもまして', ('Plus que tout : 何にも まして.', 'More than anything: 何にも まして.'), ('La santé compte plus que tout.', 'Health matters more than anything.')),
        FB(CHOOSE, '去年の 失敗＿、今年は 大成功だった。', ['にひきかえ', 'にもまして', 'とばかりに'], 'にひきかえ', ('Opposition : 〜にひきかえ.', 'Contrast: 〜にひきかえ.'), ('Contrairement à l’échec de l’an dernier, cette année a été un grand succès.', 'In contrast to last year’s failure, this year was a great success.')),
        TF('教育の 重要性は 以前にも まして 高まって いる。', ('L’éducation compte moins qu’avant.', 'Education matters less than before.'), FAUX, ('〜にもまして : son importance grandit encore plus.', '〜にもまして: its importance is growing even more.')),
        PC(COMPLETE, '兄＿ ひきかえ、弟は よく 勉強する。', ['に', 'を', 'と'], 'に', ('〜に ひきかえ.', '〜に ひきかえ.'), ('Contrairement à son frère aîné, le cadet étudie beaucoup.', 'Unlike his elder brother, the younger one studies hard.')),
      ]),
  ])])

# ═════════════════════════ Île 6 : occasions et aboutissements ═════════════════════════
W6 = WORLD('n1-w6', ('Occasions et aboutissements', 'Occasions and outcomes'), REGION,
  ('Saisir une occasion pour changer, dire jusqu’où une chose est allée, et décrire une circonstance particulière.', 'Seize an occasion to change, say how far something has gone, and describe a special circumstance.'),
  (('L’Umibōzu des Marées', 'The Umibōzu of the Tides'), '海', ('Au port de l’ouest, le moine des mers surgit des vagues et réclame un tonneau. Il n’épargne que les navires qui savent saisir l’occasion et dire jusqu’où ils sont allés.', 'At the western port, the sea monk rises from the waves and demands a barrel. He spares only ships that know how to seize the moment and say how far they have come.')),
  [CH('n1-w6-c1', ('À l’occasion de, jusqu’à, puisque', 'On the occasion of, as far as, since'), [
    L('n1-wo-ki-ni', ('À l’occasion de… : 〜を機に・〜を契機に', 'Taking the opportunity of…: 〜を機に・〜を契機に'), ('Dire qu’un événement a servi de point de départ à un changement.', 'Say that an event served as the starting point for a change.'), 10, [
        ('Nom + を機に = à l’occasion de, en profitant de (un tournant personnel) : 結婚を 機に、仕事を 辞めた.', 'Noun + を機に = on the occasion of, taking the chance of (a personal turning point): 結婚を 機に、仕事を 辞めた.'),
        ('Nom + を契機に / を契機として = à la suite de, avec… pour déclencheur (plus soutenu, souvent historique ou social) : 事故を 契機に、法律が 改正された.', 'Noun + を契機に / を契機として = prompted by, with… as the trigger (more formal, often historical or social): 事故を 契機に、法律が 改正された.'),
        ('La seconde partie exprime un changement ou un nouveau départ, jamais une simple suite d’événements.', 'The second half expresses a change or a new start, never a mere sequence of events.'),
      ], [
        G('gram-n1-wo-ki-ni', '〜を機に', '〜をきに', '~wo ki ni', ('à l’occasion de…, en profitant de…', 'taking the opportunity of…')),
        G('gram-n1-wo-keiki-ni', '〜を契機に', '〜をけいきに', '~wo keiki ni', ('à la suite de…, déclenché par…', 'prompted by…, triggered by…')),
        V('vocab-kaisei', '改正', 'かいせい', 'kaisei', ('révision (d’une loi)', 'revision, amendment')),
        V('vocab-teinen', '定年', 'ていねん', 'teinen', ('âge de la retraite', 'retirement age')),
        V('vocab-kikai-ni', '機会', 'きかい', 'kikai', ('occasion, opportunité', 'opportunity, chance')),
        V('vocab-kaikaku', '改革', 'かいかく', 'kaikaku', ('réforme', 'reform')),
        K('kanji-n1-ki', '機', 'き', 'ki', ('machine ; occasion', 'machine; occasion'), ['キ'], ['はた'], 16),
        K('kanji-n1-kaku', '革', 'かく', 'kaku', ('cuir ; réformer', 'leather; reform'), ['カク'], ['かわ'], 9),
      ], [
        ex('転勤を 機に、家族で 田舎へ 引っ越した。', 'てんきんを きに、かぞくで いなかへ ひっこした。', 'Profitant de ma mutation, nous avons déménagé en famille à la campagne.', 'Taking the opportunity of my transfer, the family moved to the countryside.'),
        ex('その 事件を 契機に、政治改革が 始まった。', 'その じけんを けいきに、せいじかいかくが はじまった。', 'C’est à la suite de cette affaire que la réforme politique a commencé.', 'Prompted by that incident, political reform began.'),
      ], [
        FB(CHOOSE, '入院を ＿、たばこを やめた。', ['機に', '限りに', 'もって'], '機に', ('Tournant personnel : 〜を機に.', 'A personal turning point: 〜を機に.'), ('Mon hospitalisation m’a poussé à arrêter de fumer.', 'I took my hospital stay as the moment to quit smoking.')),
        FB(CHOOSE, '大地震を ＿ として、建物の 基準が 見直された。', ['契機', '機会', '改正'], '契機', ('〜を契機として = déclenché par.', '〜を契機として = triggered by.'), ('À la suite du grand séisme, les normes de construction ont été revues.', 'Prompted by the major earthquake, building standards were reviewed.')),
        TF('卒業を 機に、一人暮らしを 始めた。', ('La personne a commencé à vivre seule à l’occasion de son diplôme.', 'The speaker started living alone upon graduating.'), VRAI, ('〜を機に = en profitant de ce tournant.', '〜を機に = taking that turning point.')),
        SO(ORDER('À l’occasion de son mariage, elle a déménagé.', 'On getting married, she moved house.'), ['結婚', 'を 機に', '彼女は', '引っ越した'], ('Nom + を 機に, puis le changement.', 'Noun + を 機に, then the change.')),
      ]),
    L('n1-ni-itatte', ('Jusqu’à…, quant à… : 〜に至っては・〜に至るまで', 'To the point of…, as for…: 〜に至っては・〜に至るまで'), ('Dire qu’une situation est allée jusqu’à un point extrême, ou couvre tout un ensemble.', 'Say that a situation has reached an extreme point, or covers a whole range.'), 10, [
        ('Nom + に至っては = quant à… (le cas le plus extrême d’une série, souvent négatif) : 父は 料理が 苦手だが、兄に 至っては お湯も 沸かせない.', 'Noun + に至っては = as for… (the most extreme case in a series, often negative): 父は 料理が 苦手だが、兄に 至っては お湯も 沸かせない.'),
        ('Nom + に至るまで = jusqu’à (y compris le détail le plus inattendu) : 服装から 言葉遣いに 至るまで 注意された.', 'Noun + に至るまで = right down to (including the most unexpected detail): 服装から 言葉遣いに 至るまで 注意された.'),
        ('Verbe / nom + に至って(初めて) = ce n’est qu’en arrivant à ce stade que : 死者が 出るに 至って、ようやく 対策が とられた.', 'Verb / noun + に至って(初めて) = only on reaching that stage: 死者が 出るに 至って、ようやく 対策が とられた.'),
      ], [
        G('gram-n1-ni-itatte-wa', '〜に至っては', '〜にいたっては', '~ni itatte wa', ('quant à… (cas extrême)', 'as for… (the extreme case)')),
        G('gram-n1-ni-itaru-made', '〜に至るまで', '〜にいたるまで', '~ni itaru made', ('jusqu’à… (y compris)', 'right down to…')),
        V('vocab-kotobazukai', '言葉遣い', 'ことばづかい', 'kotobazukai', ('façon de parler, langage', 'choice of words, language')),
        V('vocab-fukusou', '服装', 'ふくそう', 'fukusou', ('tenue vestimentaire', 'attire, dress')),
        V('vocab-taisaku', '対策', 'たいさく', 'taisaku', ('mesures (contre un problème)', 'countermeasures')),
        V('vocab-yamamichi', '山道', 'やまみち', 'yamamichi', ('chemin de montagne', 'mountain path')),
        K('kanji-n1-itaru', '至', 'いたる', 'itaru', ('atteindre, parvenir à', 'reach, arrive at'), ['シ'], ['いた(る)'], 6),
        K('kanji-n1-saku', '策', 'さく', 'saku', ('plan, mesure', 'plan, measure'), ['サク'], [], 12),
      ], [
        ex('面接では 服装から 言葉遣いに 至るまで 見られる。', 'めんせつでは ふくそうから ことばづかいに いたるまで みられる。', 'En entretien, on regarde tout, de la tenue jusqu’à la façon de parler.', 'In an interview, everything is checked, from your attire right down to your language.'),
        ex('被害が 広がるに 至って、ようやく 対策が とられた。', 'ひがいが ひろがるに いたって、ようやく たいさくが とられた。', 'Ce n’est qu’une fois les dégâts étendus que des mesures ont enfin été prises.', 'Only when the damage had spread were countermeasures finally taken.'),
      ], [
        FB(CHOOSE, 'みんな 遅刻したが、田中さん＿、来も しなかった。', ['に至っては', 'に至るまで', 'を機に'], 'に至っては', ('Le cas le plus extrême : 〜に至っては.', 'The most extreme case: 〜に至っては.'), ('Tout le monde est arrivé en retard, et M. Tanaka, lui, n’est même pas venu.', 'Everyone was late, and as for Mr Tanaka, he did not even come.')),
        FB(CHOOSE, '子どもから お年寄り＿、誰もが 楽しめる 祭りだ。', ['に至るまで', 'に至っては', 'にひきかえ'], 'に至るまで', ('Jusqu’à (inclus) : 〜に至るまで.', 'Right down to: 〜に至るまで.'), ('C’est une fête que tout le monde apprécie, des enfants jusqu’aux personnes âgées.', 'It is a festival everyone enjoys, from children to the elderly.')),
        TF('問題が 大きく なるに 至って 初めて、政府は 動いた。', ('Le gouvernement a agi dès le début.', 'The government acted from the start.'), FAUX, ('〜に至って初めて : il n’a agi qu’une fois le problème devenu grave.', '〜に至って初めて: it only acted once the problem had become serious.')),
        PC(COMPLETE, '細かい 点＿ 至るまで、よく 調べて ある。', ['に', 'を', 'で'], 'に', ('〜に 至るまで.', '〜に 至るまで.'), ('Tout a été vérifié avec soin, jusque dans les moindres détails.', 'Everything has been checked carefully, right down to the fine points.')),
      ]),
    L('n1-to-atte', ('Puisque c’est…, en pleine… : 〜とあって・〜ところを', 'Since it is…, despite being…: 〜とあって・〜ところを'), ('Expliquer une situation par une circonstance exceptionnelle, et remercier ou s’excuser d’avoir dérangé.', 'Explain a situation by an exceptional circumstance, and thank or apologise for a disturbance.'), 10, [
        ('Forme neutre / nom + とあって = étant donné que (une circonstance spéciale) ; la suite décrit ce qu’on observe : 連休とあって、観光地は 人で いっぱいだ.', 'Plain form / noun + とあって = given that (a special circumstance); what follows describes what is observed: 連休とあって、観光地は 人で いっぱいだ.'),
        ('〜とあれば = s’il s’agit de… (alors on est prêt à) : 子どもの ためと あれば、何でも する.', '〜とあれば = if it is a matter of… (then one is willing to): 子どもの ためと あれば、何でも する.'),
        ('〜ところを (soutenu) = alors que vous êtes en train de… : お休みの ところを 失礼します ; お忙しい ところを ありがとうございます.', '〜ところを (formal) = when you are in the middle of…: お休みの ところを 失礼します ; お忙しい ところを ありがとうございます.'),
      ], [
        G('gram-n1-to-atte', '〜とあって', '〜とあって', '~to atte', ('étant donné que… (circonstance spéciale)', 'given that… (special circumstance)')),
        G('gram-n1-to-areba', '〜とあれば', '〜とあれば', '~to areba', ('s’il s’agit de…, pour…', 'if it is for…, if it means…')),
        V('vocab-renkyuu', '連休', 'れんきゅう', 'renkyuu', ('jours fériés consécutifs, pont', 'consecutive holidays')),
        V('vocab-kankouchi', '観光地', 'かんこうち', 'kankouchi', ('site touristique', 'tourist spot')),
        V('vocab-gentei', '限定', 'げんてい', 'gentei', ('édition limitée, limité à', 'limited (edition)')),
        V('vocab-gyouretsu', '行列', 'ぎょうれつ', 'gyouretsu', ('file d’attente, cortège', 'queue, procession')),
        K('kanji-n1-retsu', '列', 'れつ', 'retsu', ('rangée, file', 'row, line'), ['レツ'], [], 6),
        K('kanji-n1-chin', '陳', 'ちん', 'chin', ('exposer, aligner', 'exhibit, set out'), ['チン'], [], 11),
      ], [
        ex('期間限定の 商品とあって、店の 前には 長い 行列が できた。', 'きかんげんていの しょうひんとあって、みせの まえには ながい ぎょうれつが できた。', 'Comme c’était un produit en édition limitée, une longue file s’est formée devant le magasin.', 'Since it was a limited-time product, a long queue formed in front of the shop.'),
        ex('お休みの ところを お邪魔して、申し訳ありません。', 'おやすみの ところを おじゃまして、もうしわけありません。', 'Je suis désolé de vous déranger pendant votre jour de repos.', 'I am sorry to disturb you on your day off.'),
      ], [
        FB(CHOOSE, '人気歌手が 来る＿、会場は 満員だった。', ['とあって', 'ところを', 'に至っては'], 'とあって', ('Circonstance spéciale : 〜とあって.', 'A special circumstance: 〜とあって.'), ('Comme une chanteuse célèbre venait, la salle était comble.', 'With a popular singer coming, the hall was packed.')),
        FB(CHOOSE, 'お忙しい ＿、ありがとうございました。', ['ところを', 'とあって', 'までもなく'], 'ところを', ('Remerciement poli : お忙しい ところを.', 'Polite thanks: お忙しい ところを.'), ('Merci de nous avoir accordé du temps malgré votre emploi du temps chargé.', 'Thank you for taking the time when you are so busy.')),
        TF('家族の ためと あれば、どんな 仕事でも する。', ('La personne refuse de travailler pour sa famille.', 'The speaker refuses to work for their family.'), FAUX, ('〜とあれば : pour sa famille, elle est prête à tout.', '〜とあれば: for the family, they will do anything.')),
        SO(ORDER('Comme c’est un long week-end, les sites touristiques sont bondés.', 'Since it is a long weekend, tourist spots are crowded.'), ['連休', 'とあって', '観光地は', '混んで いる'], ('Nom + とあって, puis le constat.', 'Noun + とあって, then the observation.')),
      ]),
  ])])

# ═════════════════════════ Île 7 : quoi qu'il arrive ═════════════════════════
W7 = WORLD('n1-w7', ('Quoi qu’il arrive', 'Whatever happens'), REGION,
  ('Dire qu’une chose ne change rien, qu’une autre est indispensable, et qu’un résultat est inévitable.', 'Say that one thing changes nothing, that another is essential, and that a result is unavoidable.'),
  (('Le Gashadokuro Implacable', 'The Relentless Gashadokuro'), '骨', ('Ce squelette géant, fait des os de soldats oubliés, assiège le château de l’ouest. Il ne recule devant rien. Prouve que, quoi qu’il arrive, tu tiendras parole.', 'This giant skeleton, made of the bones of forgotten soldiers, besieges the western castle. Nothing makes it retreat. Prove that, whatever happens, you will keep your word.')),
  [CH('n1-w7-c1', ('Que…ou non, sans, forcément', 'Whether or not, without, inevitably'), [
    L('n1-you-ga', ('Que… ou non : 〜ようが・〜ようが〜まいが', 'Whether… or not: 〜ようが・〜ようが〜まいが'), ('Dire qu’une condition ne change rien à la décision.', 'Say that a condition makes no difference to the decision.'), 10, [
        ('Verbe à la forme volontaire + が / と = même si, peu importe que : 誰が 何と 言おうが、私は 行く.', 'Volitional verb + が / と = even if, no matter whether: 誰が 何と 言おうが、私は 行く.'),
        ('Volontaire + が + verbe + まいが = que… ou non : 雨が 降ろうが 降るまいが、試合は 行う. まい = négation de la volonté (行くまい, するまい / しまい).', 'Volitional + が + verb + まいが = whether… or not: 雨が 降ろうが 降るまいが、試合は 行う. まい = negative volitional (行くまい, するまい / しまい).'),
        ('Avec un adjectif : 高かろうが 安かろうが ; avec un nom : 子どもだろうが 大人だろうが.', 'With an adjective: 高かろうが 安かろうが ; with a noun: 子どもだろうが 大人だろうが.'),
      ], [
        G('gram-n1-you-ga', '〜ようが・〜ようと', '〜ようが・〜ようと', '~you ga / ~you to', ('peu importe que…, même si…', 'no matter whether…, even if…')),
        G('gram-n1-you-ga-mai-ga', '〜ようが〜まいが', '〜ようが〜まいが', '~you ga ~mai ga', ('que… ou non', 'whether… or not')),
        V('vocab-kesshin', '決心', 'けっしん', 'kesshin', ('résolution, décision ferme', 'resolve, determination')),
        V('vocab-shinpai-goto', '心配事', 'しんぱいごと', 'shinpaigoto', ('souci', 'worry, concern')),
        V('vocab-kitai-hazure', '期待外れ', 'きたいはずれ', 'kitaihazure', ('déception', 'disappointment')),
        V('vocab-kankei-nai', '無関係', 'むかんけい', 'mukankei', ('sans rapport', 'unrelated, irrelevant')),
        K('kanji-n1-kotsu', '骨', 'ほね', 'hone', ('os', 'bone'), ['コツ'], ['ほね'], 10),
        K('kanji-n1-tou', '頭', 'とう', 'tou', ('tête ; tête de bétail', 'head; head of cattle'), ['トウ', 'ズ'], ['あたま'], 16),
      ], [
        ex('周りが 何と 言おうが、私の 決心は 変わらない。', 'まわりが なんと いおうが、わたしの けっしんは かわらない。', 'Quoi que disent les autres, ma décision ne changera pas.', 'Whatever people around me say, my resolve will not change.'),
        ex('雨が 降ろうが 降るまいが、祭りは 予定どおり 行われる。', 'あめが ふろうが ふるまいが、まつりは よていどおり おこなわれる。', 'Qu’il pleuve ou non, la fête aura lieu comme prévu.', 'Whether it rains or not, the festival will go ahead as planned.'),
      ], [
        FB(CHOOSE, '反対され＿、この 計画は 続ける。', ['ようが', 'まいが', 'とあって'], 'ようが', ('Même si : volontaire + が.', 'Even if: volitional + が.'), ('Même si on s’y oppose, je poursuivrai ce projet.', 'Even if people oppose it, I will continue this plan.')),
        FB(CHOOSE, '参加しようが ＿、連絡だけは して ください。', ['しまいが', 'しないが', 'するまいと'], 'しまいが', ('する → しまい / するまい.', 'する → しまい / するまい.'), ('Que vous participiez ou non, prévenez-nous au moins.', 'Whether you take part or not, at least let us know.')),
        TF('高かろうが 安かろうが、必要な ものは 買う。', ('La personne n’achète que ce qui est bon marché.', 'The speaker buys only cheap things.'), FAUX, ('〜かろうが〜かろうが : le prix ne change rien.', '〜かろうが〜かろうが: the price makes no difference.')),
        SO(ORDER('Quoi qu’on dise, je ne renoncerai pas.', 'Whatever anyone says, I will not give up.'), ['誰が', '何と 言おうが', 'あきらめない'], ('Volontaire + が, puis la décision.', 'Volitional + が, then the decision.')),
      ]),
    L('n1-nashi-ni-wa', ('Sans… impossible : 〜なしには・〜なくしては', 'Impossible without…: 〜なしには・〜なくしては'), ('Dire qu’une chose est la condition indispensable d’une autre.', 'Say that one thing is the essential condition for another.'), 10, [
        ('Nom + なしには / なしでは + forme négative ou de possibilité niée = sans…, impossible de : 努力なしには 成功できない.', 'Noun + なしには / なしでは + negative or impossible form = without…, it is impossible to: 努力なしには 成功できない.'),
        ('Nom + なくしては = sans (plus écrit et solennel) : 皆様の ご支援なくしては、この 成果は ありませんでした.', 'Noun + なくしては = without (more written and solemn): 皆様の ご支援なくしては、この 成果は ありませんでした.'),
        ('Nom + なしに = sans (simple absence) : 許可なしに 入らないで ください.', 'Noun + なしに = without (simple absence): 許可なしに 入らないで ください.'),
      ], [
        G('gram-n1-nashi-ni-wa', '〜なしには', '〜なしには', '~nashi ni wa', ('sans… (impossible)', 'without… (impossible)')),
        G('gram-n1-nakushite-wa', '〜なくしては', '〜なくしては', '~nakushite wa', ('sans… (solennel)', 'without… (solemn)')),
        V('vocab-shien', '支援', 'しえん', 'shien', ('soutien, aide', 'support, backing')),
        V('vocab-seika', '成果', 'せいか', 'seika', ('résultat obtenu, fruit (du travail)', 'achievement, fruits of work')),
        V('vocab-rikai', '理解', 'りかい', 'rikai', ('compréhension', 'understanding')),
        V('vocab-namida-nashi', '涙なし', 'なみだなし', 'namida nashi', ('sans larmes', 'without tears')),
        K('kanji-n1-en', '援', 'えん', 'en', ('soutenir, appuyer', 'support, assist'), ['エン'], [], 12),
        K('kanji-n1-ka', '果', 'か', 'ka', ('fruit, résultat', 'fruit, result'), ['カ'], ['は(たす)', 'は(て)'], 8),
      ], [
        ex('皆様の ご支援なくしては、この 成果は ありませんでした。', 'みなさまの ごしえんなくしては、この せいかは ありませんでした。', 'Sans votre soutien à tous, ce résultat n’aurait pas été possible.', 'Without the support of all of you, this achievement would not have been possible.'),
        ex('この 映画は 涙なしには 見られない。', 'この えいがは なみだなしには みられない。', 'On ne peut pas regarder ce film sans pleurer.', 'You cannot watch this film without crying.'),
      ], [
        FB(CHOOSE, '家族の 理解＿、留学は できなかった。', ['なしには', 'とあって', 'ようが'], 'なしには', ('Condition indispensable : 〜なしには.', 'Essential condition: 〜なしには.'), ('Sans la compréhension de ma famille, je n’aurais pas pu partir étudier à l’étranger.', 'Without my family’s understanding, I could not have studied abroad.')),
        FB(CHOOSE, '許可＿ 写真を 撮っては いけません。', ['なしに', 'なくしては', 'ならでは'], 'なしに', ('Simple absence : 〜なしに.', 'Simple absence: 〜なしに.'), ('Il est interdit de prendre des photos sans autorisation.', 'Do not take photos without permission.')),
        TF('彼の 協力なくしては、成功しなかっただろう。', ('Son aide n’a joué aucun rôle.', 'His help played no part.'), FAUX, ('〜なくしては : sans lui, pas de succès.', '〜なくしては: without him, no success.')),
        PC(COMPLETE, '努力＿ しには、上手に ならない。', ['な', 'の', 'を'], 'な', ('努力なしには.', '努力なしには.'), ('Sans effort, on ne progresse pas.', 'You will not improve without effort.')),
      ]),
    L('n1-zu-ni-wa-okanai', ('Ne manquera pas de… : 〜ずにはおかない・〜ずにはすまない', 'Will inevitably…: 〜ずにはおかない・〜ずにはすまない'), ('Dire qu’un effet se produira forcément, ou qu’une obligation ne peut être évitée.', 'Say that an effect will inevitably occur, or that an obligation cannot be avoided.'), 10, [
        ('Radical en ない + ずにはおかない = ne manquera pas de, provoque forcément (effet sur les autres) : 彼の 演説は 人々を 感動させずには おかない. する → せずにはおかない.', 'ない-stem + ずにはおかない = will not fail to, inevitably causes (an effect on others): 彼の 演説は 人々を 感動させずには おかない. する → せずにはおかない.'),
        ('Radical en ない + ずにはすまない / ないではすまない = on ne peut pas s’en tirer sans (obligation sociale) : 謝らずには すまない.', 'ない-stem + ずにはすまない / ないではすまない = one cannot get away without (social obligation): 謝らずには すまない.'),
        ('Ces formes sont fermes et assez écrites ; à l’oral on dira 〜なければならない ou 〜しかない.', 'These forms are firm and fairly written; in speech one would say 〜なければならない or 〜しかない.'),
      ], [
        G('gram-n1-zu-ni-wa-okanai', '〜ずにはおかない', '〜ずにはおかない', '~zu ni wa okanai', ('ne manquera pas de…, forcément', 'will not fail to…, inevitably')),
        G('gram-n1-zu-ni-wa-sumanai', '〜ずにはすまない', '〜ずにはすまない', '~zu ni wa sumanai', ('ne pas pouvoir éviter de…', 'cannot get away without…')),
        V('vocab-enzetsu', '演説', 'えんぜつ', 'enzetsu', ('discours (public)', 'public speech')),
        V('vocab-hamon', '波紋', 'はもん', 'hamon', ('remous, répercussions', 'ripples, repercussions')),
        V('vocab-shazai', '謝罪', 'しゃざい', 'shazai', ('excuses officielles', 'formal apology')),
        V('vocab-sekininsha', '責任者', 'せきにんしゃ', 'sekininsha', ('responsable (personne)', 'person in charge')),
        K('kanji-n1-en-perform', '演', 'えん', 'en', ('jouer, représenter', 'perform, act'), ['エン'], [], 14),
        K('kanji-n1-zai', '罪', 'つみ', 'tsumi', ('faute, crime', 'sin, crime'), ['ザイ'], ['つみ'], 13),
      ], [
        ex('首相の 発言は 波紋を 呼ばずには おかないだろう。', 'しゅしょうの はつげんは はもんを よばずには おかないだろう。', 'Les propos du Premier ministre ne manqueront pas de faire des remous.', 'The prime minister’s remarks will inevitably cause a stir.'),
        ex('これだけの 迷惑を かけたのだから、謝罪せずには すまない。', 'これだけの めいわくを かけたのだから、しゃざいせずには すまない。', 'Après avoir causé autant de tort, on ne peut pas se dispenser de présenter des excuses.', 'Having caused this much trouble, we cannot get away without apologising.'),
      ], [
        FB(CHOOSE, 'この 作品は 見る 人を 感動させ＿。', ['ずにはおかない', 'ずにはすまない', 'なしには'], 'ずにはおかない', ('Effet inévitable sur les autres : 〜ずにはおかない.', 'An inevitable effect on others: 〜ずにはおかない.'), ('Cette œuvre ne manquera pas d’émouvoir ceux qui la verront.', 'This work will not fail to move those who see it.')),
        FB(CHOOSE, '責任者として、説明せ＿ すまない。', ['ずには', 'ずにはおか', 'ないでも'], 'ずには', ('Obligation : 〜ずには すまない ; する → せずには.', 'Obligation: 〜ずには すまない ; する → せずには.'), ('En tant que responsable, je ne peux pas me dispenser de m’expliquer.', 'As the person in charge, I cannot avoid giving an explanation.')),
        TF('この 問題は 社会に 影響を 与えずには おかない。', ('Le problème n’aura sans doute aucun effet.', 'The problem will probably have no effect.'), FAUX, ('〜ずにはおかない : il aura forcément un impact.', '〜ずにはおかない: it will inevitably have an impact.')),
        DC(('Tu as cassé un vase précieux chez ton hôte. Un ami te demande ce que tu vas faire.', 'You broke a precious vase at your host’s home. A friend asks what you will do.'), [('友だち', 'どう するの？')], ('Ton ami te demande ce que tu comptes faire.', 'Your friend asks what you intend to do.'), ['直接 謝らずには すまないよ。', '直接 謝らずには おかないよ。', '直接 謝るまでもないよ。'], '直接 謝らずには すまないよ。', ('Obligation morale : 〜ずにはすまない.', 'A moral obligation: 〜ずにはすまない.')),
      ]),
  ])])

# ═════════════════════════ Île 8 : le style des discours ═════════════════════════
W8 = WORLD('n1-w8', ('Le style des discours', 'The style of speeches'), REGION,
  ('Dire le but dans un style solennel, élever le ton selon le rang ou l’enjeu, et énumérer avec force.', 'State a purpose in a solemn style, raise the tone according to rank or stakes, and enumerate forcefully.'),
  (('Ryūjin, Roi des Mers', 'Ryūjin, King of the Seas'), '龍', ('Le dieu-dragon des mers s’est levé devant la côte. Il ne rendra la paix aux eaux que si le nouveau shōgun prononce un discours digne de son rang, devant tout le peuple.', 'The dragon god of the seas has risen off the coast. He will return peace to the waters only if the new shōgun gives a speech worthy of his rank, before all the people.')),
  [CH('n1-w8-c1', ('Afin de, dès lors que, qu’il s’agisse de', 'In order to, once it comes to, be it'), [
    L('n1-beku', ('Afin de… : 〜べく・〜んがため（に）', 'In order to…: 〜べく・〜んがため（に）'), ('Exprimer un but dans le style des discours et des récits.', 'Express a purpose in the style of speeches and narratives.'), 10, [
        ('Verbe au dictionnaire + べく = afin de, pour (écrit) : 夢を 実現す(る)べく、努力を 続けた. する → すべく.', 'Dictionary-form verb + べく = in order to (written): 夢を 実現す(る)べく、努力を 続けた. する → すべく.'),
        ('Radical en ない + んがため(に) = dans le seul but de (très solennel) : 生きんが ために 働く. する → せんがため.', 'ない-stem + んがため(に) = solely in order to (very solemn): 生きんが ために 働く. する → せんがため.'),
        ('〜べく ne se termine pas sur un ordre ou une demande ; la phrase raconte ce qu’on a fait ou fait pour ce but.', '〜べく does not end in an order or request; the sentence tells what one did or does for that purpose.'),
      ], [
        G('gram-n1-beku', '〜べく', '〜べく', '~beku', ('afin de…, pour… (écrit)', 'in order to… (written)')),
        G('gram-n1-n-ga-tame', '〜んがため（に）', '〜んがため（に）', '~n ga tame (ni)', ('dans le seul but de…', 'solely in order to…')),
        V('vocab-jitsugen', '実現', 'じつげん', 'jitsugen', ('réalisation (d’un projet, d’un rêve)', 'realisation, making real')),
        V('vocab-kokumin', '国民', 'こくみん', 'kokumin', ('citoyens, peuple d’un pays', 'the people, citizens')),
        V('vocab-shimei', '使命', 'しめい', 'shimei', ('mission (devoir)', 'mission, calling')),
        V('vocab-fukkou', '復興', 'ふっこう', 'fukkou', ('reconstruction, relèvement', 'reconstruction, revival')),
        K('kanji-n1-mei', '命', 'めい', 'mei', ('vie ; ordre', 'life; command'), ['メイ', 'ミョウ'], ['いのち'], 8),
        K('kanji-n1-kou-rise', '興', 'こう', 'kou', ('s’élever, intérêt', 'rise, interest'), ['コウ', 'キョウ'], ['おこ(る)'], 16),
      ], [
        ex('町を 復興すべく、住民は 力を 合わせた。', 'まちを ふっこうすべく、じゅうみんは ちからを あわせた。', 'Pour reconstruire la ville, les habitants ont uni leurs forces.', 'To rebuild the town, the residents joined forces.'),
        ex('勝たんが ために、手段を 選ばない 人も いる。', 'かたんが ために、しゅだんを えらばない ひとも いる。', 'Certains sont prêts à tout dans le seul but de gagner.', 'Some people stop at nothing solely in order to win.'),
      ], [
        FB(CHOOSE, '夢を 実現す＿、彼は 海外へ 渡った。', ['べく', 'べからず', 'まじき'], 'べく', ('But (écrit) : 〜べく.', 'Purpose (written): 〜べく.'), ('Pour réaliser son rêve, il est parti à l’étranger.', 'To realise his dream, he went overseas.')),
        FB(CHOOSE, '国民の 生活を 守らん＿ ために、全力を 尽くします。', ['が', 'の', 'を'], 'が', ('〜んが ため.', '〜んが ため.'), ('Je ferai tout mon possible dans le seul but de protéger la vie des citoyens.', 'I will do my utmost solely to protect the lives of the people.')),
        TF('早く 来るべく、準備して ください。', ('Cette phrase est naturelle en japonais.', 'This sentence is natural Japanese.'), FAUX, ('〜べく ne s’emploie pas avec une demande (〜てください).', '〜べく is not used with a request (〜てください).')),
        SO(ORDER('Pour accomplir sa mission, il a travaillé jour et nuit.', 'To fulfil his mission, he worked day and night.'), ['使命を', '果たすべく', '彼は', '昼も 夜も 働いた'], ('Verbe + べく, puis l’action.', 'Verb + べく, then the action.')),
      ]),
    L('n1-tomo-naru-to', ('Dès lors qu’on devient… : 〜ともなると・〜ともなれば', 'Once it comes to…: 〜ともなると・〜ともなれば'), ('Dire qu’à un certain rang, âge ou enjeu, les attentes changent naturellement.', 'Say that at a certain rank, age or stake, expectations naturally change.'), 10, [
        ('Nom / verbe au dictionnaire + ともなると / ともなれば = dès lors que l’on atteint (un niveau élevé), naturellement… : 社長とも なると、毎日 忙しい.', 'Noun / dictionary-form verb + ともなると / ともなれば = once one reaches (a high level), naturally…: 社長とも なると、毎日 忙しい.'),
        ('La suite décrit ce qui va de soi à ce niveau : 大学生とも なれば、自分で 考える べきだ.', 'What follows describes what is natural at that level: 大学生とも なれば、自分で 考える べきだ.'),
        ('Nuance : 〜となると est plus neutre ; avec も, on souligne que le niveau atteint est remarquable.', 'Nuance: 〜となると is more neutral; adding も stresses that the level reached is remarkable.'),
      ], [
        G('gram-n1-tomo-naru-to', '〜ともなると', '〜ともなると', '~tomo naru to', ('dès lors qu’on devient…, à ce niveau…', 'once one becomes…, at that level…')),
        G('gram-n1-tomo-nareba', '〜ともなれば', '〜ともなれば', '~tomo nareba', ('quand il s’agit de… (niveau élevé)', 'when it comes to… (a high level)')),
        V('vocab-shushou', '首相', 'しゅしょう', 'shushou', ('Premier ministre', 'prime minister')),
        V('vocab-chii', '地位', 'ちい', 'chii', ('position sociale, rang', 'status, rank')),
        V('vocab-omomi', '重み', 'おもみ', 'omomi', ('poids (importance)', 'weight, gravity')),
        V('vocab-taishou', '大将', 'たいしょう', 'taishou', ('général (armée), chef', 'general, commander')),
        K('kanji-n1-shou', '将', 'しょう', 'shou', ('général, commander', 'general, command'), ['ショウ'], [], 10),
        K('kanji-n1-shin', '臣', 'しん', 'shin', ('vassal, sujet', 'retainer, subject'), ['シン', 'ジン'], [], 7),
      ], [
        ex('首相とも なると、一言の 重みが 違う。', 'しゅしょうとも なると、ひとことの おもみが ちがう。', 'Quand on est Premier ministre, chaque mot a un tout autre poids.', 'Once you are prime minister, a single word carries a different weight.'),
        ex('年末とも なれば、どこも 人で いっぱいだ。', 'ねんまつとも なれば、どこも ひとで いっぱいだ。', 'En fin d’année, il y a du monde partout.', 'When it comes to the end of the year, everywhere is packed.'),
      ], [
        FB(CHOOSE, '社長＿、休みも ほとんど ない。', ['ともなると', 'をもって', 'にひきかえ'], 'ともなると', ('Dès lors qu’on atteint ce rang : 〜ともなると.', 'Once one reaches that rank: 〜ともなると.'), ('Quand on est président d’entreprise, on n’a presque pas de congés.', 'Once you are company president, you hardly get any time off.')),
        FB(CHOOSE, 'プロ＿、ミスは 許されない。', ['ともなれば', 'までもなく', 'なしには'], 'ともなれば', ('À un niveau élevé : 〜ともなれば.', 'At a high level: 〜ともなれば.'), ('Quand on est professionnel, l’erreur n’est pas permise.', 'When you are a professional, mistakes are not tolerated.')),
        TF('高い 地位とも なると、責任も 重く なる。', ('Plus le rang est élevé, plus la responsabilité est lourde.', 'The higher the rank, the heavier the responsibility.'), VRAI, ('〜ともなると : à ce niveau, cela va de soi.', '〜ともなると: at that level, it goes without saying.')),
        PC(COMPLETE, '大将 とも ＿ と、部下の 命を 預かる。', ['なる', 'する', 'ある'], 'なる', ('〜とも なると.', '〜とも なると.'), ('Quand on est général, on a la vie de ses hommes entre ses mains.', 'Once you are a general, you hold your men’s lives in your hands.')),
      ]),
    L('n1-de-are', ('Qu’il s’agisse de… : 〜であれ・〜といい〜といい', 'Be it…: 〜であれ・〜といい〜といい'), ('Énumérer des cas pour montrer que la règle vaut pour tous, ou louer une chose sous tous ses aspects.', 'List cases to show the rule applies to all, or praise something in every respect.'), 10, [
        ('Nom + であれ = que ce soit… : 誰で あれ、規則は 守るべきだ. Nom + であれ + nom + であれ = que ce soit… ou… : 大人で あれ 子どもで あれ.', 'Noun + であれ = be it…: 誰で あれ、規則は 守るべきだ. Noun + であれ + noun + であれ = whether… or…: 大人で あれ 子どもで あれ.'),
        ('Nom + といい + nom + といい = tant pour… que pour… (jugement d’ensemble, souvent admiratif) : 味と いい 値段と いい、文句 なしだ.', 'Noun + といい + noun + といい = both in… and in… (an overall judgement, often admiring): 味と いい 値段と いい、文句 なしだ.'),
        ('〜にしろ〜にしろ (N2) a un sens proche de 〜であれ〜であれ, en moins solennel.', '〜にしろ〜にしろ (N2) is close in meaning to 〜であれ〜であれ, but less solemn.'),
      ], [
        G('gram-n1-de-are', '〜であれ', '〜であれ', '~de are', ('que ce soit…, qui que ce soit…', 'be it…, whoever…')),
        G('gram-n1-to-ii-to-ii', '〜といい〜といい', '〜といい〜といい', '~to ii ~to ii', ('tant pour… que pour…', 'both in… and in…')),
        V('vocab-kibo', '規模', 'きぼ', 'kibo', ('échelle, envergure', 'scale, size')),
        V('vocab-monku-nashi', '文句なし', 'もんくなし', 'monku nashi', ('irréprochable', 'faultless, beyond complaint')),
        V('vocab-mibun', '身分', 'みぶん', 'mibun', ('condition sociale, statut', 'social standing, status')),
        V('vocab-byoudou', '平等', 'びょうどう', 'byoudou', ('égalité', 'equality')),
        K('kanji-n1-mo', '模', 'も', 'mo', ('modèle, imiter', 'model, imitate'), ['モ', 'ボ'], [], 14),
        K('kanji-n1-byou', '平', 'へい', 'hei', ('plat, paisible', 'flat, peaceful'), ['ヘイ', 'ビョウ'], ['たい(ら)', 'ひら'], 5),
      ], [
        ex('身分が 何で あれ、法の 前では 皆 平等だ。', 'みぶんが なんで あれ、ほうの まえでは みな びょうどうだ。', 'Quelle que soit leur condition, tous sont égaux devant la loi.', 'Whatever their standing, all are equal before the law.'),
        ex('規模と いい 内容と いい、素晴らしい 祭りだった。', 'きぼと いい ないようと いい、すばらしい まつりだった。', 'Tant par son ampleur que par son contenu, ce fut une fête magnifique.', 'In both scale and content, it was a wonderful festival.'),
      ], [
        FB(CHOOSE, '理由が 何＿、暴力は 許されない。', ['であれ', 'といい', 'ともなると'], 'であれ', ('Quel que soit : 〜であれ.', 'Whatever: 〜であれ.'), ('Quelle qu’en soit la raison, la violence est inacceptable.', 'Whatever the reason, violence is unacceptable.')),
        FB(CHOOSE, '味と ＿ サービスと いい、この 店は 最高だ。', ['いい', 'あれ', 'して'], 'いい', ('〜といい〜といい.', '〜といい〜といい.'), ('Tant pour le goût que pour le service, ce restaurant est le meilleur.', 'Both the food and the service make this restaurant the best.')),
        TF('大人で あれ 子どもで あれ、入場料は 同じだ。', ('Les enfants paient moins cher.', 'Children pay less.'), FAUX, ('〜であれ〜であれ : adulte ou enfant, même tarif.', '〜であれ〜であれ: adult or child, same price.')),
        SO(ORDER('Qui que ce soit, il faut respecter les règles.', 'Whoever it is, the rules must be followed.'), ['誰', 'で あれ', '規則は', '守るべきだ'], ('Nom + で あれ, puis la règle.', 'Noun + で あれ, then the rule.')),
      ]),
  ])])

FINAL = {
  'slug': 'n1-final',
  'title': t(('Simulation JLPT N1', 'JLPT N1 simulation')),
  'region': REGION,
  'description': t(('Examen blanc non officiel du N1 : vocabulaire et kanji, grammaire, écoute. Chronométré, corrigé par compétence.', 'Unofficial N1 mock exam: vocabulary and kanji, grammar, listening. Timed, marked by skill.')),
  'exam': 'n1-mock',
  'chapters': [],
}

level = {
  'contentVersion': '2026.11.17b',
  'level': {'code': 'N1', 'title': t(('Avancé : japonais écrit et soutenu', 'Advanced: written and formal Japanese')), 'region': REGION, 'order': 1},
  'notice': t(('Les listes de vocabulaire et de kanji de Koto Quest sont alignées sur les compétences attendues au N1 mais ne constituent pas des listes officielles du JLPT.', 'Koto Quest’s vocabulary and kanji lists are aligned with the skills expected at N1 but are not official JLPT lists.')),
  'worlds': [W1, W2, W3, W4, W5, W6, W7, W8, FINAL],
}
t((REGION, 'The Shōgun’s Domain'))
os.makedirs(os.path.join(ROOT, 'content/n1'), exist_ok=True)
check_and_write(level, 'content/n1/n1.json', ['content/n5/n5.json', 'content/n4/n4.json', 'content/n3/n3.json', 'content/n2/n2.json'])
