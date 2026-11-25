# Lecture des kanji isolés dans les niveaux JLPT et l'onglet Caractères.
# Un kanji appris avec un mot à okurigana (長 avec 長い) gardait la lecture du mot entier (ながい, nagai) :
# sa carte répétait celle du mot. On note désormais la partie en kana entre parenthèses, comme les dictionnaires
# (なが(い), naga(i)) ; les scripts de contenu font de même (kq_content.kanji_reading).
# Corrige aussi deux romanisations de l'onglet Caractères (火 « ka-hi », 気 « ki-ki ») et aligne 雨 sur le N4.
# Idempotent. Usage : python3 scripts/kanji-readings.py
import json, os, sys
sys.path.insert(0, os.path.dirname(__file__))
from kq_content import kanji_reading

ROOT = os.path.join(os.path.dirname(__file__), '..')
FILES = ['content/n5/n5.json', 'content/n4/n4.json', 'content/n3/n3.json', 'content/n2/n2.json', 'content/n1/n1.json', 'content/characters/characters.json']
FIXES = {'kanji-ka-hi': {'romaji': 'hi'}, 'kanji-ki-ki': {'romaji': 'ki'}}

def kanji_items(o):
    if isinstance(o, dict):
        if o.get('kind') == 'kanji' and 'front' in o and 'kanji' in o:
            yield o
        for v in o.values():
            yield from kanji_items(v)
    elif isinstance(o, list):
        for v in o:
            yield from kanji_items(v)

docs = {p: json.load(open(os.path.join(ROOT, p), encoding='utf-8')) for p in FILES}
# Même slug = même notion : la version des niveaux sert de référence pour l'onglet Caractères.
levels = {it['slug']: it for p, d in docs.items() if 'characters' not in p for it in kanji_items(d)}
changed = 0
for p, d in docs.items():
    for it in kanji_items(d):
        before = json.dumps(it, ensure_ascii=False, sort_keys=True)
        it.update(FIXES.get(it['slug'], {}))
        ref = levels.get(it['slug'])
        if 'characters' in p and ref is not None and ref['kanji']['kunyomi'] != it['kanji']['kunyomi'] and set(it['kanji']['kunyomi']) <= set(ref['kanji']['kunyomi']):
            it['kanji']['kunyomi'] = list(ref['kanji']['kunyomi'])
        it['reading'], it['romaji'] = kanji_reading(it['reading'], it['romaji'], it['kanji']['kunyomi'])
        if json.dumps(it, ensure_ascii=False, sort_keys=True) != before:
            changed += 1
    # Garde la mise en forme de chaque fichier (n5 et l'onglet Caractères : indentation de 2).
    indent = 2 if p in ('content/n5/n5.json', 'content/characters/characters.json') else 1
    json.dump(d, open(os.path.join(ROOT, p), 'w', encoding='utf-8'), ensure_ascii=False, indent=indent)
print(f'Lectures des kanji : {changed} notion(s) mise(s) à jour')
