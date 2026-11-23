# Niveau DELE A2 (espagnol, CECRL A2) : 8 étapes sur la route de Barcelone, leçons et examen blanc (français + anglais).
# Mode histoire : la deuxième sortie de Don Quichotte, de la Manche à la plage de Barcelone (voir gen-story.py).
# Les notions sont en espagnol (front) avec leur sens en français ; la traduction anglaise du sens sert à l'interface en anglais.
# Usage : python3 scripts/delea2-level.py   (réécrit content/delea2/delea2.json ; le DELE A1 doit déjà exister)
from es_common import *

REGION = 'Route de Barcelone'

# ═════════════════════════ 1 : la deuxième sortie — le passé composé (pretérito perfecto) ═════════════════════════
W1 = WORLD('delea2-w1', ('La deuxième sortie', 'The second sally'), REGION,
  ('Raconter ce qu’on a fait aujourd’hui ou cette semaine avec le pretérito perfecto (he hablado), les participes irréguliers, ya et todavía no.', 'Say what you have done today or this week with the pretérito perfecto (he hablado), irregular participles, ya and todavía no.'),
  (('La Lamia du torrent', 'The Lamia of the torrent'), 'ñ', ('Au bord de la rivière, la Lamia peigne ses cheveux avec un peigne d’or et ne laisse passer que ceux qui savent dire ce qu’ils ont déjà fait. Raconte ta journée sans te tromper de participe !', 'On the riverbank, the Lamia combs her hair with a golden comb and only lets through those who can say what they have already done. Tell her about your day without mixing up a participle!')),
  [CH('delea2-w1-c1', ('Qu’as-tu fait aujourd’hui ?', 'What have you done today?'), [
    L('es-perfecto', ('Le passé composé : he hablado', 'The present perfect: he hablado'), ('Former le pretérito perfecto et dire ce qu’on a fait aujourd’hui.', 'Form the pretérito perfecto and say what you have done today.'), 9, [
        ('Le pretérito perfecto = haber au présent + participe : he, has, ha, hemos, habéis, han + hablado. He comido (j’ai mangé), ¿Has dormido bien? (as-tu bien dormi ?).', 'The pretérito perfecto = haber in the present + past participle: he, has, ha, hemos, habéis, han + hablado. He comido (I have eaten), ¿Has dormido bien? (did you sleep well?).'),
        ('Le participe régulier : -ar → -ado (hablar → hablado), -er et -ir → -ido (comer → comido, vivir → vivido). Il ne s’accorde jamais avec haber.', 'Regular participles: -ar → -ado (hablar → hablado), -er and -ir → -ido (comer → comido, vivir → vivido). It never agrees with haber.'),
        ('On l’emploie pour un passé dans une période qui n’est pas finie : hoy (aujourd’hui), esta mañana (ce matin), esta semana (cette semaine), este año (cette année).', 'It is used for the past within a period that is not over: hoy (today), esta mañana (this morning), esta semana (this week), este año (this year).'),
      ], [
        SG('perfecto', 'he / has / ha + participio', ('j’ai / tu as / il a + participe (passé composé)', 'I have / you have / he has + participle (present perfect)')),
        SG('participio', '-ado / -ido', ('terminaisons du participe passé', 'past participle endings')),
        S('esta-manana', 'esta mañana', ('ce matin', 'this morning')),
        S('esta-semana', 'esta semana', ('cette semaine', 'this week')),
        S('este-ano', 'este año', ('cette année', 'this year')),
        S('salir', 'salir', ('sortir, partir', 'to go out, to leave')),
        S('preparar', 'preparar', ('préparer', 'to prepare')),
        S('la-maleta', 'la maleta', ('la valise', 'the suitcase')),
      ], [
        x('Esta mañana hemos salido del pueblo muy temprano.', 'Ce matin, nous sommes partis du village très tôt.', 'This morning we left the village very early.'),
        x('¿Has preparado la maleta, Sancho? — Sí, ya la he preparado.', 'As-tu préparé la valise, Sancho ? — Oui, je l’ai déjà préparée.', 'Have you packed the suitcase, Sancho? — Yes, I’ve already packed it.'),
      ], [
        FB(CHOOSE, 'Hoy ＿ comido en una venta.', ['hemos', 'somos', 'tenemos'], 'hemos', ('Passé composé : haber (hemos) + participe.', 'Present perfect: haber (hemos) + participle.'), ('Aujourd’hui, nous avons mangé dans une auberge.', 'Today we have eaten at an inn.')),
        FB(CHOOSE, '¿＿ dormido bien, señor?', ['Ha', 'Es', 'Está'], 'Ha', ('Avec usted : ha + participe.', 'With usted: ha + participle.'), ('Avez-vous bien dormi, monsieur ?', 'Did you sleep well, sir?')),
        FB(CHOOSE, 'Esta semana he ＿ mucho.', ['trabajado', 'trabajo', 'trabajar'], 'trabajado', ('Trabajar → trabajado.', 'Trabajar → trabajado.'), ('Cette semaine, j’ai beaucoup travaillé.', 'This week I have worked a lot.')),
        TF('Esta mañana he desayunado pan con aceite.', ('La personne n’a pas encore pris son petit-déjeuner.', 'The person hasn’t had breakfast yet.'), FAUX, ('He desayunado = j’ai pris mon petit-déjeuner.', 'He desayunado = I have had breakfast.')),
      ]),
    L('es-participios', ('Hecho, dicho, visto : les participes irréguliers', 'Hecho, dicho, visto: irregular participles'), ('Employer les participes irréguliers les plus courants.', 'Use the most common irregular participles.'), 9, [
        ('Participes irréguliers à connaître : hacer → hecho, decir → dicho, ver → visto, escribir → escrito, volver → vuelto, poner → puesto, abrir → abierto, romper → roto, morir → muerto.', 'Irregular participles to learn: hacer → hecho, decir → dicho, ver → visto, escribir → escrito, volver → vuelto, poner → puesto, abrir → abierto, romper → roto, morir → muerto.'),
        ('Les pronoms se placent avant haber : Lo he visto (je l’ai vu), Me he levantado tarde (je me suis levé tard).', 'Pronouns go before haber: Lo he visto (I have seen it), Me he levantado tarde (I got up late).'),
        ('Ya = déjà ; todavía no = pas encore. ¿Ya has comido? — No, todavía no.', 'Ya = already; todavía no = not yet. ¿Ya has comido? — No, todavía no.'),
      ], [
        S('hecho', 'hecho (hacer)', ('fait (participe de hacer)', 'done, made (participle of hacer)')),
        S('dicho', 'dicho (decir)', ('dit (participe de decir)', 'said (participle of decir)')),
        S('visto', 'visto (ver)', ('vu (participe de ver)', 'seen (participle of ver)')),
        S('escrito', 'escrito (escribir)', ('écrit (participe de escribir)', 'written (participle of escribir)')),
        S('vuelto', 'vuelto (volver)', ('revenu (participe de volver)', 'come back (participle of volver)')),
        S('roto', 'roto (romper)', ('cassé (participe de romper)', 'broken (participle of romper)')),
        S('ya', 'ya', ('déjà', 'already')),
        S('todavia-no', 'todavía no', ('pas encore', 'not yet')),
      ], [
        x('Don Quijote ha roto su lanza otra vez.', 'Don Quichotte a encore cassé sa lance.', 'Don Quixote has broken his lance again.'),
        x('¿Ya has escrito a Dulcinea? — No, todavía no le he escrito.', 'As-tu déjà écrit à Dulcinée ? — Non, je ne lui ai pas encore écrit.', 'Have you written to Dulcinea yet? — No, I haven’t written to her yet.'),
      ], [
        FB(CHOOSE, '¿Qué has ＿ hoy?', ['hecho', 'hacido', 'hacer'], 'hecho', ('Hacer → hecho (irrégulier).', 'Hacer → hecho (irregular).'), ('Qu’as-tu fait aujourd’hui ?', 'What have you done today?')),
        FB(CHOOSE, 'Nunca he ＿ el mar.', ['visto', 'veído', 'vido'], 'visto', ('Ver → visto.', 'Ver → visto.'), ('Je n’ai jamais vu la mer.', 'I have never seen the sea.')),
        FB(CHOOSE, 'Sancho todavía no ha ＿ a casa.', ['vuelto', 'volvido', 'volvado'], 'vuelto', ('Volver → vuelto.', 'Volver → vuelto.'), ('Sancho n’est pas encore rentré à la maison.', 'Sancho hasn’t come home yet.')),
        DC(ANSWER, [('Teresa', '¿Ya habéis comido?')], ('Teresa demande si vous avez déjà mangé (ce n’est pas le cas).', 'Teresa asks if you have eaten yet (you haven’t).'), ['No, todavía no.', 'Sí, mañana.', 'No, ya.'], 'No, todavía no.', ('Pas encore : todavía no.', 'Not yet: todavía no.')),
      ]),
  ]),
  CH('delea2-w1-c2', ('As-tu déjà… ?', 'Have you ever…?'), [
    L('es-experiencias', ('As-tu déjà été à Barcelone ? alguna vez, nunca', 'Have you ever been to Barcelona? alguna vez, nunca'), ('Parler de ses expériences de vie.', 'Talk about your life experiences.'), 9, [
        ('Pour une expérience : ¿Has estado alguna vez en…? (as-tu déjà été à… ?). Réponses : Sí, una vez / dos veces / muchas veces ; No, nunca (jamais).', 'For an experience: ¿Has estado alguna vez en…? (have you ever been to…?). Answers: Sí, una vez / dos veces / muchas veces; No, nunca (never).'),
        ('Nunca avant le verbe se suffit : Nunca he montado a caballo. Après le verbe, il faut no : No he montado nunca a caballo.', 'Nunca before the verb is enough: Nunca he montado a caballo. After the verb, you need no: No he montado nunca a caballo.'),
        ('Estar en un lugar (avoir été quelque part), probar (goûter), conocer (connaître une personne ou un lieu), montar a caballo (monter à cheval).', 'Estar en un lugar (to have been somewhere), probar (to taste, try), conocer (to know a person or place), montar a caballo (to ride a horse).'),
      ], [
        S('alguna-vez', 'alguna vez', ('déjà (une fois dans sa vie)', 'ever')),
        S('nunca', 'nunca', ('jamais', 'never')),
        S('una-vez', 'una vez / dos veces', ('une fois / deux fois', 'once / twice')),
        S('probar-gusto', 'probar', ('goûter, essayer', 'to taste, to try')),
        S('conocer', 'conocer', ('connaître', 'to know (people, places)')),
        S('montar-a-caballo', 'montar a caballo', ('monter à cheval', 'to ride a horse')),
        S('el-mar', 'el mar', ('la mer', 'the sea')),
        S('el-caballo', 'el caballo', ('le cheval', 'the horse')),
      ], [
        x('¿Has estado alguna vez en Barcelona? — No, nunca. ¡Vamos a conocerla!', 'As-tu déjà été à Barcelone ? — Non, jamais. Allons la découvrir !', 'Have you ever been to Barcelona? — No, never. Let’s go and see it!'),
        x('Rocinante es el caballo de don Quijote. Sancho nunca ha montado a caballo.', 'Rossinante est le cheval de don Quichotte. Sancho n’est jamais monté à cheval.', 'Rocinante is Don Quixote’s horse. Sancho has never ridden a horse.'),
      ], [
        DC(ANSWER, [('Sancho', '¿Has probado alguna vez el gazpacho?')], ('Sancho te demande si tu as déjà goûté le gazpacho (oui, deux fois).', 'Sancho asks if you have ever tried gazpacho (yes, twice).'), ['Sí, dos veces.', 'Sí, mañana.', 'No, ya.'], 'Sí, dos veces.', ('Expérience : una vez, dos veces…', 'Experience: una vez, dos veces…')),
        FB(CHOOSE, 'No he estado ＿ en Italia.', ['nunca', 'ya', 'alguna'], 'nunca', ('No + verbe + nunca.', 'No + verb + nunca.'), ('Je n’ai jamais été en Italie.', 'I have never been to Italy.')),
        FB(CHOOSE, '¿Has ＿ alguna vez a una persona famosa?', ['conocido', 'sabido', 'probado'], 'conocido', ('Une personne : conocer.', 'A person: conocer.'), ('As-tu déjà rencontré une personne célèbre ?', 'Have you ever met a famous person?')),
        order(('Remets dans l’ordre : « Je n’ai jamais vu la mer. »', 'Put in order: “I have never seen the sea.”'), ['Nunca', 'he', 'visto', 'el', 'mar.'], ('Nunca + haber + participe.', 'Nunca + haber + participle.')),
      ]),
  ])])

