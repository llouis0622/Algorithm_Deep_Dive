import sys
from math import gcd

input = sys.stdin.read
lines = input().splitlines()

T = int(lines[0])
results = []

for line in lines[1:]:
    M, N, x, y = map(int, line.split())
    lcm = M * N // gcd(M, N)
    k = x

    while k <= lcm:
        if (k - 1) % N + 1 == y:
            results.append(k)
            break
        k += M
    else:
        results.append(-1)

for result in results:
    print(f"{result}")