import heapq

def solution(n, paths, gates, summits):
    graph = [[] for _ in range(n+1)]
    
    def dijkstra():
        visited = [10000001] * (n+1)
        q = []
        for g in gates:
            heapq.heappush(q, [0, g])
            visited[g] = 0
        
        while q:
            intensity, now = heapq.heappop(q)
            
            if now in summits or intensity > visited[now]:
                continue
            
            # i[0] : 연결된 노드번호
            # i[1] : 비용
            for i in graph[now]:
                cost = max(intensity, i[1])
                if cost < visited[i[0]]:
                    heapq.heappush(q, [cost, i[0]])
                    visited[i[0]] = cost
        
        res = []
        for s in list(summits):
            res.append([s, visited[s]])
        
        res = sorted(res, key=lambda x : (x[1], x[0]))
        return res[0]
            
        
    summits = set(summits)
    for a, b, c in paths:
        graph[a].append([b, c])
        graph[b].append([a, c])
    
    return dijkstra()
    
        
    