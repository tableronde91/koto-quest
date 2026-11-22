# Banque de questions de l'examen blanc TOEIC A1 (content/exams/a1-toeic.json), au format du TOEIC Listening & Reading
# (version abrégée) : parties 2 à 4 (écoute, 10 questions tirées), 5 et 6 (phrases et textes à compléter, 12 questions),
# 7 (compréhension écrite, 6 questions). Notation sur 990 (Listening et Reading de 5 à 495 chacun).
# Dans chaque question, le premier choix est la bonne réponse (l'ordre est mélangé à chaque examen).
# Usage : python3 scripts/a1-toeic.py
import json, os
ROOT = os.path.join(os.path.dirname(__file__), '..')
WHO = {'N': 'Narrateur', 'M': 'Homme', 'F': 'Femme'}

def LQ(audio, choices, text=None, audio_choices=False):
    lines = [l.strip() for l in audio.strip().split('\n') if l.strip()]
    for l in lines:
        assert l[1] == '|' and l[0] in WHO, l
    q = {'audio': '\n'.join(lines), 'choices': choices, 'answer': choices[0],
         'explanation': 'Transcription : ' + ' / '.join(f"{WHO[l[0]]} : {l[2:]}" for l in lines)}
    if text:
        q['text'] = text
    if audio_choices:
        q['audioChoices'] = True
    return q

def RQ(choices, jp=None, passage=None, text=None):
    q = {'choices': choices, 'answer': choices[0], 'explanation': f'Réponse : {choices[0]}'}
    if jp: q['jp'] = jp
    if passage: q['passage'] = passage
    if text: q['text'] = text
    return q

def PART(id, section, jpTitle, title, prompt, count, questions, listening=False):
    for q in questions:
        assert len(set(q['choices'])) == len(q['choices']) >= 3, q
    assert len(questions) >= count, id
    p = {'id': id, 'section': section, 'jpTitle': jpTitle, 'title': title, 'prompt': prompt, 'count': count, 'questions': questions}
    if listening:
        p['listening'] = True
    return p

# ═════════════════════════ Listening ═════════════════════════
P2 = PART('p2', 'listening', 'Part 2 — Question-Response', 'Questions-réponses', 'You will hear a question or statement. Select the best response.', 4, [
  LQ('M|Where is the meeting room?', ['It’s next to the kitchen.', 'At ten o’clock.', 'Yes, it is.']),
  LQ('F|What time does the train leave?', ['At half past eight.', 'From platform two.', 'By train.']),
  LQ('M|Can I have a coffee, please?', ['Sure. Anything else?', 'No, I can’t swim.', 'It’s on Monday.']),
  LQ('F|Who is your manager?', ['Mr Ambrose.', 'In London.', 'Every day.']),
  LQ('M|How much is this umbrella?', ['Twelve pounds.', 'It’s raining.', 'It’s mine.']),
  LQ('F|Do you work at the weekend?', ['No, I don’t.', 'No, I’m not.', 'No, it isn’t.']),
  LQ('M|Have you got a pen?', ['Yes, here you are.', 'Yes, I am.', 'Yes, it’s sunny.']),
], listening=True)

P3 = PART('p3', 'listening', 'Part 3 — Conversations', 'Conversations', 'You will hear a short conversation. Answer the question about it.', 3, [
  LQ('F|Hi, Tom. Are you coming to the meeting?\nM|Sorry, I can’t. I’m waiting for a call from a client.\nF|OK, no problem.', ['He is waiting for a call.', 'He is in a meeting.', 'He is on holiday.', 'He is at the station.'], text='Why can’t the man go to the meeting?'),
  LQ('M|Good morning. A return ticket to Oxford, please.\nF|That’s twenty-four pounds. The train leaves from platform three.\nM|Thank you.', ['At a train station.', 'In a cafe.', 'At an airport.', 'In a bank.'], text='Where are the speakers?'),
  LQ('F|What would you like?\nM|A tea and a chicken sandwich, please. To take away.\nF|That’s six pounds fifty.', ['A tea and a sandwich.', 'A coffee and a cake.', 'Two teas.', 'A glass of water.'], text='What does the man order?'),
  LQ('M|Where’s Kate today?\nF|She isn’t at the office. She’s working from home.\nM|Oh, right. I’ll send her an email.', ['She is working from home.', 'She is ill.', 'She is in Paris.', 'She is in the meeting room.'], text='Where is Kate?'),
  LQ('F|Excuse me, how do I get to the museum?\nM|Go straight on and turn left at the bank. It’s opposite the park.\nF|Thanks a lot!', ['Directions to the museum.', 'The price of a ticket.', 'The opening hours.', 'A good restaurant.'], text='What does the woman ask for?'),
], listening=True)

