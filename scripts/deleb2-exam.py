# Banque de questions de l'examen blanc DELE B2 (content/exams/deleb2.json), au format de l'épreuve officielle
# de l'Instituto Cervantes : compréhension écrite (4 tâches, 36 questions), compréhension auditive (5 tâches, 30 questions)
# et expression écrite (ici en format à choix : choisir la meilleure lettre et l’article le mieux écrit).
# L'expression orale n'est pas évaluée. 150 minutes, notation sur 100, réussite avec au moins 30 points par groupe.
# Dans chaque question, le premier choix est la bonne réponse (l'ordre est mélangé à chaque examen).
# Usage : python3 scripts/deleb2-exam.py
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



ARTICULO = ('El auge de las lenguas originarias en internet. Durante siglos, el quechua, el guaraní o el náhuatl se transmitieron casi exclusivamente de forma oral, y muchos jóvenes dejaron de hablarlos al trasladarse a las ciudades. '
            'Sin embargo, en la última década ha surgido un fenómeno inesperado: cientos de creadores publican vídeos, canciones y podcasts en estas lenguas. '
            'Según la lingüista peruana Rosa Mamani, «las redes sociales han conseguido lo que no lograron décadas de políticas educativas: que los jóvenes se sientan orgullosos de hablar la lengua de sus abuelos». '
            'No obstante, los expertos advierten de que el entusiasmo digital no basta. Para que una lengua sobreviva, es imprescindible que se utilice en la escuela, en la administración y en la vida cotidiana. '
            'En Paraguay, donde el guaraní es oficial junto al español desde 1992, la mayoría de la población es bilingüe, lo cual demuestra que la convivencia de lenguas es posible si existe voluntad política. '
            'Mamani concluye con optimismo: «Si hace veinte años me hubieran dicho que un rapero cantaría en quechua ante miles de personas, no lo habría creído».')

PERFILES = ('Valeria (Bogotá): Dejé mi trabajo en un banco para abrir una librería de barrio. Gano menos, pero por fin hago lo que me apasiona. Lo más duro fue convencer a mi familia.\n'
            'Tomás (Santiago de Chile): Llevo diez años teletrabajando para una empresa de Canadá. Me encanta la flexibilidad, aunque a veces echo de menos tener compañeros con quienes tomar un café.\n'
            'Inés (Sevilla): Me mudé a un pueblo de la sierra cuando nació mi hija. Allí la vida es más barata y tranquila, si bien las conexiones de transporte dejan mucho que desear.\n'
            'Rodrigo (Montevideo): Estudié Derecho porque mis padres insistieron, pero a los treinta años me hice cocinero. No me arrepiento en absoluto, aunque trabajo todos los fines de semana.')

def PE(question, answer):
    return RP(PERFILES, question, [answer] + [n for n in ['Valeria.', 'Tomás.', 'Inés.', 'Rodrigo.'] if n != answer])

def FR(passage, choices):
    return RP(passage, '¿Qué fragmento completa el hueco [ … ]?', choices)

def GR(sentence, choices):
    return RQ(choices, None, '★ ' + sentence)

# ═════════════════════════ Comprensión de lectura ═════════════════════════
R1 = PART('r-articulo', 'reading', 'Comprensión de lectura — Tarea 1', 'Un article', 'Lea el texto y conteste a las preguntas.', 6, [
  RP(ARTICULO, '¿Por qué muchos jóvenes dejaron de hablar las lenguas originarias?', ['Porque se fueron a vivir a las ciudades.', 'Porque estaban prohibidas en internet.', 'Porque sus abuelos no las hablaban.']),
  RP(ARTICULO, '¿Qué fenómeno ha surgido en la última década?', ['Muchos creadores publican contenidos en estas lenguas.', 'Las escuelas han dejado de enseñarlas.', 'Los jóvenes han olvidado el español.']),
  RP(ARTICULO, 'Según Rosa Mamani, las redes sociales…', ['han hecho que los jóvenes se sientan orgullosos de su lengua.', 'han fracasado como las políticas educativas.', 'son peligrosas para las lenguas originarias.']),
  RP(ARTICULO, '¿Qué advierten los expertos?', ['Que una lengua necesita usarse también en la escuela y la administración.', 'Que internet es suficiente para salvar una lengua.', 'Que el entusiasmo digital es negativo.']),
  RP(ARTICULO, '¿Qué demuestra el caso de Paraguay?', ['Que la convivencia de lenguas es posible con voluntad política.', 'Que el guaraní está desapareciendo.', 'Que nadie habla español en Paraguay.']),
  RP(ARTICULO, '¿Cómo se siente Mamani al final del texto?', ['Optimista.', 'Decepcionada.', 'Indiferente.']),
  RP(ARTICULO, '¿Desde cuándo es oficial el guaraní en Paraguay?', ['Desde 1992.', 'Desde hace veinte años exactos.', 'Desde el siglo XIX.']),
])