# ═════════════════════════ 2 : le récit de Sancho — le passé simple (pretérito indefinido) ═════════════════════════
W2 = WORLD('delea2-w2', ('Le récit de Sancho', 'Sancho’s tale'), REGION,
  ('Raconter des événements terminés avec le pretérito indefinido (hablé, comí), ses formes irrégulières (fui, tuve, hice) et retracer une biographie.', 'Tell finished events with the pretérito indefinido (hablé, comí), its irregular forms (fui, tuve, hice) and trace a biography.'),
  (('Le Tragaldabas glouton', 'The gluttonous Tragaldabas'), 'á', ('Le Tragaldabas, ogre goinfre des contes espagnols, a vidé la cuisine de l’auberge pendant la nuit. Il n’écoute que les belles histoires : raconte-lui hier, l’an dernier et toute ta vie au passé !', 'The Tragaldabas, the greedy ogre of Spanish tales, emptied the inn’s kitchen during the night. It only listens to good stories: tell it about yesterday, last year and your whole life in the past!')),
  [CH('delea2-w2-c1', ('Hier, à l’auberge', 'Yesterday, at the inn'), [
    L('es-indefinido', ('Le passé simple : hablé, comí, viví', 'The simple past: hablé, comí, viví'), ('Conjuguer les verbes réguliers au pretérito indefinido.', 'Conjugate regular verbs in the pretérito indefinido.'), 9, [
        ('-ar : hablé, hablaste, habló, hablamos, hablasteis, hablaron. -er / -ir : comí, comiste, comió, comimos, comisteis, comieron (vivir : viví, viviste, vivió…).', '-ar: hablé, hablaste, habló, hablamos, hablasteis, hablaron. -er / -ir: comí, comiste, comió, comimos, comisteis, comieron (vivir: viví, viviste, vivió…).'),
        ('L’indefinido raconte une action terminée dans un temps fini : ayer (hier), anoche (hier soir), la semana pasada, el año pasado, en 2010, hace dos días (il y a deux jours).', 'The indefinido tells a finished action in a finished time: ayer (yesterday), anoche (last night), la semana pasada, el año pasado, en 2010, hace dos días (two days ago).'),
        ('Attention à l’accent : hablo (je parle) ≠ habló (il a parlé). Et hablamos sert au présent comme au passé.', 'Watch the accent: hablo (I speak) ≠ habló (he spoke). And hablamos is both present and past.'),
      ], [
        SG('indefinido', 'hablé / comí / viví', ('je parlai / je mangeai / je vécus (passé simple)', 'I spoke / I ate / I lived (simple past)')),
        S('ayer', 'ayer', ('hier', 'yesterday')),
        S('anoche', 'anoche', ('hier soir', 'last night')),
        S('el-ano-pasado', 'el año pasado', ('l’année dernière', 'last year')),
        S('la-semana-pasada', 'la semana pasada', ('la semaine dernière', 'last week')),
        S('hace-dos-dias', 'hace dos días', ('il y a deux jours', 'two days ago')),
        S('llegar', 'llegar', ('arriver', 'to arrive')),
        S('cenar', 'cenar', ('dîner', 'to have dinner')),
      ], [
        x('Anoche cenamos en una venta y Sancho comió muchísimo.', 'Hier soir, nous avons dîné dans une auberge et Sancho a énormément mangé.', 'Last night we had dinner at an inn and Sancho ate an awful lot.'),
        x('Llegamos a Zaragoza hace dos días.', 'Nous sommes arrivés à Saragosse il y a deux jours.', 'We arrived in Zaragoza two days ago.'),
      ], [
        FB(CHOOSE, 'Ayer ＿ con Dulcinea por teléfono.', ['hablé', 'hablo', 'he hablado'], 'hablé', ('Ayer (temps fini) : indefinido.', 'Ayer (finished time): indefinido.'), ('Hier, j’ai parlé avec Dulcinée au téléphone.', 'Yesterday I spoke to Dulcinea on the phone.')),
        FB(CHOOSE, 'El año pasado mis padres ＿ en Sevilla.', ['vivieron', 'vivimos', 'vivió'], 'vivieron', ('Ellos : -ieron.', 'Ellos: -ieron.'), ('L’an dernier, mes parents ont vécu à Séville.', 'Last year my parents lived in Seville.')),
        FB(CHOOSE, 'Don Quijote ＿ a la venta por la noche.', ['llegó', 'llego', 'llegué'], 'llegó', ('Él : -ó (avec accent).', 'Él: -ó (with an accent).'), ('Don Quichotte est arrivé à l’auberge la nuit.', 'Don Quixote arrived at the inn at night.')),
        TF('Comimos en el restaurante hace tres días.', ('Le repas a eu lieu il y a trois jours.', 'The meal was three days ago.'), VRAI, ('Hace tres días = il y a trois jours.', 'Hace tres días = three days ago.')),
      ]),
    L('es-indefinido-irregular', ('Fui, tuve, hice : les passés irréguliers', 'Fui, tuve, hice: irregular pasts'), ('Employer les indefinidos irréguliers les plus courants.', 'Use the most common irregular indefinidos.'), 10, [
        ('Ser et ir ont la même forme : fui, fuiste, fue, fuimos, fuisteis, fueron. Fui a Toledo (je suis allé à Tolède) ; Fue un día largo (ce fut une longue journée).', 'Ser and ir share the same forms: fui, fuiste, fue, fuimos, fuisteis, fueron. Fui a Toledo (I went to Toledo); Fue un día largo (it was a long day).'),
        ('Radical irrégulier et terminaisons sans accent : tener → tuve, estar → estuve, hacer → hice (hizo), poder → pude, poner → puse, venir → vine, querer → quise.', 'Irregular stem and endings without accents: tener → tuve, estar → estuve, hacer → hice (hizo), poder → pude, poner → puse, venir → vine, querer → quise.'),
        ('Decir → dije, dijiste, dijo, dijimos, dijisteis, dijeron (pas de i à la 3e personne du pluriel). Dar → di, diste, dio. Ver → vi, viste, vio.', 'Decir → dije, dijiste, dijo, dijimos, dijisteis, dijeron (no i in the 3rd person plural). Dar → di, diste, dio. Ver → vi, viste, vio.'),
      ], [
        SG('fui', 'fui / fuiste / fue', ('j’allai, je fus (ir et ser au passé simple)', 'I went, I was (ir and ser in the simple past)')),
        SG('tuve', 'tuve / estuve / hice', ('j’eus / je fus / je fis (passés irréguliers)', 'I had / I was / I did (irregular pasts)')),
        S('dije', 'dije (decir)', ('je dis (passé simple de decir)', 'I said (simple past of decir)')),
        S('vine', 'vine (venir)', ('je vins (passé simple de venir)', 'I came (simple past of venir)')),
        S('pude', 'pude (poder)', ('je pus (passé simple de poder)', 'I could (simple past of poder)')),
        S('la-fiesta', 'la fiesta', ('la fête', 'the party, the festival')),
        S('el-viaje', 'el viaje', ('le voyage', 'the trip, the journey')),
        S('el-pueblo', 'el pueblo', ('le village', 'the village')),
      ], [
        x('El sábado fuimos a la fiesta del pueblo y estuvimos allí hasta las dos.', 'Samedi, nous sommes allés à la fête du village et nous y sommes restés jusqu’à deux heures.', 'On Saturday we went to the village festival and stayed there until two.'),
        x('Sancho no pudo dormir: hizo mucho calor.', 'Sancho n’a pas pu dormir : il a fait très chaud.', 'Sancho couldn’t sleep: it was very hot.'),
      ], [
        FB(CHOOSE, 'Ayer ＿ al mercado con mi madre.', ['fui', 'fue', 'iba'], 'fui', ('Yo + ir au passé : fui.', 'Yo + ir in the past: fui.'), ('Hier, je suis allé au marché avec ma mère.', 'Yesterday I went to the market with my mother.')),
        FB(CHOOSE, 'El viaje ＿ muy divertido.', ['fue', 'fui', 'estuvo de'], 'fue', ('Ser, 3e personne : fue.', 'Ser, 3rd person: fue.'), ('Le voyage a été très amusant.', 'The trip was great fun.')),
        FB(CHOOSE, 'El lunes ＿ que trabajar mucho.', ['tuve', 'tení', 'tuvé'], 'tuve', ('Tener → tuve (sans accent).', 'Tener → tuve (no accent).'), ('Lundi, j’ai dû beaucoup travailler.', 'On Monday I had to work a lot.')),
        FB(CHOOSE, 'Ellos me ＿ la verdad.', ['dijeron', 'dijieron', 'decieron'], 'dijeron', ('Decir → dijeron (sans i).', 'Decir → dijeron (no i).'), ('Ils m’ont dit la vérité.', 'They told me the truth.')),
      ]),
  ]),
  CH('delea2-w2-c2', ('La vie de Cervantes', 'Cervantes’s life'), [
    L('es-biografia', ('Une biographie : nació, se casó, murió', 'A biography: nació, se casó, murió'), ('Raconter les grandes étapes d’une vie.', 'Tell the main stages of a life.'), 9, [
        ('Les verbes de la biographie : nacer (naître) → nació, estudiar → estudió, casarse (se marier) → se casó, tener hijos → tuvo, morir (mourir) → murió.', 'Biography verbs: nacer (to be born) → nació, estudiar → estudió, casarse (to get married) → se casó, tener hijos → tuvo, morir (to die) → murió.'),
        ('Les dates : en 1547, el 23 de abril de 1616 ; a los veinte años (à vingt ans) ; dos años después (deux ans plus tard) ; luego (ensuite) ; al final (à la fin).', 'Dates: en 1547, el 23 de abril de 1616; a los veinte años (at twenty); dos años después (two years later); luego (then); al final (in the end).'),
        ('Morir et dormir changent au passé à la 3e personne : murió, murieron ; durmió, durmieron.', 'Morir and dormir change in the past in the 3rd person: murió, murieron; durmió, durmieron.'),
      ], [
        S('nacer', 'nacer', ('naître', 'to be born')),
        S('casarse', 'casarse', ('se marier', 'to get married')),
        S('morir', 'morir', ('mourir', 'to die')),
        S('a-los-veinte', 'a los veinte años', ('à vingt ans', 'at the age of twenty')),
        S('anos-despues', 'dos años después', ('deux ans plus tard', 'two years later')),
        S('luego', 'luego', ('ensuite, puis', 'then, afterwards')),
        S('el-escritor', 'el escritor / la escritora', ('l’écrivain / l’écrivaine', 'the writer')),
        S('la-novela', 'la novela', ('le roman', 'the novel')),
      ], [
        x('Miguel de Cervantes nació en Alcalá de Henares en 1547.', 'Miguel de Cervantes est né à Alcalá de Henares en 1547.', 'Miguel de Cervantes was born in Alcalá de Henares in 1547.'),
        x('Escribió la novela de don Quijote y murió en Madrid en 1616.', 'Il a écrit le roman de don Quichotte et il est mort à Madrid en 1616.', 'He wrote the novel of Don Quixote and died in Madrid in 1616.'),
      ], [
        FB(CHOOSE, 'Cervantes ＿ en 1547.', ['nació', 'nace', 'nacía'], 'nació', ('Événement daté : indefinido.', 'Dated event: indefinido.'), ('Cervantes est né en 1547.', 'Cervantes was born in 1547.')),
        FB(CHOOSE, 'Mis abuelos se ＿ en 1970.', ['casaron', 'casó', 'casamos'], 'casaron', ('Ellos : se casaron.', 'Ellos: se casaron.'), ('Mes grands-parents se sont mariés en 1970.', 'My grandparents got married in 1970.')),
        FB(CHOOSE, 'El escritor ＿ en 1616.', ['murió', 'morió', 'muró'], 'murió', ('Morir → murió.', 'Morir → murió.'), ('L’écrivain est mort en 1616.', 'The writer died in 1616.')),
        order(('Remets dans l’ordre : « À vingt ans, il est parti en Italie. »', 'Put in order: “At twenty, he left for Italy.”'), ['A', 'los', 'veinte', 'años', 'se', 'fue', 'a', 'Italia.'], ('A los + âge + años, puis le verbe.', 'A los + age + años, then the verb.')),
      ]),
  ])])

