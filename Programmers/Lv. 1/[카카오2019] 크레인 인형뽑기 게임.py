def solution(board, moves):
    stk = []
    cnt = 0
    for i in moves:
        col = i - 1
        for row in range(len(board)):
            if board[row][col] != 0:
                doll = board[row][col]
                board[row][col] = 0
                if stk and stk[-1] == doll:
                    stk.pop()
                    cnt += 2
                else:
                    stk.append(doll)
                break
    return cnt