def solution(i, j, k):
    ans = 0
    for num in range(i, j + 1):
        ans += str(num).count(str(k))
    return ans