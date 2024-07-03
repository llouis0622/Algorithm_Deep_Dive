def solution(board):
    dic = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    arr = set()
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 1:
                arr.add((i, j))
                for x, y in dic:
                    ni, nj = i + x, j + y
                    if 0 <= ni < len(board) and 0 <= nj < len(board):
                        arr.add((ni, nj))
    return len(board) * len(board) - len(arr)