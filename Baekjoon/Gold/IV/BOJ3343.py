import sys
import math

N, A, B, C, D = map(int, sys.stdin.readline().split())
if B * C < D * A:
    A, C = C, A
    B, D = D, B
ans = float('inf')
for x in range(C):
    y = math.ceil((N - A * x) / C)
    if y < 0:
        y = 0
        ans = min(ans, B * x + D * y)
        break
    ans = min(ans, B * x + D * y)
print(ans)