from itertools import combinations

L, C = map(int, input().split())
lst = sorted(input().split())
temp = {'a', 'e', 'i', 'o', 'u'}
for comb in combinations(lst, L):
    num = sum(1 for ch in comb if ch in temp)
    if num >= 1 and (L - num) >= 2:
        print(''.join(comb))