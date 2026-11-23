# Romanisation des contes (option de lecture « rōmaji / romanisation / pinyin ») :
# ajoute à chaque phrase japonaise et coréenne de content/reading/stories.json un champ `roman`.
#   - japonais : Hepburn, mot par mot (fugashi + UniDic), en suivant les furigana du conte pour la lecture
#     des kanji (les noms propres gardent la lecture choisie par le conte) ; particules は / へ / を → wa / e / o ;
#   - coréen : romanisation révisée (korean-romanizer), avec l'assimilation des nasales et des liquides ;
#   - chinois : le pinyin complet est écrit par scripts/zh-reading.py (pinyin des mots du conte).
# Dépendances (outils de contenu uniquement) : pip install cutlet unidic-lite korean-romanizer pypinyin
# Usage : python3 scripts/reading_roman.py   (appelé aussi par gen-reading.py et ko-reading.py)
import json, os, re

ROOT = os.path.join(os.path.dirname(__file__), '..')
P = os.path.join(ROOT, 'content/reading/stories.json')

_katsu = None
def _cutlet():
    global _katsu
    if _katsu is None:
        import cutlet
        _katsu = cutlet.Cutlet()
        _katsu.use_foreign_spelling = False
    return _katsu

PUNCT = {'、': ',', '。': '.', '「': '“', '」': '”', '『': '“', '』': '”', '！': '!', '？': '?', '：': ':', '（': '(', '）': ')', '…': '…', '―': '—', '・': ' ', '　': ' '}
OPEN, CLOSE = set('“('), set(',.!?:)”…')

def _segments(jp):
    """{漢字|かな} → [(surface, kana or None)]"""
    out, i = [], 0
    for m in re.finditer(r'\{([^|}]*)\|([^}]*)\}', jp):
        if m.start() > i:
            out.extend((c, None) for c in jp[i:m.start()])
        out.append((m.group(1), m.group(2)))
        i = m.end()
    out.extend((c, None) for c in jp[i:])
    return out

_BASE = dict(zip(
    'あいうえおかきくけこさしすせそたちつてとなにぬねのはひふへほまみむめもやゆよらりるれろわをんがぎぐげござじずぜぞだぢづでどばびぶべぼぱぴぷぺぽぁぃぅぇぉゔ',
    'a i u e o ka ki ku ke ko sa shi su se so ta chi tsu te to na ni nu ne no ha hi fu he ho ma mi mu me mo ya yu yo ra ri ru re ro wa o n ga gi gu ge go za ji zu ze zo da ji zu de do ba bi bu be bo pa pi pu pe po a i u e o vu'.split()))
_SMALL_Y = {'ゃ': 'a', 'ゅ': 'u', 'ょ': 'o'}

def _kana_romaji(kana):
    """Kana → Hepburn (っ redouble la consonne suivante, ん → n’ devant voyelle, ー allonge la voyelle)."""
    h = ''.join(chr(ord(c) - 0x60) if 'ァ' <= c <= 'ヶ' else c for c in kana)
    out, i, gem = [], 0, False
    while i < len(h):
        c = h[i]
        if c == 'っ':
            gem = True; i += 1; continue
        if c == 'ー':
            if out and out[-1][-1:] in 'aeiou':
                out.append(out[-1][-1])
            i += 1; continue
        r = _BASE.get(c)
        if r is None:
            out.append(c); i += 1; gem = False; continue
        if i + 1 < len(h) and h[i + 1] in _SMALL_Y and r.endswith('i') and c not in 'い':
            stem = r[:-1]
            r = (stem if stem in ('sh', 'ch', 'j') else stem + 'y') + _SMALL_Y[h[i + 1]]
            i += 1
        if c == 'ん' and i + 1 < len(h) and (_BASE.get(h[i + 1], 'x')[0] in 'aeiouy'):
            r = "n'"
        if gem:
            r = ('t' + r) if r.startswith('ch') else (r[0] + r)
            gem = False
        out.append(r); i += 1
    return ''.join(out)

