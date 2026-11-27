# Niveau Goethe-Zertifikat A2 (allemand, CECRL A2) : 8 étapes du Rhin à la Forêt-Noire, sur les traces de nouveaux contes.
# Mode histoire : l'apprenti·e des frères Grimm poursuit les personnages échappés jusque dans les châteaux et les forêts du Sud (voir gen-story.py).
# Usage : python3 scripts/goethea2-level.py   (réécrit content/goethea2/goethea2.json ; le Goethe A1 doit déjà exister)
from de_common import *
begin('GOETHEA2')

REGION = 'Forêt-Noire'

# ═════════════════════════ 1 : Le passé composé avec haben ═════════════════════════
W1 = WORLD('goethea2-w1', ('Le puits du Roi Grenouille', 'The Frog King’s well'), REGION,
  ('Raconter ce qu’on a fait avec le Perfekt (haben + participe), former les participes réguliers et irréguliers, situer une action dans le passé.', 'Say what you did with the Perfekt (haben + participle), form regular and irregular participles, place an action in the past.'),
  (('Le Roi Grenouille', 'The Frog King'), '♔', ('Au fond du puits, le Roi Grenouille garde la balle d’or de la princesse : il ne la rendra qu’à qui lui racontera sa journée d’hier sans une faute. Qu’as-tu fait, mangé, vu, perdu ?', 'At the bottom of the well, the Frog King keeps the princess’s golden ball: he will only return it to someone who tells him about yesterday without a mistake. What did you do, eat, see, lose?')),
  [CH('goethea2-w1-c1', ('Qu’as-tu fait hier ?', 'What did you do yesterday?'), [
    L('de-perfekt-haben', ('Le Perfekt avec haben', 'The Perfekt with haben'), ('Raconter une action passée avec haben et le participe en fin de phrase.', 'Describe a past action with haben and the participle at the end of the sentence.'), 9, [
        ('À l’oral, le passé se dit presque toujours au Perfekt : haben conjugué en deuxième position + participe passé à la fin. Ich habe gestern Fußball gespielt.', 'In speech, the past is almost always the Perfekt: conjugated haben in second position + past participle at the end. Ich habe gestern Fußball gespielt.'),
        ('Participe régulier : ge- + radical + -t. spielen → gespielt, machen → gemacht, kaufen → gekauft, lernen → gelernt. Radical en -t ou -d : -et (arbeiten → gearbeitet).', 'Regular participle: ge- + stem + -t. spielen → gespielt, machen → gemacht, kaufen → gekauft, lernen → gelernt. Stem in -t or -d: -et (arbeiten → gearbeitet).'),
        ('Pas de ge- pour les verbes en -ieren (telefonieren → telefoniert) ni pour les préfixes inséparables be-, ver-, er- (besuchen → besucht, verkaufen → verkauft).', 'No ge- for verbs in -ieren (telefonieren → telefoniert) or with the inseparable prefixes be-, ver-, er- (besuchen → besucht, verkaufen → verkauft).'),
      ], [
        DG('perfekt-haben', 'haben + Partizip II', ('passé composé avec haben', 'perfect tense with haben')),
        DG('partizip-ge-t', 'ge- + Stamm + -t', ('participe passé régulier', 'regular past participle')),
        D('gemacht', 'machen → gemacht', ('faire → fait', 'to do, to make → done, made')),
        D('gespielt', 'spielen → gespielt', ('jouer → joué', 'to play → played')),
        D('gekauft', 'kaufen → gekauft', ('acheter → acheté', 'to buy → bought')),
        D('besucht', 'besuchen → besucht', ('rendre visite → rendu visite', 'to visit → visited')),
        D('gestern', 'gestern', ('hier', 'yesterday')),
        D('schon', 'schon', ('déjà', 'already')),
      ], [
        x('Was hast du gestern gemacht? — Ich habe im Garten gespielt.', 'Qu’as-tu fait hier ? — J’ai joué dans le jardin.', 'What did you do yesterday? — I played in the garden.'),
        x('Die Prinzessin hat eine goldene Kugel gekauft.', 'La princesse a acheté une balle d’or.', 'The princess bought a golden ball.'),
      ], [
        FB(CHOOSE, 'Ich habe gestern Tennis ＿.', ['gespielt', 'spielen', 'spielt'], 'gespielt', ('Perfekt : haben + participe gespielt, à la fin.', 'Perfekt: haben + participle gespielt, at the end.'), ('J’ai joué au tennis hier.', 'I played tennis yesterday.')),
        FB(CHOOSE, 'Wir ＿ unsere Großmutter besucht.', ['haben', 'sind', 'hat'], 'haben', ('Besuchen se conjugue avec haben : wir haben… besucht.', 'Besuchen takes haben: wir haben… besucht.'), ('Nous avons rendu visite à notre grand-mère.', 'We visited our grandmother.')),
        order(('Remets dans l’ordre : « Qu’as-tu fait hier ? »', 'Put in order: “What did you do yesterday?”'), ['Was', 'hast', 'du', 'gestern', 'gemacht?'], ('Haben en deuxième position, le participe à la fin.', 'Haben in second position, the participle at the end.')),
        TF('Er hat das Buch schon gekauft.', ('Il n’a pas encore acheté le livre.', 'He has not bought the book yet.'), FAUX, ('Schon = déjà : le livre est acheté.', 'Schon = already: the book has been bought.')),
      ]),
    L('de-partizip-irr', ('Les participes irréguliers', 'Irregular participles'), ('Employer les participes en -en des verbes forts les plus courants.', 'Use the -en participles of the most common strong verbs.'), 9, [
        ('Les verbes forts font leur participe en ge- + radical (souvent modifié) + -en : essen → gegessen, trinken → getrunken, sehen → gesehen, lesen → gelesen, schreiben → geschrieben.', 'Strong verbs form their participle with ge- + stem (often changed) + -en: essen → gegessen, trinken → getrunken, sehen → gesehen, lesen → gelesen, schreiben → geschrieben.'),
        ('Avec une particule séparable, ge- se glisse au milieu : einkaufen → eingekauft, anrufen → angerufen, fernsehen → ferngesehen.', 'With a separable prefix, ge- slips into the middle: einkaufen → eingekauft, anrufen → angerufen, fernsehen → ferngesehen.'),
        ('Quelques formes à connaître par cœur : nehmen → genommen, finden → gefunden, verlieren → verloren, vergessen → vergessen, bringen → gebracht.', 'A few forms to learn by heart: nehmen → genommen, finden → gefunden, verlieren → verloren, vergessen → vergessen, bringen → gebracht.'),
      ], [
        D('gegessen', 'essen → gegessen', ('manger → mangé', 'to eat → eaten')),
        D('getrunken', 'trinken → getrunken', ('boire → bu', 'to drink → drunk')),
        D('gesehen', 'sehen → gesehen', ('voir → vu', 'to see → seen')),
        D('gelesen', 'lesen → gelesen', ('lire → lu', 'to read → read')),
        D('geschrieben', 'schreiben → geschrieben', ('écrire → écrit', 'to write → written')),
        D('gefunden', 'finden → gefunden', ('trouver → trouvé', 'to find → found')),
        D('verloren', 'verlieren → verloren', ('perdre → perdu', 'to lose → lost')),
        D('angerufen', 'anrufen → angerufen', ('appeler (au téléphone) → appelé', 'to phone → phoned')),
      ], [
        x('Die Prinzessin hat ihre Kugel verloren, und der Frosch hat sie gefunden.', 'La princesse a perdu sa balle, et la grenouille l’a trouvée.', 'The princess lost her ball, and the frog found it.'),
        x('Hast du das Märchen schon gelesen? — Nein, aber ich habe den Film gesehen.', 'As-tu déjà lu le conte ? — Non, mais j’ai vu le film.', 'Have you already read the tale? — No, but I have seen the film.'),
      ], [
        FB(CHOOSE, 'Der Frosch hat vom goldenen Teller ＿.', ['gegessen', 'geesst', 'essen'], 'gegessen', ('Essen → gegessen (irrégulier).', 'Essen → gegessen (irregular).'), ('La grenouille a mangé dans l’assiette d’or.', 'The frog ate from the golden plate.')),
        FB(CHOOSE, 'Ich habe meinen Schlüssel ＿.', ['verloren', 'geverloren', 'verliert'], 'verloren', ('Verlieren → verloren : pas de ge- avec le préfixe ver-.', 'Verlieren → verloren: no ge- with the prefix ver-.'), ('J’ai perdu ma clé.', 'I have lost my key.')),
        FB(CHOOSE, 'Sie hat ihre Mutter ＿.', ['angerufen', 'geanruft', 'anrufen'], 'angerufen', ('Particule séparable : an-ge-rufen.', 'Separable prefix: an-ge-rufen.'), ('Elle a appelé sa mère.', 'She phoned her mother.')),
        DC(ANSWER, [('Frosch', 'Was hast du heute gegessen?')], ('La grenouille te demande ce que tu as mangé (une soupe).', 'The frog asks what you ate (a soup).'), ['Ich habe eine Suppe gegessen.', 'Ich esse eine Suppe gegessen.', 'Ich bin eine Suppe.'], 'Ich habe eine Suppe gegessen.', ('Perfekt : ich habe… gegessen.', 'Perfekt: ich habe… gegessen.')),
      ]),
  ]),
  CH('goethea2-w1-c2', ('La balle d’or', 'The golden ball'), [
    L('de-zeit-vergangen', ('Situer dans le passé', 'Placing events in the past'), ('Dire quand une action a eu lieu et depuis combien de temps.', 'Say when an action took place and for how long.'), 8, [
        ('Repères du passé : gestern (hier), vorgestern (avant-hier), letzte Woche (la semaine dernière), letztes Jahr (l’année dernière), vor zwei Tagen (il y a deux jours).', 'Past time markers: gestern (yesterday), vorgestern (the day before yesterday), letzte Woche (last week), letztes Jahr (last year), vor zwei Tagen (two days ago).'),
        ('Vor + datif = il y a : vor einem Jahr, vor drei Wochen. Seit + datif = depuis, avec le présent : Ich lerne seit einem Jahr Deutsch (j’apprends l’allemand depuis un an).', 'Vor + dative = ago: vor einem Jahr, vor drei Wochen. Seit + dative = for / since, with the present tense: Ich lerne seit einem Jahr Deutsch (I have been learning German for a year).'),
        ('Noch nie = jamais encore ; schon einmal = déjà une fois. Warst du schon einmal in Heidelberg? — Nein, noch nie.', 'Noch nie = never yet; schon einmal = once before. Warst du schon einmal in Heidelberg? — Nein, noch nie.'),
      ], [
        D('letzte-woche', 'letzte Woche', ('la semaine dernière', 'last week')),
        D('letztes-jahr', 'letztes Jahr', ('l’année dernière', 'last year')),
        DG('vor-zeit', 'vor + Dativ (Zeit)', ('il y a (+ durée)', 'ago')),
        DG('seit', 'seit + Dativ', ('depuis', 'since, for (time)')),
        D('noch-nie', 'noch nie', ('jamais encore', 'never before')),
        D('frueher', 'früher', ('autrefois, avant', 'in the past, formerly')),
        D('danach', 'danach', ('après cela', 'after that')),
        D('zuerst', 'zuerst', ('d’abord', 'first, at first')),
      ], [
        x('Vor drei Tagen hat die Prinzessin am Brunnen gespielt.', 'Il y a trois jours, la princesse a joué près du puits.', 'Three days ago the princess played by the well.'),
        x('Der Frosch wohnt seit einem Jahr im Brunnen.', 'La grenouille habite dans le puits depuis un an.', 'The frog has lived in the well for a year.'),
      ], [
        FB(CHOOSE, 'Ich lerne ＿ zwei Jahren Deutsch.', ['seit', 'vor', 'letzte'], 'seit', ('Action qui dure encore : seit + datif, avec le présent.', 'An action still going on: seit + dative, with the present.'), ('J’apprends l’allemand depuis deux ans.', 'I have been learning German for two years.')),
        FB(CHOOSE, '＿ einer Woche habe ich ihn gesehen.', ['Vor', 'Seit', 'Früher'], 'Vor', ('Il y a une semaine : vor einer Woche.', 'A week ago: vor einer Woche.'), ('Je l’ai vu il y a une semaine.', 'I saw him a week ago.')),
        TF('Ich habe noch nie einen Frosch geküsst.', ('La personne a déjà embrassé une grenouille.', 'The person has already kissed a frog.'), FAUX, ('Noch nie = jamais encore.', 'Noch nie = never before.')),
        order(('Remets dans l’ordre : « D’abord j’ai mangé, ensuite j’ai lu. »', 'Put in order: “First I ate, then I read.”'), ['Zuerst', 'habe', 'ich', 'gegessen,', 'danach', 'habe', 'ich', 'gelesen.'], ('Zuerst et danach en tête : le verbe reste deuxième, le sujet le suit.', 'Zuerst and danach first: the verb stays second, the subject follows.')),
      ]),
  ])])

