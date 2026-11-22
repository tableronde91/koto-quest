# Niveau B1 (anglais, CECRL B1, préparation au TOEIC) : 8 îles, 22 leçons et un examen blanc TOEIC (français + anglais).
# Mode histoire : chevalier·ère errant·e en quête du Graal, cheffe ou chef de projet chez Avalon & Co.
# Usage : python3 scripts/b1-level.py   (réécrit content/b1/b1.json)
from en_common import *

REGION = 'Côtes de Cornouailles'

# ═════════════════════════ Île 1 : Le projet en cours ═════════════════════════
W1 = WORLD('b1-w1', ('Le lac de l’Afanc', 'The Afanc’s lake'), REGION,
  ('Faire le point sur un projet en cours : le present perfect continu, et sa différence avec le present perfect simple.', 'Give an update on an ongoing project: the present perfect continuous, and how it differs from the simple present perfect.'),
  (('L’Afanc, monstre du lac', 'The Afanc, the lake monster'), 'A', ('Ce monstre gallois fait déborder les lacs dès qu’on l’agace. Il veut savoir depuis combien de temps tu travailles sur ton projet et ce que tu as déjà accompli.', 'This Welsh monster makes lakes overflow as soon as someone annoys it. It wants to know how long you have been working on your project and what you have already achieved.')),
  [CH('b1-w1-c1', ('Où en est-on ?', 'Where are we?'), [
    L('en-pp-continuous', ('Le present perfect continu : I’ve been working', 'The present perfect continuous: I’ve been working'), ('Parler d’une activité commencée dans le passé qui dure encore.', 'Talk about an activity that started in the past and is still going on.'), 10, [
        ('have / has been + verbe en -ing : action qui a commencé dans le passé et continue (ou vient de s’arrêter) : I’ve been working on this report all morning.', 'have / has been + verb + -ing: an action that started in the past and continues (or has just stopped): I’ve been working on this report all morning.'),
        ('On insiste sur la durée : How long have you been waiting? — For twenty minutes.', 'It stresses duration: How long have you been waiting? — For twenty minutes.'),
        ('Résultat visible : You look tired. — I’ve been running.', 'Visible result: You look tired. — I’ve been running.'),
      ], [
        EG('pp-continuous', 'have been + -ing', ('present perfect continu (durée jusqu’à maintenant)', 'present perfect continuous')),
        E('project', 'project', ('projet', 'project')),
        E('deadline-extend', 'to extend', ('prolonger, repousser (un délai)', 'to extend')),
        E('progress', 'progress', ('avancement, progrès', 'progress')),
        E('update', 'update', ('point d’étape, mise à jour', 'update')),
        E('budget', 'budget', ('budget', 'budget')),
        E('team', 'team', ('équipe', 'team')),
      ], [
        x('We’ve been working on the new website since January.', 'Nous travaillons sur le nouveau site depuis janvier.'),
        x('How long have you been waiting? — For about twenty minutes. The client is late.', 'Depuis combien de temps attends-tu ? — Environ vingt minutes. Le client est en retard.'),
      ], [
        FB(CHOOSE, 'I’ve been ＿ on this report all morning.', ['working', 'worked', 'work'], 'working', ('have been + -ing.', 'have been + -ing.'), ('Je travaille sur ce rapport depuis ce matin.', 'I’ve been working on this report all morning.')),
        FB(CHOOSE, 'How long ＿ you been learning English?', ['have', 'are', 'did'], 'have', ('How long have you been + -ing ?', 'How long have you been + -ing?'), ('Depuis combien de temps apprends-tu l’anglais ?', 'How long have you been learning English?')),
        FB(CHOOSE, 'It ＿ been raining since this morning.', ['has', 'have', 'is'], 'has', ('it → has been.', 'it → has been.'), ('Il pleut depuis ce matin.', 'It has been raining since this morning.')),
        DC(ANSWER, [('Afanc', 'You look exhausted. What have you been doing?')], ('Le monstre remarque ta fatigue.', 'The monster notices how tired you are.'), ['I’ve been preparing the presentation.', 'I’ve prepared since the presentation.', 'I’m been preparing it.'], 'I’ve been preparing the presentation.', ('Résultat visible : I’ve been + -ing.', 'Visible result: I’ve been + -ing.')),
      ]),
    L('en-pp-simple-vs-cont', ('Simple ou continu ?', 'Simple or continuous?'), ('Choisir entre « combien » (simple) et « depuis combien de temps » (continu).', 'Choose between “how many” (simple) and “how long” (continuous).'), 10, [
        ('Present perfect simple = résultat, quantité : I’ve written three emails. Present perfect continu = activité, durée : I’ve been writing emails all day.', 'Simple present perfect = result, quantity: I’ve written three emails. Continuous = activity, duration: I’ve been writing emails all day.'),
        ('Les verbes d’état (know, like, own, believe) ne se mettent pas au continu : I’ve known her for years.', 'State verbs (know, like, own, believe) are not used in the continuous: I’ve known her for years.'),
      ], [
        EG('pp-simple-vs-cont', 'I’ve done / I’ve been doing', ('résultat (simple) / activité en cours (continu)', 'result vs activity (present perfect)')),
        E('achieve', 'to achieve', ('accomplir, atteindre (un objectif)', 'to achieve')),
        E('goal', 'goal', ('objectif, but', 'goal')),
        E('so-far', 'so far', ('jusqu’ici, pour l’instant', 'so far')),
        E('complete', 'to complete', ('terminer, achever', 'to complete')),
        E('stage', 'stage', ('étape, phase', 'stage')),
      ], [
        x('So far we’ve completed two stages of the project.', 'Jusqu’ici, nous avons terminé deux étapes du projet.'),
        x('She’s been calling clients all afternoon and she’s already signed four contracts.', 'Elle appelle des clients depuis le début de l’après-midi et elle a déjà signé quatre contrats.'),
      ], [
        FB(CHOOSE, 'I’ve ＿ five emails since lunch.', ['written', 'been writing', 'writing'], 'written', ('Quantité (cinq) : present perfect simple.', 'Quantity (five): simple present perfect.'), ('J’ai écrit cinq e-mails depuis le déjeuner.', 'I’ve written five emails since lunch.')),
        FB(CHOOSE, 'She’s ＿ the report for three hours and she still hasn’t finished.', ['been writing', 'written', 'wrote'], 'been writing', ('Durée, activité pas finie : continu.', 'Duration, unfinished activity: continuous.'), ('Elle rédige le rapport depuis trois heures et n’a toujours pas fini.', 'She’s been writing the report for three hours and she still hasn’t finished.')),
        FB(CHOOSE, 'I’ve ＿ Mark since university.', ['known', 'been knowing', 'knew'], 'known', ('know est un verbe d’état : pas de continu.', 'know is a state verb: no continuous.'), ('Je connais Mark depuis l’université.', 'I’ve known Mark since university.')),
        TF('So far we’ve achieved all our goals.', ('Tous les objectifs ont été atteints jusqu’à présent.', 'All goals have been reached so far.'), VRAI, ('so far = jusqu’ici.', 'so far = up to now.')),
      ]),
  ]),
  CH('b1-w1-c2', ('Les e-mails professionnels', 'Business emails'), [
    L('en-formal-email', ('Écrire un e-mail professionnel', 'Writing a business email'), ('Ouvrir, structurer et conclure un e-mail formel.', 'Open, structure and close a formal email.'), 9, [
        ('Ouverture : Dear Ms Smith, (nom connu) / Dear Sir or Madam, (inconnu). Objet : I am writing to… (Je vous écris pour…).', 'Opening: Dear Ms Smith, (known name) / Dear Sir or Madam, (unknown). Purpose: I am writing to…'),
        ('Formules utiles : Further to our conversation… (suite à), I would be grateful if you could… (je vous serais reconnaissant de…), Please do not hesitate to contact me.', 'Useful phrases: Further to our conversation…, I would be grateful if you could…, Please do not hesitate to contact me.'),
        ('Clôture : Kind regards / Best regards ; Yours sincerely (avec un nom), Yours faithfully (avec Dear Sir or Madam).', 'Closing: Kind regards / Best regards; Yours sincerely (with a name), Yours faithfully (with Dear Sir or Madam).'),
      ], [
        E('dear', 'Dear…', ('Cher…, Madame, Monsieur (début de lettre)', 'Dear… (letter opening)')),
        E('regards', 'Kind regards', ('Cordialement', 'Kind regards')),
        E('grateful', 'grateful', ('reconnaissant', 'grateful')),
        E('further-to', 'further to', ('suite à', 'further to')),
        E('attach', 'to attach', ('joindre (un fichier)', 'to attach')),
        E('confirm', 'to confirm', ('confirmer', 'to confirm')),
        E('request', 'request', ('demande', 'request')),
      ], [
        x('Dear Ms Taylor, I am writing to confirm our meeting on 12 May.', 'Madame Taylor, je vous écris pour confirmer notre rendez-vous du 12 mai.'),
        x('I would be grateful if you could send me the updated budget. Kind regards, Emma Martin', 'Je vous serais reconnaissante de m’envoyer le budget mis à jour. Cordialement, Emma Martin'),
      ], [
        FB(COMPLETE, 'I am ＿ to confirm the date of the meeting.', ['writing', 'write', 'wrote'], 'writing', ('I am writing to… = je vous écris pour…', 'I am writing to… states the purpose.'), ('Je vous écris pour confirmer la date de la réunion.', 'I am writing to confirm the date of the meeting.')),
        FB(COMPLETE, 'I would be ＿ if you could reply by Friday.', ['grateful', 'great', 'thankful to'], 'grateful', ('I would be grateful if you could… : formule polie.', 'I would be grateful if you could…: polite request.'), ('Je vous serais reconnaissant de répondre d’ici vendredi.', 'I would be grateful if you could reply by Friday.')),
        FB(CHOOSE, 'Dear Sir or Madam, … Yours ＿,', ['faithfully', 'sincerely', 'regards'], 'faithfully', ('Destinataire inconnu : Yours faithfully.', 'Unknown recipient: Yours faithfully.'), ('Madame, Monsieur, … Veuillez agréer…', 'Dear Sir or Madam, … Yours faithfully,')),
        TF('Please find attached the updated budget.', ('Le budget est joint à l’e-mail.', 'The budget is attached to the email.'), VRAI, ('attached = en pièce jointe.', 'attached = sent with the email.')),
      ]),
  ])])

