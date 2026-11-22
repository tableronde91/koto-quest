# Lecture en anglais : contes et légendes britanniques (domaine public), réécrits en anglais simple.
# Ajoute (ou remplace) les contes anglais dans content/reading/stories.json, sans toucher aux contes japonais et coréens.
# Usage : python3 scripts/en-reading.py
import json, os
ROOT = os.path.join(os.path.dirname(__file__), '..')
P = os.path.join(ROOT, 'content/reading/stories.json')

def S(en, fr, en_tr=None):
    """Phrase : le texte à lire et à prononcer est le même ; la « traduction anglaise » reprend le texte."""
    return {'jp': en, 'fr': fr, 'en': en_tr or en, 'kana': en}

def W(word, ipa, fr, en):
    return {'jp': word, 'reading': ipa, 'fr': fr, 'en': en}

def Q(q, choices, answer):
    return {'q': {'fr': q[0], 'en': q[1]}, 'choices': [{'fr': f, 'en': e} for f, e in choices], 'answer': answer}

def CH(slug, title, paragraphs, words, questions):
    en, fr = title
    return {'slug': slug, 'title': {'jp': en, 'fr': fr, 'en': en}, 'paragraphs': paragraphs, 'words': words, 'questions': questions}

def STORY(slug, glyph, level, color, title, summary, chapters):
    en, fr = title
    return {'slug': slug, 'glyph': glyph, 'level': level, 'color': color, 'title': {'jp': en, 'fr': fr, 'en': en}, 'summary': {'fr': summary[0], 'en': summary[1]}, 'chapters': chapters}

# ═════════════════════════ Goldilocks and the Three Bears ═════════════════════════
GOLDILOCKS = STORY('goldilocks', 'G', 'A1', '#D9A23B', ('Goldilocks and the Three Bears', 'Boucle d’or et les trois ours'),
  ('Une petite fille entre dans une maison vide au milieu de la forêt. Tout y va par trois…', 'A little girl walks into an empty house in the middle of the forest. Everything there comes in threes…'), [
  CH('goldilocks-1', ('The house in the forest', 'La maison dans la forêt'), [
    [S('Once upon a time, there were three bears.', 'Il était une fois trois ours.'),
     S('There was a big father bear, a mother bear and a little baby bear.', 'Il y avait un grand papa ours, une maman ours et un petit bébé ours.'),
     S('They lived in a small house in the forest.', 'Ils vivaient dans une petite maison dans la forêt.')],
    [S('One morning, the porridge was very hot.', 'Un matin, le porridge était très chaud.'),
     S('“Let’s go for a walk,” said Mother Bear.', '« Allons nous promener », dit maman ours.'),
     S('The three bears went out, and the door was open.', 'Les trois ours sortirent, et la porte resta ouverte.')],
  ], [
    W('bear', '/beə/', 'ours', 'bear'),
    W('forest', '/ˈfɒrɪst/', 'forêt', 'forest'),
    W('house', '/haʊs/', 'maison', 'house'),
    W('porridge', '/ˈpɒrɪdʒ/', 'porridge, bouillie d’avoine', 'porridge'),
    W('walk', '/wɔːk/', 'promenade ; marcher', 'walk'),
    W('open', '/ˈəʊpən/', 'ouvert ; ouvrir', 'open'),
  ], [
    Q(('Combien d’ours y a-t-il ?', 'How many bears are there?'), [('Deux', 'Two'), ('Trois', 'Three'), ('Quatre', 'Four')], 1),
    Q(('Pourquoi les ours sortent-ils ?', 'Why do the bears go out?'), [('Le porridge est trop chaud', 'The porridge is too hot'), ('Ils ont faim', 'They are hungry'), ('Il pleut', 'It is raining')], 0),
  ]),
  CH('goldilocks-2', ('Too hot, too cold, just right', 'Trop chaud, trop froid, parfait'), [
    [S('A little girl came to the house. Her name was Goldilocks.', 'Une petite fille arriva à la maison. Elle s’appelait Boucle d’or.'),
     S('She saw three bowls of porridge on the table.', 'Elle vit trois bols de porridge sur la table.'),
     S('The big bowl was too hot. The middle bowl was too cold.', 'Le grand bol était trop chaud. Le bol moyen était trop froid.'),
     S('The little bowl was just right, and she ate it all!', 'Le petit bol était parfait, et elle le mangea en entier !')],
    [S('Then she saw three chairs.', 'Puis elle vit trois chaises.'),
     S('She sat on the little chair, but it broke!', 'Elle s’assit sur la petite chaise, mais elle se cassa !'),
     S('Goldilocks was tired, so she went upstairs.', 'Boucle d’or était fatiguée, alors elle monta à l’étage.')],
  ], [
    W('girl', '/ɡɜːl/', 'fille', 'girl'),
    W('bowl', '/bəʊl/', 'bol', 'bowl'),
    W('too', '/tuː/', 'trop', 'too'),
    W('just right', '/dʒʌst raɪt/', 'parfait, juste comme il faut', 'just right'),
    W('broke', '/brəʊk/', 'cassa (passé de break)', 'broke'),
    W('upstairs', '/ʌpˈsteəz/', 'à l’étage', 'upstairs'),
  ], [
    Q(('Quel bol Boucle d’or mange-t-elle ?', 'Which bowl does Goldilocks eat?'), [('Le grand bol', 'The big bowl'), ('Le bol moyen', 'The middle bowl'), ('Le petit bol', 'The little bowl')], 2),
    Q(('Que se passe-t-il avec la petite chaise ?', 'What happens to the little chair?'), [('Elle se casse', 'It breaks'), ('Elle disparaît', 'It disappears'), ('Elle est trop grande', 'It is too big')], 0),
  ]),
  CH('goldilocks-3', ('Someone is in my bed!', 'Quelqu’un dort dans mon lit !'), [
    [S('Upstairs, there were three beds.', 'À l’étage, il y avait trois lits.'),
     S('The little bed was just right, and Goldilocks fell asleep.', 'Le petit lit était parfait, et Boucle d’or s’endormit.'),
     S('Then the three bears came home.', 'Puis les trois ours rentrèrent à la maison.')],
    [S('“Someone ate my porridge!” cried Baby Bear.', '« Quelqu’un a mangé mon porridge ! » cria bébé ours.'),
     S('“And someone is sleeping in my bed!”', '« Et quelqu’un dort dans mon lit ! »'),
     S('Goldilocks woke up, saw the bears and ran out of the house. She never came back!', 'Boucle d’or se réveilla, vit les ours et s’enfuit de la maison. Elle ne revint jamais !')],
  ], [
    W('bed', '/bed/', 'lit', 'bed'),
    W('fell asleep', '/fel əˈsliːp/', 's’endormit', 'fell asleep'),
    W('came home', '/keɪm həʊm/', 'rentrèrent à la maison', 'came home'),
    W('someone', '/ˈsʌmwʌn/', 'quelqu’un', 'someone'),
    W('woke up', '/wəʊk ʌp/', 'se réveilla', 'woke up'),
    W('ran', '/ræn/', 'courut (passé de run)', 'ran'),
  ], [
    Q(('Où dort Boucle d’or ?', 'Where does Goldilocks sleep?'), [('Dans le grand lit', 'In the big bed'), ('Dans le petit lit', 'In the little bed'), ('Sur une chaise', 'On a chair')], 1),
    Q(('Que fait Boucle d’or quand elle voit les ours ?', 'What does Goldilocks do when she sees the bears?'), [('Elle mange avec eux', 'She eats with them'), ('Elle s’enfuit', 'She runs away'), ('Elle se rendort', 'She goes back to sleep')], 1),
  ]),
])

