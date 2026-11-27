# Banque de questions de l'examen blanc Goethe-Zertifikat A1 « Start Deutsch 1 » (content/exams/goethea1.json), au format
# de l'épreuve officielle du Goethe-Institut : Hören (15 questions), Lesen (15 questions) et Schreiben (ici en format à
# choix : compléter un formulaire et choisir le message le mieux écrit). L'épreuve orale (Sprechen) n'est pas évaluée.
# 65 minutes, notation sur 100, réussite à partir de 60 points.
# Dans chaque question, le premier choix est la bonne réponse (l'ordre est mélangé à chaque examen).
# Usage : python3 scripts/goethea1-exam.py
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
    """Lesen : un texte, une question ★."""
    q = RQ(choices, None, '★ ' + question)
    q['passage'] = passage
    return q

R, F = ['Richtig', 'Falsch'], ['Falsch', 'Richtig']

def PART(id, section, jpTitle, title, prompt, count, questions, listening=False):
    for q in questions:
        assert 2 <= len(set(q['choices'])) == len(q['choices']) <= 4, q
    assert len(questions) >= count, id
    p = {'id': id, 'section': section, 'jpTitle': jpTitle, 'title': title, 'prompt': prompt, 'count': count, 'questions': questions}
    if listening:
        p['listening'] = True
    return p

# ═════════════════════════ Hören ═════════════════════════
H1 = PART('h-gespraeche', 'listening', 'Hören — Teil 1', 'Dialogues courts', 'Was ist richtig? Hören Sie das Gespräch und wählen Sie die richtige Antwort.', 6, [
  LQ('F|Guten Tag! Was möchten Sie?\nM|Einen Kaffee und ein Stück Kuchen, bitte.\nN|Frage: Was möchte der Mann?', ['Kaffee und Kuchen.', 'Tee und Brot.', 'Nur ein Wasser.']),
  LQ('M|Entschuldigung, wo ist der Bahnhof?\nF|Gehen Sie geradeaus und dann rechts.\nN|Frage: Wo ist der Bahnhof?', ['Geradeaus und dann rechts.', 'Gleich links.', 'Neben der Kirche.']),
  LQ('F|Was kosten die Äpfel?\nM|Zwei Euro das Kilo.\nN|Frage: Was kosten die Äpfel?', ['Zwei Euro das Kilo.', 'Zwölf Euro das Kilo.', 'Zwei Euro das Stück.']),
  LQ('M|Wann fängt der Film an?\nF|Um halb neun.\nN|Frage: Wann fängt der Film an?', ['Um 8.30 Uhr.', 'Um 9.30 Uhr.', 'Um 9.00 Uhr.']),
  LQ('F|Hast du Geschwister?\nM|Ja, eine Schwester. Sie heißt Clara und ist fünfzehn Jahre alt.\nN|Frage: Wie alt ist Clara?', ['Fünfzehn.', 'Fünf.', 'Fünfzig.']),
  LQ('M|Wie ist das Wetter heute in Bremen?\nF|Es ist kalt, und es regnet ein bisschen.\nN|Frage: Wie ist das Wetter in Bremen?', ['Es ist kalt und es regnet.', 'Die Sonne scheint.', 'Es schneit sehr.']),
  LQ('F|Was machst du am Sonntag?\nM|Ich besuche meine Großeltern in Kassel.\nN|Frage: Was macht der Mann am Sonntag?', ['Er besucht seine Großeltern.', 'Er arbeitet.', 'Er geht ins Kino.']),
  LQ('M|Guten Tag, haben Sie das Hemd auch in Größe L?\nF|Ja, in Blau und in Weiß.\nN|Frage: Welche Farben hat das Hemd?', ['Blau und Weiß.', 'Rot und Schwarz.', 'Grün.']),
  LQ('F|Wo wohnst du?\nM|Ich wohne in Hameln, in der Nähe vom Fluss.\nN|Frage: Wo wohnt der Mann?', ['In Hameln.', 'In Hanau.', 'In Hamburg.']),
  LQ('M|Was fehlt Ihnen?\nF|Mein Kopf tut sehr weh.\nN|Frage: Was fehlt der Frau?', ['Sie hat Kopfschmerzen.', 'Ihr Rücken tut weh.', 'Sie hat Hunger.']),
], listening=True)