# ═════════════════════════ Île 2 : Autrefois ═════════════════════════
W2 = WORLD('b1-w2', ('Le chat des fées', 'The fairy cat'), REGION,
  ('Raconter une histoire dans l’ordre et évoquer le passé : past perfect, used to, would.', 'Tell a story in order and talk about the past: past perfect, used to, would.'),
  (('Le Cait Sìth, chat des fées', 'The Cait Sìth, the fairy cat'), 'C', ('Ce grand chat noir à tache blanche des Highlands vole les âmes de ceux qui racontent mal leur passé. Remets les événements dans le bon ordre pour qu’il te laisse tranquille.', 'This big black cat with a white patch from the Highlands steals the souls of those who tell their past badly. Put events in the right order and it will leave you alone.')),
  [CH('b1-w2-c1', ('Avant cela', 'Before that'), [
    L('en-past-perfect', ('Le past perfect : I had already left', 'The past perfect: I had already left'), ('Situer une action antérieure à une autre dans le passé.', 'Place an action before another one in the past.'), 10, [
        ('had + participe passé = action antérieure à un autre moment du passé : When I arrived, the meeting had already started.', 'had + past participle = an action before another past moment: When I arrived, the meeting had already started.'),
        ('Comparer : When I arrived, the meeting started (elle commence à mon arrivée) / had started (elle avait déjà commencé).', 'Compare: When I arrived, the meeting started (at that moment) / had started (before I came).'),
        ('Avec before, after, by the time, already, never… before : I had never seen the sea before.', 'With before, after, by the time, already, never… before: I had never seen the sea before.'),
      ], [
        EG('past-perfect', 'had + past participle', ('plus-que-parfait (action antérieure)', 'past perfect (had + past participle)')),
        E('by-the-time', 'by the time', ('le temps que, au moment où', 'by the time')),
        E('already', 'already', ('déjà', 'already')),
        E('realise', 'to realise', ('se rendre compte', 'to realise')),
        E('forget', 'to forget', ('oublier', 'to forget')),
        E('ago-before', 'before', ('avant, auparavant', 'before')),
      ], [
        x('By the time we reached the station, the last train had left.', 'Le temps que nous arrivions à la gare, le dernier train était parti.'),
        x('I realised I had forgotten my passport at the hotel.', 'Je me suis rendu compte que j’avais oublié mon passeport à l’hôtel.'),
      ], [
        FB(CHOOSE, 'When I arrived, the film ＿ already started.', ['had', 'has', 'was'], 'had', ('Antérieur à un moment passé : had + participe.', 'Earlier than a past moment: had + participle.'), ('Quand je suis arrivé, le film avait déjà commencé.', 'When I arrived, the film had already started.')),
        FB(CHOOSE, 'She had never ＿ snow before she moved to Canada.', ['seen', 'saw', 'see'], 'seen', ('had + participe : seen.', 'had + participle: seen.'), ('Elle n’avait jamais vu de neige avant de s’installer au Canada.', 'She had never seen snow before she moved to Canada.')),
        FB(CHOOSE, 'By the time the police arrived, the thieves ＿.', ['had escaped', 'escaped already', 'have escaped'], 'had escaped', ('Avant l’arrivée de la police : past perfect.', 'Before the police arrived: past perfect.'), ('Le temps que la police arrive, les voleurs s’étaient échappés.', 'By the time the police arrived, the thieves had escaped.')),
        TF('When we got there, the shop had closed.', ('Le magasin était fermé à leur arrivée.', 'The shop was closed when they arrived.'), VRAI, ('had closed = avait (déjà) fermé.', 'had closed = closed before they arrived.')),
      ]),
    L('en-used-to', ('Les habitudes passées : used to, would', 'Past habits: used to, would'), ('Décrire ce qui était vrai autrefois et ne l’est plus.', 'Describe what was true in the past and no longer is.'), 10, [
        ('used to + base verbale = habitude ou état passé révolu : I used to live in Leeds (j’habitais à Leeds, plus maintenant).', 'used to + base verb = a past habit or state that is over: I used to live in Leeds.'),
        ('Négation : didn’t use to. Question : Did you use to…?', 'Negative: didn’t use to. Question: Did you use to…?'),
        ('would pour une action répétée (pas un état) dans un récit : Every summer we would go to the seaside. Attention : be used to + -ing = être habitué à.', 'would for a repeated action (not a state) in a story: Every summer we would go to the seaside. Careful: be used to + -ing = be accustomed to.'),
      ], [
        EG('used-to', 'used to / would', ('avoir l’habitude de (dans le passé)', 'used to / would (past habits)')),
        EG('be-used-to', 'be used to + -ing', ('être habitué à', 'be used to + -ing')),
        E('childhood', 'childhood', ('enfance', 'childhood')),
        E('seaside', 'seaside', ('bord de mer', 'seaside')),
        E('anymore', 'anymore', ('ne… plus', 'anymore')),
        E('village', 'village', ('village', 'village')),
      ], [
        x('I used to work in a bank, but I don’t anymore.', 'Avant, je travaillais dans une banque, mais plus maintenant.'),
        x('During my childhood, we would spend every summer at the seaside in Cornwall.', 'Pendant mon enfance, nous passions tous les étés au bord de la mer en Cornouailles.'),
      ], [
        FB(CHOOSE, 'I ＿ smoke, but I stopped five years ago.', ['used to', 'use to', 'was used to'], 'used to', ('Habitude passée : used to.', 'Past habit: used to.'), ('Avant je fumais, mais j’ai arrêté il y a cinq ans.', 'I used to smoke, but I stopped five years ago.')),
        FB(CHOOSE, 'Did you ＿ to live in London?', ['use', 'used', 'using'], 'use', ('Question : Did you use to… ?', 'Question: Did you use to…?'), ('Tu habitais à Londres avant ?', 'Did you use to live in London?')),
        FB(CHOOSE, 'I’m used to ＿ up early. It isn’t a problem.', ['getting', 'get', 'got'], 'getting', ('be used to + -ing = être habitué à.', 'be used to + -ing.'), ('J’ai l’habitude de me lever tôt. Ce n’est pas un problème.', 'I’m used to getting up early. It isn’t a problem.')),
        TF('She used to work in a bank.', ('Elle travaille toujours dans une banque.', 'She still works in a bank.'), FAUX, ('used to = autrefois, plus maintenant.', 'used to = in the past, not now.')),
      ]),
  ]),
  CH('b1-w2-c2', ('Raconter', 'Storytelling'), [
    L('en-narrative', ('Raconter une histoire', 'Telling a story'), ('Enchaîner un récit avec les bons temps et les mots de liaison.', 'Link a story with the right tenses and sequencing words.'), 9, [
        ('Mots de liaison : first, then, after that, later, eventually (finalement), in the end, meanwhile (pendant ce temps).', 'Sequencing words: first, then, after that, later, eventually, in the end, meanwhile.'),
        ('Les temps du récit : prétérit pour les événements, progressif pour le décor, past perfect pour ce qui s’était passé avant.', 'Narrative tenses: past simple for events, continuous for the background, past perfect for what had happened before.'),
        ('Attention : eventually = finalement, au bout du compte (pas « éventuellement » = possibly).', 'Careful: eventually = in the end (French “éventuellement” = possibly).'),
      ], [
        E('eventually', 'eventually', ('finalement, au bout du compte', 'eventually')),
        E('meanwhile', 'meanwhile', ('pendant ce temps', 'meanwhile')),
        E('afterwards', 'afterwards', ('ensuite, après', 'afterwards')),
        E('in-the-end', 'in the end', ('à la fin, en fin de compte', 'in the end')),
        E('happen', 'to happen', ('arriver, se produire', 'to happen')),
        E('story', 'story', ('histoire, récit', 'story')),
      ], [
        x('First, the flight was delayed. Then we lost our luggage. Eventually, we arrived at the hotel at 2 a.m.', 'D’abord, le vol a été retardé. Ensuite, nous avons perdu nos bagages. Finalement, nous sommes arrivés à l’hôtel à 2 heures du matin.'),
        x('Meanwhile, the client had been waiting for us since midnight.', 'Pendant ce temps, le client nous attendait depuis minuit.'),
      ], [
        FB(CHOOSE, 'We waited for hours and ＿ the train arrived.', ['eventually', 'possibly', 'lately'], 'eventually', ('Au bout du compte : eventually.', 'In the end: eventually.'), ('Nous avons attendu des heures et finalement le train est arrivé.', 'We waited for hours and eventually the train arrived.')),
        FB(CHOOSE, 'I was cooking dinner. ＿, my husband was watching TV.', ['Meanwhile', 'Afterwards', 'Eventually'], 'Meanwhile', ('Au même moment : meanwhile.', 'At the same time: meanwhile.'), ('Je préparais le dîner. Pendant ce temps, mon mari regardait la télé.', 'I was cooking dinner. Meanwhile, my husband was watching TV.')),
        DC(ANSWER, [('Cait Sìth', 'What happened on your trip?')], ('Le chat te demande de raconter ton voyage.', 'The cat asks you to tell the story of your trip.'), ['First our flight was cancelled, and then we lost our bags.', 'First our flight cancels, and then we lose.', 'Our flight had been to cancel.'], 'First our flight was cancelled, and then we lost our bags.', ('Récit : prétérit et mots de liaison.', 'Story: past simple and sequencing words.')),
        TF('Eventually, we found the hotel.', ('Ils ont peut-être trouvé l’hôtel.', 'They maybe found the hotel.'), FAUX, ('eventually = finalement (ils l’ont trouvé).', 'eventually = in the end (they did find it).')),
      ]),
  ])])

