"""
# 토마토가 다 익을 때 까지 날짜 구하기
# 익지 못하는 게 하나라도 있으면 -1 
# 이미 다 익어있으면 0

1. BFS로 품
2. 시작점이 여러개일 수도 잇음
2-1 2중 for문으로 모두를 탐색하는데 맨 처음,
not visited and board[x][y] == 1 를 찾아서
x, y를 q에 삽입, 만약 찾지를 못했으면 -1, 만약 len(q) = nxm이면 0

2-2 q가 빌 때 까지 팝하고 탐색 반복
3. 2중 for문으로 돌려서 0이 하나라도 있으면 -1  
"""
import sys
from collections import deque

input = sys.stdin.readline
m, n = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
visited = [[-1]*m for _ in range(n)]

# 초기 셋팅
q = deque()
for i in range(n):
    for j in range(m):
        if board[i][j] == 1:
            q.append([i, j])

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

while q:
    x, y = q.popleft()

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue
        if board[nx][ny] == -1:
            continue
        if board[nx][ny] == 0:
            board[nx][ny] = board[x][y] + 1
            q.append([nx, ny])

_max = -1
for i in range(n):
    for j in range(m):
        if board[i][j] == 0:
            print(-1)
            exit(0)
        _max = max(board[i][j], _max)

print(_max-1)
