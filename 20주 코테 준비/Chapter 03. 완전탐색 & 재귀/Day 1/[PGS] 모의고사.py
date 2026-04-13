def solution(answers):
    num1 = [1, 2, 3, 4, 5]
    num2 = [2, 1, 2, 3, 2, 4, 2, 5]
    num3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    check1, check2, check3 = 0, 0, 0
    for i in range(len(answers)):
        if answers[i] == num1[i % len(num1)]:
            check1 += 1
        if answers[i] == num2[i % len(num2)]:
            check2 += 1
        if answers[i] == num3[i % len(num3)]:
            check3 += 1
    arr = [check1, check2, check3]
    temp = max(arr)
    res = []
    for i in range(3):
        if arr[i] == temp:
            res.append(i + 1)
    return res
