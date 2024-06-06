def solution(arr, queries):
    ans = []
    for s, e, k in queries:
        INF = float('inf')
        bl = False
        for i in range(s, e + 1):
            if arr[i] > k:
                if arr[i] < INF:
                    INF = arr[i]
                bl = True
        if bl:
            ans.append(INF)
        else:
            ans.append(-1)
    return ans