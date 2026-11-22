# Niveau B2 (anglais, CECRL B2, préparation au TOEIC) : 8 îles, 24 leçons et un examen blanc TOEIC (français + anglais).
# Mode histoire : la trahison de Mordred, responsable d'équipe chez Avalon & Co.
# Usage : python3 scripts/b2-level.py   (réécrit content/b2/b2.json)
from en_common import *

REGION = 'Marches galloises'

# ═════════════════════════ Île 1 : Les regrets ═════════════════════════
W1 = WORLD('b2-w1', ('Le chien des landes', 'The moorland hound'), REGION,
  ('Revenir sur le passé : le troisième conditionnel, les conditionnels mixtes et les regrets.', 'Look back on the past: the third conditional, mixed conditionals and regrets.'),
  (('Le Barghest des landes', 'The Barghest of the moors'), 'b', ('Ce chien-gobelin aux griffes immenses hante les ruelles d’York et les landes du Yorkshire. Il ne laisse passer que ceux qui savent dire ce qui serait arrivé si les choses s’étaient passées autrement.', 'This goblin hound with huge claws haunts the alleys of York and the Yorkshire moors. It only lets pass those who can say what would have happened if things had gone differently.')),
  [CH('b2-w1-c1', ('Si seulement…', 'If only…'), [
    L('en-third-conditional', ('Le troisième conditionnel : If I had known…', 'The third conditional: If I had known…'), ('Imaginer un passé différent et ses conséquences.', 'Imagine a different past and its consequences.'), 10, [
        ('If + past perfect, would have + participe passé : If I had known about the meeting, I would have come. (Je ne savais pas, je ne suis pas venu.)', 'If + past perfect, would have + past participle: If I had known about the meeting, I would have come. (I didn’t know, I didn’t come.)'),
        ('could have / might have pour une possibilité : If we had left earlier, we might have caught the train.', 'could have / might have for a possibility: If we had left earlier, we might have caught the train.'),
        ('À l’oral, had et would se contractent tous deux en ’d : If I’d seen her, I’d have told her.', 'In speech, had and would both contract to ’d: If I’d seen her, I’d have told her.'),
      ], [
        EG('third-conditional', 'If + had done, would have done', ('troisième conditionnel (passé irréel)', 'third conditional')),
        E('avoid', 'to avoid', ('éviter', 'to avoid')),
        E('opportunity', 'opportunity', ('occasion, opportunité', 'opportunity')),
        E('miss-opportunity', 'to miss', ('manquer, rater', 'to miss')),
        E('consequence', 'consequence', ('conséquence', 'consequence')),
      ], [
        x('If we had checked the figures, we would have avoided the mistake.', 'Si nous avions vérifié les chiffres, nous aurions évité l’erreur.'),
        x('She might have got the job if she had applied earlier.', 'Elle aurait peut-être obtenu le poste si elle avait postulé plus tôt.'),
      ], [
        FB(CHOOSE, 'If I ＿ about the strike, I would have taken the car.', ['had known', 'knew', 'would know'], 'had known', ('Condition dans le passé : If + past perfect.', 'Past condition: If + past perfect.'), ('Si j’avais été au courant de la grève, j’aurais pris la voiture.', 'If I had known about the strike, I would have taken the car.')),
        FB(CHOOSE, 'If they had invested earlier, they ＿ more money.', ['would have made', 'would make', 'had made'], 'would have made', ('Conséquence passée : would have + participe.', 'Past result: would have + participle.'), ('S’ils avaient investi plus tôt, ils auraient gagné plus d’argent.', 'If they had invested earlier, they would have made more money.')),
        FB(CHOOSE, 'We ＿ have won the contract if our price had been lower.', ['might', 'will', 'can'], 'might', ('Possibilité passée : might have.', 'Past possibility: might have.'), ('Nous aurions peut-être remporté le contrat si notre prix avait été plus bas.', 'We might have won the contract if our price had been lower.')),
        TF('If she had left on time, she would have caught the train.', ('Elle a pris le train.', 'She caught the train.'), FAUX, ('Troisième conditionnel : elle est partie en retard et l’a raté.', 'Third conditional: she left late and missed it.')),
      ]),
    L('en-mixed-conditionals', ('Les conditionnels mixtes', 'Mixed conditionals'), ('Relier une cause passée à un résultat présent, et inversement.', 'Link a past cause to a present result, and vice versa.'), 10, [
        ('Passé → présent : If I had taken the job in London, I would be living there now.', 'Past → present: If I had taken the job in London, I would be living there now.'),
        ('Présent → passé : If I were more organised, I wouldn’t have missed the deadline. (Je ne suis pas organisé, donc j’ai raté l’échéance.)', 'Present → past: If I were more organised, I wouldn’t have missed the deadline.'),
        ('I wish + past perfect = regret sur le passé : I wish I had studied harder. Should have + participe : I should have listened.', 'I wish + past perfect = regret about the past: I wish I had studied harder. Should have + participle: I should have listened.'),
      ], [
        EG('mixed-conditional', 'If I had done…, I would be…', ('conditionnel mixte (passé → présent)', 'mixed conditional')),
        EG('wish-past-perfect', 'I wish I had done', ('je regrette de ne pas avoir fait', 'I wish + past perfect')),
        E('decision', 'decision', ('décision', 'decision')),
        E('career', 'career', ('carrière', 'career')),
        E('in-hindsight', 'in hindsight', ('avec le recul', 'in hindsight')),
        E('turn-down', 'to turn down', ('refuser, décliner (une offre)', 'to turn down')),
      ], [
        x('If I hadn’t turned down that offer, I would be a manager by now.', 'Si je n’avais pas refusé cette offre, je serais responsable à l’heure qu’il est.'),
        x('In hindsight, I wish I had asked for more advice.', 'Avec le recul, je regrette de ne pas avoir demandé plus de conseils.'),
      ], [
        FB(CHOOSE, 'If I had studied medicine, I ＿ a doctor now.', ['would be', 'would have been', 'had been'], 'would be', ('Cause passée, résultat présent : would be.', 'Past cause, present result: would be.'), ('Si j’avais fait médecine, je serais médecin aujourd’hui.', 'If I had studied medicine, I would be a doctor now.')),
        FB(CHOOSE, 'I wish I ＿ that email. Now everyone is angry.', ['hadn’t sent', 'didn’t send', 'wouldn’t send'], 'hadn’t sent', ('Regret sur le passé : wish + past perfect.', 'Regret about the past: wish + past perfect.'), ('Je regrette d’avoir envoyé cet e-mail. Maintenant tout le monde est fâché.', 'I wish I hadn’t sent that email. Now everyone is angry.')),
        FB(CHOOSE, 'If he ＿ so shy, he would have spoken at the meeting.', ['weren’t', 'hadn’t', 'wouldn’t be'], 'weren’t', ('Trait présent, conséquence passée : If + prétérit.', 'Present trait, past result: If + past simple.'), ('S’il n’était pas si timide, il aurait pris la parole à la réunion.', 'If he weren’t so shy, he would have spoken at the meeting.')),
        DC(ANSWER, [('Barghest', 'You missed the flight. What do you regret?')], ('Le Barghest t’interroge sur tes regrets.', 'The Barghest asks about your regrets.'), ['I should have left home earlier.', 'I should leave home earlier yesterday.', 'I must have left earlier, I regret.'], 'I should have left home earlier.', ('Regret : should have + participe.', 'Regret: should have + participle.')),
      ]),
  ]),
  CH('b2-w1-c2', ('Le bilan', 'The review'), [
    L('en-project-review', ('Faire le bilan d’un projet', 'Reviewing a project'), ('Analyser ce qui a marché, ce qui a échoué et les leçons à retenir.', 'Analyse what worked, what failed and the lessons learnt.'), 9, [
        ('Expressions utiles : On the whole, the project was a success. / What went well was… / Where we fell short was… / With hindsight, we should have…', 'Useful phrases: On the whole, the project was a success. / What went well was… / Where we fell short was… / With hindsight, we should have…'),
        ('Vocabulaire : lessons learnt, outcome (résultat), to meet a target (atteindre un objectif), to fall behind schedule (prendre du retard), overrun (dépassement).', 'Vocabulary: lessons learnt, outcome, to meet a target, to fall behind schedule, overrun.'),
      ], [
        E('outcome', 'outcome', ('résultat, issue', 'outcome')),
        E('meet-target', 'to meet a target', ('atteindre un objectif', 'to meet a target')),
        E('behind-schedule', 'behind schedule', ('en retard sur le calendrier', 'behind schedule')),
        E('on-the-whole', 'on the whole', ('dans l’ensemble', 'on the whole')),
        E('lessons-learnt', 'lessons learnt', ('enseignements tirés', 'lessons learnt')),
        E('overrun', 'cost overrun', ('dépassement de budget', 'cost overrun')),
      ], [
        x('On the whole, we met our targets, although the project fell behind schedule in March.', 'Dans l’ensemble, nous avons atteint nos objectifs, même si le projet a pris du retard en mars.'),
        x('If we had hired a second engineer, we wouldn’t have had such a large cost overrun.', 'Si nous avions embauché un deuxième ingénieur, nous n’aurions pas eu un tel dépassement de budget.'),
      ], [
        FB(COMPLETE, 'On the ＿, the launch went very well.', ['whole', 'all', 'total'], 'whole', ('on the whole = dans l’ensemble.', 'on the whole = generally.'), ('Dans l’ensemble, le lancement s’est très bien passé.', 'On the whole, the launch went very well.')),
        FB(COMPLETE, 'The project is two weeks behind ＿.', ['schedule', 'time', 'agenda'], 'schedule', ('behind schedule = en retard.', 'behind schedule = late.'), ('Le projet a deux semaines de retard.', 'The project is two weeks behind schedule.')),
        FB(COMPLETE, 'We didn’t ＿ our sales target this quarter.', ['meet', 'join', 'arrive'], 'meet', ('meet a target = atteindre un objectif.', 'meet a target.'), ('Nous n’avons pas atteint notre objectif de ventes ce trimestre.', 'We didn’t meet our sales target this quarter.')),
        TF('The outcome of the negotiation was positive.', ('La négociation a échoué.', 'The negotiation failed.'), FAUX, ('outcome = résultat ; il est positif.', 'outcome = result; it was positive.')),
      ]),
  ])])

