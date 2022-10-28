import sys
sys.setrecursionlimit(10**8)

input = sys.stdin.readline


n = int(input())
graph = [[] for _ in range(n+1)]
for i in range(n-1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

visited = [0] * (n+1)
# dp[i][0]는 i 노드가 얼리어 답터가 아닐 때
# dp[i][1]은 i 노드가 얼리어 답터일 때
dp = [[0, 0] for _ in range(n+1)]


def dfs(parent):
   # 내가 얼리어답터니깐 일단 + 1
    dp[parent][1] = 1
    visited[parent] = 1
    for child in graph[parent]:
        if not visited[child]:
            dfs(child)
            # 내가 얼리어답터가 아닐 때는 자식 노드들이 모두 얼리어답터여야함
            dp[parent][0] += dp[child][1]
            # 내가 얼리어답터일 때는 자식 노드들이
            # 얼리어답터인지 아닌지 상관없이 둘 중 최솟값을 더해줌
            dp[parent][1] += min(dp[child][0], dp[child][1])


dfs(1)
print(min(dp[1][0], dp[1][1]))
