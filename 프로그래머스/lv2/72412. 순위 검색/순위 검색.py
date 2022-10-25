import copy
from itertools import combinations
from bisect import bisect_left

def solution(info, query):
    answer = []
    chk = {}
    for i in info:
        tmp = i.split(' ')
        score = int(tmp[-1])  # 점수 따로
        conditions = tmp[:-1]  # 조건 따로
        for i in range(5):
            case = list(combinations(range(4), i))
            for c in case:
                tmp_s = copy.deepcopy(conditions)
                for idx in c:
                    tmp_s[idx] = '-'
                key = ''.join(tmp_s)
                if key not in chk:
                    chk[key] = [score]
                else:
                    chk[key].append(score)
    for v in chk.values():
        v.sort()
        
    for q in query:
        # java, backend, junior, pizza 100
        tmp = q.replace('and ', '')
        # pizza, 100
        tmp = tmp.split(' ')
        # pizza
        score = int(tmp[-1])
        # 100
        condition = ''.join(tmp[:-1])
        count = 0
        if condition in chk:
            idx = bisect_left(chk[condition], score)
            count = len(chk[condition]) - idx
        answer.append(count)

    return answer

   