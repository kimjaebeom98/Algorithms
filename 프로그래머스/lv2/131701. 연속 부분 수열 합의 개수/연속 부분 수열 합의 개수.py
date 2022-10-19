def solution(elements):
    n = len(elements)
    res = set()
    for k in range(1, n+1):
        for j in range(n):
            if j+k > n-1:
                res.add(sum(elements[j:] + elements[:j+k-n]))
            else:
                res.add(sum(elements[j:j+k]))
    return len(res)
                