# Lecture en espagnol : contes populaires d'Espagne (domaine public), réécrits en espagnol simple.
# Ajoute (ou remplace) les contes espagnols dans content/reading/stories.json, sans toucher aux autres langues.
# Usage : python3 scripts/es-reading.py
import json, os
ROOT = os.path.join(os.path.dirname(__file__), '..')
P = os.path.join(ROOT, 'content/reading/stories.json')

def S(es, fr, en):
    """Phrase : le texte à lire et à prononcer est le même (l'espagnol se lit comme il s'écrit)."""
    return {'jp': es, 'fr': fr, 'en': en, 'kana': es}

def W(word, ipa, fr, en):
    return {'jp': word, 'reading': ipa, 'fr': fr, 'en': en}

def Q(q, choices, answer):
    return {'q': {'fr': q[0], 'en': q[1]}, 'choices': [{'fr': f, 'en': e} for f, e in choices], 'answer': answer}

def CH(slug, title, paragraphs, words, questions):
    es, fr, en = title
    return {'slug': slug, 'title': {'jp': es, 'fr': fr, 'en': en}, 'paragraphs': paragraphs, 'words': words, 'questions': questions}

def STORY(slug, glyph, level, color, title, summary, chapters):
    es, fr, en = title
    return {'slug': slug, 'glyph': glyph, 'level': level, 'color': color, 'title': {'jp': es, 'fr': fr, 'en': en}, 'summary': {'fr': summary[0], 'en': summary[1]}, 'chapters': chapters}

# ═════════════════════════ El medio pollito ═════════════════════════
POLLITO = STORY('medio-pollito', 'm', 'DELEA1', '#E2A23B', ('El medio pollito', 'Le demi-poussin', 'Half-Chick'),
  ('Un petit poussin né avec une seule patte, une seule aile et un seul œil part voir le roi à Madrid.', 'A little chick born with only one leg, one wing and one eye sets off to see the king in Madrid.'), [
  CH('medio-pollito-1', ('Un pollito diferente', 'Un poussin différent', 'A different chick'), [
    [S('Había una vez una gallina con doce pollitos.', 'Il était une fois une poule qui avait douze poussins.', 'Once upon a time there was a hen with twelve chicks.'),
     S('Once pollitos son normales, pero uno es diferente.', 'Onze poussins sont normaux, mais un est différent.', 'Eleven chicks are normal, but one is different.'),
     S('Tiene una pata, un ala y un ojo: es medio pollito.', 'Il a une patte, une aile et un œil : c’est un demi-poussin.', 'He has one leg, one wing and one eye: he is half a chick.')],
    [S('Un día, el medio pollito dice: «Mamá, me voy a Madrid. Quiero ver al rey».', 'Un jour, le demi-poussin dit : « Maman, je m’en vais à Madrid. Je veux voir le roi. »', 'One day, Half-Chick says: “Mum, I’m going to Madrid. I want to see the king.”'),
     S('La gallina está triste, pero el pollito sale de casa muy contento.', 'La poule est triste, mais le poussin quitte la maison très content.', 'The hen is sad, but the chick leaves home very happy.')],
  ], [
    W('la gallina', '/la ɡaˈʎina/', 'la poule', 'the hen'),
    W('el pollito', '/el poˈʎito/', 'le poussin', 'the chick'),
    W('la pata', '/la ˈpata/', 'la patte', 'the leg (of an animal)'),
    W('el ala', '/el ˈala/', 'l’aile', 'the wing'),
    W('el ojo', '/el ˈoxo/', 'l’œil', 'the eye'),
    W('el rey', '/el rei/', 'le roi', 'the king'),
  ], [
    Q(('Combien de poussins a la poule ?', 'How many chicks does the hen have?'), [('Douze', 'Twelve'), ('Deux', 'Two'), ('Onze', 'Eleven')], 0),
    Q(('Où veut aller le demi-poussin ?', 'Where does Half-Chick want to go?'), [('À Madrid', 'To Madrid'), ('À la rivière', 'To the river'), ('Chez sa grand-mère', 'To his grandmother’s')], 0),
  ]),
  CH('medio-pollito-2', ('El agua, el fuego y el viento', 'L’eau, le feu et le vent', 'Water, fire and wind'), [
    [S('En el camino, el agua del río le dice: «Pollito, ayúdame, por favor».', 'En chemin, l’eau de la rivière lui dit : « Petit poussin, aide-moi, s’il te plaît. »', 'On the way, the river water says to him: “Little chick, help me, please.”'),
     S('El fuego y el viento también piden ayuda.', 'Le feu et le vent demandent aussi de l’aide.', 'Fire and wind also ask for help.'),
     S('Pero el pollito contesta: «No tengo tiempo, voy a ver al rey».', 'Mais le poussin répond : « Je n’ai pas le temps, je vais voir le roi. »', 'But the chick answers: “I don’t have time, I’m going to see the king.”')],
    [S('En el palacio, el cocinero lo mete en una olla con agua.', 'Au palais, le cuisinier le met dans une marmite pleine d’eau.', 'At the palace, the cook puts him in a pot of water.'),
     S('El agua y el fuego no lo ayudan, pero el viento sí: lo sube muy alto.', 'L’eau et le feu ne l’aident pas, mais le vent, si : il l’emporte très haut.', 'The water and the fire don’t help him, but the wind does: it carries him up very high.'),
     S('Y desde entonces, el medio pollito vive en lo alto de las torres: es la veleta.', 'Et depuis, le demi-poussin vit en haut des tours : c’est la girouette.', 'And since then, Half-Chick has lived at the top of towers: he is the weathervane.')],
  ], [
    W('el camino', '/el kaˈmino/', 'le chemin', 'the way, the path'),
    W('el río', '/el ˈri.o/', 'la rivière', 'the river'),
    W('el fuego', '/el ˈfweɣo/', 'le feu', 'the fire'),
    W('el viento', '/el ˈbjento/', 'le vent', 'the wind'),
    W('la olla', '/la ˈoʎa/', 'la marmite', 'the pot'),
    W('la veleta', '/la beˈleta/', 'la girouette', 'the weathervane'),
  ], [
    Q(('Pourquoi le poussin n’aide-t-il personne ?', 'Why doesn’t the chick help anyone?'), [('Il n’a pas le temps', 'He has no time'), ('Il est malade', 'He is ill'), ('Il a peur', 'He is afraid')], 0),
    Q(('Que devient le demi-poussin à la fin ?', 'What does Half-Chick become in the end?'), [('Une girouette', 'A weathervane'), ('Un roi', 'A king'), ('Un cuisinier', 'A cook')], 0),
  ]),
])

