# Niveau Goethe-Zertifikat C1 (allemand, CECRL C1) : 8 étapes le long du Danube, de Worms à Vienne et à Prague, parmi les Nibelungen et les légendes des villes.
# Mode histoire : l'apprenti·e des frères Grimm franchit « la porte des savants » ; les héros de l'épopée exigent une langue soutenue (voir gen-story.py).
# Usage : python3 scripts/goethec1-level.py   (réécrit content/goethec1/goethec1.json ; les niveaux A1 à B2 doivent déjà exister)
from de_common import *
begin('GOETHEC1')

REGION = 'Danube des Nibelungen'

# ═════════════════════════ 1 : Le style nominal, les locutions à verbe support ═════════════════════════
W1 = WORLD('goethec1-w1', ('La lande du Dragon', 'The Dragon’s heath'), REGION,
  ('Condenser une subordonnée en groupe nominal, employer les locutions à verbe support de la langue soutenue, parler d’exploit et de renommée.', 'Condense a subordinate clause into a noun phrase, use the support-verb phrases of formal German, talk about feats and fame.'),
  (('Le Dragon Fafnir', 'The Dragon Fafnir'), '☄', ('Sur la lande, le Dragon Fafnir couve l’or du Rhin et ne répond qu’aux phrases denses des chroniques. Dis en un groupe nominal ce que d’autres disent en une subordonnée, et il baissera la tête.', 'On the heath, the Dragon Fafnir broods over the Rhine gold and answers only the dense sentences of the chronicles. Say in one noun phrase what others say in a clause, and he will lower his head.')),
  [CH('goethec1-w1-c1', ('La langue des chroniques', 'The language of chronicles'), [
    L('de-nominalstil', ('De la subordonnée au groupe nominal', 'From clause to noun phrase'), ('Transformer une subordonnée en complément nominal avec la bonne préposition.', 'Turn a subordinate clause into a noun complement with the right preposition.'), 10, [
        ('Chaque conjonction a sa préposition : weil → wegen / aufgrund (+ génitif) ; obwohl → trotz ; wenn / falls → bei / im Falle ; nachdem → nach ; bevor → vor ; während → während ; damit / um… zu → zu / zwecks ; indem → durch.', 'Each conjunction has its preposition: weil → wegen / aufgrund (+ genitive); obwohl → trotz; wenn / falls → bei / im Falle; nachdem → nach; bevor → vor; während → während; damit / um… zu → zu / zwecks; indem → durch.'),
        ('Le verbe devient un nom, son sujet ou son objet passe au génitif : Nachdem der Drache besiegt worden war… → Nach dem Sieg über den Drachen… ; Weil der Schatz verloren ging… → Wegen des Verlusts des Schatzes…', 'The verb becomes a noun, its subject or object goes into the genitive: Nachdem der Drache besiegt worden war… → Nach dem Sieg über den Drachen… ; Weil der Schatz verloren ging… → Wegen des Verlusts des Schatzes…'),
        ('L’adverbe devient adjectif : Weil die Preise stark steigen → wegen des starken Anstiegs der Preise. Le pronom sujet devient possessif : Bevor er abreiste → vor seiner Abreise.', 'The adverb becomes an adjective: Weil die Preise stark steigen → wegen des starken Anstiegs der Preise. The subject pronoun becomes a possessive: Bevor er abreiste → vor seiner Abreise.'),
      ], [
        DG('nominal-kausal', 'weil … → wegen / aufgrund + Genitiv', ('cause : de la subordonnée au groupe nominal', 'cause: from clause to noun phrase')),
        DG('nominal-konzessiv', 'obwohl … → trotz + Genitiv', ('concession : de la subordonnée au groupe nominal', 'concession: from clause to noun phrase')),
        DG('nominal-temporal', 'nachdem … → nach + Dativ', ('temps : de la subordonnée au groupe nominal', 'time: from clause to noun phrase')),
        DG('nominal-final', 'um … zu → zu / zwecks', ('but : de la subordonnée au groupe nominal', 'purpose: from clause to noun phrase')),
        DG('nominal-modal', 'indem … → durch + Akkusativ', ('moyen : de la subordonnée au groupe nominal', 'means: from clause to noun phrase')),
        D('sieg', 'der Sieg', ('la victoire', 'the victory')),
        D('verlust', 'der Verlust', ('la perte', 'the loss')),
        D('abreise', 'die Abreise', ('le départ (en voyage)', 'the departure')),
        D('zwecks', 'zwecks', ('en vue de, aux fins de', 'for the purpose of')),
      ], [
        x('Nach dem Sieg über den Drachen badete Siegfried in dessen Blut.', 'Après sa victoire sur le dragon, Siegfried se baigna dans son sang.', 'After his victory over the dragon, Siegfried bathed in its blood.'),
        x('Trotz seiner Unverwundbarkeit blieb eine Stelle zwischen den Schultern ungeschützt.', 'Malgré son invulnérabilité, un endroit entre les épaules resta sans protection.', 'Despite his invulnerability, one spot between the shoulders remained unprotected.'),
      ], [
        FB(CHOOSE, '＿ des schlechten Wetters wurde das Fest verschoben. (= Weil das Wetter schlecht war)', ['Wegen', 'Trotz', 'Zwecks'], 'Wegen', ('Weil → wegen + génitif.', 'Weil → wegen + genitive.'), ('En raison du mauvais temps, la fête a été reportée.', 'Because of the bad weather, the celebration was postponed.')),
        FB(CHOOSE, '＿ seiner Ankunft rief er sofort an. (= Nachdem er angekommen war)', ['Nach', 'Vor', 'Bei'], 'Nach', ('Nachdem → nach + datif.', 'Nachdem → nach + dative.'), ('Après son arrivée, il a tout de suite appelé.', 'After his arrival, he called at once.')),
        FB(CHOOSE, 'Durch ＿ kann man viel Geld sparen. (= Indem man Preise vergleicht)', ['den Vergleich der Preise', 'die Preise vergleichen', 'dem Vergleich die Preise'], 'den Vergleich der Preise', ('Indem → durch + accusatif, objet au génitif.', 'Indem → durch + accusative, object in the genitive.'), ('En comparant les prix, on peut économiser beaucoup d’argent.', 'By comparing prices, you can save a lot of money.')),
        FB(CHOOSE, '＿ großer Anstrengung gelang es ihm nicht. (= Obwohl er sich sehr anstrengte)', ['Trotz', 'Wegen', 'Durch'], 'Trotz', ('Obwohl → trotz.', 'Obwohl → trotz.'), ('Malgré de grands efforts, il n’y est pas parvenu.', 'Despite great effort, he did not succeed.')),
      ]),
    L('de-fvg', ('Les verbes supports : zum Ausdruck bringen', 'Support verbs: zum Ausdruck bringen'), ('Reconnaître et employer les locutions figées de la langue administrative et savante.', 'Recognise and use the fixed phrases of administrative and scholarly German.'), 9, [
        ('Sens actif avec bringen, stellen, nehmen, treffen : zum Ausdruck bringen (exprimer), in Frage stellen (remettre en question), in Betracht ziehen (prendre en considération), zur Kenntnis nehmen (prendre acte de), Maßnahmen ergreifen (prendre des mesures).', 'Active meaning with bringen, stellen, nehmen, treffen: zum Ausdruck bringen (to express), in Frage stellen (to call into question), in Betracht ziehen (to take into consideration), zur Kenntnis nehmen (to take note of), Maßnahmen ergreifen (to take measures).'),
        ('Sens passif avec kommen, stehen, finden, geraten : zum Ausdruck kommen (s’exprimer), zur Sprache kommen (être abordé), unter Druck stehen, Anerkennung finden (être reconnu), in Vergessenheit geraten (tomber dans l’oubli).', 'Passive meaning with kommen, stehen, finden, geraten: zum Ausdruck kommen (to be expressed), zur Sprache kommen (to be raised), unter Druck stehen, Anerkennung finden (to be recognised), in Vergessenheit geraten (to fall into oblivion).'),
        ('Ces locutions précisent le déroulement : in Gang setzen (mettre en marche), in Kraft treten (entrer en vigueur), zum Abschluss bringen (mener à terme), ein Ende nehmen (prendre fin).', 'These phrases specify how the action unfolds: in Gang setzen (to set in motion), in Kraft treten (to come into force), zum Abschluss bringen (to bring to a close), ein Ende nehmen (to come to an end).'),
      ], [
        D('zum-ausdruck-bringen', 'zum Ausdruck bringen', ('exprimer', 'to express')),
        D('in-frage-stellen', 'in Frage stellen', ('remettre en question', 'to call into question')),
        D('in-betracht-ziehen', 'in Betracht ziehen', ('prendre en considération', 'to take into consideration')),
        D('zur-kenntnis-nehmen', 'zur Kenntnis nehmen', ('prendre acte de', 'to take note of')),
        D('massnahmen-ergreifen', 'Maßnahmen ergreifen', ('prendre des mesures', 'to take measures')),
        D('zur-sprache-kommen', 'zur Sprache kommen', ('être abordé, être évoqué', 'to be raised, to come up')),
        D('in-vergessenheit-geraten', 'in Vergessenheit geraten', ('tomber dans l’oubli', 'to fall into oblivion')),
        D('in-kraft-treten', 'in Kraft treten', ('entrer en vigueur', 'to come into force')),
      ], [
        x('Das Nibelungenlied war lange in Vergessenheit geraten, ehe es im 18. Jahrhundert wiederentdeckt wurde.', 'La Chanson des Nibelungen était longtemps tombée dans l’oubli avant d’être redécouverte au XVIIIe siècle.', 'The Nibelungenlied had long fallen into oblivion before it was rediscovered in the eighteenth century.'),
        x('Niemand wagte es, Siegfrieds Mut in Frage zu stellen.', 'Personne n’osait remettre en question le courage de Siegfried.', 'Nobody dared to call Siegfried’s courage into question.'),
      ], [
        FB(CHOOSE, 'Die Regierung muss endlich Maßnahmen ＿.', ['ergreifen', 'stellen', 'bringen'], 'ergreifen', ('Maßnahmen ergreifen.', 'Maßnahmen ergreifen.'), ('Le gouvernement doit enfin prendre des mesures.', 'The government must finally take measures.')),
        FB(CHOOSE, 'Das neue Gesetz ＿ am ersten Januar in Kraft.', ['tritt', 'kommt', 'bringt'], 'tritt', ('In Kraft treten.', 'In Kraft treten.'), ('La nouvelle loi entre en vigueur le premier janvier.', 'The new law comes into force on the first of January.')),
        FB(CHOOSE, 'In der Sitzung ＿ auch die Finanzen zur Sprache.', ['kamen', 'brachten', 'stellten'], 'kamen', ('Sens passif : zur Sprache kommen.', 'Passive meaning: zur Sprache kommen.'), ('Lors de la réunion, les finances ont aussi été abordées.', 'At the meeting, finances were also raised.')),
        FB(CHOOSE, 'Wir sollten auch andere Möglichkeiten in Betracht ＿.', ['ziehen', 'nehmen', 'treffen'], 'ziehen', ('In Betracht ziehen.', 'In Betracht ziehen.'), ('Nous devrions aussi envisager d’autres possibilités.', 'We should also consider other options.')),
      ]),
  ]),
  CH('goethec1-w1-c2', ('La gloire de Siegfried', 'Siegfried’s glory'), [
    L('de-ruhm', ('L’exploit et la renommée', 'Feats and fame'), ('Parler de réussite, de réputation et de reconnaissance.', 'Talk about success, reputation and recognition.'), 8, [
        ('La réussite : die Leistung (la performance), der Erfolg, etwas vollbringen (accomplir), sich bewähren (faire ses preuves), sich auszeichnen durch (se distinguer par), übertreffen (surpasser).', 'Success: die Leistung (the achievement), der Erfolg, etwas vollbringen (to accomplish), sich bewähren (to prove oneself), sich auszeichnen durch (to distinguish oneself by), übertreffen (to surpass).'),
        ('La réputation : der Ruf (la réputation), der Ruhm (la gloire), das Ansehen (le prestige), die Anerkennung (la reconnaissance), bewundern (admirer), beneiden (envier), der Neid (l’envie).', 'Reputation: der Ruf (the reputation), der Ruhm (fame, glory), das Ansehen (prestige), die Anerkennung (recognition), bewundern (to admire), beneiden (to envy), der Neid (envy).'),
        ('Nuancer un éloge : Er gilt als… (il passe pour…). Sie genießt hohes Ansehen. Sein Ruf eilt ihm voraus (sa réputation le précède). Hochmut kommt vor dem Fall (l’orgueil précède la chute).', 'Qualifying praise: Er gilt als… (he is considered…). Sie genießt hohes Ansehen. Sein Ruf eilt ihm voraus (his reputation precedes him). Hochmut kommt vor dem Fall (pride comes before a fall).'),
      ], [
        D('leistung', 'die Leistung', ('la performance, la prestation', 'the achievement, the performance')),
        D('vollbringen', 'vollbringen', ('accomplir', 'to accomplish')),
        D('sich-bewaehren', 'sich bewähren', ('faire ses preuves', 'to prove oneself')),
        D('uebertreffen', 'übertreffen', ('surpasser', 'to surpass')),
        D('ruf', 'der Ruf', ('la réputation', 'the reputation')),
        D('ansehen', 'das Ansehen', ('le prestige, la considération', 'prestige, standing')),
        D('gelten-als', 'gelten als', ('passer pour, être considéré comme', 'to be considered (as)')),
        D('neid', 'der Neid', ('l’envie, la jalousie', 'envy')),
      ], [
        x('Siegfried galt als der stärkste aller Helden, und sein Ruf eilte ihm voraus.', 'Siegfried passait pour le plus fort de tous les héros, et sa réputation le précédait.', 'Siegfried was considered the strongest of all heroes, and his reputation preceded him.'),
        x('Sein Ruhm weckte am Hof nicht nur Bewunderung, sondern auch Neid.', 'À la cour, sa gloire n’éveilla pas seulement l’admiration, mais aussi l’envie.', 'At court his fame aroused not only admiration but also envy.'),
      ], [
        FB(CHOOSE, 'Sie gilt ＿ eine der besten Ärztinnen des Landes.', ['als', 'für', 'wie'], 'als', ('Gelten als + nominatif.', 'Gelten als + nominative.'), ('Elle passe pour l’une des meilleures médecins du pays.', 'She is considered one of the best doctors in the country.')),
        FB(COMPLETE, 'Der neue Mitarbeiter hat sich in der Krise ＿: Man kann sich auf ihn verlassen.', ['bewährt', 'beneidet', 'übertroffen'], 'bewährt', ('Faire ses preuves : sich bewähren.', 'To prove oneself: sich bewähren.'), ('Le nouveau collègue a fait ses preuves pendant la crise : on peut compter sur lui.', 'The new colleague proved himself during the crisis: he can be relied on.')),
        TF('Das Ergebnis hat alle Erwartungen übertroffen.', ('Le résultat est décevant.', 'The result is disappointing.'), FAUX, ('Übertreffen = dépasser, surpasser.', 'Übertreffen = to exceed, to surpass.')),
        DC(ANSWER, [('Kollege', 'Frau Dr. Sommer hat schon wieder einen Preis bekommen. Ist das nicht übertrieben?')], ('Un collègue jalouse une chercheuse primée (réponds qu’elle jouit à juste titre d’une grande considération).', 'A colleague is jealous of a prize-winning researcher (reply that she rightly enjoys high standing).'), ['Ich finde, sie genießt zu Recht hohes Ansehen.', 'Ich finde, sie genießt zu Recht hohen Neid.', 'Ich finde, sie gilt zu Recht für hohes Ansehen.'], 'Ich finde, sie genießt zu Recht hohes Ansehen.', ('Hohes Ansehen genießen.', 'Hohes Ansehen genießen.')),
      ]),
  ])])

