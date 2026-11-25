# Île « Maîtrise des katakana » du N5 : les 46 katakana de base, comme l'île des hiragana.
# Elle n'avait que アイウエオ et カキクケコ ; on ajoute les lignes S, T, N, H, M, Y/W/ン et R, en 4 chapitres.
# Les notions reprennent celles de l'onglet Caractères (même slug = même notion = maîtrise partagée).
# Idempotent. Usage : python3 scripts/n5-katakana.py
import json, os

ROOT = os.path.join(os.path.dirname(__file__), '..')
P_N5 = os.path.join(ROOT, 'content/n5/n5.json')
P_CHARS = os.path.join(ROOT, 'content/characters/characters.json')
P_DICT = os.path.join(ROOT, 'content/i18n/en/content.json')

n5 = json.load(open(P_N5, encoding='utf-8'))
chars = json.load(open(P_CHARS, encoding='utf-8'))
dico = json.load(open(P_DICT, encoding='utf-8'))
KATA = {it['front']: it for s in chars['sections'] if s['slug'] == 'katakana' for g in s['groups'] for it in g['items']}
EN = {}

def t(fr, en):
    # Un texte déjà traduit garde sa traduction.
    EN[fr] = dico.get(fr, en)
    return fr

def items(row):
    return [{k: KATA[c][k] for k in ('slug', 'kind', 'front', 'reading', 'romaji', 'meaning')} for c in row]

def ex(jp, reading, fr, en):
    return {'jp': jp, 'reading': reading, 'fr': t(fr, en)}

def read(word, choices, expl):
    assert choices[0] not in choices[1:]
    return {'type': 'fill_blank', 'prompt': t('Comment se lit ce mot ?', 'How is this word read?'), 'sentence': word, 'choices': choices, 'answer': choices[0], 'explanation': t(*expl)}

def lesson(slug, row, explanation, examples, exercises, minutes=6):
    return {
        'slug': slug,
        'title': t(f'Katakana : {row}', f'Katakana: {row}'),
        'objective': t(f'Lire et reconnaître {row}.', f'Read and recognise {row}.'),
        'minutes': minutes,
        'explanation': [t(fr, en) for fr, en in explanation],
        'items': items(row),
        'examples': examples,
        'exercises': exercises,
    }

SA = lesson('n5-kata-sa', 'サシスセソ', [
    ('シ (shi) et ツ (tsu) se ressemblent : les deux petits traits de シ sont presque horizontaux et son grand trait remonte vers la droite ; ceux de ツ sont presque verticaux et son grand trait descend.',
     'シ (shi) and ツ (tsu) look alike: the two short strokes of シ are almost horizontal and its long stroke sweeps up to the right; those of ツ are almost vertical and its long stroke comes down.'),
    ('De même, ソ (so) a un petit trait presque vertical, alors que celui de ン (n) est presque horizontal. Écoute chaque caractère, puis entraîne-toi à le reconnaître.',
     'Likewise, ソ (so) has an almost vertical short stroke, whereas that of ン (n) is almost horizontal. Listen to each character, then practise recognising it.'),
  ], [ex('アイス', 'あいす', 'glace (dessert)', 'ice cream'), ex('スイス', 'すいす', 'Suisse', 'Switzerland')],
  [read('スイス', ['suisu', 'shiisu', 'tsuisu'], ('ス = su, イ = i, ス = su : スイス, la Suisse.', 'ス = su, イ = i, ス = su: スイス, Switzerland.'))])

TA = lesson('n5-kata-ta', 'タチツテト', [
    ('チ (chi) et ツ (tsu) se prononcent comme leurs équivalents hiragana ち et つ.', 'チ (chi) and ツ (tsu) are pronounced like their hiragana equivalents ち and つ.'),
    ('Dans les mots étrangers, le trait ー allonge la voyelle qui le précède et compte pour un temps : タクシー (takushī, taxi).',
     'In foreign words, the bar ー lengthens the vowel before it and counts as one beat: タクシー (takushī, taxi).'),
  ], [ex('テキスト', 'てきすと', 'manuel (de cours)', 'textbook'), ex('タクシー', 'たくしー', 'taxi', 'taxi')],
  [read('テキスト', ['tekisuto', 'tekisoto', 'tekishito'], ('テ = te, キ = ki, ス = su, ト = to : テキスト, le manuel.', 'テ = te, キ = ki, ス = su, ト = to: テキスト, the textbook.'))])

NA = lesson('n5-kata-na', 'ナニヌネノ', [
    ('ヌ (nu) ressemble à ス (su), avec un petit trait de plus qui croise sa diagonale.', 'ヌ (nu) looks like ス (su), with an extra short stroke crossing its diagonal.'),
    ('ノ (no) n’est qu’un seul trait penché ; ニ (ni) est formé de deux traits horizontaux, comme le kanji 二 (deux).',
     'ノ (no) is just one slanting stroke; ニ (ni) is made of two horizontal strokes, like the kanji 二 (two).'),
  ], [ex('テニス', 'てにす', 'tennis', 'tennis'), ex('ネクタイ', 'ねくたい', 'cravate', 'tie')],
  [read('ネクタイ', ['nekutai', 'nukutai', 'nekutsui'], ('ネ = ne, ク = ku, タ = ta, イ = i : ネクタイ, la cravate.', 'ネ = ne, ク = ku, タ = ta, イ = i: ネクタイ, the tie.'))])

