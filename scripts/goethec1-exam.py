# Banque de questions de l'examen blanc Goethe-Zertifikat C1 (content/exams/goethec1.json), au format de l'épreuve
# modulaire du Goethe-Institut : Hören (30 questions en 4 parties : podcast, interview, discussion, exposé), Lesen (30 questions
# en 4 parties) et Schreiben (ici en format à choix : contribution à un forum, message formel). L'épreuve orale (Sprechen) n'est pas évaluée.
# 180 minutes ; chaque module est noté sur 100 et se valide séparément à partir de 60 points.
# Usage : python3 scripts/goethec1-exam.py
from goethe_exam import *

# ═════════════════════════ Hören ═════════════════════════
PODCAST = ('F|Willkommen bei „Kopfsache“, dem Podcast über Psychologie im Alltag. Heute geht es um das Aufschieben, in der Fachsprache Prokrastination genannt. Mein Gast ist der Psychologe Dr. Henrik Voss. Herr Voss, schieben nur faule Menschen ihre Aufgaben auf?\n'
           'M|Keineswegs, und genau das ist das größte Missverständnis. Wer aufschiebt, tut ja nicht nichts: Er putzt die Wohnung, beantwortet E-Mails oder sortiert seine Bücher. Mit Faulheit hat das wenig zu tun, sondern mit dem Umgang mit unangenehmen Gefühlen.\n'
           'F|Das müssen Sie erklären.\n'
           'M|Eine Aufgabe, die uns überfordert oder langweilt, löst Unbehagen aus. Indem wir uns einer anderen Tätigkeit zuwenden, verschwindet dieses Gefühl, allerdings nur kurzfristig. Das Gehirn lernt: Ausweichen wird belohnt. So entsteht eine Gewohnheit, die sich mit jedem Mal verfestigt.\n'
           'F|Betrifft das alle Menschen gleichermaßen?\n'
           'M|Gelegentliches Aufschieben kennt fast jeder. Problematisch wird es bei etwa einem Fünftel der Erwachsenen, bei denen das Verhalten chronisch ist. Besonders gefährdet sind Menschen mit hohen Ansprüchen an sich selbst. Wer fürchtet, eine Arbeit nicht perfekt zu erledigen, fängt lieber gar nicht erst an.\n'
           'F|Viele behaupten ja, sie bräuchten den Druck der letzten Minute, um gute Ideen zu haben.\n'
           'M|Das hört man oft, es lässt sich aber nicht belegen. In Studien schnitten diejenigen, die unter Zeitdruck arbeiteten, im Schnitt schlechter ab, hielten ihre Leistung jedoch für besser. Es handelt sich also eher um eine nachträgliche Rechtfertigung.\n'
           'F|Was raten Sie Betroffenen?\n'
           'M|Erstens: die Aufgabe so weit zu zerlegen, dass der erste Schritt lächerlich klein wirkt, etwa: das Dokument öffnen und einen Satz schreiben. Zweitens: sich nicht zu beschimpfen. Es klingt paradox, aber wer sich das Aufschieben verzeiht, schiebt beim nächsten Mal nachweislich weniger auf. Strenge gegen sich selbst verstärkt nämlich genau die unangenehmen Gefühle, vor denen man flieht.\n'
           'F|Und wenn all das nicht hilft?\n'
           'M|Dann sollte man sich nicht scheuen, professionelle Hilfe in Anspruch zu nehmen. Viele Hochschulen bieten inzwischen eigene Beratungsstellen an.')
H1 = PART('h-podcast', 'listening', 'Hören — Teil 1', 'Un podcast', 'Sie hören einen Podcast. Wählen Sie die richtige Lösung.', 7, [
  LQ(PODCAST, ['Aufschieben hat mit Faulheit wenig zu tun.', 'Nur faule Menschen schieben Aufgaben auf.', 'Wer aufschiebt, tut in dieser Zeit gar nichts.'], 'Was ist laut Dr. Voss ein Missverständnis?'),
  LQ(PODCAST, ['Weil das unangenehme Gefühl dadurch kurzfristig verschwindet.', 'Weil andere Tätigkeiten wichtiger sind.', 'Weil das Gehirn Abwechslung braucht.'], 'Warum weichen Menschen einer unangenehmen Aufgabe aus?'),
  LQ(PODCAST, ['Bei rund einem Fünftel der Erwachsenen.', 'Bei fast allen Erwachsenen.', 'Nur bei Studierenden.'], 'Bei wie vielen ist das Aufschieben chronisch?'),
  LQ(PODCAST, ['Menschen mit sehr hohen Ansprüchen an sich selbst.', 'Menschen, denen ihre Arbeit gleichgültig ist.', 'Menschen mit wenig Freizeit.'], 'Wer ist besonders gefährdet?'),
  LQ(PODCAST, ['Die Betroffenen überschätzen ihre Leistung unter Zeitdruck.', 'Unter Zeitdruck entstehen nachweislich die besten Ideen.', 'Zeitdruck hat keinen Einfluss auf die Leistung.'], 'Was zeigen Studien über das Arbeiten in letzter Minute?'),
  LQ(PODCAST, ['Den ersten Schritt möglichst klein zu machen.', 'Mit dem schwierigsten Teil zu beginnen.', 'Sich feste Strafen zu überlegen.'], 'Was empfiehlt Dr. Voss als Erstes?'),
  LQ(PODCAST, ['Wer nachsichtig mit sich ist, schiebt später weniger auf.', 'Strenge gegen sich selbst hilft am meisten.', 'Verzeihen führt dazu, dass man noch mehr aufschiebt.'], 'Was sagt er über den Umgang mit sich selbst?'),
], listening=True)

