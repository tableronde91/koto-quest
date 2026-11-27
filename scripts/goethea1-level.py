# Niveau Goethe-Zertifikat A1 (allemand, CECRL A1, « Start Deutsch 1 ») : 8 étapes sur la Route des contes, de Hanau à Brême.
# Mode histoire : l'apprenti·e des frères Grimm ramène dans le grand livre les personnages échappés des contes (voir gen-story.py).
# Les notions sont en allemand (front) avec leur sens en français ; la traduction anglaise du sens sert à l'interface en anglais.
# Usage : python3 scripts/goethea1-level.py   (réécrit content/goethea1/goethea1.json)
from de_common import *
begin('GOETHEA1')

REGION = 'Route des contes'

# ═════════════════════════ 1 : Hallo! — saluer, se présenter, l'alphabet ═════════════════════════
W1 = WORLD('goethea1-w1', ('Hallo! À Hanau', 'Hallo! In Hanau'), REGION,
  ('Saluer et prendre congé, se présenter avec sein, heißen et kommen, épeler son nom et prononcer les lettres propres à l’allemand (ä, ö, ü, ß).', 'Greet and say goodbye, introduce yourself with sein, heißen and kommen, spell your name and pronounce the letters specific to German (ä, ö, ü, ß).'),
  (('Le Rumpelstilzchen', 'Rumpelstiltskin'), 'Ä', ('Ce petit bonhomme danse autour de son feu et ne rend le manuscrit des frères Grimm qu’à qui sait se présenter… et deviner son nom. Dis qui tu es sans faute, puis épelle le sien !', 'This little man dances around his fire and will only give back the Brothers Grimm’s manuscript to someone who can introduce themselves… and guess his name. Say who you are without a mistake, then spell his!')),
  [CH('goethea1-w1-c1', ('Premiers mots', 'First words'), [
    L('de-hallo', ('Hallo! Saluer et prendre congé', 'Hallo! Greeting and saying goodbye'), ('Saluer quelqu’un selon le moment de la journée, demander comment il va et dire au revoir.', 'Greet someone according to the time of day, ask how they are and say goodbye.'), 7, [
        ('Hallo! sert à tout moment entre amis. Guten Morgen = bonjour (le matin), Guten Tag = bonjour (la journée), Guten Abend = bonsoir, Gute Nacht = bonne nuit (au coucher).', 'Hallo! works at any time between friends. Guten Morgen = good morning, Guten Tag = hello (during the day), Guten Abend = good evening, Gute Nacht = good night (at bedtime).'),
        ('Wie geht’s? (familier) / Wie geht es Ihnen? (poli) = comment ça va ? Réponse : Gut, danke. Und dir? (familier) / Und Ihnen? (poli).', 'Wie geht’s? (casual) / Wie geht es Ihnen? (polite) = how are you? Answer: Gut, danke. Und dir? (casual) / Und Ihnen? (polite).'),
        ('Pour partir : Tschüss! (familier), Auf Wiedersehen! (poli), Bis später! (à plus tard), Bis morgen! (à demain). Tous les noms prennent une majuscule en allemand : der Morgen, der Tag.', 'When leaving: Tschüss! (casual), Auf Wiedersehen! (polite), Bis später! (see you later), Bis morgen! (see you tomorrow). All nouns take a capital letter in German: der Morgen, der Tag.'),
      ], [
        D('hallo', 'Hallo!', ('salut, bonjour', 'hi, hello')),
        D('guten-morgen', 'Guten Morgen!', ('bonjour (le matin)', 'good morning')),
        D('guten-tag', 'Guten Tag!', ('bonjour (dans la journée)', 'hello, good day')),
        D('guten-abend', 'Guten Abend!', ('bonsoir', 'good evening')),
        D('wie-gehts', 'Wie geht’s?', ('Comment ça va ?', 'How are things?')),
        D('gut', 'gut', ('bien, bon', 'good, well')),
        D('danke', 'danke', ('merci', 'thank you')),
        D('tschuess', 'Tschüss!', ('salut ! (en partant)', 'bye!')),
        D('auf-wiedersehen', 'Auf Wiedersehen!', ('au revoir', 'goodbye')),
      ], [
        x('Guten Morgen, Herr Grimm! — Guten Morgen! Wie geht’s?', 'Bonjour, monsieur Grimm ! — Bonjour ! Comment ça va ?', 'Good morning, Mr Grimm! — Good morning! How are things?'),
        x('Gut, danke. Und dir?', 'Bien, merci. Et toi ?', 'Fine, thanks. And you?'),
      ], [
        DC(ANSWER, [('Wilhelm', 'Hallo! Wie geht’s?')], ('Wilhelm te demande comment tu vas.', 'Wilhelm asks how you are.'), ['Gut, danke. Und dir?', 'Gute Nacht!', 'Ich heiße Anna.'], 'Gut, danke. Und dir?', ('À Wie geht’s?, on répond Gut, danke.', 'You answer Wie geht’s? with Gut, danke.')),
        FB(COMPLETE, 'Es ist neun Uhr morgens: Guten ＿!', ['Morgen', 'Abend', 'Nacht'], 'Morgen', ('Le matin : Guten Morgen.', 'In the morning: Guten Morgen.'), ('Il est neuf heures du matin : bonjour !', 'It’s nine in the morning: good morning!')),
        TF('Tschüss! Bis morgen!', ('La personne arrive.', 'The person is arriving.'), FAUX, ('Tschüss, bis morgen = salut, à demain : la personne s’en va.', 'Tschüss, bis morgen = bye, see you tomorrow: the person is leaving.')),
        FB(COMPLETE, 'Es ist acht Uhr abends. Guten ＿!', ['Abend', 'Morgen', 'Tag'], 'Abend', ('Le soir : Guten Abend.', 'In the evening: Guten Abend.'), ('Il est huit heures du soir. Bonsoir !', 'It’s eight in the evening. Good evening!')),
      ]),
    L('de-sein-ich', ('Je suis… : ich bin, du bist, ich heiße', 'I am…: ich bin, du bist, ich heiße'), ('Se présenter, dire d’où l’on vient et demander le nom de quelqu’un.', 'Introduce yourself, say where you come from and ask someone’s name.'), 8, [
        ('Le verbe sein (être) au singulier : ich bin (je suis), du bist (tu es), er / sie ist (il / elle est), Sie sind (vous êtes, poli). Le pronom sujet est obligatoire, comme en français.', 'The verb sein (to be) in the singular: ich bin, du bist, er / sie ist, Sie sind (polite you). The subject pronoun is required, as in English.'),
        ('Ich heiße… = je m’appelle… ; Wie heißt du? = comment t’appelles-tu ? ; Wie heißen Sie? (poli). Freut mich! = enchanté·e !', 'Ich heiße… = my name is…; Wie heißt du? = what’s your name?; Wie heißen Sie? (polite). Freut mich! = pleased to meet you!'),
        ('Woher kommst du? = d’où viens-tu ? Ich komme aus Frankreich (je viens de France). Dans une question avec mot interrogatif, le verbe reste en deuxième position : Wie heißt du?', 'Woher kommst du? = where do you come from? Ich komme aus Frankreich (I come from France). In a question with a question word, the verb stays in second position: Wie heißt du?'),
      ], [
        DG('sein-sing', 'ich bin / du bist / er ist', ('je suis / tu es / il est (sein)', 'I am / you are / he is (sein)')),
        D('ich-heisse', 'ich heiße…', ('je m’appelle…', 'my name is…')),
        D('wie-heisst-du', 'Wie heißt du?', ('Comment t’appelles-tu ?', 'What’s your name?')),
        D('freut-mich', 'Freut mich!', ('ravi·e de faire ta connaissance !', 'pleased to meet you!')),
        D('woher', 'Woher kommst du?', ('D’où viens-tu ?', 'Where do you come from?')),
        D('ich-komme-aus', 'ich komme aus…', ('je viens de…', 'I come from…')),
        D('sie-hoeflich', 'Sie', ('vous (politesse)', 'you (polite)')),
        D('herr-frau', 'Herr / Frau', ('monsieur / madame', 'Mr / Mrs, sir / madam')),
      ], [
        x('Ich heiße Jacob Grimm. Ich komme aus Hanau.', 'Je m’appelle Jacob Grimm. Je viens de Hanau.', 'My name is Jacob Grimm. I come from Hanau.'),
        x('Wie heißen Sie? — Ich heiße Dorothea Viehmann. Freut mich!', 'Comment vous appelez-vous ? — Je m’appelle Dorothea Viehmann. Enchantée !', 'What is your name? — My name is Dorothea Viehmann. Pleased to meet you!'),
      ], [
        FB(CHOOSE, 'Ich ＿ Student.', ['bin', 'bist', 'ist'], 'bin', ('Avec ich : bin.', 'With ich: bin.'), ('Je suis étudiant.', 'I am a student.')),
        FB(CHOOSE, 'Sie ＿ aus Kassel.', ['ist', 'bin', 'bist'], 'ist', ('Avec er / sie (il / elle) : ist.', 'With er / sie (he / she): ist.'), ('Elle est de Kassel.', 'She is from Kassel.')),
        DC(ANSWER, [('Jacob', 'Wie heißt du?')], ('Jacob te demande ton nom.', 'Jacob asks your name.'), ['Ich heiße Lukas.', 'Ich komme aus Paris.', 'Gut, danke.'], 'Ich heiße Lukas.', ('On donne son nom avec ich heiße.', 'You give your name with ich heiße.')),
        order(('Remets dans l’ordre : « Je viens de France. »', 'Put in order: “I come from France.”'), ['Ich', 'komme', 'aus', 'Frankreich.'], ('Sujet, verbe en deuxième position, puis aus + pays.', 'Subject, verb in second position, then aus + country.')),
      ]),
  ]),
  CH('goethea1-w1-c2', ('Le nom du lutin', 'The imp’s name'), [
    L('de-alphabet', ('L’alphabet et les sons allemands', 'The alphabet and German sounds'), ('Épeler son nom et prononcer les lettres propres à l’allemand.', 'Spell your name and pronounce the letters specific to German.'), 8, [
        ('Les trémas changent le son : ä = « è » (Mädchen), ö = « eu » (schön), ü = « u » français (Tür). Sans tréma, u se dit « ou » (gut). Le ß (Eszett) se prononce « ss » : heißen.', 'Umlauts change the sound: ä = “eh” (Mädchen), ö = like French “eu” (schön), ü = like French “u” (Tür). Without an umlaut, u sounds like “oo” (gut). ß (Eszett) is pronounced “ss”: heißen.'),
        ('À retenir : w = « v » (Wasser), v = « f » (Vater), z = « ts » (zehn), j = « y » (ja), sch = « ch » (Schule), ei = « aï » (nein), ie = « i » long (sieben), eu = « oï » (neun).', 'To remember: w = “v” (Wasser), v = “f” (Vater), z = “ts” (zehn), j = “y” (ja), sch = “sh” (Schule), ei = “eye” (nein), ie = long “ee” (sieben), eu = “oy” (neun).'),
        ('Pour épeler : Wie schreibt man das? = comment ça s’écrit ? Können Sie das buchstabieren? = pouvez-vous l’épeler ? Le ch est doux après i, e (ich) et raclé après a, o, u (Buch).', 'To spell: Wie schreibt man das? = how do you write that? Können Sie das buchstabieren? = can you spell that? ch is soft after i, e (ich) and throaty after a, o, u (Buch).'),
      ], [
        D('wie-schreibt-man', 'Wie schreibt man das?', ('Comment ça s’écrit ?', 'How do you spell it?')),
        D('buchstabieren', 'buchstabieren', ('épeler', 'to spell')),
        D('buchstabe', 'der Buchstabe', ('la lettre (de l’alphabet)', 'the letter (of the alphabet)')),
        D('name', 'der Name', ('le nom', 'the name')),
        D('vorname', 'der Vorname', ('le prénom', 'the first name')),
        D('familienname', 'der Familienname', ('le nom de famille', 'the surname')),
        D('maedchen', 'das Mädchen', ('la fille, la fillette', 'the girl')),
        D('ja-nein', 'ja / nein', ('oui / non', 'yes / no')),
      ], [
        x('Wie schreibt man das? — G, R, I, M, M: Grimm.', 'Comment ça s’écrit ? — G, R, I, M, M : Grimm.', 'How do you spell that? — G, R, I, M, M: Grimm.'),
        x('Mein Vorname ist Jörg, mit ö.', 'Mon prénom est Jörg, avec un ö.', 'My first name is Jörg, with an ö.'),
      ], [
        DC(ANSWER, [('Rumpelstilzchen', 'Wie schreibt man deinen Namen?')], ('Le lutin veut savoir comment s’écrit ton nom.', 'The imp wants to know how to spell your name.'), ['A, N, N, A: Anna.', 'Ich komme aus Frankreich.', 'Bis morgen!'], 'A, N, N, A: Anna.', ('On épelle lettre par lettre.', 'You spell it letter by letter.')),
        FB(COMPLETE, 'Mein ＿ ist Müller. — Und dein Vorname? — Lena.', ['Familienname', 'Buchstabe', 'Mädchen'], 'Familienname', ('Müller est un nom de famille : Familienname.', 'Müller is a surname: Familienname.'), ('Mon nom de famille est Müller. — Et ton prénom ? — Lena.', 'My surname is Müller. — And your first name? — Lena.')),
        TF('Das „w“ in „Wasser“ spricht man wie ein französisches „v“.', ('Le w allemand se prononce « v ».', 'German w is pronounced “v”.'), VRAI, ('Wasser se dit « vasser » : w = « v ».', 'Wasser is said “vasser”: w = “v”.')),
        FB(COMPLETE, 'Können Sie das bitte ＿? — Ja: H, A, N, A, U.', ['buchstabieren', 'heißen', 'kommen'], 'buchstabieren', ('Épeler = buchstabieren.', 'To spell = buchstabieren.'), ('Pouvez-vous l’épeler, s’il vous plaît ? — Oui : H, A, N, A, U.', 'Can you spell that, please? — Yes: H, A, N, A, U.')),
      ]),
  ])])

