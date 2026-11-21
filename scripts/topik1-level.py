# Niveau TOPIK 1 (coréen, TOPIK I niveau 1) : 8 îles, 28 leçons et un examen blanc (français + anglais).
# Écrit aussi l'onglet Hangeul (content/characters/hangul.json) : mêmes notions que les îles 1 et 2.
# Usage : python3 scripts/topik1-level.py   (réécrit content/topik1/topik1.json et content/characters/hangul.json)
import json, os, sys
sys.path.insert(0, os.path.dirname(__file__))
from kq_content import *
from ko_hangul import *

REGION = 'Péninsule du Matin calme'

def KL(slug, title, objective, explanation, items, minutes=5):
    """Leçon d'écriture : uniquement des lettres, les questions sont générées."""
    return L(slug, title, objective, minutes, explanation, items, [], [])

# ═════════════════════════ Île 1 : les lettres du roi Sejong ═════════════════════════
W1 = WORLD('topik1-w1', ('Les lettres du roi Sejong', 'King Sejong’s letters'), REGION,
  ('Les voyelles et les consonnes de base du hangeul, l’alphabet inventé en 1443.', 'The basic vowels and consonants of Hangul, the alphabet invented in 1443.'),
  (('Le Dokkaebi farceur', 'The Prankster Dokkaebi'), '도', ('Ce lutin à massue magique mélange les lettres des enseignes. Lis-les juste et il te laissera passer… peut-être.', 'This goblin with a magic club scrambles the letters on every sign. Read them right and he will let you pass… perhaps.')),
  [CH('topik1-w1-c1', ('Voyelles', 'Vowels'), [
    KL('ko-vowels-1', ('Les voyelles ㅏ ㅓ ㅗ ㅜ ㅡ ㅣ', 'The vowels ㅏ ㅓ ㅗ ㅜ ㅡ ㅣ'), ('Lire et reconnaître les six voyelles de base.', 'Read and recognise the six basic vowels.'), [
      ('Le roi Sejong a fait créer le hangeul en 1443 pour que chacun puisse apprendre à lire « en une matinée ». Les voyelles reposent sur trois symboles : le ciel (un point, devenu un petit trait), la terre (ㅡ) et l’homme (ㅣ).', 'King Sejong had Hangul created in 1443 so that anyone could learn to read “in a single morning”. The vowels rest on three symbols: heaven (a dot, now a short stroke), earth (ㅡ) and man (ㅣ).'),
      ('ㅏ = a, ㅓ = eo (un « o » très ouvert, bouche détendue), ㅗ = o (lèvres arrondies), ㅜ = ou, ㅡ = eu (lèvres étirées, sans arrondir), ㅣ = i.', 'ㅏ = a, ㅓ = eo (a very open “o”, relaxed mouth), ㅗ = o (rounded lips), ㅜ = u, ㅡ = eu (lips spread, not rounded), ㅣ = i.'),
      ('Une voyelle ne s’écrit jamais seule : on la précède du rond ㅇ, qui est muet en début de syllabe. Écoute : 아, 어, 오, 우, 으, 이.', 'A vowel is never written alone: it is preceded by the circle ㅇ, which is silent at the start of a syllable. Listen: 아, 어, 오, 우, 으, 이.'),
    ], V_BASE),
    KL('ko-vowels-2', ('Les voyelles en y et ㅐ ㅔ', 'The “y” vowels and ㅐ ㅔ'), ('Reconnaître ㅑ ㅕ ㅛ ㅠ, puis ㅐ et ㅔ.', 'Recognise ㅑ ㅕ ㅛ ㅠ, then ㅐ and ㅔ.'), [
      ('Un trait de plus ajoute un son « y » : ㅏ → ㅑ (ya), ㅓ → ㅕ (yeo), ㅗ → ㅛ (yo), ㅜ → ㅠ (yu).', 'One extra stroke adds a “y” sound: ㅏ → ㅑ (ya), ㅓ → ㅕ (yeo), ㅗ → ㅛ (yo), ㅜ → ㅠ (yu).'),
      ('ㅐ (ae) et ㅔ (e) se prononcent aujourd’hui presque pareil, comme le « è » de « mère ». On les distingue à l’écrit : 개 (chien), 게 (crabe).', 'ㅐ (ae) and ㅔ (e) are pronounced almost the same today, like the “e” in “bed”. They are told apart in writing: 개 (dog), 게 (crab).'),
    ], V_Y + V_AE),
  ]),
  CH('topik1-w1-c2', ('Consonnes', 'Consonants'), [
    KL('ko-cons-1', ('Les consonnes ㄱ ㄴ ㄷ ㄹ ㅁ', 'The consonants ㄱ ㄴ ㄷ ㄹ ㅁ'), ('Lire les cinq premières consonnes de base.', 'Read the first five basic consonants.'), [
      ('Les consonnes dessinent la bouche : ㄱ montre la langue qui touche le fond du palais, ㄴ la langue contre les dents, ㅁ la forme des lèvres fermées.', 'The consonants draw the mouth: ㄱ shows the tongue touching the back of the palate, ㄴ the tongue against the teeth, ㅁ the shape of closed lips.'),
      ('ㄱ = g (k en fin de mot), ㄴ = n, ㄷ = d (t en fin de mot), ㄹ = r entre deux voyelles, l en fin de syllabe, ㅁ = m. Avec ㅏ : 가, 나, 다, 라, 마.', 'ㄱ = g (k at the end of a word), ㄴ = n, ㄷ = d (t at the end of a word), ㄹ = r between two vowels, l at the end of a syllable, ㅁ = m. With ㅏ: 가, 나, 다, 라, 마.'),
      ('La consonne se place à gauche d’une voyelle verticale (가) ou au-dessus d’une voyelle horizontale (고).', 'The consonant goes to the left of a vertical vowel (가) or above a horizontal vowel (고).'),
    ], C_BASE1),
    KL('ko-cons-2', ('Les consonnes ㅂ ㅅ ㅇ ㅈ ㅎ', 'The consonants ㅂ ㅅ ㅇ ㅈ ㅎ'), ('Lire les cinq autres consonnes de base.', 'Read the other five basic consonants.'), [
      ('ㅂ = b (p en fin de mot), ㅅ = s (sh devant ㅣ : 시), ㅈ = j, ㅎ = h.', 'ㅂ = b (p at the end of a word), ㅅ = s (sh before ㅣ: 시), ㅈ = j, ㅎ = h.'),
      ('ㅇ est muet en début de syllabe (아 = a) mais se prononce « ng » en fin de syllabe (강 = gang).', 'ㅇ is silent at the start of a syllable (아 = a) but is pronounced “ng” at the end of a syllable (강 = gang).'),
      ('Tu peux déjà lire : 바나나 (banane), 하마 (hippopotame), 나무 (arbre).', 'You can already read: 바나나 (banana), 하마 (hippo), 나무 (tree).'),
    ], C_BASE2),
  ])])

# ═════════════════════════ Île 2 : le palais des syllabes ═════════════════════════
W2 = WORLD('topik1-w2', ('Le palais des syllabes', 'The palace of syllables'), REGION,
  ('Consonnes aspirées et doubles, voyelles composées et consonnes finales (batchim).', 'Aspirated and double consonants, compound vowels and final consonants (batchim).'),
  (('Le Haetae du palais', 'The Palace Haetae'), '해', ('Le lion de pierre qui garde le palais Gyeongbokgung ne laisse entrer que ceux qui lisent chaque bloc sans hésiter.', 'The stone lion guarding Gyeongbokgung Palace lets in only those who read every block without hesitating.')),
  [CH('topik1-w2-c1', ('Consonnes fortes', 'Strong consonants'), [
    KL('ko-cons-3', ('Les aspirées ㅋ ㅌ ㅍ ㅊ', 'The aspirated consonants ㅋ ㅌ ㅍ ㅊ'), ('Distinguer les consonnes aspirées des consonnes simples.', 'Tell aspirated consonants apart from simple ones.'), [
      ('Un trait de plus ajoute un souffle : ㄱ → ㅋ, ㄷ → ㅌ, ㅂ → ㅍ, ㅈ → ㅊ. Place une main devant la bouche : avec 카, 타, 파, 차 tu sens l’air sortir.', 'One extra stroke adds a puff of air: ㄱ → ㅋ, ㄷ → ㅌ, ㅂ → ㅍ, ㅈ → ㅊ. Put a hand in front of your mouth: with 카, 타, 파, 차 you feel the air come out.'),
      ('Exemples : 커피 (café), 토마토 (tomate), 피자 (pizza), 차 (thé ; voiture).', 'Examples: 커피 (coffee), 토마토 (tomato), 피자 (pizza), 차 (tea; car).'),
    ], C_ASP),
    KL('ko-cons-4', ('Les doubles ㄲ ㄸ ㅃ ㅆ ㅉ', 'The double consonants ㄲ ㄸ ㅃ ㅆ ㅉ'), ('Reconnaître les consonnes tendues.', 'Recognise the tense consonants.'), [
      ('Doubler la lettre rend le son tendu, sans souffle, la gorge serrée : 가 / 까, 다 / 따, 바 / 빠, 사 / 싸, 자 / 짜.', 'Doubling the letter makes the sound tense, with no puff of air and a tight throat: 가 / 까, 다 / 따, 바 / 빠, 사 / 싸, 자 / 짜.'),
      ('Trois sons proches à bien distinguer : 가 (simple), 카 (aspiré), 까 (tendu). 비싸요 (c’est cher) contient ㅆ.', 'Three close sounds to tell apart: 가 (plain), 카 (aspirated), 까 (tense). 비싸요 (it’s expensive) contains ㅆ.'),
    ], C_TENSE),
  ]),
  CH('topik1-w2-c2', ('Voyelles composées et batchim', 'Compound vowels and batchim'), [
    KL('ko-vowels-3', ('ㅒ ㅖ et les voyelles en w (1)', 'ㅒ ㅖ and the “w” vowels (1)'), ('Lire ㅒ, ㅖ, ㅘ, ㅙ et ㅚ.', 'Read ㅒ, ㅖ, ㅘ, ㅙ and ㅚ.'), [
      ('ㅒ (yae) et ㅖ (ye) sont les versions en « y » de ㅐ et ㅔ : 얘기 (histoire), 예 (oui, poli).', 'ㅒ (yae) and ㅖ (ye) are the “y” versions of ㅐ and ㅔ: 얘기 (story), 예 (yes, polite).'),
      ('ㅗ + ㅏ = ㅘ (wa), ㅗ + ㅐ = ㅙ (wae), ㅗ + ㅣ = ㅚ (oe, prononcé « wé »). 사과 (pomme), 왜 (pourquoi), 회사 (entreprise).', 'ㅗ + ㅏ = ㅘ (wa), ㅗ + ㅐ = ㅙ (wae), ㅗ + ㅣ = ㅚ (oe, pronounced “we”). 사과 (apple), 왜 (why), 회사 (company).'),
    ], V_YAE + V_W1),
    KL('ko-vowels-4', ('Les voyelles en w (2) et ㅢ', 'The “w” vowels (2) and ㅢ'), ('Lire ㅝ, ㅞ, ㅟ et ㅢ.', 'Read ㅝ, ㅞ, ㅟ and ㅢ.'), [
      ('ㅜ + ㅓ = ㅝ (wo), ㅜ + ㅔ = ㅞ (we), ㅜ + ㅣ = ㅟ (wi). 뭐 (quoi), 귀 (oreille).', 'ㅜ + ㅓ = ㅝ (wo), ㅜ + ㅔ = ㅞ (we), ㅜ + ㅣ = ㅟ (wi). 뭐 (what), 귀 (ear).'),
      ('ㅡ + ㅣ = ㅢ (ui) : 의사 (médecin). Comme particule (의 = de), on la prononce souvent « é ».', 'ㅡ + ㅣ = ㅢ (ui): 의사 (doctor). As a particle (의 = of), it is often pronounced “e”.'),
    ], V_W2),
    KL('ko-batchim', ('Les consonnes finales (batchim)', 'Final consonants (batchim)'), ('Lire une syllabe avec une consonne finale.', 'Read a syllable with a final consonant.'), [
      ('Une syllabe peut se terminer par une consonne, écrite en bas du bloc : c’est le batchim (받침). 가 + ㄱ = 각.', 'A syllable can end with a consonant, written at the bottom of the block: this is the batchim (받침). 가 + ㄱ = 각.'),
      ('En finale, il n’existe que sept sons : k (각), n (안), t (옷 : le ㅅ final se dit t), l (말), m (밤), p (밥), ng (강).', 'At the end of a syllable there are only seven sounds: k (각), n (안), t (옷: a final ㅅ is said t), l (말), m (밤), p (밥), ng (강).'),
      ('Devant une voyelle, le batchim glisse sur la syllabe suivante : 한국어 se dit « han-gu-geo ».', 'Before a vowel, the batchim slides onto the next syllable: 한국어 is said “han-gu-geo”.'),
    ], BATCHIM, minutes=6),
  ])])

