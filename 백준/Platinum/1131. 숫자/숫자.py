INF = 9876543210
cache=[INF]*10000001 # 노드들을 처음 값으로 무한 값으로 초기화
A, B, K = map(int, input().split())


def dfs(n):
  # 처음 방문 노드 
  if cache[n] == INF:
    cache[n] = 0 #임시마크
    n_next = sum(int(ch)**K for ch in str(n))
    cache[n] = min(n, dfs(n_next)) 
  # INF 값이 아니라면 처음 방문 노드가 아니고
  # 예를 들어 n = 2일 때, cache[n] = min(n, dfs(n_sum)) 에서
  # n_sum = 2, 4, 16, 37, 58, 89, 142, 42, 20, 4
  # n_sum은 4일 때 cache[n_sum] = 0이니깐 else로 들어 올 수 있음
  # 즉 이제 한 사이클로 다 돌았고 이후에 4, 16, 37, 58, 89, 142, 42, 20 반복
  else:
    # (방문 했고,)
    # 처리가 된 n값이라면
    if cache[n] :
      return cache[n]
    
    minimum = n 
    nn = sum(int(ch)**K for ch in str(n))
    # 또 사이클을 돌 거임
    # 왜냐하면 사이클에서 가장 작은 최솟 값을 구하기 위해
    # 사이클에서 가장 작은 최솟 값은 사이클에 속하는 n 값들의 최솟값도
    # 같으니깐
    while nn != n:
      minimum = min(minimum, nn)
      nn = sum(int(ch)**K for ch in str(nn))

    # 사이클 내 최솟값 찾음
    cache[n] = minimum
    nn = sum(int(ch)**K for ch in str(n))
    # 사이클 내 노드들에 최솟값 삽입
    while nn != n:
      cache[nn] = minimum
      nn = sum(int(ch)**K for ch in str(nn))

  return cache[n]


print(sum(dfs(i) for i in range(A, B+1)))