# ═════════════════════════ 2 : La famille, haben, les nombres ═════════════════════════
W2 = WORLD('goethea1-w2', ('La maison de Steinau', 'The house in Steinau'), REGION,
  ('Présenter sa famille avec mein et dein, dire ce qu’on a avec haben, donner son âge et compter jusqu’à cent.', 'Introduce your family with mein and dein, say what you have with haben, give your age and count to a hundred.'),
  (('Les sept Nains', 'The Seven Dwarfs'), 'Ö', ('De retour de la mine, les sept Nains trouvent leur maisonnette en désordre : qui a mangé dans leurs assiettes ? Compte les lits, les cuillères et les frères sans te tromper pour qu’ils retournent dans le livre.', 'Back from the mine, the seven Dwarfs find their cottage in a mess: who has been eating from their plates? Count the beds, the spoons and the brothers without a slip so that they go back into the book.')),
  [CH('goethea1-w2-c1', ('Portraits de famille', 'Family portraits'), [
    L('de-familie', ('La famille : mein, dein', 'The family: mein, dein'), ('Présenter les membres de sa famille et dire à qui ils sont liés.', 'Introduce the members of your family and say whose relatives they are.'), 8, [
        ('Chaque nom a un genre : der (masculin), die (féminin), das (neutre). Le pluriel est toujours die : die Eltern (les parents), die Kinder (les enfants). On apprend le nom avec son article.', 'Every noun has a gender: der (masculine), die (feminine), das (neuter). The plural is always die: die Eltern (the parents), die Kinder (the children). Learn each noun with its article.'),
        ('Les possessifs : mein (mon), dein (ton). Ils prennent -e devant un féminin ou un pluriel : mein Vater, meine Mutter, meine Eltern.', 'Possessives: mein (my), dein (your). They take -e before a feminine or plural noun: mein Vater, meine Mutter, meine Eltern.'),
        ('Das ist… = c’est… ; Das sind… = ce sont… Das ist meine Schwester. Das sind meine Brüder. Wer ist das? = qui est-ce ?', 'Das ist… = this is…; Das sind… = these are… Das ist meine Schwester. Das sind meine Brüder. Wer ist das? = who is that?'),
      ], [
        D('familie', 'die Familie', ('la famille', 'the family')),
        D('vater', 'der Vater', ('le père', 'the father')),
        D('mutter', 'die Mutter', ('la mère', 'the mother')),
        D('eltern', 'die Eltern', ('les parents', 'the parents')),
        D('bruder', 'der Bruder', ('le frère', 'the brother')),
        D('schwester', 'die Schwester', ('la sœur', 'the sister')),
        D('kind', 'das Kind', ('l’enfant', 'the child')),
        DG('mein-dein', 'mein / meine, dein / deine', ('mon / ma / mes, ton / ta / tes', 'my, your (informal)')),
        D('wer-ist-das', 'Wer ist das?', ('Qui est-ce ?', 'Who is that?')),
      ], [
        x('Das ist mein Bruder Wilhelm, und das ist meine Schwester Lotte.', 'Voici mon frère Wilhelm, et voici ma sœur Lotte.', 'This is my brother Wilhelm, and this is my sister Lotte.'),
        x('Wer ist das? — Das sind meine Eltern.', 'Qui est-ce ? — Ce sont mes parents.', 'Who is that? — These are my parents.'),
      ], [
        FB(CHOOSE, 'Das ist ＿ Mutter.', ['meine', 'mein', 'meinen'], 'meine', ('Mutter est féminin : meine.', 'Mutter is feminine: meine.'), ('C’est ma mère.', 'This is my mother.')),
        FB(CHOOSE, 'Ist das ＿ Vater?', ['dein', 'deine', 'die'], 'dein', ('Vater est masculin : dein.', 'Vater is masculine: dein.'), ('Est-ce ton père ?', 'Is that your father?')),
        TF('Das sind meine Eltern: mein Vater und meine Mutter.', ('La personne présente son frère et sa sœur.', 'The person is introducing their brother and sister.'), FAUX, ('Die Eltern = les parents : le père et la mère.', 'Die Eltern = the parents: the father and the mother.')),
        DC(ANSWER, [('Zwerg', 'Wer ist das?')], ('Un nain te montre un portrait (c’est ta sœur).', 'A dwarf shows you a portrait (it is your sister).'), ['Das ist meine Schwester.', 'Ich bin gut.', 'Das ist dein Name.'], 'Das ist meine Schwester.', ('Das ist + meine Schwester.', 'Das ist + meine Schwester.')),
      ]),
    L('de-haben', ('Avoir : haben, ein et kein', 'To have: haben, ein and kein'), ('Dire ce qu’on a ou n’a pas, et donner son âge.', 'Say what you have or don’t have, and give your age.'), 8, [
        ('Le verbe haben (avoir) : ich habe, du hast, er / sie hat, wir haben, ihr habt, sie / Sie haben.', 'The verb haben (to have): ich habe, du hast, er / sie hat, wir haben, ihr habt, sie / Sie haben.'),
        ('L’article indéfini : ein (masculin, neutre), eine (féminin). La négation du nom : kein, keine. Ich habe eine Schwester, aber ich habe keine Kinder.', 'The indefinite article: ein (masculine, neuter), eine (feminine). To negate a noun: kein, keine. Ich habe eine Schwester, aber ich habe keine Kinder.'),
        ('Attention : l’âge se dit avec sein, pas avec haben ! Wie alt bist du? — Ich bin zwanzig Jahre alt (j’ai vingt ans).', 'Careful: age uses sein, as in English! Wie alt bist du? — Ich bin zwanzig Jahre alt (I am twenty years old).'),
      ], [
        DG('haben', 'ich habe / du hast / er hat', ('j’ai / tu as / il a (haben)', 'I have / you have / he has (haben)')),
        DG('ein-kein', 'ein, eine / kein, keine', ('un, une / pas de', 'a, an / no, not any')),
        D('wie-alt', 'Wie alt bist du?', ('Quel âge as-tu ?', 'How old are you?')),
        D('jahre-alt', 'Ich bin … Jahre alt.', ('J’ai … ans.', 'I am … years old.')),
        D('sohn', 'der Sohn', ('le fils', 'the son')),
        D('tochter', 'die Tochter', ('la fille (de ses parents)', 'the daughter')),
        D('hund', 'der Hund', ('le chien', 'the dog')),
        D('katze', 'die Katze', ('le chat', 'the cat')),
      ], [
        x('Wir haben sieben Betten, aber wir haben keinen Hund.', 'Nous avons sept lits, mais nous n’avons pas de chien.', 'We have seven beds, but we have no dog.'),
        x('Wie alt bist du? — Ich bin zwölf Jahre alt.', 'Quel âge as-tu ? — J’ai douze ans.', 'How old are you? — I am twelve years old.'),
      ], [
        FB(CHOOSE, 'Du ＿ zwei Brüder.', ['hast', 'habe', 'hat'], 'hast', ('Avec du : hast.', 'With du: hast.'), ('Tu as deux frères.', 'You have two brothers.')),
        FB(CHOOSE, 'Ich ＿ zwanzig Jahre alt.', ['bin', 'habe', 'hat'], 'bin', ('L’âge se dit avec sein : ich bin.', 'Age uses sein: ich bin.'), ('J’ai vingt ans.', 'I am twenty years old.')),
        FB(CHOOSE, 'Sie hat eine Tochter, aber ＿ Sohn.', ['keinen', 'nicht', 'eine'], 'keinen', ('On nie un nom avec kein (ici keinen : masculin, complément d’objet).', 'A noun is negated with kein (here keinen: masculine, direct object).'), ('Elle a une fille, mais pas de fils.', 'She has a daughter but no son.')),
        order(('Remets dans l’ordre : « Nous avons un chat. »', 'Put in order: “We have a cat.”'), ['Wir', 'haben', 'eine', 'Katze.'], ('Sujet, verbe, puis eine Katze (féminin).', 'Subject, verb, then eine Katze (feminine).')),
      ]),
  ]),
  CH('goethea1-w2-c2', ('Sept petits lits', 'Seven little beds'), [
    L('de-zahlen', ('Les nombres de 0 à 100', 'Numbers from 0 to 100'), ('Compter, donner un numéro de téléphone et comprendre un nombre entendu.', 'Count, give a phone number and understand a number you hear.'), 9, [
        ('De 0 à 12 : null, eins, zwei, drei, vier, fünf, sechs, sieben, acht, neun, zehn, elf, zwölf. De 13 à 19 : unité + zehn (dreizehn, vierzehn… mais sechzehn, siebzehn).', 'From 0 to 12: null, eins, zwei, drei, vier, fünf, sechs, sieben, acht, neun, zehn, elf, zwölf. From 13 to 19: unit + zehn (dreizehn, vierzehn… but sechzehn, siebzehn).'),
        ('Les dizaines : zwanzig (20), dreißig (30), vierzig (40), fünfzig (50)… hundert (100).', 'The tens: zwanzig (20), dreißig (30), vierzig (40), fünfzig (50)… hundert (100).'),
        ('Piège : à partir de 21, l’unité se dit avant la dizaine : einundzwanzig (21, « un-et-vingt »), fünfunddreißig (35). À l’oral, écoute donc la fin du nombre !', 'Trap: from 21 on, the unit comes before the ten: einundzwanzig (21, “one-and-twenty”), fünfunddreißig (35). When listening, wait for the end of the number!'),
      ], [
        D('eins', 'eins', ('un (1)', 'one (1)')),
        D('zwei', 'zwei', ('deux (2)', 'two (2)')),
        D('drei', 'drei', ('trois (3)', 'three (3)')),
        D('sieben', 'sieben', ('sept (7)', 'seven (7)')),
        D('zehn', 'zehn', ('dix (10)', 'ten (10)')),
        D('zwoelf', 'zwölf', ('douze (12)', 'twelve (12)')),
        D('zwanzig', 'zwanzig', ('vingt (20)', 'twenty (20)')),
        D('einundzwanzig', 'einundzwanzig', ('vingt et un (21)', 'twenty-one (21)')),
        D('hundert', 'hundert', ('cent (100)', 'a hundred (100)')),
      ], [
        x('Sieben Zwerge, sieben Betten, sieben Löffel.', 'Sept nains, sept lits, sept cuillères.', 'Seven dwarfs, seven beds, seven spoons.'),
        x('Meine Telefonnummer ist null, sechs, eins, zwei, drei.', 'Mon numéro de téléphone est le zéro, six, un, deux, trois.', 'My phone number is zero, six, one, two, three.'),
      ], [
        FB(COMPLETE, 'Zehn plus zwei ist ＿.', ['zwölf', 'zwanzig', 'zwei'], 'zwölf', ('10 + 2 = 12 : zwölf.', '10 + 2 = 12: zwölf.'), ('Dix plus deux font douze.', 'Ten plus two is twelve.')),
        TF('Fünfunddreißig', ('Ce nombre est 53.', 'This number is 53.'), FAUX, ('L’unité se dit d’abord : fünf-und-dreißig = 35.', 'The unit comes first: fünf-und-dreißig = 35.')),
        FB(COMPLETE, '21 = ＿', ['einundzwanzig', 'zwanzigeins', 'zweiundzehn'], 'einundzwanzig', ('Unité + und + dizaine : einundzwanzig.', 'Unit + und + ten: einundzwanzig.'), ('21 = vingt et un', '21 = twenty-one')),
        DC(ANSWER, [('Zwerg', 'Wie viele Zwerge sind wir?')], ('Le nain te demande combien ils sont.', 'The dwarf asks you how many of them there are.'), ['Ihr seid sieben.', 'Ihr seid zwölf.', 'Ich bin sieben Jahre alt.'], 'Ihr seid sieben.', ('Les nains sont sept : sieben.', 'There are seven dwarfs: sieben.')),
      ]),
  ])])

