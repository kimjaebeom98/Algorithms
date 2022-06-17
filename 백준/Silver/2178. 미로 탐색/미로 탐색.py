from collections import deque



def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    visited[0][0] = 1
    while queue:
        x, y = queue.popleft()
        if x == N and y == M:
            break
        for i in range(4):
            
            nx = x + dx[i]
            ny = y + dy[i]

            if nx >= N or nx < 0 or ny >= M or ny < 0:
                continue
        
            if graph[nx][ny] == 0:
                continue

            if visited[nx][ny] :
                continue

            if graph[nx][ny] == 1:
                visited[nx][ny] = visited[x][y] + 1
                queue.append((nx, ny))

    
    return visited[N-1][M-1]


N, M = map(int, input().split())
graph = []
for i in range(N):
    graph.append(list(map(int, input())))

# 상, 하, 좌, 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

visited = [[0 for _ in range(M)] for _ in range(N)]

print(bfs(0, 0))


    


