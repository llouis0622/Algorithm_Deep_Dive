def solution(N, stages):
    rate = []
    total = len(stages)
    for i in range(1, N + 1):
        res = stages.count(i)
        if total > 0:
            arr = res / total
        else:
            arr = 0
        rate.append((i, arr))
        total -= res
    rate.sort(key=lambda x: (-x[1], x[0]))
    return [i for i, rate in rate]