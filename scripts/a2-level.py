# Niveau A2 (anglais, CECRL A2, préparation au TOEIC) : 8 îles, 22 leçons et un examen blanc TOEIC (français + anglais).
# Mode histoire : écuyer·ère de la Table ronde, en déplacement pour Avalon & Co. sur les terres de Logres.
# Usage : python3 scripts/a2-level.py   (réécrit content/a2/a2.json)
from en_common import *

REGION = 'Terres de Logres'

# ═════════════════════════ Île 1 : Le voyage d'affaires ═════════════════════════
W1 = WORLD('a2-w1', ('Le voyage d’affaires', 'The business trip'), REGION,
  ('Raconter un voyage et ses imprévus : prétérit et prétérit progressif, when et while.', 'Tell the story of a trip and its surprises: past simple and past continuous, when and while.'),
  (('Redcap, le lutin au bonnet rouge', 'Redcap, the goblin with the red cap'), 'R', ('Ce lutin des tours en ruine de la frontière écossaise a semé la pagaille dans ton train de nuit. Raconte précisément ce qui se passait quand tout a déraillé.', 'This goblin from the ruined towers of the Scottish border caused chaos on your night train. Describe exactly what was happening when everything went wrong.')),
  [CH('a2-w1-c1', ('En route', 'On the way'), [
    L('en-past-continuous', ('Le prétérit progressif : I was working', 'The past continuous: I was working'), ('Décrire une action en cours dans le passé avec was / were + -ing.', 'Describe an action in progress in the past with was / were + -ing.'), 9, [
        ('was / were + verbe en -ing décrit une action en cours à un moment du passé : At 8 p.m. I was having dinner.', 'was / were + verb + -ing describes an action in progress at a moment in the past: At 8 p.m. I was having dinner.'),
        ('C’est le décor de l’histoire : It was raining and people were waiting for the train.', 'It sets the scene of a story: It was raining and people were waiting for the train.'),
        ('Négation : wasn’t / weren’t + -ing. Question : What were you doing at nine?', 'Negative: wasn’t / weren’t + -ing. Question: What were you doing at nine?'),
      ], [
        EG('past-continuous', 'was / were + -ing', ('prétérit progressif (action en cours dans le passé)', 'past continuous (action in progress in the past)')),
        E('journey', 'journey', ('trajet, voyage', 'journey')),
        E('delay', 'delay', ('retard', 'delay')),
        E('passenger', 'passenger', ('passager, passagère', 'passenger')),
        E('luggage', 'luggage', ('bagages', 'luggage')),
        E('carriage', 'carriage', ('voiture (de train)', 'carriage')),
        E('snow', 'to snow', ('neiger', 'to snow')),
      ], [
        x('At midnight, the train was crossing the border and most passengers were sleeping.', 'À minuit, le train franchissait la frontière et la plupart des passagers dormaient.'),
        x('What were you doing when the lights went out? — I was reading a report.', 'Que faisais-tu quand les lumières se sont éteintes ? — Je lisais un rapport.'),
      ], [
        FB(CHOOSE, 'At 10 p.m. I ＿ an email to the client.', ['was writing', 'wrote', 'am writing'], 'was writing', ('Action en cours à 22 h : was + -ing.', 'Action in progress at 10 p.m.: was + -ing.'), ('À 22 h, j’écrivais un e-mail au client.', 'At 10 p.m. I was writing an email to the client.')),
        FB(CHOOSE, 'It was snowing and the passengers ＿ on the platform.', ['were waiting', 'was waiting', 'waited for'], 'were waiting', ('Sujet pluriel : were + -ing.', 'Plural subject: were + -ing.'), ('Il neigeait et les passagers attendaient sur le quai.', 'It was snowing and the passengers were waiting on the platform.')),
        DC(ANSWER, [('Mr Ambrose', 'What were you doing at nine last night?')], ('M. Ambrose te demande ce que tu faisais hier à 21 h.', 'Mr Ambrose asks what you were doing at nine last night.'), ['I was travelling to York.', 'I travel to York.', 'I’m travelling to York.'], 'I was travelling to York.', ('What were you doing? → I was + -ing.', 'What were you doing? → I was + -ing.')),
        TF('The train was crossing the border when the lights went out.', ('Le train était arrêté en gare.', 'The train was stopped at a station.'), FAUX, ('was crossing = il était en train de franchir la frontière.', 'was crossing = it was moving across the border.')),
      ]),
    L('en-when-while', ('Quand tout bascule : when, while', 'When everything changes: when, while'), ('Combiner prétérit simple et progressif pour raconter un imprévu.', 'Combine the past simple and continuous to tell an unexpected event.'), 10, [
        ('Action longue (progressif) interrompue par une action courte (prétérit) : I was sleeping when the train stopped.', 'A long action (continuous) interrupted by a short one (past simple): I was sleeping when the train stopped.'),
        ('while + action longue : While I was waiting, I met an old friend. when + action courte : when the phone rang.', 'while + long action: While I was waiting, I met an old friend. when + short action: when the phone rang.'),
        ('Rappel des irréguliers utiles en voyage : lose → lost, leave → left, find → found, miss → missed.', 'Useful irregular verbs when travelling: lose → lost, leave → left, find → found, miss → missed.'),
      ], [
        EG('when-while', 'when / while', ('quand (action courte) / pendant que (action longue)', 'when / while (past actions)')),
        E('miss', 'to miss (a train)', ('rater (un train)', 'to miss (a train)')),
        E('lose', 'to lose', ('perdre', 'to lose')),
        E('lost', 'lost', ('perdu (passé de lose)', 'lost (past of lose)')),
        E('suddenly', 'suddenly', ('soudain, tout à coup', 'suddenly')),
        E('break-down', 'to break down', ('tomber en panne', 'to break down')),
        E('arrive', 'to arrive', ('arriver', 'to arrive')),
      ], [
        x('While we were crossing the moors, the train suddenly broke down.', 'Pendant que nous traversions la lande, le train est soudain tombé en panne.'),
        x('I lost my ticket when I was running for the bus.', 'J’ai perdu mon billet en courant après le bus.'),
      ], [
        FB(CHOOSE, 'I was having lunch ＿ the phone rang.', ['when', 'while', 'during'], 'when', ('Action courte qui interrompt : when.', 'A short action that interrupts: when.'), ('Je déjeunais quand le téléphone a sonné.', 'I was having lunch when the phone rang.')),
        FB(CHOOSE, '＿ I was waiting for the taxi, it started to rain.', ['While', 'When', 'During'], 'While', ('Action longue : while + progressif.', 'Long action: while + continuous.'), ('Pendant que j’attendais le taxi, il s’est mis à pleuvoir.', 'While I was waiting for the taxi, it started to rain.')),
        FB(CHOOSE, 'We ＿ the last train, so we took a taxi.', ['missed', 'were missing', 'miss'], 'missed', ('Action courte et terminée : prétérit.', 'A short, finished action: past simple.'), ('Nous avons raté le dernier train, alors nous avons pris un taxi.', 'We missed the last train, so we took a taxi.')),
        order(('Remets dans l’ordre : « Je dormais quand le train s’est arrêté. »', 'Put in order: “I was sleeping when the train stopped.”'), ['I', 'was', 'sleeping', 'when', 'the', 'train', 'stopped.'], ('Action longue + when + action courte.', 'Long action + when + short action.')),
      ]),
  ]),
  CH('a2-w1-c2', ('À l’hôtel', 'At the hotel'), [
    L('en-hotel', ('À la réception de l’hôtel', 'At the hotel reception'), ('Réserver, arriver et signaler un problème à l’hôtel.', 'Book, check in and report a problem at a hotel.'), 9, [
        ('Arriver : I’d like to check in, please. I have a reservation / a booking under the name Martin.', 'Arriving: I’d like to check in, please. I have a reservation / a booking under the name Martin.'),
        ('Signaler un problème poliment : I’m afraid there’s a problem with my room. The heating doesn’t work.', 'Reporting a problem politely: I’m afraid there’s a problem with my room. The heating doesn’t work.'),
        ('Partir : What time is check-out? Could I leave my luggage here?', 'Leaving: What time is check-out? Could I leave my luggage here?'),
      ], [
        E('check-in', 'to check in', ('s’enregistrer, arriver (hôtel, aéroport)', 'to check in')),
        E('booking', 'booking', ('réservation', 'booking')),
        E('single-room', 'single room', ('chambre simple', 'single room')),
        E('heating', 'heating', ('chauffage', 'heating')),
        E('floor-level', 'floor', ('étage', 'floor (level)')),
        E('lift', 'lift', ('ascenseur', 'lift')),
        E('receipt', 'receipt', ('reçu, ticket de caisse', 'receipt')),
      ], [
        x('Good evening. I have a booking under the name Martin. — Welcome! You’re in room 214, on the second floor.', 'Bonsoir. J’ai une réservation au nom de Martin. — Bienvenue ! Vous êtes à la chambre 214, au deuxième étage.'),
        x('I’m afraid the heating in my room isn’t working.', 'Je suis désolé, mais le chauffage de ma chambre ne fonctionne pas.'),
      ], [
        DC(ANSWER, [('Receptionist', 'Good evening. How can I help you?')], ('Tu arrives à l’hôtel.', 'You arrive at the hotel.'), ['I’d like to check in, please.', 'I’d like to check the time.', 'I check in yesterday.'], 'I’d like to check in, please.', ('Pour arriver à l’hôtel : I’d like to check in.', 'To arrive at a hotel: I’d like to check in.')),
        FB(COMPLETE, 'Take the ＿ to the fourth floor.', ['lift', 'stairs up', 'heating'], 'lift', ('lift = ascenseur (en américain : elevator).', 'lift = elevator in American English.'), ('Prenez l’ascenseur jusqu’au quatrième étage.', 'Take the lift to the fourth floor.')),
        DC(ANSWER, [('Receptionist', 'Is everything all right with your room?')], ('La réceptionniste te demande si tout va bien.', 'The receptionist asks if everything is all right.'), ['I’m afraid the heating doesn’t work.', 'Yes, I’m a room.', 'I’d like a receipt of heating.'], 'I’m afraid the heating doesn’t work.', ('Pour signaler poliment un problème : I’m afraid…', 'To report a problem politely: I’m afraid…')),
        TF('Could I have a receipt, please?', ('La personne demande un reçu.', 'The person is asking for a receipt.'), VRAI, ('receipt = reçu.', 'receipt = proof of payment.')),
      ]),
  ])])

