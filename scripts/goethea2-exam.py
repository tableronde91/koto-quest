# Banque de questions de l'examen blanc Goethe-Zertifikat A2 (content/exams/goethea2.json), au format de l'épreuve
# officielle du Goethe-Institut : Lesen (20 questions en 4 parties), Hören (20 questions en 4 parties) et Schreiben
# (ici en format à choix : un SMS et un courriel). L'épreuve orale (Sprechen) n'est pas évaluée.
# 90 minutes, notation sur 100, réussite à partir de 60 points.
# Usage : python3 scripts/goethea2-exam.py
from goethe_exam import *

# ═════════════════════════ Hören ═════════════════════════
H1 = PART('h-radio', 'listening', 'Hören — Teil 1', 'Radio, annonces et répondeur', 'Sie hören fünf kurze Texte. Wählen Sie die richtige Lösung.', 5, [
  LQ('N|Und jetzt das Wetter für morgen: Am Vormittag regnet es noch im ganzen Land. Am Nachmittag kommt die Sonne, und es wird bis zu zwanzig Grad warm.', ['Am Nachmittag scheint die Sonne.', 'Es regnet den ganzen Tag.', 'Es wird kälter als heute.'], 'Wie wird das Wetter morgen?'),
  LQ('N|Achtung an Gleis sieben: Der ICE nach Freiburg, Abfahrt 14.12 Uhr, hat heute circa zwanzig Minuten Verspätung. Wir bitten um Entschuldigung.', ['Der Zug kommt später.', 'Der Zug fällt aus.', 'Der Zug fährt von einem anderen Gleis.'], 'Was ist mit dem Zug nach Freiburg?'),
  LQ('F|Guten Tag, Herr Lang, hier ist die Praxis Doktor Weber. Ihr Termin am Donnerstag fällt leider aus. Können Sie am Freitag um halb elf kommen? Bitte rufen Sie uns zurück.', ['Am Freitag um 10.30 Uhr.', 'Am Donnerstag um 10.30 Uhr.', 'Am Freitag um 11.30 Uhr.'], 'Wann ist der neue Termin?'),
  LQ('N|Liebe Kundinnen und Kunden, heute im Angebot: frisches Brot aus unserer Bäckerei für nur zwei Euro und Äpfel aus der Region, das Kilo für einen Euro neunundneunzig.', ['Brot und Äpfel.', 'Käse und Milch.', 'Kuchen und Kaffee.'], 'Was ist heute im Angebot?'),
  LQ('M|Hallo Julia, hier ist Markus. Ich stehe im Stau und komme eine halbe Stunde später zum Kino. Kauf bitte schon die Karten, ich gebe dir das Geld später.', ['Die Kinokarten kaufen.', 'Auf Markus zu Hause warten.', 'Markus mit dem Auto abholen.'], 'Was soll Julia tun?'),
  LQ('N|Verkehrsmeldung: Auf der A5 zwischen Karlsruhe und Baden-Baden gibt es nach einem Unfall fünf Kilometer Stau. Bitte fahren Sie langsam.', ['Es gibt einen Stau.', 'Die Autobahn ist geschlossen.', 'Es schneit stark.'], 'Was ist auf der A5 los?'),
  LQ('F|Sie hören den Anrufbeantworter der Stadtbibliothek. Wir sind von Dienstag bis Samstag von zehn bis achtzehn Uhr für Sie da. Am Montag ist die Bibliothek geschlossen.', ['Am Montag.', 'Am Samstag.', 'Am Dienstag.'], 'Wann ist die Bibliothek geschlossen?'),
], listening=True)

G2 = ('F|Na, Tim, wie war deine Woche?\n'
      'M|Ziemlich voll! Am Montag habe ich bis acht Uhr im Büro gearbeitet. Am Dienstag bin ich mit Lena ins Kino gegangen.\n'
      'F|Und am Mittwoch?\n'
      'M|Da war ich beim Zahnarzt. Am Donnerstag habe ich für meine Eltern eingekauft, und am Freitag habe ich endlich Fußball gespielt.\n'
      'F|Und das Wochenende?\n'
      'M|Am Samstag habe ich lange geschlafen und dann meine Wohnung geputzt. Am Sonntag bin ich mit dem Zug zu meiner Schwester nach Heidelberg gefahren.')
