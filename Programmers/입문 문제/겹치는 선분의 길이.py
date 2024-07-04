def solution(lines):
    lst = [0] * 201
    for i, j in lines:
        for i in range(i + 100, j + 100):
            lst[i] += 1
    ans = 0
    for i in lst:
        if i > 1:
            ans += 1
    return ans