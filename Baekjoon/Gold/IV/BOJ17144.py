import sys

R, C, T = map(int, sys.stdin.readline().split())
A = [list(map(int, sys.stdin.readline().split())) for _ in range(R)]
temp = [i for i in range(R) if A[i][0] == -1]
up, down = temp[0], temp[1]
dx = (-1, 1, 0, 0)
dy = (0, 0, -1, 1)


def spread():
    add = [[0] * C for _ in range(R)]
    for i in range(R):
        for j in range(C):
            if A[i][j] > 0:
                v = A[i][j] // 5
                if v:
                    cnt = 0
                    for k in range(4):
                        ni, nj = i + dx[k], j + dy[k]
                        if 0 <= ni < R and 0 <= nj < C and A[ni][nj] != -1:
                            add[ni][nj] += v
                            cnt += 1
                    A[i][j] -= v * cnt
    for i in range(R):
        for j in range(C):
            if A[i][j] != -1:
                A[i][j] += add[i][j]


def cal():
    for i in range(up - 1, 0, -1):
        A[i][0] = A[i - 1][0]
    for j in range(0, C - 1):
        A[0][j] = A[0][j + 1]
    for i in range(0, up):
        A[i][C - 1] = A[i + 1][C - 1]
    for j in range(C - 1, 1, -1):
        A[up][j] = A[up][j - 1]
    A[up][1] = 0
    for i in range(down + 1, R - 1):
        A[i][0] = A[i + 1][0]
    for j in range(0, C - 1):
        A[R - 1][j] = A[R - 1][j + 1]
    for i in range(R - 1, down, -1):
        A[i][C - 1] = A[i - 1][C - 1]
    for j in range(C - 1, 1, -1):
        A[down][j] = A[down][j - 1]
    A[down][1] = 0
    A[up][0] = -1
    A[down][0] = -1


for _ in range(T):
    spread()
    cal()
ans = 0
for i in range(R):
    for j in range(C):
        if A[i][j] > 0:
            ans += A[i][j]
print(ans)