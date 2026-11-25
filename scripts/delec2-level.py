# Niveau DELE C2 (espagnol, CECRL C2) : 8 étapes dans le Rayon secret, leçons et examen blanc (français + anglais).
# Mode histoire : au fond de la Bibliothèque nationale, un rayon oublié réunit les classiques d'Espagne et d'Amérique (domaine public),
# dont les personnages discutent avec leurs auteurs. Les gardiens portent les fleurons de la typographie ancienne (❦, ❧, ☙, ⁂, ✦, ✿, ◊, ✧).
# Les notions sont en espagnol (front) avec leur sens en français ; la traduction anglaise du sens sert à l'interface en anglais.
# Usage : python3 scripts/delec2-level.py   (réécrit content/delec2/delec2.json ; les DELE A1 à C1 doivent déjà exister)
from es_common import *

REGION = 'Rayon secret'

# ═════════════════════════ 1 : Sor Juana — synonymes, faux amis, précision lexicale ═════════════════════════
W1 = WORLD('delec2-w1', ('La Dixième Muse', 'The Tenth Muse'), REGION,
  ('Choisir le mot exact : nuances entre quasi-synonymes (mirar, ver, observar), pièges des faux amis (embarazada, constipado) et remplacement des verbes passe-partout.', 'Choose the exact word: nuances between near-synonyms (mirar, ver, observar), false-friend traps (embarazada, constipado) and replacing all-purpose verbs.'),
  (('La Dixième Muse', 'The Tenth Muse'), '❦', ('Sor Juana Inés de la Cruz, religieuse et poétesse de la Nouvelle-Espagne que l’on surnomma « la Dixième Muse », s’est éveillée dans le Rayon secret. Elle ne tolère aucune approximation : à chaque mot imprécis, elle referme un livre pour toujours. Choisis le terme juste.', 'Sor Juana Inés de la Cruz, the nun and poet of New Spain known as “the Tenth Muse”, has awoken in the Secret Shelf. She tolerates no approximation: for every imprecise word, she closes a book forever. Choose the exact term.')),
  [CH('delec2-w1-c1', ('La cellule de Sor Juana', 'Sor Juana’s cell'), [
    L('es-sinonimos', ('Mirar, ver, observar : les nuances', 'Mirar, ver, observar: shades of meaning'), ('Distinguer les quasi-synonymes et choisir le plus précis.', 'Tell near-synonyms apart and choose the most precise one.'), 10, [
        ('La perception : ver (percevoir), mirar (diriger le regard), observar (examiner avec attention), contemplar (regarder longuement, avec admiration) ; oír (percevoir un son) / escuchar (prêter l’oreille).', 'Perception: ver (to see), mirar (to look at), observar (to observe closely), contemplar (to gaze at, admiringly); oír (to hear) / escuchar (to listen).'),
        ('Savoir et connaître : saber (une information, un savoir-faire : sé nadar), conocer (une personne, un lieu, une œuvre). Demander : pedir (solliciter quelque chose) / preguntar (poser une question).', 'Knowing: saber (a fact, a skill: sé nadar), conocer (a person, a place, a work). Asking: pedir (to ask for something) / preguntar (to ask a question).'),
        ('Nuances d’intensité : enfadado < furioso < colérico ; temer < aterrorizar ; agradable < delicioso < exquisito.', 'Shades of intensity: enfadado < furioso < colérico; temer < aterrorizar; agradable < delicioso < exquisito.'),
      ], [
        S('contemplar', 'contemplar', ('contempler', 'to gaze at, to contemplate')),
        S('observar', 'observar', ('observer', 'to observe')),
        S('oir-escuchar', 'oír / escuchar', ('entendre / écouter', 'to hear / to listen')),
        S('saber-conocer', 'saber / conocer', ('savoir / connaître', 'to know (a fact) / to know (a person, a place)')),
        S('pedir-preguntar', 'pedir / preguntar', ('demander (quelque chose) / poser une question', 'to ask for / to ask (a question)')),
        S('exquisito', 'exquisito / exquisita', ('exquis / exquise', 'exquisite, delicious')),
        S('la-celda', 'la celda', ('la cellule (de couvent, de prison)', 'the cell')),
        S('el-convento', 'el convento', ('le couvent', 'the convent')),
      ], [
        x('Sor Juana no se limitaba a mirar el cielo: lo observaba con un telescopio y anotaba cuanto veía.', 'Sor Juana ne se contentait pas de regarder le ciel : elle l’observait au télescope et notait tout ce qu’elle voyait.', 'Sor Juana didn’t just look at the sky: she observed it through a telescope and noted down everything she saw.'),
        x('Oía las campanas del convento, pero no las escuchaba: estaba absorta en su lectura.', 'Elle entendait les cloches du couvent, mais ne les écoutait pas : elle était absorbée par sa lecture.', 'She heard the convent bells, but wasn’t listening to them: she was absorbed in her reading.'),
      ], [
        FB(CHOOSE, '¿＿ a la autora de este poema?', ['Conoces', 'Sabes', 'Sabes a'], 'Conoces', ('Une personne : conocer.', 'A person: conocer.'), ('Connais-tu l’autrice de ce poème ?', 'Do you know the author of this poem?')),
        FB(CHOOSE, 'Le ＿ que me prestara su libro.', ['pedí', 'pregunté', 'demandé'], 'pedí', ('Solliciter quelque chose : pedir.', 'To ask for something: pedir.'), ('Je lui ai demandé de me prêter son livre.', 'I asked her to lend me her book.')),
        FB(CHOOSE, 'Pasó horas ＿ el atardecer desde la terraza.', ['contemplando', 'viendo de', 'oyendo'], 'contemplando', ('Regarder longuement avec admiration : contemplar.', 'To gaze admiringly: contemplar.'), ('Il passa des heures à contempler le coucher du soleil depuis la terrasse.', 'He spent hours gazing at the sunset from the terrace.')),
        TF('Lo oí, pero no lo escuché.', ('La personne a perçu le son sans y prêter attention.', 'The person heard the sound without paying attention.'), VRAI, ('Oír = percevoir ; escuchar = prêter l’oreille.', 'Oír = to hear; escuchar = to listen.')),
      ]),
    L('es-falsos-amigos', ('Embarazada, constipado : les faux amis', 'Embarazada, constipado: false friends'), ('Éviter les faux amis entre le français et l’espagnol.', 'Avoid false friends between French and Spanish.'), 10, [
        ('Faux amis classiques : embarazada (enceinte, et non embarrassée), constipado (enrhumé), la carpeta (la chemise, le classeur), el éxito (le succès), largo (long, et non large), el suceso (le fait divers).', 'Classic false friends: embarazada (pregnant, not embarrassed), constipado (having a cold), la carpeta (folder), el éxito (success), largo (long, not large), el suceso (event, news story).'),
        ('Encore : molestar (déranger), el compromiso (l’engagement, les fiançailles), la firma (la signature), salir (sortir, partir), la oficina (le bureau), recordar (se souvenir, rappeler).', 'Also: molestar (to bother), el compromiso (commitment, engagement), la firma (signature), salir (to go out, to leave), la oficina (office), recordar (to remember, to remind).'),
        ('Pour « embarrassé » : avergonzado ou cortado ; pour « constipé » : estreñido ; pour « large » : ancho.', 'For “embarrassed”: avergonzado or cortado; for “constipated”: estreñido; for “wide”: ancho.'),
      ], [
        S('embarazada', 'embarazada', ('enceinte', 'pregnant')),
        S('constipado', 'constipado / constipada', ('enrhumé / enrhumée', 'having a cold')),
        S('la-carpeta', 'la carpeta', ('la chemise (dossier), le classeur', 'the folder')),
        S('el-exito', 'el éxito', ('le succès', 'success')),
        S('el-suceso', 'el suceso', ('le fait divers, l’événement', 'the incident, the news story')),
        S('molestar', 'molestar', ('déranger, gêner', 'to bother, to disturb')),
        S('el-compromiso', 'el compromiso', ('l’engagement, les fiançailles', 'commitment, engagement')),
        S('avergonzado', 'avergonzado / cortado', ('embarrassé, gêné', 'embarrassed')),
      ], [
        x('Estoy constipada y me siento avergonzada: he estornudado en plena conferencia.', 'Je suis enrhumée et je me sens gênée : j’ai éternué en pleine conférence.', 'I’ve got a cold and I feel embarrassed: I sneezed in the middle of the lecture.'),
        x('El libro fue un éxito, pero la sección de sucesos del periódico apenas lo mencionó.', 'Le livre fut un succès, mais la rubrique faits divers du journal le mentionna à peine.', 'The book was a success, but the newspaper’s local news section barely mentioned it.'),
      ], [
        FB(CHOOSE, 'Me puse rojo: estaba muy ＿.', ['avergonzado', 'embarazado', 'constipado'], 'avergonzado', ('Embarrassé : avergonzado (embarazada = enceinte).', 'Embarrassed: avergonzado (embarazada = pregnant).'), ('J’ai rougi : j’étais très gêné.', 'I blushed: I was very embarrassed.')),
        FB(CHOOSE, 'Guarda los documentos en esta ＿ azul.', ['carpeta', 'alfombra', 'firma'], 'carpeta', ('Une chemise à documents : la carpeta.', 'A document folder: la carpeta.'), ('Range les documents dans cette chemise bleue.', 'Put the documents in this blue folder.')),
        FB(CHOOSE, 'El río es muy ＿: mide cien metros de orilla a orilla.', ['ancho', 'largo', 'amplio de'], 'ancho', ('Large : ancho (largo = long).', 'Wide: ancho (largo = long).'), ('Le fleuve est très large : il mesure cent mètres d’une rive à l’autre.', 'The river is very wide: it measures a hundred metres from bank to bank.')),
        TF('Mi hermana está embarazada.', ('La sœur attend un enfant.', 'The sister is expecting a baby.'), VRAI, ('Embarazada = enceinte.', 'Embarazada = pregnant.')),
      ]),
  ]),
  CH('delec2-w1-c2', ('La plume exacte', 'The precise pen'), [
    L('es-precision-lexica', ('Formuler, padecer, depositar : remplacer les verbes passe-partout', 'Formuler, padecer, depositar: replacing all-purpose verbs'), ('Remplacer hacer, tener, poner, decir par des verbes précis.', 'Replace hacer, tener, poner, decir with precise verbs.'), 10, [
        ('Hacer : hacer una pregunta → formular ; hacer un informe → elaborar, redactar ; hacer un crimen → cometer ; hacer un viaje → realizar, emprender.', 'Hacer: hacer una pregunta → formular; hacer un informe → elaborar, redactar; hacer un crimen → cometer; hacer un viaje → realizar, emprender.'),
        ('Tener : tener una enfermedad → padecer ; tener un cargo → ocupar, desempeñar ; tener éxito → cosechar ; tener lugar → celebrarse.', 'Tener: tener una enfermedad → padecer; tener un cargo → ocupar, desempeñar; tener éxito → cosechar; tener lugar → celebrarse.'),
        ('Poner et decir : poner dinero → ingresar, depositar ; poner una norma → establecer ; decir una opinión → expresar, manifestar ; decir un secreto → revelar, desvelar.', 'Poner and decir: poner dinero → ingresar, depositar; poner una norma → establecer; decir una opinión → expresar, manifestar; decir un secreto → revelar, desvelar.'),
      ], [
        S('formular', 'formular', ('formuler', 'to formulate, to put (a question)')),
        S('elaborar', 'elaborar', ('élaborer, rédiger', 'to draw up, to produce')),
        S('padecer', 'padecer', ('souffrir de', 'to suffer from')),
        S('desempenar', 'desempeñar', ('exercer, remplir (une fonction)', 'to hold, to perform (a role)')),
        S('cosechar', 'cosechar', ('récolter, remporter', 'to reap, to win')),
        S('ingresar', 'ingresar', ('déposer (de l’argent), entrer (à l’hôpital)', 'to pay in, to be admitted')),
        S('manifestar', 'manifestar', ('manifester, exprimer', 'to express, to state')),
        S('desvelar', 'desvelar', ('dévoiler, révéler', 'to reveal, to unveil')),
      ], [
        x('Sor Juana desempeñó un papel decisivo en la literatura novohispana y cosechó una fama inmensa en vida.', 'Sor Juana joua un rôle décisif dans la littérature de la Nouvelle-Espagne et connut une immense renommée de son vivant.', 'Sor Juana played a decisive role in the literature of New Spain and won immense fame in her lifetime.'),
        x('La investigadora formuló una hipótesis audaz y desveló el origen del manuscrito.', 'La chercheuse formula une hypothèse audacieuse et dévoila l’origine du manuscrit.', 'The researcher put forward a bold hypothesis and revealed the origin of the manuscript.'),
      ], [
        FB(CHOOSE, 'El ministro ＿ el cargo durante diez años.', ['desempeñó', 'hizo', 'puso'], 'desempeñó', ('Exercer une fonction : desempeñar un cargo.', 'To hold a post: desempeñar un cargo.'), ('Le ministre a exercé la fonction pendant dix ans.', 'The minister held the post for ten years.')),
        FB(CHOOSE, 'Su abuelo ＿ una enfermedad rara.', ['padecía', 'tenía de', 'hacía'], 'padecía', ('Souffrir d’une maladie : padecer.', 'To suffer from an illness: padecer.'), ('Son grand-père souffrait d’une maladie rare.', 'His grandfather suffered from a rare disease.')),
        FB(CHOOSE, 'La periodista ＿ una pregunta incómoda.', ['formuló', 'puso', 'tuvo'], 'formuló', ('Poser une question (soutenu) : formular.', 'To put a question (formal): formular.'), ('La journaliste a posé une question gênante.', 'The journalist asked an awkward question.')),
        TF('La película cosechó un gran éxito.', ('Le film a remporté un grand succès.', 'The film was a great success.'), VRAI, ('Cosechar un éxito = remporter un succès.', 'Cosechar un éxito = to achieve a success.')),
      ]),
  ])])

