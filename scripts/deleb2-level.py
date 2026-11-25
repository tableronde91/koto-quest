# Niveau DELE B2 (espagnol, CECRL B2) : 8 étapes à travers les Amériques, leçons et examen blanc (français + anglais).
# Mode histoire : la traversée de l'Atlantique, des Canaries au Río de la Plata (voir gen-story.py).
# Les gardiens portent les voyelles à tilde du guaraní (ã, ẽ, ĩ, õ, ũ, ỹ), langue officielle du Paraguay.
# Les notions sont en espagnol (front) avec leur sens en français ; la traduction anglaise du sens sert à l'interface en anglais.
# Usage : python3 scripts/deleb2-level.py   (réécrit content/deleb2/deleb2.json ; les DELE A1 à B1 doivent déjà exister)
from es_common import *

REGION = 'Traversée des Amériques'

# ═════════════════════════ 1 : les Canaries — ser et estar, devenir, le caractère ═════════════════════════
W1 = WORLD('deleb2-w1', ('Les volcans des Canaries', 'The volcanoes of the Canaries'), REGION,
  ('Maîtriser ser et estar quand le sens change (ser listo / estar listo), exprimer les changements (ponerse, volverse, hacerse, quedarse) et décrire le caractère avec nuance.', 'Master ser and estar when the meaning changes (ser listo / estar listo), express change (ponerse, volverse, hacerse, quedarse) and describe personality with nuance.'),
  (('Guayota du Teide', 'Guayota of Mount Teide'), 'ã', ('Selon les Guanches, premiers habitants des Canaries, Guayota, démon des volcans, avait un jour enfermé le soleil dans le Teide. Il a de nouveau assombri le ciel de Tenerife : décris avec précision les gens et leurs changements, et il rendra la lumière.', 'According to the Guanches, the first inhabitants of the Canaries, Guayota, the demon of the volcanoes, once locked the sun inside Mount Teide. He has darkened the sky over Tenerife again: describe people and how they change with precision, and he will give back the light.')),
  [CH('deleb2-w1-c1', ('Au pied du Teide', 'At the foot of Mount Teide'), [
    L('es-ser-estar-b2', ('Être prêt ou être intelligent ? ser et estar', 'Ready or clever? ser and estar'), ('Choisir ser ou estar quand un adjectif change de sens, et employer estar de et ser pour les événements.', 'Choose ser or estar when an adjective changes meaning, and use estar de and ser for events.'), 10, [
        ('Certains adjectifs changent de sens : ser listo (être intelligent) / estar listo (être prêt) ; ser rico (riche) / estar rico (délicieux) ; ser aburrido (ennuyeux) / estar aburrido (s’ennuyer) ; ser malo (méchant) / estar malo (malade).', 'Some adjectives change meaning: ser listo (to be clever) / estar listo (to be ready); ser rico (rich) / estar rico (delicious); ser aburrido (boring) / estar aburrido (bored); ser malo (bad) / estar malo (ill).'),
        ('Estar de + nom ou activité : estar de vacaciones, de viaje, de buen / mal humor, de camarero (travailler provisoirement comme serveur).', 'Estar de + noun or activity: estar de vacaciones, de viaje, de buen / mal humor, de camarero (working temporarily as a waiter).'),
        ('Pour dire où a lieu un événement, on emploie ser : La fiesta es en la playa. El concierto fue en el auditorio.', 'To say where an event takes place, use ser: La fiesta es en la playa. El concierto fue en el auditorio.'),
      ], [
        SG('ser-estar-sentido', 'ser listo / estar listo', ('être intelligent / être prêt', 'to be clever / to be ready')),
        S('ser-aburrido', 'ser aburrido / estar aburrido', ('être ennuyeux / s’ennuyer', 'to be boring / to be bored')),
        S('estar-malo', 'ser malo / estar malo', ('être méchant / être malade', 'to be bad / to be ill')),
        S('estar-de-vacaciones', 'estar de vacaciones', ('être en vacances', 'to be on holiday')),
        S('estar-de-mal-humor', 'estar de mal humor', ('être de mauvaise humeur', 'to be in a bad mood')),
        S('el-volcan', 'el volcán', ('le volcan', 'the volcano')),
        S('el-archipielago', 'el archipiélago', ('l’archipel', 'the archipelago')),
        S('la-lava', 'la lava', ('la lave', 'lava')),
      ], [
        x('Mi primo es muy listo, pero nunca está listo a tiempo.', 'Mon cousin est très intelligent, mais il n’est jamais prêt à l’heure.', 'My cousin is very clever, but he’s never ready on time.'),
        x('La fiesta es en la playa de Las Teresitas, y todos estamos de buen humor.', 'La fête a lieu sur la plage de Las Teresitas, et nous sommes tous de bonne humeur.', 'The party is on Las Teresitas beach, and we’re all in a good mood.'),
      ], [
        FB(CHOOSE, 'Esta paella ＿ riquísima.', ['está', 'es', 'hay'], 'está', ('Estar rico = être délicieux.', 'Estar rico = to be delicious.'), ('Cette paella est délicieuse.', 'This paella is delicious.')),
        FB(CHOOSE, 'El concierto ＿ en el auditorio de Tenerife.', ['es', 'está', 'hay'], 'es', ('Un événement a lieu : ser.', 'An event takes place: ser.'), ('Le concert a lieu à l’auditorium de Tenerife.', 'The concert is at the Tenerife auditorium.')),
        FB(CHOOSE, 'Mi abuelo ＿ malo: tiene gripe.', ['está', 'es', 'tiene'], 'está', ('Estar malo = être malade.', 'Estar malo = to be ill.'), ('Mon grand-père est malade : il a la grippe.', 'My grandfather is ill: he has flu.')),
        TF('Este libro es muy aburrido.', ('Le livre est ennuyeux.', 'The book is boring.'), VRAI, ('Ser aburrido = être ennuyeux.', 'Ser aburrido = to be boring.')),
      ]),
    L('es-verbos-cambio', ('Devenir : ponerse, volverse, hacerse, quedarse', 'Becoming: ponerse, volverse, hacerse, quedarse'), ('Choisir le bon verbe pour exprimer un changement.', 'Choose the right verb to express a change.'), 10, [
        ('Ponerse + adjectif = changement passager : ponerse nervioso, rojo, triste. Quedarse = le résultat d’un événement : quedarse sordo, sin trabajo, solo, sin palabras.', 'Ponerse + adjective = temporary change: ponerse nervioso, rojo, triste. Quedarse = the result of an event: quedarse sordo, sin trabajo, solo, sin palabras.'),
        ('Volverse = changement profond, souvent négatif : volverse loco, egoísta, desconfiado. Hacerse = changement par l’effort ou la volonté : hacerse rico, famoso, médico, vegetariano.', 'Volverse = deep, often negative change: volverse loco, egoísta, desconfiado. Hacerse = change through effort or choice: hacerse rico, famoso, médico, vegetariano.'),
        ('Llegar a ser = finir par devenir, après un long chemin : Llegó a ser alcaldesa. Convertirse en + nom : El pueblo se convirtió en una ciudad.', 'Llegar a ser = to go on to become, after a long road: Llegó a ser alcaldesa. Convertirse en + noun: El pueblo se convirtió en una ciudad.'),
      ], [
        SG('ponerse', 'ponerse + adjetivo', ('devenir (changement passager)', 'to become (temporary change)')),
        SG('volverse', 'volverse + adjetivo', ('devenir (changement profond)', 'to become (deep change)')),
        SG('hacerse', 'hacerse + adjetivo / nombre', ('devenir (par la volonté)', 'to become (through effort)')),
        S('quedarse-cambio', 'quedarse + adjetivo', ('se retrouver (résultat d’un événement)', 'to end up (result of an event)')),
        S('llegar-a-ser', 'llegar a ser', ('finir par devenir', 'to go on to become')),
        S('convertirse', 'convertirse en', ('se transformer en', 'to turn into')),
        S('ponerse-rojo', 'ponerse rojo', ('rougir', 'to blush')),
        S('volverse-loco', 'volverse loco', ('devenir fou', 'to go mad')),
      ], [
        x('Cuando vio la erupción, se puso muy nerviosa y se quedó sin palabras.', 'Quand elle a vu l’éruption, elle est devenue très nerveuse et est restée sans voix.', 'When she saw the eruption, she got very nervous and was left speechless.'),
        x('Empezó vendiendo plátanos en el mercado y llegó a ser el empresario más rico de la isla.', 'Il a commencé en vendant des bananes au marché et il a fini par devenir l’entrepreneur le plus riche de l’île.', 'He started out selling bananas at the market and went on to become the richest businessman on the island.'),
      ], [
        FB(CHOOSE, 'Cuando habla en público, se ＿ muy nervioso.', ['pone', 'vuelve', 'hace'], 'pone', ('Changement passager : ponerse.', 'Temporary change: ponerse.'), ('Quand il parle en public, il devient très nerveux.', 'When he speaks in public, he gets very nervous.')),
        FB(CHOOSE, 'Después de años de estudio, se ＿ médica.', ['hizo', 'puso', 'quedó'], 'hizo', ('Par l’effort : hacerse.', 'Through effort: hacerse.'), ('Après des années d’études, elle est devenue médecin.', 'After years of study, she became a doctor.')),
        FB(CHOOSE, 'Con tanto trabajo, me voy a ＿ loco.', ['volver', 'poner', 'hacer'], 'volver', ('Volverse loco = devenir fou.', 'Volverse loco = to go mad.'), ('Avec tout ce travail, je vais devenir fou.', 'With all this work, I’m going to go mad.')),
        FB(CHOOSE, 'Cerraron la fábrica y muchos se ＿ sin trabajo.', ['quedaron', 'pusieron', 'hicieron'], 'quedaron', ('Résultat d’un événement : quedarse.', 'Result of an event: quedarse.'), ('L’usine a fermé et beaucoup se sont retrouvés sans travail.', 'The factory closed and many people were left without work.')),
      ]),
  ]),
  CH('deleb2-w1-c2', ('Les gens de l’île', 'The island’s people'), [
    L('es-caracter', ('Le caractère : orgulloso, terco, generoso', 'Personality: orgulloso, terco, generoso'), ('Décrire les qualités et les défauts de quelqu’un avec nuance.', 'Describe someone’s qualities and faults with nuance.'), 9, [
        ('Qualités : generoso, sincero, sensato (raisonnable), comprensivo (compréhensif), trabajador, valiente.', 'Qualities: generoso, sincero, sensato (sensible), comprensivo (understanding), trabajador, valiente.'),
        ('Défauts : orgulloso (fier, orgueilleux), terco ou cabezota (têtu), tacaño (radin), celoso (jaloux), vago (paresseux), mentiroso (menteur).', 'Faults: orgulloso (proud), terco or cabezota (stubborn), tacaño (stingy), celoso (jealous), vago (lazy), mentiroso (liar).'),
        ('Nuancer : un poco, bastante, demasiado ; tener buen / mal carácter ; ser de los que… (faire partie de ceux qui…).', 'Qualifying: un poco, bastante, demasiado; tener buen / mal carácter; ser de los que… (to be one of those who…).'),
      ], [
        S('orgulloso', 'orgulloso / orgullosa', ('fier, orgueilleux', 'proud')),
        S('terco', 'terco / terca', ('têtu / têtue', 'stubborn')),
        S('tacano', 'tacaño / tacaña', ('radin, mesquin', 'stingy')),
        S('celoso', 'celoso / celosa', ('jaloux / jalouse', 'jealous')),
        S('vago', 'vago / vaga', ('paresseux / paresseuse', 'lazy')),
        S('sensato', 'sensato / sensata', ('raisonnable, sensé', 'sensible')),
        S('comprensivo', 'comprensivo / comprensiva', ('compréhensif / compréhensive', 'understanding (kind)')),
        S('tener-buen-caracter', 'tener buen carácter', ('avoir bon caractère', 'to be good-natured')),
      ], [
        x('Mi abuela es generosa y comprensiva, pero un poco terca cuando discute de política.', 'Ma grand-mère est généreuse et compréhensive, mais un peu têtue quand elle parle politique.', 'My grandmother is generous and understanding, but a bit stubborn when she argues about politics.'),
        x('No seas tan orgulloso: pídele perdón.', 'Ne sois pas si orgueilleux : demande-lui pardon.', 'Don’t be so proud: say sorry to her.'),
      ], [
        FB(COMPLETE, 'Nunca invita a nadie y cuenta cada céntimo: es muy ＿.', ['tacaño', 'generoso', 'sensato'], 'tacaño', ('Radin : tacaño.', 'Stingy: tacaño.'), ('Il n’invite jamais personne et compte chaque centime : il est très radin.', 'He never invites anyone and counts every cent: he’s very stingy.')),
        FB(COMPLETE, 'No cambia de opinión aunque se equivoque: es muy ＿.', ['terco', 'comprensivo', 'vago'], 'terco', ('Têtu : terco.', 'Stubborn: terco.'), ('Il ne change pas d’avis même quand il se trompe : il est très têtu.', 'He never changes his mind even when he’s wrong: he’s very stubborn.')),
        DC(ANSWER, [('Guayota', '¿Cómo es tu mejor amigo?')], ('Guayota te demande comment est ton meilleur ami.', 'Guayota asks what your best friend is like.'), ['Es sincero y trabajador, aunque a veces es un poco celoso.', 'Está sincero y trabajador.', 'Tiene sincero.'], 'Es sincero y trabajador, aunque a veces es un poco celoso.', ('Caractère : ser + adjectif.', 'Personality: ser + adjective.')),
        TF('Es una persona muy sensata.', ('Elle prend des décisions raisonnables.', 'She makes sensible decisions.'), VRAI, ('Sensato = raisonnable.', 'Sensato = sensible.')),
      ]),
  ])])

