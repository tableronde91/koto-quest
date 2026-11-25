# Niveau DELE C1 (espagnol, CECRL C1) : 8 étapes dans la Bibliothèque enchantée, leçons et examen blanc (français + anglais).
# Mode histoire : à la Bibliothèque nationale de Madrid, des personnages des classiques espagnols (domaine public) s'échappent des livres.
# Les gardiens portent les signes de la typographie (§, ¶, †, ‡, °, ¤, ‰, ¬).
# Les notions sont en espagnol (front) avec leur sens en français ; la traduction anglaise du sens sert à l'interface en anglais.
# Usage : python3 scripts/delec1-level.py   (réécrit content/delec1/delec1.json ; les DELE A1 à B2 doivent déjà exister)
from es_common import *

REGION = 'Bibliothèque enchantée'

# ═════════════════════════ 1 : le Cantar de mio Cid — les registres, la nominalisation, les collocations ═════════════════════════
W1 = WORLD('delec1-w1', ('Le Cantar de mio Cid', 'The Song of My Cid'), REGION,
  ('Adapter son registre (formel ou familier), transformer des verbes en noms pour un style soutenu et employer les collocations courantes (llevar a cabo, hacer frente a).', 'Adapt your register (formal or informal), turn verbs into nouns for a formal style and use common collocations (llevar a cabo, hacer frente a).'),
  (('Le Lion du Cid', 'The Cid’s Lion'), '§', ('Dans le Cantar de mio Cid, un lion s’échappe de sa cage à Valence et seul le Cid parvient à le calmer. Le voilà sorti du vieux manuscrit, rugissant dans la salle des incunables : parle-lui avec la dignité d’un chevalier, dans le registre qui convient.', 'In the Song of My Cid, a lion escapes from its cage in Valencia and only the Cid manages to calm it. Now it has stepped out of the old manuscript and is roaring in the incunabula room: speak to it with a knight’s dignity, in the right register.')),
  [CH('delec1-w1-c1', ('La salle des incunables', 'The incunabula room'), [
    L('es-registro', ('Formel ou familier : choisir son registre', 'Formal or informal: choosing your register'), ('Identifier et adapter le registre selon la situation et l’interlocuteur.', 'Identify and adapt the register to the situation and the person you’re addressing.'), 10, [
        ('Registre formel : usted, phrases complètes, vocabulaire précis : ¿Sería tan amable de indicarme…? Le ruego que… (je vous prie de…). Registre familier : tú, phrases courtes, mots expressifs : ¿Me dices dónde…?', 'Formal register: usted, full sentences, precise vocabulary: ¿Sería tan amable de indicarme…? Le ruego que… (I kindly ask you to…). Informal register: tú, short sentences, expressive words: ¿Me dices dónde…?'),
        ('Verbes soutenus et leurs équivalents courants : comenzar (empezar), finalizar (acabar), solicitar (pedir), adquirir (comprar), residir (vivir), efectuar (hacer).', 'Formal verbs and their everyday equivalents: comenzar (empezar), finalizar (acabar), solicitar (pedir), adquirir (comprar), residir (vivir), efectuar (hacer).'),
        ('Dirigirse a alguien (s’adresser à quelqu’un) ; tutear (tutoyer) et tratar de usted (vouvoyer).', 'Dirigirse a alguien (to address someone); tutear (to address as tú) and tratar de usted (to address as usted).'),
      ], [
        S('el-registro', 'el registro', ('le registre (de langue)', 'register (of language)')),
        S('le-ruego-que', 'le ruego que…', ('je vous prie de…', 'I kindly ask you to…')),
        S('seria-tan-amable', '¿Sería tan amable de…?', ('Auriez-vous l’amabilité de… ?', 'Would you be so kind as to…?')),
        S('solicitar', 'solicitar', ('solliciter, demander (soutenu)', 'to request, to apply for')),
        S('adquirir', 'adquirir', ('acquérir', 'to acquire')),
        S('residir', 'residir', ('résider', 'to reside')),
        S('tutear', 'tutear / tratar de usted', ('tutoyer / vouvoyer', 'to address as tú / as usted')),
        S('dirigirse-a', 'dirigirse a', ('s’adresser à', 'to address (someone)')),
      ], [
        x('Le ruego que disculpe la molestia: ¿sería tan amable de indicarme dónde se encuentra la sala de manuscritos?', 'Je vous prie d’excuser le dérangement : auriez-vous l’amabilité de m’indiquer où se trouve la salle des manuscrits ?', 'Please excuse the inconvenience: would you be so kind as to tell me where the manuscript room is?'),
        x('En la biblioteca se trata de usted a los bibliotecarios, aunque muchos jóvenes se tutean.', 'À la bibliothèque, on vouvoie les bibliothécaires, même si beaucoup de jeunes se tutoient.', 'In the library people address the librarians as usted, although many young people use tú with each other.'),
      ], [
        FB(CHOOSE, 'Para ＿ la beca, rellene este formulario.', ['solicitar', 'pedir prestado', 'currar'], 'solicitar', ('Registre administratif : solicitar.', 'Administrative register: solicitar.'), ('Pour solliciter la bourse, remplissez ce formulaire.', 'To apply for the grant, fill in this form.')),
        FB(CHOOSE, 'Le ＿ que no utilice el teléfono en la sala.', ['ruego', 'digo tío', 'mola'], 'ruego', ('Demande formelle : le ruego que…', 'Formal request: le ruego que…'), ('Je vous prie de ne pas utiliser votre téléphone dans la salle.', 'I kindly ask you not to use your phone in the room.')),
        DC(ANSWER, [('León', '¿Quién osa despertarme?')], ('Le lion demande qui ose le réveiller ; réponds avec la courtoisie d’un chevalier.', 'The lion asks who dares to wake it; answer with a knight’s courtesy.'), ['Le ruego que me disculpe, noble señor: soy un humilde lector.', '¡Hola, tío! ¿Qué pasa?', 'Nada, que te he despertado.'], 'Le ruego que me disculpe, noble señor: soy un humilde lector.', ('Registre soutenu : le ruego que…', 'Formal register: le ruego que…')),
        TF('«Residir» es más formal que «vivir».', ('Residir appartient au registre soutenu.', 'Residir belongs to the formal register.'), VRAI, ('Residir = vivir, en registre administratif.', 'Residir = vivir, in an administrative register.')),
      ]),
    L('es-nominalizacion', ('La llegada, el aumento : la nominalisation', 'La llegada, el aumento: nominalisation'), ('Transformer des verbes et des adjectifs en noms pour un style écrit et soutenu.', 'Turn verbs and adjectives into nouns for a written, formal style.'), 10, [
        ('Les suffixes de nominalisation : -ción (organizar → la organización), -miento (crecer → el crecimiento), -ada / -ida (llegar → la llegada, salir → la salida), -dad (posible → la posibilidad), -ez / -eza (rápido → la rapidez, bello → la belleza).', 'Nominalisation suffixes: -ción (organizar → la organización), -miento (crecer → el crecimiento), -ada / -ida (llegar → la llegada, salir → la salida), -dad (posible → la posibilidad), -ez / -eza (rápido → la rapidez, bello → la belleza).'),
        ('Style écrit : Cuando llegó el rey… → Tras la llegada del rey… ; Porque aumentaron los precios… → Debido al aumento de los precios…', 'Written style: Cuando llegó el rey… → Tras la llegada del rey…; Porque aumentaron los precios… → Debido al aumento de los precios…'),
        ('Les prépositions qui accompagnent : tras (après), ante (devant, face à), debido a (en raison de), a raíz de (à la suite de).', 'Accompanying prepositions: tras (after), ante (before, faced with), debido a (owing to), a raíz de (following).'),
      ], [
        SG('nominalizacion', '-ción / -miento / -dad', ('suffixes de nominalisation', 'nominalisation suffixes')),
        S('el-crecimiento', 'el crecimiento', ('la croissance', 'growth')),
        S('el-aumento', 'el aumento', ('l’augmentation, la hausse', 'the increase')),
        S('la-llegada', 'la llegada', ('l’arrivée', 'the arrival')),
        S('tras', 'tras', ('après, derrière (soutenu)', 'after, behind (formal)')),
        S('ante', 'ante', ('devant, face à', 'before, in the face of')),
        S('debido-a', 'debido a', ('en raison de, dû à', 'owing to, due to')),
        S('a-raiz-de', 'a raíz de', ('à la suite de', 'following, as a result of')),
      ], [
        x('Tras la llegada del Cid a Valencia, la ciudad vivió un periodo de gran crecimiento.', 'Après l’arrivée du Cid à Valence, la ville connut une période de forte croissance.', 'After the Cid’s arrival in Valencia, the city went through a period of great growth.'),
        x('Debido al aumento del número de lectores, la biblioteca ha ampliado su horario.', 'En raison de l’augmentation du nombre de lecteurs, la bibliothèque a élargi ses horaires.', 'Owing to the increase in the number of readers, the library has extended its opening hours.'),
      ], [
        FB(CHOOSE, 'Tras la ＿ del rey, empezó la fiesta.', ['llegada', 'llegar', 'llegó'], 'llegada', ('Après tras : un nom.', 'After tras: a noun.'), ('Après l’arrivée du roi, la fête commença.', 'After the king’s arrival, the celebration began.')),
        FB(CHOOSE, 'El ＿ de la población preocupa a las autoridades.', ['envejecimiento', 'envejecer', 'envejecido'], 'envejecimiento', ('Envejecer → el envejecimiento.', 'Envejecer → el envejecimiento.'), ('Le vieillissement de la population inquiète les autorités.', 'The ageing of the population worries the authorities.')),
        FB(CHOOSE, 'La ＿ de los trenes sorprendió a todos.', ['rapidez', 'rápida', 'rapidamente'], 'rapidez', ('Adjectif → nom : rápido → la rapidez.', 'Adjective → noun: rápido → la rapidez.'), ('La rapidité des trains a surpris tout le monde.', 'The speed of the trains surprised everyone.')),
        TF('A raíz de la crisis, cerraron varias librerías.', ('Les librairies ont fermé à la suite de la crise.', 'The bookshops closed as a result of the crisis.'), VRAI, ('A raíz de = à la suite de.', 'A raíz de = as a result of.')),
      ]),
  ]),
  CH('delec1-w1-c2', ('Les chevaliers de la langue', 'Knights of language'), [
    L('es-colocaciones', ('Llevar a cabo, hacer frente a : les collocations', 'Llevar a cabo, hacer frente a: collocations'), ('Employer les associations de mots les plus naturelles en espagnol soutenu.', 'Use the most natural word combinations in formal Spanish.'), 9, [
        ('Verbe + nom : llevar a cabo (réaliser), poner en marcha (lancer), tomar medidas (prendre des mesures), hacer frente a (faire face à), dar lugar a (donner lieu à), tener lugar (avoir lieu).', 'Verb + noun: llevar a cabo (to carry out), poner en marcha (to launch), tomar medidas (to take measures), hacer frente a (to face up to), dar lugar a (to give rise to), tener lugar (to take place).'),
        ('Adjectif + nom : grave error, firme decisión, estrecha colaboración (étroite collaboration), amplia mayoría (large majorité).', 'Adjective + noun: grave error, firme decisión, estrecha colaboración (close collaboration), amplia mayoría (large majority).'),
        ('Attention aux faux amis : realizar = réaliser, mais darse cuenta = se rendre compte ; asistir a = assister à (être présent).', 'Watch out for false friends: realizar = to carry out, but darse cuenta = to realise; asistir a = to attend.'),
      ], [
        S('llevar-a-cabo', 'llevar a cabo', ('réaliser, effectuer', 'to carry out')),
        S('poner-en-marcha', 'poner en marcha', ('lancer, mettre en route', 'to launch, to set in motion')),
        S('tomar-medidas', 'tomar medidas', ('prendre des mesures', 'to take measures')),
        S('hacer-frente-a', 'hacer frente a', ('faire face à', 'to face up to')),
        S('dar-lugar-a', 'dar lugar a', ('donner lieu à', 'to give rise to')),
        S('tener-lugar', 'tener lugar', ('avoir lieu', 'to take place')),
        S('darse-cuenta', 'darse cuenta de', ('se rendre compte', 'to realise')),
        S('asistir-a', 'asistir a', ('assister à', 'to attend')),
      ], [
        x('La biblioteca ha puesto en marcha un proyecto para digitalizar el manuscrito del Cantar.', 'La bibliothèque a lancé un projet de numérisation du manuscrit du Cantar.', 'The library has launched a project to digitise the manuscript of the Cantar.'),
        x('La presentación tendrá lugar el jueves; se espera que asistan más de doscientas personas.', 'La présentation aura lieu jeudi ; on attend plus de deux cents personnes.', 'The presentation will take place on Thursday; more than two hundred people are expected to attend.'),
      ], [
        FB(CHOOSE, 'El gobierno tomará ＿ contra la contaminación.', ['medidas', 'pasos de cabo', 'lugares'], 'medidas', ('Tomar medidas = prendre des mesures.', 'Tomar medidas = to take measures.'), ('Le gouvernement prendra des mesures contre la pollution.', 'The government will take measures against pollution.')),
        FB(CHOOSE, 'El congreso ＿ lugar en Salamanca.', ['tendrá', 'dará', 'hará'], 'tendrá', ('Avoir lieu : tener lugar.', 'To take place: tener lugar.'), ('Le congrès aura lieu à Salamanque.', 'The conference will take place in Salamanca.')),
        FB(CHOOSE, 'No me di ＿ de que era tan tarde.', ['cuenta', 'lugar', 'cabo'], 'cuenta', ('Se rendre compte : darse cuenta.', 'To realise: darse cuenta.'), ('Je ne me suis pas rendu compte qu’il était si tard.', 'I didn’t realise it was so late.')),
        TF('Asistí a la conferencia del sábado.', ('La personne a aidé le conférencier.', 'The person helped the speaker.'), FAUX, ('Asistir a = être présent à.', 'Asistir a = to attend.')),
      ]),
  ])])

