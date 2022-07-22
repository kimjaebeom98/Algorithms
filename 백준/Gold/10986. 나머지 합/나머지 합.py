import sys

input = sys.stdin.readline
n, m = map(int, input().split())
a = list(map(int, input().split()))

s = [0 for _ in range(n)]
s[0] = a[0]
for i in range(1, n):
  s[i] = s[i-1] + a[i]


cnt = 0 # (i, j) 구간이 m으로 나누어 떨어 지는 횟수
s_m = [0 for _ in range(m)]
for i in range(n):
  r = s[i] % m
  if r == 0: # (0 ~ i)까지의 구간
    cnt += 1 
  s_m[r] += 1

for i in s_m:
  if i == 0:
    continue

  cnt += i*(i-1)/2
  # i개 중 2개를 뽑는 경우의 수 : i*(i-1)/2

print(int(cnt))