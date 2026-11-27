# Banque de questions de l'examen blanc Goethe-Zertifikat B2 (content/exams/goetheb2.json), au format de l'épreuve
# officielle du Goethe-Institut : Hören (30 questions en 4 parties), Lesen (30 questions en 5 parties) et Schreiben
# (ici en format à choix : contribution à un forum, message formel). L'épreuve orale (Sprechen) n'est pas évaluée.
# 180 minutes ; chaque module est noté sur 100 et se valide séparément à partir de 60 points.
# Usage : python3 scripts/goetheb2-exam.py
from goethe_exam import *

# ═════════════════════════ Hören ═════════════════════════
def PAIR(audio, aussage, richtig, frage, choices):
    """Teil 1 : un texte, une affirmation vrai / faux puis une question à choix."""
    return [LQ(audio, R if richtig else F, aussage), LQ(audio, choices, frage)]

T1 = [
  PAIR('F|Sie hören nun einen Hinweis für alle Teilnehmenden der Tagung „Arbeit im Wandel“. Der Vortrag von Professor Lindner über künstliche Intelligenz im Büro muss leider entfallen, da der Referent wegen eines Streiks am Flughafen nicht anreisen konnte. Stattdessen findet im selben Saal eine Podiumsdiskussion statt. Die Folien des Vortrags werden Ihnen im Laufe der Woche per E-Mail zugeschickt.',
       'Der Vortrag wird auf den Nachmittag verschoben.', False, 'Was erhalten die Teilnehmenden später?', ['Die Folien des Vortrags.', 'Ihr Geld zurück.', 'Eine Einladung zur nächsten Tagung.']),
  PAIR('M|Guten Tag, Frau Petrović, hier spricht Baumann von der Hausverwaltung. Sie hatten sich wegen des Wasserschadens in Ihrem Bad gemeldet. Der Handwerker könnte am Donnerstag zwischen acht und zwölf Uhr kommen. Sollten Sie dann nicht zu Hause sein, können Sie den Schlüssel bei Ihrer Nachbarin hinterlegen. Die Kosten übernimmt selbstverständlich der Vermieter.',
       'Frau Petrović muss die Reparatur selbst bezahlen.', False, 'Was soll Frau Petrović tun, falls sie nicht da ist?', ['Den Schlüssel bei der Nachbarin lassen.', 'Einen neuen Termin vereinbaren.', 'Den Handwerker selbst anrufen.']),
  PAIR('N|Wissenschaft aktuell: Laut einer Studie der Universität Jena lernen Erwachsene Vokabeln deutlich besser, wenn sie kurz nach dem Lernen schlafen. Die Forscher vermuten, dass das Gehirn im Schlaf neue Informationen sortiert. Wer also abends lernt, behält am nächsten Tag bis zu vierzig Prozent mehr als jemand, der morgens lernt und den ganzen Tag wach bleibt.',
       'Der Studie zufolge ist es günstig, am Abend zu lernen.', True, 'Was vermuten die Forscher?', ['Dass das Gehirn im Schlaf Informationen ordnet.', 'Dass Erwachsene schlechter lernen als Kinder.', 'Dass man morgens konzentrierter ist.']),
  PAIR('F|Hallo Markus, ich bin’s, Irene. Ich wollte dir nur sagen, dass ich mich nun doch für die Stelle in Weimar entschieden habe. Das Gehalt ist zwar etwas niedriger als in Hamburg, aber die Aufgaben sind viel interessanter, und ich könnte zwei Tage pro Woche von zu Hause aus arbeiten. Wenn ich das Angebot abgelehnt hätte, hätte ich es bestimmt bereut.',
       'Irene verdient in Weimar mehr als in Hamburg.', False, 'Warum hat Irene die Stelle angenommen?', ['Weil die Aufgaben interessanter sind.', 'Weil sie nicht mehr im Büro arbeiten muss.', 'Weil Markus in Weimar wohnt.']),
  PAIR('N|Verkehrshinweis: Auf der A4 zwischen Erfurt und Weimar hat sich nach einem Unfall mit einem Lastwagen ein Stau von zwölf Kilometern Länge gebildet. Die Fahrbahn in Richtung Dresden bleibt voraussichtlich bis achtzehn Uhr gesperrt. Autofahrern wird empfohlen, die Autobahn an der Ausfahrt Erfurt-Ost zu verlassen und der Umleitung zu folgen.',
       'Die Autobahn ist in Richtung Dresden gesperrt.', True, 'Was wird den Autofahrern geraten?', ['Die Autobahn zu verlassen.', 'Im Stau zu warten.', 'Erst nach achtzehn Uhr loszufahren.']),
]
H1 = PART('h-kurztexte', 'listening', 'Hören — Teil 1', 'Textes courts : vrai ou faux, puis une question', 'Sie hören fünf kurze Texte. Zu jedem Text lösen Sie zwei Aufgaben.', 10, [q for pair in T1 for q in pair], listening=True)

