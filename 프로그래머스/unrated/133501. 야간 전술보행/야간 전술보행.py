"""
핵심은 구간을 지나갈 때 그때 그 구간을 감시하는 감시병이 근무중이면
못지나감
"""

def solution(distance, scope, times):
    for i in range(len(scope)):
        scope[i].sort()
    tmp = []
    for i in zip(scope, times):
        tmp.append(i)
    tmp = sorted(tmp, key = lambda x : x[0])
    print(tmp)
    idx = 0
    while idx < distance:
        # 감시하지 않는 구간이라면
        if idx < tmp[0][0][0]:
            idx += 1
        # 감시하는 구간이라면
        elif tmp[0][0][0] <= idx <= tmp[0][0][1]:
            work = tmp[0][1][0]
            rest = tmp[0][1][1]
            q = idx // (work + rest)
            r = idx % (work + rest)
            if r and idx <= q * (work+rest) + work:
                return idx
            else:
                idx += 1
        elif idx > tmp[0][0][1]:
            tmp.pop(0)
            if not tmp:
                return distance
    return distance