# ═════════════════════════ Île 2 : Les relatives ═════════════════════════
W2 = WORLD('b2-w2', ('Le sauteur de Londres', 'The London leaper'), REGION,
  ('Donner des précisions avec les propositions relatives : déterminatives, explicatives et réduites.', 'Add detail with relative clauses: defining, non-defining and reduced.'),
  (('Spring-heeled Jack', 'Spring-heeled Jack'), 'Z', ('Ce mystérieux personnage aux bottes à ressorts bondit par-dessus les toits de Londres. Décris précisément les gens et les choses pour le démasquer.', 'This mysterious figure with spring-loaded boots leaps over the roofs of London. Describe people and things precisely to unmask him.')),
  [CH('b2-w2-c1', ('Qui, que, dont', 'Who, which, whose'), [
    L('en-relative-clauses', ('Relatives déterminatives et explicatives', 'Defining and non-defining relative clauses'), ('Choisir entre who, which, that, whose et la virgule.', 'Choose between who, which, that, whose and the comma.'), 10, [
        ('Déterminative (indispensable, sans virgule) : The man who called you is my boss. that peut remplacer who/which ; le pronom peut disparaître s’il est complément : The report (that) I wrote…', 'Defining (essential, no commas): The man who called you is my boss. that can replace who/which; the pronoun can be dropped when it is the object: The report (that) I wrote…'),
        ('Explicative (information en plus, entre virgules) : Mr Hall, who has worked here for 20 years, is retiring. Jamais that, jamais d’omission.', 'Non-defining (extra information, between commas): Mr Hall, who has worked here for 20 years, is retiring. Never that, never omitted.'),
        ('whose = dont (possession) ; where = où ; which en fin de phrase peut reprendre toute la proposition : He was late, which annoyed everyone.', 'whose = possession; where = place; which at the end can refer to the whole clause: He was late, which annoyed everyone.'),
      ], [
        EG('relative-clauses', 'who / which / that / whose', ('pronoms relatifs (qui, que, où)', 'relative pronouns')),
        EG('non-defining', ', who… , / , which… ,', ('relative explicative (entre virgules)', 'non-defining relative clause')),
        E('retire', 'to retire', ('prendre sa retraite', 'to retire')),
        E('headquarters', 'headquarters', ('siège social', 'headquarters')),
        E('annoy', 'to annoy', ('agacer, contrarier', 'to annoy')),
      ], [
        x('The supplier whose prices were the lowest won the contract.', 'Le fournisseur dont les prix étaient les plus bas a remporté le contrat.'),
        x('Our headquarters, which are in Cardiff, will move next year.', 'Notre siège, qui se trouve à Cardiff, déménagera l’année prochaine.'),
      ], [
        FB(CHOOSE, 'The woman ＿ car was stolen called the police.', ['whose', 'who', 'which'], 'whose', ('Possession : whose.', 'Possession: whose.'), ('La femme dont la voiture a été volée a appelé la police.', 'The woman whose car was stolen called the police.')),
        FB(CHOOSE, 'Ms Price, ＿ joined us last year, is our new director.', ['who', 'that', 'which'], 'who', ('Explicative, personne : who (jamais that).', 'Non-defining, person: who (never that).'), ('Mme Price, qui nous a rejoints l’an dernier, est notre nouvelle directrice.', 'Ms Price, who joined us last year, is our new director.')),
        FB(CHOOSE, 'He forgot the meeting, ＿ was very embarrassing.', ['which', 'that', 'what'], 'which', ('which reprend toute la proposition.', 'which refers to the whole clause.'), ('Il a oublié la réunion, ce qui était très gênant.', 'He forgot the meeting, which was very embarrassing.')),
        FB(CHOOSE, 'This is the hotel ＿ we stayed last year.', ['where', 'which', 'whose'], 'where', ('Lieu : where.', 'Place: where.'), ('C’est l’hôtel où nous avons séjourné l’an dernier.', 'This is the hotel where we stayed last year.')),
      ]),
    L('en-reduced-relatives', ('Les relatives réduites', 'Reduced relative clauses'), ('Alléger une phrase avec un participe : the man sitting…, the goods ordered…', 'Lighten a sentence with a participle: the man sitting…, the goods ordered…'), 10, [
        ('Sens actif → participe en -ing : The people working on this project (= who work…) are very busy.', 'Active meaning → -ing participle: The people working on this project (= who work…) are very busy.'),
        ('Sens passif → participe passé : The goods ordered last week (= which were ordered…) have arrived.', 'Passive meaning → past participle: The goods ordered last week (= which were ordered…) have arrived.'),
        ('Très fréquent au TOEIC : Applicants wishing to attend… / All forms submitted after 1 May…', 'Very common in the TOEIC: Applicants wishing to attend… / All forms submitted after 1 May…'),
      ], [
        EG('reduced-relatives', 'the people working… / the goods ordered…', ('relative réduite (participe)', 'reduced relative clause')),
        E('applicant', 'applicant', ('candidat (à un poste, une demande)', 'applicant')),
        E('submit', 'to submit', ('soumettre, remettre', 'to submit')),
        E('attend', 'to attend', ('assister à', 'to attend')),
        E('wishing-to', 'wishing to', ('souhaitant (+ verbe)', 'wishing to')),
        E('enclosed', 'enclosed', ('ci-joint (courrier)', 'enclosed')),
      ], [
        x('Employees wishing to attend the training should register by Friday.', 'Les salariés souhaitant participer à la formation doivent s’inscrire d’ici vendredi.'),
        x('Applications submitted after the deadline will not be accepted.', 'Les candidatures envoyées après la date limite ne seront pas acceptées.'),
      ], [
        FB(CHOOSE, 'Passengers ＿ to Paris should go to gate 12.', ['travelling', 'travelled', 'travel'], 'travelling', ('Sens actif : -ing.', 'Active meaning: -ing.'), ('Les passagers à destination de Paris doivent se rendre à la porte 12.', 'Passengers travelling to Paris should go to gate 12.')),
        FB(CHOOSE, 'The products ＿ in our factory are sold worldwide.', ['made', 'making', 'make'], 'made', ('Sens passif : participe passé.', 'Passive meaning: past participle.'), ('Les produits fabriqués dans notre usine sont vendus dans le monde entier.', 'The products made in our factory are sold worldwide.')),
        FB(CHOOSE, 'Applicants ＿ to apply should send a CV.', ['wishing', 'wished', 'wish'], 'wishing', ('Applicants wishing to… = qui souhaitent.', 'Applicants wishing to… = who wish to.'), ('Les candidats souhaitant postuler doivent envoyer un CV.', 'Applicants wishing to apply should send a CV.')),
        TF('Please find enclosed a copy of the contract.', ('Une copie du contrat est jointe.', 'A copy of the contract is included.'), VRAI, ('enclosed = ci-joint.', 'enclosed = included with the letter.')),
      ]),
  ]),
  CH('b2-w2-c2', ('Présenter', 'Presenting'), [
    L('en-presentations', ('Faire une présentation', 'Giving a presentation'), ('Structurer une présentation et guider son auditoire.', 'Structure a presentation and guide the audience.'), 9, [
        ('Introduire : Today I’d like to talk about… / I’ve divided my presentation into three parts.', 'Introducing: Today I’d like to talk about… / I’ve divided my presentation into three parts.'),
        ('Enchaîner : Moving on to… / Let’s now turn to… / As you can see on this slide…', 'Moving on: Moving on to… / Let’s now turn to… / As you can see on this slide…'),
        ('Conclure : To sum up… / I’d be happy to answer any questions.', 'Concluding: To sum up… / I’d be happy to answer any questions.'),
      ], [
        E('slide', 'slide', ('diapositive', 'slide')),
        E('sum-up', 'to sum up', ('pour résumer', 'to sum up')),
        E('move-on', 'to move on to', ('passer à', 'to move on to')),
        E('audience', 'audience', ('public, auditoire', 'audience')),
        E('highlight', 'to highlight', ('souligner, mettre en évidence', 'to highlight')),
        E('overview', 'overview', ('vue d’ensemble, aperçu', 'overview')),
      ], [
        x('I’ll start with a brief overview, then move on to the figures.', 'Je commencerai par un bref aperçu, puis je passerai aux chiffres.'),
        x('To sum up, I’d like to highlight three key points.', 'Pour résumer, j’aimerais souligner trois points clés.'),
      ], [
        FB(COMPLETE, 'To ＿ up, our sales have doubled in two years.', ['sum', 'add', 'end'], 'sum', ('to sum up = pour résumer.', 'to sum up = to summarise.'), ('Pour résumer, nos ventes ont doublé en deux ans.', 'To sum up, our sales have doubled in two years.')),
        FB(COMPLETE, 'As you can see on this ＿, costs have fallen.', ['slide', 'page', 'board'], 'slide', ('Diapositive = slide.', 'Presentation page = slide.'), ('Comme vous le voyez sur cette diapositive, les coûts ont baissé.', 'As you can see on this slide, costs have fallen.')),
        DC(ANSWER, [('Spring-heeled Jack', 'You have finished your talk. What do you say?')], ('Fin de ta présentation.', 'End of your presentation.'), ['Thank you. I’d be happy to answer any questions.', 'That’s all. Go away now.', 'Questions are not possible.'], 'Thank you. I’d be happy to answer any questions.', ('Conclure en invitant les questions.', 'Close by inviting questions.')),
        TF('Let me give you a brief overview.', ('L’orateur va entrer dans tous les détails.', 'The speaker will go into every detail.'), FAUX, ('overview = vue d’ensemble.', 'overview = general summary.')),
      ]),
  ])])