# ═════════════════════════ 2 : Perfekt avec sein, war / hatte, la fête ═════════════════════════
W2 = WORLD('goethea2-w2', ('Le bal de Cendrillon', 'Cinderella’s ball'), REGION,
  ('Employer le Perfekt avec sein pour les déplacements, le prétérit de sein et haben, inviter, accepter et refuser.', 'Use the Perfekt with sein for movement, the simple past of sein and haben, invite, accept and decline.'),
  (('La Marâtre de Cendrillon', 'Cinderella’s Stepmother'), '♟', ('La Marâtre a enfermé Cendrillon et mêlé les lentilles aux cendres. Elle n’ouvrira la porte qu’à qui racontera le bal : qui est venu, où es-tu allé, comment c’était ?', 'The Stepmother has locked Cinderella in and mixed the lentils into the ashes. She will only open the door to someone who can describe the ball: who came, where did you go, what was it like?')),
  [CH('goethea2-w2-c1', ('Aller et revenir', 'There and back'), [
    L('de-perfekt-sein', ('Le Perfekt avec sein', 'The Perfekt with sein'), ('Raconter un déplacement ou un changement d’état au passé.', 'Describe movement or a change of state in the past.'), 9, [
        ('Les verbes de déplacement et de changement d’état forment leur Perfekt avec sein : gehen → ist gegangen, kommen → ist gekommen, fahren → ist gefahren, fliegen → ist geflogen.', 'Verbs of movement and change of state form the Perfekt with sein: gehen → ist gegangen, kommen → ist gekommen, fahren → ist gefahren, fliegen → ist geflogen.'),
        ('Aussi avec sein : bleiben → ist geblieben (rester), sein → ist gewesen (être), aufstehen → ist aufgestanden, einschlafen → ist eingeschlafen, passieren → ist passiert.', 'Also with sein: bleiben → ist geblieben (to stay), sein → ist gewesen (to be), aufstehen → ist aufgestanden, einschlafen → ist eingeschlafen, passieren → ist passiert.'),
        ('Test simple : je vais de A à B, ou mon état change → sein. Tout le reste → haben. Ich bin nach Hause gegangen, mais Ich habe zu Hause gegessen.', 'Simple test: I go from A to B, or my state changes → sein. Everything else → haben. Ich bin nach Hause gegangen, but Ich habe zu Hause gegessen.'),
      ], [
        DG('perfekt-sein', 'sein + Partizip II', ('passé composé avec sein', 'perfect tense with sein')),
        D('gegangen', 'gehen → ist gegangen', ('aller → allé', 'to go → gone')),
        D('gekommen', 'kommen → ist gekommen', ('venir → venu', 'to come → come')),
        D('gefahren', 'fahren → ist gefahren', ('aller (en véhicule) → allé', 'to go (by vehicle) → gone')),
        D('geblieben', 'bleiben → ist geblieben', ('rester → resté', 'to stay → stayed')),
        D('aufgestanden', 'aufstehen → ist aufgestanden', ('se lever → levé', 'to get up → got up')),
        D('passiert', 'Was ist passiert?', ('Que s’est-il passé ?', 'What happened?')),
        D('tanzen', 'tanzen', ('danser', 'to dance')),
      ], [
        x('Aschenputtel ist zum Ball gegangen und hat mit dem Prinzen getanzt.', 'Cendrillon est allée au bal et a dansé avec le prince.', 'Cinderella went to the ball and danced with the prince.'),
        x('Um Mitternacht ist sie schnell nach Hause gefahren.', 'À minuit, elle est vite rentrée chez elle.', 'At midnight she quickly went home.'),
      ], [
        FB(CHOOSE, 'Ich ＿ gestern ins Kino gegangen.', ['bin', 'habe', 'ist'], 'bin', ('Gehen (déplacement) se conjugue avec sein : ich bin gegangen.', 'Gehen (movement) takes sein: ich bin gegangen.'), ('Hier, je suis allé au cinéma.', 'Yesterday I went to the cinema.')),
        FB(CHOOSE, 'Wir ＿ Pizza gegessen.', ['haben', 'sind', 'seid'], 'haben', ('Essen n’est pas un déplacement : haben.', 'Essen is not movement: haben.'), ('Nous avons mangé une pizza.', 'We ate pizza.')),
        FB(CHOOSE, 'Er ist zu Hause ＿.', ['geblieben', 'gebleibt', 'bleiben'], 'geblieben', ('Bleiben → geblieben, avec sein.', 'Bleiben → geblieben, with sein.'), ('Il est resté à la maison.', 'He stayed at home.')),
        DC(ANSWER, [('Stiefmutter', 'Was ist passiert?')], ('La Marâtre demande ce qui s’est passé (Cendrillon est partie).', 'The Stepmother asks what happened (Cinderella has left).'), ['Aschenputtel ist weggegangen.', 'Aschenputtel hat weggegangen.', 'Aschenputtel geht gestern.'], 'Aschenputtel ist weggegangen.', ('Weggehen : déplacement, donc ist weggegangen.', 'Weggehen: movement, so ist weggegangen.')),
      ]),
    L('de-war-hatte', ('C’était… : war et hatte', 'It was…: war and hatte'), ('Décrire une situation passée avec le prétérit de sein et haben.', 'Describe a past situation with the simple past of sein and haben.'), 8, [
        ('Pour sein et haben, on préfère le prétérit au Perfekt : ich war (j’étais, j’ai été), du warst, er war, wir waren, ihr wart, sie waren.', 'For sein and haben, the simple past is preferred to the Perfekt: ich war (I was), du warst, er war, wir waren, ihr wart, sie waren.'),
        ('Haben : ich hatte (j’avais, j’ai eu), du hattest, er hatte, wir hatten, ihr hattet, sie hatten. Ich hatte keine Zeit.', 'Haben: ich hatte (I had), du hattest, er hatte, wir hatten, ihr hattet, sie hatten. Ich hatte keine Zeit.'),
        ('Pour donner son avis sur un moment passé : Wie war das Fest? — Es war toll / schön / langweilig. Es hat mir gefallen (ça m’a plu).', 'To give an opinion on a past event: Wie war das Fest? — Es war toll / schön / langweilig. Es hat mir gefallen (I liked it).'),
      ], [
        DG('war', 'ich war / du warst / er war', ('j’étais / tu étais / il était', 'I was / you were / he was')),
        DG('hatte', 'ich hatte / du hattest / er hatte', ('j’avais / tu avais / il avait', 'I had / you had / he had')),
        D('toll', 'toll', ('génial, super', 'great, fantastic')),
        D('langweilig', 'langweilig', ('ennuyeux', 'boring')),
        D('fest', 'das Fest', ('la fête', 'the party, the celebration')),
        D('zeit-haben', 'Zeit haben', ('avoir le temps', 'to have time')),
        D('gefallen', 'Es hat mir gefallen.', ('Ça m’a plu.', 'I liked it.')),
        D('muede', 'müde', ('fatigué', 'tired')),
      ], [
        x('Wie war der Ball? — Er war toll, aber ich hatte nur wenig Zeit.', 'Comment était le bal ? — Il était génial, mais je n’avais que peu de temps.', 'How was the ball? — It was great, but I only had a little time.'),
        x('Die Schwestern waren müde und hatten schlechte Laune.', 'Les sœurs étaient fatiguées et de mauvaise humeur.', 'The sisters were tired and in a bad mood.'),
      ], [
        FB(CHOOSE, 'Gestern ＿ ich sehr müde.', ['war', 'hatte', 'bin'], 'war', ('Être au passé : ich war.', 'To be in the past: ich war.'), ('Hier, j’étais très fatigué.', 'Yesterday I was very tired.')),
        FB(CHOOSE, 'Wir ＿ leider keine Zeit.', ['hatten', 'waren', 'hattet'], 'hatten', ('Avoir au passé, avec wir : hatten.', 'To have in the past, with wir: hatten.'), ('Nous n’avions malheureusement pas le temps.', 'Unfortunately we had no time.')),
        TF('Das Fest war langweilig.', ('La fête était géniale.', 'The party was great.'), FAUX, ('Langweilig = ennuyeux.', 'Langweilig = boring.')),
        DC(ANSWER, [('Prinz', 'Wie war der Abend?')], ('Le prince te demande comment était la soirée (elle t’a plu).', 'The prince asks how the evening was (you liked it).'), ['Er war toll. Es hat mir gefallen.', 'Er hatte toll.', 'Ich bin toll gewesen haben.'], 'Er war toll. Es hat mir gefallen.', ('Avis au passé : es war + adjectif.', 'Opinion in the past: es war + adjective.')),
      ]),
  ]),
  CH('goethea2-w2-c2', ('Trois soirs de fête', 'Three nights of celebration'), [
    L('de-einladen', ('Inviter, accepter, refuser', 'Inviting, accepting, declining'), ('Inviter quelqu’un, fixer un rendez-vous et répondre à une invitation.', 'Invite someone, arrange to meet and reply to an invitation.'), 8, [
        ('Inviter : Ich möchte dich zu meinem Geburtstag einladen. Hast du am Samstag Zeit? Kommst du mit? (tu viens avec nous ?).', 'Inviting: Ich möchte dich zu meinem Geburtstag einladen. Hast du am Samstag Zeit? Kommst du mit? (are you coming along?).'),
        ('Accepter : Ja, gern! / Ich komme gern. / Vielen Dank für die Einladung. Refuser : Tut mir leid, ich kann leider nicht. / Da habe ich schon etwas vor (j’ai déjà quelque chose de prévu).', 'Accepting: Ja, gern! / Ich komme gern. / Vielen Dank für die Einladung. Declining: Tut mir leid, ich kann leider nicht. / Da habe ich schon etwas vor (I already have plans).'),
        ('Fixer le rendez-vous : Wann treffen wir uns? (quand se retrouve-t-on ?) — Um acht vor dem Schloss. Soll ich etwas mitbringen? (dois-je apporter quelque chose ?).', 'Arranging to meet: Wann treffen wir uns? (when shall we meet?) — Um acht vor dem Schloss. Soll ich etwas mitbringen? (shall I bring something?).'),
      ], [
        D('einladen', 'einladen', ('inviter', 'to invite')),
        D('einladung', 'die Einladung', ('l’invitation', 'the invitation')),
        D('tut-mir-leid', 'Tut mir leid.', ('Je suis désolé·e.', 'I am sorry.')),
        D('sich-treffen', 'sich treffen', ('se retrouver, se rencontrer', 'to meet (each other)')),
        D('mitbringen', 'mitbringen', ('apporter (avec soi)', 'to bring along')),
        D('geschenk', 'das Geschenk', ('le cadeau', 'the present, the gift')),
        D('vorhaben', 'etwas vorhaben', ('avoir quelque chose de prévu', 'to have plans')),
        D('mitkommen', 'mitkommen', ('venir avec (quelqu’un)', 'to come along')),
      ], [
        x('Der König lädt alle Mädchen zum Ball ein.', 'Le roi invite toutes les jeunes filles au bal.', 'The king invites all the girls to the ball.'),
        x('Kommst du mit? — Tut mir leid, ich habe schon etwas vor.', 'Tu viens avec nous ? — Désolé, j’ai déjà quelque chose de prévu.', 'Are you coming along? — Sorry, I already have plans.'),
      ], [
        DC(ANSWER, [('Freundin', 'Ich mache am Samstag eine Party. Kommst du?')], ('Une amie t’invite samedi (tu acceptes).', 'A friend invites you on Saturday (you accept).'), ['Ja, gern! Soll ich etwas mitbringen?', 'Ja, ich habe gegangen.', 'Nein, ich bin ein Geschenk.'], 'Ja, gern! Soll ich etwas mitbringen?', ('On accepte avec Ja, gern!', 'You accept with Ja, gern!')),
        FB(COMPLETE, 'Vielen Dank für die ＿!', ['Einladung', 'Zeit', 'Woche'], 'Einladung', ('On remercie pour l’invitation : die Einladung.', 'You say thanks for the invitation: die Einladung.'), ('Merci beaucoup pour l’invitation !', 'Thank you very much for the invitation!')),
        FB(COMPLETE, 'Wann ＿ wir uns? — Um acht vor dem Schloss.', ['treffen', 'laden', 'bringen'], 'treffen', ('Se retrouver : sich treffen.', 'To meet: sich treffen.'), ('Quand se retrouve-t-on ? — À huit heures devant le château.', 'When shall we meet? — At eight in front of the castle.')),
        TF('Tut mir leid, ich kann leider nicht kommen.', ('La personne accepte l’invitation.', 'The person accepts the invitation.'), FAUX, ('Ich kann leider nicht = je ne peux malheureusement pas : c’est un refus.', 'Ich kann leider nicht = unfortunately I can’t: it is a refusal.')),
      ]),
  ])])

