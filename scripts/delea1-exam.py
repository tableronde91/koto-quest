# Banque de questions de l'examen blanc DELE A1 (content/exams/delea1.json), au format de l'épreuve officielle
# de l'Instituto Cervantes : compréhension écrite (25 questions), compréhension auditive (25 questions) et expression
# écrite (ici en format à choix : choisir la bonne réponse d'un formulaire et le message le mieux écrit). L'expression
# orale n'est pas évaluée. 90 minutes, notation sur 100, réussite avec au moins 30 points par groupe.
# Dans chaque question, le premier choix est la bonne réponse (l'ordre est mélangé à chaque examen).
# Usage : python3 scripts/delea1-exam.py
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

CORREO = ('¡Hola, Marta! Te escribo desde Toledo. Estoy aquí con mi hermano Pablo para las vacaciones. '
          'El hotel está en el centro, al lado de la catedral. Por la mañana visitamos museos y por la tarde paseamos por las calles. '
          'La comida es muy buena: me encanta el queso manchego. Hace mucho calor, ¡treinta y ocho grados! '
          'El sábado vamos a ir a Consuegra para ver los molinos. Volvemos a Madrid el domingo en tren. Un beso, Lucía.')

# ═════════════════════════ Comprensión de lectura ═════════════════════════
R1 = PART('r-correo', 'reading', 'Comprensión de lectura — Tarea 1', 'Un courriel', 'Lea el correo y conteste a las preguntas.', 5, [
  RP(CORREO, '¿Con quién está Lucía en Toledo?', ['Con su hermano.', 'Con Marta.', 'Con sus padres.']),
  RP(CORREO, '¿Dónde está el hotel?', ['Al lado de la catedral.', 'Lejos del centro.', 'En la estación.']),
  RP(CORREO, '¿Qué hacen por la tarde?', ['Pasean por las calles.', 'Visitan museos.', 'Duermen en el hotel.']),
  RP(CORREO, '¿Qué tiempo hace en Toledo?', ['Hace mucho calor.', 'Llueve mucho.', 'Hace frío.']),
  RP(CORREO, '¿Qué van a hacer el sábado?', ['Ver los molinos de Consuegra.', 'Volver a Madrid.', 'Comer en casa de Marta.']),
  RP(CORREO, '¿Cómo vuelven a Madrid?', ['En tren.', 'En coche.', 'En autobús.']),
])

R2 = PART('r-anuncios', 'reading', 'Comprensión de lectura — Tarea 2', 'Panneaux et annonces', 'Lea los textos y elija la opción correcta.', 10, [
  RP('FARMACIA DE GUARDIA\nAbierta hoy de 22:00 a 9:00.', 'Esta farmacia…', ['abre por la noche.', 'está cerrada hoy.', 'abre solo por la mañana.']),
  RP('MUSEO DEL GRECO\nEntrada: 3 €. Domingos por la tarde: gratis.\nLunes cerrado.', 'El museo…', ['es gratis el domingo por la tarde.', 'abre todos los días.', 'cuesta tres euros el domingo por la tarde.']),
  RP('SE ALQUILA PISO\nDos habitaciones, cocina y baño. Cerca de la estación. 500 € al mes.\nTeléfono: 612 345 678', 'El piso…', ['tiene dos habitaciones.', 'está lejos de la estación.', 'cuesta 500 € a la semana.']),
  RP('RESTAURANTE LA VENTA\nMenú del día: 12 €\nPrimer plato, segundo plato, postre, pan y bebida.', 'En el menú del día…', ['la bebida está incluida.', 'no hay postre.', 'el pan cuesta aparte.']),
  RP('PROHIBIDO FUMAR', 'Este cartel dice que…', ['no se puede fumar.', 'se puede fumar.', 'hay tabaco.']),
  RP('BIBLIOTECA MUNICIPAL\nHorario: de lunes a viernes, de 9:00 a 20:00.\nSábados: de 10:00 a 14:00.', 'La biblioteca…', ['abre el sábado por la mañana.', 'abre el domingo.', 'cierra a las dos todos los días.']),
  RP('CLASES DE GUITARRA\nPara niños y adultos. Martes y jueves, a las 18:00.\nPrimera clase gratis.', 'Las clases de guitarra…', ['son dos días a la semana.', 'son solo para niños.', 'son por la mañana.']),
  RP('TIENDA DE ROPA SOL\n¡Rebajas! Todo al 50 %.\nCamisas desde 10 €.', 'En la tienda…', ['la ropa está más barata.', 'las camisas cuestan 50 €.', 'no hay camisas.']),
  RP('ESTACIÓN DE AUTOBUSES\nAutobús a Madrid: cada hora, de 7:00 a 22:00.', 'El autobús a Madrid…', ['sale cada hora.', 'sale una vez al día.', 'no sale por la tarde.']),
  RP('PISCINA MUNICIPAL\nAbierta de junio a septiembre.\nNiños menores de 6 años: gratis.', 'La piscina…', ['abre en verano.', 'abre todo el año.', 'es gratis para todos.']),
  RP('PANADERÍA EL MOLINO\nPan recién hecho todas las mañanas.\nCerrado los domingos.', 'La panadería…', ['no abre el domingo.', 'solo vende pasteles.', 'abre por la noche.']),
])