# ═════════════════════════ 2 : le Cygne de Darío — suffixes, dérivation, mots savants ═════════════════════════
W2 = WORLD('delec2-w2', ('Le Cygne de Darío', 'Darío’s Swan'), REGION,
  ('Jouer avec la formation des mots : suffixes affectifs (-ito, -ón, -ucho), préfixes et suffixes de dérivation, et mots savants du registre littéraire (efímero, inefable).', 'Play with word formation: affective suffixes (-ito, -ón, -ucho), derivational prefixes and suffixes, and learned words of the literary register (efímero, inefable).'),
  (('Le Cygne de Darío', 'Darío’s Swan'), '❧', ('Le cygne, emblème du modernisme de Rubén Darío, a quitté les pages d’Azul… pour glisser sur la fontaine du Rayon secret. Il ne se laisse approcher que par ceux qui savent sculpter les mots comme des bijoux.', 'The swan, emblem of Rubén Darío’s modernismo, has left the pages of Azul… to glide across the fountain of the Secret Shelf. It only lets near those who can sculpt words like jewels.')),
  [CH('delec2-w2-c1', ('Le bassin du cygne', 'The swan’s pool'), [
    L('es-sufijos', ('Casita, casona, casucha : les suffixes affectifs', 'Casita, casona, casucha: affective suffixes'), ('Comprendre et employer diminutifs, augmentatifs et péjoratifs.', 'Understand and use diminutives, augmentatives and pejoratives.'), 10, [
        ('Diminutifs : -ito (le plus courant), -illo (fréquent en Andalousie), -ico (Aragon, Colombie), -ín (Asturies). Ils expriment la petite taille ou l’affection : un cafecito, ahorita, abuelito.', 'Diminutives: -ito (most common), -illo (frequent in Andalusia), -ico (Aragon, Colombia), -ín (Asturias). They express small size or affection: un cafecito, ahorita, abuelito.'),
        ('Augmentatifs : -ón / -ona (un cucharón, una mujerona), -azo (un golpazo : un grand coup ; un cochazo : une superbe voiture).', 'Augmentatives: -ón / -ona (un cucharón, una mujerona), -azo (un golpazo: a big blow; un cochazo: a fancy car).'),
        ('Péjoratifs : -ucho (una casucha : une masure), -ejo (un pueblejo), -aco (un libraco : un gros livre sans intérêt). Certains mots ont pris un sens propre : la bombilla, el cigarrillo, el bolsillo.', 'Pejoratives: -ucho (una casucha: a hovel), -ejo (un pueblejo), -aco (un libraco: a boring old tome). Some words have taken on their own meaning: la bombilla, el cigarrillo, el bolsillo.'),
      ], [
        SG('diminutivo', '-ito / -illo / -ico', ('suffixes diminutifs', 'diminutive suffixes')),
        SG('aumentativo', '-ón / -azo', ('suffixes augmentatifs', 'augmentative suffixes')),
        SG('despectivo', '-ucho / -ejo / -aco', ('suffixes péjoratifs', 'pejorative suffixes')),
        S('el-golpazo', 'el golpazo', ('le grand coup', 'the heavy blow')),
        S('la-casucha', 'la casucha', ('la masure', 'the hovel')),
        S('el-cisne', 'el cisne', ('le cygne', 'the swan')),
        S('el-modernismo', 'el modernismo', ('le modernisme (littéraire)', 'modernismo (literary movement)')),
        S('la-bombilla', 'la bombilla', ('l’ampoule (électrique)', 'the light bulb')),
      ], [
        x('El abuelito vivía en una casita junto al lago, donde nadaba un cisne blanquísimo.', 'Le grand-père vivait dans une maisonnette près du lac, où nageait un cygne d’une blancheur éclatante.', 'Grandpa lived in a little house by the lake, where a dazzling white swan swam.'),
        x('Se dio un golpazo contra la puerta y pasó la noche en una casucha del pueblo.', 'Il s’est donné un grand coup contre la porte et a passé la nuit dans une masure du village.', 'He banged himself hard against the door and spent the night in a hovel in the village.'),
      ], [
        FB(CHOOSE, '¿Tomamos un ＿? Solo tengo diez minutos.', ['cafecito', 'cafetón', 'cafeucho'], 'cafecito', ('Affection et petite quantité : -ito.', 'Affection and small amount: -ito.'), ('On prend un petit café ? Je n’ai que dix minutes.', 'Shall we have a quick coffee? I’ve only got ten minutes.')),
        FB(CHOOSE, 'Vive en una ＿ sin luz ni agua.', ['casucha', 'casita', 'casona'], 'casucha', ('Péjoratif : -ucha.', 'Pejorative: -ucha.'), ('Il vit dans une masure sans électricité ni eau.', 'He lives in a hovel with no electricity or water.')),
        FB(CHOOSE, 'Se dio un ＿ tremendo contra la puerta.', ['golpazo', 'golpito', 'golpucho'], 'golpazo', ('Grand coup : -azo.', 'Big blow: -azo.'), ('Il s’est donné un coup terrible contre la porte.', 'He banged himself really hard against the door.')),
        TF('«Bombilla» significa una bomba pequeña.', ('Le mot désigne une petite bombe.', 'The word means a small bomb.'), FAUX, ('Bombilla a son propre sens : l’ampoule.', 'Bombilla has its own meaning: light bulb.')),
      ]),
    L('es-derivacion', ('Deshacer, imprevisible : préfixes et suffixes', 'Deshacer, imprevisible: prefixes and suffixes'), ('Comprendre et former des mots par dérivation.', 'Understand and form words by derivation.'), 10, [
        ('Préfixes : des- / dis- (contraire : deshacer, disgustar), in- / im- / i- (négation : inútil, imposible, ilegal), re- (répétition : releer), pre- (avant : prever), sobre- (excès : sobrevalorar), contra- (opposition : contradecir).', 'Prefixes: des- / dis- (opposite: deshacer, disgustar), in- / im- / i- (negation: inútil, imposible, ilegal), re- (repetition: releer), pre- (before: prever), sobre- (excess: sobrevalorar), contra- (opposition: contradecir).'),
        ('Suffixes : -able / -ible (possibilité : imprevisible, legible), -ismo (doctrine : realismo), -ista (personne : novelista), -ez (qualité : timidez), -ería (lieu ou commerce : librería).', 'Suffixes: -able / -ible (possibility: imprevisible, legible), -ismo (doctrine: realismo), -ista (person: novelista), -ez (quality: timidez), -ería (place or shop: librería).'),
        ('Attention aux accords : prever se conjugue comme ver (preví, previsto) ; contradecir comme decir (contradijo).', 'Watch the forms: prever is conjugated like ver (preví, previsto); contradecir like decir (contradijo).'),
      ], [
        SG('prefijos', 'des- / in- / re- / pre- / sobre-', ('préfixes de dérivation', 'derivational prefixes')),
        SG('sufijos-derivacion', '-able / -ismo / -ista / -ería', ('suffixes de dérivation', 'derivational suffixes')),
        S('imprevisible', 'imprevisible', ('imprévisible', 'unpredictable')),
        S('releer', 'releer', ('relire', 'to reread')),
        S('prever', 'prever', ('prévoir', 'to foresee')),
        S('sobrevalorar', 'sobrevalorar', ('surestimer', 'to overrate')),
        S('contradecir', 'contradecir', ('contredire', 'to contradict')),
        S('legible', 'legible / ilegible', ('lisible / illisible', 'legible / illegible')),
      ], [
        x('Releí el poema tres veces: su final es tan imprevisible como hermoso.', 'J’ai relu le poème trois fois : sa fin est aussi imprévisible que belle.', 'I reread the poem three times: its ending is as unpredictable as it is beautiful.'),
        x('Muchos críticos sobrevaloraron su obra; otros contradijeron esa opinión con argumentos sólidos.', 'Beaucoup de critiques surestimèrent son œuvre ; d’autres contredirent cet avis avec des arguments solides.', 'Many critics overrated his work; others contradicted that view with solid arguments.'),
      ], [
        FB(CHOOSE, 'Nadie ＿ el final de la historia.', ['previó', 'prevenió', 'preveyó'], 'previó', ('Prever se conjugue comme ver : previó.', 'Prever is conjugated like ver: previó.'), ('Personne ne prévit la fin de l’histoire.', 'Nobody foresaw the end of the story.')),
        FB(CHOOSE, 'Su letra es tan mala que el texto es ＿.', ['ilegible', 'inlegible', 'deslegible'], 'ilegible', ('Devant l : il- (ilegible).', 'Before l: il- (ilegible).'), ('Son écriture est si mauvaise que le texte est illisible.', 'His handwriting is so bad that the text is illegible.')),
        FB(CHOOSE, 'Compré la novela en una ＿ de viejo.', ['librería', 'librista', 'librismo'], 'librería', ('Commerce : -ería.', 'Shop: -ería.'), ('J’ai acheté le roman chez un bouquiniste.', 'I bought the novel at a second-hand bookshop.')),
        TF('Le contradijo delante de todos.', ('Il a dit l’inverse de lui en public.', 'He said the opposite in front of everyone.'), VRAI, ('Contradecir = contredire.', 'Contradecir = to contradict.')),
      ]),
  ]),
  CH('delec2-w2-c2', ('Les bijoux du poète', 'The poet’s jewels'), [
    L('es-cultismos', ('Efímero, inefable : les mots savants', 'Efímero, inefable: learned words'), ('Reconnaître et employer les mots savants du registre littéraire.', 'Recognise and use learned words of the literary register.'), 9, [
        ('Adjectifs savants : efímero (éphémère), inefable (indicible), lúgubre (lugubre), nimio (insignifiant), ubérrimo (très fertile), prístino (originel, pur), sempiterno (éternel, sans fin).', 'Learned adjectives: efímero (ephemeral), inefable (ineffable), lúgubre (gloomy), nimio (trivial), ubérrimo (very fertile), prístino (pristine), sempiterno (everlasting).'),
        ('Ils donnent un ton soutenu ou poétique ; employés hors contexte, ils peuvent paraître pédants. L’ironie les utilise volontiers : su sempiterna queja (sa sempiternelle plainte).', 'They give a formal or poetic tone; used out of context, they can sound pedantic. Irony likes them: su sempiterna queja (his everlasting complaint).'),
        ('Leurs équivalents courants : efímero → breve, inefable → indescriptible, nimio → sin importancia, lúgubre → triste y oscuro.', 'Everyday equivalents: efímero → breve, inefable → indescriptible, nimio → sin importancia, lúgubre → triste y oscuro.'),
      ], [
        S('efimero', 'efímero / efímera', ('éphémère', 'ephemeral')),
        S('inefable', 'inefable', ('indicible, ineffable', 'ineffable')),
        S('lugubre', 'lúgubre', ('lugubre', 'gloomy, lugubrious')),
        S('nimio', 'nimio / nimia', ('insignifiant, futile', 'trivial, trifling')),
        S('pristino', 'prístino / prístina', ('originel, pur', 'pristine')),
        S('sempiterno', 'sempiterno / sempiterna', ('sempiternel', 'everlasting, eternal')),
        S('la-fugacidad', 'la fugacidad', ('le caractère fugace', 'fleetingness, transience')),
        S('el-ocaso', 'el ocaso', ('le crépuscule, le déclin', 'sunset, decline')),
      ], [
        x('El poeta canta la belleza efímera de la rosa y la inefable melancolía del ocaso.', 'Le poète chante la beauté éphémère de la rose et l’indicible mélancolie du crépuscule.', 'The poet sings of the ephemeral beauty of the rose and the ineffable melancholy of sunset.'),
        x('Discutieron durante horas por un detalle nimio, con su sempiterno orgullo.', 'Ils discutèrent pendant des heures pour un détail insignifiant, avec leur sempiternel orgueil.', 'They argued for hours over a trivial detail, with their everlasting pride.'),
      ], [
        FB(CHOOSE, 'La fama es ＿: hoy te aplauden y mañana te olvidan.', ['efímera', 'sempiterna', 'prístina'], 'efímera', ('Qui dure peu : efímero.', 'Short-lived: efímero.'), ('La gloire est éphémère : aujourd’hui on t’applaudit, demain on t’oublie.', 'Fame is fleeting: today they applaud you, tomorrow they forget you.')),
        FB(CHOOSE, 'No discutas por algo tan ＿.', ['nimio', 'inefable', 'lúgubre'], 'nimio', ('Sans importance : nimio.', 'Unimportant: nimio.'), ('Ne te dispute pas pour une chose aussi futile.', 'Don’t argue over something so trivial.')),
        FB(CHOOSE, 'El castillo tenía un aspecto ＿ bajo la tormenta.', ['lúgubre', 'nimio', 'efímero'], 'lúgubre', ('Triste et sombre : lúgubre.', 'Dark and gloomy: lúgubre.'), ('Le château avait un aspect lugubre sous l’orage.', 'The castle looked gloomy in the storm.')),
        TF('Sintió una alegría inefable.', ('La joie était impossible à exprimer.', 'The joy was impossible to put into words.'), VRAI, ('Inefable = indicible.', 'Inefable = ineffable.')),
      ]),
  ])])

