L = [(i + 1) for i in range(20)]
for _ in range(10):
    A, B = map(int, input().split())
    L = L[:A-1] + list(reversed(L[A-1:B])) + L[B:]
for i in L:
    print(i, end=' ')