# ═════════════════════════ 3 : La ville, es gibt, le chemin ═════════════════════════
W3 = WORLD('goethea1-w3', ('Les ruelles de Marbourg', 'The lanes of Marburg'), REGION,
  ('Nommer les lieux de la ville avec der, die, das, dire ce qu’il y a avec es gibt, situer un endroit et demander son chemin.', 'Name the places in town with der, die, das, say what there is with es gibt, locate a place and ask the way.'),
  (('Le Loup du Chaperon rouge', 'Red Riding Hood’s Wolf'), 'ß', ('Au pays du Petit Chaperon rouge, le Loup attend au carrefour et envoie les voyageurs sur le mauvais chemin. Demande ta route et comprends les indications pour arriver avant lui chez la grand-mère !', 'In Little Red Riding Hood country, the Wolf waits at the crossroads and sends travellers down the wrong path. Ask your way and understand the directions to reach grandmother’s house before he does!')),
  [CH('goethea1-w3-c1', ('En ville', 'In town'), [
    L('de-stadt', ('La ville : der, die, das et es gibt', 'The town: der, die, das and es gibt'), ('Nommer les lieux d’une ville et dire ce qu’on y trouve.', 'Name the places in a town and say what you can find there.'), 8, [
        ('L’article défini : der Bahnhof (masculin), die Kirche (féminin), das Rathaus (neutre). Rien n’indique toujours le genre : on l’apprend avec le mot. Indice : les noms en -e sont souvent féminins (die Straße, die Schule).', 'The definite article: der Bahnhof (masculine), die Kirche (feminine), das Rathaus (neuter). Nothing always shows the gender: learn it with the word. Hint: nouns ending in -e are often feminine (die Straße, die Schule).'),
        ('Es gibt = il y a. Il est suivi de l’accusatif : Es gibt einen Bahnhof, eine Kirche, ein Rathaus. Négation : Es gibt keinen Bahnhof.', 'Es gibt = there is / there are. It takes the accusative: Es gibt einen Bahnhof, eine Kirche, ein Rathaus. Negative: Es gibt keinen Bahnhof.'),
        ('L’allemand colle les mots : der Bahnhof = die Bahn (le train) + der Hof (la cour) ; das Rathaus = der Rat (le conseil) + das Haus (la maison). Le dernier mot donne le genre.', 'German glues words together: der Bahnhof = die Bahn (the railway) + der Hof (the yard); das Rathaus = der Rat (the council) + das Haus (the house). The last word gives the gender.'),
      ], [
        D('stadt', 'die Stadt', ('la ville', 'the town, the city')),
        D('strasse', 'die Straße', ('la rue', 'the street')),
        D('bahnhof', 'der Bahnhof', ('la gare', 'the railway station')),
        D('kirche', 'die Kirche', ('l’église', 'the church')),
        D('rathaus', 'das Rathaus', ('la mairie, l’hôtel de ville', 'the town hall')),
        D('haus', 'das Haus', ('la maison', 'the house')),
        D('platz', 'der Platz', ('la place', 'the square')),
        D('wald', 'der Wald', ('la forêt', 'the forest')),
        DG('es-gibt', 'es gibt + Akkusativ', ('il y a', 'there is, there are')),
      ], [
        x('In Marburg gibt es ein Schloss und eine alte Kirche.', 'À Marbourg, il y a un château et une vieille église.', 'In Marburg there is a castle and an old church.'),
        x('Das Haus der Großmutter ist im Wald.', 'La maison de la grand-mère est dans la forêt.', 'The grandmother’s house is in the forest.'),
      ], [
        FB(CHOOSE, '＿ Kirche ist sehr alt.', ['Die', 'Der', 'Das'], 'Die', ('Kirche est féminin : die.', 'Kirche is feminine: die.'), ('L’église est très vieille.', 'The church is very old.')),
        FB(CHOOSE, '＿ Rathaus ist am Platz.', ['Das', 'Der', 'Die'], 'Das', ('Rathaus (comme Haus) est neutre : das.', 'Rathaus (like Haus) is neuter: das.'), ('La mairie est sur la place.', 'The town hall is on the square.')),
        FB(COMPLETE, 'In der Stadt ＿ es einen Bahnhof.', ['gibt', 'ist', 'hat'], 'gibt', ('Il y a = es gibt.', 'There is = es gibt.'), ('Dans la ville, il y a une gare.', 'In the town there is a railway station.')),
        TF('Hier gibt es keinen Bahnhof.', ('Il y a une gare ici.', 'There is a railway station here.'), FAUX, ('Keinen Bahnhof = pas de gare.', 'Keinen Bahnhof = no railway station.')),
      ]),
    L('de-wo', ('Où est… ? : wo, hier, neben, in', 'Where is…? wo, hier, neben, in'), ('Demander où se trouve un lieu et le situer.', 'Ask where a place is and locate it.'), 8, [
        ('Wo ist…? = où est… ? Wo ist der Bahnhof? Réponse simple : hier (ici), dort (là-bas), links (à gauche), rechts (à droite), in der Nähe (tout près), weit (loin).', 'Wo ist…? = where is…? Wo ist der Bahnhof? Simple answer: hier (here), dort (over there), links (on the left), rechts (on the right), in der Nähe (nearby), weit (far).'),
        ('Pour situer, la préposition est suivie du datif : der → dem, das → dem, die → der. Neben dem Rathaus (à côté de la mairie), neben der Kirche, in der Stadt.', 'To locate something, the preposition takes the dative: der → dem, das → dem, die → der. Neben dem Rathaus (next to the town hall), neben der Kirche, in der Stadt.'),
        ('Formes contractées très courantes : in + dem = im (im Wald), an + dem = am (am Platz), zu + dem = zum, zu + der = zur.', 'Very common contractions: in + dem = im (im Wald), an + dem = am (am Platz), zu + dem = zum, zu + der = zur.'),
      ], [
        D('wo-ist', 'Wo ist …?', ('Où est… ?', 'Where is…?')),
        D('hier', 'hier', ('ici', 'here')),
        D('dort', 'dort', ('là-bas', 'over there')),
        D('links', 'links', ('à gauche', 'on the left')),
        D('rechts', 'rechts', ('à droite', 'on the right')),
        D('neben', 'neben', ('à côté de', 'next to')),
        D('in-der-naehe', 'in der Nähe', ('tout près, dans les environs', 'nearby')),
        D('weit', 'weit', ('loin', 'far')),
      ], [
        x('Entschuldigung, wo ist der Bahnhof? — Dort, neben der Kirche.', 'Excusez-moi, où est la gare ? — Là-bas, à côté de l’église.', 'Excuse me, where is the station? — Over there, next to the church.'),
        x('Die Großmutter wohnt im Wald. Das ist nicht weit.', 'La grand-mère habite dans la forêt. Ce n’est pas loin.', 'The grandmother lives in the forest. It is not far.'),
      ], [
        FB(CHOOSE, 'Der Bahnhof ist neben ＿ Kirche.', ['der', 'die', 'dem'], 'der', ('Neben + datif : die Kirche → der Kirche.', 'Neben + dative: die Kirche → der Kirche.'), ('La gare est à côté de l’église.', 'The station is next to the church.')),
        FB(CHOOSE, 'Das Haus ist ＿ Wald.', ['im', 'in', 'am'], 'im', ('In + dem Wald = im Wald.', 'In + dem Wald = im Wald.'), ('La maison est dans la forêt.', 'The house is in the forest.')),
        DC(ANSWER, [('Rotkäppchen', 'Entschuldigung, wo ist das Rathaus?')], ('Le Petit Chaperon rouge cherche la mairie (elle est à gauche).', 'Little Red Riding Hood is looking for the town hall (it is on the left).'), ['Das Rathaus ist links.', 'Ich heiße Rathaus.', 'Es gibt sieben.'], 'Das Rathaus ist links.', ('On situe avec ist + links.', 'You locate with ist + links.')),
        TF('Der Platz ist in der Nähe.', ('La place est loin.', 'The square is far away.'), FAUX, ('In der Nähe = tout près.', 'In der Nähe = nearby.')),
      ]),
  ]),
  CH('goethea1-w3-c2', ('Le chemin de la forêt', 'The forest path'), [
    L('de-weg', ('Demander son chemin', 'Asking the way'), ('Demander comment aller quelque part et suivre des indications simples.', 'Ask how to get somewhere and follow simple directions.'), 8, [
        ('Wie komme ich zum Bahnhof / zur Kirche? = comment vais-je à la gare / à l’église ? (zum pour der et das, zur pour die).', 'Wie komme ich zum Bahnhof / zur Kirche? = how do I get to the station / to the church? (zum for der and das, zur for die).'),
        ('L’impératif poli : verbe + Sie. Gehen Sie geradeaus (allez tout droit), nehmen Sie die erste Straße links (prenez la première rue à gauche).', 'The polite imperative: verb + Sie. Gehen Sie geradeaus (go straight on), nehmen Sie die erste Straße links (take the first street on the left).'),
        ('Pour remercier : Danke schön! / Vielen Dank! Réponse : Bitte! (je vous en prie). Entschuldigung! sert à aborder quelqu’un ou à s’excuser.', 'To say thanks: Danke schön! / Vielen Dank! Reply: Bitte! (you’re welcome). Entschuldigung! is used to approach someone or to apologise.'),
      ], [
        D('entschuldigung', 'Entschuldigung!', ('excusez-moi, pardon !', 'excuse me, sorry!')),
        D('wie-komme-ich', 'Wie komme ich zum / zur …?', ('Comment vais-je à… ?', 'How do I get to…?')),
        D('geradeaus', 'geradeaus', ('tout droit', 'straight on')),
        D('gehen', 'gehen', ('aller (à pied)', 'to go (on foot), to walk')),
        D('nehmen', 'nehmen', ('prendre', 'to take')),
        D('weg', 'der Weg', ('le chemin', 'the way, the path')),
        D('vielen-dank', 'Vielen Dank!', ('merci beaucoup !', 'thank you very much!')),
        D('bitte', 'bitte', ('s’il vous plaît ; je vous en prie', 'please; you’re welcome')),
      ], [
        x('Wie komme ich zur Großmutter? — Gehen Sie geradeaus und dann links.', 'Comment vais-je chez la grand-mère ? — Allez tout droit, puis à gauche.', 'How do I get to grandmother’s? — Go straight on and then left.'),
        x('Nehmen Sie den Weg rechts. — Vielen Dank! — Bitte!', 'Prenez le chemin à droite. — Merci beaucoup ! — Je vous en prie !', 'Take the path on the right. — Thank you very much! — You’re welcome!'),
      ], [
        FB(CHOOSE, 'Wie komme ich ＿ Bahnhof?', ['zum', 'zur', 'im'], 'zum', ('Der Bahnhof : zu + dem = zum.', 'Der Bahnhof: zu + dem = zum.'), ('Comment vais-je à la gare ?', 'How do I get to the station?')),
        FB(CHOOSE, 'Wie komme ich ＿ Kirche?', ['zur', 'zum', 'in'], 'zur', ('Die Kirche : zu + der = zur.', 'Die Kirche: zu + der = zur.'), ('Comment vais-je à l’église ?', 'How do I get to the church?')),
        order(('Remets dans l’ordre : « Allez tout droit. »', 'Put in order: “Go straight on.”'), ['Gehen', 'Sie', 'geradeaus.'], ('Impératif poli : verbe, puis Sie.', 'Polite imperative: verb, then Sie.')),
        DC(ANSWER, [('Wolf', 'Nehmen Sie den Weg links. Das ist nicht weit!')], ('Le Loup t’indique un chemin. Remercie-le poliment.', 'The Wolf shows you a path. Thank him politely.'), ['Vielen Dank!', 'Guten Morgen!', 'Ich bin links.'], 'Vielen Dank!', ('On remercie avec Vielen Dank.', 'You say thanks with Vielen Dank.')),
      ]),
  ])])