# ═════════════════════════ Dick Whittington and his Cat ═════════════════════════
WHITTINGTON = STORY('dick-whittington', 'L', 'A1', '#3F6FB5', ('Dick Whittington and his Cat', 'Dick Whittington et son chat'),
  ('Un garçon pauvre part chercher fortune à Londres, où les rues seraient pavées d’or. Son seul trésor : un chat.', 'A poor boy goes to seek his fortune in London, where the streets are said to be paved with gold. His only treasure: a cat.'), [
  CH('whittington-1', ('Streets of gold', 'Des rues pavées d’or'), [
    [S('Dick was a poor boy. He had no family and no money.', 'Dick était un garçon pauvre. Il n’avait ni famille ni argent.'),
     S('People said: “In London, the streets are made of gold!”', 'Les gens disaient : « À Londres, les rues sont en or ! »'),
     S('So Dick walked to London. It was a very long way.', 'Alors Dick partit à pied pour Londres. C’était très loin.')],
    [S('But the streets of London were not gold. They were dirty and grey.', 'Mais les rues de Londres n’étaient pas en or. Elles étaient sales et grises.'),
     S('Dick was cold and hungry.', 'Dick avait froid et faim.'),
     S('A kind merchant, Mr Fitzwarren, gave him a job in his kitchen.', 'Un marchand généreux, M. Fitzwarren, lui donna du travail dans sa cuisine.')],
  ], [
    W('poor', '/pɔː/', 'pauvre', 'poor'),
    W('gold', '/ɡəʊld/', 'or', 'gold'),
    W('long way', '/lɒŋ weɪ/', 'long chemin, loin', 'long way'),
    W('dirty', '/ˈdɜːti/', 'sale', 'dirty'),
    W('hungry', '/ˈhʌŋɡri/', 'affamé, qui a faim', 'hungry'),
    W('merchant', '/ˈmɜːtʃənt/', 'marchand', 'merchant'),
  ], [
    Q(('Pourquoi Dick va-t-il à Londres ?', 'Why does Dick go to London?'), [('Pour voir sa famille', 'To see his family'), ('Parce que les rues seraient en or', 'Because the streets are said to be gold'), ('Pour acheter un chat', 'To buy a cat')], 1),
    Q(('Qui donne du travail à Dick ?', 'Who gives Dick a job?'), [('Un marchand', 'A merchant'), ('Le roi', 'The king'), ('Un capitaine', 'A captain')], 0),
  ]),
  CH('whittington-2', ('The cat on the ship', 'Le chat sur le bateau'), [
    [S('Dick slept in a small room with many mice.', 'Dick dormait dans une petite chambre pleine de souris.'),
     S('He bought a cat for one penny. The cat caught all the mice!', 'Il acheta un chat pour un penny. Le chat attrapa toutes les souris !'),
     S('Dick loved his cat very much.', 'Dick aimait beaucoup son chat.')],
    [S('One day, Mr Fitzwarren’s ship was ready to go to a far country.', 'Un jour, le bateau de M. Fitzwarren fut prêt à partir pour un pays lointain.'),
     S('“Everyone can send something to sell,” he said.', '« Chacun peut envoyer quelque chose à vendre », dit-il.'),
     S('Dick had only his cat. Sadly, he sent the cat on the ship.', 'Dick n’avait que son chat. Tristement, il envoya le chat sur le bateau.')],
  ], [
    W('mice', '/maɪs/', 'souris (pluriel de mouse)', 'mice'),
    W('penny', '/ˈpeni/', 'penny (pièce de monnaie)', 'penny'),
    W('caught', '/kɔːt/', 'attrapa (passé de catch)', 'caught'),
    W('ship', '/ʃɪp/', 'navire, bateau', 'ship'),
    W('far', '/fɑː/', 'lointain, loin', 'far'),
    W('sell', '/sel/', 'vendre', 'sell'),
  ], [
    Q(('Combien coûte le chat ?', 'How much does the cat cost?'), [('Un penny', 'One penny'), ('Une livre', 'One pound'), ('Rien', 'Nothing')], 0),
    Q(('Que fait Dick de son chat ?', 'What does Dick do with his cat?'), [('Il le garde dans sa chambre', 'He keeps it in his room'), ('Il l’envoie sur le bateau', 'He sends it on the ship'), ('Il le donne au roi', 'He gives it to the king')], 1),
  ]),
  CH('whittington-3', ('Turn again, Whittington', 'Fais demi-tour, Whittington'), [
    [S('Dick was sad without his cat, so he left London.', 'Sans son chat, Dick était triste, alors il quitta Londres.'),
     S('On the hill, he heard the bells of London.', 'Sur la colline, il entendit les cloches de Londres.'),
     S('The bells sang: “Turn again, Whittington, Lord Mayor of London!”', 'Les cloches chantaient : « Fais demi-tour, Whittington, lord-maire de Londres ! »')],
    [S('Dick went back. The ship was home, and there was great news.', 'Dick revint. Le bateau était rentré, et il y avait une grande nouvelle.'),
     S('In the far country, the king had too many rats. He paid a lot of gold for the cat!', 'Dans le pays lointain, le roi avait trop de rats. Il avait payé beaucoup d’or pour le chat !'),
     S('Dick was rich. Later, he became Lord Mayor of London three times.', 'Dick était riche. Plus tard, il devint trois fois lord-maire de Londres.')],
  ], [
    W('sad', '/sæd/', 'triste', 'sad'),
    W('hill', '/hɪl/', 'colline', 'hill'),
    W('bells', '/belz/', 'cloches', 'bells'),
    W('news', '/njuːz/', 'nouvelle(s)', 'news'),
    W('rich', '/rɪtʃ/', 'riche', 'rich'),
    W('Lord Mayor', '/lɔːd ˈmeə/', 'lord-maire (maire de la City de Londres)', 'Lord Mayor'),
  ], [
    Q(('Que disent les cloches ?', 'What do the bells say?'), [('De rentrer à Londres', 'To go back to London'), ('De partir en bateau', 'To take a ship'), ('De chercher son chat', 'To look for his cat')], 0),
    Q(('Pourquoi Dick devient-il riche ?', 'Why does Dick become rich?'), [('Il trouve de l’or dans la rue', 'He finds gold in the street'), ('Le roi a payé son chat très cher', 'The king paid a lot for his cat'), ('Il gagne un concours', 'He wins a contest')], 1),
  ]),
])

# ═════════════════════════ The Sword in the Stone ═════════════════════════
SWORD = STORY('sword-in-the-stone', 'A', 'A1', '#2E6B4F', ('The Sword in the Stone', 'L’Épée dans le rocher'),
  ('Le roi est mort sans héritier. Une épée plantée dans un rocher attend celui qui saura l’en tirer.', 'The king is dead without an heir. A sword stuck in a stone waits for the one who can pull it out.'), [
  CH('sword-1', ('A sword in a stone', 'Une épée dans un rocher'), [
    [S('Long ago, the King of England died. He had no son to be the new king.', 'Il y a très longtemps, le roi d’Angleterre mourut. Il n’avait pas de fils pour devenir le nouveau roi.'),
     S('The knights were angry. They all wanted to be king.', 'Les chevaliers étaient en colère. Ils voulaient tous être roi.')],
    [S('Merlin, a wise old wizard, had an idea.', 'Merlin, un vieux magicien sage, eut une idée.'),
     S('In a churchyard in London, there was a big stone with a sword in it.', 'Dans un cimetière de Londres, il y avait un grand rocher avec une épée plantée dedans.'),
     S('On the stone, there were these words: “Only the true king can pull out this sword.”', 'Sur le rocher, il y avait ces mots : « Seul le vrai roi peut retirer cette épée. »')],
  ], [
    W('king', '/kɪŋ/', 'roi', 'king'),
    W('died', '/daɪd/', 'mourut (passé de die)', 'died'),
    W('knight', '/naɪt/', 'chevalier', 'knight'),
    W('wizard', '/ˈwɪzəd/', 'magicien, sorcier', 'wizard'),
    W('stone', '/stəʊn/', 'pierre, rocher', 'stone'),
    W('sword', '/sɔːd/', 'épée', 'sword'),
  ], [
    Q(('Pourquoi les chevaliers sont-ils en colère ?', 'Why are the knights angry?'), [('Ils veulent tous être roi', 'They all want to be king'), ('Ils ont perdu une épée', 'They lost a sword'), ('Merlin est parti', 'Merlin has left')], 0),
    Q(('Que dit l’inscription sur le rocher ?', 'What do the words on the stone say?'), [('Que l’épée est à vendre', 'That the sword is for sale'), ('Que seul le vrai roi peut retirer l’épée', 'That only the true king can pull out the sword'), ('Que Merlin est le roi', 'That Merlin is the king')], 1),
  ]),
  CH('sword-2', ('Arthur and the sword', 'Arthur et l’épée'), [
    [S('Many knights tried, but nobody could move the sword.', 'Beaucoup de chevaliers essayèrent, mais personne ne put bouger l’épée.'),
     S('Years later, there was a big tournament in London.', 'Des années plus tard, il y eut un grand tournoi à Londres.'),
     S('A young knight, Sir Kay, came with his little brother, Arthur.', 'Un jeune chevalier, sire Kay, vint avec son petit frère, Arthur.')],
    [S('Kay forgot his sword at home! “Arthur, please find me a sword!”', 'Kay avait oublié son épée chez lui ! « Arthur, trouve-moi une épée, s’il te plaît ! »'),
     S('Arthur saw the sword in the stone and pulled it out. It was easy!', 'Arthur vit l’épée dans le rocher et la retira. C’était facile !'),
     S('Everyone was surprised. Arthur was the true king!', 'Tout le monde fut surpris. Arthur était le vrai roi !')],
  ], [
    W('tried', '/traɪd/', 'essayèrent (passé de try)', 'tried'),
    W('nobody', '/ˈnəʊbədi/', 'personne (aucune personne)', 'nobody'),
    W('tournament', '/ˈtʊənəmənt/', 'tournoi', 'tournament'),
    W('forgot', '/fəˈɡɒt/', 'oublia (passé de forget)', 'forgot'),
    W('pulled out', '/pʊld aʊt/', 'retira, arracha', 'pulled out'),
    W('surprised', '/səˈpraɪzd/', 'surpris', 'surprised'),
  ], [
    Q(('Pourquoi Arthur cherche-t-il une épée ?', 'Why does Arthur look for a sword?'), [('Pour devenir roi', 'To become king'), ('Kay a oublié la sienne', 'Kay forgot his'), ('Pour le tournoi de Merlin', 'For Merlin’s tournament')], 1),
    Q(('Est-ce difficile pour Arthur de retirer l’épée ?', 'Is it difficult for Arthur to pull out the sword?'), [('Oui, très difficile', 'Yes, very difficult'), ('Non, c’est facile', 'No, it is easy'), ('Il n’y arrive pas', 'He cannot do it')], 1),
  ]),
])


