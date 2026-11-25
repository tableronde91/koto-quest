# Niveau DELE B1 (espagnol, CECRL B1) : 8 étapes sur le chemin de Saint-Jacques, leçons et examen blanc (français + anglais).
# Mode histoire : le pèlerin ou la pèlerine du Camino francés, de Roncevaux à Fisterra (voir gen-story.py).
# Les notions sont en espagnol (front) avec leur sens en français ; la traduction anglaise du sens sert à l'interface en anglais.
# Usage : python3 scripts/deleb1-level.py   (réécrit content/deleb1/deleb1.json ; les DELE A1 et A2 doivent déjà exister)
from es_common import *

REGION = 'Chemin de Saint-Jacques'

# ═════════════════════════ 1 : Roncevaux — le futur, le conditionnel, les suppositions ═════════════════════════
W1 = WORLD('deleb1-w1', ('Le départ de Roncevaux', 'Setting off from Roncesvalles'), REGION,
  ('Parler de ses projets au futur, demander poliment et conseiller au conditionnel, et faire des suppositions (estará, a lo mejor, quizás).', 'Talk about plans in the future, ask politely and give advice in the conditional, and make guesses (estará, a lo mejor, quizás).'),
  (('L’Herensuge d’Aralar', 'The Herensuge of Aralar'), 'Ç', ('Dans la sierra d’Aralar, l’Herensuge, dragon à sept têtes des légendes navarraises, garde le col des Pyrénées. Il ne laisse passer que les pèlerins qui savent dire ce qu’ils feront demain et ce qu’ils feraient à sa place.', 'In the Aralar range, the Herensuge, the seven-headed dragon of Navarrese legend, guards the Pyrenean pass. It only lets through pilgrims who can say what they will do tomorrow and what they would do in its place.')),
  [CH('deleb1-w1-c1', ('Au pied des Pyrénées', 'At the foot of the Pyrenees'), [
    L('es-futuro', ('Demain, nous marcherons : le futur', 'Tomorrow we will walk: the future'), ('Former le futur simple et parler de ses projets et de ses promesses.', 'Form the simple future and talk about plans and promises.'), 9, [
        ('Futur simple = infinitif + -é, -ás, -á, -emos, -éis, -án : hablaré, comerás, vivirá. Les terminaisons sont les mêmes pour tous les verbes.', 'Simple future = infinitive + -é, -ás, -á, -emos, -éis, -án: hablaré, comerás, vivirá. The endings are the same for all verbs.'),
        ('Radicaux irréguliers : tener → tendré, poner → pondré, salir → saldré, venir → vendré, poder → podré, saber → sabré, hacer → haré, decir → diré, querer → querré.', 'Irregular stems: tener → tendré, poner → pondré, salir → saldré, venir → vendré, poder → podré, saber → sabré, hacer → haré, decir → diré, querer → querré.'),
        ('Pour les prévisions et les promesses : Mañana lloverá. Te escribiré todos los días. Marqueurs : pasado mañana, dentro de dos días, el año que viene, algún día.', 'For forecasts and promises: Mañana lloverá. Te escribiré todos los días. Time markers: pasado mañana, dentro de dos días, el año que viene, algún día.'),
      ], [
        SG('futuro', 'hablaré / comerás / vivirá', ('je parlerai / tu mangeras / il vivra (futur)', 'I will speak / you will eat / he will live (future)')),
        SG('futuro-irregular', 'tendré / saldré / haré / diré', ('j’aurai / je sortirai / je ferai / je dirai', 'I will have / leave / do / say')),
        S('pasado-manana', 'pasado mañana', ('après-demain', 'the day after tomorrow')),
        S('dentro-de-dos-dias', 'dentro de dos días', ('dans deux jours', 'in two days')),
        S('algun-dia', 'algún día', ('un jour (dans le futur)', 'one day, someday')),
        S('el-peregrino', 'el peregrino / la peregrina', ('le pèlerin / la pèlerine', 'the pilgrim')),
        S('la-mochila', 'la mochila', ('le sac à dos', 'the backpack, the rucksack')),
        S('la-etapa', 'la etapa', ('l’étape', 'the stage (of a journey)')),
      ], [
        x('Mañana saldremos a las seis y haremos una etapa de veinticinco kilómetros.', 'Demain, nous partirons à six heures et nous ferons une étape de vingt-cinq kilomètres.', 'Tomorrow we will leave at six and do a twenty-five-kilometre stage.'),
        x('Algún día volveré a Roncesvalles con mis hijos.', 'Un jour, je reviendrai à Roncevaux avec mes enfants.', 'One day I will come back to Roncesvalles with my children.'),
      ], [
        FB(CHOOSE, 'Mañana ＿ a las seis de la mañana.', ['saldremos', 'saliremos', 'salderemos'], 'saldremos', ('Salir → saldr- au futur.', 'Salir → saldr- in the future.'), ('Demain, nous partirons à six heures du matin.', 'Tomorrow we will leave at six in the morning.')),
        FB(CHOOSE, 'El año que viene ＿ más tiempo libre.', ['tendré', 'teneré', 'tenré'], 'tendré', ('Tener → tendr- au futur.', 'Tener → tendr- in the future.'), ('L’année prochaine, j’aurai plus de temps libre.', 'Next year I will have more free time.')),
        FB(CHOOSE, 'Te prometo que te ＿ la verdad.', ['diré', 'deciré', 'diceré'], 'diré', ('Decir → dir- au futur.', 'Decir → dir- in the future.'), ('Je te promets que je te dirai la vérité.', 'I promise I will tell you the truth.')),
        TF('Pasado mañana llegaremos a Pamplona.', ('Ils arriveront à Pampelune dans deux jours.', 'They will arrive in Pamplona in two days.'), VRAI, ('Pasado mañana = après-demain.', 'Pasado mañana = the day after tomorrow.')),
      ]),
    L('es-condicional', ('Pourriez-vous… ? Le conditionnel', 'Could you…? The conditional'), ('Demander poliment, exprimer un souhait et conseiller avec le conditionnel.', 'Ask politely, express a wish and give advice with the conditional.'), 9, [
        ('Conditionnel = infinitif + -ía, -ías, -ía, -íamos, -íais, -ían : hablaría, comería. Les radicaux irréguliers sont ceux du futur : tendría, saldría, haría, diría, podría.', 'Conditional = infinitive + -ía, -ías, -ía, -íamos, -íais, -ían: hablaría, comería. The irregular stems are those of the future: tendría, saldría, haría, diría, podría.'),
        ('Pour être poli : ¿Podría ayudarme? ¿Le importaría cerrar la ventana? Me gustaría reservar una cama.', 'To be polite: ¿Podría ayudarme? ¿Le importaría cerrar la ventana? Me gustaría reservar una cama.'),
        ('Pour conseiller : Yo que tú, descansaría (à ta place, je me reposerais). Deberías llevar menos peso.', 'To give advice: Yo que tú, descansaría (if I were you, I’d rest). Deberías llevar menos peso (you should carry less weight).'),
      ], [
        SG('condicional', 'hablaría / comería / viviría', ('je parlerais / je mangerais / je vivrais (conditionnel)', 'I would speak / eat / live (conditional)')),
        S('me-gustaria', 'me gustaría…', ('j’aimerais…', 'I would like…')),
        S('podria', '¿Podría…?', ('Pourriez-vous… ?', 'Could you…?')),
        S('deberias', 'deberías + infinitivo', ('tu devrais + infinitif', 'you should + verb')),
        S('yo-que-tu', 'yo que tú…', ('à ta place…', 'if I were you…')),
        S('le-importaria', '¿Le importaría…?', ('Cela vous dérangerait-il de… ?', 'Would you mind…?')),
        S('el-albergue', 'el albergue', ('le gîte (de pèlerins)', 'the hostel (for pilgrims)')),
        S('el-peso', 'el peso', ('le poids', 'the weight')),
      ], [
        x('¿Podría decirme dónde está el albergue de peregrinos?', 'Pourriez-vous me dire où se trouve le gîte des pèlerins ?', 'Could you tell me where the pilgrims’ hostel is?'),
        x('Tu mochila pesa demasiado: yo que tú, dejaría algunas cosas aquí.', 'Ton sac pèse trop lourd : à ta place, je laisserais quelques affaires ici.', 'Your rucksack is too heavy: if I were you, I’d leave a few things here.'),
      ], [
        FB(CHOOSE, '¿＿ abrir la ventana, por favor?', ['Podría', 'Podré', 'Puedría'], 'Podría', ('Demande polie : conditionnel (podría).', 'Polite request: conditional (podría).'), ('Pourriez-vous ouvrir la fenêtre, s’il vous plaît ?', 'Could you open the window, please?')),
        FB(CHOOSE, 'Me ＿ reservar una cama para esta noche.', ['gustaría', 'gustará', 'gusto'], 'gustaría', ('Souhait poli : me gustaría.', 'Polite wish: me gustaría.'), ('J’aimerais réserver un lit pour ce soir.', 'I’d like to book a bed for tonight.')),
        FB(CHOOSE, 'Estás muy cansado: ＿ descansar un día.', ['deberías', 'deberás', 'debías'], 'deberías', ('Conseil : deber au conditionnel.', 'Advice: deber in the conditional.'), ('Tu es très fatigué : tu devrais te reposer un jour.', 'You’re very tired: you should rest for a day.')),
        DC(ANSWER, [('Peregrina', 'Me duelen mucho los pies. ¿Qué hago?')], ('Une pèlerine a très mal aux pieds et te demande conseil.', 'A pilgrim’s feet hurt a lot and she asks for your advice.'), ['Yo que tú, descansaría hoy.', 'Yo que tú, descansé ayer.', 'Tú que yo, descansarás.'], 'Yo que tú, descansaría hoy.', ('Conseil : yo que tú + conditionnel.', 'Advice: yo que tú + conditional.')),
      ]),
  ]),
  CH('deleb1-w1-c2', ('Le col dans la brume', 'The pass in the mist'), [
    L('es-probabilidad', ('Il doit être au gîte : les suppositions', 'He must be at the hostel: making guesses'), ('Faire des suppositions avec le futur, a lo mejor, quizás et seguramente.', 'Make guesses with the future, a lo mejor, quizás and seguramente.'), 9, [
        ('Le futur sert aussi à supposer quelque chose sur le présent : ¿Dónde está Ana? — Estará en el albergue (elle doit être au gîte). ¿Qué hora es? — Serán las diez.', 'The future is also used to guess about the present: ¿Dónde está Ana? — Estará en el albergue (she must be at the hostel). ¿Qué hora es? — Serán las diez (it must be about ten).'),
        ('A lo mejor (peut-être, familier) est toujours suivi de l’indicatif : A lo mejor llueve esta tarde. Quizás et tal vez acceptent l’indicatif ou le subjonctif.', 'A lo mejor (maybe, informal) is always followed by the indicative: A lo mejor llueve esta tarde. Quizás and tal vez take the indicative or the subjunctive.'),
        ('Pour nuancer : seguramente, probablemente (probablement), es posible, no estoy seguro (je ne suis pas sûr).', 'To hedge: seguramente, probablemente (probably), es posible, no estoy seguro (I’m not sure).'),
      ], [
        SG('futuro-probabilidad', 'estará / serán las diez', ('il doit être… / il doit être dix heures (supposition)', 'he must be… / it must be about ten (guess)')),
        S('a-lo-mejor', 'a lo mejor', ('peut-être (familier)', 'maybe')),
        S('quizas', 'quizás / tal vez', ('peut-être', 'perhaps')),
        S('seguramente', 'seguramente', ('sûrement, probablement', 'surely, probably')),
        S('no-estoy-seguro', 'no estoy seguro / segura', ('je ne suis pas sûr·e', 'I’m not sure')),
        S('la-niebla', 'la niebla', ('le brouillard', 'the fog')),
        S('la-subida', 'la subida / la bajada', ('la montée / la descente', 'the climb / the descent')),
        S('el-cruce', 'el cruce', ('le carrefour, le croisement', 'the crossroads, the junction')),
      ], [
        x('No veo a Marco. — Estará todavía en la subida: camina muy despacio.', 'Je ne vois pas Marco. — Il doit encore être dans la montée : il marche très lentement.', 'I can’t see Marco. — He must still be on the climb: he walks very slowly.'),
        x('A lo mejor hay niebla mañana en el puerto de Ibañeta.', 'Il y aura peut-être du brouillard demain au col d’Ibañeta.', 'Maybe there will be fog tomorrow at the Ibañeta pass.'),
      ], [
        DC(ANSWER, [('Peregrino', '¿Qué hora es? No tengo reloj.')], ('Un pèlerin demande l’heure ; tu n’es pas sûr·e.', 'A pilgrim asks the time; you’re not sure.'), ['No sé, serán las cinco.', 'No sé, fueron las cinco.', 'No sé, sean las cinco.'], 'No sé, serán las cinco.', ('Supposition sur le présent : futur (serán).', 'Guess about the present: future (serán).')),
        FB(CHOOSE, 'A lo mejor ＿ esta tarde.', ['llueve', 'llueva', 'llover'], 'llueve', ('A lo mejor + indicatif.', 'A lo mejor + indicative.'), ('Il pleuvra peut-être cet après-midi.', 'Maybe it will rain this afternoon.')),
        FB(CHOOSE, 'Juan no contesta: ＿ durmiendo.', ['estará', 'estuvo', 'esté'], 'estará', ('Supposition : futur.', 'Guess: future.'), ('Juan ne répond pas : il doit être en train de dormir.', 'Juan isn’t answering: he must be asleep.')),
        TF('Serán las diez.', ('La personne est sûre de l’heure.', 'The person is sure of the time.'), FAUX, ('Futur de probabilité : c’est une supposition.', 'Future of probability: it’s a guess.')),
      ]),
  ])])

