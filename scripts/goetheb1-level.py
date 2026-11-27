# Niveau Goethe-Zertifikat B1 (allemand, CECRL B1) : 8 étapes au pays des légendes, du Kyffhäuser au Rhin et au Brocken.
# Mode histoire : après les contes, l'apprenti·e des frères Grimm recueille les « Deutsche Sagen », les légendes allemandes (voir gen-story.py).
# Usage : python3 scripts/goetheb1-level.py   (réécrit content/goetheb1/goetheb1.json ; les Goethe A1 et A2 doivent déjà exister)
from de_common import *
begin('GOETHEB1')

REGION = 'Pays des légendes'

# ═════════════════════════ 1 : Raconter au prétérit ═════════════════════════
W1 = WORLD('goetheb1-w1', ('La montagne de Barberousse', 'Barbarossa’s mountain'), REGION,
  ('Raconter une histoire au prétérit, verbes réguliers et forts, et ordonner les événements avec nachdem, bevor et le plus-que-parfait.', 'Tell a story in the simple past, regular and strong verbs, and order events with nachdem, bevor and the past perfect.'),
  (('L’Empereur Barberousse', 'Emperor Barbarossa'), '♤', ('Sous le Kyffhäuser, l’Empereur Barberousse dort depuis des siècles, sa barbe rousse poussée à travers la table de pierre. Il ne s’éveille que pour entendre une chronique bien racontée : au prétérit, comme dans les livres.', 'Beneath the Kyffhäuser, Emperor Barbarossa has slept for centuries, his red beard grown through the stone table. He only wakes to hear a chronicle well told: in the simple past, as in books.')),
  [CH('goetheb1-w1-c1', ('Il était une fois…', 'Once upon a time…'), [
    L('de-praet-schwach', ('Le prétérit des verbes réguliers', 'The simple past of regular verbs'), ('Raconter à l’écrit avec le prétérit en -te.', 'Narrate in writing with the simple past in -te.'), 9, [
        ('Le prétérit est le temps du récit écrit : contes, romans, articles. À l’oral, on garde le Perfekt, sauf pour sein, haben et les verbes de modalité.', 'The simple past is the tense of written narrative: tales, novels, articles. In speech the Perfekt is kept, except for sein, haben and the modal verbs.'),
        ('Verbes réguliers : radical + -te + terminaison. ich machte, du machtest, er machte, wir machten, ihr machtet, sie machten. La 1re et la 3e personne du singulier sont identiques.', 'Regular verbs: stem + -te + ending. ich machte, du machtest, er machte, wir machten, ihr machtet, sie machten. The first and third person singular are identical.'),
        ('Radical en -t ou -d : on intercale -e- (arbeiten → er arbeitete, warten → er wartete). Verbes de modalité : sans tréma (können → konnte, müssen → musste, wollen → wollte, dürfen → durfte).', 'Stem in -t or -d: insert -e- (arbeiten → er arbeitete, warten → er wartete). Modal verbs: no umlaut (können → konnte, müssen → musste, wollen → wollte, dürfen → durfte).'),
      ], [
        DG('praet-te', 'Stamm + -te (Präteritum)', ('prétérit régulier en -te', 'regular simple past in -te')),
        D('machte', 'machen → er machte', ('faire → il fit, il faisait', 'to do → he did')),
        D('wohnte', 'wohnen → er wohnte', ('habiter → il habitait', 'to live → he lived')),
        D('wartete', 'warten → er wartete', ('attendre → il attendit', 'to wait → he waited')),
        D('konnte', 'können → er konnte', ('pouvoir → il pouvait, il put', 'can → he could')),
        D('musste', 'müssen → er musste', ('devoir → il devait, il dut', 'must → he had to')),
        D('wollte', 'wollen → er wollte', ('vouloir → il voulait', 'to want → he wanted')),
        D('es-war-einmal', 'Es war einmal …', ('Il était une fois…', 'Once upon a time…')),
        D('kaiser', 'der Kaiser', ('l’empereur', 'the emperor')),
      ], [
        x('Es war einmal ein Kaiser, der in einem Berg wohnte und auf bessere Zeiten wartete.', 'Il était une fois un empereur qui habitait dans une montagne et attendait des jours meilleurs.', 'Once upon a time there was an emperor who lived in a mountain and waited for better times.'),
        x('Niemand konnte ihn wecken, und niemand wollte es versuchen.', 'Personne ne pouvait le réveiller, et personne ne voulait essayer.', 'Nobody could wake him, and nobody wanted to try.'),
      ], [
        FB(CHOOSE, 'Der Hirte ＿ lange vor dem Berg.', ['wartete', 'wartet', 'gewartet'], 'wartete', ('Prétérit, radical en -t : wartete.', 'Simple past, stem in -t: wartete.'), ('Le berger attendit longtemps devant la montagne.', 'The shepherd waited for a long time in front of the mountain.')),
        FB(CHOOSE, 'Wir ＿ den Weg nicht finden.', ['konnten', 'könnten', 'gekonnt'], 'konnten', ('Prétérit de können : konnte, sans tréma.', 'Simple past of können: konnte, no umlaut.'), ('Nous ne pouvions pas trouver le chemin.', 'We could not find the way.')),
        FB(CHOOSE, 'Früher ＿ hier viele Raben.', ['lebten', 'leben', 'gelebt'], 'lebten', ('Prétérit pluriel : lebten.', 'Plural simple past: lebten.'), ('Autrefois, beaucoup de corbeaux vivaient ici.', 'In the past many ravens lived here.')),
        TF('Der Kaiser wollte nicht aufwachen.', ('L’empereur voulait se réveiller.', 'The emperor wanted to wake up.'), FAUX, ('Wollte nicht = ne voulait pas.', 'Wollte nicht = did not want to.')),
      ]),
    L('de-praet-stark', ('Le prétérit des verbes forts', 'The simple past of strong verbs'), ('Reconnaître et employer les prétérits irréguliers les plus fréquents.', 'Recognise and use the most common irregular simple pasts.'), 9, [
        ('Les verbes forts changent de voyelle et ne prennent pas -te : gehen → ging, kommen → kam, sehen → sah, geben → gab, finden → fand, sprechen → sprach.', 'Strong verbs change their vowel and take no -te: gehen → ging, kommen → kam, sehen → sah, geben → gab, finden → fand, sprechen → sprach.'),
        ('Pas de terminaison à ich et er : ich ging, er ging. Les autres : du gingst, wir gingen, ihr gingt, sie gingen.', 'No ending for ich and er: ich ging, er ging. The others: du gingst, wir gingen, ihr gingt, sie gingen.'),
        ('Verbes mixtes (voyelle changée + -te) : bringen → brachte, denken → dachte, wissen → wusste, kennen → kannte. Et werden → wurde.', 'Mixed verbs (changed vowel + -te): bringen → brachte, denken → dachte, wissen → wusste, kennen → kannte. And werden → wurde.'),
      ], [
        DG('praet-stark', 'ging, kam, sah (Präteritum)', ('prétérit des verbes forts', 'simple past of strong verbs')),
        D('ging', 'gehen → er ging', ('aller → il alla', 'to go → he went')),
        D('kam', 'kommen → er kam', ('venir → il vint', 'to come → he came')),
        D('sah', 'sehen → er sah', ('voir → il vit', 'to see → he saw')),
        D('gab', 'geben → er gab', ('donner → il donna', 'to give → he gave')),
        D('fand', 'finden → er fand', ('trouver → il trouva', 'to find → he found')),
        D('sprach', 'sprechen → er sprach', ('parler → il parla', 'to speak → he spoke')),
        D('wusste', 'wissen → er wusste', ('savoir → il savait', 'to know → he knew')),
        D('wurde', 'werden → er wurde', ('devenir → il devint', 'to become → he became')),
      ], [
        x('Ein Hirte ging in den Berg und sah den schlafenden Kaiser.', 'Un berger entra dans la montagne et vit l’empereur endormi.', 'A shepherd went into the mountain and saw the sleeping emperor.'),
        x('Der Kaiser gab ihm Gold und sprach: „Fliegen die Raben noch um den Berg?“', 'L’empereur lui donna de l’or et dit : « Les corbeaux volent-ils encore autour de la montagne ? »', 'The emperor gave him gold and said: “Are the ravens still flying around the mountain?”'),
      ], [
        FB(CHOOSE, 'Er ＿ in den Berg.', ['ging', 'gehte', 'gegangen'], 'ging', ('Gehen → ging (verbe fort).', 'Gehen → ging (strong verb).'), ('Il entra dans la montagne.', 'He went into the mountain.')),
        FB(CHOOSE, 'Plötzlich ＿ ein Rabe.', ['kam', 'kommte', 'kamt'], 'kam', ('Kommen → kam ; pas de terminaison à la 3e personne.', 'Kommen → kam; no ending in the third person.'), ('Soudain, un corbeau arriva.', 'Suddenly a raven came.')),
        FB(CHOOSE, 'Niemand ＿, wo der Kaiser war.', ['wusste', 'wisste', 'weiß'], 'wusste', ('Wissen → wusste (verbe mixte).', 'Wissen → wusste (mixed verb).'), ('Personne ne savait où était l’empereur.', 'Nobody knew where the emperor was.')),
        FB(CHOOSE, 'Die Kinder ＿ einen alten Schlüssel.', ['fanden', 'fand', 'findeten'], 'fanden', ('Finden → fand ; au pluriel : fanden.', 'Finden → fand; in the plural: fanden.'), ('Les enfants trouvèrent une vieille clé.', 'The children found an old key.')),
      ]),
  ]),
  CH('goetheb1-w1-c2', ('Avant, après', 'Before, after'), [
    L('de-nachdem', ('Avant et après : nachdem, bevor, le plus-que-parfait', 'Before and after: nachdem, bevor, the past perfect'), ('Dire qu’une action en précède une autre dans le passé.', 'Say that one action came before another in the past.'), 8, [
        ('Le plus-que-parfait : hatte ou war + participe. Er hatte lange geschlafen. Sie war schon gegangen. Il exprime ce qui s’est passé avant un autre moment du passé.', 'The past perfect: hatte or war + participle. Er hatte lange geschlafen. Sie war schon gegangen. It expresses what happened before another moment in the past.'),
        ('Nachdem (après que) introduit l’action la plus ancienne, au plus-que-parfait : Nachdem er gegessen hatte, ging er schlafen. Le verbe conjugué est à la fin de la subordonnée.', 'Nachdem (after) introduces the earlier action, in the past perfect: Nachdem er gegessen hatte, ging er schlafen. The conjugated verb is at the end of the clause.'),
        ('Bevor (avant que), während (pendant que), bis (jusqu’à ce que), sobald (dès que). Bevor er ging, schloss er die Tür. Während er schlief, wuchs sein Bart.', 'Bevor (before), während (while), bis (until), sobald (as soon as). Bevor er ging, schloss er die Tür. Während er schlief, wuchs sein Bart.'),
      ], [
        DG('plusquamperfekt', 'hatte / war + Partizip II', ('plus-que-parfait', 'past perfect')),
        DG('nachdem', 'nachdem', ('après que', 'after (conjunction)')),
        DG('bevor', 'bevor', ('avant que', 'before (conjunction)')),
        DG('waehrend-konj', 'während', ('pendant que', 'while')),
        DG('bis-konj', 'bis', ('jusqu’à ce que', 'until')),
        DG('sobald', 'sobald', ('dès que', 'as soon as')),
        D('ploetzlich', 'plötzlich', ('soudain', 'suddenly')),
        D('schliesslich', 'schließlich', ('finalement', 'finally, in the end')),
      ], [
        x('Nachdem der Hirte den Berg verlassen hatte, waren hundert Jahre vergangen.', 'Après que le berger eut quitté la montagne, cent ans s’étaient écoulés.', 'After the shepherd had left the mountain, a hundred years had passed.'),
        x('Der Kaiser schläft, bis die Raben nicht mehr fliegen.', 'L’empereur dort jusqu’à ce que les corbeaux ne volent plus.', 'The emperor sleeps until the ravens no longer fly.'),
      ], [
        FB(CHOOSE, 'Nachdem er gegessen ＿, ging er schlafen.', ['hatte', 'hat', 'war'], 'hatte', ('Après nachdem : plus-que-parfait, hatte gegessen.', 'After nachdem: past perfect, hatte gegessen.'), ('Après avoir mangé, il alla dormir.', 'After he had eaten, he went to bed.')),
        FB(CHOOSE, 'Als ich ankam, ＿ der Zug schon abgefahren.', ['war', 'hatte', 'ist'], 'war', ('Abfahren (déplacement) : war abgefahren.', 'Abfahren (movement): war abgefahren.'), ('Quand je suis arrivé, le train était déjà parti.', 'When I arrived, the train had already left.')),
        FB(CHOOSE, '＿ er das Haus verließ, schloss er alle Fenster.', ['Bevor', 'Nachdem', 'Bis'], 'Bevor', ('Il ferme d’abord, puis sort : bevor.', 'He closes first, then leaves: bevor.'), ('Avant de quitter la maison, il ferma toutes les fenêtres.', 'Before he left the house, he closed all the windows.')),
        order(('Remets dans l’ordre : « Pendant qu’il dormait, sa barbe poussait. »', 'Put in order: “While he slept, his beard grew.”'), ['Während', 'er', 'schlief,', 'wuchs', 'sein', 'Bart.'], ('Subordonnée en tête : le verbe wuchs suit la virgule.', 'Subordinate clause first: the verb wuchs follows the comma.')),
      ]),
  ])])

