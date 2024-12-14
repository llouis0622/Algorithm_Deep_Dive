from itertools import permutations

N, M = map(int, input().split())
num = sorted(map(int, input().split()))
for i in permutations(num, M):
    print(" ".join(map(str, i)))