INTERVIEW = ('M|Wissenschaft im Gespräch. Unser Gast ist heute die Stadtforscherin Professorin Leyla Aksoy, die seit Jahren untersucht, wie Städte auf die Hitze reagieren. Frau Aksoy, warum ist es in Städten so viel heißer als auf dem Land?\n'
             'F|Das liegt vor allem an den versiegelten Flächen. Asphalt und Beton speichern tagsüber die Wärme und geben sie nachts wieder ab. Hinzu kommt, dass dichte Bebauung den Wind bremst. In manchen Innenstädten messen wir nachts bis zu zehn Grad mehr als im Umland.\n'
             'M|Was bedeutet das für die Bewohner?\n'
             'F|Gesundheitlich ist nicht der heiße Tag das Hauptproblem, sondern die Nacht, in der sich der Körper nicht erholen kann. Betroffen sind keineswegs nur ältere Menschen, wenngleich diese am stärksten gefährdet sind. Auch die Konzentration und die Arbeitsleistung sinken messbar.\n'
             'M|Viele Städte setzen jetzt auf Klimaanlagen.\n'
             'F|Was ich für einen Irrweg halte. Klimaanlagen kühlen den Innenraum, indem sie die Wärme nach draußen leiten, sie heizen die Straße also zusätzlich auf. Außerdem verbrauchen sie genau dann viel Strom, wenn das Netz ohnehin belastet ist.\n'
             'M|Was wäre die Alternative?\n'
             'F|Bäume, Wasser und helle Oberflächen. Ein ausgewachsener Straßenbaum kühlt seine Umgebung so stark wie zehn Klimaanlagen, und zwar ohne Strom. Allerdings braucht ein neu gepflanzter Baum zwanzig Jahre, bis er diese Wirkung entfaltet. Wir hätten also längst anfangen müssen.\n'
             'M|Scheitert es am Geld?\n'
             'F|Weniger am Geld als am Platz. Jeder Baum konkurriert mit Parkplätzen, Leitungen und Radwegen. Solange die Politik nicht bereit ist, dem Auto Fläche zu nehmen, bleibt vieles Theorie. In Wien hat man gezeigt, dass es geht: Dort wurden ganze Straßenzüge umgebaut, zunächst gegen heftigen Widerstand der Geschäftsleute, die inzwischen zu den größten Befürwortern zählen.\n'
             'M|Und was kann der Einzelne tun?\n'
             'F|Begrünte Fassaden und Dächer bringen durchaus etwas. Entscheidend sind jedoch Vorgaben der Stadt, denn freiwillig geschieht erfahrungsgemäß zu wenig.')
H2 = PART('h-interview', 'listening', 'Hören — Teil 2', 'Une interview d’experte', 'Sie hören ein Interview. Wählen Sie die richtige Lösung.', 8, [
  LQ(INTERVIEW, ['Versiegelte Flächen speichern die Wärme.', 'In Städten scheint die Sonne länger.', 'Die vielen Menschen erzeugen die Wärme.'], 'Was ist der Hauptgrund für die Hitze in Städten?'),
  LQ(INTERVIEW, ['Sie verhindert, dass der Wind die Stadt kühlt.', 'Sie spendet zu wenig Schatten.', 'Sie hat keinen Einfluss auf die Temperatur.'], 'Welche Rolle spielt die dichte Bebauung?'),
  LQ(INTERVIEW, ['Die Nächte, in denen man sich nicht erholen kann.', 'Die Mittagsstunden.', 'Die plötzlichen Temperaturwechsel.'], 'Was belastet die Gesundheit am meisten?'),
  LQ(INTERVIEW, ['Sie sind am stärksten, aber nicht als Einzige betroffen.', 'Nur sie sind von der Hitze betroffen.', 'Sie vertragen die Hitze besser als Jüngere.'], 'Was sagt Frau Aksoy über ältere Menschen?'),
  LQ(INTERVIEW, ['Sie erwärmen die Straßen zusätzlich.', 'Sie sind die wirksamste Lösung.', 'Sie verbrauchen kaum Strom.'], 'Warum lehnt sie Klimaanlagen ab?'),
  LQ(INTERVIEW, ['Sie wirken erst nach vielen Jahren.', 'Sie brauchen zu viel Wasser.', 'Sie kühlen weniger als erwartet.'], 'Welchen Nachteil haben neu gepflanzte Bäume?'),
  LQ(INTERVIEW, ['Der fehlende Platz.', 'Die hohen Kosten.', 'Der Widerstand der Radfahrer.'], 'Woran scheitert die Begrünung vor allem?'),
  LQ(INTERVIEW, ['Sie waren zuerst dagegen und sind jetzt dafür.', 'Sie waren von Anfang an begeistert.', 'Sie haben ihre Geschäfte geschlossen.'], 'Wie haben die Wiener Geschäftsleute reagiert?'),
], listening=True)