# ═════════════════════════ 4 : Manger et boire, commander, aimer ═════════════════════════
W4 = WORLD('goethea1-w4', ('À table, à Cassel', 'At the table, in Kassel'), REGION,
  ('Nommer les aliments et les boissons, commander poliment avec ich möchte et l’accusatif, dire ce qu’on aime avec mögen et gern.', 'Name food and drinks, order politely with ich möchte and the accusative, say what you like with mögen and gern.'),
  (('La Sorcière de pain d’épices', 'The Gingerbread Witch'), 'ä', ('Dans sa maison de pain d’épices, la Sorcière propose mille gourmandises… pour mieux te garder. Commande poliment, dis ce que tu aimes et demande l’addition avant qu’elle ne ferme la porte !', 'In her gingerbread house, the Witch offers a thousand treats… the better to keep you. Order politely, say what you like and ask for the bill before she shuts the door!')),
  [CH('goethea1-w4-c1', ('À l’auberge de la conteuse', 'At the storyteller’s inn'), [
    L('de-essen', ('Manger et boire', 'Eating and drinking'), ('Nommer les aliments et les boissons du quotidien et parler des repas.', 'Name everyday food and drinks and talk about meals.'), 8, [
        ('Les repas : das Frühstück (petit-déjeuner), das Mittagessen (déjeuner), das Abendessen (dîner). Le soir, on mange souvent froid : c’est l’Abendbrot, « le pain du soir ».', 'Meals: das Frühstück (breakfast), das Mittagessen (lunch), das Abendessen (dinner). In the evening people often eat a cold meal: the Abendbrot, “evening bread”.'),
        ('Essen (manger) et trinken (boire). Essen change de voyelle : ich esse, du isst, er isst. Trinken est régulier : ich trinke, du trinkst, er trinkt.', 'Essen (to eat) and trinken (to drink). Essen changes its vowel: ich esse, du isst, er isst. Trinken is regular: ich trinke, du trinkst, er trinkt.'),
        ('Sans article pour une quantité indéfinie : Ich esse Brot und trinke Wasser (je mange du pain et je bois de l’eau).', 'No article for an indefinite quantity: Ich esse Brot und trinke Wasser (I eat bread and drink water).'),
      ], [
        D('brot', 'das Brot', ('le pain', 'the bread')),
        D('wasser', 'das Wasser', ('l’eau', 'the water')),
        D('apfel', 'der Apfel', ('la pomme', 'the apple')),
        D('kaese', 'der Käse', ('le fromage', 'the cheese')),
        D('kuchen', 'der Kuchen', ('le gâteau', 'the cake')),
        D('milch', 'die Milch', ('le lait', 'the milk')),
        D('essen', 'essen', ('manger', 'to eat')),
        D('trinken', 'trinken', ('boire', 'to drink')),
        D('fruehstueck', 'das Frühstück', ('le petit-déjeuner', 'the breakfast')),
      ], [
        x('Zum Frühstück esse ich Brot mit Käse und trinke Milch.', 'Au petit-déjeuner, je mange du pain avec du fromage et je bois du lait.', 'For breakfast I eat bread with cheese and drink milk.'),
        x('Hänsel isst Kuchen, und Gretel isst einen Apfel.', 'Hänsel mange du gâteau, et Gretel mange une pomme.', 'Hansel eats cake, and Gretel eats an apple.'),
      ], [
        FB(CHOOSE, 'Du ＿ gern Kuchen.', ['isst', 'esse', 'essen'], 'isst', ('Essen change de voyelle : du isst.', 'Essen changes its vowel: du isst.'), ('Tu manges volontiers du gâteau.', 'You like eating cake.')),
        FB(COMPLETE, 'Ich ＿ ein Glas Wasser.', ['trinke', 'esse', 'heiße'], 'trinke', ('L’eau se boit : trinken.', 'You drink water: trinken.'), ('Je bois un verre d’eau.', 'I drink a glass of water.')),
        TF('Zum Frühstück trinkt Gretel Milch.', ('Gretel boit du lait le matin.', 'Gretel drinks milk in the morning.'), VRAI, ('Das Frühstück est le repas du matin.', 'Das Frühstück is the morning meal.')),
        FB(COMPLETE, 'Das Haus der Hexe ist aus Brot und ＿.', ['Kuchen', 'Wasser', 'Milch'], 'Kuchen', ('Dans le conte, la maison est faite de pain et de gâteau.', 'In the tale, the house is made of bread and cake.'), ('La maison de la sorcière est en pain et en gâteau.', 'The witch’s house is made of bread and cake.')),
      ]),
    L('de-bestellen', ('Commander : ich möchte et l’accusatif', 'Ordering: ich möchte and the accusative'), ('Commander à manger et à boire poliment et demander l’addition.', 'Order food and drink politely and ask for the bill.'), 8, [
        ('Ich möchte… = je voudrais… ; Ich hätte gern… = j’aimerais avoir… Pour commander : Ich möchte einen Kaffee, bitte.', 'Ich möchte… = I would like…; Ich hätte gern… = I’d like to have… To order: Ich möchte einen Kaffee, bitte.'),
        ('Le complément d’objet est à l’accusatif : seul le masculin change. der → den, ein → einen, kein → keinen. Féminin, neutre et pluriel ne changent pas : eine Suppe, ein Wasser.', 'The direct object is in the accusative: only the masculine changes. der → den, ein → einen, kein → keinen. Feminine, neuter and plural stay the same: eine Suppe, ein Wasser.'),
        ('Au restaurant : Was möchten Sie? (que désirez-vous ?), Die Rechnung, bitte! ou Zahlen, bitte! (l’addition, s’il vous plaît), Guten Appetit! (bon appétit).', 'At the restaurant: Was möchten Sie? (what would you like?), Die Rechnung, bitte! or Zahlen, bitte! (the bill, please), Guten Appetit! (enjoy your meal).'),
      ], [
        DG('moechten', 'ich möchte…', ('je voudrais…', 'I would like…')),
        DG('akkusativ', 'den, einen, keinen (Akkusativ)', ('le, un, pas de (masculin complément d’objet)', 'the, a, no (masculine direct object)')),
        D('kaffee', 'der Kaffee', ('le café', 'the coffee')),
        D('tee', 'der Tee', ('le thé', 'the tea')),
        D('suppe', 'die Suppe', ('la soupe', 'the soup')),
        D('rechnung', 'die Rechnung', ('l’addition, la facture', 'the bill')),
        D('guten-appetit', 'Guten Appetit!', ('bon appétit', 'enjoy your meal')),
        D('was-moechten-sie', 'Was möchten Sie?', ('Que désirez-vous ?', 'What would you like?')),
      ], [
        x('Was möchten Sie? — Ich möchte eine Suppe und einen Tee, bitte.', 'Que désirez-vous ? — Je voudrais une soupe et un thé, s’il vous plaît.', 'What would you like? — I would like a soup and a tea, please.'),
        x('Die Rechnung, bitte! — Das macht neun Euro.', 'L’addition, s’il vous plaît ! — Cela fait neuf euros.', 'The bill, please! — That comes to nine euros.'),
      ], [
        FB(CHOOSE, 'Ich möchte ＿ Kaffee, bitte.', ['einen', 'ein', 'eine'], 'einen', ('Der Kaffee, complément d’objet : einen.', 'Der Kaffee, direct object: einen.'), ('Je voudrais un café, s’il vous plaît.', 'I would like a coffee, please.')),
        FB(CHOOSE, 'Ich nehme ＿ Suppe.', ['die', 'den', 'der'], 'die', ('Die Suppe est féminin : pas de changement à l’accusatif.', 'Die Suppe is feminine: no change in the accusative.'), ('Je prends la soupe.', 'I’ll take the soup.')),
        DC(ANSWER, [('Wirtin', 'Guten Tag! Was möchten Sie?')], ('L’aubergiste prend ta commande.', 'The innkeeper takes your order.'), ['Ich möchte einen Tee, bitte.', 'Ich heiße Tee.', 'Die Rechnung ist gut.'], 'Ich möchte einen Tee, bitte.', ('On commande avec ich möchte + accusatif.', 'You order with ich möchte + accusative.')),
        order(('Remets dans l’ordre : « L’addition, s’il vous plaît ! »', 'Put in order: “The bill, please!”'), ['Die', 'Rechnung,', 'bitte!'], ('Die Rechnung, puis bitte.', 'Die Rechnung, then bitte.')),
      ]),
  ]),
  CH('goethea1-w4-c2', ('La maison de pain d’épices', 'The gingerbread house'), [
    L('de-moegen', ('Aimer : mögen, gern et lieber', 'Liking: mögen, gern and lieber'), ('Dire ce qu’on aime, ce qu’on n’aime pas et ce qu’on préfère.', 'Say what you like, what you don’t like and what you prefer.'), 8, [
        ('Mögen (aimer une chose) : ich mag, du magst, er mag, wir mögen. Ich mag Kuchen. Négation avec kein : Ich mag keinen Fisch.', 'Mögen (to like a thing): ich mag, du magst, er mag, wir mögen. Ich mag Kuchen. Negative with kein: Ich mag keinen Fisch.'),
        ('Pour une activité, on ajoute gern au verbe : Ich esse gern Äpfel (j’aime manger des pommes). Négation : nicht gern. Ich trinke nicht gern Milch.', 'For an activity, add gern to the verb: Ich esse gern Äpfel (I like eating apples). Negative: nicht gern. Ich trinke nicht gern Milch.'),
        ('La préférence : lieber (plutôt, de préférence). Ich trinke lieber Tee = je préfère boire du thé. Schmeckt’s? = c’est bon ? — Ja, sehr lecker!', 'Preference: lieber (rather). Ich trinke lieber Tee = I prefer to drink tea. Schmeckt’s? = does it taste good? — Ja, sehr lecker!'),
      ], [
        DG('moegen', 'ich mag / du magst / er mag', ('j’aime / tu aimes / il aime (mögen)', 'I like / you like / he likes (mögen)')),
        DG('gern', 'gern + Verb', ('aimer faire (volontiers)', 'to like doing (gladly)')),
        DG('lieber', 'lieber', ('plutôt, de préférence', 'rather, preferably')),
        D('lecker', 'lecker', ('délicieux', 'delicious')),
        D('fisch', 'der Fisch', ('le poisson', 'the fish')),
        D('fleisch', 'das Fleisch', ('la viande', 'the meat')),
        D('suess', 'süß', ('sucré ; mignon', 'sweet; cute')),
        D('hunger', 'Ich habe Hunger.', ('J’ai faim.', 'I am hungry.')),
      ], [
        x('Ich mag Kuchen, aber ich esse lieber Brot mit Käse.', 'J’aime le gâteau, mais je préfère manger du pain avec du fromage.', 'I like cake, but I prefer to eat bread with cheese.'),
        x('Schmeckt’s? — Ja, das Haus ist sehr lecker!', 'C’est bon ? — Oui, la maison est délicieuse !', 'Does it taste good? — Yes, the house is delicious!'),
      ], [
        FB(CHOOSE, 'Er ＿ keinen Fisch.', ['mag', 'magst', 'mögen'], 'mag', ('Avec er : mag (sans -t).', 'With er: mag (no -t).'), ('Il n’aime pas le poisson.', 'He doesn’t like fish.')),
        FB(COMPLETE, 'Ich trinke ＿ Tee als Kaffee.', ['lieber', 'gern', 'sehr'], 'lieber', ('Préférence entre deux choses : lieber… als.', 'Preference between two things: lieber… als.'), ('Je préfère boire du thé plutôt que du café.', 'I prefer drinking tea to coffee.')),
        TF('Gretel isst nicht gern Fleisch.', ('Gretel aime manger de la viande.', 'Gretel likes eating meat.'), FAUX, ('Nicht gern = ne pas aimer faire.', 'Nicht gern = not to like doing.')),
        DC(ANSWER, [('Hexe', 'Magst du Kuchen?')], ('La Sorcière te demande si tu aimes le gâteau (oui, beaucoup).', 'The Witch asks whether you like cake (yes, a lot).'), ['Ja, ich mag Kuchen sehr.', 'Ja, ich bin Kuchen.', 'Nein, ich komme aus Kuchen.'], 'Ja, ich mag Kuchen sehr.', ('On répond avec ich mag.', 'You answer with ich mag.')),
      ]),
  ])])

