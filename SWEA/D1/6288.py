N = list(range(1, 21))
A = [i ** 2 for i in N if i % 3 != 0 or i % 5 != 0]
print(A)