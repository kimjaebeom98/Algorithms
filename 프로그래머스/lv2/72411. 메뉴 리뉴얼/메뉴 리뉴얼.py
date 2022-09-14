"""
course로 첫 for문을 시작했을 때, 
예를 들어 c가 2라고 하면 orders를 뽑아내서 combination 적용시켜서
하면됨 그러고나서 Counter
"""
from itertools import combinations
from collections import Counter

def solution(orders, course):
    result = []
    chk = {}
    for c in course:
        tmp = []
        for order in orders:
            order = list(order)
            order.sort()
            # course요리를 구성하는 메뉴 갯수 만큼의 조합을 뽑아냄
            for combi in combinations(order, c):
                combi = ''.join(combi)
                tmp.append(combi)
        new = Counter(tmp).most_common()
  
        if len(new) == 0 or new[0][1] < 2:
            continue
        result.append(new[0][0])
        _max = new[0][1]
        for data in new[1:]:
            if data[1] < _max:
                break
            else:
                result.append(data[0])
       
    result.sort()
    return result
        
        
        