# ═════════════════════════ A2 : Jack and the Beanstalk ═════════════════════════
JACK = STORY('jack-beanstalk', 'J', 'A2', '#4E8F3A', ('Jack and the Beanstalk', 'Jack et le haricot magique'),
  ('Jack échange la vache de la famille contre cinq haricots. Sa mère est furieuse… jusqu’au lendemain matin.', 'Jack swaps the family cow for five beans. His mother is furious… until the next morning.'), [
  CH('jack-1', ('Five magic beans', 'Cinq haricots magiques'), [
    [S('Jack and his mother were very poor. They had nothing left except an old cow.', 'Jack et sa mère étaient très pauvres. Il ne leur restait qu’une vieille vache.'),
     S('“Take the cow to the market and sell it,” his mother said. “We need the money.”', '« Emmène la vache au marché et vends-la, dit sa mère. Nous avons besoin de cet argent. »')],
    [S('While Jack was walking to town, he met a strange old man.', 'Pendant que Jack marchait vers la ville, il rencontra un vieil homme étrange.'),
     S('“I’ll give you five magic beans for your cow,” the man said. Jack thought it was a great deal.', '« Je te donne cinq haricots magiques pour ta vache », dit l’homme. Jack pensa que c’était une excellente affaire.'),
     S('When he got home, his mother was furious. She threw the beans out of the window.', 'Quand il rentra, sa mère était furieuse. Elle jeta les haricots par la fenêtre.')],
  ], [
    W('poor', '/pɔː/', 'pauvre', 'poor'),
    W('cow', '/kaʊ/', 'vache', 'cow'),
    W('market', '/ˈmɑːkɪt/', 'marché', 'market'),
    W('beans', '/biːnz/', 'haricots', 'beans'),
    W('strange', '/streɪndʒ/', 'étrange', 'strange'),
    W('threw', '/θruː/', 'jeta (passé de throw)', 'threw'),
  ], [
    Q(('Pourquoi Jack va-t-il au marché ?', 'Why does Jack go to the market?'), [('Pour acheter des haricots', 'To buy beans'), ('Pour vendre la vache', 'To sell the cow'), ('Pour voir un vieil homme', 'To see an old man')], 1),
    Q(('Que fait la mère de Jack des haricots ?', 'What does Jack’s mother do with the beans?'), [('Elle les cuisine', 'She cooks them'), ('Elle les jette par la fenêtre', 'She throws them out of the window'), ('Elle les vend', 'She sells them')], 1),
  ]),
  CH('jack-2', ('The giant’s castle', 'Le château du géant'), [
    [S('The next morning, an enormous beanstalk was growing outside the window. It went up into the clouds!', 'Le lendemain matin, un énorme haricot géant poussait devant la fenêtre. Il montait jusqu’aux nuages !'),
     S('Jack climbed up and found a huge castle. A giant lived there with his wife.', 'Jack grimpa et découvrit un immense château. Un géant y vivait avec sa femme.')],
    [S('“Fee-fi-fo-fum!” shouted the giant. “I can smell a boy!”', '« Fee-fi-fo-fum ! cria le géant. Je sens l’odeur d’un garçon ! »'),
     S('Jack hid in the kitchen. While the giant was sleeping, Jack took a bag of gold coins and ran away.', 'Jack se cacha dans la cuisine. Pendant que le géant dormait, Jack prit un sac de pièces d’or et s’enfuit.')],
  ], [
    W('beanstalk', '/ˈbiːnstɔːk/', 'tige de haricot', 'beanstalk'),
    W('clouds', '/klaʊdz/', 'nuages', 'clouds'),
    W('climbed', '/klaɪmd/', 'grimpa', 'climbed'),
    W('huge', '/hjuːdʒ/', 'immense', 'huge'),
    W('smell', '/smel/', 'sentir (une odeur)', 'smell'),
    W('hid', '/hɪd/', 'se cacha (passé de hide)', 'hid'),
  ], [
    Q(('Jusqu’où monte le haricot ?', 'How high does the beanstalk go?'), [('Jusqu’au toit', 'To the roof'), ('Jusqu’aux nuages', 'Up into the clouds'), ('Jusqu’à la forêt', 'To the forest')], 1),
    Q(('Que prend Jack au géant ?', 'What does Jack take from the giant?'), [('Un sac de pièces d’or', 'A bag of gold coins'), ('Une poule', 'A hen'), ('Une harpe', 'A harp')], 0),
  ]),
  CH('jack-3', ('The golden hen', 'La poule aux œufs d’or'), [
    [S('Jack went up the beanstalk again. This time, he took the giant’s hen, which laid golden eggs.', 'Jack remonta le long du haricot. Cette fois, il prit la poule du géant, qui pondait des œufs d’or.'),
     S('But the third time, the giant woke up and ran after him.', 'Mais la troisième fois, le géant se réveilla et le poursuivit.')],
    [S('Jack climbed down faster than ever. “Mother, bring me the axe!” he shouted.', 'Jack descendit plus vite que jamais. « Maman, apporte-moi la hache ! » cria-t-il.'),
     S('He cut the beanstalk, and the giant fell. Jack and his mother were never poor again.', 'Il coupa le haricot, et le géant tomba. Jack et sa mère ne furent plus jamais pauvres.')],
  ], [
    W('hen', '/hen/', 'poule', 'hen'),
    W('laid', '/leɪd/', 'pondit (passé de lay)', 'laid'),
    W('golden', '/ˈɡəʊldən/', 'en or, doré', 'golden'),
    W('woke up', '/wəʊk ʌp/', 'se réveilla', 'woke up'),
    W('axe', '/æks/', 'hache', 'axe'),
    W('fell', '/fel/', 'tomba (passé de fall)', 'fell'),
  ], [
    Q(('Que fait la poule du géant ?', 'What does the giant’s hen do?'), [('Elle chante', 'It sings'), ('Elle pond des œufs d’or', 'It lays golden eggs'), ('Elle parle', 'It talks')], 1),
    Q(('Comment Jack arrête-t-il le géant ?', 'How does Jack stop the giant?'), [('Il coupe le haricot', 'He cuts the beanstalk'), ('Il le cache', 'He hides him'), ('Il lui donne de l’or', 'He gives him gold')], 0),
  ]),
])

# ═════════════════════════ A2 : King Canute and the Waves ═════════════════════════
CANUTE = STORY('king-canute', 'C', 'A2', '#3F6F9F', ('King Canute and the Waves', 'Le roi Knut et les vagues'),
  ('Ses courtisans le disent plus puissant que la mer. Le roi Knut décide de leur donner une leçon sur la plage.', 'His courtiers say he is more powerful than the sea. King Canute decides to teach them a lesson on the beach.'), [
  CH('canute-1', ('The most powerful king', 'Le roi le plus puissant'), [
    [S('A thousand years ago, Canute was the king of England, Denmark and Norway.', 'Il y a mille ans, Knut était roi d’Angleterre, du Danemark et de Norvège.'),
     S('His courtiers always told him how great he was. “You are the most powerful man in the world!” they said.', 'Ses courtisans lui répétaient sans cesse à quel point il était grand. « Vous êtes l’homme le plus puissant du monde ! » disaient-ils.')],
    [S('“Even the sea will obey you,” said one courtier.', '« Même la mer vous obéira », dit un courtisan.'),
     S('Canute was tired of these silly words. He decided to show them the truth.', 'Knut était las de ces paroles stupides. Il décida de leur montrer la vérité.')],
  ], [
    W('thousand', '/ˈθaʊznd/', 'mille', 'thousand'),
    W('courtiers', '/ˈkɔːtiəz/', 'courtisans', 'courtiers'),
    W('powerful', '/ˈpaʊəfl/', 'puissant', 'powerful'),
    W('obey', '/əˈbeɪ/', 'obéir', 'obey'),
    W('silly', '/ˈsɪli/', 'stupide, idiot', 'silly'),
    W('truth', '/truːθ/', 'vérité', 'truth'),
  ], [
    Q(('Que disent les courtisans au roi ?', 'What do the courtiers tell the king?'), [('Qu’il est le plus puissant du monde', 'That he is the most powerful in the world'), ('Qu’il doit partir', 'That he must leave'), ('Qu’il est malade', 'That he is ill')], 0),
    Q(('Que pense Knut de ces paroles ?', 'What does Canute think of these words?'), [('Il les trouve vraies', 'He thinks they are true'), ('Il les trouve stupides', 'He thinks they are silly'), ('Il ne les entend pas', 'He does not hear them')], 1),
  ]),
  CH('canute-2', ('On the beach', 'Sur la plage'), [
    [S('Canute took his courtiers to the beach and sat on his throne near the water.', 'Knut emmena ses courtisans à la plage et s’assit sur son trône près de l’eau.'),
     S('“Waves, I order you to stop!” he shouted. But the waves kept coming.', '« Vagues, je vous ordonne de vous arrêter ! » cria-t-il. Mais les vagues continuèrent d’avancer.')],
    [S('Soon the king’s feet were wet, and the courtiers looked very uncomfortable.', 'Bientôt, le roi eut les pieds mouillés, et les courtisans semblaient très mal à l’aise.'),
     S('“You see?” said Canute. “A king is not stronger than the sea. Remember that.”', '« Vous voyez ? dit Knut. Un roi n’est pas plus fort que la mer. Souvenez-vous-en. »')],
  ], [
    W('beach', '/biːtʃ/', 'plage', 'beach'),
    W('throne', '/θrəʊn/', 'trône', 'throne'),
    W('waves', '/weɪvz/', 'vagues', 'waves'),
    W('order', '/ˈɔːdə/', 'ordonner', 'order'),
    W('wet', '/wet/', 'mouillé', 'wet'),
    W('stronger', '/ˈstrɒŋɡə/', 'plus fort', 'stronger'),
  ], [
    Q(('Que fait le roi sur la plage ?', 'What does the king do on the beach?'), [('Il nage', 'He swims'), ('Il ordonne aux vagues de s’arrêter', 'He orders the waves to stop'), ('Il pêche', 'He goes fishing')], 1),
    Q(('Quelle leçon donne le roi ?', 'What lesson does the king give?'), [('Un roi n’est pas plus fort que la mer', 'A king is not stronger than the sea'), ('La mer obéit au roi', 'The sea obeys the king'), ('Il faut aimer la plage', 'You must love the beach')], 0),
  ]),
])