# ═════════════════════════ 2 : Les relatives, décrire ═════════════════════════
W2 = WORLD('goetheb1-w2', ('Les monts de Rübezahl', 'Rübezahl’s mountains'), REGION,
  ('Préciser de qui ou de quoi l’on parle avec les propositions relatives, au nominatif, à l’accusatif, au datif et avec préposition.', 'Specify who or what you mean with relative clauses, in the nominative, accusative, dative and with a preposition.'),
  (('Le Géant Rübezahl', 'The Giant Rübezahl'), '♧', ('Rübezahl, l’esprit des monts des Géants, change de forme à chaque rencontre : moine, bûcheron, tempête. Pour le démasquer, décris-le précisément : l’homme qui…, le manteau qu’il…, le bâton avec lequel…', 'Rübezahl, the spirit of the Giant Mountains, changes shape at every encounter: monk, woodcutter, storm. To unmask him, describe him precisely: the man who…, the coat that he…, the staff with which…')),
  [CH('goetheb1-w2-c1', ('L’homme qui…', 'The man who…'), [
    L('de-relativ-nom', ('Les relatives : der, die, das', 'Relative clauses: der, die, das'), ('Préciser un nom avec une relative sujet ou objet.', 'Specify a noun with a subject or object relative clause.'), 9, [
        ('Le pronom relatif ressemble à l’article défini et s’accorde en genre et en nombre avec le nom qu’il reprend : der Mann, der… ; die Frau, die… ; das Kind, das… ; die Leute, die…', 'The relative pronoun looks like the definite article and agrees in gender and number with the noun it refers to: der Mann, der…; die Frau, die…; das Kind, das…; die Leute, die…'),
        ('Son cas dépend de sa fonction dans la relative. Sujet : Der Mann, der dort steht (qui). Objet : Der Mann, den ich sehe (que). Seul le masculin change à l’accusatif.', 'Its case depends on its function in the relative clause. Subject: Der Mann, der dort steht (who). Object: Der Mann, den ich sehe (whom). Only the masculine changes in the accusative.'),
        ('La relative est une subordonnée : verbe conjugué à la fin, virgule avant et après. Der Wanderer, der den Weg nicht kannte, fragte einen Mönch.', 'The relative clause is a subordinate clause: conjugated verb at the end, a comma before and after. Der Wanderer, der den Weg nicht kannte, fragte einen Mönch.'),
      ], [
        DG('rel-nom', 'der / die / das (Relativpronomen, Nominativ)', ('qui (pronom relatif sujet)', 'who, which (subject relative pronoun)')),
        DG('rel-akk', 'den / die / das (Relativpronomen, Akkusativ)', ('que (pronom relatif objet)', 'whom, which (object relative pronoun)')),
        D('berg', 'der Berg', ('la montagne', 'the mountain')),
        D('geist', 'der Geist', ('l’esprit, le fantôme', 'the spirit, the ghost')),
        D('wanderer', 'der Wanderer', ('le randonneur, le voyageur à pied', 'the hiker, the wanderer')),
        D('leute', 'die Leute', ('les gens', 'people')),
        D('fremd', 'fremd', ('étranger, inconnu', 'strange, foreign')),
        D('aussehen', 'aussehen', ('avoir l’air, ressembler à', 'to look (like)')),
      ], [
        x('Rübezahl ist ein Geist, der in den Bergen wohnt.', 'Rübezahl est un esprit qui habite dans les montagnes.', 'Rübezahl is a spirit who lives in the mountains.'),
        x('Der Mönch, den die Wanderer trafen, war in Wirklichkeit Rübezahl.', 'Le moine que les randonneurs rencontrèrent était en réalité Rübezahl.', 'The monk whom the hikers met was in reality Rübezahl.'),
      ], [
        FB(CHOOSE, 'Das ist die Frau, ＿ mir geholfen hat.', ['die', 'der', 'den'], 'die', ('Die Frau, sujet de la relative : die.', 'Die Frau, subject of the relative clause: die.'), ('C’est la femme qui m’a aidé.', 'That is the woman who helped me.')),
        FB(CHOOSE, 'Der Weg, ＿ wir genommen haben, war zu lang.', ['den', 'der', 'dem'], 'den', ('Der Weg, objet de nehmen : den.', 'Der Weg, object of nehmen: den.'), ('Le chemin que nous avons pris était trop long.', 'The path that we took was too long.')),
        FB(CHOOSE, 'Das Kind, ＿ dort spielt, ist mein Sohn.', ['das', 'der', 'den'], 'das', ('Das Kind, sujet : das.', 'Das Kind, subject: das.'), ('L’enfant qui joue là-bas est mon fils.', 'The child who is playing over there is my son.')),
        order(('Remets dans l’ordre : « L’homme qui habite ici est un esprit. »', 'Put in order: “The man who lives here is a spirit.”'), ['Der', 'Mann,', 'der', 'hier', 'wohnt,', 'ist', 'ein', 'Geist.'], ('Dans la relative, le verbe wohnt est à la fin.', 'In the relative clause, the verb wohnt is at the end.')),
      ]),
    L('de-relativ-dat', ('Les relatives au datif et avec préposition', 'Relative clauses in the dative and with a preposition'), ('Préciser un nom quand le verbe ou la préposition demande un autre cas.', 'Specify a noun when the verb or preposition requires another case.'), 8, [
        ('Au datif : dem (masculin, neutre), der (féminin), denen (pluriel). Der Mann, dem ich geholfen habe. Die Leute, denen das Haus gehört.', 'In the dative: dem (masculine, neuter), der (feminine), denen (plural). Der Mann, dem ich geholfen habe. Die Leute, denen das Haus gehört.'),
        ('Avec une préposition, celle-ci précède le pronom et impose son cas : Der Stock, mit dem er geht. Die Stadt, in der ich wohne. Das Thema, über das wir sprechen.', 'With a preposition, it comes before the pronoun and sets its case: Der Stock, mit dem er geht. Die Stadt, in der ich wohne. Das Thema, über das wir sprechen.'),
        ('Pour un lieu, wo remplace souvent in + pronom : Die Stadt, wo ich wohne. Après alles, etwas, nichts, das : was. Alles, was er sagte, war falsch.', 'For a place, wo often replaces in + pronoun: Die Stadt, wo ich wohne. After alles, etwas, nichts, das: was. Alles, was er sagte, war falsch.'),
      ], [
        DG('rel-dat', 'dem / der / denen (Relativpronomen, Dativ)', ('à qui, auquel (pronom relatif au datif)', 'to whom, to which (dative relative pronoun)')),
        DG('rel-praep', 'Präposition + Relativpronomen', ('préposition + pronom relatif', 'preposition + relative pronoun')),
        DG('rel-was', 'alles, was … / nichts, was …', ('tout ce que… / rien de ce que…', 'everything that… / nothing that…')),
        D('stock', 'der Stock', ('le bâton, la canne', 'the stick, the staff')),
        D('dorf', 'das Dorf', ('le village', 'the village')),
        D('bauer', 'der Bauer', ('le paysan', 'the farmer')),
        D('reich', 'reich', ('riche', 'rich')),
        D('arm-adj', 'arm', ('pauvre', 'poor')),
      ], [
        x('Der Bauer, dem Rübezahl Geld geliehen hatte, wurde reich.', 'Le paysan à qui Rübezahl avait prêté de l’argent devint riche.', 'The farmer to whom Rübezahl had lent money became rich.'),
        x('Das Dorf, in dem die Geschichte spielt, liegt hoch in den Bergen.', 'Le village où se passe l’histoire se trouve haut dans les montagnes.', 'The village in which the story takes place lies high in the mountains.'),
      ], [
        FB(CHOOSE, 'Der Freund, ＿ ich das Buch gegeben habe, liest es gerade.', ['dem', 'den', 'der'], 'dem', ('Geben + datif : dem.', 'Geben + dative: dem.'), ('L’ami à qui j’ai donné le livre est en train de le lire.', 'The friend to whom I gave the book is reading it right now.')),
        FB(CHOOSE, 'Die Kinder, ＿ wir geholfen haben, sind glücklich.', ['denen', 'die', 'den'], 'denen', ('Helfen + datif, pluriel : denen.', 'Helfen + dative, plural: denen.'), ('Les enfants que nous avons aidés sont heureux.', 'The children whom we helped are happy.')),
        FB(CHOOSE, 'Das ist das Haus, in ＿ ich geboren bin.', ['dem', 'das', 'der'], 'dem', ('In + datif (lieu) ; das Haus → dem.', 'In + dative (location); das Haus → dem.'), ('C’est la maison dans laquelle je suis né.', 'That is the house in which I was born.')),
        FB(CHOOSE, 'Alles, ＿ er erzählt, ist wahr.', ['was', 'das', 'dem'], 'was', ('Après alles : was.', 'After alles: was.'), ('Tout ce qu’il raconte est vrai.', 'Everything that he tells is true.')),
      ]),
  ]),
  CH('goetheb1-w2-c2', ('Mille visages', 'A thousand faces'), [
    L('de-charakter', ('Décrire le caractère', 'Describing character'), ('Parler des qualités et des défauts de quelqu’un et nuancer son jugement.', 'Talk about someone’s qualities and faults and qualify your judgement.'), 8, [
        ('Qualités : ehrlich (honnête), hilfsbereit (serviable), geduldig (patient), fleißig (travailleur), zuverlässig (fiable). Défauts : faul (paresseux), geizig (avare), stur (têtu), neugierig (curieux).', 'Qualities: ehrlich (honest), hilfsbereit (helpful), geduldig (patient), fleißig (hard-working), zuverlässig (reliable). Faults: faul (lazy), geizig (stingy), stur (stubborn), neugierig (curious).'),
        ('Le préfixe un- forme souvent le contraire : freundlich → unfreundlich, höflich → unhöflich, geduldig → ungeduldig, ehrlich → unehrlich.', 'The prefix un- often forms the opposite: freundlich → unfreundlich, höflich → unhöflich, geduldig → ungeduldig, ehrlich → unehrlich.'),
        ('Pour nuancer : ziemlich (assez), ein bisschen (un peu), überhaupt nicht (pas du tout), eher (plutôt). Er ist ziemlich stur, aber überhaupt nicht geizig.', 'To qualify: ziemlich (rather), ein bisschen (a bit), überhaupt nicht (not at all), eher (rather, more). Er ist ziemlich stur, aber überhaupt nicht geizig.'),
      ], [
        D('ehrlich', 'ehrlich', ('honnête', 'honest')),
        D('hilfsbereit', 'hilfsbereit', ('serviable', 'helpful')),
        D('geduldig', 'geduldig', ('patient (qui sait attendre)', 'patient (able to wait)')),
        D('fleissig', 'fleißig', ('travailleur, appliqué', 'hard-working')),
        D('faul', 'faul', ('paresseux', 'lazy')),
        D('geizig', 'geizig', ('avare', 'stingy, mean')),
        D('stur', 'stur', ('têtu', 'stubborn')),
        D('ziemlich', 'ziemlich', ('assez, plutôt', 'rather, quite')),
        D('ueberhaupt-nicht', 'überhaupt nicht', ('pas du tout', 'not at all')),
      ], [
        x('Rübezahl hilft den Armen, die ehrlich und fleißig sind.', 'Rübezahl aide les pauvres qui sont honnêtes et travailleurs.', 'Rübezahl helps the poor who are honest and hard-working.'),
        x('Den geizigen Kaufmann dagegen mag er überhaupt nicht.', 'Le marchand avare, en revanche, il ne l’aime pas du tout.', 'The stingy merchant, on the other hand, he does not like at all.'),
      ], [
        FB(COMPLETE, 'Er gibt nie Geld aus: Er ist sehr ＿.', ['geizig', 'hilfsbereit', 'fleißig'], 'geizig', ('Qui ne dépense jamais : geizig.', 'Someone who never spends: geizig.'), ('Il ne dépense jamais d’argent : il est très avare.', 'He never spends money: he is very stingy.')),
        FB(COMPLETE, 'Sie arbeitet von morgens bis abends. Sie ist wirklich ＿.', ['fleißig', 'faul', 'stur'], 'fleißig', ('Qui travaille beaucoup : fleißig.', 'Someone who works a lot: fleißig.'), ('Elle travaille du matin au soir. Elle est vraiment travailleuse.', 'She works from morning till evening. She is really hard-working.')),
        TF('Mein Bruder ist überhaupt nicht geduldig.', ('Son frère est très patient.', 'Their brother is very patient.'), FAUX, ('Überhaupt nicht = pas du tout.', 'Überhaupt nicht = not at all.')),
        DC(ANSWER, [('Wanderer', 'Wie ist dein neuer Chef?')], ('On te demande comment est ton nouveau chef (plutôt têtu, mais honnête).', 'You are asked what your new boss is like (rather stubborn, but honest).'), ['Er ist ziemlich stur, aber ehrlich.', 'Er hat ziemlich stur, aber ehrlich.', 'Er ist ein Stur, der ehrlich.'], 'Er ist ziemlich stur, aber ehrlich.', ('Sein + adjectifs ; ziemlich nuance.', 'Sein + adjectives; ziemlich qualifies.')),
      ]),
  ])])

