import math

N = int(input())
result = N

for p in range(2, int(math.sqrt(N)) + 1):
    if N % p == 0:
        result -= result / p

        while N % p == 0:
            N /= p

if N > 1:
    result -= result / N

print(int(result))