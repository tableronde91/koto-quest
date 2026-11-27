# Banque de questions de l'examen blanc Goethe-Zertifikat B1 (content/exams/goetheb1.json), au format de l'épreuve
# officielle du Goethe-Institut : Hören (30 questions en 4 parties), Lesen (30 questions en 5 parties) et Schreiben
# (ici en format à choix : courriel personnel, avis sur un forum, courriel formel). L'épreuve orale (Sprechen) n'est pas évaluée.
# 165 minutes ; chaque module est noté sur 100 et se valide séparément à partir de 60 points.
# Usage : python3 scripts/goetheb1-exam.py
from goethe_exam import *

# ═════════════════════════ Hören ═════════════════════════
def PAIR(audio, aussage, richtig, frage, choices):
    """Teil 1 : un texte, une affirmation vrai / faux puis une question à choix."""
    return [LQ(audio, R if richtig else F, aussage), LQ(audio, choices, frage)]

T1 = [
  PAIR('F|Guten Tag, Herr Okafor, hier ist Schmitt von der Sprachschule Lingua. Ihr B1-Kurs, der am Montag anfangen sollte, beginnt leider erst am Mittwoch, weil die Lehrerin krank geworden ist. Der Raum bleibt derselbe, Raum zwölf im zweiten Stock. Die erste Stunde wird am Ende des Kurses nachgeholt.',
       'Der Kurs fällt ganz aus.', False, 'Warum beginnt der Kurs später?', ['Die Lehrerin ist krank.', 'Der Raum ist nicht frei.', 'Es gibt zu wenige Teilnehmer.']),
  PAIR('N|Verehrte Fahrgäste, wegen Bauarbeiten zwischen Göttingen und Kassel fahren die Züge in Richtung Frankfurt heute nicht von Gleis vier, sondern von Gleis neun. Bitte rechnen Sie mit einer Verspätung von etwa fünfzehn Minuten.',
       'Die Züge nach Frankfurt fahren heute von einem anderen Gleis.', True, 'Was ist der Grund für die Änderung?', ['Bauarbeiten.', 'Ein Unfall.', 'Schlechtes Wetter.']),
  PAIR('M|Hallo Katrin, hier ist Jens. Ich wollte dich an das Konzert am Samstag erinnern. Ich habe die Karten schon abgeholt, sie haben fünfunddreißig Euro pro Stück gekostet. Wir treffen uns am besten um sieben vor der Halle, denn später findet man keinen Parkplatz mehr.',
       'Jens muss die Karten noch kaufen.', False, 'Warum sollen sie sich schon um sieben treffen?', ['Weil man später keinen Parkplatz findet.', 'Weil das Konzert um sieben beginnt.', 'Weil die Karten an der Kasse liegen.']),
  PAIR('N|Und nun das Wetter im Harz: In der Nacht fällt oberhalb von achthundert Metern Schnee. Morgen bleibt es den ganzen Tag bewölkt, bei Temperaturen um zwei Grad. Wer auf den Brocken wandern möchte, sollte warme Kleidung und feste Schuhe mitnehmen.',
       'Auf den Bergen schneit es in der Nacht.', True, 'Was wird Wanderern empfohlen?', ['Warme Kleidung und feste Schuhe.', 'Zu Hause zu bleiben.', 'Einen Regenschirm mitzunehmen.']),
  PAIR('F|Liebe Besucherinnen und Besucher, unser Museum schließt in dreißig Minuten. Die Sonderausstellung über die Brüder Grimm im ersten Stock ist noch bis Sonntag geöffnet. Bitte denken Sie daran, Ihre Taschen und Jacken an der Garderobe abzuholen.',
       'Die Sonderausstellung endet am Sonntag.', True, 'Woran sollen die Besucher denken?', ['Ihre Sachen an der Garderobe abzuholen.', 'Eine Karte für Sonntag zu kaufen.', 'Den ersten Stock sofort zu verlassen.']),
]
H1 = PART('h-kurztexte', 'listening', 'Hören — Teil 1', 'Textes courts : vrai ou faux, puis une question', 'Sie hören fünf kurze Texte. Zu jedem Text lösen Sie zwei Aufgaben.', 10, [q for pair in T1 for q in pair], listening=True)

