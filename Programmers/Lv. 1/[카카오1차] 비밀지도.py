def solution(n, arr1, arr2):
    ans = []
    for i in range(n):
        arr = arr1[i] | arr2[i]
        res = ""
        for j in range(n):
            if arr & (1 << (n - 1 - j)):
                res += "#"
            else:
                res += " "
        ans.append(res)
    return ans