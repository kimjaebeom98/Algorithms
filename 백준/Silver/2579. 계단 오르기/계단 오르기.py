n = int(input())
arr = [0]
for i in range(n):
    arr.append(int(input()))

# dp[i][j] 현재까지 j개의 계단을 연속해서 밟고,
# i번째 계단에 올라섰을 때 점수 합의 최댓값
# 단 i번째 계단은 반드시 밟아야함

dp = [[0 for _ in range(3)] for _ in range(n+1)]
if n == 1:
    print(arr[1])
    exit(0)

dp[1][1] = arr[1]
dp[1][2] = 0
dp[2][1] = arr[2]
dp[2][2] = arr[1] + arr[2]

# dp[k][1] = 연속해서 1개의 계단을 연속해서 밟고 k번째 계단에 있는거니깐
# k번째 계단은 이미 밟고 있으니 바로 직전꺼를 밟지 않았다는 소리
# dp[k][1] = dp[k-2][1] + arr[k], dp[k-2][2] + arr[k] 중 맥스
# dp[k][2] = 연속해서 2개의 계단을 연속해서 밟고 k번째 계단에 있다는 소리니깐
# k번째 계단은 이미 밟고 있고 이전꺼도 밟아서 왓다는소리
# 그러나 이번껏도 밟고 있고 이전껏도 밟았으니 그 전에꺼는 밟으면 안됨
# dp[k][2] = dp[k-1][1] + arr[k]

for i in range(3, n+1):
    dp[i][1] = max(dp[i-2][1], dp[i-2][2]) + arr[i]
    dp[i][2] = dp[i-1][1] + arr[i]

print(max(dp[n][1], dp[n][2]))
