from collections import deque



def n_to_k(n, k, res):
    global answer
    if n == 0:
        return res
    r = n % k # 나머지
    q = n // k # 몫
    res.append(r)
    return n_to_k(q, k, res)

def solution(n, k):
    count = 0
    res = n_to_k(n, k, [])
    res = [str(res[i]) for i in range(len(res)-1, -1, -1)]
    res = ''.join(res)
    
    res = res.split('0')
    for num in res:
        if len(num) == 0 or int(num) < 2:
            continue
        num = int(num)
        flag = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                flag = False
        if flag:
            count += 1
    
    return count
            