import heapq


def solution(jobs):
    n = len(jobs)
    temp = [(s, l, m) for m, (s, l) in enumerate(jobs)]
    temp.sort()
    h = []
    t, i, num, ans = 0, 0, 0, 0
    while num < n:
        while i < n and temp[i][0] <= t:
            s, l, idx = temp[i]
            heapq.heappush(h, (l, s, idx))
            i += 1
        if h:
            l, s, idx = heapq.heappop(h)
            t += l
            ans += t - s
            num += 1
        else:
            t = temp[i][0]
    return ans // n