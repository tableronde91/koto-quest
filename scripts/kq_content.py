# Aides communes aux scripts de contenu (français dans le niveau, anglais dans content/i18n/en/content.json).
import json, os

ROOT = os.path.join(os.path.dirname(__file__), '..')
P_DICT = os.path.join(ROOT, 'content/i18n/en/content.json')
DICO = json.load(open(P_DICT, encoding='utf-8'))
EN = {}  # français → anglais (nouvelles traductions)

def t(pair):
    fr, en = pair
    if fr in EN and EN[fr] != en:
        raise SystemExit(f'Traduction contradictoire pour « {fr} » : « {EN[fr]} » / « {en} »')
    EN[fr] = en
    return fr

def item(slug, kind, front, reading, romaji, meaning, kanji=None):
    # Un sens identique à un sens existant garde la même traduction.
    fr = meaning[0]
    meaning = (fr, EN.get(fr) or DICO.get(fr) or meaning[1])
    it = {'slug': slug, 'kind': kind, 'front': front, 'reading': reading, 'romaji': romaji, 'meaning': t(meaning)}
    if kanji:
        on, kun, strokes = kanji
        it['kanji'] = {'onyomi': on, 'kunyomi': kun, 'strokes': strokes}
    return it

def G(slug, front, reading, romaji, meaning): return item(slug, 'grammar', front, reading, romaji, meaning)
def V(slug, front, reading, romaji, meaning): return item(slug, 'vocabulary', front, reading, romaji, meaning)
def K(slug, front, reading, romaji, meaning, on, kun, strokes): return item(slug, 'kanji', front, reading, romaji, meaning, (on, kun, strokes))

def ex(jp, reading, fr, en):
    return {'jp': jp, 'reading': reading, 'fr': t((fr, en))}

def FB(prompt, sentence, choices, answer, expl, tr, kind='fill_blank'):
    assert answer in choices and len(set(choices)) == len(choices), (sentence, answer)
    assert '＿' in sentence, sentence
    return {'type': kind, 'prompt': t(prompt), 'sentence': sentence, 'choices': choices, 'answer': answer, 'explanation': t(expl), 'translation': t(tr)}

def PC(prompt, sentence, choices, answer, expl, tr): return FB(prompt, sentence, choices, answer, expl, tr, 'particle_choice')

def SO(prompt, tokens, expl):
    return {'type': 'sentence_order', 'prompt': t(prompt), 'answer': tokens, 'explanation': t(expl)}

VRAI, FAUX = ('Vrai', 'True'), ('Faux', 'False')
def TF(sentence, claim, answer, expl):
    return {'type': 'true_false', 'prompt': t(('Vrai ou faux ?', 'True or false?')), 'sentence': sentence, 'translation': t(claim), 'choices': [t(VRAI), t(FAUX)], 'answer': t(answer), 'explanation': t(expl)}

def DC(prompt, lines, tr, choices, answer, expl):
    assert answer in choices
    return {'type': 'dialogue_choice', 'prompt': t(prompt), 'lines': [{'speaker': s, 'jp': j} for s, j in lines], 'translation': t(tr), 'choices': choices, 'answer': answer, 'explanation': t(expl)}

def L(slug, title, objective, minutes, explanation, items, examples, exercises):
    return {'slug': slug, 'title': t(title), 'objective': t(objective), 'minutes': minutes, 'explanation': [t(e) for e in explanation], 'items': items, 'examples': examples, 'exercises': exercises}

def CH(slug, title, lessons): return {'slug': slug, 'title': t(title), 'lessons': lessons}

def WORLD(slug, title, region, description, boss, chapters):
    name, glyph, intro = boss
    return {'slug': slug, 'title': t(title), 'region': region, 'description': t(description), 'boss': {'name': t(name), 'glyph': glyph, 'intro': t(intro)}, 'chapters': chapters}

COMPLETE = ('Complète la phrase.', 'Complete the sentence.')
CHOOSE = ('Choisis la forme qui convient.', 'Choose the right form.')

def items_of(level):
    for w in level['worlds']:
        for c in w['chapters']:
            for l in c['lessons']:
                yield from l['items']

def check_and_write(level, path, other_paths):
    """Contrôle doublons et traductions, puis écrit le niveau et le dictionnaire anglais."""
    others = [json.load(open(os.path.join(ROOT, p), encoding='utf-8')) for p in other_paths]
    old = {}
    for o in others:
        for it in items_of(o):
            old[it['slug']] = it
    expr = json.load(open(os.path.join(ROOT, 'content/expressions/expressions.json'), encoding='utf-8'))
    for th in expr['themes']:
        for it in th['expressions']:
            old.setdefault(it['slug'], it)
    problems, seen = [], {}
    new_items = list(items_of(level))
    for it in new_items:
        if it['slug'] in old:
            problems.append(f"slug déjà utilisé dans un autre niveau : {it['slug']}")
        if it['slug'] in seen and seen[it['slug']] != it:
            problems.append(f"slug en double : {it['slug']}")
        seen[it['slug']] = it
        if it['kind'] in ('vocabulary', 'kanji'):
            for o in list(old.values()) + [x for x in seen.values() if x is not it]:
                if o.get('kind') == it['kind'] and o['front'] == it['front'] and o['slug'] != it['slug']:
                    problems.append(f"{it['kind']} déjà présent : {it['front']} ({o['slug']})")
    full = {**DICO, **EN}
    by_en = {}
    for it in list(old.values()) + new_items:
        by_en.setdefault(full.get(it['meaning'], it['meaning']), set()).add(it['meaning'])
    for e, frs in by_en.items():
        if len(frs) > 1 and any(it['meaning'] in frs for it in new_items):
            problems.append(f"sens anglais en double : {e} ← {' | '.join(sorted(frs))}")
    for fr, en in EN.items():
        if fr in DICO and DICO[fr] != en:
            problems.append(f"traduction existante différente : {fr} → {DICO[fr]} / {en}")
    if problems:
        raise SystemExit('\n'.join(sorted(set(problems))))
    json.dump(level, open(os.path.join(ROOT, path), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    DICO.update(EN)
    json.dump(DICO, open(P_DICT, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    lessons = sum(len(c['lessons']) for w in level['worlds'] for c in w['chapters'])
    print(f"{level['level']['code']} : {len(level['worlds'])} îles, {lessons} leçons, {len(seen)} notions ; {len(EN)} traductions")
