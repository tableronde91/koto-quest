# Banque de questions de l'examen blanc DELE C1 (content/exams/delec1.json), au format de l'épreuve officielle
# de l'Instituto Cervantes : compréhension écrite et usage de la langue (5 tâches, 40 questions), compréhension auditive (4 tâches, 30 questions)
# et expression écrite intégrée (ici en format à choix : la meilleure synthèse et le compte rendu le mieux écrit).
# L'expression orale n'est pas évaluée. 170 minutes, notation sur 100, réussite avec au moins 30 points par groupe.
# Dans chaque question, le premier choix est la bonne réponse (l'ordre est mélangé à chaque examen).
# Usage : python3 scripts/delec1-exam.py
import json, os
ROOT = os.path.join(os.path.dirname(__file__), '..')
WHO = {'N': 'Narrateur', 'M': 'Homme', 'F': 'Femme'}

def LQ(audio, choices, text=None):
    lines = [l.strip() for l in audio.strip().split('\n') if l.strip()]
    for l in lines:
        assert l[1] == '|' and l[0] in WHO, l
    q = {'audio': '\n'.join(lines), 'choices': choices, 'answer': choices[0],
         'explanation': 'Transcription : ' + ' / '.join(f"{WHO[l[0]]} : {l[2:]}" for l in lines)}
    if text:
        q['text'] = text
    return q

def RQ(choices, jp=None, text=None, expl=None):
    q = {'choices': choices, 'answer': choices[0], 'explanation': expl or f'Réponse : {choices[0]}'}
    if jp: q['jp'] = jp
    if text: q['text'] = text
    return q

def RP(passage, question, choices):
    """Lecture : un texte, une question ★."""
    q = RQ(choices, None, '★ ' + question)
    q['passage'] = passage
    return q

def PART(id, section, jpTitle, title, prompt, count, questions, listening=False):
    for q in questions:
        assert 2 <= len(set(q['choices'])) == len(q['choices']) <= 4, q
    assert len(questions) >= count, id
    p = {'id': id, 'section': section, 'jpTitle': jpTitle, 'title': title, 'prompt': prompt, 'count': count, 'questions': questions}
    if listening:
        p['listening'] = True
    return p


TEXTO = ('La lectura en la era de las pantallas. Durante décadas se vaticinó la muerte del libro impreso; sin embargo, las cifras desmienten aquel pronóstico apocalíptico. '
         'En España, el número de lectores habituales no solo no ha disminuido, sino que ha aumentado ligeramente en la última década, impulsado en gran medida por los jóvenes. '
         'Lo que sí ha cambiado es la manera de leer. Diversos estudios señalan que la lectura en pantalla tiende a ser más fragmentaria y superficial: el lector salta de un párrafo a otro y retiene peor los detalles. '
         'No obstante, sería un error demonizar los dispositivos electrónicos. Para muchas personas con dificultades visuales, la posibilidad de ampliar la letra ha supuesto una auténtica revolución. '
         'Los expertos coinciden en que la clave no reside en el soporte, sino en la atención que le dedicamos. De ahí que algunas escuelas hayan recuperado la lectura en voz alta y los clubes de lectura, '
         'convencidas de que leer despacio, y en compañía, sigue siendo la mejor manera de comprender un texto en profundidad.')

RESENAS = ('A. «Una novela ambiciosa que, sin embargo, peca de excesiva: le sobran al menos cien páginas.»\n'
           'B. «El montaje teatral destaca por la interpretación de la protagonista; la escenografía, en cambio, deja que desear.»\n'
           'C. «Un ensayo riguroso y ameno a la vez, imprescindible para quien quiera entender la historia de la lengua.»\n'
           'D. «La película logra emocionar sin caer en el sentimentalismo, aunque el desenlace resulta previsible.»')

def RE(question, answer):
    return RP(RESENAS, question, [answer] + [n for n in ['A.', 'B.', 'C.', 'D.'] if n != answer])

