import heapq


def solution(n, k, enemy):
    heap = []
    for i, e in enumerate(enemy):
        heapq.heappush(heap, -e)
        n -= e
        if n < 0:
            if k == 0:
                return i
            temp = -heapq.heappop(heap)
            n += temp
            k -= 1
    return len(enemy)