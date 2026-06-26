class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        m, n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                temp = 0
                for dx, dy in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
                    ni, nj = i + dx, j + dy
                    if 0 <= ni < m and 0 <= nj < n and abs(board[ni][nj]) == 1:
                        temp += 1
                if board[i][j] == 1 and (temp < 2 or temp > 3):
                    board[i][j] = -1
                if board[i][j] == 0 and temp == 3:
                    board[i][j] = 2
        for i in range(m):
            for j in range(n):
                if board[i][j] > 0:
                    board[i][j] = 1
                else:
                    board[i][j] = 0
