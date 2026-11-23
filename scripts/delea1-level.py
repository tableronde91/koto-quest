# Niveau DELE A1 (espagnol, CECRL A1) : 8 étapes sur les chemins de la Manche, leçons et examen blanc (français + anglais).
# Mode histoire : l'écuyer·ère de Don Quichotte apaise les créatures des légendes d'Espagne (voir gen-story.py).
# Les notions sont en espagnol (front) avec leur sens en français ; la traduction anglaise du sens sert à l'interface en anglais.
# Usage : python3 scripts/delea1-level.py   (réécrit content/delea1/delea1.json)
from es_common import *

REGION = 'Chemins de la Manche'

# ═════════════════════════ 1 : ¡Hola! — saluer, se présenter, l'alphabet ═════════════════════════
W1 = WORLD('delea1-w1', ('¡Hola! À l’auberge', '¡Hola! At the inn'), REGION,
  ('Saluer et prendre congé, se présenter avec ser et llamarse, épeler son nom et prononcer les lettres propres à l’espagnol (ñ, ll, j, rr).', 'Greet and say goodbye, introduce yourself with ser and llamarse, spell your name and pronounce the letters specific to Spanish (ñ, ll, j, rr).'),
  (('Le Duende farceur', 'The prankster Duende'), 'Á', ('Ce petit lutin des maisons espagnoles cache les clés des chambres et mélange les noms sur le registre de l’auberge. Présente-toi sans faute pour qu’il te rende ta clé !', 'This little goblin of Spanish homes hides the room keys and mixes up the names in the inn’s register. Introduce yourself without a mistake and it will give your key back!')),
  [CH('delea1-w1-c1', ('Premiers mots', 'First words'), [
    L('es-hola', ('¡Hola! Saluer et prendre congé', '¡Hola! Greeting and saying goodbye'), ('Saluer quelqu’un selon le moment de la journée, demander comment il va et dire au revoir.', 'Greet someone according to the time of day, ask how they are and say goodbye.'), 7, [
        ('¡Hola! sert à tout moment. Buenos días = bonjour (le matin, jusqu’au déjeuner, vers 14 h), buenas tardes = bonjour (l’après-midi), buenas noches = bonsoir et bonne nuit.', '¡Hola! works at any time. Buenos días = good morning (until lunch, around 2 p.m.), buenas tardes = good afternoon, buenas noches = good evening and good night.'),
        ('À l’écrit, une question ou une exclamation s’ouvre par un signe à l’envers : ¿Qué tal? ¡Hola!', 'In writing, a question or exclamation opens with an upside-down mark: ¿Qué tal? ¡Hola!'),
        ('¿Qué tal? / ¿Cómo estás? = comment vas-tu ? Réponse : Bien, gracias. ¿Y tú? Pour partir : adiós, hasta luego (à plus tard), hasta mañana (à demain).', '¿Qué tal? / ¿Cómo estás? = how are you? Answer: Bien, gracias. ¿Y tú? When leaving: adiós, hasta luego (see you later), hasta mañana (see you tomorrow).'),
      ], [
        S('hola', 'hola', ('salut, bonjour', 'hi, hello')),
        S('buenos-dias', 'buenos días', ('bonjour (le matin)', 'good morning')),
        S('buenas-tardes', 'buenas tardes', ('bonjour (l’après-midi)', 'good afternoon')),
        S('buenas-noches', 'buenas noches', ('bonsoir, bonne nuit', 'good evening, good night')),
        S('que-tal', '¿Qué tal?', ('Comment ça va ?', 'How are things?')),
        S('bien', 'bien', ('bien', 'well, fine')),
        S('gracias', 'gracias', ('merci', 'thank you')),
        S('adios', 'adiós', ('au revoir', 'goodbye')),
        S('hasta-luego', 'hasta luego', ('à plus tard', 'see you later')),
      ], [
        x('¡Buenos días, don Quijote! — ¡Buenos días! ¿Qué tal?', 'Bonjour, don Quichotte ! — Bonjour ! Comment ça va ?', 'Good morning, Don Quixote! — Good morning! How are things?'),
        x('Bien, gracias. ¿Y tú?', 'Bien, merci. Et toi ?', 'Fine, thanks. And you?'),
      ], [
        DC(ANSWER, [('Sancho', '¡Hola! ¿Qué tal?')], ('Sancho te demande comment tu vas.', 'Sancho asks how you are.'), ['Bien, gracias. ¿Y tú?', 'Buenas noches.', 'Me llamo Ana.'], 'Bien, gracias. ¿Y tú?', ('À ¿Qué tal?, on répond Bien, gracias.', 'You answer ¿Qué tal? with Bien, gracias.')),
        FB(COMPLETE, 'Son las nueve de la mañana: ¡Buenos ＿!', ['días', 'tardes', 'noches'], 'días', ('Le matin : buenos días.', 'In the morning: buenos días.'), ('Il est neuf heures du matin : bonjour !', 'It’s nine in the morning: good morning!')),
        TF('¡Adiós! Hasta mañana.', ('La personne arrive.', 'The person is arriving.'), FAUX, ('Adiós, hasta mañana = au revoir, à demain : la personne s’en va.', 'Adiós, hasta mañana = goodbye, see you tomorrow: the person is leaving.')),
        FB(COMPLETE, 'Son las diez de la noche. ¡Buenas ＿!', ['noches', 'días', 'tardes'], 'noches', ('Le soir : buenas noches.', 'In the evening: buenas noches.'), ('Il est dix heures du soir. Bonsoir !', 'It’s ten at night. Good evening!')),
      ]),
    L('es-ser-yo', ('Je suis… : soy, eres, se llama', 'I am…: soy, eres, se llama'), ('Se présenter, dire sa nationalité et demander le nom de quelqu’un.', 'Introduce yourself, give your nationality and ask someone’s name.'), 8, [
        ('Le verbe ser (être) au singulier : yo soy (je suis), tú eres (tu es), él / ella es (il / elle est), usted es (vous êtes, poli). Le pronom sujet se laisse souvent tomber : Soy francés.', 'The verb ser (to be) in the singular: yo soy, tú eres, él / ella es, usted es (polite you). The subject pronoun is often dropped: Soy francés.'),
        ('Me llamo… = je m’appelle… ; ¿Cómo te llamas? = comment t’appelles-tu ? ; ¿Cómo se llama usted? (poli). Mucho gusto / encantado, encantada = enchanté·e.', 'Me llamo… = my name is…; ¿Cómo te llamas? = what’s your name?; ¿Cómo se llama usted? (polite). Mucho gusto / encantado, encantada = pleased to meet you.'),
        ('Les nationalités s’accordent : francés / francesa, español / española, inglés / inglesa ; elles s’écrivent sans majuscule.', 'Nationalities agree in gender: francés / francesa, español / española, inglés / inglesa; they take no capital letter.'),
      ], [
        SG('ser-sing', 'yo soy / tú eres / él es', ('je suis / tu es / il est (ser)', 'I am / you are / he is (ser)')),
        S('me-llamo', 'me llamo…', ('je m’appelle…', 'my name is…')),
        S('como-te-llamas', '¿Cómo te llamas?', ('Comment t’appelles-tu ?', 'What’s your name?')),
        S('mucho-gusto', 'mucho gusto', ('ravi de vous rencontrer', 'pleased to meet you')),
        S('frances', 'francés / francesa', ('français / française', 'French (m / f)')),
        S('espanol', 'español / española', ('espagnol / espagnole', 'Spanish (m / f)')),
        S('usted', 'usted', ('vous (politesse, une personne)', 'you (polite, singular)')),
        S('senor', 'señor / señora', ('monsieur / madame', 'Mr / Mrs, sir / madam')),
      ], [
        x('Me llamo Teresa. Soy francesa, de Lyon.', 'Je m’appelle Teresa. Je suis française, de Lyon.', 'My name is Teresa. I’m French, from Lyon.'),
        x('¿Cómo se llama usted? — Me llamo Alonso Quijano. Mucho gusto.', 'Comment vous appelez-vous ? — Je m’appelle Alonso Quijano. Enchanté.', 'What is your name? — My name is Alonso Quijano. Pleased to meet you.'),
      ], [
        FB(CHOOSE, 'Yo ＿ francés.', ['soy', 'eres', 'es'], 'soy', ('Avec yo : soy.', 'With yo: soy.'), ('Je suis français.', 'I am French.')),
        FB(CHOOSE, 'Ella ＿ española.', ['es', 'soy', 'eres'], 'es', ('Avec él / ella : es.', 'With él / ella: es.'), ('Elle est espagnole.', 'She is Spanish.')),
        DC(ANSWER, [('Posadera', '¿Cómo te llamas?')], ('L’aubergiste te demande ton nom.', 'The innkeeper asks your name.'), ['Me llamo Lucas.', 'Soy de Madrid.', 'Muy bien, gracias.'], 'Me llamo Lucas.', ('On donne son nom avec me llamo.', 'You give your name with me llamo.')),
        order(('Remets dans l’ordre : « Je m’appelle Sancho, enchanté. »', 'Put in order: “My name is Sancho, pleased to meet you.”'), ['Me', 'llamo', 'Sancho,', 'mucho', 'gusto.'], ('Me llamo + prénom, puis mucho gusto.', 'Me llamo + name, then mucho gusto.')),
      ]),
  ]),
  CH('delea1-w1-c2', ('Le registre de l’auberge', 'The inn’s register'), [
    L('es-alfabeto', ('L’alphabet et les sons espagnols', 'The alphabet and Spanish sounds'), ('Épeler son nom et prononcer les lettres propres à l’espagnol.', 'Spell your name and pronounce the letters specific to Spanish.'), 8, [
        ('L’espagnol se lit comme il s’écrit. Toutes les lettres se prononcent : la e finale aussi (noche = « notché »), le u se dit « ou » (luna).', 'Spanish is read as it is written. Every letter is pronounced: the final e too (noche = “NO-cheh”), u sounds like “oo” (luna).'),
        ('Les sons à retenir : ñ = « gn » (España), ll = « y » (llamarse), j et g devant e, i = un h raclé (jamón, gente), h ne se prononce jamais (hola = « ola »), rr = r roulé fort (perro).', 'Sounds to learn: ñ = “ny” (España), ll = “y” (llamarse), j and g before e, i = a throaty h (jamón, gente), h is never pronounced (hola = “O-la”), rr = strongly rolled r (perro).'),
        ('Pour épeler : ¿Cómo se escribe? = comment ça s’écrit ? La lettre ñ s’appelle eñe, la h hache, la j jota, la g ge.', 'To spell: ¿Cómo se escribe? = how do you spell it? The letter ñ is called eñe, h is hache, j is jota, g is ge.'),
      ], [
        S('como-se-escribe', '¿Cómo se escribe?', ('Comment ça s’écrit ?', 'How do you spell it?')),
        S('letra', 'la letra', ('la lettre', 'the letter')),
        S('ene', 'la eñe (ñ)', ('la lettre ñ', 'the letter ñ')),
        S('espana', 'España', ('l’Espagne', 'Spain')),
        S('nombre', 'el nombre', ('le prénom, le nom', 'the first name, the name')),
        S('apellido', 'el apellido', ('le nom de famille', 'the surname')),
        S('perro', 'el perro', ('le chien', 'the dog')),
        S('noche', 'la noche', ('la nuit', 'the night')),
      ], [
        x('¿Cómo se escribe tu apellido? — Pe, e, erre, e, zeta: Pérez.', 'Comment s’écrit ton nom de famille ? — P, E, R, E, Z : Pérez.', 'How do you spell your surname? — P, E, R, E, Z: Pérez.'),
        x('Mi nombre es Iñigo, con eñe.', 'Mon prénom est Iñigo, avec un ñ.', 'My first name is Iñigo, with an ñ.'),
      ], [
        DC(ANSWER, [('Posadero', '¿Cómo se escribe tu nombre?')], ('L’aubergiste veut savoir comment s’écrit ton prénom.', 'The innkeeper wants to know how to spell your first name.'), ['A, ene, a: Ana.', 'Soy de Francia.', 'Hasta mañana.'], 'A, ene, a: Ana.', ('On épelle lettre par lettre.', 'You spell it letter by letter.')),
        FB(COMPLETE, 'Mi ＿ es García. — ¿Y tu nombre? — Lucía.', ['apellido', 'letra', 'noche'], 'apellido', ('García est un nom de famille : apellido.', 'García is a surname: apellido.'), ('Mon nom de famille est García. — Et ton prénom ? — Lucía.', 'My surname is García. — And your first name? — Lucía.')),
        TF('En «hola», la hache no se pronuncia.', ('Le h de hola ne se prononce pas.', 'The h in hola is silent.'), VRAI, ('Le h espagnol est toujours muet.', 'The Spanish h is always silent.')),
        TF('«España» se escribe con eñe.', ('España s’écrit avec un ñ.', 'España is spelt with an ñ.'), VRAI, ('España : e, ese, pe, a, eñe, a.', 'España: e, ese, pe, a, eñe, a.')),
      ]),
  ])])