# ═════════════════════════ 2 : La Havane — l'imparfait du subjonctif, la concordance, como si ═════════════════════════
W2 = WORLD('deleb2-w2', ('Les rythmes de La Havane', 'The rhythms of Havana'), REGION,
  ('Employer l’imparfait du subjonctif (quería que vinieras), respecter la concordance des temps et comparer avec como si.', 'Use the past subjunctive (quería que vinieras), follow the sequence of tenses and compare with como si.'),
  (('La Ciguapa aux pieds inversés', 'The backward-footed Ciguapa'), 'ẽ', ('Dans les montagnes des Caraïbes, la Ciguapa, femme sauvage aux longs cheveux et aux pieds tournés vers l’arrière, égare ceux qui suivent ses traces. Elle s’est glissée dans les bals de La Havane : raconte ce qu’on voulait que tu fasses, et ne te laisse pas tromper.', 'In the mountains of the Caribbean, the Ciguapa, a wild woman with long hair and backward-facing feet, leads astray anyone who follows her footprints. She has slipped into the dance halls of Havana: say what people wanted you to do, and don’t let yourself be fooled.')),
  [CH('deleb2-w2-c1', ('Le bal de La Havane', 'The Havana dance hall'), [
    L('es-imperfecto-subjuntivo', ('Il voulait que je danse : l’imparfait du subjonctif', 'He wanted me to dance: the past subjunctive'), ('Former et employer l’imparfait du subjonctif.', 'Form and use the past subjunctive.'), 10, [
        ('Formation : 3e personne du pluriel du passé simple, -ron → -ra ou -se : hablaron → hablara / hablase ; tuvieron → tuviera / tuviese. Les deux formes sont équivalentes ; -ra est la plus courante.', 'Formation: 3rd person plural of the simple past, -ron → -ra or -se: hablaron → hablara / hablase; tuvieron → tuviera / tuviese. Both forms are equivalent; -ra is the most common.'),
        ('Il remplace le subjonctif présent quand le verbe principal est au passé : Quiero que vengas → Quería que vinieras.', 'It replaces the present subjunctive when the main verb is in the past: Quiero que vengas → Quería que vinieras.'),
        ('Irréguliers fréquents : fuera (ser, ir), estuviera, hiciera, dijera, pudiera, supiera, quisiera, viniera, diera, trajera.', 'Common irregulars: fuera (ser, ir), estuviera, hiciera, dijera, pudiera, supiera, quisiera, viniera, diera, trajera.'),
      ], [
        SG('imperf-subj-ra-se', 'hablara / hablase', ('(que) je parlasse : deux formes', 'that I spoke: two forms')),
        SG('quisiera', 'quisiera / pudiera / supiera', ('(que) je voulusse / pusse / susse', 'that I wanted / could / knew')),
        S('dijera', 'dijera / trajera', ('(que) je disse / j’apportasse', 'that I said / brought')),
        S('el-son-cubano', 'el son cubano', ('le son (musique cubaine)', 'Cuban son (music)')),
        S('bailar-salsa', 'bailar salsa', ('danser la salsa', 'to dance salsa')),
        S('el-malecon', 'el malecón', ('le front de mer', 'the seafront promenade')),
        S('el-ritmo', 'el ritmo', ('le rythme', 'the rhythm')),
        S('la-orquesta', 'la orquesta', ('l’orchestre', 'the orchestra, the band')),
      ], [
        x('Mi abuela quería que aprendiera a bailar son antes de ir a La Habana.', 'Ma grand-mère voulait que j’apprenne à danser le son avant d’aller à La Havane.', 'My grandmother wanted me to learn to dance son before going to Havana.'),
        x('El guía nos pidió que no camináramos solos por el malecón de noche.', 'Le guide nous a demandé de ne pas marcher seuls sur le front de mer la nuit.', 'The guide asked us not to walk alone along the seafront at night.'),
      ], [
        FB(CHOOSE, 'Quería que ＿ conmigo al concierto.', ['vinieras', 'vengas', 'vendrías'], 'vinieras', ('Verbe principal au passé : imparfait du subjonctif.', 'Main verb in the past: past subjunctive.'), ('Je voulais que tu viennes avec moi au concert.', 'I wanted you to come to the concert with me.')),
        FB(CHOOSE, 'Les pedí que ＿ más despacio.', ['hablaran', 'hablen', 'hablaban'], 'hablaran', ('Pedí (passé) que + imparfait du subjonctif.', 'Pedí (past) que + past subjunctive.'), ('Je leur ai demandé de parler plus lentement.', 'I asked them to speak more slowly.')),
        FB(CHOOSE, 'No creía que ＿ tan difícil.', ['fuera', 'sea', 'era'], 'fuera', ('No creía que + imparfait du subjonctif.', 'No creía que + past subjunctive.'), ('Je ne croyais pas que ce soit si difficile.', 'I didn’t think it would be so hard.')),
        FB(CHOOSE, 'Ojalá ＿ bailar como tú, pero soy muy torpe.', ['supiera', 'sé', 'sabré'], 'supiera', ('Souhait irréel : ojalá + imparfait du subjonctif.', 'Unreal wish: ojalá + past subjunctive.'), ('Si seulement je savais danser comme toi, mais je suis très maladroit.', 'If only I could dance like you, but I’m so clumsy.')),
      ]),
    L('es-concordancia', ('La concordance des temps', 'The sequence of tenses'), ('Choisir le subjonctif présent ou imparfait selon le verbe principal.', 'Choose the present or past subjunctive depending on the main verb.'), 10, [
        ('Présent, futur ou impératif → subjonctif présent : Te pido que vengas. Le diré que llame.', 'Present, future or imperative → present subjunctive: Te pido que vengas. Le diré que llame.'),
        ('Passé (passé simple, imparfait, plus-que-parfait) ou conditionnel → imparfait du subjonctif : Te pedí que vinieras. Me gustaría que vinieras.', 'Past (simple past, imperfect, past perfect) or conditional → past subjunctive: Te pedí que vinieras. Me gustaría que vinieras.'),
        ('Avec me gustaría, preferiría, sería mejor : toujours l’imparfait du subjonctif : Sería mejor que salierais temprano.', 'With me gustaría, preferiría, sería mejor: always the past subjunctive: Sería mejor que salierais temprano.'),
      ], [
        SG('concordancia-tiempos', 'quiero que vengas / quería que vinieras', ('la concordance des temps', 'the sequence of tenses')),
        S('me-gustaria-que', 'me gustaría que…', ('j’aimerais que…', 'I’d like (someone) to…')),
        S('preferiria-que', 'preferiría que…', ('je préférerais que…', 'I’d rather (someone)…')),
        S('seria-mejor-que', 'sería mejor que…', ('il vaudrait mieux que…', 'it would be better if…')),
        S('el-puro', 'el puro', ('le cigare', 'the cigar')),
        S('la-plantacion', 'la plantación', ('la plantation', 'the plantation')),
        S('la-cana-de-azucar', 'la caña de azúcar', ('la canne à sucre', 'sugar cane')),
        S('colonial', 'colonial', ('colonial, de l’époque coloniale', 'colonial')),
      ], [
        x('Me gustaría que visitarais el barrio colonial de Trinidad.', 'J’aimerais que vous visitiez le quartier colonial de Trinidad.', 'I’d like you to visit the colonial quarter of Trinidad.'),
        x('El guía nos dijo que era mejor que compráramos los puros en la fábrica.', 'Le guide nous a dit qu’il valait mieux acheter les cigares à la fabrique.', 'The guide told us it was better to buy the cigars at the factory.'),
      ], [
        FB(CHOOSE, 'Me gustaría que ＿ a mi boda.', ['vinieras', 'vengas', 'vienes'], 'vinieras', ('Me gustaría que + imparfait du subjonctif.', 'Me gustaría que + past subjunctive.'), ('J’aimerais que tu viennes à mon mariage.', 'I’d like you to come to my wedding.')),
        FB(CHOOSE, 'Le diré que te ＿ mañana.', ['llame', 'llamara', 'llamaría'], 'llame', ('Futur → subjonctif présent.', 'Future → present subjunctive.'), ('Je lui dirai de t’appeler demain.', 'I’ll tell him to call you tomorrow.')),
        FB(CHOOSE, 'Sería mejor que ＿ antes del calor.', ['saliéramos', 'salgamos', 'salimos'], 'saliéramos', ('Sería mejor que + imparfait du subjonctif.', 'Sería mejor que + past subjunctive.'), ('Il vaudrait mieux que nous partions avant la chaleur.', 'It would be better if we left before the heat.')),
        TF('Mi madre me pidió que la llamara.', ('La mère a demandé qu’on l’appelle.', 'The mother asked to be called.'), VRAI, ('Pidió que la llamara = elle a demandé que je l’appelle.', 'Pidió que la llamara = she asked me to call her.')),
      ]),
  ]),
  CH('deleb2-w2-c2', ('Les traces inversées', 'The backward footprints'), [
    L('es-como-si', ('Comme s’il était cubain : como si', 'As if he were Cuban: como si'), ('Faire une comparaison imaginaire avec como si et protester avec ni que.', 'Make an imaginary comparison with como si and protest with ni que.'), 9, [
        ('Como si + imparfait du subjonctif : Habla como si fuera cubano (il parle comme s’il était cubain).', 'Como si + past subjunctive: Habla como si fuera cubano (he talks as if he were Cuban).'),
        ('Pour une action antérieure : como si + plus-que-parfait du subjonctif : Me miró como si no me hubiera visto nunca.', 'For an earlier action: como si + past perfect subjunctive: Me miró como si no me hubiera visto nunca.'),
        ('¡Ni que + imparfait du subjonctif! pour protester : ¡Ni que fuera mi madre! (comme si c’était ma mère !). Hacer como si = faire comme si.', '¡Ni que + past subjunctive! to protest: ¡Ni que fuera mi madre! (anyone would think she was my mother!). Hacer como si = to act as if.'),
      ], [
        SG('como-si', 'como si + imperfecto de subjuntivo', ('comme si + imparfait', 'as if + past subjunctive')),
        S('ni-que', '¡Ni que…!', ('Comme si… ! (protestation)', 'Anyone would think…!')),
        S('hacer-como-si', 'hacer como si', ('faire comme si', 'to act as if')),
        S('el-acento', 'el acento', ('l’accent', 'the accent')),
        S('presumir', 'presumir', ('se vanter', 'to show off')),
        S('disimular', 'disimular', ('faire semblant, dissimuler', 'to pretend, to hide (feelings)')),
        S('el-disfraz', 'el disfraz', ('le déguisement', 'the costume, the disguise')),
        S('enganar', 'engañar', ('tromper, duper', 'to deceive')),
      ], [
        x('Baila como si hubiera nacido en La Habana.', 'Il danse comme s’il était né à La Havane.', 'He dances as if he had been born in Havana.'),
        x('Hizo como si no me conociera. ¡Ni que le hubiera hecho algo malo!', 'Il a fait comme s’il ne me connaissait pas. Comme si je lui avais fait quelque chose de mal !', 'He acted as if he didn’t know me. Anyone would think I’d done something bad to him!'),
      ], [
        FB(CHOOSE, 'Habla español como si ＿ cubana.', ['fuera', 'es', 'sea'], 'fuera', ('Como si + imparfait du subjonctif.', 'Como si + past subjunctive.'), ('Elle parle espagnol comme si elle était cubaine.', 'She speaks Spanish as if she were Cuban.')),
        FB(CHOOSE, 'Me miró como si no me ＿ nunca.', ['hubiera visto', 'ha visto', 'había visto'], 'hubiera visto', ('Action antérieure : como si + plus-que-parfait du subjonctif.', 'Earlier action: como si + past perfect subjunctive.'), ('Il m’a regardé comme s’il ne m’avait jamais vu.', 'He looked at me as if he had never seen me.')),
        FB(CHOOSE, 'Hace como si no ＿ nada.', ['supiera', 'sabe', 'sepa'], 'supiera', ('Hacer como si + imparfait du subjonctif.', 'Hacer como si + past subjunctive.'), ('Il fait comme s’il ne savait rien.', 'He acts as if he knew nothing.')),
        TF('¡Ni que fuera mi jefe!', ('La personne accepte volontiers l’ordre.', 'The person happily accepts the order.'), FAUX, ('¡Ni que…! exprime l’agacement.', '¡Ni que…! expresses irritation.')),
      ]),
  ])])