# ═════════════════════════ Île 3 : se présenter à Séoul ═════════════════════════
INTRO = ('Présente-toi.', 'Introduce yourself.')
W3 = WORLD('topik1-w3', ('Se présenter à Séoul', 'Introducing yourself in Seoul'), REGION,
  ('Saluer, dire son nom, sa nationalité et son métier, et dire ce que n’est pas une chose.', 'Greet people, give your name, nationality and job, and say what something is not.'),
  (('La Gumiho masquée', 'The Masked Gumiho'), '호', ('La renarde à neuf queues prend l’apparence des passants de Myeongdong. Présente-toi sans faute pour la démasquer !', 'The nine-tailed fox takes on the faces of passers-by in Myeongdong. Introduce yourself without a mistake to unmask her!')),
  [CH('topik1-w3-c1', ('Premières rencontres', 'First meetings'), [
    L('ko-intro', ('Bonjour, je suis… : -이에요/예요', 'Hello, I am…: -이에요/예요'), ('Saluer et dire qui l’on est avec -이에요/예요.', 'Greet someone and say who you are with -이에요/예요.'), 8, [
        ('안녕하세요 (annyeonghaseyo) est le bonjour poli de tous les jours, à toute heure.', '안녕하세요 (annyeonghaseyo) is the everyday polite hello, at any time of day.'),
        ('Nom + 이에요 après une consonne finale : 학생이에요 (je suis étudiant). Nom + 예요 après une voyelle : 의사예요 (je suis médecin).', 'Noun + 이에요 after a final consonant: 학생이에요 (I am a student). Noun + 예요 after a vowel: 의사예요 (I am a doctor).'),
        ('Le sujet « je » est souvent sous-entendu. 네 = oui, 아니요 = non.', 'The subject “I” is often left out. 네 = yes, 아니요 = no.'),
      ], [
        G('gram-ko-ieyo', '-이에요/예요', None, '-ieyo / -yeyo', ('être (poli) : je suis…, c’est…', 'to be (polite): I am…, it is…')),
        V('ko-annyeonghaseyo', '안녕하세요', None, 'annyeonghaseyo', ('bonjour (poli)', 'hello (polite)')),
        V('ko-jeo', '저', None, 'jeo', ('je, moi (humble)', 'I, me (humble)')),
        V('ko-ireum', '이름', None, 'ireum', ('nom, prénom', 'name')),
        V('ko-ne', '네', None, 'ne', ('oui', 'yes')),
        V('ko-aniyo', '아니요', None, 'aniyo', ('non', 'no')),
        V('ko-haksaeng', '학생', None, 'haksaeng', ('étudiant, élève', 'student, pupil')),
        V('ko-uisa', '의사', None, 'uisa', ('médecin', 'doctor')),
      ], [
        ex('안녕하세요. 저는 민지예요.', None, 'Bonjour. Je suis Minji.', 'Hello. I am Minji.'),
        ex('학생이에요? — 네, 학생이에요.', None, 'Tu es étudiant ? — Oui, je suis étudiant.', 'Are you a student? — Yes, I am a student.'),
      ], [
        FB(COMPLETE, '저는 학생＿.', ['이에요', '예요'], '이에요', ('학생 finit par une consonne (ㅇ) : 이에요.', '학생 ends with a consonant (ㅇ): 이에요.'), ('Je suis étudiant.', 'I am a student.')),
        FB(COMPLETE, '저는 의사＿.', ['이에요', '예요'], '예요', ('의사 finit par une voyelle : 예요.', '의사 ends with a vowel: 예요.'), ('Je suis médecin.', 'I am a doctor.')),
        DC(('Quelqu’un te salue. Que réponds-tu ?', 'Someone greets you. What do you answer?'), [('민지', '안녕하세요!')], ('Minji te dit bonjour.', 'Minji says hello to you.'), ['안녕하세요!', '아니요.', '의사예요.'], '안녕하세요!', ('On répond au salut par le même salut.', 'You answer a greeting with the same greeting.')),
        TF('저는 학생이에요.', ('La personne dit qu’elle est médecin.', 'The speaker says they are a doctor.'), FAUX, ('학생 = étudiant ; médecin se dit 의사.', '학생 = student; doctor is 의사.')),
      ]),
    L('ko-topic', ('Thème et style formel : 은/는, 입니다', 'Topic and formal style: 은/는, 입니다'), ('Présenter un thème avec 은/는 et parler en style formel.', 'Introduce a topic with 은/는 and speak in formal style.'), 9, [
        ('은/는 marque le thème de la phrase (« quant à… ») : 은 après une consonne (이름은), 는 après une voyelle (저는).', '은/는 marks the topic of the sentence (“as for…”): 은 after a consonant (이름은), 는 after a vowel (저는).'),
        ('입니다 est la version formelle de 이에요/예요, utilisée dans les présentations officielles, au travail et aux informations. Question : 입니까?', '입니다 is the formal version of 이에요/예요, used in official introductions, at work and on the news. Question: 입니까?'),
        ('Nationalité = pays + 사람 : 한국 사람 (Coréen), 프랑스 사람 (Français).', 'Nationality = country + 사람: 한국 사람 (Korean), 프랑스 사람 (French).'),
      ], [
        G('gram-ko-eun-neun', '은/는', None, 'eun / neun', ('particule du thème (quant à…)', 'topic particle (as for…)')),
        G('gram-ko-imnida', '입니다', None, 'imnida', ('être (style formel)', 'to be (formal style)')),
        V('ko-hanguk', '한국', None, 'hanguk', ('la Corée', 'Korea')),
        V('ko-saram', '사람', None, 'saram', ('personne, gens', 'person, people')),
        V('ko-peurangseu', '프랑스', None, 'peurangseu', ('la France', 'France')),
        V('ko-hoesawon', '회사원', None, 'hoesawon', ('employé de bureau', 'office worker')),
        V('ko-seonsaengnim', '선생님', None, 'seonsaengnim', ('professeur (terme respectueux)', 'teacher (respectful term)')),
      ], [
        ex('제 이름은 레아입니다. 프랑스 사람입니다.', None, 'Je m’appelle Léa. Je suis française.', 'My name is Léa. I am French.'),
        ex('김 선생님은 한국 사람이에요.', None, 'Le professeur Kim est coréen.', 'Mr Kim, the teacher, is Korean.'),
      ], [
        PC(CHOOSE, '저＿ 회사원이에요.', ['는', '은'], '는', ('저 finit par une voyelle : 는.', '저 ends with a vowel: 는.'), ('Moi, je suis employé de bureau.', 'As for me, I am an office worker.')),
        PC(CHOOSE, '이름＿ 뭐예요?', ['은', '는'], '은', ('이름 finit par une consonne (ㅁ) : 은.', '이름 ends with a consonant (ㅁ): 은.'), ('Comment tu t’appelles ? (Ton nom, c’est quoi ?)', 'What is your name?')),
        FB(COMPLETE, '저는 프랑스 사람＿.', ['입니다', '입니까'], '입니다', ('Affirmation formelle : 입니다 ; 입니까 sert à poser une question.', 'Formal statement: 입니다; 입니까 is used to ask a question.'), ('Je suis français.', 'I am French.')),
        SO(('Remets dans l’ordre : « Je suis coréen. »', 'Put in order: “I am Korean.”'), ['저는', '한국', '사람이에요.'], ('Thème + nom + 이에요.', 'Topic + noun + 이에요.')),
      ]),
    L('ko-not-noun', ('Ce n’est pas… : 이/가 아니에요', 'It is not…: 이/가 아니에요'), ('Nier avec 이/가 아니에요 et demander ce qu’est une chose.', 'Negate with 이/가 아니에요 and ask what something is.'), 8, [
        ('Nom + 이/가 아니에요 = ce n’est pas… : 학생이 아니에요, 의사가 아니에요 (이 après consonne, 가 après voyelle).', 'Noun + 이/가 아니에요 = it is not…: 학생이 아니에요, 의사가 아니에요 (이 after a consonant, 가 after a vowel).'),
        ('이거 (ceci, près de moi), 그거 (cela, près de toi), 저거 (cela, là-bas). 뭐예요? = qu’est-ce que c’est ?', '이거 (this, near me), 그거 (that, near you), 저거 (that, over there). 뭐예요? = what is it?'),
      ], [
        G('gram-ko-anieyo', '이/가 아니에요', None, 'i / ga anieyo', ('ce n’est pas…, je ne suis pas…', 'it is not…, I am not…')),
        V('ko-igeo', '이거', None, 'igeo', ('ceci (près de moi)', 'this (near me)')),
        V('ko-geugeo', '그거', None, 'geugeo', ('cela (près de toi)', 'that (near you)')),
        V('ko-mwo', '뭐', None, 'mwo', ('quoi', 'what')),
        V('ko-chaek', '책', None, 'chaek', ('livre', 'book')),
        V('ko-gabang', '가방', None, 'gabang', ('sac', 'bag')),
        V('ko-uyu', '우유', None, 'uyu', ('lait', 'milk')),
      ], [
        ex('이거 뭐예요? — 책이에요.', None, 'Qu’est-ce que c’est ? — C’est un livre.', 'What is this? — It’s a book.'),
        ex('그거 제 가방이 아니에요.', None, 'Ce n’est pas mon sac.', 'That is not my bag.'),
      ], [
        PC(CHOOSE, '저는 의사＿ 아니에요.', ['가', '이'], '가', ('의사 finit par une voyelle : 가 아니에요.', '의사 ends with a vowel: 가 아니에요.'), ('Je ne suis pas médecin.', 'I am not a doctor.')),
        PC(CHOOSE, '이거 책＿ 아니에요.', ['이', '가'], '이', ('책 finit par une consonne : 이 아니에요.', '책 ends with a consonant: 이 아니에요.'), ('Ce n’est pas un livre.', 'This is not a book.')),
        DC(('On te montre un objet en te demandant ce que c’est.', 'Someone shows you an object and asks what it is.'), [('준호', '이거 뭐예요?')], ('Junho te demande ce que c’est.', 'Junho asks you what it is.'), ['우유예요.', '안녕하세요.', '네, 학생이에요.'], '우유예요.', ('À 뭐예요?, on répond avec un nom + 예요/이에요.', 'You answer 뭐예요? with a noun + 예요/이에요.')),
        TF('그거 가방이 아니에요. 책이에요.', ('L’objet est un livre.', 'The object is a book.'), VRAI, ('가방이 아니에요 = ce n’est pas un sac ; 책이에요 = c’est un livre.', '가방이 아니에요 = it is not a bag; 책이에요 = it is a book.')),
      ]),
  ])])