# ═════════════════════════ 5 : Le présent, l'heure, la journée ═════════════════════════
W5 = WORLD('goethea1-w5', ('Le château de Sababurg', 'Sababurg Castle'), REGION,
  ('Conjuguer les verbes au présent, placer le verbe en deuxième position, dire l’heure et raconter sa journée avec les verbes à particule.', 'Conjugate verbs in the present, put the verb in second position, tell the time and describe your day with separable verbs.'),
  (('La Treizième Fée', 'The Thirteenth Fairy'), 'ö', ('Au château de la Belle au bois dormant, la Treizième Fée a arrêté toutes les horloges : plus personne ne sait quand se lever. Dis l’heure et raconte une journée entière pour réveiller le château !', 'At Sleeping Beauty’s castle, the Thirteenth Fairy has stopped all the clocks: nobody knows when to get up any more. Tell the time and describe a whole day to wake the castle!')),
  [CH('goethea1-w5-c1', ('Les horloges arrêtées', 'The stopped clocks'), [
    L('de-praesens', ('Le présent et la place du verbe', 'The present tense and verb position'), ('Conjuguer un verbe régulier et construire une phrase simple.', 'Conjugate a regular verb and build a simple sentence.'), 9, [
        ('Le présent : radical + -e, -st, -t, -en, -t, -en. wohnen (habiter) : ich wohne, du wohnst, er wohnt, wir wohnen, ihr wohnt, sie / Sie wohnen.', 'The present: stem + -e, -st, -t, -en, -t, -en. wohnen (to live): ich wohne, du wohnst, er wohnt, wir wohnen, ihr wohnt, sie / Sie wohnen.'),
        ('Règle d’or : dans une phrase déclarative, le verbe conjugué est toujours en deuxième position. Si la phrase commence par autre chose que le sujet, le sujet passe après le verbe : Heute arbeite ich.', 'Golden rule: in a statement, the conjugated verb is always in second position. If the sentence starts with something other than the subject, the subject goes after the verb: Heute arbeite ich.'),
        ('La question sans mot interrogatif commence par le verbe : Wohnst du in Kassel? Négation du verbe avec nicht : Ich arbeite nicht.', 'A question without a question word starts with the verb: Wohnst du in Kassel? The verb is negated with nicht: Ich arbeite nicht.'),
      ], [
        DG('praesens', '-e, -st, -t, -en, -t, -en', ('terminaisons du présent', 'present tense endings')),
        DG('verb-zwei', 'Verb an Position 2', ('verbe en deuxième position', 'verb in second position')),
        D('wohnen', 'wohnen', ('habiter', 'to live (somewhere)')),
        D('arbeiten', 'arbeiten', ('travailler', 'to work')),
        D('lernen', 'lernen', ('apprendre, étudier', 'to learn, to study')),
        D('spielen', 'spielen', ('jouer', 'to play')),
        D('schlafen', 'schlafen', ('dormir', 'to sleep')),
        D('heute', 'heute', ('aujourd’hui', 'today')),
        DG('nicht', 'nicht', ('ne… pas', 'not')),
      ], [
        x('Dornröschen wohnt im Schloss. Heute schläft sie.', 'La Belle au bois dormant habite au château. Aujourd’hui, elle dort.', 'Sleeping Beauty lives in the castle. Today she is sleeping.'),
        x('Arbeitest du heute? — Nein, heute arbeite ich nicht.', 'Tu travailles aujourd’hui ? — Non, aujourd’hui je ne travaille pas.', 'Are you working today? — No, today I’m not working.'),
      ], [
        FB(CHOOSE, 'Wir ＿ Deutsch.', ['lernen', 'lernst', 'lernt'], 'lernen', ('Avec wir : -en.', 'With wir: -en.'), ('Nous apprenons l’allemand.', 'We are learning German.')),
        FB(CHOOSE, 'Wo ＿ du?', ['wohnst', 'wohne', 'wohnen'], 'wohnst', ('Avec du : -st.', 'With du: -st.'), ('Où habites-tu ?', 'Where do you live?')),
        order(('Remets dans l’ordre : « Aujourd’hui, je joue. »', 'Put in order: “Today I am playing.”'), ['Heute', 'spiele', 'ich.'], ('Heute en tête : le verbe reste deuxième, le sujet le suit.', 'Heute first: the verb stays second, the subject follows it.')),
        FB(COMPLETE, 'Der König schläft, die Königin schläft: sie arbeiten ＿.', ['nicht', 'kein', 'nein'], 'nicht', ('On nie un verbe avec nicht.', 'A verb is negated with nicht.'), ('Le roi dort, la reine dort : ils ne travaillent pas.', 'The king is asleep, the queen is asleep: they are not working.')),
      ]),
    L('de-uhrzeit', ('L’heure et les jours', 'The time and the days'), ('Demander et dire l’heure, donner un rendez-vous dans la semaine.', 'Ask and tell the time, arrange to meet during the week.'), 8, [
        ('Wie spät ist es? / Wie viel Uhr ist es? = quelle heure est-il ? Es ist drei Uhr (il est trois heures). Um drei Uhr = à trois heures.', 'Wie spät ist es? / Wie viel Uhr ist es? = what time is it? Es ist drei Uhr (it is three o’clock). Um drei Uhr = at three o’clock.'),
        ('Piège : halb drei = deux heures et demie (« la moitié vers trois ») ! Viertel nach zwei = 2 h 15, Viertel vor drei = 2 h 45. Officiellement : vierzehn Uhr dreißig (14 h 30).', 'Trap: halb drei = half past two (“half towards three”)! Viertel nach zwei = 2:15, Viertel vor drei = 2:45. Officially: vierzehn Uhr dreißig (14:30).'),
        ('Les jours : Montag, Dienstag, Mittwoch, Donnerstag, Freitag, Samstag, Sonntag. Am Montag = lundi ; am Wochenende = le week-end.', 'The days: Montag, Dienstag, Mittwoch, Donnerstag, Freitag, Samstag, Sonntag. Am Montag = on Monday; am Wochenende = at the weekend.'),
      ], [
        D('wie-spaet', 'Wie spät ist es?', ('Quelle heure est-il ?', 'What time is it?')),
        D('uhr', 'die Uhr', ('l’horloge, la montre ; … heure(s)', 'the clock, the watch; o’clock')),
        D('um', 'um … Uhr', ('à … heure(s)', 'at … o’clock')),
        D('halb', 'halb drei', ('deux heures et demie', 'half past two')),
        D('montag', 'der Montag', ('le lundi', 'Monday')),
        D('sonntag', 'der Sonntag', ('le dimanche', 'Sunday')),
        D('wochenende', 'das Wochenende', ('le week-end', 'the weekend')),
        D('wann', 'Wann?', ('Quand ?', 'When?')),
      ], [
        x('Wie spät ist es? — Es ist halb acht.', 'Quelle heure est-il ? — Il est sept heures et demie.', 'What time is it? — It is half past seven.'),
        x('Wann kommt der Prinz? — Am Sonntag um zwölf Uhr.', 'Quand vient le prince ? — Dimanche à midi.', 'When is the prince coming? — On Sunday at twelve o’clock.'),
      ], [
        TF('Es ist halb drei.', ('Il est 3 h 30.', 'It is 3:30.'), FAUX, ('Halb drei = 2 h 30 : la moitié vers trois.', 'Halb drei = 2:30: half towards three.')),
        FB(CHOOSE, 'Der Zug kommt ＿ neun Uhr.', ['um', 'am', 'im'], 'um', ('Devant une heure : um.', 'Before a clock time: um.'), ('Le train arrive à neuf heures.', 'The train arrives at nine o’clock.')),
        FB(CHOOSE, '＿ Montag arbeite ich.', ['Am', 'Um', 'Im'], 'Am', ('Devant un jour : am.', 'Before a day: am.'), ('Lundi, je travaille.', 'On Monday I work.')),
        DC(ANSWER, [('Fee', 'Wie spät ist es?')], ('La Fée te demande l’heure (il est dix heures).', 'The Fairy asks you the time (it is ten o’clock).'), ['Es ist zehn Uhr.', 'Es ist Montag.', 'Um zehn Jahre.'], 'Es ist zehn Uhr.', ('Es ist + heure + Uhr.', 'Es ist + hour + Uhr.')),
      ]),
  ]),
  CH('goethea1-w5-c2', ('Le réveil du château', 'The castle wakes up'), [
    L('de-alltag', ('La journée : les verbes à particule', 'The day: separable verbs'), ('Raconter sa journée, du lever au coucher.', 'Describe your day, from getting up to going to bed.'), 8, [
        ('Beaucoup de verbes ont une particule qui se détache et part à la fin de la phrase : aufstehen (se lever) → Ich stehe um sieben Uhr auf.', 'Many verbs have a prefix that splits off and goes to the end of the sentence: aufstehen (to get up) → Ich stehe um sieben Uhr auf.'),
        ('Autres verbes à particule : einkaufen (faire les courses) → Ich kaufe ein ; fernsehen (regarder la télé) → Er sieht fern ; anfangen (commencer) → Die Schule fängt um acht an.', 'Other separable verbs: einkaufen (to do the shopping) → Ich kaufe ein; fernsehen (to watch TV) → Er sieht fern; anfangen (to begin) → Die Schule fängt um acht an.'),
        ('Les moments : am Morgen (le matin), am Mittag (à midi), am Nachmittag (l’après-midi), am Abend (le soir), mais in der Nacht (la nuit). Zuerst… dann… = d’abord… ensuite…', 'Times of day: am Morgen (in the morning), am Mittag (at noon), am Nachmittag (in the afternoon), am Abend (in the evening), but in der Nacht (at night). Zuerst… dann… = first… then…'),
      ], [
        DG('trennbar', 'trennbare Verben', ('verbes à particule séparable', 'separable verbs')),
        D('aufstehen', 'aufstehen', ('se lever', 'to get up')),
        D('einkaufen', 'einkaufen', ('faire les courses', 'to do the shopping')),
        D('fernsehen', 'fernsehen', ('regarder la télévision', 'to watch television')),
        D('anfangen', 'anfangen', ('commencer', 'to begin, to start')),
        D('am-morgen', 'am Morgen', ('le matin', 'in the morning')),
        D('am-abend', 'am Abend', ('le soir', 'in the evening')),
        D('dann', 'dann', ('ensuite, puis', 'then')),
      ], [
        x('Am Morgen steht der Koch auf, und dann kauft er ein.', 'Le matin, le cuisinier se lève, puis il fait les courses.', 'In the morning the cook gets up, and then he does the shopping.'),
        x('Das Fest fängt am Abend um acht Uhr an.', 'La fête commence le soir à huit heures.', 'The party starts in the evening at eight o’clock.'),
      ], [
        FB(COMPLETE, 'Ich stehe um sechs Uhr ＿.', ['auf', 'ein', 'an'], 'auf', ('Aufstehen : la particule auf va à la fin.', 'Aufstehen: the prefix auf goes to the end.'), ('Je me lève à six heures.', 'I get up at six o’clock.')),
        FB(COMPLETE, 'Am Samstag kaufen wir ＿.', ['ein', 'auf', 'fern'], 'ein', ('Einkaufen : wir kaufen… ein.', 'Einkaufen: wir kaufen… ein.'), ('Samedi, nous faisons les courses.', 'On Saturday we do the shopping.')),
        order(('Remets dans l’ordre : « Le soir, il regarde la télé. »', 'Put in order: “In the evening he watches TV.”'), ['Am', 'Abend', 'sieht', 'er', 'fern.'], ('Le verbe conjugué reste deuxième, la particule fern va à la fin.', 'The conjugated verb stays second, the prefix fern goes to the end.')),
        TF('Die Schule fängt um acht Uhr an.', ('L’école finit à huit heures.', 'School finishes at eight o’clock.'), FAUX, ('Anfangen = commencer.', 'Anfangen = to begin.')),
      ]),
  ])])

