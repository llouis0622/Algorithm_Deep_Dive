def solution(board, skill):
    n, m = len(board), len(board[0])
    arr = [[0] * (m + 1) for _ in range(n + 1)]
    for t, r1, c1, r2, c2, i in skill:
        if t == 1:
            i = -i
        arr[r1][c1] += i
        arr[r1][c2 + 1] -= i
        arr[r2 + 1][c1] -= i
        arr[r2 + 1][c2 + 1] += i
    for i in range(n):
        for j in range(1, m):
            arr[i][j] += arr[i][j - 1]
    for j in range(m):
        for i in range(1, n):
            arr[i][j] += arr[i - 1][j]
    ans = 0
    for i in range(n):
        for j in range(m):
            if board[i][j] + arr[i][j] > 0:
                ans += 1
    return ans
