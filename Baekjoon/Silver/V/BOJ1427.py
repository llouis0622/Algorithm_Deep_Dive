import sys

print = sys.stdout.write

A = list(input())

for i in range(len(A)):
    idx = i

    for j in range(i + 1, len(A)):
        if A[j] > A[idx]:
            idx = j

    if A[i] < A[idx]:
        temp = A[i]
        A[i] = A[idx]
        A[idx] = temp

for i in range(len(A)):
    print(A[i])