# ═════════════════════════ Île 3 : Gérondif et infinitif ═════════════════════════
W3 = WORLD('b2-w3', ('L’étang du Grindylow', 'The Grindylow’s pond'), REGION,
  ('Maîtriser le gérondif et l’infinitif après les verbes, prépositions et adjectifs.', 'Master gerunds and infinitives after verbs, prepositions and adjectives.'),
  (('Le Grindylow des étangs', 'The Grindylow of the ponds'), 'I', ('Ce démon aquatique aux longs bras attrape ceux qui s’approchent trop de l’eau. Il ne lâche que ceux qui choisissent sans hésiter entre -ing et to.', 'This long-armed water demon grabs anyone who comes too close to the water. It only lets go of those who choose between -ing and to without hesitation.')),
  [CH('b2-w3-c1', ('-ing ou to ?', '-ing or to?'), [
    L('en-gerund-infinitive', ('Verbe + -ing ou verbe + to', 'Verb + -ing or verb + to'), ('Retenir quels verbes se construisent avec -ing, lesquels avec to.', 'Learn which verbs take -ing and which take to.'), 10, [
        ('+ -ing : enjoy, avoid, finish, mind, suggest, consider, recommend, look forward to : I suggest postponing the meeting.', '+ -ing: enjoy, avoid, finish, mind, suggest, consider, recommend, look forward to: I suggest postponing the meeting.'),
        ('+ to : want, decide, agree, refuse, promise, manage, plan, afford, expect : We managed to finish on time.', '+ to: want, decide, agree, refuse, promise, manage, plan, afford, expect: We managed to finish on time.'),
        ('Après une préposition, toujours -ing : interested in working, before leaving, instead of calling.', 'After a preposition, always -ing: interested in working, before leaving, instead of calling.'),
      ], [
        EG('gerund', 'enjoy doing, avoid doing', ('gérondif après certains verbes', 'gerund after verbs')),
        EG('infinitive', 'want to do, decide to do', ('infinitif après certains verbes', 'infinitive after verbs')),
        E('manage', 'to manage to', ('réussir à, parvenir à', 'to manage to')),
        E('afford', 'to afford', ('avoir les moyens de', 'to afford')),
        E('consider', 'to consider', ('envisager, considérer', 'to consider')),
        E('look-forward', 'to look forward to', ('avoir hâte de, se réjouir de', 'to look forward to')),
        E('refuse', 'to refuse', ('refuser', 'to refuse')),
      ], [
        x('We can’t afford to lose this client.', 'Nous ne pouvons pas nous permettre de perdre ce client.'),
        x('I look forward to hearing from you.', 'Dans l’attente de votre réponse. (litt. J’ai hâte d’avoir de vos nouvelles.)'),
      ], [
        FB(CHOOSE, 'I suggest ＿ the meeting until Friday.', ['postponing', 'to postpone', 'postpone'], 'postponing', ('suggest + -ing.', 'suggest + -ing.'), ('Je propose de reporter la réunion à vendredi.', 'I suggest postponing the meeting until Friday.')),
        FB(CHOOSE, 'They refused ＿ the price.', ['to lower', 'lowering', 'lower'], 'to lower', ('refuse + to.', 'refuse + to.'), ('Ils ont refusé de baisser le prix.', 'They refused to lower the price.')),
        FB(CHOOSE, 'I look forward to ＿ you in Cardiff.', ['meeting', 'meet', 'met'], 'meeting', ('look forward to + -ing (to est une préposition).', 'look forward to + -ing (to is a preposition).'), ('J’ai hâte de vous rencontrer à Cardiff.', 'I look forward to meeting you in Cardiff.')),
        FB(CHOOSE, 'She is interested in ＿ abroad.', ['working', 'to work', 'work'], 'working', ('Après une préposition : -ing.', 'After a preposition: -ing.'), ('Elle souhaite travailler à l’étranger.', 'She is interested in working abroad.')),
      ]),
    L('en-stop-remember', ('Changement de sens : stop, remember, try', 'Change of meaning: stop, remember, try'), ('Distinguer les verbes dont le sens change selon -ing ou to.', 'Tell apart verbs whose meaning changes with -ing or to.'), 10, [
        ('stop doing = arrêter de faire ; stop to do = s’arrêter pour faire : He stopped smoking. / He stopped to buy a coffee.', 'stop doing = quit; stop to do = pause in order to do: He stopped smoking. / He stopped to buy a coffee.'),
        ('remember doing = se souvenir d’avoir fait ; remember to do = penser à faire : Remember to lock the door.', 'remember doing = recall a past action; remember to do = not forget: Remember to lock the door.'),
        ('try to do = essayer (effort) ; try doing = tester une solution : Try restarting the computer.', 'try to do = make an effort; try doing = test a solution: Try restarting the computer.'),
      ], [
        EG('stop-remember-try', 'stop doing / stop to do', ('verbes à double construction', 'verbs with -ing or to (change of meaning)')),
        E('remember', 'to remember', ('se souvenir', 'to remember')),
        E('lock', 'to lock', ('fermer à clé', 'to lock')),
        E('restart', 'to restart', ('redémarrer', 'to restart')),
        E('quit', 'to quit', ('arrêter, quitter', 'to quit')),
      ], [
        x('Please remember to switch off the lights when you leave.', 'Pensez à éteindre les lumières en partant.'),
        x('If the printer doesn’t work, try turning it off and on again.', 'Si l’imprimante ne marche pas, essayez de l’éteindre et de la rallumer.'),
      ], [
        FB(CHOOSE, 'Remember ＿ the door when you leave.', ['to lock', 'locking', 'lock'], 'to lock', ('Penser à faire : remember to.', 'Not forget: remember to.'), ('Pense à fermer la porte à clé en partant.', 'Remember to lock the door when you leave.')),
        FB(CHOOSE, 'I remember ＿ him at the conference last year.', ['meeting', 'to meet', 'meet'], 'meeting', ('Souvenir d’une action passée : remember + -ing.', 'Memory of a past action: remember + -ing.'), ('Je me souviens de l’avoir rencontré au congrès l’an dernier.', 'I remember meeting him at the conference last year.')),
        FB(CHOOSE, 'We stopped ＿ some petrol on the way.', ['to buy', 'buying', 'buy'], 'to buy', ('S’arrêter pour faire : stop to.', 'Pause to do: stop to.'), ('Nous nous sommes arrêtés pour prendre de l’essence en route.', 'We stopped to buy some petrol on the way.')),
        DC(ANSWER, [('Grindylow', 'My computer has frozen. What should I do?')], ('Le Grindylow demande un conseil technique.', 'The Grindylow asks for tech advice.'), ['Try restarting it.', 'Try to restarting it.', 'Stop to restart.'], 'Try restarting it.', ('Tester une solution : try + -ing.', 'Testing a solution: try + -ing.')),
      ]),
  ]),
  CH('b2-w3-c2', ('Les finances', 'Finance'), [
    L('en-finance', ('Parler finances', 'Talking about finance'), ('Comprendre les termes financiers courants du TOEIC.', 'Understand common TOEIC finance terms.'), 9, [
        ('Compte de résultat : revenue / turnover (chiffre d’affaires), expenses (dépenses), profit, loss (perte). Break even = atteindre l’équilibre.', 'Income statement: revenue / turnover, expenses, profit, loss. Break even = make neither profit nor loss.'),
        ('Banque : account, loan (prêt), interest rate (taux d’intérêt), to transfer money (virer), a payment is due (exigible).', 'Banking: account, loan, interest rate, to transfer money, a payment is due.'),
      ], [
        E('revenue', 'revenue', ('chiffre d’affaires, recettes', 'revenue')),
        E('profit', 'profit', ('bénéfice', 'profit')),
        E('loss', 'loss', ('perte', 'loss')),
        E('loan', 'loan', ('prêt, emprunt', 'loan')),
        E('interest-rate', 'interest rate', ('taux d’intérêt', 'interest rate')),
        E('due', 'due', ('dû, exigible, attendu', 'due')),
        E('break-even', 'to break even', ('atteindre le seuil de rentabilité', 'to break even')),
      ], [
        x('Revenue rose by 12%, but higher costs led to a small loss.', 'Le chiffre d’affaires a augmenté de 12 %, mais la hausse des coûts a entraîné une petite perte.'),
        x('The first payment on the loan is due on 1 March.', 'La première échéance du prêt est due le 1er mars.'),
      ], [
        FB(COMPLETE, 'The company made a ＿ of £2 million last year.', ['profit', 'benefit', 'gain'], 'profit', ('Bénéfice d’une entreprise : profit.', 'A company’s earnings: profit.'), ('L’entreprise a réalisé un bénéfice de 2 millions de livres l’an dernier.', 'The company made a profit of £2 million last year.')),
        FB(COMPLETE, 'We expect to break ＿ in our second year.', ['even', 'down', 'out'], 'even', ('break even = atteindre l’équilibre.', 'break even.'), ('Nous prévoyons d’atteindre l’équilibre dès la deuxième année.', 'We expect to break even in our second year.')),
        FB(COMPLETE, 'The bank has raised its interest ＿.', ['rates', 'prices', 'levels'], 'rates', ('interest rate = taux d’intérêt.', 'interest rate.'), ('La banque a relevé ses taux d’intérêt.', 'The bank has raised its interest rates.')),
        TF('The invoice is due next week.', ('La facture doit être payée la semaine prochaine.', 'The invoice must be paid next week.'), VRAI, ('due = à payer à une date.', 'due = to be paid by a date.')),
      ]),
  ])])

