import sys
sys.setrecursionlimit(10000)

def dfs(v):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            dfs(i)

input = sys.stdin.readline


N, M = map(int, input().split())
visited = [False]*(N+1)

graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in graph : 
    i.sort()

count = 0

for i in range(1, N+1):
    if visited[i] == False:
        dfs(i)
        count+=1

print(count)



    