# ═════════════════════════ 2 : la Rioja — le subjonctif présent, l'opinion ═════════════════════════
W2 = WORLD('deleb1-w2', ('Les vignes de la Rioja', 'The vineyards of La Rioja'), REGION,
  ('Former le subjonctif présent, donner son avis (creo que, no creo que), exprimer son accord ou son désaccord et porter un jugement (es importante que…).', 'Form the present subjunctive, give your opinion (creo que, no creo que), agree or disagree and make judgements (es importante que…).'),
  (('Le Gizotso des vignes', 'The Gizotso of the vineyards'), 'ç', ('Le Gizotso, loup-garou des légendes basques et navarraises, rôde entre les vignes à la tombée de la nuit. Il adore les disputes : donne ton avis avec nuance, accepte celui des autres, et il retournera dans la forêt.', 'The Gizotso, the werewolf of Basque and Navarrese legend, prowls among the vines at nightfall. It loves arguments: give your opinion with nuance, accept other people’s, and it will go back into the forest.')),
  [CH('deleb1-w2-c1', ('À la cave', 'At the winery'), [
    L('es-subjuntivo', ('Que tu viennes : le subjonctif présent', 'That you come: the present subjunctive'), ('Former le subjonctif présent des verbes réguliers et irréguliers.', 'Form the present subjunctive of regular and irregular verbs.'), 10, [
        ('On part de la 1re personne du présent et on « inverse » la voyelle : -ar → -e (hable, hables, hable, hablemos, habléis, hablen), -er / -ir → -a (coma, viva). Tengo → tenga, hago → haga, digo → diga, salgo → salga.', 'Start from the 1st person of the present and “swap” the vowel: -ar → -e (hable, hables, hable, hablemos, habléis, hablen), -er / -ir → -a (coma, viva). Tengo → tenga, hago → haga, digo → diga, salgo → salga.'),
        ('Six verbes vraiment irréguliers : ser → sea, ir → vaya, estar → esté, dar → dé, saber → sepa, haber → haya.', 'Six truly irregular verbs: ser → sea, ir → vaya, estar → esté, dar → dé, saber → sepa, haber → haya.'),
        ('Le subjonctif s’emploie après les expressions de souhait, de doute, de sentiment ou de jugement (leçons suivantes). Formule d’adieu : ¡Que te vaya bien! (bonne continuation).', 'The subjunctive is used after expressions of wish, doubt, feeling or judgement (next lessons). A goodbye formula: ¡Que te vaya bien! (all the best).'),
      ], [
        SG('subjuntivo', 'hable / coma / viva', ('que je parle / mange / vive (subjonctif)', 'that I speak / eat / live (subjunctive)')),
        SG('subjuntivo-irregular', 'tenga / haga / diga / salga', ('que j’aie / fasse / dise / sorte', 'that I have / do / say / leave')),
        SG('sea-vaya', 'sea / vaya / esté / sepa', ('que je sois / aille / sois (estar) / sache', 'that I be / go / be (estar) / know')),
        S('que-te-vaya-bien', '¡Que te vaya bien!', ('Bonne continuation !', 'All the best!')),
        S('la-vina', 'la viña', ('la vigne', 'the vineyard, the vine')),
        S('la-bodega', 'la bodega', ('la cave (à vin), le chai', 'the wine cellar, the winery')),
        S('la-uva', 'la uva', ('le raisin', 'the grape')),
        S('la-cosecha', 'la cosecha', ('la récolte, les vendanges', 'the harvest')),
      ], [
        x('El bodeguero quiere que probemos el vino de este año.', 'Le vigneron veut que nous goûtions le vin de cette année.', 'The winemaker wants us to taste this year’s wine.'),
        x('¡Buen Camino! ¡Que te vaya bien!', 'Bon chemin ! Bonne continuation !', 'Buen Camino! All the best!'),
      ], [
        FB(CHOOSE, 'Quiero que ＿ conmigo a la bodega.', ['vengas', 'vienes', 'vendrás'], 'vengas', ('Querer que + subjonctif : vengo → vengas.', 'Querer que + subjunctive: vengo → vengas.'), ('Je veux que tu viennes avec moi à la cave.', 'I want you to come with me to the winery.')),
        FB(CHOOSE, 'Espero que mañana ＿ buen tiempo.', ['haga', 'hace', 'hará'], 'haga', ('Esperar que + subjonctif : hago → haga.', 'Esperar que + subjunctive: hago → haga.'), ('J’espère qu’il fera beau demain.', 'I hope the weather will be nice tomorrow.')),
        FB(CHOOSE, 'Es necesario que ＿ paciencia.', ['tengas', 'tienes', 'tendrás'], 'tengas', ('Es necesario que + subjonctif.', 'Es necesario que + subjunctive.'), ('Il faut que tu sois patient.', 'You need to be patient.')),
        FB(CHOOSE, 'Ojalá ＿ en Logroño antes de la noche.', ['estemos', 'estamos', 'estaremos'], 'estemos', ('Ojalá + subjonctif : estar → estemos.', 'Ojalá + subjunctive: estar → estemos.'), ('Pourvu que nous soyons à Logroño avant la nuit.', 'Hopefully we’ll be in Logroño before nightfall.')),
      ]),
    L('es-opinion', ('À mon avis… : donner son opinion', 'In my opinion…: giving your view'), ('Donner son avis, dire qu’on est d’accord ou non.', 'Give your opinion and say whether you agree.'), 9, [
        ('Creo que / pienso que / me parece que + indicatif : Creo que es buena idea. À la forme négative, le subjonctif : No creo que sea buena idea.', 'Creo que / pienso que / me parece que + indicative: Creo que es buena idea. In the negative, the subjunctive: No creo que sea buena idea.'),
        ('Pour introduire son avis : en mi opinión, para mí, desde mi punto de vista (de mon point de vue).', 'To introduce your view: en mi opinión, para mí, desde mi punto de vista (from my point of view).'),
        ('Accord et désaccord : Estoy de acuerdo (contigo), tienes razón (tu as raison), no estoy de acuerdo, depende (ça dépend), yo no lo veo así (je ne vois pas les choses comme ça).', 'Agreeing and disagreeing: Estoy de acuerdo (contigo), tienes razón (you’re right), no estoy de acuerdo, depende (it depends), yo no lo veo así (I don’t see it that way).'),
      ], [
        SG('creo-que', 'creo que + indicativo', ('je crois que + indicatif', 'I think that + indicative')),
        SG('no-creo-que', 'no creo que + subjuntivo', ('je ne crois pas que + subjonctif', 'I don’t think that + subjunctive')),
        S('en-mi-opinion', 'en mi opinión', ('à mon avis', 'in my opinion')),
        S('punto-de-vista', 'desde mi punto de vista', ('de mon point de vue', 'from my point of view')),
        S('estar-de-acuerdo', 'estar de acuerdo', ('être d’accord', 'to agree (with someone)')),
        S('tener-razon', 'tener razón', ('avoir raison', 'to be right')),
        S('depende', 'depende', ('ça dépend', 'it depends')),
        S('la-ventaja', 'la ventaja / el inconveniente', ('l’avantage / l’inconvénient', 'the advantage / the drawback')),
      ], [
        x('Creo que el Camino es más bonito en otoño, pero no creo que haya menos gente.', 'Je crois que le Chemin est plus beau en automne, mais je ne crois pas qu’il y ait moins de monde.', 'I think the Camino is more beautiful in autumn, but I don’t think there are fewer people.'),
        x('Tienes razón: la gran ventaja de ir a pie es que conoces a mucha gente.', 'Tu as raison : le grand avantage d’y aller à pied, c’est qu’on rencontre beaucoup de gens.', 'You’re right: the great advantage of going on foot is that you meet lots of people.'),
      ], [
        FB(CHOOSE, 'No creo que ＿ demasiado tarde.', ['sea', 'es', 'será'], 'sea', ('No creo que + subjonctif.', 'No creo que + subjunctive.'), ('Je ne crois pas qu’il soit trop tard.', 'I don’t think it’s too late.')),
        FB(CHOOSE, 'Creo que ＿ razón.', ['tienes', 'tengas', 'tuvieras'], 'tienes', ('Creo que + indicatif.', 'Creo que + indicative.'), ('Je crois que tu as raison.', 'I think you’re right.')),
        DC(ANSWER, [('Bodeguero', 'El vino de Rioja es el mejor de España, ¿no?')], ('Le vigneron dit que le rioja est le meilleur vin d’Espagne ; tu n’es pas tout à fait d’accord.', 'The winemaker says Rioja is the best wine in Spain; you don’t quite agree.'), ['Depende, yo no lo veo así: el de Ribera también es muy bueno.', 'Depende, no creo que es el mejor.', 'Tienes razón no.'], 'Depende, yo no lo veo así: el de Ribera también es muy bueno.', ('Nuancer : depende, yo no lo veo así.', 'Hedging: depende, yo no lo veo así.')),
        TF('No estoy de acuerdo contigo.', ('La personne partage ton avis.', 'The person shares your view.'), FAUX, ('No estoy de acuerdo = je ne suis pas d’accord.', 'No estoy de acuerdo = I don’t agree.')),
      ]),
  ]),
  CH('deleb1-w2-c2', ('Conseils de pèlerins', 'Pilgrims’ advice'), [
    L('es-valorar', ('Il est important que… : juger et évaluer', 'It’s important that…: making judgements'), ('Porter un jugement avec es importante que, es verdad que, está claro que.', 'Make judgements with es importante que, es verdad que, está claro que.'), 9, [
        ('Es importante / necesario / mejor / normal / lógico que + subjonctif : Es importante que bebas agua.', 'Es importante / necesario / mejor / normal / lógico que + subjunctive: Es importante que bebas agua.'),
        ('Sans sujet précis, on garde l’infinitif : Es importante beber agua.', 'With no specific subject, keep the infinitive: Es importante beber agua.'),
        ('La certitude prend l’indicatif : es verdad que, está claro que, es evidente que + indicatif. Mais à la forme négative : No es verdad que + subjonctif.', 'Certainty takes the indicative: es verdad que, está claro que, es evidente que + indicative. But in the negative: No es verdad que + subjunctive.'),
      ], [
        SG('es-importante-que', 'es importante que + subjuntivo', ('il est important que + subjonctif', 'it’s important that + subjunctive')),
        SG('es-verdad-que', 'es verdad que + indicativo', ('il est vrai que + indicatif', 'it’s true that + indicative')),
        S('es-necesario', 'es necesario', ('il est nécessaire', 'it’s necessary')),
        S('es-logico', 'es lógico / es normal', ('c’est logique / c’est normal', 'it makes sense / it’s normal')),
        S('esta-claro', 'está claro que…', ('il est clair que…', 'it’s clear that…')),
        S('la-ampolla', 'la ampolla', ('l’ampoule (au pied)', 'the blister')),
        S('la-crema-solar', 'la crema solar', ('la crème solaire', 'the sun cream')),
        S('hidratarse', 'hidratarse', ('s’hydrater', 'to stay hydrated')),
      ], [
        x('Es importante que te pongas crema solar y que bebas mucha agua.', 'Il est important que tu mettes de la crème solaire et que tu boives beaucoup d’eau.', 'It’s important that you put on sun cream and drink plenty of water.'),
        x('Es normal que tengas ampollas los primeros días.', 'C’est normal que tu aies des ampoules les premiers jours.', 'It’s normal to get blisters in the first few days.'),
      ], [
        FB(CHOOSE, 'Es mejor que ＿ temprano, antes del calor.', ['salgamos', 'salimos', 'saldremos'], 'salgamos', ('Es mejor que + subjonctif.', 'Es mejor que + subjunctive.'), ('Il vaut mieux que nous partions tôt, avant la chaleur.', 'It’s better that we leave early, before the heat.')),
        FB(CHOOSE, 'Está claro que el Camino ＿ duro.', ['es', 'sea', 'fuera'], 'es', ('Certitude : está claro que + indicatif.', 'Certainty: está claro que + indicative.'), ('Il est clair que le Chemin est dur.', 'It’s clear that the Camino is hard.')),
        FB(CHOOSE, 'Es importante ＿ agua durante la etapa.', ['beber', 'que beber', 'bebas'], 'beber', ('Sans sujet : es importante + infinitif.', 'With no subject: es importante + infinitive.'), ('Il est important de boire de l’eau pendant l’étape.', 'It’s important to drink water during the stage.')),
        TF('No es verdad que el albergue esté cerrado.', ('Le gîte est fermé.', 'The hostel is closed.'), FAUX, ('No es verdad que… = ce n’est pas vrai : le gîte est ouvert.', 'No es verdad que… = it isn’t true: the hostel is open.')),
      ]),
  ])])