FUEHRUNG = ('F|Herzlich willkommen in Quedlinburg! Mein Name ist Ute Brandt, und ich führe Sie heute durch unsere Altstadt. '
            'Quedlinburg ist über tausend Jahre alt und hat mehr als zweitausend Fachwerkhäuser. Deshalb gehört die Stadt seit 1994 zum Weltkulturerbe. '
            'Unsere Führung dauert ungefähr neunzig Minuten. Wir beginnen hier am Marktplatz, gehen dann durch die engen Gassen hinauf zum Schlossberg und besichtigen dort die Kirche. '
            'In der Kirche darf leider nicht fotografiert werden. Wer nicht gut zu Fuß ist, kann unten im Café auf uns warten, denn der Weg nach oben ist ziemlich steil. '
            'Nach der Führung haben Sie zwei Stunden Zeit zur freien Verfügung. Ich empfehle Ihnen den Käsekuchen, für den Quedlinburg bekannt ist. '
            'Unser Bus fährt pünktlich um siebzehn Uhr vom Parkplatz am Bahnhof ab. Bitte seien Sie zehn Minuten früher dort.')
H2 = PART('h-fuehrung', 'listening', 'Hören — Teil 2', 'Une visite guidée', 'Sie hören eine Stadtführung. Wählen Sie die richtige Lösung.', 5, [
  LQ(FUEHRUNG, ['Weil sie sehr viele Fachwerkhäuser hat.', 'Weil sie die älteste Stadt Deutschlands ist.', 'Weil dort die Brüder Grimm gelebt haben.'], 'Warum gehört Quedlinburg zum Weltkulturerbe?'),
  LQ(FUEHRUNG, ['Etwa anderthalb Stunden.', 'Etwa zwei Stunden.', 'Den ganzen Nachmittag.'], 'Wie lange dauert die Führung?'),
  LQ(FUEHRUNG, ['Fotografieren.', 'Sprechen.', 'Sitzen.'], 'Was ist in der Kirche verboten?'),
  LQ(FUEHRUNG, ['Im Café warten.', 'Mit dem Bus hinauffahren.', 'Die Führung später machen.'], 'Was können Personen tun, die nicht gut laufen können?'),
  LQ(FUEHRUNG, ['Um 17 Uhr.', 'Um 16.50 Uhr.', 'Um 19 Uhr.'], 'Wann fährt der Bus ab?'),
], listening=True)

GESPRAECH = ('F|Hallo Daniel! Dich habe ich ja lange nicht gesehen. Wohnst du noch in Leipzig?\n'
             'M|Nein, ich bin vor einem halben Jahr nach Köln gezogen, weil ich dort eine Stelle bei einem Verlag bekommen habe.\n'
             'F|Toll! Und gefällt es dir?\n'
             'M|Die Arbeit ja, sehr sogar. Aber eine Wohnung zu finden war furchtbar schwer. Ich habe drei Monate bei einem Kollegen gewohnt, bevor ich etwas gefunden habe.\n'
             'F|Das kenne ich. Meine Schwester sucht seit einem Jahr in München.\n'
             'M|Jetzt habe ich zwei Zimmer am Stadtrand. Die Miete ist hoch, aber ich fahre nur zwanzig Minuten mit der Bahn ins Büro.\n'
             'F|Und kennst du schon Leute?\n'
             'M|Ein paar. Ich bin in einen Chor eingetreten, obwohl ich nicht besonders gut singe. Dort habe ich nette Leute kennengelernt.\n'
             'F|Ich würde auch gern umziehen, aber mein Mann möchte Leipzig nicht verlassen.\n'
             'M|Dann besucht mich doch mal in Köln! Im Februar ist Karneval, das müsst ihr sehen.')
