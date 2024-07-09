def solution(n):
    ans = 0
    for i in range(2, n + 1):
        if any(i % j == 0 for j in range(2, int(i ** 0.5) + 1)):
            ans += 1
    return ans