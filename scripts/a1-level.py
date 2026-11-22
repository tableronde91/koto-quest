# Niveau A1 (anglais, CECRL A1, préparation au TOEIC) : 8 îles, 22 leçons et un examen blanc TOEIC (français + anglais).
# Mode histoire : l'apprenti·e de Merlin, embauché·e chez Avalon & Co. à Londres, apaise les créatures des légendes britanniques.
# Les notions sont en anglais (front) avec leur sens en français ; la traduction anglaise du sens sert à l'interface en anglais.
# Usage : python3 scripts/a1-level.py   (réécrit content/a1/a1.json)
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from kq_content import *

REGION = 'Royaume d’Albion'

def E(slug, front, meaning):
    """Mot ou expression anglaise (pas de lecture ni de romaji)."""
    return V('en-' + slug, front, None, None, meaning)

def EG(slug, front, meaning):
    return G('gram-en-' + slug, front, None, None, meaning)

def x(en, fr, en_tr):
    """Exemple : phrase anglaise, traduction française (et sa version anglaise pour l'interface)."""
    return ex(en, None, fr, en_tr)

COMPLETE = ('Complète la phrase.', 'Complete the sentence.')
CHOOSE = ('Choisis la forme qui convient.', 'Choose the right form.')
ANSWER = ('Que réponds-tu ?', 'What do you answer?')

def order(fr_en, words, expl):
    return SO(fr_en, words, expl)

# ═════════════════════════ Île 1 : Hello, London! ═════════════════════════
W1 = WORLD('a1-w1', ('Hello, London !', 'Hello, London!'), REGION,
  ('Saluer, se présenter, épeler son nom et compter jusqu’à vingt : le verbe be au présent.', 'Greet people, introduce yourself, spell your name and count to twenty: the verb be in the present.'),
  (('Le Boggart farceur', 'The Prankster Boggart'), 'B', ('Ce lutin des maisons anglaises cache les badges et mélange les noms à l’accueil d’Avalon & Co. Présente-toi sans faute pour qu’il te rende le tien !', 'This house goblin from English homes hides badges and mixes up names at the Avalon & Co. reception. Introduce yourself without a mistake and he will give yours back!')),
  [CH('a1-w1-c1', ('Premiers mots', 'First words'), [
    L('en-hello', ('Bonjour ! Saluer et prendre congé', 'Hello! Greeting and saying goodbye'), ('Saluer quelqu’un, demander comment il va et dire au revoir.', 'Greet someone, ask how they are and say goodbye.'), 7, [
        ('Hello est le bonjour de tous les jours ; Hi est plus familier. Le matin, on dit aussi Good morning, l’après-midi Good afternoon, le soir Good evening.', 'Hello is the everyday greeting; Hi is more casual. In the morning you also say Good morning, in the afternoon Good afternoon, in the evening Good evening.'),
        ('How are you? (Comment vas-tu ?) appelle une réponse courte : I’m fine, thank you. And you?', 'How are you? calls for a short answer: I’m fine, thank you. And you?'),
        ('Pour partir : Goodbye, ou plus simplement Bye. See you! = à plus tard. Attention : Good night ne sert qu’à souhaiter une bonne nuit.', 'When leaving: Goodbye, or simply Bye. See you! = see you later. Careful: Good night is only used to wish someone a good night.'),
      ], [
        E('hello', 'hello', ('bonjour', 'hello')),
        E('good-morning', 'good morning', ('bonjour (le matin)', 'good morning')),
        E('good-evening', 'good evening', ('bonsoir', 'good evening')),
        E('how-are-you', 'How are you?', ('Comment vas-tu ?', 'How are you?')),
        E('fine', 'fine', ('bien (en forme)', 'fine, well')),
        E('thank-you', 'thank you', ('merci', 'thank you')),
        E('goodbye', 'goodbye', ('au revoir', 'goodbye')),
      ], [
        x('Good morning, Mr Ambrose! — Good morning! How are you?', 'Bonjour, monsieur Ambrose ! — Bonjour ! Comment allez-vous ?', 'Good morning, Mr Ambrose! — Good morning! How are you?'),
        x('I’m fine, thank you. And you?', 'Je vais bien, merci. Et vous ?', 'I’m fine, thank you. And you?'),
      ], [
        DC(ANSWER, [('Mr Ambrose', 'How are you?')], ('M. Ambrose te demande comment tu vas.', 'Mr Ambrose asks how you are.'), ['I’m fine, thank you.', 'Good night!', 'I’m Emma.'], 'I’m fine, thank you.', ('À How are you?, on répond I’m fine, thank you.', 'You answer How are you? with I’m fine, thank you.')),
        FB(COMPLETE, 'It’s 9 a.m. Good ＿, everyone!', ['morning', 'night', 'evening'], 'morning', ('À 9 heures du matin : Good morning.', 'At 9 a.m.: Good morning.'), ('Il est 9 heures. Bonjour à tous !', 'It’s 9 a.m. Good morning, everyone!')),
        TF('Goodbye! See you tomorrow.', ('La personne arrive au bureau.', 'The person is arriving at the office.'), FAUX, ('Goodbye = au revoir : la personne s’en va.', 'Goodbye: the person is leaving.')),
        DC(('Tu quittes le bureau à 18 h. Que dis-tu ?', 'You leave the office at 6 p.m. What do you say?'), [('Anna', 'Bye! See you tomorrow!')], ('Anna te dit au revoir.', 'Anna says goodbye to you.'), ['Goodbye, Anna!', 'Good morning, Anna!', 'How are you, Anna?'], 'Goodbye, Anna!', ('On répond à Bye par Goodbye ou Bye.', 'You answer Bye with Goodbye or Bye.')),
      ]),
    L('en-be-i', ('Je suis… : I am, you are', 'I am…: I am, you are'), ('Se présenter avec I am et poser une question avec Are you… ?', 'Introduce yourself with I am and ask a question with Are you…?'), 8, [
        ('Le verbe be (être) : I am (je suis), you are (tu es / vous êtes). À l’oral, on contracte : I’m, you’re.', 'The verb be: I am, you are. In speech they are contracted: I’m, you’re.'),
        ('My name is… ou I’m… pour donner son nom. What’s your name? = comment t’appelles-tu ?', 'My name is… or I’m… to give your name. What’s your name? asks for someone’s name.'),
        ('Question : on inverse le verbe. You are French → Are you French? Réponse courte : Yes, I am. / No, I’m not.', 'Question: swap the verb. You are French → Are you French? Short answer: Yes, I am. / No, I’m not.'),
      ], [
        EG('i-am', 'I am / you are', ('je suis / tu es (be)', 'I am / you are (be)')),
        E('name', 'name', ('nom, prénom', 'name')),
        E('my', 'my', ('mon, ma, mes', 'my')),
        E('your', 'your', ('ton, ta, tes ; votre, vos', 'your')),
        E('yes', 'yes', ('oui', 'yes')),
        E('no', 'no', ('non', 'no')),
        E('french', 'French', ('français, française', 'French')),
      ], [
        x('Hello, I’m Emma. I’m French. — Nice to meet you, Emma!', 'Bonjour, je suis Emma. Je suis française. — Enchanté, Emma !', 'Hello, I’m Emma. I’m French. — Nice to meet you, Emma!'),
        x('Are you the new intern? — Yes, I am.', 'Tu es le nouveau stagiaire ? — Oui.', 'Are you the new intern? — Yes, I am.'),
      ], [
        FB(COMPLETE, 'Hello! I ＿ Tom.', ['am', 'are', 'is'], 'am', ('Avec I : am.', 'With I: am.'), ('Bonjour ! Je suis Tom.', 'Hello! I am Tom.')),
        FB(COMPLETE, '＿ you French? — Yes, I am.', ['Are', 'Am', 'Is'], 'Are', ('Question avec you : Are you… ?', 'Question with you: Are you…?'), ('Tu es français ? — Oui.', 'Are you French? — Yes, I am.')),
        DC(ANSWER, [('Mr Ambrose', 'What’s your name?')], ('M. Ambrose te demande ton nom.', 'Mr Ambrose asks your name.'), ['My name is Emma.', 'I’m fine.', 'Yes, I am.'], 'My name is Emma.', ('What’s your name? → My name is…', 'What’s your name? → My name is…')),
        order(('Remets dans l’ordre : « Je m’appelle Sam. »', 'Put in order: “My name is Sam.”'), ['My', 'name', 'is', 'Sam.'], ('My name is + prénom.', 'My name is + first name.')),
      ]),
  ]),
  CH('a1-w1-c2', ('Lettres et nombres', 'Letters and numbers'), [
    L('en-spell', ('Épeler et compter jusqu’à 10', 'Spelling and counting to 10'), ('Épeler son nom et dire les nombres de 0 à 10.', 'Spell your name and say the numbers from 0 to 10.'), 8, [
        ('Au téléphone ou à l’accueil, on demande souvent : How do you spell that? (Comment ça s’écrit ?). Attention aux lettres piège : A se dit « eï », E « i », I « aï ».', 'On the phone or at reception you are often asked: How do you spell that? Watch the tricky letters: A sounds like “ay”, E like “ee”, I like “eye”.'),
        ('Les nombres : zero (ou « oh » dans un numéro de téléphone), one, two, three, four, five, six, seven, eight, nine, ten.', 'The numbers: zero (or “oh” in a phone number), one, two, three, four, five, six, seven, eight, nine, ten.'),
        ('Un numéro se lit chiffre par chiffre : 07 52 → oh seven five two. Deux chiffres pareils : double five (55).', 'A phone number is read digit by digit: 07 52 → oh seven five two. Two identical digits: double five (55).'),
      ], [
        E('spell', 'to spell', ('épeler', 'to spell')),
        E('one', 'one', ('un (1)', 'one (1)')),
        E('two', 'two', ('deux (2)', 'two (2)')),
        E('three', 'three', ('trois (3)', 'three (3)')),
        E('five', 'five', ('cinq (5)', 'five (5)')),
        E('eight', 'eight', ('huit (8)', 'eight (8)')),
        E('ten', 'ten', ('dix (10)', 'ten (10)')),
        E('phone-number', 'phone number', ('numéro de téléphone', 'phone number')),
      ], [
        x('How do you spell your name? — M-A-R-T-I-N.', 'Comment s’écrit ton nom ? — M-A-R-T-I-N.', 'How do you spell your name? — M-A-R-T-I-N.'),
        x('My phone number is oh seven, double five, three, eight.', 'Mon numéro est le 07 55 38.', 'My phone number is 07 55 38.'),
      ], [
        FB(COMPLETE, 'Three + five = ＿', ['eight', 'seven', 'ten'], 'eight', ('3 + 5 = 8 : eight.', '3 + 5 = 8: eight.'), ('Trois plus cinq égale huit.', 'Three plus five equals eight.')),
        DC(ANSWER, [('Receptionist', 'How do you spell your name?')], ('La réceptionniste te demande d’épeler ton nom.', 'The receptionist asks you to spell your name.'), ['E-M-M-A.', 'I’m fine.', 'Ten.'], 'E-M-M-A.', ('How do you spell…? → on épelle lettre par lettre.', 'How do you spell…? → spell it letter by letter.')),
        TF('My phone number is double two, five, one.', ('Le numéro commence par 22.', 'The number starts with 22.'), VRAI, ('double two = 22.', 'double two = 22.')),
        FB(COMPLETE, 'Ten − eight = ＿', ['two', 'three', 'one'], 'two', ('10 − 8 = 2 : two.', '10 − 8 = 2: two.'), ('Dix moins huit égale deux.', 'Ten minus eight equals two.')),
      ]),
    L('en-be-he', ('Il est, elle est : he is, she is, it is', 'He is, she is, it is'), ('Présenter quelqu’un avec he / she is et compter jusqu’à 20.', 'Introduce someone with he / she is and count to 20.'), 9, [
        ('He is (il est) pour un homme, she is (elle est) pour une femme, it is pour une chose ou un animal. Contractions : he’s, she’s, it’s.', 'He is for a man, she is for a woman, it is for a thing or an animal. Contractions: he’s, she’s, it’s.'),
        ('Négation : is not → isn’t. She isn’t English, she’s Irish. Question : Is he your manager?', 'Negative: is not → isn’t. She isn’t English, she’s Irish. Question: Is he your manager?'),
        ('De 11 à 20 : eleven, twelve, thirteen, fourteen, fifteen, sixteen, seventeen, eighteen, nineteen, twenty. -teen = 13 à 19.', 'From 11 to 20: eleven, twelve, thirteen, fourteen, fifteen, sixteen, seventeen, eighteen, nineteen, twenty. -teen = 13 to 19.'),
      ], [
        EG('he-is', 'he is / she is / it is', ('il est / elle est (be)', 'he is / she is / it is (be)')),
        EG('isnt', 'isn’t', ('n’est pas (is not)', 'is not')),
        E('he', 'he', ('il (homme)', 'he (pronoun)')),
        E('she', 'she', ('elle (femme)', 'she')),
        E('twelve', 'twelve', ('douze (12)', 'twelve (12)')),
        E('fifteen', 'fifteen', ('quinze (15)', 'fifteen (15)')),
        E('twenty', 'twenty', ('vingt (20)', 'twenty (20)')),
        E('english', 'English', ('anglais, anglaise', 'English')),
      ], [
        x('This is Anna. She’s from Dublin. She isn’t English, she’s Irish.', 'Voici Anna. Elle vient de Dublin. Elle n’est pas anglaise, elle est irlandaise.', 'This is Anna. She’s from Dublin. She isn’t English, she’s Irish.'),
        x('The meeting room is on floor twelve.', 'La salle de réunion est au douzième étage.', 'The meeting room is on floor twelve.'),
      ], [
        FB(COMPLETE, 'This is Mr Ambrose. ＿ is our manager.', ['He', 'She', 'It'], 'He', ('Mr = monsieur : he.', 'Mr = a man: he.'), ('Voici M. Ambrose. C’est notre responsable.', 'This is Mr Ambrose. He is our manager.')),
        FB(COMPLETE, 'Anna ＿ Irish.', ['is', 'are', 'am'], 'is', ('Avec une personne (she) : is.', 'With one person (she): is.'), ('Anna est irlandaise.', 'Anna is Irish.')),
        FB(CHOOSE, 'He ＿ English, he’s Scottish.', ['isn’t', 'aren’t', 'not'], 'isn’t', ('Négation de is : isn’t.', 'Negative of is: isn’t.'), ('Il n’est pas anglais, il est écossais.', 'He isn’t English, he’s Scottish.')),
        TF('Twelve + three = fifteen.', ('12 + 3 = 15.', '12 + 3 = 15.'), VRAI, ('twelve (12) + three (3) = fifteen (15).', 'twelve (12) + three (3) = fifteen (15).')),
      ]),
  ])])