def FR(passage, choices):
    return RP(passage, '¿Qué fragmento completa el hueco [ … ]?', choices)

def GR(sentence, choices):
    return RQ(choices, None, '★ ' + sentence)

# ═════════════════════════ Comprensión de lectura y uso de la lengua ═════════════════════════
R1 = PART('r-texto', 'reading', 'Comprensión de lectura y uso de la lengua — Tarea 1', 'Un texte d’analyse', 'Lea el texto y conteste a las preguntas.', 6, [
  RP(TEXTO, '¿Qué afirma el texto sobre el pronóstico de la muerte del libro?', ['Que los datos lo contradicen.', 'Que se ha cumplido.', 'Que nadie lo formuló nunca.']),
  RP(TEXTO, '¿Qué ha ocurrido con el número de lectores en España?', ['Ha aumentado ligeramente.', 'Se ha reducido a la mitad.', 'Se ha mantenido idéntico.']),
  RP(TEXTO, 'Según los estudios citados, la lectura en pantalla…', ['suele ser más superficial.', 'mejora la memoria.', 'es más lenta y profunda.']),
  RP(TEXTO, '¿Por qué no conviene demonizar los dispositivos electrónicos?', ['Porque ayudan a personas con problemas de visión.', 'Porque son más baratos.', 'Porque los jóvenes no leen libros.']),
  RP(TEXTO, 'Según los expertos, ¿qué es lo fundamental?', ['La atención que se presta a la lectura.', 'El tipo de soporte.', 'El precio de los libros.']),
  RP(TEXTO, '¿Por qué algunas escuelas recuperan la lectura en voz alta?', ['Porque creen que favorece la comprensión profunda.', 'Porque faltan libros.', 'Porque los alumnos no saben leer en silencio.']),
  RP(TEXTO, '¿Qué tono predomina en el texto?', ['Matizado y argumentativo.', 'Alarmista.', 'Humorístico.']),
])

R2 = PART('r-fragmentos', 'reading', 'Comprensión de lectura y uso de la lengua — Tarea 2', 'Un texte à reconstituer', 'Lea el texto y elija el fragmento que falta.', 6, [
  FR('La Celestina se publicó por primera vez en 1499. [ … ] De ahí que su autoría haya suscitado tantos debates.', ['Su autor, Fernando de Rojas, afirmó haber encontrado el primer acto ya escrito.', 'Es una novela de ciencia ficción.', 'Nunca llegó a imprimirse.']),
  FR('El Lazarillo de Tormes apareció de forma anónima en 1554. [ … ] Por eso fue incluido en el índice de libros prohibidos.', ['Su crítica a la hipocresía del clero incomodó a las autoridades.', 'Era un libro de recetas de cocina.', 'Lo escribió un rey para sus hijos.']),
  FR('Calderón de la Barca escribió más de cien comedias. [ … ] En ella, la frontera entre sueño y vigilia se vuelve borrosa.', ['La más célebre es, sin duda, La vida es sueño.', 'Ninguna se representó en vida del autor.', 'Todas transcurren en América.']),
  FR('Gustavo Adolfo Bécquer murió en 1870 sin ver publicadas sus Rimas. [ … ] Hoy es uno de los poetas más leídos en lengua española.', ['Sus amigos las reunieron y editaron un año después.', 'Las quemó antes de morir y se perdieron.', 'Se publicaron en francés.']),
  FR('El español es la lengua materna de casi quinientos millones de personas. [ … ] Sin embargo, la unidad del idioma se mantiene gracias a una norma culta compartida.', ['Su extensión geográfica explica la gran variedad de acentos y vocabulario.', 'Solo se habla en la península ibérica.', 'No tiene ninguna variante regional.']),
  FR('La Biblioteca Nacional de España fue fundada en 1712 por Felipe V. [ … ] Hoy conserva más de treinta millones de documentos.', ['En sus orígenes se llamó Real Biblioteca Pública.', 'Se cerró definitivamente en 1800.', 'Solo guarda periódicos actuales.']),
  FR('Muchos refranes tienen su origen en la vida rural. [ … ] Aun así, siguen usándose en las ciudades del siglo XXI.', ['Hablan de cosechas, de animales y del tiempo atmosférico.', 'Fueron inventados por las redes sociales.', 'Nadie los entiende en la actualidad.']),
])

