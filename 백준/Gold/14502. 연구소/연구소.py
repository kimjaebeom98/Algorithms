import sys
from itertools import combinations, permutations
from collections import deque
import copy

input = sys.stdin.readline
n, m = map(int, input().split())

tmp = [list(map(int, input().split())) for _ in range(n)]
comb = []
it = [] # 바이러스 초기지역
for i in range(n):
  for j in range(m):
    if tmp[i][j] == 2:
      it.append([i, j])
    if tmp[i][j] == 0:
      comb.append([i, j])

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(it):
  q = deque()
  visited = [[0]*m for _ in range(n)]
  for i in it:
    init_x, init_y = i
    q.append([init_x, init_y])
    visited[init_x][init_y] = 1
  count = 0
  while q:
    x, y = q.popleft()
    count += 1

    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      if nx >= n or nx < 0 or ny >= m or ny < 0:
        continue
      if visited[nx][ny]:
        continue
      if board[nx][ny] == 1:
        continue
      visited[nx][ny] = 1
      board[nx][ny] = 2
      q.append([nx, ny])

  return 


_max = 0
for i in combinations(comb, 3):
  board = copy.deepcopy(tmp)
  
  board[i[0][0]][i[0][1]] = 1
  board[i[1][0]][i[1][1]] = 1
  board[i[2][0]][i[2][1]] = 1

  bfs(it)
  count = 0
  for i in range(n):
    for j in range(m):
      if board[i][j] == 0:
        count += 1
  _max = max(count, _max)

print(_max)