from math import factorial


def solution(n, k):
    num = list(range(1, n + 1))
    k -= 1
    ans = []
    for i in range(n, 0, -1):
        temp = factorial(i - 1)
        idx = k // temp
        ans.append(num.pop(idx))
        k %= temp
    return ans