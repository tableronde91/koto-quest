# Banque de questions de l'examen blanc DELE B1 (content/exams/deleb1.json), au format de l'épreuve officielle
# de l'Instituto Cervantes : compréhension écrite (5 tâches, 30 questions), compréhension auditive (5 tâches, 30 questions)
# et expression écrite (ici en format à choix : choisir la meilleure réponse à un message et le texte le mieux écrit).
# L'expression orale n'est pas évaluée. 130 minutes, notation sur 100, réussite avec au moins 30 points par groupe.
# Dans chaque question, le premier choix est la bonne réponse (l'ordre est mélangé à chaque examen).
# Usage : python3 scripts/deleb1-exam.py
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


ANUNCIOS = ('A. Escuela Sabores: cursos de cocina española los sábados y domingos por la mañana. Grupos pequeños.\n'
            'B. Club Montaña Norte: rutas de senderismo cada domingo; salida en autobús desde la estación.\n'
            'C. Academia Lenguas Vivas: clases de inglés y francés por la tarde, de lunes a jueves.\n'
            'D. Taller Manos: cerámica y pintura para niños de 6 a 12 años, los miércoles.\n'
            'E. Gimnasio Agua Viva: piscina climatizada abierta hasta las 23:00, también los festivos.\n'
            'F. Asociación Vecinos Unidos: buscamos voluntarios para enseñar a usar internet a personas mayores.\n'
            'G. Cine Club Lumière: películas en versión original con debate después de la sesión, los viernes.')

def AN(person, answer, distractors):
    return RP(ANUNCIOS, person + ' ¿Qué anuncio le conviene?', [answer] + distractors)

ARTICULO = ('Hace diez años, Clara Vidal dejó su trabajo en un banco de Madrid y se fue a vivir a un pueblo de Teruel de solo cuarenta habitantes. '
            '«Estaba cansada del tráfico, del ruido y de llegar a casa a las nueve de la noche», explica. Al principio, sus amigos pensaban que volvería a la ciudad en pocos meses. '
            'Sin embargo, Clara abrió una pequeña panadería con su pareja y hoy vende pan a cinco pueblos de la comarca. '
            '«Lo más difícil fue el primer invierno: hacía mucho frío y casi no había clientes», recuerda. '
            'Gracias a internet, ahora también recibe pedidos de toda España. Además, su llegada animó a otras dos familias jóvenes a instalarse en el pueblo, y el ayuntamiento ha podido reabrir la escuela, que estaba cerrada desde 2009. '
            'Clara no se arrepiente: «Gano menos dinero, pero tengo tiempo para vivir». Aun así, reconoce que la vida rural no es para todo el mundo: «Si no te gusta la tranquilidad, aquí te aburrirás».')

TESTIMONIOS = ('Ana: Hice el Camino de Santiago sola a los sesenta años. Mis hijos tenían miedo, pero nunca me sentí en peligro: siempre había alguien dispuesto a ayudar. Lo que más me costó fue la lluvia en Galicia.\n'
               'Luis: Yo lo hice en bicicleta con dos amigos. Fuimos muy rápido, quizás demasiado: no tuvimos tiempo de visitar los pueblos. Si lo repito, iré a pie y con más calma.\n'
               'Carmen: Para mí fue un viaje espiritual. Caminé en invierno, cuando hay pocos peregrinos, y muchos albergues estaban cerrados. Aun así, el silencio de la Meseta me cambió la vida.')

def TE(question, answer):
    return RP(TESTIMONIOS, question, [answer] + [n for n in ['Ana.', 'Luis.', 'Carmen.'] if n != answer])

def FR(passage, choices):
    return RP(passage, '¿Qué fragmento completa el hueco [ … ]?', choices)

def GR(sentence, choices):
    return RQ(choices, None, '★ ' + sentence)

