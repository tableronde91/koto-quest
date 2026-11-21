# Banques des examens blancs « TOPIK II — niveau 5 » et « niveau 6 » (content/exams/topik5.json, topik6.json).
# Le TOPIK II est une seule épreuve pour les niveaux 3 à 6 : chaque banque reprend la précédente
# et y ajoute des questions plus difficiles. Validation : niveau 5 (190/300) puis niveau 6 (230/300).
# Usage : python3 scripts/topik56-exam.py   (après scripts/topik4-exam.py)
import json, os, runpy, copy
ROOT = os.path.join(os.path.dirname(__file__), '..')
HERE = os.path.dirname(__file__)
T4 = runpy.run_path(os.path.join(HERE, 'topik4-exam.py'))
T1 = runpy.run_path(os.path.join(HERE, 'topik1-exam.py'))
LQ, RQ = T1['LQ'], T1['RQ']
BANK4 = json.load(open(os.path.join(ROOT, 'content/exams/topik4.json'), encoding='utf-8'))

EXTRA5 = {
 'l-next': [
  LQ('F|이번 신제품 반응이 생각보다 안 좋대요.\nM|가격이 비싼 반면에 기능은 별로 다르지 않으니까요.', ['그럼 가격을 다시 검토해 봐야겠네요.', '반응이 좋을 리가 없어요.', '신제품이 나왔다면서요?', '가격이 싸서 다행이에요.']),
 ],
 'l-same': [
  LQ('M|최근 한 연구에 따르면 하루에 삼십 분씩 걷는 사람은 그렇지 않은 사람보다 우울증에 걸릴 위험이 낮다고 합니다. 연구팀은 운동 시간보다 꾸준함이 더 중요하다고 강조했습니다.', ['연구팀은 꾸준히 운동하는 것을 강조했다.', '운동 시간이 길수록 효과가 크다.', '걷기는 우울증과 관계가 없다.', '하루에 세 시간 걸어야 한다.']),
 ],
 'l-main': [
  LQ('F|요즘은 실패를 두려워해서 도전하지 않는 젊은이가 많대요.\nM|실패를 해 봐야 무엇이 부족한지 알 수 있는 법이에요. 실패도 하나의 경험으로 받아들이는 태도가 필요해요.', ['실패를 경험으로 받아들여야 한다.', '실패하지 않는 것이 가장 중요하다.', '젊은이들은 도전을 많이 한다.', '실패하면 다시 도전하면 안 된다.']),
 ],
 'l-long': [
  LQ('F|바리공주 이야기는 부모에게 버림받은 딸이 오히려 부모를 살리기 위해 저승까지 다녀오는 내용입니다. 이 이야기는 죽은 사람의 넋을 위로하는 굿에서 불렸으며, 오늘날에도 효와 희생의 의미를 전하고 있습니다.', ['바리공주 이야기는 굿에서 불렸다.', '바리공주는 부모를 원망하며 떠났다.', '이 이야기는 최근에 만들어졌다.', '바리공주는 저승에 가지 않았다.'], '들은 내용과 같은 것을 고르십시오.'),
  LQ('M|인공지능이 사람의 일을 대신하는 분야가 늘고 있습니다. 일자리가 줄어들 거라는 걱정이 있는 반면에, 새로운 직업이 생겨날 거라는 기대도 있습니다. 중요한 것은 변화를 막는 것이 아니라 변화에 맞는 교육을 준비하는 것입니다.', ['변화에 맞는 교육을 준비해야 한다.', '인공지능 사용을 금지해야 한다.', '일자리는 전혀 줄지 않을 것이다.', '새로운 직업은 생기지 않는다.'], '남자의 중심 생각으로 가장 알맞은 것을 고르십시오.'),
 ],
 'w-blank': [
  RQ(['실패를 두려워하지 않는 것이 중요하다', '실패하지 않는 방법만 배워야 한다', '도전은 위험하므로 피해야 한다', '성공한 사람은 실패한 적이 없다'],
     passage='많은 사람들이 실패를 피하려고만 한다. 그러나 실패를 통해 우리는 자신에게 부족한 점을 알게 된다. 따라서 새로운 일에 도전할 때는 (㉠). 실패는 끝이 아니라 성장의 과정이기 때문이다.'),
 ],
 'w-graph': [
  RQ(['재택근무를 원하는 직장인은 5년 사이에 크게 늘었다.', '재택근무를 원하는 사람은 줄었다.', '2024년에는 모든 직장인이 재택근무를 원했다.', '재택근무에 대한 생각은 변하지 않았다.'],
     passage='「재택근무를 원하는 직장인 비율」\n\n2019년 : 18%\n2024년 : 52%'),
 ],
 'r-blank': [
  RQ(['하기 마련이다', '할 리가 없다', '할 뻔했다', '할 셈이다'], jp='사람은 누구나 실수를 (　).'),
  RQ(['볼 만하다', '볼 뻔하다', '보는 척하다', '볼 리가 없다'], jp='이 전시회는 한 번쯤 가서 (　).'),
 ],
 'r-similar': [
  RQ(['오기 마련이에요', '올 리가 없어요', '올 뻔했어요', '오는 척해요'], jp='겨울이 가면 봄은 <u>오는 법이에요</u>.'),
 ],
 'r-headline': [
  RQ(['청년 실업 문제가 해결되기는커녕 오히려 더 심각해졌다.', '청년 실업 문제가 해결되었다.', '청년들의 취업률이 크게 올랐다.', '정부가 청년 일자리를 줄였다.'], jp='청년 실업, 해결은커녕 더 악화'),
 ],
 'r-passage': [
  RQ(['서로 다른 의견을 존중하는 태도', '자기 의견만 주장하는 태도', '토론을 피하는 태도', '다수의 의견을 무조건 따르는 태도'], text='필자가 강조하는 것은 무엇입니까?',
     passage='토론에서 이기는 것만이 목적이라면 상대의 말을 듣지 않기 십상이다. 그러나 좋은 토론은 상대의 의견을 듣고 자신의 생각을 다시 돌아보는 과정이다. 생각이 다른 사람을 적으로 보는 대신에, 함께 답을 찾는 동료로 보아야 한다.'),
  RQ(['평생 학습이 필요한 이유', '대학 입학 방법', '노인의 건강 관리', '직장인의 휴가'], text='무엇에 대한 글인지 고르십시오.',
     passage='예전에는 학교를 졸업하면 공부가 끝난다고 생각했다. 그러나 기술이 빠르게 변하는 오늘날에는 한 번 배운 지식만으로 평생 일하기 어렵다. 나이가 들수록 새로운 것을 배우는 사람이 사회 변화에 더 잘 적응하기 마련이다.'),
 ],
}

