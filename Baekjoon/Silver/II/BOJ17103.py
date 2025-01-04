def prime(n):
    p = [True] * (n + 1)
    p[0] = p[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if p[i]:
            for j in range(i * i, n + 1, i):
                p[j] = False
    return p


def goldbach(n, p):
    cnt = 0
    for i in range(2, n // 2 + 1):
        if p[i] and p[n - i]:
            cnt += 1
    return cnt


T = int(input())
case = [int(input()) for _ in range(T)]
temp = max(case)
p = prime(temp)
res = [goldbach(n, p) for n in case]
print("\n".join(map(str, res)))