# ═════════════════════════ 3 : Burgos — souhaits, demandes et sentiments ═════════════════════════
W3 = WORLD('deleb1-w3', ('La cathédrale de Burgos', 'Burgos cathedral'), REGION,
  ('Exprimer des souhaits (ojalá, espero que), demander et recommander (pedir que, recomendar que) et réagir avec ses sentiments (me alegra que, me molesta que).', 'Express wishes (ojalá, espero que), ask and recommend (pedir que, recomendar que) and react with your feelings (me alegra que, me molesta que).'),
  (('La Tarasca de la procession', 'The Tarasca of the procession'), 'º', ('La Tarasca, dragon de carton des processions de Castille, s’est réveillée pour de bon et sème la panique sur la place de la cathédrale. Elle ne se calme que si l’on exprime ses souhaits et ses sentiments avec délicatesse.', 'The Tarasca, the papier-mâché dragon of Castilian processions, has woken up for real and is causing panic in the cathedral square. It only calms down if you express your wishes and feelings tactfully.')),
  [CH('deleb1-w3-c1', ('Sur le parvis', 'On the cathedral square'), [
    L('es-deseos', ('Pourvu qu’il fasse beau ! ojalá, espero que', 'Hopefully it’ll be sunny! ojalá, espero que'), ('Exprimer des souhaits et des vœux avec le subjonctif.', 'Express wishes and good wishes with the subjunctive.'), 9, [
        ('Ojalá + subjonctif : Ojalá no llueva mañana (pourvu qu’il ne pleuve pas demain). Espero que + subjonctif : Espero que te guste.', 'Ojalá + subjunctive: Ojalá no llueva mañana (hopefully it won’t rain tomorrow). Espero que + subjunctive: Espero que te guste.'),
        ('Même sujet → infinitif : Quiero visitar la catedral. Sujets différents → que + subjonctif : Quiero que visites la catedral.', 'Same subject → infinitive: Quiero visitar la catedral. Different subjects → que + subjunctive: Quiero que visites la catedral.'),
        ('Les vœux du quotidien : ¡Que tengas buen viaje! ¡Que aproveche! (bon appétit) ¡Que te mejores! (bon rétablissement).', 'Everyday good wishes: ¡Que tengas buen viaje! ¡Que aproveche! (enjoy your meal) ¡Que te mejores! (get well soon).'),
      ], [
        SG('ojala', 'ojalá + subjuntivo', ('pourvu que…, si seulement…', 'hopefully…, if only…')),
        SG('quiero-que', 'quiero que + subjuntivo', ('je veux que + subjonctif', 'I want (someone) to…')),
        S('espero-que', 'espero que…', ('j’espère que…', 'I hope that…')),
        S('que-aproveche', '¡Que aproveche!', ('Bon appétit !', 'Enjoy your meal!')),
        S('que-te-mejores', '¡Que te mejores!', ('Bon rétablissement !', 'Get well soon!')),
        S('el-deseo', 'el deseo', ('le souhait, le désir', 'the wish, the desire')),
        S('la-catedral', 'la catedral', ('la cathédrale', 'the cathedral')),
        S('el-claustro', 'el claustro', ('le cloître', 'the cloister')),
      ], [
        x('Ojalá podamos ver el claustro de la catedral antes de que cierre.', 'Pourvu que nous puissions voir le cloître de la cathédrale avant qu’il ferme.', 'Hopefully we can see the cathedral cloister before it closes.'),
        x('Mis padres quieren que les mande una foto desde Burgos.', 'Mes parents veulent que je leur envoie une photo de Burgos.', 'My parents want me to send them a photo from Burgos.'),
      ], [
        FB(CHOOSE, 'Ojalá ＿ sol mañana.', ['haga', 'hace', 'hará'], 'haga', ('Ojalá + subjonctif.', 'Ojalá + subjunctive.'), ('Pourvu qu’il fasse soleil demain.', 'Hopefully it’ll be sunny tomorrow.')),
        FB(CHOOSE, 'Quiero ＿ la catedral esta tarde.', ['visitar', 'que visite', 'visite'], 'visitar', ('Même sujet : infinitif.', 'Same subject: infinitive.'), ('Je veux visiter la cathédrale cet après-midi.', 'I want to visit the cathedral this afternoon.')),
        FB(CHOOSE, 'Mi madre quiere que la ＿ todos los días.', ['llame', 'llamo', 'llamar'], 'llame', ('Sujets différents : que + subjonctif.', 'Different subjects: que + subjunctive.'), ('Ma mère veut que je l’appelle tous les jours.', 'My mother wants me to call her every day.')),
        DC(ANSWER, [('Hospitalera', 'Estoy un poco enferma, tengo fiebre.')], ('La responsable du gîte te dit qu’elle est malade.', 'The hostel warden tells you she is ill.'), ['¡Vaya! ¡Que te mejores!', '¡Que aproveche!', '¡Felicidades!'], '¡Vaya! ¡Que te mejores!', ('À une personne malade : ¡Que te mejores!', 'To someone who is ill: ¡Que te mejores!')),
      ]),
    L('es-peticiones', ('Je te recommande de… : pedir, recomendar que', 'I recommend you…: pedir, recomendar que'), ('Demander, recommander, permettre ou interdire avec que + subjonctif.', 'Ask, recommend, allow or forbid with que + subjunctive.'), 9, [
        ('Pedir, recomendar, aconsejar, sugerir que + subjonctif : Te recomiendo que visites el museo. Le pido que hable más despacio.', 'Pedir, recomendar, aconsejar, sugerir que + subjunctive: Te recomiendo que visites el museo. Le pido que hable más despacio.'),
        ('Permettre et interdire : permitir que, prohibir que, no dejar que (ne pas laisser) + subjonctif : No dejan que entremos con la mochila.', 'Allowing and forbidding: permitir que, prohibir que, no dejar que (not to let) + subjunctive: No dejan que entremos con la mochila.'),
        ('Pour rapporter une consigne : El hospitalero nos ha pedido que apaguemos la luz a las diez.', 'To report an instruction: El hospitalero nos ha pedido que apaguemos la luz a las diez.'),
      ], [
        SG('pedir-que', 'pedir que + subjuntivo', ('demander que + subjonctif', 'to ask (someone) to…')),
        SG('recomendar-que', 'recomendar que + subjuntivo', ('recommander que + subjonctif', 'to recommend that…')),
        S('aconsejar', 'aconsejar', ('conseiller', 'to advise')),
        S('sugerir', 'sugerir', ('suggérer, proposer', 'to suggest')),
        S('permitir', 'permitir', ('permettre, autoriser', 'to allow')),
        S('dejar-que', 'dejar que…', ('laisser (quelqu’un faire)', 'to let (someone do)')),
        S('apagar', 'apagar / encender', ('éteindre / allumer', 'to switch off / to switch on')),
        S('el-hospitalero', 'el hospitalero / la hospitalera', ('le responsable / la responsable du gîte', 'the hostel warden')),
      ], [
        x('El hospitalero nos pide que apaguemos la luz a las diez y que no hagamos ruido.', 'Le responsable du gîte nous demande d’éteindre la lumière à dix heures et de ne pas faire de bruit.', 'The hostel warden asks us to switch off the light at ten and not to make any noise.'),
        x('Te recomiendo que subas a la torre: las vistas son increíbles.', 'Je te recommande de monter dans la tour : la vue est incroyable.', 'I recommend you go up the tower: the views are amazing.'),
      ], [
        FB(CHOOSE, 'Le pido que ＿ más despacio, por favor.', ['hable', 'habla', 'hablará'], 'hable', ('Pedir que + subjonctif.', 'Pedir que + subjunctive.'), ('Je vous demande de parler plus lentement, s’il vous plaît.', 'Please speak more slowly.')),
        FB(CHOOSE, 'El médico me aconseja que ＿ dos días.', ['descanse', 'descanso', 'descansar'], 'descanse', ('Aconsejar que + subjonctif.', 'Aconsejar que + subjunctive.'), ('Le médecin me conseille de me reposer deux jours.', 'The doctor advises me to rest for two days.')),
        FB(CHOOSE, 'En la catedral no permiten que ＿ fotos con flash.', ['hagamos', 'hacemos', 'hacer'], 'hagamos', ('Permitir que + subjonctif.', 'Permitir que + subjunctive.'), ('Dans la cathédrale, on ne nous permet pas de prendre des photos au flash.', 'In the cathedral they don’t let us take flash photos.')),
        TF('Nos han pedido que no hagamos ruido.', ('On leur a demandé d’être silencieux.', 'They have been asked to be quiet.'), VRAI, ('Pedir que no hagamos ruido = demander de ne pas faire de bruit.', 'Pedir que no hagamos ruido = to ask us not to make noise.')),
      ]),
  ]),
  CH('deleb1-w3-c2', ('Le cœur du pèlerin', 'The pilgrim’s heart'), [
    L('es-sentimientos', ('Ça me fait plaisir que… : les sentiments', 'I’m glad that…: feelings'), ('Réagir et exprimer ses sentiments avec que + subjonctif.', 'React and express feelings with que + subjunctive.'), 9, [
        ('Ces verbes se construisent comme gustar, avec que + subjonctif : Me alegra que estés aquí (ça me fait plaisir que tu sois là). Me molesta que haya tanto ruido.', 'These verbs work like gustar, with que + subjunctive: Me alegra que estés aquí (I’m glad you’re here). Me molesta que haya tanto ruido.'),
        ('Autres réactions : me sorprende que (ça me surprend que), me preocupa que (ça m’inquiète que), me da pena que (ça me fait de la peine que), tengo miedo de que.', 'Other reactions: me sorprende que (it surprises me that), me preocupa que (it worries me that), me da pena que (it’s a shame that), tengo miedo de que (I’m afraid that).'),
        ('Même personne → infinitif : Me alegra estar aquí. Me da pena irme.', 'Same person → infinitive: Me alegra estar aquí. Me da pena irme.'),
      ], [
        SG('me-alegra-que', 'me alegra que + subjuntivo', ('ça me fait plaisir que + subjonctif', 'I’m glad that + subjunctive')),
        S('me-molesta', 'me molesta que…', ('ça me dérange que…', 'it bothers me that…')),
        S('me-sorprende', 'me sorprende que…', ('ça me surprend que…', 'it surprises me that…')),
        S('me-preocupa', 'me preocupa que…', ('ça m’inquiète que…', 'it worries me that…')),
        S('me-da-pena', 'me da pena que…', ('ça me fait de la peine que…', 'it’s a shame that…')),
        S('tener-miedo-de', 'tener miedo de', ('avoir peur de', 'to be afraid of')),
        S('roncar', 'roncar', ('ronfler', 'to snore')),
        S('emocionarse', 'emocionarse', ('être ému', 'to be moved')),
      ], [
        x('Me alegra mucho que caminemos juntos hasta León.', 'Ça me fait très plaisir que nous marchions ensemble jusqu’à León.', 'I’m really glad we’re walking together as far as León.'),
        x('Me molesta que la gente ronque en el albergue, pero me da pena despertarla.', 'Ça me dérange que les gens ronflent au gîte, mais ça me fait de la peine de les réveiller.', 'It bothers me when people snore in the hostel, but I feel bad waking them up.'),
      ], [
        FB(CHOOSE, 'Me alegra que ＿ aquí.', ['estés', 'estás', 'estar'], 'estés', ('Me alegra que + subjonctif.', 'Me alegra que + subjunctive.'), ('Ça me fait plaisir que tu sois là.', 'I’m glad you’re here.')),
        FB(CHOOSE, 'Me preocupa que mi amigo no ＿ el teléfono.', ['conteste', 'contesta', 'contestar'], 'conteste', ('Me preocupa que + subjonctif.', 'Me preocupa que + subjunctive.'), ('Ça m’inquiète que mon ami ne réponde pas au téléphone.', 'It worries me that my friend isn’t answering the phone.')),
        FB(CHOOSE, 'Me da pena ＿ tan pronto.', ['irme', 'que me vaya', 'me voy'], 'irme', ('Même personne : infinitif.', 'Same person: infinitive.'), ('Ça me fait de la peine de partir si tôt.', 'I’m sad to leave so soon.')),
        DC(ANSWER, [('Amiga', '¡Mañana llego a Santiago!')], ('Ton amie t’annonce qu’elle arrive demain à Saint-Jacques.', 'Your friend tells you she’s arriving in Santiago tomorrow.'), ['¡Qué bien! Me alegro mucho por ti.', '¡Qué pena! Me alegra.', 'Me molesta que llegas.'], '¡Qué bien! Me alegro mucho por ti.', ('Se réjouir pour quelqu’un : me alegro mucho por ti.', 'Being happy for someone: me alegro mucho por ti.')),
      ]),
  ])])

