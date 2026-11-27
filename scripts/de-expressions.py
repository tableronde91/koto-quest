# Onglet Expressions en allemand (content/expressions/expressions-de.json), français + anglais.
# Politesse, vie quotidienne, expressions imagées et proverbes d'Allemagne.
# Le sens anglais (pour l'interface en anglais) est une courte définition de l'expression.
# Usage : python3 scripts/de-expressions.py
import json, os, sys
sys.path.insert(0, os.path.dirname(__file__))
from de_common import ROOT, DICO, P_DICT, t
import kq_content

def E(slug, front, meaning, note, register, example=None):
    it = {'slug': 'dex-' + slug, 'kind': 'vocabulary', 'front': front, 'reading': None, 'romaji': None,
          'meaning': t(meaning), 'note': t(note), 'register': register}
    if example:
        de, fr, en = example
        it['example'] = {'jp': de, 'fr': t((fr, en))}
    return it

def TH(slug, glyph, title, description, expressions):
    return {'slug': slug, 'glyph': glyph, 'title': t(title), 'description': t(description), 'expressions': expressions}

THEMES = [
  TH('de-hoeflichkeit', '„', ('Politesse et salutations', 'Politeness and greetings'), ('Les formules qui ouvrent toutes les portes : en Allemagne, on se serre la main et on choisit avec soin entre du et Sie.', 'The phrases that open every door: in Germany, people shake hands and choose carefully between du and Sie.'), [
    E('freut-mich', 'Freut mich!', ('ravi·e de vous rencontrer !', 'nice to meet you!'), ('Forme courte de Es freut mich, Sie kennenzulernen. On la dit en serrant la main.', 'Short for Es freut mich, Sie kennenzulernen. People say it while shaking hands.'), 'neutral', ('Ich bin Jacob Grimm. — Freut mich!', 'Je suis Jacob Grimm. — Ravi de vous rencontrer !', 'I am Jacob Grimm. — Nice to meet you!')),
    E('bitte-schoen', 'Bitte schön!', ('je vous en prie ! ; voici !', 'you’re welcome!; here you are!'), ('Bitte sert à tout : demander (s’il vous plaît), répondre à danke (de rien) et tendre quelque chose (voici).', 'Bitte does everything: asking (please), replying to danke (you’re welcome) and handing something over (here you are).'), 'polite'),
    E('entschuldigung', 'Entschuldigung!', ('excusez-moi !', 'excuse me!; sorry!'), ('Pour aborder quelqu’un ou s’excuser d’un petit faux pas. Plus fort : Es tut mir leid (je suis désolé).', 'To approach someone or apologise for a small slip. Stronger: Es tut mir leid (I am sorry).'), 'neutral'),
    E('mahlzeit', 'Mahlzeit!', ('bon appétit ! ; bonjour ! (à midi, au travail)', 'enjoy your meal!; hello! (at lunchtime, at work)'), ('Littéralement « repas ». Entre collègues, on se salue ainsi dans les couloirs vers midi.', 'Literally “mealtime”. Colleagues greet each other this way in the corridors around noon.'), 'casual'),
    E('gesundheit', 'Gesundheit!', ('à tes souhaits !', 'bless you!'), ('Littéralement « santé ». On le dit quand quelqu’un éternue ; pour trinquer, on dit Prost!', 'Literally “health”. Said when someone sneezes; to make a toast, people say Prost!'), 'neutral'),
    E('schoenen-tag', 'Schönen Tag noch!', ('bonne journée !', 'have a nice day!'), ('La formule des commerçants en fin d’échange. Réponse : Danke, gleichfalls! (merci, pareillement).', 'What shopkeepers say at the end of an exchange. Reply: Danke, gleichfalls! (thanks, same to you).'), 'polite', ('Auf Wiedersehen und schönen Tag noch! — Danke, gleichfalls!', 'Au revoir et bonne journée ! — Merci, pareillement !', 'Goodbye and have a nice day! — Thanks, same to you!')),
  ]),
  TH('de-alltag', '☀', ('Au quotidien', 'Everyday life'), ('Les petits mots qu’on entend partout en Allemagne, à la boulangerie comme au bureau.', 'The little words you hear everywhere in Germany, at the bakery as in the office.'), [
    E('genau', 'Genau!', ('exactement !', 'exactly!'), ('Le mot préféré des Allemands pour dire qu’on est d’accord. On l’entend cent fois par jour.', 'Germans’ favourite word for agreeing. You hear it a hundred times a day.'), 'neutral', ('Wir treffen uns um acht? — Genau!', 'On se retrouve à huit heures ? — Exactement !', 'We’re meeting at eight? — Exactly!')),
    E('na', 'Na?', ('alors, ça va ?', 'well, how’s it going?'), ('Le salut le plus court du monde, entre amis. On peut répondre… Na? ou Na, du?', 'The shortest greeting in the world, between friends. You can answer… Na? or Na, du?'), 'casual'),
    E('doch', 'Doch!', ('si ! (pour contredire une négation)', 'yes it is! (contradicting a negative)'), ('Comme le « si » français : Du kommst nicht? — Doch! (tu ne viens pas ? — Si !).', 'Like French “si”: Du kommst nicht? — Doch! (you’re not coming? — Yes I am!).'), 'neutral'),
    E('feierabend', 'der Feierabend', ('la fin de la journée de travail', 'the end of the working day'), ('Littéralement « soirée de fête ». Schönen Feierabend! = bonne soirée (après le travail).', 'Literally “celebration evening”. Schönen Feierabend! = enjoy your evening (after work).'), 'neutral'),
    E('gemuetlich', 'gemütlich', ('douillet, chaleureux, où l’on se sent bien', 'cosy, warm and relaxed'), ('La Gemütlichkeit est un art de vivre : bougies, coussins, café et gâteau entre amis.', 'Gemütlichkeit is a way of life: candles, cushions, coffee and cake with friends.'), 'neutral'),
    E('kaffee-und-kuchen', 'Kaffee und Kuchen', ('le café-gâteau de l’après-midi', 'afternoon coffee and cake'), ('Le goûter des adultes, vers quinze ou seize heures, surtout le dimanche.', 'The grown-ups’ afternoon tea, around three or four o’clock, especially on Sundays.'), 'neutral'),
  ]),
  TH('de-bilder', '♥', ('Expressions imagées', 'Colourful expressions'), ('Des images surprenantes qu’il ne faut surtout pas traduire mot à mot.', 'Surprising images that must never be translated word for word.'), [
    E('nur-bahnhof', 'Ich verstehe nur Bahnhof.', ('je n’y comprends rien', 'I don’t understand a thing'), ('Littéralement « je ne comprends que gare ».', 'Literally “I only understand railway station”.'), 'casual', ('Kannst du das wiederholen? Ich verstehe nur Bahnhof.', 'Tu peux répéter ? Je n’y comprends rien.', 'Can you repeat that? I don’t understand a thing.')),
    E('daumen-druecken', 'Ich drücke dir die Daumen!', ('je croise les doigts pour toi !', 'I’m keeping my fingers crossed for you!'), ('En allemand, on « presse les pouces » au lieu de croiser les doigts.', 'In German you “press your thumbs” instead of crossing your fingers.'), 'casual'),
    E('tomaten-auf-den-augen', 'Tomaten auf den Augen haben', ('ne pas voir ce qui crève les yeux', 'to fail to see what is obvious'), ('Littéralement « avoir des tomates sur les yeux ».', 'Literally “to have tomatoes on your eyes”.'), 'casual'),
    E('wurst', 'Das ist mir Wurst.', ('ça m’est égal', 'I don’t mind either way'), ('Littéralement « c’est saucisse pour moi ».', 'Literally “that is sausage to me”.'), 'casual'),
    E('schwein-haben', 'Schwein haben', ('avoir de la chance', 'to be lucky'), ('Littéralement « avoir du cochon » : le cochon porte bonheur en Allemagne.', 'Literally “to have pig”: the pig is a lucky charm in Germany.'), 'casual', ('Du hast Schwein gehabt!', 'Tu as eu de la chance !', 'You were lucky!')),
    E('die-nase-voll', 'die Nase voll haben', ('en avoir assez', 'to be fed up'), ('Littéralement « avoir le nez plein ».', 'Literally “to have your nose full”.'), 'casual'),
  ]),
  TH('de-sprichwoerter', '❧', ('Proverbes (Sprichwörter)', 'Proverbs (Sprichwörter)'), ('Les proverbes allemands aiment le travail bien fait et le bon sens paysan ; plusieurs viennent tout droit des contes.', 'German proverbs love a job well done and country common sense; several come straight from the tales.'), [
    E('ende-gut', 'Ende gut, alles gut.', ('tout est bien qui finit bien', 'if it ends well, nothing else matters'), ('La morale de bien des contes des frères Grimm.', 'The moral of many of the Brothers Grimm’s tales.'), 'neutral'),
    E('uebung-macht', 'Übung macht den Meister.', ('c’est en forgeant qu’on devient forgeron', 'you become skilled by practising'), ('Littéralement « l’exercice fait le maître ».', 'Literally “practice makes the master”.'), 'neutral'),
    E('morgenstund', 'Morgenstund hat Gold im Mund.', ('l’avenir appartient à ceux qui se lèvent tôt', 'people who start early succeed'), ('Littéralement « l’heure du matin a de l’or dans la bouche ».', 'Literally “the morning hour has gold in its mouth”.'), 'neutral'),
    E('aller-anfang', 'Aller Anfang ist schwer.', ('il n’y a que le premier pas qui coûte', 'the first step is always the hardest'), ('Littéralement « tout début est difficile » : à se répéter quand on commence l’allemand !', 'Literally “every beginning is hard”: worth repeating when you start German!'), 'neutral'),
    E('wer-a-sagt', 'Wer A sagt, muss auch B sagen.', ('quand le vin est tiré, il faut le boire', 'once you have started, you must go on'), ('Littéralement « qui dit A doit aussi dire B ».', 'Literally “whoever says A must also say B”.'), 'neutral'),
    E('alles-hat-ein-ende', 'Alles hat ein Ende, nur die Wurst hat zwei.', ('tout a une fin (sauf la saucisse, qui en a deux)', 'everything comes to an end (except the sausage, which has two)'), ('Un proverbe humoristique, devenu une chanson célèbre.', 'A humorous proverb that became a famous song.'), 'casual'),
  ]),
]

DATA = {
  'contentVersion': '2026.11.27',
  'language': 'de',
  'notice': t(('Expressions allemandes courantes sélectionnées par Koto Quest (allemand d’Allemagne) ; le registre (poli, familier…) aide à choisir la bonne formule selon la situation.', 'Common German expressions selected by Koto Quest (German as spoken in Germany); the register (polite, casual…) helps you pick the right phrase for the situation.')),
  'themes': THEMES,
}

slugs = [e['slug'] for th in THEMES for e in th['expressions']]
assert len(slugs) == len(set(slugs)), 'slug en double'
json.dump(DATA, open(os.path.join(ROOT, 'content/expressions/expressions-de.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
DICO.update(kq_content.EN)
json.dump(DICO, open(P_DICT, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(f'Expressions allemandes : {len(THEMES)} thèmes, {len(slugs)} expressions')
