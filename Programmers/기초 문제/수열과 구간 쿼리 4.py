def solution(arr, queries):
    for s, e, k in queries:
        for i in range(s, e + 1):
            if k != 0 and i % k == 0:
                arr[i] += 1
    return arr