INTERVIEW = ('F|Kultur am Mittag. Bei mir im Studio ist heute Jonas Reuter, der seit drei Jahren als Stadtschreiber in Weimar lebt. Herr Reuter, was macht ein Stadtschreiber eigentlich?\n'
             'M|Im Grunde werde ich dafür bezahlt, die Stadt zu beobachten und darüber zu schreiben. Die Stadt stellt mir eine Wohnung zur Verfügung, und ich veröffentliche jeden Monat einen Text in der Lokalzeitung.\n'
             'F|Sie stammen aus Hamburg. War die Umstellung schwer?\n'
             'M|Anfangs schon. Ich hatte befürchtet, dass Weimar ein einziges Museum sei, in dem sich alles um Goethe und Schiller dreht. Inzwischen habe ich festgestellt, dass hier erstaunlich viele junge Leute leben, vor allem wegen der Universität.\n'
             'F|Worüber schreiben Sie am liebsten?\n'
             'M|Nicht über die berühmten Dichter, sondern über die Menschen, denen ich im Alltag begegne: die Bäckerin, den Busfahrer, die Studenten im Park. Mich interessiert, wie man in einer Stadt lebt, deren Vergangenheit so groß ist.\n'
             'F|Gab es auch Kritik an Ihren Texten?\n'
             'M|Natürlich. Als ich schrieb, dass die Innenstadt abends wie ausgestorben wirke, haben sich einige Leser beschwert. Andere haben mir allerdings zugestimmt. Ich finde, ein Stadtschreiber sollte nicht nur loben.\n'
             'F|Ihre Zeit hier endet im Sommer. Was nehmen Sie mit?\n'
             'M|Vor allem die Erkenntnis, dass man eine Stadt erst versteht, wenn man langsam durch sie geht. Ich habe hier kein Auto gebraucht. Und ich arbeite an einem Roman, der in Weimar spielt, allerdings in der Gegenwart.')
H2 = PART('h-interview', 'listening', 'Hören — Teil 2', 'Une interview à la radio', 'Sie hören ein Interview. Wählen Sie die richtige Lösung.', 6, [
  LQ(INTERVIEW, ['Er schreibt regelmäßig Texte über die Stadt.', 'Er führt Touristen durch die Stadt.', 'Er leitet das Goethe-Museum.'], 'Was ist die Aufgabe von Herrn Reuter?'),
  LQ(INTERVIEW, ['Eine Wohnung.', 'Ein Auto.', 'Ein Büro in der Zeitung.'], 'Was bekommt er von der Stadt?'),
  LQ(INTERVIEW, ['Dass sich alles nur um die Dichter dreht.', 'Dass er keine Wohnung findet.', 'Dass zu viele Studenten dort leben.'], 'Was hatte er vor seinem Umzug befürchtet?'),
  LQ(INTERVIEW, ['Über Menschen aus dem Alltag.', 'Über Goethe und Schiller.', 'Über die Geschichte der Universität.'], 'Worüber schreibt er am liebsten?'),
  LQ(INTERVIEW, ['Sie waren unterschiedlicher Meinung.', 'Sie haben ihm alle zugestimmt.', 'Sie haben seine Texte nicht gelesen.'], 'Wie haben die Leser auf seine Kritik an der Innenstadt reagiert?'),
  LQ(INTERVIEW, ['Einen Roman, der im heutigen Weimar spielt.', 'Ein Buch über Goethes Leben.', 'Einen Reiseführer für Autofahrer.'], 'Woran arbeitet er zurzeit?'),
], listening=True)