# ═════════════════════════ 2 : Attributs étendus, gérondif, pouvoir ═════════════════════════
W2 = WORLD('goethec1-w2', ('La cour de Worms', 'The court of Worms'), REGION,
  ('Lire et construire les attributs étendus de la langue écrite, exprimer ce qui est à faire avec zu + participe, parler de pouvoir et de politique.', 'Read and build the extended attributes of written German, express what is to be done with zu + participle, talk about power and politics.'),
  (('La Reine Kriemhild', 'Queen Kriemhild'), '♛', ('Devant la cathédrale de Worms, deux reines se disputent le pas. La Reine Kriemhild pèse chaque titre : il te faudra des phrases longues et sans faute, où tout ce qui qualifie le nom se glisse devant lui.', 'In front of Worms cathedral, two queens argue over precedence. Queen Kriemhild weighs every title: you will need long, flawless sentences in which everything that qualifies the noun slips in before it.')),
  [CH('goethec1-w2-c1', ('Chaque mot à sa place', 'Every word in its place'), [
    L('de-attribut-erweitert', ('Les attributs étendus : lire la phrase à tiroirs', 'Extended attributes: reading the nested phrase'), ('Décoder et former les longs groupes placés entre l’article et le nom.', 'Decode and form the long groups placed between the article and the noun.'), 10, [
        ('Entre l’article et le nom, l’allemand écrit peut placer toute une relative condensée : die [seit Jahren in Worms lebende] Königin = die Königin, die seit Jahren in Worms lebt. On lit d’abord l’article et le nom, puis le groupe de droite à gauche.', 'Between the article and the noun, written German can place a whole condensed relative clause: die [seit Jahren in Worms lebende] Königin = die Königin, die seit Jahren in Worms lebt. Read the article and the noun first, then the group from right to left.'),
        ('Participe I = relative active et simultanée : der [laut schreiende] Bote. Participe II = relative passive ou achevée : der [von Hagen verratene] Held ; die [gestern eingetroffenen] Gäste.', 'Participle I = active, simultaneous relative: der [laut schreiende] Bote. Participle II = passive or completed relative: der [von Hagen verratene] Held; die [gestern eingetroffenen] Gäste.'),
        ('Un adjectif peut aussi porter des compléments : ein [für alle Beteiligten vorteilhafter] Vertrag ; die [auf ihren Rang stolze] Königin. Le participe ou l’adjectif garde sa terminaison d’épithète.', 'An adjective can also carry complements: ein [für alle Beteiligten vorteilhafter] Vertrag; die [auf ihren Rang stolze] Königin. The participle or adjective keeps its attributive ending.'),
      ], [
        DG('attribut-part1', 'die seit Jahren hier lebende Familie', ('attribut étendu au participe I (relative active)', 'extended attribute with participle I (active relative)')),
        DG('attribut-part2', 'der von allen bewunderte Held', ('attribut étendu au participe II (relative passive)', 'extended attribute with participle II (passive relative)')),
        DG('attribut-adj', 'ein für alle vorteilhafter Vertrag', ('adjectif épithète avec complément', 'attributive adjective with a complement')),
        D('beteiligt', 'beteiligt an', ('impliqué dans, qui participe à', 'involved in')),
        D('eintreffen', 'eintreffen', ('arriver (officiel)', 'to arrive (formal)')),
        D('verraten', 'verraten', ('trahir', 'to betray')),
        D('rang', 'der Rang', ('le rang', 'the rank')),
        D('vorteilhaft', 'vorteilhaft', ('avantageux', 'advantageous')),
      ], [
        x('Die auf ihren Rang stolze Königin wollte als Erste den Dom betreten.', 'La reine, fière de son rang, voulait entrer la première dans la cathédrale.', 'The queen, proud of her rank, wanted to be the first to enter the cathedral.'),
        x('Der von seinem eigenen Freund verratene Held ahnte nichts.', 'Le héros, trahi par son propre ami, ne se doutait de rien.', 'The hero, betrayed by his own friend, suspected nothing.'),
      ], [
        FB(CHOOSE, 'Die gestern ＿ Gäste wohnen im Schloss. (= die gestern eingetroffen sind)', ['eingetroffenen', 'eintreffenden', 'eingetroffen'], 'eingetroffenen', ('Action achevée : participe II décliné.', 'Completed action: declined participle II.'), ('Les invités arrivés hier logent au château.', 'The guests who arrived yesterday are staying at the castle.')),
        FB(CHOOSE, 'Die in dieser Stadt ＿ Menschen sind stolz auf ihren Dom. (= die hier leben)', ['lebenden', 'gelebten', 'lebende'], 'lebenden', ('Action en cours : participe I, pluriel avec article.', 'Ongoing action: participle I, plural with an article.'), ('Les gens qui vivent dans cette ville sont fiers de leur cathédrale.', 'The people living in this town are proud of their cathedral.')),
        FB(CHOOSE, 'Das ist ein für beide Seiten ＿ Kompromiss.', ['annehmbarer', 'annehmbare', 'annehmbar'], 'annehmbarer', ('Ein + masculin nominatif : -er.', 'Ein + masculine nominative: -er.'), ('C’est un compromis acceptable pour les deux parties.', 'That is a compromise acceptable to both sides.')),
        TF('Der von der Presse scharf kritisierte Minister trat zurück.', ('Le ministre a critiqué la presse.', 'The minister criticised the press.'), FAUX, ('Von der Presse kritisiert = critiqué par la presse.', 'Von der Presse kritisiert = criticised by the press.')),
      ]),
    L('de-gerundivum', ('Ce qui est à faire : das zu lösende Problem', 'What is to be done: das zu lösende Problem'), ('Exprimer une nécessité ou une possibilité passive devant le nom.', 'Express a passive necessity or possibility before the noun.'), 8, [
        ('Zu + participe I devant un nom = qui doit ou peut être fait : das zu lösende Problem (= das Problem, das gelöst werden muss) ; die zu erwartenden Kosten (= die Kosten, die zu erwarten sind).', 'Zu + participle I before a noun = that must or can be done: das zu lösende Problem (= das Problem, das gelöst werden muss); die zu erwartenden Kosten (= die Kosten, die zu erwarten sind).'),
        ('Avec un verbe à particule, zu s’intercale : die auszufüllenden Formulare ; der einzuhaltende Termin. La tournure correspond à sein + zu + infinitif : Die Formulare sind auszufüllen.', 'With a separable verb, zu is inserted: die auszufüllenden Formulare; der einzuhaltende Termin. The construction corresponds to sein + zu + infinitive: Die Formulare sind auszufüllen.'),
        ('Avec une négation ou kaum, le sens est « qui ne peut pas être fait » : ein nicht zu unterschätzendes Risiko (un risque à ne pas sous-estimer) ; ein kaum zu ertragender Lärm (un bruit à peine supportable).', 'With a negation or kaum, the meaning is “that cannot be done”: ein nicht zu unterschätzendes Risiko (a risk not to be underestimated); ein kaum zu ertragender Lärm (a barely bearable noise).'),
      ], [
        DG('gerundivum', 'zu + Partizip I (das zu lösende Problem)', ('gérondif : qui doit ou peut être fait', 'gerundive: that must or can be done')),
        DG('gerundivum-trennbar', 'die auszufüllenden Formulare', ('gérondif d’un verbe à particule', 'gerundive of a separable verb')),
        DG('gerundivum-negativ', 'ein nicht zu unterschätzendes Risiko', ('gérondif nié : qu’on ne peut pas…', 'negated gerundive: that cannot be…')),
        D('einhalten', 'einhalten', ('respecter (un délai, une règle)', 'to keep to, to comply with')),
        D('unterschaetzen', 'unterschätzen', ('sous-estimer', 'to underestimate')),
        D('ertragen', 'ertragen', ('supporter, endurer', 'to bear, to endure')),
        D('erwarten', 'erwarten', ('attendre, s’attendre à', 'to expect')),
        D('risiko', 'das Risiko', ('le risque', 'the risk')),
      ], [
        x('Die Beleidigung vor dem Dom war eine nicht zu verzeihende Kränkung.', 'L’insulte devant la cathédrale était un affront impardonnable.', 'The insult in front of the cathedral was an unforgivable affront.'),
        x('Die zu erwartende Rache ließ nicht lange auf sich warten.', 'La vengeance à laquelle il fallait s’attendre ne se fit pas attendre longtemps.', 'The revenge that was to be expected was not long in coming.'),
      ], [
        FB(CHOOSE, 'Bitte beachten Sie die ＿ Fristen. (= die Fristen, die einzuhalten sind)', ['einzuhaltenden', 'eingehaltenen', 'zu einhaltenden'], 'einzuhaltenden', ('Verbe à particule : ein-zu-haltend + en.', 'Separable verb: ein-zu-haltend + en.'), ('Veuillez tenir compte des délais à respecter.', 'Please note the deadlines to be met.')),
        FB(CHOOSE, 'Das ist ein nicht zu ＿ Problem.', ['unterschätzendes', 'unterschätztes', 'unterschätzen'], 'unterschätzendes', ('Zu + participe I, neutre après ein : -es.', 'Zu + participle I, neuter after ein: -es.'), ('C’est un problème à ne pas sous-estimer.', 'That is a problem not to be underestimated.')),
        FB(CHOOSE, 'Die zu ＿ Aufgaben stehen auf der Liste.', ['erledigenden', 'erledigten', 'erledigen'], 'erledigenden', ('Qui doivent être faites : zu erledigenden.', 'That must be done: zu erledigenden.'), ('Les tâches à accomplir figurent sur la liste.', 'The tasks to be done are on the list.')),
        TF('Die bereits bezahlten Rechnungen liegen links, die noch zu bezahlenden rechts.', ('Les factures de droite ont déjà été payées.', 'The bills on the right have already been paid.'), FAUX, ('Noch zu bezahlend = qui restent à payer.', 'Noch zu bezahlend = still to be paid.')),
      ]),
  ]),
  CH('goethec1-w2-c2', ('La querelle des reines', 'The queens’ quarrel'), [
    L('de-macht', ('Le pouvoir et la politique', 'Power and politics'), ('Parler d’institutions, de décisions et de rapports de force.', 'Talk about institutions, decisions and power relations.'), 8, [
        ('Les institutions : die Regierung (le gouvernement), das Parlament, der Abgeordnete (le député), die Partei (le parti), die Opposition, die Wahl (l’élection), die Verfassung (la constitution), die Behörde (l’administration).', 'Institutions: die Regierung (the government), das Parlament, der Abgeordnete (the member of parliament), die Partei (the party), die Opposition, die Wahl (the election), die Verfassung (the constitution), die Behörde (the authority).'),
        ('Décider : ein Gesetz verabschieden (adopter une loi), abstimmen über (voter sur), beschließen (décider), zurücktreten (démissionner), verhandeln (négocier), sich durchsetzen (s’imposer), der Kompromiss.', 'Deciding: ein Gesetz verabschieden (to pass a law), abstimmen über (to vote on), beschließen (to resolve), zurücktreten (to resign), verhandeln (to negotiate), sich durchsetzen (to prevail), der Kompromiss.'),
        ('Le pouvoir : die Macht, der Einfluss (l’influence), die Herrschaft (la domination), der Machtkampf (la lutte de pouvoir), jemanden stürzen (renverser), die Mehrheit erringen (obtenir la majorité).', 'Power: die Macht, der Einfluss (influence), die Herrschaft (rule), der Machtkampf (the power struggle), jemanden stürzen (to overthrow), die Mehrheit erringen (to win the majority).'),
      ], [
        D('regierung', 'die Regierung', ('le gouvernement', 'the government')),
        D('abgeordnete', 'der / die Abgeordnete', ('le député, la députée', 'the member of parliament')),
        D('verfassung', 'die Verfassung', ('la constitution', 'the constitution')),
        D('verabschieden', 'ein Gesetz verabschieden', ('adopter une loi', 'to pass a law')),
        D('zuruecktreten', 'zurücktreten', ('démissionner (d’une fonction)', 'to step down')),
        D('verhandeln', 'verhandeln', ('négocier', 'to negotiate')),
        D('sich-durchsetzen', 'sich durchsetzen', ('s’imposer', 'to prevail, to assert oneself')),
        D('macht', 'die Macht', ('le pouvoir', 'power')),
        D('einfluss', 'der Einfluss', ('l’influence', 'influence')),
      ], [
        x('Nach langen Verhandlungen hat das Parlament das umstrittene Gesetz verabschiedet.', 'Après de longues négociations, le parlement a adopté la loi controversée.', 'After long negotiations, parliament passed the controversial law.'),
        x('Hinter dem Streit der Königinnen stand ein Machtkampf zwischen zwei Höfen.', 'Derrière la querelle des reines se cachait une lutte de pouvoir entre deux cours.', 'Behind the queens’ quarrel lay a power struggle between two courts.'),
      ], [
        FB(COMPLETE, 'Nach dem Skandal musste die Ministerin ＿.', ['zurücktreten', 'verabschieden', 'verhandeln'], 'zurücktreten', ('Démissionner : zurücktreten.', 'To step down: zurücktreten.'), ('Après le scandale, la ministre a dû démissionner.', 'After the scandal, the minister had to step down.')),
        FB(CHOOSE, 'Morgen stimmen die Abgeordneten ＿ den Haushalt ab.', ['über', 'für', 'an'], 'über', ('Abstimmen über + accusatif.', 'Abstimmen über + accusative.'), ('Demain, les députés votent sur le budget.', 'Tomorrow the members vote on the budget.')),
        TF('Die Opposition konnte sich mit ihrem Vorschlag nicht durchsetzen.', ('La proposition de l’opposition a été adoptée.', 'The opposition’s proposal was adopted.'), FAUX, ('Sich nicht durchsetzen = ne pas réussir à s’imposer.', 'Sich nicht durchsetzen = to fail to prevail.')),
        DC(ANSWER, [('Journalist', 'Wie beurteilen Sie den Kompromiss, den die Regierung gestern vorgestellt hat?')], ('Un journaliste te demande ton avis sur un compromis (tu le juges acceptable pour toutes les parties).', 'A journalist asks your view of a compromise (you find it acceptable to all parties).'), ['Es ist eine für alle Beteiligten annehmbare Lösung.', 'Es ist eine für alle Beteiligte annehmbar Lösung.', 'Es ist eine Lösung für alle annehmbaren Beteiligten zu lösen.'], 'Es ist eine für alle Beteiligten annehmbare Lösung.', ('Attribut étendu : für alle Beteiligten annehmbare.', 'Extended attribute: für alle Beteiligten annehmbare.')),
      ]),
  ])])

