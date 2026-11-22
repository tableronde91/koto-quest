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

EN_STORIES = [GOLDILOCKS, WHITTINGTON, SWORD, JACK, CANUTE]
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