R3 = PART('r-resenas', 'reading', 'Comprensión de lectura y uso de la lengua — Tarea 3', 'Quatre critiques', 'Lea las reseñas y diga a cuál corresponde cada enunciado.', 8, [
  RE('¿Qué reseña critica la extensión de la obra?', 'A.'),
  RE('¿Qué reseña elogia a una actriz?', 'B.'),
  RE('¿Qué reseña recomienda la obra sin reservas?', 'C.'),
  RE('¿Qué reseña considera que el final no sorprende?', 'D.'),
  RE('¿Qué reseña se refiere a un texto de no ficción?', 'C.'),
  RE('¿Qué reseña critica el decorado?', 'B.'),
  RE('¿Qué reseña destaca que la obra emociona con contención?', 'D.'),
  RE('¿Qué reseña califica la obra de ambiciosa?', 'A.'),
  RE('¿Qué reseña combina rigor y amenidad?', 'C.'),
])

R4 = PART('r-lexico', 'reading', 'Comprensión de lectura y uso de la lengua — Tarea 4', 'Lexique en contexte', 'Lea las frases y elija la opción correcta.', 10, [
  GR('El ayuntamiento ha decidido llevar a ＿ una reforma de la biblioteca.', ['cabo', 'término de', 'fin']),
  GR('La crisis dio ＿ a numerosas protestas.', ['lugar', 'paso de', 'cuenta']),
  GR('Hay que hacer ＿ a los nuevos retos tecnológicos.', ['frente', 'cara de', 'cabo']),
  GR('La reunión tendrá ＿ el próximo lunes.', ['lugar', 'sitio', 'espacio']),
  GR('No me di ＿ de que había cerrado la puerta.', ['cuenta', 'lugar', 'paso']),
  GR('El gobierno ha puesto en ＿ un plan de lectura.', ['marcha', 'camino', 'paso']),
  GR('Le preguntó por su ex delante de todos: metió la ＿.', ['pata', 'mano', 'pierna']),
  GR('Ese abrigo le costó un ojo de la ＿.', ['cara', 'mano', 'cabeza']),
  GR('No tiene pelos en la ＿: dice siempre lo que piensa.', ['lengua', 'boca', 'cabeza']),
  GR('El examen fue pan ＿: lo terminé en media hora.', ['comido', 'duro', 'tierno']),
  GR('Como dice el ＿, a quien madruga, Dios le ayuda.', ['refrán', 'dicho que', 'proverbial']),
])

R5 = PART('r-gramatica', 'reading', 'Comprensión de lectura y uso de la lengua — Tarea 5', 'Grammaire en contexte', 'Lea el texto y elija la opción correcta para cada hueco.', 10, [
  GR('El hecho de que la biblioteca ＿ los domingos es una excelente noticia.', ['abra', 'abre', 'abrirá']),
  GR('Que yo ＿, nadie ha encontrado todavía el manuscrito original.', ['sepa', 'sé', 'supe']),
  GR('Pase lo que ＿, terminaré la tesis este año.', ['pase', 'pasa', 'pasará']),
  GR('No es que no me ＿ el libro, es que no tengo tiempo.', ['guste', 'gusta', 'gustará']),
  GR('De ＿ sabido la verdad, habría actuado de otra manera.', ['haber', 'hubiera', 'habría']),
  GR('Tengo ＿ ya veinte páginas del informe.', ['escritas', 'escrito', 'escribiendo']),
  GR('Resulta curioso que nadie ＿ antes de este fenómeno.', ['hablara', 'habló', 'hablará']),
  GR('Se estima que más de mil personas ＿ a la conferencia.', ['asistieron', 'asistieran', 'asistan']),
  GR('Por mucho que lo ＿, no lograrás convencerlo.', ['intentes', 'intentas', 'intentarás']),
  GR('Lo ＿ es que la obra sigue siendo actual.', ['sorprendente', 'sorprendida', 'sorprender']),
  GR('Para ＿ tan joven, escribe con una madurez asombrosa.', ['ser', 'estar', 'tener']),
])

