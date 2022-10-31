import sys
sys.setrecursionlimit(int(1e9))

def solution(a, b, n):
    answer = 0
    
    def recur(a, b, n):
        nonlocal answer
        if n < a:
            return
        
        q = n // a
        r = n % a
        answer += q*b
        recur(a, b, q*b+r)
    
    recur(a, b, n)
    return answer

        