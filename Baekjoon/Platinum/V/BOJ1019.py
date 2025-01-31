def page(n):
    cnt = [0] * 10
    num = 1
    temp = 1
    while num <= n:
        while n % 10 != 9 and num <= n:
            for digit in str(n):
                cnt[int(digit)] += temp
            n -= 1
        if n < num:
            break
        while num % 10 != 0 and num <= n:
            for digit in str(num):
                cnt[int(digit)] += temp
            num += 1
        if num > n:
            break
        for i in range(10):
            cnt[i] += ((n // 10) - (num // 10) + 1) * temp
        num //= 10
        n //= 10
        temp *= 10
    return cnt


n = int(input())
print(" ".join(map(str, page(n))))