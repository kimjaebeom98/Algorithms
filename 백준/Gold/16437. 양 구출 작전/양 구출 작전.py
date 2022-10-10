import sys
sys.setrecursionlimit(int(1e6))
input = sys.stdin.readline
n = int(input())
# 각 노드에서 담고 있는 양이나, 늑대
val = [0] * (n+1)
graph = [[] for _ in range(n+1)]
visited = [0] * (n+1)
for i in range(n-1):
    t, a, p = map(str, input().split())
    a = int(a)
    p = int(p)
    if t == 'W':
        a = -a
    val[i+2] = a
    graph[p].append(i+2)
    graph[i+2].append(p)


_max = 0


def dfs(start):
    visited[start] = 1
    tmp = val[start]
    k = 0
    for i in graph[start]:
        if not visited[i]:
            k += dfs(i)

    if tmp < 0:
        if k + tmp > 0:
            return k + tmp
        else:
            return 0
    else:
        if k + tmp > 0:
            return k + tmp
        else:
            return 0


visited[1] = 1
for i in graph[1]:
    kk = dfs(i)
    _max += kk

print(_max)
