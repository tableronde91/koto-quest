# Hangeul : définitions communes à l'onglet Caractères (content/characters/hangul.json)
# et aux deux premières îles du parcours TOPIK 1. Même slug = même notion = maîtrise partagée.
# Romanisation révisée (romanisation officielle de la Corée du Sud).
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from kq_content import item

MEANING_EN = {'muet / ng': 'silent / ng', 'k (aspiré)': 'k (aspirated)', 't (aspiré)': 't (aspirated)', 'p (aspiré)': 'p (aspirated)'}

def J(slug, front, sound, romaji):
    """Lettre (자모) ou syllabe : notion de type « kana ». `sound` est la syllabe prononcée par la synthèse vocale."""
    return item(slug, 'kana', front, sound, romaji, (romaji, MEANING_EN.get(romaji, romaji)))

# ─── Voyelles ───
V_BASE = [J('hg-a', 'ㅏ', '아', 'a'), J('hg-eo', 'ㅓ', '어', 'eo'), J('hg-o', 'ㅗ', '오', 'o'), J('hg-u', 'ㅜ', '우', 'u'), J('hg-eu', 'ㅡ', '으', 'eu'), J('hg-i', 'ㅣ', '이', 'i')]
V_Y = [J('hg-ya', 'ㅑ', '야', 'ya'), J('hg-yeo', 'ㅕ', '여', 'yeo'), J('hg-yo', 'ㅛ', '요', 'yo'), J('hg-yu', 'ㅠ', '유', 'yu')]
V_AE = [J('hg-ae', 'ㅐ', '애', 'ae'), J('hg-e', 'ㅔ', '에', 'e')]
V_YAE = [J('hg-yae', 'ㅒ', '얘', 'yae'), J('hg-ye', 'ㅖ', '예', 'ye')]
V_W1 = [J('hg-wa', 'ㅘ', '와', 'wa'), J('hg-wae', 'ㅙ', '왜', 'wae'), J('hg-oe', 'ㅚ', '외', 'oe')]
V_W2 = [J('hg-wo', 'ㅝ', '워', 'wo'), J('hg-we', 'ㅞ', '웨', 'we'), J('hg-wi', 'ㅟ', '위', 'wi'), J('hg-ui', 'ㅢ', '의', 'ui')]

# ─── Consonnes ───
C_BASE1 = [J('hg-g', 'ㄱ', '가', 'g / k'), J('hg-n', 'ㄴ', '나', 'n'), J('hg-d', 'ㄷ', '다', 'd / t'), J('hg-r', 'ㄹ', '라', 'r / l'), J('hg-m', 'ㅁ', '마', 'm')]
C_BASE2 = [J('hg-b', 'ㅂ', '바', 'b / p'), J('hg-s', 'ㅅ', '사', 's'), J('hg-ng', 'ㅇ', '아', 'muet / ng'), J('hg-j', 'ㅈ', '자', 'j'), J('hg-h', 'ㅎ', '하', 'h')]
C_ASP = [J('hg-k', 'ㅋ', '카', 'k (aspiré)'), J('hg-t', 'ㅌ', '타', 't (aspiré)'), J('hg-p', 'ㅍ', '파', 'p (aspiré)'), J('hg-ch', 'ㅊ', '차', 'ch')]
C_TENSE = [J('hg-kk', 'ㄲ', '까', 'kk'), J('hg-tt', 'ㄸ', '따', 'tt'), J('hg-pp', 'ㅃ', '빠', 'pp'), J('hg-ss', 'ㅆ', '싸', 'ss'), J('hg-jj', 'ㅉ', '짜', 'jj')]

# ─── Syllabes ───
S_A = [J('hg-ga', '가', '가', 'ga'), J('hg-na', '나', '나', 'na'), J('hg-da', '다', '다', 'da'), J('hg-ra', '라', '라', 'ra'), J('hg-ma', '마', '마', 'ma'),
       J('hg-ba', '바', '바', 'ba'), J('hg-sa', '사', '사', 'sa'), J('hg-ja', '자', '자', 'ja'), J('hg-ha', '하', '하', 'ha')]
S_ASP = [J('hg-ka', '카', '카', 'ka'), J('hg-ta', '타', '타', 'ta'), J('hg-pa', '파', '파', 'pa'), J('hg-cha', '차', '차', 'cha')]
S_G = [J('hg-geo', '거', '거', 'geo'), J('hg-go', '고', '고', 'go'), J('hg-gu', '구', '구', 'gu'), J('hg-geu', '그', '그', 'geu'), J('hg-gi', '기', '기', 'gi')]
S_TENSE = [J('hg-kka', '까', '까', 'kka'), J('hg-tta', '따', '따', 'tta'), J('hg-ppa', '빠', '빠', 'ppa'), J('hg-ssa', '싸', '싸', 'ssa'), J('hg-jja', '짜', '짜', 'jja')]
BATCHIM = [J('hg-bc-gak', '각', '각', 'gak'), J('hg-bc-an', '안', '안', 'an'), J('hg-bc-mal', '말', '말', 'mal'), J('hg-bc-bam', '밤', '밤', 'bam'),
           J('hg-bc-bap', '밥', '밥', 'bap'), J('hg-bc-gang', '강', '강', 'gang'), J('hg-bc-ot', '옷', '옷', 'ot')]

