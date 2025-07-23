import sys
import heapq

input = sys.stdin.readline

n, k = map(int, input().split())
jewels = [tuple(map(int, input().split())) for _ in range(n)]
bags = [int(input()) for _ in range(k)]
jewels.sort()
bags.sort()
ans = 0
pq = []
j = 0
for i in bags:
    while j < n and jewels[j][0] <= i:
        heapq.heappush(pq, -jewels[j][1])
        j += 1
    if pq:
        ans += -heapq.heappop(pq)
print(ans)