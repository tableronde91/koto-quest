# Outils communs aux niveaux d'espagnol (DELE A1 à C2) : notions, exemples, consignes, examen final et écriture du niveau.
# Les notions sont en espagnol (front) avec leur sens en français ; la traduction anglaise du sens sert à l'interface en anglais.
import os, sys, json
sys.path.insert(0, os.path.dirname(__file__))
from kq_content import *

def S(slug, front, meaning):
    """Mot ou expression espagnole (pas de lecture : l'espagnol se lit comme il s'écrit)."""
    return V('es-' + slug, front, None, None, meaning)

def SG(slug, front, meaning):
    """Point de grammaire espagnol."""
    return G('gram-es-' + slug, front, None, None, meaning)

def x(es, fr, en):
    """Exemple : phrase espagnole, sa traduction française et sa version anglaise (interface en anglais)."""
    return ex(es, None, fr, en)

COMPLETE = ('Complète la phrase.', 'Complete the sentence.')
CHOOSE = ('Choisis la forme qui convient.', 'Choose the right form.')
ANSWER = ('Que réponds-tu ?', 'What do you answer?')

def order(fr_en, words, expl):
    """Phrase à remettre dans l'ordre (les mots espagnols, séparés par des espaces)."""
    return SO(fr_en, words, expl)

# Niveaux d'espagnol déjà écrits (contrôle des graphies en double dans la même langue)
DELE_PATHS = [f'content/dele{c}/dele{c}.json' for c in ('a1', 'a2', 'b1', 'b2', 'c1', 'c2')]
OTHER_LEVELS = ['content/n5/n5.json', 'content/n4/n4.json', 'content/n3/n3.json', 'content/n2/n2.json', 'content/n1/n1.json',
  'content/topik1/topik1.json', 'content/topik2/topik2.json', 'content/topik3/topik3.json', 'content/topik4/topik4.json',
  'content/topik5/topik5.json', 'content/topik6/topik6.json',
  'content/a1/a1.json', 'content/a2/a2.json', 'content/b1/b1.json', 'content/b2/b2.json', 'content/c1/c1.json'] + \
  [f'content/hsk{n}/hsk{n}.json' for n in range(1, 7)]

def FINAL(code, region, title, parts_fr, parts_en):
    cefr = code[4:]
    return {
      'slug': f'{code.lower()}-final', 'title': t(title), 'region': region,
      'description': t((f'Examen blanc au format du DELE {cefr}, en espagnol : {parts_fr}. Noté sur 100 ; réussite avec au moins 30 points dans chacun des deux groupes d’épreuves.',
                        f'Mock exam in DELE {cefr} format, in Spanish: {parts_en}. Marked out of 100; pass with at least 30 points in each of the two groups of tests.')),
      'exam': f'{code.lower()}-official', 'chapters': [],
    }

def write_level(code, title, region, region_en, order_, worlds):
    cefr = code[4:]
    level = {
      'contentVersion': '2026.11.23',
      'level': {'code': code, 'title': t(title), 'region': region, 'order': order_},
      'notice': t((f'Les listes de vocabulaire de Koto Quest suivent les compétences du niveau {cefr} du CECRL et préparent au DELE {cefr}, mais ne sont pas des listes officielles de l’Instituto Cervantes.',
                   f'Koto Quest’s vocabulary lists follow the CEFR {cefr} skills and prepare for the DELE {cefr}, but they are not official Instituto Cervantes lists.')),
      'worlds': worlds,
    }
    t((region, region_en))
    path = f'content/{code.lower()}/{code.lower()}.json'
    os.makedirs(os.path.join(ROOT, f'content/{code.lower()}'), exist_ok=True)
    earlier = [p for p in DELE_PATHS if p != path and os.path.exists(os.path.join(ROOT, p))]
    check_and_write(level, path, OTHER_LEVELS + earlier, earlier)