# ═════════════════════════ 3 : quand j'étais petit — l'imparfait ═════════════════════════
W3 = WORLD('delea2-w3', ('Les souvenirs d’Aragon', 'Memories of Aragon'), REGION,
  ('Évoquer ses souvenirs et les habitudes passées avec l’imparfait (hablaba, comía, era, iba), décrire un lieu d’autrefois et l’opposer au passé simple.', 'Recall memories and past habits with the imperfect (hablaba, comía, era, iba), describe a place in the past and contrast it with the simple past.'),
  (('L’Homme du sac', 'The Sack Man'), 'é', ('Dans les villages d’Aragon, on menaçait les enfants désobéissants de l’Homme du sac. Ce soir, il rôde dans la vieille ferme et vole les souvenirs des anciens : rends-les-leur en racontant comment c’était avant.', 'In the villages of Aragon, naughty children were threatened with the Sack Man. Tonight he prowls the old farm and steals the elders’ memories: give them back by telling how things used to be.')),
  [CH('delea2-w3-c1', ('Quand j’étais petit', 'When I was little'), [
    L('es-imperfecto', ('L’imparfait : hablaba, comía', 'The imperfect: hablaba, comía'), ('Raconter ses habitudes passées avec l’imparfait.', 'Talk about past habits with the imperfect.'), 9, [
        ('-ar : hablaba, hablabas, hablaba, hablábamos, hablabais, hablaban. -er / -ir : comía, comías, comía, comíamos, comíais, comían.', '-ar: hablaba, hablabas, hablaba, hablábamos, hablabais, hablaban. -er / -ir: comía, comías, comía, comíamos, comíais, comían.'),
        ('Seulement trois verbes irréguliers : ser → era, ir → iba, ver → veía.', 'Only three irregular verbs: ser → era, ir → iba, ver → veía.'),
        ('L’imparfait sert aux habitudes passées : de pequeño (enfant), antes (avant), todos los veranos (tous les étés), a menudo (souvent), cada día (chaque jour).', 'The imperfect is used for past habits: de pequeño (as a child), antes (before), todos los veranos (every summer), a menudo (often), cada día (every day).'),
      ], [
        SG('imperfecto', 'hablaba / comía / vivía', ('je parlais / je mangeais / je vivais (imparfait)', 'I used to speak / eat / live (imperfect)')),
        SG('era-iba', 'era / iba / veía', ('j’étais / j’allais / je voyais', 'I was / I used to go / I used to see')),
        S('de-pequeno', 'de pequeño / de pequeña', ('quand j’étais petit·e', 'as a child')),
        S('antes', 'antes', ('avant, autrefois', 'before, in the past')),
        S('a-menudo', 'a menudo', ('souvent', 'often')),
        S('cada-dia', 'cada día', ('tous les jours', 'every day')),
        S('jugar', 'jugar', ('jouer', 'to play')),
        S('el-campo', 'el campo', ('la campagne', 'the countryside')),
      ], [
        x('De pequeño, vivía en el campo y jugaba en el río cada día.', 'Quand j’étais petit, je vivais à la campagne et je jouais dans la rivière chaque jour.', 'As a child, I lived in the countryside and played in the river every day.'),
        x('Antes don Quijote leía libros de caballerías toda la noche.', 'Avant, don Quichotte lisait des romans de chevalerie toute la nuit.', 'Don Quixote used to read books of chivalry all night.'),
      ], [
        FB(CHOOSE, 'De pequeña, ＿ al colegio a pie.', ['iba', 'fui', 'voy'], 'iba', ('Habitude passée : imparfait (ir → iba).', 'Past habit: imperfect (ir → iba).'), ('Quand j’étais petite, j’allais à l’école à pied.', 'As a child I walked to school.')),
        FB(CHOOSE, 'Antes mis abuelos ＿ en un pueblo pequeño.', ['vivían', 'vivieron', 'viven'], 'vivían', ('Antes : imparfait.', 'Antes: imperfect.'), ('Autrefois, mes grands-parents vivaient dans un petit village.', 'My grandparents used to live in a small village.')),
        FB(CHOOSE, 'Cuando yo ＿ niño, no me gustaban las verduras.', ['era', 'fui', 'estaba'], 'era', ('Ser à l’imparfait : era.', 'Ser in the imperfect: era.'), ('Quand j’étais enfant, je n’aimais pas les légumes.', 'When I was a child, I didn’t like vegetables.')),
        TF('De pequeño, jugaba al fútbol todos los sábados.', ('C’était une habitude.', 'It was a habit.'), VRAI, ('Todos los sábados + imparfait = habitude.', 'Todos los sábados + imperfect = habit.')),
      ]),
    L('es-describir-pasado', ('Comment c’était : había, era, estaba', 'What it was like: había, era, estaba'), ('Décrire un lieu, une personne ou une situation dans le passé.', 'Describe a place, a person or a situation in the past.'), 9, [
        ('Hay → había (il y avait) : En el pueblo había una plaza y dos fuentes. Avec un pluriel aussi : había.', 'Hay → había (there was / there were): En el pueblo había una plaza y dos fuentes. With a plural too: había.'),
        ('Pour décrire au passé : era (c’était, il était — description durable), estaba (état ou lieu), tenía (il avait), llevaba (il portait).', 'To describe in the past: era (it was, he was — lasting description), estaba (state or place), tenía (he had), llevaba (he wore).'),
        ('Les objets d’autrefois : la radio, la carta (la lettre), la vela (la bougie), el pozo (le puits), la granja (la ferme).', 'Things from the past: la radio, la carta (the letter), la vela (the candle), el pozo (the well), la granja (the farm).'),
      ], [
        SG('habia', 'había', ('il y avait', 'there was, there were')),
        S('la-granja', 'la granja', ('la ferme', 'the farm')),
        S('la-fuente', 'la fuente', ('la fontaine, la source', 'the fountain, the spring')),
        S('el-pozo', 'el pozo', ('le puits', 'the well')),
        S('la-vela', 'la vela', ('la bougie', 'the candle')),
        S('la-carta', 'la carta', ('la lettre (courrier)', 'the letter (mail)')),
        S('tranquilo', 'tranquilo / tranquila', ('calme', 'quiet, calm')),
        S('la-luz', 'la luz', ('la lumière, l’électricité', 'the light, electricity')),
      ], [
        x('En la granja no había luz: leíamos con una vela.', 'À la ferme, il n’y avait pas d’électricité : nous lisions à la bougie.', 'There was no electricity on the farm: we read by candlelight.'),
        x('El pueblo era pequeño y muy tranquilo. En la plaza había una fuente.', 'Le village était petit et très calme. Sur la place, il y avait une fontaine.', 'The village was small and very quiet. In the square there was a fountain.'),
      ], [
        FB(CHOOSE, 'En mi calle ＿ dos panaderías.', ['había', 'habían', 'era'], 'había', ('Había ne se met pas au pluriel.', 'Había doesn’t go in the plural.'), ('Dans ma rue, il y avait deux boulangeries.', 'There were two bakeries in my street.')),
        FB(CHOOSE, 'Mi abuelo ＿ el pelo blanco y siempre llevaba sombrero.', ['tenía', 'tuvo', 'era'], 'tenía', ('Description au passé : imparfait.', 'Description in the past: imperfect.'), ('Mon grand-père avait les cheveux blancs et portait toujours un chapeau.', 'My grandfather had white hair and always wore a hat.')),
        FB(CHOOSE, 'La casa ＿ muy grande y tenía un pozo.', ['era', 'estaba', 'había'], 'era', ('Description durable : ser → era.', 'Lasting description: ser → era.'), ('La maison était très grande et avait un puits.', 'The house was very big and had a well.')),
        DC(ANSWER, [('Nieta', 'Abuela, ¿cómo era el pueblo antes?')], ('La petite-fille demande comment était le village autrefois.', 'The granddaughter asks what the village used to be like.'), ['Era muy tranquilo y había pocos coches.', 'Fue muy tranquilo ayer.', 'Es tranquilo mañana.'], 'Era muy tranquilo y había pocos coches.', ('Description au passé : era, había.', 'Description in the past: era, había.')),
      ]),
  ]),
  CH('delea2-w3-c2', ('Ce soir-là…', 'That evening…'), [
    L('es-imperfecto-indefinido', ('Je dormais quand… : imparfait ou passé simple', 'I was sleeping when…: imperfect or simple past'), ('Raconter une histoire en distinguant le décor (imparfait) et les événements (passé simple).', 'Tell a story distinguishing the background (imperfect) from the events (simple past).'), 10, [
        ('L’imparfait pose le décor et ce qui était en cours ; l’indefinido raconte ce qui est arrivé. Dormía cuando llegó el Hombre del saco.', 'The imperfect sets the scene and what was going on; the indefinido tells what happened. Dormía cuando llegó el Hombre del saco (I was sleeping when the Sack Man arrived).'),
        ('Mientras (pendant que) + imparfait : Mientras Sancho cenaba, don Quijote salió. De repente (soudain) introduit l’événement.', 'Mientras (while) + imperfect: Mientras Sancho cenaba, don Quijote salió. De repente (suddenly) introduces the event.'),
        ('L’heure et l’âge au passé se disent à l’imparfait : Eran las diez. Tenía doce años.', 'Time and age in the past use the imperfect: Eran las diez (it was ten o’clock). Tenía doce años (I was twelve).'),
      ], [
        SG('imp-ind', 'dormía cuando llegó', ('je dormais quand il est arrivé (imparfait + passé simple)', 'I was sleeping when he arrived (imperfect + simple past)')),
        S('mientras', 'mientras', ('pendant que', 'while')),
        S('de-repente', 'de repente', ('soudain, tout à coup', 'suddenly')),
        S('el-ruido', 'el ruido', ('le bruit', 'the noise')),
        S('oscuro', 'oscuro / oscura', ('sombre', 'dark')),
        S('asustarse', 'asustarse', ('avoir peur, s’effrayer', 'to get scared')),
        S('despertarse', 'despertarse', ('se réveiller', 'to wake up')),
        S('la-puerta', 'la puerta', ('la porte', 'the door')),
      ], [
        x('Era de noche y todo estaba oscuro. De repente, oímos un ruido en la puerta.', 'C’était la nuit et tout était sombre. Soudain, nous avons entendu un bruit à la porte.', 'It was night and everything was dark. Suddenly we heard a noise at the door.'),
        x('Mientras Sancho dormía, don Quijote se despertó y salió al patio.', 'Pendant que Sancho dormait, don Quichotte s’est réveillé et est sorti dans la cour.', 'While Sancho was sleeping, Don Quixote woke up and went out into the courtyard.'),
      ], [
        FB(CHOOSE, 'Yo ＿ la tele cuando sonó el teléfono.', ['veía', 'vi', 'veo'], 'veía', ('Action en cours : imparfait.', 'Ongoing action: imperfect.'), ('Je regardais la télé quand le téléphone a sonné.', 'I was watching TV when the phone rang.')),
        FB(CHOOSE, 'Mientras cenábamos, de repente ＿ la luz.', ['se fue', 'se iba', 'se va'], 'se fue', ('Événement soudain : indefinido.', 'Sudden event: indefinido.'), ('Pendant que nous dînions, soudain l’électricité a été coupée.', 'While we were having dinner, the lights suddenly went out.')),
        FB(CHOOSE, '＿ las once de la noche cuando llegamos.', ['Eran', 'Fueron', 'Son'], 'Eran', ('L’heure au passé : imparfait.', 'Time in the past: imperfect.'), ('Il était onze heures du soir quand nous sommes arrivés.', 'It was eleven at night when we arrived.')),
        TF('Dormía cuando oí un ruido.', ('Le bruit a réveillé ou surpris la personne pendant son sommeil.', 'The noise came while the person was asleep.'), VRAI, ('Dormía = action en cours ; oí = événement.', 'Dormía = ongoing action; oí = event.')),
      ]),
  ])])