# ═════════════════════════ 3 : L'irréel et les souhaits ═════════════════════════
W3 = WORLD('goetheb1-w3', ('La cabane du Pêcheur', 'The Fisherman’s hut'), REGION,
  ('Exprimer un souhait, une hypothèse irréelle et un conseil avec le Konjunktiv II : wäre, hätte, würde, könnte.', 'Express a wish, an unreal hypothesis and advice with Konjunktiv II: wäre, hätte, würde, könnte.'),
  (('La Femme du pêcheur', 'The Fisherman’s Wife'), '♡', ('« Si j’avais une maison… si j’étais reine… si j’étais pape ! » La Femme du pêcheur en veut toujours plus, et la mer noircit à chaque vœu. Formule tes hypothèses sans faute avant que la tempête n’emporte tout.', '“If I had a house… if I were queen… if I were pope!” The Fisherman’s Wife always wants more, and the sea darkens with every wish. Phrase your hypotheses without a mistake before the storm sweeps everything away.')),
  [CH('goetheb1-w3-c1', ('Si j’étais…', 'If I were…'), [
    L('de-konj2-formen', ('Le Konjunktiv II : wäre, hätte, würde', 'Konjunktiv II: wäre, hätte, würde'), ('Former le conditionnel des verbes les plus courants.', 'Form the conditional of the most common verbs.'), 9, [
        ('Sein et haben ont leur propre forme : ich wäre, du wärst, er wäre, wir wären ; ich hätte, du hättest, er hätte, wir hätten.', 'Sein and haben have their own forms: ich wäre, du wärst, er wäre, wir wären; ich hätte, du hättest, er hätte, wir hätten.'),
        ('Les verbes de modalité aussi : könnte (pourrait), müsste (devrait), dürfte (aurait le droit), sollte (devrait), wollte (voudrait).', 'So do the modal verbs: könnte (could), müsste (would have to), dürfte (would be allowed to), sollte (should), wollte (would want).'),
        ('Pour presque tous les autres verbes : würde + infinitif à la fin. Ich würde ein Haus kaufen. Quelques formes courtes restent courantes : käme, ginge, wüsste, gäbe (es gäbe = il y aurait).', 'For almost all other verbs: würde + infinitive at the end. Ich würde ein Haus kaufen. A few short forms remain common: käme, ginge, wüsste, gäbe (es gäbe = there would be).'),
      ], [
        DG('waere', 'ich wäre / du wärst / er wäre', ('je serais / tu serais / il serait', 'I would be / you would be / he would be')),
        DG('haette', 'ich hätte / du hättest / er hätte', ('j’aurais / tu aurais / il aurait', 'I would have / you would have / he would have')),
        DG('wuerde-inf', 'würde + Infinitiv', ('conditionnel (würde + infinitif)', 'conditional (würde + infinitive)')),
        DG('koennte-muesste', 'könnte / müsste / dürfte', ('pourrait / devrait / aurait le droit', 'could / would have to / would be allowed to')),
        D('wunsch', 'der Wunsch', ('le souhait, le vœu', 'the wish')),
        D('sich-wuenschen', 'sich wünschen', ('souhaiter, désirer', 'to wish for')),
        D('zufrieden', 'zufrieden', ('satisfait, content', 'satisfied, content')),
        D('fischer', 'der Fischer', ('le pêcheur', 'the fisherman')),
      ], [
        x('Ich hätte gern ein Schloss, und ich wäre gern Königin.', 'J’aimerais avoir un château, et j’aimerais être reine.', 'I would like to have a castle, and I would like to be queen.'),
        x('Der Fischer würde lieber in seiner Hütte bleiben.', 'Le pêcheur préférerait rester dans sa cabane.', 'The fisherman would rather stay in his hut.'),
      ], [
        FB(CHOOSE, 'Ich ＿ gern mehr Zeit.', ['hätte', 'wäre', 'würde'], 'hätte', ('Avoir au conditionnel : ich hätte.', 'To have in the conditional: ich hätte.'), ('J’aimerais avoir plus de temps.', 'I would like to have more time.')),
        FB(CHOOSE, 'Sie ＿ gern Kaiserin.', ['wäre', 'hätte', 'würde'], 'wäre', ('Être au conditionnel : sie wäre.', 'To be in the conditional: sie wäre.'), ('Elle aimerait être impératrice.', 'She would like to be empress.')),
        FB(CHOOSE, 'Wir ＿ gern ans Meer fahren.', ['würden', 'hätten', 'wären'], 'würden', ('Avec un infinitif : würden… fahren.', 'With an infinitive: würden… fahren.'), ('Nous aimerions aller à la mer.', 'We would like to go to the seaside.')),
        TF('Der Fischer ist mit seiner Hütte zufrieden.', ('Le pêcheur voudrait autre chose que sa cabane.', 'The fisherman would like something other than his hut.'), FAUX, ('Zufrieden = satisfait.', 'Zufrieden = satisfied.')),
      ]),
    L('de-wenn-irreal', ('L’hypothèse irréelle : wenn ich … wäre', 'The unreal hypothesis: wenn ich … wäre'), ('Imaginer ce qu’on ferait dans une situation qui n’existe pas.', 'Imagine what you would do in a situation that does not exist.'), 9, [
        ('Condition irréelle : Konjunktiv II dans les deux propositions. Wenn ich reich wäre, würde ich ein Schloss kaufen (si j’étais riche, j’achèterais un château).', 'Unreal condition: Konjunktiv II in both clauses. Wenn ich reich wäre, würde ich ein Schloss kaufen (if I were rich, I would buy a castle).'),
        ('Attention : en français, « si » est suivi de l’imparfait ; en allemand, wenn est suivi du Konjunktiv II, verbe à la fin. Wenn ich Zeit hätte, käme ich mit.', 'Careful: in French “si” is followed by the imperfect; in German, wenn is followed by Konjunktiv II, verb at the end. Wenn ich Zeit hätte, käme ich mit.'),
        ('Pour un regret : An deiner Stelle würde ich… (à ta place, je…). Wenn ich doch nur… ! (si seulement je… !). Wenn ich doch nur mehr Geduld hätte!', 'For a regret: An deiner Stelle würde ich… (if I were you, I would…). Wenn ich doch nur…! (if only I…!). Wenn ich doch nur mehr Geduld hätte!'),
      ], [
        DG('wenn-irreal', 'Wenn ich … wäre / hätte, würde ich …', ('Si j’étais / j’avais…, je…', 'If I were / had…, I would…')),
        D('an-deiner-stelle', 'an deiner Stelle', ('à ta place', 'if I were you, in your place')),
        DG('wenn-doch-nur', 'Wenn ich doch nur …!', ('Si seulement je… !', 'If only I…!')),
        D('meer', 'das Meer', ('la mer', 'the sea')),
        D('huette', 'die Hütte', ('la cabane, la hutte', 'the hut')),
        D('schloss', 'das Schloss', ('le château', 'the castle, the palace')),
        D('sturm', 'der Sturm', ('la tempête', 'the storm')),
        D('verlieren-alles', 'alles verlieren', ('tout perdre', 'to lose everything')),
      ], [
        x('Wenn ich Königin wäre, hätte ich ein Schloss aus Gold.', 'Si j’étais reine, j’aurais un château en or.', 'If I were queen, I would have a castle made of gold.'),
        x('An deiner Stelle würde ich zufrieden sein. Sonst verlierst du alles.', 'À ta place, je serais satisfaite. Sinon, tu perdras tout.', 'If I were you, I would be content. Otherwise you will lose everything.'),
      ], [
        FB(CHOOSE, 'Wenn ich reich ＿, würde ich viel reisen.', ['wäre', 'bin', 'würde'], 'wäre', ('Après wenn irréel : Konjunktiv II, wäre.', 'After unreal wenn: Konjunktiv II, wäre.'), ('Si j’étais riche, je voyagerais beaucoup.', 'If I were rich, I would travel a lot.')),
        FB(CHOOSE, 'Wenn wir Zeit hätten, ＿ wir dich besuchen.', ['würden', 'werden', 'hätten'], 'würden', ('Principale : würden + infinitif.', 'Main clause: würden + infinitive.'), ('Si nous avions le temps, nous te rendrions visite.', 'If we had time, we would visit you.')),
        order(('Remets dans l’ordre : « À ta place, je resterais à la maison. »', 'Put in order: “If I were you, I would stay at home.”'), ['An', 'deiner', 'Stelle', 'würde', 'ich', 'zu', 'Hause', 'bleiben.'], ('An deiner Stelle en tête, puis würde, le sujet, et l’infinitif à la fin.', 'An deiner Stelle first, then würde, the subject, and the infinitive at the end.')),
        DC(ANSWER, [('Fisch', 'Was würdest du dir wünschen?')], ('Le poisson magique te demande ton vœu (tu voudrais une petite maison).', 'The magic fish asks for your wish (you would like a small house).'), ['Ich hätte gern ein kleines Haus.', 'Ich habe gern ein kleines Haus gehabt.', 'Wenn ich ein Haus bin.'], 'Ich hätte gern ein kleines Haus.', ('Souhait : ich hätte gern…', 'Wish: ich hätte gern…')),
      ]),
  ]),
  CH('goetheb1-w3-c2', ('La mer se fâche', 'The sea grows angry'), [
    L('de-ratschlag', ('Proposer et conseiller', 'Suggesting and advising'), ('Faire une proposition polie, donner un conseil et y réagir.', 'Make a polite suggestion, give advice and respond to it.'), 8, [
        ('Proposer : Wir könnten ins Kino gehen (nous pourrions…). Wie wäre es mit einem Spaziergang? (que dirais-tu d’une promenade ?). Hättest du Lust, mitzukommen?', 'Suggesting: Wir könnten ins Kino gehen (we could…). Wie wäre es mit einem Spaziergang? (how about a walk?). Hättest du Lust, mitzukommen?'),
        ('Conseiller : Du solltest mit ihr sprechen. Ich würde dir raten, zu warten. Es wäre besser, wenn du jetzt gehst.', 'Advising: Du solltest mit ihr sprechen. Ich würde dir raten, zu warten. Es wäre besser, wenn du jetzt gehst.'),
        ('Réagir : Das ist eine gute Idee. Einverstanden! (d’accord !). Ich weiß nicht… Lieber nicht (plutôt pas). Das kommt nicht in Frage (il n’en est pas question).', 'Responding: Das ist eine gute Idee. Einverstanden! (agreed!). Ich weiß nicht… Lieber nicht (I’d rather not). Das kommt nicht in Frage (that is out of the question).'),
      ], [
        D('wie-waere-es', 'Wie wäre es mit …?', ('Que dirais-tu de… ?', 'How about…?')),
        D('lust-haben', 'Lust haben', ('avoir envie', 'to feel like (doing)')),
        D('raten', 'raten', ('conseiller', 'to advise')),
        D('einverstanden', 'Einverstanden!', ('D’accord !', 'Agreed!')),
        D('lieber-nicht', 'Lieber nicht.', ('Plutôt pas.', 'I’d rather not.')),
        D('nicht-in-frage', 'Das kommt nicht in Frage.', ('Il n’en est pas question.', 'That is out of the question.')),
        D('vorschlag', 'der Vorschlag', ('la proposition', 'the suggestion')),
        D('es-waere-besser', 'Es wäre besser, wenn …', ('Il vaudrait mieux que…', 'It would be better if…')),
      ], [
        x('Wie wäre es mit einem kleinen Haus? — Einverstanden, aber nur für den Anfang!', 'Que dirais-tu d’une petite maison ? — D’accord, mais seulement pour commencer !', 'How about a small house? — Agreed, but only to begin with!'),
        x('Es wäre besser, wenn du den Fisch nicht noch einmal rufst.', 'Il vaudrait mieux que tu n’appelles pas le poisson encore une fois.', 'It would be better if you did not call the fish again.'),
      ], [
        FB(COMPLETE, 'Wie ＿ es mit einem Kaffee?', ['wäre', 'hätte', 'würde'], 'wäre', ('Proposer : Wie wäre es mit…?', 'Suggesting: Wie wäre es mit…?'), ('Que dirais-tu d’un café ?', 'How about a coffee?')),
        FB(COMPLETE, 'Hast du ＿, heute Abend auszugehen?', ['Lust', 'Wunsch', 'Vorschlag'], 'Lust', ('Avoir envie : Lust haben.', 'To feel like: Lust haben.'), ('As-tu envie de sortir ce soir ?', 'Do you feel like going out tonight?')),
        DC(ANSWER, [('Fischer', 'Soll ich den Fisch noch einmal rufen?')], ('Le pêcheur hésite à rappeler le poisson (tu le lui déconseilles).', 'The fisherman hesitates to call the fish again (you advise against it).'), ['Lieber nicht. Du solltest zufrieden sein.', 'Einverstanden, du wärst rufen.', 'Wie wäre es, du rufst würde.'], 'Lieber nicht. Du solltest zufrieden sein.', ('Déconseiller : Lieber nicht ; conseil : du solltest…', 'Advising against: Lieber nicht; advice: du solltest…')),
        TF('Das kommt nicht in Frage!', ('La personne accepte la proposition.', 'The person accepts the suggestion.'), FAUX, ('C’est un refus net : il n’en est pas question.', 'It is a flat refusal: out of the question.')),
      ]),
  ])])