RUNDE = ('N|Campusradio, die Gesprächsrunde. Heute geht es um die Frage, ob man nach dem Abitur sofort studieren oder erst ein Jahr Pause machen sollte. Zu Gast sind Lena, die ein Jahr in Chile verbracht hat, und Paul, der direkt mit dem Studium begonnen hat.\n'
         'F|Für mich war das Jahr im Ausland die beste Entscheidung. Ich hatte nach der Schule keine Ahnung, was ich studieren wollte. Hätte ich sofort angefangen, hätte ich wahrscheinlich das falsche Fach gewählt.\n'
         'M|Das kann ich verstehen, aber so ein Jahr muss man sich auch leisten können. Meine Eltern hätten mir das nicht bezahlen können.\n'
         'F|Ich habe dort gearbeitet, in einem Kindergarten. Reich wird man dabei nicht, aber es reicht zum Leben.\n'
         'M|Trotzdem: Wer ein Jahr aussetzt, verliert die Gewohnheit zu lernen. Ich habe an meinen Freunden gesehen, wie schwer ihnen der Anfang an der Uni gefallen ist.\n'
         'F|Bei mir war es umgekehrt. Ich war viel motivierter, weil ich endlich wusste, wofür ich lerne. Und selbstständiger war ich auch.\n'
         'M|Selbstständig wird man auch, wenn man in eine andere Stadt zieht und allein wohnt. Dafür muss man nicht um die halbe Welt fliegen.\n'
         'F|Da hast du recht. Aber eine Fremdsprache lernt man zu Hause nicht so gut.\n'
         'M|Stimmt. Mein Spanisch ist jedenfalls furchtbar. Vielleicht gehe ich im Master für ein Semester ins Ausland.\n'
         'N|Man sieht: Den einen richtigen Weg gibt es wohl nicht. Vielen Dank euch beiden.')
WER = ['Lena', 'Paul', 'Der Moderator']
def WHO3(first):
    return [first] + [w for w in WER if w != first]
H3 = PART('h-gespraechsrunde', 'listening', 'Hören — Teil 3', 'Une table ronde : qui dit quoi ?', 'Sie hören ein Gespräch mit mehreren Personen. Wer sagt was?', 6, [
  LQ(RUNDE, WHO3('Lena'), 'Ohne die Pause hätte ich vermutlich das Falsche studiert.'),
  LQ(RUNDE, WHO3('Paul'), 'Nicht jede Familie kann ein solches Jahr finanzieren.'),
  LQ(RUNDE, WHO3('Paul'), 'Nach einer langen Pause fällt das Lernen schwerer.'),
  LQ(RUNDE, WHO3('Lena'), 'Nach dem Jahr war ich motivierter als vorher.'),
  LQ(RUNDE, WHO3('Paul'), 'Auch in einer anderen deutschen Stadt wird man selbstständig.'),
  LQ(RUNDE, WHO3('Der Moderator'), 'Es gibt nicht nur eine richtige Lösung.'),
], listening=True)

VORTRAG = ('F|Meine Damen und Herren, ich begrüße Sie zu meinem Vortrag „Wie viel Arbeit braucht der Mensch?“. '
           'Lassen Sie mich mit einer Zahl beginnen: Vor hundertfünfzig Jahren arbeitete ein Fabrikarbeiter in Deutschland durchschnittlich über siebzig Stunden pro Woche. Heute sind es weniger als vierzig. '
           'Man könnte also annehmen, dass wir so viel freie Zeit haben wie nie zuvor. Dennoch klagen in Umfragen zwei von drei Beschäftigten über Zeitmangel. Wie lässt sich das erklären?\n'
           'F|Der erste Grund ist, dass die Grenze zwischen Arbeit und Freizeit verschwimmt. Wer abends noch dienstliche Nachrichten liest, hat zwar offiziell frei, kann aber nicht abschalten. '
           'Der zweite Grund betrifft die Freizeit selbst: Sie ist zu einer Aufgabe geworden. Sport, Weiterbildung, soziale Netzwerke: Auch in der freien Zeit haben viele das Gefühl, etwas leisten zu müssen.\n'
           'F|Einige Unternehmen haben darauf reagiert. In einem Versuch mit sechzig Firmen wurde die Arbeitszeit bei gleichem Gehalt auf vier Tage verkürzt. Das Ergebnis hat selbst die Forscher überrascht: Die Leistung blieb gleich, die Zahl der Krankheitstage sank um ein Drittel. '
           'Allerdings, und das muss man betonen, lässt sich dieses Modell nicht auf alle Berufe übertragen. In der Pflege oder im Handwerk kann man die Arbeit nicht einfach schneller erledigen.\n'
           'F|Mein Fazit lautet deshalb: Entscheidend ist nicht nur, wie lange wir arbeiten, sondern ob wir über unsere Zeit selbst bestimmen können. Wer seine Arbeitszeit mitgestalten darf, ist nachweislich zufriedener, und zwar unabhängig von der Zahl der Stunden. Vielen Dank für Ihre Aufmerksamkeit.')