# ═════════════════════════ B1 : Robin Hood and the Golden Arrow ═════════════════════════
ROBIN = STORY('robin-hood', 'R', 'B1', '#2F6B3A', ('Robin Hood and the Golden Arrow', 'Robin des Bois et la flèche d’or'),
  ('Le shérif de Nottingham organise un concours de tir à l’arc pour piéger Robin des Bois. Robin décide d’y aller quand même.', 'The Sheriff of Nottingham organises an archery contest to trap Robin Hood. Robin decides to go anyway.'), [
  CH('robin-1', ('The Sheriff’s trap', 'Le piège du shérif'), [
    [S('For years, Robin Hood had been living in Sherwood Forest with his band of outlaws.', 'Depuis des années, Robin des Bois vivait dans la forêt de Sherwood avec sa bande de hors-la-loi.'),
     S('They took money from the rich and gave it to the poor, which made the Sheriff of Nottingham furious.', 'Ils prenaient l’argent des riches pour le donner aux pauvres, ce qui rendait furieux le shérif de Nottingham.')],
    [S('One day, the Sheriff announced an archery contest. The prize would be an arrow made of gold.', 'Un jour, le shérif annonça un concours de tir à l’arc. Le prix serait une flèche en or.'),
     S('“Robin is so proud that he will come,” the Sheriff thought. “And when he does, my soldiers will catch him.”', '« Robin est si fier qu’il viendra, pensa le shérif. Et quand il viendra, mes soldats l’attraperont. »')],
  ], [
    W('outlaws', '/ˈaʊtlɔːz/', 'hors-la-loi', 'outlaws'),
    W('furious', '/ˈfjʊəriəs/', 'furieux', 'furious'),
    W('announced', '/əˈnaʊnst/', 'annonça', 'announced'),
    W('contest', '/ˈkɒntest/', 'concours', 'contest'),
    W('prize', '/praɪz/', 'prix, récompense', 'prize'),
    W('proud', '/praʊd/', 'fier', 'proud'),
    W('catch', '/kætʃ/', 'attraper', 'catch'),
  ], [
    Q(('Pourquoi le shérif est-il furieux ?', 'Why is the Sheriff furious?'), [('Robin vole les riches pour aider les pauvres', 'Robin robs the rich to help the poor'), ('Robin a gagné un concours', 'Robin won a contest'), ('Ses soldats sont partis', 'His soldiers have left')], 0),
    Q(('Quel est le vrai but du concours ?', 'What is the real aim of the contest?'), [('Trouver le meilleur archer', 'To find the best archer'), ('Attraper Robin', 'To catch Robin'), ('Gagner de l’argent', 'To make money')], 1),
  ]),
  CH('robin-2', ('The stranger in red', 'L’inconnu en rouge'), [
    [S('Robin’s friends begged him not to go. “It must be a trap,” said Little John.', 'Les amis de Robin le supplièrent de ne pas y aller. « Ce doit être un piège », dit Petit Jean.'),
     S('But Robin had an idea. If he wore a disguise, nobody would recognise him.', 'Mais Robin eut une idée. S’il se déguisait, personne ne le reconnaîtrait.')],
    [S('On the day of the contest, a stranger in a red cloak and a hood stepped forward.', 'Le jour du concours, un inconnu vêtu d’une cape rouge et d’un capuchon s’avança.'),
     S('His arrows flew straight to the centre of the target, one after another. The crowd had never seen such an archer.', 'Ses flèches filaient droit au centre de la cible, l’une après l’autre. La foule n’avait jamais vu un tel archer.')],
  ], [
    W('begged', '/beɡd/', 'supplièrent', 'begged'),
    W('trap', '/træp/', 'piège', 'trap'),
    W('disguise', '/dɪsˈɡaɪz/', 'déguisement', 'disguise'),
    W('recognise', '/ˈrekəɡnaɪz/', 'reconnaître', 'recognise'),
    W('cloak', '/kləʊk/', 'cape', 'cloak'),
    W('target', '/ˈtɑːɡɪt/', 'cible', 'target'),
  ], [
    Q(('Que pense Petit Jean du concours ?', 'What does Little John think of the contest?'), [('Que c’est sûrement un piège', 'That it must be a trap'), ('Que Robin va perdre', 'That Robin will lose'), ('Qu’il veut y participer', 'That he wants to take part')], 0),
    Q(('Comment Robin évite-t-il d’être reconnu ?', 'How does Robin avoid being recognised?'), [('Il arrive la nuit', 'He arrives at night'), ('Il porte un déguisement', 'He wears a disguise'), ('Il envoie Petit Jean', 'He sends Little John')], 1),
  ]),
  CH('robin-3', ('The golden arrow', 'La flèche d’or'), [
    [S('The Sheriff gave the golden arrow to the stranger in red without realising who he was.', 'Le shérif remit la flèche d’or à l’inconnu en rouge sans se rendre compte de qui il était.'),
     S('That evening, a letter was found on the Sheriff’s table: “Thank you for the prize. Robin Hood.”', 'Ce soir-là, on trouva une lettre sur la table du shérif : « Merci pour le prix. Robin des Bois. »')],
    [S('The Sheriff was so angry that he could not eat his dinner.', 'Le shérif était si furieux qu’il ne put manger son dîner.'),
     S('Meanwhile, in Sherwood Forest, the outlaws were laughing and singing around the fire.', 'Pendant ce temps, dans la forêt de Sherwood, les hors-la-loi riaient et chantaient autour du feu.')],
  ], [
    W('golden', '/ˈɡəʊldən/', 'en or, doré', 'golden'),
    W('stranger', '/ˈstreɪndʒə/', 'inconnu', 'stranger'),
    W('realising', '/ˈrɪəlaɪzɪŋ/', 'se rendre compte', 'realising'),
    W('letter', '/ˈletə/', 'lettre', 'letter'),
    W('angry', '/ˈæŋɡri/', 'en colère', 'angry'),
    W('meanwhile', '/ˈmiːnwaɪl/', 'pendant ce temps', 'meanwhile'),
  ], [
    Q(('Comment le shérif apprend-il la vérité ?', 'How does the Sheriff learn the truth?'), [('Par une lettre', 'From a letter'), ('Par ses soldats', 'From his soldiers'), ('Robin le lui dit en face', 'Robin tells him face to face')], 0),
    Q(('Que font les hors-la-loi ce soir-là ?', 'What do the outlaws do that evening?'), [('Ils s’enfuient', 'They run away'), ('Ils font la fête autour du feu', 'They celebrate around the fire'), ('Ils attaquent le château', 'They attack the castle')], 1),
  ]),
])