# ═════════════════════════ Île 4 : le marché de Namdaemun ═════════════════════════
W4 = WORLD('topik1-w4', ('Le marché de Namdaemun', 'Namdaemun Market'), REGION,
  ('Les deux séries de nombres, les prix en wons, les compteurs et l’heure.', 'The two sets of numbers, prices in won, counters and telling the time.'),
  (('Le Tigre et le kaki séché', 'The Tiger and the Dried Persimmon'), '범', ('Le tigre du conte ne craint qu’une chose : le kaki séché. Compte juste chaque pièce du marché, ou il bondit !', 'The tiger in the tale fears only one thing: the dried persimmon. Count every coin at the market correctly, or he pounces!')),
  [CH('topik1-w4-c1', ('Compter en sino-coréen', 'Counting in Sino-Korean'), [
    L('ko-sino-1', ('Les nombres sino-coréens 1 à 10', 'Sino-Korean numbers 1 to 10'), ('Compter de 1 à 10 avec les nombres d’origine chinoise.', 'Count from 1 to 10 with the numbers of Chinese origin.'), 7, [
        ('Le coréen a deux séries de nombres. Les nombres sino-coréens servent pour les prix, les dates, les numéros de téléphone et les minutes.', 'Korean has two sets of numbers. Sino-Korean numbers are used for prices, dates, phone numbers and minutes.'),
        ('일 1, 이 2, 삼 3, 사 4, 오 5, 육 6, 칠 7, 팔 8, 구 9, 십 10. Ensuite on combine : 십일 11, 이십 20, 이십오 25.', '일 1, 이 2, 삼 3, 사 4, 오 5, 육 6, 칠 7, 팔 8, 구 9, 십 10. Then you combine them: 십일 11, 이십 20, 이십오 25.'),
      ], [
        V('ko-il', '일', None, 'il', ('un (sino-coréen)', 'one (Sino-Korean)')),
        V('ko-i2', '이', None, 'i', ('deux (sino-coréen)', 'two (Sino-Korean)')),
        V('ko-sam', '삼', None, 'sam', ('trois (sino-coréen)', 'three (Sino-Korean)')),
        V('ko-sa', '사', None, 'sa', ('quatre (sino-coréen)', 'four (Sino-Korean)')),
        V('ko-o', '오', None, 'o', ('cinq (sino-coréen)', 'five (Sino-Korean)')),
        V('ko-yuk', '육', None, 'yuk', ('six (sino-coréen)', 'six (Sino-Korean)')),
        V('ko-chil', '칠', None, 'chil', ('sept (sino-coréen)', 'seven (Sino-Korean)')),
        V('ko-pal', '팔', None, 'pal', ('huit (sino-coréen)', 'eight (Sino-Korean)')),
        V('ko-gu', '구', None, 'gu', ('neuf (sino-coréen)', 'nine (Sino-Korean)')),
        V('ko-sip', '십', None, 'sip', ('dix (sino-coréen)', 'ten (Sino-Korean)')),
      ], [
        ex('제 전화번호는 공일공 사오육칠 팔구일이예요.', None, 'Mon numéro de téléphone est le 010 4567 8912.', 'My phone number is 010 4567 8912.'),
        ex('이십오 번 버스를 타요.', None, 'Je prends le bus numéro 25.', 'I take bus number 25.'),
      ], [
        FB(('Combien font 3 + 4 ?', 'What is 3 + 4?'), '삼 더하기 사는 ＿이에요.', ['칠', '팔', '육'], '칠', ('3 + 4 = 7 : 칠.', '3 + 4 = 7: 칠.'), ('Trois plus quatre font sept.', 'Three plus four is seven.')),
        FB(('Écris 20 en sino-coréen.', 'Write 20 in Sino-Korean.'), '스물은 숫자로 20, 한자어로는 ＿이에요.', ['이십', '십이', '이백'], '이십', ('2 × 10 : 이 + 십 = 이십 ; 십이 = 12.', '2 × 10: 이 + 십 = 이십; 십이 = 12.'), ('Vingt se dit 이십 en sino-coréen.', 'Twenty is 이십 in Sino-Korean.')),
        TF('구 더하기 일은 십이에요.', ('9 + 1 = 10.', '9 + 1 = 10.'), VRAI, ('구 (9) + 일 (1) = 십 (10).', '구 (9) + 일 (1) = 십 (10).')),
        SO(('Remets dans l’ordre : « Je prends le bus 25. »', 'Put in order: “I take bus 25.”'), ['이십오', '번', '버스를', '타요.'], ('Numéro + 번 + nom + 을/를 + verbe.', 'Number + 번 + noun + 을/를 + verb.')),
      ]),
    L('ko-price', ('Combien ça coûte ? : 얼마예요?', 'How much is it?: 얼마예요?'), ('Demander un prix et compter en centaines, milliers et dizaines de milliers de wons.', 'Ask a price and count in hundreds, thousands and tens of thousands of won.'), 9, [
        ('백 = 100, 천 = 1 000, 만 = 10 000. On ne dit pas « un » devant : 천 원 (1 000 wons), 만 원 (10 000 wons).', '백 = 100, 천 = 1,000, 만 = 10,000. You don’t say “one” in front: 천 원 (1,000 won), 만 원 (10,000 won).'),
        ('Attention : le coréen compte par 10 000. 50 000 = 오만, 15 000 = 만오천.', 'Careful: Korean counts in units of 10,000. 50,000 = 오만, 15,000 = 만오천.'),
        ('얼마예요? = combien ça coûte ? 이거 얼마예요? — 오천 원이에요.', '얼마예요? = how much is it? 이거 얼마예요? — 오천 원이에요.'),
      ], [
        G('gram-ko-eolmayeyo', '얼마예요?', None, 'eolmayeyo?', ('combien ça coûte ?', 'how much is it?')),
        V('ko-baek', '백', None, 'baek', ('cent', 'hundred')),
        V('ko-cheon', '천', None, 'cheon', ('mille', 'thousand')),
        V('ko-man', '만', None, 'man', ('dix mille', 'ten thousand')),
        V('ko-won', '원', None, 'won', ('won (monnaie coréenne)', 'won (Korean currency)')),
        V('ko-bissada', '비싸다', None, 'bissada', ('être cher', 'to be expensive')),
        V('ko-ssada', '싸다', None, 'ssada', ('être bon marché', 'to be cheap')),
      ], [
        ex('이 사과 얼마예요? — 천오백 원이에요.', None, 'Combien coûte cette pomme ? — 1 500 wons.', 'How much is this apple? — It’s 1,500 won.'),
        ex('와, 비싸요! 좀 깎아 주세요.', None, 'Ouah, c’est cher ! Faites-moi un petit prix, s’il vous plaît.', 'Wow, that’s expensive! Please give me a discount.'),
      ], [
        FB(('Lis le prix : 3 000 ₩', 'Read the price: ₩3,000'), '이 우유는 ＿ 원이에요.', ['삼천', '삼백', '삼만'], '삼천', ('3 000 = 삼 + 천.', '3,000 = 삼 + 천.'), ('Ce lait coûte 3 000 wons.', 'This milk costs 3,000 won.')),
        FB(('Lis le prix : 20 000 ₩', 'Read the price: ₩20,000'), '가방은 ＿ 원이에요.', ['이만', '이천', '이십만'], '이만', ('20 000 = 2 × 10 000 = 이만.', '20,000 = 2 × 10,000 = 이만.'), ('Le sac coûte 20 000 wons.', 'The bag costs 20,000 won.')),
        DC(('Au marché, tu veux connaître le prix.', 'At the market, you want to know the price.'), [('손님', '이거 얼마예요?'), ('점원', '만 원이에요.')], ('Le vendeur dit 10 000 wons. Tu trouves que c’est cher.', 'The seller says 10,000 won. You think it is expensive.'), ['비싸요.', '싸요.', '얼마예요?'], '비싸요.', ('비싸요 = c’est cher ; 싸요 = ce n’est pas cher.', '비싸요 = it’s expensive; 싸요 = it’s cheap.')),
        TF('만오천 원은 15,000원이에요.', ('만오천 = 15 000.', '만오천 = 15,000.'), VRAI, ('만 (10 000) + 오천 (5 000) = 15 000.', '만 (10,000) + 오천 (5,000) = 15,000.')),
      ]),
  ]),
  CH('topik1-w4-c2', ('Compter en coréen natif', 'Counting in native Korean'), [
    L('ko-native', ('Les nombres natifs et les compteurs', 'Native numbers and counters'), ('Compter les objets et les personnes avec 하나, 둘, 셋 et les compteurs 개, 명.', 'Count objects and people with 하나, 둘, 셋 and the counters 개, 명.'), 9, [
        ('Les nombres coréens natifs servent à compter les choses, les personnes, l’âge et les heures : 하나 1, 둘 2, 셋 3, 넷 4, 다섯 5.', 'Native Korean numbers are used to count things, people, age and hours: 하나 1, 둘 2, 셋 3, 넷 4, 다섯 5.'),
        ('Devant un compteur, 1 à 4 raccourcissent : 한 개, 두 개, 세 개, 네 개, mais 다섯 개.', 'Before a counter, 1 to 4 get shorter: 한 개, 두 개, 세 개, 네 개, but 다섯 개.'),
        ('개 compte les objets, 명 les personnes, 살 les années d’âge : 사과 두 개, 학생 세 명, 스무 살.', '개 counts objects, 명 people, 살 years of age: 사과 두 개, 학생 세 명, 스무 살.'),
      ], [
        G('gram-ko-counter', '한 개, 두 명', None, 'han gae, du myeong', ('compter avec un nombre natif et un compteur', 'counting with a native number and a counter')),
        V('ko-hana', '하나', None, 'hana', ('un (coréen natif)', 'one (native Korean)')),
        V('ko-dul', '둘', None, 'dul', ('deux (coréen natif)', 'two (native Korean)')),
        V('ko-set', '셋', None, 'set', ('trois (coréen natif)', 'three (native Korean)')),
        V('ko-net', '넷', None, 'net', ('quatre (coréen natif)', 'four (native Korean)')),
        V('ko-daseot', '다섯', None, 'daseot', ('cinq (coréen natif)', 'five (native Korean)')),
        V('ko-gae', '개', None, 'gae', ('compteur des objets', 'counter for objects')),
        V('ko-myeong', '명', None, 'myeong', ('compteur de personnes', 'counter for people')),
        V('ko-sagwa', '사과', None, 'sagwa', ('pomme', 'apple')),
      ], [
        ex('사과 세 개 주세요.', None, 'Trois pommes, s’il vous plaît.', 'Three apples, please.'),
        ex('우리 반에 학생이 다섯 명 있어요.', None, 'Il y a cinq élèves dans notre classe.', 'There are five students in our class.'),
      ], [
        FB(CHOOSE, '사과 ＿ 개 주세요. (2)', ['두', '둘', '이'], '두', ('Devant un compteur, 둘 devient 두.', 'Before a counter, 둘 becomes 두.'), ('Deux pommes, s’il vous plaît.', 'Two apples, please.')),
        FB(CHOOSE, '친구가 세 ＿ 와요.', ['명', '개', '원'], '명', ('On compte les personnes avec 명.', 'People are counted with 명.'), ('Trois amis viennent.', 'Three friends are coming.')),
        FB(CHOOSE, '가방이 ＿ 개 있어요. (1)', ['한', '하나', '일'], '한', ('Devant un compteur, 하나 devient 한.', 'Before a counter, 하나 becomes 한.'), ('Il y a un sac.', 'There is one bag.')),
        TF('학생 네 명', ('Il s’agit de quatre étudiants.', 'This means four students.'), VRAI, ('네 (4, devant un compteur) + 명 (personnes).', '네 (4, before a counter) + 명 (people).')),
      ]),
    L('ko-time', ('L’heure : 시, 분', 'Telling the time: 시, 분'), ('Dire et demander l’heure.', 'Say and ask the time.'), 8, [
        ('Les heures se comptent en coréen natif (한 시, 두 시, 세 시…) et les minutes en sino-coréen (십 분, 삼십 분).', 'Hours are counted in native Korean (한 시, 두 시, 세 시…) and minutes in Sino-Korean (십 분, 삼십 분).'),
        ('반 = et demie : 두 시 반 = 2 h 30. 몇 시예요? = quelle heure est-il ?', '반 = half past: 두 시 반 = 2:30. 몇 시예요? = what time is it?'),
        ('오전 = le matin (a.m.), 오후 = l’après-midi (p.m.).', '오전 = morning (a.m.), 오후 = afternoon (p.m.).'),
      ], [
        G('gram-ko-si-bun', '…시 …분', None, '…si …bun', ('… heures … minutes', '… o’clock … minutes')),
        V('ko-si', '시', None, 'si', ('heure (sur l’horloge)', 'o’clock, hour')),
        V('ko-bun', '분', None, 'bun', ('minute', 'minute')),
        V('ko-myeot', '몇', None, 'myeot', ('combien, quel (nombre)', 'how many, what (number)')),
        V('ko-jigeum', '지금', None, 'jigeum', ('maintenant', 'now')),
        V('ko-ban', '반', None, 'ban', ('moitié ; et demie', 'half; half past')),
        V('ko-ohu', '오후', None, 'ohu', ('l’après-midi (après midi)', 'afternoon (p.m.)')),
      ], [
        ex('지금 몇 시예요? — 세 시 십 분이에요.', None, 'Quelle heure est-il ? — 3 h 10.', 'What time is it now? — It’s ten past three.'),
        ex('오후 한 시 반에 만나요.', None, 'On se voit à 13 h 30.', 'Let’s meet at 1:30 p.m.'),
      ], [
        FB(('Lis l’heure : 2 h 00', 'Read the time: 2:00'), '지금 ＿ 시예요.', ['두', '이', '둘'], '두', ('Heures en coréen natif : 두 시.', 'Hours in native Korean: 두 시.'), ('Il est 2 heures.', 'It is two o’clock.')),
        FB(('Lis l’heure : 4 h 30', 'Read the time: 4:30'), '네 시 ＿이에요.', ['반', '삼십', '셋'], '반', ('30 minutes = 반 (on peut aussi dire 삼십 분).', '30 minutes = 반 (you can also say 삼십 분).'), ('Il est 4 h 30.', 'It is half past four.')),
        DC(('Un passant te demande l’heure. Il est 9 h.', 'A passer-by asks you the time. It is 9 o’clock.'), [('행인', '실례지만, 지금 몇 시예요?')], ('Un passant te demande l’heure.', 'A passer-by asks you the time.'), ['아홉 시예요.', '구 시예요.', '아홉 분이에요.'], '아홉 시예요.', ('Heures en coréen natif : 아홉 시.', 'Hours in native Korean: 아홉 시.')),
        TF('세 시 이십 분', ('Il est 3 h 20.', 'It is 3:20.'), VRAI, ('세 시 = 3 h, 이십 분 = 20 minutes.', '세 시 = 3 o’clock, 이십 분 = 20 minutes.')),
      ]),
  ])])

