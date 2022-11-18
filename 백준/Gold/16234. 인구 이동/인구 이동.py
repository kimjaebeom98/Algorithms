import sys
from collections import deque

input = sys.stdin.readline
n, l, r = map(int, input().split())
board = list(list(map(int, input().split())) for _ in range(n))
tmp = [[0] * n for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(start_x, start_y, val):
  q = deque()
  q.append([start_x, start_y])
  visited[start_x][start_y] = val
  chk = 0
  _sum = 0
  while q:
    x, y = q.popleft()
    chk += 1
    _sum += board[x][y]
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0 <= nx < n and 0 <= ny < n:
        if not visited[nx][ny] and l <= abs(board[x][y] - board[nx][ny]) <= r :
          visited[nx][ny] = val
          q.append([nx, ny])
  return chk, _sum

cnt = 0
while cnt < 2001:
  visited = [[0] * n for _ in range(n)]
  res = []
  val = 1
  flag = 0
  for i in range(n):
    for j in range(n):
      if not visited[i][j]:
        count, _sum = bfs(i, j, val)
        if count > 1:
          flag = 1 
        res.append([val, _sum // count])
        val += 1
  
  if not flag:
    break

  for i in range(n):
    for j in range(n):
      # val이 담겨져 있슴
      board[i][j] = res[visited[i][j]-1][1]

  cnt += 1
      
if cnt == 2001:
  print(2000)
else:
  print(cnt)
  