# ═════════════════════════ 4 : Le passif, la ville et l'environnement ═════════════════════════
W4 = WORLD('goetheb1-w4', ('Les ateliers de Cologne', 'The workshops of Cologne'), REGION,
  ('Dire ce qui est fait sans nommer qui le fait avec le passif, au présent, au prétérit et avec un verbe de modalité ; parler d’environnement.', 'Say what is done without naming who does it with the passive, in the present, the simple past and with a modal verb; talk about the environment.'),
  (('Les Lutins de Cologne', 'The Elves of Cologne'), '♙', ('La nuit, à Cologne, le pain est cuit, les habits sont cousus, les maisons sont bâties… sans que personne ne voie les Lutins. Dis ce qui est fait et par qui, sans jamais les surprendre, sinon ils partiront pour toujours !', 'At night in Cologne, the bread is baked, the clothes are sewn, the houses are built… without anyone seeing the Elves. Say what is done and by whom, without ever catching them out, or they will leave for ever!')),
  [CH('goetheb1-w4-c1', ('Pendant que la ville dort', 'While the town sleeps'), [
    L('de-passiv-praesens', ('Le passif : werden + participe', 'The passive: werden + participle'), ('Décrire une action sans dire qui la fait.', 'Describe an action without saying who does it.'), 9, [
        ('Le passif : werden conjugué + participe passé à la fin. Das Brot wird gebacken (le pain est cuit, on cuit le pain). Die Häuser werden gebaut.', 'The passive: conjugated werden + past participle at the end. Das Brot wird gebacken (the bread is baked). Die Häuser werden gebaut.'),
        ('L’objet à l’accusatif de la phrase active devient sujet : Der Bäcker backt den Kuchen → Der Kuchen wird gebacken. L’auteur de l’action s’ajoute avec von + datif : von dem Bäcker.', 'The accusative object of the active sentence becomes the subject: Der Bäcker backt den Kuchen → Der Kuchen wird gebacken. The agent is added with von + dative: von dem Bäcker.'),
        ('Le passif remplace souvent « on » : Hier wird Deutsch gesprochen (ici, on parle allemand). On peut aussi dire man : Hier spricht man Deutsch.', 'The passive often replaces “one / they”: Hier wird Deutsch gesprochen (German is spoken here). You can also use man: Hier spricht man Deutsch.'),
      ], [
        DG('passiv', 'werden + Partizip II (Passiv)', ('passif (werden + participe)', 'passive (werden + participle)')),
        DG('von-agens', 'von + Dativ (Passiv)', ('par (auteur de l’action)', 'by (agent of the action)')),
        DG('man', 'man', ('on', 'one, people (impersonal)')),
        D('bauen', 'bauen', ('construire', 'to build')),
        D('backen', 'backen', ('cuire (au four), faire du pain', 'to bake')),
        D('naehen', 'nähen', ('coudre', 'to sew')),
        D('reparieren', 'reparieren', ('réparer', 'to repair')),
        D('werkstatt', 'die Werkstatt', ('l’atelier', 'the workshop')),
        D('heimlich', 'heimlich', ('en secret, en cachette', 'secretly')),
      ], [
        x('In der Nacht wird das Brot gebacken und die Kleidung genäht.', 'La nuit, le pain est cuit et les vêtements sont cousus.', 'At night the bread is baked and the clothes are sewn.'),
        x('Die ganze Arbeit wird heimlich von den Heinzelmännchen gemacht.', 'Tout le travail est fait en secret par les lutins.', 'All the work is secretly done by the elves.'),
      ], [
        FB(CHOOSE, 'Das Haus ＿ in drei Monaten gebaut.', ['wird', 'ist', 'hat'], 'wird', ('Passif : wird + participe.', 'Passive: wird + participle.'), ('La maison est construite en trois mois.', 'The house is built in three months.')),
        FB(CHOOSE, 'Die Fenster werden jede Woche ＿.', ['geputzt', 'putzen', 'putzt'], 'geputzt', ('Passif : participe à la fin.', 'Passive: participle at the end.'), ('Les fenêtres sont nettoyées chaque semaine.', 'The windows are cleaned every week.')),
        FB(CHOOSE, 'Der Kuchen wird ＿ Bäcker gebacken.', ['vom', 'durch', 'mit dem'], 'vom', ('L’auteur de l’action : von + datif (von dem = vom).', 'The agent: von + dative (von dem = vom).'), ('Le gâteau est fait par le boulanger.', 'The cake is baked by the baker.')),
        order(('Remets dans l’ordre : « Ici, on parle allemand. »', 'Put in order: “German is spoken here.”'), ['Hier', 'wird', 'Deutsch', 'gesprochen.'], ('Wird en deuxième position, le participe à la fin.', 'Wird in second position, the participle at the end.')),
      ]),
    L('de-passiv-praet', ('Le passif au passé et avec un verbe de modalité', 'The passive in the past and with a modal verb'), ('Dire ce qui a été fait et ce qui doit être fait.', 'Say what was done and what must be done.'), 8, [
        ('Au prétérit : wurde + participe. Der Kölner Dom wurde 1880 fertig gebaut. Die Briefe wurden gestern geschickt.', 'In the simple past: wurde + participle. Der Kölner Dom wurde 1880 fertig gebaut. Die Briefe wurden gestern geschickt.'),
        ('Au Perfekt : ist + participe + worden (sans ge-). Das Auto ist repariert worden.', 'In the Perfekt: ist + participle + worden (no ge-). Das Auto ist repariert worden.'),
        ('Avec un verbe de modalité : modal + participe + werden. Das Formular muss ausgefüllt werden (le formulaire doit être rempli). Hier darf nicht geparkt werden.', 'With a modal verb: modal + participle + werden. Das Formular muss ausgefüllt werden (the form must be filled in). Hier darf nicht geparkt werden.'),
      ], [
        DG('passiv-praet', 'wurde + Partizip II', ('passif au prétérit', 'passive in the simple past')),
        DG('passiv-perfekt', 'ist … worden', ('passif au passé composé', 'passive in the perfect')),
        DG('passiv-modal', 'muss / kann / darf + Partizip II + werden', ('passif avec verbe de modalité', 'passive with a modal verb')),
        D('ausfuellen', 'ausfüllen', ('remplir (un formulaire)', 'to fill in (a form)')),
        D('erfinden', 'erfinden', ('inventer', 'to invent')),
        D('gruenden', 'gründen', ('fonder', 'to found')),
        D('zerstoeren', 'zerstören', ('détruire', 'to destroy')),
        D('jahrhundert', 'das Jahrhundert', ('le siècle', 'the century')),
      ], [
        x('Die Stadt Köln wurde vor zweitausend Jahren von den Römern gegründet.', 'La ville de Cologne a été fondée il y a deux mille ans par les Romains.', 'The city of Cologne was founded two thousand years ago by the Romans.'),
        x('Die Heinzelmännchen dürfen bei der Arbeit nicht gesehen werden.', 'Les lutins ne doivent pas être vus pendant leur travail.', 'The elves must not be seen at work.'),
      ], [
        FB(CHOOSE, 'Der Buchdruck ＿ von Gutenberg erfunden.', ['wurde', 'wird', 'hat'], 'wurde', ('Fait passé : wurde + participe.', 'A past fact: wurde + participle.'), ('L’imprimerie a été inventée par Gutenberg.', 'Printing was invented by Gutenberg.')),
        FB(CHOOSE, 'Das Formular muss heute ausgefüllt ＿.', ['werden', 'worden', 'wird'], 'werden', ('Modal + participe + werden.', 'Modal + participle + werden.'), ('Le formulaire doit être rempli aujourd’hui.', 'The form must be filled in today.')),
        FB(CHOOSE, 'Mein Fahrrad ist repariert ＿.', ['worden', 'geworden', 'werden'], 'worden', ('Passif au Perfekt : worden, sans ge-.', 'Passive in the Perfekt: worden, no ge-.'), ('Mon vélo a été réparé.', 'My bicycle has been repaired.')),
        TF('Im Krieg wurden viele Häuser zerstört.', ('Beaucoup de maisons ont été construites pendant la guerre.', 'Many houses were built during the war.'), FAUX, ('Zerstört = détruites.', 'Zerstört = destroyed.')),
      ]),
  ]),
  CH('goetheb1-w4-c2', ('Une ville propre', 'A clean town'), [
    L('de-umwelt', ('L’environnement', 'The environment'), ('Parler du tri, de l’énergie et des gestes du quotidien.', 'Talk about recycling, energy and everyday habits.'), 8, [
        ('En Allemagne, le tri est une affaire sérieuse : der Müll (les déchets), den Müll trennen (trier), die Mülltonne (la poubelle), das Altpapier (le vieux papier), der Pfand (la consigne des bouteilles).', 'In Germany recycling is serious business: der Müll (rubbish), den Müll trennen (to sort), die Mülltonne (the bin), das Altpapier (waste paper), der Pfand (the bottle deposit).'),
        ('Die Umwelt schützen (protéger l’environnement), Energie sparen (économiser l’énergie), Wasser verschwenden (gaspiller l’eau), umweltfreundlich (écologique).', 'Die Umwelt schützen (to protect the environment), Energie sparen (to save energy), Wasser verschwenden (to waste water), umweltfreundlich (environmentally friendly).'),
        ('Pour dire son engagement : Ich achte darauf, weniger Plastik zu benutzen (je fais attention à utiliser moins de plastique). Statt mit dem Auto fahre ich mit dem Rad (au lieu de…).', 'To state your commitment: Ich achte darauf, weniger Plastik zu benutzen (I take care to use less plastic). Statt mit dem Auto fahre ich mit dem Rad (instead of…).'),
      ], [
        D('umwelt', 'die Umwelt', ('l’environnement', 'the environment')),
        D('muell', 'der Müll', ('les déchets, les ordures', 'rubbish, waste')),
        D('muell-trennen', 'den Müll trennen', ('trier les déchets', 'to sort the rubbish')),
        D('schuetzen', 'schützen', ('protéger', 'to protect')),
        D('sparen', 'sparen', ('économiser', 'to save (money, energy)')),
        D('verschwenden', 'verschwenden', ('gaspiller', 'to waste')),
        D('umweltfreundlich', 'umweltfreundlich', ('écologique, respectueux de l’environnement', 'environmentally friendly')),
        D('statt', 'statt', ('au lieu de', 'instead of')),
      ], [
        x('In Deutschland wird der Müll getrennt: Papier, Glas, Plastik und Bio.', 'En Allemagne, les déchets sont triés : papier, verre, plastique et bio.', 'In Germany rubbish is sorted: paper, glass, plastic and organic.'),
        x('Wir sollten Energie sparen und kein Wasser verschwenden.', 'Nous devrions économiser l’énergie et ne pas gaspiller l’eau.', 'We should save energy and not waste water.'),
      ], [
        FB(COMPLETE, 'Papier und Glas kommen nicht in dieselbe Tonne: Man muss den Müll ＿.', ['trennen', 'sparen', 'schützen'], 'trennen', ('Trier : den Müll trennen.', 'To sort: den Müll trennen.'), ('Le papier et le verre ne vont pas dans la même poubelle : il faut trier les déchets.', 'Paper and glass do not go in the same bin: you have to sort the rubbish.')),
        FB(COMPLETE, 'Mach das Licht aus! Wir müssen Energie ＿.', ['sparen', 'verschwenden', 'trennen'], 'sparen', ('Économiser : sparen.', 'To save: sparen.'), ('Éteins la lumière ! Nous devons économiser l’énergie.', 'Turn off the light! We have to save energy.')),
        TF('Mit dem Fahrrad zu fahren ist umweltfreundlich.', ('Aller à vélo est mauvais pour l’environnement.', 'Cycling is bad for the environment.'), FAUX, ('Umweltfreundlich = respectueux de l’environnement.', 'Umweltfreundlich = environmentally friendly.')),
        DC(ANSWER, [('Nachbarin', 'Was machen Sie für die Umwelt?')], ('Ta voisine te demande ce que tu fais pour l’environnement (tu tries et tu prends le vélo).', 'Your neighbour asks what you do for the environment (you sort rubbish and cycle).'), ['Ich trenne den Müll und fahre mit dem Rad.', 'Ich verschwende den Müll mit dem Rad.', 'Der Müll wird mich getrennt.'], 'Ich trenne den Müll und fahre mit dem Rad.', ('Deux actions au présent, reliées par und.', 'Two actions in the present, joined by und.')),
      ]),
  ])])