# ═════════════════════════ 2 : la famille de Sancho — famille, tener, nombres ═════════════════════════
W2 = WORLD('delea1-w2', ('La maison de Sancho', 'Sancho’s house'), REGION,
  ('Présenter sa famille avec les possessifs (mi, tu, su), dire son âge avec tener et compter jusqu’à cent.', 'Introduce your family with possessives (mi, tu, su), give your age with tener and count to a hundred.'),
  (('Le Trasgu de la cuisine', 'The kitchen Trasgu'), 'É', ('Le Trasgu, lutin asturien boiteux au bonnet rouge, renverse les casseroles et cache les photos de famille chez Sancho. Montre-lui que tu connais chaque membre de la famille pour qu’il range la cuisine.', 'The Trasgu, a limping Asturian goblin with a red cap, knocks over the pans and hides the family photos at Sancho’s. Show it that you know every member of the family so it tidies the kitchen.')),
  [CH('delea1-w2-c1', ('Teresa et les enfants', 'Teresa and the children'), [
    L('es-familia', ('La famille : mi, tu, su', 'The family: mi, tu, su'), ('Nommer les membres de sa famille et utiliser les possessifs.', 'Name family members and use possessives.'), 8, [
        ('Possessifs devant le nom : mi (mon, ma), tu (ton, ta), su (son, sa, votre) ; au pluriel : mis, tus, sus. Mi padre, mis padres.', 'Possessives before the noun: mi (my), tu (your), su (his, her, your polite); plural: mis, tus, sus. Mi padre, mis padres.'),
        ('Los padres = les parents (le père et la mère) ; los hermanos = les frères et sœurs ; los hijos = les enfants (fils et filles). Le masculin pluriel englobe les deux.', 'Los padres = the parents (father and mother); los hermanos = brothers and sisters; los hijos = the children (sons and daughters). The masculine plural covers both.'),
        ('¿Tienes hermanos? = as-tu des frères et sœurs ? Sí, tengo una hermana. / No, soy hijo único (fils unique).', '¿Tienes hermanos? = do you have brothers and sisters? Sí, tengo una hermana. / No, soy hijo único (only child).'),
      ], [
        SG('posesivos', 'mi / tu / su', ('mon / ton / son (possessifs)', 'my / your / his-her (possessives)')),
        S('padre', 'el padre', ('le père', 'the father')),
        S('madre', 'la madre', ('la mère', 'the mother')),
        S('padres', 'los padres', ('les parents', 'the parents')),
        S('hermano', 'el hermano / la hermana', ('le frère / la sœur', 'the brother / the sister')),
        S('hijo', 'el hijo / la hija', ('le fils / la fille', 'the son / the daughter')),
        S('abuelo', 'el abuelo / la abuela', ('le grand-père / la grand-mère', 'the grandfather / the grandmother')),
        S('marido', 'el marido / la mujer', ('le mari / la femme (épouse)', 'the husband / the wife')),
        S('familia', 'la familia', ('la famille', 'the family')),
      ], [
        x('Teresa es la mujer de Sancho. Sus hijos se llaman Sanchico y Sanchica.', 'Teresa est la femme de Sancho. Leurs enfants s’appellent Sanchico et Sanchica.', 'Teresa is Sancho’s wife. Their children are called Sanchico and Sanchica.'),
        x('¿Tienes hermanos? — Sí, tengo dos hermanas.', 'As-tu des frères et sœurs ? — Oui, j’ai deux sœurs.', 'Do you have brothers and sisters? — Yes, I have two sisters.'),
      ], [
        FB(CHOOSE, 'Esta es ＿ madre. Se llama Carmen.', ['mi', 'mis', 'yo'], 'mi', ('Un seul nom au singulier : mi.', 'One singular noun: mi.'), ('Voici ma mère. Elle s’appelle Carmen.', 'This is my mother. Her name is Carmen.')),
        FB(CHOOSE, '¿Cómo se llaman ＿ padres?', ['tus', 'tu', 'tú'], 'tus', ('Padres est pluriel : tus.', 'Padres is plural: tus.'), ('Comment s’appellent tes parents ?', 'What are your parents’ names?')),
        TF('El padre de mi madre es mi abuelo.', ('Le père de ma mère est mon grand-père.', 'My mother’s father is my grandfather.'), VRAI, ('Abuelo = grand-père.', 'Abuelo = grandfather.')),
        DC(ANSWER, [('Teresa', '¿Tienes hermanos?')], ('Teresa te demande si tu as des frères et sœurs.', 'Teresa asks if you have brothers and sisters.'), ['Sí, tengo un hermano.', 'Sí, soy un hermano.', 'Tengo veinte años.'], 'Sí, tengo un hermano.', ('On répond avec tengo (j’ai).', 'You answer with tengo (I have).')),
      ]),
    L('es-tener', ('J’ai vingt ans : tener', 'I’m twenty: tener'), ('Dire son âge et ce qu’on possède avec tener.', 'Give your age and say what you have with tener.'), 8, [
        ('Tener (avoir) : tengo, tienes, tiene, tenemos, tenéis, tienen. Il sert aussi pour l’âge : Tengo veinte años (j’ai vingt ans).', 'Tener (to have): tengo, tienes, tiene, tenemos, tenéis, tienen. It is also used for age: Tengo veinte años (I am twenty).'),
        ('¿Cuántos años tienes? = quel âge as-tu ? (littéralement « combien d’années as-tu ? »).', '¿Cuántos años tienes? = how old are you? (literally “how many years do you have?”).'),
        ('Tener aussi pour des sensations : tengo hambre (j’ai faim), tengo sed (j’ai soif), tengo frío (j’ai froid).', 'Tener is also used for sensations: tengo hambre (I’m hungry), tengo sed (I’m thirsty), tengo frío (I’m cold).'),
      ], [
        SG('tener', 'tengo / tienes / tiene', ('j’ai / tu as / il a (tener)', 'I have / you have / he has (tener)')),
        S('cuantos-anos', '¿Cuántos años tienes?', ('Quel âge as-tu ?', 'How old are you?')),
        S('ano', 'el año', ('l’an, l’année', 'the year')),
        S('hambre', 'tener hambre', ('avoir faim', 'to be hungry')),
        S('sed', 'tener sed', ('avoir soif', 'to be thirsty')),
        S('casa', 'la casa', ('la maison', 'the house')),
        S('gato', 'el gato', ('le chat', 'the cat')),
        S('burro', 'el burro', ('l’âne', 'the donkey')),
      ], [
        x('Sancho tiene un burro que se llama Rucio.', 'Sancho a un âne qui s’appelle Grison.', 'Sancho has a donkey called Dapple.'),
        x('¿Cuántos años tienes? — Tengo diecinueve años.', 'Quel âge as-tu ? — J’ai dix-neuf ans.', 'How old are you? — I’m nineteen.'),
      ], [
        FB(CHOOSE, 'Yo ＿ veinte años.', ['tengo', 'tiene', 'soy'], 'tengo', ('L’âge se dit avec tener : tengo.', 'Age uses tener: tengo.'), ('J’ai vingt ans.', 'I am twenty.')),
        FB(CHOOSE, 'Mi hermana ＿ un gato negro.', ['tiene', 'tengo', 'tienes'], 'tiene', ('Avec ella : tiene.', 'With ella: tiene.'), ('Ma sœur a un chat noir.', 'My sister has a black cat.')),
        DC(ANSWER, [('Sanchica', '¿Cuántos años tienes?')], ('Sanchica te demande ton âge.', 'Sanchica asks your age.'), ['Tengo dieciocho años.', 'Soy dieciocho años.', 'Me llamo dieciocho.'], 'Tengo dieciocho años.', ('L’âge : tengo + nombre + años.', 'Age: tengo + number + años.')),
        TF('Tengo sed: quiero agua.', ('La personne a soif.', 'The person is thirsty.'), VRAI, ('Tener sed = avoir soif.', 'Tener sed = to be thirsty.')),
      ]),
  ]),
  CH('delea1-w2-c2', ('Compter les moutons', 'Counting the sheep'), [
    L('es-numeros', ('Les nombres de 0 à 100', 'Numbers from 0 to 100'), ('Compter, donner un numéro de téléphone et un âge.', 'Count, give a phone number and an age.'), 9, [
        ('0 cero, 1 uno, 2 dos, 3 tres, 4 cuatro, 5 cinco, 6 seis, 7 siete, 8 ocho, 9 nueve, 10 diez, 11 once, 12 doce, 13 trece, 14 catorce, 15 quince.', '0 cero, 1 uno, 2 dos, 3 tres, 4 cuatro, 5 cinco, 6 seis, 7 siete, 8 ocho, 9 nueve, 10 diez, 11 once, 12 doce, 13 trece, 14 catorce, 15 quince.'),
        ('De 16 à 29, un seul mot : dieciséis, diecisiete… veinte, veintiuno, veintidós. Ensuite on ajoute y : treinta y uno, cuarenta y cinco.', 'From 16 to 29, one word: dieciséis, diecisiete… veinte, veintiuno, veintidós. After that, add y: treinta y uno, cuarenta y cinco.'),
        ('Les dizaines : treinta (30), cuarenta (40), cincuenta (50), sesenta (60), setenta (70), ochenta (80), noventa (90), cien (100).', 'The tens: treinta (30), cuarenta (40), cincuenta (50), sesenta (60), setenta (70), ochenta (80), noventa (90), cien (100).'),
      ], [
        S('cero', 'cero', ('zéro', 'zero')),
        S('cinco', 'cinco', ('cinq', 'five')),
        S('diez', 'diez', ('dix', 'ten')),
        S('quince', 'quince', ('quinze', 'fifteen')),
        S('veinte', 'veinte', ('vingt', 'twenty')),
        S('treinta-y-uno', 'treinta y uno', ('trente et un', 'thirty-one')),
        S('cincuenta', 'cincuenta', ('cinquante', 'fifty')),
        S('cien', 'cien', ('cent', 'a hundred')),
        S('telefono', 'el número de teléfono', ('le numéro de téléphone', 'the phone number')),
      ], [
        x('Sancho tiene cuarenta y cinco ovejas.', 'Sancho a quarante-cinq brebis.', 'Sancho has forty-five sheep.'),
        x('Mi número de teléfono es el seis, uno, dos, treinta y cuatro…', 'Mon numéro de téléphone est le six, un, deux, trente-quatre…', 'My phone number is six, one, two, thirty-four…'),
      ], [
        FB(COMPLETE, 'Diez y cinco son ＿.', ['quince', 'cincuenta', 'doce'], 'quince', ('10 + 5 = 15 : quince.', '10 + 5 = 15: quince.'), ('Dix et cinq font quinze.', 'Ten and five make fifteen.')),
        FB(COMPLETE, 'Treinta y treinta son ＿.', ['sesenta', 'setenta', 'treinta'], 'sesenta', ('30 + 30 = 60 : sesenta.', '30 + 30 = 60: sesenta.'), ('Trente et trente font soixante.', 'Thirty and thirty make sixty.')),
        TF('«Cien» es el número 100.', ('Cien = 100.', 'Cien = 100.'), VRAI, ('Cien = cent.', 'Cien = a hundred.')),
        TF('«Cuarenta» es el número 14.', ('Cuarenta = 14.', 'Cuarenta = 14.'), FAUX, ('Cuarenta = 40 ; 14 = catorce.', 'Cuarenta = 40; 14 = catorce.')),
      ]),
  ])])

