import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
vip = {int(sys.stdin.readline()) for _ in range(m)}
dp = [1] * (n + 1)
if n > 1:
    dp[2] = 2
for i in range(3, n + 1):
    dp[i] = dp[i - 1] + dp[i - 2]
res = 1
temp = 0
for v in sorted(vip):
    length = v - temp - 1
    if length > 0:
        res *= dp[length]
    temp = v
length = n - temp
if length > 0:
    res *= dp[length]
print(res)