DISKUSSION = ('N|Forum Bildung, die Diskussion. Soll an den Universitäten künftig mehr auf Englisch gelehrt werden? Darüber streiten heute die Sprachwissenschaftlerin Professorin Ines Brandt und der Physiker Professor Tobias Reimann.\n'
              'M|Für mich ist die Sache klar. Die Sprache der Naturwissenschaften ist Englisch. Wer seine Ergebnisse auf Deutsch veröffentlicht, wird international schlicht nicht wahrgenommen. Demzufolge müssen unsere Studierenden so früh wie möglich lernen, auf Englisch zu denken und zu schreiben.\n'
              'F|Dass man auf Englisch veröffentlicht, bestreite ich gar nicht. Etwas anderes ist jedoch die Lehre. Untersuchungen zeigen, dass Studierende in einer Fremdsprache weniger nachfragen und komplexe Zusammenhänge oberflächlicher verarbeiten.\n'
              'M|Das mag am Anfang zutreffen. Nach zwei Semestern haben sich die meisten daran gewöhnt. Und denken Sie an die ausländischen Studierenden: Ohne englische Studiengänge kämen viele gar nicht erst zu uns.\n'
              'F|Sie kommen, das stimmt. Aber sie bleiben nicht. Wer während des gesamten Studiums kein Deutsch braucht, findet später hier kaum eine Stelle und geht wieder. Das kann nicht im Interesse des Landes sein, das diese Ausbildung bezahlt.\n'
              'M|Dann sollte man eben zusätzlich Deutschkurse verlangen. Das eine schließt das andere nicht aus.\n'
              'F|Einverstanden, sofern diese Kurse verpflichtend sind und nicht bloß angeboten werden. Mir geht es noch um etwas anderes: Eine Sprache, in der nicht mehr geforscht wird, verliert ihre Fachbegriffe. Irgendwann lässt sich über Physik auf Deutsch gar nicht mehr präzise sprechen, und damit auch nicht mehr mit der Öffentlichkeit.\n'
              'M|Das halte ich für übertrieben. Die Öffentlichkeit interessiert sich für Ergebnisse, nicht für Fachbegriffe. Allerdings räume ich ein, dass wir Forscher uns zu wenig darum bemühen, verständlich zu erklären, was wir tun.\n'
              'N|Zumindest in diesem Punkt scheint also Einigkeit zu bestehen. Herzlichen Dank an Sie beide.')
WER = ['Frau Brandt', 'Herr Reimann', 'Der Moderator']
def WHO3(first):
    return [first] + [w for w in WER if w != first]
H3 = PART('h-diskussion', 'listening', 'Hören — Teil 3', 'Une discussion : qui dit quoi ?', 'Sie hören eine Diskussion. Wer vertritt welche Position?', 7, [
  LQ(DISKUSSION, WHO3('Herr Reimann'), 'Wer nicht auf Englisch veröffentlicht, wird international übersehen.'),
  LQ(DISKUSSION, WHO3('Frau Brandt'), 'In einer Fremdsprache wird der Stoff weniger gründlich verarbeitet.'),
  LQ(DISKUSSION, WHO3('Herr Reimann'), 'Englische Studiengänge ziehen Studierende aus dem Ausland an.'),
  LQ(DISKUSSION, WHO3('Frau Brandt'), 'Ohne Deutschkenntnisse verlassen viele Absolventen das Land wieder.'),
  LQ(DISKUSSION, WHO3('Frau Brandt'), 'Deutschkurse müssten Pflicht sein.'),
  LQ(DISKUSSION, WHO3('Herr Reimann'), 'Forscher erklären ihre Arbeit nicht verständlich genug.'),
  LQ(DISKUSSION, WHO3('Der Moderator'), 'In einem Punkt sind sich beide einig.'),
], listening=True)

VORTRAG = ('F|Sehr geehrte Damen und Herren, das Thema meines Vortrags lautet: „Vergessen als Leistung des Gedächtnisses“. Das mag zunächst widersinnig klingen, gilt das Vergessen doch gemeinhin als Schwäche. Ich möchte Ihnen zeigen, dass es sich umgekehrt verhält.\n'
           'F|Lange nahm die Forschung an, Erinnerungen verblassten einfach mit der Zeit, so wie Tinte auf Papier. Heute wissen wir, dass das Gehirn aktiv vergisst. Bestimmte Zellen sind eigens dafür zuständig, Verbindungen zwischen Nervenzellen wieder abzubauen, und zwar vor allem im Schlaf.\n'
           'F|Wozu dieser Aufwand? Stellen Sie sich vor, Sie würden sich an jedes Gesicht in der Straßenbahn, an jedes Mittagessen der letzten zehn Jahre erinnern. Es gibt tatsächlich einige wenige Menschen mit einem solchen Gedächtnis. Sie berichten übereinstimmend, dass sie darunter leiden: Es fällt ihnen schwer, Wichtiges von Unwichtigem zu trennen und Entscheidungen zu treffen.\n'
           'F|Vergessen ermöglicht also erst das Verallgemeinern. Ein Kind, das zehn verschiedene Hunde gesehen hat, bildet den Begriff „Hund“ nur deshalb, weil es die Einzelheiten jedes einzelnen Tieres vergisst. Ohne Vergessen gäbe es kein Lernen im eigentlichen Sinn.\n'
           'F|Was folgt daraus für den Alltag? Zum einen, dass ständiges Wiederholen kurz vor einer Prüfung wenig bringt. Wirksamer ist es, den Stoff in wachsenden Abständen zu wiederholen, also gerade dann, wenn man ihn beinahe vergessen hat. Zum anderen sollten wir aufhören, digitale Speicher mit dem Gedächtnis zu verwechseln. Ein Archiv, das nichts aussortiert, ist kein Gedächtnis, sondern ein Lager.\n'
           'F|Lassen Sie mich mit einer Einschränkung schließen. All das gilt für das gesunde Vergessen. Krankhafter Gedächtnisverlust, wie er bei einer Demenz auftritt, folgt anderen Mechanismen und ist nicht Gegenstand dieses Vortrags. Ich danke Ihnen für Ihre Aufmerksamkeit.')