# ═════════════════════════ 3 : les souris de fray Martín — variétés, espagnol andin, orthographe ═════════════════════════
W3 = WORLD('delec2-w3', ('Les souris de fray Martín', 'Fray Martín’s mice'), REGION,
  ('Reconnaître les variétés de l’espagnol (seseo, yeísmo, aspiration, leísmo), comprendre l’espagnol des Andes et maîtriser les subtilités de l’orthographe (tilde diacritique, porque / por qué).', 'Recognise varieties of Spanish (seseo, yeísmo, aspiration, leísmo), understand Andean Spanish and master spelling subtleties (diacritic accent, porque / por qué).'),
  (('Les Souris de fray Martín', 'Fray Martín’s Mice'), '☙', ('Dans une Tradition péruvienne de Ricardo Palma, fray Martín de Porres parvient à faire manger dans la même écuelle un chien, un chat et une souris. Ses souris se sont échappées et grignotent les accents des manuscrits : rends à chaque mot sa forme et à chaque accent sa région.', 'In one of Ricardo Palma’s Peruvian Traditions, Fray Martín de Porres gets a dog, a cat and a mouse to eat from the same bowl. His mice have escaped and are nibbling the accents off the manuscripts: give every word back its form and every accent its region.')),
  [CH('delec2-w3-c1', ('Le couvent de Lima', 'The convent in Lima'), [
    L('es-variedades', ('Seseo, yeísmo, leísmo : les variétés de l’espagnol', 'Seseo, yeísmo, leísmo: varieties of Spanish'), ('Identifier les principaux traits de prononciation et de grammaire selon les régions.', 'Identify the main pronunciation and grammar features by region.'), 10, [
        ('Prononciation : seseo (z et c prononcés s : Andalousie, Canaries, toute l’Amérique), ceceo (s prononcé comme z, une partie de l’Andalousie), yeísmo (ll = y, quasi général), aspiration du s final (los amigos → « loh amigoh », Caraïbes, Andalousie).', 'Pronunciation: seseo (z and c pronounced s: Andalusia, the Canaries, all of the Americas), ceceo (s pronounced like z, part of Andalusia), yeísmo (ll = y, almost universal), aspiration of final s (los amigos → “loh amigoh”, Caribbean, Andalusia).'),
        ('Rioplatense : rehilamiento (ll et y prononcés « ch » ou « j » français : « shó » pour yo). Mexique : consonnes nettes, voyelles parfois affaiblies.', 'River Plate: rehilamiento (ll and y pronounced “sh” or “zh”: “shó” for yo). Mexico: clear consonants, sometimes weakened vowels.'),
        ('Grammaire : leísmo (le comme COD masculin de personne : a Juan le vi, admis par la RAE), laísmo (la comme COI : la dije, fautif), ustedes au lieu de vosotros en Amérique et aux Canaries.', 'Grammar: leísmo (le as masculine direct object for people: a Juan le vi, accepted by the RAE), laísmo (la as indirect object: la dije, incorrect), ustedes instead of vosotros in the Americas and the Canaries.'),
      ], [
        S('el-seseo', 'el seseo', ('le seseo (c et z prononcés s)', 'seseo (c and z pronounced s)')),
        S('el-yeismo', 'el yeísmo', ('le yeísmo (ll prononcé y)', 'yeísmo (ll pronounced y)')),
        S('aspirar-la-s', 'aspirar la s', ('aspirer le s', 'to aspirate the s')),
        S('el-leismo', 'el leísmo', ('le leísmo (le complément direct)', 'leísmo (le as direct object)')),
        S('el-laismo', 'el laísmo', ('le laísmo (la complément indirect)', 'laísmo (la as indirect object)')),
        S('el-habla', 'el habla', ('le parler (d’une région)', 'the speech, the dialect')),
        S('la-variedad', 'la variedad', ('la variété', 'the variety')),
        S('la-norma-culta', 'la norma culta', ('la norme cultivée', 'the educated standard')),
      ], [
        x('En Lima, como en toda América, se practica el seseo: «cielo» y «sielo» suenan igual.', 'À Lima, comme dans toute l’Amérique, on pratique le seseo : « cielo » et « sielo » sonnent pareil.', 'In Lima, as throughout the Americas, seseo is used: “cielo” and “sielo” sound the same.'),
        x('El leísmo de persona está admitido («a Juan le vi»), pero el laísmo («la dije la verdad») se considera incorrecto.', 'Le leísmo de personne est admis (« a Juan le vi »), mais le laísmo (« la dije la verdad ») est considéré comme fautif.', 'Personal leísmo is accepted (“a Juan le vi”), but laísmo (“la dije la verdad”) is considered incorrect.'),
      ], [
        FB(CHOOSE, 'A mi madre ＿ dije la verdad.', ['le', 'la', 'lo'], 'le', ('Complément indirect : le (la serait un laísmo).', 'Indirect object: le (la would be laísmo).'), ('J’ai dit la vérité à ma mère.', 'I told my mother the truth.')),
        FB(COMPLETE, 'Si «casa» y «caza» suenan igual, se trata de ＿.', ['seseo', 'yeísmo', 'leísmo'], 'seseo', ('c / z prononcés s : seseo.', 'c / z pronounced s: seseo.'), ('Si « casa » et « caza » sonnent pareil, il s’agit de seseo.', 'If “casa” and “caza” sound the same, it’s seseo.')),
        TF('En Buenos Aires, «yo» puede sonar «shó».', ('C’est le rehilamiento rioplatense.', 'It is River Plate rehilamiento.'), VRAI, ('Ll et y prononcés « sh » au Río de la Plata.', 'Ll and y pronounced “sh” in the River Plate.')),
        TF('El laísmo es la norma culta en América.', ('Le laísmo est la norme en Amérique.', 'Laísmo is the standard in the Americas.'), FAUX, ('Le laísmo est considéré comme fautif.', 'Laísmo is considered incorrect.')),
      ]),
    L('es-andino', ('Palta, choclo, guagua : l’espagnol des Andes', 'Palta, choclo, guagua: Andean Spanish'), ('Comprendre le vocabulaire andin, souvent d’origine quechua.', 'Understand Andean vocabulary, often of Quechua origin.'), 9, [
        ('Mots d’origine quechua : la palta (l’avocat ; aguacate au Mexique et en Espagne), el choclo (l’épi de maïs tendre), la chacra (la petite ferme), la guagua (le bébé au Pérou et en Bolivie… mais le bus aux Canaries et à Cuba !), el poncho, la cancha (le terrain).', 'Words of Quechua origin: la palta (avocado; aguacate in Mexico and Spain), el choclo (sweetcorn cob), la chacra (smallholding), la guagua (baby in Peru and Bolivia… but bus in the Canaries and Cuba!), el poncho, la cancha (pitch, field).'),
        ('Usages andins : le diminutif de politesse (ahorita, cerquita, ¿me pasas la sal, por favorcito?), dice que (paraît-il) pour rapporter une information.', 'Andean usage: the polite diminutive (ahorita, cerquita, ¿me pasas la sal, por favorcito?), dice que (apparently) to report information.'),
        ('Le Pérou a deux traditions littéraires majeures : Ricardo Palma (Tradiciones peruanas) et l’Inca Garcilaso de la Vega (Comentarios reales).', 'Peru has two major literary traditions: Ricardo Palma (Peruvian Traditions) and the Inca Garcilaso de la Vega (Royal Commentaries).'),
      ], [
        S('la-palta', 'la palta', ('l’avocat (fruit, Andes)', 'avocado (Andes)')),
        S('el-choclo', 'el choclo', ('l’épi de maïs tendre', 'sweetcorn cob')),
        S('la-chacra', 'la chacra', ('la petite ferme (Andes)', 'smallholding (Andes)')),
        S('la-guagua', 'la guagua', ('le bébé (Andes), le bus (Canaries, Caraïbes)', 'baby (Andes), bus (Canaries, Caribbean)')),
        S('la-cancha', 'la cancha', ('le terrain (de sport)', 'the pitch, the court')),
        S('el-quechua', 'el quechua', ('le quechua', 'Quechua')),
        S('la-tradicion', 'la tradición', ('la tradition, le récit traditionnel', 'tradition, traditional tale')),
        S('cerquita', 'cerquita', ('tout près (diminutif)', 'very close by (diminutive)')),
      ], [
        x('En la chacra de mis abuelos comíamos choclo con queso y palta.', 'Dans la petite ferme de mes grands-parents, nous mangions du maïs tendre avec du fromage et de l’avocat.', 'On my grandparents’ smallholding we ate sweetcorn with cheese and avocado.'),
        x('En Lima, la guagua dormía; en Las Palmas, la guagua no llegaba.', 'À Lima, le bébé dormait ; à Las Palmas, le bus n’arrivait pas.', 'In Lima, the baby was sleeping; in Las Palmas, the bus wasn’t coming.'),
      ], [
        FB(COMPLETE, 'En Perú no se dice «aguacate», sino «＿».', ['palta', 'choclo', 'chacra'], 'palta', ('L’avocat au Pérou : la palta.', 'Avocado in Peru: la palta.'), ('Au Pérou, on ne dit pas « aguacate », mais « palta ».', 'In Peru you don’t say “aguacate”, but “palta”.')),
        FB(COMPLETE, 'Los niños juegan al fútbol en la ＿ del barrio.', ['cancha', 'chacra', 'palta'], 'cancha', ('Le terrain : la cancha.', 'The pitch: la cancha.'), ('Les enfants jouent au football sur le terrain du quartier.', 'The children play football on the local pitch.')),
        TF('En Canarias, «coger la guagua» es tomar el autobús.', ('Aux Canaries, guagua veut dire bus.', 'In the Canaries, guagua means bus.'), VRAI, ('Guagua = bus aux Canaries et à Cuba.', 'Guagua = bus in the Canaries and Cuba.')),
        DC(ANSWER, [('Ratón', '¿Dónde está el convento?')], ('Une souris de fray Martín te demande où est le couvent ; il est tout près.', 'One of Fray Martín’s mice asks where the convent is; it’s very close.'), ['Aquí cerquita, a la vuelta de la esquina.', 'Aquí cerquísimo de lejos.', 'Está choclo.'], 'Aquí cerquita, a la vuelta de la esquina.', ('Diminutif andin : cerquita.', 'Andean diminutive: cerquita.')),
      ]),
  ]),
  CH('delec2-w3-c2', ('Les accents grignotés', 'The nibbled accents'), [
    L('es-ortografia', ('Tú / tu, aún / aun, porque / por qué : l’orthographe fine', 'Tú / tu, aún / aun, porque / por qué: fine spelling points'), ('Maîtriser la tilde diacritique et les formes qu’on confond.', 'Master the diacritic accent and commonly confused forms.'), 10, [
        ('Tilde diacritique : tú (pronom) / tu (possessif), él / el, mí / mi, sí (oui, soi) / si (si), té (thé) / te, más (plus) / mas (mais, littéraire), aún (encore = todavía) / aun (même = incluso). Depuis 2010, la RAE recommande solo sans accent.', 'Diacritic accent: tú (pronoun) / tu (possessive), él / el, mí / mi, sí (yes, oneself) / si (if), té (tea) / te, más (more) / mas (but, literary), aún (still = todavía) / aun (even = incluso). Since 2010 the RAE recommends solo without an accent.'),
        ('Porque (parce que), por qué (pourquoi ?), el porqué (la raison), por que (pour lequel / par lequel) : No sé por qué se fue. Ignoro el porqué de su decisión.', 'Porque (because), por qué (why?), el porqué (the reason), por que (for which / through which): No sé por qué se fue. Ignoro el porqué de su decisión.'),
        ('Sino (mais au contraire, après une négation) / si no (si… ne… pas) : No es rojo, sino azul. Si no vienes, me voy.', 'Sino (but rather, after a negative) / si no (if… not): No es rojo, sino azul. Si no vienes, me voy.'),
      ], [
        SG('tilde-diacritica', 'tú / tu, él / el, sí / si', ('accent diacritique', 'diacritic accent')),
        S('aun-aun', 'aún / aun', ('encore / même', 'still / even')),
        S('porque-por-que', 'porque / por qué / el porqué', ('parce que / pourquoi / la raison', 'because / why / the reason why')),
        S('sino-si-no', 'sino / si no', ('mais (au contraire) / si… ne… pas', 'but rather / if not')),
        S('la-tilde', 'la tilde', ('l’accent écrit', 'the written accent')),
        S('la-ortografia', 'la ortografía', ('l’orthographe', 'spelling, orthography')),
        S('la-errata', 'la errata', ('la coquille (faute d’impression)', 'the typo, the misprint')),
        S('el-manuscrito', 'el manuscrito', ('le manuscrit', 'the manuscript')),
      ], [
        x('Aún no entiendo el porqué de tantas erratas en el manuscrito: ¡los ratones se comieron las tildes!', 'Je ne comprends toujours pas la raison de tant de coquilles dans le manuscrit : les souris ont mangé les accents !', 'I still don’t understand the reason for so many typos in the manuscript: the mice ate the accents!'),
        x('No lo escribió fray Martín, sino Ricardo Palma; si no me crees, mira la portada.', 'Ce n’est pas fray Martín qui l’a écrit, mais Ricardo Palma ; si tu ne me crois pas, regarde la couverture.', 'It wasn’t Fray Martín who wrote it, but Ricardo Palma; if you don’t believe me, look at the cover.'),
      ], [
        FB(CHOOSE, '¿＿ no viniste ayer?', ['Por qué', 'Porque', 'Porqué'], 'Por qué', ('Question : por qué.', 'Question: por qué.'), ('Pourquoi n’es-tu pas venu hier ?', 'Why didn’t you come yesterday?')),
        FB(CHOOSE, 'No es francés, ＿ belga.', ['sino', 'si no', 'sí no'], 'sino', ('Après une négation, rectification : sino.', 'After a negative, correction: sino.'), ('Il n’est pas français, mais belge.', 'He isn’t French, but Belgian.')),
        FB(CHOOSE, '＿ no ha llegado el tren.', ['Aún', 'Aun', 'Haún'], 'Aún', ('Encore (= todavía) : aún avec accent.', 'Still (= todavía): aún with an accent.'), ('Le train n’est toujours pas arrivé.', 'The train still hasn’t arrived.')),
        FB(CHOOSE, 'Este regalo es para ＿.', ['ti', 'tí', 'tu'], 'ti', ('Ti ne porte jamais d’accent.', 'Ti never takes an accent.'), ('Ce cadeau est pour toi.', 'This present is for you.')),
      ]),
  ])])