# ═════════════════════════ 3 : Discours rapporté avancé, les médias ═════════════════════════
W3 = WORLD('goethec1-w3', ('La forêt d’Odenwald', 'The Odenwald forest'), REGION,
  ('Rapporter questions, ordres et prières au discours indirect, choisir le verbe introducteur juste, parler de presse et d’information.', 'Report questions, orders and requests in indirect speech, choose the right reporting verb, talk about the press and information.'),
  (('Hagen de Tronje', 'Hagen of Tronje'), '⚔', ('À la source de l’Odenwald, Hagen a caché sa lance et prépare son récit : il jure qu’il n’y est pour rien. Rapporte ses paroles, ses questions et ses ordres sans les prendre à ton compte, et la vérité paraîtra d’elle-même.', 'At the Odenwald spring, Hagen has hidden his spear and prepares his story: he swears he had nothing to do with it. Report his words, questions and orders without vouching for them, and the truth will appear by itself.')),
  [CH('goethec1-w3-c1', ('Il aurait dit que…', 'He is said to have said…'), [
    L('de-indirekte-rede-2', ('Questions et ordres rapportés', 'Reported questions and orders'), ('Rapporter une question, un ordre ou une prière au Konjunktiv I.', 'Report a question, an order or a request in Konjunktiv I.'), 9, [
        ('Question rapportée : ob ou mot interrogatif + Konjunktiv I, verbe à la fin. Er fragte, ob sie die Stelle kenne. Sie wollte wissen, wann er zurückkomme und was geschehen sei.', 'Reported question: ob or question word + Konjunktiv I, verb at the end. Er fragte, ob sie die Stelle kenne. Sie wollte wissen, wann er zurückkomme und was geschehen sei.'),
        ('Ordre rapporté : sollen au Konjunktiv I. „Schweig!“ → Er sagte, sie solle schweigen. Prière polie : mögen. „Bitte warten Sie!“ → Er bat, man möge warten.', 'Reported order: sollen in Konjunktiv I. „Schweig!“ → Er sagte, sie solle schweigen. Polite request: mögen. „Bitte warten Sie!“ → Er bat, man möge warten.'),
        ('Les repères changent : ich → er / sie ; hier → dort ; heute → an jenem Tag ; morgen → am nächsten Tag ; gestern → am Tag zuvor. Le futur se rapporte avec werde : Er sagte, er werde kommen.', 'Reference points shift: ich → er / sie; hier → dort; heute → an jenem Tag; morgen → am nächsten Tag; gestern → am Tag zuvor. The future is reported with werde: Er sagte, er werde kommen.'),
      ], [
        DG('indirekte-frage-konj', 'Er fragte, ob sie … kenne.', ('question rapportée au Konjunktiv I', 'reported question in Konjunktiv I')),
        DG('indirekt-solle', 'Er sagte, sie solle schweigen.', ('ordre rapporté (solle)', 'reported order (solle)')),
        DG('indirekt-moege', 'Er bat, man möge warten.', ('prière rapportée (möge)', 'reported request (möge)')),
        DG('indirekt-werde', 'Er sagte, er werde kommen.', ('futur rapporté (werde)', 'reported future (werde)')),
        D('am-tag-zuvor', 'am Tag zuvor', ('la veille', 'the day before')),
        D('schweigen', 'schweigen', ('se taire', 'to be silent')),
        D('geschehen', 'geschehen', ('se passer, arriver', 'to happen (formal)')),
        D('auffordern', 'jemanden auffordern, … zu', ('sommer, inviter quelqu’un à', 'to call on someone to')),
      ], [
        x('Kriemhild fragte, wer ihren Mann getötet habe und warum niemand ihm geholfen habe.', 'Kriemhild demanda qui avait tué son mari et pourquoi personne ne l’avait aidé.', 'Kriemhild asked who had killed her husband and why nobody had helped him.'),
        x('Hagen erwiderte, sie solle nicht weiter fragen; Räuber hätten den Helden überfallen.', 'Hagen répliqua qu’elle ne devait pas poser d’autres questions ; des brigands avaient attaqué le héros.', 'Hagen retorted that she should ask no more questions; robbers had attacked the hero.'),
      ], [
        FB(CHOOSE, 'Sie fragte, ob er die Wahrheit ＿.', ['sage', 'sagt', 'sagen'], 'sage', ('Question rapportée : Konjunktiv I, sage.', 'Reported question: Konjunktiv I, sage.'), ('Elle demanda s’il disait la vérité.', 'She asked whether he was telling the truth.')),
        FB(CHOOSE, 'Der Arzt sagte, ich ＿ mehr schlafen.', ['solle', 'sollte gewesen', 'möge sein'], 'solle', ('Ordre ou conseil rapporté : solle.', 'Reported order or advice: solle.'), ('Le médecin a dit que je devais dormir davantage.', 'The doctor said that I should sleep more.')),
        FB(CHOOSE, 'Er kündigte an, er ＿ am nächsten Tag abreisen.', ['werde', 'wird', 'würde sein'], 'werde', ('Futur rapporté : werde.', 'Reported future: werde.'), ('Il annonça qu’il partirait le lendemain.', 'He announced that he would leave the next day.')),
        FB(CHOOSE, 'Die Rednerin bat, man ＿ die Handys ausschalten.', ['möge', 'mag', 'mochte'], 'möge', ('Prière rapportée : möge.', 'Reported request: möge.'), ('L’oratrice pria le public d’éteindre les téléphones.', 'The speaker asked that phones be switched off.')),
      ]),
    L('de-redeverben', ('Les verbes de parole', 'Reporting verbs'), ('Choisir un verbe introducteur précis au lieu de sagen.', 'Choose a precise reporting verb instead of sagen.'), 8, [
        ('Affirmer : erklären (déclarer), versichern (assurer), betonen (souligner), hervorheben (mettre en avant), einräumen (concéder), andeuten (laisser entendre).', 'Asserting: erklären (to declare), versichern (to assure), betonen (to stress), hervorheben (to highlight), einräumen (to concede), andeuten (to hint).'),
        ('Contredire et critiquer : widersprechen + datif (contredire), leugnen (nier), einwenden (objecter), bemängeln (déplorer), jemandem etwas vorwerfen (reprocher), anzweifeln (mettre en doute).', 'Contradicting and criticising: widersprechen + dative (to contradict), leugnen (to deny), einwenden (to object), bemängeln (to find fault with), jemandem etwas vorwerfen (to accuse someone of), anzweifeln (to cast doubt on).'),
        ('Demander et annoncer : fordern (exiger), appellieren an (en appeler à), ankündigen (annoncer), in Aussicht stellen (laisser espérer), sich äußern zu (s’exprimer sur), Stellung nehmen zu (prendre position sur).', 'Demanding and announcing: fordern (to demand), appellieren an (to appeal to), ankündigen (to announce), in Aussicht stellen (to hold out the prospect of), sich äußern zu (to comment on), Stellung nehmen zu (to take a stand on).'),
      ], [
        D('versichern', 'versichern', ('assurer, affirmer', 'to assure, to affirm')),
        D('einraeumen', 'einräumen', ('concéder, reconnaître', 'to concede')),
        D('andeuten', 'andeuten', ('laisser entendre', 'to hint, to imply')),
        D('leugnen', 'leugnen', ('nier', 'to deny (a fact)')),
        D('einwenden', 'einwenden', ('objecter', 'to object')),
        D('vorwerfen', 'jemandem etwas vorwerfen', ('reprocher quelque chose à quelqu’un', 'to accuse someone of something')),
        D('ankuendigen', 'ankündigen', ('annoncer', 'to announce')),
        D('stellung-nehmen', 'Stellung nehmen zu', ('prendre position sur', 'to take a stand on')),
      ], [
        x('Hagen leugnete die Tat nicht lange; später räumte er ein, den Helden getötet zu haben.', 'Hagen ne nia pas longtemps son acte ; plus tard, il reconnut avoir tué le héros.', 'Hagen did not deny the deed for long; later he conceded that he had killed the hero.'),
        x('Die Königin warf ihm vor, er habe das Vertrauen ihres Mannes missbraucht.', 'La reine lui reprocha d’avoir abusé de la confiance de son mari.', 'The queen accused him of having abused her husband’s trust.'),
      ], [
        FB(COMPLETE, 'Der Minister ＿ ein, dass Fehler gemacht worden seien.', ['räumte', 'leugnete', 'forderte'], 'räumte', ('Concéder : einräumen.', 'To concede: einräumen.'), ('Le ministre a reconnu que des erreurs avaient été commises.', 'The minister conceded that mistakes had been made.')),
        FB(CHOOSE, 'Die Gewerkschaft wirft ＿ vor, die Löhne zu drücken.', ['dem Unternehmen', 'das Unternehmen', 'des Unternehmens'], 'dem Unternehmen', ('Jemandem (datif) etwas vorwerfen.', 'Jemandem (dative) etwas vorwerfen.'), ('Le syndicat reproche à l’entreprise de tirer les salaires vers le bas.', 'The union accuses the company of pushing wages down.')),
        FB(CHOOSE, 'Zu den Vorwürfen wollte der Sprecher keine Stellung ＿.', ['nehmen', 'geben', 'machen'], 'nehmen', ('Stellung nehmen zu.', 'Stellung nehmen zu.'), ('Le porte-parole n’a pas voulu prendre position sur les accusations.', 'The spokesman declined to comment on the accusations.')),
        TF('Die Firma deutete an, dass es bald Entlassungen geben könnte.', ('L’entreprise a annoncé officiellement des licenciements.', 'The company officially announced redundancies.'), FAUX, ('Andeuten = laisser entendre, sans l’annoncer clairement.', 'Andeuten = to hint, without announcing it clearly.')),
      ]),
  ]),
  CH('goethec1-w3-c2', ('La version de Hagen', 'Hagen’s version'), [
    L('de-medien', ('La presse et l’information', 'The press and information'), ('Parler des médias, des sources et de la fiabilité d’une information.', 'Talk about the media, sources and the reliability of information.'), 8, [
        ('Les médias : die Berichterstattung (la couverture médiatique), die Schlagzeile (le gros titre), der Leitartikel (l’éditorial), die Meldung (la dépêche), die Quelle (la source), der Rundfunk (la radiodiffusion), die Pressefreiheit.', 'The media: die Berichterstattung (coverage), die Schlagzeile (the headline), der Leitartikel (the editorial), die Meldung (the news item), die Quelle (the source), der Rundfunk (broadcasting), die Pressefreiheit.'),
        ('Informer : recherchieren (enquêter), veröffentlichen (publier), enthüllen (révéler), verbreiten (diffuser), überprüfen (vérifier), sich berufen auf (se réclamer de, invoquer).', 'Informing: recherchieren (to research), veröffentlichen (to publish), enthüllen (to reveal), verbreiten (to spread), überprüfen (to check), sich berufen auf (to cite, to invoke).'),
        ('Juger une information : glaubwürdig (crédible), seriös (sérieux), einseitig (partial), die Falschmeldung (la fausse nouvelle), aus dem Zusammenhang reißen (sortir de son contexte), die Meinungsbildung (la formation de l’opinion).', 'Judging information: glaubwürdig (credible), seriös (reputable), einseitig (one-sided), die Falschmeldung (the false report), aus dem Zusammenhang reißen (to take out of context), die Meinungsbildung (opinion forming).'),
      ], [
        D('berichterstattung', 'die Berichterstattung', ('la couverture médiatique', 'media coverage, reporting')),
        D('schlagzeile', 'die Schlagzeile', ('le gros titre', 'the headline')),
        D('quelle', 'die Quelle', ('la source', 'the source')),
        D('veroeffentlichen', 'veröffentlichen', ('publier', 'to publish')),
        D('enthuellen', 'enthüllen', ('révéler, dévoiler', 'to reveal, to expose')),
        D('ueberpruefen', 'überprüfen', ('vérifier, contrôler', 'to check, to verify')),
        D('glaubwuerdig', 'glaubwürdig', ('crédible', 'credible')),
        D('einseitig', 'einseitig', ('partial, unilatéral', 'one-sided')),
        D('sich-berufen', 'sich berufen auf', ('invoquer, se réclamer de', 'to cite, to invoke')),
      ], [
        x('Die Zeitung beruft sich auf eine Quelle, die nicht genannt werden möchte.', 'Le journal invoque une source qui ne souhaite pas être nommée.', 'The newspaper cites a source who does not wish to be named.'),
        x('Eine einseitige Berichterstattung erschwert die freie Meinungsbildung.', 'Une couverture médiatique partiale rend plus difficile la libre formation de l’opinion.', 'One-sided coverage makes it harder to form opinions freely.'),
      ], [
        FB(COMPLETE, 'Bevor man eine Nachricht teilt, sollte man die ＿ überprüfen.', ['Quelle', 'Schlagzeile', 'Meinungsbildung'], 'Quelle', ('La source : die Quelle.', 'The source: die Quelle.'), ('Avant de partager une nouvelle, il faut en vérifier la source.', 'Before sharing a piece of news, you should check the source.')),
        FB(CHOOSE, 'Der Bericht beruft sich ＿ interne Dokumente.', ['auf', 'an', 'über'], 'auf', ('Sich berufen auf + accusatif.', 'Sich berufen auf + accusative.'), ('Le rapport s’appuie sur des documents internes.', 'The report cites internal documents.')),
        TF('Das Zitat wurde aus dem Zusammenhang gerissen und wirkt deshalb viel schärfer.', ('La citation a été replacée dans son contexte.', 'The quotation was put back in its context.'), FAUX, ('Aus dem Zusammenhang reißen = sortir du contexte.', 'Aus dem Zusammenhang reißen = to take out of context.')),
        DC(ANSWER, [('Freundin', 'Hast du gelesen? Angeblich wird das Museum für immer geschlossen!')], ('Une amie relaie une rumeur lue en ligne (tu veux d’abord savoir d’où vient l’information).', 'A friend passes on a rumour read online (you first want to know where the information comes from).'), ['Woher stammt die Meldung? Ist die Quelle glaubwürdig?', 'Woher stammt die Meldung? Ist die Quelle einseitig veröffentlicht?', 'Wohin stammt die Meldung? Ist die Schlagzeile glaubwürdig auf?'], 'Woher stammt die Meldung? Ist die Quelle glaubwürdig?', ('Vérifier la source : glaubwürdig.', 'Checking the source: glaubwürdig.')),
      ]),
  ])])

