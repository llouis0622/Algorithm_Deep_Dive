def solution(board, h, w):
    n = len(board)
    color = board[h][w]
    dh = [0, 1, -1, 0]
    dw = [1, 0, 0, -1]
    cnt = 0
    for i in range(4):
        num_h = h + dh[i]
        num_w = w + dw[i]
        if 0 <= num_h < n and 0 <= num_w < len(board[0]):
            if board[num_h][num_w] == color:
                cnt += 1
    return cnt