# ═════════════════════════ 3 : Le logement, où ? / vers où ?, le datif ═════════════════════════
W3 = WORLD('goethea2-w3', ('La tour de Raiponce', 'Rapunzel’s tower'), REGION,
  ('Décrire un logement et ses meubles, distinguer le lieu (datif) et la direction (accusatif), employer les prépositions toujours suivies du datif.', 'Describe a home and its furniture, tell location (dative) from direction (accusative), use the prepositions that always take the dative.'),
  (('Dame Gothel', 'Mother Gothel'), '♜', ('Dame Gothel a muré la porte de la tour : on n’y entre que par la fenêtre. Décris chaque pièce et dis où poser chaque meuble pour qu’elle te laisse monter jusqu’à Raiponce.', 'Mother Gothel has walled up the tower door: the only way in is the window. Describe each room and say where to put each piece of furniture so that she lets you climb up to Rapunzel.')),
  [CH('goethea2-w3-c1', ('Une chambre sous les toits', 'A room under the roof'), [
    L('de-wohnung', ('Le logement et les meubles', 'Home and furniture'), ('Décrire les pièces d’un logement et ce qui s’y trouve.', 'Describe the rooms of a home and what is in them.'), 8, [
        ('Les pièces : das Zimmer (la pièce, la chambre), das Wohnzimmer (le salon), das Schlafzimmer (la chambre à coucher), die Küche (la cuisine), das Bad (la salle de bains).', 'The rooms: das Zimmer (the room), das Wohnzimmer (the living room), das Schlafzimmer (the bedroom), die Küche (the kitchen), das Bad (the bathroom).'),
        ('Pour louer : die Wohnung (l’appartement), die Miete (le loyer), der Vermieter (le propriétaire). Die Wohnung ist 60 Quadratmeter groß und kostet 600 Euro warm (charges comprises).', 'To rent: die Wohnung (the flat), die Miete (the rent), der Vermieter (the landlord). Die Wohnung ist 60 Quadratmeter groß und kostet 600 Euro warm (bills included).'),
        ('Donner son avis : Die Wohnung ist hell (lumineuse), dunkel (sombre), ruhig (calme), laut (bruyante). Ich finde sie zu klein = je la trouve trop petite.', 'Giving an opinion: Die Wohnung ist hell (bright), dunkel (dark), ruhig (quiet), laut (noisy). Ich finde sie zu klein = I find it too small.'),
      ], [
        D('wohnung', 'die Wohnung', ('l’appartement', 'the flat, the apartment')),
        D('zimmer', 'das Zimmer', ('la pièce, la chambre', 'the room')),
        D('kueche', 'die Küche', ('la cuisine (pièce)', 'the kitchen')),
        D('bad', 'das Bad', ('la salle de bains', 'the bathroom')),
        D('miete', 'die Miete', ('le loyer', 'the rent')),
        D('tisch', 'der Tisch', ('la table', 'the table')),
        D('bett', 'das Bett', ('le lit', 'the bed')),
        D('fenster', 'das Fenster', ('la fenêtre', 'the window')),
        D('hell-dunkel', 'hell / dunkel', ('clair / sombre', 'bright / dark')),
      ], [
        x('Rapunzels Zimmer ist klein, aber hell: Es hat nur ein Fenster.', 'La chambre de Raiponce est petite mais lumineuse : elle n’a qu’une fenêtre.', 'Rapunzel’s room is small but bright: it has only one window.'),
        x('Die Wohnung hat zwei Zimmer, eine Küche und ein Bad. Die Miete ist nicht teuer.', 'L’appartement a deux pièces, une cuisine et une salle de bains. Le loyer n’est pas cher.', 'The flat has two rooms, a kitchen and a bathroom. The rent is not expensive.'),
      ], [
        FB(COMPLETE, 'Wir kochen in der ＿.', ['Küche', 'Miete', 'Wohnung'], 'Küche', ('On cuisine dans la cuisine : die Küche.', 'You cook in the kitchen: die Küche.'), ('Nous cuisinons dans la cuisine.', 'We cook in the kitchen.')),
        FB(COMPLETE, 'Die ＿ kostet 600 Euro im Monat.', ['Miete', 'Küche', 'Tisch'], 'Miete', ('Ce qu’on paie chaque mois : die Miete.', 'What you pay every month: die Miete.'), ('Le loyer coûte 600 euros par mois.', 'The rent is 600 euros a month.')),
        TF('Das Zimmer ist dunkel.', ('La pièce est lumineuse.', 'The room is bright.'), FAUX, ('Dunkel = sombre, le contraire de hell.', 'Dunkel = dark, the opposite of hell.')),
        DC(ANSWER, [('Vermieter', 'Wie finden Sie die Wohnung?')], ('Le propriétaire demande ton avis (tu la trouves belle mais trop petite).', 'The landlord asks your opinion (you find it nice but too small).'), ['Sie ist schön, aber zu klein.', 'Sie hat schön, aber klein.', 'Ich bin die Wohnung.'], 'Sie ist schön, aber zu klein.', ('Avis : sie ist + adjectif ; zu = trop.', 'Opinion: sie ist + adjective; zu = too.')),
      ]),
    L('de-wechsel', ('Où ? ou vers où ? Les prépositions mixtes', 'Where or where to? Two-way prepositions'), ('Dire où se trouve un objet et où on le pose.', 'Say where an object is and where you put it.'), 9, [
        ('Neuf prépositions changent de cas : in, an, auf, über, unter, vor, hinter, neben, zwischen. Lieu (wo ?) → datif ; direction (wohin ?) → accusatif.', 'Nine prepositions change case: in, an, auf, über, unter, vor, hinter, neben, zwischen. Location (wo?) → dative; direction (wohin?) → accusative.'),
        ('Das Buch liegt auf dem Tisch (où ? datif). Ich lege das Buch auf den Tisch (vers où ? accusatif). Rappel : dem → masculin et neutre, der → féminin au datif.', 'Das Buch liegt auf dem Tisch (where? dative). Ich lege das Buch auf den Tisch (where to? accusative). Reminder: dem → masculine and neuter, der → feminine in the dative.'),
        ('Les verbes vont par paires : liegen / legen (être posé / poser à plat), stehen / stellen (être debout / poser debout), hängen (être accroché / accrocher).', 'Verbs come in pairs: liegen / legen (to lie / to lay), stehen / stellen (to stand / to put upright), hängen (to hang).'),
      ], [
        DG('wechselpraep', 'Wo? + Dativ / Wohin? + Akkusativ', ('lieu au datif / direction à l’accusatif', 'location in the dative / direction in the accusative')),
        D('auf', 'auf', ('sur (posé dessus)', 'on (top of)')),
        D('unter', 'unter', ('sous', 'under')),
        D('vor-ort', 'vor', ('devant', 'in front of')),
        D('hinter', 'hinter', ('derrière', 'behind')),
        D('zwischen', 'zwischen', ('entre', 'between')),
        D('legen-liegen', 'legen / liegen', ('poser à plat / être posé', 'to lay / to lie')),
        D('stellen-stehen', 'stellen / stehen', ('poser debout / être debout', 'to put (upright) / to stand')),
      ], [
        x('Der Prinz steht vor dem Turm. Rapunzel lässt ihr Haar aus dem Fenster.', 'Le prince est devant la tour. Raiponce laisse tomber ses cheveux par la fenêtre.', 'The prince is standing in front of the tower. Rapunzel lets her hair down from the window.'),
        x('Stell die Lampe auf den Tisch! — Sie steht schon auf dem Tisch.', 'Pose la lampe sur la table ! — Elle est déjà sur la table.', 'Put the lamp on the table! — It is already on the table.'),
      ], [
        FB(CHOOSE, 'Das Buch liegt auf ＿ Tisch.', ['dem', 'den', 'der'], 'dem', ('Où ? → datif : auf dem Tisch.', 'Where? → dative: auf dem Tisch.'), ('Le livre est sur la table.', 'The book is on the table.')),
        FB(CHOOSE, 'Ich lege das Buch auf ＿ Tisch.', ['den', 'dem', 'das'], 'den', ('Vers où ? → accusatif : auf den Tisch.', 'Where to? → accusative: auf den Tisch.'), ('Je pose le livre sur la table.', 'I put the book on the table.')),
        FB(CHOOSE, 'Die Katze schläft unter ＿ Bett.', ['dem', 'das', 'den'], 'dem', ('Où ? → datif ; das Bett → dem Bett.', 'Where? → dative; das Bett → dem Bett.'), ('Le chat dort sous le lit.', 'The cat is sleeping under the bed.')),
        FB(CHOOSE, 'Wir gehen in ＿ Küche.', ['die', 'der', 'dem'], 'die', ('Direction → accusatif : in die Küche.', 'Direction → accusative: in die Küche.'), ('Nous allons dans la cuisine.', 'We are going into the kitchen.')),
      ]),
  ]),
  CH('goethea2-w3-c2', ('Par la fenêtre', 'Through the window'), [
    L('de-dativ-praep', ('Les prépositions toujours suivies du datif', 'Prepositions that always take the dative'), ('Employer mit, bei, von, zu, aus, nach et seit avec le bon article.', 'Use mit, bei, von, zu, aus, nach and seit with the right article.'), 8, [
        ('Toujours le datif après : aus (hors de, originaire de), bei (chez, près de), mit (avec), nach (après, vers), seit (depuis), von (de), zu (chez, vers).', 'Always the dative after: aus (out of, from), bei (at someone’s, near), mit (with), nach (after, to), seit (since), von (from, of), zu (to).'),
        ('Les articles au datif : dem (masculin, neutre), der (féminin), den + -n (pluriel). Mit dem Bus, mit der Bahn, mit den Kindern. Contractions : zum, zur, vom, beim.', 'Dative articles: dem (masculine, neuter), der (feminine), den + -n (plural). Mit dem Bus, mit der Bahn, mit den Kindern. Contractions: zum, zur, vom, beim.'),
        ('Bei = chez quelqu’un, sans mouvement : Ich wohne bei meinen Eltern. Zu = chez quelqu’un, avec mouvement : Ich gehe zu meinen Eltern. Pour les villes et pays : nach Berlin.', 'Bei = at someone’s, no movement: Ich wohne bei meinen Eltern. Zu = to someone’s, with movement: Ich gehe zu meinen Eltern. For towns and countries: nach Berlin.'),
      ], [
        DG('dativ-praep', 'aus, bei, mit, nach, seit, von, zu + Dativ', ('prépositions suivies du datif', 'prepositions followed by the dative')),
        D('mit', 'mit', ('avec', 'with')),
        D('bei', 'bei', ('chez, près de (sans mouvement)', 'at (someone’s), near')),
        D('von', 'von', ('de (provenance, appartenance)', 'from, of')),
        D('zu-prep', 'zu', ('chez, vers (avec mouvement)', 'to (a person, a place)')),
        D('nach-ort', 'nach', ('vers (ville, pays) ; après', 'to (town, country); after')),
        D('turm', 'der Turm', ('la tour', 'the tower')),
        D('haar', 'das Haar', ('le cheveu, la chevelure', 'the hair (single hair, head of hair)')),
      ], [
        x('Rapunzel wohnt bei Frau Gothel in einem Turm.', 'Raiponce habite chez Dame Gothel, dans une tour.', 'Rapunzel lives with Mother Gothel in a tower.'),
        x('Der Prinz kommt mit dem Pferd und geht zum Turm.', 'Le prince arrive à cheval et va vers la tour.', 'The prince comes on horseback and goes to the tower.'),
      ], [
        FB(CHOOSE, 'Ich fahre mit ＿ Bus zur Arbeit.', ['dem', 'den', 'der'], 'dem', ('Mit + datif ; der Bus → dem Bus.', 'Mit + dative; der Bus → dem Bus.'), ('Je vais au travail en bus.', 'I go to work by bus.')),
        FB(CHOOSE, 'Sie wohnt ＿ ihren Eltern.', ['bei', 'zu', 'nach'], 'bei', ('Chez quelqu’un, sans mouvement : bei.', 'At someone’s, no movement: bei.'), ('Elle habite chez ses parents.', 'She lives with her parents.')),
        FB(CHOOSE, 'Am Sonntag fahren wir ＿ Heidelberg.', ['nach', 'zu', 'bei'], 'nach', ('Vers une ville : nach.', 'To a town: nach.'), ('Dimanche, nous allons à Heidelberg.', 'On Sunday we are going to Heidelberg.')),
        order(('Remets dans l’ordre : « Je vais chez le médecin. »', 'Put in order: “I am going to the doctor’s.”'), ['Ich', 'gehe', 'zum', 'Arzt.'], ('Mouvement vers une personne : zu + dem = zum.', 'Movement towards a person: zu + dem = zum.')),
      ]),
  ])])