H4 = PART('h-vortrag', 'listening', 'Hören — Teil 4', 'Un exposé scientifique', 'Sie hören einen Vortrag. Wählen Sie die richtige Lösung.', 8, [
  LQ(VORTRAG, ['Vergessen ist eine Fähigkeit und keine Schwäche.', 'Vergessen lässt sich durch Training vermeiden.', 'Vergessen ist ein Zeichen von Krankheit.'], 'Welche These vertritt die Rednerin?'),
  LQ(VORTRAG, ['Dass Erinnerungen von selbst allmählich verblassen.', 'Dass das Gehirn nichts vergisst.', 'Dass man nur im Schlaf vergisst.'], 'Was nahm die Forschung früher an?'),
  LQ(VORTRAG, ['Das Gehirn baut Verbindungen gezielt ab.', 'Erinnerungen werden auf andere Zellen verteilt.', 'Das Gehirn speichert alles dauerhaft.'], 'Was weiß man heute?'),
  LQ(VORTRAG, ['Sie haben Mühe, Wichtiges zu erkennen und sich zu entscheiden.', 'Sie sind in Prüfungen besonders erfolgreich.', 'Sie fühlen sich glücklicher als andere.'], 'Was berichten Menschen, die fast nichts vergessen?'),
  LQ(VORTRAG, ['Weil es Einzelheiten vergisst und so verallgemeinern kann.', 'Weil es sich jeden einzelnen Hund genau merkt.', 'Weil die Eltern das Wort oft wiederholen.'], 'Warum kann ein Kind den Begriff „Hund“ bilden?'),
  LQ(VORTRAG, ['In immer größeren Abständen zu wiederholen.', 'Kurz vor der Prüfung möglichst oft zu wiederholen.', 'Den Stoff nur einmal gründlich zu lesen.'], 'Was empfiehlt die Rednerin für das Lernen?'),
  LQ(VORTRAG, ['Sie sortieren nichts aus und sind deshalb kein Gedächtnis.', 'Sie arbeiten genauso wie das menschliche Gedächtnis.', 'Sie machen das Gedächtnis überflüssig.'], 'Was sagt sie über digitale Speicher?'),
  LQ(VORTRAG, ['Der krankhafte Gedächtnisverlust.', 'Das Vergessen im Schlaf.', 'Das Lernen bei Kindern.'], 'Was behandelt der Vortrag ausdrücklich nicht?'),
], listening=True)

# ═════════════════════════ Lesen ═════════════════════════
ART1 = ('DIE ENTDECKUNG DER LANGSAMKEIT IM LESESAAL\n'
        'Wer heute einen wissenschaftlichen Aufsatz liest, tut dies in aller Regel am Bildschirm, und zwar selten von Anfang bis Ende. Man überfliegt die Zusammenfassung, springt zu den Ergebnissen, sucht nach einem Stichwort. Diese Art der Lektüre, von Forschern als „Scannen“ bezeichnet, ist keineswegs ein Zeichen von Oberflächlichkeit, sondern eine sinnvolle Anpassung an die schiere Menge der verfügbaren Texte. Problematisch wird sie erst, wenn sie zur einzigen Lesetechnik wird.\n'
        'Genau dies befürchtet die Leseforscherin Katharina Mühlberg. In einer Langzeitstudie mit Studierenden dreier Fächer stellte sie fest, dass die Fähigkeit, einem langen Gedankengang über mehrere Seiten zu folgen, innerhalb von zehn Jahren spürbar nachgelassen hat. Auffällig sei, dass die Betroffenen dies selbst kaum bemerkten: Sie schätzten ihr Textverständnis durchweg höher ein, als es die Tests ergaben.\n'
        'Als Ursache nennt Mühlberg weniger das Medium als die Lesesituation. Am Bildschirm konkurriere jeder Text mit Nachrichten, Hinweisen und offenen Fenstern. Die Aufmerksamkeit werde dadurch in kurze Abschnitte zerlegt, was sich mit der Zeit auch auf das Lesen gedruckter Bücher übertrage. Ein Versuch, bei dem dieselben Texte einmal auf Papier und einmal auf einem Lesegerät ohne Internetzugang vorgelegt wurden, ergab denn auch kaum Unterschiede.\n'
        'Einige Hochschulen ziehen daraus bereits Konsequenzen. An der Universität Graz wurden „stille Lesestunden“ eingeführt, in denen Seminargruppen gemeinsam, aber schweigend einen längeren Text lesen, ehe sie darüber diskutieren. Was zunächst belächelt wurde, stößt inzwischen auf rege Nachfrage. Kritiker wenden allerdings ein, damit würden lediglich Symptome behandelt; solange Prüfungen vor allem abfragbares Einzelwissen belohnten, fehle der Anreiz, sich auf lange Texte einzulassen.')