# ═════════════════════════ 4 : en route pour Saragosse — voyager ═════════════════════════
W4 = WORLD('delea2-w4', ('En route pour Saragosse', 'On the way to Zaragoza'), REGION,
  ('Se débrouiller en voyage : acheter un billet, comprendre les horaires, réserver une chambre, se plaindre poliment et employer por et para.', 'Get by when travelling: buy a ticket, understand timetables, book a room, complain politely and use por and para.'),
  (('L’Encantada de la fontaine', 'The Encantada of the fountain'), 'í', ('Près de Saragosse, l’Encantada, demoiselle enchantée des légendes aragonaises, apparaît à la fontaine la nuit de la Saint-Jean. Elle a embrouillé les horaires, les billets et les réservations : remets de l’ordre dans le voyage pour rompre le charme.', 'Near Zaragoza, the Encantada, the enchanted maiden of Aragonese legends, appears at the fountain on Midsummer night. She has muddled the timetables, tickets and bookings: put the trip back in order to break the spell.')),
  [CH('delea2-w4-c1', ('À la gare', 'At the station'), [
    L('es-transporte', ('Un aller-retour, s’il vous plaît', 'A return ticket, please'), ('Acheter un billet et comprendre les horaires et les retards.', 'Buy a ticket and understand timetables and delays.'), 9, [
        ('Un billet : un billete de ida (aller simple), de ida y vuelta (aller-retour). ¿A qué hora sale el próximo tren para Zaragoza? ¿De qué andén sale?', 'A ticket: un billete de ida (single), de ida y vuelta (return). ¿A qué hora sale el próximo tren para Zaragoza? (when does the next train to Zaragoza leave?) ¿De qué andén sale? (from which platform?)'),
        ('Salir (partir) ≠ llegar (arriver). El tren sale a las 8:15 y llega a las 10:40. Tiene un retraso de veinte minutos (il a vingt minutes de retard).', 'Salir (to leave) ≠ llegar (to arrive). El tren sale a las 8:15 y llega a las 10:40. Tiene un retraso de veinte minutos (it is twenty minutes late).'),
        ('Coger (prendre) le bus, le train ; perder el tren (rater le train) ; hacer transbordo (changer, faire une correspondance).', 'Coger (to take) the bus, the train; perder el tren (to miss the train); hacer transbordo (to change, make a connection).'),
      ], [
        S('billete', 'el billete', ('le billet, le ticket', 'the ticket')),
        S('ida-y-vuelta', 'de ida y vuelta', ('aller-retour', 'return (ticket)')),
        S('anden', 'el andén', ('le quai', 'the platform')),
        S('retraso', 'el retraso', ('le retard', 'the delay')),
        S('proximo', 'el próximo / la próxima', ('le prochain / la prochaine', 'the next')),
        S('coger', 'coger', ('prendre (un transport)', 'to take, to catch (transport)')),
        S('perder-el-tren', 'perder el tren', ('rater le train', 'to miss the train')),
        S('el-autobus', 'el autobús', ('le bus, l’autocar', 'the bus, the coach')),
      ], [
        x('Un billete de ida y vuelta para Zaragoza, por favor. — ¿Para qué día?', 'Un aller-retour pour Saragosse, s’il vous plaît. — Pour quel jour ?', 'A return ticket to Zaragoza, please. — For which day?'),
        x('El próximo autobús sale del andén tres con diez minutos de retraso.', 'Le prochain bus part du quai trois avec dix minutes de retard.', 'The next bus leaves from platform three ten minutes late.'),
      ], [
        DC(ANSWER, [('Taquillera', 'Buenos días, ¿qué desea?')], ('L’employée du guichet te demande ce que tu veux (un aller-retour pour Saragosse).', 'The ticket clerk asks what you want (a return ticket to Zaragoza).'), ['Un billete de ida y vuelta para Zaragoza.', 'Un andén para Zaragoza.', 'He perdido Zaragoza.'], 'Un billete de ida y vuelta para Zaragoza.', ('Un billete de ida y vuelta = un aller-retour.', 'Un billete de ida y vuelta = a return ticket.')),
        FB(COMPLETE, 'El tren ＿ de Madrid a las nueve y llega a Zaragoza a las once.', ['sale', 'llega', 'coge'], 'sale', ('Partir : salir.', 'To leave: salir.'), ('Le train part de Madrid à neuf heures et arrive à Saragosse à onze heures.', 'The train leaves Madrid at nine and arrives in Zaragoza at eleven.')),
        FB(COMPLETE, 'Me he levantado tarde y he ＿ el tren.', ['perdido', 'cogido', 'salido'], 'perdido', ('Rater le train : perder el tren.', 'To miss the train: perder el tren.'), ('Je me suis levé tard et j’ai raté le train.', 'I got up late and missed the train.')),
        TF('El tren de las 10:15 tiene un retraso de quince minutos.', ('Le train partira vers 10 h 30.', 'The train will leave at about 10:30.'), VRAI, ('10 h 15 + 15 minutes de retard = 10 h 30.', '10:15 + 15 minutes late = 10:30.')),
      ]),
    L('es-por-para', ('Por ou para ?', 'Por or para?'), ('Distinguer por et para dans les situations courantes.', 'Tell por and para apart in everyday situations.'), 10, [
        ('Para : la destination et le but. Un tren para Zaragoza. Estudio español para viajar (pour voyager). Este regalo es para ti.', 'Para: destination and purpose. Un tren para Zaragoza. Estudio español para viajar (in order to travel). Este regalo es para ti (for you).'),
        ('Por : la cause, le lieu par où l’on passe, le moyen et le moment de la journée. Gracias por todo. Paseamos por el parque. Hablo por teléfono. Por la mañana.', 'Por: cause, the place you go through, means and time of day. Gracias por todo. Paseamos por el parque (we walk through the park). Hablo por teléfono. Por la mañana.'),
        ('Pour un prix : por diez euros (pour dix euros). Pour une date limite : para el lunes (pour lundi).', 'For a price: por diez euros (for ten euros). For a deadline: para el lunes (for/by Monday).'),
      ], [
        SG('para', 'para', ('pour (but, destination, destinataire)', 'for, to (purpose, destination, recipient)')),
        SG('por', 'por', ('par, pour (cause, passage, moyen)', 'through, by, because of (cause, route, means)')),
        S('el-regalo', 'el regalo', ('le cadeau', 'the present, the gift')),
        S('pasear', 'pasear', ('se promener', 'to go for a walk')),
        S('gracias-por', 'gracias por…', ('merci pour…', 'thanks for…')),
        S('el-parque', 'el parque', ('le parc', 'the park')),
        S('por-telefono', 'por teléfono', ('au téléphone', 'on the phone')),
      ], [
        x('Este tren va para Zaragoza, pero pasa por Calatayud.', 'Ce train va à Saragosse, mais il passe par Calatayud.', 'This train goes to Zaragoza, but it goes through Calatayud.'),
        x('Gracias por el regalo. — Es para tu viaje.', 'Merci pour le cadeau. — C’est pour ton voyage.', 'Thanks for the present. — It’s for your trip.'),
      ], [
        FB(CHOOSE, 'Estudio español ＿ trabajar en Madrid.', ['para', 'por', 'de'], 'para', ('But : para + infinitif.', 'Purpose: para + infinitive.'), ('J’étudie l’espagnol pour travailler à Madrid.', 'I study Spanish to work in Madrid.')),
        FB(CHOOSE, 'Muchas gracias ＿ tu ayuda.', ['por', 'para', 'a'], 'por', ('Gracias por…', 'Gracias por…'), ('Merci beaucoup pour ton aide.', 'Thank you very much for your help.')),
        FB(CHOOSE, 'Paseamos ＿ el centro de la ciudad.', ['por', 'para', 'en para'], 'por', ('Passage dans un lieu : por.', 'Going through a place: por.'), ('Nous nous promenons dans le centre-ville.', 'We walk around the city centre.')),
        FB(CHOOSE, 'Este regalo es ＿ Dulcinea.', ['para', 'por', 'con'], 'para', ('Destinataire : para.', 'Recipient: para.'), ('Ce cadeau est pour Dulcinée.', 'This present is for Dulcinea.')),
      ]),
  ]),
  CH('delea2-w4-c2', ('À l’hôtel', 'At the hotel'), [
    L('es-hotel', ('Réserver une chambre et se plaindre', 'Booking a room and complaining'), ('Réserver, s’enregistrer à l’hôtel et signaler un problème.', 'Book, check in at a hotel and report a problem.'), 9, [
        ('Réserver : Quería reservar una habitación doble / individual para dos noches. ¿El desayuno está incluido? L’imparfait quería rend la demande plus polie.', 'Booking: Quería reservar una habitación doble / individual para dos noches. ¿El desayuno está incluido? The imperfect quería makes the request more polite.'),
        ('À l’arrivée : Tengo una reserva a nombre de… (j’ai une réservation au nom de…). On vous donne la llave (la clé) de la habitación.', 'On arrival: Tengo una reserva a nombre de… (I have a booking in the name of…). They give you la llave (the key) to the room.'),
        ('Se plaindre poliment : Perdone, la ducha no funciona (la douche ne marche pas). Hay mucho ruido. ¿Me puede cambiar de habitación?', 'Complaining politely: Perdone, la ducha no funciona (the shower isn’t working). Hay mucho ruido. ¿Me puede cambiar de habitación? (can you change my room?)'),
      ], [
        S('reservar', 'reservar', ('réserver', 'to book, to reserve')),
        S('la-reserva', 'la reserva', ('la réservation', 'the booking, the reservation')),
        S('habitacion-doble', 'la habitación doble', ('la chambre double', 'the double room')),
        S('la-llave', 'la llave', ('la clé', 'the key')),
        S('incluido', 'incluido / incluida', ('compris, inclus', 'included')),
        S('funcionar', 'funcionar', ('fonctionner, marcher', 'to work (machine)')),
        S('la-ducha', 'la ducha', ('la douche', 'the shower')),
        S('quejarse', 'quejarse', ('se plaindre', 'to complain')),
      ], [
        x('Quería reservar una habitación doble para el viernes y el sábado.', 'Je voudrais réserver une chambre double pour vendredi et samedi.', 'I’d like to book a double room for Friday and Saturday.'),
        x('Perdone, el aire acondicionado no funciona. ¿Me puede cambiar de habitación?', 'Excusez-moi, la climatisation ne marche pas. Pouvez-vous me changer de chambre ?', 'Excuse me, the air conditioning isn’t working. Can you change my room?'),
      ], [
        DC(ANSWER, [('Recepcionista', 'Buenas tardes, ¿tiene reserva?')], ('La réceptionniste te demande si tu as une réservation.', 'The receptionist asks if you have a booking.'), ['Sí, a nombre de Panza.', 'Sí, la llave es mía.', 'No, gracias, ya he comido.'], 'Sí, a nombre de Panza.', ('Une réservation au nom de… : a nombre de…', 'A booking in the name of…: a nombre de…')),
        FB(COMPLETE, '¿El desayuno está ＿ en el precio?', ['incluido', 'reservado', 'roto'], 'incluido', ('Compris dans le prix : incluido.', 'Included in the price: incluido.'), ('Le petit-déjeuner est-il compris dans le prix ?', 'Is breakfast included in the price?')),
        FB(COMPLETE, 'Perdone, la ducha no ＿.', ['funciona', 'reserva', 'sale'], 'funciona', ('Ne pas marcher : no funcionar.', 'Not working: no funcionar.'), ('Excusez-moi, la douche ne marche pas.', 'Excuse me, the shower isn’t working.')),
        TF('Quería una habitación individual para tres noches.', ('Le client veut une chambre pour deux personnes.', 'The guest wants a room for two people.'), FAUX, ('Individual = pour une personne.', 'Individual = for one person.')),
      ]),
  ])])