# ═════════════════════════ 4 : le Miroir déformant — l'humour, les euphémismes, les expressions ═════════════════════════
W4 = WORLD('delec2-w4', ('Le Miroir déformant', 'The Distorting Mirror'), REGION,
  ('Saisir l’humour et les jeux de mots, décoder les euphémismes (la tercera edad, pasar a mejor vida) et employer les expressions idiomatiques les plus fines.', 'Catch humour and wordplay, decode euphemisms (la tercera edad, pasar a mejor vida) and use the subtlest idioms.'),
  (('Le Miroir déformant', 'The Distorting Mirror'), '⁂', ('Dans Lumières de bohème de Valle-Inclán (1924), Max Estrella affirme que l’esperpento est né des miroirs concaves de la rue du Chat, à Madrid. L’un d’eux a pris vie dans le Rayon secret et déforme tout ce qu’on lui dit : montre-lui que tu lis entre les lignes.', 'In Valle-Inclán’s Bohemian Lights (1924), Max Estrella claims the esperpento was born from the concave mirrors of the Callejón del Gato in Madrid. One of them has come to life in the Secret Shelf and distorts everything it hears: show it you can read between the lines.')),
  [CH('delec2-w4-c1', ('La rue du Chat', 'The Callejón del Gato'), [
    L('es-humor', ('Les jeux de mots et le double sens', 'Wordplay and double meaning'), ('Comprendre l’humour verbal, les calembours et le double sens.', 'Understand verbal humour, puns and double meaning.'), 10, [
        ('Le calembour (el juego de palabras) joue sur la polysémie : «El banco cerró» (la banque ou le banc ?). «Estar en las nubes» et «tener la cabeza en las nubes».', 'The pun (el juego de palabras) plays on polysemy: «El banco cerró» (the bank or the bench?). «Estar en las nubes» and «tener la cabeza en las nubes».'),
        ('Les chistes (blagues) espagnols aiment les jeux phoniques : «—¿Qué le dice un jaguar a otro? —Jaguar you» (jeu sur l’anglais).', 'Spanish jokes (chistes) love sound play: «—¿Qué le dice un jaguar a otro? —Jaguar you» (a play on English).'),
        ('L’esperpento de Valle-Inclán déforme la réalité pour la critiquer : el esperpento, lo esperpéntico (grotesque et absurde).', 'Valle-Inclán’s esperpento distorts reality to criticise it: el esperpento, lo esperpéntico (grotesque and absurd).'),
      ], [
        S('el-juego-de-palabras', 'el juego de palabras', ('le jeu de mots', 'the pun, wordplay')),
        S('el-chiste', 'el chiste', ('la blague', 'the joke')),
        S('la-polisemia', 'la polisemia', ('la polysémie', 'polysemy')),
        S('el-esperpento', 'el esperpento', ('l’esperpento (grotesque), un épouvantail', 'esperpento (grotesque style)')),
        S('esperpentico', 'esperpéntico / esperpéntica', ('grotesque, absurde', 'grotesque, absurd')),
        S('hacer-gracia', 'hacer gracia', ('faire rire, amuser', 'to amuse')),
        S('el-ingenio', 'el ingenio', ('l’esprit, l’ingéniosité', 'wit, ingenuity')),
        S('el-espejo-concavo', 'el espejo cóncavo', ('le miroir concave', 'the concave mirror')),
      ], [
        x('El chiste no me hizo ninguna gracia, aunque reconozco el ingenio del juego de palabras.', 'La blague ne m’a pas du tout fait rire, même si je reconnais l’ingéniosité du jeu de mots.', 'The joke didn’t amuse me at all, although I acknowledge the wit of the pun.'),
        x('Max Estrella decía que los héroes clásicos, reflejados en los espejos cóncavos, dan el esperpento.', 'Max Estrella disait que les héros classiques, reflétés dans les miroirs concaves, donnent l’esperpento.', 'Max Estrella said that classical heroes, reflected in concave mirrors, produce the esperpento.'),
      ], [
        FB(CHOOSE, 'Su chiste no me ＿ ninguna gracia.', ['hizo', 'puso', 'tuvo'], 'hizo', ('Faire rire : hacer gracia.', 'To amuse: hacer gracia.'), ('Sa blague ne m’a pas fait rire du tout.', 'His joke didn’t amuse me at all.')),
        FB(COMPLETE, 'La escena era tan absurda que resultaba ＿.', ['esperpéntica', 'ingeniosa', 'cóncava'], 'esperpéntica', ('Grotesque et absurde : esperpéntico.', 'Grotesque and absurd: esperpéntico.'), ('La scène était si absurde qu’elle en devenait grotesque.', 'The scene was so absurd that it became grotesque.')),
        TF('«El banco cerró» puede tener dos sentidos.', ('La phrase est ambiguë.', 'The sentence is ambiguous.'), VRAI, ('Banco = banque ou banc.', 'Banco = bank or bench.')),
        DC(ANSWER, [('Espejo', '¿Sabes por qué el libro de matemáticas estaba triste? Porque tenía muchos problemas.')], ('Le miroir te raconte une blague à double sens ; réagis.', 'The mirror tells you a double-meaning joke; react.'), ['¡Qué ingenioso! Juega con el doble sentido de «problemas».', '¡Qué triste el libro!', 'No tengo problemas.'], '¡Qué ingenioso! Juega con el doble sentido de «problemas».', ('Problemas = exercices ou soucis.', 'Problemas = maths problems or worries.')),
      ]),
    L('es-eufemismos', ('La tercera edad, pasar a mejor vida : les euphémismes', 'La tercera edad, pasar a mejor vida: euphemisms'), ('Reconnaître les euphémismes et le langage politiquement correct.', 'Recognise euphemisms and politically correct language.'), 9, [
        ('L’âge et la mort : la tercera edad, las personas mayores (les personnes âgées), pasar a mejor vida, fallecer (décéder), dejarnos (nous quitter).', 'Age and death: la tercera edad, las personas mayores (senior citizens), pasar a mejor vida (to pass away), fallecer (to die, formal), dejarnos (to leave us).'),
        ('Le travail et l’économie : el reajuste de plantilla (la réduction d’effectifs), la desaceleración económica (la crise), el crecimiento negativo, los recursos humanos.', 'Work and the economy: el reajuste de plantilla (staff cuts), la desaceleración económica (downturn), el crecimiento negativo, los recursos humanos.'),
        ('Le handicap et la société : persona con discapacidad, persona invidente (aveugle), persona sin hogar (sans-abri), en situación de vulnerabilidad.', 'Disability and society: persona con discapacidad, persona invidente (blind), persona sin hogar (homeless), en situación de vulnerabilidad.'),
      ], [
        S('el-eufemismo', 'el eufemismo', ('l’euphémisme', 'the euphemism')),
        S('la-tercera-edad', 'la tercera edad', ('le troisième âge', 'old age, senior citizens')),
        S('pasar-a-mejor-vida', 'pasar a mejor vida', ('passer de vie à trépas', 'to pass away')),
        S('fallecer', 'fallecer', ('décéder', 'to pass away, to die (formal)')),
        S('el-reajuste-de-plantilla', 'el reajuste de plantilla', ('la réduction d’effectifs', 'staff cuts')),
        S('la-desaceleracion', 'la desaceleración', ('le ralentissement', 'the slowdown')),
        S('invidente', 'invidente', ('non-voyant', 'blind, visually impaired')),
        S('persona-sin-hogar', 'persona sin hogar', ('sans-abri', 'homeless person')),
      ], [
        x('Max Estrella, poeta invidente, pasó a mejor vida en la miseria, como tantos bohemios de su tiempo.', 'Max Estrella, poète non-voyant, passa de vie à trépas dans la misère, comme tant de bohèmes de son temps.', 'Max Estrella, a blind poet, passed away in poverty, like so many bohemians of his time.'),
        x('La empresa anunció un «reajuste de plantilla»: en realidad, despidió a cien personas.', 'L’entreprise annonça un « ajustement des effectifs » : en réalité, elle licencia cent personnes.', 'The company announced a “staff readjustment”: in reality, it fired a hundred people.'),
      ], [
        FB(CHOOSE, 'El abuelo de Lucía ＿ anoche.', ['falleció', 'deceso', 'fallecido'], 'falleció', ('Décéder (soutenu) : fallecer.', 'To pass away (formal): fallecer.'), ('Le grand-père de Lucía est décédé hier soir.', 'Lucía’s grandfather passed away last night.')),
        FB(COMPLETE, 'Detrás del «＿ de plantilla» se esconden despidos.', ['reajuste', 'crecimiento', 'hogar'], 'reajuste', ('Euphémisme : reajuste de plantilla.', 'Euphemism: reajuste de plantilla.'), ('Derrière l’« ajustement des effectifs » se cachent des licenciements.', 'Behind the “staff readjustment” lie redundancies.')),
        TF('«Crecimiento negativo» significa que la economía crece.', ('L’économie progresse.', 'The economy is growing.'), FAUX, ('C’est un euphémisme pour une baisse.', 'It is a euphemism for a decline.')),
        TF('«Pasar a mejor vida» es una forma suave de decir «morir».', ('C’est un euphémisme de la mort.', 'It is a euphemism for death.'), VRAI, ('Pasar a mejor vida = mourir.', 'Pasar a mejor vida = to die.')),
      ]),
  ]),
  CH('delec2-w4-c2', ('Le café des bohèmes', 'The bohemians’ café'), [
    L('es-expresiones-c2', ('Dar en el clavo, a regañadientes : les expressions fines', 'Dar en el clavo, a regañadientes: subtle idioms'), ('Employer des expressions idiomatiques de niveau maîtrise.', 'Use idioms at mastery level.'), 10, [
        ('Expressions verbales : dar en el clavo (mettre dans le mille), hacer de tripas corazón (prendre son courage à deux mains), echar leña al fuego (jeter de l’huile sur le feu), andarse por las ramas (tourner autour du pot).', 'Verbal idioms: dar en el clavo (to hit the nail on the head), hacer de tripas corazón (to pluck up courage), echar leña al fuego (to add fuel to the fire), andarse por las ramas (to beat about the bush).'),
        ('Locutions adverbiales : a regañadientes (à contrecœur), a trancas y barrancas (tant bien que mal), de buenas a primeras (tout à coup), sin ton ni son (sans rime ni raison), a la chita callando (en douce).', 'Adverbial phrases: a regañadientes (reluctantly), a trancas y barrancas (with great difficulty), de buenas a primeras (all of a sudden), sin ton ni son (for no reason), a la chita callando (on the quiet).'),
        ('Proverbes de maîtrise : a buen entendedor, pocas palabras bastan (à bon entendeur, salut) ; cría cuervos y te sacarán los ojos (nourris un serpent…).', 'Mastery-level proverbs: a buen entendedor, pocas palabras bastan (a word to the wise); cría cuervos y te sacarán los ojos (bite the hand that feeds you).'),
      ], [
        S('dar-en-el-clavo', 'dar en el clavo', ('mettre dans le mille', 'to hit the nail on the head')),
        S('hacer-de-tripas-corazon', 'hacer de tripas corazón', ('prendre son courage à deux mains', 'to pluck up courage')),
        S('echar-lena-al-fuego', 'echar leña al fuego', ('jeter de l’huile sur le feu', 'to add fuel to the fire')),
        S('andarse-por-las-ramas', 'andarse por las ramas', ('tourner autour du pot', 'to beat about the bush')),
        S('a-reganadientes', 'a regañadientes', ('à contrecœur', 'reluctantly')),
        S('a-trancas-y-barrancas', 'a trancas y barrancas', ('tant bien que mal', 'with great difficulty')),
        S('de-buenas-a-primeras', 'de buenas a primeras', ('tout à coup, de but en blanc', 'out of the blue')),
        S('a-buen-entendedor', 'a buen entendedor, pocas palabras bastan', ('à bon entendeur, salut', 'a word to the wise')),
      ], [
        x('No te andes por las ramas: dime qué opinas. — Pues creo que has dado en el clavo.', 'Ne tourne pas autour du pot : dis-moi ce que tu penses. — Eh bien, je crois que tu as mis dans le mille.', 'Don’t beat about the bush: tell me what you think. — Well, I think you’ve hit the nail on the head.'),
        x('Aceptó a regañadientes y terminó la obra a trancas y barrancas.', 'Il accepta à contrecœur et termina l’œuvre tant bien que mal.', 'He reluctantly agreed and finished the work with great difficulty.'),
      ], [
        FB(CHOOSE, 'Con esa respuesta has dado en el ＿.', ['clavo', 'martillo', 'tornillo'], 'clavo', ('Mettre dans le mille : dar en el clavo.', 'To hit the nail on the head: dar en el clavo.'), ('Avec cette réponse, tu as mis dans le mille.', 'With that answer you’ve hit the nail on the head.')),
        FB(CHOOSE, 'No eches más leña al ＿: ya están bastante enfadados.', ['fuego', 'agua', 'viento'], 'fuego', ('Jeter de l’huile sur le feu : echar leña al fuego.', 'To add fuel to the fire: echar leña al fuego.'), ('N’en rajoute pas : ils sont déjà assez fâchés.', 'Don’t add fuel to the fire: they’re angry enough already.')),
        FB(CHOOSE, 'Lo hizo a ＿: no quería en absoluto.', ['regañadientes', 'buenas', 'trancas'], 'regañadientes', ('À contrecœur : a regañadientes.', 'Reluctantly: a regañadientes.'), ('Il l’a fait à contrecœur : il n’en avait aucune envie.', 'He did it reluctantly: he didn’t want to at all.')),
        TF('De buenas a primeras se puso a llorar.', ('Elle s’est mise à pleurer soudainement.', 'She suddenly started crying.'), VRAI, ('De buenas a primeras = tout à coup.', 'De buenas a primeras = all of a sudden.')),
      ]),
  ])])

