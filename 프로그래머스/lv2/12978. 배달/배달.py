import heapq
    

def solution(N, road, K):
    graph = [[] for _ in range(N+1)]
    
    for a, b, c in road:
        graph[a].append([b, c])
        graph[b].append([a, c])
    
    distance = [10000 * 2001] * (N+1)
    q = []
    heapq.heappush(q, [0, 1])
    distance[1] = 0
   
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        
        for i in graph[now]:
            cost = dist + i[1]
            
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, [cost, i[0]])
    
    cnt = 0 
    for i in range(1, len(distance)):
        if distance[i] <= K:
            cnt += 1
    return cnt
            
        
