from collections import deque


class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        graph = [[] for _ in range(n)]
        degree = [0] * n
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
            degree[u] += 1
            degree[v] += 1
        q = deque()
        for i in range(n):
            if degree[i] == 1:
                q.append(i)
        temp = n
        while temp > 2:
            num = len(q)
            temp -= num
            for _ in range(num):
                cur = q.popleft()
                for i in graph[cur]:
                    degree[i] -= 1
                    if degree[i] == 1:
                        q.append(i)
        return list(q)
