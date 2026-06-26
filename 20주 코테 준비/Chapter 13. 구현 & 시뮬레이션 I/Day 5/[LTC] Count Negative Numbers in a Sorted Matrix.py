class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        row, col, ans = m - 1, 0, 0
        while row >= 0 and col < n:
            if grid[row][col] < 0:
                ans += n - col
                row -= 1
            else:
                col += 1
        return ans