L1 = PART('l-fachartikel', 'reading', 'Lesen — Teil 1', 'Un article de vulgarisation', 'Lesen Sie den Artikel und wählen Sie die richtige Lösung.', 7, [
  RP(ART1, 'Das „Scannen“ von Texten ist laut dem Artikel …', ['grundsätzlich eine vernünftige Technik.', 'ein Zeichen mangelnder Bildung.', 'nur bei gedruckten Texten sinnvoll.']),
  RP(ART1, 'Bedenklich wird es, wenn …', ['man gar nicht mehr anders liest.', 'man zu viele Texte liest.', 'man Zusammenfassungen überspringt.']),
  RP(ART1, 'Die Studie von Frau Mühlberg zeigt, dass Studierende …', ['langen Argumentationen schlechter folgen können als früher.', 'heute insgesamt weniger lesen.', 'gedruckte Bücher ablehnen.']),
  RP(ART1, 'Die Studierenden selbst …', ['überschätzten ihr Textverständnis.', 'waren sich des Problems bewusst.', 'baten um zusätzliche Kurse.']),
  RP(ART1, 'Die Hauptursache sieht die Forscherin …', ['in den ständigen Ablenkungen beim Lesen am Bildschirm.', 'in der schlechteren Qualität digitaler Texte.', 'im Bildschirm als solchem.']),
  RP(ART1, 'Der Versuch mit dem Lesegerät ohne Internet ergab, dass …', ['Papier und Gerät etwa gleich gut abschnitten.', 'Papier deutlich überlegen war.', 'das Gerät zu besseren Ergebnissen führte.']),
  RP(ART1, 'Die Kritiker der „stillen Lesestunden“ meinen, dass …', ['das Prüfungssystem das eigentliche Problem sei.', 'gemeinsames Lesen Zeitverschwendung sei.', 'die Studierenden das Angebot nicht annähmen.']),
])

KOMM = ('KOMMENTAR: Die Vier-Tage-Woche ist kein Geschenk\n'
        'Kaum ein Vorschlag hat in den letzten Jahren so viel Zustimmung gefunden wie die Verkürzung der Arbeitswoche bei vollem Lohn. Die Ergebnisse der bisherigen Versuche scheinen den Befürwortern recht zu geben: zufriedenere Beschäftigte, weniger Krankmeldungen, gleichbleibende Leistung. Wer wollte da noch widersprechen?\n'
        'Ich möchte es dennoch tun, wenngleich nicht aus den Gründen, die üblicherweise vorgebracht werden. Dass die Wirtschaft zusammenbräche, halte ich für ebenso übertrieben wie die Verheißung, alle würden glücklicher. Mein Einwand betrifft die Frage, wer an den Versuchen überhaupt teilgenommen hat. Es waren nahezu ausschließlich Unternehmen, die sich freiwillig gemeldet hatten, überwiegend aus Beratung, Werbung und Softwareentwicklung, mithin aus Branchen, in denen sich Arbeit verdichten lässt, indem man Besprechungen streicht.\n'
        'Für die Pflegerin, den Busfahrer oder die Erzieherin gilt das nicht. Ihre Arbeit bemisst sich nach der Zeit, die sie anwesend sind. Wird ihre Woche verkürzt, muss jemand anderes die fehlenden Stunden übernehmen, und eben diese Fachkräfte fehlen schon heute. Eine allgemeine Vier-Tage-Woche liefe somit Gefahr, die Kluft zwischen jenen zu vertiefen, die ihre Zeit frei einteilen können, und jenen, die es nicht können.\n'
        'Hinzu kommt ein Zweites. In mehreren Firmen berichteten Beschäftigte nach einem Jahr, die gewonnene Freizeit werde durch die höhere Belastung an den verbleibenden Tagen aufgezehrt. Wer in vier Tagen dasselbe schaffen muss wie zuvor in fünf, hat am fünften keine freie Zeit gewonnen, sondern braucht ihn, um sich zu erholen.\n'
        'Nichts davon spricht dagegen, kürzere Arbeitszeiten zu erproben. Es spricht aber dagegen, aus den Erfahrungen einer privilegierten Minderheit ein Modell für alle abzuleiten. Sinnvoller wäre es, dort anzusetzen, wo die Belastung am größten ist, auch wenn es dort Geld kostet.')
