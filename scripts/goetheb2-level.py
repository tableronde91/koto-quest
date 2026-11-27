# Niveau Goethe-Zertifikat B2 (allemand, CECRL B2) : 8 étapes à Weimar, parmi les ballades de Goethe et de Schiller.
# Mode histoire : l'apprenti·e des frères Grimm entre à la cour des poètes ; les créatures des ballades se sont échappées des manuscrits (voir gen-story.py).
# Usage : python3 scripts/goetheb2-level.py   (réécrit content/goetheb2/goetheb2.json ; les niveaux A1 à B1 doivent déjà exister)
from de_common import *
begin('GOETHEB2')

REGION = 'Weimar des poètes'

# ═════════════════════════ 1 : L'irréel du passé, les émotions ═════════════════════════
W1 = WORLD('goetheb2-w1', ('La chevauchée du Roi des Aulnes', 'The Erlking’s ride'), REGION,
  ('Exprimer un regret et une hypothèse sur le passé avec le Konjunktiv II passé, comparer avec als ob, nommer les émotions.', 'Express regret and a hypothesis about the past with the past Konjunktiv II, compare with als ob, name emotions.'),
  (('Le Roi des Aulnes', 'The Erlking'), '☾', ('Dans la nuit et le vent, le Roi des Aulnes murmure à l’oreille de l’enfant ce que le père ne veut pas entendre. Dis ce qui aurait pu se passer, ce qu’il aurait fallu faire, et rassure sans mentir.', 'In the night and the wind, the Erlking whispers in the child’s ear what the father will not hear. Say what could have happened, what should have been done, and reassure without lying.')),
  [CH('goetheb2-w1-c1', ('Si seulement…', 'If only…'), [
    L('de-konj2-verg', ('L’irréel du passé : hätte / wäre + participe', 'The unreal past: hätte / wäre + participle'), ('Dire ce qui se serait passé si les choses avaient été différentes.', 'Say what would have happened if things had been different.'), 9, [
        ('Konjunktiv II passé : hätte ou wäre + participe passé. Ich hätte angerufen (j’aurais appelé). Sie wäre gekommen (elle serait venue). Il n’existe qu’une seule forme pour tout le passé.', 'Past Konjunktiv II: hätte or wäre + past participle. Ich hätte angerufen (I would have called). Sie wäre gekommen (she would have come). There is only one form for the whole past.'),
        ('Hypothèse irréelle du passé : Wenn er schneller geritten wäre, hätte er das Kind gerettet. Sans wenn, le verbe passe en tête : Wäre er schneller geritten, hätte er…', 'Unreal past hypothesis: Wenn er schneller geritten wäre, hätte er das Kind gerettet. Without wenn, the verb moves to the front: Wäre er schneller geritten, hätte er…'),
        ('Avec un verbe de modalité : hätte + infinitif + modal à l’infinitif. Du hättest zuhören sollen (tu aurais dû écouter). Ich hätte helfen können (j’aurais pu aider). Dans une subordonnée, hätte passe devant : …, dass er hätte kommen sollen.', 'With a modal verb: hätte + infinitive + modal in the infinitive. Du hättest zuhören sollen (you should have listened). Ich hätte helfen können (I could have helped). In a subordinate clause, hätte moves in front: …, dass er hätte kommen sollen.'),
      ], [
        DG('konj2-verg', 'hätte / wäre + Partizip II', ('conditionnel passé (irréel du passé)', 'past conditional (unreal past)')),
        DG('haette-sollen', 'hätte … sollen', ('aurait dû', 'should have')),
        DG('haette-koennen', 'hätte … können', ('aurait pu', 'could have')),
        DG('wenn-weglassen', 'Wäre er …, hätte er …', ('hypothèse sans wenn (verbe en tête)', 'hypothesis without wenn (verb first)')),
        D('retten', 'retten', ('sauver', 'to save, to rescue')),
        D('bereuen', 'bereuen', ('regretter', 'to regret')),
        D('reiten', 'reiten', ('aller à cheval, chevaucher', 'to ride (a horse)')),
        D('rechtzeitig', 'rechtzeitig', ('à temps', 'in time')),
        D('beinahe', 'beinahe / fast', ('presque, faillir', 'nearly (it almost happened)')),
      ], [
        x('Wenn der Vater dem Kind geglaubt hätte, wäre er vielleicht schneller geritten.', 'Si le père avait cru l’enfant, il aurait peut-être chevauché plus vite.', 'If the father had believed the child, he might have ridden faster.'),
        x('Er hätte umkehren sollen. Später bereute er, dass er nicht zugehört hatte.', 'Il aurait dû faire demi-tour. Plus tard, il regretta de ne pas avoir écouté.', 'He should have turned back. Later he regretted that he had not listened.'),
      ], [
        FB(CHOOSE, 'Wenn ich das gewusst ＿, wäre ich früher gekommen.', ['hätte', 'wäre', 'würde'], 'hätte', ('Wissen se conjugue avec haben : gewusst hätte.', 'Wissen takes haben: gewusst hätte.'), ('Si j’avais su cela, je serais venu plus tôt.', 'If I had known that, I would have come earlier.')),
        FB(CHOOSE, 'Wir ＿ fast zu spät gekommen.', ['wären', 'hätten', 'würden'], 'wären', ('Kommen se conjugue avec sein : wären gekommen.', 'Kommen takes sein: wären gekommen.'), ('Nous avons failli arriver en retard.', 'We almost arrived too late.')),
        FB(CHOOSE, 'Du hättest mich anrufen ＿.', ['sollen', 'gesollt', 'sollst'], 'sollen', ('Hätte + infinitif + sollen.', 'Hätte + infinitive + sollen.'), ('Tu aurais dû m’appeler.', 'You should have called me.')),
        order(('Remets dans l’ordre : « J’aurais pu t’aider. »', 'Put in order: “I could have helped you.”'), ['Ich', 'hätte', 'dir', 'helfen', 'können.'], ('Hätte en deuxième position, puis infinitif + können à la fin.', 'Hätte in second position, then infinitive + können at the end.')),
      ]),
    L('de-als-ob', ('Comme si : als ob', 'As if: als ob'), ('Décrire une apparence trompeuse ou une impression.', 'Describe a deceptive appearance or an impression.'), 8, [
        ('Als ob (comme si) est suivi du Konjunktiv II, verbe à la fin : Er tut so, als ob er nichts hörte / hören würde. Au passé : als ob er nichts gehört hätte.', 'Als ob (as if) is followed by Konjunktiv II, verb at the end: Er tut so, als ob er nichts hörte / hören würde. In the past: als ob er nichts gehört hätte.'),
        ('Sans ob, le verbe suit immédiatement als : Es sieht aus, als wäre es Nebel. Es klang, als käme jemand.', 'Without ob, the verb follows als directly: Es sieht aus, als wäre es Nebel. Es klang, als käme jemand.'),
        ('Verbes fréquents avant als ob : aussehen (avoir l’air), scheinen (sembler), klingen (sonner), sich anfühlen (donner la sensation), so tun (faire semblant), wirken (donner l’impression).', 'Common verbs before als ob: aussehen (to look), scheinen (to seem), klingen (to sound), sich anfühlen (to feel), so tun (to pretend), wirken (to come across).'),
      ], [
        DG('als-ob', 'als ob + Konjunktiv II', ('comme si', 'as if, as though')),
        DG('als-verb', 'als + Verb (Konjunktiv II)', ('comme si (sans ob, verbe en tête)', 'as if (without ob, verb first)')),
        D('so-tun', 'so tun, als ob', ('faire semblant de', 'to pretend')),
        D('scheinen', 'scheinen', ('sembler, paraître', 'to seem, to appear')),
        D('wirken', 'wirken', ('donner l’impression, paraître', 'to come across, to appear')),
        D('klingen', 'klingen', ('sonner, avoir un son', 'to sound')),
        D('nebel', 'der Nebel', ('le brouillard', 'the fog, the mist')),
        D('fluestern', 'flüstern', ('chuchoter', 'to whisper')),
      ], [
        x('Der Vater tut so, als ob er die Stimme nicht hörte.', 'Le père fait comme s’il n’entendait pas la voix.', 'The father acts as if he did not hear the voice.'),
        x('Es sah aus, als wäre der König nur ein Streifen Nebel.', 'On aurait dit que le roi n’était qu’une traînée de brouillard.', 'It looked as if the king were only a streak of mist.'),
      ], [
        FB(CHOOSE, 'Sie tut so, als ob sie alles ＿.', ['wüsste', 'weiß', 'gewusst'], 'wüsste', ('Als ob + Konjunktiv II : wüsste.', 'Als ob + Konjunktiv II: wüsste.'), ('Elle fait comme si elle savait tout.', 'She acts as if she knew everything.')),
        FB(CHOOSE, 'Es sieht aus, als ＿ es gleich regnen.', ['würde', 'wird', 'ob'], 'würde', ('Sans ob, le verbe suit als : als würde es regnen.', 'Without ob, the verb follows als: als würde es regnen.'), ('On dirait qu’il va pleuvoir.', 'It looks as if it is about to rain.')),
        FB(CHOOSE, 'Er sah aus, als ob er die ganze Nacht nicht geschlafen ＿.', ['hätte', 'wäre', 'hat'], 'hätte', ('Passé : geschlafen hätte.', 'Past: geschlafen hätte.'), ('Il avait l’air de ne pas avoir dormi de la nuit.', 'He looked as if he had not slept all night.')),
        TF('Sie wirkt ruhig, aber in Wirklichkeit ist sie sehr nervös.', ('Elle est aussi calme qu’elle en a l’air.', 'She is as calm as she looks.'), FAUX, ('Wirken = donner l’impression ; in Wirklichkeit = en réalité.', 'Wirken = to come across; in Wirklichkeit = in reality.')),
      ]),
  ]),
  CH('goetheb2-w1-c2', ('La peur de l’enfant', 'The child’s fear'), [
    L('de-gefuehle', ('Les émotions', 'Emotions'), ('Nommer ce que l’on ressent et réagir aux émotions des autres.', 'Name what you feel and respond to other people’s emotions.'), 8, [
        ('Noms et verbes vont ensemble : die Angst / sich fürchten vor, die Sorge / sich Sorgen machen um, die Wut / wütend sein auf, die Enttäuschung / enttäuscht sein von, die Erleichterung / erleichtert sein.', 'Nouns and verbs go together: die Angst / sich fürchten vor, die Sorge / sich Sorgen machen um, die Wut / wütend sein auf, die Enttäuschung / enttäuscht sein von, die Erleichterung / erleichtert sein.'),
        ('Verbes de réaction : erschrecken (sursauter, effrayer), jemanden beruhigen (calmer), trösten (consoler), sich aufregen über (s’énerver à propos de), zittern (trembler).', 'Verbs of reaction: erschrecken (to be startled, to frighten), jemanden beruhigen (to calm), trösten (to comfort), sich aufregen über (to get worked up about), zittern (to tremble).'),
        ('Pour rassurer : Mach dir keine Sorgen. Beruhige dich. Es ist halb so schlimm (ce n’est pas si grave). Das bildest du dir nur ein (tu te fais des idées).', 'To reassure: Mach dir keine Sorgen. Beruhige dich. Es ist halb so schlimm (it is not that bad). Das bildest du dir nur ein (you are only imagining it).'),
      ], [
        D('sich-fuerchten', 'sich fürchten vor', ('avoir peur de, craindre', 'to be frightened of')),
        D('sich-sorgen-machen', 'sich Sorgen machen um', ('se faire du souci pour', 'to worry about')),
        D('erschrecken', 'erschrecken', ('sursauter ; effrayer', 'to be startled; to frighten')),
        D('beruhigen', 'beruhigen', ('calmer, rassurer', 'to calm, to reassure')),
        D('troesten', 'trösten', ('consoler', 'to comfort, to console')),
        D('erleichtert', 'erleichtert', ('soulagé', 'relieved')),
        D('wuetend', 'wütend', ('furieux, en colère', 'furious, angry')),
        D('sich-einbilden', 'sich etwas einbilden', ('s’imaginer quelque chose, se faire des idées', 'to imagine something (wrongly)')),
      ], [
        x('Das Kind fürchtet sich vor dem Erlkönig, aber der Vater versucht, es zu beruhigen.', 'L’enfant a peur du Roi des Aulnes, mais le père essaie de le calmer.', 'The child is frightened of the Erlking, but the father tries to calm him.'),
        x('„Das bildest du dir nur ein, mein Sohn. Es ist der Wind in den Blättern.“', '« Tu te fais des idées, mon fils. C’est le vent dans les feuilles. »', '“You are only imagining it, my son. It is the wind in the leaves.”'),
      ], [
        FB(CHOOSE, 'Ich mache mir Sorgen ＿ meine Mutter.', ['um', 'vor', 'auf'], 'um', ('Sich Sorgen machen um + accusatif.', 'Sich Sorgen machen um + accusative.'), ('Je me fais du souci pour ma mère.', 'I am worried about my mother.')),
        FB(CHOOSE, 'Das Kind fürchtet sich ＿ der Dunkelheit.', ['vor', 'um', 'über'], 'vor', ('Sich fürchten vor + datif.', 'Sich fürchten vor + dative.'), ('L’enfant a peur du noir.', 'The child is afraid of the dark.')),
        FB(COMPLETE, 'Die Prüfung ist vorbei, und ich habe bestanden. Ich bin so ＿!', ['erleichtert', 'wütend', 'enttäuscht'], 'erleichtert', ('Soulagé : erleichtert.', 'Relieved: erleichtert.'), ('L’examen est fini, et je l’ai réussi. Je suis tellement soulagé !', 'The exam is over, and I passed. I am so relieved!')),
        DC(ANSWER, [('Kind', 'Vater, siehst du den Erlkönig nicht?')], ('L’enfant, effrayé, te montre le Roi des Aulnes (rassure-le comme le père).', 'The frightened child points out the Erlking to you (reassure him as the father does).'), ['Beruhige dich, das bildest du dir nur ein.', 'Beruhige mich, ich bilde mir dich ein.', 'Ich fürchte mich um dir.'], 'Beruhige dich, das bildest du dir nur ein.', ('Rassurer : Beruhige dich ; sich etwas einbilden.', 'Reassuring: Beruhige dich; sich etwas einbilden.')),
      ]),
  ])])