# ═════════════════════════ La ratita presumida ═════════════════════════
RATITA = STORY('ratita-presumida', 'r', 'DELEA1', '#C8323F', ('La ratita presumida', 'La petite souris coquette', 'The vain little mouse'),
  ('Une petite souris trouve une pièce d’or, s’achète un ruban rouge… et tous les animaux veulent l’épouser.', 'A little mouse finds a gold coin, buys a red ribbon… and every animal wants to marry her.'), [
  CH('ratita-presumida-1', ('Una moneda de oro', 'Une pièce d’or', 'A gold coin'), [
    [S('Había una vez una ratita muy limpia y muy presumida.', 'Il était une fois une petite souris très propre et très coquette.', 'Once upon a time there was a very clean and very vain little mouse.'),
     S('Un día, barriendo la puerta de su casa, encuentra una moneda de oro.', 'Un jour, en balayant devant sa porte, elle trouve une pièce d’or.', 'One day, sweeping in front of her door, she finds a gold coin.'),
     S('«¿Qué compro? ¿Caramelos? No. ¡Un lazo rojo para mi cola!»', '« Qu’est-ce que j’achète ? Des bonbons ? Non. Un ruban rouge pour ma queue ! »', '“What shall I buy? Sweets? No. A red ribbon for my tail!”')],
    [S('La ratita se pone el lazo y se sienta en la ventana.', 'La petite souris met le ruban et s’assoit à la fenêtre.', 'The little mouse puts on the ribbon and sits at the window.'),
     S('Todos los animales del pueblo pasan y la miran.', 'Tous les animaux du village passent et la regardent.', 'All the animals in the village walk by and look at her.')],
  ], [
    W('la ratita', '/la raˈtita/', 'la petite souris', 'the little mouse'),
    W('presumida', '/pɾesuˈmida/', 'coquette, vaniteuse', 'vain'),
    W('la moneda', '/la moˈneða/', 'la pièce (de monnaie)', 'the coin'),
    W('el oro', '/el ˈoɾo/', 'l’or', 'gold'),
    W('el lazo', '/el ˈlaθo/', 'le ruban, le nœud', 'the ribbon, the bow'),
    W('la ventana', '/la benˈtana/', 'la fenêtre', 'the window'),
  ], [
    Q(('Que trouve la petite souris ?', 'What does the little mouse find?'), [('Une pièce d’or', 'A gold coin'), ('Un ruban', 'A ribbon'), ('Des bonbons', 'Sweets')], 0),
    Q(('Qu’achète-t-elle ?', 'What does she buy?'), [('Un ruban rouge', 'A red ribbon'), ('Des bonbons', 'Sweets'), ('Une robe', 'A dress')], 0),
  ]),
  CH('ratita-presumida-2', ('¿Y por las noches, qué haces?', 'Et la nuit, que fais-tu ?', 'And at night, what do you do?'), [
    [S('Llega el burro: «Ratita, ¿te quieres casar conmigo?». «¿Y por las noches, qué haces?» «¡Hiooo, hiooo!» «¡No, que me asustas!»', 'L’âne arrive : « Petite souris, veux-tu m’épouser ? » « Et la nuit, que fais-tu ? » « Hi-han, hi-han ! » « Non, tu me fais peur ! »', 'The donkey comes: “Little mouse, will you marry me?” “And at night, what do you do?” “Hee-haw, hee-haw!” “No, you frighten me!”'),
     S('El perro hace «guau, guau» y el gallo hace «quiquiriquí». La ratita dice que no a todos.', 'Le chien fait « ouaf, ouaf » et le coq fait « cocorico ». La petite souris dit non à tous.', 'The dog goes “woof, woof” and the rooster goes “cock-a-doodle-doo”. The little mouse says no to them all.')],
    [S('Por fin llega un gato muy elegante. «¿Y por las noches, qué haces?» «Dormir y callar».', 'Enfin arrive un chat très élégant. « Et la nuit, que fais-tu ? » « Dormir et me taire. »', 'At last a very elegant cat arrives. “And at night, what do you do?” “Sleep and keep quiet.”'),
     S('La ratita se casa con el gato… pero por la noche el gato quiere comérsela.', 'La petite souris épouse le chat… mais la nuit, le chat veut la manger.', 'The little mouse marries the cat… but at night the cat wants to eat her.'),
     S('Por suerte, su amigo el ratón la salva. Y la ratita aprende a no ser tan presumida.', 'Heureusement, son ami le souriceau la sauve. Et la petite souris apprend à ne plus être si coquette.', 'Luckily, her friend the mouse saves her. And the little mouse learns not to be so vain.')],
  ], [
    W('casarse', '/kaˈsaɾse/', 'se marier', 'to get married'),
    W('el gallo', '/el ˈɡaʎo/', 'le coq', 'the rooster'),
    W('asustar', '/asusˈtaɾ/', 'faire peur', 'to frighten'),
    W('dormir', '/doɾˈmiɾ/', 'dormir', 'to sleep'),
    W('callar', '/kaˈʎaɾ/', 'se taire', 'to keep quiet'),
    W('por suerte', '/poɾ ˈsweɾte/', 'heureusement', 'luckily'),
  ], [
    Q(('Pourquoi la souris refuse-t-elle l’âne ?', 'Why does the mouse refuse the donkey?'), [('Il lui fait peur', 'He frightens her'), ('Il est trop vieux', 'He is too old'), ('Il est pauvre', 'He is poor')], 0),
    Q(('Qui sauve la petite souris ?', 'Who saves the little mouse?'), [('Son ami le souriceau', 'Her friend the mouse'), ('Le coq', 'The rooster'), ('Le chat', 'The cat')], 0),
  ]),
])