# ═════════════════════════ 3 : Mexico — la concession, l'espagnol du Mexique ═════════════════════════
W3 = WORLD('deleb2-w3', ('Les marchés de Mexico', 'The markets of Mexico City'), REGION,
  ('Exprimer la concession (aunque + indicatif ou subjonctif, a pesar de, por mucho que) et découvrir l’espagnol du Mexique (¿mande?, ahorita, ustedes).', 'Express concession (aunque + indicative or subjunctive, a pesar de, por mucho que) and discover Mexican Spanish (¿mande?, ahorita, ustedes).'),
  (('Le Nahual masqué', 'The masked Nahual'), 'ĩ', ('Au marché de la Merced, un Nahual, sorcier des légendes mésoaméricaines capable de se changer en jaguar ou en coyote, se cache parmi les marchands. Il ne cède qu’à ceux qui savent concéder sans se contredire… et qui comprennent l’espagnol du Mexique.', 'At La Merced market, a Nahual, a sorcerer of Mesoamerican legend who can turn into a jaguar or a coyote, is hiding among the stallholders. He only gives way to those who can concede without contradicting themselves… and who understand Mexican Spanish.')),
  [CH('deleb2-w3-c1', ('Au marché de la Merced', 'At La Merced market'), [
    L('es-aunque-subjuntivo', ('Bien que, même si : aunque', 'Although, even if: aunque'), ('Choisir l’indicatif ou le subjonctif après aunque.', 'Choose the indicative or the subjunctive after aunque.'), 10, [
        ('Aunque + indicatif : un fait réel et connu (bien que) : Aunque llueve, voy a salir (il pleut, et je sors quand même).', 'Aunque + indicative: a real, known fact (although): Aunque llueve, voy a salir (it’s raining, and I’m going out anyway).'),
        ('Aunque + subjonctif : une hypothèse, ou un fait dont on ne tient pas compte (même si) : Aunque llueva, saldré (même s’il pleut).', 'Aunque + subjunctive: a hypothesis, or a fact you disregard (even if): Aunque llueva, saldré (even if it rains).'),
        ('Aunque + imparfait du subjonctif : une hypothèse irréelle : Aunque tuviera dinero, no lo compraría.', 'Aunque + past subjunctive: an unreal hypothesis: Aunque tuviera dinero, no lo compraría.'),
      ], [
        SG('aunque-indicativo', 'aunque + indicativo', ('bien que (fait réel)', 'although (real fact)')),
        SG('aunque-subjuntivo', 'aunque + subjuntivo', ('même si (hypothèse)', 'even if (hypothesis)')),
        S('aun-asi', 'aun así', ('malgré tout, quand même', 'even so')),
        S('de-todas-formas', 'de todas formas', ('de toute façon', 'anyway')),
        S('el-puesto-mercado', 'el puesto del mercado', ('l’étal (du marché)', 'the market stall')),
        S('picante', 'picante', ('piquant, épicé', 'spicy, hot')),
        S('el-chile', 'el chile', ('le piment', 'the chilli')),
        S('la-tortilla-de-maiz', 'la tortilla de maíz', ('la galette de maïs', 'the corn tortilla')),
      ], [
        x('Aunque el mole es picante, me encanta.', 'Bien que le mole soit épicé, je l’adore.', 'Although mole is spicy, I love it.'),
        x('Aunque me pagaras, no comería ese chile: ¡es demasiado picante!', 'Même si tu me payais, je ne mangerais pas ce piment : il est bien trop fort !', 'Even if you paid me, I wouldn’t eat that chilli: it’s far too hot!'),
      ], [
        FB(CHOOSE, 'Aunque mañana ＿, iremos a Teotihuacán.', ['llueva', 'llovió', 'lloverá'], 'llueva', ('Hypothèse : aunque + subjonctif.', 'Hypothesis: aunque + subjunctive.'), ('Même s’il pleut demain, nous irons à Teotihuacán.', 'Even if it rains tomorrow, we’ll go to Teotihuacán.')),
        FB(CHOOSE, 'Aunque ＿ muy cansado, ayer salí a cenar.', ['estaba', 'esté', 'estuviera'], 'estaba', ('Fait réel passé : aunque + indicatif.', 'Real past fact: aunque + indicative.'), ('Bien que je fusse très fatigué, je suis sorti dîner hier.', 'Although I was very tired, I went out for dinner yesterday.')),
        FB(CHOOSE, 'Aunque ＿ millonario, seguiría trabajando.', ['fuera', 'soy', 'sea'], 'fuera', ('Hypothèse irréelle : imparfait du subjonctif.', 'Unreal hypothesis: past subjunctive.'), ('Même si j’étais millionnaire, je continuerais à travailler.', 'Even if I were a millionaire, I would keep working.')),
        TF('Aunque haga frío, iremos a la playa.', ('Il fait certainement froid en ce moment.', 'It is definitely cold right now.'), FAUX, ('Aunque + subjonctif : on ne sait pas s’il fera froid.', 'Aunque + subjunctive: we don’t know if it will be cold.')),
      ]),
    L('es-concesivas', ('Malgré, avoir beau : a pesar de, por mucho que', 'Despite, however much: a pesar de, por mucho que'), ('Exprimer l’obstacle et la concession avec d’autres tournures.', 'Express obstacles and concession with other structures.'), 10, [
        ('A pesar de + nom ou infinitif : A pesar del tráfico, llegamos a tiempo. A pesar de que + indicatif pour un fait réel.', 'A pesar de + noun or infinitive: A pesar del tráfico, llegamos a tiempo. A pesar de que + indicative for a real fact.'),
        ('Por mucho que / por más que + subjonctif = avoir beau… : Por mucho que estudie, no lo entiende. Por muy + adjectif + que : Por muy caro que sea, lo compraré.', 'Por mucho que / por más que + subjunctive = however much…: Por mucho que estudie, no lo entiende. Por muy + adjective + que: Por muy caro que sea, lo compraré.'),
        ('Registre soutenu : si bien (bien que), no obstante. Familier : aun así (malgré tout), de todas formas (de toute façon).', 'Formal register: si bien (although), no obstante. Informal: aun así (even so), de todas formas (anyway).'),
      ], [
        SG('a-pesar-de', 'a pesar de / a pesar de que', ('malgré / bien que', 'despite / even though')),
        SG('por-mucho-que', 'por mucho que + subjuntivo', ('avoir beau… (por mucho que)', 'however much…')),
        S('por-muy-que', 'por muy… que', ('si… que (concession)', 'however… (adjective)')),
        S('si-bien', 'si bien', ('bien que (soutenu)', 'although (formal)')),
        S('el-trafico', 'el tráfico', ('la circulation', 'traffic')),
        S('el-atasco', 'el atasco', ('l’embouteillage', 'the traffic jam')),
        S('la-capital', 'la capital', ('la capitale', 'the capital (city)')),
        S('el-metro', 'el metro', ('le métro', 'the underground, the subway')),
      ], [
        x('A pesar del tráfico, la Ciudad de México es una capital fascinante.', 'Malgré la circulation, Mexico est une capitale fascinante.', 'Despite the traffic, Mexico City is a fascinating capital.'),
        x('Por mucho que le explique el camino, siempre se pierde en el metro.', 'J’ai beau lui expliquer le chemin, il se perd toujours dans le métro.', 'However much I explain the way, he always gets lost on the metro.'),
      ], [
        FB(CHOOSE, '＿ la lluvia, el mercado estaba lleno.', ['A pesar de', 'Aunque', 'Por mucho que'], 'A pesar de', ('Devant un nom : a pesar de.', 'Before a noun: a pesar de.'), ('Malgré la pluie, le marché était plein.', 'Despite the rain, the market was full.')),
        FB(CHOOSE, 'Por mucho que lo ＿, no consigo dormir.', ['intente', 'intento', 'intentaré'], 'intente', ('Por mucho que + subjonctif.', 'Por mucho que + subjunctive.'), ('J’ai beau essayer, je n’arrive pas à dormir.', 'However hard I try, I can’t sleep.')),
        FB(CHOOSE, 'Por muy caro que ＿, lo compraré.', ['sea', 'es', 'será'], 'sea', ('Por muy… que + subjonctif.', 'Por muy… que + subjunctive.'), ('Aussi cher qu’il soit, je l’achèterai.', 'However expensive it is, I’ll buy it.')),
        DC(ANSWER, [('Nahual', 'La ciudad es enorme y hay mucho ruido. ¿Te gusta?')], ('Le Nahual te demande si la ville te plaît malgré le bruit.', 'The Nahual asks if you like the city despite the noise.'), ['Sí, a pesar del ruido, me encanta.', 'Sí, a pesar de que el ruido me encante.', 'Sí, por mucho que me gusta.'], 'Sí, a pesar del ruido, me encanta.', ('A pesar de + nom.', 'A pesar de + noun.')),
      ]),
  ]),
  CH('deleb2-w3-c2', ('L’espagnol du Mexique', 'Mexican Spanish'), [
    L('es-mexico', ('¿Mande?, ahorita, ¡qué padre! : l’espagnol du Mexique', '¿Mande?, ahorita, ¡qué padre!: Mexican Spanish'), ('Comprendre les tournures et le vocabulaire de l’espagnol du Mexique.', 'Understand the expressions and vocabulary of Mexican Spanish.'), 9, [
        ('Formules mexicaines : ¿Mande? (pardon ? — pour faire répéter, poli), ahorita (tout de suite… ou plus tard !), ¡Qué padre! (génial !), ¡Órale! (d’accord ! allez !).', 'Mexican phrases: ¿Mande? (pardon? — to ask someone to repeat, polite), ahorita (right now… or later!), ¡Qué padre! (cool!), ¡Órale! (OK! come on!).'),
        ('Vocabulaire d’Amérique latine : el carro (la voiture ; el coche en Espagne), el celular (le portable ; el móvil en Espagne), la chamba (le boulot, familier au Mexique).', 'Latin American vocabulary: el carro (the car; el coche in Spain), el celular (the mobile; el móvil in Spain), la chamba (the job, informal in Mexico).'),
        ('Dans toute l’Amérique, ustedes remplace vosotros, même entre amis : ¿Ustedes quieren venir?', 'Throughout the Americas, ustedes replaces vosotros, even among friends: ¿Ustedes quieren venir?'),
      ], [
        S('mande', '¿Mande?', ('Pardon ? (Mexique)', 'Pardon? (Mexico)')),
        S('ahorita', 'ahorita', ('tout de suite, dans un moment (Mexique)', 'right away, in a bit (Mexico)')),
        S('que-padre', '¡Qué padre!', ('Génial ! (Mexique)', 'Cool! (Mexico)')),
        S('orale', '¡Órale!', ('D’accord ! Allez ! (Mexique)', 'OK! Come on! (Mexico)')),
        S('el-carro', 'el carro', ('la voiture (Amérique latine)', 'the car (Latin America)')),
        S('el-celular', 'el celular', ('le portable (Amérique latine)', 'the mobile phone (Latin America)')),
        S('la-chamba', 'la chamba', ('le boulot (Mexique, familier)', 'the job (Mexico, informal)')),
        S('ustedes-america', 'ustedes (en América)', ('vous (pluriel, en Amérique)', 'you all (plural, in the Americas)')),
      ], [
        x('¿Mande? — Le pregunto si ustedes ya tienen carro para ir a Puebla.', 'Pardon ? — Je vous demande si vous avez déjà une voiture pour aller à Puebla.', 'Pardon? — I’m asking whether you already have a car to go to Puebla.'),
        x('Ahorita vengo, voy a buscar mi celular. — ¡Órale!', 'Je reviens tout de suite, je vais chercher mon portable. — D’accord !', 'I’ll be right back, I’m getting my phone. — OK!'),
      ], [
        DC(ANSWER, [('Vendedora', '¿Qué va a llevar, joven?')], ('La vendeuse parle très vite et tu n’as pas compris.', 'The stallholder speaks very fast and you didn’t understand.'), ['¿Mande?', '¡Órale!', '¡Qué padre!'], '¿Mande?', ('Faire répéter poliment au Mexique : ¿Mande?', 'Asking someone to repeat politely in Mexico: ¿Mande?')),
        FB(COMPLETE, 'En México no se dice «el coche», sino «el ＿».', ['carro', 'celular', 'metro'], 'carro', ('La voiture : el carro.', 'The car: el carro.'), ('Au Mexique, on ne dit pas « el coche », mais « el carro ».', 'In Mexico you don’t say “el coche”, but “el carro”.')),
        FB(CHOOSE, 'En México, a un grupo de amigos se le dice: «¿＿ quieren venir?»', ['Ustedes', 'Vosotros', 'Vos'], 'Ustedes', ('En Amérique : ustedes.', 'In the Americas: ustedes.'), ('Au Mexique, à un groupe d’amis on dit : « Vous voulez venir ? »', 'In Mexico you say to a group of friends: “Do you all want to come?”')),
        TF('¡Qué padre!', ('La personne trouve la chose géniale.', 'The person thinks it’s great.'), VRAI, ('¡Qué padre! = génial !', '¡Qué padre! = cool!')),
      ]),
  ])])

