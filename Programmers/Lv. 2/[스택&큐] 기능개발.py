from collections import deque


def solution(progresses, speeds):
    v = []
    q = deque(range(len(speeds)))
    while q:
        num = 0
        for i in range(len(speeds)):
            progresses[i] += speeds[i]
        while q and progresses[q[0]] >= 100:
            num += 1
            q.popleft()
        if num != 0:
            v.append(num)
    return v