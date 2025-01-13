import sys
input = sys.stdin.read


def matrix(temp):
    n = len(temp)
    dp = [[0] * n for _ in range(n)]
    for l in range(2, n + 1):
        for i in range(n - l + 1):
            j = i + l - 1
            dp[i][j] = float('inf')
            for k in range(i, j):
                num = (dp[i][k] + dp[k + 1][j] + temp[i][0] * temp[k][1] * temp[j][1])
                dp[i][j] = min(dp[i][j], num)
    return dp[0][n - 1]


data = input().strip().split("\n")
n = int(data[0])
temp = [tuple(map(int, line.split())) for line in data[1:]]
print(matrix(temp))