# ═════════════════════════ Île 2 : Ma famille et moi ═════════════════════════
W2 = WORLD('a1-w2', ('Ma famille et mes collègues', 'My family and my colleagues'), REGION,
  ('Parler de sa famille, de son métier et de ce que l’on possède : have got, a / an, les possessifs.', 'Talk about your family, your job and what you own: have got, a / an, possessives.'),
  (('Puck le malicieux', 'Puck the Mischief-Maker'), 'P', ('Le lutin de Shakespeare échange les photos de famille sur tous les bureaux. Dis qui est qui, et il remettra chaque cadre à sa place.', 'Shakespeare’s sprite swaps the family photos on every desk. Say who is who, and he will put every frame back in its place.')),
  [CH('a1-w2-c1', ('Qui est-ce ?', 'Who is it?'), [
    L('en-family', ('La famille : his, her, their', 'Family: his, her, their'), ('Présenter sa famille avec les adjectifs possessifs.', 'Introduce your family with possessive adjectives.'), 9, [
        ('Les possessifs dépendent du possesseur : my (je), your (tu/vous), his (à lui), her (à elle), our (nous), their (eux). His sister = la sœur de lui ; her brother = le frère d’elle.', 'Possessives depend on the owner: my, your, his, her, our, their. His sister = the sister of a man; her brother = the brother of a woman.'),
        ('Le possessif ’s : Tom’s mother = la mère de Tom. The manager’s office = le bureau du responsable.', 'The possessive ’s: Tom’s mother. The manager’s office.'),
      ], [
        EG('his-her', 'his / her / their', ('son, sa (à lui / à elle), leur', 'his / her / their (possessive)')),
        EG('apostrophe-s', '’s (Tom’s)', ('de (possession : Tom’s = de Tom)', '’s (possession)')),
        E('mother', 'mother', ('mère', 'mother')),
        E('father', 'father', ('père', 'father')),
        E('sister', 'sister', ('sœur', 'sister')),
        E('brother', 'brother', ('frère', 'brother')),
        E('children', 'children', ('enfants', 'children')),
        E('wife', 'wife', ('épouse, femme', 'wife')),
      ], [
        x('This is my brother Paul and his wife, Emma. Their children are six and nine.', 'Voici mon frère Paul et sa femme, Emma. Leurs enfants ont six et neuf ans.', 'This is my brother Paul and his wife, Emma. Their children are six and nine.'),
        x('Is that Anna’s sister? — Yes, her name is Kate.', 'C’est la sœur d’Anna ? — Oui, elle s’appelle Kate.', 'Is that Anna’s sister? — Yes, her name is Kate.'),
      ], [
        FB(CHOOSE, 'Anna is here with ＿ brother.', ['her', 'his', 'their'], 'her', ('Anna est une femme : her brother.', 'Anna is a woman: her brother.'), ('Anna est là avec son frère.', 'Anna is here with her brother.')),
        FB(CHOOSE, 'Tom and Kate are with ＿ children.', ['their', 'his', 'her'], 'their', ('Deux possesseurs : their.', 'Two owners: their.'), ('Tom et Kate sont avec leurs enfants.', 'Tom and Kate are with their children.')),
        FB(COMPLETE, 'This is ＿ office.', ['Mr Ambrose’s', 'Mr Ambrose', 'of Mr Ambrose'], 'Mr Ambrose’s', ('La possession : nom + ’s.', 'Possession: noun + ’s.'), ('C’est le bureau de M. Ambrose.', 'This is Mr Ambrose’s office.')),
        TF('Paul is my brother. His wife is Emma.', ('Emma est la femme de Paul.', 'Emma is Paul’s wife.'), VRAI, ('His wife = la femme de Paul.', 'His wife = Paul’s wife.')),
      ]),
    L('en-jobs', ('Les métiers : a / an', 'Jobs: a / an'), ('Dire son métier avec l’article a ou an.', 'Say your job with the article a or an.'), 8, [
        ('Pour un métier, l’anglais met toujours un article : I’m an engineer, she’s a teacher (en français : je suis ingénieur, sans article).', 'English always puts an article before a job: I’m an engineer, she’s a teacher.'),
        ('a devant un son consonne (a manager), an devant un son voyelle (an accountant, an hour).', 'a before a consonant sound (a manager), an before a vowel sound (an accountant, an hour).'),
        ('What do you do? = qu’est-ce que tu fais (dans la vie) ?', 'What do you do? asks about someone’s job.'),
      ], [
        EG('a-an', 'a / an', ('un, une (a devant consonne, an devant voyelle)', 'a / an (article)')),
        E('job', 'job', ('travail, emploi', 'job')),
        E('teacher', 'teacher', ('professeur', 'teacher')),
        E('engineer', 'engineer', ('ingénieur', 'engineer')),
        E('nurse', 'nurse', ('infirmier, infirmière', 'nurse')),
        E('manager', 'manager', ('responsable, manager', 'manager')),
        E('intern', 'intern', ('stagiaire', 'intern')),
      ], [
        x('What do you do? — I’m an engineer. And you? — I’m a nurse.', 'Tu fais quoi dans la vie ? — Je suis ingénieur. Et toi ? — Je suis infirmière.', 'What do you do? — I’m an engineer. And you? — I’m a nurse.'),
        x('Emma is an intern at Avalon & Co.', 'Emma est stagiaire chez Avalon & Co.', 'Emma is an intern at Avalon & Co.'),
      ], [
        FB(CHOOSE, 'She’s ＿ engineer.', ['an', 'a', '—'], 'an', ('engineer commence par un son voyelle : an.', 'engineer starts with a vowel sound: an.'), ('Elle est ingénieure.', 'She’s an engineer.')),
        FB(CHOOSE, 'I’m ＿ teacher.', ['a', 'an', '—'], 'a', ('teacher commence par une consonne : a.', 'teacher starts with a consonant: a.'), ('Je suis professeur.', 'I’m a teacher.')),
        DC(ANSWER, [('Kate', 'What do you do?')], ('Kate te demande ton métier.', 'Kate asks about your job.'), ['I’m an intern.', 'I’m fine.', 'I’m twenty.'], 'I’m an intern.', ('What do you do? → I’m a / an + métier.', 'What do you do? → I’m a / an + job.')),
        TF('Tom is a nurse.', ('Tom est infirmier.', 'Tom is a nurse.'), VRAI, ('nurse = infirmier.', 'nurse = someone who looks after patients.')),
      ]),
  ]),
  CH('a1-w2-c2', ('Ce que j’ai', 'What I have'), [
    L('en-have-got', ('Avoir : have got / has got', 'Having: have got / has got'), ('Dire ce que l’on a avec have got et has got.', 'Say what you have with have got and has got.'), 9, [
        ('En anglais britannique, avoir = have got : I’ve got a car, you’ve got a cat. Avec he / she / it : has got (he’s got).', 'In British English, possession is often expressed with have got: I’ve got a car, you’ve got a cat. With he / she / it: has got (he’s got).'),
        ('Négation : haven’t got / hasn’t got. Question : Have you got a pen? — Yes, I have. / No, I haven’t.', 'Negative: haven’t got / hasn’t got. Question: Have you got a pen? — Yes, I have. / No, I haven’t.'),
        ('L’âge se dit avec be, pas avec have : I’m twenty (j’ai vingt ans).', 'Age uses be, not have: I’m twenty.'),
      ], [
        EG('have-got', 'have got / has got', ('avoir (posséder)', 'have got (possession)')),
        E('car', 'car', ('voiture', 'car')),
        E('cat', 'cat', ('chat', 'cat')),
        E('dog', 'dog', ('chien', 'dog')),
        E('pen', 'pen', ('stylo', 'pen')),
        E('laptop', 'laptop', ('ordinateur portable', 'laptop')),
        E('old', 'old', ('vieux ; âgé (âge)', 'old')),
      ], [
        x('Have you got a pen? — Yes, I have. Here you are.', 'Tu as un stylo ? — Oui. Tiens.', 'Have you got a pen? — Yes, I have. Here you are.'),
        x('Kate has got two cats and a dog. She’s thirty years old.', 'Kate a deux chats et un chien. Elle a trente ans.', 'Kate has got two cats and a dog. She’s thirty years old.'),
      ], [
        FB(CHOOSE, 'Tom ＿ got a new laptop.', ['has', 'have', 'is'], 'has', ('Avec he (Tom) : has got.', 'With he (Tom): has got.'), ('Tom a un nouvel ordinateur portable.', 'Tom has got a new laptop.')),
        FB(CHOOSE, '＿ you got a car?', ['Have', 'Has', 'Are'], 'Have', ('Question avec you : Have you got… ?', 'Question with you: Have you got…?'), ('Tu as une voiture ?', 'Have you got a car?')),
        FB(CHOOSE, 'I ＿ twenty-five.', ['am', 'have', 'have got'], 'am', ('L’âge se dit avec be : I’m 25.', 'Age uses be: I’m 25.'), ('J’ai vingt-cinq ans.', 'I am twenty-five.')),
        DC(ANSWER, [('Anna', 'Have you got a pen?')], ('Anna te demande un stylo.', 'Anna asks you for a pen.'), ['Yes, I have. Here you are.', 'Yes, I am.', 'Yes, it is.'], 'Yes, I have. Here you are.', ('Have you got…? → Yes, I have. / No, I haven’t.', 'Have you got…? → Yes, I have. / No, I haven’t.')),
      ]),
  ])])

