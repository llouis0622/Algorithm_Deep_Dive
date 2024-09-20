def solution(price, money, count):
    cost = price * count * (count + 1) // 2
    num = cost - money
    return max(0, num)