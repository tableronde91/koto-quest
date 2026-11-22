# Révision des proverbes en japonais : thèmes ことわざ et 四字熟語 ajoutés à l'onglet Expressions
# (content/expressions/expressions.json), avec leur entraînement. Les thèmes existants sont conservés.
# Usage : python3 scripts/ja-proverbs.py
import json, os, sys
sys.path.insert(0, os.path.dirname(__file__))
from kq_content import ROOT, DICO, EN, P_DICT, t

P = os.path.join(ROOT, 'content/expressions/expressions.json')

def E(slug, front, reading, romaji, meaning, note, register, example=None):
    fr = meaning[0]
    meaning = (fr, EN.get(fr) or DICO.get(fr) or meaning[1])
    it = {'slug': slug, 'kind': 'vocabulary', 'front': front, 'reading': reading, 'romaji': romaji, 'meaning': t(meaning), 'note': t(note), 'register': register}
    if example:
        jp, fr_, en_ = example
        it['example'] = {'jp': jp, 'fr': t((fr_, en_))}
    return it

def TH(slug, glyph, title, description, expressions):
    return {'slug': slug, 'glyph': glyph, 'title': t(title), 'description': t(description), 'expressions': expressions}

THEMES = [
  TH('kotowaza', '諺', ('Proverbes (ことわざ)', 'Proverbs (ことわざ)'), ('Les proverbes que les Japonais glissent dans la conversation : à réviser jusqu’à les reconnaître au vol.', 'The proverbs Japanese people slip into conversation: review them until you recognise them instantly.'), [
    E('jprov-saru', '猿も木から落ちる', 'さるもきからおちる', 'saru mo ki kara ochiru', ('même les meilleurs se trompent', 'even monkeys fall from trees'), ('« Même les singes tombent des arbres » : pour consoler un expert qui vient de se tromper.', '“Even monkeys fall from trees”: to console an expert who has just made a mistake.'), 'neutral'),
    E('jprov-ishi', '石の上にも三年', 'いしのうえにもさんねん', 'ishi no ue ni mo sannen', ('la persévérance finit par payer', 'perseverance pays off'), ('« Trois ans assis sur une pierre, et elle finit par chauffer. »', '“Sit on a stone for three years and even it grows warm.”'), 'neutral', ('石の上にも三年だよ。毎日続けよう。', 'La persévérance paie : continue chaque jour.', 'Perseverance pays off: keep at it every day.')),
    E('jprov-nanakorobi', '七転び八起き', 'ななころびやおき', 'nanakorobi yaoki', ('tomber sept fois, se relever huit', 'fall seven times, get up eight'), ('Pour encourager quelqu’un après un échec : on se relève toujours.', 'To encourage someone after a setback: you always get back up.'), 'neutral'),
    E('jprov-isogaba', '急がば回れ', 'いそがばまわれ', 'isogaba maware', ('hâte-toi lentement', 'more haste, less speed'), ('« Si tu es pressé, fais le détour » : le chemin sûr est souvent le plus rapide.', '“If you are in a hurry, take the long way round”: the safe path is often the quickest.'), 'neutral'),
    E('jprov-hanayori', '花より団子', 'はなよりだんご', 'hana yori dango', ('le concret avant l’esthétique', 'substance over style'), ('« Les dango plutôt que les fleurs » : se dit de celui qui préfère manger que contempler les cerisiers.', '“Dumplings rather than flowers”: said of someone who would rather eat than admire the cherry blossoms.'), 'casual', ('お花見なのに、みんな花より団子だね。', 'C’est la fête des cerisiers, mais tout le monde ne pense qu’à manger !', 'It’s cherry-blossom viewing, but everyone only cares about the food!')),
    E('jprov-neko', '猫に小判', 'ねこにこばん', 'neko ni koban', ('donner de la confiture aux cochons', 'pearls before swine'), ('« Une pièce d’or à un chat » : un objet précieux offert à qui ne peut l’apprécier.', '“A gold coin to a cat”: something precious given to someone who cannot appreciate it.'), 'casual'),
    E('jprov-chiri', '塵も積もれば山となる', 'ちりもつもればやまとなる', 'chiri mo tsumoreba yama to naru', ('les petits ruisseaux font les grandes rivières', 'many a little makes a mickle'), ('« Même la poussière, accumulée, devient montagne » : parfait pour l’apprentissage des kanji !', '“Even dust, piled up, becomes a mountain”: perfect for learning kanji!'), 'neutral'),
    E('jprov-kawazu', '井の中の蛙大海を知らず', 'いのなかのかわずたいかいをしらず', 'i no naka no kawazu taikai o shirazu', ('avoir une vision étroite du monde', 'a frog in a well'), ('« La grenouille au fond du puits ne connaît pas l’océan » : le même proverbe existe en coréen (우물 안 개구리).', '“The frog in the well knows nothing of the ocean”: the same proverb exists in Korean (우물 안 개구리).'), 'neutral'),
    E('jprov-uwasa', '噂をすれば影', 'うわさをすればかげ', 'uwasa o sureba kage', ('quand on parle du loup, on en voit la queue', 'speak of the devil'), ('« Parle de quelqu’un, et voici son ombre. »', '“Talk about someone, and here comes their shadow.”'), 'casual', ('噂をすれば影だ。田中さんが来たよ。', 'Quand on parle du loup… voilà Tanaka.', 'Speak of the devil, here comes Tanaka.')),
    E('jprov-anzuru', '案ずるより産むが易し', 'あんずるよりうむがやすし', 'anzuru yori umu ga yasushi', ('c’est moins difficile qu’on ne le craint', 'it’s easier done than feared'), ('Pour rassurer quelqu’un avant une épreuve, comme le JLPT.', 'To reassure someone before an ordeal, like the JLPT.'), 'neutral'),
  ]),
  TH('yojijukugo', '熟', ('Expressions en quatre caractères (四字熟語)', 'Four-character idioms (四字熟語)'), ('Les yojijukugo, venus du chinois classique, donnent du style à l’écrit et aux discours.', 'Yojijukugo, from classical Chinese, add style to writing and speeches.'), [
    E('jprov-isseki', '一石二鳥', 'いっせきにちょう', 'isseki nichō', ('faire d’une pierre deux coups', 'to kill two birds with one stone'), ('Une pierre, deux oiseaux.', 'One stone, two birds.'), 'formal'),
    E('jprov-ichigo', '一期一会', 'いちごいちえ', 'ichigo ichie', ('chaque rencontre est unique', 'a once-in-a-lifetime encounter'), ('Venu de la cérémonie du thé : chérir chaque rencontre, car elle ne se reproduira pas.', 'From the tea ceremony: treasure each meeting, for it will never happen again.'), 'formal', ('一期一会を大切にしたい。', 'Je veux chérir chaque rencontre.', 'I want to treasure every encounter.')),
    E('jprov-junin', '十人十色', 'じゅうにんといろ', 'jūnin toiro', ('à chacun ses goûts', 'to each their own'), ('« Dix personnes, dix couleurs. »', '“Ten people, ten colours.”'), 'neutral'),
    E('jprov-jigo', '自業自得', 'じごうじとく', 'jigō jitoku', ('on récolte ce qu’on a semé', 'you reap what you sow'), ('Terme bouddhique : on reçoit le fruit de ses propres actes.', 'A Buddhist term: you receive the fruit of your own deeds.'), 'formal'),
    E('jprov-kishi', '起死回生', 'きしかいせい', 'kishi kaisei', ('retournement inespéré', 'a miraculous comeback'), ('« Ressusciter le mourant » : un renversement de situation spectaculaire.', '“Reviving the dying”: a spectacular turnaround.'), 'formal'),
    E('jprov-onko', '温故知新', 'おんこちしん', 'onko chishin', ('tirer des leçons du passé', 'learning new things from the old'), ('Confucius : réviser l’ancien pour comprendre le nouveau. La devise des révisions !', 'Confucius: review the old to understand the new. The motto of reviews!'), 'formal'),
    E('jprov-ishin', '以心伝心', 'いしんでんしん', 'ishin denshin', ('se comprendre sans un mot', 'to understand each other without words'), ('De cœur à cœur : le même idiome existe en coréen (이심전심).', 'From heart to heart: the same idiom exists in Korean (이심전심).'), 'formal'),
    E('jprov-taiki', '大器晩成', 'たいきばんせい', 'taiki bansei', ('les grands talents mûrissent lentement', 'great talents mature late'), ('Les grands vases se font lentement : pour encourager qui progresse doucement.', 'Great vessels take long to make: to encourage someone who progresses slowly.'), 'formal'),
    E('jprov-mikka', '三日坊主', 'みっかぼうず', 'mikka bōzu', ('bonnes résolutions sans lendemain', 'resolutions that last three days'), ('« Moine de trois jours » : qui abandonne vite ce qu’il commence.', '“A three-day monk”: someone who quickly gives up what they start.'), 'casual', ('日記はいつも三日坊主だ。', 'Mon journal, je l’abandonne toujours au bout de trois jours.', 'I always give up my diary after three days.')),
    E('jprov-uo', '右往左往', 'うおうさおう', 'uō saō', ('aller dans tous les sens, s’affoler', 'to run around in confusion'), ('Aller à droite, aller à gauche.', 'Going right, going left.'), 'formal'),
  ]),
]