# ═════════════════════════ 4 : Comparer, décrire avec l'adjectif ═════════════════════════
W4 = WORLD('goethea2-w4', ('Le miroir de la Reine', 'The Queen’s mirror'), REGION,
  ('Comparer avec le comparatif et le superlatif, accorder l’adjectif devant le nom, demander lequel avec welcher.', 'Compare with the comparative and the superlative, decline the adjective before a noun, ask which one with welcher.'),
  (('La Reine au miroir', 'The Queen with the mirror'), '♕', ('« Miroir, miroir au mur… » La Reine veut savoir qui est la plus belle, la plus grande, la plus rapide. Compare sans te tromper : son miroir ne ment jamais, et elle déteste les fautes de grammaire.', '“Mirror, mirror on the wall…” The Queen wants to know who is the fairest, the tallest, the fastest. Compare without a slip: her mirror never lies, and she hates grammar mistakes.')),
  [CH('goethea2-w4-c1', ('Miroir, miroir', 'Mirror, mirror'), [
    L('de-komparativ', ('Le comparatif : -er als', 'The comparative: -er als'), ('Comparer deux personnes ou deux choses.', 'Compare two people or two things.'), 8, [
        ('Comparatif : adjectif + -er, puis als (que). klein → kleiner, schön → schöner. Schneewittchen ist schöner als die Königin.', 'Comparative: adjective + -er, then als (than). klein → kleiner, schön → schöner. Schneewittchen ist schöner als die Königin.'),
        ('Les adjectifs courts en a, o, u prennent souvent le tréma : alt → älter, groß → größer, jung → jünger, kalt → kälter, warm → wärmer.', 'Short adjectives in a, o, u often take an umlaut: alt → älter, groß → größer, jung → jünger, kalt → kälter, warm → wärmer.'),
        ('Irréguliers : gut → besser, viel → mehr, gern → lieber, hoch → höher. Égalité : so… wie (aussi… que). Er ist so groß wie ich.', 'Irregular: gut → besser, viel → mehr, gern → lieber, hoch → höher. Equality: so… wie (as… as). Er ist so groß wie ich.'),
      ], [
        DG('komparativ', 'Adjektiv + -er als', ('plus… que', 'more… than (-er than)')),
        DG('so-wie', 'so … wie', ('aussi… que', 'as… as')),
        D('aelter', 'alt → älter', ('vieux → plus vieux', 'old → older')),
        D('groesser', 'groß → größer', ('grand → plus grand', 'big → bigger')),
        D('besser', 'gut → besser', ('bon → meilleur', 'good → better')),
        D('mehr', 'viel → mehr', ('beaucoup → plus', 'much → more')),
        D('spiegel', 'der Spiegel', ('le miroir', 'the mirror')),
        D('koenigin', 'die Königin', ('la reine', 'the queen')),
      ], [
        x('Schneewittchen ist jünger und schöner als die Königin.', 'Blanche-Neige est plus jeune et plus belle que la reine.', 'Snow White is younger and more beautiful than the queen.'),
        x('Der Jäger ist so groß wie der König.', 'Le chasseur est aussi grand que le roi.', 'The huntsman is as tall as the king.'),
      ], [
        FB(CHOOSE, 'Mein Bruder ist ＿ als ich.', ['älter', 'alter', 'am ältesten'], 'älter', ('Alt → älter, avec tréma.', 'Alt → älter, with an umlaut.'), ('Mon frère est plus âgé que moi.', 'My brother is older than me.')),
        FB(CHOOSE, 'Dieser Kuchen schmeckt ＿ als der Apfel.', ['besser', 'guter', 'mehr gut'], 'besser', ('Gut → besser (irrégulier).', 'Gut → besser (irregular).'), ('Ce gâteau est meilleur que la pomme.', 'This cake tastes better than the apple.')),
        FB(CHOOSE, 'Sie ist so schön ＿ ihre Mutter.', ['wie', 'als', 'von'], 'wie', ('Égalité : so… wie.', 'Equality: so… wie.'), ('Elle est aussi belle que sa mère.', 'She is as beautiful as her mother.')),
        TF('Die Zwerge sind kleiner als Schneewittchen.', ('Les nains sont plus grands que Blanche-Neige.', 'The dwarfs are taller than Snow White.'), FAUX, ('Kleiner = plus petits.', 'Kleiner = smaller.')),
      ]),
    L('de-superlativ', ('Le superlatif : am -sten', 'The superlative: am -sten'), ('Dire qui est le plus… de tous.', 'Say who is the most… of all.'), 8, [
        ('Superlatif après un verbe : am + adjectif + -sten. schnell → am schnellsten, schön → am schönsten. Après -t, -d, -s, -ß, -z : -esten (alt → am ältesten).', 'Superlative after a verb: am + adjective + -sten. schnell → am schnellsten, schön → am schönsten. After -t, -d, -s, -ß, -z: -esten (alt → am ältesten).'),
        ('Devant un nom : der / die / das + adjectif + -ste. Die schönste Frau im ganzen Land (la plus belle femme de tout le pays).', 'Before a noun: der / die / das + adjective + -ste. Die schönste Frau im ganzen Land (the fairest woman in all the land).'),
        ('Irréguliers : gut → am besten, viel → am meisten, gern → am liebsten, groß → am größten, hoch → am höchsten. Am liebsten esse ich Kuchen = ce que je préfère, c’est le gâteau.', 'Irregular: gut → am besten, viel → am meisten, gern → am liebsten, groß → am größten, hoch → am höchsten. Am liebsten esse ich Kuchen = what I like best is cake.'),
      ], [
        DG('superlativ', 'am + Adjektiv + -sten', ('le plus… (superlatif)', 'the most… (superlative)')),
        D('am-besten', 'am besten', ('le mieux', 'best')),
        D('am-liebsten', 'am liebsten', ('de préférence (ce que j’aime le plus)', 'most of all, best (liking)')),
        D('am-meisten', 'am meisten', ('le plus (quantité)', 'the most')),
        D('die-schoenste', 'die Schönste', ('la plus belle', 'the fairest, the most beautiful one')),
        D('land', 'das Land', ('le pays', 'the country, the land')),
        D('wer', 'Wer?', ('Qui ?', 'Who?')),
        D('ganz', 'ganz', ('tout entier ; tout à fait', 'whole; quite')),
      ], [
        x('Spieglein, Spieglein an der Wand, wer ist die Schönste im ganzen Land?', 'Miroir, petit miroir au mur, qui est la plus belle de tout le pays ?', 'Mirror, mirror on the wall, who is the fairest in all the land?'),
        x('Von allen Zwergen läuft der jüngste am schnellsten.', 'De tous les nains, c’est le plus jeune qui court le plus vite.', 'Of all the dwarfs, the youngest runs the fastest.'),
      ], [
        FB(CHOOSE, 'Wer läuft am ＿?', ['schnellsten', 'schneller', 'schnell'], 'schnellsten', ('Superlatif : am schnellsten.', 'Superlative: am schnellsten.'), ('Qui court le plus vite ?', 'Who runs the fastest?')),
        FB(CHOOSE, 'Am ＿ trinke ich Tee.', ['liebsten', 'lieber', 'gern'], 'liebsten', ('Gern → lieber → am liebsten.', 'Gern → lieber → am liebsten.'), ('Ce que je préfère boire, c’est le thé.', 'I like drinking tea best.')),
        FB(CHOOSE, 'Sie ist die ＿ Frau im Land.', ['schönste', 'schöner', 'am schönsten'], 'schönste', ('Devant un nom : die schönste Frau.', 'Before a noun: die schönste Frau.'), ('Elle est la plus belle femme du pays.', 'She is the most beautiful woman in the land.')),
        DC(ANSWER, [('Königin', 'Wer ist die Schönste im ganzen Land?')], ('La Reine interroge son miroir (réponds comme lui : Blanche-Neige).', 'The Queen questions her mirror (answer as it does: Snow White).'), ['Schneewittchen ist die Schönste.', 'Schneewittchen ist schöner.', 'Schneewittchen ist am schön.'], 'Schneewittchen ist die Schönste.', ('Superlatif devant un nom sous-entendu : die Schönste.', 'Superlative before an implied noun: die Schönste.')),
      ]),
  ]),
  CH('goethea2-w4-c2', ('La pomme rouge', 'The red apple'), [
    L('de-adjektiv', ('L’adjectif devant le nom', 'The adjective before a noun'), ('Accorder l’adjectif épithète après ein et après der.', 'Decline the attributive adjective after ein and after der.'), 9, [
        ('Après sein, l’adjectif ne change pas (Der Apfel ist rot). Devant un nom, il prend une terminaison : der rote Apfel, ein roter Apfel.', 'After sein the adjective does not change (Der Apfel ist rot). Before a noun it takes an ending: der rote Apfel, ein roter Apfel.'),
        ('Après ein (nominatif) : l’adjectif montre le genre. ein roter Apfel (der), eine rote Blume (die), ein rotes Kleid (das). Après der, die, das : toujours -e (der rote Apfel, die rote Blume, das rote Kleid).', 'After ein (nominative): the adjective shows the gender. ein roter Apfel (der), eine rote Blume (die), ein rotes Kleid (das). After der, die, das: always -e (der rote Apfel, die rote Blume, das rote Kleid).'),
        ('À l’accusatif masculin, tout prend -en : Ich esse einen roten Apfel / den roten Apfel. Au pluriel après die : -en (die roten Äpfel). Welcher Apfel? = quelle pomme ? — Dieser hier (celle-ci).', 'In the masculine accusative everything takes -en: Ich esse einen roten Apfel / den roten Apfel. In the plural after die: -en (die roten Äpfel). Welcher Apfel? = which apple? — Dieser hier (this one).'),
      ], [
        DG('adj-ein', 'ein roter / eine rote / ein rotes', ('adjectif après ein (nominatif)', 'adjective after ein (nominative)')),
        DG('adj-der', 'der / die / das rote …', ('adjectif après der, die, das (nominatif)', 'adjective after der, die, das (nominative)')),
        DG('adj-akk-m', 'einen roten / den roten', ('adjectif à l’accusatif masculin', 'adjective in the masculine accusative')),
        DG('welcher', 'welcher / welche / welches', ('quel / quelle (lequel ?)', 'which (one)')),
        DG('dieser', 'dieser / diese / dieses', ('ce / cette (celui-ci)', 'this (one)')),
        D('kleid', 'das Kleid', ('la robe', 'the dress')),
        D('blume', 'die Blume', ('la fleur', 'the flower')),
        D('neu', 'neu', ('nouveau, neuf', 'new')),
      ], [
        x('Die Königin bringt einen schönen roten Apfel.', 'La reine apporte une belle pomme rouge.', 'The queen brings a beautiful red apple.'),
        x('Welches Kleid möchtest du? — Dieses neue Kleid hier.', 'Quelle robe voudrais-tu ? — Cette nouvelle robe-ci.', 'Which dress would you like? — This new dress here.'),
      ], [
        FB(CHOOSE, 'Das ist ein ＿ Apfel.', ['roter', 'rote', 'rotes'], 'roter', ('Der Apfel, après ein : -er.', 'Der Apfel, after ein: -er.'), ('C’est une pomme rouge.', 'That is a red apple.')),
        FB(CHOOSE, 'Sie trägt ein ＿ Kleid.', ['neues', 'neuer', 'neue'], 'neues', ('Das Kleid, après ein : -es.', 'Das Kleid, after ein: -es.'), ('Elle porte une robe neuve.', 'She is wearing a new dress.')),
        FB(CHOOSE, 'Ich esse den ＿ Apfel nicht!', ['roten', 'rote', 'roter'], 'roten', ('Accusatif masculin : den roten Apfel.', 'Masculine accusative: den roten Apfel.'), ('Je ne mange pas la pomme rouge !', 'I am not eating the red apple!')),
        FB(CHOOSE, '＿ Blume gefällt dir? — Die rote.', ['Welche', 'Welcher', 'Welches'], 'Welche', ('Die Blume est féminin : welche.', 'Die Blume is feminine: welche.'), ('Quelle fleur te plaît ? — La rouge.', 'Which flower do you like? — The red one.')),
      ]),
  ])])