# ═════════════════════════ 2 : La Célestine — le subjonctif avancé, la persuasion ═════════════════════════
W2 = WORLD('delec1-w2', ('Les ruses de la Célestine', 'The Celestina’s wiles'), REGION,
  ('Maîtriser les emplois avancés du subjonctif (el hecho de que, que yo sepa, sea como sea) et les verbes de la persuasion et de la manipulation.', 'Master advanced uses of the subjunctive (el hecho de que, que yo sepa, sea como sea) and the verbs of persuasion and manipulation.'),
  (('La Célestine', 'The Celestina'), '¶', ('Échappée de la tragicomédie de Fernando de Rojas (1499), la vieille entremetteuse Célestine tisse ses intrigues entre les rayonnages. Elle manie l’art de convaincre mieux que personne : déjoue ses ruses en maîtrisant toutes les nuances du subjonctif.', 'Escaped from Fernando de Rojas’s tragicomedy (1499), the old go-between Celestina weaves her intrigues among the shelves. She is a master of persuasion: foil her schemes by mastering every nuance of the subjunctive.')),
  [CH('delec1-w2-c1', ('Les intrigues de Salamanque', 'Intrigues in Salamanca'), [
    L('es-el-hecho-de-que', ('Le fait que… : el hecho de que, que yo sepa', 'The fact that…: el hecho de que, que yo sepa'), ('Employer le subjonctif après el hecho de que et dans les tournures restrictives.', 'Use the subjunctive after el hecho de que and in restrictive expressions.'), 10, [
        ('El hecho de que + subjonctif quand on commente ou évalue un fait : El hecho de que no haya llamado me preocupa. Même règle avec que en début de phrase : Que llegue tarde no es raro.', 'El hecho de que + subjunctive when commenting on or evaluating a fact: El hecho de que no haya llamado me preocupa. Same rule with que at the start of a sentence: Que llegue tarde no es raro.'),
        ('Tournures restrictives : que yo sepa (autant que je sache), que yo recuerde (autant que je me souvienne), que se sepa (à ce qu’on sache).', 'Restrictive expressions: que yo sepa (as far as I know), que yo recuerde (as far as I remember), que se sepa (as far as anyone knows).'),
        ('Après no es que : No es que no quiera, es que no puedo (ce n’est pas que je ne veuille pas…).', 'After no es que: No es que no quiera, es que no puedo (it’s not that I don’t want to…).'),
      ], [
        SG('el-hecho-de-que', 'el hecho de que + subjuntivo', ('le fait que + subjonctif', 'the fact that + subjunctive')),
        SG('que-yo-sepa', 'que yo sepa', ('autant que je sache', 'as far as I know')),
        S('que-yo-recuerde', 'que yo recuerde', ('autant que je me souvienne', 'as far as I remember')),
        S('no-es-que', 'no es que… es que…', ('ce n’est pas que… c’est que…', 'it’s not that… it’s that…')),
        S('la-intriga', 'la intriga', ('l’intrigue', 'the intrigue, the plot')),
        S('la-alcahueta', 'la alcahueta', ('l’entremetteuse', 'the go-between, the procuress')),
        S('el-hechizo', 'el hechizo', ('le sortilège, l’envoûtement', 'the spell')),
        S('sospechar', 'sospechar', ('soupçonner', 'to suspect')),
      ], [
        x('El hecho de que Celestina conozca a todo el mundo en Salamanca la hace peligrosa.', 'Le fait que Célestine connaisse tout le monde à Salamanque la rend dangereuse.', 'The fact that Celestina knows everyone in Salamanca makes her dangerous.'),
        x('Que yo sepa, nadie ha leído todos los libros de esta sala. — No es que no queramos, es que no hay tiempo.', 'Autant que je sache, personne n’a lu tous les livres de cette salle. — Ce n’est pas que nous ne voulions pas, c’est qu’on n’a pas le temps.', 'As far as I know, nobody has read every book in this room. — It’s not that we don’t want to, it’s that there’s no time.'),
      ], [
        FB(CHOOSE, 'El hecho de que no ＿ me parece sospechoso.', ['conteste', 'contesta', 'contestará'], 'conteste', ('El hecho de que + subjonctif.', 'El hecho de que + subjunctive.'), ('Le fait qu’il ne réponde pas me paraît suspect.', 'The fact that he isn’t answering seems suspicious to me.')),
        FB(CHOOSE, 'Que yo ＿, la biblioteca cierra a las nueve.', ['sepa', 'sé', 'sabía'], 'sepa', ('Tournure figée : que yo sepa.', 'Set phrase: que yo sepa.'), ('Autant que je sache, la bibliothèque ferme à neuf heures.', 'As far as I know, the library closes at nine.')),
        FB(CHOOSE, 'No es que no te ＿, es que estoy ocupado.', ['quiera', 'quiero', 'querré'], 'quiera', ('No es que + subjonctif.', 'No es que + subjunctive.'), ('Ce n’est pas que je ne t’aime pas, c’est que je suis occupé.', 'It’s not that I don’t love you, it’s that I’m busy.')),
        TF('Que yo recuerde, nunca hemos estado aquí.', ('La personne est absolument certaine.', 'The person is absolutely certain.'), FAUX, ('Que yo recuerde nuance l’affirmation.', 'Que yo recuerde hedges the statement.')),
      ]),
    L('es-sea-como-sea', ('Quoi qu’il arrive : sea como sea, pase lo que pase', 'Whatever happens: sea como sea, pase lo que pase'), ('Employer les structures redoublées au subjonctif.', 'Use reduplicated subjunctive structures.'), 10, [
        ('Subjonctif + relatif + même subjonctif = quel que soit… : sea como sea (quoi qu’il en soit), pase lo que pase (quoi qu’il arrive), digan lo que digan (quoi qu’on dise), cueste lo que cueste (coûte que coûte).', 'Subjunctive + relative + same subjunctive = whatever…: sea como sea (be that as it may), pase lo que pase (whatever happens), digan lo que digan (whatever they say), cueste lo que cueste (at all costs).'),
        ('Avec quien, donde, cuando : vayas donde vayas (où que tu ailles), venga quien venga (qui que ce soit qui vienne).', 'With quien, donde, cuando: vayas donde vayas (wherever you go), venga quien venga (whoever comes).'),
        ('Quieras o no (que tu le veuilles ou non), te guste o no (que ça te plaise ou non).', 'Quieras o no (whether you like it or not), te guste o no (like it or not).'),
      ], [
        SG('pase-lo-que-pase', 'pase lo que pase', ('quoi qu’il arrive', 'whatever happens')),
        S('sea-como-sea', 'sea como sea', ('quoi qu’il en soit', 'be that as it may')),
        S('digan-lo-que-digan', 'digan lo que digan', ('quoi qu’on dise', 'whatever people say')),
        S('cueste-lo-que-cueste', 'cueste lo que cueste', ('coûte que coûte', 'at all costs')),
        S('vayas-donde-vayas', 'vayas donde vayas', ('où que tu ailles', 'wherever you go')),
        S('quieras-o-no', 'quieras o no', ('que tu le veuilles ou non', 'whether you like it or not')),
        S('la-astucia', 'la astucia', ('la ruse, l’astuce', 'cunning')),
        S('el-engano', 'el engaño', ('la tromperie', 'deception')),
      ], [
        x('Pase lo que pase, no firmes nada que te dé Celestina.', 'Quoi qu’il arrive, ne signe rien de ce que te donne Célestine.', 'Whatever happens, don’t sign anything Celestina gives you.'),
        x('Digan lo que digan los críticos, La Celestina es una obra maestra.', 'Quoi qu’en disent les critiques, La Célestine est un chef-d’œuvre.', 'Whatever the critics say, La Celestina is a masterpiece.'),
      ], [
        FB(CHOOSE, 'Lo terminaré mañana, ＿ lo que cueste.', ['cueste', 'cuesta', 'costará'], 'cueste', ('Structure redoublée : cueste lo que cueste.', 'Reduplicated structure: cueste lo que cueste.'), ('Je le terminerai demain, coûte que coûte.', 'I’ll finish it tomorrow at all costs.')),
        FB(CHOOSE, 'Vayas donde ＿, te encontraré.', ['vayas', 'vas', 'irás'], 'vayas', ('Où que tu ailles : vayas donde vayas.', 'Wherever you go: vayas donde vayas.'), ('Où que tu ailles, je te trouverai.', 'Wherever you go, I’ll find you.')),
        FB(CHOOSE, 'Sea como ＿, tenemos que decidir hoy.', ['sea', 'es', 'fuera'], 'sea', ('Quoi qu’il en soit : sea como sea.', 'Be that as it may: sea como sea.'), ('Quoi qu’il en soit, nous devons décider aujourd’hui.', 'Be that as it may, we have to decide today.')),
        TF('Quieras o no, mañana vienes conmigo.', ('La personne demande l’avis de l’autre.', 'The person is asking for the other’s opinion.'), FAUX, ('Quieras o no = que tu le veuilles ou non.', 'Quieras o no = whether you like it or not.')),
      ]),
  ]),
  CH('delec1-w2-c2', ('L’art de convaincre', 'The art of persuasion'), [
    L('es-persuasion', ('Convaincre, insinuer, flatter : les verbes de la parole', 'Convincing, hinting, flattering: verbs of speech'), ('Choisir le verbe de parole précis pour rapporter une intention.', 'Choose the precise speech verb to report an intention.'), 9, [
        ('Au-delà de decir : afirmar, sostener (soutenir), insinuar (insinuer), sugerir, advertir (avertir), reprochar, admitir (admettre), reconocer (reconnaître).', 'Beyond decir: afirmar, sostener (to maintain), insinuar (to hint), sugerir, advertir (to warn), reprochar, admitir (to admit), reconocer (to acknowledge).'),
        ('Pour agir sur quelqu’un : convencer de (convaincre de), persuadir, halagar (flatter), engatusar (embobiner, familier), presionar (faire pression).', 'To influence someone: convencer de (to convince to), persuadir, halagar (to flatter), engatusar (to sweet-talk, informal), presionar (to pressure).'),
        ('Attention à la construction : convencer a alguien de algo / de que + subjonctif quand on pousse à agir : La convenció de que se fuera.', 'Watch the construction: convencer a alguien de algo / de que + subjunctive when pushing someone to act: La convenció de que se fuera.'),
      ], [
        S('sostener', 'sostener', ('soutenir (une idée)', 'to maintain, to hold (a view)')),
        S('insinuar', 'insinuar', ('insinuer', 'to insinuate, to hint')),
        S('admitir', 'admitir', ('admettre, avouer', 'to admit')),
        S('reconocer', 'reconocer', ('reconnaître', 'to acknowledge, to recognise')),
        S('convencer', 'convencer de', ('convaincre de', 'to convince (to)')),
        S('halagar', 'halagar', ('flatter', 'to flatter')),
        S('engatusar', 'engatusar', ('embobiner, enjôler', 'to sweet-talk, to cajole')),
        S('presionar', 'presionar', ('faire pression', 'to pressure')),
      ], [
        x('Celestina halagó a Melibea, insinuó que Calisto estaba enfermo y acabó convenciéndola de que lo recibiera.', 'Célestine flatta Mélibée, insinua que Calixte était malade et finit par la convaincre de le recevoir.', 'Celestina flattered Melibea, hinted that Calisto was ill and ended up convincing her to see him.'),
        x('El autor reconoce que la obra es moralizante, aunque sostiene que también es una comedia.', 'L’auteur reconnaît que l’œuvre est moralisatrice, même s’il soutient que c’est aussi une comédie.', 'The author acknowledges that the work is moralising, although he maintains that it is also a comedy.'),
      ], [
        FB(CHOOSE, 'No lo dijo claramente, solo lo ＿.', ['insinuó', 'gritó', 'admitió'], 'insinuó', ('Dire sans dire : insinuar.', 'Saying without saying: insinuar.'), ('Il ne l’a pas dit clairement, il l’a seulement insinué.', 'He didn’t say it clearly, he only hinted at it.')),
        FB(CHOOSE, 'Al final ＿ que se había equivocado.', ['reconoció', 'halagó', 'presionó'], 'reconoció', ('Reconnaître une erreur : reconocer.', 'To acknowledge a mistake: reconocer.'), ('Finalement, il a reconnu qu’il s’était trompé.', 'In the end, he acknowledged he had been wrong.')),
        FB(CHOOSE, 'La convenció de que ＿ la carta.', ['firmara', 'firmaba', 'firmó'], 'firmara', ('Convencer de que (pousser à agir) + subjonctif.', 'Convencer de que (pushing to act) + subjunctive.'), ('Elle l’a convaincue de signer la lettre.', 'She convinced her to sign the letter.')),
        TF('Celestina halagaba a todo el mundo.', ('Célestine disait des choses flatteuses.', 'Celestina said flattering things.'), VRAI, ('Halagar = flatter.', 'Halagar = to flatter.')),
      ]),
  ])])

