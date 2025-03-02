import sys

N = int(sys.stdin.readline().strip())
DP = [False] * (N + 1)
if N >= 1:
    DP[1] = True
if N >= 2:
    DP[2] = False
if N >= 3:
    DP[3] = True
if N >= 4:
    DP[4] = True
for i in range(5, N + 1):
    DP[i] = not(DP[i - 1] and DP[i - 3] and DP[i - 4])
print("SK" if DP[N] else "CY")