class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ans = []
        t, b = 0, len(matrix) - 1
        l, r = 0, len(matrix[0]) - 1
        while t <= b and l <= r:
            for col in range(l, r + 1):
                ans.append(matrix[t][col])
            t += 1
            for row in range(t, b + 1):
                ans.append(matrix[row][r])
            r -= 1
            if t <= b:
                for col in range(r, l - 1, -1):
                    ans.append(matrix[b][col])
                b -= 1
            if l <= r:
                for row in range(b, t - 1, -1):
                    ans.append(matrix[row][l])
                l += 1
        return ans