# ═════════════════════════ Île 3 : Le passif ═════════════════════════
W3 = WORLD('b1-w3', ('Le ver de Lambton', 'The Lambton Worm'), REGION,
  ('Décrire des procédés, des fabrications et des décisions : la voix passive à tous les temps courants.', 'Describe processes, production and decisions: the passive voice in all common tenses.'),
  (('Le ver de Lambton', 'The Lambton Worm'), 'L', ('Ce serpent géant pêché par un jeune noble a grandi dans un puits et s’enroule autour de la colline. Explique comment les choses sont fabriquées et décidées, et il desserrera son étreinte.', 'This giant serpent, fished out by a young nobleman, grew in a well and coils around the hill. Explain how things are made and decided, and it will loosen its grip.')),
  [CH('b1-w3-c1', ('Comment c’est fait', 'How it’s made'), [
    L('en-passive-present', ('Le passif : is made, was built', 'The passive: is made, was built'), ('Former le passif au présent et au passé.', 'Form the passive in the present and the past.'), 10, [
        ('be + participe passé : The cars are made in Sunderland. The bridge was built in 1890.', 'be + past participle: The cars are made in Sunderland. The bridge was built in 1890.'),
        ('On utilise le passif quand l’action compte plus que l’auteur, ou qu’on ne le connaît pas. L’auteur s’introduit par by : The novel was written by Dickens.', 'Use the passive when the action matters more than who did it, or when we don’t know. The agent is introduced by by: The novel was written by Dickens.'),
        ('Négation et question : The invoice wasn’t paid. Where are these phones made?', 'Negative and question: The invoice wasn’t paid. Where are these phones made?'),
      ], [
        EG('passive', 'be + past participle', ('voix passive', 'passive voice (be + past participle)')),
        E('made', 'made', ('fabriqué, fait (participe de make)', 'made')),
        E('built', 'built', ('construit (participe de build)', 'built')),
        E('produce', 'to produce', ('produire, fabriquer', 'to produce')),
        E('deliver', 'to deliver', ('livrer', 'to deliver')),
        E('goods', 'goods', ('marchandises', 'goods')),
        E('warehouse', 'warehouse', ('entrepôt', 'warehouse')),
      ], [
        x('Our tea is grown in India and packed in our factory in Bristol.', 'Notre thé est cultivé en Inde et emballé dans notre usine de Bristol.'),
        x('The goods were delivered to the wrong warehouse.', 'Les marchandises ont été livrées au mauvais entrepôt.'),
      ], [
        FB(CHOOSE, 'These cars ＿ in Sunderland.', ['are made', 'make', 'are making'], 'are made', ('Passif présent : are + participe.', 'Present passive: are + participle.'), ('Ces voitures sont fabriquées à Sunderland.', 'These cars are made in Sunderland.')),
        FB(CHOOSE, 'The castle ＿ in the 12th century.', ['was built', 'built', 'is building'], 'was built', ('Passif passé : was + participe.', 'Past passive: was + participle.'), ('Le château a été construit au XIIe siècle.', 'The castle was built in the 12th century.')),
        FB(CHOOSE, 'The order ＿ delivered yesterday.', ['wasn’t', 'didn’t', 'hasn’t'], 'wasn’t', ('Négation au passif passé : wasn’t + participe.', 'Past passive negative: wasn’t + participle.'), ('La commande n’a pas été livrée hier.', 'The order wasn’t delivered yesterday.')),
        order(('Remets dans l’ordre : « Le rapport a été écrit par Tom. »', 'Put in order: “The report was written by Tom.”'), ['The', 'report', 'was', 'written', 'by', 'Tom.'], ('be + participe + by + auteur.', 'be + participle + by + agent.')),
      ]),
    L('en-passive-other', ('Le passif aux autres temps', 'The passive in other tenses'), ('Passif au present perfect, au futur et avec les modaux.', 'Passive with the present perfect, the future and modals.'), 10, [
        ('Present perfect : has / have been + participe : The contract has been signed. Futur : will be + participe : The results will be announced on Monday.', 'Present perfect: has / have been + participle: The contract has been signed. Future: will be + participle: The results will be announced on Monday.'),
        ('Modaux : must / can / should be + participe : All forms must be completed in English.', 'Modals: must / can / should be + participle: All forms must be completed in English.'),
        ('Progressif : is being + participe : The office is being painted this week.', 'Continuous: is being + participle: The office is being painted this week.'),
      ], [
        EG('passive-perfect-future', 'has been done / will be done', ('passif au present perfect et au futur', 'passive (present perfect, future)')),
        E('announce', 'to announce', ('annoncer', 'to announce')),
        E('cancel', 'to cancel', ('annuler', 'to cancel')),
        E('postpone', 'to postpone', ('reporter, différer', 'to postpone')),
        E('form', 'form', ('formulaire', 'form')),
        E('approve', 'to approve', ('approuver, valider', 'to approve')),
      ], [
        x('The meeting has been postponed until next week.', 'La réunion a été reportée à la semaine prochaine.'),
        x('All expenses must be approved by your manager.', 'Toutes les dépenses doivent être validées par votre responsable.'),
      ], [
        FB(CHOOSE, 'The flight has ＿ cancelled because of the storm.', ['been', 'be', 'being'], 'been', ('has been + participe.', 'has been + participle.'), ('Le vol a été annulé à cause de la tempête.', 'The flight has been cancelled because of the storm.')),
        FB(CHOOSE, 'The winners will ＿ announced tomorrow.', ['be', 'been', 'being'], 'be', ('will be + participe.', 'will be + participle.'), ('Les gagnants seront annoncés demain.', 'The winners will be announced tomorrow.')),
        FB(CHOOSE, 'This form must be ＿ in black ink.', ['completed', 'complete', 'completing'], 'completed', ('must be + participe.', 'must be + participle.'), ('Ce formulaire doit être rempli à l’encre noire.', 'This form must be completed in black ink.')),
        TF('The office is being painted this week.', ('Les travaux de peinture ont lieu cette semaine.', 'The painting is happening this week.'), VRAI, ('is being painted = en train d’être repeint.', 'is being painted = the work is in progress.')),
      ]),
  ]),
  CH('b1-w3-c2', ('Procédures', 'Procedures'), [
    L('en-process', ('Décrire un procédé', 'Describing a process'), ('Expliquer les étapes d’un processus de fabrication ou de commande.', 'Explain the stages of a production or ordering process.'), 9, [
        ('Pour décrire un processus : First, the order is received. Next, it is checked. Then the goods are packed and finally they are shipped.', 'To describe a process: First, the order is received. Next, it is checked. Then the goods are packed and finally they are shipped.'),
        ('Vocabulaire du TOEIC : ship (expédier), stock (stock), supplier (fournisseur), invoice (facture), quality control (contrôle qualité).', 'TOEIC vocabulary: ship, stock, supplier, invoice, quality control.'),
      ], [
        E('ship', 'to ship', ('expédier', 'to ship')),
        E('supplier', 'supplier', ('fournisseur', 'supplier')),
        E('invoice', 'invoice', ('facture', 'invoice')),
        E('stock', 'stock', ('stock', 'stock')),
        E('check', 'to check', ('vérifier', 'to check')),
        E('pack', 'to pack', ('emballer', 'to pack')),
      ], [
        x('Once the order is received, it is checked and packed within 24 hours.', 'Une fois la commande reçue, elle est vérifiée et emballée dans les 24 heures.'),
        x('The invoice is sent to the customer when the goods are shipped.', 'La facture est envoyée au client lorsque les marchandises sont expédiées.'),
      ], [
        FB(CHOOSE, 'First, the orders are ＿ by our team.', ['checked', 'checking', 'check'], 'checked', ('Passif : are + participe.', 'Passive: are + participle.'), ('D’abord, les commandes sont vérifiées par notre équipe.', 'First, the orders are checked by our team.')),
        FB(COMPLETE, 'The goods are ＿ to customers all over Europe.', ['shipped', 'shipping', 'ship'], 'shipped', ('ship → shipped (consonne doublée).', 'ship → shipped (double consonant).'), ('Les marchandises sont expédiées à des clients dans toute l’Europe.', 'The goods are shipped to customers all over Europe.')),
        DC(ANSWER, [('Client', 'When will I receive the invoice?')], ('Un client demande quand il recevra la facture.', 'A client asks when they will receive the invoice.'), ['It will be sent when your order is shipped.', 'It sends when your order ships it.', 'It will send by shipped.'], 'It will be sent when your order is shipped.', ('Passif au futur : will be sent.', 'Future passive: will be sent.')),
        TF('The product is out of stock.', ('Le produit est disponible immédiatement.', 'The product is available immediately.'), FAUX, ('out of stock = en rupture de stock.', 'out of stock = none left.')),
      ]),
  ])])