# ═════════════════════════ 3 : le village — lieux, hay et estar, articles ═════════════════════════
W3 = WORLD('delea1-w3', ('Un village de la Manche', 'A village in La Mancha'), REGION,
  ('Les lieux de la ville avec hay (il y a) et estar (se trouver), les articles et le pluriel, demander son chemin.', 'Places in town with hay (there is) and estar (to be located), articles and plurals, asking the way.'),
  (('Le Nuberu des nuages', 'The cloud Nuberu'), 'Í', ('Le Nuberu, maître des nuages vêtu de peaux de chèvre, fait tomber la grêle sur le village et brouille les panneaux. Retrouve chaque lieu pour qu’il chasse l’orage.', 'The Nuberu, master of clouds dressed in goatskins, makes hail fall on the village and scrambles the signs. Find every place so it drives away the storm.')),
  [CH('delea1-w3-c1', ('La place du village', 'The village square'), [
    L('es-hay', ('Il y a une église : hay, el / la, un / una', 'There is a church: hay, el / la, un / una'), ('Décrire un lieu avec hay et les articles.', 'Describe a place with hay and the articles.'), 8, [
        ('Hay = il y a (invariable) : hay una iglesia, hay dos bares. ¿Hay un banco por aquí? = y a-t-il une banque par ici ?', 'Hay = there is / there are (invariable): hay una iglesia, hay dos bares. ¿Hay un banco por aquí? = is there a bank around here?'),
        ('Articles : el (masculin), la (féminin), los, las (pluriel) ; un, una (indéfinis). Les noms en -o sont souvent masculins (el museo), en -a souvent féminins (la plaza).', 'Articles: el (masculine), la (feminine), los, las (plural); un, una (indefinite). Nouns in -o are usually masculine (el museo), in -a usually feminine (la plaza).'),
        ('Pluriel : -s après une voyelle (la casa → las casas), -es après une consonne (el hotel → los hoteles).', 'Plural: -s after a vowel (la casa → las casas), -es after a consonant (el hotel → los hoteles).'),
      ], [
        SG('hay', 'hay…', ('il y a…', 'there is / there are…')),
        SG('articulos', 'el / la / los / las', ('le / la / les (articles)', 'the (articles)')),
        S('plaza', 'la plaza', ('la place', 'the square')),
        S('iglesia', 'la iglesia', ('l’église', 'the church')),
        S('calle', 'la calle', ('la rue', 'the street')),
        S('banco', 'el banco', ('la banque ; le banc', 'the bank; the bench')),
        S('farmacia', 'la farmacia', ('la pharmacie', 'the chemist’s, the pharmacy')),
        S('mercado', 'el mercado', ('le marché', 'the market')),
        S('hotel', 'el hotel', ('l’hôtel', 'the hotel')),
      ], [
        x('En la plaza hay una iglesia, un bar y dos tiendas.', 'Sur la place, il y a une église, un bar et deux magasins.', 'In the square there is a church, a bar and two shops.'),
        x('Perdone, ¿hay una farmacia por aquí?', 'Excusez-moi, y a-t-il une pharmacie par ici ?', 'Excuse me, is there a chemist’s around here?'),
      ], [
        FB(CHOOSE, 'En mi calle ＿ un mercado.', ['hay', 'es', 'tiene'], 'hay', ('Il y a : hay.', 'There is: hay.'), ('Dans ma rue, il y a un marché.', 'In my street there is a market.')),
        FB(CHOOSE, '＿ iglesia es muy antigua.', ['La', 'El', 'Los'], 'La', ('Iglesia est féminin : la.', 'Iglesia is feminine: la.'), ('L’église est très ancienne.', 'The church is very old.')),
        FB(CHOOSE, 'En el pueblo hay tres ＿.', ['hoteles', 'hotels', 'hotel'], 'hoteles', ('Après une consonne : -es.', 'After a consonant: -es.'), ('Dans le village, il y a trois hôtels.', 'In the village there are three hotels.')),
        TF('Hay dos bancos en la plaza.', ('Il y a une seule banque.', 'There is only one bank.'), FAUX, ('Dos bancos = deux banques (ou bancs).', 'Dos bancos = two banks (or benches).')),
      ]),
    L('es-estar-lugar', ('Où est la poste ? estar', 'Where is the post office? estar'), ('Situer un lieu avec estar et les prépositions de lieu.', 'Locate a place with estar and prepositions of place.'), 8, [
        ('Estar (se trouver) : estoy, estás, está, estamos, estáis, están. ¿Dónde está el hotel? = où est l’hôtel ? Hay présente un lieu nouveau ; estar situe un lieu connu.', 'Estar (to be located): estoy, estás, está, estamos, estáis, están. ¿Dónde está el hotel? = where is the hotel? Hay introduces a new place; estar locates a known one.'),
        ('Prépositions : al lado de (à côté de), enfrente de (en face de), cerca de / lejos de (près de / loin de), entre (entre). De + el = del : al lado del bar.', 'Prepositions: al lado de (next to), enfrente de (opposite), cerca de / lejos de (near / far from), entre (between). De + el = del: al lado del bar.'),
        ('A + el = al : voy al mercado (je vais au marché).', 'A + el = al: voy al mercado (I’m going to the market).'),
      ], [
        SG('estar-lugar', 'está / están (lieu)', ('se trouve / se trouvent (estar)', 'is / are located (estar)')),
        S('donde', '¿Dónde está…?', ('Où est… ?', 'Where is…?')),
        S('al-lado', 'al lado de', ('à côté de', 'next to')),
        S('enfrente', 'enfrente de', ('en face de', 'opposite')),
        S('cerca', 'cerca de', ('près de', 'near to, close to')),
        S('lejos', 'lejos de', ('loin de', 'far from')),
        S('correos', 'Correos', ('la poste', 'the post office')),
        S('estacion', 'la estación', ('la gare', 'the station')),
      ], [
        x('¿Dónde está Correos? — Está enfrente de la iglesia.', 'Où est la poste ? — Elle est en face de l’église.', 'Where is the post office? — It is opposite the church.'),
        x('El hotel está al lado del mercado, muy cerca de la estación.', 'L’hôtel est à côté du marché, tout près de la gare.', 'The hotel is next to the market, very near the station.'),
      ], [
        FB(CHOOSE, 'La farmacia ＿ al lado del banco.', ['está', 'hay', 'es'], 'está', ('Situer un lieu connu : está.', 'Locating a known place: está.'), ('La pharmacie est à côté de la banque.', 'The chemist’s is next to the bank.')),
        FB(CHOOSE, 'El hotel está cerca ＿ la plaza.', ['de', 'en', 'a'], 'de', ('Cerca de.', 'Cerca de.'), ('L’hôtel est près de la place.', 'The hotel is near the square.')),
        DC(ANSWER, [('Turista', 'Perdone, ¿dónde está la estación?')], ('Un touriste cherche la gare (elle est loin, à vingt minutes).', 'A tourist is looking for the station (it’s far, twenty minutes away).'), ['Está lejos, a veinte minutos.', 'Hay una estación.', 'Soy la estación.'], 'Está lejos, a veinte minutos.', ('Situer : está lejos.', 'Locate: está lejos.')),
        order(('Remets dans l’ordre : « La poste est en face du marché. »', 'Put in order: “The post office is opposite the market.”'), ['Correos', 'está', 'enfrente', 'del', 'mercado.'], ('Lieu + está + enfrente de (de + el = del).', 'Place + está + enfrente de (de + el = del).')),
      ]),
  ]),
  CH('delea1-w3-c2', ('Le chemin du moulin', 'The way to the mill'), [
    L('es-direcciones', ('Demander son chemin', 'Asking the way'), ('Comprendre et donner un itinéraire simple.', 'Understand and give simple directions.'), 8, [
        ('Pour demander poliment : Perdone, ¿para ir a…? (excusez-moi, pour aller à… ?).', 'To ask politely: Perdone, ¿para ir a…? (excuse me, how do I get to…?).'),
        ('Les indications : todo recto (tout droit), a la derecha (à droite), a la izquierda (à gauche), la primera / segunda calle (la première / deuxième rue), cruzar (traverser).', 'Directions: todo recto (straight on), a la derecha (on the right), a la izquierda (on the left), la primera / segunda calle (the first / second street), cruzar (to cross).'),
        ('Avec usted, les consignes sont à l’impératif poli : siga (continuez), gire (tournez), cruce (traversez).', 'With usted, instructions use the polite imperative: siga (go on), gire (turn), cruce (cross).'),
      ], [
        S('perdone', 'perdone', ('excusez-moi', 'excuse me')),
        S('todo-recto', 'todo recto', ('tout droit', 'straight on')),
        S('derecha', 'a la derecha', ('à droite', 'on the right')),
        S('izquierda', 'a la izquierda', ('à gauche', 'on the left')),
        S('primera', 'la primera calle', ('la première rue', 'the first street')),
        S('cruzar', 'cruzar', ('traverser', 'to cross')),
        S('molino', 'el molino', ('le moulin', 'the mill')),
        S('puente', 'el puente', ('le pont', 'the bridge')),
      ], [
        x('Perdone, ¿para ir al molino? — Siga todo recto y gire la segunda calle a la izquierda.', 'Excusez-moi, pour aller au moulin ? — Continuez tout droit et prenez la deuxième rue à gauche.', 'Excuse me, how do I get to the mill? — Go straight on and take the second street on the left.'),
        x('Cruce el puente y el molino está a la derecha.', 'Traversez le pont et le moulin est à droite.', 'Cross the bridge and the mill is on the right.'),
      ], [
        FB(COMPLETE, 'Gire a la ＿: el hotel está allí, a su derecha.', ['derecha', 'izquierda', 'recto'], 'derecha', ('À droite : a la derecha.', 'On the right: a la derecha.'), ('Tournez à droite : l’hôtel est là, sur votre droite.', 'Turn right: the hotel is there, on your right.')),
        FB(COMPLETE, '＿, ¿para ir a la estación?', ['Perdone', 'Adiós', 'Gracias'], 'Perdone', ('Pour interpeller poliment : perdone.', 'To politely get attention: perdone.'), ('Excusez-moi, pour aller à la gare ?', 'Excuse me, how do I get to the station?')),
        TF('Siga todo recto y cruce el puente.', ('Il faut tourner à gauche.', 'You must turn left.'), FAUX, ('Todo recto = tout droit.', 'Todo recto = straight on.')),
        DC(ANSWER, [('Don Quijote', '¿Dónde está el molino?')], ('Don Quichotte cherche le moulin (tout droit, puis à gauche).', 'Don Quixote is looking for the mill (straight on, then left).'), ['Todo recto y luego a la izquierda.', 'Tengo un molino.', 'Hay un molino.'], 'Todo recto y luego a la izquierda.', ('Indiquer le chemin : todo recto, a la izquierda.', 'Give directions: todo recto, a la izquierda.')),
      ]),
  ])])

