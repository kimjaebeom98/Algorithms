


from collections import deque


dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

while True:
  l, r, c = map(int, input().split())
  if l == 0 and r == 0 and c == 0:
    break
  
  bui = [[]*r for _ in range(l)]
  for i in range(l):
    for j in range(r):
      bui[i].append(list(map(str, input())))
    input()

  
  for i in range(l):
    for j in range(r):
      for k in range(c):
        if bui[i][j][k] == 'S':
          s_tmp = (i, j, k)
        if bui[i][j][k] == 'E':
          el, ex, ey = i, j, k
  
  visit = [[[0 for _ in range(c)] for _ in range(r)] for _ in range(l)]
  cnt = [[[0 for _ in range(c)] for _ in range(r)] for _ in range(l)]
  stk = deque()
  stk.append(s_tmp)
  
  while stk:
    z, x, y = stk.popleft()

    visit[z][x][y] = 1
    for i in range(6):
      nz = z + dz[i]
      nx = x + dx[i]
      ny = y + dy[i]

      if 0 <= nz < l and 0 <= nx < r and 0 <= ny < c  and not visit[nz][nx][ny]:
        if bui[nz][nx][ny] == '.' or bui[nz][nx][ny] == 'E':
          stk.append((nz, nx, ny))
          visit[nz][nx][ny] = 1
          cnt[nz][nx][ny] = cnt[z][x][y]+1

  if cnt[el][ex][ey] == 0:
    print("Trapped!")
  else:
    print(f"Escaped in {cnt[el][ex][ey]} minute(s).")
    
    
