import heapq


def solution(n, s, a, b, fares):
    graph = [[] for _ in range(n+1)]
    for v1, v2, c in fares:
        graph[v1].append([v2, c])
        graph[v2].append([v1, c])

    def dijkstra(start):
        nonlocal s, a, b, graph, fares, n

        distance = [int(1e6)*len(fares)] * (n+1)
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

    start = dijkstra(s)
    a_s = dijkstra(a)
    b_s = dijkstra(b)
  
    _min = int(1e6)*len(fares)+1

    for i in range(1, n+1):
        _min = min(start[i]+b_s[i]+a_s[i], _min)

    return _min
