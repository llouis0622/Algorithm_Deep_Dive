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