EXTRA6 = {
 'l-next': [
  LQ('M|이번 사업은 위험 부담이 커서 다시 생각해 보는 게 좋지 않을까 싶습니다.\nF|하지만 지금 시작하지 않으면 경쟁사에 뒤처질 게 뻔해요.', ['그럼 위험을 줄일 방안부터 마련해 봅시다.', '사업이 끝나서 다행이에요.', '경쟁사가 없어서 좋겠네요.', '위험할 리가 없어요.']),
 ],
 'l-main': [
  LQ('F|전통문화는 박물관에 보관하는 것만으로도 충분하지 않을까요?\nM|보관하는 데 그치지 않고 사람들이 일상에서 즐길 수 있어야 전통이 살아 있는 법입니다.', ['전통은 일상에서 즐겨야 살아 있다.', '전통은 박물관에만 보관해야 한다.', '전통문화는 필요 없다.', '박물관을 더 지어야 한다.']),
 ],
 'l-long': [
  LQ('M|단군 신화에서 곰과 호랑이는 사람이 되기 위해 동굴에서 백 일을 견뎌야 했습니다. 호랑이는 참지 못하고 뛰쳐나간 반면, 곰은 끝까지 견뎌 사람이 되었습니다. 이 이야기는 인내와 끈기를 중요하게 여긴 고대인의 생각을 보여 준다고 할 수 있습니다.', ['신화를 통해 고대인의 가치관을 설명하고 있다.', '호랑이의 용기를 칭찬하고 있다.', '신화가 사실이라고 주장하고 있다.', '곰과 호랑이의 생태를 비교하고 있다.'], '남자가 하는 일로 가장 알맞은 것을 고르십시오.'),
  LQ('F|우리 연구소에서는 사라져 가는 지역 방언을 기록하는 사업을 하고 있습니다. 방언은 단순히 말투가 다른 것이 아니라 그 지역의 역사와 생활이 담긴 문화유산이기 때문입니다. 지금 기록하지 않으면 영원히 사라질 게 뻔합니다.', ['방언을 기록하는 일의 필요성', '표준어를 배우는 방법', '연구소의 위치', '지역 축제의 역사'], '무엇에 대한 내용인지 고르십시오.'),
 ],
 'w-blank': [
  RQ(['오히려 독이 되기 십상이다', '언제나 도움이 된다', '건강과는 관계가 없다', '반드시 필요하다'],
     passage='무엇이든 지나치면 좋지 않다. 몸에 좋은 음식이라도 한 가지만 지나치게 먹으면 (㉠). 그러므로 다양한 음식을 골고루 적당히 먹는 것이 건강을 지키는 길이다.'),
 ],
 'r-blank': [
  RQ(['후회한들', '후회하자마자', '후회하는 김에', '후회할 겸'], jp='이미 지나간 일을 (　) 무슨 소용이 있겠는가?'),
  RQ(['굶을지언정', '굶는 김에', '굶다 보면', '굶는 바람에'], jp='그는 (　) 남에게 도움을 청하지 않았다.'),
  RQ(['그지없다', '마련이다', '십상이다', '일쑤이다'], jp='이렇게 큰 상을 받게 되어 영광스럽기 (　).'),
 ],
 'r-similar': [
  RQ(['보시다시피', '보시는 김에', '보실 겸', '보시자마자'], jp='<u>여러분이 보고 계신 것처럼</u> 결과는 매우 좋습니다.'),
 ],
 'r-topic': [
  RQ(['속담', '광고', '안내문', '일기 예보'], jp='낮말은 새가 듣고 밤말은 쥐가 듣는다.'),
 ],
 'r-passage': [
  RQ(['자업자득', '일석이조', '금시초문', '우왕좌왕'], text='이 글의 내용과 가장 관계있는 사자성어를 고르십시오.',
     passage='그는 시험 기간에도 공부는 하지 않고 매일 놀기만 했다. 결국 시험에 떨어지자 그는 운이 나빴다고 말했지만, 친구들은 모두 그가 스스로 만든 결과라고 생각했다.'),
  RQ(['신화는 공동체의 정체성을 형성하는 데 기여한다.', '신화는 모두 역사적 사실이다.', '신화는 오늘날 아무런 의미가 없다.', '신화는 한 사람이 만든 이야기이다.'], text='이 글의 중심 생각으로 가장 알맞은 것을 고르십시오.',
     passage='건국 신화는 단순한 옛이야기에 그치지 않는다. 한 민족이 어디에서 왔으며 무엇을 소중히 여기는지를 보여 주는 이야기이기 때문이다. 단군 신화의 「홍익인간」 정신이 오늘날까지 교육의 이념으로 이어지고 있는 것도 신화가 공동체의 정체성을 만드는 데 큰 역할을 한다는 것을 보여 준다.'),
 ],
}

