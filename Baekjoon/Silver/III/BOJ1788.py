import sys

n = int(sys.stdin.readline())
MOD = 1_000_000_000
a, b = 0, 1
for _ in range(abs(n)):
    a, b = b % MOD, (a + b) % MOD
print(1 if n > 0 or n % 2 == 0 else -1)
print(a)