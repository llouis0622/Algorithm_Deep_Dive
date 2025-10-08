def solution(rows, columns, queries):
    g = [[i * columns + j + 1 for j in range(columns)] for i in range(rows)]
    ans = []
    for x1, y1, x2, y2 in queries:
        x1 -= 1
        y1 -= 1
        x2 -= 1
        y2 -= 1
        temp = g[x1][y1]
        m = temp
        for x in range(x1 + 1, x2 + 1):
            g[x - 1][y1] = g[x][y1]
            if g[x - 1][y1] < m:
                m = g[x - 1][y1]
        for y in range(y1 + 1, y2 + 1):
            g[x2][y - 1] = g[x2][y]
            if g[x2][y - 1] < m:
                m = g[x2][y - 1]
        for x in range(x2 - 1, x1 - 1, -1):
            g[x + 1][y2] = g[x][y2]
            if g[x + 1][y2] < m:
                m = g[x + 1][y2]
        for y in range(y2 - 1, y1 - 1, -1):
            g[x1][y + 1] = g[x1][y]
            if g[x1][y + 1] < m:
                m = g[x1][y + 1]
        g[x1][y1 + 1] = temp
        if temp < m:
            m = temp
        ans.append(m)
    return ans