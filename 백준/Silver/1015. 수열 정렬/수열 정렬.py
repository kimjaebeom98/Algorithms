n = int(input())
a = list(map(int, input().split()))

q = []
for idx, data in enumerate(a):
  q.append([idx, data])

q.sort(key=lambda x:x[1])

p = list(0 for _ in range(n))

idx = 0
for data in q:
  p[data[0]] = idx
  idx+=1
  
for i in p:
  print(i, end=' ')
