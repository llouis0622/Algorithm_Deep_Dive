N, K = map(int, input().split())
F, M = [0] * 1000, [0] * 1000
for _ in range(N):
    S, Y = map(int, input().split())
    if S == 0:
        F[Y] += 1
    else:
        M[Y] += 1
for i in range(1, 7):
    if F[i] % K == 0:
        F[i] = F[i] // K
    else:
        F[i] = (F[i] // K) + 1
    if M[i] % K == 0:
        M[i] = M[i] // K
    else:
        M[i] = (M[i] // K) + 1
print(sum(F) + sum(M))