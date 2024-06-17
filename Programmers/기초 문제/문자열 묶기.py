def solution(strArr):
    ans = {}
    for i in strArr:
        length = len(i)
        if length in ans:
            ans[length] += 1
        else:
            ans[length] = 1
    return max(ans.values())