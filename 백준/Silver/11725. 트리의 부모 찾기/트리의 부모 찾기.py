import sys
from collections import deque

input = sys.stdin.readline
n = int(input())
tree = [[] for _ in range(n+1)]

for _ in range(n-1):
  a, b = map(int, input().split())
  tree[a].append(b)
  tree[b].append(a)

for i in range(1, n+1):
  tree[i].sort()

def bfs(start):
  q = deque([start])
  visited = [0] * (n+1)
  visited[start] = 1

  res = [0]*(n+1)
  while q:
    parent = q.popleft()
    
    for i in tree[parent]:
      if not visited[i]:
        visited[i] = 1
        q.append(i)
        res[i] = parent

  return res

res = bfs(1)
for i in range(2, len(res)):
  print(res[i])