data = json.load(open(P, encoding='utf-8'))
mine = {th['slug'] for th in THEMES}
data['themes'] = [th for th in data['themes'] if th['slug'] not in mine] + THEMES
data['contentVersion'] = '2026.11-expr2'

# Contrôles : slugs uniques, aucune forme déjà enseignée dans les leçons, traductions cohérentes
slugs = [e['slug'] for th in data['themes'] for e in th['expressions']]
assert len(slugs) == len(set(slugs)), 'slug en double'
fronts = set()
for lv in ['n5', 'n4', 'n3', 'n2', 'n1']:
    d = json.load(open(os.path.join(ROOT, f'content/{lv}/{lv}.json'), encoding='utf-8'))
    for w in d['worlds']:
        for c in w['chapters']:
            for l in c['lessons']:
                fronts.update(it['front'] for it in l['items'])
clash = [e['front'] for th in THEMES for e in th['expressions'] if e['front'] in fronts]
assert not clash, f'déjà dans les leçons : {clash}'
for fr, en in EN.items():
    if fr in DICO and DICO[fr] != en:
        raise SystemExit(f'traduction existante différente : {fr} → {DICO[fr]} / {en}')
full = {**DICO, **EN}
by_en = {}
for th in data['themes']:
    for e in th['expressions']:
        by_en.setdefault(full.get(e['meaning'], e['meaning']), set()).add(e['meaning'])
dup = {k: v for k, v in by_en.items() if len(v) > 1}
assert not dup, f'sens anglais en double : {dup}'
open(P, "w", encoding="utf-8", newline="").write(json.dumps(data, ensure_ascii=False, indent=2).replace("\n", "\r\n"))
DICO.update(EN)
json.dump(DICO, open(P_DICT, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(f"Expressions japonaises : {len(data['themes'])} thèmes, {len(slugs)} expressions")