# ═════════════════════════ 4 : Antigua — les conditions, la précaution, le patrimoine ═════════════════════════
W4 = WORLD('deleb2-w4', ('Les volcans d’Antigua', 'The volcanoes of Antigua'), REGION,
  ('Poser des conditions (siempre que, a no ser que, con tal de que), prévoir l’imprévu (en caso de que, por si acaso) et parler du patrimoine et de l’histoire.', 'Set conditions (siempre que, a no ser que, con tal de que), plan for the unexpected (en caso de que, por si acaso) and talk about heritage and history.'),
  (('Le Sombrerón', 'The Sombrerón'), 'õ', ('À Antigua, le Sombrerón, petit homme au chapeau géant des légendes guatémaltèques, tresse la crinière des chevaux et chante des sérénades sous les balcons. Il propose des marchés pleins de conditions : apprends à poser les tiennes avant qu’il ne t’embobine.', 'In Antigua, the Sombrerón, the little man with a giant hat from Guatemalan legend, braids horses’ manes and sings serenades under balconies. He offers deals full of conditions: learn to set your own before he tricks you.')),
  [CH('deleb2-w4-c1', ('Le marché d’Antigua', 'Antigua market'), [
    L('es-condicionales-b2', ('À condition que, à moins que : siempre que, a no ser que', 'As long as, unless: siempre que, a no ser que'), ('Poser des conditions avec les conjonctions suivies du subjonctif.', 'Set conditions with conjunctions followed by the subjunctive.'), 10, [
        ('Siempre que + subjonctif = à condition que : Te lo presto siempre que me lo devuelvas. Con tal de que (pourvu que), a condición de que (soutenu).', 'Siempre que + subjunctive = as long as: Te lo presto siempre que me lo devuelvas. Con tal de que (so long as), a condición de que (formal).'),
        ('A no ser que / a menos que + subjonctif = à moins que : Iremos a pie, a no ser que llueva.', 'A no ser que / a menos que + subjunctive = unless: Iremos a pie, a no ser que llueva.'),
        ('De + infinitif passé = si (soutenu) : De haberlo sabido, no habría venido. Como + subjonctif = si jamais (menace) : Como llegues tarde, me enfado.', 'De + perfect infinitive = if (formal): De haberlo sabido, no habría venido. Como + subjunctive = if (warning): Como llegues tarde, me enfado.'),
      ], [
        SG('siempre-que', 'siempre que + subjuntivo', ('à condition que', 'as long as, provided that')),
        SG('a-no-ser-que', 'a no ser que / a menos que', ('à moins que, sauf si', 'unless')),
        S('con-tal-de-que', 'con tal de que', ('pourvu que', 'so long as')),
        S('como-amenaza', 'como + subjuntivo (amenaza)', ('si jamais… (menace)', 'if… (warning)')),
        S('el-trato', 'el trato', ('le marché, l’accord', 'the deal')),
        S('regatear', 'regatear', ('marchander', 'to haggle')),
        S('la-artesania', 'la artesanía', ('l’artisanat', 'handicrafts')),
        S('el-tejido', 'el tejido', ('le tissu, le tissage', 'fabric, weaving')),
      ], [
        x('Te hago un buen precio siempre que me compres dos tejidos.', 'Je te fais un bon prix à condition que tu m’achètes deux tissus.', 'I’ll give you a good price as long as you buy two pieces of fabric.'),
        x('Subiremos al volcán mañana, a no ser que haya mucha niebla.', 'Nous monterons sur le volcan demain, à moins qu’il y ait beaucoup de brouillard.', 'We’ll climb the volcano tomorrow, unless it’s very foggy.'),
      ], [
        FB(CHOOSE, 'Puedes venir siempre que no ＿ ruido.', ['hagas', 'haces', 'harás'], 'hagas', ('Siempre que + subjonctif.', 'Siempre que + subjunctive.'), ('Tu peux venir à condition de ne pas faire de bruit.', 'You can come as long as you don’t make any noise.')),
        FB(CHOOSE, 'Iremos al lago, a no ser que ＿ mal tiempo.', ['haga', 'hace', 'hará'], 'haga', ('A no ser que + subjonctif.', 'A no ser que + subjunctive.'), ('Nous irons au lac, à moins qu’il fasse mauvais.', 'We’ll go to the lake unless the weather is bad.')),
        FB(CHOOSE, 'Como ＿ tarde otra vez, me voy sin ti.', ['llegues', 'llegas', 'llegarás'], 'llegues', ('Menace : como + subjonctif.', 'Warning: como + subjunctive.'), ('Si jamais tu arrives encore en retard, je pars sans toi.', 'If you’re late again, I’m leaving without you.')),
        DC(ANSWER, [('Sombrerón', 'Te presto mi caballo… pero me lo traes mañana.')], ('Le Sombrerón te prête son cheval ; tu acceptes en posant ta condition.', 'The Sombrerón lends you his horse; you accept on your own terms.'), ['De acuerdo, siempre que no le trences la crin.', 'De acuerdo, siempre que no le trenzas la crin.', 'De acuerdo, a no ser que le trenzarás la crin.'], 'De acuerdo, siempre que no le trences la crin.', ('Siempre que + subjonctif.', 'Siempre que + subjunctive.')),
      ]),
    L('es-en-caso-de-que', ('Au cas où : en caso de que, por si acaso', 'In case: en caso de que, por si acaso'), ('Prévoir l’imprévu et donner des consignes de sécurité.', 'Plan for the unexpected and give safety instructions.'), 9, [
        ('En caso de que + subjonctif = au cas où : En caso de que no funcione, llame a este número. En caso de + nom : en caso de emergencia.', 'En caso de que + subjunctive = in case: En caso de que no funcione, llame a este número. En caso de + noun: en caso de emergencia.'),
        ('Por si (acaso) + indicatif = au cas où : Lleva paraguas por si acaso. Por si llueve.', 'Por si (acaso) + indicative = just in case: Lleva paraguas por si acaso. Por si llueve.'),
        ('Prévoir : prevenir (anticiper), el imprevisto (l’imprévu), el seguro de viaje (l’assurance voyage), la salida de emergencia (la sortie de secours).', 'Planning ahead: prevenir (to forestall), el imprevisto (the unexpected), el seguro de viaje (travel insurance), la salida de emergencia (the emergency exit).'),
      ], [
        SG('en-caso-de-que', 'en caso de que + subjuntivo', ('au cas où + conditionnel', 'in case + clause')),
        S('por-si-acaso', 'por si acaso', ('au cas où, par précaution', 'just in case')),
        S('la-emergencia', 'la emergencia', ('l’urgence', 'the emergency')),
        S('el-imprevisto', 'el imprevisto', ('l’imprévu', 'the unexpected event')),
        S('el-seguro-de-viaje', 'el seguro de viaje', ('l’assurance voyage', 'travel insurance')),
        S('el-terremoto', 'el terremoto', ('le tremblement de terre', 'the earthquake')),
        S('la-salida-de-emergencia', 'la salida de emergencia', ('la sortie de secours', 'the emergency exit')),
        S('prevenir', 'prevenir', ('prévenir, anticiper', 'to prevent, to forestall')),
      ], [
        x('En caso de que haya un terremoto, salga por la salida de emergencia.', 'En cas de tremblement de terre, sortez par la sortie de secours.', 'In the event of an earthquake, leave by the emergency exit.'),
        x('Llévate el seguro de viaje por si acaso.', 'Emporte ton assurance voyage, au cas où.', 'Take your travel insurance just in case.'),
      ], [
        FB(CHOOSE, 'En caso de que ＿ problemas, llámame.', ['tengas', 'tienes', 'tendrás'], 'tengas', ('En caso de que + subjonctif.', 'En caso de que + subjunctive.'), ('Au cas où tu aurais des problèmes, appelle-moi.', 'Call me in case you have any problems.')),
        FB(CHOOSE, 'Llevo dinero extra ＿.', ['por si acaso', 'en caso de que', 'a no ser que'], 'por si acaso', ('En fin de phrase : por si acaso.', 'At the end of a sentence: por si acaso.'), ('J’emporte de l’argent en plus, au cas où.', 'I’m taking extra money just in case.')),
        FB(COMPLETE, 'En caso de ＿, llame al 112.', ['emergencia', 'seguro', 'salida'], 'emergencia', ('En cas d’urgence : en caso de emergencia.', 'In an emergency: en caso de emergencia.'), ('En cas d’urgence, appelez le 112.', 'In an emergency, call 112.')),
        TF('En caso de que llueva, la excursión se cancela.', ('L’excursion est déjà annulée.', 'The trip is already cancelled.'), FAUX, ('Elle ne sera annulée que s’il pleut.', 'It will only be cancelled if it rains.')),
      ]),
  ]),
  CH('deleb2-w4-c2', ('Les ruines de Tikal', 'The ruins of Tikal'), [
    L('es-patrimonio', ('Le patrimoine : las ruinas, el yacimiento', 'Heritage: las ruinas, el yacimiento'), ('Parler du patrimoine et situer des faits historiques.', 'Talk about heritage and place historical events in time.'), 9, [
        ('Le patrimoine : el patrimonio (de la humanidad), las ruinas, el yacimiento arqueológico (le site archéologique), la pirámide, el templo, la civilización maya.', 'Heritage: el patrimonio (de la humanidad), las ruinas, el yacimiento arqueológico (the archaeological site), la pirámide, el templo, la civilización maya.'),
        ('Situer dans le temps : en el siglo X, a lo largo de (tout au long de), a principios / a mediados / a finales de (au début / au milieu / à la fin de).', 'Placing in time: en el siglo X, a lo largo de (throughout), a principios / a mediados / a finales de (at the beginning / in the middle / at the end of).'),
        ('Les verbes de l’histoire : fundar (fonder), construir, conquistar, desaparecer, descubrir (découvrir). Au passif : La ciudad fue fundada en 1543.', 'History verbs: fundar (to found), construir, conquistar, desaparecer, descubrir (to discover). In the passive: La ciudad fue fundada en 1543.'),
      ], [
        S('el-patrimonio', 'el patrimonio', ('le patrimoine', 'heritage')),
        S('las-ruinas', 'las ruinas', ('les ruines', 'the ruins')),
        S('el-yacimiento', 'el yacimiento', ('le site (archéologique)', 'the (archaeological) site')),
        S('la-piramide', 'la pirámide', ('la pyramide', 'the pyramid')),
        S('la-civilizacion', 'la civilización', ('la civilisation', 'civilisation')),
        S('fundar', 'fundar', ('fonder', 'to found')),
        S('descubrir', 'descubrir', ('découvrir', 'to discover')),
        S('a-finales-de', 'a principios de / a finales de', ('au début de / à la fin de', 'at the beginning of / at the end of')),
      ], [
        x('Tikal fue una de las ciudades más importantes de la civilización maya y hoy es patrimonio de la humanidad.', 'Tikal fut l’une des villes les plus importantes de la civilisation maya et elle est aujourd’hui patrimoine de l’humanité.', 'Tikal was one of the most important cities of the Maya civilisation and is now a World Heritage Site.'),
        x('Antigua fue fundada a mediados del siglo XVI y destruida por un terremoto en 1773.', 'Antigua fut fondée au milieu du XVIe siècle et détruite par un tremblement de terre en 1773.', 'Antigua was founded in the mid-sixteenth century and destroyed by an earthquake in 1773.'),
      ], [
        FB(COMPLETE, 'Los arqueólogos trabajan en un ＿ maya.', ['yacimiento', 'patrimonio', 'siglo'], 'yacimiento', ('Le site archéologique : el yacimiento.', 'The archaeological site: el yacimiento.'), ('Les archéologues travaillent sur un site maya.', 'The archaeologists are working at a Maya site.')),
        FB(CHOOSE, 'La ciudad fue ＿ en el siglo XVI.', ['fundada', 'fundado', 'fundó'], 'fundada', ('Passif : ser + participe accordé (la ciudad → fundada).', 'Passive: ser + agreeing participle (la ciudad → fundada).'), ('La ville fut fondée au XVIe siècle.', 'The city was founded in the sixteenth century.')),
        FB(CHOOSE, 'Las ruinas fueron ＿ por un campesino.', ['descubiertas', 'descubiertos', 'descubrieron'], 'descubiertas', ('Participe irrégulier accordé : descubiertas.', 'Irregular agreeing participle: descubiertas.'), ('Les ruines furent découvertes par un paysan.', 'The ruins were discovered by a farmer.')),
        TF('El templo se construyó a finales del siglo VIII.', ('Le temple date de la fin du VIIIe siècle.', 'The temple dates from the end of the eighth century.'), VRAI, ('A finales de = à la fin de.', 'A finales de = at the end of.')),
      ]),
  ])])