CATALOG = {
  'contentVersion': '2026.11.20',
  'language': 'ko',
  'notice': 'Romanisation révisée (système officiel de la Corée du Sud). Les consonnes se prononcent ici avec la voyelle ㅏ pour qu’on les entende.',
  'sections': [
    {'slug': 'hangul-vowels', 'glyph': 'ㅏ', 'title': 'Voyelles', 'description': 'Les 21 voyelles du hangeul : six de base, quatre en « y », et les voyelles composées. Elles se tracent avec des traits horizontaux et verticaux.', 'groups': [
      {'slug': 'hg-v-base', 'title': 'Voyelles de base', 'items': V_BASE},
      {'slug': 'hg-v-y', 'title': 'Voyelles en y', 'items': V_Y},
      {'slug': 'hg-v-ae', 'title': 'ㅐ ㅔ ㅒ ㅖ', 'items': V_AE + V_YAE},
      {'slug': 'hg-v-w', 'title': 'Voyelles en w et ㅢ', 'items': V_W1 + V_W2},
    ]},
    {'slug': 'hangul-consonants', 'glyph': 'ㄱ', 'title': 'Consonnes', 'description': 'Les 19 consonnes : quatorze simples, dont quatre aspirées, et cinq doubles prononcées tendues. Leur forme imite la position de la bouche.', 'groups': [
      {'slug': 'hg-c-base', 'title': 'Consonnes de base', 'items': C_BASE1 + C_BASE2},
      {'slug': 'hg-c-asp', 'title': 'Consonnes aspirées', 'items': C_ASP},
      {'slug': 'hg-c-tense', 'title': 'Consonnes doubles (tendues)', 'items': C_TENSE},
    ]},
    {'slug': 'hangul-syllables', 'glyph': '가', 'title': 'Syllabes', 'description': 'Les lettres s’assemblent en blocs : consonne + voyelle (가), parfois une consonne finale en dessous, le batchim (각).', 'groups': [
      {'slug': 'hg-s-a', 'title': 'Consonne + ㅏ', 'items': S_A},
      {'slug': 'hg-s-asp', 'title': 'Aspirées + ㅏ', 'items': S_ASP},
      {'slug': 'hg-s-tense', 'title': 'Doubles + ㅏ', 'items': S_TENSE},
      {'slug': 'hg-s-g', 'title': 'ㄱ + voyelles', 'items': S_G},
      {'slug': 'hg-s-bc', 'title': 'Batchim (consonne finale)', 'items': BATCHIM},
    ]},
  ],
}

CATALOG_EN = {
  'Romanisation révisée (système officiel de la Corée du Sud). Les consonnes se prononcent ici avec la voyelle ㅏ pour qu’on les entende.': 'Revised Romanization (South Korea’s official system). Consonants are pronounced here with the vowel ㅏ so that you can hear them.',
  'Voyelles': 'Vowels',
  'Les 21 voyelles du hangeul : six de base, quatre en « y », et les voyelles composées. Elles se tracent avec des traits horizontaux et verticaux.': 'The 21 Hangul vowels: six basic ones, four “y” vowels, and the compound vowels. They are drawn with horizontal and vertical strokes.',
  'Voyelles de base': 'Basic vowels',
  'Voyelles en y': '“Y” vowels',
  'Voyelles en w et ㅢ': '“W” vowels and ㅢ',
  'Consonnes': 'Consonants',
  'Les 19 consonnes : quatorze simples, dont quatre aspirées, et cinq doubles prononcées tendues. Leur forme imite la position de la bouche.': 'The 19 consonants: fourteen simple ones, four of them aspirated, and five double consonants pronounced tense. Their shapes imitate the position of the mouth.',
  'Consonnes de base': 'Basic consonants',
  'Consonnes aspirées': 'Aspirated consonants',
  'Consonnes doubles (tendues)': 'Double (tense) consonants',
  'Syllabes': 'Syllables',
  'Les lettres s’assemblent en blocs : consonne + voyelle (가), parfois une consonne finale en dessous, le batchim (각).': 'Letters combine into blocks: consonant + vowel (가), sometimes with a final consonant underneath, the batchim (각).',
  'Consonne + ㅏ': 'Consonant + ㅏ',
  'Aspirées + ㅏ': 'Aspirated + ㅏ',
  'Doubles + ㅏ': 'Doubles + ㅏ',
  'ㄱ + voyelles': 'ㄱ + vowels',
  'Batchim (consonne finale)': 'Batchim (final consonant)',
}
