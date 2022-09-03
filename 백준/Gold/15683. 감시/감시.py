import copy
import sys

input = sys.stdin.readline
n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

# 북, 동, 남, 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

direction = {

    1: [[0], [1], [2], [3]],
    2: [[0, 2], [1, 3]],
    3: [[0, 1], [1, 2], [2, 3], [3, 0]],
    4: [[3, 0, 1], [0, 1, 2], [3, 2, 1], [2, 3, 0]],
    5: [[0, 1, 2, 3]]
}

cctv = []
for i in range(n):
    for j in range(m):
        if 1 <= board[i][j] <= 5:
            # cctv 위치와 종류(몇 번 cctv인지)
            cctv.append([i, j, board[i][j]])

_min = 1e9


def chk(x, y, dir, tmp):
    # cctv가 현재 방향으로, 감시가 가능한 구역찾기
    for i in dir:
        nx, ny = x, y
        while True:
            nx += dx[i]
            ny += dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m or tmp[nx][ny] == 6:
                break
            elif tmp[nx][ny] == 0:
                tmp[nx][ny] = 7


def dfs(depth, board):
    global _min


    # 모든 cctv 감시구역 체크가 끝났으면 사각지대 갯수를 구함
    if depth == len(cctv):
        cnt = 0
        for t in board:
          cnt += t.count(0)
        # 최소 감시구역 갯수 구하기
        _min = min(_min, cnt)
        return

    tmp = copy.deepcopy(board)
    x, y, cctv_type = cctv[depth]

    # cctv의 종류에 따른 감시구역을 구함
    for di in direction[cctv_type]:
        chk(x, y, di, tmp)
        dfs(depth+1, tmp)
        tmp = copy.deepcopy(board)


dfs(0, board)
print(_min)