# ═════════════════════════ Comprensión de lectura ═════════════════════════
R1 = PART('r-anuncios', 'reading', 'Comprensión de lectura — Tarea 1', 'Annonces et besoins', 'Lea los anuncios y decida cuál conviene a cada persona.', 6, [
  AN('Julia trabaja toda la semana y quiere aprender a hacer paella el fin de semana.', 'A.', ['C.', 'G.']),
  AN('Andrés quiere conocer gente y caminar por la montaña los domingos.', 'B.', ['E.', 'F.']),
  AN('Elena necesita mejorar su inglés, pero solo puede por las tardes entre semana.', 'C.', ['A.', 'G.']),
  AN('Pedro busca una actividad creativa para su hija de ocho años.', 'D.', ['A.', 'B.']),
  AN('Marisa termina de trabajar a las nueve de la noche y quiere nadar.', 'E.', ['B.', 'D.']),
  AN('Jorge está jubilado, sabe mucho de informática y quiere ayudar a los demás.', 'F.', ['C.', 'E.']),
  AN('Sofía estudia cine y le gusta hablar de las películas que ve.', 'G.', ['C.', 'D.']),
])

R2 = PART('r-texto', 'reading', 'Comprensión de lectura — Tarea 2', 'Un article', 'Lea el texto y conteste a las preguntas.', 6, [
  RP(ARTICULO, '¿Por qué dejó Clara su trabajo en Madrid?', ['Porque estaba cansada del ritmo de la ciudad.', 'Porque perdió su trabajo en el banco.', 'Porque su familia vivía en Teruel.']),
  RP(ARTICULO, '¿Qué pensaban sus amigos?', ['Que pronto volvería a la ciudad.', 'Que tenía una idea excelente.', 'Que debía abrir una panadería.']),
  RP(ARTICULO, '¿Qué fue lo más difícil para Clara?', ['El primer invierno, por el frío y la falta de clientes.', 'Aprender a hacer pan.', 'Encontrar una casa en el pueblo.']),
  RP(ARTICULO, '¿Qué papel tiene internet en su negocio?', ['Le permite recibir pedidos de toda España.', 'Solo lo usa para hablar con sus amigos.', 'No tiene conexión en el pueblo.']),
  RP(ARTICULO, '¿Qué consecuencia tuvo su llegada al pueblo?', ['Se pudo volver a abrir la escuela.', 'Cerró la escuela del pueblo.', 'El pueblo perdió habitantes.']),
  RP(ARTICULO, 'Según Clara, la vida rural…', ['no conviene a quien no le gusta la tranquilidad.', 'es perfecta para todo el mundo.', 'permite ganar más dinero.']),
  RP(ARTICULO, '¿Con quién abrió Clara la panadería?', ['Con su pareja.', 'Con sus amigos de Madrid.', 'Con otras dos familias.']),
])

R3 = PART('r-testimonios', 'reading', 'Comprensión de lectura — Tarea 3', 'Trois témoignages', 'Lea los textos y diga a qué persona corresponde cada afirmación.', 6, [
  TE('¿Quién viajó acompañado y en poco tiempo?', 'Luis.'),
  TE('¿Quién dice que su familia estaba preocupada?', 'Ana.'),
  TE('¿Quién encontró pocos sitios abiertos para dormir?', 'Carmen.'),
  TE('¿Quién tuvo problemas con el tiempo en Galicia?', 'Ana.'),
  TE('¿Quién cambiaría su forma de hacer el Camino?', 'Luis.'),
  TE('¿Quién habla de un cambio interior?', 'Carmen.'),
  TE('¿Quién no pudo conocer bien los pueblos?', 'Luis.'),
])

R4 = PART('r-fragmentos', 'reading', 'Comprensión de lectura — Tarea 4', 'Un texte à compléter', 'Lea el texto y elija el fragmento que falta.', 6, [
  FR('Cada año más de 400.000 personas llegan a Santiago. [ … ] Por eso, el ayuntamiento ha creado nuevas zonas para descansar.', ['La mayoría hace la última etapa en verano, cuando la ciudad está llena.', 'Santiago tiene una universidad muy antigua.', 'Nunca llueve en Galicia en invierno.']),
  FR('Antes de salir, conviene preparar bien la mochila. [ … ] Un consejo: no debe pesar más del diez por ciento de tu peso.', ['Muchos peregrinos llevan demasiadas cosas y se cansan pronto.', 'Las mochilas rojas son las más bonitas.', 'Los albergues cierran a las diez.']),
  FR('Los albergues públicos son baratos y no se pueden reservar. [ … ] Si llegas tarde, es posible que no encuentres cama.', ['Las camas se dan por orden de llegada.', 'Todos tienen piscina y restaurante.', 'Solo aceptan grupos de más de diez personas.']),
  FR('La credencial es el pasaporte del peregrino. [ … ] Al final, con ella se pide la Compostela en la Oficina del Peregrino.', ['En cada etapa hay que sellarla en albergues, iglesias o bares.', 'Se compra en el aeropuerto de Madrid.', 'Sirve para viajar gratis en tren.']),
  FR('El Camino no es solo para deportistas. [ … ] Lo importante es caminar a tu ritmo y escuchar a tu cuerpo.', ['Lo hacen personas de todas las edades y condiciones físicas.', 'Hay que correr al menos treinta kilómetros al día.', 'Está prohibido para mayores de sesenta años.']),
  FR('En Galicia el tiempo cambia muy rápido. [ … ] Por eso, el chubasquero es imprescindible en la mochila.', ['Por la mañana puede hacer sol y por la tarde llover mucho.', 'Allí hace calor todo el año.', 'Allí nunca hay niebla.']),
  FR('Muchos peregrinos continúan hasta Fisterra después de Santiago. [ … ] Allí, frente al océano, termina simbólicamente el viaje.', ['Son tres o cuatro días más de camino hasta la costa.', 'Fisterra está en el centro de Madrid.', 'Para ir allí hay que coger un avión.']),
])

