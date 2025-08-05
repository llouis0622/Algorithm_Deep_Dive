import sys
from collections import Counter

M, N = map(int, sys.stdin.readline().split())
temp = []
for _ in range(M):
    arr = list(map(int, sys.stdin.readline().split()))
    rank = {v: i for i, v in enumerate(sorted(set(arr)))}
    temp.append(tuple(rank[p] for p in arr))
cnt = Counter(temp)
ans = sum(v * (v - 1) // 2 for v in cnt.values())
print(ans)