# ═════════════════════════ 3 : le Lazarillo — expressions idiomatiques, proverbes, ironie ═════════════════════════
W3 = WORLD('delec1-w3', ('Les tours du Lazarillo', 'Lazarillo’s tricks'), REGION,
  ('Comprendre et employer les expressions idiomatiques, les proverbes et l’ironie, si fréquents dans la langue courante.', 'Understand and use idioms, proverbs and irony, so common in everyday Spanish.'),
  (('L’Aveugle du Lazarillo', 'Lazarillo’s Blind Master'), '†', ('Dans le Lazarillo de Tormes (1554), le premier maître de Lázaro est un aveugle rusé qui lui apprend la vie à coups de tours pendables. Sorti du roman, il parle en proverbes et en sous-entendus : comprends son langage imagé, sinon il te jouera un tour.', 'In Lazarillo de Tormes (1554), Lázaro’s first master is a cunning blind man who teaches him about life through dirty tricks. Out of the novel, he speaks in proverbs and innuendo: understand his colourful language, or he’ll play a trick on you.')),
  [CH('delec1-w3-c1', ('Sur le pont de Salamanque', 'On the bridge of Salamanca'), [
    L('es-modismos', ('Meter la pata : les expressions idiomatiques', 'Meter la pata: idioms'), ('Comprendre et employer les expressions idiomatiques les plus courantes.', 'Understand and use the most common idioms.'), 10, [
        ('Expressions avec le corps : meter la pata (faire une gaffe), no tener pelos en la lengua (ne pas mâcher ses mots), costar un ojo de la cara (coûter les yeux de la tête), tomar el pelo (se moquer de quelqu’un).', 'Body idioms: meter la pata (to put your foot in it), no tener pelos en la lengua (not to mince your words), costar un ojo de la cara (to cost an arm and a leg), tomar el pelo (to pull someone’s leg).'),
        ('Autres expressions : estar en las nubes (être dans la lune), ponerse las pilas (se secouer, s’y mettre), dar gato por liebre (rouler quelqu’un), ser pan comido (être du gâteau).', 'Other idioms: estar en las nubes (to have your head in the clouds), ponerse las pilas (to get your act together), dar gato por liebre (to rip someone off), ser pan comido (to be a piece of cake).'),
        ('Ces expressions sont figées : on ne change pas les mots, seulement le temps du verbe : Metí la pata. Me estás tomando el pelo.', 'These expressions are fixed: you don’t change the words, only the verb tense: Metí la pata. Me estás tomando el pelo.'),
      ], [
        S('meter-la-pata', 'meter la pata', ('faire une gaffe', 'to put one’s foot in it')),
        S('tomar-el-pelo', 'tomar el pelo', ('se moquer de quelqu’un, faire marcher', 'to pull someone’s leg')),
        S('pelos-en-la-lengua', 'no tener pelos en la lengua', ('ne pas mâcher ses mots', 'not to mince one’s words')),
        S('ojo-de-la-cara', 'costar un ojo de la cara', ('coûter les yeux de la tête', 'to cost an arm and a leg')),
        S('estar-en-las-nubes', 'estar en las nubes', ('être dans la lune', 'to have one’s head in the clouds')),
        S('ponerse-las-pilas', 'ponerse las pilas', ('se secouer, s’y mettre', 'to get one’s act together')),
        S('gato-por-liebre', 'dar gato por liebre', ('rouler quelqu’un, tromper sur la marchandise', 'to rip someone off')),
        S('pan-comido', 'ser pan comido', ('être du gâteau', 'to be a piece of cake')),
      ], [
        x('El ciego no tenía pelos en la lengua y a Lázaro le tomaba el pelo constantemente.', 'L’aveugle ne mâchait pas ses mots et faisait sans cesse marcher Lázaro.', 'The blind man didn’t mince his words and was constantly pulling Lázaro’s leg.'),
        x('Este manuscrito me costó un ojo de la cara… y creo que me dieron gato por liebre.', 'Ce manuscrit m’a coûté les yeux de la tête… et je crois qu’on m’a roulé.', 'This manuscript cost me an arm and a leg… and I think I was ripped off.'),
      ], [
        FB(CHOOSE, 'Le pregunté por su ex delante de su novia: ¡metí la ＿!', ['pata', 'mano', 'pierna'], 'pata', ('Faire une gaffe : meter la pata.', 'To put your foot in it: meter la pata.'), ('Je lui ai parlé de son ex devant sa copine : j’ai fait une gaffe !', 'I asked him about his ex in front of his girlfriend: I put my foot in it!')),
        FB(CHOOSE, 'El examen fue pan ＿.', ['comido', 'duro', 'caliente'], 'comido', ('Facile : ser pan comido.', 'Easy: ser pan comido.'), ('L’examen était du gâteau.', 'The exam was a piece of cake.')),
        FB(CHOOSE, 'Si quieres aprobar, tienes que ponerte las ＿.', ['pilas', 'botas', 'nubes'], 'pilas', ('S’y mettre : ponerse las pilas.', 'To get your act together: ponerse las pilas.'), ('Si tu veux réussir, il faut t’y mettre.', 'If you want to pass, you need to get your act together.')),
        TF('Siempre está en las nubes.', ('La personne est très attentive.', 'The person is very attentive.'), FAUX, ('Estar en las nubes = être dans la lune.', 'Estar en las nubes = to be daydreaming.')),
      ]),
    L('es-refranes', ('Más vale tarde que nunca : les proverbes', 'Better late than never: proverbs'), ('Comprendre les proverbes courants et savoir les citer à propos.', 'Understand common proverbs and quote them appropriately.'), 9, [
        ('Les refranes condensent une sagesse populaire. On les cite souvent à moitié : «Ya sabes, a quien madruga…» (Dios le ayuda).', 'Refranes condense popular wisdom. People often quote only half: «Ya sabes, a quien madruga…» (Dios le ayuda).'),
        ('Proverbes fréquents : No hay mal que por bien no venga (à quelque chose malheur est bon), En boca cerrada no entran moscas (la parole est d’argent, le silence est d’or), Dime con quién andas y te diré quién eres (dis-moi qui tu fréquentes…).', 'Common proverbs: No hay mal que por bien no venga (every cloud has a silver lining), En boca cerrada no entran moscas (silence is golden), Dime con quién andas y te diré quién eres (you are known by the company you keep).'),
        ('Pour introduire un proverbe : como dice el refrán…, como se suele decir…, ya lo dice el dicho…', 'To introduce a proverb: como dice el refrán…, como se suele decir…, ya lo dice el dicho…'),
      ], [
        S('el-refran', 'el refrán', ('le proverbe', 'the proverb')),
        S('a-quien-madruga', 'a quien madruga, Dios le ayuda', ('l’avenir appartient à ceux qui se lèvent tôt', 'the early bird catches the worm')),
        S('no-hay-mal', 'no hay mal que por bien no venga', ('à quelque chose malheur est bon', 'every cloud has a silver lining')),
        S('en-boca-cerrada', 'en boca cerrada no entran moscas', ('le silence est d’or', 'silence is golden')),
        S('dime-con-quien', 'dime con quién andas y te diré quién eres', ('dis-moi qui tu fréquentes, je te dirai qui tu es', 'a man is known by the company he keeps')),
        S('mas-vale-pajaro', 'más vale pájaro en mano que ciento volando', ('un tiens vaut mieux que deux tu l’auras', 'a bird in the hand is worth two in the bush')),
        S('como-dice-el-refran', 'como dice el refrán', ('comme dit le proverbe', 'as the saying goes')),
        S('el-dicho', 'el dicho', ('le dicton', 'the saying')),
      ], [
        x('Perdí el tren, pero conocí a mi mujer en la estación: no hay mal que por bien no venga.', 'J’ai raté le train, mais j’ai rencontré ma femme à la gare : à quelque chose malheur est bon.', 'I missed the train, but I met my wife at the station: every cloud has a silver lining.'),
        x('Como dice el refrán, más vale pájaro en mano que ciento volando: acepta la oferta.', 'Comme dit le proverbe, un tiens vaut mieux que deux tu l’auras : accepte l’offre.', 'As the saying goes, a bird in the hand is worth two in the bush: take the offer.'),
      ], [
        FB(COMPLETE, 'A quien madruga, Dios le ＿.', ['ayuda', 'ama', 'paga'], 'ayuda', ('Proverbe : a quien madruga, Dios le ayuda.', 'Proverb: a quien madruga, Dios le ayuda.'), ('L’avenir appartient à ceux qui se lèvent tôt.', 'The early bird catches the worm.')),
        FB(COMPLETE, 'En boca cerrada no entran ＿.', ['moscas', 'palabras', 'pájaros'], 'moscas', ('Proverbe : en boca cerrada no entran moscas.', 'Proverb: en boca cerrada no entran moscas.'), ('Le silence est d’or.', 'Silence is golden.')),
        DC(ANSWER, [('Ciego', 'He perdido el trabajo, pero ahora tengo tiempo para escribir mi novela.')], ('L’aveugle te raconte qu’il a perdu son travail mais peut enfin écrire.', 'The blind man tells you he lost his job but can finally write.'), ['Ya lo dice el refrán: no hay mal que por bien no venga.', 'Ya lo dice el refrán: en boca cerrada no entran moscas.', 'Ya lo dice el refrán: dime con quién andas.'], 'Ya lo dice el refrán: no hay mal que por bien no venga.', ('Un malheur qui apporte un bien.', 'A misfortune that brings something good.')),
        TF('Más vale pájaro en mano que ciento volando.', ('Il vaut mieux garder ce qu’on a que viser l’incertain.', 'It’s better to keep what you have than chase uncertainty.'), VRAI, ('Un tiens vaut mieux que deux tu l’auras.', 'A bird in the hand is worth two in the bush.')),
      ]),
  ]),
  CH('delec1-w3-c2', ('Le vin de l’aveugle', 'The blind man’s wine'), [
    L('es-ironia', ('¡Menudo día! : l’ironie et le sous-entendu', '¡Menudo día!: irony and innuendo'), ('Reconnaître l’ironie et les exclamations à double sens.', 'Recognise irony and double-edged exclamations.'), 9, [
        ('L’ironie dit le contraire de ce qu’on pense : ¡Qué bien! ¡Lo que faltaba! (il ne manquait plus que ça !) ¡Pues sí que estamos buenos! (nous voilà bien !).', 'Irony says the opposite of what you think: ¡Qué bien! ¡Lo que faltaba! (that’s all we needed!) ¡Pues sí que estamos buenos! (a fine mess we’re in!).'),
        ('Menudo / menuda + nom = un sacré…, souvent négatif : ¡Menudo día! ¡Menuda suerte! (selon le contexte, chance ou malchance).', 'Menudo / menuda + noun = what a…, often negative: ¡Menudo día! ¡Menuda suerte! (depending on context, good or bad luck).'),
        ('Le ton et le contexte sont essentiels. Pour signaler l’ironie à l’écrit : entre comillas, como quien dice, por así decirlo.', 'Tone and context are essential. To flag irony in writing: entre comillas, como quien dice, por así decirlo.'),
      ], [
        S('la-ironia', 'la ironía', ('l’ironie', 'irony')),
        S('lo-que-faltaba', '¡Lo que faltaba!', ('Il ne manquait plus que ça !', 'That’s all we needed!')),
        S('menudo', '¡Menudo…!', ('Un sacré… ! (exclamation)', 'What a…! (exclamation)')),
        S('estamos-buenos', '¡Pues sí que estamos buenos!', ('Nous voilà bien !', 'A fine mess we’re in!')),
        S('entre-comillas', 'entre comillas', ('entre guillemets', 'in inverted commas, so to speak')),
        S('por-asi-decirlo', 'por así decirlo', ('pour ainsi dire', 'so to speak')),
        S('el-doble-sentido', 'el doble sentido', ('le double sens', 'double meaning')),
        S('el-sarcasmo', 'el sarcasmo', ('le sarcasme', 'sarcasm')),
      ], [
        x('Se rompió la jarra de vino del ciego. — ¡Lo que faltaba! —dijo Lázaro.', 'La cruche de vin de l’aveugle s’est cassée. — Il ne manquait plus que ça ! dit Lázaro.', 'The blind man’s wine jug broke. — That’s all we needed! said Lázaro.'),
        x('Llueve, he perdido las llaves y llego tarde. ¡Menudo día!', 'Il pleut, j’ai perdu mes clés et je suis en retard. Quelle journée !', 'It’s raining, I’ve lost my keys and I’m late. What a day!'),
      ], [
        DC(ANSWER, [('Ciego', 'Se nos ha acabado el pan y empieza a llover.')], ('L’aveugle constate une nouvelle catastrophe ; réagis avec ironie.', 'The blind man notes yet another disaster; react ironically.'), ['¡Lo que faltaba!', '¡Qué buena idea!', '¡Que aproveche!'], '¡Lo que faltaba!', ('Ironie : ¡Lo que faltaba!', 'Irony: ¡Lo que faltaba!')),
        FB(CHOOSE, '¡＿ lío has montado!', ['Menudo', 'Muy', 'Mucho'], 'Menudo', ('Exclamation : ¡Menudo + nom!', 'Exclamation: ¡Menudo + noun!'), ('Tu as fait un sacré bazar !', 'What a mess you’ve made!')),
        TF('¡Qué bien! Otra vez sin luz.', ('La personne est ravie de la coupure.', 'The person is delighted about the power cut.'), FAUX, ('C’est ironique : elle est agacée.', 'It’s ironic: she’s annoyed.')),
        FB(CHOOSE, 'Es un experto, entre ＿: solo ha leído un libro.', ['comillas', 'nubes', 'pilas'], 'comillas', ('Distance ironique : entre comillas.', 'Ironic distance: entre comillas.'), ('C’est un expert, entre guillemets : il n’a lu qu’un livre.', 'He’s an “expert”: he’s only read one book.')),
      ]),
  ])])

