import sys
from itertools import combinations

input = sys.stdin.read
data = input().splitlines()

N, M = map(int, data[0].split())
arr = sorted(map(int, data[1].split()))

for comb in combinations(arr, M):
    print(*comb)