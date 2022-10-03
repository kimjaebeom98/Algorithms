import sys
input = sys.stdin.readline

n = int(input())
arr = [[0, 0, 0]]
for i in range(n):
    r, g, b = map(int, input().rstrip().split())
    arr.append([r, g, b])

"""
dp[i][0] 는 i번째 집까지 칠하는데 드는 최소 비용, 단 red로 칠함
dp[i][1] 는 i번째 집까지 칠하는데 드는 최소 비용, 단 green로 칠함
dp[i][2] 는 i번째 집까지 칠하는데 드는 최소 비용, 단 blue로 칠함

dp[i][0] = min(dp[i-1][1], dp[i-1][2])

"""
dp = [[0 for _ in range(3)] for _ in range(n+1)]
dp[1][0] = arr[1][0]
dp[1][1] = arr[1][1]
dp[1][2] = arr[1][2]
for i in range(2, n+1):
    dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + arr[i][0]
    dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + arr[i][1]
    dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + arr[i][2]

print(min(dp[n][0], dp[n][1], dp[n][2]))
