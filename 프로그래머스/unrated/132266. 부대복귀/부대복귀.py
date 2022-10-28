import heapq

def dijkstra(n, graph, start):
    hq = []
    distance = [int(1e9)] * (n+1)
    heapq.heappush(hq, [0, start])
    distance[start] = 0
    
    while hq:
        dist, now = heapq.heappop(hq)
        if dist > distance[now]:
            continue
        
        for i in graph[now]:
            cost = dist + i[1]
            if distance[i[0]] > cost:
                heapq.heappush(hq, [cost, i[0]])
                distance[i[0]] = cost
    return distance


def solution(n, roads, sources, destination):
    graph = [[] for _ in range(n+1)]
    tmp = set()
    for a, b in roads:
        graph[a].append([b, 1])
        graph[b].append([a, 1])
    dist = dijkstra(n, graph, destination)
    
    res = []
    for s in sources:
        if dist[s] == int(1e9):
            res.append(-1)
        else:
            res.append(dist[s])
    
    return res