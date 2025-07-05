from math import gcd


def GCD(numbers):
    res = numbers[0]
    for num in numbers[1:]:
        res = gcd(res, num)
    return res


def check(g, arr):
    for num in arr:
        if num % g == 0:
            return False
    return True


def solution(arrayA, arrayB):
    gcdA = GCD(arrayA)
    gcdB = GCD(arrayB)
    ans = []
    if check(gcdA, arrayB):
        ans.append(gcdA)
    if check(gcdB, arrayA):
        ans.append(gcdB)
    return max(ans) if ans else 0