# ═════════════════════════ 5 : le Magdalena — le conditionnel passé, l'irréel du passé, les regrets ═════════════════════════
W5 = WORLD('deleb2-w5', ('Le fleuve Magdalena', 'The Magdalena river'), REGION,
  ('Exprimer ce qui aurait pu se passer (habría hecho), faire des hypothèses sur le passé (si hubiera sabido…) et dire ses regrets et ses reproches.', 'Say what could have happened (habría hecho), make hypotheses about the past (si hubiera sabido…) and express regrets and reproaches.'),
  (('Le Mohán du fleuve', 'The Mohán of the river'), 'ũ', ('Sur les rives du Magdalena, le Mohán, vieux sorcier barbu des légendes colombiennes, fume sa pipe dans une grotte sous les rapides et fait chavirer les barques des imprudents. Il adore les regrets : dis-lui ce que tu aurais fait autrement… et ce qui se serait passé.', 'On the banks of the Magdalena, the Mohán, the old bearded sorcerer of Colombian legend, smokes his pipe in a cave beneath the rapids and capsizes the boats of the careless. He loves regrets: tell him what you would have done differently… and what would have happened.')),
  [CH('deleb2-w5-c1', ('Sur le fleuve', 'On the river'), [
    L('es-condicional-compuesto', ('J’aurais aimé : le conditionnel passé', 'I would have liked: the conditional perfect'), ('Former le conditionnel passé et exprimer un regret, un reproche ou une supposition.', 'Form the conditional perfect and express a regret, a reproach or a guess.'), 10, [
        ('Conditionnel passé = haber au conditionnel + participe : habría, habrías, habría, habríamos, habríais, habrían + ido. Me habría gustado verlo (j’aurais aimé le voir).', 'Conditional perfect = haber in the conditional + participle: habría, habrías, habría, habríamos, habríais, habrían + ido. Me habría gustado verlo (I would have liked to see it).'),
        ('Reproche ou regret : Deberías haberme llamado (tu aurais dû m’appeler). Podrías haberlo dicho antes (tu aurais pu le dire avant).', 'Reproach or regret: Deberías haberme llamado (you should have called me). Podrías haberlo dicho antes (you could have said so before).'),
        ('Supposition sur un passé plus lointain : ¿Por qué no vino? — Habría perdido el autobús (il avait dû rater le bus).', 'Guess about an earlier past: ¿Por qué no vino? — Habría perdido el autobús (he must have missed the bus).'),
      ], [
        SG('condicional-compuesto', 'habría + participio', ('j’aurais + participe (conditionnel passé)', 'I would have + participle')),
        S('deberias-haber', 'deberías haber + participio', ('tu aurais dû…', 'you should have…')),
        S('podrias-haber', 'podrías haber + participio', ('tu aurais pu…', 'you could have…')),
        S('me-habria-gustado', 'me habría gustado', ('j’aurais aimé', 'I would have liked')),
        S('la-orilla', 'la orilla', ('la rive', 'the bank (of a river)')),
        S('la-canoa', 'la canoa', ('la pirogue, le canoë', 'the canoe')),
        S('hundirse', 'hundirse', ('couler, sombrer', 'to sink')),
        S('el-remo', 'el remo', ('la rame, la pagaie', 'the oar, the paddle')),
      ], [
        x('Me habría gustado navegar por el Magdalena, pero no tuve tiempo.', 'J’aurais aimé naviguer sur le Magdalena, mais je n’ai pas eu le temps.', 'I would have liked to sail down the Magdalena, but I didn’t have time.'),
        x('Deberías haberme avisado: la canoa casi se hunde.', 'Tu aurais dû me prévenir : la pirogue a failli couler.', 'You should have warned me: the canoe nearly sank.'),
      ], [
        FB(CHOOSE, 'Me ＿ gustado conocerte antes.', ['habría', 'había', 'hubo'], 'habría', ('Regret : habría + participe.', 'Regret: habría + participle.'), ('J’aurais aimé te connaître plus tôt.', 'I would have liked to meet you sooner.')),
        FB(CHOOSE, 'Deberías ＿ llamado antes de venir.', ['haber', 'habías', 'hubieras'], 'haber', ('Deberías haber + participe.', 'Deberías haber + participle.'), ('Tu aurais dû appeler avant de venir.', 'You should have called before coming.')),
        FB(CHOOSE, 'Yo, en tu lugar, ＿ aceptado el trabajo.', ['habría', 'hubiera habido', 'había'], 'habría', ('À ta place : conditionnel passé.', 'In your place: conditional perfect.'), ('À ta place, j’aurais accepté le travail.', 'In your place, I would have accepted the job.')),
        TF('Podrías haberme ayudado.', ('La personne reproche à l’autre de ne pas l’avoir aidée.', 'The person reproaches the other for not helping.'), VRAI, ('Podrías haber… = tu aurais pu…', 'Podrías haber… = you could have…')),
      ]),
    L('es-si-pasado', ('Si j’avais su : l’irréel du passé', 'If I had known: unreal past conditions'), ('Faire une hypothèse sur le passé avec si + plus-que-parfait du subjonctif.', 'Make a hypothesis about the past with si + past perfect subjunctive.'), 10, [
        ('Irréel du passé : si + hubiera (ou hubiese) + participe, puis habría + participe : Si hubiera sabido que venías, te habría esperado.', 'Unreal past: si + hubiera (or hubiese) + participle, then habría + participle: Si hubiera sabido que venías, te habría esperado.'),
        ('Plus-que-parfait du subjonctif : hubiera, hubieras, hubiera, hubiéramos, hubierais, hubieran + participe. À l’oral, il remplace souvent le conditionnel passé : Si lo hubiera sabido, no hubiera venido.', 'Past perfect subjunctive: hubiera, hubieras, hubiera, hubiéramos, hubierais, hubieran + participle. In speech it often replaces the conditional perfect: Si lo hubiera sabido, no hubiera venido.'),
        ('Conséquence dans le présent : Si hubiera estudiado medicina, ahora sería médico. Tournure soutenue : De haberlo sabido… (si j’avais su…).', 'Consequence in the present: Si hubiera estudiado medicina, ahora sería médico. Formal structure: De haberlo sabido… (had I known…).'),
      ], [
        SG('pluscuamperfecto-subj', 'hubiera + participio', ('(que) j’eusse + participe (plus-que-parfait du subjonctif)', 'had + participle (past perfect subjunctive)')),
        SG('si-hubiera', 'si hubiera… habría…', ('si j’avais… j’aurais…', 'if I had… I would have…')),
        S('de-haberlo-sabido', 'de haberlo sabido', ('si j’avais su', 'had I known')),
        S('arrepentirse', 'arrepentirse de', ('regretter (d’avoir fait)', 'to regret (having done)')),
        S('la-oportunidad', 'la oportunidad', ('l’occasion, la chance', 'the opportunity')),
        S('cometer-un-error', 'cometer un error', ('commettre une erreur', 'to make a mistake')),
        S('tomar-una-decision', 'tomar una decisión', ('prendre une décision', 'to make a decision')),
        S('el-destino', 'el destino', ('le destin, la destination', 'fate, destination')),
      ], [
        x('Si hubiera escuchado al barquero, no me habría caído al río.', 'Si j’avais écouté le passeur, je ne serais pas tombé dans le fleuve.', 'If I had listened to the boatman, I wouldn’t have fallen into the river.'),
        x('Si no hubiera tomado aquella decisión, ahora no viviría en Colombia.', 'Si je n’avais pas pris cette décision, je ne vivrais pas en Colombie aujourd’hui.', 'If I hadn’t made that decision, I wouldn’t be living in Colombia now.'),
      ], [
        FB(CHOOSE, 'Si ＿ antes, habríamos visto el atardecer.', ['hubiéramos llegado', 'habríamos llegado', 'llegáramos'], 'hubiéramos llegado', ('Si + plus-que-parfait du subjonctif.', 'Si + past perfect subjunctive.'), ('Si nous étions arrivés plus tôt, nous aurions vu le coucher du soleil.', 'If we had arrived earlier, we would have seen the sunset.')),
        FB(CHOOSE, 'Si me lo hubieras dicho, te ＿.', ['habría ayudado', 'hubiera ayudo', 'ayudaba'], 'habría ayudado', ('Conséquence : habría + participe.', 'Result: habría + participle.'), ('Si tu me l’avais dit, je t’aurais aidé.', 'If you had told me, I would have helped you.')),
        FB(CHOOSE, 'De ＿ sabido, no habría venido.', ['haberlo', 'hubiera', 'habría'], 'haberlo', ('De + infinitif passé : de haberlo sabido.', 'De + perfect infinitive: de haberlo sabido.'), ('Si j’avais su, je ne serais pas venu.', 'Had I known, I wouldn’t have come.')),
        TF('Si hubiera estudiado más, habría aprobado.', ('La personne a réussi son examen.', 'The person passed the exam.'), FAUX, ('Irréel du passé : elle n’a pas réussi.', 'Unreal past: she did not pass.')),
      ]),
  ]),
  CH('deleb2-w5-c2', ('Les regrets du passeur', 'The boatman’s regrets'), [
    L('es-lamentos', ('Si seulement… : regrets et reproches', 'If only…: regrets and reproaches'), ('Exprimer un regret, un souhait impossible ou un reproche.', 'Express a regret, an impossible wish or a reproach.'), 9, [
        ('Regret : ojalá + plus-que-parfait du subjonctif : Ojalá hubiera venido (si seulement il était venu). Me arrepiento de no haber estudiado más.', 'Regret: ojalá + past perfect subjunctive: Ojalá hubiera venido (if only he had come). Me arrepiento de no haber estudiado más.'),
        ('Souhait impossible : ¡Quién pudiera volar! (si seulement je pouvais voler !) ¡Quién tuviera veinte años!', 'Impossible wish: ¡Quién pudiera volar! (if only I could fly!) ¡Quién tuviera veinte años!'),
        ('Reproche : ¡Haberlo dicho antes! (il fallait le dire avant !). Tener la culpa = être responsable : La culpa es mía.', 'Reproach: ¡Haberlo dicho antes! (you should have said so before!). Tener la culpa = to be to blame: La culpa es mía.'),
      ], [
        SG('ojala-hubiera', 'ojalá hubiera + participio', ('si seulement j’avais…', 'if only I had…')),
        S('quien-pudiera', '¡Quién pudiera…!', ('Si seulement je pouvais… !', 'If only I could…!')),
        S('haberlo-dicho', '¡Haberlo dicho antes!', ('Il fallait le dire avant !', 'You should have said so before!')),
        S('lamentar', 'lamentar', ('regretter, déplorer', 'to be sorry about')),
        S('echar-de-menos', 'echar de menos', ('manquer à quelqu’un (regretter l’absence)', 'to miss (someone)')),
        S('la-nostalgia', 'la nostalgia', ('la nostalgie', 'nostalgia')),
        S('advertir', 'advertir', ('avertir', 'to warn (formally)')),
        S('tener-la-culpa', 'tener la culpa', ('être responsable, être fautif', 'to be to blame')),
      ], [
        x('Ojalá hubiera traído el impermeable: llueve a cántaros en Medellín.', 'Si seulement j’avais pris mon imperméable : il pleut des cordes à Medellín.', 'If only I’d brought my raincoat: it’s pouring down in Medellín.'),
        x('¿Que no sabías nadar? ¡Haberlo dicho antes de subir a la canoa!', 'Tu ne savais pas nager ? Il fallait le dire avant de monter dans la pirogue !', 'You couldn’t swim? You should have said so before getting into the canoe!'),
      ], [
        FB(CHOOSE, 'Ojalá ＿ más tiempo con mis abuelos.', ['hubiera pasado', 'habría pasado', 'he pasado'], 'hubiera pasado', ('Regret : ojalá + plus-que-parfait du subjonctif.', 'Regret: ojalá + past perfect subjunctive.'), ('Si seulement j’avais passé plus de temps avec mes grands-parents.', 'If only I had spent more time with my grandparents.')),
        FB(CHOOSE, '¡Quién ＿ vivir junto al mar!', ['pudiera', 'puede', 'podría'], 'pudiera', ('Souhait impossible : quién + imparfait du subjonctif.', 'Impossible wish: quién + past subjunctive.'), ('Si seulement je pouvais vivre au bord de la mer !', 'If only I could live by the sea!')),
        DC(ANSWER, [('Mohán', 'Perdiste el último barco. ¿Qué sientes?')], ('Le Mohán te demande ce que tu ressens après avoir raté le dernier bateau.', 'The Mohán asks how you feel after missing the last boat.'), ['Me arrepiento de no haber salido antes.', 'Me arrepiento de no salir mañana.', 'Ojalá saldré antes.'], 'Me arrepiento de no haber salido antes.', ('Arrepentirse de + infinitif passé.', 'Arrepentirse de + perfect infinitive.')),
        TF('Echo de menos a mi familia.', ('La famille manque à la personne.', 'The person misses their family.'), VRAI, ('Echar de menos = manquer à quelqu’un.', 'Echar de menos = to miss.')),
      ]),
  ])])

