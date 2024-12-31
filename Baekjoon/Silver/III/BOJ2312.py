def prime(n):
    lst = {}
    num = 2
    while n > 1:
        while n % num == 0:
            if num in lst:
                lst[num] += 1
            else:
                lst[num] = 1
            n //= num
        num += 1
        if num * num > n:
            if n > 1:
                lst[n] = 1
            break
    return lst


T = int(input())
res = []
for _ in range(T):
    n = int(input())
    lst = prime(n)
    for p, c in sorted(lst.items()):
        res.append(f"{p} {c}")
print("\n".join(res))