H2 = PART('h-woche', 'listening', 'Hören — Teil 2', 'Une conversation : la semaine de Tim', 'Sie hören ein Gespräch. Was hat Tim an diesem Tag gemacht?', 5, [
  LQ(G2, ['Er hat lange gearbeitet.', 'Er war im Kino.', 'Er hat Fußball gespielt.'], 'Montag'),
  LQ(G2, ['Er ist ins Kino gegangen.', 'Er war beim Zahnarzt.', 'Er hat eingekauft.'], 'Dienstag'),
  LQ(G2, ['Er war beim Zahnarzt.', 'Er hat die Wohnung geputzt.', 'Er hat gearbeitet.'], 'Mittwoch'),
  LQ(G2, ['Er hat für seine Eltern eingekauft.', 'Er hat Fußball gespielt.', 'Er ist nach Heidelberg gefahren.'], 'Donnerstag'),
  LQ(G2, ['Er hat Fußball gespielt.', 'Er hat lange geschlafen.', 'Er war im Kino.'], 'Freitag'),
  LQ(G2, ['Er hat geschlafen und geputzt.', 'Er hat seine Schwester besucht.', 'Er hat eingekauft.'], 'Samstag'),
  LQ(G2, ['Er hat seine Schwester besucht.', 'Er hat die Wohnung geputzt.', 'Er war im Büro.'], 'Sonntag'),
], listening=True)

H3 = PART('h-gespraeche', 'listening', 'Hören — Teil 3', 'Dialogues courts', 'Sie hören fünf kurze Gespräche. Wählen Sie die richtige Lösung.', 5, [
  LQ('F|Entschuldigung, ich suche die Apotheke.\nM|Gehen Sie hier geradeaus bis zur Kirche. Die Apotheke ist direkt dahinter.', ['Hinter der Kirche.', 'Neben dem Bahnhof.', 'Vor der Schule.'], 'Wo ist die Apotheke?'),
  LQ('M|Was hast du deiner Mutter zum Geburtstag geschenkt?\nF|Zuerst wollte ich Blumen kaufen, aber dann habe ich ein Buch genommen. Sie liest so gern.', ['Ein Buch.', 'Blumen.', 'Einen Kuchen.'], 'Was hat die Frau geschenkt?'),
  LQ('F|Wie kommst du morgen zur Arbeit? Die Busse fahren doch nicht.\nM|Ich weiß. Ich nehme das Fahrrad, das Auto ist in der Werkstatt.', ['Mit dem Fahrrad.', 'Mit dem Bus.', 'Mit dem Auto.'], 'Wie fährt der Mann morgen zur Arbeit?'),
  LQ('M|Guten Tag, ich hätte gern ein Doppelzimmer für zwei Nächte.\nF|Gern. Mit Frühstück kostet das hundertsechzig Euro für beide Nächte.', ['160 Euro.', '116 Euro.', '60 Euro.'], 'Wie viel kostet das Zimmer für zwei Nächte?'),
  LQ('F|Warum warst du gestern nicht im Deutschkurs?\nM|Ich war krank. Ich hatte Fieber und bin den ganzen Tag im Bett geblieben.', ['Er war krank.', 'Er hatte Urlaub.', 'Er musste arbeiten.'], 'Warum war der Mann nicht im Kurs?'),
  LQ('M|Welche Wohnung nimmst du jetzt?\nF|Die im Zentrum ist schöner, aber zu teuer. Ich nehme die kleinere am Stadtrand, die ist ruhiger.', ['Die kleinere am Stadtrand.', 'Die teure im Zentrum.', 'Keine von beiden.'], 'Welche Wohnung nimmt die Frau?'),
  LQ('F|Sollen wir uns um sieben vor dem Restaurant treffen?\nM|Lieber um halb acht, ich muss noch meinen Sohn vom Sport abholen.', ['Um halb acht.', 'Um sieben.', 'Um acht.'], 'Wann treffen sie sich?'),
], listening=True)

