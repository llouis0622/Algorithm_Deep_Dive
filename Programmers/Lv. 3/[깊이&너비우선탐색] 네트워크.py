def DFS(node, visited, computers, n):
    stack = [node]
    while stack:
        cur = stack.pop()
        for i in range(n):
            if computers[cur][i] == 1 and not visited[i]:
                visited[i] = True
                stack.append(i)


def solution(n, computers):
    visited = [False] * n
    cnt = 0
    for i in range(n):
        if not visited[i]:
            visited[i] = True
            DFS(i, visited, computers, n)
            cnt += 1
    return cnt