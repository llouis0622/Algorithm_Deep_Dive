import sys
import math

P1, P2, P3, X1, X2, X3 = map(int, sys.stdin.readline().split())


def CRT(P1, X1, P2, X2):
    g = math.gcd(P1, P2)
    if (X2 - X1) % g != 0:
        return -1, -1
    lcm = (P1 // g) * P2
    k = ((X2 - X1) // g) * pow(P1 // g, -1, P2 // g) % (P2 // g)
    N = X1 + k * P1
    return N, lcm


N, lcm = CRT(P1, X1, P2, X2)
if N == -1 or N >= 1_000_000_000:
    print(-1)
    exit()

N, lcm = CRT(lcm, N, P3, X3)
if N == -1 or N >= 1_000_000_000:
    print(-1)
else:
    print(N)