# ═════════════════════════ 4 : à la venta — manger, querer, gustar, prix ═════════════════════════
W4 = WORLD('delea1-w4', ('À table, à la venta', 'At the table, at the venta'), REGION,
  ('La nourriture et les boissons, commander avec quiero et quisiera, dire ce qu’on aime avec me gusta, demander un prix.', 'Food and drink, ordering with quiero and quisiera, saying what you like with me gusta, asking a price.'),
  (('L’Ojáncanu affamé', 'The hungry Ojáncanu'), 'Ó', ('L’Ojáncanu, géant cantabre à un seul œil et à la barbe rousse, dévore les provisions de la venta. Commande pour lui un vrai repas espagnol et il repartira rassasié.', 'The Ojáncanu, a one-eyed Cantabrian giant with a red beard, devours the venta’s provisions. Order him a real Spanish meal and he will leave satisfied.')),
  [CH('delea1-w4-c1', ('Le menu du jour', 'The set menu'), [
    L('es-comida', ('Manger et boire', 'Eating and drinking'), ('Nommer les aliments et les boissons courants.', 'Name common foods and drinks.'), 8, [
        ('Les repas : el desayuno (petit-déjeuner), la comida (déjeuner, vers 14 h), la cena (dîner, vers 21 h). En Espagne, on mange tard !', 'Meals: el desayuno (breakfast), la comida (lunch, around 2 p.m.), la cena (dinner, around 9 p.m.). In Spain people eat late!'),
        ('Comer = manger, beber = boire. El menú del día = le menu du jour : primer plato, segundo plato, postre.', 'Comer = to eat, beber = to drink. El menú del día = the set menu: first course, second course, dessert.'),
        ('Les classiques : el pan, el agua, el vino, el queso, el jamón, la tortilla (omelette aux pommes de terre), la paella.', 'The classics: el pan, el agua, el vino, el queso, el jamón, la tortilla (potato omelette), la paella.'),
      ], [
        S('comer', 'comer', ('manger', 'to eat')),
        S('beber', 'beber', ('boire', 'to drink')),
        S('pan', 'el pan', ('le pain', 'the bread')),
        S('agua', 'el agua', ('l’eau', 'the water')),
        S('vino', 'el vino', ('le vin', 'the wine')),
        S('queso', 'el queso', ('le fromage', 'the cheese')),
        S('tortilla', 'la tortilla', ('l’omelette (aux pommes de terre)', 'the (potato) omelette')),
        S('postre', 'el postre', ('le dessert', 'the dessert')),
        S('cena', 'la cena', ('le dîner', 'dinner')),
      ], [
        x('Sancho come pan con queso y bebe vino.', 'Sancho mange du pain avec du fromage et boit du vin.', 'Sancho eats bread with cheese and drinks wine.'),
        x('En España la cena es a las nueve o a las diez.', 'En Espagne, le dîner est à neuf ou dix heures.', 'In Spain dinner is at nine or ten o’clock.'),
      ], [
        FB(COMPLETE, 'Tengo sed. Quiero ＿.', ['agua', 'pan', 'queso'], 'agua', ('Quand on a soif : agua.', 'When thirsty: agua.'), ('J’ai soif. Je veux de l’eau.', 'I’m thirsty. I want some water.')),
        FB(COMPLETE, 'De ＿ hay fruta o flan.', ['postre', 'cena', 'agua'], 'postre', ('Fruit ou flan : le dessert.', 'Fruit or flan: dessert.'), ('En dessert, il y a des fruits ou du flan.', 'For dessert there is fruit or flan.')),
        TF('La tortilla española lleva patatas y huevos.', ('La tortilla contient des pommes de terre et des œufs.', 'The tortilla contains potatoes and eggs.'), VRAI, ('Patatas y huevos = pommes de terre et œufs.', 'Patatas y huevos = potatoes and eggs.')),
        order(('Remets dans l’ordre : « Sancho boit de l’eau. »', 'Put in order: “Sancho drinks water.”'), ['Sancho', 'bebe', 'agua.'], ('Sujet + verbe + complément.', 'Subject + verb + object.')),
      ]),
    L('es-pedir', ('Commander : quiero, quisiera, ¿me pone…?', 'Ordering: quiero, quisiera, ¿me pone…?'), ('Commander au restaurant et demander l’addition.', 'Order at a restaurant and ask for the bill.'), 8, [
        ('Querer (vouloir) : quiero, quieres, quiere… Quisiera = je voudrais, plus poli. Au bar, on entend aussi ¿Me pone un café? (vous me servez un café ?).', 'Querer (to want): quiero, quieres, quiere… Quisiera = I would like, more polite. At the bar you also hear ¿Me pone un café? (could I have a coffee?).'),
        ('Le serveur demande : ¿Qué van a tomar? (qu’allez-vous prendre ?) ; ¿Algo más? (autre chose ?).', 'The waiter asks: ¿Qué van a tomar? (what will you have?); ¿Algo más? (anything else?).'),
        ('Pour finir : La cuenta, por favor (l’addition, s’il vous plaît). Por favor = s’il vous plaît.', 'To finish: La cuenta, por favor (the bill, please). Por favor = please.'),
      ], [
        SG('querer', 'quiero / quisiera', ('je veux / je voudrais', 'I want / I would like')),
        S('por-favor', 'por favor', ('s’il vous plaît', 'please')),
        S('la-cuenta', 'la cuenta', ('l’addition', 'the bill')),
        S('camarero', 'el camarero / la camarera', ('le serveur / la serveuse', 'the waiter / the waitress')),
        S('tomar', 'tomar', ('prendre (boisson, plat)', 'to have (food, drink)')),
        S('algo-mas', '¿Algo más?', ('Autre chose ?', 'Anything else?')),
        S('cafe-con-leche', 'un café con leche', ('un café au lait', 'a white coffee')),
        S('menu-del-dia', 'el menú del día', ('le menu du jour', 'the set menu')),
      ], [
        x('Camarero, quisiera el menú del día, por favor.', 'Garçon, je voudrais le menu du jour, s’il vous plaît.', 'Waiter, I would like the set menu, please.'),
        x('¿Algo más? — No, gracias. La cuenta, por favor.', 'Autre chose ? — Non, merci. L’addition, s’il vous plaît.', 'Anything else? — No, thanks. The bill, please.'),
      ], [
        DC(ANSWER, [('Camarero', '¿Qué va a tomar?')], ('Le serveur te demande ce que tu prends.', 'The waiter asks you what you’ll have.'), ['Un café con leche, por favor.', 'Me llamo café.', 'La cuenta es mía.'], 'Un café con leche, por favor.', ('On commande avec por favor.', 'Order with por favor.')),
        FB(CHOOSE, 'Yo ＿ una tortilla, por favor.', ['quiero', 'quiere', 'quieres'], 'quiero', ('Avec yo : quiero.', 'With yo: quiero.'), ('Je veux une tortilla, s’il vous plaît.', 'I want a tortilla, please.')),
        FB(COMPLETE, 'Hemos terminado. La ＿, por favor.', ['cuenta', 'carta', 'cena'], 'cuenta', ('L’addition : la cuenta.', 'The bill: la cuenta.'), ('Nous avons fini. L’addition, s’il vous plaît.', 'We have finished. The bill, please.')),
        TF('«Quisiera» es más educado que «quiero».', ('Quisiera est plus poli que quiero.', 'Quisiera is more polite than quiero.'), VRAI, ('Quisiera = je voudrais.', 'Quisiera = I would like.')),
      ]),
  ]),
  CH('delea1-w4-c2', ('Goûts et prix', 'Tastes and prices'), [
    L('es-gustar', ('J’aime le jambon : me gusta', 'I like ham: me gusta'), ('Dire ce qu’on aime ou non et demander un prix.', 'Say what you like or dislike and ask a price.'), 9, [
        ('Gustar fonctionne à l’envers : la chose plaît à la personne. Me gusta el queso (le fromage me plaît), me gustan las aceitunas (au pluriel : gustan).', 'Gustar works the other way round: the thing pleases the person. Me gusta el queso (I like cheese), me gustan las aceitunas (plural: gustan).'),
        ('Me / te / le gusta : à moi / toi / lui. No me gusta = je n’aime pas. Me encanta = j’adore.', 'Me / te / le gusta: to me / you / him-her. No me gusta = I don’t like. Me encanta = I love.'),
        ('Les prix : ¿Cuánto cuesta? (combien ça coûte ?), ¿Cuánto es? (combien je vous dois ?). Un euro, diez euros, caro (cher), barato (bon marché).', 'Prices: ¿Cuánto cuesta? (how much does it cost?), ¿Cuánto es? (how much is it?). Un euro, diez euros, caro (expensive), barato (cheap).'),
      ], [
        SG('gustar', 'me gusta / me gustan', ('j’aime (une chose / des choses)', 'I like (one thing / several things)')),
        S('me-encanta', 'me encanta', ('j’adore', 'I love (it)')),
        S('jamon', 'el jamón', ('le jambon', 'the ham')),
        S('aceitunas', 'las aceitunas', ('les olives', 'the olives')),
        S('cuanto-cuesta', '¿Cuánto cuesta?', ('Combien ça coûte ?', 'How much does it cost?')),
        S('euro', 'el euro', ('l’euro', 'the euro')),
        S('caro', 'caro / barato', ('cher / bon marché', 'expensive / cheap')),
        S('naranja', 'la naranja', ('l’orange', 'the orange')),
      ], [
        x('Me gusta mucho el jamón, pero no me gustan las aceitunas.', 'J’aime beaucoup le jambon, mais je n’aime pas les olives.', 'I really like ham, but I don’t like olives.'),
        x('¿Cuánto cuesta el queso? — Doce euros el kilo. — ¡Qué caro!', 'Combien coûte le fromage ? — Douze euros le kilo. — Que c’est cher !', 'How much is the cheese? — Twelve euros a kilo. — How expensive!'),
      ], [
        FB(CHOOSE, 'Me ＿ las naranjas.', ['gustan', 'gusta', 'gusto'], 'gustan', ('Las naranjas est pluriel : gustan.', 'Las naranjas is plural: gustan.'), ('J’aime les oranges.', 'I like oranges.')),
        FB(CHOOSE, 'No me ＿ el vino.', ['gusta', 'gustan', 'gustas'], 'gusta', ('El vino est singulier : gusta.', 'El vino is singular: gusta.'), ('Je n’aime pas le vin.', 'I don’t like wine.')),
        DC(ANSWER, [('Vendedora', 'El jamón cuesta veinte euros.')], ('La vendeuse annonce le prix du jambon (tu trouves ça cher).', 'The shopkeeper gives the price of the ham (you find it expensive).'), ['¡Qué caro!', '¡Qué barato! Me gusta.', 'Tengo veinte años.'], '¡Qué caro!', ('Vingt euros, c’est cher : ¡qué caro!', 'Twenty euros is expensive: ¡qué caro!')),
        TF('Me encanta el queso.', ('La personne déteste le fromage.', 'The person hates cheese.'), FAUX, ('Me encanta = j’adore.', 'Me encanta = I love it.')),
      ]),
  ])])