# ═════════════════════════ Île 5 : une journée au hanok ═════════════════════════
W5 = WORLD('topik1-w5', ('Une journée au hanok', 'A day in the hanok'), REGION,
  ('Conjuguer les verbes au présent poli, dire ce qu’on fait et où on le fait.', 'Conjugate verbs in the polite present, say what you do and where you do it.'),
  (('L’Imugi du puits', 'The Imugi of the Well'), '무', ('Ce serpent rêve de devenir dragon. Il lui manque la perle des verbes : conjugue-les tous sans faute et il s’envolera enfin.', 'This serpent dreams of becoming a dragon. It lacks the pearl of verbs: conjugate them all correctly and it will finally fly away.')),
  [CH('topik1-w5-c1', ('Le présent poli', 'The polite present'), [
    L('ko-ayo', ('Le présent poli : -아요/-어요', 'The polite present: -아요/-어요'), ('Conjuguer un verbe au présent poli.', 'Conjugate a verb in the polite present.'), 10, [
        ('Un verbe au dictionnaire finit par 다 : 가다 (aller). On enlève 다 pour obtenir le radical (가), puis on ajoute la terminaison.', 'A dictionary verb ends in 다: 가다 (to go). Remove 다 to get the stem (가), then add the ending.'),
        ('Si la dernière voyelle du radical est ㅏ ou ㅗ : -아요 (가 + 아요 → 가요, 오 + 아요 → 와요, 보 + 아요 → 봐요). Sinon : -어요 (먹 + 어요 → 먹어요, 마시 + 어요 → 마셔요).', 'If the stem’s last vowel is ㅏ or ㅗ: -아요 (가 + 아요 → 가요, 오 + 아요 → 와요, 보 + 아요 → 봐요). Otherwise: -어요 (먹 + 어요 → 먹어요, 마시 + 어요 → 마셔요).'),
        ('La même forme sert à affirmer et à demander : 가요. (j’y vais) / 가요? (tu y vas ?). C’est le style poli de la conversation.', 'The same form is used to state and to ask: 가요. (I’m going) / 가요? (are you going?). This is the polite conversational style.'),
      ], [
        G('gram-ko-ayo-eoyo', '-아요/-어요', None, '-ayo / -eoyo', ('présent poli des verbes', 'polite present of verbs')),
        V('ko-gada', '가다', None, 'gada', ('aller', 'to go')),
        V('ko-oda', '오다', None, 'oda', ('venir', 'to come')),
        V('ko-meokda', '먹다', None, 'meokda', ('manger', 'to eat')),
        V('ko-masida', '마시다', None, 'masida', ('boire', 'to drink')),
        V('ko-boda', '보다', None, 'boda', ('voir, regarder', 'to see, to watch')),
        V('ko-ikda', '읽다', None, 'ikda', ('lire', 'to read')),
      ], [
        ex('저는 매일 아침 커피를 마셔요.', None, 'Je bois du café tous les matins.', 'I drink coffee every morning.'),
        ex('민지 씨, 지금 뭐 봐요? — 드라마를 봐요.', None, 'Minji, qu’est-ce que tu regardes ? — Je regarde un drama.', 'Minji, what are you watching? — I’m watching a drama.'),
      ], [
        FB(CHOOSE, '저는 빵을 ＿.', ['먹어요', '먹아요', '먹요'], '먹어요', ('먹 : la voyelle est ㅓ → -어요.', '먹: the vowel is ㅓ → -어요.'), ('Je mange du pain.', 'I eat bread.')),
        FB(CHOOSE, '친구가 집에 ＿.', ['와요', '오어요', '와어요'], '와요', ('오 + 아요 se contracte en 와요.', '오 + 아요 contracts to 와요.'), ('Mon ami vient à la maison.', 'My friend is coming to my house.')),
        FB(CHOOSE, '물을 ＿.', ['마셔요', '마시요', '마사요'], '마셔요', ('마시 + 어요 se contracte en 마셔요.', '마시 + 어요 contracts to 마셔요.'), ('Je bois de l’eau.', 'I drink water.')),
        SO(('Remets dans l’ordre : « Je lis un livre. »', 'Put in order: “I read a book.”'), ['저는', '책을', '읽어요.'], ('Sujet + complément + verbe : le verbe est toujours à la fin.', 'Subject + object + verb: the verb always comes last.')),
      ]),
    L('ko-haeyo', ('Les verbes en 하다 et l’objet 을/를', '하다 verbs and the object marker 을/를'), ('Conjuguer les verbes en 하다 et marquer l’objet avec 을/를.', 'Conjugate 하다 verbs and mark the object with 을/를.'), 9, [
        ('Tous les verbes en 하다 deviennent 해요 : 공부하다 → 공부해요, 일하다 → 일해요, 운동하다 → 운동해요.', 'All 하다 verbs become 해요: 공부하다 → 공부해요, 일하다 → 일해요, 운동하다 → 운동해요.'),
        ('을/를 marque l’objet direct : 을 après une consonne (밥을), 를 après une voyelle (커피를).', '을/를 marks the direct object: 을 after a consonant (밥을), 를 after a vowel (커피를).'),
        ('On peut aussi dire 한국어를 공부해요 : l’objet + 공부해요.', 'You can also say 한국어를 공부해요: object + 공부해요.'),
      ], [
        G('gram-ko-haeyo', '하다 → 해요', None, 'hada → haeyo', ('présent poli des verbes en 하다', 'polite present of 하다 verbs')),
        G('gram-ko-eul-reul', '을/를', None, 'eul / reul', ('particule de l’objet direct', 'direct object particle')),
        V('ko-gongbuhada', '공부하다', None, 'gongbuhada', ('étudier', 'to study')),
        V('ko-ilhada', '일하다', None, 'ilhada', ('travailler', 'to work')),
        V('ko-undonghada', '운동하다', None, 'undonghada', ('faire du sport', 'to exercise')),
        V('ko-bap', '밥', None, 'bap', ('riz cuit ; repas', 'cooked rice; meal')),
        V('ko-mul', '물', None, 'mul', ('eau', 'water')),
        V('ko-hangugeo', '한국어', None, 'hangugeo', ('la langue coréenne', 'the Korean language')),
      ], [
        ex('저는 도서관에서 한국어를 공부해요.', None, 'J’étudie le coréen à la bibliothèque.', 'I study Korean at the library.'),
        ex('아버지는 은행에서 일해요.', None, 'Mon père travaille dans une banque.', 'My father works at a bank.'),
      ], [
        PC(CHOOSE, '밥＿ 먹어요.', ['을', '를'], '을', ('밥 finit par une consonne : 을.', '밥 ends with a consonant: 을.'), ('Je mange (du riz).', 'I eat (rice).')),
        PC(CHOOSE, '커피＿ 마셔요.', ['를', '을'], '를', ('커피 finit par une voyelle : 를.', '커피 ends with a vowel: 를.'), ('Je bois du café.', 'I drink coffee.')),
        FB(CHOOSE, '저는 매일 운동＿.', ['해요', '하요', '했요'], '해요', ('하다 → 해요.', '하다 → 해요.'), ('Je fais du sport tous les jours.', 'I exercise every day.')),
        TF('저는 회사에서 일해요.', ('La personne étudie à l’école.', 'The speaker studies at school.'), FAUX, ('일해요 = je travaille ; 회사 = entreprise.', '일해요 = I work; 회사 = company.')),
      ]),
    L('ko-place', ('Où ? : 에, 에서, 있어요/없어요', 'Where?: 에, 에서, 있어요/없어요'), ('Dire où l’on va, où l’on fait quelque chose, et ce qu’il y a ou n’y a pas.', 'Say where you are going, where you do something, and what there is or isn’t.'), 10, [
        ('에 marque la destination et le lieu où l’on se trouve : 학교에 가요 (je vais à l’école), 집에 있어요 (je suis à la maison). Il marque aussi le moment : 세 시에.', '에 marks the destination and where something is: 학교에 가요 (I go to school), 집에 있어요 (I am at home). It also marks time: 세 시에.'),
        ('에서 marque le lieu où se déroule l’action : 식당에서 먹어요 (je mange au restaurant).', '에서 marks where an action takes place: 식당에서 먹어요 (I eat at the restaurant).'),
        ('있어요 = il y a, j’ai ; 없어요 = il n’y a pas, je n’ai pas : 시간이 없어요 (je n’ai pas le temps).', '있어요 = there is, I have; 없어요 = there isn’t, I don’t have: 시간이 없어요 (I don’t have time).'),
      ], [
        G('gram-ko-e', '에', None, 'e', ('à, vers (destination, lieu d’existence, moment)', 'to, at (destination, location, time)')),
        G('gram-ko-eseo', '에서', None, 'eseo', ('à, dans (lieu de l’action)', 'at, in (place of action)')),
        G('gram-ko-itda', '있어요/없어요', None, 'isseoyo / eopseoyo', ('il y a / il n’y a pas ; avoir / ne pas avoir', 'there is / there isn’t; to have / not to have')),
        V('ko-jip', '집', None, 'jip', ('maison, chez soi', 'house, home')),
        V('ko-hakgyo', '학교', None, 'hakgyo', ('école', 'school')),
        V('ko-hoesa', '회사', None, 'hoesa', ('entreprise, bureau', 'company, office')),
        V('ko-sikdang', '식당', None, 'sikdang', ('restaurant', 'restaurant')),
        V('ko-sigan', '시간', None, 'sigan', ('temps ; heure (durée)', 'time; hour (duration)')),
      ], [
        ex('주말에 집에서 쉬어요.', None, 'Le week-end, je me repose à la maison.', 'At the weekend I rest at home.'),
        ex('학교 앞에 식당이 있어요.', None, 'Il y a un restaurant devant l’école.', 'There is a restaurant in front of the school.'),
      ], [
        PC(CHOOSE, '저는 지금 학교＿ 가요.', ['에', '에서'], '에', ('Destination d’un déplacement : 에.', 'Destination of movement: 에.'), ('Je vais à l’école maintenant.', 'I am going to school now.')),
        PC(CHOOSE, '식당＿ 밥을 먹어요.', ['에서', '에'], '에서', ('Lieu où se fait l’action : 에서.', 'Place where the action happens: 에서.'), ('Je mange au restaurant.', 'I eat at the restaurant.')),
        DC(('Ton ami te propose de sortir, mais tu es occupé.', 'Your friend suggests going out, but you are busy.'), [('준호', '오늘 같이 영화 봐요?')], ('Junho te propose de voir un film aujourd’hui.', 'Junho suggests watching a film today.'), ['미안해요. 시간이 없어요.', '네, 집이 있어요.', '학교에서 먹어요.'], '미안해요. 시간이 없어요.', ('시간이 없어요 = je n’ai pas le temps.', '시간이 없어요 = I don’t have time.')),
        TF('집에 고양이가 있어요.', ('Il y a un chat à la maison.', 'There is a cat at home.'), VRAI, ('있어요 = il y a ; 고양이 = chat.', '있어요 = there is; 고양이 = cat.')),
      ]),
  ])])

