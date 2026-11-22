# Niveau C1 (anglais, CECRL C1, préparation au TOEIC) : 8 îles, 24 leçons et un examen blanc TOEIC (français + anglais).
# Mode histoire : le retour d'Excalibur à la Dame du Lac, direction d'Avalon & Co.
# Usage : python3 scripts/c1-level.py   (réécrit content/c1/c1.json)
from en_common import *

REGION = 'Îles du Nord'

# ═════════════════════════ Île 1 : Hypothèses formelles ═════════════════════════
W1 = WORLD('c1-w1', ('Le démon de la mer', 'The sea demon'), REGION,
  ('Formuler des hypothèses au registre soutenu : inversions conditionnelles, but for, otherwise, suppose.', 'Express hypotheses in a formal register: conditional inversion, but for, otherwise, suppose.'),
  (('Le Nuckelavee des Orcades', 'The Nuckelavee of Orkney'), 'n', ('Ce démon marin, mi-cheval mi-homme et sans peau, sème la maladie sur les îles. Seuls ceux qui maîtrisent les hypothèses les plus subtiles peuvent le repousser vers la mer.', 'This skinless sea demon, half horse and half man, spreads disease across the islands. Only those who master the subtlest hypotheses can drive it back to the sea.')),
  [CH('c1-w1-c1', ('Si jamais…', 'Should you…'), [
    L('en-conditional-inversion', ('L’inversion conditionnelle : Should you…, Had I…', 'Conditional inversion: Should you…, Had I…'), ('Remplacer if par une inversion dans les écrits formels.', 'Replace if with inversion in formal writing.'), 10, [
        ('Should + sujet + verbe = If… (éventualité) : Should you require further information, please contact us.', 'Should + subject + verb = If… (possibility): Should you require further information, please contact us.'),
        ('Were + sujet + to / were = deuxième conditionnel : Were we to accept the offer, we would need more staff.', 'Were + subject + to / were = second conditional: Were we to accept the offer, we would need more staff.'),
        ('Had + sujet + participe = troisième conditionnel : Had I known, I would have acted differently. La négation ne se contracte pas : Had it not been for…', 'Had + subject + participle = third conditional: Had I known, I would have acted differently. The negative is not contracted: Had it not been for…'),
      ], [
        EG('conditional-inversion', 'Should you… / Were we to… / Had I known…', ('inversion conditionnelle (registre soutenu)', 'conditional inversion')),
        E('require', 'to require', ('avoir besoin de, exiger', 'to require')),
        E('further', 'further', ('supplémentaire, complémentaire', 'further')),
        E('hesitate', 'to hesitate', ('hésiter', 'to hesitate')),
        E('proceed', 'to proceed', ('procéder, poursuivre', 'to proceed')),
        E('acquisition', 'acquisition', ('acquisition, rachat', 'acquisition')),
      ], [
        x('Should you have any questions, please do not hesitate to contact me.', 'Pour toute question, n’hésitez pas à me contacter.'),
        x('Had the board approved the acquisition, we would now be the market leader.', 'Si le conseil avait approuvé l’acquisition, nous serions aujourd’hui leader du marché.'),
      ], [
        FB(CHOOSE, '＿ you require any assistance, our staff will be happy to help.', ['Should', 'Would', 'Had'], 'Should', ('Éventualité : Should + sujet.', 'Possibility: Should + subject.'), ('Si vous avez besoin d’aide, notre personnel se fera un plaisir de vous aider.', 'Should you require any assistance, our staff will be happy to help.')),
        FB(CHOOSE, '＿ we known about the problem, we would have acted sooner.', ['Had', 'Should', 'Were'], 'Had', ('Passé irréel : Had + sujet + participe.', 'Past unreal: Had + subject + participle.'), ('Si nous avions été au courant du problème, nous aurions agi plus tôt.', 'Had we known about the problem, we would have acted sooner.')),
        FB(CHOOSE, 'Were the company ＿ relocate, many staff would resign.', ['to', 'for', 'and'], 'to', ('Were + sujet + to + verbe.', 'Were + subject + to + verb.'), ('Si l’entreprise devait déménager, beaucoup de salariés démissionneraient.', 'Were the company to relocate, many staff would resign.')),
        FB(CHOOSE, 'Had it ＿ been for your help, we would have failed.', ['not', 'no', 'n’t'], 'not', ('Négation non contractée : Had it not been for…', 'Uncontracted negative: Had it not been for…'), ('Sans ton aide, nous aurions échoué.', 'Had it not been for your help, we would have failed.')),
      ]),
    L('en-but-for', ('But for, otherwise, provided, supposing', 'But for, otherwise, provided, supposing'), ('Varier l’expression de la condition.', 'Vary the way you express conditions.'), 10, [
        ('but for + nom = sans : But for the delay, we would have finished (sans le retard…). otherwise = sinon : Book now; otherwise, you may not get a seat.', 'but for + noun = without: But for the delay, we would have finished. otherwise = if not: Book now; otherwise, you may not get a seat.'),
        ('provided / providing (that), as long as, on condition that = à condition que ; unless = à moins que ; supposing / suppose = imaginons que ; in case = au cas où (précaution).', 'provided / providing (that), as long as, on condition that; unless; supposing / suppose; in case (as a precaution).'),
        ('Attention : in case n’est pas if : Take an umbrella in case it rains (par précaution).', 'Careful: in case is not if: Take an umbrella in case it rains (as a precaution).'),
      ], [
        EG('but-for', 'but for / otherwise', ('sans / sinon', 'but for / otherwise')),
        EG('in-case', 'in case / unless / supposing', ('au cas où / à moins que / imaginons que', 'in case / unless / supposing')),
        E('otherwise', 'otherwise', ('sinon, autrement', 'otherwise')),
        E('unless', 'unless', ('à moins que, sauf si', 'unless')),
        E('supposing', 'supposing', ('imaginons que, à supposer que', 'supposing')),
        E('on-condition', 'on condition that', ('à condition que', 'on condition that')),
      ], [
        x('But for the strong pound, our exports would have increased.', 'Sans la vigueur de la livre, nos exportations auraient augmenté.'),
        x('We will sign, on condition that the delivery date is guaranteed.', 'Nous signerons, à condition que la date de livraison soit garantie.'),
      ], [
        FB(CHOOSE, '＿ the bad weather, the event would have been a success.', ['But for', 'Unless', 'Otherwise'], 'But for', ('But for + nom = sans.', 'But for + noun = without.'), ('Sans le mauvais temps, l’événement aurait été un succès.', 'But for the bad weather, the event would have been a success.')),
        FB(CHOOSE, 'Save your work regularly; ＿, you may lose everything.', ['otherwise', 'unless', 'in case'], 'otherwise', ('Sinon : otherwise.', 'If not: otherwise.'), ('Enregistre régulièrement ton travail ; sinon, tu risques de tout perdre.', 'Save your work regularly; otherwise, you may lose everything.')),
        FB(CHOOSE, 'Take some cash ＿ the card machine isn’t working.', ['in case', 'unless', 'provided'], 'in case', ('Par précaution : in case.', 'As a precaution: in case.'), ('Prends du liquide au cas où le terminal de paiement ne marcherait pas.', 'Take some cash in case the card machine isn’t working.')),
        FB(CHOOSE, 'We won’t finish on time ＿ we hire more staff.', ['unless', 'provided', 'in case'], 'unless', ('À moins que : unless.', 'Except if: unless.'), ('Nous ne finirons pas à temps à moins d’embaucher plus de personnel.', 'We won’t finish on time unless we hire more staff.')),
      ]),
  ]),
  CH('c1-w1-c2', ('La stratégie', 'Strategy'), [
    L('en-strategy', ('Parler stratégie d’entreprise', 'Discussing business strategy'), ('Analyser des options stratégiques et leurs risques.', 'Analyse strategic options and their risks.'), 9, [
        ('Vocabulaire : a long-term strategy, to diversify (se diversifier), to expand into a market, a stakeholder (partie prenante), a shareholder (actionnaire), the board (conseil d’administration).', 'Vocabulary: a long-term strategy, to diversify, to expand into a market, a stakeholder, a shareholder, the board.'),
        ('Peser les options : The main advantage of… is… / This would entail (impliquer)… / There is a risk that… / On balance, I would recommend…', 'Weighing options: The main advantage of… is… / This would entail… / There is a risk that… / On balance, I would recommend…'),
      ], [
        E('strategy', 'strategy', ('stratégie', 'strategy')),
        E('diversify', 'to diversify', ('diversifier, se diversifier', 'to diversify')),
        E('stakeholder', 'stakeholder', ('partie prenante', 'stakeholder')),
        E('shareholder', 'shareholder', ('actionnaire', 'shareholder')),
        E('board', 'the board', ('le conseil d’administration', 'the board')),
        E('entail', 'to entail', ('impliquer, entraîner', 'to entail')),
        E('on-balance', 'on balance', ('tout bien considéré', 'on balance')),
      ], [
        x('Expanding into Asia would entail significant investment.', 'Une expansion en Asie impliquerait des investissements importants.'),
        x('On balance, I would recommend diversifying our product range.', 'Tout bien considéré, je recommanderais de diversifier notre gamme de produits.'),
      ], [
        FB(COMPLETE, 'The proposal will be presented to the ＿ on Monday.', ['board', 'table', 'chair'], 'board', ('Conseil d’administration = the board.', 'Company directors = the board.'), ('La proposition sera présentée au conseil d’administration lundi.', 'The proposal will be presented to the board on Monday.')),
        FB(COMPLETE, 'The merger would ＿ closing two factories.', ['entail', 'enter', 'entitle'], 'entail', ('Impliquer = entail.', 'Involve = entail.'), ('La fusion impliquerait la fermeture de deux usines.', 'The merger would entail closing two factories.')),
        FB(COMPLETE, 'On ＿, the risks outweigh the benefits.', ['balance', 'whole', 'weight'], 'balance', ('Tout bien considéré : on balance.', 'All things considered: on balance.'), ('Tout bien considéré, les risques l’emportent sur les avantages.', 'On balance, the risks outweigh the benefits.')),
        TF('Shareholders received a higher dividend this year.', ('Les actionnaires ont touché plus.', 'The shareholders received more.'), VRAI, ('shareholders = actionnaires.', 'shareholders = owners of shares.')),
      ]),
  ])])