# ═════════════════════════ 5 : une journée — présent des verbes réguliers, heure, routine ═════════════════════════
W5 = WORLD('delea1-w5', ('Une journée de chevalier', 'A knight’s day'), REGION,
  ('Le présent des verbes réguliers en -ar, -er, -ir, dire l’heure, les jours de la semaine et la routine avec les verbes pronominaux.', 'The present of regular -ar, -er, -ir verbs, telling the time, days of the week and the daily routine with reflexive verbs.'),
  (('Le Busgosu des forêts', 'The forest Busgosu'), 'Ü', ('Le Busgosu, gardien des bois mi-homme mi-bouc, égare les voyageurs qui ne savent plus quel jour ni quelle heure il est. Raconte-lui ta journée pour qu’il t’ouvre le sentier.', 'The Busgosu, a half-man half-goat guardian of the woods, leads astray travellers who no longer know the day or the time. Tell it about your day so it opens the path for you.')),
  [CH('delea1-w5-c1', ('Du lever au coucher', 'From getting up to bedtime'), [
    L('es-presente', ('Le présent : hablar, comer, vivir', 'The present: hablar, comer, vivir'), ('Conjuguer les verbes réguliers au présent.', 'Conjugate regular verbs in the present.'), 9, [
        ('Verbes en -ar (hablar) : hablo, hablas, habla, hablamos, habláis, hablan.', '-ar verbs (hablar): hablo, hablas, habla, hablamos, habláis, hablan.'),
        ('Verbes en -er (comer) : como, comes, come, comemos, coméis, comen. Verbes en -ir (vivir) : vivo, vives, vive, vivimos, vivís, viven.', '-er verbs (comer): como, comes, come, comemos, coméis, comen. -ir verbs (vivir): vivo, vives, vive, vivimos, vivís, viven.'),
        ('La terminaison suffit à savoir qui parle : Hablo español = je parle espagnol. Ustedes (vous, pluriel poli) se conjugue comme ellos : ustedes hablan.', 'The ending tells you who is speaking: Hablo español = I speak Spanish. Ustedes (polite plural you) is conjugated like ellos: ustedes hablan.'),
      ], [
        SG('presente-ar', 'hablo / hablas / habla', ('présent des verbes en -ar', 'present of -ar verbs')),
        SG('presente-er-ir', 'como / vivo', ('présent des verbes en -er, -ir', 'present of -er, -ir verbs')),
        S('hablar', 'hablar', ('parler', 'to speak')),
        S('vivir', 'vivir', ('vivre, habiter', 'to live')),
        S('trabajar', 'trabajar', ('travailler', 'to work')),
        S('estudiar', 'estudiar', ('étudier', 'to study')),
        S('leer', 'leer', ('lire', 'to read')),
        S('escribir', 'escribir', ('écrire', 'to write')),
        S('escuchar', 'escuchar', ('écouter', 'to listen (to)')),
      ], [
        x('Don Quijote lee libros de caballerías todo el día.', 'Don Quichotte lit des romans de chevalerie toute la journée.', 'Don Quixote reads books of chivalry all day long.'),
        x('Vivimos en un pueblo de La Mancha y trabajamos en el campo.', 'Nous vivons dans un village de la Manche et nous travaillons aux champs.', 'We live in a village in La Mancha and we work in the fields.'),
      ], [
        FB(CHOOSE, 'Yo ＿ español y francés.', ['hablo', 'habla', 'hablas'], 'hablo', ('Avec yo : -o.', 'With yo: -o.'), ('Je parle espagnol et français.', 'I speak Spanish and French.')),
        FB(CHOOSE, '¿Dónde ＿ tú? — En Toledo.', ['vives', 'vivo', 'viven'], 'vives', ('Avec tú : -es.', 'With tú: -es.'), ('Où habites-tu ? — À Tolède.', 'Where do you live? — In Toledo.')),
        FB(CHOOSE, 'Mis padres ＿ en una tienda.', ['trabajan', 'trabaja', 'trabajamos'], 'trabajan', ('Avec ellos : -an.', 'With ellos: -an.'), ('Mes parents travaillent dans un magasin.', 'My parents work in a shop.')),
        order(('Remets dans l’ordre : « Nous lisons un livre. »', 'Put in order: “We are reading a book.”'), ['Leemos', 'un', 'libro.'], ('Leer avec nosotros : leemos.', 'Leer with nosotros: leemos.')),
      ]),
    L('es-hora', ('Quelle heure est-il ? ¿Qué hora es?', 'What time is it? ¿Qué hora es?'), ('Dire l’heure et parler des jours de la semaine.', 'Tell the time and talk about the days of the week.'), 8, [
        ('¿Qué hora es? — Es la una (une heure), son las dos, son las tres y media (trois heures et demie), son las cuatro y cuarto, son las cinco menos cuarto.', '¿Qué hora es? — Es la una (one o’clock), son las dos, son las tres y media (half past three), son las cuatro y cuarto, son las cinco menos cuarto (quarter to five).'),
        ('Pour un rendez-vous : ¿A qué hora…? — A las ocho. De la mañana / de la tarde / de la noche précise le moment.', 'For an appointment: ¿A qué hora…? — A las ocho. De la mañana / de la tarde / de la noche says when.'),
        ('Les jours (sans majuscule) : lunes, martes, miércoles, jueves, viernes, sábado, domingo. El lunes = lundi (ce lundi) ; los lunes = le lundi (chaque lundi).', 'Days (no capital): lunes, martes, miércoles, jueves, viernes, sábado, domingo. El lunes = on Monday; los lunes = on Mondays.'),
      ], [
        S('que-hora-es', '¿Qué hora es?', ('Quelle heure est-il ?', 'What time is it?')),
        S('son-las', 'son las… / es la una', ('il est… heures / il est une heure', 'it is… o’clock / it is one o’clock')),
        S('y-media', 'y media', ('et demie', 'half past')),
        S('a-que-hora', '¿A qué hora…?', ('À quelle heure… ?', 'At what time…?')),
        S('lunes', 'el lunes', ('lundi', 'Monday')),
        S('viernes', 'el viernes', ('vendredi', 'Friday')),
        S('domingo', 'el domingo', ('dimanche', 'Sunday')),
        S('fin-de-semana', 'el fin de semana', ('le week-end', 'the weekend')),
      ], [
        x('¿Qué hora es? — Son las once y media.', 'Quelle heure est-il ? — Il est onze heures et demie.', 'What time is it? — It is half past eleven.'),
        x('Los domingos comemos a las tres con mis abuelos.', 'Le dimanche, nous déjeunons à trois heures avec mes grands-parents.', 'On Sundays we have lunch at three with my grandparents.'),
      ], [
        FB(CHOOSE, '¿Qué hora es? — ＿ la una.', ['Es', 'Son', 'Está'], 'Es', ('Une heure : es la una.', 'One o’clock: es la una.'), ('Quelle heure est-il ? — Il est une heure.', 'What time is it? — It is one o’clock.')),
        FB(CHOOSE, 'Son las cuatro y ＿: las 4:30.', ['media', 'cuarto', 'menos'], 'media', ('4 h 30 : y media.', '4:30: y media.'), ('Il est quatre heures et demie.', 'It is half past four.')),
        DC(ANSWER, [('Sancho', '¿A qué hora es la cena?')], ('Sancho demande à quelle heure est le dîner (à neuf heures).', 'Sancho asks what time dinner is (at nine).'), ['A las nueve.', 'Son nueve.', 'El nueve.'], 'A las nueve.', ('À quelle heure ? — A las + heure.', 'At what time? — A las + hour.')),
        TF('El sábado y el domingo son el fin de semana.', ('Samedi et dimanche forment le week-end.', 'Saturday and Sunday are the weekend.'), VRAI, ('Fin de semana = week-end.', 'Fin de semana = weekend.')),
      ]),
  ]),
  CH('delea1-w5-c2', ('La routine du chevalier', 'The knight’s routine'), [
    L('es-rutina', ('Je me lève : levantarse', 'I get up: levantarse'), ('Raconter sa routine avec les verbes pronominaux.', 'Describe your routine with reflexive verbs.'), 9, [
        ('Verbes pronominaux : le pronom change avec la personne. Levantarse : me levanto, te levantas, se levanta, nos levantamos, os levantáis, se levantan.', 'Reflexive verbs: the pronoun changes with the person. Levantarse: me levanto, te levantas, se levanta, nos levantamos, os levantáis, se levantan.'),
        ('Certains verbes changent de voyelle : acostarse → me acuesto (je me couche), despertarse → me despierto (je me réveille).', 'Some verbs change their vowel: acostarse → me acuesto (I go to bed), despertarse → me despierto (I wake up).'),
        ('Pour l’ordre : primero (d’abord), luego / después (ensuite), por la mañana (le matin), por la noche (le soir).', 'For order: primero (first), luego / después (then), por la mañana (in the morning), por la noche (in the evening).'),
      ], [
        SG('reflexivos', 'me levanto / te levantas / se levanta', ('verbes pronominaux (levantarse)', 'reflexive verbs (levantarse)')),
        S('levantarse', 'levantarse', ('se lever', 'to get up')),
        S('acostarse', 'acostarse', ('se coucher', 'to go to bed')),
        S('ducharse', 'ducharse', ('se doucher', 'to have a shower')),
        S('desayunar', 'desayunar', ('prendre le petit-déjeuner', 'to have breakfast')),
        S('despues', 'después', ('après, ensuite', 'after, afterwards')),
        S('por-la-manana', 'por la mañana', ('le matin', 'in the morning')),
        S('siempre', 'siempre', ('toujours', 'always')),
      ], [
        x('Don Quijote se levanta a las seis y se pone la armadura.', 'Don Quichotte se lève à six heures et met son armure.', 'Don Quixote gets up at six and puts on his armour.'),
        x('Primero me ducho, después desayuno y luego trabajo.', 'D’abord je me douche, ensuite je prends mon petit-déjeuner, puis je travaille.', 'First I shower, then I have breakfast and then I work.'),
      ], [
        FB(CHOOSE, 'Yo ＿ levanto a las siete.', ['me', 'te', 'se'], 'me', ('Avec yo : me.', 'With yo: me.'), ('Je me lève à sept heures.', 'I get up at seven.')),
        FB(CHOOSE, 'Sancho ＿ acuesta muy tarde.', ['se', 'me', 'nos'], 'se', ('Avec él : se.', 'With él: se.'), ('Sancho se couche très tard.', 'Sancho goes to bed very late.')),
        DC(ANSWER, [('Teresa', '¿A qué hora te levantas?')], ('Teresa te demande à quelle heure tu te lèves.', 'Teresa asks what time you get up.'), ['Me levanto a las siete.', 'Te levantas a las siete.', 'Se levanta el lunes.'], 'Me levanto a las siete.', ('Je me lève : me levanto.', 'I get up: me levanto.')),
        order(('Remets dans l’ordre : « D’abord je me douche. »', 'Put in order: “First I have a shower.”'), ['Primero', 'me', 'ducho.'], ('Primero + me ducho.', 'Primero + me ducho.')),
      ]),
  ])])

