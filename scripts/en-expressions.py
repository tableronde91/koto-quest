# Onglet Expressions en anglais (content/expressions/expressions-en.json), français + anglais.
# Formules de politesse, anglais du bureau et du téléphone (thèmes fréquents au TOEIC), verbes à particule, idiomes et proverbes.
# Le sens anglais (pour l'interface en anglais) est une courte définition de l'expression.
# Usage : python3 scripts/en-expressions.py
import json, os, sys
sys.path.insert(0, os.path.dirname(__file__))
from kq_content import ROOT, DICO, EN, P_DICT, t

def E(slug, front, meaning, note, register, example=None):
    it = {'slug': 'enx-' + slug, 'kind': 'vocabulary', 'front': front, 'reading': None, 'romaji': None,
          'meaning': t(meaning), 'note': t(note), 'register': register}
    if example:
        jp, fr, en = example
        it['example'] = {'jp': jp, 'fr': t((fr, en))}
    return it

def TH(slug, glyph, title, description, expressions):
    return {'slug': slug, 'glyph': glyph, 'title': t(title), 'description': t(description), 'expressions': expressions}

THEMES = [
  TH('en-politeness', '☕', ('Politesse britannique', 'British politeness'), ('Les petits mots qui adoucissent tout : en anglais, on remercie et on s’excuse beaucoup.', 'The little words that soften everything: in English, people thank and apologise a lot.'), [
    E('sorry', 'Sorry!', ('pardon ! désolé !', 'apology for a small mistake'), ('Le réflexe britannique : on dit sorry quand on bouscule quelqu’un… et même quand c’est l’autre qui vous bouscule.', 'The British reflex: you say sorry when you bump into someone… and even when they bump into you.'), 'neutral', ('Oh, sorry! — No worries!', 'Oh, pardon ! — Pas de souci !', 'Oh, sorry! — No worries!')),
    E('no-worries', 'No worries.', ('pas de souci', 'no problem at all'), ('Réponse décontractée à un merci ou à une excuse.', 'A relaxed reply to thanks or an apology.'), 'casual'),
    E('cheers', 'Cheers!', ('merci ! ; santé !', 'informal thanks; a toast'), ('Au Royaume-Uni, cheers veut souvent dire merci, en plus de « santé ! ».', 'In the UK, cheers often means thank you, as well as “to your health!”.'), 'casual'),
    E('you-are-welcome', 'You’re welcome.', ('de rien, je vous en prie', 'polite reply to thanks'), ('La réponse standard à thank you. On entend aussi No problem.', 'The standard reply to thank you. You also hear No problem.'), 'polite'),
    E('could-you', 'Could you…, please?', ('pourriez-vous…, s’il vous plaît ?', 'polite way to ask for something'), ('Plus poli que Can you… ? : idéal avec un client ou un inconnu.', 'More polite than Can you…?: ideal with a customer or a stranger.'), 'polite', ('Could you close the door, please?', 'Pourriez-vous fermer la porte, s’il vous plaît ?', 'Could you close the door, please?')),
    E('after-you', 'After you.', ('après vous (je vous en prie)', 'letting someone go first'), ('Pour laisser passer quelqu’un devant soi, à une porte ou dans une file.', 'To let someone go first, at a door or in a queue.'), 'polite'),
  ]),
  TH('en-office', '✉', ('L’anglais du bureau', 'Office English'), ('Réunions, e-mails, délais : les formules qu’on retrouve partout au travail et au TOEIC.', 'Meetings, emails, deadlines: phrases found everywhere at work and in the TOEIC.'), [
    E('please-find-attached', 'Please find attached…', ('veuillez trouver ci-joint…', 'email phrase: a file is attached'), ('Formule classique d’un e-mail professionnel avec une pièce jointe.', 'A classic phrase in a business email with an attachment.'), 'formal', ('Please find attached the report for Monday.', 'Veuillez trouver ci-joint le rapport pour lundi.', 'Please find attached the report for Monday.')),
    E('looking-forward', 'I look forward to hearing from you.', ('dans l’attente de votre réponse', 'formal email ending, waiting for a reply'), ('Pour terminer un e-mail formel. Attention : to + verbe en -ing.', 'To end a formal email. Careful: to + verb in -ing.'), 'formal'),
    E('deadline', 'deadline', ('date limite', 'deadline'), ('Mot clé du monde du travail : The deadline is Friday.', 'A key word at work: The deadline is Friday.'), 'neutral'),
    E('on-time', 'on time', ('à l’heure, dans les temps', 'not late'), ('The train is on time. Attention : in time = à temps (assez tôt).', 'The train is on time. Careful: in time = early enough.'), 'neutral'),
    E('call-back', 'to call someone back', ('rappeler quelqu’un (au téléphone)', 'to phone someone again later'), ('Can I call you back in ten minutes? = je te rappelle dans dix minutes ?', 'Can I call you back in ten minutes?'), 'neutral'),
    E('hold-on', 'Hold on, please.', ('ne quittez pas', 'please wait on the phone'), ('Au téléphone, pour faire patienter quelqu’un.', 'On the phone, to ask someone to wait.'), 'polite'),
    E('out-of-office', 'out of the office', ('absent du bureau', 'not at work today'), ('Le message automatique des absences : I’m out of the office until Monday.', 'The automatic absence message: I’m out of the office until Monday.'), 'neutral'),
  ]),
  TH('en-phrasal', '↗', ('Verbes à particule', 'Phrasal verbs'), ('Un verbe + une petite particule = un nouveau sens. Les anglophones les utilisent sans arrêt.', 'A verb + a small particle = a new meaning. English speakers use them all the time.'), [
    E('get-on', 'to get on (a bus)', ('monter (dans un bus, un train)', 'to enter a bus or train'), ('get off = descendre. Get on the bus at Victoria, get off at Oxford Street.', 'get off = to leave the vehicle. Get on the bus at Victoria, get off at Oxford Street.'), 'neutral'),
    E('turn-on', 'to turn on', ('allumer (un appareil)', 'to start a machine or light'), ('Contraire : turn off (éteindre). Turn off your phone, please.', 'Opposite: turn off. Turn off your phone, please.'), 'neutral'),
    E('look-for', 'to look for', ('chercher', 'to try to find'), ('I’m looking for my keys. À ne pas confondre avec look at (regarder).', 'I’m looking for my keys. Not to be confused with look at.'), 'neutral'),
    E('fill-in', 'to fill in (a form)', ('remplir (un formulaire)', 'to complete a form'), ('Please fill in this form. Très fréquent à l’accueil et au TOEIC.', 'Please fill in this form. Very common at reception and in the TOEIC.'), 'neutral'),
    E('find-out', 'to find out', ('découvrir, se renseigner', 'to get information about something'), ('Can you find out the time of the meeting?', 'Can you find out the time of the meeting?'), 'neutral'),
    E('give-up', 'to give up', ('abandonner, arrêter', 'to stop trying'), ('Don’t give up! = n’abandonne pas ! Aussi : give up smoking (arrêter de fumer).', 'Don’t give up! Also: give up smoking.'), 'neutral'),
  ]),
  TH('en-idioms', '☂', ('Idiomes imagés', 'Colourful idioms'), ('Des images surprenantes qu’il ne faut surtout pas traduire mot à mot.', 'Surprising images that must never be translated word for word.'), [
    E('cats-and-dogs', 'It’s raining cats and dogs.', ('il pleut des cordes', 'it is raining very hard'), ('Littéralement « il pleut des chats et des chiens » : très britannique… et très utile.', 'Literally “cats and dogs are falling”: very British… and very useful.'), 'casual'),
    E('piece-of-cake', 'a piece of cake', ('un jeu d’enfant, du gâteau', 'something very easy'), ('The test was a piece of cake! = l’examen était super facile !', 'The test was a piece of cake! = the test was very easy!'), 'casual'),
    E('break-the-ice', 'to break the ice', ('briser la glace', 'to make people feel relaxed at a first meeting'), ('Comme en français : détendre l’atmosphère au début d’une rencontre.', 'As in French: to relax the atmosphere at the start of a meeting.'), 'neutral'),
    E('under-the-weather', 'under the weather', ('patraque, pas très en forme', 'a little ill'), ('I’m feeling a bit under the weather today.', 'I’m feeling a bit under the weather today.'), 'casual'),
    E('cup-of-tea', 'not my cup of tea', ('pas mon truc', 'not something I like'), ('Football isn’t really my cup of tea. Une façon polie de dire qu’on n’aime pas.', 'Football isn’t really my cup of tea. A polite way to say you don’t like something.'), 'casual'),
    E('cost-an-arm', 'to cost an arm and a leg', ('coûter les yeux de la tête', 'to be very expensive'), ('En anglais, ça coûte « un bras et une jambe » plutôt que les yeux.', 'In English it costs “an arm and a leg” rather than your eyes.'), 'casual'),
  ]),
  TH('en-proverbs', '❦', ('Proverbes', 'Proverbs'), ('Des proverbes anglais et leur équivalent français, parfois très proche, parfois très différent.', 'English proverbs and their French equivalent, sometimes very close, sometimes very different.'), [
    E('practice-perfect', 'Practice makes perfect.', ('c’est en forgeant qu’on devient forgeron', 'you improve by doing something often'), ('La devise de tout apprenant : un peu chaque jour !', 'The motto of every learner: a little every day!'), 'neutral'),
    E('early-bird', 'The early bird catches the worm.', ('l’avenir appartient à ceux qui se lèvent tôt', 'people who start early succeed'), ('Littéralement « l’oiseau matinal attrape le ver ».', 'Literally “the early bird catches the worm”.'), 'neutral'),
    E('when-in-rome', 'When in Rome, do as the Romans do.', ('à Rome, fais comme les Romains', 'follow local customs when you travel'), ('Le même proverbe existe en français.', 'The same proverb exists in French.'), 'neutral'),
    E('better-late', 'Better late than never.', ('mieux vaut tard que jamais', 'it is good to do something even if it is late'), ('Pour accueillir quelqu’un en retard… avec le sourire.', 'To welcome someone who is late… with a smile.'), 'neutral'),
    E('actions-louder', 'Actions speak louder than words.', ('les actes valent mieux que les paroles', 'what you do matters more than what you say'), ('Ce qu’on fait compte plus que ce qu’on promet.', 'What you do counts more than what you promise.'), 'neutral'),
    E('dont-judge', 'Don’t judge a book by its cover.', ('l’habit ne fait pas le moine', 'don’t judge people by their appearance'), ('Littéralement « ne juge pas un livre à sa couverture ».', 'Literally “don’t judge a book by its cover”.'), 'neutral'),
  ]),
]

DATA = {
  'contentVersion': '2026.11.22',
  'language': 'en',
  'notice': t(('Expressions anglaises courantes sélectionnées par Koto Quest ; le registre (poli, familier…) aide à choisir la bonne formule selon la situation, au bureau comme au TOEIC.', 'Common English expressions selected by Koto Quest; the register (polite, casual…) helps you choose the right phrase for the situation, at work as in the TOEIC.')),
  'themes': THEMES,
}

for fr, en in EN.items():
    if fr in DICO and DICO[fr] != en:
        raise SystemExit(f'traduction existante différente : {fr} → {DICO[fr]} / {en}')
slugs = [e['slug'] for th in THEMES for e in th['expressions']]
assert len(slugs) == len(set(slugs)), 'slug en double'
json.dump(DATA, open(os.path.join(ROOT, 'content/expressions/expressions-en.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
DICO.update(EN)
json.dump(DICO, open(P_DICT, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(f'Expressions anglaises : {len(THEMES)} thèmes, {len(slugs)} expressions')
