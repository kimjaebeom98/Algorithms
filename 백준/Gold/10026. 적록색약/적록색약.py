from collections import deque
import sys
sys.setrecursionlimit(int(1e9))


n = int(input())
board = [list(input()) for _ in range(n)]
visited = [[0 for _ in range(n)] for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def normal_bfs(start_x, start_y):
    q = deque()
    q.append([start_x, start_y])
    visited[start_x][start_y] = 1

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue

            if not visited[nx][ny] and board[nx][ny] == board[start_x][start_y]:
                q.append([nx, ny])
                visited[nx][ny] = 1


def dfs(start_x, start_y):
    visit[start_x][start_y] = 1

    for i in range(4):
        nx = start_x + dx[i]
        ny = start_y + dy[i]

        if nx < 0 or nx >= n or ny < 0 or ny >= n:
            continue
        if board[start_x][start_y] != board[nx][ny]:
            continue
        if not visit[nx][ny]:
            dfs(nx, ny)


normal_cnt = 0
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            normal_bfs(i, j)
            normal_cnt += 1


for i in range(n):
    for j in range(n):
        if board[i][j] == 'G':
            board[i][j] = 'R'


visit = [[0 for _ in range(n)] for _ in range(n)]
cnt = 0
for i in range(n):
    for j in range(n):
        if not visit[i][j]:
            dfs(i, j)
            cnt += 1

print(normal_cnt)
print(cnt)
