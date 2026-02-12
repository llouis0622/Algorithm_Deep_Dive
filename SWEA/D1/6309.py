import random

A = list(range(1, 30))
B, C = [], []
for _ in range(10):
    B.append(random.choice(A))
for _ in range(15):
    C.append(random.choice(A))
print(B)
print(C)
print(list(set(B) & set(C)))