# ═════════════════════════ 4 : La vie est un songe — périphrases, notions abstraites, hypothèses ═════════════════════════
W4 = WORLD('delec1-w4', ('La tour de Segismundo', 'Segismundo’s tower'), REGION,
  ('Nuancer avec les périphrases verbales (venir a, andar + gérondif, tener + participe), manier le vocabulaire abstrait et formuler des hypothèses de manière variée.', 'Add nuance with verbal periphrases (venir a, andar + gerund, tener + participle), handle abstract vocabulary and express hypotheses in varied ways.'),
  (('Segismundo enchaîné', 'Segismundo in chains'), '‡', ('Dans La vie est un songe de Calderón (1635), le prince Segismundo grandit enchaîné dans une tour, sans savoir s’il rêve ou s’il vit. Échappé du drame, il doute de tout : réponds-lui en jonglant avec les idées abstraites et les hypothèses.', 'In Calderón’s Life Is a Dream (1635), Prince Segismundo grows up chained in a tower, never knowing whether he is dreaming or awake. Escaped from the play, he doubts everything: answer him by juggling abstract ideas and hypotheses.')),
  [CH('delec1-w4-c1', ('Le songe et la vie', 'Dream and life'), [
    L('es-perifrasis-c1', ('Il finit par dire : les périphrases avancées', 'He ends up saying: advanced periphrases'), ('Employer les périphrases verbales qui nuancent la durée, l’approximation ou le résultat.', 'Use verbal periphrases that express duration, approximation or result.'), 10, [
        ('Venir a + infinitif = à peu près, en somme : Viene a costar cien euros. Esto viene a decir que… Acabar + gérondif = finir par : Acabó aceptando.', 'Venir a + infinitive = roughly, in effect: Viene a costar cien euros. Esto viene a decir que… Acabar + gerund = to end up: Acabó aceptando.'),
        ('Andar + gérondif = passer son temps à (souvent péjoratif) : Anda diciendo mentiras. Ir + gérondif = progression : La biblioteca va creciendo.', 'Andar + gerund = to go around doing (often pejorative): Anda diciendo mentiras. Ir + gerund = gradual progress: La biblioteca va creciendo.'),
        ('Tener + participe = résultat accumulé : Tengo leídos tres capítulos. Llevar + participe : Llevo escritas veinte páginas.', 'Tener + participle = accumulated result: Tengo leídos tres capítulos. Llevar + participle: Llevo escritas veinte páginas.'),
      ], [
        SG('venir-a', 'venir a + infinitivo', ('revenir à, à peu près', 'to amount to, roughly')),
        SG('andar-gerundio', 'andar + gerundio', ('passer son temps à', 'to go around doing')),
        SG('ir-gerundio', 'ir + gerundio', ('peu à peu (progression)', 'to be gradually doing')),
        SG('tener-participio', 'tener + participio', ('avoir (résultat accumulé)', 'to have (accumulated result)')),
        S('acabar-gerundio', 'acabar + gerundio', ('finir par', 'to end up doing')),
        S('el-sueno-y-la-vida', 'la vida es sueño', ('la vie est un songe', 'life is a dream')),
        S('encadenado', 'encadenado / encadenada', ('enchaîné / enchaînée', 'chained')),
        S('la-torre', 'la torre', ('la tour', 'the tower')),
      ], [
        x('Segismundo anda preguntándose si la vida es sueño; al final acaba aceptando que hay que obrar bien.', 'Segismundo passe son temps à se demander si la vie est un songe ; il finit par accepter qu’il faut bien agir.', 'Segismundo keeps wondering whether life is a dream; in the end he comes to accept that one must act well.'),
        x('Tengo leídas casi todas las obras de Calderón, y mi biblioteca va creciendo cada año.', 'J’ai lu presque toutes les œuvres de Calderón, et ma bibliothèque s’agrandit chaque année.', 'I’ve read almost all of Calderón’s plays, and my library keeps growing every year.'),
      ], [
        FB(CHOOSE, 'El viaje viene ＿ costar unos mil euros.', ['a', 'de', 'en'], 'a', ('Approximation : venir a + infinitif.', 'Approximation: venir a + infinitive.'), ('Le voyage revient à environ mille euros.', 'The trip comes to about a thousand euros.')),
        FB(CHOOSE, 'Anda ＿ por ahí que se va a casar.', ['diciendo', 'dicho', 'decir'], 'diciendo', ('Andar + gérondif.', 'Andar + gerund.'), ('Il raconte partout qu’il va se marier.', 'He goes around saying he’s getting married.')),
        FB(CHOOSE, 'Tengo ＿ ya la mitad del libro.', ['leída', 'leído', 'leyendo'], 'leída', ('Tener + participe accordé avec l’objet (la mitad).', 'Tener + participle agreeing with the object (la mitad).'), ('J’ai déjà lu la moitié du livre.', 'I’ve already read half the book.')),
        TF('Al final acabó aceptando la propuesta.', ('Il a refusé jusqu’au bout.', 'He refused to the end.'), FAUX, ('Acabar + gérondif = finir par.', 'Acabar + gerund = to end up.')),
      ]),
    L('es-abstracto', ('La liberté, le destin : le vocabulaire abstrait', 'Freedom, fate: abstract vocabulary'), ('Parler d’idées abstraites et philosophiques avec précision.', 'Talk precisely about abstract and philosophical ideas.'), 9, [
        ('Notions : la libertad, el libre albedrío (le libre arbitre), la conciencia (la conscience), el destino, la realidad, la apariencia, la verdad, el sentido de la vida.', 'Notions: la libertad, el libre albedrío (free will), la conciencia (conscience, consciousness), el destino, la realidad, la apariencia, la verdad, el sentido de la vida.'),
        ('Le neutre lo + adjectif = ce qui est… : lo importante (l’important), lo bueno, lo real, lo de ayer (l’affaire d’hier). Lo + adjectif + que = à quel point : No sabes lo difícil que es.', 'Neuter lo + adjective = the … thing: lo importante (what matters), lo bueno, lo real, lo de ayer (yesterday’s business). Lo + adjective + que = how …: No sabes lo difícil que es.'),
        ('Verbes de la réflexion : plantearse (se poser une question), cuestionar (remettre en question), reflexionar sobre, suponer, concebir.', 'Verbs of reflection: plantearse (to consider, to ask oneself), cuestionar (to question), reflexionar sobre, suponer, concebir.'),
      ], [
        S('el-libre-albedrio', 'el libre albedrío', ('le libre arbitre', 'free will')),
        S('la-conciencia', 'la conciencia', ('la conscience', 'conscience, consciousness')),
        S('la-apariencia', 'la apariencia', ('l’apparence', 'appearance')),
        SG('lo-adjetivo', 'lo + adjetivo', ('ce qui est… (neutre lo)', 'the … thing (neuter lo)')),
        S('lo-que-es', 'lo + adjetivo + que', ('à quel point…', 'how … (it is)')),
        S('plantearse', 'plantearse', ('se poser (une question), envisager', 'to ask oneself, to consider')),
        S('cuestionar', 'cuestionar', ('remettre en question', 'to question')),
        S('concebir', 'concebir', ('concevoir', 'to conceive')),
      ], [
        x('Lo interesante de la obra es que cuestiona la frontera entre la realidad y la apariencia.', 'Ce qui est intéressant dans l’œuvre, c’est qu’elle remet en question la frontière entre la réalité et l’apparence.', 'What’s interesting about the play is that it questions the boundary between reality and appearance.'),
        x('No sabes lo difícil que es plantearse el sentido de la vida encerrado en una torre.', 'Tu ne sais pas à quel point il est difficile de s’interroger sur le sens de la vie enfermé dans une tour.', 'You have no idea how hard it is to wonder about the meaning of life locked up in a tower.'),
      ], [
        FB(CHOOSE, '＿ importante es no rendirse.', ['Lo', 'El', 'La'], 'Lo', ('Neutre : lo + adjectif.', 'Neuter: lo + adjective.'), ('L’important, c’est de ne pas abandonner.', 'What matters is not giving up.')),
        FB(CHOOSE, 'No te imaginas lo ＿ que es este libro.', ['largo', 'larga', 'largos'], 'largo', ('Lo + adjectif accordé avec le sujet (este libro).', 'Lo + adjective agreeing with the subject (este libro).'), ('Tu n’imagines pas à quel point ce livre est long.', 'You can’t imagine how long this book is.')),
        FB(COMPLETE, 'Segismundo se ＿ si está despierto o soñando.', ['plantea', 'concibe', 'cuestiona'], 'plantea', ('Se poser la question : plantearse.', 'To ask oneself: plantearse.'), ('Segismundo se demande s’il est éveillé ou s’il rêve.', 'Segismundo wonders whether he is awake or dreaming.')),
        TF('Tenemos libre albedrío.', ('On affirme que nous pouvons choisir librement.', 'The claim is that we can choose freely.'), VRAI, ('Libre albedrío = libre arbitre.', 'Libre albedrío = free will.')),
      ]),
  ]),
  CH('delec1-w4-c2', ('Et si tout n’était qu’un rêve ?', 'What if it were all a dream?'), [
    L('es-hipotesis-c1', ('À supposer que… : les hypothèses variées', 'Supposing that…: varied hypotheses'), ('Varier l’expression de l’hypothèse au-delà de si.', 'Vary the way you express hypotheses beyond si.'), 10, [
        ('En el supuesto de que / suponiendo que / en caso de que + subjonctif : En el supuesto de que fuera verdad, ¿qué harías?', 'En el supuesto de que / suponiendo que / en caso de que + subjunctive: En el supuesto de que fuera verdad, ¿qué harías?'),
        ('Infinitif ou gérondif à valeur d’hypothèse : De seguir así, perderemos (si ça continue ainsi…). A juzgar por… (à en juger par). Estudiando más, aprobarías (en étudiant plus…).', 'Infinitive or gerund as a hypothesis: De seguir así, perderemos (if things go on like this…). A juzgar por… (judging by). Estudiando más, aprobarías (if you studied more…).'),
        ('Con + infinitif = rien qu’à, il suffit de : Con leer el prólogo, basta. Hypothèse ironique : ¡Ni que fuera un rey!', 'Con + infinitive = just by…, it’s enough to: Con leer el prólogo, basta. Ironic hypothesis: ¡Ni que fuera un rey!'),
      ], [
        SG('en-el-supuesto', 'en el supuesto de que', ('dans l’hypothèse où, à supposer que', 'in the event that, supposing')),
        SG('de-infinitivo', 'de + infinitivo (hipótesis)', ('si… (hypothèse à l’infinitif)', 'if… (infinitive hypothesis)')),
        S('suponiendo-que', 'suponiendo que', ('en supposant que', 'assuming that')),
        S('a-juzgar-por', 'a juzgar por', ('à en juger par', 'judging by')),
        S('con-infinitivo', 'con + infinitivo', ('rien qu’en, il suffit de', 'just by, it is enough to')),
        S('la-hipotesis', 'la hipótesis', ('l’hypothèse', 'the hypothesis')),
        S('despertar', 'despertar', ('réveiller, s’éveiller', 'to wake (up)')),
        S('la-ilusion', 'la ilusión', ('l’illusion, l’enthousiasme', 'illusion, excitement')),
      ], [
        x('En el supuesto de que todo fuera un sueño, ¿seguirías obrando bien?', 'À supposer que tout soit un rêve, continuerais-tu à bien agir ?', 'Supposing it were all a dream, would you still do the right thing?'),
        x('De seguir encerrado en la torre, Segismundo nunca conocería el mundo; a juzgar por su ira, tampoco estaría preparado.', 'S’il restait enfermé dans la tour, Segismundo ne connaîtrait jamais le monde ; à en juger par sa colère, il n’y serait pas prêt non plus.', 'If he stayed locked in the tower, Segismundo would never know the world; judging by his anger, he wouldn’t be ready for it either.'),
      ], [
        FB(CHOOSE, 'En el supuesto de que ＿ tarde, empezad sin mí.', ['llegue', 'llego', 'llegaré'], 'llegue', ('En el supuesto de que + subjonctif.', 'En el supuesto de que + subjunctive.'), ('Au cas où j’arriverais en retard, commencez sans moi.', 'In the event that I’m late, start without me.')),
        FB(CHOOSE, '＿ seguir así, no terminaremos nunca.', ['De', 'Con', 'A'], 'De', ('Hypothèse : de + infinitif.', 'Hypothesis: de + infinitive.'), ('Si ça continue comme ça, nous ne finirons jamais.', 'If we go on like this, we’ll never finish.')),
        FB(CHOOSE, '＿ por su cara, no le ha gustado la noticia.', ['A juzgar', 'Juzgando de', 'De juzgar'], 'A juzgar', ('À en juger par : a juzgar por.', 'Judging by: a juzgar por.'), ('À en juger par sa tête, la nouvelle ne lui a pas plu.', 'Judging by his face, he didn’t like the news.')),
        TF('Con leer el resumen, basta.', ('Il faut lire tout le livre.', 'You have to read the whole book.'), FAUX, ('Con + infinitif = il suffit de.', 'Con + infinitive = it’s enough to.')),
      ]),
  ])])