H4 = PART('h-vortrag', 'listening', 'Hören — Teil 4', 'Un exposé', 'Sie hören einen Vortrag. Wählen Sie die richtige Lösung.', 8, [
  LQ(VORTRAG, ['Deutlich mehr als heute.', 'Ungefähr so viel wie heute.', 'Weniger als heute.'], 'Wie lange arbeitete man vor hundertfünfzig Jahren?'),
  LQ(VORTRAG, ['Sie haben das Gefühl, zu wenig Zeit zu haben.', 'Sie möchten mehr arbeiten.', 'Sie sind mit ihrer Freizeit zufrieden.'], 'Was sagen zwei Drittel der Beschäftigten in Umfragen?'),
  LQ(VORTRAG, ['Arbeit und Freizeit lassen sich schlechter trennen.', 'Die Wege zur Arbeit sind länger geworden.', 'Die Arbeit ist körperlich schwerer geworden.'], 'Was nennt die Rednerin als ersten Grund?'),
  LQ(VORTRAG, ['Man fühlt sich auch dort unter Leistungsdruck.', 'Sie ist zu teuer geworden.', 'Man verbringt sie meistens allein.'], 'Was sagt sie über die Freizeit?'),
  LQ(VORTRAG, ['Die Angestellten waren seltener krank.', 'Die Leistung ging deutlich zurück.', 'Die Gehälter wurden gekürzt.'], 'Was war ein Ergebnis des Versuchs mit der Vier-Tage-Woche?'),
  LQ(VORTRAG, ['Die Forscher hatten es nicht erwartet.', 'Es entsprach genau den Erwartungen.', 'Es wurde nie veröffentlicht.'], 'Wie wurde das Ergebnis aufgenommen?'),
  LQ(VORTRAG, ['Es eignet sich nicht für jeden Beruf.', 'Es funktioniert überall gleich gut.', 'Es ist vor allem für die Pflege gedacht.'], 'Welche Einschränkung nennt die Rednerin?'),
  LQ(VORTRAG, ['Dass man über die eigene Zeit mitbestimmen kann.', 'Dass alle möglichst wenig arbeiten.', 'Dass die Freizeit besser geplant wird.'], 'Was ist laut dem Fazit am wichtigsten?'),
], listening=True)

# ═════════════════════════ Lesen ═════════════════════════
FORUM = ('FORUM: Brauchen wir noch Bargeld?\n\n'
         'A — Marlene: Ich zahle fast nur noch mit dem Handy. Es geht schneller, und ich muss nie überlegen, ob ich genug Geld dabeihabe. Angst vor Überwachung habe ich nicht: Wer nichts zu verbergen hat, braucht sich keine Sorgen zu machen. Bargeld ist außerdem teuer, denn es muss gedruckt, transportiert und bewacht werden.\n\n'
         'B — Gerd: Für mich bedeutet Bargeld Freiheit. Niemand weiß, was ich kaufe, und kein Stromausfall kann mich am Bezahlen hindern. Außerdem habe ich mit Scheinen in der Hand einen besseren Überblick über meine Ausgaben. Mit der Karte gibt man, das ist bewiesen, leichter zu viel aus.\n\n'
         'C — Aylin: Als Besitzerin eines kleinen Cafés sehe ich beide Seiten. Kartenzahlung kostet mich Gebühren, die sich bei einem Kaffee für drei Euro kaum lohnen. Andererseits muss ich abends kein Geld mehr zur Bank bringen, was sicherer ist. Ich biete deshalb beides an und lasse die Gäste entscheiden.\n\n'
         'D — Friedrich: Man vergisst oft die Menschen, die mit der Technik nicht zurechtkommen. Meine Mutter ist 84 und hat kein Smartphone. Sollte das Bargeld abgeschafft werden, wäre sie auf fremde Hilfe angewiesen. Eine Gesellschaft darf niemanden ausschließen, nur weil es bequemer ist.\n')
def FO(aussage, letter):
    names = {'A': 'Marlene', 'B': 'Gerd', 'C': 'Aylin', 'D': 'Friedrich'}
    return RP(FORUM, aussage, [names[letter]] + [n for k, n in names.items() if k != letter])
L1 = PART('l-forum', 'reading', 'Lesen — Teil 1', 'Un forum : qui exprime cette idée ?', 'Lesen Sie die Beiträge. Wer äußert diese Meinung?', 9, [
  FO('Bargeld schützt die Privatsphäre.', 'B'),
  FO('Ältere Menschen könnten benachteiligt werden.', 'D'),
  FO('Für kleine Beträge ist die Kartenzahlung für Geschäfte ungünstig.', 'C'),
  FO('Die Herstellung und Sicherung von Bargeld verursacht Kosten.', 'A'),
  FO('Mit Bargeld behält man seine Ausgaben besser im Blick.', 'B'),
  FO('Die Kunden sollen selbst wählen können.', 'C'),
  FO('Die Sorge um die eigenen Daten ist übertrieben.', 'A'),
  FO('Bequemlichkeit ist kein ausreichendes Argument.', 'D'),
  FO('Weniger Bargeld in der Kasse bedeutet weniger Risiko.', 'C'),
])