HA = lesson('n5-kata-ha', 'ハヒフヘホ', [
    ('ヘ (he) a presque la même forme que le hiragana へ : c’est le plus facile à retenir.', 'ヘ (he) has almost the same shape as the hiragana へ: it is the easiest one to remember.'),
    ('フ (fu) se prononce entre « f » et « h », les lèvres à peine rapprochées, comme ふ.', 'フ (fu) is pronounced between “f” and “h”, with the lips barely brought together, like ふ.'),
  ], [ex('ハート', 'はーと', 'cœur (le symbole)', 'heart (the symbol)'), ex('ヒーター', 'ひーたー', 'radiateur, chauffage d’appoint', 'heater')],
  [read('ハート', ['hāto', 'hato', 'heto'], ('ハ = ha, ー allonge le a, ト = to : ハート, le cœur.', 'ハ = ha, ー lengthens the a, ト = to: ハート, the heart.'))])

MA = lesson('n5-kata-ma', 'マミムメモ', [
    ('マ (ma) se termine par une petite pointe vers le bas ; ム (mu) ressemble à un triangle ouvert avec un petit trait à droite.',
     'マ (ma) ends in a small point facing down; ム (mu) looks like an open triangle with a short stroke on the right.'),
    ('ミ (mi) s’écrit en trois traits obliques, comme trois petites vagues ; メ (me) est une croix penchée.', 'ミ (mi) is written in three slanting strokes, like three small waves; メ (me) is a slanted cross.'),
  ], [ex('トマト', 'とまと', 'tomate', 'tomato'), ex('メモ', 'めも', 'mémo, note', 'memo, note')],
  [read('トマト', ['tomato', 'tomuto', 'tamato'], ('ト = to, マ = ma, ト = to : トマト, la tomate.', 'ト = to, マ = ma, ト = to: トマト, the tomato.'))])

YA = lesson('n5-kata-ya', 'ヤユヨワヲン', [
    ('ヤ (ya), ユ (yu) et ヨ (yo) s’écrivent aussi en petit (ャ, ュ, ョ) pour former des sons comme キャ (kya).', 'ヤ (ya), ユ (yu) and ヨ (yo) are also written small (ャ, ュ, ョ) to form sounds like キャ (kya).'),
    ('ヲ (wo) n’apparaît presque jamais : la particule を s’écrit en hiragana. ン (n) se lit « n », comme ん.', 'ヲ (wo) hardly ever appears: the particle を is written in hiragana. ン (n) is read “n”, like ん.'),
  ], [ex('ワイン', 'わいん', 'vin', 'wine'), ex('ユーモア', 'ゆーもあ', 'humour', 'humour')],
  [read('ワイン', ['wain', 'wein', 'yain'], ('ワ = wa, イ = i, ン = n : ワイン, le vin.', 'ワ = wa, イ = i, ン = n: ワイン, wine.'))])

RA = lesson('n5-kata-ra', 'ラリルレロ', [
    ('Le « r » japonais est battu, entre « r » et « l » : les mots étrangers en « l » s’écrivent donc aussi avec la ligne R (ホテル, hôtel).',
     'The Japanese “r” is a tap, between “r” and “l”: foreign words with an “l” are therefore also written with the R row (ホテル, hotel).'),
    ('ロ (ro) est un carré, plus petit et plus anguleux que le kanji 口 (bouche).', 'ロ (ro) is a square, smaller and more angular than the kanji 口 (mouth).'),
  ], [ex('カメラ', 'かめら', 'appareil photo', 'camera'), ex('ホテル', 'ほてる', 'hôtel', 'hotel')],
  [read('ホテル', ['hoteru', 'hotero', 'hoteri'], ('ホ = ho, テ = te, ル = ru : ホテル, l’hôtel.', 'ホ = ho, テ = te, ル = ru: ホテル, the hotel.'))])

w2 = next(w for w in n5['worlds'] if w['slug'] == 'n5-w2')
c1 = w2['chapters'][0]
assert [l['slug'] for l in c1['lessons']][:2] == ['n5-kata-a', 'n5-kata-ka']
c1['title'] = t('Voyelles et ligne K', 'Vowels and the K row')
c1['lessons'] = [l for l in c1['lessons'] if l['slug'] in ('n5-kata-a', 'n5-kata-ka')]
ka = c1['lessons'][1]
if not ka['exercises']:
    ka['exercises'] = [read('ココア', ['kokoa', 'kakoa', 'kokua'], ('コ = ko, コ = ko, ア = a : ココア, le chocolat chaud.', 'コ = ko, コ = ko, ア = a: ココア, hot chocolate.'))]
w2['chapters'] = [
    c1,
    {'slug': 'n5-w2-c2', 'title': t('Lignes S et T', 'S and T rows'), 'lessons': [SA, TA]},
    {'slug': 'n5-w2-c3', 'title': t('Lignes N et H', 'N and H rows'), 'lessons': [NA, HA]},
    {'slug': 'n5-w2-c4', 'title': t('Lignes M, Y, R, W et ン', 'M, Y, R, W rows and ン'), 'lessons': [MA, YA, RA]},
]
w2['description'] = t('Les 46 katakana de base, l’écriture des mots étrangers.', 'The 46 basic katakana, the script of foreign words.')

kata = [i['front'] for c in w2['chapters'] for l in c['lessons'] for i in l['items']]
assert len(kata) == 46 == len(set(kata)), len(kata)
json.dump(n5, open(P_N5, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
for k, v in EN.items():
    if dico.get(k, v) != v:
        raise SystemExit(f'traduction existante différente : {k}')
    dico[k] = v
json.dump(dico, open(P_DICT, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(f'Katakana du N5 : {len(kata)} caractères en {sum(len(c["lessons"]) for c in w2["chapters"])} leçons')
