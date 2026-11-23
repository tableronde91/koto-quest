# Banque de questions de l'examen blanc DELE A2 (content/exams/delea2.json), au format de l'épreuve officielle
# de l'Instituto Cervantes : compréhension écrite (4 tâches, 25 questions), compréhension auditive (5 tâches, 30 questions)
# et expression écrite (ici en format à choix : choisir la meilleure réponse à un courriel et le récit le mieux écrit).
# L'expression orale n'est pas évaluée. 110 minutes, notation sur 100, réussite avec au moins 30 points par groupe.
# Dans chaque question, le premier choix est la bonne réponse (l'ordre est mélangé à chaque examen).
# Usage : python3 scripts/delea2-exam.py
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

CORREO = ('Querida Elena: ¿qué tal todo? Te escribo desde Barcelona. Llegué el lunes pasado en tren desde Zaragoza: el viaje fue largo, pero muy bonito. '
          'Estoy en un piso pequeño cerca del puerto con dos compañeras de trabajo; es más barato que un hotel y tiene una terraza con vistas al mar. '
          'Esta semana he trabajado mucho en la nueva oficina, pero ayer por la tarde fuimos a la playa y cenamos pescado en un restaurante del barrio. '
          'Todavía no he visitado la Sagrada Familia: hay que comprar la entrada por internet y no he tenido tiempo. '
          '¿Por qué no vienes en mayo? Puedes dormir en el sofá. Un abrazo, Lucía.')

TEXTO = ('Cuando era pequeño, mi abuelo Antonio vivía en un pueblo de Aragón. No había coches y las calles eran de tierra. '
         'Todos los días se levantaba a las seis, daba de comer a las vacas y después iba al campo con su padre. '
         'En invierno hacía mucho frío y los niños estudiaban en una sola clase con una estufa de leña. '
         'Su mejor recuerdo es la fiesta de agosto: había música en la plaza y la gente bailaba hasta el amanecer. '
         'A los dieciocho años se fue a Barcelona para trabajar en el puerto. Allí conoció a mi abuela, que era enfermera, y se casaron en 1965. '
         'Ahora tiene ochenta y cinco años y vive con nosotros, pero cada verano vuelve al pueblo una semana.')

# ═════════════════════════ Comprensión de lectura ═════════════════════════
R1 = PART('r-correo', 'reading', 'Comprensión de lectura — Tarea 1', 'Un courriel', 'Lea el correo y conteste a las preguntas.', 5, [
  RP(CORREO, '¿Cómo llegó Lucía a Barcelona?', ['En tren.', 'En avión.', 'En autobús.']),
  RP(CORREO, '¿Con quién vive Lucía?', ['Con dos compañeras de trabajo.', 'Con Elena.', 'Sola, en un hotel.']),
  RP(CORREO, '¿Qué tiene el piso?', ['Una terraza con vistas al mar.', 'Tres dormitorios.', 'Un jardín grande.']),
  RP(CORREO, '¿Qué hizo Lucía ayer por la tarde?', ['Fue a la playa y cenó fuera.', 'Visitó la Sagrada Familia.', 'Trabajó en la oficina hasta tarde.']),
  RP(CORREO, '¿Por qué no ha visitado la Sagrada Familia?', ['Porque no ha tenido tiempo de comprar la entrada.', 'Porque está cerrada.', 'Porque es muy cara.']),
  RP(CORREO, '¿Qué le propone Lucía a Elena?', ['Venir a Barcelona en mayo.', 'Buscar un piso juntas.', 'Trabajar en su oficina.']),
])

