def search(n, k):
    length = 0
    num = 1
    cnt = 9
    while length + num * cnt < k and n >= 10 ** (num - 1):
        length += num * cnt
        num += 1
        cnt *= 10
    if length + num * (n - 10 ** (num - 1) + 1) < k:
        return -1
    temp = k - length - 1
    start = 10 ** (num - 1)
    number = start + temp // num
    return int(str(number)[temp % num])


n, k = map(int, input().split())
print(search(n, k))