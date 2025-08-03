s = input()
MOD = 1000000
n = len(s)
if s[0] == '0':
    print(0)
    exit()
dp = [0] * (n + 1)
dp[0] = 1
dp[1] = 1
for i in range(2, n + 1):
    num = int(s[i - 1])
    temp = int(s[i - 2:i])
    if 1 <= num <= 9:
        dp[i] += dp[i - 1]
    if 10 <= temp <= 26:
        dp[i] += dp[i - 2]
    dp[i] %= MOD
print(dp[n])