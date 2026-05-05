def solution(n, results):
    win = [[False] * n for _ in range(n)]
    for a, b in results:
        win[a - 1][b - 1] = True
    for i in range(n):
        for j in range(n):
            for k in range(n):
                if win[j][i] and win[i][k]:
                    win[j][k] = True
    ans = 0
    for i in range(n):
        cnt = 0
        for j in range(n):
            if win[i][j] or win[j][i]:
                cnt += 1
        if cnt == n - 1:
            ans += 1
    return ans