# ═════════════════════════ Île 2 : Comparer ═════════════════════════
W2 = WORLD('a2-w2', ('Le marché aux merveilles', 'The market of wonders'), REGION,
  ('Comparer des offres, des produits et des villes : comparatifs, superlatifs, as… as.', 'Compare offers, products and cities: comparatives, superlatives, as… as.'),
  (('Jenny Greenteeth, la sorcière des étangs', 'Jenny Greenteeth, the pond witch'), 'J', ('Cachée sous les lentilles d’eau, la vieille Jenny marchande avec les passants et leur vend toujours le pire article. Compare mieux qu’elle pour repartir avec la bonne affaire.', 'Hidden under the duckweed, old Jenny bargains with passers-by and always sells them the worst item. Compare better than her and leave with the right deal.')),
  [CH('a2-w2-c1', ('Plus ou moins', 'More or less'), [
    L('en-comparatives', ('Comparer : cheaper, more expensive', 'Comparing: cheaper, more expensive'), ('Former le comparatif des adjectifs courts et longs.', 'Form the comparative of short and long adjectives.'), 10, [
        ('Adjectif court + -er + than : cheap → cheaper than, big → bigger than (consonne doublée), easy → easier than.', 'Short adjective + -er + than: cheap → cheaper than, big → bigger than (double consonant), easy → easier than.'),
        ('Adjectif long : more + adjectif + than : more expensive than, more comfortable than.', 'Long adjective: more + adjective + than: more expensive than, more comfortable than.'),
        ('Irréguliers : good → better, bad → worse, far → further.', 'Irregular: good → better, bad → worse, far → further.'),
      ], [
        EG('comparative', 'comparative (-er than / more… than)', ('comparatif (plus… que)', 'comparative (-er / more… than)')),
        E('expensive', 'expensive', ('cher, coûteux', 'expensive')),
        E('better', 'better', ('meilleur, mieux', 'better')),
        E('worse', 'worse', ('pire, plus mauvais', 'worse')),
        E('comfortable', 'comfortable', ('confortable', 'comfortable')),
        E('fast', 'fast', ('rapide', 'fast')),
        E('offer', 'offer', ('offre', 'offer')),
      ], [
        x('The train is faster than the bus, but it’s more expensive.', 'Le train est plus rapide que le bus, mais il est plus cher.'),
        x('This offer is better than the first one.', 'Cette offre est meilleure que la première.'),
      ], [
        FB(CHOOSE, 'The new laptop is ＿ than the old one.', ['lighter', 'more light', 'lightest'], 'lighter', ('Adjectif court : light → lighter.', 'Short adjective: light → lighter.'), ('Le nouvel ordinateur portable est plus léger que l’ancien.', 'The new laptop is lighter than the old one.')),
        FB(CHOOSE, 'First class is ＿ than second class.', ['more comfortable', 'comfortabler', 'most comfortable'], 'more comfortable', ('Adjectif long : more + adjectif.', 'Long adjective: more + adjective.'), ('La première classe est plus confortable que la seconde.', 'First class is more comfortable than second class.')),
        FB(CHOOSE, 'The weather today is ＿ than yesterday.', ['worse', 'badder', 'more bad'], 'worse', ('bad → worse (irrégulier).', 'bad → worse (irregular).'), ('Le temps aujourd’hui est pire qu’hier.', 'The weather today is worse than yesterday.')),
        TF('The bus is cheaper than the train.', ('Le bus coûte plus cher que le train.', 'The bus costs more than the train.'), FAUX, ('cheaper = moins cher.', 'cheaper = it costs less.')),
      ]),
    L('en-superlatives', ('Le meilleur : the cheapest, the most popular', 'The best: the cheapest, the most popular'), ('Former le superlatif et comparer avec as… as.', 'Form the superlative and compare with as… as.'), 10, [
        ('Superlatif : the + adjectif court + -est (the cheapest), the most + adjectif long (the most popular). Irréguliers : the best, the worst.', 'Superlative: the + short adjective + -est (the cheapest), the most + long adjective (the most popular). Irregular: the best, the worst.'),
        ('as + adjectif + as = aussi… que : The hotel is as nice as the photos. not as… as = moins… que.', 'as + adjective + as = equally: The hotel is as nice as the photos. not as… as = less than.'),
        ('Après un superlatif, in + lieu : the tallest building in London.', 'After a superlative, in + place: the tallest building in London.'),
      ], [
        EG('superlative', 'superlative (the tallest / the most…)', ('superlatif (le plus…)', 'superlative (the -est / the most)')),
        EG('as-as', 'as… as', ('aussi… que', 'as… as (equal comparison)')),
        E('the-best', 'the best', ('le meilleur, la meilleure', 'the best')),
        E('popular', 'popular', ('populaire, apprécié', 'popular')),
        E('tall', 'tall', ('grand (taille), haut', 'tall')),
        E('quiet', 'quiet', ('calme, silencieux', 'quiet')),
        E('choice', 'choice', ('choix', 'choice')),
      ], [
        x('The Shard is the tallest building in London.', 'Le Shard est le plus haut bâtiment de Londres.'),
        x('This hotel is the most popular, but it isn’t as quiet as the small inn.', 'Cet hôtel est le plus apprécié, mais il n’est pas aussi calme que la petite auberge.'),
      ], [
        FB(CHOOSE, 'It’s the ＿ restaurant in the city.', ['best', 'better', 'goodest'], 'best', ('good → the best.', 'good → the best.'), ('C’est le meilleur restaurant de la ville.', 'It’s the best restaurant in the city.')),
        FB(CHOOSE, 'This is the ＿ popular product in the shop.', ['most', 'more', 'much'], 'most', ('Superlatif d’un adjectif long : the most.', 'Superlative of a long adjective: the most.'), ('C’est le produit le plus populaire du magasin.', 'This is the most popular product in the shop.')),
        FB(CHOOSE, 'My room is as big ＿ yours.', ['as', 'than', 'like'], 'as', ('Égalité : as… as.', 'Equality: as… as.'), ('Ma chambre est aussi grande que la tienne.', 'My room is as big as yours.')),
        DC(ANSWER, [('Jenny', 'Which bag is the cheapest?')], ('Jenny te demande quel sac est le moins cher.', 'Jenny asks which bag is the cheapest.'), ['The blue one. It’s only ten pounds.', 'The blue one is cheaper than.', 'Yes, it’s the cheap.'], 'The blue one. It’s only ten pounds.', ('Which… the cheapest? → on désigne l’objet.', 'Which… the cheapest? → point to the item.')),
      ]),
  ]),
  CH('a2-w2-c2', ('Faire ses achats', 'Shopping'), [
    L('en-shopping', ('Dans un magasin : too, enough', 'In a shop: too, enough'), ('Essayer, demander une autre taille, rendre un article : too et enough.', 'Try things on, ask for another size, return an item: too and enough.'), 9, [
        ('too + adjectif = trop : It’s too small. adjectif + enough = assez : It isn’t big enough.', 'too + adjective = more than needed: It’s too small. adjective + enough = sufficient: It isn’t big enough.'),
        ('Can I try it on? (l’essayer) Have you got it in a larger size? Where are the changing rooms?', 'Can I try it on? Have you got it in a larger size? Where are the changing rooms?'),
        ('Rendre un article : I’d like to return this / get a refund (un remboursement). Do you have the receipt?', 'Returning an item: I’d like to return this / get a refund. Do you have the receipt?'),
      ], [
        EG('too-enough', 'too / enough', ('trop / assez', 'too / enough')),
        E('try-on', 'to try on', ('essayer (un vêtement)', 'to try on')),
        E('size', 'size', ('taille, pointure', 'size')),
        E('refund', 'refund', ('remboursement', 'refund')),
        E('sale', 'sale', ('soldes ; vente', 'sale')),
        E('customer', 'customer', ('client, cliente', 'customer')),
        E('discount', 'discount', ('réduction, remise', 'discount')),
      ], [
        x('Can I try this jacket on? — Of course. The changing rooms are over there.', 'Je peux essayer cette veste ? — Bien sûr. Les cabines sont là-bas.'),
        x('These shoes are too small. Have you got them in a larger size?', 'Ces chaussures sont trop petites. Vous les avez dans une pointure au-dessus ?'),
      ], [
        FB(CHOOSE, 'This coat is ＿ expensive. I can’t buy it.', ['too', 'enough', 'very enough'], 'too', ('Excès : too + adjectif.', 'Excess: too + adjective.'), ('Ce manteau est trop cher. Je ne peux pas l’acheter.', 'This coat is too expensive. I can’t buy it.')),
        FB(CHOOSE, 'The room isn’t big ＿ for ten people.', ['enough', 'too', 'very'], 'enough', ('adjectif + enough.', 'adjective + enough.'), ('La salle n’est pas assez grande pour dix personnes.', 'The room isn’t big enough for ten people.')),
        DC(ANSWER, [('Shop assistant', 'Can I help you?')], ('Un vendeur t’aborde.', 'A shop assistant comes up to you.'), ['Yes, can I try this shirt on?', 'Yes, I’m too help.', 'Yes, it’s enough.'], 'Yes, can I try this shirt on?', ('Pour essayer : Can I try it on?', 'To try something: Can I try it on?')),
        TF('There’s a 20% discount on all shoes.', ('Les chaussures sont moins chères.', 'The shoes are cheaper.'), VRAI, ('discount = réduction.', 'discount = a lower price.')),
      ]),
  ])])

