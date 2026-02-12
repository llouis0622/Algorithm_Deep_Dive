num = list(range(1, 11))
A = []
for i in num:
    if i % 2 == 0:
        A.append(i ** 2)
print(A)