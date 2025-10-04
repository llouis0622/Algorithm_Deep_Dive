import sys

MOD = 1_000_000_007
m = int(sys.stdin.readline())
ans = 0
for _ in range(m):
    n, s = map(int, sys.stdin.readline().split())
    num = pow(n % MOD, MOD - 2, MOD)
    ans = (ans + (s % MOD) * num) % MOD
print(ans)