R5 = PART('r-gramatica', 'reading', 'Comprensión de lectura — Tarea 5', 'Grammaire en contexte', 'Lea el mensaje y elija la opción correcta para cada hueco.', 6, [
  GR('Querida Inés: te escribo desde León. Llevo dos semanas ＿ y estoy muy contenta.', ['caminando', 'caminar', 'caminado']),
  GR('Ayer, cuando llegué al albergue, mis amigos ya ＿ la cena.', ['habían preparado', 'prepararán', 'preparen']),
  GR('Espero que tú ＿ venir a Santiago para la llegada.', ['puedas', 'puedes', 'podrás']),
  GR('Cuando ＿ a la catedral, te enviaré una foto.', ['llegue', 'llegaré', 'llego']),
  GR('No creo que ＿ problemas con el tiempo: dicen que hará sol.', ['tengamos', 'tenemos', 'tendremos']),
  GR('Si ＿ más días libres, seguiría hasta Fisterra.', ['tuviera', 'tengo', 'tendría']),
  GR('Te recomiendo que ＿ ropa cómoda si vienes.', ['traigas', 'traes', 'traerás']),
  GR('Un abrazo muy fuerte y hasta ＿.', ['pronto', 'pronta', 'prontamente']),
])

# ═════════════════════════ Comprensión auditiva ═════════════════════════
L1 = PART('l-mensajes', 'listening', 'Comprensión auditiva — Tarea 1', 'Messages courts', 'Escuche los mensajes y elija la opción correcta.', 6, [
  LQ('F|Hola, Pablo, soy Lucía. Al final no puedo ir a la cena del viernes porque me han cambiado el turno en el hospital. ¿Quedamos el sábado para comer?\nN|Pregunta: ¿Qué propone Lucía?', ['Comer juntos el sábado.', 'Cenar el viernes en el hospital.', 'Cambiar de trabajo.']),
  LQ('M|Le llamamos de la clínica dental. Su cita del martes se ha retrasado al jueves a la misma hora. Si no le viene bien, llámenos.\nN|Pregunta: ¿Qué ha cambiado?', ['El día de la cita.', 'La hora de la cita.', 'El nombre del dentista.']),
  LQ('F|Mamá, he perdido el autobús de las seis. Cojo el de las siete y llego a casa para cenar, no te preocupes.\nN|Pregunta: ¿Por qué llegará tarde la hija?', ['Porque perdió el autobús.', 'Porque tiene que trabajar.', 'Porque va a cenar fuera.']),
  LQ('M|Buenos días, soy el técnico de la lavadora. Hoy no puedo ir a su casa: se me ha estropeado la furgoneta. Iré mañana por la mañana, si le parece bien.\nN|Pregunta: ¿Cuándo irá el técnico?', ['Mañana por la mañana.', 'Hoy por la tarde.', 'La semana que viene.']),
  LQ('F|Hola, soy Marta, del curso de fotografía. Te recuerdo que mañana salimos a las ocho desde la plaza y que tienes que traer la cámara cargada.\nN|Pregunta: ¿Qué tiene que llevar el alumno?', ['La cámara con la batería cargada.', 'La comida.', 'Un mapa de la ciudad.']),
  LQ('M|Oye, Clara, ¿me puedes devolver el libro que te presté? Lo necesito para el examen del lunes.\nN|Pregunta: ¿Para qué necesita el libro?', ['Para estudiar para un examen.', 'Para regalárselo a alguien.', 'Para un viaje.']),
  LQ('F|Atención: debido a la huelga, mañana no habrá clases en el instituto. Las actividades se recuperarán el sábado.\nN|Pregunta: ¿Qué pasará mañana?', ['No habrá clases.', 'Las clases serán el domingo.', 'Habrá un examen.']),
], listening=True)