L2 = PART('l-kommentar', 'reading', 'Lesen — Teil 2', 'Un commentaire de presse', 'Lesen Sie den Kommentar und wählen Sie die richtige Lösung.', 7, [
  RP(KOMM, 'Die bisherigen Versuche mit der Vier-Tage-Woche …', ['lieferten überwiegend positive Ergebnisse.', 'wurden vorzeitig abgebrochen.', 'führten zu sinkender Leistung.']),
  RP(KOMM, 'Die Warnung vor einem Zusammenbruch der Wirtschaft hält der Autor für …', ['überzogen.', 'berechtigt.', 'sein wichtigstes Argument.']),
  RP(KOMM, 'Sein zentraler Einwand lautet, dass …', ['die teilnehmenden Firmen nicht repräsentativ waren.', 'die Versuche zu kurz dauerten.', 'die Ergebnisse gefälscht wurden.']),
  RP(KOMM, 'In den beteiligten Branchen ließ sich Zeit sparen, indem …', ['man auf Besprechungen verzichtete.', 'man Personal entließ.', 'man die Löhne senkte.']),
  RP(KOMM, 'Bei Berufen wie Pflege oder Erziehung …', ['müssten zusätzliche Kräfte die Stunden auffangen.', 'wäre die Umstellung besonders einfach.', 'arbeiten die Beschäftigten bereits vier Tage.']),
  RP(KOMM, 'Einige Beschäftigte stellten nach einem Jahr fest, dass …', ['der freie Tag zum Ausruhen gebraucht wird.', 'sie den freien Tag für einen zweiten Job nutzen.', 'sie lieber wieder fünf Tage arbeiten wollten.']),
  RP(KOMM, 'Der Autor fordert am Ende, …', ['zuerst die am stärksten belasteten Berufe zu entlasten.', 'die Versuche ganz einzustellen.', 'die Vier-Tage-Woche sofort für alle einzuführen.']),
])

STIMMEN = ('UMFRAGE: Soll das Wahlalter auf 16 Jahre gesenkt werden?\n\n'
           'A — Dr. Miriam Seidel, Politologin: Die Forschung aus Österreich, wo seit 2007 ab sechzehn gewählt wird, ist ermutigend. Jugendliche, die zum ersten Mal wählen, solange sie noch zur Schule gehen und bei den Eltern wohnen, beteiligen sich häufiger als Achtzehnjährige, die gerade umgezogen sind. Und wer einmal gewählt hat, tut es meist wieder.\n\n'
           'B — Konrad Falk, Richter im Ruhestand: Mit sechzehn darf man weder einen Mietvertrag unterschreiben noch ohne Zustimmung der Eltern einen Kredit aufnehmen. Das Gesetz traut Jugendlichen in eigenen Angelegenheiten also keine volle Verantwortung zu. Es wäre widersprüchlich, ihnen zugleich die Mitentscheidung über die Angelegenheiten aller zu übertragen.\n\n'
           'C — Jana Petrow, Schülersprecherin, 17: Über Renten, Klima und Schulden wird heute entschieden, bezahlen werden wir. Dass man uns Reife abspricht, finde ich seltsam: Niemand prüft bei einem Achtzigjährigen, ob er die Programme gelesen hat. Entweder gilt der Maßstab für alle oder für niemanden.\n\n'
           'D — Prof. Uwe Hartung, Erziehungswissenschaftler: Ich bin weder dafür noch dagegen, solange die Voraussetzung fehlt. In vielen Bundesländern findet politische Bildung eine Stunde pro Woche statt, mancherorts erst ab Klasse zehn. Wer das Wahlalter senkt, ohne zuvor den Unterricht auszubauen, lädt Jugendliche zu einer Entscheidung ein, auf die die Schule sie nicht vorbereitet hat.\n')
def ST(aussage, letter):
    names = {'A': 'Dr. Seidel', 'B': 'Herr Falk', 'C': 'Jana Petrow', 'D': 'Prof. Hartung'}
    return RP(STIMMEN, aussage, [names[letter]] + [n for k, n in names.items() if k != letter])
L3 = PART('l-stimmen', 'reading', 'Lesen — Teil 3', 'Quatre points de vue : qui dit quoi ?', 'Lesen Sie die Stellungnahmen. Wer vertritt diese Position?', 8, [
  ST('Die rechtliche Stellung Jugendlicher spricht gegen das Wahlrecht.', 'B'),
  ST('Erfahrungen aus einem Nachbarland sprechen für die Senkung.', 'A'),
  ST('Zuerst muss die Schule besser auf das Wählen vorbereiten.', 'D'),
  ST('Die Jungen tragen die Folgen heutiger Entscheidungen.', 'C'),
  ST('Frühes Wählen führt zu einer dauerhaften Gewohnheit.', 'A'),
  ST('An Ältere werden keine vergleichbaren Anforderungen gestellt.', 'C'),
  ST('Es wäre unlogisch, in privaten Fragen weniger zuzutrauen als in öffentlichen.', 'B'),
  ST('Diese Person legt sich auf kein Ja oder Nein fest.', 'D'),
])