# ═════════════════════════ Île 4 : Faire faire ═════════════════════════
W4 = WORLD('b2-w4', ('La mine des Coblynau', 'The Coblynau’s mine'), REGION,
  ('Déléguer et organiser : la forme causative (have / get something done), et les verbes make, let, help.', 'Delegate and organise: the causative (have / get something done), and make, let, help.'),
  (('Les Coblynau des mines', 'The Coblynau of the mines'), 'h', ('Ces petits lutins des mines galloises frappent les parois et cassent les outils des mineurs. Ils ne se calment que si tu sais faire réparer ce qu’ils ont abîmé.', 'These little goblins of the Welsh mines knock on the walls and break the miners’ tools. They only calm down if you know how to get what they damaged repaired.')),
  [CH('b2-w4-c1', ('Le faire faire', 'Getting it done'), [
    L('en-causative', ('La forme causative : have something done', 'The causative: have something done'), ('Dire qu’on fait faire quelque chose par un professionnel.', 'Say that someone else does something for you.'), 10, [
        ('have + objet + participe passé : I had my car repaired (on m’a réparé ma voiture). We’re having the office painted.', 'have + object + past participle: I had my car repaired. We’re having the office painted.'),
        ('get est plus familier : I need to get my hair cut. On peut aussi subir quelque chose : She had her bag stolen.', 'get is more informal: I need to get my hair cut. It can also describe something bad: She had her bag stolen.'),
        ('Faire faire à une personne : have someone do / get someone to do : I’ll have my assistant call you. I got Tom to check the figures.', 'Making a person do something: have someone do / get someone to do: I’ll have my assistant call you. I got Tom to check the figures.'),
      ], [
        EG('causative', 'have / get something done', ('faire faire quelque chose', 'causative have / get')),
        E('repair', 'to repair', ('réparer', 'to repair')),
        E('install', 'to install', ('installer', 'to install')),
        E('service', 'to service', ('entretenir, réviser (une machine)', 'to service')),
        E('technician', 'technician', ('technicien', 'technician')),
        E('maintenance', 'maintenance', ('maintenance, entretien', 'maintenance')),
      ], [
        x('We’re having new air conditioning installed next week.', 'On nous installe une nouvelle climatisation la semaine prochaine.'),
        x('I’ll have my assistant send you the contract.', 'Je demanderai à mon assistante de vous envoyer le contrat.'),
      ], [
        FB(CHOOSE, 'I had my laptop ＿ last week.', ['repaired', 'repair', 'repairing'], 'repaired', ('have + objet + participe passé.', 'have + object + past participle.'), ('J’ai fait réparer mon ordinateur portable la semaine dernière.', 'I had my laptop repaired last week.')),
        FB(CHOOSE, 'We need to get the printer ＿.', ['serviced', 'service', 'to service'], 'serviced', ('get + objet + participe passé.', 'get + object + past participle.'), ('Nous devons faire réviser l’imprimante.', 'We need to get the printer serviced.')),
        FB(CHOOSE, 'I’ll have my secretary ＿ you back.', ['call', 'to call', 'called'], 'call', ('have + personne + base verbale.', 'have + person + base verb.'), ('Je vais demander à ma secrétaire de vous rappeler.', 'I’ll have my secretary call you back.')),
        FB(CHOOSE, 'I got the technician ＿ the network.', ['to check', 'check', 'checked'], 'to check', ('get + personne + to.', 'get + person + to.'), ('J’ai demandé au technicien de vérifier le réseau.', 'I got the technician to check the network.')),
      ]),
    L('en-make-let', ('Make, let, allow, help', 'Make, let, allow, help'), ('Exprimer l’obligation, la permission et l’aide.', 'Express obligation, permission and help.'), 9, [
        ('make someone do = obliger : The manager made us work late. let someone do = laisser : She let me leave early.', 'make someone do = force: The manager made us work late. let someone do = allow: She let me leave early.'),
        ('allow someone to do (plus formel) : Visitors are not allowed to smoke. help someone (to) do : Can you help me (to) move this desk?', 'allow someone to do (more formal): Visitors are not allowed to smoke. help someone (to) do: Can you help me (to) move this desk?'),
      ], [
        EG('make-let', 'make / let someone do', ('obliger / laisser faire', 'make / let + base verb')),
        E('allow', 'to allow', ('permettre, autoriser', 'to allow')),
        E('permission', 'permission', ('autorisation', 'permission')),
        E('force', 'to force', ('forcer, obliger', 'to force')),
      ], [
        x('Our new manager lets us work from home on Fridays.', 'Notre nouvelle responsable nous laisse télétravailler le vendredi.'),
        x('Employees are not allowed to use their phones in the laboratory.', 'Les employés n’ont pas le droit d’utiliser leur téléphone dans le laboratoire.'),
      ], [
        FB(CHOOSE, 'The boss made us ＿ the report again.', ['rewrite', 'to rewrite', 'rewriting'], 'rewrite', ('make + personne + base verbale.', 'make + person + base verb.'), ('Le patron nous a fait réécrire le rapport.', 'The boss made us rewrite the report.')),
        FB(CHOOSE, 'My parents never let me ＿ out late.', ['stay', 'to stay', 'staying'], 'stay', ('let + base verbale.', 'let + base verb.'), ('Mes parents ne me laissaient jamais rentrer tard.', 'My parents never let me stay out late.')),
        FB(CHOOSE, 'Visitors are not allowed ＿ photos.', ['to take', 'take', 'taking'], 'to take', ('allowed to + verbe.', 'allowed to + verb.'), ('Les visiteurs ne sont pas autorisés à prendre des photos.', 'Visitors are not allowed to take photos.')),
        TF('She let me leave early.', ('Elle m’a obligé à partir tôt.', 'She forced me to leave early.'), FAUX, ('let = laisser, autoriser.', 'let = allow.')),
      ]),
  ]),
  CH('b2-w4-c2', ('Les ressources humaines', 'Human resources'), [
    L('en-hr', ('Ressources humaines et carrière', 'HR and careers'), ('Comprendre le vocabulaire du recrutement, de la formation et des avantages.', 'Understand recruitment, training and benefits vocabulary.'), 9, [
        ('Recruter : to recruit, to hire (embaucher), to shortlist (présélectionner), a vacancy (poste vacant). Quitter : to resign (démissionner), to dismiss / to fire (licencier), to lay off (licencier pour raison économique).', 'Recruiting: to recruit, to hire, to shortlist, a vacancy. Leaving: to resign, to dismiss / to fire, to lay off.'),
        ('Avantages : benefits package, paid leave (congés payés), a pay rise (augmentation), promotion, performance review (entretien annuel).', 'Benefits: benefits package, paid leave, a pay rise, promotion, performance review.'),
      ], [
        E('hire', 'to hire', ('embaucher, recruter', 'to hire')),
        E('resign', 'to resign', ('démissionner', 'to resign')),
        E('lay-off', 'to lay off', ('licencier (raison économique)', 'to lay off')),
        E('promotion', 'promotion', ('promotion', 'promotion')),
        E('pay-rise', 'pay rise', ('augmentation de salaire', 'pay rise')),
        E('vacancy', 'vacancy', ('poste vacant', 'vacancy')),
        E('shortlist', 'to shortlist', ('présélectionner', 'to shortlist')),
      ], [
        x('Five candidates have been shortlisted for the vacancy.', 'Cinq candidats ont été présélectionnés pour le poste.'),
        x('After her performance review, she was offered a promotion and a pay rise.', 'Après son entretien annuel, on lui a proposé une promotion et une augmentation.'),
      ], [
        FB(COMPLETE, 'He ＿ because he found a better job.', ['resigned', 'fired', 'laid off'], 'resigned', ('Partir de soi-même : resign.', 'Leaving by choice: resign.'), ('Il a démissionné parce qu’il a trouvé un meilleur emploi.', 'He resigned because he found a better job.')),
        FB(COMPLETE, 'The factory had to lay ＿ 200 workers.', ['off', 'out', 'down'], 'off', ('lay off = licencier.', 'lay off.'), ('L’usine a dû licencier 200 ouvriers.', 'The factory had to lay off 200 workers.')),
        FB(COMPLETE, 'We are going to ＿ three new engineers.', ['hire', 'rent', 'lend'], 'hire', ('Embaucher = hire.', 'Employ someone = hire.'), ('Nous allons embaucher trois nouveaux ingénieurs.', 'We are going to hire three new engineers.')),
        TF('There is a vacancy in the sales team.', ('Un poste est à pourvoir dans l’équipe commerciale.', 'A job is available in the sales team.'), VRAI, ('vacancy = poste vacant.', 'vacancy = open position.')),
      ]),
  ])])