ART1 = ('DIE RÜCKKEHR DER REPARATUR\n'
        'Noch vor wenigen Jahren galt es als selbstverständlich, ein defektes Gerät durch ein neues zu ersetzen. Eine Reparatur war oft teurer als der Neukauf, sofern sie überhaupt möglich war: Viele Hersteller verklebten ihre Geräte so, dass sie sich nicht öffnen ließen, oder lieferten keine Ersatzteile. '
        'Inzwischen zeichnet sich ein Wandel ab. In mehr als tausend deutschen Städten gibt es sogenannte Reparaturcafés, in denen Ehrenamtliche gemeinsam mit den Besitzern Toaster, Lampen oder Fahrräder wieder in Gang bringen. Bezahlt wird nichts, höchstens eine Spende für Kaffee und Kuchen. '
        'Den Organisatoren zufolge geht es dabei nicht nur um Müllvermeidung. „Wer einmal selbst etwas repariert hat, betrachtet seine Dinge anders“, sagt die Gründerin eines Cafés in Jena. Man verliere die Angst vor der Technik und kaufe bewusster ein. '
        'Auch die Politik hat reagiert: Seit Kurzem sind Hersteller bestimmter Geräte verpflichtet, Ersatzteile mindestens sieben Jahre lang anzubieten. Kritikern geht das nicht weit genug. Sie bemängeln, dass die Teile häufig so teuer seien, dass sich die Reparatur weiterhin kaum lohne, und fordern deshalb eine niedrigere Steuer auf Reparaturen.')
L2 = PART('l-artikel', 'reading', 'Lesen — Teil 2', 'Un article de magazine', 'Lesen Sie den Artikel und wählen Sie die richtige Lösung.', 6, [
  RP(ART1, 'Früher wurden defekte Geräte selten repariert, weil …', ['es sich finanziell nicht lohnte oder gar nicht ging.', 'niemand wusste, wie man sie repariert.', 'die Hersteller es verboten hatten.']),
  RP(ART1, 'Manche Hersteller …', ['bauten ihre Geräte so, dass man sie nicht öffnen konnte.', 'reparierten ihre Geräte kostenlos.', 'eröffneten eigene Reparaturcafés.']),
  RP(ART1, 'In den Reparaturcafés …', ['helfen Freiwillige den Besitzern bei der Reparatur.', 'arbeiten ausgebildete Techniker gegen Bezahlung.', 'kann man gebrauchte Geräte kaufen.']),
  RP(ART1, 'Nach Ansicht der Gründerin aus Jena …', ['verändert das Reparieren die Einstellung zu den eigenen Sachen.', 'sollte man Technik lieber Fachleuten überlassen.', 'ist Müllvermeidung das einzige Ziel.']),
  RP(ART1, 'Das neue Gesetz verpflichtet die Hersteller, …', ['Ersatzteile über mehrere Jahre zu liefern.', 'defekte Geräte zurückzunehmen.', 'die Preise für Ersatzteile zu senken.']),
  RP(ART1, 'Die Kritiker verlangen, dass …', ['Reparaturen steuerlich günstiger werden.', 'das Gesetz wieder abgeschafft wird.', 'die Reparaturcafés Geld vom Staat bekommen.']),
])

ART2 = ('ALLEIN UNTER VIELEN\n'
        'Nie zuvor war es so einfach, mit anderen in Kontakt zu treten, und doch geben in einer aktuellen Umfrage vier von zehn jungen Erwachsenen an, sich häufig einsam zu fühlen. Damit sind sie stärker betroffen als die Generation ihrer Großeltern, was viele überraschen dürfte. '
        'Die Psychologin Vera Hansen warnt allerdings davor, die Schuld allein bei den sozialen Netzwerken zu suchen. Zwar verbrächten junge Leute viel Zeit am Bildschirm, entscheidend sei jedoch, wie sie diese Zeit nutzten. Wer online Verabredungen treffe oder mit entfernten Freunden schreibe, fühle sich sogar weniger allein. Problematisch werde es erst, wenn man nur noch das scheinbar perfekte Leben anderer betrachte. '
        'Als eigentliche Ursache nennt Hansen die wachsende Mobilität. Für Ausbildung und Beruf zögen junge Menschen heute mehrmals um und müssten ihr soziales Umfeld jedes Mal neu aufbauen. Hinzu komme, dass Orte der zufälligen Begegnung verschwänden: Vereine verlören Mitglieder, und wer im Homeoffice arbeite, lerne keine Kollegen kennen. '
        'Einsamkeit sei, so die Forscherin, keine Krankheit, könne aber krank machen, wenn sie andauere. Sie rät Betroffenen, nicht auf den einen besten Freund zu warten, sondern regelmäßige, auch oberflächliche Kontakte zu pflegen: den Gruß im Treppenhaus, das Gespräch im Sportkurs. Aus solchen Begegnungen entstehe mit der Zeit Vertrauen.')
