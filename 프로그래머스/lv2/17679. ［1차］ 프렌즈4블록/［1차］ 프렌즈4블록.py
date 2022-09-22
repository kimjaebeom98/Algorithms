import copy
import collections

def rm(board, m, n):
    answer = 0
    tmp = set()
    for i in range(m-1):
        for j in range(n-1):
            if board[i][j] == board[i][j+1] == board[i+1][j] == board[i+1][j+1] != 0:
                tmp.add((i, j))
                tmp.add((i, j+1))
                tmp.add((i+1, j))
                tmp.add((i+1, j+1))
    answer += len(tmp)
    for t in tmp:
        x, y = t
        board[x][y] = 0
    return board, answer
    

def solution(m, n, board):
    res = 0
    
    board = [list(b) for b in board]
    tmp = copy.deepcopy(board)
    while tmp:
        b, ans = rm(tmp, m, n)
        if ans == 0:
            break
        res += ans
        # n은 열, m은 행
        for j in range(len(b[0])):
            q = collections.deque([])

            for i in range(len(b)-1,-1,-1):
                if b[i][j] == 0:
                    q.append((i,j)) 
                else:
                    if q:
                        qi, qj  = q.popleft()
                        b[qi][qj] = b[i][j]
                        b[i][j] = 0
                        q.append((i, j)) 
        tmp = copy.deepcopy(b)
    
    return res
        