# ═════════════════════════ Île 4 : Le discours rapporté ═════════════════════════
W4 = WORLD('b1-w4', ('Le nom secret', 'The secret name'), REGION,
  ('Rapporter ce que quelqu’un a dit, demandé ou ordonné : le discours indirect.', 'Report what someone said, asked or told you to do: reported speech.'),
  (('Tom Tit Tot', 'Tom Tit Tot'), 'T', ('Ce petit diable du Suffolk file la laine contre un prix terrible : deviner son nom. Rapporte fidèlement ce que chacun a dit pour découvrir le nom secret.', 'This little Suffolk imp spins wool for a terrible price: guessing his name. Report faithfully what everyone said to discover the secret name.')),
  [CH('b1-w4-c1', ('Il a dit que…', 'He said that…'), [
    L('en-reported-statements', ('Rapporter une déclaration', 'Reporting statements'), ('Passer du discours direct au discours indirect.', 'Change direct speech into reported speech.'), 10, [
        ('say (something) / tell (someone) something : She said (that) she was tired. She told me (that) she was tired.', 'say (something) / tell (someone) something: She said (that) she was tired. She told me (that) she was tired.'),
        ('Les temps reculent d’un cran : am → was, will → would, can → could, has done → had done, did → had done.', 'Tenses move one step back: am → was, will → would, can → could, has done → had done, did → had done.'),
        ('Les repères changent aussi : today → that day, tomorrow → the next day, here → there.', 'Time and place words change too: today → that day, tomorrow → the next day, here → there.'),
      ], [
        EG('reported-speech', 'He said (that)…', ('discours rapporté', 'reported speech')),
        EG('say-tell', 'say / tell', ('dire (quelque chose) / dire (à quelqu’un)', 'say / tell')),
        E('explain', 'to explain', ('expliquer', 'to explain')),
        E('mention', 'to mention', ('mentionner, signaler', 'to mention')),
        E('claim', 'to claim', ('affirmer, prétendre', 'to claim')),
        E('the-next-day', 'the next day', ('le lendemain', 'the next day')),
      ], [
        x('“I’m busy,” said Tom. → Tom said he was busy.', '« Je suis occupé », a dit Tom. → Tom a dit qu’il était occupé.'),
        x('She told me she would send the documents the next day.', 'Elle m’a dit qu’elle enverrait les documents le lendemain.'),
      ], [
        FB(CHOOSE, '“I’m tired,” she said yesterday. → She said she ＿ tired.', ['was', 'is', 'has been'], 'was', ('am → was.', 'am → was.'), ('« Je suis fatiguée. » → Elle a dit qu’elle était fatiguée.', '“I’m tired.” → She said she was tired.')),
        FB(CHOOSE, '“I will call you,” he said on Monday. → He said he ＿ call me.', ['would', 'will', 'can'], 'would', ('will → would.', 'will → would.'), ('« Je t’appellerai. » → Il a dit qu’il m’appellerait.', '“I will call you.” → He said he would call me.')),
        FB(CHOOSE, 'She ＿ me that the meeting was cancelled.', ['told', 'said', 'spoke'], 'told', ('tell + personne.', 'tell + person.'), ('Elle m’a dit que la réunion était annulée.', 'She told me that the meeting was cancelled.')),
        FB(CHOOSE, '“I can help,” he said last week. → He said he ＿ help.', ['could', 'can', 'will'], 'could', ('can → could.', 'can → could.'), ('« Je peux aider. » → Il a dit qu’il pouvait aider.', '“I can help.” → He said he could help.')),
      ]),
    L('en-reported-questions', ('Rapporter une question ou un ordre', 'Reporting questions and orders'), ('Rapporter une question (asked if…) et une consigne (told me to…).', 'Report a question (asked if…) and an instruction (told me to…).'), 10, [
        ('Questions oui/non : if / whether, sans inversion : “Are you ready?” → She asked if I was ready.', 'Yes/no questions: if / whether, no inversion: “Are you ready?” → She asked if I was ready.'),
        ('Questions ouvertes : mot interrogatif + sujet + verbe : “Where do you live?” → He asked where I lived.', 'Open questions: question word + subject + verb: “Where do you live?” → He asked where I lived.'),
        ('Ordres et demandes : tell / ask someone (not) to do : The manager told us to wait. She asked me not to be late.', 'Orders and requests: tell / ask someone (not) to do: The manager told us to wait. She asked me not to be late.'),
      ], [
        EG('reported-questions', 'asked if… / asked where…', ('question rapportée', 'reported questions')),
        EG('told-to', 'told someone to…', ('demander / ordonner de faire', 'told / asked someone to do')),
        E('whether', 'whether', ('si (alternative)', 'whether')),
        E('wonder', 'to wonder', ('se demander', 'to wonder')),
        E('remind', 'to remind', ('rappeler (à quelqu’un)', 'to remind')),
        E('warn', 'to warn', ('avertir, mettre en garde', 'to warn')),
      ], [
        x('The receptionist asked me if I had a reservation.', 'La réceptionniste m’a demandé si j’avais une réservation.'),
        x('My manager reminded me to send the invoice and warned me not to be late again.', 'Ma responsable m’a rappelé d’envoyer la facture et m’a averti de ne plus être en retard.'),
      ], [
        FB(CHOOSE, '“Are you coming?” → She asked ＿ I was coming.', ['if', 'that', 'what'], 'if', ('Question oui/non : if.', 'Yes/no question: if.'), ('« Tu viens ? » → Elle a demandé si je venais.', '“Are you coming?” → She asked if I was coming.')),
        FB(CHOOSE, '“Where do you work?” → He asked where I ＿.', ['worked', 'did work', 'do work'], 'worked', ('Pas d’inversion ni de do : where I worked.', 'No inversion and no do: where I worked.'), ('« Où travailles-tu ? » → Il m’a demandé où je travaillais.', '“Where do you work?” → He asked where I worked.')),
        FB(CHOOSE, 'The doctor told me ＿ more water.', ['to drink', 'drink', 'drinking'], 'to drink', ('tell someone to + verbe.', 'tell someone to + verb.'), ('Le médecin m’a dit de boire plus d’eau.', 'The doctor told me to drink more water.')),
        FB(CHOOSE, 'She asked me ＿ be late.', ['not to', 'to not to', 'don’t'], 'not to', ('Ordre négatif : not to.', 'Negative request: not to.'), ('Elle m’a demandé de ne pas être en retard.', 'She asked me not to be late.')),
      ]),
  ]),
  CH('b1-w4-c2', ('Au téléphone', 'On the phone'), [
    L('en-phone-messages', ('Prendre et laisser un message', 'Taking and leaving messages'), ('Gérer un appel professionnel et transmettre un message.', 'Handle a business call and pass on a message.'), 9, [
        ('Répondre : Good morning, Avalon & Co., Emma speaking. How can I help you?', 'Answering: Good morning, Avalon & Co., Emma speaking. How can I help you?'),
        ('Si la personne est absente : I’m afraid she’s in a meeting. Can I take a message? / Would you like to leave a message?', 'If the person is away: I’m afraid she’s in a meeting. Can I take a message? / Would you like to leave a message?'),
        ('Transmettre : Mr Lee called. He said the delivery would be late and asked you to call him back.', 'Passing it on: Mr Lee called. He said the delivery would be late and asked you to call him back.'),
      ], [
        E('take-message', 'to take a message', ('prendre un message', 'to take a message')),
        E('leave-message', 'to leave a message', ('laisser un message', 'to leave a message')),
        E('speaking', '… speaking', ('… à l’appareil', '… speaking (on the phone)')),
        E('put-through', 'to put someone through', ('passer quelqu’un (au téléphone)', 'to put someone through')),
        E('extension', 'extension', ('poste (téléphonique)', 'extension')),
        E('available', 'available', ('disponible', 'available')),
      ], [
        x('I’m afraid Ms Hall isn’t available at the moment. Would you like to leave a message?', 'Je suis désolé, Mme Hall n’est pas disponible pour le moment. Voulez-vous laisser un message ?'),
        x('Could you put me through to extension 214, please?', 'Pourriez-vous me passer le poste 214, s’il vous plaît ?'),
      ], [
        DC(ANSWER, [('Caller', 'Hello, could I speak to Mr Ambrose, please?')], ('M. Ambrose est en réunion.', 'Mr Ambrose is in a meeting.'), ['I’m afraid he’s in a meeting. Can I take a message?', 'He is meeting. You take message.', 'No, you can’t speak.'], 'I’m afraid he’s in a meeting. Can I take a message?', ('Formule polie + proposition de message.', 'Polite phrase + offer to take a message.')),
        FB(COMPLETE, 'Good morning, Avalon & Co., Emma ＿.', ['speaking', 'talking', 'here is'], 'speaking', ('Au téléphone : prénom + speaking.', 'On the phone: name + speaking.'), ('Bonjour, Avalon & Co., Emma à l’appareil.', 'Good morning, Avalon & Co., Emma speaking.')),
        DC(ANSWER, [('Tom', 'Did anyone call while I was out?')], ('Tom revient de déjeuner ; Mme Lee a appelé.', 'Tom is back from lunch; Ms Lee called.'), ['Yes, Ms Lee called. She asked you to call her back.', 'Yes, Ms Lee calls you back to her.', 'Yes, she said call.'], 'Yes, Ms Lee called. She asked you to call her back.', ('On rapporte la demande : asked you to…', 'Report the request: asked you to…')),
        TF('She isn’t available at the moment.', ('Elle peut prendre l’appel maintenant.', 'She can take the call now.'), FAUX, ('isn’t available = pas disponible.', 'isn’t available = cannot talk now.')),
      ]),
  ])])

