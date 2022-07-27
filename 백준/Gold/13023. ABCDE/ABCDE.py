n, m = map(int, input().split())

graph = [[] for _ in range(n)]
visited = [False]*n
for _ in range(m):
  a, b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)


def dfs(v, count):
  global flag
  if count == 5 or flag:
    flag = 1
    return
  
  for i in graph[v]:
    if not visited[i]:
      visited[i] = True
      dfs(i, count+1)
      visited[i] = False

flag = 0
for i in range(n):
  visited[i] = True
  dfs(i, 1)
  visited[i] = False
  if flag:
    break


print(flag)