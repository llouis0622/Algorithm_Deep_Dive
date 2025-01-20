from collections import defaultdict, deque


def CCW(ax, ay, bx, by, cx, cy):
    return (bx - ax) * (cy - ay) - (by - ay) * (cx - ax)


def intersect(x1, y1, x2, y2, x3, y3, x4, y4):
    CCW1 = CCW(x1, y1, x2, y2, x3, y3)
    CCW2 = CCW(x1, y1, x2, y2, x4, y4)
    CCW3 = CCW(x3, y3, x4, y4, x1, y1)
    CCW4 = CCW(x3, y3, x4, y4, x2, y2)
    if CCW1 * CCW2 <= 0 and CCW3 * CCW4 <= 0:
        if max(x1, x2) >= min(x3, x4) and max(x3, x4) >= min(x1, x2) and max(y1, y2) >= min(y3, y4) and max(y3, y4) >= min(y1, y2):
            return True
    return False


def find(n, seg):
    dict = defaultdict(list)
    for i in range(n):
        for j in range(i + 1, n):
            if intersect(*seg[i], *seg[j]):
                dict[i].append(j)
                dict[j].append(i)
    visited = [False] * n
    lst = []
    for i in range(n):
        if not visited[i]:
            queue = deque([i])
            visited[i] = True
            size = 0
            while queue:
                cur = queue.popleft()
                size += 1
                for n in dict[cur]:
                    if not visited[n]:
                        visited[n] = True
                        queue.append(n)
            lst.append(size)
    return len(lst), max(lst)


n = int(input())
seg = [tuple(map(int, input().split())) for _ in range(n)]
num, temp = find(n, seg)
print(num)
print(temp)