# ═════════════════════════ 5 : le Licencié de verre — la science, les prépositions, por et para ═════════════════════════
W5 = WORLD('delec1-w5', ('Le Licencié de verre', 'The Glass Graduate'), REGION,
  ('Parler de science et de recherche, maîtriser les verbes à préposition (consistir en, contar con, tratarse de) et les emplois avancés de por et para.', 'Talk about science and research, master verbs with fixed prepositions (consistir en, contar con, tratarse de) and advanced uses of por and para.'),
  (('Le Licencié de verre', 'The Glass Graduate'), '°', ('Dans la nouvelle exemplaire de Cervantes (1613), Tomás Rodaja, brillant étudiant de Salamanque, se croit fait de verre après avoir mangé un coing ensorcelé. Il répond à tout avec une précision redoutable : sois aussi précis que lui, à la préposition près.', 'In Cervantes’s exemplary novel (1613), Tomás Rodaja, a brilliant student at Salamanca, believes he is made of glass after eating a bewitched quince. He answers everything with fearsome precision: be as precise as he is, down to the last preposition.')),
  [CH('delec1-w5-c1', ('Le laboratoire de Salamanque', 'The Salamanca laboratory'), [
    L('es-ciencia', ('La recherche : la hipótesis, el hallazgo', 'Research: la hipótesis, el hallazgo'), ('Comprendre et présenter une découverte scientifique.', 'Understand and present a scientific discovery.'), 9, [
        ('La recherche : la investigación, el investigador, el hallazgo (la découverte), el experimento, los resultados, la muestra (l’échantillon), el estudio.', 'Research: la investigación, el investigador, el hallazgo (the finding), el experimento, los resultados, la muestra (the sample), el estudio.'),
        ('Verbes : demostrar (démontrer), comprobar (vérifier), analizar, plantear una hipótesis (formuler), refutar, confirmar, publicar.', 'Verbs: demostrar (to prove), comprobar (to check), analizar, plantear una hipótesis (to put forward), refutar, confirmar, publicar.'),
        ('Pour rapporter un résultat avec prudence : según el estudio, los datos sugieren que…, todo parece indicar que…, cabe la posibilidad de que + subjonctif.', 'To report a result cautiously: según el estudio, los datos sugieren que…, todo parece indicar que…, cabe la posibilidad de que + subjunctive.'),
      ], [
        S('la-investigacion', 'la investigación', ('la recherche', 'research')),
        S('el-hallazgo', 'el hallazgo', ('la découverte', 'the finding, the discovery')),
        S('la-muestra', 'la muestra', ('l’échantillon', 'the sample')),
        S('demostrar', 'demostrar', ('démontrer', 'to demonstrate, to prove')),
        S('comprobar', 'comprobar', ('vérifier', 'to check, to verify')),
        S('refutar', 'refutar', ('réfuter', 'to refute')),
        S('todo-parece-indicar', 'todo parece indicar que…', ('tout semble indiquer que…', 'everything seems to suggest that…')),
        S('cabe-la-posibilidad', 'cabe la posibilidad de que', ('il est possible que', 'it is possible that')),
      ], [
        x('Según el estudio, los datos sugieren que leer en voz alta mejora la memoria, aunque aún hay que comprobarlo con una muestra mayor.', 'Selon l’étude, les données suggèrent que lire à voix haute améliore la mémoire, même s’il faut encore le vérifier sur un échantillon plus large.', 'According to the study, the data suggest that reading aloud improves memory, although it still needs to be checked with a larger sample.'),
        x('Todo parece indicar que el hallazgo cambiará la historia de la medicina.', 'Tout semble indiquer que la découverte changera l’histoire de la médecine.', 'Everything seems to suggest that the discovery will change the history of medicine.'),
      ], [
        FB(COMPLETE, 'El ＿ de una nueva especie sorprendió a los científicos.', ['hallazgo', 'hallar', 'hallado'], 'hallazgo', ('La découverte : el hallazgo.', 'The finding: el hallazgo.'), ('La découverte d’une nouvelle espèce a surpris les scientifiques.', 'The discovery of a new species surprised the scientists.')),
        FB(COMPLETE, 'Los resultados ＿ la hipótesis: era falsa.', ['refutaron', 'comprobaron', 'publicaron'], 'refutaron', ('Prouver que c’est faux : refutar.', 'To prove false: refutar.'), ('Les résultats ont réfuté l’hypothèse : elle était fausse.', 'The results refuted the hypothesis: it was false.')),
        FB(CHOOSE, 'Cabe la posibilidad de que el estudio ＿ errores.', ['contenga', 'contiene', 'contendrá'], 'contenga', ('Cabe la posibilidad de que + subjonctif.', 'Cabe la posibilidad de que + subjunctive.'), ('Il est possible que l’étude contienne des erreurs.', 'It’s possible that the study contains errors.')),
        TF('Todo parece indicar que es cierto.', ('C’est une certitude absolue.', 'It is an absolute certainty.'), FAUX, ('C’est prudent : tout semble l’indiquer.', 'It’s cautious: everything seems to suggest it.')),
      ]),
    L('es-preposiciones', ('Consistir en, contar con : les verbes à préposition', 'Consistir en, contar con: verbs with prepositions'), ('Employer la bonne préposition après les verbes les plus fréquents.', 'Use the right preposition after the most frequent verbs.'), 10, [
        ('Con en : consistir en (consister à), confiar en (faire confiance à), fijarse en (remarquer), insistir en, quedar en (convenir de), tardar en (mettre du temps à).', 'With en: consistir en (to consist of), confiar en (to trust), fijarse en (to notice), insistir en, quedar en (to agree to), tardar en (to take time to).'),
        ('Con de : tratarse de (s’agir de), depender de, acordarse de, darse cuenta de, encargarse de (se charger de). Con con : contar con (compter sur, disposer de), soñar con, casarse con.', 'With de: tratarse de (to be about), depender de, acordarse de, darse cuenta de, encargarse de (to take charge of). With con: contar con (to count on, to have), soñar con, casarse con.'),
        ('Con a : atreverse a (oser), negarse a (refuser de), dedicarse a, aprender a. Devant que, on garde la préposition : Confío en que vengas.', 'With a: atreverse a (to dare), negarse a (to refuse to), dedicarse a, aprender a. Before que, keep the preposition: Confío en que vengas.'),
      ], [
        SG('consistir-en', 'consistir en / confiar en', ('consister à / faire confiance à', 'to consist of / to trust')),
        SG('tratarse-de', 'tratarse de', ('s’agir de', 'to be about, to be a matter of')),
        S('contar-con', 'contar con', ('compter sur, disposer de', 'to count on, to have')),
        S('fijarse-en', 'fijarse en', ('remarquer, faire attention à', 'to notice, to pay attention to')),
        S('encargarse-de', 'encargarse de', ('se charger de', 'to take charge of')),
        S('atreverse-a', 'atreverse a', ('oser', 'to dare (to)')),
        S('negarse-a', 'negarse a', ('refuser de', 'to refuse (to)')),
        S('tardar-en', 'tardar en', ('mettre du temps à', 'to take (time) to')),
      ], [
        x('El experimento consiste en medir la resistencia del vidrio; se trata de un estudio pionero.', 'L’expérience consiste à mesurer la résistance du verre ; il s’agit d’une étude pionnière.', 'The experiment consists of measuring the strength of glass; it is a pioneering study.'),
        x('Tomás se negaba a que nadie lo tocara y no se atrevía a salir sin protección.', 'Tomás refusait que quiconque le touche et n’osait pas sortir sans protection.', 'Tomás refused to let anyone touch him and didn’t dare go out unprotected.'),
      ], [
        FB(CHOOSE, 'El trabajo consiste ＿ traducir manuscritos.', ['en', 'de', 'a'], 'en', ('Consistir en.', 'Consistir en.'), ('Le travail consiste à traduire des manuscrits.', 'The job consists of translating manuscripts.')),
        FB(CHOOSE, 'Puedes contar ＿ mi ayuda.', ['con', 'en', 'de'], 'con', ('Contar con.', 'Contar con.'), ('Tu peux compter sur mon aide.', 'You can count on my help.')),
        FB(CHOOSE, 'No me atrevo ＿ decírselo.', ['a', 'de', 'en'], 'a', ('Atreverse a.', 'Atreverse a.'), ('Je n’ose pas le lui dire.', 'I don’t dare tell him.')),
        FB(CHOOSE, 'Confío ＿ que todo salga bien.', ['en', 'de', 'con'], 'en', ('On garde la préposition devant que : confiar en que.', 'Keep the preposition before que: confiar en que.'), ('J’ai confiance que tout se passera bien.', 'I trust that everything will go well.')),
      ]),
  ]),
  CH('delec1-w5-c2', ('Fragile comme le verre', 'Fragile as glass'), [
    L('es-por-para-c1', ('Estar por, para colmo : por et para avancés', 'Estar por, para colmo: advanced por and para'), ('Employer les emplois avancés et les locutions de por et para.', 'Use advanced uses and fixed phrases with por and para.'), 9, [
        ('Estar por + infinitif = être à faire, ou être tenté de : La casa está por limpiar. Estoy por irme. Estar para + infinitif = être sur le point de : El tren está para salir.', 'Estar por + infinitive = still to be done, or to be tempted to: La casa está por limpiar. Estoy por irme. Estar para + infinitive = to be about to: El tren está para salir.'),
        ('Por = en échange de, au nom de, selon : Lo cambio por otro. Lo hago por ti. Por lo visto (apparemment), por si fuera poco (comme si ça ne suffisait pas).', 'Por = in exchange for, for the sake of, apparently: Lo cambio por otro. Lo hago por ti. Por lo visto (apparently), por si fuera poco (on top of everything).'),
        ('Para = point de vue, comparaison : Para mí, es un error. Para ser tan joven, sabe mucho. Para colmo (pour couronner le tout), para siempre.', 'Para = point of view, comparison: Para mí, es un error. Para ser tan joven, sabe mucho. Para colmo (to cap it all), para siempre (forever).'),
      ], [
        SG('estar-por', 'estar por + infinitivo', ('rester à faire, être tenté de', 'to be still to be done, to be inclined to')),
        SG('estar-para', 'estar para + infinitivo', ('être sur le point de', 'to be about to')),
        S('por-lo-visto', 'por lo visto', ('apparemment', 'apparently, it seems')),
        S('por-si-fuera-poco', 'por si fuera poco', ('comme si ça ne suffisait pas', 'on top of everything')),
        S('para-colmo', 'para colmo', ('pour couronner le tout', 'to cap it all')),
        S('para-ser', 'para ser + adjetivo', ('pour quelqu’un de…', 'for someone who is…')),
        S('fragil', 'frágil', ('fragile', 'fragile')),
        S('el-vidrio', 'el vidrio', ('le verre (matière)', 'glass (material)')),
      ], [
        x('Por lo visto, Tomás creía ser de vidrio; para colmo, nadie podía acercarse a él.', 'Apparemment, Tomás croyait être de verre ; pour couronner le tout, personne ne pouvait l’approcher.', 'Apparently Tomás believed he was made of glass; to cap it all, nobody could come near him.'),
        x('Para ser tan frágil, tenía respuestas muy duras. — Y el libro sobre él todavía está por escribir.', 'Pour quelqu’un d’aussi fragile, il avait des réponses très dures. — Et le livre sur lui reste à écrire.', 'For someone so fragile, he gave very harsh answers. — And the book about him is still to be written.'),
      ], [
        FB(CHOOSE, 'La tesis todavía está ＿ terminar.', ['por', 'para', 'de'], 'por', ('Reste à faire : estar por.', 'Still to be done: estar por.'), ('La thèse reste encore à terminer.', 'The thesis is still to be finished.')),
        FB(CHOOSE, '＿ ser su primer libro, está muy bien escrito.', ['Para', 'Por', 'De'], 'Para', ('Comparaison : para ser…', 'Comparison: para ser…'), ('Pour un premier livre, il est très bien écrit.', 'For a first book, it’s very well written.')),
        FB(CHOOSE, 'Perdí las llaves y, para ＿, empezó a llover.', ['colmo', 'siempre', 'visto'], 'colmo', ('Pour couronner le tout : para colmo.', 'To cap it all: para colmo.'), ('J’ai perdu mes clés et, pour couronner le tout, il s’est mis à pleuvoir.', 'I lost my keys and, to cap it all, it started to rain.')),
        TF('Por lo visto, mañana no hay clase.', ('L’information est présentée comme une rumeur.', 'The information is presented as hearsay.'), VRAI, ('Por lo visto = apparemment.', 'Por lo visto = apparently.')),
      ]),
  ])])