# ═════════════════════════ Île 3 : Au bureau ═════════════════════════
W3 = WORLD('a1-w3', ('Les couloirs d’Avalon & Co.', 'The corridors of Avalon & Co.'), REGION,
  ('Décrire le bureau et trouver les objets : there is / there are, les prépositions de lieu, this / that, les pluriels.', 'Describe the office and find things: there is / there are, prepositions of place, this / that, plurals.'),
  (('Le Feu follet', 'The Will-o’-the-Wisp'), 'W', ('Cette petite flamme bleue égare les visiteurs dans les couloirs. Décris exactement où se trouvent les choses pour qu’elle te montre la bonne porte.', 'This little blue flame leads visitors astray in the corridors. Describe exactly where things are and it will show you the right door.')),
  [CH('a1-w3-c1', ('Dans la pièce', 'In the room'), [
    L('en-there-is', ('Il y a : there is, there are', 'There is, there are'), ('Dire ce qu’il y a dans une pièce, au singulier et au pluriel.', 'Say what there is in a room, in the singular and the plural.'), 9, [
        ('There is (there’s) + un seul objet ; there are + plusieurs : There’s a printer. There are two desks.', 'There is (there’s) + one thing; there are + several: There’s a printer. There are two desks.'),
        ('Le pluriel ajoute -s (desk → desks), -es après s, sh, ch, x (box → boxes). Quelques irréguliers : person → people, man → men, woman → women.', 'The plural adds -s (desk → desks), -es after s, sh, ch, x (box → boxes). Some irregular ones: person → people, man → men, woman → women.'),
        ('Question : Is there a coffee machine? Are there any chairs?', 'Question: Is there a coffee machine? Are there any chairs?'),
      ], [
        EG('there-is', 'there is / there are', ('il y a', 'there is / there are')),
        EG('plural-s', 'plural -s / -es (desks, boxes)', ('pluriel des noms (desks, boxes)', 'plural nouns (-s / -es)')),
        E('desk', 'desk', ('bureau (meuble)', 'desk')),
        E('chair', 'chair', ('chaise', 'chair')),
        E('printer', 'printer', ('imprimante', 'printer')),
        E('window', 'window', ('fenêtre', 'window')),
        E('people', 'people', ('gens, personnes', 'people')),
        E('meeting-room', 'meeting room', ('salle de réunion', 'meeting room')),
      ], [
        x('There’s a printer next to the window, and there are four desks.', 'Il y a une imprimante à côté de la fenêtre, et il y a quatre bureaux.', 'There’s a printer next to the window, and there are four desks.'),
        x('Is there a meeting room on this floor? — Yes, there is.', 'Il y a une salle de réunion à cet étage ? — Oui.', 'Is there a meeting room on this floor? — Yes, there is.'),
      ], [
        FB(CHOOSE, 'There ＿ three chairs in the room.', ['are', 'is', 'am'], 'are', ('Plusieurs chaises : there are.', 'Several chairs: there are.'), ('Il y a trois chaises dans la pièce.', 'There are three chairs in the room.')),
        FB(CHOOSE, 'There ＿ a printer on the desk.', ['is', 'are', 'have'], 'is', ('Une seule imprimante : there is.', 'One printer: there is.'), ('Il y a une imprimante sur le bureau.', 'There is a printer on the desk.')),
        FB(CHOOSE, 'There are ten ＿ in the meeting room.', ['people', 'peoples', 'person'], 'people', ('Pluriel de person : people.', 'Plural of person: people.'), ('Il y a dix personnes dans la salle de réunion.', 'There are ten people in the meeting room.')),
        TF('There are two windows in my office.', ('Il y a une seule fenêtre dans le bureau.', 'There is only one window in the office.'), FAUX, ('two windows = deux fenêtres.', 'two windows = more than one.')),
      ]),
    L('en-where', ('Où est… ? in, on, under, next to', 'Where is…? in, on, under, next to'), ('Situer un objet avec les prépositions de lieu.', 'Locate an object with prepositions of place.'), 8, [
        ('in = dans, on = sur, under = sous, next to = à côté de, behind = derrière, in front of = devant, between = entre.', 'in, on, under, next to, behind, in front of, between: the main prepositions of place.'),
        ('Where’s my phone? — It’s on your desk, next to the laptop.', 'Where’s my phone? — It’s on your desk, next to the laptop.'),
      ], [
        EG('prep-place', 'in / on / under / next to', ('dans / sur / sous / à côté de', 'in / on / under / next to (place)')),
        E('where', 'where', ('où', 'where')),
        E('behind', 'behind', ('derrière', 'behind')),
        E('between', 'between', ('entre', 'between')),
        E('key', 'key', ('clé', 'key')),
        E('bag', 'bag', ('sac', 'bag')),
        E('door', 'door', ('porte', 'door')),
      ], [
        x('Where are my keys? — They’re in your bag, under the folder.', 'Où sont mes clés ? — Elles sont dans ton sac, sous le classeur.', 'Where are my keys? — They’re in your bag, under the folder.'),
        x('The coffee machine is between the kitchen and the meeting room.', 'La machine à café est entre la cuisine et la salle de réunion.', 'The coffee machine is between the kitchen and the meeting room.'),
      ], [
        FB(CHOOSE, 'The phone is ＿ the desk.', ['on', 'at', 'between'], 'on', ('sur = on.', 'on top of something: on.'), ('Le téléphone est sur le bureau.', 'The phone is on the desk.')),
        FB(CHOOSE, 'The keys are ＿ my bag.', ['in', 'at', 'between'], 'in', ('dans = in.', 'inside something: in.'), ('Les clés sont dans mon sac.', 'The keys are in my bag.')),
        DC(ANSWER, [('Tom', 'Where’s the meeting room?')], ('Tom cherche la salle de réunion.', 'Tom is looking for the meeting room.'), ['It’s next to the kitchen.', 'It’s ten o’clock.', 'Yes, there is.'], 'It’s next to the kitchen.', ('Where…? → on répond avec un lieu.', 'Where…? → answer with a place.')),
        TF('The cat is under the chair.', ('Le chat est sur la chaise.', 'The cat is on the chair.'), FAUX, ('under = sous.', 'under = below.')),
      ]),
  ]),
  CH('a1-w3-c2', ('Ceci et cela', 'This and that'), [
    L('en-this-that', ('Ceci, cela : this, that, these, those', 'This, that, these, those'), ('Désigner ce qui est proche ou loin, au singulier et au pluriel.', 'Point to what is near or far, in the singular and the plural.'), 8, [
        ('this (près, singulier), these (près, pluriel), that (loin, singulier), those (loin, pluriel).', 'this (near, singular), these (near, plural), that (far, singular), those (far, plural).'),
        ('Is this your coffee? — No, that’s my coffee, over there. What’s this? = qu’est-ce que c’est ?', 'Is this your coffee? — No, that’s my coffee, over there. What’s this? asks what something is.'),
      ], [
        EG('this-that', 'this / that / these / those', ('ce…ci, ce…là (démonstratifs)', 'this / that / these / those')),
        E('folder', 'folder', ('classeur, dossier', 'folder')),
        E('notebook', 'notebook', ('carnet', 'notebook')),
        E('umbrella', 'umbrella', ('parapluie', 'umbrella')),
        E('glasses', 'glasses', ('lunettes', 'glasses')),
        E('mine', 'mine', ('le mien, la mienne', 'mine')),
      ], [
        x('Are these your glasses? — No, those are my glasses, on the table.', 'Ce sont tes lunettes ? — Non, mes lunettes sont là-bas, sur la table.', 'Are these your glasses? — No, those are my glasses, on the table.'),
        x('Is this umbrella yours? — Yes, it’s mine. Thanks!', 'Ce parapluie est à toi ? — Oui, c’est le mien. Merci !', 'Is this umbrella yours? — Yes, it’s mine. Thanks!'),
      ], [
        FB(CHOOSE, '＿ folders here are for the meeting.', ['These', 'This', 'That'], 'These', ('Près et pluriel : these.', 'Near and plural: these.'), ('Ces classeurs-ci sont pour la réunion.', 'These folders here are for the meeting.')),
        FB(CHOOSE, 'Look at ＿ building over there!', ['that', 'these', 'those'], 'that', ('Loin et singulier : that.', 'Far and singular: that.'), ('Regarde ce bâtiment là-bas !', 'Look at that building over there!')),
        DC(ANSWER, [('Anna', 'Is this notebook yours?')], ('Anna te montre un carnet.', 'Anna shows you a notebook.'), ['Yes, it’s mine. Thank you!', 'Yes, I’m fine.', 'Yes, there are.'], 'Yes, it’s mine. Thank you!', ('Is this yours? → Yes, it’s mine.', 'Is this yours? → Yes, it’s mine.')),
        order(('Remets dans l’ordre : « Ce sont mes clés ? »', 'Put in order: “Are these my keys?”'), ['Are', 'these', 'my', 'keys?'], ('Question : Are + these + nom ?', 'Question: Are + these + noun?')),
      ]),
  ])])

