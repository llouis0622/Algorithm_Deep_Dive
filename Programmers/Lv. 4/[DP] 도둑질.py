def rob(houses):
    cnt = len(houses)
    DP = [0] * cnt
    DP[0], DP[1] = houses[0], max(houses[0], houses[1])
    for i in range(2, cnt):
        DP[i] = max(DP[i - 1], DP[i - 2] + houses[i])
    return DP[-1]


def solution(money):
    return max(rob(money[:-1]), rob(money[1:]))