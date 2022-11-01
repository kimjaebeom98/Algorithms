from collections import deque



n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

max_h = 0
for i in range(n):
    for j in range(n):
        max_h = max(board[i][j], max_h)

def bfs(start_x, start_y):
	q = deque()
	q.append([start_x, start_y])
	visited[start_x][start_y] = 1
	
	dx = [-1, 1, 0, 0]
	dy = [0, 0, -1, 1]
	
	while q:
		x, y = q.popleft()
		
		for i in range(4):
			nx = x + dx[i]
			ny = y + dy[i]
			if 0 <= nx < n and 0 <= ny < n:
				if board[nx][ny] and not visited[nx][ny]:
					q.append([nx, ny])
					visited[nx][ny] = 1
	

answer = 0
for h in range(max_h):
  cnt = 0
  for i in range(n):
    for j in range(n):
      if board[i][j] <= h:
        board[i][j] = 0
  
  visited = [[0]*n for _ in range(n)]
  for i in range(n):
    for j in range(n):
      if board[i][j] and not visited[i][j]:
        bfs(i, j)
        cnt += 1
  
  answer = max(answer, cnt)

print(answer)
      
  