# ═════════════════════════ 5 : Le travail, weil, dass ═════════════════════════
W5 = WORLD('goethea2-w5', ('Le chemin de Jean le Chanceux', 'Lucky Hans’s road'), REGION,
  ('Parler de son métier et de sa journée de travail, donner une raison avec weil et rapporter une opinion avec dass.', 'Talk about your job and working day, give a reason with weil and report an opinion with dass.'),
  (('Jean le Chanceux', 'Lucky Hans'), '☘', ('Après sept ans de travail, Jean le Chanceux échange son or contre un cheval, puis une vache, puis une oie… et se dit toujours plus heureux. Demande-lui pourquoi : il ne répond qu’aux phrases où le verbe est à la bonne place.', 'After seven years’ work, Lucky Hans swaps his gold for a horse, then a cow, then a goose… and says he is happier each time. Ask him why: he only answers sentences where the verb is in the right place.')),
  [CH('goethea2-w5-c1', ('Sept ans de travail', 'Seven years’ work'), [
    L('de-beruf', ('Les métiers et le travail', 'Jobs and work'), ('Dire ce qu’on fait dans la vie et décrire son travail.', 'Say what you do for a living and describe your work.'), 8, [
        ('Was sind Sie von Beruf? = quel est votre métier ? On répond sans article : Ich bin Lehrer / Lehrerin. Le féminin se forme en -in : der Arzt → die Ärztin, der Koch → die Köchin.', 'Was sind Sie von Beruf? = what is your job? The answer has no article: Ich bin Lehrer / Lehrerin. The feminine is formed with -in: der Arzt → die Ärztin, der Koch → die Köchin.'),
        ('Ich arbeite als Verkäuferin (comme vendeuse) bei einer Firma (dans une entreprise), in einem Büro (dans un bureau). Ich arbeite Vollzeit / Teilzeit.', 'Ich arbeite als Verkäuferin (as a shop assistant) bei einer Firma (for a company), in einem Büro (in an office). Ich arbeite Vollzeit / Teilzeit.'),
        ('Der Chef / die Chefin (le / la responsable), der Kollege / die Kollegin (le / la collègue), das Gehalt (le salaire), der Urlaub (les congés). Ich habe frei = je suis en congé.', 'Der Chef / die Chefin (the boss), der Kollege / die Kollegin (the colleague), das Gehalt (the salary), der Urlaub (holiday leave). Ich habe frei = I have time off.'),
      ], [
        D('beruf', 'der Beruf', ('le métier', 'the job, the profession')),
        D('von-beruf', 'Was sind Sie von Beruf?', ('Quel est votre métier ?', 'What is your job?')),
        D('lehrer', 'der Lehrer / die Lehrerin', ('le professeur / la professeure', 'the teacher (man / woman)')),
        D('verkaeufer', 'der Verkäufer / die Verkäuferin', ('le vendeur / la vendeuse', 'the shop assistant (man / woman)')),
        D('firma', 'die Firma', ('l’entreprise', 'the company')),
        D('buero', 'das Büro', ('le bureau (lieu de travail)', 'the office')),
        D('kollege', 'der Kollege / die Kollegin', ('le / la collègue', 'the colleague (man / woman)')),
        D('urlaub', 'der Urlaub', ('les congés, les vacances', 'holiday leave')),
        D('arbeiten-als', 'arbeiten als …', ('travailler comme…', 'to work as…')),
      ], [
        x('Was sind Sie von Beruf? — Ich bin Koch. Ich arbeite in einem Gasthaus.', 'Quel est votre métier ? — Je suis cuisinier. Je travaille dans une auberge.', 'What do you do for a living? — I am a cook. I work in an inn.'),
        x('Hans hat sieben Jahre bei seinem Chef gearbeitet. Jetzt hat er Urlaub.', 'Jean a travaillé sept ans chez son patron. Maintenant, il est en congé.', 'Hans worked for his boss for seven years. Now he is on holiday.'),
      ], [
        FB(CHOOSE, 'Meine Schwester ist ＿.', ['Lehrerin', 'eine Lehrer', 'Lehrer'], 'Lehrerin', ('Métier sans article, au féminin : Lehrerin.', 'Job with no article, in the feminine: Lehrerin.'), ('Ma sœur est professeure.', 'My sister is a teacher.')),
        FB(COMPLETE, 'Er arbeitet ＿ Verkäufer.', ['als', 'wie', 'für'], 'als', ('Travailler comme : arbeiten als.', 'To work as: arbeiten als.'), ('Il travaille comme vendeur.', 'He works as a shop assistant.')),
        DC(ANSWER, [('Beamtin', 'Was sind Sie von Beruf?')], ('On te demande ton métier (tu es cuisinier ou cuisinière).', 'You are asked your job (you are a cook).'), ['Ich bin Koch.', 'Ich habe Koch.', 'Ich bin ein Büro.'], 'Ich bin Koch.', ('Ich bin + métier, sans article.', 'Ich bin + job, with no article.')),
        TF('Im August habe ich drei Wochen Urlaub.', ('La personne travaille tout le mois d’août.', 'The person works all through August.'), FAUX, ('Urlaub = congés.', 'Urlaub = holiday leave.')),
      ]),
    L('de-weil', ('Donner une raison : weil', 'Giving a reason: weil'), ('Expliquer pourquoi, avec le verbe à la fin de la subordonnée.', 'Explain why, with the verb at the end of the subordinate clause.'), 9, [
        ('Warum? (pourquoi ?) — Weil… (parce que…). Après weil, le verbe conjugué va à la fin : Ich bleibe zu Hause, weil ich krank bin.', 'Warum? (why?) — Weil… (because…). After weil, the conjugated verb goes to the end: Ich bleibe zu Hause, weil ich krank bin.'),
        ('Avec un Perfekt ou un verbe de modalité, c’est l’auxiliaire conjugué qui ferme la phrase : … weil ich lange gearbeitet habe ; … weil ich arbeiten muss.', 'With a Perfekt or a modal verb, the conjugated auxiliary closes the clause: … weil ich lange gearbeitet habe; … weil ich arbeiten muss.'),
        ('Denn (car) donne aussi la raison, mais sans changer l’ordre des mots : Ich bleibe zu Hause, denn ich bin krank. Une virgule sépare toujours les deux propositions.', 'Denn (for, because) also gives the reason, but without changing the word order: Ich bleibe zu Hause, denn ich bin krank. A comma always separates the two clauses.'),
      ], [
        DG('weil', 'weil + Verb am Ende', ('parce que (verbe à la fin)', 'because (verb at the end)')),
        DG('denn', 'denn', ('car', 'for, because (no change of word order)')),
        D('warum', 'Warum?', ('Pourquoi ?', 'Why?')),
        D('gluecklich', 'glücklich', ('heureux', 'happy')),
        D('schwer', 'schwer', ('lourd ; difficile', 'heavy; difficult')),
        D('leicht', 'leicht', ('léger ; facile', 'light; easy')),
        D('gold', 'das Gold', ('l’or', 'gold')),
        D('tauschen', 'tauschen', ('échanger', 'to swap, to exchange')),
      ], [
        x('Warum tauscht Hans sein Gold? — Weil es zu schwer ist.', 'Pourquoi Jean échange-t-il son or ? — Parce qu’il est trop lourd.', 'Why does Hans swap his gold? — Because it is too heavy.'),
        x('Er ist glücklich, weil er nichts mehr tragen muss.', 'Il est heureux parce qu’il n’a plus rien à porter.', 'He is happy because he no longer has to carry anything.'),
      ], [
        order(('Remets dans l’ordre : « … parce que je suis malade. »', 'Put in order: “… because I am ill.”'), ['weil', 'ich', 'krank', 'bin.'], ('Après weil, le verbe conjugué va à la fin.', 'After weil, the conjugated verb goes to the end.')),
        FB(CHOOSE, 'Ich lerne Deutsch, weil ich in Berlin arbeiten ＿.', ['will', 'wollen', 'gewollt'], 'will', ('Le verbe conjugué (will) ferme la subordonnée.', 'The conjugated verb (will) closes the subordinate clause.'), ('J’apprends l’allemand parce que je veux travailler à Berlin.', 'I am learning German because I want to work in Berlin.')),
        FB(CHOOSE, 'Er kommt nicht, ＿ er hat keine Zeit.', ['denn', 'weil', 'warum'], 'denn', ('Le verbe reste en deuxième position : c’est denn.', 'The verb stays in second position: so it is denn.'), ('Il ne vient pas, car il n’a pas le temps.', 'He isn’t coming, for he has no time.')),
        DC(ANSWER, [('Hans', 'Warum bist du so glücklich?')], ('Jean te demande pourquoi tu es si heureux (tu es en congé).', 'Hans asks why you are so happy (you are on holiday).'), ['Weil ich Urlaub habe.', 'Weil ich habe Urlaub.', 'Denn ich Urlaub habe.'], 'Weil ich Urlaub habe.', ('Weil + verbe à la fin : weil ich Urlaub habe.', 'Weil + verb at the end: weil ich Urlaub habe.')),
      ]),
  ]),
  CH('goethea2-w5-c2', ('De l’or contre une oie', 'Gold for a goose'), [
    L('de-dass', ('Dire ce qu’on pense : dass', 'Saying what you think: dass'), ('Donner son opinion et rapporter ce que quelqu’un dit.', 'Give your opinion and report what someone says.'), 8, [
        ('Dass (que) introduit une subordonnée, verbe à la fin : Ich glaube, dass er recht hat (je crois qu’il a raison). Ich finde, dass das Buch gut ist.', 'Dass (that) introduces a subordinate clause, verb at the end: Ich glaube, dass er recht hat (I think that he is right). Ich finde, dass das Buch gut ist.'),
        ('Pour rapporter : Er sagt, dass er müde ist (il dit qu’il est fatigué). Sie schreibt, dass sie morgen kommt.', 'To report: Er sagt, dass er müde ist (he says that he is tired). Sie schreibt, dass sie morgen kommt.'),
        ('Être d’accord ou non : Das stimmt (c’est vrai). Du hast recht (tu as raison). Das finde ich nicht (je ne trouve pas). Ich bin nicht sicher (je ne suis pas sûr).', 'Agreeing or not: Das stimmt (that’s true). Du hast recht (you are right). Das finde ich nicht (I don’t think so). Ich bin nicht sicher (I am not sure).'),
      ], [
        DG('dass', 'dass + Verb am Ende', ('que (verbe à la fin)', 'that (verb at the end)')),
        D('glauben', 'glauben', ('croire', 'to believe, to think')),
        D('sagen', 'sagen', ('dire', 'to say')),
        D('finden-meinung', 'Ich finde, dass …', ('Je trouve que…', 'I find that…, I think that…')),
        D('recht-haben', 'recht haben', ('avoir raison', 'to be right')),
        D('das-stimmt', 'Das stimmt.', ('C’est vrai, c’est exact.', 'That’s true, that’s right.')),
        D('sicher', 'sicher', ('sûr, certain', 'sure, certain')),
        D('dumm', 'dumm', ('bête, stupide', 'stupid, silly')),
      ], [
        x('Die Leute sagen, dass Hans dumm ist. Aber Hans findet, dass er Glück hat.', 'Les gens disent que Jean est bête. Mais Jean trouve qu’il a de la chance.', 'People say that Hans is stupid. But Hans thinks that he is lucky.'),
        x('Ich glaube, dass du recht hast. — Ja, das stimmt.', 'Je crois que tu as raison. — Oui, c’est vrai.', 'I think that you are right. — Yes, that’s true.'),
      ], [
        order(('Remets dans l’ordre : « Je crois qu’il est heureux. »', 'Put in order: “I think that he is happy.”'), ['Ich', 'glaube,', 'dass', 'er', 'glücklich', 'ist.'], ('Après dass, le verbe conjugué va à la fin.', 'After dass, the conjugated verb goes to the end.')),
        FB(CHOOSE, 'Sie sagt, ＿ sie morgen kommt.', ['dass', 'weil', 'denn'], 'dass', ('Rapporter une parole : sagen, dass…', 'Reporting speech: sagen, dass…'), ('Elle dit qu’elle vient demain.', 'She says that she is coming tomorrow.')),
        FB(CHOOSE, 'Ich finde, dass der Film langweilig ＿.', ['ist', 'sein', 'bin'], 'ist', ('Le verbe conjugué ferme la subordonnée : … langweilig ist.', 'The conjugated verb closes the clause: … langweilig ist.'), ('Je trouve que le film est ennuyeux.', 'I find that the film is boring.')),
        TF('Du hast recht, das stimmt.', ('La personne n’est pas d’accord.', 'The person disagrees.'), FAUX, ('Du hast recht, das stimmt = tu as raison, c’est vrai.', 'Du hast recht, das stimmt = you are right, that’s true.')),
      ]),
  ])])

