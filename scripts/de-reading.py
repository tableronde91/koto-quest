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

DE_STORIES = [BREMER, BREI, STERN, FROSCH, HANS]

import sys
sys.path.insert(0, os.path.dirname(__file__))
from reading_mix import mix
mix(DE_STORIES)

data = json.load(open(P, encoding='utf-8'))
data['stories'] = [s for s in data['stories'] if not s['level'].startswith('GOETHE')] + DE_STORIES
data.setdefault('notices', {})['de'] = {'fr': 'Contes des frères Grimm et légendes d’Allemagne (domaine public), réécrits en allemand simple pour Koto Quest. La prononciation des mots est notée en alphabet phonétique (allemand standard).', 'en': 'Tales by the Brothers Grimm and legends of Germany (public domain), retold in simple German for Koto Quest. Word pronunciation is given in the phonetic alphabet (standard German).'}
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