# ═════════════════════════ Île 5 : L'avenir ═════════════════════════
W5 = WORLD('b2-w5', ('La peau de phoque', 'The sealskin'), REGION,
  ('Se projeter : futur continu, futur antérieur, et les expressions be about to, be due to.', 'Look ahead: future continuous, future perfect, and be about to, be due to.'),
  (('La Selkie des Orcades', 'The Selkie of Orkney'), 'f', ('Mi-femme mi-phoque, la Selkie a caché sa peau pour vivre sur terre, mais elle doit repartir à une date précise. Aide-la à planifier son avenir.', 'Half woman, half seal, the Selkie hid her skin to live on land, but must return to the sea on a set date. Help her plan her future.')),
  [CH('b2-w5-c1', ('Demain à cette heure-ci', 'This time tomorrow'), [
    L('en-future-continuous', ('Le futur continu : I’ll be working', 'The future continuous: I’ll be working'), ('Décrire une action en cours à un moment du futur.', 'Describe an action in progress at a future time.'), 10, [
        ('will be + -ing : This time tomorrow, I’ll be flying to New York.', 'will be + -ing: This time tomorrow, I’ll be flying to New York.'),
        ('Pour demander poliment les projets de quelqu’un : Will you be using the meeting room this afternoon?', 'To ask politely about someone’s plans: Will you be using the meeting room this afternoon?'),
      ], [
        EG('future-continuous', 'will be + -ing', ('futur continu (action en cours dans le futur)', 'future continuous')),
        E('this-time-tomorrow', 'this time tomorrow', ('demain à la même heure', 'this time tomorrow')),
        E('fly', 'to fly', ('prendre l’avion, voler', 'to fly')),
        E('trade-fair', 'trade fair', ('salon professionnel', 'trade fair')),
      ], [
        x('This time next week, we’ll be presenting our products at the trade fair in Frankfurt.', 'La semaine prochaine à cette heure-ci, nous présenterons nos produits au salon de Francfort.'),
        x('Will you be needing a taxi to the airport?', 'Aurez-vous besoin d’un taxi pour l’aéroport ?'),
      ], [
        FB(CHOOSE, 'This time tomorrow, I ＿ on a beach in Spain.', ['will be lying', 'will lie', 'lie'], 'will be lying', ('Action en cours dans le futur : will be + -ing.', 'Action in progress in the future: will be + -ing.'), ('Demain à cette heure-ci, je serai allongé sur une plage en Espagne.', 'This time tomorrow, I will be lying on a beach in Spain.')),
        FB(CHOOSE, '＿ you be using the car tonight?', ['Will', 'Are', 'Do'], 'Will', ('Question polie : Will you be + -ing ?', 'Polite question: Will you be + -ing?'), ('Vas-tu utiliser la voiture ce soir ?', 'Will you be using the car tonight?')),
        FB(CHOOSE, 'Don’t call at eight. We ＿ dinner.', ['will be having', 'will have had', 'have'], 'will be having', ('À 20 h, l’action sera en cours.', 'At eight, the action will be in progress.'), ('N’appelle pas à huit heures. Nous serons en train de dîner.', 'Don’t call at eight. We will be having dinner.')),
        TF('This time next week, I’ll be travelling abroad.', ('La personne sera en voyage la semaine prochaine.', 'The person will be on a trip next week.'), VRAI, ('will be travelling = sera en voyage.', 'will be travelling = on a trip then.')),
      ]),
    L('en-future-perfect', ('Le futur antérieur : will have done', 'The future perfect: will have done'), ('Dire ce qui sera terminé avant un moment du futur.', 'Say what will be finished before a future time.'), 10, [
        ('will have + participe passé : By Friday, we will have finished the report.', 'will have + past participle: By Friday, we will have finished the report.'),
        ('by = d’ici, au plus tard ; by the time + présent : By the time you arrive, I’ll have left.', 'by = no later than; by the time + present: By the time you arrive, I’ll have left.'),
        ('be about to = être sur le point de ; be due to = être prévu pour : The train is due to arrive at 6.15.', 'be about to = be on the point of; be due to = be scheduled to: The train is due to arrive at 6.15.'),
      ], [
        EG('future-perfect', 'will have done', ('futur antérieur (aura fini)', 'future perfect')),
        EG('be-about-to', 'be about to / be due to', ('être sur le point de / être prévu pour', 'be about to / be due to')),
        E('by-deadline', 'by', ('d’ici, au plus tard (date)', 'by (deadline)')),
        E('launch', 'to launch', ('lancer (un produit)', 'to launch')),
        E('scheduled', 'scheduled', ('prévu, programmé', 'scheduled')),
      ], [
        x('By the end of the year, we will have opened ten new shops.', 'D’ici la fin de l’année, nous aurons ouvert dix nouveaux magasins.'),
        x('The new model is due to be launched in March.', 'Le nouveau modèle doit être lancé en mars.'),
      ], [
        FB(CHOOSE, 'By 2030, the company ＿ its carbon emissions by half.', ['will have reduced', 'will reduce', 'reduces'], 'will have reduced', ('Terminé avant 2030 : will have + participe.', 'Done before 2030: will have + participle.'), ('D’ici 2030, l’entreprise aura réduit de moitié ses émissions de carbone.', 'By 2030, the company will have reduced its carbon emissions by half.')),
        FB(CHOOSE, 'By the time you get here, the film ＿.', ['will have started', 'will start', 'starts'], 'will have started', ('Antérieur à un moment futur.', 'Before a future moment.'), ('Le temps que tu arrives, le film aura commencé.', 'By the time you get here, the film will have started.')),
        FB(CHOOSE, 'Hurry up! The train is ＿ to leave.', ['about', 'due', 'going'], 'about', ('Sur le point de : be about to.', 'On the point of: be about to.'), ('Dépêche-toi ! Le train est sur le point de partir.', 'Hurry up! The train is about to leave.')),
        FB(CHOOSE, 'The flight is ＿ to land at 10.40.', ['due', 'about', 'ready'], 'due', ('Prévu à une heure : be due to.', 'Scheduled: be due to.'), ('Le vol doit atterrir à 10 h 40.', 'The flight is due to land at 10.40.')),
      ]),
  ]),
  CH('b2-w5-c2', ('Voyages d’affaires', 'Business travel'), [
    L('en-business-travel', ('Organiser un voyage d’affaires', 'Arranging a business trip'), ('Réserver, modifier et gérer les imprévus d’un déplacement.', 'Book, change and handle problems on a business trip.'), 9, [
        ('Réserver : to book a flight, an aisle / window seat, a return ticket (aller-retour), a single (aller simple). L’itinéraire = itinerary.', 'Booking: to book a flight, an aisle / window seat, a return ticket, a single. The schedule of a trip = itinerary.'),
        ('Imprévus : the flight has been cancelled / diverted (dérouté), to miss a connection (correspondance), to reschedule (reprogrammer), to be reimbursed (être remboursé).', 'Problems: the flight has been cancelled / diverted, to miss a connection, to reschedule, to be reimbursed.'),
      ], [
        E('itinerary', 'itinerary', ('itinéraire, programme de voyage', 'itinerary')),
        E('connection', 'connection', ('correspondance', 'connection (travel)')),
        E('reschedule', 'to reschedule', ('reprogrammer, décaler', 'to reschedule')),
        E('reimburse', 'to reimburse', ('rembourser', 'to reimburse')),
        E('aisle-seat', 'aisle seat', ('place côté couloir', 'aisle seat')),
        E('accommodation', 'accommodation', ('hébergement, logement', 'accommodation')),
      ], [
        x('I’ve attached your itinerary. Your accommodation has been booked for three nights.', 'Vous trouverez ci-joint votre programme. Votre hébergement est réservé pour trois nuits.'),
        x('Keep your receipts so that your travel expenses can be reimbursed.', 'Gardez vos reçus afin que vos frais de déplacement puissent être remboursés.'),
      ], [
        FB(COMPLETE, 'I missed my ＿ in Amsterdam because the first flight was late.', ['connection', 'link', 'transfer bus'], 'connection', ('Correspondance = connection.', 'Next flight in a journey = connection.'), ('J’ai raté ma correspondance à Amsterdam parce que le premier vol était en retard.', 'I missed my connection in Amsterdam because the first flight was late.')),
        FB(COMPLETE, 'Could we ＿ the meeting for next Tuesday?', ['reschedule', 'recharge', 'replace'], 'reschedule', ('Décaler = reschedule.', 'Move to a new time = reschedule.'), ('Pourrions-nous décaler la réunion à mardi prochain ?', 'Could we reschedule the meeting for next Tuesday?')),
        DC(ANSWER, [('Selkie', 'Window or aisle seat?')], ('À l’enregistrement.', 'At check-in.'), ['An aisle seat, please. I’ll need to get up.', 'Yes, a seat.', 'I sit the window, please me.'], 'An aisle seat, please. I’ll need to get up.', ('Réponse claire et polie.', 'Clear, polite answer.')),
        TF('Your travel expenses will be reimbursed.', ('L’entreprise remboursera les frais.', 'The company will pay back the costs.'), VRAI, ('reimbursed = remboursés.', 'reimbursed = paid back.')),
      ]),
  ])])