# ═════════════════════════ Île 2 : Expressions idiomatiques ═════════════════════════
W2 = WORLD('c1-w2', ('Le détroit du Minch', 'The Minch strait'), REGION,
  ('Comprendre et employer les expressions idiomatiques et les collocations du monde professionnel.', 'Understand and use idioms and collocations from the business world.'),
  (('Les Hommes bleus du Minch', 'The Blue Men of the Minch'), 'p', ('Ces esprits des flots soulèvent des tempêtes et défient les capitaines en vers. Celui qui répond avec la bonne expression peut passer le détroit en paix.', 'These spirits of the waves raise storms and challenge captains in verse. Whoever answers with the right expression may cross the strait in peace.')),
  [CH('c1-w2-c1', ('Les idiomes', 'Idioms'), [
    L('en-business-idioms', ('Les idiomes du bureau', 'Office idioms'), ('Comprendre les idiomes courants dans les réunions.', 'Understand idioms common in meetings.'), 10, [
        ('to get the ball rolling (lancer les choses), to be on the same page (être sur la même longueur d’onde), to think outside the box (sortir des sentiers battus).', 'to get the ball rolling, to be on the same page, to think outside the box.'),
        ('to cut corners (bâcler pour économiser), to call it a day (s’arrêter là pour aujourd’hui), a ballpark figure (un ordre de grandeur), back to the drawing board (retour à la case départ).', 'to cut corners, to call it a day, a ballpark figure, back to the drawing board.'),
      ], [
        E('ball-rolling', 'to get the ball rolling', ('lancer les choses, démarrer', 'to get the ball rolling')),
        E('same-page', 'to be on the same page', ('être sur la même longueur d’onde', 'to be on the same page')),
        E('cut-corners', 'to cut corners', ('rogner sur la qualité, bâcler', 'to cut corners')),
        E('call-it-a-day', 'to call it a day', ('s’arrêter là (pour aujourd’hui)', 'to call it a day')),
        E('ballpark', 'a ballpark figure', ('un ordre de grandeur, une estimation', 'a ballpark figure')),
        E('drawing-board', 'back to the drawing board', ('retour à la case départ', 'back to the drawing board')),
      ], [
        x('Let’s get the ball rolling: who wants to present first?', 'Lançons-nous : qui veut présenter en premier ?'),
        x('The client rejected the design, so it’s back to the drawing board.', 'Le client a refusé la maquette, donc retour à la case départ.'),
      ], [
        FB(COMPLETE, 'Can you give me a ＿ figure for the total cost?', ['ballpark', 'football', 'park'], 'ballpark', ('Une estimation : a ballpark figure.', 'An estimate: a ballpark figure.'), ('Peux-tu me donner un ordre de grandeur du coût total ?', 'Can you give me a ballpark figure for the total cost?')),
        FB(COMPLETE, 'We’ve been working for ten hours. Let’s call it a ＿.', ['day', 'time', 'job'], 'day', ('S’arrêter là : call it a day.', 'Stop working: call it a day.'), ('On travaille depuis dix heures. Arrêtons-nous là.', 'We’ve been working for ten hours. Let’s call it a day.')),
        FB(COMPLETE, 'If we cut ＿, the product will be unsafe.', ['corners', 'edges', 'costs down'], 'corners', ('Bâcler : cut corners.', 'Do things badly to save money: cut corners.'), ('Si nous rognons sur la qualité, le produit sera dangereux.', 'If we cut corners, the product will be unsafe.')),
        TF('Before we start, let’s make sure we’re all on the same page.', ('L’orateur veut que tout le monde soit d’accord sur les bases.', 'The speaker wants everyone to share the same understanding.'), VRAI, ('on the same page = même compréhension.', 'on the same page = in agreement.')),
      ]),
    L('en-collocations', ('Les collocations : make, do, take, raise', 'Collocations: make, do, take, raise'), ('Associer les bons verbes et les bons noms.', 'Match the right verbs and nouns.'), 10, [
        ('make : a decision, a profit, a complaint, an effort, progress, arrangements. do : business, research, a favour, harm, your best.', 'make: a decision, a profit, a complaint, an effort, progress, arrangements. do: business, research, a favour, harm, your best.'),
        ('take : action, part, place, advantage of, responsibility. raise : a question, an issue, funds, awareness. meet : a deadline, a demand. reach : an agreement.', 'take: action, part, place, advantage of, responsibility. raise: a question, an issue, funds, awareness. meet: a deadline, a demand. reach: an agreement.'),
      ], [
        EG('collocations', 'make a decision / do business / take action', ('collocations verbe + nom', 'verb + noun collocations')),
        E('raise-issue', 'to raise an issue', ('soulever un problème', 'to raise an issue')),
        E('take-advantage', 'to take advantage of', ('profiter de', 'to take advantage of')),
        E('do-business', 'to do business', ('faire des affaires', 'to do business')),
        E('reach-agreement', 'to reach an agreement', ('parvenir à un accord', 'to reach an agreement')),
        E('raise-funds', 'to raise funds', ('lever des fonds', 'to raise funds')),
      ], [
        x('We need to take action before the situation gets worse.', 'Nous devons agir avant que la situation ne s’aggrave.'),
        x('After long talks, the unions and management reached an agreement.', 'Après de longues discussions, les syndicats et la direction sont parvenus à un accord.'),
      ], [
        FB(CHOOSE, 'We have ＿ good progress this month.', ['made', 'done', 'taken'], 'made', ('make progress.', 'make progress.'), ('Nous avons bien progressé ce mois-ci.', 'We have made good progress this month.')),
        FB(CHOOSE, 'The start-up ＿ two million pounds from investors.', ['raised', 'rose', 'lifted'], 'raised', ('Lever des fonds : raise funds (raise transitif).', 'raise funds (raise is transitive).'), ('La jeune pousse a levé deux millions de livres auprès d’investisseurs.', 'The start-up raised two million pounds from investors.')),
        FB(CHOOSE, 'Could you ＿ me a favour and check this report?', ['do', 'make', 'give'], 'do', ('do someone a favour.', 'do someone a favour.'), ('Pourrais-tu me rendre service et vérifier ce rapport ?', 'Could you do me a favour and check this report?')),
        FB(CHOOSE, 'The conference will ＿ place in Edinburgh.', ['take', 'make', 'have'], 'take', ('take place = avoir lieu.', 'take place = happen.'), ('Le congrès aura lieu à Édimbourg.', 'The conference will take place in Edinburgh.')),
      ]),
  ]),
  CH('c1-w2-c2', ('Les verbes à particule', 'Phrasal verbs'), [
    L('en-phrasal-business', ('Verbes à particule du monde des affaires', 'Business phrasal verbs'), ('Maîtriser les verbes à particule fréquents au TOEIC.', 'Master phrasal verbs common in the TOEIC.'), 10, [
        ('set up (créer), carry out (réaliser), take over (racheter, reprendre), draw up (rédiger un contrat), go through (examiner en détail), look into (étudier, enquêter).', 'set up, carry out, take over, draw up, go through, look into.'),
        ('bring forward (avancer une date), put off (repousser), call off (annuler), fall through (échouer, tomber à l’eau), run out of (être à court de), follow up (assurer le suivi).', 'bring forward, put off, call off, fall through, run out of, follow up.'),
      ], [
        EG('phrasal-verbs', 'set up / carry out / take over…', ('verbes à particule', 'phrasal verbs')),
        E('carry-out', 'to carry out', ('réaliser, effectuer', 'to carry out')),
        E('draw-up', 'to draw up', ('rédiger, établir (un document)', 'to draw up')),
        E('look-into', 'to look into', ('étudier, examiner', 'to look into')),
        E('bring-forward', 'to bring forward', ('avancer (une date)', 'to bring forward')),
        E('call-off', 'to call off', ('annuler', 'to call off')),
        E('fall-through', 'to fall through', ('échouer, tomber à l’eau', 'to fall through')),
        E('follow-up', 'to follow up', ('assurer le suivi, relancer', 'to follow up')),
      ], [
        x('Our lawyers are drawing up the contract and will send it on Friday.', 'Nos avocats rédigent le contrat et l’enverront vendredi.'),
        x('The deal fell through at the last minute, so the launch has been called off.', 'L’accord est tombé à l’eau à la dernière minute, donc le lancement a été annulé.'),
      ], [
        FB(CHOOSE, 'The meeting has been brought ＿ to Monday.', ['forward', 'up', 'off'], 'forward', ('Avancer une date : bring forward.', 'Move earlier: bring forward.'), ('La réunion a été avancée à lundi.', 'The meeting has been brought forward to Monday.')),
        FB(CHOOSE, 'We will look ＿ your complaint and reply within 48 hours.', ['into', 'after', 'up'], 'into', ('Étudier : look into.', 'Investigate: look into.'), ('Nous allons étudier votre réclamation et répondre sous 48 heures.', 'We will look into your complaint and reply within 48 hours.')),
        FB(CHOOSE, 'The survey was carried ＿ by an independent agency.', ['out', 'on', 'over'], 'out', ('Réaliser : carry out.', 'Do: carry out.'), ('L’enquête a été réalisée par un organisme indépendant.', 'The survey was carried out by an independent agency.')),
        FB(CHOOSE, 'We have run ＿ of paper for the printer.', ['out', 'off', 'down'], 'out', ('Être à court : run out of.', 'Have none left: run out of.'), ('Nous n’avons plus de papier pour l’imprimante.', 'We have run out of paper for the printer.')),
      ]),
  ])])