# ═════════════════════════ 5 : zu + infinitif, le but, le monde du travail ═════════════════════════
W5 = WORLD('goetheb1-w5', ('Le cabinet du Docteur Faust', 'Doctor Faust’s study'), REGION,
  ('Employer l’infinitif avec zu, exprimer le but avec um… zu et damit, poser sa candidature et parler de sa formation.', 'Use the infinitive with zu, express purpose with um… zu and damit, apply for a job and talk about your training.'),
  (('Le Docteur Faust', 'Doctor Faust'), '♗', ('Le Docteur Faust a tout étudié et veut encore tout savoir. Avant de signer quoi que ce soit, il exige une lettre de candidature irréprochable : pourquoi viens-tu, dans quel but, qu’as-tu l’intention de faire ?', 'Doctor Faust has studied everything and still wants to know it all. Before signing anything, he demands a flawless letter of application: why have you come, for what purpose, what do you intend to do?')),
  [CH('goetheb1-w5-c1', ('Tout savoir', 'To know everything'), [
    L('de-zu-infinitiv', ('L’infinitif avec zu', 'The infinitive with zu'), ('Compléter un verbe, un nom ou un adjectif par un infinitif.', 'Complete a verb, a noun or an adjective with an infinitive.'), 8, [
        ('Après beaucoup de verbes et d’expressions, l’infinitif est précédé de zu et placé à la fin : Ich versuche, pünktlich zu kommen. Es ist schwer, Deutsch zu lernen. Ich habe keine Lust, zu arbeiten.', 'After many verbs and expressions, the infinitive is preceded by zu and placed at the end: Ich versuche, pünktlich zu kommen. Es ist schwer, Deutsch zu lernen. Ich habe keine Lust, zu arbeiten.'),
        ('Avec un verbe à particule, zu se glisse entre la particule et le verbe : anzufangen, aufzuhören, einzukaufen. Er hat vergessen, mich anzurufen.', 'With a separable verb, zu slips between the prefix and the verb: anzufangen, aufzuhören, einzukaufen. Er hat vergessen, mich anzurufen.'),
        ('Pas de zu après les verbes de modalité, ni après werden, lassen, gehen, bleiben, sehen, hören : Ich muss arbeiten. Ich gehe einkaufen. Ich lasse mein Auto reparieren.', 'No zu after modal verbs, or after werden, lassen, gehen, bleiben, sehen, hören: Ich muss arbeiten. Ich gehe einkaufen. Ich lasse mein Auto reparieren.'),
      ], [
        DG('zu-inf', 'zu + Infinitiv', ('zu + infinitif', 'zu + infinitive')),
        D('versuchen', 'versuchen', ('essayer', 'to try')),
        D('vergessen', 'vergessen', ('oublier', 'to forget')),
        D('anfangen-zu', 'anfangen, … zu …', ('commencer à…', 'to begin to…')),
        D('aufhoeren', 'aufhören', ('arrêter, cesser', 'to stop (doing)')),
        D('sich-entscheiden', 'sich entscheiden', ('se décider', 'to make up one’s mind')),
        DG('lassen', 'lassen + Infinitiv', ('faire faire, laisser', 'to have (something done), to let')),
        D('wissen-n', 'das Wissen', ('le savoir', 'knowledge')),
      ], [
        x('Faust versucht, alle Bücher der Welt zu lesen.', 'Faust essaie de lire tous les livres du monde.', 'Faust tries to read all the books in the world.'),
        x('Er hat sich entschieden, mit dem Studieren aufzuhören.', 'Il a décidé d’arrêter d’étudier.', 'He has decided to stop studying.'),
      ], [
        FB(CHOOSE, 'Ich habe vergessen, dich ＿.', ['anzurufen', 'zu anrufen', 'anrufen'], 'anzurufen', ('Verbe à particule : an-zu-rufen.', 'Separable verb: an-zu-rufen.'), ('J’ai oublié de t’appeler.', 'I forgot to call you.')),
        FB(CHOOSE, 'Es ist nicht leicht, eine Wohnung ＿.', ['zu finden', 'finden', 'gefunden'], 'zu finden', ('Es ist leicht / schwer + zu + infinitif.', 'Es ist leicht / schwer + zu + infinitive.'), ('Il n’est pas facile de trouver un appartement.', 'It is not easy to find a flat.')),
        FB(CHOOSE, 'Ich muss heute lange ＿.', ['arbeiten', 'zu arbeiten', 'gearbeitet'], 'arbeiten', ('Après un verbe de modalité : pas de zu.', 'After a modal verb: no zu.'), ('Je dois travailler longtemps aujourd’hui.', 'I have to work late today.')),
        order(('Remets dans l’ordre : « J’essaie d’arriver à l’heure. »', 'Put in order: “I try to arrive on time.”'), ['Ich', 'versuche,', 'pünktlich', 'zu', 'kommen.'], ('Zu + infinitif à la fin.', 'Zu + infinitive at the end.')),
      ]),
    L('de-um-zu', ('Le but : um … zu et damit', 'Purpose: um … zu and damit'), ('Dire dans quel but on fait quelque chose.', 'Say for what purpose you do something.'), 8, [
        ('Wozu? (dans quel but ?). Même sujet dans les deux propositions : um… zu + infinitif. Ich lerne Deutsch, um in Berlin zu arbeiten (pour travailler à Berlin).', 'Wozu? (what for?). Same subject in both clauses: um… zu + infinitive. Ich lerne Deutsch, um in Berlin zu arbeiten (in order to work in Berlin).'),
        ('Sujets différents : damit + verbe conjugué à la fin. Ich spreche langsam, damit du mich verstehst (pour que tu me comprennes).', 'Different subjects: damit + conjugated verb at the end. Ich spreche langsam, damit du mich verstehst (so that you understand me).'),
        ('Deux cousins de um… zu : ohne… zu (sans) et statt… zu (au lieu de). Er ging, ohne ein Wort zu sagen. Statt zu arbeiten, träumt er.', 'Two cousins of um… zu: ohne… zu (without) and statt… zu (instead of). Er ging, ohne ein Wort zu sagen. Statt zu arbeiten, träumt er.'),
      ], [
        DG('um-zu', 'um … zu + Infinitiv', ('pour + infinitif', 'in order to + verb')),
        DG('damit', 'damit', ('pour que, afin que', 'so that')),
        DG('ohne-zu', 'ohne … zu', ('sans + infinitif', 'without + -ing')),
        D('wozu', 'Wozu?', ('Dans quel but ?', 'What for?')),
        D('ziel', 'das Ziel', ('le but, l’objectif', 'the goal, the aim')),
        D('erreichen', 'erreichen', ('atteindre', 'to reach, to achieve')),
        D('verstehen', 'verstehen', ('comprendre', 'to understand')),
        D('vertrag', 'der Vertrag', ('le contrat', 'the contract')),
      ], [
        x('Faust unterschreibt einen Vertrag, um alles zu wissen.', 'Faust signe un contrat pour tout savoir.', 'Faust signs a contract in order to know everything.'),
        x('Er liest den Vertrag nicht, damit niemand seine Angst sieht.', 'Il ne lit pas le contrat, pour que personne ne voie sa peur.', 'He does not read the contract, so that nobody sees his fear.'),
      ], [
        FB(CHOOSE, 'Ich spare Geld, ＿ ein Auto zu kaufen.', ['um', 'damit', 'ohne'], 'um', ('Même sujet : um… zu.', 'Same subject: um… zu.'), ('J’économise pour acheter une voiture.', 'I am saving money in order to buy a car.')),
        FB(CHOOSE, 'Ich schreibe es auf, ＿ du es nicht vergisst.', ['damit', 'um', 'dass'], 'damit', ('Sujets différents (ich / du) : damit.', 'Different subjects (ich / du): damit.'), ('Je le note pour que tu ne l’oublies pas.', 'I am writing it down so that you do not forget it.')),
        FB(CHOOSE, 'Er ging weg, ＿ sich zu verabschieden.', ['ohne', 'um', 'damit'], 'ohne', ('Sans dire au revoir : ohne… zu.', 'Without saying goodbye: ohne… zu.'), ('Il est parti sans dire au revoir.', 'He left without saying goodbye.')),
        DC(ANSWER, [('Faust', 'Wozu lernen Sie Deutsch?')], ('Faust te demande dans quel but tu apprends l’allemand (pour étudier en Allemagne).', 'Faust asks what you are learning German for (to study in Germany).'), ['Um in Deutschland zu studieren.', 'Damit in Deutschland zu studieren.', 'Um ich in Deutschland studiere.'], 'Um in Deutschland zu studieren.', ('But, même sujet : um… zu + infinitif.', 'Purpose, same subject: um… zu + infinitive.')),
      ]),
  ]),
  CH('goetheb1-w5-c2', ('La lettre de candidature', 'The letter of application'), [
    L('de-bewerbung', ('La candidature et la formation', 'Applications and training'), ('Parler de son parcours et se présenter pour un poste.', 'Talk about your background and apply for a position.'), 9, [
        ('Le parcours : die Ausbildung (la formation professionnelle), das Studium (les études supérieures), das Praktikum (le stage), der Abschluss (le diplôme), die Erfahrung (l’expérience).', 'Your background: die Ausbildung (vocational training), das Studium (university studies), das Praktikum (the internship), der Abschluss (the qualification), die Erfahrung (experience).'),
        ('Postuler : sich um eine Stelle bewerben (postuler à un poste), die Bewerbung (la candidature), der Lebenslauf (le CV), das Vorstellungsgespräch (l’entretien d’embauche).', 'Applying: sich um eine Stelle bewerben (to apply for a position), die Bewerbung (the application), der Lebenslauf (the CV), das Vorstellungsgespräch (the job interview).'),
        ('Formules utiles : Ich interessiere mich für die Stelle als… Ich habe drei Jahre Erfahrung im Verkauf. Ich würde mich über eine Einladung zum Gespräch freuen.', 'Useful phrases: Ich interessiere mich für die Stelle als… Ich habe drei Jahre Erfahrung im Verkauf. Ich würde mich über eine Einladung zum Gespräch freuen.'),
      ], [
        D('ausbildung', 'die Ausbildung', ('la formation professionnelle', 'vocational training')),
        D('studium', 'das Studium', ('les études (supérieures)', 'university studies')),
        D('praktikum', 'das Praktikum', ('le stage', 'the internship')),
        D('erfahrung', 'die Erfahrung', ('l’expérience', 'the experience')),
        D('stelle', 'die Stelle', ('le poste, l’emploi', 'the position, the job')),
        D('sich-bewerben', 'sich bewerben um', ('postuler à', 'to apply for')),
        D('lebenslauf', 'der Lebenslauf', ('le CV', 'the CV, the résumé')),
        D('vorstellungsgespraech', 'das Vorstellungsgespräch', ('l’entretien d’embauche', 'the job interview')),
        D('sich-interessieren', 'sich interessieren für', ('s’intéresser à', 'to be interested in')),
      ], [
        x('Ich habe eine Ausbildung als Koch gemacht und zwei Jahre Erfahrung.', 'J’ai fait une formation de cuisinier et j’ai deux ans d’expérience.', 'I trained as a cook and have two years’ experience.'),
        x('Ich möchte mich um die Stelle bewerben. Mein Lebenslauf liegt bei.', 'Je souhaite postuler à ce poste. Mon CV est joint.', 'I would like to apply for the position. My CV is enclosed.'),
      ], [
        FB(COMPLETE, 'Nach der Schule hat sie eine ＿ als Bäckerin gemacht.', ['Ausbildung', 'Erfahrung', 'Stelle'], 'Ausbildung', ('Formation professionnelle : die Ausbildung.', 'Vocational training: die Ausbildung.'), ('Après l’école, elle a fait une formation de boulangère.', 'After school she trained as a baker.')),
        FB(CHOOSE, 'Ich interessiere mich ＿ die Stelle als Verkäufer.', ['für', 'um', 'auf'], 'für', ('Sich interessieren für + accusatif.', 'Sich interessieren für + accusative.'), ('Je m’intéresse au poste de vendeur.', 'I am interested in the position of shop assistant.')),
        FB(CHOOSE, 'Er hat sich ＿ eine Stelle bei der Post beworben.', ['um', 'für', 'an'], 'um', ('Sich bewerben um + accusatif.', 'Sich bewerben um + accusative.'), ('Il a postulé à un poste à la poste.', 'He applied for a job at the post office.')),
        DC(ANSWER, [('Chefin', 'Warum möchten Sie bei uns arbeiten?')], ('En entretien, on te demande pourquoi tu veux ce poste (tu as de l’expérience et le poste t’intéresse).', 'In an interview you are asked why you want the job (you have experience and are interested).'), ['Weil ich Erfahrung habe und mich für die Stelle interessiere.', 'Weil ich habe Erfahrung und interessiere die Stelle.', 'Um ich Erfahrung habe.'], 'Weil ich Erfahrung habe und mich für die Stelle interessiere.', ('Weil + verbes à la fin ; sich interessieren für.', 'Weil + verbs at the end; sich interessieren für.')),
      ]),
  ])])