# ═════════════════════════ 4 : la Meseta — le temps, le but, le plus-que-parfait ═════════════════════════
W4 = WORLD('deleb1-w4', ('La Meseta infinie', 'The endless Meseta'), REGION,
  ('Situer une action dans le futur avec cuando + subjonctif, exprimer le but (para que) et la cause (como, ya que), et raconter ce qui s’était passé avant (plus-que-parfait).', 'Place an action in the future with cuando + subjunctive, express purpose (para que) and cause (como, ya que), and tell what had happened before (past perfect).'),
  (('Le Basilic de la Meseta', 'The Basilisk of the Meseta'), 'ª', ('Sous le soleil de la Meseta, le Basilic, roi des serpents des légendes castillanes, pétrifie d’un regard les pèlerins qui perdent la notion du temps. Dis-lui ce que tu feras quand tu arriveras, pourquoi tu marches et ce qui s’était passé avant.', 'Under the Meseta sun, the Basilisk, king of serpents in Castilian legend, turns to stone with a glance any pilgrim who loses track of time. Tell it what you will do when you arrive, why you are walking and what had happened before.')),
  [CH('deleb1-w4-c1', ('Entre les blés', 'Among the wheat fields'), [
    L('es-cuando', ('Quand j’arriverai : cuando + subjonctif', 'When I arrive: cuando + subjunctive'), ('Employer cuando, en cuanto et hasta que avec l’indicatif ou le subjonctif.', 'Use cuando, en cuanto and hasta que with the indicative or the subjunctive.'), 10, [
        ('Cuando + indicatif pour une habitude ou le passé : Cuando llego, me ducho. Cuando llegué, me duché.', 'Cuando + indicative for a habit or the past: Cuando llego, me ducho. Cuando llegué, me duché.'),
        ('Cuando + subjonctif pour le futur : Cuando llegue a Santiago, te llamaré (quand j’arriverai). Jamais de futur après cuando.', 'Cuando + subjunctive for the future: Cuando llegue a Santiago, te llamaré (when I get to Santiago, I’ll call you). Never use the future after cuando.'),
        ('Même règle avec en cuanto (dès que) et hasta que (jusqu’à ce que) : No pararemos hasta que encontremos un albergue.', 'Same rule with en cuanto (as soon as) and hasta que (until): No pararemos hasta que encontremos un albergue.'),
      ], [
        SG('cuando-subj', 'cuando + subjuntivo (futuro)', ('quand + futur (subjonctif en espagnol)', 'when + future (subjunctive in Spanish)')),
        S('en-cuanto', 'en cuanto', ('dès que, aussitôt que', 'as soon as')),
        S('hasta-que', 'hasta que', ('jusqu’à ce que', 'until')),
        S('la-meseta', 'la meseta', ('le plateau (la Meseta)', 'the plateau (the Meseta)')),
        S('el-trigo', 'el trigo', ('le blé', 'wheat')),
        S('la-sombra', 'la sombra', ('l’ombre', 'the shade, the shadow')),
        S('parar', 'parar', ('s’arrêter', 'to stop')),
        S('el-horizonte', 'el horizonte', ('l’horizon', 'the horizon')),
      ], [
        x('Cuando lleguemos a Sahagún, buscaremos una sombra para comer.', 'Quand nous arriverons à Sahagún, nous chercherons un coin d’ombre pour manger.', 'When we get to Sahagún, we’ll look for some shade to eat in.'),
        x('En cuanto veas la iglesia, gira a la izquierda.', 'Dès que tu verras l’église, tourne à gauche.', 'As soon as you see the church, turn left.'),
      ], [
        FB(CHOOSE, 'Cuando ＿ a Santiago, te llamaré.', ['llegue', 'llegaré', 'llego'], 'llegue', ('Futur : cuando + subjonctif.', 'Future: cuando + subjunctive.'), ('Quand j’arriverai à Saint-Jacques, je t’appellerai.', 'When I get to Santiago, I’ll call you.')),
        FB(CHOOSE, 'Cuando ＿ pequeño, vivía en el campo.', ['era', 'sea', 'seré'], 'era', ('Passé : cuando + indicatif.', 'Past: cuando + indicative.'), ('Quand j’étais petit, je vivais à la campagne.', 'When I was little, I lived in the countryside.')),
        FB(CHOOSE, 'No pararemos hasta que ＿ un pueblo.', ['encontremos', 'encontramos', 'encontraremos'], 'encontremos', ('Hasta que (futur) + subjonctif.', 'Hasta que (future) + subjunctive.'), ('Nous ne nous arrêterons pas avant d’avoir trouvé un village.', 'We won’t stop until we find a village.')),
        TF('En cuanto termine la etapa, me ducharé.', ('La personne se douchera après l’étape.', 'The person will shower after the stage.'), VRAI, ('En cuanto = dès que.', 'En cuanto = as soon as.')),
      ]),
    L('es-para-que', ('Pour que tu ne te perdes pas : le but et la cause', 'So you don’t get lost: purpose and cause'), ('Exprimer le but (para, para que) et la cause (porque, como, ya que).', 'Express purpose (para, para que) and cause (porque, como, ya que).'), 9, [
        ('Para + infinitif quand le sujet est le même : Camino para conocerme mejor. Para que + subjonctif quand il change : Te dejo mi mapa para que no te pierdas.', 'Para + infinitive when the subject is the same: Camino para conocerme mejor. Para que + subjunctive when it changes: Te dejo mi mapa para que no te pierdas.'),
        ('La cause : porque + indicatif ; como en début de phrase : Como hacía calor, salimos de noche. Ya que (puisque) : Ya que estás aquí, ayúdame.', 'Cause: porque + indicative; como at the start of a sentence: Como hacía calor, salimos de noche. Ya que (since): Ya que estás aquí, ayúdame.'),
        ('Demander la raison : ¿Por qué…? ; le but : ¿Para qué…? ¿Para qué sirve la credencial? — Para que te pongan un sello en cada albergue.', 'Asking for the reason: ¿Por qué…?; the purpose: ¿Para qué…? ¿Para qué sirve la credencial? — Para que te pongan un sello en cada albergue.'),
      ], [
        SG('para-que', 'para que + subjuntivo', ('pour que + subjonctif', 'so that + subjunctive')),
        SG('como-causa', 'como + causa', ('comme (cause, en début de phrase)', 'as, since (cause, at the start)')),
        S('ya-que', 'ya que', ('puisque', 'since, given that')),
        S('para-que-sirve', '¿Para qué sirve…?', ('À quoi sert… ?', 'What is… for?')),
        S('perderse', 'perderse', ('se perdre', 'to get lost')),
        S('la-credencial', 'la credencial', ('le carnet du pèlerin (la crédentiale)', 'the pilgrim passport (credencial)')),
        S('el-sello', 'el sello', ('le tampon, le timbre', 'the stamp')),
        S('la-flecha', 'la flecha amarilla', ('la flèche jaune', 'the yellow arrow')),
      ], [
        x('Te dejo mi mapa para que no te pierdas en la Meseta.', 'Je te laisse ma carte pour que tu ne te perdes pas sur la Meseta.', 'I’ll leave you my map so you don’t get lost on the Meseta.'),
        x('Como hacía mucho calor, salimos antes del amanecer y seguimos las flechas amarillas.', 'Comme il faisait très chaud, nous sommes partis avant l’aube et avons suivi les flèches jaunes.', 'As it was very hot, we set off before dawn and followed the yellow arrows.'),
      ], [
        FB(CHOOSE, 'Te doy mi número para que me ＿ si hay un problema.', ['llames', 'llamas', 'llamar'], 'llames', ('Para que + subjonctif.', 'Para que + subjunctive.'), ('Je te donne mon numéro pour que tu m’appelles s’il y a un problème.', 'I’m giving you my number so you can call me if there’s a problem.')),
        FB(CHOOSE, 'Camino ＿ conocer gente de todo el mundo.', ['para', 'para que', 'porque'], 'para', ('Même sujet : para + infinitif.', 'Same subject: para + infinitive.'), ('Je marche pour rencontrer des gens du monde entier.', 'I walk to meet people from all over the world.')),
        FB(CHOOSE, '＿ estaba cansado, me quedé en el albergue.', ['Como', 'Porque', 'Para que'], 'Como', ('Cause en début de phrase : como.', 'Cause at the start of a sentence: como.'), ('Comme j’étais fatigué, je suis resté au gîte.', 'As I was tired, I stayed in the hostel.')),
        DC(ANSWER, [('Peregrino', '¿Para qué sirve la credencial?')], ('Un pèlerin demande à quoi sert la crédentiale.', 'A pilgrim asks what the credencial is for.'), ['Para que te pongan un sello en cada albergue.', 'Porque te ponen un sello.', 'Para que pones un sello.'], 'Para que te pongan un sello en cada albergue.', ('But : para que + subjonctif.', 'Purpose: para que + subjunctive.')),
      ]),
  ]),
  CH('deleb1-w4-c2', ('Le village abandonné', 'The abandoned village'), [
    L('es-pluscuamperfecto', ('Le gîte avait fermé : le plus-que-parfait', 'The hostel had closed: the past perfect'), ('Raconter une action antérieure à une autre action passée.', 'Tell an action that came before another past action.'), 9, [
        ('Plus-que-parfait = haber à l’imparfait + participe : había, habías, había, habíamos, habíais, habían + llegado.', 'Past perfect = haber in the imperfect + participle: había, habías, había, habíamos, habíais, habían + llegado.'),
        ('Il marque ce qui s’était passé avant un autre moment du passé : Cuando llegué, el albergue ya había cerrado. Todavía no había visto el mar.', 'It shows what had happened before another moment in the past: Cuando llegué, el albergue ya había cerrado. Todavía no había visto el mar.'),
        ('Nunca antes había… = jamais auparavant je n’avais… : Nunca antes había caminado tanto.', 'Nunca antes había… = I had never… before: Nunca antes había caminado tanto.'),
      ], [
        SG('pluscuamperfecto', 'había + participio', ('j’avais + participe (plus-que-parfait)', 'I had + participle (past perfect)')),
        S('nunca-antes', 'nunca antes', ('jamais auparavant', 'never before')),
        S('ya-habia', 'ya había…', ('avait déjà…', 'had already…')),
        S('el-amanecer', 'el amanecer', ('l’aube, le lever du jour', 'dawn, sunrise')),
        S('agotado', 'agotado / agotada', ('épuisé / épuisée', 'exhausted')),
        S('el-cansancio', 'el cansancio', ('la fatigue', 'tiredness')),
        S('cerrar', 'cerrar', ('fermer', 'to close')),
        S('abandonado', 'abandonado / abandonada', ('abandonné / abandonnée', 'abandoned')),
      ], [
        x('Cuando llegamos a Carrión, el albergue ya había cerrado y tuvimos que dormir en la iglesia.', 'Quand nous sommes arrivés à Carrión, le gîte avait déjà fermé et nous avons dû dormir à l’église.', 'When we got to Carrión, the hostel had already closed and we had to sleep in the church.'),
        x('Nunca antes había caminado tanto: estaba agotada pero feliz.', 'Jamais auparavant je n’avais autant marché : j’étais épuisée mais heureuse.', 'I had never walked so far before: I was exhausted but happy.'),
      ], [
        FB(CHOOSE, 'Cuando llegué, el tren ya ＿ salido.', ['había', 'ha', 'hubo'], 'había', ('Antériorité dans le passé : había + participe.', 'Earlier past: había + participle.'), ('Quand je suis arrivé, le train était déjà parti.', 'When I arrived, the train had already left.')),
        FB(CHOOSE, 'Nunca antes ＿ un paisaje tan grande.', ['había visto', 'había vido', 'habría ver'], 'había visto', ('Ver → visto.', 'Ver → visto.'), ('Jamais auparavant je n’avais vu un paysage aussi vaste.', 'I had never seen such a vast landscape before.')),
        FB(CHOOSE, 'Estaba agotado porque ＿ treinta kilómetros.', ['había caminado', 'caminaré', 'camine'], 'había caminado', ('Cause antérieure : plus-que-parfait.', 'Earlier cause: past perfect.'), ('J’étais épuisé parce que j’avais marché trente kilomètres.', 'I was exhausted because I had walked thirty kilometres.')),
        order(('Remets dans l’ordre : « Le gîte avait déjà fermé. »', 'Put in order: “The hostel had already closed.”'), ['El', 'albergue', 'ya', 'había', 'cerrado.'], ('Ya se place avant había.', 'Ya goes before había.')),
      ]),
  ])])