# ═════════════════════════ 6 : les Andes — le passif, le se impersonnel, la presse ═════════════════════════
W6 = WORLD('deleb2-w6', ('Les mines des Andes', 'The mines of the Andes'), REGION,
  ('Employer la voix passive (fue construido), les tournures impersonnelles (se vende, dicen que) et comprendre la presse (según, al parecer, conditionnel journalistique).', 'Use the passive voice (fue construido), impersonal structures (se vende, dicen que) and understand the press (según, al parecer, journalistic conditional).'),
  (('Le Muki des mines', 'The Muki of the mines'), 'Ã', ('Dans les galeries des Andes, le Muki, petit gnome barbu au casque d’or, protège les filons et égare les mineurs. Il ne s’intéresse qu’aux nouvelles : apprends à lire la presse, à tourner les phrases au passif et à parler de façon impersonnelle.', 'In the tunnels of the Andes, the Muki, a little bearded gnome with a golden helmet, guards the seams and leads miners astray. He only cares about the news: learn to read the press, put sentences in the passive and speak impersonally.')),
  [CH('deleb2-w6-c1', ('Les galeries du Muki', 'The Muki’s tunnels'), [
    L('es-pasiva', ('Il a été construit : la voix passive', 'It was built: the passive voice'), ('Former la voix passive avec ser et l’état résultant avec estar.', 'Form the passive with ser and the resulting state with estar.'), 10, [
        ('Passif = ser + participe accordé (+ por) : Machu Picchu fue construido por los incas. Las ruinas fueron descubiertas en 1911.', 'Passive = ser + agreeing participle (+ por): Machu Picchu fue construido por los incas. Las ruinas fueron descubiertas en 1911.'),
        ('Estar + participe = l’état qui résulte d’une action : El museo está cerrado. La ciudad está rodeada de montañas.', 'Estar + participle = the state resulting from an action: El museo está cerrado. La ciudad está rodeada de montañas.'),
        ('Le passif avec ser s’emploie surtout à l’écrit (presse, histoire) ; à l’oral, on préfère la voix active ou la tournure avec se.', 'The passive with ser is used mainly in writing (press, history); in speech, the active voice or se is preferred.'),
      ], [
        SG('pasiva-ser', 'ser + participio (+ por)', ('être + participe (passif)', 'to be + participle (passive)')),
        SG('estar-participio', 'estar + participio', ('être + participe (état)', 'to be + participle (state)')),
        S('construir', 'construir', ('construire', 'to build')),
        S('destruir', 'destruir', ('détruire', 'to destroy')),
        S('rodeado-de', 'rodeado de', ('entouré de', 'surrounded by')),
        S('el-imperio', 'el imperio', ('l’empire', 'the empire')),
        S('la-mina', 'la mina', ('la mine', 'the mine')),
        S('el-oro', 'el oro / la plata', ('l’or / l’argent (métal)', 'gold / silver')),
      ], [
        x('Machu Picchu fue construido en el siglo XV y no fue conocido por el mundo hasta 1911.', 'Machu Picchu fut construit au XVe siècle et ne fut connu du monde qu’en 1911.', 'Machu Picchu was built in the fifteenth century and was not known to the world until 1911.'),
        x('El valle está rodeado de montañas y la mina está cerrada desde hace años.', 'La vallée est entourée de montagnes et la mine est fermée depuis des années.', 'The valley is surrounded by mountains and the mine has been closed for years.'),
      ], [
        FB(CHOOSE, 'El puente fue ＿ por los incas.', ['construido', 'construida', 'construyó'], 'construido', ('El puente (masculin) : construido.', 'El puente (masculine): construido.'), ('Le pont fut construit par les Incas.', 'The bridge was built by the Incas.')),
        FB(CHOOSE, 'Las cartas fueron ＿ por el rey.', ['escritas', 'escritos', 'escribieron'], 'escritas', ('Las cartas (féminin pluriel) : escritas.', 'Las cartas (feminine plural): escritas.'), ('Les lettres furent écrites par le roi.', 'The letters were written by the king.')),
        FB(CHOOSE, 'Ahora la puerta ＿ abierta.', ['está', 'es', 'fue'], 'está', ('État résultant : estar + participe.', 'Resulting state: estar + participle.'), ('Maintenant, la porte est ouverte.', 'Now the door is open.')),
        order(('Remets dans l’ordre : « La ville a été détruite par un tremblement de terre. »', 'Put in order: “The city was destroyed by an earthquake.”'), ['La', 'ciudad', 'fue', 'destruida', 'por', 'un', 'terremoto.'], ('Sujet + fue + participe + por + agent.', 'Subject + fue + participle + por + agent.')),
      ]),
    L('es-se-impersonal', ('On dit que… : se impersonnel et se passif', 'People say…: impersonal and passive se'), ('Parler de façon impersonnelle avec se, la 3e personne du pluriel et uno.', 'Speak impersonally with se, the 3rd person plural and uno.'), 9, [
        ('Se passif : se + verbe accordé avec le sujet : Se venden casas. Se alquila piso. Se construyeron nuevas carreteras.', 'Passive se: se + verb agreeing with the subject: Se venden casas. Se alquila piso. Se construyeron nuevas carreteras.'),
        ('Se impersonnel : se + verbe au singulier, sans sujet : Se vive bien aquí. Se busca a los responsables.', 'Impersonal se: se + singular verb, with no subject: Se vive bien aquí. Se busca a los responsables.'),
        ('Autres tournures : la 3e personne du pluriel (Dicen que… = on dit que), uno / una (Uno nunca sabe), la gente.', 'Other structures: the 3rd person plural (Dicen que… = they say that), uno / una (Uno nunca sabe), la gente.'),
      ], [
        SG('se-pasiva', 'se venden / se alquila', ('à vendre / à louer (se passif)', 'for sale / for rent (passive se)')),
        SG('se-impersonal', 'se vive / se dice', ('on vit / on dit (se impersonnel)', 'people live / people say (impersonal se)')),
        S('dicen-que', 'dicen que…', ('on dit que…', 'they say that…')),
        S('uno-nunca-sabe', 'uno nunca sabe', ('on ne sait jamais', 'you never know')),
        S('se-prohibe', 'se prohíbe', ('il est interdit de', 'it is forbidden to')),
        S('el-mal-de-altura', 'el mal de altura', ('le mal des montagnes', 'altitude sickness')),
        S('la-llama', 'la llama', ('le lama', 'the llama')),
        S('la-infusion', 'la infusión', ('l’infusion', 'the herbal tea')),
      ], [
        x('En Cuzco se recomienda descansar el primer día por el mal de altura.', 'À Cuzco, on recommande de se reposer le premier jour à cause du mal des montagnes.', 'In Cusco it’s recommended to rest on the first day because of altitude sickness.'),
        x('Dicen que en estas minas se encontró oro hace siglos. — Uno nunca sabe…', 'On dit qu’on a trouvé de l’or dans ces mines il y a des siècles. — On ne sait jamais…', 'They say gold was found in these mines centuries ago. — You never know…'),
      ], [
        FB(CHOOSE, 'Se ＿ habitaciones con vistas al lago.', ['alquilan', 'alquila', 'alquilamos'], 'alquilan', ('Se passif : accord avec habitaciones.', 'Passive se: agrees with habitaciones.'), ('Chambres à louer avec vue sur le lac.', 'Rooms for rent with lake views.')),
        FB(CHOOSE, 'En esta ciudad se ＿ muy bien.', ['vive', 'viven', 'vivimos'], 'vive', ('Se impersonnel : verbe au singulier.', 'Impersonal se: singular verb.'), ('Dans cette ville, on vit très bien.', 'People live very well in this city.')),
        FB(CHOOSE, '＿ que va a llover mañana.', ['Dicen', 'Se dicen', 'Dice uno'], 'Dicen', ('On dit que : dicen que.', 'They say that: dicen que.'), ('On dit qu’il va pleuvoir demain.', 'They say it’s going to rain tomorrow.')),
        TF('Se prohíbe fumar.', ('On a le droit de fumer.', 'Smoking is allowed.'), FAUX, ('Se prohíbe = il est interdit.', 'Se prohíbe = it is forbidden.')),
      ]),
  ]),
  CH('deleb2-w6-c2', ('Le journal de Cuzco', 'The Cusco newspaper'), [
    L('es-prensa', ('La presse : el titular, según, al parecer', 'The press: el titular, según, al parecer'), ('Comprendre un article de presse et rapporter une information non confirmée.', 'Understand a news article and report unconfirmed information.'), 9, [
        ('La presse : el periódico, la noticia, el titular (le gros titre), la portada (la une), el artículo de opinión, el / la periodista, la entrevista.', 'The press: el periódico, la noticia, el titular (the headline), la portada (the front page), el artículo de opinión, el / la periodista, la entrevista.'),
        ('Information non confirmée : según (selon), al parecer (apparemment), conditionnel journalistique : El ministro habría dimitido (le ministre aurait démissionné).', 'Unconfirmed information: según (according to), al parecer (apparently), journalistic conditional: El ministro habría dimitido (the minister has reportedly resigned).'),
        ('Les verbes de la presse : informar, anunciar, afirmar, negar (nier), confirmar, denunciar.', 'Press verbs: informar, anunciar, afirmar, negar (to deny), confirmar, denunciar.'),
      ], [
        S('el-titular', 'el titular', ('le gros titre', 'the headline')),
        S('la-noticia', 'la noticia', ('la nouvelle, l’information', 'the news item')),
        S('el-periodista', 'el / la periodista', ('le / la journaliste', 'the journalist')),
        S('la-portada', 'la portada', ('la une (d’un journal)', 'the front page')),
        S('segun', 'según', ('d’après, selon', 'according to')),
        S('al-parecer', 'al parecer', ('apparemment', 'apparently')),
        S('negar', 'negar', ('nier', 'to deny')),
        S('afirmar', 'afirmar', ('affirmer', 'to state, to claim')),
      ], [
        x('Según el periódico, los arqueólogos habrían encontrado una nueva tumba inca.', 'Selon le journal, les archéologues auraient trouvé une nouvelle tombe inca.', 'According to the newspaper, archaeologists have reportedly found a new Inca tomb.'),
        x('El alcalde negó la noticia, pero al parecer la mina volverá a abrir.', 'Le maire a démenti la nouvelle, mais apparemment la mine va rouvrir.', 'The mayor denied the story, but apparently the mine will reopen.'),
      ], [
        FB(COMPLETE, 'La noticia salió en la ＿ de todos los periódicos.', ['portada', 'periodista', 'mina'], 'portada', ('La une : la portada.', 'The front page: la portada.'), ('La nouvelle a fait la une de tous les journaux.', 'The story was on the front page of every newspaper.')),
        FB(CHOOSE, 'Según la policía, el ladrón ＿ huido a Bolivia.', ['habría', 'habrá sido', 'haya'], 'habría', ('Information non confirmée : conditionnel journalistique.', 'Unconfirmed information: journalistic conditional.'), ('Selon la police, le voleur aurait fui en Bolivie.', 'According to the police, the thief has reportedly fled to Bolivia.')),
        FB(COMPLETE, 'El ministro ＿ las acusaciones: dijo que eran falsas.', ['negó', 'afirmó', 'confirmó'], 'negó', ('Nier : negar.', 'To deny: negar.'), ('Le ministre a nié les accusations : il a dit qu’elles étaient fausses.', 'The minister denied the accusations: he said they were false.')),
        TF('Al parecer, el museo cerrará en verano.', ('L’information est présentée comme certaine.', 'The news is presented as certain.'), FAUX, ('Al parecer = apparemment : ce n’est pas confirmé.', 'Al parecer = apparently: it isn’t confirmed.')),
      ]),
  ])])