L2 = PART('l-monologo', 'listening', 'Comprensión auditiva — Tarea 2', 'Un récit', 'Escuche a Javier, que habla de su primer trabajo, y conteste a las preguntas.', 6, [
  LQ('M|Mi primer trabajo fue en un hotel de la costa, cuando tenía diecisiete años. Trabajaba en verano para pagarme los estudios.\nN|Pregunta: ¿Para qué trabajaba Javier?', ['Para pagar sus estudios.', 'Para comprarse un coche.', 'Para ayudar a sus padres.']),
  LQ('M|Al principio fregaba los platos en la cocina. Era muy duro: empezaba a las siete de la mañana y terminaba a las cuatro.\nN|Pregunta: ¿Qué hacía al principio?', ['Fregaba los platos.', 'Atendía a los clientes.', 'Cocinaba.']),
  LQ('M|Después de un mes, el jefe me pidió que trabajara en la recepción, porque hablaba inglés y francés.\nN|Pregunta: ¿Por qué cambió de puesto?', ['Porque hablaba idiomas.', 'Porque estaba enfermo.', 'Porque no le gustaba la cocina.']),
  LQ('M|En la recepción conocí a gente de todo el mundo. Me encantaba ayudar a los turistas y recomendarles restaurantes.\nN|Pregunta: ¿Qué le gustaba de la recepción?', ['Ayudar a los turistas.', 'Hacer las camas.', 'Trabajar de noche.']),
  LQ('M|Aquel verano decidí estudiar turismo. Hoy dirijo un pequeño hotel en Asturias.\nN|Pregunta: ¿A qué se dedica hoy Javier?', ['Dirige un hotel.', 'Es cocinero.', 'Es profesor de idiomas.']),
  LQ('M|A los jóvenes les diría que no tengan miedo de empezar desde abajo: se aprende muchísimo.\nN|Pregunta: ¿Qué consejo da Javier?', ['No tener miedo de empezar desde abajo.', 'Estudiar solo idiomas.', 'No trabajar en verano.']),
  LQ('M|Lo único que no echo de menos son los horarios: ¡ahora me levanto a las nueve!\nN|Pregunta: ¿Qué no echa de menos?', ['Los horarios.', 'A los turistas.', 'El mar.']),
], listening=True)

L3 = PART('l-noticias', 'listening', 'Comprensión auditiva — Tarea 3', 'Les informations', 'Escuche las noticias y elija la opción correcta.', 6, [
  LQ('N|Buenos días. Las lluvias de los últimos días han provocado el corte de varias carreteras en el norte de Galicia. Se recomienda no viajar por la zona hasta el miércoles.\nN|Pregunta: ¿Qué se recomienda?', ['No viajar por la zona hasta el miércoles.', 'Usar solo el tren.', 'Salir de Galicia hoy.']),
  LQ('N|El ayuntamiento de Valencia ha anunciado que a partir de enero los autobuses urbanos serán gratuitos para los menores de dieciocho años.\nN|Pregunta: ¿Quién viajará gratis?', ['Los menores de dieciocho años.', 'Los jubilados.', 'Todos los ciudadanos.']),
  LQ('N|Un grupo de estudiantes de Sevilla ha creado una aplicación que ayuda a reducir el desperdicio de comida en los restaurantes.\nN|Pregunta: ¿Para qué sirve la aplicación?', ['Para reducir el desperdicio de comida.', 'Para reservar mesa.', 'Para pedir taxis.']),
  LQ('N|El Museo del Prado abrirá gratis todos los domingos por la tarde durante el mes de mayo para celebrar su aniversario.\nN|Pregunta: ¿Cuándo será gratis el museo?', ['Los domingos por la tarde de mayo.', 'Todos los días de mayo.', 'Solo el día del aniversario.']),
  LQ('N|Según una encuesta, el sesenta por ciento de los españoles prefiere pasar las vacaciones en su propio país.\nN|Pregunta: ¿Qué dice la encuesta?', ['Que la mayoría prefiere viajar por España.', 'Que la mayoría viaja al extranjero.', 'Que nadie toma vacaciones.']),
  LQ('N|Mañana se espera una bajada de las temperaturas en toda la península, con nieve en las montañas a partir de mil metros.\nN|Pregunta: ¿Qué tiempo hará mañana?', ['Más frío, con nieve en las montañas.', 'Mucho calor.', 'Sol en toda España.']),
  LQ('N|La selección española de baloncesto ganó anoche la final del campeonato europeo tras un partido muy igualado.\nN|Pregunta: ¿Qué pasó anoche?', ['España ganó la final de baloncesto.', 'España perdió la final.', 'Se suspendió el partido.']),
], listening=True)

