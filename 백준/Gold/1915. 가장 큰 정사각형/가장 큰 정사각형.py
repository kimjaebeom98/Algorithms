n, m = map(int, input().split())

board = [list(map(int, input())) for _ in range(n)]
ans = max(board[0])
for i in range(1, n):
    for j in range(1, m):
        if board[i][j] == 1 :
            board[i][j] = min(board[i-1][j-1], board[i-1][j], board[i][j-1]) + 1
    ans = max(ans, max(board[i]))

print(ans**2)
                        