REGELN = ('PROMOTIONSORDNUNG (Auszug) — Philosophische Fakultät\n'
          '§ 4 Zulassung: Zur Promotion wird zugelassen, wer einen Masterabschluss oder einen gleichwertigen Abschluss mit mindestens der Note „gut“ nachweist. Über die Gleichwertigkeit ausländischer Abschlüsse entscheidet der Promotionsausschuss. Bewerberinnen und Bewerber, deren Abschluss in einem anderen Fach erworben wurde, können unter der Auflage zugelassen werden, binnen zweier Semester zusätzliche Leistungen zu erbringen.\n'
          '§ 7 Betreuung: Zwischen der Doktorandin oder dem Doktoranden und der betreuenden Person ist vor Beginn der Arbeit eine schriftliche Betreuungsvereinbarung abzuschließen. Diese regelt insbesondere die Häufigkeit der Beratungsgespräche. Ein Wechsel der Betreuung ist auf begründeten Antrag möglich.\n'
          '§ 9 Dissertation: Die Dissertation kann in deutscher oder englischer Sprache abgefasst werden; andere Sprachen bedürfen der Genehmigung des Ausschusses. Der Arbeit ist eine Erklärung beizufügen, dass sie selbstständig verfasst und alle benutzten Quellen angegeben wurden. Bereits veröffentlichte Teile sind als solche kenntlich zu machen.\n'
          '§ 12 Fristen: Die Dissertation ist spätestens sechs Jahre nach der Zulassung einzureichen. Auf Antrag kann die Frist aus wichtigem Grund, etwa wegen Krankheit oder Elternzeit, um höchstens zwei Jahre verlängert werden. Nach Ablauf der Frist erlischt die Zulassung.')
L4 = PART('l-ordnung', 'reading', 'Lesen — Teil 4', 'Un règlement universitaire', 'Lesen Sie den Auszug aus der Ordnung und wählen Sie die richtige Lösung.', 8, [
  RP(REGELN, 'Für die Zulassung braucht man …', ['einen Masterabschluss mit mindestens „gut“.', 'in jedem Fall einen deutschen Abschluss.', 'eine Empfehlung der betreuenden Person.']),
  RP(REGELN, 'Ob ein ausländischer Abschluss anerkannt wird, …', ['bestimmt der Promotionsausschuss.', 'bestimmt die betreuende Person.', 'ist gesetzlich festgelegt.']),
  RP(REGELN, 'Wer aus einem anderen Fach kommt, …', ['muss eventuell innerhalb eines Jahres Leistungen nachholen.', 'kann nicht zugelassen werden.', 'wird ohne Bedingungen zugelassen.']),
  RP(REGELN, 'Die Betreuungsvereinbarung …', ['muss vor Arbeitsbeginn schriftlich vorliegen.', 'wird erst bei Problemen geschlossen.', 'ist freiwillig.']),
  RP(REGELN, 'Die Betreuung zu wechseln, …', ['ist möglich, wenn man den Antrag begründet.', 'ist ausgeschlossen.', 'ist jederzeit ohne Angabe von Gründen möglich.']),
  RP(REGELN, 'Eine Dissertation auf Französisch …', ['braucht die Zustimmung des Ausschusses.', 'ist grundsätzlich verboten.', 'ist ohne Weiteres erlaubt.']),
  RP(REGELN, 'Teile der Arbeit, die schon erschienen sind, …', ['müssen gekennzeichnet werden.', 'dürfen nicht verwendet werden.', 'müssen neu geschrieben werden.']),
  RP(REGELN, 'Die Frist von sechs Jahren …', ['kann um maximal zwei Jahre verlängert werden.', 'kann beliebig oft verlängert werden.', 'gilt nicht bei Krankheit.']),
])

