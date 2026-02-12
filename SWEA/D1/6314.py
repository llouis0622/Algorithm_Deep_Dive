num = list(range(1, 11))
A = list(map(lambda x: x, filter(lambda x: x % 2 == 0, num)))
print(A)