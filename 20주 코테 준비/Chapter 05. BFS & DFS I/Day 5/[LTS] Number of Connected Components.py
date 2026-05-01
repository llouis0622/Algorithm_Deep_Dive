from collections import deque


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = [[] for _ in range(n)]
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        visited = [False] * n
        cnt = 0
        for i in range(n):
            if visited[i]:
                continue
            cnt += 1
            q = deque([i])
            visited[i] = True
            while q:
                cur = q.popleft()
                for x in graph[cur]:
                    if not visited[x]:
                        visited[x] = True
                        q.append(x)
        return cnt
