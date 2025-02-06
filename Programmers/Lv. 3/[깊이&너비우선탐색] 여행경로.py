from collections import defaultdict


def solution(tickets):
    g = defaultdict(list)
    for i, j in sorted(tickets, reverse=True):
        g[i].append(j)
    stack = ["ICN"]
    path = []
    while stack:
        while g[stack[-1]]:
            stack.append(g[stack[-1]].pop())
        path.append(stack.pop())
    return path[::-1]