# ═════════════════════════ B1 : The Pedlar of Swaffham ═════════════════════════
PEDLAR = STORY('pedlar-swaffham', 'P', 'B1', '#8A5A2B', ('The Pedlar of Swaffham', 'Le colporteur de Swaffham'),
  ('Un pauvre colporteur fait trois fois le même rêve : un trésor l’attend sur le pont de Londres. Il décide de partir.', 'A poor pedlar has the same dream three times: a treasure awaits him on London Bridge. He decides to set off.'), [
  CH('pedlar-1', ('The dream', 'Le rêve'), [
    [S('Long ago, in the little town of Swaffham, there lived a poor pedlar called John Chapman.', 'Il y a longtemps, dans la petite ville de Swaffham, vivait un pauvre colporteur nommé John Chapman.'),
     S('One night he dreamt that if he went to London Bridge, he would hear some wonderful news.', 'Une nuit, il rêva que s’il allait au pont de Londres, il apprendrait une merveilleuse nouvelle.')],
    [S('He had the same dream three nights in a row, so he decided to go.', 'Il fit le même rêve trois nuits de suite ; il décida donc de partir.'),
     S('His wife thought he was mad. “It must be the cheese you ate before bed,” she said.', 'Sa femme le crut fou. « Ça doit être le fromage que tu as mangé avant de te coucher », dit-elle.')],
  ], [
    W('pedlar', '/ˈpedlə/', 'colporteur', 'pedlar'),
    W('dreamt', '/dremt/', 'rêva', 'dreamt'),
    W('wonderful', '/ˈwʌndəfl/', 'merveilleux', 'wonderful'),
    W('in a row', '/ɪn ə rəʊ/', 'de suite, d’affilée', 'in a row'),
    W('mad', '/mæd/', 'fou', 'mad'),
    W('cheese', '/tʃiːz/', 'fromage', 'cheese'),
  ], [
    Q(('Combien de fois John fait-il le rêve ?', 'How many times does John have the dream?'), [('Une fois', 'Once'), ('Trois fois', 'Three times'), ('Chaque nuit depuis un an', 'Every night for a year')], 1),
    Q(('Que pense sa femme ?', 'What does his wife think?'), [('Qu’il est fou', 'That he is mad'), ('Qu’il va devenir riche', 'That he will become rich'), ('Qu’elle doit venir aussi', 'That she must come too')], 0),
  ]),
  CH('pedlar-2', ('On London Bridge', 'Sur le pont de Londres'), [
    [S('John walked for days until he reached London Bridge. He waited there from morning till night, but nothing happened.', 'John marcha des jours jusqu’au pont de Londres. Il y attendit du matin au soir, mais rien ne se passa.'),
     S('On the third day, a shopkeeper asked him why he had been standing there for so long.', 'Le troisième jour, un commerçant lui demanda pourquoi il restait planté là depuis si longtemps.')],
    [S('When John told him about his dream, the shopkeeper laughed. “I had a dream too,” he said.', 'Quand John lui parla de son rêve, le commerçant éclata de rire. « Moi aussi, j’ai fait un rêve », dit-il.'),
     S('“I dreamt that a treasure was buried under a tree in the garden of a pedlar in Swaffham. But I would never be so foolish as to go there!”', '« J’ai rêvé qu’un trésor était enterré sous un arbre, dans le jardin d’un colporteur de Swaffham. Mais je ne serais jamais assez sot pour y aller ! »')],
  ], [
    W('reached', '/riːtʃt/', 'atteignit', 'reached'),
    W('shopkeeper', '/ˈʃɒpkiːpə/', 'commerçant', 'shopkeeper'),
    W('laughed', '/lɑːft/', 'rit', 'laughed'),
    W('treasure', '/ˈtreʒə/', 'trésor', 'treasure'),
    W('buried', '/ˈberid/', 'enterré', 'buried'),
    W('foolish', '/ˈfuːlɪʃ/', 'sot, idiot', 'foolish'),
  ], [
    Q(('Que demande le commerçant à John ?', 'What does the shopkeeper ask John?'), [('Pourquoi il attend là depuis si longtemps', 'Why he has been waiting there so long'), ('S’il veut acheter quelque chose', 'If he wants to buy something'), ('D’où vient son fromage', 'Where his cheese comes from')], 0),
    Q(('Où se trouve le trésor dans le rêve du commerçant ?', 'Where is the treasure in the shopkeeper’s dream?'), [('Sous le pont de Londres', 'Under London Bridge'), ('Dans le jardin d’un colporteur de Swaffham', 'In a Swaffham pedlar’s garden'), ('Dans sa boutique', 'In his shop')], 1),
  ]),
  CH('pedlar-3', ('The treasure', 'Le trésor'), [
    [S('John said nothing and hurried home. As soon as he arrived, he started digging under the old oak tree in his garden.', 'John ne dit rien et rentra chez lui en hâte. Dès son arrivée, il se mit à creuser sous le vieux chêne de son jardin.'),
     S('Soon his spade hit something hard: a pot full of gold coins.', 'Bientôt, sa bêche heurta quelque chose de dur : une marmite pleine de pièces d’or.')],
    [S('John became a rich man, but he never forgot that he had once been poor.', 'John devint riche, mais il n’oublia jamais qu’il avait été pauvre.'),
     S('He used some of his gold to rebuild the church of Swaffham, where you can still see his statue today.', 'Il utilisa une partie de son or pour reconstruire l’église de Swaffham, où l’on peut encore voir sa statue aujourd’hui.')],
  ], [
    W('hurried', '/ˈhʌrid/', 'se dépêcha', 'hurried'),
    W('digging', '/ˈdɪɡɪŋ/', 'creuser', 'digging'),
    W('oak', '/əʊk/', 'chêne', 'oak'),
    W('spade', '/speɪd/', 'bêche', 'spade'),
    W('coins', '/kɔɪnz/', 'pièces de monnaie', 'coins'),
    W('rebuild', '/ˌriːˈbɪld/', 'reconstruire', 'rebuild'),
  ], [
    Q(('Où John trouve-t-il le trésor ?', 'Where does John find the treasure?'), [('Sous le chêne de son jardin', 'Under the oak in his garden'), ('Sur le pont de Londres', 'On London Bridge'), ('Dans l’église', 'In the church')], 0),
    Q(('Que fait John avec une partie de son or ?', 'What does John do with some of his gold?'), [('Il achète un château', 'He buys a castle'), ('Il reconstruit l’église', 'He rebuilds the church'), ('Il le donne au commerçant', 'He gives it to the shopkeeper')], 1),
  ]),
])


