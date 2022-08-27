import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]

for _ in range(m):
  a, b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)

for i in range(1, n):
  graph[i].sort()

visited = [0] * (n+1)
count = 0
def dfs(start):
  global count
  visited[start]=1
  count += 1

  for i in graph[start]:
    if not visited[i]:
      dfs(i)

dfs(1)
print(count-1)