# ═════════════════════════ Île 5 : Si j’étais… ═════════════════════════
W5 = WORLD('b1-w5', ('La licorne d’Écosse', 'The unicorn of Scotland'), REGION,
  ('Imaginer et regretter : le deuxième conditionnel, I wish, if I were you.', 'Imagine and regret: the second conditional, I wish, if I were you.'),
  (('La Licorne d’Écosse', 'The Unicorn of Scotland'), 'U', ('L’animal national de l’Écosse, fier et indomptable, ne se laisse approcher que par ceux qui savent rêver. Décris ce que tu ferais si tout était possible.', 'Scotland’s national animal, proud and untameable, only lets dreamers approach. Describe what you would do if anything were possible.')),
  [CH('b1-w5-c1', ('Et si… ?', 'What if…?'), [
    L('en-second-conditional', ('Le deuxième conditionnel : If I had…', 'The second conditional: If I had…'), ('Parler d’une situation imaginaire ou peu probable.', 'Talk about an imaginary or unlikely situation.'), 10, [
        ('If + prétérit, would + base verbale : If I had more time, I would learn Italian. (situation imaginaire au présent)', 'If + past simple, would + base verb: If I had more time, I would learn Italian. (imaginary present situation)'),
        ('Avec be, were est préféré à toutes les personnes : If I were rich, I’d travel the world. If I were you, I’d accept the offer (conseil).', 'With be, were is preferred for all persons: If I were rich, I’d travel the world. If I were you, I’d accept the offer (advice).'),
        ('Comparer : If it rains, I’ll stay (réel, probable) / If it rained, I’d stay (imaginaire).', 'Compare: If it rains, I’ll stay (real, likely) / If it rained, I’d stay (imaginary).'),
      ], [
        EG('second-conditional', 'If + past, would…', ('deuxième conditionnel (hypothèse)', 'second conditional')),
        EG('if-i-were-you', 'If I were you, I’d…', ('À ta place, je…', 'If I were you, I’d… (advice)')),
        E('rich', 'rich', ('riche', 'rich')),
        E('win', 'to win', ('gagner', 'to win')),
        E('lottery', 'lottery', ('loterie', 'lottery')),
        E('imagine', 'to imagine', ('imaginer', 'to imagine')),
        E('offer-accept', 'to accept', ('accepter', 'to accept')),
      ], [
        x('If I won the lottery, I would buy a castle in the Highlands.', 'Si je gagnais au loto, j’achèterais un château dans les Highlands.'),
        x('If I were you, I’d accept the job offer.', 'À ta place, j’accepterais l’offre d’emploi.'),
      ], [
        FB(CHOOSE, 'If I ＿ more money, I would buy a new car.', ['had', 'have', 'would have'], 'had', ('Hypothèse : If + prétérit.', 'Hypothesis: If + past simple.'), ('Si j’avais plus d’argent, j’achèterais une nouvelle voiture.', 'If I had more money, I would buy a new car.')),
        FB(CHOOSE, 'If she lived closer, she ＿ walk to work.', ['would', 'will', 'does'], 'would', ('Conséquence imaginaire : would.', 'Imaginary result: would.'), ('Si elle habitait plus près, elle irait au travail à pied.', 'If she lived closer, she would walk to work.')),
        FB(CHOOSE, 'If I ＿ you, I’d talk to the manager.', ['were', 'am', 'would be'], 'were', ('If I were you : conseil.', 'If I were you: advice.'), ('À ta place, je parlerais au responsable.', 'If I were you, I’d talk to the manager.')),
        TF('If I had a car, I would drive to work.', ('La personne a une voiture.', 'The person has a car.'), FAUX, ('Deuxième conditionnel : situation imaginaire, elle n’en a pas.', 'Second conditional: imaginary, she doesn’t have one.')),
      ]),
    L('en-i-wish', ('Les souhaits et regrets : I wish', 'Wishes and regrets: I wish'), ('Exprimer un souhait sur le présent avec I wish + prétérit.', 'Express a wish about the present with I wish + past simple.'), 9, [
        ('I wish + prétérit = regret sur le présent : I wish I spoke Chinese (je regrette de ne pas parler chinois). I wish I were taller.', 'I wish + past simple = regret about the present: I wish I spoke Chinese. I wish I were taller.'),
        ('I wish + could : I wish I could come to the party.', 'I wish + could: I wish I could come to the party.'),
        ('If only… est plus fort : If only I had more time!', 'If only… is stronger: If only I had more time!'),
      ], [
        EG('i-wish', 'I wish + past simple', ('j’aimerais que… / si seulement…', 'I wish + past simple')),
        E('if-only', 'If only…', ('Si seulement…', 'If only…')),
        E('regret', 'to regret', ('regretter', 'to regret')),
        E('dream', 'dream', ('rêve', 'dream')),
        E('wish', 'wish', ('vœu, souhait', 'wish')),
      ], [
        x('I wish I could stay longer, but my flight leaves tonight.', 'J’aimerais pouvoir rester plus longtemps, mais mon vol part ce soir.'),
        x('If only I knew the answer!', 'Si seulement je connaissais la réponse !'),
      ], [
        FB(CHOOSE, 'I wish I ＿ French fluently.', ['spoke', 'speak', 'will speak'], 'spoke', ('I wish + prétérit.', 'I wish + past simple.'), ('J’aimerais parler couramment français.', 'I wish I spoke French fluently.')),
        FB(CHOOSE, 'I wish I ＿ come to your wedding.', ['could', 'can', 'will'], 'could', ('I wish + could.', 'I wish + could.'), ('J’aimerais pouvoir venir à ton mariage.', 'I wish I could come to your wedding.')),
        DC(ANSWER, [('Unicorn', 'What is your dream?')], ('La licorne t’interroge sur ton rêve.', 'The unicorn asks about your dream.'), ['If I could, I’d travel around the world.', 'If I can, I travelled the world.', 'I will wish to travelled.'], 'If I could, I’d travel around the world.', ('Rêve : If I could, I’d…', 'Dream: If I could, I’d…')),
        TF('I wish I had more time.', ('La personne a beaucoup de temps libre.', 'The person has a lot of free time.'), FAUX, ('I wish I had… : elle n’en a pas assez.', 'I wish I had…: she doesn’t have enough.')),
      ]),
  ]),
  CH('b1-w5-c2', ('Le monde du travail', 'The world of work'), [
    L('en-job-interview', ('L’entretien d’embauche', 'The job interview'), ('Répondre aux questions classiques d’un entretien.', 'Answer the classic questions of a job interview.'), 9, [
        ('Questions fréquentes : Tell me about yourself. Why do you want this job? What are your strengths and weaknesses? Where do you see yourself in five years?', 'Common questions: Tell me about yourself. Why do you want this job? What are your strengths and weaknesses? Where do you see yourself in five years?'),
        ('Vocabulaire : apply for a job (postuler), a candidate, a CV (en américain : résumé), skills (compétences), salary, a position (un poste).', 'Vocabulary: apply for a job, a candidate, a CV (American: résumé), skills, salary, a position.'),
      ], [
        E('apply', 'to apply for', ('postuler à, candidater', 'to apply for')),
        E('candidate', 'candidate', ('candidat, candidate', 'candidate')),
        E('skills', 'skills', ('compétences', 'skills')),
        E('strength', 'strength', ('point fort, force', 'strength')),
        E('weakness', 'weakness', ('point faible, faiblesse', 'weakness')),
        E('position', 'position', ('poste (emploi)', 'position (job)')),
        E('salary', 'salary', ('salaire', 'salary')),
      ], [
        x('I’m applying for the position of sales manager.', 'Je postule au poste de responsable des ventes.'),
        x('What are your main strengths? — I’m organised and I work well in a team.', 'Quels sont vos principaux points forts ? — Je suis organisée et je travaille bien en équipe.'),
      ], [
        FB(COMPLETE, 'I would like to apply ＿ the position of assistant.', ['for', 'to', 'at'], 'for', ('apply for a job.', 'apply for a job.'), ('Je souhaite postuler au poste d’assistant.', 'I would like to apply for the position of assistant.')),
        DC(ANSWER, [('Interviewer', 'Why do you want to work for us?')], ('Question d’entretien.', 'An interview question.'), ['Because your company is a leader in its field.', 'Because I want salary.', 'Yes, I want.'], 'Because your company is a leader in its field.', ('Une réponse motivée et polie.', 'A motivated, polite answer.')),
        DC(ANSWER, [('Interviewer', 'What is your biggest weakness?')], ('Question piège classique.', 'A classic tricky question.'), ['Sometimes I spend too long on details, but I’m working on it.', 'I don’t have weakness never.', 'My weakness is weak.'], 'Sometimes I spend too long on details, but I’m working on it.', ('Un vrai défaut, et ce qu’on fait pour progresser.', 'A real weakness, and how you are improving.')),
        TF('She has the right skills for the position.', ('Elle a les compétences pour le poste.', 'She is qualified for the job.'), VRAI, ('skills = compétences.', 'skills = abilities.')),
      ]),
  ])])

