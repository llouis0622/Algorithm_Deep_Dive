N, K = map(int, input().split())
A = [0] * N

for i in range(N):
    A[i] = int(input())

count = 0

for i in range(N - 1, -1, -1):
    if A[i] <= K:
        count += int(K / A[i])
        K = K % A[i]

print(count)