R2 = PART('r-perfiles', 'reading', 'Comprensión de lectura — Tarea 2', 'Quatre parcours', 'Lea los textos y diga a qué persona corresponde cada enunciado.', 10, [
  PE('¿Quién cambió de profesión a pesar de sus estudios?', 'Rodrigo.'),
  PE('¿Quién trabaja para una empresa extranjera?', 'Tomás.'),
  PE('¿Quién tuvo dificultades con su familia?', 'Valeria.'),
  PE('¿Quién se queja del transporte?', 'Inés.'),
  PE('¿Quién echa de menos la vida en la oficina?', 'Tomás.'),
  PE('¿Quién cambió de vida por la llegada de un hijo?', 'Inés.'),
  PE('¿Quién gana ahora menos dinero?', 'Valeria.'),
  PE('¿Quién no tiene libres los fines de semana?', 'Rodrigo.'),
  PE('¿Quién vive ahora en un lugar más barato?', 'Inés.'),
  PE('¿Quién valora sobre todo la flexibilidad?', 'Tomás.'),
  PE('¿Quién eligió su carrera por presión familiar?', 'Rodrigo.'),
])

R3 = PART('r-fragmentos', 'reading', 'Comprensión de lectura — Tarea 3', 'Un texte à compléter', 'Lea el texto y elija el fragmento que falta.', 6, [
  FR('El Caleuche es uno de los mitos más conocidos de Chiloé. [ … ] Quienes lo ven, dicen, no vuelven a ser los mismos.', ['Se trata de un barco fantasma que navega de noche, iluminado y lleno de música.', 'Es un plato típico que se prepara con mariscos.', 'Es el nombre del aeropuerto de la isla.']),
  FR('El voseo no es exclusivo de Argentina. [ … ] En cada país, sin embargo, presenta formas ligeramente distintas.', ['También se usa en Uruguay, Paraguay y gran parte de Centroamérica.', 'En España es la forma más habitual de tratamiento.', 'Nadie lo utiliza ya en la vida cotidiana.']),
  FR('Machu Picchu recibe más de un millón de visitantes al año. [ … ] Por ello, las autoridades han limitado el número de entradas diarias.', ['Esta afluencia masiva pone en peligro la conservación del lugar.', 'Casi nadie conoce su existencia.', 'Está situado junto al mar Caribe.']),
  FR('La tortilla de maíz es la base de la cocina mexicana. [ … ] De hecho, en 2010 esta cocina fue declarada patrimonio cultural inmaterial de la humanidad.', ['Su elaboración se transmite de generación en generación desde hace miles de años.', 'Se inventó en Europa en el siglo XX.', 'Solo se come en los restaurantes caros.']),
  FR('El teletrabajo ha transformado muchas ciudades latinoamericanas. [ … ] Como consecuencia, algunos barrios céntricos han perdido comercios.', ['Miles de empleados ya no se desplazan cada día a las oficinas.', 'Ahora todos los trabajadores viven en el centro.', 'Las empresas han prohibido trabajar desde casa.']),
  FR('Antigua Guatemala sufrió varios terremotos devastadores. [ … ] Hoy sus ruinas coloniales atraen a viajeros de todo el mundo.', ['Tras el de 1773, la capital se trasladó a otro valle.', 'Por eso nunca ha tenido iglesias.', 'Nunca ha habido volcanes cerca de la ciudad.']),
  FR('El tango nació en los barrios humildes de Buenos Aires y Montevideo. [ … ] Hoy se baila en todo el mundo.', ['Al principio estaba mal visto por la alta sociedad, pero acabó conquistando los salones.', 'Siempre fue el baile oficial de la corte española.', 'Se inventó en un conservatorio de París.']),
])