P4 = PART('p4', 'listening', 'Part 4 — Talks', 'Annonces', 'You will hear a short talk. Answer the question about it.', 3, [
  LQ('N|Attention, please. The ten fifteen train to Cardiff is now leaving from platform six. Platform six for the ten fifteen train to Cardiff.', ['Platform six.', 'Platform two.', 'Platform ten.', 'Platform fifteen.'], text='Where does the train to Cardiff leave from?'),
  LQ('N|Good morning, everyone. Welcome to Avalon and Company. The meeting starts at nine thirty in room twelve. Coffee is in the kitchen, next to the lifts.', ['At nine thirty.', 'At nine o’clock.', 'At twelve o’clock.', 'At ten thirty.'], text='When does the meeting start?'),
  LQ('N|Hello, this is Anna from the City Cafe. Your table for two is ready for Friday at eight p.m. Please call us if you are late. Thank you!', ['To confirm a table.', 'To cancel a meeting.', 'To sell a ticket.', 'To ask for a job.'], text='Why is Anna calling?'),
  LQ('N|Today in London it’s cloudy in the morning, with some rain in the afternoon. Take an umbrella! Tomorrow will be sunny and warm.', ['Rain in the afternoon.', 'Snow in the morning.', 'Sun all day.', 'A very cold night.'], text='What is the weather like today?'),
  LQ('N|The library is open from Monday to Friday, nine a.m. to six p.m. On Saturdays, it’s open in the morning only. It’s closed on Sundays.', ['On Sundays.', 'On Saturdays.', 'On Mondays.', 'On Fridays.'], text='When is the library closed?'),
], listening=True)

# ═════════════════════════ Reading ═════════════════════════
P5 = PART('p5', 'grammar', 'Part 5 — Incomplete Sentences', 'Phrases à compléter', 'A word or phrase is missing in each sentence. Select the best answer to complete the sentence.', 8, [
  RQ(['is', 'are', 'am', 'be'], jp='Our office ＿ on the third floor.'),
  RQ(['works', 'work', 'working', 'to work'], jp='Ms Brown ＿ in the sales department.'),
  RQ(['an', 'a', 'the', 'some'], jp='He is ＿ engineer at a big company.'),
  RQ(['any', 'some', 'a', 'an'], jp='We haven’t got ＿ paper for the printer.'),
  RQ(['on', 'at', 'in', 'to'], jp='The meeting is ＿ Tuesday.'),
  RQ(['at', 'on', 'in', 'by'], jp='The shop opens ＿ nine o’clock.'),
  RQ(['Does', 'Do', 'Is', 'Are'], jp='＿ your manager speak French?'),
  RQ(['are calling', 'calls', 'call', 'is call'], jp='Please wait. We ＿ the client right now.'),
  RQ(['went', 'go', 'goes', 'going'], jp='Last week, the team ＿ to Manchester.'),
  RQ(['can', 'cans', 'can to', 'is can'], jp='I ＿ help you with the report.'),
  RQ(['their', 'there', 'they', 'them'], jp='The interns are in ＿ office.'),
  RQ(['were', 'was', 'are', 'is'], jp='Mr and Mrs Lee ＿ in Paris yesterday.'),
])

P6 = PART('p6', 'grammar', 'Part 6 — Text Completion', 'Textes à compléter', 'Read the text. A word or phrase is missing. Select the best answer to complete the text.', 4, [
  RQ(['has got', 'have got', 'is', 'are'], passage='To: All staff\nFrom: Mr Ambrose\nSubject: New colleague\n\nPlease welcome Emma Martin to the team. She is our new intern. Emma is from Lyon and she ＿ two brothers. Her desk is next to the window.', text='Choose the word for the blank.'),
  RQ(['next to', 'under', 'between', 'behind'], passage='Welcome to the City Cafe!\nOur new coffee machine is ＿ the door, on your right as you come in. Please take a cup and help yourself.', text='Choose the words for the blank.'),
  RQ(['closed', 'open', 'opens', 'close'], passage='NOTICE\nThe staff kitchen is ＿ on Friday afternoon for cleaning. Sorry for the trouble. It opens again on Monday at 8 a.m.', text='Choose the word for the blank.'),
  RQ(['Can', 'Do', 'Are', 'Is'], passage='Hi Tom,\nI’m at the station and my train is late. ＿ you start the meeting without me? I’ll be there at 10.\nThanks,\nKate', text='Choose the word for the blank.'),
  RQ(['bought', 'buy', 'buys', 'buyed'], passage='Dear Anna,\nThank you for the lovely weekend in Bath! We visited the Roman baths and I ＿ a book about the city. See you soon!\nSam', text='Choose the word for the blank.'),
  RQ(['tickets', 'ticket', 'a ticket', 'the ticket'], passage='CITY MUSEUM\nAdult ＿ cost £8. Children under 12 are free. Open every day from 10 a.m. to 5 p.m.', text='Choose the word for the blank.'),
])

