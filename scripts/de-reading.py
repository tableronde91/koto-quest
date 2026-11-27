# Lecture en allemand : contes des frères Grimm (domaine public), réécrits en allemand simple.
# Ajoute (ou remplace) les contes allemands dans content/reading/stories.json, sans toucher aux autres langues.
# Usage : python3 scripts/de-reading.py
import json, os
ROOT = os.path.join(os.path.dirname(__file__), '..')
P = os.path.join(ROOT, 'content/reading/stories.json')

def S(de, fr, en):
    """Phrase : le texte à lire et à prononcer est le même."""
    return {'jp': de, 'fr': fr, 'en': en, 'kana': de}

def W(word, ipa, fr, en):
    return {'jp': word, 'reading': ipa, 'fr': fr, 'en': en}

def Q(q, choices, answer):
    return {'q': {'fr': q[0], 'en': q[1]}, 'choices': [{'fr': f, 'en': e} for f, e in choices], 'answer': answer}

def CH(slug, title, paragraphs, words, questions):
    de, fr, en = title
    return {'slug': slug, 'title': {'jp': de, 'fr': fr, 'en': en}, 'paragraphs': paragraphs, 'words': words, 'questions': questions}

def STORY(slug, glyph, level, color, title, summary, chapters):
    de, fr, en = title
    return {'slug': slug, 'glyph': glyph, 'level': level, 'color': color, 'title': {'jp': de, 'fr': fr, 'en': en}, 'summary': {'fr': summary[0], 'en': summary[1]}, 'chapters': chapters}

# ═════════════════════════ Die Bremer Stadtmusikanten ═════════════════════════
BREMER = STORY('bremer-stadtmusikanten', 'B', 'GOETHEA1', '#8A6A3A', ('Die Bremer Stadtmusikanten', 'Les Musiciens de Brême', 'The Bremen Town Musicians'),
  ('Un âne, un chien, un chat et un coq, trop vieux pour travailler, partent à Brême pour devenir musiciens.', 'A donkey, a dog, a cat and a rooster, too old to work, set off for Bremen to become musicians.'), [
  CH('bremer-stadtmusikanten-1', ('Vier alte Tiere', 'Quatre vieux animaux', 'Four old animals'), [
    [S('Ein Esel ist alt und kann nicht mehr arbeiten.', 'Un âne est vieux et ne peut plus travailler.', 'A donkey is old and can no longer work.'),
     S('Er sagt: „Ich gehe nach Bremen. Dort mache ich Musik.“', 'Il dit : « Je vais à Brême. Là-bas, je ferai de la musique. »', 'He says: “I’m going to Bremen. There I will make music.”'),
     S('Auf dem Weg trifft er einen Hund. Der Hund ist müde und traurig.', 'En chemin, il rencontre un chien. Le chien est fatigué et triste.', 'On the way he meets a dog. The dog is tired and sad.')],
    [S('„Komm mit nach Bremen!“, sagt der Esel.', '« Viens avec moi à Brême ! » dit l’âne.', '“Come with me to Bremen!” says the donkey.'),
     S('Dann treffen sie eine Katze und einen Hahn.', 'Ensuite, ils rencontrent un chat et un coq.', 'Then they meet a cat and a rooster.'),
     S('Jetzt sind sie vier Freunde, und sie gehen zusammen weiter.', 'Maintenant, ils sont quatre amis, et ils continuent ensemble.', 'Now they are four friends, and they walk on together.')],
  ], [
    W('der Esel', '/deːɐ̯ ˈeːzl̩/', 'l’âne', 'the donkey'),
    W('der Hund', '/deːɐ̯ hʊnt/', 'le chien', 'the dog'),
    W('die Katze', '/diː ˈkatsə/', 'le chat', 'the cat'),
    W('der Hahn', '/deːɐ̯ haːn/', 'le coq', 'the rooster'),
    W('müde', '/ˈmyːdə/', 'fatigué', 'tired'),
    W('zusammen', '/tsuˈzamən/', 'ensemble', 'together'),
  ], [
    Q(('Pourquoi l’âne part-il ?', 'Why does the donkey leave?'), [('Il est vieux et ne peut plus travailler', 'He is old and can no longer work'), ('Il veut voir la mer', 'He wants to see the sea'), ('Il cherche son maître', 'He is looking for his master')], 0),
    Q(('Combien d’amis sont-ils à la fin du chapitre ?', 'How many friends are there at the end of the chapter?'), [('Quatre', 'Four'), ('Deux', 'Two'), ('Sept', 'Seven')], 0),
  ]),
  CH('bremer-stadtmusikanten-2', ('Das Haus im Wald', 'La maison dans la forêt', 'The house in the forest'), [
    [S('Am Abend kommen die Tiere in einen Wald. Sie haben Hunger.', 'Le soir, les animaux arrivent dans une forêt. Ils ont faim.', 'In the evening the animals come to a forest. They are hungry.'),
     S('Sie sehen ein Haus mit Licht. Im Haus sitzen Räuber und essen.', 'Ils voient une maison éclairée. Dans la maison, des brigands sont à table et mangent.', 'They see a house with a light on. Inside, robbers are sitting and eating.'),
     S('Der Hund steht auf dem Esel, die Katze auf dem Hund und der Hahn auf der Katze.', 'Le chien monte sur l’âne, le chat sur le chien et le coq sur le chat.', 'The dog stands on the donkey, the cat on the dog and the rooster on the cat.')],
    [S('Dann machen sie Musik: Der Esel schreit, der Hund bellt, die Katze miaut und der Hahn kräht.', 'Puis ils font de la musique : l’âne brait, le chien aboie, le chat miaule et le coq chante.', 'Then they make music: the donkey brays, the dog barks, the cat miaows and the rooster crows.'),
     S('Die Räuber haben Angst und laufen schnell weg.', 'Les brigands ont peur et s’enfuient vite.', 'The robbers are frightened and quickly run away.'),
     S('Die vier Freunde essen gut und bleiben für immer im Haus.', 'Les quatre amis mangent bien et restent pour toujours dans la maison.', 'The four friends eat well and stay in the house for ever.')],
  ], [
    W('der Wald', '/deːɐ̯ valt/', 'la forêt', 'the forest'),
    W('das Licht', '/das lɪçt/', 'la lumière', 'the light'),
    W('der Räuber', '/deːɐ̯ ˈʁɔʏbɐ/', 'le brigand', 'the robber'),
    W('bellen', '/ˈbɛlən/', 'aboyer', 'to bark'),
    W('die Angst', '/diː aŋst/', 'la peur', 'the fear'),
    W('bleiben', '/ˈblaɪbn̩/', 'rester', 'to stay'),
  ], [
    Q(('Qui se trouve dans la maison ?', 'Who is in the house?'), [('Des brigands', 'Robbers'), ('Une sorcière', 'A witch'), ('Sept nains', 'Seven dwarfs')], 0),
    Q(('Que font les brigands en entendant la « musique » ?', 'What do the robbers do when they hear the “music”?'), [('Ils s’enfuient', 'They run away'), ('Ils dansent', 'They dance'), ('Ils invitent les animaux', 'They invite the animals in')], 0),
  ]),
])