# ═════════════════════════ Los molinos de viento (d'après Cervantes, 1605) ═════════════════════════
MOLINOS = STORY('molinos-de-viento', 'q', 'DELEA1', '#6E5A3A', ('Los molinos de viento', 'Les moulins à vent', 'The windmills'),
  ('Don Quichotte croit voir des géants dans la plaine. Sancho voit des moulins. Qui a raison ? D’après Cervantes.', 'Don Quixote thinks he sees giants on the plain. Sancho sees windmills. Who is right? After Cervantes.'), [
  CH('molinos-de-viento-1', ('Gigantes en el campo', 'Des géants dans la campagne', 'Giants in the countryside'), [
    [S('Don Quijote y Sancho Panza van por el campo de La Mancha.', 'Don Quichotte et Sancho Panza vont à travers la campagne de la Manche.', 'Don Quixote and Sancho Panza ride across the countryside of La Mancha.'),
     S('De pronto, don Quijote ve treinta o cuarenta molinos de viento.', 'Soudain, don Quichotte voit trente ou quarante moulins à vent.', 'Suddenly, Don Quixote sees thirty or forty windmills.'),
     S('«¡Mira, Sancho! Allí hay unos gigantes enormes. Voy a luchar contra ellos».', '« Regarde, Sancho ! Là-bas, il y a des géants énormes. Je vais les combattre. »', '“Look, Sancho! Over there are some enormous giants. I am going to fight them.”')],
    [S('«¿Qué gigantes?», pregunta Sancho.', '« Quels géants ? », demande Sancho.', '“What giants?” asks Sancho.'),
     S('«Esos de allí, con los brazos largos».', '« Ceux-là, avec leurs longs bras. »', '“Those over there, with the long arms.”'),
     S('«Señor, no son gigantes, son molinos. Los brazos son las aspas».', '« Monsieur, ce ne sont pas des géants, ce sont des moulins. Les bras, ce sont les ailes. »', '“Sir, they are not giants, they are windmills. The arms are the sails.”')],
  ], [
    W('el campo', '/el ˈkampo/', 'la campagne, les champs', 'the countryside, the fields'),
    W('de pronto', '/de ˈpɾonto/', 'soudain', 'suddenly'),
    W('el gigante', '/el xiˈɣante/', 'le géant', 'the giant'),
    W('enorme', '/eˈnoɾme/', 'énorme', 'enormous'),
    W('luchar', '/luˈtʃaɾ/', 'combattre, lutter', 'to fight'),
    W('las aspas', '/las ˈaspas/', 'les ailes (d’un moulin)', 'the sails (of a windmill)'),
  ], [
    Q(('Que voit don Quichotte ?', 'What does Don Quixote see?'), [('Des géants', 'Giants'), ('Des moulins', 'Windmills'), ('Des soldats', 'Soldiers')], 0),
    Q(('Selon Sancho, que sont les « bras » ?', 'According to Sancho, what are the “arms”?'), [('Les ailes des moulins', 'The windmills’ sails'), ('Des arbres', 'Trees'), ('Des lances', 'Spears')], 0),
  ]),
  CH('molinos-de-viento-2', ('El caballero cae', 'Le chevalier tombe', 'The knight falls'), [
    [S('Pero don Quijote no escucha. Corre con su caballo Rocinante contra el primer molino.', 'Mais don Quichotte n’écoute pas. Il fonce avec son cheval Rossinante contre le premier moulin.', 'But Don Quixote does not listen. He charges on his horse Rocinante at the first windmill.'),
     S('En ese momento hace mucho viento y las aspas giran.', 'À ce moment-là, il y a beaucoup de vent et les ailes tournent.', 'At that moment the wind is strong and the sails turn.'),
     S('La lanza se rompe y el caballero cae al suelo.', 'La lance se brise et le chevalier tombe par terre.', 'The lance breaks and the knight falls to the ground.')],
    [S('Sancho corre a ayudarlo: «¿No le digo, señor, que son molinos?».', 'Sancho court l’aider : « Je vous l’avais bien dit, monsieur, ce sont des moulins ! »', 'Sancho runs to help him: “Didn’t I tell you, sir, that they are windmills?”'),
     S('Don Quijote está cansado y le duele todo el cuerpo, pero contesta: «Un mago malo convierte a los gigantes en molinos».', 'Don Quichotte est fatigué et a mal partout, mais il répond : « Un méchant magicien change les géants en moulins. »', 'Don Quixote is tired and aches all over, but he answers: “An evil wizard turns the giants into windmills.”')],
  ], [
    W('el caballo', '/el kaˈβaʎo/', 'le cheval', 'the horse'),
    W('girar', '/xiˈɾaɾ/', 'tourner', 'to turn, to spin'),
    W('la lanza', '/la ˈlanθa/', 'la lance', 'the lance'),
    W('romperse', '/romˈpeɾse/', 'se briser, se casser', 'to break'),
    W('el suelo', '/el ˈswelo/', 'le sol', 'the ground'),
    W('el mago', '/el ˈmaɣo/', 'le magicien', 'the wizard'),
  ], [
    Q(('Que se passe-t-il quand don Quichotte attaque ?', 'What happens when Don Quixote attacks?'), [('Sa lance se brise et il tombe', 'His lance breaks and he falls'), ('Il gagne', 'He wins'), ('Le moulin s’arrête', 'The windmill stops')], 0),
    Q(('Comment don Quichotte explique-t-il les moulins ?', 'How does Don Quixote explain the windmills?'), [('Un magicien a changé les géants', 'A wizard changed the giants'), ('Il s’est trompé', 'He made a mistake'), ('Sancho a menti', 'Sancho lied')], 0),
  ]),
])

