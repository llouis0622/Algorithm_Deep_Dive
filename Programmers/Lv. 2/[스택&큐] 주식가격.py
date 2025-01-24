def solution(prices):
    v = [0] * len(prices)
    s = []
    size = len(prices)
    for i in range(size):
        while s and prices[s[-1]] > prices[i]:
            v[s[-1]] = i - s[-1]
            s.pop()
        s.append(i)
    while s:
        v[s[-1]] = size - 1 - s[-1]
        s.pop()
    return v