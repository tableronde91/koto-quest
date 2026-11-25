# Banque de questions de l'examen blanc DELE C2 (content/exams/delec2.json), au format de l'épreuve officielle
# de l'Instituto Cervantes : usage de la langue et compréhension écrite (6 tâches, 45 questions), compréhension auditive (4 tâches, 30 questions)
# et expression écrite intégrée (ici en format à choix : la meilleure synthèse et l'article d'opinion le mieux écrit).
# L'expression orale n'est pas évaluée. 190 minutes, notation sur 100, réussite avec au moins 30 points par groupe.
# Dans chaque question, le premier choix est la bonne réponse (l'ordre est mélangé à chaque examen).
# Usage : python3 scripts/delec2-exam.py
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



TEXTO = ('Los archivos y la memoria. Suele decirse que un pueblo sin memoria está condenado a repetir sus errores; menos se repara en que la memoria colectiva no es un don natural, sino una obra laboriosa que alguien debe custodiar. '
         'El Archivo General de Indias, creado en Sevilla en 1785 por orden de Carlos III, nació precisamente de esa convicción: reunir en un solo edificio los documentos dispersos sobre la administración de los territorios americanos. '
         'Hoy, la digitalización ha puesto buena parte de esos fondos al alcance de cualquier investigador, lo que ha democratizado el acceso al pasado como nunca antes. '
         'Ahora bien, sería ingenuo creer que digitalizar equivale a conservar. Los formatos electrónicos envejecen con una rapidez que haría palidecer al papel más frágil, y no son pocos los especialistas que advierten de una posible «edad oscura digital»: '
         'un futuro en el que nuestros descendientes no podrán leer lo que hoy producimos. Paradójicamente, un pergamino del siglo XVI puede resultar más perdurable que un correo electrónico de hace veinte años. '
         'De ahí que los archiveros insistan en que la tecnología, por sí sola, no garantiza nada: sin políticas públicas sostenidas y sin profesionales que la gestionen, la memoria digital es tan efímera como un mensaje escrito en la arena.')

COLUMNAS = ('A. «Defender la lengua no consiste en prohibir anglicismos, sino en enseñar a usarlos con criterio; el purismo, como todo fanatismo, acaba por empobrecer lo que pretende proteger.»\n'
            'B. «Nada envejece tan deprisa como un aparato de última generación: el teléfono que hoy deslumbra será mañana un trasto que nadie sabrá reparar. Mal que nos pese, vivimos en la cultura de lo desechable.»\n'
            'C. «Leer a los clásicos no es un ejercicio de nostalgia. Cervantes y Sor Juana siguen interpelándonos porque plantearon preguntas que ninguna época ha logrado responder del todo.»\n'
            'D. «Las ciudades se han llenado de ruido hasta el punto de que el silencio se ha convertido en un lujo. Hay quien paga por retirarse a un monasterio, y eso que el silencio, hasta hace poco, no costaba nada.»')

def CO(question, answer):
    return RP(COLUMNAS, question, [answer] + [n for n in ['A.', 'B.', 'C.', 'D.'] if n != answer])

def FR(passage, choices):
    return RP(passage, '¿Qué fragmento completa el hueco [ … ]?', choices)

def GR(sentence, choices):
    return RQ(choices, None, '★ ' + sentence)

T_LECT = 'Uso de la lengua y comprensión de lectura — Tarea '
T_AUD = 'Uso de la lengua y comprensión auditiva — Tarea '

