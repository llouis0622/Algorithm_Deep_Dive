from collections import deque


class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        graph = [[] for _ in range(n + 1)]
        indegree = [0] * (n + 1)
        for prev, nxt in relations:
            graph[prev].append(nxt)
            indegree[nxt] += 1
        q = deque()
        dp = [0] * (n + 1)
        for i in range(1, n + 1):
            if indegree[i] == 0:
                q.append(i)
                dp[i] = time[i - 1]
        while q:
            cur = q.popleft()
            for nxt in graph[cur]:
                dp[nxt] = max(dp[nxt], dp[cur] + time[nxt - 1])
                indegree[nxt] -= 1
                if indegree[nxt] == 0:
                    q.append(nxt)
        return max(dp)
