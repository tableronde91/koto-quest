# Onglet Expressions en chinois (content/expressions/expressions-zh.json), français + anglais.
# Les formules déjà vues dans le parcours HSK 1 gardent leur slug : même notion, même maîtrise.
# Usage : python3 scripts/zh-expressions.py   (après hsk1-level.py)
import json, os, sys
sys.path.insert(0, os.path.dirname(__file__))
from kq_content import ROOT, DICO, EN, P_DICT, t, items_of

HSK1 = {it['slug']: it for it in items_of(json.load(open(os.path.join(ROOT, 'content/hsk1/hsk1.json'), encoding='utf-8')))}

def E(slug, front, pinyin, meaning, note, register, example=None):
    it = {'slug': slug, 'kind': 'vocabulary', 'front': front, 'reading': pinyin, 'romaji': None,
          'meaning': t(meaning), 'note': t(note), 'register': register}
    if slug in HSK1:
        assert (HSK1[slug]['front'], HSK1[slug]['reading'], HSK1[slug]['meaning']) == (front, pinyin, it['meaning']), slug
    if example:
        zh, fr, en = example
        it['example'] = {'jp': zh, 'fr': t((fr, en))}
    return it

def TH(slug, glyph, title, description, expressions):
    return {'slug': slug, 'glyph': glyph, 'title': t(title), 'description': t(description), 'expressions': expressions}