# ═════════════════════════ Île 4 : Une journée type ═════════════════════════
W4 = WORLD('a1-w4', ('Une journée à Londres', 'A day in London'), REGION,
  ('Raconter ses habitudes, dire l’heure et les jours : le présent simple et ses questions.', 'Talk about your habits, tell the time and the days: the present simple and its questions.'),
  (('Black Shuck, le chien noir', 'Black Shuck, the Black Dog'), 'S', ('Le grand chien fantôme du Norfolk rôde à la tombée de la nuit et dérègle toutes les horloges. Dis-lui l’heure juste et raconte ta journée pour qu’il retourne dans la lande.', 'The great ghost dog of Norfolk prowls at nightfall and throws every clock out of time. Tell him the right time and describe your day, and he will go back to the moor.')),
  [CH('a1-w4-c1', ('Mes habitudes', 'My habits'), [
    L('en-present-simple', ('Le présent simple : I work, she works', 'The present simple: I work, she works'), ('Parler de ses habitudes et de son travail au présent simple.', 'Talk about your habits and your work in the present simple.'), 10, [
        ('Le présent simple sert aux habitudes et aux vérités générales : I work in London. I drink tea every morning.', 'The present simple is used for habits and general truths: I work in London. I drink tea every morning.'),
        ('Avec he / she / it, on ajoute -s : she works, he drinks. -es après o, s, sh, ch : he goes, she watches. have → has.', 'With he / she / it, add -s: she works, he drinks. -es after o, s, sh, ch: he goes, she watches. have → has.'),
        ('Mots de fréquence avant le verbe : always (toujours), usually (d’habitude), sometimes (parfois), never (jamais).', 'Frequency words go before the verb: always, usually, sometimes, never.'),
      ], [
        EG('present-simple', 'present simple (he works)', ('présent des habitudes (-s à la 3e personne)', 'present simple (-s with he / she / it)')),
        E('work', 'to work', ('travailler', 'to work')),
        E('live', 'to live', ('vivre, habiter', 'to live')),
        E('drink', 'to drink', ('boire', 'to drink')),
        E('get-up', 'to get up', ('se lever', 'to get up')),
        E('usually', 'usually', ('d’habitude', 'usually')),
        E('never', 'never', ('jamais', 'never')),
        E('every-day', 'every day', ('tous les jours', 'every day')),
      ], [
        x('I get up at seven and I usually drink tea. My sister drinks coffee.', 'Je me lève à sept heures et je bois d’habitude du thé. Ma sœur boit du café.', 'I get up at seven and I usually drink tea. My sister drinks coffee.'),
        x('Mr Ambrose lives in Camden and works in the City.', 'M. Ambrose habite à Camden et travaille dans la City.', 'Mr Ambrose lives in Camden and works in the City.'),
      ], [
        FB(CHOOSE, 'She ＿ in a bank.', ['works', 'work', 'working'], 'works', ('he / she / it : verbe + -s.', 'he / she / it: verb + -s.'), ('Elle travaille dans une banque.', 'She works in a bank.')),
        FB(CHOOSE, 'He ＿ to the gym on Mondays.', ['goes', 'gos', 'go'], 'goes', ('go → goes (après o : -es).', 'go → goes (-es after o).'), ('Il va à la salle de sport le lundi.', 'He goes to the gym on Mondays.')),
        FB(CHOOSE, 'I ＿ drink coffee in the evening because I can’t sleep after it.', ['never', 'usually', 'always'], 'never', ('jamais = never.', 'not at any time: never.'), ('Je ne bois jamais de café le soir, car je ne dors plus ensuite.', 'I never drink coffee in the evening because I can’t sleep after it.')),
        order(('Remets dans l’ordre : « Il habite à Londres. »', 'Put in order: “He lives in London.”'), ['He', 'lives', 'in', 'London.'], ('Sujet + verbe en -s + lieu.', 'Subject + verb with -s + place.')),
      ]),
    L('en-do-does', ('Questions et négations : do, does', 'Questions and negatives: do, does'), ('Poser des questions et dire non au présent simple.', 'Ask questions and make negatives in the present simple.'), 10, [
        ('Question : Do you work here? / Does she like tea? Avec does, le verbe perd son -s : Does she like…? (pas likes).', 'Question: Do you work here? / Does she like tea? With does, the verb loses its -s: Does she like…? (not likes).'),
        ('Négation : I don’t (do not) eat meat. He doesn’t (does not) speak French.', 'Negative: I don’t (do not) eat meat. He doesn’t (does not) speak French.'),
        ('Réponses courtes : Yes, I do. / No, she doesn’t.', 'Short answers: Yes, I do. / No, she doesn’t.'),
      ], [
        EG('do-does', 'do / does', ('auxiliaire des questions au présent', 'do / does (questions)')),
        EG('dont-doesnt', 'don’t / doesn’t', ('ne… pas (présent simple)', 'don’t / doesn’t (negative)')),
        E('like', 'to like', ('aimer (bien)', 'to like')),
        E('speak', 'to speak', ('parler', 'to speak')),
        E('eat', 'to eat', ('manger', 'to eat')),
        E('meat', 'meat', ('viande', 'meat')),
        E('weekend', 'weekend', ('week-end', 'weekend')),
      ], [
        x('Do you speak English? — Yes, I do. A little!', 'Tu parles anglais ? — Oui. Un peu !', 'Do you speak English? — Yes, I do. A little!'),
        x('Tom doesn’t work at the weekend.', 'Tom ne travaille pas le week-end.', 'Tom doesn’t work at the weekend.'),
      ], [
        FB(CHOOSE, '＿ she like tea?', ['Does', 'Do', 'Is'], 'Does', ('Question avec she : Does.', 'Question with she: Does.'), ('Est-ce qu’elle aime le thé ?', 'Does she like tea?')),
        FB(CHOOSE, 'I ＿ eat meat. I’m vegetarian.', ['don’t', 'doesn’t', 'not'], 'don’t', ('Négation avec I : don’t.', 'Negative with I: don’t.'), ('Je ne mange pas de viande. Je suis végétarien.', 'I don’t eat meat. I’m vegetarian.')),
        FB(CHOOSE, 'Does he ＿ French?', ['speak', 'speaks', 'speaking'], 'speak', ('Après does : verbe sans -s.', 'After does: verb without -s.'), ('Est-ce qu’il parle français ?', 'Does he speak French?')),
        DC(ANSWER, [('Kate', 'Do you work at the weekend?')], ('Kate te demande si tu travailles le week-end.', 'Kate asks if you work at the weekend.'), ['No, I don’t.', 'No, I’m not.', 'No, it isn’t.'], 'No, I don’t.', ('Do you…? → Yes, I do. / No, I don’t.', 'Do you…? → Yes, I do. / No, I don’t.')),
      ]),
  ]),
  CH('a1-w4-c2', ('L’heure et les jours', 'Time and days'), [
    L('en-time', ('Quelle heure est-il ?', 'What time is it?'), ('Dire et demander l’heure, parler des jours de la semaine.', 'Tell and ask the time, talk about the days of the week.'), 9, [
        ('What time is it? — It’s nine o’clock (9 h), half past nine (9 h 30), quarter past nine (9 h 15), quarter to ten (9 h 45).', 'What time is it? — It’s nine o’clock, half past nine, quarter past nine, quarter to ten.'),
        ('at + heure (at 9 a.m.), on + jour (on Monday), in + moment de la journée (in the morning).', 'at + time (at 9 a.m.), on + day (on Monday), in + part of the day (in the morning).'),
        ('Les jours prennent une majuscule : Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday.', 'Days take a capital letter: Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday.'),
      ], [
        EG('at-on-in', 'at / on / in (time)', ('à (heure) / le (jour) / le, en (moment)', 'at / on / in (time)')),
        E('oclock', 'o’clock', ('heure(s) pile', 'o’clock')),
        E('half-past', 'half past', ('et demie', 'half past')),
        E('quarter', 'quarter', ('quart', 'quarter')),
        E('monday', 'Monday', ('lundi', 'Monday')),
        E('friday', 'Friday', ('vendredi', 'Friday')),
        E('morning', 'morning', ('matin', 'morning')),
      ], [
        x('The meeting is on Monday at half past ten.', 'La réunion est lundi à dix heures et demie.', 'The meeting is on Monday at half past ten.'),
        x('What time is it? — It’s quarter to six. Time to go home!', 'Quelle heure est-il ? — Six heures moins le quart. L’heure de rentrer !', 'What time is it? — It’s quarter to six. Time to go home!'),
      ], [
        FB(CHOOSE, 'The train leaves ＿ 8 o’clock.', ['at', 'on', 'in'], 'at', ('Une heure : at.', 'A clock time: at.'), ('Le train part à 8 heures.', 'The train leaves at 8 o’clock.')),
        FB(CHOOSE, 'I go to the gym ＿ Friday.', ['on', 'at', 'in'], 'on', ('Un jour : on.', 'A day: on.'), ('Je vais à la salle de sport le vendredi.', 'I go to the gym on Friday.')),
        TF('It’s half past seven.', ('Il est 7 h 30.', 'It’s 7:30.'), VRAI, ('half past seven = 7 h 30.', 'half past seven = 7:30.')),
        DC(ANSWER, [('Tom', 'What time is it?')], ('Tom te demande l’heure.', 'Tom asks you the time.'), ['It’s ten o’clock.', 'It’s Monday.', 'It’s on the desk.'], 'It’s ten o’clock.', ('What time…? → It’s + heure.', 'What time…? → It’s + time.')),
      ]),
  ])])