# ═════════════════════════ 5 : la payada de Martín Fierro — réfuter, nuancer, concéder ═════════════════════════
W5 = WORLD('delec2-w5', ('La payada de Martín Fierro', 'Martín Fierro’s payada'), REGION,
  ('Débattre au plus haut niveau : réfuter une thèse (rebatir, poner en tela de juicio), nuancer son propos (hasta cierto punto, más bien) et concéder avec des tournures littéraires (si bien, así + subjonctif).', 'Debate at the highest level: refute a thesis (rebatir, poner en tela de juicio), qualify what you say (hasta cierto punto, más bien) and concede with literary constructions (si bien, así + subjunctive).'),
  (('Martín Fierro le payador', 'Martín Fierro the Payador'), '✦', ('Martín Fierro, le gaucho du poème de José Hernández (1872), a planté sa guitare sous les étoiles de la pampa du Rayon secret. Comme autrefois face au Moreno, il te défie en payada, un duel de couplets improvisés : réfute, nuance et concède sans jamais perdre le fil.', 'Martín Fierro, the gaucho of José Hernández’s poem (1872), has set up his guitar under the stars of the Secret Shelf’s pampas. As he once did against El Moreno, he challenges you to a payada, a duel of improvised verses: refute, qualify and concede without ever losing the thread.')),
  [CH('delec2-w5-c1', ('La pulpería', 'The pulpería'), [
    L('es-refutar', ('Rebatir, refutar : contredire avec des arguments', 'Rebatir, refutar: contradicting with arguments'), ('Réfuter une thèse et formuler des objections.', 'Refute a thesis and raise objections.'), 10, [
        ('Réfuter : rebatir un argumento, refutar una tesis, desmentir una noticia (démentir), poner en tela de juicio (remettre en question), echar por tierra un razonamiento (le réduire à néant).', 'Refuting: rebatir un argumento, refutar una tesis, desmentir una noticia (to deny a report), poner en tela de juicio (to call into question), echar por tierra un razonamiento (to demolish it).'),
        ('Objecter : objetar que…, plantear una objeción, cabría objetar que… (on pourrait objecter que), carecer de fundamento (être sans fondement), no se sostiene (ne tient pas).', 'Objecting: objetar que…, plantear una objeción, cabría objetar que… (one might object that), carecer de fundamento (to be unfounded), no se sostiene (it doesn’t hold up).'),
        ('Concéder pour mieux réfuter : Es cierto que…, pero… ; Admitamos que…, aun así… ; Nadie niega que + subjonctif…, sin embargo…', 'Conceding in order to refute: Es cierto que…, pero…; Admitamos que…, aun así…; Nadie niega que + subjunctive…, sin embargo…'),
      ], [
        S('rebatir', 'rebatir', ('réfuter, contrer', 'to rebut, to counter')),
        S('objetar', 'objetar', ('objecter', 'to object')),
        S('desmentir', 'desmentir', ('démentir', 'to deny (a report)')),
        S('poner-en-tela-de-juicio', 'poner en tela de juicio', ('remettre en question', 'to call into question')),
        S('echar-por-tierra', 'echar por tierra', ('réduire à néant', 'to demolish, to wreck')),
        S('la-objecion', 'la objeción', ('l’objection', 'the objection')),
        S('carecer-de-fundamento', 'carecer de fundamento', ('être sans fondement', 'to be unfounded')),
        S('la-pulperia', 'la pulpería', ('l’épicerie-bar de la pampa', 'the country store and bar (pampas)')),
      ], [
        x('El Moreno rebatió cada verso de Martín Fierro y puso en tela de juicio su fama de payador.', 'Le Moreno réfuta chaque couplet de Martín Fierro et remit en question sa réputation de payador.', 'El Moreno rebutted every one of Martín Fierro’s verses and called his reputation as a payador into question.'),
        x('Cabría objetar que su argumento carece de fundamento: no cita ninguna fuente.', 'On pourrait objecter que son argument est sans fondement : il ne cite aucune source.', 'One might object that his argument is unfounded: he cites no source.'),
      ], [
        FB(CHOOSE, 'El ministro ＿ la noticia: según él, es completamente falsa.', ['desmintió', 'echó por tierra de', 'objetó a'], 'desmintió', ('Démentir une information : desmentir.', 'To deny a report: desmentir.'), ('Le ministre a démenti l’information : selon lui, elle est complètement fausse.', 'The minister denied the report: according to him, it is completely false.')),
        FB(CHOOSE, 'Esa teoría ＿ de fundamento.', ['carece', 'sobra', 'queda'], 'carece', ('Carecer de = manquer de.', 'Carecer de = to lack.'), ('Cette théorie est sans fondement.', 'That theory is unfounded.')),
        FB(CHOOSE, 'Los nuevos datos ＿ por tierra su hipótesis.', ['echaron', 'pusieron', 'dieron'], 'echaron', ('Réduire à néant : echar por tierra.', 'To demolish: echar por tierra.'), ('Les nouvelles données ont réduit son hypothèse à néant.', 'The new data demolished his hypothesis.')),
        TF('Nadie pone en tela de juicio su talento.', ('Son talent est contesté.', 'His talent is disputed.'), FAUX, ('Poner en tela de juicio = remettre en question ; ici, personne ne le fait.', 'Poner en tela de juicio = to call into question; here nobody does.')),
      ]),
    L('es-matizar', ('Hasta cierto punto : nuancer son propos', 'Hasta cierto punto: qualifying what you say'), ('Nuancer une affirmation et exprimer des degrés d’accord.', 'Qualify a statement and express degrees of agreement.'), 9, [
        ('Nuancer : hasta cierto punto (jusqu’à un certain point), en cierta medida (dans une certaine mesure), a grandes rasgos (en gros), no del todo (pas tout à fait).', 'Qualifying: hasta cierto punto (up to a point), en cierta medida (to some extent), a grandes rasgos (roughly), no del todo (not entirely).'),
        ('Rectifier : más bien (plutôt), mejor dicho (ou plutôt), por así decirlo (pour ainsi dire), valga la expresión (si j’ose dire). Matizar = nuancer ; el matiz = la nuance.', 'Correcting: más bien (rather), mejor dicho (or rather), por así decirlo (so to speak), valga la expresión (if I may put it that way). Matizar = to qualify; el matiz = the nuance.'),
        ('Degrés d’accord : Estoy totalmente de acuerdo < Coincido en parte < No lo veo del todo claro < Discrepo (je ne suis pas d’accord).', 'Degrees of agreement: Estoy totalmente de acuerdo < Coincido en parte < No lo veo del todo claro < Discrepo (I disagree).'),
      ], [
        S('hasta-cierto-punto', 'hasta cierto punto', ('jusqu’à un certain point', 'up to a point')),
        S('en-cierta-medida', 'en cierta medida', ('dans une certaine mesure', 'to some extent')),
        S('a-grandes-rasgos', 'a grandes rasgos', ('en gros, dans les grandes lignes', 'roughly, in broad terms')),
        S('valga-la-expresion', 'valga la expresión', ('si j’ose dire', 'if I may put it that way')),
        S('coincidir-en-parte', 'coincidir en parte', ('être en partie d’accord', 'to partly agree')),
        S('matizar', 'matizar', ('nuancer', 'to qualify, to nuance')),
        S('el-matiz', 'el matiz', ('la nuance', 'the nuance, the shade')),
        S('discrepar', 'discrepar', ('ne pas être d’accord, diverger', 'to differ, to dissent')),
      ], [
        x('Hasta cierto punto tienes razón, pero conviene matizar: no todos los gauchos eran payadores.', 'Jusqu’à un certain point tu as raison, mais il convient de nuancer : tous les gauchos n’étaient pas des payadores.', 'Up to a point you’re right, but it’s worth qualifying that: not all gauchos were payadores.'),
        x('Discrepo, o mejor dicho, coincido solo en parte con su análisis.', 'Je ne suis pas d’accord, ou plutôt, je ne partage qu’en partie son analyse.', 'I disagree, or rather, I only partly agree with his analysis.'),
      ], [
        FB(COMPLETE, 'Estoy de acuerdo, pero solo hasta cierto ＿.', ['punto', 'medida', 'rasgo'], 'punto', ('Jusqu’à un certain point : hasta cierto punto.', 'Up to a point: hasta cierto punto.'), ('Je suis d’accord, mais seulement jusqu’à un certain point.', 'I agree, but only up to a point.')),
        FB(COMPLETE, 'Te lo explico a grandes ＿: luego entramos en detalle.', ['rasgos', 'líneas', 'puntos'], 'rasgos', ('En gros : a grandes rasgos.', 'Roughly: a grandes rasgos.'), ('Je te l’explique dans les grandes lignes : ensuite on entre dans les détails.', 'I’ll explain it in broad terms: then we’ll go into detail.')),
        FB(CHOOSE, 'No es tímido; es, ＿, reservado.', ['más bien', 'a lo más', 'por si acaso'], 'más bien', ('Plutôt : más bien.', 'Rather: más bien.'), ('Il n’est pas timide ; il est plutôt réservé.', 'He isn’t shy; he’s reserved, rather.')),
        TF('«Discrepo» expresa un acuerdo total.', ('Le locuteur est entièrement d’accord.', 'The speaker fully agrees.'), FAUX, ('Discrepar = ne pas être d’accord.', 'Discrepar = to disagree.')),
      ]),
  ]),
  CH('delec2-w5-c2', ('Le duel de guitares', 'The guitar duel'), [
    L('es-concesion-c2', ('Si bien, así me lo pidas : la concession littéraire', 'Si bien, así me lo pidas: literary concession'), ('Exprimer la concession avec des tournures soutenues et familières.', 'Express concession with formal and colloquial constructions.'), 10, [
        ('Soutenu : aun cuando + subjonctif (même si : Aun cuando llueva, saldremos), si bien + indicatif (bien que, s’il est vrai que : Si bien es cierto que canta bien, le falta oficio).', 'Formal: aun cuando + subjunctive (even if: Aun cuando llueva, saldremos), si bien + indicative (although, while it is true that: Si bien es cierto que canta bien, le falta oficio).'),
        ('Littéraire : así + subjonctif (même si : No lo haré así me lo pidas de rodillas), mal que me pese (à mon grand regret), siquiera (ne serait-ce que : Dame siquiera una pista ; ni siquiera = même pas).', 'Literary: así + subjunctive (even if: No lo haré así me lo pidas de rodillas), mal que me pese (much as it pains me), siquiera (at least: Dame siquiera una pista; ni siquiera = not even).'),
        ('Familier : con lo + adjectif + que (vu comme : Con lo listo que es, ha suspendido), y eso que (et pourtant : Llegó tarde, y eso que salió pronto).', 'Colloquial: con lo + adjective + que (considering how: Con lo listo que es, ha suspendido), y eso que (even though: Llegó tarde, y eso que salió pronto).'),
      ], [
        SG('aun-cuando', 'aun cuando + subjuntivo', ('même si (soutenu)', 'even if (formal)')),
        SG('si-bien', 'si bien + indicativo', ('bien que, s’il est vrai que', 'although, while it is true that')),
        SG('asi-subjuntivo', 'así + subjuntivo', ('même si (littéraire)', 'even if (literary)')),
        S('mal-que-me-pese', 'mal que me pese', ('à mon grand regret', 'much as it pains me')),
        S('siquiera', 'siquiera', ('ne serait-ce que, au moins', 'even, at the very least')),
        SG('con-lo-que', 'con lo + adjetivo + que', ('vu comme, alors que', 'considering how')),
        S('y-eso-que', 'y eso que', ('et pourtant, alors même que', 'even though')),
        S('el-payador', 'el payador', ('le payador (chanteur improvisateur)', 'the payador (improvising singer)')),
      ], [
        x('Si bien el Moreno cantaba con maestría, Martín Fierro no se rindió, así le costara la vida.', 'Bien que le Moreno chantât avec maestria, Martín Fierro ne s’avoua pas vaincu, dût-il y laisser la vie.', 'Although El Moreno sang masterfully, Martín Fierro did not give in, even if it cost him his life.'),
        x('Perdió el duelo, y eso que había ensayado toda la noche.', 'Il perdit le duel, alors même qu’il avait répété toute la nuit.', 'He lost the duel, even though he had rehearsed all night.'),
      ], [
        FB(CHOOSE, 'No cambiaré de opinión aun cuando me lo ＿ el mismo presidente.', ['pida', 'pide', 'pidió'], 'pida', ('Aun cuando (même si, hypothèse) + subjonctif.', 'Aun cuando (even if, hypothesis) + subjunctive.'), ('Je ne changerai pas d’avis, même si c’est le président lui-même qui me le demande.', 'I won’t change my mind even if the president himself asks me to.')),
        FB(CHOOSE, 'Si bien ＿ cierto que es joven, tiene mucha experiencia.', ['es', 'sea', 'fuera'], 'es', ('Si bien + indicatif.', 'Si bien + indicative.'), ('S’il est vrai qu’il est jeune, il a beaucoup d’expérience.', 'While it is true that he is young, he has a lot of experience.')),
        FB(CHOOSE, 'Con lo ＿ que es, no entiendo cómo ha suspendido.', ['listo', 'listísimo de', 'más listo'], 'listo', ('Con lo + adjectif + que.', 'Con lo + adjective + que.'), ('Vu comme il est intelligent, je ne comprends pas comment il a échoué.', 'Considering how clever he is, I don’t understand how he failed.')),
        FB(CHOOSE, 'Ni ＿ me saludó: pasó de largo.', ['siquiera', 'tan', 'mal'], 'siquiera', ('Ni siquiera = même pas.', 'Ni siquiera = not even.'), ('Il ne m’a même pas salué : il est passé sans s’arrêter.', 'He didn’t even say hello: he walked straight past.')),
      ]),
  ])])