# ═════════════════════════ 7 : Chiloé — le discours rapporté au passé, les relatifs, le débat ═════════════════════════
W7 = WORLD('deleb2-w7', ('Le vaisseau fantôme de Chiloé', 'The ghost ship of Chiloé'), REGION,
  ('Rapporter des paroles au passé (dijo que vendría), employer les relatifs soutenus (cuyo, el cual, lo cual) et argumenter dans un débat.', 'Report speech in the past (dijo que vendría), use formal relatives (cuyo, el cual, lo cual) and argue in a debate.'),
  (('Le Caleuche', 'The Caleuche'), 'Õ', ('Au large de Chiloé, le Caleuche, navire fantôme illuminé et plein de musique, emporte les marins qui ne savent pas débattre. Rapporte fidèlement les paroles de l’équipage, relie tes idées avec précision et argumente pour qu’il te laisse débarquer.', 'Off the coast of Chiloé, the Caleuche, a glowing ghost ship full of music, carries off sailors who cannot debate. Report the crew’s words faithfully, link your ideas precisely and argue your case so it lets you go ashore.')),
  [CH('deleb2-w7-c1', ('Les paroles de l’équipage', 'The crew’s words'), [
    L('es-indirecto-pasado', ('Il a dit qu’il viendrait : le discours rapporté au passé', 'He said he would come: reported speech in the past'), ('Transformer les temps, les ordres et les repères dans le discours rapporté au passé.', 'Change tenses, orders and time references in reported speech in the past.'), 10, [
        ('Les temps reculent : présent → imparfait ; passé composé → plus-que-parfait ; futur → conditionnel. «Vendré» → Dijo que vendría. «He terminado» → Dijo que había terminado.', 'Tenses shift back: present → imperfect; present perfect → past perfect; future → conditional. «Vendré» → Dijo que vendría. «He terminado» → Dijo que había terminado.'),
        ('Ordres et demandes → imparfait du subjonctif : «Ven» → Me pidió que fuera. Les questions : Me preguntó si / dónde / cuándo…', 'Orders and requests → past subjunctive: «Ven» → Me pidió que fuera. Questions: Me preguntó si / dónde / cuándo…'),
        ('Les repères changent : hoy → aquel día, mañana → al día siguiente, ayer → el día anterior, aquí → allí.', 'Time and place references change: hoy → aquel día, mañana → al día siguiente, ayer → el día anterior, aquí → allí.'),
      ], [
        SG('dijo-que-vendria', 'dijo que vendría', ('il a dit qu’il viendrait', 'he said he would come')),
        SG('me-pidio-que', 'me pidió que + imperfecto de subjuntivo', ('il m’a demandé de…', 'he asked me to…')),
        S('aquel-dia', 'aquel día', ('ce jour-là', 'that day')),
        S('el-dia-anterior', 'el día anterior', ('la veille', 'the day before')),
        S('asegurar', 'asegurar', ('assurer, affirmer', 'to assure')),
        S('prometer', 'prometer', ('promettre', 'to promise')),
        S('el-marinero', 'el marinero', ('le marin', 'the sailor')),
        S('la-tripulacion', 'la tripulación', ('l’équipage', 'the crew')),
      ], [
        x('El capitán nos aseguró que llegaríamos a Chiloé al día siguiente.', 'Le capitaine nous a assuré que nous arriverions à Chiloé le lendemain.', 'The captain assured us that we would reach Chiloé the next day.'),
        x('Un marinero me pidió que no le contara a nadie lo que había visto aquella noche.', 'Un marin m’a demandé de ne raconter à personne ce que j’avais vu cette nuit-là.', 'A sailor asked me not to tell anyone what I had seen that night.'),
      ], [
        FB(CHOOSE, '«Volveré pronto». → Dijo que ＿ pronto.', ['volvería', 'volverá', 'vuelva'], 'volvería', ('Futur → conditionnel.', 'Future → conditional.'), ('« Je reviendrai bientôt. » → Il a dit qu’il reviendrait bientôt.', '“I’ll be back soon.” → He said he would be back soon.')),
        FB(CHOOSE, '«He visto el barco». → Dijo que ＿ el barco.', ['había visto', 'ha visto', 'vería'], 'había visto', ('Passé composé → plus-que-parfait.', 'Present perfect → past perfect.'), ('« J’ai vu le bateau. » → Il a dit qu’il avait vu le bateau.', '“I’ve seen the ship.” → He said he had seen the ship.')),
        FB(CHOOSE, '«Ayúdame». → Me pidió que lo ＿.', ['ayudara', 'ayude', 'ayudaba'], 'ayudara', ('Ordre rapporté au passé : imparfait du subjonctif.', 'Order reported in the past: past subjunctive.'), ('« Aide-moi. » → Il m’a demandé de l’aider.', '“Help me.” → He asked me to help him.')),
        FB(CHOOSE, '«Mañana salimos». → Dijo que ＿ salían.', ['al día siguiente', 'mañana', 'ayer'], 'al día siguiente', ('Mañana → al día siguiente.', 'Mañana → al día siguiente.'), ('« Nous partons demain. » → Il a dit qu’ils partaient le lendemain.', '“We leave tomorrow.” → He said they were leaving the next day.')),
      ]),
    L('es-relativos-b2', ('Dont, lequel : cuyo, el cual, lo cual', 'Whose, which: cuyo, el cual, lo cual'), ('Employer les relatifs soutenus cuyo, el cual et lo cual.', 'Use the formal relatives cuyo, el cual and lo cual.'), 10, [
        ('Cuyo, cuya, cuyos, cuyas = dont (possession) ; il s’accorde avec ce qui est possédé : el pescador cuya barca se hundió.', 'Cuyo, cuya, cuyos, cuyas = whose (possession); it agrees with what is owned: el pescador cuya barca se hundió.'),
        ('El cual, la cual, los cuales, las cuales après une préposition, surtout à l’écrit : la isla en la cual vivimos.', 'El cual, la cual, los cuales, las cuales after a preposition, mostly in writing: la isla en la cual vivimos.'),
        ('Lo cual / lo que = ce qui (reprend toute une phrase) : Llovió toda la semana, lo cual nos obligó a quedarnos en casa.', 'Lo cual / lo que = which (refers back to a whole clause): Llovió toda la semana, lo cual nos obligó a quedarnos en casa.'),
      ], [
        SG('cuyo', 'cuyo / cuya / cuyos / cuyas', ('dont, à qui', 'whose')),
        SG('el-cual', 'el cual / la cual', ('lequel / laquelle', 'which, whom (formal)')),
        S('lo-cual', 'lo cual', ('ce qui (reprend une phrase)', 'which (refers to a whole clause)')),
        S('la-leyenda', 'la leyenda', ('la légende', 'the legend')),
        S('el-barco-fantasma', 'el barco fantasma', ('le vaisseau fantôme', 'the ghost ship')),
        S('la-marea', 'la marea', ('la marée', 'the tide')),
        S('el-muelle', 'el muelle', ('le quai (d’un port)', 'the quay, the pier')),
        S('el-pescador', 'el pescador', ('le pêcheur', 'the fisherman')),
      ], [
        x('Es una leyenda de Chiloé cuyo origen nadie conoce.', 'C’est une légende de Chiloé dont personne ne connaît l’origine.', 'It’s a legend from Chiloé whose origin nobody knows.'),
        x('La marea subió de repente, lo cual asustó a los pescadores del muelle.', 'La marée est montée d’un coup, ce qui a effrayé les pêcheurs du quai.', 'The tide rose suddenly, which frightened the fishermen on the quay.'),
      ], [
        FB(CHOOSE, 'Es el pescador ＿ barca desapareció.', ['cuya', 'cuyo', 'que su'], 'cuya', ('Cuya s’accorde avec barca.', 'Cuya agrees with barca.'), ('C’est le pêcheur dont la barque a disparu.', 'He’s the fisherman whose boat disappeared.')),
        FB(CHOOSE, 'Perdimos el último barco, ＿ nos obligó a dormir en el puerto.', ['lo cual', 'el cual', 'cuyo'], 'lo cual', ('Reprend toute la phrase : lo cual.', 'Refers to the whole clause: lo cual.'), ('Nous avons raté le dernier bateau, ce qui nous a obligés à dormir au port.', 'We missed the last boat, which forced us to sleep at the port.')),
        FB(CHOOSE, 'Esta es la isla en ＿ nació mi abuela.', ['la cual', 'cuya', 'lo cual'], 'la cual', ('Après une préposition : la cual.', 'After a preposition: la cual.'), ('Voici l’île où est née ma grand-mère.', 'This is the island where my grandmother was born.')),
        TF('El autor, cuyos libros leo, vive en Chile.', ('Je lis les livres de cet auteur.', 'I read this author’s books.'), VRAI, ('Cuyos libros = dont les livres.', 'Cuyos libros = whose books.')),
      ]),
  ]),
  CH('deleb2-w7-c2', ('Le débat sur le pont', 'The debate on deck'), [
    L('es-debate', ('Argumenter : en primer lugar, no obstante, por consiguiente', 'Arguing: en primer lugar, no obstante, por consiguiente'), ('Structurer une argumentation avec les connecteurs du registre soutenu.', 'Structure an argument with formal connectors.'), 9, [
        ('Introduire et ordonner : en primer lugar, en segundo lugar, cabe destacar que (il convient de souligner que), hay que tener en cuenta que (il faut tenir compte de).', 'Introducing and ordering: en primer lugar, en segundo lugar, cabe destacar que (it is worth highlighting that), hay que tener en cuenta que (we must take into account that).'),
        ('Opposer et concéder : no obstante (néanmoins), si bien es cierto que… (s’il est vrai que…), por el contrario (au contraire).', 'Contrasting and conceding: no obstante (nevertheless), si bien es cierto que… (while it is true that…), por el contrario (on the contrary).'),
        ('Conclure : por consiguiente (par conséquent), en definitiva, en conclusión, para terminar.', 'Concluding: por consiguiente (consequently), en definitiva, en conclusión, para terminar.'),
      ], [
        S('en-primer-lugar', 'en primer lugar', ('premièrement, en premier lieu', 'first of all, firstly')),
        S('cabe-destacar', 'cabe destacar que', ('il convient de souligner que', 'it is worth highlighting that')),
        S('tener-en-cuenta', 'tener en cuenta', ('tenir compte de', 'to take into account')),
        S('no-obstante', 'no obstante', ('néanmoins', 'nevertheless')),
        S('por-consiguiente', 'por consiguiente', ('par conséquent', 'consequently')),
        S('en-definitiva', 'en definitiva', ('en définitive, bref', 'in short, ultimately')),
        S('por-el-contrario', 'por el contrario', ('au contraire', 'on the contrary')),
        S('el-argumento', 'el argumento', ('l’argument', 'the argument (reason)')),
      ], [
        x('En primer lugar, cabe destacar que el turismo ha traído trabajo a la isla; no obstante, también ha encarecido la vivienda.', 'En premier lieu, il convient de souligner que le tourisme a apporté du travail sur l’île ; néanmoins, il a aussi fait grimper le prix du logement.', 'First of all, it’s worth highlighting that tourism has brought jobs to the island; nevertheless, it has also made housing more expensive.'),
        x('Por consiguiente, hay que tener en cuenta la opinión de los vecinos.', 'Par conséquent, il faut tenir compte de l’avis des habitants.', 'Consequently, residents’ opinions must be taken into account.'),
      ], [
        FB(CHOOSE, 'El proyecto es caro; ＿, puede crear empleo.', ['no obstante', 'por consiguiente', 'en primer lugar'], 'no obstante', ('Opposition : no obstante.', 'Contrast: no obstante.'), ('Le projet est cher ; néanmoins, il peut créer des emplois.', 'The project is expensive; nevertheless, it can create jobs.')),
        FB(CHOOSE, 'No hay suficientes médicos; ＿, las esperas son largas.', ['por consiguiente', 'no obstante', 'por el contrario'], 'por consiguiente', ('Conséquence : por consiguiente.', 'Consequence: por consiguiente.'), ('Il n’y a pas assez de médecins ; par conséquent, l’attente est longue.', 'There aren’t enough doctors; consequently, waiting times are long.')),
        FB(CHOOSE, 'Hay que ＿ en cuenta el coste.', ['tener', 'poner', 'hacer'], 'tener', ('Tener en cuenta = tenir compte de.', 'Tener en cuenta = to take into account.'), ('Il faut tenir compte du coût.', 'The cost must be taken into account.')),
        TF('En definitiva, el turismo tiene más ventajas que inconvenientes.', ('C’est une phrase de conclusion.', 'It is a concluding sentence.'), VRAI, ('En definitiva introduit une conclusion.', 'En definitiva introduces a conclusion.')),
      ]),
  ])])