# ═════════════════════════ Comprensión auditiva y uso de la lengua ═════════════════════════
L1 = PART('l-conferencia', 'listening', 'Comprensión auditiva y uso de la lengua — Tarea 1', 'Une conférence', 'Escuche el fragmento de una conferencia sobre la historia del español y conteste a las preguntas.', 6, [
  LQ('F|El español procede del latín vulgar que hablaban los soldados y comerciantes romanos, no del latín clásico de Cicerón.\nN|Pregunta: ¿De qué procede el español, según la conferenciante?', ['Del latín vulgar.', 'Del latín clásico.', 'Del griego.']),
  LQ('F|Los primeros testimonios escritos de una lengua romance en la península son las Glosas Emilianenses, unas anotaciones al margen de un texto latino.\nN|Pregunta: ¿Qué son las Glosas Emilianenses?', ['Anotaciones al margen de un texto latino.', 'Un poema épico completo.', 'Un diccionario moderno.']),
  LQ('F|En 1492 Antonio de Nebrija publicó la primera gramática de una lengua europea moderna, la gramática castellana.\nN|Pregunta: ¿Qué publicó Nebrija en 1492?', ['La primera gramática del castellano.', 'El primer diccionario de francés.', 'Una novela de caballerías.']),
  LQ('F|Ese mismo año, la llegada de los españoles a América cambió para siempre la historia del idioma, que se extendió por todo un continente.\nN|Pregunta: ¿Qué otro hecho de 1492 destaca la conferenciante?', ['La llegada de los españoles a América.', 'La invención de la imprenta.', 'La fundación de Madrid.']),
  LQ('F|La Real Academia Española se fundó en 1713 con el lema «Limpia, fija y da esplendor».\nN|Pregunta: ¿Cuándo se fundó la Real Academia Española?', ['En 1713.', 'En 1492.', 'En 1812.']),
  LQ('F|Hoy, la Asociación de Academias de la Lengua Española reúne a veintitrés academias que trabajan de forma conjunta en la norma del idioma.\nN|Pregunta: ¿Qué hacen hoy las academias de la lengua?', ['Trabajan juntas en la norma común.', 'Compiten entre ellas.', 'Solo se ocupan del español de España.']),
  LQ('F|En definitiva, el español es una lengua policéntrica: no existe un único modelo correcto, sino varias normas cultas igualmente válidas.\nN|Pregunta: ¿Qué significa que el español es una lengua policéntrica?', ['Que tiene varias normas cultas válidas.', 'Que solo se habla en ciudades.', 'Que tiene un único modelo correcto.']),
], listening=True)