# ═════════════════════════ 2 : Autres passifs, la technique ═════════════════════════
W2 = WORLD('goetheb2-w2', ('L’atelier de l’Apprenti sorcier', 'The Sorcerer’s Apprentice’s workshop'), REGION,
  ('Distinguer l’action et l’état au passif, remplacer le passif par sich lassen, sein + zu et -bar, parler de technique et de numérique.', 'Tell action from state in the passive, replace the passive with sich lassen, sein + zu and -bar, talk about technology and the digital world.'),
  (('Le Balai ensorcelé', 'The Enchanted Broom'), '✤', ('Le maître est sorti, l’apprenti a prononcé la formule, et le Balai ensorcelé porte de l’eau sans s’arrêter. Il ne se laisse pas arrêter, il n’est pas arrêtable… à moins de connaître les bons mots.', 'The master is out, the apprentice has spoken the spell, and the Enchanted Broom carries water without stopping. It cannot be stopped, it is unstoppable… unless you know the right words.')),
  [CH('goetheb2-w2-c1', ('La formule oubliée', 'The forgotten spell'), [
    L('de-zustandspassiv', ('Action ou résultat : wird geöffnet / ist geöffnet', 'Action or result: wird geöffnet / ist geöffnet'), ('Distinguer le passif d’action du passif d’état.', 'Tell the passive of action from the passive of state.'), 8, [
        ('Passif d’action (werden) : ce qui est en train de se faire. Die Tür wird geöffnet (on ouvre la porte). Passif d’état (sein) : le résultat. Die Tür ist geöffnet (la porte est ouverte).', 'Passive of action (werden): what is being done. Die Tür wird geöffnet (the door is being opened). Passive of state (sein): the result. Die Tür ist geöffnet (the door is open).'),
        ('Au passé : Das Haus wurde 1790 gebaut (action) ; Das Haus war schon verkauft (état). Avec le passif d’état, on ne nomme en général pas l’auteur.', 'In the past: Das Haus wurde 1790 gebaut (action); Das Haus war schon verkauft (state). With the passive of state, the agent is usually not named.'),
        ('Le moyen s’exprime avec durch + accusatif, l’auteur avec von + datif : Das Haus wurde durch das Wasser zerstört. Der Besen wurde vom Lehrling verzaubert.', 'The means is expressed with durch + accusative, the agent with von + dative: Das Haus wurde durch das Wasser zerstört. Der Besen wurde vom Lehrling verzaubert.'),
      ], [
        DG('zustandspassiv', 'sein + Partizip II (Zustandspassiv)', ('passif d’état (résultat)', 'passive of state (result)')),
        DG('durch-mittel', 'durch + Akkusativ (Passiv)', ('par, au moyen de (passif)', 'by means of, through (passive)')),
        D('besen', 'der Besen', ('le balai', 'the broom')),
        D('lehrling', 'der Lehrling', ('l’apprenti', 'the apprentice')),
        D('meister', 'der Meister', ('le maître (artisan)', 'the master')),
        D('zauberspruch', 'der Zauberspruch', ('la formule magique', 'the magic spell')),
        D('ueberschwemmt', 'überschwemmt', ('inondé', 'flooded')),
        D('erledigt', 'erledigt', ('réglé, terminé', 'done, settled')),
      ], [
        x('Der Besen wurde vom Lehrling verzaubert. Bald war das ganze Haus überschwemmt.', 'Le balai fut ensorcelé par l’apprenti. Bientôt, toute la maison était inondée.', 'The broom was enchanted by the apprentice. Soon the whole house was flooded.'),
        x('Als der Meister zurückkam, war die Arbeit nicht erledigt, sondern alles zerstört.', 'Quand le maître revint, le travail n’était pas terminé : tout était détruit.', 'When the master came back, the work was not done; everything was destroyed.'),
      ], [
        FB(CHOOSE, 'Das Geschäft ＿ sonntags geschlossen. Niemand arbeitet dort.', ['ist', 'wird', 'hat'], 'ist', ('État durable : ist geschlossen.', 'A lasting state: ist geschlossen.'), ('Le magasin est fermé le dimanche. Personne n’y travaille.', 'The shop is closed on Sundays. Nobody works there.')),
        FB(CHOOSE, 'Die Brücke ＿ gerade repariert. Man kann nicht hinüberfahren.', ['wird', 'ist', 'war'], 'wird', ('Action en cours : wird repariert.', 'An action in progress: wird repariert.'), ('Le pont est en réparation. On ne peut pas le traverser.', 'The bridge is being repaired. You cannot drive across.')),
        FB(CHOOSE, 'Die Stadt wurde ＿ ein Feuer zerstört.', ['durch', 'von', 'mit'], 'durch', ('Le moyen, la cause : durch.', 'The means or cause: durch.'), ('La ville a été détruite par un incendie.', 'The town was destroyed by a fire.')),
        TF('Der Tisch ist schon gedeckt.', ('Quelqu’un est en train de mettre la table.', 'Someone is laying the table right now.'), FAUX, ('Ist gedeckt = la table est mise (résultat).', 'Ist gedeckt = the table is laid (result).')),
      ]),
    L('de-passiv-ersatz', ('Éviter le passif : sich lassen, sein + zu, -bar', 'Avoiding the passive: sich lassen, sein + zu, -bar'), ('Dire ce qui peut ou doit être fait sans employer werden.', 'Say what can or must be done without using werden.'), 9, [
        ('Sich lassen + infinitif = pouvoir être fait : Das Problem lässt sich lösen (= kann gelöst werden). Der Besen lässt sich nicht aufhalten.', 'Sich lassen + infinitive = can be done: Das Problem lässt sich lösen (= kann gelöst werden). Der Besen lässt sich nicht aufhalten.'),
        ('Sein + zu + infinitif = pouvoir ou devoir être fait, selon le contexte : Das ist nicht zu glauben (on ne peut pas le croire). Die Regeln sind zu beachten (les règles doivent être respectées).', 'Sein + zu + infinitive = can or must be done, depending on context: Das ist nicht zu glauben (it cannot be believed). Die Regeln sind zu beachten (the rules must be observed).'),
        ('Adjectifs en -bar (possible) : lösbar (soluble), essbar (comestible), machbar (faisable), erreichbar (joignable). Contraire avec un- : unlösbar, unbezahlbar. Et man reste le plus simple : Man kann das lösen.', 'Adjectives in -bar (possible): lösbar (solvable), essbar (edible), machbar (feasible), erreichbar (reachable). Opposite with un-: unlösbar, unbezahlbar. And man remains the simplest: Man kann das lösen.'),
      ], [
        DG('sich-lassen', 'sich lassen + Infinitiv', ('pouvoir être fait (se laisser…)', 'can be done (sich lassen)')),
        DG('sein-zu', 'sein + zu + Infinitiv', ('être à faire (pouvoir ou devoir être fait)', 'is to be done (can or must be done)')),
        DG('bar', '-bar (lösbar, machbar)', ('suffixe -able (possibilité)', 'suffix -able (possibility)')),
        D('loesen', 'lösen', ('résoudre', 'to solve')),
        D('aufhalten', 'aufhalten', ('arrêter, retenir', 'to stop, to hold back')),
        D('beachten', 'beachten', ('respecter, tenir compte de', 'to observe, to pay attention to')),
        D('erreichbar', 'erreichbar', ('joignable, accessible', 'reachable, available')),
        D('machbar', 'machbar', ('faisable', 'feasible, doable')),
        D('vermeiden', 'vermeiden', ('éviter', 'to avoid')),
      ], [
        x('Der Besen lässt sich nicht aufhalten: Er holt immer mehr Wasser.', 'Le balai ne se laisse pas arrêter : il va chercher toujours plus d’eau.', 'The broom cannot be stopped: it fetches more and more water.'),
        x('Die Katastrophe wäre vermeidbar gewesen. Der Zauberspruch war eben nicht zu vergessen!', 'La catastrophe aurait été évitable. Il ne fallait justement pas oublier la formule !', 'The disaster would have been avoidable. The spell was simply not to be forgotten!'),
      ], [
        FB(CHOOSE, 'Dieses Problem ＿ sich leicht lösen.', ['lässt', 'ist', 'wird'], 'lässt', ('Peut être résolu : lässt sich lösen.', 'Can be solved: lässt sich lösen.'), ('Ce problème se résout facilement.', 'This problem can easily be solved.')),
        FB(CHOOSE, 'Die Rechnung ist bis Freitag ＿.', ['zu bezahlen', 'bezahlen', 'bezahlt werden'], 'zu bezahlen', ('Doit être fait : ist… zu bezahlen.', 'Must be done: ist… zu bezahlen.'), ('La facture est à payer avant vendredi.', 'The bill is to be paid by Friday.')),
        FB(CHOOSE, 'Sind diese Pilze ＿? — Nein, sie sind giftig.', ['essbar', 'essend', 'gegessen'], 'essbar', ('Qu’on peut manger : essbar.', 'That can be eaten: essbar.'), ('Ces champignons sont-ils comestibles ? — Non, ils sont vénéneux.', 'Are these mushrooms edible? — No, they are poisonous.')),
        DC(ANSWER, [('Meister', 'Kann man diese Maschine reparieren?')], ('Le maître demande si la machine est réparable (oui, facilement).', 'The master asks whether the machine can be repaired (yes, easily).'), ['Ja, sie lässt sich leicht reparieren.', 'Ja, sie lässt leicht repariert.', 'Ja, sie ist zu reparierbar werden.'], 'Ja, sie lässt sich leicht reparieren.', ('Sich lassen + infinitif.', 'Sich lassen + infinitive.')),
      ]),
  ]),
  CH('goetheb2-w2-c2', ('Les machines sans maître', 'Machines without a master'), [
    L('de-technik', ('La technique et le numérique', 'Technology and the digital world'), ('Parler des outils numériques, de leurs avantages et de leurs risques.', 'Talk about digital tools, their advantages and their risks.'), 8, [
        ('Le numérique : die Digitalisierung, die künstliche Intelligenz (l’intelligence artificielle), das Gerät (l’appareil), die Daten (les données), der Datenschutz (la protection des données), das Netzwerk (le réseau).', 'The digital world: die Digitalisierung, die künstliche Intelligenz (artificial intelligence), das Gerät (the device), die Daten (data), der Datenschutz (data protection), das Netzwerk (the network).'),
        ('Verbes : entwickeln (développer), herunterladen (télécharger), speichern (enregistrer), löschen (effacer), ersetzen (remplacer), steuern (piloter, commander), abhängig sein von (dépendre de).', 'Verbs: entwickeln (to develop), herunterladen (to download), speichern (to save), löschen (to delete), ersetzen (to replace), steuern (to control), abhängig sein von (to depend on).'),
        ('Pour débattre : Die Technik erleichtert den Alltag (facilite). Die Entwicklung ist nicht aufzuhalten. Die Frage ist, wer die Verantwortung trägt (porte la responsabilité).', 'For debate: Die Technik erleichtert den Alltag (makes easier). Die Entwicklung ist nicht aufzuhalten. Die Frage ist, wer die Verantwortung trägt (bears responsibility).'),
      ], [
        D('kuenstliche-intelligenz', 'die künstliche Intelligenz', ('l’intelligence artificielle', 'artificial intelligence')),
        D('geraet', 'das Gerät', ('l’appareil', 'the device, the appliance')),
        D('daten', 'die Daten', ('les données', 'data')),
        D('entwickeln', 'entwickeln', ('développer', 'to develop')),
        D('speichern', 'speichern', ('enregistrer, stocker', 'to save, to store')),
        D('ersetzen', 'ersetzen', ('remplacer', 'to replace')),
        D('abhaengig', 'abhängig von', ('dépendant de', 'dependent on')),
        D('verantwortung', 'die Verantwortung', ('la responsabilité', 'responsibility')),
      ], [
        x('Maschinen, die selbst lernen, ersetzen immer mehr Arbeiten.', 'Les machines qui apprennent seules remplacent de plus en plus de tâches.', 'Machines that learn by themselves are replacing more and more jobs.'),
        x('Wer trägt die Verantwortung, wenn sich eine Maschine nicht mehr steuern lässt?', 'Qui porte la responsabilité quand une machine ne se laisse plus piloter ?', 'Who bears responsibility when a machine can no longer be controlled?'),
      ], [
        FB(COMPLETE, 'Vergiss nicht, das Dokument zu ＿, sonst ist die Arbeit verloren.', ['speichern', 'löschen', 'ersetzen'], 'speichern', ('Enregistrer : speichern.', 'To save: speichern.'), ('N’oublie pas d’enregistrer le document, sinon le travail est perdu.', 'Do not forget to save the document, otherwise the work is lost.')),
        FB(CHOOSE, 'Viele Menschen sind ＿ ihrem Handy abhängig.', ['von', 'an', 'auf'], 'von', ('Abhängig von + datif.', 'Abhängig von + dative.'), ('Beaucoup de gens sont dépendants de leur téléphone.', 'Many people are dependent on their phone.')),
        TF('Roboter können heute schon viele Arbeiten übernehmen, aber die Verantwortung bleibt beim Menschen.', ('Selon la phrase, les robots sont responsables de leurs actes.', 'According to the sentence, robots are responsible for their actions.'), FAUX, ('Die Verantwortung bleibt beim Menschen = la responsabilité reste à l’humain.', 'Die Verantwortung bleibt beim Menschen = responsibility stays with humans.')),
        DC(ANSWER, [('Kollegin', 'Glaubst du, dass künstliche Intelligenz unsere Arbeit ersetzen wird?')], ('Une collègue te demande si l’IA remplacera votre travail (en partie, selon toi).', 'A colleague asks whether AI will replace your work (partly, in your view).'), ['Zum Teil ja, aber nicht alles lässt sich automatisieren.', 'Zum Teil ja, aber nicht alles lässt automatisiert.', 'Ja, sie ist von uns ersetzbar gespeichert.'], 'Zum Teil ja, aber nicht alles lässt sich automatisieren.', ('Opinion nuancée ; sich lassen + infinitif.', 'A qualified opinion; sich lassen + infinitive.')),
      ]),
  ])])