# ═════════════════════════ Île 3 : Les propositions participiales ═════════════════════════
W3 = WORLD('c1-w3', ('Le loup des Shetland', 'The Shetland wolf'), REGION,
  ('Condenser sa pensée : propositions participiales, liens logiques avancés (given that, whereby, hence).', 'Condense your ideas: participle clauses, advanced linkers (given that, whereby, hence).'),
  (('Le Wulver des Shetland', 'The Wulver of Shetland'), 'g', ('Homme à tête de loup, le Wulver est un sage solitaire qui laisse du poisson aux familles pauvres. Il n’aime pas les longues phrases maladroites : sois concis et précis.', 'A man with a wolf’s head, the Wulver is a solitary sage who leaves fish for poor families. He dislikes long clumsy sentences: be concise and precise.')),
  [CH('c1-w3-c1', ('Condenser', 'Condensing'), [
    L('en-participle-clauses', ('Les propositions participiales', 'Participle clauses'), ('Remplacer une subordonnée par un participe.', 'Replace a subordinate clause with a participle.'), 10, [
        ('-ing pour une action simultanée ou une cause : Walking into the office, I noticed the smell. Feeling tired, she went home.', '-ing for a simultaneous action or a cause: Walking into the office, I noticed the smell. Feeling tired, she went home.'),
        ('Having + participe pour une action antérieure : Having finished the report, he left (après avoir fini…).', 'Having + participle for an earlier action: Having finished the report, he left.'),
        ('Participe passé pour le sens passif : Built in 1890, the hotel has been fully renovated. Le sujet doit être le même dans les deux parties !', 'Past participle for passive meaning: Built in 1890, the hotel has been fully renovated. The subject must be the same in both parts!'),
      ], [
        EG('participle-clauses', 'Having finished…, / Built in…,', ('proposition participiale', 'participle clauses')),
        E('renovate', 'to renovate', ('rénover', 'to renovate')),
        E('notice', 'to notice', ('remarquer', 'to notice')),
        E('fully', 'fully', ('entièrement, pleinement', 'fully')),
        E('assess', 'to assess', ('évaluer', 'to assess')),
      ], [
        x('Having reviewed your application, we are pleased to offer you the position.', 'Après examen de votre candidature, nous avons le plaisir de vous proposer le poste.'),
        x('Located in the heart of Edinburgh, the hotel offers stunning views of the castle.', 'Situé au cœur d’Édimbourg, l’hôtel offre une vue imprenable sur le château.'),
      ], [
        FB(CHOOSE, '＿ the figures, the director approved the budget.', ['Having checked', 'Checked', 'Having check'], 'Having checked', ('Action antérieure : Having + participe.', 'Earlier action: Having + participle.'), ('Après avoir vérifié les chiffres, le directeur a approuvé le budget.', 'Having checked the figures, the director approved the budget.')),
        FB(CHOOSE, '＿ in 1890, the bridge is still in use today.', ['Built', 'Building', 'Having built'], 'Built', ('Sens passif : participe passé.', 'Passive meaning: past participle.'), ('Construit en 1890, le pont est toujours utilisé aujourd’hui.', 'Built in 1890, the bridge is still in use today.')),
        FB(CHOOSE, '＿ that the store was closed, we went home.', ['Seeing', 'Seen', 'Saw'], 'Seeing', ('Cause, sens actif : -ing.', 'Cause, active meaning: -ing.'), ('Voyant que le magasin était fermé, nous sommes rentrés.', 'Seeing that the store was closed, we went home.')),
        TF('Having signed the contract, the client left.', ('Le client est parti avant de signer.', 'The client left before signing.'), FAUX, ('Having signed = après avoir signé.', 'Having signed = after signing.')),
      ]),
    L('en-advanced-linkers', ('Liens logiques avancés', 'Advanced linkers'), ('Relier ses idées avec précision dans un écrit formel.', 'Link ideas precisely in formal writing.'), 10, [
        ('Cause : given that, in view of, seeing that, on account of. Conséquence : hence, thus, consequently, thereby.', 'Cause: given that, in view of, seeing that, on account of. Result: hence, thus, consequently, thereby.'),
        ('Concession : albeit (bien que), notwithstanding (nonobstant), even so. whereby = par lequel : a system whereby customers can pay online.', 'Concession: albeit, notwithstanding, even so. whereby = by which: a system whereby customers can pay online.'),
      ], [
        EG('advanced-linkers', 'given that / hence / whereby / albeit', ('connecteurs logiques avancés', 'advanced linkers')),
        E('given-that', 'given that', ('étant donné que', 'given that')),
        E('hence', 'hence', ('d’où, par conséquent', 'hence')),
        E('whereby', 'whereby', ('par lequel, selon lequel', 'whereby')),
        E('albeit', 'albeit', ('bien que, quoique', 'albeit')),
        E('notwithstanding', 'notwithstanding', ('nonobstant, malgré', 'notwithstanding')),
        E('thereby', 'thereby', ('de ce fait, ainsi', 'thereby')),
      ], [
        x('Given that demand is falling, we should reduce production.', 'Étant donné que la demande baisse, nous devrions réduire la production.'),
        x('We introduced a scheme whereby employees can buy shares at a discount.', 'Nous avons mis en place un dispositif permettant aux salariés d’acheter des actions à prix réduit.'),
      ], [
        FB(CHOOSE, 'Costs have risen sharply; ＿ the need for new suppliers.', ['hence', 'whereby', 'albeit'], 'hence', ('D’où : hence (+ nom).', 'Therefore: hence (+ noun).'), ('Les coûts ont fortement augmenté ; d’où la nécessité de nouveaux fournisseurs.', 'Costs have risen sharply; hence the need for new suppliers.')),
        FB(CHOOSE, 'The results were positive, ＿ slightly below expectations.', ['albeit', 'hence', 'given'], 'albeit', ('Bien que : albeit (+ adjectif).', 'Although: albeit (+ adjective).'), ('Les résultats étaient positifs, quoique légèrement inférieurs aux attentes.', 'The results were positive, albeit slightly below expectations.')),
        FB(CHOOSE, '＿ that the deadline is tomorrow, we must work late.', ['Given', 'Hence', 'Albeit'], 'Given', ('Étant donné que : given that.', 'Since: given that.'), ('Étant donné que l’échéance est demain, nous devons travailler tard.', 'Given that the deadline is tomorrow, we must work late.')),
        FB(CHOOSE, 'This is a system ＿ clients can track their orders online.', ['whereby', 'whereas', 'hence'], 'whereby', ('Par lequel : whereby.', 'By which: whereby.'), ('C’est un système qui permet aux clients de suivre leurs commandes en ligne.', 'This is a system whereby clients can track their orders online.')),
      ]),
  ]),
  CH('c1-w3-c2', ('Le droit des affaires', 'Business law'), [
    L('en-contracts', ('Les contrats et le juridique', 'Contracts and legal matters'), ('Comprendre le vocabulaire des contrats et des litiges.', 'Understand the vocabulary of contracts and disputes.'), 9, [
        ('Contrat : a clause, terms and conditions, to be binding (contraignant), to breach a contract (rompre), to comply with (se conformer à), liability (responsabilité).', 'Contract: a clause, terms and conditions, to be binding, to breach a contract, to comply with, liability.'),
        ('Litiges : a dispute, to settle out of court (régler à l’amiable), to sue (poursuivre), compensation (indemnisation), a warranty (garantie).', 'Disputes: a dispute, to settle out of court, to sue, compensation, a warranty.'),
      ], [
        E('clause', 'clause', ('clause', 'clause')),
        E('binding', 'binding', ('contraignant, ayant force obligatoire', 'binding')),
        E('breach', 'breach', ('violation, rupture (de contrat)', 'breach')),
        E('comply', 'to comply with', ('se conformer à, respecter', 'to comply with')),
        E('liability', 'liability', ('responsabilité (juridique)', 'liability')),
        E('dispute', 'dispute', ('litige, différend', 'dispute')),
        E('settle', 'to settle', ('régler (un litige, une facture)', 'to settle')),
        E('warranty', 'warranty', ('garantie (produit)', 'warranty')),
      ], [
        x('Failure to comply with clause 7 will be considered a breach of contract.', 'Le non-respect de la clause 7 sera considéré comme une rupture de contrat.'),
        x('The two companies settled the dispute out of court.', 'Les deux entreprises ont réglé le litige à l’amiable.'),
      ], [
        FB(COMPLETE, 'All products must ＿ with EU safety standards.', ['comply', 'agree', 'respect'], 'comply', ('comply with = se conformer à.', 'comply with = follow (rules).'), ('Tous les produits doivent être conformes aux normes de sécurité de l’UE.', 'All products must comply with EU safety standards.')),
        FB(COMPLETE, 'The laptop is still under ＿, so the repair is free.', ['warranty', 'guarantor', 'insurance policy'], 'warranty', ('Garantie produit : warranty.', 'Product guarantee: warranty.'), ('L’ordinateur est encore sous garantie, donc la réparation est gratuite.', 'The laptop is still under warranty, so the repair is free.')),
        FB(COMPLETE, 'They decided to ＿ the case out of court.', ['settle', 'set', 'solve up'], 'settle', ('Régler à l’amiable : settle out of court.', 'settle out of court.'), ('Ils ont décidé de régler l’affaire à l’amiable.', 'They decided to settle the case out of court.')),
        TF('This agreement is legally binding.', ('Le contrat n’a aucune valeur juridique.', 'The agreement has no legal force.'), FAUX, ('binding = qui engage juridiquement.', 'binding = legally enforceable.')),
      ]),
  ])])