# ═════════════════════════ Île 3 : Projets et prédictions ═════════════════════════
W3 = WORLD('a2-w3', ('La tour de la fée Morgane', 'Morgan le Fay’s tower'), REGION,
  ('Parler de ses projets et prédire l’avenir : going to, will, le présent progressif pour les rendez-vous.', 'Talk about plans and predict the future: going to, will, the present continuous for arrangements.'),
  (('Morgane la fée', 'Morgan le Fay'), 'M', ('La demi-sœur d’Arthur lit l’avenir dans un miroir et brouille l’agenda de toute l’équipe. Dis clairement ce qui est prévu, décidé ou probable pour déjouer ses prophéties.', 'Arthur’s half-sister reads the future in a mirror and scrambles the whole team’s schedule. Say clearly what is planned, decided or likely to foil her prophecies.')),
  [CH('a2-w3-c1', ('L’agenda', 'The schedule'), [
    L('en-going-to', ('Les projets : be going to', 'Plans: be going to'), ('Annoncer une intention ou une prédiction évidente avec going to.', 'Announce an intention or an obvious prediction with going to.'), 9, [
        ('be going to + base verbale = intention déjà décidée : I’m going to visit the factory next week.', 'be going to + base verb = an intention already decided: I’m going to visit the factory next week.'),
        ('Aussi pour une prédiction évidente : Look at those clouds! It’s going to rain.', 'Also for an obvious prediction: Look at those clouds! It’s going to rain.'),
        ('Repères : tomorrow, next week, next month, in two days, soon.', 'Time words: tomorrow, next week, next month, in two days, soon.'),
      ], [
        EG('going-to', 'be going to', ('aller faire (intention, prédiction évidente)', 'be going to (plans)')),
        E('tomorrow', 'tomorrow', ('demain', 'tomorrow')),
        E('next-week', 'next week', ('la semaine prochaine', 'next week')),
        E('plan', 'plan', ('projet, plan', 'plan')),
        E('factory', 'factory', ('usine', 'factory')),
        E('soon', 'soon', ('bientôt', 'soon')),
        E('visit-trip', 'trip', ('voyage, déplacement', 'trip')),
      ], [
        x('Next week, Tom is going to visit the factory in Manchester.', 'La semaine prochaine, Tom va visiter l’usine de Manchester.'),
        x('Look at the sky! It’s going to snow.', 'Regarde le ciel ! Il va neiger.'),
      ], [
        FB(CHOOSE, 'I’m ＿ to call the client tomorrow.', ['going', 'go', 'will'], 'going', ('Intention : be going to.', 'Intention: be going to.'), ('Je vais appeler le client demain.', 'I’m going to call the client tomorrow.')),
        FB(CHOOSE, 'They ＿ going to open a new office.', ['are', 'is', 'will'], 'are', ('they → are going to.', 'they → are going to.'), ('Ils vont ouvrir un nouveau bureau.', 'They are going to open a new office.')),
        DC(ANSWER, [('Kate', 'What are you going to do this weekend?')], ('Kate te demande tes projets du week-end.', 'Kate asks about your weekend plans.'), ['I’m going to visit my parents.', 'I visited my parents.', 'I’m visit my parents.'], 'I’m going to visit my parents.', ('going to → I’m going to + verbe.', 'going to → I’m going to + verb.')),
        TF('Look at those clouds! It’s going to rain.', ('La personne pense qu’il va pleuvoir.', 'The person thinks it will rain.'), VRAI, ('Prédiction évidente : going to.', 'An obvious prediction: going to.')),
      ]),
    L('en-arrangements', ('Les rendez-vous : I’m meeting…', 'Arrangements: I’m meeting…'), ('Parler d’un rendez-vous fixé avec le présent progressif.', 'Talk about a fixed arrangement with the present continuous.'), 9, [
        ('Un rendez-vous fixé (avec une heure, une personne) se dit souvent au présent progressif : I’m meeting the director at 3 p.m.', 'A fixed arrangement (with a time, a person) is often in the present continuous: I’m meeting the director at 3 p.m.'),
        ('Les horaires officiels (trains, réunions planifiées) utilisent le présent simple : The train leaves at 7.15.', 'Timetables (trains, scheduled meetings) use the present simple: The train leaves at 7.15.'),
        ('Pour proposer : Are you free on Thursday? / How about Friday morning?', 'To suggest: Are you free on Thursday? / How about Friday morning?'),
      ], [
        EG('present-cont-future', 'present continuous for the future', ('rendez-vous prévu (I’m meeting…)', 'present continuous for arrangements')),
        E('appointment', 'appointment', ('rendez-vous (médecin, professionnel)', 'appointment')),
        E('free', 'free', ('libre ; gratuit', 'free')),
        E('busy', 'busy', ('occupé', 'busy')),
        E('schedule', 'schedule', ('emploi du temps, planning', 'schedule')),
        E('director', 'director', ('directeur, directrice', 'director')),
        E('how-about', 'How about…?', ('Et si… ? Que dirais-tu de… ?', 'How about…? (suggestion)')),
      ], [
        x('Are you free on Thursday? — Sorry, I’m flying to Dublin on Thursday. How about Friday?', 'Tu es libre jeudi ? — Désolé, je pars en avion pour Dublin jeudi. Et vendredi ?'),
        x('I have an appointment with the director at four.', 'J’ai rendez-vous avec la directrice à 16 heures.'),
      ], [
        FB(CHOOSE, 'I ＿ the director tomorrow at 10. It’s in my calendar.', ['am meeting', 'have met', 'met'], 'am meeting', ('Rendez-vous fixé : présent progressif.', 'Fixed arrangement: present continuous.'), ('Je vois la directrice demain à 10 h. C’est dans mon agenda.', 'I am meeting the director tomorrow at 10. It’s in my calendar.')),
        FB(CHOOSE, 'The train ＿ at 7.15 tomorrow morning.', ['leaves', 'is leave', 'leaving'], 'leaves', ('Horaire officiel : présent simple.', 'Timetable: present simple.'), ('Le train part demain à 7 h 15.', 'The train leaves at 7.15 tomorrow morning.')),
        DC(ANSWER, [('Tom', 'Are you free on Monday afternoon?')], ('Tom veut te voir lundi après-midi.', 'Tom wants to meet on Monday afternoon.'), ['Sorry, I’m busy. How about Tuesday?', 'Sorry, I’m free busy.', 'Yes, I was free.'], 'Sorry, I’m busy. How about Tuesday?', ('Pour refuser et proposer : How about… ?', 'To decline and suggest: How about…?')),
        TF('I have an appointment with the doctor at five.', ('La personne voit le médecin à 17 h.', 'The person is seeing the doctor at 5 p.m.'), VRAI, ('appointment = rendez-vous.', 'appointment = a fixed meeting.')),
      ]),
  ]),
  CH('a2-w3-c2', ('L’avenir', 'The future'), [
    L('en-will', ('Le futur avec will', 'The future with will'), ('Prédire, promettre et décider sur le moment avec will.', 'Predict, promise and decide on the spot with will.'), 10, [
        ('will + base verbale : prédiction (I think it will be sunny), promesse (I’ll call you back), décision prise sur le moment (I’ll have the soup).', 'will + base verb: prediction (I think it will be sunny), promise (I’ll call you back), decision made on the spot (I’ll have the soup).'),
        ('Contraction : I’ll, you’ll, she’ll. Négation : won’t (will not).', 'Contraction: I’ll, you’ll, she’ll. Negative: won’t (will not).'),
        ('Avec probably, maybe, I think, I’m sure : I think prices will go up.', 'With probably, maybe, I think, I’m sure: I think prices will go up.'),
      ], [
        EG('will', 'will / won’t', ('futur (prédiction, promesse, décision immédiate)', 'will / won’t (future)')),
        E('probably', 'probably', ('probablement', 'probably')),
        E('promise', 'to promise', ('promettre', 'to promise')),
        E('future', 'future', ('avenir, futur', 'future')),
        E('price-rise', 'to go up', ('augmenter (prix, chiffres)', 'to go up (prices)')),
        E('sure', 'sure', ('sûr, certain', 'sure')),
      ], [
        x('I think the meeting will probably finish late.', 'Je pense que la réunion finira probablement tard.'),
        x('Don’t worry, I won’t forget. I promise I’ll call you tomorrow.', 'Ne t’inquiète pas, je n’oublierai pas. Je te promets de t’appeler demain.'),
      ], [
        FB(CHOOSE, 'The phone is ringing. — I ＿ answer it!', ['’ll', '’m going to', 'am'], '’ll', ('Décision sur le moment : will.', 'Decision on the spot: will.'), ('Le téléphone sonne. — Je réponds !', 'The phone is ringing. — I’ll answer it!')),
        FB(CHOOSE, 'Don’t worry, I ＿ be late.', ['won’t', 'don’t', 'willn’t'], 'won’t', ('Négation de will : won’t.', 'Negative of will: won’t.'), ('Ne t’inquiète pas, je ne serai pas en retard.', 'Don’t worry, I won’t be late.')),
        FB(CHOOSE, 'I think prices ＿ go up next year.', ['will', 'are', 'going'], 'will', ('Prédiction avec I think : will.', 'Prediction with I think: will.'), ('Je pense que les prix vont augmenter l’an prochain.', 'I think prices will go up next year.')),
        DC(ANSWER, [('Waiter', 'Are you ready to order?')], ('Le serveur attend ta commande.', 'The waiter is waiting for your order.'), ['Yes, I’ll have the fish, please.', 'Yes, I have the fish yesterday.', 'Yes, I’m going have fish.'], 'Yes, I’ll have the fish, please.', ('Décision immédiate : I’ll have…', 'Decision on the spot: I’ll have…')),
      ]),
  ])])

