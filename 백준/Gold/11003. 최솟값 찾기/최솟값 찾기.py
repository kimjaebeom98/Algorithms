from collections import deque
import sys

input = sys.stdin.readline
n, l = map(int, input().split())
a = list(map(int, input().split()))
tmp = deque()
d = []

tmp.append([0, a[0]])
d.append(a[0])
print(d[0], end=' ')
for idx, data in enumerate(a[1:], 1):
  if idx - tmp[0][0] + 1 > l:
    tmp.popleft()
    while tmp:
      if tmp[-1][1] >= data:
        tmp.pop()
      else:
        break
    tmp.append([idx, data])
  else:
    while tmp:
      if tmp[-1][1] >= data:
        tmp.pop()
      else:
        break
    tmp.append([idx, data])
  print(tmp[0][1], end=' ')