from collections import deque


def solution(x, y, n):
    v = set()
    q = deque()
    q.append((x, 0))
    while q:
        cur, cnt = q.popleft()
        if cur == y:
            return cnt
        for num in [cur + n, cur * 2, cur * 3]:
            if num <= y and num not in v:
                v.add(num)
                q.append((num, cnt + 1))
    return -1