# ═════════════════════════ 6 : Les vêtements, les couleurs, les achats ═════════════════════════
W6 = WORLD('goethea1-w6', ('Le marché de Göttingen', 'Göttingen market'), REGION,
  ('Nommer les vêtements et les couleurs, demander un prix, donner son avis et acheter au marché.', 'Name clothes and colours, ask a price, give your opinion and buy at the market.'),
  (('Le Vaillant Petit Tailleur', 'The Brave Little Tailor'), '7', ('« Sept d’un coup ! » Le Vaillant Petit Tailleur se vante sur la place du marché et vend ses ceintures à prix d’or. Nomme les vêtements, demande les prix et marchande sans te laisser impressionner !', '“Seven at one blow!” The Brave Little Tailor boasts on the market square and sells his belts for a fortune. Name the clothes, ask the prices and bargain without being impressed!')),
  [CH('goethea1-w6-c1', ('Sept d’un coup', 'Seven at one blow'), [
    L('de-kleidung', ('Les vêtements et les couleurs', 'Clothes and colours'), ('Décrire ce que l’on porte et donner la couleur d’un vêtement.', 'Describe what you are wearing and give the colour of a piece of clothing.'), 8, [
        ('Tragen (porter) change de voyelle : ich trage, du trägst, er trägt. Er trägt einen Mantel (il porte un manteau) : le vêtement est à l’accusatif.', 'Tragen (to wear) changes its vowel: ich trage, du trägst, er trägt. Er trägt einen Mantel (he is wearing a coat): the piece of clothing is in the accusative.'),
        ('Après sein, l’adjectif de couleur ne s’accorde pas : Der Mantel ist rot, die Hose ist rot, die Schuhe sind rot.', 'After sein, the colour adjective does not change: Der Mantel ist rot, die Hose ist rot, die Schuhe sind rot.'),
        ('Les couleurs : rot (rouge), blau (bleu), grün (vert), gelb (jaune), schwarz (noir), weiß (blanc). Welche Farbe hat…? = de quelle couleur est… ?', 'Colours: rot (red), blau (blue), grün (green), gelb (yellow), schwarz (black), weiß (white). Welche Farbe hat…? = what colour is…?'),
      ], [
        D('kleidung', 'die Kleidung', ('les vêtements', 'clothes, clothing')),
        D('mantel', 'der Mantel', ('le manteau', 'the coat')),
        D('hose', 'die Hose', ('le pantalon', 'the trousers')),
        D('hemd', 'das Hemd', ('la chemise', 'the shirt')),
        D('schuhe', 'die Schuhe', ('les chaussures', 'the shoes')),
        D('tragen', 'tragen', ('porter (un vêtement)', 'to wear')),
        D('farbe', 'die Farbe', ('la couleur', 'the colour')),
        D('rot', 'rot', ('rouge', 'red')),
        D('blau', 'blau', ('bleu', 'blue')),
        D('schwarz-weiss', 'schwarz / weiß', ('noir / blanc', 'black / white')),
      ], [
        x('Das Schneiderlein trägt ein weißes Hemd und eine blaue Hose.', 'Le petit tailleur porte une chemise blanche et un pantalon bleu.', 'The little tailor is wearing a white shirt and blue trousers.'),
        x('Welche Farbe hat der Mantel? — Er ist rot.', 'De quelle couleur est le manteau ? — Il est rouge.', 'What colour is the coat? — It is red.'),
      ], [
        FB(CHOOSE, 'Du ＿ heute einen Mantel.', ['trägst', 'trage', 'tragen'], 'trägst', ('Tragen change de voyelle : du trägst.', 'Tragen changes its vowel: du trägst.'), ('Tu portes un manteau aujourd’hui.', 'You are wearing a coat today.')),
        FB(COMPLETE, 'Die Schuhe ＿ schwarz.', ['sind', 'ist', 'bin'], 'sind', ('Die Schuhe est un pluriel : sind.', 'Die Schuhe is plural: sind.'), ('Les chaussures sont noires.', 'The shoes are black.')),
        TF('Rotkäppchen trägt eine rote Kappe.', ('Le Petit Chaperon rouge porte un bonnet bleu.', 'Little Red Riding Hood wears a blue cap.'), FAUX, ('Rot = rouge.', 'Rot = red.')),
        DC(ANSWER, [('Schneider', 'Welche Farbe hat das Hemd?')], ('Le Tailleur te demande la couleur de la chemise (elle est blanche).', 'The Tailor asks you the colour of the shirt (it is white).'), ['Das Hemd ist weiß.', 'Das Hemd ist neun Euro.', 'Ich trage das Hemd.'], 'Das Hemd ist weiß.', ('Couleur : ist + adjectif.', 'Colour: ist + adjective.')),
      ]),
    L('de-preise', ('Acheter : prix et avis', 'Buying: prices and opinions'), ('Demander le prix, dire qu’un article est cher ou bon marché et conclure un achat.', 'Ask the price, say that an item is expensive or cheap and complete a purchase.'), 8, [
        ('Was kostet das? / Wie viel kostet der Mantel? = combien coûte… ? Au pluriel : Was kosten die Schuhe? Réponse : Das kostet zwanzig Euro.', 'Was kostet das? / Wie viel kostet der Mantel? = how much is…? In the plural: Was kosten die Schuhe? Answer: Das kostet zwanzig Euro.'),
        ('Donner son avis : Das ist teuer (cher), billig (bon marché), zu teuer (trop cher), schön (beau). Zu + adjectif = trop.', 'Giving an opinion: Das ist teuer (expensive), billig (cheap), zu teuer (too expensive), schön (beautiful). Zu + adjective = too.'),
        ('Le vendeur demande : Kann ich Ihnen helfen? (puis-je vous aider ?). Pour conclure : Ich nehme den Mantel (je prends le manteau). Les prix se lisent : 9,50 € = neun Euro fünfzig.', 'The seller asks: Kann ich Ihnen helfen? (can I help you?). To close: Ich nehme den Mantel (I’ll take the coat). Prices are read: €9.50 = neun Euro fünfzig.'),
      ], [
        D('was-kostet', 'Was kostet das?', ('Combien ça coûte ?', 'How much is it?')),
        D('teuer', 'teuer', ('cher', 'expensive')),
        D('billig', 'billig', ('bon marché', 'cheap')),
        D('schoen', 'schön', ('beau, joli', 'beautiful, nice')),
        DG('zu-adj', 'zu + Adjektiv', ('trop + adjectif', 'too + adjective')),
        D('kaufen', 'kaufen', ('acheter', 'to buy')),
        D('markt', 'der Markt', ('le marché', 'the market')),
        D('geld', 'das Geld', ('l’argent', 'the money')),
      ], [
        x('Was kostet der Gürtel? — Zwölf Euro. — Das ist zu teuer!', 'Combien coûte la ceinture ? — Douze euros. — C’est trop cher !', 'How much is the belt? — Twelve euros. — That’s too expensive!'),
        x('Die Schuhe sind schön und billig. Ich nehme sie.', 'Les chaussures sont belles et bon marché. Je les prends.', 'The shoes are nice and cheap. I’ll take them.'),
      ], [
        FB(CHOOSE, 'Was ＿ die Schuhe?', ['kosten', 'kostet', 'koste'], 'kosten', ('Die Schuhe est un pluriel : kosten.', 'Die Schuhe is plural: kosten.'), ('Combien coûtent les chaussures ?', 'How much are the shoes?')),
        FB(COMPLETE, 'Hundert Euro? Das ist ＿ teuer!', ['zu', 'nicht', 'gern'], 'zu', ('Trop cher = zu teuer.', 'Too expensive = zu teuer.'), ('Cent euros ? C’est trop cher !', 'A hundred euros? That’s too expensive!')),
        DC(ANSWER, [('Verkäuferin', 'Der Mantel kostet nur zwanzig Euro.')], ('La vendeuse annonce un petit prix. Tu décides d’acheter.', 'The seller announces a low price. You decide to buy.'), ['Gut, ich nehme den Mantel.', 'Ich trage zwanzig Euro.', 'Der Mantel ist zu teuer.'], 'Gut, ich nehme den Mantel.', ('On conclut avec ich nehme + accusatif.', 'You close with ich nehme + accusative.')),
        TF('Das Hemd ist billig.', ('La chemise coûte cher.', 'The shirt is expensive.'), FAUX, ('Billig = bon marché, le contraire de teuer.', 'Billig = cheap, the opposite of teuer.')),
      ]),
  ])])