THEMES = [
  TH('zh-politesse', '礼', ('Politesse essentielle', 'Essential politeness'), ('Les formules de base pour saluer, remercier et s’excuser en chinois.', 'The basic phrases for greeting, thanking and apologising in Chinese.'), [
    E('zh-nihao', '你好', 'nǐ hǎo', ('bonjour', 'hello'), ('Le salut universel, à toute heure. Plus respectueux : 您好 (nín hǎo), avec 您, le « vous » de politesse.', 'The universal greeting, at any time of day. More respectful: 您好 (nín hǎo), with 您, the polite “you”.'), 'neutral', ('你好！我叫大卫。', 'Bonjour ! Je m’appelle David.', 'Hello! My name is David.')),
    E('zexpr-ninhao', '您好', 'nín hǎo', ('bonjour (respectueux)', 'hello (respectful)'), ('À une personne âgée, un client, un supérieur : 您 est la forme polie de 你.', 'To an older person, a customer or a superior: 您 is the polite form of 你.'), 'polite'),
    E('zh-xiexie', '谢谢', 'xièxie', ('merci', 'thank you'), ('On le double parfois pour insister : 谢谢谢谢！ Entre proches, on remercie moins qu’en français.', 'It is sometimes repeated for emphasis: 谢谢谢谢！ Close friends thank each other less than in English.'), 'neutral'),
    E('zh-bukeqi', '不客气', 'bú kèqi', ('de rien', 'you’re welcome'), ('Littéralement « ne fais pas de manières ». Variante : 不用谢 (bú yòng xiè), « pas besoin de remercier ».', 'Literally “don’t stand on ceremony”. Variant: 不用谢 (bú yòng xiè), “no need to thank me”.'), 'neutral'),
    E('zh-duibuqi', '对不起', 'duìbuqǐ', ('pardon, désolé', 'sorry'), ('Pour une vraie excuse. Pour attirer l’attention, on dit plutôt 请问 ou 不好意思.', 'For a real apology. To get someone’s attention, you say 请问 or 不好意思 instead.'), 'neutral'),
    E('zh-meiguanxi', '没关系', 'méi guānxi', ('ce n’est pas grave', 'it doesn’t matter'), ('La réponse à 对不起 : « il n’y a pas de lien », rien de grave.', 'The answer to 对不起: “there is no connection”, nothing serious.'), 'neutral', ('——对不起！——没关系。', '— Pardon ! — Ce n’est pas grave.', '— Sorry! — It doesn’t matter.')),
    E('zexpr-buhaoyisi', '不好意思', 'bù hǎoyìsi', ('excusez-moi, je suis gêné', 'excuse me, I’m embarrassed'), ('Excuse légère du quotidien : pour un petit retard, déranger quelqu’un ou refuser poliment.', 'A light everyday apology: for being a little late, disturbing someone or declining politely.'), 'polite'),
  ]),
  TH('zh-rencontres', '见', ('Rencontres et au revoir', 'Meeting and parting'), ('Se présenter, prendre des nouvelles et se quitter.', 'Introducing yourself, asking how someone is and saying goodbye.'), [
    E('zexpr-renshi-ni', '认识你很高兴', 'rènshi nǐ hěn gāoxìng', ('ravi de te connaître', 'glad to get to know you'), ('À dire après une présentation. Réponse : 我也很高兴 (moi aussi).', 'Said after an introduction. Answer: 我也很高兴 (me too).'), 'neutral'),
    E('zexpr-ni-hao-ma', '你好吗？', 'nǐ hǎo ma?', ('comment ça va ?', 'how are you doing?'), ('Moins courant qu’en français ; on répond 我很好 (je vais bien). Entre amis, on demande plutôt 最近怎么样？', 'Less common than in English; the answer is 我很好 (I’m fine). Between friends you rather ask 最近怎么样？'), 'neutral'),
    E('zexpr-chi-le-ma', '吃了吗？', 'chī le ma?', ('tu as mangé ? (salut familier)', 'have you eaten? (casual greeting)'), ('Salut traditionnel entre voisins et proches : ce n’est pas une invitation, juste une façon de dire bonjour.', 'A traditional greeting between neighbours and close friends: it is not an invitation, just a way of saying hello.'), 'casual'),
    E('zh-zaijian', '再见', 'zàijiàn', ('au revoir', 'goodbye'), ('« Se revoir ». Entre amis, on entend aussi 拜拜 (báibái), de l’anglais bye-bye.', '“See again”. Between friends you also hear 拜拜 (báibái), from English bye-bye.'), 'neutral'),
    E('zexpr-mingtian-jian', '明天见', 'míngtiān jiàn', ('à demain', 'see you tomorrow'), ('Moment + 见 : 下午见 (à cet après-midi), 星期一见 (à lundi).', 'Time + 见: 下午见 (see you this afternoon), 星期一见 (see you Monday).'), 'neutral'),
    E('zexpr-man-zou', '慢走', 'màn zǒu', ('prends soin de toi en partant', 'take care on your way'), ('« Marche lentement » : l’hôte le dit à l’invité qui s’en va.', '“Walk slowly”: the host says it to a guest who is leaving.'), 'polite'),
  ]),
  TH('zh-comprendre', '懂', ('Se faire comprendre', 'Making yourself understood'), ('Demander de répéter, de ralentir ou de traduire.', 'Asking someone to repeat, slow down or translate.'), [
    E('zexpr-qingwen', '请问', 'qǐngwèn', ('excusez-moi, puis-je vous demander…', 'excuse me, may I ask…'), ('Pour commencer une question à un inconnu : 请问，火车站在哪儿？', 'To start a question to a stranger: 请问，火车站在哪儿？'), 'polite', ('请问，洗手间在哪儿？', 'Excusez-moi, où sont les toilettes ?', 'Excuse me, where is the toilet?')),
    E('zexpr-ting-bu-dong', '我听不懂', 'wǒ tīng bu dǒng', ('je ne comprends pas (à l’oral)', 'I don’t understand (what I hear)'), ('听 = écouter, 懂 = comprendre : « j’écoute mais je ne comprends pas ».', '听 = listen, 懂 = understand: “I listen but I don’t understand”.'), 'neutral'),
    E('zexpr-zai-shuo', '请再说一遍', 'qǐng zài shuō yí biàn', ('pouvez-vous répéter, s’il vous plaît ?', 'could you say that again, please?'), ('一遍 = une fois (du début à la fin).', '一遍 = once (from start to finish).'), 'polite'),
    E('zexpr-man-dianr', '请说慢一点儿', 'qǐng shuō màn yìdiǎnr', ('parlez plus lentement, s’il vous plaît', 'please speak more slowly'), ('慢 = lent ; 一点儿 = un peu (plus).', '慢 = slow; 一点儿 = a little (more).'), 'polite'),
    E('zexpr-zenme-shuo', '这个用汉语怎么说？', 'zhè ge yòng Hànyǔ zěnme shuō?', ('comment dit-on ça en chinois ?', 'how do you say this in Chinese?'), ('En montrant un objet : le meilleur moyen d’apprendre du vocabulaire.', 'While pointing at an object: the best way to learn vocabulary.'), 'neutral'),
  ]),
  TH('zh-restaurant', '吃', ('Au restaurant', 'At the restaurant'), ('Commander, trinquer et demander l’addition.', 'Ordering, raising a toast and asking for the bill.'), [
    E('zexpr-fuwuyuan', '服务员！', 'fúwùyuán!', ('s’il vous plaît ! (au serveur)', 'excuse me! (to the waiter)'), ('On appelle le serveur ou la serveuse à voix haute : c’est tout à fait normal en Chine.', 'You call the waiter or waitress out loud: it is perfectly normal in China.'), 'neutral'),
    E('zexpr-lai-yi-ge', '来一个…', 'lái yí ge…', ('je vais prendre un…', 'I’ll have a…'), ('Pour commander de façon naturelle : 来一个米饭 (un riz, s’il vous plaît).', 'To order naturally: 来一个米饭 (one rice, please).'), 'casual'),
    E('zexpr-ganbei', '干杯！', 'gānbēi!', ('santé ! (cul sec)', 'cheers! (bottoms up)'), ('« Vider le verre » : on trinque souvent pendant les repas.', '“Dry the glass”: people raise toasts often during meals.'), 'neutral'),
    E('zexpr-mai-dan', '买单', 'mǎidān', ('l’addition, s’il vous plaît', 'the bill, please'), ('Aussi 结账 (jiézhàng). En Chine, une seule personne invite souvent toute la table.', 'Also 结账 (jiézhàng). In China, one person often pays for the whole table.'), 'neutral'),
    E('zexpr-hao-chi', '很好吃', 'hěn hǎochī', ('c’est très bon', 'it’s delicious'), ('好吃 = bon (à manger) ; 好喝 = bon (à boire).', '好吃 = tasty (food); 好喝 = tasty (drink).'), 'neutral'),
  ]),
  TH('zh-marche', '买', ('Faire ses courses', 'Shopping'), ('Demander un prix et marchander au marché.', 'Asking a price and bargaining at the market.'), [
    E('zexpr-duoshao-qian', '多少钱？', 'duōshao qián?', ('combien ça coûte ?', 'how much is it?'), ('La question de base au marché ; la réponse se donne en 块 (yuans).', 'The basic market question; the answer is given in 块 (yuan).'), 'neutral'),
    E('zexpr-tai-gui', '太贵了！', 'tài guì le!', ('c’est trop cher !', 'it’s too expensive!'), ('Le premier mot pour marchander. 贵 = cher.', 'The first word for bargaining. 贵 = expensive.'), 'casual'),
    E('zexpr-pianyi', '便宜一点儿吧', 'piányi yìdiǎnr ba', ('un peu moins cher, s’il vous plaît', 'a bit cheaper, please'), ('便宜 = bon marché ; 吧 adoucit la demande.', '便宜 = cheap; 吧 softens the request.'), 'casual'),
    E('zexpr-wo-kankan', '我看看', 'wǒ kànkan', ('je regarde seulement', 'I’m just looking'), ('Le verbe redoublé (看看) rend l’action légère : « juste un coup d’œil ».', 'The doubled verb (看看) makes the action light: “just a quick look”.'), 'neutral'),
    E('zexpr-wo-yao-zhe-ge', '我要这个', 'wǒ yào zhè ge', ('je prends celui-ci', 'I’ll take this one'), ('要 = vouloir, prendre ; en montrant l’objet.', '要 = to want, to take; while pointing at the item.'), 'neutral'),
  ]),
  TH('zh-chengyu', '成', ('Expressions en quatre caractères', 'Four-character idioms'), ('Les chengyu (成语), souvent tirés d’histoires de l’époque des Royaumes combattants.', 'Chengyu (成语), often drawn from stories of the Warring States period.'), [
    E('zexpr-yi-lu-ping-an', '一路平安', 'yí lù píng’ān', ('bon voyage', 'have a safe trip'), ('« Toute la route en paix » : à dire à quelqu’un qui part en voyage.', '“Peace all along the road”: said to someone setting off on a journey.'), 'neutral'),
    E('zexpr-ma-ma-hu-hu', '马马虎虎', 'mǎmǎhūhū', ('comme ci, comme ça', 'so-so'), ('« Cheval cheval tigre tigre » : ni bien ni mal, ou fait à la va-vite.', '“Horse horse tiger tiger”: neither good nor bad, or done carelessly.'), 'casual'),
    E('zexpr-wan-shi-ru-yi', '万事如意', 'wàn shì rú yì', ('que tout se passe comme tu le souhaites', 'may all go as you wish'), ('Vœu du Nouvel An chinois, avec 新年快乐 (bonne année).', 'A Chinese New Year wish, along with 新年快乐 (happy new year).'), 'formal'),
    E('zexpr-hua-she-tian-zu', '画蛇添足', 'huà shé tiān zú', ('en faire trop et tout gâcher', 'to overdo it and spoil everything'), ('« Ajouter des pattes au serpent qu’on dessine » : une fable du royaume de Chu.', '“Adding legs to a snake you are drawing”: a fable from the state of Chu.'), 'formal'),
    E('zexpr-shou-zhu-dai-tu', '守株待兔', 'shǒu zhū dài tù', ('attendre que la chance revienne sans rien faire', 'to wait idly for luck to strike again'), ('« Garder la souche en attendant le lièvre » : un paysan de Song vit un lièvre s’assommer contre une souche et n’attendit plus que ça.', '“Guarding the stump, waiting for a hare”: a farmer of Song saw a hare knock itself out on a stump and did nothing but wait for another.'), 'formal'),
    E('zexpr-zi-xiang-mao-dun', '自相矛盾', 'zì xiāng máodùn', ('se contredire', 'to contradict oneself'), ('Un marchand de Chu vantait une lance qui perce tout et un bouclier que rien ne perce : d’où 矛盾, « lance-bouclier », la contradiction.', 'A merchant of Chu boasted of a spear that pierces everything and a shield nothing can pierce: hence 矛盾, “spear-shield”, a contradiction.'), 'formal'),
  ]),
]

DATA = {
  'contentVersion': '2026.11.22',
  'language': 'zh',
  'notice': t(('Expressions chinoises courantes sélectionnées par Koto Quest ; le pinyin et le registre (poli, familier…) aident à choisir la bonne formule selon la situation.', 'Common Chinese expressions selected by Koto Quest; the pinyin and the register (polite, casual…) help you choose the right phrase for the situation.')),
  'themes': THEMES,
}

for fr, en in EN.items():
    if fr in DICO and DICO[fr] != en:
        raise SystemExit(f'traduction existante différente : {fr} → {DICO[fr]} / {en}')
slugs = [e['slug'] for th in THEMES for e in th['expressions']]
assert len(slugs) == len(set(slugs)), 'slug en double'
json.dump(DATA, open(os.path.join(ROOT, 'content/expressions/expressions-zh.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
DICO.update(EN)
json.dump(DICO, open(P_DICT, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(f'Expressions chinoises : {len(THEMES)} thèmes, {len(slugs)} expressions')