R2 = PART('r-anuncios', 'reading', 'Comprensión de lectura — Tarea 2', 'Panneaux et annonces', 'Lea los textos y elija la opción correcta.', 8, [
  RP('SE ALQUILA HABITACIÓN\nEn piso compartido, cerca de la universidad. 350 € al mes, gastos incluidos.\nNo se aceptan animales.', 'La habitación…', ['tiene los gastos incluidos en el precio.', 'es para una persona con perro.', 'está lejos de la universidad.']),
  RP('MUSEO PICASSO\nCerrado por obras hasta el 15 de marzo.\nDisculpen las molestias.', 'El museo…', ['no abre hasta mediados de marzo.', 'cierra el 15 de marzo.', 'está abierto con descuento.']),
  RP('SE BUSCA CAMARERO/A\nPara fines de semana. Experiencia mínima: un año.\nInteresados: enviar currículum a info@barlaola.es', 'Para este trabajo…', ['hay que tener experiencia y trabajar los fines de semana.', 'hay que trabajar de lunes a viernes.', 'no hace falta experiencia.']),
  RP('RENFE INFORMA\nPor obras en la vía, los trenes a Tarragona salen de la estación de Sants con 30 minutos de retraso.', 'Los trenes a Tarragona…', ['salen media hora más tarde.', 'no salen hoy.', 'salen de otra estación.']),
  RP('CURSO DE COCINA CATALANA\n4 sábados de octubre, de 10:00 a 13:00.\nPrecio: 120 €. Plazas limitadas: reserve antes del 30 de septiembre.', 'Para hacer el curso…', ['hay que reservar antes de octubre.', 'hay que ir cuatro domingos.', 'no hay que pagar.']),
  RP('PLAYA DE LA BARCELONETA\nBandera roja: prohibido bañarse.', 'Hoy en la playa…', ['no se puede nadar.', 'se puede nadar con cuidado.', 'hay que llevar bandera.']),
  RP('ATENCIÓN, CLIENTES\nEl ascensor no funciona. Por favor, utilicen la escalera.\nGracias por su paciencia.', 'El cartel dice que…', ['hay que subir a pie.', 'el ascensor es nuevo.', 'la escalera está cerrada.']),
  RP('PERDIDO\nGato blanco y negro, se llama Tigre. Lo perdimos el domingo en el parque del Retiro.\nSi lo ves, llama al 655 210 987.', 'Los dueños del gato…', ['lo perdieron el domingo.', 'lo encontraron en el parque.', 'quieren vender el gato.']),
  RP('BIBLIOTECA\nLos libros se pueden tener tres semanas.\nSi los devuelve tarde, no podrá sacar libros durante un mes.', 'En la biblioteca…', ['hay que devolver los libros en tres semanas.', 'los libros se pueden tener un mes.', 'no se pueden sacar libros.']),
  RP('FIESTA MAYOR DE GRÀCIA\nDel 15 al 21 de agosto: conciertos, desfiles y fuegos artificiales.\nTodas las actividades son gratuitas.', 'En la fiesta…', ['no hay que pagar por las actividades.', 'los conciertos cuestan 15 €.', 'solo hay fuegos artificiales.']),
])

R3 = PART('r-mensajes', 'reading', 'Comprensión de lectura — Tarea 3', 'Messages courts', 'Lea los mensajes y elija la opción correcta.', 6, [
  RP('Javier: ¿Quedamos mañana para tomar algo? A las siete en la plaza Real me va bien.', 'Javier propone…', ['quedar mañana a las siete.', 'cenar en su casa.', 'ir a la plaza hoy.']),
  RP('Clara: Lo siento, no puedo ir al cine esta noche: es que tengo que terminar un trabajo. ¿El viernes?', 'Clara…', ['no puede ir hoy y propone otro día.', 'va al cine sola.', 'ya ha terminado su trabajo.']),
  RP('Mamá: He dejado la llave debajo de la maceta. Saca la basura y pon la lavadora, por favor.', 'La madre pide a su hijo que…', ['haga dos tareas de casa.', 'compre una maceta.', 'busque la llave en la oficina.']),
  RP('Dr. Vidal: Su cita es el martes 12 a las 9:30. Si no puede venir, llame al centro antes del lunes.', 'El paciente debe llamar si…', ['no puede ir a la cita.', 'llega antes de las nueve.', 'quiere ir el lunes.']),
  RP('Pablo: Ya he llegado a Valencia. El viaje ha sido muy tranquilo. Te llamo esta noche.', 'Pablo…', ['ya está en Valencia.', 'todavía está en el tren.', 'no ha podido viajar.']),
  RP('Inés: Ayer perdí mi móvil en el autobús 24. Si alguien lo encuentra, escribid a este correo.', 'Inés…', ['perdió el teléfono en el autobús.', 'encontró un móvil.', 'compró un móvil nuevo.']),
  RP('Hotel Mar: Le recordamos que la habitación debe dejarse libre antes de las 12:00. Puede dejar sus maletas en recepción.', 'El cliente…', ['tiene que salir de la habitación antes de mediodía.', 'no puede dejar las maletas.', 'puede quedarse hasta la noche.']),
  RP('Sergio: Te presto mi bici el sábado, pero devuélvemela el domingo por la mañana, ¿vale?', 'Sergio…', ['le presta la bicicleta a su amigo.', 'le regala la bicicleta.', 'necesita la bici el sábado.']),
])

