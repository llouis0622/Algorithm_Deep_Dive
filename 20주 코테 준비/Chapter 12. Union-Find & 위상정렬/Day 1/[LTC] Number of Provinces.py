class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        visited = [False] * n

        def dfs(node):
            visited[node] = True
            for nxt in range(n):
                if isConnected[node][nxt] and not visited[nxt]:
                    dfs(nxt)

        ans = 0
        for i in range(n):
            if not visited[i]:
                dfs(i)
                ans += 1
        return ans