R4 = PART('r-gramatica', 'reading', 'Comprensión de lectura — Tarea 4', 'Grammaire en contexte', 'Lea el texto y elija la opción correcta para cada hueco.', 14, [
  GR('Si hubiera sabido que el viaje era tan largo, ＿ más libros.', ['habría traído', 'traería', 'traje']),
  GR('Mis padres querían que ＿ Medicina, pero elegí Historia.', ['estudiara', 'estudie', 'estudiaba']),
  GR('Aunque ＿ toda la noche, no terminaré el informe a tiempo.', ['trabaje', 'trabajaría', 'trabajé']),
  GR('El puente ＿ construido por los incas hace cinco siglos.', ['fue', 'estuvo', 'era siendo']),
  GR('Te llamaré en cuanto ＿ a Lima.', ['llegue', 'llego', 'llegaré']),
  GR('Es el escritor ＿ novelas se han traducido a treinta idiomas.', ['cuyas', 'cuyos', 'que sus']),
  GR('Hablaba con tanta seguridad como si ＿ el dueño de la empresa.', ['fuera', 'es', 'sea']),
  GR('Por mucho que ＿, no lograrás convencerme.', ['insistas', 'insistes', 'insistirás']),
  GR('El guía nos dijo que al día siguiente ＿ la excursión al volcán.', ['haríamos', 'haremos', 'hagamos']),
  GR('Llévate el paraguas ＿ llueve.', ['por si', 'en caso de que', 'a no ser que']),
  GR('Cuando se enteró de la noticia, se ＿ muy triste.', ['puso', 'hizo', 'volvió a']),
  GR('Se ＿ pisos en el centro histórico.', ['alquilan', 'alquila', 'alquilen']),
  GR('Ojalá ＿ venido a la fiesta: lo habríamos pasado genial.', ['hubieras', 'habrías', 'hayas sido']),
  GR('No creo que la reunión ＿ antes de las ocho.', ['termine', 'termina', 'terminará']),
  GR('Te presto el coche siempre que me lo ＿ con el depósito lleno.', ['devuelvas', 'devuelves', 'devolverás']),
])

# ═════════════════════════ Comprensión auditiva ═════════════════════════
L1 = PART('l-conversaciones', 'listening', 'Comprensión auditiva — Tarea 1', 'Conversations courtes', 'Escuche las conversaciones y elija la opción correcta.', 6, [
  LQ('F|¿Al final aceptaste el trabajo en Quito?\nM|No, me lo pensé mucho, pero si me hubiera ido, habría tenido que dejar a mi padre solo.\nN|Pregunta: ¿Por qué no aceptó el trabajo?', ['Para no dejar solo a su padre.', 'Porque el sueldo era bajo.', 'Porque no le gusta Quito.']),
  LQ('M|¿Qué tal la entrevista?\nF|Bien, aunque me preguntaron por mis puntos débiles y me quedé en blanco.\nN|Pregunta: ¿Qué le pasó a la mujer en la entrevista?', ['No supo qué responder a una pregunta.', 'Llegó tarde.', 'Le ofrecieron el puesto enseguida.']),
  LQ('F|Te noto cansado.\nM|Es que llevo una semana durmiendo mal: los vecinos están de obras.\nN|Pregunta: ¿Por qué está cansado el hombre?', ['Por las obras de los vecinos.', 'Porque trabaja de noche.', 'Porque está enfermo.']),
  LQ('M|¿Vienes al concierto el sábado?\nF|Iré siempre que termine el informe a tiempo; si no, me quedo en casa.\nN|Pregunta: ¿De qué depende que la mujer vaya al concierto?', ['De terminar un informe.', 'Del precio de la entrada.', 'Del tiempo que haga.']),
  LQ('F|Dicen que van a cerrar la biblioteca del barrio.\nM|¿En serio? Pues habría que hacer algo: es el único sitio donde estudian los chicos.\nN|Pregunta: ¿Qué opina el hombre?', ['Que hay que actuar para evitar el cierre.', 'Que el cierre es una buena idea.', 'Que nadie usa la biblioteca.']),
  LQ('M|¿Has leído la novela que te presté?\nF|Sí, y aunque el final me decepcionó un poco, la recomendaría.\nN|Pregunta: ¿Qué piensa la mujer de la novela?', ['Que merece la pena, a pesar del final.', 'Que es la peor que ha leído.', 'Que todavía no la ha empezado.']),
  LQ('F|Perdona por no haberte llamado.\nM|No pasa nada, pero la próxima vez avísame antes, que te estuve esperando una hora.\nN|Pregunta: ¿Qué le pide el hombre?', ['Que le avise la próxima vez.', 'Que le devuelva el dinero.', 'Que no lo llame nunca.']),
], listening=True)