H3 = PART('h-gespraech', 'listening', 'Hören — Teil 3', 'Une conversation : vrai ou faux', 'Sie hören ein Gespräch. Sind die Aussagen richtig oder falsch?', 7, [
  LQ(GESPRAECH, R, 'Daniel ist wegen einer neuen Arbeit umgezogen.'),
  LQ(GESPRAECH, F, 'Daniel ist mit seiner Arbeit unzufrieden.'),
  LQ(GESPRAECH, R, 'Am Anfang hat Daniel bei einem Kollegen gewohnt.'),
  LQ(GESPRAECH, F, 'Daniels Wohnung liegt im Zentrum von Köln.'),
  LQ(GESPRAECH, R, 'Daniel braucht zwanzig Minuten bis zur Arbeit.'),
  LQ(GESPRAECH, R, 'Im Chor hat Daniel neue Leute kennengelernt.'),
  LQ(GESPRAECH, F, 'Der Mann der Frau möchte auch aus Leipzig wegziehen.'),
], listening=True)

DISKUSSION = ('N|Radio Brocken, die Diskussion am Abend. Das Thema heute: Sollten Innenstädte autofrei sein? Im Studio sind Frau Albers, die ein Geschäft in der Altstadt hat, und Herr Demir vom Fahrradclub.\n'
              'M|Ich bin ganz klar dafür. Je weniger Autos fahren, desto besser ist die Luft. Außerdem haben Kinder und ältere Menschen dann endlich Platz.\n'
              'F|Das sehe ich anders. Viele meiner Kunden kommen aus den Dörfern. Wenn sie nicht mehr parken können, bestellen sie alles im Internet.\n'
              'M|In anderen Städten sind nach der Sperrung sogar mehr Leute gekommen, weil man in Ruhe bummeln kann.\n'
              'F|Mag sein. Aber wie sollen meine Waren geliefert werden? Ich kann die Kartons nicht tragen.\n'
              'M|Lieferwagen dürfen natürlich morgens bis zehn Uhr hineinfahren. Das wird überall so gemacht.\n'
              'F|Wichtig wäre mir, dass zuerst die Busse häufiger fahren. Im Moment kommt abends nur einer pro Stunde.\n'
              'M|Da stimme ich Ihnen zu. Ohne bessere Busse und sichere Radwege funktioniert es nicht.\n'
              'F|Und Parkhäuser am Stadtrand müssten billig sein, sonst bezahlen wieder die Leute vom Land.\n'
              'M|Einverstanden. Man sollte es ein Jahr lang testen und dann gemeinsam entscheiden.')
WER = ['Herr Demir', 'Frau Albers', 'Beide']
def WHO3(first):
    return [first] + [w for w in WER if w != first]
H4 = PART('h-diskussion', 'listening', 'Hören — Teil 4', 'Une discussion à la radio : qui dit quoi ?', 'Sie hören eine Diskussion. Wer sagt was?', 8, [
  LQ(DISKUSSION, WHO3('Herr Demir'), 'Weniger Autos bedeuten bessere Luft.'),
  LQ(DISKUSSION, WHO3('Frau Albers'), 'Kunden vom Land könnten lieber online einkaufen.'),
  LQ(DISKUSSION, WHO3('Herr Demir'), 'In anderen Städten kamen danach mehr Besucher.'),
  LQ(DISKUSSION, WHO3('Frau Albers'), 'Die Lieferung der Waren ist ein Problem.'),
  LQ(DISKUSSION, WHO3('Herr Demir'), 'Lieferwagen dürfen am Morgen in die Stadt fahren.'),
  LQ(DISKUSSION, WHO3('Beide'), 'Die Busse müssen öfter fahren.'),
  LQ(DISKUSSION, WHO3('Frau Albers'), 'Parken am Stadtrand sollte nicht teuer sein.'),
  LQ(DISKUSSION, WHO3('Herr Demir'), 'Man sollte die Idee ein Jahr lang ausprobieren.'),
], listening=True)

