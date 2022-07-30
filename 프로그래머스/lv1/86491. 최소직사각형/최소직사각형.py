def solution(sizes):
    tmp_big = []
    tmp_small = []
    
    for a, b in sizes:
        if a >= b:
            tmp_big.append(a)
            tmp_small.append(b)
        else:
            tmp_big.append(b)
            tmp_small.append(a)
    return max(tmp_big)*max(tmp_small)