# ═════════════════════════ Juan sin Miedo (DELE A2, au passé) ═════════════════════════
JUAN = STORY('juan-sin-miedo', 'j', 'DELEA2', '#4A5A8A', ('Juan sin Miedo', 'Jean sans Peur', 'Fearless John'),
  ('Un garçon qui n’a jamais eu peur part dans le monde pour apprendre ce qu’est la peur… et passe trois nuits dans un château hanté.', 'A boy who has never been afraid sets out into the world to learn what fear is… and spends three nights in a haunted castle.'), [
  CH('juan-sin-miedo-1', ('Un chico valiente', 'Un garçon courageux', 'A brave boy'), [
    [S('Hace muchos años, en un pueblo de Castilla, vivía un chico que se llamaba Juan.', 'Il y a bien longtemps, dans un village de Castille, vivait un garçon qui s’appelait Juan.', 'Many years ago, in a village in Castile, there lived a boy called Juan.'),
     S('Juan nunca tenía miedo: ni de la noche, ni de los lobos, ni de las historias de fantasmas.', 'Juan n’avait jamais peur : ni de la nuit, ni des loups, ni des histoires de fantômes.', 'Juan was never afraid: not of the night, not of wolves, not of ghost stories.'),
     S('Por eso, en el pueblo todos lo llamaban Juan sin Miedo.', 'C’est pourquoi, au village, tout le monde l’appelait Juan sans Peur.', 'That is why everyone in the village called him Fearless John.')],
    [S('Un día, Juan le dijo a su padre: «Quiero saber qué es el miedo. Me voy a buscarlo».', 'Un jour, Juan dit à son père : « Je veux savoir ce qu’est la peur. Je pars la chercher. »', 'One day Juan said to his father: “I want to know what fear is. I’m going to look for it.”'),
     S('Su padre le dio un poco de dinero y un trozo de pan, y Juan salió del pueblo.', 'Son père lui donna un peu d’argent et un morceau de pain, et Juan quitta le village.', 'His father gave him a little money and a piece of bread, and Juan left the village.'),
     S('Caminó durante tres días hasta que llegó a una ciudad con un castillo muy viejo.', 'Il marcha pendant trois jours jusqu’à une ville où se dressait un très vieux château.', 'He walked for three days until he came to a town with a very old castle.')],
  ], [
    W('el miedo', '/el ˈmjeðo/', 'la peur', 'fear'),
    W('el lobo', '/el ˈloβo/', 'le loup', 'the wolf'),
    W('el fantasma', '/el fanˈtasma/', 'le fantôme', 'the ghost'),
    W('buscar', '/busˈkaɾ/', 'chercher', 'to look for'),
    W('el trozo', '/el ˈtɾoθo/', 'le morceau', 'the piece'),
    W('el castillo', '/el kasˈtiʎo/', 'le château fort', 'the castle'),
  ], [
    Q(('Pourquoi appelait-on Juan « sans Peur » ?', 'Why was Juan called “Fearless”?'), [('Il n’avait jamais peur', 'He was never afraid'), ('Il était très fort', 'He was very strong'), ('Il était le fils du roi', 'He was the king’s son')], 0),
    Q(('Que voulait apprendre Juan ?', 'What did Juan want to learn?'), [('Ce qu’est la peur', 'What fear is'), ('À lire', 'To read'), ('Un métier', 'A trade')], 0),
  ]),
  CH('juan-sin-miedo-2', ('Tres noches en el castillo', 'Trois nuits au château', 'Three nights in the castle'), [
    [S('El rey de la ciudad dijo: «Nadie puede dormir en ese castillo. Si pasas tres noches allí, te doy la mano de mi hija».', 'Le roi de la ville dit : « Personne ne peut dormir dans ce château. Si tu y passes trois nuits, je te donne la main de ma fille. »', 'The king of the town said: “No one can sleep in that castle. If you spend three nights there, I will give you my daughter’s hand.”'),
     S('La primera noche, mientras Juan cenaba junto al fuego, unos gatos negros entraron por la ventana.', 'La première nuit, pendant que Juan dînait près du feu, des chats noirs entrèrent par la fenêtre.', 'On the first night, while Juan was having dinner by the fire, some black cats came in through the window.'),
     S('La segunda noche, oyó ruidos de cadenas, pero se rió y siguió durmiendo.', 'La deuxième nuit, il entendit des bruits de chaînes, mais il rit et continua à dormir.', 'On the second night, he heard the rattling of chains, but he laughed and went on sleeping.')],
    [S('La tercera noche, un fantasma le enseñó un tesoro escondido debajo del suelo.', 'La troisième nuit, un fantôme lui montra un trésor caché sous le plancher.', 'On the third night, a ghost showed him a treasure hidden under the floor.'),
     S('Juan se casó con la princesa, pero seguía sin saber qué era el miedo.', 'Juan épousa la princesse, mais il ne savait toujours pas ce qu’était la peur.', 'Juan married the princess, but he still did not know what fear was.'),
     S('Una mañana, mientras dormía, la princesa le echó un cubo de agua fría con peces… y por fin Juan gritó: «¡Ay, qué miedo!».', 'Un matin, pendant qu’il dormait, la princesse lui renversa un seau d’eau froide plein de poissons… et Juan cria enfin : « Aïe, quelle peur ! »', 'One morning, while he was asleep, the princess poured a bucket of cold water full of fish over him… and at last Juan shouted: “Oh, how scary!”')],
  ], [
    W('la cadena', '/la kaˈðena/', 'la chaîne', 'the chain'),
    W('reírse', '/reˈiɾse/', 'rire', 'to laugh'),
    W('el tesoro', '/el teˈsoɾo/', 'le trésor', 'the treasure'),
    W('esconder', '/eskonˈdeɾ/', 'cacher', 'to hide'),
    W('el cubo', '/el ˈkuβo/', 'le seau', 'the bucket'),
    W('gritar', '/ɡɾiˈtaɾ/', 'crier', 'to shout'),
  ], [
    Q(('Que montra le fantôme à Juan ?', 'What did the ghost show Juan?'), [('Un trésor caché', 'A hidden treasure'), ('Une porte secrète', 'A secret door'), ('Le chemin du village', 'The way to the village')], 0),
    Q(('Comment Juan apprit-il enfin la peur ?', 'How did Juan finally learn fear?'), [('Avec un seau d’eau froide et des poissons', 'With a bucket of cold water and fish'), ('Avec un loup', 'With a wolf'), ('Avec le roi', 'With the king')], 0),
  ]),
])