G4 = ('F|Herzlich willkommen bei Radio Schwarzwald. Mein Gast heute ist Jonas Keller. Jonas, Sie sind Koch von Beruf. Warum?\n'
      'M|Weil ich schon als Kind gern mit meiner Großmutter gekocht habe. Mit sechzehn habe ich dann die Ausbildung in einem Hotel angefangen.\n'
      'F|Und heute haben Sie ein eigenes Restaurant.\n'
      'M|Ja, seit drei Jahren, in Freiburg. Wir sind sechs Kollegen. Am Montag ist geschlossen, da habe ich frei.\n'
      'F|Was gefällt Ihnen nicht so an Ihrem Beruf?\n'
      'M|Die Arbeitszeiten. Ich arbeite fast jeden Abend und oft am Wochenende. Meine Familie sehe ich zu wenig.\n'
      'F|Und Ihre Pläne für die Zukunft?\n'
      'M|Nächstes Jahr werde ich ein Kochbuch schreiben, mit Rezepten aus der Region.')
H4 = PART('h-interview', 'listening', 'Hören — Teil 4', 'Une interview : vrai ou faux', 'Sie hören ein Interview. Sind die Aussagen richtig oder falsch?', 5, [
  LQ(G4, R, 'Jonas hat als Kind gern mit seiner Großmutter gekocht.'),
  LQ(G4, F, 'Er hat seine Ausbildung in einer Bäckerei gemacht.'),
  LQ(G4, R, 'Sein Restaurant ist in Freiburg.'),
  LQ(G4, F, 'Am Montag arbeitet er.'),
  LQ(G4, R, 'Er findet, dass er seine Familie zu wenig sieht.'),
  LQ(G4, R, 'Er möchte ein Kochbuch schreiben.'),
  LQ(G4, F, 'Das Restaurant gibt es seit zehn Jahren.'),
], listening=True)

# ═════════════════════════ Lesen ═════════════════════════
ARTIKEL = ('NEU IN UNSERER STADT: DAS MÄRCHENCAFÉ\n'
           'Seit einem Monat gibt es in der Schlossstraße ein besonderes Café. Die Besitzerin, Clara Roth, hat früher als Lehrerin gearbeitet. '
           '„Ich habe meinen Schülern immer Märchen vorgelesen“, sagt sie. „Jetzt mache ich das für alle.“ Jeden Samstag um 15 Uhr liest sie im Café ein Märchen der Brüder Grimm vor. '
           'Der Eintritt ist frei, aber man sollte einen Platz reservieren, weil das Café sehr klein ist. Auf der Karte stehen Kuchen mit Namen wie „Rotkäppchen“ oder „Schneewittchen“. '
           'Am beliebtesten ist der Apfelkuchen. Das Café ist von Mittwoch bis Sonntag geöffnet. Im Sommer möchte Frau Roth auch im Garten vorlesen.')
L1 = PART('l-artikel', 'reading', 'Lesen — Teil 1', 'Un article de journal', 'Lesen Sie den Text und wählen Sie die richtige Lösung.', 5, [
  RP(ARTIKEL, 'Clara Roth …', ['war früher Lehrerin.', 'ist Köchin von Beruf.', 'arbeitet noch in einer Schule.']),
  RP(ARTIKEL, 'Am Samstag um 15 Uhr …', ['liest Frau Roth ein Märchen vor.', 'ist das Café geschlossen.', 'gibt es einen Kochkurs.']),
  RP(ARTIKEL, 'Man sollte reservieren, weil …', ['das Café klein ist.', 'der Eintritt teuer ist.', 'es nur am Samstag geöffnet ist.']),
  RP(ARTIKEL, 'Die Gäste essen am liebsten …', ['Apfelkuchen.', 'Rotkäppchen-Kuchen.', 'Suppe.']),
  RP(ARTIKEL, 'Im Sommer …', ['will Frau Roth auch im Garten vorlesen.', 'ist das Café geschlossen.', 'liest Frau Roth nicht mehr vor.']),
  RP(ARTIKEL, 'Das Café gibt es …', ['seit einem Monat.', 'seit einem Jahr.', 'seit letzter Woche.']),
])

