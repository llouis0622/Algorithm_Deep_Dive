from collections import deque


def solution(board):
    n = len(board)
    s = ((0, 0), (0, 1))
    queue = deque([(s, 0)])
    visited = {s}

    def get_next(pos):
        (x1, y1), (x2, y2) = pos
        res = []
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nx1, ny1 = x1 + dx, y1 + dy
            nx2, ny2 = x2 + dx, y2 + dy
            if (0 <= nx1 < n and 0 <= ny1 < n and 0 <= nx2 < n and 0 <= ny2 < n and board[nx1][ny1] == 0 and board[nx2][ny2] == 0):
                res.append(tuple(sorted(((nx1, ny1), (nx2, ny2)))))
        if x1 == x2:
            for d in (-1, 1):
                if (0 <= x1 + d < n and board[x1 + d][y1] == 0 and board[x2 + d][y2] == 0):
                    res.append(tuple(sorted(((x1, y1), (x1 + d, y1)))))
                    res.append(tuple(sorted(((x2, y2), (x2 + d, y2)))))
        else:
            for d in (-1, 1):
                if (0 <= y1 + d < n and board[x1][y1 + d] == 0 and board[x2][y2 + d] == 0):
                    res.append(tuple(sorted(((x1, y1), (x1, y1 + d)))))
                    res.append(tuple(sorted(((x2, y2), (x2, y2 + d)))))
        return res

    while queue:
        pos, cost = queue.popleft()
        if (n - 1, n - 1) in pos:
            return cost
        for nxt in get_next(pos):
            if nxt not in visited:
                visited.add(nxt)
                queue.append((nxt, cost + 1))