# ═════════════════════════ 3 : Le discours rapporté, la science ═════════════════════════
W3 = WORLD('goetheb2-w3', ('Le gouffre du Plongeur', 'The Diver’s abyss'), REGION,
  ('Rapporter les paroles d’autrui au Konjunktiv I, nuancer la source d’une information, parler de recherche et de découvertes.', 'Report other people’s words in Konjunktiv I, qualify the source of information, talk about research and discoveries.'),
  (('Le Monstre du gouffre', 'The Monster of the Abyss'), '❂', ('Le roi a jeté sa coupe d’or dans le tourbillon, et un jeune plongeur en est revenu avec un récit incroyable. Le Monstre du gouffre garde le reste : rapporte fidèlement ce que le plongeur dit avoir vu, sans le reprendre à ton compte.', 'The king threw his golden cup into the whirlpool, and a young diver came back with an incredible tale. The Monster of the Abyss guards the rest: report faithfully what the diver says he saw, without vouching for it yourself.')),
  [CH('goetheb2-w3-c1', ('Il dit qu’il a vu…', 'He says he saw…'), [
    L('de-konj1', ('Le discours indirect : le Konjunktiv I', 'Reported speech: Konjunktiv I'), ('Rapporter des paroles à l’écrit sans les reprendre à son compte.', 'Report speech in writing without vouching for it.'), 9, [
        ('Dans la presse et les textes soignés, les paroles rapportées se mettent au Konjunktiv I : radical + -e, -est, -e, -en, -et, -en. Er sagt, er komme morgen. Sie sagt, sie habe keine Zeit.', 'In the press and formal texts, reported speech uses Konjunktiv I: stem + -e, -est, -e, -en, -et, -en. Er sagt, er komme morgen. Sie sagt, sie habe keine Zeit.'),
        ('Sein est irrégulier : ich sei, du sei(e)st, er sei, wir seien, ihr seiet, sie seien. Au passé : habe / sei + participe. Er sagte, er habe nichts gesehen. Sie sei schon gegangen.', 'Sein is irregular: ich sei, du sei(e)st, er sei, wir seien, ihr seiet, sie seien. In the past: habe / sei + participle. Er sagte, er habe nichts gesehen. Sie sei schon gegangen.'),
        ('Quand le Konjunktiv I se confond avec l’indicatif (surtout au pluriel), on prend le Konjunktiv II : Sie sagen, sie hätten keine Zeit (et non haben). Sie kämen später.', 'When Konjunktiv I is identical to the indicative (especially in the plural), Konjunktiv II is used: Sie sagen, sie hätten keine Zeit (not haben). Sie kämen später.'),
      ], [
        DG('konj1', 'er sei / er habe / er komme (Konjunktiv I)', ('subjonctif I du discours rapporté', 'Konjunktiv I for reported speech')),
        DG('konj1-verg', 'er habe … gesehen / er sei … gegangen', ('discours rapporté au passé', 'reported speech in the past')),
        DG('konj1-ersatz', 'sie hätten / sie kämen (statt Konjunktiv I)', ('Konjunktiv II de remplacement', 'Konjunktiv II as a substitute')),
        D('behaupten', 'behaupten', ('affirmer, prétendre', 'to claim, to assert')),
        D('berichten', 'berichten', ('rapporter, relater', 'to report')),
        D('taucher', 'der Taucher', ('le plongeur', 'the diver')),
        D('tiefe', 'die Tiefe', ('la profondeur', 'the depth')),
        D('zeuge', 'der Zeuge', ('le témoin', 'the witness')),
      ], [
        x('Der Taucher berichtete, er habe in der Tiefe schreckliche Tiere gesehen.', 'Le plongeur rapporta qu’il avait vu dans les profondeurs des animaux effroyables.', 'The diver reported that he had seen terrible creatures in the depths.'),
        x('Er behauptete, das Wasser sei dort unten schwarz wie die Nacht.', 'Il affirma que l’eau, là en bas, était noire comme la nuit.', 'He claimed that the water down there was as black as night.'),
      ], [
        FB(CHOOSE, 'Der Minister sagte, er ＿ von nichts gewusst.', ['habe', 'hat', 'sei'], 'habe', ('Discours rapporté au passé, wissen avec haben : habe gewusst.', 'Reported speech in the past, wissen with haben: habe gewusst.'), ('Le ministre a déclaré qu’il n’était au courant de rien.', 'The minister said that he had known nothing.')),
        FB(CHOOSE, 'Sie schreibt, sie ＿ gut angekommen.', ['sei', 'habe', 'ist'], 'sei', ('Ankommen avec sein : sei angekommen.', 'Ankommen with sein: sei angekommen.'), ('Elle écrit qu’elle est bien arrivée.', 'She writes that she has arrived safely.')),
        FB(CHOOSE, 'Die Zeugen sagten, sie ＿ nichts gehört.', ['hätten', 'haben', 'seien'], 'hätten', ('Au pluriel, haben se confondrait avec l’indicatif : hätten.', 'In the plural, haben would look like the indicative: hätten.'), ('Les témoins ont dit qu’ils n’avaient rien entendu.', 'The witnesses said that they had heard nothing.')),
        FB(CHOOSE, 'Der Sprecher erklärte, die Lage ＿ unter Kontrolle.', ['sei', 'wäre gewesen', 'ist gewesen'], 'sei', ('Konjunktiv I de sein : sei.', 'Konjunktiv I of sein: sei.'), ('Le porte-parole a déclaré que la situation était sous contrôle.', 'The spokesman stated that the situation was under control.')),
      ]),
    L('de-quelle', ('Citer ses sources : laut, sollen, angeblich', 'Citing sources: laut, sollen, angeblich'), ('Indiquer d’où vient une information et prendre ses distances.', 'Say where information comes from and distance yourself from it.'), 8, [
        ('Laut + datif / génitif et … zufolge (placé après le nom) = selon : Laut einer Studie… Dem Bericht zufolge… Ils sont suivis de l’indicatif.', 'Laut + dative / genitive and … zufolge (placed after the noun) = according to: Laut einer Studie… Dem Bericht zufolge… They are followed by the indicative.'),
        ('Sollen rapporte une rumeur : Er soll sehr reich sein (il serait très riche, dit-on). Wollen rapporte ce que quelqu’un prétend de lui-même : Er will nichts gesehen haben (il prétend n’avoir rien vu).', 'Sollen reports a rumour: Er soll sehr reich sein (he is said to be very rich). Wollen reports what someone claims about themselves: Er will nichts gesehen haben (he claims to have seen nothing).'),
        ('Adverbes de distance : angeblich (soi-disant), offenbar (manifestement), vermutlich (probablement), anscheinend (apparemment). Verbes : betonen (souligner), bestätigen (confirmer), bestreiten (contester), zugeben (admettre).', 'Adverbs of distance: angeblich (allegedly), offenbar (evidently), vermutlich (presumably), anscheinend (apparently). Verbs: betonen (to stress), bestätigen (to confirm), bestreiten (to dispute), zugeben (to admit).'),
      ], [
        DG('laut', 'laut + Dativ / … zufolge', ('selon, d’après', 'according to')),
        DG('sollen-geruecht', 'Er soll … sein.', ('Il serait…, dit-on (rumeur)', 'He is said to be… (rumour)')),
        DG('wollen-behauptung', 'Er will … gesehen haben.', ('Il prétend avoir vu…', 'He claims to have seen…')),
        D('angeblich', 'angeblich', ('soi-disant, prétendument', 'allegedly')),
        D('offenbar', 'offenbar', ('manifestement', 'evidently, obviously')),
        D('bestaetigen', 'bestätigen', ('confirmer', 'to confirm')),
        D('bestreiten', 'bestreiten', ('contester, nier', 'to dispute, to deny')),
        D('zugeben', 'zugeben', ('admettre, avouer', 'to admit')),
      ], [
        x('Laut dem König soll der Becher aus reinem Gold gewesen sein.', 'Selon le roi, la coupe aurait été en or pur.', 'According to the king, the cup is said to have been of pure gold.'),
        x('Der Taucher will ein Ungeheuer mit hundert Armen gesehen haben.', 'Le plongeur prétend avoir vu un monstre à cent bras.', 'The diver claims to have seen a monster with a hundred arms.'),
      ], [
        FB(CHOOSE, '＿ einer neuen Studie schlafen die Deutschen zu wenig.', ['Laut', 'Zufolge', 'Wegen'], 'Laut', ('Devant le nom : laut ; zufolge se place après.', 'Before the noun: laut; zufolge goes after.'), ('Selon une nouvelle étude, les Allemands dorment trop peu.', 'According to a new study, Germans sleep too little.')),
        FB(CHOOSE, 'Der neue Film ＿ sehr gut sein, habe ich gehört.', ['soll', 'will', 'muss'], 'soll', ('Ouï-dire : soll… sein.', 'Hearsay: soll… sein.'), ('Le nouveau film serait très bon, à ce que j’ai entendu.', 'The new film is said to be very good, I have heard.')),
        FB(CHOOSE, 'Er ＿ den Unfall nicht bemerkt haben, aber niemand glaubt ihm.', ['will', 'soll', 'darf'], 'will', ('Il prétend lui-même : will… haben.', 'He himself claims: will… haben.'), ('Il prétend ne pas avoir remarqué l’accident, mais personne ne le croit.', 'He claims not to have noticed the accident, but nobody believes him.')),
        TF('Der Politiker bestreitet, das Geld bekommen zu haben.', ('L’homme politique reconnaît avoir reçu l’argent.', 'The politician admits having received the money.'), FAUX, ('Bestreiten = contester ; reconnaître = zugeben.', 'Bestreiten = to dispute; to admit = zugeben.')),
      ]),
  ]),
  CH('goetheb2-w3-c2', ('Ce que cache la mer', 'What the sea hides'), [
    L('de-wissenschaft', ('La science et la recherche', 'Science and research'), ('Parler d’une étude, d’une découverte et de ses résultats.', 'Talk about a study, a discovery and its results.'), 8, [
        ('La recherche : die Forschung, der Forscher / die Forscherin, die Studie (l’étude), der Versuch (l’expérience), das Ergebnis (le résultat), die Ursache (la cause), die Wirkung (l’effet).', 'Research: die Forschung, der Forscher / die Forscherin, die Studie (the study), der Versuch (the experiment), das Ergebnis (the result), die Ursache (the cause), die Wirkung (the effect).'),
        ('Verbes : untersuchen (examiner, étudier), entdecken (découvrir), beweisen (prouver), feststellen (constater), messen (mesurer), vermuten (supposer).', 'Verbs: untersuchen (to examine, to study), entdecken (to discover), beweisen (to prove), feststellen (to establish), messen (to measure), vermuten (to suppose).'),
        ('Présenter un résultat : Die Studie zeigt, dass… Die Forscher haben herausgefunden, dass… Es ist noch unklar, ob… Daraus lässt sich schließen, dass… (on peut en conclure que…).', 'Presenting a result: Die Studie zeigt, dass… Die Forscher haben herausgefunden, dass… Es ist noch unklar, ob… Daraus lässt sich schließen, dass… (it can be concluded that…).'),
      ], [
        D('forschung', 'die Forschung', ('la recherche (scientifique)', 'research')),
        D('studie', 'die Studie', ('l’étude', 'the study')),
        D('ergebnis', 'das Ergebnis', ('le résultat', 'the result')),
        D('ursache', 'die Ursache', ('la cause', 'the cause')),
        D('untersuchen', 'untersuchen', ('examiner, étudier', 'to examine, to investigate')),
        D('entdecken', 'entdecken', ('découvrir', 'to discover')),
        D('beweisen', 'beweisen', ('prouver', 'to prove')),
        D('herausfinden', 'herausfinden', ('découvrir, trouver (en cherchant)', 'to find out')),
        D('feststellen', 'feststellen', ('constater', 'to establish, to notice')),
      ], [
        x('Forscher haben in der Tiefsee Tiere entdeckt, die noch niemand gesehen hatte.', 'Des chercheurs ont découvert dans les abysses des animaux que personne n’avait encore vus.', 'Researchers have discovered creatures in the deep sea that nobody had seen before.'),
        x('Die Studie beweist nichts. Die Ursache ist noch unklar.', 'L’étude ne prouve rien. La cause n’est pas encore claire.', 'The study proves nothing. The cause is still unclear.'),
      ], [
        FB(COMPLETE, 'Die Forscher wollen die ＿ der Krankheit finden.', ['Ursache', 'Studie', 'Forschung'], 'Ursache', ('Ce qui provoque : die Ursache.', 'What brings it about: die Ursache.'), ('Les chercheurs veulent trouver la cause de la maladie.', 'The researchers want to find the cause of the disease.')),
        FB(COMPLETE, 'Das ＿ des Versuchs hat alle überrascht.', ['Ergebnis', 'Ursache', 'Wirkung'], 'Ergebnis', ('Le résultat : das Ergebnis (neutre).', 'The result: das Ergebnis (neuter).'), ('Le résultat de l’expérience a surpris tout le monde.', 'The result of the experiment surprised everyone.')),
        TF('Die Forscher vermuten, dass es einen Zusammenhang gibt, können es aber nicht beweisen.', ('Le lien est prouvé.', 'The link has been proved.'), FAUX, ('Vermuten = supposer ; nicht beweisen = ne pas prouver.', 'Vermuten = to suppose; nicht beweisen = not to prove.')),
        DC(ANSWER, [('Journalistin', 'Was haben Sie bei Ihrer Untersuchung herausgefunden?')], ('Une journaliste t’interroge sur ton étude (elle montre que le sommeil améliore la mémoire).', 'A journalist asks about your study (it shows that sleep improves memory).'), ['Unsere Studie zeigt, dass Schlaf das Gedächtnis verbessert.', 'Unsere Studie zeigt, dass verbessert Schlaf das Gedächtnis.', 'Wir haben entdeckt die Ursache beweisen.'], 'Unsere Studie zeigt, dass Schlaf das Gedächtnis verbessert.', ('Die Studie zeigt, dass + verbe à la fin.', 'Die Studie zeigt, dass + verb at the end.')),
      ]),
  ])])

