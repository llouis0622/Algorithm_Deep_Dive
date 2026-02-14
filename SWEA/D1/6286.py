A = [1, 1]
for i in range(1, 9):
    A += [A[i - 1] + A[i]]
print(A)