# ═════════════════════════ El Caballero de la Blanca Luna (Don Quichotte, IIe partie ; DELE A2) ═════════════════════════
BLANCA = STORY('blanca-luna', 'l', 'DELEA2', '#2E7DA8', ('El Caballero de la Blanca Luna', 'Le chevalier de la Blanche Lune', 'The Knight of the White Moon'),
  ('À Barcelone, un mystérieux chevalier défie don Quichotte sur la plage. Le vaincu devra rentrer chez lui pour un an.', 'In Barcelona, a mysterious knight challenges Don Quixote on the beach. The loser must go home for a year.'), [
  CH('blanca-luna-1', ('El desafío en la playa', 'Le défi sur la plage', 'The challenge on the beach'), [
    [S('Una mañana, don Quijote paseaba por la playa de Barcelona con su armadura.', 'Un matin, don Quichotte se promenait sur la plage de Barcelone avec son armure.', 'One morning, Don Quixote was walking along the beach in Barcelona in his armour.'),
     S('De repente, llegó un caballero con una luna blanca pintada en el escudo.', 'Soudain, arriva un chevalier avec une lune blanche peinte sur son bouclier.', 'Suddenly a knight arrived with a white moon painted on his shield.'),
     S('«Soy el Caballero de la Blanca Luna —dijo—. Mi dama es más hermosa que Dulcinea».', '« Je suis le chevalier de la Blanche Lune, dit-il. Ma dame est plus belle que Dulcinée. »', '“I am the Knight of the White Moon,” he said. “My lady is more beautiful than Dulcinea.”')],
    [S('Don Quijote se enfadó mucho y aceptó el combate.', 'Don Quichotte se mit très en colère et accepta le combat.', 'Don Quixote got very angry and accepted the duel.'),
     S('Las condiciones eran claras: si perdía don Quijote, tenía que volver a su pueblo y quedarse allí un año.', 'Les conditions étaient claires : si don Quichotte perdait, il devait rentrer dans son village et y rester un an.', 'The terms were clear: if Don Quixote lost, he had to go back to his village and stay there for a year.'),
     S('Sancho estaba muy nervioso y miraba el mar sin decir nada.', 'Sancho était très nerveux et regardait la mer sans rien dire.', 'Sancho was very nervous and stared at the sea without saying a word.')],
  ], [
    W('la armadura', '/la aɾmaˈðuɾa/', 'l’armure', 'the armour'),
    W('el escudo', '/el esˈkuðo/', 'le bouclier', 'the shield'),
    W('la dama', '/la ˈdama/', 'la dame', 'the lady'),
    W('hermoso', '/eɾˈmoso/', 'beau, magnifique', 'beautiful'),
    W('enfadarse', '/enfaˈðaɾse/', 'se fâcher', 'to get angry'),
    W('aceptar', '/aθepˈtaɾ/', 'accepter', 'to accept'),
  ], [
    Q(('Qu’y avait-il sur le bouclier du chevalier ?', 'What was on the knight’s shield?'), [('Une lune blanche', 'A white moon'), ('Un soleil', 'A sun'), ('Un moulin', 'A windmill')], 0),
    Q(('Que devait faire don Quichotte s’il perdait ?', 'What did Don Quixote have to do if he lost?'), [('Rentrer chez lui pour un an', 'Go home for a year'), ('Quitter l’Espagne', 'Leave Spain'), ('Donner son cheval', 'Give up his horse')], 0),
  ]),
  CH('blanca-luna-2', ('La vuelta a casa', 'Le retour à la maison', 'The return home'), [
    [S('Los dos caballeros corrieron uno contra otro. El caballo del desconocido era más rápido y más fuerte que Rocinante.', 'Les deux chevaliers foncèrent l’un sur l’autre. Le cheval de l’inconnu était plus rapide et plus fort que Rossinante.', 'The two knights charged at each other. The stranger’s horse was faster and stronger than Rocinante.'),
     S('Don Quijote cayó al suelo, pero no quiso decir que su dama era menos hermosa.', 'Don Quichotte tomba par terre, mais il refusa de dire que sa dame était moins belle.', 'Don Quixote fell to the ground, but he refused to say that his lady was less beautiful.'),
     S('Entonces el caballero se quitó el casco: ¡era Sansón Carrasco, un vecino de su pueblo!', 'Alors le chevalier retira son casque : c’était Sansón Carrasco, un voisin de son village !', 'Then the knight took off his helmet: it was Sansón Carrasco, a neighbour from his village!')],
    [S('Sansón explicó: «Lo he hecho por su bien, señor. Su familia está preocupada».', 'Sansón expliqua : « Je l’ai fait pour votre bien, monsieur. Votre famille est inquiète. »', 'Sansón explained: “I did it for your own good, sir. Your family is worried.”'),
     S('Don Quijote y Sancho volvieron a la Mancha despacio, tristes pero tranquilos.', 'Don Quichotte et Sancho rentrèrent lentement dans la Manche, tristes mais apaisés.', 'Don Quixote and Sancho slowly returned to La Mancha, sad but at peace.'),
     S('En el camino, don Quijote dijo: «Sancho, ha sido el viaje más bonito de mi vida».', 'En chemin, don Quichotte dit : « Sancho, ce fut le plus beau voyage de ma vie. »', 'On the way, Don Quixote said: “Sancho, it has been the finest journey of my life.”')],
  ], [
    W('el desconocido', '/el deskonoˈθiðo/', 'l’inconnu', 'the stranger'),
    W('fuerte', '/ˈfweɾte/', 'fort', 'strong'),
    W('quitarse', '/kiˈtaɾse/', 'enlever, retirer (un vêtement)', 'to take off'),
    W('el casco', '/el ˈkasko/', 'le casque', 'the helmet'),
    W('preocupado', '/pɾeokuˈpaðo/', 'inquiet', 'worried'),
    W('despacio', '/desˈpaθjo/', 'lentement', 'slowly'),
  ], [
    Q(('Qui était le chevalier de la Blanche Lune ?', 'Who was the Knight of the White Moon?'), [('Sansón Carrasco, un voisin', 'Sansón Carrasco, a neighbour'), ('Le duc', 'The duke'), ('Un géant', 'A giant')], 0),
    Q(('Pourquoi Sansón a-t-il fait cela ?', 'Why did Sansón do it?'), [('Pour le bien de don Quichotte', 'For Don Quixote’s own good'), ('Pour gagner de l’argent', 'To win money'), ('Pour épouser Dulcinée', 'To marry Dulcinea')], 0),
  ]),
])

