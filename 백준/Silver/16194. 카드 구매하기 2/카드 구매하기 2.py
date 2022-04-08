from sys import stdin

n = int(stdin.readline())
price_arr = [0] + list(map(int, stdin.readline().split()))

dp = [0]*(n+1)
dp[1] = price_arr[1]
for i in range(2, n+1):
    dp[i] = price_arr[i]
    for k in range(0, i):
        dp[i] = min(dp[i], dp[i-k]+price_arr[k])

print(dp[n])