H2 = PART('h-durchsagen', 'listening', 'Hören — Teil 2', 'Annonces : vrai ou faux', 'Richtig oder falsch? Hören Sie die Durchsage.', 4, [
  LQ('N|Achtung, eine Durchsage: Der Zug nach Göttingen fährt heute von Gleis vier ab.', R, '★ Der Zug fährt von Gleis vier.'),
  LQ('N|Liebe Kunden, unser Supermarkt schließt in zehn Minuten. Vielen Dank für Ihren Besuch.', F, '★ Der Supermarkt öffnet in zehn Minuten.'),
  LQ('N|Heute im Kaufhaus: Alle Schuhe sind dreißig Prozent billiger.', R, '★ Die Schuhe sind heute billiger.'),
  LQ('N|Das Wetter für morgen: Im Norden regnet es. Im Süden scheint die Sonne, und es ist warm.', F, '★ Im Süden regnet es morgen.'),
  LQ('N|Herzlich willkommen im Brüder-Grimm-Museum. Die Führung beginnt um elf Uhr am Eingang.', R, '★ Die Führung beginnt um elf Uhr.'),
  LQ('N|Information für unsere Gäste: Das Schwimmbad im Hotel ist von zehn bis zwanzig Uhr geöffnet.', F, '★ Das Schwimmbad schließt um zehn Uhr.'),
  LQ('N|Der Bus nach Marburg hat heute zwanzig Minuten Verspätung.', R, '★ Der Bus kommt heute später.'),
], listening=True)

H3 = PART('h-nachrichten', 'listening', 'Hören — Teil 3', 'Messages téléphoniques', 'Was ist richtig? Hören Sie die Nachricht am Telefon.', 5, [
  LQ('F|Hallo Jan, hier ist Lena. Ich kann morgen leider nicht kommen. Können wir uns am Donnerstag treffen? Ruf mich bitte an.\nN|Frage: Wann möchte Lena Jan treffen?', ['Am Donnerstag.', 'Morgen.', 'Am Dienstag.']),
  LQ('M|Guten Tag, hier ist das Restaurant Zur Mühle. Ihr Tisch ist für neun Uhr reserviert, für vier Personen.\nN|Frage: Für wie viele Personen ist der Tisch?', ['Für vier.', 'Für neun.', 'Für zwei.']),
  LQ('M|Hallo Mama. Ich komme um acht Uhr nach Hause. Soll ich das Abendessen machen?\nN|Frage: Wann kommt der Sohn nach Hause?', ['Um acht Uhr.', 'Um elf Uhr.', 'Um vier Uhr.']),
  LQ('F|Hier ist die Praxis Doktor Weber. Ihr Termin ist nicht am Montag, sondern am Mittwoch um zehn Uhr.\nN|Frage: Wann ist der Termin?', ['Am Mittwoch.', 'Am Montag.', 'Um zwölf Uhr.']),
  LQ('F|Meine Telefonnummer ist null, sechs, vier, acht, zwanzig, einunddreißig.\nN|Frage: Wie ist die Nummer?', ['0648 20 31', '0648 12 13', '0684 20 31']),
  LQ('M|Hallo Tom, der Deutschkurs ist jetzt am Dienstag und am Donnerstag, nicht mehr am Montag.\nN|Frage: An welchen Tagen ist der Kurs?', ['Dienstag und Donnerstag.', 'Montag und Mittwoch.', 'Nur am Montag.']),
  LQ('F|Guten Tag, Frau Schmidt. Ihre Schuhe sind fertig. Sie können sie bis achtzehn Uhr abholen. Das macht fünfunddreißig Euro.\nN|Frage: Was kosten die Schuhe?', ['35 €', '53 €', '25 €']),
  LQ('M|Hier ist Paul. Ich bin schon am Bahnhof, aber mein Zug kommt erst in dreißig Minuten. Warte bitte am Rathaus auf mich.\nN|Frage: Wo soll man auf Paul warten?', ['Am Rathaus.', 'Am Bahnhof.', 'Im Zug.']),
], listening=True)

