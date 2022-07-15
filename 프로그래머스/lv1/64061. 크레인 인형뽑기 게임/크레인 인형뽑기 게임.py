def solution(board, moves):
    answer = 0
    stk = []
    for cur in moves:
        cur = cur - 1
        for i in range(len(board)):
            if board[i][cur] != 0:
                if stk and stk[-1] == board[i][cur]:
                    stk.pop()
                    board[i][cur] = 0
                    answer+=2
                    break
                else:
                    stk.append(board[i][cur])
                    board[i][cur] = 0
                    break

    return answer