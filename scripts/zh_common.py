# Outils communs aux niveaux de chinois (HSK 1 à 6) : notions, exemples, consignes, examen final,
# écriture du niveau et de l'onglet Hanzi (content/characters/hanzi.json).
# Le pinyin (avec les tons) sert de lecture : il s'affiche au-dessus des caractères, comme les furigana.
import os, sys, json
sys.path.insert(0, os.path.dirname(__file__))
from kq_content import *

def Z(slug, front, pinyin, meaning):
    """Mot chinois : caractères, pinyin et sens."""
    return V('zh-' + slug, front, pinyin, None, meaning)

def ZG(slug, front, pinyin, meaning):
    """Point de grammaire chinois (le pinyin peut être None pour une structure)."""
    return G('gram-zh-' + slug, front, pinyin, None, meaning)

def H(slug, char, pinyin, meaning, strokes):
    """Caractère (hanzi) : notion de type « kanji » lue en pinyin, sans on'yomi ni kun'yomi."""
    return K('hz-' + slug, char, pinyin, None, meaning, [], [], strokes)

def x(zh, pinyin, fr, en):
    """Exemple : phrase chinoise, son pinyin (affiché dessous) et sa traduction."""
    return ex(zh, pinyin, fr, en)

def HL(slug, title, objective, explanation, items, minutes=5):
    """Leçon de caractères : uniquement des hanzi, les questions sont générées (sens, pinyin, reconnaissance)."""
    return L(slug, title, objective, minutes, explanation, items, [], [])

COMPLETE = ('Complète la phrase.', 'Complete the sentence.')
CHOOSE = ('Choisis le mot qui convient.', 'Choose the right word.')
ANSWER = ('Que réponds-tu ?', 'What do you answer?')
ORDER = lambda fr, en: (f'Remets dans l’ordre : « {fr} »', f'Put in order: “{en}”')

ALL_LEVELS = ['content/n5/n5.json', 'content/n4/n4.json', 'content/n3/n3.json', 'content/n2/n2.json', 'content/n1/n1.json',
  'content/topik1/topik1.json', 'content/topik2/topik2.json', 'content/topik3/topik3.json', 'content/topik4/topik4.json',
  'content/topik5/topik5.json', 'content/topik6/topik6.json',
  'content/a1/a1.json', 'content/a2/a2.json', 'content/b1/b1.json', 'content/b2/b2.json', 'content/c1/c1.json']
HSK_PATHS = [f'content/hsk{n}/hsk{n}.json' for n in range(1, 7)]

def FINAL(n, region, title, total, passmark, parts_fr, parts_en):
    return {
      'slug': f'hsk{n}-final', 'title': t(title), 'region': region,
      'description': t((f'Examen blanc au format du HSK {n}, en chinois : {parts_fr}. Noté sur {total} ; réussite à {passmark} points.',
                        f'Mock exam in HSK {n} format, in Chinese: {parts_en}. Marked out of {total}; pass mark {passmark} points.')),
      'exam': f'hsk{n}-official', 'chapters': [],
    }

def hanzi_groups(worlds):
    """Groupes de l'onglet Hanzi : une ligne par leçon de caractères du niveau, dans l'ordre du parcours."""
    out = []
    for w in worlds:
        for c in w['chapters']:
            for l in c['lessons']:
                hz = [it for it in l['items'] if it['kind'] == 'kanji']
                if hz and len(hz) == len(l['items']):
                    out.append({'slug': 'hzg-' + l['slug'], 'title': l['title'], 'items': hz})
    return out

def write_level(n, title, region, region_en, worlds, notice=None):
    code = f'HSK{n}'
    level = {
      'contentVersion': '2026.11.22',
      'level': {'code': code, 'title': t(title), 'region': region, 'order': 47 - n},
      'notice': t(notice or (f'Les listes de vocabulaire de Koto Quest suivent le programme du HSK {n} (HSK 2.0, utilisé aux sessions de 2026) mais ne sont pas des listes officielles du Centre for Language Education and Cooperation (CLEC).',
                             f'Koto Quest’s vocabulary lists follow the HSK {n} syllabus (HSK 2.0, used in the 2026 sessions) but are not official lists of the Centre for Language Education and Cooperation (CLEC).')),
      'worlds': worlds,
    }
    t((region, region_en))
    os.makedirs(os.path.join(ROOT, f'content/hsk{n}'), exist_ok=True)
    earlier = [p for p in HSK_PATHS[: n - 1] if os.path.exists(os.path.join(ROOT, p))]
    # Section de l'onglet Hanzi pour ce niveau
    p_cat = os.path.join(ROOT, 'content/characters/hanzi.json')
    cat = json.load(open(p_cat, encoding='utf-8'))
    sec_title = t((f'HSK {n}', f'HSK {n}'))
    groups = hanzi_groups(worlds)
    section = {'slug': f'hanzi-hsk{n}', 'glyph': '字', 'title': sec_title,
               'description': t((f'Les caractères du HSK {n} vus dans le parcours, avec leur pinyin et leur sens. Même caractère, même maîtrise que dans les leçons.',
                                 f'The HSK {n} characters seen in the path, with their pinyin and meaning. Same character, same mastery as in the lessons.')),
               'groups': groups}
    cat['sections'] = sorted([s for s in cat['sections'] if s['slug'] != section['slug']] + [section], key=lambda s: s['slug'])
    cat['notice'] = t(('Pinyin avec les tons (ā á ǎ à). Les caractères sont présentés en écriture simplifiée, celle du HSK et de la Chine continentale.',
                       'Pinyin with tone marks (ā á ǎ à). Characters are shown in simplified script, as used in the HSK and in mainland China.'))
    cat['contentVersion'] = '2026.11.22'
    check_and_write(level, f'content/hsk{n}/hsk{n}.json', ALL_LEVELS + earlier, earlier)
    json.dump(cat, open(p_cat, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print('Hanzi :', sum(len(g['items']) for g in groups), 'caractères')