# ═════════════════════════ 5 : la maison sans toit — le logement, les pronoms, l'impératif ═════════════════════════
W5 = WORLD('delea2-w5', ('La maison sans toit', 'The roofless house'), REGION,
  ('Décrire un logement, chercher un appartement à louer, éviter les répétitions avec lo, la, los, las et donner des consignes à l’impératif.', 'Describe a home, look for a flat to rent, avoid repetition with lo, la, los, las and give instructions in the imperative.'),
  (('Le Diablo Cojuelo', 'The Diablo Cojuelo'), 'ó', ('Le Diablo Cojuelo, diable boiteux des romans espagnols, soulève les toits des maisons pour espionner ceux qui y vivent… et met tout en désordre. Décris chaque pièce, range les meubles et donne-lui des ordres clairs pour qu’il repose les toits.', 'The Diablo Cojuelo, the limping devil of Spanish novels, lifts the roofs off houses to spy on the people inside… and turns everything upside down. Describe every room, put the furniture away and give it clear orders so it puts the roofs back.')),
  [CH('delea2-w5-c1', ('Un appartement à louer', 'A flat to rent'), [
    L('es-vivienda', ('Le logement : el piso, alquilar', 'Housing: el piso, alquilar'), ('Décrire un logement et comprendre une annonce de location.', 'Describe a home and understand a rental advert.'), 9, [
        ('Les pièces : el salón (le salon), la cocina (la cuisine), el dormitorio (la chambre), el baño (la salle de bains), la terraza (la terrasse), el pasillo (le couloir).', 'Rooms: el salón (living room), la cocina (kitchen), el dormitorio (bedroom), el baño (bathroom), la terraza (terrace), el pasillo (corridor).'),
        ('Une annonce : Se alquila piso (appartement à louer) : tres dormitorios, amueblado (meublé), exterior (sur rue), con ascensor (avec ascenseur), en el tercer piso (au troisième étage).', 'An advert: Se alquila piso (flat to rent): three bedrooms, amueblado (furnished), exterior (facing the street), con ascensor (with a lift), en el tercer piso (on the third floor).'),
        ('Los vecinos = les voisins. Vivir en un piso (en appartement) / en una casa (en maison) / en las afueras (en banlieue, à l’extérieur de la ville).', 'Los vecinos = the neighbours. Vivir en un piso (in a flat) / en una casa (in a house) / en las afueras (on the outskirts).'),
      ], [
        S('el-piso', 'el piso', ('l’appartement, l’étage', 'the flat, the floor (storey)')),
        S('alquilar', 'alquilar', ('louer', 'to rent')),
        S('el-salon', 'el salón', ('le salon', 'the living room')),
        S('la-cocina', 'la cocina', ('la cuisine (pièce)', 'the kitchen')),
        S('el-dormitorio', 'el dormitorio', ('la chambre (à coucher)', 'the bedroom')),
        S('el-bano', 'el baño', ('la salle de bains', 'the bathroom')),
        S('el-ascensor', 'el ascensor', ('l’ascenseur', 'the lift, the elevator')),
        S('amueblado', 'amueblado / amueblada', ('meublé / meublée', 'furnished')),
        S('el-vecino', 'el vecino / la vecina', ('le voisin / la voisine', 'the neighbour')),
      ], [
        x('Se alquila piso amueblado: dos dormitorios, salón, cocina y baño. Tercer piso con ascensor.', 'Appartement meublé à louer : deux chambres, salon, cuisine et salle de bains. Troisième étage avec ascenseur.', 'Furnished flat to rent: two bedrooms, living room, kitchen and bathroom. Third floor with a lift.'),
        x('Mis vecinos son muy simpáticos, pero hacen mucho ruido por la noche.', 'Mes voisins sont très sympathiques, mais ils font beaucoup de bruit la nuit.', 'My neighbours are very nice, but they make a lot of noise at night.'),
      ], [
        FB(COMPLETE, 'Dormimos en el ＿ y cocinamos en la cocina.', ['dormitorio', 'salón', 'ascensor'], 'dormitorio', ('Dormir : el dormitorio.', 'Sleeping: el dormitorio.'), ('Nous dormons dans la chambre et nous cuisinons dans la cuisine.', 'We sleep in the bedroom and cook in the kitchen.')),
        FB(COMPLETE, 'Vivo en un quinto piso y no hay ＿: ¡subo a pie!', ['ascensor', 'baño', 'vecino'], 'ascensor', ('Monter sans ascenseur : no hay ascensor.', 'Climbing with no lift: no hay ascensor.'), ('J’habite au cinquième étage et il n’y a pas d’ascenseur : je monte à pied !', 'I live on the fifth floor and there’s no lift: I walk up!')),
        TF('Se alquila piso amueblado.', ('L’appartement est à vendre, sans meubles.', 'The flat is for sale, unfurnished.'), FAUX, ('Se alquila = à louer ; amueblado = meublé.', 'Se alquila = to rent; amueblado = furnished.')),
        DC(ANSWER, [('Agente', '¿Cómo quiere el piso?')], ('L’agent immobilier te demande quel appartement tu cherches.', 'The estate agent asks what kind of flat you want.'), ['Con dos dormitorios y cerca del centro.', 'Con dos vecinos y un ascensor roto.', 'Lo quiero ayer.'], 'Con dos dormitorios y cerca del centro.', ('On décrit les pièces et le quartier.', 'You describe the rooms and the area.')),
      ]),
    L('es-pronombres-od', ('Je la vois : lo, la, los, las', 'I see it: lo, la, los, las'), ('Remplacer un complément d’objet direct par un pronom.', 'Replace a direct object with a pronoun.'), 10, [
        ('Les pronoms compléments directs : me, te, lo (le), la (la), nos, os, los, las. Ils se placent avant le verbe conjugué : ¿La mesa? La pongo aquí.', 'Direct object pronouns: me, te, lo (him, it), la (her, it), nos, os, los, las. They go before the conjugated verb: ¿La mesa? La pongo aquí (I’ll put it here).'),
        ('Avec un infinitif ou un gérondif, on peut les accrocher à la fin : Voy a comprarlo = Lo voy a comprar.', 'With an infinitive or gerund, they can be attached to the end: Voy a comprarlo = Lo voy a comprar (I’m going to buy it).'),
        ('Les meubles : la mesa (la table), la silla (la chaise), el sofá (le canapé), la cama (le lit), el armario (l’armoire, le placard), la estantería (l’étagère), la lámpara (la lampe).', 'Furniture: la mesa (table), la silla (chair), el sofá (sofa), la cama (bed), el armario (wardrobe, cupboard), la estantería (shelves), la lámpara (lamp).'),
      ], [
        SG('lo-la', 'lo / la / los / las', ('le / la / les (pronoms COD)', 'him-it / her-it / them (direct object pronouns)')),
        S('la-mesa', 'la mesa', ('la table', 'the table')),
        S('la-silla', 'la silla', ('la chaise', 'the chair')),
        S('el-sofa', 'el sofá', ('le canapé', 'the sofa')),
        S('la-cama', 'la cama', ('le lit', 'the bed')),
        S('el-armario', 'el armario', ('l’armoire, le placard', 'the wardrobe, the cupboard')),
        S('la-lampara', 'la lámpara', ('la lampe', 'the lamp')),
        S('poner', 'poner', ('mettre, poser', 'to put')),
      ], [
        x('¿Dónde pongo el sofá? — Ponlo en el salón, al lado de la ventana.', 'Où est-ce que je mets le canapé ? — Mets-le dans le salon, à côté de la fenêtre.', 'Where shall I put the sofa? — Put it in the living room, next to the window.'),
        x('¿Has visto mis llaves? — Sí, las he visto en la mesa.', 'As-tu vu mes clés ? — Oui, je les ai vues sur la table.', 'Have you seen my keys? — Yes, I saw them on the table.'),
      ], [
        FB(CHOOSE, '¿La lámpara? ＿ he comprado en el mercado.', ['La', 'Lo', 'Le'], 'La', ('La lámpara est féminin singulier : la.', 'La lámpara is feminine singular: la.'), ('La lampe ? Je l’ai achetée au marché.', 'The lamp? I bought it at the market.')),
        FB(CHOOSE, '¿Y los libros? — ＿ tengo en el armario.', ['Los', 'Las', 'Lo'], 'Los', ('Los libros : los.', 'Los libros: los.'), ('Et les livres ? — Je les ai dans le placard.', 'And the books? — I have them in the cupboard.')),
        FB(CHOOSE, 'Esta silla es bonita. Voy a ＿.', ['comprarla', 'comprarlo', 'la comprar'], 'comprarla', ('Infinitif + pronom attaché : comprarla.', 'Infinitive + attached pronoun: comprarla.'), ('Cette chaise est jolie. Je vais l’acheter.', 'This chair is pretty. I’m going to buy it.')),
        order(('Remets dans l’ordre : « Je ne le connais pas. »', 'Put in order: “I don’t know him.”'), ['No', 'lo', 'conozco.'], ('No + pronom + verbe.', 'No + pronoun + verb.')),
      ]),
  ]),
  CH('delea2-w5-c2', ('Le grand rangement', 'The big tidy-up'), [
    L('es-imperativo', ('Range ta chambre ! l’impératif', 'Tidy your room! The imperative'), ('Donner des ordres et des consignes avec l’impératif (tú et usted).', 'Give orders and instructions with the imperative (tú and usted).'), 10, [
        ('Impératif tú = 3e personne du présent : habla, come, escribe, limpia (nettoie), friega los platos (fais la vaisselle).', 'Imperative tú = 3rd person of the present: habla, come, escribe, limpia (clean), friega los platos (do the washing-up).'),
        ('Huit impératifs irréguliers : pon (mets), haz (fais), di (dis), ven (viens), sal (sors), ten (tiens), ve (va), sé (sois). Haz la cama (fais le lit) !', 'Eight irregular imperatives: pon (put), haz (do), di (say), ven (come), sal (go out), ten (have, hold), ve (go), sé (be). Haz la cama (make the bed)!'),
        ('Les pronoms s’accrochent à la fin : ¡Ponlo aquí! ¡Siéntate! Pour usted : hable, coma, pase (entrez), siéntese (asseyez-vous).', 'Pronouns are attached to the end: ¡Ponlo aquí! ¡Siéntate! For usted: hable, coma, pase (come in), siéntese (sit down).'),
      ], [
        SG('imperativo', 'habla / come / escribe', ('parle / mange / écris (impératif)', 'speak / eat / write (imperative)')),
        SG('imperativo-irregular', 'pon / haz / ven / sal', ('mets / fais / viens / sors', 'put / do / come / go out')),
        S('limpiar', 'limpiar', ('nettoyer', 'to clean')),
        S('fregar', 'fregar los platos', ('faire la vaisselle', 'to do the washing-up')),
        S('hacer-la-cama', 'hacer la cama', ('faire le lit', 'to make the bed')),
        S('ordenar', 'ordenar', ('ranger', 'to tidy')),
        S('la-basura', 'la basura', ('les ordures, la poubelle', 'the rubbish, the bin')),
        S('pase', 'pase / siéntese', ('entrez / asseyez-vous (vous de politesse)', 'come in / sit down (polite)')),
      ], [
        x('Sancho, ordena tu habitación, haz la cama y saca la basura.', 'Sancho, range ta chambre, fais le lit et sors la poubelle.', 'Sancho, tidy your room, make the bed and take out the rubbish.'),
        x('Pase, señor, siéntese. ¿Quiere un café?', 'Entrez, monsieur, asseyez-vous. Voulez-vous un café ?', 'Come in, sir, sit down. Would you like a coffee?'),
      ], [
        FB(CHOOSE, '¡＿ la cama antes de salir!', ['Haz', 'Hace', 'Hacé'], 'Haz', ('Hacer → haz (irrégulier).', 'Hacer → haz (irregular).'), ('Fais le lit avant de sortir !', 'Make the bed before going out!')),
        FB(CHOOSE, '＿ aquí, Sancho, rápido.', ['Ven', 'Viene', 'Vienes'], 'Ven', ('Venir → ven.', 'Venir → ven.'), ('Viens ici, Sancho, vite.', 'Come here, Sancho, quickly.')),
        FB(CHOOSE, 'El libro está en la mesa: ＿ en la estantería.', ['ponlo', 'lo pon', 'pónelo'], 'ponlo', ('Impératif + pronom attaché : ponlo.', 'Imperative + attached pronoun: ponlo.'), ('Le livre est sur la table : mets-le sur l’étagère.', 'The book is on the table: put it on the shelf.')),
        DC(ANSWER, [('Duquesa', 'Buenas tardes, ¿se puede?')], ('La duchesse frappe et demande si elle peut entrer.', 'The duchess knocks and asks if she may come in.'), ['Sí, claro, pase y siéntese.', 'Sí, sal.', 'No, haz la cama.'], 'Sí, claro, pase y siéntese.', ('Avec usted : pase, siéntese.', 'With usted: pase, siéntese.')),
      ]),
  ])])

