from collections import deque

# 행, 열
r, c = map(int, input().split())
cur_x, cur_y, d = map(int, input().split())

board = list(list(map(int, input().split())) for _ in range(r))

# 북, 동, 남, 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

backmoving = [[1, 0], [0, -1], [-1, 0], [0, 1]]

visited = [[0] * c for _ in range(r)]
q = deque()
# 현재위치, 바라보는 방향
q.append([cur_x, cur_y, d])
visited[cur_x][cur_y] = 1
cnt = 1
while q:
  x, y, di = q.popleft()
  # 청소한 곳

  flag = 0
  for i in range(4):
    if di == 0:
      di = 4
    di -= 1
    nx = x + dx[di] 
    ny = y + dy[di] 

    if 0 <= nx < r and 0 <= ny < c :
      # 1
      if not visited[nx][ny] and not board[nx][ny]:
        flag = 1
        visited[nx][ny] = 1
        cnt += 1
        q.append([nx, ny, di])
        break
        
  if not flag:
    if di == 4:
      di = 0
    
    if x + backmoving[di][0] < 0 or x + backmoving[di][0] >= r or y + backmoving[di][1] < 0 or y + backmoving[di][1] >= c or board[x+backmoving[di][0]][y+backmoving[di][1]] == 1:
      break
    else:
      x += backmoving[di][0]
      y += backmoving[di][1]
      q.append([x, y, di])

print(cnt)
    
    
  