"""
1. BFS로 푼다.
2. 지훈에 대한 BFS와 불에 대한 BFS 둘 다 수행한다.
3. 불에 대한 BFS를 먼저 진행하고 . 위치에 불의 전파시간을 기록한다
4. 이후 지훈에 대한 BFS를 진행하는데, board[nx][ny]가 fire_board[nx][ny]보다 크다면
지훈이가 불 보다 늦게 도착한거니깐 진행을 못하게 해야함
5. 가장자리에 도달하면 종료
"""


import sys
from collections import deque
input = sys.stdin.readline
 
def bfs():
    while f_queue:    # fire BFS
        x, y = f_queue.popleft()
 
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
 
            if nx < 0 or ny < 0 or nx >= R or ny >= C:
                continue
 
            if f_visited[nx][ny] != 0 or graph[nx][ny] == '#':
                continue
 
            f_visited[nx][ny] = f_visited[x][y] + 1
            f_queue.append((nx, ny))
 
    while j_queue:    # jihoon BFS
        x, y = j_queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
 
            if nx < 0 or ny < 0 or nx >= R or ny >= C:
                return j_visited[x][y] + 1    # escape map
 
            if j_visited[nx][ny] != 0 or graph[nx][ny] == '#' or (f_visited[nx][ny] != 0 and f_visited[nx][ny] <= j_visited[x][y]+1):    # important code
                continue
 
            j_visited[nx][ny] = j_visited[x][y] + 1
            j_queue.append((nx, ny))
 
    return 'IMPOSSIBLE'    # not escape map
 
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
 
R, C = map(int, input().split())
graph = [list(input().strip()) for _ in range(R)]
f_queue, j_queue = deque(), deque()    # declare fire, jihoon queue
f_visited, j_visited = [[0] * C for _ in range(R)], [[0] * C for _ in range(R)]    # declare fire, jihoon visited
 
for i in range(R):
    for j in range(C):
        if graph[i][j] == 'F':
            f_queue.append((i, j))
        elif graph[i][j] == 'J':
            j_queue.append((i, j))
print(bfs())