L2 = PART('l-debate', 'listening', 'Comprensión auditiva — Tarea 2', 'Un débat', 'Escuche a Lucía y Martín, que debaten sobre el turismo, y elija la opción correcta.', 6, [
  LQ('F|Para mí, el turismo es una oportunidad: crea empleo y permite conservar el patrimonio.\nN|Pregunta: ¿Qué ventaja menciona Lucía?', ['Crea empleo y ayuda a conservar el patrimonio.', 'Hace subir los precios.', 'Reduce la contaminación.']),
  LQ('M|No niego que crea empleo, pero muchos contratos son temporales y mal pagados.\nN|Pregunta: ¿Qué critica Martín?', ['La calidad de los empleos.', 'La falta de turistas.', 'El patrimonio histórico.']),
  LQ('F|Si bien es cierto que hay problemas, sin turismo muchos pueblos se habrían quedado vacíos.\nN|Pregunta: ¿Qué argumento da Lucía?', ['El turismo ha evitado que algunos pueblos se vacíen.', 'Los pueblos ya estaban vacíos.', 'El turismo no tiene problemas.']),
  LQ('M|Por el contrario, en el centro de muchas ciudades los vecinos se han tenido que ir por el precio de los alquileres.\nN|Pregunta: ¿Qué problema menciona Martín?', ['El aumento de los alquileres expulsa a los vecinos.', 'El ruido de los bares.', 'La falta de hoteles.']),
  LQ('F|Quizás la solución sea limitar los pisos turísticos en ciertos barrios.\nN|Pregunta: ¿Qué propone Lucía?', ['Limitar los pisos turísticos en algunos barrios.', 'Prohibir el turismo.', 'Construir más hoteles.']),
  LQ('M|En eso estoy de acuerdo contigo: hay que encontrar un equilibrio.\nN|Pregunta: ¿En qué coinciden finalmente?', ['En que hace falta un equilibrio.', 'En que el turismo es malo.', 'En que no hay solución.']),
  LQ('F|Y, por supuesto, habría que escuchar más a los vecinos antes de tomar decisiones.\nN|Pregunta: ¿Qué añade Lucía?', ['Que hay que tener en cuenta la opinión de los vecinos.', 'Que los vecinos deben irse.', 'Que las decisiones ya están tomadas.']),
], listening=True)

L3 = PART('l-entrevista', 'listening', 'Comprensión auditiva — Tarea 3', 'Une interview', 'Escuche la entrevista a una fotógrafa chilena y conteste a las preguntas.', 6, [
  LQ('M|Carla, ¿cómo empezó tu interés por la fotografía?\nF|Mi abuelo era pescador en Chiloé y tenía una cámara vieja. De pequeña me pasaba las horas fotografiando los barcos del muelle.\nN|Pregunta: ¿Quién la inició en la fotografía?', ['Su abuelo.', 'Un profesor.', 'Su madre.']),
  LQ('M|¿Estudiaste fotografía?\nF|No, estudié Periodismo, pero nada más terminar la carrera me di cuenta de que prefería contar historias con imágenes.\nN|Pregunta: ¿Qué estudió Carla?', ['Periodismo.', 'Fotografía.', 'Bellas Artes.']),
  LQ('M|Tu último libro trata sobre las mujeres de la Patagonia.\nF|Sí, pasé dos años viajando por la región. Quería mostrar cómo viven en un lugar tan aislado.\nN|Pregunta: ¿Cuánto tiempo duró el proyecto?', ['Dos años.', 'Dos meses.', 'Doce años.']),
  LQ('M|¿Qué fue lo más difícil?\nF|El clima, sin duda. Por mucho que te prepares, el viento de la Patagonia siempre te sorprende.\nN|Pregunta: ¿Qué fue lo más difícil?', ['El clima.', 'Conseguir financiación.', 'Hablar con las mujeres.']),
  LQ('M|¿Usas fotografía digital?\nF|Para el trabajo diario, sí, pero para mis proyectos personales sigo usando carrete, como mi abuelo.\nN|Pregunta: ¿Qué usa para sus proyectos personales?', ['Cámara de carrete.', 'El teléfono móvil.', 'Solo cámara digital.']),
  LQ('M|¿Qué consejo darías a los jóvenes fotógrafos?\nF|Que no tengan prisa. Una buena foto exige paciencia y, sobre todo, respeto por las personas a las que fotografías.\nN|Pregunta: ¿Qué aconseja Carla?', ['Tener paciencia y respeto.', 'Comprar el mejor equipo.', 'Publicar mucho en redes.']),
  LQ('M|¿Próximo proyecto?\nF|Me gustaría volver a Chiloé y fotografiar a los últimos constructores de barcos de madera, antes de que desaparezca el oficio.\nN|Pregunta: ¿Qué quiere fotografiar Carla?', ['A los constructores de barcos de madera.', 'Las ciudades del norte.', 'Los glaciares de la Patagonia.']),
], listening=True)

