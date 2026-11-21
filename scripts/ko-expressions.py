# Onglet Expressions en coréen (content/expressions/expressions-ko.json), français + anglais.
# Usage : python3 scripts/ko-expressions.py
import json, os, sys
sys.path.insert(0, os.path.dirname(__file__))
from kq_content import ROOT, DICO, EN, P_DICT, t

def E(slug, front, romaji, meaning, note, register, example=None):
    it = {'slug': slug, 'kind': 'vocabulary', 'front': front, 'reading': None, 'romaji': romaji,
          'meaning': t(meaning), 'note': t(note), 'register': register}
    if example:
        jp, fr, en = example
        it['example'] = {'jp': jp, 'fr': t((fr, en))}
    return it

def TH(slug, glyph, title, description, expressions):
    return {'slug': slug, 'glyph': glyph, 'title': t(title), 'description': t(description), 'expressions': expressions}

THEMES = [
  TH('ko-politesse', '예', ('Politesse essentielle', 'Essential politeness'), ('Les petites formules polies qui ouvrent toutes les portes en Corée.', 'The small polite phrases that open every door in Korea.'), [
    E('ko-annyeonghaseyo', '안녕하세요', 'annyeonghaseyo', ('bonjour (poli)', 'hello (polite)'), ('Le salut de tous les jours, à toute heure. On l’accompagne d’une légère inclinaison de la tête.', 'The everyday greeting, at any time of day. It comes with a slight bow of the head.'), 'polite', ('안녕하세요, 처음 뵙겠습니다.', 'Bonjour, enchanté de faire votre connaissance.', 'Hello, nice to meet you.')),
    E('kexpr-gamsahamnida', '감사합니다', 'gamsahamnida', ('merci (formel)', 'thank you (formal)'), ('Le merci le plus courant avec des inconnus, dans les magasins et au travail.', 'The most common thank you with strangers, in shops and at work.'), 'formal'),
    E('kexpr-gomawoyo', '고마워요', 'gomawoyo', ('merci (poli, plus chaleureux)', 'thanks (polite, warmer)'), ('Merci poli mais plus proche, entre collègues ou connaissances.', 'A polite but warmer thank you, between colleagues or acquaintances.'), 'polite'),
    E('kexpr-joesonghamnida', '죄송합니다', 'joesonghamnida', ('je suis désolé (formel)', 'I am sorry (formal)'), ('Pour s’excuser sincèrement, auprès d’un client, d’un aîné ou d’un supérieur.', 'To apologise sincerely, to a customer, an elder or a superior.'), 'formal'),
    E('kexpr-mianhaeyo', '미안해요', 'mianhaeyo', ('pardon, désolé (poli)', 'sorry (polite)'), ('Excuses du quotidien, pour un petit retard ou une bousculade.', 'Everyday apology, for being a little late or bumping into someone.'), 'polite'),
    E('kexpr-gwaenchanayo', '괜찮아요', 'gwaenchanayo', ('ça va, ce n’est rien', 'it’s OK, no problem'), ('Réponse passe-partout : pour rassurer, refuser poliment ou dire que tout va bien.', 'All-purpose answer: to reassure, decline politely or say everything is fine.'), 'polite', ('— 미안해요! — 괜찮아요.', '— Pardon ! — Ce n’est rien.', '— Sorry! — That’s OK.')),
    E('kexpr-sillyehamnida', '실례합니다', 'sillyehamnida', ('excusez-moi (pour déranger)', 'excuse me (to interrupt)'), ('Pour interpeller quelqu’un, entrer dans une pièce ou passer devant une personne.', 'To get someone’s attention, enter a room or pass in front of someone.'), 'formal'),
  ]),
  TH('ko-rencontres', '만', ('Rencontres et au revoir', 'Meeting and parting'), ('Se présenter et prendre congé, en tenant compte de qui part et qui reste.', 'Introducing yourself and taking leave, depending on who is leaving and who is staying.'), [
    E('kexpr-cheoeum', '처음 뵙겠습니다', 'cheoeum boepgetseumnida', ('enchanté (première rencontre)', 'nice to meet you (first meeting)'), ('Formule très polie, à dire la toute première fois qu’on rencontre quelqu’un.', 'A very polite phrase, said the very first time you meet someone.'), 'formal'),
    E('kexpr-mannaseo-bangawoyo', '만나서 반가워요', 'mannaseo bangawoyo', ('ravi de vous rencontrer', 'pleased to meet you'), ('Plus naturel et chaleureux que 처음 뵙겠습니다.', 'More natural and warmer than 처음 뵙겠습니다.'), 'polite'),
    E('kexpr-annyeonghi-gaseyo', '안녕히 가세요', 'annyeonghi gaseyo', ('au revoir (à celui qui part)', 'goodbye (to the person leaving)'), ('Littéralement « partez en paix » : on le dit quand l’autre s’en va.', 'Literally “go in peace”: you say it when the other person is leaving.'), 'polite'),
    E('kexpr-annyeonghi-gyeseyo', '안녕히 계세요', 'annyeonghi gyeseyo', ('au revoir (à celui qui reste)', 'goodbye (to the person staying)'), ('Littéralement « restez en paix » : on le dit quand c’est soi qui part.', 'Literally “stay in peace”: you say it when you are the one leaving.'), 'polite', ('사장님, 안녕히 계세요!', 'Au revoir, patron ! (en quittant la boutique)', 'Goodbye! (to the shop owner, as you leave)')),
    E('kexpr-tto-mannayo', '또 만나요', 'tto mannayo', ('à bientôt, à la prochaine', 'see you again'), ('Pour se quitter en promettant de se revoir.', 'To part while promising to meet again.'), 'polite'),
    E('kexpr-jal-jinaesseoyo', '잘 지냈어요?', 'jal jinaesseoyo?', ('comment ça va depuis le temps ?', 'how have you been?'), ('Quand on retrouve quelqu’un qu’on n’a pas vu depuis un moment.', 'When you see someone again after a while.'), 'polite'),
  ]),
  TH('ko-comprendre', '말', ('Se faire comprendre', 'Making yourself understood'), ('Demander de répéter, de ralentir ou de traduire.', 'Asking someone to repeat, slow down or translate.'), [
    E('kexpr-dasi', '다시 한번 말해 주세요', 'dasi hanbeon malhae juseyo', ('pouvez-vous répéter, s’il vous plaît ?', 'could you say that again, please?'), ('Indispensable quand on débute : personne ne s’en offusque.', 'Essential when you are a beginner: nobody takes offence.'), 'polite'),
    E('kexpr-cheoncheonhi', '천천히 말해 주세요', 'cheoncheonhi malhae juseyo', ('parlez lentement, s’il vous plaît', 'please speak slowly'), ('천천히 = lentement.', '천천히 = slowly.'), 'polite'),
    E('kexpr-molla', '잘 모르겠어요', 'jal moreugesseoyo', ('je ne sais pas trop, je ne comprends pas bien', 'I’m not sure, I don’t quite understand'), ('Façon douce de dire qu’on ne sait pas ou qu’on n’a pas compris.', 'A gentle way of saying you don’t know or didn’t understand.'), 'polite'),
    E('kexpr-mwora', '이거 한국어로 뭐예요?', 'igeo hangugeoro mwoyeyo?', ('comment dit-on ça en coréen ?', 'what is this in Korean?'), ('En montrant un objet : le meilleur moyen d’apprendre du vocabulaire.', 'While pointing at an object: the best way to learn vocabulary.'), 'polite'),
    E('kexpr-arasseoyo', '알겠어요', 'algesseoyo', ('j’ai compris, d’accord', 'I see, understood'), ('Pour confirmer qu’on a compris une consigne.', 'To confirm that you have understood an instruction.'), 'polite'),
  ]),
  TH('ko-restaurant', '식', ('Au restaurant et au café', 'At restaurants and cafés'), ('Commander, remercier, payer : la table coréenne a ses rituels.', 'Ordering, thanking, paying: the Korean table has its rituals.'), [
    E('kexpr-yeogiyo', '여기요!', 'yeogiyo!', ('s’il vous plaît ! (pour appeler le serveur)', 'excuse me! (to call the waiter)'), ('Littéralement « ici ! » : on appelle le serveur à voix haute, c’est tout à fait normal.', 'Literally “over here!”: you call the waiter out loud, it is completely normal.'), 'neutral'),
    E('ko-jal-meokgetseumnida', '잘 먹겠습니다', 'jal meokgetseumnida', ('merci pour ce repas (avant de manger)', 'thank you for the meal (before eating)'), ('À dire avant de commencer, surtout quand quelqu’un vous invite ou a cuisiné.', 'Said before you start, especially when someone treats you or has cooked.'), 'formal'),
    E('kexpr-jal-meogeosseumnida', '잘 먹었습니다', 'jal meogeotseumnida', ('merci, c’était très bon (après le repas)', 'thank you, that was delicious (after the meal)'), ('À dire en finissant ou en quittant le restaurant.', 'Said when you finish or leave the restaurant.'), 'formal'),
    E('kexpr-mat-itgye', '맛있게 드세요', 'masitge deuseyo', ('bon appétit', 'enjoy your meal'), ('Ce que dit le serveur ou l’hôte en servant le plat.', 'What the waiter or host says when serving the dish.'), 'polite'),
    E('kexpr-gyesan', '계산해 주세요', 'gyesanhae juseyo', ('l’addition, s’il vous plaît', 'the bill, please'), ('En Corée, on paie souvent au comptoir à la sortie.', 'In Korea you often pay at the counter on the way out.'), 'polite'),
    E('kexpr-an-maepge', '안 맵게 해 주세요', 'an maepge hae juseyo', ('pas épicé, s’il vous plaît', 'not spicy, please'), ('Utile : beaucoup de plats coréens sont relevés au piment (고추).', 'Useful: many Korean dishes are seasoned with chilli (고추).'), 'polite'),
  ]),
  TH('ko-magasins', '돈', ('Dans les magasins', 'In shops'), ('Demander un prix, marchander un peu au marché, payer par carte.', 'Asking a price, haggling a little at the market, paying by card.'), [
    E('kexpr-eolmayeyo', '이거 얼마예요?', 'igeo eolmayeyo?', ('combien coûte ceci ?', 'how much is this?'), ('La question à connaître par cœur au marché de Namdaemun.', 'The question to know by heart at Namdaemun Market.'), 'polite'),
    E('kexpr-kkakka', '좀 깎아 주세요', 'jom kkakka juseyo', ('faites-moi un petit prix', 'please give me a discount'), ('Au marché traditionnel, marchander gentiment est courant ; pas dans les grands magasins.', 'At traditional markets, gentle haggling is common; not in department stores.'), 'polite'),
    E('kexpr-kadeu', '카드 돼요?', 'kadeu dwaeyo?', ('vous acceptez la carte ?', 'do you take cards?'), ('돼요 = « ça marche ? », « c’est possible ? ».', '돼요 = “does it work?”, “is it possible?”.'), 'polite'),
    E('kexpr-bongtu', '봉투 주세요', 'bongtu juseyo', ('un sac, s’il vous plaît', 'a bag, please'), ('Les sacs sont souvent payants : on les demande à la caisse.', 'Bags often cost extra: you ask for one at the till.'), 'polite'),
    E('kexpr-gureogo', '그냥 구경하고 있어요', 'geunyang gugyeonghago isseoyo', ('je regarde seulement', 'I’m just looking'), ('Pour répondre au vendeur qui propose son aide.', 'To answer a shop assistant who offers help.'), 'polite'),
  ]),
  TH('ko-transports', '길', ('Transports et orientation', 'Getting around'), ('Trouver son chemin dans le métro, le bus et le taxi.', 'Finding your way on the subway, bus and taxi.'), [
    E('kexpr-eodi-isseoyo', '화장실이 어디에 있어요?', 'hwajangsiri eodie isseoyo?', ('où sont les toilettes ?', 'where is the toilet?'), ('Nom + 이/가 어디에 있어요? : la question pour tout lieu.', 'Noun + 이/가 어디에 있어요?: the question for any place.'), 'polite'),
    E('kexpr-gajuseyo', '서울역으로 가 주세요', 'seoulyeogeuro ga juseyo', ('à la gare de Séoul, s’il vous plaît (taxi)', 'to Seoul Station, please (taxi)'), ('Destination + (으)로 가 주세요 : à dire au chauffeur de taxi.', 'Destination + (으)로 가 주세요: to say to the taxi driver.'), 'polite'),
    E('kexpr-yeogiseo-naeryeo', '여기서 내려 주세요', 'yeogiseo naeryeo juseyo', ('déposez-moi ici, s’il vous plaît', 'please drop me off here'), ('En taxi, pour descendre tout de suite.', 'In a taxi, to get out right here.'), 'polite'),
    E('kexpr-eolmana-geollyeo', '얼마나 걸려요?', 'eolmana geollyeoyo?', ('combien de temps ça prend ?', 'how long does it take?'), ('Pour demander la durée d’un trajet.', 'To ask how long a journey takes.'), 'polite'),
    E('kexpr-gireul-ileosseoyo', '길을 잃었어요', 'gireul ireosseoyo', ('je me suis perdu(e)', 'I’m lost'), ('Littéralement « j’ai perdu le chemin ».', 'Literally “I have lost the way”.'), 'polite'),
  ]),
  TH('ko-reactions', '감', ('Réactions et émotions', 'Reactions and feelings'), ('Les exclamations qu’on entend dans tous les dramas.', 'The exclamations you hear in every drama.'), [
    E('kexpr-daebak', '대박!', 'daebak!', ('génial ! incroyable !', 'awesome! amazing!'), ('Exclamation familière d’émerveillement ou de surprise.', 'Casual exclamation of amazement or surprise.'), 'casual'),
    E('kexpr-jinjja', '진짜요?', 'jinjjayo?', ('vraiment ?', 'really?'), ('진짜 = vrai. Sans 요, entre amis : 진짜?', '진짜 = real. Without 요, among friends: 진짜?'), 'polite'),
    E('kexpr-hwaiting', '화이팅!', 'hwaiting!', ('courage ! allez !', 'go for it! you can do it!'), ('Pour encourager quelqu’un avant un examen, un match, un entretien.', 'To encourage someone before an exam, a match, an interview.'), 'casual', ('토픽 시험 화이팅!', 'Courage pour le TOPIK !', 'Good luck with the TOPIK!')),
    E('kexpr-aigo', '아이고', 'aigo', ('oh là là, aïe', 'oh dear, oh my'), ('Soupir de fatigue, de surprise ou de compassion, très courant chez les plus âgés.', 'A sigh of tiredness, surprise or sympathy, very common among older people.'), 'casual'),
    E('kexpr-sugohasyeosseumnida', '수고하셨습니다', 'sugohasyeotseumnida', ('merci pour votre travail, bon travail', 'thank you for your hard work'), ('Pour saluer l’effort de quelqu’un à la fin d’une tâche ou d’une journée.', 'To acknowledge someone’s effort at the end of a task or a working day.'), 'formal'),
  ]),
  # ── Révision des proverbes (TOPIK 5-6) ──
  TH('ko-sokdam', '속', ('Proverbes du quotidien', 'Everyday proverbs'), ('Les 속담 que les Coréens glissent dans la conversation : à réviser jusqu’à les reconnaître au vol.', 'The 속담 Koreans slip into conversation: review them until you recognise them instantly.'), [
    E('kprov-gowaya', '가는 말이 고와야 오는 말이 곱다', 'ganeun mari gowaya oneun mari gopda', ('qui parle bien reçoit de bonnes paroles', 'speak kindly and you’ll be spoken to kindly'), ('Mot à mot : « si les mots qui partent sont beaux, ceux qui reviennent le sont aussi ».', 'Literally: “if the words that go out are fine, those that come back are fine too”.'), 'neutral', ('가는 말이 고와야 오는 말이 곱다고, 먼저 친절하게 말해 보세요.', 'Qui parle bien reçoit de bonnes paroles : commencez par parler gentiment.', 'Speak kindly and you will be spoken to kindly: try being nice first.')),
    E('kprov-natmal', '낮말은 새가 듣고 밤말은 쥐가 듣는다', 'nanmareun saega deutgo bammareun jwiga deunneunda', ('les murs ont des oreilles', 'walls have ears'), ('« Le jour, les oiseaux écoutent ; la nuit, les souris » : méfiez-vous de ce que vous dites.', '“By day the birds listen; by night, the mice”: be careful what you say.'), 'neutral'),
    E('kprov-baekji', '백지장도 맞들면 낫다', 'baekjijangdo matdeulmyeon natda', ('l’union fait la force', 'many hands make light work'), ('« Même une feuille de papier est plus légère portée à deux. »', '“Even a sheet of paper is lighter when two people carry it.”'), 'neutral'),
    E('kprov-haneul', '하늘이 무너져도 솟아날 구멍이 있다', 'haneuri muneojyeodo sosanal gumeongi itda', ('il y a toujours une issue', 'there is always a way out'), ('« Même si le ciel s’effondre, il reste un trou par où s’échapper. »', '“Even if the sky falls, there is a hole to escape through.”'), 'neutral'),
    E('kprov-so', '소 잃고 외양간 고친다', 'so ilko oeyanggan gochinda', ('fermer l’écurie quand le cheval s’est enfui', 'to shut the stable door after the horse has bolted'), ('« Réparer l’étable après avoir perdu la vache » : agir trop tard.', '“Repairing the cowshed after losing the cow”: acting too late.'), 'neutral'),
    E('kprov-sijak', '시작이 반이다', 'sijagi banida', ('commencer, c’est déjà faire la moitié du chemin', 'well begun is half done'), ('On le dit pour encourager quelqu’un qui hésite à se lancer.', 'Said to encourage someone who hesitates to get started.'), 'neutral', ('시작이 반이에요. 오늘부터 토픽 공부를 해 봐요!', 'Commencer, c’est déjà la moitié : on se met au TOPIK dès aujourd’hui !', 'Well begun is half done: let’s start studying for the TOPIK today!')),
    E('kprov-beoreut', '세 살 버릇 여든까지 간다', 'se sal beoreut yeodeunkkaji ganda', ('les habitudes d’enfance durent toute la vie', 'old habits die hard'), ('« Une habitude prise à trois ans dure jusqu’à quatre-vingts ans. »', '“A habit formed at three lasts until eighty.”'), 'neutral'),
    E('kprov-deungjan', '등잔 밑이 어둡다', 'deungjan miti eoduptta', ('ce qu’on cherche est souvent sous son nez', 'it is darkest under the lamp'), ('« Il fait sombre sous la lampe » : on ne voit pas ce qui est tout près.', '“It is dark under the oil lamp”: we miss what is right next to us.'), 'neutral'),
    E('kprov-wonsungi', '원숭이도 나무에서 떨어진다', 'wonsungido namueseo tteoreojinda', ('même les meilleurs se trompent', 'even monkeys fall from trees'), ('Pour consoler quelqu’un de doué qui vient de faire une erreur.', 'To console a skilled person who has just made a mistake.'), 'neutral'),
    E('kprov-geumgang', '금강산도 식후경', 'geumgangsando sikugyeong', ('on admire mieux le ventre plein', 'even Mount Geumgang is best seen after a meal'), ('Même les plus beaux monts Geumgang se contemplent après le repas : d’abord manger !', 'Even the beautiful Geumgang mountains are best admired after eating: food first!'), 'casual'),
  ]),
  TH('ko-sokdam-contes', '담', ('Proverbes des contes et des animaux', 'Proverbs from tales and animals'), ('Tigres, grenouilles, baleines et jarres percées : les images des contes devenues proverbes.', 'Tigers, frogs, whales and leaky jars: images from folk tales that became proverbs.'), [
    E('kprov-horangi', '호랑이도 제 말 하면 온다', 'horangido je mal hamyeon onda', ('quand on parle du loup, on en voit la queue', 'speak of the devil'), ('« Même le tigre arrive quand on parle de lui. »', '“Even the tiger comes when you talk about it.”'), 'casual', ('호랑이도 제 말 하면 온다더니, 민수 씨가 왔네요!', 'Quand on parle du loup… voilà Minsu !', 'Speak of the devil, here comes Minsu!')),
    E('kprov-gaeguri', '개구리 올챙이 적 생각 못 한다', 'gaeguri olchaengi jeok saenggak mot handa', ('oublier d’où l’on vient', 'to forget where you came from'), ('« La grenouille ne se souvient pas d’avoir été têtard » : se dit d’un parvenu.', '“The frog forgets it was once a tadpole”: said of an upstart.'), 'neutral'),
    E('kprov-gorae', '고래 싸움에 새우 등 터진다', 'gorae ssaume saeu deung teojinda', ('les petits paient les querelles des grands', 'the little ones suffer when the big ones fight'), ('« Quand les baleines se battent, c’est le dos de la crevette qui éclate. »', '“When whales fight, the shrimp’s back bursts.”'), 'neutral'),
    E('kprov-umul', '우물 안 개구리', 'umul an gaeguri', ('avoir une vision étroite du monde', 'a frog in a well'), ('Se dit de quelqu’un qui ne connaît que son petit monde.', 'Said of someone who knows only their own small world.'), 'neutral'),
    E('kprov-kong', '콩 심은 데 콩 나고 팥 심은 데 팥 난다', 'kong simeun de kong nago pat simeun de pat nanda', ('les effets découlent de leurs causes', 'as you sow, so shall you reap'), ('« Là où l’on sème du soja pousse du soja, là où l’on sème des haricots rouges poussent des haricots rouges. »', '“Where soybeans are sown, soybeans grow; where red beans are sown, red beans grow.”'), 'neutral'),
    E('kprov-dok', '밑 빠진 독에 물 붓기', 'mit ppajin doge mul butgi', ('un effort sans fin et sans résultat', 'pouring water into a bottomless jar'), ('L’épreuve de Kongjwi dans le conte 콩쥐팥쥐 : remplir une jarre percée.', 'Kongjwi’s ordeal in the tale 콩쥐팥쥐: filling a jar with a hole in it.'), 'neutral'),
    E('kprov-nat', '낫 놓고 기역 자도 모른다', 'nat noko giyeok jado moreunda', ('être complètement ignorant', 'to be utterly ignorant'), ('« Ne pas reconnaître la lettre ㄱ même avec une faucille (en forme de ㄱ) devant soi. »', '“Not to recognise the letter ㄱ even with a ㄱ-shaped sickle in front of you.”'), 'casual'),
    E('kprov-tteok', '누워서 떡 먹기', 'nuwoseo tteok meokgi', ('simple comme bonjour', 'a piece of cake'), ('« Manger un gâteau de riz allongé » : une tâche très facile.', '“Eating a rice cake lying down”: a very easy task.'), 'casual', ('이 문제는 누워서 떡 먹기예요.', 'Cet exercice, c’est simple comme bonjour.', 'This question is a piece of cake.')),
  ]),
  TH('ko-sajaseongeo', '성', ('Expressions en quatre caractères', 'Four-character idioms'), ('Les 사자성어, venus des caractères chinois, donnent du style à l’écrit et aux discours.', 'The 사자성어, from Chinese characters, add style to writing and speeches.'), [
    E('kprov-ilseok', '일석이조', 'ilseogijo', ('faire d’une pierre deux coups', 'to kill two birds with one stone'), ('一石二鳥 : une pierre, deux oiseaux.', '一石二鳥: one stone, two birds.'), 'formal'),
    E('kprov-uwang', '우왕좌왕', 'uwangjwawang', ('aller dans tous les sens, s’affoler', 'to run around in confusion'), ('右往左往 : aller à droite, aller à gauche.', '右往左往: going right, going left.'), 'formal'),
    E('kprov-dongmun', '동문서답', 'dongmunseodap', ('répondre à côté de la question', 'an answer beside the point'), ('東問西答 : on demande à l’est, on répond à l’ouest.', '東問西答: asked about the east, answering about the west.'), 'formal'),
    E('kprov-jaksim', '작심삼일', 'jaksimsamil', ('bonnes résolutions sans lendemain', 'resolutions that last three days'), ('作心三日 : une résolution qui tient trois jours.', '作心三日: a resolution that lasts three days.'), 'formal'),
    E('kprov-geumsi', '금시초문', 'geumsichomun', ('première nouvelle', 'the first one has heard of it'), ('今時初聞 : entendu pour la première fois à l’instant.', '今時初聞: heard for the first time just now.'), 'formal'),
    E('kprov-jaeop', '자업자득', 'jaeopjadeuk', ('on récolte ce qu’on a semé', 'you reap what you sow'), ('自業自得 : on reçoit le fruit de ses propres actes.', '自業自得: you receive the fruit of your own deeds.'), 'formal'),
    E('kprov-gwayu', '과유불급', 'gwayubulgeup', ('trop, c’est comme pas assez', 'too much is as bad as too little'), ('過猶不及 : l’excès vaut le manque (Confucius).', '過猶不及: excess is as bad as deficiency (Confucius).'), 'formal'),
    E('kprov-sipjung', '십중팔구', 'sipjungpalgu', ('neuf fois sur dix', 'nine times out of ten'), ('十中八九 : huit ou neuf sur dix, presque sûrement.', '十中八九: eight or nine out of ten, almost certainly.'), 'formal'),
    E('kprov-isim', '이심전심', 'isimjeonsim', ('se comprendre sans un mot', 'to understand each other without words'), ('以心傳心 : de cœur à cœur.', '以心傳心: from heart to heart.'), 'formal'),
    E('kprov-daegi', '대기만성', 'daegimanseong', ('les grands talents mûrissent lentement', 'great talents mature late'), ('大器晩成 : les grands vases se font lentement. Pour encourager qui progresse doucement.', '大器晩成: great vessels take long to make. To encourage someone who progresses slowly.'), 'formal'),
  ]),
]

DATA = {
  'contentVersion': '2026.11.21',
  'language': 'ko',
  'notice': t(('Expressions coréennes courantes sélectionnées par Koto Quest ; la romanisation et le registre (poli, familier…) aident à choisir la bonne formule selon la situation.', 'Common Korean expressions selected by Koto Quest; the romanisation and the register (polite, casual…) help you choose the right phrase for the situation.')),
  'themes': THEMES,
}

for fr, en in EN.items():
    if fr in DICO and DICO[fr] != en:
        raise SystemExit(f'traduction existante différente : {fr} → {DICO[fr]} / {en}')
slugs = [e['slug'] for th in THEMES for e in th['expressions']]
assert len(slugs) == len(set(slugs)), 'slug en double'
json.dump(DATA, open(os.path.join(ROOT, 'content/expressions/expressions-ko.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
DICO.update(EN)
json.dump(DICO, open(P_DICT, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(f'Expressions coréennes : {len(THEMES)} thèmes, {len(slugs)} expressions')