# ═════════════════════════ B2 : Tam Lin ═════════════════════════
TAMLIN = STORY('tam-lin', 'T', 'B2', '#5A3E7A', ('Tam Lin', 'Tam Lin'),
  ('Dans la forêt de Carterhaugh, la jeune Janet rencontre Tam Lin, un chevalier prisonnier de la reine des fées. Pour le sauver, elle devra tenir bon une nuit entière.', 'In the forest of Carterhaugh, young Janet meets Tam Lin, a knight held captive by the Queen of the Fairies. To save him, she will have to hold on for a whole night.'), [
  CH('tamlin-1', ('The forbidden forest', 'La forêt interdite'), [
    [S('Every young woman in the Scottish Borders had been warned never to go to Carterhaugh, a forest which was said to be guarded by an elf knight.', 'Toutes les jeunes filles des Borders écossais avaient été averties de ne jamais aller à Carterhaugh, une forêt que l’on disait gardée par un chevalier elfe.'),
     S('Janet, however, was not the kind of person who did what she was told.', 'Janet, cependant, n’était pas du genre à obéir aux ordres.')],
    [S('She had barely picked a single rose when a young man appeared, asking her who had given her permission to be there.', 'Elle avait à peine cueilli une rose qu’un jeune homme apparut et lui demanda qui lui avait permis d’être là.'),
     S('“Carterhaugh is mine,” Janet replied. “My father gave it to me, so I need nobody’s permission.”', '« Carterhaugh m’appartient, répondit Janet. Mon père me l’a donnée, je n’ai donc besoin de la permission de personne. »')],
  ], [
    W('warned', '/wɔːnd/', 'averti, prévenu', 'warned'),
    W('guarded', '/ˈɡɑːdɪd/', 'gardé', 'guarded'),
    W('however', '/haʊˈevə/', 'cependant', 'however'),
    W('barely', '/ˈbeəli/', 'à peine', 'barely'),
    W('picked', '/pɪkt/', 'cueilli', 'picked'),
    W('replied', '/rɪˈplaɪd/', 'répondit', 'replied'),
  ], [
    Q(('Que disait-on de la forêt de Carterhaugh ?', 'What was said about the forest of Carterhaugh?'), [('Qu’elle était gardée par un chevalier elfe', 'That it was guarded by an elf knight'), ('Qu’elle était pleine de trésors', 'That it was full of treasure'), ('Qu’elle avait brûlé', 'That it had burnt down')], 0),
    Q(('Pourquoi Janet dit-elle n’avoir besoin d’aucune permission ?', 'Why does Janet say she needs no permission?'), [('Elle est une fée', 'She is a fairy'), ('Son père lui a donné la forêt', 'Her father gave her the forest'), ('Le chevalier l’a invitée', 'The knight invited her')], 1),
  ]),
  CH('tamlin-2', ('The prisoner of the fairies', 'Le prisonnier des fées'), [
    [S('The young man, whose name was Tam Lin, explained that he had once been a mortal knight.', 'Le jeune homme, qui s’appelait Tam Lin, expliqua qu’il avait autrefois été un chevalier mortel.'),
     S('Years before, he had fallen from his horse, and the Queen of the Fairies had caught him and taken him to her kingdom.', 'Des années plus tôt, il était tombé de cheval, et la reine des fées l’avait rattrapé et emmené dans son royaume.')],
    [S('“Every seven years, the fairies pay a price to hell, and I fear I will be the price this time,” he said.', '« Tous les sept ans, les fées paient un tribut à l’enfer, et je crains d’être ce tribut cette fois-ci », dit-il.'),
     S('“If you truly want to save me, you must pull me from my horse on Halloween night and hold me tight, whatever happens.”', '« Si tu veux vraiment me sauver, tu devras me faire tomber de cheval la nuit d’Halloween et me tenir serré, quoi qu’il arrive. »')],
  ], [
    W('mortal', '/ˈmɔːtl/', 'mortel', 'mortal'),
    W('kingdom', '/ˈkɪŋdəm/', 'royaume', 'kingdom'),
    W('fear', '/fɪə/', 'craindre', 'fear'),
    W('truly', '/ˈtruːli/', 'vraiment, sincèrement', 'truly'),
    W('pull', '/pʊl/', 'tirer', 'pull'),
    W('whatever', '/wɒtˈevə/', 'quoi que', 'whatever'),
  ], [
    Q(('Comment Tam Lin est-il devenu prisonnier des fées ?', 'How did Tam Lin become the fairies’ prisoner?'), [('Il est tombé de cheval et la reine l’a emmené', 'He fell from his horse and the Queen took him'), ('Il est né chez les fées', 'He was born among the fairies'), ('Il a perdu un pari', 'He lost a bet')], 0),
    Q(('Que doit faire Janet la nuit d’Halloween ?', 'What must Janet do on Halloween night?'), [('Chanter une chanson', 'Sing a song'), ('Le faire tomber de cheval et le tenir serré', 'Pull him from his horse and hold him tight'), ('Allumer un feu', 'Light a fire')], 1),
  ]),
  CH('tamlin-3', ('Halloween night', 'La nuit d’Halloween'), [
    [S('At midnight, the fairy procession rode past, and Janet recognised Tam Lin on a white horse. She pulled him down and held him in her arms.', 'À minuit, le cortège des fées passa et Janet reconnut Tam Lin sur un cheval blanc. Elle le fit tomber et le serra dans ses bras.'),
     S('Furious, the Queen turned him into a snake, then a lion, then a burning piece of iron, but Janet did not let go.', 'Furieuse, la reine le transforma en serpent, puis en lion, puis en morceau de fer brûlant, mais Janet ne lâcha pas prise.')],
    [S('At last, Tam Lin became a man again. “Had I known what a human heart could do,” said the Queen bitterly, “I would have taken his eyes.”', 'Enfin, Tam Lin redevint un homme. « Si j’avais su de quoi un cœur humain est capable, dit la reine avec amertume, je lui aurais pris les yeux. »'),
     S('Then the fairies vanished, and Janet and Tam Lin walked home together as the sun rose.', 'Puis les fées disparurent, et Janet et Tam Lin rentrèrent ensemble tandis que le soleil se levait.')],
  ], [
    W('procession', '/prəˈseʃn/', 'cortège', 'procession'),
    W('recognised', '/ˈrekəɡnaɪzd/', 'reconnut', 'recognised'),
    W('burning', '/ˈbɜːnɪŋ/', 'brûlant', 'burning'),
    W('let go', '/let ɡəʊ/', 'lâcher prise', 'let go'),
    W('bitterly', '/ˈbɪtəli/', 'avec amertume', 'bitterly'),
    W('vanished', '/ˈvænɪʃt/', 'disparurent', 'vanished'),
  ], [
    Q(('Que fait la reine pour forcer Janet à lâcher Tam Lin ?', 'What does the Queen do to make Janet let go?'), [('Elle le transforme en créatures et en fer brûlant', 'She turns him into creatures and burning iron'), ('Elle appelle ses soldats', 'She calls her soldiers'), ('Elle lui offre de l’or', 'She offers her gold')], 0),
    Q(('Que regrette la reine à la fin ?', 'What does the Queen regret at the end?'), [('D’avoir perdu son cheval', 'Losing her horse'), ('De ne pas avoir pris les yeux de Tam Lin', 'Not having taken Tam Lin’s eyes'), ('D’être venue à Carterhaugh', 'Coming to Carterhaugh')], 1),
  ]),
])

# ═════════════════════════ B2 : Gelert ═════════════════════════
GELERT = STORY('gelert', 'D', 'B2', '#7A5A3A', ('Gelert the Faithful Hound', 'Gelert, le chien fidèle'),
  ('Le prince Llywelyn part à la chasse en laissant son fils sous la garde de son chien Gelert. À son retour, il découvre une scène terrible et agit sans réfléchir.', 'Prince Llywelyn goes hunting, leaving his son in the care of his hound Gelert. On his return, he finds a terrible scene and acts without thinking.'), [
  CH('gelert-1', ('The prince’s hound', 'Le chien du prince'), [
    [S('In the thirteenth century, Prince Llywelyn of Wales owned a hound called Gelert, which was said to be the most loyal dog in the kingdom.', 'Au XIIIe siècle, le prince Llywelyn de Galles possédait un chien nommé Gelert, que l’on disait le plus fidèle du royaume.'),
     S('Gelert went everywhere with the prince, and nobody could remember seeing one without the other.', 'Gelert accompagnait le prince partout, et personne ne se souvenait d’avoir vu l’un sans l’autre.')],
    [S('One day, however, Llywelyn decided to go hunting without him, leaving the dog to guard his baby son.', 'Un jour pourtant, Llywelyn décida d’aller chasser sans lui, laissant le chien veiller sur son bébé.'),
     S('“Look after him,” the prince said, before riding off into the mountains of Snowdonia.', '« Veille sur lui », dit le prince avant de partir à cheval vers les montagnes de Snowdonia.')],
  ], [
    W('century', '/ˈsentʃəri/', 'siècle', 'century'),
    W('owned', '/əʊnd/', 'possédait', 'owned'),
    W('hound', '/haʊnd/', 'chien de chasse', 'hound'),
    W('loyal', '/ˈlɔɪəl/', 'fidèle, loyal', 'loyal'),
    W('hunting', '/ˈhʌntɪŋ/', 'chasse', 'hunting'),
    W('look after', '/lʊk ˈɑːftə/', 'veiller sur, s’occuper de', 'look after'),
  ], [
    Q(('Que disait-on de Gelert ?', 'What was said about Gelert?'), [('Qu’il était le chien le plus fidèle du royaume', 'That he was the most loyal dog in the kingdom'), ('Qu’il était dangereux', 'That he was dangerous'), ('Qu’il était très vieux', 'That he was very old')], 0),
    Q(('Pourquoi Gelert ne part-il pas à la chasse ce jour-là ?', 'Why doesn’t Gelert go hunting that day?'), [('Il est malade', 'He is ill'), ('Il doit garder le bébé', 'He must guard the baby'), ('Il s’est perdu', 'He got lost')], 1),
  ]),
  CH('gelert-2', ('A terrible mistake', 'Une terrible erreur'), [
    [S('When the prince returned, Gelert ran to meet him, wagging his tail. His mouth was covered in blood.', 'Quand le prince revint, Gelert courut à sa rencontre en remuant la queue. Sa gueule était couverte de sang.'),
     S('Llywelyn rushed into the house: the cradle had been turned over and his son was nowhere to be seen.', 'Llywelyn se précipita dans la maison : le berceau était renversé et son fils restait introuvable.')],
    [S('Convinced that the dog had killed the child, the prince drew his sword and struck Gelert, who died with a last cry.', 'Convaincu que le chien avait tué l’enfant, le prince tira son épée et frappa Gelert, qui mourut en poussant un dernier cri.'),
     S('At that very moment, a baby’s voice answered from under the cradle.', 'À cet instant précis, la voix d’un bébé répondit sous le berceau.')],
  ], [
    W('wagging', '/ˈwæɡɪŋ/', 'remuant (la queue)', 'wagging'),
    W('rushed', '/rʌʃt/', 'se précipita', 'rushed'),
    W('cradle', '/ˈkreɪdl/', 'berceau', 'cradle'),
    W('nowhere', '/ˈnəʊweə/', 'nulle part', 'nowhere'),
    W('convinced', '/kənˈvɪnst/', 'convaincu', 'convinced'),
    W('struck', '/strʌk/', 'frappa', 'struck'),
  ], [
    Q(('Pourquoi le prince croit-il que Gelert a tué son fils ?', 'Why does the prince think Gelert killed his son?'), [('Le chien a du sang sur la gueule et l’enfant a disparu', 'The dog has blood on his mouth and the child is missing'), ('Un serviteur le lui a dit', 'A servant told him'), ('Le chien s’enfuit', 'The dog runs away')], 0),
    Q(('Que se passe-t-il juste après la mort de Gelert ?', 'What happens just after Gelert dies?'), [('Le prince s’endort', 'The prince falls asleep'), ('On entend le bébé sous le berceau', 'The baby is heard under the cradle'), ('Un loup entre', 'A wolf comes in')], 1),
  ]),
  CH('gelert-3', ('The grave of Gelert', 'La tombe de Gelert'), [
    [S('Under the cradle lay the baby, unharmed, and beside him lay an enormous dead wolf.', 'Sous le berceau se trouvait le bébé, indemne, et à côté de lui gisait un énorme loup mort.'),
     S('Llywelyn understood at once: Gelert had not attacked his son but had saved him from the wolf.', 'Llywelyn comprit aussitôt : Gelert n’avait pas attaqué son fils, il l’avait sauvé du loup.')],
    [S('Had he waited a moment longer, his faithful hound would still be alive. The prince was said never to have smiled again.', 'S’il avait attendu un instant de plus, son fidèle chien serait encore en vie. On dit que le prince ne sourit plus jamais.'),
     S('He buried Gelert with great honour, and the village of Beddgelert, which means “Gelert’s grave”, still bears his name today.', 'Il enterra Gelert avec de grands honneurs, et le village de Beddgelert, qui signifie « la tombe de Gelert », porte encore son nom aujourd’hui.')],
  ], [
    W('unharmed', '/ʌnˈhɑːmd/', 'indemne', 'unharmed'),
    W('beside', '/bɪˈsaɪd/', 'à côté de', 'beside'),
    W('wolf', '/wʊlf/', 'loup', 'wolf'),
    W('faithful', '/ˈfeɪθfl/', 'fidèle', 'faithful'),
    W('grave', '/ɡreɪv/', 'tombe', 'grave'),
    W('bears', '/beəz/', 'porte (un nom)', 'bears'),
  ], [
    Q(('Que s’était-il vraiment passé ?', 'What had really happened?'), [('Gelert avait sauvé le bébé d’un loup', 'Gelert had saved the baby from a wolf'), ('Le bébé était tombé du berceau', 'The baby had fallen from the cradle'), ('Un voleur était entré', 'A thief had come in')], 0),
    Q(('Que signifie le nom Beddgelert ?', 'What does the name Beddgelert mean?'), [('Le chien fidèle', 'The faithful dog'), ('La tombe de Gelert', 'Gelert’s grave'), ('La maison du prince', 'The prince’s house')], 1),
  ]),
])