L4 = PART('l-monologos', 'listening', 'Comprensión auditiva — Tarea 4', 'Des témoignages', 'Escuche a estas personas que hablan de un cambio en su vida y elija la opción correcta.', 6, [
  LQ('M|Me jubilé el año pasado y, aunque al principio me sentía perdido, ahora estudio guitarra y viajo con mi mujer.\nN|Pregunta: ¿Cómo se sintió al principio de la jubilación?', ['Perdido.', 'Muy feliz.', 'Enfermo.']),
  LQ('F|Cuando me quedé sin trabajo, decidí montar mi propia empresa de traducción. Fue lo mejor que me pudo pasar.\nN|Pregunta: ¿Qué hizo la mujer al perder su trabajo?', ['Creó su propia empresa.', 'Se fue al extranjero.', 'Volvió a estudiar.']),
  LQ('M|Dejé de fumar hace tres años. Si me hubieran dicho que sería tan fácil, lo habría hecho antes.\nN|Pregunta: ¿Qué opina ahora de haber dejado de fumar?', ['Que debería haberlo hecho antes.', 'Que fue muy difícil.', 'Que volverá a fumar.']),
  LQ('F|Me mudé a Buenos Aires por amor. La relación no funcionó, pero me quedé porque me enamoré de la ciudad.\nN|Pregunta: ¿Por qué se quedó en Buenos Aires?', ['Porque le encantó la ciudad.', 'Porque encontró trabajo.', 'Porque se casó.']),
  LQ('M|Tras el accidente, tuve que aprender a caminar de nuevo. Me volví más paciente y valoro mucho más las cosas pequeñas.\nN|Pregunta: ¿Cómo cambió el hombre?', ['Se volvió más paciente.', 'Se hizo rico.', 'Se puso muy nervioso.']),
  LQ('F|Adoptamos a nuestra hija con cinco años. Por mucho que lo hubiéramos preparado, nada nos preparó para tanta felicidad.\nN|Pregunta: ¿Qué cambio vivió la mujer?', ['La adopción de su hija.', 'Un cambio de casa.', 'Un nuevo trabajo.']),
  LQ('M|Vendí el coche y ahora voy a todas partes en bici. Ahorro dinero y, de paso, me he puesto en forma.\nN|Pregunta: ¿Qué ventajas ha encontrado?', ['Ahorra dinero y está más en forma.', 'Llega antes a todas partes.', 'Ya no tiene que trabajar.']),
], listening=True)

L5 = PART('l-radio', 'listening', 'Comprensión auditiva — Tarea 5', 'Un reportage radio', 'Escuche el reportaje sobre el tango y conteste a las preguntas.', 6, [
  LQ('N|El tango nació a finales del siglo XIX en los barrios del puerto de Buenos Aires y Montevideo, donde vivían inmigrantes de todo el mundo.\nN|Pregunta: ¿Dónde nació el tango?', ['En los barrios del puerto.', 'En el centro elegante de la ciudad.', 'En el campo.']),
  LQ('N|Al principio, la alta sociedad lo consideraba vulgar; sin embargo, tras triunfar en París hacia 1910, fue aceptado en los salones porteños.\nN|Pregunta: ¿Qué cambió la opinión de la alta sociedad?', ['Su éxito en París.', 'Una ley del gobierno.', 'La radio.']),
  LQ('N|El instrumento más característico del tango es el bandoneón, que llegó de Alemania en los barcos de los inmigrantes.\nN|Pregunta: ¿De dónde llegó el bandoneón?', ['De Alemania.', 'De Italia.', 'De España.']),
  LQ('N|En 2009, la UNESCO declaró el tango patrimonio cultural inmaterial de la humanidad, a propuesta de Argentina y Uruguay.\nN|Pregunta: ¿Qué ocurrió en 2009?', ['El tango fue declarado patrimonio de la humanidad.', 'Se prohibió el tango.', 'Se inventó el bandoneón.']),
  LQ('N|Hoy, en las milongas, que así se llaman los salones de baile, conviven jubilados y jóvenes de veinte años.\nN|Pregunta: ¿Qué es una milonga en este contexto?', ['Un salón de baile.', 'Un instrumento.', 'Un barrio.']),
  LQ('N|Los profesores insisten en que, para bailar bien, no basta con aprender los pasos: hay que escuchar la música y al compañero.\nN|Pregunta: ¿Qué aconsejan los profesores?', ['Escuchar la música y a la pareja.', 'Aprender solo los pasos.', 'Bailar siempre solo.']),
  LQ('N|Cada agosto, Buenos Aires celebra un festival y un mundial de tango que reúne a bailarines de más de cuarenta países.\nN|Pregunta: ¿Qué se celebra cada agosto?', ['Un festival y un mundial de tango.', 'El aniversario de la ciudad.', 'Un concurso de cocina.']),
], listening=True)