# ═════════════════════════ Île 5 : Au café ═════════════════════════
W5 = WORLD('a1-w5', ('Le café du géant', 'The giant’s café'), REGION,
  ('Commander au café, faire ses courses et parler des prix : some / any, can I have…, how much.', 'Order at a café, go shopping and talk about prices: some / any, can I have…, how much.'),
  (('Cormoran, le géant de Cornouailles', 'Cormoran, the Giant of Cornwall'), 'G', ('Le géant affamé a pris le café du coin et réclame des montagnes de nourriture. Commande poliment et compte juste pour qu’il rende les clés au patron.', 'The hungry giant has taken over the corner café and demands mountains of food. Order politely and count right, and he will give the keys back to the owner.')),
  [CH('a1-w5-c1', ('Commander', 'Ordering'), [
    L('en-can-i-have', ('Je voudrais… : Can I have…? I’d like…', 'Can I have…? I’d like…'), ('Commander poliment au café ou au restaurant.', 'Order politely at a café or restaurant.'), 9, [
        ('Pour commander : Can I have a tea, please? ou, plus poli, I’d like (I would like) a sandwich, please.', 'To order: Can I have a tea, please? or, more politely, I’d like a sandwich, please.'),
        ('Le serveur dit : What would you like? / Anything else? / Here you are. Pour emporter : to take away ; sur place : to eat in.', 'The waiter says: What would you like? / Anything else? / Here you are. To take away or to eat in.'),
        ('Please (s’il vous plaît) et thank you sont indispensables : en anglais, une demande sans please paraît brusque.', 'Please and thank you are essential: in English, a request without please sounds rude.'),
      ], [
        EG('can-i-have', 'Can I have…? / I’d like…', ('je voudrais… (commander poliment)', 'can I have…? / I’d like… (ordering)')),
        E('please', 'please', ('s’il vous plaît', 'please')),
        E('tea', 'tea', ('thé', 'tea')),
        E('coffee', 'coffee', ('café', 'coffee')),
        E('water', 'water', ('eau', 'water')),
        E('sandwich', 'sandwich', ('sandwich', 'sandwich')),
        E('cake', 'cake', ('gâteau', 'cake')),
        E('take-away', 'to take away', ('à emporter', 'to take away')),
      ], [
        x('Hi! Can I have a white coffee and a piece of cake, please? — Sure. To eat in or take away?', 'Bonjour ! Je peux avoir un café au lait et une part de gâteau, s’il vous plaît ? — Bien sûr. Sur place ou à emporter ?', 'Hi! Can I have a white coffee and a piece of cake, please? — Sure. To eat in or take away?'),
        x('I’d like a glass of water, please.', 'Je voudrais un verre d’eau, s’il vous plaît.', 'I’d like a glass of water, please.'),
      ], [
        FB(COMPLETE, 'Can I ＿ a tea, please?', ['have', 'like', 'want to'], 'have', ('Can I have… ? pour commander.', 'Can I have…? to order.'), ('Je peux avoir un thé, s’il vous plaît ?', 'Can I have a tea, please?')),
        FB(COMPLETE, 'I’d ＿ a sandwich, please.', ['like', 'have', 'want'], 'like', ('I’d like = je voudrais.', 'I’d like = polite request.'), ('Je voudrais un sandwich, s’il vous plaît.', 'I’d like a sandwich, please.')),
        DC(ANSWER, [('Waiter', 'What would you like?')], ('Le serveur prend ta commande.', 'The waiter takes your order.'), ['A coffee, please.', 'I’m fine, thanks.', 'It’s on the table.'], 'A coffee, please.', ('What would you like? → ce que tu veux + please.', 'What would you like? → what you want + please.')),
        DC(ANSWER, [('Waiter', 'Anything else?')], ('Le serveur demande si tu veux autre chose.', 'The waiter asks if you want anything else.'), ['No, thank you.', 'Yes, I am.', 'Goodbye, see you.'], 'No, thank you.', ('Anything else? → No, thank you. / Yes, a…', 'Anything else? → No, thank you. / Yes, a…')),
      ]),
    L('en-some-any', ('Du, des : some, any', 'Some and any'), ('Distinguer les noms comptables et indénombrables avec some et any.', 'Tell countable and uncountable nouns apart with some and any.'), 9, [
        ('some (du, des) dans les phrases affirmatives : There’s some milk. I’ve got some apples.', 'some in affirmative sentences: There’s some milk. I’ve got some apples.'),
        ('any dans les questions et les négations : Is there any sugar? There aren’t any eggs.', 'any in questions and negatives: Is there any sugar? There aren’t any eggs.'),
        ('Indénombrables (pas de pluriel) : milk, water, bread, sugar, money, information. On ne dit pas « an information ».', 'Uncountable nouns (no plural): milk, water, bread, sugar, money, information. You don’t say “an information”.'),
      ], [
        EG('some-any', 'some / any', ('du, des (some : affirmation ; any : question, négation)', 'some / any')),
        E('milk', 'milk', ('lait', 'milk')),
        E('bread', 'bread', ('pain', 'bread')),
        E('sugar', 'sugar', ('sucre', 'sugar')),
        E('apple', 'apple', ('pomme', 'apple')),
        E('egg', 'egg', ('œuf', 'egg')),
        E('money', 'money', ('argent', 'money')),
      ], [
        x('Is there any milk in the fridge? — No, there isn’t any. But there’s some juice.', 'Il y a du lait dans le frigo ? — Non, il n’y en a pas. Mais il y a du jus.', 'Is there any milk in the fridge? — No, there isn’t any. But there’s some juice.'),
        x('I need some bread and some eggs.', 'J’ai besoin de pain et d’œufs.', 'I need some bread and some eggs.'),
      ], [
        FB(CHOOSE, 'There’s ＿ sugar on the table.', ['some', 'any', 'a'], 'some', ('Phrase affirmative : some.', 'Affirmative sentence: some.'), ('Il y a du sucre sur la table.', 'There’s some sugar on the table.')),
        FB(CHOOSE, 'Are there ＿ eggs?', ['any', 'some', 'a'], 'any', ('Question : any.', 'Question: any.'), ('Il y a des œufs ?', 'Are there any eggs?')),
        FB(CHOOSE, 'We haven’t got ＿ bread.', ['any', 'some', 'a'], 'any', ('Négation : any.', 'Negative: any.'), ('Nous n’avons pas de pain.', 'We haven’t got any bread.')),
        TF('There isn’t any milk.', ('Il reste du lait.', 'There is some milk left.'), FAUX, ('isn’t any = il n’y en a pas.', 'isn’t any = none at all.')),
      ]),
  ]),
  CH('a1-w5-c2', ('Payer', 'Paying'), [
    L('en-how-much', ('C’est combien ? Les prix', 'How much is it? Prices'), ('Demander et comprendre un prix, compter par dizaines.', 'Ask for and understand a price, count in tens.'), 9, [
        ('How much is this? (singulier) / How much are these? (pluriel). It’s £4.50 se dit « four pounds fifty ».', 'How much is this? (singular) / How much are these? (plural). £4.50 is said “four pounds fifty”.'),
        ('Les dizaines : thirty (30), forty (40), fifty (50), sixty, seventy, eighty, ninety, a hundred (100). Attention : thirteen (13) / thirty (30).', 'Tens: thirty, forty, fifty, sixty, seventy, eighty, ninety, a hundred. Careful: thirteen (13) / thirty (30).'),
        ('Pour payer : Can I pay by card? — Yes, of course. / Cash only, sorry.', 'To pay: Can I pay by card? — Yes, of course. / Cash only, sorry.'),
      ], [
        EG('how-much', 'How much is / are…?', ('combien coûte(nt)… ?', 'how much is / are…? (price)')),
        E('price', 'price', ('prix', 'price')),
        E('pound', 'pound (£)', ('livre sterling', 'pound (£)')),
        E('thirty', 'thirty', ('trente (30)', 'thirty (30)')),
        E('fifty', 'fifty', ('cinquante (50)', 'fifty (50)')),
        E('hundred', 'a hundred', ('cent (100)', 'a hundred (100)')),
        E('card', 'card', ('carte (bancaire)', 'card')),
        E('cheap', 'cheap', ('bon marché', 'cheap')),
      ], [
        x('How much are these sandwiches? — They’re three pounds fifty each.', 'Combien coûtent ces sandwichs ? — 3,50 £ chacun.', 'How much are these sandwiches? — They’re £3.50 each.'),
        x('That’s twelve pounds, please. — Can I pay by card? — Of course.', 'Ça fait 12 livres, s’il vous plaît. — Je peux payer par carte ? — Bien sûr.', 'That’s twelve pounds, please. — Can I pay by card? — Of course.'),
      ], [
        FB(CHOOSE, 'How much ＿ these apples?', ['are', 'is', 'do'], 'are', ('Pluriel : How much are… ?', 'Plural: How much are…?'), ('Combien coûtent ces pommes ?', 'How much are these apples?')),
        FB(COMPLETE, 'Fifty + fifty = a ＿', ['hundred', 'thirty', 'fifty'], 'hundred', ('50 + 50 = 100 : a hundred.', '50 + 50 = 100: a hundred.'), ('Cinquante plus cinquante égale cent.', 'Fifty plus fifty equals a hundred.')),
        DC(ANSWER, [('Cashier', 'That’s eight pounds, please.')], ('La caissière t’annonce le total.', 'The cashier tells you the total.'), ['Can I pay by card?', 'I’m eight.', 'Good evening.'], 'Can I pay by card?', ('Pour payer : Can I pay by card?', 'To pay: Can I pay by card?')),
        TF('It’s thirty pounds.', ('C’est 13 £.', 'It’s £13.'), FAUX, ('thirty = 30 ; 13 = thirteen.', 'thirty = 30; 13 = thirteen.')),
      ]),
  ])])