R4 = PART('r-texto', 'reading', 'Comprensión de lectura — Tarea 4', 'Un texte long', 'Lea el texto y conteste a las preguntas.', 6, [
  RP(TEXTO, '¿Cómo era el pueblo del abuelo?', ['No había coches y las calles eran de tierra.', 'Era una ciudad grande.', 'Tenía muchas tiendas.']),
  RP(TEXTO, '¿Qué hacía el abuelo todos los días?', ['Daba de comer a las vacas e iba al campo.', 'Iba a la playa.', 'Trabajaba en el puerto.']),
  RP(TEXTO, '¿Cómo era la escuela?', ['Una sola clase con una estufa.', 'Un colegio muy moderno.', 'Una escuela en la ciudad.']),
  RP(TEXTO, '¿Cuál es el mejor recuerdo del abuelo?', ['La fiesta de agosto.', 'El primer día de trabajo.', 'Su viaje en tren.']),
  RP(TEXTO, '¿Por qué se fue a Barcelona?', ['Para trabajar.', 'Para estudiar.', 'Para casarse.']),
  RP(TEXTO, '¿Qué hace el abuelo ahora cada verano?', ['Vuelve una semana al pueblo.', 'Trabaja en el campo.', 'Va de vacaciones a la playa.']),
  RP(TEXTO, '¿Quién era la abuela?', ['Una enfermera que conoció en Barcelona.', 'Una vecina del pueblo.', 'Una profesora de la escuela.']),
])

# ═════════════════════════ Comprensión auditiva ═════════════════════════
L1 = PART('l-dialogos', 'listening', 'Comprensión auditiva — Tarea 1', 'Dialogues courts', 'Escuche el diálogo y conteste a la pregunta.', 6, [
  LQ('F|¿Qué hiciste el fin de semana?\nM|El sábado fui a la montaña y el domingo me quedé en casa leyendo.\nN|Pregunta: ¿Qué hizo el hombre el domingo?', ['Se quedó en casa.', 'Fue a la montaña.', 'Fue al cine.']),
  LQ('M|¿Has comprado ya los billetes?\nF|Todavía no. Los compro esta tarde por internet.\nN|Pregunta: ¿Cuándo va a comprar los billetes la mujer?', ['Esta tarde.', 'Ya los ha comprado.', 'Mañana por la mañana.']),
  LQ('F|Perdone, ¿el autobús para el aeropuerto?\nM|Sale cada veinte minutos de la parada de enfrente.\nN|Pregunta: ¿Cada cuánto sale el autobús?', ['Cada veinte minutos.', 'Cada dos horas.', 'Cada doce minutos.']),
  LQ('M|¿Te gusta más el piso nuevo?\nF|Sí, es más grande que el otro y tiene más luz, pero está más lejos del trabajo.\nN|Pregunta: ¿Qué problema tiene el piso nuevo?', ['Está más lejos del trabajo.', 'Es más pequeño.', 'Tiene poca luz.']),
  LQ('F|¿Qué te pasa? Tienes mala cara.\nM|Anoche no dormí nada: mis vecinos hicieron una fiesta.\nN|Pregunta: ¿Por qué está cansado el hombre?', ['Porque sus vecinos hicieron una fiesta.', 'Porque trabajó toda la noche.', 'Porque está enfermo.']),
  LQ('M|¿Quedamos para cenar el jueves?\nF|El jueves no puedo; es que tengo clase de inglés. ¿Qué tal el viernes?\nN|Pregunta: ¿Qué día propone la mujer?', ['El viernes.', 'El jueves.', 'El sábado.']),
  LQ('F|¿Cuándo empezaste a trabajar aquí?\nM|Hace tres años, después de terminar la universidad.\nN|Pregunta: ¿Cuándo empezó a trabajar el hombre?', ['Hace tres años.', 'Hace trece años.', 'El año pasado.']),
  LQ('M|¿Qué le vas a regalar a tu hermana?\nF|Le voy a regalar un libro de cocina, porque le encanta cocinar.\nN|Pregunta: ¿Qué le va a regalar a su hermana?', ['Un libro de cocina.', 'Una cena en un restaurante.', 'Un curso de cocina.']),
], listening=True)

