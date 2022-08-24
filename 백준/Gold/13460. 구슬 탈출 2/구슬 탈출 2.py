from collections import deque

n, m = map(int, input().split())
board = [input() for _ in range(n)]

for i in range(n):
    for j in range(m):
        if board[i][j] == 'R':
            rx, ry = i, j
        if board[i][j] == 'B':
            bx, by = i, j

# 상, 하, 좌, 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(rx, ry, bx, by):
    q = deque()
    q.append([rx, ry, bx, by, 1])
    visited = []
    visited.append([rx, ry, bx, by])
    
    
    while q:
        rx, ry, bx, by, count = q.popleft()

        if count > 10:
            break
        
        for i in range(4):
            r_nx = rx
            r_ny = ry
            r_m = 0
            while board[r_nx+dx[i]][r_ny+dy[i]] != '#' and board[r_nx][r_ny] != 'O':
                r_nx += dx[i]
                r_ny += dy[i]
                r_m += 1

            b_nx = bx
            b_ny = by
            b_m = 0
            while board[b_nx+dx[i]][b_ny+dy[i]] != '#' and board[b_nx][b_ny] != 'O':
                b_nx += dx[i]
                b_ny += dy[i]
                b_m += 1
            if board[b_nx][b_ny] != 'O':
                # 레드 구슬 먼저 탈출
                if board[r_nx][r_ny] == 'O':
                    print(count)
                    return
                # 같은 자리
                # 많이 움직인게 더 뒤에서 출발한거니깐 뒤로 무름
                if r_nx == b_nx and r_ny == b_ny:
                    if r_m > b_m:
                        r_nx -= dx[i]
                        r_ny -= dy[i]
                    else:
                        b_nx -= dx[i]
                        b_ny -= dy[i]
                
                if [r_nx, r_ny, b_nx, b_ny] not in visited:
                    visited.append([r_nx, r_ny, b_nx, b_ny])
                    q.append([r_nx, r_ny, b_nx, b_ny, count+1])
                

    print(-1)
    return

bfs(rx, ry, bx, by)
            



            
                    
            



            

