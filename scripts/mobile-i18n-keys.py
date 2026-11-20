"""Liste les textes de l'appli mobile (clés T('…') et tables traduites à l'affichage) sans traduction anglaise."""
import json, re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MOBILE = ROOT / 'apps/mobile'
# Textes passés à T() par une variable (tables de libellés)
INDIRECT = ['Kana', 'Vocabulaire', 'Kanji', 'Grammaire', 'kanji', 'notions', 'kana ou mots', 'Victoire', 'Défaite', 'Égalité', 'Annulé',
            'Classé', 'Amical', 'Entraînement', 'Débutant', 'Élémentaire', 'Intermédiaire', 'Avancé', 'Expert',
            'Un petit défi t’attend ⛩️', 'Quelques notions sont sur le point de t’échapper : deux minutes suffisent.',
            'Le gardien s’impatiente 👹', 'Une révision rapide pour garder ta série ?', 'Ton jardin a soif 🌸', 'Arrose tes notions avant qu’elles ne fanent.',
            'Serveur injoignable ({0}). Vérifie que l’API tourne et que le téléphone est sur le même réseau.', 'Une erreur est survenue.',
            'Hiragana', 'Katakana', 'Kanji', 'Expressions', 'Découverte', 'En apprentissage', 'Fragile', 'Maîtrisée', 'À réviser vite', 'Poli', 'Neutre', 'Familier', 'Formel',
            'Courant', 'Rare', 'Épique', 'Courts', 'Longs', 'Chignon', 'En pétard', 'Carré', 'Rasés', 'Ronds', 'Rieurs', 'Sereins', 'Noir', 'Châtain', 'Roux', 'Blond', 'Gris', 'Bleu', 'Étude', 'Régularité', 'Maîtrise', 'Aventure', 'Jeux et collection',
            'Maître du Koto', 'Sensei en herbe', 'Gardien·ne des kanji', 'Lame des kana', 'Voyageur·se des îles', 'Apprenti·e du dojo', 'Vocabulaire', 'Grammaire', 'En fleur', 'En pousse', 'Graines', 'Feuilles fragiles', 'À arroser vite']

def keys():
    out = set(INDIRECT)
    for f in list(MOBILE.glob('app/**/*.tsx')) + list(MOBILE.glob('src/*.ts*')):
        s = f.read_text()
        for m in re.finditer(r"\b(?:T|plural)\(\s*'((?:[^'\\]|\\.)*)'(?:\s*,\s*'((?:[^'\\]|\\.)*)')?(?:\s*,\s*'((?:[^'\\]|\\.)*)')?", s):
            for g in m.groups():
                if g is not None: out.add(g)
    return out

if __name__ == '__main__':
    d = {}
    for n in ['ui', 'engine', 'api', 'content', 'mobile']:
        d.update({k: v for k, v in json.loads((ROOT / f'content/i18n/en/{n}.json').read_text()).items() if v})
    missing = sorted(k for k in keys() if k not in d and re.search(r'[A-Za-zÀ-ÿ]', k) and k not in ('points',) or (k == 'points' and k not in d))
    json.dump(missing, sys.stdout, ensure_ascii=False, indent=1)