P7 = PART('p7', 'reading', 'Part 7 — Reading Comprehension', 'Compréhension écrite', 'Read the text and answer the question.', 6, [
  RQ(['At 3 p.m.', 'At 10 a.m.', 'At 1 p.m.', 'At 5 p.m.'], passage='MEMO\nTo: Sales team\nThe team meeting is now at 3 p.m., not 10 a.m. It is in room 4. Please bring your laptop.\nMr Ambrose', text='When is the meeting?'),
  RQ(['Bring a laptop.', 'Call Mr Ambrose.', 'Go to room 10.', 'Buy a coffee.'], passage='MEMO\nTo: Sales team\nThe team meeting is now at 3 p.m., not 10 a.m. It is in room 4. Please bring your laptop.\nMr Ambrose', text='What must the team do?'),
  RQ(['£2.50', '£3.20', '£4.00', '£1.80'], passage='CITY CAFE — MENU\nTea ........ £1.80\nCoffee ...... £2.50\nSandwich .... £4.00\nCake ........ £3.20', text='How much is a coffee?'),
  RQ(['On Sunday.', 'On Monday.', 'On Saturday morning.', 'On Friday.'], passage='GREEN PARK SWIMMING POOL\nMonday – Friday: 7 a.m. – 9 p.m.\nSaturday: 8 a.m. – 1 p.m.\nSunday: closed', text='When is the pool closed?'),
  RQ(['She is ill.', 'She is on holiday.', 'Her train is late.', 'She is in a meeting.'], passage='Hi Tom,\nI’m sorry, I can’t come to work today. I’m ill and I’m staying at home. I can answer emails this afternoon.\nKate', text='Why is Kate not at work?'),
  RQ(['A new intern.', 'A new office.', 'A party.', 'A trip to Lyon.'], passage='To: All staff\nSubject: New colleague\nPlease welcome Emma Martin. She is our new intern. Emma is from Lyon. She speaks French and English.', text='What is the email about?'),
  RQ(['By train.', 'By bus.', 'By car.', 'On foot.'], passage='Dear Sam,\nWe went to Edinburgh last weekend. We took the train from London — it was fast and comfortable! We saw the castle and we ate in a great restaurant.\nAnna', text='How did Anna travel to Edinburgh?'),
  RQ(['A castle.', 'A museum.', 'A park.', 'A shop.'], passage='Dear Sam,\nWe went to Edinburgh last weekend. We took the train from London — it was fast and comfortable! We saw the castle and we ate in a great restaurant.\nAnna', text='What did Anna see?'),
  RQ(['Two.', 'One.', 'Three.', 'Four.'], passage='FOR SALE\nSmall flat in Camden: two bedrooms, one kitchen, one bathroom. Near the Underground station. £1,500 a month. Call 020 7946 0321.', text='How many bedrooms are there?'),
])

PARTS = [P2, P3, P4, P5, P6, P7]
lis = sum(p['count'] for p in PARTS if p['section'] == 'listening')
gra = sum(p['count'] for p in PARTS if p['section'] == 'grammar')
rea = sum(p['count'] for p in PARTS if p['section'] == 'reading')
assert (lis, gra, rea) == (10, 12, 6), (lis, gra, rea)
bank = {
  'slug': 'a1-toeic',
  'level': 'A1',
  'contentVersion': '2026.11.22',
  'notice': 'Questions rédigées par Koto Quest au format du TOEIC Listening & Reading (version abrégée : mêmes parties, consignes en anglais, notation sur 990). Ce ne sont pas des questions officielles d’ETS.',
  'parts': PARTS,
}
json.dump(bank, open(os.path.join(ROOT, 'content/exams/a1-toeic.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
EN = {
  bank['notice']: 'Questions written by Koto Quest in the format of the TOEIC Listening & Reading test (shortened version: same parts, instructions in English, scored out of 990). They are not official ETS questions.',
  'Questions-réponses': 'Question-response', 'Conversations': 'Conversations', 'Annonces': 'Talks',
  'Phrases à compléter': 'Incomplete sentences', 'Textes à compléter': 'Text completion', 'Compréhension écrite': 'Reading comprehension',
}
P_DICT = os.path.join(ROOT, 'content/i18n/en/content.json')
d = json.load(open(P_DICT, encoding='utf-8'))
for k, v in EN.items():
    if k in d and d[k] != v:
        raise SystemExit(f'traduction existante différente : {k} → {d[k]} / {v}')
d.update(EN)
json.dump(d, open(P_DICT, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(f"TOEIC A1 : {sum(len(p['questions']) for p in PARTS)} questions en banque ; examen de {lis} + {gra} + {rea} questions")
