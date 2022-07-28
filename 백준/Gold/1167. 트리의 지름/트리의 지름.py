import sys

input = sys.stdin.readline

v = int(input())
graph = [[] for _ in range(v+1)]

for _ in range(v):
  tmp = list(map(int, input().split()))
  for i in range(1, len(tmp)-2, 2):
    graph[tmp[0]].append([tmp[i], tmp[i+1]])

visited = [-1]*(v+1)

def dfs(a, b):
  for e, d in graph[a]:
    if visited[e] == -1:
      visited[e] = d + b
      dfs(e, visited[e])


visited[1] = 0
dfs(1, visited[1])
start = visited.index(max(visited))
visited = [-1]*(v+1)
visited[start] = 0
dfs(start, visited[start])
print(max(visited))