# ═════════════════════════ Île 4 : Le subjonctif ═════════════════════════
W4 = WORLD('c1-w4', ('La sorcière des brumes', 'The hag of the mists'), REGION,
  ('Exprimer l’exigence et la recommandation au registre formel : subjonctif, It’s time…, would rather.', 'Express demands and recommendations formally: the subjunctive, It’s time…, would rather.'),
  (('La Gwrach y Rhibyn', 'The Gwrach y Rhibyn'), 'r', ('Cette sorcière galloise aux ailes de cuir frappe aux fenêtres en appelant ceux qui vont partir. Elle exige qu’on lui parle dans la langue la plus soutenue.', 'This Welsh hag with leathery wings taps on windows, calling the names of those about to depart. She demands to be addressed in the most formal language.')),
  [CH('c1-w4-c1', ('Il est essentiel que…', 'It is essential that…'), [
    L('en-subjunctive', ('Le subjonctif : It is essential that he be…', 'The subjunctive: It is essential that he be…'), ('Utiliser la base verbale après les verbes et adjectifs d’exigence.', 'Use the base verb after verbs and adjectives of demand.'), 10, [
        ('Après recommend, suggest, insist, demand, require + that : base verbale sans -s : We recommend that he attend the training. They insisted that she be present.', 'After recommend, suggest, insist, demand, require + that: base verb without -s: We recommend that he attend the training. They insisted that she be present.'),
        ('Après essential, vital, important, imperative + that : It is essential that every employee complete the form.', 'After essential, vital, important, imperative + that: It is essential that every employee complete the form.'),
        ('Négation : not + base : The board requested that the results not be published.', 'Negative: not + base: The board requested that the results not be published.'),
      ], [
        EG('subjunctive', 'recommend that he attend / be', ('subjonctif (base verbale après that)', 'mandative subjunctive')),
        E('essential', 'essential', ('essentiel, indispensable', 'essential')),
        E('imperative', 'imperative', ('impératif, crucial', 'imperative')),
        E('demand', 'to demand', ('exiger', 'to demand')),
        E('compliance', 'compliance', ('conformité', 'compliance')),
      ], [
        x('It is essential that all visitors wear a safety helmet.', 'Il est indispensable que tous les visiteurs portent un casque.'),
        x('The auditors recommended that the company review its procedures.', 'Les auditeurs ont recommandé que l’entreprise revoie ses procédures.'),
      ], [
        FB(CHOOSE, 'We recommend that he ＿ the course.', ['attend', 'attends', 'attended'], 'attend', ('Subjonctif : base verbale, sans -s.', 'Subjunctive: base verb, no -s.'), ('Nous recommandons qu’il suive la formation.', 'We recommend that he attend the course.')),
        FB(CHOOSE, 'It is vital that the data ＿ kept confidential.', ['be', 'is', 'are'], 'be', ('Subjonctif de be : be.', 'Subjunctive of be: be.'), ('Il est vital que les données restent confidentielles.', 'It is vital that the data be kept confidential.')),
        FB(CHOOSE, 'The client insisted that the meeting ＿ postponed.', ['not be', 'won’t be', 'isn’t'], 'not be', ('Négation : not + base.', 'Negative: not + base.'), ('Le client a exigé que la réunion ne soit pas reportée.', 'The client insisted that the meeting not be postponed.')),
        TF('The board demanded that she resign.', ('Le conseil a exigé sa démission.', 'The board required her to step down.'), VRAI, ('demand that she resign = exiger qu’elle démissionne.', 'demand that she resign.')),
      ]),
    L('en-would-rather', ('It’s time, would rather, as if', 'It’s time, would rather, as if'), ('Exprimer préférence et irréel avec le prétérit modal.', 'Express preference and unreality with the past tense.'), 10, [
        ('It’s (high) time + sujet + prétérit = il est grand temps que : It’s high time we updated our website.', 'It’s (high) time + subject + past simple: It’s high time we updated our website.'),
        ('would rather + base (soi-même) : I’d rather stay. would rather + sujet + prétérit (autrui) : I’d rather you didn’t smoke here.', 'would rather + base (yourself): I’d rather stay. would rather + subject + past (someone else): I’d rather you didn’t smoke here.'),
        ('as if / as though + prétérit pour l’irréel : He talks as if he were the boss.', 'as if / as though + past for unreality: He talks as if he were the boss.'),
      ], [
        EG('its-time', 'It’s high time we…', ('il est grand temps que', 'It’s high time + past')),
        EG('would-rather', 'I’d rather you didn’t…', ('je préférerais que tu ne… pas', 'would rather + past')),
        E('as-if', 'as if', ('comme si', 'as if')),
        E('outdated', 'outdated', ('dépassé, obsolète', 'outdated')),
      ], [
        x('It’s high time we replaced these outdated computers.', 'Il est grand temps que nous remplacions ces ordinateurs obsolètes.'),
        x('I’d rather you sent the report by email.', 'Je préférerais que tu envoies le rapport par e-mail.'),
      ], [
        FB(CHOOSE, 'It’s high time we ＿ a decision.', ['made', 'make', 'will make'], 'made', ('It’s high time + prétérit.', 'It’s high time + past.'), ('Il est grand temps que nous prenions une décision.', 'It’s high time we made a decision.')),
        FB(CHOOSE, 'I’d rather you ＿ tell anyone about this.', ['didn’t', 'don’t', 'won’t'], 'didn’t', ('would rather + sujet + prétérit.', 'would rather + subject + past.'), ('Je préférerais que tu n’en parles à personne.', 'I’d rather you didn’t tell anyone about this.')),
        FB(CHOOSE, 'He behaves as if he ＿ the owner.', ['were', 'is', 'be'], 'were', ('Irréel : as if + were.', 'Unreal: as if + were.'), ('Il se comporte comme s’il était le propriétaire.', 'He behaves as if he were the owner.')),
        FB(CHOOSE, 'I’d rather ＿ at home tonight.', ['stay', 'stayed', 'to stay'], 'stay', ('Pour soi-même : would rather + base.', 'For yourself: would rather + base.'), ('Je préférerais rester à la maison ce soir.', 'I’d rather stay at home tonight.')),
      ]),
  ]),
  CH('c1-w4-c2', ('Le registre', 'Register'), [
    L('en-formal-register', ('Formel ou familier ?', 'Formal or informal?'), ('Adapter son vocabulaire au registre attendu.', 'Adapt your vocabulary to the expected register.'), 9, [
        ('Familier → formel : get → obtain / receive, ask for → request, need → require, help → assist, start → commence, end → terminate, enough → sufficient.', 'Informal → formal: get → obtain / receive, ask for → request, need → require, help → assist, start → commence, end → terminate, enough → sufficient.'),
        ('À l’écrit formel : pas de contractions, voix passive plus fréquente, verbes simples plutôt qu’à particule.', 'In formal writing: no contractions, more passives, single verbs rather than phrasal verbs.'),
      ], [
        E('obtain', 'to obtain', ('obtenir', 'to obtain')),
        E('assist', 'to assist', ('aider, assister', 'to assist')),
        E('commence', 'to commence', ('commencer (formel)', 'to commence')),
        E('terminate', 'to terminate', ('mettre fin à, résilier', 'to terminate')),
        E('sufficient', 'sufficient', ('suffisant', 'sufficient')),
        E('inquire', 'to inquire', ('se renseigner, demander', 'to inquire')),
      ], [
        x('Construction will commence in April, subject to planning permission.', 'Les travaux commenceront en avril, sous réserve du permis de construire.'),
        x('We regret to inform you that your contract will be terminated.', 'Nous avons le regret de vous informer que votre contrat sera résilié.'),
      ], [
        FB(CHOOSE, 'Formal: Our staff will be glad to ＿ you.', ['assist', 'help out', 'give a hand'], 'assist', ('Formel : assist.', 'Formal: assist.'), ('Notre personnel se fera un plaisir de vous aider.', 'Our staff will be glad to assist you.')),
        FB(CHOOSE, 'Formal: The funds are not ＿ to cover the costs.', ['sufficient', 'enough of', 'plenty'], 'sufficient', ('Formel : sufficient.', 'Formal: sufficient.'), ('Les fonds ne suffisent pas à couvrir les coûts.', 'The funds are not sufficient to cover the costs.')),
        FB(CHOOSE, 'Formal: I am writing to ＿ about the vacancy.', ['inquire', 'ask around', 'find out stuff'], 'inquire', ('Formel : inquire.', 'Formal: inquire.'), ('Je vous écris pour me renseigner sur le poste vacant.', 'I am writing to inquire about the vacancy.')),
        TF('The agreement was terminated in June.', ('L’accord a pris fin en juin.', 'The agreement ended in June.'), VRAI, ('terminated = résilié.', 'terminated = ended.')),
      ]),
  ])])

