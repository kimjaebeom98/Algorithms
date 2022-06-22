from collections import deque
t = int(input())

dx = [-1, -2, -2, -1, 1, 2, 2, 1]
dy = [-2, -1, 1, 2, 2, 1, -1, -2]

def bfs(x, y, l, i, j):
    queue = deque()
    queue.append((x, y))

    board[x][y] = 1
    while queue:
        a, b = queue.popleft()
        
        if a == i and b == j:
            break

        for k in range(8):
            nx = a + dx[k]
            ny = b + dy[k]

            if 0 <= nx < l and 0 <= ny < l and board[nx][ny] == 0 :
                board[nx][ny] = board[a][b] + 1
                queue.append((nx, ny))
    return board[i][j] - 1
            

for _ in range(t):
    l = int(input())
    board = list([0 for _ in range(l)] for _ in range(l))
    start_x, start_y = map(int, input().split()) # 나이트 현재 위치
    dest_x, dest_y = map(int, input().split())
    if start_x == dest_x and start_y == dest_y:
        print(0)
        continue
    print(bfs(start_x, start_y, l, dest_x, dest_y))