# ═════════════════════════ 4 : Connecteurs soutenus, concession, environnement ═════════════════════════
W4 = WORLD('goethec1-w4', ('Le puits du Basilic', 'The Basilisk’s well'), REGION,
  ('Employer les connecteurs de la langue soutenue, exprimer une concession nuancée, parler d’environnement et de climat.', 'Use the connectors of formal German, express a nuanced concession, talk about the environment and climate.'),
  (('Le Basilic de Vienne', 'The Basilisk of Vienna'), '☤', ('Dans un puits de la Schönlaterngasse, le Basilic empoisonne l’eau et l’air de tout le quartier. Nul ne peut le regarder en face : relie tes arguments avec précision, concède ce qu’il faut, et tends-lui le miroir.', 'In a well on Schönlaterngasse, the Basilisk poisons the water and air of the whole district. Nobody can look it in the face: link your arguments precisely, concede what you must, and hold up the mirror.')),
  [CH('goethec1-w4-c1', ('Si dangereux soit-il', 'However dangerous it may be'), [
    L('de-konnektoren-c1', ('Les connecteurs soutenus : indem, zumal, wohingegen', 'Formal connectors: indem, zumal, wohingegen'), ('Relier les idées avec les conjonctions de l’écrit.', 'Link ideas with the conjunctions of written German.'), 9, [
        ('Moyen : indem (en + participe présent) et dadurch, dass : Man besiegte ihn, indem man ihm einen Spiegel vorhielt. Cause renforcée : zumal (d’autant plus que) : Niemand ging hinunter, zumal die Luft giftig war.', 'Means: indem (by + -ing) and dadurch, dass: Man besiegte ihn, indem man ihm einen Spiegel vorhielt. Reinforced cause: zumal (especially as): Niemand ging hinunter, zumal die Luft giftig war.'),
        ('Opposition : wohingegen / während (alors que) : Die einen flohen, wohingegen der Bäckergeselle blieb. Restriction : insofern, als (dans la mesure où) ; nur dass (sauf que) ; außer dass / außer wenn.', 'Contrast: wohingegen / während (whereas): Die einen flohen, wohingegen der Bäckergeselle blieb. Restriction: insofern, als (insofar as); nur dass (except that); außer dass / außer wenn.'),
        ('Gradation : geschweige denn (encore moins, à plus forte raison) après une négation : Er konnte kaum stehen, geschweige denn laufen. Absence : ohne dass (sans que) ; anstatt dass (au lieu que).', 'Gradation: geschweige denn (let alone) after a negation: Er konnte kaum stehen, geschweige denn laufen. Absence: ohne dass (without); anstatt dass (instead of).'),
      ], [
        DG('indem', 'indem', ('en (faisant), par le fait de', 'by (doing)')),
        DG('zumal', 'zumal', ('d’autant plus que', 'especially as')),
        DG('wohingegen', 'wohingegen', ('alors que, tandis que (opposition)', 'whereas')),
        DG('insofern-als', 'insofern, als', ('dans la mesure où', 'insofar as')),
        DG('geschweige-denn', 'geschweige denn', ('encore moins, sans parler de', 'let alone, much less')),
        DG('ohne-dass', 'ohne dass', ('sans que', 'without (+ clause)')),
        DG('dadurch-dass', 'dadurch, dass', ('du fait que, par le fait que', 'by the fact that, through')),
        D('giftig', 'giftig', ('toxique, vénéneux', 'poisonous, toxic')),
        D('spiegel-vorhalten', 'jemandem den Spiegel vorhalten', ('tendre le miroir à quelqu’un', 'to hold up a mirror to someone')),
      ], [
        x('Der Geselle besiegte das Ungeheuer, indem er ihm einen Spiegel vorhielt.', 'Le compagnon vainquit le monstre en lui tendant un miroir.', 'The journeyman defeated the monster by holding up a mirror to it.'),
        x('Niemand wagte, in den Brunnen zu schauen, geschweige denn hinabzusteigen.', 'Personne n’osait regarder dans le puits, encore moins y descendre.', 'Nobody dared to look into the well, let alone climb down.'),
      ], [
        FB(CHOOSE, 'Man kann Energie sparen, ＿ man die Heizung niedriger stellt.', ['indem', 'zumal', 'wohingegen'], 'indem', ('Le moyen : indem.', 'The means: indem.'), ('On peut économiser de l’énergie en baissant le chauffage.', 'You can save energy by turning the heating down.')),
        FB(CHOOSE, 'Ich bleibe heute zu Hause, ＿ ich ohnehin erkältet bin.', ['zumal', 'indem', 'ohne dass'], 'zumal', ('Raison supplémentaire : zumal.', 'An additional reason: zumal.'), ('Je reste à la maison aujourd’hui, d’autant que je suis enrhumé de toute façon.', 'I am staying at home today, especially as I have a cold anyway.')),
        FB(CHOOSE, 'Er hat kein Geld für ein Fahrrad, ＿ für ein Auto.', ['geschweige denn', 'wohingegen', 'insofern als'], 'geschweige denn', ('Encore moins : geschweige denn.', 'Let alone: geschweige denn.'), ('Il n’a pas d’argent pour un vélo, encore moins pour une voiture.', 'He has no money for a bicycle, let alone a car.')),
        FB(CHOOSE, 'Im Norden regnet es viel, ＿ der Süden unter Trockenheit leidet.', ['wohingegen', 'zumal', 'indem'], 'wohingegen', ('Opposition : wohingegen.', 'Contrast: wohingegen.'), ('Il pleut beaucoup dans le nord, alors que le sud souffre de la sécheresse.', 'It rains a lot in the north, whereas the south suffers from drought.')),
      ]),
    L('de-konzessiv-c1', ('La concession nuancée : wenngleich, so… auch', 'Nuanced concession: wenngleich, so… auch'), ('Concéder un point avec les tournures de l’écrit.', 'Concede a point with the constructions of written German.'), 9, [
        ('Synonymes soutenus de obwohl : wenngleich, obgleich, obschon, wenn auch. Wenngleich die Gefahr bekannt war, unternahm niemand etwas.', 'Formal synonyms of obwohl: wenngleich, obgleich, obschon, wenn auch. Wenngleich die Gefahr bekannt war, unternahm niemand etwas.'),
        ('So + adjectif… auch (si… que) : So gefährlich das Tier auch war, es hatte eine Schwäche. Wie / was / wer… auch (immer) : Was auch immer geschieht, wir bleiben. La principale garde l’ordre normal, sans inversion.', 'So + adjective… auch (however…): So gefährlich das Tier auch war, es hatte eine Schwäche. Wie / was / wer… auch (immer): Was auch immer geschieht, wir bleiben. The main clause keeps normal order, with no inversion.'),
        ('Adverbes et prépositions : gleichwohl / nichtsdestotrotz / dennoch (néanmoins), allerdings (toutefois), ungeachtet + génitif (en dépit de), selbst wenn (même si), auch wenn.', 'Adverbs and prepositions: gleichwohl / nichtsdestotrotz / dennoch (nevertheless), allerdings (however), ungeachtet + genitive (regardless of), selbst wenn (even if), auch wenn.'),
      ], [
        DG('wenngleich', 'wenngleich / obgleich', ('bien que (soutenu)', 'although (formal)')),
        DG('so-auch', 'so + Adjektiv … auch', ('si… que, aussi… que', 'however + adjective')),
        DG('was-auch-immer', 'was / wer / wie auch immer', ('quoi que, qui que, de quelque manière que', 'whatever, whoever, however')),
        DG('gleichwohl', 'gleichwohl / nichtsdestotrotz', ('néanmoins', 'nevertheless, nonetheless')),
        DG('ungeachtet', 'ungeachtet + Genitiv', ('en dépit de, sans tenir compte de', 'regardless of, notwithstanding')),
        DG('selbst-wenn', 'selbst wenn', ('même si', 'even if')),
        D('schwaeche', 'die Schwäche', ('la faiblesse', 'the weakness')),
        D('etwas-unternehmen', 'etwas unternehmen gegen', ('agir contre, entreprendre quelque chose', 'to take action against')),
      ], [
        x('So schrecklich der Basilisk auch aussah, seinen eigenen Anblick ertrug er nicht.', 'Si effrayant que fût le Basilic, il ne supportait pas sa propre vue.', 'However terrible the Basilisk looked, it could not bear the sight of itself.'),
        x('Ungeachtet aller Warnungen stieg der junge Mann in den Brunnen.', 'En dépit de tous les avertissements, le jeune homme descendit dans le puits.', 'Regardless of all the warnings, the young man climbed into the well.'),
      ], [
        FB(CHOOSE, 'So teuer das Projekt auch ＿, es lohnt sich.', ['ist', 'wäre gewesen', 'sein'], 'ist', ('So… auch + verbe conjugué à la fin.', 'So… auch + conjugated verb at the end.'), ('Si coûteux que soit le projet, il en vaut la peine.', 'However expensive the project is, it is worth it.')),
        FB(CHOOSE, '＿ auch immer anruft, ich bin nicht da.', ['Wer', 'Was', 'Wie'], 'Wer', ('Une personne, sujet : wer auch immer.', 'A person, subject: wer auch immer.'), ('Qui que ce soit qui appelle, je ne suis pas là.', 'Whoever calls, I am not in.')),
        FB(CHOOSE, 'Ungeachtet ＿ wurde die Straße gebaut.', ['der Proteste', 'die Proteste', 'den Protesten'], 'der Proteste', ('Ungeachtet + génitif.', 'Ungeachtet + genitive.'), ('En dépit des protestations, la route a été construite.', 'Regardless of the protests, the road was built.')),
        order(('Remets dans l’ordre : « Si fatigué qu’il fût, il continua à travailler. »', 'Put in order: “However tired he was, he went on working.”'), ['So', 'müde', 'er', 'auch', 'war,', 'er', 'arbeitete', 'weiter.'], ('Après so… auch, la principale garde l’ordre sujet-verbe.', 'After so… auch, the main clause keeps subject-verb order.')),
      ]),
  ]),
  CH('goethec1-w4-c2', ('L’air empoisonné', 'The poisoned air'), [
    L('de-umwelt-c1', ('L’environnement et le climat', 'The environment and climate'), ('Parler de pollution, de ressources et de transition écologique.', 'Talk about pollution, resources and the green transition.'), 8, [
        ('Constater : der Klimawandel, die Erderwärmung (le réchauffement), der Ausstoß von Treibhausgasen (les émissions de gaz à effet de serre), die Dürre (la sécheresse), das Artensterben (l’extinction des espèces), die Verschmutzung.', 'Stating: der Klimawandel, die Erderwärmung (global warming), der Ausstoß von Treibhausgasen (greenhouse gas emissions), die Dürre (drought), das Artensterben (species extinction), die Verschmutzung.'),
        ('Agir : erneuerbare Energien (les énergies renouvelables), der Verbrauch (la consommation), Ressourcen schonen (ménager les ressources), verringern (réduire), verzichten auf (renoncer à), umsteigen auf (passer à), die Energiewende (la transition énergétique).', 'Acting: erneuerbare Energien (renewable energy), der Verbrauch (consumption), Ressourcen schonen (to conserve resources), verringern (to reduce), verzichten auf (to do without), umsteigen auf (to switch to), die Energiewende (the energy transition).'),
        ('Évaluer : umweltfreundlich / umweltschädlich (respectueux / nuisible), langfristig / kurzfristig (à long / court terme), die Folgen abschätzen (évaluer les conséquences), unumkehrbar (irréversible), dringend (urgent).', 'Assessing: umweltfreundlich / umweltschädlich (environmentally friendly / harmful), langfristig / kurzfristig (long-term / short-term), die Folgen abschätzen (to assess the consequences), unumkehrbar (irreversible), dringend (urgent).'),
      ], [
        D('erderwaermung', 'die Erderwärmung', ('le réchauffement climatique', 'global warming')),
        D('ausstoss', 'der Ausstoß', ('les émissions, le rejet', 'emissions, output')),
        D('duerre', 'die Dürre', ('la sécheresse', 'drought')),
        D('erneuerbar', 'erneuerbare Energien', ('les énergies renouvelables', 'renewable energy')),
        D('verbrauch', 'der Verbrauch', ('la consommation (d’énergie, de ressources)', 'consumption (of energy, resources)')),
        D('schonen', 'schonen', ('ménager, préserver', 'to conserve, to go easy on')),
        D('verringern', 'verringern', ('réduire, diminuer', 'to reduce')),
        D('langfristig', 'langfristig', ('à long terme', 'in the long term')),
        D('unumkehrbar', 'unumkehrbar', ('irréversible', 'irreversible')),
      ], [
        x('Der Ausstoß von Treibhausgasen muss langfristig deutlich verringert werden.', 'Les émissions de gaz à effet de serre doivent être nettement réduites à long terme.', 'Greenhouse gas emissions must be reduced significantly in the long term.'),
        x('Manche Schäden sind unumkehrbar, wohingegen sich andere noch begrenzen lassen.', 'Certains dégâts sont irréversibles, alors que d’autres peuvent encore être limités.', 'Some damage is irreversible, whereas other damage can still be limited.'),
      ], [
        FB(CHOOSE, 'Viele Menschen wollen nicht ＿ das Auto verzichten.', ['auf', 'von', 'über'], 'auf', ('Verzichten auf + accusatif.', 'Verzichten auf + accusative.'), ('Beaucoup de gens ne veulent pas renoncer à la voiture.', 'Many people do not want to do without the car.')),
        FB(COMPLETE, 'Wind und Sonne gehören zu den ＿ Energien.', ['erneuerbaren', 'unumkehrbaren', 'langfristigen'], 'erneuerbaren', ('Renouvelables : erneuerbar.', 'Renewable: erneuerbar.'), ('Le vent et le soleil font partie des énergies renouvelables.', 'Wind and sun are among the renewable energies.')),
        TF('Kurzfristig ist die Umstellung teuer, langfristig spart sie jedoch Kosten.', ('La transition coûte cher à long terme.', 'The switch is expensive in the long term.'), FAUX, ('Langfristig spart sie Kosten = à long terme, elle fait économiser.', 'Langfristig spart sie Kosten = in the long term it saves money.')),
        DC(ANSWER, [('Moderatorin', 'Reicht es, wenn jeder Einzelne weniger Energie verbraucht?')], ('Dans un débat, on te demande si les gestes individuels suffisent (concède, puis nuance).', 'In a debate, you are asked whether individual action is enough (concede, then qualify).'), ['So wichtig das auch ist, ohne politische Maßnahmen genügt es nicht.', 'So wichtig das auch ist, genügt es ohne politische Maßnahmen nicht.', 'Wenngleich wichtig das ist, es nicht genügt ohne Maßnahmen.'], 'So wichtig das auch ist, ohne politische Maßnahmen genügt es nicht.', ('So… auch ; la principale garde l’ordre normal.', 'So… auch; the main clause keeps normal order.')),
      ]),
  ])])