# ═════════════════════════ Lesen ═════════════════════════
BLOG = ('MEIN JAHR OHNE AUTO — Blog von Tobias\n'
        'Vor einem Jahr ist mein altes Auto kaputtgegangen. Die Reparatur wäre teurer gewesen als ein gebrauchtes Fahrrad, also habe ich das Auto verkauft. '
        'Am Anfang war es schwer. Im Winter bin ich oft nass im Büro angekommen, und meine Kollegen haben gelacht. Trotzdem habe ich weitergemacht. '
        'Nach drei Monaten habe ich gemerkt, dass ich besser schlafe und fast nie mehr krank bin. Außerdem spare ich jeden Monat ungefähr dreihundert Euro. '
        'Natürlich gibt es Nachteile: Große Einkäufe sind kompliziert, und meine Eltern, die auf dem Land wohnen, besuche ich jetzt mit dem Zug, was doppelt so lange dauert. '
        'Wenn ich Kinder hätte, würde ich es mir vielleicht anders überlegen. Aber im Moment kann ich mir nicht vorstellen, wieder ein Auto zu kaufen. '
        'Inzwischen fahren sogar zwei meiner Kollegen mit dem Rad zur Arbeit.')
L1 = PART('l-blog', 'reading', 'Lesen — Teil 1', 'Un blog : vrai ou faux', 'Lesen Sie den Blog. Sind die Aussagen richtig oder falsch?', 6, [
  RP(BLOG, 'Tobias hat sein Auto reparieren lassen.', F),
  RP(BLOG, 'Am Anfang fand Tobias das Leben ohne Auto schwierig.', R),
  RP(BLOG, 'Seine Kollegen haben ihn von Anfang an unterstützt.', F),
  RP(BLOG, 'Tobias fühlt sich heute gesünder als früher.', R),
  RP(BLOG, 'Die Fahrt zu seinen Eltern dauert jetzt länger.', R),
  RP(BLOG, 'Tobias möchte bald wieder ein Auto kaufen.', F),
])

ART1 = ('TAUSCHEN STATT KAUFEN\nIn Goslar hat am Wochenende das erste „Tauschhaus“ der Region eröffnet. Die Idee ist einfach: Wer etwas nicht mehr braucht, bringt es vorbei und darf dafür etwas anderes mitnehmen. '
        'Geld wird nicht benutzt. „Wir wollen, dass weniger weggeworfen wird“, erklärt die Gründerin Hanna Vogt. Besonders beliebt sind Kinderkleidung, Bücher und Werkzeug. '
        'Elektrische Geräte werden nur angenommen, wenn sie funktionieren. Das Tauschhaus wird von zwölf Freiwilligen betreut und ist dienstags und samstags geöffnet.')
ART2 = ('WENIGER STUNDEN, GLEICHES GEHALT\nEine Tischlerei in Wernigerode testet seit einem halben Jahr die Vier-Tage-Woche. Die fünfzehn Angestellten arbeiten von Montag bis Donnerstag jeweils neun Stunden und haben freitags frei. '
        'Der Chef, Martin Krüger, war zuerst skeptisch. „Ich hatte Angst, dass wir weniger Aufträge schaffen“, sagt er. Das Gegenteil ist passiert: Es wird konzentrierter gearbeitet, und es gibt weniger Krankmeldungen. '
        'Seit dem Test bewerben sich außerdem viel mehr junge Leute um eine Ausbildung. Nur einige Kunden mussten sich daran gewöhnen, dass freitags niemand ans Telefon geht.')
L2 = PART('l-presse', 'reading', 'Lesen — Teil 2', 'Deux articles de presse', 'Lesen Sie den Text und wählen Sie die richtige Lösung.', 6, [
  RP(ART1, 'Im Tauschhaus …', ['bezahlt man nichts.', 'kann man billig einkaufen.', 'werden kaputte Geräte repariert.']),
  RP(ART1, 'Das Ziel von Hanna Vogt ist, dass …', ['weniger Dinge im Müll landen.', 'arme Familien Geld bekommen.', 'mehr Leute Bücher lesen.']),
  RP(ART1, 'Elektrische Geräte …', ['müssen funktionieren.', 'werden nie angenommen.', 'sind am beliebtesten.']),
  RP(ART2, 'Die Angestellten der Tischlerei …', ['arbeiten an vier Tagen länger.', 'verdienen jetzt weniger.', 'arbeiten auch am Freitag.']),
  RP(ART2, 'Herr Krüger hatte befürchtet, dass …', ['die Firma weniger Arbeit schafft.', 'die Angestellten kündigen.', 'die Kunden mehr bezahlen müssen.']),
  RP(ART2, 'Seit dem Test …', ['interessieren sich mehr junge Leute für die Firma.', 'gibt es mehr Krankmeldungen.', 'ist die Firma freitags telefonisch erreichbar.']),
])

