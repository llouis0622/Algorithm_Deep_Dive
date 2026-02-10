A = [2, 4, 6, 8, 10]
print(A)


def find(n):
    if n in A:
        print(f'{n} => True')
    else:
        print(f'{n} => False')


find(5)
find(10)