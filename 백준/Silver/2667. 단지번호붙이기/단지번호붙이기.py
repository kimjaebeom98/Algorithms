import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
board = []
for _ in range(n):
    board.append(list(map(int, input().rstrip())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

answer = []


def bfs(board, start_x, start_y):
    q = deque()
    q.append([start_x, start_y])
    board[start_x][start_y] = 0

    count = 1
    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if board[nx][ny] == 1:
                    board[nx][ny] = 0
                    count += 1
                    q.append([nx, ny])
    return count


for i in range(n):
    for j in range(n):
        if board[i][j] == 1:
            answer.append(bfs(board, int(i), int(j)))


print(len(answer))
answer.sort()
for i in answer:
    print(i)