# ═════════════════════════ 8 : Buenos Aires — le voseo, les subordonnées de temps, l'entretien ═════════════════════════
W8 = WORLD('deleb2-w8', ('Buenos Aires et la pampa', 'Buenos Aires and the pampas'), REGION,
  ('Comprendre le voseo et l’espagnol du Río de la Plata, situer les actions dans le temps (antes de que, nada más + infinitif) et réussir un entretien d’embauche.', 'Understand voseo and River Plate Spanish, place actions in time (antes de que, nada más + infinitive) and succeed in a job interview.'),
  (('Le Pombero', 'The Pombero'), 'ỹ', ('Dans les forêts du nord de l’Argentine et du Paraguay, le Pombero, petit homme velu qui imite le chant des oiseaux, protège la nature et joue des tours aux voyageurs. Pour le gagner à ta cause, parle comme un vrai porteño, situe chaque action dans le temps et réussis ton entretien d’embauche.', 'In the forests of northern Argentina and Paraguay, the Pombero, a hairy little man who imitates birdsong, protects nature and plays tricks on travellers. To win him over, talk like a real porteño, place every action in time and ace your job interview.')),
  [CH('deleb2-w8-c1', ('Les rues de Buenos Aires', 'The streets of Buenos Aires'), [
    L('es-voseo', ('Vos tenés : le voseo du Río de la Plata', 'Vos tenés: River Plate voseo'), ('Comprendre et employer le voseo et le vocabulaire rioplatense.', 'Understand and use voseo and River Plate vocabulary.'), 10, [
        ('En Argentine, en Uruguay et au Paraguay, vos remplace tú : vos sos (tu es), vos tenés, vos querés, vos vivís. L’accent tombe sur la fin et il n’y a pas de diphtongue : tenés (tienes), podés (puedes).', 'In Argentina, Uruguay and Paraguay, vos replaces tú: vos sos (you are), vos tenés, vos querés, vos vivís. The stress falls at the end and there is no diphthong: tenés (tienes), podés (puedes).'),
        ('L’impératif : vení (viens), decime (dis-moi), mirá (regarde), tomá (tiens, prends).', 'The imperative: vení (come), decime (tell me), mirá (look), tomá (here, take it).'),
        ('Mots rioplatenses : che (hé, eh), ¡dale! (d’accord, vas-y), el colectivo (le bus), la pileta (la piscine), el subte (le métro de Buenos Aires), laburar (travailler).', 'River Plate words: che (hey), ¡dale! (OK, go on), el colectivo (the bus), la pileta (the pool), el subte (the Buenos Aires underground), laburar (to work).'),
      ], [
        SG('voseo', 'vos sos / vos tenés', ('tu es / tu as (voseo)', 'you are / you have (voseo)')),
        SG('imperativo-vos', 'vení / decime / mirá', ('viens / dis-moi / regarde (voseo)', 'come / tell me / look (voseo)')),
        S('che', 'che', ('hé, eh (Río de la Plata)', 'hey, mate (River Plate)')),
        S('dale', '¡Dale!', ('D’accord ! Vas-y ! (Río de la Plata)', 'OK! Go on! (River Plate)')),
        S('el-colectivo', 'el colectivo', ('le bus (Argentine)', 'the bus (Argentina)')),
        S('laburar', 'laburar', ('travailler (Argentine, familier)', 'to work (Argentina, informal)')),
        S('el-subte', 'el subte', ('le métro (Buenos Aires)', 'the underground (Buenos Aires)')),
        S('la-pileta', 'la pileta', ('la piscine (Argentine)', 'the swimming pool (Argentina)')),
      ], [
        x('Che, ¿vos sabés a qué hora sale el colectivo para La Plata?', 'Hé, tu sais à quelle heure part le bus pour La Plata ?', 'Hey, do you know what time the bus to La Plata leaves?'),
        x('Vení el sábado a casa, tenemos pileta. — ¡Dale!', 'Viens samedi à la maison, on a une piscine. — D’accord !', 'Come over on Saturday, we’ve got a pool. — Sure!'),
      ], [
        FB(CHOOSE, 'Vos ＿ argentino, ¿no?', ['sos', 'eres', 'es'], 'sos', ('Voseo : vos sos.', 'Voseo: vos sos.'), ('Tu es argentin, non ?', 'You’re Argentinian, aren’t you?')),
        FB(CHOOSE, '¿Vos ＿ hermanos?', ['tenés', 'tienes', 'tenéis'], 'tenés', ('Voseo : vos tenés.', 'Voseo: vos tenés.'), ('Tu as des frères et sœurs ?', 'Have you got any brothers or sisters?')),
        DC(ANSWER, [('Porteña', '¿Venís al asado el domingo?')], ('Une habitante de Buenos Aires t’invite à un barbecue ; tu acceptes.', 'A woman from Buenos Aires invites you to a barbecue; you accept.'), ['¡Dale! ¿Llevo algo?', '¡Órale! Llevo algo.', 'Vale, llevaré nada.'], '¡Dale! ¿Llevo algo?', ('Accepter au Río de la Plata : ¡dale!', 'Accepting in the River Plate: ¡dale!')),
        FB(COMPLETE, 'En Buenos Aires, para ir al centro, tomo el ＿.', ['subte', 'pileta', 'asado'], 'subte', ('Le métro de Buenos Aires : el subte.', 'The Buenos Aires underground: el subte.'), ('À Buenos Aires, pour aller au centre, je prends le métro.', 'In Buenos Aires, I take the underground to go downtown.')),
      ]),
    L('es-temporales', ('Avant que, dès que : antes de que, nada más', 'Before, as soon as: antes de que, nada más'), ('Situer les actions dans le temps avec les subordonnées et les tournures à l’infinitif.', 'Place actions in time with subordinate clauses and infinitive structures.'), 10, [
        ('Antes de que + subjonctif, toujours : Llámame antes de que salga el avión. Au passé : Me fui antes de que llegaran.', 'Antes de que + subjunctive, always: Llámame antes de que salga el avión. In the past: Me fui antes de que llegaran.'),
        ('Después de que, en cuanto, cuando : subjonctif pour le futur, indicatif pour le passé : En cuanto llegues, avísame. En cuanto llegó, me avisó.', 'Después de que, en cuanto, cuando: subjunctive for the future, indicative for the past: En cuanto llegues, avísame. En cuanto llegó, me avisó.'),
        ('Nada más + infinitif = dès que, à peine : Nada más llegar, se durmió. Al + infinitif = au moment de : Al salir, vi a Pedro.', 'Nada más + infinitive = as soon as: Nada más llegar, se durmió. Al + infinitive = on/when: Al salir, vi a Pedro.'),
      ], [
        SG('antes-de-que', 'antes de que + subjuntivo', ('avant que + subjonctif', 'before + clause')),
        SG('despues-de-que', 'después de que', ('après que', 'after + clause')),
        S('nada-mas', 'nada más + infinitivo', ('dès que, à peine…', 'as soon as, no sooner…')),
        S('al-infinitivo', 'al + infinitivo', ('au moment de, en (+ participe présent)', 'on/when + -ing')),
        S('mientras-tanto', 'mientras tanto', ('pendant ce temps', 'meanwhile')),
        S('el-asado', 'el asado', ('le barbecue (argentin)', 'the barbecue (Argentinian)')),
        S('la-pampa', 'la pampa', ('la pampa', 'the pampas')),
        S('el-gaucho', 'el gaucho', ('le gaucho', 'the gaucho')),
      ], [
        x('Nada más llegar a la estancia, los gauchos nos invitaron a un asado.', 'Dès notre arrivée à l’estancia, les gauchos nous ont invités à un barbecue.', 'As soon as we arrived at the ranch, the gauchos invited us to a barbecue.'),
        x('Volvamos a la ciudad antes de que se haga de noche en la pampa.', 'Rentrons en ville avant qu’il fasse nuit dans la pampa.', 'Let’s go back to the city before it gets dark on the pampas.'),
      ], [
        FB(CHOOSE, 'Salgamos antes de que ＿ a llover.', ['empiece', 'empieza', 'empezará'], 'empiece', ('Antes de que + subjonctif.', 'Antes de que + subjunctive.'), ('Partons avant qu’il commence à pleuvoir.', 'Let’s leave before it starts raining.')),
        FB(CHOOSE, 'Después de que ＿ los invitados, limpiaremos.', ['se vayan', 'se van', 'se irán'], 'se vayan', ('Futur : después de que + subjonctif.', 'Future: después de que + subjunctive.'), ('Après le départ des invités, nous ferons le ménage.', 'After the guests leave, we’ll clean up.')),
        FB(CHOOSE, 'Nada más ＿ a casa, se quitó los zapatos.', ['llegar', 'llegó', 'llegue'], 'llegar', ('Nada más + infinitif.', 'Nada más + infinitive.'), ('Dès qu’il est arrivé à la maison, il a enlevé ses chaussures.', 'As soon as he got home, he took off his shoes.')),
        FB(CHOOSE, '＿ salir del cine, vimos a Lucía.', ['Al', 'Nada', 'Antes'], 'Al', ('Au moment de : al + infinitif.', 'When: al + infinitive.'), ('En sortant du cinéma, nous avons vu Lucía.', 'Coming out of the cinema, we saw Lucía.')),
      ]),
  ]),
  CH('deleb2-w8-c2', ('Un emploi à l’estancia', 'A job at the ranch'), [
    L('es-entrevista', ('L’entretien d’embauche', 'The job interview'), ('Se présenter, parler de son expérience et répondre aux questions d’un entretien.', 'Introduce yourself, talk about your experience and answer interview questions.'), 9, [
        ('Le poste : el puesto de trabajo, la oferta de empleo, el contrato (indefinido / temporal), a jornada completa / a tiempo parcial, el sueldo.', 'The job: el puesto de trabajo, la oferta de empleo, el contrato (indefinido / temporal), a jornada completa / a tiempo parcial, el sueldo.'),
        ('Se présenter : Tengo experiencia en…, Me considero una persona responsable, Domino el inglés (je maîtrise l’anglais), Me encantaría formar parte de su equipo.', 'Presenting yourself: Tengo experiencia en…, Me considero una persona responsable, Domino el inglés (I’m fluent in English), Me encantaría formar parte de su equipo.'),
        ('Les questions : ¿Por qué quiere este puesto? ¿Cuáles son sus puntos fuertes y débiles? ¿Cuándo podría incorporarse? (quand pourriez-vous commencer ?)', 'Questions: ¿Por qué quiere este puesto? ¿Cuáles son sus puntos fuertes y débiles? ¿Cuándo podría incorporarse? (when could you start?)'),
      ], [
        S('el-puesto-de-trabajo', 'el puesto de trabajo', ('le poste (de travail)', 'the post, the position')),
        S('la-oferta-de-empleo', 'la oferta de empleo', ('l’offre d’emploi', 'the job offer')),
        S('el-contrato', 'el contrato', ('le contrat', 'the contract')),
        S('jornada-completa', 'a jornada completa / a tiempo parcial', ('à temps plein / à temps partiel', 'full-time / part-time')),
        S('el-sueldo', 'el sueldo', ('le salaire', 'the salary, the wage')),
        S('dominar', 'dominar (un idioma)', ('maîtriser (une langue)', 'to be fluent in (a language)')),
        S('incorporarse', 'incorporarse', ('prendre son poste', 'to start (a job)')),
        S('los-puntos-fuertes', 'los puntos fuertes / débiles', ('les points forts / faibles', 'strengths / weaknesses')),
      ], [
        x('Me encantaría formar parte de su equipo: domino el inglés y tengo cinco años de experiencia.', 'J’aimerais beaucoup faire partie de votre équipe : je maîtrise l’anglais et j’ai cinq ans d’expérience.', 'I would love to join your team: I’m fluent in English and have five years’ experience.'),
        x('Es un contrato indefinido a jornada completa. ¿Cuándo podría incorporarse?', 'C’est un CDI à temps plein. Quand pourriez-vous commencer ?', 'It’s a permanent full-time contract. When could you start?'),
      ], [
        DC(ANSWER, [('Entrevistadora', '¿Por qué quiere este puesto?')], ('La recruteuse te demande pourquoi tu veux ce poste.', 'The interviewer asks why you want this job.'), ['Porque me apasiona el turismo y creo que puedo aportar mucho a su empresa.', 'Porque el sueldo.', 'Porque quería que me lo dieras.'], 'Porque me apasiona el turismo y creo que puedo aportar mucho a su empresa.', ('Motiver sa candidature : intérêt et apport.', 'Explaining your application: interest and contribution.')),
        FB(COMPLETE, 'Busco un trabajo a tiempo ＿, solo por las mañanas.', ['parcial', 'completo', 'fuerte'], 'parcial', ('À temps partiel : a tiempo parcial.', 'Part-time: a tiempo parcial.'), ('Je cherche un travail à temps partiel, seulement le matin.', 'I’m looking for a part-time job, mornings only.')),
        FB(COMPLETE, 'Firmé un ＿ indefinido el mes pasado.', ['contrato', 'sueldo', 'puesto'], 'contrato', ('Le contrat : el contrato.', 'The contract: el contrato.'), ('J’ai signé un CDI le mois dernier.', 'I signed a permanent contract last month.')),
        TF('Podría incorporarme el lunes.', ('Le candidat peut commencer lundi.', 'The candidate can start on Monday.'), VRAI, ('Incorporarse = prendre son poste.', 'Incorporarse = to start a job.')),
      ]),
  ])])

write_level('DELEB2', ('DELE B2 : la traversée des Amériques', 'DELE B2: across the Americas'), REGION, 'Across the Americas', 53,
  [W1, W2, W3, W4, W5, W6, W7, W8, FINAL('DELEB2', REGION, ('Simulation DELE B2 : le théâtre Colón', 'DELE B2 simulation: the Teatro Colón'), 'compréhension écrite, compréhension auditive et expression écrite (l’oral n’est pas évalué)', 'reading comprehension, listening comprehension and written expression (speaking is not assessed)')])

