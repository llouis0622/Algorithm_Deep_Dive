class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        n = len(matrix[0])
        h = [0] * (n + 1)
        ans = 0
        for row in matrix:
            for i in range(n):
                if row[i] == "1":
                    h[i] += 1
                else:
                    h[i] = 0
            stack = [-1]
            for i in range(n + 1):
                while h[i] < h[stack[-1]]:
                    num = h[stack.pop()]
                    w = i - stack[-1] - 1
                    ans = max(ans, num * w)
                stack.append(i)
        return ans