# ═════════════════════════ Île 6 : le temple dans la montagne ═════════════════════════
W6 = WORLD('topik1-w6', ('Le temple dans la montagne', 'The temple in the mountains'), REGION,
  ('Raconter ce qu’on a fait, dire ce qu’on ne fait pas et ce qu’on va faire.', 'Talk about what you did, what you don’t do and what you are going to do.'),
  (('Le Bulgasari mangeur de fer', 'The Iron-eating Bulgasari'), '불', ('Ce monstre avale toutes les cloches du temple. Raconte-lui hier, aujourd’hui et demain : il ne digère que les phrases justes.', 'This monster swallows every bell in the temple. Tell it about yesterday, today and tomorrow: it only digests correct sentences.')),
  [CH('topik1-w6-c1', ('Hier, jamais, demain', 'Yesterday, never, tomorrow'), [
    L('ko-past', ('Le passé : -았어요/-었어요', 'The past: -았어요/-었어요'), ('Raconter ce qu’on a fait.', 'Talk about what you did.'), 10, [
        ('Même règle qu’au présent : -았어요 si la dernière voyelle est ㅏ ou ㅗ (가다 → 갔어요, 보다 → 봤어요), sinon -었어요 (먹다 → 먹었어요, 마시다 → 마셨어요).', 'Same rule as in the present: -았어요 if the last vowel is ㅏ or ㅗ (가다 → 갔어요, 보다 → 봤어요), otherwise -었어요 (먹다 → 먹었어요, 마시다 → 마셨어요).'),
        ('하다 → 했어요 : 공부했어요, 운동했어요.', '하다 → 했어요: 공부했어요, 운동했어요.'),
        ('Avec un nom : 학생이었어요 (après consonne), 의사였어요 (après voyelle).', 'With a noun: 학생이었어요 (after a consonant), 의사였어요 (after a vowel).'),
      ], [
        G('gram-ko-past', '-았어요/-었어요', None, '-asseoyo / -eosseoyo', ('passé poli', 'polite past')),
        V('ko-eoje', '어제', None, 'eoje', ('hier', 'yesterday')),
        V('ko-jumal', '주말', None, 'jumal', ('week-end', 'weekend')),
        V('ko-chingu', '친구', None, 'chingu', ('ami', 'friend')),
        V('ko-mannada', '만나다', None, 'mannada', ('rencontrer, voir (quelqu’un)', 'to meet, to see (someone)')),
        V('ko-jeol', '절', None, 'jeol', ('temple bouddhiste', 'Buddhist temple')),
        V('ko-san', '산', None, 'san', ('montagne', 'mountain')),
      ], [
        ex('어제 친구를 만났어요.', None, 'Hier, j’ai vu un ami.', 'Yesterday I met a friend.'),
        ex('주말에 산에 갔어요. 절을 봤어요.', None, 'Ce week-end, je suis allé à la montagne. J’ai vu un temple.', 'At the weekend I went to the mountains. I saw a temple.'),
      ], [
        FB(CHOOSE, '어제 학교에 ＿.', ['갔어요', '갔었요', '가었어요'], '갔어요', ('가 + 았어요 → 갔어요.', '가 + 았어요 → 갔어요.'), ('Hier, je suis allé à l’école.', 'Yesterday I went to school.')),
        FB(CHOOSE, '아침에 빵을 ＿.', ['먹었어요', '먹았어요', '먹어요어'], '먹었어요', ('먹 (voyelle ㅓ) + 었어요.', '먹 (vowel ㅓ) + 었어요.'), ('Ce matin, j’ai mangé du pain.', 'This morning I ate bread.')),
        FB(CHOOSE, '주말에 한국어를 공부＿.', ['했어요', '해요었', '하었어요'], '했어요', ('하다 → 했어요.', '하다 → 했어요.'), ('Ce week-end, j’ai étudié le coréen.', 'At the weekend I studied Korean.')),
        TF('어제 친구를 만났어요.', ('La personne verra un ami demain.', 'The speaker will see a friend tomorrow.'), FAUX, ('어제 + 만났어요 : c’est passé, c’était hier.', '어제 + 만났어요: it is past, it was yesterday.')),
      ]),
    L('ko-negation', ('La négation : 안, -지 않아요, 못', 'Negation: 안, -지 않아요, 못'), ('Dire qu’on ne fait pas ou qu’on ne peut pas faire quelque chose.', 'Say that you don’t do or can’t do something.'), 10, [
        ('안 + verbe = ne… pas (choix) : 안 가요, 안 먹어요. Pour un verbe en 하다, 안 se place devant 하다 : 공부 안 해요.', '안 + verb = not (by choice): 안 가요, 안 먹어요. For a 하다 verb, 안 goes before 하다: 공부 안 해요.'),
        ('Radical + 지 않아요 a le même sens, un peu plus soutenu : 가지 않아요.', 'Stem + 지 않아요 means the same, slightly more formal: 가지 않아요.'),
        ('못 + verbe = ne pas pouvoir (impossibilité) : 못 가요 (je ne peux pas y aller). 수영 못 해요.', '못 + verb = cannot (impossibility): 못 가요 (I can’t go). 수영 못 해요.'),
      ], [
        G('gram-ko-an', '안 + verbe', None, 'an + verbe', ('ne… pas (négation courte)', 'not (short negation)')),
        G('gram-ko-ji-anayo', '-지 않아요', None, '-ji anayo', ('ne… pas (négation longue)', 'not (long negation)')),
        G('gram-ko-mot', '못 + verbe', None, 'mot + verbe', ('ne pas pouvoir', 'cannot')),
        V('ko-gimchi', '김치', None, 'gimchi', ('kimchi', 'kimchi')),
        V('ko-joahada', '좋아하다', None, 'joahada', ('aimer (bien)', 'to like')),
        V('ko-jada', '자다', None, 'jada', ('dormir', 'to sleep')),
        V('ko-suyeong', '수영', None, 'suyeong', ('natation', 'swimming')),
      ], [
        ex('저는 고기를 안 먹어요.', None, 'Je ne mange pas de viande.', 'I don’t eat meat.'),
        ex('오늘은 바빠서 못 가요.', None, 'Aujourd’hui je suis occupé, je ne peux pas venir.', 'I’m busy today, so I can’t go.'),
      ], [
        FB(CHOOSE, '저는 커피를 ＿ 마셔요.', ['안', '못해', '지'], '안', ('Négation courte : 안 + verbe.', 'Short negation: 안 + verb.'), ('Je ne bois pas de café.', 'I don’t drink coffee.')),
        FB(CHOOSE, '주말에는 공부 ＿.', ['안 해요', '안 공부해요', '공부 지 않아요'], '안 해요', ('Verbe en 하다 : 안 se place devant 하다.', '하다 verb: 안 goes before 하다.'), ('Le week-end, je n’étudie pas.', 'At the weekend I don’t study.')),
        DC(('Ton ami t’invite à la piscine, mais tu ne sais pas nager.', 'Your friend invites you to the pool, but you can’t swim.'), [('민지', '내일 같이 수영해요!')], ('Minji te propose d’aller nager demain.', 'Minji suggests swimming together tomorrow.'), ['미안해요. 저는 수영 못 해요.', '네, 수영 안 좋아해요.', '어제 수영했어요.'], '미안해요. 저는 수영 못 해요.', ('못 해요 = je ne sais pas / ne peux pas le faire.', '못 해요 = I can’t do it.')),
        TF('김치를 먹지 않아요.', ('La personne mange du kimchi.', 'The speaker eats kimchi.'), FAUX, ('-지 않아요 = ne… pas.', '-지 않아요 = not.')),
      ]),
    L('ko-future', ('Le futur : -(으)ㄹ 거예요', 'The future: -(으)ㄹ 거예요'), ('Dire ce qu’on va faire.', 'Say what you are going to do.'), 9, [
        ('Radical terminé par une voyelle + ㄹ 거예요 : 가다 → 갈 거예요, 보다 → 볼 거예요.', 'Stem ending in a vowel + ㄹ 거예요: 가다 → 갈 거예요, 보다 → 볼 거예요.'),
        ('Radical terminé par une consonne + 을 거예요 : 먹다 → 먹을 거예요, 읽다 → 읽을 거예요. 하다 → 할 거예요.', 'Stem ending in a consonant + 을 거예요: 먹다 → 먹을 거예요, 읽다 → 읽을 거예요. 하다 → 할 거예요.'),
        ('Mots du futur : 내일 (demain), 다음 주 (la semaine prochaine), 방학 (les vacances scolaires).', 'Future words: 내일 (tomorrow), 다음 주 (next week), 방학 (school holidays).'),
      ], [
        G('gram-ko-future', '-(으)ㄹ 거예요', None, '-(eu)l geoyeyo', ('futur : je vais…', 'future: I am going to…')),
        V('ko-naeil', '내일', None, 'naeil', ('demain', 'tomorrow')),
        V('ko-daeum-ju', '다음 주', None, 'daeum ju', ('la semaine prochaine', 'next week')),
        V('ko-yeohaeng', '여행', None, 'yeohaeng', ('voyage', 'trip, travel')),
        V('ko-bada', '바다', None, 'bada', ('mer', 'sea')),
        V('ko-jeju-do', '제주도', None, 'jeju-do', ('l’île de Jeju', 'Jeju Island')),
      ], [
        ex('다음 주에 제주도에 갈 거예요.', None, 'La semaine prochaine, j’irai sur l’île de Jeju.', 'Next week I’m going to Jeju Island.'),
        ex('내일 바다에서 수영할 거예요.', None, 'Demain, je vais nager dans la mer.', 'Tomorrow I’m going to swim in the sea.'),
      ], [
        FB(CHOOSE, '내일 영화를 ＿ 거예요.', ['볼', '봘', '보을'], '볼', ('보 (voyelle) + ㄹ 거예요 → 볼 거예요.', '보 (vowel) + ㄹ 거예요 → 볼 거예요.'), ('Demain, je vais voir un film.', 'Tomorrow I’m going to watch a film.')),
        FB(CHOOSE, '저녁에 비빔밥을 ＿ 거예요.', ['먹을', '먹ㄹ', '먹는'], '먹을', ('먹 (consonne) + 을 거예요.', '먹 (consonant) + 을 거예요.'), ('Ce soir, je vais manger un bibimbap.', 'This evening I’m going to eat bibimbap.')),
        SO(('Remets dans l’ordre : « Je vais voyager la semaine prochaine. »', 'Put in order: “I am going to travel next week.”'), ['다음 주에', '여행을', '할 거예요.'], ('Moment + objet + verbe au futur.', 'Time + object + verb in the future.')),
        TF('내일 바다에 갈 거예요.', ('La personne est allée à la mer hier.', 'The speaker went to the sea yesterday.'), FAUX, ('내일 + 갈 거예요 : c’est pour demain.', '내일 + 갈 거예요: it is for tomorrow.')),
      ]),
  ])])