R3 = PART('r-mensajes', 'reading', 'Comprensión de lectura — Tarea 3', 'Messages courts', 'Lea los mensajes y elija la opción correcta.', 10, [
  RP('Mamá: Hoy llego tarde, a las nueve. La cena está en la cocina. Besos.', '¿Qué dice la madre?', ['Que llega a las nueve.', 'Que no hay cena.', 'Que llega temprano.']),
  RP('Pedro: ¿Vamos al cine esta noche? La película empieza a las diez.', 'Pedro quiere…', ['ir al cine.', 'cenar en casa.', 'ver la película mañana.']),
  RP('Ana: No puedo ir a clase hoy, estoy enferma. ¿Me pasas los deberes?', 'Ana…', ['está enferma.', 'va a clase.', 'tiene los deberes.']),
  RP('Señor Ruiz: La reunión es el lunes a las once en la sala 3, no el martes.', 'La reunión es…', ['el lunes.', 'el martes.', 'a las tres.']),
  RP('Carlos: ¡Feliz cumpleaños, Elena! ¿Celebramos el sábado en mi casa?', 'Carlos…', ['invita a Elena a su casa.', 'tiene su cumpleaños.', 'no puede el sábado.']),
  RP('Laura: Estoy en la puerta del museo. ¿Dónde estás tú?', 'Laura está…', ['delante del museo.', 'en casa.', 'en el tren.']),
  RP('Hotel Sol: Su habitación es la 204, en el segundo piso. El desayuno es de 7:30 a 10:00.', 'El desayuno termina…', ['a las diez.', 'a las siete y media.', 'a las dos.']),
  RP('Jorge: Compra pan y leche, por favor. Yo compro la fruta.', 'Jorge compra…', ['la fruta.', 'el pan.', 'la leche.']),
  RP('Profesora: Mañana no hay clase. Nos vemos el jueves.', 'La próxima clase es…', ['el jueves.', 'mañana.', 'hoy.']),
  RP('Marta: El autobús no viene. Voy a llegar veinte minutos tarde. ¡Perdón!', 'Marta va a llegar tarde porque…', ['el autobús no llega.', 'está enferma.', 'no tiene dinero.']),
  RP('Tienda: Su pedido está listo. Puede recogerlo de lunes a sábado, de 10:00 a 20:00.', 'El cliente puede recoger el pedido…', ['el sábado.', 'el domingo.', 'a las nueve de la mañana.']),
])

