# Outils communs aux banques d'examen Goethe-Zertifikat (A2 et au-delà) : questions d'écoute, de lecture, parties et écriture du fichier.
# Dans chaque question, le premier choix est la bonne réponse (l'ordre est mélangé à chaque examen).
import json, os
ROOT = os.path.join(os.path.dirname(__file__), '..')
WHO = {'N': 'Narrateur', 'M': 'Homme', 'F': 'Femme'}
R, F = ['Richtig', 'Falsch'], ['Falsch', 'Richtig']

def LQ(audio, choices, text=None):
    """Hören : document sonore (lignes « N|… », « M|… », « F|… ») ; `text` est l'affirmation ou la question affichée."""
    lines = [l.strip() for l in audio.strip().split('\n') if l.strip()]
    for l in lines:
        assert l[1] == '|' and l[0] in WHO, l
    q = {'audio': '\n'.join(lines), 'choices': list(choices), 'answer': choices[0],
         'explanation': 'Transcription : ' + ' / '.join(f"{WHO[l[0]]} : {l[2:]}" for l in lines)}
    if text:
        q['text'] = '★ ' + text
    return q

def RQ(choices, text, expl=None):
    return {'choices': list(choices), 'answer': choices[0], 'explanation': expl or f'Réponse : {choices[0]}', 'text': text}

def RP(passage, question, choices):
    """Lesen : un texte, une question ★."""
    q = RQ(choices, '★ ' + question)
    q['passage'] = passage
    return q

def PART(id, section, jpTitle, title, prompt, count, questions, listening=False):
    for q in questions:
        assert 2 <= len(set(q['choices'])) == len(q['choices']) <= 4, q
    assert len(questions) >= count, id
    p = {'id': id, 'section': section, 'jpTitle': jpTitle, 'title': title, 'prompt': prompt, 'count': count, 'questions': questions}
    if listening:
        p['listening'] = True
    return p

def write_bank(code, parts, expected, notice, notice_en, titles_en):
    """Écrit content/exams/<code>.json et les traductions anglaises des titres. `expected` = (écoute, lecture, écriture)."""
    got = tuple(sum(p['count'] for p in parts if p['section'] == s) for s in ('listening', 'reading', 'writing'))
    assert got == expected, got
    bank = {'slug': code.lower(), 'level': code, 'contentVersion': '2026.11.27', 'notice': notice, 'parts': parts}
    json.dump(bank, open(os.path.join(ROOT, f'content/exams/{code.lower()}.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    p_dict = os.path.join(ROOT, 'content/i18n/en/content.json')
    d = json.load(open(p_dict, encoding='utf-8'))
    en = {notice: notice_en, **titles_en}
    for p in parts:
        assert p['title'] in en or p['title'] in d, 'titre sans traduction : ' + p['title']
    for k, v in en.items():
        if k in d and d[k] != v:
            raise SystemExit(f'traduction existante différente : {k} → {d[k]} / {v}')
    d.update(en)
    json.dump(d, open(p_dict, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print(f"{code} : {sum(len(p['questions']) for p in parts)} questions en banque ; examen de {got[0]} + {got[1]} + {got[2]} questions")
