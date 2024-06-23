def solution(n):
    ans = []
    while n != 1:
        ans.append(n)
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
    ans.append(1)
    return ans