# ═════════════════════════ Île 6 : Se déplacer ═════════════════════════
W6 = WORLD('a1-w6', ('Le grand voyage vers le nord', 'The great journey north'), REGION,
  ('Demander et indiquer son chemin, prendre les transports et dire ce que l’on sait faire : l’impératif, can / can’t.', 'Ask for and give directions, take transport and say what you can do: the imperative, can / can’t.'),
  (('Nessie, le monstre du loch', 'Nessie, the Loch Monster'), 'N', ('Au bord du loch Ness, le monstre fait chavirer les bateaux des voyageurs perdus. Retrouve ton chemin et explique ce que tu sais faire pour qu’elle te laisse traverser.', 'On the shores of Loch Ness, the monster capsizes the boats of lost travellers. Find your way and explain what you can do, and she will let you cross.')),
  [CH('a1-w6-c1', ('Trouver son chemin', 'Finding your way'), [
    L('en-directions', ('Le chemin : turn left, go straight on', 'Directions: turn left, go straight on'), ('Demander son chemin et le comprendre, à l’impératif.', 'Ask for directions and understand them, in the imperative.'), 9, [
        ('Demander : Excuse me, where’s the station? / How do I get to the museum?', 'Asking: Excuse me, where’s the station? / How do I get to the museum?'),
        ('L’impératif = la base verbale, sans sujet : Turn left (tournez à gauche), Turn right, Go straight on (allez tout droit), Take the second street.', 'The imperative = the base verb, with no subject: Turn left, Turn right, Go straight on, Take the second street.'),
        ('Négation : Don’t turn left! Pour finir : It’s on your left / on your right / opposite the bank (en face de).', 'Negative: Don’t turn left! To finish: It’s on your left / on your right / opposite the bank.'),
      ], [
        EG('imperative', 'imperative (Turn left!)', ('impératif (ordre, consigne)', 'imperative (instructions)')),
        E('excuse-me', 'excuse me', ('excusez-moi', 'excuse me')),
        E('left', 'left', ('gauche', 'left')),
        E('right', 'right', ('droite', 'right')),
        E('straight-on', 'straight on', ('tout droit', 'straight on')),
        E('station', 'station', ('gare', 'station')),
        E('street', 'street', ('rue', 'street')),
        E('opposite', 'opposite', ('en face de', 'opposite')),
      ], [
        x('Excuse me, how do I get to King’s Cross station? — Go straight on, then turn left. It’s on your right.', 'Excusez-moi, comment aller à la gare de King’s Cross ? — Allez tout droit, puis tournez à gauche. C’est sur votre droite.', 'Excuse me, how do I get to King’s Cross station? — Go straight on, then turn left. It’s on your right.'),
        x('The café is opposite the bank.', 'Le café est en face de la banque.', 'The café is opposite the bank.'),
      ], [
        FB(COMPLETE, '＿ left at the bank.', ['Turn', 'Turns', 'You turning'], 'Turn', ('Impératif : verbe seul.', 'Imperative: the base verb alone.'), ('Tournez à gauche à la banque.', 'Turn left at the bank.')),
        FB(CHOOSE, 'Go ＿ on, then take the first street.', ['straight', 'right', 'left'], 'straight', ('tout droit = straight on.', 'without turning: straight on.'), ('Allez tout droit, puis prenez la première rue.', 'Go straight on, then take the first street.')),
        DC(ANSWER, [('Tourist', 'Excuse me, where’s the station?')], ('Une touriste te demande la gare.', 'A tourist asks you where the station is.'), ['Turn right, it’s on your left.', 'It’s ten pounds.', 'Yes, I can.'], 'Turn right, it’s on your left.', ('Where’s…? → on indique le chemin.', 'Where’s…? → give directions.')),
        TF('The museum is on your left.', ('Le musée est sur ta droite.', 'The museum is on your right.'), FAUX, ('left = gauche.', 'left is the opposite of right.')),
      ]),
    L('en-transport', ('Les transports : by bus, on foot', 'Transport: by bus, on foot'), ('Dire comment on se déplace et acheter un billet.', 'Say how you travel and buy a ticket.'), 8, [
        ('by + moyen de transport : by bus, by train, by car, by plane. Mais : on foot (à pied).', 'by + means of transport: by bus, by train, by car, by plane. But: on foot.'),
        ('Au guichet : A single / A return ticket to Edinburgh, please. (aller simple / aller-retour). What time does the next train leave?', 'At the ticket office: A single / A return ticket to Edinburgh, please. What time does the next train leave?'),
        ('Le métro de Londres s’appelle the Underground ou the Tube.', 'The London metro is called the Underground or the Tube.'),
      ], [
        EG('by-transport', 'by bus / by train / on foot', ('en bus / en train / à pied', 'by bus / by train / on foot')),
        E('bus', 'bus', ('bus', 'bus')),
        E('train', 'train', ('train', 'train')),
        E('ticket', 'ticket', ('billet, ticket', 'ticket')),
        E('return-ticket', 'return ticket', ('billet aller-retour', 'return ticket')),
        E('platform', 'platform', ('quai', 'platform')),
        E('airport', 'airport', ('aéroport', 'airport')),
      ], [
        x('I go to work by bus, but on Fridays I go on foot.', 'Je vais au travail en bus, mais le vendredi j’y vais à pied.', 'I go to work by bus, but on Fridays I go on foot.'),
        x('A return ticket to Inverness, please. — That’s forty pounds. The train leaves from platform four.', 'Un aller-retour pour Inverness, s’il vous plaît. — Ça fait 40 livres. Le train part du quai 4.', 'A return ticket to Inverness, please. — That’s forty pounds. The train leaves from platform four.'),
      ], [
        FB(CHOOSE, 'I go to work ＿ train.', ['by', 'on', 'in'], 'by', ('Moyen de transport : by.', 'Means of transport: by.'), ('Je vais au travail en train.', 'I go to work by train.')),
        FB(CHOOSE, 'She walks to school. She goes on ＿.', ['foot', 'feet', 'walk'], 'foot', ('à pied = on foot.', 'walking: on foot.'), ('Elle va à l’école à pied.', 'She goes on foot.')),
        DC(ANSWER, [('Ticket office', 'Single or return?')], ('Au guichet, on te demande quel billet tu veux.', 'At the ticket office, they ask which ticket you want.'), ['Return, please.', 'By bus, please.', 'Platform two.'], 'Return, please.', ('Single or return? → aller simple ou aller-retour.', 'Single or return? → choose one.')),
        TF('The train leaves from platform four.', ('Le train part du quai 4.', 'The train leaves from platform 4.'), VRAI, ('platform four = quai 4.', 'platform four = platform 4.')),
      ]),
  ]),
  CH('a1-w6-c2', ('Ce que je sais faire', 'What I can do'), [
    L('en-can', ('Savoir, pouvoir : can, can’t', 'Ability: can, can’t'), ('Dire ce que l’on sait ou peut faire, et demander une permission.', 'Say what you can do and ask for permission.'), 9, [
        ('can + base verbale, sans -s ni to : I can swim, she can drive (pas « she cans », pas « can to »).', 'can + base verb, no -s and no to: I can swim, she can drive.'),
        ('Négation : can’t (cannot). Question : Can you speak Spanish? — Yes, I can. / No, I can’t.', 'Negative: can’t (cannot). Question: Can you speak Spanish? — Yes, I can. / No, I can’t.'),
        ('Can I…? sert aussi à demander la permission : Can I open the window?', 'Can I…? is also used to ask for permission: Can I open the window?'),
      ], [
        EG('can', 'can / can’t', ('savoir, pouvoir (capacité, permission)', 'can / can’t (ability, permission)')),
        E('swim', 'to swim', ('nager', 'to swim')),
        E('drive', 'to drive', ('conduire', 'to drive')),
        E('cook', 'to cook', ('cuisiner', 'to cook')),
        E('help', 'to help', ('aider', 'to help')),
        E('open', 'to open', ('ouvrir', 'to open')),
      ], [
        x('Can you drive? — Yes, I can, but I can’t drive on the left!', 'Tu sais conduire ? — Oui, mais je ne sais pas conduire à gauche !', 'Can you drive? — Yes, I can, but I can’t drive on the left!'),
        x('Can I help you? — Yes, please. Can you open the door?', 'Je peux vous aider ? — Oui, s’il vous plaît. Vous pouvez ouvrir la porte ?', 'Can I help you? — Yes, please. Can you open the door?'),
      ], [
        FB(CHOOSE, 'She ＿ swim very well.', ['can', 'cans', 'can to'], 'can', ('can ne prend jamais de -s.', 'can never takes -s.'), ('Elle sait très bien nager.', 'She can swim very well.')),
        FB(CHOOSE, 'I can ＿ Italian food.', ['cook', 'cooks', 'to cook'], 'cook', ('Après can : base verbale.', 'After can: base verb.'), ('Je sais cuisiner italien.', 'I can cook Italian food.')),
        DC(ANSWER, [('Nessie', 'Can you swim?')], ('Le monstre te demande si tu sais nager.', 'The monster asks if you can swim.'), ['No, I can’t!', 'No, I don’t swim.', 'No, I’m not.'], 'No, I can’t!', ('Can you…? → Yes, I can. / No, I can’t.', 'Can you…? → Yes, I can. / No, I can’t.')),
        order(('Remets dans l’ordre : « Je peux ouvrir la fenêtre ? »', 'Put in order: “Can I open the window?”'), ['Can', 'I', 'open', 'the', 'window?'], ('Permission : Can I + verbe ?', 'Permission: Can I + verb?')),
      ]),
  ])])