# ═════════════════════════ Der süße Brei ═════════════════════════
BREI = STORY('suesser-brei', 'S', 'GOETHEA1', '#C8923A', ('Der süße Brei', 'La bouillie sucrée', 'Sweet Porridge'),
  ('Une petite fille pauvre reçoit une marmite magique qui cuit de la bouillie… mais il faut connaître les mots pour l’arrêter.', 'A poor little girl is given a magic pot that cooks porridge… but you need to know the words to stop it.'), [
  CH('suesser-brei-1', ('Der kleine Topf', 'La petite marmite', 'The little pot'), [
    [S('Ein Mädchen wohnt mit seiner Mutter in einem kleinen Haus.', 'Une fillette habite avec sa mère dans une petite maison.', 'A girl lives with her mother in a small house.'),
     S('Sie sind arm und haben nichts zu essen.', 'Elles sont pauvres et n’ont rien à manger.', 'They are poor and have nothing to eat.'),
     S('Das Mädchen geht in den Wald. Dort trifft es eine alte Frau.', 'La fillette va dans la forêt. Là, elle rencontre une vieille femme.', 'The girl goes into the forest. There she meets an old woman.')],
    [S('Die Frau gibt dem Mädchen einen kleinen Topf.', 'La femme donne à la fillette une petite marmite.', 'The woman gives the girl a little pot.'),
     S('Das Mädchen sagt: „Töpfchen, koche!“ Und der Topf kocht süßen Brei.', 'La fillette dit : « Petite marmite, cuis ! » Et la marmite cuit de la bouillie sucrée.', 'The girl says: “Little pot, cook!” And the pot cooks sweet porridge.'),
     S('Es sagt: „Töpfchen, steh!“ Und der Topf kocht nicht mehr.', 'Elle dit : « Petite marmite, arrête ! » Et la marmite ne cuit plus.', 'She says: “Little pot, stop!” And the pot stops cooking.')],
  ], [
    W('arm', '/aʁm/', 'pauvre', 'poor'),
    W('der Topf', '/deːɐ̯ tɔpf/', 'la marmite, la casserole', 'the pot'),
    W('kochen', '/ˈkɔxn̩/', 'cuire, cuisiner', 'to cook'),
    W('der Brei', '/deːɐ̯ bʁaɪ/', 'la bouillie', 'the porridge'),
    W('süß', '/zyːs/', 'sucré', 'sweet'),
    W('nichts', '/nɪçts/', 'rien', 'nothing'),
  ], [
    Q(('Que donne la vieille femme à la fillette ?', 'What does the old woman give the girl?'), [('Une petite marmite', 'A little pot'), ('Un gâteau', 'A cake'), ('Une pièce d’or', 'A gold coin')], 0),
    Q(('Que faut-il dire pour arrêter la marmite ?', 'What must you say to stop the pot?'), [('« Töpfchen, steh! »', '“Töpfchen, steh!”'), ('« Töpfchen, koche! »', '“Töpfchen, koche!”'), ('« Guten Appetit! »', '“Guten Appetit!”')], 0),
  ]),
  CH('suesser-brei-2', ('Brei in der ganzen Stadt', 'De la bouillie dans toute la ville', 'Porridge all over town'), [
    [S('Eines Tages ist das Mädchen nicht zu Hause.', 'Un jour, la fillette n’est pas à la maison.', 'One day the girl is not at home.'),
     S('Die Mutter hat Hunger und sagt: „Töpfchen, koche!“', 'La mère a faim et dit : « Petite marmite, cuis ! »', 'The mother is hungry and says: “Little pot, cook!”'),
     S('Sie isst und ist satt. Aber sie kennt das zweite Wort nicht!', 'Elle mange et n’a plus faim. Mais elle ne connaît pas le deuxième mot !', 'She eats and is full. But she doesn’t know the second word!')],
    [S('Der Topf kocht und kocht. Der Brei ist in der Küche, im Haus und dann auf der Straße.', 'La marmite cuit et cuit encore. La bouillie est dans la cuisine, dans la maison, puis dans la rue.', 'The pot cooks and cooks. The porridge is in the kitchen, in the house and then in the street.'),
     S('Am Abend kommt das Mädchen und sagt schnell: „Töpfchen, steh!“', 'Le soir, la fillette revient et dit vite : « Petite marmite, arrête ! »', 'In the evening the girl comes back and quickly says: “Little pot, stop!”'),
     S('Wer jetzt in die Stadt will, muss zuerst viel Brei essen.', 'Celui qui veut maintenant entrer dans la ville doit d’abord manger beaucoup de bouillie.', 'Anyone who now wants to enter the town must first eat a lot of porridge.')],
  ], [
    W('zu Hause', '/tsuː ˈhaʊzə/', 'à la maison', 'at home'),
    W('satt', '/zat/', 'rassasié', 'full (after eating)'),
    W('kennen', '/ˈkɛnən/', 'connaître', 'to know'),
    W('das Wort', '/das vɔʁt/', 'le mot', 'the word'),
    W('die Küche', '/diː ˈkʏçə/', 'la cuisine', 'the kitchen'),
    W('zuerst', '/tsuˈeːɐ̯st/', 'd’abord', 'first'),
  ], [
    Q(('Pourquoi la marmite ne s’arrête-t-elle pas ?', 'Why doesn’t the pot stop?'), [('La mère ne connaît pas le mot pour l’arrêter', 'The mother doesn’t know the word to stop it'), ('La marmite est cassée', 'The pot is broken'), ('La fillette l’a voulu', 'The girl wanted it to')], 0),
    Q(('Qui arrête enfin la marmite ?', 'Who finally stops the pot?'), [('La fillette', 'The girl'), ('La vieille femme', 'The old woman'), ('Le maire', 'The mayor')], 0),
  ]),
])