# ═════════════════════════ Île 5 : Écrire comme un expert ═════════════════════════
W5 = WORLD('c1-w5', ('La reine de l’hiver', 'The winter queen'), REGION,
  ('Écrire avec densité : nominalisation, groupes nominaux complexes, adjectifs composés.', 'Write densely: nominalisation, complex noun phrases, compound adjectives.'),
  (('La Cailleach, reine de l’hiver', 'The Cailleach, queen of winter'), 'c', ('La vieille déesse de l’hiver façonne les montagnes d’Écosse avec son marteau. Elle exige des phrases aussi denses et solides que la pierre.', 'The old goddess of winter shapes the mountains of Scotland with her hammer. She demands sentences as dense and solid as stone.')),
  [CH('c1-w5-c1', ('La nominalisation', 'Nominalisation'), [
    L('en-nominalisation', ('Transformer des verbes en noms', 'Turning verbs into nouns'), ('Rendre un écrit plus formel et plus dense.', 'Make writing more formal and dense.'), 10, [
        ('Verbe → nom : decide → decision, analyse → analysis, fail → failure, reduce → reduction, introduce → introduction.', 'Verb → noun: decide → decision, analyse → analysis, fail → failure, reduce → reduction, introduce → introduction.'),
        ('Prices rose sharply, which worried investors. → The sharp rise in prices worried investors.', 'Prices rose sharply, which worried investors. → The sharp rise in prices worried investors.'),
        ('Suffixes fréquents : -tion, -ment, -ance / -ence, -ity, -al (approval, refusal), -ure (failure).', 'Common suffixes: -tion, -ment, -ance / -ence, -ity, -al (approval, refusal), -ure (failure).'),
      ], [
        EG('nominalisation', 'the sharp rise in prices', ('nominalisation (verbe → nom)', 'nominalisation')),
        E('approval', 'approval', ('approbation, accord', 'approval')),
        E('failure', 'failure', ('échec, défaillance', 'failure')),
        E('reduction', 'reduction', ('réduction, baisse', 'reduction')),
        E('implementation', 'implementation', ('mise en œuvre', 'implementation')),
        E('analysis', 'analysis', ('analyse', 'analysis')),
      ], [
        x('The implementation of the new system has led to a significant reduction in errors.', 'La mise en œuvre du nouveau système a entraîné une baisse significative des erreurs.'),
        x('The failure of the negotiations came as a surprise.', 'L’échec des négociations a surpris tout le monde.'),
      ], [
        FB(CHOOSE, 'The project requires the board’s ＿.', ['approval', 'approve', 'approving'], 'approval', ('Nom : approval.', 'Noun: approval.'), ('Le projet nécessite l’approbation du conseil.', 'The project requires the board’s approval.')),
        FB(CHOOSE, 'The ＿ of the plan will take two years.', ['implementation', 'implement', 'implemented'], 'implementation', ('Nom : implementation.', 'Noun: implementation.'), ('La mise en œuvre du plan prendra deux ans.', 'The implementation of the plan will take two years.')),
        FB(CHOOSE, 'There has been a sharp ＿ in demand.', ['increase', 'increasing', 'increased'], 'increase', ('a + adjectif + nom : an increase.', 'a + adjective + noun: an increase.'), ('Il y a eu une forte hausse de la demande.', 'There has been a sharp increase in demand.')),
        FB(CHOOSE, 'A detailed ＿ of the data is needed.', ['analysis', 'analysed', 'analytic'], 'analysis', ('Nom : analysis.', 'Noun: analysis.'), ('Une analyse détaillée des données est nécessaire.', 'A detailed analysis of the data is needed.')),
      ]),
    L('en-compound-adjectives', ('Les adjectifs composés', 'Compound adjectives'), ('Condenser une information : a two-day course, a well-known brand.', 'Condense information: a two-day course, a well-known brand.'), 9, [
        ('Nombre + nom au singulier : a two-day conference, a five-star hotel, a ten-minute walk (jamais « days »).', 'Number + singular noun: a two-day conference, a five-star hotel, a ten-minute walk (never “days”).'),
        ('Adverbe + participe : well-known, highly-qualified, long-standing (de longue date), fast-growing ; nom + participe : time-consuming, award-winning.', 'Adverb + participle: well-known, highly-qualified, long-standing, fast-growing; noun + participle: time-consuming, award-winning.'),
      ], [
        EG('compound-adjectives', 'a two-day course / a well-known brand', ('adjectifs composés', 'compound adjectives')),
        E('time-consuming', 'time-consuming', ('chronophage, qui prend du temps', 'time-consuming')),
        E('long-standing', 'long-standing', ('de longue date', 'long-standing')),
        E('award-winning', 'award-winning', ('primé', 'award-winning')),
        E('fast-growing', 'fast-growing', ('en pleine croissance', 'fast-growing')),
        E('highly-qualified', 'highly qualified', ('hautement qualifié', 'highly qualified')),
      ], [
        x('We are a fast-growing company looking for highly qualified engineers.', 'Nous sommes une entreprise en pleine croissance qui recherche des ingénieurs hautement qualifiés.'),
        x('The hotel is a ten-minute walk from the station.', 'L’hôtel est à dix minutes à pied de la gare.'),
      ], [
        FB(CHOOSE, 'She attended a ＿ training course.', ['three-day', 'three-days', 'three days'], 'three-day', ('Nombre + nom au singulier avec trait d’union.', 'Number + singular noun with a hyphen.'), ('Elle a suivi une formation de trois jours.', 'She attended a three-day training course.')),
        FB(CHOOSE, 'Checking every invoice by hand is very ＿.', ['time-consuming', 'time-consumed', 'consuming-time'], 'time-consuming', ('Qui prend du temps : time-consuming.', 'Takes a lot of time: time-consuming.'), ('Vérifier chaque facture à la main prend beaucoup de temps.', 'Checking every invoice by hand is very time-consuming.')),
        FB(CHOOSE, 'We have a ＿ relationship with this supplier.', ['long-standing', 'long-stood', 'standing-long'], 'long-standing', ('De longue date : long-standing.', 'Existing for a long time: long-standing.'), ('Nous entretenons une relation de longue date avec ce fournisseur.', 'We have a long-standing relationship with this supplier.')),
        TF('It is an award-winning restaurant.', ('Le restaurant a reçu des prix.', 'The restaurant has won prizes.'), VRAI, ('award-winning = primé.', 'award-winning = has won awards.')),
      ]),
  ]),
  CH('c1-w5-c2', ('Le développement durable', 'Sustainability'), [
    L('en-sustainability', ('Environnement et responsabilité', 'Environment and responsibility'), ('Parler des enjeux environnementaux et sociaux de l’entreprise.', 'Discuss companies’ environmental and social issues.'), 9, [
        ('Vocabulaire : sustainable (durable), renewable energy, carbon footprint (empreinte carbone), emissions, waste (déchets), to recycle, to offset (compenser).', 'Vocabulary: sustainable, renewable energy, carbon footprint, emissions, waste, to recycle, to offset.'),
        ('Responsabilité : corporate social responsibility (RSE), ethical sourcing (approvisionnement éthique), supply chain (chaîne d’approvisionnement), transparency.', 'Responsibility: corporate social responsibility (CSR), ethical sourcing, supply chain, transparency.'),
      ], [
        E('sustainable', 'sustainable', ('durable (écologique)', 'sustainable')),
        E('renewable', 'renewable', ('renouvelable', 'renewable')),
        E('carbon-footprint', 'carbon footprint', ('empreinte carbone', 'carbon footprint')),
        E('waste', 'waste', ('déchets, gaspillage', 'waste')),
        E('supply-chain', 'supply chain', ('chaîne d’approvisionnement', 'supply chain')),
        E('offset', 'to offset', ('compenser', 'to offset')),
        E('transparency', 'transparency', ('transparence', 'transparency')),
      ], [
        x('By 2030, all our factories will run on renewable energy.', 'D’ici 2030, toutes nos usines fonctionneront aux énergies renouvelables.'),
        x('We are working with suppliers to reduce waste across the supply chain.', 'Nous travaillons avec nos fournisseurs pour réduire les déchets tout au long de la chaîne d’approvisionnement.'),
      ], [
        FB(COMPLETE, 'Wind and solar power are ＿ sources of energy.', ['renewable', 'renewing', 'renewed'], 'renewable', ('Renouvelable : renewable.', 'Can be replaced naturally: renewable.'), ('L’éolien et le solaire sont des sources d’énergie renouvelables.', 'Wind and solar power are renewable sources of energy.')),
        FB(COMPLETE, 'Flying less is the best way to reduce your carbon ＿.', ['footprint', 'footstep', 'fingerprint'], 'footprint', ('Empreinte carbone : carbon footprint.', 'carbon footprint.'), ('Prendre moins l’avion est le meilleur moyen de réduire ton empreinte carbone.', 'Flying less is the best way to reduce your carbon footprint.')),
        FB(COMPLETE, 'The airline plants trees to ＿ its emissions.', ['offset', 'set off', 'outset'], 'offset', ('Compenser : offset.', 'Balance out: offset.'), ('La compagnie plante des arbres pour compenser ses émissions.', 'The airline plants trees to offset its emissions.')),
        TF('The company is committed to transparency.', ('L’entreprise cache ses informations.', 'The company hides information.'), FAUX, ('transparency = transparence.', 'transparency = openness.')),
      ]),
  ])])