# ═════════════════════════ Île 6 : Déductions ═════════════════════════
W6 = WORLD('b1-w6', ('L’homme-hibou', 'The Owlman'), REGION,
  ('Faire des déductions et parler de possibilités : must, might, may, could, can’t.', 'Make deductions and talk about possibility: must, might, may, could, can’t.'),
  (('L’Homme-hibou de Mawnan', 'The Owlman of Mawnan'), 'O', ('Cette créature mi-homme mi-hibou qui hante le clocher de Mawnan pose des énigmes. Déduis avec logique ce qui est certain, possible ou impossible.', 'This half-man, half-owl creature that haunts Mawnan church tower asks riddles. Deduce logically what is certain, possible or impossible.')),
  [CH('b1-w6-c1', ('Certain ou possible ?', 'Certain or possible?'), [
    L('en-deduction', ('Les déductions : must, might, can’t', 'Deductions: must, might, can’t'), ('Exprimer la certitude ou le doute sur le présent.', 'Express certainty or doubt about the present.'), 10, [
        ('must be = sûrement (presque certain) : She must be at home — her car is outside.', 'must be = almost certain: She must be at home — her car is outside.'),
        ('might / may / could be = peut-être : He might be in a meeting.', 'might / may / could be = perhaps: He might be in a meeting.'),
        ('can’t be = impossible : That can’t be Tom — he’s in Paris today.', 'can’t be = impossible: That can’t be Tom — he’s in Paris today.'),
      ], [
        EG('deduction', 'must be / might be / can’t be', ('doit être / est peut-être / ne peut pas être', 'modals of deduction')),
        E('might', 'might', ('pourrait (peut-être)', 'might')),
        E('may', 'may', ('pourrait, peut (éventualité, permission)', 'may')),
        E('certain', 'certain', ('certain, sûr', 'certain')),
        E('perhaps', 'perhaps', ('peut-être', 'perhaps')),
        E('impossible', 'impossible', ('impossible', 'impossible')),
      ], [
        x('The lights are off. They must be on holiday.', 'Les lumières sont éteintes. Ils doivent être en vacances.'),
        x('That can’t be the right address. There’s no office here.', 'Ça ne peut pas être la bonne adresse. Il n’y a aucun bureau ici.'),
      ], [
        FB(CHOOSE, 'He’s been working for twelve hours. He ＿ be exhausted.', ['must', 'can’t', 'mustn’t'], 'must', ('Déduction logique : must.', 'Logical deduction: must.'), ('Il travaille depuis douze heures. Il doit être épuisé.', 'He’s been working for twelve hours. He must be exhausted.')),
        FB(CHOOSE, 'That ＿ be Kate. She’s in Japan this week.', ['can’t', 'must', 'might'], 'can’t', ('Impossible : can’t.', 'Impossible: can’t.'), ('Ça ne peut pas être Kate. Elle est au Japon cette semaine.', 'That can’t be Kate. She’s in Japan this week.')),
        FB(CHOOSE, 'Take an umbrella. It ＿ rain later.', ['might', 'must', 'can’t'], 'might', ('Possibilité : might.', 'Possibility: might.'), ('Prends un parapluie. Il pourrait pleuvoir plus tard.', 'Take an umbrella. It might rain later.')),
        TF('She must be at home; her car is outside.', ('La personne en est presque sûre.', 'The speaker is almost sure.'), VRAI, ('must be = presque certain.', 'must be = almost certain.')),
      ]),
    L('en-deduction-past', ('Déductions sur le passé : must have done', 'Past deductions: must have done'), ('Faire une hypothèse sur ce qui s’est passé.', 'Make a guess about what happened.'), 10, [
        ('modal + have + participe passé : He must have missed the train (il a dû rater le train). She might have forgotten. They can’t have finished already.', 'modal + have + past participle: He must have missed the train. She might have forgotten. They can’t have finished already.'),
        ('should have done = aurait dû (reproche) : You should have told me!', 'should have done = criticism: You should have told me!'),
      ], [
        EG('must-have-done', 'must / might / can’t have done', ('a dû / a peut-être / n’a pas pu (passé)', 'past modals of deduction')),
        EG('should-have', 'should have done', ('aurait dû', 'should have done')),
        E('mistake', 'mistake', ('erreur', 'mistake')),
        E('guess', 'to guess', ('deviner', 'to guess')),
        E('clue', 'clue', ('indice', 'clue')),
        E('missing', 'missing', ('manquant, disparu', 'missing')),
      ], [
        x('Mark isn’t here yet. He must have missed his train.', 'Mark n’est pas encore là. Il a dû rater son train.'),
        x('You should have told me about the problem earlier.', 'Tu aurais dû me parler du problème plus tôt.'),
      ], [
        FB(CHOOSE, 'The window is broken. Someone must have ＿ it.', ['broken', 'broke', 'break'], 'broken', ('must have + participe.', 'must have + participle.'), ('La fenêtre est cassée. Quelqu’un a dû la casser.', 'The window is broken. Someone must have broken it.')),
        FB(CHOOSE, 'She ＿ have finished already — she only started an hour ago.', ['can’t', 'must', 'should'], 'can’t', ('Impossible dans le passé : can’t have.', 'Impossible in the past: can’t have.'), ('Elle ne peut pas avoir déjà fini — elle a commencé il y a une heure.', 'She can’t have finished already — she only started an hour ago.')),
        FB(CHOOSE, 'You ＿ have booked a table. The restaurant is full.', ['should', 'must', 'can'], 'should', ('Reproche : should have.', 'Criticism: should have.'), ('Tu aurais dû réserver une table. Le restaurant est complet.', 'You should have booked a table. The restaurant is full.')),
        DC(ANSWER, [('Owlman', 'The keys are missing. What happened?')], ('L’homme-hibou te pose une énigme.', 'The Owlman gives you a riddle.'), ['Someone might have taken them.', 'Someone might took them.', 'Someone must taking them.'], 'Someone might have taken them.', ('might have + participe.', 'might have + participle.')),
      ]),
  ]),
  CH('b1-w6-c2', ('Les problèmes', 'Problems'), [
    L('en-complaints', ('Se plaindre poliment', 'Complaining politely'), ('Formuler une réclamation et y répondre.', 'Make a complaint and respond to one.'), 9, [
        ('Se plaindre : I’m afraid there seems to be a problem with… / I’m not satisfied with… / I’d like to make a complaint.', 'Complaining: I’m afraid there seems to be a problem with… / I’m not satisfied with… / I’d like to make a complaint.'),
        ('Répondre : I’m very sorry about that. / I apologise for the inconvenience. / We’ll replace it immediately. / We’ll give you a full refund.', 'Responding: I’m very sorry about that. / I apologise for the inconvenience. / We’ll replace it immediately. / We’ll give you a full refund.'),
      ], [
        E('complaint', 'complaint', ('plainte, reproche', 'complaint')),
        E('apologise', 'to apologise', ('s’excuser', 'to apologise')),
        E('inconvenience', 'inconvenience', ('désagrément, gêne', 'inconvenience')),
        E('replace', 'to replace', ('remplacer', 'to replace')),
        E('damaged', 'damaged', ('endommagé, abîmé', 'damaged')),
        E('satisfied', 'satisfied', ('satisfait', 'satisfied')),
      ], [
        x('I’m afraid the laptop I ordered arrived damaged.', 'Je suis désolé, mais l’ordinateur portable que j’ai commandé est arrivé abîmé.'),
        x('We apologise for the inconvenience and will replace it free of charge.', 'Nous vous prions de nous excuser pour ce désagrément et le remplacerons gratuitement.'),
      ], [
        DC(ANSWER, [('Customer', 'The printer I bought last week doesn’t work.')], ('Un client se plaint.', 'A customer complains.'), ['I’m very sorry. We’ll replace it immediately.', 'It’s not my printer.', 'You must have broken it, so no.'], 'I’m very sorry. We’ll replace it immediately.', ('S’excuser et proposer une solution.', 'Apologise and offer a solution.')),
        FB(COMPLETE, 'We apologise for the ＿ caused by the delay.', ['inconvenience', 'convenient', 'complain'], 'inconvenience', ('apologise for the inconvenience.', 'apologise for the inconvenience.'), ('Nous vous prions de nous excuser pour le désagrément causé par ce retard.', 'We apologise for the inconvenience caused by the delay.')),
        FB(COMPLETE, 'I’d like to make a ＿ about the service.', ['complaint', 'complain', 'complaining'], 'complaint', ('Nom : complaint.', 'Noun: complaint.'), ('Je voudrais faire une réclamation concernant le service.', 'I’d like to make a complaint about the service.')),
        TF('The parcel arrived damaged.', ('Le colis est arrivé en bon état.', 'The parcel arrived in good condition.'), FAUX, ('damaged = abîmé.', 'damaged = broken, harmed.')),
      ]),
  ])])

