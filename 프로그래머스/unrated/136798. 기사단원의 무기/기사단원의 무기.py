"""
약수의 개수를 구하는게 포인트
"""
def solution(number, limit, power):
    answer = 0
    res = []
    chk = 1
    for i in range(1, number+1):
        cnt = 0
        flag = 0
        if i ** 0.5 == chk:
            flag = 1
            chk += 1
        
        for k in range(1, int(i**0.5)+1):
            if i % k == 0:
                cnt += 1
        if not flag:
            res.append(cnt * 2)
        else:
            res.append(cnt * 2 -1)
    
    
    return sum([power if r > limit else r for r in res])