def solution(intStrs, k, s, l):
    ans = []
    for i in intStrs:
        str = i[s:s + l]
        num = int(str)
        if num > k:
            ans.append(num)
    return ans