# ═════════════════════════ Lesen ═════════════════════════
MAIL = ('Liebe Marta,\nviele Grüße aus Kassel! Ich bin mit meinem Bruder Paul hier. Unser Hotel ist im Zentrum, neben dem Museum. '
        'Am Morgen besuchen wir die Stadt, und am Nachmittag gehen wir im Park spazieren. Das Essen ist sehr gut: Ich mag die Suppen! '
        'Es ist kalt, nur drei Grad. Am Samstag wollen wir das Schloss Sababurg sehen. Am Sonntag fahren wir mit dem Zug nach Hause.\nBis bald!\nLucie')
L1 = PART('l-email', 'reading', 'Lesen — Teil 1', 'Un courriel : vrai ou faux', 'Richtig oder falsch? Lesen Sie die E-Mail.', 5, [
  RP(MAIL, 'Lucie ist mit ihrem Bruder in Kassel.', R),
  RP(MAIL, 'Das Hotel ist weit vom Zentrum.', F),
  RP(MAIL, 'Am Nachmittag gehen sie im Park spazieren.', R),
  RP(MAIL, 'In Kassel ist es warm.', F),
  RP(MAIL, 'Am Samstag wollen sie ein Schloss sehen.', R),
  RP(MAIL, 'Sie fahren mit dem Auto nach Hause.', F),
  RP(MAIL, 'Lucie mag das Essen nicht.', F),
])

L2 = PART('l-anzeigen', 'reading', 'Lesen — Teil 2', 'Petites annonces', 'Lesen Sie die Anzeige. Was ist richtig?', 5, [
  RP('APOTHEKE AM MARKT\nNotdienst: heute von 22 bis 9 Uhr geöffnet.', 'Die Apotheke …', ['ist in der Nacht geöffnet.', 'ist heute geschlossen.', 'öffnet nur am Morgen.']),
  RP('BRÜDER-GRIMM-MUSEUM\nEintritt: 5 €. Sonntagnachmittag: frei.\nMontag geschlossen.', 'Das Museum …', ['kostet am Sonntagnachmittag nichts.', 'ist jeden Tag geöffnet.', 'kostet am Sonntagnachmittag fünf Euro.']),
  RP('WOHNUNG ZU VERMIETEN\nZwei Zimmer, Küche und Bad. In der Nähe vom Bahnhof. 500 € im Monat.\nTelefon: 0561 34 56 78', 'Die Wohnung …', ['hat zwei Zimmer.', 'ist weit vom Bahnhof.', 'kostet 500 € in der Woche.']),
  RP('GASTHAUS ZUR MÜHLE\nTagesmenü: 12 €\nSuppe, Hauptgericht, Kuchen und ein Getränk.', 'Im Tagesmenü …', ['ist ein Getränk dabei.', 'gibt es keinen Kuchen.', 'kostet die Suppe extra.']),
  RP('STADTBIBLIOTHEK\nMontag bis Freitag: 9 bis 20 Uhr.\nSamstag: 10 bis 14 Uhr.', 'Die Bibliothek …', ['ist am Samstagmorgen geöffnet.', 'ist am Sonntag geöffnet.', 'schließt jeden Tag um 14 Uhr.']),
  RP('GITARRENKURS\nFür Kinder und Erwachsene. Dienstag und Donnerstag um 18 Uhr.\nDie erste Stunde ist gratis.', 'Der Gitarrenkurs …', ['ist an zwei Tagen in der Woche.', 'ist nur für Kinder.', 'ist am Morgen.']),
  RP('MODEHAUS SONNE\nAlles 50 % billiger!\nHemden ab 10 €.', 'Im Modehaus …', ['ist die Kleidung jetzt billiger.', 'kosten die Hemden 50 €.', 'gibt es keine Hemden.']),
  RP('SCHWIMMBAD\nGeöffnet von Juni bis September.\nKinder bis 6 Jahre: gratis.', 'Das Schwimmbad …', ['ist im Sommer geöffnet.', 'ist das ganze Jahr geöffnet.', 'ist für alle gratis.']),
])

