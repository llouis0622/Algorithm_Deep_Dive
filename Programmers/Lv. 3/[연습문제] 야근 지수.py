import heapq


def solution(n, works):
    if sum(works) <= n:
        return 0
    works = [-w for w in works]
    heapq.heapify(works)
    for _ in range(n):
        temp = heapq.heappop(works)
        heapq.heappush(works, temp + 1)
    return sum(w ** 2 for w in works)