def n_to_k(n, k):
    if n < k:
        return str(n)
    q = n // k
    r = n % k
    return n_to_k(q, k) + str(r)

def chk(n):
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return 0
    return 1

def solution(n, k):
    res = n_to_k(n, k)
    res = res.split('0')
    cnt = 0
    for r in res:
        if len(r) and r != '1' and chk(int(r)):
            cnt += 1

    return cnt
    