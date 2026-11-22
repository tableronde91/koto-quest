# Outils communs aux banques d'examens blancs TOEIC (A2 à C1) : questions d'écoute et de lecture, parties, écriture.
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

def RQ(choices, jp=None, passage=None, text=None):
    q = {'choices': choices, 'answer': choices[0], 'explanation': f'Réponse : {choices[0]}'}
    if jp: q['jp'] = jp
    if passage: q['passage'] = passage
    if text: q['text'] = text
    return q

def P2(count, qs): return part('p2', 'listening', 'Part 2 — Question-Response', 'Questions-réponses', 'You will hear a question or statement. Select the best response.', count, qs, True)
def P3(count, qs): return part('p3', 'listening', 'Part 3 — Conversations', 'Conversations', 'You will hear a short conversation. Answer the question about it.', count, qs, True)
def P4(count, qs): return part('p4', 'listening', 'Part 4 — Talks', 'Annonces', 'You will hear a short talk. Answer the question about it.', count, qs, True)
def P5(count, qs): return part('p5', 'grammar', 'Part 5 — Incomplete Sentences', 'Phrases à compléter', 'A word or phrase is missing in each sentence. Select the best answer to complete the sentence.', count, qs)
def P6(count, qs): return part('p6', 'grammar', 'Part 6 — Text Completion', 'Textes à compléter', 'Read the text. A word or phrase is missing. Select the best answer to complete the text.', count, qs)
def P7(count, qs): return part('p7', 'reading', 'Part 7 — Reading Comprehension', 'Compréhension écrite', 'Read the text and answer the question.', count, qs)

def part(id, section, jpTitle, title, prompt, count, questions, listening=False):
    for q in questions:
        assert len(set(q['choices'])) == len(q['choices']) >= 3, q
        for field in ('jp', 'passage', 'text', 'audio'):
            assert 'é' not in q.get(field, '') and 'è' not in q.get(field, ''), ('accent dans un texte anglais', q)
    assert len(questions) >= count, (id, len(questions), count)
    p = {'id': id, 'section': section, 'jpTitle': jpTitle, 'title': title, 'prompt': prompt, 'count': count, 'questions': questions}
    if listening:
        p['listening'] = True
    return p

def write_bank(code, parts, expected):
    lis = sum(p['count'] for p in parts if p['section'] == 'listening')
    gra = sum(p['count'] for p in parts if p['section'] == 'grammar')
    rea = sum(p['count'] for p in parts if p['section'] == 'reading')
    assert (lis, gra, rea) == expected, (lis, gra, rea)
    bank = {'slug': f'{code.lower()}-toeic', 'level': code, 'contentVersion': '2026.11.22',
            'notice': 'Questions rédigées par Koto Quest au format du TOEIC Listening & Reading (version abrégée : mêmes parties, consignes en anglais, notation sur 990). Ce ne sont pas des questions officielles d’ETS.',
            'parts': parts}
    json.dump(bank, open(os.path.join(ROOT, f'content/exams/{code.lower()}-toeic.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print(f"TOEIC {code} : {sum(len(p['questions']) for p in parts)} questions en banque ; examen de {lis} + {gra} + {rea} questions")

# ── Partie 1 : photos (scènes dessinées, packages/shared/src/toeicScenes.ts) ──
# Quatre phrases lues, une seule décrit la scène ; la première est la bonne.
def PQ(scene, statements):
    assert len(statements) == 4
    return {'image': scene, 'audioChoices': True, 'choices': statements, 'answer': statements[0],
            'explanation': 'Phrases entendues : ' + ' / '.join(statements)}

def P1(count, qs): return part('p1', 'listening', 'Part 1 — Photographs', 'Photos', 'Look at the picture and listen to the four statements. Select the one that best describes the picture.', count, qs, True)

PHOTOS_EASY = [
    PQ('laptop-desk', ['A person is typing on a laptop.', 'A person is opening a window.', 'A person is watering a plant.', 'Two people are eating lunch.']),
    PQ('meeting-chart', ['A woman is pointing at a chart.', 'Two people are standing at the door.', 'A man is writing on the board.', 'The room is empty.']),
    PQ('warehouse-boxes', ['A man is carrying a box.', 'A man is driving a van.', 'Two men are lifting a table.', 'A woman is opening a box.']),
    PQ('cafe-pouring', ['A waiter is pouring coffee.', 'A woman is paying the bill.', 'A man is cooking in the kitchen.', 'Two people are dancing.']),
    PQ('station-platform', ['Two people are waiting on the platform.', 'The passengers are getting off a bus.', 'A woman is buying a ticket.', 'A man is running to the train.']),
    PQ('handshake-entrance', ['Two people are shaking hands.', 'Two people are opening the door.', 'A man is reading a newspaper.', 'A woman is talking on the phone.']),
    PQ('empty-conference', ['There are no people in the room.', 'All the chairs are taken.', 'A man is turning on the screen.', 'A woman is giving a talk.']),
    PQ('park-cyclist', ['A man is riding a bicycle.', 'A man is sitting on a bench.', 'Two people are walking a dog.', 'A woman is cutting a tree.']),
    PQ('shop-checkout', ['A woman is paying at the counter.', 'A man is putting food on the shelves.', 'A woman is trying on a coat.', 'The shop is empty.']),
    PQ('ladder-painting', ['A man is standing on a ladder.', 'A man is washing a car.', 'A man is sitting on the floor.', 'Two people are painting a door.']),
]

PHOTOS_HARD = [
    PQ('laptop-desk', ['Someone is seated in front of a laptop.', 'A window is being cleaned.', 'Some plants are being watered.', 'Documents have been stacked on the floor.']),
    PQ('meeting-chart', ['A presenter is gesturing toward a graph.', 'The participants are leaving the room.', 'A screen is being installed on the wall.', 'Chairs have been stacked in a corner.']),
    PQ('warehouse-boxes', ['A worker is holding a box.', 'A vehicle is being loaded onto a ship.', 'Boxes are being unpacked on a table.', 'The back doors of a van are open.']),
    PQ('cafe-pouring', ['A drink is being poured into a cup.', 'A customer is reading a menu.', 'Chairs have been placed on the tables.', 'A waiter is clearing the table.']),
    PQ('station-platform', ['Some travellers are standing beside their luggage.', 'Passengers are boarding a bus.', 'The platform is crowded with people.', 'Suitcases are being loaded onto a train.']),
    PQ('handshake-entrance', ['Two people are greeting each other at an entrance.', 'A door is being repaired.', 'Some people are waiting in line.', 'A sign is being hung above the door.']),
    PQ('empty-conference', ['Rows of chairs are facing a screen.', 'An audience has gathered in the room.', 'A projector is being carried out.', 'Chairs have been stacked against the wall.']),
    PQ('park-cyclist', ['A cyclist is riding along a path.', 'Some benches are occupied.', 'Trees are being planted in the park.', 'A bicycle has been left by a bench.']),
    PQ('shop-checkout', ['A customer is handing over a card.', 'Shelves are being stocked by an employee.', 'A cashier is wrapping a gift.', 'The store is closed for the day.']),
    PQ('ladder-painting', ['A worker is reaching up toward the wall.', 'A ladder is lying on the ground.', 'Paint is being sprayed onto a window.', 'Tools have been left on a table.']),
]