# ═════════════════════════ 6 : le marché — vêtements, couleurs, accord, démonstratifs ═════════════════════════
W6 = WORLD('delea1-w6', ('Le marché de Toboso', 'The Toboso market'), REGION,
  ('Les vêtements et les couleurs, l’accord des adjectifs, este / ese pour montrer, faire des achats.', 'Clothes and colours, adjective agreement, este / ese for pointing, shopping.'),
  (('Le Cuélebre du trésor', 'The treasure Cuélebre'), 'Ú', ('Le Cuélebre, serpent ailé des Asturies, garde le trésor caché sous la place du marché et souffle sur les étals. Achète ce qu’il te faut sans te tromper et il retournera dormir sur son or.', 'The Cuélebre, a winged serpent from Asturias, guards the treasure hidden under the market square and blows on the stalls. Buy what you need without mistakes and it will go back to sleep on its gold.')),
  [CH('delea1-w6-c1', ('Un habit pour Dulcinée', 'An outfit for Dulcinea'), [
    L('es-ropa', ('Les vêtements et les couleurs', 'Clothes and colours'), ('Nommer les vêtements et accorder les couleurs.', 'Name clothes and make colours agree.'), 8, [
        ('Llevar = porter (un vêtement) : Llevo una camisa blanca (je porte une chemise blanche).', 'Llevar = to wear: Llevo una camisa blanca (I’m wearing a white shirt).'),
        ('Les adjectifs s’accordent et se placent après le nom : un sombrero negro, una falda negra, unos zapatos negros.', 'Adjectives agree and come after the noun: un sombrero negro, una falda negra, unos zapatos negros.'),
        ('Les adjectifs en -e ou en consonne ne changent qu’au pluriel : verde → verdes, azul → azules, gris → grises.', 'Adjectives ending in -e or a consonant only change in the plural: verde → verdes, azul → azules, gris → grises.'),
      ], [
        SG('concordancia', 'negro / negra / negros', ('accord des adjectifs (genre et nombre)', 'adjective agreement (gender and number)')),
        S('llevar', 'llevar', ('porter (un vêtement) ; emporter', 'to wear; to carry')),
        S('camisa', 'la camisa', ('la chemise', 'the shirt')),
        S('falda', 'la falda', ('la jupe', 'the skirt')),
        S('zapatos', 'los zapatos', ('les chaussures', 'the shoes')),
        S('sombrero', 'el sombrero', ('le chapeau', 'the hat')),
        S('rojo', 'rojo / roja', ('rouge', 'red')),
        S('blanco', 'blanco / blanca', ('blanc', 'white')),
        S('azul', 'azul', ('bleu', 'blue')),
        S('verde', 'verde', ('vert', 'green')),
      ], [
        x('Dulcinea lleva una falda roja y unos zapatos blancos.', 'Dulcinée porte une jupe rouge et des chaussures blanches.', 'Dulcinea is wearing a red skirt and white shoes.'),
        x('El sombrero de Sancho es verde y viejo.', 'Le chapeau de Sancho est vert et vieux.', 'Sancho’s hat is green and old.'),
      ], [
        FB(CHOOSE, 'Llevo una camisa ＿.', ['blanca', 'blanco', 'blancos'], 'blanca', ('Camisa est féminin singulier : blanca.', 'Camisa is feminine singular: blanca.'), ('Je porte une chemise blanche.', 'I’m wearing a white shirt.')),
        FB(CHOOSE, 'Me gustan los zapatos ＿.', ['rojos', 'roja', 'rojo'], 'rojos', ('Zapatos est masculin pluriel : rojos.', 'Zapatos is masculine plural: rojos.'), ('J’aime les chaussures rouges.', 'I like the red shoes.')),
        FB(CHOOSE, 'Tiene dos faldas ＿.', ['azules', 'azul', 'azulas'], 'azules', ('Azul au pluriel : azules.', 'Azul in the plural: azules.'), ('Elle a deux jupes bleues.', 'She has two blue skirts.')),
        TF('Lleva un sombrero negro.', ('La personne porte un chapeau blanc.', 'The person is wearing a white hat.'), FAUX, ('Negro = noir.', 'Negro = black.')),
      ]),
    L('es-comprar', ('Acheter : este, ese, ¿tiene…?', 'Buying: este, ese, ¿tiene…?'), ('Montrer un objet, demander une taille et payer.', 'Point at an item, ask for a size and pay.'), 8, [
        ('Démonstratifs : este / esta (ce… -ci, tout près), ese / esa (ce… -là, un peu plus loin). Pluriel : estos, estas, esos, esas.', 'Demonstratives: este / esta (this, very close), ese / esa (that, a little further). Plural: estos, estas, esos, esas.'),
        ('Au magasin : ¿Tiene esta camisa en azul? (vous avez cette chemise en bleu ?), ¿Qué talla tiene? (quelle taille faites-vous ?), ¿Puedo probármela? (je peux l’essayer ?).', 'In the shop: ¿Tiene esta camisa en azul? (do you have this shirt in blue?), ¿Qué talla tiene? (what size are you?), ¿Puedo probármela? (can I try it on?).'),
        ('Payer : en efectivo (en espèces) ou con tarjeta (par carte). Grande / pequeño = grand / petit.', 'Paying: en efectivo (in cash) or con tarjeta (by card). Grande / pequeño = big / small.'),
      ], [
        SG('demostrativos', 'este / ese', ('ce… -ci / ce… -là (démonstratifs)', 'this / that (demonstratives)')),
        S('tienda', 'la tienda', ('le magasin', 'the shop')),
        S('talla', 'la talla', ('la taille (vêtement)', 'the size (clothes)')),
        S('probar', 'probarse', ('essayer (un vêtement)', 'to try on')),
        S('grande', 'grande', ('grand, gros', 'big, large')),
        S('pequeno', 'pequeño / pequeña', ('petit', 'small')),
        S('tarjeta', 'con tarjeta', ('par carte', 'by card')),
        S('efectivo', 'en efectivo', ('en espèces', 'in cash')),
      ], [
        x('¿Tiene este sombrero en una talla más grande?', 'Vous avez ce chapeau dans une taille plus grande ?', 'Do you have this hat in a bigger size?'),
        x('Esa camisa es muy bonita. ¿Puedo pagar con tarjeta?', 'Cette chemise-là est très jolie. Je peux payer par carte ?', 'That shirt is very nice. Can I pay by card?'),
      ], [
        FB(CHOOSE, '＿ falda (aquí, en mi mano) es muy bonita.', ['Esta', 'Este', 'Estos'], 'Esta', ('Falda est féminin, tout près : esta.', 'Falda is feminine, very close: esta.'), ('Cette jupe (ici, dans ma main) est très jolie.', 'This skirt (here, in my hand) is very nice.')),
        FB(CHOOSE, '¿Cuánto cuestan ＿ zapatos (allí)?', ['esos', 'esas', 'ese'], 'esos', ('Zapatos est masculin pluriel, un peu loin : esos.', 'Zapatos is masculine plural, a bit further: esos.'), ('Combien coûtent ces chaussures-là ?', 'How much are those shoes?')),
        DC(ANSWER, [('Vendedor', '¿Cómo va a pagar?')], ('Le vendeur demande comment tu vas payer.', 'The seller asks how you will pay.'), ['Con tarjeta, por favor.', 'En una talla grande.', 'Me gusta el azul.'], 'Con tarjeta, por favor.', ('Payer : con tarjeta / en efectivo.', 'Paying: con tarjeta / en efectivo.')),
        TF('Este vestido es pequeño para mí.', ('La robe est trop grande.', 'The dress is too big.'), FAUX, ('Pequeño = petit.', 'Pequeño = small.')),
      ]),
  ])])

