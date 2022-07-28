from itertools import permutations

def solution(numbers):
    answer = 0
    a = set()
    for i in range(1, len(numbers)+1):
        for j in permutations(numbers, i):
            s = ''.join(j)
            a.add(int(s))
    
    a = list(a)
    for i in a:
        if i == 0 or i == 1:
            continue
        flag = 0
        for j in range(2, int(i**0.5)+1):
            if i % j == 0:
                flag = 1
                break
                
        if not flag:
            answer += 1
    
    return answer