# ═════════════════════════ Île 7 : Débattre ═════════════════════════
W7 = WORLD('b1-w7', ('Les dragons de Vortigern', 'Vortigern’s dragons'), REGION,
  ('Donner son avis, nuancer et relier ses idées : although, however, despite, so… that, in order to.', 'Give opinions, qualify them and link ideas: although, however, despite, so… that, in order to.'),
  (('Les dragons de Vortigern', 'Vortigern’s dragons'), 'V', ('Sous la tour du roi Vortigern, un dragon rouge et un dragon blanc se battent sans fin. Argumente avec nuance pour mettre fin à leur querelle.', 'Beneath King Vortigern’s tower, a red dragon and a white dragon fight endlessly. Argue with nuance to end their quarrel.')),
  [CH('b1-w7-c1', ('En réunion', 'In a meeting'), [
    L('en-opinions', ('Donner son avis, être d’accord ou non', 'Giving opinions, agreeing and disagreeing'), ('Participer à une discussion en réunion.', 'Take part in a discussion in a meeting.'), 9, [
        ('Donner son avis : In my opinion… / I think… / As far as I’m concerned… / If you ask me…', 'Giving an opinion: In my opinion… / I think… / As far as I’m concerned… / If you ask me…'),
        ('Être d’accord : I agree with you. / That’s a good point. / Exactly. Ne pas l’être, poliment : I see your point, but… / I’m not sure I agree.', 'Agreeing: I agree with you. / That’s a good point. / Exactly. Disagreeing politely: I see your point, but… / I’m not sure I agree.'),
        ('Attention : I agree (pas « I am agree »).', 'Careful: I agree (not “I am agree”).'),
      ], [
        E('opinion', 'opinion', ('opinion, avis', 'opinion')),
        E('agree-with', 'to agree with', ('être d’accord avec', 'to agree with')),
        E('disagree', 'to disagree', ('ne pas être d’accord', 'to disagree')),
        E('point', 'point', ('argument, remarque', 'point (argument)')),
        E('suggest', 'to suggest', ('suggérer, proposer', 'to suggest')),
        E('meeting-agenda', 'agenda', ('ordre du jour', 'agenda')),
      ], [
        x('In my opinion, we should launch the product in spring.', 'À mon avis, nous devrions lancer le produit au printemps.'),
        x('I see your point, but I’m not sure the budget is big enough.', 'Je comprends ton argument, mais je ne suis pas sûr que le budget soit suffisant.'),
      ], [
        FB(CHOOSE, 'I ＿ with you. It’s a great idea.', ['agree', 'am agree', 'agreeing'], 'agree', ('I agree (verbe, sans am).', 'I agree (verb, no am).'), ('Je suis d’accord avec toi. C’est une excellente idée.', 'I agree with you. It’s a great idea.')),
        DC(ANSWER, [('Red dragon', 'We should cut the budget by half.')], ('Tu n’es pas d’accord, mais tu restes poli.', 'You disagree, but you stay polite.'), ['I see your point, but that might be too much.', 'You are wrong and stupid.', 'I am agree no.'], 'I see your point, but that might be too much.', ('Désaccord poli : I see your point, but…', 'Polite disagreement: I see your point, but…')),
        FB(COMPLETE, 'The first item on the ＿ is the budget.', ['agenda', 'diary', 'calendar'], 'agenda', ('Ordre du jour = agenda.', 'List of topics for a meeting = agenda.'), ('Le premier point à l’ordre du jour est le budget.', 'The first item on the agenda is the budget.')),
        TF('In my opinion, the price is too high.', ('La personne donne son avis.', 'The person gives their opinion.'), VRAI, ('In my opinion = à mon avis.', 'In my opinion = what I think.')),
      ]),
    L('en-contrast', ('Nuancer : although, however, despite', 'Contrast: although, however, despite'), ('Opposer deux idées avec les connecteurs de contraste.', 'Contrast two ideas with linking words.'), 10, [
        ('although / even though + sujet + verbe : Although it was raining, we went out.', 'although / even though + subject + verb: Although it was raining, we went out.'),
        ('despite / in spite of + nom ou -ing : Despite the rain, we went out. Despite being tired, she finished.', 'despite / in spite of + noun or -ing: Despite the rain, we went out. Despite being tired, she finished.'),
        ('however en début de phrase, suivi d’une virgule : The product is good. However, it’s too expensive.', 'however at the start of a sentence, followed by a comma: The product is good. However, it’s too expensive.'),
      ], [
        EG('although-despite', 'although / despite / however', ('bien que / malgré / cependant', 'although / despite / however')),
        E('although', 'although', ('bien que, même si', 'although')),
        E('despite', 'despite', ('malgré', 'despite')),
        E('however', 'however', ('cependant, toutefois', 'however')),
        E('whereas', 'whereas', ('alors que, tandis que', 'whereas')),
        E('advantage', 'advantage', ('avantage', 'advantage')),
        E('drawback', 'drawback', ('inconvénient', 'drawback')),
      ], [
        x('Although the hotel was expensive, it was worth it.', 'Bien que l’hôtel soit cher, il en valait la peine.'),
        x('Despite the delay, the project was a success. However, we went over budget.', 'Malgré le retard, le projet a été un succès. Cependant, nous avons dépassé le budget.'),
      ], [
        FB(CHOOSE, '＿ the bad weather, the event was a success.', ['Despite', 'Although', 'However'], 'Despite', ('+ nom : despite.', '+ noun: despite.'), ('Malgré le mauvais temps, l’événement a été un succès.', 'Despite the bad weather, the event was a success.')),
        FB(CHOOSE, '＿ she was tired, she finished the report.', ['Although', 'Despite', 'However'], 'Although', ('+ sujet + verbe : although.', '+ subject + verb: although.'), ('Bien qu’elle soit fatiguée, elle a terminé le rapport.', 'Although she was tired, she finished the report.')),
        FB(CHOOSE, 'The plan is good. ＿, it’s very expensive.', ['However', 'Although', 'Despite'], 'However', ('Début de phrase + virgule : however.', 'Start of sentence + comma: however.'), ('Le plan est bon. Cependant, il est très cher.', 'The plan is good. However, it’s very expensive.')),
        TF('One drawback of the plan is the cost.', ('Le coût est un inconvénient du plan.', 'The cost is a disadvantage of the plan.'), VRAI, ('drawback = inconvénient.', 'drawback = disadvantage.')),
      ]),
  ]),
  CH('b1-w7-c2', ('Le but et la conséquence', 'Purpose and result'), [
    L('en-purpose-result', ('Pour, si… que : in order to, so that, so… that', 'Purpose and result: in order to, so that, so… that'), ('Exprimer le but et la conséquence.', 'Express purpose and result.'), 10, [
        ('But : to / in order to + verbe : I called in order to confirm. so that + sujet + can/will : I left early so that I could catch the train.', 'Purpose: to / in order to + verb: I called in order to confirm. so that + subject + can/will: I left early so that I could catch the train.'),
        ('Conséquence : so + adjectif + that / such + (a) + nom + that : It was so hot that we stayed inside. It was such a good offer that we accepted.', 'Result: so + adjective + that / such + (a) + noun + that: It was so hot that we stayed inside. It was such a good offer that we accepted.'),
      ], [
        EG('purpose', 'in order to / so that', ('pour, afin de / pour que', 'in order to / so that')),
        EG('so-such', 'so… that / such… that', ('si… que / tellement… que', 'so… that / such… that')),
        E('in-order-to', 'in order to', ('pour, afin de', 'in order to')),
        E('therefore', 'therefore', ('par conséquent', 'therefore')),
        E('reduce', 'to reduce', ('réduire', 'to reduce')),
        E('increase', 'to increase', ('augmenter', 'to increase')),
      ], [
        x('We changed suppliers in order to reduce costs.', 'Nous avons changé de fournisseur afin de réduire les coûts.'),
        x('It was such a good presentation that the client signed immediately.', 'La présentation était si bonne que le client a signé immédiatement.'),
      ], [
        FB(CHOOSE, 'I’m saving money ＿ buy a house.', ['in order to', 'so that', 'for'], 'in order to', ('But + verbe : in order to.', 'Purpose + verb: in order to.'), ('J’économise pour acheter une maison.', 'I’m saving money in order to buy a house.')),
        FB(CHOOSE, 'The film was ＿ boring that I fell asleep.', ['so', 'such', 'too'], 'so', ('so + adjectif + that.', 'so + adjective + that.'), ('Le film était si ennuyeux que je me suis endormi.', 'The film was so boring that I fell asleep.')),
        FB(CHOOSE, 'It was ＿ a long meeting that everyone was tired.', ['such', 'so', 'very'], 'such', ('such + a + nom.', 'such + a + noun.'), ('C’était une réunion si longue que tout le monde était fatigué.', 'It was such a long meeting that everyone was tired.')),
        FB(CHOOSE, 'Sales fell. ＿, we must reduce costs.', ['Therefore', 'Although', 'Despite'], 'Therefore', ('Conséquence : therefore.', 'Result: therefore.'), ('Les ventes ont baissé. Par conséquent, nous devons réduire les coûts.', 'Sales fell. Therefore, we must reduce costs.')),
      ]),
  ])])