# ═════════════════════════ 4 : Connecteurs doubles, conséquence, société ═════════════════════════
W4 = WORLD('goetheb2-w4', ('L’arène du Gant', 'The arena of the Glove'), REGION,
  ('Relier deux idées avec les connecteurs doubles, exprimer la conséquence, parler de la société et de ses valeurs.', 'Link two ideas with paired connectors, express consequence, talk about society and its values.'),
  (('Le Lion de l’arène', 'The Lion of the Arena'), '✠', ('Une dame a laissé tomber son gant entre les fauves pour éprouver son chevalier. Le Lion de l’arène attend : ni la peur ni l’orgueil ne t’aideront, seulement des phrases bien liées.', 'A lady has dropped her glove among the wild beasts to test her knight. The Lion of the Arena is waiting: neither fear nor pride will help you, only well-linked sentences.')),
  [CH('goetheb2-w4-c1', ('Ni peur ni orgueil', 'Neither fear nor pride'), [
    L('de-doppelkonnektoren', ('Les connecteurs doubles', 'Paired connectors'), ('Additionner, exclure, opposer ou proposer un choix en deux temps.', 'Add, exclude, contrast or offer a choice in two steps.'), 9, [
        ('Addition : sowohl… als auch (aussi bien… que), nicht nur… sondern auch (non seulement… mais aussi). Exclusion : weder… noch (ni… ni). Choix : entweder… oder (soit… soit).', 'Addition: sowohl… als auch (both… and), nicht nur… sondern auch (not only… but also). Exclusion: weder… noch (neither… nor). Choice: entweder… oder (either… or).'),
        ('Concession : zwar… aber (certes… mais). Opposition : einerseits… andererseits (d’un côté… de l’autre). Partage : teils… teils (en partie… en partie). Proportion : je + comparatif (verbe à la fin)…, desto / umso + comparatif (verbe en 2e position).', 'Concession: zwar… aber (admittedly… but). Contrast: einerseits… andererseits (on the one hand… on the other). Split: teils… teils (partly… partly). Proportion: je + comparative (verb at the end)…, desto / umso + comparative (verb second).'),
        ('Ordre des mots : entweder, zwar, einerseits et weder peuvent occuper la première place (verbe ensuite) : Entweder kommst du mit, oder du bleibst hier. Weder hat er angerufen, noch hat er geschrieben.', 'Word order: entweder, zwar, einerseits and weder can take first position (verb next): Entweder kommst du mit, oder du bleibst hier. Weder hat er angerufen, noch hat er geschrieben.'),
      ], [
        DG('sowohl-als-auch', 'sowohl … als auch', ('aussi bien… que', 'both… and')),
        DG('weder-noch', 'weder … noch', ('ni… ni', 'neither… nor')),
        DG('entweder-oder', 'entweder … oder', ('soit… soit', 'either… or')),
        DG('nicht-nur-sondern', 'nicht nur … sondern auch', ('non seulement… mais aussi', 'not only… but also')),
        DG('zwar-aber', 'zwar … aber', ('certes… mais', 'admittedly… but')),
        DG('teils-teils', 'teils … teils', ('en partie… en partie', 'partly… partly')),
        D('handschuh', 'der Handschuh', ('le gant', 'the glove')),
        D('ritter', 'der Ritter', ('le chevalier', 'the knight')),
        D('mutig', 'mutig', ('courageux', 'brave')),
      ], [
        x('Der Ritter zeigte weder Angst noch Stolz, als er den Handschuh holte.', 'Le chevalier ne montra ni peur ni orgueil en allant chercher le gant.', 'The knight showed neither fear nor pride as he fetched the glove.'),
        x('Er war zwar mutig, aber er wollte der Dame nicht mehr dienen.', 'Il était certes courageux, mais il ne voulait plus servir la dame.', 'He was brave, admittedly, but he no longer wanted to serve the lady.'),
      ], [
        FB(CHOOSE, 'Sie spricht sowohl Deutsch ＿ Französisch.', ['als auch', 'noch', 'oder'], 'als auch', ('Sowohl… als auch.', 'Sowohl… als auch.'), ('Elle parle aussi bien allemand que français.', 'She speaks both German and French.')),
        FB(CHOOSE, 'Ich habe weder Zeit ＿ Lust.', ['noch', 'oder', 'als auch'], 'noch', ('Weder… noch.', 'Weder… noch.'), ('Je n’ai ni le temps ni l’envie.', 'I have neither the time nor the inclination.')),
        FB(CHOOSE, 'Je mehr ich lerne, ＿ besser verstehe ich die Texte.', ['desto', 'als', 'so'], 'desto', ('Je… desto + comparatif.', 'Je… desto + comparative.'), ('Plus j’apprends, mieux je comprends les textes.', 'The more I learn, the better I understand the texts.')),
        order(('Remets dans l’ordre : « Soit tu viens avec nous, soit tu restes ici. »', 'Put in order: “Either you come with us, or you stay here.”'), ['Entweder', 'kommst', 'du', 'mit,', 'oder', 'du', 'bleibst', 'hier.'], ('Entweder en tête, verbe ensuite ; après oder, ordre normal.', 'Entweder first, then the verb; after oder, normal order.')),
      ]),
    L('de-konsekutiv', ('La conséquence : sodass, folglich, infolgedessen', 'Consequence: sodass, folglich, infolgedessen'), ('Tirer la conséquence d’un fait.', 'Draw the consequence of a fact.'), 8, [
        ('Sodass (si bien que) introduit une subordonnée, verbe à la fin : Es regnete stark, sodass das Fest ausfiel. Avec un adjectif : so + adjectif…, dass : Er war so müde, dass er sofort einschlief.', 'Sodass (so that) introduces a subordinate clause, verb at the end: Es regnete stark, sodass das Fest ausfiel. With an adjective: so + adjective…, dass: Er war so müde, dass er sofort einschlief.'),
        ('Adverbes de conséquence (verbe juste après) : folglich (par conséquent), infolgedessen (en conséquence), demnach (d’après cela), somit (ainsi), also (donc). Die Straße war gesperrt. Folglich kamen wir zu spät.', 'Adverbs of consequence (verb right after): folglich (consequently), infolgedessen (as a result), demnach (accordingly), somit (thus), also (so). Die Straße war gesperrt. Folglich kamen wir zu spät.'),
        ('Verbes et noms : führen zu (mener à), verursachen (causer), zur Folge haben (avoir pour conséquence), die Folge (la conséquence), die Auswirkung auf + accusatif (la répercussion sur).', 'Verbs and nouns: führen zu (to lead to), verursachen (to cause), zur Folge haben (to result in), die Folge (the consequence), die Auswirkung auf + accusative (the impact on).'),
      ], [
        DG('sodass', 'sodass', ('si bien que, de sorte que', 'so that (result)')),
        DG('so-dass', 'so + Adjektiv …, dass', ('si / tellement… que', 'so… that')),
        DG('folglich', 'folglich', ('par conséquent', 'consequently')),
        DG('infolgedessen', 'infolgedessen', ('en conséquence', 'as a result')),
        D('fuehren-zu', 'führen zu', ('mener à, conduire à', 'to lead to')),
        D('verursachen', 'verursachen', ('causer, provoquer', 'to cause')),
        D('zur-folge-haben', 'zur Folge haben', ('avoir pour conséquence', 'to result in')),
        D('auswirkung', 'die Auswirkung', ('la répercussion, l’effet', 'the impact, the effect')),
      ], [
        x('Die Dame war so stolz, dass sie das Leben des Ritters riskierte.', 'La dame était si orgueilleuse qu’elle risqua la vie du chevalier.', 'The lady was so proud that she risked the knight’s life.'),
        x('Er warf ihr den Handschuh ins Gesicht. Folglich verlor sie ihn für immer.', 'Il lui jeta le gant au visage. Par conséquent, elle le perdit pour toujours.', 'He threw the glove in her face. Consequently, she lost him for ever.'),
      ], [
        FB(CHOOSE, 'Der Zug hatte Verspätung, ＿ ich den Anschluss verpasste.', ['sodass', 'folglich', 'deshalb'], 'sodass', ('Verbe à la fin : subordonnée avec sodass.', 'Verb at the end: subordinate clause with sodass.'), ('Le train avait du retard, si bien que j’ai manqué la correspondance.', 'The train was late, so I missed my connection.')),
        FB(CHOOSE, 'Es war ＿ kalt, dass der See zufror.', ['so', 'sehr', 'zu'], 'so', ('So + adjectif…, dass.', 'So + adjective…, dass.'), ('Il faisait si froid que le lac a gelé.', 'It was so cold that the lake froze over.')),
        FB(CHOOSE, 'Die Preise sind gestiegen. ＿ kaufen die Leute weniger.', ['Folglich', 'Sodass', 'Weil'], 'Folglich', ('Adverbe en tête, verbe ensuite : folglich.', 'Adverb first, then the verb: folglich.'), ('Les prix ont augmenté. Par conséquent, les gens achètent moins.', 'Prices have risen. Consequently, people are buying less.')),
        FB(COMPLETE, 'Zu wenig Schlaf kann zu Krankheiten ＿.', ['führen', 'verursachen', 'folgen'], 'führen', ('Mener à : führen zu.', 'To lead to: führen zu.'), ('Le manque de sommeil peut mener à des maladies.', 'Too little sleep can lead to illness.')),
      ]),
  ]),
  CH('goetheb2-w4-c2', ('La cour et ses règles', 'The court and its rules'), [
    L('de-gesellschaft', ('La société et ses valeurs', 'Society and its values'), ('Parler de la vie en société, des inégalités et de l’engagement.', 'Talk about life in society, inequality and commitment.'), 8, [
        ('La société : die Gesellschaft, die Bevölkerung (la population), die Mehrheit / die Minderheit (la majorité / la minorité), die Generation, die Gleichberechtigung (l’égalité des droits), die Armut (la pauvreté), der Wohlstand (la prospérité).', 'Society: die Gesellschaft, die Bevölkerung (the population), die Mehrheit / die Minderheit (the majority / the minority), die Generation, die Gleichberechtigung (equal rights), die Armut (poverty), der Wohlstand (prosperity).'),
        ('S’engager : sich engagieren für, sich einsetzen für (s’investir pour), ehrenamtlich arbeiten (être bénévole), unterstützen (soutenir), benachteiligt sein (être défavorisé), der Respekt, die Würde (la dignité).', 'Getting involved: sich engagieren für, sich einsetzen für (to stand up for), ehrenamtlich arbeiten (to volunteer), unterstützen (to support), benachteiligt sein (to be disadvantaged), der Respekt, die Würde (dignity).'),
        ('Pour constater : Die Kluft zwischen Arm und Reich wächst (le fossé se creuse). Immer mehr Menschen… Im Vergleich zu früher… Der Anteil der… ist gestiegen / gesunken (la part de… a augmenté / baissé).', 'To state a fact: Die Kluft zwischen Arm und Reich wächst (the gap is widening). Immer mehr Menschen… Im Vergleich zu früher… Der Anteil der… ist gestiegen / gesunken (the share of… has risen / fallen).'),
      ], [
        D('gesellschaft', 'die Gesellschaft', ('la société', 'society')),
        D('bevoelkerung', 'die Bevölkerung', ('la population', 'the population')),
        D('mehrheit', 'die Mehrheit', ('la majorité', 'the majority')),
        D('gleichberechtigung', 'die Gleichberechtigung', ('l’égalité des droits', 'equal rights')),
        D('armut', 'die Armut', ('la pauvreté', 'poverty')),
        D('sich-einsetzen', 'sich einsetzen für', ('s’investir pour, défendre', 'to stand up for, to campaign for')),
        D('ehrenamtlich', 'ehrenamtlich', ('bénévole, bénévolement', 'voluntary, as a volunteer')),
        D('anteil', 'der Anteil', ('la part, la proportion', 'the share, the proportion')),
      ], [
        x('Sie setzt sich seit Jahren ehrenamtlich für benachteiligte Kinder ein.', 'Elle s’investit bénévolement depuis des années pour les enfants défavorisés.', 'She has been volunteering for disadvantaged children for years.'),
        x('Die Mehrheit der Bevölkerung ist für mehr Gleichberechtigung.', 'La majorité de la population est favorable à davantage d’égalité.', 'The majority of the population is in favour of more equality.'),
      ], [
        FB(CHOOSE, 'Er setzt sich ＿ den Schutz der Umwelt ein.', ['für', 'um', 'an'], 'für', ('Sich einsetzen für + accusatif.', 'Sich einsetzen für + accusative.'), ('Il s’engage pour la protection de l’environnement.', 'He campaigns for the protection of the environment.')),
        FB(COMPLETE, 'Der ＿ der Menschen über 65 steigt jedes Jahr.', ['Anteil', 'Armut', 'Mehrheit'], 'Anteil', ('La part : der Anteil.', 'The share: der Anteil.'), ('La part des personnes de plus de 65 ans augmente chaque année.', 'The share of people over 65 rises every year.')),
        TF('Nur eine Minderheit arbeitet ehrenamtlich, aber ihre Zahl wächst.', ('La plupart des gens sont bénévoles.', 'Most people volunteer.'), FAUX, ('Eine Minderheit = une minorité.', 'Eine Minderheit = a minority.')),
        DC(ANSWER, [('Moderator', 'Was halten Sie davon, dass junge Leute ein soziales Jahr machen sollen?')], ('Dans un débat, on te demande ton avis sur une année de service social (nuance ta réponse).', 'In a debate, you are asked your view on a year of community service (give a balanced answer).'), ['Einerseits ist es sinnvoll, andererseits sollte es freiwillig bleiben.', 'Einerseits ist es sinnvoll, noch sollte es freiwillig bleiben.', 'Weder es ist sinnvoll, als auch freiwillig.'], 'Einerseits ist es sinnvoll, andererseits sollte es freiwillig bleiben.', ('Einerseits… andererseits.', 'Einerseits… andererseits.')),
      ]),
  ])])

