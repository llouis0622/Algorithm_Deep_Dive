N = int(input())
A = list(map(int, input().split()))
L = [0] * N
L[0] = A[0]
result = L[0]
for i in range(1, N):
    L[i] = max(A[i], L[i - 1] + A[i])
    result = max(result, L[i])
R = [0] * N
R[N - 1] = A[N - 1]
for i in range(N - 2, -1, -1):
    R[i] = max(A[i], R[i + 1] + A[i])
for i in range(1, N - 1):
    temp = L[i - 1] + R[i + 1]
    result = max(result, temp)
print(result)