from collections import deque

def solution(maps):
    # 상, 하, 좌, 우
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    n = len(maps)
    m = len(maps[0])
    
    def bfs(start_x, start_y):
        nonlocal maps, dx, dy, n, m
        visited = [[-1 for _ in range(m)] for _ in range(n)]
        
        q = deque()
        q.append([start_x, start_y])
        visited[start_x][start_y] = 1
        
        mini = n*m
        flag = 0
        while q:
            x, y = q.popleft()
            
            if x == n-1 and y == m - 1:
                flag = 1
            
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                
                if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == -1:
                    if maps[nx][ny] == 1:
                        visited[nx][ny] = visited[x][y] + 1
                        if nx == n-1 and ny == m-1:
                            mini = min(visited[nx][ny], mini)
                        q.append([nx, ny])
        if flag:
            return mini
        else:
            return -1
    
    return bfs(0, 0)