# ═════════════════════════ Comprensión auditiva ═════════════════════════
L1 = PART('l-dialogos', 'listening', 'Comprensión auditiva — Tarea 1', 'Dialogues courts', 'Escuche el diálogo y conteste a la pregunta.', 10, [
  LQ('F|Hola, ¿qué quieres tomar?\nM|Un café con leche, por favor.\nN|Pregunta: ¿Qué quiere el hombre?', ['Un café con leche.', 'Un té.', 'Un zumo de naranja.']),
  LQ('M|Perdone, ¿dónde está la estación?\nF|Siga todo recto y gire a la derecha.\nN|Pregunta: ¿Dónde está la estación?', ['Recto y a la derecha.', 'A la izquierda.', 'Detrás del hotel.']),
  LQ('F|¿Cuánto cuestan estas naranjas?\nM|Dos euros el kilo.\nN|Pregunta: ¿Cuánto cuestan las naranjas?', ['Dos euros el kilo.', 'Doce euros el kilo.', 'Dos euros cada una.']),
  LQ('M|¿A qué hora empieza la película?\nF|A las nueve y media.\nN|Pregunta: ¿A qué hora empieza la película?', ['A las nueve y media.', 'A las nueve.', 'A las diez y media.']),
  LQ('F|¿Tienes hermanos?\nM|Sí, tengo una hermana. Se llama Clara y tiene quince años.\nN|Pregunta: ¿Cuántos años tiene Clara?', ['Quince.', 'Cinco.', 'Cincuenta.']),
  LQ('M|¿Qué tiempo hace hoy en Madrid?\nF|Hace frío y llueve un poco.\nN|Pregunta: ¿Qué tiempo hace en Madrid?', ['Hace frío y llueve.', 'Hace sol y calor.', 'Nieva mucho.']),
  LQ('F|¿Qué vas a hacer el domingo?\nM|Voy a visitar a mis abuelos en Segovia.\nN|Pregunta: ¿Qué va a hacer el hombre el domingo?', ['Visitar a sus abuelos.', 'Trabajar.', 'Ir al cine.']),
  LQ('M|Buenos días, ¿tiene esta camisa en talla grande?\nF|Sí, en azul y en blanco.\nN|Pregunta: ¿De qué colores tiene la camisa?', ['Azul y blanco.', 'Rojo y negro.', 'Verde.']),
  LQ('F|¿Dónde vives?\nM|Vivo en Sevilla, cerca del río.\nN|Pregunta: ¿Dónde vive el hombre?', ['En Sevilla.', 'En Valencia.', 'En Madrid.']),
  LQ('M|¿Qué te pasa?\nF|Me duele mucho la cabeza.\nN|Pregunta: ¿Qué le pasa a la mujer?', ['Le duele la cabeza.', 'Le duele la espalda.', 'Tiene hambre.']),
  LQ('F|¿A qué te dedicas?\nM|Soy profesor en un colegio.\nN|Pregunta: ¿Cuál es la profesión del hombre?', ['Profesor.', 'Médico.', 'Camarero.']),
], listening=True)

L2 = PART('l-avisos', 'listening', 'Comprensión auditiva — Tarea 2', 'Annonces et messages', 'Escuche el anuncio o el mensaje y elija la opción correcta.', 8, [
  LQ('N|Atención, señores pasajeros: el tren con destino a Barcelona sale del andén número cuatro.\nN|Pregunta: ¿De qué andén sale el tren?', ['Del andén cuatro.', 'Del andén catorce.', 'Del andén dos.']),
  LQ('N|El supermercado cierra en diez minutos. Gracias por su visita.\nN|Pregunta: ¿Qué pasa en diez minutos?', ['Cierra el supermercado.', 'Abre el supermercado.', 'Empieza una oferta.']),
  LQ('F|Hola, Juan, soy Elena. Mañana no puedo ir a la reunión. ¿La cambiamos al jueves? Llámame.\nN|Pregunta: ¿Qué quiere Elena?', ['Cambiar la reunión al jueves.', 'Ir a la reunión mañana.', 'Cenar con Juan.']),
  LQ('N|Hoy, en el centro comercial, todos los zapatos tienen un treinta por ciento de descuento.\nN|Pregunta: ¿Qué tiene descuento?', ['Los zapatos.', 'Las camisas.', 'La comida.']),
  LQ('M|Buenas tardes, llamo del restaurante El Molino. Su mesa está reservada para las nueve, para cuatro personas.\nN|Pregunta: ¿Para cuántas personas es la mesa?', ['Para cuatro.', 'Para nueve.', 'Para dos.']),
  LQ('N|Mañana, en el norte de España, va a llover. En el sur va a hacer sol y calor.\nN|Pregunta: ¿Qué tiempo va a hacer en el sur?', ['Sol y calor.', 'Lluvia.', 'Nieve.']),
  LQ('F|Bienvenidos al museo. La visita guiada empieza a las once en la puerta principal.\nN|Pregunta: ¿Dónde empieza la visita?', ['En la puerta principal.', 'En la cafetería.', 'En la tienda.']),
  LQ('M|Hola, mamá. Llego a casa a las ocho. ¿Preparo yo la cena?\nN|Pregunta: ¿A qué hora llega el hijo?', ['A las ocho.', 'A las once.', 'A las cuatro.']),
  LQ('N|Información para los clientes: la piscina del hotel está abierta de diez de la mañana a ocho de la tarde.\nN|Pregunta: ¿Cuándo cierra la piscina?', ['A las ocho de la tarde.', 'A las diez de la mañana.', 'A medianoche.']),
], listening=True)

