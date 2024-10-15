N = int(input())
A = list(map(int, input().split()))
S = [0] * N

for i in range(1, N):
    idx = i
    num = A[i]

    for j in range(i - 1, -1, -1):
        if A[j] < A[i]:
            idx = j + 1
            break

        if j == 0:
            idx = 0

    for j in range(i, idx, -1):
        A[j] = A[j - 1]

    A[idx] = num

S[0] = A[0]

for i in range(1, N):
    S[i] = S[i - 1] + A[i]

sum = 0

for i in range(0, N):
    sum += S[i]

print(sum)