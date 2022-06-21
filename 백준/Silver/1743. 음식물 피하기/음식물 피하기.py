from collections import deque
n, m, k = map(int, input().split())

board = list([0 for _ in range(m)] for _ in range(n))

# 쓰레기 위치에 1로 표시
for _ in range(k):
    r, c = map(int, input().split())
    board[r-1][c-1] = 1

# 상, 하, 좌, 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


# 각 좌표값이 최대로 갈 수 있을 만큼 탐색
def bfs(x, y, board):
    queue = deque()
    queue.append((x,y))
    result = 1
    board[x][y] = 2 # 2는 방문했다는 표시

    
    while queue:
        a, b = queue.popleft()
        
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            
            if 0 <= nx < n and 0 <= ny < m and board[nx][ny] == 1:
                queue.append((nx, ny))
                board[nx][ny] = 2
                result += 1
    return result

temp = board
answer = 0
for i in range(n):
    for j in range(m):
        if board[i][j] == 1:
            ans = bfs(i, j, board)
            answer = max(ans, answer)
            board = temp

print(answer)