L2 = PART('l-avisos', 'listening', 'Comprensión auditiva — Tarea 2', 'Annonces et messages', 'Escuche el anuncio y elija la opción correcta.', 6, [
  LQ('N|Señores pasajeros: el vuelo IB 3410 con destino Sevilla tiene un retraso de cuarenta y cinco minutos. Embarque por la puerta B12.\nN|Pregunta: ¿Qué le pasa al vuelo?', ['Sale con retraso.', 'Está cancelado.', 'Sale de la puerta A12.']),
  LQ('N|Atención: el mercado de la Boquería cierra hoy a las tres de la tarde por la fiesta local.\nN|Pregunta: ¿Por qué cierra antes el mercado?', ['Porque hay una fiesta local.', 'Porque hay obras.', 'Porque es domingo.']),
  LQ('N|Esta semana, en la tienda Deportes Ruiz, las bicicletas tienen un veinte por ciento de descuento.\nN|Pregunta: ¿Qué está más barato?', ['Las bicicletas.', 'Los zapatos.', 'La ropa de baño.']),
  LQ('N|Les informamos de que la piscina del hotel está cerrada hasta mañana por limpieza. Disculpen las molestias.\nN|Pregunta: ¿Hasta cuándo está cerrada la piscina?', ['Hasta mañana.', 'Hasta el fin de semana.', 'Todo el verano.']),
  LQ('N|Biblioteca municipal: el próximo martes a las seis, el escritor Carlos Zafra presenta su nueva novela. Entrada libre.\nN|Pregunta: ¿Qué pasa el martes?', ['Un escritor presenta su novela.', 'Cierra la biblioteca.', 'Hay un concierto.']),
  LQ('N|Último aviso: el tren regional con destino Girona va a salir de la vía siete. Los viajeros deben subir al tren.\nN|Pregunta: ¿De qué vía sale el tren?', ['De la vía siete.', 'De la vía once.', 'De la vía uno.']),
  LQ('N|Mañana, en Barcelona, cielo nublado por la mañana y lluvia por la tarde. Las temperaturas van a bajar.\nN|Pregunta: ¿Qué tiempo va a hacer mañana por la tarde?', ['Va a llover.', 'Va a hacer sol.', 'Va a nevar.']),
], listening=True)

L3 = PART('l-radio', 'listening', 'Comprensión auditiva — Tarea 3', 'À la radio', 'Escuche el programa de radio y conteste a las preguntas.', 6, [
  LQ('N|Hoy hablamos con Marta Soler, cocinera. Marta, ¿cómo empezaste?\nF|De pequeña cocinaba con mi abuela todos los domingos. A los veinte años estudié cocina y luego trabajé en París dos años.\nN|Pregunta: ¿Con quién cocinaba Marta de pequeña?', ['Con su abuela.', 'Con su madre.', 'Con un cocinero de París.']),
  LQ('N|Marta, ¿dónde trabajaste antes de abrir tu restaurante?\nF|Trabajé dos años en París, en un hotel muy famoso.\nN|Pregunta: ¿Cuánto tiempo trabajó en París?', ['Dos años.', 'Doce años.', 'Dos meses.']),
  LQ('N|¿Y cuándo abriste tu restaurante?\nF|Lo abrí en 2018, aquí en Barcelona, cerca del puerto.\nN|Pregunta: ¿Dónde está el restaurante?', ['Cerca del puerto de Barcelona.', 'En París.', 'En el pueblo de su abuela.']),
  LQ('N|¿Cuál es el plato más famoso de tu restaurante?\nF|El arroz negro. Es el plato que más piden los clientes.\nN|Pregunta: ¿Cuál es el plato más pedido?', ['El arroz negro.', 'La paella de verduras.', 'El pescado al horno.']),
  LQ('N|¿Qué consejo das a los jóvenes cocineros?\nF|Hay que trabajar mucho y probar todo. Y es mejor usar productos del mercado.\nN|Pregunta: ¿Qué consejo da Marta?', ['Usar productos del mercado.', 'Trabajar poco.', 'Viajar a París.']),
  LQ('N|¿Y qué haces en tu tiempo libre?\nF|Casi no tengo tiempo libre, pero los lunes, cuando el restaurante cierra, nado en el mar.\nN|Pregunta: ¿Qué hace Marta los lunes?', ['Nada en el mar.', 'Trabaja en el restaurante.', 'Va al mercado.']),
  LQ('N|Por último, ¿un sueño para el futuro?\nF|Me gustaría escribir un libro con las recetas de mi abuela.\nN|Pregunta: ¿Qué quiere hacer Marta en el futuro?', ['Escribir un libro de recetas.', 'Abrir otro restaurante.', 'Vivir en París.']),
], listening=True)

