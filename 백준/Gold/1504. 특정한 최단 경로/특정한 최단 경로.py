import sys
import heapq
inf = sys.maxsize
input = sys.stdin.readline
n, e = map(int, input().split())
graph = [[] for _ in range(n+1)]

for i in range(e):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])
    graph[b].append([a, c])

v1, v2 = map(int, input().split())


def dijkstra(start):
    distance = [inf] * (n+1)
    distance[start] = 0
    q = []
    heapq.heappush(q, [0, start])

    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, [cost, i[0]])

    return distance


start = dijkstra(1)
v1_s = dijkstra(v1)
v2_s = dijkstra(v2)

cnt = min(start[v1] + v1_s[v2] + v2_s[n], start[v2] + v2_s[v1] + v1_s[n])
if cnt < inf:
    print(cnt)
else:
    print(-1)
