def solution(n):
    arr = [[0] * n for _ in range(n)]
    num = 1
    x, y, i, j = 0, 0, 0, 1
    for _ in range(n * n):
        arr[x][y] = num
        num += 1
        if arr[(x + i) % n][(y + j) % n] != 0:
            i, j = j, -i
        x += i
        y += j
    return arr