L2 = PART('l-implicito', 'listening', 'Comprensión auditiva y uso de la lengua — Tarea 2', 'Le sens implicite', 'Escuche las conversaciones y elija la interpretación correcta.', 8, [
  LQ('M|¿Qué tal el concierto?\nF|¡Uf! Menudo rollo: tres horas de solos de batería.\nN|Pregunta: ¿Qué opina la mujer del concierto?', ['Le pareció aburrido.', 'Le encantó.', 'No fue.']),
  LQ('F|He suspendido el examen de conducir otra vez.\nM|Bueno, no hay mal que por bien no venga: así practicas un poco más.\nN|Pregunta: ¿Qué intenta hacer el hombre?', ['Consolarla.', 'Burlarse de ella.', 'Criticarla.']),
  LQ('M|¿Le has dicho a Marta lo de la fiesta sorpresa?\nF|Sí… creo que he metido la pata.\nN|Pregunta: ¿Qué ha pasado?', ['La mujer ha cometido un error.', 'La fiesta ha sido un éxito.', 'Marta no ha entendido nada.']),
  LQ('F|¿Me prestas tu coche nuevo para el fin de semana?\nM|Sí, claro, y te doy también las llaves de mi casa, ¿no?\nN|Pregunta: ¿Qué quiere decir el hombre?', ['Que no piensa prestarle el coche.', 'Que le prestará el coche y la casa.', 'Que no tiene coche.']),
  LQ('M|¿Has visto a Luis? Dice que ha escrito una novela de mil páginas.\nF|¿Luis? Ese no tiene abuela.\nN|Pregunta: ¿Qué piensa la mujer de Luis?', ['Que es presumido.', 'Que es huérfano.', 'Que es muy modesto.']),
  LQ('F|Llevamos media hora esperando y el camarero ni nos mira.\nM|¡Pues sí que estamos buenos! Así no cenamos hasta medianoche.\nN|Pregunta: ¿Cómo se siente el hombre?', ['Molesto por la situación.', 'Contento con el servicio.', 'Indiferente.']),
  LQ('M|Al final, ¿aceptaste el trabajo en Bilbao?\nF|Ni loca. Con lo que pagaban, no me daba ni para el alquiler.\nN|Pregunta: ¿Qué decidió la mujer?', ['Rechazar el trabajo.', 'Aceptar el trabajo.', 'Mudarse a Bilbao.']),
  LQ('F|¿Te ayudo con la mudanza?\nM|Si no es mucha molestia… te lo agradecería en el alma.\nN|Pregunta: ¿Qué responde el hombre?', ['Acepta la ayuda con mucho agradecimiento.', 'Rechaza la ayuda.', 'Dice que ya ha terminado.']),
  LQ('M|¿Qué te pareció la conferencia?\nF|Digamos que he oído cosas más interesantes.\nN|Pregunta: ¿Qué opina la mujer de la conferencia?', ['No le gustó mucho.', 'Le pareció fascinante.', 'No la escuchó.']),
], listening=True)

L3 = PART('l-entrevista', 'listening', 'Comprensión auditiva y uso de la lengua — Tarea 3', 'Une interview', 'Escuche la entrevista a una traductora literaria y conteste a las preguntas.', 8, [
  LQ('M|Elena, ¿cómo llegó a la traducción literaria?\nF|Por casualidad. Estudiaba Filología Francesa y un profesor me pidió que tradujera unos poemas para una revista.\nN|Pregunta: ¿Cómo empezó Elena a traducir?', ['Por un encargo de un profesor.', 'Por un concurso.', 'Por su padre, que era traductor.']),
  LQ('M|¿Qué es lo más difícil de traducir?\nF|El humor, sin duda. Un juego de palabras rara vez funciona en otra lengua; hay que reinventarlo.\nN|Pregunta: ¿Qué le resulta más difícil?', ['Traducir el humor.', 'Traducir los nombres propios.', 'Cumplir los plazos.']),
  LQ('M|¿Y la poesía?\nF|La poesía es otro reto: hay que elegir entre ser fiel al sentido o a la música del verso. Casi nunca se puede tener las dos cosas.\nN|Pregunta: ¿Qué dilema plantea la poesía?', ['Elegir entre el sentido y la música.', 'Elegir entre dos editoriales.', 'Elegir entre prosa y verso.']),
  LQ('M|¿Usa herramientas de traducción automática?\nF|Para documentos técnicos, quizá; para la literatura, no. Una máquina no capta la ironía ni los dobles sentidos.\nN|Pregunta: ¿Qué piensa de la traducción automática?', ['Que no sirve para la literatura.', 'Que es mejor que un traductor humano.', 'Que la usa para todo.']),
  LQ('M|¿Está bien pagado el oficio?\nF|Digamos que nadie se hace rico traduciendo novelas. Lo hacemos por vocación.\nN|Pregunta: ¿Qué da a entender sobre el sueldo?', ['Que es modesto.', 'Que es muy alto.', 'Que depende del idioma.']),
  LQ('M|¿Qué libro le habría gustado traducir?\nF|El Quijote al francés, aunque ya existen traducciones magníficas. ¡Quién tuviera ese honor!\nN|Pregunta: ¿Qué libro le habría gustado traducir?', ['El Quijote.', 'La Celestina.', 'Las Rimas de Bécquer.']),
  LQ('M|¿Algún consejo para los futuros traductores?\nF|Que lean muchísimo en su propia lengua. Se traduce hacia la lengua materna, y hay que dominarla a la perfección.\nN|Pregunta: ¿Qué aconseja Elena?', ['Leer mucho en la lengua materna.', 'Vivir en el extranjero.', 'Aprender muchos idiomas a la vez.']),
  LQ('M|Por último, ¿en qué trabaja ahora?\nF|En una antología de cuentos latinoamericanos que saldrá en primavera.\nN|Pregunta: ¿En qué trabaja actualmente?', ['En una antología de cuentos.', 'En una novela propia.', 'En un diccionario.']),
  LQ('M|¿Cuánto tarda en traducir una novela?\nF|Depende, pero una novela de trescientas páginas me lleva unos seis meses de trabajo.\nN|Pregunta: ¿Cuánto tarda en traducir una novela de trescientas páginas?', ['Unos seis meses.', 'Unas tres semanas.', 'Unos dos años.']),
], listening=True)