# ═════════════════════════ Uso de la lengua y comprensión de lectura ═════════════════════════
R1 = PART('r-texto', 'reading', T_LECT + '1', 'Un texte d’analyse', 'Lea el texto y conteste a las preguntas.', 6, [
  RP(TEXTO, '¿Qué idea matiza el autor al comienzo del texto?', ['Que la memoria colectiva exige un trabajo de conservación.', 'Que los pueblos repiten siempre sus errores.', 'Que la memoria es un don natural.']),
  RP(TEXTO, '¿Con qué propósito se creó el Archivo General de Indias?', ['Reunir documentos dispersos sobre la administración americana.', 'Exponer obras de arte sevillanas.', 'Digitalizar documentos antiguos.']),
  RP(TEXTO, '¿Qué efecto ha tenido la digitalización, según el texto?', ['Ha facilitado el acceso a los fondos.', 'Ha destruido muchos documentos.', 'Ha reducido el número de investigadores.']),
  RP(TEXTO, '¿A qué se refiere la expresión «edad oscura digital»?', ['A un futuro en que no se podrán leer los documentos actuales.', 'A una época sin electricidad.', 'A un periodo de censura en internet.']),
  RP(TEXTO, '¿Por qué resulta paradójico el ejemplo del pergamino?', ['Porque un soporte antiguo puede durar más que uno moderno.', 'Porque el pergamino es más barato que un ordenador.', 'Porque nadie sabe leer los pergaminos.']),
  RP(TEXTO, '¿Qué sostienen los archiveros?', ['Que la tecnología no basta sin políticas ni profesionales.', 'Que hay que abandonar el papel.', 'Que la memoria digital es eterna.']),
  RP(TEXTO, '¿Cuál es la actitud del autor ante la digitalización?', ['Valora sus ventajas, pero advierte de sus límites.', 'La rechaza por completo.', 'La celebra sin reservas.']),
])

R2 = PART('r-fragmentos', 'reading', T_LECT + '2', 'Un texte à reconstituer', 'Lea el texto y elija el fragmento que falta.', 6, [
  FR('Sor Juana Inés de la Cruz ingresó en el convento de San Jerónimo en 1669. [ … ] Allí reunió una de las bibliotecas privadas más importantes de la Nueva España.', ['La vida religiosa le permitía dedicarse al estudio.', 'Nunca aprendió a leer ni a escribir.', 'Abandonó el convento al día siguiente.']),
  FR('Rubén Darío publicó Azul… en Valparaíso en 1888. [ … ] Por eso se le considera el gran renovador de la poesía en español.', ['El libro transformó la métrica y el lenguaje poético de su tiempo.', 'Era un tratado de geografía chilena.', 'Nadie llegó a leerlo nunca.']),
  FR('Ricardo Palma dirigió la Biblioteca Nacional del Perú tras la guerra del Pacífico. [ … ] Por ello se le apodó «el bibliotecario mendigo».', ['Como la biblioteca había sido saqueada, pidió libros a amigos e instituciones de todo el mundo.', 'Vendió todos los libros para pagar sus deudas.', 'Se negó a ocupar el cargo.']),
  FR('José Hernández publicó la primera parte del Martín Fierro en 1872 y la segunda, La vuelta, en 1879. [ … ] Hoy el poema se considera la obra cumbre de la literatura gauchesca.', ['El éxito fue inmediato entre la gente del campo, que lo recitaba de memoria.', 'Ambas partes se perdieron en un incendio.', 'El autor lo escribió en inglés.']),
  FR('Horacio Quiroga vivió durante años en la selva de Misiones. [ … ] De ahí que la naturaleza ocupe un lugar central en sus cuentos.', ['Allí conoció de cerca la belleza y los peligros del monte.', 'Nunca salió de su despacho en la ciudad.', 'Detestaba escribir sobre animales.']),
  FR('Unamuno llamó «nivola» a su obra Niebla. [ … ] Con ese término quería distanciarse de las convenciones de la novela realista.', ['Inventó la palabra para responder a quienes dijeran que su libro no respetaba las reglas del género.', 'Era el nombre de su pueblo natal.', 'Así se llamaba su editor.']),
  FR('El futuro de subjuntivo apenas se usa hoy en la lengua hablada. [ … ] Sobrevive, sin embargo, en los textos jurídicos y en algunos refranes.', ['Sus formas fueron sustituidas por el presente de subjuntivo o de indicativo.', 'Es el tiempo más frecuente en las conversaciones.', 'Nunca existió en español.']),
])

