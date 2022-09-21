# bfs

# import sys
# from collections import deque

# input = sys.stdin.readline
# n = int(input().rstrip())

# board = list(list(input().rstrip()) for _ in range(n))
# visited = list([0] * n for _ in range(n))

# # 상, 하, 좌, 우
# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]


# def bfs(start_x, start_y):
#     q = deque()
#     count = 0
#     q.append([start_x, start_y])
#     visited[start_x][start_y] = 1

#     while q:
#         x, y = q.popleft()
#         count += 1

#         for i in range(4):
#             nx = dx[i] + x
#             ny = dy[i] + y
#             if nx < 0 or nx >= n or ny < 0 or ny >= n:
#                 continue

#             if not visited[nx][ny] and board[nx][ny] == '1':
#                 visited[nx][ny] = 1
#                 q.append([nx, ny])

#     return count


# cnt = 0
# res = []
# for i in range(n):
#     for j in range(n):
#         if not visited[i][j] and board[i][j] == '1':
#             res.append(bfs(i, j))
#             cnt += 1
# print(cnt)
# res.sort()
# for i in range(cnt):
#     print(res[i])

# dfs

import sys
input = sys.stdin.readline
n = int(input().rstrip())
board = list(list(map(int, input().rstrip())) for _ in range(n))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def dfs(x, y):
    global cnt
    board[x][y] = 0
    cnt += 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= n or ny < 0 or ny >= n:
            continue
        if board[nx][ny]:
            dfs(nx, ny)


res = []
for i in range(n):
    for j in range(n):
        if board[i][j] == 1:
            cnt = 0
            dfs(i, j)
            res.append(cnt)

print(len(res))
res.sort()
for r in res:
    print(r)
