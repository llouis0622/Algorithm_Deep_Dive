def solution(arr):
    ans = []
    for i in arr:
        ans.extend([i] * i)
    return ans