def romaji(jp):
    k = _cutlet()
    segs = _segments(jp)
    plain = ''.join(s for s, _ in segs)
    group_of, readings = [], []
    for g, (surface, kana) in enumerate(segs):
        for _ in surface:
            group_of.append(g)
        readings.append(kana if kana is not None else surface)
    # Découpage en mots ; un mot qui coupe un groupe annoté est fusionné avec le précédent
    words, start = [], 0
    for tok in k.tagger(plain):
        surf = tok.surface
        idx = plain.find(surf, start)
        if idx < 0:
            continue
        end = idx + len(surf)
        groups = sorted(set(group_of[idx:end]))
        f = tok.feature
        shared = set(groups) & set(words[-1]['groups']) if words else set()
        if shared and any(segs[g][1] is not None for g in shared):
            w = words[-1]
            w['groups'], w['surface'] = sorted(set(w['groups']) | set(groups)), w['surface'] + surf
        else:
            words.append({'groups': groups, 'pos1': f.pos1, 'pos2': f.pos2, 'surface': surf})
        start = end
    for w in words:
        w['kana'] = w['surface'] if all(segs[g][1] is None for g in w['groups']) else ''.join(readings[g] for g in w['groups'])
    # Regroupement : préfixe + mot, mot + auxiliaires / suffixes / て・で (la romanisation se fait sur le groupe entier)
    chunks = []
    for w in words:
        surf, pos1 = w['surface'], w['pos1']
        if all(c in PUNCT for c in surf):
            chunks.append({'kind': 'p', 'text': ''.join(PUNCT[c] for c in surf)}); continue
        if pos1 == '助詞' and surf in ('は', 'へ', 'を'):
            chunks.append({'kind': 'w', 'text': {'は': 'wa', 'へ': 'e', 'を': 'o'}[surf]}); continue
        prev = chunks[-1] if chunks and chunks[-1]['kind'] == 'w' and 'kana' in chunks[-1] else None
        copula = pos1 == '助動詞' and surf[:1] in ('で', 'だ')
        glue = prev is not None and (
            prev.get('prefix')
            or pos1 == '接尾辞'
            or (pos1 == '助動詞' and not (copula and prev['pos1'] in ('名詞', '代名詞', '形状詞')))
            or (pos1 == '助詞' and w['pos2'] == '接続助詞' and surf in ('て', 'で')))
        if glue:
            prev['kana'] += w['kana']; prev['prefix'] = pos1 == '接頭辞'
            prev['pos1'] = pos1 if not prev.get('prefix') else prev['pos1']
            continue
        chunks.append({'kind': 'w', 'kana': w['kana'], 'pos1': pos1, 'proper': w['pos2'] == '固有名詞', 'prefix': pos1 == '接頭辞'})
    text = ''
    for ch in chunks:
        if ch['kind'] == 'p':
            r = ch['text']
            if r[0] in OPEN:
                text += (' ' if text and not text.endswith(' ') else '') + r
            else:
                text = text.rstrip() + r + ' '
            continue
        r = ch['text'] if 'text' in ch else _kana_romaji(ch['kana'])
        if ch.get('proper'):
            r = r[:1].upper() + r[1:]
        if text and not text.endswith((' ', '“', '(')):
            text += ' '
        text += r + ' '
    text = re.sub(r'\s+', ' ', text).strip()
    text = re.sub(r' ([,.!?:)”])', r'\1', text)
    text = re.sub(r'(^|[.!?“]\s*)[Dd]e mo\b', lambda m: m.group(1) + 'demo', text)
    return _sentence_case(text)

def _sentence_case(text):
    return re.sub(r'(^|[.!?]\s+|“)([a-z])', lambda m: m.group(1) + m.group(2).upper(), text)

def revised(hangul):
    from korean_romanizer.romanizer import Romanizer
    r = Romanizer(hangul).romanize()
    for a, b in (('「', '“'), ('」', '”'), ('『', '“'), ('』', '”'), ('…', '…')):
        r = r.replace(a, b)
    r = re.sub(r'(?<=[aeiouy])lr(?=[aeiouwy])', 'll', r)
    # Assimilation que la bibliothèque n'applique pas : occlusive finale devant ㄴ / ㅁ (옛날 → yennal, 합니다 → hamnida)
    for a, b in (('tn', 'nn'), ('tm', 'nm'), ('kn', 'ngn'), ('km', 'ngm'), ('pn', 'mn'), ('pm', 'mm'), ('nr', 'll'), ('ln', 'll')):
        r = re.sub(rf'(?<=[aeiouy]){a}(?=[aeiouwy])', b, r)
    return _sentence_case(r)

def add_roman(data):
    for s in data['stories']:
        lv = s['level']
        lang = 'ja' if re.match(r'^N\d$', lv) else 'ko' if lv.startswith('TOPIK') else None
        if not lang:
            continue
        for c in s['chapters']:
            for para in c['paragraphs']:
                for sent in para:
                    sent['roman'] = romaji(sent['jp']) if lang == 'ja' else revised(sent['kana'])
    return data

if __name__ == '__main__':
    data = json.load(open(P, encoding='utf-8'))
    add_roman(data)
    json.dump(data, open(P, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    n = sum(1 for s in data['stories'] for c in s['chapters'] for p in c['paragraphs'] for x in p if 'roman' in x)
    print(f'Romanisation : {n} phrases')