# ═════════════════════════ Die Sterntaler ═════════════════════════
STERN = STORY('sterntaler', 'Z', 'GOETHEA1', '#3A5A8A', ('Die Sterntaler', 'Les Écus tombés du ciel', 'The Star Talers'),
  ('Une orpheline donne tout ce qu’elle possède à plus pauvre qu’elle… et les étoiles la récompensent.', 'An orphan girl gives away everything she owns to those poorer than her… and the stars reward her.'), [
  CH('sterntaler-1', ('Ein Stück Brot', 'Un morceau de pain', 'A piece of bread'), [
    [S('Ein kleines Mädchen hat keinen Vater und keine Mutter mehr.', 'Une petite fille n’a plus ni père ni mère.', 'A little girl no longer has a father or a mother.'),
     S('Es hat kein Haus und kein Bett. Es hat nur seine Kleidung und ein Stück Brot.', 'Elle n’a ni maison ni lit. Elle n’a que ses vêtements et un morceau de pain.', 'She has no house and no bed. She has only her clothes and a piece of bread.'),
     S('Aber das Mädchen ist gut und geht allein in die Welt.', 'Mais la fillette est bonne et s’en va seule dans le monde.', 'But the girl is good and goes out alone into the world.')],
    [S('Ein armer Mann sagt: „Ich habe Hunger. Gib mir bitte etwas zu essen!“', 'Un pauvre homme dit : « J’ai faim. Donne-moi quelque chose à manger, s’il te plaît ! »', 'A poor man says: “I’m hungry. Please give me something to eat!”'),
     S('Das Mädchen gibt ihm das ganze Brot.', 'La fillette lui donne tout le pain.', 'The girl gives him all the bread.'),
     S('Dann kommt ein Kind: „Mein Kopf ist so kalt.“ Das Mädchen gibt ihm seine Mütze.', 'Puis vient un enfant : « J’ai si froid à la tête. » La fillette lui donne son bonnet.', 'Then a child comes: “My head is so cold.” The girl gives him her cap.')],
  ], [
    W('das Stück', '/das ʃtʏk/', 'le morceau', 'the piece'),
    W('das Bett', '/das bɛt/', 'le lit', 'the bed'),
    W('allein', '/aˈlaɪn/', 'seul', 'alone'),
    W('die Welt', '/diː vɛlt/', 'le monde', 'the world'),
    W('geben', '/ˈɡeːbn̩/', 'donner', 'to give'),
    W('die Mütze', '/diː ˈmʏtsə/', 'le bonnet', 'the cap, the woolly hat'),
  ], [
    Q(('Que possède la fillette au début ?', 'What does the girl own at the beginning?'), [('Ses vêtements et un morceau de pain', 'Her clothes and a piece of bread'), ('Une maison et un lit', 'A house and a bed'), ('Une marmite magique', 'A magic pot')], 0),
    Q(('Que donne-t-elle à l’homme pauvre ?', 'What does she give the poor man?'), [('Tout son pain', 'All her bread'), ('Son bonnet', 'Her cap'), ('De l’argent', 'Money')], 0),
  ]),
  CH('sterntaler-2', ('Sterne im Wald', 'Des étoiles dans la forêt', 'Stars in the forest'), [
    [S('Am Abend ist das Mädchen im Wald. Es ist dunkel und sehr kalt.', 'Le soir, la fillette est dans la forêt. Il fait sombre et très froid.', 'In the evening the girl is in the forest. It is dark and very cold.'),
     S('Noch ein Kind kommt und möchte ein Hemd. Das Mädchen gibt auch sein Hemd.', 'Un autre enfant arrive et voudrait une chemise. La fillette donne aussi sa chemise.', 'Another child comes and would like a shirt. The girl gives her shirt too.'),
     S('Jetzt hat es nichts mehr.', 'Maintenant, elle n’a plus rien.', 'Now she has nothing left.')],
    [S('Da fallen die Sterne vom Himmel, und sie sind Geld aus Silber!', 'Alors les étoiles tombent du ciel, et ce sont des pièces d’argent !', 'Then the stars fall from the sky, and they are silver coins!'),
     S('Das Mädchen trägt plötzlich ein neues, schönes Hemd.', 'La fillette porte soudain une belle chemise neuve.', 'Suddenly the girl is wearing a beautiful new shirt.'),
     S('Es sammelt die Taler und ist reich für sein ganzes Leben.', 'Elle ramasse les écus et elle est riche pour toute sa vie.', 'She gathers the talers and is rich for the rest of her life.')],
  ], [
    W('dunkel', '/ˈdʊŋkl̩/', 'sombre', 'dark'),
    W('der Stern', '/deːɐ̯ ʃtɛʁn/', 'l’étoile', 'the star'),
    W('der Himmel', '/deːɐ̯ ˈhɪml̩/', 'le ciel', 'the sky'),
    W('fallen', '/ˈfalən/', 'tomber', 'to fall'),
    W('reich', '/ʁaɪç/', 'riche', 'rich'),
    W('das Leben', '/das ˈleːbn̩/', 'la vie', 'the life'),
  ], [
    Q(('Que donne encore la fillette dans la forêt ?', 'What else does the girl give away in the forest?'), [('Sa chemise', 'Her shirt'), ('Ses chaussures', 'Her shoes'), ('Son pain', 'Her bread')], 0),
    Q(('Que deviennent les étoiles ?', 'What do the stars turn into?'), [('Des pièces d’argent', 'Silver coins'), ('De la neige', 'Snow'), ('Des gâteaux', 'Cakes')], 0),
  ]),
])

# ═════════════════════════ Der Froschkönig (A2) ═════════════════════════
FROSCH = STORY('froschkoenig', 'F', 'GOETHEA2', '#3E7A4A', ('Der Froschkönig', 'Le Roi Grenouille', 'The Frog King'),
  ('Une princesse perd sa balle d’or dans un puits ; une grenouille la lui rend… contre une promesse qu’elle voudrait bien oublier.', 'A princess loses her golden ball in a well; a frog gives it back… in return for a promise she would rather forget.'), [
  CH('froschkoenig-1', ('Die goldene Kugel', 'La balle d’or', 'The golden ball'), [
    [S('Eine junge Prinzessin hat jeden Tag am Brunnen mit ihrer goldenen Kugel gespielt.', 'Une jeune princesse jouait chaque jour près du puits avec sa balle d’or.', 'A young princess played by the well every day with her golden ball.'),
     S('Eines Tages ist die Kugel ins Wasser gefallen.', 'Un jour, la balle est tombée dans l’eau.', 'One day the ball fell into the water.'),
     S('Die Prinzessin hat geweint, weil der Brunnen so tief war.', 'La princesse a pleuré, parce que le puits était si profond.', 'The princess cried because the well was so deep.')],
    [S('Da hat ein Frosch gefragt: „Was gibst du mir, wenn ich dir die Kugel hole?“', 'Alors une grenouille a demandé : « Que me donnes-tu si je vais te chercher la balle ? »', 'Then a frog asked: “What will you give me if I fetch the ball for you?”'),
     S('„Ich möchte mit dir essen und in deinem Bett schlafen.“', '« Je voudrais manger avec toi et dormir dans ton lit. »', '“I would like to eat with you and sleep in your bed.”'),
     S('Die Prinzessin hat alles versprochen, aber sie hat gedacht: „Ein Frosch kann doch nicht mitkommen!“', 'La princesse a tout promis, mais elle a pensé : « Une grenouille ne peut tout de même pas venir avec moi ! »', 'The princess promised everything, but she thought: “A frog can’t come along, surely!”')],
  ], [
    W('der Brunnen', '/deːɐ̯ ˈbʁʊnən/', 'le puits', 'the well'),
    W('die Kugel', '/diː ˈkuːɡl̩/', 'la balle, la boule', 'the ball'),
    W('weinen', '/ˈvaɪnən/', 'pleurer', 'to cry'),
    W('tief', '/tiːf/', 'profond', 'deep'),
    W('der Frosch', '/deːɐ̯ fʁɔʃ/', 'la grenouille', 'the frog'),
    W('versprechen', '/fɛɐ̯ˈʃpʁɛçn̩/', 'promettre', 'to promise'),
  ], [
    Q(('Pourquoi la princesse pleure-t-elle ?', 'Why does the princess cry?'), [('Sa balle est tombée dans un puits profond', 'Her ball has fallen into a deep well'), ('Elle a perdu son chemin', 'She has lost her way'), ('La grenouille l’a mordue', 'The frog bit her')], 0),
    Q(('Que demande la grenouille en échange ?', 'What does the frog ask for in return?'), [('Manger avec elle et dormir dans son lit', 'To eat with her and sleep in her bed'), ('De l’or et des bijoux', 'Gold and jewels'), ('Un baiser tout de suite', 'A kiss straight away')], 0),
  ]),
  CH('froschkoenig-2', ('Der Gast am Tisch', 'L’invité à table', 'The guest at the table'), [
    [S('Am nächsten Tag hat es an der Tür geklopft: Der Frosch war da.', 'Le lendemain, on a frappé à la porte : la grenouille était là.', 'The next day there was a knock at the door: the frog was there.'),
     S('Der König hat gesagt: „Was du versprochen hast, musst du auch halten.“', 'Le roi a dit : « Ce que tu as promis, tu dois le tenir. »', 'The king said: “What you have promised, you must keep.”'),
     S('Also hat der Frosch vom goldenen Teller gegessen, und die Prinzessin hat sich sehr geärgert.', 'La grenouille a donc mangé dans l’assiette d’or, et la princesse s’est beaucoup fâchée.', 'So the frog ate from the golden plate, and the princess was very annoyed.')],
    [S('Im Schlafzimmer hat sie den Frosch wütend an die Wand geworfen.', 'Dans la chambre, furieuse, elle a jeté la grenouille contre le mur.', 'In the bedroom she angrily threw the frog against the wall.'),
     S('Aber da war er kein Frosch mehr, sondern ein junger König mit freundlichen Augen.', 'Mais ce n’était plus une grenouille : c’était un jeune roi au regard bienveillant.', 'But he was no longer a frog: he was a young king with friendly eyes.'),
     S('Eine Hexe hatte ihn verzaubert. Am nächsten Morgen sind die beiden zusammen in sein Land gefahren.', 'Une sorcière l’avait ensorcelé. Le lendemain matin, ils sont partis ensemble pour son pays.', 'A witch had put a spell on him. The next morning the two of them travelled to his country together.')],
  ], [
    W('klopfen', '/ˈklɔpfn̩/', 'frapper (à la porte)', 'to knock'),
    W('halten', '/ˈhaltn̩/', 'tenir (une promesse)', 'to keep (a promise)'),
    W('der Teller', '/deːɐ̯ ˈtɛlɐ/', 'l’assiette', 'the plate'),
    W('wütend', '/ˈvyːtn̩t/', 'furieux', 'angry, furious'),
    W('werfen', '/ˈvɛʁfn̩/', 'jeter, lancer', 'to throw'),
    W('verzaubern', '/fɛɐ̯ˈtsaʊbɐn/', 'ensorceler', 'to put a spell on'),
  ], [
    Q(('Que dit le roi à sa fille ?', 'What does the king tell his daughter?'), [('Qu’elle doit tenir sa promesse', 'That she must keep her promise'), ('Qu’elle doit chasser la grenouille', 'That she must send the frog away'), ('Qu’elle doit retourner au puits', 'That she must go back to the well')], 0),
    Q(('Qui était vraiment la grenouille ?', 'Who was the frog really?'), [('Un jeune roi ensorcelé', 'A young king under a spell'), ('Une sorcière', 'A witch'), ('Le frère de la princesse', 'The princess’s brother')], 0),
  ]),
])