# ═════════════════════════ 5 : León — les relatifs, le discours rapporté ═════════════════════════
W5 = WORLD('deleb1-w5', ('Les vitraux de León', 'The stained glass of León'), REGION,
  ('Relier ses phrases avec les relatifs (que, donde, lo que, con quien), choisir l’indicatif ou le subjonctif après un relatif, et rapporter les paroles de quelqu’un.', 'Link sentences with relative pronouns (que, donde, lo que, con quien), choose the indicative or the subjunctive after a relative, and report what someone said.'),
  (('Le Trenti de la forêt', 'The forest Trenti'), '«', ('Le Trenti, petit lutin cantabre couvert de mousse et de feuilles, s’est glissé dans la cathédrale de León et a mélangé tous les messages des pèlerins. Rapporte fidèlement ce que chacun a dit, et il retournera dans sa forêt.', 'The Trenti, a little Cantabrian goblin covered in moss and leaves, has slipped into León cathedral and mixed up all the pilgrims’ messages. Report faithfully what everyone said, and it will go back to its forest.')),
  [CH('deleb1-w5-c1', ('Sous les vitraux', 'Under the stained glass'), [
    L('es-relativos', ('Ce qui m’a le plus plu : que, donde, lo que', 'What I liked most: que, donde, lo que'), ('Relier deux phrases avec les pronoms relatifs.', 'Link two sentences with relative pronouns.'), 9, [
        ('Que est le relatif le plus courant, pour les personnes et les choses : El peregrino que conocí ayer es italiano. Donde pour un lieu : el pueblo donde dormimos.', 'Que is the most common relative, for people and things: El peregrino que conocí ayer es italiano. Donde for a place: el pueblo donde dormimos.'),
        ('Après une préposition : el / la / los / las que (la mochila con la que viajo) ; quien pour une personne (la chica con quien hablé).', 'After a preposition: el / la / los / las que (la mochila con la que viajo); quien for a person (la chica con quien hablé).'),
        ('Lo que = ce que, ce qui : Lo que más me gusta es el silencio. No entiendo lo que dices.', 'Lo que = what: Lo que más me gusta es el silencio. No entiendo lo que dices.'),
      ], [
        SG('relativo-que', 'que / donde', ('qui, que / où (relatifs)', 'who, which, that / where (relatives)')),
        SG('el-que', 'el que / la que / lo que', ('celui que / celle que / ce que', 'the one that / what')),
        S('quien', 'quien / quienes', ('qui (personne, après une préposition)', 'whom, who (after a preposition)')),
        S('la-vidriera', 'la vidriera', ('le vitrail', 'the stained-glass window')),
        S('el-silencio', 'el silencio', ('le silence', 'silence')),
        S('brillar', 'brillar', ('briller', 'to shine')),
        S('el-recuerdo', 'el recuerdo', ('le souvenir', 'the memory, the souvenir')),
        S('impresionar', 'impresionar', ('impressionner', 'to impress')),
      ], [
        x('Lo que más me impresionó de León fueron las vidrieras de la catedral.', 'Ce qui m’a le plus impressionné à León, ce sont les vitraux de la cathédrale.', 'What impressed me most in León was the cathedral’s stained glass.'),
        x('Esta es la plaza donde conocí a la peregrina con la que camino desde Burgos.', 'Voici la place où j’ai rencontré la pèlerine avec qui je marche depuis Burgos.', 'This is the square where I met the pilgrim I’ve been walking with since Burgos.'),
      ], [
        FB(CHOOSE, 'Ese es el bar ＿ cenamos anoche.', ['donde', 'que', 'quien'], 'donde', ('Un lieu : donde.', 'A place: donde.'), ('C’est le bar où nous avons dîné hier soir.', 'That’s the bar where we had dinner last night.')),
        FB(CHOOSE, 'No entiendo ＿ dices.', ['lo que', 'que', 'el que'], 'lo que', ('Ce que : lo que.', 'What: lo que.'), ('Je ne comprends pas ce que tu dis.', 'I don’t understand what you’re saying.')),
        FB(CHOOSE, 'Es la amiga con ＿ viajo.', ['la que', 'que', 'lo que'], 'la que', ('Après une préposition : la que.', 'After a preposition: la que.'), ('C’est l’amie avec qui je voyage.', 'She’s the friend I travel with.')),
        order(('Remets dans l’ordre : « Le pèlerin que j’ai rencontré est italien. »', 'Put in order: “The pilgrim I met is Italian.”'), ['El', 'peregrino', 'que', 'conocí', 'es', 'italiano.'], ('Nom + que + verbe.', 'Noun + que + verb.')),
      ]),
    L('es-relativo-subjuntivo', ('Je cherche un gîte qui ait… : relatif + subjonctif', 'I’m looking for a hostel that has…: relative + subjunctive'), ('Choisir l’indicatif ou le subjonctif après un relatif.', 'Choose the indicative or the subjunctive after a relative.'), 9, [
        ('Relatif + indicatif quand on connaît ce dont on parle : Conozco un albergue que tiene piscina.', 'Relative + indicative when you know what you’re talking about: Conozco un albergue que tiene piscina.'),
        ('Relatif + subjonctif quand on ne sait pas si cela existe : Busco un albergue que tenga lavadora. ¿Hay alguien que hable inglés?', 'Relative + subjunctive when you don’t know if it exists: Busco un albergue que tenga lavadora. ¿Hay alguien que hable inglés?'),
        ('Après une négation, toujours le subjonctif : No hay nadie que sepa la respuesta. No conozco a nadie que viva aquí.', 'After a negative, always the subjunctive: No hay nadie que sepa la respuesta. No conozco a nadie que viva aquí.'),
      ], [
        SG('relativo-subj', 'busco algo que + subjuntivo', ('je cherche quelque chose qui + subjonctif', 'I’m looking for something that + subjunctive')),
        S('alguien', 'alguien / nadie', ('quelqu’un / personne', 'someone / no one')),
        S('algo-nada', 'algo / nada', ('quelque chose / rien', 'something / nothing')),
        S('la-lavadora', 'la lavadora', ('la machine à laver', 'the washing machine')),
        S('el-enchufe', 'el enchufe', ('la prise (électrique)', 'the socket, the plug')),
        S('la-litera', 'la litera', ('le lit superposé', 'the bunk bed')),
        S('compartir', 'compartir', ('partager', 'to share')),
        S('silencioso', 'silencioso / silenciosa', ('silencieux / silencieuse', 'silent')),
      ], [
        x('Busco un albergue que tenga lavadora y que no sea muy caro.', 'Je cherche un gîte qui ait une machine à laver et qui ne soit pas trop cher.', 'I’m looking for a hostel that has a washing machine and isn’t too expensive.'),
        x('¿Hay alguien que tenga un cargador? No encuentro ningún enchufe libre.', 'Est-ce que quelqu’un a un chargeur ? Je ne trouve aucune prise libre.', 'Has anyone got a charger? I can’t find a free socket.'),
      ], [
        FB(CHOOSE, 'Busco a alguien que ＿ alemán.', ['hable', 'habla', 'hablará'], 'hable', ('On ne sait pas si cette personne existe : subjonctif.', 'We don’t know if this person exists: subjunctive.'), ('Je cherche quelqu’un qui parle allemand.', 'I’m looking for someone who speaks German.')),
        FB(CHOOSE, 'Tengo un amigo que ＿ en León.', ['vive', 'viva', 'vivir'], 'vive', ('Personne connue : indicatif.', 'Known person: indicative.'), ('J’ai un ami qui vit à León.', 'I have a friend who lives in León.')),
        FB(CHOOSE, 'No hay nadie que ＿ la respuesta.', ['sepa', 'sabe', 'sabrá'], 'sepa', ('Après une négation : subjonctif.', 'After a negative: subjunctive.'), ('Personne ne connaît la réponse.', 'Nobody knows the answer.')),
        TF('Busco un albergue que tenga literas libres.', ('La personne connaît déjà un gîte précis avec des lits libres.', 'The person already knows a specific hostel with free beds.'), FAUX, ('Subjonctif : on ne sait pas encore s’il existe.', 'Subjunctive: we don’t know yet whether it exists.')),
      ]),
  ]),
  CH('deleb1-w5-c2', ('Les messages mélangés', 'The mixed-up messages'), [
    L('es-estilo-indirecto', ('Il dit que… : le discours rapporté', 'He says that…: reported speech'), ('Rapporter des paroles, des questions et des demandes.', 'Report statements, questions and requests.'), 10, [
        ('Au présent, on garde le temps : «Estoy cansado» → Dice que está cansado. Les questions : pregunta si… (oui / non), pregunta dónde, cuándo, qué…', 'In the present, keep the tense: «Estoy cansado» → Dice que está cansado. Questions: pregunta si… (yes / no), pregunta dónde, cuándo, qué…'),
        ('Les ordres et les demandes passent au subjonctif : «Cierra la puerta» → Dice que cierres la puerta. Me pide que lo llame.', 'Orders and requests go into the subjunctive: «Cierra la puerta» → Dice que cierres la puerta. Me pide que lo llame.'),
        ('Au passé, le présent devient imparfait et le futur conditionnel : «Estoy cansado» → Dijo que estaba cansado ; «Iré mañana» → Dijo que iría al día siguiente.', 'In the past, the present becomes the imperfect and the future the conditional: «Estoy cansado» → Dijo que estaba cansado; «Iré mañana» → Dijo que iría al día siguiente.'),
      ], [
        SG('dice-que', 'dice que…', ('il dit que…', 'he says that…')),
        SG('pregunta-si', 'pregunta si…', ('il demande si…', 'he asks whether…')),
        SG('dijo-que', 'dijo que + imperfecto', ('il a dit que + imparfait', 'he said that + imperfect')),
        S('el-mensaje-de-voz', 'el mensaje de voz', ('le message vocal', 'the voice message')),
        S('al-dia-siguiente', 'al día siguiente', ('le lendemain', 'the next day')),
        S('contestar', 'contestar', ('répondre', 'to answer, to reply')),
        S('avisar', 'avisar', ('prévenir', 'to let (someone) know')),
        S('el-recado', 'el recado', ('le message (laissé à quelqu’un)', 'the message (left for someone)')),
      ], [
        x('Laura dice que está en León y pregunta si queremos cenar con ella.', 'Laura dit qu’elle est à León et demande si nous voulons dîner avec elle.', 'Laura says she’s in León and asks if we want to have dinner with her.'),
        x('El hospitalero dijo que el albergue estaba lleno y que había otro cerca de la plaza.', 'Le responsable a dit que le gîte était complet et qu’il y en avait un autre près de la place.', 'The warden said the hostel was full and that there was another one near the square.'),
      ], [
        FB(CHOOSE, '«Estoy cansado». → Dice que ＿ cansado.', ['está', 'estoy', 'esté'], 'está', ('Il parle de lui : 3e personne, même temps.', 'He talks about himself: 3rd person, same tense.'), ('« Je suis fatigué. » → Il dit qu’il est fatigué.', '“I’m tired.” → He says he’s tired.')),
        FB(CHOOSE, '«¿Hay camas libres?» → Pregunta ＿ hay camas libres.', ['si', 'que', 'qué'], 'si', ('Question oui / non : pregunta si.', 'Yes / no question: pregunta si.'), ('« Y a-t-il des lits libres ? » → Il demande s’il y a des lits libres.', '“Are there any free beds?” → He asks if there are any free beds.')),
        FB(CHOOSE, '«Llámame». → Me pide que lo ＿.', ['llame', 'llamo', 'llamará'], 'llame', ('Demande rapportée : subjonctif.', 'Reported request: subjunctive.'), ('« Appelle-moi. » → Il me demande de l’appeler.', '“Call me.” → He asks me to call him.')),
        FB(CHOOSE, '«Vivo en Roma». → Ayer me dijo que ＿ en Roma.', ['vivía', 'vivo', 'viva'], 'vivía', ('Au passé : présent → imparfait.', 'In the past: present → imperfect.'), ('« J’habite à Rome. » → Hier, il m’a dit qu’il habitait à Rome.', '“I live in Rome.” → Yesterday he told me he lived in Rome.')),
      ]),
  ])])