# ═════════════════════════ 5 : Particules modales, expressions imagées, registres ═════════════════════════
W5 = WORLD('goethec1-w5', ('La taverne du Cher Augustin', 'Dear Augustin’s tavern'), REGION,
  ('Saisir et employer les particules modales, comprendre les expressions imagées, adapter son registre.', 'Grasp and use modal particles, understand idioms, adapt your register.'),
  (('Le Cher Augustin', 'Dear Augustin'), '♨', ('Vienne, 1679 : la peste vide les rues, et le Cher Augustin chante encore dans sa taverne, cornemuse sous le bras. Avec lui, tout se joue dans les petits mots : doch, ja, halt, eben. Réponds-lui sur le même ton.', 'Vienna, 1679: the plague empties the streets, and Dear Augustin still sings in his tavern, bagpipes under his arm. With him, everything hangs on the little words: doch, ja, halt, eben. Answer him in the same tone.')),
  [CH('goethec1-w5-c1', ('Les petits mots', 'The little words'), [
    L('de-modalpartikeln', ('Les particules modales : doch, ja, eben, halt', 'Modal particles: doch, ja, eben, halt'), ('Donner à une phrase sa nuance affective avec la bonne particule.', 'Give a sentence its emotional nuance with the right particle.'), 9, [
        ('Ja rappelle ce que l’autre sait déjà : Du weißt ja, wie er ist. Doch contredit doucement ou insiste : Das habe ich dir doch gesagt! Komm doch mit! Eben et halt marquent la résignation : Das ist eben so. Dann gehen wir halt.', 'Ja recalls what the other person already knows: Du weißt ja, wie er ist. Doch gently contradicts or insists: Das habe ich dir doch gesagt! Komm doch mit! Eben and halt mark resignation: Das ist eben so. Dann gehen wir halt.'),
        ('Dans une question : denn exprime l’intérêt (Was machst du denn hier?), eigentlich change de sujet (Wie alt bist du eigentlich?), etwa attend un non (Hast du das etwa vergessen?), wohl exprime le doute (Ob er wohl kommt?).', 'In a question: denn expresses interest (Was machst du denn hier?), eigentlich changes the subject (Wie alt bist du eigentlich?), etwa expects a no (Hast du das etwa vergessen?), wohl expresses doubt (Ob er wohl kommt?).'),
        ('Dans un ordre : mal adoucit (Hör mal zu!), ruhig encourage (Nimm ruhig noch ein Stück!), bloß / ja menacent ou avertissent (Mach das bloß nicht! Komm ja nicht zu spät!), schon rassure (Das wird schon klappen).', 'In a command: mal softens (Hör mal zu!), ruhig encourages (Nimm ruhig noch ein Stück!), bloß / ja threaten or warn (Mach das bloß nicht! Komm ja nicht zu spät!), schon reassures (Das wird schon klappen).'),
      ], [
        DG('partikel-ja', 'ja (Partikel)', ('particule : tu le sais bien', 'particle: as you know')),
        DG('partikel-doch', 'doch (Partikel)', ('particule : mais si, donc (insistance)', 'particle: surely, do (insistence)')),
        DG('partikel-eben-halt', 'eben / halt', ('particules : c’est comme ça (résignation)', 'particles: that is just how it is (resignation)')),
        DG('partikel-etwa', 'etwa (in Fragen)', ('particule : par hasard (on espère que non)', 'particle: by any chance (hoping not)')),
        DG('partikel-ruhig', 'ruhig (Partikel)', ('particule : n’hésite pas à', 'particle: feel free to')),
        DG('partikel-bloss', 'bloß / ja (Warnung)', ('particules : surtout (avertissement)', 'particles: whatever you do (warning)')),
        DG('partikel-schon', 'schon (Partikel)', ('particule : ça ira bien (rassurer)', 'particle: it will be all right (reassuring)')),
        DG('partikel-wohl', 'wohl (Partikel)', ('particule : sans doute, je me demande', 'particle: I suppose, I wonder')),
      ], [
        x('„Alles ist hin“, sang Augustin, „aber das wird schon wieder!“', '« Tout est perdu, chantait Augustin, mais ça va bien finir par s’arranger ! »', '“All is lost,” sang Augustin, “but it will come right again!”'),
        x('Du willst doch nicht etwa nachts allein durch die Stadt gehen?', 'Tu ne veux tout de même pas traverser la ville seul en pleine nuit ?', 'You surely do not mean to walk through the city alone at night?'),
      ], [
        FB(CHOOSE, 'Das habe ich dir ＿ schon dreimal erklärt!', ['doch', 'etwa', 'ruhig'], 'doch', ('Reproche, insistance : doch.', 'Reproach, insistence: doch.'), ('Mais je te l’ai déjà expliqué trois fois !', 'But I have already explained that to you three times!')),
        FB(CHOOSE, 'Setzen Sie sich ＿, es dauert noch einen Moment.', ['ruhig', 'etwa', 'bloß'], 'ruhig', ('Encourager : ruhig.', 'Encouraging: ruhig.'), ('Asseyez-vous, je vous en prie, il y en a encore pour un moment.', 'Do sit down, it will take a moment longer.')),
        FB(CHOOSE, 'Hast du ＿ den Schlüssel verloren?', ['etwa', 'ruhig', 'halt'], 'etwa', ('On craint que oui : etwa.', 'Fearing the answer is yes: etwa.'), ('Tu n’aurais tout de même pas perdu la clé ?', 'You have not lost the key, have you?')),
        FB(CHOOSE, 'Der Zug ist weg. Dann nehmen wir ＿ den nächsten.', ['halt', 'etwa', 'denn'], 'halt', ('Résignation : halt / eben.', 'Resignation: halt / eben.'), ('Le train est parti. Eh bien, nous prendrons le suivant.', 'The train has gone. Then we will just take the next one.')),
      ]),
    L('de-redewendungen', ('Les expressions imagées', 'Idioms'), ('Comprendre et placer les tournures figurées du quotidien.', 'Understand and use everyday figurative expressions.'), 8, [
        ('Le corps : jemandem die Daumen drücken (croiser les doigts pour quelqu’un), die Nase voll haben (en avoir assez), auf die Nerven gehen (taper sur les nerfs), ein Auge zudrücken (fermer les yeux sur), sich etwas aus dem Kopf schlagen (s’ôter une idée de la tête).', 'The body: jemandem die Daumen drücken (to keep one’s fingers crossed for someone), die Nase voll haben (to be fed up), auf die Nerven gehen (to get on someone’s nerves), ein Auge zudrücken (to turn a blind eye), sich etwas aus dem Kopf schlagen (to put something out of one’s mind).'),
        ('La chance et l’échec : Schwein haben (avoir de la veine), ins Fettnäpfchen treten (mettre les pieds dans le plat), im Stich lassen (laisser tomber), den Faden verlieren (perdre le fil), etwas auf die lange Bank schieben (remettre à plus tard).', 'Luck and failure: Schwein haben (to be lucky), ins Fettnäpfchen treten (to put one’s foot in it), im Stich lassen (to leave in the lurch), den Faden verlieren (to lose the thread), etwas auf die lange Bank schieben (to put something off).'),
        ('Ces tournures sont figées : on ne change ni l’article ni le nom. Elles appartiennent au registre familier ; à l’écrit soutenu, on préfère le verbe simple (aufschieben au lieu de auf die lange Bank schieben).', 'These expressions are fixed: neither the article nor the noun changes. They belong to the informal register; in formal writing the simple verb is preferred (aufschieben instead of auf die lange Bank schieben).'),
      ], [
        D('daumen-druecken', 'jemandem die Daumen drücken', ('croiser les doigts pour quelqu’un', 'to keep one’s fingers crossed for someone')),
        D('nase-voll', 'die Nase voll haben', ('en avoir par-dessus la tête', 'to be sick and tired of it')),
        D('auf-die-nerven', 'jemandem auf die Nerven gehen', ('taper sur les nerfs de quelqu’un', 'to get on someone’s nerves')),
        D('auge-zudruecken', 'ein Auge zudrücken', ('fermer les yeux (sur une faute)', 'to turn a blind eye')),
        D('schwein-haben', 'Schwein haben', ('avoir de la veine', 'to be lucky (informal)')),
        D('fettnaepfchen', 'ins Fettnäpfchen treten', ('mettre les pieds dans le plat', 'to put one’s foot in it')),
        D('im-stich-lassen', 'im Stich lassen', ('laisser tomber, abandonner', 'to leave in the lurch')),
        D('lange-bank', 'auf die lange Bank schieben', ('remettre à plus tard', 'to put off')),
      ], [
        x('Augustin fiel betrunken in die Pestgrube und wachte gesund wieder auf: Da hat er wirklich Schwein gehabt.', 'Augustin tomba ivre dans la fosse aux pestiférés et se réveilla en bonne santé : il a vraiment eu de la veine.', 'Augustin fell drunk into the plague pit and woke up healthy: he really was lucky.'),
        x('Seine Freunde hatten ihn nicht im Stich gelassen, sie hatten ihn nur für tot gehalten.', 'Ses amis ne l’avaient pas laissé tomber, ils l’avaient seulement cru mort.', 'His friends had not left him in the lurch; they had only taken him for dead.'),
      ], [
        FB(COMPLETE, 'Morgen hast du deine Prüfung? Ich drücke dir die ＿!', ['Daumen', 'Nase', 'Augen'], 'Daumen', ('Die Daumen drücken.', 'Die Daumen drücken.'), ('Tu as ton examen demain ? Je croise les doigts pour toi !', 'Is your exam tomorrow? I will keep my fingers crossed for you!')),
        FB(COMPLETE, 'Seit drei Wochen regnet es. Ich habe die ＿ voll!', ['Nase', 'Daumen', 'Bank'], 'Nase', ('Die Nase voll haben.', 'Die Nase voll haben.'), ('Il pleut depuis trois semaines. J’en ai assez !', 'It has been raining for three weeks. I am fed up!')),
        TF('Der Lehrer hat heute ein Auge zugedrückt, als ich zu spät kam.', ('Le professeur m’a puni pour mon retard.', 'The teacher punished me for being late.'), FAUX, ('Ein Auge zudrücken = fermer les yeux, être indulgent.', 'Ein Auge zudrücken = to turn a blind eye, to be lenient.')),
        DC(ANSWER, [('Freund', 'Ich habe die Chefin gefragt, wann ihr Baby kommt. Sie ist gar nicht schwanger!')], ('Un ami te raconte sa gaffe (commente avec l’expression qui convient).', 'A friend tells you about his blunder (comment with the fitting idiom).'), ['Oje, da bist du ja richtig ins Fettnäpfchen getreten!', 'Oje, da hast du ja richtig Schwein gehabt!', 'Oje, da hast du ihr ja die Daumen gedrückt!'], 'Oje, da bist du ja richtig ins Fettnäpfchen getreten!', ('Faire une gaffe : ins Fettnäpfchen treten.', 'To make a blunder: ins Fettnäpfchen treten.')),
      ]),
  ]),
  CH('goethec1-w5-c2', ('Parler à chacun', 'Speaking to everyone'), [
    L('de-register', ('Les registres : familier, courant, soutenu', 'Registers: informal, neutral, formal'), ('Reconnaître le niveau de langue et le changer selon la situation.', 'Recognise the level of language and change it to suit the situation.'), 8, [
        ('Un même sens, trois registres : kriegen (familier) / bekommen (courant) / erhalten (soutenu) ; gucken / sehen / betrachten ; kaputt / defekt / beschädigt ; Job / Arbeit / Tätigkeit ; klappen / gelingen.', 'One meaning, three registers: kriegen (informal) / bekommen (neutral) / erhalten (formal); gucken / sehen / betrachten; kaputt / defekt / beschädigt; Job / Arbeit / Tätigkeit; klappen / gelingen.'),
        ('À l’oral familier : contractions (’ne, ’s, hab’), particules, was pour etwas, mots courts (Uni, Abi, Azubi). À l’écrit soutenu : style nominal, passif, génitif, connecteurs (folglich, zudem, hingegen).', 'In informal speech: contractions (’ne, ’s, hab’), particles, was for etwas, short words (Uni, Abi, Azubi). In formal writing: nominal style, passive, genitive, connectors (folglich, zudem, hingegen).'),
        ('Atténuer : Ich würde meinen, dass… ; Es scheint mir, als… ; Wenn ich mich nicht irre… ; Dürfte ich Sie bitten, …? Renforcer : zweifellos (sans aucun doute), keineswegs (nullement), durchaus (tout à fait).', 'Softening: Ich würde meinen, dass… ; Es scheint mir, als… ; Wenn ich mich nicht irre… ; Dürfte ich Sie bitten, …? Strengthening: zweifellos (undoubtedly), keineswegs (by no means), durchaus (absolutely).'),
      ], [
        D('erhalten', 'erhalten', ('recevoir (soutenu)', 'to receive (formal)')),
        D('kriegen', 'kriegen', ('recevoir, avoir (familier)', 'to get (informal)')),
        D('taetigkeit', 'die Tätigkeit', ('l’activité (professionnelle)', 'the occupation, the activity')),
        D('gelingen', 'gelingen', ('réussir (à quelqu’un)', 'to succeed, to work out')),
        D('klappen', 'klappen', ('marcher, fonctionner (familier)', 'to work out (informal)')),
        D('zweifellos', 'zweifellos', ('sans aucun doute', 'undoubtedly')),
        D('keineswegs', 'keineswegs', ('nullement, en aucun cas', 'by no means')),
        D('durchaus', 'durchaus', ('tout à fait, parfaitement', 'absolutely, perfectly')),
      ], [
        x('Unter Freunden sagt man: „Hat’s geklappt?“ Im Bericht schreibt man: „Der Versuch ist gelungen.“', 'Entre amis, on dit : « Ça a marché ? » Dans un rapport, on écrit : « L’expérience a réussi. »', 'Among friends you say: “Did it work?” In a report you write: “The experiment succeeded.”'),
        x('Das ist keineswegs sicher, aber durchaus möglich.', 'Ce n’est nullement certain, mais tout à fait possible.', 'That is by no means certain, but perfectly possible.'),
      ], [
        FB(CHOOSE, 'In einem formellen Brief: „Wir haben Ihr Schreiben vom 3. Mai ＿.“', ['erhalten', 'gekriegt', 'geguckt'], 'erhalten', ('Registre soutenu : erhalten.', 'Formal register: erhalten.'), ('Dans une lettre formelle : « Nous avons bien reçu votre courrier du 3 mai. »', 'In a formal letter: “We have received your letter of 3 May.”')),
        FB(CHOOSE, 'Zu einem Freund: „Und, hat alles ＿?“', ['geklappt', 'gelungen', 'erhalten'], 'geklappt', ('Registre familier, avec haben : geklappt.', 'Informal register, with haben: geklappt.'), ('À un ami : « Alors, tout a marché ? »', 'To a friend: “So, did everything work out?”')),
        FB(CHOOSE, 'Das Experiment ist uns leider nicht ＿.', ['gelungen', 'geklappt', 'gekriegt'], 'gelungen', ('Avec sein et un datif : gelingen.', 'With sein and a dative: gelingen.'), ('Malheureusement, nous n’avons pas réussi l’expérience.', 'Unfortunately, we did not succeed with the experiment.')),
        TF('Der Vorschlag ist durchaus vernünftig.', ('La proposition est jugée déraisonnable.', 'The proposal is judged unreasonable.'), FAUX, ('Durchaus = tout à fait.', 'Durchaus = absolutely.')),
      ]),
  ])])