HAUS = ('KAUFHAUS AM MARKT — Wegweiser\n'
        '3. Stock: Restaurant, Kinderspielplatz, Toiletten\n'
        '2. Stock: Möbel, Lampen, Betten, Küchen\n'
        '1. Stock: Damenmode, Herrenmode, Schuhe, Kinderkleidung\n'
        'Erdgeschoss: Bücher, Zeitungen, Handys und Computer, Blumen, Information\n'
        'Untergeschoss: Supermarkt, Bäckerei, Apotheke')
L2 = PART('l-kaufhaus', 'reading', 'Lesen — Teil 2', 'Le plan d’un grand magasin', 'Lesen Sie den Wegweiser. In welchen Stock gehen Sie?', 5, [
  RP(HAUS, 'Sie brauchen einen neuen Tisch für Ihre Küche.', ['2. Stock', '1. Stock', 'Erdgeschoss']),
  RP(HAUS, 'Sie möchten Tabletten gegen Husten kaufen.', ['Untergeschoss', 'Erdgeschoss', '3. Stock']),
  RP(HAUS, 'Sie suchen einen Mantel für Ihren Sohn.', ['1. Stock', '2. Stock', 'Untergeschoss']),
  RP(HAUS, 'Ihr Handy ist kaputt. Sie möchten ein neues.', ['Erdgeschoss', '2. Stock', '1. Stock']),
  RP(HAUS, 'Sie haben Hunger und möchten etwas Warmes essen.', ['3. Stock', 'Untergeschoss', 'Erdgeschoss']),
  RP(HAUS, 'Sie möchten Ihrer Freundin Blumen mitbringen.', ['Erdgeschoss', 'Untergeschoss', '3. Stock']),
  RP(HAUS, 'Sie brauchen Brot für das Frühstück.', ['Untergeschoss', '3. Stock', '1. Stock']),
])

MAILT = ('Liebe Sophie,\nvielen Dank für deine Einladung! Ich komme sehr gern zu deiner Party am Samstag. Leider kann ich erst um neun Uhr da sein, '
         'weil ich bis acht arbeiten muss. Soll ich etwas mitbringen? Ich könnte einen Salat machen oder Getränke kaufen. '
         'Mein Bruder Felix ist gerade bei mir zu Besuch. Darf er auch mitkommen? Er ist sehr nett und kennt hier noch niemanden. '
         'Nach der Party können wir bei mir schlafen, dann musst du nicht für uns aufräumen. '
         'Übrigens: Ich habe letzte Woche deine Schwester in der Stadt getroffen. Sie hat mir erzählt, dass du eine neue Stelle hast. Herzlichen Glückwunsch!\n'
         'Bis Samstag und liebe Grüße\nMarie')
L3 = PART('l-email', 'reading', 'Lesen — Teil 3', 'Un courriel', 'Lesen Sie die E-Mail und wählen Sie die richtige Lösung.', 5, [
  RP(MAILT, 'Marie kommt später zur Party, weil …', ['sie arbeiten muss.', 'ihr Bruder krank ist.', 'sie einen Salat machen muss.']),
  RP(MAILT, 'Marie möchte wissen, …', ['ob sie etwas mitbringen soll.', 'wo Sophie wohnt.', 'wann die Party anfängt.']),
  RP(MAILT, 'Felix …', ['besucht gerade seine Schwester.', 'wohnt schon lange in der Stadt.', 'kennt Sophie gut.']),
  RP(MAILT, 'Nach der Party …', ['schlafen Marie und Felix bei Marie.', 'schlafen alle bei Sophie.', 'fährt Felix nach Hause.']),
  RP(MAILT, 'Sophie hat …', ['eine neue Arbeit.', 'eine neue Wohnung.', 'eine neue Schwester.']),
  RP(MAILT, 'Marie hat Sophies Schwester …', ['letzte Woche getroffen.', 'zur Party eingeladen.', 'noch nie gesehen.']),
])

