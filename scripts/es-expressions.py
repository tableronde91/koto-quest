# Onglet Expressions en espagnol (content/expressions/expressions-es.json), français + anglais.
# Politesse, vie quotidienne et tapas, expressions imagées et proverbes d'Espagne.
# Le sens anglais (pour l'interface en anglais) est une courte définition de l'expression.
# Usage : python3 scripts/es-expressions.py
import json, os, sys
sys.path.insert(0, os.path.dirname(__file__))
from kq_content import ROOT, DICO, EN, P_DICT, t

def E(slug, front, meaning, note, register, example=None):
    it = {'slug': 'esx-' + slug, 'kind': 'vocabulary', 'front': front, 'reading': None, 'romaji': None,
          'meaning': t(meaning), 'note': t(note), 'register': register}
    if example:
        es, fr, en = example
        it['example'] = {'jp': es, 'fr': t((fr, en))}
    return it

def TH(slug, glyph, title, description, expressions):
    return {'slug': slug, 'glyph': glyph, 'title': t(title), 'description': t(description), 'expressions': expressions}

THEMES = [
  TH('es-cortesia', '¡', ('Politesse et salutations', 'Politeness and greetings'), ('Les formules qui ouvrent toutes les portes : en Espagne, on salue en entrant dans un magasin ou un ascenseur.', 'The phrases that open every door: in Spain, people say hello when entering a shop or a lift.'), [
    E('encantado', '¡Encantado! / ¡Encantada!', ('enchanté·e !', 'pleased to meet you (said by a man / a woman)'), ('Accordé selon qui parle : encantado pour un homme, encantada pour une femme. En Espagne, on se fait souvent deux bises.', 'It agrees with the speaker: encantado for a man, encantada for a woman. In Spain people often greet with two kisses.'), 'neutral', ('Hola, soy Marta. — ¡Encantado!', 'Bonjour, je suis Marta. — Enchanté !', 'Hi, I’m Marta. — Pleased to meet you!')),
    E('de-nada', 'De nada.', ('de rien', 'you’re welcome'), ('La réponse standard à gracias. Plus soutenu : No hay de qué.', 'The standard reply to gracias. More formal: No hay de qué.'), 'neutral'),
    E('perdon', '¡Perdón!', ('pardon !', 'sorry (small mistake)'), ('Pour s’excuser d’un petit faux pas. Lo siento (je suis désolé) exprime un regret plus fort.', 'To apologise for a small slip. Lo siento (I’m sorry) expresses stronger regret.'), 'neutral'),
    E('con-permiso', 'Con permiso.', ('pardon, vous permettez ?', 'excuse me (to get past)'), ('Pour passer devant quelqu’un ou entrer dans une pièce. On répond : Adelante (je vous en prie).', 'To get past someone or enter a room. The reply is: Adelante (go ahead).'), 'polite'),
    E('que-aproveche', '¡Que aproveche!', ('bon appétit', 'enjoy your meal'), ('On le dit en passant près de quelqu’un qui mange, même un inconnu au restaurant. Aussi : ¡Buen provecho!', 'People say it when passing someone who is eating, even a stranger in a restaurant. Also: ¡Buen provecho!'), 'polite'),
    E('salud', '¡Salud!', ('santé ! ; à tes souhaits !', 'cheers!; bless you!'), ('Pour trinquer… et quand quelqu’un éternue.', 'To make a toast… and when someone sneezes.'), 'casual'),
  ]),
  TH('es-diario', '☀', ('Au quotidien', 'Everyday life'), ('Les petits mots qu’on entend partout en Espagne, au bar comme dans la rue.', 'The little words you hear everywhere in Spain, at the bar as in the street.'), [
    E('vale', '¡Vale!', ('d’accord !', 'OK! (Spain)'), ('Le « OK » espagnol, entendu cent fois par jour en Espagne. En Amérique latine, on dit plutôt dale ou está bien.', 'The Spanish “OK”, heard a hundred times a day in Spain. In Latin America people tend to say dale or está bien.'), 'casual', ('¿Nos vemos a las ocho? — ¡Vale!', 'On se voit à huit heures ? — D’accord !', 'Shall we meet at eight? — OK!')),
    E('venga', '¡Venga!', ('allez ! vas-y !', 'come on!; right then!'), ('Pour encourager, presser… ou conclure une conversation : Venga, hasta luego.', 'To encourage, hurry someone up… or wrap up a conversation: Venga, hasta luego.'), 'casual'),
    E('que-guay', '¡Qué guay!', ('trop bien ! génial !', 'how cool! (Spain)'), ('Très familier, surtout chez les jeunes en Espagne.', 'Very casual, especially among young people in Spain.'), 'casual'),
    E('no-pasa-nada', 'No pasa nada.', ('ce n’est rien, pas de souci', 'no problem, don’t worry'), ('Pour rassurer quelqu’un qui s’excuse.', 'To reassure someone who apologises.'), 'neutral'),
    E('ir-de-tapas', 'ir de tapas', ('aller manger des tapas', 'to go out for tapas'), ('On passe de bar en bar en goûtant de petites assiettes, debout au comptoir.', 'You go from bar to bar tasting small dishes, standing at the counter.'), 'casual'),
    E('la-sobremesa', 'la sobremesa', ('le moment passé à table après le repas', 'time spent chatting at the table after a meal'), ('Mot sans équivalent : on reste à table pour discuter, parfois des heures.', 'A word with no equivalent: people stay at the table to talk, sometimes for hours.'), 'neutral'),
  ]),
  TH('es-imagenes', '♥', ('Expressions imagées', 'Colourful expressions'), ('Des images surprenantes qu’il ne faut surtout pas traduire mot à mot.', 'Surprising images that must never be translated word for word.'), [
    E('estar-en-las-nubes', 'estar en las nubes', ('être dans la lune', 'to be daydreaming'), ('Littéralement « être dans les nuages ».', 'Literally “to be in the clouds”.'), 'casual'),
    E('ser-pan-comido', 'ser pan comido', ('être du gâteau, un jeu d’enfant', 'to be very easy'), ('Littéralement « être du pain mangé ».', 'Literally “to be eaten bread”.'), 'casual', ('El examen es pan comido.', 'L’examen, c’est du gâteau.', 'The exam is a piece of cake.')),
    E('costar-un-ojo', 'costar un ojo de la cara', ('coûter les yeux de la tête', 'to be very expensive'), ('En espagnol, ça ne coûte qu’un œil… du visage.', 'In Spanish it only costs one eye… from your face.'), 'casual'),
    E('tomar-el-pelo', 'tomar el pelo', ('se moquer de quelqu’un, faire marcher', 'to pull someone’s leg'), ('Littéralement « prendre les cheveux ». ¿Me estás tomando el pelo? = tu te moques de moi ?', 'Literally “to take the hair”. ¿Me estás tomando el pelo? = are you pulling my leg?'), 'casual'),
    E('media-naranja', 'mi media naranja', ('ma moitié, l’âme sœur', 'my other half, soulmate'), ('Littéralement « ma moitié d’orange ».', 'Literally “my half orange”.'), 'casual'),
    E('meter-la-pata', 'meter la pata', ('faire une gaffe', 'to put your foot in it'), ('Littéralement « mettre la patte ».', 'Literally “to put the paw in”.'), 'casual'),
  ]),
  TH('es-refranes', '❦', ('Proverbes (refranes)', 'Proverbs (refranes)'), ('Les refranes rythment la conversation en Espagne ; Sancho Panza en cite sans arrêt dans Don Quichotte.', 'Refranes punctuate conversation in Spain; Sancho Panza quotes them all the time in Don Quixote.'), [
    E('mas-vale-tarde', 'Más vale tarde que nunca.', ('mieux vaut tard que jamais', 'it is good to do something even if it is late'), ('Exactement comme en français.', 'Exactly as in French.'), 'neutral'),
    E('dime-con-quien', 'Dime con quién andas y te diré quién eres.', ('dis-moi qui tu fréquentes, je te dirai qui tu es', 'you are judged by the company you keep'), ('Un refrán que Sancho aime citer.', 'A refrán Sancho likes to quote.'), 'neutral'),
    E('quien-madruga', 'A quien madruga, Dios le ayuda.', ('l’avenir appartient à ceux qui se lèvent tôt', 'people who start early succeed'), ('Littéralement « Dieu aide celui qui se lève tôt ».', 'Literally “God helps the one who gets up early”.'), 'neutral'),
    E('perro-ladrador', 'Perro ladrador, poco mordedor.', ('chien qui aboie ne mord pas', 'his bark is worse than his bite'), ('Ceux qui menacent le plus agissent rarement.', 'Those who threaten most rarely act.'), 'neutral'),
    E('en-boca-cerrada', 'En boca cerrada no entran moscas.', ('la parole est d’argent, le silence est d’or', 'least said, soonest mended'), ('Littéralement « dans une bouche fermée, les mouches n’entrent pas ».', 'Literally “flies don’t get into a closed mouth”.'), 'neutral'),
    E('no-hay-mal', 'No hay mal que por bien no venga.', ('à quelque chose malheur est bon', 'every cloud has a silver lining'), ('Même un malheur peut apporter du bon.', 'Even a misfortune can bring something good.'), 'neutral'),
  ]),
]

DATA = {
  'contentVersion': '2026.11.23',
  'language': 'es',
  'notice': t(('Expressions espagnoles courantes sélectionnées par Koto Quest (espagnol d’Espagne) ; le registre (poli, familier…) aide à choisir la bonne formule selon la situation.', 'Common Spanish expressions selected by Koto Quest (Spanish from Spain); the register (polite, casual…) helps you choose the right phrase for the situation.')),
  'themes': THEMES,
}

for fr, en in EN.items():
    if fr in DICO and DICO[fr] != en:
        raise SystemExit(f'traduction existante différente : {fr} → {DICO[fr]} / {en}')
slugs = [e['slug'] for th in THEMES for e in th['expressions']]
assert len(slugs) == len(set(slugs)), 'slug en double'
json.dump(DATA, open(os.path.join(ROOT, 'content/expressions/expressions-es.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
DICO.update(EN)
json.dump(DICO, open(P_DICT, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(f'Expressions espagnoles : {len(THEMES)} thèmes, {len(slugs)} expressions')
