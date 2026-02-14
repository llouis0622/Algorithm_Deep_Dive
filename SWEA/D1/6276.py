A = [[] for _ in range(8)]
for i in range(2, 10):
    for j in range(1, 10):
        if (i * j) % 3 != 0 and (i * j) % 7 != 0:
            A[i - 2].append(i * j)
print(A)