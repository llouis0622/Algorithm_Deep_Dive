def solution(numbers, n):
    ans = 0
    for i in range(len(numbers)):
        if ans > n:
            break
        ans += numbers[i]
    return ans