from collections import deque


def solution(n, roads, sources, destination):
    s = [[] for _ in range(n + 1)]
    for a, b in roads:
        s[a].append(b)
        s[b].append(a)
    temp = [-1] * (n + 1)
    q = deque([destination])
    temp[destination] = 0
    while q:
        cur = q.popleft()
        for i in s[cur]:
            if temp[i] == -1:
                temp[i] = temp[cur] + 1
                q.append(i)
    return [temp[i] for i in sources]