L4 = PART('l-mensajes', 'listening', 'Comprensión auditiva — Tarea 4', 'Messages vocaux', 'Escuche los mensajes y elija la opción correcta.', 6, [
  LQ('F|Hola, Andrés, soy Rosa. Esta tarde no puedo ir al gimnasio contigo porque tengo que llevar a mi hijo al médico. ¿Vamos mañana?\nN|Pregunta: ¿Por qué no puede ir Rosa al gimnasio?', ['Tiene que ir al médico con su hijo.', 'Está enferma.', 'Tiene que trabajar.']),
  LQ('M|Buenos días, le llamamos de la agencia Pisos Sol. El piso de la calle Aragón todavía está libre. Puede visitarlo el jueves a las cinco.\nN|Pregunta: ¿Cuándo puede visitar el piso?', ['El jueves a las cinco.', 'Hoy a las cinco.', 'El martes por la mañana.']),
  LQ('F|Papá, soy Laura. Ya he llegado al hotel. La habitación es pequeña pero muy bonita. Mañana te llamo.\nN|Pregunta: ¿Cómo es la habitación?', ['Pequeña pero bonita.', 'Grande y fea.', 'Grande y bonita.']),
  LQ('M|Hola, soy Diego, tu vecino del tercero. Te he dejado un paquete en la puerta: el cartero lo trajo ayer.\nN|Pregunta: ¿Dónde está el paquete?', ['En la puerta.', 'En Correos.', 'En el tercer piso.']),
  LQ('F|Le recordamos su cita con la dentista mañana, miércoles, a las diez y cuarto. Por favor, llegue diez minutos antes.\nN|Pregunta: ¿A qué hora debe llegar el paciente?', ['A las diez y cinco.', 'A las diez y cuarto.', 'A las diez y media.']),
  LQ('M|Hola, Elena. He perdido el tren de las ocho. Cojo el siguiente, que sale a las nueve. Llego una hora tarde, lo siento.\nN|Pregunta: ¿Qué ha pasado?', ['Ha perdido el tren.', 'El tren tiene retraso.', 'Ha llegado antes.']),
  LQ('F|Hola, soy Marisa. ¿Me puedes prestar tu maleta grande para el viaje a Roma? Te la devuelvo el domingo.\nN|Pregunta: ¿Qué le pide Marisa?', ['Que le preste una maleta.', 'Que vaya con ella a Roma.', 'Que le compre un billete.']),
], listening=True)

