def solution(arr, k):
    ans = []
    lst = set()
    for i in arr:
        if i not in lst:
            lst.add(i)
            ans.append(i)
        if len(ans) == k:
            break
    while len(ans) < k:
        ans.append(-1)
    return ans