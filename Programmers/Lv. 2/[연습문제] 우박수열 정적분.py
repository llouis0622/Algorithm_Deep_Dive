def solution(k, ranges):
    num = [k]
    while num[-1] != 1:
        if num[-1] % 2 == 0:
            num.append(num[-1] // 2)
        else:
            num.append(num[-1] * 3 + 1)
    n = len(num) - 1
    temp = []
    for i in range(n):
        temp.append((num[i] + num[i + 1]) / 2)
    check = [0]
    for a in temp:
        check.append(check[-1] + a)
    ans = []
    for a, b in ranges:
        start = a
        end = n + b
        if start > end:
            ans.append(-1.0)
        else:
            res = check[end] - check[start]
            ans.append(res)
    return ans