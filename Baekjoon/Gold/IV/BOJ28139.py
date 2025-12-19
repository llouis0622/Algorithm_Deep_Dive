import sys
import math

input = sys.stdin.readline

n = int(input())
x = [0] * n
y = [0] * n
for i in range(n):
    a, b = map(int, input().split())
    x[i] = a
    y[i] = b
s = 0.0
hypot = math.hypot
for i in range(n):
    a = x[i]
    b = y[i]
    for j in range(i + 1, n):
        s += hypot(a - x[j], b - y[j])
ans = (2.0 / n) * s
print(f"{ans:.10f}")