L5 = PART('l-conversacion', 'listening', 'Comprensión auditiva — Tarea 5', 'Une conversation', 'Escuche la conversación entre dos amigos y conteste a las preguntas.', 6, [
  LQ('M|¡Hola, Carmen! ¿Qué tal las vacaciones?\nF|¡Genial! Estuve diez días en Asturias con mi hermana.\nN|Pregunta: ¿Con quién fue Carmen de vacaciones?', ['Con su hermana.', 'Con su novio.', 'Sola.']),
  LQ('M|¿Y qué tiempo hizo?\nF|Llovió casi todos los días, pero no hizo frío.\nN|Pregunta: ¿Qué tiempo hizo en Asturias?', ['Llovió mucho.', 'Hizo mucho calor.', 'Hizo frío y nevó.']),
  LQ('M|¿Dónde dormíais?\nF|En una casa rural en un pueblo pequeño, al lado de un río. Era muy tranquila.\nN|Pregunta: ¿Dónde se alojaron?', ['En una casa rural.', 'En un hotel de la ciudad.', 'En un camping.']),
  LQ('M|¿Qué hicisteis?\nF|Hicimos senderismo por la montaña y un día fuimos a la costa en coche.\nN|Pregunta: ¿Cómo fueron a la costa?', ['En coche.', 'En tren.', 'A pie.']),
  LQ('M|¿Y la comida?\nF|Riquísima. Lo mejor fue el queso; compré tres para mi familia.\nN|Pregunta: ¿Qué compró Carmen?', ['Queso.', 'Vino.', 'Pescado.']),
  LQ('M|¿Vas a volver?\nF|Sí, el año que viene quiero ir otra vez, pero en septiembre, porque en agosto hay demasiada gente.\nN|Pregunta: ¿Por qué quiere volver en septiembre?', ['Porque en agosto hay mucha gente.', 'Porque en septiembre hace más calor.', 'Porque trabaja en agosto.']),
  LQ('F|¿Y tú, Óscar? ¿Qué hiciste en verano?\nM|Nada especial: trabajé todo el mes de julio y en agosto pinté mi piso.\nN|Pregunta: ¿Qué hizo Óscar en agosto?', ['Pintó su piso.', 'Trabajó.', 'Fue a Asturias.']),
], listening=True)

# ═════════════════════════ Expresión e interacción escritas ═════════════════════════
MAIL = 'Usted ha recibido este correo de su amigo Marcos:\n«¡Hola! El mes que viene voy a visitar tu ciudad. ¿Qué me recomiendas ver? ¿Dónde puedo dormir? ¿Quedamos un día para cenar?»'
W1 = PART('w-correo', 'writing', 'Expresión escrita — Tarea 1', 'Répondre à un courriel', 'Lea el correo y elija la mejor respuesta.', 3, [
  RQ(['¡Hola, Marcos! ¡Qué bien que vienes! Te recomiendo ver el casco antiguo y el museo. Puedes dormir en un hostal cerca de la estación. ¿Cenamos el sábado? Un abrazo.',
      '¡Hola, Marcos! Fui a tu ciudad el año pasado. Era muy bonita. Un abrazo.',
      '¡Hola, Marcos! Te recomiendo ver el casco antiguo. Puedes dormir en el museo. No quiero cenar contigo.',
      'Marcos: ciudad, museo, hostal, cenar.'],
     None, f'{MAIL}\n★ Elija la respuesta que contesta a las tres preguntas de Marcos.'),
  RQ(['Te recomiendo visitar el puerto: es lo más bonito de la ciudad.', 'Te recomiendo visitado el puerto: es la más bonito de la ciudad.', 'Te recomiendo visitar el puerto: es lo más bonita que la ciudad.', 'Te recomiendo que visitas el puerto: es lo más bonito en la ciudad.'],
     None, f'{MAIL}\n★ Elija la frase correcta para recomendar un lugar.'),
  RQ(['¿Quedamos el viernes a las nueve en la plaza Mayor?', '¿Quedamos el viernes en las nueve a la plaza Mayor?', '¿Quedamos al viernes a nueve por la plaza Mayor?', '¿Quedemos el viernes a las nueve en plaza Mayor?'],
     None, f'{MAIL}\n★ Elija la frase correcta para proponer una cita.'),
  RQ(['Lo siento, ese fin de semana no estoy en la ciudad, pero mi hermano te puede enseñar el barrio.', 'Lo siento, ese fin de semana no soy en la ciudad, pero mi hermano te puede enseñar el barrio.', 'Lo siento, ese fin de semana no estoy a la ciudad, pero mi hermano te puedes enseñar el barrio.', 'Lo siento, ese fin de semana no estuve en la ciudad, pero mi hermano te ha enseñado el barrio.'],
     None, f'{MAIL}\n★ Usted no va a estar en la ciudad. Elija la frase correcta.'),
])

