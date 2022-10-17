import sys
input = sys.stdin.readline
"""
노드의 갯수 + 1만큼  2차원 배열을 만드는데,
자기 자신을 도착하는 노선을 제외하고 나머지 모두에
값이 존재하면 자신의 키가 몇 번째인지 알 수 있음
도착 -> 출발 노선을 -1
출발 -> 도착 노선을 +1

"""


n, m = map(int, input().split())
graph = [[0] * (n+1) for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    # 시작 -> 끝
    graph[a][b] = 1
    graph[b][a] = -1

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            # 자기 자신이거나 이미 값이 있으면
            if i == j or graph[i][j] in [1, -1]:
                continue

            # i보다 k가 크고, k보다 j가 크면
            # 결국 j가 i보다 큰 거니깐 graph[i][j] = 1
            # 나머지들은 -1
            if graph[i][k] + graph[k][j] == 2:
                graph[i][j] = 1
                graph[j][i] = -1
                graph[j][k] = -1
                graph[k][i] = -1


cnt = 0
for i in range(1, n+1):
    if graph[i][1:].count(0) == 1:
        cnt += 1

print(cnt)