# ═════════════════════════ Expresión e interacción escritas ═════════════════════════
CARTA = 'Usted leyó en el periódico que el ayuntamiento va a cerrar la biblioteca de su barrio para construir un aparcamiento.'
W1 = PART('w-carta', 'writing', 'Expresión escrita — Tarea 1', 'Une lettre de protestation', 'Lea la situación y elija la opción mejor escrita.', 3, [
  RQ(['Estimado señor alcalde: me dirijo a usted para expresar mi desacuerdo con el cierre de la biblioteca del barrio. En primer lugar, es el único espacio cultural de la zona; en segundo lugar, cientos de estudiantes la utilizan cada día. Por consiguiente, le ruego que reconsidere su decisión. Atentamente, Ana Ruiz.',
      'Estimado señor alcalde: me dirijo a usted para expresar mi desacuerdo con el cierre. Es el único espacio cultural; cientos de estudiantes la utilizan. Le ruego que reconsidera su decisión. Atentamente.',
      'Hola, alcalde: no cierres la biblioteca, que es muy bonita. Un beso.',
      'Estimado señor alcalde: le felicito por cerrar la biblioteca, ya que nadie la usa. Atentamente, Ana Ruiz.'],
     None, f'{CARTA}\n★ Elija la carta que expone el problema, argumenta y hace una petición formal.'),
  RQ(['Le agradecería que tuviera en cuenta la opinión de los vecinos.', 'Le agradecería que tiene en cuenta la opinión de los vecinos.', 'Le agradeceré que tuviera en cuenta la opinión de los vecinos.', 'Le agradecería tener en cuenta de la opinión de los vecinos.'],
     None, f'{CARTA}\n★ Elija la frase correcta.'),
  RQ(['Si se cerrara la biblioteca, los jóvenes no tendrían dónde estudiar.', 'Si se cerraría la biblioteca, los jóvenes no tendrían dónde estudiar.', 'Si se cerrara la biblioteca, los jóvenes no tenían dónde estudiar.', 'Si se cierre la biblioteca, los jóvenes no tendrán dónde estudiar.'],
     None, f'{CARTA}\n★ Elija la frase correcta para presentar una consecuencia.'),
  RQ(['A pesar de que entiendo la falta de aparcamiento, creo que hay otras soluciones.', 'A pesar de entiendo la falta de aparcamiento, creo que hay otras soluciones.', 'Aunque entendiera la falta de aparcamiento ayer, creo que hay otras soluciones.', 'Por mucho que entiendo la falta de aparcamiento, creo que hay otras soluciones.'],
     None, f'{CARTA}\n★ Elija la frase correcta para hacer una concesión.'),
])