# ═════════════════════════ 6 : Voyager, wenn, les pronoms au datif ═════════════════════════
W6 = WORLD('goethea2-w6', ('Les routes du Chat botté', 'Puss in Boots’ roads'), REGION,
  ('Voyager en train et à l’hôtel, exprimer une condition avec wenn, employer les pronoms au datif avec geben, helfen et gefallen.', 'Travel by train and stay in a hotel, express a condition with wenn, use dative pronouns with geben, helfen and gefallen.'),
  (('Le Chat botté', 'Puss in Boots'), '♞', ('Bottes aux pattes et sac sur l’épaule, le Chat botté court les routes pour faire la fortune de son maître. Il te mènera au château… si tu sais prendre un billet, réserver une chambre et dire à qui tu donnes quoi.', 'Boots on his paws and a sack on his shoulder, Puss in Boots roams the roads to make his master’s fortune. He will lead you to the castle… if you can buy a ticket, book a room and say who you give what to.')),
  [CH('goethea2-w6-c1', ('En route', 'On the road'), [
    L('de-reise', ('Voyager : le train et l’hôtel', 'Travelling: train and hotel'), ('Acheter un billet, comprendre une annonce de gare et réserver une chambre.', 'Buy a ticket, understand a station announcement and book a room.'), 8, [
        ('À la gare : die Fahrkarte (le billet), einfach (aller simple) / hin und zurück (aller-retour), das Gleis (la voie), die Abfahrt (le départ), die Ankunft (l’arrivée), umsteigen (changer de train).', 'At the station: die Fahrkarte (the ticket), einfach (single) / hin und zurück (return), das Gleis (the platform), die Abfahrt (departure), die Ankunft (arrival), umsteigen (to change trains).'),
        ('Annonces : Der Zug hat zehn Minuten Verspätung (dix minutes de retard). Der Zug fällt aus (le train est supprimé). Bitte einsteigen! (en voiture !).', 'Announcements: Der Zug hat zehn Minuten Verspätung (ten minutes late). Der Zug fällt aus (the train is cancelled). Bitte einsteigen! (all aboard!).'),
        ('À l’hôtel : Ich habe ein Zimmer reserviert. Ein Einzelzimmer / Doppelzimmer für zwei Nächte, mit Frühstück. Wo ist der Schlüssel?', 'At the hotel: Ich habe ein Zimmer reserviert. Ein Einzelzimmer / Doppelzimmer für zwei Nächte, mit Frühstück. Wo ist der Schlüssel?'),
      ], [
        D('zug', 'der Zug', ('le train', 'the train')),
        D('fahrkarte', 'die Fahrkarte', ('le billet (de train, de bus)', 'the ticket (train, bus)')),
        D('gleis', 'das Gleis', ('la voie, le quai', 'the platform, the track')),
        D('verspaetung', 'die Verspätung', ('le retard', 'the delay')),
        D('umsteigen', 'umsteigen', ('changer (de train, de bus)', 'to change (trains, buses)')),
        D('hin-und-zurueck', 'hin und zurück', ('aller-retour', 'return (ticket), there and back')),
        D('reservieren', 'reservieren', ('réserver', 'to book, to reserve')),
        D('schluessel', 'der Schlüssel', ('la clé', 'the key')),
        D('koffer', 'der Koffer', ('la valise', 'the suitcase')),
      ], [
        x('Eine Fahrkarte nach Freiburg, hin und zurück, bitte. — Der Zug fährt von Gleis drei.', 'Un billet pour Fribourg, aller-retour, s’il vous plaît. — Le train part de la voie trois.', 'A return ticket to Freiburg, please. — The train leaves from platform three.'),
        x('Der Zug hat Verspätung. Wir müssen in Karlsruhe umsteigen.', 'Le train a du retard. Nous devons changer à Karlsruhe.', 'The train is late. We have to change in Karlsruhe.'),
      ], [
        FB(COMPLETE, 'Der Zug nach Basel fährt von ＿ fünf.', ['Gleis', 'Koffer', 'Schlüssel'], 'Gleis', ('La voie : das Gleis.', 'The platform: das Gleis.'), ('Le train pour Bâle part de la voie cinq.', 'The train to Basel leaves from platform five.')),
        FB(COMPLETE, 'Der Zug kommt später: Er hat zwanzig Minuten ＿.', ['Verspätung', 'Fahrkarte', 'Abfahrt'], 'Verspätung', ('Il arrive plus tard : Verspätung.', 'It arrives later: Verspätung.'), ('Le train arrive plus tard : il a vingt minutes de retard.', 'The train is coming later: it is twenty minutes late.')),
        DC(ANSWER, [('Hotel', 'Guten Abend! Kann ich Ihnen helfen?')], ('À la réception, tu as réservé une chambre.', 'At reception; you have booked a room.'), ['Ja, ich habe ein Zimmer reserviert.', 'Ja, ich bin ein Zimmer.', 'Nein, der Zug hat Verspätung.'], 'Ja, ich habe ein Zimmer reserviert.', ('Réserver : ich habe… reserviert.', 'To book: ich habe… reserviert.')),
        TF('Sie müssen in Mannheim umsteigen.', ('Le train est direct.', 'The train is direct.'), FAUX, ('Umsteigen = changer de train.', 'Umsteigen = to change trains.')),
      ]),
    L('de-wenn', ('Si, quand : wenn', 'If, when: wenn'), ('Exprimer une condition ou une habitude.', 'Express a condition or a habit.'), 8, [
        ('Wenn = si (condition) ou quand, chaque fois que (habitude). Le verbe va à la fin : Wenn ich Zeit habe, …', 'Wenn = if (condition) or when, whenever (habit). The verb goes to the end: Wenn ich Zeit habe, …'),
        ('Si la subordonnée est en tête, elle occupe la première place : le verbe de la principale vient juste après la virgule. Wenn es regnet, bleibe ich zu Hause.', 'If the subordinate clause comes first, it takes first position: the main verb comes right after the comma. Wenn es regnet, bleibe ich zu Hause.'),
        ('Ne pas confondre : wenn (si, chaque fois que), wann (quand ? dans une question) et als (quand, pour un moment unique du passé : Als ich klein war, …).', 'Do not confuse: wenn (if, whenever), wann (when? in a question) and als (when, for a single moment in the past: Als ich klein war, …).'),
      ], [
        DG('wenn', 'wenn + Verb am Ende', ('si, quand (verbe à la fin)', 'if, when (verb at the end)')),
        DG('nebensatz-vorn', 'Nebensatz, Verb + Subjekt', ('subordonnée en tête, puis verbe + sujet', 'subordinate clause first, then verb + subject')),
        DG('als-zeit', 'als (Vergangenheit)', ('quand (moment unique du passé)', 'when (a single moment in the past)')),
        D('vielleicht', 'vielleicht', ('peut-être', 'perhaps, maybe')),
        D('immer', 'immer', ('toujours', 'always')),
        D('manchmal', 'manchmal', ('parfois', 'sometimes')),
        D('nie', 'nie', ('jamais', 'never')),
        D('stiefel', 'der Stiefel', ('la botte', 'the boot')),
      ], [
        x('Wenn du mir Stiefel gibst, mache ich dich reich.', 'Si tu me donnes des bottes, je te rendrai riche.', 'If you give me boots, I will make you rich.'),
        x('Wenn der König kommt, läuft der Kater immer schnell zum Schloss.', 'Quand le roi arrive, le chat court toujours vite au château.', 'When the king comes, the cat always runs quickly to the castle.'),
      ], [
        order(('Remets dans l’ordre : « S’il pleut, je reste à la maison. »', 'Put in order: “If it rains, I stay at home.”'), ['Wenn', 'es', 'regnet,', 'bleibe', 'ich', 'zu', 'Hause.'], ('Subordonnée en tête : le verbe bleibe suit la virgule.', 'Subordinate clause first: the verb bleibe follows the comma.')),
        FB(CHOOSE, 'Wenn ich Zeit ＿, besuche ich dich.', ['habe', 'haben', 'gehabt'], 'habe', ('Après wenn, le verbe conjugué est à la fin de la subordonnée.', 'After wenn, the conjugated verb is at the end of the clause.'), ('Si j’ai le temps, je te rendrai visite.', 'If I have time, I will visit you.')),
        FB(CHOOSE, '＿ fährt der Zug ab? — Um neun Uhr.', ['Wann', 'Wenn', 'Als'], 'Wann', ('Question sur le moment : wann.', 'A question about time: wann.'), ('Quand part le train ? — À neuf heures.', 'When does the train leave? — At nine o’clock.')),
        FB(CHOOSE, '＿ ich klein war, hatte ich eine Katze.', ['Als', 'Wenn', 'Wann'], 'Als', ('Moment unique du passé : als.', 'A single moment in the past: als.'), ('Quand j’étais petit, j’avais un chat.', 'When I was little, I had a cat.')),
      ]),
  ]),
  CH('goethea2-w6-c2', ('Le marquis de Carabas', 'The Marquis of Carabas'), [
    L('de-pronomen-dativ', ('À qui ? Les pronoms au datif', 'To whom? Dative pronouns'), ('Dire à qui on donne, on montre ou on offre quelque chose.', 'Say who you give, show or offer something to.'), 9, [
        ('Les pronoms au datif : mir (à moi), dir (à toi), ihm (à lui), ihr (à elle), uns (à nous), euch (à vous), ihnen (à eux), Ihnen (à vous, poli).', 'Dative pronouns: mir (to me), dir (to you), ihm (to him), ihr (to her), uns (to us), euch (to you, plural), ihnen (to them), Ihnen (to you, polite).'),
        ('Verbes à deux compléments : la personne au datif, la chose à l’accusatif. Ich gebe dem König einen Fisch. Ich schenke ihm ein Buch. Kannst du mir den Weg zeigen?', 'Verbs with two objects: the person in the dative, the thing in the accusative. Ich gebe dem König einen Fisch. Ich schenke ihm ein Buch. Kannst du mir den Weg zeigen?'),
        ('Certains verbes demandent toujours le datif : helfen (Ich helfe dir), gefallen (Das gefällt mir = ça me plaît), gehören (Das gehört mir = c’est à moi), danken (Ich danke Ihnen).', 'Some verbs always take the dative: helfen (Ich helfe dir), gefallen (Das gefällt mir = I like that), gehören (Das gehört mir = that belongs to me), danken (Ich danke Ihnen).'),
      ], [
        DG('mir-dir', 'mir / dir / ihm / ihr', ('à moi / à toi / à lui / à elle', 'to me / to you / to him / to her')),
        DG('uns-euch', 'uns / euch / ihnen / Ihnen', ('à nous / à vous / à eux / à vous (poli)', 'to us / to you (plural) / to them / to you (polite)')),
        D('geben', 'geben', ('donner', 'to give')),
        D('schenken', 'schenken', ('offrir', 'to give (as a present)')),
        D('zeigen', 'zeigen', ('montrer', 'to show')),
        D('gefaellt-mir', 'Das gefällt mir.', ('Ça me plaît.', 'I like that.')),
        D('gehoeren', 'gehören', ('appartenir à', 'to belong to')),
        D('danken', 'danken', ('remercier', 'to thank')),
      ], [
        x('Der Kater schenkt dem König einen Hasen. Der König dankt ihm.', 'Le chat offre un lièvre au roi. Le roi le remercie.', 'The cat gives the king a hare. The king thanks him.'),
        x('Wem gehört das Schloss? — Es gehört meinem Herrn.', 'À qui appartient le château ? — Il appartient à mon maître.', 'Who does the castle belong to? — It belongs to my master.'),
      ], [
        FB(CHOOSE, 'Kannst du ＿ helfen? Ich finde den Weg nicht.', ['mir', 'mich', 'ich'], 'mir', ('Helfen demande le datif : mir.', 'Helfen takes the dative: mir.'), ('Peux-tu m’aider ? Je ne trouve pas le chemin.', 'Can you help me? I can’t find the way.')),
        FB(CHOOSE, 'Ich schenke ＿ ein Buch. Er liest gern.', ['ihm', 'ihn', 'er'], 'ihm', ('À lui : ihm (datif).', 'To him: ihm (dative).'), ('Je lui offre un livre. Il aime lire.', 'I am giving him a book. He likes reading.')),
        FB(CHOOSE, 'Die Stiefel gefallen ＿ sehr, Frau Müller?', ['Ihnen', 'Sie', 'dich'], 'Ihnen', ('Gefallen + datif ; forme polie : Ihnen.', 'Gefallen + dative; polite form: Ihnen.'), ('Les bottes vous plaisent beaucoup, madame Müller ?', 'Do you like the boots very much, Mrs Müller?')),
        DC(ANSWER, [('König', 'Wem gehört dieses Land?')], ('Le roi demande à qui est cette terre (à ton maître).', 'The king asks whose land this is (your master’s).'), ['Es gehört meinem Herrn.', 'Es gehört mein Herr.', 'Es gefällt mich.'], 'Es gehört meinem Herrn.', ('Gehören + datif : meinem Herrn.', 'Gehören + dative: meinem Herrn.')),
      ]),
  ])])

