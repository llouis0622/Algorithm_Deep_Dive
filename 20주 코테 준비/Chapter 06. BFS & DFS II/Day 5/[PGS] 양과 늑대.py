def solution(info, edges):
    graph = [[] for _ in range(len(info))]
    for p, c in edges:
        graph[p].append(c)
    ans = 0

    def dfs(sheep, wolf, cur, num):
        nonlocal ans
        if info[cur] == 0:
            sheep += 1
        else:
            wolf += 1
        if sheep <= wolf:
            return
        ans = max(ans, sheep)
        temp = num[:]
        temp.remove(cur)
        for c in graph[cur]:
            temp.append(c)
        for nxt in temp:
            dfs(sheep, wolf, nxt, temp)

    dfs(0, 0, 0, [0])
    return ans