ANZ = {
  'A': 'A — WANDERN IM HARZ: Geführte Tagestouren für Anfänger, jeden Samstag. Gute Schuhe genügen. Treffpunkt Bahnhof Wernigerode, 9 Uhr.',
  'B': 'B — KOCHKURS „REGIONALE KÜCHE“: Vier Abende, vegetarische Gerichte aus dem Harz. Zutaten inklusive. Mittwochs 18 bis 21 Uhr.',
  'C': 'C — FAHRRADWERKSTATT FÜR ALLE: Reparieren Sie Ihr Rad selbst! Werkzeug und Hilfe kostenlos. Freitags 15 bis 19 Uhr im Jugendzentrum.',
  'D': 'D — SPRACHCAFÉ: Deutsch sprechen in gemütlicher Runde mit Muttersprachlern. Jeden Donnerstagabend in der Stadtbibliothek. Ohne Anmeldung.',
  'E': 'E — NACHBARSCHAFTSHILFE: Wir suchen Freiwillige, die älteren Menschen beim Einkaufen helfen. Zwei Stunden pro Woche reichen.',
  'F': 'F — COMPUTERKURS 60+: Internet und E-Mail in kleinen Schritten. Sechs Vormittage, eigener Laptop nicht nötig.',
  'G': 'G — THEATERGRUPPE sucht Mitspieler ab 16 Jahren. Proben montags. Im Juni spielen wir den „Faust“ auf dem Marktplatz.',
}
ALLE = '\n'.join(ANZ.values())
def AN(situation, letter, wrong):
    return RP(ALLE, situation, ['Anzeige ' + letter] + ['Anzeige ' + w for w in wrong])
L3 = PART('l-anzeigen', 'reading', 'Lesen — Teil 3', 'Petites annonces', 'Lesen Sie die Anzeigen. Welche Anzeige passt zu welcher Person?', 7, [
  AN('Samira lernt seit einem Jahr Deutsch und möchte mehr sprechen, aber keinen Kurs bezahlen.', 'D', ['B', 'F']),
  AN('Herr Lindner ist seit kurzem Rentner und hat noch nie eine E-Mail geschrieben.', 'F', ['D', 'E']),
  AN('Jonas hat einen platten Reifen und wenig Geld.', 'C', ['A', 'E']),
  AN('Frau Petrova hat nachmittags Zeit und möchte etwas für andere Menschen tun.', 'E', ['C', 'G']),
  AN('Mia isst kein Fleisch und möchte neue Rezepte kennenlernen.', 'B', ['A', 'D']),
  AN('Familie Ortega ist neu in der Region und möchte am Wochenende die Natur entdecken.', 'A', ['C', 'G']),
  AN('Leon ist siebzehn und steht gern auf der Bühne.', 'G', ['B', 'F']),
])

THEMA = 'In einer Zeitung lesen Sie Kommentare zum Thema: „Sollen Schüler ihr Handy mit in den Unterricht nehmen dürfen?“\n'
def MEIN(name, text, dafuer):
    return RP(THEMA + f'{name}: {text}', f'Ist {name} für Handys im Unterricht?', ['Ja', 'Nein'] if dafuer else ['Nein', 'Ja'])