# ═════════════════════════ Hans im Glück (A2) ═════════════════════════
HANS = STORY('hans-im-glueck', 'U', 'GOETHEA2', '#B8902A', ('Hans im Glück', 'Jean le Chanceux', 'Lucky Hans'),
  ('Après sept ans de travail, Jean reçoit un lingot d’or… et l’échange, de troc en troc, jusqu’à n’avoir plus rien. Est-il fou ou heureux ?', 'After seven years’ work, Hans is given a lump of gold… and swaps it, deal after deal, until he has nothing left. Is he a fool or a happy man?'), [
  CH('hans-im-glueck-1', ('Gold, Pferd und Kuh', 'L’or, le cheval et la vache', 'Gold, horse and cow'), [
    [S('Hans hat sieben Jahre bei seinem Herrn gearbeitet. Jetzt wollte er nach Hause zu seiner Mutter.', 'Jean a travaillé sept ans chez son maître. Maintenant, il voulait rentrer chez sa mère.', 'Hans worked for his master for seven years. Now he wanted to go home to his mother.'),
     S('Der Herr hat ihm ein Stück Gold gegeben, so groß wie sein Kopf.', 'Le maître lui a donné un morceau d’or gros comme sa tête.', 'The master gave him a lump of gold as big as his head.'),
     S('Aber das Gold war schwer, und der Weg war lang.', 'Mais l’or était lourd, et le chemin était long.', 'But the gold was heavy, and the way was long.')],
    [S('Da ist ein Reiter gekommen. „Reiten ist besser als laufen“, hat Hans gedacht, und er hat das Gold gegen das Pferd getauscht.', 'Alors un cavalier est arrivé. « Aller à cheval vaut mieux que marcher », a pensé Jean, et il a échangé l’or contre le cheval.', 'Then a rider came along. “Riding is better than walking,” thought Hans, and he swapped the gold for the horse.'),
     S('Das Pferd ist zu schnell gelaufen, und Hans ist heruntergefallen.', 'Le cheval a couru trop vite, et Jean est tombé.', 'The horse ran too fast, and Hans fell off.'),
     S('Also hat er das Pferd gegen eine Kuh getauscht, weil eine Kuh ruhiger ist und Milch gibt.', 'Il a donc échangé le cheval contre une vache, parce qu’une vache est plus calme et donne du lait.', 'So he swapped the horse for a cow, because a cow is calmer and gives milk.')],
  ], [
    W('der Herr', '/deːɐ̯ hɛʁ/', 'le maître, le patron', 'the master'),
    W('schwer', '/ʃveːɐ̯/', 'lourd', 'heavy'),
    W('der Reiter', '/deːɐ̯ ˈʁaɪtɐ/', 'le cavalier', 'the rider'),
    W('das Pferd', '/das pfeːɐ̯t/', 'le cheval', 'the horse'),
    W('tauschen', '/ˈtaʊʃn̩/', 'échanger', 'to swap'),
    W('die Kuh', '/diː kuː/', 'la vache', 'the cow'),
  ], [
    Q(('Pourquoi Jean échange-t-il son or ?', 'Why does Hans swap his gold?'), [('Il est lourd et le chemin est long', 'It is heavy and the way is long'), ('Il veut acheter une maison', 'He wants to buy a house'), ('Son maître le lui demande', 'His master asks him to')], 0),
    Q(('Pourquoi préfère-t-il ensuite une vache au cheval ?', 'Why does he then prefer a cow to the horse?'), [('Elle est plus calme et donne du lait', 'It is calmer and gives milk'), ('Elle court plus vite', 'It runs faster'), ('Elle vaut plus cher', 'It is worth more')], 0),
  ]),
  CH('hans-im-glueck-2', ('Frei wie ein Vogel', 'Libre comme un oiseau', 'Free as a bird'), [
    [S('Die Kuh hat keine Milch gegeben. Hans hat sie gegen ein Schwein getauscht und das Schwein gegen eine Gans.', 'La vache n’a pas donné de lait. Jean l’a échangée contre un cochon, et le cochon contre une oie.', 'The cow gave no milk. Hans swapped it for a pig, and the pig for a goose.'),
     S('Für die Gans hat er am Ende einen schweren Stein bekommen.', 'Contre l’oie, il a fini par recevoir une lourde pierre.', 'For the goose he ended up with a heavy stone.'),
     S('„Ich habe immer Glück“, hat er gesagt. „Jeder Tausch war besser als der letzte.“', '« J’ai toujours de la chance, a-t-il dit. Chaque échange était meilleur que le précédent. »', '“I am always lucky,” he said. “Every swap was better than the last.”')],
    [S('An einem Brunnen wollte Hans trinken. Da ist der Stein ins Wasser gefallen.', 'Près d’un puits, Jean a voulu boire. Alors la pierre est tombée dans l’eau.', 'At a well Hans wanted to drink. Then the stone fell into the water.'),
     S('Hans hat gelacht: „Jetzt muss ich nichts mehr tragen. Ich bin der glücklichste Mensch der Welt!“', 'Jean a ri : « Maintenant, je n’ai plus rien à porter. Je suis l’homme le plus heureux du monde ! »', 'Hans laughed: “Now I don’t have to carry anything any more. I am the happiest person in the world!”'),
     S('Und er ist frei und leicht zu seiner Mutter nach Hause gelaufen.', 'Et il a couru, libre et léger, jusque chez sa mère.', 'And he ran home to his mother, free and light.')],
  ], [
    W('das Schwein', '/das ʃvaɪn/', 'le cochon', 'the pig'),
    W('die Gans', '/diː ɡans/', 'l’oie', 'the goose'),
    W('der Stein', '/deːɐ̯ ʃtaɪn/', 'la pierre', 'the stone'),
    W('das Glück', '/das ɡlʏk/', 'la chance ; le bonheur', 'luck; happiness'),
    W('frei', '/fʁaɪ/', 'libre', 'free'),
    W('leicht', '/laɪçt/', 'léger', 'light'),
  ], [
    Q(('Que reçoit Jean en échange de l’oie ?', 'What does Hans get in exchange for the goose?'), [('Une lourde pierre', 'A heavy stone'), ('Un cochon', 'A pig'), ('Un sac d’or', 'A bag of gold')], 0),
    Q(('Pourquoi Jean rit-il à la fin ?', 'Why does Hans laugh at the end?'), [('Il n’a plus rien à porter', 'He has nothing left to carry'), ('Il a retrouvé son or', 'He has found his gold again'), ('Sa mère lui offre un cheval', 'His mother gives him a horse')], 0),
  ]),
])