# ═════════════════════════ Île 6 : Nuancer ═════════════════════════
W6 = WORLD('c1-w6', ('Le serpent de Falmouth', 'The Falmouth serpent'), REGION,
  ('Nuancer et spéculer avec prudence : hedging, seem / appear to, be likely to, there is bound to be.', 'Hedge and speculate cautiously: seem / appear to, be likely to, there is bound to be.'),
  (('Morgawr, serpent de Falmouth', 'Morgawr, the Falmouth serpent'), 's', ('Ce serpent de mer géant de Cornouailles n’apparaît qu’à ceux qui n’affirment rien sans preuve. Nuance chacune de tes affirmations pour l’apercevoir.', 'This giant Cornish sea serpent only appears to those who claim nothing without proof. Qualify every statement to catch sight of it.')),
  [CH('c1-w6-c1', ('Il semblerait que…', 'It would appear that…'), [
    L('en-hedging', ('Le hedging : atténuer une affirmation', 'Hedging: softening claims'), ('Présenter une information avec la prudence attendue dans un rapport.', 'Present information with the caution expected in a report.'), 10, [
        ('seem / appear + to (+ have done) : Sales appear to have stabilised. It would seem that… / It would appear that…', 'seem / appear + to (+ have done): Sales appear to have stabilised. It would seem that… / It would appear that…'),
        ('Modaux et adverbes : may, might, could ; arguably (on peut soutenir que), presumably (vraisemblablement), to some extent (dans une certaine mesure), tend to.', 'Modals and adverbs: may, might, could; arguably, presumably, to some extent, tend to.'),
      ], [
        EG('hedging', 'It would appear that… / seem to have…', ('atténuation (hedging)', 'hedging')),
        E('appear-to', 'to appear to', ('sembler, paraître', 'to appear to')),
        E('arguably', 'arguably', ('sans doute, on peut soutenir que', 'arguably')),
        E('presumably', 'presumably', ('vraisemblablement, sans doute', 'presumably')),
        E('to-some-extent', 'to some extent', ('dans une certaine mesure', 'to some extent')),
        E('tend-to', 'to tend to', ('avoir tendance à', 'to tend to')),
      ], [
        x('It would appear that the new campaign has had little effect on sales.', 'Il semblerait que la nouvelle campagne ait eu peu d’effet sur les ventes.'),
        x('This is arguably the most important decision in the company’s history.', 'C’est sans doute la décision la plus importante de l’histoire de l’entreprise.'),
      ], [
        FB(CHOOSE, 'The problem ＿ to have been caused by a software error.', ['appears', 'appear', 'is appearing'], 'appears', ('Sujet singulier : appears to.', 'Singular subject: appears to.'), ('Le problème semble avoir été causé par une erreur logicielle.', 'The problem appears to have been caused by a software error.')),
        FB(CHOOSE, 'Customers ＿ to prefer shopping online.', ['tend', 'tendency', 'tending'], 'tend', ('Avoir tendance à : tend to.', 'Usually do: tend to.'), ('Les clients ont tendance à préférer acheter en ligne.', 'Customers tend to prefer shopping online.')),
        FB(CHOOSE, 'It would ＿ that the figures are incorrect.', ['seem', 'look', 'show'], 'seem', ('It would seem that…', 'It would seem that…'), ('Il semblerait que les chiffres soient erronés.', 'It would seem that the figures are incorrect.')),
        TF('To some extent, the plan was successful.', ('Le plan a été un succès total.', 'The plan was a complete success.'), FAUX, ('to some extent = en partie seulement.', 'to some extent = partly.')),
      ]),
    L('en-probability', ('La probabilité : be likely to, be bound to', 'Probability: be likely to, be bound to'), ('Graduer la probabilité d’un événement futur.', 'Grade the likelihood of a future event.'), 10, [
        ('be bound to / be certain to = c’est sûr : Prices are bound to rise. be likely to / unlikely to = probable / peu probable : The deal is unlikely to go ahead.', 'be bound to / be certain to = certain: Prices are bound to rise. be likely to / unlikely to: The deal is unlikely to go ahead.'),
        ('There is a good chance that… / There is little chance of… / In all likelihood (selon toute vraisemblance)…', 'There is a good chance that… / There is little chance of… / In all likelihood…'),
      ], [
        EG('likely-bound', 'be likely to / be bound to', ('être probable / être certain', 'be likely to / be bound to')),
        E('likely', 'likely', ('probable', 'likely')),
        E('bound-to', 'bound to', ('forcément, à coup sûr', 'bound to')),
        E('likelihood', 'likelihood', ('probabilité', 'likelihood')),
        E('go-ahead', 'to go ahead', ('avoir lieu, se poursuivre', 'to go ahead')),
      ], [
        x('Interest rates are likely to remain high for some time.', 'Les taux d’intérêt devraient rester élevés pendant un certain temps.'),
        x('With so many changes, there are bound to be a few problems.', 'Avec autant de changements, il y aura forcément quelques problèmes.'),
      ], [
        FB(CHOOSE, 'Given the storm, the flight is ＿ to be delayed.', ['likely', 'probably', 'likelihood'], 'likely', ('be likely to.', 'be likely to.'), ('Vu la tempête, le vol risque d’être retardé.', 'Given the storm, the flight is likely to be delayed.')),
        FB(CHOOSE, 'He’s been working so hard — he’s ＿ to succeed.', ['bound', 'binding', 'bond'], 'bound', ('Certain : be bound to.', 'Certain: be bound to.'), ('Il travaille tellement — il va forcément réussir.', 'He’s been working so hard — he’s bound to succeed.')),
        FB(CHOOSE, 'There is little ＿ of the merger going ahead.', ['chance', 'luck', 'likely'], 'chance', ('little chance of + -ing.', 'little chance of + -ing.'), ('Il y a peu de chances que la fusion aboutisse.', 'There is little chance of the merger going ahead.')),
        TF('The project is unlikely to be finished on time.', ('Le projet sera probablement en retard.', 'The project will probably be late.'), VRAI, ('unlikely = peu probable.', 'unlikely = not probable.')),
      ]),
  ]),
  CH('c1-w6-c2', ('La gestion de crise', 'Crisis management'), [
    L('en-crisis', ('Communiquer en temps de crise', 'Communicating in a crisis'), ('Annoncer une mauvaise nouvelle et rassurer.', 'Announce bad news and reassure.'), 9, [
        ('Annoncer : We regret to announce that… / Due to unforeseen circumstances (circonstances imprévues)… / A product recall (rappel) has been issued.', 'Announcing: We regret to announce that… / Due to unforeseen circumstances… / A product recall has been issued.'),
        ('Rassurer : We are taking every possible measure to… / We will keep you informed. / Rest assured that (soyez assurés que)…', 'Reassuring: We are taking every possible measure to… / We will keep you informed. / Rest assured that…'),
      ], [
        E('unforeseen', 'unforeseen', ('imprévu', 'unforeseen')),
        E('recall', 'recall', ('rappel (de produit)', 'recall')),
        E('measure', 'measure', ('mesure, disposition', 'measure')),
        E('rest-assured', 'rest assured', ('soyez assurés', 'rest assured')),
        E('reputation', 'reputation', ('réputation', 'reputation')),
        E('spokesperson', 'spokesperson', ('porte-parole', 'spokesperson')),
      ], [
        x('Due to unforeseen circumstances, tonight’s performance has been cancelled.', 'En raison de circonstances imprévues, la représentation de ce soir est annulée.'),
        x('Rest assured that we are taking every possible measure to protect your data.', 'Soyez assurés que nous prenons toutes les mesures possibles pour protéger vos données.'),
      ], [
        FB(COMPLETE, 'The company has issued a ＿ of all affected models.', ['recall', 'return back', 'remind'], 'recall', ('Rappel de produit : recall.', 'Product recall.'), ('L’entreprise a lancé un rappel de tous les modèles concernés.', 'The company has issued a recall of all affected models.')),
        FB(COMPLETE, 'Rest ＿ that your money will be refunded.', ['assured', 'assuring', 'sure'], 'assured', ('Rest assured = soyez assurés.', 'Rest assured.'), ('Soyez assurés que vous serez remboursés.', 'Rest assured that your money will be refunded.')),
        DC(ANSWER, [('Journalist', 'Is it true that customer data was stolen?')], ('Tu es porte-parole ; l’enquête est en cours.', 'You are the spokesperson; the investigation is ongoing.'), ['We are investigating and will keep you informed as soon as we know more.', 'Leave me alone, please.', 'Yes, everything was stolen, it’s a disaster.'], 'We are investigating and will keep you informed as soon as we know more.', ('Prudence et transparence.', 'Caution and transparency.')),
        TF('The event was cancelled due to unforeseen circumstances.', ('L’annulation était prévue depuis longtemps.', 'The cancellation had been planned for a long time.'), FAUX, ('unforeseen = imprévu.', 'unforeseen = unexpected.')),
      ]),
  ])])

