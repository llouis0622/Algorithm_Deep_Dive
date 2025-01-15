from itertools import combinations


def solution(line):
    section = set()
    for (A1, B1, C1), (A2, B2, C2) in combinations(line, 2):
        det = A1 * B2 - A2 * B1
        if det == 0:
            continue
        X = (B1 * C2 - B2 * C1) / det
        Y = (A2 * C1 - A1 * C2) / det
        if X.is_integer() and Y.is_integer():
            section.add((int(X), int(Y)))
    if not section:
        return []
    min_X = min(X for X, Y in section)
    maX_X = max(X for X, Y in section)
    min_Y = min(Y for X, Y in section)
    maX_Y = max(Y for X, Y in section)
    W = maX_X - min_X + 1
    H = maX_Y - min_Y + 1
    G = [['.'] * W for _ in range(H)]
    for X, Y in section:
        G[maX_Y - Y][X - min_X] = '*'
    return [''.join(row) for row in G]