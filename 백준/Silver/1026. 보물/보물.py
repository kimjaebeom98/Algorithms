import heapq

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))



s = 0
re_b = []
for idx, data in enumerate(b):
  re_b.append((idx, data))

re_b.sort(key = lambda x:x[1], reverse = True) 

re_a = [0 for _ in range(n)]
heap_a = []
for i in range(n):
  heapq.heappush(heap_a, a[i])
for idx, data in re_b:
  re_a[idx] = heapq.heappop(heap_a)


for i in range(n):
  s += b[i]*re_a[i]

print(s)