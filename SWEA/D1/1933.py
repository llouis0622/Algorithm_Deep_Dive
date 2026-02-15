N = int(input())
A = []
for i in range(1, N + 1):
    if N % i == 0:
        A.append(str(i))
print(' '.join(A))