# ═════════════════════════ 6 : les montagnes de Mari — comparer, la nature ═════════════════════════
W6 = WORLD('delea2-w6', ('Les montagnes de Mari', 'Mari’s mountains'), REGION,
  ('Comparer des lieux et des personnes (más… que, tan… como), employer le superlatif et -ísimo, et décrire la nature et les paysages.', 'Compare places and people (más… que, tan… como), use the superlative and -ísimo, and describe nature and landscapes.'),
  (('Mari d’Amboto', 'Mari of Amboto'), 'ú', ('Mari, la dame des montagnes basques, voyage dans le ciel en boule de feu et commande les orages. Elle méprise les vantards : compare avec justesse les sommets, les rivières et les villages, et elle laissera passer le chevalier.', 'Mari, the lady of the Basque mountains, travels across the sky as a ball of fire and commands the storms. She despises braggarts: compare peaks, rivers and villages fairly, and she will let the knight pass.')),
  [CH('delea2-w6-c1', ('Plus haut que la Manche', 'Higher than La Mancha'), [
    L('es-comparar', ('Plus grand que… : más, menos, tan', 'Taller than…: más, menos, tan'), ('Comparer avec más… que, menos… que et tan… como.', 'Compare with más… que, menos… que and tan… como.'), 9, [
        ('Más + adjectif + que (plus… que), menos + adjectif + que (moins… que), tan + adjectif + como (aussi… que). Sancho es más bajo que don Quijote.', 'Más + adjective + que (more… than), menos + adjective + que (less… than), tan + adjective + como (as… as). Sancho es más bajo que don Quijote.'),
        ('Avec un nom : más / menos + nom + que ; tanto, tanta, tantos, tantas + nom + como (autant de… que). Tengo tantos libros como tú.', 'With a noun: más / menos + noun + que; tanto, tanta, tantos, tantas + noun + como (as much / as many… as). Tengo tantos libros como tú.'),
        ('Comparatifs irréguliers : mejor (meilleur, mieux), peor (pire), mayor (plus âgé), menor (plus jeune). Mi hermano mayor.', 'Irregular comparatives: mejor (better), peor (worse), mayor (older), menor (younger). Mi hermano mayor (my older brother).'),
      ], [
        SG('mas-que', 'más… que / menos… que', ('plus… que / moins… que', 'more… than / less… than')),
        SG('tan-como', 'tan… como', ('aussi… que', 'as… as')),
        S('mejor', 'mejor / peor', ('meilleur, mieux / pire', 'better / worse')),
        S('mayor', 'mayor / menor', ('plus âgé / plus jeune', 'older / younger')),
        S('la-montana', 'la montaña', ('la montagne', 'the mountain')),
        S('el-rio', 'el río', ('la rivière, le fleuve', 'the river')),
        S('ancho', 'ancho / ancha', ('large', 'wide')),
        S('largo', 'largo / larga', ('long', 'long')),
      ], [
        x('Los Pirineos son más altos que las montañas de la Manche, pero el Ebro es menos largo que el Tajo.', 'Les Pyrénées sont plus hautes que les montagnes de la Manche, mais l’Èbre est moins long que le Tage.', 'The Pyrenees are higher than the mountains of La Mancha, but the Ebro is shorter than the Tagus.'),
        x('Sancho no es tan valiente como su señor, pero es mucho más prudente.', 'Sancho n’est pas aussi courageux que son maître, mais il est beaucoup plus prudent.', 'Sancho isn’t as brave as his master, but he is much more careful.'),
      ], [
        FB(CHOOSE, 'Madrid es más grande ＿ Toledo.', ['que', 'como', 'de'], 'que', ('Comparaison : más… que.', 'Comparison: más… que.'), ('Madrid est plus grande que Tolède.', 'Madrid is bigger than Toledo.')),
        FB(CHOOSE, 'Mi hermana es tan alta ＿ yo.', ['como', 'que', 'de'], 'como', ('Égalité : tan… como.', 'Equality: tan… como.'), ('Ma sœur est aussi grande que moi.', 'My sister is as tall as me.')),
        FB(CHOOSE, 'Este vino es ＿ que el otro.', ['mejor', 'más bueno de', 'tan mejor'], 'mejor', ('Más bueno → mejor.', 'Más bueno → mejor.'), ('Ce vin est meilleur que l’autre.', 'This wine is better than the other one.')),
        TF('Ana tiene 20 años y su hermano 15: él es su hermano menor.', ('Le frère est plus jeune qu’Ana.', 'The brother is younger than Ana.'), VRAI, ('Menor = plus jeune.', 'Menor = younger.')),
      ]),
    L('es-superlativo', ('Le plus beau : el más, -ísimo', 'The most beautiful: el más, -ísimo'), ('Exprimer le superlatif relatif et absolu.', 'Express the relative and absolute superlative.'), 9, [
        ('Superlatif relatif : el / la / los / las + más + adjectif + de. El Aneto es la montaña más alta de los Pirineos.', 'Relative superlative: el / la / los / las + más + adjective + de. El Aneto es la montaña más alta de los Pirineos (the highest mountain in the Pyrenees).'),
        ('Superlatif absolu : adjectif + -ísimo = très, très. Alto → altísimo, bonito → bonitísimo, fácil → facilísimo. Mucho → muchísimo.', 'Absolute superlative: adjective + -ísimo = very, very. Alto → altísimo, bonito → bonitísimo, fácil → facilísimo. Mucho → muchísimo.'),
        ('Attention à l’orthographe : rico → riquísimo (c → qu), largo → larguísimo (g → gu).', 'Watch the spelling: rico → riquísimo (c → qu), largo → larguísimo (g → gu).'),
      ], [
        SG('el-mas', 'el más… de', ('le plus… de (superlatif)', 'the most… in (superlative)')),
        SG('isimo', '-ísimo', ('très, extrêmement (suffixe)', 'very, extremely (suffix)')),
        S('bonito', 'bonito / bonita', ('joli / jolie', 'pretty, nice')),
        S('rico', 'rico / rica', ('délicieux (plat), riche', 'delicious (food), rich')),
        S('el-paisaje', 'el paisaje', ('le paysage', 'the landscape')),
        S('famoso', 'famoso / famosa', ('célèbre', 'famous')),
        S('el-mundo', 'el mundo', ('le monde', 'the world')),
      ], [
        x('Este paisaje es bonitísimo: es el más bonito del viaje.', 'Ce paysage est magnifique : c’est le plus beau du voyage.', 'This landscape is gorgeous: it’s the most beautiful of the trip.'),
        x('El queso de esta sierra está riquísimo.', 'Le fromage de cette sierra est délicieux.', 'The cheese from this sierra is delicious.'),
      ], [
        FB(CHOOSE, 'Es el río más largo ＿ España.', ['de', 'que', 'en'], 'de', ('Superlatif : el más… de.', 'Superlative: el más… de.'), ('C’est le fleuve le plus long d’Espagne.', 'It’s the longest river in Spain.')),
        FB(CHOOSE, 'La paella está ＿.', ['riquísima', 'ricísima', 'muy riquísima'], 'riquísima', ('Rico → riquísimo (c → qu).', 'Rico → riquísimo (c → qu).'), ('La paella est délicieuse.', 'The paella is delicious.')),
        FB(CHOOSE, 'Es la novela más ＿ de Cervantes.', ['famosa', 'famosísima', 'famoso'], 'famosa', ('El / la más + adjectif.', 'El / la más + adjective.'), ('C’est le roman le plus célèbre de Cervantes.', 'It’s Cervantes’s most famous novel.')),
        order(('Remets dans l’ordre : « C’est la montagne la plus haute. »', 'Put in order: “It’s the highest mountain.”'), ['Es', 'la', 'montaña', 'más', 'alta.'], ('La + nom + más + adjectif.', 'La + noun + más + adjective.')),
      ]),
  ]),
  CH('delea2-w6-c2', ('Le chemin des crêtes', 'The ridge path'), [
    L('es-naturaleza', ('La nature : el bosque, el lago, la costa', 'Nature: el bosque, el lago, la costa'), ('Décrire un paysage et une excursion dans la nature.', 'Describe a landscape and an outing in nature.'), 9, [
        ('Les paysages : el bosque (la forêt), el lago (le lac), la costa (la côte), la playa (la plage), la isla (l’île), el valle (la vallée), la cueva (la grotte).', 'Landscapes: el bosque (forest), el lago (lake), la costa (coast), la playa (beach), la isla (island), el valle (valley), la cueva (cave).'),
        ('Les animaux : la vaca (la vache), la oveja (la brebis), el pájaro (l’oiseau), el águila (l’aigle).', 'Animals: la vaca (cow), la oveja (sheep), el pájaro (bird), el águila (eagle).'),
        ('Une excursion : hacer senderismo (faire de la randonnée), subir (monter), bajar (descendre), la cima (le sommet), el camino (le chemin).', 'An outing: hacer senderismo (to go hiking), subir (to go up), bajar (to go down), la cima (the summit), el camino (the path).'),
      ], [
        S('el-bosque', 'el bosque', ('la forêt, le bois', 'the forest, the woods')),
        S('el-lago', 'el lago', ('le lac', 'the lake')),
        S('la-costa', 'la costa', ('la côte', 'the coast')),
        S('la-cueva', 'la cueva', ('la grotte', 'the cave')),
        S('el-pajaro', 'el pájaro', ('l’oiseau', 'the bird')),
        S('senderismo', 'hacer senderismo', ('faire de la randonnée', 'to go hiking')),
        S('subir', 'subir / bajar', ('monter / descendre', 'to go up / to go down')),
        S('el-camino', 'el camino', ('le chemin', 'the path, the way')),
      ], [
        x('Subimos a la cima por un camino estrecho y vimos un lago azul y una cueva.', 'Nous sommes montés au sommet par un chemin étroit et nous avons vu un lac bleu et une grotte.', 'We climbed to the summit along a narrow path and saw a blue lake and a cave.'),
        x('Según la leyenda, Mari vive en una cueva del monte Amboto.', 'Selon la légende, Mari vit dans une grotte du mont Amboto.', 'According to legend, Mari lives in a cave on Mount Amboto.'),
      ], [
        FB(COMPLETE, 'En el ＿ hay muchos árboles y pájaros.', ['bosque', 'lago', 'mar'], 'bosque', ('Beaucoup d’arbres : el bosque.', 'Lots of trees: el bosque.'), ('Dans la forêt, il y a beaucoup d’arbres et d’oiseaux.', 'In the forest there are lots of trees and birds.')),
        FB(COMPLETE, 'Los fines de semana me gusta hacer ＿ en la montaña.', ['senderismo', 'camino', 'costa'], 'senderismo', ('Randonnée : senderismo.', 'Hiking: senderismo.'), ('Le week-end, j’aime faire de la randonnée en montagne.', 'At weekends I like hiking in the mountains.')),
        TF('Bajamos de la montaña a las seis.', ('Ils sont montés au sommet à six heures.', 'They climbed to the summit at six.'), FAUX, ('Bajar = descendre.', 'Bajar = to go down.')),
        DC(ANSWER, [('Pastor', '¿Qué camino vais a tomar?')], ('Le berger demande quel chemin vous allez prendre (celui de la côte).', 'The shepherd asks which way you’re going to take (the coast path).'), ['El camino de la costa.', 'El camino de la cueva de ayer.', 'Vamos a subir el lago.'], 'El camino de la costa.', ('Le chemin de… : el camino de…', 'The path of…: el camino de…')),
      ]),
  ])])

