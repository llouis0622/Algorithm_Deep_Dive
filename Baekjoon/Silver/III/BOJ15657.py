from itertools import combinations_with_replacement

N, M = map(int, input().split())
lst = sorted(list(map(int, input().split())))
for cwr in combinations_with_replacement(lst, M):
    print(*cwr)