# ═════════════════════════ 6 : Passif complexe, formation des mots, éthique ═════════════════════════
W6 = WORLD('goethec1-w6', ('Le grenier du Golem', 'The Golem’s attic'), REGION,
  ('Maîtriser le passif avec verbe de modalité aux temps composés, comprendre la formation des mots, débattre d’éthique et de progrès.', 'Master the passive with a modal verb in compound tenses, understand word formation, debate ethics and progress.'),
  (('Le Golem', 'The Golem'), '⚒', ('À Prague, sous les toits de la vieille synagogue, le Golem d’argile attend qu’on lui dise ce qui aurait dû être fait. Démonte les mots préfixe par préfixe, et tu trouveras celui qui l’arrête.', 'In Prague, under the roof of the old synagogue, the clay Golem waits to be told what should have been done. Take the words apart prefix by prefix, and you will find the one that stops him.')),
  [CH('goethec1-w6-c1', ('Ce qui aurait dû être fait', 'What should have been done'), [
    L('de-passiv-c1', ('Le passif complexe : hätte gemacht werden müssen', 'The complex passive: hätte gemacht werden müssen'), ('Combiner passif, verbe de modalité et temps composés.', 'Combine the passive, a modal verb and compound tenses.'), 10, [
        ('Passif + modal au parfait : hat + participe + werden + modal à l’infinitif. Der Golem hat aufgehalten werden müssen. À l’irréel du passé : Er hätte früher aufgehalten werden müssen (il aurait fallu l’arrêter plus tôt).', 'Passive + modal in the perfect: hat + participle + werden + modal in the infinitive. Der Golem hat aufgehalten werden müssen. In the unreal past: Er hätte früher aufgehalten werden müssen (he should have been stopped earlier).'),
        ('Dans une subordonnée, l’auxiliaire conjugué se place avant le groupe verbal : …, weil er früher hätte aufgehalten werden müssen. C’est la seule exception à la règle du verbe final.', 'In a subordinate clause, the conjugated auxiliary goes before the verb group: …, weil er früher hätte aufgehalten werden müssen. This is the only exception to the verb-final rule.'),
        ('Passif du destinataire avec bekommen / erhalten + participe : Er bekam das Wort auf die Stirn geschrieben (on lui écrivit le mot sur le front). Passif impersonnel : Es wurde lange diskutiert. Hier wird nicht geraucht.', 'Recipient passive with bekommen / erhalten + participle: Er bekam das Wort auf die Stirn geschrieben (he had the word written on his forehead). Impersonal passive: Es wurde lange diskutiert. Hier wird nicht geraucht.'),
      ], [
        DG('passiv-modal-perfekt', 'hat … gemacht werden müssen', ('passif avec modal au parfait', 'passive with a modal in the perfect')),
        DG('passiv-modal-konj2', 'hätte … gemacht werden müssen', ('il aurait fallu que ce soit fait', 'should have been done')),
        DG('passiv-nebensatz', '…, weil es hätte gemacht werden müssen', ('auxiliaire avant le groupe verbal en subordonnée', 'auxiliary before the verb group in a subordinate clause')),
        DG('bekommen-passiv', 'bekommen / erhalten + Partizip II', ('passif du destinataire', 'recipient passive')),
        DG('unpersoenliches-passiv', 'Es wurde lange diskutiert.', ('passif impersonnel (sans sujet)', 'impersonal passive (no subject)')),
        D('lehm', 'der Lehm', ('l’argile, la glaise', 'clay')),
        D('stirn', 'die Stirn', ('le front', 'the forehead')),
        D('erschaffen', 'erschaffen', ('créer', 'to create')),
        D('verhindern', 'verhindern', ('empêcher', 'to prevent, to stop from happening')),
      ], [
        x('Das Unglück hätte verhindert werden können, wenn der Rabbi das Wort rechtzeitig entfernt hätte.', 'Le malheur aurait pu être évité si le rabbin avait retiré le mot à temps.', 'The disaster could have been prevented if the rabbi had removed the word in time.'),
        x('Der Golem bekam jeden Freitag das Zeichen von der Stirn genommen.', 'Chaque vendredi, on retirait le signe du front du Golem.', 'Every Friday the Golem had the sign taken from his forehead.'),
      ], [
        FB(CHOOSE, 'Der Fehler hätte früher bemerkt werden ＿.', ['müssen', 'gemusst', 'muss'], 'müssen', ('Double infinitif : werden müssen.', 'Double infinitive: werden müssen.'), ('L’erreur aurait dû être remarquée plus tôt.', 'The mistake should have been noticed earlier.')),
        FB(CHOOSE, 'Ich weiß, dass das Gebäude ＿ renoviert werden sollen.', ['hätte', 'wäre', 'würde'], 'hätte', ('En subordonnée, hätte précède le groupe verbal.', 'In a subordinate clause, hätte precedes the verb group.'), ('Je sais que le bâtiment aurait dû être rénové.', 'I know that the building should have been renovated.')),
        FB(CHOOSE, 'Zum Geburtstag ＿ sie ein Fahrrad geschenkt.', ['bekam', 'wurde', 'war'], 'bekam', ('Passif du destinataire : bekam… geschenkt.', 'Recipient passive: bekam… geschenkt.'), ('Pour son anniversaire, on lui a offert un vélo.', 'For her birthday she was given a bicycle.')),
        order(('Remets dans l’ordre : « La décision aurait pu être mieux expliquée. »', 'Put in order: “The decision could have been explained better.”'), ['Die', 'Entscheidung', 'hätte', 'besser', 'erklärt', 'werden', 'können.'], ('Hätte en 2e position ; participe + werden + können à la fin.', 'Hätte in second position; participle + werden + können at the end.')),
      ]),
    L('de-wortbildung', ('La formation des mots : ver-, zer-, ent-, miss-', 'Word formation: ver-, zer-, ent-, miss-'), ('Deviner le sens d’un mot grâce à ses préfixes et suffixes.', 'Work out the meaning of a word from its prefixes and suffixes.'), 9, [
        ('Préfixes inséparables : zer- (mettre en morceaux : zerbrechen, zerstören), ent- (ôter, s’éloigner : entfernen, entkommen), miss- (mal : missverstehen, misslingen), ver- (erreur ou transformation : sich verlaufen, verbessern), er- (résultat : erreichen, erfinden).', 'Inseparable prefixes: zer- (into pieces: zerbrechen, zerstören), ent- (removing, moving away: entfernen, entkommen), miss- (wrongly: missverstehen, misslingen), ver- (error or change: sich verlaufen, verbessern), er- (result: erreichen, erfinden).'),
        ('Suffixes d’adjectifs : -los (sans : hilflos, sinnlos), -haft (qui a l’allure de : fehlerhaft, dauerhaft), -mäßig (conforme à : regelmäßig, planmäßig), -sam (enclin à : sparsam, schweigsam), -wert / -würdig (digne de : sehenswert, glaubwürdig).', 'Adjective suffixes: -los (without: hilflos, sinnlos), -haft (having the nature of: fehlerhaft, dauerhaft), -mäßig (in accordance with: regelmäßig, planmäßig), -sam (inclined to: sparsam, schweigsam), -wert / -würdig (worthy of: sehenswert, glaubwürdig).'),
        ('Composés : le dernier élément donne le genre et le sens de base, les précédents le précisent. Die Lebensmittelverschwendung = das Verschwenden von Lebensmitteln. Un -s- ou -n- de liaison est fréquent : Arbeitszeit, Sonnenschein.', 'Compounds: the last element gives the gender and basic meaning, the earlier ones specify it. Die Lebensmittelverschwendung = das Verschwenden von Lebensmitteln. A linking -s- or -n- is common: Arbeitszeit, Sonnenschein.'),
      ], [
        DG('praefix-zer', 'zer- (zerbrechen, zerstören)', ('préfixe zer- : mettre en pièces', 'prefix zer-: into pieces')),
        DG('praefix-ent', 'ent- (entfernen, entkommen)', ('préfixe ent- : ôter, s’éloigner', 'prefix ent-: removing, moving away')),
        DG('praefix-miss', 'miss- (missverstehen, misslingen)', ('préfixe miss- : mal, de travers', 'prefix miss-: wrongly')),
        DG('suffix-los', '-los (hilflos, sinnlos)', ('suffixe -los : sans', 'suffix -los: without')),
        DG('suffix-haft', '-haft (fehlerhaft, dauerhaft)', ('suffixe -haft : qui a le caractère de', 'suffix -haft: having the nature of')),
        D('entfernen', 'entfernen', ('enlever, retirer', 'to remove')),
        D('misslingen', 'misslingen', ('échouer, rater', 'to fail, to go wrong')),
        D('zerfallen', 'zerfallen', ('tomber en poussière, se désagréger', 'to crumble, to fall apart')),
        D('sinnlos', 'sinnlos', ('absurde, vain', 'pointless, senseless')),
      ], [
        x('Als der Rabbi den ersten Buchstaben entfernte, zerfiel der Golem zu Staub.', 'Quand le rabbin retira la première lettre, le Golem tomba en poussière.', 'When the rabbi removed the first letter, the Golem crumbled to dust.'),
        x('Jeder Versuch, ihn mit Gewalt aufzuhalten, war misslungen und schien sinnlos.', 'Toute tentative de l’arrêter par la force avait échoué et semblait vaine.', 'Every attempt to stop him by force had failed and seemed pointless.'),
      ], [
        FB(CHOOSE, 'Das Glas ist auf den Boden gefallen und ＿.', ['zerbrochen', 'entbrochen', 'verbrochen'], 'zerbrochen', ('En morceaux : zer-.', 'Into pieces: zer-.'), ('Le verre est tombé par terre et s’est brisé.', 'The glass fell on the floor and shattered.')),
        FB(CHOOSE, 'Entschuldigung, ich habe Sie ＿. Können Sie das wiederholen?', ['missverstanden', 'zerverstanden', 'entverstanden'], 'missverstanden', ('Mal comprendre : miss-.', 'To misunderstand: miss-.'), ('Excusez-moi, je vous ai mal compris. Pouvez-vous répéter ?', 'Sorry, I misunderstood you. Could you repeat that?')),
        FB(CHOOSE, 'Ohne Karte und Handy fühlte sie sich völlig ＿.', ['hilflos', 'hilfhaft', 'hilfsam'], 'hilflos', ('Sans aide : -los.', 'Without help: -los.'), ('Sans carte ni téléphone, elle se sentait complètement désemparée.', 'Without a map or phone, she felt completely helpless.')),
        TF('Die Rechnung war fehlerhaft und musste korrigiert werden.', ('La facture était correcte.', 'The bill was correct.'), FAUX, ('Fehlerhaft = qui contient des erreurs.', 'Fehlerhaft = containing errors.')),
      ]),
  ]),
  CH('goethec1-w6-c2', ('La créature et son maître', 'The creature and its master'), [
    L('de-ethik', ('L’éthique et le progrès', 'Ethics and progress'), ('Débattre des limites de la science et de la responsabilité.', 'Debate the limits of science and responsibility.'), 8, [
        ('Les notions : die Ethik, die Würde (la dignité), das Gewissen (la conscience morale), die Pflicht (le devoir), die Freiheit, der Fortschritt (le progrès), die Grenze (la limite), der Grundsatz (le principe).', 'The concepts: die Ethik, die Würde (dignity), das Gewissen (conscience), die Pflicht (duty), die Freiheit, der Fortschritt (progress), die Grenze (the limit), der Grundsatz (the principle).'),
        ('Juger : vertretbar (défendable), verwerflich (condamnable), fragwürdig (contestable), etwas rechtfertigen (justifier), abwägen (peser), verantworten (répondre de), missbrauchen (abuser de).', 'Judging: vertretbar (defensible), verwerflich (reprehensible), fragwürdig (questionable), etwas rechtfertigen (to justify), abwägen (to weigh up), verantworten (to answer for), missbrauchen (to misuse).'),
        ('Formules de débat : Es stellt sich die Frage, inwieweit… (dans quelle mesure). Der Zweck heiligt nicht die Mittel (la fin ne justifie pas les moyens). Man muss Nutzen und Risiken gegeneinander abwägen.', 'Debate phrases: Es stellt sich die Frage, inwieweit… (to what extent). Der Zweck heiligt nicht die Mittel (the end does not justify the means). Man muss Nutzen und Risiken gegeneinander abwägen.'),
      ], [
        D('gewissen', 'das Gewissen', ('la conscience (morale)', 'conscience')),
        D('wuerde', 'die Würde', ('la dignité', 'dignity')),
        D('fortschritt', 'der Fortschritt', ('le progrès', 'progress')),
        D('vertretbar', 'vertretbar', ('défendable, acceptable', 'defensible, justifiable')),
        D('fragwuerdig', 'fragwürdig', ('contestable, douteux', 'questionable')),
        D('rechtfertigen', 'rechtfertigen', ('justifier', 'to justify')),
        D('abwaegen', 'abwägen', ('peser, soupeser', 'to weigh up')),
        D('missbrauchen', 'missbrauchen', ('abuser de, détourner', 'to misuse, to abuse')),
        D('inwieweit', 'inwieweit', ('dans quelle mesure', 'to what extent')),
      ], [
        x('Es stellt sich die Frage, inwieweit der Mensch erschaffen darf, was er nicht beherrschen kann.', 'La question se pose de savoir dans quelle mesure l’homme a le droit de créer ce qu’il ne peut pas maîtriser.', 'The question arises to what extent humans may create what they cannot control.'),
        x('Auch ein guter Zweck rechtfertigt nicht jedes Mittel.', 'Même un but louable ne justifie pas tous les moyens.', 'Even a good end does not justify every means.'),
      ], [
        FB(COMPLETE, 'Bei dieser Entscheidung muss man Nutzen und Risiken sorgfältig ＿.', ['abwägen', 'missbrauchen', 'rechtfertigen'], 'abwägen', ('Peser : abwägen.', 'To weigh up: abwägen.'), ('Pour cette décision, il faut peser soigneusement avantages et risques.', 'In this decision, benefits and risks must be weighed up carefully.')),
        FB(COMPLETE, 'Ich konnte nicht lügen: Mein ＿ hat es nicht erlaubt.', ['Gewissen', 'Fortschritt', 'Grundsatz'], 'Gewissen', ('La conscience morale : das Gewissen.', 'Conscience: das Gewissen.'), ('Je n’ai pas pu mentir : ma conscience ne me l’a pas permis.', 'I could not lie: my conscience would not allow it.')),
        TF('Viele halten die Methode für fragwürdig, auch wenn sie legal ist.', ('La méthode fait l’unanimité.', 'Everyone approves of the method.'), FAUX, ('Fragwürdig = contestable.', 'Fragwürdig = questionable.')),
        DC(ANSWER, [('Professorin', 'Darf die Forschung alles, was technisch möglich ist?')], ('En séminaire, on te demande si la recherche peut tout se permettre (réponds que non, avec nuance).', 'In a seminar, you are asked whether research may do anything (answer no, with nuance).'), ['Meines Erachtens nicht: Nicht alles, was machbar ist, ist auch vertretbar.', 'Meines Erachtens nicht: Nicht alles, was machbar ist, ist auch missbraucht.', 'Meiner Erachtens nach nicht: Alles machbar ist fragwürdig vertretbar.'], 'Meines Erachtens nicht: Nicht alles, was machbar ist, ist auch vertretbar.', ('Meines Erachtens ; vertretbar = défendable.', 'Meines Erachtens; vertretbar = defensible.')),
      ]),
  ])])