# ═════════════════════════ 6 : la tortue géante de Quiroga — sons, mouvements, constructions absolues ═════════════════════════
W6 = WORLD('delec2-w6', ('La tortue géante de Quiroga', 'Quiroga’s giant tortoise'), REGION,
  ('Décrire la nature avec précision : les bruits et les cris (zumbar, crujir, aullar), les verbes de mouvement (deslizarse, serpentear) et les constructions absolues du récit (terminada la cena, al llegar).', 'Describe nature precisely: noises and calls (zumbar, crujir, aullar), verbs of movement (deslizarse, serpentear) and absolute constructions in narrative (terminada la cena, al llegar).'),
  (('La Tortue géante de Quiroga', 'Quiroga’s Giant Tortoise'), '✿', ('Dans les Contes de la forêt vierge d’Horacio Quiroga (1918), une tortue géante porte un chasseur malade à travers la jungle jusqu’à Buenos Aires. La voici dans le Rayon secret, couverte de lianes : elle ne laisse passer que ceux qui savent nommer chaque bruit et chaque mouvement de la forêt.', 'In Horacio Quiroga’s South American Jungle Tales (1918), a giant tortoise carries a sick hunter through the jungle all the way to Buenos Aires. Here she is in the Secret Shelf, covered in vines: she only lets through those who can name every sound and every movement of the forest.')),
  [CH('delec2-w6-c1', ('La forêt de Misiones', 'The Misiones forest'), [
    L('es-sonidos', ('Zumbar, crujir, aullar : les bruits et les cris', 'Zumbar, crujir, aullar: noises and calls'), ('Nommer précisément les sons de la nature et des objets.', 'Name the sounds of nature and objects precisely.'), 10, [
        ('Cris d’animaux : el perro ladra, el lobo aúlla, el león ruge, la rana croa, la abeja zumba, el pájaro trina, el caballo relincha.', 'Animal calls: el perro ladra (barks), el lobo aúlla (howls), el león ruge (roars), la rana croa (croaks), la abeja zumba (buzzes), el pájaro trina (trills), el caballo relincha (neighs).'),
        ('Bruits : crujir (craquer : la madera cruje), chirriar (grincer : la puerta chirría), chasquear (claquer), retumbar (retentir, gronder), el estruendo (le fracas), el chapoteo (le clapotis).', 'Noises: crujir (to creak: la madera cruje), chirriar (to squeak: la puerta chirría), chasquear (to snap, to crack), retumbar (to rumble, to boom), el estruendo (the din), el chapoteo (the splashing).'),
        ('L’accent écrit sur le u ou le i en hiatus : aullar → aúlla, chirriar → chirría, reunir → reúne, prohibir → prohíbe.', 'The written accent on u or i in hiatus: aullar → aúlla, chirriar → chirría, reunir → reúne, prohibir → prohíbe.'),
      ], [
        S('zumbar', 'zumbar', ('bourdonner', 'to buzz, to hum')),
        S('aullar', 'aullar', ('hurler (comme un loup)', 'to howl')),
        S('rugir', 'rugir', ('rugir', 'to roar')),
        S('croar', 'croar', ('coasser', 'to croak')),
        S('chasquear', 'chasquear', ('claquer (fouet, doigts, langue)', 'to snap, to crack (a whip)')),
        S('chirriar', 'chirriar', ('grincer', 'to squeak, to screech')),
        S('el-chapoteo', 'el chapoteo', ('le clapotis', 'the splashing, the lapping')),
        S('el-estruendo', 'el estruendo', ('le fracas', 'the din, the crash')),
      ], [
        x('De noche la selva no calla: zumban los mosquitos, croan las ranas y, a lo lejos, ruge un yaguareté.', 'La nuit, la forêt ne se tait pas : les moustiques bourdonnent, les grenouilles coassent et, au loin, rugit un jaguar.', 'At night the jungle is never silent: mosquitoes buzz, frogs croak and, far away, a jaguar roars.'),
        x('Crujían las ramas bajo el peso de la tortuga y el trueno retumbaba sobre el río.', 'Les branches craquaient sous le poids de la tortue et le tonnerre grondait au-dessus du fleuve.', 'The branches creaked under the tortoise’s weight and thunder rumbled over the river.'),
      ], [
        FB(CHOOSE, 'Toda la noche ＿ los lobos en la montaña.', ['aullaron', 'croaron', 'zumbaron'], 'aullaron', ('Le loup hurle : aullar.', 'Wolves howl: aullar.'), ('Les loups ont hurlé toute la nuit dans la montagne.', 'The wolves howled all night in the mountains.')),
        FB(CHOOSE, 'La puerta vieja ＿ cada vez que la abro.', ['chirría', 'ruge', 'trina'], 'chirría', ('Une porte grince : chirriar.', 'A door squeaks: chirriar.'), ('La vieille porte grince chaque fois que je l’ouvre.', 'The old door squeaks every time I open it.')),
        FB(CHOOSE, 'Una abeja me ＿ junto al oído.', ['zumbaba', 'relinchaba', 'aullaba'], 'zumbaba', ('L’abeille bourdonne : zumbar.', 'Bees buzz: zumbar.'), ('Une abeille me bourdonnait près de l’oreille.', 'A bee was buzzing next to my ear.')),
        TF('La rana ruge.', ('C’est le cri de la grenouille.', 'That is the frog’s call.'), FAUX, ('La grenouille coasse : la rana croa.', 'Frogs croak: la rana croa.')),
      ]),
    L('es-movimiento', ('Deslizarse, serpentear : les verbes de mouvement', 'Deslizarse, serpentear: verbs of movement'), ('Décrire un mouvement avec le verbe exact.', 'Describe movement with the exact verb.'), 9, [
        ('Mouvements d’animaux : deslizarse (glisser), arrastrarse (ramper), serpentear (serpenter), revolotear (voleter), trepar (grimper), brincar (bondir).', 'Animal movements: deslizarse (to glide, to slide), arrastrarse (to crawl), serpentear (to wind, to snake), revolotear (to flutter), trepar (to climb), brincar (to leap).'),
        ('Le fleuve et l’eau : el río serpentea, desemboca (se jette), se desborda (déborde) ; zambullirse (plonger), chapotear (patauger), flotar (flotter).', 'The river and water: el río serpentea (winds), desemboca (flows into), se desborda (bursts its banks); zambullirse (to dive), chapotear (to splash about), flotar (to float).'),
        ('Guetter et rôder : acechar (être à l’affût), merodear (rôder), vislumbrar (apercevoir au loin). Attention : zambullirse fait zambulló, zambulleron (sans i).', 'Watching and prowling: acechar (to lie in wait), merodear (to prowl), vislumbrar (to glimpse in the distance). Careful: zambullirse gives zambulló, zambulleron (no i).'),
      ], [
        S('deslizarse', 'deslizarse', ('glisser', 'to glide, to slide')),
        S('arrastrarse', 'arrastrarse', ('ramper', 'to crawl')),
        S('serpentear', 'serpentear', ('serpenter', 'to wind, to snake')),
        S('revolotear', 'revolotear', ('voleter, voltiger', 'to flutter')),
        S('trepar', 'trepar', ('grimper', 'to clamber up')),
        S('zambullirse', 'zambullirse', ('plonger', 'to dive, to plunge')),
        S('acechar', 'acechar', ('guetter, être à l’affût', 'to lie in wait, to stalk')),
        S('merodear', 'merodear', ('rôder', 'to prowl')),
      ], [
        x('El Paraná serpentea entre la selva; un yacaré se desliza en el agua mientras las mariposas revolotean.', 'Le Paraná serpente dans la forêt ; un caïman glisse dans l’eau tandis que les papillons voltigent.', 'The Paraná winds through the jungle; a caiman glides into the water while butterflies flutter about.'),
        x('El yaguareté acechaba entre las cañas, pero los monos ya habían trepado a lo alto del árbol.', 'Le jaguar guettait parmi les roseaux, mais les singes avaient déjà grimpé en haut de l’arbre.', 'The jaguar lay in wait among the reeds, but the monkeys had already climbed to the top of the tree.'),
      ], [
        FB(CHOOSE, 'La serpiente se ＿ silenciosamente entre las hojas.', ['deslizaba', 'revoloteaba', 'zambullía'], 'deslizaba', ('Glisser sans bruit : deslizarse.', 'To slide silently: deslizarse.'), ('Le serpent glissait silencieusement entre les feuilles.', 'The snake slid silently through the leaves.')),
        FB(CHOOSE, 'Los niños se ＿ en el río desde la roca.', ['zambulleron', 'zambullieron', 'trepar'], 'zambulleron', ('Zambullirse : zambulleron, sans i.', 'Zambullirse: zambulleron, no i.'), ('Les enfants ont plongé dans le fleuve depuis le rocher.', 'The children dived into the river from the rock.')),
        FB(CHOOSE, 'Un hombre sospechoso ＿ por el barrio desde ayer.', ['merodea', 'revolotea', 'serpentea'], 'merodea', ('Rôder : merodear.', 'To prowl: merodear.'), ('Un homme suspect rôde dans le quartier depuis hier.', 'A suspicious man has been prowling around the neighbourhood since yesterday.')),
        TF('El mono trepó al árbol.', ('Le singe est descendu de l’arbre.', 'The monkey came down from the tree.'), FAUX, ('Trepar = grimper.', 'Trepar = to climb.')),
      ]),
  ]),
  CH('delec2-w6-c2', ('Le voyage vers Buenos Aires', 'The journey to Buenos Aires'), [
    L('es-construcciones-absolutas', ('Terminada la cena, al llegar : les constructions absolues', 'Terminada la cena, al llegar: absolute constructions'), ('Condenser le récit avec des participes, des gérondifs et des infinitifs.', 'Condense narrative with participles, gerunds and infinitives.'), 10, [
        ('Participe absolu (action terminée) : Terminada la cena, salieron. Dicho esto, se marchó. Una vez + participe : Una vez firmado el contrato, empezaremos. Le participe s’accorde avec son nom.', 'Absolute participle (completed action): Terminada la cena, salieron. Dicho esto, se marchó. Una vez + participle: Una vez firmado el contrato, empezaremos. The participle agrees with its noun.'),
        ('Gérondif de cause : Siendo así, no insisto (puisqu’il en est ainsi). Al + infinitif (au moment où) : Al llegar a la orilla, la tortuga se detuvo.', 'Gerund of cause: Siendo así, no insisto (that being so). Al + infinitive (on, when): Al llegar a la orilla, la tortuga se detuvo.'),
        ('De + infinitif (condition) : De haberlo sabido, habría venido (si j’avais su). De seguir así, nos perderemos (si on continue ainsi).', 'De + infinitive (condition): De haberlo sabido, habría venido (had I known). De seguir así, nos perderemos (if we carry on like this).'),
      ], [
        SG('participio-absoluto', 'terminada la cena, …', ('le participe absolu', 'the absolute participle')),
        SG('una-vez-participio', 'una vez + participio', ('une fois + participe', 'once + past participle')),
        SG('al-infinitivo', 'al + infinitivo', ('en + participe présent, au moment où', 'on, when (+ -ing)')),
        S('de-seguir-asi', 'de seguir así', ('si ça continue ainsi', 'if things carry on like this')),
        S('dicho-esto', 'dicho esto', ('cela dit', 'having said this')),
        S('siendo-asi', 'siendo así', ('puisqu’il en est ainsi', 'that being so')),
        S('el-cazador', 'el cazador / la cazadora', ('le chasseur / la chasseuse', 'the hunter')),
        S('el-caparazon', 'el caparazón', ('la carapace', 'the shell (of a tortoise)')),
      ], [
        x('Una vez curado el cazador, la tortuga emprendió el camino de vuelta a la selva.', 'Une fois le chasseur guéri, la tortue reprit le chemin de la forêt.', 'Once the hunter had recovered, the tortoise set off back to the jungle.'),
        x('Al llegar a Buenos Aires, la tortuga apenas podía caminar; de haber tardado un día más, el hombre habría muerto.', 'En arrivant à Buenos Aires, la tortue pouvait à peine marcher ; si elle avait tardé un jour de plus, l’homme serait mort.', 'On reaching Buenos Aires, the tortoise could barely walk; had she taken one more day, the man would have died.'),
      ], [
        FB(CHOOSE, '＿ la reunión, todos volvieron a casa.', ['Terminada', 'Terminado', 'Terminando de'], 'Terminada', ('Le participe s’accorde : la reunión → terminada.', 'The participle agrees: la reunión → terminada.'), ('La réunion terminée, tout le monde rentra chez soi.', 'Once the meeting was over, everyone went home.')),
        FB(CHOOSE, '＿ salir de casa, me di cuenta de que llovía.', ['Al', 'De', 'Una vez'], 'Al', ('Au moment où : al + infinitif.', 'When: al + infinitive.'), ('En sortant de chez moi, je me suis rendu compte qu’il pleuvait.', 'On leaving home, I realised it was raining.')),
        FB(CHOOSE, 'De ＿ la verdad, no habría firmado.', ['haber sabido', 'sabiendo', 'sabido'], 'haber sabido', ('Condition passée : de + haber + participe.', 'Past condition: de + haber + participle.'), ('Si j’avais su la vérité, je n’aurais pas signé.', 'Had I known the truth, I wouldn’t have signed.')),
        TF('«Dicho esto, se marchó» significa que se fue antes de hablar.', ('Il est parti avant de parler.', 'He left before speaking.'), FAUX, ('Dicho esto = cela dit : il a parlé, puis il est parti.', 'Dicho esto = having said that: he spoke, then left.')),
      ]),
  ])])

