from itertools import product

N, M = map(int, input().split())
lst = sorted(list(map(int, input().split())))
for prod in product(lst, repeat=M):
    print(*prod)