R3 = PART('r-columnas', 'reading', T_LECT + '3', 'Quatre chroniques', 'Lea las columnas y diga a cuál corresponde cada enunciado.', 8, [
  CO('¿Qué columna critica una actitud excesivamente protectora con el idioma?', 'A.'),
  CO('¿Qué columna denuncia que los objetos se quedan anticuados muy pronto?', 'B.'),
  CO('¿Qué columna defiende la vigencia de los autores antiguos?', 'C.'),
  CO('¿Qué columna señala que algo gratuito se ha vuelto caro?', 'D.'),
  CO('¿Qué columna compara una postura lingüística con el fanatismo?', 'A.'),
  CO('¿Qué columna reconoce, aunque a disgusto, un rasgo de nuestra época?', 'B.'),
  CO('¿Qué columna menciona a escritores concretos?', 'C.'),
  CO('¿Qué columna alude a una forma de retiro espiritual?', 'D.'),
  CO('¿Qué columna niega que leer a los clásicos sea mirar al pasado con añoranza?', 'C.'),
])

R4 = PART('r-lexico', 'reading', T_LECT + '4', 'Lexique en contexte', 'Lea las frases y elija la opción correcta.', 10, [
  GR('El ministro ＿ las acusaciones en una rueda de prensa.', ['desmintió', 'desmontó de', 'deshizo']),
  GR('Su argumentación carece de ＿: no aporta ningún dato.', ['fundamento', 'fondo de', 'fundación']),
  GR('Los nuevos hallazgos ponen en tela de ＿ la teoría tradicional.', ['juicio', 'duda', 'razón']),
  GR('Le costó lo ＿ convencer al tribunal.', ['suyo', 'mío', 'propio']),
  GR('Aceptó la propuesta a ＿, sin ningún entusiasmo.', ['regañadientes', 'carcajadas', 'borbotones']),
  GR('No te andes por las ＿ y dime qué ha pasado.', ['ramas', 'hojas', 'nubes']),
  GR('Con ese comentario solo has echado ＿ al fuego: ahora están aún más enfadados.', ['leña', 'agua', 'arena']),
  GR('La empresa anunció un «reajuste de ＿», es decir, despidos.', ['plantilla', 'personal de', 'oficina']),
  GR('Es un detalle ＿: no merece la pena discutir por eso.', ['nimio', 'inefable', 'lúgubre']),
  GR('Las ventas cayeron; la empresa lo llamó «crecimiento ＿».', ['negativo', 'positivo', 'inverso']),
  GR('Esa película es un ＿: grotesca y absurda de principio a fin.', ['esperpento', 'eufemismo', 'ingenio']),
])

R5 = PART('r-gramatica', 'reading', T_LECT + '5', 'Grammaire en contexte', 'Lea el texto y elija la opción correcta para cada hueco.', 10, [
  GR('Aun cuando me lo ＿ de rodillas, no cambiaré de opinión.', ['pidas', 'pides', 'pedirás']),
  GR('Si bien ＿ cierto que la obra es extensa, se lee con facilidad.', ['es', 'sea', 'fuera']),
  GR('＿ la cena, los invitados pasaron al salón.', ['Terminada', 'Terminado', 'Terminadas']),
  GR('No te imaginas lo ＿ que estaban las calles.', ['vacías', 'vacío', 'vacíos']),
  GR('Se me ＿ las gafas en el tren.', ['olvidaron', 'olvidó', 'olvidé']),
  GR('Fue en este café ＿ se conocieron los dos poetas.', ['donde', 'quien', 'cuando']),
  GR('Con lo ＿ que es, no entiendo cómo ha perdido.', ['hábil', 'habilidad', 'hábilmente']),
  GR('El que ＿ esta norma será sancionado (texto jurídico).', ['infringiere', 'infringiera', 'infringiría']),
  GR('De ＿ así, no llegaremos nunca a un acuerdo.', ['seguir', 'seguido', 'siguiendo']),
  GR('No lo haría así me lo ＿ el rey en persona.', ['pidiera', 'pide', 'pedirá']),
  GR('Es lógico que el proyecto ＿ críticos.', ['tenga', 'tiene', 'tendrá']),
  GR('¿＿ no sabías que la biblioteca cierra los lunes?', ['Acaso', 'Vaya si', 'Lo que']),
])

