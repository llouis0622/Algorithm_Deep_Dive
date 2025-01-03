def deciaml(n):
    if n == 0:
        return "0"
    res = ""
    while n != 0:
        temp = n % -2
        n //= -2
        if temp < 0:
            temp += 2
            n += 1
        res = str(temp) + res
    return res


n = int(input())
print(deciaml(n))