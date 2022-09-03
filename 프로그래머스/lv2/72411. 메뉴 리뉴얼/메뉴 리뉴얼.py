from itertools import combinations
from collections import Counter


def solution(orders, course):

    answer = []
    for c in course:
        tmp = []
        for order in orders:
            for comb in combinations(order, c):
                tmp_s = ''.join(sorted(comb))
                tmp.append(tmp_s)

        tmp = Counter(tmp).most_common()
        if len(tmp) >= 1:
            _max = tmp[0][1]
        else:
            continue
        for i in tmp:
            if i[1] == _max and i[1] >= 2:
                answer.append(i[0])
  
    return sorted(answer)
    