# ═════════════════════════ Île 6 : On dit que… ═════════════════════════
W6 = WORLD('b2-w6', ('La lavandière du gué', 'The washer at the ford'), REGION,
  ('Rapporter avec nuance : verbes introducteurs (admit, deny, insist) et passif impersonnel (It is said that…).', 'Report with nuance: reporting verbs (admit, deny, insist) and the impersonal passive (It is said that…).'),
  (('La Bean Nighe, lavandière du gué', 'The Bean Nighe, the washer at the ford'), 'm', ('Cette lavandière des Highlands lave les vêtements de ceux qui vont mourir. On dit qu’elle répond à trois questions si on la surprend : rapporte les rumeurs avec précision.', 'This Highland washerwoman washes the clothes of those about to die. It is said she answers three questions if you catch her: report the rumours precisely.')),
  [CH('b2-w6-c1', ('Il a nié…', 'He denied…'), [
    L('en-reporting-verbs', ('Les verbes introducteurs', 'Reporting verbs'), ('Rapporter des paroles avec le verbe qui en donne le sens.', 'Report speech with a verb that conveys its meaning.'), 10, [
        ('+ to : agree, offer, refuse, promise, threaten : He offered to help. + someone to : advise, remind, warn, persuade, encourage : She advised me to wait.', '+ to: agree, offer, refuse, promise, threaten: He offered to help. + someone to: advise, remind, warn, persuade, encourage: She advised me to wait.'),
        ('+ -ing : admit, deny, suggest, recommend : He denied taking the money. + préposition + -ing : apologise for, insist on, accuse someone of : She apologised for being late.', '+ -ing: admit, deny, suggest, recommend: He denied taking the money. + preposition + -ing: apologise for, insist on, accuse someone of: She apologised for being late.'),
      ], [
        EG('reporting-verbs', 'deny / admit / offer / insist on…', ('verbes introducteurs du discours', 'reporting verbs')),
        E('deny', 'to deny', ('nier', 'to deny')),
        E('admit', 'to admit', ('admettre, avouer', 'to admit')),
        E('insist', 'to insist on', ('insister pour', 'to insist on')),
        E('accuse', 'to accuse', ('accuser', 'to accuse')),
        E('persuade', 'to persuade', ('persuader, convaincre', 'to persuade')),
        E('threaten', 'to threaten', ('menacer', 'to threaten')),
      ], [
        x('The supplier denied sending the wrong goods.', 'Le fournisseur a nié avoir envoyé la mauvaise marchandise.'),
        x('Our lawyer advised us not to sign the contract.', 'Notre avocat nous a conseillé de ne pas signer le contrat.'),
      ], [
        FB(CHOOSE, 'He admitted ＿ the mistake.', ['making', 'to make', 'make'], 'making', ('admit + -ing.', 'admit + -ing.'), ('Il a reconnu avoir commis l’erreur.', 'He admitted making the mistake.')),
        FB(CHOOSE, 'She offered ＿ me to the station.', ['to drive', 'driving', 'drive'], 'to drive', ('offer + to.', 'offer + to.'), ('Elle a proposé de me conduire à la gare.', 'She offered to drive me to the station.')),
        FB(CHOOSE, 'The client insisted ＿ speaking to the manager.', ['on', 'to', 'for'], 'on', ('insist on + -ing.', 'insist on + -ing.'), ('Le client a insisté pour parler au responsable.', 'The client insisted on speaking to the manager.')),
        FB(CHOOSE, 'They accused him ＿ lying.', ['of', 'for', 'about'], 'of', ('accuse someone of + -ing.', 'accuse someone of + -ing.'), ('Ils l’ont accusé de mentir.', 'They accused him of lying.')),
      ]),
    L('en-impersonal-passive', ('Le passif impersonnel : It is said that…', 'The impersonal passive: It is said that…'), ('Rapporter une opinion générale ou une rumeur.', 'Report a general opinion or a rumour.'), 10, [
        ('It is said / believed / expected / reported that + phrase : It is expected that prices will rise.', 'It is said / believed / expected / reported that + clause: It is expected that prices will rise.'),
        ('Sujet + is said / believed + to + verbe : Prices are expected to rise. Pour le passé : to have + participe : The castle is believed to have been built in 1100.', 'Subject + is said / believed + to + verb: Prices are expected to rise. For the past: to have + participle: The castle is believed to have been built in 1100.'),
        ('Très fréquent dans la presse et les rapports.', 'Very common in news and reports.'),
      ], [
        EG('impersonal-passive', 'It is said that… / is said to…', ('passif impersonnel (on dit que…)', 'impersonal passive')),
        E('rumour', 'rumour', ('rumeur', 'rumour')),
        E('expected', 'expected', ('attendu, prévu', 'expected')),
        E('reportedly', 'reportedly', ('selon certaines sources', 'reportedly')),
        E('merger', 'merger', ('fusion (d’entreprises)', 'merger')),
        E('takeover', 'takeover', ('rachat, prise de contrôle', 'takeover')),
      ], [
        x('It is rumoured that the two companies are planning a merger.', 'On dit que les deux entreprises préparent une fusion.'),
        x('The CEO is reported to have resigned last night.', 'Le PDG aurait démissionné hier soir.'),
      ], [
        FB(CHOOSE, 'It ＿ that the economy will grow next year.', ['is expected', 'expects', 'is expecting'], 'is expected', ('It is expected that…', 'It is expected that…'), ('On s’attend à ce que l’économie croisse l’an prochain.', 'It is expected that the economy will grow next year.')),
        FB(CHOOSE, 'The company is said ＿ 5,000 people.', ['to employ', 'employing', 'that employs'], 'to employ', ('Sujet + is said to + verbe.', 'Subject + is said to + verb.'), ('L’entreprise emploierait 5 000 personnes.', 'The company is said to employ 5,000 people.')),
        FB(CHOOSE, 'The bridge is believed ＿ built by the Romans.', ['to have been', 'to be', 'having'], 'to have been', ('Passé : to have been + participe.', 'Past: to have been + participle.'), ('On pense que le pont a été construit par les Romains.', 'The bridge is believed to have been built by the Romans.')),
        TF('The minister has reportedly resigned.', ('La démission est confirmée officiellement.', 'The resignation is officially confirmed.'), FAUX, ('reportedly = selon certaines sources, non confirmé.', 'reportedly = according to reports, not confirmed.')),
      ]),
  ]),
  CH('b2-w6-c2', ('Le marketing', 'Marketing'), [
    L('en-marketing', ('Le marketing et la publicité', 'Marketing and advertising'), ('Parler de produits, de clients et de campagnes.', 'Talk about products, customers and campaigns.'), 9, [
        ('Le marché : target market (cible), market share (part de marché), competitor (concurrent), brand (marque), consumer (consommateur).', 'The market: target market, market share, competitor, brand, consumer.'),
        ('La campagne : advertising campaign, to promote, a special offer, a survey (enquête), customer feedback (retours clients).', 'The campaign: advertising campaign, to promote, a special offer, a survey, customer feedback.'),
      ], [
        E('brand', 'brand', ('marque', 'brand')),
        E('competitor', 'competitor', ('concurrent', 'competitor')),
        E('market-share', 'market share', ('part de marché', 'market share')),
        E('campaign', 'campaign', ('campagne', 'campaign')),
        E('survey', 'survey', ('enquête, sondage', 'survey')),
        E('feedback', 'feedback', ('retour, avis', 'feedback')),
        E('promote', 'to promote', ('promouvoir', 'to promote')),
      ], [
        x('Our main competitor has increased its market share to 30%.', 'Notre principal concurrent a porté sa part de marché à 30 %.'),
        x('Customer feedback from the survey was very positive.', 'Les retours clients de l’enquête étaient très positifs.'),
      ], [
        FB(COMPLETE, 'The campaign aims to ＿ our new range of sportswear.', ['promote', 'promise', 'propose'], 'promote', ('promouvoir = promote.', 'advertise = promote.'), ('La campagne vise à promouvoir notre nouvelle gamme de vêtements de sport.', 'The campaign aims to promote our new range of sportswear.')),
        FB(COMPLETE, 'We lost market ＿ to cheaper brands.', ['share', 'part', 'piece'], 'share', ('part de marché = market share.', 'market share.'), ('Nous avons perdu des parts de marché au profit de marques moins chères.', 'We lost market share to cheaper brands.')),
        FB(COMPLETE, 'Thank you for your ＿ on our new website.', ['feedback', 'answer back', 'advices'], 'feedback', ('Retour, avis = feedback (indénombrable).', 'feedback (uncountable).'), ('Merci pour vos retours sur notre nouveau site.', 'Thank you for your feedback on our new website.')),
        TF('Our competitors offer lower prices.', ('Les concurrents sont moins chers.', 'The competitors are cheaper.'), VRAI, ('competitors = concurrents.', 'competitors = rival companies.')),
      ]),
  ])])