L4 = PART('l-opiniones', 'listening', 'Comprensión auditiva — Tarea 4', 'Des opinions', 'Escuche a estas personas que hablan del teletrabajo y elija la opción correcta.', 6, [
  LQ('F|Para mí trabajar desde casa es perfecto: ahorro dos horas de transporte al día y puedo estar con mis hijos.\nN|Pregunta: ¿Qué ventaja menciona la mujer?', ['No pierde tiempo en el transporte.', 'Gana más dinero.', 'Ve más a sus compañeros.']),
  LQ('M|A mí no me gusta nada. Echo de menos a mis compañeros y me cuesta separar el trabajo de la vida privada.\nN|Pregunta: ¿Qué opina el hombre?', ['Que es difícil separar trabajo y vida privada.', 'Que es la mejor solución.', 'Que trabaja menos horas.']),
  LQ('F|Creo que lo ideal es combinar: dos días en casa y tres en la oficina. Así tienes lo mejor de cada sistema.\nN|Pregunta: ¿Qué propone la mujer?', ['Combinar la casa y la oficina.', 'Trabajar siempre en casa.', 'Volver a la oficina todos los días.']),
  LQ('M|Yo vivo en un piso muy pequeño y no tengo espacio para trabajar. Por eso prefiero ir a la oficina.\nN|Pregunta: ¿Por qué prefiere ir a la oficina?', ['Porque su piso es pequeño.', 'Porque vive cerca.', 'Porque no tiene ordenador.']),
  LQ('F|No estoy segura de que el teletrabajo sea bueno para los jóvenes: se aprende mucho viendo trabajar a los demás.\nN|Pregunta: ¿Qué duda tiene la mujer?', ['Si es bueno para los jóvenes.', 'Si es más barato.', 'Si los jefes lo aceptan.']),
  LQ('M|Gracias al teletrabajo me fui a vivir a un pueblo de Cuenca. Pago menos alquiler y vivo más tranquilo.\nN|Pregunta: ¿Qué cambió en la vida del hombre?', ['Se fue a vivir a un pueblo.', 'Cambió de empresa.', 'Compró un piso en Madrid.']),
  LQ('F|Lo que más me molesta es que algunas empresas quieren controlar a los empleados todo el tiempo por la cámara.\nN|Pregunta: ¿Qué le molesta a la mujer?', ['El control constante de algunas empresas.', 'Los horarios flexibles.', 'Las reuniones presenciales.']),
], listening=True)

