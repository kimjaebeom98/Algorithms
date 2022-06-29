import heapq
import sys

input = sys.stdin.readline
t = int(input())


def check(data):
    mid = data[0]
    maxl = []
    minr = []
    result = []
    result.append(mid)
    for idx, val in enumerate(data[1:], 1):
        if val < mid:
            heapq.heappush(maxl, -val)
        else:
            heapq.heappush(minr, val)
        if idx % 2 == 0:
            if len(maxl) > len(minr):
                heapq.heappush(minr, mid)
                mid = -heapq.heappop(maxl)
            elif len(maxl) < len(minr):
                heapq.heappush(maxl, -mid)
                mid = heapq.heappop(minr)
            result.append(mid)
    
    print(len(result))
    for i in range(len(result)):
        if (i+1) != 1 and (i+1) % 10 == 1:
            print()
        print(result[i], end=' ')
    print()


for _ in range(t):
    m = int(input())
    data = []
    if m % 10 == 0:
        for _ in range(m//10):
            data.extend(list(map(int, input().rstrip().split())))
    else:
        for _ in range(m//10 + 1):
            data.extend(list(map(int, input().rstrip().split())))
    check(data)
