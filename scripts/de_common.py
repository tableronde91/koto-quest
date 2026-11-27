# Outils communs aux niveaux d'allemand (Goethe-Zertifikat A1 à C2) : notions, exemples, consignes, examen final et écriture du niveau.
# Les notions sont en allemand (front) avec leur sens en français ; la traduction anglaise du sens sert à l'interface en anglais.
import os, sys, json
sys.path.insert(0, os.path.dirname(__file__))
from kq_content import *
import kq_content

def t(pair):
    """Comme kq_content.t, mais un texte français déjà traduit garde sa traduction anglaise existante."""
    fr, en = pair
    en = DICO.get(fr, kq_content.EN.get(fr, en))
    kq_content.EN[fr] = en
    return fr
kq_content.t = t

# Niveaux d'allemand déjà écrits (contrôle des graphies en double dans la même langue)
GOETHE_PATHS = [f'content/goethe{c}/goethe{c}.json' for c in ('a1', 'a2', 'b1', 'b2', 'c1', 'c2')]
OTHER_LEVELS = ['content/n5/n5.json', 'content/n4/n4.json', 'content/n3/n3.json', 'content/n2/n2.json', 'content/n1/n1.json',
  'content/topik1/topik1.json', 'content/topik2/topik2.json', 'content/topik3/topik3.json', 'content/topik4/topik4.json',
  'content/topik5/topik5.json', 'content/topik6/topik6.json',
  'content/a1/a1.json', 'content/a2/a2.json', 'content/b1/b1.json', 'content/b2/b2.json', 'content/c1/c1.json'] + \
  [f'content/hsk{n}/hsk{n}.json' for n in range(1, 7)] + [f'content/dele{c}/dele{c}.json' for c in ('a1', 'a2', 'b1', 'b2', 'c1', 'c2')]

# Sens déjà pris par une notion d'un autre niveau : anglais → français. Un même sens anglais ne peut pas
# traduire deux sens français différents (voir check_and_write) : on reprend alors le libellé français existant.
_TAKEN = {}
ADOPTED = []
def _load_taken(current):
    paths = [p for p in OTHER_LEVELS + GOETHE_PATHS if p != current and os.path.exists(os.path.join(ROOT, p))]
    for p in paths:
        for it in items_of(json.load(open(os.path.join(ROOT, p), encoding='utf-8'))):
            _TAKEN.setdefault(DICO.get(it['meaning'], it['meaning']), it['meaning'])
    for th in json.load(open(os.path.join(ROOT, 'content/expressions/expressions.json'), encoding='utf-8'))['themes']:
        for it in th['expressions']:
            _TAKEN.setdefault(DICO.get(it['meaning'], it['meaning']), it['meaning'])

def _meaning(meaning):
    fr, en = meaning
    if fr in DICO:
        if DICO[fr] != en: ADOPTED.append(f'traduction reprise : {fr} → {DICO[fr]} (au lieu de {en})')
        en = DICO[fr]
    elif fr in kq_content.EN:
        en = kq_content.EN[fr]
    other = _TAKEN.get(en)
    if other and other != fr:
        ADOPTED.append(f'sens repris : {fr} → {other} ({en})')
        return (other, DICO.get(other, en))
    _TAKEN[en] = fr
    return (fr, en)

def D(slug, front, meaning):
    """Mot ou expression allemande (pas de lecture : la prononciation s'explique dans les leçons)."""
    return V('de-' + slug, front, None, None, _meaning(meaning))

def DG(slug, front, meaning):
    """Point de grammaire allemand."""
    return G('gram-de-' + slug, front, None, None, _meaning(meaning))

def x(de, fr, en):
    """Exemple : phrase allemande, sa traduction française et sa version anglaise (interface en anglais)."""
    return ex(de, None, fr, en)

COMPLETE = ('Complète la phrase.', 'Complete the sentence.')
CHOOSE = ('Choisis la forme qui convient.', 'Choose the right form.')
ANSWER = ('Que réponds-tu ?', 'What do you answer?')

def order(fr_en, words, expl):
    """Phrase à remettre dans l'ordre (les mots allemands, séparés par des espaces)."""
    return SO(fr_en, words, expl)

def FINAL(code, region, title, parts_fr, parts_en):
    cefr = code[6:]
    return {
      'slug': f'{code.lower()}-final', 'title': t(title), 'region': region,
      'description': t((f'Examen blanc au format du Goethe-Zertifikat {cefr}, en allemand : {parts_fr}. Noté sur 100 ; réussite à partir de 60 points.',
                        f'Mock exam in Goethe-Zertifikat {cefr} format, in German: {parts_en}. Marked out of 100; pass from 60 points.')),
      'exam': f'{code.lower()}-official', 'chapters': [],
    }

def begin(code):
    """À appeler avant de déclarer les notions du niveau : charge les sens déjà pris ailleurs."""
    _load_taken(f'content/{code.lower()}/{code.lower()}.json')

def write_level(code, title, region, region_en, order_, worlds):
    cefr = code[6:]
    level = {
      'contentVersion': '2026.11.27',
      'level': {'code': code, 'title': t(title), 'region': region, 'order': order_},
      'notice': t((f'Les listes de vocabulaire de Koto Quest suivent les compétences du niveau {cefr} du CECRL et préparent au Goethe-Zertifikat {cefr}, mais ne sont pas des listes officielles du Goethe-Institut.',
                   f'Koto Quest’s vocabulary lists follow the CEFR {cefr} skills and prepare for the Goethe-Zertifikat {cefr}, but they are not official Goethe-Institut lists.')),
      'worlds': worlds,
    }
    t((region, region_en))
    path = f'content/{code.lower()}/{code.lower()}.json'
    os.makedirs(os.path.join(ROOT, f'content/{code.lower()}'), exist_ok=True)
    earlier = [p for p in GOETHE_PATHS if p != path and os.path.exists(os.path.join(ROOT, p))]
    for a in ADOPTED: print(' ·', a)
    check_and_write(level, path, OTHER_LEVELS + earlier, earlier)
