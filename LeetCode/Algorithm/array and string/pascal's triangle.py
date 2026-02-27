class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        A = []
        for i in range(numRows):
            x = [1] * (i + 1)
            for j in range(1, i):
                x[j] = A[i - 1][j - 1] + A[i - 1][j]
            A.append(x)
        return A