# ═════════════════════════ Vom Fischer und seiner Frau (B1) ═════════════════════════
FISCHER = STORY('fischer-und-frau', 'V', 'GOETHEB1', '#2E6A7A', ('Vom Fischer und seiner Frau', 'Le Pêcheur et sa femme', 'The Fisherman and His Wife'),
  ('Un pêcheur relâche un poisson enchanté ; sa femme, elle, veut une maison, puis un château, puis davantage encore.', 'A fisherman lets an enchanted fish go; his wife, however, wants a house, then a castle, then even more.'), [
  CH('fischer-und-frau-1', ('Der verzauberte Fisch', 'Le poisson enchanté', 'The enchanted fish'), [
    [S('Es war einmal ein Fischer, der mit seiner Frau Ilsebill in einer alten Hütte am Meer wohnte.', 'Il était une fois un pêcheur qui habitait avec sa femme Ilsebill dans une vieille cabane au bord de la mer.', 'Once upon a time there was a fisherman who lived with his wife Ilsebill in an old hut by the sea.'),
     S('Eines Tages fing er einen großen Fisch, der plötzlich zu sprechen begann.', 'Un jour, il attrapa un gros poisson qui se mit soudain à parler.', 'One day he caught a big fish that suddenly began to speak.'),
     S('„Lass mich leben“, bat der Fisch, „ich bin ein verzauberter Prinz.“ Da ließ der Fischer ihn wieder ins Wasser.', '« Laisse-moi la vie, pria le poisson, je suis un prince ensorcelé. » Alors le pêcheur le remit à l’eau.', '“Let me live,” begged the fish, “I am an enchanted prince.” So the fisherman put him back in the water.')],
    [S('Als die Frau das hörte, wurde sie böse: „Hättest du dir doch etwas gewünscht! Geh zurück und sag ihm, dass wir ein Haus haben wollen.“', 'Quand la femme entendit cela, elle se fâcha : « Si seulement tu avais fait un vœu ! Retourne lui dire que nous voulons une maison. »', 'When his wife heard this, she grew angry: “If only you had made a wish! Go back and tell him that we want a house.”'),
     S('Der Mann ging nicht gern, aber er rief den Fisch. Das Meer war grün und gelb und gar nicht mehr so klar.', 'L’homme n’y alla pas de bon cœur, mais il appela le poisson. La mer était verte et jaune, et plus du tout aussi claire.', 'The man did not go gladly, but he called the fish. The sea was green and yellow and no longer so clear.'),
     S('„Geh nur nach Hause“, sagte der Fisch, „sie hat es schon.“', '« Rentre donc chez toi, dit le poisson, elle l’a déjà. »', '“Just go home,” said the fish, “she already has it.”')],
  ], [
    W('fangen', '/ˈfaŋən/', 'attraper', 'to catch'),
    W('verzaubert', '/fɛɐ̯ˈtsaʊbɐt/', 'ensorcelé', 'enchanted'),
    W('bitten', '/ˈbɪtn̩/', 'prier, demander', 'to ask, to beg'),
    W('sich etwas wünschen', '/zɪç ˈɛtvas ˈvʏnʃn̩/', 'faire un vœu', 'to wish for something'),
    W('rufen', '/ˈʁuːfn̩/', 'appeler', 'to call'),
    W('klar', '/klaːɐ̯/', 'clair, limpide', 'clear'),
  ], [
    Q(('Pourquoi le pêcheur relâche-t-il le poisson ?', 'Why does the fisherman let the fish go?'), [('Le poisson dit qu’il est un prince ensorcelé', 'The fish says he is an enchanted prince'), ('Le poisson est trop petit', 'The fish is too small'), ('Sa femme le lui demande', 'His wife asks him to')], 0),
    Q(('Que reproche la femme à son mari ?', 'What does the wife reproach her husband for?'), [('De ne pas avoir fait de vœu', 'Not having made a wish'), ('D’être rentré trop tard', 'Coming home too late'), ('D’avoir mangé le poisson', 'Eating the fish')], 0),
  ]),
  CH('fischer-und-frau-2', ('Immer mehr', 'Toujours plus', 'More and more'), [
    [S('Das Haus war schön, doch nach zwei Wochen sagte die Frau: „Es ist zu klein. Ich möchte in einem Schloss wohnen.“', 'La maison était belle, mais au bout de deux semaines la femme dit : « Elle est trop petite. Je voudrais habiter dans un château. »', 'The house was lovely, but after two weeks the wife said: “It is too small. I would like to live in a castle.”'),
     S('Der Fischer ging wieder ans Meer, das jetzt dunkelgrau war, und sie bekam ihr Schloss.', 'Le pêcheur retourna à la mer, qui était maintenant gris foncé, et elle eut son château.', 'The fisherman went back to the sea, which was now dark grey, and she got her castle.'),
     S('Dann wollte sie Königin werden, danach Kaiserin, und jedes Mal wurde das Meer schwärzer und der Wind stärker.', 'Puis elle voulut devenir reine, ensuite impératrice, et à chaque fois la mer devenait plus noire et le vent plus fort.', 'Then she wanted to become queen, after that empress, and each time the sea grew blacker and the wind stronger.')],
    [S('Eines Morgens sah sie die Sonne aufgehen und dachte: „Wenn ich doch die Sonne und den Mond aufgehen lassen könnte!“', 'Un matin, elle vit le soleil se lever et pensa : « Si seulement je pouvais faire lever le soleil et la lune ! »', 'One morning she saw the sun rise and thought: “If only I could make the sun and the moon rise!”'),
     S('Der Fischer zitterte vor Angst, aber er ging. Ein Sturm tobte, und die Wellen waren so hoch wie Kirchtürme.', 'Le pêcheur tremblait de peur, mais il y alla. Une tempête faisait rage, et les vagues étaient aussi hautes que des clochers.', 'The fisherman trembled with fear, but he went. A storm was raging, and the waves were as high as church towers.'),
     S('„Geh nur nach Hause“, sagte der Fisch. „Sie sitzt wieder in der alten Hütte.“ Und dort sitzen die beiden noch heute.', '« Rentre donc chez toi, dit le poisson. Elle est de nouveau dans la vieille cabane. » Et ils y sont encore aujourd’hui.', '“Just go home,” said the fish. “She is sitting in the old hut again.” And there the two of them sit to this day.')],
  ], [
    W('die Kaiserin', '/diː ˈkaɪzəʁɪn/', 'l’impératrice', 'the empress'),
    W('aufgehen', '/ˈaʊfˌɡeːən/', 'se lever (astre)', 'to rise (sun, moon)'),
    W('zittern', '/ˈtsɪtɐn/', 'trembler', 'to tremble'),
    W('toben', '/ˈtoːbn̩/', 'faire rage', 'to rage'),
    W('die Welle', '/diː ˈvɛlə/', 'la vague', 'the wave'),
    W('der Kirchturm', '/deːɐ̯ ˈkɪʁçˌtʊʁm/', 'le clocher', 'the church tower'),
  ], [
    Q(('Comment la mer change-t-elle au fil des vœux ?', 'How does the sea change as the wishes go on?'), [('Elle devient de plus en plus sombre et agitée', 'It becomes darker and rougher'), ('Elle devient de plus en plus calme', 'It becomes calmer and calmer'), ('Elle se retire peu à peu', 'It gradually recedes')], 0),
    Q(('Quel dernier vœu fait tout perdre à la femme ?', 'Which last wish makes the wife lose everything?'), [('Commander au soleil et à la lune', 'To command the sun and the moon'), ('Devenir reine', 'To become queen'), ('Avoir un château en or', 'To have a castle of gold')], 0),
  ]),
])