# ═════════════════════════ Île 7 : la fête de Chuseok ═════════════════════════
W7 = WORLD('topik1-w7', ('La fête de Chuseok', 'The Chuseok festival'), REGION,
  ('Exprimer un souhait, demander poliment, proposer, relier et opposer deux idées.', 'Express a wish, ask politely, make a suggestion, link and contrast two ideas.'),
  (('Le Messager de l’au-delà', 'The Messenger of the Afterlife'), '저', ('À la pleine lune de Chuseok, le jeoseung saja vient chercher les mots oubliés. Parle à ta famille sans hésiter pour qu’il reparte les mains vides.', 'At the Chuseok full moon, the jeoseung saja comes for forgotten words. Talk to your family without hesitating so that he leaves empty-handed.')),
  [CH('topik1-w7-c1', ('En famille', 'With the family'), [
    L('ko-want', ('Je voudrais… : -고 싶어요', 'I would like to…: -고 싶어요'), ('Exprimer ce qu’on a envie de faire.', 'Say what you want to do.'), 9, [
        ('Radical + 고 싶어요 = je veux, j’ai envie de : 가고 싶어요, 먹고 싶어요. Pas de règle de voyelle : on ajoute directement 고.', 'Stem + 고 싶어요 = I want to, I feel like: 가고 싶어요, 먹고 싶어요. No vowel rule: you just add 고.'),
        ('Question : 뭐 하고 싶어요? (Qu’est-ce que tu veux faire ?). Au passé : 보고 싶었어요 (tu m’as manqué, littéralement « je voulais te voir »).', 'Question: 뭐 하고 싶어요? (What do you want to do?). In the past: 보고 싶었어요 (I missed you, literally “I wanted to see you”).'),
        ('Pendant Chuseok, la fête des récoltes, les familles rentrent au 고향 (village natal) et mangent des 송편.', 'During Chuseok, the harvest festival, families go back to their 고향 (hometown) and eat 송편.'),
      ], [
        G('gram-ko-go-sipeoyo', '-고 싶어요', None, '-go sipeoyo', ('je veux…, j’ai envie de…', 'I want to…, I feel like…')),
        V('ko-gajok', '가족', None, 'gajok', ('famille', 'family')),
        V('ko-eomeoni', '어머니', None, 'eomeoni', ('mère', 'mother')),
        V('ko-abeoji', '아버지', None, 'abeoji', ('père', 'father')),
        V('ko-gohyang', '고향', None, 'gohyang', ('ville ou village natal', 'hometown')),
        V('ko-songpyeon', '송편', None, 'songpyeon', ('songpyeon (gâteau de riz de Chuseok)', 'songpyeon (Chuseok rice cake)')),
      ], [
        ex('추석에 고향에 가고 싶어요.', None, 'Pour Chuseok, je voudrais rentrer dans ma ville natale.', 'For Chuseok I want to go back to my hometown.'),
        ex('어머니, 정말 보고 싶었어요!', None, 'Maman, tu m’as tellement manqué !', 'Mum, I really missed you!'),
      ], [
        FB(CHOOSE, '송편을 먹＿ 싶어요.', ['고', '어', '을'], '고', ('Radical + 고 싶어요.', 'Stem + 고 싶어요.'), ('J’ai envie de manger des songpyeon.', 'I want to eat songpyeon.')),
        FB(CHOOSE, '가족을 ＿ 싶어요.', ['보고', '봐고', '볼고'], '보고', ('보 + 고 싶어요 → 보고 싶어요.', '보 + 고 싶어요 → 보고 싶어요.'), ('Ma famille me manque. (Je veux voir ma famille.)', 'I miss my family. (I want to see my family.)')),
        DC(('Ton ami te demande ce que tu veux faire pour les vacances.', 'Your friend asks what you want to do for the holidays.'), [('준호', '방학에 뭐 하고 싶어요?')], ('Junho te demande ce que tu veux faire pendant les vacances.', 'Junho asks what you want to do during the holidays.'), ['한국에 여행 가고 싶어요.', '어제 여행했어요.', '네, 하고 싶어요.'], '한국에 여행 가고 싶어요.', ('On répond à 뭐 하고 싶어요? avec -고 싶어요.', 'You answer 뭐 하고 싶어요? with -고 싶어요.')),
        TF('아버지가 보고 싶어요.', ('La personne voudrait voir son père.', 'The speaker would like to see their father.'), VRAI, ('보고 싶어요 = je veux voir, il me manque.', '보고 싶어요 = I want to see, I miss.')),
      ]),
    L('ko-request', ('Demander et proposer : -(으)세요, -(으)ㄹ까요?', 'Asking and suggesting: -(으)세요, -(으)ㄹ까요?'), ('Inviter poliment quelqu’un à faire quelque chose et faire une proposition.', 'Politely invite someone to do something and make a suggestion.'), 10, [
        ('Radical + (으)세요 = demande polie : 앉으세요 (asseyez-vous), 기다리세요 (attendez), 가세요 (allez-y). 으 s’ajoute après une consonne.', 'Stem + (으)세요 = polite request: 앉으세요 (please sit down), 기다리세요 (please wait), 가세요 (please go). 으 is added after a consonant.'),
        ('Radical + (으)ㄹ까요? = « et si on… ? » : 같이 갈까요? (on y va ensemble ?), 뭐 먹을까요? (on mange quoi ?).', 'Stem + (으)ㄹ까요? = “shall we…?”: 같이 갈까요? (shall we go together?), 뭐 먹을까요? (what shall we eat?).'),
        ('Pour accepter : 좋아요! (d’accord, avec plaisir).', 'To accept: 좋아요! (sounds good!).'),
      ], [
        G('gram-ko-seyo', '-(으)세요', None, '-(eu)seyo', ('demande polie : faites…, veuillez…', 'polite request: please…')),
        G('gram-ko-lkkayo', '-(으)ㄹ까요?', None, '-(eu)lkkayo?', ('proposition : et si on… ?', 'suggestion: shall we…?')),
        V('ko-anjda', '앉다', None, 'anjda', ("s'asseoir", 'to sit down')),
        V('ko-gidarida', '기다리다', None, 'gidarida', ('attendre', 'to wait')),
        V('ko-gachi', '같이', None, 'gachi', ('ensemble', 'together')),
        V('ko-joayo', '좋아요', None, 'joayo', ('c’est bien, d’accord', 'it’s good, OK')),
      ], [
        ex('할머니, 여기 앉으세요.', None, 'Grand-mère, asseyez-vous ici.', 'Grandma, please sit here.'),
        ex('같이 송편을 만들까요? — 좋아요!', None, 'On fait des songpyeon ensemble ? — D’accord !', 'Shall we make songpyeon together? — Sounds good!'),
      ], [
        FB(CHOOSE, '잠깐만 ＿.', ['기다리세요', '기다리으세요', '기다려세요'], '기다리세요', ('기다리 (voyelle) + 세요.', '기다리 (vowel) + 세요.'), ('Attendez un instant, s’il vous plaît.', 'Please wait a moment.')),
        FB(CHOOSE, '여기 ＿.', ['앉으세요', '앉세요', '앉아세요'], '앉으세요', ('앉 (consonne) + 으세요.', '앉 (consonant) + 으세요.'), ('Asseyez-vous ici, je vous en prie.', 'Please sit here.')),
        FB(CHOOSE, '주말에 같이 영화를 ＿?', ['볼까요', '봐까요', '보을까요'], '볼까요', ('보 (voyelle) + ㄹ까요.', '보 (vowel) + ㄹ까요.'), ('On va voir un film ensemble ce week-end ?', 'Shall we watch a film together at the weekend?')),
        DC(('Ton amie te propose de manger ensemble. Tu acceptes.', 'Your friend suggests eating together. You accept.'), [('민지', '같이 점심 먹을까요?')], ('Minji te propose de déjeuner ensemble.', 'Minji suggests having lunch together.'), ['좋아요!', '앉으세요.', '먹었어요?'], '좋아요!', ('좋아요 = d’accord, avec plaisir.', '좋아요 = sounds good.')),
      ]),
    L('ko-and-but', ('Et, mais : -고, -지만', 'And, but: -고, -지만'), ('Relier deux idées et les opposer, avec des adjectifs courants.', 'Link two ideas and contrast them, with common adjectives.'), 9, [
        ('En coréen, les adjectifs se conjuguent comme des verbes : 크다 (être grand) → 커요, 작다 (être petit) → 작아요, 맛있다 (être bon) → 맛있어요.', 'In Korean, adjectives are conjugated like verbs: 크다 (to be big) → 커요, 작다 (to be small) → 작아요, 맛있다 (to be tasty) → 맛있어요.'),
        ('Radical + 고 = et : 싸고 맛있어요 (c’est bon marché et délicieux).', 'Stem + 고 = and: 싸고 맛있어요 (it’s cheap and tasty).'),
        ('Radical + 지만 = mais : 비싸지만 맛있어요 (c’est cher mais délicieux).', 'Stem + 지만 = but: 비싸지만 맛있어요 (it’s expensive but tasty).'),
      ], [
        G('gram-ko-go', '-고', None, '-go', ('et (relie deux propositions)', 'and (links two clauses)')),
        G('gram-ko-jiman', '-지만', None, '-jiman', ('mais', 'but')),
        V('ko-keuda', '크다', None, 'keuda', ('être grand, gros', 'to be big')),
        V('ko-jakda', '작다', None, 'jakda', ('être petit', 'to be small')),
        V('ko-masitda', '맛있다', None, 'masitda', ('être bon, délicieux', 'to be tasty, delicious')),
        V('ko-jaemiitda', '재미있다', None, 'jaemiitda', ('être amusant, intéressant', 'to be fun, interesting')),
      ], [
        ex('이 식당은 싸고 맛있어요.', None, 'Ce restaurant est bon marché et délicieux.', 'This restaurant is cheap and tasty.'),
        ex('한국어는 어렵지만 재미있어요.', None, 'Le coréen est difficile mais passionnant.', 'Korean is difficult but fun.'),
      ], [
        FB(CHOOSE, '방이 크＿ 깨끗해요.', ['고', '지만', '어서'], '고', ('Deux qualités qui s’ajoutent : -고.', 'Two qualities that add up: -고.'), ('La chambre est grande et propre.', 'The room is big and clean.')),
        FB(CHOOSE, '이 가방은 예쁘＿ 비싸요.', ['지만', '고', '세요'], '지만', ('Opposition (joli / cher) : -지만.', 'Contrast (pretty / expensive): -지만.'), ('Ce sac est joli mais cher.', 'This bag is pretty but expensive.')),
        SO(('Remets dans l’ordre : « Le kimchi est épicé mais bon. »', 'Put in order: “Kimchi is spicy but tasty.”'), ['김치는', '맵지만', '맛있어요.'], ('Thème + adjectif-지만 + adjectif conjugué.', 'Topic + adjective-지만 + conjugated adjective.')),
        TF('집이 작지만 좋아요.', ('La personne trouve sa maison grande.', 'The speaker finds their house big.'), FAUX, ('작지만 = petit mais…', '작지만 = small but…')),
      ]),
  ])])