L5 = PART('l-conversacion', 'listening', 'Comprensión auditiva — Tarea 5', 'Une conversation', 'Escuche la conversación entre Marta y Diego y conteste a las preguntas.', 6, [
  LQ('F|Diego, ¿has visto el anuncio? Buscan voluntarios para limpiar la playa el sábado.\nM|Sí, lo he visto. Me apetece, pero el sábado por la mañana tengo partido de fútbol.\nN|Pregunta: ¿Por qué duda Diego?', ['Porque tiene un partido.', 'Porque no le gusta la playa.', 'Porque trabaja el sábado.']),
  LQ('F|La limpieza empieza a las diez y termina a las dos. Podrías venir después del partido.\nM|Vale, el partido acaba a las doce, así que llegaría a las doce y media.\nN|Pregunta: ¿A qué hora llegaría Diego?', ['A las doce y media.', 'A las diez.', 'A las dos.']),
  LQ('F|Tienes que inscribirte por internet antes del jueves.\nM|De acuerdo, lo hago esta noche. ¿Hay que llevar algo?\nN|Pregunta: ¿Cuándo hay que inscribirse?', ['Antes del jueves.', 'El mismo sábado.', 'Antes del lunes.']),
  LQ('F|Dan guantes y bolsas, pero recomiendan llevar gorra, crema solar y mucha agua.\nN|Pregunta: ¿Qué dan los organizadores?', ['Guantes y bolsas.', 'Gorras y crema.', 'Comida y agua.']),
  LQ('M|¿Y después qué hacemos?\nF|Al terminar, hay una comida para todos los voluntarios en el paseo marítimo.\nN|Pregunta: ¿Qué hay al final?', ['Una comida para los voluntarios.', 'Un concierto.', 'Un partido de voleibol.']),
  LQ('M|Le voy a decir a mi hermana que venga también; le encantan estas cosas.\nF|¡Genial! Cuantos más seamos, mejor.\nN|Pregunta: ¿A quién quiere invitar Diego?', ['A su hermana.', 'A su entrenador.', 'A sus compañeros de equipo.']),
  LQ('F|Por cierto, el año pasado recogimos más de trescientos kilos de plástico.\nM|¡Qué barbaridad! No me lo puedo creer.\nN|Pregunta: ¿Cómo reacciona Diego?', ['Se sorprende.', 'Se enfada.', 'No le interesa.']),
], listening=True)

# ═════════════════════════ Expresión e interacción escritas ═════════════════════════
MSG = 'Usted ha recibido este mensaje de una amiga:\n«¡Hola! Me han ofrecido un trabajo en Barcelona, pero tendría que dejar a mi familia y mi ciudad. No sé qué hacer. ¿Qué harías tú en mi lugar?»'
W1 = PART('w-mensaje', 'writing', 'Expresión escrita — Tarea 1', 'Répondre à un message', 'Lea el mensaje y elija la mejor respuesta.', 3, [
  RQ(['¡Hola, Laura! ¡Enhorabuena por la oferta! Entiendo que sea difícil, pero yo que tú aceptaría: es una gran oportunidad y Barcelona no está tan lejos. Además, podrás volver a menudo. ¡Ya me contarás!',
      '¡Hola, Laura! Enhorabuena. Yo que tú aceptaré, porque es una gran oportunidad y Barcelona no esté tan lejos.',
      '¡Hola, Laura! Yo el año pasado fui a Barcelona de vacaciones. Comí muy bien. Un beso.',
      'Laura: trabajo, Barcelona, familia, aceptar.'],
     None, f'{MSG}\n★ Elija la respuesta que reacciona, aconseja y argumenta.'),
  RQ(['Es normal que tengas dudas, pero creo que deberías intentarlo.', 'Es normal que tienes dudas, pero creo que deberías intentarlo.', 'Es normal que tengas dudas, pero creo que debas intentarlo.', 'Es normal tener dudas, pero no creo que deberías intentarlo.'],
     None, f'{MSG}\n★ Elija la frase correcta.'),
  RQ(['Si yo estuviera en tu lugar, hablaría primero con tu familia.', 'Si yo estaría en tu lugar, hablaría primero con tu familia.', 'Si yo estuviera en tu lugar, hablara primero con tu familia.', 'Si yo esté en tu lugar, hablaré primero con tu familia.'],
     None, f'{MSG}\n★ Elija la frase correcta para dar un consejo.'),
  RQ(['Cuando vayas a Barcelona, avísame y te presento a mis primos.', 'Cuando irás a Barcelona, avísame y te presento a mis primos.', 'Cuando vas a Barcelona mañana, avísame y te presentaré mis primos.', 'Cuando fueras a Barcelona, avísame y te presento a mis primos.'],
     None, f'{MSG}\n★ Elija la frase correcta.'),
])