# ═════════════════════════ Die Heinzelmännchen zu Köln (B1) ═════════════════════════
HEINZEL = STORY('heinzelmaennchen', 'K', 'GOETHEB1', '#8A4A6A', ('Die Heinzelmännchen zu Köln', 'Les Lutins de Cologne', 'The Elves of Cologne'),
  ('Autrefois, à Cologne, de petits lutins faisaient tout le travail pendant la nuit… jusqu’à ce qu’une curieuse veuille les voir.', 'Long ago in Cologne, little elves did all the work during the night… until a curious woman wanted to see them.'), [
  CH('heinzelmaennchen-1', ('Wie bequem es war', 'Comme c’était commode', 'How comfortable it was'), [
    [S('Früher war das Leben in Köln sehr bequem, denn in der Nacht kamen die Heinzelmännchen.', 'Autrefois, la vie à Cologne était très commode, car les lutins venaient pendant la nuit.', 'In the old days life in Cologne was very comfortable, for the elves came during the night.'),
     S('Während die Handwerker schliefen, wurde ihre ganze Arbeit von den kleinen Männern erledigt.', 'Pendant que les artisans dormaient, tout leur travail était fait par les petits hommes.', 'While the craftsmen slept, all their work was done by the little men.'),
     S('Beim Bäcker wurde das Brot gebacken, beim Zimmermann wurden Häuser gebaut, und beim Schneider wurden die Kleider genäht.', 'Chez le boulanger le pain était cuit, chez le charpentier les maisons étaient bâties, et chez le tailleur les habits étaient cousus.', 'At the baker’s the bread was baked, at the carpenter’s houses were built, and at the tailor’s the clothes were sewn.')],
    [S('Am Morgen war alles fertig, obwohl niemand einen Finger bewegt hatte.', 'Le matin, tout était prêt, bien que personne n’eût bougé le petit doigt.', 'In the morning everything was ready, although nobody had lifted a finger.'),
     S('Niemand wusste, wie die Heinzelmännchen aussahen, denn sie wollten nicht gesehen werden.', 'Personne ne savait à quoi ressemblaient les lutins, car ils ne voulaient pas être vus.', 'Nobody knew what the elves looked like, for they did not want to be seen.'),
     S('So lebten die Kölner viele Jahre lang faul und zufrieden.', 'C’est ainsi que les habitants de Cologne vécurent de longues années, paresseux et contents.', 'And so the people of Cologne lived for many years, lazy and content.')],
  ], [
    W('bequem', '/bəˈkveːm/', 'commode, confortable', 'comfortable, easy'),
    W('der Handwerker', '/deːɐ̯ ˈhantˌvɛʁkɐ/', 'l’artisan', 'the craftsman'),
    W('erledigen', '/ɛɐ̯ˈleːdɪɡn̩/', 'accomplir, régler', 'to get done'),
    W('der Zimmermann', '/deːɐ̯ ˈtsɪmɐˌman/', 'le charpentier', 'the carpenter'),
    W('der Schneider', '/deːɐ̯ ˈʃnaɪdɐ/', 'le tailleur', 'the tailor'),
    W('bewegen', '/bəˈveːɡn̩/', 'bouger', 'to move'),
  ], [
    Q(('Quand les lutins travaillaient-ils ?', 'When did the elves work?'), [('La nuit, pendant que les artisans dormaient', 'At night, while the craftsmen slept'), ('Le dimanche seulement', 'Only on Sundays'), ('Le jour, avec les artisans', 'By day, with the craftsmen')], 0),
    Q(('Pourquoi personne ne savait-il à quoi ils ressemblaient ?', 'Why did nobody know what they looked like?'), [('Ils ne voulaient pas être vus', 'They did not want to be seen'), ('Ils portaient des masques', 'They wore masks'), ('Ils vivaient dans une autre ville', 'They lived in another town')], 0),
  ]),
  CH('heinzelmaennchen-2', ('Die neugierige Frau', 'La femme curieuse', 'The curious woman'), [
    [S('Die Frau des Schneiders war jedoch sehr neugierig. Sie wollte unbedingt wissen, wer nachts in der Werkstatt arbeitete.', 'La femme du tailleur, cependant, était très curieuse. Elle voulait absolument savoir qui travaillait la nuit dans l’atelier.', 'The tailor’s wife, however, was very curious. She absolutely wanted to know who worked in the workshop at night.'),
     S('Eines Abends streute sie Erbsen auf die Treppe und versteckte sich mit einer Lampe.', 'Un soir, elle répandit des petits pois sur l’escalier et se cacha avec une lampe.', 'One evening she scattered peas on the stairs and hid with a lamp.'),
     S('Als die Heinzelmännchen kamen, rutschten sie auf den Erbsen aus und fielen mit großem Lärm die Treppe hinunter.', 'Quand les lutins arrivèrent, ils glissèrent sur les pois et dégringolèrent l’escalier à grand bruit.', 'When the elves came, they slipped on the peas and tumbled down the stairs with a great noise.')],
    [S('Die Frau lief mit der Lampe herbei, um sie zu sehen. Aber die Heinzelmännchen waren schon verschwunden.', 'La femme accourut avec la lampe pour les voir. Mais les lutins avaient déjà disparu.', 'The woman came running with the lamp to see them. But the elves had already vanished.'),
     S('Seit dieser Nacht sind sie nie wieder zurückgekommen.', 'Depuis cette nuit-là, ils ne sont plus jamais revenus.', 'Since that night they have never come back.'),
     S('Deshalb müssen die Kölner heute alles selbst machen — und wenn die Frau nicht so neugierig gewesen wäre, hätten sie es noch immer bequem.', 'C’est pourquoi les habitants de Cologne doivent aujourd’hui tout faire eux-mêmes — et si la femme n’avait pas été aussi curieuse, ils auraient encore la vie facile.', 'That is why the people of Cologne have to do everything themselves today — and if the woman had not been so curious, they would still have an easy life.')],
  ], [
    W('neugierig', '/ˈnɔʏˌɡiːʁɪç/', 'curieux', 'curious'),
    W('streuen', '/ˈʃtʁɔʏən/', 'répandre, semer', 'to scatter'),
    W('die Erbse', '/diː ˈɛʁpsə/', 'le petit pois', 'the pea'),
    W('sich verstecken', '/zɪç fɛɐ̯ˈʃtɛkn̩/', 'se cacher', 'to hide'),
    W('ausrutschen', '/ˈaʊsˌʁʊtʃn̩/', 'glisser', 'to slip'),
    W('verschwinden', '/fɛɐ̯ˈʃvɪndn̩/', 'disparaître', 'to disappear'),
  ], [
    Q(('Que fait la femme du tailleur pour surprendre les lutins ?', 'What does the tailor’s wife do to catch the elves?'), [('Elle répand des pois sur l’escalier', 'She scatters peas on the stairs'), ('Elle ferme la porte à clé', 'She locks the door'), ('Elle leur prépare un repas', 'She cooks them a meal')], 0),
    Q(('Quelle est la conséquence pour les habitants de Cologne ?', 'What is the consequence for the people of Cologne?'), [('Ils doivent désormais tout faire eux-mêmes', 'They now have to do everything themselves'), ('Ils deviennent riches', 'They become rich'), ('Ils quittent la ville', 'They leave the town')], 0),
  ]),
])

