# Outils communs aux niveaux d'anglais (A2 à C1) : notions, exemples, consignes, examen final et écriture du niveau.
import os, sys, json
sys.path.insert(0, os.path.dirname(__file__))
from kq_content import *

def E(slug, front, meaning):
    """Mot ou expression anglaise (pas de lecture ni de romaji)."""
    return V('en-' + slug, front, None, None, meaning)

def EG(slug, front, meaning):
    return G('gram-en-' + slug, front, None, None, meaning)

def x(en, fr, en_tr=None):
    """Exemple : phrase anglaise et sa traduction française (la version anglaise de l'interface reprend la phrase)."""
    return ex(en, None, fr, en_tr or en)

COMPLETE = ('Complète la phrase.', 'Complete the sentence.')
CHOOSE = ('Choisis la forme qui convient.', 'Choose the right form.')
ANSWER = ('Que réponds-tu ?', 'What do you answer?')
order = SO

PREVIOUS = ['content/n5/n5.json', 'content/n4/n4.json', 'content/n3/n3.json', 'content/n2/n2.json', 'content/n1/n1.json',
  'content/topik1/topik1.json', 'content/topik2/topik2.json', 'content/topik3/topik3.json', 'content/topik4/topik4.json',
  'content/topik5/topik5.json', 'content/topik6/topik6.json', 'content/a1/a1.json']

def FINAL(code, region, title, score):
    return {
      'slug': f'{code.lower()}-final', 'title': t(title), 'region': region,
      'description': t((f'Examen blanc au format du TOEIC Listening & Reading, en anglais : questions-réponses, conversations et annonces, phrases et textes à compléter, compréhension écrite. Noté sur 990 ; objectif {code} à {score} points.',
                        f'Mock exam in TOEIC Listening & Reading format, in English: question-response, conversations and talks, incomplete sentences and texts, reading comprehension. Marked out of 990; {code} target at {score} points.')),
      'exam': f'{code.lower()}-toeic', 'chapters': [],
    }

def write_level(code, title, region, region_en, order_, worlds, previous):
    level = {
      'contentVersion': '2026.11.22',
      'level': {'code': code, 'title': t(title), 'region': region, 'order': order_},
      'notice': t((f'Les listes de vocabulaire de Koto Quest suivent les compétences du niveau {code} du CECRL et préparent au TOEIC Listening & Reading, mais ne sont pas des listes officielles d’ETS.',
                   f'Koto Quest’s vocabulary lists follow the CEFR {code} skills and prepare for the TOEIC Listening & Reading test, but they are not official ETS lists.')),
      'worlds': worlds,
    }
    t((region, region_en))
    os.makedirs(os.path.join(ROOT, f'content/{code.lower()}'), exist_ok=True)
    check_and_write(level, f'content/{code.lower()}/{code.lower()}.json', previous)
