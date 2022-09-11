"""
1. BFS로 풀어야 함
2. for문으로 모든 좌표값을 확인 해야함
2-1. 이때 visited가 안됏고, 새로운 그림의 시작점이 있으면 bfs를 시전하고 count += 1(그림의 갯수)
2-2. 큐에서 pop해서 방문처리를 할 때 cnt를 올려서 마지막에 cnt값을 리턴
3. 리턴 받은 cnt와 _max값을 비교하여 가장 큰 넓이를 구함
"""


import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
# 방문한지 안한지
visited = [[0]*m for _ in range(n)]

# 상, 하, 좌, 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y):
    # 초기 셋팅
    q = deque()
    q.append([x, y])
    visited[x][y] = 1

    # 그림의 넓이
    cnt = 0
    while q:
        cur_x, cur_y = q.popleft()
        cnt += 1
      
        for i in range(4):
            nx = cur_x + dx[i]
            ny = cur_y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue

            if not visited[nx][ny] and board[nx][ny] == 1:
                q.append([nx, ny])
                visited[nx][ny] = 1
   
    return cnt


_max = 0
# 그림의 갯수
count = 0
for i in range(n):
    for j in range(m):
        if not visited[i][j] and board[i][j] == 1:
            count += 1
            _max = max(_max, bfs(i, j))

print(count)
print(_max)