# ═════════════════════════ 6 : Concéder, conclure, donner son avis ═════════════════════════
W6 = WORLD('goetheb1-w6', ('Les tours de Till l’Espiègle', 'Till Eulenspiegel’s tricks'), REGION,
  ('Opposer et conclure avec obwohl, trotzdem et deshalb, défendre une opinion, parler des médias.', 'Contrast and conclude with obwohl, trotzdem and deshalb, defend an opinion, talk about the media.'),
  (('Till l’Espiègle', 'Till Eulenspiegel'), '♘', ('Till l’Espiègle prend tout au pied de la lettre et retourne chaque phrase contre celui qui la dit. Discute avec lui sans te faire piéger : bien que…, pourtant…, c’est pourquoi…', 'Till Eulenspiegel takes everything literally and turns every sentence against the person who says it. Argue with him without getting caught: although…, nevertheless…, that is why…')),
  [CH('goetheb1-w6-c1', ('Bien que…, pourtant…', 'Although…, nevertheless…'), [
    L('de-obwohl', ('Concéder : obwohl et trotzdem', 'Conceding: obwohl and trotzdem'), ('Exprimer une opposition entre deux faits.', 'Express a contrast between two facts.'), 8, [
        ('Obwohl (bien que) introduit une subordonnée, verbe à la fin, et toujours à l’indicatif : Obwohl es regnet, gehen wir spazieren.', 'Obwohl (although) introduces a subordinate clause, verb at the end, always in the indicative: Obwohl es regnet, gehen wir spazieren.'),
        ('Trotzdem (pourtant, malgré tout) est un adverbe : il occupe la première place et le verbe le suit. Es regnet. Trotzdem gehen wir spazieren.', 'Trotzdem (nevertheless) is an adverb: it takes first position and the verb follows. Es regnet. Trotzdem gehen wir spazieren.'),
        ('Avec un nom : trotz + génitif (malgré). Trotz des Regens gehen wir spazieren. Aber et doch relient deux principales sans changer l’ordre.', 'With a noun: trotz + genitive (despite). Trotz des Regens gehen wir spazieren. Aber and doch link two main clauses without changing the order.'),
      ], [
        DG('obwohl', 'obwohl', ('bien que', 'although')),
        DG('trotzdem', 'trotzdem', ('pourtant, malgré tout', 'nevertheless, all the same')),
        DG('trotz', 'trotz + Genitiv', ('malgré', 'despite, in spite of')),
        D('narr', 'der Narr', ('le fou, le bouffon', 'the fool, the jester')),
        D('streich', 'der Streich', ('la farce, le mauvais tour', 'the prank, the trick')),
        D('woertlich', 'wörtlich', ('au pied de la lettre, littéralement', 'literally')),
        D('boese', 'böse', ('fâché ; méchant', 'angry; wicked')),
        D('sich-beschweren', 'sich beschweren', ('se plaindre', 'to complain')),
      ], [
        x('Obwohl Till arm war, lachte er über die reichen Leute.', 'Bien que Till fût pauvre, il se moquait des gens riches.', 'Although Till was poor, he laughed at rich people.'),
        x('Die Leute waren böse. Trotzdem erzählten sie seine Streiche weiter.', 'Les gens étaient fâchés. Pourtant, ils continuaient à raconter ses farces.', 'People were angry. Nevertheless, they went on telling his pranks.'),
      ], [
        FB(CHOOSE, '＿ er krank ist, geht er zur Arbeit.', ['Obwohl', 'Trotzdem', 'Trotz'], 'Obwohl', ('Le verbe ist est à la fin : c’est obwohl.', 'The verb ist is at the end: so obwohl.'), ('Bien qu’il soit malade, il va au travail.', 'Although he is ill, he goes to work.')),
        FB(CHOOSE, 'Er ist krank. ＿ geht er zur Arbeit.', ['Trotzdem', 'Obwohl', 'Weil'], 'Trotzdem', ('Le verbe suit immédiatement : c’est trotzdem.', 'The verb follows straight away: so trotzdem.'), ('Il est malade. Pourtant, il va au travail.', 'He is ill. Nevertheless, he goes to work.')),
        FB(CHOOSE, '＿ des schlechten Wetters machen wir einen Ausflug.', ['Trotz', 'Obwohl', 'Trotzdem'], 'Trotz', ('Devant un nom au génitif : trotz.', 'Before a noun in the genitive: trotz.'), ('Malgré le mauvais temps, nous faisons une excursion.', 'Despite the bad weather, we are going on an outing.')),
        order(('Remets dans l’ordre : « Bien qu’il pleuve, nous restons dehors. »', 'Put in order: “Although it is raining, we are staying outside.”'), ['Obwohl', 'es', 'regnet,', 'bleiben', 'wir', 'draußen.'], ('Subordonnée en tête, puis verbe + sujet.', 'Subordinate clause first, then verb + subject.')),
      ]),
    L('de-deshalb', ('Conclure : deshalb, also, sonst', 'Concluding: deshalb, also, sonst'), ('Exprimer la conséquence et l’alternative.', 'Express consequence and the alternative.'), 8, [
        ('Deshalb, deswegen, darum (c’est pourquoi) : en première place, suivis du verbe. Ich war krank. Deshalb bin ich zu Hause geblieben.', 'Deshalb, deswegen, darum (that is why): in first position, followed by the verb. Ich war krank. Deshalb bin ich zu Hause geblieben.'),
        ('Also (donc) conclut ; sonst (sinon) annonce ce qui arrivera autrement : Beeil dich, sonst verpassen wir den Zug.', 'Also (so) concludes; sonst (otherwise) announces what will happen if not: Beeil dich, sonst verpassen wir den Zug.'),
        ('Cause et conséquence, deux manières : Weil ich krank war, blieb ich zu Hause. = Ich war krank, deshalb blieb ich zu Hause. Avec un nom : wegen + génitif (wegen der Krankheit).', 'Cause and consequence, two ways: Weil ich krank war, blieb ich zu Hause. = Ich war krank, deshalb blieb ich zu Hause. With a noun: wegen + genitive (wegen der Krankheit).'),
      ], [
        DG('deshalb', 'deshalb / deswegen', ('c’est pourquoi', 'that is why, therefore')),
        DG('also', 'also', ('donc', 'so, therefore')),
        DG('sonst', 'sonst', ('sinon', 'otherwise')),
        DG('wegen', 'wegen + Genitiv', ('à cause de', 'because of')),
        D('sich-beeilen', 'sich beeilen', ('se dépêcher', 'to hurry')),
        D('verpassen', 'verpassen', ('rater, manquer', 'to miss (a train, a chance)')),
        D('grund', 'der Grund', ('la raison', 'the reason')),
        D('folge', 'die Folge', ('la conséquence', 'the consequence')),
      ], [
        x('Der Bäcker sagte: „Back Eulen und Affen!“ Deshalb backte Till Eulen und Affen aus Brot.', 'Le boulanger dit : « Fais des chouettes et des singes ! » C’est pourquoi Till fit des chouettes et des singes en pain.', 'The baker said: “Bake owls and monkeys!” That is why Till baked owls and monkeys out of bread.'),
        x('Sag genau, was du meinst, sonst macht Till etwas anderes.', 'Dis exactement ce que tu veux dire, sinon Till fera autre chose.', 'Say exactly what you mean, otherwise Till will do something else.'),
      ], [
        FB(CHOOSE, 'Es regnete. ＿ blieben wir zu Hause.', ['Deshalb', 'Weil', 'Obwohl'], 'Deshalb', ('Conséquence, verbe juste après : deshalb.', 'Consequence, verb straight after: deshalb.'), ('Il pleuvait. C’est pourquoi nous sommes restés à la maison.', 'It was raining. That is why we stayed at home.')),
        FB(CHOOSE, 'Beeil dich, ＿ verpassen wir den Bus!', ['sonst', 'deshalb', 'trotzdem'], 'sonst', ('Sinon : sonst.', 'Otherwise: sonst.'), ('Dépêche-toi, sinon nous allons rater le bus !', 'Hurry up, otherwise we will miss the bus!')),
        FB(CHOOSE, '＿ des Streiks fahren heute keine Züge.', ['Wegen', 'Weil', 'Deshalb'], 'Wegen', ('Devant un nom au génitif : wegen.', 'Before a noun in the genitive: wegen.'), ('À cause de la grève, aucun train ne circule aujourd’hui.', 'Because of the strike, no trains are running today.')),
        TF('Ich hatte kein Geld, deshalb habe ich nichts gekauft.', ('La personne a acheté quelque chose.', 'The person bought something.'), FAUX, ('Deshalb… nichts gekauft = c’est pourquoi je n’ai rien acheté.', 'Deshalb… nichts gekauft = that is why I bought nothing.')),
      ]),
  ]),
  CH('goetheb1-w6-c2', ('À chacun son avis', 'To each their opinion'), [
    L('de-meinung', ('Donner son avis et discuter', 'Giving your opinion and discussing'), ('Exprimer son opinion, approuver, contredire et parler des médias.', 'Express your opinion, agree, disagree and talk about the media.'), 9, [
        ('Donner son avis : Meiner Meinung nach… (à mon avis, puis le verbe), Ich bin der Meinung, dass…, Ich bin dafür / dagegen (je suis pour / contre), Ich bin überzeugt, dass…', 'Giving your opinion: Meiner Meinung nach… (in my opinion, then the verb), Ich bin der Meinung, dass…, Ich bin dafür / dagegen (I am for / against it), Ich bin überzeugt, dass…'),
        ('Approuver ou contredire : Da stimme ich dir zu (je suis d’accord avec toi). Das sehe ich anders (je vois cela autrement). Einerseits…, andererseits… (d’un côté…, de l’autre…).', 'Agreeing or disagreeing: Da stimme ich dir zu (I agree with you). Das sehe ich anders (I see that differently). Einerseits…, andererseits… (on the one hand…, on the other…).'),
        ('Les médias : die Zeitung (le journal), die Nachrichten (les informations), die Sendung (l’émission), soziale Medien (les réseaux sociaux), der Vorteil / der Nachteil (l’avantage / l’inconvénient).', 'The media: die Zeitung (the newspaper), die Nachrichten (the news), die Sendung (the programme), soziale Medien (social media), der Vorteil / der Nachteil (the advantage / the disadvantage).'),
      ], [
        D('meiner-meinung-nach', 'meiner Meinung nach', ('à mon avis', 'in my opinion')),
        D('dafuer-dagegen', 'dafür / dagegen sein', ('être pour / contre', 'to be for / against')),
        D('zustimmen', 'zustimmen', ('approuver, être d’accord avec', 'to agree with')),
        D('das-sehe-ich-anders', 'Das sehe ich anders.', ('Je vois cela autrement.', 'I see that differently.')),
        DG('einerseits', 'einerseits …, andererseits …', ('d’un côté…, de l’autre…', 'on the one hand…, on the other hand…')),
        D('vorteil', 'der Vorteil', ('l’avantage', 'the advantage')),
        D('nachteil', 'der Nachteil', ('l’inconvénient', 'the disadvantage')),
        D('zeitung', 'die Zeitung', ('le journal', 'the newspaper')),
        D('nachrichten', 'die Nachrichten', ('les informations, les nouvelles', 'the news')),
      ], [
        x('Meiner Meinung nach haben soziale Medien mehr Nachteile als Vorteile.', 'À mon avis, les réseaux sociaux ont plus d’inconvénients que d’avantages.', 'In my opinion social media have more disadvantages than advantages.'),
        x('Das sehe ich anders. Einerseits kosten sie Zeit, andererseits bleibt man in Kontakt.', 'Je vois cela autrement. D’un côté ils prennent du temps, de l’autre on reste en contact.', 'I see that differently. On the one hand they take up time, on the other hand you stay in touch.'),
      ], [
        order(('Remets dans l’ordre : « À mon avis, c’est faux. »', 'Put in order: “In my opinion that is wrong.”'), ['Meiner', 'Meinung', 'nach', 'ist', 'das', 'falsch.'], ('Meiner Meinung nach occupe la première place, le verbe suit.', 'Meiner Meinung nach takes first position, the verb follows.')),
        FB(COMPLETE, 'Rauchverbot in Restaurants? Ich bin ＿: Rauchen stört beim Essen.', ['dafür', 'dagegen', 'anders'], 'dafür', ('Fumer dérange : la personne est pour l’interdiction, dafür.', 'Smoking is a nuisance: the person is for the ban, dafür.'), ('L’interdiction de fumer au restaurant ? Je suis pour : la fumée dérange pendant le repas.', 'A smoking ban in restaurants? I am for it: smoke is a nuisance while eating.')),
        DC(ANSWER, [('Till', 'Fernsehen macht dumm, oder?')], ('Till affirme que la télévision rend bête (tu n’es pas d’accord).', 'Till claims television makes you stupid (you disagree).'), ['Das sehe ich anders. Es gibt auch gute Sendungen.', 'Da stimme ich dir zu, es gibt auch gute Sendungen.', 'Ich bin dafür, dass dumm.'], 'Das sehe ich anders. Es gibt auch gute Sendungen.', ('Désaccord poli : Das sehe ich anders.', 'Polite disagreement: Das sehe ich anders.')),
        TF('Ein Vorteil ist etwas Positives.', ('Un Vorteil est un inconvénient.', 'A Vorteil is a disadvantage.'), FAUX, ('Der Vorteil = l’avantage ; der Nachteil = l’inconvénient.', 'Der Vorteil = the advantage; der Nachteil = the disadvantage.')),
      ]),
  ])])