# ═════════════════════════ Île 4 : Expériences ═════════════════════════
W4 = WORLD('a2-w4', ('La bête de la quête', 'The Questing Beast'), REGION,
  ('Parler de ses expériences et de ce qui vient d’arriver : le present perfect avec ever, never, just, already, yet.', 'Talk about experiences and recent events: the present perfect with ever, never, just, already, yet.'),
  (('La Bête glatissante', 'The Questing Beast'), 'Q', ('Cette créature au corps de léopard et au bruit de meute que les chevaliers poursuivent sans fin demande à chacun ce qu’il a déjà fait dans sa vie. Réponds juste pour qu’elle te laisse passer.', 'This creature with a leopard’s body and the sound of a baying pack, which knights chase forever, asks everyone what they have already done in their life. Answer correctly and it will let you pass.')),
  [CH('a2-w4-c1', ('As-tu déjà… ?', 'Have you ever…?'), [
    L('en-present-perfect', ('Le present perfect : I have visited', 'The present perfect: I have visited'), ('Parler de ses expériences avec have + participe passé.', 'Talk about experiences with have + past participle.'), 10, [
        ('have / has + participe passé relie le passé au présent, sans date précise : I have visited Scotland (je connais l’Écosse).', 'have / has + past participle links the past to the present, with no precise date: I have visited Scotland.'),
        ('Participes : réguliers en -ed (worked) ; irréguliers à apprendre : be → been, go → gone/been, see → seen, eat → eaten, do → done.', 'Participles: regular in -ed (worked); irregular ones to learn: be → been, go → gone/been, see → seen, eat → eaten, do → done.'),
        ('Have you ever…? (as-tu déjà… ?) — Yes, I have. / No, I’ve never… Avec une date, on revient au prétérit : I went there in 2019.', 'Have you ever…? — Yes, I have. / No, I’ve never… With a date, go back to the past simple: I went there in 2019.'),
      ], [
        EG('present-perfect', 'have / has + past participle', ('present perfect (expérience, lien avec le présent)', 'present perfect (have + past participle)')),
        EG('ever-never', 'ever / never', ('déjà (question) / jamais', 'ever / never')),
        E('been', 'been', ('été, allé (participe de be / go)', 'been')),
        E('seen', 'seen', ('vu (participe de see)', 'seen')),
        E('eaten', 'eaten', ('mangé (participe de eat)', 'eaten')),
        E('abroad', 'abroad', ('à l’étranger', 'abroad')),
        E('experience', 'experience', ('expérience (vécue)', 'experience')),
      ], [
        x('Have you ever been to Edinburgh? — Yes, I have. I went there last summer.', 'Tu es déjà allé à Édimbourg ? — Oui. J’y suis allé l’été dernier.'),
        x('I’ve never eaten haggis, but I’ve seen it on a menu!', 'Je n’ai jamais mangé de haggis, mais j’en ai vu sur un menu !'),
      ], [
        FB(CHOOSE, 'Have you ever ＿ to Ireland?', ['been', 'went', 'go'], 'been', ('Have you ever + participe : been.', 'Have you ever + participle: been.'), ('Tu es déjà allé en Irlande ?', 'Have you ever been to Ireland?')),
        FB(CHOOSE, 'She ＿ worked abroad three times.', ['has', 'have', 'is'], 'has', ('she → has + participe.', 'she → has + participle.'), ('Elle a travaillé trois fois à l’étranger.', 'She has worked abroad three times.')),
        FB(CHOOSE, 'I ＿ to Wales in 2022.', ['went', 'have been', 'have gone'], 'went', ('Date précise : prétérit.', 'Precise date: past simple.'), ('Je suis allé au pays de Galles en 2022.', 'I went to Wales in 2022.')),
        DC(ANSWER, [('Questing Beast', 'Have you ever seen a dragon?')], ('La bête te pose une question.', 'The beast asks you a question.'), ['Yes, I have. I saw one in Wales!', 'Yes, I did seen one.', 'Yes, I have saw one.'], 'Yes, I have. I saw one in Wales!', ('Yes, I have, puis le prétérit pour les détails.', 'Yes, I have, then the past simple for details.')),
      ]),
    L('en-just-already-yet', ('Les nouvelles : just, already, yet', 'News: just, already, yet'), ('Annoncer ce qui vient d’arriver et faire le point sur les tâches.', 'Announce what has just happened and check progress on tasks.'), 10, [
        ('just = venir de : I’ve just sent the email (je viens d’envoyer l’e-mail).', 'just = a very short time ago: I’ve just sent the email.'),
        ('already = déjà (plus tôt que prévu) : She’s already finished the report.', 'already = sooner than expected: She’s already finished the report.'),
        ('yet en fin de phrase, dans les questions (déjà ?) et les négations (pas encore) : Have you called him yet? I haven’t called him yet.', 'yet at the end, in questions and negatives: Have you called him yet? I haven’t called him yet.'),
      ], [
        EG('just-already-yet', 'just / already / yet', ('venir de / déjà / pas encore', 'just / already / yet')),
        E('send', 'to send', ('envoyer', 'to send')),
        E('sent', 'sent', ('envoyé (passé de send)', 'sent (past of send)')),
        E('finish', 'to finish', ('finir, terminer', 'to finish')),
        E('report', 'report', ('rapport', 'report')),
        E('task', 'task', ('tâche', 'task')),
        E('not-yet', 'not yet', ('pas encore', 'not yet')),
      ], [
        x('Has the client signed the contract yet? — Yes, he’s just signed it!', 'Le client a déjà signé le contrat ? — Oui, il vient de le signer !'),
        x('I haven’t finished the report yet, but I’ve already written the first part.', 'Je n’ai pas encore fini le rapport, mais j’ai déjà écrit la première partie.'),
      ], [
        FB(CHOOSE, 'I’ve ＿ sent you the file. Check your inbox.', ['just', 'yet', 'ever'], 'just', ('Il y a un instant : just.', 'A moment ago: just.'), ('Je viens de t’envoyer le fichier. Regarde ta boîte de réception.', 'I’ve just sent you the file. Check your inbox.')),
        FB(CHOOSE, 'Have you finished the task ＿?', ['yet', 'already', 'just'], 'yet', ('Question : yet en fin de phrase.', 'Question: yet at the end.'), ('Tu as déjà fini la tâche ?', 'Have you finished the task yet?')),
        FB(CHOOSE, 'We haven’t received the invoice ＿.', ['yet', 'already', 'never'], 'yet', ('Négation : not… yet = pas encore.', 'Negative: not… yet.'), ('Nous n’avons pas encore reçu la facture.', 'We haven’t received the invoice yet.')),
        TF('She’s already finished the report.', ('Le rapport n’est pas terminé.', 'The report isn’t finished.'), FAUX, ('already finished = déjà terminé.', 'already finished = it is done.')),
      ]),
  ]),
  CH('a2-w4-c2', ('Depuis quand ?', 'Since when?'), [
    L('en-for-since', ('Depuis : for, since', 'Duration: for, since'), ('Dire depuis combien de temps avec le present perfect, for et since.', 'Say how long with the present perfect, for and since.'), 10, [
        ('En anglais, « depuis » + situation qui dure encore = present perfect : I’ve worked here for two years (je travaille ici depuis deux ans).', 'For a situation that is still true, English uses the present perfect: I’ve worked here for two years.'),
        ('for + durée (for three months, for a long time) ; since + point de départ (since 2021, since Monday, since I was a child).', 'for + duration (for three months, for a long time); since + starting point (since 2021, since Monday, since I was a child).'),
        ('Question : How long have you lived in London?', 'Question: How long have you lived in London?'),
      ], [
        EG('for-since', 'for / since', ('depuis (durée / point de départ)', 'for / since (duration)')),
        E('how-long', 'How long…?', ('Depuis combien de temps… ? Combien de temps… ?', 'How long…?')),
        E('company', 'company', ('entreprise', 'company')),
        E('known', 'known', ('connu (participe de know)', 'known')),
        E('month', 'month', ('mois', 'month')),
        E('year', 'year', ('an, année', 'year')),
      ], [
        x('How long have you worked for Avalon & Co.? — Since March. So for about eight months.', 'Depuis combien de temps travailles-tu chez Avalon & Co. ? — Depuis mars. Donc depuis environ huit mois.'),
        x('I’ve known Kate since we were at school.', 'Je connais Kate depuis l’école.'),
      ], [
        FB(CHOOSE, 'I’ve lived in London ＿ 2020.', ['since', 'for', 'during'], 'since', ('Point de départ (2020) : since.', 'Starting point (2020): since.'), ('J’habite à Londres depuis 2020.', 'I’ve lived in London since 2020.')),
        FB(CHOOSE, 'She’s worked here ＿ six months.', ['for', 'since', 'ago'], 'for', ('Durée : for.', 'Duration: for.'), ('Elle travaille ici depuis six mois.', 'She’s worked here for six months.')),
        FB(CHOOSE, 'How long ＿ you known him?', ['have', 'do', 'are'], 'have', ('How long + present perfect.', 'How long + present perfect.'), ('Depuis combien de temps le connais-tu ?', 'How long have you known him?')),
        TF('I’ve worked for this company for two years.', ('La personne ne travaille plus dans cette entreprise.', 'The person no longer works for this company.'), FAUX, ('Present perfect + for : elle y travaille encore.', 'Present perfect + for: she still works there.')),
      ]),
  ])])

