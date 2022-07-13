def solution(N, stages):
    answer = []

    fail = [0 for _ in range(N+1)]
    stop = [0 for _ in range(N+1)]
    pa = [0 for _ in range(N+1)]
    for i in range(1, N+1):
      for j in stages:
        if  j >= i:
          pa[i] += 1
    
    for i in stages:
        if not i > N:
          stop[i] += 1

    
    for i in range(1, N+1):
      if pa[i]:
        fail[i] = stop[i] / pa[i]
      else:
        fail[i] = 0

    res = []
    for idx, data in enumerate(fail):
      res.append((idx, data))
    
    res = sorted(res[1:],key=lambda x:-x[1])
    for idx, data in res:
      answer.append(idx)
    
    return answer