def build(base, extra, slug, level, notice):
    parts = copy.deepcopy(base['parts'])
    extra = dict(extra)
    for p in parts:
        add = extra.pop(p['id'], [])
        for q in add:
            assert len(set(q['choices'])) == len(q['choices']) == 4, q
            d = q.get('display') or q
            for k in ('jp', 'passage'):
                if isinstance(q.get(k), str):
                    q[k] = q[k].replace('<u>', '{{').replace('</u>', '}}')
        p['questions'] = add + p['questions']
    assert not extra, list(extra)
    return {'slug': slug, 'level': level, 'contentVersion': '2026.11.21', 'notice': notice, 'parts': parts}

N5 = 'Questions rédigées par Koto Quest au format de l’examen officiel du TOPIK II (niveau 5 : 190 points sur 300), en version abrégée. L’écriture (쓰기) est adaptée en questions à choix. Ce ne sont pas des questions officielles.'
N6 = 'Questions rédigées par Koto Quest au format de l’examen officiel du TOPIK II (niveau 6 : 230 points sur 300), en version abrégée. L’écriture (쓰기) est adaptée en questions à choix. Ce ne sont pas des questions officielles.'
bank5 = build(BANK4, EXTRA5, 'topik5', 'TOPIK5', N5)
bank6 = build(bank5, EXTRA6, 'topik6', 'TOPIK6', N6)
for b in (bank5, bank6):
    json.dump(b, open(os.path.join(ROOT, f"content/exams/{b['slug']}.json"), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
P_DICT = os.path.join(ROOT, 'content/i18n/en/content.json')
d = json.load(open(P_DICT, encoding='utf-8'))
d[N5] = 'Questions written by Koto Quest in the format of the official TOPIK II exam (level 5: 190 points out of 300), in a shortened version. Writing (쓰기) is adapted as multiple-choice questions. They are not official questions.'
d[N6] = 'Questions written by Koto Quest in the format of the official TOPIK II exam (level 6: 230 points out of 300), in a shortened version. Writing (쓰기) is adapted as multiple-choice questions. They are not official questions.'
json.dump(d, open(P_DICT, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
count = lambda b: sum(len(p['questions']) for p in b['parts'])
print(f"TOPIK II niveau 5 : {count(bank5)} questions ; niveau 6 : {count(bank6)} questions")
