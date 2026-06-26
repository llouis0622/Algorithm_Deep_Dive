from functools import lru_cache


def solution(board, aloc, bloc):
    n, m = len(board), len(board[0])

    @lru_cache(None)
    def dfs(ax, ay, bx, by, turn, state):
        arr = [[0] * m for _ in range(n)]
        bit = 0
        for i in range(n):
            for j in range(m):
                arr[i][j] = (state >> bit) & 1
                bit += 1
        x, y = (ax, ay) if turn == 0 else (bx, by)
        if arr[x][y] == 0:
            return (False, 0)
        win = False
        min_win = float("inf")
        max_lose = 0
        for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and arr[nx][ny]:
                num = state & ~(1 << (x * m + y))
                if turn == 0:
                    opp_win, cnt = dfs(nx, ny, bx, by, 1, num)
                else:
                    opp_win, cnt = dfs(ax, ay, nx, ny, 0, num)
                if not opp_win:
                    win = True
                    min_win = min(min_win, cnt + 1)
                elif not win:
                    max_lose = max(max_lose, cnt + 1)
        if win:
            return (True, min_win)
        return (False, max_lose)

    state = 0
    bit = 0
    for i in range(n):
        for j in range(m):
            if board[i][j]:
                state |= 1 << bit
            bit += 1
    return dfs(aloc[0], aloc[1], bloc[0], bloc[1], 0, state)[1]
