def solution(n):
    lst = []
    num = 2
    while n >= num:
        if n % num == 0:
            if num not in lst:
                lst.append(num)
            n //= num
        else:
            num += 1
    return lst