# ═════════════════════════ Île 5 : Règles et conseils ═════════════════════════
W5 = WORLD('a2-w5', ('Le gué du kelpie', 'The kelpie’s ford'), REGION,
  ('Exprimer l’obligation, l’interdiction et le conseil : must, have to, mustn’t, don’t have to, should.', 'Express obligation, prohibition and advice: must, have to, mustn’t, don’t have to, should.'),
  (('Le Kelpie, cheval des eaux', 'The Kelpie, the water horse'), 'H', ('Ce cheval magique des rivières écossaises entraîne au fond de l’eau ceux qui ignorent les règles. Explique ce qu’on doit, ne doit pas et devrait faire pour traverser le gué sans danger.', 'This magic horse of Scottish rivers drags those who ignore the rules to the bottom of the water. Explain what you must, mustn’t and should do to cross the ford safely.')),
  [CH('a2-w5-c1', ('Les règles', 'Rules'), [
    L('en-must-have-to', ('L’obligation : must, have to', 'Obligation: must, have to'), ('Dire ce qui est obligatoire ou interdit au travail et dans les lieux publics.', 'Say what is compulsory or forbidden at work and in public places.'), 10, [
        ('must + base verbale = obligation forte (souvent écrite ou ressentie) : You must wear a badge. have to = obligation extérieure : I have to work on Saturday.', 'must + base verb = strong obligation (often written or personal): You must wear a badge. have to = external obligation: I have to work on Saturday.'),
        ('mustn’t = interdiction : You mustn’t smoke here. Attention : don’t have to = pas obligé : You don’t have to come (tu n’es pas obligé de venir).', 'mustn’t = prohibition: You mustn’t smoke here. Careful: don’t have to = not necessary: You don’t have to come.'),
        ('Au passé, on utilise had to : I had to wait an hour.', 'In the past, use had to: I had to wait an hour.'),
      ], [
        EG('must', 'must / mustn’t', ('devoir (obligation) / ne pas avoir le droit', 'must / mustn’t')),
        EG('have-to', 'have to / don’t have to', ('devoir / ne pas être obligé de', 'have to / don’t have to')),
        E('wear-badge', 'badge', ('badge', 'badge')),
        E('rule', 'rule', ('règle', 'rule')),
        E('allowed', 'allowed', ('autorisé, permis', 'allowed')),
        E('smoke', 'to smoke', ('fumer', 'to smoke')),
        E('safety', 'safety', ('sécurité', 'safety')),
      ], [
        x('Visitors must wear a badge at all times. You mustn’t take photos in the factory.', 'Les visiteurs doivent porter un badge en permanence. Il est interdit de prendre des photos dans l’usine.'),
        x('You don’t have to wear a tie, but you have to arrive on time.', 'Tu n’es pas obligé de porter une cravate, mais tu dois arriver à l’heure.'),
      ], [
        FB(CHOOSE, 'You ＿ smoke in the building. It’s forbidden.', ['mustn’t', 'don’t have to', 'must'], 'mustn’t', ('Interdiction : mustn’t.', 'Prohibition: mustn’t.'), ('Il est interdit de fumer dans le bâtiment.', 'You mustn’t smoke in the building. It’s forbidden.')),
        FB(CHOOSE, 'It’s Saturday tomorrow. I ＿ get up early.', ['don’t have to', 'mustn’t', 'have'], 'don’t have to', ('Pas obligé : don’t have to.', 'Not necessary: don’t have to.'), ('Demain c’est samedi. Je ne suis pas obligé de me lever tôt.', 'It’s Saturday tomorrow. I don’t have to get up early.')),
        FB(CHOOSE, 'Yesterday I ＿ to wait two hours at the airport.', ['had', 'must', 'have'], 'had', ('Passé de have to : had to.', 'Past of have to: had to.'), ('Hier, j’ai dû attendre deux heures à l’aéroport.', 'Yesterday I had to wait two hours at the airport.')),
        TF('Visitors must wear a badge.', ('Le badge est facultatif.', 'The badge is optional.'), FAUX, ('must = obligatoire.', 'must = compulsory.')),
      ]),
    L('en-should', ('Le conseil : should', 'Advice: should'), ('Donner et demander un conseil avec should.', 'Give and ask for advice with should.'), 9, [
        ('should + base verbale = conseil : You should take a jacket. shouldn’t = conseil négatif : You shouldn’t work so late.', 'should + base verb = advice: You should take a jacket. shouldn’t = negative advice: You shouldn’t work so late.'),
        ('Demander conseil : What should I do? Should I call him? Autres formules : Why don’t you…? / If I were you, I’d…', 'Asking for advice: What should I do? Should I call him? Other phrases: Why don’t you…? / If I were you, I’d…'),
      ], [
        EG('should', 'should / shouldn’t', ('devrais (conseil)', 'should / shouldn’t (advice)')),
        E('advice', 'advice', ('conseil(s)', 'advice')),
        E('rest', 'to rest', ('se reposer', 'to rest')),
        E('careful', 'careful', ('prudent, attentif', 'careful')),
        E('worry', 'to worry', ('s’inquiéter', 'to worry')),
        E('why-dont-you', 'Why don’t you…?', ('Pourquoi tu ne… pas ? (suggestion)', 'Why don’t you…? (suggestion)')),
      ], [
        x('I feel tired all the time. — You should rest more and you shouldn’t drink so much coffee.', 'Je suis tout le temps fatigué. — Tu devrais te reposer davantage et tu ne devrais pas boire autant de café.'),
        x('What should I wear for the interview? — Why don’t you wear your blue suit?', 'Qu’est-ce que je devrais porter pour l’entretien ? — Pourquoi tu ne mets pas ton costume bleu ?'),
      ], [
        FB(CHOOSE, 'You look tired. You ＿ go to bed early.', ['should', 'mustn’t', 'shouldn’t'], 'should', ('Conseil : should.', 'Advice: should.'), ('Tu as l’air fatigué. Tu devrais te coucher tôt.', 'You look tired. You should go to bed early.')),
        FB(CHOOSE, 'You ＿ drive so fast. It’s dangerous.', ['shouldn’t', 'should', 'don’t have'], 'shouldn’t', ('Conseil négatif : shouldn’t.', 'Negative advice: shouldn’t.'), ('Tu ne devrais pas rouler si vite. C’est dangereux.', 'You shouldn’t drive so fast. It’s dangerous.')),
        DC(ANSWER, [('Anna', 'I’ve got a job interview tomorrow. What should I do?')], ('Anna te demande conseil.', 'Anna asks you for advice.'), ['You should prepare some questions.', 'You should to prepare questions.', 'You must prepared questions.'], 'You should prepare some questions.', ('should + base verbale.', 'should + base verb.')),
        TF('Be careful! The floor is wet.', ('Le sol est mouillé : il faut faire attention.', 'The floor is wet: you need to be careful.'), VRAI, ('careful = prudent.', 'careful = paying attention to danger.')),
      ]),
  ]),
  CH('a2-w5-c2', ('La santé', 'Health'), [
    L('en-health', ('Chez le médecin', 'At the doctor’s'), ('Dire où l’on a mal, décrire des symptômes et comprendre des conseils.', 'Say where it hurts, describe symptoms and understand advice.'), 9, [
        ('What’s the matter? / What’s wrong? — I’ve got a headache (mal à la tête), a sore throat (mal à la gorge), a temperature (de la fièvre).', 'What’s the matter? / What’s wrong? — I’ve got a headache, a sore throat, a temperature.'),
        ('My back hurts = j’ai mal au dos. I feel sick = j’ai la nausée (en anglais britannique).', 'My back hurts. I feel sick (= I want to vomit, in British English).'),
        ('Au travail : I’m off sick today = je suis en arrêt maladie aujourd’hui.', 'At work: I’m off sick today = not at work because ill.'),
      ], [
        E('headache', 'headache', ('mal de tête', 'headache')),
        E('sore-throat', 'sore throat', ('mal de gorge', 'sore throat')),
        E('temperature', 'temperature', ('fièvre ; température', 'temperature')),
        E('hurt', 'to hurt', ('faire mal', 'to hurt')),
        E('medicine', 'medicine', ('médicament', 'medicine')),
        E('chemist', 'chemist’s', ('pharmacie', 'chemist’s')),
        E('ill', 'ill', ('malade', 'ill')),
      ], [
        x('What’s the matter? — I’ve got a sore throat and a temperature.', 'Qu’est-ce qui ne va pas ? — J’ai mal à la gorge et de la fièvre.'),
        x('You should take this medicine twice a day. You can buy it at the chemist’s.', 'Prenez ce médicament deux fois par jour. Vous pouvez l’acheter à la pharmacie.'),
      ], [
        DC(ANSWER, [('Doctor', 'What’s the matter?')], ('Le médecin te demande ce qui ne va pas.', 'The doctor asks what the problem is.'), ['I’ve got a headache.', 'I’ve got a doctor.', 'It matters a lot.'], 'I’ve got a headache.', ('What’s the matter? → on décrit le symptôme.', 'What’s the matter? → describe the symptom.')),
        FB(COMPLETE, 'My back ＿. I can’t sit for long.', ['hurts', 'hurt me', 'is hurting me pain'], 'hurts', ('Avoir mal : + hurts.', 'Pain: + hurts.'), ('J’ai mal au dos. Je ne peux pas rester assis longtemps.', 'My back hurts. I can’t sit for long.')),
        FB(COMPLETE, 'Kate isn’t at work. She’s ＿ sick today.', ['off', 'in', 'on'], 'off', ('off sick = en arrêt maladie.', 'off sick = away from work because ill.'), ('Kate n’est pas au travail. Elle est en arrêt maladie aujourd’hui.', 'Kate isn’t at work. She’s off sick today.')),
        TF('You can buy medicine at the chemist’s.', ('On achète des médicaments à la pharmacie.', 'You buy medicine at the pharmacy.'), VRAI, ('chemist’s = pharmacie.', 'chemist’s = pharmacy.')),
      ]),
  ])])