# ═════════════════════════ 5 : Participes épithètes, relatifs au génitif, la justice ═════════════════════════
W5 = WORLD('goetheb2-w5', ('Le théâtre des Grues', 'The theatre of the Cranes'), REGION,
  ('Condenser une relative avec un participe épithète, employer dessen et deren, parler de justice et de délits.', 'Condense a relative clause with a participle used as an adjective, use dessen and deren, talk about justice and offences.'),
  (('Les Grues d’Ibycus', 'The Cranes of Ibycus'), '❖', ('Le poète Ibycus a été tué sur la route, et seules les grues qui passaient l’ont vu. Les Grues d’Ibycus survolent maintenant le théâtre : désigne les coupables avec des phrases précises, et ils se trahiront.', 'The poet Ibycus was killed on the road, and only the passing cranes saw it. The Cranes of Ibycus now fly over the theatre: point out the culprits with precise sentences, and they will give themselves away.')),
  [CH('goetheb2-w5-c1', ('Les oiseaux qui passaient', 'The passing birds'), [
    L('de-partizip-adj', ('Les participes épithètes : fliegend, gestohlen', 'Participles as adjectives: fliegend, gestohlen'), ('Remplacer une relative par un participe placé devant le nom.', 'Replace a relative clause with a participle placed before the noun.'), 9, [
        ('Participe I = infinitif + d : fliegend, schlafend, lachend. Il exprime une action en cours et active : die fliegenden Kraniche (= die Kraniche, die fliegen). Il se décline comme un adjectif.', 'Participle I = infinitive + d: fliegend, schlafend, lachend. It expresses an ongoing, active action: die fliegenden Kraniche (= die Kraniche, die fliegen). It is declined like an adjective.'),
        ('Participe II devant le nom : action achevée, le plus souvent passive. Das gestohlene Geld (= das Geld, das gestohlen wurde). Der angekommene Zug (= der Zug, der angekommen ist).', 'Participle II before the noun: a completed action, usually passive. Das gestohlene Geld (= das Geld, das gestohlen wurde). Der angekommene Zug (= der Zug, der angekommen ist).'),
        ('À l’écrit, le participe peut porter des compléments, placés avant lui : die über das Theater fliegenden Kraniche ; der gestern von der Polizei verhaftete Mann. Tout le groupe se glisse entre l’article et le nom.', 'In writing, the participle can carry complements, placed before it: die über das Theater fliegenden Kraniche; der gestern von der Polizei verhaftete Mann. The whole group slots in between the article and the noun.'),
      ], [
        DG('partizip-1', 'Infinitiv + d (fliegend, lachend)', ('participe présent épithète (action en cours)', 'present participle as adjective (ongoing action)')),
        DG('partizip-2-attr', 'das gestohlene Geld', ('participe passé épithète (action achevée)', 'past participle as adjective (completed action)')),
        DG('partizip-erweitert', 'der von der Polizei verhaftete Mann', ('groupe participial étendu', 'extended participial phrase')),
        D('kranich', 'der Kranich', ('la grue (oiseau)', 'the crane (bird)')),
        D('stehlen', 'stehlen', ('voler, dérober', 'to steal')),
        D('verhaften', 'verhaften', ('arrêter (police)', 'to arrest')),
        D('schreien', 'schreien', ('crier', 'to shout, to scream')),
        D('dichter', 'der Dichter', ('le poète', 'the poet')),
      ], [
        x('Der sterbende Dichter rief die vorbeifliegenden Kraniche als Zeugen an.', 'Le poète mourant prit à témoin les grues qui passaient.', 'The dying poet called on the passing cranes as witnesses.'),
        x('Die von den Zuschauern gehörten Worte verrieten die beiden Mörder.', 'Les mots entendus par les spectateurs trahirent les deux meurtriers.', 'The words heard by the spectators gave the two murderers away.'),
      ], [
        FB(CHOOSE, 'Das ＿ Kind lag ruhig im Bett.', ['schlafende', 'geschlafene', 'schlafen'], 'schlafende', ('Action en cours : participe I, schlafend + e.', 'Ongoing action: participle I, schlafend + e.'), ('L’enfant endormi était tranquille dans son lit.', 'The sleeping child lay quietly in bed.')),
        FB(CHOOSE, 'Die Polizei hat das ＿ Auto gefunden.', ['gestohlene', 'stehlende', 'gestohlen'], 'gestohlene', ('Action achevée et passive : participe II décliné.', 'Completed, passive action: declined participle II.'), ('La police a retrouvé la voiture volée.', 'The police have found the stolen car.')),
        FB(CHOOSE, 'Die ＿ Preise machen vielen Familien Sorgen.', ['steigenden', 'gestiegenden', 'steigende'], 'steigenden', ('Participe I au pluriel avec article : steigenden.', 'Participle I in the plural with an article: steigenden.'), ('La hausse des prix inquiète beaucoup de familles.', 'Rising prices worry many families.')),
        TF('Der frisch gebackene Kuchen steht auf dem Tisch.', ('Le gâteau est encore au four.', 'The cake is still in the oven.'), FAUX, ('Gebacken = participe II, action achevée.', 'Gebacken = participle II, a completed action.')),
      ]),
    L('de-relativ-gen', ('Dont : dessen, deren ; wer…, der', 'Whose: dessen, deren; wer…, der'), ('Exprimer la possession dans une relative et généraliser avec wer.', 'Express possession in a relative clause and generalise with wer.'), 8, [
        ('Relatif au génitif : dessen (antécédent masculin ou neutre), deren (féminin ou pluriel). Der Dichter, dessen Lieder alle kannten… Die Stadt, deren Theater berühmt ist… Le nom qui suit n’a pas d’article.', 'Genitive relative: dessen (masculine or neuter antecedent), deren (feminine or plural). Der Dichter, dessen Lieder alle kannten… Die Stadt, deren Theater berühmt ist… The noun that follows has no article.'),
        ('Avec une préposition : Der Freund, mit dessen Auto wir fahren… Die Leute, in deren Haus wir wohnen… Le cas du nom dépend de la préposition, mais dessen / deren ne changent pas.', 'With a preposition: Der Freund, mit dessen Auto wir fahren… Die Leute, in deren Haus wir wohnen… The case of the noun depends on the preposition, but dessen / deren do not change.'),
        ('Relative sans antécédent : Wer das getan hat, (der) wird bestraft (quiconque a fait cela sera puni). Wen ich einmal gesehen habe, den vergesse ich nicht. Was man verspricht, (das) muss man halten.', 'Relative with no antecedent: Wer das getan hat, (der) wird bestraft (whoever did this will be punished). Wen ich einmal gesehen habe, den vergesse ich nicht. Was man verspricht, (das) muss man halten.'),
      ], [
        DG('dessen', 'dessen', ('dont (antécédent masculin ou neutre)', 'whose (masculine or neuter antecedent)')),
        DG('deren', 'deren', ('dont (antécédent féminin ou pluriel)', 'whose (feminine or plural antecedent)')),
        DG('wer-der', 'Wer …, der …', ('celui qui…, quiconque…', 'whoever…')),
        D('moerder', 'der Mörder', ('le meurtrier', 'the murderer')),
        D('opfer', 'das Opfer', ('la victime', 'the victim')),
        D('sich-verraten', 'sich verraten', ('se trahir', 'to give oneself away')),
        D('zuschauer', 'der Zuschauer', ('le spectateur', 'the spectator')),
        D('schuld', 'die Schuld', ('la faute, la culpabilité', 'guilt, fault')),
      ], [
        x('Der Dichter, dessen Stimme ganz Griechenland liebte, kam nie in Korinth an.', 'Le poète, dont toute la Grèce aimait la voix, n’arriva jamais à Corinthe.', 'The poet, whose voice all Greece loved, never arrived in Corinth.'),
        x('Wer eine Schuld trägt, der verrät sich früher oder später.', 'Celui qui porte une faute se trahit tôt ou tard.', 'Whoever bears guilt gives himself away sooner or later.'),
      ], [
        FB(CHOOSE, 'Das ist die Frau, ＿ Sohn in Berlin studiert.', ['deren', 'dessen', 'der'], 'deren', ('Antécédent féminin : deren.', 'Feminine antecedent: deren.'), ('C’est la femme dont le fils étudie à Berlin.', 'That is the woman whose son studies in Berlin.')),
        FB(CHOOSE, 'Der Mann, ＿ Auto gestohlen wurde, rief die Polizei.', ['dessen', 'deren', 'dem'], 'dessen', ('Antécédent masculin : dessen.', 'Masculine antecedent: dessen.'), ('L’homme dont la voiture a été volée a appelé la police.', 'The man whose car was stolen called the police.')),
        FB(CHOOSE, '＿ zu spät kommt, den bestraft das Leben.', ['Wer', 'Der', 'Wen'], 'Wer', ('Sujet de la relative : wer.', 'Subject of the relative clause: wer.'), ('Celui qui arrive trop tard est puni par la vie.', 'Life punishes those who come too late.')),
        FB(CHOOSE, 'Die Nachbarn, mit ＿ Kindern unsere Tochter spielt, ziehen um.', ['deren', 'dessen', 'denen'], 'deren', ('Antécédent pluriel, possession : deren.', 'Plural antecedent, possession: deren.'), ('Les voisins, avec les enfants desquels notre fille joue, déménagent.', 'The neighbours whose children our daughter plays with are moving.')),
      ]),
  ]),
  CH('goetheb2-w5-c2', ('Le tribunal du théâtre', 'The court in the theatre'), [
    L('de-recht', ('La justice et les délits', 'Justice and offences'), ('Parler d’un délit, d’une enquête et d’un jugement.', 'Talk about an offence, an investigation and a verdict.'), 8, [
        ('Le délit : das Verbrechen (le crime), der Diebstahl (le vol), der Betrug (l’escroquerie), der Täter (l’auteur), der Verdächtige (le suspect). L’enquête : ermitteln (enquêter), der Beweis (la preuve), die Spur (la piste, la trace).', 'The offence: das Verbrechen (the crime), der Diebstahl (theft), der Betrug (fraud), der Täter (the perpetrator), der Verdächtige (the suspect). The investigation: ermitteln (to investigate), der Beweis (the evidence), die Spur (the lead, the trace).'),
        ('Le procès : das Gericht (le tribunal), der Richter (le juge), der Anwalt (l’avocat), anklagen (accuser), gestehen (avouer), verurteilen zu (condamner à), die Strafe (la peine), freisprechen (acquitter).', 'The trial: das Gericht (the court), der Richter (the judge), der Anwalt (the lawyer), anklagen (to charge), gestehen (to confess), verurteilen zu (to sentence to), die Strafe (the penalty), freisprechen (to acquit).'),
        ('La loi : das Gesetz (la loi), das Recht (le droit), gegen das Gesetz verstoßen (enfreindre la loi), schuldig / unschuldig (coupable / innocent), gerecht / ungerecht (juste / injuste).', 'The law: das Gesetz (the law), das Recht (the right, law), gegen das Gesetz verstoßen (to break the law), schuldig / unschuldig (guilty / innocent), gerecht / ungerecht (just / unjust).'),
      ], [
        D('verbrechen', 'das Verbrechen', ('le crime', 'the crime')),
        D('taeter', 'der Täter', ('l’auteur (d’un délit), le coupable', 'the perpetrator')),
        D('beweis', 'der Beweis', ('la preuve', 'the evidence, the proof')),
        D('gericht-justiz', 'das Gericht (Justiz)', ('le tribunal', 'the court (of law)')),
        D('richter', 'der Richter', ('le juge', 'the judge')),
        D('gestehen', 'gestehen', ('avouer', 'to confess')),
        D('verurteilen', 'verurteilen', ('condamner', 'to sentence, to convict')),
        D('gesetz', 'das Gesetz', ('la loi', 'the law')),
        D('unschuldig', 'unschuldig', ('innocent', 'innocent')),
      ], [
        x('Ohne Beweise konnte das Gericht die Täter nicht verurteilen.', 'Sans preuves, le tribunal ne pouvait pas condamner les coupables.', 'Without evidence, the court could not convict the perpetrators.'),
        x('Vor allen Zuschauern gestanden die Mörder ihr Verbrechen.', 'Devant tous les spectateurs, les meurtriers avouèrent leur crime.', 'In front of all the spectators, the murderers confessed their crime.'),
      ], [
        FB(COMPLETE, 'Der Richter hat den Täter zu drei Jahren Gefängnis ＿.', ['verurteilt', 'gestanden', 'ermittelt'], 'verurteilt', ('Condamner à : verurteilen zu.', 'To sentence to: verurteilen zu.'), ('Le juge a condamné le coupable à trois ans de prison.', 'The judge sentenced the perpetrator to three years in prison.')),
        FB(COMPLETE, 'Die Polizei hat keine ＿, also muss sie den Mann freilassen.', ['Beweise', 'Gesetze', 'Richter'], 'Beweise', ('Les preuves : die Beweise.', 'Evidence: die Beweise.'), ('La police n’a pas de preuves, elle doit donc relâcher l’homme.', 'The police have no evidence, so they must release the man.')),
        TF('Der Angeklagte wurde freigesprochen, weil er unschuldig war.', ('L’accusé est allé en prison.', 'The accused went to prison.'), FAUX, ('Freisprechen = acquitter.', 'Freisprechen = to acquit.')),
        DC(ANSWER, [('Polizist', 'Haben Sie gesehen, wer das Fahrrad gestohlen hat?')], ('Un policier te demande si tu as vu le voleur (tu as vu un homme dont la veste était rouge).', 'A police officer asks whether you saw the thief (you saw a man whose jacket was red).'), ['Ja, einen Mann, dessen Jacke rot war.', 'Ja, einen Mann, deren Jacke rot war.', 'Ja, ein Mann, der Jacke rot war.'], 'Ja, einen Mann, dessen Jacke rot war.', ('Antécédent masculin : dessen.', 'Masculine antecedent: dessen.')),
      ]),
  ])])