# ═════════════════════════ El gallo de Santo Domingo (légende du Camino ; DELE B1) ═════════════════════════
GALLO = STORY('gallo-santo-domingo', 'g', 'DELEB1', '#C8823A', ('El gallo de Santo Domingo', 'Le coq de Santo Domingo', 'The rooster of Santo Domingo'),
  ('À Santo Domingo de la Calzada, un jeune pèlerin accusé à tort est sauvé par un miracle… et par un coq rôti qui se met à chanter.', 'In Santo Domingo de la Calzada, a young pilgrim falsely accused is saved by a miracle… and by a roast rooster that starts to crow.'), [
  CH('gallo-santo-domingo-1', ('Una acusación injusta', 'Une accusation injuste', 'An unfair accusation'), [
    [S('Hace muchos siglos, una familia alemana hacía el Camino de Santiago con su hijo, un chico de dieciocho años.', 'Il y a bien des siècles, une famille allemande faisait le chemin de Saint-Jacques avec son fils, un garçon de dix-huit ans.', 'Many centuries ago, a German family was walking the Camino de Santiago with their son, a boy of eighteen.'),
     S('Una noche durmieron en una posada de Santo Domingo de la Calzada. La hija del posadero se enamoró del joven, pero él no le hizo caso.', 'Un soir, ils dormirent dans une auberge de Santo Domingo de la Calzada. La fille de l’aubergiste tomba amoureuse du jeune homme, mais il ne fit pas attention à elle.', 'One night they slept at an inn in Santo Domingo de la Calzada. The innkeeper’s daughter fell in love with the young man, but he paid no attention to her.'),
     S('Enfadada, la chica escondió una copa de plata en la mochila del peregrino y lo acusó de haberla robado.', 'Vexée, la jeune fille cacha une coupe en argent dans le sac du pèlerin et l’accusa de l’avoir volée.', 'Offended, the girl hid a silver cup in the pilgrim’s bag and accused him of stealing it.')],
    [S('Los guardias encontraron la copa y el juez condenó al chico sin escucharlo.', 'Les gardes trouvèrent la coupe et le juge condamna le garçon sans l’écouter.', 'The guards found the cup and the judge condemned the boy without listening to him.'),
     S('Sus padres, muy tristes, siguieron el Camino hasta Santiago para rezar por él.', 'Ses parents, très tristes, continuèrent le Chemin jusqu’à Saint-Jacques pour prier pour lui.', 'His parents, very sad, continued along the Camino to Santiago to pray for him.')],
  ], [
    W('la posada', '/la poˈsaða/', 'l’auberge', 'the inn'),
    W('enamorarse', '/enamoˈɾaɾse/', 'tomber amoureux', 'to fall in love'),
    W('hacer caso', '/aˈθeɾ ˈkaso/', 'faire attention, écouter', 'to pay attention'),
    W('la copa', '/la ˈkopa/', 'la coupe, le verre à pied', 'the cup, the goblet'),
    W('acusar', '/akuˈsaɾ/', 'accuser', 'to accuse'),
    W('el juez', '/el xweθ/', 'le juge', 'the judge'),
  ], [
    Q(('Pourquoi la fille de l’aubergiste accusa-t-elle le pèlerin ?', 'Why did the innkeeper’s daughter accuse the pilgrim?'), [('Il ne s’était pas intéressé à elle', 'He had paid no attention to her'), ('Il avait vraiment volé la coupe', 'He had really stolen the cup'), ('Il n’avait pas payé', 'He had not paid')], 0),
    Q(('Que firent les parents ?', 'What did the parents do?'), [('Ils continuèrent jusqu’à Saint-Jacques', 'They went on to Santiago'), ('Ils rentrèrent en Allemagne', 'They went back to Germany'), ('Ils restèrent à l’auberge', 'They stayed at the inn')], 0),
  ]),
  CH('gallo-santo-domingo-2', ('El gallo que cantó', 'Le coq qui chanta', 'The rooster that crowed'), [
    [S('A la vuelta, los padres pasaron otra vez por Santo Domingo y, para su sorpresa, su hijo seguía vivo: el santo lo había protegido.', 'Au retour, les parents repassèrent par Santo Domingo et, à leur grande surprise, leur fils était toujours en vie : le saint l’avait protégé.', 'On the way back, the parents passed through Santo Domingo again and, to their surprise, their son was still alive: the saint had protected him.'),
     S('Corrieron a casa del juez, que estaba a punto de cenar un gallo y una gallina asados.', 'Ils coururent chez le juge, qui s’apprêtait à dîner d’un coq et d’une poule rôtis.', 'They ran to the judge’s house, as he was about to dine on a roast rooster and hen.'),
     S('«Su hijo está tan vivo como este gallo que voy a comer», se rio el juez.', '« Votre fils est aussi vivant que ce coq que je vais manger », se moqua le juge.', '“Your son is as alive as this rooster I’m about to eat,” the judge laughed.')],
    [S('En ese momento, el gallo saltó del plato y se puso a cantar.', 'À ce moment-là, le coq sauta de l’assiette et se mit à chanter.', 'At that moment, the rooster jumped off the plate and began to crow.'),
     S('El juez liberó al joven y, desde entonces, en la catedral de Santo Domingo viven un gallo y una gallina blancos.', 'Le juge libéra le jeune homme et, depuis, un coq et une poule blancs vivent dans la cathédrale de Santo Domingo.', 'The judge set the young man free and, ever since, a white rooster and hen have lived in Santo Domingo cathedral.'),
     S('Por eso dice el refrán: «Santo Domingo de la Calzada, donde cantó la gallina después de asada».', 'C’est pourquoi le proverbe dit : « Santo Domingo de la Calzada, où la poule chanta après avoir été rôtie ».', 'That is why the saying goes: “Santo Domingo de la Calzada, where the hen sang after being roasted”.')],
  ], [
    W('la vuelta', '/la ˈbwelta/', 'le retour', 'the return'),
    W('a punto de', '/a ˈpunto ðe/', 'sur le point de', 'about to'),
    W('asado', '/aˈsaðo/', 'rôti', 'roast, roasted'),
    W('el gallo', '/el ˈɡaʎo/', 'le coq', 'the rooster'),
    W('saltar', '/salˈtaɾ/', 'sauter', 'to jump'),
    W('liberar', '/liβeˈɾaɾ/', 'libérer', 'to set free'),
  ], [
    Q(('Que fit le coq rôti ?', 'What did the roast rooster do?'), [('Il sauta de l’assiette et chanta', 'It jumped off the plate and crowed'), ('Il s’envola par la fenêtre', 'It flew out of the window'), ('Il resta dans l’assiette', 'It stayed on the plate')], 0),
    Q(('Qu’y a-t-il aujourd’hui dans la cathédrale ?', 'What is there in the cathedral today?'), [('Un coq et une poule blancs', 'A white rooster and hen'), ('Une coupe en argent', 'A silver cup'), ('La maison du juge', 'The judge’s house')], 0),
  ]),
])

