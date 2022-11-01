
from collections import deque

def bfs(x, y):

    # bfs 를 위한 deque
    queue = deque()
    # 처음 start 지점을 enqueue
    queue.append((x, y))
    # 처음 start 지점을 visited 처리 
    visited[0][0] = 1
    # queue가 비어 있지 않는 동안 반복 
    while queue:
        x, y = queue.popleft()
        # 목표 지점에 도달했으면 중단
        #if x == N and y == M:
         #   break

        # 상, 하, 좌, 우 이동
        for i in range(4):
            
            nx = x + dx[i]
            ny = y + dy[i]
            # 상,하,좌,우 이동한 값이 invalid한 영역에 있는지 check
            if nx >= N or nx < 0 or ny >= M or ny < 0:
                continue
            # 벽에 가로 막히는지 check
            if graph[nx][ny] == 0:
                continue
            # 이미 방문한 노드인지 check
            if visited[nx][ny] :
                continue
            # 갈 수 있는 길이라면 
            if graph[nx][ny] == 1:
                # 이전에 방문 한 노드의 값 + 1 즉 이동한 거리
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


    