ZAUBER = STORY('zauberlehrling', 'W', 'GOETHEB2', '#3F4A6B', ('Der Zauberlehrling', 'L’Apprenti sorcier', 'The Sorcerer’s Apprentice'),
  ('Le maître est sorti, et l’apprenti veut enfin essayer la magie tout seul. D’après la ballade de Goethe.', 'The master is out, and the apprentice finally wants to try magic on his own. After Goethe’s ballad.'), [
  CH('zauberlehrling-1', ('Der Meister ist fort', 'Le maître est sorti', 'The master is away'), [
    [S('Kaum hatte der alte Meister das Haus verlassen, beschloss sein Lehrling, die Gelegenheit zu nutzen.', 'À peine le vieux maître avait-il quitté la maison que son apprenti décida de profiter de l’occasion.', 'Hardly had the old master left the house when his apprentice decided to seize the opportunity.'),
     S('Er hatte oft genug beobachtet, wie der Meister zauberte, und war überzeugt, es genauso gut zu können.', 'Il avait observé assez souvent comment le maître pratiquait la magie, et il était convaincu de pouvoir en faire autant.', 'He had watched the master work magic often enough and was convinced he could do it just as well.'),
     S('Statt selbst Wasser für das Bad zu holen, sprach er die Worte, die er gehört hatte, und der alte Besen in der Ecke begann sich zu bewegen.', 'Au lieu d’aller chercher lui-même l’eau du bain, il prononça les mots qu’il avait entendus, et le vieux balai, dans son coin, se mit à bouger.', 'Instead of fetching the bath water himself, he spoke the words he had heard, and the old broom in the corner began to move.')],
    [S('Dem Besen wuchsen zwei Beine und ein Kopf, und er lief zum Fluss, als hätte er nie etwas anderes getan.', 'Deux jambes et une tête poussèrent au balai, et il courut à la rivière comme s’il n’avait jamais rien fait d’autre.', 'The broom grew two legs and a head, and it ran to the river as if it had never done anything else.'),
     S('Eimer um Eimer wurde herbeigetragen, und bald war die Wanne gefüllt.', 'Seau après seau fut apporté, et la baignoire fut bientôt remplie.', 'Bucket after bucket was carried in, and soon the tub was full.'),
     S('Der Lehrling war stolz: Wozu sollte man jahrelang lernen, wenn sich alles so leicht erledigen ließ?', 'L’apprenti était fier : à quoi bon étudier pendant des années, si tout se réglait aussi facilement ?', 'The apprentice was proud: why study for years if everything could be done so easily?')],
  ], [
    W('die Gelegenheit', '/diː ɡəˈleːɡn̩haɪt/', 'l’occasion', 'the opportunity'),
    W('beobachten', '/bəˈʔoːbaxtn̩/', 'observer', 'to watch, to observe'),
    W('überzeugt', '/yːbɐˈtsɔʏkt/', 'convaincu', 'convinced'),
    W('der Eimer', '/deːɐ̯ ˈaɪmɐ/', 'le seau', 'the bucket'),
    W('die Wanne', '/diː ˈvanə/', 'la baignoire', 'the tub'),
    W('stolz', '/ʃtɔlts/', 'fier', 'proud'),
  ], [
    Q(('Pourquoi l’apprenti pense-t-il pouvoir faire de la magie ?', 'Why does the apprentice think he can work magic?'), [('Il a souvent observé le maître', 'He has often watched the master'), ('Le maître lui a tout appris', 'The master has taught him everything'), ('Il a trouvé un livre de formules', 'He has found a book of spells')], 0),
    Q(('Que fait le balai ensorcelé ?', 'What does the enchanted broom do?'), [('Il va chercher de l’eau à la rivière', 'It fetches water from the river'), ('Il balaie tout l’atelier', 'It sweeps the whole workshop'), ('Il s’envole par la fenêtre', 'It flies out of the window')], 0),
  ]),
  CH('zauberlehrling-2', ('Die Geister, die ich rief', 'Les esprits que j’ai appelés', 'The spirits I summoned'), [
    [S('Doch der Besen hörte nicht auf: Das Wasser lief über den Rand der Wanne und stand bald im ganzen Zimmer.', 'Mais le balai ne s’arrêtait pas : l’eau déborda de la baignoire et monta bientôt dans toute la pièce.', 'But the broom did not stop: the water ran over the edge of the tub and soon stood in the whole room.'),
     S('Erst jetzt wurde dem Lehrling klar, dass er das Wort vergessen hatte, mit dem sich der Zauber beenden ließ.', 'C’est seulement alors que l’apprenti comprit qu’il avait oublié le mot qui permettait de mettre fin au sortilège.', 'Only now did the apprentice realise that he had forgotten the word with which the spell could be ended.'),
     S('In seiner Verzweiflung griff er zum Beil und schlug den Besen entzwei, aber nun liefen zwei Besen zum Fluss, und das Wasser stieg doppelt so schnell.', 'Dans son désespoir, il saisit la hache et fendit le balai en deux, mais voilà que deux balais couraient à la rivière, et l’eau monta deux fois plus vite.', 'In his despair he seized the axe and split the broom in two, but now two brooms ran to the river, and the water rose twice as fast.')],
    [S('Wäre der Meister nicht in diesem Augenblick zurückgekehrt, wäre das ganze Haus überschwemmt worden.', 'Si le maître n’était pas revenu à cet instant, toute la maison aurait été inondée.', 'Had the master not returned at that moment, the whole house would have been flooded.'),
     S('Mit einem einzigen Satz schickte er die Besen in die Ecke zurück und erklärte, nur der Meister dürfe sie rufen.', 'D’une seule phrase, il renvoya les balais dans leur coin et déclara que seul le maître avait le droit de les appeler.', 'With a single sentence he sent the brooms back to their corner and declared that only the master might call them.'),
     S('Der Lehrling soll danach geschworen haben, nie wieder etwas zu beginnen, was er nicht auch beenden könne.', 'On dit que l’apprenti jura ensuite de ne plus jamais commencer ce qu’il ne saurait pas aussi terminer.', 'The apprentice is said to have sworn afterwards never again to start anything he could not also finish.')],
  ], [
    W('der Rand', '/deːɐ̯ ʁant/', 'le bord', 'the edge'),
    W('der Zauber', '/deːɐ̯ ˈtsaʊbɐ/', 'le sortilège, la magie', 'the spell, magic'),
    W('die Verzweiflung', '/diː fɛɐ̯ˈtsvaɪflʊŋ/', 'le désespoir', 'despair'),
    W('das Beil', '/das baɪl/', 'la hache', 'the axe'),
    W('zurückkehren', '/tsuˈʁʏkˌkeːʁən/', 'revenir', 'to return'),
    W('schwören', '/ˈʃvøːʁən/', 'jurer', 'to swear'),
  ], [
    Q(('Quel est le problème de l’apprenti ?', 'What is the apprentice’s problem?'), [('Il a oublié le mot qui arrête le sortilège', 'He has forgotten the word that stops the spell'), ('Il ne trouve plus le balai', 'He cannot find the broom any more'), ('Le maître a emporté la baignoire', 'The master has taken the tub away')], 0),
    Q(('Que se passe-t-il quand il fend le balai ?', 'What happens when he splits the broom?'), [('Deux balais apportent de l’eau', 'Two brooms bring water'), ('Le balai s’arrête enfin', 'The broom finally stops'), ('L’eau disparaît', 'The water disappears')], 0),
  ]),
])

