n = int(input())
per = list(map(int, input().split()))

dp = list(0 for _ in range(n))
dp[0] = per[0]

for i in range(1, n):
    cur = per[i]
    for j in range(i):
        if per[j] < per[i]:
            dp[i] = max(dp[i], dp[j]+per[i])
        else:
            dp[i] = max(dp[i], per[i])
print(max(dp))

