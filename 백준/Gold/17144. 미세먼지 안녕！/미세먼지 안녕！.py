import sys


input = sys.stdin.readline
r, c, t = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(r)]


for i in range(r):
    if board[i][0] == -1:
        up = i
        down = i+1
        break


def bfs():
    tmp = [[0 for _ in range(c)] for _ in range(r)]
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    for x in range(r):
        for y in range(c):
            if board[x][y] != 0 and board[x][y] != -1:
                k = board[x][y] // 5
                cnt = 0
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if 0 <= nx < r and 0 <= ny < c and board[nx][ny] != -1:
                        cnt += 1
                        tmp[nx][ny] += k
                board[x][y] -= k * cnt

    for i in range(r):
        for j in range(c):
            board[i][j] += tmp[i][j]

    return


def air_up():
    dx = [0, -1, 0, 1]
    dy = [1, 0, -1, 0]
    direct = 0
    before = 0
    x, y = up, 1
    while True:
        nx = x + dx[direct]
        ny = y + dy[direct]
        if x == up and y == 0:
            break
        if nx < 0 or nx >= r or ny < 0 or ny >= c:
            direct += 1
            continue
        board[x][y], before = before, board[x][y]
        x = nx
        y = ny


def air_down():
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    direct = 0
    before = 0
    x, y = down, 1
    while True:
        nx = x + dx[direct]
        ny = y + dy[direct]
        if x == down and y == 0:
            break
        if nx < 0 or nx >= r or ny < 0 or ny >= c:
            direct += 1
            continue
        board[x][y], before = before, board[x][y]
        x = nx
        y = ny


time = 0
while time < t:
    bfs()
    air_up()
    air_down()
    time += 1

res = 0
for i in range(r):
    for j in range(c):
        if board[i][j] != -1:
            res += board[i][j]

print(res)
