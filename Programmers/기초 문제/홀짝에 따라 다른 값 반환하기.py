def solution(n):
    ans = 0
    if n % 2 == 1:
        for i in range(1, n + 1, 2):
            ans += i
    else:
        for i in range(2, n + 1, 2):
            ans += i * i
    return ans