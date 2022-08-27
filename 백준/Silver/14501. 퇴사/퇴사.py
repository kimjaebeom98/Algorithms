import sys

input = sys.stdin.readline

n = int(input())

dp = [0] * 16
for i in range(1, n+1):
  t, p = map(int, input().split())
  if t + i -1 <= n:
    dp[t+i-1] = max((max(dp[:i])+p), dp[t+i-1])

print(max(dp))
