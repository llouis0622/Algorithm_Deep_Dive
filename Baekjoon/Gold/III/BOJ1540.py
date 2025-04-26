import math

N = int(input())
m = math.isqrt(N)
k = N - m * m
print(
    m * (m - 1) * (2 * m - 1) // 6 + k * (k - 1) // 2
    if k <= m
    else m * (m - 1) * (m + 1) // 3 + (k - m) * (k - m - 1) // 2
)