from collections import deque
import heapq


def solution(priorities, location):
    ans = 0
    q = deque((priority, idx) for idx, priority in enumerate(priorities))
    pq = [-priority for priority in priorities]
    heapq.heapify(pq)
    while q and pq:
        if q[0][0] == -pq[0]:
            ans += 1
            if q[0][1] == location:
                return ans
            q.popleft()
            heapq.heappop(pq)
        else:
            q.append(q.popleft())
    return ans