L4 = PART('l-tertulia', 'listening', 'Comprensión auditiva y uso de la lengua — Tarea 4', 'Un débat radio', 'Escuche la tertulia sobre las redes sociales y elija la opción correcta.', 8, [
  LQ('N|Hoy debatimos sobre si las redes sociales empobrecen el idioma.\nM|Yo no lo creo: los jóvenes escriben más que nunca, aunque de otra manera.\nN|Pregunta: ¿Qué opina el primer tertuliano?', ['Que los jóvenes escriben más, pero de otra forma.', 'Que los jóvenes ya no escriben.', 'Que hay que prohibir las redes.']),
  LQ('F|Discrepo. Escribir mucho no significa escribir bien: las abreviaturas y la falta de tildes se trasladan a los exámenes.\nN|Pregunta: ¿Qué preocupa a la tertuliana?', ['Que los errores pasen a los exámenes.', 'Que los jóvenes lean demasiado.', 'Que desaparezcan las abreviaturas.']),
  LQ('M|No obstante, la lengua siempre ha evolucionado. Lo mismo se dijo del telégrafo y del teléfono.\nN|Pregunta: ¿Qué argumento usa el tertuliano?', ['Que la lengua siempre ha cambiado.', 'Que el telégrafo fue un error.', 'Que el teléfono empobreció el idioma.']),
  LQ('F|Estoy de acuerdo en que cambia, pero la escuela debe enseñar a distinguir registros: no se escribe igual un mensaje que una carta formal.\nN|Pregunta: ¿Qué propone la tertuliana?', ['Enseñar a distinguir registros.', 'Eliminar las cartas formales.', 'Escribir siempre como en los mensajes.']),
  LQ('M|En eso coincidimos. Y, por cierto, las redes también han difundido palabras de toda Hispanoamérica.\nN|Pregunta: ¿Qué efecto positivo menciona?', ['La difusión de palabras de toda Hispanoamérica.', 'La desaparición de los acentos.', 'El aumento de las faltas.']),
  LQ('F|Cierto. Gracias a internet, un chico de Madrid sabe hoy lo que significa «chamba» o «pibe».\nN|Pregunta: ¿Qué ejemplo da la tertuliana?', ['El conocimiento de palabras americanas.', 'El uso de palabras inglesas.', 'El olvido del vocabulario español.']),
  LQ('N|Para terminar, ¿una recomendación?\nM|Leer, leer y leer. Es la mejor vacuna contra el empobrecimiento del idioma.\nN|Pregunta: ¿Qué recomienda el tertuliano?', ['Leer mucho.', 'Usar menos el móvil.', 'Estudiar gramática.']),
  LQ('F|Y escribir a mano de vez en cuando; obliga a pensar antes de escribir.\nN|Pregunta: ¿Qué recomienda la tertuliana?', ['Escribir a mano de vez en cuando.', 'No escribir nunca a mano.', 'Escribir solo en el ordenador.']),
  LQ('N|En resumen, ¿las redes empobrecen el idioma?\nF|Digamos que depende de cómo las usemos.\nN|Pregunta: ¿Cuál es la conclusión de la tertuliana?', ['Que depende del uso que hagamos.', 'Que sí, sin ninguna duda.', 'Que no tienen ningún efecto.']),
], listening=True)