# ═════════════════════════ Île 7 : Le moulin du Hob ═════════════════════════
W7 = WORLD('c1-w7', ('Le moulin du Hob', 'The Hob’s mill'), REGION,
  ('Insister et structurer un discours : inversion après only, so, such ; fronting ; mots de discours.', 'Emphasise and structure speech: inversion after only, so, such; fronting; discourse markers.'),
  (('Le Hob du moulin', 'The mill Hob'), 'e', ('Cet esprit domestique travaille la nuit en échange d’une jatte de crème, mais quitte la maison au moindre mot mal placé. Structure ton discours avec soin pour qu’il reste.', 'This household spirit works at night in exchange for a bowl of cream, but leaves the house at the slightest misplaced word. Structure your speech carefully so that he stays.')),
  [CH('c1-w7-c1', ('Mettre en relief', 'Highlighting'), [
    L('en-inversion-c1', ('Inversions avancées : Only when…, So… that', 'Advanced inversion: Only when…, So… that'), ('Mettre une idée en tête de phrase pour insister.', 'Put an idea first for emphasis.'), 10, [
        ('Only + complément + inversion : Only when the results came in did we realise the scale of the problem. Only then…, Only by…, Only after…', 'Only + phrase + inversion: Only when the results came in did we realise the scale of the problem. Only then…, Only by…, Only after…'),
        ('So + adjectif + inversion + that : So successful was the launch that we sold out in a day. Such + be + nom : Such was the demand that…', 'So + adjective + inversion + that: So successful was the launch that we sold out in a day. Such + be + noun: Such was the demand that…'),
        ('Hardly / No sooner : Hardly had we arrived when it started raining. No sooner had he left than the phone rang.', 'Hardly / No sooner: Hardly had we arrived when it started raining. No sooner had he left than the phone rang.'),
      ], [
        EG('only-when', 'Only when… did…', ('ce n’est que lorsque… que…', 'Only when… + inversion')),
        EG('so-such-inversion', 'So successful was… that / Such was…', ('si… que (inversion)', 'So / Such + inversion')),
        EG('no-sooner', 'No sooner had… than / Hardly had… when', ('à peine… que', 'No sooner… than')),
        E('scale', 'scale', ('ampleur, échelle', 'scale')),
        E('sell-out', 'to sell out', ('être épuisé (stock)', 'to sell out')),
      ], [
        x('Only after the audit did we discover the error.', 'Ce n’est qu’après l’audit que nous avons découvert l’erreur.'),
        x('No sooner had the product been launched than orders started pouring in.', 'À peine le produit était-il lancé que les commandes ont afflué.'),
      ], [
        FB(CHOOSE, 'Only when I read the report ＿ how serious it was.', ['did I understand', 'I understood', 'I did understand'], 'did I understand', ('Only when… + inversion.', 'Only when… + inversion.'), ('Ce n’est qu’en lisant le rapport que j’ai compris la gravité de la situation.', 'Only when I read the report did I understand how serious it was.')),
        FB(CHOOSE, 'No sooner had she sat down ＿ the fire alarm went off.', ['than', 'when', 'then'], 'than', ('No sooner… than.', 'No sooner… than.'), ('À peine s’était-elle assise que l’alarme incendie s’est déclenchée.', 'No sooner had she sat down than the fire alarm went off.')),
        FB(CHOOSE, 'So popular ＿ the product that it sold out in hours.', ['was', 'it was', 'has'], 'was', ('So + adjectif + verbe + sujet.', 'So + adjective + verb + subject.'), ('Le produit était si populaire qu’il a été épuisé en quelques heures.', 'So popular was the product that it sold out in hours.')),
        FB(CHOOSE, 'Hardly ＿ the meeting started when the power went out.', ['had', 'has', 'did'], 'had', ('Hardly had… when.', 'Hardly had… when.'), ('La réunion avait à peine commencé que le courant a été coupé.', 'Hardly had the meeting started when the power went out.')),
      ]),
    L('en-discourse-markers', ('Les marqueurs du discours', 'Discourse markers'), ('Guider l’auditeur à l’oral comme à l’écrit.', 'Guide the listener in speech and writing.'), 9, [
        ('Recentrer : As far as… is concerned (en ce qui concerne), With regard to, Regarding. Préciser : In other words, That is to say, To put it another way.', 'Focusing: As far as… is concerned, With regard to, Regarding. Clarifying: In other words, That is to say, To put it another way.'),
        ('Revenir et digresser : Incidentally (au fait), Be that as it may (quoi qu’il en soit), Anyway, Having said that (cela dit).', 'Digressing and returning: Incidentally, Be that as it may, Anyway, Having said that.'),
      ], [
        E('as-far-as', 'as far as… is concerned', ('en ce qui concerne…', 'as far as… is concerned')),
        E('with-regard-to', 'with regard to', ('en ce qui concerne, quant à', 'with regard to')),
        E('in-other-words', 'in other words', ('autrement dit', 'in other words')),
        E('incidentally', 'incidentally', ('au fait, soit dit en passant', 'incidentally')),
        E('having-said-that', 'having said that', ('cela dit, ceci étant dit', 'having said that')),
        E('be-that-as-it-may', 'be that as it may', ('quoi qu’il en soit', 'be that as it may')),
      ], [
        x('As far as the budget is concerned, we are on track. Having said that, the schedule is tight.', 'En ce qui concerne le budget, nous sommes dans les clous. Cela dit, le calendrier est serré.'),
        x('Sales fell by 20%. In other words, we need to act quickly.', 'Les ventes ont chuté de 20 %. Autrement dit, nous devons agir vite.'),
      ], [
        FB(COMPLETE, 'As far as I’m ＿, the plan is excellent.', ['concerned', 'concerning', 'concern'], 'concerned', ('As far as I’m concerned = pour ma part.', 'As far as I’m concerned = in my view.'), ('Pour ma part, le plan est excellent.', 'As far as I’m concerned, the plan is excellent.')),
        FB(COMPLETE, 'The hotel is expensive. Having ＿ that, it’s very comfortable.', ['said', 'told', 'spoken'], 'said', ('Cela dit : Having said that.', 'However: Having said that.'), ('L’hôtel est cher. Cela dit, il est très confortable.', 'The hotel is expensive. Having said that, it’s very comfortable.')),
        FB(COMPLETE, 'We’re over budget. In other ＿, we can’t hire anyone.', ['words', 'sentences', 'ways'], 'words', ('Autrement dit : in other words.', 'To rephrase: in other words.'), ('Nous dépassons le budget. Autrement dit, nous ne pouvons embaucher personne.', 'We’re over budget. In other words, we can’t hire anyone.')),
        TF('Incidentally, did you get my email?', ('La question est le sujet principal de la conversation.', 'The question is the main topic of the conversation.'), FAUX, ('incidentally = au passage.', 'incidentally = by the way.')),
      ]),
  ]),
  CH('c1-w7-c2', ('Diriger', 'Leading'), [
    L('en-leadership', ('Le management et le leadership', 'Management and leadership'), ('Parler de motivation, de délégation et de changement.', 'Talk about motivation, delegation and change.'), 9, [
        ('to delegate (déléguer), to empower (responsabiliser), to motivate, to give feedback, accountability (responsabilité), morale (moral des équipes), to boost (stimuler).', 'to delegate, to empower, to motivate, to give feedback, accountability, morale, to boost.'),
        ('Le changement : to implement change, to overcome resistance (surmonter les résistances), a smooth transition (une transition en douceur), to streamline (rationaliser).', 'Change: to implement change, to overcome resistance, a smooth transition, to streamline.'),
      ], [
        E('delegate', 'to delegate', ('déléguer', 'to delegate')),
        E('empower', 'to empower', ('responsabiliser, donner du pouvoir', 'to empower')),
        E('morale', 'morale', ('moral (d’une équipe)', 'morale')),
        E('accountability', 'accountability', ('responsabilité (devoir de rendre des comptes)', 'accountability')),
        E('streamline', 'to streamline', ('rationaliser, simplifier', 'to streamline')),
        E('overcome', 'to overcome', ('surmonter', 'to overcome')),
      ], [
        x('A good manager delegates tasks and empowers the team.', 'Un bon manager délègue et responsabilise son équipe.'),
        x('The new software has streamlined our ordering process.', 'Le nouveau logiciel a simplifié notre processus de commande.'),
      ], [
        FB(COMPLETE, 'Staff ＿ is low after the job cuts.', ['morale', 'moral', 'morality'], 'morale', ('Moral d’une équipe : morale.', 'Team spirit: morale.'), ('Le moral du personnel est au plus bas après les suppressions de postes.', 'Staff morale is low after the job cuts.')),
        FB(COMPLETE, 'You can’t do everything yourself; learn to ＿.', ['delegate', 'delete', 'delay'], 'delegate', ('Déléguer : delegate.', 'Give tasks to others: delegate.'), ('Tu ne peux pas tout faire toi-même ; apprends à déléguer.', 'You can’t do everything yourself; learn to delegate.')),
        FB(COMPLETE, 'We need to ＿ our procedures to save time.', ['streamline', 'downstream', 'outline'], 'streamline', ('Simplifier : streamline.', 'Make more efficient: streamline.'), ('Nous devons rationaliser nos procédures pour gagner du temps.', 'We need to streamline our procedures to save time.')),
        TF('The team overcame many obstacles.', ('L’équipe a été arrêtée par les obstacles.', 'The team was stopped by the obstacles.'), FAUX, ('overcome = surmonter.', 'overcome = get past.')),
      ]),
  ])])

