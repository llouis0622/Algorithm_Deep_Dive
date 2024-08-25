def solution(n):
    if n < 2:
        return 0
    num = [True] * (n + 1)
    num[0] = num[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if num[i]:
            for j in range(i * i, n + 1, i):
                num[j] = False
    return sum(num)