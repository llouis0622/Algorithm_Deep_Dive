def check(arr):
    num1, num2 = 0, 0
    for i in arr:
        num2, num1 = num1, max(num1, num2 + i)
    return num1


def solution(sticker):
    n = len(sticker)
    if n == 1:
        return sticker[0]
    if n == 2:
        return max(sticker)
    return max(check(sticker[:-1]), check(sticker[1:]))