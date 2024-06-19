def solution(arr):
    ans = []
    i = 0
    while i < len(arr):
        if not ans:
            ans.append(arr[i])
            i += 1
        elif ans[-1] == arr[i]:
            ans.pop()
            i += 1
        else:
            ans.append(arr[i])
            i += 1
    return ans if ans else [-1]