ANZ = {
  'a': 'A — SPRACHSCHULE LINGUA: Deutschkurse am Abend für Berufstätige. Montag und Mittwoch, 18.30 bis 20 Uhr. Kleine Gruppen.',
  'b': 'B — FAHRRAD-FRITZ: Wir reparieren Ihr Fahrrad in 24 Stunden. Auch gebrauchte Fahrräder ab 80 Euro.',
  'c': 'C — WOHNEN IM GRÜNEN: Helle 3-Zimmer-Wohnung mit Garten, ruhig, 10 Minuten zum Bahnhof. 850 Euro warm.',
  'd': 'D — RESTAURANT ZUM GOLDENEN HIRSCH sucht Koch / Köchin in Teilzeit. Erfahrung erwünscht. Tel. 0761 23 45 67.',
  'e': 'E — SCHWIMMKURSE FÜR KINDER ab 5 Jahren. Jeden Samstagvormittag im Stadtbad. Anmeldung online.',
  'f': 'F — COMPUTER-HILFE zu Hause: Ich installiere Programme und erkläre alles in Ruhe. 20 Euro pro Stunde.',
}
ALLE = '\n'.join(ANZ.values())
OPT = ['Anzeige A', 'Anzeige B', 'Anzeige C', 'Anzeige D', 'Anzeige E', 'Anzeige F']
def AN(situation, letter, wrong):
    return RP(ALLE, situation, ['Anzeige ' + letter] + ['Anzeige ' + w for w in wrong])
L4 = PART('l-anzeigen', 'reading', 'Lesen — Teil 4', 'Petites annonces', 'Lesen Sie die Anzeigen. Welche Anzeige passt zu welcher Person?', 5, [
  AN('Herr Yilmaz arbeitet den ganzen Tag und möchte nach der Arbeit Deutsch lernen.', 'A', ['E', 'F']),
  AN('Frau Berg sucht eine Wohnung für ihre Familie. Sie möchte nicht im Zentrum wohnen.', 'C', ['A', 'D']),
  AN('Das Fahrrad von Lukas ist kaputt. Er braucht es morgen wieder.', 'B', ['C', 'F']),
  AN('Die Tochter von Frau Kim ist sechs Jahre alt und kann noch nicht schwimmen.', 'E', ['A', 'B']),
  AN('Herr Braun ist Koch und möchte nur zwanzig Stunden pro Woche arbeiten.', 'D', ['B', 'C']),
  AN('Frau Schulz ist siebzig und versteht ihren neuen Laptop nicht.', 'F', ['A', 'E']),
])

# ═════════════════════════ Schreiben ═════════════════════════
S1 = PART('s-sms', 'writing', 'Schreiben — Teil 1', 'Un SMS', 'Lesen Sie die Situation und wählen Sie die beste Nachricht.', 2, [
  RQ(['Hallo Tom, es tut mir leid, ich komme zwanzig Minuten später, weil mein Bus Verspätung hat. Wir treffen uns direkt vor dem Kino. Bis gleich! Anna',
      'Hallo Tom, es tut mir leid, ich komme zwanzig Minuten später, weil mein Bus hat Verspätung. Wir treffen uns direkt vor das Kino. Bis gleich!',
      'Tom, Bus, später, Kino.',
      'Hallo Tom, ich bin pünktlich, weil mein Bus Verspätung hat. Wir treffen uns gestern vor dem Kino.'],
     '★ Situation: Sie sind mit Tom verabredet und kommen zu spät. Schreiben Sie: Entschuldigung, warum Sie später kommen, wo Sie sich treffen.'),
  RQ(['Liebe Frau Meier, ich bin heute leider krank und kann nicht zum Kurs kommen. Könnten Sie mir bitte die Hausaufgaben schicken? Vielen Dank und viele Grüße, Paul Martin',
      'Liebe Frau Meier, ich bin heute leider krank und kann nicht zum Kurs gekommen. Könnten Sie mich bitte die Hausaufgaben schicken?',
      'Hallo, bin krank. Hausaufgaben?',
      'Liebe Frau Meier, ich komme heute zum Kurs, weil ich krank bin. Schicken Sie die Hausaufgaben nicht.'],
     '★ Situation: Sie können heute nicht zum Deutschkurs kommen. Schreiben Sie Ihrer Lehrerin: warum, und bitten Sie um die Hausaufgaben.'),
  RQ(['Hallo Lena, danke für die Einladung! Ich komme gern am Freitag. Soll ich etwas zu trinken mitbringen? Wann fängt die Party an? Liebe Grüße, Max',
      'Hallo Lena, danke für die Einladung! Ich komme gern am Freitag. Soll ich etwas zu trinken mitbringe? Wann die Party fängt an?',
      'Lena, Freitag ok. Trinken? Wann?',
      'Hallo Lena, danke für die Einladung! Ich kann leider nicht, aber ich komme gern am Freitag nicht.'],
     '★ Situation: Lena hat Sie zu einer Party eingeladen. Schreiben Sie: Dank, dass Sie kommen, eine Frage zum Mitbringen, eine Frage zur Uhrzeit.'),
])