# ═════════════════════════ 6 : Don Juan Tenorio — l'oral familier, les marqueurs, l'intensité ═════════════════════════
W6 = WORLD('delec1-w6', ('La statue du Commandeur', 'The Commander’s statue'), REGION,
  ('Comprendre l’oral spontané : marqueurs de discours (o sea, pues, vamos), registre familier d’Espagne et intensificateurs (de lo más, la mar de, un montón).', 'Understand spontaneous speech: discourse markers (o sea, pues, vamos), informal Spanish from Spain and intensifiers (de lo más, la mar de, un montón).'),
  (('Le Commandeur de pierre', 'The Stone Commander'), '¤', ('Dans le Don Juan Tenorio de Zorrilla (1844), la statue de pierre du Commandeur s’anime pour venir chercher le séducteur. Échappée de la scène, elle erre dans la bibliothèque et n’écoute que ceux qui parlent comme dans la rue : montre-lui que tu comprends l’espagnol de tous les jours.', 'In Zorrilla’s Don Juan Tenorio (1844), the Commander’s stone statue comes to life to fetch the seducer. Escaped from the stage, it roams the library and only listens to those who talk like people in the street: show it you understand everyday Spanish.')),
  [CH('delec1-w6-c1', ('Le cimetière de Séville', 'The Seville cemetery'), [
    L('es-marcadores-orales', ('O sea, pues, vamos : les marqueurs de l’oral', 'O sea, pues, vamos: spoken discourse markers'), ('Comprendre et employer les marqueurs typiques de la conversation.', 'Understand and use typical conversation markers.'), 10, [
        ('Reformuler : o sea (c’est-à-dire, bref), es decir, mejor dicho (ou plutôt), vamos (enfin, bref) : Es caro, o sea, no lo compro.', 'Rephrasing: o sea (I mean, so), es decir, mejor dicho (or rather), vamos (well, I mean): Es caro, o sea, no lo compro.'),
        ('Commencer ou réagir : pues (eh bien), bueno (bon), mira (écoute), oye (dis donc), ¿sabes? (tu vois ?), ¿no? (n’est-ce pas ?).', 'Starting or reacting: pues (well), bueno (OK, well), mira (look), oye (hey), ¿sabes? (you know?), ¿no? (right?).'),
        ('Gagner du temps et nuancer : a ver (voyons), digamos (disons), en plan… (genre…, familier), total, que… (bref).', 'Buying time and hedging: a ver (let’s see), digamos (let’s say), en plan… (like…, informal), total, que… (anyway).'),
      ], [
        S('o-sea', 'o sea', ('c’est-à-dire, bref', 'I mean, in other words')),
        S('mejor-dicho', 'mejor dicho', ('ou plutôt', 'or rather')),
        S('vamos-marcador', 'vamos (marcador)', ('enfin, bref (marqueur)', 'well, I mean (marker)')),
        S('pues', 'pues', ('eh bien, alors', 'well, then')),
        S('mira-oye', 'mira / oye', ('écoute / dis donc', 'look / hey')),
        S('a-ver', 'a ver', ('voyons', 'let’s see')),
        S('digamos', 'digamos', ('disons', 'let’s say')),
        S('total-que', 'total, que…', ('bref, au final…', 'anyway, in the end…')),
      ], [
        x('A ver, la estatua se movió, o sea, yo la vi moverse… bueno, digamos que eso me pareció.', 'Voyons, la statue a bougé, enfin, je l’ai vue bouger… bon, disons que c’est ce qu’il m’a semblé.', 'Let’s see, the statue moved, I mean, I saw it move… well, let’s say that’s what it looked like.'),
        x('Llegué tarde, no había nadie, empezó a llover… total, que me volví a casa.', 'Je suis arrivé en retard, il n’y avait personne, il s’est mis à pleuvoir… bref, je suis rentré chez moi.', 'I arrived late, there was nobody there, it started raining… anyway, I went back home.'),
      ], [
        FB(CHOOSE, 'No tengo dinero, ＿, que no voy al concierto.', ['o sea', 'mira', 'a ver'], 'o sea', ('Conséquence reformulée : o sea.', 'Rephrased consequence: o sea.'), ('Je n’ai pas d’argent, bref, je ne vais pas au concert.', 'I’ve got no money, so I’m not going to the concert.')),
        FB(CHOOSE, 'Es el lunes, ＿ dicho, el martes.', ['mejor', 'o', 'pues'], 'mejor', ('Se corriger : mejor dicho.', 'Correcting yourself: mejor dicho.'), ('C’est lundi, ou plutôt mardi.', 'It’s Monday, or rather Tuesday.')),
        DC(ANSWER, [('Comendador', '¿Y qué pasó después con Don Juan?')], ('La statue veut connaître la suite ; résume une longue histoire.', 'The statue wants to know what happened next; sum up a long story.'), ['Pues… total, que al final se arrepintió.', 'Mejor dicho total pues que.', 'Oye, digamos, ¿no?'], 'Pues… total, que al final se arrepintió.', ('Résumer : total, que…', 'Summing up: total, que…')),
        TF('A ver, déjame pensar.', ('La personne prend le temps de réfléchir.', 'The person is taking time to think.'), VRAI, ('A ver = voyons.', 'A ver = let’s see.')),
      ]),
    L('es-coloquial', ('Currar, molar, flipar : l’espagnol familier d’Espagne', 'Currar, molar, flipar: informal Spanish from Spain'), ('Comprendre le vocabulaire familier courant en Espagne.', 'Understand common informal vocabulary in Spain.'), 9, [
        ('Verbes familiers : currar (bosser), molar (plaire, être cool : me mola), flipar (halluciner, adorer), pillar (attraper, piger), liarse (s’embrouiller, se lancer).', 'Informal verbs: currar (to work), molar (to be cool: me mola), flipar (to be amazed, to love), pillar (to catch, to get it), liarse (to get muddled, to get carried away).'),
        ('Noms et adjectifs : la pasta (le fric), el curro (le boulot), guay (génial), un rollo (un truc ennuyeux, une histoire), tío / tía (mec / nana, mon vieux).', 'Nouns and adjectives: la pasta (cash), el curro (the job), guay (cool), un rollo (a drag, a thing), tío / tía (mate, dude).'),
        ('À éviter à l’écrit formel et avec des inconnus : on reconnaît ces mots, on les emploie avec prudence.', 'Avoid in formal writing and with strangers: recognise these words, use them with care.'),
      ], [
        S('currar', 'currar', ('bosser (familier)', 'to work (informal)')),
        S('molar', 'molar', ('plaire, être cool (familier)', 'to be cool, to like (informal)')),
        S('flipar', 'flipar', ('halluciner, adorer (familier)', 'to be amazed, to love (informal)')),
        S('pillar', 'pillar', ('attraper, piger (familier)', 'to catch, to get it (informal)')),
        S('la-pasta', 'la pasta', ('le fric (familier)', 'cash, dough (informal)')),
        S('guay', 'guay', ('génial, cool (familier)', 'cool, great (informal)')),
        S('un-rollo', 'un rollo', ('un truc ennuyeux, une histoire', 'a drag, a thing (informal)')),
        S('tio-tia', 'tío / tía', ('mec / nana, mon vieux (familier)', 'mate, dude (informal)')),
      ], [
        x('Tío, la obra de teatro me molaba, pero el final fue un rollo.', 'Mec, la pièce me plaisait, mais la fin était barbante.', 'Mate, I was enjoying the play, but the ending was a drag.'),
        x('Curro todo el día y no tengo pasta para nada. — ¡Qué rollo!', 'Je bosse toute la journée et je n’ai de fric pour rien. — Quelle galère !', 'I work all day and have no cash for anything. — What a drag!'),
      ], [
        FB(CHOOSE, '¡Este museo me ＿! Es guay.', ['mola', 'curra', 'pilla'], 'mola', ('Plaire : molar.', 'To like: molar.'), ('Ce musée me plaît trop ! Il est génial.', 'I love this museum! It’s cool.')),
        FB(CHOOSE, 'No tengo ＿ para el viaje.', ['pasta', 'rollo', 'guay'], 'pasta', ('L’argent : la pasta.', 'Money: la pasta.'), ('Je n’ai pas le fric pour le voyage.', 'I haven’t got the cash for the trip.')),
        FB(CHOOSE, '¿Lo has ＿? — Sí, ya lo entiendo.', ['pillado', 'molado', 'flipado'], 'pillado', ('Comprendre : pillar.', 'To get it: pillar.'), ('Tu as pigé ? — Oui, je comprends maintenant.', 'Did you get it? — Yes, I understand now.')),
        TF('En una carta formal se puede escribir «tío».', ('Le mot convient à une lettre formelle.', 'The word suits a formal letter.'), FAUX, ('Tío est familier.', 'Tío is informal.')),
      ]),
  ]),
  CH('delec1-w6-c2', ('Le festin de pierre', 'The stone banquet'), [
    L('es-intensificadores', ('De lo más, la mar de : intensifier', 'De lo más, la mar de: intensifying'), ('Renforcer ou atténuer un adjectif ou une quantité avec naturel.', 'Strengthen or tone down an adjective or a quantity naturally.'), 9, [
        ('Intensifier un adjectif : de lo más + adjectif (on ne peut plus), la mar de (vraiment, familier), súper / re- / requete- (familier) : Es de lo más interesante. Estaba la mar de contento.', 'Intensifying an adjective: de lo más + adjective (extremely), la mar de (really, informal), súper / re- / requete- (informal): Es de lo más interesante. Estaba la mar de contento.'),
        ('Les quantités : un montón de (plein de), la tira de (des tas de, familier), a montones (à la pelle), ni uno (pas un seul).', 'Quantities: un montón de (loads of), la tira de (tons of, informal), a montones (by the dozen), ni uno (not a single one).'),
        ('Atténuer : un tanto (un peu), algo (assez), más bien (plutôt), no del todo (pas tout à fait) : Es más bien aburrido.', 'Toning down: un tanto (somewhat), algo (rather), más bien (rather), no del todo (not entirely): Es más bien aburrido.'),
      ], [
        SG('de-lo-mas', 'de lo más + adjetivo', ('on ne peut plus…', 'extremely…, most…')),
        S('la-mar-de', 'la mar de + adjetivo', ('vraiment, drôlement (familier)', 'really, ever so (informal)')),
        S('un-monton-de', 'un montón de', ('plein de, un tas de', 'loads of')),
        S('a-montones', 'a montones', ('à la pelle', 'by the dozen, in heaps')),
        S('mas-bien', 'más bien', ('plutôt', 'rather')),
        S('un-tanto', 'un tanto', ('un peu, quelque peu', 'somewhat')),
        S('no-del-todo', 'no del todo', ('pas tout à fait', 'not entirely')),
        S('requete', 'requete- / re- (prefijo)', ('archi-, super- (préfixe familier)', 'really, super- (informal prefix)')),
      ], [
        x('La cena con la estatua fue de lo más extraña: había un montón de velas y nadie comía.', 'Le dîner avec la statue fut on ne peut plus étrange : il y avait plein de bougies et personne ne mangeait.', 'Dinner with the statue was most strange: there were loads of candles and nobody ate.'),
        x('Don Juan estaba la mar de tranquilo, aunque el ambiente era más bien inquietante.', 'Don Juan était drôlement tranquille, même si l’ambiance était plutôt inquiétante.', 'Don Juan was ever so calm, although the atmosphere was rather unsettling.'),
      ], [
        FB(CHOOSE, 'Es una persona de ＿ simpática.', ['lo más', 'la mar', 'un montón'], 'lo más', ('On ne peut plus : de lo más.', 'Extremely: de lo más.'), ('C’est une personne on ne peut plus sympathique.', 'She is an extremely nice person.')),
        FB(CHOOSE, 'Hay un ＿ de libros en el suelo.', ['montón', 'mar', 'tanto'], 'montón', ('Plein de : un montón de.', 'Loads of: un montón de.'), ('Il y a plein de livres par terre.', 'There are loads of books on the floor.')),
        FB(CHOOSE, 'No es feo, es más ＿ original.', ['bien', 'mal', 'tanto'], 'bien', ('Plutôt : más bien.', 'Rather: más bien.'), ('Il n’est pas laid, il est plutôt original.', 'It isn’t ugly, it’s rather original.')),
        TF('No estoy del todo convencido.', ('La personne est entièrement convaincue.', 'The person is completely convinced.'), FAUX, ('No del todo = pas tout à fait.', 'No del todo = not entirely.')),
      ]),
  ])])