L4 = PART('l-meinungen', 'reading', 'Lesen — Teil 4', 'Courrier des lecteurs : pour ou contre ?', 'Lesen Sie die Texte. Ist die Person für Handys im Unterricht?', 7, [
  MEIN('Anja', 'Als Lehrerin sehe ich jeden Tag, wie schwer es den Kindern fällt, sich zu konzentrieren. Sobald ein Handy auf dem Tisch liegt, hört mir die halbe Klasse nicht mehr zu. Die Geräte gehören in die Tasche.', False),
  MEIN('Bernd', 'Wir können nicht so tun, als ob es das Internet nicht gäbe. Meine Tochter recherchiert im Unterricht mit dem Handy und lernt dabei, gute von schlechten Quellen zu unterscheiden. Genau das braucht sie später.', True),
  MEIN('Carla', 'Ich bin fünfzehn und finde, dass man uns mehr vertrauen sollte. Natürlich gibt es Schüler, die nur spielen. Aber deshalb allen das Handy wegzunehmen, wäre ungerecht. Mit klaren Regeln funktioniert es gut.', True),
  MEIN('Dieter', 'Früher haben wir auch ohne Handy gelernt, und zwar nicht schlechter. In den Pausen reden die Kinder kaum noch miteinander. Wenigstens in der Schule sollten sie eine Zeit ohne Bildschirm haben.', False),
  MEIN('Elif', 'An unserer Schule benutzen wir Tablets, die der Schule gehören. Das reicht völlig. Private Handys bringen nur Streit, weil nicht alle Familien sich ein teures Gerät leisten können.', False),
  MEIN('Frank', 'Obwohl ich die Sorgen der Lehrer verstehe, halte ich ein Verbot für altmodisch. Übersetzer, Taschenrechner, Kamera für Experimente: Das alles steckt in einem Gerät, das die Schüler sowieso haben.', True),
  MEIN('Greta', 'Mein Sohn hat in einem Jahr ohne Handy in der Schule viel bessere Noten bekommen. Für mich ist die Sache klar: Während des Unterrichts sollten die Geräte ausgeschaltet beim Lehrer liegen.', False),
])

REGELN = ('HAUSORDNUNG — Jugendherberge Brockenblick\n'
          '1. Die Zimmer können am Anreisetag ab 15 Uhr bezogen werden und müssen am Abreisetag bis 10 Uhr verlassen werden.\n'
          '2. Frühstück gibt es von 7 bis 9.30 Uhr. Wer früher zu einer Wanderung aufbricht, kann am Vorabend ein Lunchpaket bestellen.\n'
          '3. Ab 22 Uhr ist Nachtruhe. Die Haustür wird um 23 Uhr geschlossen; mit der Zimmerkarte kommt man auch später hinein.\n'
          '4. Rauchen ist im ganzen Haus verboten. Im Garten gibt es einen Platz für Raucher.\n'
          '5. Die Küche im Erdgeschoss darf von allen Gästen benutzt werden. Geschirr bitte selbst spülen.\n'
          '6. Haustiere können leider nicht mitgebracht werden.')
L5 = PART('l-hausordnung', 'reading', 'Lesen — Teil 5', 'Un règlement', 'Lesen Sie die Hausordnung und wählen Sie die richtige Lösung.', 4, [
  RP(REGELN, 'Am Abreisetag …', ['muss man das Zimmer bis 10 Uhr verlassen.', 'kann man bis 15 Uhr bleiben.', 'gibt es kein Frühstück.']),
  RP(REGELN, 'Wer sehr früh wandern geht, …', ['kann ein Lunchpaket bestellen.', 'bekommt um 6 Uhr Frühstück.', 'muss auf das Frühstück verzichten.']),
  RP(REGELN, 'Nach 23 Uhr …', ['kommt man mit der Zimmerkarte ins Haus.', 'kommt niemand mehr ins Haus.', 'muss man klingeln.']),
  RP(REGELN, 'In der Küche …', ['spült jeder sein Geschirr selbst.', 'dürfen nur Mitarbeiter kochen.', 'darf geraucht werden.']),
])