# ═════════════════════════ La ciudad sumergida de Duio (légende de Fisterra ; DELE B1) ═════════════════════════
DUIO = STORY('ciudad-de-duio', 'd', 'DELEB1', '#2E6A8A', ('La ciudad sumergida de Duio', 'La ville engloutie de Duio', 'The sunken city of Duio'),
  ('Près de Fisterra, une ville orgueilleuse refuse d’accueillir les voyageurs… et disparaît sous la mer. On dit qu’on entend encore ses cloches.', 'Near Fisterra, a proud city refuses to welcome travellers… and disappears beneath the sea. They say you can still hear its bells.'), [
  CH('ciudad-de-duio-1', ('Una ciudad orgullosa', 'Une ville orgueilleuse', 'A proud city'), [
    [S('Cuenta la leyenda que, junto a la playa de Langosteira, había una ciudad rica y poderosa llamada Duio.', 'La légende raconte qu’à côté de la plage de Langosteira se trouvait une ville riche et puissante appelée Duio.', 'Legend has it that, next to Langosteira beach, there was a rich and powerful city called Duio.'),
     S('Sus habitantes vivían en casas de piedra, comían en platos de oro y no querían que nadie de fuera entrara en la ciudad.', 'Ses habitants vivaient dans des maisons de pierre, mangeaient dans des assiettes en or et ne voulaient pas que des étrangers entrent dans la ville.', 'Its inhabitants lived in stone houses, ate from gold plates and did not want any outsiders to enter the city.')],
    [S('Un día llegaron dos viajeros cansados que pidieron agua y un lugar donde dormir.', 'Un jour arrivèrent deux voyageurs fatigués qui demandèrent de l’eau et un endroit où dormir.', 'One day two tired travellers arrived and asked for water and a place to sleep.'),
     S('«Aquí no hay sitio para mendigos», les dijeron. Y les cerraron todas las puertas.', '« Ici, il n’y a pas de place pour les mendiants », leur dit-on. Et on leur ferma toutes les portes.', '“There’s no room here for beggars,” they were told. And every door was shut in their faces.'),
     S('Solo una mujer pobre, que vivía fuera de las murallas, les ofreció pan y su cama.', 'Seule une femme pauvre, qui vivait hors des remparts, leur offrit du pain et son lit.', 'Only a poor woman, who lived outside the walls, offered them bread and her bed.')],
  ], [
    W('poderoso', '/poðeˈɾoso/', 'puissant', 'powerful'),
    W('el habitante', '/el aβiˈtante/', 'l’habitant', 'the inhabitant'),
    W('la piedra', '/la ˈpjeðɾa/', 'la pierre', 'stone'),
    W('el viajero', '/el bjaˈxeɾo/', 'le voyageur', 'the traveller'),
    W('el mendigo', '/el menˈdiɣo/', 'le mendiant', 'the beggar'),
    W('ofrecer', '/ofɾeˈθeɾ/', 'offrir, proposer', 'to offer'),
  ], [
    Q(('Que refusaient les habitants de Duio ?', 'What did the people of Duio refuse?'), [('Que des étrangers entrent dans la ville', 'To let outsiders into the city'), ('De manger dans de l’or', 'To eat from gold plates'), ('D’aller à la plage', 'To go to the beach')], 0),
    Q(('Qui aida les voyageurs ?', 'Who helped the travellers?'), [('Une femme pauvre hors des remparts', 'A poor woman outside the walls'), ('Le maire de la ville', 'The mayor of the city'), ('Personne', 'Nobody')], 0),
  ]),
  CH('ciudad-de-duio-2', ('Las campanas bajo el mar', 'Les cloches sous la mer', 'The bells beneath the sea'), [
    [S('Por la mañana, los viajeros le dijeron a la mujer: «Vete al monte y no mires atrás, pase lo que pase».', 'Le matin, les voyageurs dirent à la femme : « Va sur la montagne et ne te retourne pas, quoi qu’il arrive. »', 'In the morning, the travellers said to the woman: “Go up the mountain and don’t look back, whatever happens.”'),
     S('Mientras ella subía, se levantó una tormenta terrible y el mar cubrió la ciudad entera.', 'Pendant qu’elle montait, une terrible tempête se leva et la mer recouvrit la ville entière.', 'As she was climbing, a terrible storm rose and the sea covered the whole city.'),
     S('La mujer obedeció y se salvó; de Duio no quedó nada.', 'La femme obéit et fut sauvée ; de Duio, il ne resta rien.', 'The woman obeyed and was saved; nothing was left of Duio.')],
    [S('Hoy los pescadores de Fisterra dicen que, en las noches tranquilas, se oyen las campanas de la ciudad bajo el agua.', 'Aujourd’hui, les pêcheurs de Fisterra disent que, par les nuits calmes, on entend les cloches de la ville sous l’eau.', 'Today the fishermen of Fisterra say that, on calm nights, you can hear the city’s bells beneath the water.'),
     S('Y los peregrinos que llegan al fin del mundo recuerdan la lección: siempre hay que abrir la puerta al viajero.', 'Et les pèlerins qui arrivent au bout du monde se souviennent de la leçon : il faut toujours ouvrir sa porte au voyageur.', 'And the pilgrims who reach the end of the world remember the lesson: you should always open your door to the traveller.')],
  ], [
    W('mirar atrás', '/miˈɾaɾ aˈtɾas/', 'regarder en arrière', 'to look back'),
    W('pase lo que pase', '/ˈpase lo ke ˈpase/', 'quoi qu’il arrive', 'whatever happens'),
    W('cubrir', '/kuˈβɾiɾ/', 'couvrir', 'to cover'),
    W('salvarse', '/salˈβaɾse/', 'se sauver, être sauvé', 'to be saved'),
    W('la campana', '/la kamˈpana/', 'la cloche', 'the bell'),
    W('el pescador', '/el peskaˈðoɾ/', 'le pêcheur', 'the fisherman'),
  ], [
    Q(('Que conseillèrent les voyageurs à la femme ?', 'What did the travellers advise the woman?'), [('De monter sans se retourner', 'To climb without looking back'), ('De rester chez elle', 'To stay at home'), ('De prévenir la ville', 'To warn the city')], 0),
    Q(('Qu’entendent les pêcheurs par les nuits calmes ?', 'What do fishermen hear on calm nights?'), [('Les cloches de la ville engloutie', 'The bells of the sunken city'), ('Des chants de pèlerins', 'Pilgrims singing'), ('La tempête', 'The storm')], 0),
  ]),
])

ES_STORIES = [POLLITO, RATITA, MOLINOS, JUAN, BLANCA, GALLO, DUIO]

data = json.load(open(P, encoding='utf-8'))
data['stories'] = [s for s in data['stories'] if not s['level'].startswith('DELE')] + ES_STORIES
data.setdefault('notices', {})['es'] = {'fr': 'Contes populaires d’Espagne et épisodes de Don Quichotte (domaine public), réécrits en espagnol simple pour Koto Quest. La prononciation des mots est notée en alphabet phonétique (espagnol d’Espagne).', 'en': 'Spanish folk tales and episodes from Don Quixote (public domain), retold in simple Spanish for Koto Quest. Word pronunciation is shown in phonetic script (Spanish from Spain).'}
slugs = [c['slug'] for s in data['stories'] for c in s['chapters']]
assert len(slugs) == len(set(slugs)), 'slug de chapitre en double'
for s in ES_STORIES:
    for c in s['chapters']:
        assert len(c['words']) >= 6, c['slug']
        for q in c['questions']:
            assert 0 <= q['answer'] < len(q['choices'])
json.dump(data, open(P, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('Contes espagnols :', len(ES_STORIES), 'contes,', sum(len(s['chapters']) for s in ES_STORIES), 'chapitres')