W2 = PART('w-relato', 'writing', 'Expresión escrita — Tarea 2', 'Raconter au passé', 'Lea la situación y elija el texto mejor escrito.', 2, [
  RQ(['El verano pasado fui a Galicia con mis padres. Hacía buen tiempo y todos los días íbamos a la playa. Un día visitamos Santiago de Compostela y comimos pulpo. ¡Fue un viaje estupendo!',
      'El verano pasado voy a Galicia con mis padres. Hizo buen tiempo y todos los días fuimos a la playa. Un día visitábamos Santiago y comemos pulpo.',
      'Verano pasado Galicia padres. Buen tiempo, playa, Santiago, pulpo. Estupendo.',
      'El verano que viene fui a Galicia con mis padres. Hacía buen tiempo mañana y vamos a la playa ayer.'],
     None, '★ Situación: cuente un viaje que hizo (adónde fue, con quién, qué tiempo hacía, qué hizo).'),
  RQ(['Cuando era pequeña, vivía en un pueblo cerca de Valencia. Mi casa tenía un jardín con naranjos y yo jugaba allí con mi perro. Los domingos mi abuela preparaba paella para toda la familia.',
      'Cuando fui pequeña, viví en un pueblo cerca de Valencia. Mi casa tuvo un jardín y yo jugué allí todos los días con mi perro.',
      'Cuando soy pequeña, vivo en un pueblo. Mi casa tiene un jardín. Mi abuela prepara paella.',
      'Cuando era pequeña, vivía en un pueblo cerca de Valencia. Mi casa era un jardín con naranjos y yo estaba con mi perro los domingos de mi abuela.'],
     None, '★ Situación: describa cómo era su vida de niño o niña (dónde vivía, cómo era su casa, qué hacía).'),
  RQ(['Ayer tuve un día horrible: me levanté tarde, perdí el autobús y llegué al trabajo a las diez. Mi jefe estaba muy enfadado.',
      'Ayer tenía un día horrible: me levantaba tarde, perdía el autobús y llegaba al trabajo a las diez. Mi jefe estuvo muy enfadado.',
      'Ayer he tenido un día horrible: me he levantado tarde. Mi jefe es muy enfadado.',
      'Ayer tengo un día horrible: me levanto tarde y pierdo el autobús.'],
     None, '★ Situación: cuente un día en que todo salió mal (qué pasó, cómo se sentía).'),
])

PARTS = [R1, R2, R3, R4, L1, L2, L3, L4, L5, W1, W2]
rea = sum(p['count'] for p in PARTS if p['section'] == 'reading')
lis = sum(p['count'] for p in PARTS if p['section'] == 'listening')
wri = sum(p['count'] for p in PARTS if p['section'] == 'writing')
assert (rea, lis, wri) == (25, 30, 5), (rea, lis, wri)
bank = {
  'slug': 'delea2',
  'level': 'DELEA2',
  'contentVersion': '2026.11.23',
  'notice': 'Questions rédigées par Koto Quest au format de l’examen officiel du DELE A2 (Instituto Cervantes : types d’épreuves, consignes en espagnol, notation sur 100 en deux groupes). L’expression écrite se fait par choix multiple et l’expression orale n’est pas évaluée : le groupe 2 est noté sur l’écoute. Ce ne sont pas des questions officielles.',
  'parts': PARTS,
}
json.dump(bank, open(os.path.join(ROOT, 'content/exams/delea2.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
EN = {
  bank['notice']: 'Questions written by Koto Quest in the format of the official DELE A2 exam (Instituto Cervantes: question types, instructions in Spanish, scoring out of 100 in two groups). Written expression is multiple choice and speaking is not assessed: group 2 is marked on listening. They are not official questions.',
  'Un courriel': 'An email', 'Panneaux et annonces': 'Signs and adverts', 'Messages courts': 'Short messages', 'Un texte long': 'A long text',
  'Dialogues courts': 'Short dialogues', 'Annonces et messages': 'Notices and messages', 'À la radio': 'On the radio',
  'Messages vocaux': 'Voice messages', 'Une conversation': 'A conversation',
  'Répondre à un courriel': 'Replying to an email', 'Raconter au passé': 'Telling a story in the past',
}
P_DICT = os.path.join(ROOT, 'content/i18n/en/content.json')
d = json.load(open(P_DICT, encoding='utf-8'))
for k, v in EN.items():
    if k in d and d[k] != v:
        raise SystemExit(f'traduction existante différente : {k} → {d[k]} / {v}')
d.update(EN)
json.dump(d, open(P_DICT, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(f"DELE A2 : {sum(len(p['questions']) for p in PARTS)} questions en banque ; examen de {rea} + {lis} + {wri} questions")