# ═════════════════════════ Île 7 : En ce moment ═════════════════════════
W7 = WORLD('a1-w7', ('Le chevalier vert', 'The Green Knight'), REGION,
  ('Décrire ce qui se passe en ce moment, la météo et les vêtements : le présent continu.', 'Describe what is happening right now, the weather and clothes: the present continuous.'),
  (('Le Chevalier vert', 'The Green Knight'), 'K', ('Le géant tout vert de la cour d’Arthur lance un défi : décris ce que chacun fait à l’instant, le temps qu’il fait et ce qu’il porte, sans une erreur.', 'The all-green giant from Arthur’s court sets a challenge: describe what everyone is doing right now, the weather and what they are wearing, without a mistake.')),
  [CH('a1-w7-c1', ('En ce moment', 'Right now'), [
    L('en-present-continuous', ('Le présent continu : I’m working', 'The present continuous: I’m working'), ('Dire ce que l’on fait en ce moment avec be + -ing.', 'Say what you are doing now with be + -ing.'), 10, [
        ('be + verbe en -ing pour une action en cours : I’m working (je suis en train de travailler), she’s calling a client.', 'be + verb + -ing for an action in progress: I’m working, she’s calling a client.'),
        ('Orthographe : write → writing (e muet tombe), sit → sitting (consonne doublée), play → playing.', 'Spelling: write → writing (silent e drops), sit → sitting (consonant doubled), play → playing.'),
        ('Comparaison : I usually take the bus, but today I’m walking. (présent simple = habitude ; présent continu = maintenant).', 'Compare: I usually take the bus, but today I’m walking. (present simple = habit; present continuous = now).'),
      ], [
        EG('present-continuous', 'be + -ing (I’m working)', ('présent continu (action en cours)', 'present continuous (action in progress)')),
        E('now', 'now', ('maintenant', 'now')),
        E('today', 'today', ('aujourd’hui', 'today')),
        E('call', 'to call', ('appeler (au téléphone)', 'to call')),
        E('write', 'to write', ('écrire', 'to write')),
        E('wait', 'to wait', ('attendre', 'to wait')),
        E('read', 'to read', ('lire', 'to read')),
      ], [
        x('Where’s Tom? — He’s in the meeting room. He’s calling a client.', 'Où est Tom ? — Dans la salle de réunion. Il est en train d’appeler un client.', 'Where’s Tom? — He’s in the meeting room. He’s calling a client.'),
        x('I usually drive, but today I’m taking the train.', 'D’habitude je conduis, mais aujourd’hui je prends le train.', 'I usually drive, but today I’m taking the train.'),
      ], [
        FB(CHOOSE, 'Shh! The manager ＿ on the phone.', ['is talking', 'talks', 'talking'], 'is talking', ('Action en cours : is + -ing.', 'Action in progress: is + -ing.'), ('Chut ! Le responsable est au téléphone.', 'Shh! The manager is talking on the phone.')),
        FB(CHOOSE, 'I’m ＿ an email to the client.', ['writing', 'writeing', 'writting'], 'writing', ('write → writing (le e tombe).', 'write → writing (the e drops).'), ('J’écris un e-mail au client.', 'I’m writing an email to the client.')),
        FB(CHOOSE, 'She usually ＿ tea, but today she’s drinking coffee.', ['drinks', 'is drinking', 'drinking'], 'drinks', ('Habitude (usually) : présent simple.', 'Habit (usually): present simple.'), ('D’habitude elle boit du thé, mais aujourd’hui elle boit du café.', 'She usually drinks tea, but today she’s drinking coffee.')),
        DC(ANSWER, [('Kate', 'What are you doing?')], ('Kate te demande ce que tu fais.', 'Kate asks what you are doing.'), ['I’m reading a report.', 'I read a report.', 'I’m a report.'], 'I’m reading a report.', ('What are you doing? → I’m + -ing.', 'What are you doing? → I’m + -ing.')),
      ]),
    L('en-weather', ('Le temps qu’il fait', 'The weather'), ('Parler de la météo et des saisons.', 'Talk about the weather and the seasons.'), 8, [
        ('What’s the weather like? — It’s sunny (ensoleillé), cloudy (nuageux), windy (venteux), cold (froid), hot (chaud).', 'What’s the weather like? — It’s sunny, cloudy, windy, cold, hot.'),
        ('Pour la pluie et la neige en ce moment : It’s raining, it’s snowing (présent continu).', 'For rain and snow right now: It’s raining, it’s snowing (present continuous).'),
        ('Les saisons : spring, summer, autumn (en américain : fall), winter.', 'The seasons: spring, summer, autumn (American English: fall), winter.'),
      ], [
        E('weather', 'weather', ('temps (météo)', 'weather')),
        E('sunny', 'sunny', ('ensoleillé', 'sunny')),
        E('cloudy', 'cloudy', ('nuageux', 'cloudy')),
        E('rain', 'to rain', ('pleuvoir', 'to rain')),
        E('cold', 'cold', ('froid', 'cold')),
        E('hot', 'hot', ('chaud', 'hot')),
        E('winter', 'winter', ('hiver', 'winter')),
      ], [
        x('What’s the weather like in Glasgow? — It’s cloudy and it’s raining. As usual!', 'Quel temps fait-il à Glasgow ? — C’est nuageux et il pleut. Comme d’habitude !', 'What’s the weather like in Glasgow? — It’s cloudy and it’s raining. As usual!'),
        x('In winter it’s cold, but in summer it’s sometimes hot.', 'En hiver il fait froid, mais en été il fait parfois chaud.', 'In winter it’s cold, but in summer it’s sometimes hot.'),
      ], [
        FB(CHOOSE, 'Take an umbrella. It’s ＿.', ['raining', 'sunny', 'hot'], 'raining', ('Parapluie → il pleut : raining.', 'Umbrella → it’s raining.'), ('Prends un parapluie. Il pleut.', 'Take an umbrella. It’s raining.')),
        FB(CHOOSE, 'It’s 30 °C. It’s very ＿ today!', ['hot', 'cold', 'cloudy'], 'hot', ('30 °C : hot.', '30 °C: hot.'), ('Il fait 30 °C. Il fait très chaud aujourd’hui !', 'It’s 30 °C. It’s very hot today!')),
        DC(ANSWER, [('Anna', 'What’s the weather like in Paris?')], ('Anna te demande le temps à Paris.', 'Anna asks about the weather in Paris.'), ['It’s sunny and warm.', 'It’s on Monday.', 'I like Paris.'], 'It’s sunny and warm.', ('What’s the weather like? → It’s + adjectif.', 'What’s the weather like? → It’s + adjective.')),
        TF('It’s snowing in London.', ('Il neige à Londres.', 'It’s snowing in London.'), VRAI, ('snowing = il neige.', 'snowing = snow is falling.')),
      ]),
  ]),
  CH('a1-w7-c2', ('Les vêtements', 'Clothes'), [
    L('en-clothes', ('Les vêtements et les couleurs', 'Clothes and colours'), ('Décrire ce que quelqu’un porte : wear, les couleurs, la place de l’adjectif.', 'Describe what someone is wearing: wear, colours, adjective order.'), 9, [
        ('wear = porter (un vêtement) : She’s wearing a blue jacket. Au travail : What do you wear to work?', 'wear: She’s wearing a blue jacket. At work: What do you wear to work?'),
        ('L’adjectif se place avant le nom et ne s’accorde jamais : a red dress, two red dresses (pas « reds »).', 'The adjective goes before the noun and never agrees: a red dress, two red dresses (not “reds”).'),
        ('Couleurs : red, blue, green, yellow, black, white, grey (gray en américain), brown.', 'Colours: red, blue, green, yellow, black, white, grey (gray in American English), brown.'),
      ], [
        EG('adjective-order', 'adjective + noun (a red dress)', ('place de l’adjectif (avant le nom, invariable)', 'adjective before the noun (no plural)')),
        E('wear', 'to wear', ('porter (un vêtement)', 'to wear')),
        E('jacket', 'jacket', ('veste', 'jacket')),
        E('shoes', 'shoes', ('chaussures', 'shoes')),
        E('shirt', 'shirt', ('chemise', 'shirt')),
        E('green', 'green', ('vert', 'green')),
        E('black', 'black', ('noir', 'black')),
        E('blue', 'blue', ('bleu', 'blue')),
      ], [
        x('The Green Knight is wearing green armour and green shoes!', 'Le Chevalier vert porte une armure verte et des chaussures vertes !', 'The Green Knight is wearing green armour and green shoes!'),
        x('For the interview, I’m wearing a white shirt and a black jacket.', 'Pour l’entretien, je porte une chemise blanche et une veste noire.', 'For the interview, I’m wearing a white shirt and a black jacket.'),
      ], [
        FB(CHOOSE, 'She’s wearing ＿.', ['a blue jacket', 'a jacket blue', 'a jacket blues'], 'a blue jacket', ('Adjectif avant le nom.', 'Adjective before the noun.'), ('Elle porte une veste bleue.', 'She’s wearing a blue jacket.')),
        FB(CHOOSE, 'I’ve got two ＿ shirts.', ['white', 'whites', 'whiten'], 'white', ('L’adjectif ne prend jamais de -s.', 'An adjective never takes -s.'), ('J’ai deux chemises blanches.', 'I’ve got two white shirts.')),
        TF('Tom is wearing black shoes.', ('Les chaussures de Tom sont noires.', 'Tom’s shoes are black.'), VRAI, ('black = noir.', 'black = the darkest colour.')),
        order(('Remets dans l’ordre : « Il porte une chemise verte. »', 'Put in order: “He is wearing a green shirt.”'), ['He', 'is', 'wearing', 'a', 'green', 'shirt.'], ('be + wearing + adjectif + nom.', 'be + wearing + adjective + noun.')),
      ]),
  ])])

