"""
1. n을 k진수로 변환
2. 변환된 값에서 원소 하나씩 살펴보는데 0이 아니면 stk에 넣고, 0을 만나면 stk를 다 뽑는 식으로
3. stk에서 뽑은 거는 소수 판단해줌
"""
from collections import deque

def solution(n, k):
    cnt = 0
    n_to_k = ''
    tmp = []
    while n:
        r = n % k
        n = n // k
        tmp.append(str(r))
    while tmp:
        i = tmp.pop()
        n_to_k += i
    
    n_to_k = n_to_k.split('0')
    for num in n_to_k:
        if len(num) == 0 or num == '1':
            continue
        else:
            num = int(num)
            flag = 0
            
            for i in range(2, int(num ** 0.5)+1):
                if num % i == 0:
                    flag = 1
                    break
            if not flag:
                cnt += 1
    return cnt