def solution(num_list):
    mul = 1
    sum = 0
    for i in num_list:
        mul *= i
        sum += i
    if mul < sum * sum:
        return 1
    else:
        return 0