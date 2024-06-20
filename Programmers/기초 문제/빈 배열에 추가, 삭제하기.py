def solution(arr, flag):
    ans = []
    for i in range(len(arr)):
        if flag[i]:
            ans.extend([arr[i]] * (arr[i] * 2))
        else:
            ans = ans[:-arr[i]]
    return ans