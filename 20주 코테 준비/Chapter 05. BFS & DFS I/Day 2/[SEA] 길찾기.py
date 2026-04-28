from collections import deque

for _ in range(10):
    T, N = map(int, input().split())
    arr = list(map(int, input().split()))
    graph = [[] for _ in range(100)]
    for i in range(0, len(arr), 2):
        a, b = arr[i], arr[i + 1]
        graph[a].append(b)
    visited = [False] * 100
    q = deque([0])
    visited[0] = True
    ans = 0
    while q:
        cur = q.popleft()
        if cur == 99:
            ans = 1
            break
        for x in graph[cur]:
            if not visited[x]:
                visited[x] = True
                q.append(x)
    print(f'#{T} {ans}')
