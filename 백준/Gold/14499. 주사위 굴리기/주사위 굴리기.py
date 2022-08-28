import sys
input = sys.stdin.readline

n, m, x, y, k = map(int, input().split())
board = []

for _ in range(n):
  tmp = list(map(int, input().split()))
  board.append(tmp)

inst = list(map(int, input().split()))
jusawhi = [0] * 6

def chk(i):
  # 현재 주사위 상태
  a, b, c, d, e, f = jusawhi[0], jusawhi[1], jusawhi[2], jusawhi[3], jusawhi[4], jusawhi[5]
  # 동쪽 일때
  if i == 1:
    jusawhi[0], jusawhi[1], jusawhi[2], jusawhi[3], jusawhi[4], jusawhi[5] = c, b, f, a, e, d
  # 서쪽 일때
  if i == 2:
    jusawhi[0], jusawhi[1], jusawhi[2], jusawhi[3], jusawhi[4], jusawhi[5] = d, b, a, f, e, c
  # 북쪽 일때
  if i == 3:
    jusawhi[0], jusawhi[1], jusawhi[2], jusawhi[3], jusawhi[4], jusawhi[5] = b, f, c, d, a, e
  # 남쪽 일때
  if i == 4:
    jusawhi[0], jusawhi[1], jusawhi[2], jusawhi[3], jusawhi[4], jusawhi[5] = e, a, c, d, f, b


# 동, 서, 북, 남
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

nx, ny = x, y
for i in inst:
  nx += dx[i-1]
  ny += dy[i-1] 
  if nx < 0 or nx >=n or ny < 0 or ny >= m:
    nx -= dx[i-1]
    ny -= dy[i-1]

  else:
    if board[nx][ny] != 0 :
      chk(i)
      jusawhi[0] = board[nx][ny] 
      board[nx][ny] = 0
    else:
      chk(i)
      board[nx][ny] = jusawhi[0]

    print(jusawhi[5])