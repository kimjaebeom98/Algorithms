# r : 세로, c : 가로
r, c = map(int, input().split())

# 각 칸에 알파벳이 들어 있는 보드 
board = []
for _ in range(r):
    board.append(list(input()))

# 중복 방지를 위해 set
visit_alpha = set()

# 상, 하, 좌, 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# max count값을 기록할 ans
# 최고 멀리 간 지점까지의 거리만 기록하면 됨
ans = 0

def dfs(x, y, count):
    # 다른 함수에서도 공통인 ans를 사용하기 위함
    global ans
    # 최고 지점을 기록하기 위해
    ans = max(count, ans)
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if 0<= nx < r and 0<= ny < c and not board[nx][ny] in visit_alpha:
            visit_alpha.add(board[nx][ny])
            # 막힐 때 까지 최고 지점까지 
            dfs(nx, ny, count+1)
            # 백트래킹 하기 위하여 
            # 막힌 부분에 도달하고 돌아왔을 때 다른 루트로 가기 위함
            visit_alpha.remove(board[nx][ny])


visit_alpha.add(board[0][0])    
dfs(0, 0, 1)
print(ans)