# ═════════════════════════ 7 : le brouillard d'Unamuno — lo neutre, valeurs de se, mise en relief ═════════════════════════
W7 = WORLD('delec2-w7', ('Le brouillard d’Unamuno', 'Unamuno’s mist'), REGION,
  ('Manier les ressources expressives : le neutre lo (lo difícil que es), les valeurs de se (se me olvidó, leerse un libro) et la mise en relief (fue él quien…, ¿acaso…?).', 'Handle expressive resources: neuter lo (lo difícil que es), the uses of se (se me olvidó, leerse un libro) and emphasis (fue él quien…, ¿acaso…?).'),
  (('Augusto dans le brouillard', 'Augusto in the Mist'), '◊', ('Dans Brouillard (Niebla, 1914), Augusto Pérez découvre qu’il n’est qu’un personnage et se rend à Salamanque pour supplier son auteur, Miguel de Unamuno, de le laisser vivre. Égaré dans la brume du Rayon secret, Augusto cherche encore la réponse : aide-le à dire l’indicible.', 'In Mist (Niebla, 1914), Augusto Pérez discovers that he is only a character and goes to Salamanca to beg his author, Miguel de Unamuno, to let him live. Lost in the mist of the Secret Shelf, Augusto is still looking for the answer: help him say what cannot be said.')),
  [CH('delec2-w7-c1', ('Salamanque dans la brume', 'Salamanca in the mist'), [
    L('es-lo-neutro', ('Lo difícil que es : le neutre lo', 'Lo difícil que es: neuter lo'), ('Employer lo pour abstraire, insister et résumer.', 'Use lo to abstract, emphasise and sum up.'), 10, [
        ('Lo + adjectif = ce qui est… : lo bueno (le bon côté), lo importante, lo raro es que… Lo + participe : lo dicho (ce qui a été dit).', 'Lo + adjective = what is…: lo bueno (the good thing), lo importante, lo raro es que… Lo + participle: lo dicho (what has been said).'),
        ('Lo + adjectif ou adverbe + que (= à quel point) : No sabes lo difícil que es. Me sorprende lo bien que canta. L’adjectif s’accorde : lo altas que son.', 'Lo + adjective or adverb + que (= how): No sabes lo difícil que es. Me sorprende lo bien que canta. The adjective agrees: lo altas que son.'),
        ('Lo de + nom ou infinitif (l’affaire de) : ¿Te has enterado de lo de Augusto? Locutions : a lo grande (en grand), a lo loco (n’importe comment), lo suyo (pas mal : Le costó lo suyo).', 'Lo de + noun or infinitive (the matter of): ¿Te has enterado de lo de Augusto? Expressions: a lo grande (in style), a lo loco (wildly, without thinking), lo suyo (quite a lot: Le costó lo suyo).'),
      ], [
        S('lo-raro-es-que', 'lo raro es que…', ('ce qui est étrange, c’est que…', 'the strange thing is that…')),
        SG('lo-que-intensidad', 'lo + adjetivo + que', ('à quel point', 'how (+ adjective)')),
        S('lo-de', 'lo de…', ('l’affaire de, l’histoire de', 'the business about, the matter of')),
        S('lo-dicho', 'lo dicho', ('ce qui a été dit, c’est entendu', 'what has been said, as agreed')),
        S('a-lo-grande', 'a lo grande', ('en grand', 'in style, lavishly')),
        S('a-lo-loco', 'a lo loco', ('n’importe comment, à la légère', 'wildly, without thinking')),
        S('lo-suyo', 'lo suyo', ('pas mal, énormément', 'quite a lot, a fair bit')),
        S('la-bruma', 'la bruma', ('la brume', 'the mist, the haze')),
      ], [
        x('Augusto no sabía lo difícil que es ser un personaje: lo peor era no poder decidir su propio destino.', 'Augusto ne savait pas à quel point il est difficile d’être un personnage : le pire était de ne pas pouvoir décider de son propre destin.', 'Augusto didn’t know how hard it is to be a character: the worst thing was not being able to decide his own fate.'),
        x('¿Te has enterado de lo de Augusto? Convencer a su autor le costó lo suyo.', 'Tu connais l’histoire d’Augusto ? Convaincre son auteur lui a donné bien du mal.', 'Have you heard about Augusto? Persuading his author took him quite some effort.'),
      ], [
        FB(CHOOSE, 'No te imaginas lo ＿ que son estas montañas.', ['altas', 'alto', 'altos'], 'altas', ('L’adjectif s’accorde avec le nom : las montañas → altas.', 'The adjective agrees with the noun: las montañas → altas.'), ('Tu n’imagines pas à quel point ces montagnes sont hautes.', 'You can’t imagine how high these mountains are.')),
        FB(CHOOSE, 'Me sorprende lo ＿ que habla español.', ['bien', 'bueno', 'buen'], 'bien', ('Avec un verbe, un adverbe : lo bien que.', 'With a verb, an adverb: lo bien que.'), ('Je suis surpris de voir à quel point il parle bien espagnol.', 'I’m surprised how well he speaks Spanish.')),
        FB(CHOOSE, 'Celebraron la boda a lo ＿: trescientos invitados y fuegos artificiales.', ['grande', 'largo', 'suyo'], 'grande', ('En grand : a lo grande.', 'In style: a lo grande.'), ('Ils ont célébré le mariage en grand : trois cents invités et un feu d’artifice.', 'They celebrated the wedding in style: three hundred guests and fireworks.')),
        TF('«Lo bueno de vivir aquí es el clima.»', ('Le locuteur parle d’un avantage.', 'The speaker is talking about an advantage.'), VRAI, ('Lo bueno = le bon côté.', 'Lo bueno = the good thing.')),
      ]),
    L('es-valores-se', ('Se me olvidó, leerse un libro : les valeurs de se', 'Se me olvidó, leerse un libro: the uses of se'), ('Distinguer le se involontaire, le se d’intensité et le se qui change le sens.', 'Distinguish involuntary se, intensifying se and meaning-changing se.'), 10, [
        ('Se involontaire (on n’en est pas responsable) : se me olvidó la llave, se le cayó el vaso, se nos rompió el coche, se te ocurre una idea. Le verbe s’accorde avec la chose : se me olvidaron las llaves.', 'Involuntary se (not one’s fault): se me olvidó la llave, se le cayó el vaso, se nos rompió el coche, se te ocurre una idea. The verb agrees with the thing: se me olvidaron las llaves.'),
        ('Se d’intensité ou d’accomplissement (avec un complément précis) : comerse una pizza entera, leerse un libro en un día, saberse la lección de memoria, beberse el café de un trago.', 'Intensifying or completive se (with a specific object): comerse una pizza entera, leerse un libro en un día, saberse la lección de memoria, beberse el café de un trago.'),
        ('Se qui change le sens : ir / irse (partir), dormir / dormirse (s’endormir), llevar / llevarse (emporter), negar / negarse a (refuser de), parecer / parecerse a (ressembler à).', 'Meaning-changing se: ir / irse (to leave), dormir / dormirse (to fall asleep), llevar / llevarse (to take away), negar / negarse a (to refuse to), parecer / parecerse a (to look like).'),
      ], [
        SG('se-involuntario', 'se me olvidó, se le cayó', ('le se involontaire', 'involuntary se')),
        SG('se-aspectual', 'comerse, leerse', ('le se d’intensité', 'intensifying se')),
        S('ocurrirsele', 'ocurrírsele algo a alguien', ('venir à l’esprit de quelqu’un', 'to occur to someone')),
        S('caersele', 'caérsele algo a alguien', ('faire tomber sans le vouloir', 'to drop accidentally')),
        S('saberse', 'saberse algo de memoria', ('connaître par cœur', 'to know by heart')),
        S('beberse', 'beberse algo de un trago', ('boire d’un trait', 'to down in one')),
        S('el-personaje', 'el personaje', ('le personnage', 'the character')),
        S('el-autor', 'el autor / la autora', ('l’auteur / l’autrice', 'the author')),
      ], [
        x('Se me olvidó que eras un personaje, Augusto; y a ti se te ocurrió rebelarte contra tu autor.', 'J’avais oublié que tu étais un personnage, Augusto ; et toi, tu as eu l’idée de te rebeller contre ton auteur.', 'I forgot you were a character, Augusto; and it occurred to you to rebel against your author.'),
        x('Unamuno se negó a cambiar el final, aunque Augusto se sabía de memoria todos sus argumentos.', 'Unamuno refusa de changer la fin, bien qu’Augusto connût par cœur tous ses arguments.', 'Unamuno refused to change the ending, although Augusto knew all his arguments by heart.'),
      ], [
        FB(CHOOSE, 'Perdona, se me ＿ las llaves en casa.', ['olvidaron', 'olvidó', 'olvidé'], 'olvidaron', ('Le verbe s’accorde avec les choses : las llaves → olvidaron.', 'The verb agrees with the things: las llaves → olvidaron.'), ('Pardon, j’ai oublié les clés à la maison.', 'Sorry, I left the keys at home.')),
        FB(CHOOSE, 'Se ＿ un libro entero en una tarde.', ['leyó', 'leía de', 'lee a'], 'leyó', ('Se d’accomplissement : leerse un libro.', 'Completive se: leerse un libro.'), ('Il a lu un livre entier en un après-midi.', 'He read a whole book in one afternoon.')),
        FB(CHOOSE, 'El testigo se ＿ a declarar.', ['negó', 'negó de', 'negaba en'], 'negó', ('Refuser de : negarse a.', 'To refuse to: negarse a.'), ('Le témoin a refusé de témoigner.', 'The witness refused to testify.')),
        TF('«Se le cayó el vaso» indica que lo rompió a propósito.', ('Il l’a fait exprès.', 'He did it on purpose.'), FAUX, ('Se involontaire : c’est un accident.', 'Involuntary se: it was an accident.')),
      ]),
  ]),
  CH('delec2-w7-c2', ('La visite à l’auteur', 'The visit to the author'), [
    L('es-enfasis', ('Fue él quien…, ¿acaso…? : la mise en relief', 'Fue él quien…, ¿acaso…?: emphasis'), ('Mettre une idée en relief et poser des questions rhétoriques.', 'Highlight an idea and ask rhetorical questions.'), 10, [
        ('Phrases clivées : ser + élément + relatif. Fue Unamuno quien lo decidió. Es aquí donde nos conocimos. Fue entonces cuando lo entendí. Lo que quiero es… / Lo que pasa es que… Ser se met au temps de la phrase.', 'Cleft sentences: ser + element + relative. Fue Unamuno quien lo decidió. Es aquí donde nos conocimos. Fue entonces cuando lo entendí. Lo que quiero es… / Lo que pasa es que… Ser takes the tense of the sentence.'),
        ('Questions rhétoriques : ¿Acaso no lo sabías? (tu ne le savais donc pas ?), ¿A que no lo adivinas? (je parie que tu ne devines pas), ¿Quién no ha soñado alguna vez…?', 'Rhetorical questions: ¿Acaso no lo sabías? (didn’t you know, then?), ¿A que no lo adivinas? (I bet you can’t guess), ¿Quién no ha soñado alguna vez…?'),
        ('Exclamations d’insistance : ¡Vaya si lo sé! (et comment !), ¡Si será tonto! (qu’est-ce qu’il est bête !), ¡Pues sí que…! (eh bien vraiment…).', 'Emphatic exclamations: ¡Vaya si lo sé! (I certainly do!), ¡Si será tonto! (how silly can he be!), ¡Pues sí que…! (well, really…).'),
      ], [
        SG('oracion-hendida', 'fue… quien / es… donde', ('la phrase clivée (c’est… qui)', 'the cleft sentence (it is… who)')),
        S('acaso-retorico', '¿acaso…?', ('est-ce donc que… ?', 'is it that…?, could it be that…?')),
        S('a-que', '¿a que…?', ('je parie que… ?', 'I bet…?')),
        S('vaya-si', '¡vaya si…!', ('et comment !', 'and how!, I certainly do!')),
        S('lo-que-pasa-es-que', 'lo que pasa es que…', ('le problème, c’est que…', 'the thing is that…')),
        S('el-creador', 'el creador / la creadora', ('le créateur / la créatrice', 'the creator')),
        S('rebelarse', 'rebelarse', ('se rebeller', 'to rebel')),
        S('la-nivola', 'la nivola', ('la « nivola » (le roman selon Unamuno)', 'the “nivola” (Unamuno’s novel form)')),
      ], [
        x('Fue en Salamanca donde Augusto se enfrentó a su creador. —¿Acaso no puedo vivir sin usted? —le preguntó.', 'C’est à Salamanque qu’Augusto affronta son créateur. « Ne puis-je donc pas vivre sans vous ? » lui demanda-t-il.', 'It was in Salamanca that Augusto confronted his creator. “Can I not live without you, then?” he asked.'),
        x('—¿A que no adivinas quién escribió esta nivola? —¡Vaya si lo adivino: Unamuno!', '« Je parie que tu ne devines pas qui a écrit cette nivola ! — Et comment que je devine : Unamuno ! »', '“I bet you can’t guess who wrote this nivola.” “I certainly can: Unamuno!”'),
      ], [
        FB(CHOOSE, 'Fue mi abuela ＿ me enseñó a leer.', ['quien', 'donde', 'cuando'], 'quien', ('Une personne : fue… quien.', 'A person: fue… quien.'), ('C’est ma grand-mère qui m’a appris à lire.', 'It was my grandmother who taught me to read.')),
        FB(CHOOSE, 'Fue en 1914 ＿ se publicó Niebla.', ['cuando', 'donde', 'quien'], 'cuando', ('Le temps : fue… cuando.', 'Time: fue… cuando.'), ('C’est en 1914 que Niebla fut publié.', 'It was in 1914 that Niebla was published.')),
        FB(CHOOSE, '¿＿ no te lo había dicho ya?', ['Acaso', 'Vaya si', 'Lo que'], 'Acaso', ('Question rhétorique : ¿acaso…?', 'Rhetorical question: ¿acaso…?'), ('Est-ce que je ne te l’avais pas déjà dit ?', 'Hadn’t I already told you?')),
        DC(ANSWER, [('Augusto', '¿Sabes tú quién decide mi destino?')], ('Augusto te demande qui décide de son destin ; réponds en insistant sur l’auteur.', 'Augusto asks who decides his fate; answer by emphasising the author.'), ['Es tu autor quien lo decide, no tú.', 'Es tu autor donde lo decide.', 'Lo que tu autor es decide.'], 'Es tu autor quien lo decide, no tú.', ('Mise en relief : es… quien.', 'Emphasis: es… quien.')),
      ]),
  ])])

