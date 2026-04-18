def rotate(key):
    m = len(key)
    temp = [[0] * m for _ in range(m)]
    for i in range(m):
        for j in range(m):
            temp[j][m - 1 - i] = key[i][j]
    return temp


def check(board, m, n):
    for i in range(n):
        for j in range(n):
            if board[i + m - 1][j + m - 1] != 1:
                return False
    return True


def solution(key, lock):
    m = len(key)
    n = len(lock)
    size = n + 2 * (m - 1)
    board = [[0] * size for _ in range(size)]
    for i in range(n):
        for j in range(n):
            board[i + m - 1][j + m - 1] = lock[i][j]
    for _ in range(4):
        key = rotate(key)
        for x in range(n + m - 1):
            for y in range(n + m - 1):
                for i in range(m):
                    for j in range(m):
                        board[x + i][y + j] += key[i][j]
                if check(board, m, n):
                    return True
                for i in range(m):
                    for j in range(m):
                        board[x + i][y + j] -= key[i][j]
    return False
