import sys

input = sys.stdin.readline
n, m = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(n)]


# s[x][y] = x행 y열 까지의 합
s = [[0 for _ in range(n+1)] for _ in range(n+1)]
s[1][1] = board[0][0]

for i in range(1, n+1):
  for j in range(1,n+1):
    if i == 0 and j == 0:
      continue
    else:
      s[i][j] = s[i][j-1] + board[i-1][j-1]

  if i != 1 :
    for j in range(1, n+1):
      s[i][j] = s[i-1][j] + s[i][j]

for _ in range(m):
  x1, y1, x2, y2 = map(int, input().split())
  print(s[x2][y2] - s[x1-1][y2] - s[x2][y1-1] + s[x1-1][y1-1])
  