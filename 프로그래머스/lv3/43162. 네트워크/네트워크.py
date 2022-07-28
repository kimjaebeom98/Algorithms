def solution(n, computers):
    graph = [[] for _ in range(n)]

    for i, d in enumerate(computers):
      for idx, data in enumerate(d):
        if idx == i:
          continue
        if data == 1:
          graph[i].append(idx)

    visited = [-1] * n
    def dfs(start):
      nonlocal visited, graph  
      visited[start] = 1

      for i in graph[start]:
        if visited[i] == -1:
          dfs(i)

    count = 0
    for i in range(n):
      if visited[i] == -1:
        dfs(i)
        count+=1
    return count