R6 = PART('r-correccion', 'reading', T_LECT + '6', 'La phrase correcte', 'Elija la frase correcta.', 5, [
  RQ(['Si me lo hubieras dicho, habría venido.', 'Si me lo habrías dicho, hubiera venido.', 'Si me lo dirías, habría venido.']),
  RQ(['A mi madre le dije la verdad.', 'A mi madre la dije la verdad.', 'A mi madre lo dije la verdad.']),
  RQ(['No es rojo, sino azul.', 'No es rojo, si no azul.', 'No es rojo, sino que azul.']),
  RQ(['Nadie previó la crisis.', 'Nadie prevenió la crisis.', 'Nadie preveyó la crisis.']),
  RQ(['¿Por qué no viniste?', '¿Porqué no viniste?', '¿Porque no viniste?']),
  RQ(['Me sorprende lo bien que canta.', 'Me sorprende lo bueno que canta.', 'Me sorprende lo buen que canta.']),
])

# ═════════════════════════ Uso de la lengua y comprensión auditiva ═════════════════════════
L1 = PART('l-conferencia', 'listening', T_AUD + '1', 'Une conférence', 'Escuche el fragmento de una conferencia sobre los libros en la América colonial y conteste a las preguntas.', 6, [
  LQ('F|La primera imprenta del continente americano se instaló en la Ciudad de México en 1539.\nN|Pregunta: ¿Dónde se instaló la primera imprenta de América?', ['En la Ciudad de México.', 'En Lima.', 'En Buenos Aires.']),
  LQ('F|Medio siglo después, en 1584, se imprimió el primer libro en Lima, la capital del virreinato del Perú.\nN|Pregunta: ¿Qué ocurrió en Lima en 1584?', ['Se imprimió el primer libro de la ciudad.', 'Se fundó la ciudad.', 'Se cerró la última imprenta.']),
  LQ('F|Aunque la Corona prohibía en teoría enviar novelas de caballerías a las Indias, los registros de los barcos demuestran que viajaban por cajas.\nN|Pregunta: ¿Qué demuestran los registros de los barcos?', ['Que las novelas prohibidas llegaban igualmente.', 'Que la prohibición se cumplía estrictamente.', 'Que no se enviaban libros a América.']),
  LQ('F|En 1605, el mismo año de su publicación, numerosos ejemplares de la primera parte del Quijote cruzaron el Atlántico.\nN|Pregunta: ¿Qué dice la conferenciante sobre el Quijote?', ['Que llegó a América el mismo año de su publicación.', 'Que se publicó por primera vez en México.', 'Que estuvo prohibido durante siglos.']),
  LQ('F|Los conventos desempeñaron un papel decisivo: en sus bibliotecas se formaron autoras como Sor Juana Inés de la Cruz.\nN|Pregunta: ¿Qué papel tuvieron los conventos?', ['Fueron centros de formación y lectura.', 'Prohibieron toda lectura.', 'Solo guardaban libros de cuentas.']),
  LQ('F|Leer en voz alta era entonces una práctica social: un solo lector podía transmitir un libro a decenas de oyentes que no sabían leer.\nN|Pregunta: ¿Por qué era importante la lectura en voz alta?', ['Permitía que quienes no sabían leer conocieran los libros.', 'Estaba prohibida en las plazas.', 'Solo se practicaba en las universidades.']),
  LQ('F|En resumidas cuentas, el libro llegó a América con los conquistadores, pero fueron los lectores americanos quienes lo hicieron suyo.\nN|Pregunta: ¿Cuál es la conclusión de la conferenciante?', ['Que los lectores americanos se apropiaron del libro.', 'Que el libro nunca interesó en América.', 'Que solo los conquistadores leían.']),
], listening=True)