# ═════════════════════════ C1 : The Lady of Shalott ═════════════════════════
SHALOTT = STORY('lady-of-shalott', 'L', 'C1', '#4A6A8A', ('The Lady of Shalott', 'La Dame de Shalott'),
  ('Enfermée dans une tour près de Camelot, une jeune femme ne peut regarder le monde qu’à travers un miroir. Le jour où elle voit passer Lancelot, elle brave la malédiction.', 'Shut away in a tower near Camelot, a young woman may only look at the world through a mirror. The day she sees Lancelot ride by, she defies the curse.'), [
  CH('shalott-1', ('The curse', 'La malédiction'), [
    [S('On an island in the river that flows down to Camelot stood a grey tower, in which lived a lady whom hardly anyone had ever seen.', 'Sur une île de la rivière qui descend vers Camelot se dressait une tour grise, où vivait une dame que presque personne n’avait jamais vue.'),
     S('Day and night she wove a magic tapestry, for she had been told that, were she to look directly at the outside world, a curse would fall upon her.', 'Jour et nuit, elle tissait une tapisserie magique, car on lui avait dit que si elle regardait directement le monde extérieur, une malédiction s’abattrait sur elle.')],
    [S('Not knowing what the curse might be, she dared not disobey, and watched life pass only as reflections in a mirror.', 'Ignorant la nature de cette malédiction, elle n’osait désobéir et ne voyait passer la vie que sous forme de reflets dans un miroir.'),
     S('Farmers, knights and young lovers appeared in the glass, yet she remained, in her own words, “half sick of shadows”.', 'Paysans, chevaliers et jeunes amoureux apparaissaient dans la glace ; pourtant, elle restait, selon ses propres mots, « à demi lasse des ombres ».')],
  ], [
    W('wove', '/wəʊv/', 'tissait', 'wove'),
    W('tapestry', '/ˈtæpəstri/', 'tapisserie', 'tapestry'),
    W('curse', '/kɜːs/', 'malédiction', 'curse'),
    W('dared', '/deəd/', 'osait', 'dared'),
    W('disobey', '/ˌdɪsəˈbeɪ/', 'désobéir', 'disobey'),
    W('reflections', '/rɪˈflekʃnz/', 'reflets', 'reflections'),
  ], [
    Q(('Que se passerait-il si la dame regardait directement dehors ?', 'What would happen if the lady looked directly outside?'), [('Une malédiction s’abattrait sur elle', 'A curse would fall upon her'), ('Elle deviendrait reine', 'She would become queen'), ('La tour s’effondrerait', 'The tower would collapse')], 0),
    Q(('Comment voit-elle le monde ?', 'How does she see the world?'), [('Par la fenêtre', 'Through the window'), ('Dans un miroir', 'In a mirror'), ('Dans ses rêves', 'In her dreams')], 1),
  ]),
  CH('shalott-2', ('Sir Lancelot', 'Sire Lancelot'), [
    [S('One bright summer morning, Sir Lancelot rode past the tower, his armour flashing in the sun and his voice ringing out in song.', 'Un lumineux matin d’été, sire Lancelot passa près de la tour, son armure étincelant au soleil et sa voix résonnant dans une chanson.'),
     S('No sooner had his reflection crossed the mirror than the lady left her loom and went to the window.', 'À peine son reflet eut-il traversé le miroir que la dame quitta son métier à tisser et alla à la fenêtre.')],
    [S('At that very moment, the mirror cracked from side to side and the tapestry flew out of the window.', 'À cet instant précis, le miroir se fendit d’un bout à l’autre et la tapisserie s’envola par la fenêtre.'),
     S('“The curse is come upon me,” she cried, knowing that there was no turning back.', '« La malédiction s’abat sur moi », s’écria-t-elle, sachant qu’il n’y avait plus de retour possible.')],
  ], [
    W('armour', '/ˈɑːmə/', 'armure', 'armour'),
    W('flashing', '/ˈflæʃɪŋ/', 'étincelant', 'flashing'),
    W('ringing out', '/ˈrɪŋɪŋ aʊt/', 'résonnant', 'ringing out'),
    W('loom', '/luːm/', 'métier à tisser', 'loom'),
    W('cracked', '/krækt/', 'se fendit', 'cracked'),
    W('no turning back', '/nəʊ ˈtɜːnɪŋ bæk/', 'pas de retour possible', 'no turning back'),
  ], [
    Q(('Qu’est-ce qui pousse la dame à aller à la fenêtre ?', 'What makes the lady go to the window?'), [('Le passage de Lancelot', 'Lancelot riding by'), ('Un orage', 'A storm'), ('Un cri d’enfant', 'A child’s cry')], 0),
    Q(('Que se passe-t-il quand elle regarde dehors ?', 'What happens when she looks outside?'), [('Elle s’endort', 'She falls asleep'), ('Le miroir se fend', 'The mirror cracks'), ('Lancelot s’arrête', 'Lancelot stops')], 1),
  ]),
  CH('shalott-3', ('The boat to Camelot', 'La barque vers Camelot'), [
    [S('Sensing that her end was near, she found a boat beneath a willow, wrote her name upon its prow and lay down in it.', 'Pressentant sa fin proche, elle trouva une barque sous un saule, inscrivit son nom sur la proue et s’y allongea.'),
     S('The boat drifted down the river towards Camelot as she sang her last song, her voice growing ever fainter.', 'La barque dériva sur la rivière vers Camelot tandis qu’elle chantait son dernier chant, d’une voix de plus en plus faible.')],
    [S('By the time it reached the town, she had died. Knights and ladies gathered on the bank, wondering who she might have been.', 'Le temps qu’elle atteigne la ville, la dame était morte. Chevaliers et dames se rassemblèrent sur la rive, se demandant qui elle avait bien pu être.'),
     S('Only Lancelot paused to look at her face, and, unaware of the part he had played, said simply that she had a lovely face.', 'Seul Lancelot s’arrêta pour regarder son visage et, ignorant le rôle qu’il avait joué, dit simplement qu’elle avait un beau visage.')],
  ], [
    W('sensing', '/ˈsensɪŋ/', 'pressentant', 'sensing'),
    W('willow', '/ˈwɪləʊ/', 'saule', 'willow'),
    W('prow', '/praʊ/', 'proue', 'prow'),
    W('drifted', '/ˈdrɪftɪd/', 'dériva', 'drifted'),
    W('fainter', '/ˈfeɪntə/', 'plus faible', 'fainter'),
    W('unaware', '/ˌʌnəˈweə/', 'ignorant, inconscient', 'unaware'),
  ], [
    Q(('Qu’écrit la dame sur la barque ?', 'What does the lady write on the boat?'), [('Son nom', 'Her name'), ('Une lettre à Lancelot', 'A letter to Lancelot'), ('Le nom de Camelot', 'The name of Camelot')], 0),
    Q(('Que sait Lancelot de son rôle dans l’histoire ?', 'What does Lancelot know about his part in the story?'), [('Il se sent coupable', 'He feels guilty'), ('Il n’en sait rien', 'He knows nothing of it'), ('Il l’avait prévu', 'He had planned it')], 1),
  ]),
])

