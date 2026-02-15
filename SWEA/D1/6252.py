import random

A = []
while len(A) < 6:
    N = random.randint(1, 45)
    if N not in A:
        A.append(N)
A.sort()
print(A)