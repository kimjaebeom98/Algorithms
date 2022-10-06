import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
visited = [[0 for _ in range(n)] for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(start_x, start_y, cnt):
    q = deque()
    q.append([start_x, start_y])
    visited[start_x][start_y] = 1
    board[start_x][start_y] = cnt

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue

            if not visited[nx][ny] and board[nx][ny]:
                board[nx][ny] = cnt
                visited[nx][ny] = 1
                q.append([nx, ny])


cnt = 1
for i in range(n):
    for j in range(n):
        if not visited[i][j] and board[i][j]:
            bfs(i, j, cnt)
            cnt += 1


def chk(k):
    global res
    distance = [[-1 for _ in range(n)] for _ in range(n)]
    # 먼저 k에 해당하는 땅들 찾기
    # 거리 초기화
    q = deque()
    for i in range(n):
        for j in range(n):
            if board[i][j] == k:
                q.append([i, j])
                distance[i][j] = 0

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue

            if board[nx][ny] and board[nx][ny] != k:
                res = min(res, distance[x][y])
                return
            if not board[nx][ny] and distance[nx][ny] == -1:
                distance[nx][ny] = distance[x][y] + 1
                q.append([nx, ny])


res = n**2
for i in range(1, cnt):
    chk(i)

print(res)
