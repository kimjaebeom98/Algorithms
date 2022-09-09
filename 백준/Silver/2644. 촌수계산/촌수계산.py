import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline


# 사람의 수
n = int(input())
# 촌수를 구할 사람 두 명
p1, p2 = map(int, input().split())
# 부모-자식 관계의 개수
m = int(input())

graph = [[] for _ in range(n+1)]

for i in range(m):
    # x는 부모, y는 자식
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

visited = [0]*(n+1)


def dfs(parent):
    for i in graph[parent]:
        if not visited[i]:
            visited[i] = visited[parent] + 1
            dfs(i)


dfs(p1)

if visited[p2] == 0:
    print(-1)
else:
    print(visited[p2])