L3 = PART('l-datos', 'listening', 'Comprensión auditiva — Tarea 3', 'Nombres, heures et lieux', 'Escuche y elija la información correcta.', 7, [
  LQ('F|Mi número de teléfono es el seis, cuatro, ocho, veinte, treinta y uno, cincuenta.\nN|Pregunta: ¿Cuál es el número?', ['648 20 31 50', '648 12 31 15', '684 20 13 50']),
  LQ('M|La clase de español es los martes y los jueves.\nN|Pregunta: ¿Qué días es la clase?', ['Martes y jueves.', 'Lunes y miércoles.', 'Sábados.']),
  LQ('F|El cumpleaños de mi madre es el dieciséis de mayo.\nN|Pregunta: ¿Cuándo es el cumpleaños?', ['El 16 de mayo.', 'El 6 de mayo.', 'El 16 de marzo.']),
  LQ('M|Son las cinco menos cuarto.\nN|Pregunta: ¿Qué hora es?', ['4:45', '5:15', '5:45']),
  LQ('F|Vivo en la calle Mayor, número setenta y dos.\nN|Pregunta: ¿En qué número vive?', ['72', '62', '27']),
  LQ('M|El billete cuesta treinta y cinco euros.\nN|Pregunta: ¿Cuánto cuesta el billete?', ['35 €', '25 €', '53 €']),
  LQ('F|Me llamo Begoña Jiménez. Jiménez: jota, i, eme, e, ene, e, zeta.\nN|Pregunta: ¿Cuál es el apellido?', ['Jiménez', 'Giménez', 'Ximénez']),
  LQ('M|La farmacia está entre el banco y el supermercado.\nN|Pregunta: ¿Dónde está la farmacia?', ['Entre el banco y el supermercado.', 'Al lado de la iglesia.', 'Enfrente del hotel.']),
], listening=True)

# ═════════════════════════ Expresión e interacción escritas ═════════════════════════
FORM = 'Usted se llama Claire Martín, tiene 28 años, es francesa, vive en Lyon y quiere viajar por España.\nFORMULARIO DE INSCRIPCIÓN — Escuela de idiomas'
W1 = PART('w-formulario', 'writing', 'Expresión escrita — Tarea 1', 'Remplir un formulaire', 'Complete el formulario: elija la respuesta adecuada.', 3, [
  RQ(['Martín', '28 años', 'francesa', 'Calle Sol, 5'], None, f'{FORM}\n★ Apellido:'),
  RQ(['francesa', 'Lyon', '28', 'Martín'], None, f'{FORM}\n★ Nacionalidad:'),
  RQ(['28', 'veintiocho de mayo', 'mayo', 'Martín'], None, f'{FORM}\n★ Edad:'),
  RQ(['Porque quiero viajar por España.', 'Porque es martes.', 'Porque soy alta.', 'Porque tengo veintiocho.'], None, f'{FORM}\n★ ¿Por qué quiere estudiar español?'),
])

