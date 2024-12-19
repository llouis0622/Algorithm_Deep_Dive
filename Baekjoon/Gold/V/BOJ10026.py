import sys
sys.setrecursionlimit(10 ** 6)

n = int(input())
graph = []
for _ in range(n):
    graph.append(list(input()))


def DFS(graph, color, x, y, blind):
    if x < 0 or x >= n or y < 0 or y >= n:
        return False
    if blind:
        if (graph[x][y] == 'R' or graph[x][y] == 'G') and (color == 'R' or color == 'G'):
            color = graph[x][y]
    if graph[x][y] == color:
        graph[x][y] = '#'
        DFS(graph, color, x - 1, y, blind)
        DFS(graph, color, x + 1, y, blind)
        DFS(graph, color, x, y - 1, blind)
        DFS(graph, color, x, y + 1, blind)
        return True
    return False


normal = 0
odd = 0
normal_lst = [_list.copy() for _list in graph]
odd_lst = [_list.copy() for _list in graph]
for i in range(n):
    for j in range(n):
        if normal_lst[i][j] != '#':
            if DFS(normal_lst, normal_lst[i][j], i, j, False):
                normal += 1
        if odd_lst[i][j] != '#':
            if DFS(odd_lst, odd_lst[i][j], i, j, True):
                odd += 1
print(normal, odd, end=' ')