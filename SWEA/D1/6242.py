B = ['A', 'A', 'A', 'O', 'B', 'B', 'O', 'AB', 'AB', 'O']
A = {}
for i in B:
    if i in A:
        A[i] += 1
    else:
        A[i] = 1
print(A)