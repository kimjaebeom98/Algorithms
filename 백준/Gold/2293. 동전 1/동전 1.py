n, k = map(int, input().split())
money = []
for i in range(n):
    money.append(int(input()))

money.sort()

# dp[i]는 주어진 동전들로 i를 만들 수 있는 경우의 수
dp = [0] * (k+1)


# i를 만드는 경우의수는
# 화폐의 가치 1, 2, 5가 있다고 가정했을 때
# dp[i]는 dp[i-1] + dp[i-2] + dp[i-5]이다
# i를 1원을 더해서 만들 수 있는 거는
dp[0] = 1
for m in money:
    for i in range(m, k+1):
        dp[i] += dp[i-m]
print(dp[k])