L3 = PART('l-zeitung', 'reading', 'Lesen — Teil 3', 'Un article de presse', 'Lesen Sie den Zeitungsartikel und wählen Sie die richtige Lösung.', 6, [
  RP(ART2, 'Die Umfrage zeigt, dass …', ['junge Erwachsene sich öfter einsam fühlen als alte Menschen.', 'die Großeltern am einsamsten sind.', 'Einsamkeit insgesamt abnimmt.']),
  RP(ART2, 'Frau Hansen meint, dass soziale Netzwerke …', ['je nach Nutzung helfen oder schaden können.', 'die Hauptursache der Einsamkeit sind.', 'von jungen Leuten kaum genutzt werden.']),
  RP(ART2, 'Schädlich ist es laut Hansen, …', ['nur das Leben anderer zu beobachten.', 'online Treffen zu vereinbaren.', 'mit Freunden in der Ferne zu schreiben.']),
  RP(ART2, 'Den wichtigsten Grund sieht die Psychologin darin, dass …', ['junge Menschen häufig den Wohnort wechseln.', 'junge Menschen zu viel arbeiten.', 'Familien kleiner geworden sind.']),
  RP(ART2, 'Über das Homeoffice sagt der Text, dass …', ['man dort kaum neue Leute trifft.', 'es die Einsamkeit verringert.', 'es vor allem ältere Menschen betrifft.']),
  RP(ART2, 'Hansen empfiehlt, …', ['auch kleine alltägliche Kontakte zu pflegen.', 'sich auf einen engen Freund zu konzentrieren.', 'sofort einen Arzt aufzusuchen.']),
])

THEMA = 'LESERBRIEFE: Sollten Hausaufgaben abgeschafft werden?\n\n'
def MEIN(name, text, dafuer):
    return RP(THEMA + f'{name}: {text}', f'Ist {name} für die Abschaffung der Hausaufgaben?', ['Ja', 'Nein'] if dafuer else ['Nein', 'Ja'])
L4 = PART('l-meinungen', 'reading', 'Lesen — Teil 4', 'Courrier des lecteurs : pour ou contre ?', 'Lesen Sie die Texte. Ist die Person für die Abschaffung der Hausaufgaben?', 6, [
  MEIN('Sabine', 'Als Mutter von drei Kindern erlebe ich jeden Nachmittag denselben Streit. Was in der Schule nicht verstanden wurde, soll ich zu Hause erklären, obwohl ich dafür nicht ausgebildet bin. Üben gehört in die Schule, und zwar unter Anleitung von Fachleuten.', True),
  MEIN('Herr Albrecht', 'Ich unterrichte seit dreißig Jahren Mathematik. Wer glaubt, man könne Rechnen lernen, ohne regelmäßig allein zu üben, der irrt. In fünfundvierzig Minuten Unterricht ist dafür schlicht keine Zeit. Auf Hausaufgaben zu verzichten, hieße, auf Lernerfolg zu verzichten.', False),
  MEIN('Deniz', 'Bei uns zu Hause gab es keinen ruhigen Platz zum Arbeiten und niemanden, der helfen konnte. Meine Mitschüler mit studierten Eltern hatten es leichter. Hausaufgaben vergrößern also die Unterschiede, die die Schule eigentlich ausgleichen sollte. Weg damit!', True),
  MEIN('Kathrin', 'Natürlich sind Hausaufgaben lästig. Aber Kinder lernen dabei etwas, das kein Unterricht vermitteln kann: sich selbst zu organisieren und eine Aufgabe auch dann zu Ende zu bringen, wenn niemand danebensteht. Das wird später im Beruf von ihnen erwartet.', False),
  MEIN('Professor Lange', 'Die Forschung ist eindeutig: In der Grundschule lässt sich kaum ein Zusammenhang zwischen Hausaufgaben und Leistung nachweisen. Statt an einer Tradition festzuhalten, sollten wir die Zeit für Bewegung, Musik und Spiel nutzen und das Üben in den Schultag einbauen.', True),
  MEIN('Jonas', 'Ich bin sechzehn und fände es zwar bequem, nachmittags frei zu haben. Ehrlich gesagt würde ich dann aber vor Prüfungen nichts mehr können. Die Aufgaben zwingen mich, den Stoff zu wiederholen. Weniger wäre gut, gar keine wäre ein Fehler.', False),
])

