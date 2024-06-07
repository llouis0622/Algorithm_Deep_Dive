def solution(l, r):
    ans = []
    for i in range(l, r + 1):
        nstr = str(i)
        if all(char in '05' for char in nstr):
            ans.append(i)
    if not ans:
        return [-1]
    return ans