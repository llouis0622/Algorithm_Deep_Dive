def solution(n):
    ans = 0
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            ans += 1
            if i != n // i:
                ans += 1
    return ans