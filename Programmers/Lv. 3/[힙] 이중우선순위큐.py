import heapq


def solution(operations):
    min_h, max_h = [], []
    cnt = {}
    for i in operations:
        cmd, x = i.split()
        if cmd == 'I':
            z = int(x)
            heapq.heappush(min_h, z)
            heapq.heappush(max_h, -z)
            cnt[z] = cnt.get(z, 0) + 1
        else:
            if x == '1':
                while max_h and cnt.get(-max_h[0], 0) == 0:
                    heapq.heappop(max_h)
                if max_h:
                    z = -heapq.heappop(max_h)
                    c = cnt[z] - 1
                    if c:
                        cnt[z] = c
                    else:
                        del cnt[z]
            else:
                while min_h and cnt.get(min_h[0], 0) == 0:
                    heapq.heappop(min_h)
                if min_h:
                    z = heapq.heappop(min_h)
                    c = cnt[z] - 1
                    if c:
                        cnt[z] = c
                    else:
                        del cnt[z]
    while min_h and cnt.get(min_h[0], 0) == 0:
        heapq.heappop(min_h)
    while max_h and cnt.get(-max_h[0], 0) == 0:
        heapq.heappop(max_h)
    if not min_h or not max_h:
        return [0, 0]
    return [-max_h[0], min_h[0]]