# ═════════════════════════ 7 : les saisons — météo, mois, ir a + infinitif ═════════════════════════
W7 = WORLD('delea1-w7', ('La sierra en toutes saisons', 'The sierra in every season'), REGION,
  ('Parler du temps qu’il fait, des mois et des saisons, et de ses projets avec ir a + infinitif.', 'Talk about the weather, months and seasons, and your plans with ir a + infinitive.'),
  (('Le Basajaun de la montagne', 'The mountain Basajaun'), '¿', ('Le Basajaun, géant velu des forêts basques, protège les troupeaux et sent venir l’orage. Il ne laisse passer la sierra qu’à ceux qui savent dire le temps qu’il fait et ce qu’ils vont faire.', 'The Basajaun, a hairy giant of the Basque forests, protects the flocks and senses storms coming. It only lets those who can say what the weather is like and what they are going to do cross the sierra.')),
  [CH('delea1-w7-c1', ('Pluie et soleil', 'Rain and sun'), [
    L('es-tiempo', ('Quel temps fait-il ? hace calor, llueve', 'What’s the weather like? hace calor, llueve'), ('Décrire la météo avec hace, hay et está.', 'Describe the weather with hace, hay and está.'), 8, [
        ('¿Qué tiempo hace? — Hace sol (il fait soleil), hace calor (il fait chaud), hace frío (il fait froid), hace viento (il y a du vent), hace buen / mal tiempo.', '¿Qué tiempo hace? — Hace sol (it’s sunny), hace calor (it’s hot), hace frío (it’s cold), hace viento (it’s windy), hace buen / mal tiempo (the weather is good / bad).'),
        ('Llueve (il pleut), nieva (il neige) ; está nublado (c’est nuageux) ; hay niebla (il y a du brouillard).', 'Llueve (it’s raining), nieva (it’s snowing); está nublado (it’s cloudy); hay niebla (it’s foggy).'),
        ('Pour nuancer : mucho / un poco : hace mucho calor, hace un poco de frío.', 'To qualify: mucho / un poco: hace mucho calor, hace un poco de frío.'),
      ], [
        S('que-tiempo', '¿Qué tiempo hace?', ('Quel temps fait-il ?', 'What’s the weather like?')),
        S('hace-calor', 'hace calor', ('il fait chaud', 'it’s hot')),
        S('hace-frio', 'hace frío', ('il fait froid', 'it’s cold')),
        S('hace-sol', 'hace sol', ('il fait soleil', 'it’s sunny')),
        S('llueve', 'llueve', ('il pleut', 'it’s raining')),
        S('nieva', 'nieva', ('il neige', 'it’s snowing')),
        S('viento', 'el viento', ('le vent', 'the wind')),
        S('nublado', 'está nublado', ('le ciel est nuageux', 'it’s cloudy')),
      ], [
        x('En agosto hace mucho calor en La Mancha.', 'En août, il fait très chaud dans la Manche.', 'In August it is very hot in La Mancha.'),
        x('Hoy hace viento y está nublado: va a llover.', 'Aujourd’hui il y a du vent et c’est nuageux : il va pleuvoir.', 'Today it’s windy and cloudy: it’s going to rain.'),
      ], [
        FB(CHOOSE, 'En invierno ＿ mucho frío.', ['hace', 'está', 'hay'], 'hace', ('Froid, chaud, soleil : hace.', 'Cold, hot, sun: hace.'), ('En hiver, il fait très froid.', 'In winter it is very cold.')),
        FB(COMPLETE, 'Coge el paraguas: ＿.', ['llueve', 'hace sol', 'hace calor'], 'llueve', ('Le parapluie, c’est pour la pluie : llueve.', 'An umbrella is for rain: llueve.'), ('Prends le parapluie : il pleut.', 'Take the umbrella: it’s raining.')),
        DC(ANSWER, [('Sancho', '¿Qué tiempo hace hoy?')], ('Sancho demande le temps qu’il fait (beau et chaud).', 'Sancho asks what the weather is like (nice and hot).'), ['Hace sol y calor.', 'Es sol y calor.', 'Tengo sol.'], 'Hace sol y calor.', ('Météo : hace sol, hace calor.', 'Weather: hace sol, hace calor.')),
        TF('Nieva en la sierra.', ('Il neige sur la sierra.', 'It is snowing in the sierra.'), VRAI, ('Nieva = il neige.', 'Nieva = it’s snowing.')),
      ]),
    L('es-meses', ('Les mois et les saisons', 'Months and seasons'), ('Dire une date et parler des saisons.', 'Give a date and talk about the seasons.'), 8, [
        ('Les mois (sans majuscule) : enero, febrero, marzo, abril, mayo, junio, julio, agosto, septiembre, octubre, noviembre, diciembre.', 'Months (no capital): enero, febrero, marzo, abril, mayo, junio, julio, agosto, septiembre, octubre, noviembre, diciembre.'),
        ('La date : Hoy es el 3 de mayo (aujourd’hui, c’est le 3 mai). ¿Cuándo es tu cumpleaños? — Es el 12 de octubre.', 'The date: Hoy es el 3 de mayo (today is 3 May). ¿Cuándo es tu cumpleaños? — Es el 12 de octubre.'),
        ('Les saisons : la primavera, el verano, el otoño, el invierno. En verano = en été.', 'The seasons: la primavera, el verano, el otoño, el invierno. En verano = in summer.'),
      ], [
        S('enero', 'enero', ('janvier', 'January')),
        S('mayo', 'mayo', ('mai', 'May')),
        S('agosto', 'agosto', ('août', 'August')),
        S('diciembre', 'diciembre', ('décembre', 'December')),
        S('primavera', 'la primavera', ('le printemps', 'spring')),
        S('verano', 'el verano', ('été', 'summer')),
        S('invierno', 'el invierno', ('hiver', 'winter')),
        S('cumpleanos', 'el cumpleaños', ('l’anniversaire', 'the birthday')),
      ], [
        x('Mi cumpleaños es el veinte de abril, en primavera.', 'Mon anniversaire est le vingt avril, au printemps.', 'My birthday is on the twentieth of April, in spring.'),
        x('En invierno nieva en la sierra y en verano hace calor.', 'En hiver, il neige sur la sierra et en été il fait chaud.', 'In winter it snows in the sierra and in summer it’s hot.'),
      ], [
        FB(COMPLETE, 'Después de abril viene ＿.', ['mayo', 'marzo', 'junio'], 'mayo', ('Avril, puis mai.', 'April, then May.'), ('Après avril vient mai.', 'After April comes May.')),
        FB(COMPLETE, 'En España, julio y agosto son meses de ＿.', ['verano', 'invierno', 'otoño'], 'verano', ('Juillet et août : l’été.', 'July and August: summer.'), ('En Espagne, juillet et août sont des mois d’été.', 'In Spain, July and August are summer months.')),
        DC(ANSWER, [('Teresa', '¿Cuándo es tu cumpleaños?')], ('Teresa te demande la date de ton anniversaire.', 'Teresa asks when your birthday is.'), ['Es el doce de octubre.', 'Tengo doce años.', 'Son las doce.'], 'Es el doce de octubre.', ('Une date : es el + jour + de + mois.', 'A date: es el + day + de + month.')),
        TF('Diciembre es un mes de invierno en España.', ('Décembre est en hiver en Espagne.', 'December is in winter in Spain.'), VRAI, ('Diciembre = décembre.', 'Diciembre = December.')),
      ]),
  ]),
  CH('delea1-w7-c2', ('Projets de voyage', 'Travel plans'), [
    L('es-ir-a', ('Je vais partir : ir a + infinitif', 'I’m going to leave: ir a + infinitive'), ('Parler de ses projets proches.', 'Talk about your near plans.'), 9, [
        ('Ir (aller) : voy, vas, va, vamos, vais, van. Voy a Sevilla = je vais à Séville.', 'Ir (to go): voy, vas, va, vamos, vais, van. Voy a Sevilla = I’m going to Seville.'),
        ('Futur proche : ir a + infinitif. Voy a viajar (je vais voyager), vamos a comer (nous allons manger).', 'Near future: ir a + infinitive. Voy a viajar (I’m going to travel), vamos a comer (we’re going to eat).'),
        ('Les repères : hoy (aujourd’hui), mañana (demain), esta tarde (cet après-midi), la semana que viene (la semaine prochaine), en tren / en coche / a pie.', 'Time markers: hoy (today), mañana (tomorrow), esta tarde (this afternoon), la semana que viene (next week), en tren / en coche / a pie (by train / by car / on foot).'),
      ], [
        SG('ir-a', 'voy a + infinitivo', ('je vais + infinitif (futur proche)', 'I’m going to + verb (near future)')),
        S('ir', 'ir', ('aller', 'to go')),
        S('viajar', 'viajar', ('voyager', 'to travel')),
        S('hoy', 'hoy', ('aujourd’hui', 'today')),
        S('manana', 'mañana', ('demain', 'tomorrow')),
        S('semana-que-viene', 'la semana que viene', ('la semaine prochaine', 'next week')),
        S('en-tren', 'en tren', ('en train', 'by train')),
        S('vacaciones', 'las vacaciones', ('les vacances', 'the holidays')),
      ], [
        x('Mañana vamos a salir muy temprano hacia la sierra.', 'Demain, nous allons partir très tôt vers la sierra.', 'Tomorrow we are going to leave very early for the sierra.'),
        x('En vacaciones voy a viajar a Barcelona en tren.', 'Pendant les vacances, je vais voyager à Barcelone en train.', 'During the holidays I’m going to travel to Barcelona by train.'),
      ], [
        FB(CHOOSE, 'Esta tarde ＿ a visitar el castillo.', ['voy', 'va', 'van'], 'voy', ('Avec yo : voy a.', 'With yo: voy a.'), ('Cet après-midi, je vais visiter le château.', 'This afternoon I’m going to visit the castle.')),
        FB(CHOOSE, 'Mañana vamos ＿ comer paella.', ['a', 'de', 'en'], 'a', ('Ir a + infinitif.', 'Ir a + infinitive.'), ('Demain, nous allons manger une paella.', 'Tomorrow we are going to eat paella.')),
        DC(ANSWER, [('Don Quijote', '¿Qué vas a hacer el fin de semana?')], ('Don Quichotte te demande tes projets du week-end.', 'Don Quixote asks about your weekend plans.'), ['Voy a visitar a mis abuelos.', 'Visito a mis abuelos ayer.', 'Soy mis abuelos.'], 'Voy a visitar a mis abuelos.', ('Projet : voy a + infinitif.', 'Plan: voy a + infinitive.')),
        order(('Remets dans l’ordre : « Nous allons voyager en train. »', 'Put in order: “We are going to travel by train.”'), ['Vamos', 'a', 'viajar', 'en', 'tren.'], ('Vamos a + infinitif + en tren.', 'Vamos a + infinitive + en tren.')),
      ]),
  ])])