# ═════════════════════════ Île 8 : Le roi gris ═════════════════════════
W8 = WORLD('b1-w8', ('Le roi des brumes', 'The king of the mists'), REGION,
  ('Être poli et précis dans les échanges professionnels : questions indirectes, question tags, demandes formelles.', 'Be polite and precise in business exchanges: indirect questions, question tags, formal requests.'),
  (('Y Brenin Llwyd, le roi gris', 'Y Brenin Llwyd, the Grey King'), 'Y', ('Le roi des brumes des montagnes galloises enveloppe les voyageurs impolis dans un brouillard éternel. Demande ton chemin vers le Graal avec la plus grande politesse.', 'The king of the mists of the Welsh mountains wraps rude travellers in an eternal fog. Ask your way to the Grail with the utmost politeness.')),
  [CH('b1-w8-c1', ('Poliment', 'Politely'), [
    L('en-indirect-questions', ('Les questions indirectes', 'Indirect questions'), ('Poser une question de façon plus polie avec Could you tell me… ?', 'Ask a question more politely with Could you tell me…?'), 10, [
        ('Formule d’introduction + ordre normal sujet-verbe : Where is the station? → Could you tell me where the station is?', 'Introductory phrase + normal subject-verb order: Where is the station? → Could you tell me where the station is?'),
        ('Pas de do / does / did : What time does it open? → Do you know what time it opens?', 'No do / does / did: What time does it open? → Do you know what time it opens?'),
        ('Question oui/non : if / whether : Is it free? → I was wondering if it was free.', 'Yes/no question: if / whether: Is it free? → I was wondering if it was free.'),
      ], [
        EG('indirect-questions', 'Could you tell me where… is?', ('question indirecte (polie)', 'indirect questions')),
        E('wondering', 'I was wondering if…', ('Je me demandais si… (demande polie)', 'I was wondering if… (polite request)')),
        E('direction', 'directions', ('indications (pour trouver un lieu)', 'directions')),
        E('open-hours', 'opening hours', ('horaires d’ouverture', 'opening hours')),
        E('reception', 'reception', ('accueil, réception', 'reception')),
      ], [
        x('Could you tell me where the conference room is?', 'Pourriez-vous me dire où se trouve la salle de conférence ?'),
        x('I was wondering if you could help me with this form.', 'Je me demandais si vous pourriez m’aider avec ce formulaire.'),
      ], [
        FB(CHOOSE, 'Could you tell me where the toilets ＿?', ['are', 'are they', 'do'], 'are', ('Question indirecte : ordre sujet + verbe.', 'Indirect question: subject + verb.'), ('Pourriez-vous me dire où sont les toilettes ?', 'Could you tell me where the toilets are?')),
        FB(CHOOSE, 'Do you know what time the shop ＿?', ['opens', 'does open', 'open'], 'opens', ('Pas de does dans une question indirecte.', 'No does in an indirect question.'), ('Savez-vous à quelle heure ouvre le magasin ?', 'Do you know what time the shop opens?')),
        FB(CHOOSE, 'I was wondering ＿ you could help me.', ['if', 'that', 'what'], 'if', ('Question oui/non : if.', 'Yes/no question: if.'), ('Je me demandais si vous pourriez m’aider.', 'I was wondering if you could help me.')),
        order(('Remets dans l’ordre : « Savez-vous où il habite ? »', 'Put in order: “Do you know where he lives?”'), ['Do', 'you', 'know', 'where', 'he', 'lives?'], ('Question indirecte : sujet + verbe.', 'Indirect question: subject + verb.')),
      ]),
    L('en-question-tags', ('Les question tags : isn’t it?', 'Question tags: isn’t it?'), ('Vérifier une information ou relancer la conversation.', 'Check information or keep the conversation going.'), 10, [
        ('Phrase affirmative → tag négatif : It’s cold, isn’t it? Phrase négative → tag affirmatif : You don’t eat meat, do you?', 'Affirmative sentence → negative tag: It’s cold, isn’t it? Negative sentence → affirmative tag: You don’t eat meat, do you?'),
        ('Le tag reprend l’auxiliaire : You’ve finished, haven’t you? She can swim, can’t she? He works here, doesn’t he?', 'The tag repeats the auxiliary: You’ve finished, haven’t you? She can swim, can’t she? He works here, doesn’t he?'),
        ('Exception : I’m late, aren’t I?', 'Exception: I’m late, aren’t I?'),
      ], [
        EG('question-tags', 'question tags (isn’t it?)', ('n’est-ce pas ? (question tag)', 'question tags')),
        E('isnt-it', 'isn’t it?', ('n’est-ce pas ?', 'isn’t it?')),
        E('lovely', 'lovely', ('charmant, très agréable', 'lovely')),
        E('weather-nice', 'nice', ('agréable, sympa', 'nice')),
      ], [
        x('It’s a lovely day, isn’t it? — Yes, it is!', 'Il fait un temps magnifique, n’est-ce pas ? — Oui !'),
        x('You haven’t seen my keys, have you?', 'Tu n’aurais pas vu mes clés, par hasard ?'),
      ], [
        FB(CHOOSE, 'It’s cold today, ＿?', ['isn’t it', 'is it', 'doesn’t it'], 'isn’t it', ('Affirmatif → tag négatif.', 'Affirmative → negative tag.'), ('Il fait froid aujourd’hui, n’est-ce pas ?', 'It’s cold today, isn’t it?')),
        FB(CHOOSE, 'You don’t like coffee, ＿?', ['do you', 'don’t you', 'are you'], 'do you', ('Négatif → tag affirmatif.', 'Negative → affirmative tag.'), ('Tu n’aimes pas le café, si ?', 'You don’t like coffee, do you?')),
        FB(CHOOSE, 'She works in marketing, ＿?', ['doesn’t she', 'isn’t she', 'don’t she'], 'doesn’t she', ('Présent simple : doesn’t.', 'Present simple: doesn’t.'), ('Elle travaille au marketing, n’est-ce pas ?', 'She works in marketing, doesn’t she?')),
        FB(CHOOSE, 'You’ve met Mr Ambrose, ＿?', ['haven’t you', 'didn’t you', 'don’t you'], 'haven’t you', ('Present perfect : haven’t.', 'Present perfect: haven’t.'), ('Tu as déjà rencontré M. Ambrose, n’est-ce pas ?', 'You’ve met Mr Ambrose, haven’t you?')),
      ]),
  ]),
  CH('b1-w8-c2', ('La négociation', 'Negotiation'), [
    L('en-negotiation', ('Négocier', 'Negotiating'), ('Proposer, faire une concession et conclure un accord.', 'Make an offer, a concession and close a deal.'), 9, [
        ('Proposer : We’d be prepared to… / How about if we…? / What if we offered…?', 'Proposing: We’d be prepared to… / How about if we…? / What if we offered…?'),
        ('Concéder sous condition : We could lower the price, provided that you order 500 units.', 'Conceding with a condition: We could lower the price, provided that you order 500 units.'),
        ('Conclure : I think we have a deal. / Let’s put that in writing.', 'Closing: I think we have a deal. / Let’s put that in writing.'),
      ], [
        E('negotiate', 'to negotiate', ('négocier', 'to negotiate')),
        E('provided-that', 'provided that', ('à condition que', 'provided that')),
        E('compromise', 'compromise', ('compromis', 'compromise')),
        E('units', 'units', ('unités (de produit)', 'units')),
        E('terms', 'terms', ('conditions (d’un contrat)', 'terms')),
        E('contract', 'contract', ('contrat', 'contract')),
      ], [
        x('We could offer a 5% discount, provided that you sign a two-year contract.', 'Nous pourrions accorder une remise de 5 %, à condition que vous signiez un contrat de deux ans.'),
        x('I think we’ve reached a good compromise. Let’s put it in writing.', 'Je pense que nous sommes parvenus à un bon compromis. Mettons-le par écrit.'),
      ], [
        FB(COMPLETE, 'We can lower the price, ＿ that you pay in advance.', ['provided', 'unless', 'despite'], 'provided', ('à condition que = provided that.', 'on condition that = provided that.'), ('Nous pouvons baisser le prix, à condition que vous payiez d’avance.', 'We can lower the price, provided that you pay in advance.')),
        DC(ANSWER, [('Supplier', 'We can offer 3% off if you order 1,000 units.')], ('Le fournisseur fait une offre ; tu veux mieux.', 'The supplier makes an offer; you want more.'), ['How about 5% if we order 1,500?', 'No. Bye.', 'Yes, we agree with all, of course.'], 'How about 5% if we order 1,500?', ('Contre-proposition : How about… ?', 'Counter-offer: How about…?')),
        FB(COMPLETE, 'Both sides accepted the ＿ of the contract.', ['terms', 'times', 'units'], 'terms', ('terms = conditions d’un contrat.', 'terms = conditions of a contract.'), ('Les deux parties ont accepté les conditions du contrat.', 'Both sides accepted the terms of the contract.')),
        TF('I think we have a deal.', ('La négociation a abouti.', 'The negotiation was successful.'), VRAI, ('a deal = un accord conclu.', 'a deal = an agreement.')),
      ]),
  ])])

write_level('B1', ('B1 : la quête du Graal', 'B1: the Grail quest'), REGION, 'Cornish coasts', 28,
  [W1, W2, W3, W4, W5, W6, W7, W8, FINAL('B1', REGION, ('Simulation TOEIC B1 : la chapelle du Graal', 'TOEIC B1 simulation: the Grail chapel'), 550)], PREVIOUS + ['content/a2/a2.json'])