# ═════════════════════════ 6 : Locutions verbales, style nominal, le monde du travail ═════════════════════════
W6 = WORLD('goetheb2-w6', ('La forêt du Chasseur sauvage', 'The Wild Huntsman’s forest'), REGION,
  ('Employer les locutions verbales de la langue soignée, passer du verbe au nom, parler du monde du travail.', 'Use the verb-noun phrases of formal German, turn verbs into nouns, talk about the world of work.'),
  (('Le Chasseur sauvage', 'The Wild Huntsman'), '✺', ('Un comte chassait le dimanche sans égard pour personne ; il est devenu le Chasseur sauvage, condamné à courir jusqu’à la fin des temps. Pour l’arrêter, prends une décision, pose une question, tiens compte des autres : tout se dit avec les bons verbes.', 'A count hunted on Sundays with no regard for anyone; he became the Wild Huntsman, doomed to ride until the end of time. To stop him, make a decision, ask a question, take others into account: it is all said with the right verbs.')),
  [CH('goetheb2-w6-c1', ('Prendre une décision', 'Making a decision'), [
    L('de-nomen-verb', ('Les locutions verbales : eine Entscheidung treffen', 'Verb-noun phrases: eine Entscheidung treffen'), ('Employer les associations fixes d’un nom et d’un verbe.', 'Use fixed combinations of a noun and a verb.'), 9, [
        ('Dans la langue soignée, un verbe simple est souvent remplacé par nom + verbe : entscheiden → eine Entscheidung treffen ; fragen → eine Frage stellen ; antworten → eine Antwort geben ; kritisieren → Kritik üben an.', 'In formal German, a simple verb is often replaced by noun + verb: entscheiden → eine Entscheidung treffen; fragen → eine Frage stellen; antworten → eine Antwort geben; kritisieren → Kritik üben an.'),
        ('Avec préposition : in Frage kommen (entrer en ligne de compte), zur Verfügung stehen (être à disposition), in Anspruch nehmen (avoir recours à), Rücksicht nehmen auf (tenir compte de), Einfluss haben auf (avoir de l’influence sur).', 'With a preposition: in Frage kommen (to be an option), zur Verfügung stehen (to be available), in Anspruch nehmen (to make use of), Rücksicht nehmen auf (to show consideration for), Einfluss haben auf (to have influence on).'),
        ('Le verbe perd son sens propre : treffen ne veut plus dire rencontrer, stellen ne veut plus dire poser debout. Il faut apprendre le couple entier : einen Antrag stellen (déposer une demande), eine Rolle spielen (jouer un rôle).', 'The verb loses its own meaning: treffen no longer means to meet, stellen no longer means to stand something up. The whole pair must be learnt: einen Antrag stellen (to submit an application), eine Rolle spielen (to play a part).'),
      ], [
        D('entscheidung-treffen', 'eine Entscheidung treffen', ('prendre une décision', 'to make a decision')),
        D('frage-stellen', 'eine Frage stellen', ('poser une question', 'to ask a question')),
        D('in-frage-kommen', 'in Frage kommen', ('entrer en ligne de compte', 'to be an option, to be considered')),
        D('zur-verfuegung', 'zur Verfügung stehen', ('être à disposition', 'to be available')),
        D('ruecksicht-nehmen', 'Rücksicht nehmen auf', ('tenir compte de, ménager', 'to show consideration for')),
        D('in-anspruch-nehmen', 'in Anspruch nehmen', ('avoir recours à, faire appel à', 'to avail oneself of')),
        D('rolle-spielen', 'eine Rolle spielen', ('jouer un rôle', 'to play a part, to matter')),
        D('antrag-stellen', 'einen Antrag stellen', ('déposer une demande', 'to submit an application')),
        D('kritik-ueben', 'Kritik üben an', ('critiquer', 'to criticise')),
      ], [
        x('Der Graf nahm auf niemanden Rücksicht: weder auf die Bauern noch auf die Tiere.', 'Le comte n’avait d’égard pour personne : ni pour les paysans ni pour les bêtes.', 'The count showed consideration for no one: neither the peasants nor the animals.'),
        x('Er musste eine Entscheidung treffen, aber Umkehren kam für ihn nicht in Frage.', 'Il devait prendre une décision, mais faire demi-tour était exclu pour lui.', 'He had to make a decision, but turning back was out of the question for him.'),
      ], [
        FB(CHOOSE, 'Wir müssen heute eine Entscheidung ＿.', ['treffen', 'machen', 'nehmen'], 'treffen', ('Eine Entscheidung treffen.', 'Eine Entscheidung treffen.'), ('Nous devons prendre une décision aujourd’hui.', 'We have to make a decision today.')),
        FB(CHOOSE, 'Darf ich Ihnen eine Frage ＿?', ['stellen', 'geben', 'machen'], 'stellen', ('Eine Frage stellen.', 'Eine Frage stellen.'), ('Puis-je vous poser une question ?', 'May I ask you a question?')),
        FB(CHOOSE, 'Bitte nehmen Sie Rücksicht ＿ die Nachbarn.', ['auf', 'für', 'an'], 'auf', ('Rücksicht nehmen auf + accusatif.', 'Rücksicht nehmen auf + accusative.'), ('Veuillez avoir des égards pour les voisins.', 'Please show consideration for the neighbours.')),
        FB(CHOOSE, 'Der Raum ＿ Ihnen den ganzen Tag zur Verfügung.', ['steht', 'stellt', 'kommt'], 'steht', ('Zur Verfügung stehen.', 'Zur Verfügung stehen.'), ('La salle est à votre disposition toute la journée.', 'The room is available to you all day.')),
      ]),
    L('de-nominalisierung', ('Du verbe au nom : le style nominal', 'From verb to noun: nominal style'), ('Comprendre et former les noms tirés de verbes et d’adjectifs.', 'Understand and form nouns derived from verbs and adjectives.'), 8, [
        ('L’infinitif devient un nom neutre : das Lesen, das Reisen, beim Essen (en mangeant), zum Arbeiten (pour travailler). Suffixes fréquents : -ung (die Entwicklung, féminin), -heit / -keit (die Freiheit, die Möglichkeit), -schaft (die Wissenschaft).', 'The infinitive becomes a neuter noun: das Lesen, das Reisen, beim Essen (while eating), zum Arbeiten (for working). Common suffixes: -ung (die Entwicklung, feminine), -heit / -keit (die Freiheit, die Möglichkeit), -schaft (die Wissenschaft).'),
        ('Le style nominal condense une subordonnée : Weil die Preise steigen… → Wegen des Anstiegs der Preise… ; Nachdem er angekommen war… → Nach seiner Ankunft… ; Obwohl es regnete… → Trotz des Regens…', 'Nominal style condenses a subordinate clause: Weil die Preise steigen… → Wegen des Anstiegs der Preise… ; Nachdem er angekommen war… → Nach seiner Ankunft… ; Obwohl es regnete… → Trotz des Regens…'),
        ('Le sujet ou l’objet du verbe passe au génitif ou avec von : die Entwicklung der Technik, die Lösung des Problems, der Bau von Wohnungen. Ce style domine dans les textes administratifs et scientifiques.', 'The subject or object of the verb goes into the genitive or takes von: die Entwicklung der Technik, die Lösung des Problems, der Bau von Wohnungen. This style dominates administrative and scientific texts.'),
      ], [
        DG('nominalisierter-infinitiv', 'das Lesen / beim Essen', ('infinitif substantivé', 'infinitive used as a noun')),
        DG('ung', '-ung (die Entwicklung)', ('suffixe -ung : nom féminin d’action', 'suffix -ung: feminine noun of action')),
        DG('heit-keit', '-heit / -keit (die Freiheit)', ('suffixes -heit / -keit : nom féminin de qualité', 'suffixes -heit / -keit: feminine noun of quality')),
        D('entwicklung', 'die Entwicklung', ('le développement, l’évolution', 'development')),
        D('anstieg', 'der Anstieg', ('la hausse', 'the rise, the increase')),
        D('rueckgang', 'der Rückgang', ('la baisse, le recul', 'the decline, the drop')),
        D('ankunft', 'die Ankunft', ('l’arrivée', 'the arrival')),
        D('loesung', 'die Lösung', ('la solution', 'the solution')),
      ], [
        x('Nach der Ankunft des Jägers flohen alle Tiere aus dem Wald.', 'Après l’arrivée du chasseur, toutes les bêtes s’enfuirent de la forêt.', 'After the huntsman’s arrival, all the animals fled the forest.'),
        x('Beim Jagen vergaß der Graf alles: die Zeit, die Menschen und den Sonntag.', 'En chassant, le comte oubliait tout : le temps, les hommes et le dimanche.', 'While hunting, the count forgot everything: time, people and Sunday.'),
      ], [
        FB(CHOOSE, '＿ Essen sollte man nicht aufs Handy schauen.', ['Beim', 'Zum', 'Im'], 'Beim', ('Pendant l’action : beim + infinitif substantivé.', 'During the action: beim + infinitive used as a noun.'), ('En mangeant, on ne devrait pas regarder son téléphone.', 'You should not look at your phone while eating.')),
        FB(CHOOSE, 'Die ＿ der Technik ist nicht aufzuhalten.', ['Entwicklung', 'Entwickeln', 'Entwickelte'], 'Entwicklung', ('Nom d’action en -ung.', 'Noun of action in -ung.'), ('Le développement de la technique ne peut pas être arrêté.', 'The development of technology cannot be stopped.')),
        FB(CHOOSE, 'Trotz ＿ sind wir spazieren gegangen.', ['des Regens', 'es regnete', 'der Regen'], 'des Regens', ('Trotz + génitif.', 'Trotz + genitive.'), ('Malgré la pluie, nous sommes allés nous promener.', 'Despite the rain, we went for a walk.')),
        TF('Der Rückgang der Arbeitslosigkeit freut die Regierung.', ('Le chômage a augmenté.', 'Unemployment has risen.'), FAUX, ('Der Rückgang = la baisse.', 'Der Rückgang = the decline.')),
      ]),
  ]),
  CH('goetheb2-w6-c2', ('Sans repos', 'Without rest'), [
    L('de-arbeitswelt', ('Le monde du travail', 'The world of work'), ('Parler de ses conditions de travail, d’une candidature et de sa carrière.', 'Talk about working conditions, an application and a career.'), 8, [
        ('Le poste : die Stelle (le poste), die Bewerbung (la candidature), der Lebenslauf (le CV), das Vorstellungsgespräch (l’entretien), das Gehalt (le salaire), befristet / unbefristet (à durée déterminée / indéterminée), die Probezeit (la période d’essai).', 'The job: die Stelle (the position), die Bewerbung (the application), der Lebenslauf (the CV), das Vorstellungsgespräch (the interview), das Gehalt (the salary), befristet / unbefristet (fixed-term / permanent), die Probezeit (the probation period).'),
        ('Les conditions : die Überstunden (les heures supplémentaires), die Teilzeit / die Vollzeit, das Homeoffice (le télétravail), die Gewerkschaft (le syndicat), kündigen (démissionner, licencier), befördert werden (être promu).', 'Conditions: die Überstunden (overtime), die Teilzeit / die Vollzeit, das Homeoffice (working from home), die Gewerkschaft (the trade union), kündigen (to resign, to dismiss), befördert werden (to be promoted).'),
        ('En entretien : Ich bringe Erfahrung in… mit. Zu meinen Stärken gehört… Ich bin belastbar (résistant au stress), teamfähig (apte au travail d’équipe) und zuverlässig (fiable). Ich könnte ab dem ersten Mai anfangen.', 'In an interview: Ich bringe Erfahrung in… mit. Zu meinen Stärken gehört… Ich bin belastbar (resilient), teamfähig (a team player) und zuverlässig (reliable). Ich könnte ab dem ersten Mai anfangen.'),
      ], [
        D('gewerkschaft', 'die Gewerkschaft', ('le syndicat', 'the trade union')),
        D('probezeit', 'die Probezeit', ('la période d’essai', 'the probation period')),
        D('gehalt', 'das Gehalt', ('le salaire', 'the salary')),
        D('ueberstunden', 'die Überstunden', ('les heures supplémentaires', 'overtime')),
        D('befristet', 'befristet', ('à durée déterminée', 'fixed-term, temporary')),
        D('kuendigen', 'kündigen', ('démissionner ; licencier ; résilier', 'to resign; to dismiss; to cancel')),
        D('zuverlaessig', 'zuverlässig', ('fiable', 'reliable')),
        D('belastbar', 'belastbar', ('résistant au stress', 'resilient, able to work under pressure')),
      ], [
        x('Sie hat gekündigt, weil sie jede Woche zehn Überstunden machen musste.', 'Elle a démissionné parce qu’elle devait faire dix heures supplémentaires par semaine.', 'She resigned because she had to do ten hours of overtime every week.'),
        x('Die Stelle ist auf zwei Jahre befristet, aber das Gehalt ist gut.', 'Le poste est limité à deux ans, mais le salaire est bon.', 'The position is limited to two years, but the salary is good.'),
      ], [
        FB(COMPLETE, 'Zur Bewerbung gehören ein Anschreiben und ein ＿.', ['Lebenslauf', 'Gehalt', 'Vorstellungsgespräch'], 'Lebenslauf', ('Le CV : der Lebenslauf.', 'The CV: der Lebenslauf.'), ('Une candidature comprend une lettre de motivation et un CV.', 'An application includes a covering letter and a CV.')),
        FB(COMPLETE, 'Mein Vertrag ist ＿: Er endet im Dezember.', ['befristet', 'belastbar', 'zuverlässig'], 'befristet', ('À durée déterminée : befristet.', 'Fixed-term: befristet.'), ('Mon contrat est à durée déterminée : il se termine en décembre.', 'My contract is fixed-term: it ends in December.')),
        TF('Er arbeitet Teilzeit, damit er mehr Zeit für seine Kinder hat.', ('Il travaille à temps plein.', 'He works full time.'), FAUX, ('Teilzeit = temps partiel.', 'Teilzeit = part time.')),
        DC(ANSWER, [('Personalchefin', 'Warum sollten wir gerade Sie einstellen?')], ('En entretien, la DRH te demande pourquoi t’embaucher (mets en avant ton expérience et ta fiabilité).', 'In an interview, the HR manager asks why they should hire you (stress your experience and reliability).'), ['Ich bringe fünf Jahre Erfahrung mit und bin sehr zuverlässig.', 'Ich bringe fünf Jahre Erfahrung und bin sehr befristet.', 'Ich habe gekündigt eine Entscheidung zuverlässig.'], 'Ich bringe fünf Jahre Erfahrung mit und bin sehr zuverlässig.', ('Erfahrung mitbringen ; zuverlässig.', 'Erfahrung mitbringen; zuverlässig.')),
      ]),
  ])])

