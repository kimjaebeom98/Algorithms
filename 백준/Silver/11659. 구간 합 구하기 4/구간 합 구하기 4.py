import sys

input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))

s = [0 for _ in range(n)]
s[0] = arr[0]
for i in range(1, n):
  s[i] = s[i-1] + arr[i]


for _ in range(m):
  l, r = map(int, input().split())
  if l-2 >= 0:
    print(s[r-1] - s[l-2])
  else:
    print(s[r-1])