# ═════════════════════════ Schreiben ═════════════════════════
S1 = PART('s-forum', 'writing', 'Schreiben — Teil 1', 'Une contribution argumentée sur un forum', 'Lesen Sie die Situation und wählen Sie den besten Text.', 3, [
  RQ(['Dass soziale Medien die öffentliche Debatte verändern, steht außer Frage; strittig ist allein, ob zum Schlechteren. Einerseits ermöglichen sie Menschen eine Stimme, die früher kein Gehör fanden. Andererseits belohnen ihre Mechanismen Zuspitzung statt Abwägung, was die sachliche Auseinandersetzung erschwert. Meines Erachtens liegt die Lösung weniger in Verboten als darin, Plattformen zu mehr Transparenz zu verpflichten und die Medienbildung an Schulen auszubauen.',
      'Dass soziale Medien die öffentliche Debatte verändern, steht außer Frage; strittig ist allein, ob zum Schlechteren. Einerseits sie ermöglichen Menschen eine Stimme, die früher kein Gehör finden. Andererseits ihre Mechanismen belohnen Zuspitzung statt Abwägung, was erschwert die sachliche Auseinandersetzung. Meiner Erachtens nach liegt die Lösung weniger in Verboten als darin, Plattformen zu mehr Transparenz verpflichten.',
      'Soziale Medien sind schlecht. Alle streiten nur noch. Früher war es besser. Man sollte sie verbieten, finde ich. Was meint ihr?',
      'Soziale Medien verändern die Debatte keineswegs, deshalb sind sie ein großes Problem. Einerseits geben sie vielen eine Stimme, folglich sollte man sie verbieten. Andererseits belohnen sie Abwägung, weshalb Verbote unnötig und zugleich die einzige Lösung sind.'],
     '★ Situation: In einem Forum wird diskutiert, ob soziale Medien der öffentlichen Debatte schaden. Schreiben Sie einen Beitrag: Nehmen Sie Stellung, wägen Sie ab und machen Sie einen Vorschlag.'),
  RQ(['So verständlich dieser Wunsch auch ist, er lässt außer Acht, dass nicht alle Familien sich Nachhilfe leisten können.',
      'So verständlich dieser Wunsch auch ist, lässt er außer Acht, dass nicht alle Familien können sich Nachhilfe leisten.',
      'Wie verständlich dieser Wunsch ist auch, er lässt außer Acht, dass sich nicht alle Familien Nachhilfe leisten.',
      'So verständlich auch dieser Wunsch, er außer Acht lässt, dass alle Familien sich keine Nachhilfe leisten können.'],
     '★ Sie möchten in Ihrem Beitrag ein Gegenargument einräumen und es dann entkräften. Welcher Satz ist korrekt?'),
  RQ(['Abschließend lässt sich festhalten, dass die Vorteile zwar überwiegen, die genannten Risiken jedoch nicht unterschätzt werden dürfen.',
      'Abschließend lässt sich festhalten, dass die Vorteile zwar überwiegen, jedoch die genannten Risiken dürfen nicht unterschätzt werden.',
      'Also am Ende: Vorteile gibt es mehr, aber Risiken halt auch, na ja.',
      'Abschließend lässt es sich festhalten, dass überwiegen zwar die Vorteile, die genannten Risiken jedoch nicht unterschätzt zu werden dürfen.'],
     '★ Welcher Schlusssatz passt in Stil und Grammatik zu einem argumentativen Beitrag auf C1-Niveau?'),
])
S2 = PART('s-formell', 'writing', 'Schreiben — Teil 2', 'Un message formel', 'Lesen Sie die Situation und wählen Sie die passende Formulierung.', 2, [
  RQ(['Sehr geehrter Herr Professor Albers, mit großem Bedauern muss ich Ihnen mitteilen, dass ich meine Hausarbeit krankheitsbedingt nicht fristgerecht einreichen kann. Ein ärztliches Attest füge ich bei. Ich wäre Ihnen sehr verbunden, wenn Sie die Abgabefrist um zwei Wochen verlängern könnten. Für Ihr Verständnis danke ich Ihnen im Voraus. Mit freundlichen Grüßen, Elena Marković',
      'Hallo Herr Albers, leider bin ich krank und schaffe die Hausarbeit nicht. Kann ich zwei Wochen mehr kriegen? Attest schicke ich mit. Danke schon mal! LG Elena',
      'Sehr geehrter Herr Professor Albers, mit großem Bedauern muss ich Ihnen mitteilen, dass ich kann meine Hausarbeit krankheitsbedingt nicht fristgerecht einreichen. Ein ärztliches Attest ich füge bei. Ich wäre Ihnen sehr verbunden, wenn Sie verlängern könnten die Abgabefrist um zwei Wochen.',
      'Sehr geehrter Herr Professor Albers, hiermit teile ich Ihnen mit, dass ich meine Hausarbeit fristgerecht eingereicht habe, obwohl ich gesund bin. Bitte verkürzen Sie deshalb die Frist um zwei Wochen. Mit freundlichen Grüßen, Elena Marković'],
     '★ Situation: Sie können Ihre Hausarbeit wegen einer Krankheit nicht rechtzeitig abgeben. Schreiben Sie Ihrem Professor: Entschuldigen Sie sich, verweisen Sie auf das Attest und bitten Sie um eine Verlängerung.'),
  RQ(['Sollten Sie weitere Unterlagen benötigen, lasse ich Ihnen diese selbstverständlich umgehend zukommen.',
      'Wenn Sie noch was brauchen, sagen Sie einfach Bescheid, dann schicke ich es.',
      'Sollten Sie weitere Unterlagen benötigen, ich lasse Ihnen diese selbstverständlich umgehend zukommen.',
      'Solltet ihr weitere Unterlagen benötigen, lasse ich dir diese selbstverständlich umgehend zukommen.'],
     '★ Sie bieten in einer formellen E-Mail an, fehlende Dokumente nachzureichen. Welcher Satz ist angemessen und korrekt?'),
])

write_bank('GOETHEC1', [H1, H2, H3, H4, L1, L2, L3, L4, S1, S2], (30, 30, 5),
  'Questions rédigées par Koto Quest au format de l’examen officiel Goethe-Zertifikat C1 (Goethe-Institut : quatre parties de Hören, quatre de Lesen, deux de Schreiben, consignes en allemand, modules notés sur 100 et validés séparément à 60 points). L’épreuve Schreiben se fait par choix multiple et l’épreuve orale (Sprechen) n’est pas évaluée. Ce ne sont pas des questions officielles.',
  'Questions written by Koto Quest in the format of the official Goethe-Zertifikat C1 exam (Goethe-Institut: four Hören parts, four Lesen parts, two Schreiben parts, instructions in German, modules marked out of 100 and passed separately at 60 points). The Schreiben test is multiple choice and the speaking test (Sprechen) is not assessed. They are not official questions.',
  {'Un podcast': 'A podcast', 'Une interview d’experte': 'An interview with an expert', 'Une discussion : qui dit quoi ?': 'A discussion: who says what?', 'Un exposé scientifique': 'A scientific talk',
   'Un article de vulgarisation': 'A popular science article', 'Un commentaire de presse': 'A press commentary', 'Quatre points de vue : qui dit quoi ?': 'Four viewpoints: who says what?',
   'Un règlement universitaire': 'University regulations', 'Une contribution argumentée sur un forum': 'A reasoned forum post', 'Un message formel': 'A formal message'})
