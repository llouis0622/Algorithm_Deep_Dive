import math

N = list(map(int, input().split(', ')))
print(*[f'{i * 2 * math.pi:.2f}' for i in N], sep=', ')