# ═════════════════════════ Île 8 : Le week-end dernier ═════════════════════════
W8 = WORLD('a1-w8', ('Le réveil du dragon rouge', 'The red dragon wakes'), REGION,
  ('Raconter son week-end au passé : was / were, le prétérit des verbes réguliers et des irréguliers les plus courants.', 'Talk about your weekend in the past: was / were, the past simple of regular verbs and the most common irregular ones.'),
  (('Y Ddraig Goch, le dragon rouge', 'Y Ddraig Goch, the Red Dragon'), 'D', ('Le dragon du pays de Galles se réveille sous la colline et veut savoir ce que tu as fait pour mériter l’épée. Raconte ton voyage au passé, sans faute.', 'The dragon of Wales wakes beneath the hill and wants to know what you did to deserve the sword. Tell the story of your journey in the past, without a mistake.')),
  [CH('a1-w8-c1', ('Hier', 'Yesterday'), [
    L('en-was-were', ('Le passé de be : was, were', 'The past of be: was, were'), ('Dire où l’on était et comment c’était hier.', 'Say where you were and how it was yesterday.'), 9, [
        ('I / he / she / it was ; you / we / they were. Négation : wasn’t, weren’t.', 'I / he / she / it was; you / we / they were. Negative: wasn’t, weren’t.'),
        ('Question : Were you at the office yesterday? — No, I wasn’t. I was at home.', 'Question: Were you at the office yesterday? — No, I wasn’t. I was at home.'),
        ('Repères du passé : yesterday (hier), last week (la semaine dernière), last night (hier soir), two days ago (il y a deux jours).', 'Past time words: yesterday, last week, last night, two days ago.'),
      ], [
        EG('was-were', 'was / were', ('était, étaient (passé de be)', 'was / were (past of be)')),
        E('yesterday', 'yesterday', ('hier', 'yesterday')),
        E('last-week', 'last week', ('la semaine dernière', 'last week')),
        E('ago', 'ago', ('il y a (temps écoulé)', 'ago')),
        E('tired', 'tired', ('fatigué', 'tired')),
        E('home', 'home', ('maison, chez soi', 'home')),
      ], [
        x('Where were you yesterday? — I was in Cardiff. It was great!', 'Où étais-tu hier ? — J’étais à Cardiff. C’était génial !', 'Where were you yesterday? — I was in Cardiff. It was great!'),
        x('We weren’t at the office last week. We were on holiday.', 'Nous n’étions pas au bureau la semaine dernière. Nous étions en vacances.', 'We weren’t at the office last week. We were on holiday.'),
      ], [
        FB(CHOOSE, 'I ＿ tired last night.', ['was', 'were', 'am'], 'was', ('Passé avec I : was.', 'Past with I: was.'), ('J’étais fatigué hier soir.', 'I was tired last night.')),
        FB(CHOOSE, 'They ＿ at home yesterday.', ['were', 'was', 'are'], 'were', ('Passé avec they : were.', 'Past with they: were.'), ('Ils étaient à la maison hier.', 'They were at home yesterday.')),
        DC(ANSWER, [('Mr Ambrose', 'Were you at the office on Friday?')], ('M. Ambrose te demande si tu étais au bureau vendredi.', 'Mr Ambrose asks if you were at the office on Friday.'), ['No, I wasn’t. I was ill.', 'No, I don’t.', 'No, I’m not.'], 'No, I wasn’t. I was ill.', ('Were you…? → Yes, I was. / No, I wasn’t.', 'Were you…? → Yes, I was. / No, I wasn’t.')),
        TF('I was in Wales two days ago.', ('La personne est au pays de Galles en ce moment.', 'The person is in Wales now.'), FAUX, ('two days ago = il y a deux jours : c’est passé.', 'two days ago: it’s in the past.')),
      ]),
    L('en-past-regular', ('Le prétérit régulier : worked, played', 'The regular past simple: worked, played'), ('Raconter des actions passées avec les verbes réguliers en -ed.', 'Talk about past actions with regular -ed verbs.'), 10, [
        ('Le prétérit (past simple) raconte une action terminée : I worked late yesterday. Les verbes réguliers prennent -ed à toutes les personnes.', 'The past simple tells a finished action: I worked late yesterday. Regular verbs take -ed with every subject.'),
        ('Orthographe : like → liked, stop → stopped, study → studied. Prononciation : worked « t », played « d », visited « id ».', 'Spelling: like → liked, stop → stopped, study → studied. Pronunciation: worked “t”, played “d”, visited “id”.'),
        ('Question et négation avec did + base verbale : Did you visit the castle? I didn’t watch TV.', 'Questions and negatives with did + base verb: Did you visit the castle? I didn’t watch TV.'),
      ], [
        EG('past-ed', 'regular past -ed (worked)', ('passé simple des verbes réguliers', 'past simple of regular verbs (-ed)')),
        EG('did', 'did / didn’t', ('auxiliaire des questions et négations au passé', 'did / didn’t (past questions and negatives)')),
        E('visit', 'to visit', ('visiter, rendre visite', 'to visit')),
        E('watch', 'to watch', ('regarder (un film, la télé)', 'to watch')),
        E('play', 'to play', ('jouer', 'to play')),
        E('stay', 'to stay', ('rester, séjourner', 'to stay')),
        E('castle', 'castle', ('château fort', 'castle')),
      ], [
        x('Last weekend we visited Conwy Castle and stayed in a small hotel.', 'Le week-end dernier, nous avons visité le château de Conwy et séjourné dans un petit hôtel.', 'Last weekend we visited Conwy Castle and stayed in a small hotel.'),
        x('Did you watch the match? — No, I didn’t. I worked late.', 'Tu as regardé le match ? — Non. J’ai travaillé tard.', 'Did you watch the match? — No, I didn’t. I worked late.'),
      ], [
        FB(CHOOSE, 'Yesterday I ＿ my grandmother.', ['visited', 'visit', 'visits'], 'visited', ('yesterday → prétérit : visited.', 'yesterday → past simple: visited.'), ('Hier, j’ai rendu visite à ma grand-mère.', 'Yesterday I visited my grandmother.')),
        FB(CHOOSE, 'We ＿ tennis last Sunday.', ['played', 'plaied', 'play'], 'played', ('play → played (voyelle + y : on garde y).', 'play → played (vowel + y: keep the y).'), ('Nous avons joué au tennis dimanche dernier.', 'We played tennis last Sunday.')),
        FB(CHOOSE, 'Did you ＿ the film?', ['watch', 'watched', 'watching'], 'watch', ('Après did : base verbale.', 'After did: base verb.'), ('Tu as regardé le film ?', 'Did you watch the film?')),
        DC(ANSWER, [('Kate', 'Did you stay in a hotel?')], ('Kate te pose une question sur ton voyage.', 'Kate asks about your trip.'), ['Yes, I did.', 'Yes, I was.', 'Yes, I stay.'], 'Yes, I did.', ('Did you…? → Yes, I did. / No, I didn’t.', 'Did you…? → Yes, I did. / No, I didn’t.')),
      ]),
  ]),
  CH('a1-w8-c2', ('Un voyage inoubliable', 'An unforgettable trip'), [
    L('en-past-irregular', ('Les irréguliers : went, had, saw', 'Irregular verbs: went, had, saw'), ('Utiliser les verbes irréguliers les plus fréquents au passé.', 'Use the most common irregular verbs in the past.'), 10, [
        ('Les verbes les plus courants sont irréguliers et s’apprennent par cœur : go → went, have → had, see → saw, eat → ate, buy → bought, get → got, take → took.', 'The most common verbs are irregular and must be learnt: go → went, have → had, see → saw, eat → ate, buy → bought, get → got, take → took.'),
        ('Avec did, on revient à la base : Where did you go? (pas « did you went »).', 'With did, go back to the base form: Where did you go? (not “did you went”).'),
      ], [
        EG('past-irregular', 'irregular past (went, had)', ('passé simple des verbes irréguliers', 'past simple of irregular verbs')),
        E('went', 'went', ('suis allé (passé de go)', 'went (past of go)')),
        E('had', 'had', ('ai eu (passé de have)', 'had (past of have)')),
        E('saw', 'saw', ('ai vu (passé de see)', 'saw (past of see)')),
        E('bought', 'bought', ('ai acheté (passé de buy)', 'bought (past of buy)')),
        E('took', 'took', ('ai pris (passé de take)', 'took (past of take)')),
        E('holiday', 'holiday', ('vacances', 'holiday')),
      ], [
        x('Last summer I went to Wales. I saw a castle on a hill and I had fish and chips by the sea.', 'L’été dernier, je suis allé au pays de Galles. J’ai vu un château sur une colline et j’ai mangé un fish and chips au bord de la mer.', 'Last summer I went to Wales. I saw a castle on a hill and I had fish and chips by the sea.'),
        x('Where did you go on holiday? — We went to Scotland. We took the night train.', 'Où êtes-vous partis en vacances ? — En Écosse. Nous avons pris le train de nuit.', 'Where did you go on holiday? — We went to Scotland. We took the night train.'),
      ], [
        FB(CHOOSE, 'Last year I ＿ to Edinburgh.', ['went', 'goed', 'go'], 'went', ('go → went.', 'go → went.'), ('L’année dernière, je suis allé à Édimbourg.', 'Last year I went to Edinburgh.')),
        FB(CHOOSE, 'She ＿ a new jacket on Saturday.', ['bought', 'buyed', 'buys'], 'bought', ('buy → bought.', 'buy → bought.'), ('Elle a acheté une nouvelle veste samedi.', 'She bought a new jacket on Saturday.')),
        FB(CHOOSE, 'Where did you ＿ on holiday?', ['go', 'went', 'going'], 'go', ('Après did : base verbale.', 'After did: base verb.'), ('Où es-tu allé en vacances ?', 'Where did you go on holiday?')),
        TF('We saw the dragon yesterday.', ('Nous avons vu le dragon hier.', 'We saw the dragon yesterday.'), VRAI, ('saw = passé de see (voir).', 'saw = past of see.')),
      ]),
  ])])

FINAL = {
  'slug': 'a1-final',
  'title': t(('Simulation TOEIC A1 : l’épée dans le rocher', 'TOEIC A1 simulation: the sword in the stone')),
  'region': REGION,
  'description': t(('Examen blanc au format du TOEIC Listening & Reading, en anglais : questions-réponses, conversations et annonces, phrases et textes à compléter, compréhension écrite. Noté sur 990 ; objectif A1 à 120 points.', 'Mock exam in TOEIC Listening & Reading format, in English: question-response, conversations and talks, incomplete sentences and texts, reading comprehension. Marked out of 990; A1 target at 120 points.')),
  'exam': 'a1-toeic',
  'chapters': [],
}

level = {
  'contentVersion': '2026.11.22',
  'level': {'code': 'A1', 'title': t(('A1 : premiers pas en anglais', 'A1: first steps in English')), 'region': REGION, 'order': 30},
  'notice': t(('Les listes de vocabulaire de Koto Quest suivent les compétences du niveau A1 du CECRL et préparent au TOEIC Listening & Reading, mais ne sont pas des listes officielles d’ETS.', 'Koto Quest’s vocabulary lists follow the CEFR A1 skills and prepare for the TOEIC Listening & Reading test, but they are not official ETS lists.')),
  'worlds': [W1, W2, W3, W4, W5, W6, W7, W8, FINAL],
}
t((REGION, 'Kingdom of Albion'))
os.makedirs(os.path.join(ROOT, 'content/a1'), exist_ok=True)
check_and_write(level, 'content/a1/a1.json', ['content/n5/n5.json', 'content/n4/n4.json', 'content/n3/n3.json', 'content/n2/n2.json', 'content/n1/n1.json',
  'content/topik1/topik1.json', 'content/topik2/topik2.json', 'content/topik3/topik3.json', 'content/topik4/topik4.json', 'content/topik5/topik5.json', 'content/topik6/topik6.json'])