W2 = PART('w-articulo', 'writing', 'Expresión escrita — Tarea 2', 'Un article d’opinion', 'Lea la situación y elija el texto mejor escrito.', 2, [
  RQ(['Cada vez más personas trabajan desde casa. Si bien es cierto que el teletrabajo ofrece flexibilidad y ahorra tiempo de transporte, también puede provocar aislamiento. En mi opinión, la solución sería un modelo mixto, siempre que las empresas respeten el derecho a desconectar. En definitiva, el teletrabajo no es bueno ni malo: depende de cómo se organice.',
      'Cada vez más personas trabajan desde casa. Si bien es cierto que el teletrabajo ofrece flexibilidad, también puede provocar aislamiento. En mi opinión, la solución sería un modelo mixto, siempre que las empresas respetan el derecho a desconectar.',
      'Teletrabajo: flexibilidad, aislamiento, modelo mixto, desconectar.',
      'Cada vez más personas trabajan desde casa, lo cual es bueno porque es bueno, y también es malo porque es malo. En definitiva, no sé.'],
     None, '★ Situación: escriba un artículo de opinión sobre el teletrabajo (ventajas, inconvenientes, propuesta).'),
  RQ(['Hace cinco años tomé una decisión que cambió mi vida: dejé mi empleo en una gran empresa y me fui a vivir a Cuzco. Al principio echaba de menos a mi familia, pero poco a poco me adapté. Si no me hubiera atrevido, nunca habría descubierto mi verdadera vocación.',
      'Hace cinco años tomaba una decisión que cambió mi vida: dejaba mi empleo y me iba a vivir a Cuzco. Al principio eché de menos a mi familia. Si no me atrevería, nunca habría descubierto mi vocación.',
      'Cinco años. Decisión. Cuzco. Familia. Vocación.',
      'Hace cinco años tomaré una decisión: dejo mi empleo y me fui a Cuzco mañana.'],
     None, '★ Situación: escriba un relato sobre una decisión importante de su vida (qué pasó, cómo se sintió, qué habría pasado si…).'),
  RQ(['Las redes sociales han transformado la manera en que nos informamos. No obstante, cabe destacar que muchas noticias falsas se difunden con rapidez. Por consiguiente, es fundamental que aprendamos a contrastar las fuentes antes de compartir una información.',
      'Las redes sociales han transformado la manera en que nos informamos. No obstante, muchas noticias falsas se difunden. Por consiguiente, es fundamental que aprendemos a contrastar las fuentes.',
      'Redes sociales malas. Noticias falsas. Contrastar.',
      'Las redes sociales son geniales y nunca hay noticias falsas, por consiguiente no hay que contrastar nada.'],
     None, '★ Situación: escriba un texto para un foro sobre las redes sociales y la información.'),
])

PARTS = [R1, R2, R3, R4, L1, L2, L3, L4, L5, W1, W2]
rea = sum(p['count'] for p in PARTS if p['section'] == 'reading')
lis = sum(p['count'] for p in PARTS if p['section'] == 'listening')
wri = sum(p['count'] for p in PARTS if p['section'] == 'writing')
assert (rea, lis, wri) == (36, 30, 5), (rea, lis, wri)
bank = {
  'slug': 'deleb2',
  'level': 'DELEB2',
  'contentVersion': '2026.11.23',
  'notice': 'Questions rédigées par Koto Quest au format de l’examen officiel du DELE B2 (Instituto Cervantes : types d’épreuves, consignes en espagnol, notation sur 100 en deux groupes). L’expression écrite se fait par choix multiple et l’expression orale n’est pas évaluée : le groupe 2 est noté sur l’écoute. Ce ne sont pas des questions officielles.',
  'parts': PARTS,
}
json.dump(bank, open(os.path.join(ROOT, 'content/exams/deleb2.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
EN = {
  bank['notice']: 'Questions written by Koto Quest in the format of the official DELE B2 exam (Instituto Cervantes: question types, instructions in Spanish, scoring out of 100 in two groups). Written expression is multiple choice and speaking is not assessed: group 2 is marked on listening. They are not official questions.',
  'Un article': 'An article', 'Quatre parcours': 'Four life stories', 'Un texte à compléter': 'A text to complete', 'Grammaire en contexte': 'Grammar in context',
  'Conversations courtes': 'Short conversations', 'Un débat': 'A debate', 'Une interview': 'An interview', 'Des témoignages': 'Personal accounts', 'Un reportage radio': 'A radio report',
  'Une lettre de protestation': 'A letter of complaint', 'Un article d’opinion': 'An opinion piece',
}
P_DICT = os.path.join(ROOT, 'content/i18n/en/content.json')
d = json.load(open(P_DICT, encoding='utf-8'))
for k, v in EN.items():
    if k in d and d[k] != v:
        raise SystemExit(f'traduction existante différente : {k} → {d[k]} / {v}')
d.update(EN)
json.dump(d, open(P_DICT, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(f"DELE B2 : {sum(len(p['questions']) for p in PARTS)} questions en banque ; examen de {rea} + {lis} + {wri} questions")
