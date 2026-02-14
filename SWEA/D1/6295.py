N, M = map(int, input().split(', '))
A = [[0] * M for _ in range(N)]
for i in range(N):
    for j in range(M):
        A[i][j] = i * j
print(A)