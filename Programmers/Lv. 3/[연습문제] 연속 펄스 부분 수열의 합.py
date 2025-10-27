def solution(sequence):
    num1 = 0
    num2 = 0
    ans = -10 ** 20
    for i, x in enumerate(sequence):
        temp1 = x if i % 2 == 0 else -x
        temp2 = -temp1
        num1 = max(temp1, num1 + temp1)
        num2 = max(temp2, num2 + temp2)
        if num1 > ans:
            ans = num1
        if num2 > ans:
            ans = num2
    return ans