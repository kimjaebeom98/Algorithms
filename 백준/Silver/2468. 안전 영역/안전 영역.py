"""
지역의 높이 정보를 파악 
물에 잠기지 않는 안전한 영역이 최대로 몇개가 있는지
일정한 높이 이하의 모든 지점은 물에 잠긴다고 가정
먼저 bfs로 해당 높이 아래인 녀석들을 다 마킹해줌 
마킹 아닌것들을 또 bfs 해주면 됨!
"""

import sys
from collections import deque
import copy

input = sys.stdin.readline
n = int(input().rstrip())
map = list(list(map(int, input().rstrip().split())) for _ in range(n))
visited = [[0] * n for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(start_x, start_y, h):
    q = deque()
    q.append([start_x, start_y])
    board[start_x][start_y] = 101

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            # 마킹이 안돼있고 일정 높이 이하이면 마킹해줌
            if board[nx][ny] != 101 and board[nx][ny] <= h:
                board[nx][ny] = 101
                q.append([nx, ny])


def bfs2(start_x, start_y):
    q = deque()
    q.append([start_x, start_y])
    board[start_x][start_y] = 101

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            # 마킹이 안돼있고 일정 높이 이하이면 마킹해줌
            if board[nx][ny] != 101:
                board[nx][ny] = 101
                q.append([nx, ny])


_max = 0
for b in map:
    _max = max(max(b), _max)

m = 0
for k in range(_max+1):
    board = copy.deepcopy(map)
    for i in range(n):
        for j in range(n):
            if board[i][j] != 101 and board[i][j] <= k:
                bfs(i, j, k)
    cnt = 0
    for i in range(n):
        for j in range(n):
            if board[i][j] != 101:
                bfs2(i, j)
                cnt += 1
    
    if m < cnt:
        m = cnt

print(m)
