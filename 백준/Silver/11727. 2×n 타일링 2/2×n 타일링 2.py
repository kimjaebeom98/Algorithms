from sys import stdin

n = int(input())

dp = [0 for _ in range(1002)]

dp[1] = 1
dp[2] = 3

for i in range(3, 1001):
    dp[i] = dp[i-1] + 2*dp[i-2]

print(dp[n]%10007)