# ═════════════════════════ 7 : Le génitif, le voyage et la nature ═════════════════════════
W7 = WORLD('goetheb1-w7', ('Le rocher de la Lorelei', 'The Lorelei rock'), REGION,
  ('Exprimer l’appartenance avec le génitif et ses prépositions, décrire un paysage et un voyage, comparer avec je… desto.', 'Express possession with the genitive and its prepositions, describe a landscape and a journey, compare with je… desto.'),
  (('La Lorelei', 'The Lorelei'), '♫', ('Au sommet de son rocher, la Lorelei peigne ses cheveux d’or et chante ; les bateliers du Rhin oublient le courant. Garde les yeux sur le fleuve et décris le voyage sans te laisser distraire : le chant de la sirène, le bord du fleuve, la fin du jour.', 'On top of her rock, the Lorelei combs her golden hair and sings; the Rhine boatmen forget the current. Keep your eyes on the river and describe the journey without being distracted: the siren’s song, the river bank, the end of the day.')),
  [CH('goetheb1-w7-c1', ('Le chant du fleuve', 'The song of the river'), [
    L('de-genitiv', ('Le génitif', 'The genitive'), ('Exprimer l’appartenance et employer les prépositions suivies du génitif.', 'Express possession and use the prepositions that take the genitive.'), 9, [
        ('Le génitif répond à wessen? (de qui ?). Masculin et neutre : des + nom en -s ou -es (das Lied des Fischers, am Ufer des Flusses). Féminin et pluriel : der (die Farbe der Blume, die Namen der Kinder).', 'The genitive answers wessen? (whose?). Masculine and neuter: des + noun in -s or -es (das Lied des Fischers, am Ufer des Flusses). Feminine and plural: der (die Farbe der Blume, die Namen der Kinder).'),
        ('Avec ein et les possessifs : eines, einer, meines, meiner. Das Haus meines Vaters, das Auto meiner Schwester. Pour un nom propre : -s sans apostrophe (Annas Buch, Heines Gedicht).', 'With ein and possessives: eines, einer, meines, meiner. Das Haus meines Vaters, das Auto meiner Schwester. For a proper name: -s with no apostrophe (Annas Buch, Heines Gedicht).'),
        ('Prépositions suivies du génitif : während (pendant), wegen (à cause de), trotz (malgré), innerhalb (à l’intérieur de, en moins de), außerhalb (en dehors de). Während der Fahrt, innerhalb einer Woche.', 'Prepositions that take the genitive: während (during), wegen (because of), trotz (despite), innerhalb (inside, within), außerhalb (outside). Während der Fahrt, innerhalb einer Woche.'),
      ], [
        DG('genitiv', 'des / der (Genitiv)', ('du, de la, des (génitif)', 'of the (genitive)')),
        DG('genitiv-s', 'des Flusses, des Fischers', ('nom masculin ou neutre au génitif (-s, -es)', 'masculine or neuter noun in the genitive (-s, -es)')),
        DG('wessen', 'Wessen?', ('De qui ? À qui ?', 'Whose?')),
        DG('waehrend-gen', 'während + Genitiv', ('pendant (+ nom)', 'during')),
        DG('innerhalb', 'innerhalb / außerhalb + Genitiv', ('à l’intérieur de / en dehors de', 'inside, within / outside')),
        D('fluss', 'der Fluss', ('le fleuve, la rivière', 'the river')),
        D('ufer', 'das Ufer', ('la rive, le bord', 'the bank, the shore')),
        D('lied', 'das Lied', ('la chanson, le chant', 'the song')),
        D('felsen', 'der Felsen', ('le rocher', 'the rock, the cliff')),
      ], [
        x('Am Ufer des Rheins steht der Felsen der Loreley.', 'Au bord du Rhin se dresse le rocher de la Lorelei.', 'On the bank of the Rhine stands the rock of the Lorelei.'),
        x('Während der Fahrt hörten die Fischer das Lied der schönen Frau.', 'Pendant le trajet, les pêcheurs entendirent le chant de la belle femme.', 'During the journey the fishermen heard the song of the beautiful woman.'),
      ], [
        FB(CHOOSE, 'Das ist das Auto ＿ Vaters.', ['meines', 'meinem', 'meiner'], 'meines', ('Der Vater au génitif : meines Vaters.', 'Der Vater in the genitive: meines Vaters.'), ('C’est la voiture de mon père.', 'That is my father’s car.')),
        FB(CHOOSE, 'Die Farbe ＿ Blume ist wunderschön.', ['der', 'des', 'dem'], 'der', ('Die Blume au génitif : der Blume.', 'Die Blume in the genitive: der Blume.'), ('La couleur de la fleur est magnifique.', 'The colour of the flower is beautiful.')),
        FB(CHOOSE, '＿ des Konzerts darf man nicht telefonieren.', ['Während', 'Innerhalb', 'Seit'], 'Während', ('Pendant le concert : während + génitif.', 'During the concert: während + genitive.'), ('Pendant le concert, on n’a pas le droit de téléphoner.', 'During the concert you are not allowed to make phone calls.')),
        FB(CHOOSE, 'Am Ufer des ＿ sitzen viele Leute.', ['Flusses', 'Fluss', 'Flüsse'], 'Flusses', ('Masculin au génitif : des Flusses.', 'Masculine in the genitive: des Flusses.'), ('Au bord du fleuve, beaucoup de gens sont assis.', 'Many people are sitting on the river bank.')),
      ]),
    L('de-landschaft', ('Le paysage et le voyage', 'Landscape and travel'), ('Décrire un paysage, une excursion et ses impressions de voyage.', 'Describe a landscape, an outing and your travel impressions.'), 8, [
        ('Le paysage : die Landschaft, das Tal (la vallée), der Hügel (la colline), der See (le lac) mais die See (la mer), die Burg (le château fort), die Aussicht (la vue).', 'The landscape: die Landschaft, das Tal (the valley), der Hügel (the hill), der See (the lake) but die See (the sea), die Burg (the fortress), die Aussicht (the view).'),
        ('Le voyage : der Ausflug (l’excursion), die Unterkunft (l’hébergement), die Sehenswürdigkeit (la curiosité touristique), das Schiff (le bateau), unterwegs (en route), besichtigen (visiter un lieu).', 'Travel: der Ausflug (the outing), die Unterkunft (accommodation), die Sehenswürdigkeit (the sight), das Schiff (the boat), unterwegs (on the way), besichtigen (to visit a place).'),
        ('Ses impressions : Die Aussicht war herrlich (magnifique). Es hat sich gelohnt (ça valait la peine). Ich war beeindruckt (impressionné), enttäuscht (déçu).', 'Your impressions: Die Aussicht war herrlich (magnificent). Es hat sich gelohnt (it was worth it). Ich war beeindruckt (impressed), enttäuscht (disappointed).'),
      ], [
        D('landschaft', 'die Landschaft', ('le paysage', 'the landscape')),
        D('tal', 'das Tal', ('la vallée', 'the valley')),
        D('burg', 'die Burg', ('le château fort', 'the fortress, the castle')),
        D('aussicht', 'die Aussicht', ('la vue (panorama)', 'the view')),
        D('ausflug', 'der Ausflug', ('l’excursion', 'the outing, the excursion')),
        D('schiff', 'das Schiff', ('le bateau, le navire', 'the ship, the boat')),
        D('besichtigen', 'besichtigen', ('visiter (un lieu)', 'to visit (a place)')),
        D('es-lohnt-sich', 'Es lohnt sich.', ('Ça vaut la peine.', 'It is worth it.')),
        D('enttaeuscht', 'enttäuscht', ('déçu', 'disappointed')),
      ], [
        x('Wir haben einen Ausflug mit dem Schiff gemacht und drei Burgen besichtigt.', 'Nous avons fait une excursion en bateau et visité trois châteaux forts.', 'We went on a boat trip and visited three castles.'),
        x('Die Aussicht vom Felsen ins Tal war herrlich. Es hat sich gelohnt!', 'La vue du rocher sur la vallée était magnifique. Ça valait la peine !', 'The view from the rock into the valley was magnificent. It was worth it!'),
      ], [
        FB(COMPLETE, 'Von der Burg hat man eine schöne ＿ auf den Rhein.', ['Aussicht', 'Unterkunft', 'Landschaft'], 'Aussicht', ('La vue : die Aussicht.', 'The view: die Aussicht.'), ('Du château, on a une belle vue sur le Rhin.', 'From the castle you have a beautiful view of the Rhine.')),
        FB(COMPLETE, 'Am Sonntag machen wir einen ＿ in die Berge.', ['Ausflug', 'Fluss', 'Felsen'], 'Ausflug', ('Une excursion : der Ausflug.', 'An outing: der Ausflug.'), ('Dimanche, nous faisons une excursion à la montagne.', 'On Sunday we are going on an outing to the mountains.')),
        TF('Das Hotel war schmutzig und laut. Wir waren enttäuscht.', ('Les voyageurs étaient ravis de l’hôtel.', 'The travellers were delighted with the hotel.'), FAUX, ('Enttäuscht = déçus.', 'Enttäuscht = disappointed.')),
        DC(ANSWER, [('Freundin', 'Wie war eure Reise an den Rhein?')], ('Une amie te demande comment était le voyage (magnifique, ça valait la peine).', 'A friend asks how the trip was (wonderful, worth it).'), ['Herrlich! Es hat sich wirklich gelohnt.', 'Herrlich! Es hat mich gelohnt.', 'Enttäuscht! Es lohnt gern.'], 'Herrlich! Es hat sich wirklich gelohnt.', ('Sich lohnen : es hat sich gelohnt.', 'Sich lohnen: es hat sich gelohnt.')),
      ]),
  ]),
  CH('goetheb1-w7-c2', ('Plus le chant est beau…', 'The lovelier the song…'), [
    L('de-je-desto', ('Plus…, plus… : je … desto', 'The more…, the more…: je … desto'), ('Mettre deux évolutions en relation et nuancer une comparaison.', 'Relate two developments and qualify a comparison.'), 8, [
        ('Je + comparatif (verbe à la fin), desto / umso + comparatif (puis verbe et sujet). Je länger er zuhörte, desto weniger sah er die Felsen.', 'Je + comparative (verb at the end), desto / umso + comparative (then verb and subject). Je länger er zuhörte, desto weniger sah er die Felsen.'),
        ('Nuancer une comparaison : viel größer (beaucoup plus grand), etwas kleiner (un peu plus petit), genauso schön wie (tout aussi beau que), nicht so teuer wie (pas aussi cher que).', 'Qualifying a comparison: viel größer (much bigger), etwas kleiner (a little smaller), genauso schön wie (just as beautiful as), nicht so teuer wie (not as expensive as).'),
        ('Immer + comparatif = de plus en plus : Es wird immer dunkler. Das Leben wird immer teurer.', 'Immer + comparative = more and more: Es wird immer dunkler. Das Leben wird immer teurer.'),
      ], [
        DG('je-desto', 'je … desto …', ('plus…, plus…', 'the more…, the more…')),
        DG('immer-komp', 'immer + Komparativ', ('de plus en plus', 'more and more')),
        DG('genauso-wie', 'genauso … wie', ('tout aussi… que', 'just as… as')),
        DG('nicht-so-wie', 'nicht so … wie', ('pas aussi… que', 'not as… as')),
        D('zuhoeren', 'zuhören', ('écouter (attentivement)', 'to listen (to)')),
        D('gefaehrlich', 'gefährlich', ('dangereux', 'dangerous')),
        D('vorsichtig', 'vorsichtig', ('prudent', 'careful')),
        D('strom', 'der Strom', ('le courant ; le grand fleuve', 'the current; the great river')),
      ], [
        x('Je schöner sie sang, desto gefährlicher wurde die Fahrt.', 'Plus elle chantait bien, plus le trajet devenait dangereux.', 'The more beautifully she sang, the more dangerous the journey became.'),
        x('Der Strom wird immer schneller. Sei vorsichtig!', 'Le courant devient de plus en plus rapide. Sois prudent !', 'The current is getting faster and faster. Be careful!'),
      ], [
        FB(CHOOSE, 'Je mehr ich lerne, ＿ besser verstehe ich.', ['desto', 'als', 'wie'], 'desto', ('Je… desto…', 'Je… desto…'), ('Plus j’apprends, mieux je comprends.', 'The more I learn, the better I understand.')),
        FB(CHOOSE, 'Die Mieten werden ＿ teurer.', ['immer', 'mehr', 'sehr'], 'immer', ('De plus en plus : immer + comparatif.', 'More and more: immer + comparative.'), ('Les loyers deviennent de plus en plus chers.', 'Rents are getting more and more expensive.')),
        FB(CHOOSE, 'Der Zug ist nicht so schnell ＿ das Flugzeug.', ['wie', 'als', 'desto'], 'wie', ('Nicht so… wie.', 'Nicht so… wie.'), ('Le train n’est pas aussi rapide que l’avion.', 'The train is not as fast as the plane.')),
        order(('Remets dans l’ordre : « Plus il fait froid, plus je dors. »', 'Put in order: “The colder it is, the more I sleep.”'), ['Je', 'kälter', 'es', 'ist,', 'desto', 'mehr', 'schlafe', 'ich.'], ('Je + comparatif + verbe à la fin ; desto + comparatif + verbe + sujet.', 'Je + comparative + verb at the end; desto + comparative + verb + subject.')),
      ]),
  ])])

