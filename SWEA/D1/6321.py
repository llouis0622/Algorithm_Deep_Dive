N = int(input())


def check(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


print('소수입니다.' if check(N) is True else '소수가 아닙니다.')