W2 = PART('w-texto', 'writing', 'Expresión escrita — Tarea 2', 'Un texte argumenté', 'Lea la situación y elija el texto mejor escrito.', 2, [
  RQ(['En mi opinión, las redes sociales tienen ventajas e inconvenientes. Por un lado, nos permiten estar en contacto con amigos que viven lejos; por otro, pasamos demasiado tiempo delante de la pantalla. Por eso creo que es importante que aprendamos a usarlas con moderación.',
      'En mi opinión, las redes sociales tienen ventajas e inconvenientes. Por un lado, nos permiten estar en contacto; por otro, pasamos demasiado tiempo. Por eso creo que es importante que aprendemos a usarlas.',
      'Redes sociales: buenas y malas. Amigos lejos. Mucho tiempo. Moderación.',
      'En mi opinión las redes sociales son buenas porque son buenas y también son malas porque son malas, así que no sé.'],
     None, '★ Situación: escriba un texto para la revista de su escuela sobre las redes sociales (ventajas, inconvenientes, su opinión).'),
  RQ(['Nunca olvidaré mi primer viaje sola. Tenía veinte años y había ahorrado durante meses para ir a México. Cuando llegué, estaba nerviosa, pero la gente fue tan amable que enseguida me sentí como en casa. Desde entonces, viajo siempre que puedo.',
      'Nunca olvidaré mi primer viaje sola. Tuve veinte años y ahorraba durante meses para ir a México. Cuando llegaba, estuve nerviosa, pero la gente era tan amable.',
      'Primer viaje. México. Veinte años. Gente amable.',
      'Nunca olvidaré mi primer viaje sola. Tendré veinte años y voy a ahorrar para ir a México el año pasado.'],
     None, '★ Situación: cuente un viaje que recuerda especialmente (cuándo fue, qué pasó, cómo se sintió).'),
  RQ(['Estimados señores: les escribo para quejarme del servicio de su hotel. La habitación estaba sucia y el aire acondicionado no funcionaba. Les agradecería que me devolvieran parte del dinero. Atentamente, Marc Dubois.',
      'Estimados señores: les escribo para quejarme del servicio. La habitación estuvo sucia y el aire no funcionó. Les agradezco que me devuelvan todo. Besos, Marc.',
      'Hola, chicos: el hotel fue fatal. Devolvedme el dinero ya.',
      'Estimados señores: les escribo para felicitarles por la habitación sucia. Atentamente.'],
     None, '★ Situación: escriba una reclamación a un hotel (problemas y lo que pide).'),
])

PARTS = [R1, R2, R3, R4, R5, L1, L2, L3, L4, L5, W1, W2]
rea = sum(p['count'] for p in PARTS if p['section'] == 'reading')
lis = sum(p['count'] for p in PARTS if p['section'] == 'listening')
wri = sum(p['count'] for p in PARTS if p['section'] == 'writing')
assert (rea, lis, wri) == (30, 30, 5), (rea, lis, wri)
bank = {
  'slug': 'deleb1',
  'level': 'DELEB1',
  'contentVersion': '2026.11.23',
  'notice': 'Questions rédigées par Koto Quest au format de l’examen officiel du DELE B1 (Instituto Cervantes : types d’épreuves, consignes en espagnol, notation sur 100 en deux groupes). L’expression écrite se fait par choix multiple et l’expression orale n’est pas évaluée : le groupe 2 est noté sur l’écoute. Ce ne sont pas des questions officielles.',
  'parts': PARTS,
}
json.dump(bank, open(os.path.join(ROOT, 'content/exams/deleb1.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
EN = {
  bank['notice']: 'Questions written by Koto Quest in the format of the official DELE B1 exam (Instituto Cervantes: question types, instructions in Spanish, scoring out of 100 in two groups). Written expression is multiple choice and speaking is not assessed: group 2 is marked on listening. They are not official questions.',
  'Annonces et besoins': 'Adverts and needs', 'Un article': 'An article', 'Trois témoignages': 'Three accounts',
  'Un texte à compléter': 'A text to complete', 'Grammaire en contexte': 'Grammar in context',
  'Messages courts': 'Short messages', 'Un récit': 'A personal account', 'Les informations': 'The news',
  'Des opinions': 'Opinions', 'Une conversation': 'A conversation',
  'Répondre à un message': 'Replying to a message', 'Un texte argumenté': 'An argued text',
}
P_DICT = os.path.join(ROOT, 'content/i18n/en/content.json')
d = json.load(open(P_DICT, encoding='utf-8'))
for k, v in EN.items():
    if k in d and d[k] != v:
        raise SystemExit(f'traduction existante différente : {k} → {d[k]} / {v}')
d.update(EN)
json.dump(d, open(P_DICT, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(f"DELE B1 : {sum(len(p['questions']) for p in PARTS)} questions en banque ; examen de {rea} + {lis} + {wri} questions")