REGELN = ('NUTZUNGSORDNUNG — Herzogin-Bibliothek Weimar\n'
          '§ 1 Anmeldung: Die Nutzung des Lesesaals ist kostenlos. Für die Ausleihe ist ein Bibliotheksausweis erforderlich, der gegen Vorlage eines gültigen Ausweises ausgestellt wird. Studierende erhalten ihn gebührenfrei, alle anderen zahlen zwanzig Euro pro Jahr.\n'
          '§ 2 Ausleihe: Bücher können vier Wochen ausgeliehen werden. Die Frist lässt sich zweimal online verlängern, sofern das Buch nicht von einer anderen Person vorbestellt wurde. Werke, die vor 1900 erschienen sind, dürfen ausschließlich im Lesesaal eingesehen werden.\n'
          '§ 3 Verhalten: Im Lesesaal ist Ruhe zu halten. Mobiltelefone sind stumm zu schalten. Getränke in verschließbaren Flaschen sind gestattet, Speisen dagegen nicht. Taschen und Mäntel sind in den Schließfächern im Erdgeschoss aufzubewahren.\n'
          '§ 4 Haftung: Bei Verlust oder Beschädigung eines Buches hat die Nutzerin oder der Nutzer den Wiederbeschaffungswert zu ersetzen. Für überschrittene Fristen wird eine Gebühr von fünfzig Cent pro Tag und Buch erhoben.')
L5 = PART('l-ordnung', 'reading', 'Lesen — Teil 5', 'Un règlement', 'Lesen Sie die Nutzungsordnung und wählen Sie die richtige Lösung.', 3, [
  RP(REGELN, 'Den Bibliotheksausweis …', ['bekommen Studierende umsonst.', 'braucht man schon für den Lesesaal.', 'muss jeder bezahlen.']),
  RP(REGELN, 'Die Leihfrist kann man nicht verlängern, wenn …', ['jemand anderes das Buch reserviert hat.', 'man sie schon einmal verlängert hat.', 'das Buch nach 1900 erschienen ist.']),
  RP(REGELN, 'Im Lesesaal darf man …', ['aus einer verschließbaren Flasche trinken.', 'leise telefonieren.', 'seine Tasche mitnehmen.']),
])