L2 = PART('l-implicito', 'listening', T_AUD + '2', 'Le sens implicite', 'Escuche las conversaciones y elija la interpretación correcta.', 8, [
  LQ('M|¿Qué tal el nuevo jefe?\nF|Encantador. Sobre todo cuando no habla.\nN|Pregunta: ¿Qué opina la mujer del nuevo jefe?', ['Que no le cae bien.', 'Que es muy simpático.', 'Que no lo conoce todavía.']),
  LQ('F|¿Le has dicho a tu hermano que no le han dado el puesto?\nM|Se lo he dado a entender. A buen entendedor…\nN|Pregunta: ¿Qué ha hecho el hombre?', ['Se lo ha insinuado sin decirlo claramente.', 'Se lo ha explicado con todo detalle.', 'Le ha dicho que sí le han dado el puesto.']),
  LQ('M|La empresa habla de un «reajuste de plantilla».\nF|Ya. Llamémoslo por su nombre: van a echar a la mitad.\nN|Pregunta: ¿Qué denuncia la mujer?', ['El uso de un eufemismo.', 'Una subida de sueldos.', 'Un error de traducción.']),
  LQ('M|¿Vienes a la cena de esta noche?\nF|Mal que me pese, tengo que terminar este artículo.\nN|Pregunta: ¿Qué responde la mujer?', ['Que no puede ir, aunque le gustaría.', 'Que irá encantada.', 'Que no le apetece nada ir.']),
  LQ('M|¿Qué te pareció la novela?\nF|Se deja leer.\nN|Pregunta: ¿Qué opina la mujer?', ['Que es correcta, sin más.', 'Que es una obra maestra.', 'Que es ilegible.']),
  LQ('F|Llevo tres horas con este formulario.\nM|¡Vaya si es complicado! A mí me pasó lo mismo.\nN|Pregunta: ¿Qué expresa el hombre?', ['Que está de acuerdo en que es muy complicado.', 'Que no le parece complicado.', 'Que nunca ha rellenado el formulario.']),
  LQ('M|¿Al final le prestaste dinero a Pablo?\nF|Sí, y ya ves cómo me lo ha agradecido: cría cuervos…\nN|Pregunta: ¿Qué da a entender la mujer?', ['Que Pablo ha sido un ingrato con ella.', 'Que Pablo le ha devuelto el dinero con intereses.', 'Que Pablo cría animales.']),
  LQ('F|El ponente habló dos horas sin decir nada.\nM|Ya. Se anduvo por las ramas todo el rato.\nN|Pregunta: ¿Qué opinan del ponente?', ['Que no fue al grano.', 'Que fue muy concreto.', 'Que habló de botánica.']),
  LQ('M|¿Has visto el nuevo museo?\nF|Sí. Digamos que el edificio es más interesante que lo que hay dentro.\nN|Pregunta: ¿Qué opina la mujer de la colección?', ['Que le decepcionó.', 'Que es extraordinaria.', 'Que todavía no está abierta.']),
], listening=True)

L3 = PART('l-entrevista', 'listening', T_AUD + '3', 'Une interview', 'Escuche la entrevista a una restauradora de manuscritos y conteste a las preguntas.', 8, [
  LQ('M|Lucía, ¿en qué consiste exactamente su trabajo?\nF|Restauro manuscritos antiguos: limpio, consolido el papel y, sobre todo, intento intervenir lo menos posible.\nN|Pregunta: ¿Cuál es el principio de su trabajo?', ['Intervenir lo mínimo.', 'Reescribir los textos dañados.', 'Sustituir el papel antiguo.']),
  LQ('M|¿Cuál es el peor enemigo de un manuscrito?\nF|La humedad, sin duda; mucho más que el paso del tiempo. Un documento bien guardado puede durar siglos.\nN|Pregunta: ¿Cuál es el peor enemigo de un manuscrito?', ['La humedad.', 'El paso del tiempo.', 'La luz eléctrica.']),
  LQ('M|¿Y los ratones?\nF|Existen, como en la tradición de fray Martín, pero hoy los controlamos bien. Los insectos son mucho más traicioneros.\nN|Pregunta: ¿Qué dice sobre los animales?', ['Que los insectos son más peligrosos que los ratones.', 'Que los ratones destruyen la mayoría de los libros.', 'Que no hay ningún animal en los archivos.']),
  LQ('M|¿Recuerda algún hallazgo especial?\nF|Una vez, dentro de la encuadernación de un libro del siglo XVII, apareció una carta de amor doblada en ocho.\nN|Pregunta: ¿Qué encontró?', ['Una carta escondida en la encuadernación.', 'Un mapa del tesoro.', 'Una moneda de oro.']),
  LQ('M|¿La digitalización no hace innecesaria la restauración?\nF|En absoluto. La copia digital protege el original del uso, pero no lo salva de deteriorarse.\nN|Pregunta: ¿Qué opina de la digitalización?', ['Que complementa la restauración, pero no la sustituye.', 'Que hace inútil la restauración.', 'Que daña los originales.']),
  LQ('M|¿Qué formación hace falta?\nF|Química, historia del arte y, mal que les pese a algunos, mucha paciencia. Un solo folio puede llevar semanas.\nN|Pregunta: ¿Qué cualidad destaca?', ['La paciencia.', 'La rapidez.', 'La fuerza física.']),
  LQ('M|¿Se siente a veces como una detective?\nF|Más bien como una médica: diagnostico, trato y, si hace falta, dejo al paciente en reposo.\nN|Pregunta: ¿Con qué profesión compara su trabajo?', ['Con la de una médica.', 'Con la de una detective.', 'Con la de una escritora.']),
  LQ('M|¿Qué le diría a quien piensa que su trabajo es inútil?\nF|Que un pueblo que no cuida sus papeles acaba sin saber quién es.\nN|Pregunta: ¿Qué defiende la restauradora?', ['La relación entre los documentos y la identidad.', 'La destrucción de los papeles viejos.', 'La venta de manuscritos.']),
  LQ('M|¿En qué trabaja ahora?\nF|En un códice del siglo XV muy dañado por un incendio. Va para largo.\nN|Pregunta: ¿Qué dice de su proyecto actual?', ['Que llevará mucho tiempo.', 'Que lo terminará mañana.', 'Que lo ha abandonado.']),
], listening=True)