# ═════════════════════════ Île 7 : Les tendances ═════════════════════════
W7 = WORLD('b2-w7', ('La chasse sauvage', 'The Wild Hunt'), REGION,
  ('Décrire des tendances et des chiffres : hausse, baisse, stabilité, comparaisons et quantités.', 'Describe trends and figures: rises, falls, stability, comparisons and quantities.'),
  (('Gwyn ap Nudd, roi des fées', 'Gwyn ap Nudd, king of the fairies'), 'd', ('Le roi de l’Autre Monde mène la Chasse sauvage dans le ciel gallois, ses chiens comptant chaque âme. Décris les chiffres sans erreur pour qu’il épargne la tienne.', 'The king of the Otherworld leads the Wild Hunt across the Welsh sky, his hounds counting every soul. Describe the figures without error and he will spare yours.')),
  [CH('b2-w7-c1', ('Les courbes', 'Graphs'), [
    L('en-trends', ('Décrire une tendance', 'Describing trends'), ('Commenter un graphique : verbes, noms et adverbes.', 'Comment on a graph: verbs, nouns and adverbs.'), 10, [
        ('Hausse : rise, increase, go up, grow, soar (s’envoler). Baisse : fall, decrease, drop, decline, plunge (chuter). Stabilité : remain stable, level off (se stabiliser), peak (atteindre un pic).', 'Up: rise, increase, go up, grow, soar. Down: fall, decrease, drop, decline, plunge. Stable: remain stable, level off, peak.'),
        ('Intensité : sharply, dramatically, significantly (fortement) ; slightly, gradually, steadily (légèrement, progressivement, régulièrement).', 'Degree: sharply, dramatically, significantly; slightly, gradually, steadily.'),
        ('Prépositions : rise by 5% (de 5 points), rise to 20% (jusqu’à 20 %), from 10 to 15 ; a rise in sales (une hausse des ventes).', 'Prepositions: rise by 5%, rise to 20%, from 10 to 15; a rise in sales.'),
      ], [
        EG('trends-by-to', 'rise by / rise to', ('augmenter de / augmenter jusqu’à', 'rise by / rise to')),
        E('rise', 'to rise', ('augmenter, monter', 'to rise')),
        E('decline', 'to decline', ('baisser, décliner', 'to decline')),
        E('sharply', 'sharply', ('fortement, brusquement', 'sharply')),
        E('slightly', 'slightly', ('légèrement', 'slightly')),
        E('steadily', 'steadily', ('régulièrement, constamment', 'steadily')),
        E('level-off', 'to level off', ('se stabiliser', 'to level off')),
        E('peak', 'to peak', ('atteindre un pic', 'to peak')),
      ], [
        x('Sales rose sharply in the first quarter, then levelled off in the summer.', 'Les ventes ont fortement augmenté au premier trimestre, puis se sont stabilisées en été.'),
        x('Unemployment fell by 2% to 5.5%.', 'Le chômage a baissé de 2 points pour s’établir à 5,5 %.'),
      ], [
        FB(CHOOSE, 'Profits rose ＿ 10% last year, from £5m to £5.5m.', ['by', 'to', 'of'], 'by', ('Écart : by.', 'The difference: by.'), ('Les bénéfices ont augmenté de 10 % l’an dernier, passant de 5 à 5,5 millions de livres.', 'Profits rose by 10% last year, from £5m to £5.5m.')),
        FB(CHOOSE, 'There was a sharp rise ＿ online sales.', ['in', 'of', 'at'], 'in', ('a rise in + nom.', 'a rise in + noun.'), ('Il y a eu une forte hausse des ventes en ligne.', 'There was a sharp rise in online sales.')),
        FB(CHOOSE, 'After months of growth, prices have ＿ off.', ['levelled', 'peaked', 'stayed'], 'levelled', ('Se stabiliser : level off.', 'Stop changing: level off.'), ('Après des mois de hausse, les prix se sont stabilisés.', 'After months of growth, prices have levelled off.')),
        TF('Sales increased slightly in May.', ('Les ventes ont explosé en mai.', 'Sales soared in May.'), FAUX, ('slightly = légèrement.', 'slightly = a little.')),
      ]),
    L('en-quantifiers', ('Les quantités : most, few, a great deal', 'Quantifiers: most, few, a great deal'), ('Exprimer des proportions avec précision.', 'Express proportions precisely.'), 9, [
        ('Dénombrables : many, a large number of, few (peu), a few (quelques-uns). Indénombrables : much, a great deal of, little (peu), a little (un peu).', 'Countable: many, a large number of, few, a few. Uncountable: much, a great deal of, little, a little.'),
        ('Proportions : most of the staff, the majority of, half of, a third of, none of, neither / either (sur deux).', 'Proportions: most of the staff, the majority of, half of, a third of, none of, neither / either (of two).'),
        ('Attention : few = peu (négatif), a few = quelques (positif) : Few people came (presque personne).', 'Careful: few = not many (negative), a few = some (positive): Few people came.'),
      ], [
        EG('few-a-few', 'few / a few, little / a little', ('peu / quelques, peu / un peu', 'few / a few, little / a little')),
        E('majority', 'majority', ('majorité', 'majority')),
        E('a-great-deal', 'a great deal of', ('beaucoup de (indénombrable)', 'a great deal of')),
        E('neither', 'neither', ('aucun des deux', 'neither')),
        E('proportion', 'proportion', ('proportion', 'proportion')),
      ], [
        x('The majority of our customers are under 35.', 'La majorité de nos clients ont moins de 35 ans.'),
        x('Few employees took part in the survey, so the results are not reliable.', 'Peu d’employés ont participé à l’enquête, donc les résultats ne sont pas fiables.'),
      ], [
        FB(CHOOSE, 'We have ＿ time left, so let’s hurry.', ['little', 'few', 'many'], 'little', ('Indénombrable, sens négatif : little.', 'Uncountable, negative: little.'), ('Il nous reste peu de temps, alors dépêchons-nous.', 'We have little time left, so let’s hurry.')),
        FB(CHOOSE, 'I have ＿ questions about the contract.', ['a few', 'a little', 'much'], 'a few', ('Dénombrable, quelques : a few.', 'Countable, some: a few.'), ('J’ai quelques questions sur le contrat.', 'I have a few questions about the contract.')),
        FB(CHOOSE, '＿ of the two candidates was suitable.', ['Neither', 'None', 'Either'], 'Neither', ('Aucun des deux : neither.', 'Not one of two: neither.'), ('Aucun des deux candidats ne convenait.', 'Neither of the two candidates was suitable.')),
        FB(CHOOSE, 'The project required a great ＿ of effort.', ['deal', 'number', 'many'], 'deal', ('a great deal of + indénombrable.', 'a great deal of + uncountable.'), ('Le projet a demandé beaucoup d’efforts.', 'The project required a great deal of effort.')),
      ]),
  ]),
  CH('b2-w7-c2', ('Les rapports', 'Reports'), [
    L('en-reports', ('Rédiger un rapport', 'Writing a report'), ('Structurer un rapport et formuler des recommandations.', 'Structure a report and make recommendations.'), 9, [
        ('Structure : Introduction (The aim of this report is to…), Findings (It was found that…), Conclusion, Recommendations (It is recommended that… / We would suggest…).', 'Structure: Introduction (The aim of this report is to…), Findings (It was found that…), Conclusion, Recommendations (It is recommended that… / We would suggest…).'),
        ('Liens formels : due to / owing to (en raison de), as a result (par conséquent), in addition (de plus), on the other hand (en revanche).', 'Formal links: due to / owing to, as a result, in addition, on the other hand.'),
      ], [
        E('aim', 'aim', ('but, objectif', 'aim')),
        E('findings', 'findings', ('conclusions, résultats (d’une étude)', 'findings')),
        E('recommend', 'to recommend', ('recommander', 'to recommend')),
        E('due-to', 'due to', ('en raison de, à cause de', 'due to')),
        E('as-a-result', 'as a result', ('par conséquent, en conséquence', 'as a result')),
        E('in-addition', 'in addition', ('de plus, en outre', 'in addition')),
      ], [
        x('The aim of this report is to assess customer satisfaction.', 'Ce rapport a pour objectif d’évaluer la satisfaction des clients.'),
        x('Due to rising costs, it is recommended that prices be reviewed.', 'En raison de la hausse des coûts, il est recommandé de revoir les prix.'),
      ], [
        FB(COMPLETE, 'The ＿ of this report is to compare two suppliers.', ['aim', 'end', 'goal of'], 'aim', ('The aim of this report is to…', 'The aim of this report is to…'), ('Ce rapport a pour but de comparer deux fournisseurs.', 'The aim of this report is to compare two suppliers.')),
        FB(COMPLETE, 'The flight was cancelled ＿ to bad weather.', ['due', 'because', 'thanks'], 'due', ('due to + nom.', 'due to + noun.'), ('Le vol a été annulé en raison du mauvais temps.', 'The flight was cancelled due to bad weather.')),
        FB(COMPLETE, 'Sales fell. As a ＿, three shops were closed.', ['result', 'consequence of', 'reason'], 'result', ('As a result = par conséquent.', 'As a result = therefore.'), ('Les ventes ont baissé. Par conséquent, trois magasins ont fermé.', 'Sales fell. As a result, three shops were closed.')),
        TF('The findings show that customers are satisfied.', ('Les résultats de l’étude montrent une satisfaction.', 'The study results show satisfaction.'), VRAI, ('findings = résultats d’une étude.', 'findings = results of a study.')),
      ]),
  ])])