# ═════════════════════════ 6 : Ponferrada — les périphrases, la durée, la santé ═════════════════════════
W6 = WORLD('deleb1-w6', ('Le château des Templiers', 'The Templar castle'), REGION,
  ('Dire qu’on vient de faire, qu’on recommence ou qu’on continue quelque chose (acabar de, volver a, seguir), exprimer la durée (llevar, desde hace) et expliquer ses symptômes au médecin.', 'Say you have just done, are doing again or are still doing something (acabar de, volver a, seguir), express duration (llevar, desde hace) and explain your symptoms to the doctor.'),
  (('Le Diaño burlón', 'The mocking Diaño'), '»', ('Au château templier de Ponferrada, le Diaño burlón, diable farceur des Asturies et du Bierzo qui change sans cesse de forme, se moque des pèlerins fatigués. Prouve-lui que tu sais dire ce que tu viens de faire, depuis quand tu marches et où tu as mal.', 'At the Templar castle of Ponferrada, the Diaño burlón, the shape-shifting trickster devil of Asturias and El Bierzo, mocks weary pilgrims. Prove to it that you can say what you have just done, how long you have been walking and where it hurts.')),
  [CH('deleb1-w6-c1', ('Dans les remparts', 'Inside the walls'), [
    L('es-perifrasis', ('Je viens d’arriver : acabar de, volver a, seguir', 'I’ve just arrived: acabar de, volver a, seguir'), ('Employer les périphrases verbales les plus courantes.', 'Use the most common verbal periphrases.'), 9, [
        ('Acabar de + infinitif = venir de : Acabo de llegar. Volver a + infinitif = refaire : He vuelto a perder el mapa (j’ai encore perdu la carte).', 'Acabar de + infinitive = to have just: Acabo de llegar. Volver a + infinitive = to do again: He vuelto a perder el mapa (I’ve lost the map again).'),
        ('Empezar a (commencer à), dejar de (arrêter de), ponerse a (se mettre à) : Ha dejado de llover. Se puso a cantar.', 'Empezar a (to start), dejar de (to stop), ponerse a (to start suddenly): Ha dejado de llover. Se puso a cantar.'),
        ('Seguir + gérondif = continuer à, être toujours en train de : Sigue lloviendo. ¿Sigues viviendo en Madrid?', 'Seguir + gerund = to keep doing, to still be doing: Sigue lloviendo. ¿Sigues viviendo en Madrid?'),
      ], [
        SG('acabar-de', 'acabar de + infinitivo', ('venir de + infinitif', 'to have just done')),
        SG('volver-a', 'volver a + infinitivo', ('refaire, recommencer à', 'to do again')),
        SG('seguir-gerundio', 'seguir + gerundio', ('continuer à + infinitif', 'to keep doing, to still be doing')),
        S('dejar-de', 'dejar de + infinitivo', ('arrêter de', 'to stop doing')),
        S('empezar-a', 'empezar a + infinitivo', ('commencer à', 'to start doing')),
        S('ponerse-a', 'ponerse a + infinitivo', ('se mettre à', 'to start (suddenly) doing')),
        S('el-templario', 'el templario', ('le templier', 'the Templar')),
        S('la-muralla', 'la muralla', ('la muraille, le rempart', 'the wall (of a city or castle)')),
      ], [
        x('Acabamos de llegar a Ponferrada y ha vuelto a llover.', 'Nous venons d’arriver à Ponferrada et il s’est remis à pleuvoir.', 'We have just arrived in Ponferrada and it has started raining again.'),
        x('¿Sigues caminando con Marco? — No, dejó de caminar en León: le dolía la rodilla.', 'Tu marches toujours avec Marco ? — Non, il a arrêté de marcher à León : il avait mal au genou.', 'Are you still walking with Marco? — No, he stopped walking in León: his knee hurt.'),
      ], [
        FB(CHOOSE, 'Acabo ＿ llegar al albergue.', ['de', 'a', 'que'], 'de', ('Venir de : acabar de.', 'To have just: acabar de.'), ('Je viens d’arriver au gîte.', 'I’ve just arrived at the hostel.')),
        FB(CHOOSE, '¡Por fin ha dejado ＿ llover!', ['de', 'a', 'en'], 'de', ('Arrêter de : dejar de.', 'To stop: dejar de.'), ('Il a enfin arrêté de pleuvoir !', 'It has finally stopped raining!')),
        FB(CHOOSE, 'Sigue ＿ mucho: no podemos salir.', ['nevando', 'nevar', 'nevado'], 'nevando', ('Seguir + gérondif.', 'Seguir + gerund.'), ('Il continue à neiger beaucoup : nous ne pouvons pas sortir.', 'It’s still snowing hard: we can’t go out.')),
        TF('He vuelto a perder las gafas.', ('C’est la première fois que la personne perd ses lunettes.', 'It’s the first time the person has lost their glasses.'), FAUX, ('Volver a = de nouveau.', 'Volver a = again.')),
      ]),
    L('es-llevar-tiempo', ('Je marche depuis trois semaines : llevar, desde hace', 'I’ve been walking for three weeks: llevar, desde hace'), ('Exprimer depuis combien de temps on fait quelque chose.', 'Say how long you have been doing something.'), 9, [
        ('Llevar + durée + gérondif = faire quelque chose depuis… : Llevo tres semanas caminando.', 'Llevar + period + gerund = to have been doing something for…: Llevo tres semanas caminando.'),
        ('Desde hace + durée : Camino desde hace tres semanas. Hace + durée + que : Hace tres semanas que camino. Desde + date : desde el lunes, desde 2020.', 'Desde hace + period: Camino desde hace tres semanas. Hace + period + que: Hace tres semanas que camino. Desde + date: desde el lunes, desde 2020.'),
        ('Pour demander : ¿Cuánto tiempo llevas en España? ¿Desde cuándo vives aquí?', 'To ask: ¿Cuánto tiempo llevas en España? ¿Desde cuándo vives aquí?'),
      ], [
        SG('llevar-tiempo', 'llevar + tiempo + gerundio', ('faire quelque chose depuis… (llevar)', 'to have been doing for…')),
        SG('desde-hace', 'desde hace / hace… que', ('depuis (une durée)', 'for (a period of time)')),
        S('desde-cuando', '¿Desde cuándo…?', ('Depuis quand… ?', 'Since when…?')),
        S('cuanto-tiempo', '¿Cuánto tiempo…?', ('Combien de temps… ?', 'How long… (question)?')),
        S('el-mes', 'el mes', ('le mois', 'the month')),
        S('la-quincena', 'la quincena', ('la quinzaine', 'the fortnight')),
        S('el-siglo', 'el siglo', ('le siècle', 'the century')),
        S('mudarse', 'mudarse', ('déménager', 'to move (house)')),
      ], [
        x('Llevo veinte días caminando y todavía no me he cansado del Camino.', 'Je marche depuis vingt jours et je ne me suis pas encore lassé du Chemin.', 'I’ve been walking for twenty days and I’m still not tired of the Camino.'),
        x('El castillo de los templarios está aquí desde hace más de ocho siglos.', 'Le château des Templiers est ici depuis plus de huit siècles.', 'The Templar castle has stood here for more than eight centuries.'),
      ], [
        FB(CHOOSE, 'Llevo dos años ＿ español.', ['estudiando', 'estudiar', 'estudiado'], 'estudiando', ('Llevar + durée + gérondif.', 'Llevar + period + gerund.'), ('J’étudie l’espagnol depuis deux ans.', 'I’ve been studying Spanish for two years.')),
        FB(CHOOSE, 'Vivo en Ponferrada ＿ hace cinco años.', ['desde', 'hace', 'durante'], 'desde', ('Depuis + durée : desde hace.', 'For + period: desde hace.'), ('J’habite à Ponferrada depuis cinq ans.', 'I’ve lived in Ponferrada for five years.')),
        FB(CHOOSE, '＿ tres días que no veo a Marco.', ['Hace', 'Desde', 'Lleva'], 'Hace', ('Hace + durée + que.', 'Hace + period + que.'), ('Ça fait trois jours que je ne vois pas Marco.', 'I haven’t seen Marco for three days.')),
        DC(ANSWER, [('Guía', '¿Cuánto tiempo llevas en el Camino?')], ('La guide du château te demande depuis combien de temps tu es sur le Chemin.', 'The castle guide asks how long you’ve been on the Camino.'), ['Llevo tres semanas caminando.', 'Llevo tres semanas caminar.', 'Desde tres semanas.'], 'Llevo tres semanas caminando.', ('Llevar + durée + gérondif.', 'Llevar + period + gerund.')),
      ]),
  ]),
  CH('deleb1-w6-c2', ('Le centre de santé', 'The health centre'), [
    L('es-medico', ('Chez le médecin : la fiebre, la tos, la receta', 'At the doctor’s: la fiebre, la tos, la receta'), ('Décrire ses symptômes et comprendre les conseils du médecin.', 'Describe your symptoms and understand the doctor’s advice.'), 9, [
        ('Les symptômes : tengo fiebre (de la fièvre), tos (la toux), dolor de garganta (mal à la gorge), estoy mareado (j’ai des vertiges), me he torcido el tobillo (je me suis tordu la cheville).', 'Symptoms: tengo fiebre (a temperature), tos (a cough), dolor de garganta (a sore throat), estoy mareado (I feel dizzy), me he torcido el tobillo (I’ve twisted my ankle).'),
        ('Chez le médecin : ¿Desde cuándo le duele? Le voy a recetar… (je vais vous prescrire). La receta (l’ordonnance), las pastillas (les comprimés).', 'At the doctor’s: ¿Desde cuándo le duele? Le voy a recetar… (I’m going to prescribe you…). La receta (the prescription), las pastillas (the tablets).'),
        ('Les conseils : Tiene que hacer reposo (vous devez rester au repos). Póngase hielo. No haga deporte durante una semana.', 'Advice: Tiene que hacer reposo (you must rest). Póngase hielo (put ice on it). No haga deporte durante una semana.'),
      ], [
        S('la-fiebre', 'la fiebre', ('fièvre', 'fever')),
        S('la-tos', 'la tos', ('la toux', 'the cough')),
        S('dolor-de-garganta', 'el dolor de garganta', ('le mal de gorge', 'the sore throat')),
        S('mareado', 'mareado / mareada', ('pris·e de vertiges', 'dizzy')),
        S('torcerse', 'torcerse el tobillo', ('se tordre la cheville', 'to twist one’s ankle')),
        S('la-receta', 'la receta', ('l’ordonnance, la recette', 'the prescription, the recipe')),
        S('la-pastilla', 'la pastilla', ('le comprimé', 'the tablet, the pill')),
        S('hacer-reposo', 'hacer reposo', ('rester au repos', 'to rest (medical)')),
        S('la-rodilla', 'la rodilla', ('le genou', 'the knee')),
      ], [
        x('Me he torcido el tobillo bajando del castillo y tengo la rodilla hinchada.', 'Je me suis tordu la cheville en descendant du château et j’ai le genou enflé.', 'I twisted my ankle coming down from the castle and my knee is swollen.'),
        x('La médica me ha recetado unas pastillas y me ha dicho que haga reposo dos días.', 'La médecin m’a prescrit des comprimés et m’a dit de rester au repos deux jours.', 'The doctor has prescribed me some tablets and told me to rest for two days.'),
      ], [
        DC(ANSWER, [('Médica', '¿Qué le pasa?')], ('La médecin te demande ce qui ne va pas (tu as de la fièvre et tu tousses).', 'The doctor asks what’s wrong (you have a temperature and a cough).'), ['Tengo fiebre y mucha tos desde ayer.', 'Soy fiebre y tos.', 'Me duele la fiebre.'], 'Tengo fiebre y mucha tos desde ayer.', ('Symptômes : tengo fiebre, tengo tos.', 'Symptoms: tengo fiebre, tengo tos.')),
        FB(COMPLETE, 'Me he ＿ el tobillo en la bajada.', ['torcido', 'dolido', 'mareado'], 'torcido', ('Se tordre la cheville : torcerse el tobillo.', 'To twist one’s ankle: torcerse el tobillo.'), ('Je me suis tordu la cheville dans la descente.', 'I twisted my ankle on the way down.')),
        FB(COMPLETE, 'Con esta ＿ puede comprar las pastillas en la farmacia.', ['receta', 'tos', 'rodilla'], 'receta', ('L’ordonnance : la receta.', 'The prescription: la receta.'), ('Avec cette ordonnance, vous pouvez acheter les comprimés à la pharmacie.', 'With this prescription you can buy the tablets at the chemist’s.')),
        TF('Tiene que hacer reposo una semana.', ('Le patient peut reprendre la marche demain.', 'The patient can start walking again tomorrow.'), FAUX, ('Hacer reposo = rester au repos.', 'Hacer reposo = to rest.')),
      ]),
  ])])