W2 = PART('w-mensaje', 'writing', 'Expresión escrita — Tarea 2', 'Un message court', 'Lea la situación y elija el mensaje mejor escrito.', 2, [
  RQ(['¡Hola, Ana! Este sábado es mi cumpleaños. ¿Quieres venir a mi casa a las ocho? Vamos a cenar y bailar. ¡Un beso!',
      '¡Hola, Ana! Este sábado son mi cumpleaños. ¿Quieres venir en mi casa a ocho? Vamos cenar y bailar.',
      'Ana, sábado cumpleaños casa ocho cenar bailar.',
      '¡Hola, Ana! El sábado es tu cumpleaños. ¿Vienes a tu casa? Yo no voy a ir.'],
     None, '★ Situación: invita a tu amiga Ana a tu cumpleaños (día, hora, lugar, actividad).'),
  RQ(['Querido Pablo: estoy en Granada con mi familia. El hotel es muy bonito y hace sol. Mañana vamos a visitar la Alhambra. Un abrazo, Sara.',
      'Querido Pablo: soy en Granada con mi familia. El hotel está muy bonito y hace sol. Mañana vamos visitar la Alhambra.',
      'Pablo: Granada. Familia. Hotel bonito. Sol. Alhambra.',
      'Querido Pablo: estoy en Granada. Ayer voy a visitar la Alhambra mañana. El hotel es frío y hace nieve.'],
     None, '★ Situación: escribe una postal a tu amigo Pablo desde tus vacaciones (dónde estás, con quién, el tiempo, un plan).'),
  RQ(['Buenos días: me llamo Hugo Leroy y quiero reservar una habitación doble para el 10 y el 11 de julio. Muchas gracias.',
      'Buenos días: me llamo Hugo Leroy y quiero reservo una habitación doble para el 10 y el 11 de julio.',
      'Hola, quiero habitación. Gracias.',
      'Buenos días: me llamo Hugo Leroy y tengo una habitación doble en el 10 de julio. Adiós.'],
     None, '★ Situación: escribe al hotel para reservar una habitación (nombre, tipo de habitación, fechas).'),
])

PARTS = [R1, R2, R3, L1, L2, L3, W1, W2]
rea = sum(p['count'] for p in PARTS if p['section'] == 'reading')
lis = sum(p['count'] for p in PARTS if p['section'] == 'listening')
wri = sum(p['count'] for p in PARTS if p['section'] == 'writing')
assert (rea, lis, wri) == (25, 25, 5), (rea, lis, wri)
bank = {
  'slug': 'delea1',
  'level': 'DELEA1',
  'contentVersion': '2026.11.23',
  'notice': 'Questions rédigées par Koto Quest au format de l’examen officiel du DELE A1 (Instituto Cervantes : types d’épreuves, consignes en espagnol, notation sur 100 en deux groupes). L’expression écrite se fait par choix multiple et l’expression orale n’est pas évaluée : le groupe 2 est noté sur l’écoute. Ce ne sont pas des questions officielles.',
  'parts': PARTS,
}
json.dump(bank, open(os.path.join(ROOT, 'content/exams/delea1.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
EN = {
  bank['notice']: 'Questions written by Koto Quest in the format of the official DELE A1 exam (Instituto Cervantes: question types, instructions in Spanish, scoring out of 100 in two groups). Written expression is multiple choice and speaking is not assessed: group 2 is marked on listening. They are not official questions.',
  'Un courriel': 'An email', 'Panneaux et annonces': 'Signs and adverts', 'Messages courts': 'Short messages',
  'Dialogues courts': 'Short dialogues', 'Annonces et messages': 'Notices and messages', 'Nombres, heures et lieux': 'Numbers, times and places',
  'Remplir un formulaire': 'Filling in a form', 'Un message court': 'A short message',
}
P_DICT = os.path.join(ROOT, 'content/i18n/en/content.json')
d = json.load(open(P_DICT, encoding='utf-8'))
for k, v in EN.items():
    if k in d and d[k] != v:
        raise SystemExit(f'traduction existante différente : {k} → {d[k]} / {v}')
d.update(EN)
json.dump(d, open(P_DICT, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(f"DELE A1 : {sum(len(p['questions']) for p in PARTS)} questions en banque ; examen de {rea} + {lis} + {wri} questions")