# ═════════════════════════ Schreiben ═════════════════════════
S1 = PART('s-email', 'writing', 'Schreiben — Teil 1', 'Un courriel à un ami', 'Lesen Sie die Situation und wählen Sie den besten Text.', 2, [
  RQ(['Liebe Nora, am Samstag habe ich meinen Geburtstag gefeiert. Schade, dass du nicht kommen konntest! Wir haben im Garten gegrillt und bis Mitternacht getanzt. Von meinen Eltern habe ich ein Fahrrad bekommen, über das ich mich riesig gefreut habe. Hast du nächstes Wochenende Zeit? Dann könnten wir zusammen eine Tour machen. Liebe Grüße, Jan',
      'Liebe Nora, am Samstag ich habe meinen Geburtstag gefeiert. Schade, dass du konntest nicht kommen! Wir haben im Garten gegrillt und bis Mitternacht getanzen. Von meinen Eltern habe ich ein Fahrrad bekommen, über dem ich mich riesig gefreut habe.',
      'Hallo Nora. Geburtstag war gut. Fahrrad bekommen. Tschüss.',
      'Liebe Nora, am Samstag feiere ich meinen Geburtstag. Schade, dass du gekommen bist! Von meinen Eltern werde ich gestern ein Fahrrad bekommen.'],
     '★ Situation: Ihre Freundin Nora konnte nicht zu Ihrer Geburtstagsfeier kommen. Schreiben Sie ihr: Wie war die Feier? Welches Geschenk hat Ihnen am besten gefallen? Schlagen Sie ein Treffen vor.'),
  RQ(['Lieber Malte, ich bin gut in Wien angekommen. Die Stadt gefällt mir sehr, obwohl es jeden Tag regnet. Gestern habe ich das Schloss Schönbrunn besichtigt, das noch größer ist, als ich dachte. Wenn du Lust hast, könntest du mich im Mai besuchen. Ich würde mich sehr freuen! Viele Grüße, Eva',
      'Lieber Malte, ich bin gut in Wien angekommen. Die Stadt gefällt mich sehr, obwohl es regnet jeden Tag. Gestern habe ich das Schloss besichtigt, der noch größer ist. Wenn du hast Lust, du könntest mich besuchen.',
      'Malte! Wien schön, Regen, Schloss groß. Komm im Mai.',
      'Lieber Malte, ich komme gut in Wien an. Die Stadt gefällt mir nicht, trotzdem sie schön ist. Gestern besichtige ich das Schloss. Besuch mich, weil du keine Lust hast.'],
     '★ Situation: Sie verbringen ein Semester in Wien. Schreiben Sie Ihrem Freund Malte: Wie gefällt Ihnen die Stadt? Was haben Sie schon gesehen? Laden Sie ihn ein.'),
])
S2 = PART('s-forum', 'writing', 'Schreiben — Teil 2', 'Donner son avis sur un forum', 'Lesen Sie die Situation und wählen Sie den besten Beitrag.', 1, [
  RQ(['Meiner Meinung nach hat die Arbeit zu Hause viele Vorteile: Man spart Zeit, weil man nicht fahren muss, und kann sich besser konzentrieren. Andererseits fehlt mir der Kontakt zu den Kollegen. Deshalb finde ich es am besten, wenn man zwei oder drei Tage pro Woche im Büro arbeitet.',
      'Meiner Meinung nach die Arbeit zu Hause hat viele Vorteile: Man spart Zeit, weil man muss nicht fahren. Andererseits mir fehlt der Kontakt. Deshalb ich finde es am besten, zwei Tage im Büro arbeiten.',
      'Homeoffice ist gut. Büro ist auch gut. Ich weiß nicht.',
      'Ich bin dagegen, weil die Arbeit zu Hause viele Vorteile hat. Trotzdem spart man Zeit, obwohl man nicht fahren muss. Also sollte niemand im Büro oder zu Hause arbeiten.'],
     '★ Situation: Im Forum Ihrer Firma wird diskutiert: „Homeoffice — ja oder nein?“ Schreiben Sie Ihre Meinung mit Gründen.'),
  RQ(['Ich finde, dass Kinder nicht zu früh ein eigenes Handy bekommen sollten. Einerseits ist es praktisch, wenn die Eltern sie erreichen können. Andererseits verbringen viele Kinder dann zu viel Zeit vor dem Bildschirm. Mit zwölf Jahren und klaren Regeln wäre es für mich in Ordnung.',
      'Ich finde, dass Kinder sollten nicht zu früh ein Handy bekommen. Einerseits es ist praktisch, wenn die Eltern können sie erreichen. Mit zwölf Jahre und klare Regeln es wäre in Ordnung.',
      'Handy für Kinder: nein. Oder ja. Egal.',
      'Ich finde, dass Kinder früh ein Handy bekommen sollten, weil sie zu viel Zeit vor dem Bildschirm verbringen. Deshalb bin ich dagegen und dafür.'],
     '★ Situation: In einem Elternforum lesen Sie die Frage: „Ab welchem Alter sollten Kinder ein eigenes Handy haben?“ Schreiben Sie Ihre Meinung.'),
])
S3 = PART('s-formell', 'writing', 'Schreiben — Teil 3', 'Un courriel formel', 'Lesen Sie die Situation und wählen Sie die passende Formulierung.', 2, [
  RQ(['Sehr geehrte Frau Dr. Henning, leider kann ich am Dienstag nicht zum Termin kommen, da ich beruflich verreisen muss. Wäre es möglich, den Termin auf Donnerstag zu verschieben? Für Ihr Verständnis danke ich Ihnen im Voraus. Mit freundlichen Grüßen, Paul Mertens',
      'Hallo Frau Henning, ich komme Dienstag nicht, ich muss weg. Geht Donnerstag? Danke, Paul',
      'Sehr geehrte Frau Dr. Henning, leider ich kann am Dienstag nicht kommen, da ich muss beruflich verreisen. Wäre es möglich, verschieben den Termin? Mit freundlichen Grüßen',
      'Liebe Frau Dr. Henning, ich habe keine Lust auf den Termin am Dienstag. Verschieben Sie ihn sofort auf Donnerstag! Tschüss, Paul'],
     '★ Situation: Sie haben am Dienstag einen Termin bei Ihrer Kursleiterin, Frau Dr. Henning, können aber nicht kommen. Schreiben Sie ihr: Entschuldigung, Grund, neuer Vorschlag.'),
  RQ(['Könnten Sie mir bitte mitteilen, ob in dem Kurs noch Plätze frei sind?', 'Sagen Sie mir, ob gibt es noch Plätze!', 'Ich will wissen, sind noch Plätze frei?', 'Können Sie mir mitteilen, wenn noch Plätze frei sind?'],
     '★ Sie möchten höflich fragen, ob es im Kurs noch freie Plätze gibt. Was schreiben Sie?'),
  RQ(['Ich würde mich über eine baldige Antwort sehr freuen.', 'Antworten Sie schnell!', 'Ich freue mich an eine baldige Antwort.', 'Ich warte Ihre Antwort bald.'],
     '★ Wie beenden Sie einen formellen Brief höflich, wenn Sie auf eine Antwort warten?'),
])