# ═════════════════════════ 7 : Le temps qu'il fait, les mois, les projets ═════════════════════════
W7 = WORLD('goethea1-w7', ('La montagne de Dame Holle', 'Mother Holle’s mountain'), REGION,
  ('Parler du temps qu’il fait, des mois et des saisons, et dire ce qu’on veut ou peut faire avec wollen et können.', 'Talk about the weather, months and seasons, and say what you want to or can do with wollen and können.'),
  (('Dame Holle', 'Mother Holle'), '❄', ('Sur le mont Meissner, Dame Holle secoue ses édredons : il neige sur toute la Hesse, même en plein été ! Dis-lui le temps qu’il fait, le mois et la saison pour qu’elle remette le ciel en ordre.', 'On the Hoher Meissner, Mother Holle shakes her featherbeds: it snows all over Hesse, even in midsummer! Tell her the weather, the month and the season so that she puts the sky back in order.')),
  [CH('goethea1-w7-c1', ('Les édredons du ciel', 'The featherbeds of the sky'), [
    L('de-wetter', ('Le temps qu’il fait', 'The weather'), ('Décrire le temps et comprendre un bulletin météo simple.', 'Describe the weather and understand a simple forecast.'), 8, [
        ('Wie ist das Wetter? = quel temps fait-il ? Avec es : Es regnet (il pleut), es schneit (il neige), es ist kalt (il fait froid), es ist warm (il fait chaud).', 'Wie ist das Wetter? = what is the weather like? With es: Es regnet (it is raining), es schneit (it is snowing), es ist kalt (it is cold), es ist warm (it is warm).'),
        ('Die Sonne scheint = le soleil brille, il fait beau. Es ist windig (il y a du vent), es ist bewölkt (c’est nuageux).', 'Die Sonne scheint = the sun is shining. Es ist windig (it is windy), es ist bewölkt (it is cloudy).'),
        ('Les températures : Es sind zwanzig Grad (il fait vingt degrés). Minus fünf Grad = moins cinq. En Allemagne, quand il neige, on dit que Dame Holle secoue ses lits !', 'Temperatures: Es sind zwanzig Grad (it is twenty degrees). Minus fünf Grad = minus five. In Germany, when it snows, people say Mother Holle is shaking out her beds!'),
      ], [
        D('wetter', 'das Wetter', ('le temps (météo)', 'the weather')),
        D('es-regnet', 'Es regnet.', ('Il pleut.', 'It is raining.')),
        D('es-schneit', 'Es schneit.', ('Il neige.', 'It is snowing.')),
        D('sonne', 'die Sonne', ('le soleil', 'the sun')),
        D('kalt', 'kalt', ('froid', 'cold')),
        D('warm', 'warm', ('chaud, doux', 'warm, mild')),
        D('wind', 'der Wind', ('le vent', 'the wind')),
        D('grad', 'der Grad', ('le degré', 'the degree')),
      ], [
        x('Wie ist das Wetter? — Es schneit, und es ist sehr kalt.', 'Quel temps fait-il ? — Il neige, et il fait très froid.', 'What’s the weather like? — It’s snowing, and it’s very cold.'),
        x('Heute scheint die Sonne. Es sind zwanzig Grad.', 'Aujourd’hui, le soleil brille. Il fait vingt degrés.', 'Today the sun is shining. It is twenty degrees.'),
      ], [
        FB(COMPLETE, 'Frau Holle schüttelt die Betten: Es ＿.', ['schneit', 'regnet', 'scheint'], 'schneit', ('Quand Dame Holle secoue ses lits, il neige : es schneit.', 'When Mother Holle shakes her beds, it snows: es schneit.'), ('Dame Holle secoue les lits : il neige.', 'Mother Holle shakes the beds: it snows.')),
        FB(COMPLETE, 'Die Sonne ＿.', ['scheint', 'schneit', 'regnet'], 'scheint', ('Le soleil brille : scheinen.', 'The sun shines: scheinen.'), ('Le soleil brille.', 'The sun is shining.')),
        TF('Es sind minus fünf Grad.', ('Il fait chaud.', 'It is warm.'), FAUX, ('Minus fünf Grad : il fait froid, es ist kalt.', 'Minus five degrees: it is cold, es ist kalt.')),
        DC(ANSWER, [('Frau Holle', 'Wie ist das Wetter heute?')], ('Dame Holle te demande le temps qu’il fait (il pleut).', 'Mother Holle asks you about the weather (it is raining).'), ['Es regnet.', 'Es ist Montag.', 'Ich bin kalt.'], 'Es regnet.', ('Le temps se dit avec es : es regnet.', 'Weather uses es: es regnet.')),
      ]),
    L('de-monate', ('Les mois et les saisons', 'Months and seasons'), ('Situer un événement dans l’année et donner une date simple.', 'Place an event in the year and give a simple date.'), 8, [
        ('Les saisons : der Frühling (printemps), der Sommer (été), der Herbst (automne), der Winter (hiver). Saisons et mois sont tous masculins et s’emploient avec im : im Winter, im Mai.', 'The seasons: der Frühling (spring), der Sommer (summer), der Herbst (autumn), der Winter (winter). Seasons and months are all masculine and take im: im Winter, im Mai.'),
        ('Les mois : Januar, Februar, März, April, Mai, Juni, Juli, August, September, Oktober, November, Dezember.', 'The months: Januar, Februar, März, April, Mai, Juni, Juli, August, September, Oktober, November, Dezember.'),
        ('Rappel des prépositions de temps : um + heure (um acht Uhr), am + jour (am Montag), im + mois ou saison (im Juli). Wann hast du Geburtstag? — Im März.', 'Reminder of time prepositions: um + clock time (um acht Uhr), am + day (am Montag), im + month or season (im Juli). Wann hast du Geburtstag? — Im März.'),
      ], [
        D('fruehling', 'der Frühling', ('le printemps', 'spring')),
        D('sommer', 'der Sommer', ('l’été', 'summer')),
        D('herbst', 'der Herbst', ('l’automne', 'autumn')),
        D('winter', 'der Winter', ('l’hiver', 'winter')),
        D('monat', 'der Monat', ('le mois', 'the month')),
        D('jahr', 'das Jahr', ('l’année, l’an', 'the year')),
        D('geburtstag', 'der Geburtstag', ('l’anniversaire', 'the birthday')),
        DG('im-zeit', 'im + Monat / Jahreszeit', ('en + mois ou saison', 'in + month or season')),
      ], [
        x('Im Winter schneit es, und im Sommer ist es warm.', 'En hiver il neige, et en été il fait chaud.', 'In winter it snows, and in summer it is warm.'),
        x('Wann hast du Geburtstag? — Im Oktober.', 'C’est quand, ton anniversaire ? — En octobre.', 'When is your birthday? — In October.'),
      ], [
        FB(CHOOSE, '＿ Dezember ist es kalt.', ['Im', 'Am', 'Um'], 'Im', ('Devant un mois : im.', 'Before a month: im.'), ('En décembre, il fait froid.', 'In December it is cold.')),
        FB(COMPLETE, 'Juni, Juli und August: Das ist der ＿.', ['Sommer', 'Winter', 'Herbst'], 'Sommer', ('Juin, juillet, août : l’été.', 'June, July, August: summer.'), ('Juin, juillet et août : c’est l’été.', 'June, July and August: that is summer.')),
        TF('Im Frühling schneit es immer.', ('La phrase dit qu’il neige toujours au printemps.', 'The sentence says it always snows in spring.'), VRAI, ('Im Frühling = au printemps ; immer = toujours (ce qui est faux dans la réalité !).', 'Im Frühling = in spring; immer = always (which is not true in real life!).')),
        order(('Remets dans l’ordre : « Mon anniversaire est en mai. »', 'Put in order: “My birthday is in May.”'), ['Mein', 'Geburtstag', 'ist', 'im', 'Mai.'], ('Sujet, verbe, puis im + mois.', 'Subject, verb, then im + month.')),
      ]),
  ]),
  CH('goethea1-w7-c2', ('La porte d’or', 'The golden gate'), [
    L('de-wollen', ('Vouloir et pouvoir : wollen, können', 'Wanting and being able: wollen, können'), ('Dire ce qu’on veut faire, ce qu’on sait faire et proposer une activité.', 'Say what you want to do, what you can do and suggest an activity.'), 8, [
        ('Wollen (vouloir) : ich will, du willst, er will, wir wollen. Können (pouvoir, savoir faire) : ich kann, du kannst, er kann, wir können. Pas de -e ni de -t à ich et er.', 'Wollen (to want): ich will, du willst, er will, wir wollen. Können (can, to be able to): ich kann, du kannst, er kann, wir können. No -e or -t for ich and er.'),
        ('Avec un verbe de modalité, l’autre verbe est à l’infinitif et va à la fin de la phrase : Ich will morgen arbeiten. Kannst du schwimmen?', 'With a modal verb, the other verb is in the infinitive and goes to the end of the sentence: Ich will morgen arbeiten. Kannst du schwimmen?'),
        ('Pour proposer : Wollen wir…? (on… ?). Wollen wir ins Kino gehen? Réponses : Ja, gern! / Gute Idee! / Leider kann ich nicht (malheureusement, je ne peux pas).', 'To suggest: Wollen wir…? (shall we…?). Wollen wir ins Kino gehen? Answers: Ja, gern! / Gute Idee! / Leider kann ich nicht (unfortunately I can’t).'),
      ], [
        DG('wollen', 'ich will / du willst / er will', ('je veux / tu veux / il veut (wollen)', 'I want / you want / he wants (wollen)')),
        DG('koennen', 'ich kann / du kannst / er kann', ('je peux / tu peux / il peut (können)', 'I can / you can / he can (können)')),
        DG('modal-ende', 'Modalverb + Infinitiv am Ende', ('verbe de modalité + infinitif à la fin', 'modal verb + infinitive at the end')),
        D('morgen', 'morgen', ('demain', 'tomorrow')),
        D('helfen', 'helfen', ('aider', 'to help')),
        D('schwimmen', 'schwimmen', ('nager', 'to swim')),
        D('leider', 'leider', ('malheureusement', 'unfortunately')),
        D('gute-idee', 'Gute Idee!', ('Bonne idée !', 'Good idea!')),
      ], [
        x('Ich will Frau Holle helfen: Ich kann die Betten schütteln.', 'Je veux aider Dame Holle : je peux secouer les lits.', 'I want to help Mother Holle: I can shake the beds.'),
        x('Wollen wir morgen schwimmen gehen? — Gute Idee!', 'On va nager demain ? — Bonne idée !', 'Shall we go swimming tomorrow? — Good idea!'),
      ], [
        FB(CHOOSE, 'Er ＿ nicht arbeiten.', ['will', 'willst', 'wollen'], 'will', ('Avec er : will (sans -t).', 'With er: will (no -t).'), ('Il ne veut pas travailler.', 'He doesn’t want to work.')),
        FB(CHOOSE, '＿ du schwimmen?', ['Kannst', 'Kann', 'Können'], 'Kannst', ('Avec du : kannst.', 'With du: kannst.'), ('Sais-tu nager ?', 'Can you swim?')),
        order(('Remets dans l’ordre : « Je veux travailler demain. »', 'Put in order: “I want to work tomorrow.”'), ['Ich', 'will', 'morgen', 'arbeiten.'], ('Le verbe de modalité est deuxième, l’infinitif à la fin.', 'The modal verb is second, the infinitive at the end.')),
        DC(ANSWER, [('Frau Holle', 'Kannst du mir helfen?')], ('Dame Holle te demande de l’aide (tu acceptes volontiers).', 'Mother Holle asks you for help (you gladly accept).'), ['Ja, gern!', 'Nein, es schneit.', 'Ich will Winter.'], 'Ja, gern!', ('On accepte avec Ja, gern!', 'You accept with Ja, gern!')),
      ]),
  ])])