# ═════════════════════════ 7 : la Galice — l'environnement, les connecteurs, la technologie ═════════════════════════
W7 = WORLD('deleb1-w7', ('Les brumes de Galice', 'The mists of Galicia'), REGION,
  ('Parler de l’environnement, organiser et nuancer ses idées avec les connecteurs (aunque, sin embargo, por eso) et se débrouiller avec le téléphone et les réseaux sociaux.', 'Talk about the environment, organise and qualify ideas with connectors (aunque, sin embargo, por eso) and get by with phones and social media.'),
  (('La Meiga du Cebreiro', 'The Meiga of O Cebreiro'), '~', ('Dans les brumes du Cebreiro, la Meiga, sorcière des légendes galiciennes, prépare sa queimada et jette des sorts aux pèlerins distraits. « Las meigas, haberlas, haylas », dit le proverbe. Elle respecte ceux qui savent argumenter et relier leurs idées.', 'In the mists of O Cebreiro, the Meiga, the witch of Galician legend, brews her queimada and casts spells on absent-minded pilgrims. “Witches? There are some, there are,” says the proverb. She respects those who can argue and link their ideas.')),
  [CH('deleb1-w7-c1', ('La montée du Cebreiro', 'The climb to O Cebreiro'), [
    L('es-medio-ambiente', ('L’environnement : reciclar, ahorrar, proteger', 'The environment: reciclar, ahorrar, proteger'), ('Parler des problèmes de l’environnement et des gestes pour le protéger.', 'Talk about environmental problems and what we can do to protect it.'), 9, [
        ('Les problèmes : la contaminación (la pollution), el cambio climático, la sequía (la sécheresse), los incendios (les incendies de forêt).', 'The problems: la contaminación (pollution), el cambio climático (climate change), la sequía (drought), los incendios (forest fires).'),
        ('Les gestes : reciclar, ahorrar agua y energía (économiser), no tirar basura al suelo (ne pas jeter de déchets par terre), proteger la naturaleza, reducir los residuos.', 'What we can do: reciclar, ahorrar agua y energía (save water and energy), no tirar basura al suelo (not drop litter), proteger la naturaleza, reducir los residuos (reduce waste).'),
        ('Pour argumenter : Hay que + infinitif ; deberíamos + infinitif ; es fundamental que + subjonctif : Es fundamental que cuidemos los bosques.', 'To argue: Hay que + infinitive; deberíamos + infinitive; es fundamental que + subjunctive: Es fundamental que cuidemos los bosques.'),
      ], [
        S('el-medio-ambiente', 'el medio ambiente', ('l’environnement', 'the environment')),
        S('la-contaminacion', 'la contaminación', ('pollution', 'pollution')),
        S('el-cambio-climatico', 'el cambio climático', ('le changement climatique', 'climate change')),
        S('reciclar', 'reciclar', ('recycler', 'to recycle')),
        S('ahorrar', 'ahorrar', ('économiser', 'to save (money, energy)')),
        S('los-residuos', 'los residuos', ('les déchets', 'waste, rubbish')),
        S('el-incendio', 'el incendio', ('l’incendie', 'the fire (blaze)')),
        S('la-sequia', 'la sequía', ('sécheresse', 'drought')),
        S('proteger', 'proteger', ('protéger', 'to protect')),
      ], [
        x('En el Camino hay que llevarse los residuos y no tirar nada al suelo.', 'Sur le Chemin, il faut emporter ses déchets et ne rien jeter par terre.', 'On the Camino you have to take your rubbish with you and not throw anything on the ground.'),
        x('Cada verano hay incendios en Galicia por la sequía y el cambio climático.', 'Chaque été, il y a des incendies en Galice à cause de la sécheresse et du changement climatique.', 'Every summer there are fires in Galicia because of drought and climate change.'),
      ], [
        FB(COMPLETE, 'Para ＿ agua, me ducho en tres minutos.', ['ahorrar', 'reciclar', 'contaminar'], 'ahorrar', ('Économiser : ahorrar.', 'To save: ahorrar.'), ('Pour économiser l’eau, je me douche en trois minutes.', 'To save water, I take three-minute showers.')),
        FB(CHOOSE, 'Es fundamental que ＿ los bosques.', ['protejamos', 'protegemos', 'protegeremos'], 'protejamos', ('Es fundamental que + subjonctif (proteger → protejamos).', 'Es fundamental que + subjunctive (proteger → protejamos).'), ('Il est essentiel que nous protégions les forêts.', 'It’s essential that we protect the forests.')),
        TF('Los incendios aumentan con la sequía.', ('La sécheresse augmente le risque d’incendie.', 'Drought increases the risk of fire.'), VRAI, ('Aumentar = augmenter.', 'Aumentar = to increase.')),
        DC(ANSWER, [('Meiga', '¿Qué haces tú para cuidar el medio ambiente?')], ('La Meiga te demande ce que tu fais pour l’environnement.', 'The Meiga asks what you do for the environment.'), ['Reciclo, ahorro agua y voy a pie siempre que puedo.', 'Contamino mucho y reciclo nada.', 'Soy medio ambiente.'], 'Reciclo, ahorro agua y voy a pie siempre que puedo.', ('On cite ses gestes au présent.', 'You list what you do in the present.')),
      ]),
    L('es-conectores', ('Cependant, c’est pourquoi : les connecteurs', 'However, that’s why: connectors'), ('Organiser ses idées et nuancer avec les connecteurs.', 'Organise and qualify your ideas with connectors.'), 9, [
        ('Ajouter : además (de plus), también, incluso (même). Opposer : pero, sin embargo (cependant), en cambio (en revanche), aunque (même si, bien que).', 'Adding: además (besides), también, incluso (even). Contrasting: pero, sin embargo (however), en cambio (on the other hand), aunque (although).'),
        ('La conséquence : por eso (c’est pourquoi), así que (donc, alors), por lo tanto (par conséquent).', 'Consequence: por eso (that’s why), así que (so), por lo tanto (therefore).'),
        ('Organiser : en primer lugar, por un lado… por otro (lado), por último, en resumen.', 'Organising: en primer lugar, por un lado… por otro (lado), por último, en resumen.'),
      ], [
        S('ademas', 'además', ('de plus, en outre', 'besides, moreover')),
        S('sin-embargo', 'sin embargo', ('cependant, toutefois', 'however')),
        S('en-cambio', 'en cambio', ('en revanche', 'on the other hand, whereas')),
        S('aunque', 'aunque', ('bien que, même si', 'although, even though')),
        S('por-eso', 'por eso', ('c’est pourquoi', 'that’s why')),
        S('asi-que', 'así que', ('donc, alors', 'so (consequence)')),
        S('por-un-lado', 'por un lado… por otro', ('d’un côté… de l’autre', 'on the one hand… on the other')),
        S('por-ultimo', 'por último', ('enfin, pour finir', 'finally, lastly')),
      ], [
        x('Aunque llovía mucho, subimos al Cebreiro; sin embargo, no vimos nada por la niebla.', 'Même s’il pleuvait beaucoup, nous sommes montés au Cebreiro ; cependant, nous n’avons rien vu à cause du brouillard.', 'Although it was pouring, we climbed up to O Cebreiro; however, we saw nothing because of the fog.'),
        x('Por un lado, el Camino es duro; por otro, es una experiencia única. Por eso lo recomiendo.', 'D’un côté, le Chemin est dur ; de l’autre, c’est une expérience unique. C’est pourquoi je le recommande.', 'On the one hand the Camino is hard; on the other, it’s a unique experience. That’s why I recommend it.'),
      ], [
        FB(CHOOSE, 'Estaba cansada; ＿, siguió caminando.', ['sin embargo', 'por eso', 'además'], 'sin embargo', ('Opposition : sin embargo.', 'Contrast: sin embargo.'), ('Elle était fatiguée ; cependant, elle a continué à marcher.', 'She was tired; however, she kept on walking.')),
        FB(CHOOSE, 'Llovía mucho, ＿ nos quedamos en el albergue.', ['así que', 'aunque', 'en cambio'], 'así que', ('Conséquence : así que.', 'Consequence: así que.'), ('Il pleuvait beaucoup, alors nous sommes restés au gîte.', 'It was pouring, so we stayed in the hostel.')),
        FB(CHOOSE, '＿ hace frío, me encanta Galicia.', ['Aunque', 'Por eso', 'Así que'], 'Aunque', ('Concession : aunque.', 'Concession: aunque.'), ('Même s’il fait froid, j’adore la Galice.', 'Even though it’s cold, I love Galicia.')),
        FB(CHOOSE, 'Mi hermano es muy deportista; yo, ＿, prefiero leer.', ['en cambio', 'además', 'así que'], 'en cambio', ('Contraste entre deux personnes : en cambio.', 'Contrast between two people: en cambio.'), ('Mon frère est très sportif ; moi, en revanche, je préfère lire.', 'My brother is very sporty; I, on the other hand, prefer reading.')),
      ]),
  ]),
  CH('deleb1-w7-c2', ('Pas de réseau dans la brume', 'No signal in the mist'), [
    L('es-tecnologia', ('Le portable et les réseaux : descargar, subir una foto', 'Phones and social media: descargar, subir una foto'), ('Parler de son téléphone, des applications et des réseaux sociaux.', 'Talk about your phone, apps and social media.'), 9, [
        ('Le téléphone : el móvil, la aplicación (l’appli), descargar (télécharger), la contraseña (le mot de passe), la batería, cargar el móvil (le recharger).', 'The phone: el móvil, la aplicación (the app), descargar (to download), la contraseña (the password), la batería, cargar el móvil (to charge it).'),
        ('Les réseaux : las redes sociales, subir una foto (publier), compartir, el seguidor (l’abonné), dar a «me gusta».', 'Social media: las redes sociales, subir una foto (to post a photo), compartir, el seguidor (the follower), dar a «me gusta» (to like).'),
        ('Les problèmes : No tengo cobertura (je n’ai pas de réseau), se me ha acabado la batería, no funciona la conexión.', 'Problems: No tengo cobertura (I have no signal), se me ha acabado la batería (my battery has died), no funciona la conexión.'),
      ], [
        S('el-movil', 'el móvil', ('le portable (téléphone)', 'the mobile phone')),
        S('la-aplicacion', 'la aplicación', ('l’application', 'the app')),
        S('descargar', 'descargar', ('télécharger', 'to download')),
        S('la-contrasena', 'la contraseña', ('le mot de passe', 'the password')),
        S('las-redes-sociales', 'las redes sociales', ('les réseaux sociaux', 'social media')),
        S('subir-una-foto', 'subir una foto', ('publier une photo', 'to post a photo')),
        S('la-cobertura', 'la cobertura', ('le réseau (téléphone)', 'signal, coverage')),
        S('cargar', 'cargar el móvil', ('recharger son portable', 'to charge one’s phone')),
        S('la-bateria', 'la batería', ('la batterie', 'the battery')),
      ], [
        x('En O Cebreiro no había cobertura, así que no pude subir las fotos a las redes.', 'À O Cebreiro, il n’y avait pas de réseau, donc je n’ai pas pu publier les photos sur les réseaux.', 'In O Cebreiro there was no signal, so I couldn’t post the photos on social media.'),
        x('¿Cuál es la contraseña del wifi? — Está escrita en la puerta.', 'Quel est le mot de passe du wifi ? — Il est écrit sur la porte.', 'What’s the wifi password? — It’s written on the door.'),
      ], [
        FB(COMPLETE, 'Me he quedado sin ＿: ¿tienes un cargador?', ['batería', 'contraseña', 'cobertura'], 'batería', ('Sans batterie : sin batería.', 'Out of battery: sin batería.'), ('Je n’ai plus de batterie : tu as un chargeur ?', 'My battery’s dead: have you got a charger?')),
        FB(COMPLETE, 'Para entrar en la red necesitas la ＿.', ['contraseña', 'batería', 'aplicación'], 'contraseña', ('Le mot de passe : la contraseña.', 'The password: la contraseña.'), ('Pour te connecter au réseau, il te faut le mot de passe.', 'To log on to the network you need the password.')),
        DC(ANSWER, [('Peregrina', '¿Me puedes enviar las fotos?')], ('Une pèlerine te demande de lui envoyer les photos ; tu n’as pas de réseau.', 'A pilgrim asks you to send her the photos; you have no signal.'), ['Claro, te las envío en cuanto tenga cobertura.', 'Claro, te las envío en cuanto tengo cobertura mañana.', 'Claro, se los envié ayer.'], 'Claro, te las envío en cuanto tenga cobertura.', ('Futur : en cuanto + subjonctif.', 'Future: en cuanto + subjunctive.')),
        TF('No tengo cobertura.', ('Le téléphone n’a pas de réseau.', 'The phone has no signal.'), VRAI, ('Cobertura = réseau.', 'Cobertura = signal.')),
      ]),
  ])])