# ═════════════════════════ 7 : Bécquer — la place de l'adjectif, les figures, les sens ═════════════════════════
W7 = WORLD('delec1-w7', ('La source aux yeux verts', 'The green-eyed spring'), REGION,
  ('Décrire avec finesse : place de l’adjectif et changement de sens (un gran hombre / un hombre grande), figures de style et verbes de perception littéraires.', 'Describe with finesse: adjective position and meaning (un gran hombre / un hombre grande), figures of speech and literary verbs of perception.'),
  (('La Dame aux yeux verts', 'The Green-Eyed Lady'), '‰', ('Dans une légende de Bécquer (1861), un jeune chasseur de Soria tombe amoureux d’une femme aux yeux verts qui vit au fond d’une source… et qui l’attire dans l’eau. Échappée du recueil, elle hante la salle des poètes : ne te laisse pas ensorceler, réponds-lui avec les mots justes de la poésie.', 'In a legend by Bécquer (1861), a young hunter from Soria falls in love with a green-eyed woman who lives at the bottom of a spring… and lures him into the water. Escaped from the book, she haunts the poets’ room: don’t let yourself be bewitched, answer her with the precise words of poetry.')),
  [CH('delec1-w7-c1', ('La salle des poètes', 'The poets’ room'), [
    L('es-adjetivo-posicion', ('Un gran hombre, un hombre grande : la place de l’adjectif', 'Un gran hombre, un hombre grande: adjective position'), ('Comprendre comment la place de l’adjectif change le sens.', 'Understand how adjective position changes meaning.'), 10, [
        ('Après le nom, l’adjectif distingue ; avant, il apprécie ou souligne : una casa blanca / la blanca nieve. En littérature, l’adjectif antéposé est fréquent : la oscura noche.', 'After the noun, the adjective distinguishes; before it, it evaluates or emphasises: una casa blanca / la blanca nieve. In literature, preposed adjectives are common: la oscura noche.'),
        ('Changement de sens : un gran hombre (un grand homme) / un hombre grande (un homme grand) ; un pobre chico (malheureux) / un chico pobre (sans argent) ; un viejo amigo (de longue date) / un amigo viejo (âgé).', 'Change of meaning: un gran hombre (a great man) / un hombre grande (a big man); un pobre chico (poor thing) / un chico pobre (penniless); un viejo amigo (long-standing) / un amigo viejo (elderly).'),
        ('Aussi : cierto libro (un certain livre) / un dato cierto (vrai) ; el mismo día (le même) / el rey mismo (en personne) ; un nuevo coche (un autre) / un coche nuevo (neuf).', 'Also: cierto libro (a certain book) / un dato cierto (true); el mismo día (the same) / el rey mismo (in person); un nuevo coche (another) / un coche nuevo (brand new).'),
      ], [
        SG('adjetivo-antepuesto', 'adjetivo antepuesto / pospuesto', ('adjectif avant / après le nom', 'adjective before / after the noun')),
        S('un-gran-hombre', 'un gran hombre / un hombre grande', ('un grand homme / un homme grand', 'a great man / a big man')),
        S('un-pobre-chico', 'un pobre chico / un chico pobre', ('un pauvre garçon / un garçon pauvre', 'a poor (unfortunate) boy / a poor (penniless) boy')),
        S('un-viejo-amigo', 'un viejo amigo / un amigo viejo', ('un vieil ami / un ami âgé', 'an old (long-standing) friend / an elderly friend')),
        S('cierto', 'cierto libro / un dato cierto', ('un certain livre / une donnée exacte', 'a certain book / a true fact')),
        S('nuevo-antepuesto', 'un nuevo coche / un coche nuevo', ('une autre voiture / une voiture neuve', 'another car / a brand-new car')),
        S('la-leyenda-becquer', 'la rima', ('le poème (de Bécquer), la rime', 'the poem (by Bécquer), the rhyme')),
        S('el-poeta', 'el / la poeta', ('le poète / la poétesse', 'the poet')),
      ], [
        x('Bécquer fue un gran poeta, aunque murió joven y pobre.', 'Bécquer fut un grand poète, même s’il mourut jeune et pauvre.', 'Bécquer was a great poet, although he died young and poor.'),
        x('El pobre Fernando vio unos ojos verdes en el fondo de la fuente, la misma noche de la cacería.', 'Le pauvre Fernando vit des yeux verts au fond de la source, la nuit même de la chasse.', 'Poor Fernando saw a pair of green eyes at the bottom of the spring, on the very night of the hunt.'),
      ], [
        FB(CHOOSE, 'Cervantes fue un ＿ escritor.', ['gran', 'grande', 'grandes'], 'gran', ('Valeur (grand par le talent) : gran avant le nom.', 'Value (great in talent): gran before the noun.'), ('Cervantes fut un grand écrivain.', 'Cervantes was a great writer.')),
        FB(CHOOSE, 'Es un ＿ amigo: nos conocemos desde niños.', ['viejo', 'amigo viejo', 'vieja'], 'viejo', ('De longue date : viejo avant le nom.', 'Long-standing: viejo before the noun.'), ('C’est un vieil ami : nous nous connaissons depuis l’enfance.', 'He’s an old friend: we’ve known each other since childhood.')),
        FB(CHOOSE, '¡＿ chico! Ha perdido a su perro.', ['Pobre', 'Chico pobre', 'Pobres'], 'Pobre', ('Compassion : pobre avant le nom.', 'Sympathy: pobre before the noun.'), ('Pauvre garçon ! Il a perdu son chien.', 'Poor boy! He’s lost his dog.')),
        TF('Me he comprado un coche nuevo.', ('La voiture sort de l’usine.', 'The car is brand new.'), VRAI, ('Nuevo après le nom = neuf.', 'Nuevo after the noun = brand new.')),
      ]),
    L('es-figuras', ('Comme une étoile : les figures de style', 'Like a star: figures of speech'), ('Reconnaître et employer comparaisons, métaphores et personnifications.', 'Recognise and use similes, metaphors and personification.'), 9, [
        ('La comparaison : como, cual (littéraire), igual que, parecido a : Sus ojos brillaban como dos esmeraldas.', 'The simile: como, cual (literary), igual que, parecido a: Sus ojos brillaban como dos esmeraldas.'),
        ('La métaphore et la personnification : las perlas del rocío (les perles de la rosée), el viento suspira (le vent soupire), la noche abraza el bosque.', 'Metaphor and personification: las perlas del rocío (the pearls of dew), el viento suspira (the wind sighs), la noche abraza el bosque.'),
        ('Expressions imagées courantes : ser un pozo de sabiduría (un puits de science), tener un corazón de oro, estar hecho un mar de lágrimas (fondre en larmes).', 'Common imagery: ser un pozo de sabiduría (a well of wisdom), tener un corazón de oro (a heart of gold), estar hecho un mar de lágrimas (to be in floods of tears).'),
      ], [
        S('la-metafora', 'la metáfora', ('la métaphore', 'the metaphor')),
        S('la-comparacion', 'la comparación', ('la comparaison', 'the comparison, the simile')),
        S('cual', 'cual (comparación literaria)', ('tel, comme (littéraire)', 'like (literary)')),
        S('la-esmeralda', 'la esmeralda', ('l’émeraude', 'the emerald')),
        S('el-rocio', 'el rocío', ('la rosée', 'dew')),
        S('suspirar', 'suspirar', ('soupirer', 'to sigh')),
        S('corazon-de-oro', 'tener un corazón de oro', ('avoir un cœur d’or', 'to have a heart of gold')),
        S('mar-de-lagrimas', 'estar hecho un mar de lágrimas', ('fondre en larmes', 'to be in floods of tears')),
      ], [
        x('Sus ojos, verdes como las esmeraldas, brillaban cual estrellas en el agua.', 'Ses yeux, verts comme des émeraudes, brillaient telles des étoiles dans l’eau.', 'Her eyes, green as emeralds, shone like stars in the water.'),
        x('El viento suspiraba entre los álamos y el rocío cubría de perlas la hierba.', 'Le vent soupirait entre les peupliers et la rosée couvrait l’herbe de perles.', 'The wind sighed among the poplars and the dew covered the grass with pearls.'),
      ], [
        FB(CHOOSE, 'Sus labios eran rojos ＿ la sangre.', ['como', 'que', 'tan'], 'como', ('Comparaison : como.', 'Simile: como.'), ('Ses lèvres étaient rouges comme le sang.', 'Her lips were red as blood.')),
        FB(COMPLETE, 'Es generosísimo: tiene un corazón de ＿.', ['oro', 'piedra', 'vidrio'], 'oro', ('Cœur d’or : corazón de oro.', 'Heart of gold: corazón de oro.'), ('Il est très généreux : il a un cœur d’or.', 'He is very generous: he has a heart of gold.')),
        TF('«El viento suspira» es una personificación.', ('On prête au vent une action humaine.', 'The wind is given a human action.'), VRAI, ('Suspirar est une action humaine.', 'Sighing is a human action.')),
        DC(ANSWER, [('Dama', '¿Cómo son mis ojos?')], ('La dame aux yeux verts veut un compliment poétique.', 'The green-eyed lady wants a poetic compliment.'), ['Son verdes como el agua del lago en primavera.', 'Son verdes y ya está.', 'Son ojos.'], 'Son verdes como el agua del lago en primavera.', ('Une comparaison poétique : como…', 'A poetic simile: como…')),
      ]),
  ]),
  CH('delec1-w7-c2', ('Au bord de la source', 'At the edge of the spring'), [
    L('es-sentidos', ('Entrevoir, murmurer, frémir : les verbes de perception', 'Glimpse, whisper, shiver: verbs of perception'), ('Enrichir une description avec des verbes de perception précis.', 'Enrich a description with precise verbs of perception.'), 9, [
        ('La vue : vislumbrar (entrevoir), contemplar, divisar (apercevoir au loin), resplandecer (resplendir), centellear (scintiller).', 'Sight: vislumbrar (to glimpse), contemplar, divisar (to make out in the distance), resplandecer (to shine), centellear (to sparkle).'),
        ('L’ouïe : susurrar (chuchoter), murmurar, crujir (craquer), retumbar (résonner). Le toucher et le corps : estremecerse (frissonner), rozar (frôler).', 'Hearing: susurrar (to whisper), murmurar, crujir (to creak), retumbar (to echo). Touch and body: estremecerse (to shiver), rozar (to brush against).'),
        ('Construction : oír / ver + infinitif ou gérondif : Oí crujir las ramas. La vi alejándose.', 'Construction: oír / ver + infinitive or gerund: Oí crujir las ramas. La vi alejándose.'),
      ], [
        S('vislumbrar', 'vislumbrar', ('entrevoir', 'to glimpse')),
        S('divisar', 'divisar', ('apercevoir (au loin)', 'to make out (in the distance)')),
        S('resplandecer', 'resplandecer', ('resplendir', 'to shine, to glow')),
        S('susurrar', 'susurrar', ('chuchoter, murmurer', 'to whisper')),
        S('crujir', 'crujir', ('craquer, crisser', 'to creak, to crunch')),
        S('retumbar', 'retumbar', ('résonner, gronder', 'to echo, to rumble')),
        S('estremecerse', 'estremecerse', ('frissonner, tressaillir', 'to shiver, to shudder')),
        S('rozar', 'rozar', ('frôler, effleurer', 'to brush against')),
      ], [
        x('En la oscuridad vislumbró unos ojos que resplandecían bajo el agua y se estremeció.', 'Dans l’obscurité, il entrevit des yeux qui resplendissaient sous l’eau et il frissonna.', 'In the darkness he glimpsed eyes glowing beneath the water and he shuddered.'),
        x('Oyó crujir las hojas secas y una voz le susurró su nombre.', 'Il entendit craquer les feuilles sèches et une voix lui chuchota son nom.', 'He heard the dry leaves crunch and a voice whispered his name.'),
      ], [
        FB(CHOOSE, 'A lo lejos se ＿ las torres de Soria.', ['divisaban', 'susurraban', 'crujían'], 'divisaban', ('Apercevoir au loin : divisar.', 'To make out in the distance: divisar.'), ('Au loin, on apercevait les tours de Soria.', 'In the distance, the towers of Soria could be made out.')),
        FB(CHOOSE, 'Me ＿ al oído un secreto.', ['susurró', 'retumbó', 'divisó'], 'susurró', ('Chuchoter : susurrar.', 'To whisper: susurrar.'), ('Il m’a chuchoté un secret à l’oreille.', 'He whispered a secret in my ear.')),
        FB(CHOOSE, 'El trueno ＿ en el valle.', ['retumbó', 'rozó', 'vislumbró'], 'retumbó', ('Le tonnerre gronde : retumbar.', 'Thunder rumbles: retumbar.'), ('Le tonnerre a grondé dans la vallée.', 'The thunder rumbled through the valley.')),
        TF('Sintió que algo le rozaba la mano.', ('Quelque chose a frôlé sa main.', 'Something brushed against his hand.'), VRAI, ('Rozar = frôler.', 'Rozar = to brush against.')),
      ]),
  ])])