# ═════════════════════════ 7 : les fêtes de Catalogne — loisirs, invitations, gérondif ═════════════════════════
W7 = WORLD('delea2-w7', ('Les fêtes du chemin', 'The festivals on the way'), REGION,
  ('Parler de ses loisirs et de ses sports, proposer une sortie, accepter ou refuser, fixer un rendez-vous et dire ce qu’on est en train de faire (estar + gérondif).', 'Talk about hobbies and sports, suggest an outing, accept or decline, arrange to meet and say what you are doing right now (estar + gerund).'),
  (('La Mula Guita', 'The Mula Guita'), 'ü', ('Pendant la fête du village, la Mula Guita, mule de feu des fêtes catalanes, crache des étincelles et fait fuir les danseurs. Invite tout le monde, organise les rendez-vous et commente la fête en direct pour qu’elle rejoigne le cortège.', 'During the village festival, the Mula Guita, the fire mule of Catalan festivals, spits sparks and scares away the dancers. Invite everyone, arrange the meetings and describe the festival live so it joins the procession.')),
  [CH('delea2-w7-c1', ('Le temps libre', 'Free time'), [
    L('es-ocio', ('Les loisirs : jugar al fútbol, ir al cine', 'Free time: jugar al fútbol, ir al cine'), ('Parler de ses loisirs, de ses sports et de leur fréquence.', 'Talk about your hobbies, your sports and how often you do them.'), 9, [
        ('Jugar a + sport ou jeu : jugar al fútbol, al tenis, a las cartas. Mais : hacer deporte, nadar (nager), correr (courir), montar en bici (faire du vélo).', 'Jugar a + sport or game: jugar al fútbol, al tenis, a las cartas. But: hacer deporte, nadar (to swim), correr (to run), montar en bici (to ride a bike).'),
        ('Sortir : ir al cine, al teatro, a un concierto, a un museo, de compras (faire les magasins), de tapas (aller manger des tapas).', 'Going out: ir al cine, al teatro, a un concierto, a un museo, de compras (shopping), de tapas (out for tapas).'),
        ('La fréquence : una vez a la semana (une fois par semaine), dos veces al mes, casi nunca (presque jamais), a veces (parfois), en mi tiempo libre (pendant mon temps libre).', 'Frequency: una vez a la semana (once a week), dos veces al mes (twice a month), casi nunca (hardly ever), a veces (sometimes), en mi tiempo libre (in my free time).'),
      ], [
        S('el-tiempo-libre', 'el tiempo libre', ('le temps libre', 'free time')),
        S('jugar-al-futbol', 'jugar al fútbol', ('jouer au football', 'to play football')),
        S('nadar', 'nadar', ('nager', 'to swim')),
        S('correr', 'correr', ('courir', 'to run')),
        S('el-cine', 'el cine', ('le cinéma', 'the cinema')),
        S('el-concierto', 'el concierto', ('le concert', 'the concert')),
        S('a-veces', 'a veces', ('parfois', 'sometimes')),
        S('a-la-semana', 'una vez a la semana', ('une fois par semaine', 'once a week')),
      ], [
        x('En mi tiempo libre juego al fútbol y, a veces, voy al cine con mis amigos.', 'Pendant mon temps libre, je joue au football et, parfois, je vais au cinéma avec mes amis.', 'In my free time I play football and sometimes go to the cinema with my friends.'),
        x('Sancho nada una vez a la semana, pero no corre nunca.', 'Sancho nage une fois par semaine, mais il ne court jamais.', 'Sancho swims once a week, but he never runs.'),
      ], [
        FB(CHOOSE, 'Los domingos juego ＿ tenis con mi padre.', ['al', 'el', 'a la'], 'al', ('Jugar a + el → jugar al.', 'Jugar a + el → jugar al.'), ('Le dimanche, je joue au tennis avec mon père.', 'On Sundays I play tennis with my father.')),
        FB(COMPLETE, 'Voy al gimnasio dos veces ＿ semana.', ['a la', 'en la', 'por'], 'a la', ('Fréquence : dos veces a la semana.', 'Frequency: dos veces a la semana.'), ('Je vais à la salle de sport deux fois par semaine.', 'I go to the gym twice a week.')),
        TF('Casi nunca voy a conciertos.', ('La personne va souvent au concert.', 'The person often goes to concerts.'), FAUX, ('Casi nunca = presque jamais.', 'Casi nunca = hardly ever.')),
        DC(ANSWER, [('Amiga', '¿Qué haces en tu tiempo libre?')], ('Ton amie te demande ce que tu fais pendant ton temps libre.', 'Your friend asks what you do in your free time.'), ['Leo, nado y a veces voy al cine.', 'Tengo tiempo libre en la mesa.', 'Fui libre ayer.'], 'Leo, nado y a veces voy al cine.', ('On cite ses loisirs au présent.', 'You list your hobbies in the present.')),
      ]),
    L('es-quedar', ('On se retrouve ? quedar, ¿te apetece…?', 'Shall we meet? quedar, ¿te apetece…?'), ('Proposer une sortie, accepter, refuser et fixer un rendez-vous.', 'Suggest an outing, accept, decline and arrange to meet.'), 10, [
        ('Proposer : ¿Quieres venir al cine? ¿Te apetece tomar algo? (ça te dit de boire un verre ?) ¿Por qué no vamos a la playa? ¿Vamos a…?', 'Suggesting: ¿Quieres venir al cine? ¿Te apetece tomar algo? (do you fancy a drink?) ¿Por qué no vamos a la playa? ¿Vamos a…?'),
        ('Accepter : Vale, de acuerdo, ¡qué buena idea! Refuser : Lo siento, no puedo, es que tengo que trabajar (désolé, je ne peux pas, c’est que je dois travailler).', 'Accepting: Vale, de acuerdo, ¡qué buena idea! Declining: Lo siento, no puedo, es que tengo que trabajar (sorry, I can’t, I have to work).'),
        ('Quedar = se donner rendez-vous : ¿Dónde quedamos? — En la plaza. ¿A qué hora quedamos? — A las ocho. Poder et querer changent au présent : puedo, quiero.', 'Quedar = to arrange to meet: ¿Dónde quedamos? — En la plaza. ¿A qué hora quedamos? — A las ocho. Poder and querer change in the present: puedo, quiero.'),
      ], [
        S('quedar', 'quedar', ('se donner rendez-vous', 'to arrange to meet')),
        S('te-apetece', '¿Te apetece…?', ('Ça te dit de… ?', 'Do you fancy…?')),
        S('vale', 'vale', ('d’accord, OK', 'OK, fine')),
        S('lo-siento', 'lo siento', ('pardon, je suis désolé(e)', 'I’m sorry')),
        S('no-puedo', 'no puedo', ('je ne peux pas', 'I can’t')),
        S('es-que', 'es que…', ('c’est que…', 'the thing is…')),
        S('que-buena-idea', '¡Qué buena idea!', ('Quelle bonne idée !', 'What a good idea!')),
        S('tomar-algo', 'tomar algo', ('prendre un verre', 'to have a drink')),
      ], [
        x('¿Te apetece ir a la fiesta esta noche? — ¡Vale! ¿Dónde quedamos?', 'Ça te dit d’aller à la fête ce soir ? — D’accord ! Où est-ce qu’on se retrouve ?', 'Do you fancy going to the festival tonight? — OK! Where shall we meet?'),
        x('Lo siento, no puedo: es que mañana me levanto muy temprano.', 'Désolé, je ne peux pas : c’est que demain je me lève très tôt.', 'Sorry, I can’t: the thing is, I’m getting up very early tomorrow.'),
      ], [
        DC(ANSWER, [('Duque', '¿Por qué no venís a cenar el sábado?')], ('Le duc vous invite à dîner samedi (tu acceptes).', 'The duke invites you to dinner on Saturday (you accept).'), ['¡Qué buena idea! ¿A qué hora?', 'Lo siento, es que sí.', 'No puedo, vale.'], '¡Qué buena idea! ¿A qué hora?', ('Accepter : ¡qué buena idea!', 'Accepting: ¡qué buena idea!')),
        DC(ANSWER, [('Amigo', '¿Quieres jugar al fútbol mañana?')], ('Ton ami te propose un match demain, mais tu dois travailler.', 'Your friend suggests a match tomorrow, but you have to work.'), ['Lo siento, no puedo: es que tengo que trabajar.', 'Vale, tengo que trabajar.', 'Sí, no puedo.'], 'Lo siento, no puedo: es que tengo que trabajar.', ('Refuser poliment : lo siento, no puedo, es que…', 'Declining politely: lo siento, no puedo, es que…')),
        FB(CHOOSE, '¿A qué hora ＿ ? — A las siete en la plaza.', ['quedamos', 'quedan', 'quedé'], 'quedamos', ('Nous : quedamos.', 'We: quedamos.'), ('À quelle heure on se retrouve ? — À sept heures sur la place.', 'What time shall we meet? — At seven in the square.')),
        FB(CHOOSE, 'Hoy no ＿ salir: estoy enfermo.', ['puedo', 'podo', 'pudo'], 'puedo', ('Poder → puedo (o → ue).', 'Poder → puedo (o → ue).'), ('Aujourd’hui je ne peux pas sortir : je suis malade.', 'I can’t go out today: I’m ill.')),
      ]),
  ]),
  CH('delea2-w7-c2', ('En direct de la fête', 'Live from the festival'), [
    L('es-gerundio', ('Je suis en train de danser : estar + gérondif', 'I’m dancing: estar + gerund'), ('Dire ce qui se passe en ce moment avec estar + gérondif.', 'Say what is happening right now with estar + gerund.'), 9, [
        ('Estar + gérondif = être en train de : estoy bailando, estás comiendo, está escribiendo. -ar → -ando, -er / -ir → -iendo.', 'Estar + gerund = to be doing something: estoy bailando, estás comiendo, está escribiendo. -ar → -ando, -er / -ir → -iendo.'),
        ('Gérondifs irréguliers : leer → leyendo, oír → oyendo, ir → yendo, dormir → durmiendo, pedir → pidiendo, decir → diciendo.', 'Irregular gerunds: leer → leyendo, oír → oyendo, ir → yendo, dormir → durmiendo, pedir → pidiendo, decir → diciendo.'),
        ('À la fête : bailar (danser), cantar (chanter), los fuegos artificiales (le feu d’artifice), el desfile (le défilé), la música, la gente (les gens).', 'At the festival: bailar (to dance), cantar (to sing), los fuegos artificiales (fireworks), el desfile (parade), la música, la gente (people).'),
      ], [
        SG('gerundio', 'estoy + -ando / -iendo', ('je suis en train de… (gérondif)', 'I am …-ing (gerund)')),
        S('leyendo', 'leyendo (leer)', ('en lisant (gérondif de leer)', 'reading (gerund of leer)')),
        S('durmiendo', 'durmiendo (dormir)', ('en dormant (gérondif de dormir)', 'sleeping (gerund of dormir)')),
        S('bailar', 'bailar', ('danser', 'to dance')),
        S('cantar', 'cantar', ('chanter', 'to sing')),
        S('fuegos', 'los fuegos artificiales', ('le feu d’artifice', 'the fireworks')),
        S('el-desfile', 'el desfile', ('le défilé', 'the parade')),
        S('la-gente', 'la gente', ('gens, personnes', 'people')),
      ], [
        x('¡Mira! La gente está bailando en la plaza y los niños están cantando.', 'Regarde ! Les gens dansent sur la place et les enfants chantent.', 'Look! People are dancing in the square and the children are singing.'),
        x('¿Dónde está Sancho? — Está durmiendo debajo de un árbol.', 'Où est Sancho ? — Il est en train de dormir sous un arbre.', 'Where’s Sancho? — He’s sleeping under a tree.'),
      ], [
        FB(CHOOSE, 'Ahora mismo estoy ＿ un libro.', ['leyendo', 'leiendo', 'leído'], 'leyendo', ('Leer → leyendo.', 'Leer → leyendo.'), ('En ce moment, je suis en train de lire un livre.', 'Right now I’m reading a book.')),
        FB(CHOOSE, 'Los músicos ＿ tocando en el desfile.', ['están', 'son', 'hay'], 'están', ('Estar + gérondif.', 'Estar + gerund.'), ('Les musiciens jouent dans le défilé.', 'The musicians are playing in the parade.')),
        FB(CHOOSE, 'No hagas ruido: el niño está ＿.', ['durmiendo', 'dormiendo', 'dormido'], 'durmiendo', ('Dormir → durmiendo.', 'Dormir → durmiendo.'), ('Ne fais pas de bruit : l’enfant dort.', 'Don’t make any noise: the child is sleeping.')),
        DC(ANSWER, [('Teresa', '¿Qué estás haciendo?')], ('Teresa t’appelle et demande ce que tu fais (tu regardes le feu d’artifice).', 'Teresa calls and asks what you are doing (you are watching the fireworks).'), ['Estoy viendo los fuegos artificiales.', 'Veo los fuegos ayer.', 'Estoy visto los fuegos.'], 'Estoy viendo los fuegos artificiales.', ('Action en cours : estoy + gérondif.', 'Ongoing action: estoy + gerund.')),
      ]),
  ])])

