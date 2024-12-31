import math


def LCM(a, b):
    return abs(a * b) // math.gcd(a, b)


T = int(input())
res = []
for _ in range(T):
    a, b = map(int, input().split())
    res.append(LCM(a, b))
print("\n".join(map(str, res)))