# ═════════════════════════ Destrezas integradas: comprensión y expresión escritas ═════════════════════════
CONF = 'Usted ha asistido a una conferencia sobre la lectura en la era digital. Según la ponente, el número de lectores ha aumentado, pero se lee de forma más fragmentaria; propone recuperar la lectura en voz alta y los clubes de lectura.'
W1 = PART('w-sintesis', 'writing', 'Destrezas integradas — Tarea 1', 'Une synthèse', 'Lea la situación y elija la opción mejor redactada.', 3, [
  RQ(['La ponente sostuvo que, si bien el número de lectores ha aumentado, la lectura digital tiende a ser más fragmentaria; por consiguiente, propuso recuperar la lectura en voz alta y los clubes de lectura.',
      'La ponente dijo que hay más lectores pero se lee peor y que hay que leer en voz alta.',
      'La ponente sostuvo que el número de lectores ha disminuido drásticamente y que conviene prohibir las pantallas.',
      'Lectores, pantallas, voz alta, clubes.'],
     None, f'{CONF}\n★ Elija la síntesis más completa, fiel y formal.'),
  RQ(['Cabe señalar que la ponente no rechazó los dispositivos electrónicos.', 'Cabe señalar de que la ponente no rechazó los dispositivos electrónicos.', 'Cabe señalar que la ponente no rechazara los dispositivos electrónicos.', 'Cabe a señalar que la ponente no rechazó los dispositivos electrónicos.'],
     None, f'{CONF}\n★ Elija la frase correcta.'),
  RQ(['Resulta lógico que las escuelas quieran recuperar la lectura en voz alta.', 'Resulta lógico que las escuelas quieren recuperar la lectura en voz alta.', 'Resulta lógico de que las escuelas quieran recuperar la lectura en voz alta.', 'Resulta lógico que las escuelas querrán recuperar la lectura en voz alta.'],
     None, f'{CONF}\n★ Elija la frase correcta para valorar la propuesta.'),
  RQ(['En cuanto a los clubes de lectura, la ponente destacó su función social.', 'En cuanto los clubes de lectura, la ponente destacó su función social.', 'En cuanto a los clubes de lectura, la ponente destacó por su función social a.', 'Cuanto a los clubes de lectura, la ponente destacó su función social.'],
     None, f'{CONF}\n★ Elija la frase correcta.'),
])