# ═════════════════════════ 7 : Supposer, poser des conditions, l'équilibre ═════════════════════════
W7 = WORLD('goetheb2-w7', ('Le lac de l’Ondine', 'The Undine’s lake'), REGION,
  ('Exprimer une supposition avec les verbes de modalité, poser des conditions avec falls et sofern, parler de stress et d’équilibre.', 'Express a supposition with modal verbs, set conditions with falls and sofern, talk about stress and balance.'),
  (('L’Ondine', 'The Undine'), '⚘', ('Au bord de l’eau, le pêcheur regarde sa ligne, et l’Ondine sort des vagues en chantant. Elle doit bien vouloir quelque chose, elle pourrait dire vrai… Pèse chaque supposition, pose tes conditions, et garde ton calme.', 'By the water, the fisherman watches his line, and the Undine rises from the waves, singing. She must want something, she might be telling the truth… Weigh every supposition, set your conditions, and keep calm.')),
  [CH('goetheb2-w7-c1', ('Elle doit bien savoir…', 'She must know…'), [
    L('de-modal-subjektiv', ('Supposer : müsste, dürfte, könnte, wird wohl', 'Supposing: müsste, dürfte, könnte, wird wohl'), ('Exprimer le degré de certitude d’une supposition.', 'Express how certain a supposition is.'), 9, [
        ('Du plus sûr au moins sûr : Er muss krank sein (j’en suis sûr). Er müsste zu Hause sein (très probable). Er dürfte etwa vierzig sein (probable). Er könnte / kann im Büro sein (possible). Er kann nicht der Täter sein (impossible).', 'From most to least certain: Er muss krank sein (I am sure). Er müsste zu Hause sein (very likely). Er dürfte etwa vierzig sein (probable). Er könnte / kann im Büro sein (possible). Er kann nicht der Täter sein (impossible).'),
        ('Le futur exprime aussi une supposition sur le présent, souvent avec wohl : Sie wird wohl noch schlafen (elle dort sans doute encore). Er wird im Stau stehen (il doit être dans les bouchons).', 'The future also expresses a supposition about the present, often with wohl: Sie wird wohl noch schlafen (she is probably still asleep). Er wird im Stau stehen (he must be stuck in traffic).'),
        ('Supposition sur le passé : modal + participe + haben / sein. Er muss den Zug verpasst haben (il a dû manquer le train). Sie könnte es vergessen haben. Er wird schon gegangen sein.', 'Supposition about the past: modal + participle + haben / sein. Er muss den Zug verpasst haben (he must have missed the train). Sie könnte es vergessen haben. Er wird schon gegangen sein.'),
      ], [
        DG('muss-vermutung', 'Er muss … sein.', ('Il doit être… (quasi-certitude)', 'He must be… (near certainty)')),
        DG('duerfte', 'Er dürfte … sein.', ('Il doit être…, sans doute (probabilité)', 'He is probably… (probability)')),
        DG('koennte-vermutung', 'Er könnte … sein.', ('Il pourrait être… (possibilité)', 'He could be… (possibility)')),
        DG('wird-wohl', 'Er wird wohl … (Futur)', ('Il… sans doute (supposition au futur)', 'He is probably… (future of supposition)')),
        DG('muss-haben', 'Er muss … verpasst haben.', ('Il a dû… (supposition sur le passé)', 'He must have… (supposition about the past)')),
        D('vermutlich', 'vermutlich', ('probablement', 'presumably')),
        D('wahrscheinlich', 'wahrscheinlich', ('vraisemblablement, probablement', 'probably, likely')),
        D('zweifeln', 'zweifeln an', ('douter de', 'to doubt')),
      ], [
        x('Das Wasser dürfte hier sehr tief sein. Der Fischer muss das wissen.', 'L’eau doit être très profonde ici. Le pêcheur le sait forcément.', 'The water is probably very deep here. The fisherman must know that.'),
        x('Niemand hat ihn je wieder gesehen. Er wird ihr wohl gefolgt sein.', 'Personne ne l’a jamais revu. Il l’aura sans doute suivie.', 'Nobody ever saw him again. He will probably have followed her.'),
      ], [
        FB(CHOOSE, 'Das Licht ist an. Sie ＿ zu Hause sein, da bin ich sicher.', ['muss', 'könnte', 'darf'], 'muss', ('Certitude : muss.', 'Certainty: muss.'), ('La lumière est allumée. Elle doit être chez elle, j’en suis sûr.', 'The light is on. She must be at home, I am sure.')),
        FB(CHOOSE, 'Er ist noch nicht da. Er ＿ den Bus verpasst haben, aber ich weiß es nicht.', ['könnte', 'muss', 'soll'], 'könnte', ('Simple possibilité : könnte.', 'A mere possibility: könnte.'), ('Il n’est pas encore là. Il a peut-être manqué le bus, mais je n’en sais rien.', 'He is not here yet. He could have missed the bus, but I do not know.')),
        FB(CHOOSE, 'Sie ＿ wohl noch im Büro sein.', ['wird', 'würde', 'wurde'], 'wird', ('Futur de supposition : wird wohl.', 'Future of supposition: wird wohl.'), ('Elle est sans doute encore au bureau.', 'She is probably still at the office.')),
        TF('Das kann nicht stimmen.', ('La personne pense que c’est probablement vrai.', 'The speaker thinks it is probably true.'), FAUX, ('Kann nicht = impossible.', 'Kann nicht = impossible.')),
      ]),
    L('de-konditional', ('Poser des conditions : falls, sofern, es sei denn', 'Setting conditions: falls, sofern, es sei denn'), ('Nuancer une condition au-delà de wenn.', 'Qualify a condition beyond wenn.'), 8, [
        ('Falls (au cas où) pour une condition incertaine : Falls es regnet, bleiben wir hier. Sofern / solange (pour autant que, tant que) : Sofern nichts dazwischenkommt, komme ich.', 'Falls (in case) for an uncertain condition: Falls es regnet, bleiben wir hier. Sofern / solange (provided that, as long as): Sofern nichts dazwischenkommt, komme ich.'),
        ('Es sei denn, … (à moins que) est suivi d’une principale : Ich komme, es sei denn, ich muss arbeiten. Vorausgesetzt, (dass)… (à condition que) : Vorausgesetzt, dass alle einverstanden sind…', 'Es sei denn, … (unless) is followed by a main clause: Ich komme, es sei denn, ich muss arbeiten. Vorausgesetzt, (dass)… (provided that): Vorausgesetzt, dass alle einverstanden sind…'),
        ('Avec un nom : bei + datif (Bei Regen fällt das Fest aus), ohne + accusatif (Ohne deine Hilfe hätte ich es nicht geschafft), im Falle + génitif (im Falle eines Unfalls). Sonst / andernfalls = sinon.', 'With a noun: bei + dative (Bei Regen fällt das Fest aus), ohne + accusative (Ohne deine Hilfe hätte ich es nicht geschafft), im Falle + genitive (im Falle eines Unfalls). Sonst / andernfalls = otherwise.'),
      ], [
        DG('falls', 'falls', ('au cas où, si jamais', 'in case, if')),
        DG('sofern', 'sofern', ('pour autant que, si', 'provided that, as long as')),
        DG('es-sei-denn', 'es sei denn, …', ('à moins que', 'unless')),
        DG('vorausgesetzt', 'vorausgesetzt, (dass) …', ('à condition que', 'provided that')),
        DG('bei-bedingung', 'bei + Dativ (Bedingung)', ('en cas de', 'in the event of')),
        D('andernfalls', 'andernfalls', ('sinon, dans le cas contraire', 'otherwise')),
        D('bedingung', 'die Bedingung', ('la condition', 'the condition')),
        D('voraussetzung', 'die Voraussetzung', ('la condition préalable', 'the prerequisite')),
      ], [
        x('Falls du ihr Lied hörst, halte dir die Ohren zu, andernfalls bist du verloren.', 'Si jamais tu entends son chant, bouche-toi les oreilles, sinon tu es perdu.', 'If you hear her song, cover your ears, otherwise you are lost.'),
        x('Sie lässt dich gehen, es sei denn, du schaust ihr in die Augen.', 'Elle te laisse partir, à moins que tu ne la regardes dans les yeux.', 'She lets you go, unless you look into her eyes.'),
      ], [
        FB(CHOOSE, '＿ Sie Fragen haben, rufen Sie uns bitte an.', ['Falls', 'Es sei denn', 'Andernfalls'], 'Falls', ('Condition incertaine, verbe à la fin : falls.', 'Uncertain condition, verb at the end: falls.'), ('Au cas où vous auriez des questions, appelez-nous.', 'In case you have any questions, please call us.')),
        FB(CHOOSE, 'Wir fahren morgen ans Meer, ＿, das Wetter ist schlecht.', ['es sei denn', 'falls', 'sofern'], 'es sei denn', ('À moins que + principale : es sei denn.', 'Unless + main clause: es sei denn.'), ('Nous allons à la mer demain, à moins qu’il ne fasse mauvais.', 'We are going to the seaside tomorrow, unless the weather is bad.')),
        FB(CHOOSE, '＿ Regen findet das Konzert in der Halle statt.', ['Bei', 'Falls', 'Wenn'], 'Bei', ('Devant un nom : bei + datif.', 'Before a noun: bei + dative.'), ('En cas de pluie, le concert a lieu dans la salle.', 'In the event of rain, the concert takes place in the hall.')),
        FB(CHOOSE, 'Beeil dich, ＿ verpassen wir den Zug.', ['andernfalls', 'falls', 'sofern'], 'andernfalls', ('Sinon : andernfalls / sonst.', 'Otherwise: andernfalls / sonst.'), ('Dépêche-toi, sinon nous allons manquer le train.', 'Hurry up, otherwise we will miss the train.')),
      ]),
  ]),
  CH('goetheb2-w7-c2', ('Le calme de l’eau', 'The calm of the water'), [
    L('de-psyche', ('Le stress et l’équilibre', 'Stress and balance'), ('Parler de la pression, de la fatigue et de ce qui fait du bien.', 'Talk about pressure, tiredness and what does you good.'), 8, [
        ('La pression : der Stress, der Druck (la pression), unter Druck stehen (être sous pression), überfordert sein (être dépassé), erschöpft (épuisé), die Belastung (la charge), der Leistungsdruck (la pression du résultat).', 'Pressure: der Stress, der Druck (pressure), unter Druck stehen (to be under pressure), überfordert sein (to be overwhelmed), erschöpft (exhausted), die Belastung (the strain), der Leistungsdruck (pressure to perform).'),
        ('Se ressourcer : sich erholen (se reposer, récupérer), abschalten (décrocher), sich entspannen (se détendre), die Ausgeglichenheit (l’équilibre), auf sich achten (prendre soin de soi), die Gewohnheit (l’habitude).', 'Recharging: sich erholen (to recover), abschalten (to switch off), sich entspannen (to relax), die Ausgeglichenheit (balance), auf sich achten (to look after oneself), die Gewohnheit (the habit).'),
        ('Conseiller avec tact : An deiner Stelle würde ich… (à ta place). Es würde dir guttun, … zu… (cela te ferait du bien de…). Du solltest dir mehr Zeit für dich nehmen. Hast du schon einmal daran gedacht, … zu…?', 'Advising tactfully: An deiner Stelle würde ich… (in your place). Es würde dir guttun, … zu… (it would do you good to…). Du solltest dir mehr Zeit für dich nehmen. Hast du schon einmal daran gedacht, … zu…?'),
      ], [
        D('druck', 'der Druck', ('la pression', 'pressure')),
        D('ueberfordert', 'überfordert', ('dépassé, débordé', 'overwhelmed, overstretched')),
        D('erschoepft', 'erschöpft', ('épuisé', 'exhausted')),
        D('sich-erholen', 'sich erholen', ('se reposer, récupérer', 'to recover, to rest')),
        D('abschalten', 'abschalten', ('décrocher ; éteindre', 'to switch off')),
        D('guttun', 'guttun', ('faire du bien', 'to do (someone) good')),
        D('gewohnheit', 'die Gewohnheit', ('l’habitude', 'the habit')),
        D('ausgeglichen', 'ausgeglichen', ('équilibré, serein', 'well-balanced, even-tempered')),
      ], [
        x('Seit Monaten steht sie unter Druck und kann abends nicht mehr abschalten.', 'Depuis des mois, elle est sous pression et n’arrive plus à décrocher le soir.', 'She has been under pressure for months and can no longer switch off in the evening.'),
        x('An deiner Stelle würde ich ein paar Tage ans Wasser fahren. Das würde dir guttun.', 'À ta place, j’irais quelques jours au bord de l’eau. Cela te ferait du bien.', 'If I were you, I would go to the water for a few days. It would do you good.'),
      ], [
        FB(COMPLETE, 'Nach der Prüfungswoche war ich völlig ＿ und habe zwölf Stunden geschlafen.', ['erschöpft', 'erholt', 'entspannt'], 'erschöpft', ('Épuisé : erschöpft.', 'Exhausted: erschöpft.'), ('Après la semaine d’examens, j’étais complètement épuisé et j’ai dormi douze heures.', 'After exam week I was completely exhausted and slept for twelve hours.')),
        FB(CHOOSE, 'Im Urlaub konnte er sich endlich ＿.', ['erholen', 'überfordern', 'belasten'], 'erholen', ('Récupérer : sich erholen.', 'To recover: sich erholen.'), ('En vacances, il a enfin pu se reposer.', 'On holiday he was finally able to rest.')),
        TF('Sie fühlt sich bei der Arbeit überfordert, weil sie zu viele Aufgaben hat.', ('Elle s’ennuie au travail.', 'She is bored at work.'), FAUX, ('Überfordert = dépassée par trop de tâches.', 'Überfordert = overwhelmed by too many tasks.')),
        DC(ANSWER, [('Freund', 'Ich schlafe schlecht und denke nur noch an die Arbeit.')], ('Un ami te confie qu’il dort mal à cause du travail (conseille-le avec tact).', 'A friend tells you he sleeps badly because of work (advise him tactfully).'), ['An deiner Stelle würde ich abends das Handy ausschalten.', 'An deiner Stelle werde ich abends das Handy ausgeschaltet.', 'Auf deiner Stelle würdest ich abschalten das Handy.'], 'An deiner Stelle würde ich abends das Handy ausschalten.', ('An deiner Stelle würde ich + infinitif.', 'An deiner Stelle würde ich + infinitive.')),
      ]),
  ])])