# ═════════════════════════ 7 : Les verbes pronominaux, la santé, les conseils ═════════════════════════
W7 = WORLD('goethea2-w7', ('L’auberge de l’Oie d’or', 'The Golden Goose inn'), REGION,
  ('Employer les verbes pronominaux, décrire ses symptômes chez le médecin et donner un conseil avec sollen.', 'Use reflexive verbs, describe your symptoms at the doctor’s and give advice with sollen.'),
  (('L’Oie d’or', 'The Golden Goose'), '♢', ('Quiconque touche l’Oie d’or y reste collé : l’aubergiste, ses filles, le curé… toute une file qui éternue et se plaint. Soigne chacun, donne les bons conseils, et fais enfin rire la princesse triste !', 'Whoever touches the Golden Goose sticks fast: the innkeeper, his daughters, the parson… a whole line of people sneezing and complaining. Look after each one, give the right advice, and make the sad princess laugh at last!')),
  [CH('goethea2-w7-c1', ('Tous collés !', 'All stuck together!'), [
    L('de-reflexiv', ('Les verbes pronominaux', 'Reflexive verbs'), ('Parler de sa toilette, de ses sentiments et de ses habitudes.', 'Talk about washing, feelings and habits.'), 8, [
        ('Le pronom réfléchi : ich … mich, du … dich, er / sie … sich, wir … uns, ihr … euch, sie / Sie … sich. Ich wasche mich. Er freut sich.', 'The reflexive pronoun: ich … mich, du … dich, er / sie … sich, wir … uns, ihr … euch, sie / Sie … sich. Ich wasche mich. Er freut sich.'),
        ('Le pronom suit le verbe conjugué : Ich ziehe mich an (je m’habille). Dans une question : Freust du dich?', 'The pronoun follows the conjugated verb: Ich ziehe mich an (I get dressed). In a question: Freust du dich?'),
        ('Verbes courants : sich waschen (se laver), sich anziehen (s’habiller), sich freuen (se réjouir), sich ärgern (s’énerver), sich setzen (s’asseoir), sich fühlen (se sentir).', 'Common verbs: sich waschen (to wash), sich anziehen (to get dressed), sich freuen (to be pleased), sich ärgern (to get annoyed), sich setzen (to sit down), sich fühlen (to feel).'),
      ], [
        DG('reflexiv', 'mich / dich / sich / uns / euch', ('me / te / se / nous / vous (réfléchi)', 'myself / yourself / himself, herself / ourselves / yourselves')),
        D('sich-waschen', 'sich waschen', ('se laver', 'to wash (oneself)')),
        D('sich-anziehen', 'sich anziehen', ('s’habiller', 'to get dressed')),
        D('sich-freuen', 'sich freuen', ('se réjouir, être content', 'to be pleased, to be glad')),
        D('sich-aergern', 'sich ärgern', ('s’énerver, se fâcher', 'to get annoyed')),
        D('sich-setzen', 'sich setzen', ('s’asseoir', 'to sit down, to take a seat')),
        D('sich-fuehlen', 'sich fühlen', ('se sentir', 'to feel (well, ill)')),
        D('lachen', 'lachen', ('rire', 'to laugh')),
      ], [
        x('Die Prinzessin lacht nie. Heute freut sie sich zum ersten Mal.', 'La princesse ne rit jamais. Aujourd’hui, elle se réjouit pour la première fois.', 'The princess never laughs. Today she is glad for the first time.'),
        x('Der Wirt ärgert sich, weil er an der Gans klebt.', 'L’aubergiste s’énerve parce qu’il est collé à l’oie.', 'The innkeeper is annoyed because he is stuck to the goose.'),
      ], [
        FB(CHOOSE, 'Ich wasche ＿ jeden Morgen.', ['mich', 'sich', 'dich'], 'mich', ('Avec ich : mich.', 'With ich: mich.'), ('Je me lave tous les matins.', 'I wash every morning.')),
        FB(CHOOSE, 'Er freut ＿ über das Geschenk.', ['sich', 'ihn', 'mich'], 'sich', ('Avec er / sie : sich.', 'With er / sie: sich.'), ('Il se réjouit du cadeau.', 'He is pleased with the present.')),
        order(('Remets dans l’ordre : « Comment te sens-tu aujourd’hui ? »', 'Put in order: “How do you feel today?”'), ['Wie', 'fühlst', 'du', 'dich', 'heute?'], ('Dans la question, le pronom réfléchi suit le sujet.', 'In a question, the reflexive pronoun follows the subject.')),
        TF('Sie ärgert sich über den Lärm.', ('Elle est contente du bruit.', 'She is happy about the noise.'), FAUX, ('Sich ärgern = s’énerver.', 'Sich ärgern = to get annoyed.')),
      ]),
    L('de-arzt', ('Chez le médecin', 'At the doctor’s'), ('Décrire ses symptômes, comprendre une ordonnance et prendre rendez-vous.', 'Describe your symptoms, understand a prescription and make an appointment.'), 8, [
        ('Les symptômes : Ich habe Fieber (de la fièvre), Husten (la toux), Schnupfen (le rhume), Halsschmerzen (mal à la gorge). Ich bin erkältet = je suis enrhumé.', 'Symptoms: Ich habe Fieber (a temperature), Husten (a cough), Schnupfen (a cold), Halsschmerzen (a sore throat). Ich bin erkältet = I have a cold.'),
        ('Le médecin prescrit : das Rezept (l’ordonnance), das Medikament (le médicament), die Tablette (le comprimé). Nehmen Sie dreimal täglich eine Tablette. On va les chercher à la Apotheke.', 'The doctor prescribes: das Rezept (the prescription), das Medikament (the medicine), die Tablette (the tablet). Nehmen Sie dreimal täglich eine Tablette. You collect them at the Apotheke.'),
        ('Prendre rendez-vous : Ich hätte gern einen Termin (je voudrais un rendez-vous). Geht es am Dienstag um zehn? En cas d’arrêt : die Krankschreibung.', 'Making an appointment: Ich hätte gern einen Termin (I would like an appointment). Geht es am Dienstag um zehn? If you are signed off work: die Krankschreibung.'),
      ], [
        D('fieber', 'das Fieber', ('la fièvre', 'the fever, the temperature')),
        D('husten', 'der Husten', ('la toux', 'the cough')),
        D('erkaeltet', 'erkältet sein', ('être enrhumé', 'to have a cold')),
        D('rezept', 'das Rezept', ('l’ordonnance ; la recette', 'the prescription; the recipe')),
        D('medikament', 'das Medikament', ('le médicament', 'the medicine')),
        D('tablette', 'die Tablette', ('le comprimé', 'the tablet, the pill')),
        D('termin', 'der Termin', ('le rendez-vous', 'the appointment')),
        D('apotheke', 'die Apotheke', ('la pharmacie', 'the pharmacy')),
        D('gesund', 'gesund', ('en bonne santé ; sain', 'healthy')),
      ], [
        x('Ich habe Fieber und Husten. — Hier ist ein Rezept. Gehen Sie zur Apotheke.', 'J’ai de la fièvre et je tousse. — Voici une ordonnance. Allez à la pharmacie.', 'I have a temperature and a cough. — Here is a prescription. Go to the pharmacy.'),
        x('Ich hätte gern einen Termin. — Geht es morgen um neun Uhr?', 'Je voudrais un rendez-vous. — Demain à neuf heures, ça va ?', 'I would like an appointment. — Is tomorrow at nine all right?'),
      ], [
        FB(COMPLETE, 'Mit dem Rezept gehe ich zur ＿.', ['Apotheke', 'Tablette', 'Husten'], 'Apotheke', ('Les médicaments se retirent à la pharmacie : die Apotheke.', 'Medicine is collected at the pharmacy: die Apotheke.'), ('Avec l’ordonnance, je vais à la pharmacie.', 'With the prescription I go to the pharmacy.')),
        FB(COMPLETE, 'Nehmen Sie dreimal täglich eine ＿.', ['Tablette', 'Apotheke', 'Termin'], 'Tablette', ('On prend un comprimé : die Tablette.', 'You take a tablet: die Tablette.'), ('Prenez un comprimé trois fois par jour.', 'Take one tablet three times a day.')),
        DC(ANSWER, [('Praxis', 'Praxis Doktor Weber, guten Tag!')], ('Tu appelles le cabinet pour prendre rendez-vous.', 'You call the surgery to make an appointment.'), ['Guten Tag, ich hätte gern einen Termin.', 'Guten Tag, ich bin ein Rezept.', 'Guten Tag, ich habe gesund.'], 'Guten Tag, ich hätte gern einen Termin.', ('Demander un rendez-vous : ich hätte gern einen Termin.', 'Asking for an appointment: ich hätte gern einen Termin.')),
        TF('Ich bin wieder gesund.', ('La personne est encore malade.', 'The person is still ill.'), FAUX, ('Wieder gesund = de nouveau en bonne santé.', 'Wieder gesund = healthy again.')),
      ]),
  ]),
  CH('goethea2-w7-c2', ('Le rire de la princesse', 'The princess’s laughter'), [
    L('de-sollen', ('Conseiller : sollen et l’impératif', 'Giving advice: sollen and the imperative'), ('Rapporter une consigne et donner un conseil.', 'Report an instruction and give advice.'), 8, [
        ('Sollen rapporte la consigne de quelqu’un d’autre : Der Arzt sagt, ich soll im Bett bleiben (le médecin dit que je dois rester au lit). ich soll, du sollst, er soll, wir sollen.', 'Sollen reports someone else’s instruction: Der Arzt sagt, ich soll im Bett bleiben (the doctor says I should stay in bed). ich soll, du sollst, er soll, wir sollen.'),
        ('Pour conseiller poliment : Du solltest… (tu devrais…). Du solltest mehr schlafen. Sie sollten weniger arbeiten.', 'For polite advice: Du solltest… (you should…). Du solltest mehr schlafen. Sie sollten weniger arbeiten.'),
        ('L’impératif à trois personnes : Trink viel Wasser! (du) / Trinkt viel Wasser! (ihr) / Trinken Sie viel Wasser! (Sie). Avec bitte ou mal, l’ordre devient aimable : Komm mal her!', 'The imperative in three persons: Trink viel Wasser! (du) / Trinkt viel Wasser! (ihr) / Trinken Sie viel Wasser! (Sie). With bitte or mal the order sounds friendlier: Komm mal her!'),
      ], [
        DG('sollen', 'ich soll / du sollst / er soll', ('je dois (on me le demande)', 'I am supposed to, I should')),
        DG('solltest', 'du solltest / Sie sollten', ('tu devrais / vous devriez', 'you should (advice)')),
        DG('imperativ-ihr', 'Trink! / Trinkt! / Trinken Sie!', ('impératif (du, ihr, Sie)', 'imperative (du, ihr, Sie)')),
        D('im-bett-bleiben', 'im Bett bleiben', ('rester au lit', 'to stay in bed')),
        D('rauchen', 'rauchen', ('fumer', 'to smoke')),
        D('sport-machen', 'Sport machen', ('faire du sport', 'to do sport, to exercise')),
        D('viel-wenig', 'viel / wenig', ('beaucoup / peu', 'a lot / little')),
        D('rat', 'der Rat', ('le conseil', 'the advice')),
      ], [
        x('Der Arzt sagt, ich soll viel Tee trinken und im Bett bleiben.', 'Le médecin dit que je dois boire beaucoup de thé et rester au lit.', 'The doctor says I should drink a lot of tea and stay in bed.'),
        x('Du solltest weniger arbeiten und mehr Sport machen.', 'Tu devrais moins travailler et faire plus de sport.', 'You should work less and do more sport.'),
      ], [
        FB(CHOOSE, 'Der Arzt sagt, du ＿ nicht rauchen.', ['sollst', 'soll', 'sollen'], 'sollst', ('Avec du : sollst.', 'With du: sollst.'), ('Le médecin dit que tu ne dois pas fumer.', 'The doctor says you should not smoke.')),
        FB(CHOOSE, 'Du bist müde? Du ＿ mehr schlafen.', ['solltest', 'sollst du', 'gesollt'], 'solltest', ('Conseil : du solltest + infinitif.', 'Advice: du solltest + infinitive.'), ('Tu es fatigué ? Tu devrais dormir davantage.', 'You are tired? You should sleep more.')),
        FB(CHOOSE, 'Kinder, ＿ viel Wasser!', ['trinkt', 'trink', 'trinken'], 'trinkt', ('À plusieurs personnes qu’on tutoie : trinkt!', 'To several people you address as du: trinkt!'), ('Les enfants, buvez beaucoup d’eau !', 'Children, drink a lot of water!')),
        DC(ANSWER, [('Freund', 'Ich habe Fieber und Husten. Was soll ich tun?')], ('Un ami malade te demande conseil.', 'A sick friend asks for your advice.'), ['Du solltest zum Arzt gehen.', 'Du sollst krank.', 'Du solltest mehr rauchen.'], 'Du solltest zum Arzt gehen.', ('Conseil : du solltest… gehen.', 'Advice: du solltest… gehen.')),
      ]),
  ])])