# ═════════════════════════ Île 8 : les rues de Busan ═════════════════════════
W8 = WORLD('topik1-w8', ('Les rues de Busan', 'The streets of Busan'), REGION,
  ('Se déplacer, parler du temps qu’il fait et commander au restaurant.', 'Get around, talk about the weather and order at a restaurant.'),
  (('Le Dragon de la mer de l’Est', 'The Dragon of the East Sea'), '용', ('Le roi Munmu devenu dragon veille sur le port de Busan. Guide-toi en ville, commande ton repas : il juge ceux qui veulent prendre la mer.', 'King Munmu, turned into a dragon, watches over the port of Busan. Find your way round the city and order your meal: he judges all who wish to put to sea.')),
  [CH('topik1-w8-c1', ('Vie quotidienne', 'Daily life'), [
    L('ko-transport', ('Se déplacer : (으)로, 에서… 까지', 'Getting around: (으)로, 에서… 까지'), ('Dire comment on se déplace, d’où et jusqu’où.', 'Say how you travel, where from and how far.'), 9, [
        ('Moyen de transport + (으)로 : 버스로, 지하철로, 기차로 (로 après une voyelle ou ㄹ, 으로 après une autre consonne : 택시로, 발으로 n’existe pas, on dit 걸어서 = à pied).', 'Means of transport + (으)로: 버스로, 지하철로, 기차로 (로 after a vowel or ㄹ, 으로 after another consonant; on foot is 걸어서).'),
        ('A에서 B까지 = de A jusqu’à B : 서울에서 부산까지 기차로 가요.', 'A에서 B까지 = from A to B: 서울에서 부산까지 기차로 가요.'),
        ('타다 = monter dans, prendre (un véhicule) : 버스를 타요.', '타다 = to get on, to take (a vehicle): 버스를 타요.'),
      ], [
        G('gram-ko-euro', '(으)로', None, '(eu)ro', ('en, par (moyen)', 'by, with (means)')),
        G('gram-ko-eseo-kkaji', '에서 … 까지', None, 'eseo … kkaji', ('de … jusqu’à …', 'from … to …')),
        V('ko-beoseu', '버스', None, 'beoseu', ('bus', 'bus')),
        V('ko-jihacheol', '지하철', None, 'jihacheol', ('métro', 'subway, underground')),
        V('ko-gicha', '기차', None, 'gicha', ('train', 'train')),
        V('ko-tada', '타다', None, 'tada', ('monter dans, prendre (un véhicule)', 'to get on, to take (a vehicle)')),
        V('ko-yeok', '역', None, 'yeok', ('gare', 'station')),
      ], [
        ex('서울에서 부산까지 기차로 세 시간 걸려요.', None, 'De Séoul à Busan, il faut trois heures en train.', 'It takes three hours by train from Seoul to Busan.'),
        ex('부산역에서 지하철을 타세요.', None, 'Prenez le métro à la gare de Busan.', 'Take the subway at Busan Station.'),
      ], [
        PC(CHOOSE, '저는 회사에 지하철＿ 가요.', ['로', '으로', '에'], '로', ('지하철 finit par ㄹ : 로.', '지하철 ends with ㄹ: 로.'), ('Je vais au bureau en métro.', 'I go to the office by subway.')),
        PC(CHOOSE, '집에서 학교＿ 걸어서 가요.', ['까지', '에서', '로'], '까지', ('Jusqu’à : 까지.', 'Up to, as far as: 까지.'), ('Je vais de chez moi à l’école à pied.', 'I walk from home to school.')),
        DC(('Un touriste te demande comment aller à la plage de Haeundae.', 'A tourist asks you how to get to Haeundae Beach.'), [('관광객', '해운대에 어떻게 가요?')], ('Un touriste demande comment aller à Haeundae.', 'A tourist asks how to get to Haeundae.'), ['지하철 2호선을 타세요.', '해운대에 있어요.', '어제 갔어요.'], '지하철 2호선을 타세요.', ('Pour indiquer un chemin : 타세요 (prenez…).', 'To give directions: 타세요 (take…).')),
        TF('부산까지 버스로 가요.', ('La personne va à Busan en train.', 'The speaker goes to Busan by train.'), FAUX, ('버스로 = en bus.', '버스로 = by bus.')),
      ]),
    L('ko-weather', ('Le temps et les saisons : 덥다 → 더워요', 'Weather and seasons: 덥다 → 더워요'), ('Parler du temps qu’il fait et des saisons.', 'Talk about the weather and the seasons.'), 9, [
        ('Corée = quatre saisons bien marquées : 봄 (printemps), 여름 (été), 가을 (automne), 겨울 (hiver).', 'Korea has four distinct seasons: 봄 (spring), 여름 (summer), 가을 (autumn), 겨울 (winter).'),
        ('Beaucoup d’adjectifs dont le radical finit par ㅂ changent ㅂ en 우 : 덥다 → 더워요 (il fait chaud), 춥다 → 추워요 (il fait froid).', 'Many adjectives whose stem ends in ㅂ turn ㅂ into 우: 덥다 → 더워요 (it’s hot), 춥다 → 추워요 (it’s cold).'),
        ('비가 와요 = il pleut, 눈이 와요 = il neige. 날씨가 좋아요 = il fait beau.', '비가 와요 = it’s raining, 눈이 와요 = it’s snowing. 날씨가 좋아요 = the weather is nice.'),
      ], [
        G('gram-ko-b-irregular', 'ㅂ → 우 : 더워요', None, 'b → u : deowoyo', ('adjectifs en ㅂ irréguliers', 'irregular ㅂ adjectives')),
        V('ko-nalssi', '날씨', None, 'nalssi', ('temps (météo)', 'weather')),
        V('ko-deopda', '덥다', None, 'deopda', ('faire chaud', 'to be hot (weather)')),
        V('ko-chupda', '춥다', None, 'chupda', ('faire froid', 'to be cold (weather)')),
        V('ko-bi', '비', None, 'bi', ('pluie', 'rain')),
        V('ko-yeoreum', '여름', None, 'yeoreum', ('été', 'summer')),
        V('ko-gyeoul', '겨울', None, 'gyeoul', ('hiver', 'winter')),
        V('ko-gaeul', '가을', None, 'gaeul', ('automne', 'autumn')),
      ], [
        ex('부산의 여름은 덥지만 바다가 좋아요.', None, 'L’été à Busan, il fait chaud, mais la mer est agréable.', 'Summer in Busan is hot, but the sea is lovely.'),
        ex('오늘은 비가 와요. 우산을 가져가세요.', None, 'Il pleut aujourd’hui. Prenez un parapluie.', 'It’s raining today. Take an umbrella.'),
      ], [
        FB(CHOOSE, '여름에는 날씨가 ＿.', ['더워요', '덥어요', '더어요'], '더워요', ('덥다 : ㅂ devient 우 → 더워요.', '덥다: ㅂ becomes 우 → 더워요.'), ('En été, il fait chaud.', 'In summer the weather is hot.')),
        FB(CHOOSE, '겨울에는 정말 ＿.', ['추워요', '춥어요', '추어요'], '추워요', ('춥다 → 추워요.', '춥다 → 추워요.'), ('En hiver, il fait vraiment froid.', 'In winter it is really cold.')),
        DC(('Ton ami te demande quelle saison tu préfères.', 'Your friend asks which season you prefer.'), [('민지', '무슨 계절을 좋아해요?')], ('Minji te demande quelle saison tu aimes.', 'Minji asks which season you like.'), ['가을을 좋아해요.', '비가 와요.', '추워요?'], '가을을 좋아해요.', ('계절 = saison ; on répond avec une saison + 을/를 좋아해요.', '계절 = season; you answer with a season + 을/를 좋아해요.')),
        TF('오늘은 비가 와요.', ('Il fait beau aujourd’hui.', 'The weather is fine today.'), FAUX, ('비가 와요 = il pleut.', '비가 와요 = it’s raining.')),
      ]),
    L('ko-restaurant', ('Au restaurant : 주세요, 하고', 'At the restaurant: 주세요, 하고'), ('Commander, demander quelque chose et énumérer des plats.', 'Order, ask for something and list dishes.'), 9, [
        ('Nom + 주세요 = donnez-moi…, s’il vous plaît : 물 주세요, 비빔밥 하나 주세요.', 'Noun + 주세요 = please give me…: 물 주세요, 비빔밥 하나 주세요.'),
        ('하고 relie deux noms (« et ») : 비빔밥하고 불고기 주세요. À l’oral, on entend aussi 이랑/랑.', '하고 links two nouns (“and”): 비빔밥하고 불고기 주세요. In speech you also hear 이랑/랑.'),
        ('Avant de manger : 잘 먹겠습니다 (merci pour ce repas). Le serveur dit : 맛있게 드세요 (bon appétit).', 'Before eating: 잘 먹겠습니다 (thank you for the meal). The waiter says: 맛있게 드세요 (enjoy your meal).'),
      ], [
        G('gram-ko-juseyo', '주세요', None, 'juseyo', ('donnez-moi…, s’il vous plaît', 'please give me…')),
        G('gram-ko-hago', '하고', None, 'hago', ('et (entre deux noms)', 'and (between two nouns)')),
        V('ko-bibimbap', '비빔밥', None, 'bibimbap', ('bibimbap (riz mélangé aux légumes)', 'bibimbap (rice mixed with vegetables)')),
        V('ko-bulgogi', '불고기', None, 'bulgogi', ('bulgogi (bœuf mariné grillé)', 'bulgogi (marinated grilled beef)')),
        V('ko-menyu', '메뉴', None, 'menyu', ('menu, carte', 'menu')),
        V('ko-maepda', '맵다', None, 'maepda', ('être épicé, piquant', 'to be spicy')),
        V('ko-jal-meokgetseumnida', '잘 먹겠습니다', None, 'jal meokgetseumnida', ('merci pour ce repas (avant de manger)', 'thank you for the meal (before eating)')),
      ], [
        ex('여기요! 비빔밥하고 불고기 주세요.', None, 'S’il vous plaît ! Un bibimbap et un bulgogi.', 'Excuse me! A bibimbap and a bulgogi, please.'),
        ex('이 김치는 너무 매워요. 물 좀 주세요.', None, 'Ce kimchi est trop épicé. De l’eau, s’il vous plaît.', 'This kimchi is too spicy. Some water, please.'),
      ], [
        FB(CHOOSE, '메뉴 좀 ＿.', ['주세요', '줘요세요', '주어세요'], '주세요', ('Nom + 주세요.', 'Noun + 주세요.'), ('La carte, s’il vous plaît.', 'The menu, please.')),
        PC(CHOOSE, '김밥＿ 라면 주세요.', ['하고', '에서', '을'], '하고', ('하고 relie deux noms.', '하고 links two nouns.'), ('Un gimbap et des ramyeon, s’il vous plaît.', 'A gimbap and ramyeon, please.')),
        DC(('Le plat arrive. Que dis-tu avant de manger ?', 'The dish arrives. What do you say before eating?'), [('점원', '맛있게 드세요.')], ('Le serveur te souhaite bon appétit.', 'The waiter wishes you a good meal.'), ['잘 먹겠습니다!', '주세요.', '얼마예요?'], '잘 먹겠습니다!', ('Avant de manger : 잘 먹겠습니다.', 'Before eating: 잘 먹겠습니다.')),
        TF('이 떡볶이는 매워요.', ('Le tteokbokki est épicé.', 'The tteokbokki is spicy.'), VRAI, ('맵다 → 매워요 : c’est épicé.', '맵다 → 매워요: it’s spicy.')),
      ]),
  ])])