# ═════════════════════════ Île 6 : Quantités et habitudes ═════════════════════════
W6 = WORLD('a2-w6', ('La forêt du chasseur', 'The hunter’s forest'), REGION,
  ('Parler des quantités et de la fréquence, décrire la façon de faire : much / many, a few / a little, les adverbes.', 'Talk about quantities and frequency, describe how things are done: much / many, a few / a little, adverbs.'),
  (('Herne le chasseur', 'Herne the Hunter'), 'E', ('Le chasseur aux bois de cerf de la forêt de Windsor compte ses proies à la lueur de la lune. Dis combien, à quelle fréquence et de quelle manière, sans te tromper, pour qu’il range son arc.', 'The antlered hunter of Windsor Forest counts his prey by moonlight. Say how many, how often and in what way, without a mistake, and he will put away his bow.')),
  [CH('a2-w6-c1', ('Combien ?', 'How much? How many?'), [
    L('en-much-many', ('Beaucoup, peu : much, many, a few, a little', 'Much, many, a few, a little'), ('Exprimer une quantité avec les noms dénombrables et indénombrables.', 'Express quantity with countable and uncountable nouns.'), 10, [
        ('Dénombrables (pluriel) : many, a few (quelques-uns), few (peu). Indénombrables : much, a little (un peu), little (peu).', 'Countable (plural): many, a few, few. Uncountable: much, a little, little.'),
        ('a lot of convient aux deux, surtout dans les phrases affirmatives : a lot of emails, a lot of work.', 'a lot of works with both, especially in affirmative sentences: a lot of emails, a lot of work.'),
        ('Questions : How many people…? How much time / money…?', 'Questions: How many people…? How much time / money…?'),
      ], [
        EG('much-many', 'much / many', ('beaucoup de (indénombrable / dénombrable)', 'much / many')),
        EG('few-little', 'a few / a little', ('quelques / un peu de', 'a few / a little')),
        E('a-lot-of', 'a lot of', ('beaucoup de', 'a lot of')),
        E('time', 'time', ('temps', 'time')),
        E('information', 'information', ('informations, renseignements', 'information')),
        E('furniture', 'furniture', ('meubles, mobilier', 'furniture')),
        E('employee', 'employee', ('employé, employée', 'employee')),
      ], [
        x('How many employees work in the London office? — Not many, about thirty.', 'Combien d’employés travaillent au bureau de Londres ? — Pas beaucoup, une trentaine.'),
        x('We have a little time before the meeting. Can you give me a few minutes?', 'Nous avons un peu de temps avant la réunion. Tu peux m’accorder quelques minutes ?'),
      ], [
        FB(CHOOSE, 'How ＿ money do we need?', ['much', 'many', 'few'], 'much', ('money est indénombrable : much.', 'money is uncountable: much.'), ('De combien d’argent avons-nous besoin ?', 'How much money do we need?')),
        FB(CHOOSE, 'There were ＿ people at the conference.', ['a lot of', 'much', 'a little'], 'a lot of', ('Affirmation + dénombrable : a lot of.', 'Affirmative + countable: a lot of.'), ('Il y avait beaucoup de monde à la conférence.', 'There were a lot of people at the conference.')),
        FB(CHOOSE, 'I need ＿ information about the hotel.', ['some', 'an', 'many'], 'some', ('information est indénombrable : pas de « an ».', 'information is uncountable: no “an”.'), ('J’ai besoin de renseignements sur l’hôtel.', 'I need some information about the hotel.')),
        FB(CHOOSE, 'Can I ask you ＿ questions?', ['a few', 'a little', 'much'], 'a few', ('questions est dénombrable : a few.', 'questions is countable: a few.'), ('Je peux te poser quelques questions ?', 'Can I ask you a few questions?')),
      ]),
    L('en-frequency', ('Combien de fois ? How often', 'How often?'), ('Dire la fréquence d’une habitude.', 'Say how often you do something.'), 9, [
        ('How often do you…? — once a week (une fois par semaine), twice a month (deux fois par mois), three times a year, every other day (un jour sur deux).', 'How often do you…? — once a week, twice a month, three times a year, every other day.'),
        ('Rappel : les adverbes de fréquence se placent avant le verbe, mais après be : I often travel. I’m often late.', 'Reminder: frequency adverbs go before the verb, but after be: I often travel. I’m often late.'),
        ('hardly ever = presque jamais ; rarely = rarement ; often = souvent.', 'hardly ever = almost never; rarely; often.'),
      ], [
        EG('how-often', 'How often…? (once, twice…)', ('À quelle fréquence… ? (une fois, deux fois…)', 'How often…? (frequency)')),
        E('once', 'once', ('une fois', 'once')),
        E('twice', 'twice', ('deux fois', 'twice')),
        E('often', 'often', ('souvent', 'often')),
        E('rarely', 'rarely', ('rarement', 'rarely')),
        E('hardly-ever', 'hardly ever', ('presque jamais', 'hardly ever')),
      ], [
        x('How often do you travel for work? — About twice a month.', 'À quelle fréquence voyages-tu pour le travail ? — Environ deux fois par mois.'),
        x('I’m hardly ever late, but today the train was cancelled.', 'Je ne suis presque jamais en retard, mais aujourd’hui le train a été annulé.'),
      ], [
        DC(ANSWER, [('Herne', 'How often do you go to the gym?')], ('Le chasseur te demande ta fréquence de sport.', 'The hunter asks how often you exercise.'), ['Twice a week.', 'Two times week.', 'Since two weeks.'], 'Twice a week.', ('How often? → once / twice / three times a…', 'How often? → once / twice / three times a…')),
        FB(CHOOSE, 'She ＿ late for meetings.', ['is often', 'often is', 'often be'], 'is often', ('Avec be : adverbe après le verbe.', 'With be: adverb after the verb.'), ('Elle est souvent en retard aux réunions.', 'She is often late for meetings.')),
        FB(CHOOSE, 'We have a team meeting ＿ a week, on Mondays.', ['once', 'one', 'one time of'], 'once', ('Une fois = once.', 'One time = once.'), ('Nous avons une réunion d’équipe une fois par semaine, le lundi.', 'We have a team meeting once a week, on Mondays.')),
        TF('I hardly ever drink coffee.', ('La personne boit beaucoup de café.', 'The person drinks a lot of coffee.'), FAUX, ('hardly ever = presque jamais.', 'hardly ever = almost never.')),
      ]),
  ]),
  CH('a2-w6-c2', ('De quelle manière ?', 'In what way?'), [
    L('en-adverbs', ('Les adverbes de manière : quickly, well', 'Adverbs of manner: quickly, well'), ('Décrire comment on fait les choses avec les adverbes en -ly.', 'Describe how things are done with -ly adverbs.'), 10, [
        ('Adjectif + -ly = adverbe : quick → quickly, careful → carefully, easy → easily. Il décrit le verbe : She speaks clearly.', 'Adjective + -ly = adverb: quick → quickly, careful → carefully, easy → easily. It describes the verb: She speaks clearly.'),
        ('Irréguliers : good → well, fast → fast, hard → hard (hardly veut dire « à peine » !).', 'Irregular: good → well, fast → fast, hard → hard (hardly means “almost not”!).'),
        ('Adjectif après be ou un nom (He’s a careful driver), adverbe après le verbe (He drives carefully).', 'Adjective after be or before a noun (He’s a careful driver), adverb after the verb (He drives carefully).'),
      ], [
        EG('adverbs-ly', '-ly adverb (quickly)', ('adverbe de manière', 'adverb of manner (-ly)')),
        E('quickly', 'quickly', ('rapidement, vite', 'quickly')),
        E('slowly', 'slowly', ('lentement', 'slowly')),
        E('well', 'well', ('bien (adverbe)', 'well (adverb)')),
        E('carefully', 'carefully', ('soigneusement, prudemment', 'carefully')),
        E('clearly', 'clearly', ('clairement', 'clearly')),
        E('hard', 'hard', ('dur (travailler dur) ; difficile', 'hard')),
      ], [
        x('Could you speak more slowly, please? I didn’t understand.', 'Pourriez-vous parler plus lentement, s’il vous plaît ? Je n’ai pas compris.'),
        x('She works hard and she speaks English very well.', 'Elle travaille dur et parle très bien anglais.'),
      ], [
        FB(CHOOSE, 'Please read the contract ＿.', ['carefully', 'careful', 'care'], 'carefully', ('Décrit le verbe read : adverbe.', 'Describes the verb read: adverb.'), ('Veuillez lire le contrat attentivement.', 'Please read the contract carefully.')),
        FB(CHOOSE, 'He speaks Spanish very ＿.', ['well', 'good', 'goodly'], 'well', ('good → well (adverbe irrégulier).', 'good → well (irregular adverb).'), ('Il parle très bien espagnol.', 'He speaks Spanish very well.')),
        FB(CHOOSE, 'She’s a ＿ driver.', ['careful', 'carefully', 'care'], 'careful', ('Avant un nom : adjectif.', 'Before a noun: adjective.'), ('C’est une conductrice prudente.', 'She’s a careful driver.')),
        DC(ANSWER, [('Herne', 'Do you understand me?')], ('Le chasseur parle très vite.', 'The hunter speaks very fast.'), ['Not really. Could you speak more slowly, please?', 'Not really. Could you speak more slow?', 'Yes, you speak slowlier.'], 'Not really. Could you speak more slowly, please?', ('more + adverbe : more slowly.', 'more + adverb: more slowly.')),
      ]),
  ])])