# ═════════════════════════ 8 : les moulins — décrire, ser / estar, le corps, la santé ═════════════════════════
W8 = WORLD('delea1-w8', ('Les géants de la plaine', 'The giants of the plain'), REGION,
  ('Décrire une personne avec ser et estar, parler du corps et de la santé (me duele, tener que).', 'Describe a person with ser and estar, talk about the body and health (me duele, tener que).'),
  (('Le Coco des moulins', 'The windmill Coco'), '¡', ('Le Coco, croque-mitaine des berceuses espagnoles, s’est caché dans les moulins et les fait tourner comme des bras de géant. Décris-le sans trembler et il redeviendra une ombre.', 'The Coco, the bogeyman of Spanish lullabies, has hidden in the windmills and spins them like giants’ arms. Describe it without trembling and it will turn back into a shadow.')),
  [CH('delea1-w8-c1', ('Portraits', 'Portraits'), [
    L('es-describir', ('Il est grand : ser + adjectif', 'He is tall: ser + adjective'), ('Décrire l’apparence et le caractère de quelqu’un.', 'Describe someone’s appearance and personality.'), 9, [
        ('Ser décrit ce qu’on est de façon durable : Don Quijote es alto y delgado (grand et mince), Sancho es bajo y gordo (petit et gros).', 'Ser describes what someone lastingly is: Don Quijote es alto y delgado (tall and thin), Sancho es bajo y gordo (short and plump).'),
        ('Les cheveux et les yeux avec tener : tiene el pelo largo (il a les cheveux longs), tiene los ojos verdes.', 'Hair and eyes with tener: tiene el pelo largo (he has long hair), tiene los ojos verdes.'),
        ('Le caractère : simpático (sympathique), amable (aimable), valiente (courageux), tímido (timide), divertido (drôle).', 'Personality: simpático (nice), amable (kind), valiente (brave), tímido (shy), divertido (funny).'),
      ], [
        S('alto', 'alto / alta', ('grand (taille), haut', 'tall')),
        S('bajo', 'bajo / baja', ('petit / petite (taille)', 'short (height)')),
        S('delgado', 'delgado / delgada', ('mince', 'thin, slim')),
        S('pelo', 'el pelo', ('cheveux', 'hair')),
        S('ojos', 'los ojos', ('les yeux', 'the eyes')),
        S('simpatico', 'simpático / simpática', ('sympathique', 'nice, friendly')),
        S('valiente', 'valiente', ('courageux', 'brave')),
        S('joven', 'joven', ('jeune', 'young')),
        S('viejo', 'viejo / vieja', ('vieux ; âgé (âge)', 'old')),
      ], [
        x('Don Quijote es alto, delgado y muy valiente.', 'Don Quichotte est grand, mince et très courageux.', 'Don Quixote is tall, thin and very brave.'),
        x('Dulcinea es joven, tiene el pelo largo y los ojos negros.', 'Dulcinée est jeune, elle a les cheveux longs et les yeux noirs.', 'Dulcinea is young, she has long hair and dark eyes.'),
      ], [
        FB(CHOOSE, 'Sancho ＿ bajo y simpático.', ['es', 'está', 'tiene'], 'es', ('Description durable : ser.', 'Lasting description: ser.'), ('Sancho est petit et sympathique.', 'Sancho is short and nice.')),
        FB(CHOOSE, 'Mi hermana ＿ los ojos azules.', ['tiene', 'es', 'está'], 'tiene', ('Les yeux : tener.', 'Eyes: tener.'), ('Ma sœur a les yeux bleus.', 'My sister has blue eyes.')),
        FB(CHOOSE, 'Mis abuelos son muy ＿.', ['simpáticos', 'simpático', 'simpática'], 'simpáticos', ('Abuelos est masculin pluriel.', 'Abuelos is masculine plural.'), ('Mes grands-parents sont très sympathiques.', 'My grandparents are very nice.')),
        TF('Don Quijote es bajo y gordo.', ('Don Quichotte est grand et mince.', 'Don Quixote is tall and thin.'), FAUX, ('Bajo y gordo = petit et gros : c’est Sancho !', 'Bajo y gordo = short and plump: that’s Sancho!')),
      ]),
    L('es-ser-estar', ('Ser ou estar ?', 'Ser or estar?'), ('Choisir entre ser (ce qu’on est) et estar (comment on est, où on est).', 'Choose between ser (what you are) and estar (how or where you are).'), 9, [
        ('Ser : identité, origine, métier, caractère, description durable. Soy médico. Es de Toledo. Es alto.', 'Ser: identity, origin, job, personality, lasting description. Soy médico. Es de Toledo. Es alto.'),
        ('Estar : état passager et lieu. Estoy cansado (je suis fatigué), está enfermo (il est malade), estamos en casa (nous sommes à la maison).', 'Estar: temporary state and location. Estoy cansado (I’m tired), está enfermo (he’s ill), estamos en casa (we’re at home).'),
        ('Les états avec estar : contento (content), triste, cansado (fatigué), enfermo (malade), nervioso (nerveux), ocupado (occupé).', 'States with estar: contento (happy), triste (sad), cansado (tired), enfermo (ill), nervioso (nervous), ocupado (busy).'),
      ], [
        SG('ser-estar', 'ser / estar', ('être (identité) / être (état, lieu)', 'to be (identity) / to be (state, place)')),
        S('cansado', 'cansado / cansada', ('fatigué', 'tired')),
        S('contento', 'contento / contenta', ('content / contente', 'happy, pleased')),
        S('triste', 'triste', ('triste', 'sad')),
        S('enfermo', 'enfermo / enferma', ('malade', 'ill, sick')),
        S('nervioso', 'nervioso / nerviosa', ('nerveux / nerveuse', 'nervous')),
        S('medico', 'el médico / la médica', ('le médecin', 'the doctor')),
      ], [
        x('Sancho es simpático, pero hoy está cansado y triste.', 'Sancho est sympathique, mais aujourd’hui il est fatigué et triste.', 'Sancho is nice, but today he is tired and sad.'),
        x('Soy de Madrid, pero ahora estoy en Toledo.', 'Je suis de Madrid, mais en ce moment je suis à Tolède.', 'I’m from Madrid, but right now I’m in Toledo.'),
      ], [
        FB(CHOOSE, 'Hoy ＿ muy cansado.', ['estoy', 'soy', 'tengo'], 'estoy', ('État passager : estar.', 'Temporary state: estar.'), ('Aujourd’hui, je suis très fatigué.', 'Today I am very tired.')),
        FB(CHOOSE, 'Mi madre ＿ médica.', ['es', 'está', 'hay'], 'es', ('Métier : ser.', 'Job: ser.'), ('Ma mère est médecin.', 'My mother is a doctor.')),
        FB(CHOOSE, 'Don Quijote ＿ en el molino.', ['está', 'es', 'son'], 'está', ('Lieu : estar.', 'Location: estar.'), ('Don Quichotte est au moulin.', 'Don Quixote is at the mill.')),
        TF('Estoy enfermo: no voy a trabajar.', ('La personne est malade.', 'The person is ill.'), VRAI, ('Estar enfermo = être malade.', 'Estar enfermo = to be ill.')),
      ]),
  ]),
  CH('delea1-w8-c2', ('Après la bataille', 'After the battle'), [
    L('es-salud', ('J’ai mal : me duele, tener que', 'It hurts: me duele, tener que'), ('Dire où l’on a mal et donner un conseil simple.', 'Say where it hurts and give simple advice.'), 9, [
        ('Doler fonctionne comme gustar : me duele la cabeza (j’ai mal à la tête), me duelen los pies (au pluriel : duelen).', 'Doler works like gustar: me duele la cabeza (I have a headache), me duelen los pies (plural: duelen).'),
        ('Le corps : la cabeza (tête), el brazo (bras), la pierna (jambe), la mano (main), el pie (pied), la espalda (dos), el estómago (estomac).', 'The body: la cabeza (head), el brazo (arm), la pierna (leg), la mano (hand), el pie (foot), la espalda (back), el estómago (stomach).'),
        ('Obligation : tener que + infinitif. Tienes que descansar (tu dois te reposer), tengo que ir al médico.', 'Obligation: tener que + infinitive. Tienes que descansar (you must rest), tengo que ir al médico (I have to go to the doctor).'),
      ], [
        SG('doler', 'me duele / me duelen', ('j’ai mal à… (doler)', 'my… hurts (doler)')),
        SG('tener-que', 'tener que + infinitivo', ('devoir + infinitif', 'to have to + verb')),
        S('cabeza', 'la cabeza', ('la tête', 'the head')),
        S('brazo', 'el brazo', ('le bras', 'the arm')),
        S('pierna', 'la pierna', ('la jambe', 'the leg')),
        S('mano', 'la mano', ('la main', 'the hand')),
        S('espalda', 'la espalda', ('le dos', 'the back')),
        S('descansar', 'descansar', ('se reposer', 'to rest')),
      ], [
        x('Después de la batalla con los molinos, a don Quijote le duele todo el cuerpo.', 'Après la bataille contre les moulins, don Quichotte a mal partout.', 'After the battle with the windmills, Don Quixote aches all over.'),
        x('Me duele la cabeza. — Tienes que descansar y beber agua.', 'J’ai mal à la tête. — Tu dois te reposer et boire de l’eau.', 'I have a headache. — You must rest and drink water.'),
      ], [
        FB(CHOOSE, 'Me ＿ la espalda.', ['duele', 'duelen', 'duelo'], 'duele', ('La espalda est singulier : duele.', 'La espalda is singular: duele.'), ('J’ai mal au dos.', 'My back hurts.')),
        FB(CHOOSE, 'Me duelen los ＿.', ['pies', 'cabeza', 'mano'], 'pies', ('Duelen demande un pluriel : los pies.', 'Duelen needs a plural: los pies.'), ('J’ai mal aux pieds.', 'My feet hurt.')),
        FB(CHOOSE, 'Estás enfermo: tienes ＿ ir al médico.', ['que', 'a', 'de'], 'que', ('Obligation : tener que.', 'Obligation: tener que.'), ('Tu es malade : tu dois aller chez le médecin.', 'You’re ill: you have to go to the doctor.')),
        DC(ANSWER, [('Médico', '¿Qué le pasa?')], ('Le médecin demande ce qui ne va pas (tu as mal à la tête).', 'The doctor asks what’s wrong (you have a headache).'), ['Me duele mucho la cabeza.', 'Tengo la cabeza.', 'Soy la cabeza.'], 'Me duele mucho la cabeza.', ('Douleur : me duele + partie du corps.', 'Pain: me duele + body part.')),
      ]),
  ])])

write_level('DELEA1', ('DELE A1 : le chevalier de la Manche', 'DELE A1: the knight of La Mancha'), REGION, 'Roads of La Mancha', 56,
  [W1, W2, W3, W4, W5, W6, W7, W8, FINAL('DELEA1', REGION, ('Simulation DELE A1 : le palais des Ducs', 'DELE A1 simulation: the Dukes’ palace'), 'compréhension écrite, compréhension auditive et expression écrite (l’oral n’est pas évalué)', 'reading comprehension, listening comprehension and written expression (speaking is not assessed)')])