# ═════════════════════════ 8 : le manuscrit de Cide Hamete — espagnol classique, futur du subjonctif, médiation ═════════════════════════
W8 = WORLD('delec2-w8', ('Le manuscrit de Cide Hamete', 'Cide Hamete’s manuscript'), REGION,
  ('Lire l’espagnol classique (vuestra merced, fermosa), reconnaître le futur du subjonctif des textes juridiques et des proverbes (adonde fueres…), puis reformuler et résumer comme un médiateur.', 'Read classical Spanish (vuestra merced, fermosa), recognise the future subjunctive in legal texts and proverbs (adonde fueres…), then rephrase and summarise like a mediator.'),
  (('Le Manuscrit de Benengeli', 'Benengeli’s Manuscript'), '✧', ('Au chapitre IX du Quichotte, Cervantès raconte avoir acheté à l’Alcaná de Tolède des cahiers en arabe signés Cide Hamete Benengeli, le véritable historien de don Quichotte. Ce manuscrit est le cœur du Rayon secret : pour le refermer, il faudra lire, traduire et résumer comme Cervantès lui-même.', 'In chapter IX of Don Quixote, Cervantes tells how he bought, at the Alcaná market in Toledo, notebooks in Arabic signed by Cide Hamete Benengeli, the true historian of Don Quixote. This manuscript is the heart of the Secret Shelf: to close it, you must read, translate and summarise like Cervantes himself.')),
  [CH('delec2-w8-c1', ('L’Alcaná de Tolède', 'The Alcaná of Toledo'), [
    L('es-espanol-clasico', ('Vuestra merced, fermosa : lire l’espagnol classique', 'Vuestra merced, fermosa: reading classical Spanish'), ('Comprendre les formes de l’espagnol du Siècle d’or.', 'Understand the forms of Golden Age Spanish.'), 10, [
        ('Traitement : vuestra merced (votre grâce, d’où vient usted), vos (tu ou vous de respect), os (vous). Don Quichotte imite la vieille langue des romans de chevalerie : fermosa (hermosa), facer (hacer), desfacer entuertos (redresser les torts).', 'Forms of address: vuestra merced (your grace, the origin of usted), vos (respectful you), os (you, plural). Don Quixote imitates the old language of chivalric romances: fermosa (hermosa), facer (hacer), desfacer entuertos (to right wrongs).'),
        ('Mots anciens : asaz (fort, très), do (où), maguer (bien que), mesmo (mismo), agora (ahora), luengo (largo), la ínsula (l’île).', 'Old words: asaz (very, exceedingly), do (where), maguer (although), mesmo (mismo), agora (ahora), luengo (largo), la ínsula (the isle).'),
        ('Le pronom accolé au verbe conjugué : díjole (le dijo), fuese (se fue), hablóme (me habló). Aujourd’hui, il ne survit que dans un style très littéraire.', 'Pronouns attached to finite verbs: díjole (le dijo), fuese (se fue), hablóme (me habló). Today this only survives in very literary style.'),
      ], [
        S('vuestra-merced', 'vuestra merced', ('votre grâce (ancêtre de usted)', 'your grace (origin of usted)')),
        S('fermoso', 'fermoso / fermosa', ('beau, belle (forme archaïque)', 'fair, beautiful (archaic)')),
        S('desfacer-entuertos', 'desfacer entuertos', ('redresser les torts', 'to right wrongs')),
        S('asaz', 'asaz', ('fort, très (archaïque)', 'very, exceedingly (archaic)')),
        S('agora', 'agora', ('maintenant (archaïque)', 'now (archaic)')),
        S('la-insula', 'la ínsula', ('l’île (archaïque)', 'the isle (archaic)')),
        S('el-hidalgo', 'el hidalgo', ('l’hidalgo, le petit noble', 'the hidalgo, the minor nobleman')),
        S('el-escudero', 'el escudero', ('l’écuyer', 'the squire')),
      ], [
        x('—Vuestra merced no ha de temer —dijo don Quijote—, que yo he venido a desfacer entuertos.', '« Votre grâce n’a rien à craindre, dit don Quichotte, car je suis venu redresser les torts. »', '“Your grace need not fear,” said Don Quixote, “for I have come to right wrongs.”'),
        x('Sancho, el escudero, soñaba con gobernar una ínsula asaz rica.', 'Sancho, l’écuyer, rêvait de gouverner une île fort riche.', 'Sancho, the squire, dreamed of governing an exceedingly rich isle.'),
      ], [
        FB(COMPLETE, 'En español moderno, «vuestra merced» se convirtió en «＿».', ['usted', 'vosotros', 'vos'], 'usted', ('Vuestra merced → vuesarced → usted.', 'Vuestra merced → vuesarced → usted.'), ('En espagnol moderne, « vuestra merced » est devenu « usted ».', 'In modern Spanish, “vuestra merced” became “usted”.')),
        FB(COMPLETE, '«Fermosa» es la forma antigua de «＿».', ['hermosa', 'famosa', 'ferviente'], 'hermosa', ('Le f- initial latin est devenu h- : fermosa → hermosa.', 'Latin initial f- became h-: fermosa → hermosa.'), ('« Fermosa » est la forme ancienne de « hermosa ».', '“Fermosa” is the old form of “hermosa”.')),
        FB(COMPLETE, '«Díjole la verdad» equivale hoy a «＿ dijo la verdad».', ['Le', 'Se', 'Lo'], 'Le', ('Pronom accolé ancien : díjole = le dijo.', 'Old attached pronoun: díjole = le dijo.'), ('« Díjole la verdad » équivaut aujourd’hui à « Le dijo la verdad ».', '“Díjole la verdad” is equivalent today to “Le dijo la verdad”.')),
        TF('Don Quijote quería desfacer entuertos.', ('Il voulait redresser les torts.', 'He wanted to right wrongs.'), VRAI, ('Desfacer entuertos = deshacer agravios.', 'Desfacer entuertos = to undo wrongs.')),
      ]),
    L('es-futuro-subjuntivo', ('Si así fuere : le futur du subjonctif', 'Si así fuere: the future subjunctive'), ('Reconnaître le futur du subjonctif dans les textes juridiques et les proverbes.', 'Recognise the future subjunctive in legal texts and proverbs.'), 9, [
        ('Formation : à partir de la 3e personne du pluriel du passé simple (hablaron → hablare, tuvieron → tuviere, fueron → fuere). Formes : hablare, hablares, hablare, habláremos, hablareis, hablaren.', 'Formation: from the third-person plural of the preterite (hablaron → hablare, tuvieron → tuviere, fueron → fuere). Forms: hablare, hablares, hablare, habláremos, hablareis, hablaren.'),
        ('Emplois actuels : les textes juridiques (El que infringiere esta norma será sancionado ; si hubiere controversia…) et quelques expressions figées : sea lo que fuere (quoi qu’il en soit), venga de donde viniere.', 'Current uses: legal texts (El que infringiere esta norma será sancionado; si hubiere controversia…) and some set phrases: sea lo que fuere (be that as it may), venga de donde viniere.'),
        ('Proverbe : Adonde fueres, haz lo que vieres (à Rome, fais comme les Romains). Dans l’usage courant, on le remplace par le présent du subjonctif ou de l’indicatif : el que infrinja, si hay.', 'Proverb: Adonde fueres, haz lo que vieres (when in Rome, do as the Romans do). In everyday use it is replaced by the present subjunctive or indicative: el que infrinja, si hay.'),
      ], [
        SG('futuro-subjuntivo', 'hablare, tuviere, fuere', ('le futur du subjonctif', 'the future subjunctive')),
        S('sea-lo-que-fuere', 'sea lo que fuere', ('quoi qu’il en soit', 'be that as it may')),
        S('adonde-fueres', 'adonde fueres, haz lo que vieres', ('à Rome, fais comme les Romains', 'when in Rome, do as the Romans do')),
        S('infringir', 'infringir', ('enfreindre', 'to infringe, to break (a rule)')),
        S('la-controversia', 'la controversia', ('la controverse, le litige', 'the controversy, the dispute')),
        S('el-codigo-civil', 'el código civil', ('le code civil', 'the civil code')),
        S('vigente', 'vigente', ('en vigueur', 'in force, current')),
        S('la-clausula', 'la cláusula', ('la clause', 'the clause')),
      ], [
        x('«El que infringiere lo dispuesto en esta cláusula será sancionado», dice un artículo todavía vigente.', '« Quiconque enfreindra les dispositions de cette clause sera sanctionné », dit un article toujours en vigueur.', '“Whoever infringes the provisions of this clause shall be penalised,” says an article that is still in force.'),
        x('Sea lo que fuere, Cervantes siguió el viejo refrán: adonde fueres, haz lo que vieres.', 'Quoi qu’il en soit, Cervantès suivit le vieux proverbe : à Rome, fais comme les Romains.', 'Be that as it may, Cervantes followed the old proverb: when in Rome, do as the Romans do.'),
      ], [
        FB(COMPLETE, 'Adonde ＿, haz lo que vieres.', ['fueres', 'fueras', 'vayas a'], 'fueres', ('Proverbe figé au futur du subjonctif : fueres.', 'Set proverb in the future subjunctive: fueres.'), ('À Rome, fais comme les Romains.', 'When in Rome, do as the Romans do.')),
        FB(COMPLETE, 'Sea lo que ＿, mañana lo sabremos.', ['fuere', 'fue', 'sería'], 'fuere', ('Expression figée : sea lo que fuere.', 'Set phrase: sea lo que fuere.'), ('Quoi qu’il en soit, demain nous le saurons.', 'Be that as it may, we’ll know tomorrow.')),
        FB(COMPLETE, 'En la lengua corriente, «si hubiere dudas» se dice «si ＿ dudas».', ['hay', 'haya', 'habría'], 'hay', ('Si + présent de l’indicatif : si hay.', 'Si + present indicative: si hay.'), ('Dans la langue courante, « si hubiere dudas » se dit « si hay dudas ».', 'In everyday language, “si hubiere dudas” becomes “si hay dudas”.')),
        TF('La ley vigente ya no se aplica.', ('La loi ne s’applique plus.', 'The law no longer applies.'), FAUX, ('Vigente = en vigueur.', 'Vigente = in force.')),
      ]),
  ]),
  CH('delec2-w8-c2', ('Le traducteur morisque', 'The Morisco translator'), [
    L('es-reformular', ('Dicho de otro modo : reformuler et résumer', 'Dicho de otro modo: rephrasing and summarising'), ('Reformuler, résumer et transmettre un texte (médiation).', 'Rephrase, summarise and pass on a text (mediation).'), 10, [
        ('Reformuler : dicho de otro modo, en otras palabras, o lo que es lo mismo (ce qui revient au même), esto es (c’est-à-dire, soutenu).', 'Rephrasing: dicho de otro modo, en otras palabras, o lo que es lo mismo (which amounts to the same thing), esto es (that is, formal).'),
        ('Résumer et conclure : en resumidas cuentas (en somme), en definitiva (en définitive), en suma, a modo de conclusión. Verbes : resumir, sintetizar, parafrasear, condensar.', 'Summarising and concluding: en resumidas cuentas (in short), en definitiva (ultimately), en suma, a modo de conclusión. Verbs: resumir, sintetizar, parafrasear, condensar.'),
        ('Transmettre (médiation) : Según el texto…, El autor sostiene que…, Viene a decir que… (il veut dire en substance que) ; traducir al pie de la letra (mot à mot) ou libremente.', 'Passing on (mediation): Según el texto…, El autor sostiene que…, Viene a decir que… (he is essentially saying that); traducir al pie de la letra (word for word) or libremente.'),
      ], [
        S('esto-es', 'esto es', ('c’est-à-dire (soutenu)', 'that is (formal)')),
        S('o-lo-que-es-lo-mismo', 'o lo que es lo mismo', ('ce qui revient au même', 'which is the same as saying')),
        S('en-resumidas-cuentas', 'en resumidas cuentas', ('en somme, bref', 'in short, all in all')),
        S('en-suma', 'en suma', ('en résumé, au total', 'in sum')),
        S('parafrasear', 'parafrasear', ('paraphraser', 'to paraphrase')),
        S('sintetizar', 'sintetizar', ('synthétiser', 'to synthesise, to sum up')),
        S('venir-a-decir', 'venir a decir', ('vouloir dire en substance', 'to essentially mean')),
        S('al-pie-de-la-letra', 'al pie de la letra', ('à la lettre, mot à mot', 'to the letter, word for word')),
      ], [
        x('El morisco tradujo el manuscrito en poco más de mes y medio; dicho de otro modo, Cervantes no escribió la historia, sino que la mandó traducir.', 'Le morisque traduisit le manuscrit en un peu plus d’un mois et demi ; autrement dit, Cervantès n’écrivit pas l’histoire : il la fit traduire.', 'The Morisco translated the manuscript in little more than a month and a half; put another way, Cervantes did not write the story, he had it translated.'),
        x('En resumidas cuentas, el capítulo viene a decir que toda historia depende de quien la cuenta.', 'En somme, le chapitre veut dire en substance que toute histoire dépend de celui qui la raconte.', 'In short, the chapter essentially says that every story depends on who tells it.'),
      ], [
        FB(CHOOSE, 'Es un poema difícil; ＿, no es para principiantes.', ['dicho de otro modo', 'al pie de la letra', 'sea lo que fuere'], 'dicho de otro modo', ('Reformuler : dicho de otro modo.', 'Rephrasing: dicho de otro modo.'), ('C’est un poème difficile ; autrement dit, il n’est pas pour les débutants.', 'It’s a difficult poem; put another way, it isn’t for beginners.')),
        FB(CHOOSE, 'No lo traduzcas al pie de la ＿: suena muy artificial.', ['letra', 'página', 'palabra'], 'letra', ('Mot à mot : al pie de la letra.', 'Word for word: al pie de la letra.'), ('Ne le traduis pas mot à mot : ça sonne très artificiel.', 'Don’t translate it word for word: it sounds very artificial.')),
        FB(CHOOSE, 'En resumidas ＿, el proyecto ha sido un éxito.', ['cuentas', 'palabras', 'líneas'], 'cuentas', ('En somme : en resumidas cuentas.', 'In short: en resumidas cuentas.'), ('En somme, le projet a été un succès.', 'All in all, the project has been a success.')),
        DC(ANSWER, [('Benengeli', '¿Qué dice, en pocas palabras, el capítulo IX?')], ('Benengeli te demande de résumer le chapitre IX en quelques mots.', 'Benengeli asks you to sum up chapter IX in a few words.'), ['Viene a decir que la historia de don Quijote procede de un manuscrito árabe.', 'Viene decir que el manuscrito al pie.', 'En resumidas palabras, sí.'], 'Viene a decir que la historia de don Quijote procede de un manuscrito árabe.', ('Résumer : viene a decir que…', 'Summarising: viene a decir que…')),
      ]),
  ])])

write_level('DELEC2', ('DELE C2 : le Rayon secret', 'DELE C2: the Secret Shelf'), REGION, 'The Secret Shelf', 51,
  [W1, W2, W3, W4, W5, W6, W7, W8, FINAL('DELEC2', REGION, ('Simulation DELE C2 : la salle des manuscrits', 'DELE C2 simulation: the manuscript room'), 'usage de la langue, compréhension écrite, compréhension auditive et expression écrite intégrée (l’oral n’est pas évalué)', 'use of language, reading comprehension, listening comprehension and integrated written expression (speaking is not assessed)')])
