import sys
import heapq
from collections import defaultdict
input = sys.stdin.readline


def dual_pq(operation):
    min_heap = []
    max_heap = []
    cnt = defaultdict(int)
    for op in operation:
        cmd, num = op.split()
        num = int(num)
        if cmd == 'I':
            heapq.heappush(min_heap, num)
            heapq.heappush(max_heap, -num)
            cnt[num] += 1
        elif cmd == 'D':
            if num == 1:
                while max_heap and cnt[-max_heap[0]] == 0:
                    heapq.heappop(max_heap)
                if max_heap:
                    max_val = -heapq.heappop(max_heap)
                    cnt[max_val] -= 1
            elif num == -1:
                while min_heap and cnt[min_heap[0]] == 0:
                    heapq.heappop(min_heap)
                if min_heap:
                    min_val = heapq.heappop(min_heap)
                    cnt[min_val] -= 1
    while min_heap and cnt[min_heap[0]] == 0:
        heapq.heappop(min_heap)
    while max_heap and cnt[-max_heap[0]] == 0:
        heapq.heappop(max_heap)
    if not min_heap or not max_heap:
        return "EMPTY"
    else:
        return f"{-max_heap[0]} {min_heap[0]}"


T = int(input())
res = []
for _ in range(T):
    k = int(input())
    operation = [input().strip() for _ in range(k)]
    res.append(dual_pq(operation))
print("\n".join(res))