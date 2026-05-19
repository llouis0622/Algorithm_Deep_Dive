def solution(triangle):
    DP = [row[:] for row in triangle]
    for i in range(1, len(DP)):
        for j in range(len(DP[i])):
            if j == 0:
                DP[i][j] += DP[i - 1][j]
            elif j == len(DP[i]) - 1:
                DP[i][j] += DP[i - 1][j - 1]
            else:
                DP[i][j] += max(DP[i - 1][j - 1], DP[i - 1][j])
    return max(DP[-1])


def solution(triangle):
    DP = [row[:] for row in triangle]
    for i in range(len(DP) - 2, -1, -1):
        for j in range(len(DP[i])):
            DP[i][j] += max(DP[i + 1][j], DP[i + 1][j + 1])
    return DP[0][0]


def solution(triangle):
    DP = triangle[-1][:]
    for i in range(len(triangle) - 2, -1, -1):
        for j in range(len(triangle[i])):
            DP[j] = triangle[i][j] + max(DP[j], DP[j + 1])
    return DP[0]