# ═════════════════════════ 8 : Décrire, le corps, devoir ═════════════════════════
W8 = WORLD('goethea1-w8', ('Hamelin et le Joueur de flûte', 'Hamelin and the Pied Piper'), REGION,
  ('Décrire une personne, nommer les parties du corps, dire où l’on a mal et exprimer l’obligation avec müssen.', 'Describe a person, name the parts of the body, say where it hurts and express obligation with müssen.'),
  (('Le Joueur de flûte', 'The Pied Piper'), '♪', ('À Hamelin, le Joueur de flûte au manteau bariolé réclame son dû et menace d’emmener toute la ville derrière lui. Décris-le aux gardes, soigne les danseurs épuisés et rappelle à chacun ce qu’il doit faire !', 'In Hamelin, the Pied Piper in his many-coloured coat demands his due and threatens to lead the whole town away behind him. Describe him to the guards, look after the exhausted dancers and remind everyone what they must do!')),
  [CH('goethea1-w8-c1', ('L’homme au manteau bariolé', 'The man in the many-coloured coat'), [
    L('de-beschreiben', ('Décrire une personne', 'Describing a person'), ('Dire à quoi ressemble quelqu’un et quel est son caractère.', 'Say what someone looks like and what they are like.'), 8, [
        ('Wie sieht er aus? = à quoi ressemble-t-il ? (aussehen est un verbe à particule). Er ist groß (grand), klein (petit), jung (jeune), alt (vieux).', 'Wie sieht er aus? = what does he look like? (aussehen is a separable verb). Er ist groß (tall), klein (small), jung (young), alt (old).'),
        ('Les cheveux et les yeux se décrivent avec haben : Sie hat lange Haare und blaue Augen. Devant un nom au pluriel sans article, l’adjectif prend -e.', 'Hair and eyes are described with haben: Sie hat lange Haare und blaue Augen. Before a plural noun with no article, the adjective takes -e.'),
        ('Pour nuancer : sehr (très), ein bisschen (un peu), nicht (pas). Er ist sehr nett, aber ein bisschen müde.', 'To qualify: sehr (very), ein bisschen (a little), nicht (not). Er ist sehr nett, aber ein bisschen müde.'),
      ], [
        D('gross', 'groß', ('grand', 'big, tall')),
        D('klein', 'klein', ('petit', 'small, short')),
        D('jung', 'jung', ('jeune', 'young')),
        D('alt', 'alt', ('vieux, âgé', 'old, elderly')),
        D('nett', 'nett', ('gentil, sympathique', 'nice, kind')),
        D('haare', 'die Haare', ('les cheveux', 'the hair')),
        D('augen', 'die Augen', ('les yeux', 'the eyes')),
        D('sehr', 'sehr', ('très', 'very')),
        D('ein-bisschen', 'ein bisschen', ('un peu', 'a little')),
      ], [
        x('Der Rattenfänger ist groß und trägt einen bunten Mantel.', 'Le Joueur de flûte est grand et porte un manteau bariolé.', 'The Pied Piper is tall and wears a many-coloured coat.'),
        x('Wie sieht sie aus? — Sie hat lange Haare und blaue Augen.', 'À quoi ressemble-t-elle ? — Elle a les cheveux longs et les yeux bleus.', 'What does she look like? — She has long hair and blue eyes.'),
      ], [
        FB(COMPLETE, 'Der Mann ist nicht klein, er ist ＿.', ['groß', 'jung', 'nett'], 'groß', ('Le contraire de klein : groß.', 'The opposite of klein: groß.'), ('L’homme n’est pas petit, il est grand.', 'The man is not small, he is tall.')),
        FB(CHOOSE, 'Sie ＿ blaue Augen.', ['hat', 'ist', 'sieht'], 'hat', ('Les yeux et les cheveux se décrivent avec haben.', 'Eyes and hair are described with haben.'), ('Elle a les yeux bleus.', 'She has blue eyes.')),
        TF('Die Großmutter ist sehr alt.', ('La grand-mère est très jeune.', 'The grandmother is very young.'), FAUX, ('Alt = vieux, le contraire de jung.', 'Alt = old, the opposite of jung.')),
        DC(ANSWER, [('Wächter', 'Wie sieht der Mann aus?')], ('Le garde te demande de décrire l’homme (il est grand et jeune).', 'The guard asks you to describe the man (he is tall and young).'), ['Er ist groß und jung.', 'Er heißt groß.', 'Er hat zwanzig Jahre.'], 'Er ist groß und jung.', ('Description : er ist + adjectifs.', 'Description: er ist + adjectives.')),
      ]),
    L('de-koerper', ('Le corps et la santé', 'The body and health'), ('Nommer les parties du corps et dire où l’on a mal.', 'Name the parts of the body and say where it hurts.'), 8, [
        ('Le corps : der Kopf (tête), der Arm (bras), das Bein (jambe), die Hand (main), der Fuß (pied), der Bauch (ventre), der Rücken (dos).', 'The body: der Kopf (head), der Arm (arm), das Bein (leg), die Hand (hand), der Fuß (foot), der Bauch (stomach), der Rücken (back).'),
        ('Avoir mal : Mein Kopf tut weh (j’ai mal à la tête), au pluriel Meine Füße tun weh. Ou avec un mot composé : Ich habe Kopfschmerzen, Bauchschmerzen.', 'To be in pain: Mein Kopf tut weh (my head hurts), in the plural Meine Füße tun weh. Or with a compound word: Ich habe Kopfschmerzen, Bauchschmerzen.'),
        ('Chez le médecin : Was fehlt Ihnen? (qu’est-ce qui ne va pas ?). Ich bin krank (je suis malade). Gute Besserung! = bon rétablissement !', 'At the doctor’s: Was fehlt Ihnen? (what is wrong?). Ich bin krank (I am ill). Gute Besserung! = get well soon!'),
      ], [
        D('kopf', 'der Kopf', ('la tête', 'the head')),
        D('arm', 'der Arm', ('le bras', 'the arm')),
        D('bein', 'das Bein', ('la jambe', 'the leg')),
        D('hand', 'die Hand', ('la main', 'the hand')),
        D('fuss', 'der Fuß', ('le pied', 'the foot')),
        D('weh-tun', 'wehtun', ('faire mal', 'to hurt')),
        D('krank', 'krank', ('malade', 'ill, sick')),
        D('arzt', 'der Arzt / die Ärztin', ('le médecin (homme / femme)', 'the doctor (man / woman)')),
        D('gute-besserung', 'Gute Besserung!', ('Bon rétablissement !', 'Get well soon!')),
      ], [
        x('Die Kinder tanzen den ganzen Tag: Ihre Füße tun weh.', 'Les enfants dansent toute la journée : ils ont mal aux pieds.', 'The children dance all day: their feet hurt.'),
        x('Was fehlt Ihnen? — Mein Kopf tut weh. Ich bin krank.', 'Qu’est-ce qui ne va pas ? — J’ai mal à la tête. Je suis malade.', 'What is wrong? — My head hurts. I am ill.'),
      ], [
        FB(CHOOSE, 'Mein Bein ＿ weh.', ['tut', 'tun', 'tue'], 'tut', ('Das Bein est singulier : tut weh.', 'Das Bein is singular: tut weh.'), ('J’ai mal à la jambe.', 'My leg hurts.')),
        FB(CHOOSE, 'Meine Füße ＿ weh.', ['tun', 'tut', 'tust'], 'tun', ('Die Füße est un pluriel : tun weh.', 'Die Füße is plural: tun weh.'), ('J’ai mal aux pieds.', 'My feet hurt.')),
        DC(ANSWER, [('Ärztin', 'Was fehlt Ihnen?')], ('La médecin demande ce qui ne va pas (tu as mal à la tête).', 'The doctor asks what is wrong (you have a headache).'), ['Ich habe Kopfschmerzen.', 'Ich bin ein Kopf.', 'Mein Kopf ist groß.'], 'Ich habe Kopfschmerzen.', ('Douleur : ich habe + Kopfschmerzen.', 'Pain: ich habe + Kopfschmerzen.')),
        FB(COMPLETE, 'Du bist krank? Gute ＿!', ['Besserung', 'Nacht', 'Idee'], 'Besserung', ('À un malade : Gute Besserung!', 'To someone ill: Gute Besserung!'), ('Tu es malade ? Bon rétablissement !', 'You are ill? Get well soon!')),
      ]),
  ]),
  CH('goethea1-w8-c2', ('La dette de la ville', 'The town’s debt'), [
    L('de-muessen', ('Devoir : müssen et l’impératif', 'Having to: müssen and the imperative'), ('Dire ce qu’on doit faire et donner un conseil ou un ordre simple.', 'Say what you have to do and give simple advice or an order.'), 8, [
        ('Müssen (devoir, être obligé) : ich muss, du musst, er muss, wir müssen. Comme les autres verbes de modalité, il renvoie l’infinitif à la fin : Du musst zum Arzt gehen.', 'Müssen (must, to have to): ich muss, du musst, er muss, wir müssen. Like the other modal verbs, it sends the infinitive to the end: Du musst zum Arzt gehen.'),
        ('Dürfen = avoir le droit : Hier darf man nicht rauchen (ici, on n’a pas le droit de fumer). Attention : nicht müssen = ne pas être obligé ; nicht dürfen = ne pas avoir le droit.', 'Dürfen = to be allowed: Hier darf man nicht rauchen (smoking is not allowed here). Careful: nicht müssen = not to have to; nicht dürfen = not to be allowed to.'),
        ('L’impératif familier : le radical du verbe, sans du. Komm! (viens !), Geh nach Hause! (rentre à la maison !), Bezahl bitte! (paie, s’il te plaît !). Poli : Kommen Sie!', 'The informal imperative: the verb stem, without du. Komm! (come!), Geh nach Hause! (go home!), Bezahl bitte! (please pay!). Polite: Kommen Sie!'),
      ], [
        DG('muessen', 'ich muss / du musst / er muss', ('je dois / tu dois / il doit (müssen)', 'I must / you must / he must (müssen)')),
        DG('duerfen', 'dürfen', ('avoir le droit de', 'to be allowed to')),
        DG('imperativ-du', 'Komm! / Geh!', ('Viens ! / Va ! (impératif familier)', 'Come! / Go! (informal imperative)')),
        D('bezahlen', 'bezahlen', ('payer', 'to pay')),
        D('nach-hause', 'nach Hause', ('à la maison (direction)', 'home (direction)')),
        D('kommen', 'kommen', ('venir', 'to come')),
        D('schnell', 'schnell', ('vite, rapide', 'fast, quickly')),
        D('ruhe', 'die Ruhe', ('le calme, le repos', 'quiet, rest')),
      ], [
        x('Die Stadt muss den Rattenfänger bezahlen.', 'La ville doit payer le Joueur de flûte.', 'The town must pay the Pied Piper.'),
        x('Kinder, kommt schnell nach Hause! Ihr dürft nicht mit ihm gehen.', 'Les enfants, rentrez vite à la maison ! Vous n’avez pas le droit de partir avec lui.', 'Children, come home quickly! You are not allowed to go with him.'),
      ], [
        FB(CHOOSE, 'Du ＿ zum Arzt gehen.', ['musst', 'muss', 'müssen'], 'musst', ('Avec du : musst.', 'With du: musst.'), ('Tu dois aller chez le médecin.', 'You must go to the doctor.')),
        order(('Remets dans l’ordre : « Nous devons payer. »', 'Put in order: “We have to pay.”'), ['Wir', 'müssen', 'bezahlen.'], ('Verbe de modalité en deuxième position, infinitif à la fin.', 'Modal verb in second position, infinitive at the end.')),
        FB(COMPLETE, 'Hier ＿ man nicht spielen: Der König schläft.', ['darf', 'muss', 'mag'], 'darf', ('Interdiction : nicht dürfen.', 'Prohibition: nicht dürfen.'), ('Ici, on n’a pas le droit de jouer : le roi dort.', 'You are not allowed to play here: the king is asleep.')),
        DC(ANSWER, [('Bürgermeister', 'Was müssen wir tun?')], ('Le maire demande ce que la ville doit faire (payer le Joueur de flûte).', 'The mayor asks what the town must do (pay the Pied Piper).'), ['Sie müssen den Rattenfänger bezahlen.', 'Sie mögen den Rattenfänger.', 'Sie sind der Rattenfänger.'], 'Sie müssen den Rattenfänger bezahlen.', ('Obligation : müssen + infinitif à la fin.', 'Obligation: müssen + infinitive at the end.')),
      ]),
  ])])

write_level('GOETHEA1', ('Goethe A1 : la Route des contes', 'Goethe A1: the Fairy Tale Route'), REGION, 'Fairy Tale Route', 50,
  [W1, W2, W3, W4, W5, W6, W7, W8, FINAL('GOETHEA1', REGION, ('Simulation Goethe A1 : les Musiciens de Brême', 'Goethe A1 simulation: the Bremen Town Musicians'), 'Hören, Lesen et Schreiben (l’oral, Sprechen, n’est pas évalué)', 'Hören, Lesen and Schreiben (the speaking test, Sprechen, is not assessed)')])