L4 = PART('l-tertulia', 'listening', T_AUD + '4', 'Un débat radio', 'Escuche la tertulia sobre las versiones adaptadas de los clásicos y elija la opción correcta.', 8, [
  LQ('N|Hoy debatimos si conviene leer a los clásicos en versiones adaptadas.\nM|Yo lo defiendo: más vale leer un Quijote adaptado que no leer ninguno.\nN|Pregunta: ¿Qué defiende el tertuliano?', ['Las adaptaciones como puerta de entrada.', 'La prohibición de las adaptaciones.', 'Leer solo textos originales.']),
  LQ('F|Hasta cierto punto te doy la razón, pero una adaptación que lo simplifica todo traiciona al autor.\nN|Pregunta: ¿Cuál es la postura de la tertuliana?', ['Está de acuerdo solo en parte.', 'Está totalmente de acuerdo.', 'No tiene opinión.']),
  LQ('M|No digo que se sustituya el original, sino que se use como primer paso.\nN|Pregunta: ¿Qué precisa el tertuliano?', ['Que la adaptación es solo un primer paso.', 'Que el original debe desaparecer.', 'Que los jóvenes no deben leer.']),
  LQ('F|El problema es que muchos se quedan en ese primer paso y creen haber leído a Cervantes.\nN|Pregunta: ¿Qué objeción plantea la tertuliana?', ['Que muchos lectores no pasan al original.', 'Que las adaptaciones son caras.', 'Que Cervantes es demasiado fácil.']),
  LQ('M|Cabría objetar que lo mismo pasa con las traducciones, y nadie propone prohibirlas.\nN|Pregunta: ¿Con qué compara las adaptaciones?', ['Con las traducciones.', 'Con las películas.', 'Con los resúmenes escolares.']),
  LQ('F|Una traducción busca ser fiel; una adaptación, por definición, recorta. No es lo mismo.\nN|Pregunta: ¿Qué diferencia establece?', ['La traducción busca la fidelidad y la adaptación recorta.', 'Ambas son exactamente iguales.', 'La adaptación es más fiel que la traducción.']),
  LQ('M|En suma, se trata de acompañar al lector, no de darle gato por liebre.\nN|Pregunta: ¿Qué quiere decir «dar gato por liebre»?', ['Engañar dando algo de menor calidad.', 'Regalar un animal.', 'Explicar algo con claridad.']),
  LQ('F|En eso coincidimos: el papel del profesor es clave para que la adaptación lleve al original.\nN|Pregunta: ¿En qué están de acuerdo?', ['En la importancia del profesor.', 'En prohibir los clásicos.', 'En que la adaptación basta.']),
  LQ('N|Para terminar, ¿un clásico para empezar?\nF|Las Tradiciones peruanas de Palma: breves, irónicas y llenas de vida.\nN|Pregunta: ¿Qué recomienda la tertuliana?', ['Las Tradiciones peruanas.', 'El Quijote adaptado.', 'Un manual de gramática.']),
], listening=True)