L3 = PART('l-schilder', 'reading', 'Lesen — Teil 3', 'Panneaux et messages : vrai ou faux', 'Richtig oder falsch? Lesen Sie den Text.', 5, [
  RP('An der Tür der Bäckerei:\nBÄCKEREI MÜLLER — Am Sonntag geschlossen.', 'Am Sonntag kann man hier Brot kaufen.', F),
  RP('Im Park:\nHunde müssen an der Leine bleiben.', 'Hunde dürfen im Park frei laufen.', F),
  RP('Am Bahnhof:\nDer Zug nach Bremen fährt heute von Gleis 7, nicht von Gleis 2.', 'Der Zug nach Bremen fährt von Gleis 7.', R),
  RP('In der Schule:\nMorgen ist kein Unterricht. Wir sehen uns am Donnerstag.', 'Morgen gibt es Unterricht.', F),
  RP('Im Restaurant:\nHier darf man nicht rauchen.', 'Im Restaurant ist Rauchen verboten.', R),
  RP('An der Arztpraxis:\nSprechstunde: Montag bis Freitag, 8 bis 12 Uhr.', 'Am Samstag ist die Praxis geöffnet.', F),
  RP('Nachricht von Mama:\nIch komme heute spät, um neun Uhr. Das Abendessen ist in der Küche.', 'Das Abendessen ist schon fertig.', R),
  RP('Im Kaufhaus:\nKinderkleidung finden Sie im zweiten Stock.', 'Kleidung für Kinder ist im zweiten Stock.', R),
])

# ═════════════════════════ Schreiben ═════════════════════════
FORM = 'Sie heißen Claire Martin, sind 28 Jahre alt, kommen aus Frankreich, wohnen in Lyon und möchten Deutsch lernen, weil Sie in Deutschland arbeiten wollen.\nANMELDUNG — Sprachschule'
S1 = PART('s-formular', 'writing', 'Schreiben — Teil 1', 'Remplir un formulaire', 'Ergänzen Sie das Formular: Wählen Sie die passende Antwort.', 3, [
  RQ(['Martin', '28 Jahre', 'Frankreich', 'Sonnenstraße 5'], None, f'{FORM}\n★ Familienname:'),
  RQ(['Frankreich', 'Lyon', '28', 'Martin'], None, f'{FORM}\n★ Land:'),
  RQ(['28', 'achtundzwanzig Euro', 'Mai', 'Claire'], None, f'{FORM}\n★ Alter:'),
  RQ(['Ich möchte in Deutschland arbeiten.', 'Es ist Dienstag.', 'Ich bin groß.', 'Ich bin achtundzwanzig.'], None, f'{FORM}\n★ Warum möchten Sie Deutsch lernen?'),
  RQ(['Lyon', 'Frankreich', 'Claire', 'Sprachschule'], None, f'{FORM}\n★ Wohnort:'),
])