# ═════════════════════════ Île 7 : Si… ═════════════════════════
W7 = WORLD('a2-w7', ('La cour de la reine Mab', 'Queen Mab’s court'), REGION,
  ('Faire des hypothèses réalistes et parler de ses goûts : le premier conditionnel, unless, -ing ou to après un verbe.', 'Make realistic hypotheses and talk about likes: the first conditional, unless, -ing or to after a verb.'),
  (('La reine Mab', 'Queen Mab'), 'F', ('La minuscule reine des fées, qui apporte les rêves, propose des marchés pleins de conditions. Fais des promesses claires pour qu’elle ne te piège pas dans un songe.', 'The tiny fairy queen who brings dreams offers deals full of conditions. Make clear promises so she doesn’t trap you in a dream.')),
  [CH('a2-w7-c1', ('Les conditions', 'Conditions'), [
    L('en-first-conditional', ('Si… : le premier conditionnel', 'If…: the first conditional'), ('Exprimer une condition réaliste et sa conséquence.', 'Express a realistic condition and its result.'), 10, [
        ('If + présent, will + base verbale : If it rains, we’ll stay inside. (Jamais will après if.)', 'If + present, will + base verb: If it rains, we’ll stay inside. (Never will after if.)'),
        ('L’ordre peut s’inverser, sans virgule : We’ll stay inside if it rains.', 'The order can be reversed, without a comma: We’ll stay inside if it rains.'),
        ('unless = if… not (à moins que) : I won’t come unless you invite me.', 'unless = if… not: I won’t come unless you invite me.'),
      ], [
        EG('first-conditional', 'If + present, will…', ('premier conditionnel (condition réaliste)', 'first conditional (if + present, will)')),
        EG('unless', 'unless', ('à moins que, sauf si', 'unless')),
        E('if', 'if', ('si', 'if')),
        E('deal', 'deal', ('marché, accord', 'deal')),
        E('agree', 'to agree', ('être d’accord ; accepter', 'to agree')),
        E('order-buy', 'order', ('commande', 'order (purchase)')),
      ], [
        x('If you sign today, we’ll give you a ten per cent discount.', 'Si vous signez aujourd’hui, nous vous accorderons une remise de dix pour cent.'),
        x('I won’t agree to the deal unless the price goes down.', 'Je n’accepterai pas le marché à moins que le prix baisse.'),
      ], [
        FB(CHOOSE, 'If it ＿ tomorrow, we’ll cancel the picnic.', ['rains', 'will rain', 'rained'], 'rains', ('Après if : présent.', 'After if: present.'), ('S’il pleut demain, nous annulerons le pique-nique.', 'If it rains tomorrow, we’ll cancel the picnic.')),
        FB(CHOOSE, 'If you order now, you ＿ get free delivery.', ['will', 'would', 'are'], 'will', ('Conséquence : will.', 'Result: will.'), ('Si vous commandez maintenant, la livraison sera gratuite.', 'If you order now, you will get free delivery.')),
        FB(CHOOSE, 'We’ll miss the train ＿ we leave now.', ['unless', 'if', 'when'], 'unless', ('à moins que = unless.', 'if not = unless.'), ('Nous allons rater le train à moins de partir maintenant.', 'We’ll miss the train unless we leave now.')),
        order(('Remets dans l’ordre : « S’il est en retard, je l’appellerai. »', 'Put in order: “If he is late, I will call him.”'), ['If', 'he', 'is', 'late,', 'I', 'will', 'call', 'him.'], ('If + présent, will + verbe.', 'If + present, will + verb.')),
      ]),
  ]),
  CH('a2-w7-c2', ('Goûts et envies', 'Likes and wishes'), [
    L('en-ing-to', ('J’aime voyager, je veux partir : -ing ou to', 'I like travelling, I want to go: -ing or to'), ('Choisir entre verbe + -ing et verbe + to.', 'Choose between verb + -ing and verb + to.'), 10, [
        ('Après like, love, enjoy, hate, finish, mind : verbe en -ing. I enjoy travelling. Would you mind closing the window?', 'After like, love, enjoy, hate, finish, mind: verb + -ing. I enjoy travelling. Would you mind closing the window?'),
        ('Après want, would like, need, decide, hope, plan, try : to + base verbale. I want to change jobs. We decided to stay.', 'After want, would like, need, decide, hope, plan, try: to + base verb. I want to change jobs. We decided to stay.'),
        ('Après une préposition, toujours -ing : I’m good at cooking. Thank you for coming.', 'After a preposition, always -ing: I’m good at cooking. Thank you for coming.'),
      ], [
        EG('verb-ing-to', 'verb + -ing / verb + to', ('verbe suivi de -ing ou de to', 'verb + -ing / verb + to')),
        E('enjoy', 'to enjoy', ('apprécier, aimer', 'to enjoy')),
        E('decide', 'to decide', ('décider', 'to decide')),
        E('hope', 'to hope', ('espérer', 'to hope')),
        E('mind', 'to mind', ('voir un inconvénient à', 'to mind')),
        E('hate', 'to hate', ('détester', 'to hate')),
        E('good-at', 'good at', ('doué pour, bon en', 'good at')),
      ], [
        x('I enjoy working with customers, but I hate waiting.', 'J’aime travailler avec les clients, mais je déteste attendre.'),
        x('We decided to open a new shop. We hope to finish it in May.', 'Nous avons décidé d’ouvrir un nouveau magasin. Nous espérons le terminer en mai.'),
      ], [
        FB(CHOOSE, 'I enjoy ＿ new people.', ['meeting', 'to meet', 'meet'], 'meeting', ('enjoy + -ing.', 'enjoy + -ing.'), ('J’aime rencontrer de nouvelles personnes.', 'I enjoy meeting new people.')),
        FB(CHOOSE, 'She decided ＿ the job.', ['to accept', 'accepting', 'accept'], 'to accept', ('decide + to.', 'decide + to.'), ('Elle a décidé d’accepter le poste.', 'She decided to accept the job.')),
        FB(CHOOSE, 'Would you mind ＿ the door?', ['closing', 'to close', 'close'], 'closing', ('mind + -ing.', 'mind + -ing.'), ('Ça vous dérangerait de fermer la porte ?', 'Would you mind closing the door?')),
        FB(CHOOSE, 'Thank you for ＿ me.', ['helping', 'to help', 'help'], 'helping', ('Après une préposition : -ing.', 'After a preposition: -ing.'), ('Merci de m’avoir aidé.', 'Thank you for helping me.')),
      ]),
  ])])