S2 = PART('s-email', 'writing', 'Schreiben — Teil 2', 'Un courriel', 'Lesen Sie die Situation und wählen Sie die passende Antwort.', 3, [
  RQ(['Sehr geehrter Herr Braun,', 'Hallo Braun,', 'Lieber Chef Braun!', 'Hi,'],
     '★ Sie schreiben Ihrem neuen Vermieter, Herrn Braun, eine E-Mail. Wie beginnen Sie?'),
  RQ(['Mit freundlichen Grüßen', 'Tschüss und bis bald', 'Liebe Grüße und Küsse', 'Mach’s gut'],
     '★ Wie beenden Sie die E-Mail an Herrn Braun?'),
  RQ(['Könnten Sie mir bitte sagen, wann ich den Schlüssel abholen kann?', 'Sag mir, wann ich den Schlüssel abhole!', 'Wann ich kann den Schlüssel abholen?', 'Ich will den Schlüssel jetzt.'],
     '★ Sie möchten höflich fragen, wann Sie den Wohnungsschlüssel bekommen. Was schreiben Sie?'),
  RQ(['Ich habe die Wohnung am Samstag gesehen, und sie hat mir sehr gut gefallen.', 'Ich habe die Wohnung am Samstag gesehen, und sie hat mich sehr gut gefallen.', 'Ich bin die Wohnung am Samstag gesehen.', 'Ich sehe die Wohnung letzten Samstag.'],
     '★ Sie möchten schreiben, dass Sie die Wohnung besichtigt haben und sie mögen. Was ist richtig?'),
  RQ(['Leider kann ich am Montag nicht kommen, weil ich arbeiten muss.', 'Leider ich kann am Montag nicht kommen, weil ich muss arbeiten.', 'Leider kann ich am Montag nicht kommen, denn ich arbeiten muss.', 'Leider kommen ich am Montag nicht.'],
     '★ Sie können am Montag nicht zum Termin kommen und geben den Grund an. Was ist richtig?'),
])

write_bank('GOETHEA2', [H1, H2, H3, H4, L1, L2, L3, L4, S1, S2], (20, 20, 5),
  'Questions rédigées par Koto Quest au format de l’examen officiel Goethe-Zertifikat A2 (Goethe-Institut : types d’épreuves, consignes en allemand, notation sur 100, réussite à 60 points). L’épreuve Schreiben se fait par choix multiple et l’épreuve orale (Sprechen) n’est pas évaluée. Ce ne sont pas des questions officielles.',
  'Questions written by Koto Quest in the format of the official Goethe-Zertifikat A2 exam (Goethe-Institut: question types, instructions in German, scoring out of 100, pass at 60 points). The Schreiben test is multiple choice and the speaking test (Sprechen) is not assessed. They are not official questions.',
  {'Radio, annonces et répondeur': 'Radio, announcements and voicemail', 'Une conversation : la semaine de Tim': 'A conversation: Tim’s week', 'Dialogues courts': 'Short dialogues',
   'Une interview : vrai ou faux': 'An interview: true or false', 'Un article de journal': 'A newspaper article', 'Le plan d’un grand magasin': 'A department store directory',
   'Un courriel': 'An email', 'Petites annonces': 'Small ads', 'Un SMS': 'A text message'})