# ═════════════════════════ 8 : la plage de Barcelone — le travail, les pronoms COI, les conseils ═════════════════════════
W8 = WORLD('delea2-w8', ('La plage de Barcelone', 'The beach of Barcelona'), REGION,
  ('Parler de son travail et de ses études, écrire à quelqu’un avec les pronoms le et les, et donner des conseils et des obligations (hay que, deber, es mejor).', 'Talk about your work and studies, write to someone with the pronouns le and les, and give advice and obligations (hay que, deber, es mejor).'),
  (('Le Drac de Sant Jordi', 'The Drac of Sant Jordi'), 'Ñ', ('Sur la plage de Barcelone, le Drac, dragon de la légende de Sant Jordi, surgit des vagues et réclame un tribut. Le chevalier de la Blanche Lune l’attend… Prouve au Drac que tu sais travailler, écrire et conseiller en espagnol, et il replongera dans la mer.', 'On the beach of Barcelona, the Drac, the dragon of the Sant Jordi legend, rises from the waves and demands a tribute. The Knight of the White Moon is waiting… Prove to the Drac that you can work, write and give advice in Spanish, and it will dive back into the sea.')),
  [CH('delea2-w8-c1', ('Au port de Barcelone', 'At the port of Barcelona'), [
    L('es-trabajo', ('Le travail : la empresa, el horario', 'Work: la empresa, el horario'), ('Parler de son métier, de son lieu et de ses horaires de travail.', 'Talk about your job, workplace and working hours.'), 9, [
        ('Les métiers : el profesor / la profesora, el enfermero / la enfermera (infirmier), el cocinero (cuisinier), el abogado (avocat), el dependiente (vendeur), el ingeniero (ingénieur).', 'Jobs: el profesor / la profesora (teacher), el enfermero / la enfermera (nurse), el cocinero (cook), el abogado (lawyer), el dependiente (shop assistant), el ingeniero (engineer).'),
        ('Trabajo en una empresa (dans une entreprise), en una oficina, en un hospital. Trabajo como cocinero (je travaille comme cuisinier). ¿A qué te dedicas? = que fais-tu dans la vie ?', 'Trabajo en una empresa (in a company), en una oficina, en un hospital. Trabajo como cocinero (I work as a cook). ¿A qué te dedicas? = what do you do for a living?'),
        ('Le travail au quotidien : el horario (les horaires), el jefe / la jefa (le chef), los compañeros (les collègues), buscar trabajo (chercher du travail), el currículum (le CV).', 'Work day to day: el horario (working hours), el jefe / la jefa (the boss), los compañeros (colleagues), buscar trabajo (to look for work), el currículum (the CV).'),
      ], [
        S('a-que-te-dedicas', '¿A qué te dedicas?', ('Que fais-tu dans la vie ?', 'What do you do for a living?')),
        S('la-empresa', 'la empresa', ('l’entreprise', 'the company')),
        S('la-oficina', 'la oficina', ('le bureau (lieu)', 'the office')),
        S('el-horario', 'el horario', ('les horaires', 'the timetable, the working hours')),
        S('el-jefe', 'el jefe / la jefa', ('le chef / la cheffe', 'the boss')),
        S('el-companero', 'el compañero / la compañera', ('le collègue / la collègue, le camarade', 'the colleague, the classmate')),
        S('el-enfermero', 'el enfermero / la enfermera', ('l’infirmier / l’infirmière', 'the nurse')),
        S('el-cocinero', 'el cocinero / la cocinera', ('le cuisinier / la cuisinière', 'the cook')),
        S('buscar-trabajo', 'buscar trabajo', ('chercher du travail', 'to look for work')),
      ], [
        x('¿A qué te dedicas? — Soy enfermera. Trabajo en un hospital de Barcelona.', 'Que fais-tu dans la vie ? — Je suis infirmière. Je travaille dans un hôpital de Barcelone.', 'What do you do for a living? — I’m a nurse. I work in a hospital in Barcelona.'),
        x('Mi horario es de nueve a cinco y mis compañeros son muy simpáticos.', 'Mes horaires sont de neuf heures à cinq heures et mes collègues sont très sympathiques.', 'My hours are nine to five and my colleagues are very nice.'),
      ], [
        DC(ANSWER, [('Pescador', '¿A qué te dedicas?')], ('Un pêcheur te demande ce que tu fais dans la vie (tu es cuisinier·ère).', 'A fisherman asks what you do for a living (you are a cook).'), ['Soy cocinero, trabajo en un restaurante.', 'Me dedico a las nueve.', 'Tengo un horario.'], 'Soy cocinero, trabajo en un restaurante.', ('Métier : soy + métier (sans article).', 'Job: soy + job (no article).')),
        FB(COMPLETE, 'Mi ＿ es muy flexible: empiezo a las diez.', ['horario', 'jefe', 'currículum'], 'horario', ('Les horaires : el horario.', 'Working hours: el horario.'), ('Mes horaires sont très souples : je commence à dix heures.', 'My hours are very flexible: I start at ten.')),
        FB(COMPLETE, 'Estoy buscando ＿ y he enviado mi currículum a tres empresas.', ['trabajo', 'jefe', 'oficina'], 'trabajo', ('Chercher du travail : buscar trabajo.', 'To look for work: buscar trabajo.'), ('Je cherche du travail et j’ai envoyé mon CV à trois entreprises.', 'I’m looking for work and have sent my CV to three companies.')),
        TF('Trabaja como profesor en un colegio.', ('Il travaille dans une école.', 'He works at a school.'), VRAI, ('Un colegio = une école.', 'Un colegio = a school.')),
      ]),
    L('es-pronombres-oi', ('Je lui écris : le, les', 'I’m writing to him: le, les'), ('Employer les pronoms compléments indirects avec dar, decir, escribir, regalar.', 'Use indirect object pronouns with dar, decir, escribir, regalar.'), 10, [
        ('Pronoms COI : me, te, le (lui), nos, os, les (leur). Le escribo una carta a Dulcinea (j’écris une lettre à Dulcinée). On garde souvent le même si on nomme la personne.', 'Indirect object pronouns: me, te, le (to him/her), nos, os, les (to them). Le escribo una carta a Dulcinea (I’m writing a letter to Dulcinea). Le is usually kept even when the person is named.'),
        ('Les verbes qui les appellent : dar (donner), decir (dire), regalar (offrir), enviar (envoyer), pedir (demander quelque chose), prestar (prêter), contar (raconter).', 'Verbs that take them: dar (to give), decir (to say, tell), regalar (to give as a present), enviar (to send), pedir (to ask for), prestar (to lend), contar (to tell, recount).'),
        ('Comme lo et la, ils se placent avant le verbe conjugué ou s’accrochent à l’infinitif : Voy a regalarle un libro = Le voy a regalar un libro.', 'Like lo and la, they go before the conjugated verb or attach to the infinitive: Voy a regalarle un libro = Le voy a regalar un libro.'),
      ], [
        SG('le-les', 'le / les', ('lui / leur (pronoms COI)', 'to him-her / to them (indirect object pronouns)')),
        S('dar', 'dar', ('donner', 'to give')),
        S('regalar', 'regalar', ('offrir (un cadeau)', 'to give (as a present)')),
        S('enviar', 'enviar', ('envoyer', 'to send')),
        S('pedir', 'pedir', ('demander (quelque chose), commander', 'to ask for, to order')),
        S('prestar', 'prestar', ('prêter', 'to lend')),
        S('contar', 'contar', ('raconter, compter', 'to tell, to count')),
      ], [
        x('Don Quijote le escribe una carta a Dulcinea y Sancho se la lleva.', 'Don Quichotte écrit une lettre à Dulcinée et Sancho la lui porte.', 'Don Quixote writes a letter to Dulcinea and Sancho takes it to her.'),
        x('¿Qué les vas a regalar a tus padres? — Les voy a regalar un viaje.', 'Qu’est-ce que tu vas offrir à tes parents ? — Je vais leur offrir un voyage.', 'What are you going to give your parents? — I’m going to give them a trip.'),
      ], [
        FB(CHOOSE, 'Mañana es el cumpleaños de Ana: ＿ voy a regalar flores.', ['le', 'la', 'les'], 'le', ('À Ana (une personne) : le.', 'To Ana (one person): le.'), ('Demain, c’est l’anniversaire d’Ana : je vais lui offrir des fleurs.', 'Tomorrow is Ana’s birthday: I’m going to give her flowers.')),
        FB(CHOOSE, 'He visto a mis abuelos y ＿ he contado el viaje.', ['les', 'le', 'los'], 'les', ('À mes grands-parents : les.', 'To my grandparents: les.'), ('J’ai vu mes grands-parents et je leur ai raconté le voyage.', 'I saw my grandparents and told them about the trip.')),
        FB(CHOOSE, '¿Me ＿ tu bolígrafo, por favor?', ['prestas', 'pides', 'cuentas'], 'prestas', ('Prêter : prestar.', 'To lend: prestar.'), ('Tu me prêtes ton stylo, s’il te plaît ?', 'Can you lend me your pen, please?')),
        order(('Remets dans l’ordre : « Je lui envoie un message. »', 'Put in order: “I’m sending him a message.”'), ['Le', 'envío', 'un', 'mensaje.'], ('Le + verbe + complément.', 'Le + verb + object.')),
      ]),
  ]),
  CH('delea2-w8-c2', ('La veille du combat', 'The eve of the duel'), [
    L('es-consejos', ('Il faut s’entraîner : hay que, deber, es mejor', 'You need to train: hay que, deber, es mejor'), ('Exprimer l’obligation et donner des conseils.', 'Express obligation and give advice.'), 10, [
        ('Obligation générale : hay que + infinitif (il faut). Hay que llevar el pasaporte. Obligation personnelle : tener que (A1) ou deber + infinitif (devoir) : Debes descansar.', 'General obligation: hay que + infinitive (one must). Hay que llevar el pasaporte. Personal obligation: tener que (A1) or deber + infinitive: Debes descansar (you should rest).'),
        ('Conseiller : Es mejor + infinitif (il vaut mieux), ¿Por qué no…? (pourquoi ne pas… ?), Si tienes tiempo, visita el puerto (si tu as le temps, visite le port).', 'Advising: Es mejor + infinitive (it’s better to), ¿Por qué no…? (why don’t you…?), Si tienes tiempo, visita el puerto (if you have time, visit the port).'),
        ('Interdire : no se puede + infinitif (on ne peut pas), está prohibido (c’est interdit). No se puede fumar. Está prohibido bañarse.', 'Forbidding: no se puede + infinitive (you can’t), está prohibido (it is forbidden). No se puede fumar. Está prohibido bañarse (no swimming).'),
      ], [
        SG('hay-que', 'hay que + infinitivo', ('il faut + infinitif', 'one must, you have to')),
        SG('deber', 'deber + infinitivo', ('devoir + infinitif', 'should, must + verb')),
        S('es-mejor', 'es mejor + infinitivo', ('il vaut mieux…', 'it’s better to…')),
        S('no-se-puede', 'no se puede', ('on ne peut pas, il est interdit de', 'you can’t, it’s not allowed')),
        S('prohibido', 'prohibido / prohibida', ('interdit / interdite', 'forbidden')),
        S('el-consejo', 'el consejo', ('le conseil', 'the piece of advice')),
        S('entrenar', 'entrenar', ('s’entraîner', 'to train')),
        S('el-pasaporte', 'el pasaporte', ('le passeport', 'the passport')),
      ], [
        x('Mañana hay que levantarse pronto: debes entrenar antes del combate.', 'Demain, il faut se lever tôt : tu dois t’entraîner avant le combat.', 'Tomorrow we have to get up early: you must train before the duel.'),
        x('Es mejor no bañarse aquí: está prohibido y hay mucho viento.', 'Il vaut mieux ne pas se baigner ici : c’est interdit et il y a beaucoup de vent.', 'It’s better not to swim here: it’s forbidden and it’s very windy.'),
      ], [
        FB(CHOOSE, 'Para viajar a México ＿ llevar el pasaporte.', ['hay que', 'hay', 'debe que'], 'hay que', ('Obligation générale : hay que + infinitif.', 'General obligation: hay que + infinitive.'), ('Pour aller au Mexique, il faut avoir son passeport.', 'To travel to Mexico you have to take your passport.')),
        FB(CHOOSE, 'Estás muy cansado: ＿ dormir más.', ['debes', 'hay', 'es'], 'debes', ('Conseil personnel : deber + infinitif.', 'Personal advice: deber + infinitive.'), ('Tu es très fatigué : tu dois dormir davantage.', 'You’re very tired: you should sleep more.')),
        TF('En el museo no se puede hacer fotos.', ('On peut prendre des photos dans le musée.', 'You can take photos in the museum.'), FAUX, ('No se puede = c’est interdit.', 'No se puede = it’s not allowed.')),
        DC(ANSWER, [('Turista', 'Quiero ver Barcelona en un día. ¿Qué me aconsejas?')], ('Un touriste te demande un conseil pour visiter Barcelone en un jour.', 'A tourist asks you for advice on seeing Barcelona in a day.'), ['Es mejor ir a pie por el centro y visitar el puerto.', 'Hay que no Barcelona.', 'Debes visitado el puerto.'], 'Es mejor ir a pie por el centro y visitar el puerto.', ('Conseiller : es mejor + infinitif.', 'Advising: es mejor + infinitive.')),
      ]),
  ])])

write_level('DELEA2', ('DELE A2 : la route de Barcelone', 'DELE A2: the road to Barcelona'), REGION, 'Road to Barcelona', 55,
  [W1, W2, W3, W4, W5, W6, W7, W8, FINAL('DELEA2', REGION, ('Simulation DELE A2 : le chevalier de la Blanche Lune', 'DELE A2 simulation: the Knight of the White Moon'), 'compréhension écrite, compréhension auditive et expression écrite (l’oral n’est pas évalué)', 'reading comprehension, listening comprehension and written expression (speaking is not assessed)')])