W2 = PART('w-resena', 'writing', 'Destrezas integradas — Tarea 2', 'Un compte rendu critique', 'Lea la situación y elija el texto mejor escrito.', 2, [
  RQ(['La versión teatral de La vida es sueño que se representa estos días en Madrid destaca por la intensidad del actor protagonista y por una escenografía sobria que pone el foco en el texto. Si bien el ritmo decae en el tercer acto, el montaje logra transmitir la vigencia de las preguntas de Calderón. En definitiva, una propuesta que merece la pena.',
      'La versión teatral de La vida es sueño destaca por el actor y por la escenografía. Si bien el ritmo decaiga en el tercer acto, el montaje logra transmitir. En definitiva, merece pena.',
      'Fui al teatro. Estaba bien. El actor guay. Recomendado.',
      'La versión teatral de La vida es sueño es la peor obra de la historia porque es mala y no me gustó nada de nada.'],
     None, '★ Situación: escriba la reseña de una obra de teatro para una revista cultural.'),
  RQ(['El ensayo aborda con rigor la evolución del español en América. Cabe destacar la claridad con la que el autor explica fenómenos complejos, como el voseo o el seseo. No obstante, se echa de menos un capítulo dedicado a las lenguas indígenas. Aun así, resulta una lectura imprescindible.',
      'El ensayo aborda la evolución del español. Cabe destacar la claridad. No obstante, se echa de menos un capítulo. Aun así, resulte imprescindible.',
      'Libro sobre el español en América. Voseo, seseo. Bueno.',
      'El ensayo no aborda nada y cabe destacar que no explica nada, por lo tanto es imprescindible.'],
     None, '★ Situación: escriba la reseña de un ensayo para el blog de una biblioteca.'),
  RQ(['La película adapta con acierto la leyenda de Bécquer: la fotografía, de tonos verdes y fríos, recrea la atmósfera inquietante del relato. Sin embargo, el guion añade un desenlace feliz que traiciona el espíritu del original. Pese a ello, merece la pena verla en pantalla grande.',
      'La película adapta la leyenda de Bécquer: la fotografía recrea la atmósfera. Sin embargo, el guion añadiera un desenlace feliz. Pese a ello, merece verla.',
      'Película verde. Final feliz. Bien.',
      'La película es exactamente igual que el libro y por eso no tiene nada que comentar.'],
     None, '★ Situación: escriba la reseña de una adaptación cinematográfica.'),
])

PARTS = [R1, R2, R3, R4, R5, L1, L2, L3, L4, W1, W2]
rea = sum(p['count'] for p in PARTS if p['section'] == 'reading')
lis = sum(p['count'] for p in PARTS if p['section'] == 'listening')
wri = sum(p['count'] for p in PARTS if p['section'] == 'writing')
assert (rea, lis, wri) == (40, 30, 5), (rea, lis, wri)
bank = {
  'slug': 'delec1',
  'level': 'DELEC1',
  'contentVersion': '2026.11.24',
  'notice': 'Questions rédigées par Koto Quest au format de l’examen officiel du DELE C1 (Instituto Cervantes : épreuves de compréhension et d’usage de la langue, consignes en espagnol, notation sur 100 en deux groupes). L’expression écrite intégrée se fait par choix multiple et l’expression orale n’est pas évaluée : le groupe 2 est noté sur l’écoute. Ce ne sont pas des questions officielles.',
  'parts': PARTS,
}
json.dump(bank, open(os.path.join(ROOT, 'content/exams/delec1.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
EN = {
  bank['notice']: 'Questions written by Koto Quest in the format of the official DELE C1 exam (Instituto Cervantes: comprehension and use-of-language tests, instructions in Spanish, scoring out of 100 in two groups). Integrated written expression is multiple choice and speaking is not assessed: group 2 is marked on listening. They are not official questions.',
  'Un texte d’analyse': 'An analytical text', 'Un texte à reconstituer': 'A text to reconstruct', 'Quatre critiques': 'Four reviews',
  'Lexique en contexte': 'Vocabulary in context', 'Grammaire en contexte': 'Grammar in context',
  'Une conférence': 'A lecture', 'Le sens implicite': 'Implied meaning', 'Une interview': 'An interview', 'Un débat radio': 'A radio debate',
  'Une synthèse': 'A summary', 'Un compte rendu critique': 'A critical review',
}
P_DICT = os.path.join(ROOT, 'content/i18n/en/content.json')
d = json.load(open(P_DICT, encoding='utf-8'))
for k, v in EN.items():
    if k in d and d[k] != v:
        raise SystemExit(f'traduction existante différente : {k} → {d[k]} / {v}')
d.update(EN)
json.dump(d, open(P_DICT, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(f"DELE C1 : {sum(len(p['questions']) for p in PARTS)} questions en banque ; examen de {rea} + {lis} + {wri} questions")
