def solution(k, dungeons):
    ans = 0
    visited = [False] * len(dungeons)


    def dfs(cur, cnt):
        nonlocal ans
        ans = max(ans, cnt)
        for i in range(len(dungeons)):
            temp, cost = dungeons[i]
            if not visited[i] and cur >= temp:
                visited[i] = True
                dfs(cur - cost, cnt + 1)
                visited[i] = False


    dfs(k, 0)
    return ans