# ═════════════════════════ Île 8 : La Dame du Lac ═════════════════════════
W8 = WORLD('c1-w8', ('Le lac d’Excalibur', 'The lake of Excalibur'), REGION,
  ('Convaincre au plus haut niveau : rhétorique, concessions habiles et nuances de sens entre mots proches.', 'Persuade at the highest level: rhetoric, skilful concessions and fine distinctions between similar words.'),
  (('La Dame du Lac', 'The Lady of the Lake'), 'a', ('Gardienne d’Excalibur, la Dame du Lac ne reprendra l’épée que des mains de celui ou celle qui saura plaider sa cause avec une éloquence parfaite.', 'Keeper of Excalibur, the Lady of the Lake will only take back the sword from one who can plead their case with perfect eloquence.')),
  [CH('c1-w8-c1', ('L’art de convaincre', 'The art of persuasion'), [
    L('en-persuasion', ('Argumenter et concéder', 'Arguing and conceding'), ('Construire un argumentaire en anticipant les objections.', 'Build an argument while anticipating objections.'), 10, [
        ('Concéder pour mieux contrer : Admittedly, … ; however… / While it is true that…, … / Granted, …, but… / There is no denying that…, yet…', 'Concede to counter: Admittedly, …; however… / While it is true that…, … / Granted, …, but… / There is no denying that…, yet…'),
        ('Renforcer : What is more, … / Not to mention… / Above all, … / The bottom line is (l’essentiel, c’est)…', 'Reinforcing: What is more, … / Not to mention… / Above all, … / The bottom line is…'),
      ], [
        EG('concession', 'Admittedly…, however… / While it is true that…', ('concession argumentative', 'concession (argument)')),
        E('admittedly', 'admittedly', ('certes, il faut l’admettre', 'admittedly')),
        E('granted', 'granted', ('certes, d’accord', 'granted')),
        E('what-is-more', 'what is more', ('qui plus est, de plus', 'what is more')),
        E('bottom-line', 'the bottom line', ('l’essentiel, le fond du problème', 'the bottom line')),
        E('no-denying', 'there is no denying that', ('on ne peut nier que', 'there is no denying that')),
      ], [
        x('Admittedly, the initial cost is high; however, the savings will be considerable.', 'Certes, le coût initial est élevé ; cependant, les économies seront considérables.'),
        x('The bottom line is that we cannot afford to lose this client.', 'L’essentiel, c’est que nous ne pouvons pas nous permettre de perdre ce client.'),
      ], [
        FB(CHOOSE, '＿, the plan has risks, but the rewards are greater.', ['Admittedly', 'Consequently', 'Therefore'], 'Admittedly', ('Concession : Admittedly.', 'Concession: Admittedly.'), ('Certes, le plan comporte des risques, mais les gains sont plus importants.', 'Admittedly, the plan has risks, but the rewards are greater.')),
        FB(CHOOSE, 'While it is ＿ that prices are high, quality is excellent.', ['true', 'truth', 'truly'], 'true', ('While it is true that…', 'While it is true that…'), ('S’il est vrai que les prix sont élevés, la qualité est excellente.', 'While it is true that prices are high, quality is excellent.')),
        FB(CHOOSE, 'The product is cheap. What is ＿, it is eco-friendly.', ['more', 'better', 'plus'], 'more', ('Qui plus est : What is more.', 'In addition: What is more.'), ('Le produit est bon marché. Qui plus est, il est écologique.', 'The product is cheap. What is more, it is eco-friendly.')),
        DC(ANSWER, [('Lady of the Lake', 'Why should I take back the sword from you?')], ('Plaide ta cause avec éloquence.', 'Plead your case eloquently.'), ['Admittedly, I am not a king; yet there is no denying that I have kept my word.', 'Because I say so.', 'Take it, I don’t want it.'], 'Admittedly, I am not a king; yet there is no denying that I have kept my word.', ('Concession puis argument fort.', 'Concession, then a strong argument.')),
      ]),
    L('en-confusables', ('Les faux amis et mots proches', 'False friends and confusable words'), ('Éviter les pièges classiques du TOEIC.', 'Avoid classic TOEIC traps.'), 10, [
        ('Faux amis : actually (en fait), eventually (finalement), sensible (raisonnable), library (bibliothèque), achieve (accomplir), currently (actuellement), to attend (assister à).', 'False friends: actually, eventually, sensible, library, achieve, currently, to attend.'),
        ('Paires piégeuses : affect (verbe) / effect (nom) ; economic (de l’économie) / economical (économe) ; principal (principal) / principle (principe) ; lose / loose ; rise (intransitif) / raise (transitif).', 'Tricky pairs: affect (verb) / effect (noun); economic / economical; principal / principle; lose / loose; rise (intransitive) / raise (transitive).'),
      ], [
        EG('affect-effect', 'affect / effect', ('affecter (verbe) / effet (nom)', 'affect / effect')),
        EG('rise-raise', 'rise / raise', ('augmenter (intransitif / transitif)', 'rise / raise')),
        E('sensible', 'sensible', ('raisonnable, sensé', 'sensible')),
        E('economical', 'economical', ('économique, économe (qui consomme peu)', 'economical')),
        E('principle', 'principle', ('principe', 'principle')),
        E('currently', 'currently', ('actuellement', 'currently')),
      ], [
        x('The new rules will affect small businesses, but the effect on large firms will be limited.', 'Les nouvelles règles toucheront les petites entreprises, mais l’effet sur les grandes sera limité.'),
        x('This car is very economical: it uses only four litres per 100 km.', 'Cette voiture est très économique : elle ne consomme que quatre litres aux 100 km.'),
      ], [
        FB(CHOOSE, 'The strike will seriously ＿ deliveries.', ['affect', 'effect', 'afflict'], 'affect', ('Verbe : affect.', 'Verb: affect.'), ('La grève va sérieusement perturber les livraisons.', 'The strike will seriously affect deliveries.')),
        FB(CHOOSE, 'The company decided to ＿ its prices.', ['raise', 'rise', 'arise'], 'raise', ('Transitif (avec complément) : raise.', 'Transitive (with object): raise.'), ('L’entreprise a décidé d’augmenter ses prix.', 'The company decided to raise its prices.')),
        FB(CHOOSE, 'Taking the train is the most ＿ option.', ['sensible', 'sensitive', 'sensational'], 'sensible', ('Raisonnable : sensible.', 'Reasonable: sensible.'), ('Prendre le train est l’option la plus raisonnable.', 'Taking the train is the most sensible option.')),
        FB(CHOOSE, 'The website is ＿ under maintenance and will be back online at 6 p.m.', ['currently', 'eventually', 'lately'], 'currently', ('Actuellement : currently (actually = en fait).', 'At the moment: currently (actually = in fact).'), ('Le site est actuellement en maintenance et sera de nouveau accessible à 18 h.', 'The website is currently under maintenance and will be back online at 6 p.m.')),
      ]),
  ]),
  CH('c1-w8-c2', ('Négocier au sommet', 'High-level negotiation'), [
    L('en-advanced-negotiation', ('La négociation avancée', 'Advanced negotiation'), ('Mener une négociation complexe jusqu’à l’accord.', 'Lead a complex negotiation to an agreement.'), 9, [
        ('Sonder : What would it take for you to…? / Where do you have some flexibility? Conditionner : We could consider…, subject to… (sous réserve de).', 'Probing: What would it take for you to…? / Where do you have some flexibility? Conditioning: We could consider…, subject to…'),
        ('Débloquer : Let’s find some common ground (un terrain d’entente). / Can we meet each other halfway (couper la poire en deux)? / That’s a deal-breaker (point de rupture) for us.', 'Unblocking: Let’s find some common ground. / Can we meet each other halfway? / That’s a deal-breaker for us.'),
      ], [
        E('common-ground', 'common ground', ('terrain d’entente', 'common ground')),
        E('meet-halfway', 'to meet halfway', ('faire un compromis, couper la poire en deux', 'to meet halfway')),
        E('deal-breaker', 'deal-breaker', ('point de rupture (rédhibitoire)', 'deal-breaker')),
        E('flexibility', 'flexibility', ('souplesse, marge de manœuvre', 'flexibility')),
        E('subject-to', 'subject to', ('sous réserve de', 'subject to')),
        E('concession', 'concession', ('concession', 'concession')),
      ], [
        x('We could consider a longer contract, subject to a review after one year.', 'Nous pourrions envisager un contrat plus long, sous réserve d’un bilan au bout d’un an.'),
        x('Exclusive rights are a deal-breaker for us, but perhaps we can meet halfway on price.', 'Les droits exclusifs sont rédhibitoires pour nous, mais nous pourrions peut-être faire un compromis sur le prix.'),
      ], [
        FB(COMPLETE, 'Let’s try to find some common ＿.', ['ground', 'land', 'field'], 'ground', ('Terrain d’entente : common ground.', 'Shared position: common ground.'), ('Essayons de trouver un terrain d’entente.', 'Let’s try to find some common ground.')),
        FB(COMPLETE, 'The offer is ＿ to approval by our lawyers.', ['subject', 'object', 'subjective'], 'subject', ('Sous réserve de : subject to.', 'Depending on: subject to.'), ('L’offre est sous réserve de validation par nos avocats.', 'The offer is subject to approval by our lawyers.')),
        DC(ANSWER, [('Supplier', 'We cannot go below 50 pounds per unit.')], ('Tu proposais 40 livres ; trouve un compromis.', 'You offered 40 pounds; find a compromise.'), ['Could we meet halfway at 45, provided you cover delivery?', 'Then the deal is over forever.', 'OK, 50, whatever you want.'], 'Could we meet halfway at 45, provided you cover delivery?', ('Compromis conditionnel.', 'Conditional compromise.')),
        TF('The delivery date is a deal-breaker for us.', ('La date de livraison est négociable.', 'The delivery date is negotiable.'), FAUX, ('deal-breaker = point non négociable.', 'deal-breaker = non-negotiable point.')),
      ]),
  ])])

write_level('C1', ('C1 : le retour d’Excalibur', 'C1: the return of Excalibur'), REGION, 'Northern Isles', 26,
  [W1, W2, W3, W4, W5, W6, W7, W8, FINAL('C1', REGION, ('Simulation TOEIC C1 : l’île d’Avalon', 'TOEIC C1 simulation: the Isle of Avalon'), 945)], PREVIOUS + ['content/a2/a2.json', 'content/b1/b1.json', 'content/b2/b2.json'])
