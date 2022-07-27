from collections import deque

n, m, v = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = [False]*(n+1)

for _ in range(m):
  a, b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)

for i in range(n+1):
  graph[i].sort()

"""
1 -> 2 -> 3 -> 4
2 -> 1 -> 4
3 -> 1 -> 4
4 -> 1 -> 2 -> 3

"""

def dfs(v, count):
  visited[v] = True
  print(v, end = ' ')

  for i in graph[v]:
    if not visited[i]:
      dfs(i, count+1)

dfs(v, 1)
print()
visited = [False]*(n+1)

def bfs(v):
  q = deque()
  q.append(v)
  visited[v] = True

  while q:
    i = q.popleft()
    print(i, end = ' ')

    for j in graph[i]:
      if not visited[j]:
        visited[j] = True
        q.append(j)

bfs(v)