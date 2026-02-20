T = int(input())
for i in range(1, T + 1):
    N = int(input())
    A = [list(map(int, input().split())) for _ in range(N)]
    num = 10 ** 9
    check = [0] * N


    def dfs(r, s):
        global num
        if s >= num:
            return
        if r == N:
            num = s
            return
        for j in range(N):
            if check[j] == 0:
                check[j] = 1
                dfs(r + 1, s + A[r][j])
                check[j] = 0


    dfs(0, 0)
    print(f"#{i} {num}")