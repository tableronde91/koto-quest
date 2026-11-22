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