# ═════════════════════════ 8 : Les questions indirectes, les verbes à préposition, les relations ═════════════════════════
W8 = WORLD('goetheb1-w8', ('Les récits du Baron de Münchhausen', 'Baron Münchhausen’s tales'), REGION,
  ('Poser une question indirecte, employer les verbes à préposition avec wo(r)- et da(r)-, parler des relations et de la vérité.', 'Ask an indirect question, use verbs with prepositions with wo(r)- and da(r)-, talk about relationships and the truth.'),
  (('Le Baron de Münchhausen', 'Baron Münchhausen'), '♖', ('À cheval sur un boulet de canon ou tiré d’un marais par ses propres cheveux, le Baron de Münchhausen raconte sans rougir. Interroge-le poliment — savez-vous si… ? à quoi pensez-vous ? — et démêle le vrai du faux.', 'Riding a cannonball or pulling himself out of a swamp by his own hair, Baron Münchhausen tells his tales without blushing. Question him politely — do you know whether…? what are you thinking of? — and sort truth from lies.')),
  [CH('goetheb1-w8-c1', ('Savez-vous si… ?', 'Do you know whether…?'), [
    L('de-indirekt', ('Les questions indirectes', 'Indirect questions'), ('Poser une question avec tact et rapporter une question.', 'Ask a question tactfully and report a question.'), 8, [
        ('Question indirecte : le mot interrogatif reste, le verbe va à la fin. Wo ist der Bahnhof? → Können Sie mir sagen, wo der Bahnhof ist?', 'Indirect question: the question word stays, the verb goes to the end. Wo ist der Bahnhof? → Können Sie mir sagen, wo der Bahnhof ist?'),
        ('Question fermée (oui / non) : ob (si). Kommt er morgen? → Ich weiß nicht, ob er morgen kommt. Ne pas confondre ob (question) et wenn (condition).', 'Yes / no question: ob (whether). Kommt er morgen? → Ich weiß nicht, ob er morgen kommt. Do not confuse ob (question) and wenn (condition).'),
        ('Amorces polies : Wissen Sie, ob…? Können Sie mir sagen, wann…? Ich möchte gern wissen, wie viel… Darf ich fragen, warum…?', 'Polite openers: Wissen Sie, ob…? Können Sie mir sagen, wann…? Ich möchte gern wissen, wie viel… Darf ich fragen, warum…?'),
      ], [
        DG('indirekte-frage', 'Ich weiß nicht, wo / wann / wie …', ('question indirecte (verbe à la fin)', 'indirect question (verb at the end)')),
        DG('ob', 'ob', ('si (question indirecte)', 'whether, if (indirect question)')),
        D('koennen-sie-mir-sagen', 'Können Sie mir sagen, …?', ('Pouvez-vous me dire… ?', 'Can you tell me…?')),
        D('fragen', 'fragen', ('demander, interroger', 'to ask')),
        D('wissen', 'wissen', ('savoir', 'to know (a fact)')),
        D('keine-ahnung', 'Keine Ahnung!', ('Aucune idée !', 'No idea!')),
        D('erzaehlen', 'erzählen', ('raconter', 'to tell (a story)')),
        D('geschichte', 'die Geschichte', ('l’histoire', 'the story; history')),
      ], [
        x('Wissen Sie, ob der Baron wirklich auf einer Kanonenkugel geritten ist?', 'Savez-vous si le baron a vraiment chevauché un boulet de canon ?', 'Do you know whether the baron really rode on a cannonball?'),
        x('Niemand weiß, woher er seine Geschichten hat.', 'Personne ne sait d’où il tient ses histoires.', 'Nobody knows where he gets his stories from.'),
      ], [
        FB(CHOOSE, 'Ich weiß nicht, ＿ er heute kommt.', ['ob', 'wenn', 'dass'], 'ob', ('Question fermée rapportée : ob.', 'A reported yes / no question: ob.'), ('Je ne sais pas s’il vient aujourd’hui.', 'I do not know whether he is coming today.')),
        order(('Remets dans l’ordre : « Pouvez-vous me dire où est la gare ? »', 'Put in order: “Can you tell me where the station is?”'), ['Können', 'Sie', 'mir', 'sagen,', 'wo', 'der', 'Bahnhof', 'ist?'], ('Dans la question indirecte, le verbe ist est à la fin.', 'In the indirect question, the verb ist is at the end.')),
        FB(CHOOSE, 'Darf ich fragen, wann der Film ＿?', ['anfängt', 'fängt an', 'anfangen'], 'anfängt', ('Verbe à la fin, particule rattachée : anfängt.', 'Verb at the end, prefix attached: anfängt.'), ('Puis-je demander quand le film commence ?', 'May I ask when the film starts?')),
        DC(ANSWER, [('Tourist', 'Wissen Sie, wie spät es ist?')], ('Un touriste te demande l’heure (tu n’en as aucune idée).', 'A tourist asks you the time (you have no idea).'), ['Keine Ahnung, tut mir leid.', 'Ja, ob es spät ist.', 'Ich weiß, wann ist es.'], 'Keine Ahnung, tut mir leid.', ('Ne pas savoir : Keine Ahnung.', 'Not knowing: Keine Ahnung.')),
      ]),
    L('de-verben-praep', ('Les verbes à préposition', 'Verbs with prepositions'), ('Employer la bonne préposition après le verbe, et la reprendre avec wo(r)- et da(r)-.', 'Use the right preposition after the verb, and refer back to it with wo(r)- and da(r)-.'), 9, [
        ('Beaucoup de verbes ont une préposition fixe : warten auf (+ accusatif), denken an (+ acc.), sich freuen auf (se réjouir d’avance) / über (être content de), träumen von (+ datif), sprechen über (+ acc.), Angst haben vor (+ dat.).', 'Many verbs have a fixed preposition: warten auf (+ accusative), denken an (+ acc.), sich freuen auf (to look forward to) / über (to be pleased about), träumen von (+ dative), sprechen über (+ acc.), Angst haben vor (+ dat.).'),
        ('Question sur une chose : wo(r) + préposition. Worauf wartest du? Wovon träumst du? Woran denkst du? Sur une personne : préposition + wen / wem. Auf wen wartest du?', 'A question about a thing: wo(r) + preposition. Worauf wartest du? Wovon träumst du? Woran denkst du? About a person: preposition + wen / wem. Auf wen wartest du?'),
        ('Reprise d’une chose : da(r) + préposition. Ich warte darauf. Ich freue mich darüber. Ich denke oft daran. Pour une personne : Ich warte auf ihn.', 'Referring back to a thing: da(r) + preposition. Ich warte darauf. Ich freue mich darüber. Ich denke oft daran. For a person: Ich warte auf ihn.'),
      ], [
        D('warten-auf', 'warten auf + Akk.', ('attendre (quelque chose, quelqu’un)', 'to wait for')),
        D('denken-an', 'denken an + Akk.', ('penser à', 'to think of')),
        D('sich-freuen-auf', 'sich freuen auf + Akk.', ('se réjouir d’avance de', 'to look forward to')),
        D('traeumen-von', 'träumen von + Dat.', ('rêver de', 'to dream of')),
        D('angst-haben-vor', 'Angst haben vor + Dat.', ('avoir peur de', 'to be afraid of')),
        D('sprechen-ueber', 'sprechen über + Akk.', ('parler de', 'to talk about')),
        DG('wo-r', 'worauf / wovon / woran', ('sur quoi / de quoi / à quoi', 'what… for / of / about (wo- compounds)')),
        DG('da-r', 'darauf / davon / daran', ('y, en (sur cela, de cela, à cela)', 'for it / of it / about it (da- compounds)')),
      ], [
        x('Wovon träumt der Baron? — Er träumt von einer Reise zum Mond.', 'De quoi rêve le baron ? — Il rêve d’un voyage sur la Lune.', 'What does the baron dream of? — He dreams of a journey to the moon.'),
        x('Die Gäste warten auf die nächste Geschichte. Sie freuen sich schon darauf.', 'Les invités attendent la prochaine histoire. Ils s’en réjouissent déjà.', 'The guests are waiting for the next story. They are already looking forward to it.'),
      ], [
        FB(CHOOSE, 'Ich warte ＿ den Bus.', ['auf', 'für', 'an'], 'auf', ('Warten auf + accusatif.', 'Warten auf + accusative.'), ('J’attends le bus.', 'I am waiting for the bus.')),
        FB(CHOOSE, '＿ denkst du gerade? — An meinen Urlaub.', ['Woran', 'Wovon', 'Worauf'], 'Woran', ('Denken an → woran.', 'Denken an → woran.'), ('À quoi penses-tu en ce moment ? — À mes vacances.', 'What are you thinking of right now? — My holiday.')),
        FB(CHOOSE, 'Morgen fahren wir ans Meer. Ich freue mich schon ＿.', ['darauf', 'darüber', 'davon'], 'darauf', ('Se réjouir d’avance : sich freuen auf → darauf.', 'To look forward to: sich freuen auf → darauf.'), ('Demain, nous allons à la mer. Je m’en réjouis déjà.', 'Tomorrow we are going to the seaside. I am already looking forward to it.')),
        FB(CHOOSE, 'Hast du Angst ＿ Hunden?', ['vor', 'von', 'für'], 'vor', ('Angst haben vor + datif.', 'Angst haben vor + dative.'), ('As-tu peur des chiens ?', 'Are you afraid of dogs?')),
      ]),
  ]),
  CH('goetheb1-w8-c2', ('Le vrai du faux', 'Truth and lies'), [
    L('de-beziehungen', ('Les relations et la vérité', 'Relationships and the truth'), ('Parler de l’amitié, des disputes et de la confiance.', 'Talk about friendship, quarrels and trust.'), 9, [
        ('Les relations : sich kennenlernen (faire connaissance), sich verlieben in (tomber amoureux de), sich gut verstehen (bien s’entendre), sich streiten (se disputer), sich trennen (se séparer), sich versöhnen (se réconcilier).', 'Relationships: sich kennenlernen (to get to know each other), sich verlieben in (to fall in love with), sich gut verstehen (to get on well), sich streiten (to quarrel), sich trennen (to separate), sich versöhnen (to make up).'),
        ('La confiance : jemandem vertrauen (faire confiance à, + datif), sich auf jemanden verlassen (compter sur), die Wahrheit sagen (dire la vérité), lügen (mentir), übertreiben (exagérer).', 'Trust: jemandem vertrauen (to trust, + dative), sich auf jemanden verlassen (to rely on), die Wahrheit sagen (to tell the truth), lügen (to lie), übertreiben (to exaggerate).'),
        ('Réagir à un récit : Wirklich? (vraiment ?), Das glaube ich nicht (je n’y crois pas), Das kann nicht sein (ce n’est pas possible), Du übertreibst! (tu exagères !).', 'Reacting to a story: Wirklich? (really?), Das glaube ich nicht (I do not believe it), Das kann nicht sein (that cannot be), Du übertreibst! (you are exaggerating!).'),
      ], [
        D('kennenlernen', 'kennenlernen', ('faire la connaissance de', 'to get to know, to meet')),
        D('sich-verlieben', 'sich verlieben in', ('tomber amoureux de', 'to fall in love with')),
        D('sich-streiten', 'sich streiten', ('se disputer', 'to quarrel, to argue')),
        D('sich-verstehen', 'sich gut verstehen', ('bien s’entendre', 'to get on well')),
        D('vertrauen', 'vertrauen', ('faire confiance à', 'to trust')),
        D('wahrheit', 'die Wahrheit', ('la vérité', 'the truth')),
        D('luegen', 'lügen', ('mentir', 'to lie (not tell the truth)')),
        D('uebertreiben', 'übertreiben', ('exagérer', 'to exaggerate')),
        D('wirklich', 'wirklich', ('vraiment', 'really')),
      ], [
        x('Der Baron lügt nicht, sagt er: Er übertreibt nur ein bisschen.', 'Le baron ne ment pas, dit-il : il exagère seulement un peu.', 'The baron does not lie, he says: he only exaggerates a little.'),
        x('Wir verstehen uns gut, obwohl wir uns manchmal streiten.', 'Nous nous entendons bien, même si nous nous disputons parfois.', 'We get on well, although we sometimes quarrel.'),
      ], [
        FB(COMPLETE, 'Sie sagt immer die ＿: Man kann ihr vertrauen.', ['Wahrheit', 'Geschichte', 'Ahnung'], 'Wahrheit', ('Dire la vérité : die Wahrheit sagen.', 'To tell the truth: die Wahrheit sagen.'), ('Elle dit toujours la vérité : on peut lui faire confiance.', 'She always tells the truth: you can trust her.')),
        FB(CHOOSE, 'Er hat sich ＿ seine Kollegin verliebt.', ['in', 'an', 'mit'], 'in', ('Sich verlieben in + accusatif.', 'Sich verlieben in + accusative.'), ('Il est tombé amoureux de sa collègue.', 'He has fallen in love with his colleague.')),
        TF('Meine Schwester und ich streiten uns nie. Wir verstehen uns sehr gut.', ('Les deux sœurs se disputent souvent.', 'The two sisters often quarrel.'), FAUX, ('Nie = jamais ; sich gut verstehen = bien s’entendre.', 'Nie = never; sich gut verstehen = to get on well.')),
        DC(ANSWER, [('Baron', 'Ich bin auf einer Kanonenkugel über die Stadt geflogen!')], ('Le baron raconte un exploit impossible (tu n’y crois pas).', 'The baron tells of an impossible feat (you do not believe it).'), ['Das glaube ich nicht. Sie übertreiben!', 'Das glaube ich nicht. Sie vertrauen!', 'Wirklich? Ich streite mich darauf.'], 'Das glaube ich nicht. Sie übertreiben!', ('Doute poli : Das glaube ich nicht ; exagérer = übertreiben.', 'Polite doubt: Das glaube ich nicht; to exaggerate = übertreiben.')),
      ]),
  ])])

write_level('GOETHEB1', ('Goethe B1 : le pays des légendes', 'Goethe B1: the land of legends'), REGION, 'Land of legends', 48,
  [W1, W2, W3, W4, W5, W6, W7, W8, FINAL('GOETHEB1', REGION, ('Simulation Goethe B1 : la nuit de Walpurgis', 'Goethe B1 simulation: Walpurgis Night'), 'Lesen, Hören et Schreiben (l’oral, Sprechen, n’est pas évalué)', 'Lesen, Hören and Schreiben (the speaking test, Sprechen, is not assessed)', modules=True)])