# ═════════════════════════ 7 : Rections, prépositions soutenues, la culture ═════════════════════════
W7 = WORLD('goethec1-w7', ('Le mont de Vénus', 'The Venusberg'), REGION,
  ('Employer la bonne préposition après un nom ou un adjectif, comprendre les prépositions de la langue officielle, parler d’art et de culture.', 'Use the right preposition after a noun or adjective, understand the prepositions of official German, talk about art and culture.'),
  (('Dame Vénus', 'Lady Venus'), '❀', ('Le chevalier-poète Tannhäuser est entré dans la montagne, et Dame Vénus ne laisse repartir que ceux qui chantent juste. Ici, chaque nom réclame sa préposition : un seul faux accord, et la porte reste close.', 'The knight-poet Tannhäuser has entered the mountain, and Lady Venus lets only those who sing true leave again. Here every noun demands its preposition: one wrong link, and the door stays shut.')),
  [CH('goethec1-w7-c1', ('Chaque nom sa préposition', 'Every noun its preposition'), [
    L('de-rektion', ('Noms et adjectifs à préposition', 'Nouns and adjectives with prepositions'), ('Associer un nom ou un adjectif à sa préposition fixe.', 'Pair a noun or adjective with its fixed preposition.'), 9, [
        ('Adjectifs : angewiesen auf + accusatif (tributaire de), stolz auf, neugierig auf, abhängig von, begeistert von, überzeugt von, zuständig für (compétent pour), bekannt für, fähig zu, bereit zu, interessiert an + datif, reich an, arm an.', 'Adjectives: angewiesen auf + accusative (reliant on), stolz auf, neugierig auf, abhängig von, begeistert von, überzeugt von, zuständig für (responsible for), bekannt für, fähig zu, bereit zu, interessiert an + dative, reich an, arm an.'),
        ('Noms : der Bedarf an + datif (le besoin en), der Mangel an (le manque de), das Interesse an, die Teilnahme an ; der Anspruch auf + accusatif (le droit à), der Einfluss auf, die Hoffnung auf ; die Sehnsucht nach (la nostalgie de), die Nachfrage nach ; die Angst vor.', 'Nouns: der Bedarf an + dative (the need for), der Mangel an (the lack of), das Interesse an, die Teilnahme an; der Anspruch auf + accusative (the entitlement to), der Einfluss auf, die Hoffnung auf; die Sehnsucht nach (the longing for), die Nachfrage nach; die Angst vor.'),
        ('Le nom garde en général la préposition du verbe : sich interessieren für → mais das Interesse an ; hoffen auf → die Hoffnung auf ; sich sehnen nach → die Sehnsucht nach. Avec une subordonnée : darauf, dass… ; daran, zu…', 'The noun usually keeps the verb’s preposition: sich interessieren für → but das Interesse an; hoffen auf → die Hoffnung auf; sich sehnen nach → die Sehnsucht nach. With a clause: darauf, dass… ; daran, zu…'),
      ], [
        D('angewiesen', 'angewiesen sein auf', ('être tributaire de, dépendre de', 'to be reliant on')),
        D('zustaendig', 'zuständig für', ('compétent pour, chargé de', 'responsible for, in charge of')),
        D('bereit-zu', 'bereit zu', ('prêt à', 'ready to, willing to')),
        D('bedarf', 'der Bedarf an', ('le besoin en', 'the need for, the demand for')),
        D('mangel', 'der Mangel an', ('le manque de, la pénurie de', 'the lack of, the shortage of')),
        D('anspruch', 'der Anspruch auf', ('le droit à, la prétention à', 'the entitlement to, the claim to')),
        D('sehnsucht', 'die Sehnsucht nach', ('la nostalgie de, le désir ardent de', 'the longing for')),
        D('reich-an', 'reich an', ('riche en', 'rich in')),
        D('begeistert-von', 'begeistert von', ('enthousiasmé par', 'enthusiastic about')),
      ], [
        x('Nach einem Jahr im Venusberg ergriff Tannhäuser die Sehnsucht nach der Welt der Menschen.', 'Après un an au mont de Vénus, Tannhäuser fut saisi par la nostalgie du monde des hommes.', 'After a year in the Venusberg, Tannhäuser was seized by longing for the world of men.'),
        x('Er war auf die Gnade des Papstes angewiesen, hatte aber wenig Hoffnung auf Vergebung.', 'Il dépendait de la grâce du pape, mais avait peu d’espoir d’être pardonné.', 'He was reliant on the Pope’s mercy but had little hope of forgiveness.'),
      ], [
        FB(CHOOSE, 'Viele Studierende sind ＿ finanzielle Hilfe angewiesen.', ['auf', 'von', 'an'], 'auf', ('Angewiesen auf + accusatif.', 'Angewiesen auf + accusative.'), ('Beaucoup d’étudiants dépendent d’une aide financière.', 'Many students are reliant on financial support.')),
        FB(CHOOSE, 'In der Pflege herrscht ein großer Mangel ＿ Fachkräften.', ['an', 'von', 'für'], 'an', ('Der Mangel an + datif.', 'Der Mangel an + dative.'), ('Dans les soins, il y a une grande pénurie de personnel qualifié.', 'In nursing there is a great shortage of skilled staff.')),
        FB(CHOOSE, 'Jeder Arbeitnehmer hat Anspruch ＿ bezahlten Urlaub.', ['auf', 'an', 'für'], 'auf', ('Der Anspruch auf + accusatif.', 'Der Anspruch auf + accusative.'), ('Chaque salarié a droit à des congés payés.', 'Every employee is entitled to paid leave.')),
        FB(CHOOSE, 'Wer ist hier ＿ die Anmeldung zuständig?', ['für', 'auf', 'zu'], 'für', ('Zuständig für.', 'Zuständig für.'), ('Qui est chargé des inscriptions ici ?', 'Who is responsible for registration here?')),
      ]),
    L('de-praep-c1', ('Les prépositions officielles : gemäß, zugunsten, anlässlich', 'Official prepositions: gemäß, zugunsten, anlässlich'), ('Comprendre et employer les prépositions des textes administratifs.', 'Understand and use the prepositions of administrative texts.'), 8, [
        ('Avec le datif : gemäß (conformément à), entsprechend (selon, en fonction de), zufolge (d’après, placé après le nom), entgegen (contrairement à), samt (avec, y compris). Gemäß Paragraf 5… Entgegen allen Erwartungen…', 'With the dative: gemäß (in accordance with), entsprechend (according to), zufolge (according to, placed after the noun), entgegen (contrary to), samt (together with). Gemäß Paragraf 5… Entgegen allen Erwartungen…'),
        ('Avec le génitif : anlässlich (à l’occasion de), zugunsten (en faveur de), mangels (faute de), kraft (en vertu de), seitens (de la part de), einschließlich (y compris), abzüglich (déduction faite de), binnen (dans un délai de).', 'With the genitive: anlässlich (on the occasion of), zugunsten (in favour of), mangels (for lack of), kraft (by virtue of), seitens (on the part of), einschließlich (including), abzüglich (less), binnen (within).'),
        ('Ces prépositions appartiennent à la langue officielle. À l’oral, on dit plutôt : nach (gemäß), wegen (aufgrund), für (zugunsten), weil… fehlt (mangels), mit (samt).', 'These prepositions belong to official language. In speech people tend to say: nach (gemäß), wegen (aufgrund), für (zugunsten), weil… fehlt (mangels), mit (samt).'),
      ], [
        DG('gemaess', 'gemäß + Dativ', ('conformément à', 'in accordance with')),
        DG('entgegen', 'entgegen + Dativ', ('contrairement à', 'contrary to')),
        DG('anlaesslich', 'anlässlich + Genitiv', ('à l’occasion de', 'on the occasion of')),
        DG('zugunsten', 'zugunsten + Genitiv', ('en faveur de, au profit de', 'in favour of, for the benefit of')),
        DG('mangels', 'mangels + Genitiv', ('faute de', 'for lack of')),
        DG('kraft', 'kraft + Genitiv', ('en vertu de', 'by virtue of')),
        DG('seitens', 'seitens + Genitiv', ('de la part de', 'on the part of')),
        DG('einschliesslich', 'einschließlich + Genitiv', ('y compris', 'including')),
      ], [
        x('Entgegen allen Erwartungen begann der trockene Stab des Papstes zu blühen.', 'Contre toute attente, le bâton desséché du pape se mit à fleurir.', 'Contrary to all expectations, the Pope’s dry staff began to blossom.'),
        x('Anlässlich des Sängerfestes kamen Dichter aus dem ganzen Land auf die Wartburg.', 'À l’occasion du concours de chant, des poètes de tout le pays vinrent à la Wartburg.', 'On the occasion of the song contest, poets from all over the land came to the Wartburg.'),
      ], [
        FB(CHOOSE, '＿ Beweisen wurde der Angeklagte freigesprochen.', ['Mangels', 'Anlässlich', 'Zugunsten'], 'Mangels', ('Faute de : mangels.', 'For lack of: mangels.'), ('Faute de preuves, l’accusé a été acquitté.', 'For lack of evidence, the accused was acquitted.')),
        FB(CHOOSE, '＿ des Jubiläums findet ein Konzert statt.', ['Anlässlich', 'Mangels', 'Entgegen'], 'Anlässlich', ('À l’occasion de : anlässlich.', 'On the occasion of: anlässlich.'), ('À l’occasion de l’anniversaire, un concert est organisé.', 'On the occasion of the anniversary, a concert is being held.')),
        FB(CHOOSE, 'Entgegen ＿ ist der Umsatz gestiegen.', ['der Prognose', 'die Prognose', 'des Prognose'], 'der Prognose', ('Entgegen + datif.', 'Entgegen + dative.'), ('Contrairement aux prévisions, le chiffre d’affaires a augmenté.', 'Contrary to the forecast, turnover has risen.')),
        FB(CHOOSE, 'Die Spenden werden ＿ der Flutopfer gesammelt.', ['zugunsten', 'mangels', 'kraft'], 'zugunsten', ('Au profit de : zugunsten.', 'For the benefit of: zugunsten.'), ('Les dons sont collectés au profit des victimes des inondations.', 'Donations are being collected for the flood victims.')),
      ]),
  ]),
  CH('goethec1-w7-c2', ('Le concours des chanteurs', 'The singers’ contest'), [
    L('de-kultur', ('L’art et la culture', 'Art and culture'), ('Parler d’une œuvre, d’une mise en scène et de sa réception.', 'Talk about a work, a production and its reception.'), 8, [
        ('Les œuvres : das Werk (l’œuvre), das Gemälde (le tableau), die Ausstellung, die Aufführung (la représentation), die Inszenierung (la mise en scène), die Uraufführung (la première mondiale), das Bühnenbild (le décor), die Oper.', 'Works: das Werk (the work), das Gemälde (the painting), die Ausstellung, die Aufführung (the performance), die Inszenierung (the production), die Uraufführung (the world premiere), das Bühnenbild (the set), die Oper.'),
        ('Créer et interpréter : entwerfen (concevoir), vertonen (mettre en musique), darstellen (représenter, interpréter), deuten (interpréter, expliquer), anspielen auf (faire allusion à), prägen (marquer).', 'Creating and interpreting: entwerfen (to design), vertonen (to set to music), darstellen (to portray), deuten (to interpret), anspielen auf (to allude to), prägen (to shape, to leave a mark on).'),
        ('Critiquer : gelungen (réussi), ergreifend (poignant), eindrucksvoll (impressionnant), langatmig (qui traîne en longueur), umstritten (controversé), die Kritik fiel begeistert / vernichtend aus (la critique fut enthousiaste / assassine).', 'Reviewing: gelungen (successful), ergreifend (moving), eindrucksvoll (impressive), langatmig (long-winded), umstritten (controversial), die Kritik fiel begeistert / vernichtend aus (the reviews were enthusiastic / scathing).'),
      ], [
        D('werk', 'das Werk', ('l’œuvre', 'the work (of art)')),
        D('auffuehrung', 'die Aufführung', ('la représentation', 'the performance')),
        D('inszenierung', 'die Inszenierung', ('la mise en scène', 'the production, the staging')),
        D('darstellen', 'darstellen', ('représenter, interpréter', 'to portray, to depict')),
        D('deuten', 'deuten', ('interpréter, expliquer', 'to interpret')),
        D('praegen', 'prägen', ('marquer, façonner', 'to shape, to leave a mark on')),
        D('ergreifend', 'ergreifend', ('poignant, émouvant', 'moving, gripping')),
        D('umstritten', 'umstritten', ('controversé', 'controversial')),
        D('langatmig', 'langatmig', ('qui traîne en longueur', 'long-winded')),
      ], [
        x('Wagners Oper hat das Bild des Tannhäuser bis heute geprägt.', 'L’opéra de Wagner a marqué jusqu’à aujourd’hui l’image de Tannhäuser.', 'Wagner’s opera has shaped the image of Tannhäuser to this day.'),
        x('Die neue Inszenierung ist umstritten: Die einen finden sie ergreifend, die anderen langatmig.', 'La nouvelle mise en scène est controversée : les uns la trouvent poignante, les autres trop longue.', 'The new production is controversial: some find it moving, others long-winded.'),
      ], [
        FB(COMPLETE, 'Die ＿ des Stücks dauerte vier Stunden, aber niemand ging früher.', ['Aufführung', 'Ausstellung', 'Schlagzeile'], 'Aufführung', ('La représentation : die Aufführung.', 'The performance: die Aufführung.'), ('La représentation de la pièce a duré quatre heures, mais personne n’est parti avant la fin.', 'The performance of the play lasted four hours, but nobody left early.')),
        FB(CHOOSE, 'Der Titel spielt ＿ ein berühmtes Gedicht an.', ['auf', 'an', 'zu'], 'auf', ('Anspielen auf + accusatif.', 'Anspielen auf + accusative.'), ('Le titre fait allusion à un poème célèbre.', 'The title alludes to a famous poem.')),
        TF('Die Kritik fiel vernichtend aus.', ('Les critiques ont adoré le spectacle.', 'The critics loved the show.'), FAUX, ('Vernichtend = assassine, très négative.', 'Vernichtend = scathing, very negative.')),
        DC(ANSWER, [('Bekannte', 'Wie hat Ihnen die Ausstellung gefallen?')], ('Une connaissance te demande ton avis sur une exposition (tu l’as trouvée impressionnante, mais un peu longue).', 'An acquaintance asks your view of an exhibition (you found it impressive but a little long).'), ['Eindrucksvoll, wenngleich stellenweise etwas langatmig.', 'Eindrucksvoll, wenngleich stellenweise etwas umstritten an.', 'Ergreifend auf, geschweige denn langatmig.'], 'Eindrucksvoll, wenngleich stellenweise etwas langatmig.', ('Wenngleich + adjectif : concession.', 'Wenngleich + adjective: concession.')),
      ]),
  ])])