# ═════════════════════════ C1 : Thomas the Rhymer ═════════════════════════
RHYMER = STORY('thomas-rhymer', 'H', 'C1', '#3E7A5A', ('Thomas the Rhymer', 'Thomas le Rimeur'),
  ('Le poète écossais Thomas d’Erceldoune rencontre la reine d’Elfland sous un arbre. Il la suit dans son royaume, où le temps ne s’écoule pas comme ailleurs.', 'The Scottish poet Thomas of Erceldoune meets the Queen of Elfland beneath a tree. He follows her into her kingdom, where time does not pass as it does elsewhere.'), [
  CH('rhymer-1', ('The Eildon Tree', 'L’arbre d’Eildon'), [
    [S('Thomas of Erceldoune, a poet renowned throughout the Borders, was resting beneath the Eildon Tree when a lady of dazzling beauty rode towards him.', 'Thomas d’Erceldoune, poète renommé dans tous les Borders, se reposait sous l’arbre d’Eildon quand une dame d’une beauté éblouissante s’avança vers lui à cheval.'),
     S('Her horse was white as milk, and from its mane hung fifty silver bells that rang with every step.', 'Son cheval était blanc comme le lait, et à sa crinière pendaient cinquante clochettes d’argent qui tintaient à chaque pas.')],
    [S('Mistaking her for the Queen of Heaven, Thomas knelt before her, only to be told that she was the Queen of fair Elfland.', 'La prenant pour la Reine des Cieux, Thomas s’agenouilla devant elle, avant d’apprendre qu’elle était la reine de la belle Elfland.'),
     S('Bold, albeit unwise, he kissed her, thereby binding himself to serve her for seven years.', 'Audacieux, bien qu’imprudent, il l’embrassa, se liant ainsi à elle pour la servir sept ans.')],
  ], [
    W('renowned', '/rɪˈnaʊnd/', 'renommé', 'renowned'),
    W('dazzling', '/ˈdæzlɪŋ/', 'éblouissant', 'dazzling'),
    W('mane', '/meɪn/', 'crinière', 'mane'),
    W('knelt', '/nelt/', 's’agenouilla', 'knelt'),
    W('bold', '/bəʊld/', 'audacieux', 'bold'),
    W('binding', '/ˈbaɪndɪŋ/', 'liant, engageant', 'binding'),
  ], [
    Q(('Pour qui Thomas prend-il d’abord la dame ?', 'Who does Thomas first take the lady to be?'), [('La Reine des Cieux', 'The Queen of Heaven'), ('Une paysanne', 'A peasant'), ('La reine d’Écosse', 'The Queen of Scotland')], 0),
    Q(('Quelle est la conséquence du baiser ?', 'What is the consequence of the kiss?'), [('Il devient roi', 'He becomes king'), ('Il doit la servir sept ans', 'He must serve her for seven years'), ('Il perd la voix', 'He loses his voice')], 1),
  ]),
  CH('rhymer-2', ('Three roads', 'Trois chemins'), [
    [S('They rode for forty days through darkness, wading through rivers of blood, until they came to a place where three roads met.', 'Ils chevauchèrent quarante jours dans l’obscurité, traversant à gué des rivières de sang, jusqu’à un lieu où trois chemins se rejoignaient.'),
     S('The first, narrow and thorny, was the path of righteousness; the second, broad and easy, led to wickedness.', 'Le premier, étroit et épineux, était le chemin de la vertu ; le second, large et facile, menait au vice.')],
    [S('The third, winding up a hillside of ferns, was the road to fair Elfland, and it was this one that they took.', 'Le troisième, serpentant sur un coteau de fougères, était la route de la belle Elfland, et c’est celui qu’ils prirent.'),
     S('“Should you speak a single word while you are in my land,” the Queen warned, “you will never return to your own.”', '« Si tu prononces un seul mot pendant ton séjour dans mon royaume, avertit la reine, tu ne reverras jamais le tien. »')],
  ], [
    W('wading', '/ˈweɪdɪŋ/', 'traversant à gué', 'wading'),
    W('thorny', '/ˈθɔːni/', 'épineux', 'thorny'),
    W('righteousness', '/ˈraɪtʃəsnəs/', 'vertu, droiture', 'righteousness'),
    W('wickedness', '/ˈwɪkɪdnəs/', 'méchanceté, vice', 'wickedness'),
    W('winding', '/ˈwaɪndɪŋ/', 'sinueux', 'winding'),
    W('ferns', '/fɜːnz/', 'fougères', 'ferns'),
  ], [
    Q(('Quel chemin mène à Elfland ?', 'Which road leads to Elfland?'), [('Le chemin sinueux parmi les fougères', 'The winding road among the ferns'), ('Le chemin étroit et épineux', 'The narrow, thorny road'), ('Le chemin large et facile', 'The broad, easy road')], 0),
    Q(('Que ne doit pas faire Thomas à Elfland ?', 'What must Thomas not do in Elfland?'), [('Manger', 'Eat'), ('Prononcer un seul mot', 'Speak a single word'), ('Dormir', 'Sleep')], 1),
  ]),
  CH('rhymer-3', ('The gift of truth', 'Le don de vérité'), [
    [S('Thomas kept silent for what seemed to him three days, only to discover that seven years had passed.', 'Thomas garda le silence pendant ce qui lui sembla trois jours, avant de découvrir que sept années s’étaient écoulées.'),
     S('Before sending him home, the Queen gave him a tongue that could never lie, a gift he considered, to some extent, a burden.', 'Avant de le renvoyer chez lui, la reine lui donna une langue incapable de mentir, un don qu’il considéra, dans une certaine mesure, comme un fardeau.')],
    [S('Back in Scotland, he became famous for his prophecies, many of which were said to have come true.', 'De retour en Écosse, il devint célèbre pour ses prophéties, dont beaucoup se seraient réalisées.'),
     S('Years later, when two white deer appeared at his door, he followed them into the forest and was never seen again.', 'Des années plus tard, quand deux cerfs blancs apparurent à sa porte, il les suivit dans la forêt et on ne le revit jamais.')],
  ], [
    W('silent', '/ˈsaɪlənt/', 'silencieux', 'silent'),
    W('tongue', '/tʌŋ/', 'langue (organe)', 'tongue'),
    W('burden', '/ˈbɜːdn/', 'fardeau', 'burden'),
    W('prophecies', '/ˈprɒfəsiz/', 'prophéties', 'prophecies'),
    W('come true', '/kʌm truː/', 'se réaliser', 'come true'),
    W('deer', '/dɪə/', 'cerf(s)', 'deer'),
  ], [
    Q(('Combien de temps Thomas est-il vraiment resté à Elfland ?', 'How long did Thomas really stay in Elfland?'), [('Sept ans', 'Seven years'), ('Trois jours', 'Three days'), ('Quarante jours', 'Forty days')], 0),
    Q(('Quel don reçoit-il de la reine ?', 'What gift does he receive from the Queen?'), [('Une épée magique', 'A magic sword'), ('Une langue qui ne peut mentir', 'A tongue that cannot lie'), ('Un cheval blanc', 'A white horse')], 1),
  ]),
])

EN_STORIES = [GOLDILOCKS, WHITTINGTON, SWORD, JACK, CANUTE, ROBIN, PEDLAR, TAMLIN, GELERT, SHALOTT, RHYMER]
EN_LEVELS = ('A1', 'A2', 'B1', 'B2', 'C1')

data = json.load(open(P, encoding='utf-8'))
data['stories'] = [s for s in data['stories'] if s['level'] not in EN_LEVELS] + EN_STORIES
data.setdefault('notices', {})['en'] = {'fr': 'Contes et légendes britanniques (domaine public), réécrits en anglais simple pour Koto Quest. La prononciation des mots est notée en alphabet phonétique.', 'en': 'British folk tales and legends (public domain), retold in simple English for Koto Quest. Word pronunciation is shown in phonetic script.'}
slugs = [c['slug'] for s in data['stories'] for c in s['chapters']]
assert len(slugs) == len(set(slugs)), 'slug de chapitre en double'
for s in EN_STORIES:
    for c in s['chapters']:
        assert len(c['words']) >= 6, c['slug']
        for q in c['questions']:
            assert 0 <= q['answer'] < len(q['choices'])
json.dump(data, open(P, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('Contes anglais :', len(EN_STORIES), 'contes,', sum(len(s['chapters']) for s in EN_STORIES), 'chapitres')