write_bank('GOETHEB1', [H1, H2, H3, H4, L1, L2, L3, L4, L5, S1, S2, S3], (30, 30, 5),
  'Questions rédigées par Koto Quest au format de l’examen officiel Goethe-Zertifikat B1 (Goethe-Institut : types d’épreuves, consignes en allemand, modules notés sur 100 et validés séparément à 60 points). L’épreuve Schreiben se fait par choix multiple et l’épreuve orale (Sprechen) n’est pas évaluée. Ce ne sont pas des questions officielles.',
  'Questions written by Koto Quest in the format of the official Goethe-Zertifikat B1 exam (Goethe-Institut: question types, instructions in German, modules marked out of 100 and passed separately at 60 points). The Schreiben test is multiple choice and the speaking test (Sprechen) is not assessed. They are not official questions.',
  {'Textes courts : vrai ou faux, puis une question': 'Short texts: true or false, then a question', 'Une visite guidée': 'A guided tour', 'Une conversation : vrai ou faux': 'A conversation: true or false',
   'Une discussion à la radio : qui dit quoi ?': 'A radio discussion: who says what?', 'Un blog : vrai ou faux': 'A blog: true or false', 'Deux articles de presse': 'Two press articles',
   'Courrier des lecteurs : pour ou contre ?': 'Readers’ letters: for or against?', 'Un règlement': 'House rules', 'Un courriel à un ami': 'An email to a friend',
   'Donner son avis sur un forum': 'Giving your opinion on a forum', 'Un courriel formel': 'A formal email'})