S2 = PART('s-nachricht', 'writing', 'Schreiben — Teil 2', 'Un message court', 'Lesen Sie die Situation und wählen Sie die beste Nachricht.', 2, [
  RQ(['Liebe Anna, am Samstag habe ich Geburtstag. Kommst du um acht Uhr zu mir? Wir essen und tanzen. Viele Grüße, Tom',
      'Liebe Anna, am Samstag ich habe Geburtstag. Kommst du um acht Uhr bei mich? Wir essen und tanzt.',
      'Anna, Samstag Geburtstag acht Uhr essen tanzen.',
      'Liebe Anna, am Samstag hast du Geburtstag. Ich komme nicht zu mir. Tschüss.'],
     None, '★ Situation: Laden Sie Ihre Freundin Anna zum Geburtstag ein (Tag, Uhrzeit, Ort, was Sie machen).'),
  RQ(['Lieber Paul, ich bin mit meiner Familie in Bremen. Das Hotel ist sehr schön, und die Sonne scheint. Morgen wollen wir das Rathaus besuchen. Viele Grüße, Sara',
      'Lieber Paul, ich bin mit meine Familie in Bremen. Das Hotel sehr schön ist, und die Sonne scheinen. Morgen wir wollen besuchen das Rathaus.',
      'Paul: Bremen. Familie. Hotel schön. Sonne. Rathaus.',
      'Lieber Paul, ich bin in Bremen. Gestern wollen wir morgen das Rathaus besuchen. Das Hotel ist kalt, und es schneit Sonne.'],
     None, '★ Situation: Schreiben Sie Ihrem Freund Paul eine Postkarte aus dem Urlaub (wo, mit wem, Wetter, ein Plan).'),
  RQ(['Sehr geehrte Damen und Herren, mein Name ist Hugo Leroy. Ich möchte ein Doppelzimmer vom 10. bis 12. Juli reservieren. Vielen Dank! Mit freundlichen Grüßen, Hugo Leroy',
      'Sehr geehrte Damen und Herren, mein Name ist Hugo Leroy. Ich möchte reservieren ein Doppelzimmer vom 10. bis 12. Juli.',
      'Hallo, ich will Zimmer. Danke.',
      'Sehr geehrte Damen und Herren, mein Name ist Hugo Leroy. Ich habe ein Doppelzimmer am 10. Juli. Auf Wiedersehen.'],
     None, '★ Situation: Schreiben Sie an das Hotel und reservieren Sie ein Zimmer (Name, Zimmer, Datum).'),
])

PARTS = [H1, H2, H3, L1, L2, L3, S1, S2]
lis = sum(p['count'] for p in PARTS if p['section'] == 'listening')
rea = sum(p['count'] for p in PARTS if p['section'] == 'reading')
wri = sum(p['count'] for p in PARTS if p['section'] == 'writing')
assert (lis, rea, wri) == (15, 15, 5), (lis, rea, wri)
bank = {
  'slug': 'goethea1',
  'level': 'GOETHEA1',
  'contentVersion': '2026.11.27',
  'notice': 'Questions rédigées par Koto Quest au format de l’examen officiel Goethe-Zertifikat A1 « Start Deutsch 1 » (Goethe-Institut : types d’épreuves, consignes en allemand, notation sur 100, réussite à 60 points). L’épreuve Schreiben se fait par choix multiple et l’épreuve orale (Sprechen) n’est pas évaluée. Ce ne sont pas des questions officielles.',
  'parts': PARTS,
}
json.dump(bank, open(os.path.join(ROOT, 'content/exams/goethea1.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
EN = {
  bank['notice']: 'Questions written by Koto Quest in the format of the official Goethe-Zertifikat A1 “Start Deutsch 1” exam (Goethe-Institut: question types, instructions in German, scoring out of 100, pass at 60 points). The Schreiben test is multiple choice and the speaking test (Sprechen) is not assessed. They are not official questions.',
  'Dialogues courts': 'Short dialogues', 'Annonces : vrai ou faux': 'Announcements: true or false', 'Messages téléphoniques': 'Phone messages',
  'Un courriel : vrai ou faux': 'An email: true or false', 'Petites annonces': 'Small ads', 'Panneaux et messages : vrai ou faux': 'Signs and messages: true or false',
  'Remplir un formulaire': 'Filling in a form', 'Un message court': 'A short message',
}
P_DICT = os.path.join(ROOT, 'content/i18n/en/content.json')
d = json.load(open(P_DICT, encoding='utf-8'))
for k, v in EN.items():
    if k in d and d[k] != v:
        raise SystemExit(f'traduction existante différente : {k} → {d[k]} / {v}')
d.update(EN)
json.dump(d, open(P_DICT, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(f"Goethe A1 : {sum(len(p['questions']) for p in PARTS)} questions en banque ; examen de {lis} + {rea} + {wri} questions")
