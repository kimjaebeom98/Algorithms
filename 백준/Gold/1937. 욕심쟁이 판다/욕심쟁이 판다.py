import sys

sys.setrecursionlimit(10**6)

n = int(input())
board = list(list(map(int, input().split())) for _ in range(n))
dp = [[-1] * n for _ in range(n)]

# 상, 하, 좌, 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def dfs(start_x, start_y):
    if dp[start_x][start_y] == -1:
        dp[start_x][start_y] = 0
        for i in range(4):
            nx = start_x + dx[i]
            ny = start_y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and board[nx][ny] > board[start_x][start_y]:
                dp[start_x][start_y] = max(dp[start_x][start_y], dfs(nx, ny))

    return dp[start_x][start_y] + 1


maximum = 0
for x in range(n):
    for y in range(n):
        k = dfs(x, y)
        maximum = max(maximum, k)


print(maximum)
