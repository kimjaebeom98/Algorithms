import heapq


n  = int(input())
hq = []
for i in range(n):
    s = list(map(int, input().split()))
    for j in s:
        if len(hq) >= n:
            heapq.heappush(hq, j)
            heapq.heappop(hq)
        else:
            heapq.heappush(hq, j)


print(heapq.heappop(hq))
    
    