# ═════════════════════════ Schreiben ═════════════════════════
S1 = PART('s-forum', 'writing', 'Schreiben — Teil 1', 'Une contribution argumentée sur un forum', 'Lesen Sie die Situation und wählen Sie den besten Text.', 3, [
  RQ(['Meiner Ansicht nach sollte das Tempolimit auf Autobahnen eingeführt werden. Dafür spricht vor allem, dass bei niedrigerer Geschwindigkeit weniger schwere Unfälle passieren. Hinzu kommt, dass der Verbrauch und damit die Belastung für die Umwelt sinken würden. Zwar verliert man auf langen Strecken etwas Zeit, aber dieser Nachteil wiegt meines Erachtens weniger schwer als der Gewinn an Sicherheit.',
      'Meiner Ansicht nach das Tempolimit sollte eingeführt werden. Dafür spricht, dass passieren weniger Unfälle. Hinzu kommt, der Verbrauch würde sinken. Zwar man verliert Zeit, aber dieser Nachteil wiegt weniger schwer als der Gewinn von Sicherheit.',
      'Tempolimit ist gut. Ich fahre gern schnell. Autos sind laut. Was denkt ihr?',
      'Ich bin für ein Tempolimit, weil dadurch mehr Unfälle passieren. Deshalb würde der Verbrauch steigen, obwohl man Zeit verliert. Folglich bin ich dagegen.'],
     '★ Situation: In einem Forum wird über ein Tempolimit auf Autobahnen diskutiert. Äußern Sie Ihre Meinung, nennen Sie Gründe und gehen Sie auf ein Gegenargument ein.'),
  RQ(['Zusammenfassend lässt sich sagen, dass sowohl ökologische als auch gesundheitliche Gründe dafür sprechen, weniger Fleisch zu essen.',
      'Zusammenfassend lässt sich sagen, dass sowohl ökologische noch gesundheitliche Gründe sprechen dafür, weniger Fleisch zu essen.',
      'Zusammenfassend ich sage, dass ökologische als auch gesundheitliche Gründe dafür sprechen, weniger Fleisch essen.',
      'Zusammenfassend lässt es sagen, dass weder ökologische als auch gesundheitliche Gründe dafür spricht.'],
     '★ Sie möchten Ihren Forumsbeitrag über Fleischkonsum mit einem Schlusssatz beenden. Welcher Satz ist korrekt?'),
  RQ(['Das mag in Einzelfällen zutreffen, allerdings zeigen Studien, dass die meisten Beschäftigten zu Hause genauso produktiv sind.',
      'Das stimmt nicht, du hast keine Ahnung. Alle arbeiten zu Hause viel.',
      'Das mag in Einzelfällen zutreffen, allerdings Studien zeigen, dass die meisten Beschäftigten sind zu Hause genauso produktiv.',
      'Das mag zutreffen, folglich arbeiten die meisten zu Hause weniger, wie du sagst, und ich widerspreche dir.'],
     '★ Ein Nutzer schreibt: „Im Homeoffice arbeitet doch niemand richtig.“ Sie möchten sachlich widersprechen. Welche Antwort passt?'),
])
S2 = PART('s-formell', 'writing', 'Schreiben — Teil 2', 'Un message formel', 'Lesen Sie die Situation und wählen Sie die passende Formulierung.', 2, [
  RQ(['Sehr geehrte Frau Dr. Winter, aufgrund eines Arzttermins, der sich leider nicht verschieben lässt, kann ich am Donnerstag nicht an der Besprechung teilnehmen. Ich wäre Ihnen dankbar, wenn Sie mir das Protokoll zukommen lassen könnten. Selbstverständlich stehe ich am Freitag für Rückfragen zur Verfügung. Mit freundlichen Grüßen, Tomás Vidal',
      'Hallo Frau Winter, am Donnerstag kann ich nicht, ich muss zum Arzt. Schick mir bitte das Protokoll. Bis Freitag! Tomás',
      'Sehr geehrte Frau Dr. Winter, aufgrund einen Arzttermin, der sich leider nicht verschieben lasst, ich kann am Donnerstag nicht an die Besprechung teilnehmen. Ich wäre Ihnen dankbar, wenn Sie könnten mir das Protokoll zukommen lassen.',
      'Sehr geehrte Frau Dr. Winter, ich werde am Donnerstag an der Besprechung teilnehmen, obwohl ich keinen Termin habe. Bitte schicken Sie mir deshalb kein Protokoll. Mit freundlichen Grüßen, Tomás Vidal'],
     '★ Situation: Sie können an einer Besprechung mit Ihrer Vorgesetzten, Frau Dr. Winter, nicht teilnehmen. Entschuldigen Sie sich, nennen Sie den Grund und bitten Sie um das Protokoll.'),
  RQ(['Ich wäre Ihnen sehr verbunden, wenn Sie mir bis Ende der Woche Bescheid geben könnten.',
      'Sagen Sie mir Bescheid bis Ende der Woche, okay?',
      'Ich wäre Ihnen sehr verbunden, wenn Sie könnten mir bis Ende der Woche Bescheid geben.',
      'Ich bin dir sehr verbunden, wenn Sie mir bis Ende der Woche Bescheid gibst.'],
     '★ Sie bitten in einer formellen E-Mail höflich um eine schnelle Antwort. Welcher Satz ist angemessen und korrekt?'),
])

write_bank('GOETHEB2', [H1, H2, H3, H4, L1, L2, L3, L4, L5, S1, S2], (30, 30, 5),
  'Questions rédigées par Koto Quest au format de l’examen officiel Goethe-Zertifikat B2 (Goethe-Institut : types d’épreuves, consignes en allemand, modules notés sur 100 et validés séparément à 60 points). L’épreuve Schreiben se fait par choix multiple et l’épreuve orale (Sprechen) n’est pas évaluée. Ce ne sont pas des questions officielles.',
  'Questions written by Koto Quest in the format of the official Goethe-Zertifikat B2 exam (Goethe-Institut: question types, instructions in German, modules marked out of 100 and passed separately at 60 points). The Schreiben test is multiple choice and the speaking test (Sprechen) is not assessed. They are not official questions.',
  {'Textes courts : vrai ou faux, puis une question': 'Short texts: true or false, then a question', 'Une interview à la radio': 'A radio interview', 'Une table ronde : qui dit quoi ?': 'A round table: who says what?',
   'Un exposé': 'A talk', 'Un forum : qui exprime cette idée ?': 'A forum: who expresses this idea?', 'Un article de magazine': 'A magazine article', 'Un article de presse': 'A press article',
   'Courrier des lecteurs : pour ou contre ?': 'Readers’ letters: for or against?', 'Un règlement': 'House rules',
   'Une contribution argumentée sur un forum': 'A reasoned forum post', 'Un message formel': 'A formal message'})