ERLKOENIG = STORY('erlkoenig', 'E', 'GOETHEB2', '#2F4F4A', ('Der Erlkönig', 'Le Roi des Aulnes', 'The Erlking'),
  ('Un père chevauche dans la nuit avec son fils malade, et l’enfant voit ce que le père ne voit pas. D’après la ballade de Goethe.', 'A father rides through the night with his sick son, and the child sees what the father does not. After Goethe’s ballad.'), [
  CH('erlkoenig-1', ('Der Ritt durch die Nacht', 'La chevauchée dans la nuit', 'The ride through the night'), [
    [S('Spät in der Nacht ritt ein Vater durch den Wind, seinen kranken Sohn fest im Arm.', 'Tard dans la nuit, un père chevauchait dans le vent, son fils malade serré dans ses bras.', 'Late at night a father rode through the wind, his sick son held tight in his arms.'),
     S('Plötzlich verbarg das Kind sein Gesicht und fragte, ob der Vater den Erlkönig mit Krone und Mantel nicht sehe.', 'Soudain, l’enfant cacha son visage et demanda si le père ne voyait pas le Roi des Aulnes avec sa couronne et son manteau.', 'Suddenly the child hid his face and asked whether his father did not see the Erlking with his crown and cloak.'),
     S('Der Vater antwortete ruhig, das sei nur ein Streifen Nebel über den Wiesen.', 'Le père répondit calmement que ce n’était qu’une traînée de brouillard au-dessus des prés.', 'The father answered calmly that it was only a streak of mist over the meadows.')],
    [S('Doch das Kind hörte eine leise Stimme, die ihm schöne Spiele und bunte Blumen am Ufer versprach.', 'Mais l’enfant entendait une voix douce qui lui promettait de beaux jeux et des fleurs de toutes les couleurs sur la rive.', 'But the child heard a soft voice that promised him lovely games and bright flowers on the shore.'),
     S('„Hörst du nicht, was er mir zuflüstert?“, rief es. Der Vater meinte, es sei bloß der Wind in den trockenen Blättern.', '« N’entends-tu pas ce qu’il me chuchote ? » s’écria-t-il. Le père estima que ce n’était que le vent dans les feuilles sèches.', '“Do you not hear what he whispers to me?” he cried. The father said it was merely the wind in the dry leaves.'),
     S('Er tat so, als ob er keine Angst hätte, und trieb das Pferd dennoch schneller an.', 'Il faisait comme s’il n’avait pas peur, et pourtant il pressa son cheval.', 'He acted as if he were not afraid, and yet he urged the horse on faster.')],
  ], [
    W('verbergen', '/fɛɐ̯ˈbɛʁɡn̩/', 'cacher', 'to hide'),
    W('die Krone', '/diː ˈkʁoːnə/', 'la couronne', 'the crown'),
    W('der Streifen', '/deːɐ̯ ˈʃtʁaɪfn̩/', 'la bande, la traînée', 'the streak, the strip'),
    W('die Wiese', '/diː ˈviːzə/', 'le pré', 'the meadow'),
    W('das Ufer', '/das ˈuːfɐ/', 'la rive', 'the shore, the bank'),
    W('antreiben', '/ˈanˌtʁaɪbn̩/', 'presser, pousser en avant', 'to urge on'),
  ], [
    Q(('Que voit l’enfant ?', 'What does the child see?'), [('Le Roi des Aulnes avec une couronne', 'The Erlking with a crown'), ('Un loup au bord du chemin', 'A wolf by the roadside'), ('Sa mère qui l’attend', 'His mother waiting for him')], 0),
    Q(('Comment le père explique-t-il ce que l’enfant voit et entend ?', 'How does the father explain what the child sees and hears?'), [('Par le brouillard et le vent', 'By the mist and the wind'), ('Par un rêve', 'By a dream'), ('Par des voyageurs sur la route', 'By travellers on the road')], 0),
  ]),
  CH('erlkoenig-2', ('Die Stimme im Wind', 'La voix dans le vent', 'The voice in the wind'), [
    [S('Die Stimme wurde lockender: Die Töchter des Königs würden das Kind wiegen und für es tanzen und singen.', 'La voix se fit plus enjôleuse : les filles du roi berceraient l’enfant, danseraient et chanteraient pour lui.', 'The voice grew more enticing: the king’s daughters would rock the child and dance and sing for him.'),
     S('Der Vater behauptete, dort hinten stünden nur alte, graue Weiden, obwohl ihm selbst unheimlich zumute war.', 'Le père affirma qu’il n’y avait là-bas que de vieux saules gris, alors que lui-même se sentait mal à l’aise.', 'The father claimed that only old grey willows stood over there, although he himself felt uneasy.'),
     S('Da drohte die Stimme: Wenn das Kind nicht freiwillig komme, werde sie Gewalt gebrauchen.', 'Alors la voix menaça : si l’enfant ne venait pas de son plein gré, elle emploierait la force.', 'Then the voice threatened: if the child did not come willingly, it would use force.')],
    [S('Das Kind schrie auf, der Erlkönig habe ihm wehgetan, und dem Vater lief es kalt über den Rücken.', 'L’enfant poussa un cri : le Roi des Aulnes lui avait fait mal ; et le père sentit un frisson lui courir dans le dos.', 'The child cried out that the Erlking had hurt him, and a shiver ran down the father’s back.'),
     S('Er ritt, so schnell er konnte, und erreichte den Hof mit letzter Kraft.', 'Il chevaucha aussi vite qu’il le put et atteignit la ferme à bout de forces.', 'He rode as fast as he could and reached the farm with his last strength.'),
     S('Als er aber in seine Arme blickte, war es zu spät: Hätte er dem Kind doch nur früher geglaubt!', 'Mais quand il baissa les yeux vers ses bras, il était trop tard : si seulement il avait cru l’enfant plus tôt !', 'But when he looked down into his arms, it was too late: if only he had believed the child sooner!')],
  ], [
    W('wiegen', '/ˈviːɡn̩/', 'bercer', 'to rock'),
    W('die Weide', '/diː ˈvaɪdə/', 'le saule', 'the willow'),
    W('unheimlich', '/ˈʊnhaɪmlɪç/', 'inquiétant, sinistre', 'eerie, uncanny'),
    W('drohen', '/ˈdʁoːən/', 'menacer', 'to threaten'),
    W('die Gewalt', '/diː ɡəˈvalt/', 'la force, la violence', 'force, violence'),
    W('der Hof', '/deːɐ̯ hoːf/', 'la ferme, la cour', 'the farm, the yard'),
  ], [
    Q(('Que promet la voix à l’enfant ?', 'What does the voice promise the child?'), [('Que les filles du roi s’occuperont de lui', 'That the king’s daughters will look after him'), ('Qu’il deviendra roi à son tour', 'That he will become king in turn'), ('Que son père sera riche', 'That his father will be rich')], 0),
    Q(('Que regrette le père à la fin ?', 'What does the father regret at the end?'), [('De ne pas avoir cru l’enfant plus tôt', 'Not having believed the child sooner'), ('D’avoir pris le mauvais chemin', 'Having taken the wrong road'), ('D’être parti sans manteau', 'Having left without a cloak')], 0),
  ]),
])

DE_STORIES = [BREMER, BREI, STERN, FROSCH, HANS, FISCHER, HEINZEL, ZAUBER, ERLKOENIG]

import sys
sys.path.insert(0, os.path.dirname(__file__))
from reading_mix import mix
mix(DE_STORIES)

data = json.load(open(P, encoding='utf-8'))
data['stories'] = [s for s in data['stories'] if not s['level'].startswith('GOETHE')] + DE_STORIES
data.setdefault('notices', {})['de'] = {'fr': 'Contes des frères Grimm, légendes d’Allemagne et ballades de Goethe (domaine public), réécrits en prose et en allemand simple pour Koto Quest. La prononciation des mots est notée en alphabet phonétique (allemand standard).', 'en': 'Tales by the Brothers Grimm, legends of Germany and ballads by Goethe (public domain), retold in prose and in simple German for Koto Quest. Word pronunciation is given in the phonetic alphabet (standard German).'}
slugs = [c['slug'] for s in data['stories'] for c in s['chapters']]
assert len(slugs) == len(set(slugs)), 'slug de chapitre en double'
others = {s['glyph'] for s in data['stories'] if not s['level'].startswith('GOETHE')}
glyphs = [s['glyph'] for s in DE_STORIES]
assert len(glyphs) == len(set(glyphs)) and not others & set(glyphs), 'glyphe de conte en double'
for s in DE_STORIES:
    for c in s['chapters']:
        assert len(c['words']) >= 6, c['slug']
        for q in c['questions']:
            assert 0 <= q['answer'] < len(q['choices'])
json.dump(data, open(P, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('Contes allemands :', len(DE_STORIES), 'contes,', sum(len(s['chapters']) for s in DE_STORIES), 'chapitres')