# ═════════════════════════ 8 : La politesse, le futur, les médias ═════════════════════════
W8 = WORLD('goethea2-w8', ('Le château du Roi Barbe-de-Grive', 'King Thrushbeard’s castle'), REGION,
  ('Demander poliment avec könnte, würde et hätte gern, parler de l’avenir avec werden, téléphoner et écrire un message.', 'Ask politely with könnte, würde and hätte gern, talk about the future with werden, make a phone call and write a message.'),
  (('Le Roi Barbe-de-Grive', 'King Thrushbeard'), '♚', ('La princesse orgueilleuse s’est moquée de tous ses prétendants, et le Roi Barbe-de-Grive lui donne une leçon de politesse. À toi d’abord : demande, propose et promets avec les formes les plus courtoises.', 'The proud princess mocked all her suitors, and King Thrushbeard is teaching her a lesson in politeness. You first: ask, offer and promise with the most courteous forms.')),
  [CH('goethea2-w8-c1', ('Une leçon de politesse', 'A lesson in politeness'), [
    L('de-hoeflich', ('La politesse : könnte, würde, hätte gern', 'Politeness: könnte, würde, hätte gern'), ('Demander un service ou exprimer un souhait avec courtoisie.', 'Ask a favour or express a wish courteously.'), 8, [
        ('Könnten Sie…? (pourriez-vous… ?) est plus poli que Können Sie…? Könnten Sie mir bitte helfen? Könntest du das Fenster öffnen?', 'Könnten Sie…? (could you…?) is more polite than Können Sie…? Könnten Sie mir bitte helfen? Könntest du das Fenster öffnen?'),
        ('Würde + infinitif exprime un souhait ou une demande : Ich würde gern nach Berlin fahren (j’aimerais aller à Berlin). Würden Sie bitte warten?', 'Würde + infinitive expresses a wish or a request: Ich würde gern nach Berlin fahren (I would like to go to Berlin). Würden Sie bitte warten?'),
        ('Ich hätte gern… = j’aimerais avoir… (au magasin, au restaurant). Ich wäre gern… = j’aimerais être… Darf ich…? = puis-je… ?', 'Ich hätte gern… = I would like to have… (in a shop, a restaurant). Ich wäre gern… = I would like to be… Darf ich…? = may I…?'),
      ], [
        DG('koennten', 'Könnten Sie …? / Könntest du …?', ('Pourriez-vous… ? / Pourrais-tu… ?', 'Could you…?')),
        DG('wuerde', 'ich würde gern + Infinitiv', ('j’aimerais + infinitif', 'I would like to + verb')),
        DG('haette-gern', 'ich hätte gern …', ('j’aimerais avoir…', 'I would like to have…')),
        D('darf-ich', 'Darf ich …?', ('Puis-je… ?', 'May I…?')),
        D('warten', 'warten', ('attendre', 'to wait')),
        D('oeffnen', 'öffnen', ('ouvrir', 'to open')),
        D('hoeflich', 'höflich', ('poli', 'polite')),
        D('natuerlich', 'natürlich', ('bien sûr, naturellement', 'of course, naturally')),
      ], [
        x('Könnten Sie mir bitte die Tür öffnen? — Natürlich, gern.', 'Pourriez-vous m’ouvrir la porte, s’il vous plaît ? — Bien sûr, volontiers.', 'Could you open the door for me, please? — Of course, gladly.'),
        x('Ich würde gern den König sprechen. — Würden Sie bitte hier warten?', 'J’aimerais parler au roi. — Voudriez-vous attendre ici, s’il vous plaît ?', 'I would like to speak to the king. — Would you please wait here?'),
      ], [
        FB(CHOOSE, '＿ Sie mir bitte helfen?', ['Könnten', 'Könntest', 'Kann'], 'Könnten', ('Forme polie avec Sie : Könnten Sie…?', 'Polite form with Sie: Könnten Sie…?'), ('Pourriez-vous m’aider, s’il vous plaît ?', 'Could you help me, please?')),
        FB(CHOOSE, 'Ich ＿ gern einen Kaffee.', ['hätte', 'würde', 'könnte'], 'hätte', ('J’aimerais avoir : ich hätte gern.', 'I would like to have: ich hätte gern.'), ('J’aimerais un café.', 'I would like a coffee.')),
        FB(CHOOSE, 'Ich ＿ gern nach Wien fahren.', ['würde', 'hätte', 'wäre'], 'würde', ('Souhait + infinitif : ich würde gern… fahren.', 'Wish + infinitive: ich würde gern… fahren.'), ('J’aimerais aller à Vienne.', 'I would like to go to Vienna.')),
        DC(ANSWER, [('Diener', 'Guten Tag. Was wünschen Sie?')], ('Le serviteur t’accueille au château (tu voudrais parler au roi).', 'The servant greets you at the castle (you would like to speak to the king).'), ['Ich würde gern den König sprechen.', 'Ich will König.', 'Gib mir den König!'], 'Ich würde gern den König sprechen.', ('Demande polie : ich würde gern + infinitif.', 'Polite request: ich würde gern + infinitive.')),
      ]),
    L('de-werden', ('Parler de l’avenir : werden', 'Talking about the future: werden'), ('Dire ce qu’on fera, faire une promesse ou une prévision.', 'Say what you will do, make a promise or a prediction.'), 8, [
        ('Souvent, le présent + un repère de temps suffit : Morgen fahre ich nach Köln. Nächste Woche habe ich Urlaub.', 'Often the present + a time marker is enough: Morgen fahre ich nach Köln. Nächste Woche habe ich Urlaub.'),
        ('Pour une promesse, une prévision ou un projet : werden + infinitif à la fin. ich werde, du wirst, er wird, wir werden, ihr werdet, sie werden. Ich werde dich nie vergessen.', 'For a promise, a prediction or a plan: werden + infinitive at the end. ich werde, du wirst, er wird, wir werden, ihr werdet, sie werden. Ich werde dich nie vergessen.'),
        ('Werden seul = devenir : Sie wird Königin (elle devient reine). Es wird kalt (il commence à faire froid). Repères : bald (bientôt), später (plus tard), in zwei Jahren (dans deux ans).', 'Werden alone = to become: Sie wird Königin (she becomes queen). Es wird kalt (it is getting cold). Markers: bald (soon), später (later), in zwei Jahren (in two years).'),
      ], [
        DG('futur', 'werden + Infinitiv', ('futur (werden + infinitif)', 'future (werden + infinitive)')),
        D('werden', 'werden', ('devenir', 'to become')),
        D('bald', 'bald', ('bientôt', 'soon')),
        D('spaeter', 'später', ('plus tard', 'later')),
        D('naechste-woche', 'nächste Woche', ('la semaine prochaine', 'next week')),
        D('zukunft', 'die Zukunft', ('l’avenir', 'the future (time to come)')),
        D('versprechen', 'versprechen', ('promettre', 'to promise')),
        D('heiraten', 'heiraten', ('se marier, épouser', 'to marry, to get married')),
      ], [
        x('Die Prinzessin wird den ersten Bettler heiraten: Das hat der König versprochen.', 'La princesse épousera le premier mendiant venu : le roi l’a promis.', 'The princess will marry the first beggar: the king has promised it.'),
        x('Bald wird sie Königin. In Zukunft wird sie höflicher sein.', 'Bientôt, elle sera reine. À l’avenir, elle sera plus polie.', 'Soon she will be queen. In future she will be more polite.'),
      ], [
        FB(CHOOSE, 'Ich ＿ dich morgen anrufen.', ['werde', 'wirst', 'wird'], 'werde', ('Avec ich : werde.', 'With ich: werde.'), ('Je t’appellerai demain.', 'I will call you tomorrow.')),
        FB(CHOOSE, 'Er ＿ Arzt. Er studiert Medizin.', ['wird', 'werde', 'ist geworden haben'], 'wird', ('Werden = devenir ; avec er : wird.', 'Werden = to become; with er: wird.'), ('Il devient médecin. Il étudie la médecine.', 'He is becoming a doctor. He is studying medicine.')),
        order(('Remets dans l’ordre : « Nous irons bientôt à Berlin. »', 'Put in order: “We will soon go to Berlin.”'), ['Wir', 'werden', 'bald', 'nach', 'Berlin', 'fahren.'], ('Werden en deuxième position, l’infinitif à la fin.', 'Werden in second position, the infinitive at the end.')),
        TF('Nächste Woche habe ich Urlaub.', ('La personne parle de la semaine dernière.', 'The person is talking about last week.'), FAUX, ('Nächste Woche = la semaine prochaine.', 'Nächste Woche = next week.')),
      ]),
  ]),
  CH('goethea2-w8-c2', ('Des nouvelles du château', 'News from the castle'), [
    L('de-medien', ('Téléphoner et écrire un message', 'Phoning and writing a message'), ('Se présenter au téléphone, laisser un message et écrire un courriel simple.', 'Introduce yourself on the phone, leave a message and write a simple email.'), 8, [
        ('Au téléphone, on décroche en donnant son nom : Müller, guten Tag! Hier ist Anna Weber. Kann ich bitte Herrn Braun sprechen? Auf Wiederhören! (au revoir, au téléphone).', 'On the phone you answer with your name: Müller, guten Tag! Hier ist Anna Weber. Kann ich bitte Herrn Braun sprechen? Auf Wiederhören! (goodbye, on the phone).'),
        ('Laisser un message : Können Sie ihm etwas ausrichten? (pouvez-vous lui transmettre un message ?). Ich rufe später zurück (je rappelle plus tard). Bitte rufen Sie mich zurück.', 'Leaving a message: Können Sie ihm etwas ausrichten? (can you give him a message?). Ich rufe später zurück (I will call back later). Bitte rufen Sie mich zurück.'),
        ('Écrire : Liebe Anna, / Lieber Paul, (familier) ; Sehr geehrte Frau Braun, / Sehr geehrter Herr Braun, (formel). Fin : Viele Grüße / Liebe Grüße (familier), Mit freundlichen Grüßen (formel).', 'Writing: Liebe Anna, / Lieber Paul, (informal); Sehr geehrte Frau Braun, / Sehr geehrter Herr Braun, (formal). Closing: Viele Grüße / Liebe Grüße (informal), Mit freundlichen Grüßen (formal).'),
      ], [
        D('handy', 'das Handy', ('le téléphone portable', 'the mobile phone')),
        D('nachricht', 'die Nachricht', ('le message ; la nouvelle', 'the message; the news')),
        D('zurueckrufen', 'zurückrufen', ('rappeler (au téléphone)', 'to call back')),
        D('auf-wiederhoeren', 'Auf Wiederhören!', ('au revoir ! (au téléphone)', 'goodbye! (on the phone)')),
        D('schicken', 'schicken', ('envoyer', 'to send')),
        D('sehr-geehrte', 'Sehr geehrte Frau … / Sehr geehrter Herr …', ('Madame… / Monsieur… (lettre formelle)', 'Dear Mrs… / Dear Mr… (formal letter)')),
        D('viele-gruesse', 'Viele Grüße', ('amicalement, bien à toi', 'best wishes')),
        D('mfg', 'Mit freundlichen Grüßen', ('cordialement', 'yours sincerely')),
        D('antworten', 'antworten', ('répondre', 'to answer, to reply')),
      ], [
        x('Hier ist Anna Weber. Kann ich bitte Herrn Braun sprechen? — Er ist nicht da. Er ruft Sie später zurück.', 'Ici Anna Weber. Puis-je parler à monsieur Braun ? — Il n’est pas là. Il vous rappellera plus tard.', 'This is Anna Weber. May I speak to Mr Braun, please? — He is not here. He will call you back later.'),
        x('Schick mir bitte eine Nachricht, wenn du am Bahnhof bist.', 'Envoie-moi un message quand tu seras à la gare, s’il te plaît.', 'Please send me a message when you are at the station.'),
      ], [
        FB(COMPLETE, 'Am Telefon sagt man zum Schluss: Auf ＿!', ['Wiederhören', 'Wiedersehen', 'Nachricht'], 'Wiederhören', ('Au téléphone, on s’entend sans se voir : Auf Wiederhören.', 'On the phone you hear but do not see each other: Auf Wiederhören.'), ('Au téléphone, on dit pour finir : au revoir !', 'On the phone you end by saying: goodbye!')),
        FB(CHOOSE, 'Sehr ＿ Herr Braun, …', ['geehrter', 'geehrte', 'lieber'], 'geehrter', ('Formel, pour un homme : Sehr geehrter Herr…', 'Formal, to a man: Sehr geehrter Herr…'), ('Monsieur Braun, …', 'Dear Mr Braun, …')),
        DC(ANSWER, [('Sekretärin', 'Herr Braun ist leider nicht da.')], ('La secrétaire t’annonce que M. Braun est absent (tu rappelleras plus tard).', 'The secretary tells you Mr Braun is out (you will call back later).'), ['Danke, ich rufe später zurück.', 'Danke, ich bin Herr Braun.', 'Auf Wiedersehen am Telefon gehabt.'], 'Danke, ich rufe später zurück.', ('Rappeler : zurückrufen ; ich rufe später zurück.', 'To call back: zurückrufen; ich rufe später zurück.')),
        TF('Liebe Anna, … Viele Grüße, Tom', ('C’est une lettre formelle.', 'This is a formal letter.'), FAUX, ('Liebe… et Viele Grüße sont familiers.', 'Liebe… and Viele Grüße are informal.')),
      ]),
  ])])

write_level('GOETHEA2', ('Goethe A2 : du Rhin à la Forêt-Noire', 'Goethe A2: from the Rhine to the Black Forest'), REGION, 'Black Forest', 49,
  [W1, W2, W3, W4, W5, W6, W7, W8, FINAL('GOETHEA2', REGION, ('Simulation Goethe A2 : le festin des contes', 'Goethe A2 simulation: the feast of tales'), 'Lesen, Hören et Schreiben (l’oral, Sprechen, n’est pas évalué)', 'Lesen, Hören and Schreiben (the speaking test, Sprechen, is not assessed)')])