# ═════════════════════════ 8 : Saint-Jacques et Fisterra — les conditions, la lettre formelle ═════════════════════════
W8 = WORLD('deleb1-w8', ('Saint-Jacques et la fin du monde', 'Santiago and the end of the world'), REGION,
  ('Poser des conditions (si + présent), imaginer et faire des hypothèses (si tuviera…, iría…) et écrire une lettre formelle.', 'Set conditions (si + present), imagine and make hypotheses (si tuviera…, iría…) and write a formal letter.'),
  (('L’Urco de Fisterra', 'The Urco of Fisterra'), '€', ('Sur la côte de la Mort, l’Urco, grand chien noir aux cornes de taureau des légendes galiciennes, sort des vagues les nuits de tempête. Pour l’apaiser, imagine ce qui arriverait si…, puis écris-lui une lettre en bonne et due forme.', 'On the Coast of Death, the Urco, the great black dog with bull’s horns of Galician legend, rises from the waves on stormy nights. To calm it, imagine what would happen if…, then write it a proper formal letter.')),
  [CH('deleb1-w8-c1', ('Sur la côte de la Mort', 'On the Coast of Death'), [
    L('es-si-real', ('S’il fait beau, nous irons au phare : si + présent', 'If it’s sunny, we’ll go to the lighthouse: si + present'), ('Exprimer une condition réelle avec si + présent.', 'Express a real condition with si + present.'), 9, [
        ('Si + présent, puis présent, futur ou impératif : Si llueve, nos quedamos. Si llegas pronto, te esperaré. Si te duele, para.', 'Si + present, then present, future or imperative: Si llueve, nos quedamos. Si llegas pronto, te esperaré. Si te duele, para.'),
        ('Jamais de futur ni de subjonctif présent après si : Si mañana hace sol… (et non hará).', 'Never use the future or the present subjunctive after si: Si mañana hace sol… (not hará).'),
        ('Por si = au cas où : Llévate un chubasquero por si llueve. En caso de + nom : en caso de tormenta.', 'Por si = in case: Llévate un chubasquero por si llueve. En caso de + noun: en caso de tormenta (in case of a storm).'),
      ], [
        SG('si-presente', 'si + presente', ('si + présent (condition réelle)', 'if + present (real condition)')),
        S('por-si', 'por si…', ('au cas où…', 'in case…')),
        S('el-chubasquero', 'el chubasquero', ('le coupe-vent, l’imperméable', 'the raincoat')),
        S('en-caso-de', 'en caso de', ('en cas de', 'in case of')),
        S('la-tormenta', 'la tormenta', ('l’orage, la tempête', 'the storm')),
        S('el-faro', 'el faro', ('le phare', 'the lighthouse')),
        S('el-acantilado', 'el acantilado', ('la falaise', 'the cliff')),
        S('la-ola', 'la ola', ('la vague', 'the wave')),
      ], [
        x('Si mañana hace buen tiempo, iremos andando hasta el faro de Fisterra.', 'S’il fait beau demain, nous irons à pied jusqu’au phare de Fisterra.', 'If the weather is good tomorrow, we’ll walk to the Fisterra lighthouse.'),
        x('Llévate el chubasquero por si hay tormenta en la costa.', 'Prends ton imperméable au cas où il y aurait un orage sur la côte.', 'Take your raincoat in case there’s a storm on the coast.'),
      ], [
        FB(CHOOSE, 'Si ＿ tiempo, visitaremos el faro.', ['tenemos', 'tendremos', 'tengamos'], 'tenemos', ('Si + présent.', 'Si + present.'), ('Si nous avons le temps, nous visiterons le phare.', 'If we have time, we’ll visit the lighthouse.')),
        FB(CHOOSE, 'Si estás cansado, ＿ un poco.', ['descansa', 'descansarías', 'descanses'], 'descansa', ('Si + présent, puis impératif.', 'Si + present, then imperative.'), ('Si tu es fatigué, repose-toi un peu.', 'If you’re tired, have a rest.')),
        FB(CHOOSE, 'Lleva agua ＿ no hay fuentes.', ['por si', 'si no', 'aunque'], 'por si', ('Au cas où : por si.', 'In case: por si.'), ('Emporte de l’eau au cas où il n’y aurait pas de fontaines.', 'Take water in case there are no fountains.')),
        TF('Si llueve, no iremos a la playa.', ('Ils iront à la plage même s’il pleut.', 'They will go to the beach even if it rains.'), FAUX, ('S’il pleut, ils n’iront pas.', 'If it rains, they won’t go.')),
      ]),
    L('es-si-irreal', ('Si j’avais le temps… : l’hypothèse', 'If I had time…: hypotheses'), ('Imaginer une situation avec si + imparfait du subjonctif et le conditionnel.', 'Imagine a situation with si + past subjunctive and the conditional.'), 10, [
        ('Pour imaginer : si + imparfait du subjonctif, puis conditionnel : Si tuviera tiempo, haría el Camino otra vez (si j’avais le temps, je referais le Chemin).', 'To imagine: si + past subjunctive, then conditional: Si tuviera tiempo, haría el Camino otra vez (if I had time, I’d walk the Camino again).'),
        ('Formation : 3e personne du pluriel du passé simple, -ron → -ra : hablaron → hablara, tuvieron → tuviera, fueron → fuera, pudieron → pudiera, hicieron → hiciera.', 'Formation: 3rd person plural of the simple past, -ron → -ra: hablaron → hablara, tuvieron → tuviera, fueron → fuera, pudieron → pudiera, hicieron → hiciera.'),
        ('Pour conseiller : Si yo fuera tú… (si j’étais toi). Pour rêver : Si pudiera, viviría junto al mar.', 'To give advice: Si yo fuera tú… (if I were you). To dream: Si pudiera, viviría junto al mar.'),
      ], [
        SG('si-imperfecto', 'si + imperfecto de subjuntivo', ('si + imparfait (hypothèse)', 'if + past subjunctive (hypothesis)')),
        SG('imperfecto-subj', 'hablara / tuviera / fuera', ('(que) je parlasse / j’eusse / je fusse (subjonctif imparfait)', 'that I spoke / had / were (past subjunctive)')),
        S('si-yo-fuera-tu', 'si yo fuera tú', ('si j’étais toi', 'if I were you')),
        S('si-pudiera', 'si pudiera…', ('si je pouvais…', 'if I could…')),
        S('sonar-con', 'soñar con', ('rêver de', 'to dream of')),
        S('el-sueno', 'el sueño', ('le rêve, le sommeil', 'the dream, sleep')),
        S('la-loteria', 'la lotería', ('la loterie', 'the lottery')),
        S('jubilarse', 'jubilarse', ('prendre sa retraite', 'to retire')),
      ], [
        x('Si tuviera un mes libre, volvería a hacer el Camino desde el principio.', 'Si j’avais un mois de libre, je referais le Chemin depuis le début.', 'If I had a month off, I’d walk the Camino again from the beginning.'),
        x('Si me tocara la lotería, me compraría una casa cerca del faro.', 'Si je gagnais à la loterie, je m’achèterais une maison près du phare.', 'If I won the lottery, I’d buy a house near the lighthouse.'),
      ], [
        FB(CHOOSE, 'Si ＿ dinero, viajaría por toda América.', ['tuviera', 'tengo', 'tendría'], 'tuviera', ('Hypothèse : si + imparfait du subjonctif.', 'Hypothesis: si + past subjunctive.'), ('Si j’avais de l’argent, je voyagerais dans toute l’Amérique.', 'If I had money, I’d travel all over the Americas.')),
        FB(CHOOSE, 'Si yo fuera tú, ＿ al médico.', ['iría', 'iré', 'vaya'], 'iría', ('Conséquence imaginée : conditionnel.', 'Imagined result: conditional.'), ('Si j’étais toi, j’irais chez le médecin.', 'If I were you, I’d go to the doctor.')),
        FB(CHOOSE, 'Si ＿ más despacio, te entendería mejor.', ['hablaras', 'hablas', 'hablarías'], 'hablaras', ('Si + imparfait du subjonctif : hablaron → hablaras.', 'Si + past subjunctive: hablaron → hablaras.'), ('Si tu parlais plus lentement, je te comprendrais mieux.', 'If you spoke more slowly, I’d understand you better.')),
        DC(ANSWER, [('Urco', '¿Qué harías si pudieras vivir en cualquier lugar?')], ('L’Urco te demande ce que tu ferais si tu pouvais vivre n’importe où.', 'The Urco asks what you would do if you could live anywhere.'), ['Si pudiera, viviría junto al mar, en Galicia.', 'Si puedo, vivo junto al mar.', 'Si pudiera, viviré junto al mar.'], 'Si pudiera, viviría junto al mar, en Galicia.', ('Si + imparfait du subjonctif, puis conditionnel.', 'Si + past subjunctive, then conditional.')),
      ]),
  ]),
  CH('deleb1-w8-c2', ('Au bureau du pèlerin', 'At the Pilgrim’s Office'), [
    L('es-carta-formal', ('Madame, Monsieur : la lettre formelle', 'Dear Sir or Madam: the formal letter'), ('Écrire une lettre ou un courriel formel : saluer, présenter l’objet, demander, conclure.', 'Write a formal letter or email: greet, state the purpose, ask, close.'), 9, [
        ('Commencer : Estimado señor / Estimada señora: (avec deux-points). Présenter l’objet : Le escribo para… / Me pongo en contacto con ustedes para…', 'Opening: Estimado señor / Estimada señora: (with a colon). Stating the purpose: Le escribo para… / Me pongo en contacto con ustedes para…'),
        ('Demander poliment : Le agradecería que + imparfait du subjonctif (je vous serais reconnaissant de…). Adjunto… (je joins…). Quedo a la espera de su respuesta (dans l’attente de votre réponse).', 'Asking politely: Le agradecería que + past subjunctive (I would be grateful if you…). Adjunto… (I attach…). Quedo a la espera de su respuesta (I look forward to your reply).'),
        ('Finir : Atentamente ou Un cordial saludo, puis la signature. On vouvoie avec usted du début à la fin.', 'Closing: Atentamente or Un cordial saludo, then your signature. Use usted from start to finish.'),
      ], [
        S('estimado', 'Estimado señor / Estimada señora:', ('Monsieur, / Madame, (en-tête de lettre)', 'Dear Sir / Dear Madam')),
        S('le-escribo-para', 'le escribo para…', ('je vous écris pour…', 'I am writing to…')),
        S('le-agradeceria', 'le agradecería que…', ('je vous serais reconnaissant de…', 'I would be grateful if you…')),
        S('quedo-a-la-espera', 'quedo a la espera de su respuesta', ('dans l’attente de votre réponse', 'I look forward to your reply')),
        S('atentamente', 'atentamente', ('salutations distinguées', 'yours faithfully, yours sincerely')),
        S('la-reclamacion', 'la reclamación', ('la réclamation', 'the complaint')),
        S('el-certificado', 'el certificado', ('le certificat', 'the certificate')),
        S('adjuntar', 'adjuntar', ('joindre (un document)', 'to attach (a document)')),
      ], [
        x('Estimada señora: le escribo para pedir información sobre la Compostela. Quedo a la espera de su respuesta. Atentamente, Paul Martin.', 'Madame, je vous écris pour demander des informations sur la Compostela. Dans l’attente de votre réponse, veuillez agréer mes salutations distinguées. Paul Martin.', 'Dear Madam, I am writing to ask for information about the Compostela. I look forward to your reply. Yours faithfully, Paul Martin.'),
        x('Le agradecería que me enviaran el certificado por correo. Adjunto una copia de mi credencial.', 'Je vous serais reconnaissant de m’envoyer le certificat par courrier. Je joins une copie de ma crédentiale.', 'I would be grateful if you could send me the certificate by post. I attach a copy of my pilgrim passport.'),
      ], [
        FB(COMPLETE, '＿ señor: le escribo para hacer una reclamación.', ['Estimado', 'Hola', 'Un beso'], 'Estimado', ('Lettre formelle : Estimado señor.', 'Formal letter: Estimado señor.'), ('Monsieur, je vous écris pour faire une réclamation.', 'Dear Sir, I am writing to make a complaint.')),
        FB(COMPLETE, 'Quedo a la ＿ de su respuesta.', ['espera', 'esperanza', 'reclamación'], 'espera', ('Formule : quedo a la espera de…', 'Set phrase: quedo a la espera de…'), ('Dans l’attente de votre réponse.', 'I look forward to your reply.')),
        FB(COMPLETE, 'Le ＿ que me devolvieran el dinero.', ['agradecería', 'agradecí', 'agradezca'], 'agradecería', ('Demande polie : le agradecería que…', 'Polite request: le agradecería que…'), ('Je vous serais reconnaissant de me rembourser.', 'I would be grateful if you could refund me.')),
        TF('Atentamente, María López.', ('C’est une formule pour finir une lettre familière.', 'It’s a way to end an informal letter.'), FAUX, ('Atentamente termine une lettre formelle.', 'Atentamente ends a formal letter.')),
      ]),
  ])])

write_level('DELEB1', ('DELE B1 : le chemin de Saint-Jacques', 'DELE B1: the Way of St James'), REGION, 'The Way of St James', 54,
  [W1, W2, W3, W4, W5, W6, W7, W8, FINAL('DELEB1', REGION, ('Simulation DELE B1 : la cathédrale de Saint-Jacques', 'DELE B1 simulation: Santiago cathedral'), 'compréhension écrite, compréhension auditive et expression écrite (l’oral n’est pas évalué)', 'reading comprehension, listening comprehension and written expression (speaking is not assessed)')])