# ═════════════════════════ 8 : Argumenter, prépositions du génitif, l'économie ═════════════════════════
W8 = WORLD('goetheb2-w8', ('Le cabinet de Méphisto', 'Mephisto’s study'), REGION,
  ('Construire une argumentation, employer les prépositions de la langue écrite, parler d’économie et de consommation.', 'Build an argument, use the prepositions of written German, talk about the economy and consumption.'),
  (('Méphisto', 'Mephisto'), '✥', ('Dans le cabinet de travail, Méphisto déroule son contrat : tout a un prix, dit-il, et tout s’achète. Réfute-le point par point, pèse le pour et le contre, et conclus avant lui.', 'In the study, Mephisto unrolls his contract: everything has a price, he says, and everything can be bought. Refute him point by point, weigh the pros and cons, and conclude before he does.')),
  [CH('goetheb2-w8-c1', ('Le pour et le contre', 'The pros and cons'), [
    L('de-argumentieren', ('Argumenter : thèse, objection, conclusion', 'Arguing: thesis, objection, conclusion'), ('Structurer un avis à l’écrit comme dans un débat.', 'Structure an opinion in writing and in debate.'), 9, [
        ('Ouvrir : Heutzutage wird viel darüber diskutiert, ob… Es stellt sich die Frage, ob… Donner son avis : Meiner Ansicht nach… Ich bin der Auffassung, dass… Ich vertrete den Standpunkt, dass…', 'Opening: Heutzutage wird viel darüber diskutiert, ob… Es stellt sich die Frage, ob… Giving your view: Meiner Ansicht nach… Ich bin der Auffassung, dass… Ich vertrete den Standpunkt, dass…'),
        ('Peser : Dafür spricht, dass… (un argument pour). Dagegen spricht, dass… (un argument contre). Ein weiterer Vorteil / Nachteil ist… Man darf nicht vergessen, dass… Hinzu kommt, dass… (à cela s’ajoute que).', 'Weighing: Dafür spricht, dass… (an argument for). Dagegen spricht, dass… (an argument against). Ein weiterer Vorteil / Nachteil ist… Man darf nicht vergessen, dass… Hinzu kommt, dass… (in addition).'),
        ('Objecter et conclure : Das mag sein, aber… (c’est possible, mais). Dem kann ich nicht zustimmen. Im Gegenteil (au contraire). Zusammenfassend lässt sich sagen, dass… Abschließend möchte ich betonen, dass…', 'Objecting and concluding: Das mag sein, aber… (that may be so, but). Dem kann ich nicht zustimmen. Im Gegenteil (on the contrary). Zusammenfassend lässt sich sagen, dass… Abschließend möchte ich betonen, dass…'),
      ], [
        DG('meiner-ansicht-nach', 'Meiner Ansicht nach …', ('À mon avis…', 'In my view…')),
        DG('dafuer-spricht', 'Dafür / Dagegen spricht, dass …', ('Un argument pour / contre est que…', 'An argument for / against is that…')),
        DG('das-mag-sein', 'Das mag sein, aber …', ('C’est possible, mais…', 'That may be so, but…')),
        DG('zusammenfassend', 'Zusammenfassend lässt sich sagen, dass …', ('En résumé, on peut dire que…', 'To sum up, it can be said that…')),
        D('einwand', 'der Einwand', ('l’objection', 'the objection')),
        D('ueberwiegen', 'überwiegen', ('l’emporter, prédominer', 'to prevail, to outweigh')),
        D('widersprechen', 'widersprechen', ('contredire', 'to contradict')),
        D('im-gegenteil', 'im Gegenteil', ('au contraire', 'on the contrary')),
        D('standpunkt', 'der Standpunkt', ('le point de vue', 'the point of view')),
      ], [
        x('„Alles hat seinen Preis“, sagt Mephisto. — Das mag sein, aber nicht alles ist zu verkaufen.', '« Tout a un prix », dit Méphisto. — C’est possible, mais tout n’est pas à vendre.', '“Everything has its price,” says Mephisto. — That may be so, but not everything is for sale.'),
        x('Zusammenfassend lässt sich sagen, dass die Nachteile dieses Vertrags überwiegen.', 'En résumé, on peut dire que les inconvénients de ce contrat l’emportent.', 'To sum up, it can be said that the disadvantages of this contract prevail.'),
      ], [
        FB(CHOOSE, 'Meiner Ansicht ＿ sollte man weniger Fleisch essen.', ['nach', 'zu', 'für'], 'nach', ('Meiner Ansicht nach.', 'Meiner Ansicht nach.'), ('À mon avis, on devrait manger moins de viande.', 'In my view, we should eat less meat.')),
        FB(CHOOSE, 'Dafür ＿, dass man im Homeoffice Zeit spart.', ['spricht', 'sagt', 'redet'], 'spricht', ('Dafür spricht, dass…', 'Dafür spricht, dass…'), ('Un argument pour est qu’on gagne du temps en télétravail.', 'An argument in favour is that working from home saves time.')),
        FB(CHOOSE, 'In diesem Punkt kann ich Ihnen leider nicht ＿.', ['zustimmen', 'einverstanden', 'abstimmen'], 'zustimmen', ('Zustimmen + datif.', 'Zustimmen + dative.'), ('Sur ce point, je ne peux malheureusement pas vous approuver.', 'On this point, I am afraid I cannot agree with you.')),
        DC(ANSWER, [('Mephisto', 'Wer reich ist, ist auch glücklich. Das wissen doch alle.')], ('Méphisto affirme que la richesse fait le bonheur (objecte poliment).', 'Mephisto claims that wealth brings happiness (object politely).'), ['Das mag sein, aber Geld allein reicht nicht.', 'Das mag sein, dagegen Geld allein reicht nicht.', 'Dem kann ich zustimmen nicht, im Gegenteil reicht.'], 'Das mag sein, aber Geld allein reicht nicht.', ('Das mag sein, aber…', 'Das mag sein, aber…')),
      ]),
    L('de-praep-gen', ('Les prépositions de l’écrit : aufgrund, anhand, angesichts', 'Prepositions of written German: aufgrund, anhand, angesichts'), ('Comprendre et employer les prépositions suivies du génitif.', 'Understand and use prepositions followed by the genitive.'), 8, [
        ('Cause : aufgrund (en raison de), infolge (à la suite de), dank (grâce à). Aufgrund des schlechten Wetters… Infolge des Unfalls… Dank deiner Hilfe…', 'Cause: aufgrund (because of), infolge (as a result of), dank (thanks to). Aufgrund des schlechten Wetters… Infolge des Unfalls… Dank deiner Hilfe…'),
        ('Moyen et point de vue : anhand (à l’aide de, à partir de), mithilfe (au moyen de), angesichts (face à, au vu de), hinsichtlich / bezüglich (en ce qui concerne). Anhand eines Beispiels… Angesichts der Lage…', 'Means and viewpoint: anhand (on the basis of), mithilfe (with the help of), angesichts (in view of), hinsichtlich / bezüglich (with regard to). Anhand eines Beispiels… Angesichts der Lage…'),
        ('Lieu et temps : innerhalb (à l’intérieur de, dans un délai de), außerhalb (en dehors de), während (pendant). Opposition : anstatt / statt (au lieu de). Innerhalb einer Woche ; außerhalb der Stadt ; statt eines Geschenks.', 'Place and time: innerhalb (inside, within), außerhalb (outside), während (during). Contrast: anstatt / statt (instead of). Innerhalb einer Woche; außerhalb der Stadt; statt eines Geschenks.'),
      ], [
        DG('aufgrund', 'aufgrund + Genitiv', ('en raison de', 'because of, owing to')),
        DG('infolge', 'infolge + Genitiv', ('à la suite de', 'as a result of')),
        DG('anhand', 'anhand + Genitiv', ('à l’aide de, à partir de', 'on the basis of, by means of')),
        DG('angesichts', 'angesichts + Genitiv', ('face à, au vu de', 'in view of')),
        DG('ausserhalb', 'außerhalb + Genitiv', ('en dehors de', 'outside of')),
        DG('mithilfe', 'mithilfe + Genitiv', ('au moyen de, avec l’aide de', 'with the help of')),
        DG('statt-gen', '(an)statt + Genitiv', ('au lieu de', 'instead of')),
        DG('hinsichtlich', 'hinsichtlich + Genitiv', ('en ce qui concerne', 'with regard to')),
        D('unterschreiben', 'unterschreiben', ('signer', 'to sign')),
      ], [
        x('Angesichts der Gefahr wollte Faust den Vertrag nicht sofort unterschreiben.', 'Face au danger, Faust ne voulut pas signer le contrat tout de suite.', 'In view of the danger, Faust did not want to sign the contract at once.'),
        x('Anhand eines einzigen Satzes erkannte er, mit wem er sprach.', 'À partir d’une seule phrase, il reconnut à qui il parlait.', 'From a single sentence he recognised whom he was speaking to.'),
      ], [
        FB(CHOOSE, '＿ des Streiks fahren heute keine Züge.', ['Aufgrund', 'Anhand', 'Innerhalb'], 'Aufgrund', ('La cause : aufgrund + génitif.', 'The cause: aufgrund + genitive.'), ('En raison de la grève, aucun train ne circule aujourd’hui.', 'Because of the strike, no trains are running today.')),
        FB(CHOOSE, 'Bitte antworten Sie ＿ einer Woche.', ['innerhalb', 'angesichts', 'infolge'], 'innerhalb', ('Dans un délai de : innerhalb.', 'Within: innerhalb.'), ('Veuillez répondre dans un délai d’une semaine.', 'Please reply within one week.')),
        FB(CHOOSE, 'Der Lehrer erklärt die Regel ＿ eines Beispiels.', ['anhand', 'aufgrund', 'statt'], 'anhand', ('À l’aide de : anhand.', 'By means of: anhand.'), ('Le professeur explique la règle à l’aide d’un exemple.', 'The teacher explains the rule by means of an example.')),
        FB(CHOOSE, 'Angesichts ＿ müssen wir sparen.', ['der hohen Kosten', 'die hohen Kosten', 'den hohen Kosten'], 'der hohen Kosten', ('Angesichts + génitif pluriel : der hohen Kosten.', 'Angesichts + genitive plural: der hohen Kosten.'), ('Au vu des coûts élevés, nous devons économiser.', 'In view of the high costs, we have to save.')),
      ]),
  ]),
  CH('goetheb2-w8-c2', ('Tout a un prix', 'Everything has a price'), [
    L('de-wirtschaft', ('L’économie et la consommation', 'The economy and consumption'), ('Parler de prix, d’entreprises et d’habitudes de consommation.', 'Talk about prices, companies and consumer habits.'), 8, [
        ('L’économie : die Wirtschaft, das Unternehmen (l’entreprise), der Umsatz (le chiffre d’affaires), der Gewinn / der Verlust (le bénéfice / la perte), die Nachfrage (la demande), das Angebot (l’offre), die Konkurrenz (la concurrence).', 'The economy: die Wirtschaft, das Unternehmen (the company), der Umsatz (turnover), der Gewinn / der Verlust (profit / loss), die Nachfrage (demand), das Angebot (supply, the offer), die Konkurrenz (competition).'),
        ('La consommation : der Verbraucher (le consommateur), der Konsum, sich etwas leisten können (pouvoir s’offrir), die Schulden (les dettes), die Werbung (la publicité), nachhaltig (durable), die Ware (la marchandise).', 'Consumption: der Verbraucher (the consumer), der Konsum, sich etwas leisten können (to be able to afford), die Schulden (debts), die Werbung (advertising), nachhaltig (sustainable), die Ware (the goods).'),
        ('Décrire une évolution : steigen / zunehmen (augmenter), sinken / abnehmen (baisser), um zehn Prozent (de dix pour cent), auf zwei Millionen (à deux millions), stabil bleiben, sich verdoppeln (doubler).', 'Describing a trend: steigen / zunehmen (to rise), sinken / abnehmen (to fall), um zehn Prozent (by ten per cent), auf zwei Millionen (to two million), stabil bleiben, sich verdoppeln (to double).'),
      ], [
        D('wirtschaft', 'die Wirtschaft', ('l’économie', 'the economy')),
        D('unternehmen', 'das Unternehmen', ('l’entreprise', 'the company')),
        D('gewinn', 'der Gewinn', ('le bénéfice, le gain', 'the profit')),
        D('nachfrage', 'die Nachfrage', ('la demande', 'demand')),
        D('verbraucher', 'der Verbraucher', ('le consommateur', 'the consumer')),
        D('sich-leisten', 'sich etwas leisten', ('s’offrir quelque chose', 'to afford something')),
        D('nachhaltig', 'nachhaltig', ('durable (écologiquement)', 'sustainable')),
        D('zunehmen', 'zunehmen', ('augmenter ; grossir', 'to increase; to put on weight')),
        D('sinken', 'sinken', ('baisser ; couler', 'to fall, to sink')),
      ], [
        x('Die Nachfrage nach nachhaltigen Waren ist um zwanzig Prozent gestiegen.', 'La demande de produits durables a augmenté de vingt pour cent.', 'Demand for sustainable goods has risen by twenty per cent.'),
        x('Viele Verbraucher können sich teure Bioprodukte nicht leisten.', 'Beaucoup de consommateurs ne peuvent pas s’offrir des produits bio chers.', 'Many consumers cannot afford expensive organic products.'),
      ], [
        FB(CHOOSE, 'Der Umsatz ist ＿ fünf Prozent gestiegen.', ['um', 'auf', 'bei'], 'um', ('La différence : um + pourcentage.', 'The difference: um + percentage.'), ('Le chiffre d’affaires a augmenté de cinq pour cent.', 'Turnover has risen by five per cent.')),
        FB(COMPLETE, 'Wenn die ＿ steigt, steigen meistens auch die Preise.', ['Nachfrage', 'Konkurrenz', 'Werbung'], 'Nachfrage', ('La demande : die Nachfrage.', 'Demand: die Nachfrage.'), ('Quand la demande augmente, les prix augmentent le plus souvent aussi.', 'When demand rises, prices usually rise too.')),
        FB(CHOOSE, 'So ein teures Auto kann ich ＿ nicht leisten.', ['mir', 'mich', 'sich'], 'mir', ('Sich (datif) etwas leisten : ich… mir.', 'Sich (dative) etwas leisten: ich… mir.'), ('Je ne peux pas m’offrir une voiture aussi chère.', 'I cannot afford such an expensive car.')),
        TF('Das Unternehmen hat im letzten Jahr Verluste gemacht und muss Stellen streichen.', ('L’entreprise a fait des bénéfices.', 'The company made a profit.'), FAUX, ('Verluste = des pertes.', 'Verluste = losses.')),
      ]),
  ])])

write_level('GOETHEB2', ('Goethe B2 : la cour des poètes', 'Goethe B2: the court of poets'), REGION, 'Weimar of the poets', 47,
  [W1, W2, W3, W4, W5, W6, W7, W8, FINAL('GOETHEB2', REGION, ('Simulation Goethe B2 : la bibliothèque de Weimar', 'Goethe B2 simulation: the Weimar library'), 'Lesen, Hören et Schreiben (l’oral, Sprechen, n’est pas évalué)', 'Lesen, Hören and Schreiben (the speaking test, Sprechen, is not assessed)', modules=True)])