# ═════════════════════════ Destrezas integradas: comprensión y expresión escritas ═════════════════════════
ART = 'Usted ha leído un artículo sobre la conservación de los archivos. Según el autor, la digitalización ha democratizado el acceso al pasado, pero los formatos electrónicos envejecen deprisa; sin políticas públicas y sin profesionales, la memoria digital es efímera.'
W1 = PART('w-sintesis', 'writing', 'Destrezas integradas — Tarea 1', 'Une synthèse', 'Lea la situación y elija la opción mejor redactada.', 3, [
  RQ(['El autor sostiene que, si bien la digitalización ha democratizado el acceso a los fondos, no garantiza por sí sola su conservación; de ahí que reclame políticas públicas sostenidas y profesionales cualificados.',
      'El autor dice que digitalizar está bien pero que no dura y que hace falta gente.',
      'El autor sostiene que la digitalización ha destruido los archivos y que conviene volver al pergamino.',
      'Archivos, digitalización, memoria, políticas.'],
     None, f'{ART}\n★ Elija la síntesis más completa, fiel y formal.'),
  RQ(['Cabría objetar que no todos los archivos disponen de recursos para digitalizar sus fondos.', 'Cabría objetar de que no todos los archivos disponen de recursos para digitalizar sus fondos.', 'Cabría a objetar que no todos los archivos disponen de recursos para digitalizar sus fondos.', 'Cabría objetar que no todos los archivos disponen recursos para digitalizar sus fondos.'],
     None, f'{ART}\n★ Elija la frase correcta.'),
  RQ(['Dicho de otro modo, lo digital puede desaparecer con suma facilidad.', 'Dicho de otro modo, lo digital es eterno.', 'Dicho de otro modo, hay que escribir en la playa.', 'Dicho de otro modo, la arena es un soporte digital.'],
     None, f'{ART}\n★ Elija la reformulación más fiel de: «La memoria digital es tan efímera como un mensaje escrito en la arena».'),
  RQ(['ahora bien', 'por consiguiente', 'es decir', 'de ahí que'],
     None, f'{ART}\n★ Elija el conector adecuado: «La digitalización facilita el acceso; ＿, plantea nuevos riesgos de conservación».'),
])