FINAL = {
  'slug': 'topik1-final',
  'title': t(('Simulation TOPIK I', 'TOPIK I simulation')),
  'region': REGION,
  'description': t(('Examen blanc au format du TOPIK I : écoute (듣기) et lecture (읽기), en coréen, noté sur 200. Niveau 1 à 80 points, niveau 2 à 140.', 'Mock exam in TOPIK I format: listening (듣기) and reading (읽기), in Korean, marked out of 200. Level 1 at 80 points, level 2 at 140.')),
  'exam': 'topik1-official',
  'chapters': [],
}

level = {
  'contentVersion': '2026.11.20',
  'level': {'code': 'TOPIK1', 'title': t(('Débutant : premiers pas en coréen', 'Beginner: first steps in Korean')), 'region': REGION, 'order': 16},
  'notice': t(('Les listes de vocabulaire de Koto Quest sont alignées sur les compétences attendues au TOPIK I (niveau 1) mais ne constituent pas des listes officielles du TOPIK.', 'Koto Quest’s vocabulary lists are aligned with the skills expected at TOPIK I (level 1) but are not official TOPIK lists.')),
  'worlds': [W1, W2, W3, W4, W5, W6, W7, W8, FINAL],
}
t((REGION, 'Land of the Morning Calm'))
for fr, en in CATALOG_EN.items():
    t((fr, en))
for sec in CATALOG['sections']:
    t((sec['title'], CATALOG_EN.get(sec['title'], sec['title'])))
os.makedirs(os.path.join(ROOT, 'content/topik1'), exist_ok=True)
check_and_write(level, 'content/topik1/topik1.json', ['content/n5/n5.json', 'content/n4/n4.json', 'content/n3/n3.json', 'content/n2/n2.json', 'content/n1/n1.json'])
json.dump(CATALOG, open(os.path.join(ROOT, 'content/characters/hangul.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('Hangeul :', sum(len(g['items']) for s in CATALOG['sections'] for g in s['groups']), 'caractères')