# ═════════════════════════ 8 : l'Étudiant de Salamanque — l'écrit académique, l'impersonnel formel, le compte rendu ═════════════════════════
W8 = WORLD('delec1-w8', ('Le Spectre de Salamanque', 'The Spectre of Salamanca'), REGION,
  ('Rédiger comme à l’université : organiser un texte académique (en cuanto a, cabe señalar), employer les tournures impersonnelles formelles et écrire un compte rendu critique.', 'Write like a university student: organise an academic text (en cuanto a, cabe señalar), use formal impersonal structures and write a critical review.'),
  (('Le Spectre de Salamanque', 'The Spectre of Salamanca'), '¬', ('Dans L’Étudiant de Salamanque d’Espronceda (1840), le libertin Don Félix poursuit une mystérieuse dame voilée à travers les rues… jusqu’à découvrir qu’elle est un spectre. Celui-ci s’est glissé dans la salle des thèses : seul un texte académique impeccable le fera reculer.', 'In Espronceda’s The Student of Salamanca (1840), the libertine Don Félix pursues a mysterious veiled lady through the streets… until he discovers she is a spectre. It has slipped into the thesis room: only a flawless academic text will drive it back.')),
  [CH('delec1-w8-c1', ('La salle des thèses', 'The thesis room'), [
    L('es-texto-academico', ('En cuanto a, cabe señalar : le texte académique', 'En cuanto a, cabe señalar: academic writing'), ('Organiser un texte académique ou un exposé.', 'Organise an academic text or a presentation.'), 10, [
        ('Introduire le thème : el presente trabajo tiene como objetivo…, en cuanto a (quant à), con respecto a (en ce qui concerne), en lo que se refiere a.', 'Introducing the topic: el presente trabajo tiene como objetivo…, en cuanto a (as for), con respecto a (with regard to), en lo que se refiere a.'),
        ('Développer et nuancer : cabe señalar que (il convient de signaler que), cabe preguntarse si (on peut se demander si), en este sentido (en ce sens), dicho de otro modo (autrement dit).', 'Developing and qualifying: cabe señalar que (it should be noted that), cabe preguntarse si (one may wonder whether), en este sentido (in this respect), dicho de otro modo (in other words).'),
        ('Conclure : a modo de conclusión, en síntesis, de todo lo anterior se desprende que (il ressort de ce qui précède que).', 'Concluding: a modo de conclusión, en síntesis, de todo lo anterior se desprende que (it follows from the above that).'),
      ], [
        S('en-cuanto-a', 'en cuanto a', ('quant à', 'as for, regarding')),
        S('con-respecto-a', 'con respecto a', ('en ce qui concerne, quant à', 'with regard to')),
        S('cabe-senalar', 'cabe señalar que', ('il convient de signaler que', 'it should be noted that')),
        S('cabe-preguntarse', 'cabe preguntarse si', ('on peut se demander si', 'one may wonder whether')),
        S('dicho-de-otro-modo', 'dicho de otro modo', ('autrement dit', 'in other words')),
        S('en-sintesis', 'en síntesis', ('en résumé, en somme', 'in summary')),
        S('se-desprende', 'se desprende que', ('il ressort que', 'it follows that')),
        S('el-objetivo', 'el objetivo', ('l’objectif', 'the aim, the objective')),
      ], [
        x('El presente trabajo tiene como objetivo analizar la figura del libertino. En cuanto a Don Félix, cabe señalar que es un personaje romántico por excelencia.', 'Le présent travail a pour objectif d’analyser la figure du libertin. Quant à Don Félix, il convient de signaler qu’il est le personnage romantique par excellence.', 'The aim of this paper is to analyse the figure of the libertine. As for Don Félix, it should be noted that he is the quintessential Romantic character.'),
        x('De todo lo anterior se desprende que el poema critica, dicho de otro modo, la soberbia humana.', 'Il ressort de ce qui précède que le poème critique, autrement dit, l’orgueil humain.', 'It follows from the above that the poem criticises, in other words, human pride.'),
      ], [
        FB(CHOOSE, 'En ＿ a los resultados, son muy positivos.', ['cuanto', 'cuenta', 'cuando'], 'cuanto', ('Quant à : en cuanto a.', 'As for: en cuanto a.'), ('Quant aux résultats, ils sont très positifs.', 'As for the results, they are very positive.')),
        FB(CHOOSE, 'Cabe ＿ si el autor conocía esta obra.', ['preguntarse', 'señalar que', 'desprender'], 'preguntarse', ('On peut se demander si : cabe preguntarse si.', 'One may wonder whether: cabe preguntarse si.'), ('On peut se demander si l’auteur connaissait cette œuvre.', 'One may wonder whether the author knew this work.')),
        FB(CHOOSE, 'De lo anterior se ＿ que la hipótesis es correcta.', ['desprende', 'señala', 'cuenta'], 'desprende', ('Il ressort que : se desprende que.', 'It follows that: se desprende que.'), ('Il ressort de ce qui précède que l’hypothèse est correcte.', 'It follows from the above that the hypothesis is correct.')),
        TF('En síntesis, el poema es una crítica social.', ('C’est une phrase de conclusion.', 'It is a concluding sentence.'), VRAI, ('En síntesis = en résumé.', 'En síntesis = in summary.')),
      ]),
    L('es-impersonal-formal', ('Il est à noter que : l’impersonnel formel', 'It is worth noting that: the formal impersonal'), ('Employer les tournures impersonnelles du registre académique et administratif.', 'Use impersonal structures of academic and administrative language.'), 9, [
        ('Se + verbe d’opinion : se considera que, se cree que, se estima que (on estime que), se afirma que. Résultat : se ha demostrado que…', 'Se + opinion verb: se considera que, se cree que, se estima que (it is estimated that), se afirma que. Result: se ha demostrado que…'),
        ('Verbe + adjectif : resulta evidente / curioso que (il est évident / curieux que), es de destacar que (il est à souligner que), conviene + infinitif (il convient de).', 'Verb + adjective: resulta evidente / curioso que (it is clear / curious that), es de destacar que (it is worth stressing that), conviene + infinitive (it is advisable to).'),
        ('Attention : resulta curioso que, es lógico que + subjonctif (jugement) ; resulta evidente que, se ha demostrado que + indicatif (certitude).', 'Note: resulta curioso que, es lógico que + subjunctive (judgement); resulta evidente que, se ha demostrado que + indicative (certainty).'),
      ], [
        S('se-considera-que', 'se considera que', ('on considère que', 'it is considered that')),
        S('se-estima-que', 'se estima que', ('on estime que', 'it is estimated that')),
        S('resulta-evidente', 'resulta evidente que', ('il est évident que', 'it is clear that')),
        S('resulta-curioso', 'resulta curioso que', ('il est curieux que', 'it is curious that')),
        S('es-de-destacar', 'es de destacar que', ('il est à souligner que', 'it is worth stressing that')),
        S('conviene', 'conviene + infinitivo', ('il convient de', 'it is advisable to')),
        S('el-romanticismo', 'el Romanticismo', ('le romantisme', 'Romanticism')),
        S('la-obra-maestra', 'la obra maestra', ('le chef-d’œuvre', 'the masterpiece')),
      ], [
        x('Se considera que El estudiante de Salamanca es una de las obras maestras del Romanticismo español.', 'On considère que L’Étudiant de Salamanque est l’un des chefs-d’œuvre du romantisme espagnol.', 'The Student of Salamanca is considered one of the masterpieces of Spanish Romanticism.'),
        x('Resulta curioso que el poema se publicara solo dos años antes de la muerte del autor.', 'Il est curieux que le poème ait été publié deux ans seulement avant la mort de l’auteur.', 'It is curious that the poem was published only two years before the author’s death.'),
      ], [
        FB(CHOOSE, 'Resulta evidente que el autor ＿ la obra de Byron.', ['conocía', 'conociera', 'conozca'], 'conocía', ('Certitude : resulta evidente que + indicatif.', 'Certainty: resulta evidente que + indicative.'), ('Il est évident que l’auteur connaissait l’œuvre de Byron.', 'It is clear that the author knew Byron’s work.')),
        FB(CHOOSE, 'Resulta curioso que nadie ＿ el manuscrito antes.', ['encontrara', 'encontró', 'encontrará'], 'encontrara', ('Jugement : resulta curioso que + subjonctif.', 'Judgement: resulta curioso que + subjunctive.'), ('Il est curieux que personne n’ait trouvé le manuscrit avant.', 'It is curious that nobody found the manuscript earlier.')),
        FB(CHOOSE, '＿ leer el prólogo antes de empezar.', ['Conviene', 'Se estima', 'Resulta'], 'Conviene', ('Il convient de : conviene + infinitif.', 'It is advisable to: conviene + infinitive.'), ('Il convient de lire la préface avant de commencer.', 'It is advisable to read the preface before starting.')),
        TF('Se estima que el poema tiene unos 1700 versos.', ('Le nombre est une estimation.', 'The figure is an estimate.'), VRAI, ('Se estima que = on estime que.', 'Se estima que = it is estimated that.')),
      ]),
  ]),
  CH('delec1-w8-c2', ('Le compte rendu', 'The review'), [
    L('es-resena', ('La trama, el desenlace : écrire un compte rendu', 'La trama, el desenlace: writing a review'), ('Présenter et évaluer une œuvre dans un compte rendu critique.', 'Present and evaluate a work in a critical review.'), 9, [
        ('Présenter l’œuvre : la trama (l’intrigue), el argumento (le résumé de l’histoire), el / la protagonista, el desenlace (le dénouement), la ambientación (le cadre).', 'Presenting the work: la trama (the plot), el argumento (the storyline), el / la protagonista, el desenlace (the ending), la ambientación (the setting).'),
        ('Évaluer : destaca por… (se distingue par), peca de… (pèche par), logra + infinitif (réussit à), deja que desear (laisse à désirer), merece la pena (vaut la peine).', 'Evaluating: destaca por… (stands out for), peca de… (suffers from), logra + infinitive (manages to), deja que desear (leaves much to be desired), merece la pena (is worth it).'),
        ('Recommander : Se la recomiendo a…, imprescindible (incontournable), apta para todos los públicos (tout public).', 'Recommending: Se la recomiendo a…, imprescindible (essential), apta para todos los públicos (suitable for all audiences).'),
      ], [
        S('la-resena', 'la reseña', ('le compte rendu, la critique', 'the review')),
        S('la-trama', 'la trama', ('l’intrigue', 'the plot')),
        S('el-desenlace', 'el desenlace', ('le dénouement', 'the ending, the denouement')),
        S('el-protagonista', 'el / la protagonista', ('le / la protagoniste', 'the protagonist')),
        S('destacar-por', 'destacar por', ('se distinguer par', 'to stand out for')),
        S('dejar-que-desear', 'dejar que desear', ('laisser à désirer', 'to leave much to be desired')),
        S('merecer-la-pena', 'merecer la pena', ('valoir la peine', 'to be worth it')),
        S('imprescindible', 'imprescindible', ('indispensable, incontournable', 'essential, indispensable')),
      ], [
        x('La obra destaca por su ritmo y por un desenlace inolvidable, aunque la trama deja que desear en algunos pasajes.', 'L’œuvre se distingue par son rythme et par un dénouement inoubliable, même si l’intrigue laisse à désirer par endroits.', 'The work stands out for its rhythm and an unforgettable ending, although the plot leaves much to be desired in places.'),
        x('Merece la pena leerla en voz alta: es una lectura imprescindible del Romanticismo.', 'Elle vaut la peine d’être lue à voix haute : c’est une lecture incontournable du romantisme.', 'It is worth reading aloud: it is essential reading from the Romantic period.'),
      ], [
        FB(COMPLETE, 'El ＿ de la novela me sorprendió: no esperaba ese final.', ['desenlace', 'argumento', 'protagonista'], 'desenlace', ('La fin de l’histoire : el desenlace.', 'The end of the story: el desenlace.'), ('Le dénouement du roman m’a surpris : je ne m’attendais pas à cette fin.', 'The novel’s ending surprised me: I didn’t expect it.')),
        FB(COMPLETE, 'La película ＿ por su fotografía.', ['destaca', 'deja', 'peca'], 'destaca', ('Se distinguer : destacar por.', 'To stand out: destacar por.'), ('Le film se distingue par sa photographie.', 'The film stands out for its cinematography.')),
        DC(ANSWER, [('Espectro', '¿Recomendarías la obra?')], ('Le spectre te demande si tu recommandes l’œuvre.', 'The spectre asks whether you would recommend the work.'), ['Sí, merece la pena, aunque el final deja que desear.', 'Sí, merece pena dejar desear.', 'Sí, es la trama.'], 'Sí, merece la pena, aunque el final deja que desear.', ('Évaluer avec nuance.', 'Evaluating with nuance.')),
        TF('El servicio deja que desear.', ('Le service est excellent.', 'The service is excellent.'), FAUX, ('Dejar que desear = laisser à désirer.', 'Dejar que desear = to leave much to be desired.')),
      ]),
  ])])

write_level('DELEC1', ('DELE C1 : la Bibliothèque enchantée', 'DELE C1: the enchanted library'), REGION, 'The enchanted library', 52,
  [W1, W2, W3, W4, W5, W6, W7, W8, FINAL('DELEC1', REGION, ('Simulation DELE C1 : la salle de lecture', 'DELE C1 simulation: the reading room'), 'compréhension écrite, compréhension auditive et expression écrite intégrée (l’oral n’est pas évalué)', 'reading comprehension, listening comprehension and integrated written expression (speaking is not assessed)')])