# ═════════════════════════ Île 8 : Le défi ═════════════════════════
W8 = WORLD('b2-w8', ('La trahison de Mordred', 'Mordred’s treachery'), REGION,
  ('Argumenter et persuader : inversions d’insistance simples, phrases emphatiques et langage diplomatique.', 'Argue and persuade: simple emphatic inversion, cleft sentences and diplomatic language.'),
  (('Mordred, le traître', 'Mordred the traitor'), 'k', ('Neveu d’Arthur, Mordred a profité de l’absence du roi pour s’emparer du trône. Il tente de rallier les chevaliers par de beaux discours : convaincs-les mieux que lui, avec des arguments impeccables.', 'Arthur’s nephew, Mordred seized the throne while the king was away. He tries to win the knights over with fine speeches: persuade them better than he does, with flawless arguments.')),
  [CH('b2-w8-c1', ('Insister', 'Emphasis'), [
    L('en-cleft', ('Les phrases emphatiques : What we need is…', 'Cleft sentences: What we need is…'), ('Mettre en relief une idée avec It is… that et What… is.', 'Highlight an idea with It is… that and What… is.'), 10, [
        ('It is / was + élément + that / who : It was Sarah who found the solution (c’est Sarah qui…).', 'It is / was + element + that / who: It was Sarah who found the solution.'),
        ('What + sujet + verbe + is : What we need is more time. What I like about this job is the variety.', 'What + subject + verb + is: What we need is more time. What I like about this job is the variety.'),
        ('Insister avec do / does / did : I do understand your concerns (je comprends vraiment).', 'Emphatic do / does / did: I do understand your concerns.'),
      ], [
        EG('cleft-it', 'It is… that / who…', ('c’est… qui / que (mise en relief)', 'cleft sentence (It is… that)')),
        EG('cleft-what', 'What… is…', ('ce dont… c’est… (mise en relief)', 'cleft sentence (What… is)')),
        E('concern', 'concern', ('inquiétude, préoccupation', 'concern')),
        E('variety', 'variety', ('variété', 'variety')),
        E('crucial', 'crucial', ('crucial, essentiel', 'crucial')),
      ], [
        x('What our clients really want is faster delivery.', 'Ce que nos clients veulent vraiment, c’est une livraison plus rapide.'),
        x('It was the marketing team that came up with the idea.', 'C’est l’équipe marketing qui a eu l’idée.'),
      ], [
        FB(CHOOSE, '＿ we need is a better plan.', ['What', 'That', 'Which'], 'What', ('What + sujet + verbe + is.', 'What + subject + verb + is.'), ('Ce qu’il nous faut, c’est un meilleur plan.', 'What we need is a better plan.')),
        FB(CHOOSE, 'It was Tom ＿ broke the printer.', ['who', 'which', 'what'], 'who', ('It was + personne + who.', 'It was + person + who.'), ('C’est Tom qui a cassé l’imprimante.', 'It was Tom who broke the printer.')),
        FB(CHOOSE, 'I ＿ understand your concerns, but we must decide today.', ['do', 'am', 'have'], 'do', ('do d’insistance + base verbale.', 'Emphatic do + base verb.'), ('Je comprends vraiment vos inquiétudes, mais nous devons décider aujourd’hui.', 'I do understand your concerns, but we must decide today.')),
        TF('What I like about the job is the travel.', ('La personne aime surtout les déplacements.', 'The person especially likes travelling.'), VRAI, ('Mise en relief de the travel.', 'Emphasis on the travel.')),
      ]),
    L('en-inversion-b2', ('L’inversion d’insistance : Not only…, Never…', 'Emphatic inversion: Not only…, Never…'), ('Utiliser les inversions les plus courantes à l’écrit formel.', 'Use the most common inversions in formal writing.'), 10, [
        ('Après certaines expressions négatives en tête de phrase, on inverse auxiliaire et sujet : Never have I seen such a mess. Not only did he arrive late, but he also forgot the documents.', 'After some negative expressions at the start, the auxiliary and subject are inverted: Never have I seen such a mess. Not only did he arrive late, but he also forgot the documents.'),
        ('Autres : Rarely…, Under no circumstances…, Only then… : Under no circumstances should you share your password.', 'Others: Rarely…, Under no circumstances…, Only then…: Under no circumstances should you share your password.'),
      ], [
        EG('inversion', 'Never have I… / Not only did…', ('inversion après une expression négative', 'negative inversion')),
        E('not-only', 'not only… but also', ('non seulement… mais aussi', 'not only… but also')),
        E('under-no-circumstances', 'under no circumstances', ('en aucun cas', 'under no circumstances')),
        E('password', 'password', ('mot de passe', 'password')),
      ], [
        x('Not only did we meet the deadline, but we also stayed under budget.', 'Non seulement nous avons respecté l’échéance, mais nous sommes aussi restés sous le budget.'),
        x('Under no circumstances should this door be left open.', 'Cette porte ne doit en aucun cas rester ouverte.'),
      ], [
        FB(CHOOSE, 'Never ＿ such a beautiful view.', ['have I seen', 'I have seen', 'I saw'], 'have I seen', ('Inversion : auxiliaire + sujet.', 'Inversion: auxiliary + subject.'), ('Jamais je n’ai vu une si belle vue.', 'Never have I seen such a beautiful view.')),
        FB(CHOOSE, 'Not only ＿ late, but he also forgot his laptop.', ['did he arrive', 'he arrived', 'he did arrive'], 'did he arrive', ('Not only + did + sujet + base verbale.', 'Not only + did + subject + base verb.'), ('Non seulement il est arrivé en retard, mais il a aussi oublié son ordinateur.', 'Not only did he arrive late, but he also forgot his laptop.')),
        FB(CHOOSE, 'Under no circumstances ＿ your password with anyone.', ['should you share', 'you should share', 'share you'], 'should you share', ('Inversion : should + sujet.', 'Inversion: should + subject.'), ('Ne communiquez en aucun cas votre mot de passe.', 'Under no circumstances should you share your password with anyone.')),
        TF('Rarely do we receive complaints.', ('Les réclamations sont fréquentes.', 'Complaints are frequent.'), FAUX, ('Rarely = rarement.', 'Rarely = not often.')),
      ]),
  ]),
  CH('b2-w8-c2', ('La diplomatie', 'Diplomacy'), [
    L('en-diplomatic', ('Le langage diplomatique', 'Diplomatic language'), ('Adoucir un désaccord, une critique ou un refus.', 'Soften disagreement, criticism or refusal.'), 9, [
        ('Adoucir : I’m afraid… / It seems that… / We might want to… / Wouldn’t it be better to…?', 'Softening: I’m afraid… / It seems that… / We might want to… / Wouldn’t it be better to…?'),
        ('Remplacer un mot négatif : not very / not entirely + adjectif positif : The results are not entirely satisfactory (au lieu de bad).', 'Replace a negative word: not very / not entirely + positive adjective: The results are not entirely satisfactory (instead of bad).'),
        ('Refuser : Unfortunately, we are unable to… / I’m not in a position to…', 'Refusing: Unfortunately, we are unable to… / I’m not in a position to…'),
      ], [
        E('unfortunately', 'unfortunately', ('malheureusement', 'unfortunately')),
        E('unable', 'unable to', ('dans l’impossibilité de', 'unable to')),
        E('entirely', 'entirely', ('entièrement, tout à fait', 'entirely')),
        E('in-a-position', 'in a position to', ('en mesure de', 'in a position to')),
        E('appreciate', 'to appreciate', ('apprécier, être reconnaissant de', 'to appreciate')),
      ], [
        x('I’m afraid we’re not in a position to offer a bigger discount.', 'Je crains que nous ne soyons pas en mesure d’accorder une remise plus importante.'),
        x('The report is not entirely accurate. We might want to check the figures again.', 'Le rapport n’est pas tout à fait exact. Il faudrait peut-être revérifier les chiffres.'),
      ], [
        DC(ANSWER, [('Mordred', 'Your plan is a disaster!')], ('Mordred critique durement ton plan. Réponds avec diplomatie.', 'Mordred harshly criticises your plan. Answer diplomatically.'), ['I appreciate your feedback. Perhaps we could look at it together?', 'No, your plan is a disaster!', 'Be quiet, please.'], 'I appreciate your feedback. Perhaps we could look at it together?', ('Remercier puis proposer.', 'Thank, then propose.')),
        FB(COMPLETE, 'Unfortunately, we are ＿ to deliver before June.', ['unable', 'impossible', 'not possible'], 'unable', ('be unable to = ne pas pouvoir.', 'be unable to = cannot.'), ('Malheureusement, nous ne sommes pas en mesure de livrer avant juin.', 'Unfortunately, we are unable to deliver before June.')),
        FB(COMPLETE, 'The results are not ＿ satisfactory.', ['entirely', 'whole', 'complete'], 'entirely', ('not entirely = pas tout à fait.', 'not entirely = not completely.'), ('Les résultats ne sont pas tout à fait satisfaisants.', 'The results are not entirely satisfactory.')),
        TF('I’m not in a position to accept your offer.', ('La personne accepte l’offre.', 'The person accepts the offer.'), FAUX, ('not in a position to = pas en mesure de.', 'not in a position to = unable to.')),
      ]),
  ])])

write_level('B2', ('B2 : la trahison de Mordred', 'B2: Mordred’s treachery'), REGION, 'Welsh Marches', 27,
  [W1, W2, W3, W4, W5, W6, W7, W8, FINAL('B2', REGION, ('Simulation TOEIC B2 : la bataille de Camlann', 'TOEIC B2 simulation: the battle of Camlann'), 785)], PREVIOUS + ['content/a2/a2.json', 'content/b1/b1.json'])