# ═════════════════════════ Île 8 : Le chevalier noir ═════════════════════════
W8 = WORLD('a2-w8', ('Le pont du chevalier noir', 'The Black Knight’s bridge'), REGION,
  ('Décrire et préciser : les pronoms relatifs who, which, that, where, et les pronoms possessifs.', 'Describe and specify: relative pronouns who, which, that, where, and possessive pronouns.'),
  (('Le Chevalier noir', 'The Black Knight'), 'X', ('Il garde un pont et ne laisse passer que ceux qui décrivent exactement les gens, les objets et les lieux. À toi de préciser qui, quoi et où pour gagner ta place à la Table ronde.', 'He guards a bridge and only lets through those who describe people, things and places exactly. Say who, what and where to win your seat at the Round Table.')),
  [CH('a2-w8-c1', ('Qui, que, où', 'Who, which, where'), [
    L('en-relatives', ('Les relatives : who, which, that, where', 'Relative clauses: who, which, that, where'), ('Préciser de qui ou de quoi l’on parle avec un pronom relatif.', 'Make clear who or what you mean with a relative pronoun.'), 10, [
        ('who (ou that) pour une personne : the woman who works in sales. which (ou that) pour une chose : the report which I sent.', 'who (or that) for a person: the woman who works in sales. which (or that) for a thing: the report which I sent.'),
        ('where pour un lieu : the hotel where we stayed. whose pour la possession : the man whose car broke down.', 'where for a place: the hotel where we stayed. whose for possession: the man whose car broke down.'),
        ('Quand le pronom est complément, on peut l’omettre : the report (that) I sent.', 'When the pronoun is the object, it can be left out: the report (that) I sent.'),
      ], [
        EG('relatives', 'who / which / that / where', ('pronoms relatifs (qui, que, où)', 'relative pronouns')),
        E('who-rel', 'who', ('qui', 'who')),
        E('which-rel', 'which', ('qui, que (chose) ; lequel', 'which')),
        E('whose', 'whose', ('dont, à qui', 'whose')),
        E('colleague', 'colleague', ('collègue', 'colleague')),
        E('product', 'product', ('produit', 'product')),
      ], [
        x('The colleague who helped me is from Leeds.', 'Le collègue qui m’a aidé vient de Leeds.'),
        x('That’s the castle where King Arthur was born, or so the story says.', 'C’est le château où le roi Arthur est né, du moins d’après la légende.'),
      ], [
        FB(CHOOSE, 'The woman ＿ called you is the new director.', ['who', 'which', 'where'], 'who', ('Une personne : who.', 'A person: who.'), ('La femme qui t’a appelé est la nouvelle directrice.', 'The woman who called you is the new director.')),
        FB(CHOOSE, 'This is the product ＿ sells best.', ['which', 'who', 'where'], 'which', ('Une chose : which.', 'A thing: which.'), ('C’est le produit qui se vend le mieux.', 'This is the product which sells best.')),
        FB(CHOOSE, 'That’s the restaurant ＿ we had lunch.', ['where', 'which', 'who'], 'where', ('Un lieu : where.', 'A place: where.'), ('C’est le restaurant où nous avons déjeuné.', 'That’s the restaurant where we had lunch.')),
        FB(CHOOSE, 'He’s the client ＿ order was late.', ['whose', 'who', 'which'], 'whose', ('Possession : whose.', 'Possession: whose.'), ('C’est le client dont la commande était en retard.', 'He’s the client whose order was late.')),
      ]),
    L('en-possessive-pronouns', ('À qui est-ce ? mine, yours, theirs', 'Whose is it? mine, yours, theirs'), ('Utiliser les pronoms possessifs et whose.', 'Use possessive pronouns and whose.'), 9, [
        ('Pronoms possessifs (remplacent adjectif + nom) : mine, yours, his, hers, ours, theirs. This bag is mine.', 'Possessive pronouns (replace adjective + noun): mine, yours, his, hers, ours, theirs. This bag is mine.'),
        ('Whose…? = à qui… ? Whose coat is this? — It’s Kate’s / It’s hers.', 'Whose…? asks about the owner. Whose coat is this? — It’s Kate’s / It’s hers.'),
        ('Pronoms compléments : me, you, him, her, us, them. Can you help them?', 'Object pronouns: me, you, him, her, us, them. Can you help them?'),
      ], [
        EG('possessive-pronouns', 'mine / yours / hers / theirs', ('le mien, le tien, le sien, le leur', 'possessive pronouns')),
        EG('object-pronouns', 'me / him / her / us / them', ('pronoms compléments (me, le, la, nous, les)', 'object pronouns')),
        E('hers', 'hers', ('le sien, la sienne (à elle)', 'hers')),
        E('theirs', 'theirs', ('le leur, la leur', 'theirs')),
        E('ours', 'ours', ('le nôtre, la nôtre', 'ours')),
        E('coat', 'coat', ('manteau', 'coat')),
      ], [
        x('Whose umbrella is this? — It isn’t mine. I think it’s hers.', 'À qui est ce parapluie ? — Ce n’est pas le mien. Je crois que c’est le sien.'),
        x('Our office is bigger than theirs, but theirs has a view of the river.', 'Notre bureau est plus grand que le leur, mais le leur a vue sur la rivière.'),
      ], [
        FB(CHOOSE, 'Is this phone yours? — No, it isn’t ＿.', ['mine', 'my', 'me'], 'mine', ('Pronom possessif : mine.', 'Possessive pronoun: mine.'), ('Ce téléphone est à toi ? — Non, ce n’est pas le mien.', 'Is this phone yours? — No, it isn’t mine.')),
        FB(CHOOSE, '＿ car is this? — It’s Tom’s.', ['Whose', 'Who', 'Who’s'], 'Whose', ('À qui… ? = Whose… ?', 'Whose…? asks about the owner.'), ('À qui est cette voiture ? — À Tom.', 'Whose car is this? — It’s Tom’s.')),
        FB(CHOOSE, 'I called Anna and Tom, but I couldn’t reach ＿.', ['them', 'their', 'theirs'], 'them', ('Pronom complément pluriel : them.', 'Plural object pronoun: them.'), ('J’ai appelé Anna et Tom, mais je n’ai pas pu les joindre.', 'I called Anna and Tom, but I couldn’t reach them.')),
        TF('This coat is hers.', ('Le manteau appartient à une femme.', 'The coat belongs to a woman.'), VRAI, ('hers = à elle.', 'hers = belonging to her.')),
      ]),
  ]),
  CH('a2-w8-c2', ('La place à la Table ronde', 'A seat at the Round Table'), [
    L('en-describe-people', ('Décrire quelqu’un', 'Describing people'), ('Décrire l’apparence et le caractère d’une personne.', 'Describe someone’s appearance and personality.'), 9, [
        ('Apparence : What does she look like? — She’s tall, with short dark hair. He’s got a beard.', 'Appearance: What does she look like? — She’s tall, with short dark hair. He’s got a beard.'),
        ('Caractère : What is he like? — He’s friendly, hard-working and very patient.', 'Personality: What is he like? — He’s friendly, hard-working and very patient.'),
        ('Attention : What is she like? (caractère) ≠ What does she like? (goûts).', 'Careful: What is she like? (personality) ≠ What does she like? (tastes).'),
      ], [
        E('look-like', 'to look like', ('ressembler à', 'to look like')),
        E('friendly', 'friendly', ('aimable, sympathique', 'friendly')),
        E('hard-working', 'hard-working', ('travailleur, travailleuse', 'hard-working')),
        E('patient', 'patient', ('patient (caractère)', 'patient (adjective)')),
        E('hair', 'hair', ('cheveux', 'hair')),
        E('beard', 'beard', ('barbe', 'beard')),
        E('shy', 'shy', ('timide', 'shy')),
      ], [
        x('What does your new manager look like? — She’s quite tall, with long red hair.', 'À quoi ressemble ta nouvelle responsable ? — Elle est assez grande, avec de longs cheveux roux.'),
        x('What is Tom like? — He’s a bit shy, but he’s very friendly and hard-working.', 'Comment est Tom ? — Il est un peu timide, mais très sympathique et travailleur.'),
      ], [
        DC(ANSWER, [('Black Knight', 'What is your manager like?')], ('Le chevalier te questionne sur ton responsable.', 'The knight asks about your manager.'), ['He’s friendly and very patient.', 'He likes tea and cake.', 'He’s like a manager.'], 'He’s friendly and very patient.', ('What is he like? → le caractère.', 'What is he like? → personality.')),
        DC(ANSWER, [('Black Knight', 'What does Merlin look like?')], ('Le chevalier te demande à quoi ressemble Merlin.', 'The knight asks what Merlin looks like.'), ['He’s old, with a long grey beard.', 'He looks at the castle.', 'He likes magic.'], 'He’s old, with a long grey beard.', ('look like → l’apparence.', 'look like → appearance.')),
        FB(CHOOSE, 'She’s very ＿. She always helps her colleagues.', ['friendly', 'shy', 'lazy'], 'friendly', ('Qui aide les autres : friendly.', 'Someone who helps others: friendly.'), ('Elle est très sympathique. Elle aide toujours ses collègues.', 'She’s very friendly. She always helps her colleagues.')),
        TF('He’s got a beard and short hair.', ('Il a une barbe.', 'He has a beard.'), VRAI, ('beard = barbe.', 'beard = hair on the chin.')),
      ]),
  ])])

write_level('A2', ('A2 : l’écuyer·ère de la Table ronde', 'A2: squire of the Round Table'), REGION, 'Lands of Logres', 29,
  [W1, W2, W3, W4, W5, W6, W7, W8, FINAL('A2', REGION, ('Simulation TOEIC A2 : l’épreuve de la Table ronde', 'TOEIC A2 simulation: the trial of the Round Table'), 225)], PREVIOUS)