W2 = PART('w-articulo', 'writing', 'Destrezas integradas — Tarea 2', 'Un article d’opinion', 'Lea la situación y elija el texto mejor escrito.', 2, [
  RQ(['Nadie pone en tela de juicio que el Quijote intimida a muchos lectores jóvenes. Ahora bien, de ahí a sustituirlo por versiones que lo reducen a una sucesión de anécdotas media un abismo. Las adaptaciones pueden ser, en el mejor de los casos, una puerta de entrada; en el peor, una coartada para no cruzarla nunca. Si bien no conviene demonizarlas, sí cabe exigir que inviten expresamente a leer el original.',
      'Nadie pone en tela de juicio que el Quijote intimida a muchos lectores. Ahora bien, de ahí a sustituirlo media abismo. Las adaptaciones pueden ser una puerta. Si bien no conviene demonizarlas, sí cabe exigir de que inviten a leer el original.',
      'Los clásicos son aburridos y las adaptaciones también. Mejor ver la película.',
      'Las adaptaciones son lo mejor que existe porque son buenas y todo el mundo debería leerlas siempre sin excepción porque sí.'],
     None, '★ Situación: escriba un artículo de opinión para un periódico sobre las versiones adaptadas de los clásicos.'),
  RQ(['El silencio se ha convertido en un bien de lujo. Quien vive en el centro de una gran ciudad lo sabe: el estruendo del tráfico, las obras y las terrazas no da tregua. Cabría objetar que el ruido es el precio de una ciudad viva; sin embargo, numerosos estudios lo relacionan con el estrés y los trastornos del sueño. De ahí que urja replantear el urbanismo: no se trata de apagar la ciudad, sino de devolverle, siquiera a ratos, el derecho al silencio.',
      'El silencio se ha convertido en un bien de lujo. El estruendo del tráfico no da tregua. Cabría objetar que el ruido es el precio; sin embargo, numerosos estudios lo relacionan con el estrés. De ahí que urge replantear el urbanismo.',
      'Hay mucho ruido. Molesta. Hay que hacer algo ya.',
      'El ruido no existe en las ciudades modernas; por lo tanto, es un problema muy grave que afecta a todos.'],
     None, '★ Situación: escriba un artículo de opinión sobre el ruido en las ciudades.'),
  RQ(['Pocas polémicas resultan tan recurrentes como la de los anglicismos. Los puristas ven en cada préstamo una amenaza; los más permisivos, una prueba de vitalidad. A mi juicio, la cuestión no estriba en prohibir, sino en discernir: hay préstamos que colman un vacío y otros que desplazan sin motivo palabras perfectamente vigentes. En definitiva, conviene usar el idioma con criterio, no con miedo.',
      'Pocas polémicas resultan tan recurrentes como la de los anglicismos. A mi juicio, la cuestión no estriba prohibir, sino en discernir. En definitiva, conviene que usamos el idioma con criterio.',
      'Los anglicismos me gustan. Son modernos. Y ya está.',
      'Hay que prohibir todas las palabras de origen extranjero, incluidas las que vienen del árabe, como «aceite» o «almohada».'],
     None, '★ Situación: escriba un artículo de opinión sobre el uso de los anglicismos.'),
])

PARTS = [R1, R2, R3, R4, R5, R6, L1, L2, L3, L4, W1, W2]
rea = sum(p['count'] for p in PARTS if p['section'] == 'reading')
lis = sum(p['count'] for p in PARTS if p['section'] == 'listening')
wri = sum(p['count'] for p in PARTS if p['section'] == 'writing')
assert (rea, lis, wri) == (45, 30, 5), (rea, lis, wri)
bank = {
  'slug': 'delec2',
  'level': 'DELEC2',
  'contentVersion': '2026.11.24',
  'notice': 'Questions rédigées par Koto Quest au format de l’examen officiel du DELE C2 (Instituto Cervantes : épreuves d’usage de la langue et de compréhension, consignes en espagnol, notation sur 100 en deux groupes). L’expression écrite intégrée se fait par choix multiple et l’expression orale n’est pas évaluée : le groupe 2 est noté sur l’écoute. Ce ne sont pas des questions officielles.',
  'parts': PARTS,
}
json.dump(bank, open(os.path.join(ROOT, 'content/exams/delec2.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
EN = {
  bank['notice']: 'Questions written by Koto Quest in the format of the official DELE C2 exam (Instituto Cervantes: use-of-language and comprehension tests, instructions in Spanish, scoring out of 100 in two groups). Integrated written expression is multiple choice and speaking is not assessed: group 2 is marked on listening. They are not official questions.',
  'Un texte d’analyse': 'An analytical text', 'Un texte à reconstituer': 'A text to reconstruct', 'Quatre chroniques': 'Four columns',
  'Lexique en contexte': 'Vocabulary in context', 'Grammaire en contexte': 'Grammar in context', 'La phrase correcte': 'The correct sentence',
  'Une conférence': 'A lecture', 'Le sens implicite': 'Implied meaning', 'Une interview': 'An interview', 'Un débat radio': 'A radio debate',
  'Une synthèse': 'A summary', 'Un article d’opinion': 'An opinion piece',
}
P_DICT = os.path.join(ROOT, 'content/i18n/en/content.json')
d = json.load(open(P_DICT, encoding='utf-8'))
for k, v in EN.items():
    if k in d and d[k] != v:
        raise SystemExit(f'traduction existante différente : {k} → {d[k]} / {v}')
d.update(EN)
json.dump(d, open(P_DICT, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(f"DELE C2 : {sum(len(p['questions']) for p in PARTS)} questions en banque ; examen de {rea} + {lis} + {wri} questions")