# ═════════════════════════ 8 : Cohésion du texte, écrit universitaire, université ═════════════════════════
W8 = WORLD('goethec1-w8', ('La rive du Chevalier au cygne', 'The Swan Knight’s shore'), REGION,
  ('Assurer la cohésion d’un texte par les mots de reprise, rédiger un résumé et commenter un graphique, parler d’études et de recherche.', 'Make a text cohesive with reference words, write a summary and comment on a chart, talk about studies and research.'),
  (('Le Chevalier au cygne', 'The Swan Knight'), '⚜', ('Une nacelle tirée par un cygne accoste au bord du fleuve : le Chevalier au cygne défend la duchesse, à condition qu’on ne lui demande jamais son nom. Renvoie à ce qui a été dit sans le répéter, résume sans trahir, et il restera.', 'A boat drawn by a swan lands on the river bank: the Swan Knight defends the duchess, provided he is never asked his name. Refer to what has been said without repeating it, summarise without betraying, and he will stay.')),
  [CH('goethec1-w8-c1', ('Sans jamais répéter', 'Without ever repeating'), [
    L('de-textkohaesion', ('Les mots de reprise : dieser, letzterer, hierbei', 'Reference words: dieser, letzterer, hierbei'), ('Relier les phrases d’un texte sans répéter les noms.', 'Link the sentences of a text without repeating nouns.'), 9, [
        ('Reprendre un nom : dieser / jener (celui-ci / celui-là), ersterer… letzterer (le premier… le second), derselbe (le même), solch ein (un tel), der Genannte. Der Ritter und der Herzog stritten; letzterer verlor.', 'Referring back to a noun: dieser / jener (this one / that one), ersterer… letzterer (the former… the latter), derselbe (the same), solch ein (such a), der Genannte. Der Ritter und der Herzog stritten; letzterer verlor.'),
        ('Reprendre une phrase entière : das / dies (cela), was (ce qui) : Er verschwieg seinen Namen, was alle wunderte. Adverbes pronominaux : dabei / hierbei (ce faisant), dadurch, daraus, demzufolge (par conséquent), diesbezüglich (à ce sujet).', 'Referring back to a whole sentence: das / dies (that), was (which): Er verschwieg seinen Namen, was alle wunderte. Pronominal adverbs: dabei / hierbei (in doing so), dadurch, daraus, demzufolge (accordingly), diesbezüglich (in this regard).'),
        ('Structurer : zunächst (tout d’abord), ferner / darüber hinaus (en outre), schließlich (enfin), im Folgenden (ci-après), wie bereits erwähnt (comme déjà mentionné), im Hinblick auf (en vue de, eu égard à), was… betrifft (en ce qui concerne).', 'Structuring: zunächst (first of all), ferner / darüber hinaus (furthermore), schließlich (finally), im Folgenden (below), wie bereits erwähnt (as already mentioned), im Hinblick auf (with a view to), was… betrifft (as far as… is concerned).'),
      ], [
        DG('letzterer', 'ersterer … letzterer', ('le premier… le second', 'the former… the latter')),
        DG('was-satzbezug', '…, was alle wunderte', ('ce qui (reprise de toute la phrase)', 'which (referring to the whole clause)')),
        DG('hierbei', 'hierbei / dabei', ('ce faisant, à cette occasion', 'in doing so, in this')),
        DG('demzufolge', 'demzufolge', ('par conséquent, en conséquence', 'accordingly')),
        DG('diesbezueglich', 'diesbezüglich', ('à ce sujet, à cet égard', 'in this regard')),
        DG('darueber-hinaus', 'darüber hinaus / ferner', ('en outre, de plus', 'furthermore, moreover')),
        DG('im-hinblick-auf', 'im Hinblick auf + Akkusativ', ('eu égard à, en vue de', 'with a view to, with regard to')),
        DG('wie-erwaehnt', 'wie bereits erwähnt', ('comme déjà mentionné', 'as already mentioned')),
      ], [
        x('Der Ritter stellte eine einzige Bedingung, was der Herzogin zunächst leicht erschien.', 'Le chevalier posa une seule condition, ce qui parut d’abord facile à la duchesse.', 'The knight set a single condition, which at first seemed easy to the duchess.'),
        x('Sie fragte dennoch nach seinem Namen; demzufolge musste er sie für immer verlassen.', 'Elle lui demanda pourtant son nom ; par conséquent, il dut la quitter pour toujours.', 'She asked his name nonetheless; accordingly, he had to leave her for ever.'),
      ], [
        FB(CHOOSE, 'Er kam eine Stunde zu spät, ＿ die Chefin sehr ärgerte.', ['was', 'das', 'welche'], 'was', ('Reprise de toute la phrase : was.', 'Referring to the whole clause: was.'), ('Il est arrivé avec une heure de retard, ce qui a beaucoup agacé la directrice.', 'He arrived an hour late, which greatly annoyed the manager.')),
        FB(CHOOSE, 'Wir bieten Kurse und Workshops an; ＿ finden am Wochenende statt.', ['letztere', 'erstere', 'dieselbe'], 'letztere', ('Le dernier nommé : letztere.', 'The last named: letztere.'), ('Nous proposons des cours et des ateliers ; ces derniers ont lieu le week-end.', 'We offer courses and workshops; the latter take place at the weekend.')),
        FB(CHOOSE, 'Die Kosten sind gestiegen. ＿ müssen die Preise erhöht werden.', ['Demzufolge', 'Diesbezüglich', 'Hierbei'], 'Demzufolge', ('Conséquence : demzufolge.', 'Consequence: demzufolge.'), ('Les coûts ont augmenté. Par conséquent, les prix doivent être relevés.', 'Costs have risen. Accordingly, prices must be raised.')),
        FB(CHOOSE, 'Zu Ihrer Anfrage: ＿ kann ich Ihnen leider noch nichts mitteilen.', ['Diesbezüglich', 'Demzufolge', 'Ferner'], 'Diesbezüglich', ('À ce sujet : diesbezüglich.', 'In this regard: diesbezüglich.'), ('Concernant votre demande : je ne peux malheureusement encore rien vous dire à ce sujet.', 'Regarding your enquiry: I am afraid I cannot tell you anything on that yet.')),
      ]),
    L('de-wissenschaftlich', ('Résumer et commenter un graphique', 'Summarising and commenting on a chart'), ('Rédiger un résumé objectif et décrire des données chiffrées.', 'Write an objective summary and describe figures.'), 9, [
        ('Résumer : Der Text handelt von… / befasst sich mit… (traite de). Der Autor vertritt die These, dass… Er führt als Beleg an, dass… (il cite comme preuve). Abschließend kommt er zu dem Schluss, dass…', 'Summarising: Der Text handelt von… / befasst sich mit… (deals with). Der Autor vertritt die These, dass… Er führt als Beleg an, dass… (he cites as evidence). Abschließend kommt er zu dem Schluss, dass…'),
        ('Décrire un graphique : Die Grafik stellt dar, wie… Aus dem Schaubild geht hervor, dass… (il ressort du graphique que). Der Anteil beträgt… (s’élève à). Die Zahl hat sich verdoppelt / halbiert. An erster Stelle steht…', 'Describing a chart: Die Grafik stellt dar, wie… Aus dem Schaubild geht hervor, dass… (the chart shows that). Der Anteil beträgt… (amounts to). Die Zahl hat sich verdoppelt / halbiert. An erster Stelle steht…'),
        ('Comparer et nuancer : im Vergleich zu, im Gegensatz zu, verglichen mit ; rund / knapp / gut (environ / un peu moins de / un peu plus de) ; auffällig ist, dass… (il est frappant que) ; dies lässt sich darauf zurückführen, dass… (cela s’explique par).', 'Comparing and qualifying: im Vergleich zu, im Gegensatz zu, verglichen mit; rund / knapp / gut (around / just under / just over); auffällig ist, dass… (it is striking that); dies lässt sich darauf zurückführen, dass… (this can be put down to).'),
      ], [
        DG('sich-befassen', 'Der Text befasst sich mit …', ('Le texte traite de…', 'The text deals with…')),
        DG('these-vertreten', 'die These vertreten, dass …', ('soutenir la thèse que…', 'to argue that…')),
        DG('geht-hervor', 'Aus der Grafik geht hervor, dass …', ('Il ressort du graphique que…', 'The chart shows that…')),
        DG('zurueckfuehren', 'Das lässt sich auf … zurückführen.', ('Cela s’explique par…', 'This can be put down to…')),
        D('beleg', 'der Beleg', ('la preuve, la référence', 'the evidence, the reference')),
        D('betragen', 'betragen', ('s’élever à', 'to amount to')),
        D('schaubild', 'das Schaubild', ('le graphique, le schéma', 'the chart, the diagram')),
        D('knapp', 'knapp', ('un peu moins de, à peine', 'just under, barely')),
        D('auffaellig', 'auffällig', ('frappant, remarquable', 'striking, conspicuous')),
      ], [
        x('Aus dem Schaubild geht hervor, dass knapp die Hälfte der Befragten täglich liest.', 'Il ressort du graphique qu’un peu moins de la moitié des personnes interrogées lit chaque jour.', 'The chart shows that just under half of those surveyed read every day.'),
        x('Der Autor vertritt die These, dass sich dieser Rückgang auf die sozialen Medien zurückführen lässt.', 'L’auteur soutient la thèse que ce recul s’explique par les réseaux sociaux.', 'The author argues that this decline can be put down to social media.'),
      ], [
        FB(CHOOSE, 'Der Artikel befasst sich ＿ den Folgen der Digitalisierung.', ['mit', 'über', 'von'], 'mit', ('Sich befassen mit.', 'Sich befassen mit.'), ('L’article traite des conséquences de la numérisation.', 'The article deals with the consequences of digitalisation.')),
        FB(CHOOSE, 'Der Anteil der Frauen ＿ 42 Prozent.', ['beträgt', 'steht', 'handelt'], 'beträgt', ('S’élever à : betragen.', 'To amount to: betragen.'), ('La part des femmes s’élève à 42 pour cent.', 'The share of women amounts to 42 per cent.')),
        FB(CHOOSE, 'Dieser Anstieg lässt sich ＿ die höheren Energiepreise zurückführen.', ['auf', 'an', 'zu'], 'auf', ('Zurückführen auf + accusatif.', 'Zurückführen auf + accusative.'), ('Cette hausse s’explique par l’augmentation des prix de l’énergie.', 'This rise can be put down to higher energy prices.')),
        TF('Knapp 30 Prozent der Befragten stimmten zu.', ('Un peu plus de 30 % des personnes interrogées étaient d’accord.', 'Just over 30% of those surveyed agreed.'), FAUX, ('Knapp = un peu moins de.', 'Knapp = just under.')),
      ]),
  ]),
  CH('goethec1-w8-c2', ('La question interdite', 'The forbidden question'), [
    L('de-hochschule', ('Les études et la vie universitaire', 'Studies and university life'), ('Parler de son cursus, d’un séminaire et d’un travail de recherche.', 'Talk about your course, a seminar and a research paper.'), 8, [
        ('Le cursus : das Studienfach (la discipline), der Studiengang (le cursus), das Semester, die Vorlesung (le cours magistral), das Seminar, der Abschluss (le diplôme), sich einschreiben (s’inscrire), das Stipendium (la bourse).', 'The course: das Studienfach (the subject), der Studiengang (the degree course), das Semester, die Vorlesung (the lecture), das Seminar, der Abschluss (the degree), sich einschreiben (to enrol), das Stipendium (the scholarship).'),
        ('Les travaux : das Referat (l’exposé), die Hausarbeit (le dossier, le mémoire court), die Abschlussarbeit (le mémoire de fin d’études), die Doktorarbeit (la thèse), der Betreuer (le directeur de recherche), die Fragestellung (la problématique), die Gliederung (le plan).', 'Coursework: das Referat (the presentation), die Hausarbeit (the term paper), die Abschlussarbeit (the final thesis), die Doktorarbeit (the doctoral thesis), der Betreuer (the supervisor), die Fragestellung (the research question), die Gliederung (the outline).'),
        ('Travailler : sich auseinandersetzen mit (étudier de près), zitieren, belegen (étayer), eine Arbeit einreichen (remettre un travail), eine Frist verlängern (prolonger un délai), sich spezialisieren auf.', 'Working: sich auseinandersetzen mit (to engage closely with), zitieren, belegen (to back up), eine Arbeit einreichen (to hand in a paper), eine Frist verlängern (to extend a deadline), sich spezialisieren auf.'),
      ], [
        D('studiengang', 'der Studiengang', ('le cursus, la filière', 'the degree course')),
        D('vorlesung', 'die Vorlesung', ('le cours magistral', 'the lecture')),
        D('referat', 'das Referat', ('l’exposé', 'the presentation, the paper')),
        D('hausarbeit', 'die Hausarbeit', ('le dossier, le mémoire court', 'the term paper')),
        D('fragestellung', 'die Fragestellung', ('la problématique', 'the research question')),
        D('gliederung', 'die Gliederung', ('le plan (d’un texte)', 'the outline, the structure')),
        D('einreichen', 'einreichen', ('remettre, déposer', 'to hand in, to submit')),
        D('sich-auseinandersetzen', 'sich auseinandersetzen mit', ('étudier de près, se confronter à', 'to engage closely with')),
        D('stipendium', 'das Stipendium', ('la bourse d’études', 'the scholarship')),
      ], [
        x('In ihrer Hausarbeit setzt sie sich mit der Frage auseinander, warum Lohengrin seinen Namen verschweigt.', 'Dans son dossier, elle étudie de près la question de savoir pourquoi Lohengrin tait son nom.', 'In her term paper she engages closely with the question of why Lohengrin conceals his name.'),
        x('Die Arbeit ist bis Ende des Semesters beim Betreuer einzureichen.', 'Le travail est à remettre au directeur de recherche avant la fin du semestre.', 'The paper is to be handed in to the supervisor by the end of the semester.'),
      ], [
        FB(COMPLETE, 'Bevor du schreibst, brauchst du eine klare ＿ mit Einleitung, Hauptteil und Schluss.', ['Gliederung', 'Vorlesung', 'Frist'], 'Gliederung', ('Le plan : die Gliederung.', 'The outline: die Gliederung.'), ('Avant d’écrire, il te faut un plan clair avec introduction, développement et conclusion.', 'Before you write, you need a clear outline with introduction, main body and conclusion.')),
        FB(CHOOSE, 'Im Seminar setzen wir uns ＿ aktuellen Theorien auseinander.', ['mit', 'über', 'an'], 'mit', ('Sich auseinandersetzen mit.', 'Sich auseinandersetzen mit.'), ('En séminaire, nous étudions de près les théories actuelles.', 'In the seminar we engage closely with current theories.')),
        TF('Die Professorin hat die Frist um zwei Wochen verlängert.', ('Il faut rendre le travail deux semaines plus tôt.', 'The paper must be handed in two weeks earlier.'), FAUX, ('Die Frist verlängern = prolonger le délai.', 'Die Frist verlängern = to extend the deadline.')),
        DC(ANSWER, [('Betreuerin', 'Worum geht es in Ihrer Abschlussarbeit?')], ('Ta directrice de mémoire te demande ton sujet (les effets du télétravail sur la santé).', 'Your supervisor asks about your topic (the effects of working from home on health).'), ['Sie befasst sich mit den Auswirkungen des Homeoffice auf die Gesundheit.', 'Sie befasst sich über die Auswirkungen des Homeoffice an die Gesundheit.', 'Sie handelt mit den Auswirkungen von Homeoffice zu Gesundheit.'], 'Sie befasst sich mit den Auswirkungen des Homeoffice auf die Gesundheit.', ('Sich befassen mit ; Auswirkungen auf.', 'Sich befassen mit; Auswirkungen auf.')),
      ]),
  ])])

write_level('GOETHEC1', ('Goethe C1 : le Danube des Nibelungen', 'Goethe C1: the Danube of the Nibelungs'), REGION, 'Danube of the Nibelungs', 46,
  [W1, W2, W3, W4, W5, W6, W7, W8, FINAL('GOETHEC1', REGION, ('Simulation Goethe C1 : la porte des savants', 'Goethe C1 simulation: the scholars’ gate'), 'Lesen, Hören et Schreiben (l’oral, Sprechen, n’est pas évalué)', 'Lesen, Hören and Schreiben (the speaking test, Sprechen, is not assessed)', modules=True)])
